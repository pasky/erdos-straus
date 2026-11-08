# Z64_UNPROV — can unprovability of ES be proved? (checkpoint 1)

Status: z64 lane UNPROV (brief `z52bbriefs/z64_lanes.md` §UNPROV; common rules `z58_lanes.md`, `z53_depth.md`).
**ES is OPEN. Nothing here proves or disproves ES, (MS), or any case of them.** Internal, unrefereed.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z64_unprov_*`,
data `data/z64/unprov/`. Primary source for the model: Berarducci–Otero, *A recursive nonstandard model of normal open
induction*, JSL 61 (1996) 1228–1241 (author PDF archived as `data/z64/unprov/berarducci_otero_1996_recNOI.pdf`, read in
full; cited below as BO with their lemma/theorem numbers).

**Headline (PROVED, relative to BO Thms 4.2/4.3 and ET Prop 1.6).** *For every primitive residue class r mod q that is
a unit square mod q, normal open induction does not prove "ES holds at every prime ≡ r (mod q)".* Together with
Mordell's identities this decides open-induction provability class by class mod 840: IOpen proves ES on every class
outside 𝔐 = {1, 121, 169, 289, 361, 529}, and normal IOpen proves it at primes of no class in 𝔐. It also answers the
open question of `Z58_LOGIC.md` §6.1: IOpen ⊬ (MS★) and IOpen ⊬ (MS). The counterexamples are infinite *primes* whose
residue in Ẑ is a square-mimicking unit; the proof transfers the odd-square obstruction T1 (ET Prop 1.6) into the model by
an analytic interpolation argument. No Hypothesis H is used: in the model the generic primality H supplies is built in.

## 0. Falsifier table (mandatory)

This lane proves *non-provability* theorems, not positivity. The table records how they interact with the screens.

| screen | behaviour |
|---|---|
| **F1 odd squares** | The mechanism *is* F1. The unprovability theorem (Thm A) is T1 (ET Prop 1.6 / Z57_SYNTH Lemma A.1(b)) imported into a model: any hypothetical ES solution at the model prime specialises to a Type I/II solution at an odd square ℓ². So the result covers exactly the residue classes that contain unit squares, and Thm B shows that the remaining classes mod 840 are IOpen-provable. Reading: a proof of ES must use, at an identifiable step, a principle false in the model M_{q*}. Candidates are divisor arithmetic beyond normality (Bezout/GCD-level), counting, or reciprocity for non-standard moduli. Open induction, normality, residue information and "every element has an irreducible divisor" (§2.6) are not enough. |
| **F2 C-even sub-line** | Thm A transfers verbatim to R₈ and every (★)-sub-line, since R₈(m²) ≤ R(m²) = 0. Nothing here distinguishes C odd from C even. Nothing here is falsified by F2 either: no positivity is claimed. |
| **F3 composites** | The model counterexamples are *primes* of the model (BO Lemma 2.10; §2.2). For (MS★) primality is not even used (§2.5): any element β with square-mimicking residue fails. This is consistent with F3: by `Z58_LOGIC` Thm 6.2, composite-shaped counterexamples already exist in Shepherdson's model. |
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

**Theorem A (PROVED, relative to BO Thms 4.2, 4.3 and ET Prop 1.6 / Z57_SYNTH Lemma A.1(b)).** Let q* ∈ (Ẑ^×)². There
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
  to ℚM_n = ℚ[β₁..β_n]. Hence **M ⊨ NOI**. (Recursiveness, BO Thm 4.4, is not needed; it holds when q* is computable.)

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
* *Type II.* The same, with X in the role of Y, Z (choose b′ with X(0, b′) ≠ 0). It yields a Type II solution for ℓ²,
  contradicting ET Prop 1.6 (f_II(m²) = 0).
* (iii): suppose u, B, C ∈ M are ≥ 1 with 4uBC − u − B = n. Take D from (F4) for {u, B, C}, any odd s ≡ s₀ (mod D),
  and b = (s², b′) with b′_i ≡ q* (mod D). Lemmas 2.3 and 2.4 ((★)-form) give positive integers u(b), B(b), C(b) with
  4u(b)B(b)C(b) − u(b) − B(b) = s². This contradicts R(s²) = 0 (T1; Z57_SYNTH Lemma A.1(b)). No primality is used here. ∎

*Remarks.*
* ET Prop 1.6 is used only in its Diophantine content: the proof (ET §4) uses only the equations (2.1)–(2.2)
  (resp. (2.13)–(2.14)) of the Type I/II parametrisation together with Jacobi-symbol reciprocity. The parametrisation is
  ET Prop 2.2/2.6 for natural-number solutions, and we apply it only to the integer solution (x₀, y₀, z₀).
* Every β_i with positive leading coefficient works equally, with T chosen beyond the last zero of p_i′ and of p_i + π_i.
  So the counterexamples are cofinal. β_i with negative leading coefficient give the positive prime −β_i of residue
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
* *Bezout fails:* β₁, β₂ have gcd 1 but no Bezout identity, by degree in ℚ[β]. So M ⊭ IE₁ (Smith 1992 abstract, verified
  in `lit_models.md` §6: IE₁ ⊢ IOpen + Bez).
* *GCD fails in M_{q*}* when all ϕ(β_i) are equal. β₁ − β₂ and β₁ − β₃ have ϕ = 0, so both are divisible by every
  standard integer. They are coprime in ℚ[β], so their common divisors in M are exactly the nonzero integers, and there
  is no greatest one. §2.7 repairs this with generic residues.

### 2.7 The GCD strengthening (PROVED)

**Theorem A′.** For every primitive unit-square class r mod q there is a model M ⊨ NOI + GCD + PD (every pair of
elements has a gcd; every element ≥ 2 has an irreducible divisor) with cofinal infinite primes. It contains an infinite
prime n ≡ r (mod q) with M ⊨ ¬ES(n) ∧ ¬ES★(n). Hence **IOpen + GCD + PD ⊬ ES_prime[r mod q]**. In particular the Type I/II
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

*Remark (what the generic residues do).* In this M, n + 1 = β₁ + 1 is divisible by infinitely many standard primes ℓ
(almost surely: those with a_{1,ℓ} ≡ −1 mod ℓ, probability 2/(ℓ − 1) for ℓ ≡ 1 (mod 4), independent across ℓ, Σ diverges). But all of them have ℓ ≡ 1 (mod 4), since a₁ is a square. So every
standard divisor d of n + 1 is ≡ 1 (mod 4) and never a u = 1 hit. This is T1's Jacobi mechanism seen inside the model.

## 3. Theorem B: what IOpen does prove

**Theorem B (PROVED; elementary).** If a primitive class r mod q is solvable by polynomials, with P₁, P₂, P₃ positive
on every n ≥ 1 of the class, then IOpen ⊢ ES[r mod q]. (Without the positivity proviso: IOpen ⊢ ∀n ≥ N₀ (Cl_{r,q}(n) →
ES(n)) for a numeral N₀, and the finitely many standard n < N₀ are settled by exhibiting witnesses.)

*Proof.* Work in a model M ⊨ OI and let n ∈ M, n ≥ 1, n = qk + r.
* *Integer values.* Q_i(k) := P_i(qk + r) is integer-valued on ℤ, so Q_i = Σ_j c_{ij} C(k, j) with c_{ij} ∈ ℤ (Newton
  basis). OI proves j! | k(k − 1)⋯(k − j + 1): split k into its residues mod j!, using division by the numeral j!, and in
  each case the divisibility is a polynomial identity. So C(k, j) ∈ M is defined as the quotient, and x := Q₁(k),
  y := Q₂(k), z := Q₃(k) ∈ M.
* *The identity.* N!·(4Q₁Q₂Q₃ − (qk + r)(Q₁Q₂ + Q₂Q₃ + Q₃Q₁)), with N ≥ deg, is a polynomial in the falling factorials
  with integer coefficients that vanishes in ℤ[k]. So it vanishes in M, and M is torsion-free.
* *Positivity.* "∀ real t ≥ 1: P_i(t) > 0" is a true universal statement of real closed fields, hence true in RC(M) ⊇ M.
  So x, y, z ≥ 1 in the discrete ring M. ∎

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

*Reading (Assessment).* At modulus 840, open induction proves *exactly* Mordell's theorem: whatever IOpen can prove about
ES on residue classes mod 840, polynomial identities already prove. For a general modulus, ET Prop 1.9 lists the classes
solvable by polynomials; Thm A excludes the unit-square classes; classes in neither family are not settled here.

## 4–7. TODO (after checkpoint)
PA/ZFC; bounded arithmetic; barrier reading; proof complexity; GCD strengthening.

## 8. Verdict (checkpoint)
**Strengthened (logic).** New theorem: square classes are not provable in normal open induction (Thm A). This is the
first formal-system unprovability result for ES at *primes*, and it is unconditional (B1 Thm C needed Hypothesis H).
Exact mod-840 dichotomy (Thm A + B). It does not bear on the truth of ES.
