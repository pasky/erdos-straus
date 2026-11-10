# z70 LOOSE item 5 (I9 rerun): p = X^2 + 840 Y^2 (p in the six Mordell classes mod 840),
# Q(p) = [exists prime q | X with (840/q) = -1].
# Pre-registered design (Z70_LOOSE.md §1.5): disjoint controls, 20 per hard prime, same class mod 840,
# uniform in [p/2, 2p], no hard-list member, no reuse anywhere in the design. Effect bound 0.10 (noprime set).
# q-to-word construction: least such q; f = q*m (m <= 64), f = 3 mod 4, f <= (4p+1)/3; Y = [some f is a (*) witness:
# r = (-p mod f) divides (f+1)/4].  Decoy q': nearest prime with (p/q') = -1, q' !| X, q' = q mod 8, |q'-q| <= 0.1 q.
import sys, math, random, json
sys.path.insert(0, 'scripts')
from sympy import isprime, factorint, jacobi_symbol, legendre_symbol
from z69_twist_i9 import rep840, load, MOR

SETS = {'star14': 'data/z58/screens/star_prime_zeros.txt', 'gstar38': 'data/z58/screens/gstar_zeros.txt',
        'noprime231': 'data/z68/u7f/noprime_primes_1e9.txt', 'u8zero': 'data/z68/u7f/u8zero_primes_1e8.txt',
        'r8zero12': 'data/z58/screens/r8_zeros_1e10.txt'}

def badq(p):
    X, Y = rep840(p)
    fx = factorint(X) if X > 1 else {}
    return X, Y, sorted(q for q in fx if q > 2 and jacobi_symbol(840, q) == -1)

def yword(p, q, M=64):
    lim = (4 * p + 1) // 3
    for m in range(1, M + 1):
        f = q * m
        if f > lim: break
        if f % 4 != 3: continue
        r = (-p) % f
        if r and ((f + 1) // 4) % r == 0: return 1
    return 0

def decoy(p, q, X, win=True):
    for k in range(1, (int(0.1 * q) + 2) if win else 10**6):
        for c in (q - k, q + k):
            if c > 2 and (abs(c - q) <= 0.1 * q or not win) and c % 8 == q % 8 and isprime(c) and X % c and legendre_symbol(p % c, c) == -1:
                return c
    return None

def main(seed=7070, NC=20):
    rng = random.Random(seed)
    hard = {}
    allhard = set()
    for name, fn in SETS.items():
        H = [p for p in load(fn) if p % 840 in MOR and isprime(p)]
        hard[name] = H; allhard |= set(load(fn))
    used = set()
    out = {}
    for name, H in hard.items():
        rows = []
        for p in H:
            lo, hi = (p // 2) // 840, (2 * p) // 840
            ctl = []; tries = 0
            while len(ctl) < NC and tries < 200000:
                tries += 1
                c = 840 * rng.randint(lo, hi) + p % 840
                if c < p / 2 or c > 2 * p or c in used or c in allhard or not isprime(c): continue
                used.add(c); ctl.append(c)
            X, Y, bq = badq(p)
            hrow = {'p': p, 'X': X, 'Y': Y, 'bad': bq, 'Q': int(bool(bq))}
            if bq:
                q = bq[0]; hrow['Yq'] = yword(p, q); d = decoy(p, q, X); hrow['qd'] = d
                hrow['Yd'] = yword(p, d) if d else None
                d2 = decoy(p, q, X, False); hrow['Yd2'] = yword(p, d2)  # amendment: nearest decoy, no 10% window
            cq = []
            for c in ctl:
                Xc, Yc, bc = badq(c); r = {'p': c, 'Q': int(bool(bc))}
                if bc:
                    q = bc[0]; r['Yq'] = yword(c, q); d = decoy(c, q, Xc); r['Yd'] = yword(c, d) if d else None
                    d2 = decoy(c, q, Xc, False); r['Yd2'] = yword(c, d2)
                cq.append(r)
            hrow['ctl'] = cq
            rows.append(hrow)
        out[name] = rows
        # stats
        num = 0.0; var = 0.0; n = 0
        print(f"{name}: hard primes without any control in [p/2,2p]: {[r['p'] for r in rows if not r['ctl']]}")
        for r in rows:
            m = len(r['ctl'])
            if m == 0: continue
            n += 1; cb = sum(c['Q'] for c in r['ctl']) / m
            num += r['Q'] - cb; var += cb * (1 - cb) * (1 + 1 / m)
        D = num / n; se = math.sqrt(var) / n
        print(f"{name}: n={n} hard Q={sum(r['Q'] for r in rows)/len(rows):.3f} ctl Q={sum(c['Q'] for r in rows for c in r['ctl'])/sum(len(r['ctl']) for r in rows):.3f} "
              f"Delta={D:+.4f} (strata={n}) se={se:.4f} z={D/se if se else 0:+.2f} 95%CI=({D-1.96*se:+.3f},{D+1.96*se:+.3f})")
        # q-to-word
        for lab, pool, key in (('hard', rows, 'Yd'), ('ctl', [c for r in rows for c in r['ctl']], 'Yd'),
                               ('hard/amended', rows, 'Yd2'), ('ctl/amended', [c for r in rows for c in r['ctl']], 'Yd2')):
            pr = [(r['Yq'], r[key]) for r in pool if r['Q'] and r.get(key) is not None]
            b = sum(1 for a, d in pr if a and not d); c = sum(1 for a, d in pr if d and not a)
            z = (b - c) / math.sqrt(b + c) if b + c else 0
            print(f"   q-to-word {lab}: pairs={len(pr)} Y(q)={sum(a for a,_ in pr)/max(1,len(pr)):.3f} Y(q')={sum(d for _,d in pr)/max(1,len(pr)):.3f} McNemar b={b} c={c} z={z:+.2f}; "
                  f"Q-primes without decoy={sum(1 for r in pool if r['Q'] and r.get(key) is None)}")
        sys.stdout.flush()
    json.dump(out, open('data/z70/loose/i9_rows.json', 'w'))

if __name__ == '__main__':
    main()
