# AGENT_REPORT_O263 — route (b): class forcing beyond parity (checkpoint 1, R272 repairs applied)

Branch side-agent/class-forcing. Main file CLASS_FORCING.md; memos BRAINSTORM/z33_{forced_quotient_total, kummer_shadow,
forced_factor_criterion, target_davenport, hc_realisation, census_tiers}.md; scripts scripts/z33_{forced_quotient_table,
census, haar_forced}.py; logs logs/z33_*.txt (tiny). **ES is not solved; nothing here advances it.**

SHARP: no breakthrough-grade finding. (R272 repair of the wording.) Cleanest statement (a closing dictionary, not a door):
**reciprocity data of p = congruence data of p plus an independent non-abelian part.** Any Frobenius datum of p in a Galois Ω
sees [N] mod t only through F = Ω ∩ ℚ(ζ_t), a quotient of p mod t (Thm 2.1(b); G/G²-type plus p mod n for residue/Rédei
data; for general governing fields the size of F was NOT determined — the earlier "multiquadratic" claim is withdrawn). For a
prime factor ℓ of p + 4d the only link of its class mod 4d to p is χ_{−4d}(ℓ) = (ℓ/p) (Prop 5.1). The single abelian higher
Kummer datum is −4b⁴ = ((1+i)b)⁴ — the Sophie-Germain identity of the thin families (J)74/(J)80.

## R272 repairs applied (hostile review reviews/class-forcing-review.md)
* D1 FATAL: HC as first stated was inconsistent and Thm 6.1 false (Ω = ℚ(ζ₇), C = {p ≡ −4 (7)}: 7 | p + 4 certifies d = 1).
  Restated HC (local condition on Ω₀ = Ω ∩ ℚ^{ab}) and Thm 6.1 (C|_{Ω₀} = 1, B ≥ conductor primes); proof completed per review.
* D2 MAJOR: multiquadratic-Ω^{ab} claim for governing fields withdrawn; slogan replaced (above).
* D8 MAJOR: Cor 5.3 restated as (i) PROVED class-invariance only mod squares, (ii) Assessment for abstract class data,
  (iii) PROVED: concrete reduced forms determine the divisor (= factorisation, B2); "any line's N" dropped.
* Minors: D3 (proof of 2.1(a), c-line parity), (ii)/(iii) hypotheses, D4 ("contained in"; role of 16D(D+1)), D5 (s defined
  via min(v_q, e_q)), D6 (unproved sentence deleted), D7 (q ≡ 3 (4); z29(b) only for total data; criterion wording;
  η ≥ 1 ⟺ exp > 2 checked to d ≤ 150, general proof Assessment), Prop 5.1(c) hypothesis −4d ∉ ℚ^{×n}, D9 attribution,
  Haar error bars.

## Results
* Thm 2.1 + Table 2.2 (PROVED): the class of N mod t on every line (p + 4d, cp + 1, Type II/I e-slices) is congruence data, so
  the "forced quotient" of the total product is G itself; from total data E is forced iff [N] = −1, never on the b = 1 line.
  Residue-symbol / Rédei data see G/G²-type quotients (table column "quad", d ≤ 30); general Frobenius data a quotient of p mod t.
* Lemma 3.1 / Prop 3.2 (PROVED): strongest forced-factor lemma = product formula + realisability; exact forced criterion
  −1 ∈ Σ(s) ∪ Σ(s)·[L]. §3.3: forced small factors chosen via d = ET Type II classes d | (w+1)/4, p ≡ −4d (mod w).
* Thm 3.4 (PROVED, unconditional, explicit class): every forced rule with bounded levels/small primes, on all four lines,
  fails at every prime p ≡ 1 (mod M) — N becomes the integer of "p = 1". (R272: the classical p ≡ 1 (M) obstruction,
  JOINT_BUDGET Prop 4.3 / B1_LINE §4, in forced-factor language; low novelty.)
* Lemma 4.1 / Prop 4.2 (PROVED): target-Davenport constant η(G) ≥ (q − 3)/2 at t = 4q; forced supply ≤ 1 escaping large factor
  per subgroup per integer; no pooling (privacy Lemma 2.3 SS8). Zero-sum works only at exponent-2 levels t | 24.
* Prop 5.1, Thm 5.2 (PROVED): individual reciprocity link; no class is forbidden for a single large factor in any Chebotarev
  class of p. Cor 5.3 restated per R272 D8 ((i), (iii) PROVED; (ii) Assessment).
* Thm 6.1 (CONDITIONAL on the corrected HC; first version FALSE, R272 D1): for every finite Galois Ω and class C with
  C|_{Ω₀} = 1 (Ω₀ = Ω ∩ ℚ^{ab}), infinitely many p ∈ C, p ≡ 1 (M), have no certificate at levels ≤ D on any of the four lines
  (extends B1_LINE Thm 4.2). The abelian part of Frobenius data is B1 and can cover whole classes.
* §7 EVIDENCE (p ≤ 10⁶, levels ≤ 200, every actual certificate verified as an ES solution; forced ⟹ actual asserted):
  actual fails at 193, 2521, 66529, 252001(>200); generated-subgroup relaxation never fails; forced F₁₀ / F₃₀ fail at 734 / 43
  primes (Haar limits 1.8 % / 0.22 %); exponent-2 shadow X2 fails at 73 primes (2521 among them). All tiers fail at all 499 odd
  squares — Gen factor by factor because every ℓ | m² + 4d has χ_{−4d}(ℓ) = 1.
* §8 construction log C1–C7 with the hypothesis each attempt hit.

## Labels / scope caveats for the reviewer
* Thm 2.1(c)(iv): multiquadratic claim withdrawn (R272 D2); the abelian parts of Smith / Koymans–Pagano fields are unchecked.
* HC (corrected) is the Bateman–Horn–Chebotarev heuristic with the local condition on Ω₀; flagged CONDITIONAL.
* Thm 3.4: c-line 2-part confirmed harmless by R272; q^{e_q} > 4D + 1 suffices there, 16D(D+1) is for Thm 6.1.

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
