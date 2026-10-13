# R196 — independent hostile review of FROBENIUS_FIRING.md (O196)

Reviewer: R196 side agent (branch side-agent/review-frobenius), independent of the author's self-review (the "R196 #k"
markers already in the file are the author's own deep-self-review repairs, not this review).
Document reviewed: FROBENIUS_FIRING.md at merge of side-agent/frobenius-firing.
From-scratch scripts: `scripts/review_frob_*.py` (own integer factorisation/primality, own F_q arithmetic; nothing
imported from `ff_frob_*` or `fm_poly`).

(Review in progress — sections are filled in one claim at a time.)

## Summary verdicts

* **Thm 4.2 (ES^{(y)} for every odd n > 1; Type II shape at every non-square; exact-T1): SOUND** (PROVED relative to
  UNIT_ORBIT Lemma 2.2, as labelled). Re-derived independently:
  - *Class choice.* M = 4·rad(n)·s₁…s₄ with a ≡ 3 (4), a ≡ −1 (s_i), a mod rad(n) as in UNIT_ORBIT Thm 2.4(a)
    (a ≢ 0, 1 mod ℓ | n, Jacobi (a/n) = −1 via ℓ₀ ≥ 5). CRT-compatible (s_i ∤ n odd, −1 ≡ 3 mod 4 consistent), and
    every hypothesis of Lemma 2.2 holds: gcd(a, M) = 1, a ≡ 3 (4), a ≢ 1 mod each odd ℓ | M (for ℓ = s_i: −1 ≢ 1
    since s_i odd). Lemma 2.2's sieve sifts only ℓ ∤ M; the s_i never divide (r − 1)/2 (r ≡ −1 mod s_i), so nothing
    changes in the sieve.
  - *Reciprocity.* (r − 1)/2 odd ⇒ (s/r) = (r/s)(−1)^{(s−1)/2} = (−1/s)(−1)^{(s−1)/2} = ((−1)^{(s−1)/2})² = 1.
    So Γ_r ⊆ (F_r^*)², which has odd order (r − 1)/2; a proper subgroup has index with an odd prime factor
    dividing (r − 1)/2, hence ≥ x^{1/4−ε}; |Γ_r| ≤ x^{3/4+ε}; Lemma 2.3 (k = 4) gives ≪ x^{(3/4+ε)·5/4} = o(x/log²x)
    for ε < 1/20 (15/16 + 5ε/4 < 1). Since Γ_r = (F_r^*)² has odd order, Q ↦ Q² is a bijection of it, so −n/4 = Q²
    with Q ∈ ⟨S⟩ (non-negative exponents, finite group). r ≠ s_i, r ∤ n automatic.
  - *Solution.* Prop 2.1: z = n·x·((r+1)/4)/Q² has denominator dividing Q², even s-adic valuation when negative
    (re-derived: 4rx = n(r+1) + 4Q², σ = v_s(r+1) < 2c ⇒ v_s(x) = σ, v_s(z) = 2σ − 2c); s_i odd and s_i | r + 1 ⇒
    s_i | (r + 1)/4 | y; s_i ∤ 2n. Type II shape at every ℓ | n inherited from Prop 2.1. n ≡ 3 (4): Q = 1, z ∈ ℤ.
  - *(b)* An ES^{(y)} solution is an ES^{(S′)} solution, S′ := {ℓ : v_ℓ(z) < 0} (odd, prime to n, even
    valuations); Lemma 1.1/Cor 1.2 of UNIT_ORBIT need exactly these hypotheses (x, y ∈ ℤ, z ∈ ℤ[1/S′], parity).
    The statement correctly says "Type I/II shape at *every* prime of m" (consistent with UNIT_ORBIT's R186 m2 repair).
  - *(c)* n = t^{2^j}, t not a square, k = n/t; primes of den(kz) = primes of den(z) (they are prime to n ⊇ primes
    of k), parity unchanged, ℓ | y ⇒ ℓ | ky. S must be chosen prime to n (= prime to t, same radical) — it is.
  - Not trivial: (b) shows ES^{(y)} has the same exact T1 as ES^{(S)}, so no Type-I/II polynomial covering can prove
    it (UNIT_ORBIT Rem (4) transfers), i.e. the sieve is genuinely needed.
  - Numerics (own code): see Checks. Only label/wording issues (m1, m2 below).

* **Cor 4.3 (shot family: ES^{(y)} ⇔ rad(Q) | (r+1)/4; ES ⇔ Q | (r+1)/4): SOUND** as a statement about the
  Prop 2.1 solution. Re-derived: v_s(z) < 0 ⇔ σ < c (for c ≤ σ < 2c, v_s(z) = 2σ − 2c ≥ 0 — the author's proof
  states this correctly); ES^{(y)} at s then needs s | y = n(r+1)/4 ⇔ σ ≥ 1 (s ∤ n). So ES^{(y)} ⇔ ∀ s | Q:
  (σ ≥ c or σ ≥ 1) ⇔ σ ≥ 1 ⇔ rad(Q) | r + 1 ⇔ rad(Q) | (r+1)/4 (rad(Q) odd). ES ⇔ ∀ s | Q: σ ≥ c ⇔ Q | (r+1)/4.
  Brute-force test (own code, S = {3,5,7,11}, 1568 random shots incl. 38 ES^{(y)}-but-not-ES and 72 ES cases):
  0 mismatches of either equivalence, and every shot is an ES^{(S)} solution. The interpretive tail ("exactly the
  B2 obstruction", Kummer–Chebotarev reading) is Assessment, not part of what is proved (m2).

* **Thm 4.4 (GRH, one mute prime, ES^{(s)} and ES^{(y)}): SOUND as CONDITIONAL, citation-level** (label correct).
  The set is exactly Lenstra's M(K = ℚ, F = ℚ(ζ_M), C = D, W = ⟨s⟩, d = 2): r ≡ 3 (4) forces 4 ∤ r − 1, so
  "s is not an ℓ-th power residue for every odd ℓ | r − 1" ⇔ [F_r^* : ⟨s⟩] | 2 (Lenstra, Invent. Math. 42 (1977), as
  summarised in Moree's survey §9.5, sources/uo/moree-artin-survey-2012.pdf; I could NOT access Lenstra's paper itself,
  so the GRH density theorem is accepted at the level of that summary; Moree gives pages 202–224, the document 201–224).
  Re-derived the Galois part: for m odd squarefree and s prime, Gal(ℚ(ζ_m, s^{1/m})/ℚ) = ℤ/m ⋊ (ℤ/m)^*, whose
  commutator subgroup is all of ℤ/m (for each ℓ | m take u ≡ 2 mod ℓ: u − 1 a unit), so the maximal abelian
  subfield is ℚ(ζ_m) and ℚ(ζ_M) ∩ ℚ(ζ_m, s^{1/m}) = ℚ(ζ_{gcd(m,M)}); c_m = 0 unless gcd(m, M) = 1 because every
  a ∈ D has a ≢ 1 mod each odd ℓ | M; then linear disjointness gives the Euler product. Also checked that the
  conditions are automatically met at odd ℓ | M (ℓ ∤ r − 1). **Numerical test of the density formula** (own code,
  r < 3·10⁵, `scripts/review_frob_density.py`): (n, s) = (13, 3), (13, 5), (85, 3), (17, 7), both variants — predicted
  δ vs observed: .1129/.1145, .0495/.0492, .1486/.1496, .0815/.0814, .0320/.0327, .1602/.1606; and for every counted
  r, −n/4 ∈ ⟨s²⟩ mod r (0 exceptions). Only defect: the scope sentence (m3).

* **Prop 1.2 (Fire(p) finite ⇒ no sufficient Frobenius condition): (a), (b) SOUND; (c) GAP (not a statement).**
  (a) is cited (FIXED_MODULUS_SHOTS Prop 6.1, FF_MUTE Prop 5.1, both reviewed); I re-derived the Type I bound
  (wf ≤ 2p/3, g | p² + 4wf² ⇒ g ≤ 25p²/9 < 3p²) and brute-forced the Type II bound h ≤ (p+1)(p+5)/4 for all primes
  p < 400 (0 violations, `review_frob_heegner.py`). (b) is immediate from Chebotarev (constant-field part handled
  correctly: infinitely many degrees in any residue class mod e). (c) names no (L, C) — "C = {Frob restricted as in
  Lemma 3.2}" plus "s primitive root" is a heuristic description, yet sits inside a PROVED proposition (m4).
* **Thm 1.3 (FF effective no-go): SOUND, CONDITIONAL label acceptable (could be PROVED-relative-to-citation).**
  Logic re-checked: geometric L ⇒ the Chebotarev count at every degree d has main term (|C|/|G|)q^d/d with error
  ≪ (|C|/|G|)(g_L + |G|(1 + deg 𝔡_L))q^{d/2}/d + (ramified primes, ≤ deg 𝔡_L/d) — the shape is the standard one
  (Murty–Scherk; Fried–Jarden Prop 6.4.8 has an extra |G|(2g_F + 1)q^{d/4} term, harmless with g_F = 0); sources
  not in sources/, not re-read. Every degree-d prime fires only if the count vanishes, impossible for
  q^{d/2} > c₀(…) as no prime of degree ≥ 2n − k + 1 is a Type II modulus. AGENT_REPORT calls it "unconditional"
  (m5).
* **Thm 1.4 (ℤ, GRH, range-restricted no-go): SOUND as CONDITIONAL.** Re-derived the arithmetic: with the Serre
  (1981, Thm 4) GRH form, Li(X) − Li(X/2) ≥ X/(2 log X), the first alternative failing gives bracket ≥ X/(6 log X);
  |Fire(p)| ≤ p^{1+o(1)} (Type II: Σ_{x ≤ p/2} τ(x²); Type I: (w, f) with wf ≤ 2p/3 times τ(p² + 4wf²)) — fine (Elsholtz–Tao
  give even p^{3/5+o(1)} for all solutions). The final "in particular" checks out: X^{1/2}/log²X ≥ √3p/log²(3p²) ≫
  p^{1−ε}, and X/(6 log X) ≥ p^{2−o(1)} > p^{2−ε+o(1)}. Note: for X ≥ 3p² the window (X/2, X] contains no Type II
  modulus at all, so the theorem is really about Type I moduli, and "fires (Type I)" is never defined (m6).

* **Thm 2.1 (Weil count for subgroup membership): SOUND.** χ(P/B) = χ(P B^{e−1}); P irreducible, P ∤ B ⇒ the
  roots of P are simple in P B^{e−1} ⇒ not c·g^e; Lidl–Niederreiter 5.41 gives (#distinct roots − 1)q^{d/2}; the
  trivial character gives q^d − r. The 2q^{d/2} bound for elements of proper subfields is right
  (Σ_{e ≤ d/2} q^e ≤ q^{d/2}·q/(q − 1)). Brute force over F_{q^d} (own arithmetic; (q, d) ∈ {(3,4), (3,5), (3,6),
  (5,3), (5,4), (7,3), (2,8)}, all m | q^d − 1, random P, B): 0 violations, worst |dev|/bound = 0.61.
* **Prop 2.2 (expansion threshold): SOUND (scoped to the method, as stated).** Re-derived (term-by-term, ŝ(1) =
  |S|/|G_d|; ‖ŝ‖₁ ≥ 1 by inversion at x ∈ S; |S| ≤ |G_d|/2 ⇒ ‖ŝ‖₁ − ŝ(1) ≥ 1/2). Numerically (random S of sizes 1
  … N/2, exact FFT coefficients): 0 violations. Examples: coset ‖ŝ‖₁ = 1 ✓; exponent intervals ‖ŝ‖₁ ≤ 4.2 for
  N ≈ 1.6·10⁴ ✓ (but a log q factor is dropped, m7); the GAP bound is unproved and needs properness (m7) — my FFT
  test of 2-dim proper GAPs in ℤ/(3⁹−1) gives ‖ŝ‖₁/∏(1 + log(2κ_i + 1)) ≤ 0.34, so it is plausible.
* **Prop 2.3 (ES box below threshold): SOUND.** |𝔉(f)| ≤ τ₃(m) (ordered triples adc = m); C(e+2, 2) ≤ 3^e ✓;
  τ₃ ≤ τ² ✓; q ≥ 9 comparison checked for q ∈ {9, 11, 13, 16, 25}, k ≤ 4, n ≤ 7, d < 30 (0 failures). The phrase
  "any fixed S ⊆ 𝔉(f)" must be read as S ⊆ ⋂ 𝔉(f_α) over the α counted (then |S| ≤ min |𝔉| ≤ τ₃) — fine.

* **F1 (Heegner/ideal dictionary): SOUND.** Re-derived both directions: f | Nα = 1 + 4c²dp, f ∤ 2cdp ⇒ f splits
  in ℚ(√−dp) (−dp ≡ (2c)^{−2}); 𝔣 | αᾱ ⇒ 𝔣 or 𝔣̄ divides α, not both (else f | α, impossible as α/f ∉ O_K);
  conversely N𝔣 = f prime ≡ −1 (4cd) and Nα ≡ 1 (4cd) give f′ ≡ −1. The campaign-letter certificate
  (f | 4c²dp + 1, f ≡ −1 mod 4cd) is the (d, j)-line of the FIXED_MODULUS cube with c ↔ j, so it is exactly
  "Type II with modulus f". Brute force (own code, all primes 5 ≤ p < 400): the F1 set {f prime : ∃ c, d} equals the
  set of prime moduli 4y′ − 1, 4z′ − 1 of a brute-force Type II enumeration, 0 mismatches; exactly one of the two
  roots t of t² ≡ −dp works every time. (It is a tautological repackaging, which the text admits: "Violates nothing".)
* **F2 (supersingular torsion): SOUND-AFTER-REPAIRS (m8).** (−d/f) = −1 re-derived (f ≡ −1 mod 4d, (r−1)/2 odd;
  2 | d ⇒ f ≡ 7 mod 8) and confirmed at every certificate for p < 400; Deuring ⇒ supersingular ⇒ a_f = 0 for
  f ≥ 5 ✓; point counts of the CM curves for d = 1, 2, 3, 7, 11 at all certificate primes f < 400: #E(F_f) = f + 1
  in every case. But "elliptic curve over ℚ with CM by an order of ℚ(√−d)" exists only for the 13 class-number-one
  orders (d ∈ {1, 2, 3, 7, 11, 19, 43, 67, 163} up to the orders of disc −12, −16, −27, −28), so for generic d the
  statement is vacuous; and the Drinfeld clause is unreferenced and slightly off (m8).
* **F3–F5: Assessments, acceptable**, with a sign caveat in F3 (m9).

## Defects

## Checks performed
