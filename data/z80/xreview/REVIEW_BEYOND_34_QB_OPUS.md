# Hostile cross-lab review: Theorem QB, `notes/z80/BEYOND_34.md` §§10–11 (commit a313c48f7)

Reviewer: Claude Opus (Anthropic). Author: GPT-6.2 Astra lane. Scope: all of `git log main..` (850a05506, bab4cf1cc,
a313c48f7). The focus is the new Theorem QB, which the earlier review (`REVIEW_BEYOND_34_OPUS.md`, at 850a05506) did
not cover. That earlier audit is **not** treated as endorsing QB. I worked from these sources:
* Maynard, arXiv:2006.06572v2, Thm 1.1, read literally in `data/z80/lit/maynard_scratch.txt` ll. 105–125, and cross-checked
  against `sources/lit2026f/maynard-2006.06572-excerpt.txt`;
* Thorner–Zaman, arXiv:1803.02823v3, Thm 1.4 and (1.4), in `data/z80/lit/tz_scratch.txt`;
* the GRH smooth explicit formula in `notes/z78/ANALYTIC_WILD.md` §4;
* the cap definition in `EXPONENT_CAP.md` Def 1.1 and `CAP_POINTWISE.md` l. 8, and the archimedean wall and coverage
  barriers in `EXPONENT_CAP.md` Thm 2.1, Cor 2.2 and Prop 3.1;
* the planted and free carriers and the radical reduction in `notes/z75/ANALYTIC_BREAK.md` §§1, 4, 4a;
* FRONTIER §5.3 (the e* bullet) and §5.4 (cap implications, l. 1345).

No master files were edited and nothing was committed.

## Outcome

**I accept QB in substance. I found no decisive obstruction and no mathematical gap.** Concretely, for each fixed ε > 0,
log(1 + e*(n)) ≪_ε (log R)^ε unconditionally, and ≪_ε (log₂R)^ε on Dirichlet GRH alone, for the capped relaxation of
`EXPONENT_CAP.md`. I re-derived every inequality, quantifier, congruence and valuation. I also replayed the lane's
script and ran two independent exact or modular checks (§5).

Fixes are required before promotion, but they concern form, scope and labels, not mathematics. The most important
one: **QB is ineffective, because Maynard's ≪_{a,ε,A} relies on Siegel–Walfisz.** The STATUS delta must therefore
*keep* the effective z75 bound e* ≤ exp(C√(log R·log log 3R)) as the best effective result, not replace it (R1 below).

None of this touches ES, cap zero, bounded cap, or the integral divisor problem. The note says so correctly.

## 1. The cap definition the proof must meet

e*(n) = min{e : ES^{(y,e)}(n)}. Here 4/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0} and z ∈ ℚ_{>0}, and every prime ℓ with
v_ℓ(z) < 0 must satisfy all of: ℓ ∤ 2n, ℓ | y, v_ℓ(z) even, v_ℓ(z) ≥ −2e. There is **no height condition on x, y, z or
on the window**. QB's packet is
(x, y, z) = (K′, RA₀, RK′A₀/d₁), with K′ = (R+qb)/4, d₁ = K′·g^{L_o}·∏v_i^{2La_i}, A₀ = (K′+d₁)/(qb).
It is then scaled by n/R.

* **Identity.** RA₀ + K′ + d₁ = A₀(R+qb) = 4K′A₀. ✓
* **Denominator support.** Every prime of d₁ divides K′: this covers g, the prime 3, and each v_i. K′ is odd and
  coprime to qbR, hence to 2n. ✓
* **Valuations.** For p | K′ with c = v_p(K′) and w = v_p(d₁) > c, we have v_p(K′+d₁) = c (because v_p(qb) = 0), so
  v_p(A₀) = c ≥ 1 and p | y. ✓ Also v_p(z) = 2c − w, and
  w − 2c = L_o·v_p(g) + 2L·a_p − c ≡ v_p(g) − c ≡ 0 (mod 2). This uses that L_o is odd and that v_p(g) ≡ c (mod 2),
  which includes p = 3, where v_3(g) = 2δ + (c mod 4). ✓
* **Cap.** e ≤ (5L_o + 2L)/2, because v_p(g) ≤ 5 and a_p ∈ {0,1}. ✓
* **Scaling.** Scaling by n/R multiplies the three denominators by an integer whose primes divide R. These primes are
  coprime to den(z), so the reduced denominator of z and the condition ℓ | y are preserved. ✓
* **Integrality.** R ≡ 1 (8) and qb ≡ 3 (8), so K′ is odd. q ≡ −1 (3), b ≡ 1 (3) and R ≡ 1 (3) give 3 | K′. This is
  needed when δ = 1: otherwise 3^{2δL_o} would sit at a prime not dividing y. That is exactly why R ≡ 2 (3) is split
  off. ✓

## 2. Step audit of §10

**Case split (complete).**
* If R is not hard, some prime factor is not 1 mod 8, so there is an integral ES solution (z75 §4a) and e* = 0.
* If R ≡ 2 (3), then (3/R) = (R/3) = −1. The planted carrier at s = 3 (q′ ≡ 3 (4), q′ ≡ 12 − R (9)) gives v_3(K) = 1
  and (3/q′) = −(q′/3) = −(−R/3) = −1, so e* ≪ 1. ✓ 3 ∤ R, since R's primes are 1 mod 8.
* If (R/r) = −1 for some synchronised r, z75's planted carrier applies: r ∥ K and (r/q′) = (q′/r) = (−R/r) = −1, since
  r ≡ 1 (4). The cost is log q′ ≪ log r ≪ log y = A log U. ✓
* Otherwise we are in the main branch. I found no missing case.

**Synchronised-prime surplus (Maynard). Correct.**
* *Inclusion–exclusion.* 1_{4d} − 1_{8d} − 1_{12d} + 1_{24d} = 1_{d|r−1}·1_{r≡5 (8)}·1_{r≡2 (3)} for primes r > 3,
  with (d, 6) = 1. This equals 1_{r≡5 (24)}·1_{d|r−1}. So everything is at the fixed residue a = 1, which is what
  Maynard's Thm 1.1 needs. ✓
* *Main coefficient.* 1/φ(4d) − 1/φ(8d) − 1/φ(12d) + 1/φ(24d) = (1/2 − 1/4 − 1/4 + 1/8)/φ(d) = 1/(8φ(d)). ✓
* *Maynard conditions*, checked literally (x = y and x = 2y, Q₁ = 48Y₁, Q₂ = 2Y₂). The exponents of Q₁Q₂², Q₁¹²Q₂⁷ and
  Q₁²⁰Q₂¹⁹ are .03 + .95 = .980, .36 + 3.325 = 3.685 and .60 + 9.025 = 9.625. These sit below 1, 4 and 10 with fixed
  slack, so 100ε′ ≈ 10⁻³ works. ✓
* *Reduction to Maynard's sum.* For each fixed j ∈ {4, 8, 12, 24}, the map (d₁, d₂) ↦ (jd₁, d₂) is injective, so the sum
  over our pairs is dominated by Maynard's full double sum. No coprimality of q₁, q₂ is needed. ✓
* *Absolute-value budget.* The main term is ≫ ρ(600/ε)·ρ(9500/ε)·y/log y. The ratios are
  log Y_i/log z = 0.03·10⁴/(ε/2) and 0.475·10⁴/(ε/2), both fixed for fixed ε, so Dickman's asymptotic applies. The
  error is O_{ε,A′}(y/(log y)^{A′}), which is smaller for large y. ✓
  (Debate point: this budget is also *why* z = U^{ε/2} is essentially optimal for the method. A log-power error cannot
  absorb a smooth-number density ρ(u) that is U^{−c}. So pushing to a polylog-in-U exponent would need power-saving
  level > 1/2, or some other way to synchronise r − 1. This is not a flaw.)
* *Pigeonhole.* t₀ ≤ 2y/(Y₁Y₂) = 2y^{.495}. Some t₀ carries ≫ y^{.505}/log y triples, and for fixed t₀ each r arises
  ≤ τ(d) = y^{o(1)} times. So there are ≥ y^{.504} distinct r. ✓ r − 1 = t₀d₁d₂ | t₀L₀² = L, and
  log L ≤ 2.1z + log(2y) ≪ U^{ε/2} + log U. ✓

**Colour before q (no circularity).** The colour is s_r = (R/4)^{(r−1)/4} ∈ {±1}, which depends only on (R, r). Keeping
the larger class gives P ≥ y^{.504}/2 ≥ y^{.503}. δ is fixed by 3^{(r−1)/2} = (3/r) = (r/3) = (2/3) = −1. ✓ Neither q,
b nor g enters.

**The window prime q.** The conditions are q ≡ 3 (8), q ≡ −1 mod every odd p | 3L, and (q/R) = −1.
* *(L, Q) = 1.* Q = (q−1)/2 is odd, and p ∤ q − 1 for every odd p | L. ✓
* *Shared primes.* If G = (R, D₀) > 1, then χ_G is constant (= 1) on the forced class, since q ≡ −1 and p ≡ 1 (4).
  R ∤ D₀ because D₀ < R and R is squarefree. Hence χ_{R/G} is nonprincipal mod R/G, and R/G is coprime to D₀. So the
  expansion of 1_{a (D₀)}(1 − χ_R)/2 has mean 1/(2φ(D₀)) and ℓ¹ norm 1. ✓ The note's sentence is right but terse.
  Please spell out the χ_G-constancy.
* *Unconditional height.* Linnik gives log q ≪ log(RD₀) ≪ log R. ✓
* *GRH height.* X = (log R)²D₀⁴(1+U)¹⁰. The smooth GRH error is O(√X log(RD₀X)) plus prime powers
  O(√X log² X) plus O(log RD₀), against a main term X/(2φ(D₀)). The ratio is ≫ D₀U⁵ → ∞, so log q ≪ log₂R. ✓ This
  is the *smooth* form. With an unsmoothed √X log² error the ratio would be D₀U⁵/log R, which fails, so the smoothing
  is genuinely needed and is correctly cited (z78 §4 l. 73–77).

## 3. Step audit of §11

**Basis v_i after q.** The squares group has odd order Q and (L, Q) = 1, so v ↦ v^{2L} on squares is a bijection. The
target h^{2^i} therefore fixes v² mod q, and we pick one root ≡ 3 (4). ✓
* *Distinctness is automatic.* The values 2^i for 0 ≤ i < k are distinct and < Q, so the targets, and hence the
  classes mod q, are distinct. The note's repetition probability O(k²V^{−.999}) is unnecessary (harmless).
* *List sizes.* TZ Thm 1.4 over ℚ for ℚ(ζ_{4q}) has n_K = 1, D_K = 1 and 𝒬 ≤ 4q. In the harmful-sign case, TZ (1.4) at
  degree 2 gives 1 − β ≫ (4 log D + √D)^{−1}. Since the error in TZ Thm 1.4 is relative to Li − θLi(x^β), each list has
  ≫ V/((4q)² log V) ≥ V^{.999} primes once C ≥ ~2000·C₀. ✓ Under GRH this is used unconditionally too; that is fine.

**Bad conductors (large sieve).** Put S(χ) = Σ_{r∈𝒞} χ(r), and let a_n count the ordered l-tuples with product n
(n ≤ (2y)^l ≤ M²).
* Σa_n² ≤ l!·P^l. ✓
* The primitive large sieve gives Σ_{m≤M} Σ*|S|^{2l} ≤ (N+M²)Σa_n². Markov at |S| > P/2 then bounds the number of bad
  characters by ≤ 2M²(4l/P)^l. ✓
* *Exponent.* With l ≥ 2 log M/log 2y − 1 and log(P/4l) ≥ .502 log 2y (true because .001·log y = 10 log U ≫ log(4l),
  and l ≤ U³), the exponent is ≤ .996 log M + O(log y). At j = 1, log M = CU while log y = A log U, so the bound is
  ≤ M^{.997}. ✓
* The bound holds for an arbitrary subset 𝒞 (energy bound for that subset). So letting 𝒞 depend on R, and on the
  colour, is legitimate. ✓

**Random choice of v_i.** A squarefree m with j prime factors, each ≤ V, has m ≤ V^j. P(m | D′) ≤ (k·V^{−.999})^j by
summing over injections. The union bound over bad characters gives Σ_j V^{.997j}(kV^{−.999})^j = Σ_j (kV^{−.002})^j →
0. ✓ No equidistribution of bad conductors in the lists is used, only |list| ≥ V^{.999}. This is robust: even if every
bad prime lay in the list, the j = 1 term would still be V^{−.002}k. The comparison .997 < .999 is precisely where
level > 1/2 is needed. With BV (θ < 1/2) the large-sieve count is ≥ M^{1+} and cannot be beaten by any list density.
So Maynard is essential, as claimed.

**Even subset products.**
* For nonprincipal ψ mod D′, E[ψ(b) | even] = ∏(1+ψ(r))/2 + ∏(1−ψ(r))/2. This is exact, because P(even) = 1/2. ✓
* |(1±z)/2|² = (1 ± Re z)/2 and log x ≤ x − 1 give each product ≤ exp(−(P ∓ Re S)/4) ≤ e^{−P/8}. ✓
* *Inversion.* Each class has probability ≥ (1 − 2φ(D′)e^{−P/8})/φ(D′) > 0. Here log D′ ≤ kCU = O(U²), while
  P ≥ U^{5030}. ✓
* The relevant ψ are nonprincipal mod D′ with primitive inducer of conductor m | D′, m > 1. That m is a product of chosen
  v_i, hence not bad. ✓

**b after v_i, g last, digits last.**
* b ≡ −R/q (mod D′) puts every v_i in K′. ✓ Even parity gives b ≡ 1 (24). ✓
* g = 3^{2δ}·∏p^{v_p(K′) mod 4} is a square mod r, with g^{(r−1)/4} = −1. (r−1)/4 is odd and divides L_o, and L_o is
  odd, so g^{L_o} ≡ −1 (mod r). This holds **for every b**, because only K′ ≡ R/4 (mod r) is used. ✓
* *At q.* (g/q) = (K′/q) = (R/q) = (q/R) = −1 and (−1/q) = −1, so −g^{L_o} is a square. Its inverse is h^c with
  0 ≤ c < Q ≤ 2^k, written in binary digits. ✓
* *Mod r.* v_i^{2L} ≡ 1 because r − 1 | L. So d₁ ≡ −K′ mod qb, by CRT over the distinct primes q and r | b, with b
  squarefree. ✓
* *Dependency graph.* colour(R, 𝒞) → L → q → lists(q, L) → v_i → b(v_i, q, R, 𝒞) → K′, g → digits(g, q). The graph is
  acyclic, and no later choice feeds an earlier constraint.
* The digits do not need to be known when b is chosen, because *all* v_i are made to divide K′. This is the step I
  would have expected to hide a circularity, and it does not.

**Final bound.** log(1+e*) ≤ max(O(1), O(log y), log L + O(1)) ≪_ε U^{ε/2} + log U. ✓

## 4. Obstructions I tried, all negative

* **Archimedean wall** (EXPONENT_CAP Thm 2.1, Cor 2.2: window ≤ 2nQ₁²(n+Q₁²)). The window qb is astronomically large
  (log b up to y^{.5+}), but so is den z: the overflow at primes of g alone is ≈ g^{L_o}. No contradiction. No height
  is required by the definition.
* **Coverage barrier** (Prop 3.1(c): coverage at a prime window r needs e ≥ (log r)^{1−o(1)}). That statement has
  group order = window = r. Here the group is 𝔽_q^* with log q ≪ U, while e ≈ L ≥ e^{z}, and the mod-b part costs
  nothing. No contradiction. As with z78 §2, this is the decoupled window/group height already flagged in the first
  review.
* **FRONTIER l. 1345** ("GRH alone does not reach (log₂p)^{O(1)} this way"). QB under GRH gives
  e* ≤ exp((log₂R)^ε), which is far weaker than (log₂R)^{O(1)}. It is consistent, and does not supersede the
  Hypothesis W/EQ/S conditionals.
* **Squares** (T1). The packet works at rad(n), where χ_R is nontrivial. For n = m² this is a statement about
  rational-z caps, already covered by z75's all-n bound. There is no Type II claim at squares. ✓
* **Exceptional zeros.** These matter only (a) in the TZ lists, where they are handled by a relative error plus Stark
  at degree 2, and (b) in Linnik's theorem for q, where only the height is needed. Maynard's fixed-residue theorem has
  no exceptional-zero term to worry about at a = 1.
* **Parity, sign and denominator traps.** These are K′ odd (not (R+qb)/8), 3 | K′ when δ = 1, v_p(g) parity at p = 3,
  overflow primes dividing y, and the prime 2. All pass. They are also verified by the checks below.

## 5. Computation (ulimit -v 6000000, single process each)

1. **Replay.** `timeout 600 uv run --offline --no-project python -B scripts/z80_beyond34.py` takes 0.5 s and is
   **byte-identical** to `data/z80/beyond34.txt`. It reports 8266 packets, 18 exact reconstructions, and the binary
   packet at R = 241 with b = 702947178360131601769 and digit {71}.
2. **Independent exact check (mine, `/tmp/qb_check.py`, not committed; 2 min).** Setup: L = 9100, cofactor pool
   {5, 29, 53, 101, 701, 1301}, hard R ≤ 6000 together with 697, 3649 and 113·137, both n = R and n = R·p.
   * Every even same-colour product b is tested, for every admissible q ≤ 400. Binary digits are taken over the primes
     of K′.
   * **154 packets** have the full exact integer identity 4xyz_num = n(…) and the reduced denominator recomputed by gcd.
   * Each denominator prime is checked against the Def 1.1 conditions directly: odd, ∤ n, | y, even exponent, exponent
     equal to (w−2c)⁺.
   * The cap is ≤ (5L_o+2L)/2, and the maximum observed cap/L is 1.625.
3. **Order-faithful check (mine, `/tmp/qb_order_check.py`; 4 s).** This runs QB's order: colour → q → basis v_i fixed
   **before** b (v_i^{2L} = h^{2^i} mod q) → minimal even b by DP hitting −R/q mod D′ → K′, g → digits by discrete log.
   * It verifies d₁ ≡ −K′ mod qb by modular powering.
   * It verifies v_p(K′+d₁) = c by direct computation mod p^{c+2}, without the formula.
   * Result: **15 packets** (q = 11, 15 values of R, both colours, |b| ∈ {4, 6, 8}, 0–2 nonzero digits).
     q = 59 found no hit, as expected at |𝒞| ≤ 20 against |D′| ≈ 10¹⁰.

   This differs from the theorem in one respect: the test restricts 𝒞 to residues r rather than invoking the planted
   branch.

None of these checks the asymptotic inputs (Maynard, the large sieve, TZ); they test the packet and the ordering
algebra.

## 6. Form fixes from the first review: confirmed

* Renaming B/C → P/Q. ✓
* PS exponent 6. ✓
* CLOZ cited as v2. ✓
* The "Jordan shortcut" paragraph has been deleted, and the cryptic heading replaced. ✓
* §0 names the internal TQ/AP2 inputs. ✓
* The Q label is split (Lemmas 5–6 PROVED, §7 GRH). ✓
* "No effective onset" is stated for P. ✓
* The z78 §2 reconciliation appears at the end of §7, and the FRONTIER §6 qualification is in the STATUS delta. ✓
* No master-file edits in the branch. ✓

## 7. Required fixes before promotion (QB)

1. **(Required: effectivity and the STATUS delta.)** Maynard's Thm 1.1 is ≪_{a,ε,A} for every A, which goes through
   Siegel–Walfisz. So QB's onset is **ineffective** unconditionally, not merely "no numerical onset asserted".
   * Write "ineffective" into the QB statement and the §0 label.
   * The proposed "§1B replacement of both pointwise asymptotics" must keep the z75 line "**Unconditional effective**
     e* ≤ exp(C√(log R·log log 3R))" as the best *effective* bound, with QB added as the ineffective asymptotic.
   * Under Dirichlet GRH, Siegel–Walfisz is effective, so the GRH form may be effective in principle. Do not assert
     this without checking Maynard's proof.
2. **(Required: label completeness.)** The §0/QB label should also name these inputs:
   * the internal, unrefereed elementary inputs: z75 §1 planted carrier, the z75 §4a hard-radical and scaling
     reduction, and the Lemma 6 packet;
   * TZ Thm 1.4 together with TZ (1.4)/Stark at degree 2, used for the v_i lists. "Linnik" alone understates this; a
     quantitative Linnik would also do.
3. **(Required: notation.)** In §§10–11, several symbols are reused with different meanings from §§5–7. List them in
   one place or rename them before any master quotes them.
   * U is both the scale log R or log₂R and, in §6 (which §11 relies on), the squares group (𝔽_q^*)².
   * k, j, M, Q and L also differ from their §§5–7 meanings.
4. **(Minor.)**
   * Spell out why χ_R stays nontrivial on the forced class when (R, D₀) > 1 (χ_G is constant there; see §2 above).
   * Drop or annotate the unnecessary repetition probability (the v_i are automatically distinct).
   * State explicitly that log b, the window qb and den z are unbounded in terms of R, and why the EXPONENT_CAP
     Thm 2.1 wall is consistent. This will stop a master-file reader from seeing a contradiction with Cor 2.2 or
     Prop 3.1.
   * In §0, "smaller U CONDITIONAL on Dirichlet GRH" should say that GRH is used **only** for the height of q. The
     Maynard, large sieve and TZ steps stay unconditional.
5. **(Export.)** This is one cross-lab review of a claimed improvement of an *internal* record, so per AGENTS §3 it
   suffices for STATUS §1B. External priority is not established, and the cap relaxation is internal, so no
   publication-type claim should be made.
   * FRONTIER §5.3's e* bullet needs the same rewrite.
   * FRONTIER l. 1345 and open problem 13 stay unchanged.

## 8. Debate and challenge (non-blocking)

* *Is the gain real or bookkeeping?* It is real for this relaxation. The previous √(log R log log R) came from paying a
  Minkowski index or diameter against a single window group. QB pays nothing for the group because a binary basis is
  *planted after* q and inside K′, using the freedom in b. The price moves entirely into the common exponent L of the
  cofactor primes.
* *What would bounded or polylog caps need?* The method's floor is log L. One needs P ≥ y^{1/2+} primes with r − 1 | L
  (forcing τ(L) ≥ y^{1/2+}). One also needs the distribution input to absorb the smooth-modulus density with
  log-power errors. Together these force L ≥ exp(U^{c/log log U}) roughly. Breaking through would need power-saving
  beyond-1/2 equidistribution, or a correction scheme with no common exponent. The note's closing sentence ("dispose
  of the common exponent L") correctly identifies this.
* *Does it say anything about ES?* No. Overflow parity is preserved, while the size of the overflow is huge
  (≈ L·log g). Cap zero remains B2.

**Verdict on the posed question.** Yes, rel. the cited theorems: for each fixed ε > 0, log(1+e*(n)) ≪_ε (log R)^ε
unconditionally (ineffective), and ≪_ε (log₂R)^ε on Dirichlet GRH. I found no decisive obstruction.
