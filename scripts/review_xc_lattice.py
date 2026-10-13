"""R200 from-scratch check of EXPONENT_CAP Prop 3.1 and of the geometry-of-numbers step of Thm 3.2 for k = 2,
S = {3, 5}: for primes r ≡ -1 (mod 60), r < RMAX:
  * least L with {9^a 25^b : 0 <= a, b <= L} = (F_r^*)^2  (brute force over discrete logs),
  * ℓ^∞ successive minima λ1 <= λ2 of Λ_r = {(a,b) : 9^a 25^b ≡ 1 (mod r)} (exhaustive),
  * checks: λ1·λ2 <= det = (r-1)/2 (Minkowski II for the cube), L <= 2(λ1 + λ2) (Thm 3.2's representative bound),
    (L+1)^2 >= (r-1)/2 (Prop 3.1(a) at the box level), and the B_r(e) count vs Prop 3.1(a)/(b).
Usage: review_xc_lattice.py RMAX [cap]   (cap: stop at L = 4√r+10, as the author's §5.2 statistic)
"""
import sys
from math import gcd, isqrt
from statistics import median


def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def dlogs(r):
    # generator h of the squares subgroup (order N=(r-1)/2, odd since r ≡ 3 mod 4): h = g^2 for a primitive root g
    N = (r - 1) // 2
    fac = [q for q in range(2, r) if (r - 1) % q == 0 and is_prime(q)]
    g = next(g for g in range(2, r) if all(pow(g, (r - 1) // q, r) != 1 for q in fac))
    h = g * g % r
    lg = {}
    x = 1
    for i in range(N):
        lg[x] = i; x = x * h % r
    return N, lg


def least_L(N, al, be, cap=None):
    seen = bytearray(N); cnt = 0; L = -1
    while cnt < N:
        L += 1
        if L > (N if cap is None else cap): return None
        for a in range(L + 1):
            for t in ((a * al + L * be) % N, (L * al + a * be) % N):
                if not seen[t]: seen[t] = 1; cnt += 1
    return L


def minima(N, al, be):
    T = N  # λ2 <= N always (N·e_i ∈ Λ)
    best = []
    # all lattice vectors (a,b) with |a| <= T: b ≡ -a·al/be mod N, need gcd handling
    d = gcd(be, N); M = N // d
    inv = pow(be // d, -1, M) if M > 1 else 0
    vecs = []
    for a in range(0, T + 1):
        if (a * al) % d: continue
        b0 = (-(a * al) // d * inv) % M if M > 1 else 0
        for b in (b0, b0 - M):
            if a == 0 and b == 0:
                b = M if M > 0 else N
            vecs.append((max(abs(a), abs(b)), a, b))
        if a == 0:
            vecs.append((M, 0, M))
    vecs.sort()
    l1, a1, b1 = vecs[0]
    for (n2, a2, b2) in vecs[1:]:
        if a1 * b2 - a2 * b1 != 0:
            return l1, n2
    return l1, None


def main(RMAX):
    rows = []
    viol = 0; nprime = nfull = nexc = 0
    for r in range(59, RMAX, 60):
        if not is_prime(r): continue
        nprime += 1
        N, lg = dlogs(r)
        if 9 % r == 0: continue
        al, be = lg[9 % r], lg[25 % r]
        if gcd(gcd(al, be), N) != 1:
            continue  # <9,25> != squares
        nfull += 1
        L = least_L(N, al, be, cap=int(4 * r ** 0.5 + 10) if CAP else None)
        if L is None and CAP:
            nexc += 1; continue
        l1, l2 = minima(N, al, be)
        ok = (l1 * l2 <= N) and (L is not None and L <= 2 * (l1 + l2)) and (L is not None and (L + 1) ** 2 >= N)
        # Prop 3.1(a)/(b): |B_r(e)| for e = 0..3 with κ = v_3, v_5 of (r+1)/4
        K = (r + 1) // 4
        k3 = k5 = 0
        while K % 3 == 0: K //= 3; k3 += 1
        K = (r + 1) // 4
        while K % 5 == 0: K //= 5; k5 += 1
        for e in range(4):
            B = {(a * al + b * be) % N for a in range(k3 + e + 1) for b in range(k5 + e + 1)}
            if len(B) > (k3 + e + 1) * (k5 + e + 1) or (k3 + e + 1) * (k5 + e + 1) > k3 * k5 * (e + 2) ** 2:
                ok = False
        if not ok: viol += 1; print("VIOL", r, L, l1, l2)
        rows.append((r, L, l1, l2))
    print(f"r ≡ -1 (60) primes: {nprime}, <9,25> full: {nfull}, L > 4 sqrt r + 10 (capped runs): {nexc}")
    rat = [L / r ** 0.5 for r, L, _, _ in rows]
    print(f"primes r≡-1 (60) < {RMAX} with <9,25> = squares: {len(rows)}; violations: {viol}")
    print(f"  L/sqrt r: min {min(rat):.3f} median {median(rat):.3f} max {max(rat):.3f}; "
          f"#L > 4 sqrt r + 10: {sum(1 for r, L, _, _ in rows if L > 4 * r ** 0.5 + 10)}")
    print(f"  max L/(λ1+λ2) = {max(L / (a + b) for _, L, a, b in rows):.3f};  max λ1λ2/N = "
          f"{max(a * b / ((r - 1) / 2) for r, _, a, b in rows):.3f}")


if __name__ == "__main__":
    CAP = len(sys.argv) > 2 and sys.argv[2] == "cap"
    main(int(sys.argv[1]))
