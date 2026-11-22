<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="b9f4b3a9e">
A separate reviewer subagent was asked to review the changes in `git log b9f4b3a9e..`. Its request and review follow.

Request: review changes since b9f4b3a9e carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Focused hostile follow-up review: verify the post-R1 changes to notes/z81/S_U7_FORCE.md, especially the exact C|60 sharpness construction via D=-128,-256 and its quadratic twists, split-prime refinement, and generator signs (K2 second 85329). No need to replay the 110 blocks or anything already verified by R1. Keep computational checks under 2 minutes. Explicit lane write allowlist forbids editing master files or Z68_U7F.md; check that the corrections are ready for the orchestrator. Flag any still-unresolved mathematical issue.

Commit log:
commit e385b5b68e0bbd1462c5de8bd2cc20bc94d1476c
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:19:57 2026 +0100

    z81: apply Opus review, sharpen class-field detector on split primes and attain its bound

 data/z81/xreview/REVIEW_S_U7_R1_OPUS.md | 69 +++++++++++++++++++++++++++++++++
 notes/z81/S_U7_FORCE.md                 | 30 ++++++++------
 2 files changed, 87 insertions(+), 12 deletions(-)

Review:
**Verdict: ACCEPT, with minor fixes.** I found no mathematical error in what changed after R1 (`e385b5b68`). Four export and labelling fixes are needed before the orchestrator applies the corrections. My checks ran in about 30 s using cypari2 and sympy.

## What I verified

**The C|60 sharpness construction is correct.**
- **Class groups.** `quadclassunit(-256)` and `quadclassunit(-128)` both return cyclic groups of order 4. The form lists in the note are reduced, primitive and complete.
- **The two fields are different.** I built each ring class field as the compositum of its base field with `polclass(D)`:
  - D = −256 gives a field containing a root of x⁴−2, so it is ℚ(i,⁴√2).
  - D = −128 gives a field containing a root of x⁴−2x²+2, so it is ℚ(i,√(1±i)).
  - `nfisisom` returns 0, so they are not isomorphic. Both are degree-8 non-abelian fields ramified only at 2, and both contain ζ₈.
  - Their compositum has degree 16 and contains ζ₁₆, which is the claim.
- **The group theory holds.** η² cuts out ℚ(√2), the third quadratic subfield of ℚ(i,√2). Mixed cosets have odd rotation because ℚ(√2) lies in each genus field. (ℤ/16)^× = ⟨−1⟩×⟨3⟩, and ρ² = (2/·), since its kernel is ±1 mod 8. η/ρ is quadratic and ramified only at 2, so it lies in ℚ(i,√2). Together these give ℚ(ζ₁₆). Adding ℚ(√−3) and the ℚ(ζ₅) from the p=341041 construction gives ℚ(ζ₂₄₀). Its exponent is λ(240)=4, consistent with Theorem B.
- **One small gap.** The note never says the two fields differ, and the fibre-product argument needs that. It is automatic: D₄ has a unique cyclic subgroup of order 4, so a D₄ field has only one possible base, and the bases ℚ(i) and ℚ(√−2) differ. Add one clause saying so.

**The split-prime refinement is correct.**
- Since K∩E=ℚ, the prescription "identity on K, −1 on E" is realisable. Varying the result by Gal(EL/L) keeps the restriction to L, and therefore keeps K split, while changing the target bit.
- K=ℚ(√−Cp) with p∤4C is ramified at p, so it is not contained in E.
- For a prime q dividing 4Cp+1, −Cp ≡ (1/2)² mod q, so q splits in K.
- The scope sentence ("Chebotarev does not prescribe divisibility") is right.

**The generator signs are correct.**
- The represented integers are right: Qfb(11,11,426304) has discriminant −18757255, and Qfb(275,275,85329) has discriminant −93786275 and is primitive.
- (χ₅,χ₋₁₁) takes the values 2:(−,−), 426304:(+,−), 3:(−,+), 85329:(+,−), as stated. Both matrices are nonsingular over F₂.
- The 2-ranks are 2 ([1476,2] and [1388,2]), so these two characters generate the genus characters.
- 151 and 239 both give (+,−), so their genus labels are equal.
- The values match the `chi 5` columns in `class.txt`.

**The other edits are correct.** 5T−1=(p+5)/34. The heuristic paragraph matches `Z68_U7F.md` §9.1 (the count of three was flat from 10⁷ to 10⁹, and the fitted exponent is ≈1.08). Removing "requested monster primes" and the opaque numerator-8 sentence is right.

## Issues to fix (form, export readiness)

1. **The Review line overstates coverage.** R1 reviewed `b9f4b3a9e`. The split-prime refinement, the C|60 sharpness paragraph and the generator-sign replacement were all added afterwards. Add something like "post-R1 additions: R2 (this review)".
2. **The STATUS delta is ambiguous and incomplete.**
   - "(two new prime exceptions, §4)" reads as note §4, which is the class-field section. Write "STATUS §4" or name the primes.
   - The delta should keep the rest of item 3: the `Z70_CLASS.md` open list (Rédei 4-rank, split-prime orbits, solution-graph moves).
3. **The erratum pointers are incomplete.**
   - The FRONTIER caveat "sample-certified only; no (★)-internal configuration was constructed" appears at **lines 837, 1039 and 2672**. The erratum says only "the Z60_RAYCLASS/Screen 9 caveat"; give all three lines.
   - An erratum at the start of `Z68_U7F.md` §9.1 (line 324) sits *after* the §6 summaries at lines 292 and 314. A reader of §6 would not see it. Put a second marked erratum at line 292, or put one at the top of the file.
4. **A census consequence is missing.** The sieve's `ok()` only marks f = c·q with q prime and c∈{1,3,5}, so every marked prime has a three-cofactor witness with ω(f)≤2. The two exceptions were audited directly. So Conjecture B, the six-cofactor clause and U₇ (no prime U₇-zero) all hold, CERTIFIED with one engine, for every prime p≡1 (8) in (10⁹, 1.11·10¹¹]. That extends the listed ≤10⁹ census, and the FRONTIER EVIDENCE claim up to 4·10⁹, by about 28×. AGENTS §3 lets a census extension reach STATUS §1F, so the note should state it and propose the delta.

## Still-unresolved mathematics
There is no error. Two scope points remain:
- The quartic configuration is "(★)-internal" only *up to quadratic twist*: it uses auxiliary quadratic fields unramified outside {2,5,11,p}, which are not (★) data. The proposed FRONTIER wording says this correctly; keep that qualifier.
- Calling §4 BARRIER-SCOPED rather than BARRIER-BROAD is defensible, but it is a judgement call.

None of the three corrections (master files, `Z68_U7F.md`, FRONTIER) has been applied yet, which is expected given the lane's write allowlist. Once fixes 2 and 3 are in, they are ready for the orchestrator.
</code-review>
