# R289 — independent hostile review #2 (round 1)

Author revision reviewed: `5e418734`, `paper/es-threequarter-note.tex` (C2). Reviewer branch: `side-agent/review-threequarter-2`. No author files changed; no access to reviewer #1's report or branch. This report is being built claim by claim.

## Cold referee summary

The argument fixes a family of Type II congruences modulo `kℓ`, with multipliers `k ≤ X^κ`, large primes `√X < ℓ ≤ X`, and reduced pairs `H < u,v ≤ x^(1/6)` satisfying `4uv | kℓ+1`. The large lower cutoff makes the classes modulo a given `ℓ` distinct even across different multipliers. Revealing the entire small-modulus residue `c mod L_K` therefore turns the hit count into a sum of independent Bernoulli variables, not independent individual atoms.

The analytic core is a uniform-in-`c` supply estimate. A lattice calculation supplies mass `t² Σ φ(k)/k²`. Brun–Titchmarsh gives its upper bound. The lower bound uses Bombieri–Vinogradov and Cauchy–Schwarz with a weighted second incidence moment; Shiu bounds the latter after replacing two multiplier conditions by one condition modulo their least common multiple. This avoids multiplying a BV error bound by the maximum incidence multiplicity.

Nonunit fibres can have small supply. Conditioning on avoidance of primes up to `y = B t³` makes severe loss of multiplier mass exponentially rare, by an exponential-moment estimate on `Σ_{p|c,p>y} 1/p`. The resulting conditional void probability is `exp(-c t³)`. The same fibre decomposition gives factorial moment bounds with a base independent of the moment order. An even Bonferroni polynomial of degree `O(t³)`, multiplied by the exact small-prime selector, is a nonnegative majorant with small CRT mean. Expanding it into actual congruence classes costs `exp(O(t⁴))` coefficients. Integer counting then costs at most one per coefficient, without ever splitting the interval into fibres modulo `L_K`. Choosing `t` proportional to `(log N)^(1/4)` yields the prime exceptional-set saving. Rankin's trick transfers this to all integers because an exceptional integer can only have exceptional prime factors.

The logical route is reconstructible from the note alone. In particular, the enormous conditioning modulus is not itself an integer-counting cost. The issue to test is uniform supply, not a supposed requirement that `L_K ≤ N`.

## Scope and evidence

This is an independent mathematical audit, not external refereeing or a claim that ES is solved. Numerical tests below will be finite sanity checks, not validation of asymptotic analytic estimates. Source-access limitations will be stated explicitly.

## Claim-by-claim verdicts (in progress)

- Sections 1–2, identity and conditional independence: **SOUND** (core statements).
- Section 3, analytic inputs and lattice sums: **SOUND**.
- Section 4, weighted incidence moment and uniform cubic supply: **SOUND**.
- Sections 5–6, moments and conditioned void: pending.
- Section 7, Bonferroni and coefficient ledger: pending.
- Section 8, primes and Rankin transfer: pending.
- Section 9 and introductory comparison/cap remarks: pending.

## Detailed checks

### Sections 1–2: identity, atoms, CRT — SOUND

Independently clearing denominators gives `nv + u + s = s(kℓ + 1) = 4suvw`. Since `nv+u` is a positive multiple of `kℓ`, all three denominators are positive integers. No primality or coprimality with `n` is required for this identity. Coprimality of `v` with `kℓ` follows from `uvw | kℓ+1`.

For a fixed prime, equality of residues implies `ℓ | uv′−u′v`; its absolute value is less than `z² < ℓ`. Equality of two reduced positive fractions forces equality of both numerator and denominator. Then `4uv | k−k′`, and `4uv > K` forces equality of the multipliers. This checks distinctness across **all** multipliers, not just within a fibre. Consequently the prime-level indicator really is Bernoulli even when several multipliers are active.

Every large prime is coprime to `lcm(L_K,P_y)`. Conditioning on a residue of that modulus, or any compatible event determined by it, leaves the large-prime coordinates mutually independent and uniform. Zero-probability combinations of `c` and `S_y=1` are simply omitted when averaging. There is no equidistribution assertion about `[1,N]` in this step. The exact fibre activity test is `k | u+cv`; it also forces `gcd(c,k)=1`.

The parameter inequality is strict in the needed direction: `20κ < 1/12`, so `H² ≤ X^(20κ) < X^(1/12) ≤ z_j`. This implies `log(z_j/H) ≥ ½ log z_j`. Fixing `κ=1/480` before all other constants makes the eventual constants absolute. No inaccessible finite asymptotic threshold is being presented as a numerical certification.

### Section 3: inputs and lattice sums — SOUND

**Shiu checked against the primary scan.** I rendered and read printed pp. 161–163 of `sources/shiu-1980.pdf`, not the author's transcription. Theorem 1, equation (2.1), has `Y/(φ(q) log V)` and the exponential sum excluding primes dividing `q`; the conditions are `q < Y^(1−α)`, `V^β < Y ≤ V`, `0<α,β<1/2`, and the reduced representative `0<a<q`. The class M has precisely the two growth hypotheses quoted in C2. The scan explicitly states dependence only on `α,β,f`. C2 uses one fixed function, so there is no varying-function uniformity issue.

For `F(n)=2^ω(n)n/φ(n)`, `F(p^a)≤4≤4^a` and `F(n)≤4^ω(n)≤τ(n)²≪ε n^ε`. On every box, `d≤K²≤U^(1/5)`, while `Y=U/20`, so both Shiu range inequalities hold after an absolute threshold. Since every prime divisor of `d` is below `V`, all the removed Euler factors are present in Shiu's sum. Importantly, `F(p)/p=2/(p−1)`, and `log(1−1/p)≥−1/(p−1)` gives the local-factor inequality in the **correct** direction. The modulus-one case is legitimately separate: `F=1*h`, `h(p)=(p+1)/(p−1)`, `h(p^a)=0` for `a≥2`, and the Euler product for `Σ h(d)/d` is `O(log V)`.

**Lattice calculation re-derived.** The one-dimensional AP harmonic sum has error `O(1/H′)` even for an empty progression. Multiplying the AP and coprime sums gives `T=φ(k)Λ′²/k²+O(Λ′τ(k)/H′)` when `H′,Λ′≥1`; the product-error term is absorbed. For common divisors `d≤H`, scaling preserves the reduced congruence because `(d,k)=1`. Summing their errors gives `O(Λ τ(k) log H/H)`. The tail `d>H` is `O((1+log z)²/H)=O(Λ²/H)`. The main Euler factor is at least `6/π²`; the relative error is `O(K²/H)`. Thus the numerical constant `1/4` is justified asymptotically and uniformly in `c,k,z`.

For the upper lattice bound, the divisor expansion of `1/φ` gives the displayed three terms. Its convergent sum `Σ μ²(d)/(dφ(d))`, logarithmic sum `Σ_{d≤H} μ²(d)/φ(d)`, and `H^(−1/2)` tail give exactly the claimed uniform estimates; multiplying the uniform AP bound by the coprime-v bound is valid despite the AP residue depending on `v`. The multiplier harmonic constant is `(1/4)∏_{p>2}(1−p^(−2))=2/π²`, and the removal estimate follows from `φ(pm)/(pm)²≤1/(pm)`.

**Other source limitation.** I did not access Davenport Ch. 28 or the original Montgomery–Vaughan Theorem 2. Their displayed inputs are the standard BV and interval Brun–Titchmarsh statements, and I checked their use rather than claiming a primary-source verification. In particular, partial summation on `[x,2x]` converts a uniform ψ-bound to the required π-bound. At the actually used level `q≤4x^(1/3)`, the sum of the trivial prime-power errors is `O(x^(5/6) log x)`, smaller than `x/log^R x` for every fixed R. At the larger level in the stated BV input one can increase the logarithmic loss in the level. No effective constants are extracted.

### Section 4: uniform cubic supply — SOUND

Expand `r_J²` into ordered multiplier pairs. Their simultaneous condition is exactly modulo `d=[k,k′]≤K²`. Before dropping `(u,v)=1`, it forces `(v,d)=1`, because `c` is a unit modulo every multiplier in J. Thus the inner residue remains reduced after relaxing coprimality. The upper bound factors as `(1/2)(Σ F(v)/v)(Σ_{u≡−cv(d)} F(u)/u)`. Shiu and box summation give respectively `O(log²z)` and `O(log²z·φ(d)/d²)`. The lcm-pair sum is bounded by `Σ_{g≤K} g^(−1)(Σ_{a≤K/g} a^(−1))²=O((1+log K)³)`. No maximum value of `r_J` is substituted, and neither J nor c enters the constant.

In a full block the main term is at least `xΛ² h(J)/(16 log(2x)) ≫ xt h(J)`. Grouping the errors by `q=4uv`, there are at most `2^ω(q/4)` ordered coprime splittings, so `W(q)²≤2^ω(q/4)Σ r_J²`. Brun–Titchmarsh bounds the maximum absolute error (including its main term) by `O(x/(φ(q)log x))`. Hence `Σ W²E*≪xt⁶`. Cauchy–Schwarz against BV with the fixed exponent 26 gives `O(xt^(−10))`, and `h(J)≥1` absorbs this **uniformly even for sparse J**. There are order t full blocks and `1/ℓ≥1/(2x)` in each, giving the lower `t²h(J)` bound. The upper bound is the corresponding BT/lattice calculation, enlarging only the last block.

Finally, activity forces `(c,k)=1`, so `f_c=f_{c;J_c}` is an equality, not an upper comparison. This permits applying both bounds to data-dependent nonunit fibres. I find no circular use of the void estimate or moment theorem in this analytic input.

### Independent numerical checks (completed first pass)

From-scratch script: `scripts/review_r289_checks.py`; raw output: `reviews/threequarter-hardened-review-2-checks.log`. No campaign modules or author scripts are imported or reused. All assertions pass under a 180-second timeout, one-thread environment, 8,000,000-KiB shell cap and 768-MiB internal cap.

- 18,999 exact rational identity checks; exact equality of the two identity-class descriptions for `A≤300`; divisor convolution for `τ(A²)`.
- Direct streamed enumeration of a full CRT period **20,122,110**, with six atoms at primes 47, 67, 71, multipliers 1, 5, 9, all 45 fibres (including nonunits): the entire hit-count distribution equals the independently predicted Bernoulli product law. Factorial moments checked through order 8. A negative control exhibits collisions when the distinctness cutoff is omitted.
- Signed class expansions at even degrees 0, 2, 4 match both the full-period mean and direct interval counts at five lengths, including moduli larger than the interval. The rounding error is bounded by the number of nonempty terms, hence by the raw coefficient ledger.
- Exhaustive finite Bonferroni identities, factorial lower bound, totient inequalities, Shiu local-factor direction, selector exponential-moment bound, and Rankin pointwise inequality pass.
- Toy lattice ratios with `H=24,z=600,k≤20`: lower/main ranges 0.598330–0.914175; upper/main at most 1.51945. Forty weighted-incidence `(c,J)` cases verify the grouping Cauchy inequality. Multiplier removal and the complete lcm-pair inequality pass.

**Limit:** toy lattice/incidence parameters are not `H=K^10,z≥H²`; the script explicitly labels their ratios EVIDENCE only. It neither tests BV/Shiu asymptotically nor certifies the unknown constants or thresholds.

## Numbered defects

None entered yet; this is not a final clean bill of health.
