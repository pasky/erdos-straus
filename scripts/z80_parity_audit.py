"""Residue supports & class-number controls on the hard prime census, backwards-compatible raw layouts."""
from pathlib import Path
import gzip,sys,itertools,math
from collections import defaultdict
D=Path('data/z80/jugular/r2')

def rows(s):
    ans={}
    for line in (D/(s+'.csv')).read_text().splitlines():
        n,*z=map(int,line.split(',')); ans[n]=z
    return ans

def main():
    h5=rows('hj'); w=rows('words'); prime=rows('prime'); h={}; check={}
    with gzip.open('data/z52d/parity/counts_1e8.txt.gz','rt') as f:
        for line in f:
            n,E,B,r,ea,fii,cl,mis=map(int,line.split());
            if n>10**7:break
            if n%840==1:h[n]=cl;check[n]=(r,fii)
    pop=sorted(h); assert len(pop)==3426
    out={}; weights=('N','jac_first','par_first','chi4','sgn','jac_mid')
    for p in pop:
        v=prime[p];z=h5[p];q=w[p];assert q[0]==2*check[p][0];assert 2*v[10*2]==check[p][1];
        for k in range(2):
            hbeg=24*k;kw='HJ'+str(3+2*k)
            for j in range(6):
                for o in range(2):
                    a=z[hbeg+o*6+j];b=z[hbeg+12+o*6+j]
                    for suff,val in [('bad',a),('good',b),('all',a+b),('diff',a-b)]:out.setdefault((kw+suff,['ord','un'][o],weights[j]),[]).append(val)
        for i,name in enumerate(('R','Rodd','R8','U7','HJ3bad','HJ3good')):
            for j in range(6):
                for o in range(2):
                    val=q[12*i+6*o+j]
                    if i>=4:
                        if j in (0,2,3,4,5) and (j!=4 or o==0):assert val==out[name,['ord','un'][o],weights[j]][-1] or (j in (2,) and o and False)
                    else:out.setdefault((name,['ord','un'][o],weights[j]),[]).append(val)
        for j,tag in enumerate(weights[:5]):
            for o in range(2):
                a=v[10+5*o+j];b=v[20+5*o+j]
                for suff,val in [('I',a),('II',b),('ES',a+b),('I-II',a-b)]:out.setdefault((suff,['un','ord'][o],tag),[]).append(val)
    mods=(2,3,4,6,8,12,24)
    with (D/'residues.tsv').open('w') as f:
        print('object ordering weight modulus residues_hex_mask never_zero',file=f)
        for (obj,o,tag),vals in sorted(out.items()):
            for m in mods:
                rs={x%m for x in vals};print(obj,o,tag,m,hex(sum(1<<r for r in rs)),int(0 not in rs),file=f)
    print('nonzero-only across panel',[(k,m) for k,v in out.items() for m in mods if not any(x%m==0 for x in v)])
    print('ordinary unweighted unordered supports at 24:',[(k,len(set(x%24 for x in v))) for k,v in out.items() if k[1:] == ('un','N')]);
    # is it even a function of class number mod 32 (so includes h/4 mod 8)?
    with (D/'class.tsv').open('w') as f:
        print('object ordering weight modulus fixed_mod_h32 full_strata total_strata',file=f)
        for k,v in sorted(out.items()):
            for m in mods:
                sm=defaultdict(set)
                for p,x in zip(pop,v):sm[h[p]%32].add(x%m)
                print(*k,m,int(all(len(s)==1 for s in sm.values())),sum(len(s)==m for s in sm.values()),len(sm),file=f)
    # Affine parity law among basic unordered counts and h/4, modulo 2,3.
    names=('I','II','Rodd','R8','U7','HJ3good','HJ3bad','HJ5good','HJ5bad'); vs=[out[n,'un','N'] for n in names]+[[h[p]//4 for p in pop],[1]*len(pop)]
    for m in (2,3):
        piv={};witness=[]
        for p,row in zip(pop,zip(*vs)):
            a=[e%m for e in row]
            for j in sorted(piv):
                c=a[j];a=[(x-c*y)%m for x,y in zip(a,piv[j])]
            if any(a):
                j=next(i for i,x in enumerate(a) if x);inv=pow(a[j],-1,m);piv[j]=[x*inv%m for x in a];witness.append(p)
        print('augmented rank',m,len(piv),'of',len(vs),'independent rows',witness)
if __name__=='__main__':main()
