# Review R179 of FF_STERILE_PROOF.md (O179) — hostile, round 1

Reviewer: R179. Document reviewed: FF_STERILE_PROOF.md at merge of side-agent/ff-sterile-proof (report
reviews/agent-reports/AGENT_REPORT_O179.md). From-scratch scripts: `scripts/review_fsp_poly.py` (own F_q[T]
arithmetic incl. irreducibility test and Cantor–Zassenhaus factorisation), `scripts/review_fsp_enum.py`,
further `scripts/review_fsp_*.py` listed per claim. Nothing here concerns ES over Z.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (one-sided form), Lemma 1.2 (cylinder = rational approximation) | SOUND |
| Lemma 2.1 (genus parity) | SOUND (but not new: it is FF2 §3's R166-checked parity plus arithmetic; see D-list) |
| Lemma 3.1 (π-weights, π-free families) | SOUND |
| **Thm 3.2 (O(q, A) Haar-null)** | **SOUND** (true, short, essentially the classical almost-all mechanism of FUNCTIONFIELD_ES Thm 5.3 in profinite form; consequence (a) needs a scope sentence) |
| (in progress) | |

## Lemma 1.1 / 1.2 — SOUND
Re-derived. (⇒) E′r = TH′L′r − r = H′L″(H + H′) − r = HH′L″ + H′²L″ − r = T^K + H′²L″ using (I), (II) and
L′ = g′L″. (⇐) as written. Lemma 1.2: H′(1 − THL′) = H′ − T g′ HH′L″ ... = −H − T^{K+1}g′ (asserted on every
enumerated solution in `review_fsp_enum.py`); EE′ = D = 1 + T^{K+2}g′²L″ (asserted on every solution).
**Independent enumeration.** `review_fsp_enum.py` enumerates by the *one-sided* route of Lemma 1.1 (choose
H′, g′, L″, test E′ | T^K + H′²L″, recover H) — a different search from the author's (H, H′) route. Solutions
with a ≥ b are found directly (bound b + deg g′ + λ ≤ K − 1 from deg r = K − 1 − (b + deg g′ + λ)); a < b
solutions are their H ↔ H′ swaps. Result for K ≤ 12: 226 solutions, **set-identical** to `fsp_enum.py 12`
(sorted line-by-line `cmp`), per-K counts 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104 (K = 2..12). Note: the
document's "cyclotomic counts 2, 6, 8, 12, 4, 72, 4" are the r-constant subcounts, not these totals.
(K ≤ 14 run: see below.)

## Lemma 2.1 (genus parity) — SOUND; attribution needs repair
Re-derived step by step: D = EE′ = 1 + T^{K+2}g′²L″ = 1 + MY² with (M, Y) as stated; for π | E, π ∤ MY (else
π | 1), so −M ≡ Y^{−2} is a nonzero square mod π and (−M/E) = 1 (E monic of degree 1 + a + l ≥ 1, E(0) = −1).
In F₃[T] ((q − 1)/2 = 1): (A/B)(B/A) = (−1)^{deg A deg B}; (−1/B) = (−1)^{deg B} since (3^d − 1)/2 ≡ d (mod 2);
(T/B) = (−1)^{deg B}(B(0)/3); (2/3) = −1. (E/L″) = (−1)^λ since L″ | L′ | E + 1. Hence
K even: (−1)^{deg E + λ + λ deg E} = 1 ⟺ (1 + deg E)(1 + λ) odd ⟺ deg E, λ even;
K odd: (−1)^{deg E + (deg E + 1) + λ + λ deg E} = 1 ⟺ λ(1 + deg E) odd ⟺ λ odd, deg E even. Same for E′.
Consequences a ≡ b, a + b ≡ 0, l ≡ a + 1, λ ≡ K (mod 2) follow from deg E = 1 + a + l, deg E′ = 1 + b + l,
K = a + b + λ. deg r ≡ K: re-derived (cases a > b, a = b (leading coefficient 1 + 1 = 2 ≠ 0), a < b).
Check (from scratch, independent solution list): K ≤ 12, 226 solutions, **0 violations** of deg E, deg E′ even,
λ ≡ K, deg r ≡ K; classes (a, b, λ, K mod 2): (0,0,0,0) 100, (1,1,0,0) 62, (0,0,1,1) 52, (1,1,1,1) 12.
Note that the hypothesis "on the slice (u(0) = 1)" is not used: E(0) = E′(0) = −1 holds for every solution of
(I), (II) by definition of E, E′. Only the identification of solutions with families needs the slice.

## Lemma 3.1 (π-weights) — SOUND
Re-derived. AL | P + E with x a unit gives gcd(E, AL) = 1, so mod E: P ≡ π, X ≡ π/A, X/L ≡ π/(AL), and the four
types are ≡ a₀, πa₀, π/(Aa₀), π²/(Aa₀) (weights 0, 1, 1, 2). Equal weights: E | s reduces to E | a₀ + b₀,
E | L/a₀ + L/b₀ (types 2,2 and 3,3, using X/L a unit mod E) or E | 1 + Aa₀b₀ (types 1,2), no π. Weight difference 1
(types (0,1), (0,2), (1,3), (2,3)): linear in π; (0,3): π² ≡ −Aa₀b₀. lc(s) = 1 for distinct types once n ≥ n_F
(Lemma 6.2). Correct.

## Theorem 3.2 (O(q, A) is Haar-null) — SOUND
*Setting.* R̂ = lim F_q[T]/W = ∏_ℓ O_ℓ (CRT), R̂^* = ∏_ℓ O_ℓ^*, Haar = product of the normalised Haar measures;
O(q, A) is closed (FF2 §0.1: complement = union of the clopen validity sets V_F), hence Borel. Fine.
*Family.* F_ℓ = (ℓ; 0, 1; 2, 1): a = 1, b = X, s = 1 + X, n_F = 1 + max(k, deg ℓ). Valid ⟺ A | P + ℓ and
ℓ | 1 + X ⟺ ℓ | A + P + ℓ (A invertible mod ℓ) ⟺ P ≡ −A (mod ℓ); lc(s) = lc(X) = 1 = lc(ℓ) since n > k; s ≠ 0.
ℓ ≡ −κ (mod A) with κ a unit forces ℓ ∤ A. Checked from scratch (`scripts/review_fsp_thm32.py`, log
`data/review_fsp_thm32_log.txt`): for (q, A) ∈ {(3, T²), (5, T), (3, T² + 1), (2, T³)}, all monic P of one degree
n and all irreducible ℓ ∤ A of degree ≤ 2 (≤ 3 for q = 2), 15 337 pairs: generic validity (FUNCTIONFIELD_ES §6.2
definition) ⟺ the two congruences, and in every valid case A·XYZ = P(XY + YZ + ZX) holds with monic X, Y, Z of
degree ≥ n − k. (Includes q = 2: the theorem's "every q" is fine, NC being checked.)
*Probability.* B_ℓ = {x_ℓ ≡ −A (mod ℓ)} depends only on the ℓ-component; −A is a unit mod ℓ, so μ(B_ℓ) =
1/(|ℓ| − 1). The κ-event lives on the components at primes of A, disjoint from all ℓ, so conditioning on κ is
harmless; the B_ℓ are mutually independent (product measure) — full independence, not just pairwise, so BC-II
applies verbatim. Divergence: #{ℓ monic irreducible, deg ℓ = e, ℓ ≡ −κ (A)} = q^e/(Φ(A)e) + O((k + 1)q^{e/2}/e)
(prime polynomial theorem in progressions, Rosen, *Number Theory in Function Fields*, Thm 4.8 — **not accessed
by me** (no copy in sources/); FUNCTIONFIELD_ES Fact 5.2 cites the same standard result). Even Dirichlet's
theorem in analytic form (L(1, χ) ≠ 0) suffices for divergence of Σ 1/|ℓ|. Numerically (q = 3, A = T²,
`review_fsp_thm32.py`): S(e) = Σ_{deg ℓ ≤ e} 1/(|ℓ| − 1) per class grows by ≈ 1/(6e) per degree (≈ (H_e)/Φ(A),
Φ(T²) = 6) for all six unit classes κ; e.g. e = 11: S ∈ [0.24, 0.86].
*Conclusion.* For each of the Φ(A) classes κ, a.s. infinitely many F_ℓ are valid; a finite union of null sets
is null. ∎ Correct as stated, including "for every q and every monic A of positive degree".
*Consistency with earlier statements* (all checked, no contradiction):
* O140 Prop 4.1 (1 ∈ O for char ≥ 5): a nonempty null set. Direct check: F_ℓ at x = 1 needs ℓ ≡ −1 (A) and
  ℓ | A + 1; deg ℓ ≤ k with ℓ monic ≡ −1 (A) forces ℓ = A − 1, and A − 1 ∤ A + 1 (difference 2). So no F_ℓ is valid
  at 1, as it must be.
* FF2 §0.1 tree plateau ≈ 1 % (R166 D11): O null ⇒ for every ε finitely many families cover mass ≥ 1 − ε (inner
  regularity), so the plateau must eventually fall with NTH → ∞. But see D2: the theorem gives **no rate**; the F_ℓ
  family alone leaves uncovered mass ∏(1 − 1/(|ℓ| − 1)) ≈ e^{−S(e)} ≍ e^{−1/6} at deg ℓ ≤ e (computed: 0.35–0.79
  per class at e = 11), so F_ℓ alone would need astronomically large ℓ to beat 1 %.
* FF2 §0.2 / (J)14 positive *slice* measure: the slice {x ≡ 1 off T} has Haar measure 0 in R̂^*, and the slice
  measure is a different measure; O ∩ slice may have positive slice measure while O is Haar-null. No conflict;
  DISCOVERIES (J)14 already states this. Thm 3.2 does **not** decide FF2 §0.2's slice alternative ("positive
  measure inside this slice" vs "empty or null") — see D2.
* FUNCTIONFIELD_ES Thm 5.3 (failure proportion ≤ (Φ(A) + o(1))/log n) is the same mechanism (one prime g in a
  progression dividing a shift of P, BC/second-moment); Thm 3.2 is its measure-theoretic profinite form. The
  "PROVED, ~5 lines" headline is accurate, but novelty is low (D3).
*Integer analogue (sanity).* Over Z the same argument (ℓ ≡ −x (mod 4) prime, x ≡ −4 (mod ℓ); a = 1, b = X =
(n + ℓ)/4, ℓ | 1 + X) shows the Mordell/linear-family obstructed set in Ẑ^* is Haar-null. That is weaker than the
known "almost all n" theorems (Vaughan 1970: exceptions ≤ N exp(−c(log N)^{2/3})) and says nothing about every
prime. The document makes no integer claim; the report's spark correctly guesses "probably just a restatement".
No overclaim.
