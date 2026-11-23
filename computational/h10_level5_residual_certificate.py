"""Exact symbolic checks for the H10 level-five correction.

This certificate verifies the published polynomial/Fourier identity in
Z[c,s]/(c^2+s^2-1), plus exact endpoint values. It does not rebuild the
large graph trace from first principles; see the report for this boundary.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

# Monomials are (power of c, power of s), with integer coefficients.
POLY = {
    (0,2):-748240, (1,2):11036800, (0,3):4927360,
    (1,3):-261920, (0,4):330960, (1,4):1920,
    (0,5):-3200, (1,5):320, (0,6):640,
}
FOURIER = {
    0:(-249810,0), 1:(2759440,3693520),
    2:(208340,-65430), 3:(-2759560,-1230840),
    4:(41490,32700), 5:(120,-200), 6:(-20,10),
}
D5_PI = -2505633280
D6_PI = -7512392320

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if not out[k]: del out[k]
    return out

def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            out[(i+k,j+l)]=out.get((i+k,j+l),0)+x*y
    return {k:v for k,v in out.items() if v}

def reduce_relation(poly):
    """Reduce c^2 to 1-s^2, yielding c-degree <= 1."""
    out={}
    for (i,j),v in poly.items():
        while i>=2:
            # c^i s^j = c^(i-2)s^j - c^(i-2)s^(j+2)
            out=add(out,{(i-2,j):v})
            out=add(out,{(i-2,j+2):-v})
            v=0
            break
        if v:
            out[(i,j)]=out.get((i,j),0)+v
    # Repeat because the previous substitution can aggregate terms.
    changed=True
    while changed:
        changed=False
        nxt={}
        for (i,j),v in out.items():
            if i>=2:
                changed=True
                nxt=add(nxt,{(i-2,j):v,(i-2,j+2):-v})
            else:
                nxt=add(nxt,{(i,j):v})
        out=nxt
    return out

def fourier_to_cs():
    # cos(ku)+i sin(ku)=(c+i*s)^k; real and imaginary parts.
    result={}
    for k,(a,b) in FOURIER.items():
        for r in range(k+1):
            # term c^(k-r) (i*s)^r
            if r%2==0:
                coeff=a*((-1)**(r//2))*__import__('math').comb(k,r)
                result[(k-r,r)]=result.get((k-r,r),0)+coeff
            else:
                coeff=b*((-1)**((r-1)//2))*__import__('math').comb(k,r)
                result[(k-r,r)]=result.get((k-r,r),0)+coeff
    return result

def verify():
    lhs=reduce_relation(POLY)
    rhs=reduce_relation(fourier_to_cs())
    if lhs!=rhs:
        raise AssertionError({"polynomial":lhs,"fourier":rhs})
    if sum(v for (i,j),v in POLY.items() if i==0 and j==0)!=0:
        raise AssertionError("C10(0) must be zero")
    if D6_PI-3*D5_PI != 4507520:
        raise AssertionError("endpoint trace residual mismatch")
    return {
        "identity":"verified in Z[c,s]/(c^2+s^2-1)",
        "polynomial_terms":len(POLY),
        "fourier_modes":len(FOURIER),
        "D5_pi":D5_PI,"D6_pi":D6_PI,"C10_pi":D6_PI-3*D5_PI,
        "scope":"symbolic coefficient identity and exact endpoint arithmetic; graph trace reconstruction is not performed by this script"
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    result=verify()
    payload=json.dumps(result,indent=2,sort_keys=True)+"\\n"
    if args.output:
        Path(args.output).parent.mkdir(parents=True,exist_ok=True)
        Path(args.output).write_text(payload)
    print(payload,end="")
if __name__=="__main__":
    main()
