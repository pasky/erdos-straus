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

### Theorem 6.1 — (a) SOUND; (b) SOUND (with MINOR D2, D5); (c) SOUND; (d) SOUND as CONDITIONAL (MINOR D3)

This was scrutinised hardest. The questions and my answers:

1. **Does Z (hence a component's curve C) vary with p?** No. In INVOLUTION_ES Lemma 4.1 the menu maps are
   `g(x) = A(n)x + β(n)` evaluated at `n := P(x)`, so `Z₀ = ⋃ cl{x : P(g(x)) = P(x)}`, `Z₁`, `Z₂` are zero sets of
   fixed rational functions of x; Prop 4.2(b) gives `H = {id, ρ}` for every n ≠ 0, so `Z₃ = ∅`; the only
   p-dependence is a finite exceptional level set, absorbed in "all but finitely many p ∈ F" of Thm 5.1. In
   the (A,B,t) case the menu is n-independent. So Z is one fixed proper closed set; its components, and the
   curves C under its cylinders, are finitely many fixed curves.
2. **Uniformity of Siegel's theorem in a family?** Not needed, by 1: Siegel is applied to finitely many fixed
   affine curves, each giving a finite set of integer points (ineffective), hence finitely many axis lines with
   moduli α; α₀ is their lcm (with 24 and the Prop 3.2 lines). The only ineffective quantity is α₀ (through
   curves of genus ≥ 1); the Siegel/non-Siegel dichotomy itself is decidable for a given Z (genus 0, ≤ 2
   places: unit/Pell equations).
3. **Are all components handled?** (i) excluded by hypothesis; (ii) non-Siegel cylinders → finitely many axis
   lines (Cor 3.4) → Lemma 2.1 at `p ≡ 1 (α₀)`; axis lines → Lemma 2.1; (iii) surfaces / curves / points off
   their finitely many axis lines → at most `≪_W N^{2/3}` values `P(x) ≤ N`, constant depending only on deg W
   (Prop 3.2). Components over ℚ̄ but not over ℚ are covered (Prop 3.2 does not need ℚ; Cor 3.4 via
   `C ∩ C^σ`). Points of (iii) components lying on an axis line of that component are covered by α₀.
4. **Density.** `π(N; α₀, 1) ≍ N/log N ≫ N^{2/3}`, so "100% of primes `p ≡ 1 (mod α₀)`" is correct, with an
   explicit power saving `O(N^{2/3})` for the exceptional set. Since `α₀` is a multiple of 24, this is also a
   positive proportion `≥ 1/φ(α₀)·(1−o(1))` of all primes ≡ 1 (24), and Cor 6.2.1's "no positive-density set in
   that class" follows from Thm 5.1 (F ⊆ {E(p) ∩ Z ≠ ∅} ∪ finite).

So 6.1(b) is SOUND and its label (PROVED, unconditional, ineffective) is honest. The text should say point 1
explicitly (D2). (a): admissible q with `P(q) ∉ 𝔈_Z` — each case checked. (c): curves absorbed into
`cl π_e⁻¹π_e(D)`, which is 2-dimensional for a non-e-line D. (d): Theorem M(c) gives `≫ Y/(log Y)^{|S|}`
admissible `y ≤ Y`, `Y ≍ N/(24M)`, which beats `#𝔈_Z ∩ [1,N] ≪ N^{2/3}`.

**Exactly what (d) needs** (asked in the brief). For the explicit finite family `𝓕 = {f_h(y) = h(My+q̃)/C_h :
h ∈ S}` — each f_h irreducible, primitive, positive leading coefficient, pairwise non-proportional, `∏ f_h` with no
fixed prime divisor (all PROVED in POINTWISE_SIZE Thm M(b)) — one needs
`#{y ≤ Y : f_h(y) prime ∀h ∈ S} > C_Z·(24MY)^{2/3}` for all large Y (C_Z the implicit constant of Prop 3.2
summed over the (iii) components). Bateman–Horn (the standard asymptotic conjecture) gives `∼ c_𝓕 Y/(log Y)^{|S|}`
with `c_𝓕 > 0`, far more. So the hypothesis is a consequence of a standard conjecture; the *minimal* form
("an `Y^{2/3+δ}` lower bound in H") is not itself a named conjecture, and qualitative H does not suffice
(admissible primes could all lie in the thin set 𝔈_Z). The author says this correctly in the report; the
document should state the minimal form (D3). When Z has no type-(iii) component, H suffices (part (c)).

### Corollary 6.2 / class match with INVOLUTION_ES Thm 5.1 — SOUND

Cor 6.2 hypotheses = Thm 5.1 hypotheses (F ⊆ primes ≡ 1 (4); finite menu as in Thm 4.4(1), (t,u,v) with
ℚ(n)-coefficients or (A,B,t) n-independent; `Fix τ_p ⊆ E(p)`). The (A,B,t) → (t,u,v) transfer in §1 is right
(preimage of a proper closed set under a dominant morphism is proper closed; bijection on integer points). Note
(not a defect): in the (A,B,t) case Z contains planes `t = c` (INVOLUTION_ES Lemma 4.3), which are Siegel
cylinders, so Cor 6.2.1 never applies to (A,B,t) menus with a nontrivial scaling; Cor 6.2.2 does. In the
(t,u,v) case Thm 5.1 forces the axis line `{(t,1,1)}` ⊆ Z (via `(p+2,1,1)`), which is harmless (axis line).
Scope paragraph honest.

### Proposition 7.1 ({t = u}, lower density > 72%) — SOUND (MINOR D1 in the stated tail inequality)

Re-derived: `x ∈ E(p) ∩ {t=u}` ⇔ `x = (a,a,(p+a)/(a²−1))`, a odd ≥ 3, `a²−1 | p+a` (cross-checked against the
brute-force E(p) for all 385 primes `p = 24q+1 < 30000`: identical, 52 hits). Compatibility with `p ≡ 1 (24)`
recomputed by CRT: exactly `a ≡ 15, 23 (24)`. BT (Montgomery–Vaughan 1973, `π(x;q,a) ≤ 2x/(φ(q)log(x/q))`,
`q < x` — statement as I know it; the PDF is not in sources/) with `φ(lcm)φ(gcd) = φ(24)φ(a²−1)` gives the
`2μ/(1−θ)` bound; the large-a range is `≪ N^{1−θ/2} + N^{1/2} = o(N/log N)`. From-scratch sum
(`scripts/review_inv2_mass.py 200000 2000000`, log `logs/review_inv2_mass.txt`): partial mass
0.1384504578 (rounded up), independent tail ≤ 1.28·10⁻⁴, **μ ≤ 0.1385782, 1 − 2μ ≥ 0.72284**; empirical
2439/18507 covered — all as claimed. The text's tail inequality `φ(n) ≥ 0.375 n^{0.9}` is **false at n = 30**
(`φ(30)/30^{0.9} = 0.374698`; this is the global minimum, by multiplicativity: only p ≤ 5 have
`p^{0.1}(1−1/p) < 1`). The author's script actually uses `φ(n) ≥ n^{0.9}/3` (true), and only `n ≥ 4·10¹⁰` occur,
so the certified constant stands (D1, text only).

