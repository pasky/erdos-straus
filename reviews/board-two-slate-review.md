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
