# Exponent beyond 1/13: a linear transfer (task O34)

Task O34 (branch `omega9-exponent`). Labels as in the house rules. ES is
not touched; nothing below bears on whether `W(p)<∞`. Notation: PO =
`POINTWISE_OMEGA.md`, O8 = `POINTWISE_OMEGA8.md` (incl. §6), `𝓛=log T`.

**Status: checkpoint 1 (self-reviewed once, R34a; not parent-reviewed).**

**Results at a glance.**
1. **Theorem 1.1 (linear transfer; PROVED modulo Gallagher's theorem (G)).**
   PO Thm 4.1's condition `log x ≥ C(1+log(M_1/μ))·max(log Z,K)` is replaced
   by `log x ≥ C(1+log A)·log Z` with `A=E|B|/μ`. Neither `M_1` nor the
   number of cells enters.
2. **Theorem 2.2 (PROVED mod (G) and Elsholtz–Tao Prop 1.4):**
   `W(p) ≥ exp(c(log p)^{1/7})` for infinitely many Mordell-hard p;
   `log L_h(T) ≪ (log T)^7`. Replaces O8 Thm 6.3 (1/13).
3. **Theorem 2.3 (PROVED mod (G)):** `log W ≥ (1/log2−o(1))log₂p·log₃p`
   (O8 Thm 4.4 had `1/(2log2)`).

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
`E[F−B]≤μ/99`, `E|B| ≤ 1.03μ` (Lemma 2.1). Every χ with `c(χ)≠0` has
conductor dividing some `Qd_i`, hence `≤Z`. A log-free zero-density
estimate summed over **all** primitive characters of conductor `≤Z`
(Gallagher 1970) then bounds the total error by
`≪ μ·x·exp(−c log x/log Z)/φ(Q)`, as in Linnik's theorem for a single
class. Result: the certified bound is `log p ≪ log Z`.

## 1. The linear transfer theorem

**Cited input (G) — Gallagher (Invent. Math. 11 (1970) 329–339, Thm 7),
in the form of Montgomery–Vaughan, *Multiplicative Number Theory III*
(draft, `sources/omega9/montgomery-mnt3.pdf`, Theorem 28.19, p. 229–230):**
there are absolute constants `c≥1`, `κ_0≥3` such that, for any fixed
`κ≥κ_0`, for `1<Q_G^{6c}≤x`

```
Σ_{q≤Q_G} Σ*_{χ mod q} |ϑ(x;χ) − E_0(χ)x|  ≪  x·exp(−log x/(κ log Q_G)) + (log x/log Q_G)²·x/Q_G,
```

(`ϑ(x;χ)=Σ_{p≤x}χ(p)log p`, Σ* over primitive χ, `E_0(χ)=1` iff χ is the
trivial character mod 1) **unless** `∏_{q≤Q_G}∏*_χ L(s,χ)` has a real zero
`β_1` with `1−β_1<1/(κ log Q_G)`. In that case the term of the (unique, real)
exceptional character `χ_1` is replaced by `|ϑ(x;χ_1)+x^{β_1}/β_1|` and the
right side by `(1−β_1)(log x)·[x·exp(−log x/log Q_G) + x log x/(Q_G log Q_G)]`
(the prefactor multiplies both terms; review R34a MAJOR 1).

Uniqueness, reality and quadraticity of `χ_1` come from MV's Exceptional
Zero Statement (28.61)–(28.62), p. 216, valid for zeros with
`1−β<c_1/log Q_G`; so we fix `κ := max(3κ_0, 1/c_1)` (R34a m1). *Source
caveat (R34a m2):* MV III is an unpublished draft, and its printed proof of
28.19 matches its two cases only for `κ=3κ_0` (a repairable slip). The
statement is the classical Gallagher (1970) Thm 7; neither the original nor
a published restatement (e.g. Iwaniec–Kowalski ch. 18) was checked.

We also use the classical effective bound `1−β_1 ≫ q_1^{−1/2}(log q_1)^{−2}`
for a real zero of `L(s,χ_1)`, `χ_1` real primitive of conductor `q_1`
(Davenport ch. 14; also MV III (28.62)).

**Theorem 1.1 (linear transfer; PROVED modulo (G)).** Let `T,Q`, and
`B(n)=Σ_{i∈I}c_i1[n≡b_i (d_i)]` satisfy the hypotheses of PO Thm 4.1
(`gcd(d_i,Q)=gcd(b_i,d_i)=1`; `B(n)≤1[W(n)>T]` for all `n≡1 (Q)` coprime to
all `d_i`; `μ>0`; twist condition `|μ_ψ|≤μ/4` for every real primitive ψ of
conductor `f>1`, `gcd(f,Q)=1`, `f|d_i` for some i). Let `D:=lcm_i d_i`,
`Z:=Q·max d_i` and

```
A := E_D|B| / μ      (E_D: mean over the units mod D).
```

There is an absolute effective constant `C_2` such that, if `A≤Z^{1/4}` and

```
log x ≥ C_2·(1+log A)·log Z,
```

then some prime `p≤x`, `p≡1 (Q)`, `p∤D`, has `W(p)>T`.

So neither `M_1` nor the number of cells enters at all. Compare PO Thm 4.1: `log x ≥ C_1(1+log(M_1/μ))·max(log Z, K)`.

*Proof.* Write `C_G` for the implied constant in (G). Put
`L:=2c+log(400C_G(A+1))` and `Q_G:=x^{1/(κL)}`. For `C_2` large the
hypothesis gives: `log Q_G ≥ C'log Z` with `C'` as large as we like (since
`L≪1+log A`), hence `Q_G ≥ Z`, `Q_G ≥ 10^4C_G(A+1)(κL)²` (use `A≤Z^{1/4}`,
`Z≥2`); `Q_G^{6c}≤x` (as `κL≥6c`); `log x≥16`; `x ≥ Z^5 ≥ C·A·Z^{4}` (R34a m4, R34b m1). Note
`D | lcm(1,…,max d_i)`, so `log D ≤ 1.04·max d_i` and `log(QD) ≤ 2Z`.

*Character expansion.* `f(n):=B(n)1[n≡1 (Q)]` is a function on
`G=(ℤ/QD)^*`, so `f(n)=Σ_{χ mod QD}c(χ)χ(n)` for `(n,QD)=1`, with
`c(χ)=φ(QD)^{−1}Σ_{n∈G}f(n)χ̄(n)`. Writing `χ=χ_Qχ_D` (CRT) and summing
over the class `n≡1 (Q)`: `c(χ)=E_D[Bχ̄_D]/φ(Q)`. Hence:

1. `c(χ)=0` unless `cond χ_D | d_i` for some i (the mean of
   `1[n≡b_i (d_i)]χ̄_D(n)` over units mod D vanishes unless `χ_D` is trivial on
   `n≡1 (d_i)`). So `c(χ)≠0` implies `cond χ ≤ Q·d_i ≤ Z ≤ Q_G`; as
   `χ↦χ*` is injective (below), there are at most `Σ_{q≤Z}φ(q) ≤ Z²` such χ.
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
S(x) = μx/φ(Q) + Σ_{χ: c(χ)≠0} c(χ)(ϑ(x;χ*) − E_0(χ*)x) + R_1,   |R_1| ≤ Z²·(Aμ/φ(Q))·2Z ≤ μx/(400φ(Q)).
```

*Case 0: no exceptional zero for the family `q≤Q_G`.* By (G) and item 2
the middle sum is at most
`(Aμ/φ(Q))·C_G x[e^{−L}+(κL)²/Q_G] ≤ μx/(200φ(Q))`. So `S(x)>0`.

*Exceptional zero `β_1`, character `χ_1`, `1−β_1<1/(κ log Q_G)`.*
Then `log x/log Q_G = κL`; put `u:=(1−β_1)log x < L`. The replaced right
side of (G) is `C_G·u·x[e^{−κL}+κL/Q_G]`, and times `Aμ/φ(Q)` it is
`≤ (μx/φ(Q))·C_G A·L[e^{−κL}+κL/Q_G] ≤ μx/(200φ(Q))·min(u,1)` — indeed
`u·[…]/min(u,1) = max(u,1)[…] ≤ L[…]`, and `2C_GAL(e^{−κL}+κL/Q_G) ≤ 1/100`
by the choice of L and `Q_G`. If no χ with `c(χ)≠0` has `χ*=χ_1`, this
finishes as in Case 0. Otherwise there is exactly one, and its term is
`c(χ)(ϑ(x;χ_1)+x^{β_1}/β_1) − c(χ)x^{β_1}/β_1`. The first part is inside
(G); `c(χ)` is real since χ and B are.

* *Case A: `χ_D` trivial.* Then `c(χ)=μ/φ(Q)` and the main term becomes
  `λμx/φ(Q)` with `λ:=1−x^{β_1−1}/β_1`. Since `1/β_1 ≤ 1+2(1−β_1)`,
  `λ ≥ 1−e^{−u}−2(1−β_1)e^{−u} ≥ 0.63min(u,1)−2min(u,1)/log x ≥ min(u,1)/2`,
  since `2(1−β_1)e^{−u} = 2ue^{−u}/log x ≤ 2min(u,1)/log x` (`ue^{−u}≤min(u,1/e)`)
  and `log x≥16` (R34a m3; numerically min ratio 1.215). By the previous
  paragraph the (G) error is `≤ λμx/(100φ(Q))`. For `R_1`: here `q_1 | Q`
  (χ_D trivial), so `q_1 ≤ Q ≤ Z` (R34a m5), and by the effective Page bound `u ≥ 16(1−β_1) ≫ Z^{−1/2}(log Z)^{−2}`
  and `λ ≫ Z^{−1/2}(log Z)^{−2}`; then `|R_1| ≤ 2AZ³μ/φ(Q) ≤ λμx/(100φ(Q))`
  because `x ≥ C·A·Z^4`. So `S(x) ≥ λμx/φ(Q)·(1−2/100) > 0`.
* *Case B: `χ_D` nontrivial.* By item 3, `|c(χ)x^{β_1}/β_1| ≤
  (|μ_ψ|/φ(Q))·2x ≤ μx/(2φ(Q))`. So `S(x) ≥ μx/φ(Q)·(1−1/2−1/100) > 0`.

In all cases `S(x)>0`, so some prime `p≤x`, `p≡1 (Q)`, `p∤D`, has
`B(p)>0`, and then `W(p)>T`. ∎

*Remark.* The proof is Linnik's theorem with weights: the coefficient of
every character is bounded by `E|B|/φ(Q)`, not by `M_1/φ(Q)`, and (G)
controls all characters of conductor `≤Q_G` *simultaneously*, so the number
of moduli `d_i` and the spectral size of B never multiply the zero-density
error. The positivity of B is never used beyond `E|B| ≤ Aμ`.

## 2. Application: exponent 1/7

**Lemma 2.1 (BRW minorants are ℓ¹-tight; PROVED).** If `B≤F` pointwise,
`0≤F≤1` and `E[F−B] ≤ η·E B`, then `E|B| ≤ (1+2η)E B`.

*Proof.* `B^-:=max(−B,0) ≤ F−B` since `F≥0`; `E|B| = E B+2E B^-`. ∎

**Theorem 2.2 (PROVED modulo (G) and Elsholtz–Tao Prop 1.4; Thorner–Zaman
is no longer used).** For infinitely many Mordell-hard primes p,

```
W(p) ≥ exp( c·(log p)^{1/7} );     uniformly  log L_h(T) ≪ (log T)^7.
```

*Proof.* Take O8 Thm 3.4's system (`z=𝓛²`, `k=⌊𝓛/log z⌋`, Π from O2 Lemma
11.2 with `c_0=1/(64k)`) and O8 Lemma 6.1's minorant B with
`k_0` as in O8 Cor 4.2 (Lemma 6.1's error `e^{1/2}·2·4^{−k_0} ≤ 4·2^{−k_0}`
meets EL of Thm 3.4). O8 Thm 3.4's proof gives:
`δ=E F ≥ e^{−2.2S}`, `E[F−B] ≤ δ/100`, `μ ≥ 0.99δ`, `B≤1[W>T]` on
`n≡1 (Q)` coprime to all `d_i`, the twist condition (Lemma 3.3), and the
cell conditions, with `Q:=Q_Π·ℓ_aux` as in O4 Thm 2.1 (`ℓ_aux∈(R,2R]`, `R=max(T,max d_i)`,
only to force `p>T`). By Lemma 2.1 with
`η=1/99`: `A ≤ 1.03` (Thm 1.1's `E_D` over units mod `D=lcm d_i` is O8's
Haar expectation for functions of the residues mod the `d_i`; R34a note). Now apply Theorem 1.1 instead of PO Thm 4.1; it
needs only `log x ≥ C·log Z`, and (as in O8 Thm 3.4/6.3)
`log Z ≤ log Q_Π + 2(3k+2d+1)𝓛`.

With `z=𝓛²` and ET (`S≤S*≪𝓛^4log𝓛`, O2 Lemma 11.1) these are upper bounds:
`w=kb≪𝓛²/log𝓛`, `k_0≪S*+k𝓛≪𝓛^4log𝓛`, `d=4C_Hwk_0≪𝓛^6`,
`log Q_Π ≤ (π(z)+64k²S*)𝓛+4 ≪ 𝓛^7/log𝓛`, `(3k+2d+1)𝓛≪𝓛^7`. Hence some
hard p with `W(p)>T=e^𝓛` has `log p ≪ 𝓛^7`. Since `p>T`, letting `T→∞`
gives infinitely many distinct such p. ∎

**Theorem 2.3 (PROVED modulo (G) only).**
For infinitely many Mordell-hard p, `log W(p) ≥ (1/log 2 − o(1))·log₂p·log₃p`.

*Proof.* As 2.2, unconditionally. O2 Lemma 11.1 gives
`S* ≤ C log𝓛·(3+𝓛)·Σ_{sr'²≤T}τ(4sr'²+1)/(sr')`; a single τ appears, so
Wigert's `τ(n)≤2^{(1+o(1))log n/log log n}` (`n≤4T+1`) and
`Σ_{sr'²≤T}1/(sr')≪𝓛²` give `log S* ≤ (log2+o(1))𝓛/log𝓛` (R34b m2). Then every cost
term is `≤ 𝓛^{O(1)}(S*+1)`, so `log₂p ≤ log S* + O(log𝓛) ≤
(log2+o(1))𝓛/log𝓛`, which inverts to `𝓛 ≥ (1/log2−o(1))log₂p·log₃p`. ∎

(O8 Thm 4.4 had `1/(2log2)`: the square `K·log Z` doubled `log S*`.)

**Budget after Thm 1.1 (under ET; upper bounds, not asymptotics).** The
certified bound is `log p ≪ log Q_Π + d𝓛`, with the budgets
`log Q_Π ≪ k²S*𝓛 ≪ 𝓛^7/log𝓛` and `d𝓛 ≪ k·b·S*·𝓛 ≪ 𝓛^7`. K and the number of
cells are now irrelevant, so R30c M1(i)
(the missing q-ary ℓ¹ bound) is **no longer needed** for the ESW route.
Remaining losses: the bit width `b≍𝓛` in d; the quarantine budget `|𝓑|≤64k²S*`;
S* through ET; and the per-prime cost `𝓛` of every modulus prime.

## 4. Phase 2: the junta term `d𝓛`

After Thm 1.1 the certificate is `log p ≪ log Q_Π + d𝓛`, and `d𝓛` is the
larger term (R34b tally): `d=4C_H·kb·k_0`. Here we ask what any proof of
an Efron–Stein (ES) tail bound, the EL hypothesis of O8 Thm 3.4, could
give for general systems.

**Lemma 4.1 (junta lower bound for ES approximation; PROVED).** Let
`E_1,…,E_m` be single-value events with pairwise disjoint supports, each
on k coordinates uniform on `[q]` (`π:=q^{−k}=P(E_i)`, `S=mπ`), and
`F=∏(1−A_i)`, `δ=E F=(1−π)^m`. Then for every t,

```
energy(F;t) ≥ (1−π)^{2m} Σ_{j>t/k} binom(m,j) ρ^j,     ρ := π(1−1/q)^k/(1−π)².
```

Consequently, as `q→∞` with k, S fixed and `m=S/π`:
`energy(F;t)/δ → e^{−S}Σ_{j>t/k}S^j/j! = Pr[Po(S)>t/k]`.

*Proof.* `1−A_i` depends only on `X_{E_i}`, and the supports are disjoint,
so `F^{=U}=∏_i(1−A_i)^{=U∩E_i}`. Hence
`‖F^{=U}‖²=∏_i‖(1−A_i)^{=U∩E_i}‖²`. Keep only the sets
`U=⋃_{i∈J}E_i`. Then `‖(1−A_i)^{=∅}‖²=(1−π)²`, and for `i∈J`
`‖(1−A_i)^{=E_i}‖²=‖A_i^{=E_i}‖²=∏_{ℓ∈E_i}q^{−1}(1−q^{−1})=π(1−1/q)^k`,
since `A_i` is a product of the independent indicators `1[X_ℓ=c_ℓ]`, whose
nonconstant parts have variance `q^{−1}(1−q^{−1})`. Such U have
`|U|=k|J|`, so summing over `|J|>t/k` gives the bound. For the limit,
`binom(m,j)ρ^j → S^j/j!` and `(1−π)^m → e^{−S}`. ∎

**Corollary 4.2 (the method needs junta `≳k·S`; PROVED).** In the
setting of Lemma 4.1 (limit `q→∞`):
* every junta-t function g with `E(F−g)² ≤ δ/3` has `t ≥ k(S−1)`.
  (`Pr[Po(S)≥S−1] ≥ 1/2`, since the median of `Po(S)` is `≥S−log2`
  (Choi 1994); so `E(F−g)² ≥ energy(F;t) ≥ (1/2−o(1))δ`.)
* O8's EL level `energy ≤ e^{−3S}/poly` forces `Pr[Po(S)>t/k] ≤ e^{−2S}`,
  i.e. `t ≥ (c_*−o(1))kS` as `S→∞` (Poisson large deviations), with
  `c_*log c_*−c_*+1=2` (`c_*≈3.59`).

The F^{(j)} of O8 Lemma 3.1 are of the same form (the restriction of F to
`E_j` for a disjoint system is the good-indicator of the other events). So
for general systems of width k and mass S, any argument that certifies EL
needs junta `≍kS` at least. ESW (`d≍k·k_0≍kS`) would therefore be optimal
up to constants. The bit factor `b≍𝓛` is the only removable loss in
`d=4C_H·kb·k_0`. Under ET with mass `≍S*` at width `≍k` (the worst case
the present bookkeeping allows), the method's floor is
`d𝓛 ≳ kS*·log z`. That is `𝓛^5` up to logs if junta primes are small and
`𝓛^6/log𝓛` if they are `≈T`. Hence **1/6 is the ceiling of
width-and-mass-only arguments**. (Check: `scripts/omega9_junta_lb.py`
computes exact ES energies for 4 toys (`q≤7`, `k≤3`, `m≤6`); the bound
holds at every t, with equality at the top levels.) (Assessment for the ES system: its actual
mass need not sit at width k).

**4.3 A direct q-ary route to ESW, and where it stops (identity PROVED; rest
Assessment).** For `L_V:=∏_{v∈V}(I−E_v)` (E_v averages out coordinate v) one
has the standard identity

```
Σ_U binom(|U|,s)·‖F^{=U}‖² = Σ_{|V|=s} ‖L_V F‖²,
```

so `energy(F;d)·binom(d,s) ≤ Σ_{|V|=s}‖L_VF‖²`. Here
`L_VF(x)=E_y Σ_{W⊆V}(−1)^{|W|}F(x^{(W)})`, an alternating sum over the
`2^s` hybrids `x^{(W)}` (coordinates of W taken from y). It vanishes unless
(a) the events *relevant on the cube* cover V, where an event is relevant
when its literals are met by x off V and by x or y on V (probability
`≤2^{|E∩V|}P(E)`), and (b) no event avoiding V occurs at x. With (a) alone
and a union bound over minimal covers, one would get
`energy(F;C·k·s) ≤ 2^{−s}e^{S}` when relevance events are independent. The
`2^s`, the `binom(kr,s)≤(ek)^s` choices of V and `Σ_r S^r/r!` would give
**`d≍k(S+log(1/ε))` with no bit factor**, i.e. ESW.

But relevance events of overlapping events are not independent. Take a
hub: core H (`k−1` literals) plus M completions at distinct coordinates,
with `M·P(H)/q=:S_H`. Then the union bound over covers of s completion
coordinates gives `≈P(H)^{1−s}(2eS_H/s)^s`, which is huge. The true value
carries the factor `e^{−(M−s)/q}=e^{−Θ(S_H/P(H))}` from (b): no other
completion fires. Small per-prime masses (`S_H≤1/(64k)`) do not help
without (b). So a q-ary proof of ESW must use (b), i.e. *conditional*
suppression bounds of local-lemma type. This is exactly the ingredient
O8 §2.4 identifies as missing from alternating expansions. Completion mass
alone does not give it (O8 §2.4's counterexample). We leave ESW open.

## 3. Checks, scope, open items

* `scripts/omega9_charcheck.py` (`data/omega9/charcheck.txt`): toy with
  `Q=3`, `D=7·11·13·17`, B = inclusion–exclusion expansion of a random
  good-indicator. All 23040 coefficients satisfy
  `c(χ)=E_D[Bχ̄_D]/φ(Q)` (to `3·10^{−17}`) and `|c(χ)|≤E|B|/φ(Q)`. The prime
  sum's relative error (−0.09% at `x=3·10^6`) is far below the
  per-progression bookkeeping `(M_1/μ)·max ε_i` (20.1%). (An earlier run
  dropped all primes `≤D`; fixed, R34a.) Illustration only.
* **Inputs:** (G) as stated in MV III Thm 28.19 (a draft book; Gallagher's
  paper itself not read), the effective Page bound, O8 §§3–4, 6.1 (minorant,
  twist, local lemma), O2 Lemmas 4.3(I), 11.1–11.2, O4 Thm 2.1's auxiliary
  prime, ET Prop 1.4 (Thm 2.2 only). Thorner–Zaman is no longer used.
* **Not claimed:** anything about ES; optimality of 1/7; any numerical
  instance.
* **Supersedes (if review confirms):** O8 Thm 4.3/6.3 (1/14, 1/13), O8
  Thm 4.4's constant, and O8 §6.5/§6.6's ceilings, which concern PO Thm
  4.1 only. With Thm 1.1 the certified bound is `log p ≪ log Z`, so a large K
  is harmless; the cost of this route is the modulus budget
  `log Q_Π + (junta)·𝓛` (no lower bound for it is claimed). Note, though,
  a floor specific to the choice of z: `Q_Π ⊇ ∏_{ℓ≤z}ℓ^{e_ℓ}` with
  `ℓ^{e_ℓ}` the largest power `≤T`, so `log Q_Π ≫ π(z)𝓛 ≍ 𝓛^{1+a}/log𝓛`
  for `z=𝓛^a` (`𝓛³/log𝓛` at `a=2`: this certificate cannot beat ≈1/3
  with `z=𝓛²`). The only z-free floor is `log Z ≥ log ℓ_aux > 𝓛` (R34b).
* **Next (open):** exponent 1/6 needs *both* (i) ESW (`d≍k·k_0`; R30c
  M1(i) is moot now) and (ii) a quarantine with `log Q_Π ≪ 𝓛^6`, e.g. via a
  uniform per-prime bound `w_ℓ ≪ 𝓛^{O(1)}/ℓ` (an upper-bound divisor sum in
  progressions mod ℓ, Shiu-type), which would make the bad primes `≤𝓛^{O(1)}`.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900 uv run python scripts/omega9_charcheck.py 1 3e6)  # ~2 min -> data/omega9/charcheck.txt
(ulimit -v 8000000; timeout 600 uv run python scripts/omega9_junta_lb.py)         # ~10 s -> data/omega9/junta_lb.txt
```
