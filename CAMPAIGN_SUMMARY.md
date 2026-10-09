# Erdős–Straus campaign: summary of the state of the art (refreshed 2026-10-09 to main after ledger (D)31 and (H)34, incl. the follow-ups (D)31 [EXCEPTIONAL_MN2], (H)17 follow-ups 4-5 [TYPEI5, TYPEI6], (H)34 follow-ups [MORDELL13B, MORDELL13C, MORDELL17B, MORDELL17C] and the refutation (F)11 [MORDELL13B])

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
priority search through 2026-10-04 (`reviews/novelty-audit-2026-10.md`)
and a second, offline audit of the later rounds (2026-10-05,
`reviews/novelty-audit-2026-10b.md`).
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
  `≤ N/2`; then to large sieves at **every** frequency level, first for
  mixtures with at most one prime factor above `exp((log N)^{1/4})` per
  modulus ((D)27), then for every mixture whose multi-rough classes are
  residue-sparse, including all small-height classes such as −4 mod M
  ((D)28). The cubic witness tail is now INTERNALLY PROVED ((A)9). The
  remaining doors above 3/4 are precisely stated: the repaired
  tuple-count hypothesis TC^alt_θ (a CONJECTURE); the all-level large
  sieve for residue-dense multi-rough classes, reduced to a sup-decay
  hypothesis (A*) and further to a residue-dispersion statement (RD′)
  (open; (RD) is proved at one prime for ℛ(M) and false as first stated
  for several primes); the combinatorial statement "weak SPW" for hybrid
  methods (open; the fixed-σ version and fixed-η RSPW are refuted);
  per-frequency weights below 1, reduced to one shift-uniform avoider
  count (W_𝔊) ((D)29; open — neither proved nor refuted, and the
  CRT-alignment plan for it provably fails, EXCEPTIONAL_WEIGHTS2); and
  genuinely non-CRT arithmetic input. The 3/4 bound also holds in every
  interval of length H at any position, `E(I) ≪ H exp(−c(log H)^{3/4})`,
  and in progressions of small or rough modulus ((D)30, PROVED relative
  to the 3/4 note; modest novelty). For m/n the same argument gives
  `E_m(N) ≤ C N exp(−c(log N)^{3/4} m^{−1/4})` uniformly in m ≥ 4
  ((D)31, PROVED relative to the 3/4 note).
* **Pointwise line.** It tried to prove ES prime by prime through a
  signed solution graph. That line is **closed**: under standard prime
  hypotheses, the programme cannot work. The closure grew into a
  meta-theorem about procedures. It also produced unconditional
  Ω-results for the least multiplier witness `W(p)`. The rate went from
  every fixed power of `log p` to
  `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` for infinitely many
  hard primes (PROVED modulo Gallagher's theorem and Nair–Tenenbaum).
  The profinite (Haar) exponent is exactly 3 up to logs (lower bound
  `≫𝓛³` with no log loss), and 3 is also the true tail exponent of `W`
  over primes: `log(π(x)/#{p≤x: W(p)>T}) ≍ (log T)³` up to
  `(log log T)³` in a range of T ((H)33). So the heuristic truth is
  `log W ≍ (log p)^{1/3}`. Exponent 1/4 is proved to be the ceiling of
  the Haar-minorant architecture (up to `(log log p)^{1/4}`), and a
  Wiener-norm barrier extends it to all full-orbit uniform linear
  certificates, for which prime input such as GRH or EH is irrelevant.
  The one hypothesis known to give 1/3 is the CONJECTURE LS ("Linnik for
  sifted sets"). Support-aware certificates are the open door; their
  ceiling is reduced to a CONJECTURE SAP. The m/n analogues reach 1/4
  for m ≡ 0 (4) and 1/5 for every m; for m ≢ 0 (4) the missing input SI
  is not proved, and its failure is localised ((H)32). Window results give
  exact orders for bounded windows and show that parity input is
  necessary. Finite coverings: every Type-I covering of `{n_p = 7}` has
  height > 1.32·10¹² (CERTIFIED); no certificate at the sign point `x̂_9`
  exists with 2-adic level ≤ 22 and `v_7(k) ≤ 3` at **any** height
  (CERTIFIED, via a Pell form of fibre certificates, PROVED); ES holds for primes with `(p/13) = −1`
  outside six classes mod 720720 (PROVED by finite computation). The
  first candidate sterile point x* for r = 13 turned out to lie in an
  explicit class of modulus 12670944 (its conjecture is REFUTED, (F)11).
  The remaining candidates, `x̂_9` for Type I, x** = x(2,15) for r = 13,
  and a point on the 17-generic line for r = 17, are CONJECTURES
  ((H)17, (H)34). No sterile point other than the square points is proved.

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
* The cubic witness tail (ledger (A)9),
  `#{p≤x: W(p)>T} ≪ π(x)exp(−c(log T)³)` for `log T ≤ c₁(log x)^{1/4}`,
  is now **INTERNALLY PROVED** (2026-10-06): it follows from the 3/4
  note's atoms (`CEILINGS_UNIFIED.md` Thm 2.1, review SOUND; constants not
  effective; the small-T range cites the uniform PNT in progressions with
  the Landau–Page term from memory). It was CLAIMED/PROVISIONAL as notes
  Thm 51.2(2). Together with (H)33 it is two-sided (§3.3).

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
R36, MINOR REVISION, fixes applied; v5, 73 pp., adds smooth–rough
splitting and the residue-sparse all-level cap ((D)27–(D)28), the SPW
updates ((D)26) and the unified sieve-limit picture of §3.3, refereed
internally in R65, accept after minor revision, D1–D9 applied). The 3/4 note
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
    `Nh/(W_K−h)` and small prime factors. (H_LS∞ is now proved for two
    large subclasses of mixtures; next two items.)
* **Large sieves at every frequency level, one rough prime per modulus**
  (`EXCEPTIONAL_LARGESIEVE3.md`; ledger (D)27).
  * *Smooth–rough splitting (Thm 1.1, PROVED, elementary).* Any large
    sieve is capped by `β log N + log ρ + log E_{c∼π_s}𝓡_{2+2β}(π_c)`;
    the z-smooth coordinates cost only a density factor ρ, affordable up
    to `z = exp((log N)^{1/4})` (Lemma 2.1).
  * *Cap (Thm 3.1, PROVED given the reviewed KARY2 inputs and ET Prop 1.4
    for Case A).* For every forced mixture in which each modulus has at
    most one prime factor above `exp((log N)^{1/4})` (any modulus size,
    no B), every CRT-admissible large sieve — any rational frequencies,
    any level — saves `≤ C(log N)^{3/4}(log log N)^3`. This closes
    H_LS∞ for such families.
  * *Residual.* Classes with ≥ 2 rough primes need a correlation-decay
    statement (H_rough) (sufficient only). The symmetric local-lemma
    route fails because −4 mod M lies in ℛ(M) for every M ≡ 3 (4)
    (Lemma 4.2; "route fails" is an Assessment).
  * *Label:* **PROVED as labelled** (review
    `reviews/exceptional-largesieve3-review.md`, SOUND; two overclaims
    repaired).
* **(H_rough) reduced; the all-level cap for residue-sparse mixtures**
  (`EXCEPTIONAL_LARGESIEVE4.md` with follow-ups LS5–LS7; ledger (D)28).
  * *Damped collisions (Lemma 1.1).* Fourier decay turns the Rényi-type
    quantity of (D)27 into a positive two-copy collision quantity. Thm 4.2
    (PROVED implication): the all-level 3/4 cap for **all** forced
    mixtures follows from a sup-decay hypothesis (A*) of the conditioned
    fibre laws.
  * *Cap (Thm 5.2, Cor 5.3, PROVED with LS3's inputs).* The 3/4 cap at
    every frequency level holds for every mixture whose multi-rough
    classes are residue-sparse, in particular for all small-height
    classes −r/s (incl. −4, −1, −1/4 mod M) over all moduli. So residue
    concentration is the easy case.
  * *Follow-ups (LS5–LS7, each reviewed with repairs).* (A*) is **not**
    proved. LS5: every forced class is a rational label −r/s mod G, and
    a tilted fibre law satisfies (A*). LS6: (A*) follows from a
    first-moment damped covering count (DCC) (PROVED implication), with
    one isolated arithmetic input, residue dispersion (RD) (CONJECTURE).
    LS7: ℛ(M) = {−u/v : gcd(u,v)=1, 4uv | M+1}; (RD) holds at one prime
    for ℛ(M) classes (Thm 3.1, PROVED given Shiu/Nair–Tenenbaum) and for
    long cofactors (Thm 4.3); but (RD) as stated is **false** for several
    primes (Prop 4.1), its height-cut form fails with (a,D) classes, and
    the correct target is a residue-cut form (RD′). Short cofactors and
    the (a,D)/Case-A classes are open.
  * *Label:* **PROVED as labelled** (reviews
    `reviews/exceptional-largesieve4-review.md` … `-largesieve7-review.md`).
    *Open:* (A*) / (DCC) / (RD′) for residue-dense multi-rough classes
    (generic ℛ(M)); the covering count (CC) is a CONJECTURE.
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
  * *Exact requirement* (`EXCEPTIONAL_SPW2.md` Lemma 1.1): the hybrid
    saving is `≤ C′(log N)^{3/4} + log(K_N/η_N) + log(1+Δ′_N/K_N) + O(1)`,
    so the 3/4 cap needs `log(K/η) = O((log N)^{3/4})`; polynomially
    small margins give nothing. A K-free edge bound `η ≲_C (log N)^{−1/3}`
    (Thm 3.1) refutes the relaxation RSPW with fixed η, but only
    logarithmically. No `N^{−1/2}` decay for N ≤ 80 (EVIDENCE only).
  * *Label:* **PROVED / PROVED implication as labelled** (internal;
    reviews `reviews/exceptional-interfreq2-review.md`,
    `reviews/exceptional-spw-review.md`, SOUND;
    `reviews/exceptional-spw2-review.md`). No hybrid beating 3/4 was
    found.
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

The sources are ledger (D)18–(D)29, KARY2 §6, NONCRT §6, WEIGHTS, WEIGHTS2 and STATUS.md.
The cap is now exactly `(log N)^{3/4}` (no `log log` loss, (D)24) for
coefficient-sum sieves, large sieves of every Bessel type (at every
frequency level for one-rough-prime and residue-sparse mixtures), prime-only
majorants, and interval cancellation at moduli `≤ N/2`. A proof of
`θ > 3/4` would need at least one of the following:
* **Tuple counts of growing order.** The live form is the alternating
  hypothesis TC^alt_θ with `θ > 3/4` ((D)23; the literal TC_θ is
  obstructed above 2/3 by forced zeros). Bounded-order input cannot help
  ((D)21), and accuracy is needed at moduli `exp(c(log N)^{3θ/2})`, beyond
  any known theorem (Assessment).
* **Large sieves at super-polynomial levels, residue-dense classes only.**
  H_LS∞ for forced families ((D)25, **CONJECTURE**) is now proved for
  mixtures with one rough prime per modulus ((D)27) and for residue-sparse
  multi-rough classes ((D)28). What is left is (A*) for residue-dense
  multi-rough classes (generic ℛ(M)), reduced via (DCC) to the
  residue-cut dispersion statement (RD′) (open; (RD) proved at one prime
  for ℛ(M), false as first stated for several primes). The band-family
  example proves that a cap must use the sparsity of forced families.
* **Hybrid interval methods.** Capped if weak SPW holds ((D)26, PROVED
  implication), with the exact requirement `log(K/η) = O((log N)^{3/4})`
  (SPW2). Weak SPW is open; the fixed-σ SPW and fixed-η RSPW versions are
  refuted. Right-signed mass at moduli in `(N, CN]` is also open.
* **Per-frequency weights below 1.** Weights `w ≥ 1` are capped (NONCRT
  Thm 2.3). For weights `< 1`, `EXCEPTIONAL_WEIGHTS.md` ((D)29) proves
  that every per-frequency bound is at least the shift-uniform avoider
  count `M_𝔊(N) = max_t #(𝒜 ∩ (t, t+N])` (Lemmas 1.1–1.2, PROVED), and,
  for Selberg's band-limited window, at most `12(K+1)M_𝔊(N)` (Thm 2.1,
  PROVED). So this door is capped at 3/4 **iff** (W_𝔊)
  `M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}` holds, uniformly over the families a
  method may use (Cor 2.2). (W_𝔊) is open; that no arithmetic-free
  argument decides it is an Assessment. Sharp weights with hit-pattern
  majorants, `Q₀ = 1`, small prime slices (`|F_ℓ| ≤ ℓ^γ`, γ < 1/3) and the
  uniform mass hypothesis (M) are capped without (H_eq) (Thm 3.3, PROVED);
  (H_eq) itself is proved at one large prime for smooth windows and is a
  CONJECTURE for several primes. Review
  `reviews/exceptional-weights-review.md` (no FATAL; one MAJOR repaired).
  Follow-up `EXCEPTIONAL_WEIGHTS2.md` (review
  `reviews/exceptional-weights2-review.md`: no FATAL; 3 MAJOR and minors
  repaired by the author): (W) is **neither proved nor refuted**, and the
  CRT-alignment plan provably fails. One maximal family suffices (Lemma 1.1).
  For prime slices only subfamilies of period ≤ N are forced to pay their
  density in every window, and that forced mass is `(log N)^{o(1)}`
  (Lemmas 2.1–2.2; composite case partly open). Prime slices `ℓ ≤ Y` push the
  avoider density below `exp(−c(log Y)²)` (Prop 3.1, PROVED, ineffective via
  Bombieri–Vinogradov), but windows need not pay it. Random shifts lose
  `e^{−c(log N)²}` (Prop 4.1), so a proof of (W) must align almost all medium
  primes jointly; all ℛ(ℓ) classes are quadratic non-residues, so quadratic
  alignment caps at `√(N log N)` (Prop 5.3). For prime slices (W) is an
  attainment question for a growing-dimension large sieve of Hensley–Richards
  type (Lemma 5.1, Prop 5.2). A refutation of (W) would not by itself give
  θ > 3/4 (R90 D1/D2).
* **Genuinely arithmetic, non-CRT input** of another kind.
* **Other ingredients outside the class:** majorants with `ν ≥ 0` only
  at primes `≤ N` when the period exceeds `N^c` (Assessment: open);
  composite Gallagher kernels with huge `Nh/(W_K−h)`; class types other
  than the four above; family primes beyond `N^{O(1)}`.

Model-only remark: the a-frame/multiplicative route sits at
`θ* ≈ 0.52` under its model, below 3/4 (**Assessment**, ET §5.2). The
proposed universal "0.5823 ceiling" was withdrawn as restricted-model only
(ledger (F)6).

### 2.5 Short intervals and progressions

`EXCEPTIONAL_SHORT.md` (ledger (D)30; review
`reviews/exceptional-short-review.md`, no FATAL/MAJOR, 8 minors repaired by
the author). All statements are PROVED relative to the 3/4 note.
* Thm 1: for every interval I of length H ≥ 2, at any position,
  `E(I) ≪ H exp(−c(log H)^{3/4})`; hence `E((x,x+H]) ≪_θ H exp(−c(log x)^{3/4})`
  for `H ≥ x^θ`. The note's majorant is a finite combination of congruence
  classes counted class by class, so it is shift-uniform; a local
  decomposition n = d·m (d smooth) replaces the note's global Rankin step.
* Thm 2: the same bound in progressions n ≡ b (mod q), uniformly for
  `q ≤ exp(c'(log(H/q))^{3/4})` and for q with all prime factors > X. Large
  smooth q are open.
* Cor 3.1: the bound holds for primes in (x, x+H] once
  `H ≥ exp(C(log log x)^{4/3})`, with no primes-in-short-intervals input.
* Prop 4.1: such a bound for `H < e^{c(log x)^{3/4}}` would imply ES for all
  large n; beyond that range shift-uniform methods are governed by (W) of
  (D)29 (Assessment).
* Novelty is modest (shift-uniformity is routine); no published
  short-interval or progression result was found (Li Delang 1981 not read
  in full).

### 2.6 The 3/4 bound for m/n, uniformly in m

`EXCEPTIONAL_MN.md` (ledger (D)31; two independent hostile reviews
`reviews/exceptional-mn-review-A.md`, `-B.md`, no FATAL/MAJOR, minors
repaired by the author). All statements are PROVED relative to the 3/4 note.
* Thm A: there are absolute constants c, C such that for every m ≥ 4 and
  every interval I of length H ≥ 2,
  `E_m(I) ≤ C H exp(−c(log H)^{3/4} m^{−1/4})`. The note transfers with
  4 → m: the identity is kℓ + 1 = m·uvw, the multipliers satisfy
  (k, m) = 1, and the modulus is q = muv. The whole m-dependence is
  `t³ → t³/m`. The Jacobi dichotomy of POINTWISE_MN plays no role here.
* This improves Pomerance–Weingartner's explicit-in-m Vaughan bound
  `exp(−C(log N)^{2/3}/φ(m)^{1/3})` (arXiv:2511.16817 Thm 1.3)
  asymptotically. It is non-trivial up to m ≤ ε(log N)³.
* Thm B / Cor C: progression and short-interval prime versions, as in §2.5.
* Cor D: most primes in (N/2, N] are m-representable once
  `log N ≥ C m^{1/3}(log m)^{4/3}`. With PW Thm 3.1 this places the density
  transition at `log n = m^{1/3+o(1)}`, up to a gap factor
  `(log m)²(m/φ(m))^{1/3}`.
* Novelty (Assessment): no 3/4-type, short-interval or progression result
  for m/n was found in the literature; new for m ≠ 4, by the note's method.
* Follow-up `EXCEPTIONAL_MN2.md` (two independent reviews
  `reviews/exceptional-mn2-review-A.md`, `-B.md`, no FATAL/MAJOR): the
  density transition for m/p, with `A = log N / m^{1/3}`.
  * Thm U (PROVED relative to (D)31 Cor 3.2, Bombieri–Vinogradov and Shiu;
    ineffective): for every ε there is A_ε such that at most a proportion ε
    of the primes in (N/2, N] are m-exceptional once A ≥ A_ε, uniformly in
    m ≥ 4. This removes the `(log m)^{4/3}` of Cor D (bounded-depth
    Bonferroni in a reduced CRT model for primes).
  * Thm L (PROVED relative to ET Thm 7.1 and the structure of ET's proof of
    Prop 1.4, plus Brun–Titchmarsh and Shiu):
    `ρ_rep ≪ L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}`, a factor log m
    better than Pomerance–Weingartner.
  * Remaining gap: a factor `(m log m/φ(m))^{1/3}` in log N, from ET's Type I
    Brun–Titchmarsh log log N (open even for m = 4) and m/φ(m).
  * EVIDENCE: `L_{1/2} = (1.95 ± 0.05) m^{1/3}` for even m ∈ [60, 300]
    (reproduced from scratch by both reviewers); profile ≈ 1 − exp(−κA³).
    Conj C2 (CONJECTURE): `ρ_rep = F(A) + o(1)` with F non-degenerate, i.e.
    no sharp threshold constant.
  * Written up as §8 of `paper/es-mn-short-note` (O104; referee R104: ACCEPT
    after minor repairs, applied).

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
* *The m/n witness modulus* (POINTWISE_MN.md, (H)32). The classes −mD
  mod M are Jacobi non-residues for every atom iff m ≡ 0 (4) (Lemma 1.1,
  PROVED), which is exactly where OMEGA13's square-class quarantine
  works. For m ≡ 0 (4): Haar exponent 3 and
  `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o. (Thm 3.1, PROVED
  modulo (G), Nair–Tenenbaum, the fundamental lemma and OMEGA10). For
  every m (incl. 5/n): exponent 1/5 i.o. (Cor 6.1, PROVED modulo ET, (G),
  OMEGA10; output primes Type-II-hard only), improving (H)23's 1/7. For
  m ≢ 0 (4), 1/4 is CONDITIONAL on a bounded-drift hypothesis ADM_m;
  POINTWISE_MN2 reduces ADM_m to the prefix law and to a CONJECTURE SI
  (PROVED modulo Henriot's uniform Nair–Tenenbaum bound). Reviews
  `reviews/pointwise-mn-review.md`, `-mn2-review.md`, repairs applied.
  Follow-up (POINTWISE_MN3, review `reviews/pointwise-mn3-review.md`,
  repairs applied): SI is **not** proved; the file records where it
  fails. For the class-of-one prefix the weights are bounded by
  class-of-one sums `U_1(q)` (Lemma 1.1, PROVED), and with three
  admissible levels a variant SI_3 (which also implies ADM_m) needs only a
  square-root saving `U_1(q) ≪ q^{−1/2−δ}` plus level-0 pair sums
  (Lemma 3.1, PROVED). The multiplicity `R(N)` satisfies
  `R(N) ≪ N^{3/5+o(1)}` (Lemma 5.2). Assessment: the obstruction is a
  Kloosterman-range residual; for `q ≥ Q_0` a second moment
  (M2) `Σ_{N≤X} R(N)² ≪ X(log X)^C` would remove it (CONJECTURE); the
  range `q_0 < q < Q_0` is a separate open component.

**The Haar exponent is exactly 3, and 1/4 is a ceiling.**
* *Haar side.* For the profinite avoider density `δ*(T)`,
  `𝓛³/log 𝓛 ≪ log(1/δ*(T)) ≪ 𝓛³(log 𝓛)^5`. Lower bound:
  POINTWISE_HAAR Thm 2.1, PROVED modulo the sieve fundamental lemma, via a
  new Janson-type inequality for product spaces with one-hot coordinates
  ((H)25). Upper bound: POINTWISE_OMEGA13 Thm 3.4, PROVED modulo
  Nair–Tenenbaum ((H)26). CEILINGS_UNIFIED Prop 1.1 removes the log loss
  in the lower bound, `log(1/δ*(T)) ≫ 𝓛³` (PROVED given the 3/4 note;
  inputs BV/BT/Shiu; ineffective; (H)29), so `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log 𝓛)^5`.
  The Monte Carlo of POINTWISE_SIZE §7 fits this (EVIDENCE). So the profinite exponent is 3 up to logs, and the
  heuristic prime-side truth is `log W ≍ (log p)^{1/3}`.
* *Ceiling* (POINTWISE_OMEGA14, (H)27). Conditioned on the small
  coordinates, the problem is a sieve of dimension `κ ≍ 𝓛³` on the big
  primes, and the sieving limit forces level `≈ e^{𝓛κ}`. Thm 4.5
  (PROVED modulo Gallagher (G), the effective Page bound and the
  fundamental lemma): on any fibre, every minorant of level
  `log D ≤ c𝓛⁴/log 𝓛` has Haar mean `≤ 0`. Cor 4.6 (PROVED implication):
  1/4 is the ceiling, up to `(log log p)^{1/2}`, of every certificate
  that goes through a Haar minorant plus a transfer requiring
  `log x ≫ log Z`. The tool is a planting lemma (Lemma 1.1), the LP dual
  of lower-bound sieves; it sharpens Benjamini–Gurel-Gurevich–Peled's
  Thm 27 (audit 10b §4, "apparently new"). CEILINGS_UNIFIED Prop 4.2
  raises the blocked level to `c𝓛⁴` (on fibres with `log Q ≤ T^{0.05}`),
  so the gap between OMEGA13's exponent and the ceiling is now
  `(log log p)^{1/4}`.
* *Wiener-norm barrier* (POINTWISE_OMEGA15, (H)28; PROVED modulo (G), the
  effective Page bound and the fundamental lemma). Every minorant B ≤ F of
  any level on any fibre has `E B ≤ e^{−c𝓛⁴/log 𝓛}‖B‖_×` (ℓ¹ norm over
  residue classes or characters). So linear certificates with full-orbit
  uniform accuracy (standard sieve-remainder accounting, one-sided and
  Hölder-averaged variants) cannot beat 1/4, and within this class prime
  input (GRH etc.) is irrelevant by construction. The Siegel-model law is
  covered too (Thm 3.1), closing OMEGA14's Siegel item for such transfers.
  Assessment: the ceiling is a sieve-*dimension* barrier, a property of
  the set F itself.
* *One sieve limit behind both ceilings* (CEILINGS_UNIFIED, (H)29). In the
  one-big-coordinate setting, order-k majorants and order-k minorants are
  both trivial below `k ≍ P` (the mass), and Bonferroni attains both at
  `k ≍ P` (Thm 4.1, PROVED; no novelty claimed). The ES one-big-prime
  subfamily has mass `≍ 𝓛³` at cost `≍ 𝓛`, so the critical level is
  `≍ 𝓛⁴`: at budget `λ ≍ log N` this is the exceptional-set cap `λ^{3/4}`;
  at `λ ≍ log x` it is the pointwise cap `𝓛 ≲ λ^{1/4}` (Thm 4.3, PROVED as
  a conjunction within the scopes of (D)24/(D)27 and (H)27/(H)28,
  Assessment outside them). The "Haar-side route" to 3/4 is the 3/4 note's
  own route and cannot improve it. Review SOUND (10 minors).
* *What gives 1/3* (POINTWISE_OMEGA16, (H)30). Hypothesis LS(C)
  (**CONJECTURE**, "Linnik for sifted sets"): every unit-class sieve system
  with moduli ≤ T and avoider density δ > 0 contains a prime p > T with
  `log p ≤ C(log T + log(1/δ))`. Thm 1.2 (PROVED implication, modulo
  Nair–Tenenbaum): LS ⇒ `W(p) ≥ exp(c(log p)^{1/3}(log log p)^{−5/3})` i.o.,
  the heuristic truth. EH/GEH/BV-type inputs and GRH truncated to moduli
  ≤ x cap at 1/4 through linear certificates (Prop 3.1); Hardy–Littlewood
  for CRT-product sets gives only `W = (log p)^{2±o(1)}` (Prop 4.1). No
  refutation of LS was found.
* *Support-aware certificates* (POINTWISE_OMEGA17, (H)31). No certificate
  beyond 1/4 was found. PROVED structural lemmas (moduli > x contribute
  only the box or primality tests; validity is an integer statement; no
  monotone fake). The question reduces to **Conjecture SAP** (support-aware
  planting, restated after review), whose truth would extend the 1/4
  ceiling to LP-relaxed support-aware certificates with unconditional-type
  information. SAP is **open**; so is the role of Type II input.

**Typical size: the tail exponent of W over primes is 3.**
* *Upper bound* ((A)9, INTERNALLY PROVED via the 3/4 note;
  CEILINGS_UNIFIED Thm 2.1): `#{p≤x: W(p)>T} ≪ π(x)exp(−c(log T)³)`
  uniformly for `log T ≤ c₁(log x)^{1/4}`.
* *Lower bound* (POINTWISE_TAIL Thm 2.1/3.3, (H)33; PROVED modulo (G),
  Nair–Tenenbaum and OMEGA10 Thm 3.4). For `log x ≥ C(log T)^4 log log T`,
  `#{p ≤ x Mordell-hard : W(p) > T} ≥ π(x)exp(−C(log T)³(log log T)³)`.
* So for `log T ≤ c(log x/log log x)^{1/4}`,
  `c(log T)³ ≤ log(π(x)/#{p≤x: W(p)>T}) ≤ C(log T)³(log log T)³` (Cor 2.2):
  the Haar exponent 3 is the true tail exponent of W over primes in this
  range. Review `reviews/pointwise-tail-review.md`, no FATAL/MAJOR.

**Consequences.**
* `H_MOD(A)` is **REFUTED for every A** (ledger (F)10, (H)13).
* So no pointwise multiplier mechanism whose witness moduli are
  `≤ exp((log p)^{1/4−ε})` can prove ES.

**Related results.**
* *Heuristic truth.* `log W ≍ (log p)^{1/3}` (**Assessment**,
  POINTWISE_SIZE §7), now backed by the Haar exponent 3 above. Data:
  `W ≈ (log p)^{2.5–3.4}` for `10^8 ≤ p ≤ 10^50` (EVIDENCE). The least
  hard prime with `W > 4095` is 133050918961 (W = 5935); no hard prime
  with `W > 8191` below 2.38·10¹¹ (EVIDENCE, OMEGA16 §6, recomputed).
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
  * Follow-up (POINTWISE_TYPEI2, review SOUND): under H, `C*(r)` equals
    the least height of a finite Type-I covering of `{n_p = r}` (Theorem A;
    one direction unconditional). At the explicit sign point `x̂_9` no
    Type-I certificate exists with ck ≤ 3·10⁹ (CERTIFIED), so every finite
    Type-I covering of `{n_p = 7}` has height > 3·10⁹ (previously ≥ 539;
    under H, C(7) > 3·10⁹). Whether `x̂_9` is sterile is open (Conjecture 3.4).
  * Follow-up 2 (POINTWISE_TYPEI3, review `reviews/pointwise-typei3-review.md`,
    no FATAL/MAJOR): sterility of `x̂_9` is **not** proved. A complete
    search graded by the smaller divisor f (Lemmas 1.1–1.2, PROVED) finds no
    certificate at `x̂_9` with f < 10¹², so every Type-I covering of
    `{n_p = 7}` has height > 1.32·10¹² and, under H, C(7) > 1.32·10¹²
    (CERTIFIED: two engines to 10¹¹, one to 10¹²); for r = 23, 31, 47 the
    bounds are > 2.39/2.78/3.42·10¹¹. A Vieta/Pell descent (PROVED,
    brute-forced) shows a certificate needs t ≥ 5 and 2-adic level ≥ 7,
    because levels 5 and 6 are empty; level 7 is open. The sterile set is
    closed and nowhere dense (Prop 3.1), and an explicit summable tail bound
    for near misses would give a sterile point (Remark 4.1, PROVED
    reduction).
  * Follow-up 3 (POINTWISE_TYPEI4, review `reviews/pointwise-typei4-review.md`,
    no FATAL/MAJOR, minors applied by the reviewer): sterility of `x̂_9` is
    still **not** proved. A certificate in the fibre at 2-adic level L is a
    norm-1 unit of ℤ[√d], `d = c_o(c_oδ² + 2^{L−4})`, which is a square of a
    specific shape: `16PX² − Q·49^b = 1`, `PQ = d` (Prop 1.2, Cor 1.4, PROVED).
    No higher-reciprocity obstruction exists in these coordinates (the quadratic
    test is an identity, quartic symbols are vacuous; Assessment). For fixed
    (L, b) the problem is finite with explicit bounds at all heights (Lemma 3.1,
    PROVED). CERTIFIED (two independent complete engines on the replayed
    ranges): no certificate at `x̂_9` with L ≤ 22 and `v_7(k) ≤ 3`, or L ≤ 26
    and `v_7(k) ≤ 1`, **at any height** — complementary to the f < 10¹² search.
    For L ∈ {11, 13, 14, 16, 18–22} the fibre is inhabited at other
    w ≡ 9 (16) (Prop 4.1, CERTIFIED), so no argument that sees w only mod 16
    can work there (Assessment). At L = 7 a partial 7-adic tower argument
    (Lemma 3.6, PROVED) rules out the gap j = 1 for every b; j ≥ 2 and 7 | j
    are open. Assessment: the remaining problem is exponential-Diophantine (a
    7-power tower), so linear forms in logarithms look like the right tool.
  * Follow-up 4 (POINTWISE_TYPEI5, review `reviews/pointwise-typei5-review.md`,
    no FATAL/MAJOR, minors applied by the reviewer): the 7-power tower is
    **not** closed. PROVED (Lemma 1.1, all L): if `16PX² − Qu² = 1` with 7 | Q has a
    solution with u = 7^b, it is the minimal solution. So b is determined by
    the other parameters, the certificate unit is `ε_f^k` with k ∈ {1, 2, 4},
    and the d-graded search is complete for all b. Lemma 3.1 also repairs
    TYPEI4 Lemma 3.6 (the case 7 | j). Thm 3.7 (PROVED + CERTIFIED, two
    independent engines): a certificate at `x̂_9` with level 7 ≤ L ≤ 10 must have
    `v_7(k) ≥ 8` and `c_oδ > 10⁶`, and must lie in the two-parameter regime (v)
    (λ ≥ 1, Δ > 2Tj). Every other regime, including case A at L = 8–10, is
    excluded for all b. Regime (v) is finite for each fixed (σ, a, λ), but σ and
    λ are unbounded; linear-forms-in-logarithms bounds do not apply because the
    field moves with two free parameters (Assessment).
  * Follow-up 5 (POINTWISE_TYPEI6, review `reviews/pointwise-typei6-review.md`,
    no FATAL/MAJOR, 7 minors applied by the reviewer): regime (v) is **not**
    closed. Over ℚ[δ] no norm-1 unit of the family d = c_o(c_oδ² + T) is integral for
    L ≥ 7, and continued-fraction periods are unbounded along every progression
    (Prop 2.1, PROVED), so the polynomial fundamental-unit route
    (Richaud–Degert / Yokoi type) provably fails. Regime (v) is the large-unit
    (generic) regime (Lemma 3.1); it is inhabited at L = 13 (Remark 1.2), so a
    closing argument must use T ≤ 64. Under abc each level has only finitely
    many certificates (Thm 3.2, CONDITIONAL; explicit abc forms do not give
    emptiness). CERTIFIED: no fibre certificate at L = 7–10 with v_7(k) ≤ 15, at
    any height (two engines except (L, b) = (9,15), (10,14), (10,15)). What
    remains: fields with c_oδ > 10⁶ and u_1(d) = 7^b, b ≥ 16; a naive model
    predicts fewer than 10⁻¹¹ such certificates (EVIDENCE).
* *Mordell-type coverings mod a further prime r* (POINTWISE_MORDELL.md,
  (H)34).
  * r = 13 (Thm 3.1, PROVED by finite computation, re-certified by R80):
    if `(p/13) = −1`, ES holds for the prime p unless
    `p mod 720720 ∈ {112561, 352801, 380881, 418321, 473761, 483841}`;
    if also `(p/11) = +1`, only the first two classes remain. Novelty is
    modest: it packages the Salez/ET level sieve explicitly.
  * No finite covering is known, and none is ruled out. The point x*
    (`x*_11 = x*_13 = 2`, `x*_q = 1` otherwise) lies in no ET class of
    modulus ≤ 10⁶ (Computation 4.1, CERTIFIED), so every finite covering of
    `Σ_13` needs a class of modulus > 10⁶ (PROVED). The conjecture that x*
    is sterile (POINTWISE_MORDELL Conj 4.2) is **REFUTED** (ledger (F)11;
    POINTWISE_MORDELL13B Thm 3.1, review `reviews/pointwise-mordell13b-review.md`,
    no FATAL/MAJOR). x* lies in the II3 class (a,d,e) = (8,33,11999), of
    modulus 12670944 = 2⁵·3·11·13²·71, and in the I2 class (125,88,11999).
    For example the prime p = 12650497 has
    4/p = 1/3165624 + 1/3339731208 + 1/5005839614391.
  * MORDELL13B also attaches every class meeting the {11,13}-generic points
    to an ES solution of 4/N with N an {11,13}-unit (Lemmas 2.1–2.4,
    Cor 2.5, PROVED). This allows a complete enumeration by N (to 4·10⁷,
    CERTIFIED, one engine plus a brute-force cross-check). The (2,2) cell is
    still not covered (≤ 4.64% uncovered at resolution 11⁴·13⁴; an upper
    bound, EVIDENCE). The new candidate x** = x(2,15) lies in no class with
    e ≤ 10⁸ (II3/I3/I1), f ≤ 3·10⁷ (II2), or f, e ≤ 2·10⁷ (I2/II1/I4)
    (Comp 5.1, CERTIFIED within these ranges). That x** is sterile is Conj 5.2
    (CONJECTURE, supported only by this EVIDENCE). The main-variant r = 13
    covering question is open again.
  * Follow-up POINTWISE_MORDELL13C (review `reviews/pointwise-mordell13c-review.md`,
    no FATAL/MAJOR, minors applied by the reviewer). Thm 6.1 (PROVED by finite
    computation; three independent checkers, one by the reviewer): an adaptive
    tree certificate with 136494 covered leaves and 2140 ET classes shows that
    ES holds for every prime with (p/13) = −1 outside 35459 explicit classes,
    which make up 8.42e-5 of the six old exceptional classes mod 720720
    (about 2.3e-7 of the Mordell-hard residues with (p/13) = −1). No root
    class closes completely. A complete fixed-level witness engine (all M | L,
    no size cap) shows the modulus cap is not the bottleneck. Comp 3.1
    (CERTIFIED): the uncovered part of the (2,2) cell mod 11^2 13^2 is exactly
    {2,57,79} x {15,28,54,132,145}. x** lies in no P/Q-type class with
    e <= 2e9 and in no I2/II1/I4 class with f, e <= 2e8 (one engine);
    it remains a candidate (Conj 5.2, CONJECTURE).
  * r = 17 (POINTWISE_MORDELL17, review rounds 1–2, no FATAL/MAJOR): on the
    17-generic line the seven ET families become explicit boxes in ℤ_17
    (PROVED). Boxes of level ≤ 5 leave 67.7% of each non-residue cell
    uncovered (Comp 3.1, CERTIFIED, two engines). Thm 4.1 (PROVED
    sufficient condition): an explicit tail bound gives a sterile point,
    hence (CONDITIONAL, Cor 4.2) no finite set of polynomial ES identities
    covers the Mordell-hard primes with n_p = 17. The critical input is
    the prime-power count
    `#{(a,b): ab ≤ 17^K, (−17^K mod 4ab) | a+b} ≤ C·17^{(1/2−δ)K}`
    (ET give only the non-explicit `N^{2/5+o(1)}`; data fit ≈ K³).
    Existence of a sterile point is Conj 4.3 (CONJECTURE); making the
    bound explicit is a discrete-log equidistribution question
    (Assessment).
  * Follow-up 2 (POINTWISE_MORDELL17B, review `reviews/pointwise-mordell17b-review.md`,
    one MAJOR numerical rounding error and minors repaired by the author):
    still CONDITIONAL; no sterile point is proved. An exact form of ET's
    four-regime cover (Lemma 2.1) gives a complete P-enumerator about 50×
    faster, with D_P(11) = 836 and D_P(13) = 1463 (CERTIFIED by two engines
    for K = 13). Exact unions through P-level 6 leave ρ₁ = 16344335/24137569
    ≈ 0.677133 of each cell uncovered. Thm 4.1 (PROVED reduction): a sterile
    point in C_5 and C_7 follows from `D_P(K) ≤ C·17^{θK}` for odd K ≥ 13
    together with `D_Q(k) ≤ 17^{3k/5}` for odd k ≥ 9, e.g. with θ = 2/5 and
    C ≤ 1.40. So ET's own exponent with an explicit constant below 1.4097
    and no o(1) would suffice. Conj 4.2 (CONJECTURE): D_P(K) ≤ K⁵ (K ≥ 15)
    and D_Q(k) ≤ k⁵ (k ≥ 9), which would give a tail ≤ 4.2·10⁻³. Averaging
    over K is only a reorganisation (Lemma 5.1); the bottleneck is an
    explicit count in the e- and cd-regimes.
  * Follow-up 3 (POINTWISE_MORDELL17C, review `reviews/pointwise-mordell17c-review.md`,
    minors applied by the reviewer): still CONDITIONAL. By Abel summation,
    cumulative bounds `S_P(K) = sum_{13<=K'<=K} D_P(K') <= C*17^{theta*K}` suffice,
    raising the admissible constant at theta = 2/5 to 1.497 for K >= 13
    (Lemma 1.1, PROVED). The Q-points with c >= F^{1/2} are bounded
    unconditionally (at most 2 per (a,d); Lemma 2.1 and Cor 2.2, PROVED).
    Assessment/EVIDENCE: averaging over K cannot rescue P. Arguments that ignore
    the size of the discrete log of -e mod 4ab give only theta ~ 1, so a proof
    must show that these discrete logs rarely fall in the short window
    [log_17 4ab, K].
* *Write-ups.* `paper/es-omega-note.tex` v3 (every fixed exponent; 31 pp;
  internal referee, P1–P4 applied) and `paper/es-subexp-note.tex` v5
  (51 pp; exponent 1/4, Haar exponent 3 with the log-free lower bound,
  typical size `≪ π(x)e^{−c𝓛³}`, the ceiling at level `c𝓛⁴`, the
  Wiener-norm barrier, and LS ⇒ 1/3; refereed internally five times, R33,
  R33b, R47, R56, R64). v6 (merged) adds the two-sided tail of (H)33 and the m/n
  analogues (refereed, R77 minor revision applied). `paper/energy-dnf-note.tex`
  (17 pp) writes up the energy bound C-1 and the DNF tails as a
  stand-alone result (refereed internally, R50 minor revision applied).
  `paper/es-coverings-note` (finite coverings and candidate sterile points:
  TYPEI2/3, MORDELL, MORDELL17) is written and refereed internally (R86, repairs applied); post-referee
  additions TYPEI4 (O91) and the refutation of the x* conjecture with the new candidate x** (O96;
  25 pp) were refereed in round 2 (R98, `reviews/es-coverings-note-referee-r2.md`: no FATAL/MAJOR,
  seven minors applied; TYPEI5 added as Prop 4.15 / Thm 4.16). TYPEI6, MORDELL13C, MORDELL17B and
  MORDELL17C are not yet in the note. `paper/es-mn-short-note` (25 pp; O97 + O104) writes up
  EXCEPTIONAL_SHORT, EXCEPTIONAL_MN and, in Section 8, EXCEPTIONAL_MN2 (referees R97 and R104,
  repairs applied; R104: ACCEPT).

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

**Exact stacking orders** (POINTWISE_XWIN.md, (H)18; **PROVED**,
review `reviews/pointwise-xwin-review.md`).
* *Half-set lemma* (Lemma 1.1). For any `a ≡ 3 (mod 4)`, if window `a`
  fails at `x` then all prime factors of `x` lie in one of `2^{β(a)}`
  explicit sets of exactly `φ(a)/2` residue classes, with no exceptions.
* *Fixed-set stacking* (Thm 1.2, Cor 1.3). For any fixed set `A` of
  windows, `#{p ≤ N : all a ∈ A fail} ≪_A N/(log N)^{1+|A|/2}`. Hence
  `#{p ≤ N : a_min(p) > Z} ≪_Z π(N)(log N)^{−J(Z)/2}`, the random model's
  exact exponent.
* *Exact orders* (Cor 1.4). `#{a_min ≥ 7} ≍ x/(log x)^{3/2}`
  unconditionally and `#{a_min ≥ 11} ≍ x/(log x)²` on EH. So W1 and W2
  are sharp. A uniform version holds for `Z` up to about
  `3.6 log log N` (Thm 1.5, PROVED modulo Siegel–Walfisz).
* The window tail bound of Thm 2.2 is a second proof of what notes
  Thms 14.4/14.9 already imply (priority to the notes).

**Two windows need parity** (POINTWISE_WINDOW2.md, (H)20; review
`reviews/pointwise-window2-review.md`). Unconditional `a_min(p) ≥ 11`
was **not** reached.
* Windows 3 and 7 are both clean iff `n, n+1` are primitive norms from
  `ℚ(√−3)` and `ℚ(√−7)`: a Friedlander–Iwaniec-shaped quadric (Lemma 1.2,
  PROVED).
* *Parity is necessary* (Thm P1, PROVED; necessity modulo BV resp. EH).
  The classes `(p/3) = ±1` have identical sieve data, but the −1 class
  never has window 3 clean. This is Selberg's parity example realised by
  primes.
* *Model obstruction.* In a discrete model of Type-I correlations of
  level θ plus parity, there is a "fake" with no both-clean mass at
  θ = 1/2 (Prop 3.7, CERTIFIED in the model); the model's two-window
  threshold lies in (0.5, 0.7]. So Type-I plus parity at BV level does
  not give two windows in the model. Relevance to real sieves is weak
  EVIDENCE only.
* *Faithful model* (POINTWISE_WINDOW3; EVIDENCE/Assessment, merged without
  a separate hostile review). Type-I data at level 1/2, both parities and
  Chen-type switching give `a_min ≥ 11` only if the switched bounds are
  within ≈ 2–2.5 of the truth uniformly over every switchable family; the
  best existing switched constants are ≥ 3.9 at BV level (checked in Wu
  2004). So the unconditional two-window problem has a precise numerical
  gap.

**Write-up.** `paper/es-window-note.tex` (22 pp): window criterion,
half-set lemma, stacking, W1/W2 and exact orders, Prop P1, with the model
and data as labelled remarks (refereed internally, R41 minor revision
applied).

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
| E10 | **No θ > 3/4 for coefficient-sum CRT sieves over any mixture of the four forced/selector class types**; saving `≤ C L^{3/4}(log L)^{3/4}`, `≪_B L^{3/4}` under fixed B (log factor dropped by E16) | PROVED (internal) | `EXCEPTIONAL_KARY2.md` Thm 5.1, 5.2, Cor 6.1; `paper/sieve-limits-note.tex` | `reviews/exceptional-kary2-review.md`, `-review-2.md`; `reviews/sieve-limits-note-review-v2.md`, `reviews/papers-v3-review.md` | Elsholtz–Tao Prop 1.4 (Case-A part only) |
| E11 | Heuristic ceiling `θ = B/(B+1)` (2/3 at B = 2, 3/4 at B = 3) | Assessment (proved arithmetic under the stated assembly model) | notes §18.3–18.4 | — | — |
| E12 | Large sieve capped: every CRT-admissible large-sieve bound is `≥ N·E\|g*\|²` (Selberg-square majorant), so saves `≤ C L^{3/4}(log L)^{3/4}` (polynomial denominators), `C_B L^{3/4}` (bounded B); includes the 2/3 note's use (log factor dropped by E16) | PROVED, conditional on KARY2 Thm 5.1 | `EXCEPTIONAL_LARGESIEVE.md` Thm 2.1, 3.1, Cor 3.2, Thm 4.1, 6.2 | `reviews/exceptional-largesieve-review.md` (SOUND) | KARY2 Thm 5.1 (hence Elsholtz–Tao Prop 1.4 for Case A) |
| E13 | Selberg minorant `Σ_{n≤N}ν ≥ (N−D)Eν`; majorants from forced classes of modulus `≤ N/2` save `≤ C L^{3/4}(log L)^{3/4}` under any evaluation of the interval sum (log factor dropped by E16) | PROVED (internal) | `EXCEPTIONAL_INTERFREQ.md` Thm 2.2, Cor 2.3, Thm 2.5 | `reviews/exceptional-interfreq-review.md` | KARY2 Thm 5.1 |
| E14 | TC_θ ⇒ `E(N) ≤ (e+2)N exp(−(2/e²)L^θ)`; TC holds for `K ≤ cL^{2/3}`, fails for even `K ≥ (e²/2+ε)L`; bounded-order correlations cannot give θ > 3/4 | PROVED (internal); TC_θ for 3/4 < θ < 1 is a CONJECTURE | `EXCEPTIONAL_TUPLES.md` Cor 2.3, Prop 2.4, Thm 3.1, Prop 4.2 | `reviews/exceptional-tuples-review.md` (all items SOUND) | KARY2 Thm 5.1 (Cor 3.4) |
| E15 | Prime-only majorants (≥ 1 only at avoider primes) for any mixture save `≤ Cλ^{3/4}(log λ)^{3/4}`; prime-law methods (SW/BV/BDH/EH/GRH level, moduli `≤ N^A`) capped at 3/4 | PROVED (internal) | `EXCEPTIONAL_PRIMELAW.md` Thm 3.1, Cor 4.2 | `reviews/exceptional-primelaw-review.md` (SOUND) | Elsholtz–Tao Prop 1.4 (Case A) |
| E16 | **The `(log log N)^{3/4}` loss removed:** every CRT majorant of level λ over any mixture, no B-hypothesis, has `log(1/Eν) ≤ Cλ^{3/4}`; coefficient-sum sieves save `≤ C_A L^{3/4}`; truncated weights; bounded prime order | PROVED given KARY2 as reviewed (§§6–7 parent-checked only) | `EXCEPTIONAL_KARY3.md` Thm 4.1, Cor 4.2, Thm 5.1, Cor 5.2–5.3; `paper/sieve-limits-note.tex` v4 Thm 10.14 | `reviews/exceptional-kary3-review.md` (SOUND); `reviews/sieve-limits-note-review-v4.md` | Shiu (progressions); Elsholtz–Tao Thm 7.1, Cor 7.4, (7.10) (Case A) |
| E17 | Literal TC_θ (θ > 2/3) needs a compensating CRT excess (forced zeros); TC^alt_θ and TC^𝔄_θ ⇒ `E(N) ≤ CN exp(−(2/e²)L^θ)`; pure prime family capped at `L^{2/3}` for CRT-main-term sieves | PROVED / PROVED implications (internal); literal TC_θ false on (2/3,1) is an Assessment; TC^alt_θ for θ > 3/4 open | `EXCEPTIONAL_TUPLES2.md` Thms 2.1–2.2, Cor 2.3, Thm 4.1, Cor 4.2, Cor 6.1 | `reviews/exceptional-tuples2-review.md` (SOUND) | KARY2 Thm 5.1 (Prop 7.1) |
| E18 | Comparison measure; twisted/hybrid/Gauss-sum large sieves and the large sieve on primes capped at `C_A L^{3/4}`; Gallagher's larger sieve (prime-power kernels) `≤ 26 log log N + C`; band-family escape (abstract axioms cannot close H_LS∞) | PROVED (internal; conditional on KARY2/KARY3 where cited); H_LS∞ for forced families a CONJECTURE | `EXCEPTIONAL_LARGESIEVE2.md` Lemma 1.1, Thm 2.4, Cor 2.5, Thms 3.1, 4.3, 8.5, 9.1 | `reviews/exceptional-largesieve2-review.md`, `-review-2.md` (SOUND) | KARY2/KARY3; Montgomery–Vaughan large sieve |
| E19 | Hybrid methods: exact LP dual, sign rule; 3/4 cap when right-signed mass `≤ cB`; Flat ⇒ cap; SPW ⇒ Flat | PROVED / PROVED implication (internal) | `EXCEPTIONAL_INTERFREQ2.md` Prop 2.1, Lemma 3.1, Cor 5.1, Thm 5.2, Prop 9.1 | `reviews/exceptional-interfreq2-review.md` (SOUND) | KARY2/KARY3 |
| E20 | SPW with fixed σ is false: `σ ≲_C (log N)^{−1/2}`; exact certificates at N = 300, 1150; weak SPW untouched and open | PROVED; certificates exact | `EXCEPTIONAL_SPW.md` Thm 3.2, Cor 3.3 | `reviews/exceptional-spw-review.md` (SOUND) | Fejér kernel, Bernstein's inequality |
| E21 | Weak-SPW requirement exact: hybrid saving `≤ C′L^{3/4} + log(K_N/η_N) + log(1+Δ′_N/K_N) + O(1)`; K-free edge bound `η ≲_C L^{−1/3}` refutes fixed-η RSPW | PROVED (internal); no `N^{−1/2}` decay for N ≤ 80 is EVIDENCE only | `EXCEPTIONAL_SPW2.md` Lemma 1.1, Thm 3.1 | `reviews/exceptional-spw2-review.md` | KARY2/KARY3 |
| E22 | Smooth–rough splitting; **every CRT-admissible large sieve at any frequency level** saves `≤ C L^{3/4}(log L)^3` for mixtures with ≤ 1 prime factor above `exp(L^{1/4})` per modulus | PROVED (given the reviewed KARY2 inputs; ET Prop 1.4 for Case A) | `EXCEPTIONAL_LARGESIEVE3.md` Thm 1.1, Lemma 2.1, Thm 3.1; `paper/sieve-limits-note.tex` v5 Thms 14.12–14.13 | `reviews/exceptional-largesieve3-review.md` (SOUND); `reviews/sieve-limits-note-review-v5.md` | Hausdorff–Young; KARY2; Elsholtz–Tao Prop 1.4 |
| E23 | Damped-collision reduction; (A*) ⇒ all-level 3/4 cap for all forced mixtures; **all-level cap for residue-sparse multi-rough classes** (incl. all small-height classes −r/s, e.g. −4 mod M) | PROVED / PROVED implication (Thm 4.2) | `EXCEPTIONAL_LARGESIEVE4.md` Lemma 1.1, Thm 4.2, Thm 5.2, Cor 5.3; sieve-limits v5 Thms 14.17–14.18 | `reviews/exceptional-largesieve4-review.md` (no FATAL/MAJOR) | as E22 |
| E24 | Rational labels −r/s mod G; tilted law satisfies (A*); (DCC) ⇒ all-level cap (PROVED implication); (RD) at one prime for ℛ(M) classes and for long cofactors; (RD) as first stated false for several primes, height-cut form fails with (a,D) classes; target is (RD′) | PROVED as labelled; one-rough-prime bound of LS6 CONDITIONAL on (FM2); (RD), (CC) CONJECTURES; (A*)/(DCC)/(RD′) open | `EXCEPTIONAL_LARGESIEVE5.md`, `-6.md` Thm 6.1, `-7.md` Lemmas 1.1–1.2, Thms 3.1, 4.3, Props 4.1, 5.1 | `reviews/exceptional-largesieve5-review.md`, `-largesieve6-review.md`, `-largesieve7-review.md` (repairs applied) | Shiu; Nair–Tenenbaum (LS7) |
| E25 | Cubic witness tail `#{p≤x: W(p)>T} ≪ π(x)exp(−c(log T)³)` for `log T ≤ c₁(log x)^{1/4}` | INTERNALLY PROVED (via E2; constants not effective) | ledger (A)9; `CEILINGS_UNIFIED.md` Thm 2.1; `paper/es-subexp-note.tex` v5 Thm 11.2 | `reviews/ceilings-unified-review.md` (SOUND); `reviews/es-subexp-note-review-v5.md` | as E2; uniform PNT in progressions with Landau–Page term (small T, cited from memory) |
| E26 | Per-frequency weights below 1: every bound whose weights dominate the window transform (smooth or sharp) is ≥ the shift-uniform avoider count `M_𝔊(N)`; for Selberg's window ≤ `12(K+1)M_𝔊(N)`; door capped at 3/4 iff (W_𝔊); sharp weights with hit-pattern majorants capped without (H_eq) | PROVED (internal); (W_𝔊) open; (H_eq) at several primes a CONJECTURE; toy numerics EVIDENCE | `EXCEPTIONAL_WEIGHTS.md` Lemmas 1.1–1.2, Thm 2.1, Cor 2.2, Thm 3.3, Prop 5.1 | `reviews/exceptional-weights-review.md` (no FATAL; one MAJOR repaired) | Selberg majorant; as E22 |
| E27 | (W) neither proved nor refuted; CRT alignment fails: one maximal family suffices; forced window mass of prime slices `(log N)^{o(1)}`; prime-slice density `≤ exp(−c(log Y)²)`; random shifts lose `e^{−c(log N)²}`; quadratic alignment caps at `√(N log N)`; (W) for prime slices = growing-dimension Hensley–Richards attainment | PROVED as labelled (Prop 3.1 ineffective); composite case of Lemma 2.2 partly open; §6 numerics EVIDENCE; refutation of (W) does not give θ > 3/4 | `EXCEPTIONAL_WEIGHTS2.md` Lemmas 1.1, 2.1–2.3, 5.1, Props 3.1, 4.1, 4.3, 5.2, 5.3 | `reviews/exceptional-weights2-review.md` (no FATAL; 3 MAJOR repaired by the author) | Bombieri–Vinogradov (Prop 3.1); Montgomery large sieve; Wirsing (Prop 5.3) |
| E28 | Short intervals and progressions: `E(I) ≪ H exp(−c(log H)^{3/4})` for every interval of length H; progressions with `q ≤ exp(c'(log(H/q))^{3/4})` or q X-rough; primes in (x, x+H] for `H ≥ exp(C(log log x)^{4/3})` | PROVED relative to the 3/4 note; Prop 4.1 consequence an Assessment beyond its range | `EXCEPTIONAL_SHORT.md` Thms 1–2, Cor 3.1, Prop 4.1 | `reviews/exceptional-short-review.md` (no FATAL/MAJOR) | the 3/4 note |
| E29 | m/n uniformly in m: `E_m(I) ≤ C H exp(−c(log H)^{3/4} m^{−1/4})` for every m ≥ 4 and every interval of length H; progression and short-interval prime versions; density transition at `log n = m^{1/3+o(1)}` | PROVED relative to the 3/4 note; novelty an Assessment | `EXCEPTIONAL_MN.md` Thm A, Thm B, Cor C, Cor D | `reviews/exceptional-mn-review-A.md`, `-B.md` (no FATAL/MAJOR) | 3/4 note; Pomerance–Weingartner Thm 3.1 (Cor D comparison) |
| E30 | m/p density transition, A = log N/m^{1/3}: Thm U (exceptional proportion <= eps once A >= A_eps, uniformly in m >= 4); Thm L (`rho_rep << L^3/m + (L^3 + L^2 log^2 m) log L/phi(m) + m^{-0.35}`); gap `(m log m/phi(m))^{1/3}` in log N; `L_{1/2} = (1.95 +- 0.05) m^{1/3}` for even m in [60, 300]; Conj C2 | Thm U PROVED rel. (D)31 Cor 3.2 + BV + Shiu (ineffective); Thm L PROVED rel. ET Thm 7.1 / structure of ET's proof of Prop 1.4 + BT + Shiu; numerics EVIDENCE; C2 CONJECTURE | `EXCEPTIONAL_MN2.md` Thms U, L, §2, Conj C2; `paper/es-mn-short-note` §8 | `reviews/exceptional-mn2-review-A.md`, `-B.md` (no FATAL/MAJOR); paper R104 (ACCEPT) | Bombieri-Vinogradov, Shiu, Brun-Titchmarsh, Elsholtz-Tao, Pomerance-Weingartner |

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
| P19 | Haar side: `log(1/δ*(T)) ≤ T^{o(1)}`, and `≪ (log T)^7 log log T` | PROVED; second form modulo the cited theorem (superseded by P36–P37) | `POINTWISE_OMEGA2.md` Thm 11.3 | `reviews/pointwise-omega2-review-r3.md` | Elsholtz–Tao Prop 1.4 (second form) |
| P20 | **Every fixed exponent:** `W(p) ≥ (log p)^{k−o(1)}` i.o., every fixed `k` | PROVED modulo the cited theorem, effective | `POINTWISE_OMEGA3.md` Thms 4.3, 5.2 | `reviews/pointwise-omega3-review.md`, `-review-2.md` (SOUND) | Thorner–Zaman |
| P21 | Explicit rate `log W ≥ (1+o(1)) log₂p·log₃p/log₄p` i.o. | PROVED modulo the cited theorems | `POINTWISE_OMEGA4.md` Cor 3.1–3.3 | `reviews/pointwise-omega4-review.md` | Thorner–Zaman; Elsholtz–Tao Prop 1.4 (dropping it gives `log₂p·log₄p/log₅p`) |
| P22 | HC* ⇒ `log W ≥ 0.2√a (log₂p)^{3/2}`; `m = 1` part of HC* | PROVED implication; `m = 1` part PROVED; HC_Π open; literal HC false (route superseded by P30–P37) | `POINTWISE_OMEGA4.md` Thm 4.2; `POINTWISE_OMEGA5.md` Thm 2.3 | `reviews/pointwise-omega4-review.md`, `reviews/pointwise-omega5-review.md` | Thorner–Zaman, Elsholtz–Tao |
| P23 | `ES(p) ⇔ a_min(p) < ∞`; window reciprocity | PROVED | `POINTWISE_SIZE.md` Thm 8.1, Lemma 8.2 | as P9 | none |
| P24 | W1: `a_min ≥ 7` for `≫ x/(log x)^{3/2}` hard `p` | PROVED modulo cited sieve theorems | `POINTWISE_WINDOW.md` §2 | `reviews/pointwise-window-review.md` | semi-linear sieve, Selberg sieve, BV (also FHRSS 2025) |
| P25 | W2: `a_min ≥ 11` for `≫ x/(log x)²` hard `p` | CONDITIONAL on Elliott–Halberstam | `POINTWISE_WINDOW.md` §4 | `reviews/pointwise-window-review.md` | EH (level `x^{1−ε₀}`) |
| P26 | `log W ≍ (log p)^{1/3}`; `a_min ≍ log p/log log p` | Assessment | `POINTWISE_SIZE.md` §7, §8 | — | — |
| P27 | Type-I map: congruence input gives exactly `ck_min = n_p` in every reduced hard class; `n_p = 5 ⇒ ck_min ≤ 10` (sharp at 193); covering heights ≥ 539 (`n_p = 7`), > 3000 (`n_p = 11`) | PROVED; Schinzel-H and GRH parts CONDITIONAL; census EVIDENCE | `POINTWISE_TYPEI.md` Prop 4.2, Thm 6.1, Cor 6.4, Thms 2.1, 3.1 | `reviews/pointwise-typei-review.md` (SOUND-AFTER-REPAIRS) | Schinzel H / GRH (conditional parts only) |
| P28 | Half-set lemma; fixed-set stacking `≪_A N/(log N)^{1+\|A\|/2}`; exact orders `#{a_min≥7} ≍ x/(log x)^{3/2}`, `#{a_min≥11} ≍ x/(log x)²` (on EH) | PROVED (uniform version modulo Siegel–Walfisz) | `POINTWISE_XWIN.md` Lemma 1.1, Thm 1.2, Cor 1.3–1.4, Thm 1.5 | `reviews/pointwise-xwin-review.md` | EH for the `a_min ≥ 11` lower bound (via W2) |
| P29 | Parity is necessary for two windows (Thm P1); model fake at θ = 1/2 | PROVED (necessity modulo BV resp. EH); model result CERTIFIED in the model only | `POINTWISE_WINDOW2.md` Lemma 1.2, Thm P1, Prop 3.7 | `reviews/pointwise-window2-review.md` | BV, EH |
| P30 | `W(p) ≥ exp(c(log p)^{1/14})` i.o. (BRW sandwich + switching lemma) | PROVED modulo the cited theorems | `POINTWISE_OMEGA8.md` Thm 4.3 | `reviews/pointwise-omega8-review.md`, `-review-2.md` (SOUND) | Thorner–Zaman; Elsholtz–Tao Prop 1.4; Håstad/LMN |
| P31 | `W(p) ≥ exp(c(log p)^{1/7})` i.o. (linear transfer via Gallagher) | PROVED modulo the cited theorems | `POINTWISE_OMEGA9.md` Thms 1.1, 2.2 | `reviews/pointwise-omega9-review.md`, `-review-2.md` (SOUND) | Gallagher (G) via MV III draft Thm 28.19; Elsholtz–Tao Prop 1.4 |
| P32 | **Energy bound C-1** on product spaces; width-k DNF tails `W^{>t} ≤ 4·2^{−(t+1)/k}` (sharp rate) | PROVED (internal) | `POINTWISE_OMEGA10.md` Cor 3.5, Thm 3.4, Cor 4.1; `paper/energy-dnf-note.tex` | `reviews/pointwise-omega10-review.md`, `-review-2.md` (SOUND); `reviews/energy-dnf-note-review.md` | none |
| P33 | `W(p) ≥ exp(c(log p)^{1/6})` i.o. (graded quarantine) | PROVED modulo the cited theorems | `POINTWISE_OMEGA11.md` Thm 3.2 | `reviews/pointwise-omega11-review.md`, `-review-2.md` (SOUND) | (G); Elsholtz–Tao Prop 1.4 |
| P34 | Abstract avoidance transfer; m/n analogues `W_m(p) ≥ exp(c_m(log p)^{1/7})` i.o. | PROVED as labelled | `POINTWISE_TRANSFER.md` Thm 1.1, Cor 5.2–5.3 | `reviews/pointwise-transfer-review.md` (SOUND) | (G), Landau–Page, Håstad; ET Prop 1.4 with κ = m |
| P35 | `W(p) ≥ exp(c(log p)^{1/5}(log log p)^{−1/5})` i.o.; `Ω_0 ≪ 𝓛⁴ log 𝓛` | PROVED modulo the cited theorems | `POINTWISE_OMEGA12.md` Thms 5.1, 6.3 | `reviews/pointwise-omega12-review.md`, `-review-2.md` (SOUND) | (G); Elsholtz–Tao Prop 1.4, Thm 7.1, Cor 7.4 |
| P36 | Haar lower bound `log(1/δ*(T)) ≫ 𝓛³/log 𝓛`; Janson-type inequality for one-hot product spaces | PROVED modulo the sieve fundamental lemma | `POINTWISE_HAAR.md` Thm 1.4, Thm 2.1 | `reviews/pointwise-haar-review.md` (SOUND) | sieve fundamental lemma |
| P37 | **Haar exponent exactly 3** (`≪ 𝓛³(log 𝓛)^5`); **`W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o.** | PROVED modulo the cited theorems | `POINTWISE_OMEGA13.md` Thm 3.4, Thm 5.1; `paper/es-subexp-note.tex` v4–v5 | `reviews/pointwise-omega13-review.md`, `-review-2.md`, `-review-3.md`, `-review-4.md` (SOUND); `reviews/es-subexp-note-review-v4.md`, `-v5.md` | Nair–Tenenbaum; (G) |
| P38 | **1/4 is the ceiling** of Haar-minorant + transfer certificates (no positive minorant of level `≤ c𝓛⁴/log 𝓛` on any fibre); planting lemma | PROVED / PROVED implication (Cor 4.6) | `POINTWISE_OMEGA14.md` Lemma 1.1, Thm 4.5, Cor 4.6 | `reviews/pointwise-omega14-review.md`, `-review-2.md` (SOUND) | (G), effective Page bound, fundamental lemma |
| P39 | **Wiener-norm barrier:** every minorant B ≤ F of any level has `E B ≤ e^{−c𝓛⁴/log 𝓛}‖B‖_×`; full-orbit uniform linear certificates (incl. Siegel-model law) cannot beat 1/4; prime-only minorants of one modulus `≤ x^{1/5}/(QT)` have `E B ≤ 0` | PROVED modulo the cited theorems; "dimension barrier" is an Assessment | `POINTWISE_OMEGA15.md` Thm 1.2, Thm 3.1, Prop 5.2; `paper/es-subexp-note.tex` v5 §12 | `reviews/pointwise-omega15-review.md` (math SOUND; scope repaired) | (G), effective Page bound, fundamental lemma; Linnik–Xylouris (Prop 5.2) |
| P40 | Haar lower bound `≫ 𝓛³` without log loss; no positive minorant of level `≤ c𝓛⁴` (gap to the ceiling `(log log p)^{1/4}`); one order-k sieve limit behind the 3/4 cap and the 1/4 ceiling | PROVED given the 3/4 note (Prop 1.1, 4.2); Thm 4.1 PROVED; Thm 4.3 PROVED within the scopes of (D)24/(D)27, (H)27/(H)28, Assessment outside | `CEILINGS_UNIFIED.md` Prop 1.1, Prop 4.2, Thms 4.1, 4.3; sieve-limits v5 §18; es-subexp v5 §11 | `reviews/ceilings-unified-review.md` (no FATAL/MAJOR) | as E2 (BV/BT/Shiu; ineffective); OMEGA14 Lemma 4.1 |
| P41 | **LS ⇒ `W(p) ≥ exp(c(log p)^{1/3}(log log p)^{−5/3})` i.o.**; EH/GEH/BV and truncated GRH cap at 1/4 via linear certificates; product subsets have `log(1/δ) ≍ T^{1/2±o(1)}` | LS a CONJECTURE; Thm 1.2 PROVED implication; Prop 3.1 PROVED; Prop 4.1 lower bound PROVED (ineffective); data EVIDENCE | `POINTWISE_OMEGA16.md` Thm 1.2, Props 3.1, 4.1, §6; es-subexp v5 §13 | `reviews/pointwise-omega16-review.md` (no FATAL; scope repaired) | Nair–Tenenbaum; Barban–Davenport–Halberstam (Prop 4.1) |
| P42 | Support-aware certificates: structural lemmas (box/primality tests only above x; integer validity; no monotone fake); reduction to Conjecture SAP | PROVED lemmas; SAP a CONJECTURE (open); fakes and toy LPs EVIDENCE | `POINTWISE_OMEGA17.md` Lemmas 1.2, 1.3, 2.1, 5.1, 5.2 | `reviews/pointwise-omega17-review.md` (no FATAL; two MAJOR handled by restatement) | Harris inequality |
| P43 | **Tail exponent 3 over primes:** `#{p≤x hard: W(p)>T} ≥ π(x)exp(−C(log T)³(log log T)³)` for `log x ≥ C(log T)⁴ log log T`; two-sided with E25 | PROVED modulo the cited theorems | `POINTWISE_TAIL.md` Thms 2.1, 3.3, Cor 2.2 | `reviews/pointwise-tail-review.md` (no FATAL/MAJOR) | (G), Nair–Tenenbaum, OMEGA10 Thm 3.4 |
| P44 | m/n witness modulus: Jacobi criterion m ≡ 0 (4); exponent 1/4 and Haar exponent 3 for m ≡ 0 (4); exponent 1/5 for every m (Type-II-hard primes); ADM_m ⇐ SI | PROVED modulo the cited theorems; 1/4 for m ≢ 0 (4) CONDITIONAL on ADM_m; SI a CONJECTURE | `POINTWISE_MN.md` Lemma 1.1, Thm 3.1, Prop 3.2, Cor 6.1, Thm 5.1; `POINTWISE_MN2.md` Thm 3.1, Prop 5.1 | `reviews/pointwise-mn-review.md`, `-mn2-review.md` (repairs applied) | (G), Nair–Tenenbaum, fundamental lemma, ET (1/5), Henriot (MN2) |
| P45 | Type-I: under H, `C*(r)` = least height of a finite Type-I covering; no certificate with ck ≤ 3·10⁹ at the sign point `x̂_9`, so coverings of `{n_p=7}` have height > 3·10⁹ | Theorem A PROVED (one direction unconditional, equality under H); computation CERTIFIED; sterility open | `POINTWISE_TYPEI2.md` Theorem A, Computation 3.2, Conj 3.4 | `reviews/pointwise-typei2-review.md` (SOUND) | Schinzel H (equality only) |
| P46 | Type-I at `x̂_9`: no certificate with f < 10¹², so coverings of `{n_p=7}` have height > 1.32·10¹² (C(7) > 1.32·10¹² under H); r = 23, 31, 47 > 2.39/2.78/3.42·10¹¹; descent levels 5–6 empty | Lemmas and descent PROVED; searches CERTIFIED; sterility open | `POINTWISE_TYPEI3.md` Lemmas 1.1–1.2, Lemma 5.1–Prop 5.5, Prop 3.1, Remark 4.1 | `reviews/pointwise-typei3-review.md` (no FATAL/MAJOR) | Schinzel H (C(7) bound only) |
| P47 | r = 13: if `(p/13) = −1`, ES holds for prime p outside 6 classes mod 720720 (2 if also `(p/11) = +1`); x* in no ET class of modulus ≤ 10⁶ | Thm 3.1 PROVED by finite computation; Comp 4.1 CERTIFIED; Conj 4.2 (x* sterile) **REFUTED** (P53, ledger (F)11) | `POINTWISE_MORDELL.md` Thm 3.1, Comp 4.1, Conj 4.2 | `reviews/pointwise-mordell-review.md` (no FATAL; two MAJOR repaired) | Elsholtz–Tao Prop 1.9 (certificate classes) |
| P48 | r = 17: ET families reduce to explicit ℤ_17 boxes; levels ≤ 5 leave 67.7% of each non-residue cell uncovered; explicit prime-power count ⇒ sterile point ⇒ no finite polynomial covering of n_p = 17 | Lemmas PROVED; Comp 3.1 CERTIFIED; Thm 4.1 PROVED sufficient condition; Cor 4.2 CONDITIONAL; Conj 4.3 CONJECTURE | `POINTWISE_MORDELL17.md` Lemmas 1.1–1.3, 2.1–2.3, 5.1–5.2, Comp 3.1, Thm 4.1, Cor 4.2 | `reviews/pointwise-mordell17-review.md` (rounds 1–2, no FATAL/MAJOR) | Elsholtz–Tao (families) |
| P49 | m/n, SI localised: class-of-one weights ≤ `2ℓ·U_1(q)`; SI_3 needs only `U_1(q) ≪ q^{−1/2−δ}`; `R(N) ≪ N^{3/5+o(1)}` | PROVED lemmas; SI not proved; (M2) a CONJECTURE; Kloosterman-range obstruction an Assessment | `POINTWISE_MN3.md` Lemmas 1.1, 3.1, 5.2 | `reviews/pointwise-mn3-review.md` (repairs applied) | Elsholtz–Tao Type I count method (Lemma 5.2) |
| P50 | Type-I at `x̂_9`, Pell form: fibre certificates = norm-1 units `16PX² − Q·49^b = 1`, `PQ = d`; finite per (L, b) at all heights; no certificate at `x̂_9` with level ≤ 22 and `v_7(k) ≤ 3` (or ≤ 26, ≤ 1) at any height; fibre inhabited at levels 11, 13, 14, 16, 18–22; L = 7, gap j = 1 excluded for all b | Prop 1.2, Cor 1.4, Lemmas 3.1, 3.6 PROVED; Cor 3.5 and Prop 4.1 CERTIFIED (two complete engines on replayed ranges); Obs 1.5 EVIDENCE; §4 Assessment; sterility open | `POINTWISE_TYPEI4.md` Prop 1.2, Cor 1.4, Lemma 3.1, Cor 3.5, Lemma 3.6, Prop 4.1 | `reviews/pointwise-typei4-review.md` (no FATAL/MAJOR) | none (BHV cited in an Assessment) |
| P51 | Type-I at `x̂_9`, 7-power tower: a solution with u = 7^b is the minimal one (unit `ε_f^k`, k ∈ {1,2,4}), so the d-graded search is complete for all b; at levels 7 ≤ L ≤ 10 a certificate needs `v_7(k) ≥ 8`, `c_oδ > 10⁶` and lies in regime (v); all other regimes excluded for all b | Lemmas 1.1, 3.1 PROVED; Thm 3.7 PROVED + CERTIFIED (two engines); LFL inapplicability an Assessment; sterility open | `POINTWISE_TYPEI5.md` Lemmas 1.1, 3.1, Thm 3.7 | `reviews/pointwise-typei5-review.md` (no FATAL/MAJOR) | none |
| P52 | r = 17, explicit tail: exact four-regime P-enumerator, D_P(13) = 1463; ρ₁ = 16344335/24137569 uncovered through P-level 6; sterile point ⇐ `D_P(K) ≤ C·17^{θK}` (θ = 2/5, C ≤ 1.40) and `D_Q(k) ≤ 17^{3k/5}` | Lemma 2.1, Thm 4.1 PROVED; counts CERTIFIED (two engines, K = 13); Conj 4.2 CONJECTURE; sterility CONDITIONAL | `POINTWISE_MORDELL17B.md` Lemma 2.1, Thm 4.1, Conj 4.2, Lemma 5.1 | `reviews/pointwise-mordell17b-review.md` (one MAJOR rounding error repaired) | Elsholtz–Tao (four-regime cover) |
| P53 | r = 13: x* is **not** sterile (II3 class (8,33,11999), modulus 12670944); {11,13}-generic classes ↔ ES solutions of 4/N, N an {11,13}-unit; x** = x(2,15) in no class within the Comp 5.1 ranges | Thm 3.1 PROVED (refutes MORDELL Conj 4.2, ledger (F)11); Lemmas 1.1–2.4 PROVED; §4 enumeration CERTIFIED (one engine + cross-check); Comp 5.1 CERTIFIED in range; Conj 5.2 CONJECTURE (EVIDENCE only) | `POINTWISE_MORDELL13B.md` Lemmas 1.1–2.4, Thm 3.1, §4, Comp 5.1, Conj 5.2 | `reviews/pointwise-mordell13b-review.md` (no FATAL/MAJOR) | Elsholtz–Tao Prop 1.9 |
| P54 | Type-I at `x̂_9`, regime (v): polynomial fundamental-unit route fails for L >= 7 (no integral norm-1 unit over Q[delta], unbounded CF periods); regime (v) inhabited at L = 13, so closure must use T <= 64; finitely many certificates per level under abc; no certificate at L = 7..10 with v_7(k) <= 15 at any height | Prop 2.1, Lemmas 1.1, 3.1 PROVED; Thm 3.2 CONDITIONAL (abc); Comp 4.1 / Cor 4.2 CERTIFIED (two engines except (L,b) = (9,15), (10,14), (10,15)); §5 model EVIDENCE; sterility open | `POINTWISE_TYPEI6.md` | `reviews/pointwise-typei6-review.md` (no FATAL/MAJOR) | abc (Thm 3.2 only) |
| P55 | r = 13, (p/13) = -1: ES outside 35459 explicit classes (8.42e-5 of the six classes mod 720720); uncovered part of the (2,2) cell mod 11^2 13^2 is {2,57,79} x {15,28,54,132,145}; x** in no P/Q class with e <= 2e9, no I2/II1/I4 class with f, e <= 2e8 | Thm 6.1 PROVED by finite computation (three checkers); Comp 3.1 CERTIFIED; x** ranges CERTIFIED in range (one engine); Conj 5.2 CONJECTURE | `POINTWISE_MORDELL13C.md` Thm 6.1, Comp 3.1, §5 | `reviews/pointwise-mordell13c-review.md` (no FATAL/MAJOR) | Elsholtz-Tao Prop 1.9 |
| P56 | r = 17: cumulative bounds `sum_{13<=K'<=K} D_P(K') <= C*17^{theta K}` suffice (C* = 1.497 at theta = 2/5); Q-points with c >= F^{1/2} unconditional (<= 2 per (a,d)); averaging over K cannot rescue P | Lemma 1.1, Lemma 2.1, Cor 2.2 PROVED; §4 PROVED bullets; sterility CONDITIONAL; Assessment 2.3, §3 Assessment, §4 table EVIDENCE | `POINTWISE_MORDELL17C.md` | `reviews/pointwise-mordell17c-review.md` (minors applied) | none |

---

## 5. Novelty and attribution (from `reviews/novelty-audit-2026-10.md` and `reviews/novelty-audit-2026-10b.md`)

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
  is campaign-defined. For the sub-exponential rates (OMEGA8
  onwards) see the separate audit below.
* *The signed refactor graph and seed-component conjecture.* These are
  elementary; their value is structural, not a priority claim.

**The sub-exponential pointwise machinery** (sources:
`reviews/novelty-audit-omega8.md`, a no-internet audit partly from memory;
the novelty paragraphs of `paper/es-subexp-note.tex` v4–v5 and
`paper/energy-dnf-note.tex`). All searches here were partial.
* *Known, cited, no novelty claimed:*
  * the one-sided ℓ² sandwich of OMEGA8 Lemma 3.1 (Bazzi's scheme in
    Razborov's form, with Wigderson's choice of approximant);
  * the switching-lemma Fourier tail of OMEGA8 Lemma 4.1 (a routine
    adaptation of Linial–Mansour–Nisan and Håstad);
  * the **β-weighted local lemma** (OMEGA13 Lemma 1.1): the asymmetric
    local lemma with the choice `x_E = β^{|supp E|}P(E)`; its conditional
    form is standard (Haeupler–Saha–Srinivasan);
  * the **planting lemma** (OMEGA14 Lemma 1.1): it is the LP dual of
    lower-bound sieves, and laws of the same kind appear in
    Benjamini–Gurel-Gurevich–Peled and Peled–Yadin–Yehudayoff. (Audit
    10b later found that it sharpens BGP's Thm 27; see below.)
* *Apparently new (low-to-medium confidence):*
  * using the sandwich as a sieve minorant transferred to primes, and a
    switching-lemma bound for a covering-avoidance density (the known
    number-theoretic uses of these tools run the other way);
  * the **energy bound C-1** and the DNF tails `W^{>t} ≤ 4·2^{−(t+1)/k}`
    under any product measure (OMEGA10; `paper/energy-dnf-note.tex`).
    Nearest prior art: **Lecomte–Tan** (FOCS 2021), who bound Fourier
    coefficients of a DNF by cover probabilities but still use Håstad for
    the degree; C-1 uses signed covers, all levels at once, and no
    switching lemma. The note claims no priority;
  * the **Janson-type inequality for one-hot product spaces**
    (POINTWISE_HAAR Thm 1.4), where Harris's inequality fails: built from
    the lopsided local lemma and Janson's proof scheme; not found in this
    form, no systematic search, no priority claim.
* The m/n analogues (POINTWISE_TRANSFER) claim no novelty beyond the
  ES-type applications.

**Second audit, 2026-10-05** (`reviews/novelty-audit-2026-10b.md`, task
O70; the OMEGA9–17 / WINDOW / KARY3 round). **No internet in this pass**:
only `sources/`, the earlier audits and the auditor's memory; claims tagged
[memory] may have wrong theorem numbers or years. "Apparently new" is not a
priority certificate; confidence is the auditor's probability that a
specialist search would not find an identical prior statement.
* *Standard / known:* the β-weighted local lemma (high confidence that it
  is not new); large-sieve/Λ² duality (Montgomery 1968, Kobayashi 1973,
  [verify]); `β_κ ≍ κ` sieve limits, Bonferroni achievability and
  Rankin/Λ weights; CEILINGS_UNIFIED Thm 4.1 in substance (PYY/BGP +
  planting + Bonferroni). LS4's coin-coupling bound is the same device as
  Lecomte–Tan Fact 9.
* *Known method, new statement:* the Gallagher linear transfer (packaging
  of Gallagher's proof of Linnik's theorem; the covering-avoidance pipeline
  is new); the Janson-type inequality for one-hot product spaces (must
  check Lu–Székely and Mohr); the typical-size bound (Vaughan's method).
* *Heuristically anticipated:* the Haar exponent 3 (Elsholtz–Tao Remark
  1.2, checked).
* *Apparently new:* the energy bound C-1 (medium) and the constant in the
  DNF tail (low–medium; Lovett–Wu–Zhang 2020 and Håstad 2001 must be
  checked); the planting lemma, which is **stronger than first claimed**:
  it improves Benjamini–Gurel-Gurevich–Peled's Thm 27 upper bound on
  `n_c(k,p)` (removes `log(1/(1−p))` and the prime-power restriction;
  medium–low; later citations of BGP unchecked); the level barrier as a
  sieve/ES statement; the `W(p)` Ω-rates, the 1/4 ceiling and LS ⇒ 1/3
  (high); the ES caps, incl. the all-level large-sieve caps for
  residue-sparse mixtures (high); CEILINGS_UNIFIED's observation that one
  relation gives both ceilings (new as an Assessment-level synthesis); the
  window stacking exponent `1 + J/2` (high). LS (Hypothesis) is a log-scale
  sifted-set analogue of Linnik's theorem, weaker than the
  Granville–Pomerance / Heath-Brown least-prime conjectures; no prior named
  statement known.
* *Recommended wording* (adopted in ledger (D)19 and CEILINGS_UNIFIED §4): call the
  large-sieve duality a minimax form of the classical large sieve–Λ² equivalence, and
  call the 3/4 and 1/4 ceilings instances of the large-dimension sieve
  limit `log D ≍ κ log z`, proved here as barriers for all certificates in
  the stated classes.
* *Not audited by either pass:* EXCEPTIONAL_SPW/SPW2, LARGESIEVE5–7,
  TUPLES2, INTERFREQ2, POINTWISE_OMEGA17, POINTWISE_MN/MN2/MN3, POINTWISE_TAIL,
  POINTWISE_TYPEI2/TYPEI3/TYPEI4, POINTWISE_WINDOW3, EXCEPTIONAL_WEIGHTS/WEIGHTS2,
  EXCEPTIONAL_SHORT, EXCEPTIONAL_MN, POINTWISE_TYPEI5, POINTWISE_MORDELL,
  POINTWISE_MORDELL13B, POINTWISE_MORDELL17 and POINTWISE_MORDELL17B.

**Other attribution notes:**
* Theorem W1 is also implied by Fuchs–Hsu–Rickards–Schindler–Stange 2025
  Thm 1.1(2).
* Theorem W2 is a Friedlander–Iwaniec (2009) type theorem.
* POINTWISE_XWIN Thm 2.2 (window tail) re-proves what notes Thms
  14.4/14.9 already imply; priority to the notes.
* POINTWISE_MORDELL Thm 3.1 (r = 13) is an explicit packaging of the
  Salez/ET level sieve; Salez's data already give a mod-120120 analogue
  (modest novelty, per its review).
* The GRH part of POINTWISE_TYPEI (Thm 3.1) is Montgomery's Ω-result for
  the least non-residue, transported (sources cited from memory).
* Audit 10b covers KARY3, LARGESIEVE–LS4, CEILINGS_UNIFIED, XWIN and
  WINDOW2; the files listed at the end of the 10b block above, and
  POINTWISE_TYPEI, have not been separately novelty-audited.
* Related recent work that the campaign compares against:
  Pomerance–Weingartner (arXiv:2511.16817; an explicit-in-`m` Vaughan
  bound) and Dahan (arXiv:2608.24035). Dahan's Thm 4.17 is credited as an
  independent antecedent of the cubic exponent shape, for a different,
  ineffective statistic.

---

## 6. Open problems, ranked

Importance (I) and feasibility (F) are rated high / medium / low. These
ratings are this summary's judgement, not ledger labels.

1. **External refereeing.** (I high, F high.) Nothing is externally
   refereed. First the 3/4 note (only INTERNALLY PROVED; the cubic
   witness tail (A)9 and the CEILINGS_UNIFIED bounds now also rest on it)
   and the 2/3-loglog note (`paper/README.md` recommends showing the
   loglog note to a human referee first); then the sieve-limits note v5,
   the subexp note v6, the window note and the
   energy/DNF note. Related tasks: read Vaughan 1970 itself and complete
   the priority searches (§5).
2. **θ > 3/4 for `E(N)`.** (I high, F low.) The cap is now exactly
   `(log N)^{3/4}` for coefficient-sum sieves, every Bessel-type large
   sieve (at every frequency level for one-rough-prime and residue-sparse
   mixtures), prime-only majorants and interval cancellation at moduli
   `≤ N/2` (§§2.2–2.3). A new ingredient is required (§2.4). Two kinds of
   question remain.
   * *Opening* questions (would give θ > 3/4 if true):
     **TC^alt_θ for θ > 3/4** ((D)23, CONJECTURE), alternating witness
     correlations of growing order, needing accuracy at moduli
     `exp(c(log N)^{3θ/2})`, beyond any known theorem; other genuinely
     non-CRT input.
   * *Closing* questions (would extend the cap; a counterexample would
     open a door): **(A*) / (DCC) / (RD′)** for residue-dense multi-rough
     classes ((D)28 follow-ups; the most concrete: (RD) is proved at one
     prime for ℛ(M) and for long cofactors, and short cofactors and the
     (a,D)/Case-A classes are what is left); **weak SPW** for hybrids
     ((D)26; requirement exact, `log(K/η) = O((log N)^{3/4})`);
     **(W_𝔊)** for per-frequency weights below 1 ((D)29: for Selberg's
     window the door is capped at 3/4 iff the shift-uniform avoider count
     satisfies `M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}`; WEIGHTS2: neither proved
     nor refuted, the CRT-alignment plan fails, and for prime slices it is a
     growing-dimension Hensley–Richards attainment question).
3. **The pointwise exponent 1/3.** (I medium–high, F low.) The proved
   rate is `log W ≫ (log p)^{1/4}` up to logs; the Haar exponent and the
   tail exponent over primes are both 3 (§3.3); 1/4 is the ceiling of the
   Haar-minorant architecture and, by the Wiener-norm barrier, of every
   full-orbit uniform linear certificate, for which GRH/EH-type prime
   input is irrelevant. Routes, in order:
   * prove the CONJECTURE **LS** ("Linnik for sifted sets"), which gives
     1/3 (PROVED implication, (H)30), or any special case strong enough
     for the ES system;
   * **support-aware certificates**: decide **Conjecture SAP** ((H)31); if
     true, 1/4 is also the ceiling of LP-relaxed support-aware
     certificates with unconditional-type information, and only
     size-localised counts, Type II input or non-linear methods remain;
   * smaller tasks: remove the `(log log p)^{1/4}` gap to the ceiling and
     the `(log log T)³` factor in the tail; close the `(log 𝓛)^5` gap in
     the Haar exponent; m/n with m ≢ 0 (4) at exponent 1/4 (prove SI,
     (H)32; POINTWISE_MN3 localises the failure to a Kloosterman-range
     residual and the second moment (M2), a CONJECTURE).
4. **A pointwise route via (E1) or (E2).** (I very high, F low.) The
   natural target is X_win(C), i.e. `a_min(p) ≪ log p` (§3.4). It sits
   just above the formal-obstruction scale. Lemma 9.1 (PROVED) gives
   ES ⇐ X_QNR (least-non-residue seeding), an (E2)-type reduction. Whether
   fixed non-abelian Frobenius data (E3) escapes the obstruction is open.
   No "ES ⇐ standard hypothesis" was found ((H)18).
5. **Unconditional `a_min(p) ≥ 11` (or `a_min → ∞`).** (I medium,
   F low.) Parity input is provably necessary (Thm P1), and in the
   discrete model Type-I plus parity at BV level is not enough (§3.4). In
   the faithful model of POINTWISE_WINDOW3 (EVIDENCE/Assessment), Chen-type
   switching works only with switched bounds within ≈ 2–2.5 of the truth,
   against ≥ 3.9 for the best known constants at BV level: a precise
   numerical gap. This is the window analogue of
   the open unconditional case of Friedlander–Iwaniec 2009.
6. **Type-I: `ck_min ≥ g(p)·n_p` with `g → ∞`.** (I low–medium, F low.)
   Congruence input gives exactly `g = 1` (§3.3); beating
   `log p·log₃p` by congruences would beat known Ω-results for the least
   non-residue. Whether `C(7) < ∞` is open: every finite Type-I covering
   of `{n_p = 7}` has height > 1.32·10¹² (CERTIFIED, POINTWISE_TYPEI3), and
   under H, `C*(r) = ∞` iff a sterile profinite point exists (TYPEI2
   Thm A); the sign point `x̂_9` is the candidate (Conjecture 3.4; descent
   levels 5–6 empty; TYPEI4: no certificate at level ≤ 22 with `v_7(k) ≤ 3` at
   any height, CERTIFIED; the open part is the 7-adic tower `v_7(k) → ∞` at
   levels 7–10, an exponential-Diophantine problem; TYPEI5: there a certificate
   needs `v_7(k) ≥ 8` and lies in one two-parameter regime). Analogous candidate
   sterile points for Mordell-type coverings: x** = x(2,15) for r = 13
   (MORDELL13B Conj 5.2; the earlier candidate x*, Conj 4.2, is REFUTED,
   ledger (F)11) and r = 17
   (Conj 4.3, reduced by MORDELL17 Thm 4.1 to an explicit prime-power
   count `#{(a,b): ab ≤ 17^K, (−17^K mod 4ab) | a+b} ≤ C·17^{(1/2−δ)K}`;
   MORDELL17B Thm 4.1: ET's exponent 2/5 with an explicit constant below 1.4097
   and no o(1) would suffice).
   No sterile point is proved. A proved one would give `C(7) = ∞` under H
   (for `x̂_9`), or show that no finite set of polynomial ES identities
   covers the corresponding primes (r = 13, 17).
7. **An unconditional sterile seed component.** (I low–medium, F low.)
   Astra has reduced its hypothesis to 158 prime conditions plus one
   divisor condition; searches over actual inputs find no sterile prime.
   Note: settling this would not affect ES.
8. **Residual cap questions that do not move 3/4:** the (D)21 Cor 3.4
   window for general class order ((D)24 closes it for prime order);
   right-signed hybrid mass at moduli in `(N, CN]`; composite Gallagher kernels with huge `Nh/(W_K−h)`; majorants with
   `ν ≥ 0` only at primes `≤ N`; B-removal for general majorants over
   classes outside ℛ(M). (I low, F medium.)
9. **Open hypotheses kept in the ledger** (section (E)): `H_kBV(κ)`,
   `H_FAIL`, `H_STACK`, `H_BLK`/`H'_BLK`, `H^+_LT` and `H_PF'`. Also open:
   the replacement conjecture `C'_SQ` (`W = +∞` exactly for squares and
   three sporadic values; ledger (F)9) and `C_POLY`. (I low–medium,
   F varies.) Most of these belong to the a-frame/stacking route, whose
   model ceiling is below 3/4.
10. **Novelty checks that need library or internet access.** (I medium for
    publication, F high with access.) Mádi-Nagy–Prékopa 2004, Selberg's
    large-κ remarks, *Opera de Cribro* Ch. 7 and 11, Graham–Ringrose 1990,
    Vaughan 1970; for the pointwise machinery, Bazzi/Razborov/Braverman,
    LMN/Håstad sharpenings, Fourier-growth literature (for C-1), and
    Janson-type inequalities without Harris; Gallagher 1970 itself (only
    the MV III draft was read). Audit 10b's must-checks, in order:
    Lu–Székely and Mohr (Janson-type inequality), Lovett–Wu–Zhang 2020 and
    Håstad 2001 (DNF tail constant), citations of BGP arXiv:1201.3261
    (planting lemma), CHHL/KLLM (C-1), Montgomery 1968 / Kobayashi 1973
    (large-sieve duality). The files not covered by either audit (§5)
    need a first pass.
11. **Administrative.** Settle authorship and the citation form for astra
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
| why 3/4 is sharp for congruence sieves | `paper/sieve-limits-note.tex` (v5); then `EXCEPTIONAL_KARY3.md`, `EXCEPTIONAL_KARY2.md`, `EXCEPTIONAL_KARY.md` |
| the sieve-limit theorem and the Rankin functional | `EXCEPTIONAL_THETA.md` §§0–3 |
| the Λ² route with twin and r-prime moduli | `EXCEPTIONAL_TWIN.md` → `TWIN2` → `TWIN3` → `TWIN4` |
| non-CRT inputs, rounding, prime-only majorants | `EXCEPTIONAL_NONCRT.md` |
| per-frequency weights below 1, reduced to the avoider count (W_𝔊) | `EXCEPTIONAL_WEIGHTS.md`, then `EXCEPTIONAL_WEIGHTS2.md` (why CRT alignment fails) |
| the 3/4 bound in short intervals and progressions | `EXCEPTIONAL_SHORT.md` |
| the 3/4 bound for m/n, uniformly in m | `EXCEPTIONAL_MN.md` |
| the large sieve over forced-class mixtures | `EXCEPTIONAL_LARGESIEVE.md`, then `EXCEPTIONAL_LARGESIEVE2.md` (twisted/hybrid forms, larger sieve, band-family escape) |
| large sieves at every frequency level; what is left ((A*), (DCC), (RD′)) | `EXCEPTIONAL_LARGESIEVE3.md` (smooth–rough splitting), `EXCEPTIONAL_LARGESIEVE4.md` (residue-sparse cap), then `LARGESIEVE5` → `LARGESIEVE6` → `LARGESIEVE7` |
| prime-only majorants for all mixtures | `EXCEPTIONAL_PRIMELAW.md` |
| inter-frequency cancellation in interval counts | `EXCEPTIONAL_INTERFREQ.md` |
| hybrid methods, SPW and its refutation | `EXCEPTIONAL_INTERFREQ2.md`, `EXCEPTIONAL_SPW.md`, `EXCEPTIONAL_SPW2.md` (exact weak-SPW requirement) |
| the tuple-count door TC_θ and witness correlations | `EXCEPTIONAL_TUPLES.md`, then `EXCEPTIONAL_TUPLES2.md` (forced zeros, TC^alt) |
| the signed graph, basics | `SIGNED_REFACTOR.md`, `POINTWISE.md` |
| short escapes and exceptional sets for the seed distance | `DEPTH3.md` |
| Theorem F and its certificate | `FORMAL_CLOSURE.md`, `data/formal_closure/`, `scripts/formal2_verify.py` |
| the pointwise programme's obstruction, written up | `paper/pointwise-obstruction.tex` |
| the meta-theorem (Theorems M, C, Proposition A) and the window frame | `POINTWISE_SIZE.md` §§0–4, §8 |
| `W(p)` Ω-results, current (exponent 1/4, Haar exponent 3, the 1/4 ceiling) | `paper/es-subexp-note.tex` (v6); then `POINTWISE_OMEGA13.md`, `POINTWISE_HAAR.md`, `POINTWISE_OMEGA14.md` |
| the typical size of `W` and its tail exponent 3 over primes | `CEILINGS_UNIFIED.md` Thm 2.1 (upper), `POINTWISE_TAIL.md` (lower, two-sided Cor 2.2) |
| barriers beyond 1/4, and what would give 1/3 | `POINTWISE_OMEGA15.md` (Wiener-norm barrier), `POINTWISE_OMEGA16.md` (LS ⇒ 1/3), `POINTWISE_OMEGA17.md` (support-aware certificates, SAP) |
| one sieve limit behind the 3/4 cap and the 1/4 ceiling | `CEILINGS_UNIFIED.md`; `paper/sieve-limits-note.tex` v5 §18 |
| how the rate got there (1/14 → 1/7 → 1/6 → 1/5) | `POINTWISE_OMEGA8.md` → `OMEGA9` → `OMEGA11` → `OMEGA12` |
| the energy bound C-1 and DNF Fourier tails | `paper/energy-dnf-note.tex`; `POINTWISE_OMEGA10.md` |
| an abstract avoidance transfer; m/n analogues | `POINTWISE_TRANSFER.md`, then `POINTWISE_MN.md`, `POINTWISE_MN2.md`, `POINTWISE_MN3.md` (where SI fails) |
| `W(p)` Ω-results, polylogarithmic (every fixed exponent) | `paper/es-omega-note.tex`; then `POINTWISE_OMEGA.md` → `OMEGA2` → `OMEGA3` |
| the explicit polylog rate and the (superseded) hub route | `POINTWISE_OMEGA4.md`, `POINTWISE_OMEGA5.md`, `POINTWISE_OMEGA6.md` (`POINTWISE_OMEGA7.md` archived, unreviewed) |
| the Type-I slice parameter `ck_min` | `POINTWISE_TYPEI.md`, `POINTWISE_TYPEI2.md`, `POINTWISE_TYPEI3.md` (search to f < 10¹², descent), `POINTWISE_TYPEI4.md` (Pell form, any-height bound), `POINTWISE_TYPEI5.md` (7-power tower) |
| finite coverings mod a further prime r; candidate sterile points | `POINTWISE_MORDELL.md`, `POINTWISE_MORDELL13B.md` (r = 13; x* refuted, candidate x**), `POINTWISE_MORDELL17.md`, `POINTWISE_MORDELL17B.md` (r = 17); `paper/es-coverings-note` (refereed internally, R86) |
| the window statistic `a_min` | `paper/es-window-note.tex`; then `POINTWISE_WINDOW.md`, `POINTWISE_XWIN.md` (stacking orders), `POINTWISE_WINDOW2.md` (parity), `POINTWISE_WINDOW3.md` (faithful model) |
| what is known in the literature, and claimed proofs | `LITERATURE_2026.md` |
| priority and attribution | `reviews/novelty-audit-2026-10.md`, `reviews/novelty-audit-2026-10b.md`, `reviews/novelty-audit-omega8.md`, `reviews/lit-audit-*.md` |
| the status of each paper draft and its referee rounds | `paper/README.md` |
| what each review found | `reviews/` (file names in §4 above) |
| per-task agent reports | `reviews/agent-reports/`, `UNIT_REPORT*.md` |
| the companion signed-seed counterexample | `../erdos-straus-astra` (read-only): `SIGNED_SEED_COUNTEREXAMPLE.md`, `PRIMARY_SEED_PACKET.md` |

Suggested order for a newcomer:
1. §1 of this file.
2. `STATUS.md`.
3. The abstracts of the papers in `paper/` (status in `paper/README.md`).
4. `DISCOVERIES.md` sections (D) and (H).
5. Whichever line interests you, via the table above.
