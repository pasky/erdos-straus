# AGENT REPORT O272 — the 2-power ladder above the BM layer (spark relay of O271 SHARP 1 + sparks 1, 3)

Branch `side-agent/two-power-ladder` (merged `side-agent/synthesis-nine` first; README conflict resolved keeping both z39 and
s9 blocks). Main file `TWO_POWER_LADDER.md`; memos `BRAINSTORM/z41_{ceiling_chebotarev_schinzel, stickelberger_dictionary,
choosable_ladder, two_group_levels, cubic_hecke_shadow}.md` (indexed); scripts `scripts/z41_{ladder_test, stickelberger,
minus_l, two_group, two_group_1e7, twisted_levels}.py`; tiny logs `logs/z41_*`. **ES is not solved; no infinite case for primes
is claimed.** Outcome: a precise NEGATIVE, plus one clean structural dictionary.

## SHARP (modest; judge for yourself)
1. **Stickelberger dictionary (TWO_POWER_LADDER Thm 3.2, PROVED for m = 3, 4, sharp by Kummer independence).** Write the
   Frobenius of a split forced prime ℓ at the level prime 𝔮 | q as a vector x_a = (σ_aλ/𝔮)_m, a ∈ (ℤ/m)^×. The forcing
   (ℓ | tn + 1 ⟺ t ≡ −n⁻¹ mod ℓ) sees exactly the **Stickelberger component** S = (q/λ)_m = ∏x_a^{a⁻¹}; the ES event (a
   Dirichlet character mod t at ℓ) needs the **norm component** D = ∏x_a. D/S = ∏x_a^{1−a⁻¹}, exponents generate gcd(2, m)·ℤ/m,
   so S determines D exactly modulo μ_m^{gcd(2,m)}. For m = 2 (K = ℚ) S = D: **that coincidence is the whole BM layer and the
   whole of T1**; there is no odd-order BM layer and no odd-order T1 transported by the forcing (cubes bias only an
   anti-cyclotomic cubic Hecke character, conductor | 9t, invisible to "d ≡ −1 (t)"). Checked: (q/λ)₃ = x₁x₂² on 882/882 pairs;
   reviewer checked the m = 4 exact-sign identity on 1 892 pairs.
2. **The brief's "shrink to the odd part" holds — trivially — at levels t = 4q, q ≡ 3 (mod 4) (Prop 4.1(c), PROVED):** if
   ℓ ≡ 3 (4) and (n/ℓ) = −1 (such ℓ exists iff n is not a square), every forced level 4q with q ≡ 3 (4) has −ℓ in the odd-order
   subgroup of (ℤ/4q)^× — the 2-Sylow is (ℤ/2)² with characters χ_{−4}, χ_{−t}. Useless for ES (the odd part has (q − 1)/2
   classes, and a prime < t − 1 is never ≡ −1), but it is the exact form of what was hoped for.

## Results by goal
* **(1) Decisive test FIRST (EVIDENCE + Thm 3.1 PROVED).** Along forced progressions t = 4q ≡ −n⁻¹ (ℓ): the quadratic part of ℓ's
  class mod q is constant (24/24 progressions); 4th/8th/16th-power parts occur at 1/2, 1/4, 1/8 (Chebotarev), for squares,
  131, 241, generic n alike. Thm 3.1 (ℓ ∤ m): for one varying level prime, NO congruence on the level determines the m-layer
  beyond its quadratic part (K(ℓ^{1/d})/ℚ abelian ⟹ d | 2). This is (J)93 / CLASS_FORCING Thm 2.1 transported to level
  coordinates — not new as mathematics. Spark 1's predicted obstruction is confirmed.
* **Construction attempt (§4).** Violating "congruence data on the level": the m-layer at ℓ is an exact function of the
  Gaussian/cyclotomic lift of q mod ℓ (0 clashes), so the whole 2-part is CHOOSABLE by choosing q (Prop 4.1(b′), positive
  density, Chebotarev) — choosable ≠ forced. Prop 4.2 (size obstruction): a divisor in class −1 has size ≥ t − 1; once it is
  fixed the level is the residue of −n⁻¹ mod d — the lottery itself.
* **(2)/(3) 2-group levels t = 2^k·F (F | 3·5·17·257·65537).** Lemma 1.1: at a fixed level the event is ⋃_a{n ≡ −a (ta − 1)}
  (B1). Census (exact (★) certificates): 1 298 primes ≤ 10⁶ and 5 320 ≤ 10⁷ have no word at any 2-group level (1 180 of the
  former do have (★) words at other 4 | t levels; all-level (★) failures: 118 primes ≤ 10⁶); failure rate per decade 0.217,
  0.069, 0.029, 0.0136, 0.0069. Lemma 5.1 (PROVED): n = Dm² has no word at any level 4D | t. Controls: 0 squares hit; 131, 241
  have no 8 | t word. So 2-group levels do not suffice, and they are not forced.
* **(4) Spark 3 (Cor 6.1, PROVED, narrow scope).** No family of n biases the cubic Dirichlet layer through the forcing
  congruence (fixed n, ℓ; varying level prime). Joint restrictions on the varying prime factors of tn + 1 are NOT excluded.
* Barrier screen: (J)93 — the catch is that the forcing transports only t mod ℓ (abelian), the class needs non-abelian
  Frobenius of the level prime; B1 (fixed levels = congruence unions); B2 (lottery relocated to the odd part / large factors);
  T1 explained (m = 2 coincidence).

## Self-review (deep reviewer) — applied, marked ⟨rep⟩ in the file
No FATAL. 7 MAJOR repaired: Thm 3.1 needed ℓ ∤ m and 4 | lcm(M, m) (counterexamples m = 12, ℓ = 3; m = 6, M = 7); the "compatible
choice of 𝔮" was ill-defined (now conjugacy-invariant events / averaging over pairs); the cited Schinzel "iff" was false
(central extensions) — replaced by a direct commutator proof of the needed direction; Prop 4.1 omitted q ≡ 1 (m) (over all
forced q the fractions are 0.75/0.69/0.67) and the "choose m afterwards" step (fixed via v₂(q − 1) = j; forced case q ≡ 3 (4)
added); the "class carried by the cofactor" claim was false ([N/ℓ] = [ℓ]⁻¹); the cubic Hecke conductor divides 9t, not t
(explicit counterexample 757); scope of Cor 6.1 / summary narrowed. Minors fixed (Lemma 1.1 subtraction, boundary divisor
d = t − 1, misassigned fractions, "only m² by this mechanism", certificate docstring, duplicated log line, "known" Fermat primes).
Reviewer reproduced all six scripts' outputs.

## Sparks (not pursued)
1. **Make S ES-visible:** an ES variant whose levels live in ℤ[ω] or ℤ[i] (divisor ≡ −1 modulo a Gaussian/Eisenstein level τ)
   would see the Stickelberger component, which the forcing DOES pin — is there a descent from such certificates to rational
   ones (τ a norm, e.g. t = N(τ))? Probably no positivity, but the dictionary is exact.
2. Joint restrictions not covered by Cor 6.1: composite levels t = 4q₁q₂ with q₁, q₂ forced at two different small primes —
   the joint non-abelian Frobenius of (q₁, q₂) is choosable; does a two-prime product d = ℓ₁ℓ₂ ever get pinned to −1?
   (Prop 4.2(b) suggests no: d fixes t.)
3. Fit the 2-group failure rate (≈ halving per decade) against the BM-corrected expected number of T2 hits; small-odd-part
   levels t = 4q with (q − 1)/2^{v₂(q−1)} ≤ B as an intermediate family between T2 and all levels.
4. Complete Thm 3.2 for all odd prime m via Eisenstein reciprocity with ideal symbols (class number issues).
