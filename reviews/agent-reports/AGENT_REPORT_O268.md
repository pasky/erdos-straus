# AGENT REPORT O268 — BM-corrected count for (★): Brauer character, unconditional main term, remainder

Branch `side-agent/bm-corrected-count` (merged side-agent/single-p-count and main). Main file `BM_CORRECTED_COUNT.md`;
memos `BRAINSTORM/z38_{brauer_character, mbm_unconditional, two_sided_false, markoff_precedent, shared_brauer_character,
numerator8_control}.md`; scripts `scripts/z38_{bm_dictionary.py, mbm.c, check_mbm.py, stats.py, hx.py, zero_bins.py,
zero_law.py, zero_growth.py, typeII_check.py, b1.c, b1_stats.py, thm22_check.py}`; log `logs/z38_summary.txt`.
**ES is not solved. No "standard conjecture ⟹ ES" was obtained.**

## SHARP
1. **BL's Brauer class is exactly one character in the pair expansion (PROVED, Thm 1.1).** For every (★)-pair (u, B), at the
   rational point P_{u,B} = (uBC, pBC, puC) (C ∈ ℚ), inv_p α = (−uB/p) = χ_{−4uB}(p), and χ_{−4uB}(−(u+B)) = −1 identically
   ((u+B) | (u−B)² + 4uB). So principal + χ_{−4uB} = φ(q)^{−1}(1 + inv_∞ inv_p), a factor of Borovoi–Rudnick shape at integral points (R279 repair: no BR theorem applies to U_n) (at non-hit
   rational points the invariants at ℓ | 2uB are dropped: a heuristic density, not a BR theorem). Answers R277 D3
   ("is BL's symbol a product of genus characters?" — it is a single one, χ_{−4uB}); refutes O260's "genus = BM". Same on all
   of Type II (χ_{−4ab}, independent of c, d), on the b = 1 line (χ_{−4xy} in mutual-shift coordinates), and for m/n with 4 | m. The
   board's F4 projector (1 − χ_p(ab))/2 IS this class (for p ≡ 1 (4)).
2. **The BM-corrected singular series is ≫ (log p)² unconditionally (PROVED, Thm 2.2).**
   M_BM(p) = Σ_{𝒫(p)} (1 − (−uB/p))/φ(4uB) ≥ (3/(16π²) − o(1))(log p)² (Burgess; 1/(32π²) with PV), using only positivity of
   the pair terms + a uniform bound for Σ_{k≤t}χ(k)/k. Under GRH M_BM ∼ M₀ ∼ (3/(2π²))(log p)² (Prop 2.3, via
   Granville–Soundararajan; this is board F4 obligation (i), now derived). M_BM vanishes at squares. So the (L) half of O260's
   split is now a theorem (for the geometric main term; R277 D2 resolved in this form). Numerically min M_BM/L² = 0.062 over
   primes ≤ 10⁶, mean 0.149.
3. **Exact conditional with an unconditional main term:** (★) (hence ES) for p > p₀ ⟸ H⁻_BM(ε, p₀): R(p) ≥ ε·M_BM(p).
   Not refuted by T1 (0 = 0 at squares). Honest: H⁻_BM is ES-(★) in disguise up to ε (single-integer lower-tail statement),
   no implication from a standard conjecture is established (none known).

## Results by goal
* (1) Dictionary: SHARP 1. Checked with exact Hilbert symbols at all places (9 440 pairs, primes and squares < 400).
* (2) (L): SHARP 2. (M_gen itself still only ≫ log log p; we did not need it.)
* (3) H_X: **two-sided H_X is FALSE infinitely often (Prop 3.1, PROVED via Linnik)**: R(p) ≥ exp(c log p/log log p) for
  infinitely many p ≡ 1 (4), while M_BM ≪ log²p, M_gen ≪ log⁴p. Only one-sided H⁻ is meaningful. Numerics, all primes ≤ 10⁶
  and all odd n ≤ 10⁶ (C engine; R exact, main terms in double precision): 17 (★) failures among primes (9 ≡ 1 (8), 8 ≡ 7 (8)); H⁻ needs
  p₀ ≥ 8.9·10⁶ (census); at fixed M (M_BM8, after the self-review fix) the zero rate is ≈ 1.5–2.8× swap-Poisson e^{−M/2}
  for M < 22, 5–15× beyond (only 6 zeros); primes and composites show comparable rates (small counts). Standard-conjecture
  audit (§3.3): none is single-integer; no implication established.
  Literature calibration: Markoff surfaces (Ghosh–Sarnak; same (log)² mean) have infinitely many integral Hasse failures
  with non-empty BM set (Loughran–Mitankin Thm 1.5, CTWX Thm 5.8); "mostly non-BM" only if GS's B^{0.89} numerics hold.
* (4) b = 1 / union: (★) and b = 1 are shifts −(x+y), −(4x+y) mod 4xy with the same χ_{−4xy}; b = 1 needs the mod-4 character
  (bare M_BM diverges). Residuals positively correlated (0.21–0.30): the union's robustness is a doubled main term, nothing
  forced. Reproduces b = 1 exceptions 193, 2521, 66529.
* (5) Assessment: genuine but bookkeeping-level improvement on CONDITIONAL_ES (hypothesis T1-consistent; main term proved);
  no "ES ⟸ GRH + natural equidistribution". k = 8 control: same Brauer character; the 8/n c = 1 line fails at 835 primes
  ≤ 10⁶ incl. 131, 241 (M_BM = 0.56, 0.46) — the H⁻ analogue fails there, as it must.

## Checks
T1: all 499 odd squares ≤ 10⁶ have R* = M_BM = M_BM8 = 0. Engine `z38_mbm.c` cross-checked against brute force
(`z38_check_mbm.py`, incl. composites and M_BM8) and against z30_rgen's M₀. Thm 2.2 sub-family sums computed at 409, 102001,
712321 (0.025–0.030 L² for δ = 1/2, above the worst-case 0.019). Type II / m/n identities: `z38_typeII_check.py`.

## Honest limits
Thm 2.2's constant is small (12 % of M₀). Prop 2.3 relies on the Granville–Soundararajan GRH bound (R279: checked, GS Theorem 2; earlier caveat: not re-read in
full). The Markoff comparison is literature-level (GS Thm 1.2(i)'s log-power quoted inconsistently between sources; stated
as ≫ √K/(log K)^c). M_BM8 (mod-8 refined) is used numerically only. Zero-law fits are at ≤ 10⁶.

## Sparks (not pursued)
1. A Ghosh–Sarnak-type structured failure family for (★): descent through a singular fibre + reciprocity (their k = 4 + βν²).
   The ES surface's singular point (origin) and BL Thm 1.9's real obstruction are the candidates; a "prime T1" would be the outcome.
2. Prove M_gen ≫ (log p)²/(log log p)^A via M_gen ≥ ? M_BM-type positivity on sub-families (u prime) + averages of L(1, χ_{−up}).
3. Large-deviation model for the lower tail: the excess over swap-Poisson grows at fixed M; test a compound model with
   clusters from shared integers p + u, p + B, 4Cp + 1 (O260 spark 1) at fixed M_BM.
4. Use the unconditional Thm 2.2 inside an *average over a thin family of p* (e.g. p in a short interval or p ≡ 1 mod Q) to get
   unconditional "(★) for all but O(x^θ) primes" with an explicit θ < 1 via a variance bound à la Ghosh–Sarnak §9.
5. The Brauer character for Type I families (f | p² + 4c²d): compute and check whether M_BM^{I} has an unconditional
   (log p)³-scale lower bound (Type I mean is larger).
