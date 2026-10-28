"""z49_i3fable_zeros_table.py — the 112 zeros of I3 (census to 1e9) with their local data:
factorisation, squarefree part k, S_div(n), first-order genus factor S_gen, exact main term M0(n), the first-order
expectation S_div*S_gen*M0, and the local expectation E_loc(n) (n's residues mod primes <= B exact, k*square
Haar model beyond B; see I3_DEEP_FABLE §3).  Usage: uv run python scripts/z49_i3fable_zeros_table.py [B=50]
"""
import sys
from math import isqrt
from sympy import factorint, jacobi_symbol

def main():
    B = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    zeros = [int(l.split()[1]) for l in open("data/z48_ltfable/big_1e9.txt") if l.startswith("I30")]
    NMAX = max(z for z in zeros if z < 10**6) // 3 + 10
    spf = list(range(NMAX + 1))
    for i in range(2, isqrt(NMAX) + 1):
        if spf[i] == i:
            for j in range(i * i, NMAX + 1, i):
                if spf[j] == j: spf[j] = i
    def fac(x):
        f = {}
        while x > 1:
            p = spf[x]; e = 0
            while x % p == 0: x //= p; e += 1
            f[p] = e
        return f
    Z = 1.5198177
    print("# n, factorisation, k, S_div, S_gen(1st order), M0, S_div*S_gen*M0, E_loc(B=%d)" % B)
    for n in zeros:
        fn = factorint(n); k = 1
        for p, e in fn.items():
            if e % 2: k *= p
        Sdiv = Z
        for p in fn: Sdiv *= (p * p - p + 1) / (p * p + 1)
        Sgen = 0.5 if k == 1 else (2 / 3 if k == 2 else 1.0)
        kinv = {}
        def pmodel(A, u):
            p = 1.0
            for l, e in (fac(A) if A <= NMAX else factorint(A)).items():
                q = l ** e
                if l <= B: p *= 1.0 if (n + u) % q == 0 else 0.0
                else:
                    if n % l == 0: return 0.0
                    if l not in kinv: kinv[l] = pow(k, -1, l)
                    p *= (2.0 / q) if jacobi_symbol((-u * kinv[l]) % l, l) == 1 else 0.0
                if p == 0: return 0.0
            return p
        M0 = 0.0; E = 0.0; t = 3
        if n < 10**6:
            while 3 * (3 * t - 1) <= n + 3:
                for u in range(3, (n + 3) // (3 * t - 1) + 1):
                    A = t * u - 1; M0 += 1.0 / A; E += pmodel(A, u)
                t += 1
            Es = f"{E:.2f}"
        else:
            M0 = 69.443; Es = "14.05 (anatomy run)"
        print(f"{n:8d} {str(dict(fn)):28s} k={k:<7d} S_div={Sdiv:.3f} S_gen={Sgen:.2f} M0={M0:7.2f} 1st-order={Sdiv * Sgen * M0:6.2f} E_loc={Es}")

if __name__ == "__main__":
    main()
