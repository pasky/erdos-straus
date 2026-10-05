# Exponent beyond 1/13: a linear transfer (task O34)

Task O34 (branch `omega9-exponent`). Labels as in the house rules. ES is
not touched; nothing below bears on whether `W(p)<∞`. Notation: PO =
`POINTWISE_OMEGA.md`, O8 = `POINTWISE_OMEGA8.md` (incl. §6), `𝓛=log T`.

**Status: work in progress (checkpoint 0). Nothing here is reviewed.**

## 0. The idea (opening (c) of the brief)

PO Thm 4.1 bounds each progression `θ(x;Qd_i,a_i)` separately with a
relative error `ε_i` and pays `Σ_i|c_i|ε_i/φ(d_i) ≤ M_1·max ε_i`; hence
`exp(−c log x/log Z) ≤ μ/M_1`, i.e. `log x ≳ K·log Z` (the square of
O8 §6.5). Expand instead in characters mod `QD`, `D=lcm d_i`:

```
Σ_{n≤x, n≡1 (Q), (n,QD)=1} Λ(n)B(n) = Σ_{χ mod QD} c(χ) ψ(x,χ),
c(χ_Q χ_D) = φ(Q)^{-1} · E_D[B·χ̄_D]       (E_D = Haar mean over units mod D).
```

So `|c(χ)| ≤ E_D|B|/φ(Q)`, and for a BRW minorant `B≤F` with
`E[F−B]≤μ/99`, `E|B| = E B + 2E B^- ≤ μ + 2E[F−B] ≤ 1.03μ` (since
`B^- ≤ F−B` as `F≥0`). Every χ with `c(χ)≠0` has conductor dividing some
`Qd_i`, hence `≤Z`. A log-free zero-density estimate summed over **all**
primitive characters of conductor `≤Z` (Gallagher 1970) then bounds the
total error by `≍ μ·x·exp(−c log x/log Z)/φ(Q)` — the same as Linnik's
theorem for a single class. The size `M_1` enters only through trivial
terms (prime powers, imprimitive characters), which cost `log x ≳ K`
**additively**. Expected outcome: `log p ≪ log Z + K`, i.e. under ET
`log p ≪ 𝓛^7` with O8's data: exponent `1/7` (to be proved below).
