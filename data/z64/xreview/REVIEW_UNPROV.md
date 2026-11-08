# REVIEW_UNPROV — hostile cross-review of `Z64_UNPROV.md` (branch side-agent/z64-unprov @ 4a2a8f9bc)

Reviewer: Opus, standing in for the cross-model reviewer (OpenAI quota exhausted). ES is OPEN; nothing here changes that.
Sources I read myself: the memo; the archived BO PDF (`pdftotext`, read in full, §§1–4 and 7); ET arXiv 1107.1010
(p. 7–8, Prop 1.6, Prop 2.2, §4); `Z58_LOGIC` §§1, 3, 6.1 and Remark 6.3; `Z57_SYNTH` Lemma A.1; Aaronson's *Busy Beaver
Frontier* PDF (Thm 7, fetched); Otero JSL 58 (1993) abstract (Cambridge page). Script: `scripts/z64_xrev_unprov_check.py`.

## 1. Per-claim table

| claim | verdict | notes |
|---|---|---|
| §2.1 M_{q*} ⊨ NOI (BO with ϕ(β_i)=q*) | **CORRECT** | Checked against BO line by line. Lemma 2.7 (L_ϕ = {a/k : k∣ϕ(a)}) and Lemma 2.8 (vdD; L ⊨ NDOR ⇒ L_ϕ ⊨ NZR) are stated for *arbitrary* ϕ: L → Ẑ. The stage Claim uses ϕ only there. Lemma 2.6 (DOR of M_n[β]) needs only M_n ⊨ ZR. Choice of p_{n+1}: by Lemma 2.4 it depends on ℚ[β_1..β_n] only, so it is ϕ-independent. BO's Thm 4.2 says "integral part … by construction" without an argument. I supplied it: the element at position N of the enumeration is at finite distance after ≤ N stages, since chosen p's are never re-chosen. That argument is ϕ-free. M = {g ∈ ℚ[β] : ϕ(g) ∈ Ẑ} follows by induction on Lemma 2.7. |
| (F1) n=β_1 prime, units ±1 | **CORRECT** | UFD argument plus q* ∈ Ẑ^×. BO Lemma 2.10 / Thm 4.3 is indeed not needed. |
| (F2)/(F4) residues, specialisation | **CORRECT** | g(b) − ϕ(g) ∈ DẐ termwise; ℚ ∩ Ẑ = ℤ. Enlarging D (to 8∣D) is harmless. |
| Lemma 2.3 analytic arcs | **CORRECT** | ψ(B_i)(s) = Γ_i(T+s) + (b_i − Γ_i(T))e^{−s}. The finite Taylor expansion gives difference O((1+s)^E e^{−s}). The sign at ∞ is the sign of the leading coefficient, i.e. the M-sign (K ⊂ ℝ). For (c) I checked s + (T+π_1)(1−e^{−s}) + b_1e^{−s} > 0. |
| Lemma 2.4 positivity propagation | **CORRECT** | Largest-zero argument. 4/N is bounded at ρ ≥ 0 while some 1/F_i → +∞. (★)-form: C(ρ)=0 or u(ρ)=0 contradicts N(ρ) > 0. |
| Thm A(ii) Type split + Type I/II specialisation | **CORRECT** | Not all three divisible: 4X′Y′Z′ = ΣX′Y′ ≤ 3X′Y′Z′. Type I: ℓ ≡ s_0 (D), ℓ ≡ 1 mod r for r ∈ P∖D. r∣ℓ ⇒ Y(b) ≡ Y_0(b′) is an r-adic unit, so gcd(ℓ², y_0) = gcd(ℓ², z_0) = 1 and ℓ²∣x_0. This is *exactly* ET's Type I definition ("n divides x but is coprime to y, z", ET p. 3). ET Prop 1.6 is stated for any odd perfect square (ET p. 6). ET §4 uses only (2.1)–(2.2) plus Jacobi symbols. ET omit the Type II details; I re-did them: they need gcd(ab, n) = 1, which Prop 2.6 supplies for a genuine Type II solution. |
| Thm A(iii) ¬ES★(n) | **CORRECT** | T1 = Z57 Lemma A.1(b) holds for *every* m (memo says "odd", which is harmless). |
| Cor A.1(a)–(c); IOpen ⊬ (MS★), (MS) | **CORRECT** | q* := s′² with s′ ≡ s mod q. n > 10¹⁷ and n ≡ 1 (840) give Mord(n). Z58 Remark 6.3 gives the Hit form in any IOpen model. This does answer Z58_LOGIC §6.1 "Open" and logic_weak_arithmetic §5. The ℓ²-freedom (b_1 = ℓ², not 1) is precisely what removes the "sits over the unit 1" obstacle noted there. |
| §2.5 Remark: generators, cofinal f_m | **CORRECT** | f_m linear in β_1, so it is a prime generator with ϕ(f_m) = q*. (β_2−β_3)² ≥ 1 in M and x-degree → ∞ give cofinality. (c) with T past the zeros of Γ_1, Γ_1′ is fine. |
| §2.6 PD; Bezout fails; GCD fails in M_{q*} | **CORRECT** | PD uses 𝔸_f^× = ℚ^×Ẑ^×. Note ϕ_ℓ(f) ≠ 0 because ϕ(g) is a unit. Both counterexamples check. |
| Thm A′ (NOI + GCD + PD) | **CORRECT** | (G1), (G2) and the measure argument check: Haar on an open subset of (Z_ℓ^×)² is absolutely continuous, the point mass is ≤ 3/ℓ^k, and Borel–Cantelli applies. Point-count lemma: the SL_k(ℤ) change makes f monic-up-to-c_f in B_1; then Res ≠ 0, Schwartz–Zippel, ≤ deg f roots; the k=1 and constant cases are fine. GCD construction d = cG: I verified v_ℓ(d) = min(v_ℓ g, v_ℓ h) and the universality. (m_ℓ may be negative; the formula still works.) |
| §2.7 Caveat (no cofinal primes a.s.) | **CORRECT-WITH-FIX (label)** | Labelled "PROVED, sketch"; it should be *sketch / Assessment*. Wording: an irreducible nonconstant f needs ϕ(f) ∈ Ẑ^× (divisible by **no** ℓ), not "only finitely many". |
| §2.7 Remark (Jacobi mechanism in M) | **CORRECT-WITH-FIX** | "Never a u=1 hit" is argued for *standard* d only. A u=1 hit is B(4C−1) = n+1, and 4C−1 may be a non-standard cofactor (n+1)/k. Add the one-line check that ϕ((n+1)/k) ≡ 1 or 2 (mod 4). |
| Thm A″ (Th_∀(ℤ), ring language) | **CORRECT** | A nonzero ∏Q_j does not vanish on a translated lattice, so the atoms keep their truth values. The Shepherdson counterexample x = √2 t checks. "M_ϕ ⊭ Lagrange / TS" (top-form degree argument) checks. Ordered facts marked OPEN: honest. |
| A″ CONDITIONAL reading (U_ES) | **CORRECT as labelled** | Gaifman–Dimitracopoulos (MRDP in IΔ₀+exp) is standard. |
| Thm B | **CORRECT-WITH-FIX** | Newton basis and the (N!)³ identity are fine. **Gap:** the hypothesis is positivity on integers n ≥ 1 *of the class*, but the proof transfers "∀ real t ≥ 1 P_i(t) > 0". Fix: either assume real positivity on [1,∞), which is what the 840 certificate checks, or split the argument. For non-standard n, use RCF transfer of "∀t ≥ T_0, P_i(t) > 0" with T_0 a standard rational. Standard n are covered by the hypothesis. |
| Cor C (mod-840 dichotomy) | **CORRECT; CERTIFIED** | `mordell840.txt` and `famcheck.txt` re-run byte-identically. My independent exact search (T2a only, Fractions, 400 members per class) covers 186 classes with the same 8 members. Uncovered = {1,121,169,289,361,529} = unit squares mod 840. Mordell as cited: ET p. 8 ✓. |
| Prop 4.1 (ES_b, Σ₁-completeness, Gödel II) | **CORRECT** | I re-derived the bounds x ≤ 3n/4, y ≤ 2nx (4x−n ≥ 1 by discreteness) and z ≤ nxy in DOR. (c) and (d) are fine. |
| §4 literature: O'Rear/Aaronson Thm 7 | **VERIFIED** | Exact text in bb.pdf, with "Assuming O'Rear's construction is sound". |
| §5 table, row "S²₂ and above" | **WRONG (minor)** | "Witnessing gives nothing" is false for S²₂. S²₂ is ∀Σ^b_2-conservative over T¹₂ (Buss, Thm 5), so S²₂ ⊢ ES_prime puts the search in PLS. `Z58_LOGIC` §3 already says exactly this. The FP^NP remark only applies to the Σ^b_2-witnessing route. |
| Prop 5.1 (S¹₂ witnessing), Prop 7.1 | **CORRECT** | ES_prime is ∀Σ^b_1 after the ES_b bounds. |
| Prop 6.2 arc criterion | **CORRECT (GCD clause: sketch)** | Main clause follows from the §2.5 proof. GCD clause: I re-derived Type I in a GCD domain (x′ ~ ab via gcd(x′,y′z′) ∣ gcd(x′,y′)gcd(x′,z′); then c ∣ n(a+b) with gcd(c,n) = 1). Positivity on both systems is fine. The Type II descent (p∣ab, p∣m ⇒ p∣e, p∣a, p∣b, p²∣e) is correct. The Type II GCD algebra is "ET's algebra", not written out. |
| §5/§8 "window" / "realistic target only for T between NOI+GCD+PD+Th_∀(ℤ) and IE₁"; "at most IΔ₀+exp" | **OVERCLAIM (wording)** | These theories are not linearly ordered. IE₁ and IΔ₀+exp do **not** contain Th_∀(ℤ): by MRDP it contains sentences equivalent to Con(ZFC). So the "interval" has no lower end inside the upper one. |
| Novelty "new to our knowledge" | **Plausible** | A quick search found no prior ES/IOpen result. Otero JSL 58 (1993) (NOI embeddings of x²+by²=a via trigonometric/hyperbolic parametrisations) is adjacent prior art in method. |
| Falsifier table F1–F4 (§0, §8) | **CORRECT** | F1: the mechanism is T1. F2: R₈ = C-even ⊆ R, so R₈(m²) = 0. F3: counterexamples are primes of M (via (F1); the citation of "BO Lemma 2.10" there conflicts with the header). F4: no positivity is claimed. No HOT LEAD is claimed, and none is warranted. |

## 2. Independent computations (`scripts/z64_xrev_unprov_check.py`, ulimit -v 4e6, < 20 s)

* (1) Mod 840 by an independent T2a search with exact Fractions: 186/192 primitive classes covered; uncovered = unit squares
  = 𝔐; members (a,b,e) ∈ {(1,1,1),(1,2,3),(1,5,3),(1,6,7),(1,14,15),(1,21,11),(2,5,7),(2,21,23)}.
* (2) T1: R(s²) = 0 for all 1 ≤ s ≤ 1000 (via Lemma A.1 hit classes); sanity R(5) = R(13) = 2.
* (3) ET Prop 1.6: all ES solutions at ℓ² for odd ℓ ≤ 25 enumerated exhaustively. 0 are Type I, 0 are Type II.
  (Totals per ℓ: e.g. 46 at 81, 491 at 441; all are "neither" type.)
* (4) Type II system 4abd = m² + e, ce = a + b with no coprimality: no positive solution for odd m ≤ 121 (finite
  search, b(4a−2) ≤ m²). This extends the internal reviewer's m < 80.
* Replays of the lane's scripts: `mordell840.txt` and `famcheck.txt` reproduce byte-identically.

## 3. Required fixes (priority order)

1. **§5 table, S²₂ row**: replace "witnessing gives nothing" with "S²₂ ⊢ ES_prime ⇒ T¹₂ ⊢ ES_prime (∀Σ^b_2-conservativity,
   Buss) ⇒ search in PLS, as in `Z58_LOGIC` §3; higher levels not analysed here".
2. **Thm B proof, positivity step**: either state real positivity on [1,∞) as the hypothesis, or give the
   standard/non-standard split (RCF transfer of ∀t ≥ T_0 with standard T_0; standard n by hypothesis). Cor C is
   unaffected, since its certificate checks real positivity.
3. **"Window" wording** (§5 "lower bound/upper bound" paragraph, §8 bottom line "between … and IE₁", "at most
   IΔ₀+exp"): restate as non-containment. Any theory proving ES_prime on a square class must prove a sentence false in
   M_{q*} (NOI+PD+cofinal primes+Th_∀(ℤ)) or in the A′ model (NOI+GCD+PD+Th_∀(ℤ)). IOpen+Bez and IE₁ are open
   candidates. Note explicitly that IE₁ and IΔ₀+exp do not contain Th_∀(ℤ).
4. **Citations**: Otero JSL 58 (1993) is *Quadratic forms in NOI* (456–476). BO's [Ot2] is *The joint embedding property
   in NOI*, APAL 60 (1993) 275–290. Fix the "(BO's [Ot1], [Ot2])" attribution, and cite JSL 58 as method-adjacent
   prior art.
5. **Reliance list consistency**: add BO Lemma 2.3 / Thm 1.1 (Shepherdson), which Thm 4.2 uses. The F3 row cites "BO
   Lemma 2.10" while the header says primality is proved directly; cite (F1) only.
6. **"BO's published model verbatim" (q* = 1)**: BO fix an unspecified recursive enumeration. Say "BO's model for an
   enumeration beginning with x".
7. **§2.7 Remark**: either restrict "never a u=1 hit" to standard 4C−1, or add the non-standard cofactor check.
   Relabel the §2.7 Caveat as sketch/Assessment and fix "finitely many ℓ" → "no ℓ".
8. **Scope of novelty** (§8 bottom line "first such result at primes"): say "first unprovability result for ES at
   primes in a weak theory, to our knowledge".
9. **Proposed FRONTIER text, "Does NOT rule out"**: add the two-/four-squares principles (both fail in M_ϕ, PROVED) and
   ordered/ℕ-form universal facts such as T1 itself (OPEN whether M_ϕ satisfies them). The "Rules out" bullet should
   name the theory precisely (NOI + GCD + PD + Th_∀(ℤ), at primes of unit-square classes).
10. Prop 6.2: label the GCD clause's Type II parametrisation in GCD domains as a sketch ("ET's algebra", not written out).

## 4. Verdict

**ACCEPT-WITH-FIXES.**
* The headline theorems hold.
  * **A**: NOI (+PD, cofinal primes) ⊬ ES_prime on unit-square classes, and IOpen ⊬ (MS★), (MS).
  * **A′**: the same with GCD.
  * **A″**: the same with Th_∀(ℤ) in the ring language.
  * **B / Cor C**: IOpen proves ES on every class mod 840 outside 𝔐.
* I re-derived each of them step by step against BO (Lemmas 2.4, 2.6–2.9, 4.1, the stage Claim, Thm 4.2) and ET (Prop 1.6, §4).
  * The interpolation argument is sound: analytic arcs to integer points at odd squares ℓ² with the right coprimality,
    then positivity propagation.
  * The counterexamples are genuine primes of the model.
  * No hidden hypothesis was found.
* The fixes are a wrong side-row (S²₂), a fixable proof gap in Thm B's positivity step, overclaimed "window" wording, and citation/label hygiene.
* The labels on ES itself are honest: no claim about ℕ, no HOT LEAD.
* The verdict "strengthened (logic); narrowed (strong theories)" follows from what is proved.
