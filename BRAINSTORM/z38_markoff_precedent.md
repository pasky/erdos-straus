# z38_markoff_precedent — Ghosh–Sarnak's Markoff surfaces as the calibration family for "BM-corrected density ⟹ points" (O268)

**Idea.** Find a family of log K3 surfaces with integral-point counts of the same polylog scale as (★) where the pointwise
"local density with BM correction ≫ 1 ⟹ integral point" question has been studied, and read off what is true there.

**Literature.** Ghosh–Sarnak, Integral points on Markoff type cubic surfaces, Invent. Math. 229 (2022) 689–749,
arXiv:1706.06712: V_k : x² + y² + z² − xyz = k; Σ_{|k|≤K} h(k) ∼ CK(log K)² (mean (log k)², cf. (★): M₀ ∼ 0.152 (log p)²);
Thm 1.2: infinitely many Hasse failures (≫ √K/(log K)^{1/2} per LM), almost all admissible k represented (via a variance bound
for a local-density proxy δ^{(m)}(k) averaged over k); numerics: Hasse failures ∼ C₀K^{0.8875}. Loughran–Mitankin (IMRN 2021,
`sources/r202/1807.10223.txt`) Thm 1.5: ≫ √K/log K failures with NON-EMPTY integral BM set (CTWX Thm 5.8: √K/(log K)^{1/2});
LM Thm 1.4 bounds BM-explained failures, so if the numerics hold almost all failures are non-BM. Browning et al., Selecta Math. 2025
(doi 10.1007/s00029-025-01074-1): log K3 heuristics; BM not always sufficient for log K3.

**Dictionary.** k ↔ n; h(k) ↔ R(n); δ^{(m)}(k) ↔ M_BM(n) (product of local densities with the Brauer factor); GS "almost
all k" ↔ (★) for almost all p (known for ES-type counts on average, B6); GS Thm 1.2(i) failures k = 4 + βν² (descent through the
singular Cayley cubic V₄ + reciprocity) ↔ a hypothetical "prime T1" for (★) (none known).

**Barrier screen.** B6: GS's positive result is exactly an average-over-k theorem — the ES analogue is known and useless at
one p. B3: GS's failures are lower-tail events of a (log)²-mean count, as are (★)'s. T1: GS's structured failures are the
Markoff analogue of T1 (algebraic family + reciprocity); for ES the only such family is the squares.

**Cheap numerics.** Our (★) zero set over odd non-squares ≤ K grows with local exponent 0.66 → 0.58 (K = 10⁴…10⁶), dominated
by small-M composites; at fixed M the zero rate is ≈ 2–3× (rising to 5–15× in the far tail) the swap-Poisson e^{−M/2}
(`scripts/z38_zero_growth.py`, `z38_zero_law.py`). Unlike GS's stable 0.8875, our exponent is falling.

**Assessment.** Literature calibration (Assessment). It shows H⁻_BM is a strong, non-standard statement: in the one comparable
studied family "BM set non-empty ⟹ point" fails infinitely often (LM Thm 1.5; a large BM-corrected density along those
failures is not established). It also suggests the precise question for ES: is there a GS-type
structured family (descent through a singular fibre + reciprocity) for (★) beyond the squares? Not found here.
