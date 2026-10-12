# Hostile review R162 of INVOLUTION_ES2.md (O162, branch side-agent/windmill-surface)

Reviewer: R162. Reviewed commit: `136b3d09` (merged into side-agent/review-windmill-surface).
Background read: INVOLUTION_ES.md §4–5 (Lemma 4.1, Prop 4.2, Thm 4.4, Thm 5.1, Lemma 5.2, Cor 5.3),
POINTWISE_SIZE.md §1.2–1.3 (points, nondegeneracy, admissibility, Theorem M).
From-scratch scripts: `scripts/review_inv2_*.py` (none of the author's `inv2_*` code reused).
ES is not solved; nothing below changes that.

## Verdict table

(filled in claim by claim below)

## Claim-by-claim

### Lemma 2.1 (axis lines) — SOUND

Re-derived. On `{(a,b,v)}`: `P = (ab−1)v − b`, E iff `4 | ab−1`; on `{(a,u,c)}`: `P = (ac−1)u − c`, E iff
`u ≡ a⁻¹ (4)`; on `{(t,b,c)}`: `P = bc·t − b − c`, E iff `t ≡ b⁻¹ (4)`. Slopes are ≥ 0 (a,b,c ≥ 1). With
`α = 4·slope`, `n mod α` determines the free coordinate mod 4 (since `free = (n + const)/slope`), so `R_ℓ` is
one class (or empty), and every large `n` in it is attained. The odd-square exclusion is then exactly
INVOLUTION_ES Lemma 2.2 at large `m ≡ m₀ (mod α)`; the "unit square mod ℓ'^v, p ≡ 1 (8)" corollary is
CRT + Hensel (an odd `m₀` exists also when choosing the 2-component; 2 | α always). Correct.
Checks (`scripts/review_inv2_lemmas.py`, log `logs/review_inv2_lemmas_20000.txt`): E(m²) = ∅ for all odd
m < 200 (brute force over all of X(m²)); random axis lines (≈300, a,b ≤ 12): the realised classes mod α never
contain an odd square.

### Lemma 3.1 / Prop 3.2 / Cor 3.3 / Cor 3.4 (thin non-cylindrical components) — SOUND (two MINOR remarks)

Re-derived. Lemma 3.1: `tuv/2 − u − v + 1 ≥ uv − u − v + 1 = (u−1)(v−1)` for t ≥ 2 (checked on all of X(n),
n < 400). Prop 3.2: the line-finiteness argument is right (if `F` does not involve an axis variable, `W` is a
cylinder in that axis; otherwise `L_e` is the zero set of the coefficients, and a curve in `L_e` gives a
2-dimensional cylinder inside the irreducible surface W, hence equal to W). The count: for t = 1,
`(u−1)(v−1) = P+1` forces `min(u,v) ≤ √(N+1)+1`; for t ≥ 2, `tuv ≤ 2N+2`, and the pairs `y₁ ≤ y₂` with
`y₁y₂² ≤ X` number `≤ Σ_{y₁≤X^{1/3}} √(X/y₁) ≤ 2X^{2/3}`; times 2 orders, times 3 axes, times the fibre bound
D_W. Each counted point lies on an axis-parallel line over the two small coordinates which is not contained in
W, so the fibre bound applies. The constant depends only on W (degree), not on N or p. Cor 3.3/3.4 follow; the
"not defined over ℚ ⇒ finitely many integer points" case is right (integer points lie in `C ∩ C^σ` with
`C^σ ≠ C`).

The bound `N^{2/3}` is attained up to constants (e.g. `W = {t = u + v}` has ≍ `N^{2/3}` points with
`P ≤ N`), so nothing better can be claimed from size alone; the author does not.

