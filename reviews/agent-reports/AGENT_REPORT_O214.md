# AGENT_REPORT_O214 — the e = 2 cell (spark relay Y6), checkpoint 1

**Update after R213 (reviews/cap-two-review.md: no FATAL, no MAJOR):** minors m1–m8 applied in CAP_TWO.md, marked
"(R213 repair …)"; also Prop 5.1(c) citation now "3 ∤ n" (m4).

Main file: CAP_TWO.md. Scripts: scripts/y6_dict.py, y6_cover.py, y6_verify.py, y6_count.py, y6_fibres.py, y6_fixE.py,
y6_pt.py (tiny outputs, quoted in the file). Self-review (codex deep): no FATAL; 6 MAJOR + minors, all repaired
(Thm 1.2 hypotheses restored, narrow-class sign corrected, a CF floor bug in the scan scripts fixed and the numbers
re-run (unchanged except one count), B1 citation withdrawn, §7 conditional wording, scripts committed).
**ES^{(y,2)} is NOT proved; no infinite case of ES is claimed.** The R210 calibration is applied: no cap is called a
global finite search.

## SHARP:
1. **One equation, two cells (Thm 1.1/1.2, PROVED, checked).** k = 1 cap-2 shots are exactly the solutions of
   `4n·a² + B² + E = c·a·B·E` with c odd (Q₁ = cB², g = caB − 1, Q₀ = caB/4, 4 | a ⟺ E ≡ 3 mod 4). The SAME equation with
   c ≡ 0 (mod 4) is GROWING_MUTE's ES^{[2]} (A, B) form (k = a, Q₁ = B). Unified: "4na² + B² has a divisor ≡ −1 (mod aB)";
   the cell is the residue of the quotient c mod 4. (R213 repair m1/m6/m7: Q₁ odd is a hypothesis; c ≡ 2 with a even gives
   even-overflow shots, unused; the halves are disjoint as points but overlap as shot sets along a = 1; the fibre statement is
   a necessary condition, cells cut out by side conditions.) Fibrewise (x = cE): **the principal form of discriminant x² − 16n
   represents −E for a divisor E | x**; ES = {B = 1, 4 | c}.
2. **The O204 per-slice contrast is a slicing effect (Prop 2.1, 5.1, PROVED).** The k = 1 slice of ES^{[2]} is the line
   a = 1 of one half; the k = 1 slice of the cap-2 cell is the whole other half. Both have finite slices (fixed a, fixed B;
   c ≤ (4n+1)(B²+1)/B) and infinite Pell orbits. (R213 repair m6: inside the c-odd half the O204 contrast is the line B = 1
   vs B free, i.e. Prop 5.1; "one line vs a half" is the comparison with ES^{[2]}.) On k = 1: any FINITE exponent-2 budget keeps the slice finite; infinite
   exponent-2 support is necessary for infinitude (sufficient only conditionally on squarefree orbit terms).
3. **ES-shaped D-face (Thm 4.1, PROVED).** k = 1 cap-2 ⟺ `a(cBw − 4n) = w + cB³` with D = cBw − 4n ≡ 3 (mod 4) — ES's
   Type II normal form k(4ab − n) = a + b by analogy, (k, 4ab, n, a + b) ↦ (a, Bw, 4n, w + B³) (R213 repair m8). Box criterion: ±2√(−n) ∈ {w/B : wB | D + 4n}
   (mod D), D unbounded (ES: −p ∈ Box((h+1)/4), h = O(p²)). Fixed-modulus tests: "64n³ + c²w⁴ has a divisor ≡ −4n (mod cw),
   ≡ 3 (mod 4)"; (c, w) = (1, 1): any D ≡ 3 (mod 4) dividing 64n³ + 1 gives Q₁ = (4n + D)² (if 4n + D is squarefree and gcd((1 + (4n+D)³)/D, n) = 1 — R213 repair m2; fails e.g. n = 21, D = 19).
4. **Not a polylog lottery (EVIDENCE + Assessment).** 5–15% of odd fibres x ≤ 3000 carry points (finite range; heuristic
   fraction ≍ (log X)^{−1/2}, not a proven positive proportion — R213 repair m5) (n = 13, 379, 1009; 0 for
   n = 9, 25), but at heights up to 10¹⁷ (deep in long CF periods). This is exactly MARKOFF_ES §6's two-layer picture
   (genus layer + class-group layer), now in odd discriminants x² − 16n, plus one extra layer (B squarefree on an orbit).

## Results (labels)
* Thm 1.1, Thm 1.2, Prop 2.1, Thm 4.1, Prop 5.1: PROVED (elementary); y6_dict checks both directions (120 / 121 / 179
  points) and the D-face identities.
* §6 no polynomial families at fixed E with c non-constant (MARKOFF Thm 5.1's unit argument, verbatim): PROVED.
* EVIDENCE: every prime 3 ≤ p < 10⁶ has a k = 1 cap-≤2 shot with g ≤ 10⁶ (78 497, exact re-verification against Def 1.1);
  for 13 401 the least-g shot has B > 1 and 783 have no cap-≤1 k = 1 shot at any g ≤ 10⁶ (R213 repair m3); largest least g = 955 979 at p = 379 (long tail). No odd square ≤ 10⁶ has one (T1).
* T1 location (every face): "D (or E) ≡ 3 (mod 4) divides a sum of two coprime squares".

## Verdict / negative calibration (Assessment)
ES^{(y,2)} at k = 1 is not an easier target than ES^{[2]}: existence = "some ideal of norm E | x is principal with a
negative-norm generator in the order of discriminant x² − 16n" (a class-group statement in a quadratic family; open) plus
squarefreeness of B at some orbit point (Wieferich-type; open). Brief items: (a) explicit infinite candidate families
exist (tests, orbits) but firing is a class-group event; (b) DFI/root equidistribution works at scales ≫ 1/D, the box is
D^{o(1)} (B3); (c) R ↔ s is a ↔ B with dual weights, not an involution of W_n; (d) GRH touches neither the box nor the
class layer; (e) answered on the k = 1 slice by Prop 5.1.

## Sparks (not pursued)
1. **Relaxed norm −4nE.** The a-Vieta move is multiplication by ω = (x + √Δ)/2 (norm 4n): representations of −4nE are
   governed by 2^{ω(4n)} ideal choices instead of one; a −4nE point descends to a W_n point iff xB ≡ t (mod 4n). Is there
   an ES-variant whose certificate is exactly the −4nE point (more class freedom)?
2. **Both halves together.** ES^{(y,2)} ⟸ any W_n point with c odd (B squarefree) OR c ≡ 0 mod 4 (B cube-free). The
   combined fibre count and a cube-free (rather than squarefree) orbit condition may be the most tractable version.
3. **Fibre-count asymptotics.** Measure #{x ≤ X: fibre has a point} against a half-dimensional-sieve prediction
   X/(log X)^{1/2} and the Cohen–Lenstra factor; compare c-odd vs c ≡ 0 halves.
4. **Squarefree B along orbits.** Empirically the found orbit points are squarefree; a sieve over the Lucas sequence
   B_j for small ℓ plus abc-conditional large ℓ would give a clean conditional statement "ES^{(y,2)}(n) ⟸ c-odd fibre
   point (abc)".
