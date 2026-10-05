# START HERE — campaign status

(For a human-readable overview of all results, see `CAMPAIGN_SUMMARY.md`.)
 (2026-10-01)

**Erdős–Straus (ES) is not solved, here or anywhere.** The literature has
been checked through 2026-09-28 (`LITERATURE_2026.md`). Every recent claimed
proof has an identifiable gap.

A novelty audit was run on 2026-10-04 (`reviews/novelty-audit-2026-10.md`).
* **Known in sharper form:** the exchangeable core of the sieve-limit
  theorem (Peled–Yadin–Yehudayoff 2011; Benjamini–Gurel-Gurevich–Peled).
* **Transport of a known bound:** `ck_min ≫ log p·log₃p` is
  Graham–Ringrose's bound carried over to `ck_min`.
* **Partial:** Theorem C, which generalises known odd-square obstructions.
* **Apparently new:** the 3/4 bound, the `W(p)` Ω-results, the weighted
  sieve-limit form and the ES caps.

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
    Astra update 2026-10-04: proofs that the norm-family fibres are blocked,
    thirty certified even-q escapes, and both fourth-norm extensions shown
    impossible at prime inputs for integer secants (`NORM_SEED_FOLLOWUP.md`,
    `EVEN_NORM_SEEDS.md`). There is still no unconditional sterile seed.
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
scale). Unconditionally (modulo Thorner–Zaman and Elsholtz–Tao Prop 1.4),
`W(p) ≥ exp(c(log p)^{1/5}(log log p)^{−1/5})` for infinitely many
Mordell-hard primes (`POINTWISE_OMEGA12.md` Thm 6.3, modulo Gallagher's
theorem and Elsholtz–Tao; chain: `POINTWISE_OMEGA8.md` 1/14 →
`POINTWISE_OMEGA9.md` 1/7 → `POINTWISE_OMEGA10.md` energy bound →
`POINTWISE_OMEGA11.md` 1/6 → 1/5; each step doubly reviewed; ledger (H)16,
(H)19, (H)21, (H)22, (H)24).
This supersedes the polylogarithmic results (`POINTWISE_OMEGA3.md`, every
fixed power of log p). So no pointwise multiplier mechanism whose witness
moduli are `≤ exp((log p)^{1/5−ε})` can prove ES. The heuristic truth is `log W ≍ (log p)^{1/3}`
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
* `verify.py` blocks (ci)–(co) (O20, ~11 s) add EXCEPTIONAL_TWIN3/TWIN4/KARY/KARY2/NONCRT and
  POINTWISE_OMEGA5/WINDOW checks (KARY B*/Thm 2.5 LPs need scipy; OMEGA3 is (cc)).
* `verify.py` blocks (cp)–(ct) (O35, ~10–20 s) add EXCEPTIONAL_TUPLES2 (forms, Cor 1.2,
  Thm 4.1 Euler-characteristic identity), EXCEPTIONAL_KARY3 (Lemmas 2.1–2.3 steps, §8 data),
  EXCEPTIONAL_LARGESIEVE2 §§1–7 (LP/Bessel parts need scipy; §§8–9 are (cy)),
  POINTWISE_OMEGA8 §§1–5 (BRW Lemma 3.1, c_W formula, exponent bookkeeping) and
  POINTWISE_TYPEI (Lemma 1.1, Thm 6.1, census spot check). Full run ≈ 4.3 min;
  use `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2` on the shared machine.
* `verify.py` blocks (cu)–(cy) (O43, ~25 s) add POINTWISE_OMEGA9 (Thm 1.1 character
  coefficients on a toy mod 2520, Lemma 2.1, Case A, exponent bookkeeping), POINTWISE_XWIN
  (half-set Lemma 1.1, a ≤ 127, x ≤ 2·10⁴), POINTWISE_WINDOW2 (Lemma 1.2 norm forms; Prop 3.7
  certificate re-solved at 60 digits), EXCEPTIONAL_INTERFREQ2 (Example 3.2, Lemma 3.1, rigidity
  LP, Lemma 9.3) and EXCEPTIONAL_LARGESIEVE2 §§8–9 (Gale Lemma 8.1, Prop 8.2(a) exact measure,
  Thm 9.1 chain; LPs need scipy). Full run ≈ 4.2 min (O43, 2 threads).

## Exceptional-set exponent: where it stands (2026-10-04)

**3/4 is now proved sharp for coefficient-sum congruence sieves over any
mixture of forced (and selector) classes, with no B-hypothesis and no
`(log log N)^{3/4}` loss (`EXCEPTIONAL_KARY3.md`, ledger (D)24; reviewed).** See
`EXCEPTIONAL_KARY2.md` Thm 5.1 / Cor 6.1, which builds on `EXCEPTIONAL_KARY.md`
Thm 4.5. The 3/4 note's own majorant is literally in the class, so the 3/4
note is sharp for its method.
* For every family of ℛ(M) forced classes with `M ≤ P(M)^{1+B}` (B fixed),
  every nonnegative CRT majorant saves at most `≪_B (log N)^{3/4}`. This
  includes twin and balanced moduli.
* Earlier steps: `EXCEPTIONAL_THETA.md` (dominant primes),
  `EXCEPTIONAL_TWIN*.md` (gapped moduli; Λ² sieves with r large primes, B
  removed for fixed r), `EXCEPTIONAL_NONCRT.md` (per-frequency signed
  rounding, prime-only majorants and CRT moment methods are also capped at
  3/4).
* So the 3/4 note's exponent cannot be improved within this architecture.

The large sieve is capped as well (`EXCEPTIONAL_LARGESIEVE.md`, via duality).

A θ>3/4 proof would need at least one of:
* cancellation between frequencies, which is now known to be worthless for
  classes of modulus ≤ N/2 (`EXCEPTIONAL_INTERFREQ.md`); what remains is
  multi-witness tuple counting above modulus N. `EXCEPTIONAL_TUPLES.md`:
  CRT-accurate witness correlations up to order `(log N)^θ` (TC_θ) would
  give exponent θ; bounded-order input cannot help;
* per-frequency weights below 1;
* non-CRT tuple counts or other genuinely arithmetic input;
* classes outside the ℛ(M) family with unbounded `log M/log P(M)` for
  general majorants (B-removal is sketched only).

Papers in `paper/`:
* `es-threequarter-note` (INTERNALLY PROVED, blind-audited);
* `vaughan-loglog-note`;
* `pointwise-obstruction` (refereed internally, ACCEPT pending authorship);
* `sieve-limits-note` v4: why 3/4 is sharp for congruence sieves, now with
  no log log loss, large sieves, tuple and hybrid doors (refereed
  internally; fixes applied);
* `es-omega-note` v3: every fixed exponent (refereed internally; P1–P4
  applied).
* `es-window-note` (new): the window statistic `a_min(p)` — half-set lemma,
  exact stacking orders for bounded windows (W1/W2 sharp), parity as a
  necessary input (refereed internally, R41 minor revision applied).
* `es-subexp-note` v2: `W(p) ≥ exp(c(log p)^{1/7})` i.o. via a
  Bazzi–Razborov sandwich minorant and a Gallagher-type linear transfer
  (refereed internally twice, R33/R33b minor revisions
  applied; novelty audit `reviews/novelty-audit-omega8.md`).

Authorship and the citation form for astra are still undecided.
