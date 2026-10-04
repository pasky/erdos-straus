"""Review check of EXCEPTIONAL_NONCRT Conj 8.5 (EVIDENCE only): for n <= N count Case-B data (M,D)
via the normal form of notes Thm 60.1: (g,u,v,d), (u,v)=1, d|g, a=4gv-n>=1, au=d+v; M=4gu-1.
Enumerate (g, d|g, v, u | d+v), a=(d+v)/u, n=4gv-a in [1,N]. Report per-integer mean of data with
M>N and with M<=N, normalised by (log N)^2 and (log N)^3, plus the multiplier-one count (Prop 8.4)."""
import math, sys

def divisors(m):
    out = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            out.append(i)
            if i * i != m: out.append(m // i)
        i += 1
    return out

for N in [int(x) for x in sys.argv[1:]]:
    big = small = one = 0
    B = (N + 1) // 3
    for g in range(1, B + 1):
        dg = divisors(g)
        vmax = (N + g) // (4 * g - 1) if 4 * g > 1 else N
        for v in range(1, min(vmax, B) + 1):
            for d in dg:
                for u in divisors(d + v):
                    if math.gcd(u, v) != 1: continue
                    a = (d + v) // u
                    n = 4 * g * v - a
                    if not (1 <= n <= N): continue
                    M = 4 * g * u - 1
                    if M > N: big += 1
                    else: small += 1
                    if a == 1: one += 1
    L = math.log(N)
    print(f"N={N}: mean data M>N: {big/N:.2f} (/log^2={big/N/L**2:.3f}, /log^3={big/N/L**3:.4f}); "
          f"M<=N: {small/N:.2f} (/log^3={small/N/L**3:.4f}); mult-one mean {one/N:.2f} vs bound {(N+1)*(1+L)**2/4/N:.1f}")
