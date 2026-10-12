# Brainstorm memo: adversarial hard primes, stacking the known drivers (O154(a))

Labels as in DISCOVERIES.md. ES is not solved, and nothing here proves any case of it. Every number below is
**EVIDENCE** (finite computation; every reported prime has an explicit, exactly verified solution) or an
**Assessment** (heuristic). *Draft: sections are filled in as the experiments finish.*

## 1. Idea

The barriers are symmetric: a sterile prime would be invisible to every encoding. So run the disproof direction as
a stress test. Build primes that stack every known hardness driver at once, at sizes 10¹²–10¹⁶, and measure the
exact Type II count `f_II(p)` against the lottery model of `prob_lottery_model.md` (O142). The drivers are:

* **D1, square classes.** `p` is a quadratic residue mod every small prime. The extreme case is `p ≡ 1 (mod Q)`.
* **D2, divisible `p − 1`.** Every `f | p − 1` is a dead Type II witness modulus (redteam Lemma 3.1). Here f is
  the witness `f = 4acd − 1 | p + 4a²d`, and the small-f solutions are exactly the solutions with large slice
  parameter `e = (p + 4a²d)/f ≈ p/f`.
* **D3, near-prime shifts.** `N_e = (p+e)/4` is prime, or has few factors, for small e. Then `X_e(p) = 0` in
  the e-slice form (LONGSHOT_PIGEONHOLE Lemma 1.1).

What would count as a finding:
* (α) the model-predicted `f(p)` drops below 1 at a reachable size while solutions still exist. That would mean the
  model misses a positive force (an H-A/H-E signal);
* (β) the counts track the model. Then we can quantify how far away a counterexample would have to be;
* (γ) any prime with no solution. Triple-check before saying anything.

## 2. Literature anchor

* Elsholtz–Tao 2013 (J. Aust. Math. Soc. 94): average `Σ_{p≤N} f(p) ≍ N log²N` up to `log log`. The campaign
  sharpened the Type I part to `≪ N log²N` ((D)32b). The pointwise upper bound is `f(p) ≪ p^{3/5+o(1)}`. These are
  as quoted in the ledger; I did not re-verify them against the paper.
* Salez, arXiv:1406.6307: ES is verified to 10¹⁷ by modular filters (cited in LITERATURE_2026.md). So no
  counterexample below 10¹⁷ can exist. The purpose here is the *count*, not existence.
* Campaign: the redteam-automorphic §3.2 model test at the "class of one" (`p ≡ 1` mod all primes ≤ 97,
  p ≈ 10⁴⁰). There the truncated witness count `N_T` (T = 2·10⁵) dropped by about 30% against controls, with W(p)
  up to 251. X5 / Prop 2.3 gives `N_T(p) = 0` with `log T ≍ (log p)^{1/4}` on fibres of size `log Q ≍ 𝓛⁴`. Those
  fibres are not computable.

## 3. Tools (validated)

* `scripts/bs_adv_count.c` computes the **exact** `f_II(p)` at a single prime `p < 2⁶²`, with the convention of
  `bs_prob_fII.c`. It splits at E:
  * slices `e ≤ E`: `N_e` are consecutive integers, so it uses a segmented sieve;
  * `e > E`: then the witness satisfies `f < 2p/E + 1`, by `4a²d ≤ 4abd = p+e`, and a (a,d,c) loop finishes.

  Validation: it agrees with the 10⁸ dump on 400 random primes, with random split points
  (`scripts/bs_adv_validate.py`: 0 mismatches). Run times: 2 s at 10¹², 20 s at 10¹⁴.
* `scripts/bs_adv_construct.c` builds primes `p ≡ r (mod M)` with prescribed prime shifts.
* `scripts/bs_adv_scan.c` is a selection scan for the exact small-slice mass `Σ_{e≤E₀} X_e`.
* `scripts/bs_adv_run.py` is the driver. For every prime it checks `4/p = 1/(abd) + 1/(acdp) + 1/(bcdp)` exactly
  for the reported solution. Logs go to `logs/bs_adv_*.jsonl`.
