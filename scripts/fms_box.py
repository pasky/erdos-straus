"""fms_box.py R — sizes of the ES coverage boxes A_r = -Box((r+1)/4) mod r (FIXED_MODULUS_SHOTS Thm 3.1),
and for S = {3,5,7,11} the ES^(S) coset -4<S>^2 mod r, for primes r = 3 mod 4, r < R.
Also brute-checks Thm 3.1 for r < 3000: p mod r in A_r  <=>  some cube point with h = r (search over c,d)."""
import sys
from sympy import primerange, divisors


def box(r):
    k = (r + 1) // 4
    out = set()
    for n in divisors(k):
        for c in divisors(n):
            j = n // c
            out.add((-c * pow(j, -1, r)) % r)
    return out


def coset(r, S=(3, 5, 7, 11)):
    G = {1}
    frontier = [1]
    while frontier:
        nf = []
        for g in frontier:
            for q in S:
                h = g * q * q % r
                if h not in G:
                    G.add(h); nf.append(h)
        frontier = nf
    return {(-4 * g) % r for g in G}


def main():
    R = int(sys.argv[1])
    mx = (0, 0); tot = n = 0; ratios = []
    for r in primerange(19, R):
        if r % 4 != 3:
            continue
        A = box(r)
        n += 1; tot += len(A)
        mx = max(mx, (len(A), r))
        if r < 3000:
            # brute: p mod r certified by h=r  <=>  exists c,d with 4cd | r+1 and r | p+4c^2 d
            k = (r + 1) // 4
            Bd = set()
            for c in divisors(k):
                for d in divisors(k // c):
                    Bd.add((-4 * c * c * d) % r)
            assert Bd == A, r
        if r < 200000 and n % 50 == 0:
            ratios.append(len(coset(r)) / len(A))
    print(f"primes r=3 mod 4 in [19,{R}): {n}; mean |A_r| {tot/n:.1f}; max |A_r| = {mx[0]} at r = {mx[1]}")
    ratios.sort()
    print(f"sampled |ES^(S) coset| / |A_r| (S=3,5,7,11): min {ratios[0]:.0f}, median {ratios[len(ratios)//2]:.0f}")


if __name__ == "__main__":
    main()
