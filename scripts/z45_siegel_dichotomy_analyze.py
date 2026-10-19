"""Analyze fresh bounded-memory census; stream the old adversarial logs.
Run OPENBLAS_NUM_THREADS=1 uv run python scripts/z45_siegel_dichotomy_analyze.py
under ulimit -v 2000000 and timeout 300. No prime-by-prime Cartesian arrays.
All statistics EVIDENCE; finite identities verified exactly in the audit sample.
"""
from pathlib import Path
from math import gcd, isqrt, log
from fractions import Fraction
import csv
import gzip
import json
import subprocess
import numpy as np
from sympy import factorint, divisors, primerange, isprime, primitive_root

OUT = Path('data/z45_siegel_dichotomy')
W = np.loadtxt(OUT/'windows.csv.gz', delimiter=',', skiprows=1, dtype=np.int64)
with gzip.open(OUT/'fII.bin.gz', 'rb') as f:
    F = np.frombuffer(f.read(), dtype=np.uint32).reshape(-1, 5)
F = F[F[:, 0] % 4 == 1]
assert np.array_equal(F[:, 0], W[:, 0])
P = W[:, 0]
qs = list(primerange(2, 301))

def distances(ps):
    # Reciprocity, since every input p=1 mod 4; includes ramified zero exactly.
    ds = {}; d = np.zeros(len(ps))
    for q in qs:
        if q == 2:
            chi = np.where((ps % 8 == 1) | (ps % 8 == 7), 1, -1)
        else:
            tab = np.array([0 if a == 0 else (1 if pow(a, (q-1)//2, q) == 1 else -1) for a in range(q)])
            chi = tab[ps % q]
        d += (1 - chi) / q
        if q in (7, 47, 293):
            ds[{7: 7, 47: 50, 293: 300}[q]] = d.copy()
    return ds

D = distances(P)

def corr(x, y):
    return float(np.corrcoef(x, y)[0, 1]) if np.std(x) and np.std(y) else None

def measures(mask):
    f = F[mask, 1].astype(float); p = P[mask]
    r = f / np.log(p)**3
    ans = {'n': int(mask.sum()), 'mean_f_over_log3': float(r.mean()),
           'max_a_min': int(W[mask, 1].max()), 'max_mII': int(W[mask, 2].max())}
    ans['correlations'] = {}
    for y, ds in D.items():
        d = ds[mask]
        cmask = mask & (W[:, 3] > 0)
        ans['correlations'][y] = {'D_vs_log_f_over_log3': corr(d, np.log(r)),
            'D_vs_log_amin': corr(d, np.log(W[mask, 1])),
            'D_vs_log_mII': corr(d, np.log(W[mask, 2])),
            'D_vs_log1p_capF': corr(ds[cmask], np.log1p(W[cmask, 4]))}
    order = np.argsort(D[50][mask], kind='stable'); n = len(order)
    ans['D50_deciles'] = []
    for ids in (order[:n//10], order[-n//10:]):
        w = W[mask][ids]; c = w[:, 3] > 0
        ans['D50_deciles'].append({'n': len(ids), 'mean_D': float(D[50][mask][ids].mean()),
            'mean_f_over_log3': float(r[ids].mean()), 'mean_amin': float(w[:, 1].mean()),
            'mean_mII': float(w[:, 2].mean()), 'mean_capF': float(w[c, 4].mean()) if c.any() else None,
            'capF_zero_rate': float((w[c, 4] == 0).mean()) if c.any() else None})
    return ans

hard = np.isin(P % 840, [1,121,169,289,361,529])
near = np.array([int(p)-isqrt(int(p))**2 <= 64 for p in P])
report = {'groups': {name: measures(mask) for name, mask in [
    ('all_1mod4', P > 0), ('1mod24', P % 24 == 1), ('mordell', hard),
    ('all_upper_half', P >= 5000000), ('mordell_upper_half', hard & (P >= 5000000)),
    ('near_square_gap_le64', near)]}}
report['capF_histogram'] = {int(e): int(n) for e,n in zip(*np.unique(W[W[:, 3]>0, 4], return_counts=True))}
report['D50_zero'] = {'n': int((D[50] == 0).sum()), 'examples': W[D[50] == 0][:20].tolist()}
# Full observed e* is 0 everywhere: distinguish local cap(qF) from e*.
report['global_cap_star'] = {'all_zero': bool(np.all(W[:, 2] > 0))}

def rat_cert(p, m, verify=True):
    if gcd(p, m) != 1: return False, False
    K = (p+m)//4
    ds = [int(d) for d in divisors(K)]
    # divisors' ratio is exactly the bounded signed-exponent box after gcd cancellation.
    residues = {d % m: d for d in ds}
    hits = []
    for target in (-1, -p):
        cert = None
        for v in ds:
            if target*v % m in residues:
                u = residues[target*v % m]; g = gcd(u,v); u //= g; vv = v//g
                assert K % (u*vv) == 0
                if verify:
                    if target == -1:
                        h = (u+vv)//m; y = p*(K//u)*h; z = p*(K//vv)*h
                    else:
                        h = (u+p*vv)//m; y = p*(K//u)*h; z = (K//vv)*h
                    assert y > 0 and z > 0
                    assert Fraction(4,p) == Fraction(1,K)+Fraction(1,y)+Fraction(1,z)
                cert = (u,vv); break
        hits.append(cert is not None)
    return tuple(hits)

def cap_at(p, q):
    fs = {int(s): int(b) for s,b in factorint((p+q)//4).items()}
    assert 2 not in fs  # q=3 mod 8 and p=1 mod 8
    for e in range(q):
        res = {1}
        for s,b in fs.items():
            exps = list(range(-b,b+1))+[b+2*j for j in range(1,e+1)]
            vals = {pow(s, a, q) for a in exps}
            res = {r*v % q for r in res for v in vals}
        if q-1 in res: return e
    raise AssertionError((p,q))

fixtures = sorted(set([int(x) for x in Path('data/lsa/hard.txt').read_text().split()] +
    [193,409,577,2521,3361,5569,9601,23929,66529,83449,102001,329617,712321,
     1134241,1724209,1726201,5212561,5101441,8803369,8813281,9257329,31121,9833,1217,41]))
# Exact independently rebuilt min-window searches on every 1000th census row and fixtures.
checks = 0
for row in W[::1000]:
    p,amin,mii,q,cap = map(int,row)
    gota = gotii = 0
    for m in range(3,mii+1,4):
        ii, i = rat_cert(p,m)
        if (ii or i) and not gota: gota=m
        if ii and not gotii: gotii=m
    assert (gota,gotii)==(amin,mii)
    if q: assert cap_at(p,q)==cap
    checks += 1
report['independent_sample_audits'] = checks

with (OUT/'hard_primes.csv').open('w') as f:
    out = csv.writer(f, lineterminator='\n'); out.writerow(['p','fII','a_min','mII','qF','capF','D7','D50','D300'])
    for p in fixtures:
        assert isprime(p)
        amin=mii=0
        for m in range(3,2000,4):
            ii,i=rat_cert(p,m)
            if (ii or i) and not amin: amin=m
            if ii: mii=m; break
        q=next(q for q in primerange(3,2000) if q%8==3 and pow(q,(p-1)//2,p)==p-1)
        cap=cap_at(p,q)
        if p<=10000000:
            ix=np.searchsorted(P,p); assert W[ix,1:].tolist()==[amin,mii,q,cap]
            cnt=int(F[ix,1])
            independent=int(subprocess.check_output(['/tmp/z45_siegel_single',str(p)],text=True,timeout=30).split()[1])
            assert cnt==independent
        else:
            cnt=int(subprocess.check_output(['/tmp/z45_siegel_single',str(p)],text=True,timeout=30).split()[1])
        dd=distances(np.array([p],dtype=np.int64))
        out.writerow([p,cnt,amin,mii,q,cap]+[float(dd[y][0]) for y in (7,50,300)])

hardlist = set(map(int,Path('data/lsa/hard.txt').read_text().split()))
H = np.array([[float(x) for x in r] for r in list(csv.reader((OUT/'hard_primes.csv').open()))[1:] if int(r[0]) in hardlist])
report['hard_list'] = {'n_unique':len(H),
    'corr_D50_log_f_over_log3':corr(H[:,7],np.log(H[:,1]/np.log(H[:,0])**3)),
    'corr_D50_log_amin':corr(H[:,7],np.log(H[:,2])),
    'corr_D50_log1p_capF':corr(H[:,7],np.log1p(H[:,5]))}

# Existing stress-test logs: deduplicate by p, keep first record; counts are inherited evidence.
adv={}
for path in sorted(Path('logs').glob('bs_adv_*.jsonl')):
    for line in path.open():
        r=json.loads(line); adv.setdefault(int(r['p']),r)
AP=np.array(sorted(adv),dtype=np.int64); AD=distances(AP)
AF=np.array([adv[int(p)]['f'] for p in AP]); AE=np.array([adv[int(p)]['emin'] for p in AP])
report['adversarial']={'n_unique':len(AP),'observations':sum(1 for path in Path('logs').glob('bs_adv_*.jsonl') for _ in path.open()),
    'corr_D50_log_f_over_log3':corr(AD[50],np.log(AF/np.log(AP)**3)),
    'corr_D50_log_mII':corr(AD[50],np.log(AE)), 'count_D50_zero':int((AD[50]==0).sum())}
with (OUT/'adversarial.csv').open('w') as f:
    out=csv.writer(f, lineterminator='\n');out.writerow(['p','tag','fII','mII','D7','D50','D300'])
    for j,p in enumerate(AP):out.writerow([int(p),adv[int(p)]['tag'],int(AF[j]),int(AE[j])]+[float(AD[y][j]) for y in (7,50,300)])

# Target-aware dual separation toy. Exact integer angles, full valuation budget.
toy={'pairs':0,'hits':0,'failures':0,'separated_failures':0,'boundary_failures':0,'no_weak_separator':0,
     'nonseparable_examples':[],'separated_examples':[],'no_weak_separator_examples':[]}
for q in primerange(3,200):
    if q%8!=3:continue
    root=int(primitive_root(q)); n=q-1; logs={pow(root,j,q):j for j in range(n)}
    for p0 in P[(P<=100000)&(P%8==1)]:
        p=int(p0)
        if pow(q,(p-1)//2,p)!=p-1:continue
        fs={int(s):int(b) for s,b in factorint((p+q)//4).items()}
        ii,_=rat_cert(p,q)
        costs=[(sum(b*min((j*logs[s%q])%n,(-j*logs[s%q])%n) for s,b in fs.items()),j) for j in range(1,n,2)]
        cost,j=min(costs); sep=2*cost<n
        assert not (ii and sep)
        toy['pairs']+=1;toy['hits']+=ii;toy['failures']+=not ii;toy['separated_failures']+=sep
        toy['boundary_failures']+=not ii and 2*cost==n
        toy['no_weak_separator']+=not ii and 2*cost>n
        item=[p,q,(p+q)//4,fs,int(cost),int(n),int(j),n//gcd(n,j)]
        key='separated_examples' if sep else 'nonseparable_examples'
        if not ii and len(toy[key])<8:toy[key].append(item)
        if not ii and 2*cost>n and len(toy['no_weak_separator_examples'])<8:toy['no_weak_separator_examples'].append(item)
report['toy']=toy
# Small boundary example: projected target is attained, but the residual kernel class is wrong.
assert not rat_cert(9833,67)[0]
assert pow(3,2,67)*pow(5,-2,67)*pow(11,-1,67)%67 == 30
assert pow(30,-1,67)==38 and 66 not in (30,38)
report['boundary_example']={'p':9833,'q':67,'K':2475,'odd_character_index':27,
    'primitive_root':2,'angle_numerators_over66':[-3,9,9],'boundary_residues':[30,38]}
# Exact certificate against the conjectured weak single-character inverse theorem.
q=43; p=31121; fs={3:1,7:2,53:1}; logs={3:1,7:35,53:10}
assert isprime(p) and isprime(q) and pow(q,(p-1)//2,p)==p-1
assert all(pow(3,a,q)==s%q for s,a in logs.items())
costs=[sum(b*min(j*logs[s]%42,(-j*logs[s])%42) for s,b in fs.items()) for j in range(1,42,2)]
res={1}
for s,b in fs.items():res={r*pow(s,a,q)%q for r in res for a in range(-b,b+1)}
assert min(costs)==25 and len(res)==37 and 42 not in res
report['inverse_counterexample']={'p':p,'q':q,'K':7791,'primitive_root':3,
    'logs':logs,'odd_character_cost_numerators_over42':costs,'box_residues':sorted(res)}

(OUT/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
