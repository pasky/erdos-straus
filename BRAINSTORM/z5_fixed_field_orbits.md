# z5_fixed_field_orbits — x-orbits inside one real quadratic field: fixing the field kills the Cohen–Lenstra luck (O229)

**ES is not solved here.**

## Idea
The e = 2 (k = 1) cell is "for some odd x and E | x, E ≡ 3 (4), the principal form f_x = [4n, −x, 1] of discriminant
Δ_x = x² − 16n represents −E" (CAP_TWO §6). Construction: Δ_x = N_{ℚ(√n)}(x + 4√n)... more usefully, the x with
Δ_x = D₀m² for FIXED D₀ form Pell orbits x_k + m_k√D₀ = (x₀ + √D₀)ε^k, so the whole orbit lives in one field
K = ℚ(√D₀), with orders O_{m_k}. In a fixed field, principality in O_m is governed by the ring class group
Cl(O_m) → Cl(O_K) with kernel (O_K/m)^*/((ℤ/m)^*·⟨ε⟩): a fixed, computable object — the hoped-for control.

## Literature
Ring class groups (Cox, *Primes of the form x² + ny²*, §7–9; Neukirch I.12); MARKOFF_ES §6 (CL heuristic across fibres).

## Result (PROVED parts + Assessment)
* (PROVED) β := x₀ + √D₀ (norm 16n) satisfies βε^k ∈ ℤ + m_kO_K, so [β] ∈ ⟨[ε]⟩ in G_{m_k} := (O_K/m_k)^*/(ℤ/m_k)^*
  (gcd(m_k, 16n) = 1). The elements *guaranteed* to lie in O_{m_k} are rational multiples of β^iε^j, of norm
  ±(16n)^i·r²; norm −E with E ≡ 3 (mod 4), gcd(E, n) = 1 is impossible among them (i = 0 gives −E = ±r²).
  So the orbit supplies no free point — the T1 shape (E ≡ 3 mod 4 is not ± a square) reappears.
* (Assessment) For any other α of norm −E, membership αε^j ∈ ℤ + m_kO_K is an event of probability
  ≈ |⟨[ε]⟩|/|G_{m_k}| ≈ ord/m_k, while |G_{m_k}| ≍ m_k grows exponentially in k: along a fixed-field orbit the expected
  number of hit fibres converges. The polynomially large main term of MARKOFF_ES Prop 6.1(a) comes from *varying*
  fields (small class numbers, large regulators); fixing the field trades it for a ring class group of size ≍ m.

## Barrier screen
Violates "family of unrelated fields" (the hoped-for hypothesis), but the price is the conductor; B3 returns
(convergent expected count along the orbit). T1: shown above. B2: E | x_k is still a moving divisor condition.

## Cheap numerics
None run: x_k grows like ε^k with ε ≈ exp(√D₀), so beyond k = 1 the fibres are out of reach of CF scans
(x₁ ≈ 10¹² already gives periods ≈ 10⁶ for D₀ ≈ 10³). Not worth a script.

## Assessment
Negative (Assessment with a PROVED no-free-point lemma). The class-group layer cannot be "controlled" by fixing the
field; the luck lives across fields.
