# R198 — hostile review of CHI_FLIP.md (O198)

Reviewer: R198 (side agent). Document reviewed: CHI_FLIP.md at side-agent/chi-flip 42909547, with
reviews/agent-reports/AGENT_REPORT_O198.md. From-scratch scripts: scripts/review_cf_*.py (none reuse cf_*).
**ES is not solved here, nor any infinite case of it.**

## Summary verdicts
* **Thm 1.1** (χ = −ε₂(Q_w); local formulas) — **SOUND.** Re-derived every local invariant (see V1). From-scratch check
  `scripts/review_cf_hasse.py 2000`: all 50 008 positive words of all odd n ≤ 2000 (17 503 with n prime): det G_w = n,
  G_w positive definite, ε_∞ = −1, product formula, ε_ℓ = (−A/ℓ)^{v_ℓ(n)} at every odd ℓ | 2n·D₁D₂, and χ = −ε₂ with ε₂
  computed **two independent ways** (Hilbert symbols of a diagonalisation, and a brute-force mod-8 isotropy test):
  0 failures. Mutation tests (sign of the claim flipped; 2-adic Hilbert symbol replaced by 1) give 4 734 / 1 640
  failures at n ≤ 300, so the check has teeth. Author's counts 39 921 (letters ≤ 40) and 9 924 (prime n < 1200)
  reproduced; the "26 750" is the count for 3 ≤ n < 1200 (26 755 with the five words of n = 1) — immaterial.
* **Cor 1.2** (χ a 2-adic cell function, n-free) — **SOUND**; the period-8 statement can be made self-contained (D2).
* **Cor 1.3** (certificate ⟺ ℚ₂-isotropic ⟺ C₀ ≅ B_{p,∞} ≅ (−A*, −vA*p); else B_{2,∞}) — **SOUND** (wording minors D3).
  Ramification of (−A*, −vA*p) checked on all 17 503 prime-n words ≤ 2000: {p, ∞} iff χ = −1, {2, ∞} otherwise.
  Gross–Lucianovic: disc(Q_w) = 4tuv − 4u − 4v = 4n with their discriminant normalisation, Q_w primitive (n odd ⟹
  not all letters even), so the order is Gorenstein of reduced discriminant 4n — correct.
* **Cor 1.4** (χ n-free; scaling preserves χ; DK normalisation artefact) — **SOUND-AFTER-REPAIRS** (MAJOR D1: the
  correction is right about scaling but incomplete — in DK's own normalisation (A/n) *rotations* also flip, so
  "scaling is the only flip" was false in *both* normalisations; the ledger lines to fix are listed in D1).
  `scripts/review_cf_moves.py`: 60 480 scalings (a ∈ {3,…,15} odd, letters < 25): χ never changes, and (A/n) flips
  exactly when a ≡ 3 (mod 4).
* **Prop 1.5** (rotation law) — **SOUND** (proof relative to the cell lemma; D2 makes it unconditional).
  `review_cf_moves.py`: 78 213 positive odd→odd rotations, letters < 60, all 192 cells hit, 0 violations of
  "flip ⟺ t, u, v odd and t ≢ u (mod 4)". "Not a function of (n, n′) mod 8" confirmed: both values occur for each
  of the eight pairs (n, n′) mod 8 with n ≢ n′ (mod 4); χ is preserved on all eight pairs with n ≡ n′ (mod 4).
* **Prop 1.6** (Azumaya class β; T1 = BM obstruction in Ω₂; SQ₅ restated) — **SOUND-AFTER-REPAIRS** (minor D4).
  Re-derived: det Q ≡ n on X_n, 2n invertible ⟹ Q regular ⟹ C₀(Q) Azumaya over X_n[1/2n]; on the positive real
  cone Q is positive definite (A, A* > 0 is forced by AA* = tn + 1 > 0 and n > 0); the local formula of Thm 1.1 holds
  verbatim for ℤ_ℓ-points (it only uses AA* = tn + 1); hence at n = m² the adelic set with 2-adic component in Ω₂ has
  Σ inv = ½ — a genuine BM obstruction. Ω₂ count: `scripts/review_cf_cells.py` gives 320 odd-n cells, 80 per class
  n mod 8, of which 60 have χ = −1 (author's numbers). The SQ₅ restatement is correct but tautological (D4c).
* **§2.1–2.2 groupoid EVIDENCE** — **SOUND (reproduced exactly).** `scripts/review_cf_groupoid.py` (own union-find):
  letters ≤ 60, 1 ≤ K ≤ 10⁵, all moves: 205 568 nodes, **20 284 components**, flip numerators **{11, 79, 89, 93, 233,
  419, 439}**; odd numerators only: 27 918 components, **no flips**; letters ≤ 130, odd K ≤ 10⁶: 1 307 974 nodes,
  **278 014 components, flips exactly at n = 125 and 1119**. BFS example chain checked by hand (every step and every
  numerator), χ(6,18,1)₈₉ = (−18/89) = +1, χ(8,3,4)₈₉ = (−23/89) = −1. The cell-level groupoid figures (29 components,
  12 pairs) were not re-run (D7).
* **§2.3** (fixed chains are cell maps on a curve) — **SOUND** as scoped. Checked: K(DPw) − K(w) ≡ 0 identically forces
  det D = 1 and {σ(2), σ(3)} = {2, 3} with d₂ = d₃ = 1, i.e. identity or reversal; K∘Φ − K is n-free, so it never
  contains X_n; Z_Φ for the example chain: tuv = 7u + 9v − 9t/2, through (6, 18, 1) (108 = 126 + 9 − 27). The statement
  is nearly tautological (it excludes only maps no one proposed); the label "for this class of maps only" is honest.
* **§3.1** (q ∈ {2, 3, 5, 7} non-residue ⟹ A = q certificate word; Mordell's 840) — **SOUND.**
  `scripts/review_cf_mordell.py`: the classes t₀ = −p⁻¹ mod q computed *from actual primes* (not from the residue
  argument): among odd q < 500 exactly q ∈ {3, 5, 7} have all classes dividing q + 1; for all primes p ≡ 1 (4) < 10⁶ and
  q ∈ {2, 3, 5, 7} with (q/p) = −1, 78 544 words built, each with K = p, A = q, χ = −1: 0 failures. The residual set is
  the six square classes mod 840 (1·1·2·3 unit squares), = Mordell's list. (Pedantic: when t₀ = 1 there is a second
  word t = q + 1, u = 1.)
* **§4.1 census** — **SOUND (reproduced in full, not just a subrange).** `scripts/review_cf_census.c` (own enumerator,
  own Jacobi), all odd n ≤ 10⁶ in 1 s: χ ≡ +1 at non-squares only at **105** (|X_105| = 11, all boundary words — listed);
  499 odd squares, none with a χ = −1 word, mean |X| = 70.7; χ ≡ −1 at **38** n, all ≡ 3 (mod 4), starting 15, 311, 455,
  495, 551, …; 19 552 primes p ≡ 1 (8), mean N₋/|X_p| = 0.606, min **4/37 at p = 2521**; gcd(A, n) > 1 never occurs
  (consistent with AA* = tn + 1). At n ≤ 10⁵: 25 of the 38 χ ≡ −1 values, 157 squares, same 105.
* **§4.2** (parity facts) — **SOUND.** Proof re-derived (u = v ⟹ u | p ⟹ u = 1, the fixed point (p+2, 1, 1), A = p + 1);
  census confirms N₋ even and |X_p| odd at every p ≡ 1 (4) ≤ 10⁶, and N₋/2 even/odd = 1162/1222 for p ≡ 1 (8) < 10⁵.
* **§3.2, §4.2(c) "no closed formula", report NEGATIVE items** — Assessment, appropriately labelled.

## Defects
**No FATAL defects.** One MAJOR (ledger correctness of the "normalisation artefact" correction), minors.

**D1 (MAJOR) — Cor 1.4(b), §2 "Reading", report SHARP 3: the correction is right about scaling but misattributed and
incomplete.**
(a) *Scaling:* confirmed. Writing DK 8.3 as (at, u, v)ₘ ↦ (t, au, av)_{am}, A is unchanged, −A ≡ 1 (mod a), so
(−A/am) = (−A/m) and (A/am) = (−1/a)(A/m). DK's sign is (A/n), defined for n ≡ 1 (4) (DK 8.1), but 8.3 evaluates it at
m ≡ 3 (4), where (A/m) = −χ. In χ-language DK 8.3 says "a certificate of m scales to a certificate of am" — correct and
useful (DK 9.2), but not a flip.
(b) *Rotation flips in DK's own normalisation as well.* DK 8.2 is scoped to n, n′ ≡ 1 (4). When n ≢ n′ (mod 4) and not
all letters are odd, χ is preserved (Prop 1.5) and therefore (A/n) flips: e.g. (1,3,4)₅ ↦ (3,4,1)₇: (2/5) = −1,
(11/7) = +1, χ = −1 on both sides (`review_cf_moves.py`: 25 650 such rotations with letters < 60). So "scaling is the
only flip" was false in **both** normalisations. It is not purely "a normalisation artefact (A/n) vs (−A/n)": it
also misread DK 8.2's scope as "rotations preserve the sign".
(c) *Attribution.* DK 8.3 never says "only". The word "only" is in DISCOVERIES (J)9 bullet 3 ("the Klein group and
rotations preserve it; the only sign-flipping transfer found (scaling) needs composite n"), HJ_DEEP C3 (line 141:
"Scaling is the only flip (DK 8.3) … rotations preserve the sign (DK 8.2)"), and MODEL_SPECIFIC C3 ("DEDEKIND §8 found
only a scaling flip needing composite n").
*Repair.* In CHI_FLIP Cor 1.4(b), replace "DK 8.3/HJ_DEEP C3 called scaling 'the only flip' because they used (A/n) … is
exactly that normalisation" with: "(J)9 / HJ_DEEP C3 / MODEL_SPECIFIC C3 called scaling 'the only flip'. In the
normalisation (A/n) that DK 8.3 uses at m ≡ 3 (4), scaling with a ≡ 3 (4) flips, and so do rotations with n ≢ n′ (4)
and not all letters odd (e.g. (1,3,4)₅ ↦ (3,4,1)₇). In the uniform χ = (−A/n), scaling preserves χ and rotation flips
iff all letters are odd and t ≢ u (4). In either normalisation no classical move changes the sign at fixed n."
Ledger: (J)9 bullet 3 → "the Klein group preserves χ; rotation preserves it when n ≡ n′ (mod 4), and in the uniform
normalisation χ = (−A/n) scaling preserves it while odd-letter rotations with t ≢ u (4) flip it (CHI_FLIP Cor 1.4,
Prop 1.5); no classical move changes χ at fixed n." Add matching parenthetical repairs to HJ_DEEP C3 and MODEL_SPECIFIC
C3. HJ C3's conclusion ("no flip at fixed p from these moves") survives, in the scoped form of CHI_FLIP §2.3.

**D2 (MINOR, upgrade) — Cor 1.2 / Prop 1.5: the mod-8 period can be proved in two lines, removing the dependence on
DK Cor 4.1.** The document gets "locally constant (Hensel)" and imports the period 8 from DK Cor 4.1 / MODEL_SPECIFIC
Lemma 3.0′ (relative to Rademacher–Grosswald). Direct lemma: *if det G is odd, Q is isotropic over ℚ₂ iff some
primitive x mod 8 has Q(x) ≡ 0 (mod 8).* (⇐: ∇Q = 2Gx with Gx primitive, so some partial derivative has valuation
exactly 1, and Hensel needs v(Q(x)) ≥ 3.) Q_w(x) mod 8 depends only on (t, u, v) mod 8, so by Thm 1.1 χ is a function
of the cell mod 8 with no external input. `review_cf_hasse.py` uses this as its second ε₂ method (agrees on all 50 008
words), and `review_cf_cells.py` reproduces DK 8.1's five-class law. I also checked that the five 4-slices
(4 | A, 4 | A*, 4 | t, 4 | u, 4 | v) are exactly the 240 χ = −1 cells. **So MODEL_SPECIFIC Thm 3.1(a) (and the cell
half of DK Thm 4.5) become unconditional finite checks via Thm 1.1 + this lemma.** That is worth stating.
*Repair:* add the lemma to Cor 1.2, and relabel Prop 1.5 as "PROVED (self-contained finite cell check)".

**D3 (MINOR) — Cor 1.3 wording / attribution.** (a) "B_{2,∞} (Hurwitz quaternions)": B_{2,∞} = (−1, −1)_ℚ is the
algebra; the Hurwitz order is its maximal order. (b) "T1 = 'a positive ternary lattice … cannot ramify at an odd
prime'" is T1 *on the five slices* (the campaign's T1 covers Type I/II generally). The lattice statement is true in
general: a cyclic ℓ-part gives Jordan form ⟨a, b, ℓ^{2k}c⟩, which is isotropic. The cyclicity remark is correct:
⟨1, q, q⟩ ramifies at q ≡ 3 (4). (c) "upgraded from the p-adic genus to the rational class": ramification of C₀ is
genus (local) data. What is new is the transport p ↔ 2 by reciprocity, so say that. (d) Novelty: Thm 1.1 / Cor 1.3 are the
word-level transcription of Bright–Loughran Thm 1.2 (∏_{p|n}(−u₁/u₃, −u₂/u₃)_p = −1; the sources/ PDF is the
LITERATURE_AUTOMORPHIC transcription), of KUDLA Thm 1.2 (Diff-parity) and of DIFF_DEEP's supersingular transfer
(Diff = {p} ⟺ B_{p,∞}). Add "known in substance; new here is the uniform path-lattice form and the 2-adic reading" as
an Assessment.

**D4 (MINOR) — Prop 1.6.** (a) "odd non-square n ∉ {5, 105}" contradicts §4.1 and the same bullet's "exceptional set
{105} ∪ squares (boundary words included)": with boundary words n = 5 has (4,1,2), χ = −1. Delete 5 here. The "(or n ∈
{5, 105})" in DISCOVERIES (J)32 and MODEL_SPECIFIC C1 needs the same fix or an explicit "interior words" qualifier.
(b) "There is no BM obstruction at non-square n" needs Ω₂ ∩ X_n(ℤ₂) ≠ ∅ for every odd n, which is not argued.
Fix: for each class r mod 8, take one χ = −1 word with A odd (r ≡ 3 (4): (1, 2, n+2); r ≡ 5 (8): (4, 1, 2)₅; r ≡ 1 (8):
(1, 4, 7)₁₇, A = 3, χ = (−3/17) = −1). Keep t and u, and set v = (n + u)/A ∈ ℤ₂, which stays in the same cell mod 8. Also say "Ω₂ = the
ℤ₂-points of X_n in the 60 χ = −1 cells", not "the 60 cells". (c) The SQ₅ restatement is correct but holds *by
definition*: the β-BM set is non-empty ⟺ n is a non-square. The doc already says "= C1 restated". Keep the label
CONJECTURE and add "equivalent by definition; no new content". (d) Bright–Loughran Thm 1.9 concerns U_n (4/n = Σ 1/uᵢ),
not X_n, so say "analogy". The closer analogy is BL Cor 1.4 (divisibility patterns excluded at odd squares by BM).
Ghosh–Sarnak / Loughran–Mitankin are flagged "from memory": acceptable as Assessment, not citable as stated.

**D5 (MINOR) — §1 CERTIFIED line.** "26 750 … words over all odd n < 1200" is the count for 3 ≤ n < 1200; including
n = 1 it is 26 755. Say "3 ≤ n < 1200".

**D6 (MINOR) — report "Results (labels)".** It lists "Prop 1.5 … finite cell check" and "§4.2 parity facts" under
PROVED, consistent with the doc. But the report's headline "Thm 1.1 PROVED by Hilbert reciprocity alone" also uses
the local facts (F2). Say "Hilbert reciprocity plus the standard ℓ-adic isotropy criteria". Cosmetic.

**D7 (note) — not re-run:** the cell-level odd groupoid (29 components, 12 component/class pairs with both labels,
§2.2) and the "6 357 words" B_{p,∞} presentation count in the report. My own presentation check covers 17 503 prime-n
words ≤ 2000, so the latter is subsumed.

## Labels
All labels are appropriate after D1–D4. Thm 1.1, Cor 1.3, Cor 1.4, §3.1, §4.2: PROVED (verified). Prop 1.5: PROVED by
finite check, self-contained after D2. Prop 1.6: PROVED (BM at squares) + CONJECTURE (SQ₅ form). §2.1–2.2 and §4.1
are EVIDENCE/CERTIFIED, reproduced exactly. Nothing claims progress on ES itself.
