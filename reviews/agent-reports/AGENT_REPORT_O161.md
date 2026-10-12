# AGENT REPORT O161: function-field Erdős–Straus landscape (checkpoint 1)

Branch `side-agent/ff-landscape`. Main file `FUNCTIONFIELD_ES.md`. Scripts `scripts/ffl_es.c` (engine),
`ffl_brute.py` (independent brute force), `ffl_cover.c` / `ffl_tree.c` (finite coverings), `ffl_jacobi_check.py`,
`ffl_fit.py`, `ffl_grid.sh`, `ffl_q2_batch.sh`. Data in `data/ffl/` (`grid.txt`, `q2_batch.txt`,
`cover_q4_A10.txt`, `fail_*.txt`). ES over Z is untouched. Everything below is about F_q[T].

## Answers to the brief's questions

**(1) The analogue.** Monic A of degree k ≥ 1. Monic X, Y, Z with every deg ≥ n − k ("no cancellation at ∞",
the ultrametric image of x_i > n/4). Lemma 1.2 (PROVED): in char ≥ 5 monic already forces NC; (R161 repair) the same holds in char 3, since P divides some denominator and so m = 3
cancellation is impossible. (Superseded wording: "In char 3, NC holds
once one denominator has degree n − k.") (R161 repair: cancellation is possible only in char 2, with m = 2, e.g.
T/P = 1/T + 1/(T+1) + 1/(P(T^2+T)) with P = T^3+T^2+1; triage B's "char 2 and 3" was too broad.) The e-slice criterion (Lemma 1.3) holds in all characteristics. Prop 1.4
(PROVED): the classes P ≡ −1, −2 (mod A) are always solvable, so q = 2, 3 with A = T are trivial (all
P(0) ∈ {−1, −2}). Without a sign condition, k = 1 is trivial.

**(2) Landscape at fixed q (EVIDENCE, exhaustive, exact).** In every case computed, no failure occurs beyond
a finite degree within the computed range (R161 repair: formerly "failures die out"):
* A = T: q = 5 last failure at n = 4 (none for n = 5..12, 20.3M P at n = 12); q = 7 at n = 6 (none at 7, 8);
  q = 4 never fails (n ≤ 13).
* A = T²: q = 3 last at n = 5 (none for n = 6..15); q = 4 last at n = 7 (none for 8..11); q = 5 still 15/48750 at
  n = 8 (n ≥ 9 running).
* Counts: q^k·mean N_II/n³ is independent of q at fixed n (±3%, q = 4, 5, 7) and ≈ 0.25–0.5, slowly
  decreasing. So **mean ≈ C·n³/q^k**, the analogue of log³p. The zero-probability is overdispersed:
  P(N_II = 0) ≈ exp(−θ·mean) with θ ≈ 0.25.
* **Two thresholds (Assessment):** bulk transition n_{1/2} ≍ q^{k/3} (below it almost all P fail; this is O140
  Thm 2.1's regime), and extinction n₀ ≍ q^{k/2}(log q)^{1/2}. The N_II = 0 version predicts 9.4 at q = 5;
  observed 9. Full failures: n₀ ≈ 1.5(q log q)^{1/2}, calibrated on q = 5, 7. The q = 4, A = T² case
  (predicted ≈ 7.1, observed last failure 7) is a check. **Recorded predictions** for A = T, q = 8, 9, 11, 13:
  n₀ ≈ 6, 7, 8, 9. Those runs are queued (chain5) and were not yet available at this checkpoint.

**(3) Obstruction structure.** Prop 4.1 (PROVED, numerically checked on 3953 Type II data): every Type II
class satisfies (P/f) = (−1)^{((q−1)/2)((1+deg f)(1+deg Ad)−1)}. Over Z the sign is rigidly −1, which is the
odd-square obstruction. Over F_q[T] it is +1 for q ≡ 1 (mod 4), and for q ≡ 3 (mod 4) it depends on degree
parity. (R161 repair, rescoped:) PROVED for odd q: squares are never excluded by the Type II sign condition, so the
Mordell square-class argument has no analogue. Assessment: no quadratic-residue obstruction. Char 2 is not
addressed by Prop 4.1, and the size class still obstructs linear coverings in char 5 and higher. What remains:
(i) the size class P ≡ 1 (mod A): all N_II = 0 cases at q = 5, n ≥ 8 have P(0) = 1;
(ii) a mild quadratic tilt toward (−AP/ℓ) = +1, about 5–15% per degree-1 ℓ (Z: ×14).
(R161 repair: the former "there is no q with an obstruction class" is withdrawn as ill-defined; see the rescoped
statement above and FUNCTIONFIELD_ES.md section 4.)

**(4) Provable statements.**
* **Thm 5.3 (PROVED, given the standard Weil/RH prime-polynomial theorem in progressions, cited from Rosen
  Ch. 4 from memory; R161 repair: re-derived by R161 from Weil with the proviso D at most q^{n/2}, and the
  Chebyshev error bookkeeping is made explicit, exponentially small):** at fixed q and any A, the failure proportion at degree n is ≤ (Φ(A) + o(1))/log n → 0.
  Method: second moment over the single family "P + 1 has a prime factor g ≡ −(P+1)/h (mod A)", with the
  identity A/P = 1/(hgd) + 1/(dP) + 1/(hgdP). This is the rigorous counterpart of O140 Thm 2.1 (proportion → 1
  as q → ∞). It is the classical almost-all mechanism and says nothing about every P.
* **Small characteristic: the conjecture is a THEOREM in several cases** (computer-assisted finite coverings
  plus exhaustive small degrees; Lemma 6.2 PROVED: validity of a linear family depends only on P mod W_F
  for n ≥ n_F).
  * Thm 6.1 (pure proof): over F₂, A = T², every P. Identity T²/P = 1/R + 1/(cP) + 1/(cRP) with
    R = (P+T+1)/T² and c = (R+1)/(T+1).
  * Thm 6.3: over F₄, A = T, every P. The 81 unit classes mod T⁴ − T are covered (certificate file; R161 repair: independently re-verified by R161, max n_F = 4).
  * Thm 6.4: over F₂, every A of degree 2, 3, and A = T^4, T^4+1 (R161 repair: scoped to cases with archived, independently checked
    certificates; deg 4 uses R161's `data/ffl/cover_q2_A1000{0,1}_R161.txt`). The other 14 degree-4 A and all
    32 degree-5 A are NOT covered yet. The batch over the
    remaining degree-4/5 A was still running; a `q2_batch.txt` line counts only as EVIDENCE until its leaf list
    is archived and checked (R161 repair).
  **Mechanism (why it does not transfer):** (a) in char 2/3 the size-obstructed class P ≡ 1 coincides with the
  trivially solvable class −1 resp. −2. (b) T^q − T confines irreducible P to (F_q^*)^q classes (a single class
  for q = 2). (c) The square obstruction is absent (§4). Over Z all three fail. In char ≥ 5 O140 Prop 4.1
  forbids finite (linear) coverings, so there ES_q(A) for large n is a pure lottery: the data say failures go
  extinct, but there is no proof mechanism. No Frobenius/additive-polynomial identity is needed or found. The
  "char-p input" is exactly (a) + (b).
  * Open: q = 3, A = T² (the tree stalls at uncovered density ≈ 1.1%; no known obstruction) and q = 4, A = T².

## Validation done
* ffl_es vs the independent brute force: identical N(P) for every irreducible P in 15 (q, A, n) cases, including
  char 2/3 and A of degree 1–3.
* O140's A = T table is reproduced exactly.
* The global Type II count agrees with the per-P recount on all samples.
* Every covering leaf is re-verified on random P by the direct identity A·XYZ = P(XY+YZ+ZX) (monic, NC). For
  q = 4: 8100 checks, 0 failures.

## Caveats / what a hostile reviewer should check
* Thm 5.3's error terms use Fact 5.2 with constant (D + 2)q^{n/2}/n from memory. Any O_D(q^{n/2}) version suffices.
* Thms 6.3/6.4 depend on the correctness of ffl_tree.c's family test. Mitigation: independent identity
  verification of each leaf family. Lemma 6.2's degree-coincidence bookkeeping should be re-read.
* §7 thresholds are a fitted heuristic (Assessment). The q = 8..13 predictions are the falsifiable part.
* Background jobs still running at the time of writing (≤ 2 cores): chain4 (q = 5, 7 with A = T²; q = 5 with
  A = T²+2), the F₂ degree-4/5 batch, then chain5 (q = 8, 9, 11, 13 with A = T).

## Suggested next steps
Fill in the q = 8..13 extinction data against the predictions. Finish the F₂ batch, and try to *prove* ES₂(A)
for all A (a general F₂ construction?). Decide q = 3, A = T² (deeper tree / larger NTH using the exhaustive data
to n = 15). Write a DISCOVERIES entry once reviewed.
