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

## 3. The sterile set as a closed subset of Ẑ, and a Borel–Cantelli dichotomy for non-square patterns

Let U ⊂ Ẑ be the union of all ET classes (open) and S := Ẑ \ U (closed). For x ∈ Ẑ^× let
N(x) := {q odd prime : x_q is a non-square in ℤ_q^×} (the *non-square pattern*), and for a set T of odd primes let
G_T := {x ∈ Ẑ^× : x_q = 1 (q ∉ T), x_q non-square (q ∈ T)} (the T-generic non-square set; T = {r} is the
non-residue half of the r-generic line). ν_T := ⊗_{q∈T} (normalised Haar measure on the non-squares of ℤ_q^×) on G_T.

**Prop 3.1 (PROVED, relative to ET Props 1.3/1.4 and §10).** (a) For a prime p: ES(p) ⟺ p ∉ S.
(b) For odd n: n ∉ S ⟺ n has an ET N-point (a Type I or Type II parametrised solution). So CONJECTURE SQ
(odd n: Type I/II empty ⟺ n square) is the statement S ∩ ℕ_odd = {odd squares}; T1 is "Sq ∩ ℕ ⊂ S".
*Proof.* A class gives an N-point at every n ≥ 1 in it (POINTWISE_MORDELL §0). Conversely a Type II N-point (a,b,c,d)
of n lies in the II2 class (a, d, f = 4acd − 1) (f + 1 = 4acd, ef = n + 4a²d), and a Type I N-point in the I1 class
(a, d, f = 4acd − n) (f + n = 4acd, ef = 4a²d + 1); both conditions are exactly those of `mordell_lib`. For a prime p every
solution of 4/p is Type I or II (p cannot divide all three denominators, since then 4 = Σ 1/x_i' ≤ 3). ∎

**Prop 3.2 (divergent side; PROVED, elementary).** If Σ_{q ∈ T, q ≡ 3 (4)} 1/q = ∞, then ν_T-almost every point of G_T
lies in an ET class.
*Proof.* For q ≡ 3 (mod 4) the II2 class (a, d, f) = (1, 1, q) is {n ≡ −4 (mod q)} (4 | q + 1), and −4 is a non-residue
mod q. Under ν_T the events {x_q ≡ −4 (mod q)}, q ∈ T, are independent with probabilities 2/(q − 1). Second
Borel–Cantelli: a.s. infinitely many occur. ∎
(This is Mordell's shot "p + 4 has a prime factor ≡ 3 (mod 4)", read on the T-generic set.)

**Corollary 3.3.** For every odd non-square n, T(n) := N(n) \ {q | n} has Σ_{q∈T(n), q≡3(4)} 1/q = ∞ (Chebotarev: the
q ≡ 3 (4) with (n/q) = −1 have density 1/4 among primes, n not a square), so the T(n)-generic non-square set is
covered ν-almost everywhere. Integers are ν-null, so this says nothing about n itself (the profinite face of B6).

**Sparse side (Assessment, sketch only).** O178 Thm 3.1 is the case T = {r}: ν_{r}(S ∩ G_{r}) > 0 for r ≥ r₀.
The natural extension is: ν_T(S ∩ G_T) > 0 whenever min T ≥ r₀ and Σ_{q∈T} q^{−1/10+δ} is small; the union bound
goes through T-units F with box weight ≈ 2^{ω(F)} F^{−1/2} against f_II(F) ≪ F^{2/5+o(1)}, and an Euler product over T.
*Not proved here*: MORDELL17 Lemmas 1.1–2.3 are for one prime; with ≥ 2 primes in T the families I2, I3, II3 can split
the T-part between two of their moduli (mixed box types), which needs a new dictionary to solutions of 4/F.
With polylogarithmic counts (the truth, EVIDENCE: D_P, D_Q in MORDELL17B) the threshold would be
Σ_{q∈T} log³q/q < ∞.
*Reading (Assessment).* Non-square patterns split into a **convergent** regime (sterile points carry positive
ν_T-measure: proved for |T| = 1, expected for sparse T) and a **divergent** regime (ν_T-a.e. covered, Prop 3.2). Every
non-square integer sits in the divergent regime, and so do all primes. ES lives exactly on the divergent side of a
Borel–Cantelli dichotomy, at a ν-null point. Whether G_T ∩ S = ∅ for divergent T (a *finite* covering of G_T by
compactness) is open. Boxes whose T-part is a power of a single q ∈ T cut out a set A_q of x_q only, so their joint
uncovered set is ∏_{q∈T} A_q; if every A_q ≠ ∅ (e.g. all q ∈ T have a sterile point on their q-line, as for q ≥ r₀)
it is non-empty, and any covering of G_T must use solutions of 4/F with ≥ 2 primes of T in F. (For q = 13 the
whole non-residue half of the 13-line is covered at level 1, POINTWISE_MORDELL §1, by boxes of modulus 3·13 and 11·13; so A_13 = ∅ whenever 3, 11 ∉ T.)

## 4. Exponential families (goal 3; relative to EXPONENT_COVERING §1, O185)

Λ_k ⊂ Ẑ is the limit set of n_m = k·2^m + c (c = ±1): ν(μ)_2 = c, ν(μ)_q = k·2^μ + c (q odd), μ ∈ Ẑ.
**Lemma 4.1 (PROVED, elementary).** Λ_k meets no r-generic line {x_q = 1 for q ≠ r}, for any r, k, c.
*Proof.* If c = −1 the 2-component is −1 ≠ 1. If c = +1, x_q = 1 forces k·2^μ = 0 in the domain ℤ_q, impossible. ∎
So the O178 sterile points are invisible to exponential families: they neither obstruct nor are reached by
exponent coverings. Sterile points of Λ_k (O185 Thm 1.2) must be found inside Λ_k itself.
**Lemma 4.2 (why the O178 mechanism does not transfer; PROVED, elementary).** Push Haar measure on μ ∈ Ẑ forward to
Λ_k. An ET class with modulus 2^s M' (M' odd, gcd(k, M') = 1, s ≤ the 2-adic compatibility) has measure 0 or
1/ord_{M'}(2), not 1/M'. *Proof.* μ ↦ 2^μ mod M' is the uniform measure on the cyclic group ⟨2⟩ of order
ord_{M'}(2), and k·g + c ≡ ρ (mod M') has at most one solution g. ∎
Since ord_{M'}(2) can be as small as log₂ M' (M' | 2^L − 1), classes of huge modulus carry large measure on Λ_k. The
O178 union bound (weights 1/M against ET counts ≪ M^{2/5+o(1)} at half level) has no analogue: on Λ_k the weights are
1/ord, and Sierpiński-type finite coverings become possible, as O185 found for k = 9 and 27. *Steering (Assessment).*
The convergent-measure mechanism that produces sterile points needs moduli to carry mass ≍ 1/M, i.e. a parameter
space on which every prime coordinate moves independently (a line, or G_T of §3). Families whose residues are
coupled across primes through one exponent (Λ_k) or one integer (ℤ ⊂ Ẑ) escape it, and that coupling is exactly
what such families and ES itself have, and what sterile points lack.

## 5. Infinitely many shots: what sterile points measure (goal 4; relative to T1_TEMPLATE §1, O183, CLAIMED)

The O183 golden variant V_φ (O = ℤ[φ], η_k = φ^{2k+1}) succeeds at n via a shot k: a_k = n + 4η_k has a prime 𝔮 with
(n/𝔮) = −1. Read on the 𝔮-generic line (x ≡ 1 at every other prime) a shot is the class x ≡ −4η_k (mod 𝔮), 𝔮 with
χ_{−φ}(𝔮) = −1 (then −4η_k is a non-square mod 𝔮, and the classes for all k cover the coset −4φ·⟨φ²⟩).

**Prop 5.1 (level-1 coverage per prime; PROVED relative to ET Prop 1.7 (f(q) ≪ q^{3/5+o(1)} for primes q) and
MORDELL17 Lemmas 1.1–2.3, 1.3 for general r, as used in DEPTH_ASPECT §3).**
(a) ℤ (ET classes): the q-level-1 boxes on the q-generic line cover a fraction ≤ (6f(q) + 2f_II(q))/q
≪ q^{−2/5+o(1)} of ℤ_q^× (P-boxes need odd ES level, so K = 2 contributes nothing; K = 1 gives f_II(q) ≤ f(q) boxes).
(b) V_φ (unit shots): at every prime 𝔮 with χ_{−φ}(𝔮) = −1 the shot classes cover the fraction 1/i_𝔮 of the
non-squares mod 𝔮, i_𝔮 = [(O/𝔮)^{×2} : ⟨φ²⟩]. *Proof of (b).* −4φ^{2k+1} ranges over −4φ⟨φ²⟩, a coset of ⟨φ²⟩
inside the non-squares (−φ a non-square, 4φ^{2k} a square). ∎
*Reading (Assessment).* In V_φ, i_𝔮 = 1 for a positive proportion of 𝔮 under GRH (Artin for φ), and unconditionally
Σ 1/i_𝔮 = ∞ (ord_𝔮 φ ≥ N𝔮^{1/2} for almost all 𝔮, Erdős–Murty type). So in V_φ every infinite non-square pattern
is in the divergent regime of §3, and the analogue of an O178 sterile point (a sparse-pattern sterile point) cannot
exist on lines through primes with i_𝔮 = 1: the line is fully covered at level 1. Over ℤ the per-prime coverage is
≪ q^{−2/5+o(1)} (truth ≈ log³q/q), and O178 turns this summability into sterile points. **The O178 sterile points
are exactly the profinite signature of "finitely many shots":** a ℤ-mechanism with infinitely many shots in the V_φ
sense would need, at a positive proportion of primes q, families of classes of q-level 1 covering ≫ 1 of the
non-residues mod q. ET classes cannot (Prop 5.1(a)), because over ℤ the shot modulus 4ad grows with the shot (a²d is
not a unit); the unique ℤ-shot with bounded modulus 4 is Mordell's p + 4. This is O183's spark S4 made precise at
the level of per-prime coverage.

## 6. Making r₀ explicit (goal 2): what a computer-assisted proof at moderate r would need (Assessment)

The P-tail is the only critical term. Suppose an explicit bound D_P(K) ≤ C·r^{2K/5} for odd K ≥ K₁ (D_P = Type II
N-points of 4/r^K with r ∤ cd, MORDELL17 §4) and that ≈ 0.45 of the non-residue mass is left for it (the Q/U part and
the exact census below K₁ eating the rest). The admissible constant C_adm(r, K₁) = 0.45 / Σ_{K≥K₁ odd} 2r^{2K/5−(K+1)/2}:

| r | 17 | 101 | 1009 | 10007 | 10⁶+3 | 10⁹+7 |
|---|---|---|---|---|---|---|
| K₁ = 1 (no census) | 0.53 | 2.2 | 10.7 | 48 | 839 | 5.6·10⁴ |
| K₁ = 7 (census K ≤ 5) | 2.9 | 34 | 678 | 1.2·10⁴ | 3.3·10⁶ | 1.4·10¹⁰ |

(C_adm ≈ r^{0.1K₁+0.1}.) What is available: ET's proof gives D_P(K) ≤ r^{K(2/5 + c/log log r^K)} with τ-type losses.
With Nicolas–Robin, τ(m) ≤ m^{1.0661/log log m}, so every τ factor costs r^{K·1.07/log(K log r)}. This loss
is below the margin 1/10 only once log log r ≳ 10·(number of τ factors in ET's casework). That is
r₀ ≈ exp(exp(30–60)): explicit, but doubly exponential, matching DEPTH_ASPECT Remark (2).
The table shows that the requirement weakens polynomially in r, while the available bound has a loss that is
superpolynomial at every computable scale. So **no computer-assisted proof at r = 101 or 10⁹ is possible without a new
explicit count of Type II solutions of 4/r^K with no divisor-function loss**, the bottleneck already isolated at
r = 17 (MORDELL17B–D). The true counts are polylogarithmic (D_P(13) = 1463 at r = 17), so the gap is in the method,
not the arithmetic. Averaging over r does not help pointwise in r. It would give "sterile points for almost all r in
[R, 2R]" only via uniform averages of τ(A r^K + 1) over r with K unbounded, which are not available either.
