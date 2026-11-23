<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="6aceadc8b">
A separate reviewer subagent was asked to review the changes in `git log 6aceadc8b..`. Its request and review follow.

Request: review changes since 6aceadc8b carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus Round 3 review of notes/z83/BCM_TS_LDIV.md §0 and §§9–11. Verify merge of mixed DL at bb06ac1bc and §6 elementary prime fields; challenge new finite-history smooth-product proof especially O_M coordinate change at treated primes; challenge all claims in the census, reserve-linear system least/IR closure (minors, boundary strips, host remainders), local shadows, Vieta and Pell potential descent. Check labels (especially no claim about ES or universal invisibility), pointer to IE1_DECIDER §10, exact conditions of TS/QR/least etc, strongest justifiable export. Give concrete fixes for any issue. Use ≤15 min replay and do not edit master files.

Commit log:
commit 96a78179cd6b3af8d1f413728dcd734fa277363b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 05:16:04 2026 +0100

    Merge mixed DL and elementary prime fields; classify tests and prove reserve-linear projected closure

 notes/z83/BCM_TS_LDIV.md | 80 +++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 75 insertions(+), 5 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** §9 holds up and is the real Round 3 gain. The §11 "reserve-linear least closure" is mislabelled RECORD: as a first-order scheme it is essentially a theorem of IOpen. I edited no files.

**Checks I ran (under 2 min, `ulimit -v` set; scripts in `/tmp/r3chk.py` and `/tmp/r3lin.py`):**
- **Vieta:** no solution of x²+y²+1=kxy with k≠3 for x<400, y<4000.
- **Pell:** at every prime p<400 with p≡1 (4), the least positive Pell solution u satisfies u=2x²+1, x from the negative solution (the descent branch).
- **3-adic case:** solvability mod 3^L implies 1+12P is a square mod 3^(L+1), for L≤5.
- **Vandermonde bound:** holds on 2000 random instances.
- **§11 step 1:** the column reduction works on 150 random small instances. Nonnegativity and Ay are preserved, and the large columns end up independent.

## Substance

**§9 merge (mixed DL at bb06ac1bc with the §6 elementary prime fields): sound as an interface audit.**
- Lane 1 §7 needs only a provisional valued field, per-place elementary pair embeddings and reflection of ∃zΨ to B. §6.1's chains of elementary pair extensions keep all three.
- At q>C a mixed branch lands in the henselisation of a Gauss line, so its residue field sits inside old(T̄). New transcendental residues are queued at birth, so Tarski–Vaught survives.
- **Fix:** label it "PROVED (interface audit, not a replay)", as Lane 1 labels its own §8.

**§9 smooth-product finite-history proof: I accept it, including the O_M coordinate change.**
- d>C gives at least εL/log L primes. Removing the primes with v_q(m)>N costs at most Σj_i·L·log2/((N+1)log L), so the product d′ is still >C. The moduli m are cut scalars, so this set is PA-coded.
- At q|d′, q|m, the Picard iterate satisfies w_q(α−a₀) ≥ N·w_q(b) ≥ v_q(m), so Z′=(x−a₀)/m is integral there.
- In the converse direction, Lane 1 §8's freeze makes every coefficient of g(α+m(s+DU)) integral. Substituting back U=(Z′+(a₀−α)/m−s)/D costs at most D^deg g, and D∈C is a unit in B′. Poles off d′ clear with a multiplier coprime to d′, which lies outside M.
- Two points to state explicitly:
  - (s,D) depends on g; that is harmless because D is a unit, but say so.
  - Integrality at q|d′ really is needed. Each such q is already a unit in B′, but there can be nonstandardly many of them, so one multiplier clearing them all might lie in M.
- **Fix:** §7 ("does not establish … for T_Π") and the §8 Round 2 Assessment ("not established for T_Π") now contradict §9. Mark both "superseded by §9". Add §9 to the BARRIER-BROAD triage entry.

**§9 3-adic counterexample in T_pf: correct, and it should be triaged.**
- 3 is a unit in B′ but 3^L is not, so maximal ideals of B′ above 3^L exist.
- 2^e and every q>C are coprime to 3^L, so the fibre is regular, and 1+12p is not a square in k(p).
- Since IE₁⁻ ⊢ DL and DL has ∀E₁ shape, conservation gives T_pf ⊭ U.
- **Fix:** add it to the §0 triage as METHOD-CX. It is not in §0 now.

**§9 nonscalar audit: duplicates IE1_DECIDER §8 ("queue and mixed moduli").** Cite that section. Also correct the wording: the "supplied simple root" step gives a root modulo bh that is ≡c mod b, not "a lift c+bY mod h".

**§11 reserve-linear closure: overclaimed. This is the main issue.**
- **Standard integer A:** {b : ∃y≥0, Ay=b} is defined by a quantifier-free Presburger formula. IOpen proves division by each standard n, so every IOpen model's additive part is a Presburger model. Substituting b=B(t,p) leaves Boolean combinations of polynomial inequalities and congruences mod standard n. Splitting t mod N and using open least-number search (LOpen) gives least search in every IOpen model. So the scheme, and the "parameterized successor induction" consequence, hold in any IOpen model and say nothing specific to these towers.
- **A with nonstandard entries in C:** "entries in C" is not first-order, because C is not definable. If A depends on a parameter p, the scheme must hold for all p, including values outside C, which the proof does not cover. So the "rule soundness" sentence is unsupported for parameter-dependent coefficients.
- The proof steps are correct as instance-level statements (minors, Cramer, root strips, period M, PA-host strip search).
- **Fix:** restate it as an instance-level fact about systems with fixed constants from C (equivalently a scheme over the language with constants for C). Add one line that the standard-coefficient scheme is IOpen-provable, and say it does not bear on U. Remove "RECORD (§11 …)" and drop "reserve-linear projected" from the §0 Result and the STATUS delta.

**§11 other results: correct as scoped.**
- The shadow lemma and "not universal invisibility" are fine.
- The Vieta degree descent is fine. The cases k≤2 are excluded by the order, and the unit argument uses constant units of the polynomial or graded fibre ring.
- The Pell pole-order halving is fine. It uses the regular later fields and the factor calculus for Bézout/GCD rings.
- These are BARRIER-SCOPED or DATA, not STATUS material.

**§10 and the census: conclusions correct.**
- U and IE₁ agree on ∀E. The BCM power-cut argument is valid: the power cut satisfies IΔ₀ and every true ∀E sentence, yet fails BCM, so BCM is not axiomatisable by ∀E sentences over IOpen.
- The binary-form column bounds check: 3A²≤d, C′≤(d+A²)/4, and 4aQ = (2ax+by)² + dy².
- **Fixes:**
  - (a) Cite Kaye, *Diophantine induction*, APAL 46 (1990) as the primary source for the conservation result. The bb06ac1bc §10 lacks that credit, which Lane 1's second R2 audit (1d5bb209f) required. Drop "as requested".
  - (b) Make "Smith 1993" a full citation: Smith, NDJFL 1993 §§2–3, via z80 IE1_SPLIT §10.
  - (c) The † claim that the coinitial queue transfers to the §9 construction is asserted without proof. Downgrade it to Assessment, or add the replay argument for marked and mixed edges.
  - (d) Add a T_mix column instead of the sentence "T_mix has all positive entries common to T_Π and T_pf".

## Form
- **Broken table rows:** the PW row has a spurious extra `+` cell (8 cells against 7 columns). The "Plain successor `L(t>y ∧ t|h)`" and "Prime-primary isolation (`t|h ∧ pt∤h`)" rows contain unescaped `|` inside code spans, which GFM splits into cells. Escape them as `\|`.
- **Dependency pin:** §11 cites IE1_DECIDER §14 at 85d09bf79. That commit is not an ancestor of HEAD and still owes its own R3 review. Add it to the §0 label dependencies and mark the clause conditional on that review. The §0 label also omits z81 §§1,9,13, z75 §1, Kaye 1990 and Smith.
- **Notation:** M means both the maximal ideal (§9) and the common modulus (§11); s means both the scalar content and the freeze centre; a₀ sits next to the DL parameter a. Rename to avoid the clashes.

## Labels
I found no claim about ES and no claim of universal invisibility. "No separation of this model from U or IE₁⁻" is stated consistently.

## Strongest justifiable export (after the Round 3 cross-review)
- **RECORD:** T_mix combines all mixed DL, elementary prime fields at every q>C, host-sorted Boolean affine least search, full Farey/Th(n)/binary reduction and the §6 base package, with ¬ES(P). It fails TS at P, BCM and full unary L(Div) via the smooth-product quintic, and also the true ∀E₁ disjunction Q₂,₃ at P, pending Lane 1's R3 review. No relation to U or IE₁⁻ is asserted.
- **BARRIER-BROAD:** the smooth-product obstruction also holds in T_Π and T_mix, by the finite-history chart change.
- **METHOD-CX:** T_pf fails mixed DL at 3^L, so T_pf ⊭ U.
- **§§10–11:** NULL/Assessment only.

**Suggested STATUS delta text:** "…T_mix combines mixed DL, elementary large scalar prime fields and affine least search with full Farey and ¬ES(P); fails TS at P, BCM and full unary L(Div) (smooth-product quintic, also in T_Π); no separation from U or IE₁⁻ asserted."
</code-review>