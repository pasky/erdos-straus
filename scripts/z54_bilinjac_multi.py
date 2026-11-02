"""z54 BILINJAC: run the balanced-block strip statistics (z54_bilinjac_strip.c) over many n of each control type.
usage: uv run --with sympy python scripts/z54_bilinjac_multi.py /tmp/z54strip EXP NPRIMES NSQ OUT
  EXP: n ~ 10^EXP; types: primes = 1 mod 24 (NPRIMES consecutive), odd squares m^2 and near-squares m^2+4 (NSQ each),
  plus the FRONTIER §4 item-14 test primes when EXP == 0 (small scale; parameters scaled per n).
Balanced parameters per n: V = round(n^(1/4)), W = round(sqrt(n)/16), s in (2V, 4V]; P in {round(sqrt V), round(V/4)}; q0 = 61
(or the largest prime <= V/2 if smaller)."""
import sys, subprocess, math
from sympy import isprime, prevprime, nextprime

exe, EXP, NPR, NSQ, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]

def params(n):
    V = round(n ** 0.25); W = max(2, round(math.isqrt(n) / 16)); return V, W, 2 * V, 4 * V

def run(n, tag, fh):
    V, W, S1, S2 = params(n)
    q0 = 61 if V >= 122 else prevprime(max(5, V // 2) + 1)
    for P in (max(3, round(math.sqrt(V))), max(3, V // 4)):
        r = subprocess.run(["timeout", "600", exe, str(n), str(W), str(S1), str(S2), str(P), "300", str(q0)],
                           capture_output=True, text=True, check=True)
        fh.write(f"{tag} V={V} W={W} " + r.stdout); fh.flush()

with open(OUT, "w") as fh:
    if EXP == 0:
        for p in [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281]:
            run(p, "testprime", fh)
    else:
        x = 10 ** EXP; p = x; c = 0
        while c < NPR:
            p = nextprime(p)
            if p % 24 == 1:
                run(p, "prime1mod24", fh); c += 1
        m = math.isqrt(x) + 1
        if m % 2 == 0: m += 1
        for i in range(NSQ):
            run(m * m, "oddsquare", fh); run(m * m + 4, "nearsq+4", fh); m += 2
