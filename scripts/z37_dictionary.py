"""O267 §1: exact dictionary checks.
(a) words w=(t,u,v), n=tuv-u-v  <->  gamma_w=[[A,n],[t,A*]] in SL2(Z), A=tu-1, A*=tv-1 == -1 mod t.
(b) per-level sign: for n = 1 (4), chi(w)=(A/n) equals (2/n)^e * J(-t, A_odd)  (A = 2^e A_odd).
(c) the sign depends only on (t mod 8, A mod 8, n mod 8): print the table support.
(d) theta-multiplier / Kronecker sigma(g)=(c/d) is multiplicative on random products in Gamma1(4)>=0.
Usage: PYTHONPATH=scripts uv run python scripts/z37_dictionary.py NMAX
"""
import sys, random
from sympy import jacobi_symbol as J

def kron(a, b):  # Kronecker (a/b), b>0
    if b == 0: return 1 if abs(a) == 1 else 0
    r = 1
    while b % 2 == 0:
        b //= 2
        if a % 2 == 0: return 0
        r *= 1 if a % 8 in (1, 7) else -1
    return r * J(a % b, b) if b > 1 else r

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
bad = 0; table = {}; nw = 0
t = 2
while 4 * t - 4 <= NMAX:
    u = 2
    while 2 * (t * u - 1) - u <= NMAX:
        A = t * u - 1; v = 2
        while True:
            n = v * A - u
            if n > NMAX: break
            if n % 4 == 1:
                As = t * v - 1
                assert A * As - n * t == 1 and A % t == t - 1 and As % t == t - 1
                chi = J(A, n)
                e, Ao = 0, A
                while Ao % 2 == 0: Ao //= 2; e += 1
                pred = (J(2, n) ** e) * J(-t % Ao if Ao > 1 else 0, Ao) if Ao > 1 else J(2, n) ** e
                if chi != pred: bad += 1
                key = (t % 8, A % 8, n % 8)
                table.setdefault(key, set()).add(chi); nw += 1
            v += 1
        u += 1
    t += 1
amb = [k for k, s in table.items() if len(s) > 1]
print(f"(a,b) words n<= {NMAX}, n=1(4): {nw}; sign-formula failures: {bad}")
print(f"(c) cells (t,A,n mod 8) seen: {len(table)}; ambiguous cells: {len(amb)}")
neg = sorted(k for k, s in table.items() if s == {-1})
print("    chi=-1 cells (t%8,A%8,n%8):", neg)

# (d) sigma multiplicative on Gamma1(4)>=0
random.seed(1)
def rand_g1_4():
    # random positive word in L,R, kept if in Gamma1(4)
    while True:
        M = [[1, 0], [0, 1]]
        for _ in range(random.randint(2, 14)):
            if random.random() < .5: M = [[M[0][0] + M[0][1], M[0][1]], [M[1][0] + M[1][1], M[1][1]]]  # *L
            else: M = [[M[0][0], M[0][0] + M[0][1]], [M[1][0], M[1][0] + M[1][1]]]  # *R
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        if a % 4 == 1 and d % 4 == 1 and c % 4 == 0: return M
mul = lambda X, Y: [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
                    [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
sig = lambda M: kron(M[1][0], M[1][1])
sab = lambda M: kron(M[0][0], M[0][1])
f1 = f2 = 0; cnt = {1: 0, -1: 0}
for _ in range(20000):
    X, Y = rand_g1_4(), rand_g1_4()
    if sig(mul(X, Y)) != sig(X) * sig(Y): f1 += 1
    if sig(X) != sab(X): f2 += 1
    cnt[sig(X)] += 1
print(f"(d) sigma(XY)=sigma(X)sigma(Y) failures: {f1}/20000; (c/d)!=(a/b) failures: {f2}; sigma distribution {cnt}")
print("    example in Psi':", [[5, 2], [12, 5]], "sigma =", sig([[5, 2], [12, 5]]))
