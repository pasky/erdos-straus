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
