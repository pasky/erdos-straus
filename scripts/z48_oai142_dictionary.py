"""z48 / oai142: auxiliary primes (OAI-142 style) versus ES candidate events.

Companion to OAI_METHOD_142.md.  Pure Python, memory-light (one prime sieve).

Part A  exact check of the "index-m relaxation" identity
        ell = 4uC-1,  ell | p*g^m + u,  B = (p*g^m+u)/ell  ==>
        4/p = g^m/(uBC) + 1/(pBC) + 1/(puC)          (m = 0 / g = 1 is (*))
Part B  per-prime table: 142's auxiliary primes for q = 2, 3; the least prime
        ell = 3 (4) giving the index-2 (square-numerator) relaxation at u = 1;
        the least prime modulus and least modulus carrying an actual (*) hit.
Part C  growth of candidate counts with the search bound X at fixed p:
        142-type successes ~ X/log X versus ES successes ~ log X.
Part D  (*)-failure primes: full scans show no (*) hit at any modulus, while
        the 142-type auxiliary prime and the index-2 relaxation are tiny.

Usage: uv run python scripts/z48_oai142_dictionary.py [PMAX] > data/z48_oai142/summary.txt
"""
import math
import random
import sys
from fractions import Fraction

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
SIEVE = max(PMAX, 12_000_000)  # covers full (*) scans for p <= 8 813 281


def sieve(n):
    b = bytearray([1]) * (n + 1)
    b[0] = b[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if b[i]:
            b[i * i :: i] = bytearray(len(range(i * i, n + 1, i)))
    return b


IS_P = sieve(SIEVE)


def primes_in_class(mod, res, start=2):
    x = start + ((res - start) % mod)
    while x <= SIEVE:
        if IS_P[x]:
            yield x
        x += mod
    raise RuntimeError(f"sieve exhausted (bound {SIEVE}) in class {res} mod {mod}")


def aux_q(p, q):
    """142's auxiliary prime: ell = 1 (12q), ell not in {2,3,p,q}, p not a q-th power mod ell."""
    for ell in primes_in_class(12 * q, 1):
        if ell == p:
            continue
        if pow(p, (ell - 1) // q, ell) != 1:
            return ell


def sq_relax(p):
    """least prime ell = 3 (4) with (ell/p) = -1: index-2 relaxation at u = 1."""
    for ell in primes_in_class(4, 3):
        if pow(ell, (p - 1) // 2, p) == p - 1:
            return ell


def star_hit(p, m):
    """(*) hit with modulus m = 4uC-1 (m = 3 mod 4): u = (-p mod m) must divide (m+1)/4."""
    u = (-p) % m
    if u == 0:
        return None
    k = (m + 1) // 4
    if k % u == 0:
        C = k // u
        B = (p + u) // m
        return (u, B, C)
    return None


def least_star(p, prime_only, bound):
    m = 3
    while m <= bound:
        if (not prime_only) or IS_P[m]:
            h = star_hit(p, m)
            if h:
                return m, h
        m += 4
    return None, None


def check_solution(p, u, B, C, gm=1):
    lhs = Fraction(4, p)
    rhs = Fraction(gm, u * B * C) + Fraction(1, p * B * C) + Fraction(1, p * u * C)
    return lhs == rhs


def part_a(out):
    rng = random.Random(142)
    ok = 0
    trials = 0
    for _ in range(3000):
        p = rng.choice([q for q in range(10_001, 10_301) if IS_P[q] and q % 4 == 1])
        u = rng.randint(1, 30)
        C = rng.randint(1, 30)
        ell = 4 * u * C - 1
        if not IS_P[ell] or ell == p:
            continue
        m = rng.choice([1, 2, 3, 4, 6])
        # find g with ell | p g^m + u
        for g in range(1, ell):
            if (p * pow(g, m, ell) + u) % ell == 0:
                break
        else:
            continue
        trials += 1
        B = (p * g ** m + u) // ell
        assert 4 * u * B * C - u - B == p * g ** m
        ok += check_solution(p, u, B, C, g ** m)
    out.append(f"[A] relaxation identity: {ok}/{trials} exact (Fraction) checks passed")
    return ok == trials


def part_b(out):
    rows = []
    worst = {}
    for p in range(97, PMAX + 1, 24):  # p = 1 (24)
        if not IS_P[p]:
            continue
        L2 = math.log(p) ** 2
        track = p >= 10_000
        a2, a3, s2 = aux_q(p, 2), aux_q(p, 3), sq_relax(p)
        mP, _ = least_star(p, True, 4 * p // 3 + 1)
        mA, hA = least_star(p, False, 4 * p // 3 + 1)
        if hA:
            assert check_solution(p, *hA)
        rows.append((p, a2, a3, s2, mP, mA))
        for name, v in (("aux2", a2), ("aux3", a3), ("sq", s2), ("starPrime", mP), ("starAny", mA)):
            r = (v if v else float("inf")) / L2
            if track and (name not in worst or r > worst[name][0]):
                worst[name] = (r, p, v)
            if track and v and (name + "_fin" not in worst or r > worst[name + "_fin"][0]):
                worst[name + "_fin"] = (r, p, v)
    n = len(rows)
    out.append(f"[B] primes p = 1 (24), 97 <= p <= {PMAX}: {n} (maxima over p >= 10^4)")
    for name in ("aux2", "aux3", "sq", "starPrime", "starAny", "starPrime_fin", "starAny_fin"):
        if name not in worst:
            out.append(f"    max {name}: no data (need p >= 10^4)")
            continue
        r, p, v = worst[name]
        out.append(f"    max {name:9s}/log^2 p = {r:8.3f}  at p = {p} (value {v})")
    none_prime = [r[0] for r in rows if r[4] is None]
    none_any = [r[0] for r in rows if r[5] is None]
    out.append(f"    primes with NO prime-modulus (*) hit at all: {len(none_prime)}; first: {none_prime[:12]}")
    out.append(f"    primes with NO (*) hit at all (R(p)=0): {len(none_any)}: {none_any}")
    return rows


def part_c(out, samples):
    out.append("[C] counts of successful candidates with modulus <= X at fixed p")
    out.append("    p           X   #aux2(142,q=2)  #sq-relax(u=1)  #(*)prime-mod hits  #(*) hits")
    for p in samples:
        for X in (10**3, 10**4, 10**5, 10**6):
            n_aux = sum(1 for ell in range(1, X + 1, 24) if IS_P[ell] and ell != p and pow(p, (ell - 1) // 2, ell) == ell - 1)
            n_sq = sum(1 for ell in range(3, X + 1, 4) if IS_P[ell] and ell != p and pow(ell, (p - 1) // 2, p) == p - 1)
            n_sp = sum(1 for m in range(3, X + 1, 4) if IS_P[m] and star_hit(p, m))
            n_s = sum(1 for m in range(3, X + 1, 4) if star_hit(p, m))
            out.append(f"    {p:<10d} {X:>8d} {n_aux:>12d} {n_sq:>15d} {n_sp:>15d} {n_s:>14d}")


def part_d(out):
    fails = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281]
    out.append("[D] (*)-failure primes (p = 1 (8)): full scan of all moduli m <= (4p+1)/3")
    out.append("    p         aux2  aux3  sq-relax(u=1, ell)  lowest-terms odd-square-numerator solution checked  (*) hits")
    for p in fails:
        a2, a3, s2 = aux_q(p, 2), aux_q(p, 3), sq_relax(p)
        mA, _ = least_star(p, False, (4 * p + 1) // 3)
        # explicit relaxed solution 4/p = g^2/(BC) + 1/(pBC) + 1/(pC), ell = s2
        C = (s2 + 1) // 4
        # Thm 2.2 lift: least g odd, gcd(g, pC) = 1, p g^2 = -1 (mod ell); then gcd(g, BC) = 1 automatically
        g = next(g for g in range(1, 2 * s2 * C * p) if g % 2 == 1 and math.gcd(g, p * C) == 1 and (p * g * g + 1) % s2 == 0)
        B = (p * g * g + 1) // s2
        ok = check_solution(p, 1, B, C, g * g) and math.gcd(g, B * C) == 1
        out.append(f"    {p:<9d} {a2:>5d} {a3:>5d} {s2:>10d} (g={g}, B={B}, C={C})  {ok}   {'none' if mA is None else mA}")


def main():
    out = []
    assert part_a(out)
    part_b(out)
    samp = [next(q for q in range(10**6 + 1, 2 * 10**6, 24) if IS_P[q]), 8_813_281, 409]
    part_c(out, samp)
    part_d(out)
    print("\n".join(out))


if __name__ == "__main__":
    main()
