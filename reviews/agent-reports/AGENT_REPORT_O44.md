# AGENT REPORT O44 (branch side-agent/quarantine-bound): shrinking `log Q_Π`

Deliverable: `POINTWISE_OMEGA11.md`, `scripts/omega11_{filtration,graded,hmoment}.py`,
`data/omega11/`. The branch also merges `side-agent/esw-suppression`
(OMEGA10 including Thm 3.4).

## Results

1. **Remark 4.3's hypothesis, checked (§1).**
   * *Literally unavailable (Assessment, not proved).* If free primes
     `ℓ∈(z,√T]` occur in surviving events to top powers, and some events
     contain many of them, then `ρ≍k` and the bound gives back `𝓛^6`. Neither
     premise is proved; self-review R44a downgraded the original claim.
   * *Its conclusion holds anyway, with ρ=2 (Lemma 1.1, Cor 1.2, PROVED from
     OMEGA10 Thm 3.4).* Write each coordinate in base-ℓ digits. Weight the
     ℓ-part of an Efron–Stein component by `λ^{(top digit)+1}`, a filtration
     rather than a product weight. The weighted energy is a sum over level
     selections of `‖L_VF‖²` with tail-block coordinates. OMEGA10 Lemma 3.1
     then applies with the hypergraph `Ê={(ℓ,j): j<v_ℓ(E)}`, and Thm 3.4
     applies with edge weight `≤∏λ_ℓ^{2v_ℓ}`. ES events have
     `∏ℓ^{v_ℓ}≤M≤T`, so this gives `G'≤1` for `λ_ℓ=2^{logℓ/(2𝓛)}`.
     Conditioned systems `F^{(j)}` are covered (Remark (ii)), and no
     single-value splitting is needed.
   * *Consequence:* the junta modulus is `≪𝓛(S+𝓛)≪𝓛^5log𝓛` (ET),
     independent of z and k.
   * *Check:* exact digit-level Efron–Stein on 600 random systems gives max
     `G'=0.9972`. ρ=1 also survives numerically; that is not claimed.
2. **Graded quarantine (§2, Lemma 2.1–2.2, PROVED).**
   * *What changes.* Quarantine ℓ only to `n≡1 (ℓ^{a_ℓ})`. The coordinate
     is then the fibre of `n mod ℓ^{f_ℓ}` over 1. Raise `a_ℓ` by one while
     the fibre mass exceeds `θ=c(a_ℓ+1)logℓ/𝓛`.
   * *Why the local lemma survives.* It needs only `Σ_{ℓ∈supp E}w_ℓ≤c` per
     event, and that follows from `Σ v_ℓ(M)logℓ≤𝓛`. So **no `Π_0={ℓ≤z}` and
     no width k are needed.**
   * *Uniform weights.* O2 Lemma 11.1's mass bound holds for every graded Q,
     and (I) still holds.
   * *Cost.* Each step costs `logℓ` and is charged at ratio `𝓛/(c(a+1))`, so
     `log Q ≤ 9+(𝓛/c)Σ_{atoms}s·h(M)`, with `h(M)=Σ_{ℓ|M}H_{v_ℓ(M)}≤log₂τ(M)`.
     This gives `log Q ≤ 9+(1+o(1))𝓛²S♯/(c log𝓛) ≪ 𝓛^6` under ET. Before:
     `(π(z)+64k²S*)𝓛≪𝓛^7/log𝓛`.
3. **Exponent 1/6 (Thm 3.2).** `W(p)≥exp(c(log p)^{1/6})` for infinitely
   many Mordell-hard p. This is PROVED modulo (G), ET Prop 1.4 and OMEGA10
   Thm 3.4 (still under review). OMEGA10 Thm 4.2 alone, with `k≤ω(M)`, also
   suffices for 1/6.
   * It needs **Lemma 3.1**: O9 Thm 1.1 with fibre cells (`gcd(d_i,Q)>1`),
     using the Haar mean over `H={x≡1 (Q)}`.
   * The twist reduces to the part of ψ prime to Q: real primitive
     conductors have squarefree odd part, and `8|Q`.
   * On the Haar side (Cor 3.3): `log(1/δ*)≪𝓛^6`.
   * Without OMEGA10 the junta is O9's `𝓛^7` and the exponent stays 1/7.
   * Unconditionally, O9 Thm 2.3 is unchanged.
4. **Towards 1/5 (§4).**
   * *Only loss:* the worst-case charge `h(M)≤𝓛/log𝓛`.
   * **H_ω(B)** (`Ω♯=Σs·h≪𝓛^4(log𝓛)^B`) gives `log Q≪𝓛^5(log𝓛)^B`. Then
     `W≥exp(c(log p)^{1/5}(log log p)^{−max(B,1)/5})` (Cor 4.1, PROVED
     implication).
   * *EVIDENCE for B=2:* at `T=10^4,10^5,10^6` the s-weighted mean of h is
     `2.32, 2.57, 2.79`, which tracks `log log T`; the worst case is
     `𝓛/log𝓛 = 4.15, 4.71, 5.26`.
   * *What H_ω needs:* ET Prop 1.4 in progressions mod `ℓ≤T^{o(1)}` on
     average over ℓ. The obstacle is the first term of each u-progression,
     made explicit through the identity `M=m·N`, `s≍1/N`. I did not prove
     H_ω.
   * *Floor (Assessment):* under the main-term model, any graded quarantine
     costs `≳S/log S` (`𝓛^4`). This rule costs `≍S𝓛`, which balances the
     junta `𝓛S`, so ≈1/5 is the natural limit of the route.
5. **Finite-T EVIDENCE.** At `T=10^5` with the matching thresholds,
   `log Q=4054` (graded) against 8942 (O2). The Haar certificate at `c=1/8`
   is `log(1/δ*)≤764` against O2's 1479. The local-lemma quantity is
   `≤c` in all runs, up to `T=10^6`.

## Attack points for review

* Lemma 1.1: the filtration/selection identity, applying O10 Lemma 3.1 to
  tail blocks with split events, the edge-weight bound `1+λ^j(λ−1)≤λ²`, and
  Remark (ii) for `F^{(j)}`.
* Lemma 2.2's charging: each `(ℓ,a)` is stepped once. `w≤Σ_{v_ℓ(M)>a}s`
  holds uniformly over the stages. `H_v≤log₂(v+1)`.
* Lemma 3.1: Case A/B split via `χ|_H`, and `f_1|Q`.
* Thm 3.2's interfaces: O8 Lemma 3.3 with `c=1/64`, unsplit events in BRW,
  `ℓ_aux`.
* Labels: Thm 3.2 rests on OMEGA10 Thm 3.4, which is internal and under
  hostile review.

Self-review R44a (deep subagent): no FATAL; the MAJOR (overclaim in §1.1) and the minors are fixed (F^{(j)} wording, `8|Q` in Lemma 3.1, 840, distinct-event variant documented in the graded script, h-moment weight relabelled, empty-family crash).

DISCOVERIES/STATUS were not edited; the parent updates the ledger after review.
