# Shrinking the quarantine modulus: graded (fibre) quarantine (task O44)

Status: IN PROGRESS. Labels as in DISCOVERIES.md.

Notation: `𝓛=log T`; atoms `(M,D)`, `M≤T`, `M≡3 (4)`, `A=A_M=(M+1)/4`,
`D|A²` (O2 §4). ET = Elsholtz–Tao arXiv:1107.1010 (archived,
`sources/elsholtz-tao-1107.1010.pdf`); ET Thm 7.1 is their Erdős-type bound
`Σ_{n≤N}τ(P(n)) ≪_{deg,l,C} N Σ_{m≤N}ρ(m)/m`, ET Cor 7.4 its linear case.

## 0. Where `log Q_Π ≍ 𝓛^7/log𝓛` comes from, and the idea

In O2 Lemma 11.2 / Thm 11.3 (used by O8 Thm 3.4 and O9 Thm 2.2) a
quarantined prime ℓ is fixed to `n≡1 (ℓ^{e_ℓ})` with the *full* exponent
`e_ℓ=max{e: ℓ^e≤T}`, so every quarantined prime costs `e_ℓ log ℓ > 𝓛/2`.
Two costs:

* `Π_0={ℓ≤z}`, `z=𝓛²`: `π(z)𝓛 ≍ 𝓛³/log𝓛` (needed to make the width
  `k=⌊𝓛/log z⌋` small);
* bad primes `|𝓑| ≤ kS*/c_0 = 64k²S* ≪ 𝓛^6/log𝓛` (ET), each `≤𝓛`.

Idea (graded quarantine). Quarantine ℓ only to `n≡1 (ℓ^{e})` with a
*partial* exponent e chosen so that the remaining "fibre coordinate"
`n mod ℓ^{f_ℓ}` inside `1+ℓ^eℤ` carries per-coordinate mass `≤c_0`.
Heuristically the fibre mass at ℓ is `≈ S*/ℓ^{e+1}`, so it suffices to take
`ℓ^{e+1} > Y` with `Y ≍ S*/c_0 ≍ kS*`, and primes `ℓ>Y` need no quarantine
at all. Cost: `log Q ≤ Σ_{ℓ≤Y} log ℓ^{e} ≤ π(Y)log Y ≈ Y ≍ 𝓛^5` (ET).
The width also improves: every coordinate of an event uses a factor
`ℓ^{v}>Y` of M, so width `≤ 𝓛/log Y`, and no separate `Π_0`/z is needed.

What must be proved:

1. (Survival/uniform mass) O2 Lemma 11.1 covers graded quarantines
   (the proof only uses `m|gcd(M,4D+1)`).
2. (Fibre mass, the main lemma) a uniform bound
   `w_ℓ(Q) ≪ 𝓛^{O(1)}/ℓ^{e+1}` for the mass at the fibre coordinate of ℓ
   (ET Thm 7.1 / Cor 7.4 in progressions mod `ℓ^e`).
3. (Interfaces) the Haar local lemma (O2 Thm 11.3), O8 Thm 3.4's system,
   and O9 Thm 1.1's character expansion accept fibre coordinates.
