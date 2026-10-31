"""z52b pass1 L00 Z2822 control: same box classification over Z for rational primes p <= 200 (x,y in [-R,R]\\{0}, z = pxy/(4xy-p(x+y)) in Z).
Counts hits with p | z (the analogue of the pi | zeta family in Z[i]). Usage: python3 scripts/z52b_p1_L00_z_classify.py R"""
import sys, json
R = int(sys.argv[1]) if len(sys.argv) > 1 else 16
def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n**0.5)+1))
tot = pdiv = 0; per = []
for p in [q for q in range(2, 201) if is_prime(q)]:
    h = hz = 0
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if x == 0 or y == 0: continue
            D = 4*x*y - p*(x+y)
            if D == 0: continue
            num = p*x*y
            if num % D or num // D == 0: continue
            z = num // D; h += 1; hz += (z % p == 0)
    tot += h; pdiv += hz; per.append((p, h, hz))
out = {"R": R, "hits": tot, "hits_with_p_divides_z": pdiv, "fraction": pdiv/tot if tot else None}
json.dump(out, open("data/z52b/pass1/L00/z_classify_R%d.json" % R, "w"), indent=1)
print(out)
