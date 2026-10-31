"""Z0142 pass-1: n ≤ N with 4/n = 1/a² + 1/b² + 1/c² (a ≤ b ≤ c positive integers); exhaustive per n."""
import sys, json
from math import isqrt
N = int(sys.argv[1]); reps = {}
for n in range(1, N+1):
    sols = []
    a = isqrt(n//4)
    while True:
        a += 1
        if 4*a*a > 3*n and a*a*4 > 3*n: 
            if 3*n < 4*a*a: break
        num1, den1 = 4*a*a - n, n*a*a          # r1 = num1/den1 > 0
        if num1 <= 0: continue
        b = max(a, isqrt(den1//num1))
        while True:
            # need 1/b² ≤ r1 (strict <) and 1/b² ≥ r1/2
            if num1*b*b <= den1: b += 1; continue
            if 2*den1 < num1*b*b: break
            num2, den2 = num1*b*b - den1, den1*b*b
            if den2 % num2 == 0:
                c2 = den2//num2; c = isqrt(c2)
                if c*c == c2 and c >= b: sols.append((a, b, c))
            b += 1
    if sols: reps[n] = sols
out = dict(N=N, count=len(reps), ns=sorted(reps), examples={k: reps[k][:2] for k in sorted(reps)[:40]})
print(len(reps), sorted(reps)[:80]); json.dump(out, open(f'data/z52b/pass1/H00/recsq_{N}.json', 'w'))
