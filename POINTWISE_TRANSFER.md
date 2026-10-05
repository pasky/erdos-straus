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

* *Atoms*: the distinct cells `{X_I = σ}` (`I = supp E_i`, `σ ∈ E_i`) occurring
  in the events; `m_a` = their number. Always `m_a ≤ Σ_{j≤k} C(N,j)T^j ≤ 2(NT)^k`.

Parameters:
```
b   = ⌈log₂(4NT)⌉
k₀  = ⌈log₂(400·m_a²·(S+1)/δ_L)⌉        (≤ 2k·log₂(NT) + log₂(1/δ_L) + log₂(S+1) + 12)
t   = 10·k·b·k₀
```

## 1. Statements

**Theorem 1.1 (abstract transfer; proved modulo G+H).** In the Setting, with
(LLL) and (Tw), there is a prime `p` with `p ≡ a (mod Q)`, `p > T`, `p` lies
in no `E_i`, and
```
log p ≤ C₇ · ( log Q + (3k+2t)·log T + 1 ),
```
`C₇` absolute and effective (given effective constants in G and H).

*No* hypothesis bounds the number of residue classes inside an event or the
number of events (only `log m_a ≤ k log(NT)+1` enters), or the size of `∏ℓ^{e_ℓ}`; no single-value,
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
log p ≤ C₈ · ( log Q + k·log T·log(4NT)·(S + k·log(4NT)) ).
```
(Take `x_i = 2ℙ(E_i)`: `log(1/δ_L) ≤ 2.2S`, and Lemma 1.2 applies; see §2.)
In particular with `N ≤ T`: `log p ≪ log Q + k(log T)²(S + k log T)`.

*Benchmark (single class, Linnik).* Without the theorem the only general route
is to pick one surviving class `c mod Q·D₀`, `D₀ = ∏_{ℓ∈𝒫} ℓ^{e_ℓ}`, and apply
Linnik: `log p ≪ log Q + log D₀`, and `log D₀ ≍ Σ_ℓ e_ℓ log ℓ`, typically
`≍ N log T`. Corollary 1.3 replaces `N log T` by a polynomial in the *local*
data `(k, log T, S)` with only `log N` dependence.

## 2. Proofs

**Step 1 (atoms; the role of "single value").** Replace the family by the list
`C_1,…,C_{m_a}` of its distinct atoms, in any order. This does not change `F`
(an integer coprime to the free primes lies in some `E_i` iff it lies in some
atom). The local lemma is used only through `δ ≥ δ_L` and (Tw), which are
properties of `F`; so the LLL weights are attached to the *original* events,
while the sandwich below runs over atoms. Splitting into single values is
needed for exactly one step: [SN] `lem:brw` requires, for `u_j` a function of
the coordinates off `supp C_j`, that conditioning on `C_j` *fixes* those
coordinates (so `F^{(j)}` is defined and `𝔼[A_j e_j²] = ℙ(C_j)𝔼(F^{(j)}−u_j)²`).
Its cost is `log m_a ≤ k log(NT) + 1` in `k₀`.

**Step 2 (sandwich).** With `A_j = 1_{C_j}`, `F_{<j} = ∏_{i<j}(1−A_i)`,
`F^{(j)}` = `F_{<j}` with `X_{supp C_j}` fixed to the values of `C_j`,
`u_j = (F^{(j)})^{≤t}` (Efron–Stein truncation), `v_i = Σ_{j<i} A_j u_j`, put
`B = 1 − Σ_i A_i(1−v_i)²`. By [SN] `lem:brw` (verbatim; it is stated for
arbitrary cells and arbitrary `u_j`): `B ≤ F` pointwise for *every* assignment
of 0/1 values to the `A_i`, hence for every integer `n` (with
`A_i(n) = 1[n ∈ C_i]`), and `𝔼[F−B] ≤ m_a² Σ_j ℙ(C_j)·En(F^{(j)};t)`.

**Step 3 (tail).** `F^{(j)}` is the avoidance indicator of the restrictions of
the atoms `C_i` (`i<j`) compatible with `C_j`, each on `≤ k` coordinates (or
`F^{(j)} ≡ 0`). [SN] `lem:tail` gives `En(F^{(j)};10kbk₀) ≤ 4·2^{−k₀}` once
`2^b ≥ 4NT`. (Remark: the proof there only uses that each event is a Boolean
function of the `≤ kb` bits encoding its `≤ k` coordinates, hence a DNF of
width `≤ kb`; so it holds verbatim for arbitrary events, not only cells.)
Hence, as `Σ_j ℙ(C_j) ≤ S` (atoms of one event are disjoint; dedup only lowers
the sum) and `δ ≥ δ_L`,
`𝔼[F−B] ≤ m_a²·S·4·2^{−k₀} ≤ S δ_L/(100(S+1)) ≤ δ/100`.

**Step 4 (cells, ℓ¹).** [SN] `lem:size`: `B` is a real combination of unit
cells on `≤ 3k+2t` free coordinates, so every modulus `d_i ≤ T^{3k+2t}` and is
supported on `𝒫`. [SN] `lem:l1` with `η = 1/99`: `μ := 𝔼B ≥ 0.99δ > 0` and
`A := 𝔼|B|/μ ≤ 1 + 2/99 < 1.03`.

**Step 5 (twist).** Let `ψ` be real primitive with conductor `f > 1`, `f | d_i`
for some `i`. Then `f | ∏ℓ^{e_ℓ}`, `ψ` is a product of characters `ψ_ℓ` of the
coordinates `X_ℓ`, `ℓ | f`, and as in [SN] `lem:twist`,
`μ_ψ := Σ_{i: f|d_i} c_iψ(b_i)/φ(d_i) = 𝔼[Bψ]`. So
`|μ_ψ| ≤ 𝔼[F−B] + |𝔼[Fψ]| ≤ δ/100 + δ/5 ≤ 0.21δ/0.99·… < μ/4`
(explicitly `0.21δ ≤ 0.2122μ`). (The paper's "`f` odd squarefree" is not
needed: one only uses that `ψ` factors over the coordinates.)

**Step 6 (transfer).** Let `R = max(T, Q, max_i d_i)` and pick a prime
`ℓ' ∈ (R, 2R]`; then `ℓ' ∤ QD` and `ℓ' ∉ 𝒫`. Put `Q' = Qℓ'` and let `a'` be the
class `≡ a (Q)`, `≡ 1 (ℓ')`. Apply [SN] `thm:transfer` with `(Q', a')` in
place of `(Q, 1)` and target `1[n ∈ no E_i]` in place of `1[W(n)>T]`. Its proof
uses about the target only the pointwise inequality `B ≤ target` on
`n ≡ a' (Q')`, `gcd(n,D)=1` (Step 2). The change `1 ↦ a'`: every coefficient
acquires the factor `χ̄_{Q'}(a')` of modulus 1, which is harmless in Case 0 and
in Case B (only `|c(χ)|` is used). In Case A (`χ_D` principal, `χ = χ_1`
induced from a real character mod `Q'`), `c(χ) = χ_1(a')μ/φ(Q')` with
`χ_1(a') = ±1`; for `+1` the proof is verbatim, for `−1` the main terms
combine to `(1 + x^{β_1−1}/β_1)μx/φ(Q') ≥ μx/φ(Q')`, which is better.
Hypotheses: `gcd(d_i,Q') = 1`, `b_i` units (Step 4), twist (Step 5),
`A ≤ 1.03 ≤ Z^{1/4}`. With `Z = Q'·max d_i`,
`log Z ≤ 2log Q + 2(3k+2t)log T + log 2`, the theorem yields a prime
`p ≤ x`, `log x = C₂(1+log 1.03)log Z`, with `p ≡ a' (Q')`, `p ∤ D`,
`B(p) > 0`. Then `F(p) = 1`, i.e. `p` lies in no `E_i`, and `p > ℓ' > T`
since `ℓ' | p−1`. This proves Theorem 1.1 with `C₇ = 2C₂(1+log1.03)+1`. ∎

*Proof of Lemma 1.2.* Fix `ψ` as in (Tw) and a prime `ℓ₀ | f` such that the
`ℓ₀`-component `ψ₀` of `ψ` is a nontrivial character of `X_{ℓ₀}` (exists as
`f > 1`). Let `F'` be the avoidance indicator of the events not containing
`ℓ₀`. Given `X_{−ℓ₀}`, `F = F'·1[X_{ℓ₀} ∉ Forb(X_{−ℓ₀})]`, where `Forb` is the
set of values of `X_{ℓ₀}` putting `n` into some `E_i ∋ ℓ₀`. As `𝔼_{X_{ℓ₀}}ψ₀ = 0`,
`|𝔼[Fψ]| = |𝔼[F'·∏_{ℓ≠ℓ₀}ψ_ℓ·𝔼_{X_{ℓ₀}}[ψ₀1_{Forb}]]| ≤ 𝔼[F'·ℙ_{X_{ℓ₀}}(Forb)]
≤ Σ_{i∋ℓ₀} ℙ(F'=1, E_i) ≤ 𝔼F'·Σ_{i∋ℓ₀} ℙ(E_i)∏_{j∼i}(1−x_j)^{−1} = η_{ℓ₀}𝔼F'`,
by the conditional local lemma ([SN] `lem:lll`, second part, applied to the
subfamily defining `F'` — the (LLL) hypothesis passes to subfamilies — with
`B = E_i`, whose `Γ(E_i)` in the subfamily is contained in `{j ∼ i}`).
Likewise `𝔼F' − 𝔼F = 𝔼[F'ℙ_{X_{ℓ₀}}(Forb)] ≤ η_{ℓ₀}𝔼F'`, so
`𝔼F' ≤ δ/(1−η_{ℓ₀})`. With `η_{ℓ₀} ≤ 1/6`: `|𝔼[Fψ]| ≤ (1/5)δ`. ∎

*Proof of Corollary 1.3.* Take `x_i = 2ℙ(E_i) ≤ 2w_ℓ ≤ 1/32`. For each `i`,
`Σ_{j∼i} x_j ≤ 2Σ_{ℓ∈supp E_i} w_ℓ ≤ 1/32`, so `∏_{j∼i}(1−x_j) ≥ 31/32` and
`ℙ(E_i) ≤ x_i∏_{j∼i,j≠i}(1−x_j)` holds; `δ_L ≥ e^{−2.2S}` (`1−x ≥ e^{−1.1x}` on
`[0,1/32]`); `η_ℓ ≤ e^{1.1/32}w_ℓ ≤ 1.04/(64k) < 1/6`. Then
`k₀ ≤ 2k log₂(NT) + 3.2S + log₂(S+1) + 12 ≪ S + k log(4NT)` (as `k ≥ 1`),
`t ≪ k log(4NT)(S + k log(4NT))`, and Theorem 1.1 gives the bound (the
`3k log T` and `+1` terms are dominated). ∎
