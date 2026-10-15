# AGENT_REPORT O236 — pointwise minimal exponent cap e*(n) (spark relay Z6)

Branch side-agent/cap-pointwise (merged side-agent/cap-interpolation and side-agent/review-cap-interp). Main file
CAP_POINTWISE.md; memos BRAINSTORM/z12_{window_cap,typeI_dichotomy,grh_lattice_gap}.md; scripts scripts/z12_*;
data data/z12_*. **ES is not solved; no infinite case of ES is claimed.** Normalisation: ES(n) ⟺ e*(n) = 0, so
"e*(p) = 0 numerically" is just the known ES verification. The informative numerics are about window constructions.

## SHARP:
**Self-generated mute set ⇒ first unconditional polynomial pointwise cap (CAP_POINTWISE Thm 1.1, 1.3; PROVED).**
Take a prime window q = 4x − n with q ≡ 4 − n (mod 8), (q/n) = −1, and let the mute primes be the prime factors of
x = (n+q)/4. Since 4x ≡ n (mod q), firing needs only −1 ∈ ⟨primes of x⟩ mod q. Reciprocity gives (x/q) = −1, which
forces that (cyclic group of order 2·odd). So ES^{(y,e)}(n) holds with e < q. Hence:
e*(n) ≪ rad(n)^5 effectively (Linnik–Xylouris) for every odd n > 1;
e*(n) < 2^{201232} n^{50308} explicitly for non-square n (Ahn–Kwon d_L^{12577}, L = ℚ(i, √2, √n₀));
e*(n) ≪ (log n)² under GRH, explicitly (16 log n + 70)² for non-square n.
**Dictionary:** the cap e is exactly the overflow of the window's exponent budget (Lemma 3.1: cap = max_s (a_s − v_s(x))⁺).
The subgroup level of a Type II window is forced; only the budget is a lottery.
**Dichotomy (Prop 4.1):** Type I windows carry the opposite forced sign, (a/p) = +1, so they are never forced and are
dead at every cap when (pk′+1)/4 is prime.
Novelty is modest and honest. Finiteness of e*(n) was FROBENIUS_FIRING Thm 4.2 (ineffective). The subgroup step is
POINTWISE_SIZE Cor 8.3(b). What is new is connecting it to EXPONENT_CAP's overflow dictionary (LITERATURE_2026 (vii)
corrected accordingly).

## Results
1. Thm 1.1 (prime windows) and Thm 1.1′ (composite windows, every prime factor ≡ 3 (4) a non-residue mod n); Cor 1.2
   covers all odd n (odd squares go through a prime p | a with extra classes mod ℓ | a); Thm 1.3 gives the bounds
   above. Remark 1.4: B6 is evaded (one Chebotarev prime, no averaging) and B3 is evaded (no counting). B2 is
   respected: the shot modulus (n + 4Q²)/q is huge. T1 is respected: no window exists at an odd square.
2. §2 (goal 2, Assessment, tentative). Below the covering threshold, cap ≤ e is a divisibility lottery (Lemma 2.1).
   Whole-lattice covering under GRH loses the factor P = ∏S and reproduces exp(O(√(log₂p log₃p))). An input that
   would remove the loss: equidistribution mod P of the primes carrying short multiplicative relations among the
   first k primes. This is not a necessity theorem. The R237 calibration is incorporated: with the full 𝒟_e the
   almost-all side has a power saving at e ≥ (log N)^{1+ε}.
3. Numerics (EVIDENCE), all primes p ≡ 1 (4) ≤ 10⁶ (39 175):
   * q*(p) ≤ 227, and max q*/log²p = 2.84 (p = 4349).
   * The cap at q* is ≤ 41.
   * The best cap over windows m ≤ 1000 is ≤ 3, whether prime-only or with composites.
   * Every q*-solution was rebuilt and checked exactly: 127 821 exact checks.
   * All 49 776 non-squares n ≡ 1 (4) ≤ 2·10⁵ were checked exactly.
   * T1: 0 windows at odd squares.
   * Mordell-hard classes: mean q* 22.7 vs 17.1 elsewhere.
4. Goal 4: Type I shape adds no forced dimension (Prop 4.1, 612 identity checks, 0 violations in 95 dead windows).

## Self-review (deep reviewer subagent; all repairs applied)
* Prime-window minima bug fixed (prime-only max cap is 3, not 5).
* The false "q*/log²p ≤ 1.3" is replaced by 2.84.
* Cap 0 is only the square-shot sub-family of the Type II window. Example: p = 241, m = 11 has a general Type II
  solution but square-shot cap 1.
* GRH claims are restricted to non-square n. For those, q ∤ n is automatic, since q ≡ 3 (4) and all primes of n are
  ≡ 1 (4).
* §2 is softened to a tentative limitation of the covering argument.
* Minor fixes: Q = 1 case, a symbol clash, the size of g.
* The Ahn–Kwon and Bach–Sorenson (Thm 5.1) statements were reported confirmed by the reviewer subagent; I could not
  access the PDFs, so the parent should re-check.

## Sparks (not pursued)
1. Unconditional q*(n) ≪ n^{1/4+ε}? This needs a least prime with prescribed (χ₋₄, χ₈, χ_n) values, a Linnik–Vinogradov /
   Pollack-type argument for a coset of index 8. The Vinogradov trick fails for a non-cyclic pattern; is there a
   Burgess-based substitute?
2. Use the general Type II window (any d | K², not just d = Q²) with the cap. Does the forced-parity argument give
   cap ≤ λ(m)/2 or better, using divisors d with odd exponents?
3. Window-cap distribution: the cap at q* behaves like a discrete log (large when K has few prime factors). Does the
   minimum over the first k windows decay like a product of independent lotteries? Data: max 3 over m ≤ 1000.
4. Multi-window certificates. Combine two windows q₁, q₂ (composite windows with prime factors in both sign classes
   fail Thm 1.1′). Is there a CRT gluing that keeps the forced sign?
5. Order-3 analogue: in the ℤ[ω] T1 of (J)19, is there a self-generated mute set with forced cubic-residue parity?
