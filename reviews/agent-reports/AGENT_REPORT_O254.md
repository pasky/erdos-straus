# AGENT REPORT O254 — joint-factorisation families for every prime (hatch H-A, direction 3)

Branch side-agent/joint-budget. Main file JOINT_BUDGET.md; memos BRAINSTORM/z26_*.md (6); scripts
scripts/z26_checks.py, scripts/z26_cyclo_depth.py; outputs data/z26/ (2 small text files).
**ES is not solved; no new infinite case of ES is claimed.** Outcome: the fallback, a precise obstruction theorem with
exact scope plus several small new lemmas. No positive family was found.

SHARP: (mild; flag only if useful)
* **Theorem A (side irreducibility, PROVED, elementary):** when p is a free variable, every ES side number of the RT2
  slice table, with slice parameters any polynomials in an auxiliary vector u, is (p-free content) × (irreducible in
  ℚ[u, p]). The only non-trivial input is d > 0: with signed slices (d = −w²) the Type I side p² + 4c²d splits
  identically (Remark 1.2). So "positivity" is exactly what forbids an algebraic budget at a general prime; every
  thin-family success ((J)74/(J)75/(J)80) needs p = φ(u).
* **Prop 4.2 (PROVED):** every window built from ℤ[√p] (CF norms of √p with gcd(Q_k, m) = 1, near squares m = w² − p,
  any m | A² − pB² with gcd(B, m) = 1) has (p/m) = +1, i.e. is never Jacobi-forced (p + m = c·w² is forced iff (c/p) = −1:
  the non-residue must come from c, an (R2) choice). A clean structural reason for near-square
  hardness.
* **Prop 4.3 / Remark 4.4 (PROVED):** p is a non-square modulo every Type II class modulus 4ab (so no class modulus
  divides p − 1, and ord_{4ab}(p) is always even). Auxiliaries that hand over divisors of p − 1 (ord_p(g), Lucas ranks,
  Pocklington data) pin p to the sterile point n = 1 locally.

## What was done (iteration log in JOINT_BUDGET §0)
1. §1 Theorem A + Cor A.1 + Remark 1.3: polynomial auxiliaries with p free give only u-indexed ET congruence classes
   (firing = moving-modulus event, B2).
2. §2 Prop 2.1: relations p = φ(u): r = 1 thin; φ* irreducible ⇒ (J)79 collapse; φ linear in a variable with non-constant
   coefficient ⇒ firing is α(u′) | p − ψ(u′) (B2); residual: φ* reducible and degree ≥ 2 in every variable (no claim).
3. §3 Lemma 3.1 (certificates supported on a congruence-forced factor pin the window: one ET class), Prop 3.2 (Kneser
   threshold: Σ_{s∉H} 2v_s(K) ≥ [H₀:H] − 1 ∀H ⇒ Σ_m(K) = H₀, hence Type II at a Jacobi-forced prime window), Cor 3.3
   (structure-free needs 2Ω(K) ≥ m − 2; budget gap log m vs m — gap statement partly Assessment).
4. §4 non-polynomial auxiliaries: reciprocity gives a coset only (4.1); ℚ(√p)/archimedean windows unforced (4.2);
   Fermat-type anti-forcing (4.3, 4.4); bounded cyclotomic menus = Thm C (H).
5. §5 Theorem 5.2 (JF trichotomy, exact scope, with the uncovered residual listed). §7 budget table.
6. Numerics (§6): Theorem A sympy (0 violations), Kneser brute force (374/374), Prop 4.2 on 368 689 windows (0
   violations after restricting to the stated hypothesis gcd(m, p) = 1 — the first run's 5 flags were p | m), Remark 4.4
   on all 3188 Type II points p < 3000; cyclotomic depth k*(p) over all 28 153 Type II points of the 765 Mordell-hard
   primes ≤ 3·10⁵ (each checked exactly, p non-square mod 4ab at every point; T1 control: no odd square ≤ 3·10⁵ has a
   Type II point): always even, growing in range (k* = 72 at p = 210 961).

## Self-review (codex deep review before reporting; all repaired)
Theorem A restated for the numerators of the divided rows; Cor 3.3 and Thm 5.2(c) now say the counting criterion (3.1) is
sufficient only (box fills by luck: p = 809, m = 31, K = 210); Thm 5.2(a) restricted to identities in free X ((R3) is a
relation type); (R3) restricted to c = 1 / norm windows with gcd(B, m) = 1 (general c forced iff (c/p) = −1); 5.2(b) r = 1
needs deg φ ≥ 2; 5.2(c) "never determines" restricted to m ≥ 7; C_k = {ord | k}; cyclotomic script now checks
non-squareness at every point, cap raised to 400 (k* = 72 exact at 210 961); "unbounded" → "growing in range".

## Labels / honesty notes for the reviewer
* Most results are elementary; Theorem 5.2 is largely a *synthesis* of Theorem A + (J)79 + (J)83 + POINTWISE_SIZE Thm C
  + new Props 3.2/4.2/4.3. Its novelty is the organisation and the three small new statements, not depth.
* Lemma 3.1 is near-tautological (stated so); Cor 3.3's "exponential gap" sentence is Assessment.
* Prop 3.2 is a direct application of Kneser's theorem; (J)69/s6 already noted the Cauchy–Davenport version.
* Nothing in §5 covers residual (R1d), growing k₀, or the (J)64 regime with structured K.
* Not done: Type I analogue of the cyclotomic-depth statistic (expensive factoring); 10⁶-range runs (no positive claim
  needed them).

## Proposed ledger line
(J)84 JOINT_BUDGET (O254): no algebraic budget at a general prime — Theorem A (ES sides irreducible over any polynomial
auxiliary when p is free; positivity is the obstruction), JF trichotomy (Thm 5.2), ℚ(√p)-windows unforced (Prop 4.2),
p non-square mod every Type II modulus (Rem 4.4); EVIDENCE: cyclotomic depth unbounded. Assessment: H-A needs an
auxiliary not of polynomial / character / ℚ(√p) / divisibility type; none known.

## Sparks (not pursued)
1. Residual (R1d): search exhaustively for non-collapsing polynomial ET families over φ ∈ ℤ[u₁, u₂] with reducible top part
   and degree ≥ 2 in each variable (e.g. φ = u₁²u₂² + lower). A family over a φ that represents a positive-density set of
   primes would be the first non-thin JF family.
2. Signed→positive transfer: the signed Type I side (d = −w²) splits as (p − 2cw)(p + 2cw) with known residues; is there a
   Vieta/reflection move carrying a split signed point to a positive point (cf. (J)52)?
3. Composite Jacobi-forced windows: with several inert primes ℓ | m, the box condition splits over CRT components; does
   Prop 3.2 per component need less than 2Ω(K) ≥ m − 2?
4. Cyclotomic depth k*(p): study v₂(k*) against p mod 2^j and against the least non-residue; k* growing like log p would
   make C_{≤C log p} a natural growing menu just outside Thm C.
5. Higher reciprocity (cubic/quartic symbols at windows m ≡ 1 (3)/(4)) fixes more of H₀/H₀^ℓ; quantify how much of the
   Kneser threshold that saves.
