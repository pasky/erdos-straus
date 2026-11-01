# z52d Pass 2 NC0, item Z0848 — Vmin(p) census and independence-model check.
# Vmin(p) = least v in (4Z ∪ (8Z−p)), v>=3, such that p+v has a divisor d ≡ −1 (mod v)   ("success at v").
# fail_v(p) = not success.  Model: P(Vmin>V) ≈ Π_{v∈class(p), v≤V} q_v(p mod 8), q_v = empirical fail frequency.
# Memory: spf sieve to 3e6+400 (int32, ~12 MB).  Usage: uv run --no-project python ... [PMAX] [VMAX]
import sys, numpy as np, math, json, time
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 3_000_000
VMAX=int(sys.argv[2]) if len(sys.argv)>2 else 160
L=PMAX+VMAX+10
spf=np.zeros(L+1,dtype=np.int32)
for i in range(2,int(L**0.5)+1):
    if spf[i]==0:
        s=spf[i*i::i]; mask=(s==0); s[mask]=i
idx=np.arange(L+1); z=(spf==0); z[:2]=False; spf[z]=idx[z]   # primes map to themselves
def divisors(n):
    ds=[1]
    while n>1:
        p=int(spf[n]); e=0
        while n%p==0: n//=p; e+=1
        ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def success(p,v):
    N=p+v
    return any(d%v==v-1 for d in divisors(N))   # d ≡ -1 mod v
primes=[int(q) for q in np.nonzero(spf[:PMAX+1]==np.arange(PMAX+1))[0] if q>=5 and q%4==1]
t0=time.time()
fail_count={}; tot={}
Vmin={}
for p in primes:
    cls=[v for v in range(3,VMAX+1) if (v%4==0) or ((v+p)%8==0)]
    first=None
    for v in cls:
        s=success(p,v)
        key=(v,p%8); tot[key]=tot.get(key,0)+1
        if not s: fail_count[key]=fail_count.get(key,0)+1
        elif first is None: first=v
    Vmin[p]=first if first is not None else 10**9
print('primes',len(primes),'time',round(time.time()-t0,1),file=sys.stderr)
ok={p:v for p,v in Vmin.items()}
recs=[]; best=0
for p in sorted(Vmin):
    if Vmin[p]>best: best=Vmin[p]; recs.append((p,Vmin[p]))
print('records (p,Vmin):',recs)
json.dump({'records':recs,'PMAX':PMAX,'VMAX':VMAX,'n_primes':len(primes),
           'Vmin_hist_top':sorted(((int(v),int(p)) for p,v in Vmin.items()),reverse=True)[:10]},
          open(f'data/z52b/pass2/NC0/vmin_{PMAX}.json','w'),indent=1)
# calibrate q_v per (v, p mod 8) — and per size bin (p-dependence of the single-shift law)
BINS=[0,10**4,10**5,10**6,PMAX+1]
def binof(p):
    for i in range(len(BINS)-1):
        if BINS[i]<=p<BINS[i+1]: return i
    return len(BINS)-2
fc={}; tc={}
for p in primes:
    b=binof(p)
    for v in range(3,VMAX+1):
        if (v%4==0) or ((v+p)%8==0):
            k=(v,p%8,b); tc[k]=tc.get(k,0)+1
            if not success(p,v): fc[k]=fc.get(k,0)+1
q={k:fc.get(k,0)/tc[k] for k in tc}
# model count of primes with Vmin > V, for V in a grid, and observed
obs={}; mod={}
for V in [3,7,15,23,31,47,63,87,116,140]:
    obs[V]=sum(1 for p in Vmin if Vmin[p]>V)
    s=0.0
    for p in primes:
        r=p%8; b=binof(p); pr=1.0
        for v in range(3,V+1):
            if (v%4==0) or ((v+p)%8==0): pr*=q.get((v,r,b),0.0)
        s+=pr
    mod[V]=s
for V in obs: print(f'V={V:4d} observed #{{p: Vmin>V}}={obs[V]:6d}  model(independent, empirical q_v)={mod[V]:12.3f}')
json.dump({'obs':obs,'model':mod,'q_sample':{f'{k[0]}_{k[1]}_bin{k[2]}':round(v,4) for k,v in q.items() if k[0]<=24 and k[1]==1}},
          open(f'data/z52b/pass2/NC0/vmin_model_{PMAX}.json','w'),indent=1)
