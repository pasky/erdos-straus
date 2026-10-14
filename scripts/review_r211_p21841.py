"""R211: exhaustive word list at a given N (default 21841): all (c,m,s) >= 1 with cms - c - s = N.
Brute force over c, m (no divisor shortcuts), s solved exactly.  Reports certificates (some vertex == 0 mod 4),
the opposite vertex o, interior flag, and chi = (h'/N) via a from-scratch Jacobi symbol."""
import sys

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

N = int(sys.argv[1]) if len(sys.argv) > 1 else 21841
words = []
for c in range(1, N + 2):
    for m in range(1, N + 3):
        g = c * m - 1
        if g <= 0: continue
        if g - c > N: break
        if (N + c) % g == 0:
            s = (N + c) // g
            if s >= 1: words.append((c, m, s))
nchi = 0; certs = []
for (c, m, s) in words:
    assert c * m * s - c - s == N
    h, hp = c * m - 1, m * s - 1
    q = [hp, c, m, s, h]
    ev = [i for i in range(5) if q[i] % 2 == 0]
    i0 = ev[0] if ev[1] - ev[0] == 1 else ev[1]
    o = q[(i0 + 3) % 5]
    cert = any(x % 4 == 0 for x in q)
    chi = jacobi(hp, N)
    assert cert == (chi == -1)
    if chi == -1: nchi += 1
    if cert: certs.append((c, m, s, o, min(c, m, s) >= 2))
print(f"N={N}: formal words {len(words)}, chi=-1: {nchi}, interior words {sum(1 for w in words if min(w) >= 2)}")
print("certificates (c,m,s,o,interior):")
for t in sorted(certs, key=lambda t: t[3]): print("  ", t)
