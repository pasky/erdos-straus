"""R278: Hypothesis TG with unrestricted Lambda's is false -- 'planting' construction.
A = C + [N], B = C^{-1} + [N] with C a set of K quadratic residues mod prime p: every c in C lies in A cap B^{-1}
and contributes +1; extraneous points contribute ~ +-sqrt. Compare S = sum_{c in A cap B^-1} (c/p) with |A||B|/p.
Also: check g'^2 = [[49,20],[120,49]] is not in <R, L^4> (QUESTION_R §2 self-review example).
"""
import random, sys

def leg(a, p):
    r = pow(a % p, (p - 1) // 2, p)
    return -1 if r == p - 1 else r

def tg(p, N, K, seed=1):
    random.seed(seed)
    C = set()
    while len(C) < K:
        c = random.randrange(1, p)
        if leg(c, p) == 1: C.add(c)
    A = set((c + j) % p for c in C for j in range(N)); A.discard(0)
    B = set((pow(c, -1, p) + j) % p for c in C for j in range(N)); B.discard(0)
    S = cnt = 0
    for c in A:
        if pow(c, -1, p) in B:
            cnt += 1; S += leg(c, p)
    return len(A), len(B), cnt, S

def LR_word(M):
    a, b, c, d = M; w = []
    while (a, b, c, d) != (1, 0, 0, 1):
        if a >= b and c >= d and (b, d) != (0, 1) or (b == 0 and d == 1 and c > 0):  # last column smaller -> M = M' L
            a, c = a - b, c - d; w.append('L')
        else:
            b, d = b - a, d - c; w.append('R')
        if min(a, b, c, d) < 0: return None
    return ''.join(reversed(w))

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 1000003
    for N, K in [(4, p // 64), (8, p // 256), (16, p // 1024)]:
        a, b, cnt, S = tg(p, N, K)
        print(f"p={p} N={N} K={K}: |A|={a} |B|={b} |A||B|/p={a*b/p:.0f} #(A cap B^-1)={cnt} sum (c/p)={S}")
    w = LR_word((49, 20, 120, 49))
    print("LR word of [[49,20],[120,49]]:", w)
