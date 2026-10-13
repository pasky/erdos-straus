# bsB_salie_duality — Type II with p as the Kloosterman modulus: half-integral weight, Salié sums (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Integral-weight Kloosterman sums only have Weil's bound (PARITY_FIXED_P: short by p^{1/2}). **Half-integral weight
Kloosterman sums are Salié sums and have an exact closed form** (sum over square roots), which is how Iwaniec/Duke
get pointwise information on half-integral weight coefficients. `bsB_theta_multiplier` shows the ES sign is the
theta multiplier. Type II puts p in the lower-left slot (GI §3, O167 Lemma 10.1). Can the Type II count at p be an
average of half-integral weight Kloosterman sums *with modulus 4p*, then evaluated exactly by Salié?

## Dictionary (PROVED, elementary)
Type II: `ff' − 4c²dp = 1`, f ≡ f' ≡ −1 (mod 4cd) ⟺ γ = [[f, 4c²d],[p, f']] ∈ SL₂(ℤ) ∩ Γ⁰(4). Conjugating by
diag(2, ½) gives γ̃ = [[f, c²d],[4p, f']] ∈ Γ₀(4), with theta multiplier `ε_{f'}⁻¹ (4p/f') = −i·(f'/p)`
(f' ≡ 3 mod 4, p ≡ 1 mod 4). On every certificate (f'/p) = −1 (Bright–Loughran/Yamamoto sign, (I)7), so the
multiplier is the constant +i: ES Type II at p = "there is a γ̃ ∈ Γ₀(4) with c-entry 4p, multiplier i, and the
moving congruence f ≡ f' ≡ −1 (mod 4cd), 4c²d = upper-right entry". Checked: `scripts/bsB_typeII_mult.py 400` —
472 certificates at primes p ≡ 1 (4) < 400, 0 violations.
Salié (classical; see Iwaniec, *Topics in classical automorphic forms*, Ch. 4, or Iwaniec–Kowalski §12.3): for odd prime c,
`Σ_{x mod c} (x/c) e((ax + bx̄)/c) = ε_c √c (b/c) Σ_{y² ≡ ab (c)} e(2y/c)`.

## Construction attempt and where it breaks
1. A Kloosterman sum at modulus 4p arises from summing a Γ_∞-invariant function over the double coset
   Γ_∞ \ {γ̃ : c = 4p} / Γ_∞, i.e. over f' mod 4p with f determined mod 4p. **The certificate conditions are not
   Γ_∞-bi-invariant**: translating γ̃ by [[1, k],[0, 1]] changes f' by 4pk and the upper-right entry by multiples
   of f', so it changes the modulus 4cd of the congruence f' ≡ −1. The moving modulus (B2/H-A) is exactly the
   failure of invariance.
2. Repair attempt (iterate on the hypothesis "Γ_∞-invariance"): expand [f' ≡ −1 (mod q)] in additive characters
   e(h(f'+1)/q) for each q = 4cd separately; the sum over the coset then has frequencies h/q with q | upper-right
   entry, which is not a fixed frequency per double coset: the "Kloosterman sum" has modulus 4p **and** a
   frequency that depends on the representative. Summing out gives back Σ_b Σ_{f | bp+1} (a divisor sum): no
   Salié structure survives.
3. What Salié *would* give if the conditions were invariant: sums of e(2y/p) over roots of y² ≡ ab (mod p), i.e.
   roots of quadratic congruences to the **fixed prime modulus p** (Duke–Friedlander–Iwaniec territory, but with
   fixed modulus and varying ab). Type I needs roots of x² ≡ −d modulo **varying f** (f | p² + 4c²d). So even the
   idealised duality maps Type II at p to a Type-I-like object with the roles of modulus and argument swapped —
   the averaged (B6) direction.

## Barrier screen
B2 (moving modulus = non-invariance, item 1), B6 (item 3), T1 respected (the multiplier is the sign layer).
No step uses anything that distinguishes p from a square beyond the multiplier.

## Literature
Salié, Math. Z. 36 (1932); Iwaniec, *Topics in classical automorphic forms* (AMS GSM 17), Ch. 4; Iwaniec,
"Fourier coefficients of modular forms of half-integral weight", Invent. Math. 87 (1987); Duke, Invent. Math.
92 (1988); Duke–Friedlander–Iwaniec, Ann. Math. 141 (1995); Tóth, "Roots of quadratic congruences", IMRN 2000.

## Assessment
Dictionary PROVED (elementary). The exact Salié evaluation does not apply because the certificate set is not a
union of Γ_∞-double cosets (precise form of B2 for this route). Promise 1/5. A residual question (not pursued):
is there *any* Γ_∞-bi-invariant weight on {γ̃ : c = 4p} whose positivity at p would imply a Type II certificate?
Such a weight is a function of f' mod 4p only, i.e. congruence data at p — B1 (Thm M/C) says no.
