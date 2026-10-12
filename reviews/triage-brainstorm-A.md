# Triage red team A (O156): hostile triage of BRAINSTORM memos a–i

Scope: the 22 files `BRAINSTORM/[a-i]*` (addcomb_… through invol_windmill_signature). None of them was written by
O146 or O154 (checked: memo headers + `git log -- BRAINSTORM`; neither task has a memo or report on this branch), so all
22 are triaged here. Labels as in DISCOVERIES.md. ES is not solved; nothing here proves any case of it.
Spot-check scripts: `scripts/triage_*.py` (named per memo where used).

Format per memo: **verdict-validity** (AGREE / DISAGREE / PARTIAL with the memo's own verdict) · overclaims ·
strongest open sub-question · novelty of by-products · **promise 0–5**.

## Per-memo triage

**addcomb_unit_fraction_density (O142c; memo: COLLAPSES B3).** AGREE. Bloom's Prop 1 forces |S| ≥ N^{1−o(1)} terms and
the circle-method engine needs equidistribution of many q-adic residues per prime power; three terms have none, so the
method has no k = 3 shadow beyond the local "every ℓ-adic pole cancels" rule (§3.2), which is exactly how ET derive the
Type I/II parametrisation. §3.3's "f_II(p) ≍ log³p on average (from memory)" is consistent with ET Thm 1.7
(Σ_{p≤N} f(p) ≍ N log²N up to loglog, over N/log N primes). §3.4 (e-slice condition is purely multiplicative on the
unit part) is correct and one line. No false negative: the method's hypotheses (many terms, density in A) are
simply absent. Open sub-question: none of substance. By-products: known (ET §2). **Promise 0.**

**anal_dirichlet_series (O151a; memo: COLLAPSES B6/T7, 3/4 ceiling, B2/H-E).** AGREE with the verdict, but **one
mis-scoped PROVED item**. Prop A.1 (E finite ⟺ P_E continues along the real axis to s = 0, by Landau) is correct and
tautological. **Prop A.2 is overclaimed:** "D_g − D_f is holomorphic on Re s > 0" needs Σ_{p∈S} f(p)p^{−σ} < ∞ for all
σ > 0, i.e. f(p) ≤ p^{o(1)} on S. That pointwise bound is not known; the best is f(p) ≪ p^{3/5+O(1/loglog p)} (ET; cf.
POINTWISE_MN3 Lemma 5.2 for the m-analogue). As proved, the invisibility holds on Re s > 3/5 (and on Re s > 0 only
conditional on a sub-polynomial pointwise bound, or for S chosen inside {p : f(p) ≤ p^{ε}} — which the counterfactual
cannot guarantee). The conclusion (linear Dirichlet-series data leak exactly as T7) survives with 3/5 in place of 0, since
everything known about D_f lives at Re s ≥ 1 anyway. Open sub-question: none useful for pointwise ES (the memo's own
"continue D_II past 1/2" is an average). Novelty: A.1/A.2 folklore-level. **Promise 0.**

**anal_euler_product_law (O151c; memo: COLLAPSES B1; (E2) spurious).** AGREE. A pointwise law in the Legendre symbols
is a CRT conditional mean (Prop A / Thm F), so it cannot certify any p. The B5 point is right: at m² the zero is the
global Jacobi identity (EXF Prop 2.1), not the limit of an Euler product. The EVIDENCE (β·log p ≈ 6.2 constant over
three decades for f_I, p ≡ 1 (8)) has a heuristic explanation the memo does not spell out, and that explanation makes
the law expected rather than surprising. The Legendre symbols of small q fix the genus sign (−d/p) only for
Y-smooth d. In the log-uniform measure on d ≤ p^{O(1)} (the measure ET's mass lives in), the Y-smooth d carry a
fraction ≈ Σ_{q≤Y} 1/q / log p of the mass. So a relative effect `(A/log p)·Σ χ_p(q)/q` is what the Haar/CEILINGS
model predicts. Hostile note: "relative O(loglog p/log p)" is asymptotic only. At p ≈ 3·10⁶ the fitted β ≈ 0.42
still moves g by ±40 %, so the law explains a lot of variance at accessible p (R² 0.55). Open sub-question: none
pointwise. The memo's averaged CONJECTURE (an asymptotic for Σ_{p≡r(Q)} f(p) with an explicit local factor) is
plausibly provable by ET-style averaging but irrelevant to ES. Novelty: the numerics are plausibly new; the
mechanism is the standard Haar heuristic. **Promise 1.**

**anal_moments_structured (O151b; memo: COLLAPSES B3/B6, B1/B4, B2).** AGREE. Checked by hand:
* the row II{a,d} lift. A divisor f ≡ −1 (mod 4ad) of p + 4a²d gives c = (f+1)/4ad, e = (p+4a²d)/f and b = ce − a > 0
  (because (f+1)(p+4a²d) > 4a²d·f), with 4abd = p + e. So the "sterile ⇒ structured" direction is valid.
* Prop B.1. Exponent 2 of (ℤ/4ad)^× for 4ad | 24 means every element of the subgroup H is a squarefree-divisor
  residue.
* The B5 remark. Every prime factor of m² + 4 is ≡ 1 (mod 4).
* Remark B.2 (the extension to 4ad ∤ 24 fails) is correct and useful.

The 10-condition sieve bound N/(log N)^{1+κ′} is weaker than known results, as the memo says. The Chebyshev
arithmetic (Var/μ² ≈ 1/log p ⇒ E(N) ≪ π(N)/log N) is right. False-negative check: one could add the Type I
exponent-2 slices to Prop B.1's nine Type II slices, or use all slices with q_θ | 24·k for a fixed k. Either way the
set stays finite (Thm 2.2(iii) / B4), so the verdict stands. The fixed-p "lottery is driven by τ₃ of a few shifts
(p+e)/4" is EVIDENCE at accessible p and is exactly H-A. Open sub-question: the CONJECTURE var(log f(p)) → 0
(f(p) ~ μ(p) for almost all p). It is averaged and a plausible Turán–Kubilius-style exercise, but it gives nothing
pointwise. Novelty: Prop B.1 is folklore (Mordell/Yamamoto-era "p + 4 has a prime factor ≡ 3 (4) ⇒ ES"). The
variance-law numerics are plausibly new. **Promise 1.**
