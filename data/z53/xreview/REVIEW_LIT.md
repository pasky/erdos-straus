# z53 LIT cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** The “narrowed” Assessment survives; do not export the uncorrected PROVED summaries.
Reviewed `side-agent/z53-lit` at `88d949968b4d6d66aa29affa69526fc9a844d7eb`, independently of its §10 reviewer.
ES remains OPEN. No cited paper's full proof is certified by this review.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| L1 Poisson identity, axis terms, BB and Weil bounds | CORRECT | Re-derived below; positive nonzero bump integrals are needed for the main-term comparisons. |
| L1 η > 1/4 and perfect-orthogonality area q^{4/3} | CORRECT-WITH-FIX | Valid fixed-power thresholds for the specified error envelopes, not exact “only if” statements at q^{o(1)} boundaries or a universal bilinear barrier. |
| Pascadi BB(1/700) at q = 4p | CORRECT | Source has the gcd restriction; the memo's mod-4 splitting removes it, with the prime-modulus length condition still satisfied. |
| L2 inverse identity and Farey trial equivalence | CORRECT | Includes x = 1 and the e = x + 1 wraparound; independent finite check agrees. |
| L2 “inverse statistics are functions of p mod lcm” | WRONG as general fixed-N invariance | Only k_x and the anchors k_x/x have that invariance; the explicit 1/(xp) shift remains. At the target log²p scale the modulus exceeds p, so exact dependence is instead trivially injective. |
| L2(a) sup-discrepancy “need not be stable” | WRONG | Star discrepancy is 1-Lipschitz under maximum displacement of the points; its error here is ≤ 1/p. |
| Remark Z algebra / positivity certificate | CORRECT-WITH-FIX | Correct error-envelope calculation; write an upper-bound scale, not an equality for the actual error. |
| Remark Z “for any encoding” into ES | GAP | Incidence multiplicity need not preserve the polylog ES witness count. Restrict the transfer assertion explicitly. |
| GS polylog construction and subexponential obstruction | CORRECT-WITH-FIX | Verified, but explicitly retain existential p and a worst-frequency maximum; no prescribed-frequency obstruction follows from Thm 1.4. |
| EOS / MT real-character alternative / real-zero papers | CORRECT quotations | Verified hypotheses and conclusion types below; none supplies tied divisors or the needed zero-free half-plane. |
| F2a/F2b EVIDENCE | CORRECT numerically | Full reruns agree; independent R and exact-rational D checks agree. These are descriptive associations, not causal explanations. |
| (J)103 and final “narrowed” Assessment | ACCEPT-WITH-FIXES | A scoped “none found” conclusion, not a theorem that all other approaches fail; retain thick-object/extraction escape routes. |

## Independent proof checks

**L1.** Let H = q/X, K = q/Y; both are ≥ 1. Double Poisson gives the stated factor XY/q² and Kloosterman sum, with S(0,0;q) = φ(q).
Fourier decay outside |h|,|k| ≤ √q gives an arbitrarily small power error because X,Y ≥ q^{1/2+ε}; choose the decay order in terms of ε and the desired remainder.
For every d ≥ 1, the NONZERO progression sum satisfies Σ_{j≠0}|ŵ(dj/H)| ≪ H/d: for d ≤ H use summation/integration, and for d > H use Schwartz decay.
Thus an axis contributes ≪ (XY/q²)τ(q)H ≪ Yq^{−1+o(1)}, and the other contributes Xq^{−1+o(1)}.
The coefficient norms are ≪ √H and √K, giving E_BB ≪ √(XY)q^{−η+o(1)} (in the relevant η ≤ 1/2 range the axes are absorbed).
For Weil, bound gcd(h,k,q)^{1/2} by Σ_{d|q,d|h,d|k}√d. The weighted sum is ≪ HK Σ_{d|q}d^{−3/2} ≪ HK, proving E_Weil ≪ q^{1/2+o(1)} without an unbalanced-box gap.
With positive bump integrals, MT = XYq^{−1−o(1)}. At fixed power margins the comparisons are XY < q^{1+2η} and XY > q^{2−2η}; compatibility requires η > 1/4.
These comparisons are between guaranteed upper bounds: they do not prove that the actual error is large, nor decide logarithmic endpoint improvements.
The length-dependent benchmark gives E ≪ √(X+Y)q^{o(1)} by dyadic summation of the rapidly decaying frequencies. Since X+Y ≥ 2√(XY), the best area threshold is q^{4/3}, attained for balanced boxes, again at power scale.
For q = 4p (p large), the only non-coprime small-frequency pairs are both even. Twisted multiplicativity and ≤ 16 residue classes reduce them to S(16^{-1}m,n;p); lengths ≤ 2√p are permitted by Pascadi's p^{1/2+o(1)} range. Signed quadrants use ±λ. No missing p-dependent loss appears.

**L2.** From x x̄ = 1 + pk, obtain integer 0 ≤ k < x, pk ≡ −1 (mod x), and x̄/p = k/x + 1/(xp).
If e | x+1 and 4 | e, put u = (x+1)/e. The condition e ≡ k (mod x) is equivalent to pe ≡ −1, hence p+u ≡ 0 (mod x), giving B = (p+u)/x > 0 and p = 4uBC−u−B with C = e/4. The converse reverses these steps.
For x ≥ 3, the only representatives of k in 4 ≤ e ≤ x+1 are e = k or e = x+1 with k = 1. The memo's wraparound is correct.
But N = 2, p = 5 and p = 11 have the same residue modulo lcm(1,2) and the same anchors (0,1/2), while their inverse star discrepancies are 2/5 and 5/11. This disproves the exact statistical-dependence summaries.
For ordered points t_i, D* = max_i(max(i/N−t_i, t_i−(i−1)/N)). Ordered points move by at most δ if each labelled point moves by at most δ; hence |D*(t)−D*(s)| ≤ δ. Here δ ≤ 1/p.
Consequently the correct statement is stronger and cleaner: D_p(N) is within 1/p of a function of p mod lcm(1,…,N), for fixed N. An individual threshold count need not be stable.
The observation lcm(1,…,N) = exp((1+o(1))N) ≫ p for N ≍ log²p is correct and does not create a bounded-congruence no-go. In that regime the residue identifies p itself, so the counterexample concerns general fixed-N invariance, not injectivity at the target scale.

**Remark Z.** Set U = q^ε√(|A||B|)N^{1−η}, the quoted error-envelope scale, and M = φ(q)|A||B|N/q².
Then U/M = q^{1+ε}N^{1/2−η}/√(φ(q)M). Requiring U = o(M) gives M ≫ q^{2+2ε}N^{1−2η}/φ(q), with the appropriate growing margin and implied constants.
For N ≥ 1 and 0 < η < 1/2 this rules out certifying positivity by this envelope at polylog M when q ≥ p^c. It is not a lower bound on the actual error.
The final ES transfer needs an additional premise: the encoded expected INCIDENCE count must itself be polylog in p. An encoding with a power-size reservoir/many incidences per ES witness is not excluded merely because ES has polylog expected witnesses.

## Fresh source verification (2026-11-01)

Fetched 13 PDFs directly from arXiv, not from the lane's archived excerpts; extracted with `pdftotext -layout` into `/tmp/xrev_LIT/fresh/`.
The decisive source statements, not their complete proofs, were checked:

| Source fetched | Check |
|---|---|
| [Pascadi 2511.08445v2](https://arxiv.org/pdf/2511.08445v2), pp. 2–3 | Perfect-orthogonality benchmark and Thm 1.1 agree: saving 1/700 with (m,n,c)=1; bounded-α version 1/276 requires (n,c)=1. |
| [GS 2304.07953v1](https://arxiv.org/pdf/2304.07953v1), Thms 1.1–1.4, pp. 3–7 | Linnik prime p ≡ −1 mod m, smooth-window lcm, log p ≍ N^{1/A}, and positive Dickman proportion verified. The exponential-sum corollary is max over invertible a, not an assigned a. |
| [Zhang 2605.02518v2](https://arxiv.org/pdf/2605.02518v2), Thm 3.6, pp. 6–7 | Main term φ(q)|A||B|N/q², error q^ε√(|A||B|)N^{1−η}, and τη > 1/M agree. The theorem is for the structured sets in (3.2)/(3.5), not arbitrary encodings. |
| [Shkredov 2603.14116v2](https://arxiv.org/pdf/2603.14116v2), Thm 8 / Remark 9, p. 6 | Numerator count is for class 𝒵; all-q extension in Remark 9 is for existence. Memo correctly preserves this distinction. |
| [Banks 2609.37434v1](https://arxiv.org/pdf/2609.37434v1), p. 1 | Explicitly says EOS is open under GRH and explains the character-sum loss. The new theorem concerns a random model, not actual primes. |
| [MT 2301.07679v3](https://arxiv.org/pdf/2301.07679v3), Thms 1.1/1.3 | Three-prime coverage and ≥ (2/3−ε)φ(q) two-prime coverage agree. Free objects and power scales are genuine limitations for the stated transfer. |
| [BS 2610.19597v1](https://arxiv.org/pdf/2610.19597v1), Thms 1.1–1.4 | Unconditional prime-power results fix the base prime; general-q results require QRH. Polylog third prime does not mean a polylog representation count. |
| [MT 2605.27833v1](https://arxiv.org/pdf/2605.27833v1), Thm 1.1, p. 1 | Real multiplicative h, nonvanishing at primes outside q, squarefree witnesses ≤ q^{2+ε}, exception Σ1/p ≤ c/q^{ε/100} all agree. No identification with the ES quadratic layer follows. |
| [Banks 2610.15483v1](https://arxiv.org/pdf/2610.15483v1), Thm 1.1; [Kerr 2610.21099v1](https://arxiv.org/pdf/2610.21099v1), Thm 1; [Guo 2610.30476v1](https://arxiv.org/pdf/2610.30476v1), Thm 1.1 | Real-zero gaps only; Banks's all-conductor 0.003 uses the stated small-conductor computation; Guo states 0.01. These statements do not give the needed half-plane. Retain unrefereed/claimed status. |
| [Steiner 2302.06409v1](https://arxiv.org/pdf/2302.06409v1), Thms 1–2; [Shen 2607.07710v1](https://arxiv.org/pdf/2607.07710v1), Thm 1 | Steiner averages over moduli with m,n-dependent constants; Shen requires smooth squarefree q, so not 4p. |

Also fetched [DRZ's arXiv notice](https://arxiv.org/abs/2601.00292): withdrawal and missed L² factor confirmed.
Fresh `all:Straus` API query sorted by submission date still has Cao–Xu 2610.32302 (2026-10-23) as the newest ES item; the newer polynomial-classification hit is unrelated.
Fetched [forum #242](https://www.erdosproblems.com/forum/thread/242): latest comment 2026-02-13, page edit 2026-05-07. These checks support only the memo's scoped “none found,” not exhaustive coverage.

## Reproduction

All execution was timeout-bounded; numerical runs used `ulimit -v 6000000`. No dense Cartesian-product allocation was used.
Recompiled and reran `z53_lit_invwin_census.c` over [2,000,000,10,000,000]: all 64,380 TSV rows agree byte-for-byte, including zeros 5,212,561 and 8,813,281.
Reran the analysis: Pearson −0.1668; partial −0.0191; R²(y)=0.1234, R²(D)=0.4814; residual/raw covariance 0.0772; near-square n=2858 and partial −0.0189. Agrees with the memo.
Reran F2a and its adjustment: TSV agrees byte-for-byte; 9/19 rank threshold cases and residual mean z=+0.68, Σz/√19=2.95 agree. No population-level significance is certified by those descriptive z aggregates.
`scripts/z53_xrev_lit_check.py` independently factors p+u and uses u↔B symmetry, rather than the census's triple enumeration: R agrees at 34 selected census primes including both zeros. Exact-rational inverse discrepancy agrees at all 34.
The same script checks L2 and its Farey equivalence on 21,441 (p,x) pairs with p ≤ 500, and prints the p=5,11 counterexample.
Reproduce: `timeout 120s bash -c 'ulimit -v 6000000; uv run python scripts/z53_xrev_lit_check.py /tmp/xrev_LIT/rerun.tsv'` (the branch's original census TSV is interchangeable).

## Required fixes, priority order

1. **Major:** §5(g) “any encoding” must assume a polylog expected incidence count, or controlled polylog encoding multiplicity. Explicitly leave thick-reservoir/extraction encodings open.
2. **Moderate:** Replace the ambiguous L2 statistical-dependence summaries in §§0/4/7/9 with “anchors depend only on the residue; inverse positions differ by ≤1/p.” Distinguish fixed-N invariance from trivial injectivity when lcm > p. Replace the false discrepancy-instability warning by the Lipschitz bound proved above.
3. **Moderate:** State L1 and the perfect-orthogonality threshold at fixed-power precision, with positive bump integrals. Replace exact iff/“never” endpoint language by comparisons of guaranteed error envelopes; do not exclude logarithmic improvements or other completion methods.
4. **Moderate:** In GS routing/export text retain max_a and existential constructed (p,N); do not imply a prescribed-frequency or every-length obstruction. Keep the easy (★) class −1 caveat.
5. **Minor:** In Remark Z write U/M for the envelope ratio, not actual error/M; retain constants/margins in the positivity criterion. Keep EOS as analogy, all new preprints as unrefereed claims, and “none found” as coverage-limited.

After these fixes, the sourced “narrowed” verdict and descriptive F2 findings are supportable. No whole research lane is killed by L1, L2, or Remark Z.
