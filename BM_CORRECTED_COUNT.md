# BM_CORRECTED_COUNT — the Brauer–Manin-corrected count for (★) and its remainder (task O268)

Status: O268 working draft. **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z38_*`, memos `BRAINSTORM/z38_*.md`, tiny logs `logs/z38_*`.
Builds on SINGLE_P_COUNT (O260: pair form, genus split R = M_gen + X, Prop 4.1), Bright–Loughran arXiv:1908.02526 (BL),
PARITY_AUDIT Lemma 3.2 (χ-shadow), B1_LINE Lemma 1.2 (pair genus law), CONDITIONAL_ES Props 2.3, 3.1, 7.3.

Notation (SINGLE_P_COUNT §1–2). For odd n ≥ 3, 𝒫(n) = {(u, B) ∈ ℕ² : gcd(u, B) = 1, u + B odd, 4uB − u − B ≤ n},
q = 4uB, a = −(u + B) (a unit mod q), R*(n) = Σ_{𝒫(n)} 1[n ≡ a (mod q)] (= R(n), the (★) count, for n prime).
(★) solutions give 4/n = 1/(uBC) + 1/(nBC) + 1/(nuC), C = (n + u + B)/(4uB).

## 1. The dictionary: BL's quaternion class is ONE quadratic character per pair, χ_{−4uB}

For a pair (u, B) and odd n put C := (n + u + B)/(4uB) ∈ ℚ (no integrality) and
P_{u,B} := (x, y, z) = (uBC, nBC, nuC) ∈ U_n(ℚ), U_n : 4xyz = n(xy + xz + yz) (BL (1.2)); P_{u,B} lies in U_n(ℝ)⁺. BL's
generator α = (−x/z, −y/z) of Br U_n/Br ℚ ≅ ℤ/2 (BL Thm 1.6) evaluates on this point family to the constant-coefficient
algebra α(P_{u,B}) = (−B/n, −B/u) (x/z = B/n, y/z = B/u). Let χ_{−4uB} = (−4uB/·) be the Kronecker character: a real,
odd (χ(−1) = −1), non-trivial character modulo q = 4uB.

**Theorem 1.1 (PROVED).** Let n ≥ 3 be odd and (u, B) ∈ 𝒫(n).
1. (local invariants) inv_∞ α(P_{u,B}) = −1; inv_ℓ α(P_{u,B}) = +1 for every prime ℓ ∤ 2nuB; inv_2 α(P_{u,B}) = +1
   whenever C is 2-integral. If n = p is prime (p ∤ uB automatically), inv_p α(P_{u,B}) = (−uB/p) = χ_{−4uB}(p).
2. (value at the target) χ_{−4uB}(a) = χ_{−4uB}(−(u + B)) = −1.
3. (the BM factor in the character expansion) for gcd(n, q) = 1, the contribution of the pair of characters {1, χ_{−4uB}}
   to the orthogonality expansion 1[n ≡ a (q)] = φ(q)^{−1} Σ_{χ (q)} χ(n)χ̄(a) is
   φ(q)^{−1}(1 − χ_{−4uB}(n)), and for n = p prime this equals φ(q)^{−1}(1 + inv_∞ α(P_{u,B})·inv_p α(P_{u,B})).
   Hence for (★) hits (an integral point; then inv_ℓ = 1 at all ℓ ≠ p, ∞ by BL Lemmas 3.5, 3.8) BL's Thm 1.2
   (∏_{ℓ | n} inv_ℓ = −1) is exactly the statement χ_{−4uB}(p) = χ_{−4uB}(a), i.e. the Brauer character is the
   unique character in the expansion whose value at the target class is forced by the BM obstruction.
4. (T1) If n = m² then χ_{−4uB}(n) = +1 for every pair with gcd(n, q) = 1, so the pair term 1 − χ_{−4uB}(n) vanishes
   identically: the BM factor alone kills every pair at every odd square.

*Proof.* (1) inv_∞: −B/n < 0 and −B/u < 0, so (−B/n, −B/u)_∞ = −1. For ℓ ∤ 2nuB both entries are ℓ-adic units, so
the tame symbol is trivial. At 2, if C is 2-integral then x, y, z ∈ ℤ₂ and P_{u,B} ∈ U_n(ℤ₂), where inv₂ = 1 by BL Lemma
3.8 (n odd). At ℓ = p ∤ uB: −B/u is a p-unit and v_p(−B/p) = −1, so (−B/p, −B/u)_p = ((−B/u)/p) = (−uB/p) (u² is a
square). For odd p, (−4uB/p) = (−uB/p). (Also, p | uB is impossible: 4uB − u − B ≤ p forces u, B < p.)
(2) −4uB = (u − B)² − (u + B)² ≡ (u − B)² (mod u + B) and gcd(u − B, u + B) = gcd(2u, u + B) = 1 (u + B odd, gcd(u,B) = 1),
so for the odd positive integer u + B the Jacobi symbol (−4uB/(u + B)) = +1; χ_{−4uB}(−1) = sign(−4uB) = −1.
(3) χ_{−4uB} is real, so χ̄ = χ, and χ(n)χ(a) = −χ(n) by (2). If n = p is prime then by (1), 1 − χ(p) = 1 + inv_∞·inv_p.
For a hit, P_{u,B} is integral, inv_ℓ = 1 for ℓ ∤ p (BL Lemma 3.5 for ℓ ∤ 2p; Lemma 3.8 at 2), and Hilbert reciprocity
gives inv_p = −inv_∞^{−1}... i.e. inv_p = −1 (BL Thm 1.2), which by (1) reads χ_{−4uB}(p) = −1 = χ_{−4uB}(a).
(4) For gcd(m, 2uB) = 1, (−4uB/m²) = (−4uB/m)² = 1. ∎

(Check: `scripts/z38_bm_dictionary.py 400` — exact rationals and Hilbert symbols at all places for all 9 440 pairs at the 77
primes < 400 and the odd squares < 400: reciprocity, inv_∞ = −1, inv_ℓ = 1 off 2nuB, inv₂ = 1 at the 1 806 2-integral
points, inv_p = χ_{−4uB}(p), (2) and (4), and χ_{−4uB}(p) = −1 at all 372 (★) hits; all pass.)

**What this says about O260's dictionary (goal 1; refutation of the strong form, proof of the corrected form).**
* The O260 guess "genus indicator of Prop 2.2(a) = local BM invariant" is **false as stated**: the genus indicator is the
  conjunction of s(q) = 2^{ω(uB odd)+2} independent quadratic conditions (all real characters mod q), the Brauer class
  contributes exactly one of them, χ_{−4uB}. The other real characters mod q are (d/·) with d | q a divisor depending on the
  factorisation of u and B; as functions of the point they are not restrictions of any element of Br U_n (which is ℤ/2
  mod constants), so they are not Brauer–Manin data (Assessment: they are "genus of the moving modulus" data —
  the Brauer groups of the individual fibres over (u, B), not of the surface).
* The **corrected, exact** dictionary: in the orthogonality expansion of the pair indicator, the principal character gives
  the naive singular series 1/φ(q), and **BL's class is the Kronecker character χ_{−4uB}**, giving the Borovoi–Rudnick-type
  BM density factor 1 + inv_∞ inv_p = 1 − χ_{−4uB}(p). This is the classical BR/CT–Xu shape "density × (1 + Σ_{β ∈ Br/Br₀}
  ∏_v inv_v β)" with Br/Br₀ = ℤ/2, evaluated pair by pair.
* Thm 1.1(3) also makes BL Cor 1.3 on (★), the χ-shadow of PARITY_AUDIT Lemma 3.2 and the pair genus law of B1_LINE
  Lemma 1.2 one statement: "χ_{−4uB}(target) = −1" (an elementary identity, (2)).
