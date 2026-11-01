# Z0845: is ES-hardness (low U relative to neighbours n±4k) multiplicative? U via scripts/z52d_audit_A1_ucount.c
# (gcc -O2 -o /tmp/z52d_ucount scripts/z52d_audit_A1_ucount.c). Neighbour median over n+4k, 1<=|k|<=K.
import subprocess, statistics, sys
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**.5)+1))
cache = {}
def Ubatch(ns):
    need = sorted(set(n for n in ns if n not in cache))
    for i in range(0, len(need), 200):
        out = subprocess.run(["/tmp/z52d_ucount"] + [str(n) for n in need[i:i+200]], capture_output=True, text=True, timeout=3000).stdout
        for line in out.split("\n"):
            if line: a, b = map(int, line.split()); cache[a] = b
def ratio(n, K):
    nb = [n+4*k for k in range(-K, K+1) if k]
    Ubatch(nb + [n]); return cache[n], statistics.median(cache[m] for m in nb)
K = 5
prs = [p for p in range(4*K+5, 1500) if p % 4 == 1 and isprime(p)]
Ubatch([p+4*k for p in prs for k in range(-K, K+1)])
R = sorted((ratio(p, K)[0]/ratio(p, K)[1], p) for p in prs)
H = [p for _, p in R[:10]]; M = [p for _, p in R[len(R)//2-5:len(R)//2+5]]; Ez = [p for _, p in R[-10:]]
print("K =", K, "; hardest primes p≡1(4)<1500 (p, U, median, ratio):", [(p, *ratio(p, K), round(r, 2)) for r, p in R[:10]])
print("median-hardness primes:", M, " easiest:", Ez)
def semis(L): return [L[i]*L[j] for i in range(len(L)) for j in range(i+1, len(L))]
for name, L in (("hard×hard", H), ("median×median", M), ("easy×easy", Ez), ("hard×easy", None)):
    ns = semis(L) if L else [h*e for h in H[:5] for e in Ez[:5]]
    ns = [n for n in ns if n < 1500000][:25]
    Ubatch([n+4*k for n in ns for k in range(-K, K+1)])
    rs = [ratio(n, K)[0]/ratio(n, K)[1] for n in ns]
    print(f"{name}: {len(rs)} semiprimes, U/median: mean {statistics.mean(rs):.2f}, median {statistics.median(rs):.2f}, min {min(rs):.2f}, max {max(rs):.2f}")
    sys.stdout.flush()
print("193·241 =", 193*241, ratio(193*241, K))
# residue-matched control: primes in Mordell-hard classes (square classes mod 840), excluding the 10 hardest
sq840 = {1, 121, 169, 289, 361, 529}
C = [p for _, p in R if p % 24 == 1 and p not in H][::2]
print("residue-matched control primes (p ≡ 1 mod 24, not hardest, every 2nd by hardness rank):", C[:12], "... their prime ratios median",
      round(statistics.median(ratio(p, K)[0]/ratio(p, K)[1] for p in C), 2), "vs hardest median",
      round(statistics.median(ratio(p, K)[0]/ratio(p, K)[1] for p in H), 2))
ns = [n for n in semis(C[:10]) if n < 1500000][:25]
Ubatch([n+4*k for n in ns for k in range(-K, K+1)])
rs = [ratio(n, K)[0]/ratio(n, K)[1] for n in ns]
print(f"control×control (p,q ≡ 1 mod 24): {len(rs)} semiprimes, U/median: mean {statistics.mean(rs):.2f}, median {statistics.median(rs):.2f}, min {min(rs):.2f}")
hh = sorted((ratio(n, K)[0]/ratio(n, K)[1], n) for n in semis(H) if n < 1500000)[:5]
print("lowest hard×hard semiprimes (ratio, n, n mod 840):", [(round(r, 2), n, n % 840) for r, n in hh])
car = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
print("Carmichael U/median (K=5):", [(n, round(ratio(n, K)[0]/ratio(n, K)[1], 2)) for n in car])
