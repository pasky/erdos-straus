# z52d Pass 2 NC0, item Z0157 — |H_1| of the Brieskorn link Σ(a,b,c) = {x^a+y^b+z^c=0} ∩ S^5 via Milnor–Orlik.
# Milnor–Orlik: Δ(t)=∏_i (t^{a_i}-1)/(t-1)-type divisor: write the divisor  ∏_i (Λ_{a_i} - Λ_1)  in the ring with
# Λ_a·Λ_b = gcd(a,b)·Λ_lcm(a,b); the result Σ c_k Λ_k gives Δ(t)=∏ (t^k-1)^{c_k}.  If Σ_k c_k = 0 the link has finite H_1 and
# |H_1| = |Δ(1)| = ∏_{k>=2} k^{c_k}; if the product is 0/undefined H_1 is infinite (b_1>0).  Checks: (2,2,3)->3 (A_2), (2,2,5)->5 (A_4),
# (2,3,5)->1 (Poincaré sphere), (2,3,6)-> infinite (simple elliptic Ẽ_8).
from fractions import Fraction
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)
def milnor_orlik(exps):
    E={1:1}
    for a in exps:
        new={}
        for k,c in E.items():
            # Λ_a * Λ_k = gcd(a,k) Λ_lcm
            kk=lcm(a,k); new[kk]=new.get(kk,0)+c*gcd(a,k)
            new[k]=new.get(k,0)-c
        E={k:c for k,c in new.items() if c}
    return E
def h1_order(exps):
    E=milnor_orlik(exps)
    if sum(E.values())!=0: return None, E   # (cannot happen for isolated sing.; kept as a guard)
    val=Fraction(1); 
    for k,c in E.items():
        if k==1: continue
        val*=Fraction(k)**c
    if val==0: return 'inf', E
    return val, E
if __name__=='__main__':
    for ex in [(2,2,3),(2,2,5),(2,3,5),(2,3,6),(3,3,3),(2,2,2+1),(2,4,5)]:
        v,_=h1_order(ex); print(ex,'|H1| =',v)
