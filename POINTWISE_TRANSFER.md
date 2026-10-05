# POINTWISE_TRANSFER — Haar avoidance ⇒ prime avoidance (task O42)

Branch `side-agent/avoid-transfer`. Status labels as in DISCOVERIES.md.
Source of all machinery: `paper/es-subexp-note.tex` (cited below as [SN],
with its lemma names), i.e. POINTWISE_OMEGA8 §§1–5 + POINTWISE_OMEGA9 §§1–3.
This file *abstracts* that machinery; nothing here is about 4/n until §5.

Cited inputs (same as [SN]): Gallagher's theorem in the form [MV3, Thm 28.19]
with Landau–Page (= [SN] Thms `thm:G`, `thm:xz`), Håstad's switching lemma
([SN] `thm:hastad`). "Proved modulo G+H" means: proved here assuming these.

## 0. Setting

* `Q ≥ 1` a modulus, `a` a unit mod `Q` (the *target class*).
* `𝒫` a finite set of *free* primes, `ℓ ∤ Q`, `N = |𝒫| ≥ 1`. For `ℓ ∈ 𝒫` an
  exponent `e_ℓ ≥ 1`; `T ≥ 2` with `ℓ^{e_ℓ} ≤ T` for all `ℓ ∈ 𝒫`.
* Coordinates `X_ℓ(n) = n mod ℓ^{e_ℓ}`, valued in `G_ℓ = (ℤ/ℓ^{e_ℓ})^×` for
  `n` coprime to `ℓ`. **Haar measure** `ℙ`: the `X_ℓ` independent uniform on
  `G_ℓ` (= the uniform measure on units mod `∏ ℓ^{e_ℓ}`).
* A *congruence event* `E` is a nonempty set `supp E ⊆ 𝒫` with `|supp E| ≤ k`
  together with an **arbitrary** subset of `∏_{ℓ∈supp E} G_ℓ`; equivalently a
  set of unit classes modulo `d_E = ∏_{ℓ∈supp E} ℓ^{e_ℓ}`. An integer `n`
  coprime to `d_E` *lies in* `E` if `(X_ℓ(n))_{ℓ∈supp E} ∈ E`.
  Typical case: `E = {n ≡ b (mod d)}` with `d | ∏ℓ^{e_ℓ}`, `gcd(b,d)=1`,
  `supp E` = primes of `d`, `ℙ(E) = 1/φ(d)`.
* Family `E_1,…,E_m` (`m ≥ 1`), `S = Σ_i ℙ(E_i)`,
  `w_ℓ = Σ_{i: ℓ∈supp E_i} ℙ(E_i)`, `F = 1[no E_i occurs]`, `δ = 𝔼F`.
  `i ∼ j` iff `supp E_i ∩ supp E_j ≠ ∅`.
* (LLL) weights `x_i ∈ [0,1)` with `ℙ(E_i) ≤ x_i ∏_{j∼i, j≠i}(1−x_j)`;
  `δ_L := ∏_i (1−x_i)` (so `δ ≥ δ_L` by the local lemma).
* (Tw) *twist hypothesis*: for every real primitive character `ψ` whose
  conductor `f > 1` divides `∏_{ℓ∈𝒫} ℓ^{e_ℓ}`, `|𝔼[Fψ]| ≤ δ/5`.
  (Here `ψ(n)` is a function of the coordinates `X_ℓ`, `ℓ | f`.)

Parameters:
```
b   = ⌈log₂(4NT)⌉
k₀  = ⌈log₂(400·m²·(S+1)/δ_L)⌉
t   = 10·k·b·k₀
```

## 1. Statements

**Theorem 1.1 (abstract transfer; proved modulo G+H).** In the Setting, with
(LLL) and (Tw), there is a prime `p` with `p ≡ a (mod Q)`, `p > T`, `p` lies
in no `E_i`, and
```
log p ≤ C₇ · ( log Q + 2(3k+2t)·log T + 1 ),
```
`C₇` absolute and effective (given effective constants in G and H).

*No* hypothesis bounds the number of residue classes inside an event, the
number `m` beyond `log m`, or the size of `∏ℓ^{e_ℓ}`; no single-value,
codegree, or Siegel-zero hypothesis is needed. Coprimality: events are sets of
*unit* classes; a non-unit class `n ≡ b (d)`, `g = gcd(b,d) > 1`, contains no
prime `> T ≥ g` and may simply be deleted. Moduli must be supported on free
primes (prime-power parts dividing `Q` must first be decided by the target
class — the "survival" reduction of [SN] §2).

**Lemma 1.2 (sufficient condition for (Tw); proved).** Put
`η_ℓ = Σ_{i: ℓ∈supp E_i} ℙ(E_i) ∏_{j∼i}(1−x_j)^{−1}`. If `η_ℓ ≤ 1/6` for all
`ℓ ∈ 𝒫`, then (Tw) holds.

**Corollary 1.3 (local-density form; proved modulo G+H).** Suppose only that
every event lies on `≤ k` free primes and `w_ℓ ≤ 1/(64k)` for all `ℓ ∈ 𝒫`.
Then there is a prime `p ≡ a (Q)`, `p > T`, in no `E_i`, with
```
log p ≤ C₈ · ( log Q + k·log T·log(4NT)·(S + k·log(N+1) + 1) ).
```
In particular with `N ≤ T`: `log p ≪ log Q + k(log T)²(S + k log T)`.

*Benchmark (single class, Linnik).* Without the theorem the only general route
is to pick one surviving class `c mod Q·D₀`, `D₀ = ∏_{ℓ∈𝒫} ℓ^{e_ℓ}`, and apply
Linnik: `log p ≪ log Q + log D₀`, and `log D₀ ≍ Σ_ℓ e_ℓ log ℓ`, typically
`≍ N log T`. Corollary 1.3 replaces `N log T` by a polynomial in the *local*
data `(k, log T, S)` with only `log N` dependence.
