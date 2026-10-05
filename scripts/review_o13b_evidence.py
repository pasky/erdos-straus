"""R48b from-scratch recomputation of OMEGA13 Sec.1-2 EVIDENCE numbers (beta=1, C_1=1).

Atoms: M<=T, M=3 mod 4, A=(M+1)/4, D | A^2 (each divisor D counted once).
  S_H = sum 1/phi(M); S_g = sum g/M, g=gcd(M,4D+1); S_Y = sum g_Y/M (g_Y = Y-smooth part).
  V(l) = sum_{l|M} g/M;  report sum_{l>Y} V(l)^2, S_g^2/(Y log Y), max_{l>Y} l V(l)/S_g.
"""
import sys
from math import gcd, log

def main(T):
    N = T + 2
    spf = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j: spf[j] = i
    def fac(n):
        f = {}
        while n > 1:
            p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
        return f
    L = log(T)
    SH = Sg = 0.0
    V = {}
    natoms = 0
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fM = fac(M)
        ph = M
        for p in fM: ph = ph // p * (p - 1)
        divs = [1]
        for p, e in fac(A).items():
            divs = [d * p ** k for d in divs for k in range(2 * e + 1)]
        natoms += len(divs)
        SH += len(divs) / ph
        tot = 0.0
        for D in divs:
            g = gcd(M, 4 * D + 1)
            tot += g
        Sg += tot / M
        for p in fM:
            V[p] = V.get(p, 0.0) + tot / M
    return L, natoms, SH, Sg, V

def main2(T):
    """cleaner second pass for S_Y (avoids the incremental trick)."""
    N = T + 2
    spf = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j: spf[j] = i
    def fac(n):
        f = {}
        while n > 1:
            p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
        return f
    L = log(T)
    Ys = [L ** k for k in (1, 2, 3)]
    SY = [0.0] * len(Ys)
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        divs = [1]
        for p, e in fac(A).items():
            divs = [d * p ** k for d in divs for k in range(2 * e + 1)]
        for D in divs:
            g = gcd(M, 4 * D + 1)
            fg = fac(g)
            for j, Y in enumerate(Ys):
                gy = 1
                for p, e in fg.items():
                    if p <= Y: gy *= p ** e
                SY[j] += gy / M
    return Ys, SY

if __name__ == "__main__":
    T = int(sys.argv[1])
    L, natoms, SH, Sg, V = main(T)
    print(f"T={T} L={L:.3f} atoms={natoms} S_H={SH:.3f} S_g={Sg:.3f} ratio={Sg/SH:.3f}")
    for k in (2, 3, 4, 5):
        Y = L ** k
        s2 = sum(v * v for l, v in V.items() if l > Y)
        mx = max([l * v / Sg for l, v in V.items() if l > Y], default=0.0)
        print(f"  Y=L^{k}={Y:.0f}: sum V^2={s2:.4e}  heur={Sg*Sg/(Y*log(Y)):.4e}  max lV/S={mx:.3f}")
    if len(sys.argv) > 2:
        Ys, SY = main2(T)
        for Y, s in zip(Ys, SY):
            print(f"  S_Y(Y={Y:.0f})={s:.3f}  S_Y/S_H={s/SH:.3f}")
