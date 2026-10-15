# R248 — hostile review of STERILE_DIOPHANTINE.md (O241, branch side-agent/sterile-diophantine)

Reviewer: R248 (side-agent/review-sterile-dioph). Scope: STERILE_DIOPHANTINE.md, BRAINSTORM/z16_*.md,
reviews/agent-reports/AGENT_REPORT_O241.md, scripts/z16_*, data/z16/. O227 (FF_THIRDS_CORNER.md) is out of scope except where
cited. From-scratch scripts: `scripts/review_r248_*`; data `data/review_r248/`.

(Status: in progress; verdict table filled in claim by claim.)

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 2.1 (game barrier) | SOUND-AFTER-REPAIRS (proof of density incomplete for absolute/potential games; "games only give ⋃_k U_c^{(k)}" is Assessment) |
| Lemma 3.1 (windowed König + dimension) | SOUND (minor wording) |
| EVIDENCE q = 3 tree to depth 9 | CONFIRMED independently (identical ball set, identical table) |

## Independent recomputation: q = 3 survivor tree to depth 9

`scripts/review_r248_caseB.c` enumerates every Case B tuple of parameter s ≤ SMAX from scratch via the (w, C) parametrisation
(L' = g'm' monic, w = Tw₁, C = TC₁ monic, m'wC = T^s + v, w + C = g'v). Key re-derived fact: deg v ≤ max(a, b) < a + b = deg wC,
so m' is the polynomial quotient of T^s by wC — one division per (w₁, C₁, s). Every hit is checked against EE' = 1 + T^sL'g'.
Ball of a tuple: u ≡ −E (mod T^{⌈s/2⌉+1}) (a family at level N needs γ = s − N − 1 ∈ [0, N − 1], so N ≥ ⌈s/2⌉; depth ≤ 9 needs
s ≤ 16). Result: 312 tuples for s ≤ 16, **348 for s ≤ 17 (= the author's count in §4)**.
`scripts/review_r248_tree.py` adds Case A data re-derived from the definition (a₀ = T^α a₁', b₀ = b₁ monic, γ = 0, g' = 1; EF = T^α a₁' + b₁,
E = a₁'b₁K − 1, z := (F + b₁)/a₁', b₁KF = T^α + z, T | z ≠ 0; λ, β, deg z ≤ α − 1), enumerating z and ordered monic
factorisations of T^α + z. The resulting distinct-ball set to depth 9 is **byte-identical** to `data/z16/balls_d9.txt` (172 balls),
and the per-depth table (balls 1, 2, 4, 12, 13, 28, 26; alive fraction .667 … .5167; sibling profiles incl. two parents with
2 covered children at depth 6, none with 3) reproduces §3 exactly for both c. Copy: `data/review_r248/balls_d9.txt`.
Caveat (MINOR, see D-list): "p_d = relative mass of distinct depth-d balls" counts balls lying inside already-covered
cylinders (e.g. both depth-4 balls lie inside the depth-3 ball: profile [2, 0, 0, 0] at depth 4), so Σ p_d = 0.955 is not
a covered mass and not the quantity of the percolation model (where p_d should be the fraction of *alive* depth-d cylinders
that are balls).

## Thm 2.1 (game barrier) — SOUND-AFTER-REPAIRS

Re-derivation. Topology: U_c = X_c ∖ ⋃𝔅 is closed (𝔅 a set of clopen cylinders). X_c contains the s = 4 ball: E = T² − cT − 1,
L' = g' = 1, j = γ = 1, N = 2, D = 1 + T⁴ = (T² + T − 1)(T² − T − 1) over F₃ (checked by hand and found by
review_r248_caseB as the two s = 4 tuples, balls 112, 122 of depth 3). So U_c ≠ X_c and U_c ∩ V ≠ V for V ⊇ that ball. A
dense closed set is everything. The theorem is therefore correct **provided every listed game has dense winning sets**.

* Schmidt (α, β) game, McMullen strong game: Bob's first ball is arbitrary, radii are forced/choosable → 0, outcome ∈ Bob's
  balls; winning sets are dense. ✓
* **Absolute and potential games: the given proof ("Bob opens inside it") is incomplete.** In Fishman–Simmons–Urbański
  (arXiv 1301.5630v11, App. C, Defs C.1, C.4 — accessed) Alice also wins *by default* (if r_n ↛ 0, or if the outcome lies in one
  of her chosen sets N(A_{i,n}, r_{i,n})). FSU themselves remark (Rem. C.3) that "it is not immediately obvious … that sets
  which are winning for the new [potential] game are nonempty"; this follows only via Thm C.8 (potential ⇔ absolute winning
  under Assumption C.6, which holds for H = points in a doubling space, Obs. C.7 — X_c ≅ ℤ₃ is doubling) and absolute ⇒
  Schmidt winning on uniformly perfect spaces (FSU Prop 4.4(ii), cited in Rem. C.3; X_c is uniformly perfect). With that
  chain the density, hence the theorem, holds. The hypothesis class as worded ("any target game in which Bob's first move may
  be any ball and the outcome lies in Bob's first ball") is *not* sufficient: a game with Alice-default-wins satisfies it
  but need not have dense winning sets. → D1.
* "Hyperplane-absolute game" on X_c: hyperplanes are not defined on ℤ₃-like ultrametric spaces; in dimension 1 / H = points it
  is the absolute game. Harmless; say so. → D1.
* "Which hypothesis kills games … a winning statement … yields at most ⋃_k U_c^{(k)} ≠ ∅": this is a heuristic (no theorem says
  every game argument outputs exactly a union over shrink levels; nor is ⋃_k U_c^{(k)} shown to be winning). Inside a PROVED
  block it must be labelled Assessment. Also note that each U_c^{(k)} is itself closed and misses the shrunk s = 4 ball, so
  it too is not winning — only the non-closed union could be. → D2.

## Lemma 3.1 (windowed König lemma) — SOUND

Re-derived. (i) Ancestors of alive cylinders are alive (a ball containing the ancestor contains the descendant and has
depth ≤ the ancestor's). (ii) A depth-(n+m) descendant D of alive V is dead only via a ball B ⊇ D of depth ≤ n+m; B is
comparable with V, and depth B ≤ n would kill V; so B ⊂ V, n < depth B ≤ n+m, killing ≤ 3^{n+m−depth B} descendants;
(W) leaves ≥ K alive. (iii) Limit point x: if x ∈ B ∈ 𝔅 of depth d ≥ n₀, choose j with n₀ + jm ≥ d; the visited
cylinder of x at that depth is alive but ⊂ B — contradiction (the text's "the depth-d cylinder of x, alive by construction"
is right only via (i); MINOR wording). d < n₀: B ⊇ V₀ contradicts V₀ alive. ✓ (iv) Dimension: the uniform measure μ on the
K-ary tree; for 3^{−t}-balls with n₀ + jm ≤ t < n₀ + (j+1)m, μ ≤ K^{−j} ≤ K·(3^{−t})^{s}, s = log K/(m log 3), after
absorbing 3^{n₀ s}; mass distribution principle (Falconer, Prop 4.2 form) gives dim_H ≥ s. ✓ (Metric 3^{−v_T}; constants
depend only on n₀, K, m — legitimate.) (W) for m = 1, K = 1 is "at most 2 children in 𝔅" ✓.
Notes: "n ∈ n₀ + mℕ" must include n = n₀ (ℕ ∋ 0) — V₀ itself must satisfy (W). The parenthetical "it suffices: for the alive V
the construction visits" is correct but makes the hypothesis depend on choices; fine as stated. Nested balls in (W) are
over-counted, which only weakens (W) — harmless.
