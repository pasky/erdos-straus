"""R282 from-scratch: SPARKS9 Lemma 1.1 / Cor 1.2.  For n <= NB (all n, odd and even) and k in 2..KB:
 c=1 line of k/n:  exists a,b,d >= 1 with n + a + b = k*a*b*d
 b=1 line of k/n:  exists a,c,d >= 1 with c*n + a + 1 = k*a*c*d
 words W(n): (t,u,v) >= 1 with t*u*v - u - v = n.
Check: c=1 <=> some word has k|t ; b=1 <=> some word has k|v ; union <=> some coordinate = 0 mod k.
Also Lemma 1.1 bijection for c in 1..6."""
import sys
NB, KB = int(sys.argv[1]), int(sys.argv[2])

def words(n):
    W = []
    for t in range(1, n + 3):
        for u in range(1, n + 4):
            den = t*u - 1
            if den <= 0: continue
            if den > n + u: break
            if (n + u) % den == 0:
                W.append((t, u, (n + u)//den))
    return W

def c1(n, k):
    for a in range(1, n + 2):
        for d in range(1, n + 2):
            den = k*a*d - 1
            if den > n + a: break
            if den > 0 and (n + a) % den == 0: return True
    return False

def b1(n, k):
    for c in range(1, n + 3):
        for d in range(1, n + 2):
            den = k*c*d - 1
            if den > c*n + 1: break
            if den > 0 and (c*n + 1) % den == 0: return True
    return False

bad = 0; cnt = 0
for n in range(1, NB + 1):
    W = words(n)
    # independent sanity: each word satisfies the equation
    assert all(t*u*v - u - v == n for t, u, v in W)
    for k in range(2, KB + 1):
        A = c1(n, k); B = b1(n, k)
        wt = any(t % k == 0 for t, u, v in W); wv = any(v % k == 0 for t, u, v in W)
        wu = any(u % k == 0 for t, u, v in W)
        cnt += 1
        if A != wt or B != wv or wu != wv or (A or B) != any(x % k == 0 for w in W for x in w):
            bad += 1; print("mismatch", n, k, A, B, wt, wv, wu)
# Lemma 1.1
for n in range(1, 120):
    for c in range(1, 7):
        lhs = sorted((c*s, c*g - 1, 1) for (t, g, s) in words(n) if t == c and c*s > 1)
        rhs = sorted(w for w in words(c*n) if w[2] == 1 and w[0] % c == 0 and w[0] > 1)
        if lhs != rhs: bad += 1; print("Lemma1.1 mismatch", n, c)
print(f"n<={NB}, k<={KB}: {cnt} (n,k) cases, Lemma 1.1 n<120 c<=6; mismatches={bad}")
