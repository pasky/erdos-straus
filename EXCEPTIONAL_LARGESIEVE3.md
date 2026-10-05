# EXCEPTIONAL_LARGESIEVE3 — H_LS∞ for forced families via sparsity (task O59)

Status: **in progress** (agent O59, branch `side-agent/hls-sparse`). Labels as
in `DISCOVERIES.md`. Notation: LS = `EXCEPTIONAL_LARGESIEVE.md`, LS2 =
`EXCEPTIONAL_LARGESIEVE2.md`, K2 = `EXCEPTIONAL_KARY2.md`, K3 =
`EXCEPTIONAL_KARY3.md`, EK = `EXCEPTIONAL_KARY.md`.

Setting (LS §1). 𝔊 is a finite mixture of ℛ(M)-, (a,D)-, Case-A and selector
classes (K2 Def 2.0), `𝒜 = 𝒜(𝔊)`, `M₀` the lcm of the moduli. A large-sieve
bound is an N-large-sieve system `(Θ,w)` (LS (LS)), any rational frequencies,
any weights; it is CRT-admissible if `Z ≤ 1/L` with `L ≤ F_w(π)` for every
probability π on `𝒜 mod M'` (LS §1), `F_w(π) = Σ_θ w_θ|π̂(θ)|²`. Facts:
`w_θ ≤ 1/N` (LS Fact 1.1), `Σ_θ w_θ ≤ 1` (LS Fact 4.0). By LS Rem 3.3 we
may and do take π uniform on all CRT digits not resolved by `M₀`, so only
θ with `den θ | M₀` matter; we write `M' = M₀`.

## 0. Summary (so far)

| item | statement | label |
|---|---|---|
| Thm 1.1 | **smooth–rough splitting.** For any `z`, the z-smooth CRT coordinates cost only the *density* of a measure on the z-smooth avoider set (no Fourier or level information at all); only the z-rough part needs Fourier control, in the `ℓ^{2+2β}` sense of LS Thm 4.1 | PROVED |
| Lemma 2.1 | the z-smooth part costs `≤ 2T₁ + O(1)`, `T₁ ≍ 𝔐(z) ≪ (log z)³(log log z)³` (sequential law with square base, conditioned on a good set) | PROVED (K2 §§2–4; Case A via ElT Prop 1.4) |
| Thm 3.1 | **rough-slice mixtures**: if every modulus of 𝔊 has at most one prime factor `> z = exp((log N)^{1/4})`, every CRT-admissible large sieve (any rational frequencies, any denominators, any weights) saves `≤ C(log N)^{3/4}(log log N)³` | PROVED (same inputs) |

## 1. The smooth–rough splitting

Fix `z ≥ W₁` (W₁ an absolute constant, chosen in Lemma 2.1). Write
`M₀ = M_s M_r` with `M_s` z-smooth and `M_r` z-rough (all prime factors
`> z`). By CRT `n ↔ (c, r)`, `c = n mod M_s`, `r = n mod M_r`, and every
θ with `den θ | M₀` is uniquely `θ = θ_s + θ_r`, `den θ_s | M_s`,
`den θ_r | M_r`, with `e(nθ) = e(cθ_s)e(rθ_r)`.

For a class `C = (b mod G)` of 𝔊 write `G = G_s G_r` likewise.
* `𝒜_s ⊂ ℤ/M_s`: the residues c avoiding every class with `G_r = 1`.
* For `c ∈ 𝒜_s`, the *fibre family* `𝔊_c = {(b_C mod G_r(C)) : C ∈ 𝔊,
  G_r(C) > 1, c ≡ b_C (mod G_s(C))}` and its avoider set `𝒜_c ⊂ ℤ/M_r`.

Then `𝒜 mod M₀ = {(c,r) : c ∈ 𝒜_s, r ∈ 𝒜_c}`.

For a probability σ on a finite cyclic group `ℤ/m` and `p' ≥ 2` put
`𝓡_{p'}(σ) = Σ_{θ ∈ m^{−1}ℤ/ℤ} |σ̂(θ)|^{p'}` (θ = 0 included, `σ̂(0) = 1`).

**Theorem 1.1 (smooth–rough splitting; PROVED).** Let `0 < β ≤ 1/2`,
`p' = 2 + 2β`. Let `π_s` be a probability on `𝒜_s` with
`π_s(c) ≤ ρ/M_s` for all c, and for each `c ∈ supp π_s` let `π_c` be a
probability on `𝒜_c`. Then every CRT-admissible bound B from any
N-large-sieve system satisfies

    log(N/B) ≤ β log N + log ρ + log E_{c∼π_s} 𝓡_{p'}(π_c).            (1.1)

*Proof.* Let `π = Σ_c π_s(c) δ_c ⊗ π_c`; it is supported on 𝒜, and
`π̂(θ_s + θ_r) = Σ_c π_s(c) e(cθ_s) π̂_c(θ_r)`.
*Hausdorff–Young in c* (as in LS Thm 4.1). Fix `θ_r`. Put
`f(c) = M_s π_s(c) π̂_c(θ_r)` on `ℤ/M_s` (uniform probability on the group,
counting measure on the dual), so `π̂(θ_s+θ_r) = f̂(θ_s) := E_c f(c)e(cθ_s)`.
With `p = p'/(p'−1) ∈ (1,2)`, Hausdorff–Young gives
`Σ_{θ_s}|f̂(θ_s)|^{p'} ≤ (E_c|f|^p)^{p'/p}`. Now
`E_c|f|^p = E_{c∼π_s}[(M_sπ_s(c))^{p−1}|π̂_c(θ_r)|^p] ≤ ρ^{p−1}E_{π_s}|π̂_c(θ_r)|^p`,
and `(p−1)p'/p = 1`, so by Jensen (`p'/p ≥ 1`)
`Σ_{θ_s}|π̂(θ_s+θ_r)|^{p'} ≤ ρ (E_{π_s}|π̂_c(θ_r)|^p)^{p'/p} ≤ ρ E_{π_s}|π̂_c(θ_r)|^{p'}`.
Summing over `θ_r`: `𝓡_{p'}(π) ≤ ρ E_{π_s}𝓡_{p'}(π_c)`.
*Hölder* (LS Thm 4.1, with Facts 1.1 and 4.0):
`F_w(π) ≤ (Σ_θ w_θ)^{β/(1+β)}(Σ_θ w_θ|π̂(θ)|^{p'})^{1/(1+β)} ≤ (𝓡_{p'}(π)/N)^{1/(1+β)}`.
So `B ≥ 1/F_w(π) ≥ (N/𝓡_{p'}(π))^{1/(1+β)}` and
`log(N/B) ≤ (β log N + log 𝓡_{p'}(π))/(1+β) ≤ β log N + log⁺𝓡_{p'}(π)`
(`𝓡 ≥ 1` since θ = 0 contributes 1). ∎

*Remarks.* (a) Nothing is assumed about the smooth frequencies `θ_s`: their
denominators may have any number of prime factors `≤ z`, i.e. any level.
The smooth coordinates are paid for by `log ρ` only — a pure density
statement about `𝒜_s`. So the part of (E1) (LS §7, LS2 §5) coming from
denominators with many prime factors `≤ z` is closed as soon as `log ρ` is
small (Lemma 2.1: `z = exp((log N)^{1/4})` is affordable).
(b) In the fibres only the rough frequencies enter, through the
`ℓ^{p'}` mass `𝓡_{p'}(π_c)` (LS's (H_LS) restricted to z-rough
coordinates). For product measures `π_c` this is LS Thm 4.1's computation
(§3). What remains open in general is the case where classes of 𝔊 have
**two or more** prime factors `> z` (§4).
(c) The same proof with a level split instead of Hölder gives: if
`E_{π_c}H ≤ e^{S_r}E_U H` for all `H ≥ 0` with rough frequencies of rough
level `≤ 2λ'` and `|π̂_c(θ_r)|² ≤ e^{S_r}/N` above rough level λ', then
`log(N/B) ≤ log ρ + S_r + log 2` (Cauchy–Schwarz plus LS2 Lemma 2.2 on the
low part; `Σw ≤ 1` on the high part). This is LS2 Prop 5.2 with the smooth
coordinates removed from both conditions.
