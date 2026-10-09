# START HERE — campaign status

(For a human-readable overview of all results, see `CAMPAIGN_SUMMARY.md`.)
 (2026-10-10, refresh 8; ledger through (D)32a, (D)31 follow-up 3 [EXCEPTIONAL_MN4], (H)17 follow-up 6 [TYPEI7] and (H)34 follow-up 3 [MORDELL13E]. Refresh 7 (2026-10-09): ledger through (D)32 and (H)34, incl. the follow-ups (D)31 [EXCEPTIONAL_MN2: density transition for m/p; follow-up 2 EXCEPTIONAL_MN3: the m/φ(m) loss removed, Thm L′], (D)32 [EXCEPTIONAL_TYPEI_LOGLOG: ET's Type I log log N removed under Selberg's eigenvalue conjecture], (H)17 follow-ups 4–5 [TYPEI5, TYPEI6], (H)34 follow-ups [MORDELL13B, MORDELL13C, MORDELL13D, MORDELL17B, MORDELL17C] and the refutation (F)11 [MORDELL13B: the r = 13 candidate x* is not sterile; x** is the new candidate])

**Erdős–Straus (ES) is not solved, here or anywhere.** The literature has
been checked through 2026-09-28 (`LITERATURE_2026.md`). Every recent claimed
proof has an identifiable gap.

**Headline results of the current phase (2026-10-06 – 10-10; all internal, hostile-reviewed, not externally
refereed; none of them solves ES or any case of it):**
* *m/n uniformly in m* ((D)31, `EXCEPTIONAL_MN.md`; PROVED relative to the 3/4 note):
  `E_m(I) ≪ H exp(−c(log H)^{3/4} m^{−1/4})` for every m ≥ 4 and every interval of length H.
* *Density transition for m/p* ((D)31 follow-ups 1–3). Upper side Thm U (PROVED relative to (D)31, BV,
  Shiu; ineffective): most primes are m-representable once log N ≥ A_ε m^{1/3}. Lower side Thm L′ (PROVED
  relative to ET Thm 7.1, BT, Shiu, PV): `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}`, gap `(log log N)^{1/3}`.
  **Sharp order** `log N ≍ m^{1/3}` (MN4 Thm 5.2): CONDITIONAL on SEL_m for the lower half (for m ≤ L⁵);
  the upper half is Thm U. No sharp threshold constant is claimed (Conj C2 is open).
* *Elsholtz–Tao's Type I sum* ((D)32/(D)32a). Unconditionally, relative to Deshouillers–Iwaniec 1982 Thm 7
  and Drappeau 2017 Lemma 4.10: `Σ_{p≤N} f_I(p) = o(N log² N log log N)` (TYPEI_LOGLOG2 Thm 4.1(i), PROVED rel.
  those inputs; no quantified rate). `≪ N log² N` is CONDITIONAL on Selberg's eigenvalue conjecture (TYPEI_LOGLOG
  Thm 8.1) or on (EFF), an effectivity statement for the ε-constants of DI/Drappeau (Thm 4.1(ii); that (EFF)
  holds is an Assessment).
* *x\* refuted* ((F)11, MORDELL13B): the r = 13 candidate sterile point x* lies in an ET class (modulus
  12670944). The new candidate x** survives through ES level 2.59·10¹⁰ (MORDELL13E, CERTIFIED); sterility
  is a CONJECTURE. For Type I, TYPEI7 proves that 2-adic closeness tests cannot show `x̂_9` sterile.
* *Papers:* `es-mn-short-note` (m/n, density transition; Thm L′ section not yet re-refereed) and
  `es-typei-heegner-note` (the conditional Type I bound). The unconditional (D)32a, MN4, TYPEI7 and
  MORDELL13E are **not yet in any paper**.

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
* **Short intervals and progressions** (`EXCEPTIONAL_SHORT.md`, ledger (D)30;
  PROVED relative to the 3/4 note). For every interval I of length H ≥ 2, at
  any position, `E(I) ≪ H exp(−c(log H)^{3/4})`; the same in progressions
  n ≡ b (mod q) for `q ≤ exp(c'(log(H/q))^{3/4})` and for q with all prime
  factors > X; for primes in (x, x+H] once `H ≥ exp(C(log log x)^{4/3})`.
  The reason: the note's majorant is shift-uniform. Novelty is modest; large
  smooth q are open, and below `H = e^{c(log x)^{3/4}}` such a bound would
  imply ES for all large n (Prop 4.1).
* **m/n, uniformly in m** (`EXCEPTIONAL_MN.md`, ledger (D)31; PROVED relative to
  the 3/4 note; two hostile reviews, no FATAL/MAJOR). For every m ≥ 4 and every
  interval of length H ≥ 2, `E_m(I) ≤ C H exp(−c(log H)^{3/4} m^{−1/4})` with absolute
  c, C. This is non-trivial up to m ≤ ε(log N)³ and asymptotically improves
  Pomerance–Weingartner's explicit-in-m Vaughan bound. Progression/prime versions
  are included. The density transition lies at `log n = m^{1/3+o(1)}` (Cor D with PW
  Thm 3.1). Novelty is an Assessment: new for m ≠ 4, by the note's method.
  Follow-up `EXCEPTIONAL_MN2.md` (two reviews, no FATAL/MAJOR), with `A = log N/m^{1/3}`:
  Thm U (PROVED relative to (D)31 Cor 3.2, Bombieri–Vinogradov and Shiu; ineffective): for every
  ε there is A_ε such that at most a proportion ε of the primes in (N/2, N] are m-exceptional once
  A ≥ A_ε, uniformly in m ≥ 4 (removes Cor D's `(log m)^{4/3}`). Thm L (PROVED relative to ET Thm 7.1
  and the structure of ET's proof of Prop 1.4, plus BT and Shiu):
  `ρ_rep ≪ L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}`. EVIDENCE: `L_{1/2} = (1.95 ± 0.05) m^{1/3}`
  for even m ∈ [60, 300]. Conj C2 (CONJECTURE): `ρ_rep = F(A) + o(1)` with F non-degenerate (no sharp
  threshold constant).
  Follow-up 2 `EXCEPTIONAL_MN3.md` (review R108: no FATAL/MAJOR, minors applied by the reviewer):
  Prop 2.3 (PROVED relative to ET Thm 7.1, Brun–Titchmarsh, Shiu and Pólya–Vinogradov; effective) is ET Prop 1.4 with the
  coprimality gain φ(k)/k, and gives **Thm L′** (PROVED relative to ET Thm 7.1, BT, Shiu, PV and MN2
  Prop 3.2): `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}`. The m/φ(m) loss is gone; the remaining
  gap to Thm U is `(log log N)^{1/3}` in the threshold, exactly ET's Type I Brun–Titchmarsh log log N
  (not removed). Its obstruction is located: a bad region of area 1/6 where all progression moduli are
  ≥ N^{1−η} (Prop 3.3, PROVED geometry); method-exclusion claims are Assessment; Thm 3.8 (PROVED
  implication): a level-of-distribution hypothesis LD implies ET's conjectured `Σ_{p≤N} f_I(p) ≪ N log² N`.
* **ET's Type I log log N under Selberg** (`EXCEPTIONAL_TYPEI_LOGLOG.md`, ledger (D)32; hostile review
  R111 rounds 1–2, repairs O112, round 2: complete CONDITIONAL proof). Thm 8.1 (CONDITIONAL on Selberg's
  eigenvalue conjecture for Γ₀(4dq²) with even nebentypus, uniformly in the level):
  `Σ_{p≤N} f_I(p) ≪ N log² N`, removing the log log N in Elsholtz–Tao Thm 1.1. Ingredients: the SL₂ form
  `ef − 4a²d = 1`, uniform separation of the level-d Heegner roots (Lemma 2.2, PROVED, sharp constant
  3/2), Sobolev duality (PROVED), the Deshouillers–Iwaniec/Drappeau spectral large sieve (cited; uses
  SEL) and a per-a Weil count. With Kim–Sarnak alone this argument leaves a strip of positive width.
  *Unconditional follow-up* (`EXCEPTIONAL_TYPEI_LOGLOG2.md`, ledger (D)32a; two independent reviews R116,
  R116-B, no FATAL/MAJOR): the strip is handled by DI Thm 7's level-averaged exceptional large sieve (the
  assembly already averages over d; the exceptional term is reduced to interval sums by partial summation).
  Thm 4.1(i) (PROVED relative to DI 1982 Thm 7 and Drappeau 2017 Lemma 4.10):
  `Σ_{p≤N} f_I(p) ≤ Cε₀ N log²N log log N + O_{ε₀}(N log²N)` for every ε₀ > 0, i.e. `o(N log²N log log N)`,
  an unconditional improvement of ET's Type I bound without a rate. Thm 4.1(ii) `≪ N log²N` is CONDITIONAL on
  (EFF) (ε-constants ≤ exp(exp(A/ε))); that (EFF) holds is an Assessment. Uniformity in Drappeau's character
  modulus q₀ is the reviewers' reading of his paper.
  *m-uniform version* (`EXCEPTIONAL_MN4.md`, ledger (D)31 follow-up 3; review R117, no FATAL/MAJOR): Thm 4.1
  (CONDITIONAL on SEL_m for Γ₀(mdq²), even nebentypus): `Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L² + L log² m)/m +
  N m^{−0.35}/L` for 4 ≤ m ≤ L⁵; hence Thm 5.1 `ρ_rep ≪ (L³ + L² log² m)/m + m^{−0.35}` (unconditional for m > L⁵,
  Lemma 0.1) and Thm 5.2: under SEL the density transition for m/p is at log N ≍ m^{1/3}, matching orders on both
  sides (upper half = Thm U, unconditional). R117 also found the displayed (b3) exponent of TYPEI_LOGLOG §8 too
  strong (erratum added there; Thm 8.1 unaffected).
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
scale). **Pointwise state (ledger (H)16–(H)34):**
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
  SI is **not** proved. `POINTWISE_MN3.md` localises the failure: for the
  class-of-one prefix a variant SI_3 needs only a square-root saving
  `U_1(q) ≪ q^{−1/2−δ}` (PROVED reduction); the obstruction is a
  Kloosterman-range residual (Assessment), removable for q ≥ Q_0 by the
  second moment (M2) `Σ R(N)² ≪ X(log X)^C` (CONJECTURE); the range
  q_0 < q < Q_0 is a separate open component.
* *Finite coverings / sterile points* (ledger (H)17 follow-ups, (H)34).
  * Type I, n_p = 7 (`POINTWISE_TYPEI2.md`, `POINTWISE_TYPEI3.md`): under H,
    `C*(r)` equals the least height of a finite Type-I covering of
    {n_p = r} (TYPEI2 Thm A); no certificate exists at the sign point `x̂_9` with f < 10¹²,
    so `C(7) > 1.32·10¹²` under H (CERTIFIED). Levels 5–6 of the Vieta/Pell
    descent are empty (PROVED); sterility of `x̂_9` is open.
    `POINTWISE_TYPEI4.md` (follow-up 3): a fibre certificate at 2-adic level L is a
    norm-1 unit of ℤ[√d], `d = c_o(c_oδ² + 2^{L−4})`, of the shape
    `16PX² − Q·49^b = 1`, `PQ = d` (Pell form, Prop 1.2 / Cor 1.4, PROVED); finite with
    explicit bounds for each (L, b) at all heights (Lemma 3.1, PROVED). CERTIFIED (two
    independent complete engines on the replayed ranges): no certificate at `x̂_9` with
    L ≤ 22, v_7(k) ≤ 3, or L ≤ 26, v_7(k) ≤ 1, **at any height** — complementary to
    the f < 10¹² search. For L ∈ {11, 13, 14, 16, 18–22} the fibre is inhabited at
    other w ≡ 9 (16) (Prop 4.1, CERTIFIED), so arguments that see w only mod 16 cannot
    work there (Assessment). Open: the 7-adic tower b → ∞ at L = 7..10 (at L = 7,
    Lemma 3.6 excludes j = 1 for all b; j ≥ 2 and 7 | j open).
    `POINTWISE_TYPEI5.md` (follow-up 4; review: no FATAL/MAJOR): the tower is **not** closed.
    A solution with u = 7^b is the minimal one (Lemma 1.1, PROVED, all L), so b is determined
    and the d-graded search is complete for all b; Lemma 3.1 repairs TYPEI4 Lemma 3.6 (7 | j).
    Thm 3.7 (PROVED + CERTIFIED, two engines): a certificate at `x̂_9` with 7 ≤ L ≤ 10 needs
    `v_7(k) ≥ 8`, `c_oδ > 10⁶` and lies in the two-parameter regime (v); all other regimes
    are excluded for all b. Regime (v) has σ, λ unbounded; linear forms in logarithms do
    not apply (Assessment).
    `POINTWISE_TYPEI6.md` (follow-up 5; review: no FATAL/MAJOR): regime (v) is **not** closed.
    The polynomial fundamental-unit route (Richaud–Degert / Yokoi type) provably fails for L ≥ 7
    (Prop 2.1, PROVED); regime (v) is the generic large-unit regime (Lemma 3.1), and at L = 13 it is
    inhabited (Remark 1.2), so a closing argument must use T ≤ 64. Under abc each level has finitely
    many certificates (Thm 3.2, CONDITIONAL). CERTIFIED: no fibre certificate at `x̂_9` with
    L = 7–10 and v_7(k) ≤ 15, at any height (two engines except (L, b) = (9,15), (10,14), (10,15)).
    `POINTWISE_TYPEI7.md` (follow-up 6; review R109: no FATAL/MAJOR): a precise **negative** result on
    2-adic closeness. A fibre certificate is at `x̂_9` iff nδ ≡ 5·9⁻¹ (mod 2^{⌈L/2⌉−1}) (Lemma 1.1, PROVED, exact
    formula for v_2(F+9)); certificates come arbitrarily close to w = 9 (Thm 2.1, PROVED, F = 7^s + 2^i) and the
    covered part of the fibre is open and dense (Thm 2.4, PROVED, F = 71^ν). So no 2-adic neighbourhood test can
    prove sterility. CERTIFIED: no certificate at `x̂_9` in the grid 2^{L−4}7^b ≤ 2²⁸ (67 fibre certificates;
    two engines except a few listed one-engine cells).
  * r = 13 (`POINTWISE_MORDELL.md` Thm 3.1, PROVED by finite computation):
    if `(p/13) = −1`, ES holds for p outside 6 classes mod 720720 (2 if also
    `(p/11) = +1`); modest novelty (explicit packaging of the Salez/ET level
    sieve). The point x* lies in no ET class of modulus ≤ 10⁶ (CERTIFIED), but
    **Conj 4.2 ("x* is sterile") is REFUTED** (ledger (F)11; `POINTWISE_MORDELL13B.md`
    Thm 3.1, reviewed): x* lies in the II3 class (a,d,e) = (8,33,11999), modulus
    12670944 = 2⁵·3·11·13²·71 (and in the I2 class (125,88,11999)). MORDELL13B attaches every
    {11,13}-generic class to an ES solution of 4/N, N an {11,13}-unit (PROVED), and
    enumerates to N ≤ 4·10⁷ (CERTIFIED). The (2,2) cell is still not covered (EVIDENCE).
    The new candidate x** = x(2,15) lies in no class with e ≤ 10⁸ (II3/I3/I1), f ≤ 3·10⁷ (II2),
    f, e ≤ 2·10⁷ (I2/II1/I4) (Comp 5.1, CERTIFIED within these ranges); that it is sterile is
    Conj 5.2 (CONJECTURE, EVIDENCE only). The main-variant r = 13 covering question is open again.
    `POINTWISE_MORDELL13C.md` (review: no FATAL/MAJOR): Thm 6.1 (PROVED by finite computation; three
    independent checkers): an adaptive tree certificate (136494 covered leaves, 2140 ET classes) shows
    ES for every prime with (p/13) = −1 outside 35459 explicit classes, 8.42·10⁻⁵ of the six
    exceptional classes mod 720720; no root class closes. Comp 3.1 (CERTIFIED): the uncovered part of the
    (2,2) cell mod 11²13² is exactly {2,57,79} × {15,28,54,132,145}. x** lies in no P/Q-type class with
    e ≤ 2·10⁹ and no I2/II1/I4 class with f, e ≤ 2·10⁸ (CERTIFIED within ranges, one engine);
    it stays a candidate (Conj 5.2, CONJECTURE).
    `POINTWISE_MORDELL13D.md` (follow-up 2; EVIDENCE only, no PROVED claims, not separately reviewed):
    a fast complete C witness engine (all seven ET families, M | L, no size cap), validated against the
    13C engine (0 mismatches; replayed in `verify.py` (en) at L = 9240, 10920). A hybrid DFS does not
    close root 418321 (each open node leaves ≈ 1.3–3 open children); Assessment: closing a root needs a
    structural idea, not more computation.
    `POINTWISE_MORDELL13E.md` (follow-up 3; review R107: no FATAL/MAJOR): x** **survives**. Comp 3.1 (CERTIFIED,
    validated faster engine m13e_es): x** lies in no ET class of any family and any T-free modulus whose ES level
    is N < 2.59·10¹⁰ — all 54 T-units up to 13⁹, so no class of T-level ≤ 161050, e unbounded (2 865 550 ES
    solutions). Since x** ≡ x* (mod 143) and x* is covered, no argument seeing only x mod 143 can prove x** sterile
    (PROVED). Lemma 2.1 (PROVED): parity constraints on v_T(N) in the (2,2) cell. Prop 4.1 (PROVED reduction): a mass
    bound for boxes of level > 13⁹ meeting C_3(x**) would give a sterile point in C_3, hence no finite ET covering
    for (p/11) = (p/13) = −1. Survival looks generic (Assessment); sterility of x** stays Conj 5.2 (CONJECTURE).
  * r = 17 (`POINTWISE_MORDELL17.md`): Thm 4.1 (PROVED) reduces a sterile
    point to an explicit tail bound, whose critical part is the prime-power
    count `#{(a,b): ab ≤ 17^K, (−17^K mod 4ab) | a+b} ≤ C·17^{(1/2−δ)K}`;
    then no finite set of polynomial ES identities covers the Mordell-hard
    primes with n_p = 17
    (CONDITIONAL, Cor 4.2). Existence is Conj 4.3 (CONJECTURE). Levels ≤ 5
    leave 67.7% of each non-residue cell uncovered (CERTIFIED).
    `POINTWISE_MORDELL17B.md` (follow-up 2; one MAJOR rounding error repaired): still
    CONDITIONAL. An exact four-regime P-enumerator (Lemma 2.1) gives D_P(13) = 1463
    (CERTIFIED, two engines); exact unions through P-level 6 leave ρ₁ ≈ 0.677133 uncovered.
    Thm 4.1 (PROVED reduction): `D_P(K) ≤ C·17^{θK}` (odd K ≥ 13) and `D_Q(k) ≤ 17^{3k/5}`
    (odd k ≥ 9) give a sterile point, e.g. θ = 2/5, C ≤ 1.40, i.e. ET's own exponent with an
    explicit constant and no o(1). Conj 4.2 there (D_P(K) ≤ K⁵, D_Q(k) ≤ k⁵) is a CONJECTURE.
    `POINTWISE_MORDELL17C.md` (follow-up 3; review: minors applied): still CONDITIONAL. Cumulative
    bounds `Σ_{13≤K'≤K} D_P(K') ≤ C·17^{θK}` suffice (Lemma 1.1, PROVED, Abel summation), raising the
    admissible C at θ = 2/5 to 1.497; Q-points with c ≥ F^{1/2} are bounded unconditionally (≤ 2 per
    (a,d); Lemma 2.1, Cor 2.2, PROVED). Assessment/EVIDENCE: averaging over K cannot rescue P; a proof
    must show that discrete logs of −e mod 4ab rarely fall in the short window [log_17 4ab, K].
  * Candidate sterile points (x** for r = 13, the 17-generic line for r = 17, and `x̂_9` for
    Type I) remain candidates: no sterile point other than the square points is proved, and the
    first r = 13 candidate x* was refuted. A write-up `paper/es-coverings-note` (task O86) is refereed
    internally (R86: accept after minor revision; repairs applied). The post-referee additions
    TYPEI4 (O91), the x* refutation as Prop 5.4 and x** as an EVIDENCE-level Conjecture 5.6 (O96)
    were refereed in round 2 (R98: no FATAL/MAJOR, D1–D7 applied, TYPEI5 added as Prop 4.15 /
    Thm 4.16). The O106 additions TYPEI6, MORDELL13C, MORDELL17B/17C were refereed in round 3 (R106,
    `reviews/es-coverings-note-referee-r3.md`: accept, minor repairs applied; 29 pp). MORDELL13D
    (EVIDENCE only), TYPEI7 and MORDELL13E are not in the paper.

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
* `verify.py` blocks (dt)–(dv) (O79, ~15 s; full run ≈ 5.1 min, 2 threads, scipy + mpmath) add
  EXCEPTIONAL_LARGESIEVE7 (Lemmas 1.1–1.2 for M < 2000, author + R73 incl. brute-force H* bound;
  (167, 9) example; Prop 4.1 / 5.1 counterexamples on R73 and inline toys with exact H*), POINTWISE_MN2
  (§4 exact δ_m(Q(q₀)): m = 5 up to q₀ = 17, m = 6, 7; author + R74; inline δ_5(Q(8)) = 1/4,
  δ_5(Q(9)) = 1/8, |H_5(840)| = 48/192) and POINTWISE_TAIL (Lemma 3.1 leaf calculus on the R76 toy and
  an inline toy with level-≥ 1 lifts; Lemma 3.2 twist ratio EVIDENCE at T = 10⁵).
* `verify.py` blocks (dw)–(ea) (O85, ~36 s; full run ≈ 5.3–5.6 min, 2 threads, scipy + mpmath) add
  POINTWISE_TYPEI3 (R72 f-engine at x̂_9 to f < 10⁸, 0 certificates; engine = naive brute force at 13
  sign points, needs gcc/cc; Lemmas 1.1–1.2 inline; Lemma 5.1 / Cor 5.2 / Props 5.3–5.5 incl. mod-16/32
  checks), POINTWISE_MORDELL (Theorem 3.1: both certificates in full, integrality on t + Lℤ tested at
  s = 0..4 since I2/I3/II3 coordinates have degree 3–4 in n; 3.1(c); Computation 4.1 at M ≤ 3·10⁴ and
  rigid level 11²13², with positive controls), EXCEPTIONAL_WEIGHTS (Lemma 3.2 exhaustive for ℓ ≤ 29;
  Lemma 3.1 chain; Thm 2.1 chain + Lemma 1.2 brackets on toy LPs) and POINTWISE_MN3 (Lemma 1.1 exact
  probabilities; Lemma 2.1 on 4.2·10⁵ atoms; ET 3/5 product bound, N ≤ 1000, and inline from (M, D)) and
  POINTWISE_MORDELL17 (R83 enumerator data counts to level 5; Comp 3.1 covered fractions 0.235294,
  0.314879 at levels 2, 3 in C_5 and C_7 via R83's union, with a brute-force completeness check (M ≤ 3·10⁴);
  Lemma 1.3 on all data plus an inline brute force; Lemmas 5.1–5.2 and the §6 (a,b)-characterisation at
  levels ≤ 5; needs gcc/cc).
* `verify.py` blocks (eb)–(ec) (O91, ~28 s; full run ≈ 7.5 min on the shared machine, 2 threads, scipy +
  mpmath) add POINTWISE_TYPEI4 (R89 complete engine `review_typei4_jsearch.c` on L = 7..22, b ≤ 1 and
  L = 7..10, b ≤ 3: the 18 fibre certificates and F values of Comp 3.4, none at x̂_9, re-checked with big
  integers; Prop 1.2 (and converse), Cor 1.4, Remark 1.6, Lemma 3.1(iii) on every hit; R89 brute force from
  the definition; example (42,32,71); Prop 4.1 levels; Lemma 3.6 sympy identities and j = 1 for b < 30; needs
  gcc/cc) and EXCEPTIONAL_WEIGHTS2 (Prop 5.3 premise: all ℛ(ℓ) classes QNR for ℓ ≤ 3000, Jacobi −1 for all
  M ≡ 3 (4) ≤ 300, R90 script + inline from the (u,v) definition; §6 mass S(Y)/(log Y)² at Y ≤ 10⁵).
* `verify.py` blocks (ed)–(eg) (O96, ~29 s; full run ≈ 6.6 min on the shared machine, 2 threads, scipy +
  mpmath) add POINTWISE_MORDELL13B (R95 `review_m13b_thm31.py` + author sympy engine; inline: x* in the II3 class
  (8,33,11999) mod 12670944 and the I2 class (125,88,11999), exact solutions on 5 class members each, the prime
  p = 12650497, Lemma 2.1 at the datum; R95 Lemma 1.1/1.2 and Lemmas 2.1–2.4 random tests), EXCEPTIONAL_MN
  (Lemma 1.1 identity by author/R94B scripts and inline exhaustive small ranges; Lemma 2.1 S_m, h_m by author,
  R94A, R94B and inline; toy fibre mass m·μ ∈ [1.18, 1.37] for m = 4..13, EVIDENCE), POINTWISE_TYPEI5 (Lemma 1.1
  minimal-solution brute force, R92 + author + inline; (H), (Lin), Prop 3.3(iii) identities by sympy; L = 7
  regimes (ii)/(iii) and R92's complete engine at b ≤ 3, with positive controls; needs gcc/cc) and
  POINTWISE_MORDELL17B (Lemma 2.1 enumerator = R93 naive scan = stored data at K = 5, 7 as sets; ρ₁, ρ₂ exact by
  both union scripts, with the level-7 Q/U data read from `data/m17b/qu7_*` (two engines, re-validated against
  their definitions); Theorem 4.1 tables floor-rounded vs inline closed forms; needs gcc/cc and GNU `factor`).
* `verify.py` blocks (eh)–(ek) (O105, ~43 s; full run ≈ 7.4 min on the shared machine, 2 threads, scipy + mpmath; log `logs/o105_verify.log`) add POINTWISE_MORDELL13C (Thm 6.1 tree certificate in full with
  R100's from-scratch checker: 6000 splits, 136494 covered / 35459 open leaves, 2140 classes, 0 errors, mean
  open density 8.424e-5, per-root open counts; R100 identities, split primes ≤ 83, open moduli, roots and four
  negative controls; §2 witness engine = R100 brute force at L = 840, 9240; Comp 3.1 enumerator: 0 data at
  λ = 11⁴13⁴, control λ = 143: 34), POINTWISE_MORDELL17C (Lemma 1.1 Abel summation exact; cumulative and
  pointwise tables by author + R98b, floor-rounded vs closed forms; Lemma 2.1 by R98b brute force at
  F = 17, 4913, 1001, 9999 and all F ≤ 1500; Cor 2.2 cost 4.2254e-3), POINTWISE_TYPEI6 (R99 sympy identities;
  inline Lemma 1.1(a)–(c) on two certificates; Remark 1.2 regime-(v) control (13,1) in both Comp 4.1 engines,
  relaxed control (7,293); L = 7, b ≤ 4: 0 solutions, equal candidate counts; needs gcc + libgmp) and
  EXCEPTIONAL_MN2 (emn2_scan = R102B brute force on 6617 (m,p) pairs, m ≤ 60; R102A = R102B; R102A §1
  identities; L_{1/2}(60) = 7.636 from scratch, scanner agrees on the grid).
* `verify.py` blocks (el)–(en) (O113, ~42 s; full run ≈ 8.5 min on the shared machine, 2 threads, scipy + mpmath; log `logs/o113_verify.log`) add EXCEPTIONAL_MN3 (Prop 2.3 pointwise inputs by R108's brute force —
  ρ_{ka}(m₀) ≤ 1[(m₀,k)=1]Σ_{r|m₀}(−ka/r), odd m₀ ≤ 400, k ≤ 40, a ≤ 12; ρ(2^j) ≤ 4 — and six R108 sum rows replayed;
  §2.6 ratio in [0.81, 1.12]; §3 R108 Type I brute force for p < 180 (identities, f_I ≤ 2Σw_c); inline: Prop 3.3
  exponent table, R_bad(η) characterisation at η = 0, 1/20, areas 1, 1/6, 7/72 exactly by rational polygon clipping),
  EXCEPTIONAL_TYPEI_LOGLOG (R111: Lemma 2.1 exact and Lemma 2.2 cosh ≥ 3/2 (attained; Type I ≥ 3) on all F_d pairs,
  d ≤ 30, A ≤ 40, parity-group invariance; author's ttl_separation; O112 §8.0 identities at reduced size (13450 tuples;
  `o112_checks.py` now takes optional CMAX AMAX DMAX) and e/f-cusp densities; R111 Lemma 6.1 transitivity, quadric
  size, g formulas (ℓ ≤ 23) and Lemma 6.3 r(d) bound, d ≤ 150) and POINTWISE_MORDELL13D (m13d_wit.c = m13c_witness on
  every unit mod 9240, 10920: 113942 / 132276 incidences, all/first/req = 13 modes; needs gcc).

## Exceptional-set exponent: where it stands (2026-10-08)

**3/4 is proved sharp for the CRT architectures below; the remaining cases
are reduced to precisely stated open statements** (ledger (D)9–(D)31; all
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
  `EXCEPTIONAL_TUPLES2.md`); genuinely non-CRT input;
* per-frequency weights below 1 (the NONCRT "w < 1" door): reduced
  (`EXCEPTIONAL_WEIGHTS.md`, (D)29, Cor 2.2) to one shift-uniform avoider
  count — for Selberg's band-limited window the door is capped at 3/4 iff (W_𝔊)
  `M_𝔊(N) = max_t #(𝒜 ∩ (t, t+N]) ≥ N e^{−C(log N)^{3/4}}`, uniformly over
  the families a method may use (open). Sharp weights with hit-pattern
  majorants, Q₀ = 1, prime slices `|F_ℓ| ≤ ℓ^γ` (γ < 1/3) and the uniform
  mass hypothesis (M) are capped at 3/4 without (H_eq) (Thm 3.3, PROVED).
  Follow-up (`EXCEPTIONAL_WEIGHTS2.md`): (W) is **neither proved nor refuted**,
  and the CRT-alignment plan provably fails. One maximal family suffices
  (Lemma 1.1); prime slices ℓ ≤ Y push the avoider density below
  exp(−c(log Y)²) (Prop 3.1, PROVED, ineffective via BV), but windows are forced
  to pay only (log N)^{o(1)} of it (Lemmas 2.1–2.2, prime slices; composite case
  partly open); random shifts lose e^{−c(log N)²} (Prop 4.1); quadratic alignment
  caps at √(N log N) (Prop 5.3). For prime slices (W) is a growing-dimension
  Hensley–Richards attainment question (Lemma 5.1, Prop 5.2). A refutation of (W)
  would not by itself give θ > 3/4 (R90 D1/D2).
The first two and the last are *closing* questions (they would extend the
cap); a θ > 3/4 proof needs the third kind of input.

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
* `es-subexp-note` v6: `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o.,
  tail exponent 3 of W over primes (two-sided), the Haar avoider exponent 3,
  1/4 as the ceiling of the Haar-minorant + transfer architecture, the
  conjecture LS ⇒ 1/3, and the m/n analogues (refereed internally six times:
  R33, R33b, R47, R56, R64, R77; novelty audits `reviews/novelty-audit-omega8.md`,
  `reviews/novelty-audit-2026-10b.md`).
* `es-coverings-note`: finite coverings and candidate sterile points
  (TYPEI2/3/4/5/6, MORDELL, MORDELL13B/13C, MORDELL17/17B/17C) — 29 pp; internal referee R86 recommended accept after minor revision, and the repairs are applied (`reviews/es-coverings-note-referee.md`). The post-referee additions O91 (TYPEI4) and O96 (x* conjecture refuted, x** candidate) were refereed in round 2 (R98, `reviews/es-coverings-note-referee-r2.md`: no FATAL/MAJOR, seven minors applied; TYPEI5 added as Prop 4.15 / Thm 4.16). The O106 additions (TYPEI6, MORDELL13C, MORDELL17B, MORDELL17C) were refereed in round 3 (R106, `reviews/es-coverings-note-referee-r3.md`: accept with minor repairs, applied).
* `es-mn-short-note` (26 pp, O97 + O104 + O113): the 3/4 exponent for m/n uniformly in m (`E_m(I) ≪ H exp(−c(log H)^{3/4}m^{−1/4})`), in short intervals and progressions, and the density transition at `log n = m^{1/3+o(1)}`. Everything in Sections 1-7 is PROVED relative to the 3/4 note; Theorems U and L carry the extra inputs listed in the ledger (D)31 follow-up (BV, Shiu; ET Thm 7.1 and the structure of ET's proof of Prop 1.4, BT). Internal referee R97: accept after minor revision; repairs applied (`reviews/es-mn-short-note-referee.md`). O104 added Section 8 "The density transition" from EXCEPTIONAL_MN2 (Theorems U, L; EVIDENCE numerics; Conjecture C2); referee round 2 R104 (`reviews/es-mn-short-note-referee-r2.md`): upper side SOUND, lower side SOUND with minor repairs, m1-m8 applied, recommendation ACCEPT. O113 replaced Theorem L by Theorem L′ from EXCEPTIONAL_MN3 (Lemma 8.6 = MN3 Prop 2.3 with full proof, Prop 8.8 = MN3 Prop 2.5; gap now `(log log N)^{1/3}`) and added Remark 8.10 citing (D)32 (CONDITIONAL on Selberg) as the route to the exact scale; this post-referee addition is not yet refereed (`reviews/es-mn-short-note-referee.md`, "Post-referee addition (O113)").

* `es-typei-heegner-note` (26 pp, O114): Elsholtz–Tao's Type I sum Σ_{p≤N} f_I(p) ≪ N log² N, CONDITIONAL on Selberg's eigenvalue conjecture (ledger (D)32). Internal referee R114: no FATAL/MAJOR defect; repairs applied (`reviews/es-typei-heegner-note-referee.md`).

Authorship and the citation form for astra are still undecided.
