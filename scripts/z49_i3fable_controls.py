import numpy as np
from math import isqrt
I3=np.fromfile('/tmp/i3_1e8_i3.u16',dtype=np.uint16); MV=np.fromfile('/tmp/i3_1e8_minv.u32',dtype=np.uint32); MT=np.fromfile('/tmp/i3_1e8_mint.u32',dtype=np.uint32); L8=np.fromfile('/tmp/i3_1e8_lev8.u8',dtype=np.uint8)
print("# control primes: p, I3(p), least larger endpoint, least level")
for p in [193,409,577,2521,3361,5569,9601,66529,8813281, 17,241,131,11]:
    print(p, int(I3[p]), int(MV[p]), int(MT[p]))
N=len(I3)-1
# Lemma 4.3 / Thm 2.1 level check at all squares <= 1e8
bad=0; badE=0
for m in range(2, isqrt(N)+1):
    b=int(L8[m*m])
    if b & ((1<<0)|(1<<4)|(1<<7)): bad+=1
    if m%2==0 and (b & (1<<3)): badE+=1
print("squares m^2<=1e8:", isqrt(N)-1, "; with a word at level t=0 mod 4 or 7 mod 8:", bad, "; even m with level 3 mod 8:", badE)
# even squares: min larger endpoint > 8 always?
ev=[m*m for m in range(2,isqrt(N)+1,2)]
print("even squares with an interior word of larger endpoint <= 8:", int(np.sum(MV[ev]<=8)), " min over even squares of minV (excluding zeros):", int(np.min(MV[ev])))
od=[m*m for m in range(3,isqrt(N)+1,2)]
print("odd squares: min minV:", int(np.min(MV[od])), "; fraction with minV=6:", float(np.mean(MV[od]==6)))
# 2*squares
s2=[2*m*m for m in range(2,isqrt(N//2)+1)]
print("2m^2: min minV", int(np.min(MV[s2])))
# zeros table data
import sympy
zeros=[int(l.split()[1]) for l in open('data/z48_ltfable/big_1e9.txt') if l.startswith('I30')]
print(len(zeros))
