# AGENT_REPORT O182 — spark relay I: "T1 of order k" (TWISTED_T1.md)

**SHARP:**
1. **A genuine order-3 T1 exists (PROVED, TWISTED_T1 Thm 3.2).** Over O = ℤ[ω]: TES(n): 9/n = ω/x + ω²/y + 2/z with
   x, y, z ≡ 1 (mod 2) ("2-primary" = choice of associate up to the cube −1, the analogue of positivity/monic).
   For n ≡ 1 (2), (n, 6) = 1, every solution satisfies the cubic reciprocity law Σ_{π|n} inv_π α = −⟨ω, 2⟩₂ ≠ 0, so
   at n = π^{3k} there is **no Type I/II-shaped solution**, while TES(π³) is solvable (other shapes). Primes have
   Type I/II solutions with forced cubic invariant. Controls: removing the anchor (c = 1) or the partner (numerator
   3 instead of 9) restores Type I/II solutions at cubes. Squares/4th powers are not special; π³, π⁶ are.
2. **Anchor calculus (PROVED, §2, §4):** T1 = anchor (a place whose normalisation pins inv α ≠ 0) + partner (a
   place where the constant algebra (τ₁, τ₂) ramifies but the equation forces inv α = 0) + tame vanishing.
   Pinning ⟺ normalisation image isotropic with τ ⊥ it (Lemma 2.1). Natural normalisations — monic, unit, primary —
   are **Lagrangian**, hence pin only 0. For odd m a single target never anchors (⟨t, t⟩ = 0), so "ζ₃ as an order-3
   target" with unit twists fails over ℤ[ω] (Prop 2.3(ii)); ES's T1 order 2 = non-alternating ⟨−1, −1⟩_ℝ.
   **The partner must be wild (Prop 4.3)** ⇒ no template T1 of any odd order over function fields — the structural
   reason for "no odd-square obstruction over F_q[T]". ES = (real anchor ∞, wild partner 2 with numerator 4);
   TES = (tame congruence anchor 2, wild partner λ with numerator 9 = λ⁴·unit).

## Results (labels)
* PROVED: Lemma 1.1 (c₁+c₂+c₃ = 1 "all minimal" configuration never occurs for deg A ≥ 1 — the brief's candidate is
  empty); Prop 1.2 (F_q(T) ∞-invariant = det(1, w, d) mod m); Cor 1.3; Lemma 2.1; Cor 2.2 (catalogue; (f) uses the
  standard conductor bound for the cubic Hilbert symbol, from memory, numerically consistent: ⟨U², U²⟩_λ = 0 on 300
  pairs, ⟨ω, U²⟩, ⟨λ, U²⟩ non-trivial); Prop 2.3; Lemma 3.1; **Thm 3.2**; Thm 4.1 (template, odd m); Prop 4.3.
* EVIDENCE: §3/§5 tables (all solutions exactly verified; λ-invariant obtained by reciprocity from tame symbols,
  reciprocity code checked); census of 746 primes: 7817 solutions, invariants always (1, 2, 0); 18 primes with no
  solution in the search window (N(π) ≤ 2239; N = 103, 151 also none in much larger windows).
* Open/Assessment: is TES(π) solvable for all primes? (the ES analogue; failures in window could be genuine —
  quadratic class α_{−1} is not pinned there, so the algebraic BL Brauer group does not explain them.)

## Relevance to ES (Assessment)
T1/B5 now sits in a family: the obstruction is "anchor + wild partner"; its order is the order of the anchor
symbol. For ES the anchor is the real place and the step any Type I/II route must break is "inv_p = 0 at p²"; the
odd-order members (TES) are strictly easier to prove than ES's own T1 (no quadratic subtleties at 2). A proof of
"TES(π) for all π" would be a twisted ES-theorem that must circumvent T1₃ — a possible template, not attempted.

## Files
TWISTED_T1.md; BRAINSTORM/bsI_tes_cubic_t1.md, bsI_anchor_calculus.md; scripts/tw_eis.py (ℤ[ω] arithmetic, tame
cubic/quadratic symbols), tw_eis_solve.py, tw_eis_scan.py, tw_eis_hard.py, tw_eis_census.py, tw_eis_classify.py,
tw_eis_quad.py; logs/tw_census_60_6000.txt. Reproduce Thm 3.2 table:
`cd scripts && uv run python tw_eis_scan.py 9:0 0:1 -1:-1 2:0 30` (+ controls `9:0 1:0 1:0 1:0`, `3:0 0:1 -1:-1 2:0`).

## Sparks (not pursued)
1. **TES at all primes**: try to prove it (no size bound: infinite X-search, so maybe a deterministic
   Dirichlet/ray-class argument works where ES's bounded search fails); or prove the N = 103 failure (integral
   obstruction beyond BL?). Either outcome is informative about B5.
2. Gaussian ℤ[i], m = 4 (μ₄): the (1+i)-adic place is wild for m = 2, 4; an order-4 anchor needs a non-Lagrangian
   normalisation and the symbol is not alternating for even m — possibly an order-4 T1 at 4th powers whose
   2-part is ES-like. Not computed.
3. m = 2 over ℚ with a tame congruence anchor (e.g. x, y, z ≡ 1 mod 3, twist 3) instead of positivity: a
   "positivity-free ES" with a T1 at squares? Template fails for m = 2 (tame places give only ½ℤ/ℤ); needs the
   ES-style quadratic analysis.
4. Kudla reading of Thm 3.2(c): a cubic analogue of (−f/p) = −1 for Type II certificates (Cor 2.3-type symbol
   χ_π(−u₂/u₃) fixed) — a cubic "Diff" (Kottwitz incoherence of order 3 over ℚ(ω) with anchor at a finite place).
