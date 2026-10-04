# Erdős–Straus campaign: summary of the state of the art (2026-10-04)

This file is a human-readable overview. It adds no new mathematics and
does not change any label. The authoritative sources are
`DISCOVERIES.md` (the curated ledger, with status labels) and `STATUS.md`
(the entry point). If this file and the ledger disagree, the ledger wins.

Labels used below are the ledger's:
* **PROVED**: proved in the named file and hostile-reviewed internally;
  nothing in this campaign has been externally refereed.
* **INTERNALLY PROVED**: used for the standalone 3/4 note. It means
  proved and checked internally (including a blind audit), not externally
  refereed.
* **PROVED modulo X**: proved, assuming a cited published theorem X whose
  statement was read but whose proof was not re-checked.
* **CONDITIONAL**: a proved implication from a named unproved hypothesis
  (Schinzel's Hypothesis H, Dickson, Elliott–Halberstam, …).
* **CERTIFIED**: an exact finite computation, re-checked independently.
* **EVIDENCE**: finite computation. "Verified numerically" never means
  "proved".
* **CONJECTURE / Assessment**: heuristics and model computations.
* **CLAIMED/PROVISIONAL**: kept verbatim where the ledger keeps it.

---

## 1. Status in one paragraph

**The Erdős–Straus conjecture (ES) is not solved, here or anywhere.** The
literature was checked through 2026-09-28 (`LITERATURE_2026.md`), with a
priority search through 2026-10-04 (`reviews/novelty-audit-2026-10.md`).
Every recent claimed proof has an identifiable gap. The campaign's best
bound on the exceptional set is

    E(N) ≪ N exp(−c (log N)^{3/4}),

where `E(N)` counts the `n ≤ N` for which `4/n` is not a sum of three
positive unit fractions (`paper/es-threequarter-note.tex`). Its label is
**INTERNALLY PROVED**: three internal reviews, the last a blind
from-scratch audit (`reviews/es-threequarter-blind-audit.md`, SOUND). It
has **not** been externally refereed. The next bound down,
`E(N) ≪ N exp(−c (log N)^{2/3} (log log N)^{1/3})`
(`paper/vaughan-loglog-note.tex`), is a reviewed Theorem
(CORRECT-AFTER-REPAIRS) and is also unrefereed. Vaughan's 1970 bound,
`N exp(−c (log N)^{2/3})`, is the published record in the searched
literature.

The campaign ran two lines of research.
* **Exceptional-set line.** It went from 2/3 to 3/4. It then proved that
  3/4 is sharp for a broad, precisely defined class of congruence sieves.
* **Pointwise line.** It tried to prove ES prime by prime through a
  signed solution graph. That line is **closed**: under standard prime
  hypotheses, the programme cannot work. The closure grew into a
  meta-theorem about procedures. It also produced unconditional
  Ω-results showing that the least multiplier witness `W(p)` exceeds every
  fixed power of `log p` infinitely often.

---

## 2. The exceptional-set line

### 2.1 From 2/3 to 3/4

Notation: `L = log N`. A *forced class* is a residue class `n mod M` on
which a polynomial identity gives a solution of `4/n = 1/x+1/y+1/z`. The
central family is

    ℛ(M) = {−4D mod M : D | ((M+1)/4)²},   M ≡ 3 (mod 4)

(notes §18.1, Lemma 18.1). The method sieves out every `n` that lies in
some forced class and bounds what is left.

Chain of unconditional bounds (ledger section (A)):

| step | bound | label | source |
|---|---|---|---|
| early | `N exp(−c(log log N)²)` | Theorem | notes §12.3 |
| early | `N exp(−(log N)^{1/8})` | Theorem | notes §13.2 |
| | `N exp(−(log N)^{2/5−o(1)})` | Theorem (proved) | notes Thm 14.4 |
| | `N exp(−(log N)^{θ*−o(1)})`, `θ* = log3/(1+log3) ≈ 0.5235` | Theorem (proved) | notes Thm 14.9 |
| Vaughan + loglog | `N exp(−c L^{2/3}(log L)^{1/3})`, for primes and for all denominators | Theorem; review CORRECT-AFTER-REPAIRS | notes Thm 16.4/16.5; `paper/vaughan-loglog-note.tex` Thms 1.1–1.2 |
| 3/4 | `N exp(−c L^{3/4})` | **INTERNALLY PROVED** | `paper/es-threequarter-note.tex` Thm 1.1 |

How the 3/4 bound works (ledger (B)):
* **Multiplier identity** (notes Lemma 16.1). If `kℓ ≡ 3 (mod 4)`,
  `uvw = (kℓ+1)/4` and `nv ≡ −u (mod kℓ)`, then
  `4/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`.
* **Cubic supply.** Power-sized multipliers give forced classes of total
  mass `≍ (log X)³` (notes Thm 18.2; Thm 34.8 with pruning). Note §5 gives
  an unpruned route by Cauchy–Schwarz against Bombieri–Vinogradov
  (notes Thm 76.2, review SOUND-AFTER-REPAIRS). This removes the
  congestion pruning, the ω-cutoff and the unweighted incidence-moment
  lemma from the proof.
* **Assembly.** A fixed family of classes is assembled with exact CRT
  probabilities, a small-prime selector and an even Bonferroni
  polynomial. The coefficient and rounding ledger costs
  `exp(O((log X)⁴))`.
* **Heuristic ceiling.** The class-mass optimisation gives
  `θ = B/(B+1)`. Prime-modulus mass (`B = 2`) gives 2/3. Cubic supply
  (`B = 3`) gives 3/4. This is an **Assessment** under the stated assembly
  model (notes Assessments 18.3–18.4), not a universal theorem.

Label caveats:
* The 3/4 theorem as stated inside the large consolidation draft
  `paper/espaper.tex` (Thm 39.7) keeps its original label,
  **CLAIMED/PROVISIONAL** (ledger (B)7). The INTERNALLY PROVED label
  belongs to the standalone note (ledger (B)11).
* The general-numerator headline of `espaper.tex`, for
  `3 ≤ m ≤ (log N)^{3−ε}`, is **CLAIMED/PROVISIONAL**.
* The cubic witness tail (ledger (A)9) is **CLAIMED/PROVISIONAL**.

### 2.2 3/4 is sharp for coefficient-sum congruence sieves over forced classes

After 3/4, the campaign asked whether the same architecture could go
further. The answer is no, proved in stages. All results here are
**PROVED (internal)**. None is externally refereed, and the constants are
astronomically large (asymptotic statements only).

**Setting.** A *majorant* is `ν(n) = Σ_i a_i 1[n ≡ b_i (mod d_i)]`, with
`ν ≥ 0` on ℤ and `ν ≥ 1` on the whole avoider set (the integers missed by
every class of the family). The method's final bound has the form
`#(avoiders ≤ N) ≤ N·Eν + Σ|a_i|`, with `Σ|a_i| < N` and all family primes
`≤ N^{O(1)}`. The *saving* is `log(1/Eν)`. A bound `E(N) ≪ N exp(−L^θ)`
needs saving `≳ L^θ`.

**Main theorem (EXCEPTIONAL_KARY2.md Thm 5.1, Thm 5.2, Cor 6.1; ledger (D)18).**
Take any finite family mixing four class types: ℛ(M)-classes,
(a,D)-classes, Case-A classes and selector classes `0 mod p`. The moduli
are arbitrary: no size condition, no dominant prime, any number of prime
factors. Then every such majorant saves at most

    C (log N)^{3/4} (log log N)^{3/4}.

If every modulus `G` satisfies `G ≤ P(G)^{1+B}` with `B` fixed, the bound
is `C_B (log N)^{3/4}`, with no `log log` gain possible.
* This covers Bonferroni, Selberg Λ², β/Rosser and every combinatorial
  upper-bound sieve on these classes. It also covers CRT-evaluated moment
  methods.
* The 3/4 note's own majorant `S_y·Q_r(H_X)` is literally in the class.
  Its atoms have `B < 1/120`. **So the 3/4 note is sharp for its method.**
* The Case-A part uses Elsholtz–Tao Prop 1.4 (published, not re-proved).
  The ℛ(M)/(a,D)/selector part uses no external input.
* Reviews: two independent hostile reviews,
  `reviews/exceptional-kary2-review.md` and `-review-2.md`. Round 2
  verified all repairs.

**How it was reached:**
1. `EXCEPTIONAL_THETA.md` (ledger (D)9–11). This is the sieve-limit
   theorem for prime-slice systems (Thm 2.5). The Rankin functional
   `Ψ = inf_α [αλ + Σ p̄_ℓ ℓ^{−α}]` bounds the saving, and the Case-B profile
   `Σ p̄_ℓ ℓ^{−α} ≪ α^{−3}` turns this into `λ^{3/4}`. The theorem is then
   extended to moduli with a dominant prime (Thm 2.7, Cor 3.6). The same
   analysis shows the 2/3-loglog note is sharp for its own architecture
   (Cor 3.5). Λ² sieve limit for arbitrary systems via noise stability:
   Thm 5.5. Review: `reviews/exceptional-theta-review.md`,
   SOUND-AFTER-REPAIRS.
2. `EXCEPTIONAL_BALANCED.md` ((D)12): a partial result for gapped
   balanced moduli under an extremal hypothesis (E_δ).
   **PROVED/CONDITIONAL.** Superseded by step 3.
3. `EXCEPTIONAL_TWIN.md` ((D)13): gapped balanced moduli,
   unconditionally. Key idea: the Mordell obstruction used constructively.
   Every Case-B class has Jacobi symbol −1, so a base made of quadratic
   residue products avoids all small-modulus classes cheaply.
4. `EXCEPTIONAL_TWIN2.md` and `EXCEPTIONAL_TWIN3.md` ((D)14): the two-prime
   Λ² cap, twins included. It was conditional in TWIN2; TWIN3 Thm 4.1 made
   it unconditional.
5. `EXCEPTIONAL_TWIN4.md` ((D)16): the Λ² cap for `r` large primes,
   `≪ L^{3/4}(log L)^{3r+O(1)}`. For fixed `r` the B-hypothesis is removed.
6. `EXCEPTIONAL_KARY.md` ((D)17): every nonnegative CRT majorant over
   ℛ(M)-families with fixed `B` saves `≪_B λ^{3/4}`; twins, prime-power
   tops and any shape are allowed. The tool is a weighted k-ary
   comparison theorem (Thm 2.5): couple a sequential law with a product
   law, then extrapolate along artificial Bernoulli replacement coins.
7. `EXCEPTIONAL_NONCRT.md` ((D)15): several "non-CRT" inputs are also
   capped at 3/4 for the finite prime-slice families (details in §2.3).
8. `EXCEPTIONAL_KARY2.md` ((D)18): the main theorem above. A unit-square
   base serves all four class types, because no (a,D)- or Case-A class
   contains a square (Mordell/Jacobi). Rankin's trick plus Cauchy–Schwarz
   on smooth-dominated moduli removes `B`. The cost is
   `(log log)^{3/4}` in the cap.

Write-up: `paper/sieve-limits-note.tex` ("why 3/4 is sharp for congruence
sieves"; refereed internally, fixes applied; v3 merged).

### 2.3 What the sharpness theorem does not cover

The exclusions are taken from ledger (D)18, KARY2 §6, NONCRT §6 and
STATUS.md. A proof of `θ > 3/4` would need at least one of the following:
* **Cancellation between frequencies.** That is, a direct count of the
  interval sum `Σ_{n≤N} ν(n)`. NONCRT Thm 8.1 gives a quantitative
  dichotomy (PROVED). Either there is large Fourier mass above every level
  `λ ≤ c(log N)^{4θ/3}`, or the interval count falls well below the CRT
  mean. In one tested family (count polynomials of degree ≤ 10) there
  was no inter-frequency gain (EVIDENCE, NONCRT §8.3).
* **Per-frequency weights below 1.** Weights `w ≥ 1` are capped (NONCRT
  Thm 2.3): coefficient sums, the sawtooth bound, and complete
  Gauss/Kloosterman sums. Weights `< 1` are open, except in a smooth-window
  case that is CONDITIONAL on an equidistribution conjecture.
* **Genuinely arithmetic, non-CRT input.** For example, counting
  `(log N)^{3/4+δ}`-fold correlations of ES solutions directly.
* **Other ingredients outside the class:**
  * the large sieve beyond prime slices;
  * majorants that are `≥ 1` only on `[1,N]` or only on exceptional
    primes (majorants `≥ 1` only on primes *are* capped, NONCRT
    Thms 3.2–3.3, so BV/BDH/EH/GRH-level prime inputs do not help);
  * class types other than the four above;
  * family primes beyond `N^{O(1)}`.
* **A sharper constant without `B`.** For general moduli the cap carries
  a factor `(log log N)^{3/4}`. Whether it can be removed is open.

Model-only remark: the a-frame/multiplicative route sits at
`θ* ≈ 0.52` under its model, below 3/4 (**Assessment**, ET §5.2). The
proposed universal "0.5823 ceiling" was withdrawn as restricted-model only
(ledger (F)6).

---

## 3. The pointwise line

### 3.1 The signed graph, closed conditionally

**The idea.** Let `p = 4t+1`. The signed integer solutions of
`4/p = 1/x+1/y+1/z` form a finite set. Make it a graph by joining two
triples when they share a denominator. The seed `(t, −2pt, −2pt)` exists
for every such `p`. The *seed-component conjecture* says the seed's
component always contains an all-positive vertex. It would imply ES for
`p ≡ 1 (mod 4)`.

**Known versus new (ledger (G)1–4, `LITERATURE_2026.md`):**
* The signed character dichotomy (a signed vertex is all-positive iff its
  same-valuation pair has opposite Legendre characters mod `p`) is
  **KNOWN**: Bright–Loughran 2020, Thms 1.2 and 1.5 at `n = p`. The
  positive direction goes back to Yamamoto 1965.
* Finiteness of the signed set is **KNOWN** (Bright–Loughran Lemma 3.10).
* The labels and the Type I chart are Elsholtz–Tao coordinates in
  disguise.
* The refactor graph itself, the seed, the hub bridge and the fibre
  counts are **PROVED (elementary; no prior source found)**.

**Results:**
* **Short escapes** (DEPTH3.md Thm 1, PROVED). Exact classification of
  escapes from the seed of length ≤ 3.
* **Exits and exceptional sets** (DEPTH3 Thm 3 + Corollary). Every prime
  outside Mordell's six classes mod 840 has seed distance exactly 2
  (PROVED). Moreover `#{p ≤ N : dist > 2} ≪ N/(log N)^{11/2}` and
  `#{p ≤ N : dist > 5} ≪ N/(log N)^{10}`. These are PROVED modulo a
  standard sieve theorem, using Dahan's half-dimension lemma.
* **Unbounded distance** (DEPTH3 Thm 2, CONDITIONAL on H). For every `k`
  there are infinitely many `p = 24q+1` such that every vertex within
  distance `k` of the seed is nonpositive.
* **Theorem F** (FORMAL_CLOSURE.md; ledger (G)12). Assume Hypothesis H for
  an explicit family of 6402 polynomials of degree ≤ 2. Then for infinitely
  many `p = 24q+1` the *whole* seed component has no all-positive vertex.
  The component is the set of values of 7883 explicit formal vertices.
  Label: **CONDITIONAL on H (proved implication) + CERTIFIED.** The
  certificate was reproduced by an independent from-scratch engine
  (`reviews/formal-closure-review.md`: all 9961 fibres equal, logic
  CORRECT). No example is within computational reach, and ES itself is
  untouched.
* **Companion result** (sibling project `../erdos-straus-astra`, read-only).
  It reached the same conclusion first and in stronger form: it needs only
  Dickson's conjecture for 159 linear forms. On the subprogression
  `n ≡ 507 (857)` it also exhibits a positive solution outside the sterile
  component; that part needs Dickson for the restricted tuple. Later astra
  work (STATUS.md, 2026-10-02 and 2026-10-04) relaxed one prime condition to
  a divisor condition and ruled out some extensions, but there is still
  **no unconditional sterile seed**. The paper should cite the astra
  version first.
* **Supporting results:**
  * SIZE_CONJECTURE.md (CERTIFIED/PROVED): certified sterile components
    larger than the seed component.
  * WINDMILL.md: parity lemmas (PROVED) and negative scans (EVIDENCE).
    Theorem 7: large p-free buckets are singletons.
* **Evidence** (DEPTH3 §5). Every prime `p ≡ 1 (4)` below `10^12` has seed
  distance ≤ 3. No prime of distance ≥ 4 is known.

**Verdict.** The seed-component conjecture is **OPEN unconditionally and
FALSE under H**. So this line cannot prove ES. Write-up:
`paper/pointwise-obstruction.tex` (29 pp; internal hostile referee, round
2 ACCEPT pending the authorship and astra-citation decision).

### 3.2 The formal-genericity meta-theorem

The common mechanism behind Theorem F, DEPTH3 Thm 2 and the Elsholtz–Tao
"odd-square" remark is stated as theorems about *procedures* in
`POINTWISE_SIZE.md`. Review: `reviews/pointwise-size-step1-review.md`,
SOUND-AFTER-REPAIRS.
* **Theorem M (transfer principle; PROVED, existence CONDITIONAL).**
  * *Procedures covered:* deterministic procedures built from ring
    operations, floor division, eventual-sign tests, factorisations,
    divisor lists and loops over them.
  * *Claim:* if the formal run at a profinite point `q*` is finite, then
    at every admissible `q` the actual run follows the formal run step by
    step.
  * *Existence of admissible `q`:* CONDITIONAL on H for the finite family
    of polynomials met (Dickson if linear; Dirichlet/Linnik if only `p` is
    factored).
  * Novelty: this formalises the standard generic-point / Hypothesis-H
    principle. No prior procedure-level statement was found.
* **Lemma CT (character trap, PROVED).** For `p ≡ 1 (4)`, every p-free
  denominator of every positive solution has a prime factor that is a
  non-residue mod `p`.
* **Theorem C (formal odd-square principle, CONDITIONAL on H).** Every
  correct bounded witness-producing ES procedure fails for infinitely many
  `p ≡ 1 (24)`. Theorem F, DEPTH3 Thm 2, notes Thms 5.1/17.3 and the
  Elsholtz–Tao remark are instances. Novelty is partial (§5).
* **Scope (Proposition A, PROVED).** Eventual-sign size comparisons of
  boundedly many formal quantities are *inside* the obstruction. This
  includes comparisons against `p^θ`, against `log p`, and short-interval
  tests on formal divisors. So "using the size of p" this way does not
  escape. A pointwise proof must use one of:
  * (E1) a search whose length grows with `p`;
  * (E2) non-quasi-polynomial primitives (`⌊p^θ⌋`, the least
    non-residue, oscillating archimedean tests), and then control actual
    factorisations.

  Whether fixed non-abelian Frobenius data (E3) escapes is open.

### 3.3 Ω-results for the least witness modulus

**Definition** (notes (51.1); POINTWISE_OMEGA §0):

    W(n) = min{ M ≡ 3 (mod 4) : n mod M ∈ ℛ(M) }.

So `W(p) ≤ T` means some multiplier congruence with modulus at most `T`
forces a solution for `p`, and `W(p) < ∞` implies ES at `p`. Squares have
`W(m²) = +∞` (notes Thm 58.1, PROVED). "Hard" means Mordell-hard (in one
of Mordell's six classes mod 840).

The question: is `W(p)` bounded by a fixed power of `log p` (the
hypothesis `H_MOD(A)`)? If so, a pointwise multiplier mechanism with
polylogarithmic moduli could prove ES. The campaign shows it is not.

| result | statement (infinitely many Mordell-hard primes `p`) | label | source |
|---|---|---|---|
| notes Thm 54.1 | `W(p) ≥ c log p` (constant `1/5.2` via Xylouris' Linnik exponent) | PROVED, effective | notes §54 |
| Thm 11.2 | `limsup W(p)/log p ≥ 5/8` | PROVED modulo Chang 2014 Cor. 11 | POINTWISE_SIZE |
| Thm 5.1 | `W(p) ≥ (log p)² exp(−C log₂p/log₃p)` | PROVED modulo Thorner–Zaman, effective | POINTWISE_OMEGA |
| Thm 5.1, Cor 5.2 | `W(p) ≥ (log p)³ exp(−C log₂p/log₃p)` | PROVED modulo Thorner–Zaman, effective | POINTWISE_OMEGA2 |
| Thms 4.3, 5.2 | **for every fixed k:** `W(p) ≥ (log p)^k exp(−C_k log₂p/log₃p)`; equivalently `log L_h(T) ≤ T^{o(1)}` | PROVED modulo Thorner–Zaman, effective; no explicit rate as `k → ∞` | POINTWISE_OMEGA3 |
| Cor 3.1 | **explicit rate:** `log W(p) ≥ (1+o(1)) log₂p · log₃p / log₄p` | PROVED modulo Thorner–Zaman and Elsholtz–Tao Prop 1.4 | POINTWISE_OMEGA4 |
| Cor 3.1 (variant) | `log W(p) ≥ (1+o(1)) log₂p · log₄p / log₅p` | PROVED modulo Thorner–Zaman alone | POINTWISE_OMEGA4 |

Here `log_j` is the j-fold iterated logarithm. `L_h(T)` is the least hard
prime with `W > T`.

**Method, in brief.**
* Impose the class of one at small primes, so the remaining congruence
  system is local at a few free primes.
* Build a pointwise minorant of the void indicator. It uses
  inclusion–exclusion truncated by *support size*, organised in levels.
  It also uses a conditional local lemma (Haeupler–Saha–Srinivasan), and
  heavy "hub" vertex sets are pushed down to lower levels by Markov steps.
* Transfer to primes with Thorner–Zaman's Linnik-range prime number
  theorem in progressions (Math. Z. 306 (2024), Cor. 1.4). Its error term
  absorbs a possible Siegel zero.

**Consequences.**
* `H_MOD(A)` is **REFUTED for every A** (ledger (F)10, (H)13).
* So no pointwise multiplier mechanism with polylogarithmic witness
  moduli can prove ES.

**Related results.**
* *Heuristic truth.* `log W ≍ (log p)^{1/3}` (**Assessment**,
  POINTWISE_SIZE §7). Data: `W ≈ (log p)^{2.5–3.4}` for
  `10^8 ≤ p ≤ 10^50` (EVIDENCE).
* *Haar side* (profinite avoider density `δ*(T)`).
  `log(1/δ*(T)) ≤ T^{o(1)}` unconditionally, and
  `≪ (log T)^7 log log T` modulo Elsholtz–Tao Prop 1.4. Source:
  POINTWISE_OMEGA2 Thm 11.3, PROVED. This does not transfer to primes.
* *Bottleneck.* The factorial loss in OMEGA4 comes from the Markov
  push-down cascade. A saturated-hub codegree hypothesis HC* would give
  `log W ≥ 0.2√a (log₂p)^{3/2}`: OMEGA4 Thm 4.2, a PROVED implication.
  Two caveats:
  * HC *as literally stated* in OMEGA4 is **false**. POINTWISE_OMEGA5
    corrects it to HC*.
  * The `m = 1` part of HC* is PROVED (OMEGA5 Thm 2.3). The rest reduces
    to an open divisor problem, HC_Π.

  The proved rate remains OMEGA4 Cor 3.1.
* *Type-I slice parameter* (POINTWISE_OMEGA Thm 8.5, ledger (H)9).
  * `ck_min(p) ≫ log p · log₃p` infinitely often: PROVED modulo Lau–Wu
    Prop 5.1, not effective.
  * This is Graham–Ringrose's 1990 Ω-bound for the least quadratic
    non-residue, transported by a Yamamoto-type lemma.
  * Only the equivalence "congruence methods certify exactly `n_p`" is
    campaign content.
* *Write-up.* `paper/es-omega-note.tex` v3 (31 pp; internal referee
  `reviews/es-omega-note-review-v3.md`, P1–P4 applied).

### 3.4 Window results

**The window frame** (POINTWISE_SIZE §8; ledger (H)5).
* *Definition.* `a_min(p)` is the least `q ≡ 3 (mod 4)` such that the
  divisor-ratio spectrum `Rat_q((p+q)/4)` contains `−1` or `−p`.
* *Equivalence* (Thm 8.1, PROVED). ES holds at `p` iff `a_min(p) < ∞`.
* *Reciprocity* (Lemma 8.2, PROVED). Window reciprocity holds.
* *Not congruence-forced* (Lemma 11.3, PROVED). Window failure is never
  forced by congruences.
* *Unbounded* (Prop 8.4, CONDITIONAL on Dickson). `a_min(p)` exceeds every
  `K` infinitely often.
* *Random model* (**Assessment**). `a_min(p) ≍ log p / log log p`. This is
  just above the formal-obstruction scale.
* *Evidence.* `a_min/log p < 10` up to `10^8`, and in samples up to
  `10^24` (EVIDENCE).
* *Target.* **Conjecture X_win(C):** `a_min(p) ≤ C log p` for every prime
  `p ≡ 1 (24)` with `p > 10^18`. For any `C` it implies ES (Thm 8.1;
  the cutoff relies on existing verification). The concrete conjecture put
  forward is X_win(10). It is the natural (E1) target.

**Unconditional and conditional Ω-results** (POINTWISE_WINDOW.md; review
`reviews/pointwise-window-review.md`):
* **Thm W1.** `#{p ≤ x hard : a_min(p) ≥ 7} ≫ x/(log x)^{3/2}`, via
  `p ≡ 1 (840)` and window 3 failing. **PROVED modulo cited sieve
  theorems**: semi-linear lower sieve, Selberg upper sieve, BV. It is also
  implied by Fuchs–Hsu–Rickards–Schindler–Stange 2025 Thm 1.1(2).
* **Thm W2.** `#{p ≤ x hard : a_min(p) ≥ 11} ≫ x/(log x)²`.
  **CONDITIONAL on Elliott–Halberstam**; a fixed level `x^{1−ε₀}`
  suffices. It has the same shape as Friedlander–Iwaniec 2009 (hyperbolic
  PNT).
* **Unconditional `a_min → ∞`** is not reached. The obstruction is
  linear-sieve parity at two windows (**Assessment**). Unconditional
  `K = 11` is the window analogue of the open unconditional case of
  Friedlander–Iwaniec 2009.
