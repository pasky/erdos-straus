# AGENT_REPORT_O20 — verify.py extension (blocks (ci)–(co))

Branch `side-agent/verify-extend-2`. All new blocks are deterministic (fixed
seeds), raise `AssertionError` on any violation, and print one or two summary
lines. Full `uv run --with scipy python verify.py`: **all checks passed**
(exit 0, 3:00 wall total under `ulimit -v 12 GB`); the run without scipy
also passes, with the KARY LP parts skipped and a notice printed. Added
runtime ≈ 11 s (max block 7.8 s, (co)).

| block | document | what is checked | reused code |
|---|---|---|---|
| (ci) | EXCEPTIONAL_TWIN3 | Lemma 3.2: per-dyadic-box counts `≤ min(V(T/j+1), 2T(V/j+1))` and `≤ UW/j+min(U,W)` for every class (j = 13, 31, 101); assembled lemma (diag ≤ ζ(2)²ζ(3)² / ζ(2)², off-diag ≤ 2·mass·sup-tail, sup-tails ≤ the explicit box sums, mass ≤ (1+log Y)²) at Y = 300, j = 101, 211, 1009. (2.1): 2·10⁵ random pointwise; toy class system (k = 1, C₀ = 1, X = 2·10⁶): `Σmin(V,1)² ≤ 2·mass_small + 2ΣV_large²` | logic of reviews/exceptional-twin3-check.py partA/B and scripts/twin3_system.py, re-implemented with asserts |
| (cj) | EXCEPTIONAL_TWIN4 | Lemma 2.3 exactly on 72,328 (s ≤ 4, w, q, x, b) cases, N = 2·10⁶ (worst lhs/bound 0.126); the proof's d-step (Ω(d) ≤ s−1, Σ1/d ≤ ΣHⁱ) | reduced reviews/exceptional-twin4-check-lemma23.py |
| (ck) | EXCEPTIONAL_KARY | Lemma 2.3: §3 node sets give log B ≤ (2.1) and ≤ (3.1) on 1760 (n,t,d) (margins −5.66, −7.58), B ≥ 1; g(1) ≤ B·E g on 300 random nonnegative multilinear g. With scipy: B* (LP) ≤ B and B*(d=0) = 1; Thm 2.5 weighted LP ≤ 1 on 30 random plain-law systems (explicit Lagrange B, t = d/(EM+4d)) | node sets from scripts/kary_b21_check.py; LP/paths from scripts/kary_check.py (imported) |
| (cl) | EXCEPTIONAL_KARY2 | Lemma 2.1(1) brute force (M ≤ 1500); 2.1(2) and 2.2 (12,000 (a,D), 16,406 Case-A classes) with live control; Lemma 2.3 at (W,Q₀) = (7, 5040), (11, 18480): \|R\| matches part 2 exactly, every class of the four types with modulus \| Q₀ avoided (live shifted control), (R2) bounds | scripts/kary2_square_check.py (imported) |
| (cm) | EXCEPTIONAL_NONCRT | Lemma 2.2 on 2 × 40 random systems (max ratio 0.923/0.924, float); Θ_S pairwise disjoint and ∌ 0 (exact) | scripts/noncrt_checks.py part1 (imported) |
| (cn) | POINTWISE_OMEGA5 | Lemma 1.1 (bijection n = st², count ≤ X/q+1 for q ≤ 80, all w), Cor 1.2 (7895 cases); control: without squarefreeness the bound fails | new |
| (co) | POINTWISE_WINDOW | Lemma 1.2 parity on 73,938 (p,q); Lemma 1.1 (bad-free ⇒ window fails, via rat_hits); q = 3 converse; W1 data: one reduced class mod 840d for 291 sifting d, g(d) = 1/φ(d), 1−g(ℓ) identity, Step-2 parity for p ≡ 1 (840) < 4·10⁶, §3 table regression (395, 244) at x = 10⁶, Step-4 Euler-product inequality | rat_hits from scripts/pointwise_size_amin.py |

POINTWISE_OMEGA3's composition inequality was already block (cc); not duplicated.

**Scope caveats.** These are toy-scale and finite checks of the stated
algebra/inequalities. They are not evidence for the asymptotic theorems.
The KARY and NONCRT LP/Walsh checks use floating point. In (ci), (2.1) on the
toy system uses C₀ = 1, as in TWIN3 §5. The proof needs C₀ ≥ 6 and j > L⁸.
Not tested (as in the documents): the Brun–Titchmarsh constant of TWIN3
Lemma 3.1, the cited sieve theorems S1–S3 of W1.

Docstring and STATUS.md housekeeping updated.
