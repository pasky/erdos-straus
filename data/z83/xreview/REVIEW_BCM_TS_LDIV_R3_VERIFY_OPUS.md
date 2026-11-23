<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="df1e13ca4">
A separate reviewer subagent was asked to review the changes in `git log df1e13ca4..`. Its request and review follow.

Request: review changes since df1e13ca4 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused R3 export verification. Check all 96a78179c review fixes versus notes/z83/BCM_TS_LDIV.md §0,§§9–11 at 1761eda47. In particular independently audit the NEW pure-language guard (G) in §11: scalar descent of Pell units on all upper algebras, PA fundamental unit, exponent bound/residue, nonstandard guarded range, exact parameterized IR scope. Check table columns and the 3-primary U separation plus the merged smooth-product statement. Give EXPORT ACCEPT or necessary fixes; do not edit, replay ≤15 minutes.

Commit log:
commit 1761eda4756c1da65dcab5a257ab72b2d0336b8a
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 05:35:13 2026 +0100

    Fix census and reserve scope; certify parameter range by an arithmetic Pell guard

 notes/z83/BCM_TS_LDIV.md | 83 +++++++++++++++++++++++++++---------------------
 1 file changed, 47 insertions(+), 36 deletions(-)

Review:
**Verdict: EXPORT ACCEPT WITH ONE NECESSARY FIX.** As written, the new guard (G) in §11 does not bound the matrix entries, and its corollary is refuted by the note's own §1/§7 quintic. A one-token fix to (G) repairs it. Every other 96a78179c fix checks out, apart from small wording points. I edited nothing. My checks were a cell-parse of the census table, an ancestry check of the pinned commits, and a Pell script, all within the 15-minute replay budget.

### Necessary fix: §11, guard (G)
- **Problem.** (G) puts no sign condition on `Y`. Take `X=s+1`, `Y=−1`. Then `X²−DY²=(s+1)²−(s²+2s)=1`, and `Y=s·(−1)+(s−1)`, so `c=s−1`.
  - `s` can be any Pell abscissa of `3+2√2` in the cut, for example about `H^{1/2}`. Then `c∉C`.
  - I confirmed `c=s−1` numerically for s = 3, 17, …, 665857.
- **Consequence.** The guard then admits `A=(h²)`. The state `∃y≥0 (h²y=(1+u)((1+u)²−P)²)` is exactly instance (1). By §1 and §§7/9 it has no least element in T_mix. So "valid (G) ⇒ c∈C" and the guarded least-search/IR corollary are false as written.
- **Where the proof breaks.** It silently assumes `Y≥0` when it writes "`X+Y√D=e^n` for a PA `n≥0`".
- **Fix.** Add `Y≥0` to (G); `j≥0` then follows. The sentence "Use nonnegative coordinates throughout" does not cover this: it reads as being about the witness `y` and sign-splitting `A`, not about the guard variables.

### Audit of (G) once `Y≥0` is added: correct
- **Scalar descent.** For every nonsquare scalar `D`, norm-one pairs descend through all the upper algebras, using the same unit/contraction pattern as the accepted Vieta and Pell arguments:
  - free lines, Farey/paired edges, and marked/mixed edges: arithmetic ring inside upper `A[x]`, so units are constants;
  - unit rows: units after inverting a pivot are constants, then contraction;
  - spheres: degree filtration, with the rank-4 cone geometrically integral over `K(√D)`;
  - regularity over `K` keeps `1,√D` independent.
  
  So `s,v` are scalars. `D=s²+2s` lies strictly between `s²` and `(s+1)²`, so it is nonsquare; hence `X,Y` are scalars too, and so are `j,c` by unique division. Suggest citing z81 §9 at the point of use.
- **Fundamental unit.** `e=s+1+√D` has ordinate 1, so it is fundamental. Its powers satisfy `X_n≡1` and `Y_n≡n (mod s)` by the recurrence, so `c=n mod s≤n`. Since `e>2`, `2^n<2X`, giving `n<log₂(2X)≤j₀L+1∈C`, because `L^k<2^L`.
- **Nonstandard example.** `n=⌊L^{1/3}⌋` with `s∈(n,12(n+1)]` works: `(2s+2)^n<H` and `c=n`.
- **Scope wording to add.** The range of `c` accepted by (G) is only O(L). That is a tiny initial part of `C` (it excludes, for example, `2^{√L}`). Also say explicitly that the corollary is claimed for T_mix only.
- **Guard logic is sound.**
  - Least search on `¬G∨V` and on its complement is trivial for invalid tuples and instance-level on valid ones.
  - Polynomial witness bounds enter as linear slacks.
  - The least counterexample gives the IR conclusion from premises that are merely true in T_mix.
  - The disclaimers (IOpen does not force a small range, `C` is not definable, unguarded parameters are not covered) are right.

### The other 96a78179c review fixes, checked against §0 and §§9–11
- **§0:** "reserve-linear" is dropped from the Result and the STATUS delta. Triage now has RECORD §9, METHOD-CX for the 3-adic T_pf case, BARRIER-BROAD including §9, and DATA for §§10–11. "Fails TS at P … also in T_Π" is added. The added dependencies (Kaye, Smith, z81 §§1,9,13, z75 §1) are in the label. ✓
- **Pins:** bb06ac1bc, 00ff92258 and 6e8f6e7a2 are all in the Lane 1 merge 78d84212f; 00ff92258 is its second parent. They are not ancestors of this branch, which is the existing convention. The bb06ac1bc→00ff92258 changes in §§6–9 are clarifications only. ✓
- **Table:** a code-span-aware parse gives 7 cells on all 20 rows, with no raw `|` inside code spans (`∣` is used instead). The T_mix entries are consistent with §§6 and 9:
  - Π/DL `+ / +`;
  - plain/affine/`L(Div)` `+ / + / −`;
  - TS `− / +`;
  - BCM `−`;
  - two classes `−`;
  - numerical leastness `? †`, and the † now says this is undecided. ✓
- **3-primary U separation (`h=3^L`, `b=3`, `a=P`):**
  - `3^L∉C`, so maximal ideals of `B′` above it exist.
  - All marking moduli are coprime to `3^L`, so the fibre is regular over `k(p)`.
  - A lift would give `(6x+1)²=1+12p`, which is impossible there.
  - All divisors are powers of 3, so there is no coprime escape. ✓
- **Nonscalar Hensel paragraph:** now cites IE1_DECIDER §8 and says "≡c mod b, solves mod bh". ✓
- **Merged smooth-product statement:**
  - the renaming to `ξ_N` and `h_s` is done;
  - it now says that `(s,D)` depend on `g`, which is harmless;
  - it now justifies checking integrality on the whole sublist;
  - the `N` choice and the count of `v_q m>N` primes are correct;
  - the Picard gain `w_q(α−ξ_N)≥N·w_q(b)≥v_q m` holds;
  - §7 and the §8 "not established for T_Π" are marked superseded. ✓

### Minor fixes (non-blocking)
1. In the §8 Round 2 Assessment, "Mixed `DL` plus the elementary prime fields *with the same smooth-product obstruction* is not asserted" still contradicts §9. Tag it "(Round 2; asserted in §9)".
2. In §11's Counting bullet, "R3-reviewed revision 00ff92258 (review at 6e8f6e7a2)" is imprecise: the review was of 85d09bf79, archived at 6e8f6e7a2, and 00ff92258 holds the fixes. Say that.
3. In §0 Scope, "Rule closure here is for the §11 witness class" should add "instance-level, plus the (G)-guarded range in T_mix".
4. Optionally, add pages 420–438 to the Smith NDJFL citation.

No ES claim appears anywhere, and the labels are scoped correctly. With the `Y≥0` fix, the STATUS delta as proposed is exportable; it does not quote §11.
</code-review>