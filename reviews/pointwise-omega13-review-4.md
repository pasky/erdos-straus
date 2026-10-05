# Review R48d (independent reviewer 2 of 2) of POINTWISE_OMEGA13.md §5 and Thm 5.1

Reviewer: hostile side agent (branch side-agent/review-omega13d). Reviewed text: POINTWISE_OMEGA13.md at
side-agent/beyond-fifth commit ac109c3. Scripts: scripts/review_o13d_*.py (from scratch, no author code reused).
Written before reading reviews/pointwise-omega13-review-3.md.

## Summary verdicts

| claim | verdict |
|---|---|
| I1(a) BRW minorant + EL_mod with S_res | SOUND |
| I1(b) twist via Lemma 1.1 general conditional bound | SOUND |
| I2 junta (O11 Lemma 1.1 / Cor 1.2 on fibre `n≡r (ℓ^{a_ℓ})`) | SOUND |
| I3 coset transfer, property (I), Mordell-hardness | SOUND-AFTER-REPAIRS (D1) |
| Thm 5.1 (exponent 1/4) | (pending) |

## 1. The construction, re-derived in my own words (for a given large T)

1. *Quarantine process.* `Q_0=8`, `r≡1 (8)`; forced `a=0` steps at 3,5,7 (r mod 105 a uniformly random
   square class; mod 3 this is 1). Then, for odd primes `ℓ≤Y=𝓛^{C_0+4}` only, while some such ℓ has
   `w̃_ℓ=Σ_{E: v_ℓ(M)>a_ℓ}β^{s(E)}μ(E)>η`, raise `a_ℓ` by one, revealing `n mod ℓ^{a_ℓ+1}` uniformly among
   the fibre classes that are squares mod ℓ. Events = all atoms `(M,D)`, `M≤T`, `M≡3 (4)`, `D|A_M²`,
   with `μ(E)` the fibre probability of `n≡−4D (M)`. `β=1+1/log𝓛`, `η=(3/4)logβ≍1/log𝓛`.
2. *Good realisation.* Three bad events (cost `>4E`, residual mass `>4E`, some `ℓ∈(Y,T]` with `w̃_ℓ>η`),
   each of probability `≤1/4`; the process has finitely many outcomes, so a good `(Q,r)` exists.
3. *Residual system.* Coordinates `X_ℓ=n mod ℓ^{f_ℓ}` on `n≡r (ℓ^{a_ℓ})` for every odd `ℓ≤T` with
   `a_ℓ<f_ℓ`; (1.1) holds at all of them; no atom is deterministic (Lemma 3.1).
4. *Minorant.* BRW `B=1−ΣA_i(1−v_i)²` on the `m≤T²` atoms, `u_j`= digit-modulus truncation of `F^{(j)}`
   at `τ=2𝓛⌈log₂(100m²(S+1)e^{3S})⌉`, `S=S_res`.
5. *Transfer.* Append `ℓ_aux∈(R,2R]`, `R=max(T,max d_i)`, to Q; O9 Thm 1.1 in O11 Lemma 3.1's coset form
   on `r'H`, `H={x≡1 (Qℓ_aux)}`; this produces a prime `p≡r' (Qℓ_aux)` with `B(p)>0`, hence `W(p)>T`.

## 2. Interface checks

**I1(a) — SOUND.** O8 Lemma 3.1 is algebra for arbitrary events and `u_j` (re-derived: `F−B=ΣA_i(f_{<i}−v_i)²`).
`2^{−τ/(2𝓛)}≤1/(100m²(S+1)e^{3S})` by the choice of τ; `ΣP(E_j)≤S_res` because `β^s≥1`;
`δ≥e^{−(4/3)S_res}≥e^{−3S_res}`. O11 Lemma 1.1's hypotheses on the fibre `n≡r (ℓ^{a_ℓ})`: writing
`n=r_0+ℓ^{a}k` with `0≤r_0<ℓ^a`, there is no carry, so digits `≥a_ℓ` are those of k and are uniform (and
for `a_ℓ=0`, digit 0 uniform on `1..ℓ−1`), exactly as for r=1. Edge weights `∏λ^{2v}=2^{log M/𝓛}≤2`.
Lemma 2.1 of O9: `E[F−B]≤EF/100` and `EB≥0.99EF` give `E[F−B]≤EB/99`, `A≤1+2/99≤1.03`. ✔.

**I1(b) — SOUND.** Re-derived: with `ℓ_0|f`, `gcd(f,Q)=1` (so `ℓ_0` odd, `a_{ℓ_0}=0`, `X_{ℓ_0}` Haar on units
mod `ℓ_0^{f}`, and the `ℓ_0`-component of ψ has mean 0), `|E[Fψ]|≤E[F'·P_{X_{ℓ_0}}(Forb)]` and
`P(Forb|X_{−ℓ_0})≤Σ_{E∋ℓ_0}p_{ℓ_0}(E)1[E∖ℓ_0]`. The subfamily defining F' still satisfies the asymmetric LLL
hypothesis (fewer neighbours), and HSS's bound `P(A|∩F̄)≤P(A)∏_{F∈Γ(A)}(1−x_F)^{−1}` with
`Σ_{F∈Γ(A)}x_F≤Σ_{ℓ∈supp A}w̃_ℓ≤|supp A|η` gives `β^{s(E)−1}`; hence `|E[Fψ]|≤β^{−1}w̃_{ℓ_0}EF'≤ηEF'`.
Numerics: `η=0.19` gives `(0.01+0.19/0.81)/0.99=0.2471≤1/4` (tight but correct); at the value actually
used, `η≍1/log𝓛`, it is far from tight. `ℓ_0` may exceed Y: then (1.1) at `ℓ_0` comes from the good
realisation, not the stopping rule — covered. ✔.

**I2 — SOUND.** O11 Cor 1.2 depends on the class only through "digits `≥a_ℓ` uniform", checked above. Cell
moduli: atoms `≤T`, `u_j` cells `≤e^τ`, products of `A_iA_jA_{j'}u_ju_{j'}` give `≤T³e^{2τ}`. `log m≤2𝓛`. ✔.

**I3 — SOUND-AFTER-REPAIRS.** Case A: real characters mod Q (Q's 2-part is exactly 8) are products of
Legendre symbols at odd `p|Q` and characters mod 8; all are 1 at r. Case B, item 1, cell consistency: as
claimed. Property (I): re-derived (reduce `n≡−4D (M)` mod `gcd(M,Q)`; `M|Q` excluded by Lemma 3.1(b); else the
event occurs; all primes of M are either coordinates or have `ℓ^{v_ℓ(M)}|Q`). Mordell-hardness: the unit squares
mod 840 are exactly {1,121,169,289,361,529} (script check below). **But see D1** (class at `ℓ_aux`).
