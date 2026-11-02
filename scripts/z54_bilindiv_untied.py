# Untied (fixed-modulus-relaxed) divisor count for the k-form of the balanced block (Z54_BILINDIV §5.1, EVIDENCE):
#   N_rel(Q) := sum_{k in K} #{X | kp+1 : kU < X <= 2kU, X = -1 mod gcd(k,Q)},  K = (p/(4U^2), p/U^2]
# Q = 1 is the untied count; N2 <= N_rel(Q) for every Q (2-cycles have X = ku-1).  Usage: python ... p [Q ...]
import sys, math
from sympy import divisors
p=int(sys.argv[1]); Qs=[int(q) for q in sys.argv[2:]] or [1]
U=int(round(p**0.25))
while (U+1)**4<=p: U+=1
while U**4>p: U-=1
cnt={Q:0 for Q in Qs}; nk=0
for k in range(p//(4*U*U)+1, p//(U*U)+1):
    nk+=1; n=k*p+1
    ds=[X for X in divisors(n) if k*U< X <=2*k*U]
    for Q in Qs:
        g=math.gcd(k,Q); cnt[Q]+=sum(1 for X in ds if (X+1)%g==0)
print(p,U,"levels",nk,"U^2*log2=%.0f"%(U*U*math.log(2)), " ".join("Q=%d:%d(%.3f U^2)"%(Q,cnt[Q],cnt[Q]/U/U) for Q in Qs))
