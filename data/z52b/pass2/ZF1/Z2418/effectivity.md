# Z2418 — where Siegel enters the 3/4 note, and whether explicit PNT-in-AP inputs can replace it

Source audited: `paper/es-threequarter-note.tex` (version C2), all 902 lines grepped for
Siegel/Walfisz/Bombieri/ineffective/explicit, §§2–5 read.

## 1. Inventory of analytic inputs (premise check)

| step | input | effective? |
|---|---|---|
| eq. (BT), Thm 3.4 upper bound, Lemma 3.3 | Brun–Titchmarsh, Montgomery–Vaughan form, constant 2 | explicit |
| eq. (Shiu), Lemma 3.3 (`lem:wsecond`) | Shiu Thm 1, F = 2^ω n/φ(n), boxes (U, 21U/20] | effective (elementary proof; constant never made explicit in the literature we know) |
| Lemma lattice / lem:h | elementary (Möbius, integrals) | explicit |
| Lemma 4.? void, moments, Bonferroni ledger (§§5–7) | CRT probability, Chernoff, combinatorics | explicit |
| **eq. (BV), Thm `thm:supply`, lower bound** | **Bombieri–Vinogradov with R = 26, moduli q = 4uv** | **ineffective (the only ineffective step)** |

The note itself says so (Thm 1.1: "The constants are ineffective, because the proof uses the
Bombieri–Vinogradov theorem"). Siegel–Walfisz enters *only* through BV, and BV is used *only* in one inequality:
|Σ_triples E_x| ≤ (Σ_q W(q)² E*_x(q))^{1/2} (Σ_{q≤4x^{1/3}} E*_x(q))^{1/2} ≪ x t^{−10}, needing
Σ_{q≤4x^{1/3}} E*_x(q) ≪ x (log x)^{−26}.
Moduli actually occurring: q = 4uv with H < u, v ≤ x^{1/6}, H = K^{10} = X^{1/48}, so q ∈ (4X^{1/24}, 4x^{1/3}].

## 2. Can BMOR (Bennett–Martin–O'Bryant–Rechnitzer, arXiv:1802.00085) replace it? No.
Verified statement (BMOR Thm 1.1/1.2, eq. (1.10)): |ψ(x;q,a) − x/φ(q)| < c_ψ(q) x/log x for x ≥ x_ψ(q), with
x_ψ(q) = 8·10⁹ for 3 ≤ q ≤ 10⁵ and x_0(q) = exp(0.03 √q log³ q) for q > 10⁵. Here q > 4X^{1/24} while x ≤ X, so the
range condition would need log X ≥ 0.03·X^{1/48}·…: never satisfied. Structurally, too: a pointwise bound
c·x/(φ(q) log x) summed over q ≤ 4x^{1/3} gives ≍ x, not x(log x)^{−26}. An *average over moduli* is indispensable.

## 3. Platt–Trudgian (arXiv:2004.09765, RH to height 3·10¹²): irrelevant here except through explicit ψ(x) for the
main term ψ(y)/φ(q); no role for q ≥ X^{1/24}.

## 4. What does work (Assessment: proof sketch, not reviewed)
Inputs:
(a) Akbary–Hambrook, arXiv:1309.2730, Thm 1.2 (verified statement): for x ≥ 4,
Σ_{q≤Q} (q/φ(q)) Σ*_{χ mod q} max_{y≤x} |ψ(y,χ)| < c0 (4x + 2x^{1/2}Q² + 6x^{2/3}Q^{3/2} + 5x^{5/6}Q)(log x)^{7/2},
c0 = 48.83 (Σ* = primitive characters; fully explicit). Dyadic splitting gives the Gallagher form below. [Their Thm 1.3 — explicit BV — is restricted to moduli with least prime
factor ℓ(q) > Q1; the note's moduli 4uv are even, so Thm 1.3 does not apply verbatim.]
Use Thm 1.2 in the form of Gallagher's lemma, i.e. Σ_{Q1<r≤Q} (1/φ(r)) Σ*_{χ mod r} max|ψ(y,χ)| ≪ (x/Q1 + …)(log x)^{9/2}.
(b) Effective zero-free region with one Landau–Page exceptional real character χ1 (conductor r1) among conductors
≤ T = exp(c√log x): ψ(y,χ) ≪ x exp(−c√log x) effectively for every other primitive χ of conductor ≤ T.
(c) BMOR Prop 1.11 (verified statement): β ≤ 1 − 40/(√q log² q) for any real zero of a quadratic character mod q.

Effective BV off one modulus: reducing E*(q) to primitive characters in the standard way,
Σ_{q≤4x^{1/3}, r1∤q} E*_x(q) ≪_eff x (log x)^{−26}, taking Q1 = (log x)^{31} and Q = 4x^{1/3} (so x^{1/2}Q, x^{2/3}Q^{1/2} ≤ 4x^{5/6}), using (a) for conductors > Q1 and (b)
for conductors ≤ Q1 (Σ_{q: r|q} 1/φ(q) ≪ log x/φ(r)).
Two cases for the exceptional conductor r1 (if any):
* r1 ≤ (log x)^{1.9}: by (c), x^{β1} ≤ x exp(−40 log x/(√r1 log² r1)) ≤ x exp(−(log x)^{0.04}) — beats every log power,
  so no exclusion is needed.
* r1 > (log x)^{1.9}: in the *lower* bound of Thm supply drop all triples with r1 | 4uv (the brackets
  π(2x;q,a) − π(x;q,a) are ≥ 0, so dropping is legal). If p | (r1, k) then (uv, k) = 1 forces p ∤ uv, so only
  m = r1/(r1,4k…) matters, and Σ_{(u,v)∈S(k,c;H,z), m | uv} 1/(uv) ≪ τ(m)/m · (φ(k)/k²) Λ² ≪ (log x)^{−1.9+ε}·main.
  The remaining error is covered by the effective BV above. The upper bounds (BT, Shiu) are untouched.
Conclusion (Assessment): Theorem 1.1 of the 3/4 note (and by the same argument the log log note and the m/n note,
which also use BV only in this way — not re-audited line by line) holds with **effective** c_*, C_*; with
explicit Shiu constants (not available to us) they would even be explicit, but astronomically small.

## 5. Why no "calibration" can come out (premise of the item's `why` fails)
Any bound E(N) ≤ C N exp(−c(log N)^{3/4}) has right side → ∞; it can never certify E(N) = 0 below some X, nor "no
counterexample below X with property P" (it is a density statement). Effective constants only make the *rate*
computable. The finite verification (10¹⁷/10¹⁸) is unrelated.

## Not done
No line-by-line rewrite of the note; Shiu's constant not made explicit; vaughan-loglog / m/n notes only grepped
(BV/Siegel lines 40, 335, 356 resp. 138, 207, 1172), not re-derived.
