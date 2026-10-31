# z52b Pass 1, batch L00 (all 30 items; ES is OPEN)

Summary (batch complete, items 1-30; not merged):
1. Counts: covered 14, nothing 6, skipped 10, needs-compute 0, interesting 0 (30 items).
2. Interesting items: none. No surprising result; no depth lane recommended from this batch.
3. Calibration flags: (a) ES expected count at fixed p is quoted as log^2 p (B2_ACROSS_FIELDS.md l.87) and log^3 p (z31 §(c)); my exact counts (§Z0222) do not separate them. (b) Without the Bradford-Ionascu cone, Z[i] box identities are everywhere (§Z2822), which is the known triviality of ES without positivity; with the cone the Z[i] and Z box rates agree.
4. Main negatives: modular/Shimura Belyi route closed for large p (Z0167, Takeuchi); naive E_p -> ES-surface maps are constant (Z0423); LMU families are diagonal cubics, not ES (Z2300); Legendre-type ternary reduction absent (Z0394).
5. Data: scripts/z52b_p1_L00_*.py; data/z52b/pass1/L00/ (140 KB). Outcomes: data/z52b/pass1/outcome_L00.jsonl.

Draft question for Z1432 (for the parent to send if wanted): "Does any finer invariant than the Brauer-Manin pairing (étale Brauer, descent, or the Harpaz-Wittenberg fibration method) predict integral Hasse failures on the affine cubic surface x y z-type ES family U_n, and in particular does the Brauer class you computed vanish at the fibre k = 0 for a reason that a finer invariant would detect?"

All labels: ES remains OPEN. Labels: PROVED (elementary, re-derived), CERTIFIED (exact integers), EVIDENCE (numerics), Assessment (judgement).

## §Z0082 Vieta-type automorphisms of the ES surface (covered)

Surface: F(x,y,z) = 4xyz − n(xy+yz+zx) = 0 (PROVED, definition). Re-derived lemma (PROVED, elementary):
F = x·(4yz − n(y+z)) − n·yz is **linear in x** (and likewise in y, z). Hence for fixed (y,z) with
4yz ≠ n(y+z) there is exactly one x, namely x₀ = n·yz/(4yz − n(y+z)). A Markoff-type Vieta move
x ↦ s − x would need a second root in x; the only candidate is x₀ itself, so the fibrewise involution is the identity.
Consequence: no nontrivial fibrewise involution, hence no Vieta orbit structure of the Markoff kind on integral points.
Repo already records this in GEOMETRY_ES.md §2.2 ("no involutions", toric model with one point per side) and in the table
row "Markoff-type" (≈ line 403). Contrast: MARKOFF_ES.md §2(b) S_{n,D} has fibrewise Pell orbits only.

## §Z0161 parallel resistors (skipped)

1/R = 1/x + 1/y + 1/z with R = n/4 is exactly the ES equation (PROVED, identity). Known pedagogical identification
(Eppstein's Egyptian-fractions/parallel-resistors page: https://ics.uci.edu/~eppstein/numth/egypt/qgrady.html).
No new test; not a route.

## §Z0167 Belyi / dessins with ES passport (nothing)

* Fermat curve of exponent p: the quotient by μ_p² is a 3-point cover with ramification (p,p,p), so χ = 3/p − 1 ≠ 4/p − 1 (PROVED, standard).
* X(p), X₀(p): triangle type (2,3,∞)-like, cusps, no finite triple with 1/x+1/y+1/z = 4/p.
* Every ES triple has x, y, z > p/4 (since 1/x < 4/p). By Takeuchi (Tak77, Thm 3; 76 cocompact arithmetic
  hyperbolic triangle groups, per Calegari arXiv:2501.01780 §1.1), there is a finite bound M₀ on the entries of arithmetic
  triangle groups (**exact M₀ not checked here**). Hence for p > 4·M₀ no ES triangle group is arithmetic, and a finite-index
  subgroup of a non-arithmetic group is non-arithmetic, so no ES Belyi curve is a modular or Shimura curve. (PROVED modulo the
  cited theorem; the M₀ value is Assessment until checked.)
* Assessment: dessins with ES passport may still exist (Hurwitz-type existence) but no natural (arithmetic) construction does.

## §Z0180 friezes (covered)

FRIEZE_ES.md already contains the ES5 length-3 word dictionary: word (c,m,s), N = mcs − c − s, pentagon quiddity cycle
(h′,c,m,s,h), frozen sides (1,1,1,1,N), Ptolemy relations (P); §1 Thm 1.2 is the even-edge sign theorem (CERTIFIED for 5,115,860 words, N ≤ 10⁵).

## §Z0222 ES count vs Goldbach (covered; calibration numbers recorded)

Exact f(p) = #{x ≤ y ≤ z : 4/p = 1/x+1/y+1/z} for all primes p ≤ 11987 (CERTIFIED, integer re-verification of every hit).
Script: `scripts/z52b_p1_L00_es_count.py 12000` (≈ 1 min); stats: `scripts/z52b_p1_L00_es_count_stats.py`;
data: `data/z52b/pass1/L00/es_counts.csv`, `es_count_stats.txt`.

| p bin | primes | mean f | mean/log²p | mean/log³p | local exponent |
|---|---|---|---|---|---|
| [100,200) | 21 | 28.76 | 1.173 | 0.237 | – |
| [800,1600) | 112 | 68.16 | 1.379 | 0.196 | 3.0 (noisy) |
| [3200,6400) | 382 | 102.48 | 1.446 | 0.172 | 2.6 |
| [6400,12800) | 604 | 122.67 | 1.478 | 0.162 | 2.3 |

Overall slope d ln(mean f)/d ln(ln p) between [100,200) and [6400,12800) ≈ 2.4. Neither log²p (slope 2) nor log³p
(slope 3) fits cleanly on this range; a log²p·(log log p)^c shape would fit. EVIDENCE only; small range.
The Goldbach comparison in the item (ES ≍ log²p vs binary Goldbach ≍ p/log²p) is not a like-for-like count and is not
tested here; the repo's z31 §(c) already draws the structural contrast.

## §Z0224 Croot / Bloom / Liu–Sawhney (nothing)

Read arXiv:2404.07113 (Liu–Sawhney, "On further questions regarding unit fractions"): Thm 1.1 (A ⊆ [1,N] with Σ 1/n ≥ (log N)^{4/5+o(1)}
contains B with Σ_B 1/n = 1), Prop 1.4 (dense A gives B with Σ_B 1/n = s/t, t ≤ exp(C/α)), Thms 1.5–1.6 (unbounded term counts).
None gives a bounded number of terms with dense denominators. Erdős–Graham Problems 305/310 concern unbounded counts too.

## §Z0238 Lehmer totient (skipped)

Sibling only; no concrete first step ("low priority"); φ(n) | n−1 gives no Egyptian-fraction constraint on 4/p. Not actionable.

## §Z0326 Diophantine formalisation (skipped)

ES(n) is Σ₁ by definition (∃x,y,z ≥ 1 with 4xyz = n(xy+yz+zx)), hence Diophantine; a positive-valued polynomial is a standard
MRDP/Jones consequence and carries no arithmetic information about ES. Logic framing already in BRAINSTORM/logic_complexity.md.

## §Z0385 - Z0401 (batch 2)

* Z0385 Legendre negative Pell: covered (canonical_invariants.md (U)); no ES unit produced.
* Z0394 Sun 1-3-5: read Machiavelo-Tsopanidis arXiv:2003.02592. Mechanism: Legendre three-square theorem applied to N(zeta)m - n^4 in the Lipschitz order, then congruence handling mod 3 and 5. ES quaternion discriminant is p*e (QUATERNION_ES.md), so no ternary reduction. nothing.
* Z0395 Gauss Eureka: covered (z52_lit_thin_pointwise.md row); count not uniformly power-sized.
* Z0401 Markoff failures vs ES: covered (markoff_hasse_failures_vs_es.md); no group action in ES (Z0082 lemma).

## §Z0419 - Z0420, Z0423

* Z0419 McMullen 2009: skipped; no continued-fraction or geodesic variable in ES.
* Z0420 EKL: skipped; dimension/a.e. statements for real parameters vs ES single-n integer existence.
* Z0423 congruent numbers / Heegner: nothing. V_n = G_m^2 (GEOMETRY_ES §2.2). A regular morphism from a complete curve E_p into G_m^2 is constant, since the coordinate functions would be units on a projective curve. So a naive E_p -> ES map does not exist. A rational map defined off finitely many points is not excluded by this argument (Assessment).

## §Z0430 - Z0431, Z0489, Z0506, Z0569

* Z0430 BHV and Z0431 Zsigmondy: covered (z45 §1.2 and §B). Primitive divisors of Lucas terms satisfy l = (D/l) mod t, a sign condition, not a construction.
* Z0489 Grunwald-Wang: covered (MENU_LADDER l.26); no GW exception for square classes.
* Z0506 lonely runner: skipped; no ES inequality structure identified.
* Z0569 Graham distinct reciprocal squares: skipped; unbounded term counts (same barrier as Z0224), statement unverified.

## §Z1432 - Z1536 (batch 2)

* Z1432 contact Bright-Loughran: skipped; human action (draft question above).
* Z1472 model theory: skipped; calibration only (fixed-p ES is decidable by bounded search, the uniform statement is outside Presburger/Buchi).
* Z1489 Eichler/quaternion: covered (QUATERNION_ES §1: discriminant pe grows with p).
* Z1536 Hooley divisor sums with moving modulus: covered (technique_transfer_list item 9).

## §Z1799 - Z2044

* Z1799 Groebner identity families: covered by (J)3/(J)78/(J)79 menu-closure theorems.
* Z1897 Sperner grid: skipped; labels not defined on the boundary, no forced boundary condition.
* Z2044 Thm K nonvanishing: covered (METAPLECTIC_ES §4-5; H-E lane).

## §Z2300, Z2649, Z2822

* Z2300 LMU (arXiv:2311.10008): nothing. Their families are diagonal affine cubics a1 u1^3 + a2 u2^3 + a3 u3^3 = a0; ES is not of that form.
* Z2649 Bloom machinery, few terms: covered (addcomb_unit_fraction_density §3.1, N^{1-o(1)} terms vs 3).
* Z2822 ES over Z[i]: nothing. Box search (|xi|,|eta| <= R, Gaussian primes of norm <= 200), CERTIFIED by exact arithmetic:
  - Without cone: 87/89 primes have identities at R=8; median hits 20 (R=8), 34 (R=16), 54 (R=30). Z box: 16/46 at R=8 (signed), median hits 0, 2, 4. Known triviality of ES without positivity (Bradford-Ionascu).
  - With the Bradford-Ionascu cone (Re*Im > 0 for each denominator): fraction of primes with a hit, Z[i]: 0.34 (R=8), 0.38 (R=16), 0.38 (R=30); Z (positive ES): 0.11, 0.22, 0.37. No Gaussian advantage at R=30.
  - 86% of no-cone Z[i] hits satisfy pi | zeta, reducing to 1/xi + 1/eta = (4w-1)/(pi w); Z control also 86% (p | z). Same mechanism in both rings.
  - Scripts: scripts/z52b_p1_L00_gauss_es.py (R, optional 'cone'), scripts/z52b_p1_L00_gauss_es_classify.py, scripts/z52b_p1_L00_z_classify.py. Data: data/z52b/pass1/L00/gauss_es_R*.json, gauss_es_classify_R16.json, z_classify_R16.json.
