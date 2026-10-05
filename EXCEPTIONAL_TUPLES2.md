# EXCEPTIONAL_TUPLES2 — TC_θ above 3/4 (task O24, branch `side-agent/tc-theta`)

Status: **in progress (O24).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file (internal, unrefereed). ES is not solved. No θ > 3/4 is
claimed unconditionally.

Notation: `T1` = `EXCEPTIONAL_TUPLES.md` (Defs §1, Thm 2.1, Cor 2.2–2.3,
Prop 2.4, Prop 4.2). Prime family `𝒫_y`, classes `𝓡(ℓ)`, `p_ℓ = F(ℓ)/ℓ`,
`μ_y = Σ p_ℓ`, hit count `f_y`, order-j sums `S_j(N)`, CRT values
`e_j = e_j(p)`, TC(N; K, y, η) and TC_θ exactly as in T1 §2.

## 0. Plan / working notes

1. **Form grouping.** A hit `n ∈ −4D (mod ℓ)` corresponds to a unique
   triple (r, s, m), `gcd(r,s)=1`, `rsm = A_ℓ`, `D = r²m`, and
   `n ≡ −4D ⟺ ℓ | ns + r`. Hits with the same *form* (r,s) all divide the
   single integer `ns + r ≤ Ns + r`. This is a rigorous size constraint
   that the CRT law ignores (§1).
2. **Truncation deficit.** The CRT mass `e_j` includes tuples with a
   same-form group of product `> Ns + r`; their interval count is exactly 0.
   Compute that mass and compare with the TC precision `η_K` (§2).
3. Consequence for TC_θ (literal) vs a corrected, truncation-aware TC, and
   whether the corrected version still gives Cor 2.3 (§3).
4. Numerics: explain the T1 §5(b) moment deficits (§4).
