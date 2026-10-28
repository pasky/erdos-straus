"""z49_i3fable_anatomy.py — level-by-level and endpoint-by-endpoint anatomy of a zero of I3.
For each level t <= T: factor N_t = t n + 1, list its divisors A ≡ -1 (mod t), and say why none is interior
(interior needs 3t-1 <= A <= N_t/(3t-1)).  Reciprocity-empty levels (Lemma 4.3 at squares) are marked.
For each endpoint u <= U: factor n+u, list divisors A ≡ -1 (mod u) and the same size test (A in [3u-1, (n+u)/3]).
Also prints the local expectation E_loc(n) = sum_{(t,u)} P_model(A | n+u) with the exact residues of n modulo
primes <= B and the k*square local model beyond B (k = squarefree part of n), and S_div(n), M0(n).
Usage: uv run python scripts/z49_i3fable_anatomy.py n [T=40] [U=24] [B=50]
"""
import sys
from sympy import factorint, divisors, jacobi_symbol, primerange

def main():
    n = int(sys.argv[1]); T = int(sys.argv[2]) if len(sys.argv) > 2 else 40; U = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    B = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    fn = factorint(n); k = 1
    for p, e in fn.items():
        if e % 2: k *= p
    print(f"n = {n} = {fn}; squarefree part k = {k}")
    print(f"\n## levels t <= {T}: N_t = t n + 1, divisors A ≡ -1 (mod t) and the interior window [3t-1, N_t/(3t-1)]")
    for t in range(3, T + 1):
        Nt = t * n + 1; f = factorint(Nt); ds = [d for d in divisors(Nt) if d % t == t - 1]
        lo, hi = 3 * t - 1, Nt // (3 * t - 1)
        inside = [d for d in ds if lo <= d <= hi]
        tag = ""
        if k == 1 and (t % 4 == 0 or t % 8 == 7): tag = " [reciprocity-empty level]"
        if k == 1 and t % 8 == 3 and n % 2 == 0: tag = " [reciprocity-empty level (even m)]"
        # subgroup reason: all prime factors in an index-2 subgroup missing -1?
        print(f"t={t:3d} N_t={Nt} = {dict(f)}; A≡-1 (t): {ds[:8]}{'...' if len(ds) > 8 else ''}; interior: {inside}{tag}")
    print(f"\n## endpoints u <= {U}: n+u, divisors A ≡ -1 (mod u), interior window [3u-1, (n+u)/3]")
    for u in range(3, U + 1):
        Nu = n + u; f = factorint(Nu); ds = [d for d in divisors(Nu) if d % u == u - 1]
        inside = [d for d in ds if 3 * u - 1 <= d <= Nu // 3]
        print(f"u={u:3d} n+u={Nu} = {dict(f)}; A≡-1 (u): {ds[:10]}{'...' if len(ds) > 10 else ''}; interior: {inside}")
    # local expectation
    small = list(primerange(2, B + 1))
    def pmodel(A, u):
        p = 1.0; fa = factorint(A)
        for l, e in fa.items():
            q = l ** e
            if l <= B:
                p *= 1.0 if (n + u) % q == 0 else 0.0
            else:
                if n % l == 0: return 0.0
                # n = k m^2 with l ∤ n: n ≡ -u (mod l^e) has model probability 2/l^e if -u k^{-1} is a QR mod l, else 0
                m_inv_k = pow(k, -1, l)
                p *= (2.0 / q) if jacobi_symbol((-u * m_inv_k) % l, l) == 1 else 0.0
            if p == 0: return 0.0
        return p
    E = 0.0; M0 = 0.0; t = 3
    while 3 * (3 * t - 1) <= n + 3:
        Umax = (n + 3) // (3 * t - 1)
        for u in range(3, Umax + 1):
            A = t * u - 1; M0 += 1.0 / A; E += pmodel(A, u)
        t += 1
    Z = 1.5198177; Sdiv = Z
    for l in fn: Sdiv *= (l * l - l + 1) / (l * l + 1)
    print(f"\nM0(n) = {M0:.3f}; S_div(n) = {Sdiv:.4f}; S_div*M0 = {Sdiv * M0:.2f}; first-order genus factor = {0.5 if k == 1 else (2/3 if k == 2 else 1)}; "
          f"E_loc(n) [residues mod primes <= {B} exact, k-square model beyond] = {E:.3f}; actual I3(n) = 0")

if __name__ == "__main__":
    main()
