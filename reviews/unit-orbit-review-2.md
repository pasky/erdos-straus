# Hostile review 2 (R190) of O186 UNIT_ORBIT_ES.md — focus Thm 2.4 and Thm 5.1

Reviewer 2 of 2, independent (did not read reviews/unit-orbit-review.md). Document reviewed: UNIT_ORBIT_ES.md as merged
from side-agent/unit-orbit-es. From-scratch scripts: `scripts/review_uo2_*.py` (none of the author's `uo_*` code reused).

## Summary verdicts

(filled in progressively below)

| Claim | Verdict |
|---|---|
| Prop 2.1 (orbit-shot ⇒ ES^{(S)} solution, Type II shape, parity) | SOUND |
| Lemma 2.2 (linear sieve on (r−1)/2 in a progression) | SOUND (standard) |
| Lemma 2.3 (few r with small ⟨S⟩ mod r) | SOUND (= Gupta–Murty Lemma 2, k generators) |
| **Thm 2.4(a)** (|S| ≥ 4: every non-square n coprime to 2S solvable) | **SOUND** (minor wording/effectivity repairs m1–m3) |
| Lemma 1.1 / Cor 1.2 / **Thm 2.4(b)** (T1 of ES^{(S)}) | SOUND-AFTER-REPAIRS (m4: quantifier in (b)) |
| **Thm 5.1** (V_φ: ≪ X^{3/4} log²X exceptions) | see §3 |

## 1. Thm 2.4(a): what is sifted, and does it close?

**Reading of the sieve (brief item (c)).** The sifted variable is the PRIME r, not the S-units. The proof is exactly
Gupta–Murty with an extra fixed congruence: Lemma 2.2 sifts the shifted primes (r−1)/2, r ≤ x, r ≡ a (mod M),
M = 4·rad(n), by the primes ℓ ∤ M below x^{1/4−ε}. The polylog-many S-units Q ≤ x are never counted; Q is produced
*after* the fact as a discrete logarithm: once Γ_r := ⟨S⟩ mod r has index ≤ 2 in F_r^*, the element −n/4 (a square
mod r) is Q² for some Q ∈ ⟨S⟩ (exponents ≥ 0 since Γ_r is finite). So the "polylog many shots" objection does not
apply; the infinitely many shots are indexed by r, and Q may be astronomically large in terms of r.

**The Chebotarev condition (n/r) = −1 inside the sieve.** It is not a genuine Chebotarev condition: for n ≡ 1 (mod 4),
(n/r) = (r/n) (Jacobi), which depends only on r mod rad(n); the proof bakes it into the class a mod M together with
r ≡ 3 (mod 4) and a ≢ 0, 1 (mod ℓ) for ℓ | n. Then −n/4 is a square mod r because (−1/r) = (n/r) = −1. Lemma 2.2's
hypothesis "a ≢ 1 mod every odd ℓ | M" is what keeps primes ℓ | M from dividing (r−1)/2; it is compatible with the
Jacobi condition because some ℓ₀ ≥ 5 has odd v_{ℓ₀}(n) (re-derived: if only 3 had odd valuation, n = 3^{odd}m² ≡ 3
mod 4) and F_{ℓ₀} ∖ {0,1} contains both a residue and a non-residue for ℓ₀ ≥ 5 (ℓ₀ = 3 has only the non-residue 2,
which is why ℓ₀ ≠ 3 is needed). Re-derived; correct. The n ≡ 3 (mod 4) branch (Q = 1) is correct.

**Arithmetic closing condition (re-derived).** r ≡ 3 (mod 4) ⇒ (r−1)/2 odd, so [F_r^*:Γ_r] ∈ {1,2} or it has an odd
prime factor, which divides (r−1)/2 and hence is ≥ x^{1/4−ε}; then |Γ_r| ≤ x^{3/4+ε}. Lemma 2.3 (re-derived: (B+1)^k
exponent vectors in [0,B]^k collide; r | N_c for one of (2B+1)^k vectors c ≠ 0, ω(N_c) ≪_S B) bounds such r by
≪ x^{(3/4+ε)(1+1/k)}; for k = 4, ε < 1/20 the exponent is < (4/5)(5/4) = 1, so o(x/log²x). Lemma 2.2: linear sieve
(κ = 1, g(ℓ) = 1/(ℓ−1)), level D = x^{1/2}/log^B x by Bombieri–Vinogradov over moduli Md (one class mod Md by CRT
since gcd(d, M) = 1), s = log D/log z → 2/(1−4ε) > 2, f(s) > 0: ≫_{n,ε} x/log²x primes. Index ≤ 2 ⇒ Γ_r ⊇ (F_r^*)² (the
index-2 subgroup is unique), and (Γ_r)² = (F_r^*)² because squaring is a bijection on the odd-order group (F_r^*)².
Everything checks. k = 3 fails here exactly ((3/4)(4/3) = 1), consistent with the |S| ≥ 4 hypothesis.

**n-uniformity.** None is needed: n is fixed, x → ∞, and all constants may depend on n (through M) — the theorem is
"for each n", proved n by n. Correct as stated.

**From-scratch checks.**
* `scripts/review_uo2_brute.py 100000 10000` (S = {3,5,7,11}): all **20 713** non-squares 3 ≤ n < 10⁵ coprime to 2S are
  solved by Prop 2.1 with a prime r ≡ 3 (mod 4), r | n + 4Q²; each solution verified exactly (equation, x, y ∈ ℤ_{>0},
  z > 0, z ∈ ℤ[1/S] with even negative q-valuations, Type II shape at every prime of n); max Q = 81. All 65 squares
  have no hit for Q ≤ 10⁴. With N = 3·10⁵: 62 224 non-squares, max Q = 99, 0 failures, 112 squares no hit — the
  author's EVIDENCE numbers are reproduced exactly.
* `scripts/review_uo2_index.py 10⁶` (the proof's own route, not a search over Q): for n ∈ {13, 17, 29, 37, 41, 53, 221,
  13³, 17·19², 13²·17·29} the class a mod M is built exactly as in the proof; every prime r < 10⁶ of that class with all
  prime factors of (r−1)/2 ≥ 10^{6·0.2} has index [F_r^*:Γ_r] ≤ 2 (no exception in ~2 700 primes), and for each such r
  an explicit Q ∈ ⟨S⟩ with r | n + 4Q² is found. Also #{13 ≤ r < 10⁶ : |Γ_r| ≤ r^{3/4}} = 0.
* Prop 2.1's identity and parity analysis re-derived by hand (x + Q² = e(r+1)/4; v_q(x) = s if s < 2c, else ≥ 2c), and
  the §2 counterexample 4/9 = 1/449 + 1/18 + 3125/8082 (no parity normalisation) is reproduced by the same formulas.

### Defects for Thm 2.4(a)
* **m1 (MINOR, effectivity, Thm 2.4 / Remark (2)).** The lower-bound sieve uses Bombieri–Vinogradov, whose implied
  constant is ineffective (Siegel). The proof therefore gives no computable bound on r or Q in terms of n. Not an
  error, but "unconditionally" should be accompanied by "ineffective (no bound on Q)". *Repair:* add one sentence.
* **m2 (MINOR, Lemma 2.2 statement).** "every prime factor of (r−1)/2 at least x^{1/4−ε}" — for r ≤ x^{1/4−ε} this
  forces (r−1)/2 = 1; harmless, but say "for all r ≤ x counted" to pre-empt the dyadic objection the proof then
  addresses in Thm 2.4 ("No dyadic restriction is needed"). The implied constant depends on M (hence on n) — already
  indicated by ≫_{M,ε}. Fine.
* **m3 (MINOR, Remark (2)).** |S| = 3 indeed looks reachable: Heath-Brown's sieve lemma (≫ x/log²x primes r in a
  progression with (r−1)/2 = P or P₁P₂, P_i > x^{1/4+δ}) gives index ∈ {1, 2} or ≥ x^{1/4+δ}, so |Γ_r| ≤ x^{3/4−δ} and
  Lemma 2.3 with k = 3 gives ≪ x^{1−4δ/3}. Needs the congruence-class version of Heath-Brown's lemma (not checked by
  me either). Keep "not checked", but the stated reason is right.
