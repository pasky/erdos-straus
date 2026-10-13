# STERILE_STEER — steering by proved sterile Mordell points (O188, spark relay M)

Status: in progress (O188). **ES is not solved, here or anywhere; nothing below proves a case of it.** Labels as in
DISCOVERIES.md. Builds on DEPTH_ASPECT.md (O178, CLAIMED, under hostile review R178/R187), POINTWISE_MORDELL.md §2.1,
POINTWISE_MORDELL17*.md, EXPONENT_COVERING.md (O185, branch side-agent/exponent-covering, in progress).
Scripts `scripts/ss_*`. Memos `BRAINSTORM/bsM_*.md`.

Notation. ET class = residue class ρ (mod M) of one of the seven fixed-parameter families of ET Prop 1.9
(`scripts/mordell_lib.py`). For a prime r, x(u) ∈ Ẑ^× is the r-generic point (x_q = 1 for q ≠ r, x_r = u).
x is *sterile* if it lies in no ET class. For an integer M write M_r = r^{v_r(M)} and M' = M/M_r.

## 0. Iteration log

* (I1) Steering question (1): which hypothesis of DEPTH_ASPECT Thm 3.1 must a proof violate? §1 answers it exactly
  (Lemma 1.1): near x(u) every class of p must have r-level above the agreement depth or an r-free modulus that does
  not divide p − 1. The two escape routes (a) "moduli → ∞" and (b) "other primes, not ≡ 1" of the brief coincide.

## 1. The escape lemma (PROVED, elementary)

**Lemma 1.1 (escape).** Let p be a prime and C = {n ≡ ρ (mod M)} an ET class containing p. For every prime r,
C contains x(p) (the r-generic point with u = p ∈ ℤ_r) iff M' | p − 1. Consequently:
(a) the ET classes of p with M' | p − 1 are exactly the boxes on the r-generic line containing u = p;
(b) if x(u) lies in no box of level ≤ L and p ≡ u (mod r^L), then every ET class of p has v_r(M) > L or M' ∤ p − 1,
i.e. its modulus has a prime power q^v ∥ M, q ≠ r, with q^v ∤ p − 1.
*Proof.* x(p) ≡ p (mod M_r) and x(p) ≡ 1 (mod M'); p ≡ ρ (mod M). So x(p) ∈ C iff ρ ≡ 1 (mod M') iff p ≡ 1 (mod M').
(b): if v_r(M) ≤ L and M' | p − 1 then x(u) ≡ p ≡ ρ (mod M), i.e. x(u) ∈ C, a box of level ≤ L. ∎
*Reading.* Define the *escape modulus* of a class of p as E(M, p) = ∏_{q^v ∥ M, q^v ∤ p−1} q^v (all q, r included).
E = 1 is impossible (C would contain the profinite square 1). Near a sterile point every class of p has E divisible
by r^{L+1} or by a prime power q^v ∤ p − 1, q ≠ r. If p ≡ 1 (mod lcm(1..B)) the latter forces q > B or v > v_q(p − 1).
So the only way out is moduli carrying a prime (power) at which p is locally *not* trivial: (a) and (b) of the brief
are the same route, and it is H-A (moving modulus).
