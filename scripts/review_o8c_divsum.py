"""R30c from-scratch check of POINTWISE_OMEGA8 Prop 6.6 and input (D).

For primes l = 3 mod 4, A_l=(l+1)/4:
  S1(T)  := sum_{l in (sqrt T, T]} #{D<=A_l : D | A_l^2}/(l-1)   (single mass, m=1 atoms)
  D(x)   := sum_{p<=x, p=3(4)} tau(A_p^2) / (pi(x) (log x)^2)
Also verifies, for small l, that the classes -4D mod l are distinct.
Usage: review_o8c_divsum.py  [maxexp=8]
"""
import sys, math
import numpy as np

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0]

def spf_upto(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    for p in primes_upto(int(n ** 0.5) + 1):
        blk = spf[p * p::p]; blk[blk == 0] = p
    idx = np.nonzero(spf == 0)[0]; spf[idx] = idx
    return spf

def tau_sq(ns, spf):
    rem = ns.astype(np.int64).copy(); res = np.ones_like(rem)
    while True:
        act = rem > 1
        if not act.any(): break
        p = spf[rem[act]].astype(np.int64)
        r = rem[act]; a = np.zeros_like(r)
        while True:
            dv = (r % p == 0)
            if not dv.any(): break
            r = np.where(dv, r // p, r); a += dv
        rem[act] = r; res[act] *= (2 * a + 1)
    return res

def main():
    E = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    Tmax = 10 ** E
    P = primes_upto(Tmax); P3 = P[P % 4 == 3]
    spf = spf_upto(Tmax // 4 + 2)
    A = (P3 + 1) // 4
    tq = tau_sq(A, spf)
    # sanity: distinct classes -4D mod l, and count (tau+1)/2, for small l
    for l in P3[:400]:
        a = (int(l) + 1) // 4
        Ds = [D for D in range(1, a + 1) if (a * a) % D == 0]
        cls = {(-4 * D) % int(l) for D in Ds}
        assert len(cls) == len(Ds) and 0 not in cls
        assert len(Ds) == (int(tau_sq(np.array([a]), spf)[0]) + 1) // 2
    print("classes -4D mod l distinct, nonzero, count=(tau(A^2)+1)/2: OK (first 400 l)")
    cnt = (tq + 1) // 2
    print(" T        L=logT   S1(T)    S1/L^2   (D)-ratio sum_{p<=T,3(4)}tau/(pi(T) L^2)  dyadic (T/2,T] ratio")
    for e in range(3, E + 1):
        for T in (10 ** e, 3 * 10 ** e) if e < E else (10 ** e,):
            L = math.log(T)
            sel = (P3 > math.isqrt(T)) & (P3 <= T)
            S1 = float(np.sum(cnt[sel] / (P3[sel] - 1.0)))
            piT = int(np.sum(P <= T))
            Dr = float(np.sum(tq[P3 <= T])) / (piT * L * L)
            dy = (P3 > T // 2) & (P3 <= T)
            pid = int(np.sum((P > T // 2) & (P <= T)))
            Dd = float(np.sum(tq[dy])) / (pid * L * L)
            print(f" {T:<9.0e} {L:6.2f}  {S1:8.3f}  {S1/L/L:.4f}   {Dr:.4f}   {Dd:.4f}")

if __name__ == "__main__":
    main()
