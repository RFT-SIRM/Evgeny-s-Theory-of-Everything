// Exact finite source reconstruction for the H10 level-five residual.
// The implementation mirrors the pinned Lean source at
// RFT-SIRM/Evgeny-Theorem@4ccfae17:
//   Graph/Sierpinski.lean  : EdgeB / recursive SG graph
//   Orientation.lean       : first-occurrence A ++ B ++ C vertex order
//   Graph/Faces.lean       : facesExact / fluxEdge / fluxEdges
//   Operator.lean          : pHeO/connection entries and flux axes
//   SU2.lean               : U_a(theta) = c I - i s sigma_a
// The Lean theorem defectO10_succ_num_level5_constant_boundary_unconditional
// identifies the recurrence constant with D_6 - 3 D_5. This program computes
// those two finite traces modulo a prime, coefficient-by-coefficient.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

struct Pt {
  int x, y;
  bool operator==(const Pt& o) const { return x == o.x && y == o.y; }
  bool operator<(const Pt& o) const { return tie(x, y) < tie(o.x, o.y); }
};
using Edge = pair<Pt, Pt>;
static inline bool prod_le(Pt a, Pt b) { return a.x <= b.x && a.y <= b.y; }
static inline Pt shift_pt(Pt p, int dx, int dy) { return {p.x + dx, p.y + dy}; }
static inline Edge undirected(Pt a, Pt b) { return a < b ? Edge{a,b} : Edge{b,a}; }

vector<Pt> vertex_order(int m) {
  if (m == 0) return {{0,0}, {1,0}, {0,1}};
  const auto prev = vertex_order(m - 1);
  const int s = 1 << (m - 1);
  vector<Pt> out;
  set<Pt> seen;
  // List.eraseDups preserves first occurrences: A, then B, then C.
  for (auto [dx,dy] : {pair<int,int>{0,0}, {s,0}, {0,s}}) {
    for (Pt p : prev) {
      Pt q = shift_pt(p, dx, dy);
      if (seen.insert(q).second) out.push_back(q);
    }
  }
  return out;
}

set<Edge> edges(int m) {
  if (m == 0) return {
    undirected({0,0},{1,0}), undirected({1,0},{0,1}), undirected({0,1},{0,0})
  };
  const auto prev = edges(m - 1);
  const int s = 1 << (m - 1);
  set<Edge> out;
  for (auto [dx,dy] : {pair<int,int>{0,0}, {s,0}, {0,s}})
    for (const auto& e : prev)
      out.insert(undirected(shift_pt(e.first,dx,dy), shift_pt(e.second,dx,dy)));
  return out;
}

vector<array<Pt,3>> faces(int m) {
  if (m == 0) return {array<Pt,3>{Pt{0,0}, Pt{1,0}, Pt{0,1}}};
  const auto prev = faces(m - 1);
  const int s = 1 << (m - 1);
  vector<array<Pt,3>> out;
  for (auto [dx,dy] : {pair<int,int>{0,0}, {s,0}, {0,s}})
    for (const auto& f : prev)
      out.push_back({shift_pt(f[0],dx,dy), shift_pt(f[1],dx,dy), shift_pt(f[2],dx,dy)});
  return out;
}

static inline uint32_t add_mod_signed(uint32_t old, long long delta, uint32_t mod) {
  long long v = static_cast<long long>(old) + delta;
  v %= static_cast<long long>(mod);
  if (v < 0) v += mod;
  return static_cast<uint32_t>(v);
}

struct Poly {
  uint32_t re[11][11]{};
  uint32_t im[11][11]{};
  void clear() { memset(this, 0, sizeof(*this)); }
};
struct Transition { int to, dc, ds, re, im; };
struct MatrixRows {
  vector<vector<Transition>> row;
  vector<Pt> points;
  map<Pt,int> point_index;
  int max_degree = 0;
  int max_row_l1 = 0;
  int state_count() const { return static_cast<int>(row.size()); }
};

MatrixRows build_matrix(int m, int axis_kind) {
  MatrixRows M;
  M.points = vertex_order(m);
  const int npt = static_cast<int>(M.points.size());
  for (int i=0; i<npt; ++i) M.point_index[M.points[i]] = i;

  const auto es = edges(m);
  vector<vector<int>> adj(npt);
  vector<int> degree(npt, 0);
  for (const auto& e : es) {
    const int a = M.point_index.at(e.first), b = M.point_index.at(e.second);
    adj[a].push_back(b); adj[b].push_back(a);
    ++degree[a]; ++degree[b];
  }
  for (int d : degree) M.max_degree = max(M.max_degree, d);

  // fluxEdges is facesExact.map fluxEdge; findIdx therefore is the face index.
  const auto fs = faces(m);
  map<Edge,int> flux_index;
  for (int i=0; i<static_cast<int>(fs.size()); ++i) {
    const Pt a = fs[i][0], b = fs[i][1];
    const Edge e = prod_le(a,b) ? Edge{a,b} : Edge{b,a};
    if (!flux_index.count(e)) flux_index[e] = i;
  }

  const auto order = vertex_order(m);
  map<Pt,int> vertex_index;
  for (int i=0; i<static_cast<int>(order.size()); ++i) vertex_index[order[i]] = i;

  M.row.resize(2*npt);
  for (int pi=0; pi<npt; ++pi) {
    const Pt p = M.points[pi];
    for (int spin=0; spin<2; ++spin) {
      const int src = 2*pi + spin;
      if (degree[pi] != 0) M.row[src].push_back({src, 0, 0, degree[pi], 0});
      for (int qi : adj[pi]) {
        const Pt q = M.points[qi];
        const Edge e = prod_le(p,q) ? Edge{p,q} : Edge{q,p};
        const auto fit = flux_index.find(e);
        if (fit == flux_index.end()) {
          M.row[src].push_back({2*qi + spin, 0, 0, -1, 0});
          continue;
        }
        const int axis = (axis_kind == 0) ? (fit->second % 3) : 2;
        const bool forward = vertex_index.at(p) <= vertex_index.at(q);
        auto add_term = [&](int target_spin, int dc, int ds, int re, int im) {
          // pHeO uses -U when oriented forward and -U^H otherwise.
          M.row[src].push_back({2*qi + target_spin, dc, ds, -re, -im});
        };
        if (axis == 0) { // sigma_x
          add_term(spin, 1, 0, 1, 0);
          add_term(1-spin, 0, 1, 0, forward ? -1 : 1);
        } else if (axis == 1) { // sigma_y
          add_term(spin, 1, 0, 1, 0);
          if (spin == 0) add_term(1, 0, 1, forward ? -1 : 1, 0);
          else add_term(0, 0, 1, forward ? 1 : -1, 0);
        } else { // sigma_z
          add_term(spin, 1, 0, 1, 0);
          int si = (spin == 0) ? -1 : 1;
          if (!forward) si = -si;
          add_term(spin, 0, 1, 0, si);
        }
      }
    }
  }
  for (const auto& r : M.row) {
    int l1 = 0;
    for (const auto& t : r) l1 += abs(t.re) + abs(t.im);
    M.max_row_l1 = max(M.max_row_l1, l1);
  }
  return M;
}

Poly trace_power(const MatrixRows& M, int max_power, uint32_t mod) {
  const int N = M.state_count();
  Poly total;
  for (int src=0; src<N; ++src) {
    vector<Poly> cur(N), nxt(N);
    vector<int> active{src}, next_active;
    vector<uint8_t> mark(N, 0);
    cur[src].re[0][0] = 1;
    for (int step=1; step<=max_power; ++step) {
      next_active.clear();
      for (int u : active) {
        const Poly& P = cur[u];
        for (const auto& t : M.row[u]) {
          if (!mark[t.to]) { mark[t.to] = 1; next_active.push_back(t.to); }
          Poly& Q = nxt[t.to];
          const int maxd = step - 1;
          for (int a=0; a<=maxd; ++a) for (int b=0; b<=maxd-a; ++b) {
            const uint32_t vr = P.re[a][b], vi = P.im[a][b];
            if (vr == 0 && vi == 0) continue;
            const int aa = a + t.dc, bb = b + t.ds;
            const long long dr = static_cast<long long>(vr)*t.re - static_cast<long long>(vi)*t.im;
            const long long di = static_cast<long long>(vr)*t.im + static_cast<long long>(vi)*t.re;
            Q.re[aa][bb] = add_mod_signed(Q.re[aa][bb], dr, mod);
            Q.im[aa][bb] = add_mod_signed(Q.im[aa][bb], di, mod);
          }
        }
      }
      for (int u : active) cur[u].clear();
      cur.swap(nxt);
      active.swap(next_active);
      for (int u : active) mark[u] = 0;
    }
    for (int a=0; a<=max_power; ++a) for (int b=0; b<=max_power-a; ++b) {
      total.re[a][b] = add_mod_signed(total.re[a][b], cur[src].re[a][b], mod);
      total.im[a][b] = add_mod_signed(total.im[a][b], cur[src].im[a][b], mod);
    }
  }
  return total;
}

Poly subtract(const Poly& a, const Poly& b, uint32_t mod, int max_power) {
  Poly out = a;
  for (int i=0; i<=max_power; ++i) for (int j=0; j<=max_power-i; ++j) {
    out.re[i][j] = add_mod_signed(out.re[i][j], -static_cast<long long>(b.re[i][j]), mod);
    out.im[i][j] = add_mod_signed(out.im[i][j], -static_cast<long long>(b.im[i][j]), mod);
  }
  return out;
}
Poly scale(const Poly& a, int k, uint32_t mod, int max_power) {
  Poly out;
  for (int i=0; i<=max_power; ++i) for (int j=0; j<=max_power-i; ++j) {
    out.re[i][j] = add_mod_signed(0, static_cast<long long>(a.re[i][j])*k, mod);
    out.im[i][j] = add_mod_signed(0, static_cast<long long>(a.im[i][j])*k, mod);
  }
  return out;
}
Poly add(const Poly& a, const Poly& b, uint32_t mod, int max_power) {
  Poly out = a;
  for (int i=0; i<=max_power; ++i) for (int j=0; j<=max_power-i; ++j) {
    out.re[i][j] = add_mod_signed(out.re[i][j], b.re[i][j], mod);
    out.im[i][j] = add_mod_signed(out.im[i][j], b.im[i][j], mod);
  }
  return out;
}
uint32_t evaluate_pi(const Poly& p, uint32_t mod, int max_power) {
  uint32_t value = 0;
  for (int b=0; b<=max_power; ++b) value = add_mod_signed(value, p.re[0][b], mod);
  return value;
}

Poly reduce_cs(Poly p, uint32_t mod, int max_power) {
  // Use c^2 = 1 - s^2, descending in the c exponent.
  for (int a=max_power; a>=2; --a) {
    for (int b=0; b<=max_power-a; ++b) {
      const uint32_t vr = p.re[a][b], vi = p.im[a][b];
      if (vr == 0 && vi == 0) continue;
      p.re[a][b] = p.im[a][b] = 0;
      p.re[a-2][b] = add_mod_signed(p.re[a-2][b], vr, mod);
      p.im[a-2][b] = add_mod_signed(p.im[a-2][b], vi, mod);
      p.re[a-2][b+2] = add_mod_signed(p.re[a-2][b+2], -static_cast<long long>(vr), mod);
      p.im[a-2][b+2] = add_mod_signed(p.im[a-2][b+2], -static_cast<long long>(vi), mod);
    }
  }
  return p;
}


int main(int argc, char** argv) {
  uint32_t mod = 10000453;
  for (int i=1; i<argc; ++i) {
    string arg = argv[i];
    if (arg == "--prime" && i+1<argc) mod = static_cast<uint32_t>(stoul(argv[++i]));
    else { cerr << "usage: certificate --prime PRIME\n"; return 2; }
  }

  const auto m5_face = build_matrix(5, 0);
  const auto m5_const = build_matrix(5, 1);
  const auto m6_face = build_matrix(6, 0);
  const auto m6_const = build_matrix(6, 1);

  // Finite graph/count checks against the source's recursive definitions.
  if (m5_face.points.size() != 366 || m5_const.points.size() != 366 ||
      m6_face.points.size() != 1095 || m6_const.points.size() != 1095 ||
      edges(5).size() != 729 || edges(6).size() != 2187 ||
      faces(5).size() != 243 || faces(6).size() != 729) {
    cerr << "source graph count mismatch\n"; return 3;
  }

  const Poly d5_face = trace_power(m5_face, 10, mod);
  const Poly d5_const = trace_power(m5_const, 10, mod);
  const Poly d6_face = trace_power(m6_face, 10, mod);
  const Poly d6_const = trace_power(m6_const, 10, mod);
  const Poly D5 = subtract(d5_face, d5_const, mod, 10);
  const Poly D6 = subtract(d6_face, d6_const, mod, 10);
  const Poly threeD5 = scale(D5, 3, mod, 10);
  const Poly C = subtract(D6, threeD5, mod, 10);

  const int max_row_l1 = max({m5_face.max_row_l1, m5_const.max_row_l1,
                              m6_face.max_row_l1, m6_const.max_row_l1});

  // Independent H4 control: the source Lean theorem states
  // Delta_m(H^4) = -16(3^(m-1)+1)s^2 for m=1,...,5.
  vector<pair<int,uint32_t>> h4_sanity;
  for (int level=1; level<=6; ++level) {
    const auto F = build_matrix(level, 0);
    const auto Z = build_matrix(level, 1);
    const Poly tf = trace_power(F, 4, mod);
    const Poly tz = trace_power(Z, 4, mod);
    const Poly h4 = reduce_cs(subtract(tf, tz, mod, 4), mod, 4);
    h4_sanity.push_back({level, h4.re[0][2]});
    for (int a=0; a<=4; ++a) for (int b=0; b<=4-a; ++b) {
      if ((a != 0 || b != 2) && (h4.re[a][b] != 0 || h4.im[a][b] != 0)) {
        cerr << "H4 source sanity polynomial has unexpected terms at level " << level << "\n";
        return 4;
      }
    }
  }

  cout << "{\"prime\":" << mod
       << ",\"graph\":{\"vertices_m5\":366,\"edges_m5\":729,\"faces_m5\":243,\"vertices_m6\":1095,\"edges_m6\":2187,\"faces_m6\":729}"
       << ",\"max_degree\":" << max({m5_face.max_degree,m5_const.max_degree,m6_face.max_degree,m6_const.max_degree})
       << ",\"max_row_l1\":" << max_row_l1
       << ",\"h4_sanity\":[";
  for (size_t i=0; i<h4_sanity.size(); ++i) {
    if (i) cout << ',';
    cout << "[" << h4_sanity[i].first << ',' << h4_sanity[i].second << "]";
  }
  cout << "]"
       << ",\"D5_pi\":" << evaluate_pi(D5,mod,10)
       << ",\"D6_pi\":" << evaluate_pi(D6,mod,10)
       << ",\"C10_pi\":" << evaluate_pi(C,mod,10)
       << ",\"coefficients\":[";
  bool first = true;
  for (int a=0; a<=10; ++a) for (int b=0; b<=10-a; ++b) {
    if (!first) cout << ',';
    first = false;
    cout << "[" << a << ',' << b << ',' << C.re[a][b] << ',' << C.im[a][b] << "]";
  }
  cout << "]}\n";
  return 0;
}
