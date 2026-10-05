# Review 3 of POINTWISE_OMEGA13.md §5 / Thm 5.1 (R48c, hostile reviewer 1 of 2)

Reviewed: branch side-agent/beyond-fifth at d1a680b/ac109c3 (§5 "interface checks I1–I3", Thm 5.1).
Status: IN PROGRESS.

## Summary verdicts

| claim | verdict |
|---|---|
| §5 Setting (fixed good realisation `(Q,r)` of Thm 3.4) | SOUND (deterministic by existence; see C0) |
| I1(a) BRW minorant + EL_mod with `S_res` | SOUND |
| I1(b) twist, `|μ_ψ|≤μ/4` for `η≤0.19` | SOUND |
| I2 junta via digit filtration | SOUND |
| I3 coset transfer (Case A/B, item 1, consistency) | SOUND-AFTER-REPAIRS (m1: class of r mod `ℓ_aux`) |
| I3 property (I) via Lemma 3.1; Mordell-hardness | SOUND |
| Thm 5.1 exponent chain to `1/4`, `(loglog p)^{−1/4}` | SOUND-AFTER-REPAIRS (m1) |

### C0. Is the final statement deterministic? (brief's explicit question)
Yes. Thm 3.4 shows that, under the law of the square-class process (a finite tree: at most
`Σ_{ℓ≤Y}f_ℓ` steps, each with finitely many outcomes), the three bad events have total
probability `≤3/4`, so some leaf `(Q,r)` is good. For each T this is a *fixed* pair, chosen
before B is built; every later object (`F`, `B`, `u_j`, `τ`, `d_i`, `ℓ_aux`, `x`) is a
deterministic function of `(T,Q,r)`. Randomness is used only as an existence device
(non-constructive, but `(Q,r)` could be found by exhaustive search over the finite tree).
Nothing in O9 Thm 1.1 / O11 Lemma 3.1 is averaged over r. The only realisation-dependent
quantities fed forward are `S_res` and `log Q`, and both are bounded on the good leaf
(`S_res≤4E S_res≪𝓛³log𝓛`, `log Q≤4E log Q≪𝓛³(log𝓛)^5`). No circularity: `Y=𝓛^{C_0+4}`
uses only the Y-uniform Ξ bound (as R48a m5 already noted).

## Defects

### C1. I1(a) — BRW minorant + EL_mod with `S_res` — SOUND
Re-derived. O8 Lemma 3.1 is algebraic (any events `A_j`, any real `u_j`):
`F−B=Σ_iA_i(Σ_{j<i}A_je_j)²≥0`, `E[F−B]≤m²Σ_jP(E_j)E[e_j²|E_j]`. O11 Lemma 1.1 with
`λ_ℓ=2^{logℓ/(2𝓛)}` needs only `∏ℓ^{v_ℓ(E)}=M≤T` (edge weight `2^{logM/𝓛}≤2`) and gives
`Σ_{log m_U>τ}‖F^{(j)=U}‖²≤2^{−τ/(2𝓛)}=2^{−⌈log₂(100m²(S_res+1)e^{3S_res})⌉}`. Hence
`E[F−B]≤S_res e^{−3S_res}/(100(S_res+1))≤e^{−3S_res}/100≤δ/100`, because
`ΣP(E_j)≤Σβ^{s}P(E)=S_res` and `δ≥e^{−(4/3)S_res}≥e^{−3S_res}` (Lemma 1.1 needs `x_E≤η≤1/4`,
true). `μ≥0.99δ`, and O9 Lemma 2.1 (`B^-≤F−B`) gives `A≤1+2/99≤1.03`. Both use only
`E_{rH}`, never the class. `τ≍𝓛S_res+𝓛²` (with `log m≤2𝓛`), as claimed.
Toy check (i) in `scripts/review_o13c_twist.py`: `exp(−(4/3)S)/δ≤0.98` over ~19k events,
β up to `e^{1/3}` (`data/review_o13c/twist.txt`).

### C2. I1(b) — twist — SOUND
Re-derived. f is odd, because `8|Q` and `gcd(f,Q)=1`. So ψ is a product of Legendre symbols at
the primes of f, and each `ℓ_0|f` is an `a=0` unit coordinate. Write `F=F'·1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]`.
Since `E_{X_{ℓ_0}}ψ_{ℓ_0}=0`, we get `|E_{X_{ℓ_0}}[1_{∉Forb}ψ_{ℓ_0}]|≤P_{X_{ℓ_0}}(Forb)`, so
`|E[Fψ]|≤Σ_{E∋ℓ_0}p_{ℓ_0}(E)P(E∖ℓ_0∩F')`. The general conditional bound
`P(A|∩_𝒮F̄)≤P(A)∏_{F∈𝒮,F∼A}(1−x_F)^{−1}` is standard (HSS 2011 Thm 2.1). It needs:
* the LLL condition for 𝒮, inherited by subfamilies;
* A mutually independent of the 𝒮-events with disjoint supports, true in a product space.

The product is `≤exp((4/3)Σ_{ℓ∈supp A}w̃_ℓ)≤β^{|supp A|}`, using sums over a subfamily
`≤w̃_ℓ≤η`. With `|supp(E∖ℓ_0)|=s(E)−1` and `P(E)=p_{ℓ_0}(E)P(E∖ℓ_0)`, this gives
`|E[Fψ]|≤β^{−1}w̃_{ℓ_0}EF'`. The same computation without ψ gives `EF≥(1−η)EF'`.

Numerics: the requirement is `(0.01+η/(1−η))/0.99≤1/4`, i.e. `η≤0.19192`. With
`β=1+1/log𝓛`, `η≤0.19` iff `𝓛≥32.2` ("large T"). Also `w̃_{ℓ_0}≤η` holds at `ℓ_0>Y`, by
the good-realisation choice, and at `ℓ_0≤Y`, by stopping.

Toy checks (ii)–(iv), exact enumeration including a fibre coordinate with `a=1`, all `≤1`:
* conditional bound ratio ≤0.981;
* `|E[Fψ]|/(β^{−1}w̃_{ℓ_0}EF')` ≤0.68;
* `(1−η)EF'/EF` ≤0.997.
