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

*Proof.* Write `C_G` for the implied constant in (G). Put
`L:=2c+log(400C_G(A+1))` and `Q_G:=x^{1/(κL)}`. For `C_2` large the
hypothesis gives: `log Q_G ≥ C'log Z` with `C'` as large as we like (since
`L≪1+log A`), hence `Q_G ≥ Z`, `Q_G ≥ 10^4C_G(A+1)(κL)²` (use `A≤Z^{1/4}`,
`Z≥2`); `Q_G^{6c}≤x` (as `κL≥6c`); `log x≥16`; `x ≥ 400A·N·Z·log(QD)`.

*Character expansion.* `f(n):=B(n)1[n≡1 (Q)]` is a function on
`G=(ℤ/QD)^*`, so `f(n)=Σ_{χ mod QD}c(χ)χ(n)` for `(n,QD)=1`, with
`c(χ)=φ(QD)^{−1}Σ_{n∈G}f(n)χ̄(n)`. Writing `χ=χ_Qχ_D` (CRT) and summing
over the class `n≡1 (Q)`: `c(χ)=E_D[Bχ̄_D]/φ(Q)`. Hence:

1. `c(χ)=0` unless `cond χ_D | d_i` for some i (the mean of
   `1[n≡b_i (d_i)]χ̄_D(n)` over units mod D vanishes unless `χ_D` is trivial on
   `n≡1 (d_i)`). So `c(χ)≠0` implies `cond χ ≤ Q·d_i ≤ Z ≤ Q_G`, and there
   are at most `Σ_iφ(Qd_i) ≤ NZ` such χ.
2. `|c(χ)| ≤ E_D|B|/φ(Q) = Aμ/φ(Q)`; `c(χ_0)=μ/φ(Q)`.
3. If χ is real and `χ_D` is induced by a primitive ψ of conductor `f>1`,
   then `c(χ)=E_D[Bψ]/φ(Q)=μ_ψ/φ(Q)` (`μ_ψ=E_D[Bψ]` because the cells with
   `f∤d_i` have zero ψ-mean); if `c(χ)≠0`, the twist condition applies to ψ
   (`gcd(f,Q)=1` as `f|D`, and `f|d_i` by item 1).

*Expansion of the prime sum.* Let `S(x):=Σ_{p≤x, p∤QD, p≡1(Q)}B(p)log p
=Σ_χ c(χ)ϑ_{QD}(x;χ)`, where `ϑ_{QD}` omits `p|QD`. With χ* the primitive
character inducing χ, `|ϑ_{QD}(x;χ)−ϑ(x;χ*)| ≤ log(QD)`, and `χ↦χ*` is
injective. By items 1–2,

```
S(x) = μx/φ(Q) + Σ_{χ: c(χ)≠0} c(χ)(ϑ(x;χ*) − E_0(χ*)x) + R_1,   |R_1| ≤ NZ·(Aμ/φ(Q))·log(QD) ≤ μx/(400φ(Q)).
```

*Case 0: no exceptional zero for the family `q≤Q_G`.* By (G) and item 2
the middle sum is at most
`(Aμ/φ(Q))·C_G x[e^{−L}+(κL)²/Q_G] ≤ μx/(200φ(Q))`. So `S(x)>0`.

*Exceptional zero `β_1`, character `χ_1`, `1−β_1<1/(κ log Q_G)`.*
Then `log x/log Q_G = κL` and
`(1−β_1)log x·e^{−log x/log Q_G} ≤ L e^{−κL} ≤ e^{−L}`,
`log x/(Q_G log Q_G) = κL/Q_G`. So the replaced right side of (G),
times `Aμ/φ(Q)`, is again `≤ μx/(200φ(Q))`. If no χ with `c(χ)≠0` has
`χ*=χ_1`, this finishes as in Case 0. Otherwise there is exactly one, and
its term is `c(χ)(ϑ(x;χ_1)+x^{β_1}/β_1) − c(χ)x^{β_1}/β_1`. The first part is
inside (G); `c(χ)` is real since χ and B are.

* *Case A: `χ_D` trivial.* Then `c(χ)=μ/φ(Q)` and the main term becomes
  `λμx/φ(Q)` with `λ:=1−x^{β_1−1}/β_1`. Put `u:=(1−β_1)log x`. Since
  `1/β_1 ≤ 1+2(1−β_1)`, `λ ≥ 1−e^{−u}−2(1−β_1)e^{−u} ≥ 0.63min(u,1)−2min(u,1)/log x
  ≥ min(u,1)/2` (using `1−β_1≤1/(κ log Q_G)` when `u>1`, `log x≥16`). The
  (G) error relative to `λμx/φ(Q)` is `≤ 2AC_G[u e^{−κL}+κL/Q_G]/min(u,1)`.
  For `u≥1` this is `≤ 2AC_G[Le^{−κL}+κL/Q_G] ≤ 1/100`. For `u<1` it is
  `≤ 2AC_G[e^{−κL} + κL/(uQ_G)]`, and `uQ_G ≥ (1−β_1)Q_G ≫ Q_G^{1/2}/log²Q_G`
  by the effective Page bound (`q_1≤Q_G`); `≤1/100` for `C_2` large.
  With `R_1` (relative `≤ 1/(200λ)`... also absorbed since
  `x ≥ 400ANZ log(QD)` may be strengthened by a factor `Q_G^{1/2}`, again
  linear in `log Z`), `S(x) ≥ λμx/φ(Q)·(1−3/100) > 0`.
* *Case B: `χ_D` nontrivial.* By item 3, `|c(χ)x^{β_1}/β_1| ≤
  (|μ_ψ|/φ(Q))·2x ≤ μx/(2φ(Q))`. So `S(x) ≥ μx/φ(Q)·(1−1/2−1/100) > 0`.

In all cases `S(x)>0`, so some prime `p≤x`, `p≡1 (Q)`, `p∤D`, has
`B(p)>0`, and then `W(p)>T`. ∎

*Remark.* The proof is Linnik's theorem with weights: the coefficient of
every character is bounded by `E|B|/φ(Q)`, not by `M_1/φ(Q)`, and (G)
controls all characters of conductor `≤Q_G` *simultaneously*, so the number
of moduli `d_i` and the spectral size of B never multiply the zero-density
error. The positivity of B is never used beyond `E|B| ≤ Aμ`.
