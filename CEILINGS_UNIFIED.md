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

## 2. Witness-modulus tail relative to π(x) (goal (b))

**Theorem 2.1 (PROVED given the note (INTERNALLY PROVED, (B)11) and Page's
theorem in the form of Davenport, *Multiplicative Number Theory*, Ch. 20).**
There are absolute `c, c₁ > 0` such that, uniformly for `x ≥ 3` and
`3 ≤ T ≤ exp(c₁(log x)^{1/4})`,
```
#{p ≤ x prime : W(p) > T} ≪ π(x)·exp(−c(log T)³).
```
This upgrades ledger (A)9 / notes Thm 51.2(2) in two ways: the label (it
was CLAIMED/PROVISIONAL because Thm 34.8 was; the note now proves that input),
and the normalisation (`π(x)` instead of `N`, which matters when
`(log T)³ ≲ log log x`). No `polylog` loss.

*Proof.* Bounded `T` is trivial; let `T ≥ T_0`. Put `X = T^{1/(1+κ)}`,
`t = log X`, so `KX ≤ T`; let `y = Bt³` and `r` the least even integer
`≥ D_B t³`, with `B, D_B` as in note Thm 8.2 (enlarging `D_B` is allowed
there). Put `ν = S_y Q_r(H_X)`. Then `ν ≥ 0` on ℤ (note Lemma 8.1), and for a
prime `p > y` with `W(p) > T` we have `H_X(p) = 0` (an active atom is a
witness of modulus `kℓ ≤ T`, notes (51.2)), so `ν(p) = 1`. Hence
`#{p ≤ x : W(p) > T} ≤ y + Σ_{p≤x} ν(p)`, and `y = Bt³` is negligible.

*Case A: `c_a t³ ≥ 2 log log x`.* Choose `c₁` with `log x ≥ C_0 t⁴`. By note
Thm 8.2, `Σ_{p≤x} ν(p) ≤ Σ_{n≤x} ν(n) ≪ x e^{−c_a t³} ≤ x e^{−c_a t³/2}/log x`.

*Case B: `c_a t³ < 2 log log x`.* Then `t⁴ ≪ (log log x)^{4/3}`, so by the
ledger (note (8.3)) every term modulus `q` and the coefficient sum satisfy
`q, T_abs ≤ e^{C t⁴} ≤ exp(c₂√log x)` for `x ≥ x_0`.
(i) *Prime sum.* Write `ν = Σ_i c_i 1[n ≡ a_i (q_i)]`. Then
`Σ_{p≤x} ν(p) ≤ T_abs√x + (2/log x)Σ_{n≤x} ν(n)Λ(n)` (`ν ≥ 0`, `‖ν‖_∞ ≤ T_abs`),
and `Σ_{n≤x}νΛ = Σ_i c_i ψ(x; q_i, a_i)`. Terms with `(a_i,q_i) > 1` contribute
`≤ T_abs(log x)²`. For `(a,q)=1`, `q ≤ exp(c₂√log x)`, Page's theorem gives
`ψ(x;q,a) = x/φ(q) − 1_{q_1|q} χ_1(a) x^{β_1}/(φ(q)β_1) + O(x e^{−c₃√log x})`,
where `χ_1` (primitive mod `q_1`) is the possible exceptional real character
for this range. Define the unit-Haar functional `E_*f = Σ_{(a_i,q_i)=1} c_i/φ(q_i)`
and `χ̃_1 = χ_1(n mod q_1)` on `Ẑ^×`. Since `∫_{n≡a (q)} χ̃_1 dP_* = χ_1(a)/φ(q)`
if `q_1 | q` and `= 0` otherwise (primitivity: `χ_1` is non-trivial on the kernel of
`(ℤ/q_1)^× → (ℤ/(q,q_1))^×` when `q_1 ∤ q`), the main terms sum to
`x·E_*[ν(1 − εχ̃_1)]`, `ε = x^{β_1−1}/β_1 ∈ [0, 2]` (`β_1 ≥ 1/2`). As `ν ≥ 0`
on every residue class, hence on `Ẑ^×`, this is `≤ 3x E_*ν`. So
```
Σ_{p≤x} ν(p) ≤ (6x/log x)·E_*ν + O(x e^{−c₃√log x /2}).
```
The error is `≪ π(x)e^{−t³}`-negligible since `t³ ≪ log log x`.
(ii) *Unit mean.* On units `S_y = 1`, so `E_*ν = E_* Q_r(H_X)`. Condition on
the unit `c = n mod L_K`; as in Prop 1.1, `H_X = Σ_ℓ I_ℓ` with independent
Bernoulli `I_ℓ` of mean `f_c(ℓ)/(ℓ−1) ≤ 2f_c(ℓ)/ℓ`, so
`E_*((H_X)_m | c) ≤ (2μ_c)^m ≤ (2C_u t³)^m` (note Cor 4.3) and
`P_*(H_X = 0 | c) ≤ e^{−μ_c} ≤ e^{−a t³}` (Prop 1.1). By note Lemma 8.1,
`E_*Q_r(H) ≤ P_*(H=0) + E_*(H)_{r+1}/(r+1)! ≤ e^{−a t³} + (2eC_u t³/(r+1))^{r+1}
≤ 2e^{−a t³}` once `D_B ≥ 2e²C_u` and `D_B ≥ 2a`.
Combining: `Σ_{p≤x}ν(p) ≪ π(x)e^{−a t³}`. In both cases `t ≍ log T`. ∎

*Remark 2.2 (scope).* Case B is exactly the Siegel-model transfer
`(1 − εχ_1)P` that POINTWISE_OMEGA15 Thm 3.1 analyses for minorants: for
*majorants* the exceptional character costs only the factor `1 + ε ≤ 3`,
because a majorant is non-negative. This asymmetry (upper bounds tolerate
Siegel zeros, lower bounds need `E_*[B(1−εχ)] > 0`) is the familiar one.
Theorem 2.1 is the "typical-size" statement on the exceptional side; the
pointwise side asks for the *opposite* inequality (some `p ≤ x` with
`W(p) > T`), whose certificate must be a minorant (§4).
