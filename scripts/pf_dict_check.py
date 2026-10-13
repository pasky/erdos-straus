"""O165: brute-force checks of the dictionaries in PARITY_FIXED_P.md §1.

(D1) bijection {(a,d,f): f | n+4a^2 d, f = -1 mod 4ad}  <->  {(h,k,d): (4dhk-1) | hn+k}
(D2) Type I p-free form: #{(c,d,f): f | n^2+4c^2 d, f = -n mod 4cd}
       = #{(d,k,f): f | 4dk^2+1, f = -n mod 4dk}   (bijection c = (f+n)/(4dk))
(D3) spin lemma: prime l | n+4a^2 d, l not | 2nad, n = 1 mod 4 prime  =>  (-4d/l) = (l/n).
Run: PYTHONPATH=scripts uv run python scripts/pf_dict_check.py
"""
from sympy import factorint, jacobi_symbol, isprime


def divisors(N):
    ds = [1]
    for q, e in factorint(N).items():
        ds = [x * q**i for x in ds for i in range(e + 1)]
    return ds


def II_adf(n):
    out = set()
    # f = 4adh-1 <= n+4a^2 d  => need 4ad-1 <= n+4a^2 d always; bound a,d via g>=1: 4adk>n, k>=1
    # g = (n+4a^2d)/f >= 1 and f>=4ad-1, also g = 4adk-n >= 1 -> n+4a^2d >= (4ad-1)*1.
    # finiteness: a(4dhk-1)=hn+k gives a <= hn+k... use (h,k,d) side bound instead; here brute over a,d
    # with f|N, f=-1 mod 4ad and g=-n mod 4ad, g>0: g >= 4ad - n, so if 4ad > n then g>=4ad-n and f>=4ad-1,
    # fg = n+4a^2d >= (4ad-1)(4ad-n): bounded a,d.
    for a in range(1, 4 * n + 2):
        if (4 * a - 1) * max(1, 4 * a - n) > n + 4 * a * a:
            break
        for d in range(1, 4 * n + 2):
            q = 4 * a * d
            if (q - 1) * max(1, q - n) > n + 4 * a * a * d:
                break
            N = n + 4 * a * a * d
            for f in divisors(N):
                if (f + 1) % q == 0:
                    out.add((a, d, f))
    return out


def II_hkd(n):
    out = set()
    for h in range(1, n + 2):
        if 4 * h - 1 > h * n + 4 * n:  # d=k=1 minimal modulus already too big
            break
        for k in range(1, 4 * n + 2):
            if 4 * h * k - 1 > h * n + k:
                break
            for d in range(1, 4 * n + 2):
                m = 4 * d * h * k - 1
                if m > h * n + k:
                    break
                if (h * n + k) % m == 0:
                    out.add((h, k, d))
    return out


def map_hkd_to_adf(n, t):
    h, k, d = t
    a = (h * n + k) // (4 * d * h * k - 1)
    return (a, d, 4 * a * d * h - 1)


def I_cdf(n):
    out = set()
    for c in range(1, n * n):
        if 4 * c - n > n * n + 4 * c * c and False:
            break
        if 4 * c > n * n + 4 * c * c:  # never
            break
        for d in range(1, n * n):
            q = 4 * c * d
            N = n * n + 4 * c * c * d
            # f = -n mod q, f>=q-n; cofactor g = N/f, g = (4dk^2+1)-ish; bound: f <= N, and f >= q-n
            # Type I solutions have f = 4cdk - n | 4dk^2+1 so q-n <= f <= 4dk^2+1 with k>=1 ...
            if q - n > N:
                break
            if c > 3 * n and d > 0:  # crude cutoff, justified by the k-side bound below
                pass
            for f in divisors(N):
                if (f + n) % q == 0:
                    out.add((c, d, f))
        if c > 2 * n * n:
            break
    return out


def I_dkf(n):
    out = set()
    for d in range(1, 2 * n * n):
        if 4 * d + 1 > 10**12:
            break
        found_any_k = False
        for k in range(1, 2 * n * n):
            M = 4 * d * k * k + 1
            q = 4 * d * k
            # f = q*c - n with c>=1, and f | M with f < = M. Since (4dk^2+1)/(qc-n) must be integer:
            # loop over c with qc - n <= M
            cmax = (M + n) // q
            if cmax < 1:
                break
            found_any_k = True
            for c in range(1, cmax + 1):
                f = q * c - n
                if f >= 1 and M % f == 0:
                    out.add((d, k, f))
            if k > 3 * n:  # (h,k) bound: f | pk+j style forces k <= ~ n; generous
                break
        if d > 3 * n:
            break
    return out


if __name__ == "__main__":
    bad = 0
    for n in range(3, 120):
        A = II_adf(n)
        B = {map_hkd_to_adf(n, t) for t in II_hkd(n)}
        if A != B or len(B) != len(II_hkd(n)):
            bad += 1
            print("D1 mismatch", n, len(A), len(B), sorted(A ^ B)[:5])
    print("D1 checked n=3..119, mismatches:", bad)
    bad = 0
    for n in range(3, 40):
        A = I_dkf(n)
        # map (d,k,f) -> (c,d,f), c=(f+n)/(4dk)
        Am = {((f + n) // (4 * d * k), d, f) for (d, k, f) in A}
        # direct check of each mapped triple
        for (c, d, f) in Am:
            if (n * n + 4 * c * c * d) % f or (f + n) % (4 * c * d):
                bad += 1
                print("D2 bad", n, c, d, f)
        if len(Am) != len(A):
            bad += 1
            print("D2 non-injective", n)
    print("D2 (p-free -> Type I) direction checked n=3..39, bad:", bad)
    bad = cnt = 0
    for n in range(5, 3000, 4):
        if not isprime(n):
            continue
        for a in range(1, 8):
            for d in range(1, 8):
                N = n + 4 * a * a * d
                for l in factorint(N):
                    if (2 * n * a * d) % l == 0:
                        continue
                    cnt += 1
                    if jacobi_symbol(-4 * d % l, l) != jacobi_symbol(l % n, n):
                        bad += 1
    print("D3 spin lemma instances", cnt, "violations", bad)
