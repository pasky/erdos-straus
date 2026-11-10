"""Independent z70 CLASS review checks; run from an archived lane tree.
Pre-run kill tests: any ideal/class/dictionary mismatch kills the stated dictionary;
any nonprimitive solution refutes unqualified Cl language; any saved decoy violating
its matching rules or |z| >= 1.8 refutes the corresponding numerical claim.
Dependencies via uv: sympy, numpy, cypari2. No large Cartesian arrays.
"""
import argparse
import math
from collections import defaultdict
from pathlib import Path
import random
import re
from sympy import Matrix, divisors, factorint, jacobi_symbol
from sympy.matrices.normalforms import hermite_normal_form as hnf


def red(a, b, c):
    while True:
        k = (a - b) // (2*a)
        b, c = b + 2*a*k, c + b*k + a*k*k
        if a > c:
            a, b, c = c, -b, a
            continue
        if (abs(b) == a or a == c) and b < 0:
            b = -b
        return a, b, c


def sols(n, d):
    out = []
    for e in range(1, (n + 4*d)//(4*d-1) + 1):
        if (n+e) % (4*d):
            continue
        m = (n+e)//(4*d)
        for a in divisors(m):
            b = m//a
            if (a+b) % e == 0:
                out.append((int(a), int(b), int((a+b)//e), e))
    return out


def ideal(m, r):
    return Matrix([[m, r], [0, 1]])


def mul(u, v, dn):
    cols = []
    for i in range(u.cols):
        for j in range(v.cols):
            a, b = u[:, i]; c, e = v[:, j]
            cols.append(Matrix([a*c-dn*b*e, a*e+b*c]))
    return hnf(Matrix.hstack(*cols))


def algebra():
    import cypari2
    pari = cypari2.Pari()
    cases = [(n,d) for n in (409,4545,21841,73,25169) for d in (1,2,3,5,7)]
    cases += [(33,1),(69,1),(315,1),(105,3),(45,3),(13,3),(9,1),(25,1),(49,3)]
    failures = []
    total = 0
    for n,d in cases:
        ss = sols(n,d); good = set(); translated = set(); valid = 0
        for a,b,c,e in ss:
            A = 4*a*c*d-1; r = 2*a*d; dn = d*n
            assert A*e == n+4*a*a*d
            assert A*(4*b*c*d-1) == 4*c*c*d*n+1
            lhs = mul(mul(ideal(A,r),ideal(d,0),dn),ideal(e,r),dn)
            rhs = hnf(Matrix([[r,-dn],[1,r]]))
            prim = math.gcd(math.gcd(A,4*a*d),d*e) == 1
            ep = math.gcd(math.gcd(e,4*a*d),d*A) == 1
            if lhs != rhs or not prim or not ep or math.gcd(n,d)>1:
                failures.append((n,d,(a,b,c,e),'identity',lhs==rhs,'primitive',prim,ep))
                continue
            valid += 1; total += 1
            q = pari.Qfb(A,4*a*d,d*e)
            E = pari.Qfb(e,4*a*d,d*A)
            T = pari.Qfb(d,0,n)
            assert pari.qfbred(pari.qfbcomp(pari.qfbcomp(q,E),T)) == pari.qfbred(pari.Qfb(1,0,dn))
            good.add(red(A,4*a*d,d*e))
            translated.add(tuple(int(x) for x in pari.qfbred(pari.qfbcomp(T,E))))
            if math.gcd(e,2*dn)==1:
                assert any(aa%e == r*pow(2*d,-1,e)%e for aa in divisors((n+e)//(4*d)))
        if valid == len(ss):
            assert good == translated
        print('ALG',n,d,'solutions',len(ss),'valid',valid,'classes',len(good))
    assert len(failures)==1 and failures[0][:3]==(105,3,(3,3,2,3)),failures
    assert failures[0][4] is False and failures[0][-1] is False
    assert mul(ideal(3,6),ideal(3,6),33)==Matrix([[3,0],[0,3]])  # ramified, not split
    print('ALG qualified checks',total,'unqualified exceptions',len(failures),'examples',failures[:12])
    # Enumerate all roots for all admissible e, including absent e-ideals.
    count=0
    for n,d in [(409,1),(409,3),(4545,1),(21841,3),(13,3)]:
        from sympy.ntheory import sqrt_mod
        actual={(e,(2*a*d)%e) for a,b,c,e in sols(n,d)}
        for e in range(1,(n+4*d)//(4*d-1)+1):
            if math.gcd(e,2*d*n)>1: continue
            for r in sqrt_mod(-d*n,e,all_roots=True):
                pred=(n+e)%(4*d)==0 and any(a%e == r*pow(2*d,-1,e)%e for a in divisors((n+e)//(4*d)))
                assert pred == ((e,int(r)) in actual),(n,d,e,r)
                count+=1
    print('EQUIVALENT root tests',count)
    products=0
    for n,d in ((409,1),(4545,1),(21841,3),(13,3),(25169,1)):
        for a in (1,2,3):
            if math.gcd(n,d*a)>1:continue
            N=n+4*a*a*d; r=2*a*d
            for M in divisors(N):
                for Mp in divisors(N//M):
                    assert mul(ideal(M,r),ideal(Mp,r),d*n)==hnf(ideal(M*Mp,r))
                    products+=1
    print('PHI multiplicativity checks, including noncoprime factors',products)
    # Explicit injectivity on primitive small ideals, independently reduced.
    for n,d in [(409,1),(4545,1),(21841,3),(13,3)]:
        seen={}; count=0
        for m in range(1,math.isqrt(d*n-1)+1):
            for r in range(m):
                if (r*r+d*n)%m: continue
                C=(r*r+d*n)//m
                if math.gcd(math.gcd(m,2*r),C)>1: continue
                form=red(m,2*r,C)
                assert form not in seen,(n,d,seen.get(form),(m,r))
                seen[form]=(m,r);count+=1
        print('INJECTIVE',n,d,count)


def decoys():
    import cypari2
    pari=cypari2.Pari(); pari.allocatemem(200000000,silent=True)
    total=0; orders=0; worst=0
    for fn in sorted(Path('data/z70/class').glob('i2[bc]_*.txt')):
        groups=defaultdict(list); rows=[]
        for line in fn.read_text().splitlines():
            if line.startswith('#'): continue
            chunks=line.split('|'); p,a,b,c,e,h=map(int,chunks[0].split())
            real=list(map(float,chunks[1].split()))
            if fn.name.startswith('i2b'):
                f,x,y,z=a,b,c,e
                assert f==x*y-1 and x*y*z-x-z==p and f*(z*y-1)==y*p+1
                lead=f; mid=2; tail=z*y-1; t=y
                assert f%8==7
            else:
                u,B,C,dd=a,b,c,e
                assert dd==4*u*C-1 and 4*u*B*C-u-B==p
                lead=dd; mid=4*u*C;tail=C*(u+B);t=C
            assert mid*mid-4*lead*tail==-4*t*p
            assert math.gcd(math.gcd(lead,mid),tail)==1
            ds=[]
            for chunk in chunks[2:]:
                raw=chunk.split(); g,r=map(int,raw[:2]); st=list(map(float,raw[2:]));ds.append(st)
                assert g != lead and g%8==lead%8 and abs(g-lead)*20<=lead
                assert math.gcd(g,2*t*p)==1 and (r*r+t*p)%g==0
                for q in factorint(t*p):
                    if q>2: assert jacobi_symbol(g,q)==jacobi_symbol(lead,q)
            groups[p].append([real[j]-sum(s[j] for s in ds)/2 for j in range(3)])
            rows.append((p,t,lead,mid,tail,h,real,chunks[2:]))
        zs=[]
        for j in range(3):
            vals=[sum(v[j] for v in vs)/len(vs) for vs in groups.values()]
            mean=sum(vals)/len(vals);se=math.sqrt(sum((x-mean)**2 for x in vals)/(len(vals)-1)/len(vals))
            z=mean/se;zs.append(round(z,3));worst=max(worst,abs(z))
        # Independent PARI group/order recomputation for reproducibly sampled rows.
        for p,t,a,b,c,h,real,chunks in random.Random(70042).sample(rows,min(12,len(rows))):
            D=-4*t*p; assert int(pari.quadclassunit(D)[0])==h
            one=pari.qfbred(pari.Qfb(1,0,t*p))
            forms=[(pari.Qfb(a,b,c),real)]
            for chunk in chunks:
                raw=chunk.split();g,r=map(int,raw[:2]);forms.append((pari.Qfb(g,2*r,(r*r+t*p)//g),list(map(float,raw[2:]))))
            for form,st in forms:
                o=h
                for q in factorint(h):
                    while o%q==0 and pari.qfbred(pari.qfbpow(form,o//q))==one:o//=q
                assert pari.qfbred(pari.qfbpow(form,o))==one
                v2=(o & -o).bit_length()-1
                assert abs(math.log(o)/math.log(h)-st[0])<=0.000051 and v2==st[1] and int(o%3==0)==st[2]
                orders+=1
        total+=len(rows)
        print('DECOYS',fn.name,'primes',len(groups),'rows',len(rows),'z',zs)
    print('DECOYS total',total,'orders checked',orders,'max abs z',worst)


def pool():
    for mode in ('CS','ALL','ALLS'):
        for d in (1,2,3):
            if mode=='ALLS' and d!=1:continue
            sums=defaultdict(lambda:[0.,0.]); power=defaultdict(int)
            files=sorted(Path('data/z70/class').glob(f'i1_FIX{mode}_d{d}_[FGH][1234].txt'))
            for fn in files:
                for line in fn.read_text().splitlines():
                    if not line.startswith('n=') or '|' not in line:continue
                    n=int(line.split()[0][2:])
                    if (d==1 and n in (24001,25169)) or (d==2 and n==24481):continue
                    for stat,obs,mean,sd in re.findall(r'(\w+) ([\d.]+) \(([\d.]+)±([\d.]+)\)',line):
                        sums[stat][0]+=float(obs)-float(mean);sums[stat][1]+=float(sd)**2
                        power[stat]+=float(sd)>0
            print('POOL',mode,d,'files',len(files),{s:round(sums[s][0]/math.sqrt(sums[s][1]),3) for s in ('Mx','Ex','L1','L3','C0','A2') if sums[s][1]},'power',dict(power))


def nullcheck():
    # Independent PARI arithmetic for every fibre, ideal and statistic in a small
    # instrumented sample; kills on any broken constraint, genus or self-loop.
    import sys
    import inspect
    import cypari2
    from collections import Counter
    sys.path.insert(0,'scripts')
    import z70_class_nullfix as nf
    pari=cypari2.Pari(); oldstats=nf.stats; counts=Counter()
    def checked(G,Y,tl):
        frame=inspect.currentframe().f_back
        loc=frame.f_locals; C=loc['C']
        one=pari.Qfb(*G.form[G.one])
        def form(x):return pari.Qfb(*G.form[x])
        def key(q):return tuple(int(x) for x in pari.qfbred(q))
        if 'cls' in loc:
            cls=loc['cls']; counts['replicates']+=1
            H={key(pari.qfbpow(form(x),2)) for x in G.form}
            for q,x in cls.items():
                real=C.prime_class(q)[1]
                assert key(pari.qfbcomp(form(x),pari.qfbpow(form(real),-1))) in H
            def vc(v):
                f=one
                for q,k in v:f=pari.qfbcomp(f,pari.qfbpow(form(cls[q]),int(k)))
                return key(f)
            for a,v in loc['fib'].items():
                assert vc(v)==G.form[C.Td]
                counts['fibres']+=1
            assert [vc(v) for v in loc['vecs']]==[G.form[y] for y in Y]
            # CS includes the equal-factor case, not merely distinct graph edges.
            byideal={(e,r):vc(tuple(C.ideal_vector(e,r,loc['F']))) for e,r in loc['gi']}
            for a,b,c,e in loc['sols']:
                A=4*a*c*C.d-1
                if (C.n-1)%(4*a*C.d):continue
                E=byideal[(e,2*a*C.d%e)]; Acl=byideal[(A,2*a*C.d%A)]
                assert key(pari.qfbcomp(pari.Qfb(*E),pari.Qfb(*Acl)))==G.form[C.Td]
                counts['CS']+=1; counts['selfloops']+=A==e
        forms={G.form[y] for y in Y}; overlaps=Counter()
        for a in forms:
            for b in forms:
                if a!=b:overlaps[key(pari.qfbcomp(pari.Qfb(*b),pari.qfbpow(pari.Qfb(*a),-1)))]+=1
        o2=[]; other=[]
        for t,v in overlaps.items():
            (o2 if key(pari.qfbpow(pari.Qfb(*t),2))==key(one) else other).append(v)
        expected=dict(K=len(forms),C0=len(Y)-len(forms),M=max(overlaps.values(),default=0),E=sum(v*v for v in overlaps.values()),
                      L1=overlaps[G.form[tl[0]]] if tl else 0,L3=sum(overlaps[G.form[t]] for t in tl),
                      A2=sum(o2),Mx=max(other,default=0),Ex=sum(v*v for v in other))
        got=oldstats(G,Y,tl)
        assert got==expected,(got,expected)
        return got
    nf.stats=checked
    F=nf.Fact(100000)
    for mode in ('CS','ALL','ALLS'):
        for n,d in ((24001,1),(25169,1),(24481,2),(21841,3),(3000073,1)):
            o=nf.analyse(n,d,30,random.Random(70042),F,mode)
            print('NULLCHECK',mode,n,d,'k',o['k'],'varied',o.get('nvar'))
    print('NULLCHECK independently verified',dict(counts))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['algebra','decoys','pool','nullcheck']);args=ap.parse_args()
    globals()[args.mode]()
