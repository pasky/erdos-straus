#!/usr/bin/env python3
"""Hostile review (round 2) of POINTWISE_OMEGA.md §9.  Independent code.

For given T and quarantine levels z:
  * enumerate every M<=T, M=3 (4); m = z-smooth part, r = M/m; if r>1 the surviving atoms are
    D | A^2 with m | 4D+1, event (r, -4D mod r);
  * Lemma 9.1: m <= r^2+1 for every surviving atom;
  * S_tot (raw: sum over (M,D) of 1/phi(r)), S_ev (distinct events), w_l (distinct events),
    H_PP ratio max_l w_l * 8 log T / log z, and the Lemma 9.2 proof chain
    S_tot <= (2/3) max(r/phi(r)) (3+log X) sum_{s r'^2<=X} tau(4 s r'^2+1)/(s r');
  * Theorem 9.4's local-lemma hypothesis checked literally on the event graph when H_PP holds:
    for every event E, prod_{E' ~ E} (1 - 2/phi(r_E')) >= 1/2.
  * Theorem 9.3 structure at z = T^{1/3+eps}: rough parts have <= 2 prime factors; bad primes
    B = {g_l > 1/4}; enlarged single sets G'_l after quarantining B; max g'_l; pair weights
    w'_l under mu' and the LLL condition with x_E = 2 mu'(E).
Extra (first call only): Lemma 9.1 parametrisation vs direct enumeration for primes l<200,
F^full_19, the 19^3 example, and l = 87359.
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_haar.py T z1 [z2 ...] [--theta eps]
"""
import sys
from math import log, isqrt, prod
from collections import defaultdict
from sympy import factorint, primerange, isprime, divisor_count, totient


def sqdivs(A):
    ds = [1]
    for p, e in factorint(A).items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


def phi_from(f):
    return prod(p ** (e - 1) * (p - 1) for p, e in f.items())


def atoms(T, z):
    """yield (M, m, r, rf, D) for surviving atoms."""
    for M in range(3, T + 1, 4):
        f = factorint(M)
        m = prod(p ** e for p, e in f.items() if p <= z)
        r = M // m
        if r == 1:
            continue
        rf = {p: e for p, e in f.items() if p > z}
        A = (M + 1) // 4
        for D in sqdivs(A):
            if (4 * D + 1) % m == 0:
                yield M, m, r, rf, D


def analyse(T, z):
    S_tot = 0.0
    ev = {}
    viol = 0
    natoms = 0
    max_r_over_phi = 1.0
    for M, m, r, rf, D in atoms(T, z):
        natoms += 1
        if m > r * r + 1:
            viol += 1
        ph = phi_from(rf)
        S_tot += 1.0 / ph
        max_r_over_phi = max(max_r_over_phi, r / ph)
        ev[(r, (-4 * D) % r)] = (ph, tuple(rf))
    S_ev = sum(1.0 / ph for ph, _ in ev.values())
    w = defaultdict(float)
    for (r, a), (ph, ps) in ev.items():
        for p in ps:
            w[p] += 1.0 / ph
    ratio = max(w.values()) * 8 * log(T) / log(z)
    # Lemma 9.2 chain
    X = (T + 1) // 4
    ssum = 0.0
    for rp in range(1, isqrt(X) + 1):
        for s in range(1, X // (rp * rp) + 1):
            if any(e > 1 for e in factorint(s).values()):
                continue
            ssum += divisor_count(4 * s * rp * rp + 1) / (s * rp)
    chain = (2.0 / 3.0) * max_r_over_phi * (3 + log(X)) * ssum
    print(f"T={T} z={z}: atoms={natoms} events={len(ev)} Lemma9.1 viol={viol} S_tot={S_tot:.2f} "
          f"S_ev={S_ev:.2f} chain-bound={chain:.1f} (>=S_tot: {chain >= S_tot}) "
          f"H_PP ratio={ratio:.3f}")
    lll = None
    if ratio <= 1:
        # literal check of Theorem 9.4's LLL hypothesis
        worst = 1.0
        for (r, a), (ph, ps) in ev.items():
            # neighbours: events sharing a prime, excluding E itself
            s = sum(2 * w[p] for p in ps) - 2 * (len(ps)) / ph  # upper bound on sum x_E' (E' != E)
            # exact product would need neighbour list; use prod >= exp(-2 sum x) (x<=1/2)
            from math import exp
            worst = min(worst, exp(-2 * s))
        lll = worst
        print(f"   Thm 9.4 LLL: min_E prod_(E'~E)(1-x_E') >= {worst:.3f} (needs >= 0.5: {worst >= 0.5})")
    return viol == 0 and chain >= S_tot, ev, w


def thm93(T, eps):
    y = T ** (1 / 3 + eps)
    single = defaultdict(set)   # l -> forbidden residues mod l^{e_l}
    pairs = []
    emax = {}
    for p in primerange(int(y) + 1, T + 1):
        e = 1
        while p ** (e + 1) <= T:
            e += 1
        emax[p] = e
    multi_bad = 0
    for M, m, r, rf, D in atoms(T, y):
        ps = sorted(rf)
        if sum(rf.values()) > 2:
            multi_bad += 1
        a = (-4 * D) % r
        if len(ps) == 1:
            l = ps[0]
            mod = l ** emax[l]
            # residues mod l^e forbidden: those = a mod r
            single[l].update(x for x in range(a % r, mod, r))
        else:
            pairs.append((ps[0], ps[1], a))
    g = {l: len(single[l]) / totient(l ** emax[l]) for l in emax}
    one_in = sum(1 for l in emax if 1 in single[l])
    B = {l for l in emax if g[l] > 0.25}
    # enlarge single sets at good primes from pairs with one bad prime
    G2 = {l: set(single[l]) for l in emax if l not in B}
    good_pairs = []
    imp = conv = 0
    for l1, l2, a in pairs:
        b1, b2 = l1 in B, l2 in B
        if b1 and b2:
            if a % (l1 * l2) == 1:
                print("Fact 1.1 violated?!")
            imp += 1
        elif b1 or b2:
            b, l = (l1, l2) if b1 else (l2, l1)
            if a % b == 1:
                conv += 1
                mod = l ** emax[l]
                G2[l].update(x for x in range(a % l, mod, l))
            else:
                imp += 1
        else:
            good_pairs.append((l1, l2, a))
    g2 = {l: len(G2[l]) / totient(l ** emax[l]) for l in G2}
    gmax2 = max(g2.values()) if g2 else 0
    # mu'(E) = prod over the two primes of P'(X_l = a mod l)
    def mup(l, a):
        mod = l ** emax[l]
        allowed = totient(mod) - len(G2[l])
        hits = sum(1 for x in range(a % l, mod, l) if x not in G2[l] and x % l)
        return hits / allowed
    evs = {}
    for l1, l2, a in good_pairs:
        evs[(l1, l2, a % (l1 * l2))] = mup(l1, a) * mup(l2, a)
    wp = defaultdict(float)
    for (l1, l2, a), mu in evs.items():
        wp[l1] += mu
        wp[l2] += mu
    from math import exp
    worst = 1.0
    for (l1, l2, a), mu in evs.items():
        s = 2 * (wp[l1] + wp[l2]) - 4 * mu
        worst = min(worst, exp(-2 * s))
    print(f"Thm 9.3 at T={T}, eps={eps}: y={y:.1f}, rough parts with >2 prime factors: {multi_bad}, "
          f"1 in G_l at {one_in} primes, |B|={len(B)}, pairs: total {len(pairs)}, impossible {imp}, "
          f"converted {conv}, good events {len(evs)}; max g'={float(gmax2):.3f}; "
          f"max w'={float(max(wp.values())) if wp else 0:.4f}; LLL min prod >= {worst:.3f} (need 0.5)")
    return multi_bad == 0 and one_in == 0


def extras():
    ok = True
    # parametrisation vs direct for primes l < 200 (F^full, r = l, D <= A)
    mism = 0
    for l in primerange(5, 200):
        direct = set()
        for m in range(1, l * l + 2):
            M = m * l
            if M % 4 != 3:
                continue
            A = (M + 1) // 4
            for D in sqdivs(A):
                if D <= A and (4 * D + 1) % m == 0:
                    direct.add((m, D))
        para = set()
        for n in range(1, l // 2 + 1):
            for rp in range(1, n + 1):
                if n % rp:
                    continue
                s = n // rp
                if any(e > 1 for e in factorint(s).values()):
                    continue
                X = 4 * n * rp + 1
                for v in range(1, X + 1):
                    if X % v or (l + v) % (4 * n):
                        continue
                    m = X // v
                    k = m * (l + v) // (4 * n) - rp
                    if k >= rp and (m * l) % 4 == 3:
                        para.add((m, s * rp * rp))
        mism += (direct != para)
    print(f"Lemma 9.1 parametrisation vs direct enumeration, primes 5<=l<200: mismatching primes {mism}")
    ok &= mism == 0
    Ff = set()
    for m in range(1, 19 * 19 + 2):
        M = 19 * m
        if M % 4 != 3:
            continue
        for D in sqdivs((M + 1) // 4):
            if (4 * D + 1) % m == 0:
                Ff.add((-4 * D) % 19)
    print(f"F^full_19 = {sorted(Ff)}; 19^3 example: A={(19**3 + 1) // 4}={factorint((19**3+1)//4)}, "
          f"7 | A^2: {((19**3+1)//4)**2 % 7 == 0}, class mod 19 = {(-28) % 19}")
    l = 87359
    print(f"l=87359 prime: {isprime(l)}, (l+1)/4 = {factorint((l + 1) // 4)}, tau(A^2)={divisor_count(((l+1)//4)**2)}")
    return ok


if __name__ == "__main__":
    args = sys.argv[1:]
    eps = None
    if "--theta" in args:
        i = args.index("--theta")
        eps = float(args[i + 1])
        del args[i:i + 2]
    T = int(args[0])
    ok = True
    if "--extras" in args:
        args.remove("--extras")
        ok &= extras()
    for z in args[1:]:
        r, ev, w = analyse(T, int(z))
        ok &= r
        if T == 100000 and int(z) == 100:
            print(f"   l=87359: l*w_l = {87359 * w.get(87359, 0):.1f}")
    if eps is not None:
        ok &= thm93(T, eps)
    print("ALL OK" if ok else "FAILURE")
    sys.exit(0 if ok else 1)
