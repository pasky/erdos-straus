# z52b free lane — `free_opus` (breadth-first connection list for Erdős–Straus)

**ES is OPEN.** Nothing here proves anything. This is a breadth-first list of candidate *connections*. The only filter
was "drop obvious nonsense or literal duplicates". Items were NOT screened against the barrier checklist; many will hit
B1/B2 and that is expected.

## Summary

- **Item count:** see the line below the summary (437 at the time of writing), in 11 sections (A–K).
- **Most common tags:** see the histogram below. The largest clusters are history/literature, reformulations,
  experimental tests, meta/community and character sums/sieves.
- **New exact dictionaries found and checked numerically** (none was found in the repo by `git grep`):
  1. **Frobenius-number form** (0394, 0396, 0401). A word tuv − u − v is the t-th generalised Frobenius number of
     ⟨u,v⟩: the largest integer with at most t − 1 representations au + bv. So (★) says that p is the 4C-th
     Frobenius number of some coprime pair (u, B). The denumerant also satisfies N(n) + N(g_t − n) = t on [0, g_t].
     Both facts were checked for small u, v, t (`scripts/z52b_free_opus_check3.py`). This is classical Sylvester and
     Frobenius-problem territory, so the facts themselves are standard; what is new here is the ES dictionary.
  2. **Weighted projective line and oscillator form** (0418, 0419). This follows from (1): (★) says
     O(p) ≅ ω ⊗ π*O(4C) on P(u,B). The Popoviciu formula plays the role of Riemann–Roch and the symmetry is Serre
     duality. Equivalently, level p is the last level of degeneracy 4C − 1 in a 2D oscillator with frequencies (u, B).
  3. **Triangle-orbifold, Seifert and triangle-geometry dictionaries** (0415, 0421, 0351). Each is an exact
     restatement from standard identities:
     - ES(n) ⟺ some triangle orbifold has χ = 4/n − 1;
     - ES(n) ⟺ some Seifert space M(0;(x,1),(y,1),(z,1)) has e = −4/n and |H₁| = xy + yz + zx;
     - ES(n) ⟺ some triangle has inradius n/4 and integer exradii.
  4. **One-parameter and shift forms of R(p)** (0266, 0268), checked for p ≤ 1009, plus an exact **B = 1 slice
     criterion** (0347): the slice fails iff every prime factor of (p+1)/2 is ≡ 1 (mod 4). This was checked on 8977
     primes; the slice fails for 13.6% of them below 2·10⁵.

  These dictionaries recast (★)/ES in other languages; they do not supply an existence mechanism by themselves.

### 10 items I find most exciting (Assessment)

1. **0394 Frobenius-number form of ES words.** It opens a whole field with its own tools (Apéry sets, Popoviciu,
   Ehrhart, Barvinok) and community; `git grep` found no use of it in this repo.
2. **0401 Denumerant symmetry N(n) + N(g_t − n) = t.** It gives an exact involution attached to every certificate,
   on a thick object of size ≍ p. That is raw material for the open "non-affine windmill" cell (G1).
3. **0355 Signed certificate counts with exact formulas.** The test is cheap: scan χ-weighted counts against OEIS and
   class numbers. A nonvanishing exact formula would be a pointwise mechanism of the (R)/charge-identity type.
4. **0418 Weighted projective line / stacky Riemann–Roch.** It may give Type I and Type II a common geometric home,
   with Serre duality as the T1-carrying reciprocity.
5. **0412 Galois view of the class gate.** It reads d ≡ −1 (mod 4C) as "the Frobenius of d is complex conjugation in
   ℚ(ζ_{4C})". This ties the target class to the real place, i.e. to positivity.
6. **0429 Large-q limit of ES over F_q[T].** It would be an "every prime polynomial" theorem via monodromy, and it
   would isolate the missing integer input precisely.
7. **0253 Sterile points as profinite objects.** The test is whether every sterile point is locally a square at every
   prime. If so, it would link B1 to T1 structurally.
8. **0415 Triangle orbifolds of area 2π(1 − 4/n).** It brings in Riemann–Hurwitz and dessins, and it gives a rigidity
   heuristic for why 3 terms are hard while 4 terms are easy (0416).
9. **0166/0167 Coppersmith and factoring-with-hints.** For C ≥ p^{1/3}, the divisor-in-class question per slice is
   decidable exactly, which helps adversarial verification at astronomical p.
10. **0348 Iterated Landau–Ramanujan.** Each B-slice fails with probability (log p)^{−δ_B}. That gives a clean
    sieve-dimension model of how a (★)-failure is built, testable on the 14 known failures (0349).

### Method and coverage

Free association, organised afterwards into sections:
- A. history and solved neighbours;
- B. arithmetic geometry and automorphic forms;
- C. physics, probability and dynamics;
- D. computer science;
- E. analytic and elementary number theory;
- F. meta and community;
- G. wider mathematics;
- H. reformulations and signed counts;
- I. numerical semigroups;
- J. geometry/topology dictionary;
- K. late additions.

Each item has a concrete first step. Three cheap numerical checks were run to keep reformulations honest:
`scripts/z52b_free_opus_check{1,2,3}.py`. Literature stated as fact was spot-checked by arXiv API or web search, e.g.:
- arXiv:2112.03726, 2305.02689, math/0210333, 1406.6963, 1107.1010, 1103.2879;
- the Bloom–Mehta Lean project;
- Erdős problem #242.

The arXiv API rate-limited midway, so other references are flagged "check whether/verify" in their first step.
`seen:<file>` tags were added automatically by `git grep -i` of a distinctive keyword. They are a hint that the theme
appears in the repo, not a claim that the item does.

**Not done.** No item was taken deep. These were not run:
- the signed-count OEIS scan;
- the χ-weighted counts;
- Type I in the semigroup/stacky language;
- the large-q monodromy;
- the sterile-point square-class test.

The physics, ML and recreational sections are thinner on mathematical content by nature. The citation checks are not
exhaustive (rate limits). Items in the "outreach/community" group need the user's approval before any posting.

Data: `data/z52b/free_opus.jsonl`. Built by `scripts/z52b_free_opus_build.py` from `scripts/z52b_free_opus_batch_*.py`.
