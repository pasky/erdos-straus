# R128b — hostile review of O128 round 2 (`POINTWISE_TYPEII_SPECTRAL.md` §§7–10, `AGENT_REPORT_O128b.md`)

Reviewer: R128b side agent (branch `side-agent/review-typeii-r2`), merged `side-agent/typeii-spectral` @ a6eb39ca.
From-scratch scripts: `scripts/review_r128b_*.py` (no author code reused). Per the brief, repairs are applied
directly in the author's document and marked "(R128b repair)".

## Summary verdicts

| Claim | Verdict |
|---|---|
| R128 D1–D8 repairs (§§0–6) | SOUND-AFTER-REPAIRS (D6 left one stale "slowly widening" in §0; fixed) |
| Prop 7.1 (Gram data, converse) | SOUND |
| Prop 7.2 (Pell form) + "unusually small units" remark | SOUND (identity); remark MINOR overreach |
| Prop 8.1 (exact reduction to divisors; F vs f_II) | SOUND |
| Prop 8.2 (i)–(ii) (Stab = ±I; classes `[0,2c,k]`) | SOUND |
| Prop 8.2 (iii) (positivity = class choice k = ±1) | GAP (false as stated; contradicted by Prop 8.3) → repaired |
| Prop 8.3 (Q₀ global solution except sign; everywhere locally soluble for every n) | SOUND (core); "spinor" wording MINOR |
| "Consequence" (no local+spinor ⇒ global; Bright–Loughran) | SOUND-AFTER-REPAIRS |
| "obstruction group = ray class group mod 4cd·∞ of a split torus" | GAP (imprecise; conflates the class set with an obstruction) → repaired, relabelled Assessment |
| Remark 8.4 (three squares vs split torus) | MINOR inconsistency (both tori fail SA) → repaired |
| Prop 9.1 (character expansion; Eisenstein reading) | SOUND (identity); Eisenstein normalisation MINOR |
| Prop 9.2 (genus pairing, cancellation at odd squares) | SOUND (holds for all n, not only primes) |
| §9 EVIDENCE (t2s_eis) | not re-run (reported numbers plausible; out of scope of from-scratch budget) |
| §9.3, 9.4 (Siegel–Weil, Kudla/GKZ) | labels OK (Assessment); one MINOR overclaim |

## Defects

(numbered as found)

- **E1 (MINOR, leftover of R128 D6)** §0 bullet "§5 (EVIDENCE …)": "normalised lower tail `R ≈ 0.28` and slowly
  widening". D6 asked to soften "widening"; §5 now says "flat to slowly decreasing" but §0 was not updated.
  Repair (applied): "flat to slowly decreasing".
- **E2 (MINOR, overreach in a PROVED section)** Prop 7.2, last sentence: "a small unit forces … near-maximal class
  number of ℚ(√D')". `T + 2c√D'` has size ≈ 4c√D' for *every* Pell solution with `y = 2c`; it is "small" only when
  c is small, and c ranges up to ≈ p/2 (Prop 8.1: `2cd − 1 ≤ p`). For c ≍ p it gives `log ε ≪ log p`-type bounds
  only via `D' ≥ dp`, i.e. nothing beyond `h ≫ √D' L(1,χ)/log(c√D')`; "near-maximal" also needs a lower bound for
  `L(1,χ)` (Siegel, ineffective) and the class-number formula is for the order `ℤ[√D']`, not the field.
  Repair (applied): label the remark Assessment and add "for c ≤ p^{o(1)}; the class number is that of the order
  ℤ[√D']".

- **E3 (MAJOR — false statement inside a PROVED proposition)** Prop 8.2(iii): "'A > 0' is the choice k = +1 vs
  k = −1 … it is not an extra restriction beyond the class condition". Counterexample: the authors' own
  `Q₀ = [−1, 0, −dn]` (Prop 8.3) is paired with `S_c` itself (class k = +1), satisfies `b = 4` and the level data,
  and has A = −1 < 0. Since `q(Q) < 0`, Q is definite and `A > 0` ⇔ Q **positive** definite: positivity is the
  choice of sheet of the two-sheeted hyperboloid `q = −4dn`, an archimedean condition independent of k.
  `(Q,S) ↦ (−Q,−S)` preserves Gram matrix and level data, swaps the sheets, and sends class k to −k
  (verified: `−S_c ~ [0,2c,−1]` for c ≤ 6, `review_r128b_lattice.py`). Also for c = 1 the classes ±1 coincide
  (mod 2), so `(−Q₀,−S_1)` can be moved to `(Q′, S_1)` with Q′ positive definite and `b = 4` — but the moving γ
  destroys the level data `B ≡ 0 (4d)`, `d | C`. So for c = 1 the content of Type II is the level data.
  Repair (applied): rewrite (iii) as above.
- **E4 (MAJOR — imprecise/overclaimed structural statement, PROVED-adjacent, repeated in §0, §8.3, Conclusion,
  report)** "The obstruction group is the ray class group mod 4cd·∞ of a split torus, where strong approximation
  fails". What is true and provable: (a) with S_c fixed, the integral points are the positive divisors f of N
  (hyperbola `xy = N`, `x ≡ y ≡ −1 (M)`); (b) for a fixed local divisor shape, adelic integral points modulo the
  level subgroup `U(M)` form a torsor under `Ẑ^×/U(M) = (ℤ/M)^×`, the global point f hits exactly one class
  (namely `f mod M`), and asking for the class −1 vs the trivial divisor 1 is the narrow-vs-wide distinction
  `(ℤ/M)^×` vs `(ℤ/M)^×/±1`. But (ℤ/M)^× is the set of classes, **not an obstruction group**: for a non-square
  n no element of it is forbidden by local data. The only part that is an obstruction in the Brauer–Manin/genus
  sense is the quadratic character `χ_{−4d}·(n/·)` (Prop 9.2), i.e. a ℤ/2 quotient, which is non-trivial exactly
  when n is a square (mod the relevant f). Further, "strong approximation fails" does not distinguish this from
  three squares (Remark 8.4): every torus, split or anisotropic, fails strong approximation; three squares works
  because the ternary genus of `x²+y²+z²` has one class (spinor/SA for Spin(3) + class number one), not because
  its torus has SA. Repair (applied): rephrase as "the torus SO(S_c^⊥) ≅ 𝔾_m is split; local data fix a class
  set (ℤ/M)^× (narrow ray classes mod 4cd·∞), the target class is −1; the only class-restriction forced by local
  data is the genus character χ_{−4d}·(n/·) (BM obstruction at squares); whether divisors of N hit the class
  −1 is a global equidistribution question" and label the torus/ray-class reading Assessment.
- **E5 (MINOR)** Prop 8.3: "genus and spinor-genus data are satisfied". The pair problem has no natural spinor
  genus (the stabiliser of `(Q,S)` in SO(L) is finite and the S-stabiliser is a torus); what Q₀ proves is
  everywhere-local solubility of the integral-point problem (ℓ-adic: Q₀; ∞: any real positive-definite Q with
  `A = cB − 1`). Repair (applied): "all local conditions (ℓ-adic: Q₀; real: any positive definite real solution)".
  Also: the representation of the Gram lattice `4T₀` by L is *globally* solvable for every n (Q₀), so the
  failure at squares is of the integral Hasse principle for the problem with positivity + level data.
- **E6 (MINOR, citation precision)** "Consequence … the integral Brauer–Manin obstruction (Bright–Loughran
  2020)". Checked against arXiv:1908.02526 (sources/): BL Thm 1.1 says there is **no** BM obstruction to
  natural-number solutions of ES for any n ≥ 2; what explains the Type II failure at odd squares is BL Thm 1.2
  (a BM obstruction to strong approximation at the p-adic places, `∏_{p|n}(−u₁/u₃, −u₂/u₃)_p = −1`) and its
  Cor 1.4 (ET Prop 1.6). Repair (applied): cite Thm 1.2/Cor 1.4 and say "obstruction to the Type II
  (valuation-pattern) part, not to ES (Thm 1.1)".
- **E7 (MINOR)** Prop 9.2 is stated "for n = p prime"; the pairing `ψ(f) = χ_{−4d}(f) = (n/f)` for f | N holds for
  every n (`−4c²dn ≡ 1 (mod f)` makes −dn a square mod f). Verified for all n ≤ 500. Repair (applied): "for every n".
- **E8 (MINOR)** Prop 9.1: for η = 1 the standard (unnormalised) E(z, s) has vanishing non-constant coefficients
  at s = ½ (their normaliser `1/ζ(2s)` vanishes there; for non-trivial even η the normaliser `1/L(2s,η)` is
  finite, so only η = 1 is affected); the d(N)-type coefficients belong to the completed series `ξ(2s)E(z,s)` (resp. its level-M analogue).
  "up to normalisation" should say "completed Eisenstein series". Also "≍ n log n levels" — it is ≍ n log n
  *pairs* (c,d) (cd ≤ (n+1)/2, since `p ≥ 2cd − 1`), ≍ n distinct levels. Repair (applied).
- **E9 (MINOR, Assessment overreach)** §9.3: the coset theta series `Σ_{b(Q,S)=4} e(q(S)τ)` (correct:
  `S = −Q/(2dn) + w`, `q(S) = q(w) − 1/(dn)`, w in a coset of the positive definite `Q^⊥`) counts **all** S with
  `q(S) = 4c²`, of every class k and imprimitive ones; the Type II restriction `S = S_c` (with level data on Q)
  is not a theta coefficient. So "Type II asks for coefficients at 4c² in the class S ~ S_{c,1}" plus Siegel–Weil
  is a heuristic, not a skeleton. §9.4: for signature (2,1) and indefinite rank-2 T, Kudla's Z(T) is
  generically empty (a point and a geodesic in ℍ), and Type II is a fixed-*distance* incidence (Prop 2.4), not an
  intersection; "S_c … are isotropic-type" — S_c is anisotropic, S_c^⊥ is split. Repair (applied): wording.

## Claim-by-claim

### R128 D1–D8
Checked the text at each "(R128 repair Dk)" marker. D1 (§1), D2 (§1 table remark, §0), D3 (Prop 2.5), D4 (Lemma
6.1, §6(ii), §0), D5 (§3), D7, D8 (§4.4) are applied as requested. D6 applied in §5 but not in §0 (E1).

### Prop 7.1
Re-derived: `q(Q) = 16a²d² − 4f·de = 4d(4a²d − ef) = −4dp` (form 2: `ef − 4a²d = p`); `b(Q,S_c) = 2·4ad·2c − 4f·1
− 4·0·de = 4(4acd − f) = 4`; Gram (w.r.t. q) `[[−4dp, 4],[4, 4c²]]` ↔ binary form `4(−dp x² + xy + c²y²)`,
`disc T₀ = 1 + 4c²dp` ✓. Converse: `b = 4` ⇔ `A = cB − 1`; `A > 0` ⇒ `B ≥ 1` ⇒ `a = B/4d ≥ 1`; `q < 0, A > 0` ⇒
`C > 0` ⇒ `e ≥ 1`; then `b := ce − a = (cp + a)/(4acd − 1) ≥ 1` and `4abcd = a + b + pc` (direct). ✓
Verified from scratch (`review_r128b_lattice.py`) for all Type II quadruples of primes p < 300.

### Prop 7.2
`(T − 2cdm)(T + 2cdm) = f'f = 1 + 4c²dp` ⇒ `T² − 4c²(d²m² + dp) = 1` ✓. Converse: `s = (T+1)/2cd`,
`a = (s+m)/2`, `b = (s−m)/2 ≥ 1` by parity and `|m| < s`; `(4acd−1)(4bcd−1) = T² − 4c²d²m² = 1 + 4c²dp` ✓
(form 3 without the gcd condition, as stated). Verified numerically (same script). Remark: E2.

### Prop 8.1
Bijection f ↔ (a,b) as in Lemma 1.1.3 ✓; `4abcd = a+b+pc` forces `c | a+b` and (with `2ab ≥ a+b`)
`pc ≥ (2cd − 1)(a + b) ≥ (2cd−1)c`, so `2cd − 1 ≤ p` — the sum is finite. Non-primitive `(ga',gb',gc',d)` ↔
primitive `(a',b',c',g²d)` ✓ (g | b since `b = ce − a`). From scratch: F(p) = #all solutions = Σ_prim #{g: g²|d}
for all primes 5 ≤ p < 300 (990 solutions, 869 primitive).

### Prop 8.2
(i) primitive `[0,2c,1]`, automorphs ↔ `t² − 4c²u² = 4` ⇒ `(t−2cu)(t+2cu) = 4` with equal parity ⇒ u = 0 ✓.
(ii) square-discriminant reduction (`[0,k,r]`, r mod k) ✓; `b(Q,S_{c,k}) = 4(cB − kA)` ✓. (iii) E3.

### Prop 8.3 and the Consequence
`q(Q₀) = −4dn`, `b(Q₀,S_c) = 4`, level data ✓ (checked n ≤ 50, c,d ≤ 5). Everywhere-local solubility for every n ✓,
and F(s²) = 0 for odd s (checked below) ⇒ failure of the integral Hasse principle at odd squares ✓. E4–E6.

### Props 9.1–9.2
Orthogonality ✓. Pairing: since ψ = χ_{−4d} is odd with conductor | 4d | M, η ↦ ηψ is a bijection even ↔ odd;
`ψ(f) = (n/f)` for f | N ✓ ⇒ formula ✓. Character-free equivalent: `#{f|N: f ≡ −1 (M)} = #{f|N: f ≡ ±1 (M),
(n/f) = −1}`. From scratch (`review_r128b_eis.py`, explicit character tables built by CRT for M ≤ 96, 40 102 triples;
character-free form and `ψ(f) = (n/f)` for all 332 176 triples (n,c,d), n ≤ 500, `2cd − 1 ≤ n + 4`): all ✓;
every count is 0 at odd squares ✓; counts vanish for `2cd − 1 > n` ✓. (c,d) = (1,1): only even character mod 4 is
trivial, so MT is the whole count ✓. E7, E8.

### §9.3–9.4
Labels Assessment ✓ (report's Caveats agree). Coset-theta computation re-derived (E9). Point 1 of 9.4 (no fixed
form; bounded-level truncations vanish for many p) ✓ as EVIDENCE.
