# AGENT REPORT O45 (branch side-agent/homega): H_ω and exponent 1/5

Deliverable: `POINTWISE_OMEGA12.md`, `scripts/omega12_blocks.py`,
`data/omega12/blocks_1e{4,5,6}.txt`. Not merged into main.

## Results

1. **H_ω(2) PROVED modulo ET (Theorem 5.1).** `Ω_0=Σ_{atoms}(g/M)h(M)≪𝓛^4log𝓛`,
   so `Ω♯=C loglogT·Ω_0≪𝓛^4(log𝓛)²`. Inputs: Elsholtz–Tao Prop 1.4,
   Thm 7.1, Cor 7.4 and (7.10). All four are proved in ET; nothing new is assumed.
   * *Reduction (Lemma 2.1).* Use Type I coordinates `(a,c,d,f)`:
     `P=4a²d+1=ef`, `e=g`, `N=M/e=4acd−f≥acd`, `g/M=1/N`. Then
     `h(M)≤h(e)+h(N)`, which loses 2% numerically.
   * *Rough part `Σh(N)/N` (Lemma 3.1).* This is the step O11 §4 could not do.
     In the dyadic block `c∈[C,2C)`, sum along the c-progression only the
     prime powers `q≤C`; these have full periods, so there are no first terms.
     Pay the prime powers `q>C` pointwise with `Σ_{q|N,q>C}1/i≤log N/log C`
     (Lemma 1.1(c)). ET Prop 1.4 gives every c-scale the same mass
     (`≪log(A+B)`), so the cost `𝓛/log C` averages over the `≍𝓛` scales to
     `log𝓛`. Only ET Prop 1.4 is used here.
   * *Smooth part `Σh(e)/N` (Lemma 4.1).* `Σ_{e|P}h(e)=Σ_{q|P}τ(P/q)/i`. Per
     block `(a,d)∈[A,2A)×[B,2B)`, with `Z=max(A,B)`:
     * `q>Z^{1/2}` costs O(1) per term, by Lemma 1.1(c), since `P<32Z³`;
     * `q≤Z^{1/2}` uses ET Thm 7.1 on the shifted quadratic
       `P(qa'+x_0)/q`, with root counts ≤2 including at ℓ (case `A≥B`, plus
       ET (7.10) in its own range);
     * or ET Cor 7.4 on the linear `P(qd'+d_0)/q` (case `B>A`).
     The block total is `≪log Z·loglog Z`.
2. **Exponent 1/5 (Theorem 6.1, PROVED modulo (G), ET, OMEGA10 Thm 3.4).**
   O11 Cor 4.1 with B=2 gives `W(p)≥exp(c(log p)^{1/5}(loglog p)^{−2/5})` i.o.
3. **Sharper: `(loglog p)^{−1/5}` (Lemma 6.2, Theorem 6.3, same label).**
   Start O11 Lemma 2.2 with `a_ℓ=1` for all odd `ℓ≤𝓛`, at cost `≤1.02𝓛+7`.
   The unramified Euler factor is then `≤e³`, so `s_1=e³g/M` and `S_1≪𝓛^4`.
   This gives:
   * `log Q≪𝓛^5log𝓛` and junta `≪𝓛^5`;
   * `W(p)≥exp(c(log p)^{1/5}(log log p)^{−1/5})` i.o.;
   * `log(1/δ*)≪𝓛^5log𝓛`.

   The remaining `log𝓛` is `Ω_0`'s. Numerically the weighted mean of h grows
   like `loglog T`, so we conjecture that `Ω_0≍𝓛^4log𝓛` (CONJECTURE).
4. **EVIDENCE/checks.** `omega12_blocks.py` asserts the Lemma 2.1 identities,
   subadditivity and the pointwise large-q bound on all atoms with `D≤A`
   (7.78M atoms at `T=10^6`). Mean h is `2.16/2.40/2.62` at
   `T=10^{4,5,6}`. The Lemma 4.1 block ratio is bounded (max 1.29, the same small
   block at every T).

## Self-review

One fresh-subagent review (deep): no fatal or repairable proof errors. It
checked the ET hypotheses against the PDF (coefficients, ρ bounds, the
(7.10) range) and Lemma 6.2's compatibility with O11. Fixed:
* an invalid "mean ≪ log𝓛" claim (it divided two upper bounds);
* a residual-log assessment that overreached, now CONJECTURE;
* a numerical diagnostic, now labelled heuristic;
* cosmetics.

## For the parent

* Suggested ledger entry: (H)23, "H_ω(2) PROVED mod ET; exponent 1/5 up to
  `(loglog p)^{1/5}` PROVED mod (G), ET, OMEGA10 Thm 3.4".
* Suggested hostile-review focus:
  * Lemma 4.1's use of ET Thm 7.1, whose constant must depend only on
    (D,l,C)=(2,5,2);
  * the uniformity of Lemma 3.1's sum over scales;
  * Lemma 6.2's interface with O11 Thm 3.2 (twist prime, Cor 1.2's S).
