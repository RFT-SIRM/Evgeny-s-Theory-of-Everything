#!/usr/bin/env python3
"""Sparse-trace cross-check for H6/H8/H10 through level 7; not a proof."""
import argparse, json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
POWERS=(6,8,10); ANGLES=(("pi_over_2",float(np.pi/2)),("pi",float(np.pi)))
REF={6:[-3180.,-6956.588745030516,-18274.354980121832,-52227.653685396537],8:[-246909.026268397924,-595053.284942481667,-1632052.331668503582,-4743049.471846580505],10:[-14013358.982483163476,-37686518.369789719582,-107772338.487565994263,-318029798.840893745422]}
C_PI={6:5280.,8:277504.,10:4507520.}
def graph(level):
 V=[(0.,0.),(1.,0.),(0.,1.)]; E=[(0,1),(1,2),(0,2)]; F=None
 for _ in range(level):
  offsets=[(0.,0.),(.5,0.),(0.,.5)]; nv=[]; idx={}; ne=set(); maps=[]
  for ox,oy in offsets:
   mp={}
   for i,(x,y) in enumerate(V):
    q=(round(x*.5+ox,10),round(y*.5+oy,10))
    if q not in idx: idx[q]=len(nv); nv.append(q)
    mp[i]=idx[q]
   maps.append(mp)
  nf=[]
  for mp in maps:
   for a,b in E: ne.add(tuple(sorted((mp[a],mp[b]))))
   if F is None: nf.append((mp[0],mp[1],mp[2]))
   else: nf.extend(tuple(mp[v] for v in face) for face in F)
  V,E,F=nv,list(ne),nf
 return V,E,F
def operator(level,theta,commuting):
 V,E,F=graph(level); n=len(V); deg=np.zeros(n,dtype=int)
 for a,b in E: deg[a]+=1; deg[b]+=1
 I=np.eye(2,dtype=complex); P=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex))
 U={tuple(sorted(e)):I for e in E}; c=np.cos(theta/2); s=np.sin(theta/2)
 for k,(a,b,_z) in enumerate(F): U[tuple(sorted((a,b)))]=c*I-1j*s*P[2 if commuting else k%3]
 r=[]; col=[]; val=[]
 for v in range(n):
  for j in range(2): r.append(2*v+j); col.append(2*v+j); val.append(deg[v])
 for (a,b),u in U.items():
  for i in range(2):
   for j in range(2):
    if u[i,j]!=0:
     r.extend((2*a+i,2*b+j)); col.extend((2*b+j,2*a+i)); val.extend((-u[i,j],-np.conjugate(u[i,j])))
 return coo_matrix((val,(r,col)),shape=(2*n,2*n),dtype=complex).tocsr()
def trpow(H,p):
 Q=H.copy()
 for _ in range(p-1): Q=Q@H; Q.eliminate_zeros()
 return float(np.sum(Q.diagonal()).real)
def delta(m,t):
 A=operator(m,t,False); B=operator(m,t,True)
 return {f'H{p}':trpow(A,p)-trpow(B,p) for p in POWERS}
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",default="artifacts/independent_sparse_level7.json")
 args=ap.parse_args()
 out={'status':'independent sparse trace holdout; numerical evidence, not proof','method':'standalone graph/operator reimplementation; SciPy sparse matrix powers; no eigenspectrum','levels':list(range(1,8)),'powers':list(POWERS),'angles':{}}
 for name,t in ANGLES:
  vals={}
  for m in range(1,8):
   vals[str(m)]=delta(m,t); print(name,'level',m,vals[str(m)],flush=True)
  trans={}
  for p in POWERS:
   d=[vals[str(m)][f'H{p}'] for m in range(1,8)]; C=[d[i]-3*d[i-1] for i in range(1,7)]; c34=C[2]
   res={str(m):abs(d[m-1]-(3*d[m-2]+c34))/max(abs(d[m-1]),1.) for m in range(5,8)}
   if max(res.values())>1e-8: raise AssertionError((name,p,res))
   if abs(C[0]-c34)<1e-3: raise AssertionError((name,p,'1->2 exception missing'))
   ent={'C_1_to_2':C[0],'C_2_to_3':C[1],'C_3_to_4_reference':c34,'C_4_to_5':C[3],'C_5_to_6':C[4],'C_6_to_7':C[5],'relative_prediction_residual_levels_5_to_7':res}
   if name=='pi':
    if abs(c34-C_PI[p])>1e-6: raise AssertionError((p,c34,C_PI[p]))
   else:
    errs=[abs(d[i]-REF[p][i])/max(abs(REF[p][i]),1.) for i in range(4)]
    if max(errs)>2e-9: raise AssertionError((p,'reference mismatch',errs))
    ent['published_level1_to_4_max_relative_error']=max(errs)
   trans[f'H{p}']=ent
  out['angles'][name]={'theta_radians':t,'trace_defects':vals,'transition_constants':trans}
 path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("Wrote",path)
if __name__=='__main__': main()
