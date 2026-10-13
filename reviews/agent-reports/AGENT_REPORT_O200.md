# AGENT_REPORT_O200 — exponent cap between ES^{(y)} and ES (spark relay U)

Branch side-agent/exponent-cap (merged side-agent/frobenius-firing first, as briefed). Main file EXPONENT_CAP.md;
scripts scripts/xc_{rigidity,leaste,cover}.py; data data/xc/ (≈ 410 KB, gzipped).

SHARP:
1. **Overflow ↔ growing-modulus duality (Prop 1.3, Cor 1.4; PROVED, asserted on 46 084 shots).** In the shot family
   g | n + 4Q², g ≡ 3 (4), with Q₀ = gcd(Q, (g+1)/4), overflow Q₁ = Q/Q₀ (= √den z exactly) and k = (g+1)/(4Q₀):
   **D·g = 4k²n + Q₁²,  D ≡ −Q₁² (mod 4k)**, and conversely every such divisor D gives a shot. ES = slice Q₁ = 1
   ("4k²n+1 has a divisor ≡ −1 mod 4k"), ES^□ = slice k = 1 ("4n + Q₁² has a divisor ≡ 3 mod 4"), T1 = the mod-4
   part. Equivalently **ES^{(y)} is the FIXED_MODULUS_SHOTS certificate cube (c, d, j) with d allowed to be Q₁^{−2}**
   (rad Q₁ | y), i.e. Box(K) inflated to Box(K·Q₁²) at the same modulus.
2. **Archimedean wall (Thm 2.1; PROVED, sharp in the Q₁⁴ term).** g ≤ 2nQ₁²(n + Q₁²). Every bounded cap with fixed S (R200 repair M1) is a finite
   search (like ES, which is Q₁ = 1: g ≤ 2n(n+1)); a sieve producing r → ∞ certifies at best
   e·log rad(Q₁) ≥ ¼ log(r/4n) − O(1). The interpolation ES^{(y,e)} is discontinuous at the sieve end: with S fixed, no sieve can
   push the cap to any bounded e (R200 repair M1: with S growing the wall is no obstruction even at e = 1; only
   covering arguments are excluded, by Prop 3.1).
3. **Dictionary 3.3 (geometry of numbers / characters).** Coverage of (F_r^*)² by the exponent box ⇔ ℓ^∞ covering
   radius of the relation lattice Λ_r; by transference ⇐ "no nontrivial character of (F_r^*)² is sup-angle-close
   to 1 on S". In the ES-relevant regime (S = primes dividing (r+1)/4, e = polylog) this is a small-prime
   discrete-log non-concentration problem on primes of total size ≤ r — beyond known pointwise GRH inputs (Assessment; R200 repair m6).

Results (labels):
* Prop 1.2 (PROVED): ES^{(y,e)} shot condition ⇔ g ≡ −1 (mod 4·Q^{(e)}), Q^{(e)} = ∏ ℓ^{max(1, v_ℓ(Q) − e)}.
* Prop 3.1 (PROVED): |exponent box at r| ≤ τ((r+1)/4)(e+2)^{ω((r+1)/4)}; the brief's KEY OBSERVATION (large κ via
  r ≡ −1 mod s^K) only buys a divisor-function factor; coverage needs e ≥ (log r)^{1−o(1)} (or r^{1/k}/2 for k fixed
  primes). (a)+(b) of the brief are incompatible at e = 0 for covering arguments (R200 repair m5) by the divisor bound, independent of level of distribution.
* Thm 3.2 (PROVED relative to the FROBENIUS_FIRING Thm 4.2 / UNIT_ORBIT Lemma 2.2 sieve; ineffective): ES^{(y)} with
  exponent cap y^δ for every δ > 0 (Minkowski II on Λ_r + Lemma-2.3 count of short relations). Modest upgrade from
  cap ≍ r; optimal up to 2/(k+1) vs 1/k for fixed S.
* Prop 4.1 (PROVED relative to Coppersmith–Howgrave-Graham–Nagaraj / Lenstra; citation not re-checked): per shot,
  overflow below N^{1/4} ⇒ O(1) certificates (B3's bounded-multiplicity regime).
* EVIDENCE (§5.1): S = {3}, all 78 496 primes 5 ≤ p < 10⁶ solved with j ≤ 24; least overflow 0 for 73 910, ≤ 4 for
  98.9 % (exact for ≤ 4 by the rigidity completeness bound), max 19 (p = 598 537); geometric tail ratio ≈ 0.65,
  nearly p-independent; the best solutions use κ = 1 mostly (large K never helps). T1: 332 odd squares, no shot at
  any e (j ≤ 30). (§5.2) k = 2 coverage: L(r)/√r median 0.955, 20/1121 exceptional — matches Prop 3.1/Thm 3.2.

Verdict (Assessment): not an opening for ES. The gap ES^{(y)} → ES is not a continuous exponent interpolation a
sieve can traverse: bounded caps with fixed S are finite searches (archimedean wall; R200 repair M1), sieve-able caps need the box inflated from
r^{o(1)} to r, and the polylog-cap coverage problem is a named open problem beyond known pointwise GRH inputs (R200 repair m6) that would still only give
ES^{(y, polylog)}.

Self-check notes for the reviewer: Thm 2.1's proof splits on kj < 2Q₁² vs ≥ 2Q₁² (uses 4 | j); the Q₁⁴ sharpness
family D = 3, j = 4, k = (Q₁²+3)/4 was checked numerically (g/(nQ₁⁴) → 1/12). Thm 3.2's covering step uses only
Minkowski II for the cube and the parallelepiped representative bound Σλ_i. Transference constant in 3.3(b) cited,
not re-derived.

Sparks (not pursued):
* Diagonal families in the (Q₁, k) duality: both coordinates moving in multiplicative orbits (Q₁ ∈ ⟨S⟩, k ∈ ⟨S′⟩);
  what is the "firing" condition and is there a fixed-modulus sub-orbit beyond k = 1?
* Large sieve over the moduli r for the dual lattices Λ_r^*: could give coverage at e = r^{o(1)} with |S| → ∞
  unconditionally (needs the sieve at modulus M = x^{o(1)}).
* Effective Thm 3.2 / effective ES^{(y)} with den(z) ≤ n^{O(1)} via Linnik/Burgess at scale r ≤ n^A (Thm 4.2 is
  ineffective; ES^□ has an effective version).
* The Lenstra N^{1/4} threshold as a natural "half-way" variant ES^{(y, N^{1/4})}: is it provable, does it keep T1?
