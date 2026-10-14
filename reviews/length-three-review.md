# R205 — hostile review of LENGTH_THREE.md (O206)

Reviewer: R205 side agent. Reviewed: LENGTH_THREE.md as merged from side-agent/length-three (report AGENT_REPORT_O206.md).
From-scratch scripts: `scripts/review_l3_*.py` (none import or copy scripts/l3_*).
**ES is not solved here; nothing below changes that.**

**Repairs applied** (author quiet at review end; all marked "(R205 repair)" in LENGTH_THREE.md): D1, D2 (§2 preamble),
D3 (Cor 1.3), D4 (§6), D5 (§7.6), D6 and D7 (§5), D8 (status line), D9 (§5 scope/novelty, §7.6 O144 cite), D10 (Cor 2.2).
No mathematical content changed. Not done: the (J)9/DK attribution to Ventas 2026 (outside this document; forwarded).

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Prop 1.1 (pentagon / A₂ frieze, (P), converse, formal vs interior) | SOUND |
| Cor 1.2 (five slices = five cluster variables ≡ 0 mod 4) | SOUND |
| Cor 1.3 (cube = pentagon (c, 4dj, s) at pj; FMS divisibilities = Ptolemy) | SOUND (minor wording, D3) |
| Thm 2.1 (five ES triples = Ford-horocycle fan decompositions) | SOUND (normalisation/terminology, D1, D2) |
| Cor 2.2 (sharp dictionary) | SOUND-AFTER-REPAIRS (D10: quantifiers / interior domain) |
| Thm 3.1 (Machin = CM rotation; K_c(s) = 1/m ⟺ K = N; Type II r² = p/4d) | SOUND |
| Thm 4.1 / Cor 4.2 (m²Norm_μ = hh′ − mμ; (J)38 ε_μ; (J)37 depth 3/1) | SOUND |
| §6 (Q²-side pentagons ↔ divisors h ≡ 3 (4) of 4n + Q²; 4/n identity; torus) | SOUND-AFTER-REPAIRS (D4) |
| §7.6 (Farey-chain census) | SOUND-AFTER-REPAIRS (D5: definition omits coprimality) |
| §5 summary / four "3"s | SOUND-AFTER-REPAIRS (D6: re-asserts the retracted cutting-sequence claim; D7) |
| §7.1 ear lemma screen | SOUND (formal-word claim checked: p ≡ 1 (4) ≤ 2000, 0 mismatches) |
| §7.3 moving pencil reduction (PROVED reduction) | SOUND (D(4djλ − 1) = 4dj²p + 1 re-derived) |
| §7.4 genus argument at squares | SOUND (proof re-derived; (−d/h) = (p/h) = −1 at all 11 143 cube points p ≤ 2000; 0 cube points at odd squares ≤ 40 000) |
| §7.2, §7.5, §7.7 | Assessments, correctly labelled; 7.5's repaired statement (reduced z*_d lie on Re z = 0) is right |
| Labels / scope / novelty (§5, §8) | SOUND-AFTER-REPAIRS (D9: prior art Ventas 2026 for the V₁ row; O144 precursor) |

**Overall.** No FATAL defect and no mathematical error in any theorem. All identities, bijections and censuses
reproduce with independent code. Defects are one MAJOR-presentational leftover (D6) and minor wording, domain,
attribution and definition issues (D1–D5, D7–D10). ES is not claimed solved, and no infinite case is claimed.

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

**§6** (`scripts/review_l3_side.py 3001 15`, 11 s). All positive-integer solutions (c, s, h, h′) of the five Ptolemy
relations found by brute force over c (no divisor parametrisation): for odd n ≤ 3001, odd Q ≤ 15 they are exactly the
divisors h ≡ 3 (4) of 4n + Q² — 23 510 pentagons, matching the author; the identity 4/n = 1/(sn) + 1/(sc) + Q²/(cn) holds
exactly on all. When gcd(n, Q) = 1, gcd(cn, Q) = 1 always (q | Q, q | c ⇒ q | h ⇒ q | hh′ − Q² = 4n), so it is an
ES^{(S)} point. Even Q: the bijection fails (as it must, h ≡ −Q² ≡ 0 (4)); the doc correctly restricts to Q odd.
Symbolically (`review_l3_symbolic.py`) all five §6 Ptolemy relations and the identity hold in ℚ(n, Q, h); the torus
element (α, α⁻¹, α, α⁻¹, α) fixes the four unit sides, h, h′, and scales (c, m, s, N) by (α², α⁻², α², α²) — DK 8.3 with
α² = a (which is HJ_DEEP Lemma 2.3's map); the Q-side-tangent torus has λ₁₄ ↦ h/Q², N ↦ f₁²Q²n as stated.

**§7.6** (`uv run --with sympy python scripts/review_l3_chain.py 400`, < 1 s). My own enumeration of all ES solutions of
primes 5 ≤ p < 400 gives 1 615 Type I and 641 Type II (unordered), matching. *With the definition as printed*
(b_i | b_{i−1} + b_{i+1} only) I get 498/1615 and 298/641 chains and failures only at 13, 37, 97, 181, 193. Adding
gcd(b₀, b₁) = 1 (needed for a unimodular Farey chain) reproduces the author's 358/1615, 242/641 and failure list
13, 37, 97, 181, 193, 277, 373 exactly. See D5.

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

**D4 (MINOR, attribution; §6 "This is the fixed-modulus-4 shot", and "the ES^{(S)} shape of UNIT_ORBIT_ES").** The §6
family is "4n + Q² has a divisor ≡ 3 (mod 4)", the Q-twist of FMS's 4p + 1 shot (Q = 1: m = 4, d = j = 1). UNIT_ORBIT_ES
Prop 2.1's ES^{(S)} family is a *different* one, "n + 4Q² has a prime factor ≡ 3 (mod 4)" (at Q = 1 the p + 4 shot,
c = d = 1). Both have fixed modulus 4 and both are T1-tight at n = M² (4M² + Q² and M² + 4Q² are sums of two coprime
squares), but "the" fixed-modulus-4 shot reads as if §6 recovered UNIT_ORBIT's mechanism. Also, ES^{(S)} membership
needs gcd(n, 2Q) = 1 (UNIT_ORBIT's definition), which §6 does not state; given it, gcd(cn, Q) = 1 follows (q | Q, q | c ⇒
q | h ⇒ q | 4n). *Repair:* say "a fixed-modulus-4 ES^{(S)} family (the Q-twist of the 4p + 1 shot; UNIT_ORBIT Prop 2.1's
n + 4Q² family is a different one)", and add the hypothesis gcd(n, 2Q) = 1 with the one-line gcd argument.

**D5 (MINOR, definition does not match the census; §7.6).** The printed definition of a Farey-chain certificate,
"4/p = Σ 1/(b_ib_{i+1}) with b_i | b_{i−1} + b_{i+1}", omits coprimality. With it literally, 277 and 373 *do* have
chains, e.g. 4/277 = 1/72 + 1/2216 + 1/9972 with (b₀, b₁, b₂, b₃) = (554, 18, 4, 554) (18 | 558, 4 | 572), and the census
becomes 498/1615, 298/641 with failures only 13, 37, 97, 181, 193. The author's numbers are reproduced exactly with
gcd(b₀, b₁) = 1 added (which is what "Farey chain" needs; then gcd(b₁, b₂) = gcd(b₂, b₃) = 1 follow from the
divisibilities). Also, the "/tmp probe recorded here" is not reproducible from the repo. *Repair:* add "gcd(b₀, b₁) = 1
(a unimodular Farey chain)" to the definition and point to `scripts/review_l3_chain.py` (or commit the probe).

**D6 (MAJOR-presentational, stale retracted claim; §5 paragraph "The four '3's", line ≈165).** It still lists "the three CF
steps before the cusp −1/m (a Farey path on g_{μ_c})" as one of the four "3"s. §4's own R-self repair says exactly this
placement (cutting sequence of g_{μ_c} in the z-frame, through the Ford horocycle at −1/m) is FALSE (the frame change is
not unimodular; (7, 2, 1, 3, 1) is a counterexample, which I confirmed: the Ford disc at −1/12 lies strictly inside the
semicircle of [4, 92, 7]). The summary therefore re-asserts a refuted geometric statement as part of the headline
unification. *Repair:* replace with "the three CF steps (p₀/q₀, p₁/q₁, p₂/q₂) of √(4μ_c² − 4p) in MARKOFF's coordinates
(x, z_M), ending at the convergent ε_μ (depth 3; depth 1 when j = 1)", and drop "a Farey path on g_{μ_c}" and "before the
cusp −1/m". Also note the "3" is only "3" for j ≥ 2.

**D7 (MINOR; §5 "the tridiagonal path form with diagonal (c, m, s), whose leading/trailing principal minors are the five
cluster variables and N").** The leading minors are c, h, N and the trailing ones s, h′, N; m is the *central* 1×1 minor,
not leading or trailing. *Repair:* "whose contiguous principal minors are c, m, s, h, h′ and N".

**D8 (MINOR; header).** "Status: in progress (O206)" while §8 is a checkpoint verdict. *Repair:* update the status line.

**D9 (MINOR for this doc, IMPORTANT for the campaign's attribution; §5 "Scope/novelty", §2 preamble).** Literature
search (Jina web search + the archived `sources/lit2026/arxiv-2605.04551v2.pdf`, read in full text):
* **Ventas, arXiv:2605.04551 (May 2026), eq. (3) + Thm 2.1 ("sum by pairs") + Prop 2.2** already states: if the *ceiling*
  (= Hirzebruch–Jung) continued fraction of p/(4k) has exactly three terms, then 4k/p = 1/p₀ + 1/(p₀p₁) + 1/(p₁p₂) with
  p₂ = p, the pᵢ being the HJ convergent numerators. This is exactly the **V₁ row** of Thm 2.1 (h′/N = 1/c + 1/(ch) + 1/(hN),
  p₀ = c, p₁ = h, p₂ = N, 4k = h′), i.e. DK Cor 1.2's Type I slice. Ventas also has boundary-word shots (Thm 2.3: divisors
  ≡ 3 (4) of p + i). So "length-3 HJ fraction with numerator ≡ 0 (4) ⇒ ES via convergent telescoping" is in the literature;
  the campaign's novelty audit (reviews/novelty-audit-2026-10c.md) read this abstract only as "heuristic" and did not
  record the overlap with (J)9/DK Cor 1.2. Ventas has nothing on the other four slices, the Jacobi-symbol criterion,
  Ptolemy/friezes or the pencil, so Cor 2.2's five-vertex statement and §4 remain plausibly new.
* Prop 1.1 (continuants = λ-lengths = frieze entries; HJ path = Farey path) is classical: Conway–Coxeter, Penner, and
  explicitly Morier-Genoud–Ovsienko, "Farey boat I" (arXiv:1811.01229, Jahresber. DMV 121 (2019)). Friezes with arbitrary
  boundary values are "frieze patterns with coefficients", Cuntz–Holm–Pagano (Forum Math. Sigma 2020) — the standard
  name for the doc's "A₂ frieze with frozen values (1, 1, 1, 1, N)". (Abstract-level only; I did not read these papers.)
* No hit for frieze/Ptolemy ↔ Erdős–Straus (searches: "Erdős–Straus frieze pattern Ptolemy", "Egyptian fractions frieze
  Conway Coxeter continuants", "Farey graph Egyptian fraction Ford circles").
* In-campaign precursor not cited: **BRAINSTORM/farey_chain_frieze.md (O144)** already reformulates every ES solution as a
  3-step Farey/frieze chain (Lemma C.0, Prop C.1: Type II chain (cp, a, b, cp)), and its Prop C.2 is the census behind
  §7.6. §7.6 should cite it and compare (O144: chain-realisable ⟺ the gcd g is a square).
*Repair:* in §5 replace "no literature search was done" by the three bullets above (Ventas for the V₁ row; Farey boat /
CHP for Prop 1.1 terminology; O144 for chains) and narrow "new" to Cor 2.2's five-vertex/Jacobi statement and Thm 4.1/Cor
4.2's Ptolemy reading. Forward to the DK/(J)9 owner: (J)9's Type I slice should cite Ventas 2026.

**D10 (MINOR, quantifiers/domain; Cor 2.2).** "ES five-slice certificate at N ⟺ a Farey pentagon with four unit sides and
closing side N in which some vertex has opposite diagonal ≡ 0 (mod 4) ⟺ (DK Thm 4.5) the Jacobi symbol (A/N) = −1."
(i) A is unbound; (ii) the middle set includes *formal* pentagons (a letter 1), whose ≡ 0 (mod 4) quiddities also give ES
triples by Thm 2.1 (Thm 2.1 holds for all words — verified) but are not DK five-slice certificates and are not covered by
DK Thm 4.5 (which is for A ∈ L₃(N)). *Repair:* "For N ≡ 1 (4) and an interior word (c, m, s) at N (all letters ≥ 2): some
quiddity of its pentagon is ≡ 0 (4) ⟺ (h′/N) = −1; existentially over interior words this is the five-slice certificate
set. Formal pentagons with a quiddity ≡ 0 (4) give further (boundary, DK §4.2) ES triples." The Type II sentence of Cor 2.2
is correct as stated (I checked dcs = (p + e)/4 = FMS's x and dspj = FMS's z: both reduce to hs = pj + c).
