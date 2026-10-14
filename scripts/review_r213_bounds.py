"""R213: check Prop 2.1(a),(b) bounds on ALL c-odd W_n points (no side conditions except where stated),
odd 3 <= n <= 99, caB <= 2*10^5: (b) c <= (4n+1)(B^2+1)/B ; (a) 4|a => B <= 8 n a^2 and E <= 4na^2 + B^2.
Also completeness of the fixed-B slice for B = 1 (e <= 1 cell): max c observed vs O204 wall (16n+1)/3 among 4|a."""
from math import gcd
NMAX, M = 99, 200000
viol_b = viol_a = 0; maxc = {}
for c in range(1, M + 1, 2):
    for B in range(1, M//c + 1, 2):
        for a in range(1, M//(c*B) + 1):
            g = c*a*B - 1
            if g < 3 or g % 2 == 0: continue
            n0 = (-B*B*pow(4*a*a % g, -1, g)) % g
            for n in range(n0, NMAX + 1, g):
                if n < 3 or n % 2 == 0: continue
                E = (4*n*a*a + B*B)//g
                if c*B > (4*n + 1)*(B*B + 1): viol_b += 1
                if a % 4 == 0 and (B > 8*n*a*a or E > 4*n*a*a + B*B): viol_a += 1
                if B == 1 and a % 4 == 0 and gcd(c*a, n) == 1:
                    maxc[n] = max(maxc.get(n, 0), c)
print("violations (b):", viol_b, " (a):", viol_a)
print("B=1, 4|a: n with max c > (16n+1)/3:", [n for n in maxc if 3*maxc[n] > 16*n + 1])
