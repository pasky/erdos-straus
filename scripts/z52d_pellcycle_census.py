r"""z52d PELLCYCLE census: full-cycle roots of sqrt(p) as forest roots vs random roots.

Families (Z52D_PELLCYCLE.md §3):
  Z   the 14 (★)-zeros <= 1e10 (FRONTIER §2.1)
  N   named hard primes 2521, 3361 (b=1 / least-QNR failures)
  D   first ND primes p = 2521 + 9240a with q=(p+11)/12 prime (LOWER_TAIL_ASTRA Thm 5.1 family)
  C24 size-matched controls: for every Z/N/D prime, NC random primes p' ≡ 1 (24) with |p'-p| <= 0.1p (seeded)
  CD  Dickson-class controls: p ≡ 2521 (9240), (p+11)/12 composite, nearest to each D prime (one each)
  H   near-square H-family instances (m = 60t, five forms prime; Z52D_PELLCYCLE.md Thm 1.1)
For each prime and each root set R0..R3 (lib.root_sets): per-root status of
  depth-2 ball (bichromatic edge on a path of length <= 2 from the root) and full component (cap -> 'censored');
baselines per root u >= 8 (smaller roots are kept, they are fixed roots):
  'size'  : K uniform draws from [ceil(0.8u), floor(1.25u)] \ pZ
  'sizecol': same, conditioned on chi_p(u') = chi_p(u)
Usage: uv run --with sympy python scripts/z52d_pellcycle_census.py OUT.jsonl [ND] [NC] [K] [SHARD NSHARD]
  (rng is reseeded per prime from p, so shards are reproducible and independent)
"""
import json
import random
import sys
import time

from sympy import isprime, nextprime

from z52d_pellcycle_lib import chi, explore, root_sets

RSTAR0 = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
NAMED = [2521, 3361]
CAP = 100000


def dickson_family(n):
    out, a = [], 0
    while len(out) < n:
        p = 2521 + 9240 * a
        if isprime(p) and isprime((p + 11) // 12):
            out.append(p)
        a += 1
    return out


def dickson_controls(Dlist):
    out = []
    used = set()
    for p in Dlist:
        a0 = (p - 2521) // 9240
        for da in sorted(range(-40, 41), key=abs):
            a = a0 + da
            if a < 0:
                continue
            p2 = 2521 + 9240 * a
            if p2 not in used and isprime(p2) and not isprime((p2 + 11) // 12):
                out.append(p2)
                used.add(p2)
                break
    return out


def h_family(n):
    out, t = [], 1
    while len(out) < n:
        m = 60 * t
        fs = [m * m + 1, (m * m + 2) // 2, (m * m + 3) // 3, (m * m + 4) // 4, (m * m + 5) // 5]
        if all(isprime(f) for f in fs):
            out.append(m * m + 1)
        t += 1
    return out


def controls24(p, k, rng, used):
    out = []
    lo, hi = int(0.9 * p), int(1.1 * p)
    tries = 0
    while len(out) < k and tries < 100000:
        tries += 1
        x = rng.randrange(lo, hi)
        x -= (x - 1) % 24  # x ≡ 1 (24)
        if x > 24 and x not in used and isprime(x):
            out.append(x)
            used.add(x)
    return out


def draw(p, u, rng, colour=None):
    lo, hi = -(-4 * u // 5), (5 * u) // 4
    for _ in range(1000):
        x = rng.randint(lo, hi)
        if x % p == 0 or x > p + 2:
            continue
        if colour is None or chi(p, x) == colour:
            return x
    return None


def run_prime(p, fam, rng, K):
    rs = root_sets(p)
    memo_full = {}

    def full(u):
        if u not in memo_full:
            memo_full[u] = explore(p, u, cap=CAP)[0]
        return memo_full[u]

    def d2(u):
        return explore(p, u, depth=2, cap=CAP)[0]

    rec = dict(p=p, fam=fam, periodS=rs["periodS"], periodW=rs["periodW"])
    for name in ("R0", "R1", "R2", "R3"):
        R = sorted(rs[name])
        st = {u: (d2(u), full(u)) for u in R}
        nh2 = sum(s[0] == "hit" for s in st.values())
        nhf = sum(s[1] == "hit" for s in st.values())
        ncen = sum(s[1] == "censored" for s in st.values())
        big = [u for u in R if u >= 8]
        # baselines
        base = {}
        for bname, col in (("size", False), ("sizecol", True)):
            h2 = hf = tot = 0
            anyf = anyd = 0
            for k in range(K):
                rep = []
                for u in big:
                    x = draw(p, u, rng, chi(p, u) if col else None)
                    if x is None:
                        continue
                    rep.append(x)
                    s2, sf = d2(x), full(x)
                    tot += 1
                    h2 += s2 == "hit"
                    hf += sf == "hit"
                small = [u for u in R if u < 8]
                anyd += any(st[u][0] == "hit" for u in small) or any(d2(x) == "hit" for x in rep)
                anyf += any(st[u][1] == "hit" for u in small) or any(full(x) == "hit" for x in rep)
            base[bname] = dict(tot=tot, hit2=h2, hitf=hf, any2=anyd, anyf=anyf, K=K)
        rec[name] = dict(
            n=len(R), nbig=len(big), hit2=nh2, hitf=nhf, cens=ncen,
            hit2_big=sum(st[u][0] == "hit" for u in big), hitf_big=sum(st[u][1] == "hit" for u in big),
            any2=nh2 > 0, anyf=nhf > 0,
            small_hitf=sum(st[u][1] == "hit" for u in R if u < 8),
            hits=[u for u in R if st[u][1] == "hit"][:50],
            base=base,
        )
    return rec


def main():
    out = sys.argv[1]
    ND = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    NC = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    rng = random.Random(20261101)
    D = dickson_family(ND)
    tests = [(p, "Z") for p in RSTAR0] + [(p, "N") for p in NAMED] + [(p, "D") for p in D if p not in NAMED]
    used = set(p for p, _ in tests)
    ctrl = []
    for p, _ in tests:
        ctrl += [(x, "C24") for x in controls24(p, NC, rng, used)]
    ctrl += [(x, "CD") for x in dickson_controls(D)]
    H = [(p, "H") for p in h_family(6)]
    allp = tests + ctrl + H
    if len(sys.argv) > 6:  # shard: SHARD NSHARD
        sh, nsh = int(sys.argv[5]), int(sys.argv[6])
        allp = allp[sh::nsh]
    print(f"tests {len(tests)} controls {len(ctrl)} H {len(H)}", file=sys.stderr)
    t0 = time.time()
    with open(out, "w") as f:
        for i, (p, fam) in enumerate(allp):
            rec = run_prime(p, fam, random.Random(1000003 * p + 17), K)
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if i % 20 == 0:
                print(i, p, fam, f"{time.time() - t0:.0f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
