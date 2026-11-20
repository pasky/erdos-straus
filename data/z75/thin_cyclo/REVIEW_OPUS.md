# z75 CONJS_GEN and THIN_CYCLO — internal cross-model review

Reviewer: `anthropic/claude-opus-5-5` (`functions.review`, smart); authors: Astra. Range `90b455b57..3dd732a9d`. This is the lane's disposition/summary of the independent read-only review, not an external referee report.

**Verdict: ACCEPT-WITH-FIXES.** Opening assessment (verbatim): “I recommend accepting the 15·2^s+1 result and the three 4^s+k covers for headline promotion once the fixes below are made. The base-extension result (§2) is correct but trivial and should be a corollary, not a headline. No provider or quota issues came up.”

Reviewer's checks: (1) all three period bitsets replayed; (2) `z75_conjs_check` and `report` byte-identical to stored results, prime windows confirmed and registration commit checked; (3) independently compiled a copy of the Lean file against matching environment, `[propext, Classical.choice, Quot.sound]`, same SHA as build log; (4) independent actual-integer triple replay of every non-M type at each row's first exponent ≥32, later representatives of periods ≤6000, every s from 32 through 2599/1199/799 for k=297/273/33 and 300 random exponents per k up to 60000. Independently checked the five-slice equivalence on all 512 cells. No failure. Confirmed square obstruction/periodicity, including 19|n for s=3 mod 9 in the 297 family, and applicability of all off-core row moduli for b≡2 mod L. Only M rows depend on Mordell. Accepted mod-840 word and least-good-denominator corollary. Confirmed 196/208 explained mixed hits and descriptive, not inferential, norm null.

Required changes and disposition:
* Synchronized both notes' review and Lean status, combined §1C proposed delta, relabelled (S) dependence on Z64's certified component and superseded the old next push.
* Verifier tightened (positive f, explicit n≡1 mod 4 hypothesis, unused UV kind removed); original exact certificates unchanged. Optional additional triple output not needed, given separate reviewer checks.
* Saved every intermediate consumed by the packer, documented regeneration of packed certificates and the purpose of the Proth15 exploratory logs.
* Labeled the d=1 gap window degenerate, demoted base extension to a corollary, corrected square-unit citation to EXPONENT_COVERING Thm 1.2. Only Proth15 is Lean-checked. No external-priority/firstness claim.
* **For conductor's export:** update STATUS and FRONTIER, and add scoped supersession notice to Z64_SDEEPF §3 Remark(ii) (four classes are now fully covered; Remark(i)'s no-cover statement for its specific search remains true). No masters edited by lane.
