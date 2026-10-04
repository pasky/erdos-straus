# Part D (review round 2): targeted Lemma 6.2 test with forced codegree hubs inside (H_δ). Run from repo root: uv run --with numpy python reviews/exceptional-twin3-check-partD.py SEED TRIALS
import numpy as np, itertools, sys
src = open('scripts/twin3_kary_check.py').read().rsplit('main()', 1)[0]
exec(src)
def stars_of(evs):
    S=set()
    for E in evs:
        for r in range(1,len(E)+1):
            for s in itertools.combinations(E,r): S.add(frozenset(s))
    return S
def D(s, evs, nus): return sum(pi(E-s,nus) for E in evs if s<=E)
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 7)
nt=0; ins=0; prom=0; worst=0; worstD=0; badw=0; badD=0; badstar=0
for trial in range(int(sys.argv[2]) if len(sys.argv)>2 else 200):
    k=4; sizes=[int(rng.integers(9,13)) for _ in range(k)]
    nus=[rng.dirichlet(np.ones(s)*5) for s in sizes]; rho=rng.uniform(0.3,1,k)
    ev=set()
    for h in range(int(rng.integers(1,3))):
        l1,l2=rng.choice(k,2,replace=False); a,b=int(rng.integers(sizes[l1])),int(rng.integers(sizes[l2]))
        others=[l for l in range(k) if l not in (l1,l2)]
        for l in others:
            cs=rng.permutation(sizes[l])[:int(rng.integers(sizes[l]//2,sizes[l]+1))]
            for c in cs: ev.add(frozenset({(int(l1),a),(int(l2),b),(int(l),int(c))}))
        if rng.random()<0.5:
            l3,l4=others; ev.add(frozenset({(int(l1),a),(int(l2),b),(int(l3),0),(int(l4),1)}))
    for _ in range(int(rng.integers(0,6))):
        r=int(rng.integers(2,4)); ls=rng.choice(k,r,replace=False)
        ev.add(frozenset((int(l),int(rng.integers(sizes[l]))) for l in ls))
    ev={E for E in ev if not any(F<E for F in ev)}
    w=np.zeros(k)
    for E in ev:
        for (l,_) in E: w[l]+=pi(E,nus)
    delta=max(sum(w[l] for (l,_) in E) for E in ev)
    nt+=1
    if delta>1/16: continue
    ins+=1
    ev2=promote(ev,nus)
    if ev2!=ev: prom+=1
    w2=np.zeros(k)
    for E in ev2:
        for (l,_) in E: w2[l]+=pi(E,nus)
    badw+=int((w2>w+1e-12).any())
    S1=stars_of(ev)
    for s in stars_of(ev2):
        if s not in S1: badstar+=1; continue
        d2=D(s,ev2,nus); d1=D(s,ev,nus)
        if (len(s)>=2 and d2>min(d1,1)+1e-12) or d2>d1+1e-12: badD+=1
    worstD=max(worstD,max(D(s,ev,nus) for s in S1 if len(s)>=2))
    Z1,Z2=Zs(sizes,ev2,nus,rho); lhs=np.log(Z2/Z1**2)
    rhs=star_sum(ev,nus,rho,cap=True)
    worst=max(worst,lhs/((1+25*delta)*rhs))
print(f"trials={nt} inside(H_δ)={ins} promoted={prom} max codegree D (|σ|≥2)={worstD:.3f} "
      f"w+>w:{badw} D+ bound fails:{badD} new stars:{badstar} max lhs/((1+25δ)capped rhs)={worst:.4f}")
