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
