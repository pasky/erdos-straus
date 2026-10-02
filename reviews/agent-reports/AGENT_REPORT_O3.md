# AGENT_REPORT_O3 — two-prime Λ² cap (checkpoint 1)

Deliverable: `EXCEPTIONAL_TWIN2.md` (§0 table), scripts `scripts/twin2_binary_check.py`,
`scripts/twin2_offdiag.py`. Branch of this worktree; nothing merged.

## Outcome
* **The logarithmic form of TW target (6.2) is PROVED (Thm 1.4), without the factorisation (6.3).** (TW's literal (6.2), on `Z₂/Z₁²−1`, is false for large systems — Remark 1.6; only the log form is needed.)
  `log(Z₂/Z₁²) ≤ (1+25δ)[Σ_e ρ̃ρ̃′π_e + Σ_j ρ̃_j q_j]` when every prime-level
  binary mass `w_ℓ ≤ δ ≤ 1/16`. Proof: differentiate `log Z₂` in the coupling
  with the *unconditioned* rest law (Lemma 1.3: the `J`-denominator becomes one
  number `E[J 1_{A₋ⱼ}]`, so ET's "lower bound for J" obstacle disappears), then
  a conditional local lemma (Lemma 1.1/Cor 1.2) for the numerator. No KP, no
  Penrose, no vertex-degree bound. Exact check: 1200 random systems, bound
  never violated, ratio ≤ 0.99 (sharp to leading order).
* **Reduction 6.7 steps 1, 2, 2′ PROVED** (§3) with an explicit fibre law
  (QR base to `L^{1/2}`, local lemma on `(L^{1/2}, L^8]`, good fibres); cost
  `≤ 4L^{1/2}`; averages carry product inflation `4Γ(k)/k`. Lemma 2.1
  generalises TW Lemma 6.6 to any fibre law — this is what repairs T12/T14.
* **Summability of the unary and diagonal binary profiles PROVED** (Lemma 4.1),
  via Shiu along the top prime; needs the B-hypothesis `M ≤ P(M)^{1+B}`.
* **Theorem 5.1 (PROVED):** Λ² saving `≤ C_B L^{3/4}(log L)^C + 11·E_PΣ_jρ_jS_j`
  for ℛ(M)-families with `M ≤ X = e^L`, `M ≤ P(M)^{1+B}`, at most two prime
  factors above `(log X)^8`, twins included, level `λ ≤ A₀L`.
* **Remaining inequality (H_O), OPEN:** the off-diagonal ("deadly value") term
  `E_PΣρ_jS_j ≪ α^{−3}polylog`. This is ET Assessment 5.8's (O) term. TW's
  sketch "distinct pairs through the same residue give polylog/j²" was too
  optimistic: hubs give `≍ polylog/j` (still fine for the budget).
  New structure (Lemma 5.3, PROVED): the residue of `−4D mod M` at `j | M` is
  `−u′/v′` with `D = A u′/v′`, independent of k, m; reduced via `4A ≡ 1 (j)`
  to a canonical label. Split: same-label part SKETCH with a substantive gap (cross-cofactor pairs; label moduli are ≪ height², not height);
  cross-label part OPEN. Numerics (§5.2, toy multiplicity profile of the real system: unconditioned fibre, 1/m weights, X ≤ 1e8): cross-label
  agreements are at or below the random prediction in all 6 rows; all excess
  is same-label.
* **Cor 5.2 CONDITIONAL on (H_O):** the cap `≪ L^{3/4}(log L)^{O(1)}`.

## Caveats for the reviewer
* The cap is in `L = log X` (moduli ≤ X, λ ≤ A₀L), as in ET Cor 3.4, not in λ
  alone. "At most two large primes" means above `(log X)^8`, a family
  restriction (the full ES family has moduli with ≥ 3 such primes).
* Lemma 3.4's moment bounds use pointwise `τ(A²) ≤ C_ε M^ε` only where the
  modulus is `≤ (top prime)^{1+B}` and the sum has a spare power; the
  `L⁶/j²` bound for the m-top binary mass uses Lemma 3.3. Please check these
  case splits (top prime = j vs partner, exponents u, v ≥ 2).
* Lemma 2.2's constants were tightened by hand; (2.1) uses 9, 9.
* (H_O^=) is labelled SKETCH, not PROVED.

## Suggested next step
Write (H_O^=) at proof level; attack (H_O^≠) (equidistribution of canonical
labels mod j, uniform in j) — possibly via the n-side picture
(`j | gcd(n+4D, n+4D′)` ⇒ `j | D−D′`) with the label sets' j-dependence
handled by summing over j innermost.

## Self-review (reviewer subagent, deep) — applied
Core proofs (Thm 1.4, Lemmas 2.1, 2.2, 3.1–3.4) checked SOUND and numerics
reproduced. Fixed: (6.2) relabelled as log form (Remark 1.6 counterexample to
the literal (6.2)); label-modulus ≪ height²; same-label congruence across
cofactors (now flagged as a gap); prime-power vertices (upper bounds, `S ≤ q`);
variance remark withdrawn; inflation for `k | Q_F`; Lemma 3.2 dependency
order; numerics caveats and corrected random-label benchmark.

## Checkpoint 2
* **(H_O^=) PROVED (Lemma 5.4):** same-canonical-label part `≪ (log L)^{O(1)}`.
  Data (D fixed / (u′,v′) fixed / D̄ fixed) each impose one condition `d | A`,
  i.e. one class of the prime partner m mod 4d; Brun–Titchmarsh bounds the
  tail by `(log L)/φ(d)`; first elements `1/m₀` are charged to the m realising
  them (≤ 3τ(A²) data per m) and summed with Shiu along the top prime, with j
  innermost when j is top. Cross-cofactor pairs: AM–GM + activity inflation,
  not `d | m−m′` (closes the self-review gap). Prime powers only via the
  pointwise bound (one-line treatment — reviewer please check).
* **(H_O^≠) still OPEN**, sharply reduced (§5.4): the n-side gives
  `j | ab′−a′b ≠ 0`, and with j-independent masses the count has a margin of L
  (`L·L⁶/w₂ = L^{−1}`). The obstruction is that data and their first elements
  depend on j; the remaining statement is the displayed three-condition
  incidence count. Lenstra/CHN do not close it.
* Cor 5.2 is now CONDITIONAL on (H_O^≠) only.
* Stopping here (context budget).
