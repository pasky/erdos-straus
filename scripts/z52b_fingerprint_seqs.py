"""Build ES-derived sequences + transforms, look them up in OEIS (cached), write data/z52b/oeis_hits.json."""
import numpy as np, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from z52b_fingerprint_oeis import lookup
from sympy import isprime
R = 'data/z52b/raw/'
F = np.loadtxt(R+'f4_all_30000.txt', dtype=np.int64)   # n U D O minz mzx mzy maxx minx nx k1 k2 k3 minlcm
FP = np.vstack([F[[isprime(int(x)) for x in F[:,0]]], np.loadtxt(R+'pr_20001_200000.txt', dtype=np.int64)])
FP = FP[np.argsort(FP[:,0])]; FP = FP[np.concatenate([[True], np.diff(FP[:,0])>0])]
W = np.load(R+'words_3e6.npy')  # n W I3 R Uv ESC T1 T2
col = dict(n=0,U=1,D=2,O=3,minz=4,mzx=5,mzy=6,maxx=7,minx=8,nx=9,k1=10,k2=11,k3=12,minlcm=13)
wcol = dict(W=1,I3=2,R=3,Uv=4,ESC=5,T1=6,T2=7)
S = {}
def add(name, desc, seq): S[name] = (desc, [int(x) for x in seq])
def recs(seq, start):
    pos, val, m = [], [], None
    for i, v in enumerate(seq):
        if m is None or v > m: m = v; pos.append(i+start); val.append(int(v))
    return pos, val
def lowrecs(seq, start):
    pos, val, m = [], [], None
    for i, v in enumerate(seq):
        if m is None or v < m: m = v; pos.append(i+start); val.append(int(v))
    return pos, val
n = F[:,0]
for k in ['U','D','O','minz','maxx','nx','k1','k2','minlcm']:
    s = F[:,col[k]]
    add(k, f'{k}(n), n>=2', s)
    add(k+'_n1', f'{k}(n), n>=1 with a(1)=0', [0]+list(s))
    p, v = recs(s, 2); add(k+'_recpos', f'record positions of {k}(n)', p); add(k+'_recval', f'record values of {k}(n)', v)
    add(k+'_mod2', f'{k}(n) mod 2', s % 2)
    add(k+'_diff', f'first differences of {k}(n)', np.diff(s))
U = F[:,1]
first = {}
for i, v in enumerate(U):
    first.setdefault(int(v), int(n[i]))
add('U_first', 'first n with U(n)=k, k=1..', [first.get(k, 0) for k in range(1, 40)])
add('U_missing', 'values k never taken by U(n), n<=30000 (k<=300)', [k for k in range(1, 300) if k not in first][:30])
add('U_odd_pos', 'n with U(n) odd', n[U % 2 == 1])
add('D_odd_pos', 'n with D(n) odd', n[F[:,2] % 2 == 1])
add('minx_excess_pos', 'n with min x > floor(n/4)+1', n[F[:,8] > n//4+1])
add('maxx_minus', 'maxx(n) - floor(n/4)', F[:,7] - n//4)
add('minz_div_n_pos', 'n with n | minz(n)', n[F[:,4] % n == 0])
add('minz_over_n', 'minz(n)/n where integer', (F[:,4]//n)[F[:,4] % n == 0])
add('minlcm_over_n', 'minlcm(n)/n (lcm divisible by n?)', (F[:,13]//n)[F[:,13] % n == 0])
add('minlcm_ndiv_pos', 'n with n not dividing minlcm(n)', n[F[:,13] % n != 0])
add('D_zero', 'n with no distinct solution', n[F[:,2]==0])
add('O_mod6_nonzero', 'n with O(n) not div by 6', n[F[:,3] % 6 != 0])
P = FP[:,0]
for k in ['U','O','minz','maxx','nx','k1','k2','minlcm']:
    s = FP[:,col[k]]
    add('p_'+k, f'{k}(p) at primes p>=2', s)
    p, v = recs(s, 0); add('p_'+k+'_recp', f'primes where {k}(p) sets a record', P[p]); add('p_'+k+'_recv', f'record values of {k}(p)', v)
m1 = P % 4 == 1
add('p1_U', 'U(p) at p≡1 mod 4', FP[m1,1]); add('p3_U', 'U(p) at p≡3 mod 4', FP[(P%4==3),1])
add('p24_U', 'U(p) at p≡1 mod 24', FP[P%24==1,1])
add('p_minz_over_p', 'minz(p)/p at primes (rounded down)', FP[:,4]//P)
add('p_minz_mod_p', 'minz(p) mod p', FP[:,4] % P)
add('p1_minz', 'minz(p), p≡1 mod 4', FP[m1,4])
add('p1_minz_over_p', 'floor(minz(p)/p), p≡1 mod 4', FP[m1,4]//P[m1])
add('p1_maxx', 'maxx(p) at p≡1 mod 4', FP[m1,7])
add('p1_k1', 'k1(p) (one denom div by p) at p≡1(4)', FP[m1,10]); add('p1_k2', 'k2(p) at p≡1(4)', FP[m1,11])
lp = np.log(P.astype(float))
ratio = FP[:,1] / lp**2
pos, val = lowrecs(list(ratio[P > 50]), 0)
add('p_U_lowrec', 'primes p>50 where U(p)/log^2 p is a record low', P[P>50][pos])
add('p_U_small', 'primes with U(p)<=4', P[FP[:,1] <= 4])
add('p_U_eq', 'U(p) for primes where U(p) is a new minimum after p', [])
first = {}
for i, v in enumerate(FP[:,1]): first.setdefault(int(v), int(P[i]))
add('pU_first', 'least prime p with U(p)=k', [first.get(k,0) for k in range(1,30)])
for m in range(5, 14):
    M = np.loadtxt(R+f'm{m}_4000.txt', dtype=np.int64)
    add(f'm{m}_U', f'U_{m}(n) = #sols m/n=1/x+1/y+1/z x<=y<=z, n>=2', M[:,1])
    add(f'm{m}_zero', f'n<=4000 with no solution of {m}/n', M[M[:,1]==0,0])
    add(f'm{m}_minz', f'min max denominator for {m}/n', M[:,4])
    pr = np.array([isprime(int(x)) for x in M[:,0]])
    add(f'm{m}_pU', f'U_{m}(p) at primes', M[pr,1])
wn = W[:,0]
for k, c in wcol.items():
    add('w_'+k, f'word count {k}(n), n>=1', W[:,c])
    add('w_'+k+'_zero', f'n with {k}(n)=0', wn[W[:,c]==0][:60])
odd = wn % 2 == 1
add('w_R_odd', 'R(n) at odd n', W[odd,3])
add('w_R_1mod4', 'R(n) at n≡1 mod 4', W[wn%4==1,3])
add('w_R_zero_1mod4', 'n≡1(4) with R(n)=0', wn[(wn%4==1)&(W[:,3]==0)][:60])
sq = np.array([int(round(x**0.5))**2 == x for x in wn])
add('w_R_zero_1mod4_nonsq', 'non-square n≡1(4) with R(n)=0', wn[(wn%4==1)&(W[:,3]==0)&~sq][:60])
add('w_Uv_zero_all', 'n≡1(4) with Uv(n)=0', wn[(wn%4==1)&(W[:,4]==0)][:60])
add('w_ESC_zero_1mod4_nonsq', 'non-square n≡1(4) with ESC(n)=0', wn[(wn%4==1)&(W[:,5]==0)&~sq][:60])
add('w_I3_zero', 'I3 zeros', wn[W[:,2]==0])
add('w_I3_zero_odd', 'odd I3 zeros', wn[(W[:,2]==0)&odd])
add('w_I3_zero_even', 'even I3 zeros', wn[(W[:,2]==0)&~odd])
add('w_I3_one', 'n with I3(n)=1 (first 60)', wn[W[:,2]==1][:60])
add('w_W_recpos', 'record positions of W(n)', recs(W[:20000,1],1)[0])
add('w_R_recpos', 'record positions of R(n)', recs(W[:200000,3],1)[0])
add('w_I3_recpos', 'record positions of I3(n)', recs(W[:200000,2],1)[0])
add('hard_R', 'R-zeros (★ failures) at primes ≡1(4)', [409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281])
add('hard_A', 'Type A (b=1) failures', [193,2521,66529])
add('hard_union', 'campaign hard primes', [193,409,577,2521,3361,5569,9601,66529,8813281])
add('hard_U', 'U failures non-square', [105,2961,3985,25305,111969,978145])
add('hard_U_all', 'U failures incl squares, n≡1(4)', sorted(set([105,2961,3985,25305,111969,978145]+[k*k for k in range(1,1000,2)]))[:40])
add('m8_fail_known', '8/n failures', [2,3,11,17,131,241])
json.dump(S, open('data/z52b/seqs.json','w'))
out = {}
skip = set(sys.argv[1:])
for name, (desc, seq) in S.items():
    if len(seq) < 3: continue
    # skip leading run of a constant for lookup quality
    hits = lookup(seq, n=min(len(seq), 24))
    out[name] = dict(desc=desc, terms=seq[:24], hits=hits)
    print(name, '|', desc, '|', seq[:12], '->', [h[0]+':'+h[1][:70] for h in hits[:3]], flush=True)
json.dump(out, open('data/z52b/oeis_hits.json','w'), indent=1)
