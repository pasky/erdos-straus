<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="d94456de1">
A separate reviewer subagent was asked to review the changes in `git log d94456de1..`. Its request and review follow.

Request: review changes since d94456de1 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review, FINAL round: check notes/z80/IE1_SPLIT.md §§16–19 and §0, fde6146e4. Is scalar-factor closure exact under directed unions of increasing PA coefficients, all old requests vs actual coefficient ring, strict ES preservation under elementary arrows and not silently transferring external finite support? Re-derive the new linear-error gap G at seed by Laurent Gauss and at floor/row/sphere by derivatives/monic angular test; verify explicit non-reducible form and prime short-vector/Farey obstruction against every order/valuation assumption including J-clearing and unbounded cofinal B. Check IE1^- formula classes in §18 (divisor-minimal bad, definability vs least number), final matrix and §0 statuses including conditional scopes. Every contradiction or missing lemma is important. Give commit hash and explicit export verdict/fixes. No file edits/computation needed.

Commit log:
commit fde6146e46d30871d2e2beb356574134fa7e9448
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 20:16:10 2026 +0100

    Close scalar-union loophole and refute full reduction by a persistent linear approximation gap

 notes/z80/IE1_SPLIT.md | 113 +++++++++++++++++++++++++++++++++++++++++++++----
 1 file changed, 104 insertions(+), 9 deletions(-)

Review:
**Review of fde6146e4 (only `notes/z80/IE1_SPLIT.md` changed; d94456de1..fde6146e4)**

**Verdict: ACCEPT WITH MINOR FIXES. Export is fine once the fixes below are applied.** I checked §§16–19 and found no mathematical errors. The real problems are missing qualifiers, one table row that mixes two models, and stale text elsewhere in the note. This counts as one cross-lab review for §§16–19, so the "cross-review owed" tag on those sections can be dropped once the fixes are in.

### What I re-derived

**§16, scalar-factor closure and the diagonal limit**
- **Largest PA subring.** The proof is correct. If z is not in B, the elements z+j are non-units in A, since R∩K=B. They are pairwise comaximal, because their differences are nonzero integers. So they have distinct horizontal prime factors, and those primes persist. A fixed h≠0 cannot be divisible by all of them, since it has only externally finitely many horizontal factors. The proof relies on external finite support, and the note keeps it confined to the geometric models.
- **Closure under directed unions.** This is exact. The property ∀t,b (0≠tb∈B → t,b∈B) can be checked at a single stage containing t, b and h. So it passes to any directed union with R_i⊆R_j and B_i⊆B_j, even if B_j∩R_i is larger than B_i. The factorial test with L=1, y=P and b>2P (b in B_*) then contradicts closure. The argument actually needs only that B_* is a model of PA; elementarity is just one way to guarantee that.
- **Old requests versus the actual coefficient ring.** This is also correct.
  - δ_i lies outside the whole of R_i, not just B_i. It sits in D_{i+1} because ∀x(0<x<a → D(x)) holds by elementarity.
  - The approximation sentence (2y/3, 3y/4) is first-order and transfers.
  - Of v and v+δ_i, at least one lies outside B_i, and both lie in (y/2, y).
  - So every stage's subring is served while the union's own ring B_* fails.
- **ES preservation.** ¬ES(P) survives every elementary arrow because ES(P) is existential. The note says it uses only the first-order consequence of factor closure and makes no claim about finite horizontal support in the union. That is correct.
- **Missing context.** M_* is an elementary extension of M_0, so it fails IE₁⁻ immediately, because M_0 already does. The "fair test" therefore only illustrates the request-servicing logic. It is not a construction-level result. Scope hints at this ("preserves Model 2's first-order theory"); §16 itself should say it.

**§17, the linear-error gap (G)**
- **Seed.** Substitute P=(z+z⁻¹)/2 and α=(z−z⁻¹)/2. Then x−αy becomes a nonzero Laurent polynomial with nonzero coefficients N/(2J)^e, where N is a nonzero element of B, so |N|≥1. The residue of z/(JH) is 2η̄, which is transcendental over the residue field of rc(K). So the size of the sum is at least any single nonzero term divided by a C₀-scalar. That gives a bound of at least P^{−(e+k+2)}, using JH<P, 2J<P and C₀<P. Correct.
- **Line, floor, row and sphere edges.**
  - Clearing by J_e^m with m standard is valid: J_e lies in C, which is below C₀ and hence below P.
  - The k-th Y-derivative, or ∇^k on a row, is well defined; ∇ kills au+bv−1. It gives a nonzero pair in R_A, using constant contraction and restriction of valuations.
  - The top η-coefficient equals (scale^k/k!) times the old error, with every scale ≥1.
  - Freshness over the *whole* old real closure takes care of coefficients that involve α.
  - On the sphere: after reducing by s∈R_A, the monic normal-form coefficients lie in R_A. Distinct monomials give independent angular monomials, because 1−Ση̄² is not a square over k(η̄). Each weight s^{deg/2} is at least 1.
  - Floor centres β are never used as coefficients. All edge types in §§9.3, 12 and 13 are covered, and so is Model 1.
- **The non-reducible form.** For Q=(S²U−aV)²+V², a reduced form forces 3A²≤4S⁴. That gives |S²x−ay|<2S and |y|<2S, hence |x−αy|<4/S, which contradicts (G) because S>4P^n for every standard n. Correct.
- **Prime short vector.** Here α−t>1/2 and x=tY+(a'Y−X')/l lies in R, giving |x−αY|≤2/√l. Correct. This is consistent with PA: R/lR is not B/lB because B is not initial. It is also consistent with §15, because short vectors still exist for roots of −1.
- **Independent proof of ¬IE₁⁻.** Because z79 §4 proves Farey and short vectors in IE₁⁻ and z79 §9 proves reduction, §17 independently shows the model is not IE₁⁻. Nothing earlier in the note assumes Farey holds in the model.

**§18, minimal failures**
- The divisibility-minimal failures are exactly the bad irreducibles. The scaling argument works in IOpen. Irreducible implies prime by z79 §4. The resulting definition is U₁, and it gives a set, not a least element.
- The localization block is valid. Uniqueness makes s the same in every valid block. A reducible r gives a factor r₁ with r₁+j+1≤r+j≤s. The formula is E₁ inside the decode. Note that the z75 §1 "L(D)" is a property of a model, not a theorem of IE₁⁻, so the hedge "§7 alone does not give…" is appropriate.

**§19 matrix and §0:** statuses and conditional scopes are correct apart from the items below.

### Fixes required (form and scope)
1. **Missing hypothesis.** The §0 Result ("fair scalar-factor-conservative union") and the last-paragraph claim in §16 ("No method preserving scalar-factor closure…") need the hypothesis "with elementary PA inclusions (more generally, B_* ⊨ PA)". Without it the union need not be a PA subring.
2. **§16 fair test.** Add: "M_* ≻ M_0, so ¬IE₁⁻ is immediate; this illustrates the request logic only." Change "seed model" to "M_0". Also note that (G) is external (an infinite disjunction) and need not hold in M_*. The Farey failure is first-order and does transfer.
3. **§8 table is stale.** "Full bounded Farey brackets … not asserted" and "No proof of global proper binary reduction" should now say "FAIL (§17)".
4. **§19 mixes models.** The row "…even without optional queue" refers to a different tower. That contradicts both the "only this model" header and the falsifier check's "no models pooled". Rephrase it as "HOLDS; the queue is not needed (§12)".
5. **§18 wording.** In "conditional on standard ES … coinitial below every positive nonscalar", the conditional is in the wrong place. Bad primes below every nonscalar exist unconditionally; only "no least failure" depends on ES in ℕ.
6. **§0 Result.**
   - It runs to about ten sentences, but AGENTS.md asks for one.
   - "a nonempty set of ES failures has…" should read "the set of ES failures, if nonempty, has a prime (= divisibility-minimal) member".
7. **Label.** Add the elementary-chain/Tarski–Vaught theorem (§16). Add z79 §§1, 4, 9: freshness over the whole real closure, Farey implies short vector, and reduction as the IE₁⁻ theorems being refuted (§17).
8. **STATUS delta.** Tag the new "fails full Farey" clause "(cross-lab reviewed once, fde6146e4)". Keep z79's caveat "not excluding Bézout/(Sep)/Farey extractions" in some form: the z80 models fail Farey, so a Farey-based extraction is still untested.
9. **Small clarity fixes.**
   - The Scope phrase "§§3,6's windows" should become "z79 §3 windows as in §6".
   - In §17, rewrite "a common determinant bound is not an arithmetic basis" in plain terms: Q restricts [1,0,1] to a sublattice of scalar index S².

The master files don't quote IE1_SPLIT yet, so nothing needs correcting there now; the orchestrator's export still has to happen.
</code-review>
