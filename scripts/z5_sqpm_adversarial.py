"""z5_sqpm_adversarial.py — adversarial test of prime-modulus SQ_± (CAP_GROWING §3): n ≡ 1 (mod 8·∏_{3≤q≤Qmax} q)
(n a QR modulo every small prime, so no small prime l fires since (n/l) = −1 is necessary). For the first `count`
non-squares in the progression, count prime-modulus words with |u| ≤ U (factor n+u, test l | n+u, u | l±1,
Jacobi(−u, l) = −1) and report the least |u| and the ticket count.
usage: z5_sqpm_adversarial.py Qmax count U"""
import sys, math
from sympy import factorint, primerange, legendre_symbol
Qmax, count, U = map(int, sys.argv[1:4])
M = 8 * math.prod(primerange(3, Qmax + 1))
res = []
k = 1
while len(res) < count:
    n = 1 + k * M; k += 1
    if math.isqrt(n) ** 2 == n: continue
    tickets = 0; least = None
    for au in range(1, U + 1):
        for u in (au, -au):
            for l in factorint(abs(n + u)):
                if l == 2: continue
                if ((l + 1) % u == 0 or (l - 1) % u == 0) and legendre_symbol((-u) % l, l) == -1:
                    tickets += 1
                    if least is None: least = au
    res.append((n, least, tickets))
for r in res: print(*r)
print("Qmax", Qmax, "M", M, "min tickets", min(r[2] for r in res), "max least|u|", max((r[1] or 10**9) for r in res))
