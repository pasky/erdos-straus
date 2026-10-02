"""EXCEPTIONAL_TWIN §2 numerics: the capped measure Q' with the QR base.

Real Case-B system: all classes of R(M), M = 3 mod 4, M <= X.  Primes are
processed in increasing order (singleton windows).  Base: for p <= W,
n mod p^e is uniform on residues that are nonzero squares mod p (p odd).
For p > W: light (p(h) <= thr(p)) -> uniform off F_p(h); heavy -> uniform.
Records per sample: realised leak (did n hit a class?), the expected leak
sum_p p(h) 1{heavy}, and the light profile.  Also asserts that no class with
top prime <= W is ever hit (Lemma 1.3(1)).

Usage: uv run python scripts/twin_capped.py X samples W kappa [types]
  thr(p) = p^-kappa (kappa=0 means thr = 1/4); types = comma list of
  dom,gapM,gapB,twin or 'all' (default all); 7th arg 'cap' uses
  thr(p) = min(1/4, p^-kappa), the theorem-compatible threshold.
"""
import random
import sys
from collections import defaultdict

sys.path.insert(0, "scripts")
from balanced_numerics import build_system


def run(X, samples, W, kappa, types, seed=7, capq=False):
    sysd, maxexp, _ = build_system(X, 0.25)
    for p in list(sysd):
        sysd[p] = [c for c in sysd[p] if c[4] in types or p <= W]
    primes = sorted(maxexp)
    rng = random.Random(seed)
    thr = (lambda p: 0.25) if kappa == 0 else (lambda p: min(0.25, p ** (-kappa)) if capq else p ** (-kappa))
    hits = 0
    exp_leak = []
    band_leak = defaultdict(float)
    band_heavy = defaultdict(int)
    prof = defaultdict(float)
    for _ in range(samples):
        n, L = 0, 1
        hit = False
        el = 0.0
        for p in primes:
            e = maxexp[p]
            pe = p ** e
            forb = set()
            qc = {}
            for (q, cq, cv, v, t, M) in sysd.get(p, ()):
                r = qc.get(q)
                if r is None:
                    r = qc[q] = n % q
                if r == cq:
                    for r2 in range(cv, pe, p ** v):
                        forb.add(r2)
            pl = len(forb) / pe
            if p <= W:
                if p == 2:
                    r = rng.randrange(pe)
                else:
                    while True:
                        r = rng.randrange(pe)
                        if r % p and pow(r % p, (p - 1) // 2, p) == 1:
                            break
                assert r not in forb, ("QR base hit a class", p, r)
            elif pl <= thr(p):
                while True:
                    r = rng.randrange(pe)
                    if r not in forb:
                        break
                b = p.bit_length()
                prof[b] += pl
            else:
                r = rng.randrange(pe)
                el += pl
                b = p.bit_length()
                band_leak[b] += pl
                band_heavy[b] += 1
                if r in forb:
                    hit = True
            n = n + L * (((r - n) * pow(L, -1, pe)) % pe)
            L *= pe
        hits += hit
        exp_leak.append(el)
    out = [f"# X={X} samples={samples} W={W} kappa={kappa} cap1/4={capq} types={','.join(sorted(types))}",
           f"realised leak Q'(not avoider) ~ {hits/samples:.4f}",
           f"mean expected leak sum p 1{{heavy}} = {sum(exp_leak)/samples:.4f}  max = {max(exp_leak):.4f}",
           "# band [2^(b-1),2^b): E[sum p 1{heavy}], mean #heavy primes, E[light profile]"]
    for b in sorted(set(band_leak) | set(prof)):
        out.append(f"{b:3d} {band_leak[b]/samples:.4f} {band_heavy[b]/samples:.3f} {prof[b]/samples:.4f}")
    return "\n".join(out)


if __name__ == "__main__":
    X = int(sys.argv[1]); S = int(sys.argv[2]); W = int(sys.argv[3]); kap = float(sys.argv[4])
    types = set(sys.argv[5].split(",")) if len(sys.argv) > 5 and sys.argv[5] != "all" else {"dom", "gapM", "gapB", "twin"}
    capq = len(sys.argv) > 6 and sys.argv[6] == "cap"
    print(run(X, S, W, kap, types, capq=capq))
