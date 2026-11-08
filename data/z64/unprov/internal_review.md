# Internal hostile review of Z64_UNPROV.md

Reviewer: hostile logic/number-theory subagent. Sources read: BO JSL 1996 (archived PDF, full text via pdftotext),
ET (sources/elsholtz-tao-1107.1010.pdf: §1 defs p.3, Prop 1.6, def. "solvable by polynomials" p.7–8, Prop 1.9,
Props 2.2/2.6 and §4 proof), Z58_LOGIC §§1–3, 6.1, Z57_SYNTH Lemma A.1, BRAINSTORM/logic_weak_arithmetic.md,
POINTWISE_SIZE.md Thm C, data/z64/unprov/lit_*.md, data/z58/logic/lit_verify.md.
Computations: `scripts/z64_unprov_mordell840.py` re-run (1.2 s), output byte-identical to the committed
`mordell840.txt`. Independent re-check (exact Fractions, no sympy): all 186 triples give positive integers and satisfy
4/n = Σ1/P_i at n = r + 840t, t = 0..299 (55 800 checks, 0 failures). Brute force: the Type II system
4abd = m² + e, ce = a + b has no positive solution for odd m < 80, with no coprimality assumed (supports the fix for issue 4).

## Verdict

**Theorem A is correct**, and so are Cor A.1 and Thm B/Cor C. No FATAL issue was found. One MAJOR error: Thm A′'s
"cofinal infinite primes" clause is almost surely false for the construction given. The unprovability content of A′
(NOI + GCD + PD ⊬ ES_prime) survives. Everything else is MINOR: precision, overclaims in readings, missing citations.
ES is never claimed proved, and the labels are mostly right.

### Checked and found sound (the attack failed)
* **M = {g ∈ ℚ[β] : ϕ(g) ∈ Ẑ}.** This follows from BO Lemma 2.7 by induction on stages, since ℤ[β₁..β_{n+1}] ⊂ M_n[β_{n+1}].
  BO Lemmas 2.7, 2.8, 2.10 are stated for an arbitrary ring hom ϕ: L → Ẑ. I re-derived normality of L_ϕ for arbitrary ϕ
  (Ẑ is integrally closed in 𝔸_f), and discreteness: an element of ℚL in (0,1) is a rational k/m ∉ Ẑ. The choice of p_i
  depends only on ℚM_n = ℚ[β₁..β_n] (BO Lemma 2.4 needs only M_n ⊨ ZR, which holds for every ϕ). It is therefore
  ϕ-independent, and ϕ (also a random one) can be fixed afterwards. p₁ = x is legitimate: BO allow any fixed
  enumeration, and x ∈ K₀[x^ℚ]• is at infinite distance from ℤ.
* **β₁ is prime in M.** (F1) gives a direct proof that does not use BO Thm 4.3. The units are ±1.
* **Lemma 2.3.**
  * ψ is a ring hom on ℚ[B] into C^ω(−T, ∞).
  * ψ(g)(0) = g(b).
  * The Taylor expansion is exact and finite: (∂^αg)(Γ) = O((1+s)^E) and Δ^α = O(e^{−s}).
  * g(β) ∈ K[x^ℚ] has only non-negative exponents. So g(Γ(ξ)) either → ±∞ or is a nonzero constant c, and in the
    constant case ψ(g) = c + o(1). Both cases are handled correctly.
  * (c) is correct for p₁ = x.
* **Lemma 2.4.** Both forms are correct. Zeros are isolated on a compact set, and the blow-up/boundedness argument at the
  largest zero works. The (★) case analysis is complete.
* **§2.5.**
  * Type split in the UFD: correct, including the "all three divisible" exclusion.
  * (F4) and the CRT choice of ℓ: correct. ℓ is odd because 8 | D and gcd(s₀, D) = 1.
  * gcd(ℓ², y₀) = 1: since v_r(Y₀(b′)) + v_r(Z₀(b′)) = 0 with both ≥ 0.
  * ET's Type I/II definitions (ET p.3: "n divides x but is coprime to y, z"; "n divides y, z but is coprime to x") match
    exactly. ET Prop 1.6 is stated "for any odd perfect square n" and covers ℓ = 1 (trivially, since 4 is not a sum of
    three unit fractions ≤ 1).
  * (iii) via Z57 Lemma A.1(b), which holds for every m.
* **§2.6.**
  * PD is correct. The terse step "ϕ(f) is a unit for almost all ℓ" is justified because ϕ(f)·ϕ(g/f) ∈ Ẑ^× forces ϕ(f) ∈ 𝔸_f^×.
  * "GCD fails in M_{q*}" is correct.
  * TS failure (§6.2) is correct.
* **§2.7.**
  * gcd construction: correct. m_ℓ may be negative; this is harmless.
  * Point-count lemma: correct, including the k = 1 and constant cases.
  * Measure argument for (G1)/(G2): correct, including the 3/ℓ^k bound and Borel–Cantelli I.
* **Thm B.**
  * Newton-basis integrality in OI: correct.
  * Positivity via RCF completeness: correct.
* **Cor C(a).**
  * Every primitive r ∉ 𝔐 is covered by a T2a identity, integer-valued on the class (checked on deg+1 consecutive values,
    which suffices) and positive on all real n ≥ 1. So all n ≥ 2 of the class are covered, small n included.
  * Non-primitive classes: n = g·m with m ≥ 1, and the scaling identities hold for all m ≥ 1.
  * The uncovered classes are exactly the unit squares mod 840.
* **Cor A.1(b)** via Z58 Remark 6.3: valid. Also note that q* = 1 *is* BO's published model, so Cor A.1(b) is literally
  a statement about BO's own model.
* **Prop 5.1** (Buss witnessing, bound 2n⁴) and **Prop 7.1**: fine.

## Issues

1. **MAJOR — Thm A′ "cofinal infinite primes" is almost surely false**
   * *Location:* §2.7 line 195; repeated at §5 line 346 ("NOI + GCD + PD + cofinal primes") and §8 line 432 ("(+ cofinal primes)").
   * *Why it fails.* In M_a, a nonconstant irreducible of M must be c·f, with f irreducible in ℚ[β] and ϕ(cf) ∈ Ẑ^×. That
     forces ϕ(f) ∈ 𝔸_f^×: only finitely many ℓ may divide f(a_ℓ).
     * Take f irreducible and not associate to β₁. Then f(y², B₂, …) has an absolutely irreducible factor over some number
       field.
     * For the positive-density set of ℓ split in that field, Lang–Weil (or Chebotarev, when k = 1) gives
       P(ℓ | f(a_ℓ)) ≫ 1/ℓ.
     * The events are independent across ℓ, so Borel–Cantelli II applies. There are countably many f.
     * Hence, a.s., the only positive infinite irreducible of M_a is β₁ itself. Example: β₁ + 1 is divisible in M by every
       ℓ ≡ 1 (4) with a_{1,ℓ} ≡ −1, and those are infinitely many.
     * The β_i (i ≥ 2) are not prime either, since a_i is a non-unit at infinitely many ℓ.
   * *Fix (either):*
     * (a) Delete "with cofinal infinite primes" from Thm A′ and its echoes. Write the §5 lower bound as "NOI + GCD + PD
       (Thm A′) and NOI + PD + cofinal primes (Thm A)".
     * (b) Change the construction:
       * Take every a_i Haar-random in (Ẑ^×)². The per-point bound becomes ≤ (2/(ℓ−1))^k ≤ 3^k/ℓ^k, and (G1)/(G2)
         still hold.
       * Force {β_i} cofinal by interleaving stages that adjoin p = c·x^N with c ∈ K_n ∖ L, c > 0. This p is at infinite
         distance from M_n because its x^N-coefficient is not in L. BO's Claim-proof uses only "p ∈ K_n[x^ℚ]• at
         infinite distance", so it still applies.
       * Every such β_i is then a prime with square-mimicking residue.
     * Either way, mention Mohsenipour 2006 (recursive IOpen + GCD + cofinal primes; `lit_models.md` §3).

2. **MINOR — cofinality in M_{q*} is not argued**
   * *Location:* §2.5 Remark line 172; §2.6 line 184; §5 row "NOI (+ PD, cofinal primes)".
   * *Problem.* "So the counterexamples are cofinal" needs the positive-leading β_i to be unbounded. BO Thm 4.3 asserts
     {β_k} unbounded with only "clearly", and with an adversarial enumeration this is not obvious.
   * *Fix: cofinal primes.* For "primes are unbounded" use f_m := β₁^m + β₂ − β₃.
     * It is linear in β₂, hence irreducible.
     * ϕ(f_m) = q*^m ∈ Ẑ^×, hence f_m is prime in M.
     * f_m exceeds any given element for large m.
   * *Fix: cofinal counterexamples.* Either change coordinates to ℚ[β₁, f_m, β₃, …] and rerun Lemmas 2.3–2.4 with T beyond
     the zeros of f_m′, or use the interleaving of 1(b). Otherwise drop the claim.

3. **MINOR — imprecise reliance list**
   * *Location:* headline line 10; Thm A line 60.
   * *Problem.* Primality is proved directly in (F1), so BO Thm 4.3 is not used. What is used: BO Lemmas 2.4, 2.6, 2.7,
     2.8 ([D2]), 2.9 ([Bk]), 4.1, the stage Claim, and Thm 4.2.
   * *Fix.* Cite these instead.

4. **MINOR — Prop 6.2 GCD variant: "ET §4 shows directly" is inaccurate for Type II**
   * *Location:* §6.2 lines 380–386.
   * *Problem.* Once the coprimality condition is dropped, the integer point need not have gcd(abd, m) = 1. ET's
     (omitted) Type II argument needs gcd(ab, m) = 1, both for (n/q) = 1 and for gcd(e, q) = 1.
   * *Fix: add a descent.*
     * Suppose an odd prime p | gcd(ab, m). Then p | e, then p | b and p | a (from ce = a + b), then p² | e.
     * Then (a/p, b/p, cp, d, e/p²) solves the same system at (m/p)².
     * Descend to gcd(ab, m) = 1 (ET applies) or to m = 1, where 4abcd = a + b + c is impossible.
     * Type I needs no descent, since 4abd = m²e + 1 forces gcd(ab, m) = 1.
     * Brute force (odd m < 80) confirms there are no solutions.

5. **MINOR — Prop 4.1(a),(b): "Over Q it is equivalent" is false as stated**
   * *Location:* §4 lines 283–286.
   * *Problem.* Q cannot prove the bounds x ≤ 3n/4, y ≤ 2nx, z ≤ nxy; it does not even prove commutativity. Also, ¬ES
     with unbounded ∃xyz is not Σ₁, so formalised Σ₁-completeness applies only to the Δ₀-bounded form.
   * *Fix.* Define ES by its bounded form (as Z58 Prop 2.1 does), or state (a)–(c) for T ⊇ IOpen. Also:
     * In (e), "non-standard" presupposes ES true at standard n: say so.
     * In (d), replace "S ≠ T" by "S is not a subtheory of T (T ⊬ Con(T))".

6. **MINOR — O'Rear sentence**
   * *Location:* §4 line 297.
   * *Problem.* "independent of ZF if ZF is consistent" needs ZF ⊬ ¬Con(ZF), i.e. Σ₁-soundness (or Con(ZF + Con(ZF))).
     Aaronson's verified Theorem 7 says only "ZF cannot prove the value of BB(748)", under the caveat "assuming O'Rear's
     construction is sound".
   * *Fix.* Reword to "unprovable in ZF if ZF is consistent; independent if ZF is Σ₁-sound".

7. **MINOR — §5 table header overclaims**
   * *Location:* §5 line 318, column "ES[non-square classes]" filled with "provable" in every row.
   * *Problem.* Only classes *solvable by polynomials* are proved (Thm B). For a general modulus, non-square classes outside
     ET's families are open (the memo's own O3).
   * *Fix.* Rename the column "ES[classes solvable by polynomials (all r ∉ 𝔐 mod 840)]".

8. **MINOR — overclaim: "unconditional version of B1 Thm C"**
   * *Location:* §6.1 lines 366–372; proposed FRONTIER text line 469.
   * *Problem.* Thm C (POINTWISE_SIZE) asserts that procedures fail at actual primes in ℕ, under H. Thm A says nothing
     about ℕ. It is a proof-theoretic *analogue*, not a strengthening, and "realises H internally" is metaphor.
   * *Fix.* Write: "the model-theoretic analogue of Thm C; it neither implies nor is implied by Thm C". Keep this under
     Assessment.

9. **MINOR — §2.7 Remark: false statement**
   * *Location:* lines 238–241.
   * *Problem.* "every standard divisor d of n+1 is ≡ 1 (mod 4)" is false. a₁ ≡ 1 (mod 8) gives 2 ∥ n + 1, so d = 2 is a
     standard divisor. The conclusion "never a u = 1 hit" is still right: the odd part of d is ≡ 1 (4) and the 2-adic part
     is ≤ 2, so d ≢ 3 (4).
   * *Fix.* Correct the statement and label the remark (PROVED, almost-sure).

10. **MINOR — §8 "Tied modulus": false statement**
    * *Location:* line 455, "their non-standard divisors are absent".
    * *Problem.* n + u = β₁ + u has the non-standard divisors (n + u)/k, for every standard k | ϕ(n + u).
    * *Fix.* Say that the non-standard divisors are (n + u)/k, and that their residues are again forced by the
      square-mimicking ϕ.

11. **MINOR — F3 row: ambiguous scope**
    * *Location:* line 26, "any element β with square-mimicking residue fails".
    * *Problem.* This is proved only for generators β_i (with an appropriate T-shift), not for arbitrary elements
      g ∈ M with ϕ(g) ∈ (Ẑ^×)².
    * *Fix.* Write "any generator β_i with positive leading coefficient".

12. **MINOR — Thm B proof details**
    * *Location:* line 253.
    * *Problems and fixes:*
      * The clearing factor must be (N!)³: the products have three Newton-basis factors. Write "(N!)³·(…)".
      * The parenthetical "(without positivity proviso … settled by exhibiting witnesses)" presupposes ES at those
        standard n < N₀. Add "true since ES is verified to 10¹⁷ ≥ N₀ (or check directly)".

13. **MINOR — §2.5 Type II: G not stated**
    * *Location:* line 161.
    * *Fix.* State explicitly that G must contain Y/n and Z/n, which are needed for ℓ² | y₀, z₀ and for integrality.

14. **MINOR — novelty claims**
    * *Location:* §8 lines 432 ("new"), 481 ("first such result at primes"); §2.7.
    * *Problem and fixes:*
      * Repo priors are correctly credited (BRAINSTORM C1: IOpen ⊬ ES_all at 1 + t; Z58 Thm 6.2: pseudo-squares, not
        primes). But the literature search on ES in weak arithmetic was "brief" (BRAINSTORM §2). Qualify: "first to
        our knowledge".
      * Cite Mohsenipour 2006 next to A′ (prior IOpen + GCD + cofinal-primes model).
      * Cite S. T. Smith, *Building discretely ordered Bezout domains and GCD domains*, J. Algebra 159 (1993), as the
        natural starting point for O1 (IOpen + Bez).
      * State that the q* = 1 case uses BO's model verbatim.

15. **MINOR — miscellaneous wording**
    * §5 Presburger/Skolem row (line 331): "ES is not expressible" is meaningless for a sentence, since a true or false
      sentence is equivalent to ⊤ or ⊥. Write "the natural formalisation uses + and · on variables".
    * §2.1 line 88: "(recursiveness … holds when q* is computable)" is unproved. Label it CONJECTURE/plausible, or drop it.
    * §2.6 line 186: Bezout fails "by degree". Better: uβ₁ + vβ₂ has no constant term.
    * §3: ET Prop 1.9 "lists" the classes → "essentially classifies (necessary families plus converse)".
    * §6.2: the TS-failure fact is PROVED but unlabelled inside a heuristic paragraph. Label it.

## Labels / hierarchy / attributions
* ES is never claimed proved.
* PROVED/CONDITIONAL/Assessment usage is correct except:
  * the A′ cofinality clause (issue 1);
  * the unlabelled §2.7 and §6.2 facts (issues 9, 15);
  * the readings that overclaim (issues 8, 10).
* Arithmetic-hierarchy classifications are correct: ES Π⁰₁; Goodstein, PH and hydra Π⁰₂; Con(T) Π₁.
* Literature statements match their verification status: Smith 1992 VERIFIED; PWW via Jeřábek VERIFIED; Buss–Krajíček
  Thm 5.3 VERIFIED; Aaronson Thm 7 VERIFIED with caveat; Friedman Π₁ examples NOT FOUND and correctly not claimed.

## Second (focused) review

Reviewer: hostile logic subagent (second pass). Scope: §2.8 Thm A″ and readings; §2.5 Remarks (generators, cofinal
counterexamples); §6 Prop 6.2 Type II descent/positivity; §4 Prop 4.1 (revised); §3 famcheck; §9 O1; §5 rows/lower bound;
§2.7 Caveat; whole-memo consistency. Sources: BO (pdftotext of the archived PDF: §1, stage Claim, Thm 4.3), ET (Prop 1.6,
Prop 1.9 family list, Props 2.2/2.6, §4).
Computations (under `ulimit -v 4000000`):
* `python3 scripts/z64_unprov_famcheck.py 4000`: 75 124 members, all primitive, 0 unit-square hits (0.4 s, not ~1 min).
* An independent check of the three ET Prop 1.9 families the script omits (T1b: −f mod 4ac ∩ −c/a mod f; T1c: −f mod 4cd ∩
  n² ≡ −4c²d mod f; T2b: −4a²d mod f with 4ad | f + 1), modulus ≤ 3000: 40 288 classes, 0 unit-square hits.

### Checked and sound (the attack failed)
* **Thm A″ (proof).**
  * Ring-language atoms are P = 0 with P ∈ ℤ[x̄], and Q_j = P_j(X̄) = 0 in M iff it is 0 in ℚ[β].
  * (F4) carries over to arbitrary residues a_i: b^α − a^α ∈ DẐ.
  * A nonzero polynomial does not vanish on a whole coset of Dℤ^K.
  * Specialisation is a ring hom that preserves every atom's truth value. Correct.
* **Shepherdson's model fails Th_∀(ℤ).** √2·t and t lie in S, and BO §1 even remarks that √2 is rational in S. Correct.
* **MRDP remark.** The logic is right: U_ES is a universal sentence of the ring language, true in ℤ iff ES holds.
* **Generator remark and f_m.**
  * Generator system: f_m is linear and monic in β₁, so ℚ[f_m, β₂, …] = ℚ[β].
  * Residue: ϕ(f_m) = q* + 0, since ϕ(β₂) = ϕ(β₃).
  * Positivity: β₁ > 0 and (β₂ − β₃)² > 0, because β₂ ≠ β₃ (p₃ is at infinite distance from M₂ ∋ β₂).
  * Primality: f_m is irreducible and ϕ(f_m) is a unit, so (F1) applies.
  * Unboundedness: the x-degree is ≥ 2m·deg β₂ → ∞.
  * Generalised Lemma 2.3:
    * ψ is a hom because γ is a generator system.
    * g(Γ(ξ)) is the Puiseux polynomial g(γ) ≠ 0, so (b) is unchanged.
    * The algebra in (c) is right. Γ₁′ is a nonzero generalised polynomial with finitely many positive zeros, and it is
      eventually > 0 because γ₁ is positive and infinite.
  * (F4) and the Type I/II steps work in γ-coordinates, since ℓ² ≡ ϕ(γ₁) and b′_j ≡ ϕ(γ_j) mod D.
* **Prop 6.2.**
  * Positivity propagation is correct for both systems: 4abd = ne + 1 ≥ 1 and 4abd = n + e ≥ n > 0 at the largest zero,
    then ce = a + b.
  * The Type II descent algebra is checked: 4(a/p)(b/p)d = (m/p)² + e/p², and (cp)(e/p²) = a/p + b/p.
  * ET's omitted Type II argument (4abd = n + e ⇒ (−e/q) = (n/q)) does need gcd(ab, m) = 1, so the descent is necessary.
    The descent is sufficient: m = 1 has no solution, since e ≥ 4ab − 1 > a + b.
  * The GCD-step proof matches ET Prop 2.2's proof line by line.
* **Prop 4.1(a).** The bounds are derivable in discretely ordered rings:
  * 4x ≤ 3n from yz(3n − 4x) ≥ 0;
  * z(4xy − ny − nx) = nxy forces 4xy − ny − nx ≥ 1, hence z ≤ nxy;
  * z ≥ y gives y(4x − n) ≤ 2nx with 4x − n ≥ 1;
  * z ≤ 9n⁴/8.
  (b)–(e) are correct for the corrected ES_b (issue 4).
* **§2.7 Caveat.** Mathematically right: f(y², B′) has an absolutely irreducible factor ≠ y, Lang–Weil at split ℓ gives
  P ≫ 1/ℓ, and Borel–Cantelli II applies. The β_i, i ≥ 2, are a.s. non-units at infinitely many ℓ.
* **famcheck logic.** Correct. If a polynomially solvable class ρ mod Q were a unit square, it would contain a
  square-mimicking q*. Thm A would then give an infinite prime ≡ ρ in a model of NOI ⊇ IOpen failing ES, while Thm B
  (form without the proviso; the prime is ≥ N₀) gives IOpen ⊢ ES there. "ρ unit square mod Q" is exactly the condition.

### Issues

1. **MAJOR — §2.8 title and third Reading overclaim "all true Diophantine non-existence facts"**
   * *Location:* §2.8 heading ("All true Diophantine non-existence facts hold in M_ϕ"); third Reading bullet ("What a
     proof must use is therefore not any stock of true Diophantine non-existence facts").
   * *What A″ actually covers.* Only Th_∀ of ℤ in the ring language. Facts about natural numbers, or with positivity
     constraints, enter only through the four-square encoding, and inside M_ϕ that encoding does *not* express positivity.
     M_ϕ ⊭ Lagrange: β₁ > 0 is not a sum of four squares in ℚ[β], since Σa_i² has even degree because real top forms do not
     cancel (the TS argument of §6.2).
   * *What it misses.* The ordered/ℕ universal theory, Th_∀(ℕ; +, ·, ≤) on M⁺, is untouched. So is the ES-relevant ordered
     form of T1 itself, ∀s, u, B, C ≥ 1 (4uBC − u − B ≠ s²). Thm A only gives ¬ES★(β₁), and β₁ is not a square. Whether M⁺
     satisfies that sentence is open.
   * *Fix.*
     * Retitle: "All true universal ring-language facts of ℤ hold in M_ϕ".
     * Reword the Reading: "not any stock of true Diophantine non-existence facts *over ℤ in ring form*; ordered/ℕ-forms
       (e.g. T1 as an ordered universal sentence) are not covered, and M⁺ ⊨ Th_∀(ℕ) is OPEN".
     * Add the one-line PROVED remark "M_ϕ ⊭ Lagrange". This is also the precise reason the MRDP remark's "formulation
       matters".

2. **MINOR — §2.8 CONDITIONAL parenthetical misnumbered**
   * *Problem.* It lists three conditions (ES true, MRDP in IΔ₀ + exp, Lagrange in IΔ₀ + exp), then says "The first is
     Gaifman–Dimitracopoulos … the second is standard".
   * *Fix.* Write "the second … the third".

3. **MINOR — A″ prior art**
   * *Problem.* The proof is the standard "finitely generated subrings are residually ℤ, so M embeds in an ultrapower of ℤ"
     argument.
   * *Directly relevant, uncited:* Otero, *On Diophantine equations solvable in models of open induction*, JSL 55 (1990)
     (BO ref [Ot1]; `lit_models.md` §6), and Otero, *Quadratic forms in normal open induction*, JSL 58 (1993).
   * *Fix.* Cite both, and call A″ "elementary; plausibly folklore".

4. **MINOR — §4 Prop 4.1: the displayed ES_b omits x, y, z ≥ 1**
   * *Problem.* "∀n ≥ 2 ∃x, y, z ≤ 2n⁴ (4xyz = n(xy + yz + zx))" is trivially true with x = y = z = 0. As written, (b)
     ("if ES is false then Q ⊢ ¬ES_b") is false.
   * *Fix.* Write ∃ 1 ≤ x, y, z ≤ 2n⁴.

5. **MINOR — §3 famcheck**
   * (i) *Coverage.* It covers only 4 of ET Prop 1.9's 7 families. Add T1b, T1c, T2b (my run: 40 288 classes ≤ 3000,
     0 hits).
   * (ii) *Strength.* A hit is already excluded by ET Prop 1.6: every family member gives Type I/II solutions at the odd
     squares of its class. So the script tests the family encoding and ET 1.6, not Thm A against Thm B independently. Say
     "sanity check".
   * (iii) *Runtime.* It takes 0.4 s, not ~1 min.

6. **MINOR — summary text lags behind the theorems**
   * (a) *§0 F1 row.* It lists "Bezout/GCD-level" as candidate principles, but GCD is excluded by Thm A′. Also add GCD and
     Th_∀(ℤ) to "not enough".
   * (b) *§8 and FRONTIER text.*
     * "What was proved" and the proposed FRONTIER text omit Thm A″.
     * The FRONTIER text cites "BO Thms 4.2–4.3", but Thm 4.3 is not used (headline reliance list).
     * It says "BO's recursive normal model". Recursiveness is unchecked for q* ≠ 1, which is needed for every square class
       not containing 1 (e.g. 121 mod 840), and the A′ model (random residues) is not recursive. Drop "recursive".
   * (c) *§5 lower bound.*
     * "It must exceed both …": the theories are not linearly ordered. Write "it is contained in neither".
     * "Equivalently, … a principle failing in M_ϕ" is an implication, not an equivalence.
     * "Strictly above NOI + GCD" (the window) and the Bottom line's "between NOI + GCD and IE₁" should read
       NOI + GCD + PD + Th_∀(ℤ).
   * (d) *§0 F3 row.* Also state the Remark's condition (2): the complementary generators must have ϕ(γ_j) ∈ Ẑ.

7. **MINOR — §2.7 Caveat unlabelled**
   * *Problem.* The proof sketch is correct, but the Caveat carries no label.
   * *Fix.* Label it "(PROVED, sketch; almost surely)", and write "f not associate to β₁" instead of "f ≠ β₁".

8. **MINOR — §9 O1 Assessment wording**
   * *A¹-bundle.* Spec ℚ[B][u, v]/(ug + vh − 1) is an A¹-bundle only over D(g) ∪ D(h), the complement of the codim-2 set
     V(g, h), not over the whole previous stage.
   * *Unstated arc-side requirement.* The integer Bezout pair at b must be ≡ (ϕ(u), ϕ(v)) mod D. This is achievable: the
     syzygies of a unimodular row mod D are generated by (h, −g). It should be said.

### Verdict
* No FATAL issue. The new mathematics is correct: Thm A″ as stated (ring language), the f_m cofinality with the
  generalised Lemma 2.3, the Prop 6.2 Type II descent and positivity, the revised Prop 4.1 bounds, the §2.7 Caveat, and the
  famcheck logic.
* One MAJOR issue is an interpretive overclaim. §2.8's title and Reading extend A″ from ring-language ℤ-facts to "all
  Diophantine non-existence facts". Positivity-constrained (ℕ/ordered) facts, the form T1 takes, are not covered, and
  M_ϕ ⊭ Lagrange.
* Seven MINOR issues: one definitional typo (ES_b), one misnumbered conditional, famcheck coverage and strength, prior art,
  and summary sections not updated for A′/A″.
* Labels are otherwise right. ES is never claimed.
