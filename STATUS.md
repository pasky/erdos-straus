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
    Astra update (2026-10-02, read-only check): all 159 primary anchors
    are reachable from the seed with no primality assumption at all
    (`PRIMARY_REACHABILITY.md`). One primary prime has been replaced by an
    exact divisor (leaf) condition, leaving 158 prime conditions plus that
    leaf condition (`PRIMARY_LEAF_RELAXATION.md`). Searches over actual
    inputs still find no sterile prime.
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

This is now a theorem about procedures (`POINTWISE_SIZE.md`, Theorems M
and C, reviewed). Caution: eventual-sign *size comparisons* of formal
quantities (against `p^θ`, `log p`, short intervals) are still inside the
obstruction (Proposition A). A pointwise proof must use (E1) a search whose
length grows with p, or (E2) non-polynomial primitives such as `⌊p^θ⌋` or
the least non-residue, and then control actual factorisations. The natural
E1 target is the window statement `a_min(p)≪log p` (conjecture X_win;
heuristically `a_min≍log p/log log p`, just above the formal-obstruction
scale). Unconditionally, for every fixed k, `W(p)≥(log p)^k` infinitely often
(`POINTWISE_OMEGA3.md` Thm 5.2, modulo Thorner–Zaman; two hostile
reviews). So no pointwise multiplier mechanism with polylogarithmic
witness moduli can prove ES. The heuristic truth is `log W ≍ (log p)^{1/3}`
(POINTWISE_SIZE §7).

## Housekeeping

* Agents must work only in their own worktree. Two agents committed
  directly to the parent branch; nothing was lost.
* Large data stays compressed under `data/`. Survey scratch files in
  `/tmp` are regenerable by the scripts named in each document's Replay
  section.
* Status labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE.
  "Verified numerically" never means "proved".
* `verify.py` blocks (bz)–(ch) replay the key machine checks of
  POINTWISE_SIZE/OMEGA/OMEGA2/OMEGA3, EXCEPTIONAL_THETA/BALANCED/TWIN/TWIN2
  and the 3/4 blind audit (~25 s; the THETA LP runs only with
  `uv run --with scipy python verify.py`).

## Exceptional-set exponent: where it stands (2026-10-02)

`EXCEPTIONAL_THETA.md` (reviewed, merged) proves that **3/4 is sharp** for
every nonnegative CRT-majorant sieve built from forced classes whose moduli
have a dominant prime. This class contains the 3/4 note's own majorant
(DISCOVERIES (D)9). The note's mass heuristic θ=B/(B+1) is now a theorem
for that class. No θ>3/4 was found. Beating 3/4 requires at least one of:
* balanced moduli used jointly (they carry a positive share of the cubic
  supply; open; reduced to H_MS^{Sel} for Λ² sieves). `EXCEPTIONAL_BALANCED.md`
  (reviewed) reduces the *gapped* balanced moduli, for each fixed B, to one
  arithmetic extremal statement (E_δ). `EXCEPTIONAL_TWIN.md` (reviewed) then
  proves the gapped case unconditionally, with no need for (E_δ). The η-twin
  moduli (top two primes at comparable scale) are the open core. They reduce
  to an arithmetic-free comparison inequality (Conj 6.4), and for Λ² sieves
  to a sparse noise-stability statement (Conj 6.8). For Λ² sieves with at
  most two large primes per modulus, the cap is now proved, twins included
  (`EXCEPTIONAL_TWIN3.md`);
* multipliers beyond N^{O(1)};
* signed cancellation in rounding errors;
* a non-CRT input (actual arithmetic of `(p+a)/4`).

Papers in `paper/`:
* `es-threequarter-note` (INTERNALLY PROVED, blind-audited);
* `vaughan-loglog-note`;
* `pointwise-obstruction` (refereed internally, ACCEPT pending authorship);
* `es-omega-note` v3: every fixed exponent (refereed internally; P1–P4
  applied).

Authorship and the citation form for astra are still undecided.
