# AGENT_REPORT_O186 — spark relay L: infinite unit orbits as infinitely many shots

Main file: UNIT_ORBIT_ES.md. Scripts: scripts/uo_mute.py, uo_mute_t1.py, uo_zint.py, uo_phi_all.py. Memos:
BRAINSTORM/bsL_finite_mute.md, bsL_sieve_saturation.md. Literature: sources/uo/LITERATURE.md (+ PDFs; research subagent).
A self-review (deep reviewer subagent) found no error in the core proofs. It did find overclaims; I repaired them all
(Prop 3.2 scope, §4 scope, Thm 6.2 ES equality and convergence, dropped the needless hypothesis 3 ∈ S, (n/5) = 0 case).
ES is NOT solved, nor any infinite case of ES itself.

## SHARP:
1. **A T1-bearing ℤ-variant of ES that is PROVABLY solvable at every prime, unconditionally (Thm 2.4).**
   * The variant is ES^{(S)}: 4/n = 1/x + 1/y + Q²/Z with x, y, Z ∈ ℤ_{>0}, Q ∈ ⟨S⟩ and gcd(Z, Q) = 1. It contains ES.
   * **Mute primes.** The finite primes q ∈ S are "muted" by a parity normalisation: q may appear in only one
     denominator, and only to an even power. Lemma 1.1 shows inv_q = 0. Hence the T1 holds (Cor 1.2): at squares there
     are no Type I/II solutions.
   * **Shots.** The shots are n + 4Q², Q ∈ ⟨S⟩. They are infinitely many and all have the FIXED modulus 4: a shot
     succeeds iff n + 4Q² has a prime factor ≡ 3 (mod 4). B2 is violated.
   * **Main result.** For |S| ≥ 4, every non-square n coprime to 2S has a successful shot, and no square does. The
     theorem is exact-T1. The proof is a Gupta–Murty sieve (Bombieri–Vinogradov + linear sieve + a collision count)
     and uses no GRH. The T1-sensitive step is the congruence (n/r) = −1.
   * **Evidence (S = {3,5,7,11}).** All 78 493 primes below 10⁶ outside S and all 62 224 odd non-squares below
     3·10⁵ are solved, with every solution verified exactly. A box search finds only "other" shapes at 13², 17², 19².
   * **Control.** Dropping the parity normalisation gives Type I/II solutions at squares, with inv_q = ½.
2. **Dictionary (Prop 6.1, PROVED).** Within the orbit family, a shot solution is an ES solution iff g ≡ −1 (mod 4Q).
   So along the orbit, B2's growing modulus is exactly what separates ES from the provable ES^{(S)}. Along an S-orbit
   the expected number of successful ES shots converges (Assessment): ES gets only a finite lottery there.
3. **The real mute place is worse than a finite one (Prop 4.1, PROVED; sieve consequence = Assessment).**
   * In every number-field sign-pattern variant (V_φ; ES over r₁ = 1 fields; totally positive ES over odd-degree
     Galois fields), a shot forces the quadratic Kummer conditions (u/𝔮) = (−1)^{#{v ∈ P : σ_v u < 0}} for all
     u ∈ U_𝔪. These are not conditions on N𝔮.
   * With the Murty–Petersen levels, the Gupta–Murty closing condition 2η < r + 1 then never holds. This is a failure
     of the method, not an impossibility theorem.
   * Responsible hypothesis: a real mute place forces the orbit to be a non-square coset ηU².
4. **V_φ itself (Thm 5.1, PROVED unconditionally).** The number of odd n ≤ X with no successful shot is ≪ X^{3/4} log² X.
   * This is a power saving. For ES, CRT large sieves are capped at a (log N)^{3/4} saving (DISCOVERIES (A)19).
   * The orbit forbids ≥ ℓ^{1/2−o(1)} residue classes per prime. With ≍ ℓ classes, the large-sieve barrier is X^{1/2},
     which is exactly the size of the T1 set {m², 5m²}: the squares saturate the large sieve.
   * Under GRH, the failure set is exactly the T1 set (Thm 5.2). EVIDENCE: for all odd n < 10⁴ the failure set equals
     T (71 = 71).

## Other results
* Prop 3.1: n ≡ 3 (mod 4) is free in every unit-orbit variant.
* Prop 3.2 (PROVED identity): for n ≡ 1 (mod 8), the total Jacobi symbol of a shot is +1, the same as at m².
* Thm 6.2 lists the three ways to get an infinite orbit over ℚ:
  * ℤ: one shot.
  * ℤ[1/S] without normalisation: the T1 dies. Explicit example: 4/9 = 1/449 + 1/18 + 3125/8082.
  * ℤ[1/S] with the parity normalisation: everything works.

## Labels
* PROVED: Lemma 1.1, Cor 1.2, Prop 2.1, Lemma 2.3, Prop 3.1, Prop 3.2 (the identity), Prop 4.1, Prop 6.1.
* PROVED relative to standard sieve theorems (BV, Rosser–Iwaniec linear sieve; Gupta–Murty style, written out in
  sketch): Lemma 2.2 and Thm 2.4. Thm 5.1 is relative to Montgomery's large sieve and Chebotarev.
* CONDITIONAL (GRH, Lenstra): Thm 5.2.
* Assessment: 4.2 and the Galois paragraph (method-specific), Remark (4) after Thm 2.4, the lottery comment in Thm 6.2.
* For the reviewer: check that Lemma 2.2's sieve is correctly stated (fixed modulus M, sifting by ℓ ∤ M, level x^{1/2}).

## Not done
* Goal (4): the quick TES test over ℚ(ζ₉) and ℚ(ω, √2).
* |S| = 3 via Heath-Brown: plausible, not checked.

## Sparks
* An order-3 analogue: TES over ℤ[ω][1/S] with cube-power denominators at mute primes. This could give an
  unconditional order-3 T1 variant.
* Classify the normalisations at a finite prime that pin inv_q = 0 for non-integral points (anchor calculus,
  TWISTED_T1 §2, extended to non-integral points). Is there one compatible with z ∈ ℤ that still yields infinitely many
  fixed-modulus shots? Prop 6.1 says not along {Q²}.
* Inverse large sieve (Green–Harper, Helfgott–Venkatesh, Walsh) as an "exact-T1" principle for orbit failure sets
  (bsL_sieve_saturation).
* Is there any ES-native family that forbids a power-of-ℓ number of classes per prime? That is the quantitative
  signature of infinitely many fixed-modulus shots.
* Effective version of Thm 2.4: an explicit bound on the smallest Q. Empirically Q ≤ 99 for n < 3·10⁵ with
  S = {3,5,7,11}.
