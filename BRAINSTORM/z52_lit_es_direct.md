# L1 — Erdős–Straus and Egyptian fractions directly

## §0 Summary
- **Assessment (2026-11-01):** ES remains open; no newly verified proof or disproof.
- **Genuinely new:** Cao–Xu, arXiv:2610.32302v1, presents 56 polynomial families; its purported cover is explicitly only tested to 10¹¹ and unproved by its authors.
- **Transferable features:** exact residue-class factorization classifies composites in 24m+1, but yields no unit-fraction witness; no new ES approach candidate.
- **Verdict change:** none. The 2026-10-21 literature update remains consistent; #242 is still open.
- **Structural test:** proposed polynomial cover lacks proof and does not clear FRONTIER B1/B2 or odd-square control T1.

## §1 Verified entries

### New arXiv item in the sweep

**Yichuan Cao and Xiaoping Xu, “Prime Numbers of the Form 24m+1 and Erdös-Straus Conjecture,” arXiv:2610.32302v1, submitted 2026-10-23 (13 pp.); accessed 2026-11-01.** The arXiv abstract and full HTML were accessed. The paper gives 56 polynomial families and says the numerical test suggests they imply ES; in §3 it explicitly states the covering claim “We have used AI to test the claim for m≤10¹¹ and it holds. But we failed to get a logic proof.” Thus this is a computationally tested conjectural covering, not an ES proof; the paper itself identifies the missing step. It additionally gives analogous numerical evidence for Howerton’s 14-wild-prime conjecture, §4, and a modulo-24 Goldbach conjecture, §5. Status: unrefereed v1 preprint; no proof claim supported. Source excerpt: `sources/z52/es_direct/2610.32302.txt`. Relation: prior Xu family work appears in `LITERATURE_2026_UPDATE.md`; searches for `2610.32302` returned no earlier entry.

### Tracked-record update check (primary arXiv records, accessed 2026-11-01)

The arXiv API entries checked included version and update timestamps. None of the listed works has a version after its latest listed submission (as of access date), except Ventas and Xu I, whose records list updates on 2026-10-15 and 2026-09-19 respectively; those updated abstracts were checked. Bradford 2602.11774 is v1 (2026-02-12), “A solution to the Straus-Erdős conjecture”; only its abstract-level claim of a solution was verified here, so not treated as a proof. Dyachenko 2511.07465 is v1 (2025-11-07), “Constructive Proofs … p≡1 mod 4”; 2511.17716 is v1, updated 2025-11-25, on the 5/P Sierpiński analogue. Ventas 2605.04551 v1, updated 2026-10-15, describes a probabilistic heuristic and Borel–Cantelli argument, not a theorem on ES counterexamples. Xu 2605.23601 v2 (updated 2026-09-19) concerns tame solution families; Xu 2609.29250 v1 concerns wild solution families. Ghermoul 2508.07367 v1’s title says “Almost a Complete Proof” for 5/a, not ES. Dahan 2608.24035 v1 studies a depth-dependent exceptional set and proves a fixed-J density bound (abstract); Jiang 2609.09204 v2 explicitly says it does not address ES itself, but solution counts. Pomerance–Weingartner 2511.16817 v2 (updated 2026-01-15) studies exceptions to the generalized ES–Schinzel conjecture; Mihnea–Dumitru 2509.00128 v1 reports verification to 10¹⁸ and solution-counting data. These are not new updates in this sweep. The API abstract is the source for the paraphrases above; full texts not re-opened for these older tracked items. Relation: `LITERATURE_2026.md`, `LITERATURE_2026_UPDATE.md`, `EXCEPTIONAL_SHORT.md`, `FRONTIER.md` (items found by `git grep -il` for author names); see §4 for limits.

## §2 Structural-feature table

| Problem | Structural feature that made it solvable | Does ES share it? | Transfer verdict |
|---|---|---|---|
| Composite test for n=24m+1 (Cao–Xu, §2) | Exact factorization of composite n into two factors in residue classes mod 24 converts compositeness into finitely many divisor-residue exclusions. | Partial: same residue reduction isolates primes p≡1 mod 24, but this only identifies candidate denominators; it does not produce an Egyptian-fraction witness. FRONTIER §3 B2 / §4 fixed-divisor issue remains. | None; elementary reduction, not a proof mechanism for ES. Related reduction already in `LITERATURE_2026.md`. |
| Proposed 56-family cover (Cao–Xu, §3) | Claimed cover of all m by explicit polynomial images, tested computationally only through 10¹¹; the authors say they failed to prove the cover. | No demonstrated share: the needed universal covering is precisely the missing theorem. It would have to handle the B1 finite-menu barrier and odd squares (T1); checking a finite range cannot bridge this. | None; unproved covering conjecture, no structural feature yet shown to solve it. |

## §3 New candidates

None. The only newly found ES-direct item offers a finite-family covering whose authors explicitly say they cannot prove it. It supplies no proved pointwise mechanism or non-obvious input that survives the B1/B2 tests. Promoting its computational claim to a candidate would merely restate the missing proof obligation.

## §4 Not accessed / could not verify / incorrect leads

- The arXiv API sweep (accessed 2026-11-01) searched the brief's keyword families across the general arXiv index and returned one clearly relevant post-2026-09-28 item, Cao–Xu 2610.32302. Other broad terms returned many irrelevant hits; a mathematically exhaustive search across every specified category/subfield cannot be guaranteed. The new item was opened as full HTML and its critical §3 paragraph verified.
- For older tracked claims, this pass checked arXiv API metadata and abstracts, not full PDFs. In particular, no page/line-level error audit was attempted for Bradford, Dyachenko, Xu, Ghermoul, Ventas, Dahan, Jiang, Akaka Zenodo 22754703, or Zenodo 23003413; see the existing, dated audits in `LITERATURE_2026.md` and `LITERATURE_2026_UPDATE.md`. Pomerance–Weingartner's newest arXiv version is v2 dated 2026-01-15; Mihnea–Dumitru is v1 dated 2025-08-29.
- The current erdosproblems.com #242 page was opened on 2026-11-01 and continues to label the problems open with the known partial results. Its rendered text drops formulas. The prior repo audit `LITERATURE_2026_UPDATE.md` (2026-10-21) reports the status of erdosproblems.ai/Plasma AI and the teorth successor repository. This pass did not independently inspect every forum thread, all 2025–26 solved Egyptian-fraction problems, or the current GitHub wiki history, so makes no claim that none exist.
- The DeepMind formal-conjectures repo, mathlib, sushaan-k/erdos-straus-lean, and local `/home/pasky/projects/math/oai-math` were not independently searched in this pass. Prior audits in `LITERATURE_2026_UPDATE.md` establish an exceptional-set Lean formalization and no ES item in OpenAI family 025 beyond the short Egyptian-fraction work; those are not fresh source checks here.
- Salez 1406.6307 and Mihnea–Dumitru computational algorithm details, hardest-prime certificates, and denominator-size statistics were not newly verified from their papers. The current repository literature cites the 10¹⁷ / 10¹⁸ verification bounds, but this lane does not infer a provable deterministic complexity bound from finite verification. No fresh computation was done.
- Not an ES result: Dyachenko 2511.17716 and Ghermoul 2508.07367 concern the 5/P analogue. The checked abstracts do not resolve that generalized conjecture. No new standalone proof of ES was verified; Bradford's abstract is a claim only, and Ventas describes heuristic probability modeling.
