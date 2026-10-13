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

## 2. What the primes near a sterile point actually use (EVIDENCE; `scripts/ss_escape.py`)

Setup: r = 17, u = 5 (x(5) lies in no ET box of level ≤ 10: POINTWISE_MORDELL17D Comp 3.4, CERTIFIED). Q_B := lcm(1..B)
with the 17-part removed. Four populations of 30 random primes each, p ≈ max(10^16, 1000·Q_B·17^4):
A: p ≡ 1 (Q_B), p ≡ 5 (17^4) (near the sterile point x(5)); B: p ≡ 1 (Q_B·17^4) (near the profinite square 1, T1
control); C: p ≡ 1 (Q_B), p a random non-residue mod 17; D: random p ≡ 1 (24). For each p the script scans all ET
classes of modulus M ≤ 10^5 (own enumeration of the seven families, equal to `mordell_lib.residue_set` for
M ≤ 600; every reported witness re-solved at p by `mordell_lib.solve`), and records the Mordell height h(p) (least
modulus of a class containing p) and the least escape modulus E (Lemma 1.1). Every p of A–D lies in a class of
modulus ≤ 10^5. Medians (h, E):

| B | A (near x(5)) | B (near 1) | C (hard, non-sterile) | D (random) |
|---|---|---|---|---|
| 23 | 47, 37 | 79, 37 | 47, 17 | 7, 5 |
| 47 | 151, 67 | 159, 61 | 71, 17 | 11, 5 |
| 97 | 239, 127 | 239, 107 | 119, 17 | 11, 5 |

In A and B the escape modulus is (in all 180 cases) a single prime q > B, almost always one of the first few primes
after B (B = 97: q ∈ {101, …, 197}). In C, 70–80 % escape at q = 17 itself (a level-1 box of the cell).
*Reading (Assessment).* (i) Near the sterile point and near the square point 1 the primes behave identically: the
sterile point removes the r-boxes of level ≤ L and nothing else, and the primes escape at the **boundary**, the
first primes q at which p is locally non-trivial, with modest moduli (h ≈ 2.5B ≈ 2.5·log Q_B). No growing r-level
(k ≥ 5) and no "large" prime is ever needed. (ii) So the r-adic part of Thm 3.1 is not where the difficulty sits:
the escape is the ordinary H-A step "find the first prime where p is non-trivial and hit a covered cell there".
