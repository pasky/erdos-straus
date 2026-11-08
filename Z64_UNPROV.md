# Z64_UNPROV — can unprovability of ES be proved? Verdict: strengthened (logic). Square classes are unprovable in normal open induction (+GCD); PA/ZFC independence is not a realistic target; no HOT LEAD

Status: z64 lane UNPROV (brief `z52bbriefs/z64_lanes.md` §UNPROV; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES, (MS), or any case of them.** Internal, unrefereed.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z64_unprov_*`,
data `data/z64/unprov/`. Primary source for the model: Berarducci–Otero, *A recursive nonstandard model of normal open
induction*, JSL 61 (1996) 1228–1241 (author PDF archived as `data/z64/unprov/berarducci_otero_1996_recNOI.pdf`, read in
full; cited below as BO with their lemma/theorem numbers).

**Headline (PROVED, relative to BO Thm 1.1 (Shepherdson), Lemmas 2.3, 2.4, 2.6–2.9, 4.1, the stage Claim and Thm 4.2, and ET Prop 1.6).** *For every primitive residue class r mod q that is
a unit square mod q, normal open induction does not prove "ES holds at every prime ≡ r (mod q)"*. This stays true after
adding gcds, "every element has an irreducible divisor", and all true universal ring sentences about ℤ (Thms A′, A″). Together with
Mordell's identities this decides open-induction provability class by class mod 840: IOpen proves ES on every class
outside 𝔐 = {1, 121, 169, 289, 361, 529}, and normal IOpen proves it at primes of no class in 𝔐. It also answers the
open question of `Z58_LOGIC.md` §6.1: IOpen ⊬ (MS★) and IOpen ⊬ (MS). The counterexamples are infinite *primes* whose
residue in Ẑ is a square-mimicking unit; the proof transfers the odd-square obstruction T1 (ET Prop 1.6) into the model by
an analytic interpolation argument. No Hypothesis H is used (metaphorically, the model's generic primes play H's role).

## 0. Falsifier table (mandatory)

This lane proves *non-provability* theorems, not positivity. The table records how they interact with the screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | The mechanism *is* F1. The unprovability theorem (Thm A) is T1 (ET Prop 1.6 / Z57_SYNTH Lemma A.1(b)) imported into a model: any hypothetical ES solution at the model prime specialises to a Type I/II solution at an odd square ℓ². So the result covers exactly the residue classes that contain unit squares, and Thm B shows that the remaining classes mod 840 are IOpen-provable. Reading: a proof of ES must use, at an identifiable step, a principle false in the model M_{q*}. Candidates are Bezout-level divisor arithmetic, counting, or reciprocity for non-standard moduli. Open induction, normality, gcds, residue information, "every element has an irreducible divisor" and all true universal ring facts about ℤ (§§2.6–2.8) are not enough. |
| **F2 C-even sub-line** | Thm A transfers verbatim to R₈ and every (★)-sub-line, since R₈(m²) ≤ R(m²) = 0. Nothing here distinguishes C odd from C even. Nothing here is falsified by F2 either: no positivity is claimed. |
| **F3 composites** | The model counterexamples are *primes* of the model (proved directly in (F1), §2.2). For (MS★) primality is not even used (§2.5): every polynomial generator γ (§2.5 Remark) with positive leading coefficient and square-mimicking residue fails, provided the other generators of the system have ϕ(γ_j) ∈ Ẑ (the Remark's condition (2)). This is consistent with F3: by `Z58_LOGIC` Thm 6.2, composite-shaped counterexamples already exist in Shepherdson's model. |
| **F4 known zeros** | The counterexamples sit over profinite square points, not over the 14 (★)-zero primes. No positivity is claimed, so F4 cannot falsify anything here. A proof of ES in a stronger theory is not touched. |

No HOT LEAD (this is a logic lane; see §8 verdict).

## 1. Precise statements

Language L_or = {0, 1, +, −, ·, ≤}. Following BO §1:
* **OI** (open induction) is the theory of discretely ordered rings with the open-induction schema on the non-negative
  part. The non-negative part of a model of OI is a model of IOpen and conversely, so "OI ⊬ φ" for a sentence φ about
  non-negative elements is "IOpen ⊬ φ".
* **NOI** is OI + normality (integral closure in the fraction field, BO axiom N). IE₁ ⊢ NOI (BO §1).
* **Shepherdson's criterion** (BO Thm 1.1): an ordered domain is a model of OI iff it is an integral part of the real
  closure of its fraction field.

Formulas (all quantifiers over non-negative elements):
* ES(n) :≡ ∃x, y, z ≥ 1 (4xyz = n(xy + yz + zx)).
* ES★(n) :≡ ∃u, B, C ≥ 1 (4uBC − u − B = n)   ((★) of Z57_SYNTH; R(n) ≥ 1 in ℕ).
* Prime(n) :≡ n ≥ 2 ∧ ∀a, b (ab = n → a = 1 ∨ b = 1).
* Cl_{r,q}(n) :≡ ∃k (n = qk + r), for standard numerals q ≥ 1, 0 ≤ r < q.
* **ES_prime[r mod q]** :≡ ∀n (Prime(n) ∧ Cl_{r,q}(n) → ES(n)); **ES[r mod q]** :≡ ∀n ≥ 2 (Cl_{r,q}(n) → ES(n)).
* (MS★), (MS): as in `Z58_LOGIC.md` §1, §6.1 (Mord(n) :≡ n > 10¹⁷ ∧ n mod 840 ∈ 𝔐).

A class r mod q is **primitive** if gcd(r, q) = 1, and a **unit square** if r ≡ s² (mod q) for some s with
gcd(s, q) = 1. A unit q* ∈ Ẑ^× is **square-mimicking** if q* ∈ (Ẑ^×)². Equivalently, for every D ≥ 1 there is an
integer s, gcd(s, D) = 1, with s² ≡ q* (mod D). Every unit-square class r mod q contains such a q*: choose s′ ∈ Ẑ^×
with s′ ≡ s modulo the q-part and put q* := s′².

Solvable by polynomials (ET p. 7–8, J. Aust. Math. Soc. 94 (2013); `sources/elsholtz-tao-1107.1010.pdf`): a primitive class
r mod q is solvable by polynomials if there are P₁, P₂, P₃ ∈ ℚ[n], taking positive integer values for all sufficiently
large n ≡ r (mod q), with 4/n = 1/P₁ + 1/P₂ + 1/P₃ identically.

## 2. Theorem A: square classes are not provable in normal open induction

**Theorem A (PROVED, relative to BO Thm 1.1 (Shepherdson), Lemmas 2.3, 2.4, 2.6–2.9, 4.1, the stage Claim and Thm 4.2 (Lemma 2.8 via van den Dries
[D2], Lemma 2.9 via Bourbaki), and ET Prop 1.6 / Z57_SYNTH Lemma A.1(b); primality is proved directly in (F1), so BO
Thm 4.3 is not used).** Let q* ∈ (Ẑ^×)². There
is a model M = M_{q*} ⊨ NOI and an infinite positive prime element n ∈ M with the following properties:
* (i) n ≡ r (mod m) in M whenever r ≡ q* (mod m) (all standard m);
* (ii) M ⊨ ¬ES(n);
* (iii) M ⊨ ¬ES★(n).

**Corollary A.1 (PROVED, same reliance).**
* (a) For every primitive unit-square class r mod q: NOI ⊬ ES_prime[r mod q]; a fortiori IOpen ⊬ ES_prime[r mod q].
* (b) NOI ⊬ (MS★) and NOI ⊬ (MS). (Take q* ≡ 1 (mod 840). The Hit form follows by `Z58_LOGIC` Remark 6.3, valid in any
  model of IOpen.) This answers the "Open" item of `Z58_LOGIC.md` §6.1 and of `BRAINSTORM/logic_weak_arithmetic.md` §5.
* (c) For q* = 1 the counterexample is ≡ 1 modulo every standard m: the "formal point 1" of B1 realised by a *prime*.

### 2.1 The model (BO's construction with residue q*)

* Fix BO's recursive real closed field K ⊂ ℝ with algebraically independent π₁, π₂, … (BO §3). Let x be a positive
  infinite indeterminate. K[x^ℚ] denotes Puiseux polynomials Σ a_j x^{j/k} (a_j ∈ K); K[x^ℚ]• those without constant term.
  Ordering: f > 0 iff the leading coefficient is positive. Equivalently, since K ⊂ ℝ, f > 0 iff the real function
  ξ ↦ f(ξ) is positive for all large real ξ.
* BO §4 construct β_i = p_i(x) + π_i with p_i ∈ K_{i−1}[x^ℚ]•, where p_{i} is the first element (in a fixed enumeration of
  K[x^ℚ]•) lying in K_{i−1}[x^ℚ] and at infinite distance from M_{i−1}. We fix the enumeration to begin with x, so that
  p₁ = x and β₁ = x + π₁. The β_i are algebraically independent over ℚ (BO Lemma 4.1).
* BO use the ring homomorphism ϕ with ϕ(β_i) = 1. We use ϕ: ℚ[β₁, β₂, …] → 𝔸_f = ℚ ⊗ Ẑ with **ϕ(β_i) = q*** for all i,
  and put M_i := (M_{i−1}[β_i])_ϕ, M := ∪ M_i. By BO Lemma 2.7, L_ϕ = {a/k : a ∈ L, k | ϕ(a)}. Unwinding this gives
  > **M = {g ∈ ℚ[β₁, β₂, …] : ϕ(g) ∈ Ẑ}.**
  (If g = h/k with h ∈ ℤ[β] and ϕ(g) ∈ Ẑ then k | ϕ(h); the converse is clear.)
* BO's proofs of Thm 4.2 (M ⊨ NOI) and Thm 4.3 (the β_i are prime) use ϕ only through Lemmas 2.7, 2.8 and 2.10. These
  are stated for an arbitrary ring homomorphism ϕ: L → Ẑ (2.10 requires ϕ(p) ∈ Ẑ^×, true here since q* is a unit).
  The integral-part argument, and the choice of the p_i, do not involve ϕ: by BO Lemma 2.4, distance to M_n equals distance
  to ℚM_n = ℚ[β₁..β_n]. Hence **M ⊨ NOI**. (Recursiveness, BO Thm 4.4, is not needed. For q* = 1 the model is BO's model for an enumeration beginning with x. Whether BO's
  recursiveness proof extends to computable q* ≠ 1 is plausible but not checked.)

### 2.2 Elementary facts about M (PROVED)

* (F1) *n := β₁ is a positive infinite prime of M with ϕ(n) = q*.* Primality, directly: if gh = n·w with g, h, w ∈ M, then
  in the UFD ℚ[β] the variable β₁ divides g (say); g′ := g/β₁ has ϕ(g′) = ϕ(g)/q* ∈ Ẑ, so g′ ∈ M and n | g in M. Also
  n is not a unit, since 1/β₁ ∉ ℚ[β]. A prime of a domain is irreducible, and the units of M are ±1 (a unit is a constant
  c ∈ ℚ with c, 1/c ∈ Ẑ), so M ⊨ Prime(n).
* (F2) *Residues.* If r ≡ q* (mod m) then (n − r)/m ∈ M, since ϕ((n − r)/m) = (q* − r)/m ∈ Ẑ. So n ≡ r (mod m) in M.
* (F3) *Divisibility by n is the polynomial one.* For g ∈ M: n | g in M ⟺ β₁ | g in ℚ[β] (as in F1).
* (F4) *Integer specialisation.* Let G ⊂ M be finite, involving only β₁..β_k. There is D ≥ 1 such that every b ∈ ℤ^k with
  b_i ≡ q* (mod D) for all i satisfies g(b) ∈ ℤ for all g ∈ G.
  *Proof.* Let D₀ be a common denominator of all coefficients and put D := D₀. For g ∈ G, g(b) − ϕ(g) is a sum of terms
  c_α(b^α − q*^{|α|}) with D₀c_α ∈ ℤ, and b^α − q*^{|α|} ∈ DẐ. So g(b) ∈ ϕ(g) + Ẑ = Ẑ; also g(b) ∈ ℚ, and ℚ ∩ Ẑ = ℤ. ∎

### 2.3 Analytic interpolation (PROVED)

**Lemma 2.3.** Let k ≥ 1 and b ∈ ℤ^k with b₁ ≥ 1. There are an open interval I ⊃ [0, ∞) and a ring homomorphism
ψ: ℚ[B₁..B_k] → C^ω(I) (real-analytic functions; B_i ↦ β_i identifies ℚ[B] with ℚ[β₁..β_k]) such that:
* (a) ψ(g)(0) = g(b) for all g;
* (b) if g ≠ 0 then ψ(g) ≢ 0, and ψ(g)(s) has the sign of g in M for all sufficiently large s;
* (c) ψ(β₁)(s) > 0 for all s ≥ 0.

*Proof.* Choose a real T > max(0, −π₁), so that T + π₁ > 0, and define
> ψ(B_i)(s) := p_i(T + s) + π_i + (b_i − π_i − p_i(T))·e^{−s}.
Each p_i(ξ) = Σ a_j ξ^{j/k} is real-analytic for ξ > 0, so ψ(B_i) is real-analytic on I := (−T, ∞). Extend ψ to ℚ[B]
by substitution; it is a ring homomorphism.
* (a) p_i(T) + π_i + b_i − π_i − p_i(T) = b_i.
* (b) Put Γ_i(ξ) := p_i(ξ) + π_i and Δ_i(s) := (b_i − π_i − p_i(T))e^{−s}. By Taylor's formula
  ψ(g)(s) − g(Γ(T + s)) = Σ_{0<|α|≤deg g} (∂^α g)(Γ(T + s))·Δ(s)^α/α!. Here |Γ_i(ξ)| = O(ξ^E), and |Δ(s)^α| = O(e^{−s}) for
  |α| ≥ 1, s ≥ 0. So the difference is O((1 + s)^{E′}e^{−s}) → 0. Since the β_i are algebraically independent over ℚ
  (BO Lemma 4.1), g(Γ(ξ)) is a nonzero real Puiseux polynomial in ξ. Hence either |g(Γ(ξ))| → ∞, or it is a nonzero
  constant. Its sign for large ξ is the sign of its leading coefficient, which is the sign of g in M. So ψ(g)(s) is
  eventually nonzero with that sign.
* (c) p₁(ξ) = ξ, so ψ(β₁)(s) = s + (T + π₁)(1 − e^{−s}) + b₁e^{−s} > 0 for s ≥ 0. ∎

### 2.4 Positivity propagation (PROVED)

**Lemma 2.4.** Let F₁, F₂, F₃, N ∈ C^ω(I), I ⊃ [0, ∞). Suppose each F_i ≢ 0 and is positive for large s, N > 0 on [0, ∞),
and 4F₁F₂F₃ = N(F₁F₂ + F₂F₃ + F₃F₁) on I. Then F_i(s) > 0 for all s ∈ [0, ∞).
The same holds for (u, B, C) with 4uBC − u − B = N.

*Proof.* Each F_i has finitely many zeros in [0, ∞): none beyond some S, and finitely many in [0, S] by the identity
theorem. Suppose F₁F₂F₃ has a zero in [0, ∞), and let ρ be the largest. On (ρ, ∞) no F_i vanishes and each is eventually
positive, so all are positive there (IVT). On (ρ, ρ + ε) we may divide: 1/F₁ + 1/F₂ + 1/F₃ = 4/N. The right side is
bounded near ρ, since N(ρ) > 0. On the left, every term is positive, and the term with F_i(ρ) = 0 tends to +∞ as s ↓ ρ.
Contradiction. So no F_i vanishes on [0, ∞), and by the IVT all are positive there.
(★)-form: at the largest zero ρ of uBC all three are ≥ 0. If C(ρ) = 0 then −u(ρ) − B(ρ) = N(ρ) > 0, which is
impossible. If u(ρ) = 0 then −B(ρ) = N(ρ) > 0, also impossible; B(ρ) = 0 is symmetric. (This is `Z58_LOGIC` Lemma 6.1
for analytic functions.) ∎

### 2.5 Proof of Theorem A

(i) is (F2). Suppose (ii) fails: X, Y, Z ∈ M, X, Y, Z ≥ 1, with 4XYZ = n(XY + YZ + ZX). All of them lie in
ℚ[β₁..β_k] for some k.
* *Type split.* β₁ is prime in the UFD ℚ[β] and divides 4XYZ, so it divides at least one of X, Y, Z. It does not divide
  all three. Otherwise X′ = X/n, Y′, Z′ ∈ M by (F3), they are positive, hence ≥ 1 in the discrete ring M, and
  4X′Y′Z′ = X′Y′ + Y′Z′ + Z′X′ gives 4 = 1/X′ + 1/Y′ + 1/Z′ ≤ 3. By symmetry there are two cases:
  * Type I: β₁ | X, β₁ ∤ Y, β₁ ∤ Z;
  * Type II: β₁ | Y, Z, β₁ ∤ X.
* *Type I.* Put X₁ := X/n ∈ M, and let D be given by (F4) for G = {X, Y, Z, X₁}; enlarge D to a multiple of 8.
  * Y₀ := Y(0, B₂, …, B_k) and Z₀ := Z(0, B₂, …) are nonzero polynomials, since β₁ ∤ Y, Z. A nonzero polynomial does not
    vanish on a whole coset of Dℤ^{k−1}. So pick b′ ∈ ℤ^{k−1}, b′_i ≡ q* (mod D), with Y₀(b′)Z₀(b′) ≠ 0.
  * Let P be the finite set of primes dividing the numerator of Y₀(b′)Z₀(b′) or any denominator of a coefficient of Y
    or Z. Pick s₀ ∈ ℤ with s₀² ≡ q* (mod D), gcd(s₀, D) = 1 (q* is square-mimicking). By CRT choose ℓ ≥ 1 with
    ℓ ≡ s₀ (mod D) and ℓ ≡ 1 (mod r) for every r ∈ P with r ∤ D. Then ℓ is odd and coprime to every r ∈ P.
  * Set b := (ℓ², b′). Then b_i ≡ q* (mod D), so X(b), Y(b), Z(b), X₁(b) ∈ ℤ, and X(b) = ℓ²X₁(b).
  * Apply Lemma 2.3 to b (b₁ = ℓ² ≥ 1) and Lemma 2.4 to F = (ψX, ψY, ψZ), N = ψ(n). The F_i are eventually positive by
    2.3(b), and N > 0 on [0, ∞) by 2.3(c). So x₀ := X(b), y₀ := Y(b), z₀ := Z(b) are positive integers with
    4/ℓ² = 1/x₀ + 1/y₀ + 1/z₀.
  * For a prime r | ℓ we have r ∉ P, so Y has r-integral coefficients and Y(b) ≡ Y₀(b′) ≢ 0 (mod r). Hence
    gcd(ℓ², y₀) = 1, and likewise gcd(ℓ², z₀) = 1, while ℓ² | x₀.
  * So (x₀, y₀, z₀) is a Type I solution for the odd square ℓ², contradicting ET Prop 1.6 (f_I(m²) = 0 for odd m).
* *Type II.* The same, with X in the role of Y, Z: take G = {X, Y, Z, Y/n, Z/n} in (F4) and choose b′ with X(0, b′) ≠ 0
  and ℓ coprime to the numerator of X(0, b′). It yields a Type II solution for ℓ²,
  contradicting ET Prop 1.6 (f_II(m²) = 0).
* (iii): suppose u, B, C ∈ M are ≥ 1 with 4uBC − u − B = n. Take D from (F4) for {u, B, C}, any odd s ≡ s₀ (mod D),
  and b = (s², b′) with b′_i ≡ q* (mod D). Lemmas 2.3 and 2.4 ((★)-form) give positive integers u(b), B(b), C(b) with
  4u(b)B(b)C(b) − u(b) − B(b) = s². This contradicts R(s²) = 0 (T1; Z57_SYNTH Lemma A.1(b)). No primality is used here. ∎

*Remarks.*
* ET Prop 1.6 is used only in its Diophantine content: the proof (ET §4) uses only the equations (2.1)–(2.2)
  (resp. (2.13)–(2.14)) of the Type I/II parametrisation together with Jacobi-symbol reciprocity. The parametrisation is
  ET Prop 2.2/2.6 for natural-number solutions, and we apply it only to the integer solution (x₀, y₀, z₀).
* *Any polynomial generator works (PROVED).* The proof uses n = β₁ only through three properties. (1) n is one of a
  system of algebraically independent polynomial generators γ₁ = n, γ₂, …, γ_k with ℚ[γ₁..γ_k] = ℚ[β₁..β_k]. (2) ϕ(n)
  ∈ (Ẑ^×)², and ϕ(γ_j) ∈ Ẑ for all j. (3) n > 0 in M. Lemma 2.3 holds verbatim for such generators, with
  ψ(γ_j)(s) := Γ_j(T + s) + (b_j − Γ_j(T))e^{−s}, where Γ_j(ξ) is γ_j read as a real Puiseux polynomial (constant term
  included). For (c), take T beyond the last zero of Γ₁′ and of Γ₁: then ψ(γ₁)(s) = [Γ₁(T + s) − Γ₁(T)] +
  Γ₁(T)(1 − e^{−s}) + b₁e^{−s} > 0.
* *Cofinal counterexamples (PROVED).* For m ≥ 1 put f_m := β₁ + (β₂ − β₃)²β₂^{2m}. It is linear in β₁, so (f_m, β₂, β₃, …)
  is a polynomial generator system of ℚ[β]. Also ϕ(f_m) = q*, f_m > 0 in M, and f_m is prime by the argument of (F1).
  So M ⊨ ¬ES(f_m) ∧ ¬ES★(f_m), with f_m ≡ q*. The f_m are unbounded, since β₂ is infinite and β₂ ≠ β₃. In particular M
  has cofinal primes.
* β_i with negative leading coefficient give the positive prime −β_i of residue
  −q* ≡ 3 (mod 4); there ES is IOpen-provable (Thm B), consistent with the theorem.

### 2.6 What else holds in M_{q*} (PROVED)

* *Every element ≥ 2 has an irreducible divisor (PD).* Let g ∈ M, g ≥ 2.
  * If ϕ(g) ∉ Ẑ^×, some standard prime ℓ has ϕ(g) ≡ 0 at ℓ, so g/ℓ ∈ M, and ℓ is irreducible in M (a factorisation of
    ℓ consists of constants in M ∩ ℚ = ℤ).
  * If ϕ(g) ∈ Ẑ^×, then g is nonconstant. Take an irreducible factor f of g in ℚ[β]. Each component of ϕ(f) is nonzero,
    and ϕ(f) is an ℓ-adic unit for almost all ℓ, so ϕ(f) ∈ 𝔸_f^× = ℚ^×·Ẑ^×. Choose c ∈ ℚ^× with ϕ(cf) ∈ Ẑ^×. Then
    cf ∈ M divides g in M, and cf is irreducible in M (a factor of it is a constant in ℤ whose ϕ-image is a unit, so it is
    ±1).
  So **NOI + PD + "primes are unbounded" ⊬ ES_prime[r mod q]** for unit-square classes. Descent to prime factors does not
  help.
* *Bezout fails:* β₁, β₂ have gcd 1 in M (a common divisor is a constant c ∈ ℤ dividing ϕ(β₁) = q*, a unit), but no
  Bezout identity: uβ₁ + vβ₂ has no constant term in ℚ[β], so it is never 1. So M ⊭ IE₁ (Smith 1992 abstract, verified
  in `lit_models.md` §6: IE₁ ⊢ IOpen + Bez).
* *GCD fails in M_{q*}* when all ϕ(β_i) are equal. β₁ − β₂ and β₁ − β₃ have ϕ = 0, so both are divisible by every
  standard integer. They are coprime in ℚ[β], so their common divisors in M are exactly the nonzero integers, and there
  is no greatest one. §2.7 repairs this with generic residues.

### 2.7 The GCD strengthening (PROVED)

**Theorem A′.** For every primitive unit-square class r mod q there is a model M ⊨ NOI + GCD + PD (every pair of
elements has a gcd; every element ≥ 2 has an irreducible divisor). It contains an infinite
prime n ≡ r (mod q) with M ⊨ ¬ES(n) ∧ ¬ES★(n). Hence **IOpen + GCD + PD ⊬ ES_prime[r mod q]**. (Prior art for the model side: Mohsenipour 2006 built a recursive
model of IOpen + GCD with cofinal primes, `lit_models.md` §3; we do not use it, since its construction was not accessible.) In particular the Type I/II
reduction, which needs only gcds, is available inside M and does not help.

*Construction.* As in §2.1, but with ϕ(β_i) := a_i for a sequence a = (a_i) ∈ Ẑ^ℕ such that
* a₁ ∈ (Ẑ^×)², a₁ ≡ r (mod q);
* (G1) for every prime ℓ the ℓ-components (a_{i,ℓ})_i ∈ ℤ_ℓ are algebraically independent over ℚ;
* (G2) for every k and every pair f, g ∈ ℤ[B₁..B_k] coprime in ℚ[B], only finitely many ℓ satisfy ℓ | f(a_ℓ) and
  ℓ | g(a_ℓ), where a_ℓ := (a_{1,ℓ}, …, a_{k,ℓ}).
M := {g ∈ ℚ[β] : ϕ(g) ∈ Ẑ} ⊨ NOI as in §2.1. β₁ is prime, ϕ(β₁) = a₁ is a unit (F1), and the proof of §2.5 runs
verbatim with "b_i ≡ q* (mod D)" replaced by "b_i ≡ a_i (mod D)" and s₀² ≡ a₁ (mod D).

*Existence of a (measure argument).* Take a₁ Haar-random in the open subset {a₁ ≡ r (mod q)} of (Ẑ^×)², and a_i
(i ≥ 2) Haar-random in Ẑ, all independent. The ℓ-components are independent across ℓ. For ℓ ∤ 2q, a_{1,ℓ} mod ℓ is
uniform on the nonzero squares of 𝔽_ℓ, so every point of 𝔽_ℓ^k has probability ≤ 3/ℓ^k under a_ℓ mod ℓ.
* (G1): the zero set in ℤ_ℓ^k of a nonzero polynomial is Haar-null (Fubini over the last variable), and there are
  countably many polynomials and primes.
* (G2): by the point-count lemma below, P(ℓ | f(a_ℓ), ℓ | g(a_ℓ)) ≤ 3·#V_ℓ/ℓ^k ≤ 3C/ℓ² for ℓ ≥ ℓ₀. Since Σ_ℓ ℓ^{−2} < ∞,
  Borel–Cantelli gives finitely many such ℓ almost surely. There are countably many pairs.

*Point-count lemma.* Let f, g ∈ ℤ[B₁..B_k] be nonconstant and coprime in ℚ[B]. Then there are C, ℓ₀ such that
#V_ℓ := #{x ∈ 𝔽_ℓ^k : f(x) ≡ g(x) ≡ 0} ≤ Cℓ^{k−2} for all primes ℓ ≥ ℓ₀. (If one of them is a nonzero constant c,
V_ℓ = ∅ for ℓ ∤ c.)
*Proof.*
* Choose a primitive v ∈ ℤ^k with f_top(v) ≠ 0 (f_top = top-degree form) and A ∈ SL_k(ℤ) with Ae₁ = v. Substituting
  B ↦ AB preserves coprimality and all counts #V_ℓ. Afterwards f = c_f B₁^{deg f} + (lower in B₁), with c_f ∈ ℤ∖{0}.
* f is then primitive as a polynomial in B₁ over ℚ[B₂..B_k]. So (Gauss) f and g are coprime in ℚ(B₂..B_k)[B₁], and
  Res := Res_{B₁}(f, g) ∈ ℤ[B₂..B_k] is nonzero. Write Res = Uf + Wg with U, W ∈ ℤ[B].
* For ℓ ∤ c_f·cont(Res): a common zero x mod ℓ has Res(x₂..x_k) ≡ 0.
  * By Schwartz–Zippel this leaves ≤ deg(Res)·ℓ^{k−2} choices of (x₂..x_k).
  * For each of them, f(·, x₂..x_k) mod ℓ has leading coefficient c_f ≢ 0, so ≤ deg f roots x₁.
* Hence #V_ℓ ≤ deg f·deg Res·ℓ^{k−2}. ∎

*GCD in M.* Let ϕ_ℓ be the ℓ-component of ϕ and v_ℓ(h) := ord_ℓ ϕ_ℓ(h) for h ∈ ℚ[β]∖0. This is finite by (G1), and
additive. Then h ∈ M ⟺ v_ℓ(h) ≥ 0 for all ℓ.
* Given g, h ∈ M∖0, let G := gcd_{ℚ[β]}(g, h), with g = Gg₁, h = Gh₁ and g₁, h₁ coprime.
* m_ℓ := min(v_ℓ(g₁), v_ℓ(h₁)) is 0 for almost all ℓ. Write g₁ = λg₁′, h₁ = μh₁′ with g₁′, h₁′ primitive in ℤ[β].
  For ℓ ∤ λμ (numerators and denominators), m_ℓ > 0 iff ℓ | g₁′(a_ℓ) and ℓ | h₁′(a_ℓ), which happens finitely often by (G2).
* Put d := cG with c := ∏_ℓ ℓ^{m_ℓ} ∈ ℚ^×. Then v_ℓ(d) = min(v_ℓ(g), v_ℓ(h)) ≥ 0, so d ∈ M, and g/d, h/d ∈ M.
* If e ∈ M divides g and h in M, then e | G in ℚ[β], and v_ℓ(d/e) = min(v_ℓ g, v_ℓ h) − v_ℓ(e) ≥ 0. So e | d in M.

PD: as in §2.6. ∎

*Caveat (sketch / Assessment; almost surely; from the internal review).* Unlike M_{q*}, this M almost surely has **no
cofinal primes**: a nonconstant irreducible must have ϕ-value in Ẑ^×, i.e. divisible by no ℓ, and for f not associate
to β₁ that fails almost surely (Lang–Weil plus
Borel–Cantelli II). The β_i, i ≥ 2, are not even prime. A cofinal variant is plausible: take all a_i in (Ẑ^×)² and
interleave stages adjoining c·x^N. It is not claimed here.

*Remark (what the generic residues do; PROVED, almost surely).* In this M, n + 1 = β₁ + 1 is divisible by infinitely many
standard primes ℓ (almost surely: those with a_{1,ℓ} ≡ −1 mod ℓ, probability 2/(ℓ − 1) for ℓ ≡ 1 (mod 4), independent
across ℓ, Σ diverges; Borel–Cantelli II). But every odd such ℓ is ≡ 1 (mod 4), since a₁ is a square. And 2 ∥ n + 1 because
a₁ ≡ 1 (mod 8). So every standard divisor d of n + 1 has odd part ≡ 1 (mod 4) and 2-part ≤ 2. Hence d ≢ 3 (mod 4), and d is
never a u = 1 hit. The non-standard candidates are covered too. A u = 1 hit is n + 1 = B(4C − 1) with B, C ∈ M, and
β₁ + 1 is irreducible (linear) in ℚ[β]. So either 4C − 1 is a standard divisor (handled above), or B ∈ M ∩ ℚ = ℤ and
4C − 1 = (n + 1)/k for a standard k | n + 1. Then k is a product of at most one 2 and odd ℓ ≡ 1 (mod 4), and
(a₁ + 1)/2 ≡ 1 (mod 4). So ϕ((n + 1)/k) ≡ 1 or 2 (mod 4), never 3. This is T1's Jacobi mechanism seen inside the model.

### 2.8 All true universal ring-language facts about ℤ hold in M_ϕ (PROVED)

Let Th_∀(ℤ) be the set of universal sentences in the *ring* language {0, 1, +, −, ·} (no ≤) that are true in ℤ. It
contains every true statement "the system P₁ = … = P_r = 0 has no integer solution", more generally every true
∀x̄ ⋁_j (P_j(x̄) ≠ 0 ∨ …), and every instance of FLT, Catalan, unsolvable norm equations, etc.

**Theorem A″.** Every model M_ϕ of §§2.1, 2.7 (any residues a_i ∈ Ẑ) satisfies Th_∀(ℤ). Hence, for every primitive
unit-square class r mod q, **NOI + PD + Th_∀(ℤ) ⊬ ES_prime[r mod q]**, and NOI + GCD + PD + Th_∀(ℤ) ⊬ ES_prime[r mod q].

*Proof.* Let θ = ∀x̄ ψ(x̄), with ψ quantifier-free in the ring language, true in ℤ. Suppose M_ϕ ⊨ ¬ψ(X̄) for some X̄ ∈ M^k,
with all X_j ∈ ℚ[β₁..β_K].
* Let P₁, …, P_r be the polynomials in the atoms of ψ, and Q_j := P_j(X̄(β)) ∈ ℚ[β]. Let J be the set of j with Q_j ≠ 0.
* By (F4) there is D such that X̄(b) ∈ ℤ^k for every b ∈ ℤ^K with b_i ≡ a_i (mod D).
* The polynomial ∏_{j∈J} Q_j is nonzero, so it does not vanish on the whole coset a + Dℤ^K. Pick b in the coset with
  Q_j(b) ≠ 0 for all j ∈ J.
* For j ∉ J, Q_j(b) = 0, since Q_j = 0 identically. So the integer tuple X̄(b) gives every atom the same truth value as
  X̄ does in M, and ℤ ⊨ ¬ψ(X̄(b)). This is a contradiction. ∎

*Readings.*
* (PROVED) Shepherdson's model fails Th_∀(ℤ): x = √2·t, y = t give x² = 2y² with y ≠ 0. The BO-type models are much
  closer to ℤ. They satisfy every true universal ring statement, and still not ES on square classes.
* (CONDITIONAL on ES being true, on MRDP being provable in IΔ₀ + exp, and on Lagrange's four-square theorem being
  provable there. The second is Gaifman–Dimitracopoulos 1982, as quoted in `lit_independence.md` §3, PARTLY verified;
  the third is standard and not checked.) Matiyasevich gives a polynomial P_ES with ES ⟺ ∀z̄ ∈ ℤ: P_ES(z̄) ≠ 0 =: U_ES,
  using four squares for the ℕ-variables. This equivalence is then provable in IΔ₀ + exp. If ES is true, U_ES
  ∈ Th_∀(ℤ), so M_ϕ ⊨ U_ES ∧ ¬ES(n). Hence IOpen + U_ES ⊬ ES although IΔ₀ + exp ⊢ U_ES ↔ ES. At the level of open
  induction the *formulation* of ES matters: the Diophantine-universal form is "free", the unit-fraction form is not.
* (PROVED) M_ϕ ⊭ Lagrange's four-square theorem: β₁ is not a sum of four squares in ℚ[β]. A sum of squares of real
  polynomials of maximal degree δ ≥ 1 has a nonzero top form of degree 2δ ≥ 2, and constants would make β₁ constant.
  So over M_ϕ the four-square encoding no longer expresses positivity. Th_∀(ℤ) does **not** contain the ℕ-versions of
  Diophantine facts, i.e. those with positivity constraints. An example is T1 itself in the form
  ∀s, u, B, C ≥ 1: 4uBC − u − B ≠ s². **Whether the non-negative part of M_ϕ satisfies such ordered/ℕ facts, T1 in
  particular, is OPEN.**
* (Assessment) So a proof cannot get by on true universal *ring* facts about ℤ alone. It must use existence principles
  (a divisor or solution some axiom forces to exist, applied to non-standard data: Bezout coefficients, least-number
  principles, counting), or ordered/ℕ-Diophantine facts beyond Th_∀(ℤ). This sharpens the §5 list.
* *Prior art.* The argument is the standard "f.g. subrings embed in ℤ" one (models of the universal theory are the
  subrings of ultrapowers of ℤ), and A″ is plausibly folklore for BO-type models. Related: Otero, *On Diophantine equations
  solvable in models of open induction*, JSL 55 (1990) 779–786 (BO's [Ot1]); method-adjacent prior art: Otero,
  *Quadratic forms in normal open induction*, JSL 58 (1993) 456–476 (NOI embeddings for x² + by² = a via
  parametrisations). BO's [Ot2] is a different paper (*The joint embedding property in NOI*, APAL 60 (1993) 275–290).
  Contents not read beyond abstracts.

## 3. Theorem B: what IOpen does prove

**Theorem B (PROVED; elementary).** If a primitive class r mod q is solvable by polynomials, with P₁, P₂, P₃ positive
on the whole real interval [1, ∞) (this is what the 840 certificate checks), then IOpen ⊢ ES[r mod q]. (Without the positivity proviso: IOpen ⊢ ∀n ≥ N₀ (Cl_{r,q}(n) →
ES(n)) for a numeral N₀. The finitely many standard n < N₀ of the class are settled by exhibiting witnesses, which
exist since ES is verified to 10¹⁷ (or by direct check).)

*Proof.* Work in a model M ⊨ OI and let n ∈ M, n ≥ 1, n = qk + r.
* *Integer values.* Q_i(k) := P_i(qk + r) is integer-valued on ℤ, so Q_i = Σ_j c_{ij} C(k, j) with c_{ij} ∈ ℤ (Newton
  basis). OI proves j! | k(k − 1)⋯(k − j + 1): split k into its residues mod j!, using division by the numeral j!, and in
  each case the divisibility is a polynomial identity. So C(k, j) ∈ M is defined as the quotient, and x := Q₁(k),
  y := Q₂(k), z := Q₃(k) ∈ M.
* *The identity.* (N!)³·(4Q₁Q₂Q₃ − (qk + r)(Q₁Q₂ + Q₂Q₃ + Q₃Q₁)), with N ≥ deg, is a polynomial in the falling factorials
  with integer coefficients that vanishes in ℤ[k]. So it vanishes in M, and M is torsion-free.
* *Positivity.* By hypothesis "∀ real t ≥ 1: P_i(t) > 0" holds in ℝ. It is a first-order sentence with rational
  parameters, so it holds in every real closed field (Tarski), in particular in RC(M) ⊇ M. So x, y, z ≥ 1 in the discrete
  ring M. (If one only knows positivity at the integers of the class, split the argument. For non-standard n, transfer
  "∀t ≥ T₀: P_i(t) > 0" with a standard rational T₀ beyond the real roots. For standard n, use the hypothesis directly.) ∎

**Corollary C (the mod-840 dichotomy; PROVED + CERTIFIED).**
* (a) For every r mod 840 with r ∉ 𝔐, IOpen ⊢ ES[r mod 840] (all n ≥ 2 of the class, prime or not).
* (b) For every r ∈ 𝔐, NOI ⊬ ES_prime[r mod 840] (Cor A.1(a); 𝔐 is exactly the set of unit squares mod 840).

*Certificate for (a)* (`scripts/z64_unprov_mordell840.py` → `data/z64/unprov/mordell840.txt`).
* Each of the 186 primitive classes outside 𝔐 is covered by a member of ET's Type II family "n ≡ −e (mod 4ab), e | a + b"
  with 4ab | 840: x = (n + e)/4, y = cn(n + e)/(4b), z = cn(n + e)/(4a), c = (a + b)/e. Only eight members are needed
  (moduli 4, 8, 20, 24, 40, 56, 84, 168).
* Each member's triple is checked for: the identity (sympy), integer values on the class (deg + 1 consecutive values),
  and positivity for all real n ≥ 1.
* The uncovered primitive classes are exactly 𝔐 = the unit squares mod 840.
* The non-primitive classes use 4/(gm) = 1/(am) + 1/(bm) + 1/(cm) for (g; a, b, c) = (2; 1, 2, 2), (3; 1, 4, 12),
  (5; 2, 4, 20), (7; 2, 21, 42).
* This reproduces Mordell's classical result (ET p. 8, citing [49, 44]); the certificate is a re-verification, not new
  mathematics. Replay: `uv run --with sympy python scripts/z64_unprov_mordell840.py` (seconds).

*Consistency sanity check for Thms A and B (CERTIFIED; `scripts/z64_unprov_famcheck.py` → `data/z64/unprov/famcheck.txt`).*
Thms A and B would contradict each other if some polynomially solvable primitive class contained a unit square. The
script enumerates all 75 124 members with modulus Q ≤ 4000 of the four explicit ET identity families (T2a, T1a, T1d, T2c,
as in the 840 script). It finds **0** classes ρ mod Q that are unit squares mod Q, as ET Prop 1.6 / Mordell–Schinzel
predict. Replay: `python3 scripts/z64_unprov_famcheck.py 4000` (< 1 s). This is a sanity check of the encoding, not
an independent test: it can fail only if ET Prop 1.6 or the family encoding is wrong. The second reviewer separately checked
ET's other three families (T1b, T1c, T2b) to modulus 3000: 40 288 classes, 0 hits.

*Reading (Assessment).* At modulus 840, open induction proves *exactly* Mordell's theorem: whatever IOpen can prove about
ES on residue classes mod 840, polynomial identities already prove. For a general modulus, ET Prop 1.9 essentially classifies the classes
solvable by polynomials (necessary families plus a converse); Thm A excludes the unit-square classes; classes in neither family are not settled here.

## 4. Strong theories (PA, ZFC): what "ES is unprovable" would entail

**Proposition 4.1 (PROVED; standard metamathematics, Σ₁-completeness and Gödel II as in any textbook, e.g. Hájek–Pudlák,
*Metamathematics of First-Order Arithmetic*, Ch. I; theorem numbers not re-checked).** Let T ⊇ Q be a consistent
recursively axiomatised theory and S ⊇ IΣ₁ a metatheory. Write ES_b for the bounded form
∀n ≥ 2 ∃x, y, z (1 ≤ x, y, z ≤ 2n⁴ ∧ 4xyz = n(xy + yz + zx)), a Π⁰₁ (∀Δ₀) sentence.
* (a) ES ↔ ES_b is provable in IOpen, indeed in the theory of discretely ordered rings: for x ≤ y ≤ z one has
  x ≤ 3n/4, y ≤ 2nx and z ≤ nxy ≤ 2n⁴ (`BRAINSTORM/logic_weak_arithmetic.md` §1), all by ordered-ring algebra.
  (Q alone does not prove these bounds; below, "ES" means ES_b whenever T is as weak as Q.)
* (b) If ES is false, then Q ⊢ ¬ES_b, by Σ₁-completeness (`Z58_LOGIC` Prop 2.1(b)). Formalised:
  S ⊢ ¬ES_b → Pr_Q(⌜¬ES_b⌝).
* (c) Hence S ⊢ "T ⊬ ¬ES" implies S ⊢ ES. In particular, a proof that ES is independent of T, carried out in S, contains
  a proof of ES in S.
* (d) S ⊢ "T ⊬ ES" implies S ⊢ Con(T), since an inconsistent T proves everything (formalised in S). So by Gödel II,
  S is not a subtheory of T (T ⊬ Con(T)). Any metatheory proving "PA ⊬ ES" proves Con(PA).
* (e) PA ⊬ ES iff some model of PA contains an n ≥ 2 with no x, y, z ≤ 2n⁴ in the model solving 4/n (completeness,
  using (a)). If ES holds in ℕ, such an n must be non-standard.
So "ES is independent of PA" is a strictly stronger target than "ES is true": it needs a proof of ES (in S ⊋ PA) *and*
a proof that no PA-proof exists.

**What is known about independence of natural Π₁ sentences (literature; see `data/z64/unprov/lit_independence.md`).**
* *Consistency statements and machines.* Con(T) and Gödel sentences are Π₁. O'Rear's 748-state Turing machine halts iff
  ZF is inconsistent, so its non-halting is a Π₁ sentence that ZF does not prove if ZF is consistent, and that is
  independent of ZF if ZF is moreover Σ₁-sound. Source: Aaronson,
  *The Busy Beaver Frontier*, Theorem 7, quoted verbatim in `lit_independence.md` §4 and re-read by the lane in the
  author PDF (VERIFIED, with Aaronson's caveat
  "assuming O'Rear's construction is sound").
* *Matiyasevich (MRDP).* Every Π₁ sentence, Con(ZFC) included, is equivalent to the unsolvability of some Diophantine
  equation. So "Diophantine" is no protection against independence; the equations produced encode proof predicates.
* *Combinatorial independence.* Paris–Harrington, Goodstein and Kirby–Paris hydra are Π⁰₂ (standard classification;
  `lit_independence.md` §1 PARTLY). Their unprovability comes from fast-growing witness functions. Friedman's finite
  combinatorial Π⁰₁ statements tied to large-cardinal consistency were *not* verified at theorem level here
  (`lit_independence.md` §2: NOT FOUND); no claim is made about them.

**Assessment.**
* ES has no growth mechanism: its witness is polynomially bounded and Δ₀-definable ((a)). So the Paris–Harrington route
  (a provably-total-function argument) is unavailable in principle.
* Every verified independent Π₁ sentence above encodes consistency or a proof predicate. We know of no route by which
  a sentence like ES could imply Con(PA) or any other statement unprovable in PA.
* The heuristic picture (≍ log²p expected certificates per prime; FRONTIER §1) also points the other way.
* So **"PA ⊬ ES" or "ZFC ⊬ ES" is not a realistic research target.** It is at least as hard as proving ES ((c)), and
  no mechanism for it is visible.

## 5. Weak theories: the ladder

| theory | ES[classes solvable by polynomials] (incl. all r ∉ 𝔐 mod 840) | ES_prime[unit-square classes] | status / pointer |
|---|---|---|---|
| Q (Robinson) | each true instance ES(n̄) provable (Σ₁-completeness) | each instance provable | no induction; uniform statements not considered |
| IOpen = OI | **provable** for every class solvable by polynomials, in particular all r ∉ 𝔐 mod 840 | **unprovable** | Thm B, Cor C; Thm A |
| NOI (+ PD, cofinal primes) | provable | **unprovable** | Thm A, §2.5 Remark, §2.6 |
| NOI + GCD (+ PD) | provable | **unprovable** | Thm A′ |
| NOI + PD + Th_∀(ℤ) (all true universal ring sentences) | provable | **unprovable** | Thm A″ |
| IOpen + Bez | provable | **OPEN** | §6: the arc criterion isolates what a counter-model needs |
| IE₁ (⊢ IOpen + Bez, Smith 1992) | provable | **OPEN** | IE₁ has no recursive nonstandard models (Wilmers, cited in BO §1); a counter-model cannot be a BO-type recursive construction |
| IΔ₀, IΔ₀ + exp | provable | **OPEN**; unprovability out of reach | Assessment: no natural true Π₁ number-theoretic statement is known to be unprovable in IΔ₀. IΔ₀ ⊢ "infinitely many primes" is itself a well-known open problem; IΔ₀ + WPHP(Δ₀) proves it (Paris–Wilkie–Woods 1988, as reported in Jeřábek's introduction, `Z58_LOGIC` lit_verify item 11) |
| S¹₂ / PV | provable (the Thm B identities are S¹₂-provable) | **OPEN**; S¹₂ ⊢ ES_prime ⟹ polynomial-time "ES-solution or nontrivial factor" algorithm | Buss witnessing; `Z58_LOGIC` Thm 3.1 transferred verbatim |
| T¹₂ | provable | OPEN; T¹₂ ⊢ ES_prime ⟹ the search is in PLS (Buss–Krajíček Thm 5.3) | `Z58_LOGIC` §3 |
| S²₂ | provable | OPEN; S²₂ ⊢ ES_prime ⟹ T¹₂ ⊢ ES_prime (∀Σ^b_2-conservativity, Buss Thm 5) ⟹ search in PLS | `Z58_LOGIC` §3 |
| S³₂ and above | provable | OPEN; not analysed here (Σ^b_k-witnessing into FP^{Σ^p_{k−1}} alone gives nothing, since the search is in FP^NP) | `Z58_LOGIC` §3 |
| PA, ZFC | provable | OPEN; independence would imply ES (§4) | Prop 4.1 |
| Presburger / Skolem arithmetic | — | — | the natural formalisation of ES uses + and · on variables, outside both languages |

**Proposition 5.1 (PROVED relative to Buss's witnessing theorem; the S¹₂ row).** If S¹₂ ⊢ ES_prime[r mod q], then
some polynomial-time algorithm, on every input n ≡ r (mod q), n ≥ 2, outputs an ES solution of n or a nontrivial
factorisation of n.
*Proof.* `Z58_LOGIC` Thm 3.1, verbatim with Hit replaced by the polynomial-time predicate 4xyz = n(xy + yz + zx). The
witness bound is x, y, z ≤ 2n⁴ (Prop 4.1(a)). ∎
*Reading.*
* Assume ES. Then this "solution-or-factor" search is a total NP search problem. If P = NP it lies in FP.
* So a proof of S¹₂ ⊬ ES_prime[r mod q] that goes through witnessing (by showing the search is not in FP) would prove
  P ≠ NP.
* A model-theoretic proof, like Thm A for OI, would not obviously do so. But no BO-style explicit models of S¹₂ are
  available. The S¹₂ question is therefore, in practice, the search-complexity question of `Z58_LOGIC` §5.

**"Which weak theory is the first that could prove ES?" (answer, scoped).**
* *Non-containment (PROVED).* Any theory proving ES_prime on a unit-square class must prove a sentence false in M_{q*}
  (a model of NOI + PD + cofinal primes + Th_∀(ℤ)) and one false in the A′ model (NOI + GCD + PD + Th_∀(ℤ)). The theories
  are not linearly ordered: IE₁ and IΔ₀ + exp do **not** contain Th_∀(ℤ), which by MRDP contains sentences equivalent to
  Con(ZFC). So this is a non-containment statement, not the lower end of an interval. In particular, a proof of ES at primes
  of any square class must use a principle failing in M_ϕ. Candidates: Bezout identities, LNP/induction for formulas
  with quantifiers (bounded existential and beyond), counting (Count₂-type principles give quadratic reciprocity
  for non-standard moduli: Jeřábek, `Z58_LOGIC` lit_verify item 5), or the existence of many divisors of n + u.
* *Upper bound.* Not known: no theory is known to prove ES (ES is open). Assessment: an elementary proof, if one
  exists, would plausibly be formalisable in IΔ₀ + exp (Friedman's grand conjecture, `Z58_LOGIC` lit_verify item 8,
  is the general version of this expectation). So the honest picture is: no theory whose models include M_{q*} or the A′ model; plausibly IΔ₀ + exp suffices *if* ES
  has an elementary proof (Assessment). The two statements are not the ends of an interval.
* The first genuinely open rung is **IOpen + Bez** (and IE₁).

## 6. Barrier reading

**6.1 What Theorem A rules out (Assessment, made precise by the theorem).** NOI + GCD proves everything that follows
from the following tools, applied a fixed finite number of times:
* ring identities with rational coefficients (division by standard integers);
* Euclidean division by arbitrary, also non-standard, elements;
* integer parts of real algebraic functions of the data (Shepherdson's criterion);
* case splits on residues modulo standard numbers;
* open induction, gcds, and integral closure;
* "every element has an irreducible divisor".
None of these can prove ES at the primes of a square class. Thm A is the formal-system *analogue* of three earlier
results (Assessment: it neither implies nor is implied by any of them, since it says nothing about ℕ):
* the procedural barrier B1 (FRONTIER §3; `POINTWISE_SIZE.md` Thm M, Thm C *conditional on Hypothesis H*);
* Mordell–Schinzel (polynomial identities fail on square classes; ET p. 8);
* the T1 slogan "a mechanism must contain a step false at n = m²".

Metaphorically, M_ϕ plays the role of Hypothesis H: its primes are generic. In ℕ, H is what makes formal runs at
square-mimicking points actual (Thm M). In M_ϕ the corresponding genericity holds by construction, and the
unprovability needs no hypothesis.

**Proposition 6.2 (arc criterion; PROVED, by the proof of §2.5).** Let M ⊨ OI and n ∈ M, n > 0. Assume that for every
finite G ⊂ M there are an interval I ⊃ [0, ∞) and a ring homomorphism ψ: ℤ[G ∪ {n}] → C^ω(I) such that:
* ψ(g) ≢ 0 and ψ(g) has the M-sign of g for all large s (g ≠ 0);
* ψ(g)(0) ∈ ℤ for g ∈ G;
* ψ(n) > 0 on [0, ∞) and ψ(n)(0) = m² for an odd m;
* gcd(ψ(g)(0), m) = 1 for each g ∈ G that n does not divide in M.
Then M ⊨ ¬ES★(n), and if n is prime in M, M ⊨ ¬ES(n). If M is a GCD domain and n is prime, the last condition can be
dropped: ET's Type I/II parametrisation (Props 2.2, 2.6) goes through in any GCD domain, so the solution yields positive
a, b, c, d, e ∈ M with ce = a + b and 4abd = ne + 1 (resp. n + e). Positivity propagates along the arc for this system
too: at the largest zero, 4abd = ne + 1 ≥ 1 forces a, b, d > 0, and then ce = a + b forces c, e > 0. For Type II,
4abd = n + e ≥ n > 0 at the largest zero forces a, b, d > 0, and ce = a + b forces c, e > 0. The systems have no positive integer solution at n = m² odd:
* *Type I:* 4abd = m²e + 1 forces gcd(ab, m) = 1, and ET §4 applies.
* *Type II:* ET's argument needs gcd(ab, m) = 1, and we descend to it. If an odd prime p divides gcd(ab, m), then
  4abd = m² + e gives p | e. Then ce = a + b gives p | a + b, so p | a and p | b, and then p² | e. Now
  (a/p, b/p, cp, d, e/p²) solves the same system at (m/p)². The descent ends at gcd(ab, m) = 1, where ET's argument
  applies.
  (The internal reviewer's brute force found no positive solution of 4abd = m² + e, ce = a + b for odd m < 80.)
*Proof of the GCD step.* With x = ndx′, y = dy′, z = dz′ and gcd(x′, y′, z′) = 1, the relation 4dx′y′z′ = y′z′ + nx′y′ +
nx′z′ gives x′ | y′z′, y′ | x′z′, z′ | x′y′, using gcd(y′, n) = gcd(z′, n) = 1, which holds since n is prime and n ∤ y′, z′.
In a GCD domain, gcd(a, bc) | gcd(a, b)gcd(a, c), and coprime divisors multiply. So x′ = ab, y′ = ac, z′ = bc up to
units, with a = gcd(x′, y′), b = gcd(x′, z′), c = gcd(y′, z′). The rest is ET's algebra. ∎ (The Type II analogue in a
GCD domain is a sketch: the same steps with x = dx′, y = ndy′, z = ndz′ and ET Prop 2.6's algebra, not written out.)

*Reading.* The arc criterion says what a counter-model for a stronger theory needs: finitely generated pieces that are
"free enough" to have integer points at odd squares, connected analytically to the order at infinity. A theory
proves ES on square classes only if its axioms force Diophantine relations among the finitely many elements involved,
and these relations must have **no** integer points at odd squares.
* Bezout identities ug + vh = 1, two-square representations n = a² + b², and Fermat-type relations all have integer
  points at suitable odd squares. Heuristically, then, they do not obstruct arcs. Note (PROVED) that M_ϕ itself violates the
  two-squares principle TS ("every prime ≡ 1 (mod 4) is a sum of two squares"): in ℚ[β], a² + b² with a, b
  nonconstant has even degree ≥ 2, since the top forms cannot cancel over ℝ, so a² + b² = β₁ is impossible. So TS is
  another principle a proof could use. The arc criterion suggests it is not the decisive one.
* The ES/Type I/II relations have none, by T1.
CONJECTURE (T1 meta-principle for theories): IOpen + Bez + {every prime ≡ 1 (mod 4) is a sum of two squares} ⊬
ES_prime[r mod q] for unit-square classes. Not proved: it needs a model construction that closes under Bezout
coefficients while keeping the arc property (§9).

**6.3 Other barrier formalisations asked for (Assessment).**
* "Proofs using only local data": captured by Thm A. M_ϕ has exactly the residue ring of a square-mimicking point, and
  every congruence fact of the class holds in it.
* "Proofs using only multiplicative functions / bounded-order character sums": these are analytic, not first-order
  arithmetic. They have no natural formal system smaller than PA. Their barrier statements remain the scoped theorems of
  FRONTIER §3 (B1, B6, the bounded-order inverse lemma). We did not find a formal system that captures them without
  also capturing analysis.

## 7. Proof complexity

**Proposition 7.1 (PROVED; standard).** Every true instance ES(n̄) has a proof of length poly(log n) in any theory with
binary numerals that verifies multiplication tables (e.g. PV, S¹₂, Q with efficient numerals). Exhibit the witness of
O(log n) bits (Prop 4.1(a)) and verify the equation by school arithmetic. So no superpolylogarithmic lower bound on
instance proofs can hold.
*Consequences (Assessment).*
* The difficulty of ES is uniformity, not length. Thm A is a uniformity statement: NOI proves each ES(p̄) in poly(log p)
  steps, but proves no single sentence covering all primes of a square class.
* Proof-complexity questions about ES are therefore about the *search problem*: its TFNP class (FP? PLS? PPA?). Through
  witnessing these correspond to provability in S¹₂, T¹₂, …, and they have no unconditional answers for non-black-box
  problems.
* The propositional "ES below 2^k" is not a natural tautology family: it is ∀n ∃w, i.e. Π₂^p.

## 8. Verdict, screens, proposed FRONTIER text, bottom line

**Verdict: strengthened (logic side); narrowed (strong-theory side).** No bearing on the truth of ES; no HOT LEAD.

What was proved:
* **Thm A / A′ (new to our knowledge).** For every primitive unit-square class r mod q, neither NOI + PD + cofinal primes nor NOI + GCD + PD proves
  ES_prime[r mod q]. Also NOI ⊬ (MS★), (MS); this answers `Z58_LOGIC` §6.1 "Open" and
  `BRAINSTORM/logic_weak_arithmetic.md` §5 (IOpen ⊬ ES_prime).
  * The counterexamples are infinite primes at square-mimicking profinite points.
  * The proof transfers T1 into the model by analytic arcs (Lemmas 2.3, 2.4) and uses no hypothesis.
* **Thm A″.** These models satisfy every true universal ring sentence about ℤ. So NOI + PD + Th_∀(ℤ) ⊬ ES_prime on square
  classes. (CONDITIONAL on ES, MRDP and Lagrange in IΔ₀ + exp: IOpen + U_ES ⊬ ES although IΔ₀ + exp ⊢ U_ES ↔ ES.)
* **Thm B + Cor C.** IOpen proves ES on every class solvable by polynomials. Mod 840 this gives an exact dichotomy:
  IOpen proves ES on all classes outside 𝔐, and NOI proves it on no class of 𝔐 (at primes). CERTIFIED re-verification
  of Mordell's covering.
* **Prop 4.1.** Independence of ES from PA/ZFC would imply ES and Con(PA). There is no growth mechanism.
* **Prop 5.1.** The S¹₂ route goes through search complexity (P ≠ NP for the witnessing route).
* **Prop 6.2 (arc criterion).** States exactly what a counter-model for a stronger theory needs.
* **Prop 7.1.** Instances have poly(log n) proofs; the difficulty is uniformity.

What is out of reach (Assessment, with reasons):
* "PA ⊬ ES" / "ZFC ⊬ ES": strictly harder than ES (Prop 4.1), and no mechanism is visible.
* "IΔ₀ ⊬ ES": no explicit nonstandard models; nothing comparable is known for any natural statement.
* "S¹₂ ⊬ ES": via witnessing it needs a hardness result implying P ≠ NP.

**Hard screens (FRONTIER §4).**
* *T1 squares.* Built in: Thm A *is* T1 lifted to a theory. It covers exactly the classes containing unit squares.
* *8/131, numerator 8.* Thm A(iii) applies verbatim to R₈ and to every (★)-sub-line (subsets of R vanish at squares).
  Nothing here distinguishes C odd from C even; nothing is falsified.
* *Tied modulus (B2).* Not addressed. Assessment: in M_ϕ the integers n + u are "generic". Their standard divisors avoid
  the hit classes by the Jacobi mechanism, and their only non-standard divisors are the cofactors (n + u)/k, k a standard
  divisor, whose residues are again forced by the square-mimicking ϕ. So B2 fails there. A proof of
  B2-positivity must use a principle false in M_ϕ (§5 list).
* *Fixed p.* Not applicable: no pointwise or averaged positivity is claimed.

**Falsifier table (re-stated; details in §0).**
* *F1 odd squares:* the mechanism of Thms A–A″ *is* T1, lifted into a model. It covers exactly the unit-square classes.
* *F2 C-even:* applies verbatim to R₈ and every (★)-sub-line; nothing distinguishes C odd from C even; no positivity is
  claimed.
* *F3 composites:* the counterexamples are primes of the model (for (★), any suitable polynomial generator).
* *F4 known zeros:* untouched; no positivity is claimed.
No HOT LEAD.

**Proposed FRONTIER text** (do not edit FRONTIER here).
* §3, new barrier entry (after B1):
  > **B1-formal — square classes are unprovable in normal open induction** (`Z64_UNPROV.md` Thms A, A′, A″, B;
  > PROVED relative to Berarducci–Otero JSL 1996 (Lemmas 2.4, 2.6–2.9, 4.1, Thm 4.2) and ET Prop 1.6).
  > * For every primitive unit-square class r mod q, IOpen + normality + GCD + "every element has an irreducible
  >   divisor" + all true universal ring sentences about ℤ does not prove "ES holds at every prime ≡ r (mod q)". Conversely, IOpen proves ES on every class solvable
  >   by polynomials, so mod 840 it proves exactly Mordell's theorem.
  > * Also IOpen ⊬ (MS) (answers `Z58_LOGIC` §6.1).
  > * Model: BO's normal-model construction with residues ϕ(β) at a square-mimicking point (for q* = 1, BO's
  >   model for an enumeration beginning with x). Its infinite primes are
  >   counterexamples, by analytic arcs to integer points at odd squares plus T1.
  > * This is the formal-system analogue of B1 Thm C (which is conditional on H); it says nothing about ℕ and neither
  >   implies nor is implied by Thm C.
  > * Rules out (at primes of unit-square classes): proofs formalisable in NOI + GCD + PD + Th_∀(ℤ) (ring language):
  >   identities, floors of algebraic functions, Euclidean division, residues, open induction, gcds, irreducible
  >   divisors, true universal ring facts about ℤ.
  > * Does NOT rule out: Bezout-level divisor arithmetic (IE₁), quantified induction, counting/reciprocity for
  >   non-standard moduli; the two- and four-squares principles (both fail in M_ϕ, PROVED, so they are usable
  >   principles); ordered/ℕ-form universal facts such as T1 itself (OPEN whether M_ϕ satisfies them).
  > * Open: IOpen + Bez ⊬ ES_prime[square class] (the arc criterion, Prop 6.2, isolates what is needed).
* §6 dead ends, one line:
  > "Prove ES is independent of PA/ZFC": would prove ES plus Con(PA) (`Z64_UNPROV` Prop 4.1); no mechanism; not a target.

**Bottom line.**
* *Can unprovability of ES be proved?* For strong theories, no realistic route exists. An independence proof would
  contain a proof of ES, and ES has no consistency-strength or fast-growth mechanism.
* For weak theories, yes. This lane proves what is, to our knowledge, the first unprovability result for ES at primes in a weak theory. Normal open induction, even with
  gcds, prime divisors and all true universal ring facts about ℤ, cannot prove ES on any square class.
* The result is exactly the odd-square obstruction lifted to a formal theory. It is unconditional and sharp at
  modulus 840: IOpen proves precisely Mordell's classes.
* "ES is unprovable in T" remains a realistic research target only for weak T: open candidates are IOpen + Bez and IE₁
  (these theories are not comparable with NOI + GCD + PD + Th_∀(ℤ); see §5). For IOpen + Bez the arc criterion says what a
  counter-model must look like.
* This is logic, not progress on ES. It formally certifies that any proof must use divisor-richness or counting
  principles which the generic-prime models violate. That is B2 seen from proof theory.

## 9. Open problems (precise)
* **(O1) IOpen + Bez ⊬ ES_prime[r mod q] for unit-square r?** A Bezout model with the arc property (Prop 6.2) would
  settle it. Natural starting point: S. T. Smith, *Building discretely ordered Bezout domains and GCD domains*, J. Algebra
  159 (1993) 191–239 (citation verified, contents not read; `lit_models.md` §6). Candidate: interleave the BO step with
  Bezout steps that adjoin u, v = (1 − ug)/h for coprime pairs (g, h). Away from V(g, h) the coordinate ring is an
  A¹-bundle over the previous stage.
  *Where the difficulty sits (Assessment).*
  * The arc side looks fine.
    * Choose the integer point b with gcd(g(b), h(b)) = 1. At the finitely many bad standard primes, ϕ separates g and
      h. Above them an Ekedahl-type sieve applies, since the density of b with ℓ | g(b), h(b) is ≤ C/ℓ² by the
      point-count lemma of §2.7.
    * Choose the integer Bezout pair at b congruent to (ϕ(u), ϕ(v)) mod D. This is possible because the syzygies of a
      unimodular row mod D are generated by (h, −g).
    * Let ψ(u) interpolate analytically: the integer value at s = 0, the values 1/ψ(g) at the zeros of ψ(h) on the arc
      (a generic arc avoids the codimension-2 set V(g, h)), and u's order type at ∞.
  * The model side is the obstacle. u and v cannot be Puiseux polynomials (β₁ is not a unit mod β₂ in ℚ[β]), so
    M[u, v] leaves K[x^ℚ]. The discreteness, integral-part and GCD bookkeeping of such extensions needs a Smith-type
    construction, which we have not carried out.
* **(O2) IE₁.** Any counter-model is non-recursive (Wilmers). Does IE₁ prove ES on some square class? Expected no.
* **(O3) Non-square classes outside ET's families** (general modulus): IOpen-provable or not? Thm A needs integer points
  at odd squares. A class with no square needs a different ES-free Diophantine target.
* **(O4) T1 meta-principle for theories (CONJECTURE, §6).**

## 10. Review log and replay

**Internal hostile review** (`data/z64/unprov/internal_review.md`; Opus deep-mode subagent; the Codex reviewer was out of
quota). It reran the certificate script (byte-identical output) and added an independent exact-arithmetic check: 186
classes × 300 values, 0 failures. It also brute-forced the Type II system for odd m < 80. Verdict: **Theorem A correct**;
no FATAL issue; 1 MAJOR and 14 MINOR issues, all applied:
* (1, MAJOR) Thm A′ "cofinal primes" was almost surely false for the random-residue model. The clause was removed, a
  caveat added, and Mohsenipour cited.
* (2) Cofinality in M_{q*} is now proved: §2.5 Remark, generators f_m = β₁ + (β₂ − β₃)²β₂^{2m}, with Lemma 2.3 extended to
  arbitrary polynomial generator systems.
* (3) The reliance list now cites the BO lemmas actually used; Thm 4.3 is not used.
* (4) Prop 6.2 GCD clause: a Type II descent to gcd(ab, m) = 1 was added.
* (5) Prop 4.1 now uses the bounded form ES_b (Q does not prove the bounds), with "S is not a subtheory of T" and the
  non-standard proviso.
* (6) O'Rear: unprovable if consistent, independent if Σ₁-sound.
* (7) §5 column renamed to "classes solvable by polynomials".
* (8) "Unconditional version of Thm C" became "formal-system analogue"; the H remark is marked as metaphor.
* (9) The §2.7 remark is corrected (2 ∥ n + 1).
* (10) §8 B2 remark corrected (cofactors (n + u)/k exist).
* (11) F3 row scope restricted to polynomial generators.
* (12) Thm B: (N!)³, and the small-n proviso is made explicit.
* (13) Type II: G stated.
* (14) Novelty qualified "to our knowledge"; Smith 1993 cited for O1; q* = 1 is BO's model verbatim.
* (15) Wording: Presburger row, recursiveness parenthetical, Bezout argument, ET Prop 1.9, TS label.

**Replay** (under `ulimit -v 4000000`):
* `uv run --with sympy python scripts/z64_unprov_mordell840.py` writes `data/z64/unprov/mordell840.txt` (seconds);
* `python3 scripts/z64_unprov_famcheck.py 4000` writes `data/z64/unprov/famcheck.txt` (< 1 s).
Everything else is proof.

**Second (focused) review** (appended to `data/z64/unprov/internal_review.md`). Scope: the post-review additions,
i.e. §2.8 Thm A″, the cofinal generators f_m, the Prop 6.2 Type II descent, the revised Prop 4.1, the famcheck sanity
check and the O1 assessment. It reran famcheck and checked ET's other three families separately. Verdict: no FATAL
issue, 1 MAJOR and 7 MINOR issues, all applied:
* (1, MAJOR) §2.8 overclaimed "all Diophantine non-existence facts". It now says "universal ring-language facts", adds
  M_ϕ ⊭ Lagrange, and marks the ordered/ℕ facts (T1 included) as OPEN.
* (2) CONDITIONAL numbering fixed.
* (3) Folklore and Otero prior art noted.
* (4) ES_b now requires x, y, z ≥ 1.
* (5) famcheck relabelled a sanity check, runtime corrected, and the reviewer's T1b/T1c/T2b check recorded.
* (6) Summary texts synchronised: F1 row, §8, FRONTIER text (A″; BO lemmas; recursiveness), §5 "contained in neither",
  window and bottom line.
* (7) §2.7 Caveat labelled.
* (8) O1 wording: A¹-bundle away from V(g, h); Bezout pair matched to ϕ mod D.

**Cross-model review** (`data/z64/xreview/REVIEW_UNPROV.md`; Opus standing in for the cross-model reviewer; verdict
ACCEPT-WITH-FIXES; headline theorems A, A′, A″, B and Cor C re-derived as correct; lane scripts reproduce
byte-identically; independent checks: T1 for s ≤ 1000, ET Prop 1.6 at ℓ² for odd ℓ ≤ 25, Type II system for odd m ≤ 121).
All ten required fixes were applied:
* (1) §5 S²₂ row: PLS via ∀Σ^b_2-conservativity over T¹₂; higher levels not analysed.
* (2) Thm B hypothesis is now real positivity on [1, ∞) (what the certificate checks), with the standard/non-standard
  split noted.
* (3) The "window" wording became non-containment, with the note that IE₁ and IΔ₀ + exp do not contain Th_∀(ℤ)
  (§5, bottom line).
* (4) Otero citations corrected (JSL 55 (1990) = [Ot1]; JSL 58 (1993) method-adjacent; [Ot2] = APAL 60).
* (5) Reliance list adds BO Thm 1.1 and Lemma 2.3; the F3 row cites (F1), not BO Lemma 2.10.
* (6) "BO's model for an enumeration beginning with x".
* (7) §2.7 Remark covers the non-standard cofactors (n + 1)/k; the Caveat is relabelled sketch/Assessment, with
  "divisible by no ℓ".
* (8) Novelty scoped: "first unprovability result for ES at primes in a weak theory, to our knowledge".
* (9) FRONTIER text: "Rules out" names the theory; "Does NOT rule out" adds the two-/four-squares principles and the
  ordered/ℕ facts (T1).
* (10) Prop 6.2 GCD Type II is marked as a sketch.
