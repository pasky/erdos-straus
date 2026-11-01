# Z3054 — where Siegel enters repo ES arguments, and whether Goldfeld(–Gross–Zagier–Oesterlé) suffices

## Verified inputs
* Goldfeld–Oesterlé (statement read in Goldfeld, "The Gauss class number problem…", MSRI Book 49, p. 27):
  for D < 0 fundamental, (D, 5077) = 1: h(D) > (1/55) log|D| ∏_{p|D, p≠|D|} (1 − ⌊2√p⌋/(p+1)).
  Hence L(1, χ_D) = πh/√|D| ≫ log|D|/√|D| (times the product). Same text: for D > 0 the method needs a zero of
  order ≥ 5 to beat the trivial h log ε_D ≫ log D — i.e. for even characters Goldfeld gives nothing beyond trivial.
* Tatuzawa (quoted with constant in Harcos–Thorner arXiv:2508.10844, eq. (1.7)): L(1, χ) ≥ (ε/10) q_χ^{−ε} for all
  real primitive χ with at most ONE exception, constant effective. (Tatuzawa's 1951 paper itself not read.)
* Pollack, IJNT 10 (2014) Thm 1.4 (sources/pollack_ijnt2014_generalsplit6.pdf, Prop 3.3 and end of §4): if no prime
  q ≤ y has ξ(q) ≠ 0, then ∏_{χ≠1} L(1,χ)^{a_{χ,+}} ≪ τ(f)² y^{−ε²/80L²}; Prop 3.3 (Siegel) gives ≫ W^{−ε²/640L²};
  only the characters in ξ⁺ (a_{χ,+} > 0) need the lower bound; non-real ones are effective (≫ 1/log f).

## Inventory (git grep -i siegel over top-level *.md, all ES-side uses)
| place | statement | how Siegel enters | Goldfeld enough? | effective route |
|---|---|---|---|---|
| CAP_DOWN Cor 2.1 (DISCOVERIES (66)) | e*(n) ≪ n₀^{1/4+ε}, n ≡ 1 (8) | Pollack Prop 3.3: lower bound L(1, χ_{−4n₀}) ≫ W^{−δ}, δ = ε²/640L² (ξ⁺ = 1 + χ_{−4n₀}, imaginary) | **No.** Goldfeld gives n₀^{−1/2+o(1)}; the comparison would need y^{ε²/80L²} ≥ n₀^{1/2}, i.e. y ≥ n₀^{40L²/ε²} (L = 4: exponent ≥ 640/ε²) — far worse than the effective O236 rad(n)^5 / Cor 2.2 (p−5)/8 | **Tatuzawa:** effective for every n₀ except those with −4n₀ = the single Tatuzawa-exceptional discriminant (for given ε): one square class n₀ (case (b), n ≡ 5 (8): ξ⁺ = 1+χ₈+χ_{−4n₀}+χ_{−8n₀}: ≤ 2 values of n₀) |
| ASTRA_BRIDGE.md:282 | q₀(p) ≪ p^{1/4+ε} | same Pollack route, ξ = (1−χ₋₄)(1−χ_p) | No (same) | Tatuzawa as above |
| 3/4, log log, m/n notes; DISCOVERIES Thm 5.1 (BV + linear sieve) | exceptional sets / caps | Bombieri–Vinogradov ⇒ Siegel–Walfisz | not needed | effective BV off one exceptional modulus (Z2418 effectivity.md §4) — no class-number input at all |
| BOARD2_SLATE Thm 8.5 | density statement at windows q ≈ L^α | Siegel–Walfisz (Henriot) | not needed | moduli ≤ (log X)^{1/6}: Page + BMOR Prop 1.11 (β ≤ 1 − 40/(√q log² q)) make SW effective for q ≤ (log x)^{2−η} (not re-derived) |
| INVOLUTION_ES2 Thm 6.1(b), Cor 3.4 | windmills barred for 100% of p | Siegel's theorem on INTEGRAL POINTS of curves (not L-functions) | irrelevant (different Siegel; effectivity would need Baker) | — |
| M_BM main term (FRONTIER §2.2, BM_LVALUE Thm A) | M_BM = M₀ − T, T ∝ L(1,χ_p)² | only UPPER bounds on L(1,χ_p) (BM_LVALUE.md:229: "no Siegel-type ineffectivity") — a Siegel zero would make M_BM larger | n/a | already effective |

## Conclusion
PROVED-level arithmetic: Goldfeld's bound is a power n₀^{1/2} too weak at the only place where an L(1,χ) LOWER bound
enters (Pollack-type least-prime bounds). Assessment: Tatuzawa makes CAP_DOWN Cor 2.1 effective outside one (n ≡ 1 (8))
resp. ≤ 2 (n ≡ 5 (8)) unknown square classes n₀; the BV-based theorems become effective without any class-number
input. There is no ES main term that needs a lower bound on L(1,χ); the hypothetical "auxiliary L-function with a
high-order zero" has no slot to fill in the current arguments.
