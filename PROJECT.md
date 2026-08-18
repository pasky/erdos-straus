# Project: explicit-k correlation bounds → Erdős–Straus exceptional set

Successor session to the campaign logged in `notes.md` (read it first, §3, §6,
§8.3, §11 are the load-bearing sections; `verify.py` re-checks every claim in
~2 s). Goal: execute the one actionable lever found there.

## The target

Prove an exceptional-set bound for the Erdős–Straus conjecture of the form

    #{p ≤ N prime : 4/p has no representation} ≪ N·exp(−c(log N)^θ)

by the criterion route (notes.md Thm 3.1), with the explicit ambition θ > 2/3
(beating Vaughan 1970) and the realistic fallback of any exp-type saving
derived independently of Vaughan's method.

## The plan (phases; each is standalone publishable-progress if it works)

**Phase 1 — explicit-k mean-value bounds for indicator slices (rigorous
target).** The stackable conditions: for each modulus w ≡ 3 (mod 4) and each
of the two criterion halves, a counterexample p forces the shifted value
((p+w)/4 resp. (pw+1)/4) to have NO prime factor in specified residue classes
mod w (the −1 and −x classes, when distinct; for w = 3 and some Case-B
classes they coincide; see notes §8.3, §11.3). These necessary slices are
multiplicative 0/1-indicator conditions on k
coprime linear forms in p. Needed: a k-fold Shiu/Nair–Tenenbaum-type upper
bound with constant C(k) explicit and subexponential in k. Key simplification
vs the general machinery (sources/henriot-1102.1643.pdf, which states
Nair–Tenenbaum Thm 1 and Holowinsky Thm 2): our functions are 0/1 indicators,
f(p^ℓ) ≤ 1, product structure across forms — the full M_k(A,B,ε) generality
is not needed and a direct sieve/Halász-style argument may give good
k-dependence cheaply. Warning from notes §11.3: prime moduli alone contribute
∑ 2/(w−1) ≈ log log W. Section 12's completed direct sieve also admits all
composite w≡3 (mod 4), raising the cumulative density to ≫log W and proving
the unconditional bound N·exp(−c(log log N)²). This remains superlogarithmic,
not a positive power of log N, so it cannot reach θ = 2/3.

**Phase 2 — capture the full per-modulus condition (the prize).** Full failure
at modulus w is subset-product avoidance: no product of prime factors of x
(exponents ≤ 2eᵢ) lands in the coset −x (mod w). Empirically this fails with
probability ≈ 0.3–0.7 per modulus, roughly independently across moduli and
halves (measured: notes §11.1), for w up to the divisor-richness threshold
≈ (log p)^{1.1}. Task: prove per-modulus failure probability ≤ ρ < 1 *on
average over p* for w ≤ (log N)^{1−ε}, e.g. via large-deviation/moment
control of the vector of class-counts of prime factors of the shifted values
(multidimensional Selberg–Delange / Halász), then stack with Phase-1-style
explicit-k control. Success here gives θ near 1 — beating Vaughan.

**Phase 3 — write-up.** Compare against Vaughan 1970's actual argument
(obtain the paper); be scrupulous about what is genuinely new. House rules:
no overclaiming — "verified numerically" ≠ "proved"; every analytic step
either proved or cited to a checked source; extend `verify.py` with numerical
sanity checks for each new lemma (e.g. simulate Phase-2 class-count
large-deviations against actual data for hard-class primes).

## Assets

* `notes.md` — full campaign: criterion (Thm 3.1, proved), obstruction
  theorems (5.1, 9.3), reciprocity collapse (8.1/9.1), one-bit completeness
  (§10.2), independence data + joint record (§11.1), calibration (§11.3).
* `verify.py` — 2-second re-verification of all computational claims.
* `sources/henriot-1102.1643.pdf` — Henriot, NT bounds uniform in
  discriminant (quotes NT Thm 1, Holowinsky Thm 2 — the pair-case tools).
* `sources/bright-loughran-1908.02526.pdf` — geometry side (context only).
* `sources/nair-tenenbaum-1998.pdf`, `sources/shiu-1980.pdf` — originals.
* `sources/pomerance-weingartner-2025.pdf` — a modern proof explicitly following
  Vaughan's inaccessible 1970 paper; §4 gives the large-sieve argument.
* Still wanted: Vaughan 1970 itself (publisher page found; PDF access blocked).

## Known traps (paid for already, don't re-pay)

* The full failure condition is NOT a multiplicative indicator. Conditioning
  on p mod 4w fixes the target coset but does **not** make subset-product
  avoidance multiplicative (e.g. modulo 7, target −1: 8 and 15 each avoid it,
  while 120 does not). Only the necessary prime-class slices are multiplicative.
* Prime and near-prime x are provably useless (notes §8.3) — smoothness/many-
  factor x carry everything; don't waste effort on sparse-divisor slices.
* Identity/covering/form shortcuts are dead by theorem (notes §5, §9.3);
  don't rediscover them.
* GRH and Schinzel H do not shortcut Phase 2 (notes §10.5).

## Outcome 2 (2026-08-18, phase six — see notes.md §13)

* **Positive power achieved unconditionally (fallback prize):**
  E(N) ≤ N exp(−(log N)^{1/8}) for large N (Theorem 13.2).  Method:
  Lemma 12.4's Fourier bound discretized into hard level-set factor-count
  thresholds (Lemma 13.1), conditioned on exceptional factor patterns, and
  fed to the many-root sieve with an explicit Poisson–Chernoff/character
  union cost; a finite rate certificate (verify.py (h)) closes the
  arithmetic.  Criterion-native, keeps primality, independent of Vaughan’s
  construction — but still **weaker than Vaughan’s 2/3**; not a record.
* **Ceilings computed (§13.3):** the fully optimized version of this route
  caps at θ < γ* ≈ 0.207 (numerical estimate); any route through the first-moment pigeonhole
  (12.11) caps at θ < log 3/2 ≈ 0.549; Vaughan’s outer argument caps at
  θ = A/(A+1) with A = 2 the divisor-density of identity classes, i.e. 2/3.
  Beating 2/3 therefore needs the second-moment transfer, not more of this.
* **Unconditioned halves of the gap now proved (§13.4, Lemmas 13.3–13.5,
  Cor 13.6):** Pólya–Vinogradov character-average lemma; first-moment
  asymptotic li(N)·c_w·(log N)/h for divisor witnesses along the actual
  shifted primes (Bombieri–Vinogradov, level N^{1/4}); second-moment upper
  bound N(log N)²/h² (Brun–Titchmarsh); hence success ≫ li(N)/log N per
  modulus, uniformly for w ≤ (log N)^{1−ε}.  The lost 1/log N is exactly
  divisor over-dispersion — the ω-conditioning is the sole remaining
  analytic input.
* **Gap sharpened (§13.4):** the §12.5 demand (growing-order marked
  Sathe–Selberg) is reduced to two fixed-order hypotheses H1/H2 (BV-average
  ω-conditioned divisor correlations along the shifted forms) plus a
  w-joint version H3; together they would give every θ < 1.  The naive
  moment transfer is blocked by an elementary k!-vs-BV multiplicity
  accounting (back-of-envelope obstruction, not a nonexistence theorem);
  unconditioned Paley–Zygmund is blocked by divisor over-dispersion.
  H1–H3 are the sharpest currently-identified missing inputs; proving
  them is the successor project.

## Outcome (2026-08-17)

* **Phase 1 completed:** Lemma 12.1 is a direct many-root large sieve with
  absolute constant 4 and no hidden k-dependence. Applied to both criterion
  halves, all moduli w≡3 (mod 4) up to δ log N (prime and composite), and the
  prime affine form itself, it independently proves
  E(N)≪N exp(−c(log log N)²) (Theorem 12.2). The method is criterion-native;
  the bound is weaker than Vaughan's known theorem and is not a literature
  record.
* **Phase 2 reduced but not solved:** Lemmas 12.3–12.4 give the exact signed
  subset-product and Fourier large-deviation formulations; Lemma 12.5 proves
  success with probability 1−o(1) in the independent uniform-residue model
  throughout w≤(log N)^{1−ε}. The missing input is a growing-order,
  residue-marked factor-count theorem along a prime affine form. No uniform
  contraction ρ<1 for the actual shifted values, and hence no positive θ, was
  proved.
* **Phase 3 corrected:** Vaughan uses many sufficient residue classes per
  auxiliary prime plus the large sieve and a Rankin tail, not growing-k shifted
  correlations. Pomerance–Weingartner §4 is the checked modern reconstruction;
  Vaughan's primary PDF remained access-blocked.
