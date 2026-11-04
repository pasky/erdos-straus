# Z56_FAMDESIGN — designing a (★) sub-family with a big provable genus main term

Status: z56 lane FAMDESIGN (brief `z52bbriefs/z56_lanes.md` §3, common rules `z53_depth.md`). Internal, **checkpoint 1
skeleton** (to be completed). **ES is OPEN; nothing here proves or disproves ES or (★) at any infinite set of primes.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famdesign_*`, data
`data/z56/famdesign/`.

## 0. Setting and notation

p ≡ 1 (mod 4) prime. A (★) solution is (o, e, C) ∈ ℕ³ with o odd, e even, p = 4oeC − o − e; it gives the two ordered
pairs (u, B) = (o, e), (e, o) of FRONTIER §2.1, so R(p) = 2·#{solutions}. For a set 𝔊 of pairs (o, e) put
R_𝔊(p) := 2·#{solutions with (o, e) ∈ 𝔊} and M_𝔊(p) := the genus (order ≤ 2) part of R_𝔊, i.e. M_gen restricted to 𝔊
(every term ≥ 0). Log-coordinates a := log o/log p, b := log e/log p; the hyperbola is a + b < 1. Write e = 2^k e′, e′ odd.
Arithmetic types: **U** (Thm U's): o ≡ 1 (4) squarefree, k = 1, e′ squarefree; **S**: o squarefree (either class mod 4),
e′ squarefree, any k ≥ 1; **A**: all pairs. Mean densities (per unit log²-area, both orders, EVIDENCE/Assessment to be
checked in §2): U ≈ 1/π², A = 3/π² (so M₀ = (3/π²)·½ log²p = (3/(2π²))log²p).

## 1. Precise statements attacked (checkpoint)

**Target (i).** Find 𝔊 and the largest c with M_𝔊(p) ≥ (c − o(1)) log²p for all primes p ≡ 1 (4), unconditionally
(Thm-U type: Burgess / large sieve in free variables at fixed p).

**Corollary V1 (PROVED; immediate from the proof of `Z53_GENUSLVAL` Thm U).** Let ℛ₁(λ) := {(a, b) : a > λ,
b > (1 + a)/4, a + b < 1} with λ = 1/15, and 𝔊₁ := the U-type pairs with (a, b) ∈ ℛ₁(1/15). Then
M_𝔊₁(p) ≥ (64/(45π⁴) − o(1)) log²p ≈ 0.01460 log²p (Thm U: 2/(3π⁴) ≈ 0.00684).
*Proof.* Thm U's proof (§2.4–2.7 there) shows, for each rectangle (α₀, α₁] × (β, γ] satisfying (C1)–(C3) with margins,
that the U-type pairs with u ∈ (p^{α₀}, p^{α₁}], w ∈ (p^β, p^γ] contribute ≥ ((8/π⁴)(α₁ − α₀)(γ − β) − o(1)) log²p to M_gen
(its last display bounds the *subfamily* sum, all of whose terms are ≥ 0). Tile ℛ₁(1/15) from inside by finitely many
disjoint closed rectangles of total area ≥ area(ℛ₁(1/15)) − η: a thin rectangle [α₀, α₁] × [β, γ] ⊂ ℛ₁(1/15) satisfies
(C1) γ < 1 − α₁ and (C2) β > (1 + α₁)/4 as the closed rectangle lies inside the open region; (C3) α₀ > (1 + α₁)/16 holds
once α₁ − α₀ is small because α₀ > 1/15 ⟺ α₀ > (1 + α₀)/16. Disjoint rectangles give disjoint pair sets; sum the
lower bounds (finitely many o(1)'s), let η → 0 (r → ∞, ε → 0 as in Thm U). area(ℛ₁(1/15)) = ∫_{1/15}^{3/5}(3/4 − 5a/4)da
= 8/45. ∎ (Thm U optimised a single rectangle; the admissible set is the trapezoid.)

**Theorem V (to be proved in §3; the lane's main target).** Let G := {(a, b) : max(a, b) > (1 + min(a, b))/4, a + b < 1}
= ℛ₁ ∪ ℛ₂ (ℛ₂ the mirror of ℛ₁), i.e. "the larger entry exceeds (smaller entry · p)^{1/4}", and G_λ := G ∩ {min(a, b) > λ}.
For the S-type pairs in G_{1/15}: M ≥ ((16/π⁴)·(29/90) − o(1)) log²p ≈ 0.0529 log²p (Burgess only); in G_λ, any λ > 0
(Heath-Brown's quadratic large sieve for the average of L(1, χ)): (20/(3π⁴) − o(1)) log²p ≈ 0.0684 log²p.
area(G) = 5/12 of the full triangle's 1/2; the excluded *Burgess corner* {max(a, b) ≤ (1 + min(a, b))/4} (both entries
≲ p^{1/3}, C ≳ p^{1/3}) has area 1/12.
Needs: (a) the mirror slice (fix e, sum over o; characters mod 8·e′, discriminant of ℚ(√(−pe))); (b) o ≡ 3 (4), k ≥ 2.

**Why not closed.** Thm U (closed, §7.4) proves one rectangle of one arithmetic type; nothing in the closed list or
FRONTIER §6 concerns the *size* of the provable genus share. This lane is main-term engineering (B3): it does not touch
the order-≥3 remainder (B2) and cannot by itself give R_𝔊 ≥ 1. Its purpose is target (ii): a family where "R_𝔊 ≥ 1 for
all large p" has checkable content (CROSSF: the Thm U family's zero rate 39 % → 1.7 % at 10⁸ → 10¹⁵).

**First falsifier (to run).** Exhaustive enumeration of all (★) solutions per prime (engine
`scripts/z56_famdesign_scan.c`), classified into the families; zero rates of R_𝔊 at 10⁶–10¹³ against CROSSF's table
and the full (★) census (14 zeros ≤ 10¹⁰). Kill criterion: if R_𝔊 for the G-families still vanishes at a CROSSF-like
rate, the design is useless for (ii).

## 2. (to come) densities, ranked table
## 3. (to come) proof of Theorem V
## 4. (to come) scans
## 5. (to come) remainder structure, screens, verdict, FRONTIER text
