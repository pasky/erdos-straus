# AGENT REPORT O76 — two-sided tail of the witness modulus over primes

Branch `side-agent/two-sided-tail`. Not merged into main. Document: `POINTWISE_TAIL.md` (new).
No scripts: everything is proof.

## Result

**Cor 2.2.** Uniformly for `T≥T_0` and `log T ≤ c(log x/loglog x)^{1/4}`,

```
c(log T)³ ≤ log(π(x)/#{p≤x: W(p)>T}) ≤ C(log T)³(loglog T)³·logloglog T.
```

The lower inequality is CU Thm 2.1. The upper one is new (Thm 2.1 / Thm 3.3). So the Haar exponent 3
is the true tail exponent of W over primes, in the range of the transfer. The lower-tail constant is
effective. The primes counted are Mordell-hard.

## How

* **Lemma 1.1.** O9 Thm 1.1 (on the coset, via O11 Lemma 3.1 / O13 I3) read quantitatively. For
  *every* x with `log x ≥ C_2(1+log A)log Z` it gives `Σ_{p≡r(Q)}B(p)log p ≥ λ_Qμx/(3φ(Q))`. The
  only non-constant loss is the Case A Siegel factor. There `q_1|Q`, so the Page bound gives
  `λ_Q ≫ Q^{−1/2}(log Q)^{−2}`.
* **Thm 2.1 (one fibre).** Take O13's good realisation and **drop `ℓ_aux`**. Its only role was
  `p>T`; a Siegel conductor dividing `ℓ_aux` would cost `exp(−𝓛^4)`. Since `B≤F≤1`, the count is
  at least `S_r(x)/log x`. All losses (`log φ(Q)`, `S_res`, `log(1/λ_Q)`) are `≪𝓛³(log𝓛)^5`,
  because O13's quarantine is cheap. The expensive junta `𝓛·S_res` enters only the x-threshold.
  So the brief's "turn one fibre into a count over all fibres" is *not needed* for a bound of the
  form `exp(−C𝓛³(log𝓛)^B)`. One fibre already gives B = 5.
* **Thm 3.3 (all fibres).** Sum over the leaves of the square-class decision tree. The leaves are
  disjoint, and `P_proc(L)=4·2^{k_L}/φ(Q_L)` (Lemma 3.1). Since `E[k]≪𝓛³(log𝓛)²loglog𝓛`
  (Lemma 3.2, NT with a `t^{ω_Y}` twist), the `log φ(Q)` loss is replaced by `k log 2`. For the
  Siegel factor, `q_1≤8Y^{k}`. This gives B = 3+o(1), or 2+o(1) if there is no exceptional zero
  (CONDITIONAL).

## Self-review

There was one deep reviewer pass (gpt-6-astra). Its verdict was "core results appear sound modulo
the stated inputs". I applied four fixes:
* the architectural-floor citation is now CU Prop 4.2, not O14 Thm 4.5;
* the case where the exceptional character lies outside B's support is now written out;
* the NT-class justification is completed;
* the threshold is worded as sufficient, not `≍`.

## For the hostile review, check especially

1. Lemma 1.1's Case A uses `q_1|Q` (O11 Lemma 3.1: f_2=1 ⇒ χ induced mod Q), and `R_1` is absorbed
   for `x≥Z^5`.
2. Dropping `ℓ_aux` from O13 Thm 5.1 changes no hypothesis of I1–I3.
3. Lemma 3.2's optional-stopping bound for `k` (O13 Lemma 3.2(b) with weight 1 at `a=0`) and the NT
   modification.
4. Thm 3.3: good-leaf probability ≥ 3/8. The same x works for all good leaves.

## Proposed ledger entry (H)-section

`#{p≤x hard: W(p)>T} ≥ π(x)exp(−C(log T)³(loglog T)³logloglog T)` for `log x ≥ C(log T)^4 loglog T`
(POINTWISE_TAIL Thm 3.3; one-fibre version `(loglog T)^5`, Thm 2.1). PROVED modulo (G), NT and
OMEGA10 Thm 3.4. With CU Thm 2.1, the log-tail is `≍(log T)³` up to `(loglog T)^{3+o(1)}`
(Cor 2.2).

## Open

* The `(loglog x)^{1/4}` range gap between the two sides comes from the junta's `log𝓛`. CU Prop 4.2's
  floor is `𝓛^4`.
* The third log comes from the Siegel factor. It would go if leaves with `q_1∤Q_L` carried a fixed
  share of the mass; this would need a uniform NT bound in progressions mod ℓ.
