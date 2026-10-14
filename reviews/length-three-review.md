# R205 — hostile review of LENGTH_THREE.md (O206)

Reviewer: R205 side agent. Reviewed: LENGTH_THREE.md as merged from side-agent/length-three (report AGENT_REPORT_O206.md).
From-scratch scripts: `scripts/review_l3_*.py` (none import or copy scripts/l3_*).
**ES is not solved here; nothing below changes that.**

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Prop 1.1 (pentagon / A₂ frieze, (P), converse, formal vs interior) | SOUND |
| Cor 1.2 (five slices = five cluster variables ≡ 0 mod 4) | SOUND |
| Cor 1.3 (cube = pentagon (c, 4dj, s) at pj; FMS divisibilities = Ptolemy) | SOUND (minor wording, D3) |
| Thm 2.1 (five ES triples = Ford-horocycle fan decompositions) | SOUND (normalisation/terminology, D1, D2) |
| Cor 2.2 (sharp dictionary) | SOUND |
| Thm 3.1 (Machin = CM rotation; K_c(s) = 1/m ⟺ K = N; Type II r² = p/4d) | SOUND |
| Thm 4.1 / Cor 4.2 (m²Norm_μ = hh′ − mμ; (J)38 ε_μ; (J)37 depth 3/1) | SOUND |

## Checks performed

**Prop 1.1 / Cor 1.2** (`scripts/review_l3_words.py 20000 3000`, 55 s). Own enumeration of all words (c, m, s) ≥ 1 with
0 < N ≤ 2·10⁴: 1 194 085 words, 610 533 interior. For every word: the ten |det(V_i, V_k)| equal the claimed λ's; the
five boundary points are in the cyclic order ∞ > c > h/m > N/h′ > 0 (so the pentagon is embedded and fans make sense);
all five Ptolemy relations computed generically from the λ-table; the generic Penner fan identity at each of the
five vertices; the five table identities of Thm 2.1 *as printed*; cs − r² = (c + s)/m. For interior words: h′ < N,
gcd(h′, N) = 1, and an independently computed HJ expansion of N/h′ is exactly [c, m, s]; and own-Jacobi check of Cor 1.2
on all 139 915 + (non-slice) interior words with N ≡ 1 (4). Set identity {h′ : interior words at N} = L₃(N) (L₃ computed
by HJ-expanding every A/N) for all N ≤ 3000. 0 failures. Controls: the set of N ≤ 2·10⁴ without an interior word is
exactly E_W = {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510}; 105 has formal words but no interior word; (1, 4, 2) is a
formal word at N = 5 with L₃(5) = ∅; 69 of the 70 odd squares 9 ≤ N ≤ 2·10⁴ have interior words (9 does not), none has a
slice word.
By hand: V₄ = mV₃ − V₂, V₅ = sV₄ − V₃ = (N, h′); det(V₃, V₅) = c(ms − 1) − N = s; the five quadrilateral Ptolemy
relations (drop V₅, V₁, V₂, V₃, V₄) give exactly the five lines of (P); the converse identity
hh′ − mN − 1 = m(K − N) is correct. N > 0 forces h, h′ ≥ 1 (h = 0 or h′ = 0 forces N = −1), so V₅ ≠ ∞ and the
pentagon is non-degenerate on the whole domain. DK's (v, t, u) = (c, m, s), A = tu − 1 = h′, A* = tv − 1 = h, so DK Thm
4.5's five conditions are exactly 4 | h′, h, m, s, c as claimed.

**Cor 1.3, Thm 3.1 (Type II), Thm 4.1, Cor 4.2** (`scripts/review_l3_cube.py 5000 40000`, 4 m 44 s). Own enumeration
of cube points (bounds 3cd ≤ n + 1 and h | n + 4c²d, both valid for every n): 34 303 points for primes 5 ≤ p ≤ 5000
(10 646 with d = 1; 4 638 / 1 736 for p ≤ 1000), matching the author's counts and COMPOSITION's census. Per point:
K(c, 4dj, s) = pj; hs = N + c, hh′ = mN + 1, ch′ = N + s; j | c + s and h·(c + s)/j = p + 4c²d (so FMS's cofactor e is
(c + s)/j); r² = N/m = p/(4d); the mirror (s, d, j) is a cube point with h-value h′; m²Norm_μ(1/m + z) = hh′ − mμ, = −h at
μ_c and −h′ at μ_s, each dividing μ; the V_{pd} point (A, B) = (2j, 1) at μ = dμ_s = cd·h′ has D = 2μA − pdA² − 1 = h′
(COMPOSITION Prop 4.1(b) with the mirror convention, as the doc says); for d = 1: N(1 + 2jω) = −h in ℤ[√(4μ² − 4p)],
μ > 2p ⟺ j ≥ 2, and my own (P_k, Q_k)-continued-fraction code for √(4μ² − 4p) gives Q₃ = h and (p₂, q₂) = (2μj − 1, j)
when j ≥ 2, Q₁ = h and (p₀, q₀) = (2μ − 1, 1) when j = 1. 0 failures. Odd squares: 0 cube points at all odd squares
9 ≤ M² ≤ 40 000.
By hand: ω = 2dz satisfies ω² + 2dμω + pd = 0; for d = 1, ω = −μ + √(μ² − p) = −η̄ in COMPOSITION's notation
(η̄ = μ − √f), so 1 + 2jω = 1 − 2jη̄ = ε_μ with t = c (c ≤ (p + 1)/3 ≤ p, so Thm 1.3's range is respected). Lagrange applies
since h ≤ pj + c = μ < √(4μ² − 4p). The §4 R-self-repair example (7, 2, 1, 3, 1) is right: [4, 92, 7], and the Ford disc at
−1/12 lies strictly inside the semicircle (centre −11.5, radius 11.424; distance to the disc centre 11.417, disc radius 1/288).

**Thm 2.1, Thm 3.1, Thm 4.1, §6 algebra** (`uv run --with sympy python scripts/review_l3_symbolic.py`): every row of the
Thm 2.1 table is an identity in ℚ(c, m, s) with N := K(c, m, s); DK's b = (N + c)/s equals h; the V₂ and V₄ rows divided by w
are literally DK Thm 4.5's explicit triples for 4 | v and 4 | u (f′ = h′, f = h, t = m); K_c(s) = 1/m and K_c∘K_s = K_{1/m}
as Möbius maps; Thm 4.1 at μ_c, μ_s; Cor 4.2's ω-relation. By hand: each vertex's fan (V_i; V_{i+1}, …, V_{i+4}) gives the
row (e.g. V₂: 1/m + 1/(mh′) + N/h′ = c); K′_x(z*) = (x² + r²)/(x + ir)² = e^{−2i·arg(x+ir)} (clockwise, as repaired);
K_c∘K_s = K_{1/m} ⟸ K_c(s) = 1/m because both fix z*, are orientation-preserving (det = x² + r² > 0) and the stabiliser
of z* acts simply transitively on ∂ℍ; the arccot identity holds exactly (not only mod π) since both sides lie in (0, π)
and (c + ir)(s + ir) = (c + s)(1/m + ir) with c + s > 0.

## Defects

(numbered as found)

**D1 (MINOR, terminology; Thm 2.1 table header, Cor 2.2, §7.1, §7.7(i)).** "Opposite diagonal" of V_i is used for the
diagonal V_{i−1}V_{i+1}. In a pentagon three diagonals avoid V_i (for V₁: V₂V₄, V₂V₅, V₃V₅), so the phrase is ambiguous; the
intended one is the short diagonal that cuts off V_i, i.e. the frieze quiddity at V_i. *Repair:* define it once ("the
diagonal V_{i−1}V_{i+1} cutting off the ear at V_i = the quiddity a_i") and use that.

**D2 (MINOR, normalisation; §2 preamble).** "λ_{ik} are Penner λ-lengths" and "arc = λ_XY/(λ_VX λ_VY) (Penner)" hold
exactly with the normalisation λ = e^{δ/2} (δ = signed distance between horocycles), for which Ford horocycles give
λ = |det| and the arc at ∞ between a/b and a′/b′ is |a/b − a′/b′| = |det|/(bb′). Penner's own papers use λ = √(2e^δ),
under which these formulas acquire factors √2 / 2 (I could not access Penner's paper to quote his exact h-length
convention; sources/ has no copy). The identities themselves are convention-free (checked as rational identities).
*Repair:* state "λ := e^{δ/2} (= |det| for Ford circles)" and attribute the h-length formula with that normalisation.

**D3 (MINOR, Cor 1.3).** (i) "h | p + 4c²d with cofactor e = (c + s)/j follows from 4cd·(hs) = p(h + 1) + 4c²d": the
displayed identity gives the divisibility; the cofactor needs the extra line p + 4c²d = h(4cds − p) and
j(4cds − p) = (h + 1)s − pj = c + s. (ii) Cube words need not be interior: s = 1 or c = 1 occurs (the doc's own §4 example
(7, 2, 1, 3, 1) has s = 1), so "the cube is the pentagon (c, 4dj, s)" is a statement about formal words/friezes, not
about HJ length-3 fractions. Neither affects correctness. *Repair:* add the line and the remark "(possibly formal)".
