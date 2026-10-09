"""EXCEPTIONAL_TYPEI_LOGLOG §3 numerics (EVIDENCE): per-d counts of level-d Heegner lifts in boxes.
For fixed d count  N_d = sum_{a} w(a/A) sum_{f | 4 d a^2 + 1} w(f/F)  (smooth bump weights w on [1,2])
and compare with the local-density main term  M_d = sum_f w(f/F) rho_d(f)/f * sum_a w(a/A),
rho_d(f) = #{x mod f : 4 d x^2 + 1 = 0 mod f}.  Reports err = N_d - M_d against sqrt(A d) (the
heuristic Cauchy-Schwarz bound of §3) and against A (main term size).
Usage: ttl_perd.py A F d1 d2 ...   (needs F up to a few 10^6; pure python, slowish)."""
import sys, math

def bump(t):
    if t <= 1.0 or t >= 2.0:
        return 0.0
    u = (t - 1.0) * (2.0 - t)
    return math.exp(-1.0 / (4.0 * u)) / 0.0183156  # ~1 at t=1.5 (exp(-1/(4*0.25)) = e^-1? normalised loosely)

def spf_sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def sqrt_mod_p(a, p):
    a %= p
    if p == 2:
        return [a % 2]
    if a == 0:
        return [0]
    if pow(a, (p - 1) // 2, p) != 1:
        return []
    # Tonelli-Shanks
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return sorted({r, p - r})

def roots_mod_pk(d, p, k):
    """roots x mod p^k of 4 d x^2 + 1 = 0 (brute lift)."""
    if p == 2 or d % p == 0:
        return []  # 4dx^2+1 odd; and = 1 mod p if p | d
    inv = pow(4 * d, -1, p)
    rs = sqrt_mod_p(-inv, p)
    pk = p
    for _ in range(1, k):
        new = []
        for r in rs:
            for t in range(p):
                x = r + pk * t
                if (4 * d * x * x + 1) % (pk * p) == 0:
                    new.append(x)
        rs, pk = new, pk * p
    return rs

def run(A, F, d, spf):
    wa = [bump(a / A) for a in range(0, 2 * A + 1)]
    SA = sum(wa)
    N = 0.0; M = 0.0
    cache = {}
    for f in range(F + 1, 2 * F):
        wf = bump(f / F)
        if wf == 0.0:
            continue
        # factor f
        n, fac = f, []
        while n > 1:
            p = spf[n]; k = 0
            while n % p == 0:
                n //= p; k += 1
            fac.append((p, k))
        # CRT roots
        roots, mod = [0], 1
        ok = True
        for p, k in fac:
            key = (p, k)
            if key not in cache:
                cache[key] = roots_mod_pk(d, p, k)
            rp = cache[key]
            if not rp:
                ok = False; break
            pk = p ** k
            inv = pow(mod, -1, pk)
            roots = [r + mod * (((s - r) * inv) % pk) for r in roots for s in rp]
            mod *= pk
        if not ok:
            continue
        M += wf * len(roots) * SA / f
        for x in roots:
            a = x if x > 0 else f
            # all lifts a = x + f t in (A, 2A)
            t0 = (A - x) // f + 1
            a = x + f * max(t0, 0)
            while a < 2 * A:
                if a > A:
                    N += wf * wa[a]
                a += f
    return N, M

if __name__ == "__main__":
    A, F = int(sys.argv[1]), int(sys.argv[2])
    ds = [int(x) for x in sys.argv[3:]]
    spf = spf_sieve(2 * F + 2)
    print(f"A={A} F={F}")
    for d in ds:
        N, M = run(A, F, d, spf)
        err = N - M
        print(f"d={d:7d} N_d={N:12.2f} M_d={M:12.2f} err={err:10.2f} err/sqrt(Ad)={err/math.sqrt(A*d):8.3f} err/M={err/M:8.4f}", flush=True)
