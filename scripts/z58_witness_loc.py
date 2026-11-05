"""z58 WITNESS: where do the (★) solutions of the hardest primes sit?  Compare the log-coordinates
x = log P / log(p/4), y = log Q / log(p/4), z = log C / log(p/4) (P < Q the pair, C the level; x + y + z ≈ 1) of the
solutions of low-R primes (R <= 4) with the pooled solutions of control 𝔐-primes of the same size range.
Also: which moduli carry the least QNR n_p (rooting test), and the C-parity split.
Usage: python3 z58_witness_loc.py hard_sols.txt ctrl_sols.txt PMIN"""
import sys, math

def jac(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def n_p(p):
    # least prime l with (l/p) = -1 (p prime = 1 mod 4): l = 2 iff p = 5 mod 8; odd l via reciprocity (p/l) = (l/p)
    if p % 8 == 5: return 2
    l = 3
    while True:
        if isprime(l) and jac(p % l, l) == -1: return l
        l += 2

def load(fn, pmin):
    out = []
    for line in open(fn):
        a, b = line.split(':'); p, k = map(int, a.split())
        if p < pmin: continue
        sols = [tuple(map(int, t.split(','))) for t in b.split()]
        out.append((p, sols))
    return out

def feats(p, sols):
    L = math.log(p / 4); np_ = n_p(p); res = []
    for P, Q, C in sols:
        x, y, z = math.log(P) / L, math.log(Q) / L, math.log(C) / L
        d1, d2, q = 4 * P * C - 1, 4 * Q * C - 1, P * Q
        root = (d1 % np_ == 0) + 2 * (d2 % np_ == 0) + 4 * (q % np_ == 0)
        res.append(dict(x=x, y=y, z=z, mn=min(x, y, z), mx=max(x, y, z), Ceven=(C % 2 == 0), root=root,
                        minmod=min(d1, d2, 4 * P * Q) / p ** (2 / 3)))
    return res, np_

def ks(a, b):
    a, b = sorted(a), sorted(b); i = j = 0; D = 0.0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: i += 1
        else: j += 1
        D = max(D, abs(i / len(a) - j / len(b)))
    n = len(a) * len(b) / (len(a) + len(b))
    # asymptotic p-value
    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * D
    pv = 2 * sum((-1) ** (k - 1) * math.exp(-2 * k * k * lam * lam) for k in range(1, 100))
    return D, max(0.0, min(1.0, pv))

hard = load(sys.argv[1], int(sys.argv[3])); ctrl = load(sys.argv[2], int(sys.argv[3]))
H, Cc = [], []
anyroot_h = 0
for p, s in hard:
    f, np_ = feats(p, s); H += f; anyroot_h += any(t['root'] for t in f)
anyroot_c = 0
for p, s in ctrl:
    f, np_ = feats(p, s); Cc += f; anyroot_c += any(t['root'] for t in f)
print(f"hard primes: {len(hard)} ({len(H)} unordered solutions); control primes: {len(ctrl)} ({len(Cc)} solutions); "
      f"p range hard [{min(p for p,_ in hard)}, {max(p for p,_ in hard)}], ctrl [{min(p for p,_ in ctrl)}, {max(p for p,_ in ctrl)}]")
for key in ('x', 'y', 'z', 'mn', 'mx', 'minmod'):
    a = [t[key] for t in H]; b = [t[key] for t in Cc]
    D, pv = ks(a, b)
    print(f"{key:7s} mean hard {sum(a)/len(a):.3f}  ctrl {sum(b)/len(b):.3f}   KS D={D:.3f} p≈{pv:.3g}")
for nm, S in (('hard', H), ('ctrl', Cc)):
    n = len(S)
    print(f"{nm}: frac C even {sum(t['Ceven'] for t in S)/n:.3f}; frac solutions with n_p | (4PC-1) {sum(t['root']&1>0 for t in S)/n:.3f}, "
          f"| (4QC-1) {sum(t['root']&2>0 for t in S)/n:.3f}, | PQ {sum(t['root']&4>0 for t in S)/n:.3f}, any {sum(t['root']>0 for t in S)/n:.3f}")
print(f"primes with SOME solution rooted at n_p: hard {anyroot_h}/{len(hard)}, ctrl {anyroot_c}/{len(ctrl)}")
# uniform-simplex reference for min coordinate: P(mn > t) = (1-3t)^2
for t in (0.05, 0.1, 0.15, 0.2, 0.25):
    print(f"P(min coord > {t}): hard {sum(s['mn']>t for s in H)/len(H):.3f}  ctrl {sum(s['mn']>t for s in Cc)/len(Cc):.3f}  simplex {(1-3*t)**2:.3f}")
