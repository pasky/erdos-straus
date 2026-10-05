# Erdős–Straus campaign: summary of the state of the art (refreshed to main after ledger (D)26 and (H)27)

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
  3/4 is sharp, with no `log log` loss, for every coefficient-sum
  congruence sieve over any mixture of forced classes. Later work
  extended the cap to large sieves (twisted, hybrid, applied to primes),
  to prime-only majorants and to inter-frequency cancellation for moduli
  `≤ N/2`. The remaining doors above 3/4 are precisely stated: the
  repaired tuple-count hypothesis TC^alt_θ (a CONJECTURE), the
  large-sieve hypothesis H_LS∞ for forced families (a CONJECTURE), the
  combinatorial statement "weak SPW" for hybrid methods (open; the
  fixed-σ version is refuted), and genuinely non-CRT arithmetic input.
* **Pointwise line.** It tried to prove ES prime by prime through a
  signed solution graph. That line is **closed**: under standard prime
  hypotheses, the programme cannot work. The closure grew into a
  meta-theorem about procedures. It also produced unconditional
  Ω-results for the least multiplier witness `W(p)`. The rate went from
  every fixed power of `log p` to
  `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` for infinitely many
  hard primes (PROVED modulo Gallagher's theorem and Nair–Tenenbaum).
  The matching profinite (Haar) exponent is exactly 3 up to logs, so the
  heuristic truth is `log W ≍ (log p)^{1/3}`. Exponent 1/4 is proved to
  be the ceiling of the architecture used; 1/3 would need bilinear or
  parity-sensitive prime input. Window results give exact orders for
  bounded windows and show that parity input is necessary.

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
  mass `≍ (log X)³` (notes Thm 18.2). With pruning this is notes Thm 34.8, whose chain kept
  the label CLAIMED/PROVISIONAL (ledger (B)6). Note §5 gives
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
further. The answer is no, proved in stages. Unless marked otherwise, the
results here are **PROVED (internal)**. None is externally refereed, and
the constants are astronomically large (asymptotic statements only).

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
is `C_B (log N)^{3/4}`.

**Sharp form, no `log log` loss (EXCEPTIONAL_KARY3.md Thm 4.1, Cor 4.2;
ledger (D)24).** For the same mixtures, with arbitrary moduli and no
B-hypothesis, every CRT majorant of level λ has `log(1/Eν) ≤ Cλ^{3/4}`,
and coefficient-sum CRT methods save at most `C_A (log N)^{3/4}` when the
family primes are `≤ N^A`. So the cap is exactly `(log N)^{3/4}`.
* The old loss came from Rankin's trick on dyadic blocks of smooth
  moduli. KARY3 replaces it by a local moment
  `Z_y(M) = Σ_{p^ν | M, p^ν ≤ y} Λ(p^ν)/log y`, with a fourth moment
  controlled by Shiu's theorem in progressions.
* Variants: truncated weights `min(log ℓ, L₀)` (Thm 5.1); majorants of
  bounded prime order `k` save `≤ C_A[(log N)^{3/4} + k log log N]`
  (Cor 5.2). The `log log` factors in (D)18–(D)20 and (D)22 can all be
  dropped.
* Label: **PROVED given KARY2 as reviewed** (internal; review
  `reviews/exceptional-kary3-review.md`, all claims SOUND; Case A uses
  Elsholtz–Tao, published, not re-proved). §§6–7 of KARY3 were added
  after the review and checked by the parent only.
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
2. `EXCEPTIONAL_BALANCED.md` ((D)12, PROVED/CONDITIONAL on (E_δ)), then
   `EXCEPTIONAL_TWIN.md` ((D)13): gapped balanced moduli, now
   unconditionally. Key idea: the Mordell obstruction used constructively.
   Every Case-B class has Jacobi symbol −1, so a base made of quadratic
   residue products avoids all small-modulus classes cheaply.
3. `EXCEPTIONAL_TWIN2.md` and `EXCEPTIONAL_TWIN3.md` ((D)14): the two-prime
   Λ² cap, twins included. It was conditional in TWIN2; TWIN3 Thm 4.1 made
   it unconditional.
4. `EXCEPTIONAL_TWIN4.md` ((D)16): the Λ² cap for `r` large primes,
   `≪ L^{3/4}(log L)^{3r+O(1)}`. For fixed `r` the B-hypothesis is removed.
5. `EXCEPTIONAL_KARY.md` ((D)17): every nonnegative CRT majorant over
   ℛ(M)-families with fixed `B` saves `≪_B λ^{3/4}`; twins, prime-power
   tops and any shape are allowed. The tool is a weighted k-ary
   comparison theorem (Thm 2.5): couple a sequential law with a product
   law, then extrapolate along artificial Bernoulli replacement coins.
6. `EXCEPTIONAL_NONCRT.md` ((D)15): several "non-CRT" inputs are also
   capped at 3/4 for the finite prime-slice families (details in §2.4).
7. `EXCEPTIONAL_KARY2.md` ((D)18): the main theorem above. A unit-square
   base serves all four class types, because no (a,D)- or Case-A class
   contains a square (Mordell/Jacobi). Rankin's trick plus Cauchy–Schwarz
   on smooth-dominated moduli removes `B`. The cost is
   `(log log)^{3/4}` in the cap.
8. `EXCEPTIONAL_KARY3.md` ((D)24): removes that cost (above).

Write-up: `paper/sieve-limits-note.tex` ("why 3/4 is sharp for congruence
sieves"; v4 states the cap with no `log log` loss and adds the large-sieve,
prime-only, hybrid and tuple sections of §2.3; v4 refereed internally in
R36, MINOR REVISION, fixes applied). The 3/4 note
now has a remark that its ceiling is a theorem for its own architecture
(sieve-limits v3 Thm 10.8 / Rem 10.9; KARY2 Cor 6.1). It replaces the
note's earlier heuristic-ceiling caveat. The (D)19–(D)21 results are in
separate files (§2.3).

### 2.3 Beyond coefficient sums: the large sieve, interval cancellation, tuple counts

Later files close or sharpen the main doors left open by (D)18. All are
internal and unrefereed. With KARY3 ((D)24), every `(log log N)^{3/4}`
factor quoted in this subsection can be dropped.

* **The large sieve is capped** (`EXCEPTIONAL_LARGESIEVE.md` Thm 3.1,
  Cor 3.2; ledger (D)19).
  * *Duality.* By exact duality (Thm 2.1, standard minimax, not claimed
    new), every CRT-admissible large-sieve bound is at least `N·E|g*|²`,
    where `|g*|²` is a Selberg-square CRT majorant.
  * *Bounds covered.* Montgomery, Montgomery–Vaughan, weighted, and
    multiplicative via Gauss sums.
  * *Frequencies covered.* Farey frequencies with prime, prime-power or
    composite denominators. Forced classes may be used in any form, and
    the bound may be applied fibrewise.
  * *Result.* Combined with KARY2 Thm 5.1, the saving is at most
    `C(log N)^{3/4}(log log N)^{3/4}` for polynomial denominators, and
    `C_B(log N)^{3/4}` for bounded B. This includes the 2/3 note's use of
    the large sieve.
  * *Further cases.* Prime slices with any rational frequencies: Thm 4.1.
    Gallagher's larger sieve in kernel form is capped by a χ² functional
    (Thm 6.2).
  * *Label:* **PROVED, conditional on KARY2 Thm 5.1**.
    Review: `reviews/exceptional-largesieve-review.md`, SOUND.
  * *Open escapes (as of (D)19):* super-polynomial frequency levels
    (H_LS); the larger sieve over mixtures; twisted/hybrid forms;
    non-CRT interval information.
* **The large-sieve escapes are closed except H_LS**
  (`EXCEPTIONAL_LARGESIEVE2.md`; ledger (D)25).
  * *Comparison measure (Lemma 1.1, LP duality).* The KARY2/KARY3 cap is
    equivalent to one probability measure on the sifted set that is
    within `e^{S(λ)}` of uniform on every nonnegative level-λ test.
  * *Twisted and hybrid forms (Thm 2.4, Cor 2.5).* Every Bessel-type
    inequality with periodic rows of polynomial period (additive,
    multiplicative, mixed `χ(n)e(nθ)`, Gauss-sum rows, fibrewise use)
    is capped at `C_A(log N)^{3/4}`. The large sieve applied to the
    primes has the same cap relative to π(N) (Thm 3.1).
  * *Gallagher's larger sieve* with prime-power kernels over any mixture
    saves at most `26 log log N + C`, unconditionally (Thm 4.3).
    Composite kernels are capped up to a factor `1 + Nh/(W_K−h)` (Thm 9.1).
  * *Band-family escape (§§8–9, PROVED).* The comparison measure plus
    large-sieve axioms alone cannot close H_LS∞. For a dense abstract
    "band" family, every majorant of level below the band levels has
    mean ≥ 1, yet a Montgomery–Vaughan large sieve on the sumset of the
    band frequencies saves ≥ c log N. So a cap for forced families must
    use their sparsity or K2's moment hypotheses.
  * *Label:* **PROVED** (internal; conditional on KARY2/KARY3 where
    cited). Reviews: `reviews/exceptional-largesieve2-review.md` and
    `-review-2.md`. *Open:* H_LS∞ for forced families
    (**CONJECTURE**, Prop 5.2); composite kernels with huge
    `Nh/(W_K−h)` and small prime factors.
* **Inter-frequency cancellation is worthless for moduli ≤ N/2**
  (`EXCEPTIONAL_INTERFREQ.md`; ledger (D)20).
  * *Selberg minorant.* If every nonzero frequency of `ν ≥ 0` has
    denominator `≤ D < N`, then `Σ_{n≤N} ν ≥ (N−D)Eν` (Thm 2.2).
  * *Cap (Cor 2.3).* Majorants built from forced classes of modulus
    `≤ N/2` save at most `C(log N)^{3/4}(log log N)^{3/4}`. This holds
    with any coefficients and any evaluation of the interval sum: exact,
    dispersion, Kloosterman, Vaaler, or smooth windows.
  * *Larger classes.* The cap holds for methods whose bound dominates
    `T_>^*/c` (Thm 2.5, Rem 2.6). It is **not** proved for hybrid methods
    that charge large classes only their trivial count.
  * *Label:* **PROVED** (internal). Review:
    `reviews/exceptional-interfreq-review.md`.
  * *What remains:* multi-witness tuple counting above modulus N
    (Assessment). (H_eq) is open but not needed when all moduli are
    `≤ N/2`.
* **Hybrid methods reduced to a combinatorial hypothesis**
  (`EXCEPTIONAL_INTERFREQ2.md`, `EXCEPTIONAL_SPW.md`; ledger (D)26).
  * *Setting.* Hybrids charge each class of modulus `> N/2` only its
    least position-blind count. They have an exact LP dual (Prop 2.1).
    A sign rule (Lemma 3.1) shows that right-signed large classes can be
    counted exactly, so no inequality `B_hyb ≥ c·N·Eν` holds and the
    (D)20 accounting does not extend verbatim.
  * *Caps.* The 3/4 cap holds when the right-signed mass is `≤ c·B`
    (Cor 5.1, PROVED). It holds for every hybrid whose right-signed mass
    at moduli in `(N/2, CN]` is `O(e^{O(S)}B)`, conditional on a
    hypothesis Flat (Thm 5.2, PROVED implication). Flat follows from a
    purely combinatorial statement SPW about measures that count every
    small-modulus class exactly as `[1,N]` does (Prop 9.1).
  * *SPW with fixed σ is false* (`EXCEPTIONAL_SPW.md` Thm 3.2, PROVED;
    Fejér smoothing plus Bernstein's inequality): such measures have
    `σ ≲_C (log N)^{−1/2}`, with exact rational certificates at N = 300
    and N = 1150. The earlier "σ* = 2/5 at every N" pattern was a small-N
    artefact. Thm 5.2 needs only **weak SPW** (`σ_N ≥ c₀e^{−S_A}`), which
    Thm 3.2 does not touch and which is **open**.
  * *Label:* **PROVED / PROVED implication as labelled** (internal;
    reviews `reviews/exceptional-interfreq2-review.md`,
    `reviews/exceptional-spw-review.md`, SOUND). No hybrid beating 3/4
    was found.
* **The tuple-count door** (`EXCEPTIONAL_TUPLES.md`; ledger (D)21).
  * *Reformulation (Lemma 1.3).* Order-k witness correlations are the
    distinct-prime parts of k-point correlations of ω-type functions
    along shifts `4D`.
  * *Conditional route above 3/4 (Cor 2.3, PROVED implication).*
    Hypothesis TC_θ asks for CRT-accurate correlations up to order
    `K ≍ (log N)^θ`. It implies
    `E(N) ≤ (e+2)N exp(−(2/e²)(log N)^θ)`.
  * *Range of TC.* It holds for `K ≤ c(log N)^{2/3}` (Prop 2.4, Brun's
    pure sieve; this recovers 2/3). It fails for even
    `K ≥ (e²/2+ε)log N`, because squares avoid every class (Prop 4.2).
  * *Bounded order is useless.* Correlation input of bounded order,
    however precise, cannot give θ > 3/4 under CRT-main-term evaluation.
    Order `≳ (log N)^θ/log log N` is needed (Thm 3.1, Cor 3.2–3.4).
  * *Wrong type.* Fixed-shift correlation theorems (Heath-Brown,
    Deshouillers–Iwaniec, Matomäki–Radziwiłł–Tao, Tao–Teräväinen) do not
    fit (Prop 4.3 plus Assessment).
  * *Label:* **PROVED** (internal). Review:
    `reviews/exceptional-tuples-review.md`, all items SOUND.
  * *Open (as of (D)21):* TC_θ for `3/4 < θ < 1`, stated as a
    **CONJECTURE**; it was repaired in (D)23 (next item).
* **TC_θ repaired** (`EXCEPTIONAL_TUPLES2.md`; ledger (D)23).
  * *Forced zeros.* Tuples whose form-group product exceeds `Ns+r` have
    interval count 0 but positive CRT mass. For every θ > 2/3 this mass
    exceeds the TC precision by `e^{K/(2e²)}` (Thms 2.1–2.2). So the
    literal TC_θ, θ > 2/3, holds only with a compensating CRT excess on
    admissible tuples (Cor 2.3, PROVED necessary condition). That the
    literal TC_θ is false on (2/3, 1) is an Assessment, not proved.
  * *Repair.* The forced-zero term cancels in the alternating sum (an
    Euler-characteristic identity). The one-sided alternating hypothesis
    TC^alt_θ, and TC^𝔄_θ (accuracy on admissible tuples only), each still
    imply `E(N) ≤ C N exp(−(2/e²)(log N)^θ)` (Thm 4.1, Cor 4.2, PROVED
    implications). **TC^alt is the correct form of the tuple-count door.**
  * *Difficulty.* For the pure prime family, CRT-main-term sieves save
    `≤ C(log N)^{2/3}` (Cor 6.1); so TC^alt_θ with θ > 2/3 needs accuracy
    at moduli `exp(c(log N)^{3θ/2})`, which no known theorem reaches
    (Assessment).
  * *Label:* **PROVED** (internal; review
    `reviews/exceptional-tuples2-review.md`, SOUND). TC^alt_θ for
    θ > 3/4 is open.

* **Prime-only majorants** (`EXCEPTIONAL_PRIMELAW.md`; ledger (D)22).
  Majorants that are ≥ 1 only at the primes of the avoider set, for any
  mixture of forced and selector classes, save at most
  `Cλ^{3/4}(log λ)^{3/4}` (the log factor is dropped by (D)24).
  Prime-law methods with all moduli ≤ N^A save at most
  `C_A(log N)^{3/4}`; this includes
  SW/BV/BDH/EH/GRH-level inputs. **PROVED** (internal; Case A uses
  Elsholtz–Tao Prop 1.4). Review: `reviews/exceptional-primelaw-review.md`.

### 2.4 What remains open above 3/4

The sources are ledger (D)18–(D)26, KARY2 §6, NONCRT §6 and STATUS.md.
The cap is now exactly `(log N)^{3/4}` (no `log log` loss, (D)24) for
coefficient-sum sieves, large sieves of every Bessel type, prime-only
majorants, and interval cancellation at moduli `≤ N/2`. A proof of
`θ > 3/4` would need at least one of the following:
* **Tuple counts of growing order.** The live form is the alternating
  hypothesis TC^alt_θ with `θ > 3/4` ((D)23; the literal TC_θ is
  obstructed above 2/3 by forced zeros). Bounded-order input cannot help
  ((D)21), and accuracy is needed at moduli `exp(c(log N)^{3θ/2})`, beyond
  any known theorem (Assessment).
* **Super-polynomial large-sieve levels.** H_LS∞ for forced families
  ((D)25, **CONJECTURE**). The band-family example proves that a cap must
  use the sparsity of forced families; abstract large-sieve axioms do not
  suffice.
* **Hybrid interval methods.** Capped if weak SPW holds ((D)26, PROVED
  implication). Weak SPW is open; the fixed-σ version is refuted.
  Right-signed mass at moduli in `(N, CN]` is also open.
* **Per-frequency weights below 1.** Weights `w ≥ 1` are capped (NONCRT
  Thm 2.3). Weights `< 1` are open, except a smooth-window case that is
  CONDITIONAL on an equidistribution conjecture.
* **Genuinely arithmetic, non-CRT input** of another kind.
* **Other ingredients outside the class:** majorants with `ν ≥ 0` only
  at primes `≤ N` when the period exceeds `N^c` (Assessment: open);
  composite Gallagher kernels with huge `Nh/(W_K−h)`; class types other
  than the four above; family primes beyond `N^{O(1)}`.

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
| Thm 4.3 | **sub-exponential rate:** `W(p) ≥ exp(c(log p)^{1/14})` | PROVED modulo Thorner–Zaman and Elsholtz–Tao Prop 1.4 | POINTWISE_OMEGA8 ((H)16) |
| Thm 2.2 | `W(p) ≥ exp(c(log p)^{1/7})` | PROVED modulo Gallagher's theorem (G) and Elsholtz–Tao Prop 1.4 | POINTWISE_OMEGA9 ((H)19) |
| Thm 3.2 | `W(p) ≥ exp(c(log p)^{1/6})` | PROVED modulo (G), Elsholtz–Tao Prop 1.4 and OMEGA10 Thm 3.4 | POINTWISE_OMEGA11 ((H)22) |
| Thm 6.3 | `W(p) ≥ exp(c(log p)^{1/5}(log log p)^{−1/5})` | PROVED modulo (G), Elsholtz–Tao and OMEGA10 Thm 3.4 | POINTWISE_OMEGA12 ((H)24) |
| Thm 5.1 | **current record:** `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})`; `log L_h(T) ≪ 𝓛⁴ log 𝓛` | PROVED modulo (G), Nair–Tenenbaum and OMEGA10 Thm 3.4 (Elsholtz–Tao no longer used) | POINTWISE_OMEGA13 ((H)26) |

Here `log_j` is the j-fold iterated logarithm. `L_h(T)` is the least hard
prime with `W > T`, and `𝓛 = log T`. Each row from OMEGA8 on supersedes
the one before; each was reviewed by two independent hostile reviewers
(OMEGA13 by four). OMEGA10 Thm 3.4 is the campaign's energy bound C-1
(below), itself PROVED and doubly reviewed. Gallagher's theorem (G) is
quoted from the Montgomery–Vaughan vol. III draft (Thm 28.19); his
original paper was not obtained.

**Method of the polylogarithmic rows (OMEGA–OMEGA4), in brief.**
* Impose the class of one at small primes, so the remaining congruence
  system is local at a few free primes.
* Build a pointwise minorant of the void indicator. It uses
  inclusion–exclusion truncated by *support size*, organised in levels.
  It also uses a conditional local lemma (Haeupler–Saha–Srinivasan), and
  heavy "hub" vertex sets are pushed down to lower levels by Markov steps.
* Transfer to primes with Thorner–Zaman's Linnik-range prime number
  theorem in progressions (Math. Z. 306 (2024), Cor. 1.4). Its error term
  absorbs a possible Siegel zero.

**From polylog to `exp((log p)^{1/4})` (OMEGA8–OMEGA13).**
* *Diagnosis* (Assessment). Alternating expansions (Brun, Bonferroni,
  levels) amplify errors on partial clusters; that caused the codegree
  thresholds and the `(k−1)!` loss. The local lemma works by suppression.
* *OMEGA8 (1/14).* Replace inclusion–exclusion by Bazzi's one-sided ℓ²
  sandwich (Razborov–Wigderson form), so the error is an ℓ² Fourier tail.
  Bound the tail by writing the bad indicator as a bounded-width DNF and
  applying Håstad's switching lemma (Linial–Mansour–Nisan).
* *OMEGA9 (1/7).* A linear transfer to primes: expand the minorant in
  characters and control all of them at once with Gallagher's prime
  number theorem summed over conductors. Only `E|B|` matters, not the
  ℓ¹ mass.
* *OMEGA10 (energy bound C-1).* For the indicator F that no event of a
  single-value event system occurs, on any product probability space:
  if `∏_{v∈E} λ_v ≤ 2` for every event E, then the weighted Efron–Stein
  energy `Σ_U ∏_{v∈U} λ_v ‖F^{=U}‖²` is at most 1 (Cor 3.5). For
  width-k DNFs this gives the sharp-rate tail `W^{>t} ≤ 4·2^{−(t+1)/k}`,
  independent of the number of terms (Cor 4.1). It replaces the bit
  encoding and the switching lemma. **PROVED** (two hostile reviews,
  exhaustive exact checks).
* *OMEGA11 (1/6).* Graded quarantine: quarantine a prime ℓ only to
  `n ≡ 1 (ℓ^{a_ℓ})`, raising `a_ℓ` while the fibre mass is too large.
* *OMEGA12 (1/5).* A modulus-weighted moment bound `Ω_0 ≪ 𝓛⁴ log 𝓛`
  (Thm 5.1, modulo Elsholtz–Tao) and a digit-filtration energy lemma.
* *OMEGA13 (1/4).* A β-weighted local lemma with a constant per-coordinate
  threshold; the event classes `−4D mod M` are Jacobi non-residues, so
  quarantining to random square classes never fires an event (the class
  of one is no longer needed); supermartingale bookkeeping; Nair–Tenenbaum
  for the masses. Elsholtz–Tao is no longer used.
* *Abstract transfer* (POINTWISE_TRANSFER.md, (H)23, PROVED modulo
  Gallagher, Landau–Page and Håstad). A prime `p ≡ a (Q)` avoiding any
  system of unit-class events on few free primes, with no single-value or
  codegree hypothesis. Applications: for every fixed `m ≥ 4` (Sierpiński's
  5/n included), the m/n witness modulus satisfies
  `W_m(p) ≥ exp(c_m(log p)^{1/7})` i.o. (also modulo Elsholtz–Tao Prop 1.4
  with κ = m). No novelty claim beyond these applications.

**The Haar exponent is exactly 3, and 1/4 is a ceiling.**
* *Haar side.* For the profinite avoider density `δ*(T)`,
  `𝓛³/log 𝓛 ≪ log(1/δ*(T)) ≪ 𝓛³(log 𝓛)^5`. Lower bound:
  POINTWISE_HAAR Thm 2.1, PROVED modulo the sieve fundamental lemma, via a
  new Janson-type inequality for product spaces with one-hot coordinates
  ((H)25). Upper bound: POINTWISE_OMEGA13 Thm 3.4, PROVED modulo
  Nair–Tenenbaum ((H)26). The Monte Carlo of POINTWISE_SIZE §7 fits this
  (EVIDENCE). So the profinite exponent is 3 up to logs, and the
  heuristic prime-side truth is `log W ≍ (log p)^{1/3}`.
* *Ceiling* (POINTWISE_OMEGA14, (H)27). Conditioned on the small
  coordinates, the problem is a sieve of dimension `κ ≍ 𝓛³` on the big
  primes, and the sieving limit forces level `≈ e^{𝓛κ}`. Thm 4.5
  (PROVED modulo Gallagher (G), the effective Page bound and the
  fundamental lemma): on any fibre, every minorant of level
  `log D ≤ c𝓛⁴/log 𝓛` has Haar mean `≤ 0`. Cor 4.6 (PROVED implication):
  1/4 is the ceiling, up to `(log log p)^{1/2}`, of every certificate
  that goes through a Haar minorant plus a transfer requiring
  `log x ≫ log Z`. The tool is a planting lemma (Lemma 1.1), which is LP
  duality for lower-bound sieves (no novelty claimed).
* *What 1/3 would need.* Prime input beyond low-conductor minorants:
  bilinear (Type II) or parity-sensitive information, or a transfer whose
  positivity comes from a Siegel-zero term. These are not covered by the
  ceiling.

**Consequences.**
* `H_MOD(A)` is **REFUTED for every A** (ledger (F)10, (H)13).
* So no pointwise multiplier mechanism whose witness moduli are
  `≤ exp((log p)^{1/4−ε})` can prove ES.

**Related results.**
* *Heuristic truth.* `log W ≍ (log p)^{1/3}` (**Assessment**,
  POINTWISE_SIZE §7), now backed by the Haar exponent 3 above. Data:
  `W ≈ (log p)^{2.5–3.4}` for `10^8 ≤ p ≤ 10^50` (EVIDENCE).
* *Superseded routes.* The earlier Haar bounds (POINTWISE_OMEGA2
  Thm 11.3, `≪ (log T)^7 log log T`) and the hub-codegree route of
  OMEGA4–OMEGA6 (hypotheses HC*, HC_Π, whose target was only
  `(log₂p)^{3/2}`) are superseded by the rows above. HC as literally
  stated in OMEGA4 is false (POINTWISE_OMEGA5). `POINTWISE_OMEGA7.md`
  (partial HC_Π reductions) was merged unreviewed and is archived.
* *Type-I slice parameter* (POINTWISE_OMEGA Thm 8.5, ledger (H)9).
  * `ck_min(p) ≫ log p · log₃p` infinitely often: PROVED modulo Lau–Wu
    Prop 5.1, not effective. This is Graham–Ringrose's 1990 Ω-bound for
    the least quadratic non-residue `n_p`, transported by a Yamamoto-type
    lemma. Only the equivalence "congruence methods certify exactly
    `n_p`" is campaign content.
* *Type-I map beyond Graham–Ringrose* (POINTWISE_TYPEI.md, (H)17). The
  target `ck_min ≥ g(p)·n_p` with `g → ∞` was **not** reached.
  * Vanishing of the Type-I count is a congruence sieve on `p` with
    moduli larger than `p` (Lemma 1.1). Every reduced hard class contains
    infinitely many `p` with `ck_min = n_p`, so congruence input gives
    exactly `g = 1` (Prop 4.2, PROVED).
  * `n_p = 5 ⟹ ck_min(p) ≤ 10`, sharp at `p = 193` (Thm 6.1, PROVED).
    Every finite Type-I covering of `{n_p = 7}` has height ≥ 539, and of
    `{n_p = 11}` height > 3000 (Cor 6.4, PROVED).
  * CONDITIONAL: under Schinzel H, `ck_min > g·n_p` i.o. for every `g`;
    under GRH, `ck_min > (1/(2log 2)−ε) log p·log log p` i.o. (Montgomery's
  Ω-result transported; sources cited from memory).
  * Census to `10^7`: record `ck_min(9033649) = 883` (EVIDENCE).
* *Write-ups.* `paper/es-omega-note.tex` v3 (every fixed exponent; 31 pp;
  internal referee, P1–P4 applied) and `paper/es-subexp-note.tex` v4
  (exponent 1/4, Haar exponent 3, the ceiling theorem; 39 pp; refereed
  internally four times, R33, R33b, R47, R56). `paper/energy-dnf-note.tex`
  (17 pp) writes up the energy bound C-1 and the DNF tails as a
  stand-alone result (refereed internally, R50 minor revision applied).

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

---

## 4. Table of main results

"Internal" reviews are by campaign agents. Nothing here is externally
refereed. "Cited" inputs are published theorems whose statements were
read but whose proofs were not re-checked. Standard tools (BV,
Brun–Titchmarsh, the large sieve) are listed only where the source names
them.

### 4.1 Exceptional-set line

| # | statement | label | document | review | external inputs |
|---|---|---|---|---|---|
| E1 | `E(N) ≪ N exp(−c L^{2/3}(log L)^{1/3})`, primes and all denominators | Theorem | `paper/vaughan-loglog-note.tex` Thms 1.1–1.2; notes §16.4–16.5 | `reviews/vaughan-loglog-note-review.md` (CORRECT-AFTER-REPAIRS) | BV, Brun–Titchmarsh, Montgomery large sieve |
| E2 | `E(N) ≪ N exp(−c L^{3/4})` | INTERNALLY PROVED (standalone note); CLAIMED/PROVISIONAL in `espaper.tex` | `paper/es-threequarter-note.tex` Thm 1.1; notes §§16, 34, 39, 76 | `reviews/es-threequarter-note-review.md`, `reviews/wave32-sec76-review.md` (SOUND-AFTER-REPAIRS); `reviews/es-threequarter-blind-audit.md` (SOUND) | BV (Cauchy–Schwarz against BV in §5) |
| E3 | Sieve-limit theorem for prime-slice systems; 3/4 cap for dominant-prime forced-class majorants; 2/3-loglog note sharp for its architecture | PROVED | `EXCEPTIONAL_THETA.md` Thm 2.5, 2.7, Lemma 2.9, Cor 3.4–3.6 | `reviews/exceptional-theta-review.md` (SOUND-AFTER-REPAIRS) | Case A via Elsholtz–Tao Prop 1.4 (Lemma 3.7) |
| E4 | Λ² sieve limit for arbitrary CRT systems via noise stability | PROVED (reduces balanced moduli to the open H_MS^{Sel}) | `EXCEPTIONAL_THETA.md` Thm 5.5 | as E3 | none |
| E5 | 3/4 cap for (η,B)-gapped ℛ(M)-families, unconditional | PROVED | `EXCEPTIONAL_TWIN.md` Thm 2.7, 4.4 | `reviews/exceptional-twin-review.md` (rounds 1–2) | none named |
| E6 | Two-prime Λ² cap `≪ L^{3/4}(log L)^{O(1)}`, twins included | PROVED (internal) | `EXCEPTIONAL_TWIN2.md` Thm 5.1 + `EXCEPTIONAL_TWIN3.md` Thm 4.1 | `reviews/exceptional-twin2-review.md`, `reviews/exceptional-twin3-review.md` (SOUND) | Brun–Titchmarsh |
| E7 | Λ² cap for `r` large primes, `≪ L^{3/4}(log L)^{3r+O(1)}`; B removed for fixed `r` | PROVED (internal) | `EXCEPTIONAL_TWIN4.md` Thm 7.1, 10.4 | `reviews/exceptional-twin4-review.md` (SOUND) | arithmetic large sieve (rough-partner Brun–Titchmarsh) |
| E8 | 3/4 cap for every CRT majorant over ℛ(M)-families with fixed B; weighted k-ary comparison theorem | PROVED (internal) | `EXCEPTIONAL_KARY.md` Thm 2.5, 4.5 | `reviews/exceptional-kary-review.md`, `-review-2.md` | none |
| E9 | Per-frequency signed rounding (weights ≥ 1), prime-only majorants and CRT moment methods also capped at 3/4 (prime-slice families) | PROVED (internal) | `EXCEPTIONAL_NONCRT.md` Thm 2.3, 3.2–3.3, Props 4.1–4.2 | `reviews/exceptional-noncrt-review.md` (rounds 1–2) | none |
| E10 | **No θ > 3/4 for coefficient-sum CRT sieves over any mixture of the four forced/selector class types**; saving `≤ C L^{3/4}(log L)^{3/4}`, `≪_B L^{3/4}` under fixed B | PROVED (internal) | `EXCEPTIONAL_KARY2.md` Thm 5.1, 5.2, Cor 6.1; `paper/sieve-limits-note.tex` | `reviews/exceptional-kary2-review.md`, `-review-2.md`; `reviews/sieve-limits-note-review-v2.md`, `reviews/papers-v3-review.md` | Elsholtz–Tao Prop 1.4 (Case-A part only) |
| E11 | Heuristic ceiling `θ = B/(B+1)` (2/3 at B = 2, 3/4 at B = 3) | Assessment (proved arithmetic under the stated assembly model) | notes §18.3–18.4 | — | — |
| E12 | Large sieve capped: every CRT-admissible large-sieve bound is `≥ N·E\|g*\|²` (Selberg-square majorant), so saves `≤ C L^{3/4}(log L)^{3/4}` (polynomial denominators), `C_B L^{3/4}` (bounded B); includes the 2/3 note's use | PROVED, conditional on KARY2 Thm 5.1 | `EXCEPTIONAL_LARGESIEVE.md` Thm 2.1, 3.1, Cor 3.2, Thm 4.1, 6.2 | `reviews/exceptional-largesieve-review.md` (SOUND) | KARY2 Thm 5.1 (hence Elsholtz–Tao Prop 1.4 for Case A) |
| E13 | Selberg minorant `Σ_{n≤N}ν ≥ (N−D)Eν`; majorants from forced classes of modulus `≤ N/2` save `≤ C L^{3/4}(log L)^{3/4}` under any evaluation of the interval sum | PROVED (internal) | `EXCEPTIONAL_INTERFREQ.md` Thm 2.2, Cor 2.3, Thm 2.5 | `reviews/exceptional-interfreq-review.md` | KARY2 Thm 5.1 |
| E14 | TC_θ ⇒ `E(N) ≤ (e+2)N exp(−(2/e²)L^θ)`; TC holds for `K ≤ cL^{2/3}`, fails for even `K ≥ (e²/2+ε)L`; bounded-order correlations cannot give θ > 3/4 | PROVED (internal); TC_θ for 3/4 < θ < 1 is a CONJECTURE | `EXCEPTIONAL_TUPLES.md` Cor 2.3, Prop 2.4, Thm 3.1, Prop 4.2 | `reviews/exceptional-tuples-review.md` (all items SOUND) | KARY2 Thm 5.1 (Cor 3.4) |

### 4.2 Pointwise line

| # | statement | label | document | review | external inputs |
|---|---|---|---|---|---|
| P1 | Refactor graph, seed, hub bridge, fibre counts (the character dichotomy itself is Bright–Loughran) | PROVED (elementary) | `SIGNED_REFACTOR.md`, `POINTWISE.md` | `reviews/wave34-hostile-review.md` | Bright–Loughran 2020 (known parts) |
| P2 | Exact classification of seed escapes of length ≤ 3 | PROVED | `DEPTH3.md` Thm 1 | `reviews/wave34-hostile-review.md` | none |
| P3 | Seed distance unbounded | CONDITIONAL on H | `DEPTH3.md` Thm 2 | `reviews/wave34-hostile-review.md` | Hypothesis H (Bateman–Horn for counts) |
| P4 | Non-Mordell primes have distance 2; `#{dist>2} ≪ N/(log N)^{11/2}`, `#{dist>5} ≪ N/(log N)^{10}` | PROVED modulo a standard sieve theorem (Corollary PROVED outright) | `DEPTH3.md` Thm 3, Lemmas 4–5, Corollary | `reviews/wave34-hostile-review.md` | Dahan's half-dimension lemma; upper-bound sieve |
| P5 | Every `p ≡ 1 (4)` below `10^12` has seed distance ≤ 3 | EVIDENCE | `DEPTH3.md` §5 | — | — |
| P6 | **Theorem F:** the seed component is sterile for infinitely many `p = 24q+1` | CONDITIONAL on H + CERTIFIED | `FORMAL_CLOSURE.md`; `data/formal_closure/` | `reviews/formal-closure-review.md` (independent engine) | Hypothesis H for 6402 polynomials |
| P7 | Sterile components larger than the seed component | CERTIFIED / PROVED (Lemmas A–E) | `SIZE_CONJECTURE.md` | `reviews/wave34-hostile-review.md` | none |
| P8 | Parity/windmill lemmas; large p-free buckets are singletons (Thm 7) | PROVED (lemmas) / EVIDENCE (scans) | `WINDMILL.md` | `reviews/wave34-hostile-review.md` | none |
| P9 | Theorem M (transfer principle), Corollary M1 | PROVED; existence of admissible q CONDITIONAL | `POINTWISE_SIZE.md` §1 | `reviews/pointwise-size-step1-review.md` | H / Dickson / Dirichlet–Linnik, depending on the family |
| P10 | Lemma CT (character trap) | PROVED | `POINTWISE_SIZE.md` §2 | as P9 | none |
| P11 | Theorem C (formal odd-square principle) | CONDITIONAL on H | `POINTWISE_SIZE.md` §2 | as P9 | Hypothesis H |
| P12 | Proposition A (size comparisons are inside the obstruction) | PROVED | `POINTWISE_SIZE.md` §4 | as P9 | none |
| P13 | `W(m²) = +∞` for every integer `m` | PROVED | notes §58.1, Thm 58.1 | SOUND-AFTER-REPAIRS (wave 22) | none |
| P14 | `W(p) ≥ c log p` i.o. | PROVED, effective | notes §54, Thm 54.1 | CONFIRMED (PROJECT.md Outcome 24) | Xylouris' Linnik exponent |
| P15 | `limsup W(p)/log p ≥ 5/8`; `limsup ck_min/log p ≥ 5/12` | PROVED modulo the cited theorem | `POINTWISE_SIZE.md` Thms 11.2, 11.2' | as P9 | Chang 2014 Cor. 11 |
| P16 | `W(p) ≥ (log p)^{2−o(1)}` i.o. | PROVED modulo the cited theorem, effective | `POINTWISE_OMEGA.md` Thm 5.1 | `reviews/pointwise-omega-review.md` | Thorner–Zaman 2024 Cor. 1.4 |
| P17 | `ck_min(p) ≫ log p · log₃p` i.o. | PROVED modulo the cited theorem; not effective; Graham–Ringrose transported | `POINTWISE_OMEGA.md` Thm 8.5 | `reviews/pointwise-omega-review.md` | Lau–Wu Prop 5.1 (Graham–Ringrose 1990) |
| P18 | `W(p) ≥ (log p)^{3−o(1)}` i.o.; H_MIN(θ) for θ > 1/3 | PROVED modulo the cited theorem, effective | `POINTWISE_OMEGA2.md` Thm 5.1, Cor 5.2 | `reviews/pointwise-omega2-review.md` | Thorner–Zaman; Haeupler–Saha–Srinivasan (conditional LLL) |
| P19 | Haar side: `log(1/δ*(T)) ≤ T^{o(1)}`, and `≪ (log T)^7 log log T` | PROVED; second form modulo the cited theorem | `POINTWISE_OMEGA2.md` Thm 11.3 | `reviews/pointwise-omega2-review-r3.md` | Elsholtz–Tao Prop 1.4 (second form) |
| P20 | **Every fixed exponent:** `W(p) ≥ (log p)^{k−o(1)}` i.o., every fixed `k` | PROVED modulo the cited theorem, effective | `POINTWISE_OMEGA3.md` Thms 4.3, 5.2 | `reviews/pointwise-omega3-review.md`, `-review-2.md` (SOUND) | Thorner–Zaman |
| P21 | Explicit rate `log W ≥ (1+o(1)) log₂p·log₃p/log₄p` i.o. | PROVED modulo the cited theorems | `POINTWISE_OMEGA4.md` Cor 3.1–3.3 | `reviews/pointwise-omega4-review.md` | Thorner–Zaman; Elsholtz–Tao Prop 1.4 (dropping it gives `log₂p·log₄p/log₅p`) |
| P22 | HC* ⇒ `log W ≥ 0.2√a (log₂p)^{3/2}`; `m = 1` part of HC* | PROVED implication; `m = 1` part PROVED; HC_Π open; literal HC false | `POINTWISE_OMEGA4.md` Thm 4.2; `POINTWISE_OMEGA5.md` Thm 2.3 | `reviews/pointwise-omega4-review.md`, `reviews/pointwise-omega5-review.md` | Thorner–Zaman, Elsholtz–Tao |
| P23 | `ES(p) ⇔ a_min(p) < ∞`; window reciprocity | PROVED | `POINTWISE_SIZE.md` Thm 8.1, Lemma 8.2 | as P9 | none |
| P24 | W1: `a_min ≥ 7` for `≫ x/(log x)^{3/2}` hard `p` | PROVED modulo cited sieve theorems | `POINTWISE_WINDOW.md` §2 | `reviews/pointwise-window-review.md` | semi-linear sieve, Selberg sieve, BV (also FHRSS 2025) |
| P25 | W2: `a_min ≥ 11` for `≫ x/(log x)²` hard `p` | CONDITIONAL on Elliott–Halberstam | `POINTWISE_WINDOW.md` §4 | `reviews/pointwise-window-review.md` | EH (level `x^{1−ε₀}`) |
| P26 | `log W ≍ (log p)^{1/3}`; `a_min ≍ log p/log log p` | Assessment | `POINTWISE_SIZE.md` §7, §8 | — | — |

---

## 5. Novelty and attribution (from `reviews/novelty-audit-2026-10.md`)

The audit is a priority search, not a proof check. "New" means **no prior
source was found in what was searched**. It is not a certificate of
priority. The search was limited: the Jina search API failed, and
Semantic Scholar was rate-limited. These were **not accessed**:
* Selberg's sieve lectures and *Opera de Cribro*;
* Prékopa 1988/1990 and Mádi-Nagy–Prékopa 2004;
* Linial–Nisan and Kahn–Linial–Samorodnitsky;
* Graham–Ringrose 1990;
* Schinzel 2000 and Yamamoto 1965;
* Vaughan's 1970 primary text.

**Known; must be cited, not claimed:**
* *LP duality for sieve majorants.* A level-λ majorant sieve is dual to
  the largest avoider mass under laws matching the level-λ marginals. This
  is standard: Tao, 254A Notes 4, Thm 5; Benjamini–Gurel-Gurevich–Peled
  (BGP) Prop. 4.
* *The exchangeable single-band core of the sieve-limit theorem.* It is
  **known in sharper form**: Peled–Yadin–Yehudayoff (RSA 2011) Thm 1.1 and
  BGP Thm 23, building on Prékopa 1988. In the binomial model the k-wise LP
  optimum is within `e^{O(k)}` of the Selberg value. The campaign's ET §2.5
  "Selberg is near-optimal" EVIDENCE is a theorem there; EVIDENCE remains
  only for the Poisson model and the multi-band case. KARY Lemma 2.3
  (binomial extrapolation) is `M(n,d,t) ≥ 1/B` in BGP/PYY notation. PYY is
  sharper for `d ≤ c·nt`; KARY's crude bound covers all ranges.
* *The signed character dichotomy and finiteness* (Bright–Loughran 2020;
  Yamamoto 1965 for one direction).
* *Notes Thms 5.1 and 17.3* ("finite congruence-identity coverings cannot
  settle ES"). These are known in substance: Mordell 1969 and Schinzel
  2000 as quoted in Elsholtz–Tao p. 8, and the Elsholtz–Tao remark on p. 6.

**Transport of a known bound:**
* `ck_min(p) ≫ log p · log₃p` is Graham–Ringrose's 1990 bound
  `n_p = Ω(log p · log₃p)` carried over by a Yamamoto-type lemma (as
  stated in Lau–Wu). Cite Graham–Ringrose as the primary source. Only the
  equivalence "congruence methods certify exactly `n_p`" (POINTWISE_OMEGA
  Prop 8.3, Cor 8.4) is campaign content.

**Partial:**
* *Theorem C.* It generalises, to procedures and conditionally on H, the
  known odd-square obstructions: Elsholtz–Tao Prop 1.6 and its p. 6
  remark, Mordell–Schinzel, and Bright–Loughran Cor 1.3–1.4. Its
  unconditional instances are known.
* *Theorem M.* It formalises the standard generic-point / Hypothesis-H
  principle. No procedure-level statement was found, but the principle is
  folklore.
* *DEPTH3 Thm 2 and Theorem F* are instances of the same principle.
  Theorem F was obtained first, and in stronger form, by the sibling
  project astra (Dickson for 159 linear forms). The campaign's paper
  reports that result without re-proving it; the authorship and citation
  form are still undecided.

**Apparently new (no prior source found):**
* *The 3/4 bound* and the 2/3-loglog bound. As of 2026-10-04, no
  improvement of Vaughan's 2/3 (or of its loglog factor) was found. Vaughan
  is still cited as the record by Elsholtz–Tao, Pomerance–Weingartner and
  erdosproblems #242. The cubic average solution count of Elsholtz–Tao
  Thm 1.1 is at the same scale but is a different statistic.
* *The weighted lower-set (multi-band) sieve-limit form* with arbitrary
  densities, the Rankin-functional cap, and the sequential-law comparison
  (KARY Thm 2.5). One check is still open and needs library access:
  whether Mádi-Nagy–Prékopa 2004 contains the multivariate lower-set
  version.
* *The ES caps* (3/4 sharp for forced-class CRT sieves). No ES source
  discusses the limits of sieve majorants.
* *The `W(p)` Ω-results*, including the explicit rate. No Ω-result for any
  least ES witness parameter was found. The method follows the classical
  CRT-plus-least-prime pattern (Fridlender, Salié, Chowla–Turán). The
  technical novelty is the multilevel minorant and local-lemma machinery.
  The interest of the result depends on `W` being a natural statistic; it
  is campaign-defined.
* *The signed refactor graph and seed-component conjecture.* These are
  elementary; their value is structural, not a priority claim.

**Other attribution notes:**
* Theorem W1 is also implied by Fuchs–Hsu–Rickards–Schindler–Stange 2025
  Thm 1.1(2).
* Theorem W2 is a Friedlander–Iwaniec (2009) type theorem.
* Related recent work that the campaign compares against:
  Pomerance–Weingartner (arXiv:2511.16817; an explicit-in-`m` Vaughan
  bound) and Dahan (arXiv:2608.24035). Dahan's Thm 4.17 is credited as an
  independent antecedent of the cubic exponent shape, for a different,
  ineffective statistic.

---

## 6. Open problems, ranked

Importance (I) and feasibility (F) are rated high / medium / low. These
ratings are this summary's judgement, not ledger labels.

1. **External refereeing of the 3/4 note and the 2/3-loglog note.**
   (I high, F high.) Both are unrefereed; the 3/4 label is only
   INTERNALLY PROVED. `paper/README.md` recommends showing the loglog note
   to a human referee first. Related tasks: read Vaughan 1970 itself and
   complete the priority search.
2. **θ > 3/4 for `E(N)`.** (I high, F low.) Every coefficient-sum CRT
   sieve over the four class types is capped (§2.2). So are the large
   sieve and, for moduli `≤ N/2`, interval cancellation (§2.3). A new
   ingredient is required (§2.4). The most concrete candidate is TC_θ for
   `θ > 3/4`: CRT-accurate witness correlations of order `≍ (log N)^θ`.
   It is a CONJECTURE; its proved implication is (D)21. Other candidates:
   per-frequency weights below 1, the large-sieve escapes (H_LS), and
   other non-CRT arithmetic input.
3. **A pointwise route via (E1) or (E2).** (I very high, F low.) The
   natural target is X_win(C), i.e. `a_min(p) ≪ log p` (§3.4). It sits
   just above the formal-obstruction scale. Lemma 9.1 (PROVED) gives
   ES ⇐ X_QNR (least-non-residue seeding), an (E2)-type reduction. Whether
   fixed non-abelian Frobenius data (E3) escapes the obstruction is open.
4. **Unconditional `a_min(p) → ∞` (or even `a_min ≥ 11`).** (I medium,
   F low–medium.) This is the window analogue of the open unconditional
   case of Friedlander–Iwaniec 2009. It needs a level of distribution close
   to 1 or a bilinear, parity-breaking input.
5. **Sharper `W(p)` rates.** (I medium, F medium.) Prove HC_Π (a
   divisor-function problem in short progressions). By POINTWISE_OMEGA5,
   this gives HC*, and hence `log W ≥ c(log₂p)^{3/2}` via OMEGA4 Thm 4.2.
   Beyond that: an event-sensitive truncation (Assessment: up to
   `(log₂p)²/log₃p`). `exp((log p)^c)` is outside the method. The
   heuristic truth is `log W ≍ (log p)^{1/3}`.
6. **An unconditional sterile seed component.** (I low–medium, F low.)
   Astra has reduced its hypothesis to 158 prime conditions plus one
   divisor condition; searches over actual inputs find no sterile prime.
   Note: settling this would not affect ES.
7. **Removing `(log log N)^{3/4}` from the general cap** (KARY2 Thm 5.1),
   and closing the Λ² middle window `r ≍ log L` (TWIN4 §12). (I low,
   F medium.) Neither would change the exponent 3/4.
8. **Open hypotheses kept in the ledger** (section (E)): `H_kBV(κ)`,
   `H_FAIL`, `H_STACK`, `H_BLK`/`H'_BLK`, `H^+_LT` and `H_PF'`. Also open:
   the replacement conjecture `C'_SQ` (`W = +∞` exactly for squares and
   three sporadic values; ledger (F)9) and `C_POLY`. (I low–medium,
   F varies.) Most of these belong to the a-frame/stacking route, whose
   model ceiling is below 3/4.
9. **Novelty checks that need library access.** (I medium for
   publication, F high with access.) Mádi-Nagy–Prékopa 2004, Selberg's
   large-κ remarks, *Opera de Cribro* Ch. 7 and 11, Graham–Ringrose 1990,
   Vaughan 1970.
10. **Administrative.** Settle authorship and the citation form for astra
    before `paper/pointwise-obstruction.tex` is finalised.

---

## 7. Reading guide

| if you want… | read |
|---|---|
| the current status and house rules | `STATUS.md` |
| every claim with its exact label | `DISCOVERIES.md` |
| the original project brief and outcome log | `PROJECT.md` (Outcome 36 for the hard targets) |
| the full research notebook (§§1–77) | `notes.md`; machine checks in `verify.py` |
| the 2/3-loglog bound, self-contained (9 pp) | `paper/vaughan-loglog-note.tex` |
| the 3/4 bound, self-contained | `paper/es-threequarter-note.tex`; blind audit `reviews/es-threequarter-blind-audit.md` |
| everything up to wave 31 in one draft (177 pp; provisional labels) | `paper/espaper.tex` |
| why 3/4 is sharp for congruence sieves | `paper/sieve-limits-note.tex`; then `EXCEPTIONAL_KARY2.md` and `EXCEPTIONAL_KARY.md` |
| the sieve-limit theorem and the Rankin functional | `EXCEPTIONAL_THETA.md` §§0–3 |
| the Λ² route with twin and r-prime moduli | `EXCEPTIONAL_TWIN.md` → `TWIN2` → `TWIN3` → `TWIN4` |
| non-CRT inputs, rounding, prime-only majorants | `EXCEPTIONAL_NONCRT.md` |
| the large sieve over forced-class mixtures | `EXCEPTIONAL_LARGESIEVE.md` |
| inter-frequency cancellation in interval counts | `EXCEPTIONAL_INTERFREQ.md` |
| the tuple-count door TC_θ and witness correlations | `EXCEPTIONAL_TUPLES.md` |
| the signed graph, basics | `SIGNED_REFACTOR.md`, `POINTWISE.md` |
| short escapes and exceptional sets for the seed distance | `DEPTH3.md` |
| Theorem F and its certificate | `FORMAL_CLOSURE.md`, `data/formal_closure/`, `scripts/formal2_verify.py` |
| the pointwise programme's obstruction, written up | `paper/pointwise-obstruction.tex` |
| the meta-theorem (Theorems M, C, Proposition A) and the window frame | `POINTWISE_SIZE.md` §§0–4, §8 |
| `W(p)` Ω-results | `paper/es-omega-note.tex`; then `POINTWISE_OMEGA.md` → `OMEGA2` → `OMEGA3` |
| the explicit rate and its bottleneck | `POINTWISE_OMEGA4.md`, `POINTWISE_OMEGA5.md` |
| window Ω-results (`a_min`) | `POINTWISE_WINDOW.md` |
| what is known in the literature, and claimed proofs | `LITERATURE_2026.md` |
| priority and attribution | `reviews/novelty-audit-2026-10.md`, `reviews/lit-audit-*.md` |
| what each review found | `reviews/` (file names in §4 above) |
| per-task agent reports | `reviews/agent-reports/`, `UNIT_REPORT*.md` |
| the companion signed-seed counterexample | `../erdos-straus-astra` (read-only): `SIGNED_SEED_COUNTEREXAMPLE.md`, `PRIMARY_SEED_PACKET.md` |

Suggested order for a newcomer:
1. §1 of this file.
2. `STATUS.md`.
3. The abstracts of the five papers in `paper/`.
4. `DISCOVERIES.md` sections (D) and (H).
5. Whichever line interests you, via the table above.
