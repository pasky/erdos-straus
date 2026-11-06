# Numerical test of the Gamma(4C) trace identity (Theorem 2 candidate).
# Spectral: Tr(T_Delta | S_k(Gamma(4C))) = (-1)^k * sum_{chi mod 4C, chi(-1)=(-1)^k} Tr(T_N | S_k(Gamma0(16C^2),chi)), N=4Cn+1.
# Geometric pieces: E = sum_s P_k(4Cw-2,N) H(4s-w^2) (line class-number sum), ES_k, TRIV_k (min^{k-1} weights).
import sys, json
from fractions import Fraction
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)

def Pk(k, t, N):
    # (rho^{k-1}-rhobar^{k-1})/(rho-rhobar): P1=0? use recursion P_1=0,P_2=1,P_{j+1}=t P_j - N P_{j-1}
    a, b = 0, 1
    for _ in range(k-2):
        a, b = b, t*b - N*a
    return b if k >= 2 else 0

def H(D):
    return Fraction(str(pari.qfbhclassno(D)))

def geom_pieces(C, n, k):
    N = 4*C*n+1
    E = Fraction(0)
    s = 1
    # w = 4Cs-n, need w^2 < 4s
    smin = max(1, (n - 2*int((n/C)**0.5) - 10)//(4*C))
    for s in range(smin, (n + 2*int((n/C)**0.5) + 10)//(4*C) + 2):
        w = 4*C*s - n
        if w*w < 4*s:
            E += Pk(k, 4*C*w-2, N) * H(4*s - w*w)
    ES = 0; TR = 0
    for d in range(1, N+1):
        if d*d > N: break
        if N % d == 0:
            e = N//d
            m = min(d, e)**(k-1)
            mult = 1 if d == e else 2
            if d % (4*C) == (4*C-1) and e % (4*C) == (4*C-1): ES += mult*m
            if d % (4*C) == 1 % (4*C) and e % (4*C) == 1 % (4*C): TR += mult*m
    return E, ES, TR

def spectral(C, k, Nmax):
    M = 16*C*C; Q = 4*C
    G = pari.znstar(M, 1)
    tot = [0]*(Nmax+1)
    nsp = 0
    for a in range(1, M):
        if pari.gcd(a, M) != 1: continue
        chi = pari.znconreylog(G, a)
        cond = pari.znconreyconductor(G, chi)
        c0 = int(cond[0]) if str(pari.type(cond)) == 't_VEC' else int(cond)
        if Q % c0 != 0: continue
        par = pari.zncharisodd(G, chi)
        if int(par) != (k % 2): continue
        mf = pari.mfinit([M, k, pari.Mod(a, M)], 1)
        d = int(pari.mfdim(mf))
        if d == 0: continue
        nsp += d
        tf = pari.mftraceform([M, k, pari.Mod(a, M)], 1)
        co = pari.mfcoefs(tf, Nmax)
        for i in range(Nmax+1):
            tot[i] += co[i]
    tot = [pari.simplify(pari.lift(x)) if str(pari.type(x))=="t_POLMOD" else pari.simplify(x) for x in tot]
    return tot, nsp

if __name__ == "__main__":
    C = int(sys.argv[1]); k = int(sys.argv[2]); nmax = int(sys.argv[3])
    Nmax = 4*C*nmax+1
    tot, dim = spectral(C, k, Nmax)
    rows = []
    for n in range(1, nmax+1):
        N = 4*C*n+1
        E, ES, TR = geom_pieces(C, n, k)
        T = Fraction(str(tot[N])) * (-1)**k
        rows.append((n, N, str(T), str(E), ES, TR))
    print(json.dumps({"C": C, "k": k, "dim": dim, "rows": rows}))
