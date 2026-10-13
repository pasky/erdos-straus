"""O168 §3: Jacobi forcing on Type II prime slices.

For primes p ≡ 1 (mod 24) and primes e ≡ 3 (mod 4), N_e = (p+e)/4. Checks
 (a) (p/e) = -1  =>  N_e has a prime factor that is a non-residue mod e (forced; sanity);
 (b) group-level obstruction  -1 ∉ H_e(N_e) = <l mod e : l | N_e>  happens only if (p/e) = +1;
 (c) e-slice success rate  -1 ∈ Σ_e(N_e)  split by (p/e).
Usage: de_jacobi_slices.py PMAX EMAX
"""
import sys
from sympy import factorint, primerange, legendre_symbol


def divisors_from(fac):
    ds = [1]
    for l, k in fac.items():
        ds = [d * l**i for d in ds for i in range(k + 1)]
    return ds


def sigma_has_minus1(N, e, fac):
    ds = divisors_from(fac)
    S = set(ds)
    for a in ds:
        for b in ds:
            if a * b > N:
                continue
            if N % (a * b) == 0 and (a + b) % e == 0:
                return True
    return False


def group_has_minus1(fac, e):
    H = {1}
    gens = [l % e for l in fac]
    frontier = [1]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = x * g % e
            if y not in H:
                H.add(y)
                frontier.append(y)
    return (e - 1) in H


def main():
    PMAX, EMAX = int(sys.argv[1]), int(sys.argv[2])
    es = [e for e in primerange(3, EMAX) if e % 4 == 3]
    stats = {1: [0, 0, 0], -1: [0, 0, 0]}  # [slices, group ok, sigma ok]
    bad_a = 0
    for p in primerange(5, PMAX):
        if p % 24 != 1:
            continue
        for e in es:
            N = (p + e) // 4
            fac = factorint(N)
            s = legendre_symbol(p % e, e)
            if s == -1 and not any(legendre_symbol(l % e, e) == -1 for l in fac if l % e):
                bad_a += 1
            g = group_has_minus1(fac, e)
            sg = sigma_has_minus1(N, e, fac)
            st = stats[s]
            st[0] += 1
            st[1] += g
            st[2] += sg
            assert not (sg and not g)
    print("violations of (a):", bad_a)
    for s in (1, -1):
        n, g, sg = stats[s]
        print(f"(p/e)={s:+d}: slices={n} group-level ok={g/n:.4f} sigma ok={sg/n:.4f}")


if __name__ == "__main__":
    main()
