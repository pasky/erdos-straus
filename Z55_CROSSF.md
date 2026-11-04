# Z55_CROSSF — Problem CROSS (R_𝔉(p) ≥ 1 for all large p): direct attack, exact forms, and the scale of "sufficiently large"

Status: z55 TRYHARD lane CROSSF (brief `z52bbriefs/z55_tryhard.md`, Problem CROSS). Internal; hostile-reviewed by a subagent (§6).
**ES is OPEN. Problem CROSS is NOT proved here** (neither R_𝔉(p) ≥ 1 nor R_𝔉(p) ≥ c log²p for all large p). Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / Assessment. Scripts `scripts/z55_crossf_*`, data `data/z55/crossf/`.
Definitions from `Z53_GENUSX.md` §1, §4 (family 𝔉, R_𝔉, M_𝔉, G_𝔉, shell 𝔖, w″) and `Z53_GENUSLVAL.md` Thm U.

## 0. Summary

* **Target.** p ≡ 1 (4) prime; window exponents (α₀, α₁, β, γ) admissible for Thm U; 𝔉 = {(u, w): u ≡ 1 (4) squarefree in
  (p^{α₀}, p^{α₁}], w odd squarefree in (p^β, p^γ], gcd(w, up) = 1}; R_𝔉(p) = 2·hits(p),
  hits(p) := #{(u, w) ∈ 𝔉 : w | p + u, (p + u)/(2w) ≡ −1 (mod 4u)}. Each hit gives p = 8uwC − u − 2w, hence an ES solution.
  Wanted: hits(p) ≥ 1 for all p ≥ p₀.
* **Exact forms (PROVED, §1).** hits(p) is simultaneously (u-form) a count of divisors of (p+u)/2 in the class −1 mod 4u,
  (w-form) of divisors of p + 2w in the class −1 mod 8w, (C-form) of factorisations 4Cp + 1 = (4uC − 1)(8wC − 1), and
  (d-form) #{d : u := (−p mod d) ∈ 𝒰, 4u | d + 1, (p + u)/(2d) ∈ 𝒲}. Every hit has (p/w″) = (w″/p) = −1 (Jacobi), so
  hits(m²) = 0 at odd squares (Lemma 1.2: a proof must use that p is not a square at least here). In every one of the four
  forms, fixing all but one variable leaves a *single-integer* divisor-in-progression event whose modulus is tied to the
  fixed data (Lemma 1.3, PROVED identities). *Assessment:* at a single p the exact count therefore has no free variable in
  the plain sense, in any admissible window, long-u windows included (§2); the brief's suggested route (choose windows where
  the remainders average over u or w) reduces, in the forms we could write down, to the statement itself; the averages that
  do exist are density-level (Thm U, Thm X). Other rearrangements (dispersion, transformed bilinear forms) are not excluded
  by these identities; we did not find one.
* **The scale of "sufficiently large" (CERTIFIED counts + EVIDENCE + model, §3–4).** Exhaustive scans of all primes p ≡ 1 (4) in
  [10⁸, 10⁸ + 2·10⁶] and [10^k, 10^k + 10⁷] for k = 9, 10, 11, and of the first 58 878 such primes above 10^{12} (768 371 primes;
  two independent scanners agree line by line on the 10⁸ range) plus samples at 10^{13}–10^{16} (11 171 primes): hits(p) is
  approximately Poisson-shaped with resolved overdispersion (variance/mean = 1.03–1.07; P(hits = 0) = e^{−mean}·(1.02–1.06)),
  with mean/log²p rising 0.0025 → 0.0034 towards 1/(3π⁴) = 0.003422, half of Thm U's optimised *lower-bound* coefficient
  (used below as the model constant; the data approach it from below). **Zero fractions: 39 % at 10⁸, 24 % at 10^{10}, 9.4 % at
  10^{12}, 5.4 % at 10^{13}, 1.7 % at 10^{15}** (§3). Under the model hits ~ Poisson(c log²p), c = 1/(3π⁴), the expected number of primes with
  hits(p) = 0 is ≈ 5.6·10^{30}, concentrated near p ≈ 10^{63}, and the expected tail count crosses 1 near **p ≈ 10^{124}** (§4;
  an expected-count crossover for this standard-window model with its assumed c, not a certified last exception).
  Hence (Assessment, model-based): for this family and window the model predicts zeros up to p ≈ 10^{124}; the hypothesis (H⁻_𝔉)
  X_𝔉 ≥ −(1 − ε)M_𝔉 of `Z53_GENUSX` is *false* at every zero prime with M_𝔉 > 0 (X_𝔉 = −M_𝔉 there: e.g. p = 10000169, M_𝔉 = 1.17),
  i.e. at a 39 %-fraction of primes near 10⁸ and, under the model, at ~10^{30} primes in total. Such zeros refute (H⁻_𝔉) at
  those p and any specified threshold below them, but not eventual positivity with unspecified p₀; the model only says that
  exhaustive testing up to the predicted crossover is infeasible (no theorem forces a proof's p₀).
* **Verdict: not proved; target recalibrated.** What was proved is the exact structure (§1–2, elementary) and the certified
  counts (§3). Recommendation (§5): as a route to ES the window family is too thin in its constant; a family with a main
  term ≳ 0.1·log²p (or a different kind of positivity mechanism) is needed before "all large p" has checkable content.

## 1. Exact forms of hits(p) (PROVED)

Throughout p ≡ 1 (mod 4) is prime and windows satisfy (C1) γ < 1 − α₁ (so 8uw ≤ p for p ≥ p₀(window)); U₁ := p^{α₁} < Y := p^β
is *not* assumed unless stated (Lemma 1.3(ii) covers both cases). 𝒰 := {u ≡ 1 (4) squarefree, U₀ < u ≤ U₁}; 𝒲 := {w odd
squarefree, Y < w ≤ X}. For (u, w) ∈ 𝔉 with w | p + u put n_u := (p + u)/2 (odd, since p + u ≡ 2 (4)) and w″ := n_u/w.

**Lemma 1.1 (four forms).** For u ∈ 𝒰, w ∈ 𝒲 the following are equivalent, and hits(p) is the number of (u, w) ∈ 𝒰 × 𝒲
satisfying them (gcd(w, up) = 1 is then automatic: gcd(w, u) | gcd(p + u, u) = 1 and w < p):
 (a) w | p + u and w″ ≡ −1 (mod 4u)   [the definition];
 (b) p ≡ −(u + 2w) (mod 8uw)   [the class event of `Z53_GENUSLVAL` Lemma 2.3];
 (c) p = 8uwC − u − 2w for some integer C ≥ 1   [C-form]; equivalently 4Cp + 1 = (4uC − 1)(8wC − 1) with 4uC − 1 = w″;
 (d) (8wC − 1) | p + 2w for some C ≥ 1 with u = (p + 2w)/(8wC − 1)   [w-form];
 (e) with d := w″: d ≡ 3 (4), u = (−p mod d) (least non-negative residue), 4u | d + 1 and w = (p + u)/(2d)   [d-form].
*Proof.* (a)⟺(b): w″ ≡ −1 (4u) ⟺ (p + u) = 2ww″ ≡ −2w (mod 8uw) (w is a unit mod 4u, and the factor 2 is carried along:
2ww″ ≡ −2w (8uw) ⟺ ww″ ≡ −w (4uw) ⟺ w″ ≡ −1 (4u)). (b)⟺(c): p + u + 2w = 8uwC. (c)⟹ 4Cp + 1 = 32uwC² − 4uC − 8wC + 1 =
(4uC − 1)(8wC − 1), and w″ = (p + u)/(2w) = (8uwC − 2w)/(2w) = 4uC − 1. (c)⟺(d): p + 2w = u(8wC − 1). (a)⟺(e): if (a) holds,
d = w″ = 4uC − 1 ≡ 3 (4), p ≡ −u (mod d) and 0 < u < 4u − 1 ≤ d, so u is the least residue of −p mod d; conversely (e) gives
p + u ≡ 0 (mod d) with p + u ≡ 2 (4) and d odd, so w = (p + u)/(2d) is an integer and w″ = d ≡ −1 (4u). ∎
*Check (CERTIFIED).* `scripts/z55_crossf_count.py --brute` computes hits by (a) (factoring n_u), by (c) (no factorisation:
loop over (u, C)) and by (e) (loop over d) and agrees on all test primes (`data/z55/crossf/validate_forms.tsv`), and with the
z53 engine's R on 52 primes at 10⁹–10^{12} (`xcheck_vs_z53.tsv`, 0 mismatches). The two exhaustive scanners of §3 (u-form
with factorisation; C-form without) produce identical output on all 54 198 primes p ≡ 1 (4) in [10⁸, 1.02·10⁸].

**Lemma 1.2 (Jacobi obstruction; where primality enters).** For every hit, (p/w″) = (w″/p) = −1. At an odd square N = m²
(gcd(m, w″) = 1) the same computation gives (N/w″) = +1, so hits(m²) = 0 identically.
*Proof.* w″ = d = 4uC − 1 ≡ 3 (4) and p ≡ −u (mod d), so (p/d) = (−u/d) = (−1/d)(u/d) = −(d/u) (u ≡ 1 (4), reciprocity) =
−(−1/u) = −1; and (d/p) = (p/d) since p ≡ 1 (4). For N = m² in place of p, (N/d) = (m/d)² = 1 ≠ −1. ∎
(= `Z53_GENUSX` Lemma 2 / B5 "every hit has (w″/p) = −1", restated in the d-form; CERTIFIED: 7 odd squares near 10⁸–10⁹ have
hits = 0 with non-empty shells, `data/z55/crossf/controls.txt`.) For prime p the symbol (·/p) is −1 on half the residues
mod p, so nothing obstructs; *the target's dependence on primality (non-squareness) is visible here: the level divisors
w″ must be non-residues mod p, which no odd square allows* (whether a proof needs more than non-squareness is not
settled by this). The density main term M_𝔉 uses it through χ_{−4up} being primitive of
cube-free conductor (Burgess, Thm U).

**Lemma 1.3 (every one-variable section is a single-integer divisor-in-progression event).**
 (i) u fixed: #{w : (u, w) hit} = #{d | n_u : d ≡ −1 (mod 4u), n_u/d ∈ 𝒲}  (divisors of the one integer n_u = (p+u)/2);
 (ii) w fixed: #{u : (u, w) hit} = #{d′ | p + 2w : d′ ≡ −1 (mod 8w), (p + 2w)/d′ ∈ 𝒰}  (divisors of the one integer p + 2w);
   in particular if U₁ < w the count is ≤ 1 (u = −p mod w), and if U₁ > w (long-u windows) the AP {u ≡ −p (w)} ∩ (U₀, U₁]
   of length U₁/w contributes only through the divisors of p + 2w;
 (iii) C fixed: #{(u, w) : hit with this C} = #{d | 4Cp + 1 : d ≡ 4C − 1 (mod 16C), (d + 1)/(4C) ∈ 𝒰, ((4Cp + 1)/d + 1)/(8C) ∈ 𝒲}
   (divisors of the one integer 4Cp + 1);
 (iv) d fixed: at most one (u, w), namely u = −p mod d, present iff 4u | d + 1 and the window/squarefree conditions hold.
*Proof.* (i), (ii), (iv) are Lemma 1.1 (a), (d), (e) read at fixed u, w, d. (iii): by (c), d = 4uC − 1 ≡ −1 (4C) and u ≡ 1 (4)
give d ≡ 4C − 1 (16C); conversely d | 4Cp + 1 with 4C | d + 1 gives u := (d+1)/(4C) and, as (4uC − 1) | 4C(p + u) with
gcd(4C, 4uC − 1) = 1, d | p + u, i.e. (a) with w = (p + u)/(2d). ∎

*Reading.* The three variables (u, w, C) satisfy one equation; whichever two are summed over, the indicator is 1[m | n] with
n ∈ {p + u, p + 2w, 4Cp + 1} depending on *one* of the summed variables and m ≡ −1 mod (4 or 8 or 4)·(that variable). This
is the same "x ↦ −p mod x" structure as `Z53_GENUSX` Lemma 4.1, now seen to be form-independent.

## 2. The attack: windows with a free average (PROVED reductions; Assessment-level conclusions; outcome negative)

The brief's natural line is R_𝔉 = M_𝔉 + X_𝔉 with M_𝔉 ≫ log²p (Thm U) and X_𝔉 ≥ −(1 − ε)M_𝔉 to be shown "by choosing windows
where the remainders can be averaged over u or w". We tried the three possibilities.

**2.1 Long-u windows (α₁ > γ).** Thm U's hypotheses (C1)–(C3) do not require β > α₁; e.g. (α₀, α₁, β, γ) = (0.1, 0.45, 0.4, 0.44)
satisfies γ < 1 − α₁, β > τ(1 + α₁) = 0.3625, α₀ > τ²(1 + α₁) = 0.0906 (τ ↓ 1/4), with c = (8/π⁴)(0.04)(0.35) ≈ 0.00115; Thm U's
proof (Prop 2.4: windowed w-sums at fixed u, hyperbola, Burgess; Prop 2.5 concerns u alone; §2.7 uses coprimality and
8U₁X ≤ p) is unchanged — checked by us and by the reviewer: no step uses U₁ ≤ Y. In such a window, at fixed w the u-sum
runs over an AP of length U₁/w ≥ p^{0.01} — but by Lemma 1.3(ii) the *exact* count at fixed w is the number of divisors
d′ ≡ −1 (mod 8w) of the single integer p + 2w with cofactor in (U₀, U₁] (PROVED identity): the AP average exists for the
density ρ (which is what Thm U uses), not for the exact indicator. *Assessment:* long-u windows give no exact u-average.

**2.2 Short-u windows (β > α₁; the Thm U optimum).** At fixed w the u-sum has ≤ 1 term (Lemma 1.3(ii)); at fixed u the w-sum is
over divisors of n_u (Lemma 1.3(i)). The only average is over the *free* w with the tied condition on r_w = −p mod w
(`Z53_GENUSX` Lemma 4.1): hits(p) = #{w ∈ 𝒲 : r_w ∈ 𝒰, ⌈p/w⌉ ≡ −2 (mod 8r_w)}. The first condition alone (r_w ≤ U₁) is a
short-interval divisor count Σ_{u ≤ U₁} τ(p + u; Y, X), whose asymptotic U₁ log(X/Y) is a sawtooth-sum problem (Assessment:
accessible for α₁ > 1/3 from van der Corput's Σ_{w ~ W} ψ(N/w) ≪ N^{1/3}log N, W ≤ √N, plus the hyperbola swap for W > √N;
not written, not needed, and T1-blind in any case); the second condition selects, among
the ≈ U₁ log(X/Y) shell points, those whose level divisor lies in one class mod 8r_w. *Assessment:* we found no average
over w that sees this class.

**2.3 The C-parametrisation.** Summing Lemma 1.3(iii) over C ∈ (Z₀, Z₁] (Z ≈ p/(8uw) ∈ (p^{1−α₁−γ}, p^{1−α₀−β})) gives
hits(p) = Σ_C #{d | 4Cp + 1 : d ≡ 4C − 1 (16C), windows}. Here the modulus 16C is shared by all divisors of N_C := 4Cp + 1,
and C is free with Z₁ ≥ p^{1/2+ε} in the Thm U window (1 − α₀ − β = 7/12). The *principal-character* part Σ_C #{d | N_C,
d ~ D}/φ(16C) looks accessible (sketch only; not claimed, not needed): on hits gcd(d, 4p) = 1 (d | 4Cp + 1) and C < d
(d = 4uC − 1), so #{C < d : d | 4Cp + 1} = 1[c₀(d) ∈ range], c₀(d) := −(4p)⁻¹ mod d, and e(h c₀(d)/d) = e(h d̄/(4p))·e(−h/(4pd))
(reciprocity ā/d + d̄/a ≡ 1/(ad) mod 1), so Σ_{d ~ D, (d,4p)=1} e(h c₀(d)/d) is an incomplete Kloosterman sum mod 4p of length D
with a smooth twist, ≪ p^{1/2+ε} by Weil and completion — o(Z) once Z ≥ p^{1/2+2ε} (the weight 1/φ(16C) and the varying
interval length Z/d need partial summation and a dyadic split in d). But the class condition d ≡ 4C − 1 (16C) is *tied* (16C ≈ 4d/u), and by
Lemma 1.3(iv) the sum over C of the class indicator at fixed d collapses to the single term C = c₀(d) with the condition
4c₀(d)·(stuff) | d + 1 — i.e. "the modular inverse of −4p mod d divides (d + 1)/4". The Kloosterman structure gives the
equidistribution of c₀(d)/d at scale ≫ p^{1/2}/D, while the condition requires c₀(d) to hit a set of ≤ τ((d+1)/4) values.
PROVED (Lemma 1.3(iv)): the tied class is again a single-residue event; *Assessment:* the C-average reaches only the
principal character.

**2.4 Minorants and sieves (one PROVED no-go, one heuristic remark).**
 (a) *No genus-character minorant.* Let G = (ℤ/q)^×, S ⊂ Ĝ, f = Σ_{χ ∈ S} a_χ χ real-valued with f(x) ≤ 1[x = 1] for all x.
 Then a_{χ₀} = |G|⁻¹Σ_x f(x) ≤ f(1)/|G| ≤ 1/|G|, with equality iff f = 1_{{1}}, which forces S = Ĝ. If S lies in a proper
 subgroup of Ĝ (e.g. S = the real characters, the genus set), then f is invariant under the non-trivial group S^⊥ (= G² for
 the genus set), so for h ∈ S^⊥ \ {1}: f(1) = f(h) ≤ 0, hence a_{χ₀} ≤ 0. **No minorant of the class indicator 1[p ≡ a (q)]
 with positive main term exists inside the genus characters**: positivity cannot be obtained from M_𝔉 by a pointwise
 inequality; every character of every order must be controlled.
 (b) *Large sieve on the d-form (heuristic remark, not worked out).* In the d-form, hits(p) = 0 says that p avoids, for every
 modulus d in range, the ≤ τ((d + 1)/4) classes −u with u | (d + 1)/4, u ∈ 𝒰 (and the p-dependent cofactor conditions). A
 large sieve over prime moduli d ≤ √x with that many forbidden classes has sieve density Σ_d |𝒯_d|/d of order at most log x
 (Σ_{d prime ~ D} τ(d + 1)/d ≍ 1 per dyadic block by the Titchmarsh divisor problem), so even if the p-dependence of the
 forbidden sets were removed it could bound the number of exceptional p ≤ x only by O(x/log x) — the density of primes.
 We did not set this up rigorously (the forbidden sets depend on p through the w-window, and the restricted divisor sum
 needs its own lower bound); it is recorded only as the reason we did not pursue sieving.

**2.5 Outcome (Assessment).** In every window admissible for Thm U, X_𝔉 = R_𝔉 − M_𝔉 is a sum of single-residue events minus
densities; the averages we could identify (over w at fixed u at density level; over C for the principal character) are the
ones Thm U / Thm X already use. None of §2's methodological conclusions, nor the Kloosterman/sieve sketches, is bankable:
identifying the divisor events does not prove that no transformed average exists, and 2.4(a) concerns pointwise Fourier
minorants only. We did not find a way around this and **do not claim** any bound on X_𝔉. The remainder of the
memo quantifies what the target asks for.

## 3. Exhaustive counts of hits(p) (CERTIFIED) and the Poisson law (EVIDENCE)

**Engines.** `scripts/z55_crossf_scan.c` (u-form: factor n_u by trial division, enumerate squarefree divisors) and
`scripts/z55_crossf_cscan.c` (C-form: for each u loop over C with (8uC − 2) | p + u; no factorisation; cost ≍ Σ_u p/(8uY)
≍ p^{2/3}log p per prime, 29 ms at 10^{12}, 0.5 s at 10^{13}; Miller–Rabin with the 13 prime bases ≤ 41, deterministic far
beyond the int64 input range) — both with the standard window U₀ = round(p^{1/12} − ½),
U₁ = ⌊p^{1/3}/2⌋, Y = ⌊p^{1/3}⌋, X = ⌊p^{2/3}/4⌋ (X decreased until 8U₁X ≤ p), exactly `scripts/z53_genusx_run.py`'s. The
outputs agree line by line on [10⁸, 1.02·10⁸] (54 198 primes). Scans: all primes p ≡ 1 (4) in [10^k, 10^k + 10^7] (k = 8: +2·10⁶;
k = 12: the first 58 878 primes, time-boxed); samples at 10^{13}–10^{16} (`scripts/z55_crossf_bigscan.sh`, one prime per step).
Summary `data/z55/crossf/stats.txt` (`scripts/z55_crossf_stats.py`):

| range | N primes | mean hits | var/mean | P(hits = 0) | e^{−mean} | mean/log²p |
|---|---|---|---|---|---|---|
| [10⁸, 1.02·10⁸] | 54 198 | 0.967 | 1.07 | 0.392 | 0.380 | 0.00285 |
| [10⁹, 10⁹+10⁷] | 240 944 | 1.071 | 1.03 | 0.348 | 0.343 | 0.00249 |
| [10^{10}, +10⁷] | 217 331 | 1.457 | 1.03 | 0.238 | 0.233 | 0.00275 |
| [10^{11}, +10⁷] | 197 020 | 1.909 | 1.04 | 0.153 | 0.148 | 0.00298 |
| [10^{12}, +3.3·10⁶] | 58 878 | 2.427 | 1.05 | 0.094 | 0.088 | 0.00318 |
| 10^{13} sample (step 10⁵) | 8 290 | 2.958 | 1.06 | 0.054 | 0.052 | 0.00330 |
| 10^{14} sample (step 10⁶) | 2 238 | 3.478 | 1.02 | 0.035 | 0.031 | 0.00335 |
| 10^{15} sample (step 10⁷) | 535 | 3.903 | 1.08 | 0.017 (9 zeros) | 0.020 | 0.00327 |
| 10^{16} sample (step 10⁸) | 108 | 4.454 | 0.83 | 0 | 0.012 | 0.00328 |

(Samples: the next prime ≡ 1 (4) at or after 10^k + j·step, j = 0, 1, …, time-boxed at 1700 s each; the 10^{17}–10^{18} runs of
`z55_crossf_bigscan.sh` were stopped with too few primes to be useful and are not kept. Largest certified zero primes:
1000005280000049 (10^{15}; also 1000004470000057), 10000481500117 (10^{13}), re-checked independently by the PARI u-form
script `scripts/z55_crossf_count.py` together with two 9-hit primes, `data/z55/crossf/xcheck_zeros_1e12_1e13.tsv`.)

**Readings.** (1) hits(p) is approximately Poisson-shaped, with *resolved* overdispersion: variance/mean = 1.03–1.07 and
P(0) = e^{−mean}·(1.02–1.06), both excesses many standard errors above an iid Poisson null at N ≈ 10⁵. Hypothesis (EVIDENCE):
the excess is the mixture over p of the mean λ(p) = M_𝔉(p)/2, which varies with L(1, χ_{−4up}); the z53 data (M̂ per prime)
give P(0) ≈ mean_p e^{−M̂(p)/2} within their sampling error. (2) mean/log²p increases towards 1/(3π⁴) = 0.003422 =
(1/2)(8/π⁴)(γ − β)(α₁ − α₀) at (1/12, 1/3, 1/3, 2/3): half of Thm U's *lower-bound* coefficient at its optimum. Thm U does not
assert that M_𝔉 ∼ (2/(3π⁴))log²p (its proof discards non-negative terms and says the constant is not optimised), and no
theorem gives the mean of hits; we use c = 1/(3π⁴) as the model constant because the data approach it from below. (3) The
square controls have hits = 0 (Lemma 1.2); composite non-squares near 10⁸ behave like primes.

## 4. The scale of p₀ under the Poisson model (model computation; heuristic, with CERTIFIED inputs)

Model: hits(p) ~ Poisson(c log²p) for each prime p, with c = 1/(3π⁴) (§3(2); independence across p is not needed for
expectations). The expected number of primes p ≡ 1 (4), p > x, with hits(p) = 0 is Σ_{p > x, p ≡ 1 (4)} e^{−c log²p} ≈ E(x) :=
∫_{log x}^∞ e^{s − cs²}/(2s) ds (prime-density approximation). Numerically (`stats.txt`; re-derived by the reviewer):
E(10⁸) ≈ E(10^{18}) ≈ 5.58·10^{30}; the integrand e^{s−cs²}/(2s) peaks at s = (1 + √(1 − 8c))/(4c) ≈ 145, i.e. p ≈ 10^{63};
E(10^{100}) ≈ 5.9·10^{18}; E(x) = 1 at **x ≈ 10^{124}** (log x ≈ 286 ≈ 0.98/c). With the finite-size value c = 0.0030 instead:
1.5·10^{35} expected exceptions, E = 1 near 10^{142}. Consequences (Assessment; everything here is what *this model* predicts):
 (i) For the standard window and the assumed c, the model predicts zeros of R_𝔉 up to p ≈ 10^{124}, ~10^{30} of them; E(x) = 1
 is the crossover of an expected tail count (marginal Poisson laws do not specify the distribution of the last zero), and a
 lower-bound coefficient says nothing about other windows' means. For the stronger "R_𝔉(p) ≥ a·c log²p" (0 < a < 1), since
 R_𝔉 = 2·hits the event is hits ≤ (a/2)λ with λ = c log²p, with Poisson lower-tail exponent λ·I(a/2), I(t) := 1 − t + t log t
 < 1, so the predicted crossover is larger still (log p₀ ≈ 1/(c·I(a/2)); e.g. a = 1/2: I(1/4) = 0.403, log₁₀p₀ ≈ 315).
 (ii) (H⁻_𝔉) of `Z53_GENUSX` (X_𝔉 ≥ −(1 − ε)M_𝔉) is false at every zero prime with M_𝔉 > 0 (there X_𝔉 = −M_𝔉; M_𝔉 > 0 is
 guaranteed by Thm U for p large, and holds at the checked examples, e.g. p = 10000169 with M_𝔉 = 1.174 by direct
 summation; the cross-model review certified M_𝔉 > 0 at all 192 469 recorded exhaustive-scan zeros by a modular
 square-class witness): at 39 % of primes near 10⁸, 9 % near 10^{12}, and, under the model, at ~10^{30} primes in all. The
 model thus predicts that any true version of (H⁻_𝔉) has p₀ ≳ 10^{120}; the all-large-p statement itself is not disproved.
 (iii) For an ES route this is harmless in principle (ES needs one solution of any type, and p ≤ 10^{17} is known) but it
 means that a zero at computable p does not refute eventual positivity with unspecified p₀, while exhaustive checks of
 "R_𝔉 ≥ 1" over long ranges below ~10^{100} are predicted to show zeros at the rate e^{−c log²p} (small random samples at
 very large p will of course mostly show none); an effective proof's explicit constants could of course still be checked.
 (iv) The constant is the issue. The hits mean for the *full* (★) count (all (u, B) ∈ 𝒫(p)) is far larger (the window
 family keeps only u ∈ (p^{1/12}, p^{1/3}/2], w ∈ (p^{1/3}, p^{2/3}/4]); a family with c_hits = 0.1 would have E = 1 near x ≈ 800
 and would be checkable. Thm U's coefficient (8/π⁴)(γ − β)(α₁ − α₀) is maximised at 2/(3π⁴) under the coupled constraints
 (C1) γ < 1 − α₁, (C2) β > (1 + α₁)/4, (C3) α₀ > (1 + α₁)/16 (r → ∞), a limiting supremum approached at (1/12, 1/3, 1/3, 2/3)
 (strict-margin subwindows); even GRH (`Z53_GENUSLVAL` §4: coefficient 2/π⁴, c_hits → 1/π⁴ ≈ 0.0103) only moves the
 same E(x) = 1 crossover to ≈ 10^{39.9} (exp(1/c) alone would give 10^{42.3}).

## 5. Verdict and recommendation

* **Not proved.** No bound on X_𝔉 at a single prime was obtained; §2 shows (PROVED identities, Assessment conclusion)
  that the averaging route proposed in the brief reduces, in every admissible window and in every parametrisation we
  could write, to the single-residue events it was meant to average.
* **Recalibration (the lane's finding).** For the Theorem U family the statement "R_𝔉(p) ≥ 1 for all sufficiently large p" is,
  under this extrapolated model, a statement about p ≳ 10^{124} with ≈ 10^{30} exceptions below — true (if at all) only in the regime where
  the main term c log²p, c = 0.0034, exceeds the Poisson fluctuation scale log(#primes). A future lane on this problem
  should (a) not read R_𝔉 = 0 at computable p as refuting eventual positivity with unspecified p₀ (it is the expected
  behaviour; it does refute (H⁻_𝔉) at that p and any threshold below it), and (b) first enlarge
  the main-term constant: either prove a genus lower bound for a much larger family (all u ≤ p^{1/3}, all w ≤ p^{2/3}, no
  squarefree restriction: heuristically c_hits ≈ an absolute constant times (1/3)(2/3)·(8/π⁴)/2·(correction for the dropped
  conditions)), or move to the HC-type small-C families where the mean is ≫ log p per unit of log C and exceptions are
  provably rare at computable sizes.
* **What a proof would need (Assessment).** A lower bound at a single p for Σ_{d ~ D} 1[(−p mod d) ∈ 𝒯_d] with
  |𝒯_d| ≤ τ(d + 1): equidistribution of −p mod d jointly over d at the scale of single residues. In our hands neither
  Burgess (p in the conductor: density only), Kloosterman/Weil (principal character only, §2.3) nor sieving (§2.4(b))
  reached it; other rearrangements are not excluded by anything proved here.

## 6. Review log

**Hostile review (deep-mode subagent, no edits by the reviewer).** It re-derived Lemmas 1.1–1.3 ("the factorisation,
automatic gcd, reciprocity signs and square obstruction are correct; d = 4uC − 1 > u directly"), brute-forced forms (a)/(c)/(e)
on all 1 125 primes p ≡ 1 (4) below 20 000 in two hand-chosen windows (446 hits, identical sets), audited both scanners
("cscan's C-bounds conservatively contain every valid C; scan's distinct-prime subsets correctly allow prime powers in the
cofactor"), recomputed every number of the §3 table from the data files (all match; 768 371 primes in the exhaustive scans),
confirmed the 52 z53 cross-checks, re-evaluated E(x) (5.58·10^{30}; E = 1 at log₁₀x = 124.11) and confirmed that no step of
Thm U's proof uses U₁ ≤ Y. Its findings and the fixes applied: (1) the constant 1/(3π⁴) is half a *lower-bound* coefficient,
not a proved mean — reworded throughout, model constant labelled as such; (2) model predictions had been stated as
necessities ("any proof must …", "no effective version can be true") — rewritten as what the model predicts; (3) the
"no free variable" conclusions were labelled PROVED although only the identities are — identities keep PROVED, conclusions
downgraded to Assessment with the explicit caveat that dispersion/transformed forms are not excluded; (4) the long-u
example had γ > α₁ — replaced by (0.1, 0.45, 0.4, 0.44), and the "(u, 2w) swap" sentence removed; (5) the large-sieve
paragraph was not a proof (p-dependent forbidden sets, missing lower bound for the restricted divisor sum) — reduced to an
explicitly heuristic remark; (6) C-average sketch: restrictions C < d, gcd(d, 4p) = 1 and the exponent margin added, kept as
sketch; (7) "Poisson to the accuracy of the data" contradicted the data (overdispersion is 8–11 standard errors) — reworded,
mixture explanation labelled a hypothesis; (8) summary coverage corrected (10⁸ range is 2·10⁶ long; 10^{12} is the first
58 878 primes; two-scanner agreement is on the 10⁸ range); (9) integrand peak corrected to s = (1 + √(1 − 8c))/(4c), the
c = 0.1 example to x ≈ 800; (10) the "≥ a·c log²p" variant now carries its own rate function; (11) "(H⁻) false at zero
primes" now requires M_𝔉 > 0; (12) the summary's d-form now lists the w-condition; (13) scanner cost corrected to p^{2/3}log p.
Reviewer's verdict after fixes (paraphrase of its overall verdict): no ES proof is claimed; keep the lemmas and the counts;
the methodological and asymptotic conclusions had to be, and now are, scoped as Assessment / model predictions.

**Cross-model review** (`data/z55/xreview/REVIEW_CROSSF.md`, verdict ACCEPT-WITH-FIXES; independent checker
`scripts/z55_xrev_crossf_check.c` (loops over w, tests 8uw | p+u+2w directly) and audit `scripts/z55_xrev_crossf_audit.py`):
Lemmas 1.1–1.3, §2.1–2.4(a) and the §3 counts CORRECT (full 10⁸ C-scanner rerun byte-identical; 512 sampled primes recounted;
all five prime lists verified complete by segmented sieving; M_𝔉 > 0 certified at all 192 469 recorded zeros); E(x) numbers
CORRECT as model. Required fixes, all applied: 10^{124} scoped to the standard-window model and stated as an expected-count
crossover (not a certified last exception; "any admissible window" and "on the data" removed); §4(i) rate function corrected
to I(a/2) since R_𝔉 = 2·hits; GRH crossover recomputed by the same E(x) = 1 prescription (10^{39.9}); "attained" → limiting
supremum; "no finite-size falsifier" wording replaced (a zero with M_𝔉 > 0 does refute (H⁻_𝔉) at that p and any threshold
below it; eventual positivity with unspecified p₀ is not refuted); §2 conclusions and sketches marked non-bankable.
Bankable: the elementary identities and the finite counts; not bankable: any asymptotic positivity or impossibility claim.

**Bottom line.** Problem CROSS is not proved. The exact structure of R_𝔉 (four forms, Jacobi obstruction, single-integer
sections) is PROVED and elementary; the certified counts show hits(p) = 0 at the Poisson-predicted rate at every scale up to
10^{15}; the Poisson model places the end of the exceptions near 10^{124}. **ES remains OPEN.**
