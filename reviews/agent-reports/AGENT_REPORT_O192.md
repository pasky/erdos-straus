# AGENT_REPORT_O192 — spark synthesis II: cross-pollinating (J)13–(J)25 (checkpoint 1)

Branch side-agent/synthesis-two. Main file `SYNTHESIS_SPARKS2.md` (§§0–4). Scripts `scripts/syn2_sqden.py`,
`scripts/syn2_tes_shots.py` (both run in < 2 s). **ES is not solved; no case of ES is claimed.**

## SHARP:
1. **The T1-bearing ES variant becomes elementary once the mute set may grow (§2, Prop 2.2, PROVED from Dirichlet
   only).** ES^□ (third denominator allowed to be an odd square prime to n) holds at every odd non-square n via ONE
   prime r ≡ 3 (mod 4) with (n/r) = −1 and Q < 2r; the T1 (Lemma 2.1) is unchanged. Under GRH S = {primes ≪ log²n}
   suffices. Consequence for steering: all of (J)23's analytic content (BV + linear sieve + Gupta–Murty) is the
   restriction to a FIXED finite S, and "a T1-bearing variant is provable" carries no information about ES. The
   difficulty is never the T1; it is the size of the shot orbit, and for ES that orbit is one point (S = ∅).
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
   places, Artin problem with finitely many, finite search with none.
3. **Ledger fixes (§4):** (J)23 cites "(A)19" for the large-sieve cap; it is (D)19/(D)22, conditional on KARY2 Thm 5.1
   (UNIT_ORBIT_ES repair m8 not propagated). "W" means three different things: the signed slice count W(n) of
   (J)10/(J)14, the sign-free Lorenzini property (W) of (J)15/(J)20, and W(p) of (H)19/(H)22.

## Results (labels)
* §1: twelve cross-combinations X1–X12 (seeds (i)–(vi) plus three new: X7 ℚ(√p) Galois-fixed points with cancelling
  anchors, X8 function-field mute place via Bilharz, X11 the weaker mute normalisation), each with a sketch and a
  B1–B6/T1/F/D2 screen. Dead: X1, X5, X6, X9, X10 (B2/B3, F, genus-only). X4 is answered by O188 Lemma 4.1. X7 and X8
  are unexplored sparks.
* §2 Lemma 2.1, Prop 2.2 (PROVED); the quantitative remark (GRH bound on r(n)) is an Assessment from standard inputs.
* §3 Prop 3.1, Lemma 3.2, Thm 3.3 (PROVED), Cor 3.4 (PROVED rel. Hecke), Thm 3.5 (PROVED rel. Chebotarev for the
  abelian extension L·K(∛n)/K). The value ω² in Cor 3.4 is EVIDENCE (not derived from the supplementary laws).
* Seeds: (i) dead (no map ES^{(S)} → ES beyond Q | (r+1)/4, i.e. O186 Prop 6.1 / FMS Cor 3.2). (ii) answered: yes
  with S ≪ log²p (GRH), and the conversion is still B2. (iii) done (§3). (iv) answered by O188 Lemma 4.1.
  (v) shots are Heegner forms [r, 4Q, ·] of discriminant −4n; ES cube points are forms [h, 4cd, de] with "A ≡ −1 mod B";
  genus-only (dead). (vi) longer words give no ES certificates (length 3 is forced).

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
