# R246: s6_ydual_windows Prop (a), cap-0 (integer) slice: y = pA, M = 4A - 1; 4/p - 1/(pA) = M/(pA) = 1/x + 1/z.
# Claim: if -p/4 not in <primes of A> mod M then no integer x, z. Brute force over all divisors of (pA)^2.
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
for A in (2, 3, 5, 6, 8, 12):
    M = 4*A - 1; H = {1}
    for s in fac(A):
        for _ in range(M): H |= {(h*s) % M for h in H}
    viol = 0; tested = 0
    for p in primes(20000):
        if M % p == 0 or A % p == 0: continue
        inH = ((-p * pow(4, -1, M)) % M) in H
        N = p*A; f = fac(N); D = [1]
        for q, e in f.items(): D = [d*q**k for d in D for k in range(2*e + 1)]
        sol = any((N + d) % M == 0 and (N + N*N//d) % M == 0 for d in D)
        tested += 1; viol += (sol and not inH)
    print(f"A={A} M={M} |<primes A>|={len(H)}: primes tested {tested}, integer solutions outside the subgroup: {viol}")
