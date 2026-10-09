# R100 — hostile review of POINTWISE_MORDELL13C.md (task O100)

Reviewer: side agent R100 (branch `side-agent/review-m13c`). Reviewed against `side-agent/r13-cover-all`
as merged at the start of R100. All code from scratch: `scripts/review_m13c_*.py` (no import of `m13c_*`,
`mordell_lib`, `review_mordell_check`).

## Summary verdicts

| Claim | Label claimed | Verdict |
|---|---|---|
| Thm 6.1 (tree certificate, 35459 open classes, density 8.42e-5) | PROVED (finite computation) | **SOUND** (conditional on POINTWISE_MORDELL Thm 3.1(b) outside the six roots, as stated) |
| §2 witness engine completeness (all M ∣ L) | CERTIFIED | **SOUND** (brute force, 6 levels, 0 mismatches) |
| Comp. 3.1 ((2,2) cell uncovered set) | CERTIFIED | pending |
| §5 x** search extensions | CERTIFIED within ranges | pending |
| §1, §3, Comp. 2.1 | EVIDENCE | pending |

## A. Theorem 6.1 — independent re-check

**Family lemma (re-derived by reviewer, PROVED).** For each ET Prop. 1.9 family (statement checked in
`sources/elsholtz-tao-1107.1010.pdf`, §1 and §10; ΣI/ΣII coordinates and maps
π^I = (abdn, acd, bcd), π^II = (abd, acdn, bcdn) from ET §2) put, for n in the class:

| family (params) | class | auxiliary coordinates |
|---|---|---|
| I1 (a,d,f), f ∣ 4a²d+1 | n ≡ −f (4ad) | c=(n+f)/4ad, e=(4a²d+1)/f, b=ce−a |
| I2 (a,c,f), (4ac,f)=1 | n ≡ −f (4ac), an ≡ −c (f) | b=(an+c)/f, d=(n+f)/4ac |
| I3 (c,d,f), (4cd,f)=1 | n ≡ −f (4cd), n² ≡ −4c²d (f) | a=(n+f)/4cd, b=(n(n+f)+4c²d)/(4cdf) |
| I4 (a,b,e), e ∣ a+b, (e,4ab)=1 | n ≡ −e⁻¹ (4ab) | c=(a+b)/e, d=(ne+1)/4ab |
| II1 (a,b,e), e ∣ a+b | n ≡ −e (4ab) | c=(a+b)/e, d=(n+e)/4ab |
| II2 (a,d,f), 4ad ∣ f+1 | n ≡ −4a²d (f) | c=(f+1)/4ad, e=(n+4a²d)/f, b=ce−a |
| II3 (a,d,e), (4ad,e)=1 | n ≡ −4a²d−e (4ade) | c=(n+4a²d+e)/4ade, b=ce−a |

Each coordinate is an integer for every n in the class (the I3 `b` needs `n(n+f)+4c²d ≡ 0` mod 4cd and
mod f, coprime — this is where (4cd,f)=1 is used); the 4/n identity holds as a rational-function identity
(sympy, `review_m13c_extra.py`: all 7 True); every coordinate is positive and non-decreasing in n, so
positivity at the least positive element of a progression gives it on the whole progression.
(Note: ET's printed I3 `b`, `(n²+4c²d+nf)/(4cdf)`, equals mine; a first version of my checker used
`((n+f)²+4c²d)/(4cdf)` — that is ET's `e·c`, not `b` — and correctly rejected 9469 I3 leaves; fixed.)

**Checker `scripts/review_m13c_tree.py`** (1.6 s): for every split, children = exactly the units mod Lq over
x mod L (q lifts if q ∣ L, else q−1, the omitted one ≡ 0 (q) containing only the prime q ≤ 83, for which ES
is classical); every node has 0 < x < L; Haar masses sum to 1 per root (exact Fractions). For every covered
leaf: side conditions, own CRT for the class (I3: all square roots mod f), recorded M equals the class
modulus, recorded r is in the class, M ∣ L, x ≡ r (M), and the explicit solution is a positive-integer
solution for n = x + Ls, s = 0..4 (the lemma makes this redundant beyond s = 0, but cheap).

Result: **6000 splits, 136494 covered leaves, 35459 open leaves, 2140 distinct ET classes, 0 errors.**
Open mass per root: 112561: 1.263e-4, 352801: 3.101e-4, 380881: 1.934e-5, 418321: 5.81e-6,
473761: 1.616e-5, 483841: 2.776e-5; mean over the six = **8.424e-5** — all as claimed.
Split primes used: {2,3,5,7,17,…,83} (max 83 ✓); all open-leaf moduli divide
2⁴·3²·5²·7²·11·13·∏_{17≤ℓ≤83} ℓ ✓. Roots = the six classes of POINTWISE_MORDELL §3 / Thm 3.1(b), all with
(·/13) = −1 ✓. 8.42e-5·6/2160 = 2.34e-7 ✓.
Negative controls (`review_m13c_extra.py`): perturbed leaf parameter, deleted child, wrong residue,
open leaf faked as covered — each rejected.

**Verdict: SOUND.** The theorem as stated is a correct consequence of Thm 3.1(b) + this certificate.
Defects for this claim: see D1–D2 below (minor, presentation).

## B. §2 complete witness engine

`scripts/review_m13c_witness.py L`: own enumeration of **all** ET parameter tuples with class modulus
dividing L (parameters bounded by divisibility: I1 `f | 4a²d+1`; I4/II1 `e | a+b`; I2/I3/II3 `4uf | L`;
II2 `f | L`, `4ad | f+1`), own residues (I2/I3 by direct scan of the progression `−f mod 4u` up to M, I3 all
square roots), then the full witness set `{(fam,P)}` of every unit x mod L compared to
`m13c_witness.witness_all(x, L, first=False)`.

| L | classes | units | incidences | mismatches |
|---|---|---|---|---|
| 840 | 1118 | 192 | 8821 | 0 |
| 9240 | 4117 | 1920 | 113942 | 0 |
| 6720 = 2⁶·3·5·7 | 6055 | 1536 | 132313 | 0 |
| 31824 = 2⁴·3²·13·17 | 5438 | 9216 | 463989 | 0 |
| 55440 = 2⁴·3²·5·7·11 | 16470 | 11520 | 1202237 | 0 |

Levels 6720 (2⁶), 31824 (odd prime squares 9 and no 5,7) and 55440 were not used by the author. I also read
the docstring reductions: each is correct (I1: if `f > 4ad` then `g = N/f < 4ad` and `g ≡ −1/x` since
`fg ≡ 1 (4ad)`; II1/I4: `e ≤ a+b < 4ab`; II2: `d ≤ (f+1)/(4a) < f`). **Verdict: SOUND** as a statement about
`M | L` with `4 | L` (the engine returns ∅ if `4 ∤ L`, where II2 classes with odd `f | L` would still exist —
irrelevant for the campaign, where `16 | L`; see D3).
Comp. 2.1 (1399 survivors at L = 6.96·10¹⁰) is EVIDENCE and was not recomputed independently.

## Defects

* **D1 (MINOR, §6 proof, "two independent checkers").** Both author checkers are campaign engines
  (`mordell_check` sympy engine, R80 `review_mordell_check`); the second is an earlier reviewer's code, so
  "independent" is fair, but the dependency on Thm 3.1(b) (outside the roots) should be named in the theorem
  statement's label: "PROVED by finite computation, given POINTWISE_MORDELL Thm 3.1(b)". Repair: one phrase.
  R100 adds a third independent checker (`scripts/review_m13c_tree.py`), which may be cited.
* **D2 (MINOR, §4 "for p∤L the one non-unit child can contain only the prime p itself").** Correct, but the
  omitted child consists of multiples of q in the root class; its only possible prime is q itself, and
  q ≤ 83 < 112561 ≤ every positive element of a root class, so it contains **no** prime at all. The
  "ES checked directly for the split primes" step is therefore vacuous. Repair: say so (harmless).
* **D3 (MINOR, `m13c_witness.py` docstring / §2).** `witness_all` returns the empty list when `4 ∤ L`
  although II2 classes (modulus f odd) can have `M | L` then. Never triggered in the campaign (all levels
  are multiples of 16). Repair: state the hypothesis `4 | L` in §2 and the docstring.

## C. Computation 3.1 — work log (in progress)

Reduction (reviewer, re-derived): 13B §4 already enumerated every ES level N ≤ 4·10⁷. For T-level F | 11²13²,
ES level N > 4·10⁷ only for II3/I1/I3 with a_T (resp. c_T) = 11²13², d_T = e_T (f_T) = 1
(other T-splits give N = E·a_T²·d_T ≤ 1859²·11 < 4·10⁷). For these, with λ = 11⁴13⁴ = N, the T-generic
data are exactly the (a',d',m,j), a',d' prime to 143, with `4a'd'mj = λa' + m + j` (e = 4a'd'm − 1, cofactor
4a'd'j − 1 of 4a²d+1), and the subcell is u ≡ −e (mod 11²13²) — the same set for all three families.
Independent complete enumeration: `scripts/review_m13c_cell22.c`.
