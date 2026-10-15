# EXP_NEAR_SQUARE — exponential near-squares 4^s + k: mixed profinite points, k = 105, S-unit near-squares (task O235)

Status: in progress (O235). **ES is not solved here, nor any infinite case of it unless stated with a complete proof and a
replayed certificate.** Labels as in DISCOVERIES.md. Builds on SIGN_FIELDS.md §1 (O232: Thm 1.3, Lemmas 1.1–1.2,
§1.4), EXPONENT_COVERING.md ((J)22: Thm 1.4 compactness criterion), NEAR_SQUARE.md ((J)55). Memos BRAINSTORM/z11_*.md,
scripts `scripts/z11_*`, certificates `data/z11/`.

Notation. n_s = c₀·4^s + k (c₀ = 1 unless stated). Exponent space Ẑ = Π_ℓ ℤ_ℓ; ν(μ) ∈ Ẑ (n-space) with ν(μ)_2 = k and
ν(μ)_q = c₀·4^μ + k for odd q. A *class* = an ET Prop 1.9 residue class (M, r) (mordell_lib's seven families) or a
divisor class D_q (q | n, q odd prime, q ∤ k). For a class of modulus M = 2^a·M′, L_M := lcm_{q^e ∥ M′} ord_{q^e}(4);
for s ≥ a/2, n_s mod M depends only on s mod L_M, so the class pulls back to a clopen set E_M ⊂ Ẑ of period L_M.

## 0. Plan
1. Tree (per-branch) coverings of Ẑ instead of the global-period lifting of z8_adaptive: a node is a residue u mod L;
   it is a leaf if one class with L_M | L contains it, else it is split to lcm(L, L_M′) for a well-chosen class.
   Certificate size = number of leaves, not the global period. Independent replay checker.
2. Mixed points: classify the Ẑ-points that evade all divisor classes of the integer square points; test sterility.
3. k = 33, 273, 297; then c₀ ∈ {2, 3, 5} and 4^a·9^b + k.
4. Conceptual: which k admit a covering.

## 1. Tree coverings: first runs (k = 105)
`scripts/z11_tree.py c0 k H QMAX MMAX LCAP NODEMAX`: pool = classes whose odd prime powers q^e ≤ QMAX have ord_{q^e}(4) | H.
* H = 2⁶3⁴5²·7·11·13·17, QMAX 10⁶, MMAX 3·10⁵: 439 nodes, 372 leaves, **8 stuck nodes** (no pool class). Stuck nodes, in
  ℓ-adic labels (A: μ_ℓ = 4, B: μ_ℓ = −2, lower case = agreement only mod ℓ^j): 2:A 3:b2 5:A 7:A 11:A 13:B 17:B — binary
  A/B gluings. z8_point (any M ≤ 3·10⁵) finds classes for the binary point (A off {3, 13, 17}, B on them):
  II2 M = 23087 (ord = 7·17·97), II2 125119 (3²·7·331), … — always with a *new* large ℓ (97, 331, 317, 41, 29) in the period.
* Larger H (all ℓ ≤ 43) with the greedy split: node budget exhausted (greedy imports many ℓ, then stalls). Heuristic issue.

**Reformulation (binary Cantor core).** Integer square points of 4^x + 105: x = 2, 3, 4 (11², 13², 19²) and x = −2
((41/4)²); no others for −6 ≤ x ≤ 40 (checked). On the Cantor set C = Π_ℓ {4, −2} ⊂ Ẑ, the ℓ-component is exact, so a class of
modulus M meets C in a cylinder over supp(L_M) (exponents of ℓ irrelevant). Covering C is a finite boolean problem over
{A, B}^S for the finite set S of ℓ involved: script `z11_cantor.py`.

**Result 1.1 (CERTIFIED finite computation, `z11_cantor.py 1 105 4 -2 47 10⁶ 3·10⁵ -g`).** For S = {primes ℓ ≤ 47}, every
one of the 2¹⁵ binary patterns σ ∈ {4, −2}^S lies in an ET/divisor class whose period is S-smooth; a greedy subcover uses
10 classes: D₁₉ (3:A), II2 919 (3:B,17:A), D₄₁ (2:B,5:B), D₁₉₁ (5:A,19:B), II1 35288 (2:A,5:B), II2 419 (11:B,19:A),
II2 1787 (19:A,47:B), II2 27551 (19:A,29:B), II1 32008 (2:B,5:A; period 2²5³), II1 213384 (2:A,3:B,29:A).
With ℓ ≤ 23 only two patterns remain (B exactly on {3,13,17} or {3,13,17,23}). Hence the binary mixed-point Cantor set
C = Π_ℓ{4, −2} of k = 105 contains **no sterile point** and is covered by 10 classes (pattern check exact over 2¹⁵).

**Fibre coverage at the hard core (EVIDENCE, `z11_fiber.py 1 105 23 4 29 113 10⁶ 3·10⁵ 3:-2 13:-2 17:-2`).** Freeze the
uncovered binary point σ₀ (μ_ℓ = −2 exactly for ℓ ∈ {3, 13, 17}, = 4 for the other ℓ ≤ 23) and let μ_ℓ = c vary for one
larger ℓ. Classes with period support in {ℓ ≤ 23} ∪ {ℓ} cover 26/29 residues c mod 29 (missing 6, 9, 13), 24/31, 27/37, …,
62/113. So the neighbourhood of σ₀ needs a genuinely multi-ℓ tree; no single fibre is full at this class supply.
The *tree* must split one prime at a time (single ℓ-steps scored by covered fraction): z11_tree's multi-prime jumps import
large ℓ greedily and exhaust the node budget (200 000 nodes, H = 2⁶3⁴5³7²·∏_{11≤ℓ≤47}ℓ).

**Tree v2 diagnosis.** `z11_tree2.py` (single-prime splits scored by covered fraction, H = all ℓ ≤ 47, pool QMAX 3·10⁵,
MMAX 10⁵): the DFS follows one surviving lineage through all of H and dies at a point that is *generic* at every ℓ
(e.g. μ ≡ 38 mod 2⁶, 34 mod 3⁴, …) — not a mixed point. Such points are covered by classes whose periods involve larger ℓ
(II2 887: ord 443; II2 1487: 743; II2 3035: 2·3·101; …). So the binding constraint for a finite tree is the
**ℓ-range of the class periods**, not the mixed points; H must contain many primes ℓ (exponent 1).

**Quaternary core.** The C tree (`z11_tree.c` on the z11_pool output, H = all ℓ ≤ 200) grinds in a region whose open path is
a gluing of *all four* square points (labels A = 4 on {5, 7, 11, 23, 29, 31}, B = −2 on {3, 13, 17}, c = 2 on {19, 43}, d = 3
on {41}, generic only at 83). So the true mixed-point set is the label Cantor set C₄ = Π_ℓ {4, −2, 2, 3}.
`z11_cantor.py … 4,-2,2,3` (brute force over 4^|S|): ℓ ≤ 19: 2 of 65 536 patterns uncovered; ℓ ≤ 31: 4 of 4 194 304
(all = σ₀ with 19:2, 29:−2 and 23, 31 ∈ {4, −2}). `z11_cantor_dfs.py` (primes in increasing order, QMAX 10⁶, MMAX 3·10⁵):
survivors 4, 4, 1, 1, 2, 4, 1, 2, 4, 2, 4, 8, 8 up to ℓ = 41, then grow ×3 per prime (19 008 at ℓ = 79): for large ℓ the
pool has too few classes whose period support is {ℓ} ∪ (small primes). Next: adaptive choice of the branching prime.
