"""z52b Pass-1 U03: Z0738 — are m/p failures enriched in primes p with p-1 or p+1 smooth (5-/7-smooth)?
Reads data/z52b/pass1/U03/exact_results.json (from z52b_p1_U03_exact.py 100000)."""
import json
from math import isqrt
R = json.load(open("data/z52b/pass1/U03/exact_results.json"))["m_over_p"]
PM = 100000
s = bytearray([1]) * (PM + 2); s[0:2] = b"\x00\x00"
for i in range(2, isqrt(PM + 2) + 1):
    if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
primes = [i for i in range(3, PM + 1) if s[i]]
def smooth(n, B):
    for q in (2, 3, 5, 7)[: {5: 3, 7: 4}[B]]:
        while n % q == 0 and n > 0: n //= q
    return n == 1
for B in (5, 7):
    nb = lambda p: smooth(p - 1, B) or smooth(p + 1, B)
    base = [p for p in primes if nb(p)]
    print(f"B={B}: primes<=1e5 with p±1 {B}-smooth: {len(base)}  (Z0738 quotes 182 for 5-smooth)")
    for m in ["12", "15", "20", "24"]:
        F = [p for p in R[m]]
        nF = sum(1 for p in F if nb(p)); fr_F = nF / len(F)
        pool = [p for p in primes if p > int(m)]
        fr_pool = sum(1 for p in pool if nb(p)) / len(pool)
        print(f"  m={m}: failures {len(F)}, with p±1 smooth {nF} ({fr_F:.3f}); pool frac {fr_pool:.3f}; ratio {fr_F/fr_pool:.2f}")
