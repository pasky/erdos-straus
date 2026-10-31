# z52b Pass 1, batch L00 (PILOT: first 8 of 30 items; ES is OPEN)

Summary (pilot stop after 8 items; not merged):
1. Counts: covered 3 (Z0082, Z0180, Z0222), nothing 2 (Z0167, Z0224), skipped 3 (Z0161, Z0238, Z0326), needs-compute 0, interesting 0.
2. Interesting items: none. No surprising result turned up; no depth lane recommended from this pilot.
3. Calibration flag: the repo states the ES expected count at fixed p as log^2 p (B2_ACROSS_FIELDS.md l.87) and as log^3 p (z31_unit_fractions.md §(c)). My exact counts (§Z0222 below) do not separate the two; reconcile before using either.
4. Main negative: the modular/Shimura Belyi route for Z0167 is closed for large p (ES triangle groups are non-arithmetic); the Fermat curve gives (p,p,p), not 4/p.
5. Data: scripts/z52b_p1_L00_es_count*.py, data/z52b/pass1/L00/ (1437 primes, < 100 KB). Outcomes in data/z52b/pass1/outcome_L00.jsonl.

All labels: ES remains OPEN. Nothing here is a proof or a certified partial result. Lemma labels: PROVED (elementary, re-derived), CERTIFIED (computer, exact integers), EVIDENCE (numerics), Assessment (judgement).

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
