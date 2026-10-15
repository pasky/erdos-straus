"""O231 §5: classify primes p = 1 (8) by the psi-odd exponent profile of p+1 and report N-/U statistics.
Input: z7_types output lines (p N Nm U2 U ...) on stdin.  Profile: 'odd' = some psi-odd prime has odd exponent in p+1,
'even' = psi-odd primes exist, all exponents even (automatic family certificate rate < 1/2), 'clean'."""
import sys, numpy as np
rows = [list(map(int, l.split()[:5])) for l in sys.stdin]
H = max(r[0] for r in rows) + 2
spf = np.zeros(H + 1, dtype=np.int32)
for i in range(2, int(H ** 0.5) + 1):
    if spf[i] == 0:
        blk = spf[i * i::i]; blk[blk == 0] = i
spf[(spf == 0)] = np.arange(H + 1, dtype=np.int32)[spf == 0]
st = {}
for p, N, Nm, U2, U in rows:
    x = p + 1; f = {}
    while x > 1:
        r = int(spf[x]); f[r] = f.get(r, 0) + 1; x //= r
    nr = {r: e for r, e in f.items() if pow(r, (p - 1) // 2, p) == p - 1}
    prof = 'clean' if not nr else ('odd' if any(e % 2 for e in nr.values()) else 'even:' + '.'.join(f"{r}^{e}" for r, e in sorted(nr.items())))
    key = prof if prof in ('clean', 'odd') else ('even(3^2)' if nr == {3: 2} else 'even(other)')
    s = st.setdefault(key, [0, 9.0, None, 0])
    s[0] += 1; q = Nm / U
    if q < s[1]: s[1], s[2] = q, (p, Nm, U)
    s[3] += q < 0.5
for k, (c, mn, arg, fails) in st.items(): print(f"{k:12s} primes {c:7d}  min Nm/U {mn:.3f} at {arg}  #(Nm<U/2) {fails}")
