# K4CHEN hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/z56-k4chen` at `7e5a1aba94af79ac9c4002b6936ff2ff06d7bb87`.
Scope: `Z56_K4CHEN.md`, its numerical scripts/data, and inherited P415 Theorem U.
**ES remains OPEN. No unconditional explicit Ω_𝒬(4p+1) ≤ 6, 8, or 10 is established.**
The model strengthening is credible; promoting its conditional numerical witness to a proved theorem needs the fix below.

## Per-claim findings

| Claim | Classification | Independent check / qualification |
|---|---|---|
| §2.1 Lemma D, exact reduction | CORRECT | After removing T₁ and repeated inert factors, bad N₂ has even j ≥ r+2; its r+1 smallest factors select either the direct or switched term. Overcounting direct terms is harmless. |
| Lemma D error E | CORRECT | Sum over all integers q ≥ x^ζ bounds the reciprocal-square part by O(x^(1−ζ)); the additive terms contribute O(√x), absorbed since ζ<1/4. N₁'s diagonal has the analogous negligible bound. |
| §2.2(i) main lower sieve | CORRECT relative to stated source inputs | Nath–Xie Prop. 3.10 permits two κ=1/2 beta sieves; the lower parameters require sᵢ≥1. Its remainder is τ(d₁d₂)^4-weighted through D^(1+ε′), not merely D. Fixed slack 0.001 accommodates ε′ and the factor 8. |
| Main-term local constant | CORRECT | For q≥7 inert, the two distinct forbidden unit residues have survival (q−3)/(q−1); dividing by (1−1/q)² gives q²(q−3)/(q−1)³. At 3 the roots coincide, giving (1/2)/(2/3)²=9/8. Use lcm(d₁,d₂) in CRT. |
| §3.1 normalisation lemma | CORRECT-WITH-FIX | Euler products give C_S=√(P/8), c_W=√(πe^(−γ)P/2), hence C_S=(A/2)c_W. The explanatory “every” sentence has an endpoint exception: y=n=9 has no inert prime below √y but is not in S. Exclude n=q²=y or use an inclusive cutoff. The asymptotic is unaffected. |
| §2.2(ii) direct estimate | CONDITIONAL / GAP if treated as proved | The 1/(2^(k−1)(k−1)!) factor and residual level θ−Σαᵢ are correct. Weighted BV and local-factor summation must actually be supplied; MT explicitly retains them. |
| §2.2(iii–iv), cap removal, MT | Honest CONDITIONAL | Minimising 2/(a√b), a+b=λ gives a=2λ/3 and L=3√3 λ^(−3/2). Cap removal is consistent at main-term level by sifting primality only below x^(a/3)<z₁; it does not prove the convolution remainder estimate. |
| §2.3 “Theorem K6” | GAP in the numerical proof as written | Taking the maximum of three mesh values is not an upper-error bound for the continuum integral. The j≥27 tail controls omitted factor counts, not mesh error. Independent bounds strongly support positivity, but the theorem label needs numerical validation or weakening. |
| §3.2 masses and tail | CORRECT as integral model; numerical EVIDENCE | Successive removal of one factor gives 1/(2j); iterating yields 1/(2^j j!). Odd j are auxiliary. Integrating the last factor gives 2 atanh√(1−ζ/H)/√H; bounding it by 2/ζ proves the stated tail bound. |
| §1 finite additive-weight LP | EVIDENCE, appropriately limited | Nonnegative weights covering every k-factor multiset suffice; repeated inert factors are negligible. Rerun confirms capped C(8) failure at the exhibited point. This is not an impossibility theorem for additive weights. |
| §§4–5 margins and level crossings | EVIDENCE, not barriers | Decisive C(6), fragile C(4), and positive C(2) witnesses reproduce below. Neither negative grids nor the tested inflation range prove universal obstructions. |
| §5.2 known beyond-BV inputs | CORRECT scope restriction | Checked Lichtman Thm 1.7: triply well-factorable weights and small varying residue. It supplies neither these arbitrary CRT residues/half-dimensional weights nor the composite switched sequences. |
| Inherited P415 U: some absolute finite Ω_𝒬 bound | CORRECT-WITH-FIX at proof-detail level | Its separate crude small-level argument does not require MT; explicitly discard p≤w before asserting primality implies survival below w. This O(w) loss is negligible. It supplies no explicit r=10 or r=6. |
| Overall “strengthened at model level + narrowed” | CORRECT | Supported by the numerical comparisons, with MT retained and K6's numerical-proof status repaired. No claim closing K(4) or ES follows. |

## Source audit: switching, weights, levels

[S1] [Nath–Xie, arXiv:2501.16723v2](https://arxiv.org/pdf/2501.16723v2), downloaded and read directly.
Theorem 1.1 really gives Ω(p+2)≤11 for p−1=m²+n², with lower bound x/log^(5/2)x.
Remark 1.1's ≤3 is conditional, not an available Chen theorem for the present shifts.
Lemma 3.2 supplies divisor-weighted BV for products of primes; Prop. 3.10, equations (3.13–14), gives exactly the vector functions used here.
The source's allowance of vanishing h(q,q) is visible in its own application; the formally positive codomain is not a substantive obstruction.
Its switching uses **Pan's Theorem 3.1**, a bounded coefficient f(m), m≤x^(1−ε), and total modulus at most √x/log^B x.
Prop. 4.2 uses two *linear* upper sieves, D₁≤z₁, D₂≤z₂, with 4D₁D₂≤√(x/2)/log^B(x/2), and explicitly averages m-dependent local factors.
This is not a ready-made theorem for the present semi-linear second sieve and ordered many-inert-factor configurations.
A largest-prime Siegel–Walfisz factor and power-sized complementary factor are useful starts, not a complete proof of MT with the required coefficients and product constraints.
The value 2.35 is not a source theorem bounding this problem's switched constants; the memo correctly calls it illustrative.

[S2] [Lichtman, arXiv:2309.08522](https://arxiv.org/pdf/2309.08522), Thm 1.7 and Definitions 1.3–1.4 checked directly.
The 66/107 statement uses triply well-factorable weights and |a|<x^ε; Cor. 1.5 is the fixed-residue version.
Its introduction records BFI's 4/7 and Maynard's 3/5 with their respective factorability restrictions.
None authorises replacing BV by 66/107 in the memo's sieve; the stated hypothetical ledger is honest.

[S3] [Ford, Sieve Methods notes (2023)](https://ford126.web.illinois.edu/sieve2023.pdf), condition (Ω) and Thm 2.4 checked directly.
This supplies the uniform dimension-3/2 upper sieve needed by the inherited **unspecified** bound U.
Re-derivation: for each a=mq, the remaining prime q′ has range Y≥x^(3/8); level x^(1/8)≤Y^(1/3) is safely inside ordinary BV.
Deleting roots at split primes dividing m only improves the product axiom; the multiplicative compensation h(m) has mean ≪t/√log(2t).
Consequently the bad two-inert-factor term is O(η^(3/2)) in the stated units, whereas the lower bracket is ≫√η.
Choose η small first, then S₀ and δ=η/(8S₀); this establishes an unspecified absolute bound, independently of the unproved sharp switching constants.

## Numerical audit

All executions used `ulimit -v ≤ 6000000`, a CPU limit, `timeout`, and `uv`; no unbounded Cartesian-product arrays.
Original `witness(6,.45,.008,2.35)` rerun at ε=.001:
- main **0.335134563805**, T₁ **0.220940825775**, switched cost **0.076995674880**, margin **+0.037198063150**.
- Mesh masses n=2000/4000/8000: **0.002200215848 / 0.002197416544 / 0.002195863227**, agreeing with the memo.

Independent retained script: `scripts/z56_xrev_k4chen_check.py` (imports none of the source scripts).
It evaluates F by adaptive quadrature from the explicit f on [1,3], rather than the DDE mesh.
It bounds the mass integral using positive log-bin convolutions and extrema of the analytically integrated last-factor kernel.
For j−1 log-bins with lower-index sum t and width h, H=1−Σα lies in [1−(t+j−1)h,1−th].
The kernel is unimodal: its unique peak satisfies y atanh(y)=1, H*=ζ/(1−y²); endpoint minima and endpoint/peak maxima therefore bound each box.
These are genuine integral enclosures in exact real arithmetic; the implementation still uses ordinary floating point, not interval certification.
- Independent main **0.335134490646**; B(.45) **0.022258915057**; L **14.741139756884**.
- Fixed admissible split a=.470, b=.029 gives T₁ **0.222697990938**; positivity needs only M<**0.003212967154**.
- n=2000 bracket **[0.002176670032, 0.002211191579]**, lower margin **+0.035056735334**.
- n=8000 bracket **[0.002189856962, 0.002198489084]**, lower margin **+0.035501254060**.
- Omitted-j bound **1.51424944619e−17**, confirming the quoted tail; disagreement in main is only **7.32e−8**.

Additional source-code reruns at the recorded parameters (same seeds, not independent statistical certification):
- Direct/switch C(6), pen=2.35: **+0.070616565**; C(4), pen=1/1.1/1.2: **+0.047008084 / +0.005792705 / −0.031358294**.
- C(2), θ=.68 with BV switching: **+0.023307923**; θ=.65 with same-level switching: **+0.037967165**.
- Capped LP C(8), θ₁=.42, ζ=.008, h=.002: cost **0.302196822**, margin **−0.018937269**.
These agree with the decisive reported values. Full optimiser grids and all secondary negative ledger cells were not rerun.

## Required fixes, priority order

1. **K6 proof status:** either supply a validated quadrature/error enclosure (the independent positive-box construction offers a route), or call it a conditional numerical witness, with the numerical inequality an additional condition. Grid refinement alone does not prove it.
2. **Preserve the hypothesis firewall:** MT includes distribution *and* local-factor/main-term evaluation; no unconditional explicit Ω_𝒬 bound follows from this audit. State the title as “C(6) in the BV-level model,” not simply “C(6) at BV level.”
3. **Reproduction instructions:** §8's “all scripts default uncapped; K4CAP=1 restores the cap” is false for `lp.py` (always capped) and `direct.py` (always uncapped). Document actual per-script behaviour and the inline uncapped-LP recipe.
4. **Minor precision:** repair the √y endpoint sentence; make the P415 small-p exclusion explicit when inheriting U; for finite-x LP coverage use log(4x+1)/log x rather than 1, or state/justify the asymptotic boundary relaxation.

**Verdict: ACCEPT-WITH-FIXES as model research and exact combinatorial lemmas; do not record K6 as a proved numerical implication until fix 1.**
