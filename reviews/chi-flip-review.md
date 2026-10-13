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
(in progress)
