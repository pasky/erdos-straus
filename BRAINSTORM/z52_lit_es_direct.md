# L1 — Erdős–Straus and Egyptian fractions directly

## §0 Summary
- Status: research in progress.
- Genuinely new since 2026-09-28: pending source sweep.
- Transferable structural features: pending verification.
- Campaign verdict changes: pending verification.

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

Pending review; distinguish genuinely new candidates from known-dead transfers.

## §4 Not accessed / could not verify / incorrect leads

