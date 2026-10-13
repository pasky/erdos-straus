"""R196: numerical check of the GRH density formula of FROBENIUS_FIRING Thm 4.4 (from scratch).
Counts primes r < X, r = a (mod M) for a in D, such that the index [F_r^* : <s>] has no odd prime factor,
and compares the proportion among all primes with delta = |D|/phi(M) * prod_{l odd, l nmid M} (1 - 1/(l(l-1))).
usage: review_frob_density.py X
"""
import sys, math

X = int(sys.argv[1])
spf = list(range(X + 1))
for i in range(2, int(X ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, X + 1, i):
            if spf[j] == j:
                spf[j] = i
primes = [p for p in range(2, X + 1) if spf[p] == p]
pi_X = len(primes)


def pfac(m):
    out = set()
    while m > 1:
        out.add(spf[m]); m //= spf[m]
    return out


def jac(a, n):
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def phi(m):
    r = m
    for p in pfac(m):
        r = r // p * (p - 1)
    return r


def run(n, s, variant):
    M = 4 * math.prod(pfac(n)) * s
    D = []
    for a in range(M):
        if math.gcd(a, M) != 1 or a % 4 != 3:
            continue
        if any(a % l == 1 for l in pfac(n)):
            continue
        if jac(a, n) != -1:
            continue
        if variant == 'y' and a % s != s - 1:
            continue
        if variant == 's' and a % s in (0, 1):
            continue
        D.append(a)
    Dset = set(D)
    prod = 1.0
    for l in primes[1:]:
        if M % l:
            prod *= 1 - 1 / (l * (l - 1))
    delta = len(D) / phi(M) * prod
    cnt = 0; cnt_class = 0; bad = 0
    for r in primes:
        if r % M not in Dset:
            continue
        cnt_class += 1
        ok = True
        for l in pfac(r - 1):
            if l == 2:
                continue
            if pow(s, (r - 1) // l, r) == 1:
                ok = False; break
        if ok:
            cnt += 1
            # consequence used: -n/4 is in <s^2> mod r
            t = (-n * pow(4, -1, r)) % r
            g = s * s % r; x = 1; hit = False
            for _ in range((r - 1) // 2 + 1):
                if x == t:
                    hit = True; break
                x = x * g % r
            if not hit:
                bad += 1
    print(f"n={n} s={s} variant={variant} M={M} |D|={len(D)} phi(M)={phi(M)}: predicted delta={delta:.5f}, "
          f"observed {cnt}/{pi_X}={cnt/pi_X:.5f} (class share {cnt_class/pi_X:.5f}); r with -n/4 not in <s^2>: {bad}")


for (n, s) in [(13, 3), (13, 5), (85, 3), (17, 7)]:
    for v in ('y', 's'):
        run(n, s, v)
