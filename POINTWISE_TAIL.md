# The witness-modulus tail over primes: a matching lower bound (task O76)

Task O76 (branch `two-sided-tail`). Labels as in the house rules. ES is not touched: nothing below
bears on whether `W(p)<∞`. Notation: `𝓛=log T`; O9 = `POINTWISE_OMEGA9.md`, O11 =
`POINTWISE_OMEGA11.md`, O13 = `POINTWISE_OMEGA13.md`, CU = `CEILINGS_UNIFIED.md`.
`N(x,T):=#{p≤x prime: W(p)>T}`.

**Status: in progress (checkpoint 0).**

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
