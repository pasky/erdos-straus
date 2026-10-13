# AGENT_REPORT_O171 — SPARK synthesis of (J)1–(J)10 (checkpoint 1)

Branch `side-agent/spark-synthesis`. Main file `SYNTHESIS_SPARKS.md`. Scripts `scripts/syn_square_mimic.py`,
`scripts/syn_consistency.py`, `scripts/syn_hard_witness.py`. **ES is not solved; no positive claim is made.**

## Deliverables
* §0: a common skeleton for all (J) routes, with two layers. The **sign layer** is ψ_θ on the prime factors of
  N_θ(p), and its product is a single Legendre symbol (j_θ/p). The **class layer** is an individual divisor in a
  class. All pre-screens below use it.
* §1: **12 cross-combinations** X1–X12, each with a sketch and a barrier pre-screen. X1, the brief's (i), HJ ×
  rivers, turned out to be already closed by DK C3 + 8.2: reversal is free on L₃(p), and the sign is a rotation
  invariant.
* §2 (A1, X5 = DE Thm 7.3 × T1 × hardness law): **Lemma 2.1 (transfer) + Thm 2.3 (PROVED): if p ≡ 1 (8) and n_p > Y,
  then no Type II (or Type I, or five-HJ-slice) slice whose modulus is Y-smooth, of any size, has a Y-block witness.**
  The reason is that the block data of p equal those of a square m² ≡ p. CERTIFIED: 0 violations in 212 515 slice
  checks, and Lemma 2.2 checked on 18 348 pairs. Control (EVIDENCE): primes with n_p ≤ Y have such a witness at a
  94–100 % rate, so the dichotomy is sharp.
  **Novelty audit: Thm 2.3 is an instance of (H)3 Thm C / (H)9 Lemma 8.1, so it is known in substance.** The new
  content is cross-document: DE Cor 7.4 (O168) missed (H)9. Its scale `c₀ log p` and density `1/φ(M_E)` should
  read n_p (≫ log p·log₃p i.o.) and 2^{−π(Y)}. **Recommended repair: a cross-reference in DE §7.**
* §3 (A2, X6: index-2 / Bach-scale sign mechanism on the Farey ball): Prop 3.1 (PROVED). Small A lies in L₃(p) iff
  c = (−p mod A) divides A+1, and then (A/p) = (−c/A) is a mod-8 function. Any sign-layer argument therefore needs
  relations that are membership events or factorisations (B2/H-A). Negative.
* §4 (brief (v), EVIDENCE): locally-square primes (n_p > 19 at 10⁹, n_p > 23 at 10¹¹) have their first Type II
  witness at median e = 7 (control: 3). 87–100 % of these witnesses are at Y-smooth slices, by splitting the rough
  part of (p+e)/4. Nothing structured replaces block witnesses; what replaces them is the H-A lottery one level down.
* §5 (internal consistency, CERTIFIED): GI's W(n) equals DK's a₀(n) plus the v = 1 boundary words (749 n, 0
  mismatches). The GI census is reproduced. INV2 Lemma 5.1 holds on 647 points and is consistent with DK Thm 4.5.
  The only inconsistency found is the DE Cor 7.4 scope issue above.

## Verdict (Assessment)
No combination escapes the size/class layer. The sign layer on Y-smooth data is exactly square-mimicry (Thm 2.3).
The class layer is joint factorisation (H-A). Residual promise ≤ 1/5 for every combination (§6).

## Sparks (§7)
1. A hardness law based on square-mimic depth d(p) ≈ n_p, measured against e_min.
2. "Square-poisoned" rotation packets (DK 8.2) as an explicit T1-aware deficit term.
3. A char-2 reading of T1: an empty sign layer is why the F₂[T] coverings close. Does ℤ[1/3] have the same reason?
4. A Smith-path (√−1 Euclid) menu test.
5. Composite inheritance in the good direction: ES(p) ⟸ a Jacobi-(+1) word [[av′,t,au′]] of ap.
