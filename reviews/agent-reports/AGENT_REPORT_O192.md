# AGENT_REPORT_O192 — spark synthesis II: cross-pollinating (J)13–(J)25 (checkpoint 1)

Branch side-agent/synthesis-two. Main file `SYNTHESIS_SPARKS2.md` (§§0–4). Scripts `scripts/syn2_sqden.py`,
`scripts/syn2_tes_shots.py` (both run in < 2 s). **ES is not solved; no case of ES is claimed.**

## SHARP:
1. **The T1-bearing ES variant becomes elementary once the mute set may grow (§2, Prop 2.2, PROVED from Dirichlet
   only).** ES^□ (third denominator allowed to be an odd square prime to n) holds at every odd non-square n via ONE
   prime r ≡ 3 (mod 4) with (n/r) = −1 (for n = p prime, p > 2r: Q < 2r; for composite n only existence); the T1
   (Lemma 2.1) is unchanged. For primes under GRH S = {primes ≪ log²p} suffices (weaker than seed (ii)'s log p; *(R193 repair m2)* S = {primes ≤ log p} with larger Q ∈ ⟨S⟩ is OPEN, not refuted, and r(p) > (log p)/2 holds only on a density-zero set of p). Consequence for steering: all of (J)23's analytic content (BV + linear sieve + Gupta–Murty) is the
   restriction to a FIXED finite S, and "a T1-bearing variant is provable" is by itself weak evidence about ES
   (Assessment). In these mechanisms the T1 step is one character value; my reading is that ES's difficulty is the
   size of the shot orbit (one point for S = ∅), within the orbit family.
   EVIDENCE: all 78 496 primes ≤ 10⁶ solved and checked exactly, max r(p) = 131; odd squares give no shot.
2. **An explicit fixed-modulus Type II shot family for the order-3 TES over ℤ[ω] (§3, Prop 3.1, PROVED):**
   g | n + 18Q³ with g ≡ 10 + ω (mod 18) gives x = (ωn + E)/9, y = n(g + ω²)/9, z = nx(g + ω²)/(9Q³); cubes are
   invisible to the 2-primary anchor (Q³ ≡ 1 mod 2). With a cubic mute normalisation (Lemma 3.2, PROVED; it is needed
   only when q ∤ x — the same holds at order 2), **TES^{□₃} holds at every 2-primary non-cube** by one Chebotarev prime
   (Thm 3.5), with T1₃ at cubes (Thm 3.3). By-product: T1₃ *forces* the cubic identity "18 is a non-cube mod every
   prime r ≡ 10 + ω (mod 18)" (Cor 3.4; numerically (18/r)₃ = ω² on all 27 such r with N(r) ≤ 6000). EVIDENCE: all
   1536 2-primary split primes with N ≤ 6000 solved exactly, Type II shape, inv_π = 2 (= TWISTED_T1's census value),
   mute invariants 0 on 2908 places; cubes: 0 class-g₀ divisors in 267 shots. So the "uniform principle" (seed (iii))
   holds at orders 2 and 3: anchor + wild partner + m-th-power mute places ⇒ elementary with infinitely many mute
   places, Artin problem with finitely many; with none, ES is a finite search ((J)25) while TES finiteness is open.
3. **Ledger fixes (§4):** (J)23 cites "(A)19" (nonexistent) for the large-sieve cap; it is (D)19/(D)22/(D)24, conditional on KARY2 Thm 5.1
   (UNIT_ORBIT_ES repair m8 not propagated). "W" means three different things: the signed slice count W(n) of
   (J)10/(J)14, the sign-free Lorenzini property (W) of (J)15/(J)20, and W(p) of (H)19/(H)22.

## Results (labels)
* §1: twelve cross-combinations X1–X12 (seeds (i)–(vi) plus three new: X7 ℚ(√p) Galois-fixed points with cancelling
  anchors, X8 function-field mute place via Bilharz, X11 the weaker mute normalisation), each with a sketch and a
  B1–B6/T1/F/D2 screen. Dead: X1, X5, X6, X9, X10 (B2/B3, F, genus-only). X4 is answered by O188 Lemma 4.1. X7 and X8
  are unexplored sparks.
* §2 Lemma 2.1, Prop 2.2 (PROVED); the quantitative remark (GRH bound on r(n)) is an Assessment from standard inputs.
* §3 Prop 3.1, Lemma 3.2, Thm 3.3 (PROVED), Cor 3.4 (PROVED rel. Hecke), Thm 3.5 (PROVED rel. Chebotarev for the
  abelian extension L·K(∛n)/K). The value ω² in Cor 3.4 is EVIDENCE (not derived from the supplementary laws). *(R193 repair u1: constancy of (18/·)₃ on the class is PROVED — K(∛18) has conductor dividing (18), so K(∛18) ⊂ L.)*
* Seeds: (i) dead (no map ES^{(S)} → ES beyond Q | (r+1)/4, i.e. O186 Prop 6.1 / FMS Cor 3.2). (ii) answered: yes
  with S ≪ log²p (GRH), and the conversion is still B2. (iii) done (§3). (iv) answered by O188 Lemma 4.1.
  (v) shots are Heegner forms [r, 4Q, ·] of discriminant −4n; ES cube points are forms [h, 4cd, de] with "A ≡ −1 mod B";
  genus-only (dead). (vi) not settled: the five SQ₅ slices are length-3 words; other longer-word encodings unchecked.

## Self-review (deep reviewer subagent) and repairs
No FATAL; Prop 3.1, Lemma 3.2, Thm 3.3, Cor 3.4, Thm 3.5 judged SOUND (identities and tame symbols re-derived, scripts
re-run, solutions spot-checked independently). MAJOR, all repaired in place (marked "Self-review repair"):
(1) Prop 2.2's bound Q < 2r is false for composite n (n = 825 needs Q = 17): now only for primes p > 2r(p).
(2) seed (ii) answered only in the weaker GRH form S ≪ log²p. (3) X6 overstated "length 3 is forced for all ES";
now scoped to the five SQ₅ slices and Type II formal words. (4) global readings ("no information", "entire difficulty",
"TES finite search") restored to Assessments / "within the orbit family"; TES finiteness marked OPEN.
Minor: Thm 3.5 proof now uses L(∛18) so that constancy of (18/·)₃ on the class is not needed; (J)23 citation diagnosis
corrected ((A)19 does not exist; cite (D)19, (D)22, (D)24); X11 wording; S ⊆ S_p; box size ≤ τ₃; scope of the cube
control (one associate per split prime); scripts now assert their reported checks.

## Review R193 (reviews/synthesis-sparks2-review.md)
SOUND-AFTER-REPAIRS, minor only (no FATAL, no MAJOR); every claim re-derived, all numerics reproduced with
from-scratch scripts (`scripts/review_syn2_sqden.py`, `scripts/review_syn2_eis.py`, own ℤ[ω] arithmetic). Repairs
applied by R193 in SYNTHESIS_SPARKS2.md, marked "(R193 repair …)": m1 (Q < r(p)), m2 (density-zero, seed (ii) OPEN),
m3 (weak mute normalisation necessary at order 3), m4 (T1₃ at composite cubes), m5 (associate convention in EVIDENCE (4)),
m6 (KARY2 condition belongs to (D)19 only), m7 (W(n) clash inside (J)15), m8 (X3 scoped to shot mechanisms),
u1 (K(∛18) ⊂ L by conductors; constancy of (18/·)₃ PROVED). Ledger note for the maintainer: DISCOVERIES (J)23's
"(D)19/(D)22/(D)24, conditional on KARY2 Thm 5.1" should attach the condition to (D)19 only.

## Caveats for the reviewer
* Prop 2.2 is deliberately easy; its value is the recalibration. Check that UNIT_ORBIT_ES Lemma 1.1 / Cor 1.2 really
  extend to S = all odd primes ∤ n (they are place-by-place).
* Lemma 3.2's case split uses x, y ∈ O (integral); the twisted coefficients ω, ω² enter only through A/B = ωx/y.
* Thm 3.5 uses μ₆ ↪ (O/18)^* and h_K = 1 to turn "generator ≡ g₀ (mod 18)" into a ray class.
* `syn2_tes_shots.py` monkey-patches `tw_eis.factor_int` (sympy) and `tw_eis.split_prime` (via √−3 mod p and a gcd)
  for speed; the original brute-force `split_prime` hangs on large norms.

## Sparks (not pursued)
1. Order-3 analogue of (J)23 Thm 2.4: TES^{(S)} for a FIXED finite S via a Gupta–Murty sieve over ℚ(ω) (shots
   n + 18Q³, condition −n/18 ∈ ⟨S⟩³ mod 𝔯). Would complete the "orders 2 and 3" table at the Artin level.
2. X8: function-field ES_q^{(S)} with ONE mute prime is probably a theorem (Bilharz: Artin over F_q(T) is proved),
   while ES_q has sterile points for large q (O178 Thm 2.5). That would be a clean model separating "one mute place"
   from "no mute place".
3. TES itself (S = ∅): does it have a size bound / finite search like (J)25? TES has no positivity, so possibly not.
   If TES(π) is a finite search, the window failures (N(π) = 103, 151, …) could be *proved* failures: the first
   T1-bearing variant with a non-T1 failure. Worth one agent.
4. X7: over ℚ(√p) the two real anchors cancel; ES(p) = σ-fixed totally positive O_K-solutions. Look for a finite
   σ-stable quotient with odd cardinality (a Galois-parity mechanism). Speculative.
5. Derive (18/r)₃ = ω² on r ≡ 10 + ω (mod 18) from the cubic supplementary laws, and catalogue which (numerator,
   twist, anchor) triples give an order-m shot identity of the Prop 3.1 shape for m = 5, 7 over ℚ(ζ_m).
