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

### Lemma 4.1 / Lemma 4.2 (slice divisor divides a fixed polynomial; bounded search) — SOUND

Re-derived. `u·B = tuv − u = n + v`, `v·A = n + u`; mod A: `tu ≡ 1`, `tn ≡ −1`, so t is a unit,
`t ≡ −n⁻¹`, `u ≡ −n` (n is a unit mod A as `A | tn+1`). Then `n^{deg_T f} f(t,u) ≡ R_f(n)` and `R_f ∈ ℤ[n]`
because each monomial `T^iU^j`, `i ≤ deg_T f`, becomes `±n^{d−i+j}`. Mod u: `v ≡ −n`, so `u | g(0,−n)`;
symmetric for v. (e): `f(−1/x,−x) ≡ 0` iff f vanishes on the irreducible curve `TU = 1`. Lemma 4.2's three
search loops enumerate exactly `E(n) ∩ W` (I re-checked the reconstruction `(tu−1)(tv−1) = tn+1 ⇒ P = n`).
Check: 399 random (point of X(n), random polynomial through it) trials of (a)–(d), 0 failures
(`scripts/review_inv2_lemmas.py`).

### Lemma 5.1 (character lemma for A, B, uv) — SOUND

Re-derived every symbol. A: INVOLUTION_ES Lemma 5.2 (R158-checked). B: for `ℓ | β`, `p ≡ −t⁻¹ (ℓ)`, so
`(p/β) = (−t/β)`; `B ≡ −1 (t)` with `t ≡ 3 (4)` gives `(2/t)^e(β/t) = −1`; reciprocity with `(t−1)/2` odd gives
`(t/β) = (β/t)(−1/β)`, so `(p/β) = (β/t) = −(2/t)^e`, and `e ≥ 1 ⇒ 8 | tp+1 ⇒ t ≡ 7 (8)`. uv: `u ≡ 3 (4)`;
the coprimality argument (`p | u ⇒ p | v` via `vA = p+u`, `p ∤ A`; then `p·max(u,v) > p+u+v` for p > 3) is
right; `(p/uv₀) = (2/u)^b(−1/u)(−1/v₀)(−1)^{(u−1)(v₀−1)/4} = −(2/u)^b` in both classes of `v₀ mod 4`, and
`b ≥ 1 ⇒ 8 | p+u ⇒ (2/u) = 1`. Brute force (independent enumeration of X(p) over all (u,v)): **5528 E-points,
all primes p ≡ 1 (8), p < 20000: all three symbols −1, 0 failures**; also `t ≡ u ≡ 3 (4)` on every point, and the
individual t, u, v symbols take both values (so the statement is not a triviality about t, u, v separately).

### Lemma 5.2 / Theorem 5.3 (cylinders barred under H) — SOUND ("admissible ⇒ empty" PROVED; infinitude CONDITIONAL, labels honest)

Re-derived. `R(P(q)) = κ p^{e₀} ∏ (C_{h_j} r_j)^{e_j}`, κ ∈ ℤ (R ∈ ℤ[n]), so the primes ≠ p of `R(p)` are those of
`K` (in Λ) and the `r_j`. Odd ℓ ∈ Λ: `p ≡ 24q*_ℓ+1 (ℓ)` is a nonzero square, `(ℓ/p) = (p/ℓ) = 1`; 2: `p ≡ 1 (8)`.
`r_j`: `24q ≡ −1 (p)` ⇒ `24^{d}h_j(q) ≡ H_j (p)`, all primes of `H_j`, `C_{h_j}`, 24 in Λ, sign harmless as
`(−1/p) = 1`. Then Thm 5.3: `A`, `B` or `uv` divides `R(p) ≠ 0` (Lemma 4.1), has a non-residue prime ≠ p
(Lemma 5.1) — contradiction. The Lemma 2.1 enlargement of Λ (`E_ℓ ≥ v_ℓ(α)`) makes p a unit square mod
`ℓ^{v_ℓ(α)}` since `24q*_ℓ+1` is a square unit. The H/BH hypothesis is applied to Theorem M(b)'s normalised
family, which POINTWISE_SIZE Thm M(b) proves to be primitive, irreducible, with no fixed prime divisor; so the
conditional parts invoke the standard form of H / BH. Remark 2's plane resultants (`−(cp+1)`, `−(p+c)`,
`c(p+c)`) and Remark 3 (`p²−1 = 48q(12q+1)`, `H_X = −1`, `H_{12X+1} = 12`) recomputed.

Independent check (`scripts/review_inv2_cyl.py 30000`, log `logs/review_inv2_cyl_30000.txt`): for 11 cylinders
(5 differ from the author's: `t=7`, `u=t²+2` as v-cylinder, a B-side `v=2t+1` u-cylinder, `v=u+6`, and two
finite curves as negative controls), all 385 primes `p = 24q+1 ≤ 30000`: "every prime ≠ p of `R_W(p)` is a
residue" ⇒ `E(p) ∩ W = ∅`, **no exception**; author's counts reproduced (`{t=u}` nonempty at 52, `{t=3}` at 193,
QR at exactly the other 192). Remark 3: 17 q with `q, 12q+1, 24q+1` prime, `E ∩ {t=u} = ∅` at all.

