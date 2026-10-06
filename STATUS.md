# START HERE — campaign status

(For a human-readable overview of all results, see `CAMPAIGN_SUMMARY.md`.)
 (2026-10-06; ledger through (D)28 and (H)33)

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

A second audit (2026-10-05, `reviews/novelty-audit-2026-10b.md`, no internet) covers the
OMEGA9–17 / WINDOW / KARY3 round.
* **Standard:** the β-weighted LLL; the large-sieve/Λ² duality.
* **Known method, new statement:** the Gallagher transfer; the Janson-type inequality
  (closest suspected prior art Lu–Székely); the typical-size bound (Vaughan's method).
* **Heuristically anticipated:** the Haar exponent 3 (Elsholtz–Tao Remark 1.2).
* **Apparently new:** the energy bound and the constant-1 DNF tail (hedged); the planting
  lemma, which sharpens Benjamini–Gurel-Gurevich–Peled Thm 27; the W(p) Ω-rates, the 1/4
  ceiling and LS ⇒ 1/3; the window stacking exponent.

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
* **Open target.** θ > 3/4. 3/4 is proved sharp for every CRT architecture
  analysed except residue-dense all-level large sieves, hybrids and tuple
  counts of growing order, which are reduced to open statements (see
  "Exceptional-set exponent: where it stands" below). The cubic witness tail (ledger (A)9) is now INTERNALLY PROVED via the 3/4 note.

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
scale). **Pointwise state (ledger (H)16–(H)33):**
* *Rate.* `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` for infinitely many
  Mordell-hard primes (`POINTWISE_OMEGA13.md` Thm 5.1, PROVED modulo
  Gallagher's theorem, Nair–Tenenbaum and the campaign's energy bound; chain
  OMEGA8 1/14 → OMEGA9 1/7 → OMEGA10 energy bound → OMEGA11 1/6 → OMEGA12
  1/5 → 1/4, each step doubly reviewed). It supersedes the polylogarithmic
  results, so no pointwise multiplier mechanism whose witness moduli are
  `≤ exp((log p)^{1/4−ε})` can prove ES.
* *Exponent 3, twice.* The profinite (Haar) avoider exponent is 3:
  `𝓛³ ≪ log(1/δ*(T)) ≪ 𝓛³(log 𝓛)^5` (`CEILINGS_UNIFIED.md` Prop 1.1, given the
  3/4 note; `POINTWISE_OMEGA13.md` Thm 3.4). The tail exponent of W over
  primes is also 3: `c(log T)³ ≤ log(π(x)/#{p≤x: W(p)>T}) ≤ C(log T)³(log log T)³`
  for `log T ≤ c(log x/log log x)^{1/4}` (upper: ledger (A)9, INTERNALLY
  PROVED; lower: `POINTWISE_TAIL.md`, PROVED modulo (G), NT, OMEGA10).
* *Ceiling 1/4.* 1/4 is the ceiling of the Haar-minorant + transfer
  architecture, up to `(log log p)^{1/4}` (`POINTWISE_OMEGA14.md`, sharpened
  by `CEILINGS_UNIFIED.md` Prop 4.2); by the Wiener-norm barrier
  (`POINTWISE_OMEGA15.md`) also of every full-orbit uniform linear
  certificate, where GRH/EH-type prime input is irrelevant. The 3/4 cap and
  the 1/4 ceiling are one order-k sieve limit (`CEILINGS_UNIFIED.md`).
* *1/3.* The heuristic truth is `log W ≍ (log p)^{1/3}`. The CONJECTURE LS
  ("Linnik for sifted sets") implies it (`POINTWISE_OMEGA16.md`, PROVED
  implication); EH/GEH/BV and truncated GRH do not, through linear
  certificates. Support-aware certificates are open, reduced to Conjecture
  SAP (`POINTWISE_OMEGA17.md`).
* *m/n.* Exponent 1/4 for m ≡ 0 (4), 1/5 for every m (incl. 5/n);
  1/4 for m ≢ 0 (4) is CONDITIONAL on ADM_m ⇐ SI (`POINTWISE_MN.md`, `MN2`).

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
* `verify.py` blocks (cz)–(df) (O54, ~22 s; full run ≈ 4.8 min, 2 threads) add POINTWISE_OMEGA10 (Lemma 3.2, Thm 3.4 QM, C-1 /
  Lemma 3.1 on biased product spaces, Cor 4.1; exact), POINTWISE_OMEGA11 (Lemma 1.1 digit
  filtration, graded-quarantine toy, Lemma 2.2 at T = 3000), POINTWISE_OMEGA12 (Lemma 2.1 on all
  atoms T = 10⁴, Lemmas 1.1/2.2/3.1 steps, §7 regression), POINTWISE_HAAR (Lemmas 1.1–1.3,
  Thm 1.4 by exact enumeration), POINTWISE_OMEGA13 (Lemma 3.1 Jacobi, M ≤ 3·10⁴; β-weighted LLL
  Lemma 1.1), POINTWISE_TRANSFER (Lemmas 5.0, 5.1, identity (5.1)) and EXCEPTIONAL_SPW (embedded
  exact certificate σ ≤ 72/185 at N = 300, e = 630; LP re-derivation needs scipy).
* `verify.py` blocks (dg)–(dm) (O66, ~33 s; full run ≈ 4.4 min, 2 threads) add POINTWISE_OMEGA14
  (planting Lemma 1.1 exact, k ≤ 3; toy LP thresholds), POINTWISE_OMEGA15 (Lemma 1.1 closed form and
  `(4r*)^{k+1}` bound on toy planted systems; Lemma 2.3 with actual primes), POINTWISE_OMEGA16 §6
  (W(133050918961) = 5935; least-p table T ≤ 2047 exhaustive; Buchstab ratios at 10⁷, 10⁸),
  EXCEPTIONAL_LARGESIEVE3 (Thm 1.1 toys, Thm 3.1, Lemma 4.1, Lemma 4.2), EXCEPTIONAL_SPW2 (Lemmas
  2.2, 2.3 sharp; RSPW LP rows), CEILINGS_UNIFIED §4.4 (exact toy LP thresholds) and POINTWISE_WINDOW3
  (certified one-window LP 0.4893; 50-digit verified K = 2.5 fake; needs scipy + mpmath).
* `verify.py` blocks (dn)–(ds) (O75, ~33 s; full run ≈ 4.9 min, 2 threads) add EXCEPTIONAL_LARGESIEVE4
  (Lemma 1.1 identity + damped-collision inequality toys; Lemmas 2.1, 3.2, 5.1, Prop 4.1 toys; Cor 5.3
  residue counts), EXCEPTIONAL_LARGESIEVE5 (Lemma 1.2 label heights/compatibility, G ≤ 600),
  EXCEPTIONAL_LARGESIEVE6 (Prop 4.2 and Thm 5.1 on exact R71 toys; author MC toy), POINTWISE_OMEGA17
  (Lemma 5.2 exact), POINTWISE_TYPEI2 (sign-point checkers to ck ≤ 10⁶, author + R69, needs gcc/cc;
  Lemma 3.1 square families; Prop 4.1(i) r ≡ 3 (8) identity) and POINTWISE_MN (Lemma 1.1 Jacobi
  symbols for several m; §1 square-consistency counts).

## Exceptional-set exponent: where it stands (2026-10-06)

**3/4 is proved sharp for the CRT architectures below; the remaining cases
are reduced to precisely stated open statements** (ledger (D)9–(D)28; all
internal, reviewed, unrefereed). The 3/4 note's own majorant
is in the class, so the note is sharp for its method.
* *Coefficient-sum sieves:* over any mixture of forced (ℛ(M), (a,D),
  Case-A) and selector classes, arbitrary moduli, no B, no `log log` loss:
  saving `≤ C_A(log N)^{3/4}` (`EXCEPTIONAL_KARY3.md`, (D)24, building on
  KARY2/KARY). Also prime-only majorants ((D)22), interval cancellation at
  moduli `≤ N/2` ((D)20), Bessel-type large sieves of polynomial period
  ((D)19, (D)25).
* *All-level large sieves* (any frequency, any level): capped at 3/4 for
  mixtures with one prime factor above `exp((log N)^{1/4})` per modulus
  (`EXCEPTIONAL_LARGESIEVE3.md`, (D)27) and for residue-sparse multi-rough
  classes, incl. all small-height classes such as −4 mod M
  (`EXCEPTIONAL_LARGESIEVE4.md`, (D)28).
* *One sieve limit:* the 3/4 cap and the pointwise 1/4 ceiling are the same
  order-k limit at critical level `≍ 𝓛⁴` (`CEILINGS_UNIFIED.md`, (H)29).

**Open (each precisely stated):**
* (A*) for residue-dense multi-rough classes (generic ℛ(M)), reduced to a
  damped covering count (DCC) and then to residue dispersion (RD′)
  (LS5–LS7; (RD) PROVED at one prime for ℛ(M) and for long cofactors, false
  as first stated for several primes; short cofactors and (a,D)/Case-A
  classes open);
* hybrid interval methods: reduced to **weak SPW** (`EXCEPTIONAL_SPW2.md`:
  exact requirement `log(K/η) = O((log N)^{3/4})`; fixed-σ SPW and fixed-η
  RSPW refuted); right-signed mass at moduli in `(N, CN]`;
* tuple counts of growing order: TC^alt_θ for θ > 3/4 (CONJECTURE,
  `EXCEPTIONAL_TUPLES2.md`); per-frequency weights below 1; genuinely
  non-CRT input.
The first two are *closing* questions (they would extend the cap); a θ > 3/4
proof needs the third kind of input.

Papers in `paper/`:
* `es-threequarter-note` (INTERNALLY PROVED, blind-audited);
* `vaughan-loglog-note`;
* `pointwise-obstruction` (refereed internally, ACCEPT pending authorship);
* `sieve-limits-note` v5: why 3/4 is sharp for congruence sieves, now with
  no log log loss, all-level large sieves (residue-sparse), tuple and hybrid
  doors, and the unified sieve-limit picture (refereed internally, R36/R65;
  fixes applied);
* `es-omega-note` v3: every fixed exponent (refereed internally; P1–P4
  applied).
* `es-window-note` (new): the window statistic `a_min(p)` — half-set lemma,
  exact stacking orders for bounded windows (W1/W2 sharp), parity as a
  necessary input (refereed internally, R41 minor revision applied).
* `energy-dnf-note` (new, 17 pp): the energy bound C-1 on product spaces and
  sharp-rate DNF Fourier tails `W^{>t} ≤ 4·2^{−(t+1)/k}` (refereed internally,
  R50 minor revision applied; novelty hedged).
* `es-subexp-note` v5: `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o.,
  typical size `#{p≤x: W(p)>T} ≪ π(x)e^{−c(log T)³}`, the Haar avoider
  exponent is 3, 1/4 is the ceiling of the Haar-minorant + transfer
  architecture (and of full-orbit uniform linear certificates), and the
  conjecture LS ("Linnik for sifted sets") gives 1/3 (refereed internally
  five times: R33, R33b, R47, R56, R64; novelty audit
  `reviews/novelty-audit-omega8.md`). A v6 adding the two-sided tail
  (`POINTWISE_TAIL.md`) is in preparation (task O77; not yet merged).

Authorship and the citation form for astra are still undecided.
