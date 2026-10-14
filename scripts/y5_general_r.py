"""y5_general_r: (i) general-r frieze Jacobi law via leading-minor Hasse formula:
   for a positive word a (letters >= 2) of length r with N = K(a) odd,
       (K(a_1..a_{r-1}) / N) = prod_{i=1}^{r-1} (K_i, -K_{i+1})_2 ,  K_i = K(a_1..a_i)   [Hilbert symbols at 2]
   (i') signed words: (K_{r-1}/N) = s_2 * s_inf with s_inf = (-1)^{#i: K_i < 0 < K_{i+1}}  (archimedean factor)
   (ii) r-uniqueness: for every r >= 5 the word (2,2,2,4,2^{r-5},k) with k = (N+B)/A, N = (3+2A)^2,
   A = K(2,2,2,4,2^{r-5}), B = K(2,2,2,4,2^{r-6}) (B = K(2,2,2) = 4 if r = 5), has K = N an odd square and a
   letter = 0 (mod 4).  usage: y5_general_r.py NRAND RMAX"""
import sys, random
from y2_even_edge import jacobi


def K(w):
    a, b = 1, 0  # K(empty)=1, K(before)=0 ; K_i = a_i K_{i-1} - K_{i-2}
    for x in w: a, b = x * a - b, a
    return a


def v2(x):
    v = 0
    while x % 2 == 0: x //= 2; v += 1
    return v, x


def hilb2(a, b):
    """2-adic Hilbert symbol (a,b)_2 for nonzero integers."""
    va, u = v2(a); vb, w = v2(b)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = eps(u) * eps(w) + va * om(w) + vb * om(u)
    return -1 if e % 2 else 1


rng = random.Random(213); NR = int(sys.argv[1]); RMAX = int(sys.argv[2]); bad = 0; tested = 0
for _ in range(NR):
    r = rng.randint(1, 12); w = [rng.randint(2, rng.choice([5, 9, 40, 1000])) for _ in range(r)]
    Ks = [K(w[:i]) for i in range(r + 1)]; N = Ks[r]
    if N % 2 == 0: continue
    tested += 1
    rhs = 1
    for i in range(1, r): rhs *= hilb2(Ks[i], -Ks[i + 1])
    if jacobi(Ks[r - 1], N) != rhs: bad += 1
print(f"(i) random words tested {tested}, failures {bad}")
sbad = 0; stested = 0
for _ in range(NR):
    r = rng.randint(1, 10); w = [rng.choice([-1, 1]) * rng.randint(1, rng.choice([5, 9, 40])) for _ in range(r)]
    Ks = [K(w[:i]) for i in range(r + 1)]; N = Ks[r]
    if N <= 0 or N % 2 == 0 or 0 in Ks: continue
    stested += 1
    s2 = sinf = 1
    for i in range(1, r):
        s2 *= hilb2(Ks[i], -Ks[i + 1])
        if Ks[i] < 0 and -Ks[i + 1] < 0: sinf = -sinf
    if jacobi(Ks[r - 1] % N, N) != s2 * sinf: sbad += 1
print(f"(i') signed words (all K_i != 0, N > 0 odd) tested {stested}, failures {sbad};  law: (K_(r-1)/N) = s_2 * s_inf")
bad += sbad
fam_bad = 0
for r in range(5, RMAX + 1):
    pre = [2, 2, 2, 4] + [2] * (r - 5); A = K(pre); B = K(pre[:-1]); N = (3 + 2 * A) ** 2
    if (N + B) % A: fam_bad += 1; continue
    k = (N + B) // A; w = pre + [k]
    if not (K(w) == N and len(w) == r and k >= 2 and N % 2): fam_bad += 1
print(f"(ii) family r=5..{RMAX}: failures {fam_bad}")
sys.exit(1 if bad or fam_bad else 0)
