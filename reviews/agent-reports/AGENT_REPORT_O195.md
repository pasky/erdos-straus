# AGENT_REPORT O195 — spark relay P: function-field mute place (FF_MUTE.md)

Branch side-agent/ff-mute (merged side-agent/synthesis-two first, as instructed). Main file FF_MUTE.md; scripts
scripts/fm_*.py; outputs data/fm/*.txt (tiny).

## SHARP:
1. **Thm 3.5 (PROVED, unconditional, effective): over F_q[T], ONE mute prime s ∤ A suffices — ES_q^{(s)}(A, P) holds
   for every monic irreducible P ∤ sA, every q (incl. char 2, 3 and q = 3^r, r ≥ 27 where ES_q(T^k) has no finite
   linear covering).** Proof = Bilharz specialised to a fixed prime degree d of the modulus: Dirichlet characters mod
   A·P·s (the small Kummer primes ℓ | q−1 become characters mod s by power reciprocity; the square condition becomes
   (f/P) = sign) + Weil's character-sum bound for ℓ | q^d−1, ℓ ∤ q−1, which for prime d are ≡ 1 (mod 2d), so their
   total weight is O(log d/d). Certificate modulus degree ≤ 4 log_q n + C(q, A, deg s) (Bertrand; (2+o(1)) log_q n by PNT — R195 M1). Contrast ℤ: |S| ≥ 4 and
   Gupta–Murty, ineffective ((J)23).
2. **Thm 4.2 (PROVED): exact-T1 dichotomy, decided by the anchor character ε = χ(−1).** For f ≡ −1 (mod A):
   (−A/f) = ε^{d(1+k)+k} (FF form of "(−1/r) = −1 for r ≡ 3 mod 4"). Hence for q ≡ 3 (mod 4), k odd: the mute shot
   mechanism solves P iff P is not a square (squares fail for every s, every S); k even: squares only via even-degree
   moduli (not proved that squares ARE solved by even-degree ones); q ≡ 1 (mod 4): no T1 at all. For k odd the
   mechanism T1 exists iff the ∞-anchor is alive.
3. **Correction of the X8 framing (Prop 5.4, PROVED + Assessment).** The mute mechanism admits no finite covering by
   its shot families (prime or composite moduli; profinite sterile points exist) — yet it is a theorem at every
   admissible irreducible P. So "sterile points vs none" is not the
   separation. The precise separation: mute firing at a modulus f is a Frobenius condition whose P-dependence is the
   global character (f/P) (reciprocity), so RH forces firing at every global P; ES_q firing is the box
   −A·{a²d : ad | (f+1)/A} — a q^{−d+o(d)} fraction depending on the factorisation of f + 1 (Prop 5.2), for which no
   Frobenius description is known (not proved impossible). **The mute place replaces "divisors of f + 1" by "a finitely generated group reduced mod f"
   (Kummer theory) — that is the missing ingredient, and Cor 2.2 (f ≡ −1 mod A·Q for ES-integrality) is exactly B2.**
   Moral: a global (reciprocity) argument can prove a statement that admits no finite covering by its own shot
   families; finite-covering/compactness obstructions do not rule out such proofs.

## Results (labels)
* Prop 2.1 / Cor 2.2 (PROVED): FF mute shot identity; ES_q-integral iff f ≡ −1 (mod AQ) (FF UNIT_ORBIT Prop 6.1).
* Lemmas 3.1–3.4, Thm 3.5 (PROVED; inputs: Weil via Rosen Prop 4.3, Lidl–Niederreiter Thm 5.41, power reciprocity
  Rosen Thm 3.3 — theorem numbers from memory, not rechecked against the books).
* Thm 4.2 (PROVED), Props 5.1–5.4 (PROVED; 5.3(b) Assessment).
* EVIDENCE (§6): every irreducible P solved and exactly verified in 10 (q, A, s) ranges (q = 2, 3, 5, 7, 11; up to
  23 630 P per run), including every known ES_q failure; Lemma 3.2 sign formulas 0 mismatches; G(d) ≈ δq^d/d;
  Thm 4.2 confirmed on all monic P (squares 0/17, 0/41 for q ≡ 3 mod 4, k odd; all for q ≡ 1 mod 4); least shot
  height (all divisor moduli, by sympy factorisation — independent of the orbit search) small, max j ≤ 15, no growth
  trend in range.
* Not checked independently by a second code for the T1 runs (fm_t1 shares fm_poly with fm_mute; fm_minq uses sympy).

## Not done / honest gaps
* No claim about ES_q itself at actual P; Thm 2.5 is about profinite points.
* Whether the full variant ES_q^{(s)} (all its linear families, not just shots) has a finite covering: open.
* BL-invariant computation of mute solutions at squares (the variant's own T1, beyond the mechanism): not done; for
  q ≡ 3 (4) the FUNCTIONFIELD_ES §4 sign does not exclude even-degree Type II data at squares, but whether the full
  variant has an existence-T1 is OPEN (not inferred).
* The explicit lower bound in Thm 3.5 is positive only for d ≥ 17 (q = 3, A = T); small d covered by computation.

## Sparks (not pursued)
1. ℤ under GRH: ES^{(S)} with |S| = 1 (e.g. S = {3}) should follow from Lenstra's Artin-with-congruences theorem
   (conditions r ≡ 3 mod 4, (n/r) = −1, 3 primitive) — the exact ℤ-shadow of Thm 3.5; |S| = 3 via Heath-Brown.
2. Short mute orbits: ES_q^{(s)} with deg Q ≤ C·n (heights comparable to ES_q). Data: bounded j suffices; the
   Chebotarev proof uses deg Q up to O(q^d + n) = n^{2+o(1)} (RH square-root barrier: modulus degree ≥ 2 log_q n
   forces orbit length ≳ n²).
   Is the short-orbit variant a lottery, or provable by sums over j of "P + As^{2j} has a prime factor ≡ −1 (A)"?
3. Interpolate box ↔ group: find the weakest multiplicative structure 𝒬 (between {divisors of f+1} and ⟨s⟩) for
   which firing is still a Frobenius condition — a precise "how mute must a place be" scale.
4. Profinite sterile set of the mute mechanism {x : −xA non-square mod every prime g ∤ As} vs ES's sterile set S ⊂ Ẑ ((J)27): is
   ES's non-square sterile set (e.g. (J)26 points) of the same "non-global" type, i.e. excluded at global points by a
   hidden character? (Assessment: no character is known — B2 — but this is the right question to ask.)

## Self-review (R195, reviewer subagent; `reviews/synthesis-two-hostile-review.md`)
No fatal defect in Thm 3.5. Repaired in FF_MUTE.md / scripts (marked "R195"): M1 (certificate degree: Bertrand
4 log_q n, not 2 log_q n + O(1); shot height O(q^d + n)), M2 (Prop 5.4 for composite moduli; profinite reading scoped),
M3 (fm_minq now enumerates all divisor moduli; numbers updated), M4 (fm_mute primitivity flag; fm_count char 2),
M7 (no denominator-height bound for ES_q), m1 (n < k runs added), m2, m3, m4 (report), m7 (softened).
**Not mine, for the parent:** M5 (STERILE_STEER golden-variant 5m² omission), M6 (DISCOVERIES (J)26 measure limit),
m4 (STATUS.md:19 wording), m5, m6, m8 — they concern files merged from side-agent/synthesis-two and earlier work.
