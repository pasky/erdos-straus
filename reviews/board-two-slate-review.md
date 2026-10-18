# R284 — hostile review of O273 (board #2 slate)

Reviewer: R284 (side-agent/review-board-slate). Author branch merged: `side-agent/board-two-slate` @ abd351d7.
Documents: BOARD2_SLATE.md, FORCED_WINDOW.md §8, ZAREMBA_TRANSFER.md §2 attribution note, scripts/z42_*, logs/z42_*.
From-scratch scripts: `scripts/review_r284_*.py` (no code shared with the author's).

## Summary verdicts

| Claim | Verdict |
|---|---|
| (1) ABH transfer λ(p) ≤ (6/π²) L log L + O(L), KNOWN | (in progress) |
| (2) FORCED_WINDOW Thm 8.5 (Lemmas 8.1–8.4) | (in progress) |
| (3) Lemma 3.1/3.2, M(n), Prop 3.3/3.4 (45/(8π²)), Thm 3.5 (45/(32π²)) | (in progress) |
| (4) 8/n zero-law diagnostic to 10⁹ | (in progress) |

## (1) ABH transfer — checked against the source

Source: arXiv:2210.14095v2, downloaded by R284 (PDF + HTML). Verified verbatim:
* Thm 1: for N ≥ 3, 0 < t ≤ (log N)^C, (1/φ(N))·#{a ∈ ℤ_N^* : |S(a/N) − (12/π²) log N log log N| ≥ t log N} ≪_C 1/t
  (two-sided, absolute value present).
* Thm 6: same range, #{a : |D(a/N)| ≥ t log N}/φ(N) ≪_C 1/t (two-sided).
* (5) Barkan–Hickerson: D(a/N) = ((−1)^r − 1)/8 + (1/12)(a/N − (−1)^r[0; a_r, …, a₁] − S_alt) with
  S_alt = Σ_{i=1}^r (−1)^i a_i, hence D = −S_alt/12 + O(1).
* Convention a/N = [0; a₁, …, a_r], a_r > 1, and ℤ_N^* = {1 ≤ a ≤ N, (a, N) = 1}: as the author says.

Re-derivation. Fix C = 1 and an absolute t₀ with both exceptional proportions < 1/4 (legitimate: implied constants depend
only on C; needs t₀ ≤ log p, i.e. p ≥ e^{t₀}, small p go into the O). The good set has > (p−1)/2 elements, so it contains a
non-residue A. Σ_{j even} c_j = (S + S_alt)/2 ≤ ½[(12/π²)L log L + t₀L] + ½[12t₀L + O(1)]. With the campaign's
r(p/A) ≤ 1 + Σ_{i odd} a_i(p/A) and p/A = [a₀; a₁, …] ⇔ A/p = [0; a₀, a₁, …] (odd digits of p/A = even digits of A/p),
λ(p) ≤ (6/π²) L log L + O(L). Correct. The "typical constant" remark (most QNR have r = (6/π²)L log L + O_t(L)) also
follows, using the lower tail of Thm 1, Thm 6, and r ≥ Σ_even (see numerics: δ ≤ 1); exceptional proportion among QNR is
≤ 2× that among ℤ_p^*. Fine.

From-scratch numerics (`scripts/review_r284_abh.py`, all QNR at p = 1009, 1013, 10007, 10009, 100003, 100049, 1000003):
δ := 1 + Σ_even c_j(A/p) − r(p/A) ∈ {0, 1} always; max |S_alt + 12 D| = 2.82, 2.94, 2.93, 2.98 (exact Dedekind sums,
p ≤ 10009); median r = 10, 11, 15, 15, 20, 20, 25 vs (6/π²)L log L = 8.1, 8.1, 12.4, 12.4, 17.1, 17.1, 22.1.
Reproduces the author's numbers.

**Verdict (1): SOUND.** Label KNOWN (corollary of ABH) is right. Minor wording only:
* m1 (MINOR) ZAREMBA_TRANSFER note says "read in v2 HTML", BOARD2_SLATE (1) says "Read arXiv:2210.14095v2 myself" — harmless;
  both v2 PDF and HTML agree on Thms 1, 6, (5).
* m2 (MINOR) The ZAREMBA note's "Argon route … would give only an o(L log L) remainder, weaker than ABH's O(L)" is an
  unsupported guess about an unwritten proof; it is already labelled CONJECTURE-level sketch, acceptable.
