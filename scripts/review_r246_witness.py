# R246 from scratch: s6_witness_onesided numerics. p = 1 (4) prime < N, q = 3 (4) prime < QM, K = (p+q)/4.
# Lemma 1.1 at cap <= E: exists d = prod s^c_s, d = -K (mod q), c_2 <= 2 b_2, odd s: c_s <= 2 b_s or (c_s even, <= 2 b_s + 2E).
import sys
def primes(n):
    s = bytearray([1])*(n+1); s[0] = s[1] = 0
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def fac(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def ok(K, q, E):
    S = {1}
    for s, b in fac(K).items():
        cs = range(2*b + 1) if s == 2 else [c for c in range(2*b + 2*E + 1) if c <= 2*b or c % 2 == 0]
        S = {(x*pow(s, c, q)) % q for x in S for c in cs}
    return (-K) % q in S
N, QM, EM = 3000, 120, 6
st = {}
for p in primes(N):
    if p % 4 != 1: continue
    for q in primes(QM):
        if q % 4 != 3: continue
        K = (p + q)//4; lg = pow(q, (p-1)//2, p) == 1
        cap = next((E for E in range(EM + 1) if ok(K, q, E)), None)
        key = ('+1' if lg else '-1', K % 2)
        a = st.setdefault(key, [0, 0, 0]); a[0] += 1; a[1] += cap == 0; a[2] += cap is None
for k in sorted(st): print("(q/p) =", k[0], "K mod 2 =", k[1], " pairs, cap0, dead(cap<=6):", st[k])
# (2) (q/p) = -1: dead at EVERY cap (E = q suffices: odd exponents mod ord_q(s) | q-1)?  Split by K parity and CAP_DOWN (E).
dead_all = {}
for p in primes(N):
    if p % 4 != 1: continue
    for q in primes(QM):
        if q % 4 != 3 or pow(q, (p-1)//2, p) == 1: continue
        K = (p + q)//4; t = (K & -K).bit_length() - 1
        if not ok(K, q, q):
            key = (K % 2, q % 8 == 7 or t % 2 == 0); dead_all[key] = dead_all.get(key, 0) + 1
print("(q/p) = -1 dead at every cap, keyed (K odd?, CAP_DOWN (E) holds?):", dead_all)
