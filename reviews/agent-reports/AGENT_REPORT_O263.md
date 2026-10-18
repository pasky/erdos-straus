# AGENT_REPORT_O263 — route (b): class forcing beyond parity (checkpoint 1)

Branch side-agent/class-forcing. Main file CLASS_FORCING.md; memos BRAINSTORM/z33_{forced_quotient_total, kummer_shadow,
forced_factor_criterion, target_davenport, hc_realisation, census_tiers}.md; scripts scripts/z33_{forced_quotient_table,
census, haar_forced}.py; logs logs/z33_*.txt (tiny). **ES is not solved; nothing here advances it.**

SHARP: no breakthrough-grade finding. Cleanest new statement (PROVED, a closing dictionary, not a door):
"reciprocity forces parity, never class" — for a prime factor ℓ of p + 4d the ONLY link of its class mod 4d to any Frobenius
data of p is χ_{−4d}(ℓ) = (ℓ/p) (Prop 5.1); any governing-field / residue-symbol / Rédei datum of p sees [N] mod t only through
F = Ω ∩ ℚ(ζ_t) ⊂ Ω^{ab}, which is multiquadratic (+ℚ(ζ_n)) for all standard data (Thm 2.1); even perfect knowledge of the
ideal classes of all factors in Cl(ℚ(√−tp)) yields only the χ-shadow (Cor 5.3). The single abelian higher datum is
−4b⁴ = ((1+i)b)⁴ — exactly the Sophie-Germain identity of the thin families (J)74/(J)80.

## Results
* Thm 2.1 + Table 2.2 (PROVED): the class of N mod t on every line (p + 4d, cp + 1, Type II/I e-slices) is congruence data, so
  the "forced quotient" of the total product is G itself; from total data E is forced iff [N] = −1, never on the b = 1 line.
  Residue-symbol data see G/G² (table column "quad", d ≤ 30).
* Lemma 3.1 / Prop 3.2 (PROVED): strongest forced-factor lemma = product formula + realisability; exact forced criterion
  −1 ∈ Σ(s) ∪ Σ(s)·[L]. §3.3: forced small factors chosen via d = ET Type II classes d | (w+1)/4, p ≡ −4d (mod w).
* Thm 3.4 (PROVED, unconditional, explicit class): every forced rule with bounded levels/small primes, on all four lines,
  fails at every prime p ≡ 1 (mod M) — N becomes the integer of "p = 1". (Specialises LONGSHOT_PIGEONHOLE Thm 2.2 /
  POINTWISE_SIZE Thm C with an elementary proof.)
* Lemma 4.1 / Prop 4.2 (PROVED): target-Davenport constant η(G) ≥ (q − 3)/2 at t = 4q; forced supply ≤ 1 escaping large factor
  per subgroup per integer; no pooling (privacy Lemma 2.3 SS8). Zero-sum works only at exponent-2 levels t | 24.
* Prop 5.1, Thm 5.2 (PROVED): individual reciprocity link; no class is forbidden for a single large factor in any Chebotarev
  class of p. Cor 5.3 (PROVED from Prop 10.3/Rem 10.4, odd part of t).
* Thm 6.1 (CONDITIONAL on HC = Dickson + one Chebotarev condition): for every finite Galois Ω and class C compatible with
  p ≡ 1 (M), infinitely many p ∈ C have no certificate at levels ≤ D on any of the four lines (extends B1_LINE Thm 4.2).
* §7 EVIDENCE (p ≤ 10⁶, levels ≤ 200, every actual certificate verified as an ES solution; forced ⟹ actual asserted):
  actual fails at 193, 2521, 66529, 252001(>200); generated-subgroup relaxation never fails; forced F₁₀ / F₃₀ fail at 734 / 43
  primes (Haar limits 1.8 % / 0.22 %); exponent-2 shadow X2 fails at 73 primes (2521 among them). All tiers fail at all 499 odd
  squares — Gen factor by factor because every ℓ | m² + 4d has χ_{−4d}(ℓ) = 1.
* §8 construction log C1–C7 with the hypothesis each attempt hit.

## Labels / scope caveats for the reviewer
* Thm 2.1(c)(iv) (Smith governing fields) is stated conditionally on Ω^{ab} being multiquadratic; I did not verify this for
  every governing-field construction in the literature (memory only, no PDFs consulted). Cor 5.3 covers the class-group side
  independently.
* HC is a non-standard but natural hypothesis (Dickson with a Chebotarev constraint on one form); flagged CONDITIONAL.
* Thm 3.4's modulus condition q^{e_q} > 16D(D+1) was chosen generously; please check the c-line 2-part handling.

## Sparks (not pursued)
1. Mod-p formulation (Direction 4: xy ≡ 1 (mod 4p), height-dependent target): there the modulus is p, where higher
   reciprocity DOES act on individual factors ((ℓ/π)_n); check whether the height-dependent target can be expressed through
   power classes mod π — the only place in the map where §5's negative does not apply verbatim.
2. X2 shadow: failures are primes imitating squares for finitely many binary-form tests (p + 4 primitive sum of two squares,
   p + 8 = x² + 2y², …). A half-dimensional (Iwaniec) sieve should give X2 for all but ≪ x/(log x)^{1+κ} primes; is the union
   X2 ∪ (★) ∪ b = 1 ever failing beyond the known list?
3. Exact values of the target constant η(G) for |G| ≤ 64 and a literature check (weighted Davenport / EGZ with a prescribed
   non-zero target).
4. Sophie-Germain levels d = b²: (p/ℓ)_4 = (b/ℓ) for ℓ ≡ 1 (4), ℓ | p + 4b²; does Burde's rational quartic reciprocity give a
   p-side constraint usable at these levels?
