"""R109 from-scratch checks for POINTWISE_TYPEI7.md (does not import any author script).

Certificate definition used (TYPEI2 §0, §3, (2.2)): (c,k,F) positive integers, (F,4ck)=1,
sf(c) not in {1,2,3,6}, v_7(c) odd; it is a certificate at x̂_w iff
  F | 1+4ck^2,  F ≡ -1 mod (part of ck prime to 14),  F ≡ 1 mod 7^{v_7(ck)},  F ≡ -w mod 2^{v_2(4ck)}.
(No factorisation needed: the odd-q conditions combine by CRT.)
"""
import sys, math, random
from sympy import n_order, discrete_log, factorint, sqrt_mod


def v(p, x):
    x = abs(x); e = 0
    while x and x % p == 0:
        x //= p; e += 1
    return e


def sqfree_part_has7(c):
    return v(7, c) % 2 == 1  # then sf(c) has 7, so sf(c) not in {1,2,3,6}


def cert_at(c, k, F, w):
    """Return True iff (c,k,F) is a certificate at x̂_w (w an int standing for a 2-adic number,
    used mod 2^{v_2(4ck)})."""
    ck = c * k
    if math.gcd(F, 4 * ck) != 1 or not sqfree_part_has7(c):
        return False
    if (1 + 4 * c * k * k) % F:
        return False
    m2 = 1 << v(2, 4 * ck)
    m7 = 7 ** v(7, ck)
    rest = ck // (m2 // 4) // m7
    assert rest * (m2 // 4) * m7 == ck and rest % 2 and rest % 7
    return (F + 1) % rest == 0 and (F - 1) % m7 == 0 and (F + w) % m2 == 0


def thm21(m):
    """Construction of Theorem 2.1 for given m; returns (c,k,F,L) at the least admissible L>=7, split gamma=floor(L/2)."""
    s = 1
    while (pow(7, s, 1 << m) + 9) % (1 << m):
        s += 2
    b = (s - 1) // 2
    i = 3 * 7 ** b
    while i < m:
        i += 3 * 7 ** b
    F = 7 ** s + 2 ** i
    cp = (F + 1) // 8
    o = n_order(2, F)
    L = (1 - i) % o
    while L < 7:
        L += o
    return s, b, i, F, cp, o, L


def check_cert_split(cp7, ko, F, L, w, alpha):
    gamma = (L - alpha) // 2
    assert alpha + 2 * gamma == L
    return cert_at(2 ** alpha * cp7, 2 ** gamma * ko, F, w)


def main():
    out = []
    # --- number facts
    out.append(("ord_71(2)", n_order(2, 71)))
    out.append(("2^70 mod 71^2", pow(2, 70, 71 ** 2)))
    out.append(("2^35 mod 71^2", pow(2, 35, 71 ** 2)))
    out.append(("ord_{71^2}(2)", n_order(2, 71 ** 2)))
    out.append(("2^29*7 mod 71", pow(2, 29, 71) * 7 % 71))
    out.append(("9^-1*5 mod 2^9, 2^10", (5 * pow(9, -1, 512)) % 512, (5 * pow(9, -1, 1024)) % 1024))
    for j in range(1, 5):
        out.append((f"ord_7^{j}(2)", n_order(2, 7 ** j), 3 * 7 ** (j - 1)))
    for r in out:
        print(*r)
    # --- Theorem 2.1, m = 4, 5
    for m in (4, 5):
        s, b, i, F, cp, o, L = thm21(m)
        w = -F
        ok = [check_cert_split(7 * cp, 7 ** b, F, L, w, al) for al in (L % 2, L % 2 + 2)]
        # also at a second level L + o
        ok2 = check_cert_split(7 * cp, 7 ** b, F, L + o, w, (L + o) % 2)
        # not at x̂_9 at minimal split?
        at9 = check_cert_split(7 * cp, 7 ** b, F, L, 9, L % 2)
        print(f"Thm2.1 m={m}: s={s} b={b} i={i} F={F} c'={cp} ordF(2)={o} L={L} v2(F+9)={v(2, F + 9)} "
              f"cert@-F splits={ok} L+ord={ok2} at x9={at9}")
    # --- Thm 2.1 for m=6 (s=7?) just construct F and check the non-L conditions + v2
    for m in (6, 7, 8):
        s = 1
        while (pow(7, s, 1 << m) + 9) % (1 << m):
            s += 2
        b = (s - 1) // 2
        i = 3 * 7 ** b
        F = 7 ** s + 2 ** i
        print(f"Thm2.1 m={m}: s={s}, i={i}, log2 F~{F.bit_length()}, v2(F+9)={v(2, F + 9)}, "
              f"F%7^(b+1)={F % 7 ** (b + 1)}, F%16={F % 16}")
    # --- Remark 2.1(b) on (42,32,71): alpha=1,gamma=5, L=11
    for L in (11, 46, 81, 116):
        al = L % 2 if L % 2 else 1
        print("(c_o,k_o,F)=(21,1,71) L=", L, check_cert_split(21, 1, 71, L, -71, L % 2),
              "e=", (1 + 2 ** (L + 2) * 21) // 71, "v2(e+9)=", v(2, (1 + 2 ** (L + 2) * 21) // 71 + 9),
              "v2(9F+1)=", v(2, 9 * 71 + 1))
    # --- Thm 2.4 / Comp 2.5 rows nu = 1,3,7 with stated L
    for nu, L in ((1, 30), (3, 109685), (7, 419119864270)):
        F = 71 ** nu
        cp = (F + 1) // 8
        # modular check (2^gamma too large to build): F | 1+2^{L+2}*7c', plus the L-independent conditions
        ok = ((1 + pow(2, L + 2, F) * 7 * cp) % F == 0 and math.gcd(F, 14 * cp) == 1
              and (F + 1) % cp == 0 and (F - 1) % 7 == 0 and F % 16 == 7 and cp % 7 and cp % 2)
        # least L>=7: L-1 = log_2(-7^-1) mod ord
        o = 35 * 71 ** (nu - 1)
        tgt = (-pow(7, -1, F)) % F
        lg = discrete_log(F, tgt, 2)
        Lmin = (lg + 1) % o
        while Lmin < 7:
            Lmin += o
        print(f"Thm2.4 nu={nu}: v2(F+9)={v(2, F + 9)} stated L={L} cert={ok} least L={Lmin} n_order={n_order(2, F) == o}")
    # least odd nu with 71^nu = -9 mod 2^m
    for m in range(4, 15):
        nu = 1
        while (pow(71, nu, 1 << m) + 9) % (1 << m):
            nu += 2
        print(f"m={m}: least odd nu={nu}, v2(71^nu+9)={v(2, 71 ** nu + 9)}, bits={(71 ** nu).bit_length()}")


if __name__ == "__main__":
    main()
