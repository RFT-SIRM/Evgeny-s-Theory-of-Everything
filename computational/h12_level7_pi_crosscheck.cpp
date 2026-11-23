#include <array>
#include <cstdlib>
#include <array>
#include <cstdlib>

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;
struct Pt { int x,y; bool operator<(const Pt&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(const Pt&o)const{return x==o.x&&y==o.y;} };
using Edge=pair<Pt,Pt>;
static inline bool le(Pt a,Pt b){return a.x<=b.x&&a.y<=b.y;}
static inline Pt shift(Pt p,int dx,int dy){return {p.x+dx,p.y+dy};}
static inline Edge und(Pt a,Pt b){return a<b?Edge{a,b}:Edge{b,a};}
vector<Pt> vertex_order(int m){if(!m)return {{0,0},{1,0},{0,1}}; auto prev=vertex_order(m-1);int s=1<<(m-1);vector<Pt>out;set<Pt>seen;for(auto [dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(Pt p:prev){Pt q=shift(p,dx,dy);if(seen.insert(q).second)out.push_back(q);}return out;}
set<Edge> edges(int m){if(!m)return {und({0,0},{1,0}),und({1,0},{0,1}),und({0,1},{0,0})};auto prev=edges(m-1);int s=1<<(m-1);set<Edge>out;for(auto[dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(auto&e:prev)out.insert(und(shift(e.first,dx,dy),shift(e.second,dx,dy)));return out;}
vector<array<Pt,3>> faces(int m){if(!m)return {array<Pt,3>{Pt{0,0},Pt{1,0},Pt{0,1}}};auto prev=faces(m-1);int s=1<<(m-1);vector<array<Pt,3>>out;for(auto[dx,dy]:{pair<int,int>{0,0},{s,0},{0,s}})for(auto f:prev)out.push_back({shift(f[0],dx,dy),shift(f[1],dx,dy),shift(f[2],dx,dy)});return out;}
struct C {int64_t re=0,im=0; C& operator+=(C b){re+=b.re;im+=b.im;return *this;}};
static inline C mul(C a,C b){return {a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re};}
struct E {int to; C v;};
struct M {vector<vector<E>> rows;int maxdegree=0,maxl1=0;size_t vertices=0,edge_count=0,face_count=0;};
M build(int m,int axis_kind){M Mx;auto vs=vertex_order(m);Mx.vertices=vs.size();map<Pt,int> idx;for(int i=0;i<(int)vs.size();++i)idx[vs[i]]=i;auto es=edges(m);Mx.edge_count=es.size();vector<vector<int>>adj(vs.size());vector<int>deg(vs.size());for(auto&e:es){int a=idx.at(e.first),b=idx.at(e.second);adj[a].push_back(b);adj[b].push_back(a);++deg[a];++deg[b];}for(int d:deg)Mx.maxdegree=max(Mx.maxdegree,d);auto fs=faces(m);Mx.face_count=fs.size();map<Edge,int> flux;for(int i=0;i<(int)fs.size();++i){Pt a=fs[i][0],b=fs[i][1];Edge e=le(a,b)?Edge{a,b}:Edge{b,a};if(!flux.count(e))flux[e]=i;}Mx.rows.resize(vs.size()*2);
for(int pi=0;pi<(int)vs.size();++pi){Pt p=vs[pi];for(int spin=0;spin<2;++spin){int src=2*pi+spin;if(deg[pi])Mx.rows[src].push_back({src,{deg[pi],0}});for(int qi:adj[pi]){Pt q=vs[qi];Edge e=le(p,q)?Edge{p,q}:Edge{q,p};auto fit=flux.find(e);if(fit==flux.end()){Mx.rows[src].push_back({2*qi+spin,{-1,0}});continue;}int axis=axis_kind==0?(fit->second%3):2;bool forward=idx.at(p)<=idx.at(q);auto add=[&](int target,C coefficient){ // original entry is -U/-U^H
    Mx.rows[src].push_back({2*qi+target,{-coefficient.re,-coefficient.im}});
};
// theta=pi: c=0,s=1. U=-i sigma_axis.
if(axis==0){ // sigma_x: offdiag U=-i; conjugate changes sign
 add(1-spin,{0,forward?-1:1});
}else if(axis==1){ // sigma_y: offdiag real +/-1; see exact engine spin convention
 if(spin==0)add(1,{forward?-1:1,0});else add(0,{forward?1:-1,0});
}else{int si=(spin==0)?-1:1;if(!forward)si=-si;add(spin,{0,si});}
}}}
for(auto&r:Mx.rows){int l=0;for(auto&e:r)l+=abs(e.v.re)+abs(e.v.im);Mx.maxl1=max(Mx.maxl1,l);}return Mx;}
C trace_power(const M&Mx,int power){int N=Mx.rows.size();vector<C>cur(N),nxt(N);vector<int>active,next;vector<uint8_t>seen(N);int64_t trace_re=0,trace_im=0;for(int src=0;src<N;++src){cur[src]={1,0};active.clear();active.push_back(src);for(int k=0;k<power;++k){next.clear();for(int u:active){C a=cur[u];for(auto&e:Mx.rows[u]){int v=e.to;if(!seen[v]){seen[v]=1;next.push_back(v);}nxt[v]+=mul(a,e.v);}}for(int u:active)cur[u]={};cur.swap(nxt);active.swap(next);for(int u:active)seen[u]=0;}trace_re+=cur[src].re;trace_im+=cur[src].im;for(int u:active)cur[u]={};}return {trace_re,trace_im};}
int main(){int m=7;M F=build(m,0),Z=build(m,1);if(F.vertices!=3282||F.edge_count!=6561||F.face_count!=2187)return 3;C tf=trace_power(F,12),tz=trace_power(Z,12);cout<<"{\"level\":7,\"vertices\":"<<F.vertices<<",\"edges\":"<<F.edge_count<<",\"faces\":"<<F.face_count<<",\"max_degree\":"<<max(F.maxdegree,Z.maxdegree)<<",\"max_row_l1\":"<<max(F.maxl1,Z.maxl1)<<",\"trace_face_re\":"<<tf.re<<",\"trace_face_im\":"<<tf.im<<",\"trace_z_re\":"<<tz.re<<",\"trace_z_im\":"<<tz.im<<",\"D7_pi_re\":"<<tf.re-tz.re<<",\"D7_pi_im\":"<<tf.im-tz.im<<"}\n";}
