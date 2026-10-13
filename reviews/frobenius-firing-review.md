# R196 — independent hostile review of FROBENIUS_FIRING.md (O196)

Reviewer: R196 side agent (branch side-agent/review-frobenius), independent of the author's self-review (the "R196 #k"
markers already in the file are the author's own deep-self-review repairs, not this review).
Document reviewed: FROBENIUS_FIRING.md at merge of side-agent/frobenius-firing.
From-scratch scripts: `scripts/review_frob_*.py` (own integer factorisation/primality, own F_q arithmetic; nothing
imported from `ff_frob_*` or `fm_poly`).

**Overall: no FATAL, no MAJOR defect. Thm 4.2 SOUND, Cor 4.3 SOUND, Thm 4.4 SOUND (CONDITIONAL, citation-level),
§2 Thm 2.1 / Props 2.2–2.3 SOUND (scoped), Prop 1.2 (a)(b) SOUND, Thms 1.3/1.4 SOUND as conditional, F1 SOUND,
F2 SOUND-AFTER-REPAIRS; all numerics reproduced; ten MINOR defects (labels, one mis-described statistic, one stale
sentence contradicting an earlier withdrawal).**

Repairs applied: the author's last commit (a03d84f9, "final report numbers") preceded this review's end by > 20 min, so
m1–m10 were applied directly in FROBENIUS_FIRING.md (and m1, m5 in AGENT_REPORT_O196.md), each marked "R196 repair mk"
(distinct from the author's own "R196 #k" self-review markers). No theorem statement was weakened; only labels,
scope sentences, one statistic's description and one stale sentence changed.

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
  p < 1000 (0 violations, `review_frob_heegner.py`). (b) is immediate from Chebotarev (constant-field part handled
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
  "Type II with modulus f". Brute force (own code, all 166 primes 5 ≤ p < 1000): the F1 set {f prime : ∃ c, d} equals the
  set of prime moduli 4y′ − 1, 4z′ − 1 of a brute-force Type II enumeration, 0 mismatches; exactly one of the two
  roots t of t² ≡ −dp works every time. (It is a tautological repackaging, which the text admits: "Violates nothing".)
* **F2 (supersingular torsion): SOUND-AFTER-REPAIRS (m8).** (−d/f) = −1 re-derived (f ≡ −1 mod 4d, (f−1)/2 odd;
  2 | d ⇒ f ≡ 7 mod 8) and confirmed at every certificate for p < 1000; Deuring ⇒ supersingular ⇒ a_f = 0 for
  f ≥ 5 ✓; point counts of the CM curves for d = 1, 2, 3, 7, 11 at all certificate primes f < 400 (646 counts): #E(F_f) = f + 1
  in every case. But "elliptic curve over ℚ with CM by an order of ℚ(√−d)" exists only for the 13 class-number-one
  orders (d ∈ {1, 2, 3, 7, 11, 19, 43, 67, 163} up to the orders of disc −12, −16, −27, −28), so for generic d the
  statement is vacuous; and the Drinfeld clause is unreferenced and slightly off (m8).
* **F3–F5: Assessments, acceptable**, with a sign caveat in F3 (m9).

* **EVIDENCE §5.1 (S = {3}): ES^{(3)} REPRODUCED exactly; ES^{(y)} REPRODUCED but mis-described (m1); squares
  control REPRODUCED.** Own solver (`review_frob_selfmute.py`: Miller–Rabin + Pollard rho; every candidate solution
  rebuilt with Fractions and checked: 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, z > 0, every prime of den(z) divides y,
  is ∤ 2n and has even exponent; for ES^{(3)}: den(z) a power of 9), run to 10⁶ (brief asked 2·10⁵; both done,
  data/review_frob/selfmute_{2e5,1e6}.txt). All 78 496 primes solved in both variants. ES^{(3)} least-j histogram
  identical to the author's ({0: 68 655, …, 18: 1}). For ES^{(y)} the author's histogram ({0: 34 972, …, 21: 1}) is
  reproduced **only** with the stricter rule "r ≡ 11 (mod 12) at every j, including j = 0" (my variant `y12`); with
  the actual Definition 4.1 a j = 0 shot (Q = 1, z ∈ ℤ) is an ES solution, hence ES^{(y)}, for any r ≡ 3 (4), and the
  true least-j histogram is {0: 68 655, 1: 3053, 2: 2271, …, 19: 1, 20: 1, 21: 1} (max still 21). 332 odd squares
  m² < 10⁶ (3 ∤ m): no n + 4·9^j (j ≤ 15) has a prime factor ≡ 3 (4) (the proof is the two-squares argument, so
  j ≤ 15 vs the author's 40 is immaterial).
* **EVIDENCE §5.2 (FF overflow table): spot-check REPRODUCED.** Own F_q[T] code (`review_frob_overflow.py`), own
  search (all f = Am − 1 of degree ≤ D, all (a, d) with ad | m, all j ≤ (D − k)/deg s + 8, solution accepted only after
  a direct check of A/P = 1/X + 1/Y + 1/z, monicity, NC and den(z) = s^{2t}, t ≤ e — no use of the author's j-cap
  formula). Rows re-run: see Checks; every per-P least e coincides with the author's, and every data/ffl full
  ES_q failure in those rows is solved with the author's e (e.g. q = 7, n = 2: 101:5, 113:1, 122:1, 131:2, 152:2,
  164:3). Caveat (already stated by the author): e-values are upper bounds within the Prop 2.1 family and modulus
  degree ≤ D, not the least overflow over all solutions.

## Defects

No FATAL and no MAJOR defect found. MINOR:

**m1 (§5.1 and AGENT_REPORT SHARP 3: ES^{(y)} numerics describe a stricter variant).** "ES^{(y)}: least j = 0 for
34 972, max least j = 21" uses r ≡ 11 (mod 12) even at j = 0, i.e. it forces 3 | y also when z is integral; under
Definition 4.1 the j = 0 count is 68 655 (= ES^{(3)}'s), the max least j is still 21. *Repair:* either report the
true histogram or rename the statistic "ES^{(y)} with 3 | y forced" (the report's parenthetical "3 | y forced" is
the accurate description; §5.1's "[ES^{(y)}]" bracket and Definition-4.1 wording are not).

**m2 (Cor 4.3, F4, §4 title, §6 item 5: interpretation labelled as PROVED).** The equivalences are proved; the
sentences "exactly the B2 obstruction; the solution-dependence of the allowed primes is not", "moving mute places are
harmless" are Assessments. Moreover, in the proof of Thm 4.2 the mute places do NOT move: S is a fixed set of four
primes and "s_i | y" is enforced by the fixed congruence r ≡ −1 (mod s_i). And "exponent cap Q | (r+1)/4" is the
same thing as (J)25's growing modulus 4Q (the report's "sharpens 'growing modulus' into 'growing exponent'" is a
rephrasing, not a sharpening). *Repair:* mark these sentences (Assessment); retitle §4 e.g. "a variant whose
allowed denominators depend on the solution is still a theorem".

**m3 (Thm 4.4 scope).** Stated for n ≡ 1 (4) non-square with s ∤ n, but titled "|S| = 1 suffices under GRH, for
ES^{(s)} and for ES^{(y)}". *Repair:* add "for every odd n with s ∤ n (n ≡ 3 (4): Q = 1; squares: scaling as in
Thm 4.2(c))" to the statement, and cite Lenstra's d = 2 index condition explicitly (index of ⟨s⟩ divides 2).
Also page range: Moree's bibliography gives Invent. Math. 42 (1977) 202–224.

**m4 (Prop 1.2(c) inside a PROVED proposition).** It names no pair (L, C) and is a description of FF_MUTE Thm 3.5's
mechanism. *Repair:* move (c) to a Remark labelled Assessment.

**m5 (AGENT_REPORT vs document label of Thm 1.3).** The report says "Thm 1.3 (F_q[T], effective Chebotarev,
unconditional)", the document says CONDITIONAL on the cited shape. *Repair:* make the report match (or upgrade
both to "PROVED relative to the cited effective Chebotarev theorem" after reading Fried–Jarden Prop 6.4.8).

**m6 (Thm 1.4: "fires (Type I or II)" undefined; window contains only Type I moduli).** Definition 1.1 defines
firing only for Type II. Since X ≥ 3p² and Type II moduli are ≤ (p+1)(p+5)/4 < X/2, the counted window (X/2, X]
contains only Type I moduli. *Repair:* add the Type I firing relation (FIXED_MODULUS_SHOTS Lemma 4.1: g = 4vwf − p,
g | pv + f) to Def 1.1 and note the remark.

**m7 (Prop 2.2 examples).** (i) Exponent interval: ‖ŝ‖₁ ≪ log q^d = d log q, so "J ≫ d(n + b)q^{d/2}" silently
absorbs log q (fine for fixed q; say so). (ii) The GAP bound ‖ŝ‖₁ ≪ ∏(1 + log(2κ_i + 1)) is asserted without proof and
needs the box to be proper (injective); my numerics support it for proper 2-dim GAPs, but as written it is not
PROVED. *Repair:* add "proper" and label the GAP example heuristic/Assessment (it is not used downstream).

**m8 (F2 wording).** "Every elliptic curve over ℚ with CM by an order of ℚ(√−d)" is vacuous unless the order has class
number one. *Repair:* "every elliptic curve E over a number field with CM by an order of ℚ(√−d), at any prime above
f of good reduction (f ≥ 5), is supersingular; when E/F_f is defined over the prime field, #E(F_f) = f + 1" (for
class-number-one orders: CM curves over ℚ, checked numerically here). Drinfeld clause: for characteristic polynomial
X² + u·f, P(1) = 1 + uf = u(f + u^{−1}), so "∝ f + u^{−1}"; give a reference (Gekeler) or label it Assessment.

**m9 (F3 signs).** Thue's lemma gives (c, j) ∈ Λ_h with 0 < |c|, |j| < √h but not c, j > 0; a mixed-sign point
gives nothing. *Repair:* add "with c, j > 0" to the certificate condition and note that Thue does not control the sign
(one more reason the deterministic step fails).

**m10 (§5.2 last sentence contradicts the R196 #3 withdrawal).** "Contrast with Prop 2.2: the Weil-provable overflow is
an exponent interval of length ≳ d·n·q^{d/2}, i.e. e ≈ n² at d ≈ 2 log_q n" restates the withdrawn "threshold e ≈ n²";
F5 and §6 item 6 correctly say Prop 2.2 does not apply to the varying base s(α). *Repair:* replace by "the only
known proof (FF_MUTE Thm 3.5) uses overflow n^{2+o(1)}; whether a smaller overflow is provable is open (Prop 2.2 does
not apply to the varying base s(α))".

## Checks performed (all from scratch, scripts/review_frob_*.py, outputs data/review_frob/)

* `review_frob_selfmute.py 1000000 40` and `… 200000 40`: §5.1 (ES^{(3)}, ES^{(y)} true and stricter rule, squares).
  `review_frob_selfmute.py cor43 3000`: Cor 4.3 on 1568 random shots, S = {3,5,7,11}: 0 mismatches.
* `review_frob_density.py 300000`: Thm 4.4 density formula, 4 (n, s) pairs × 2 variants.
* `review_frob_weil.py`: Thm 2.1 brute force (8 (q, d, n, b) cases, all m | q^d − 1), Prop 2.2 with random S,
  exponent-interval and proper-GAP Fourier ℓ¹ norms, τ₃ bounds and the q ≥ 9 comparison.
* `review_frob_heegner.py 1000`: F1 dictionary vs brute-force Type II moduli, uniqueness of the dividing prime,
  (−d/f) = −1, CM point counts (d = 1, 2, 3, 7, 11), Type II modulus bound of Prop 1.2(a).
* `review_frob_overflow.py`: §5.2 rows (q, A, s, n, D) = (5, T, T+2, 2, 3), (5, T, T+2, 3, 5), (7, T, T+1, 2, 3)
  (3, T², T+1, 3, 4), (3, T², T+1, 4, 6) — 97 irreducible P in total: per-P least e identical to the author's in every
  case, and every data/ffl full ES_q failure of these rows solved with the stated e. (The (7, T, T+1, 3, 5) row was
  started but aborted after ~45 min: my divisor enumeration is brute force.)
* Not checked: Lenstra 1977 itself (not in sources/; used Moree's survey §9.5 summary), Fried–Jarden/Murty–Scherk
  error-term shapes, Serre 1981 Thm 4 (standard; not re-read), FF overflow rows with q^{D−k} ≥ 7⁴ (too slow in pure
  Python within budget; 5 of the 14 table rows re-checked).
