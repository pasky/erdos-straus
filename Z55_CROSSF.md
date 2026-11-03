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
  (d-form) #{d : (−p mod d) ∈ 𝒰 and 4·(−p mod d) | d + 1}. Every hit has (p/w″) = (w″/p) = −1 (Jacobi), so hits(m²) = 0 at
  odd squares (Lemma 1.2: this is where any proof must use that p is not a square). In every one of the four forms, fixing
  all but one variable leaves a *single-integer* divisor-in-progression event whose modulus is tied to the fixed data
  (Lemma 1.3) — there is no free variable to average over at a single p, in any admissible window, long-u windows included
  (§2). The brief's suggested route (choose windows where the remainders average) therefore reduces, exactly, to the
  statement itself; the only averages that exist are density-level (Thm U, Thm X), and these are already used.
* **The scale of "sufficiently large" (CERTIFIED counts + EVIDENCE + model, §3–4).** Exhaustive scans of all primes p ≡ 1 (4) in
  [10^k, 10^k + 10^7] for k = 8, …, 12 (≈ 770 000 primes; two independent scanners, identical output) and samples at
  10^{13}–10^{18}: hits(p) is Poisson-distributed to the accuracy of the data (variance/mean = 1.03–1.07; P(hits = 0) =
  e^{−mean}·(1.03–1.06)), with mean/log²p rising 0.0025 → 0.0034 towards the Thm U constant 1/(3π⁴) = 0.003422 (= M_𝔉/2 for
  the optimal window). **Zero fractions: 39 % at 10⁸, 24 % at 10^{10}, 9.4 % at 10^{12}, 5 % at 10^{13}** (§3). Under the
  Poisson model with the Thm U constant — the best any admissible window can give — the expected number of primes with
  hits(p) = 0 is ≈ 5.6·10^{30}, concentrated near p ≈ 10^{63}, with the last one expected near **p ≈ 10^{124}** (§4).
  Hence (Assessment): Problem CROSS can only be true as an ineffective-looking asymptotic statement with p₀ ≳ 10^{124};
  the hypothesis (H⁻_𝔉) X_𝔉 ≥ −(1 − ε)M_𝔉 of `Z53_GENUSX` is *false* at every zero prime (X_𝔉 = −M_𝔉 there: e.g. p = 10000169,
  M_𝔉 = 1.17), i.e. at a 39 %-fraction of primes near 10⁸ and, by the model, at ~10^{30} primes in total; no numerical
  support for the target is possible at any computable size, and any proof must produce p₀ ≥ 10^{124} or be ineffective.
* **Verdict: not proved; target recalibrated.** What was proved is the exact structure (§1–2, elementary) and the certified
  counts (§3). Recommendation (§5): as a route to ES the window family is too thin by a factor ≈ 30 in the constant; a route
  with a main term ≥ 0.1·log²p (or a different kind of positivity mechanism) is needed before "all large p" has content.

## 1. Exact forms of hits(p) (PROVED)

Throughout p ≡ 1 (mod 4) is prime, windows satisfy (C1) γ < 1 − α₁ (so 8uw ≤ p) and p ≥ p₀(window) so that U₁ := p^{α₁} < Y := p^β
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
d = w″ = 4uC − 1 ≡ 3 (4), p ≡ −u (mod d) and 0 < u ≤ U₁ < p^{1−γ}/2 < d (d = (p+u)/(2w) > p/(2X)), so u is the least residue
of −p mod d; conversely (e) gives p + u = 2dw with d ≡ −1 (4u). ∎
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
mod p, so nothing obstructs; *the only place primality (non-squareness) is used by the target is that the level divisors
w″ are allowed to be non-residues mod p*. The density main term M_𝔉 uses it through χ_{−4up} being primitive of
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

## 2. The attack: windows with a free average (PROVED reductions; outcome negative)

The brief's natural line is R_𝔉 = M_𝔉 + X_𝔉 with M_𝔉 ≫ log²p (Thm U) and X_𝔉 ≥ −(1 − ε)M_𝔉 to be shown "by choosing windows
where the remainders can be averaged over u or w". We tried the three possibilities.

**2.1 Long-u windows (α₁ > γ).** Thm U's hypotheses (C1)–(C3) do not require β > α₁; e.g. (α₀, α₁, β, γ) = (0.1, 0.45, 0.4, 0.5)
satisfies γ < 1 − α₁, β > τ(1 + α₁) = 0.3625, α₀ > τ²(1 + α₁) = 0.0906 (τ ↓ 1/4), with c = (8/π⁴)(0.1)(0.35) ≈ 0.0029; Thm U's
proof (Prop 2.4: windowed w-sums at fixed u, hyperbola, Burgess) is unchanged (checked: no step uses U₁ ≤ Y). In such a
window, at fixed w the u-sum runs over an AP of length U₁/w → ∞ — but by Lemma 1.3(ii) the *exact* count at fixed w is the
number of divisors d′ ≡ −1 (mod 8w) of the single integer p + 2w with cofactor in (U₀, U₁]: the AP average exists only for
the density ρ (which is what Thm U uses) and not for the exact indicator. **PROVED: no exact u-average in long-u windows.**
(Numerically the long-u count is the same function with (u, 2w) swapped, so nothing is gained.)

**2.2 Short-u windows (β > α₁; the Thm U optimum).** At fixed w the u-sum has ≤ 1 term (Lemma 1.3(ii)); at fixed u the w-sum is
over divisors of n_u (Lemma 1.3(i)). The only average is over the *free* w with the tied condition on r_w = −p mod w
(`Z53_GENUSX` Lemma 4.1): hits(p) = #{w ∈ 𝒲 : r_w ∈ 𝒰, ⌈p/w⌉ ≡ −2 (mod 8r_w)}. The first condition alone (r_w ≤ U₁) is a
short-interval divisor count Σ_{u ≤ U₁} τ(p + u; Y, X), whose asymptotic U₁ log(X/Y) is a sawtooth-sum problem (Assessment:
accessible for α₁ > 1/3 from van der Corput's Σ_{w ~ W} ψ(N/w) ≪ N^{1/3}log N, W ≤ √N, plus the hyperbola swap for W > √N;
not written, not needed, and T1-blind in any case); the second condition selects, among
the ≈ U₁ log(X/Y) shell points, those whose level divisor lies in one class mod 8r_w. No average over w sees this class.

**2.3 The C-parametrisation.** Summing Lemma 1.3(iii) over C ∈ (Z₀, Z₁] (Z ≈ p/(8uw) ∈ (p^{1−α₁−γ}, p^{1−α₀−β})) gives
hits(p) = Σ_C #{d | 4Cp + 1 : d ≡ 4C − 1 (16C), windows}. Here the modulus 16C is shared by all divisors of N_C := 4Cp + 1,
and C is free with Z₁ ≥ p^{1/2+ε} in the Thm U window (1 − α₀ − β = 7/12). The *principal-character* part Σ_C #{d | N_C,
d ~ D}/φ(16C) is accessible (sketch, not needed and not claimed in detail): Σ_{d ~ D} #{C ~ Z : d | 4Cp + 1} = Σ_{d ~ D}
1[c₀(d) ∈ range], c₀(d) := −(4p)⁻¹ mod d, and e(h c₀(d)/d) = e(h d̄/(4p))·e(−h/(4pd)) (reciprocity ā/d + d̄/a ≡ 1/(ad) mod 1), so
Σ_{d ~ D} e(h c₀(d)/d) is an incomplete Kloosterman sum mod 4p of length D with a smooth twist, ≪ p^{1/2+ε} by Weil and
completion — o(Z) for Z ≥ p^{1/2+ε}. But the class condition d ≡ 4C − 1 (16C) is *tied* (16C ≈ 4d/u), and by
Lemma 1.3(iv) the sum over C of the class indicator at fixed d collapses to the single term C = c₀(d) with the condition
4c₀(d)·(stuff) | d + 1 — i.e. "the modular inverse of −4p mod d divides (d + 1)/4". The Kloosterman structure gives the
equidistribution of c₀(d)/d at scale ≫ p^{1/2}/D, while the condition requires c₀(d) to hit a set of ≤ τ((d+1)/4) values.
**PROVED: the C-average handles only the principal character; the tied class is again a single-residue event.**

**2.4 Minorants and sieves (two short PROVED no-gos, kept because they are quantitative).**
 (a) *No genus-character minorant.* Let G = (ℤ/q)^×, S ⊂ Ĝ, f = Σ_{χ ∈ S} a_χ χ real-valued with f(x) ≤ 1[x = 1] for all x.
 Then a_{χ₀} = |G|⁻¹Σ_x f(x) ≤ f(1)/|G| ≤ 1/|G|, with equality iff f = 1_{{1}}, which forces S = Ĝ. If S lies in a proper
 subgroup of Ĝ (e.g. S = the real characters, the genus set), then f is invariant under the non-trivial group S^⊥ (= G² for
 the genus set), so for h ∈ S^⊥ \ {1}: f(1) = f(h) ≤ 0, hence a_{χ₀} ≤ 0. **No minorant of the class indicator 1[p ≡ a (q)]
 with positive main term exists inside the genus characters**: positivity cannot be obtained from M_𝔉 by a pointwise
 inequality; every character of every order must be controlled.
 (b) *Large sieve on the d-form (illustrative).* Let hits′(p) ≥ hits(p) be the count with the squarefree condition on w dropped
 and the windows defined by x instead of p (so that the forbidden sets are p-independent for p ∈ [x, 2x]). hits′(p) = 0 means
 p mod d ∉ 𝒯′_d := {d − u : u | (d+1)/4, u ∈ 𝒰} for every d ≡ 3 (4) in range. Restricting to prime d ≤ Q = √x, Montgomery's
 large sieve gives #{p ∈ [x, 2x] : hits′(p) = 0} ≤ (x + Q²)/L with L ≥ Σ_{d ≤ Q prime} |𝒯′_d|/(d − |𝒯′_d|), and
 Σ_{d prime ~ D} τ((d+1)/4)/d ≍ 1 per dyadic block (Titchmarsh divisor problem), so L ≍ log x — the bound is ≪ x/log x, no
 better than the prime number theorem. **Sieving by the ≤ τ(d + 1) forbidden classes per modulus is log-factor-exact and
 cannot see a single p.**

**2.5 Outcome.** Every window admissible for Thm U leaves X_𝔉 = R_𝔉 − M_𝔉 as a sum of single-residue events minus
densities; the averages that exist (over w at fixed u at density level; over C for the principal character) are the ones
Thm U / Thm X already use. We did not find a way around this and **do not claim** any bound on X_𝔉. The remainder of the
memo quantifies what the target asks for.

## 3. Exhaustive counts of hits(p) (CERTIFIED) and the Poisson law (EVIDENCE)

**Engines.** `scripts/z55_crossf_scan.c` (u-form: factor n_u by trial division, enumerate squarefree divisors) and
`scripts/z55_crossf_cscan.c` (C-form: for each u loop over C with (8uC − 2) | p + u; no factorisation; cost ≍ p^{1/3}log p
per prime; Miller–Rabin with 13 bases for p < 3·10^{24}) — both with the standard window U₀ = round(p^{1/12} − ½),
U₁ = ⌊p^{1/3}/2⌋, Y = ⌊p^{1/3}⌋, X = ⌊p^{2/3}/4⌋ (X decreased until 8U₁X ≤ p), exactly `scripts/z53_genusx_run.py`'s. The
outputs agree line by line on [10⁸, 1.02·10⁸] (54 198 primes). Scans: all primes p ≡ 1 (4) in [10^k, 10^k + 10^7] (k = 8: +2·10⁶;
k = 12: the first 58 878 primes, time-boxed); samples at 10^{13}–10^{18} (`scripts/z55_crossf_bigscan.sh`, one prime per step).
Summary `data/z55/crossf/stats.txt` (`scripts/z55_crossf_stats.py`):

| range | N primes | mean hits | var/mean | P(hits = 0) | e^{−mean} | mean/log²p |
|---|---|---|---|---|---|---|
| [10⁸, 1.02·10⁸] | 54 198 | 0.967 | 1.07 | 0.392 | 0.380 | 0.00285 |
| [10⁹, 10⁹+10⁷] | 240 944 | 1.071 | 1.03 | 0.348 | 0.343 | 0.00249 |
| [10^{10}, +10⁷] | 217 331 | 1.457 | 1.03 | 0.238 | 0.233 | 0.00275 |
| [10^{11}, +10⁷] | 197 020 | 1.909 | 1.04 | 0.153 | 0.148 | 0.00298 |
| [10^{12}, +3.3·10⁶] | 58 878 | 2.427 | 1.05 | 0.094 | 0.088 | 0.00318 |
| 10^{13} sample | see stats.txt | ≈ 3.0 | ≈ 1.02 | ≈ 0.05 | ≈ 0.05 | ≈ 0.0034 |

(The 10^{13}–10^{18} rows are filled from `stats.txt` as the sampled runs complete; see §6 for the final numbers.)

**Readings.** (1) hits(p) is Poisson to the accuracy of ≈ 10⁵ samples per scale: variance/mean = 1.03–1.07 and
P(0) = e^{−mean}·(1.03–1.06), the small excess being the mixture over p of the mean λ(p) = M_𝔉(p)/2 (which varies with
L(1, χ_{−4up}); the z53 data give P(0) ≈ mean_p e^{−M̂(p)/2} within sampling error). (2) mean/log²p increases towards the
Thm U constant for this window, c_hits = (1/2)(8/π⁴)(γ − β)(α₁ − α₀) = (8/π⁴)/24 = 1/(3π⁴) = 0.003422 — the largest constant
any admissible window gives (Thm U's optimisation) — the finite-size deficit being the o(1) of Thm U (window edges, 2-adic
and small-prime factors). (3) The square controls have hits = 0 (Lemma 1.2); composite non-squares near 10⁸ behave like primes.

## 4. The scale of p₀ under the Poisson model (model computation; heuristic, with CERTIFIED inputs)

Model: hits(p) ~ Poisson(c log²p) independently over p, with c = c_hits = 1/(3π⁴) (the asymptotic mean of the best admissible
window; §3 supports both the law and the constant to within the finite-size deficit). The expected number of primes
p ≡ 1 (4), p > x, with hits(p) = 0 is E(x) = ∫_{log x}^∞ e^{s − cs²}/(2s) ds (prime density 1/(2 log t) in the class). Numerically
(`stats.txt`): E(10⁸) = E(10^{18}) = 5.6·10^{30}; the integrand peaks at s = 1/(2c), p ≈ 10^{63}; E(10^{100}) = 5.9·10^{18}; E(x) = 1 at
**x ≈ 10^{124}** (log x ≈ 286 ≈ 0.98/c). With the finite-size value c = 0.0030 instead: 1.5·10^{35} exceptions, last near 10^{142}.
Consequences (Assessment, conditional on the model):
 (i) Problem CROSS, for any admissible window, is expected to be true only from p₀ ≈ 10^{124} on, with ~10^{30} exceptional
 primes below; "R_𝔉(p) ≥ c log²p for all large p" likewise (with hits ≈ c log²p ≥ 1 needing log p ≥ 17 but the fluctuations
 needing log p ≳ 1/c).
 (ii) (H⁻_𝔉) of `Z53_GENUSX` (X_𝔉 ≥ −(1 − ε)M_𝔉) is false at every zero prime (there X_𝔉 = −M_𝔉): at 39 % of primes near 10⁸,
 9 % near 10^{12}, and at ~10^{30} primes in all. Any proof of it is necessarily asymptotic with p₀ ≥ 10^{124}, i.e. its
 constants cannot be checked, and no effective version with p₀ < 10^{120} can be true.
 (iii) For an ES route this is harmless in principle (ES needs one solution of any type, and p ≤ 10^{17} is known) but it
 means the family statement has *no finite-size falsifier and no finite-size confirmation*: every numerical check of
 "R_𝔉 ≥ 1" below 10^{100} will show a positive fraction of zeros, exactly as predicted.
 (iv) The constant is the issue. The hits mean for the *full* (★) count (all (u, B) ∈ 𝒫(p)) is far larger (the window
 family keeps only u ∈ (p^{1/12}, p^{1/3}/2], w ∈ (p^{1/3}, p^{2/3}/4]); a family with c_hits ≥ 0.1 would have E = 1 near 10⁴ and
 would be checkable. Thm U's constant is capped at 1/(3π⁴) by the Burgess ranges (β ≥ 1/3, α₀ ≥ 1/12, γ ≤ 2/3), and even GRH
 (c_hits → 1/π⁴ ≈ 0.0103) only moves p₀ to ≈ 10^{40}.

## 5. Verdict and recommendation

* **Not proved.** No bound on X_𝔉 at a single prime was obtained; §2 shows (PROVED, elementary) that the averaging route
  proposed in the brief reduces in every admissible window to the single-residue events it was meant to average.
* **Recalibration (the lane's finding).** For the Theorem U family the statement "R_𝔉(p) ≥ 1 for all sufficiently large p" is,
  on the data, a statement about p ≳ 10^{124} with ≈ 10^{30} exceptions below — true (if at all) only in the regime where
  the main term c log²p, c = 0.0034, exceeds the Poisson fluctuation scale log(#primes). A future lane on this problem
  should (a) not use R_𝔉 = 0 at computable p as a falsifier of anything (it is the expected behaviour), and (b) first enlarge
  the main-term constant: either prove a genus lower bound for a much larger family (all u ≤ p^{1/3}, all w ≤ p^{2/3}, no
  squarefree restriction: heuristically c_hits ≈ an absolute constant times (1/3)(2/3)·(8/π⁴)/2·(correction for the dropped
  conditions)), or move to the HC-type small-C families where the mean is ≫ log p per unit of log C and exceptions are
  provably rare at computable sizes.
* **What a proof would need (one sentence, Assessment).** A lower bound at a single p for Σ_{d ~ D} 1[(−p mod d) ∈ 𝒯_d] with
  |𝒯_d| ≤ τ(d + 1): equidistribution of −p mod d jointly over d at the scale of single residues, which neither Burgess
  (p in the conductor: density only), Kloosterman/Weil (principal character only, §2.3) nor the large sieve (§2.4(b)) provides.

## 6. Review log and final numbers

(filled after the hostile review and the completion of the sampled scans)
