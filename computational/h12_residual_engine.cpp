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
struct Pt{int x,y;bool operator<(const Pt&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(const Pt&o)const{return x==o.x&&y==o.y;}};
using Edge=pair<Pt,Pt>;
static inline bool le(Pt a,Pt b){return a.x<=b.x&&a.y<=b.y;}
static inline Pt sh(Pt p,int dx,int dy){return {p.x+dx,p.y+dy};}
static inline Edge und(Pt a,Pt b){return a<b?Edge{a,b}:Edge{b,a};}
vector<Pt> vertex_order(int m){if(!m)return {{0,0},{1,0},{0,1}};auto p=vertex_order(m-1);int s=1<<(m-1);vector<Pt>o;set<Pt>seen;for(auto[dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(Pt q:p){Pt r=sh(q,dx,dy);if(seen.insert(r).second)o.push_back(r);}return o;}
set<Edge> edges(int m){if(!m)return {und({0,0},{1,0}),und({1,0},{0,1}),und({0,1},{0,0})};auto p=edges(m-1);int s=1<<(m-1);set<Edge>o;for(auto[dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(auto&e:p)o.insert(und(sh(e.first,dx,dy),sh(e.second,dx,dy)));return o;}
vector<array<Pt,3>> faces(int m){if(!m)return {array<Pt,3>{Pt{0,0},Pt{1,0},Pt{0,1}}};auto p=faces(m-1);int s=1<<(m-1);vector<array<Pt,3>>o;for(auto[dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(auto f:p)o.push_back({sh(f[0],dx,dy),sh(f[1],dx,dy),sh(f[2],dx,dy)});return o;}
static inline uint32_t addmod(uint32_t old,long long d,uint32_t p){long long x=(long long)old+d;x%=(long long)p;if(x<0)x+=p;return (uint32_t)x;}
struct Poly{uint32_t re[2][13]{};uint32_t im[2][13]{};void clear(){memset(this,0,sizeof(*this));}};
struct Tr{int to,dc,ds,re,im;};
struct Mat{vector<vector<Tr>> row;vector<Pt> pts;int deg=0,l1=0;size_t edge_count=0,face_count=0;};
Mat build(int m,int axis_kind){Mat M;M.pts=vertex_order(m);map<Pt,int>idx;for(int i=0;i<(int)M.pts.size();++i)idx[M.pts[i]]=i;auto es=edges(m);M.edge_count=es.size();vector<vector<int>>adj(M.pts.size());vector<int>d(M.pts.size());for(auto&e:es){int a=idx.at(e.first),b=idx.at(e.second);adj[a].push_back(b);adj[b].push_back(a);++d[a];++d[b];}for(int v:d)M.deg=max(M.deg,v);auto fs=faces(m);M.face_count=fs.size();map<Edge,int>flux;for(int i=0;i<(int)fs.size();++i){Pt a=fs[i][0],b=fs[i][1];Edge e=le(a,b)?Edge{a,b}:Edge{b,a};if(!flux.count(e))flux[e]=i;}M.row.resize(2*M.pts.size());
for(int pi=0;pi<(int)M.pts.size();++pi){Pt p=M.pts[pi];for(int spin=0;spin<2;++spin){int src=2*pi+spin;if(d[pi])M.row[src].push_back({src,0,0,d[pi],0});for(int qi:adj[pi]){Pt q=M.pts[qi];Edge e=le(p,q)?Edge{p,q}:Edge{q,p};auto it=flux.find(e);if(it==flux.end()){M.row[src].push_back({2*qi+spin,0,0,-1,0});continue;}int axis=axis_kind==0?(it->second%3):2;bool fw=idx.at(p)<=idx.at(q);auto add=[&](int ts,int dc,int ds,int re,int im){M.row[src].push_back({2*qi+ts,dc,ds,-re,-im});};if(axis==0){add(spin,1,0,1,0);add(1-spin,0,1,0,fw?-1:1);}else if(axis==1){add(spin,1,0,1,0);if(spin==0)add(1,0,1,fw?-1:1,0);else add(0,0,1,fw?1:-1,0);}else{add(spin,1,0,1,0);int si=spin==0?-1:1;if(!fw)si=-si;add(spin,0,1,0,si);}}}}
for(auto&r:M.row){int l=0;for(auto&t:r)l+=abs(t.re)+abs(t.im);M.l1=max(M.l1,l);}return M;}
// Add coef*(c^dc*s^ds)*P to Q, reducing c^2 to 1-s^2 immediately.
static inline void add_scaled(uint32_t& rr,uint32_t& ii,uint32_t vr,uint32_t vi,int cr,int ci,int sign,uint32_t mod){long long ar=(long long)vr*cr-(long long)vi*ci;long long ai=(long long)vr*ci+(long long)vi*cr;rr=addmod(rr,sign*ar,mod);ii=addmod(ii,sign*ai,mod);}
void add_transition(const Poly&P,Poly&Q,const Tr&t,int step,uint32_t mod){int maxb=step;for(int a=0;a<=1;++a)for(int b=0;b<=maxb;++b){uint32_t vr=P.re[a][b],vi=P.im[a][b];if(!vr&&!vi)continue;int bb=b+t.ds;if(t.dc==0){add_scaled(Q.re[a][bb],Q.im[a][bb],vr,vi,t.re,t.im,1,mod);}else if(a==0){add_scaled(Q.re[1][bb],Q.im[1][bb],vr,vi,t.re,t.im,1,mod);}else{add_scaled(Q.re[0][bb],Q.im[0][bb],vr,vi,t.re,t.im,1,mod);add_scaled(Q.re[0][bb+2],Q.im[0][bb+2],vr,vi,t.re,t.im,-1,mod);}}}
Poly trace_power(const Mat&M,int P,uint32_t mod){int N=M.row.size();Poly total;vector<Poly>cur(N),nxt(N);vector<int>active,next;vector<uint8_t>seen(N);for(int src=0;src<N;++src){cur[src].re[0][0]=1;active.clear();active.push_back(src);for(int step=1;step<=P;++step){next.clear();for(int u:active){const Poly&v=cur[u];for(const Tr&t:M.row[u]){if(!seen[t.to]){seen[t.to]=1;next.push_back(t.to);}add_transition(v,nxt[t.to],t,step-1,mod);}}for(int u:active)cur[u].clear();cur.swap(nxt);active.swap(next);for(int u:active)seen[u]=0;}for(int a=0;a<=1;++a)for(int b=0;b<=P-a;++b){total.re[a][b]=addmod(total.re[a][b],cur[src].re[a][b],mod);total.im[a][b]=addmod(total.im[a][b],cur[src].im[a][b],mod);}for(int u:active)cur[u].clear();}return total;}
Poly subtract(const Poly&a,const Poly&b,uint32_t mod,int P){Poly o=a;for(int x=0;x<=1;++x)for(int y=0;y<=P-x;++y){o.re[x][y]=addmod(o.re[x][y],-(long long)b.re[x][y],mod);o.im[x][y]=addmod(o.im[x][y],-(long long)b.im[x][y],mod);}return o;}
uint32_t atpi(const Poly&p,uint32_t mod,int P){uint32_t v=0;for(int b=0;b<=P;++b)v=addmod(v,p.re[0][b],mod);return v;}
int main(int argc,char**argv){
  uint32_t mod=10000453;
  for(int i=1;i<argc;++i){string a=argv[i];if(a=="--prime"&&i+1<argc)mod=(uint32_t)stoul(argv[++i]);else return 2;}
  constexpr int P=12;
  vector<pair<int,Poly>> defects;
  int max_degree=0,max_row_l1=0;
  cout<<"{\"prime\":"<<mod;
  for(int m:{7,8}){
    Mat F=build(m,0),Z=build(m,1);
    size_t pow3=1;for(int k=0;k<m;++k)pow3*=3;
    size_t expected=(3*pow3+3)/2;
    if(F.pts.size()!=expected||F.edge_count!=3*pow3||F.face_count!=pow3||Z.pts.size()!=expected||Z.edge_count!=3*pow3||Z.face_count!=pow3)return 3;
    max_degree=max({max_degree,F.deg,Z.deg});
    max_row_l1=max({max_row_l1,F.l1,Z.l1});
    Poly D=subtract(trace_power(F,P,mod),trace_power(Z,P,mod),mod,P);
    defects.push_back({m,D});
    cerr<<"computed reduced D"<<m<<"^12 (states="<<F.row.size()<<")\n";
  }
  cout<<",\"max_graph_degree\":"<<max_degree<<",\"max_row_coefficient_l1\":"<<max_row_l1<<",\"levels\":{";
  bool first=true;
  for(const auto& item:defects){
    int m=item.first;const Poly&D=item.second;
    if(!first)cout<<',';first=false;
    size_t pow3=1;for(int k=0;k<m;++k)pow3*=3;
    cout<<"\"m"<<m<<"\":{\"vertices\":"<<((3*pow3+3)/2)<<",\"edges\":"<<(3*pow3)<<",\"faces\":"<<pow3<<",\"D_pi\":"<<atpi(D,mod,P)<<",\"coefficients\":[";
    bool fc=true;
    for(int a=0;a<=1;++a)for(int b=0;b<=P-a;++b){if(!fc)cout<<',';fc=false;cout<<'['<<a<<','<<b<<','<<D.re[a][b]<<','<<D.im[a][b]<<']';}
    cout<<"]}";
  }
  cout<<"}}\n";
}
