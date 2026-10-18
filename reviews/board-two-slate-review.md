# R284 — hostile review of O273 (board #2 slate)

Reviewer: R284 (side-agent/review-board-slate). Author branch merged: `side-agent/board-two-slate` @ abd351d7.
Documents: BOARD2_SLATE.md, FORCED_WINDOW.md §8, ZAREMBA_TRANSFER.md §2 attribution note, scripts/z42_*, logs/z42_*.
From-scratch scripts: `scripts/review_r284_*.py` (no code shared with the author's).

## Summary verdicts

| Claim | Verdict |
|---|---|
| (1) ABH transfer λ(p) ≤ (6/π²) L log L + O(L), KNOWN | (in progress) |
| (2) FORCED_WINDOW Thm 8.5 (Lemmas 8.1–8.4) | (in progress) |
| (3) Lemma 3.1/3.2, M(n), Prop 3.3/3.4 (45/(8π²)), Thm 3.5 (45/(32π²)) | (in progress) |
| (4) 8/n zero-law diagnostic to 10⁹ | (in progress) |

## (1) ABH transfer — checked against the source

Source: arXiv:2210.14095v2, downloaded by R284 (PDF + HTML). Verified verbatim:
* Thm 1: for N ≥ 3, 0 < t ≤ (log N)^C, (1/φ(N))·#{a ∈ ℤ_N^* : |S(a/N) − (12/π²) log N log log N| ≥ t log N} ≪_C 1/t
  (two-sided, absolute value present).
* Thm 6: same range, #{a : |D(a/N)| ≥ t log N}/φ(N) ≪_C 1/t (two-sided).
* (5) Barkan–Hickerson: D(a/N) = ((−1)^r − 1)/8 + (1/12)(a/N − (−1)^r[0; a_r, …, a₁] − S_alt) with
  S_alt = Σ_{i=1}^r (−1)^i a_i, hence D = −S_alt/12 + O(1).
* Convention a/N = [0; a₁, …, a_r], a_r > 1, and ℤ_N^* = {1 ≤ a ≤ N, (a, N) = 1}: as the author says.

Re-derivation. Fix C = 1 and an absolute t₀ with both exceptional proportions < 1/4 (legitimate: implied constants depend
only on C; needs t₀ ≤ log p, i.e. p ≥ e^{t₀}, small p go into the O). The good set has > (p−1)/2 elements, so it contains a
non-residue A. Σ_{j even} c_j = (S + S_alt)/2 ≤ ½[(12/π²)L log L + t₀L] + ½[12t₀L + O(1)]. With the campaign's
r(p/A) ≤ 1 + Σ_{i odd} a_i(p/A) and p/A = [a₀; a₁, …] ⇔ A/p = [0; a₀, a₁, …] (odd digits of p/A = even digits of A/p),
λ(p) ≤ (6/π²) L log L + O(L). Correct. The "typical constant" remark (most QNR have r = (6/π²)L log L + O_t(L)) also
follows, using the lower tail of Thm 1, Thm 6, and r ≥ Σ_even (see numerics: δ ≤ 1); exceptional proportion among QNR is
≤ 2× that among ℤ_p^*. Fine.

From-scratch numerics (`scripts/review_r284_abh.py`, all QNR at p = 1009, 1013, 10007, 10009, 100003, 100049, 1000003):
δ := 1 + Σ_even c_j(A/p) − r(p/A) ∈ {0, 1} always; max |S_alt + 12 D| = 2.82, 2.94, 2.93, 2.98 (exact Dedekind sums,
p ≤ 10009); median r = 10, 11, 15, 15, 20, 20, 25 vs (6/π²)L log L = 8.1, 8.1, 12.4, 12.4, 17.1, 17.1, 22.1.
Reproduces the author's numbers.

**Verdict (1): SOUND.** Label KNOWN (corollary of ABH) is right. Minor wording only:
* m1 (MINOR) ZAREMBA_TRANSFER note says "read in v2 HTML", BOARD2_SLATE (1) says "Read arXiv:2210.14095v2 myself" — harmless;
  both v2 PDF and HTML agree on Thms 1, 6, (5).
* m2 (MINOR) The ZAREMBA note's "Argon route … would give only an o(L log L) remainder, weaker than ABH's O(L)" is an
  unsupported guess about an unwritten proof; it is already labelled CONJECTURE-level sketch, acceptable.

## (2) FORCED_WINDOW §8, Theorem 8.5 — checked against Henriot's erratum

Sources read by R284: `sources/henriot-erratum-2014.pdf` (New Theorem 5, (0·1)–(0·2), the three corrections) and
`sources/henriot-1102.1643.pdf` §2–3 (definitions ‖Q‖, κ, ρ̂_R (2.8), (2.9), Stewart (2.6), class M_k (2.10)).

**Hypotheses of New Thm 5, item by item.** Q₁ = t, Q₂ = 4t − q are each primitive (erratum requires each Q_i primitive;
original only Q) ✓; Q = 4t² − qt, g = 2, r = 2, R_i = Q_i, γ = 1, so F̃ = F ✓; ‖Q‖ = sum of |coefficients| = 4 + q ✓;
α = δ = 1/2 ∈ (0, 1] ✓; x = (X + q)/4, y = X/4: x^{1/2} < y ≤ x ✓, x ≥ C₀(4 + q)^{1/2} for q ≤ X^{1/4} ✓. F ∈ M₂(1, 1, ε)
by (2.10) with A = B = 1: F(a₁b₁, a₂b₂) = f(a₁)f(b₁)1[P⁻(a₂)>√x]1[P⁻(b₂)>√x] ≤ F(b₁, b₂) when (a₁a₂, b₁b₂) = 1 ✓ (f
multiplicative needs only (a₁, b₁) = 1). F may depend on x and χ: the implied constant depends only on g, α, δ, A, B ✓.
Erratum changes: ρ̆_R ≤ ρ̂_R (upper bound only helped) ✓; sub-multiplicativity fix in Lemmas 2–3 does not alter the
statement ✓; D* → a*D* only in Thm 6 / Cors 1–2, not used ✓.

**Application.** p ∈ (X, 2X], p ≡ 1 (8), q ≡ 3 (8) ⇒ p + q ≡ 4 (8), K_q odd; q ∤ K_q since q < p; n = K_q ∈ (x, x + y];
F(Q₁(n), Q₂(n)) = G_χ(K_q)·1[P⁻(p) > √x] = G_χ(K_q) ✓. ρ(ℓ) = 2 (ℓ ∤ 2q), ρ(q) = 1 ✓.

**Local factors — re-derived and brute-forced** (`scripts/review_r284_window.py` part (b): exact counts of
#{n mod lcm(ℓ^{a+1}, ℓ^{b+1}) : ℓ^a ∥ n, ℓ^b ∥ 4n − q} for q ∈ {3, 11, 19}, ℓ ≤ 19, a, b ≤ 4). For ℓ ∤ 2q: mixed (a, b ≥ 1)
terms vanish, ρ̂(ℓ^a, 1)/ℓ^{a+1} = (ℓ−1)/ℓ^{a+1}, Σ_{a≥1} = 1/ℓ exactly, so E_ℓ = 1 + g_χ(ℓ)/ℓ + 1[ℓ > √x]/ℓ ✓. ℓ = 2: only
(a, 0) terms, E₂ = 3/2 ≤ 2 ✓. ℓ = q: mixed terms do occur (e.g. (1, 1) → (q−2)/q², (1, b) → (q−1)/q^{b+1}); the Stewart
bound ρ*(q^ν) ≤ 2q^{⌊ν/2⌋} gives each ≤ 2q^{−⌈ν/2⌉} and E_q ≤ 1 + Σ_ν 2(ν+1)3^{−ν/2} = O(1) ✓ (actually F(·, q^b) = 0 for
b ≥ 1 since q < √x, so only the (a, 0) column survives; the author's bound is valid but not needed).
Collecting: y·(log x)^{−2}·exp(log log x − Σ(1 − g)/ℓ + O(1)) ✓; passing x → X costs O(1) ✓.

**Lemma 8.2** re-derived (E(1 + 2Re ζ)² = 1 + 4E Re ζ + 4E Re²ζ = 3 for d ≥ 3; real χ gives exactly 2/3) and checked for
all χ ≠ 1 mod every prime q ≤ 400: max mean = 0.666667 (attained exactly by the quadratic character) ✓.

**Lemma 8.4.** For t ≥ w = exp(L^η), (log t)^A ≥ L^{α+η} ≥ 2L^α once L^η ≥ 2 ✓; SW error after partial summation
∫_{L^η}^{L} e^{−c√u} du ≪ L^{η/2}e^{−cL^{η/2}}, times φ(q) ≤ 2L^α classes: o(1) ✓; main term
Σ_a (1 − g(a))(1 − η)log L/φ(q) ≥ (1 − η)(log L)/3 by Lemma 8.2 ✓. Ineffective (Siegel) — label says so ✓.

**Theorem 8.5.** η = 3ε: (X/L)·L^{−(1−3ε)/3} = X/L^{4/3−ε} ✓, uniformly in q ≤ 2L^α ✓. Markov over ≤ 2L^α primes q and
≤ 2L^α characters: X/L^{4/3−2α−ε} ✓. The statement is true for every α, ε (only non-trivial when 2α + ε < 1/3) ✓.
Constants depend on α, ε only ✓ (no hidden q- or χ-dependence: Lemma 8.3's constant is absolute, Lemma 8.4's is O_{α,η}).
**Lemma 8.1** re-derived (orthogonality count = (3^k/(q−1))(1 + Σ_{χ≠1} χ(−1)A_χ), real; u ≡ −v (q); M = pK(u+v)/q ∈ ℤ;
y = M/u, z = M/v ∈ ℤ, y ≠ z since (u, v) = 1 and q ∤ 2) ✓.

**Numerics, from scratch** (part (c): all primes p ≡ 1 (8) in [10⁶, 1.01·10⁶) × q ≡ 3 (8), q < 60 = 990 windows): the
exact signed-exponent count agrees with the orthogonality formula in every window; strict certificate at 269 windows
(author: 160 + 109 = 269 ✓), 0 certificate-but-no-solution, and every solution passes 4/p = 1/K + 1/y + 1/z in exact
rationals. **Strictness note confirmed and sharpened:** S = Σ_{χ≠1} G_χ = 1 exactly occurs at **72/990** windows and in
every one of them the count is **0** (e.g. p = 1 000 121, q = 11, K = 7·23·1553: count 0). Typical ties: q = 3 with all
prime factors of K ≡ 1 (mod 3) (the only χ is quadratic, G = 1). So "≤ 1" would be false, not merely unproved; the
document's strict "< 1" is correct.

**Value/priority (8.6).** "q = 3 alone ⇒ ≪ X/L^{3/2} exceptions": the q = 3 certificate fails iff every prime factor of
(p+3)/4 is ≡ 1 (3) (re-derived), and Lemma 8.3's proof with f = 1[ℓ ≡ 1 (3)] gives X/L^{3/2} ✓. Domination claim correct.
Elsholtz–Tao Thm 1.8 proof detail: not re-checked against the paper (source not in sources/; not load-bearing).

**Verdict (2): SOUND.** Label "PROVED modulo Henriot 2014 New Thm 5 + SW + Mertens; ineffective" is accurate.
* m3 (MINOR) FORCED_WINDOW Lemma 8.3 proof, ℓ = q: could note that F(·, q^b) = 0 for b ≥ 1 (q < √x), so E_q ≤ 1 + 1/q
  trivially; the Stewart route is correct but unnecessary.
* m4 (MINOR) §8.7 / BOARD2 (2): say how often ties occur (72/990 here) and that at a tie the count was 0 every time —
  makes the strictness remark concrete.

## (3) Five-slice union: Lemmas 3.1–3.2, M(n), Props 3.3–3.4, Theorem 3.5

**Lemma 3.1** re-derived: n = tuv − u − v ⇒ v(tu − 1) = n + u ⇒ (A/n)(v/n) = (u/n) ⇒ (A/n) = (uv/n) when (uv, n) = 1 ✓.
The prime restriction (21/8 counterexample) is correctly recorded ✓.

**Lemma 3.2** re-derived independently. At a hit n ≡ a (mod w), n ≡ 1 (4) ⇒ (w/n) = (n/w) = (a/w) ✓. Odd–odd:
(−v/u)(−u/v) = (−1/u)(−1/v)(−1)^{(u−1)(v−1)/4}: values on (u, v) mod 4 = (1,1): +1, (1,3), (3,1), (3,3): −1 ✓. u = 2^k u′:
(a/u′) = (−v/u′), (a/v) = (−1/v)(2/v)^k(u′/v), reciprocity ✓. k ≥ 2: 4 | n + v ⇒ v ≡ 3 (4) ⇒ ε = −(2/n)^k(2/v)^k; k even
trivially −1; k ≥ 3 odd: 8 | u ⇒ n ≡ −v (8) ⇒ (2/n) = (2/−v) = (2/v) ✓ (the author's flagged "odd k ≥ 3" point is fine).
From scratch (`scripts/review_r284_five_slice.py lemma 4000 64`): all n ≡ 1 (4) ≤ 4000, all coprime u, v ≤ 64 with k ≥ 2 and
2^k | n + u + v (269 000 triples): (2/n)^k(a/w) = −1 always ✓. At every hit of all **1 473** primes p ≡ 1 (4) in
[10⁶, 1.04·10⁶) (`hits` mode, hit enumeration v | p + u, independent of the author's loop): ε formula = (uv/p) and
Thm 4.5 five conditions ⟺ (uv/p) = −1, **0 mismatches** in both ✓.

**M(n) and Prop 3.3.** Re-derived the mean-preservation: with s := (n/w) = ±1 (balanced over reduced n mod w when
w ≠ □), the term is 1[2^k | n+u+v](1 + s(a/w))(1 − (2/n)^k s)/(2φ(w)); averaging over s gives (1 − ε)/(2φ(w)) =
1[ε = −1]/φ(w) ✓; for ε = +1 the product (1 + s(a/w))(1 − s(a/w)) = 0 identically ✓; for ε = −1 it equals 1 − (uv/n) ✓.
T1: (uv/m²) = 1 and, for w = □, ε = (2/m²)^k·1 = +1 ✓. Numerics from scratch (first-principles vectorised formula, not
Lemma 3.2's case split): M(p), M₀(p) and the four M₀ sectors at p = 1 000 033 agree **to all printed digits** with the
author's log (R = 92, M = 82.729, M₀ = 79.694, sectors 16.00 / 24.08 / 24.55 / 15.07); squares 49², 99², 105², 997²:
R = M = 0, M₀ = 13.650, 10.642, 5.003, 82.425 ✓; p = 61 (w = 9 square-odd-part repair): M = 6.922, R = 6.

**Prop 3.4 (45/(8π²)) — re-derived.** Local factor of Σ 2^{ω(m)}/(φ(m)m^s) times (1 − p^{−1})² is 1 + 1/p², so
Σ_{m ≤ x odd} 2^{ω(m)}/φ(m) ∼ ½·¼·∏_{p>2}(1 + p^{−2})·log²x = ½·¼·(12/π²) log²x = (3/(2π²)) log²x ✓ (numerically: fit to
2·10⁷ gives a = 0.15179 vs 0.15198 ✓). 2^{ω(m)} counts ordered coprime factorisations ✓. Sectors: odd–odd ¾ of classes
→ 9/(8π²); k = 1: half the (u′ mod 4, v mod 8) classes **for every p** (the sign function (−1/u′)(2/v)(−1/v)^{1+[u′≡3]} is
balanced), × 2 orientations → 3/(2π²); k = 2: v ≡ 3 (4), × 2 → 3/(2π²); k ≥ 3: P(v ≡ −p mod 2^k | v odd) = 2^{1−k},
Σ_{k≥3} = ½, × 2 → 3/(2π²). Total 45/(8π²) ✓; the board's 33/(8π²) indeed drops one of the three opposite-parity
sectors. M₀(p) ∼ (45/(8π²))L² holds for each p individually (not only on average over p mod 8); only the lower-order
terms depend on p mod 2^k (e.g. k = 1 sector 24.08 at p ≡ 1 (8) vs 27.60 at p ≡ 5 (8) near 10⁶). The label
"Assessment + EVIDENCE" is if anything conservative; the computation above is a routine Dirichlet-series argument.

**Theorem 3.5 — the two flagged steps re-derived.**
*Density scaling.* Σ_{m ≤ T₀, m ∈ S′} 1/m = D log T₀ + O(2^j) (each of the ≤ 2^j classes mod 2^j contributes
2^{−j} log T₀ + O(1)) — trivially correct; O(2^j) is O_K(1) for fixed K ✓. The tail: m = c + 2^j i ⇒ χ(m) = χ(2^j)χ(i + c′)
with c′ ≡ c·2^{−j} (mod p), an interval of length ≍ s/2^j ≥ p^{1/4+ε}; Burgess (prime modulus, any interval, r large)
gives ≪ s p^{−η} uniformly in the start, so the partial-summation tail is o(1) uniformly in d | u′ and in the class ✓.
*Constants.* Σ_{u′ ≤ X odd} φ(u′)/u′² ∼ ½·(8/π²) log X = (4/π²) log X; Σ φ(u′) log u′/u′² ∼ (2/π²) log²X;
Σ ψ(u′)/u′² ∼ ½·(12/π²) log X = (6/π²) log X (κ(u′) := Σ_{d|u′}|μ(d)|/d) ✓. Main D(L²/π²)(4δ − 2δ²) and character part
≤ D(L²/π²)·6βδ ✓; at δ = ½, β = ¼: ¾ ✓; PV: max_δ(δ − 2δ²) = ⅛ at δ = ¼ ✓ ⇒ 15/(64π²) ✓. The Möbius remainder
Σ_{d|u′} μ(d) log d/d contributes O(L) after weighting ✓.
*Families.* Active-class sets: k = 1: for fixed u′, 2 of the 4 odd classes mod 8 (D = ¼, both u′ mod 4) ✓; k = 2: D = ¼ ✓;
k ≥ 3: D = 2^{−k} ✓. σ_{u′} = χ(2^k u′) constant in v ✓. Disjointness ✓ (u′ determined by the pair; orientations by
parity; odd–odd only one orientation, avoiding double count of short–short pairs). Cutoff 2^{k+1}u′v ≤ p ⇒ (u, v) ∈ P(p) ✓.
The comparison c ≥ (1 − χ(uv))/(u′v) fails only for w = □; such pairs are inactive for k = 0 and k even (k = 2 forces
v ≡ 3 (4), impossible for v = □), so only odd k at p ≡ 5 (8), total ≪ Σ_m 2^{ω(m)}/m² = O(1) per k ✓.
Arithmetic: 3 sectors × 2 orientations × (¼)(¾)/π² = 36/(32π²), odd–odd (¼ + ½)·½·¾/π² = 9/(32π²) ✓ ⇒ 45/(32π²).

**Numerics.** From-scratch R over all 1 473 primes p ≡ 1 (4) in [10⁶, 1.04·10⁶): mean R/L² = **0.4702**, min R = 26
(author 0.472 / 26 on a 1-in-3 subsample) ✓. p = 10 000 121: R/L² = 0.493, M/L² = 0.491 ✓. 8/131 and 8/241 have no
solution, 4/241 has 8 (independent brute force, `scripts/review_r284_egypt.py`) ✓.

**Verdict (3): SOUND.** Lemma 3.1 (primes), Lemma 3.2, Prop 3.3, Prop 3.4's constant 45/(8π²), Thm 3.5 (45/(32π²),
15/(64π²)) all re-derived; the board's 33/(8π²) is correctly superseded.
* m5 (MINOR) BOARD2_SLATE (3) Numerics/Setting: "491 primes ≡ 1 (4) in [10⁶, 1.04·10⁶)" is every 3rd such prime
  (z42_five_slice -r … step 3; there are 1 473). Say "every third prime"; the full-range mean is 0.470.
* m6 (MINOR) Thm 3.5 template: "κ(u′)" is used without definition in BOARD2_SLATE; define κ(u′) := ∏_{ℓ|u′}(1 + 1/ℓ)
  (= Σ_{d|u′}|μ(d)|/d), and note the O(2^j) = O_K(1) initial-segment constant explicitly (it is why K is fixed first).
* m7 (MINOR) Prop 3.4: add that M₀(p) ∼ (45/(8π²))L² holds for each p (only lower-order terms depend on p mod 2^k),
  which is the form Thm 3.5's comparison "¼ of the principal constant" implicitly uses.
