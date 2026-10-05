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

## 1. The linear transfer theorem

**Cited input (G) — Gallagher (Invent. Math. 11 (1970) 329–339, Thm 7),
in the form of Montgomery–Vaughan, *Multiplicative Number Theory III*
(draft, `sources/omega9/montgomery-mnt3.pdf`, Theorem 28.19, p. 229–230):**
there are absolute constants `c≥1`, `κ≥3` such that for `1<Q_G^{6c}≤x`

```
Σ_{q≤Q_G} Σ*_{χ mod q} |ϑ(x;χ) − E_0(χ)x|  ≪  x·exp(−log x/(κ log Q_G)) + (log x/log Q_G)²·x/Q_G,
```

(`ϑ(x;χ)=Σ_{p≤x}χ(p)log p`, Σ* over primitive χ, `E_0(χ)=1` iff χ is the
trivial character mod 1) **unless** `∏_{q≤Q_G}∏*_χ L(s,χ)` has a real zero
`β_1` with `1−β_1<1/(κ log Q_G)`. In that case the term of the (unique, real)
exceptional character `χ_1` is replaced by `|ϑ(x;χ_1)+x^{β_1}/β_1|` and the
right side by `(1−β_1)(log x)·x·exp(−log x/log Q_G) + x log x/(Q_G log Q_G)`.

We also use the classical effective bound `1−β_1 ≫ q_1^{−1/2}(log q_1)^{−2}`
for a real zero of `L(s,χ_1)`, `χ_1` real primitive of conductor `q_1`
(Davenport ch. 14).

**Theorem 1.1 (linear transfer; PROVED modulo (G)).** Let `T,Q`, and
`B(n)=Σ_{i∈I}c_i1[n≡b_i (d_i)]` satisfy the hypotheses of PO Thm 4.1
(`gcd(d_i,Q)=gcd(b_i,d_i)=1`; `B(n)≤1[W(n)>T]` for all `n≡1 (Q)` coprime to
all `d_i`; `μ>0`; twist condition `|μ_ψ|≤μ/4` for every real primitive ψ of
conductor `f>1`, `gcd(f,Q)=1`, `f|d_i` for some i). Let `D:=lcm_i d_i`,
`Z:=Q·max d_i` and

```
A := E_D|B| / μ      (E_D: mean over the units mod D),   N := |I|.
```

There is an absolute effective constant `C_2` such that, if `A≤Z^{1/4}` and

```
log x ≥ C_2·[ (1+log A)·log Z + log N + log log(QD) ],
```

then some prime `p≤x`, `p≡1 (Q)`, `p∤D`, has `W(p)>T`.

So `M_1` disappears; the only price for the size of B is the additive
`log N`. Compare PO Thm 4.1: `log x ≥ C_1(1+log(M_1/μ))·max(log Z, K)`.
