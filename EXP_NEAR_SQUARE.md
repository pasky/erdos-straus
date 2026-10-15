# EXP_NEAR_SQUARE — exponential near-squares 4^s + k: mixed profinite points, k = 105, S-unit near-squares (task O235)

Status: checkpoint 1 (O235), awaiting review. **ES is not solved here, nor any infinite case of it unless stated with a complete proof and a
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
`z11_cantor_tree.py` (adaptive branching prime, ℓ ≤ 100, QMAX 10⁶, MMAX 3·10⁵): 20 000 nodes, 13 314 open leaves — the label
tree also explodes at large ℓ (per-ℓ class supply too thin). Not decided at this supply.

**Lemma 1.2 (CRT of squares; PROVED, elementary).** Let P be the set of integer square points of k (exponents x ∈ ℤ with
4^x + k ∈ ℚ^{×2}, here {2, 3, 4, −2}, n_x = s_x²) and σ ∈ C_P = Π_ℓ P a label point. Call an odd prime q ∤ 2k·∏s_x
*σ-pure* if all ℓ | ord_q(4) carry the same label x; then ν(σ) ≡ s_x² (mod q^e) for every e with ord_{q^e}(4) supported on
those ℓ. If every odd prime factor of M is σ-pure (labels may differ between primes) then ν(σ) is a unit square mod M
(CRT of squares; the 2-component k ≡ 1 mod 8 is a 2-adic unit square), hence lies in no ET class of modulus M (an ET
class containing a unit square residue r mod M would contain integer squares m² ≡ r, contradicting ET Prop 1.6 /
(J)55-type T1 vanishing). *So every class covering a label point uses a σ-mixed prime (or a prime dividing some s_x).*
For pure σ (constant label x) only the D_q, q | s_x, survive — D₁₉ (x = 4: needs μ₃ ≡ 4 mod 9), D₄₁ (x = −2: μ₂, μ₅),
D₁₁ (x = 2: μ₅), D₁₃ (x = 3: μ₂, μ₃) — and each depends only on ℓ ∈ supp ord_q(4); a mixed point evades them by putting
a different label on exactly those ℓ. This is the whole mechanism of "mixed points": **they are the points where the
divisor classes of the square points are switched off by the label at the ℓ's of ord_{s_x}(4), and all pure primes
see squares.**

## 2. Why the trees diverge: ℓ-lines through square points (diagnosis)

Tree runs (C, `z11_tree.c`, pool `z11_pool.py` with H ⊇ all ℓ ≤ 200, QMAX 10⁶, MMAX 3·10⁵, LCAP 3·10⁵), uncovered Haar
measure / stuck nodes at depth cap D:
| k | D = 10 | D = 12 | D = 14 |
|---|---|---|---|
| 105 | 9.0·10⁻⁹ / 80 | 3.6·10⁻¹⁰ / 959 | 3.3·10⁻¹¹ / 157 269 |
| 297 | 1.2·10⁻⁸ / 62 | 4.3·10⁻¹⁰ / 1 748 | 2.3·10⁻¹¹ / 128 092 |
The measure falls ~×20 per level but the stuck nodes multiply ~×10–100 per level: a supercritical branching process.
k = 297 has a **single** square point (4³ + 297 = 19²; checked −12 ≤ x < 60), so it has no mixed points at all, yet
diverges the same way. Its stuck nodes are labelled "3" at every split prime except ℓ = 3 (and a few others): they lie
near the **ℓ-line through the square point** X_{x,ℓ} = {μ : μ_ℓ′ = x for all ℓ′ ≠ ℓ, μ_ℓ ∈ ℤ_ℓ free}. On X_{3,3}:
ν(μ) ≡ 19² at every q with 3 ∤ ord_q(4) (≈ 5/8 of primes, pure) and ν_q = 4³ζ + 297, ζ = 4^{μ−3} ∈ μ_{3^j}(F_q), at
q with 3^j ∥ ord_q(4) (generic). This is the exponential analogue of the r-generic lines of (J)26/(J)54 (x_q = 1 for
q ≠ r), but with infinitely many generic primes. Mechanism of divergence: to use a class whose period contains a new ℓ′
the tree must split on ℓ′; the child on the line (μ_ℓ′ = x) is pure at the new primes (Lemma 1.2) and survives, and the
ℓ′ − 1 off-line children are new 2-dimensional lines. Covering converges only if fibres are nearly complete.

**Line coverage (CERTIFIED finite computation of coverage, witnesses not replayed; `z11_line.py 1 297 3 3 9 10⁶ 3·10⁵`).**
On the 3-line X_{3,3} of k = 297 (μ_ℓ′ = 3 exactly for ℓ′ ≠ 3, μ₃ ∈ ℤ₃ free) the whole of ℤ₃ is covered by classes
with v₃(L_M) ≤ 2 and arbitrary other order support (QMAX 10⁶, MMAX 3·10⁵; no residue left at any precision 3², …, 3⁹);
with the smaller supply QMAX 3·10⁵, MMAX 10⁵ one residue (μ₃ ≡ 42 mod 3⁵) remained. So this line is covered (no sterile point on it) — but only by classes whose periods involve large primes ℓ′,
which a tree of Ẑ must split on. The obstruction to a *small* covering is combinatorial (branching), not sterility.

## 3. Other shapes (goal 3)

**Lemma 3.1 (integer unit-square points for c₀·4^s + k; PROVED, elementary).** Let c₀, k > 0, k odd, **4 ∤ c₀ and k ≡ 1 (mod 8)** (R244 repair: for 4 | c₀ the criterion fails, e.g. 12·4^s + 1 = 3·4^{s+1} + 1 has a unit-square point at x = −1; normalise 4 ∤ c₀ by shifting s; k ≡ 1 (8) is the 2-adic condition ν₂ = k ∈ Sq^×). ν(x) for x ∈ ℤ is
a profinite unit square iff c₀·4^x + k = 4^j for some j ≥ 0 (odd part a unit at every odd prime ⇒ the root is ±2^j),
which forces x = 0 when c₀ is odd (x > 0: LHS odd ≠ 4^j unless j = 0, impossible; x = −a < 0: c₀ + k·4^a = 4^{a+j}
with c₀ odd forces a + j = 0, then k < 0) and is impossible for c₀ ≡ 2 (mod 4). So: **unit-square point ⟺ c₀ + k = 4^j.**
Within the non-trivial range (k ≡ 1 mod 8; c₀ + k ≡ 1 mod 3 is automatic) this means (c₀, k) = (3, 1) (j = 1) or
j ≥ 2 and c₀ ≡ 7 (mod 8), k = 4^j − c₀ (e.g. 7·4^s + 9, 15·4^s + 1, 23·4^s + 41, 31·4^s + 33, 7·4^s + 57).
By EXPONENT_COVERING Thm 1.4 (base 4, family-agnostic) and T1 (sterility of Sq^×), **each of these families has no
finite covering by ET classes and divisor classes** (PROVED, relative to the reviewed Thm 1.4). (3, 1) is a subfamily of
(J)22's 3·2^m + 1; the c₀ ≡ 7 (mod 8) series is the same mechanism (EXPONENT_COVERING §5.1, S-unit points) in new shape.

**Survey c₀ ∈ {2, 3, 5}, k ≤ 300 (EVIDENCE; `z8_expnear_survey.py c₀ 300 30000 6 12 18 30 36 60`, coverings found by
the search, not replayed through ec_cert; many are probably Mordell-immediate as R236 D1 found for c₀ = 1).**
| c₀ | non-trivial k | covered (L) | open |
|---|---|---|---|
| 2 | 12 | 41, 65, 89, 113, 137, 185, 209 | 17, 161, 233, 257, 281 |
| 3 | 13 | 25, 49, 97, 121, 145, 169, 193, 217, 241, 265, 289 | 1 (PROVED uncoverable, Lemma 3.1), 73 |
| 5 | 12 | 17, 65, 113, 137, 161, 185, 233, 257, 281 | 41, 89, 209 |
Integer non-unit square points (x ∈ [−12, 60)): every open (c₀, k) has ≥ 1 (mean 2.4: e.g. (5, 209): x = −1, 2, 3, 5;
(2, 17): 1, 2, 4); the covered ones have mean 0.8 (Assessment: square points — and the lines and mixed points through
them — are what make coverings expensive; the correlation is not a dichotomy: (2, 41), (2, 89), (2, 113), (3, 97),
(3, 193) have two square points and are covered; (1, 297), (2, 233), (2, 257), (2, 281) have one and are open).
Two-parameter 4^a·9^b + k: not run (time); note u = 4^a9^b is itself a square, so unit-square points are the
factorisations k = (y − w)(y + w) with w = 2^a3^b, y = ±2^i3^j — finitely many, explicitly listable.

## 4. Which k admit a covering? (goal 4; CONJECTURE + Assessment)

Exact criterion (PROVED, EXPONENT_COVERING Thm 1.4): a finite covering of {c₀4^s + k} exists iff Λ ∩ S′ = ∅.
Known pieces of S′ ∩ Λ: (a) unit squares — *integer* ones occur iff c₀ + k = 4^j (Lemma 3.1, 4 ∤ c₀), PROVED sterile; whether Λ meets Sq^× at non-integer μ ∈ Ẑ is OPEN (the (EH_k)-type question of EXPONENT_COVERING §2; R244 repair: formerly read as a full classification). (b) Nothing else is known.
Non-unit square points x are covered by D_q (q | s_x) on the clopen set {μ_ℓ ≡ x mod ℓ^{v_ℓ(ord_q 4)}, ℓ | ord_q(4)};
the sets around them that the D_q switch off are the *label points* (Lemma 1.2) and the *ℓ-lines* (§2).
* Heuristic for non-sterility (Assessment): a non-constant label point has a positive-density set of mixed primes
  (any q with ℓ^j | ord_q(4) at a level where two labels differ, and one more prime factor); the expected number of ET
  classes containing it, Σ_q τ((q+1)/4)²/q over those q, diverges. Same for ℓ-lines (the q with ℓ | ord_q(4)). So no sterile
  point is expected; every computed point was covered (μ* in II2 919; binary core Result 1.1; the 3-line of 297).
* **CONJECTURE E (weak; exponential coverability).** For c₀ ≥ 1 with 4 ∤ c₀ (R244 repair: false without it, e.g. (12, 1), (28, 9)) and k ≥ 1 with c₀4^s + k non-trivial, a finite covering by ET
  and divisor classes exists iff c₀ + k is not a power of 4. In particular k = 33, 105, 273, 297 (c₀ = 1) are coverable.
  Evidence: certified/surveyed coverings for 9 + 7 + 11 + 9 offsets; Λ ∩ Sq^× = ∅ screens; binary core of 105; line of 297.
  Counter-evidence: none, but the computed coverings for the open k do not terminate (§2): the conjecture predicts
  coverings that are *large* — trees whose class periods involve many primes ℓ ≥ 200.
* What this says about B1. B1 (no finite covering of all n, POINTWISE_SIZE Thm M) uses only that the parameter space
  contains a T1 point. For an exponential family the parameter space is Ẑ (exponents) and its image is not known to meet Sq^× (R244 repair: only integer unit-square points are classified) unless
  c₀ + k = 4^j, so the *qualitative* B1 obstruction is not known to persist (R244 repair: was "disappears"); what remains is *quantitative*: the square points that
  Λ does contain (non-unit) force every covering to contain a covering of neighbourhoods of their label set and lines,
  whose cost is governed by a branching process (fibre completeness ≥ 1 − 1/ℓ). So "finite coverings exist but are
  huge" is the expected shape of B1 over Ẑ-parameter spaces; certificates are practical only when the square points are
  isolated by small-period D_q's (the nine certified k).

## 5. Regenerating the scratch pools (deleted from /tmp to save disk)
Nothing committed depends on them. To rebuild them (single core, ≤ 8 GB; ulimit -v 8000000):
* `mkdir -p /tmp/z11 && gcc -O2 -o /tmp/z11/tree scripts/z11_tree.c`
* k = 105, H ⊇ ℓ ≤ 200 (~6 min, 527 MB): `PYTHONPATH=scripts uv run python scripts/z11_pool.py 1 105 200 1000000 300000 300000 /tmp/z11/p200.bin`
  (same with k = 297 → p200_297.bin, ~6 min); small pools ℓ ≤ 47 (~40 s, 31 MB each):
  `… z11_pool.py 1 K 47 300000 100000 300000 /tmp/z11/p47_K.bin`.
* Tree with depth cap D (§2 table): `/tmp/z11/tree /tmp/z11/p200.bin 300000000 /tmp/z11/t.txt D` (D = 14: ~10 min for k = 105);
  `SHOWSTUCK=100000` prints stuck nodes, labelled by `scripts/z11_stuck_labels.py stuck.txt 4,-2,2,3`.
* Survey outputs for c₀ = 2, 3, 5 are kept in data/z11/survey_c*.txt (16 KB).
