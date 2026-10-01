# START HERE — campaign status (2026-10-01)

**Erdős–Straus (ES) is not solved, here or anywhere.** The literature has
been checked through 2026-09-28 (`LITERATURE_2026.md`). Every recent claimed
proof has an identifiable gap.

Branch: `main`. Old branch names such as `wave33-sec77` were wave labels
and have been merged. `DISCOVERIES.md` is the curated ledger of every claim
with its status label. Read it before starting new work.

## Two research lines

### 1. Exceptional-set line (analytic; the original project)

* **Documents.** `PROJECT.md`, `notes.md` (§§1–77), `verify.py`, and
  `paper/`.
* **Best proved bound.** Vaughan-type
  `E(N) ≪ N exp(-c(log N)^{2/3}(log log N)^{1/3})`
  (`paper/vaughan-loglog-note.tex`), plus the 3/4 note
  `E(N) ≪ N exp(-c(log N)^{3/4})` (`paper/es-threequarter-note.tex`),
  INTERNALLY PROVED: three internal reviews, the last a blind from-scratch
  audit (`reviews/es-threequarter-blind-audit.md`, SOUND). It has not been
  externally refereed.
* **Open target.** θ > 3/4 (the 3/4 note's mass-driven heuristic ceiling
  is θ=B/(B+1) with B=3). See `PROJECT.md`, Outcome 36, and the agent
  workstream `EXCEPTIONAL_THETA.md` (in progress).

### 2. Pointwise signed-graph line (wave 33–34): CLOSED

* **The idea.** Signed solutions of `4/p=1/x+1/y+1/z` form a finite graph,
  with edges between triples that share a denominator. The *seed-component
  conjecture* asserted that the component of `(t,-2pt,-2pt)` always
  contains a positive vertex. That would imply ES for `p≡1 (4)`.
* **The verdict.** The conjecture is **false under standard prime
  hypotheses**, so this line cannot prove ES:
  * `FORMAL_CLOSURE.md` (this repo), Theorem F. Under Schinzel's
    Hypothesis H for 6402 explicit polynomials of degree at most 2, the
    whole seed component is sterile for infinitely many `p=24q+1`. The
    result is certified, and an independent engine reproduced it
    (`reviews/formal-closure-review.md`).
  * The sibling project `../erdos-straus-astra`
    (`SIGNED_SEED_COUNTEREXAMPLE.md` and `PRIMARY_SEED_PACKET.md`) reached
    the same conclusion independently. It is **stronger**: it needs
    Dickson's conjecture for only **159 linear forms**, and it exhibits a
    positive ES solution outside the sterile component (on a subprogression;
    that conclusion needs Dickson for the restricted tuple, PAPER_B_ISSUES 11).
    Cite that version first. Write-up: `paper/pointwise-obstruction.tex`
    (29 pp; internal hostile referee `reviews/pointwise-obstruction-paper-review.md`,
    round 2 ACCEPT pending the authorship/[AS] citation decision).
* **Supporting results.**
  * `DEPTH3.md`: exact classification of escapes of length ≤3. Every
    prime `p<10^12` escapes within distance ≤3. Under H the distance is
    unbounded (Theorem 2). Sieve bounds.
  * `SIZE_CONJECTURE.md`: certified sterile components larger than the
    seed component; Lemmas A–E.
  * `WINDMILL.md`: parity and windmill obstructions. Theorem 7: large
    p-free buckets are singletons.
  * `SIGNED_REFACTOR.md`, `POINTWISE.md`: the base results. The signed
    character theorem (2a) is Bright–Loughran 2020, not new.
* **Reviews.** `reviews/wave34-hostile-review.md` and
  `reviews/formal-closure-review.md`. All repairs are applied.

## What a future attempt must respect

The common mechanism behind Theorem F, DEPTH3 Theorem 2 and the
Elsholtz–Tao "odd-square" remark is this: **any argument that uses only
congruence data and the *shape* of factorisations fails for formally
generic primes.**

A pointwise proof of ES must therefore control actual factorisations of
specific shifted integers, for example by using the size of p. Otherwise
the work should return to the exceptional-set line.

## Housekeeping

* Agents must work only in their own worktree. Two agents committed
  directly to the parent branch; nothing was lost.
* Large data stays compressed under `data/`. Survey scratch files in
  `/tmp` are regenerable by the scripts named in each document's Replay
  section.
* Status labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE.
  "Verified numerically" never means "proved".
