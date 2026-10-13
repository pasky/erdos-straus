# R181 — hostile review of O181 (DRINFELD_ES.md + BRAINSTORM/bsH_*)

Reviewer branch side-agent/review-drinfeld (merged side-agent/drinfeld-degree-k). From-scratch scripts:
`scripts/review_dr_*.py` (own F_p[T] arithmetic, own Cantor–Zassenhaus factorisation, own power-residue /
tame-symbol code; nothing imported from `scripts/bsH_*`). ES is not solved anywhere; nothing below changes that.

Status: COMPLETE (round 1). Repairs applied: none (author active at time of writing; defects forwarded).

## Summary verdicts
| Claim | Verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Prop 1.2 (k-th power law) | SOUND (58 362 random symbol tests, 0 mismatches) |
| Thm 1.3 (Kummer data never embed in D^{(k)}_{P,∞}) | SOUND |
| Lemma 2.1 (Steinberg identity) | SOUND (checked place by place on > 9 000 points) |
| **Thm 2.2** (odd part of α_ζ vanishes on monic integral points) | **SOUND-AFTER-REPAIRS**: proof correct, all counts reproduced; headline overclaims "odd-order part of Br" (p-part, D1); citation fix D2 |
| BL transfer to F_q(T) | SOUND as Assessment for the prime-to-p part; independent proof that order-m classes are non-trivial via twisted points |
| Cor 2.3 (inv_P α_ζ = (−f/P)_m) | SOUND (non-vacuous tests at m = 6, 2) |
| Lemma 3.1, Lemma 3.2 | SOUND (Lemma 3.2 hypothesis is always satisfied, D3) |
| **Thm 3.3** (order-m reciprocity at m-th powers) | SOUND; one sentence over-labelled (D5); table reproduced exactly |
| §3 "never sterilises" | Assessment, "never" over-labelled (D6) |
| Prop 4.1 | SOUND; numerics incomplete — 222 pairs, not 81 (D7) |
| Prop 4.2 | SOUND-AFTER-REPAIRS (positivity, D8) |
| §5 genus vacuity | SOUND as Assessment; wrong supporting citation, elementary proof available (D10) |
| §6 Kottwitz form | SOUND; one explanatory sentence imprecise (D11) |
| bsH_lubin_tate_sterile | SOUND up to Artin-map normalisation (D13) |
| Citations from memory | Wei–Yu and FYZ exist (verified); Rosen/Pierce/Reiner numbering unverifiable (D12) |

No FATAL defects. One MAJOR (scope/label overclaim in the headline of Thm 2.2). The mathematics of O181 is correct.

## Per-claim verdicts (filled in incrementally)

### §1 Lemma 1.1, Prop 1.2, Thm 1.3 — SOUND (minor wording)
* Lemma 1.1 re-derived: (λ/ℓ)_k = λ^{(q^d−1)/k} = (λ^{(q−1)/k})^{1+q+…+q^{d−1}}, exponent ≡ d mod (q−1) hence
  mod k. SOUND. Checked on 200 random (λ, g) per q, all k | q − 1 (`scripts/review_dr_kpow.py`).
* Prop 1.2 re-derived: P ≡ −Aa²d (mod f); (−1/f)_k = ε^{deg f}; (Ad/f)_k = ε^{deg Ad·deg f}(f/Ad)_k =
  ε^{deg Ad(1+deg f)} since f ≡ −1 mod Ad; (a/f)_k = ε^{deg a deg f}(−1/a)_k = ±1, so (a²/f)_k = 1. Product
  ε^{(1+deg f)(1+deg Ad)−1}. All quantities monic (deg A ≥ 1 forces deg E < deg Aabd, so P is monic). SOUND.
  From scratch: random Type II data (a, b, c, d, A) with c a random monic divisor of a + b, q ∈ {7, 13, 19, 31},
  every k | q − 1 (incl. even k with ε_k = −1): 58 362 symbol tests, 0 mismatches; a control with P replaced by a
  random monic polynomial of the same degree gives uniformly distributed symbols (test is discriminating).
* Thm 1.3: (f/P)_k = ε^{n deg f}(P/f)_k = 1 for odd k; x^k − f then splits into distinct linear factors over F_P
  (p ∤ k, Hensel), so no place above P has local degree k and K = F(f^{1/k}) cannot embed in a degree-k division
  algebra with inv_P of exact order k (standard local–global embedding criterion; Reiner, *Maximal Orders*,
  Thm 32.15 / Pierce §18.4 — I could not open either; the criterion itself is classical and correctly stated).
  From scratch: 5 724 (P irreducible, odd k) tests, 0 mismatches. SOUND.
  Remarks (no defect): when k | deg f, f is monic of degree divisible by k, so f^{1/k} ∈ F_∞ and K also splits at
  ∞ — a second, independent reason for non-embedding; worth one sentence. The phrase "the order-k analogue of
  Diff = {P} is Diff = ∅" (§0) is interpretation (Assessment), since the choice of f^{1/k} as "the" degree-k CM
  datum is the author's.
* Rosen theorem numbering (Thm 3.5) not checkable here (book not in sources/); the reciprocity law used,
  (x/y)_k = ε_k^{deg x deg y}(y/x)_k for monic coprime x, y, is correct (Rosen Ch. 3, the d-th power reciprocity
  law) and is confirmed by the numerics above. Suggest "Rosen Ch. 3 (d-th power reciprocity law)" without number.

### §2 Lemma 2.1 (Steinberg decomposition) — SOUND
Re-derived: s = −u₁/u₃ = y·(u₁/u₂); (s, y) = (y, y) + (u₁/u₂, y), (y, y) = (y, −1); u₁/u₂ = (1 − y)^{−1}·x with
1 − y = (u₂ + u₃)/u₃ and u₁(1/u₂ + 1/u₃) = λu₁ − 1 = x; Steinberg kills ((1 − y)^{−1}, y). Hypothesis
u₂ + u₃ ≠ 0 is exactly x ≠ 0, automatic for monic u₂, u₃ in odd characteristic. From scratch
(`scripts/review_dr_checks.py`, check S): the identity inv_v α = inv_v(y, −1) + inv_v(x, y) holds **at every place**
on 2403 + 2403 + 2016 + 1750 points (q = 7; m = 3, 6, 2; A = T, T²; also the twisted c = (1,1,2) points). SOUND.

### §2 Thm 2.2 (odd part of α_ζ vanishes on monic integral points) — SOUND-AFTER-REPAIRS (proof SOUND; headline overclaims)
Proof re-derived step by step:
* Relabelling: (−b/a, 1/a) = (a, b) + 2(a, −1) = (a, b) since (a, −1) is 2-torsion; with a = −u₁/u₃,
  b = −u₂/u₃ this is the cyclic shift; transpositions give (b, a) = −(a, b). So α_ζ is S₃-invariant only up to
  sign (BL Prop 2.6 / Thm 1.2 say "invariant under S₃", literally true only for ζ = −1); the author handles this
  correctly — for 2-torsion/vanishing claims the sign is harmless.
* (i) ℓ ≠ Q: v_ℓ(λ) = v_ℓ(A) ≥ 0. If v_ℓ(λu₁) ≥ 1, x ≡ −1 unit, tame symbol = (−1)^{v(y)}. Else all u_i are
  ℓ-units (u₁ has maximal valuation 0) and ℓ ∤ A; v(x) = 0 ⇒ symbol 1; v(x) > 0 ⇒ (u₂ + u₃)/(u₂u₃) ≡ 0 ⇒ y ≡ 1 ⇒
  symbol y^{−v(x)} ≡ 1. Correct.
* (ii) ∞: λu₁ monic of positive degree ⇒ sgn x = 1, v_∞(x) < 0; sgn y = −1; symbol = ±1. Correct. (The tame
  symbol at ∞ is computed with uniformiser 1/T; principal units contribute nothing since p ∤ m.)
* (iii) Q: reciprocity (Σ_v inv_v = 0 for Br F_q(T), the function-field ABHN/Weil reciprocity). Correct.
* For odd m, (y, −1)_ζ = 0 as −1 = (−1)^m, and an element of ½ℤ/ℤ ∩ (1/m)ℤ/ℤ is 0; Br F → ⊕_v Br F_v injective.
Numerics (own enumeration of ALL monic NC solutions via (EY − N)(EZ − N) = N², own Cantor–Zassenhaus
factorisation and tame symbols at every place, Weil reciprocity asserted on every point): see table below.
Hypothesis "P a prime power" is **necessary** (confirms the author's Remark (3)): for P = Q₁Q₂ (q = 7, m = 3,
n = 3, A = T, 60 such P, 5754 positional solutions) inv_{Q₁} α_ζ takes the values 0/1/2 on 2232/1761/1761
points while inv_{Q₁} + inv_{Q₂} = 0 always (`scripts/review_dr_composite.py`).

Reproduction table (`scripts/review_dr_bl.py`; I count *positional* triples (X₁, X₂, X₃), each ES_q solution of the
author appearing 3 times — once per position of the minimal-degree denominator; author's counts × 3 in brackets):
| q, m, A, n, P | #P | #positional sol. (author ×3) | Weil recip. failures | odd inv ≠ 0 (any place) |
|---|---|---|---|---|
| 7, 3, T, 3, irred. | 112 (21 unsolvable) | 2403 (801×3 ✓) | 0 | 0 |
| 7, 3, T², 4 | 588 | 2016 (672×3 ✓) | 0 | 0 |
| 7, 3, T²+1, 4 | 588 | 2649 (883×3 ✓) | 0 | 0 |
| 7, 3, T(T+1), 4 | 588 | 2697 (899×3 ✓) | 0 | 0 |
| 19, 9, T, 2 | 171 | 489 (163×3 ✓) | 0 | 0 |
| 7, 3, T, 3, Q³ | 6 | 831 (277×3 ✓) | 0 | 0 |
| 13, 3, T, 3, Q³ | 12 | 999 (new) | 0 | 0 |
| 19, 9, T, 3, Q³ | 18 | 975 (new) | 0 | 0 |
| 7, 6, T, 3 | 112 | 2403 | 0 | 2-part only: inv_∞ = inv_P ∈ {0, 3}; all other places 0 ✓ |
| 13, 3, T, 3 | 728 (231 unsolvable) | 8487 (2829×3 ✓) | 0 | 0 |
| 7, 3, T, 4 | 588 (25 unsolvable) | 28230 (9410×3 ✓) | 0 | 0 |
| 13, 4, T, 3 | 728 | 8487 | 0 | 2-part only: inv_∞ = inv_P ∈ {0, 2}; all other places 0 ✓ |
Total (author's counting): 801 + 672 + 883 + 899 + 163 + 277 + 2829 + 9410 = **15 934** solutions at odd m (19 564
if the m = 6, 4 reruns are added). The report's "> 20 000 solutions (m = 3, 9)" is therefore an overcount (D15);
with my two new cube rows (333 + 325) the odd-m total is 16 592, all with 0 nonzero odd invariants.
Type II counts (positional II / 3) also reproduce the §1 table: 241, 2596, 192, 813, 42 (Q³, q = 7),
38 (Q³, q = 13).
The author's solution counts are reproduced exactly; every odd-order invariant is 0 at every place. EVIDENCE
confirmed.

### §2 Cor 2.3 (inv_P α_ζ = (−f/P)_m on Type II points) — SOUND
Re-derived: X = abd, Y = acdP, Z = bcdP solves the equation (Y⁻¹ + Z⁻¹ = E/(abdP), P + E = Aabd); x = E/P,
y = −a/b; deg E < n and P ∤ ab because deg abd = n − deg A < n; tame symbol y; −a/b ≡ −Aa²d/E ≡ −f using
Aabd ≡ E and Ef = P + Aa²d (checked: Ef = Aad(a + b) − E = Aa²d + P). From scratch (check C, f computed as
A·X₂/P − 1 directly from the solution, no datum reconstruction): q = 7, m = 6: 241 Type II points (= author's 241),
inv_P = class of −f on all, values 0/3 on 60/181; q = 7, m = 2, A = T², n = 4: 192 points, values 0/1 on 96/96,
0 mismatches. (With m odd the check is vacuous — both sides are 0 — so the even-m runs are the real test.)
Remark (no defect): Cor 2.3 + Thm 2.2 give a second proof of Thm 1.3, as the author says; consistent.

### §2 BL transfer to F_q(T) (author: Assessment) — SOUND as Assessment for the prime-to-p part; p-part untouched
Checked against sources/bright-loughran-1908.02526.pdf (§2 works over a field of characteristic 0). Step by step for
k = F_q(T), ℓ ≠ p: BL Lemma 2.1 (V ≅ G_m², units) is characteristic-free; Prop 2.5 needs
Br(G²_{m,k^s})[ℓ^∞] ≅ ℚ_ℓ/ℤ_ℓ(−1) (true, Gysin/Künneth, ℓ ≠ p), Gabber's absolute purity for ℓ-primary classes
along the regular disjoint boundary L_{i,j}, and H¹(A¹_{k^s}, ℚ_ℓ/ℤ_ℓ) = 0 — **true for ℓ ≠ p but false for ℓ = p**
(Artin–Schreier covers; A¹ is not simply connected in characteristic p); Lemma 2.4 (Br₁ = Br k via Pic = ℤ
with trivial action) is characteristic-free; Prop 2.6's residue computation uses only relation (2.5), which holds
with 4/n replaced by λ. (Q/Z(−1))^{Gal} restricted to ℓ ≠ p is ℤ/(q − 1)·(prime-to-p) ≅ μ_{q−1} ✓. So the
statement "Br Ũ{p′}/Br F ≅ μ_{q−1}, generated by α_ζ" is a reasonable Assessment (I would call it "standard ℓ-adic
transfer, not written out"). Independent support that the order-m classes are **non-trivial** in Br U/Br F: the
twisted points of §3 are F-points of the *same* surface U_λ (u_i = X_i/c_i), and on them α_ζ (ζ of order 3) takes all
three values at Q and at ∞ (q = 7, my runs reproduce the author's table) — so α_ζ is non-constant on U_λ(F),
hence of exact order 3 in Br U_λ/Br F. The author could state this; it removes any dependence of "order-m classes
exist" on the BL transfer.

### §3 Lemma 3.1 — SOUND. Lemma 3.2 — SOUND (hypothesis is vacuous; caveat can be deleted). Thm 3.3 — SOUND (one sentence over-labelled)
* Lemma 3.1: Thm 2.2(i) uses only λ = Σ1/u_i and ℓ-integrality of u_i = X_i/c_i. Re-derived. From scratch:
  every finite place ℓ ≠ Q has invariant 0 on all twisted points (c = (1,1,2), (1,2,4), (1,1,4); 6 116 points).
* Lemma 3.2: re-derived: sgn x = 1/c₁, v_∞(x) = n − deg A − deg X₁, sgn y = −c₃/c₂, v_∞(y) = deg X₃ − deg X₂;
  {x, y}_∞ = ±c₁^{deg X₂ − deg X₃}(c₃/c₂)^{deg A + deg X₁ − n}. ✓. From scratch, **for every admissible labelling**
  (every permutation putting a denominator of degree > n − deg A first, with c permuted accordingly): formula
  matches inv_∞ α_ζ on 20 464 (point, labelling) pairs, 0 mismatches, and α_{π} = sgn(π)·α on all of them
  (`scripts/review_dr_checks.py`, check L / perm-sign).
  **The hypothesis "some denominator has degree > n − deg A" is always satisfied** (for deg A ≥ 1, Q ∤ A): A/P is
  in lowest terms, so Q^e divides lcm(X₁, X₂, X₃), i.e. some X_i has degree ≥ n > n − deg A. The caveat "automatic
  unless c₁ + c₂ + c₃ = 1" (and AGENT_REPORT caveat 2) is therefore unnecessary. Consequence for the author's spark
  "twisted ES with c₁ + c₂ + c₃ = 1 … the one place where a full order-m sterility could occur": **vacuous** —
  all three denominators can never be of minimal degree; if no proper sub-sum of the c_i equals 1, the problem has no
  solutions for trivial degree reasons (checked: c = (3,3,2), (2,2,4), q = 7: 0 solutions for all 112 primes and 6
  cubes), otherwise Lemma 3.2 applies as usual.
* Thm 3.3: re-derived. Type II: v_Q(x) = −m; 1/u₂ + 1/u₃ = x/u₁ has valuation −m with v₂, v₃ ≥ m forces
  v₂ = v₃ (if v₂ ≠ v₃, the valuation would be −max < −m); y unit; symbol y^m. Type I: v(x) ≥ v₁ because
  (u₂+u₃)/(u₂u₃) is Q-integral; v(x) = 0 ⇒ 1; v(x) > 0 ⇒ v₁ = m and either y ≡ 1 (v(x) > m) or symbol y^{−m}
  (v(x) = m). (The "±" in "±y^{−m}" is superfluous: v(y) = 0.) Then reciprocity + Lemma 3.1. SOUND.
  From scratch (q = 7, A = T, n = 3, P = Q³): all Type I/II-shaped points have (inv_Q, inv_∞) = (0, 0):
  c = (1,1,2): 82 + 30; (1,2,4): 18 + 17; (1,1,4): 82 + 30; "other" shapes carry all three values (96/54/54,
  28/25/26, 96/62/62). The author's table is reproduced exactly (incl. #P unsolvable 4 / 6 at primes, 0 at cubes,
  and all six "(shape, inv_Q, inv_∞)" splits for c = (1,1,2), (1,2,4)).
  Over-label (MINOR): "For prime P there is no such restriction" is EVIDENCE (q = 7 tables), not part of what is
  proved; the proof only says the Type II symbol at prime P is y itself (unconstrained a priori).

### §3 "Why it never sterilises" — Assessment, correctly labelled except one word
The structural part (F_∞^*/U₁ ≅ F_q^* × ℤ; sign-normalised order-m invariants at ∞ are degree characters, Lemma 1.1 /
Lemma 3.2) is right. "a k-th power obstruction can only remove degree classes, **never all solutions**" is not proved
(nothing shows that the surviving degree classes are populated); it is EVIDENCE (0 unsolvable cubes in the q = 7
tables, reproduced) + Assessment. MINOR, see D7.

### §4 Prop 4.1 — SOUND; its numerics are incomplete (MINOR). Prop 4.2 — SOUND-AFTER-REPAIRS (sign)
* Prop 4.1 re-derived: Art_{L/ℚ}(N𝔞) = Art_{L/F'}(𝔞) (L = ℚ(ζ_M) abelian), so f mod M = Art_{L/F'}(𝔞) ∈ H and
  η(𝔞) = −1 ⟺ f ∈ H ∖ H'. "For all 𝔞" ⟺ H ∖ H' = {−1} uses that every element of H is an Artin symbol of some 𝔞 prime
  to M (Chebotarev) — implicit, should be said. Then |H| = 2, F' = ℚ(ζ_M)⁺ of degree φ(M)/2, which is even for
  4 | M > 4 (φ(M) ≡ 0 mod 4 when 8 | M or an odd prime divides M). |H ∖ H'| = φ(M)/(2[F':ℚ]) ≥ 2 since 4 | φ(M)
  and [F':ℚ] odd. SOUND.
* Numerics: the author's "81/81 pairs for M ≤ 120" comes from `scripts/bsH_descent.py`, which enumerates only
  subgroups generated by ≤ 2 elements, with the comment "enough to enumerate all subgroups for these M". **False**:
  (ℤ/24)^* ≅ (ℤ/2)³ and (ℤ/120)^* ≅ (ℤ/2)³ × ℤ/4 have subgroups needing 3 generators (e.g. H = G, F' = ℚ). My
  complete enumeration (`scripts/review_dr_descent.py`, BFS closure over all subgroups): **222** pairs (odd-degree
  F', quadratic K'/F') for 4 | M, 8 ≤ M ≤ 120, **0** with H ∖ H' = {−1}. Conclusion unchanged; count wrong (D8).
* Prop 4.2: N(β) ≡ (−1)^r = −1 (mod 4cd) and N(β)N(β') = (1 + 4c²dp)^r = 1 + 4c²d·pR_r are correct. But a
  rational Type II certificate xx' − 4c²dn' = 1, x ≡ x' ≡ −1 (mod 4cd) yields an ES solution only with x, x' > 0
  (x = 4acd − 1 etc.); N(β), N(β') may both be negative (F need not be totally real, β need not be totally
  positive), in which case (−N(β), −N(β')) ≡ (+1, +1) is not a certificate. Repair: add "if N(β), N(β') > 0"
  (or "β totally positive"); the conclusion "descent goes the wrong way" is unaffected — it only gets stronger (D9).
* FF remark (Carlitz real subfields): [K_M⁺ : F] = Φ(M)/(q − 1) with inertia at ∞ ≅ F_q^* (Hayes; Rosen Thm 12.14
  from memory) ✓; (q^d − 1)/(q − 1) ≡ d (mod 2) for q odd checked for q ≤ 13, d ≤ 8; M = T^e gives q^{e−1}. SOUND.

### §5 Rank-k genus vacuity — SOUND as Assessment; the cited mass formula is the wrong tool and is not needed
(a) = Thm 1.3 (SOUND). (b): Wei–Yu exists — F.-T. Wei, C.-F. Yu, *Mass formula of division algebras over global
function fields*, J. Number Theory 132 (2012), arXiv:1102.5465 (verified by search; I did not read it) — but it is a
**mass formula** (Denert–Van Geel) for the class set, not an optimal-embedding (Eichler trace) formula, so it does
not support "total number of optimal embeddings over the genus = h(O) × ∏ local factors" for degree k ≥ 3 (that
statement, with selectivity issues, is not classical for k ≥ 3). The conclusion the author needs is much more
elementary: if K ↪ D and O ⊂ K is an R-order, then O ⊂ D is an R-order and **every order is contained in a maximal
order**; so "∃ maximal order of D containing (a conjugate of) the datum" ⟺ "K embeds in D (local conditions at
Ram(D)) + the datum is integral". Genus vacuity in rank k is thus a one-line PROVED statement for maximal orders;
only congruence-level ("Eichler-type") orders would need more. Repair D10.
(c) LSV: Lubotzky–Samuels–Vishne, *Ramanujan complexes of type Ã_d*, Israel J. Math. 149 (2005) — correct
reference (from my memory too); the B3 scale argument is an Assessment, appropriately labelled.

### §6 Kottwitz form — SOUND (classical), one explanatory sentence imprecise
H¹(F_v, PGL_k) ↔ degree-k central simple algebras ↔ Br(F_v)[k] ≅ ℤ/k for local fields (period = index); global
exactness of H¹(F, PGL_k) → ⊕_v ℤ/k → ℤ/k → 0 at the middle (pointed sets) uses ABHN + period = index for global
fields. Ĝ = SL_k, Z(Ĝ) = μ_k with trivial Γ-action for an inner form of PGL_k. All correct. Imprecise (MINOR, D11):
"Γ_∞ acts trivially on μ_k because ∞ is not archimedean". Γ acts trivially on Z(Ĝ) for **every** inner form of PGL_k
over any field (ℚ included). The real difference: over ℝ, a form of PGL_k that is compact must be PU(k), an *outer*
form for k ≥ 3 (−1 ∉ W(A_{k−1})), whence inversion on μ_k (R177's D2c); over the non-archimedean F_∞ there are
anisotropic **inner** forms PGL₁(D_∞) for every k. Suggested wording: "because F_∞, unlike ℝ, carries anisotropic
inner forms of PGL_k for every k". Kottwitz 1986 not re-checked by me either (no source).
Diff_m(u) := {v : inv_v α_ζ(u) ≠ C_v} is the author's definition (flagged as such); given Thm 2.2,
"Diff_m(u) = {∞}" is immediate. Fine.

### Memos
* bsH_bl_order_q1, bsH_kth_power_law, bsH_twisted_targets, bsH_infinity_coordinate, bsH_odd_descent,
  bsH_carlitz_real: faithful summaries of §§1–4; inherit D1–D9 below. bsH_twisted_targets says "Lemma 3.2 formula
  matches on 4 074 solutions": I could not reconstruct 4 074 from the tables (1750 + 316 + 898 + 114 = 3078; adding
  (1,1,4): 5116); immaterial — my check covers 20 464 (point, labelling) pairs, 0 mismatches.
* bsH_lubin_tate_sterile — SOUND (convention-dependent sign only). x*_c ∈ R̂^* is ≡ 1 at ℓ ≠ T and 1 + cT at T
  (FUNCTIONFIELD_ES2 §0.2). Gal(F(Λ_∞)/F) ≅ lim (R/M)^* = R̂^* (Hayes); for T ∤ M, F(Λ_M) is unramified at T so
  rec_T(unit) is trivial on Λ_M; on Λ_{T^e} the local Artin symbol of a unit u acts by u^{−1} (Lubin–Tate/Hayes
  normalisation — with the opposite normalisation it is rec_T(1 + cT); the author should say "up to the
  normalisation of the Artin map"). 1 + cT ∈ U¹_T, and rec_T(U¹_T) is the wild inertia group ✓. 1 + cT is a square in
  F_q[[T]] (q odd, Hensel) and 1 is a square elsewhere, so x*_c is a square in R̂^*, and a limit of Q², Q ∈ R
  (R dense in R̂) ✓. The ℚ-dictionary is Assessment, so labelled.
* bsH_shtuka_theta: FYZ *Higher Siegel–Weil formula for unitary groups: the non-singular terms* is arXiv:2103.11514,
  Invent. Math. (2024) ✓ (verified by search). Yun–Zhang Ann. of Math. 186 (2017) ✓ (my memory). Assessment only.
* bsH_rank_k_genus: see §5 (D10). bsH_lsv_ramanujan, bsH_nagao_cf: Assessments/dictionaries, nothing to check
  beyond Nagao's theorem SL₂(F_q[T]) = SL₂(F_q) *_{B(F_q)} B(F_q[T]) (correct, Serre *Trees* II.1.6).

## Numbered defects

**FATAL** — none.

**MAJOR**
* **D1** (Thm 2.2 statement, last sentence "the odd-order part of the Brauer group of the ES_q surface carries no
  information at all on monic integral points"; same in §7 bullet 1 and AGENT_REPORT SHARP 1 / bsH_bl_order_q1
  "odd parts identically 0"). q is odd, so **p-primary classes are odd-order** and are not covered: BL's computation
  of Br Ũ/Br k is characteristic 0, and its key step H¹(L_{i,j}, ℚ/ℤ) = 0 for L ≅ A¹ fails for the p-part in
  characteristic p (Artin–Schreier), so Br Ũ{p} is not controlled (it may be large). What is PROVED is: α_ζ(u) = 0 in
  Br F for every ζ ∈ μ_{q−1} of odd order. *Repair:* "…in particular, for every odd m | q − 1 the class α_ζ(u)
  (ζ of order m) is zero in Br F: the odd-order **prime-to-p** classes of the ES_q surface (all of
  Br Ũ{p′}[odd]/Br F, granting the BL transfer — Assessment) carry no information on monic integral points; the
  p-primary part of Br Ũ is not addressed." Same edit in §7 and the report.

**MINOR**
* **D2** (Thm 2.2 proof (ii)) cites FUNCTIONFIELD_ES Lemma 1.2, which is stated for P prime (its (iii) uses
  primality in char 3). For P = Q^e (Q ∤ A) use: Q^e | lcm(X, Y, Z), so some denominator has degree ≥ n > n − deg A
  (deg A ≥ 1), and NC + leading coefficients (3 ≢ 1 mod p) give exactly one denominator of minimal degree.
* **D3** (Lemma 3.2 hypothesis; AGENT_REPORT caveat 2; spark "c₁ + c₂ + c₃ = 1"). The hypothesis is always true
  (same argument as D2), so delete "(automatic unless c₁ + c₂ + c₃ = 1 …)" and the caveat; the spark is vacuous
  (if no proper sub-sum of the c_i is 1 there are no solutions at all — checked c = (3,3,2), (2,2,4), q = 7).
  Also state that the formula refers to the labelling with that denominator first; in a fixed labelling multiply by
  sgn(π) (verified numerically, perm-sign check).
* **D4** (§1, "T1_k reversed (EVIDENCE + PROVED mechanism)"). The ×≈k enrichment mechanism (condition of
  "probability ≈ 1/3" at primes) is a heuristic, not proved; Q³ also admits non-primitive Type II data (Q | d is
  possible when deg Q ≤ n − deg A; Q | a or Q | b is excluded since Q | E | a + b). *Repair:* "EVIDENCE + heuristic mechanism".
* **D5** (Thm 3.3, sentence "For prime P there is no such restriction"). Not proved; EVIDENCE (q = 7 tables,
  reproduced). Also drop the superfluous "±" in "±y^{−m}".
* **D6** (§3 "Why it never sterilises", "never all solutions"; bsH_twisted_targets "never"). Not proved that the
  surviving degree classes are populated: EVIDENCE + Assessment.
* **D7** (§4 numerics "81/81 pairs M ≤ 120"; bsH_odd_descent; AGENT_REPORT). `bsH_descent.py` enumerates only
  ≤ 2-generated subgroups and wrongly claims this is exhaustive ((ℤ/24)^*, (ℤ/120)^* need 3 generators). Complete
  count: 222 pairs, 0 with H ∖ H' = {−1} (`scripts/review_dr_descent.py`). *Repair:* replace 81/81 by 222/222 (or
  say "all ≤ 2-generated H").
* **D8** (Prop 4.2). A rational certificate needs N(β), N(β') > 0. *Repair:* add the positivity hypothesis (or note
  that a negative pair is no certificate, which only strengthens the conclusion).
* **D9** (Prop 4.1 proof) uses implicitly that every element of H is Art_{L/F'}(𝔞) for some 𝔞 prime to M
  (Chebotarev) for the "iff". Add the word.
* **D10** (§5(b), bsH_rank_k_genus). Wei–Yu (JNT 132 (2012), arXiv:1102.5465 — exists) is a mass formula, not an
  optimal-embedding formula; "h(O) × ∏ local embedding numbers" is not a classical theorem in degree k ≥ 3.
  *Repair:* replace by "every R-order of D lies in a maximal order, so containment of the datum in some maximal
  order ⟺ K ↪ D (local conditions at Ram(D)) and integrality — PROVED, genus-vacuous"; keep Wei–Yu only as
  background for the size of the class set.
* **D11** (§6 "Γ_∞ acts trivially on μ_k because ∞ is not archimedean"). Γ acts trivially on Z(Ĝ) for every inner
  form of PGL_k over any field. Reword: "because F_∞, unlike ℝ, has anisotropic inner forms of PGL_k for all k
  (over ℝ the compact form PU(k) is outer for k ≥ 3)".
* **D12** (citations from memory). Rosen "Thm 3.5" and Pierce "§13.3" / Reiner "Thm 32.15" numbering could not be
  checked (no copies); the statements used are correct and the reciprocity law is confirmed numerically. Write
  "Rosen Ch. 3 (d-th power reciprocity)" and "standard embedding criterion (e.g. Reiner, Maximal Orders, §32)".
  Kottwitz 1986 remains unchecked (inherited from R177).
* **D13** (bsH_lubin_tate_sterile) "x*_c = rec_T((1 + cT)^{−1})" holds for the normalisation in which rec_T(u) acts on
  Λ_{T^e} by u^{−1}; add "with Hayes' normalisation of the Artin map".
* **D15** (AGENT_REPORT SHARP 1, "0 nonzero odd invariants on > 20 000 solutions (q = 7, 13, 19; m = 3, 9)").
  The §2 table sums to 15 934 at odd m (19 564 with the even-m rows). *Repair:* "on 15 934 solutions" (or add the
  reviewer's cube rows: 16 592).
* **D14** (cosmetic, Thm 1.3) mention that for k | deg f the Kummer field also splits at ∞ (a second reason for
  non-embedding) — optional.
