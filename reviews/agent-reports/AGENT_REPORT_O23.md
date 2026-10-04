# AGENT REPORT O23 — HC_Π (large-m divisor part of HC*)

Branch `side-agent/omega-hcpi`. Deliverables: `POINTWISE_OMEGA6.md`,
`scripts/omega6_corner.py`, `data/omega6/corner_1e9.txt`, `corner_1e11.txt`.

## Outcome: partial. HC_Π is NOT proved. The residual is sharpened and stated exactly.

The rate `log W(p) ≥ c(log₂p)^{3/2}` is still **not** established. The
proved rate is still O4 Cor 3.1. Nothing is claimed for ES.

## What is PROVED (modulo Shiu 1980 Thm 1, Henriot 2012 Thm 4, O5 Prop 7.1)

1. **Three-fibre reduction (Thm 1.5).** Every atom lies in three
   progressions: over `(a,b,m)` (s steps mod qm), over `(s,a,m)` and over
   `(s,b,m)`. Non-first elements are paid for by period sums. So
   `Σ^{>μ} ≤ (1+𝓛/2)(D_ab+D_sa+D_sb) + 𝒦`. Here `𝒦` sums over *corner
   atoms*, which are first in all three fibres, and Lemma 1.4 gives
   `s,a,b≤2qm` for them.
2. **(s,a)-plane divisor sum (Prop 2.1)**, the τ_Π(4sa²+1) average the
   brief asked for:
   `D_sa=Σ_{4sa²≡κ (q)}τ(4sa²+1)/(sa) ≪ 4^k𝓛⁴(H^{−1/2}+q^{−1/4})`,
   with absolute constants. There are three regimes:
   * Shiu in s (linear form `4a²s+1` mod `4a²q`);
   * Henriot Thm 4 in a (`P(X)=4s(r+qX)²+1`; content exactly
     `gcd(κ+1,q)`, `Δ_D=1`, `x≥c_0‖P‖^{1/4}`);
   * a short regime. There, Nicolas–Robin plus the O5 squarefree
     injectivity gives a `q^{−3/8}` saving, or a single pair with
     `sa>H`.

   With O5 Prop 7.1, all period parts are done for **all m>1**, with
   exponent 1/4 (Cor 2.2).
3. **Shallow corner (Lemma 3.1) and Thm 3.2.** Corner atoms with
   `min(4sa,4sb,4ab)≤yH^{1/4−a}` are absorbed. Hence HC_Π(a), for
   `a≤1/4`, follows from one first-term bound:
   **(FT_a)** `Σ_{4sa²≡κ, 4sa>yH^{1/4−a}} Σ_{m|4sa²+1, m>H^{1/3−a}} 2/ν(s,a,m) ≪ e^{Ck}𝓛^BH^{−a}`,
   where ν is the least `ν≥y` with `qmν≡−1 (mod 4sa)`, s is squarefree,
   and only fibres with `ν≤T/(qm)` count (review D7).

   Lemma 3.3: `ν≡−q^{−1}·(4sa²+1)/m (mod 4sa)`, and each class mod 4sa
   holds at most 2 divisors of `4sa²+1`.
4. **Long-plane boxes (Prop 3.4, Cor 3.5).** Boxes in which a plane is in
   the Shiu/Henriot range and the third side is `≥μ_0W`
   (`W=C4^k𝓛²H^a`) are done. With three long planes, HC_Π holds for
   `m<(qy/32)^{1/2}W^{−3/2}` (about `y^{3/2}H^{−3a/2}`). **Scope:** this
   holds only for `q≲T^{3/10}`, i.e. `|O|≲0.3(k+1)`. For `q≥T^{1/2}` the
   (a,b)-plane is never long, and the m-range proved without residual is
   still O5's `H^{1/3−a}` (review D5).

## Exact residual (open; split per review D5/D6)

Corner atoms with `4sa>yH^{1/4−a}` lying in boxes where every plane is
short or has its third side `<μ_0W`. These are:

* **(a)** three long planes: `m≥(qy/32)^{1/2}W^{−3/2}` with `s,a,b<2mW`.
  This exists only for `q≲T^{3/10}`.
* **(b1)** a short s-plane. Numbers are `≤q^{O(1)}`, no averaging
  theorem applies, and the pointwise `τ` bound is too weak when
  `log q≫k log k`.
* **(b2) the main residual.** Only the (a,b)-plane is short. `a,b<2mW`,
  s is large, Shiu/Henriot do apply, and **m is unrestricted**. This is
  the hub-like / unbalanced-ray family of O5 (DIV), and the numerical
  corner mass sits here.

Equivalently, the missing input is the distribution, on average over
the thin family `4sa²≡κ (q)`, of `q^{−1}·(divisors of 4sa²+1)` mod `4sa`
near the class of small ν. Shiu and Henriot count divisors but do not
locate them mod 4sa.

## EVIDENCE

Exact enumeration, two pairs (T=10⁹ and 10¹¹). At high hub height the
m>1 mass is almost entirely corner mass, so the residual is the real
one. It is about `τ(F)log(4sa/y)/(4sa)`, the average size, not the
worst case `τ(F)/y`. It stays well below `X^{−1/4}` (§4 table).

## For the reviewer: points to check hardest

* Prop 2.1 Regime II: the Henriot hypotheses. Check primitivity after
  dividing by `g_0`, `Δ_D=1` (incl. prime-power `q′`), the `‖P‖`
  condition, and the interval-splitting.
* Prop 2.1 Regime I: coprimality of `r_1` and `k_1` via the valuation
  argument. Check `k_1<y_1^{3/4}`.
* Thm 1.5: the fibres contain pseudo-atoms (true Π-part a multiple of
  m). Check that the charging is still an upper bound.
* Lemma 3.1 / Thm 3.2: one first element per fibre, and the bound
  `2/y≤Z/(2sa)`.
* Cor 3.5: the deduction of the m-threshold. Its k-dependence is
  `(C4^k𝓛²)^{−3/2}`, which is negligible only in the Thm 4.2 regime.

## Status labels used

PROVED (modulo the cited theorems): Lemmas 1.1–1.4, Thm 1.5, Prop 2.1,
Cor 2.2, Lemma 3.1, Thm 3.2, Lemma 3.3, Prop 3.4, Cor 3.5.
Assessment: residual (b) commentary and the equidistribution diagnosis.
EVIDENCE: §4. Open: HC_Π, HC*, the `(log₂p)^{3/2}` rate.

Stopping here for parent review.

## Round 1 review (`side-agent/review-omega6`): applied

* Core CONFIRMED.
* D1: Shiu α=1/4.
* D2: s squarefree in `D_sa`, `D_sb`, FT.
* D3: `𝓛³` in `P_1`.
* D4: "implied by", not "equivalent".
* D5: the q-range `q≲T^{3/10}` for the m-threshold.
* D6: residual split into (a)/(b1)/(b2), with (b2) as the main residual.
* D7: FT restricted to `ν≤T/(qm)` and squarefree s; §4 measures `𝒦`.
* D8: the `q^{−3/8}` aside holds only for `32SA²≥q`.
* D9: §4 wording.
* Nits: Prop 2.1 hypotheses, the Regime II split, the worst-case formula.
