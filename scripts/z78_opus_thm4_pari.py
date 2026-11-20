"""Opus cross-review: independent PARI test of PROTH_ALLM Thm 4 index pattern and core existence, h beyond 61.
Usage: python scripts/z78_opus_thm4_pari.py h1 h2 ...   (odd h). Prints index [U:R], [U:<all B>], core-ok."""
import sys, math, time, cypari2
pari = cypari2.Pari(); pari.allocatemem(400 * 10**6)

def run(h):
    t0 = time.time(); H = 2**h - 1; k = 2*H + 1
    G = pari.znstar(H, 1); cyc = [int(c) for c in pari('(G)->G.cyc')(G)]
    r = len(cyc)
    def lg(x): return [int(v) for v in pari.znlog(pari.Mod(x % H, H), G)]
    B = lambda a: 1 + pow(2, a % h, H)
    cols = []
    for g in [d for d in range(1, h+1) if h % d == 0]:
        base = B(g); ib = pow(base, -1, H)
        for a in range(h):
            if math.gcd(a, h) == g and a != g % h: cols.append(lg(B(a)*ib))
    diag = [[cyc[i] if i == j else 0 for i in range(r)] for j in range(r)]
    def index(extra):
        M = pari.matrix(r, len(cols) + len(extra) + r, [v for row in zip(*(cols + extra + diag)) for v in row])
        return int(abs(pari.matdet(pari.mathnf(M))))
    idx = index([])
    allB = index([lg(B(a)) for a in range(h)])
    divh = [d for d in range(1, h+1) if h % d == 0]
    mu = lambda n: int(pari.moebius(n))
    E = {d: math.prod(pow(B(b), mu(d//b), H) for b in divh if d % b == 0) % H for d in divh}
    cs = [c for c in (int(x) for x in pari.divisors(k)) if c % 16 == (14*H - 1) % 16]
    found = None; found0 = None
    for c in cs:
        for mask in range(1 << len(divh)):
            x = c
            for i, d in enumerate(divh):
                if mask >> i & 1: x = x*E[d] % H
            tgt = (-pow(x, -1, H)) % H
            if index([lg(tgt)]) == idx:
                found = (c, [d for i, d in enumerate(divh) if mask >> i & 1])
                if mask == 0: found0 = c
                break
        if found: break
    print(f'h={h} 3|h={h%3==0} 9|h={h%9==0} [U:R]={idx} [U:<B>]={allB} core={found} t={time.time()-t0:.1f}s', flush=True)

for a in sys.argv[1:]: run(int(a))
