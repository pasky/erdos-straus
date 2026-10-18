# ZAREMBA_TRANSFER — the 2026 pointwise Zaremba method, tested on ES in continued-fraction coordinates (O266)

Status: working file (spark relay on O261). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md.
The two 2026 preprints (Shkredov arXiv:2603.14116v2; X. Zhang arXiv:2605.02518v2) are **unrefereed**; anything that uses
them is CONDITIONAL on their correctness. Scripts `scripts/z36_*`; memos `BRAINSTORM/z36_*.md`.

Notation (DEDEKIND_ES): for a prime p and 0 < A < p, `r(p/A)` = Hirzebruch–Jung (HJ) length of p/A = 1 + Σ_{i odd} a_i
where p/A = [a₀; a₁, a₂, …] is the regular CF. `λ(p) = min{ r(p/A) : (A/p) = −1 }`. ES-five(p) ⟺ λ(p) ≤ 3 for p ≡ 1 (8)
(DEDEKIND_ES Cor 4.6, PROVED). `S_L(p) = {A ∈ (ℤ/p)^* : r(p/A) ≤ L}`.

## 0. Iteration log
* cp0: merged O261; read Shkredov §§2, 4, 5.1 (arXiv PDF, pdftotext in /tmp, not committed) and Zhang §3 (Thm 3.6, (3.1)–(3.8)).

## 1. The method, extracted (read in the sources; page refs to the arXiv PDFs)

**1.1 Objects.** Fix q and t = q^{1/2−ε}, N = q^{2ε} (so t²N = q) [Shk §5.1]. `Z_M(t) ⊆ ℤ/q` = numerators a whose CF
digits are ≤ M for all convergents with denominator < t [Shk (24)]. By Lemma 13 [Shk p. 8] Z_M(t) is a disjoint union of
T ≍ t^{2w_M} intervals of length between N and 16MN, i.e. `A = Λ ∔ [N]`, with |A| ≍ q^{w_M} N^{1−w_M} [Shk §5.1]. The
interval J_{u/v} is indexed by the prefix u/v (Shk (28)–(30)): **the prefix fixes the interval, the unresolved tail is the
position inside it.**

**1.2 The gluing.** By CF reversal (Shk (134)–(135)) a ∈ Z_M(t) ∩ Z_M(t)^{−1} has bounded digits at both ends (convergent
denominators < t and > q/t); only the *critical* middle window [t, q/t] = [q^{1/2−ε}, q^{1/2+ε}] is uncontrolled.
* Counting step (Shk Cor 16, via Lemma 14/15 = Bourgain–Gamburd + Helfgott; Zhang Thm 3.6 for all q):
  `|A ∩ B^{−1}| = |A||B|/q + O(√(|A||B|)·N^{−κ})` for A = Λ₁ ∔ [N], B = Λ₂ ∔ [N]; Zhang's form counts
  `(a + 2j)(b + 2j) ≡ 1 (mod q)`, j ≤ N, i.e. `g_j a = −b` with `g_j = [[2j, 1−4j²],[−1, 2j]]`, the generating set
  S = {g_j : j ≤ N} of size q^{2τ} (Zhang (3.1)–(3.5), Remark 1.4). Note g_j = ±T^{2j}ST^{2j}: **the expander alphabet is a
  set of HJ letter pairs with large letters 2j ≤ 2N** — the same kind of letters ES certificates are made of (§3).
* Main term beats error iff `|A|·N^{κ} ≫ q` [Shk (132)]: q^{2ε(1+κ−w_M)} ≫ q^{1−w_M}, i.e. **ε ≳ (1−w_M)/(2(κ+1−w_M))**,
  i.e. ε ≫ 1/M (Shk (133)); Zhang's version τη > 1/M (Zhang (3.8)). κ, η are tiny absolute constants.
* Middle step (Shk §4, Assumption 22, Lemmas 25–33, Prop 35): most a ∈ Z_M(t) ∩ Z_M(t)^{−1} have no M̃-critical
  denominator in the window; this needs ε ≤ ε₀ (an absolute constant; Shk §4 first paragraph: "(61), (99), (119) give an
  upper bound for ε").
* Coprimality / composite q: Lemma 20; Zhang §2 growth for arbitrary q.

**1.3 The threshold, stated exactly (Assessment from the sources).** The method needs a window ε with
`(1−w)/(2(κ+1−w)) ≲ ε ≤ ε₀`, i.e. **1 − w ≲ 2κε₀** — a *near-full-dimension* condition on the digit set, not merely
w > 1/2. Equivalently: each half set must have density ≥ N^{−κ} = q^{−2κε} in ℤ/q (condition (40) of Shk:
|A|N^{κ/2} ≫ q^{1+o(1)}). The gluing count |A|²/q = q^{2w−1}·N^{2−2w} is then a power, but **a power-size count is not
sufficient**: Zaremba with M = 5 (w₅ ≈ 0.837, count ≈ q^{0.67}) is out of reach of the method (Zhang Remark 1.3: "Lowering
this bound to 5 … requires a new idea"). The brief's "M1 power-size main term" should be sharpened to
**M1⁺: half sets of density q^{−o_κ(1)} at the gluing scale.**
