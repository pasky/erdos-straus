# REVIEW_UNPROV_ASTRA — hostile retro cross-model review

Reviewed `Z64_UNPROV.md` at `311454873d4461d48afbffbc29f4470a59dd5471`. **ES remains OPEN.**
Verdict: **ACCEPT-WITH-FIXES**. The prime-countermodel headline survives; several interpretations do not.
Independent derivation, not adoption of `REVIEW_UNPROV.md`: I read the archived Berarducci–Otero (BO) PDF in full;
ET `sources/elsholtz-tao-1107.1010.pdf`, definitions, Props 1.6/1.9/2.2/2.6 and §4; Z57 Lemma A.1;
Z58 Remark 6.3; the memo's scripts, data and earlier reviews. BO references below use its author-PDF numbering.
Also checked Aaronson's author PDF Thm 7, Buss's *Axiomatizations* Thm 5, and Buss–Krajíček §5 Thm 5.3 from source.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| §2.1 BO construction with arbitrary integral residues | CORRECT | Stage discreteness/normality and eventual integer-part coverage survive; no recursive presentation is required. |
| F1/F3: β₁ is prime **in M**, not merely in ℚ[β] | CORRECT | Unit residue makes division by β₁ stay in M; units of M are ±1. This proves more than the defined irreducibility predicate. |
| F2/F4: residues and integer specialisation | CORRECT | Clear one common coefficient denominator; congruence in Ẑ plus rationality gives an integer. |
| Lemma 2.3: analytic interpolation | CORRECT | Exponentially small perturbations cannot change the eventual sign of a nonzero nonnegative-exponent Puiseux polynomial. |
| Lemma 2.4: positivity propagation | CORRECT | At the last zero, positive reciprocal terms cannot cancel; the ★ variant also contradicts N>0 directly. |
| A(ii): transfer of the Type I/II obstruction | CORRECT | The CRT step preserves precisely ET's coprimality, not just divisibility; see reconstruction below. |
| A(iii), Cor A.1, nonprovability of MS★/MS | CORRECT | Integer ★ specialisation contradicts Z57 A.1(b); Hit equivalence works in IOpen. No assumption that M satisfies universal T1 is used. |
| §2.5 changed generators and cofinal counterexamples | CORRECT | The triangular change is invertible; f_m has unit square residue and unbounded x-degree. Eventual positive derivative supplies the new arc. |
| §2.6 PD, failure of Bezout and GCD | CORRECT | Unit products in finite adeles force each polynomial factor to be an adelic unit; rational rescaling works. The two failure examples check. |
| A′: simultaneous NOI+GCD+PD | CORRECT | Local algebraic independence and the summable codimension-two estimate coexist. The valuation formula really gives a gcd. |
| §2.7 no-cofinal-primes caveat; n+1 remark | CORRECT at stated scope | The caveat is only a sketch; split-prime/Lang–Weil reasoning supports it. The n+1 argument includes nonstandard cofactors and 2∥n+1. |
| A″: all true universal **ring** sentences | CORRECT | Finite simultaneous discrimination by integer evaluations suffices; no order-preserving specialisation is asserted. |
| A″ readings: Shepherdson, four squares, TS, U_ES | CORRECT / CONDITIONAL | Degree arguments check. U_ES retains its explicit formalisation hypotheses. The “f.g. subrings embed in ℤ” description is WRONG. |
| B: polynomial identities imply IOpen provability | CORRECT-WITH-FIX | The stated real-positive version is sound; the purported finite verification for arbitrary N₀ is unjustified. There is a complete repair below. |
| Cor C; certificate/family counts | CORRECT; CERTIFIED | 186 of 192 primitive classes covered; exactly six unit squares remain. Both committed outputs replay identically. |
| Prop 4.1(a)–(e) | CORRECT with standard proof predicates | Bounds and formalised Σ₁-completeness check. The subsequent inference from **one-sided** unprovability to ES truth is WRONG. |
| Prop 5.1 and corrected bounded-arithmetic rows | CORRECT | Tagged solution-or-factor witnesses are polynomially bounded; S¹₂ witnessing and S²₂→T¹₂ conservation give the stated consequences. |
| Prop 6.2 arc criterion | CORRECT, with proof clarification | The GCD Type II sketch completes algebraically. Without GCD, do not silently identify irreducibility with ring-primality; the endpoint gcd hypothesis supplies the needed split. |
| Prop 7.1, true-instance proof length | CORRECT at stated efficient-arithmetic scope | Short witnesses yield short verification proofs; the following claim that NOI proves **each** prime instance lacks the essential “true” qualifier. |
| F1–F4 and overall “strengthened (logic)” verdict | CORRECT at theorem scope | F1 is an external integer obstruction, F2 is a subset obstruction, F3 uses genuine internal primes, F4 asserts no positivity. No HOT LEAD follows. |

## Stress test of the headline

1. **Model construction.** BO Lemmas 2.6–2.9 and the stage Claim allow any homomorphism to Ẑ. Its restriction to each
   stage lands there by construction. Lemma 2.4 makes selection depend only on ℚM_i=ℚ[β₁,…,β_i], not the residues.
   For integer-part coverage, each enumerated Puiseux polynomial becomes eligible once its coefficients belong to K_i;
   only finitely many earlier entries can then delay it. Finite distance can be adjusted by a standard integer.
   BO 2.3/1.1 therefore give OI, and normality persists. Starting the enumeration with x is legitimate.
2. **Primality is not smuggled through specialisation.** In the polynomial UFD, β₁|gh implies β₁|g or β₁|h.
   If g=β₁h, then ϕ(h)=ϕ(g)/q*∈Ẑ, so h∈M. Also β₁ is not invertible and rational units of M are exactly ±1.
   Thus the nonstandard element satisfies the memo's Prime formula. Its integer image ℓ² is deliberately NOT prime.
3. **The non-square model prime really specialises to the forbidden square type.** Three divisible denominators
   give 4=1/X′+1/Y′+1/Z′≤3, because positive quotients are ≥1 in M. In Type I, avoid the nonzero constant-term
   product Y₀(b′)Z₀(b′) on the residue lattice. Put coefficient denominators into D and avoid its numerator primes
   by CRT when choosing odd ℓ. Every prime dividing ℓ then sees Y(ℓ²,b′), Z(ℓ²,b′) as units. Include X/n in F4.
   For Type II do the same with X₀ and include Y/n,Z/n. Thus the integer endpoint has exactly ET's required type.
4. **Signs cannot escape the obstruction.** The arc is injective by its Puiseux asymptotics, starts at the chosen
   integer evaluation, and keeps n positive throughout. At a last denominator zero, Σ1/F_i blows up positively
   while 4/N stays bounded. Hence the endpoint coordinates are positive integers. ET Prop 1.6 applies to odd
   squares, not just primes. This is external ordinary arithmetic; it does not require reciprocity inside M.
5. **A′ adds genuinely simultaneous axioms.** For each fixed coprime polynomial pair, the resultant argument gives
   O(ℓ^{k−2}) common zeros outside finitely many primes (k=1 is the nonzero constant resultant case).
   The square restriction on a₁ multiplies probabilities by at most 3, so Borel–Cantelli gives G2, alongside G1.
   For g=Gg₁,h=Gh₁, min(v_ℓ(g₁),v_ℓ(h₁)) has finite support, including any negative valuations.
   Rational scaling of G gives d with v_ℓ(d)=min(v_ℓ(g),v_ℓ(h)); every common divisor divides d in M.
6. **A″ is compatible with failure of ES.** Given finitely many atoms, avoid the product of their nonzero polynomial
   evaluations on one integer residue lattice. This preserves all equalities AND inequations, proving Th_∀(ℤ).
   It does not preserve arbitrary inequalities. In particular β₁ cannot be a sum of four polynomial squares;
   the ring-universal encoding of a natural-number statement need not retain its meaning in this model.
7. **Arc criterion completion.** In Type II, take d=gcd(X,Y/n,Z/n), write the primitive triple as ab,ac,bc,
   and cancel to obtain 4abcd=nc+a+b. Thus c|a+b, e=(a+b)/c>0, and 4abd=n+e. This uses GCD-domain Euclid,
   not unique factorisation. At the integer endpoint the memo's descent removes gcd(ab,m)>1 correctly.
   For the non-GCD clause, include all existing denominator/n quotients in G. If m>1, endpoint coprimality
   excludes zero n-divisible denominators; three are impossible by the same ≤3 argument. If m=1, ES fails outright.

## Recomputed certificates

Both runs used `ulimit -v 4000000`, tool timeout 1800 s, and uv:
`uv run --with sympy python scripts/z64_unprov_mordell840.py`; `uv run python scripts/z64_unprov_famcheck.py 4000`.
The 840 output is byte-identical (SHA256 `8b7105a2dffe529725c09e9e1317252f445990f82bc39bd2d33a3080aafccbfe`):
627 generated members, eight needed identities, 186 covered primitive classes, complement {1,121,169,289,361,529}.
The four scaling identities cover the other 648 classes. I checked the symbolic identity, finite-difference
integrality and real-root positivity checks in the code, not merely its printed coverage count.
Famcheck is byte-identical: 75,124 primitive family members, zero square-class hits. It tests encoding consistency,
not the model theorem. The prior review's additional 40,288-family count is not needed for, or recertified by, this review.

## Required fixes, priority order

1. **Do not assert ES instance truth.** §5's Q row must say “each TRUE instance”; §7 must say NOI proves every TRUE
   ES(p̄) instance in the stated bound, or explicitly condition on ES. Unqualified “each” would already imply ES in ℕ.
2. **Separate unprovability from independence** (§4 last Assessment; §8 “out of reach”). Prop 4.1(c) concerns
   T⊬¬ES, NOT T⊬ES. A proof of independence implies ES and Con(T); a proof only of T⊬ES implies Con(T), not ES.
   If ES were false, Con(T) plus its finite counterexample would itself prove T⊬ES. Also S need not contain PA:
   replace “S⊋PA” by “S is not a subtheory of PA” under the stated incompleteness assumptions.
3. **Delete the general n+u divisor claim** (§8 B2). It is valid for standard u, not arbitrary u∈M. Take
   t=⌊√n⌋+1 and u=t²−n>0. Then n+u=t² has the nonstandard divisor t, not (n+u)/k for any standard k.
   This counterexample even has u=O(√n)<n. A(ii)/(iii) still exclude solutions; the proposed divisor explanation fails.
4. **Repair B without assuming a finite ES check beyond its range.** No bound N₀≤10¹⁷ is supplied. Instead apply
   Lemma 2.4 to F_i(s)=P_i(ε+s), N(s)=ε+s for every ε>0: eventual positivity forces positivity on ALL t>0.
   Eventual integer values on qk+r extend to all integer k by finite differences. Thus B actually needs no positivity
   proviso or appeal to unperformed small-instance checks; the general-class summaries can be justified this way.
5. **Fix A″'s folklore description.** Finitely generated subrings do NOT embed in ℤ: ℤ[β₁] alone cannot.
   Say “finite sets of nonzero elements can simultaneously be preserved by homomorphisms to ℤ” (discrimination).
6. **Keep necessity claims at their proved scope.** §6.1 must name NOI+GCD+PD when listing PD among the tools;
   no derivation of PD from NOI+GCD is supplied. §6.2's reading and §8's final “must use divisor-richness or counting”
   overreach: failure of the sufficient arc criterion need not mean absence of integer points, and the theorem forces
   only some principle false in these models, not a specified mechanism. Two-/four-square principles are already alternatives.

**Final verdict: ACCEPT-WITH-FIXES.** A/A′/A″, internal primality, T1 specialisation and Cor C withstand the hostile check.
B has the complete repair above. No claim of ES truth, strong-theory independence, or exclusive proof mechanism is licensed.
