"""O192 §3: a fixed-modulus Type II shot family for the order-3 TES over Z[w], and its cubic mute variant.

TES(n): 9/n = w/x + w^2/y + 2/z, x, y, z 2-primary (TWISTED_T1 §3).
Shot (SYNTHESIS_SPARKS2 Prop 3.1): D = Q^3, g | n + 18 D, g ≡ g0 := 10 + w (mod 18) [g ≡ -w^2 (9), g ≡ w (2)],
E = (n + 18D)/g, x = (w n + E)/9, a = (g + w^2)/9, y = n a, z = n x a / D.
Checks:
 (1) T1_3 prediction: every prime element r ≡ g0 (mod 18) has 18 a non-cube mod r (cubic class of 18 ≠ 0); value set.
 (2) every 2-primary split prime pi, N(pi) <= X: least prime r ≡ g0 (18) with (pi/r)_3 = (18/r)_3, Q in Z with
     Q^3 ≡ -pi/18 (mod r); builds the solution, verifies the equation exactly, 2-primarity, Type II shape at pi,
     and computes the cubic tame invariants at every prime of Q (mute places) and at pi.
 (3) cubes pi^3: no divisor g ≡ g0 (18) of pi^3 + 18 Q^3 for small Q (T1_3 control).
 (4) plain TES (Q = 1 only): which pi have a divisor g ≡ g0 (18) of pi + 18.
usage: PYTHONPATH=scripts uv run python scripts/syn2_tes_shots.py X [Ncube]
"""
import sys
from math import gcd as igcd
import tw_eis as E
import sympy

E.factor_int = lambda n: dict(sympy.factorint(n))


def _split_prime_fast(p):
    """the two primes above p ≡ 1 (mod 3), via a root t of t^2 + t + 1 mod p and gcd(p, t - w)."""
    s = sympy.sqrt_mod(-3, p)
    t = (s - 1) * pow(2, -1, p) % p
    pi = E.gcd((p, 0), (t, -1))
    assert E.norm(pi) == p
    pi = E.normalise(pi)
    return (pi, E.normalise(E.conj(pi)))


E.split_prime = _split_prime_fast

W = E.W
W2 = (-1, -1)
G0 = (10, 1)


def mod18(x):
    return (x[0] % 18, x[1] % 18)


def in_class(g):
    return mod18(g) == G0


def two_primary(x):
    return (x[0] - 1) % 2 == 0 and x[1] % 2 == 0


def rat(k):
    return (k, 0)


def rational_primes(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(N + 1) if s[i]]


def class_primes(Lmax):
    """all prime elements r (any associate) with r ≡ g0 (18), N(r) = l ≤ Lmax split."""
    out = []
    for l in rational_primes(Lmax):
        if l % 3 != 1:
            continue
        for pi in E.split_prime(l):
            for u in E.UNITS:
                r = E.mul(u, pi)
                if in_class(r):
                    out.append((l, r))
    return out


def solve_shot(n, Q, g):
    D = rat(Q ** 3)
    A = E.add(n, E.mul(rat(18), D))
    Ee = E.divexact(A, g)
    assert Ee is not None
    x = E.divexact(E.add(E.mul(W, n), Ee), rat(9))
    a = E.divexact(E.add(g, W2), rat(9))
    assert x is not None and a is not None
    y = E.mul(n, a)
    Z = E.mul(E.mul(n, x), a)  # z = Z / D
    # equation  w/x + w^2/y + 2D/Z = 9/n  <=>  w n y Z + w^2 n x Z + 2 D n x y = 9 x y Z
    lhs = E.add(E.add(E.mul(E.mul(E.mul(W, n), y), Z), E.mul(E.mul(E.mul(W2, n), x), Z)),
                E.mul(E.mul(E.mul(E.mul(rat(2), D), n), x), y))
    rhs = E.mul(E.mul(E.mul(rat(9), x), y), Z)
    assert lhs == rhs, (n, Q, g)
    return x, y, Z, D


def invariants(n, x, y, Z, D, places):
    """cubic tame invariants of alpha = (-u1/u3, -u2/u3), u = (x/w, y/w^2, z/2), z = Z/D, at given primes."""
    A = (E.mul(rat(-2), E.mul(x, D)), E.mul(W, Z))
    B = (E.mul(rat(-2), E.mul(y, D)), E.mul(W2, Z))
    return {pl: E.tame_symbol(A, B, pl) for pl in places}


def main():
    X = int(sys.argv[1])
    Ncube = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    parts = sys.argv[3] if len(sys.argv) > 3 else "1234"
    CP = class_primes(max(3000, X))
    vals = {}
    for l, r in CP:
        c = E.cubic_class(rat(18), r)
        vals[c] = vals.get(c, 0) + 1
    assert set(vals) == {2}, vals
    print(f"(1) prime elements r ≡ 10+w (18), N(r) ≤ {max(3000, X)}: {len(CP)}; cubic class of 18 mod r: {vals}", flush=True)
    if "2" not in parts:
        X2 = 0
    else:
        X2 = X

    nsol, maxl, maxQ, invpi, invmute, shapes, bad = 0, 0, 0, {}, {}, 0, 0
    for l in rational_primes(X2):
        if l % 3 != 1 or l < 7:
            continue
        for pi0 in E.split_prime(l):
            for sgn in (1, -1):
                pi = None
                for u in E.UNITS:
                    c = E.mul(u, pi0)
                    if two_primary(c):
                        pi = c if sgn == 1 else E.neg(c)
                        break
                # pi and -pi are the two 2-primary associates; -1 is a cube, both are fine
                found = None
                for lr, r in CP:
                    if lr == l:
                        continue
                    if E.cubic_class(pi, r) != E.cubic_class(rat(18), r):
                        continue
                    t = E.reduce_(E.mul(E.neg(pi), rat(pow(18, -1, lr))), r)
                    for Q in range(1, 6 * lr):
                        if igcd(Q, 6 * l) == 1 and pow(Q, 3, lr) == t % lr:
                            found = (lr, r, Q)
                            break
                    if found:
                        break
                if not found:
                    bad += 1
                    print("NO SHOT", pi)
                    continue
                lr, r, Q = found
                x, y, Z, D = solve_shot(pi, Q, r)
                assert two_primary(x) and two_primary(y) and (Z[0] - D[0]) % 2 == 0 and Z[1] % 2 == 0
                vx, _ = E.valuation(x, pi)
                vy, _ = E.valuation(y, pi)
                vz = E.valuation(Z, pi)[0]
                if vx == 0 and vy >= 1 and vz >= 1:
                    shapes += 1
                places = [pi]
                for q in E.factor_int(Q):
                    places += E.primes_above(q)
                inv = invariants(pi, x, y, Z, D, places)
                invpi[inv[pi]] = invpi.get(inv[pi], 0) + 1
                for pl in places[1:]:
                    invmute[inv[pl]] = invmute.get(inv[pl], 0) + 1
                nsol += 1
                maxl, maxQ = max(maxl, lr), max(maxQ, Q)
    assert bad == 0 and shapes == nsol and set(invpi) <= {2} and set(invmute) <= {0}
    print(flush=True); print(f"(2) 2-primary split primes pi, 7 ≤ N(pi) ≤ {X}: {nsol} solved (equation exact, 2-primary), {bad} unsolved;"
          f" Type II shape at pi: {shapes}; max N(r) = {maxl}, max Q = {maxQ};"
          f" inv_pi values {invpi}; mute-place invariants {invmute}")

    # (3) cubes
    hits = 0
    tested = 0
    for l in rational_primes(Ncube if "3" in parts else 0):
        if l % 3 != 1 or l < 7:
            continue
        pi0 = E.split_prime(l)[0]
        pi = next(E.mul(u, pi0) for u in E.UNITS if two_primary(E.mul(u, pi0)))
        n = E.power(pi, 3)
        for Q in range(1, 40):
            if igcd(Q, 6 * l) != 1:
                continue
            A = E.add(n, rat(18 * Q ** 3))
            unit, fac = E.factor(A)
            for d in E.divisors(fac):
                for u in E.UNITS:
                    if in_class(E.mul(u, d)):
                        hits += 1
            tested += 1
    assert hits == 0
    print(f"(3) cubes (one 2-primary associate above one prime per split l) pi^3, N(pi) ≤ {Ncube}, Q ≤ 39: {tested} shots, divisors in class g0: {hits}")

    # (4) plain TES shot pi + 18
    fire, tot, fails = 0, 0, []
    for l in rational_primes(X if "4" in parts else 0):
        if l % 3 != 1 or l < 7:
            continue
        for pi0 in E.split_prime(l):
            pi = next(E.mul(u, pi0) for u in E.UNITS if two_primary(E.mul(u, pi0)))
            A = E.add(pi, rat(18))
            unit, fac = E.factor(A)
            ok = any(in_class(E.mul(u, d)) for d in E.divisors(fac) for u in E.UNITS)
            tot += 1
            fire += ok
            if not ok and l <= 2300:
                fails.append(l)
    print(f"(4) plain shot pi+18 fires for {fire}/{tot} 2-primary split primes N ≤ {X};"
          f" norms ≤ 2300 where it fails: {sorted(set(fails))}")


if __name__ == "__main__":
    main()
