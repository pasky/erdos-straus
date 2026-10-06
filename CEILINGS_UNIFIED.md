# One sieve limit behind both ceilings (task O60)

Branch `side-agent/unify-ceilings`. Labels follow the house rules. ES is not
solved here or anywhere. Nothing below improves the exceptional-set exponent
3/4 or the pointwise exponent 1/4.

Notation. `T` = witness-modulus cutoff, `𝓛 = log T`. `W(p)` = least witness
modulus `kℓ` as in notes (51.1)–(51.2). "The note" = `paper/es-threequarter-note.tex`
(INTERNALLY PROVED, (B)11). `t = log X`, `K = ⌊X^κ⌋`, `A_X`, `H_X`, `L_K`,
`f_c(ℓ)`, `μ_c` as in the note §§2–4. `P_*` / `E_*` = Haar measure on units
`Ẑ^×` (for a function of `n mod L`: uniform on `(ℤ/L)^×`).

## 0. Dictionary (Assessment, made precise in §§1–4)

| | exceptional set (note, KARY) | pointwise (OMEGA13/14) |
|---|---|---|
| system | atoms of modulus `kℓ ≤ KX ≤ T` | events of modulus `≤ T` |
| mass / dimension `κ` | `μ_c ≍ t³` (note Cor 4.3) | `≍ 𝓛³/log𝓛` (OMEGA14 §4) |
| certificate | majorant `S_yQ_r(H_X)`, `r ≍ t³` | minorant `B ≤ F` |
| level needed | `log q ≍ r·t ≍ t⁴` (note Thm 8.2) | `log D ≍ κ𝓛 ≍ 𝓛⁴` (OMEGA14 Thm 4.5) |
| level available | `log N` (rounding) | `log x` (transfer to primes ≤ x) |
| result | `t ≍ (log N)^{1/4}`, saving `t³` | `𝓛 ≍ (log x)^{1/4}` |

Both are the single relation `λ ≍ 𝓛·κ(𝓛) = 𝓛⁴` between the level `λ` (log of
the largest CRT modulus) and the size `𝓛` of the moduli that can be fully
exploited. The exceptional exponent is `κ(λ^{1/4}) = λ^{3/4}`, the pointwise
exponent is `λ^{1/4}`; with Haar exponent `a` they are `a/(a+1)` and
`1/(a+1)`, so they sum to 1.

## 1. The note's void is a Haar bound: `log(1/δ*(T)) ≫ 𝓛³` without log loss

**Proposition 1.1 (PROVED given the note's Cor 4.3 = notes Thm 34.8/76.2,
INTERNALLY PROVED).** There are `c, T_0 > 0` such that for `T ≥ T_0`,
with `X = T^{1/(1+κ)}`:
```
P_*(H_X(n) = 0) ≤ exp(−a_h' t³),   and   δ*(T) ≤ 8·exp(−c𝓛³),
```
where `δ*(T)` is the POINTWISE_HAAR avoider density (Haar on `Ẑ^×`, normalised
on `n ≡ 1 (24)`). Hence `log(1/δ*(T)) ≫ 𝓛³`, removing the `1/log𝓛` loss of
POINTWISE_HAAR Thm 2.1; with OMEGA13 Thm 3.4,
`𝓛³ ≪ log(1/δ*(T)) ≪ 𝓛³(log𝓛)^5`.

*Proof.* Condition on `c = n mod L_K`. Under `P_*`, `c` is a unit mod `L_K`,
and the coordinates `n mod ℓ` for the primes `ℓ ∈ (X^{1/2}, X]` (all `> K`, so
coprime to `L_K`) are independent of `c` and of each other, each uniform on
`(ℤ/ℓ)^×` (CRT on unit groups). By note Lemma 2.2, at fixed `ℓ` the active
atoms have pairwise distinct projections mod `ℓ`, and these are units
(atom residue `−uv^{-1}`, `ℓ ∤ uv` as `uv < ℓ`). So
```
P_*(H_X = 0 | c) = ∏_ℓ (1 − f_c(ℓ)/(ℓ−1)) ≤ ∏_ℓ (1 − f_c(ℓ)/ℓ) ≤ e^{−μ_c}.
```
For reduced `c`, note Cor 4.3 gives `μ_c ≥ a_h t² h(K(K)) ≥ a_h a_0 κ t³/2`
(note Lemma 3.2). Averaging over `c` gives the first bound. Conditioning on
`n ≡ 1 (24)` only restricts `c mod 3` (`3 | L_K` since `9 ∈ K(K)`) and the
independent coordinate `n mod 8`; the fibre bound holds for every unit `c`,
so it holds after conditioning. Every atom is a witness class of modulus
`kℓ ≤ KX = T` (note Lemma 2.1 with `w = (kℓ+1)/(4uv)`; equivalently a class of
`ℛ(kℓ)`, (B)1), so `{no event of modulus ≤ T} ⊆ {H_X = 0}`. Finally `t ≍ 𝓛`.
(The factor 8 is not needed but harmless.) ∎

*Remark 1.2 (Assessment).* POINTWISE_HAAR proved `≫ 𝓛³/log𝓛` by a Janson
inequality over squarefree `𝓛⁵`-rough moduli. The note's family is simpler
for this purpose: one large prime per atom plus a revealed small coordinate
`c` makes the events conditionally independent, so the exact product
replaces Janson. The two documents were never cross-referenced. The new
dependency is BV (via the note's supply theorem); POINTWISE_HAAR used only the
fundamental lemma. Both lower bounds remain valid.
