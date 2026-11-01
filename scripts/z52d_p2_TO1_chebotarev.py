# z52d pass2 TO1 (Z0252): B2 divisor covering. For C>=1 and d = -1 mod 4C, B2 holds at p if d | 4Cp+1 (repo: BRAINSTORM 'B2 <=> exists C,d: d|4Cp+1, d=-1 mod 4C').
# For fixed (C,d) the condition is p = r (mod d) with r = -(4C)^{-1} mod d, i.e. a Chebotarev/Frobenius condition in Q(zeta_d) (d prime: one class of (Z/d)^*-Frobenius; d composite: ray classes).
# Measures: fraction of primes p = 1 mod 4 (p < N) NOT covered by any (C,d) with C<=Cmax, d<=D.
# usage: uv run --with numpy python scripts/z52d_p2_TO1_chebotarev.py N Cmax D
import sys, numpy as np
N=int(sys.argv[1]); Cmax=int(sys.argv[2]); D=int(sys.argv[3])
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
P=np.array([p for p in range(5,N) if s[p] and p%4==1],dtype=np.int64)
cov_by_C={}
covered=np.zeros(len(P),bool)
for C in range(1,Cmax+1):
    cC=np.zeros(len(P),bool)
    for d in range(4*C-1, D+1, 4*C):
        if d<=1: continue
        cC |= ((4*C*P+1) % d == 0)
    cov_by_C[C]=cC.mean()
    covered |= cC
    print(f"C={C}: fraction covered by d<={D}, d=-1 mod 4C: {cC.mean():.4f}; cumulative C<=C: {covered.mean():.4f}")
print(f"primes p=1 mod 4, p<{N}: {len(P)}; uncovered by C<={Cmax}, d<={D}: {int((~covered).sum())} ({(~covered).mean():.4f})")
print("first uncovered:", P[~covered][:15].tolist())
