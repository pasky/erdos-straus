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
right side by `(1−β_1)(log x)·[x·exp(−log x/log Q_G) + x log x/(Q_G log Q_G)]`
(the prefactor multiplies both terms; review R34a MAJOR 1).

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
`Z≥2`); `Q_G^{6c}≤x` (as `κL≥6c`); `log x≥16`; `x ≥ C·A·Z^{3}`. Note
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
  `λ ≥ 1−e^{−u}−2(1−β_1)e^{−u} ≥ 0.63min(u,1)−2min(u,1)/log x ≥ min(u,1)/2`
  (using `1−β_1≤1/(κ log Q_G)` when `u>1`, and `log x≥16`). By the previous
  paragraph the (G) error is `≤ λμx/(100φ(Q))`. For `R_1`: `c(χ)≠0` gives
  `q_1 ≤ Z`, so by the effective Page bound `u ≥ 16(1−β_1) ≫ Z^{−1/2}(log Z)^{−2}`
  and `λ ≫ Z^{−1/2}(log Z)^{−2}`; then `|R_1| ≤ λμx/(100φ(Q))` because
  `x ≥ C·A·Z^3`. So `S(x) ≥ λμx/φ(Q)·(1−2/100) > 0`.
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
`η=1/99`: `A ≤ 1.03`. Now apply Theorem 1.1 instead of PO Thm 4.1. Its
cost terms:

* `log Z ≤ log Q_Π + 2(3k+2d+1)𝓛` (as in O8 Thm 3.4/6.3);
* `log N`: B is a sum of at most `1+m+m²+m³` products, each expanded over
  the cells of its `≤3k+2d` coordinates (at most `T^{3k+2d}` cells), times
  the at most `(2Tb)^{2d}` pairs `(S,S')` of bit sets of size `<d`; so
  `log N ≤ 3log m + 2d log(2Tb) + (3k+2d)𝓛 + 2 ≪ (k+d)𝓛 ≪ log Z`;
* `log log(QD) ≤ log(log Q + 2T) ≪ 𝓛`.

So `log p ≪ log Z`. With `z=𝓛²` and ET (`S≤S*≪𝓛^4log𝓛`, O2 Lemma 11.1):
`w=kb≪𝓛²/log𝓛`, `k_0≪S*+k𝓛≪𝓛^4log𝓛`, `d=4C_Hwk_0≪𝓛^6`,
`log Q_Π ≤ (π(z)+64k²S*)𝓛+4 ≪ 𝓛^7/log𝓛`, `d𝓛≪𝓛^7`. Hence
`log p ≪ 𝓛^7` and `W(p)>T=e^𝓛`. Distinct T give distinct p. ∎

**Theorem 2.3 (PROVED modulo (G) only).**
For infinitely many Mordell-hard p, `log W(p) ≥ (1/log 2 − o(1))·log₂p·log₃p`.

*Proof.* As 2.2 with Wigert's `log S* ≤ (log2+o(1))𝓛/log𝓛`: every cost
term is `≤ 𝓛^{O(1)}(S*+1)`, so `log₂p ≤ log S* + O(log𝓛) ≤
(log2+o(1))𝓛/log𝓛`, which inverts to `𝓛 ≥ (1/log2−o(1))log₂p·log₃p`. ∎

(O8 Thm 4.4 had `1/(2log2)`: the square `K·log Z` doubled `log S*`.)

**Ledger after Thm 1.1 (under ET).** `log p ≍ log Z ≍ max(log Q_Π, d𝓛)`,
with `log Q_Π ≍ k²S*𝓛 ≍ 𝓛^7/log𝓛` and `d𝓛 ≍ k·b·S*·𝓛 ≍ 𝓛^7`. K is now
irrelevant (it enters only through `log N ≪ log Z`), so R30c M1(i)
(the missing q-ary ℓ¹ bound) is **no longer needed** for the ESW route.
Remaining losses: the bit width `b≍𝓛` in d; the quarantine `|𝓑|≍k²S*`;
S* through ET; and the per-prime cost `𝓛` of every modulus prime.

## 3. Checks, scope, open items

* `scripts/omega9_charcheck.py` (`data/omega9/charcheck.txt`): toy with
  `Q=3`, `D=7·11·13·17`, B = inclusion–exclusion expansion of a random
  good-indicator. All 23040 coefficients satisfy
  `c(χ)=E_D[Bχ̄_D]/φ(Q)` (to `3·10^{−17}`) and `|c(χ)|≤E|B|/φ(Q)`. The prime
  sum's relative error (−0.6% at `x=3·10^6`) is below the per-progression
  bookkeeping `(M_1/μ)·max ε_i` (17.5%). Illustration only.
* **Inputs:** (G) as stated in MV III Thm 28.19 (a draft book; Gallagher's
  paper itself not read), the effective Page bound, O8 §§3–4, 6.1 (minorant,
  twist, local lemma), O2 Lemmas 4.3(I), 11.1–11.2, O4 Thm 2.1's auxiliary
  prime, ET Prop 1.4 (Thm 2.2 only). Thorner–Zaman is no longer used.
* **Not claimed:** anything about ES; optimality of 1/7; any numerical
  instance.
* **Supersedes (if review confirms):** O8 Thm 4.3/6.3 (1/14, 1/13), O8
  Thm 4.4's constant, and O8 §6.5/§6.6's ceilings, which concern PO Thm
  4.1 only. With Thm 1.1 the cost is `log p ≍ log Z`, so `K≫𝓛²` (R30c m7)
  is harmless, and the route's ceiling becomes `log Z ≳ junta·log z +
  log Q_Π`.
* **Next (open):** exponent 1/6 needs *both* (i) ESW (`d≍k·k_0`; R30c
  M1(i) is moot now) and (ii) a quarantine with `log Q_Π ≪ 𝓛^6`, e.g. via a
  uniform per-prime bound `w_ℓ ≪ 𝓛^{O(1)}/ℓ` (an upper-bound divisor sum in
  progressions mod ℓ, Shiu-type), which would make the bad primes `≤𝓛^{O(1)}`.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900 uv run python scripts/omega9_charcheck.py 1 3e6)  # ~2 min -> data/omega9/charcheck.txt
```
