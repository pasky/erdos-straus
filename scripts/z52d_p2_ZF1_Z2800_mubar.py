"""Z2800 / Z2844: Neumann-Siebenmann mu-bar of lens spaces L(n,A) via linear plumbing (Neumann 1980 Thm 2.1),
signature / Arf of the 2-bridge knot K(n,A), compared with the ES sign (A/n) and the DK five-slice certificate.

Conventions. n/A = [[b_1..b_r]] (HJ, b_i>=2). L(n,A) := boundary of the NEGATIVE linear plumbing with Euler numbers
-b_i (Gompf-Stipsicz / DEDEKIND_ES 5.2). Neumann Thm 2.1: for det odd there is a unique Wu set S (sum_{i in S} a_ij == a_jj
mod 2 for all j) and mubar = sign(A(Gamma)) - sum_{j in S} e_j  = -r + sum_{j in S} b_j  (an oriented-diffeo invariant).
Knot: Murasugi signature sigma(K(n,q)) = sum_{i=1}^{n-1} (-1)^floor(i q / n), q odd; Arf via Conway c2 = Delta''(1)/2 with
Hartley's Alexander polynomial Delta(t) = sum_{i=0}^{n-1} (-1)^i t^{sum_{k<=i} eps_k}, eps_k = (-1)^floor(kq/n), q odd.
Usage: python z52d_p2_ZF1_Z2800_mubar.py N_all N_words
"""
import sys, json, math
from collections import Counter, defaultdict
from sympy import jacobi_symbol, isprime


def hj(n, A):
    b = []
    while A > 0:
        c = -(-n // A)
        b.append(c)
        n, A = A, c * A - n
    return b


def wu_set(b, neg=True):
    r = len(b)
    # tridiagonal a_jj = -b_j (neg) , a_{j,j+1} = 1 ; mod 2 the signs do not matter
    sols = []
    for m in range(1 << r):
        S = [(m >> i) & 1 for i in range(r)]
        ok = True
        for j in range(r):
            s = S[j] * b[j] + (S[j - 1] if j > 0 else 0) + (S[j + 1] if j < r - 1 else 0)
            if (s - b[j]) % 2:
                ok = False; break
        if ok:
            sols.append(S)
    return sols


def wu_set_fast(b):
    # solve tridiagonal system mod 2 by forward substitution on S_1 in {0,1}
    r = len(b)
    out = []
    for s0 in (0, 1):
        S = [s0]
        for j in range(r - 1):
            # equation j: S_{j-1} + b_j S_j + S_{j+1} == b_j  -> S_{j+1}
            prev = S[j - 1] if j > 0 else 0
            S.append((b[j] - prev - b[j] * S[j]) % 2)
        j = r - 1
        prev = S[j - 1] if j > 0 else 0
        if (prev + b[j] * S[j] - b[j]) % 2 == 0:
            out.append(S)
    return out


def mubar(n, A):
    b = hj(n, A)
    S = wu_set_fast(b)
    assert len(S) == 1, (n, A, b, S)
    S = S[0]
    adj = sum(S[i] * S[i + 1] for i in range(len(b) - 1))
    return -len(b) + sum(bi for bi, s in zip(b, S) if s), len(b), adj


def murasugi_sig(n, q):
    assert q % 2 == 1
    return sum(1 if (i * q // n) % 2 == 0 else -1 for i in range(1, n))


def arf_conway(n, q):
    # Hartley: exponents e_i = sum_{k<=i} eps_k, coefficient (-1)^i
    e = 0; coef = defaultdict(int); coef[0] += 1
    for i in range(1, n):
        e += 1 if (i * q // n) % 2 == 0 else -1
        coef[e] += (-1) ** i
    # normalise: Delta(1) = +-1, symmetric; c2 = Delta''(1)/2 after centring t^{-m}
    ks = [k for k in coef if coef[k]]
    lo, hi = min(ks), max(ks); mid = (lo + hi) / 2
    D1 = sum(coef.values())
    s = 1 if D1 > 0 else -1
    # second derivative of t^{k-mid} at 1: (k-mid)(k-mid-1); for symmetric poly first-derivative terms cancel
    c2 = s * sum(c * (k - mid) * (k - mid - 1) for k, c in coef.items()) / 2
    c2b = s * sum(c * (k - mid) ** 2 for k, c in coef.items()) / 2  # same for symmetric (sum c*(k-mid)=0)
    assert abs(c2 - c2b) < 1e-9 and abs(c2 - round(c2)) < 1e-9
    Dm1 = sum(c * (-1) ** (k - lo) for k, c in coef.items())
    return int(round(c2)) % 2, abs(Dm1)


def dk_cert(t, u, v):
    return (t * u - 1) % 4 == 0 or (t * v - 1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0


def main():
    Nall = int(sys.argv[1]); Nw = int(sys.argv[2])
    res = {}
    # (1) all lens spaces n odd < Nall: uniqueness of Wu set, no adjacency, invariance mubar(-Y) = -mubar(Y),
    #     knot-signature relation, Arf vs det mod 8, mubar mod 8/16 vs Jacobi
    bad_unique = bad_inv = 0; adj_cases = 0; rel = Counter(); arfrel = Counter(); signrel = defaultdict(Counter)
    m16 = defaultdict(Counter); total = 0
    for n in range(3, Nall, 2):
        for A in range(1, n):
            if math.gcd(A, n) != 1: continue
            total += 1
            mb, r, adj = mubar(n, A)
            adj_cases += adj > 0
            mb2, _, _ = mubar(n, n - A)
            if mb2 != -mb: bad_inv += 1
            # inverse A* gives same lens space (reversed chain)
            Ainv = pow(A, -1, n)
            if mubar(n, Ainv)[0] != mb: bad_unique += 1
            q = A if A % 2 else n - A
            sg = murasugi_sig(n, q) * (1 if A % 2 else -1)
            rel[mb - sg] += 1
            if n < 400:
                arf, det = arf_conway(n, q)
                assert det == n
                arfrel[(n % 8, arf)] += 1
            if n % 4 == 1:
                J = jacobi_symbol(A, n)
                signrel[(n % 8, J)][mb % 8] += 1
                m16[(n % 16, J)][mb % 16] += 1
    res['all_lens'] = dict(N=Nall, pairs=total, inverse_invariance_fail=bad_unique, orientation_fail=bad_inv,
                           wu_adjacent_cases=adj_cases, mubar_minus_knotsig=dict(rel),
                           arf_by_n_mod8=str(dict(arfrel)),
                           mubar_mod8_by_nmod8_J={str(k): dict(v) for k, v in signrel.items()},
                           mubar_mod16_by_nmod16_J={str(k): dict(v) for k, v in m16.items()})
    # (2) length-3 words, n = p prime = 1 mod 4 < Nw: mubar value vs certificate; integer mubar distribution
    cert_mb = Counter(); non_mb = Counter(); bad45 = 0; per_p = {}
    for t in range(2, Nw):
        for u in range(2, Nw):
            if t * u * 2 - u - 2 >= Nw: break
            for v in range(2, Nw):
                n = t * u * v - u - v
                if n >= Nw: break
                if n % 4 != 1 or not isprime(n): continue
                A = t * u - 1
                b = hj(n, A); assert b == [v, t, u]
                mb, r, adj = mubar(n, A)
                c = dk_cert(t, u, v)
                J = jacobi_symbol(A, n)
                if c != (J == -1): bad45 += 1
                (cert_mb if c else non_mb)[(n % 8, mb)] += 1
                d = per_p.setdefault(n, [0, 0, Counter()])
                d[0] += 1; d[1] += c; d[2][mb % 16] += 1
    res['words'] = dict(N=Nw, thm45_fail=bad45,
                        cert_mubar={str(k): v for k, v in sorted(cert_mb.items())},
                        noncert_mubar={str(k): v for k, v in sorted(non_mb.items())})
    # does mubar mod 16 (beyond mod 8) split certificates? per p: fraction of words in each mod-16 class
    print(json.dumps(res, indent=1)[:6000])
    json.dump(res, open(sys.argv[3], 'w'), indent=1)


if __name__ == '__main__':
    main()
