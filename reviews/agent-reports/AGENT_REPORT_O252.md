# AGENT_REPORT_O252 — forced divisor at a forced window (FORCED_WINDOW.md), checkpoint 1

Branch side-agent/forced-window. Main file FORCED_WINDOW.md; memos BRAINSTORM/z24_{level_dichotomy, crt_shortfall,
balanced_primes_W, forcing_generation_gap, budget_not_mechanism}.md; scripts scripts/z24_{least_window, balanced, thm43_check}.py;
data/z24/ (tiny). **ES is not solved; no infinite case of ES is claimed.**

## SHARP:
1. **Conditional (log log p)^{2+o(1)} cap (Thm 4.3 + Cor 4.4).** Hypothesis W — for every large p there is a prime q ≤ X(p) ≈ P(y)²log⁴p
   in the class −p mod P(y), q ≡ 3 (8), (q/p) = −1, whose relation lattice of the squares of the odd primes ≤ y is balanced (a property
   of q alone) — ⇒ e*(p) ≤ L − 1; with random-lattice L and y = log₂p·log₃p: e*(p) ≤ (log log p)^{2+o(1)}. Turns z12_grh_lattice_gap's
   Assessment into a conditional theorem; covering-method floor (log log p)^{1−o(1)}. Numerics: every admissible class mod 840 / 9240
   contains a q with (L_min+1)/|U_q|^{1/k} < 1.372 / 1.472 (balance part only).
2. **Least-residue form of cap 0 vs decoupling at cap ≥ 1 (Prop 2.1/2.2, PROVED identities; reading Assessment).** Every cap-0 window
   certificate is a coprime (u, v) whose window is the least positive residue of −p mod 4uv, 4uv ≥ 2m (modulus ≥ 2 × the window;
   ≤ p as a congruence on p). At cap ≥ 1 the p-modulus (4s² for the one-prime witness) is independent of the window, which can be a
   large prime factor of s^j + 1. (ET Type II reparametrised; the cap-0/cap-1 contrast is the new reading. "Level ≥ 2" in the first
   draft was a misnomer — repaired.)
3. **In the first-success sample the exponent budget is not used (EVIDENCE, 10⁷).** Least cap-0 certificates have |δ| ≤ 1 in 97 %
   (hard primes 90 %) and support ≤ 2 in 99 % (91 %); successful K are not smooth (u 1.93 vs 1.65); forced windows succeed in 2128 of
   2133 tries with τ(K²) ≥ 4m. The brief's "smooth K with big budget" is not how cap-0 windows arise.

## Results (labels as in the file)
* Lemma 1.1 (PROVED): parity split — at a forced window, cap ≤ e ⟸ (sufficient, not equivalent: p = 241, q = 11) the one-sided box of squares of the primes of K contains
  t = −c (c = product of odd-exponent primes): the problem lives in the odd group U_q, quadratic character removed.
* Prop 1.2/1.3 (PROVED): Fourier covering criterion; pigeonhole shows the genericity must be measured at scale 1/L (lattice), not
  "θ ≥ 1/6" (impossible once |U| > 6^k).
* Thm 3.1 (PROVED): covering (not hitting) at cap e needs ∏(2b+1+e) ≥ φ(m)/2 ⇒ windows p^θ ≤ m ≤ 3p need 3(e+1) ≥ (log p)^{θ−o(1)};
  cap-0 covering windows are ≤ p^{O(1/log log p)} (subpower, not polylog). Thm 3.2 + Cor 3.3: CRT in a window interval of length h gives ω(K) ≥ log h/log log h; box ≥ window iff
  log(e+3) ≳ log log h; for cap-0 covering at a CRT window m ≍ h the forced part falls short by the factor ≍ log₃ p.
* Prop 4.1 (PROVED): covering ⟺ balanced relation lattice up to a factor 2; Minkowski floor (log q)^{1−o(1)} for forced generators.
* Prop 5.1 (PROVED rel. GRH): every element of F_q^* is ∏_{s ≤ C log⁴q} s^{δ}, δ ∈ {−1,0,1}. Prop 5.2 (CONDITIONAL on GRH for
  Dedekind zeta functions + Lagarias–Odlyzko): for each odd ℓ, i.o. q ≡ 3 (4) with all primes ≤ c_ℓ log q log log q ℓ-th powers — no all-q generation
  statement holds at the forcing scale y ≤ (1+o(1)) log q ("forcing–generation gap").
* Target (A) not reached: every route to cap 0 is either covering (subpower windows; at polylog windows needs short-interval divisor
  richness + balance) or a target-specific least-residue event; no standard hypothesis found that is not ES in disguise. (B) at
  cap ≤ log p is already GRH-known (CAP_INTERPOLATION Thm 4.2(b)); new: (log log p)^{2+o(1)} under W (random-lattice L). (C) already in CAP_BOUNDED Lemma 3.1 (density 1 − 2^{−π(4C+3;4,3)}). (D) answered in §7.
* Literature screen (§5): smooth shifted primes (wrong scale), smooth numbers in APs/short intervals (average or x^c-length only),
  Erdős–Rényi (random model only), BGK/sum-product (no additive step), Konyagin–Shparlinski (free choice of primes), Bach/Burgess
  (subgroup level, already free). Lichtman's Thm 1.1 was checked by the self-review (fixed shift only); Baker–Harman, Soundararajan,
  Harper, Friedlander–Granville, MV are recalled, not re-checked against primary texts.
* Numerics (EVIDENCE, exact rational checks): least cap-0 windows ≤ 107 for all p ≡ 1 (4) ≤ 10⁷ (record p = 8 803 369);
  765 exact Thm-4.3-style certificates (y = 7); T1 control clean (499 odd squares, windows ≤ 200).

## Self-review (R-O252, reviewer subagent) — all findings on FORCED_WINDOW applied
W was false as first quantified (fixed X; repaired to p-dependent X(p)); "level ≥ 2" misnomer (repaired); Thm 3.1(b) uniformity
(repaired); covering vs hitting conflated in places (repaired, counterexample p = 55 609 recorded); Lemma 1.1 is sufficient only
(p = 241 counterexample recorded); no density-one claim for balanced primes; smooth-shifted-primes bullet corrected (Lichtman fixed
shift; ω not O(1)); 5/2133 (not 2106); support-1 includes 3 prime-power cases; m = 3 split forced/unforced; Prop 4.1 needs integer
sides ≥ 1; Prop 5.1 constants; Prop 5.2 needs GRH for Dedekind zetas; z24_least_window small-input crash fixed. Outside my files the
reviewer flagged ASTRA_BRIEF_DIRECTION2.md:52 (growth-quantifier: successors bounded above by p^λ do not give polylog many
descendants) and checked O242 data as sound (sha256 file has an absolute /tmp path) — for the parent.

## Weak points for the reviewer
* Cor 4.4's exponent 2 + o(1) assumes W at random-lattice L ≈ |U|^{1/k}(log k)^{O(1)}; the lattices are structured sublattices of ℤ^k.
* Prop 5.1 uses the GRH bound ψ(x, χ) ≪ √x log²(qx) (recalled); the constant C is not computed.
* Prop 2.1 is ET Type II reparametrised; novelty is only in the level reading.

## Sparks (not pursued)
* A large-sieve over windows at fixed p: can the least-residue events of Prop 2.1 be counted *on average over the window variable
  with p fixed* by a dispersion argument in (u, v) (Kloosterman-type sums for −p mod 4uv)? This would be the first B6-free count.
* Hypothesis W tested only for k ≤ 4; test k = 5–6 at q ~ 10⁷ and look for classes mod 8P where all small q are unbalanced (P-loss).
* Polylog-short-interval divisor richness (Cor 3.3): is there a Dickson-conditional construction of p with every K in
  (p/4, p/4 + h] having ω ≤ C log h/log log h, i.e. a conditional proof that covering at cap 0 fails i.o. for growing h?
* The support-1 lottery (prime s | jp + 1, s ≡ 3j − 1 (mod 4j)) dominates numerically (92 %): its Landau-type failure probability
  per j and the correlation across j are an explicit model for f_II(p) worth a dedicated heuristic/numeric study.
