# The witness-modulus tail over primes: a matching lower bound (task O76)

Task O76 (branch `two-sided-tail`). Labels as in the house rules. ES is not touched: nothing below
bears on whether `W(p)<∞`. Notation: `𝓛=log T`; O9 = `POINTWISE_OMEGA9.md`, O11 =
`POINTWISE_OMEGA11.md`, O13 = `POINTWISE_OMEGA13.md`, CU = `CEILINGS_UNIFIED.md`.
`N(x,T):=#{p≤x prime: W(p)>T}`.

**Status: checkpoint 1 (not yet parent-reviewed).** Results table in §4.

**Goal.** CU Thm 2.1 gives `N(x,T) ≪ π(x)e^{−c𝓛³}` for `𝓛≤c₁(log x)^{1/4}`. We want
`N(x,T) ≥ π(x)exp(−C𝓛³(log𝓛)^B)` in (almost) the same range.

**Key observation (§1).** O13 Thm 5.1 is an *existence* statement, but its proof (O9 Thm 1.1 run
on the coset `rH`) already yields a lower bound for the *weighted* prime sum
`Σ_{p≤x, p≡r (Q)}B(p)log p ≥ c·λ·μx/φ(Q)` for **every** `x` above the threshold, with `B≤1`. On the
good fibre, `μ≥0.99e^{−(4/3)S_res}` and `log φ(Q)≪𝓛³(log𝓛)^5`. So a *single* fibre already has
relative density `exp(−O(𝓛³(log𝓛)^5))`: the `1/φ(Q)` of the fibre is not a loss beyond the
Haar exponent, because `log Q` is itself `≪𝓛³(log𝓛)^5` (the quarantine is cheap; the expensive
part `𝓛·S_res` is the *junta*, which enters only the x-threshold `log Z`). The two points to check
are (i) the exceptional-zero factor λ in Case A, and (ii) the auxiliary prime `ℓ_aux`, which
must be dropped (its only role was `p>T`), because a Siegel character of conductor divisible by
`ℓ_aux` would cost `ℓ_aux^{−1/2}`, i.e. `exp(−𝓛^4)`.

## 1. The quantitative transfer on a coset

**Lemma 1.1 (quantitative linear transfer; PROVED modulo (G)).** Let `8|Q`, r a unit mod Q that is
a square mod every odd prime of Q with `r≡1 (8)`, `H:={n≡1 (Q)}`, and let `B=Σ_i c_i1[n≡b_i (d_i)]`
satisfy the hypotheses of O13 I3 (O11 Lemma 3.1 on the coset `rH`): cells consistent with r,
`gcd(b_i,d_i)=1`, `μ:=E_{rH}B>0`, `A:=E_{rH}|B|/μ≤Z^{1/4}`, `Z:=Q·max d_i`, twist condition
`|E_{rH}[Bψ]|≤μ/4` for real primitive ψ of conductor `f>1`, `gcd(f,Q)=1`, `f|d_i` for some i.
If `log x ≥ C_2(1+log A)log Z` (`C_2` as in O9 Thm 1.1), then

```
S_r(x) := Σ_{p≤x, p∤QD, p≡r (Q)} B(p)log p  ≥  λ_Q · μx/(3φ(Q)),
λ_Q := min(1, c_P·Q^{−1/2}(log 3Q)^{−2}),
```

with `c_P>0` the absolute effective constant of the Page bound `1−β≥c'q^{−1/2}(log q)^{−2}`.

*Proof.* This is the proof of O9 Thm 1.1 (with the O11 Lemma 3.1 / O13 I3 changes), read
quantitatively; nothing in it uses a specific x, only `log x≥C_2(1+log A)log Z`. Its three cases
end with:
* *Case 0 (no exceptional zero for `q≤Q_G`)*: `S_r(x) ≥ μx/φ(Q)·(1−1/400−1/200)`.
* *Case B (exceptional χ_1, the χ with `χ*=χ_1` has nontrivial `f_2`-part)*:
  `S_r(x) ≥ μx/φ(Q)·(1−1/2−1/100−1/400) ≥ μx/(3φ(Q))`.
* *Case A (χ_1 trivial on H, so `q_1|Q`)*: `S_r(x) ≥ 0.98·λμx/φ(Q)` with
  `λ=1−x^{β_1−1}/β_1 ≥ min(u,1)/2`, `u=(1−β_1)log x`. Since `q_1|Q`, `q_1≤Q`, and the Page bound
  with `log x≥16` gives `u≥16c'Q^{−1/2}(log 3Q)^{−2}`, so `0.98λ ≥ λ_Q/3` for suitable `c_P`.
  (O9 used `q_1≤Z`; `q_1|Q` is what I3's Case A gives: χ trivial on H is induced from mod Q.)
  The R_1 bound of Case A needs `x ≥ 200AZ³/λ`, implied by `x≥Z^5` (`λ≫Z^{−1/2}(log Z)^{−2}`),
  as in O9.
In the coset version `c(χ)=μ/φ(Q)` in Case A because `χ(r)=1` for real χ mod Q (O13 I3). ∎

*Remark.* In Case 0/B the loss is a constant; λ_Q is only the price of a possible Landau–Siegel
zero whose conductor divides Q. With Siegel's (ineffective) bound one gets
`λ_Q≥c(ε)Q^{−ε}` instead.

## 2. The lower tail from a single fibre

**Theorem 2.1 (lower tail; PROVED modulo (G), NT, OMEGA10 Thm 3.4 — the inputs of O13 Thm 5.1).**
There are absolute effective constants `C, T_0` such that for all `T≥T_0` and all `x` with
`log x ≥ C·𝓛^4 log𝓛`,

```
#{p≤x prime, p Mordell-hard (p a square mod 840) : W(p)>T}  ≥  π(x)·exp(−C·𝓛³(log𝓛)^5).
```

In particular this holds uniformly for `𝓛 ≤ c(log x/log log x)^{1/4}`.

*Proof.* Fix the good realisation `(Q,r)` of O13 Thm 3.4 and build B on the fibre `rH` exactly as
in O13 §5: I1(a) (BRW minorant, EL), I1(b) (twist), I2 (junta), I3 (coset transfer hypotheses),
**but without the auxiliary prime** `ℓ_aux`: we work with `(Q,r)` itself. I3's hypotheses are
stated for `(Q,r)` and hold there (r square mod every odd prime of Q, `r≡1 (8)`, cells consistent
with r); `ℓ_aux` entered O13 Thm 5.1 only to force `p>ℓ_aux>T` (distinctness as `T→∞`), and no
atom, cell, twist prime or coordinate refers to it (O11 Thm 3.2: "it exceeds T, so no event uses
it"; the twist prime `ℓ_0|f` is a coordinate `≤T`). The ledger of O13 Thm 5.1 then reads
(realised values of a good realisation, `≤4×` their expectations):

* `log Q ≤ C𝓛³(log𝓛)^5`, `S_res ≤ C𝓛³log𝓛`;
* `μ=E_{rH}B ≥ 0.99δ ≥ 0.99e^{−(4/3)S_res}` and `A≤1.03` (I1(a), O9 Lemma 2.1);
* `log Z ≤ log Q + log max d_i ≤ log Q + 2τ+3𝓛 ≤ C_3𝓛^4log𝓛` (I2).

Take `C ≥ C_2(1+log1.03)C_3`. Lemma 1.1 applies for every such x. Since B is a BRW minorant,
`B = 1−Σ_iA_i(1−v_i)² ≤ 1` and `B≤F` pointwise (O8 Lemma 3.1), and on `rH` property (I) gives
`F(n)=1 ⇒ W(n)>T` (O13 §5, I3). Hence, for `p≤x`, `p≡r (Q)`, `p∤QD`: `B(p)>0 ⇒ W(p)>T`, and

```
log x · #{p≤x: p≡r (Q), W(p)>T} ≥ Σ_{p: B(p)>0} B(p)log p ≥ S_r(x) ≥ λ_Q μx/(3φ(Q)).
```

Now `log(1/λ_Q) ≤ (1/2)log Q+2loglog 3Q+O(1)`, `log φ(Q)≤log Q`, `log(1/μ)≤(4/3)S_res+0.02`, and
`x/log x ≥ π(x)/1.26`. All losses are `≪𝓛³(log𝓛)^5`. Every such p is ≡ r (mod 840), a square,
so Mordell-hard. ∎

**Corollary 2.2 (the tail exponent is 3 over primes; PROVED modulo the inputs of Thm 2.1 and of
CU Thm 2.1).** There are absolute constants `c,C>0` such that, uniformly for `T≥T_0` and
`log T ≤ c(log x/log log x)^{1/4}`,

```
c(log T)³  ≤  log( π(x)/N(x,T) )  ≤  C(log T)³(log log T)³·log log log T.
```

So `log log(π(x)/N(x,T)) = (3+o(1))log log T` in this range: the Haar exponent 3 (O13 Thm 3.4 with
POINTWISE_HAAR Thm 2.1) is the true tail exponent of W over primes. The upper-tail constant c is
not effective (CU Thm 2.1); the lower-tail constant C is.

*Proof.* Lower inequality: CU Thm 2.1 (its range `log T≤c₁(log x)^{1/4}` contains ours).
Upper inequality: Thm 3.3 (Thm 2.1 gives the exponent `(log log T)^5` with a one-fibre proof), since `𝓛≤c(log x/loglog x)^{1/4}` with c small gives
`C𝓛^4log𝓛 ≤ log x` (use `log𝓛≤loglog x`). ∎

*Range bookkeeping.* The two ranges differ only by the factor `(log log x)^{1/4}`. The lower
range is the x-threshold `log x ≍ log Z ≍ 𝓛·S_res ≍ 𝓛^4log𝓛` of the transfer, i.e. the *same*
threshold as O13 Thm 5.1 (existence of one p): counting costs nothing in range. By O14 Thm 4.5
this threshold cannot be lowered below `𝓛^4/log𝓛` (level of the minorant) within the Haar-minorant + Gallagher-transfer
architecture, so `(log x)^{1/4}` is also the natural range limit here (Assessment).

## 3. Summing over the quarantine outcomes: a smaller log power

Thm 2.1 pays `log φ(Q)≪𝓛³(log𝓛)^5` for the fibre. Summing over **all** outcomes of the square-class
process replaces this by `k·log2`, k the number of primes stepped at level 0, and the Siegel factor
by `(1/2)log q_1 ≤ (1/2)k log Y`. Fix a deterministic tie-breaking rule for the process (e.g. step
the least eligible ℓ, one step at a time); O13 Lemma 3.2 is stated for any such adapted rule.

**Lemma 3.1 (leaf calculus; PROVED).** The process is a finite decision tree. Its leaves
`L=(Q_L,r_L)` give pairwise disjoint fibres `{n≡r_L (Q_L)}` of `Ẑ^×`, and

```
P_proc(L) = 4·2^{k_L}/φ(Q_L),     k_L := ω(Q_L)−1  (number of odd primes of Q_L).
```

*Proof.* Each step reveals one more digit of n, chosen by a rule depending only on the revealed
digits; two distinct leaves first differ at a node where they take different values of the same
digit, so their fibres are disjoint. The number of steps is `≤Σ_{ℓ≤Y}f_ℓ<∞`. Probabilities: the
start (`Q=8`, `r≡1 (8)`) has process probability 1 and Haar mass `1/φ(8)=1/4`. A step `(ℓ,0)` picks
one of the `(ℓ−1)/2` squares mod ℓ (prob `2/(ℓ−1)`) where Haar gives the subfibre conditional mass
`1/(ℓ−1)`; a step `(ℓ,a≥1)` picks one of ℓ lifts (all squares: ℓ odd, Hensel), conditional Haar mass
`1/ℓ`. The forced steps at 3, 5, 7 are `a=0` steps (mod 3 the unique square 1 has prob `1=2/(3−1)`).
Multiply along the path: `P_proc(L)=2^{k_L}·Haar(L)/(1/4)`, `Haar(L)=1/φ(Q_L)`. ∎

**Lemma 3.2 (number of level-0 steps; PROVED modulo NT).** With O13's parameters
(`β=1+1/log𝓛`, `η=(3/4)logβ`, `Y=𝓛^{C_0+4}`),

```
E[k] ≤ 3 + (1/η)·Σ_E P_H(E)2^{ω_Y(M)}β^{ω(M)}ω_Y(M)  ≪  𝓛³(log𝓛)²log log𝓛.
```

*Proof.* First inequality: O13 Lemma 3.2(b) with `logℓ` replaced by 1 and only `a=0`:
`1[τ_{ℓ,0}<∞] ≤ η^{−1}w̃_{ℓ,0}(τ)1[τ<∞] ≤ η^{−1}G^{(ℓ,0)}_τ1[τ<∞]`, optional stopping gives
`E[·]≤G^{(ℓ,0)}_0=Σ_{ℓ|M}P_H(E)2^{ω_Y}β^{ω}`, and `Σ_{ℓ≤Y}1[ℓ|M]=ω_Y(M)`; the forced steps add 3.
Second: put `t:=1+1/loglogY`. Since `y≤t^y/(e·log t)` for `y≥0`,
`ω_Y(M) ≤ (loglogY+1)·t^{ω_Y(M)}/e`. Summing over D as in O13 (notation `w(M)`), it suffices that
`Σ_{M≤T, M≡3(4)} w(M)t^{ω_Y(M)}/M ≪ 𝓛³logY`. This is O13 Lemma 3.3(A)'s first display with `f_2`
replaced by `f_2·t^{ω_Y}`: still multiplicative with `f_2(p^k)≤2tβ·(3/2)≤8^k` for large T (NT class, uniform in T), and
the Euler-product bound for `Σf_2t^{ω_Y}(n)/n` exceeds that for `Σf_2(n)/n` by at most `∏_{p≤Y}(1+2β(t−1)/(p−1)) ≤ exp(2β(t−1)(loglogY+O(1)))=O(1)`.
Hence `E[k] ≪ η^{−1}·loglogY·𝓛³logY ≍ 𝓛³(log𝓛)²log log𝓛` (`logY≍log𝓛`). ∎

**Theorem 3.3 (lower tail, smaller log power; PROVED modulo (G), NT, OMEGA10 Thm 3.4).** There are
absolute effective `C, T_0` such that for `T≥T_0` and `log x≥C𝓛^4log𝓛`,

```
N(x,T) ≥ #{p≤x Mordell-hard: W(p)>T} ≥ π(x)·exp(−C𝓛³(log𝓛)³loglog𝓛).
```

If no character of conductor `≤x` has a Landau–Siegel zero in the sense of (G) (e.g. under GRH for
real characters; CONDITIONAL), the bound improves to `π(x)exp(−C𝓛³(log𝓛)²loglog𝓛)`.

*Proof.* Call a leaf L *good* if (i) every `ℓ>Y` has `w̃_ℓ(L)≤η`; (ii) `log Q_L≤8E[log Q_end]`;
(iii) `S_res(L)≤8E[S_res]`; (iv) `k_L≤8E[k]`. By O13 Lemma 3.2(d)+3.3(B) (as in O13 Thm 3.4),
`P(not (i))≤1/4`; by Markov each of (ii)–(iv) fails with probability `≤1/8`. So
`P_proc(good)≥3/8`. Every good leaf satisfies the hypotheses used in Thm 2.1's proof, with the
ledger constants at most doubled: (1.1) at all coordinates, no deterministic event (O13 Lemma 3.1),
`S_res≪𝓛³log𝓛`, `log Q_L≪𝓛³(log𝓛)^5`, hence `log Z_L≤C_3𝓛^4log𝓛` with one absolute `C_3` for all
good leaves. So for `log x≥C𝓛^4log𝓛` Lemma 1.1 applies to every good leaf at the same x.

*Refined Siegel factor.* In Case A for leaf L, `q_1|Q_L`; a real primitive conductor is
`2^e·(odd squarefree)` with `e≤3`, so `q_1 ≤ 8∏_{ℓ|Q_L odd}ℓ ≤ 8Y^{k_L}` and Lemma 1.1's proof gives
`λ_L ≥ min(1, c_P q_1^{−1/2}(log 3q_1)^{−2}) ≥ exp(−(1/2)k_L logY − O(log(k_L logY)+1))`.

*Summation.* The fibres of distinct leaves are disjoint (Lemma 3.1), so the prime counts add:

```
N(x,T) ≥ Σ_{L good} #{p≤x: p≡r_L (Q_L), W(p)>T}
       ≥ (x/(3log x))·Σ_{L good} λ_Lμ_L/φ(Q_L)
       = (x/(12log x))·Σ_{L good} P_proc(L)·2^{−k_L}λ_Lμ_L
       ≥ (x/(12log x))·(3/8)·min_{L good} 2^{−k_L}λ_Lμ_L.
```

On good leaves: `k_L log2 ≤ 8log2·E[k] ≪ 𝓛³(log𝓛)²loglog𝓛` (Lemma 3.2);
`log(1/μ_L) ≤ (4/3)·8E[S_res]+0.02 ≪ 𝓛³log𝓛`; `log(1/λ_L) ≤ (1/2)·8E[k]logY+O(log𝓛)
≪ 𝓛³(log𝓛)³loglog𝓛` (`logY≍log𝓛`). Without an exceptional zero, Case A does not occur and
`λ_L≥1/3`-type constants replace `λ_L` (Lemma 1.1, Cases 0/B). ∎

*Where the logs go (Assessment).* Thm 3.3's three losses are (a) the square-class restriction
`2^{−k}` (the Haar price of never firing an atom, O13 Lemma 3.1), (b) the residual mass `S_res`,
and (c) the Siegel factor. (b) is `≍` the Haar truth `𝓛³` up to `log𝓛`; (a) comes from Lemma 3.2's
`1/η≍log𝓛` and the `2^{ω_Y}` drift weight. Only (c) is new relative to the Haar bound, and it is
the familiar asymmetry of CU Remark 2.2: majorants absorb `1+ε≤3`, minorants pay `1−ε`. Siegel's
(ineffective) theorem gives `λ_L≥c(ε)q_1^{−ε}`, which still costs `ε·k_LlogY`, so it does not remove
the third log; restricting to leaves with `q_1∤Q_L` would, if those carry a fixed proportion of the
good mass (not shown).

## 4. Status (checkpoint 1)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | quantitative coset transfer: `S_r(x) ≥ λ_Qμx/(3φ(Q))`, `λ_Q≥min(1,c_PQ^{−1/2}(log3Q)^{−2})`, for all `log x≥C_2(1+logA)logZ` | PROVED mod (G) (proof of O9 Thm 1.1 read quantitatively) |
| Thm 2.1 | `#{p≤x hard: W(p)>T} ≥ π(x)e^{−C𝓛³(log𝓛)^5}` for `log x≥C𝓛^4log𝓛` (one fibre, no `ℓ_aux`) | PROVED mod (G), NT, OMEGA10 Thm 3.4 |
| Lemma 3.1 | leaves of the square-class process: disjoint fibres, `P_proc(L)=4·2^{k_L}/φ(Q_L)` | PROVED (elementary) |
| Lemma 3.2 | `E[k]≪𝓛³(log𝓛)²loglog𝓛` | PROVED mod NT |
| Thm 3.3 | `N(x,T) ≥ π(x)e^{−C𝓛³(log𝓛)³loglog𝓛}`, same range; `(log𝓛)²loglog𝓛` without exceptional zero | PROVED mod (G), NT, OMEGA10 Thm 3.4; improved form CONDITIONAL (no Siegel zero) |
| Cor 2.2 | `c𝓛³ ≤ log(π(x)/N(x,T)) ≤ C𝓛³(log𝓛)³loglog𝓛` for `𝓛≤c(log x/loglog x)^{1/4}`: tail exponent 3 | PROVED mod the above and CU Thm 2.1's inputs |

*Open.* (1) Range: close the `(log log x)^{1/4}` gap between the two sides (it is the `log𝓛` of the
junta `𝓛·S_res`; O14 suggests `𝓛^4/log𝓛` is the architectural floor). (2) The third log (Siegel
factor, §3 Assessment). (3) A lower bound in the range `𝓛^4 ≫ log x` (beyond `(log x)^{1/4}`) is out of
reach of the transfer architecture (O14 Thm 4.5); there even existence of one p is open.

## Replay

No computations: all items are proofs. The cited inputs are replayed by `verify.py` blocks (cz)–(df)
(O13 Lemma 3.1 Jacobi check, β-weighted LLL) and (cu)–(cy) (O9).
