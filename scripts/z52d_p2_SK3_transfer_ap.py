# z52d pass2 SK3 fix, item Z2960: search (*) certificate data for linear (3-AP) patterns across primes in AP.
# W_p = {(u,B,C): 4uBC-u-B=p, gcd(u,B)=1, u+B odd, C<=CMAX} (pair form, FRONTIER 2.1).
# Pattern: w1,w2,w3 in W_{p1},W_{p2},W_{p3} with p1,p2,p3 = p, p+D, p+2D and w1+w3 = 2*w2 componentwise,
# w1 != w2 (non-trivial; constant triples are excluded).  Control: p3 replaced by a non-AP prime (p3' near p+2D).
import math, random
from math import gcd
CMAX = 300
def W(p):
    out = []
    for C in range(1, CMAX+1):
        m = 4*C; N = m*p + 1; a = m-1
        while a*a <= N:
            if N % a == 0:
                b = N // a
                for d, e in ((a, b), (b, a)):
                    u = (d+1)//m; B = (e+1)//m
                    if gcd(u, B) == 1 and (u+B) % 2 == 1 and d != e or (d == e and gcd(u,B)==1 and (u+B)%2==1):
                        out.append((u, B, C))
            a += m
    return sorted(set(out))
def isprime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True
random.seed(1)
P1 = [p for p in range(50001, 300000, 4) if isprime(p) and p % 4 == 1]
cache = {}
def Wc(p):
    if p not in cache: cache[p] = W(p)
    return cache[p]
struct = 0; generic = 0; ap_count = 0; ctrl_count = 0; trials = 0; ap_hits = []
random.shuffle(P1)
for p in P1[:3000]:
    for D in (4, 8, 12, 24, 40, 60, 84, 120):
        p2 = p + D; p3 = p + 2*D
        if not (isprime(p2) and isprime(p3) and p2 % 4 == 1 and p3 % 4 == 1): continue
        trials += 1
        W1, W2, W3 = Wc(p), Wc(p2), Wc(p3)
        if not (W1 and W2 and W3): continue
        S3 = set(W3)
        hits = 0
        for w2 in W2:
            for w1 in W1:
                if w1 == w2: continue
                w3 = (2*w2[0]-w1[0], 2*w2[1]-w1[1], 2*w2[2]-w1[2])
                if w3 in S3 and w3 != w2: hits += 1
        ap_count += hits
        for w2 in W2:
            for w1 in W1:
                if w1 == w2: continue
                w3 = (2*w2[0]-w1[0], 2*w2[1]-w1[1], 2*w2[2]-w1[2])
                if w3 in S3 and w3 != w2:
                    const = sum(1 for i in range(3) if w1[i] == w2[i] == w3[i])
                    if const >= 2: struct += 1
                    else: generic += 1
        if hits and len(ap_hits) < 5: ap_hits.append((p, D, hits))
        # control: non-AP prime near p+2D
        for q in range(p3 + 4, p3 + 400, 4):
            if isprime(q) and q % 4 == 1 and q != p3:
                W3c = set(Wc(q)); break
        else:
            continue
        ch = 0
        for w2 in W2:
            for w1 in W1:
                if w1 == w2: continue
                w3 = (2*w2[0]-w1[0], 2*w2[1]-w1[1], 2*w2[2]-w1[2])
                if w3 in W3c and w3 != w2: ch += 1
        ctrl_count += ch
print("AP triples tested:", trials)
print("nontrivial 3-AP hits (AP primes):", ap_count, " control (non-AP third prime):", ctrl_count)
print("hits with >=2 coordinates constant across the triple (affine family, structural):", struct)
print("generic hits (at most one coordinate constant):", generic)
print("sample hits (p,D,count):", ap_hits)
