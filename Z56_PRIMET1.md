# Z56_PRIMET1 — is (★)-hardness a lottery? A pre-registered hunt for a global invariant ("prime T1")

Status: wave z56 lane PRIMET1 (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z56_lanes.md` §5). **ES is OPEN; nothing
here proves or disproves ES or (★).** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
This is an EVIDENCE-level lane. Scripts `scripts/z56_primet1_*`, data `data/z56/primet1/` (large intermediates kept out
of the repo in a scratch directory and regenerable by the exact commands of §7).

*(Checkpoint 1: §§1–3 written and committed BEFORE any association between an invariant and R(p) was computed. Only
engine validation (the 14 known zeros reproduced, timing) had been run at that point. Later amendments are listed in §3.9
with their reasons and their timing relative to outcomes.)*

## 0. Summary (verdict first)
* **Verdict: narrowed — a clean null with power analysis (EVIDENCE).** No global invariant of p predicts (★)-hardness
  beyond the known explanations, at minimal detectable effects of ≈ 0.2 % of E[R] (continuous) and tail OR ≈ 1.1 per SD,
  on 6.7·10⁶ primes p ≡ 1 (24) in [10⁷, 10¹⁰] with exact R(p), plus 25 000 primes at 10¹²–10¹³, the hardest 0.01 % of
  (10⁹, 10¹⁰], the 14 zeros and HC at 10¹².
* **Design.** 16 invariant families pre-registered and committed before any outcome (§3); primary block on a held-out
  split with Holm control; eight dated amendments, each run on data not used before it was written (§3.9).
* **What predicts hardness beyond the pre-registered local model** (§4.1, §4.3–4.4) is always one of:
  * local data (p-adic depth, the small-prime residue pattern n(p), local shadows);
  * L-value main terms: BM, and the genus-layer L(1, χ_{−4p}) ∝ h(−4p), worth ≈ +4.7 % of E[R] per SD given exact BM;
  * near-squares (a₁ of √p);
  * the u = 1 ticket 2τ₃(p + 1).
  Class-group 2-, 3-, 5-parts, h(p), power residuosity of 2 and 3, Frobenius in non-abelian cubic/quartic fields, Hecke
  angles and the Sato–Tate angle are null once local shadows are modelled.
* **One unexplained residual** (A9, fresh data, p_Holm = 0.014): the large-prime structure of p − 1, ≈ +0.5 % of E[R] per
  SD. It is not replicated at 10¹²–10¹³ (same sign, n.s.), so it fails the pre-registered rule. Weak candidate, no mechanism.
* **Invariant-free test (T2T, §4.5).** The disjoint ticket families 4Cp + 1 and p + u are uncorrelated given local data
  (ρ̂ = −0.005, 99 % CI [−0.011, 0.001]), although each is strongly overdispersed. A common hidden multiplier e^H therefore
  has SD(H) ≲ 1.1 % at 10⁸–10⁹ and ≲ 2.5 % at 10¹²–10¹³. A T1-like all-ticket kill would need density ≲ 1.2·10⁻⁴ there.
* **CERTIFIED (this engine).** An independent sieve reproduces exactly the 14 (★)-zeros ≤ 10¹⁰ and finds none in
  (10⁸, 10¹⁰]; min R = 2 in (10⁹, 10¹⁰], at 1 397 190 001 = 37379² + 360.
* **Assessment.** The data look like *local main term × lottery*. A prime T1 would have to:
  * act on a set of density ≲ 10⁻⁴;
  * or act only above 10¹³;
  * or be invisible both to the 17 families and to the T2T coupling test.
  Nothing here bears on a fixed prime (B6). ES remains OPEN.

## 1. The precise statement attacked

Let 𝒫₂₄ := {p prime, p ≡ 1 (mod 24)}; every (★)-zero p ≡ 1 (4) lies in 𝒫₂₄ (PROVED, elementary: `RESIDUE_HARDNESS.md` §0.6).
R(p) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = p} (FRONTIER §2.1; even; R(p) ≥ 1 ⇒ ES(p)).

**Local model.** A *local predictor* is a function of (i) the size of p, (ii) the residues p mod q for prime powers q ≤ Q₀
(Q₀ = 1000; in particular all Legendre symbols (q/p), q ≤ 1000, and divisibility q | p − 1), and (iii) the near-square
distance κ(p) := min(p − ⌊√p⌋², ⌈√p⌉² − p). It contains every known explanation of hardness: M_BM (through
L(1, χ_p)²E(χ_p) truncated to q ≤ Q₀, `BM_LVALUE.md` Thm A), the residue-hardness factor F (`RESIDUE_HARDNESS.md`), the
Mordell classes (p mod 840), and near-squares (FRONTIER §4 item 15).

**Question Q (EVIDENCE-level).** Is there a *global* invariant G(p) — one not determined by (i)–(iii) — such that, conditionally
on the best local predictor, G carries significant information about (a) the standardized residual of R(p), or (b) the
event "p is hard" (lower tail of R(p) relative to its local expectation), or (c) the (★)-zeros?

A "prime T1" (FRONTIER §3 "No BM obstruction", §7.15) would have to be such an invariant, with an effect large enough to
push ≍ (log p)² expected events to 0. A positive answer to Q would be the first sign of a non-lottery mechanism. A
negative answer is reported as a **null with power analysis** (minimal detectable effects), not as a proof of absence.

## 2. Why this is not already closed

* O154 (`BRAINSTORM/z32_prime_T1.md`) and Pass-1 items Z0795/Z1686/Z2930/Z0670 (`ES_CONNECTIONS_TODO.md`) correlated U or f_II
  with h(−4p), regulator, CF period, least non-residue at p ≤ 10³–10⁷, **unresidualised or residualised only against
  Legendre symbols, without held-out testing or multiplicity control**, and on U/f_II rather than R. The known local model
  (F, M_BM, Mordell class, near-squares) was assembled only in z52c–z55, after those screens.
* `BRAINSTORM/z45_prime_t1_dual.md` shows that real sibling failures are mostly budget failures, not character failures;
  it does not test global invariants statistically.
* Z55_CROSSF / BM_CORRECTED §3.2 measure the *shape* of the zero law (Poisson with mild overdispersion) but not whether the
  overdispersion is carried by an identifiable invariant. Overdispersion beyond Poisson is exactly where a hidden
  global variable would show up.
* No closed item of the brief covers a statistical test of non-congruence invariants (class-group 2-/3-parts, Frobenius in
  non-abelian fields, power-residuosity of 2 and 3, Hecke angles, Sato–Tate angles, Pell period) against a residualised
  R(p) at 10⁷–10¹³.

## 3. Pre-registered design (fixed before any outcome was computed)

### 3.1 Data
* **Bulk1:** all p ∈ 𝒫₂₄ ∩ [10⁷, 10⁹] with exact R(p) from the pair sieve `scripts/z56_primet1_rsieve.c` (validated against
  the independent trial-division counter `scripts/z52b_p1_H03_rcount.c` on all p ∈ 𝒫₂₄ ≤ 3·10⁴; reproduces exactly the 14
  known zeros ≤ 10⁸). Split by h(p) := splitmix64(p) mod 4: **D** (h = 0, discovery/fit), **C** (h = 1, confirmation),
  h ∈ {2, 3} reserved (untouched unless a replication of a positive finding is needed).
* **Bulk2:** all p ∈ 𝒫₂₄ ∩ (10⁹, 10¹⁰] with exact R(p) (same sieve). Used for: the census cross-check (zeros ≤ 10¹⁰), the
  extreme-tail test S2, and the height replication S1a.
* **High:** consecutive p ∈ 𝒫₂₄ above 10¹² (target 20 000) and above 10¹³ (target 5 000), exact R(p) from a per-prime
  engine (`scripts/z56_primet1_rone.c`, smallest-coordinate decomposition with factorisation; validated against the sieve
  on ≥ 10⁴ primes ≤ 10⁹). Used for height replication S1b.
* **Zeros:** the 14 (★)-zeros ≤ 10¹⁰ (FRONTIER §2.1) with matched controls (S3); descriptive table also for 193, 2521, 66529
  (b = 1 failures), 3361, 5101441 (FRONTIER §4 item 14).

### 3.2 Local model 𝓛 (fit on D only)
Negative-binomial-type quasi-likelihood GLM, log link, for Y := R/2 (R is even), with covariates:
* size: log L, 1/L (L = log p);
* residues: one-hot p mod 16 (2 classes), p mod 9 (3), p mod 35 (24; contains the Mordell classes), p mod q for the primes
  q ∈ {11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47} (q − 1 classes each);
* BM: τ(p) := E_{Q₀}(χ_p)·L_{Q₀}(1, χ_p)²/(4L²) and τ² (Euler products truncated to primes ≤ Q₀ = 1000);
* F-type: f₁(p) := Σ_{53 ≤ q ≤ 1000, q | p−1} (log q)/q;
* near-square: 1[κ ≤ 16], 1[κ ≤ 128], 1[κ ≤ 1024], log(1 + κ)/L.
Fitted mean μ̂(p) := E[Y | local]; dispersion: NB shape k̂ fitted on D by moments. Pearson residual
r(p) := (Y − μ̂)/√(μ̂ + μ̂²/k̂); mid-PIT u(p) := P(Y′ < Y) + ½P(Y′ = Y), Y′ ~ NB(μ̂, k̂). **Hard** := u(p) < 0.01.

### 3.3 Invariant families (the test list; transforms fixed now)
| id | invariant | features (df) |
|---|---|---|
| G1 | h(−4p) | log(h(−4p)/√p) (1) |
| G2 | 2-part of Cl(−4p) | v₂(h(−4p)) ∈ {2, 3, ≥ 4} one-hot (2) [8 ∣ h ⟺ p = x² + 32y²; governing-field data] |
| G3 | odd part of h(−4p) | 1[3 ∣ h], 1[5 ∣ h] (2) |
| G4 | real class number | 1[h(p) > 1] (1) [quadclassunit; GRH-conditional output] |
| G5 | L(1, χ_p) exact | log L(1, χ_p) − log L_{Q₀}(1, χ_p) (1) [the part of L not seen by q ≤ Q₀] |
| G6 | regulator / Pell | log(R_p/√p) and log(ℓ(√p)/√p), ℓ = CF period length (2) |
| G7 | least QNR n(p) | log n(p) (1) |
| G8 | ord_p(2) | index i₂ = (p−1)/ord_p(2): v₂(i₂) ∈ {1, 2, ≥ 3} one-hot, 1[3 ∣ i₂], log i₂ (4) [2 a 4th/8th power, cubic residue: Frobenius in ℚ(ζ₈, 2^{1/4}), ℚ(ζ₃, 2^{1/3})] |
| G9 | ord_p(3) | same with i₃ (4) |
| G10 | cubic S₃ Frobenius | #roots of x³ − x − 1 mod p ∈ {0, 1, 3} one-hot (2) |
| G11 | quartic S₄ Frobenius | #roots of x⁴ − x − 1 mod p ∈ {0, 1, 2, 4} one-hot (3) |
| G12 | Hecke angles | p = a² + b² (a odd): θ = arg(a + bi): cos 4θ, cos 8θ; p = x² + 3y²: ψ = arg(x + y√−3): cos 6ψ, cos 12ψ (4) |
| G13 | Sato–Tate angle (non-CM) | t = a_p(11a1)/(2√p): t, 4t² − 1 (2) |
| G14 | deeper p-adic depth | v₂(p−1) ∈ {3, 4, 5, ≥ 6} beyond mod 16: 1[v₂ = 5], 1[v₂ ≥ 6]; 1[27 ∣ p−1], 1[25 ∣ p−1], 1[49 ∣ p−1] (5) |
| G15 | Legendre symbols beyond Q₀ | (q/p) for the 10 primes 1009 ≤ q ≤ 1061 (10) |
| G16 | smoothness | log P⁺(p−1)/L, ω(p−1), log P⁺(p+1)/L, ω(p+1) (4) |

(G15 replaces the generic "p mod large smooth moduli": all residues mod q ≤ 1000 are local by definition; G14 tests deeper
prime-power depth of small primes, G15 the first symbols beyond Q₀.)

### 3.4 Primary tests (on C; Holm–Bonferroni over all 32 tests, FWER 0.05)
For each family G with feature matrix X_G (standardised on C):
* **P-cont(G):** OLS of r on [1, log L, X_G] vs [1, log L]; F-test.
* **P-tail(G):** logistic regression of 1[hard] on [1, X_G] vs [1]; likelihood-ratio χ² test.
Effect sizes reported as multiplicative effects on E[Y]: Poisson GLM on C with offset log μ̂, covariates [1, log L, X_G]
(per-SD or per-category exp(β) with 95 % CI), and tail odds ratios.

### 3.5 Secondary tests (each Holm-corrected within its own block)
* **S1 (height replication):** P-cont for all 16 families on (a) a hash-sample of Bulk2 (h(p) mod 64 = 1) and (b) High
  (10¹² and 10¹³ pooled); offset log μ̂ from 𝓛 (extrapolated), with intercept and coefficient on log μ̂ refitted.
* **S2 (extreme tail at 10⁹–10¹⁰):** the hardest 0.01 % of Bulk2 by u(p) (𝓛 refitted on the disjoint hash-sample
  h(p) mod 64 = 2 of Bulk2), each with 3 controls matched on p mod 35, p mod 16 and nearest μ̂; per-family conditional
  logistic (or matched-set permutation) test.
* **S3 (the 14 zeros):** per zero, 50 controls in 𝒫₂₄ with the same p mod 35 and p mod 16, nearest in log p; per family a
  pre-set scalar (G1: log(h/√p); G2: v₂(h); G3: 1[3 ∣ h]; G4: 1[h(p) > 1]; G5: the G5 feature; G6: log(R_p/√p); G7: log n(p);
  G8: v₂(i₂); G9: v₂(i₃); G10: #roots; G11: #roots; G12: cos 4θ; G13: t; G14: v₂(p−1); G15: Σ(q/p); G16: log P⁺(p−1)/L);
  mid-rank percentile; two-sided Fisher combination over the 14 zeros; Holm over 16 families. (Low power; descriptive.)
* **S4 (omnibus, nonlinear):** gradient-boosted regressor (resp. classifier) trained on D-residuals (resp. D-hard) with all
  family features jointly; statistic = out-of-sample R² (resp. AUC) on C; null = 200 row-permutations of the C feature
  matrix.
* **S5 (HC, if usable):** existing HC data `data/z53/hchyp/stat_1e12_X2048.txt.hc` (20 000 primes near 10¹²): logistic of
  1[HC above its 99th percentile] on each family (restricted to p ≡ 1 (24) if the sample allows), Holm within S5.

### 3.6 Positive controls and power (not part of the Holm family)
* **PC1:** refit 𝓛 without the p mod 13 one-hot; the pipeline must detect "p mod 13" (12 df) in P-cont and P-tail on C.
* **PC2 (planted signal):** replace Y on C by NB(μ̂·e^{βZ}, k̂) draws with Z a balanced random binary, β on a grid; report
  the detection rate at the Holm-adjusted level → empirical minimal detectable effect (MDE). Also analytic MDE for
  P-cont and P-tail.
* **T1 control:** odd squares m² ≡ 1 (24), gcd(m, 6) = 1: R(m²) = 0 with the gcd condition in the per-prime engine.

### 3.7 Decision rule (fixed now)
A family is a **candidate non-lottery signal** iff it is Holm-significant in the primary block AND its effect has the same
sign with nominal p < 0.05 in S1, AND it survives refitting 𝓛 with Q₀ raised to 2000 for the residue/Legendre features (to
exclude "a slightly larger local model explains it"). Otherwise: report a null with MDEs. Any signal is EVIDENCE only.

### 3.8 What a positive result would and would not mean
A significant global invariant would show that hardness is not purely local + lottery, but it would not by itself give a
disproof shape: a prime T1 must push the expected count to zero, i.e. an effect of order e^{−Θ(log² p)} on P(R = 0), not a
few percent on E[R]. Conversely, a null bounds only effects above the MDEs at the tested heights.

### 3.9 Amendments (dated relative to outcomes)
**Amendment 1 (written after seeing the primary results on C, §4.1; BEFORE any computation on the reserve split
h(p) = 2).** The primary block flagged 11 of 16 families (§4.1). The effect table shows three things the pre-registered
local model 𝓛 does not contain although they are *known or mechanical* explanations: (a) 𝓛 used L(1, χ_p) truncated
at Q₀, whereas the known M_BM uses the exact L-value; (b) 𝓛 has p mod 16, 9, 35 but not the deeper prime powers
(p mod 64, 27, 25, 49 — local by the §1 definition); (c) R contains the u = 1 / B = 1 slice, which is exactly
2τ₃(p + 1), τ₃(n) := #{m ∣ n : m ≡ 3 (mod 4)} — a ticket count, so any factorisation statistic of p + 1 is partly the
outcome itself. In addition G6 (regulator vs period) looks like a near-square effect that 𝓛's crude κ-features miss,
extended to rational approximations x/y of √p (generalised near-squares). So, on the **untouched reserve h = 2**:
* 𝓛⁺ := 𝓛 design + exact τ_ex := E_{Q₀}(χ_p)L(1, χ_p)²/(4L²) (L(1, χ_p) = 2h(p) log ε_p/√p), τ_ex², one-hot p mod 64, 27, 25,
  49 (collinear columns handled by pseudo-inverse). All tests below use 𝓛⁺ as an *in-sample regression null* on h = 2 (the
  residual r and the hard flag still come from the D-fitted 𝓛).
* **A1(G), A2(G)** for G1–G16: OLS F-test of r on [𝓛⁺, X_G] vs [𝓛⁺]; logistic score test of 1[hard] on [𝓛⁺, X_G] vs [𝓛⁺].
* **A3:** new family **G17** (generalised near-square): with a_i the partial quotients of √p and q_i the convergent
  denominators, Γ(p) := max{log a_{i+1} : i ≥ 1, q_i ≤ 1000}/L and log(a₁)/L (2 features); tests: G17 cont/tail
  with null 𝓛⁺; G6 cont/tail with null [𝓛⁺, G17] (does G17 absorb G6?).
* **A4:** G16 cont/tail with null [𝓛⁺, τ₃(p+1), log(1 + τ₃(p+1))] (is the p ± 1 signal the u = 1 ticket?).
* Holm over the whole A-block (16 + 16 + 4 + 2 = 38 tests), FWER 0.05. A family is a candidate non-lottery signal iff it is
  Holm-significant here AND sign-consistent in S1 (nominal p < 0.05). G17 by construction is a near-square variant: if
  significant it is reported as an *extension of the known near-square explanation*, not as a prime T1, unless its
  effect on the zero/tail rate is of the size §3.8 requires.

**Amendment 2 (written after an exploratory run of the Amendment-1 battery on C itself — already-seen data — and
BEFORE any computation on h = 2).** The exploratory C run (`data/z56/primet1/amendC_*`) showed: (i) with the exact BM
term in the null, G1 (h(−4p)) becomes *stronger* (≈ +4.6 % of E[Y] per SD): the genus layer M_gen (FRONTIER §2.1; the
kickoff lists it as a known explanation, 𝓛 omitted it) contains L(1, χ_{−4}χ_p)-type terms, so an L-value of
χ_{−4p} is a *known main-term* quantity; (ii) G17's power sits in log a₁/L (the ordinary near-square p − m²), and it
absorbs G6; (iii) τ₃(p+1) absorbs ~99.7 % of G16's F-statistic; (iv) G7–G10 tail effects vanish once the local design
is in the logistic null; (v) G11 has the local shadow (p/283) (its sign character), which 𝓛 does not contain as a free
covariate. Therefore a second battery **A5**, on h = 2, with the null **𝓛⁺⁺** := 𝓛⁺ + for each prime 53 ≤ q ≤ 997:
(q/p), 1[p ≡ 1 (q)], 1[p ≡ −1 (q)] (free coefficients; this makes every Legendre symbol and both "±1 classes" of
every prime ≤ Q₀ local covariates) + log L_{Q₀}(1, χ_{−4}χ_p) and its square (truncated genus-layer proxy) + log(a₁)/L
(near-square). For the logistic tail tests the null is the compact version 𝓛⁺ + f₋₁ := Σ_{53≤q≤997, q∣p+1} (log q)/q +
log L_{Q₀}(1, χ_{−4}χ_p) and square + log(a₁)/L (the full 880-column null does not fit in the memory cap with float
storage; tail tests on C showed no local-shadow effects beyond 𝓛⁺ except G1, G16, G17). Families (cont + tail each):
**G1′** := log(πh(−4p)/(2√p)) − log L_{Q₀}(1, χ_{−4}χ_p) (the part of L(1, χ_{−4p}) not determined by q ≤ Q₀), G2, G3,
G4, G5, G6, G8, G9, G10, G11, G12, G13, G15, G16 (with τ₃(p+1), log(1 + τ₃(p+1)) added to both nulls), and **G17′** := Γ
(generalised near-square beyond a₁). G7 and G14 are local by the §1 definition and are not retested (their primary
significance is reported as incompleteness of the additive local model). Holm over the 30 A5 tests. The decision rule of
Amendment 1 applies with A5 in place of the A-block.

**Amendment 3 (registered before computing anything on its data; motivated by the need for an invariant-free test).**
A *named*-invariant battery can only find what it lists. A "prime T1" acts like T1 at squares: it moves *all* ticket
families at once. The per-prime engine splits R = A1 + A2 + A3 by the smallest coordinate: A1 (C smallest) is decided by
the factorisations of the integers 4Cp + 1, C ≤ S; A2 (u smallest, u < C, u ≤ B) by those of p + u, u ≤ S; A3 is the u ↔ B
mirror of A2. The two ticket sets {4Cp + 1} and {p + u} are disjoint. **Lottery null:** conditionally on local data the
two families are (heuristically) independent, so corr(res A1, res A2) ≈ 0, up to unmodelled local/known effects, which
both act in the same direction on the two families and can only make the correlation *positive*. A hidden global
multiplier e^H of all event rates gives Cov(A1, A2) ≈ μ₁μ₂ Var(H). **Test T2T:** on the fresh sample S₃ := {p ∈ Bulk1,
p ≥ 10⁸, splitmix64(p) mod 16 = 3} (⊂ the untouched reserve h = 3) and on High: fit quasi-Poisson GLMs for A1 and A2
with the 𝓛 design on the half splitmix64(p) mod 32 < 16 of S₃ (resp. High), compute Pearson residuals on the other half,
report their correlation ρ̂ with CI and the implied upper bound on SD(H) (conservative: unmodelled shared local effects
inflate ρ̂). Positive control: the same statistic on a mixture with odd squares (gcd version, R* = 0) is trivially
large; we instead report the planted version: multiply both families' simulated rates by e^H, H ~ N(0, σ²).
One pre-specified test: H₀: ρ ≤ 0.005 vs ρ > 0.005 on S₃ (one-sided, α = 0.01); High is replication.

**Amendment 4 (before S4 was run).** S4 as registered uses all 16 families, several of which are local or mechanical
(§4.1), so its omnibus will be significant for known reasons. Added **S4b**: the same omnibus restricted to the
families without a local shadow or ticket content in their own definition: G2, G3, G4, G8, G9, G10, G12, G13 (G10 keeps
its (p/23) shadow; noted).

**Amendment 5 (after the Amendment-1 battery and the continuous part of A5 on h = 2; before touching its data).** On h = 2
the part of L(1, χ_{−4p}) beyond Q₀ (G1′) is strongly significant (F = 160), and G6, G15, G16 (with τ₃) remain. All of
these are consistent with the *exact* genus-layer L-values mattering, which is a known main-term mechanism: for
p ≡ 1 (8) the real characters of the genus layer evaluated at p are (d/p) for fundamental d, and M_gen is a weighted sum of
them, i.e. of L-value data of the four fields ℚ(√p), ℚ(√−p), ℚ(√2p), ℚ(√−2p). So a battery **A6** on the fresh sample
**h₃′** := {p ∈ Bulk1 : splitmix64(p) mod 16 ∈ {7, 11, 15}} (disjoint from S₃ and from everything else), null
**𝓛⁺⁺⁺** := 𝓛⁺⁺ + ℓ_d := log L(1, χ_dχ_p) exactly for d ∈ {1, −4, 8, −8} (via h(p) log ε_p, h(−4p), h(−8p), h(8p) log ε_{8p};
PARI, GRH-conditional for the real fields), their squares and pairwise products (14 columns). Families (cont + tail):
G2, G3, G4, G6, G8, G9, G10, G11, G12, G13, G15, G16 (+τ₃ in the null), G17′; tail null = compact 𝓛⁺ + the 14 columns
+ f₋₁ + log(a₁)/L. Holm over the 26 tests; same decision rule.

**Amendment 6 (after A6; before computing any invariant on S₃).** A6 leaves exactly one Holm-significant family, G16
(factorisation of p ± 1), with τ₃(p+1) already in the null. Two non-global explanations remain to be excluded: (i) the
u = 1 ticket enters R exactly as τ₃(p+1), but a linear-plus-log covariate adjustment of a *standardised* residual need not
remove it exactly; (ii) "q ∣ p ∓ 1" for 1000 < q is local data at a larger modulus (F-type shift effects, tickets
4Cp + 1 with 4C ≡ ∓1 (mod q)). Test **A7** on **S₃** (fresh for invariants; its counts were used only in T2T): outcome
z′ := (Y − τ₃(p+1))/s(μ̂) with s(μ) = √(μ + μ²/k̂) (the u = 1 slice removed exactly); null = 𝓛 design + μ̂/s(μ̂) + f₁, f₋₁
(53 ≤ q ≤ 997) + f₁⁺, f₋₁⁺ := Σ_{1000<q≤20000, q∣p∓1} (log q)/q; tests (a) p + 1 part {ω(p+1), log P⁺(p+1)/L} and (b) p − 1
part {ω(p−1), log P⁺(p−1)/L}; Holm over the 2 tests. The same is run on h₃′ as a labelled exploratory comparison.

**Amendments 7–8 (after A7 on S₃; exploratory runs A8, A9 on h₃′ only).** A7 (S₃) is significant for both parts, but its
null lacked the per-q indicators of 𝓛⁺⁺ and the prime-power depth (G14). Exploration on h₃′: with per-q indicators
(53 ≤ q ≤ 997) the ≤ 1000 parts of ω(p ± 1) are linear in the null (rank 0, untestable as interactions); adding the
1000-smooth parts of p ∓ 1 (local p-adic data at q ≤ 1000) and one-hots mod 64, 27, 25, 49, the p + 1 part beyond 1000
vanishes (F = 0.66) and the p − 1 part beyond 1000 drops to F = 14 (+0.7 % and +0.6 % of E[Y] per SD for ω_{>1000}(p−1)
and log P⁺(p−1)/L). **Final confirmatory test A9** (registered now, before touching its data) on **B₂₃** := {p ∈ Bulk2 :
splitmix64(p) mod 64 = 3} (789 181 primes in (10⁹, 10¹⁰]; only the 𝓛 prediction had been computed on it, no invariant), μ̂ from 𝓛 refitted on Bulk2 h64 = 2: outcome z′, the
A9 null (𝓛 design, per-q (q/p), 1[p ≡ ±1 (q)] for 53 ≤ q ≤ 997, μ̂/s, f₁⁺, f₋₁⁺, log of the 1000-smooth parts of p ∓ 1 over
L, one-hots mod 64, 27, 25, 49); tests (b′) {ω_{>1000}(p−1), log P⁺(p−1)/L} and (d′) the same for p + 1; Holm over 2.

## 4. Results

### 4.1 Primary block on C (as pre-registered; EVIDENCE)
C = 1 566 421 primes p ∈ 𝒫₂₄ ∩ [10⁷, 10⁹] (h = 1); 𝓛 fitted on D (1 568 230 primes, h = 0): 325 parameters, NB shape
k̂ = 58.5, Pearson dispersion of Y vs Poisson 1.48. Out-of-sample on C: mean r = −0.0006, sd r = 0.998, corr(log μ̂,
log(Y + ½)) = 0.653 (D: 0.653); P(u < 0.01) = 0.81 % (12 725 hard primes), P(u < 0.001) = 0.072 %. Full tables:
`data/z56/primet1/primary_C_tests.tsv`, `primary_C_effects.tsv`.

| family | P-cont p_Holm | P-tail p_Holm | largest effect on E[Y] per SD (± se) | largest tail OR per SD |
|---|---|---|---|---|
| G1 h(−4p) | 3e−25 | 9e−18 | +0.18 % (0.02) | 1.08 |
| G2 v₂(h(−4p)) | 1 | 1 | +0.04 % | 0.997 / 1.016 |
| G3 3, 5 ∣ h(−4p) | 1 | 1 | +0.03 % | 0.99 |
| G4 h(p) > 1 | 1 | 1 | 0.00 % | 1.00 |
| G5 L-tail beyond Q₀ | 4e−23 | 0.49 | −0.19 % (0.02) | 0.98 |
| G6 regulator, period | 6e−9 | 4e−62 | ±4.5 % (collinear pair) | 4.0 / 0.29 |
| G7 n(p) | 0.079 | < 1e−300 | −0.04 % | 1.38 |
| G8 ord_p(2) | 1 | 0.0043 | −0.06 % | ≤ 1.06 |
| G9 ord_p(3) | 1 | 0.00065 | −0.02 % | ≤ 1.06 |
| G10 x³ − x − 1 | 1 | 0.0043 | +0.01 % | 0.97 |
| G11 x⁴ − x − 1 | 0.0043 | 1 | +0.07 % | 1.00 |
| G12 Hecke angles | 1 | 1 | −0.04 % | ≤ 1.015 |
| G13 Sato–Tate 11a1 | 1 | 1 | −0.02 % | ≤ 1.006 |
| G14 deeper 2/3/5/7-adic depth | < 1e−300 | 2e−55 | −0.65 % (27 ∣ p−1) | 1.09 |
| G15 (q/p), 1009 ≤ q ≤ 1061 | 0.0043 | 1 | −0.08 % | 1.01 |
| G16 smoothness of p ± 1 | < 1e−300 | < 1e−300 | −6.3 % (log P⁺(p+1)/L) | 2.01 |

*Reading (Assessment, written before Amendment 1 was run).* Every family whose effect exceeds 0.1 % of E[Y] has an
obvious local, known or mechanical candidate explanation: G14 is local by definition (prime powers ≤ Q₀ that 𝓛 did not
include); G1/G5/G15 are L-value effects (𝓛 truncated L(1, χ_p) at Q₀; the known M_BM uses the exact value); G16's
p + 1 part is a ticket (R ⊇ the u = 1 slice 2τ₃(p+1)); G6 is collinear regulator/period and is a near-square signature;
G7–G10 are pure tail effects of invariants whose local shadows (Legendre symbols of small primes, (p/23)) enter 𝓛
only additively in the mean, not in the tail shape. The non-congruence invariants with no local shadow at all — G2
(Cl(−4p)[2^∞]), G3, G4, G12 (Hecke angles), G13 (Sato–Tate) — are null in both tests. Amendment 1 (§3.9) tests
these explanations on the untouched reserve.

### 4.2 Engines, census cross-check, controls, power (CERTIFIED / EVIDENCE)
* **Engines.** `z56_primet1_rsieve.c` (pair sieve) = `z52b_p1_H03_rcount.c` (trial division) on all 385 p ∈ 𝒫₂₄ ≤ 3·10⁴;
  `z56_primet1_rone.c` (per-prime, smallest-coordinate decomposition with factorisation) = sieve on 5 000 primes ≤ 10⁹
  and on all 353 214 primes of S₃ (0 mismatches). Timing: rone ≈ 0.1 s/prime at 10¹², 0.32 s at 10¹³.
* **Census (CERTIFIED by this engine; a second, independent engine for the 10⁸–10¹⁰ part).** Sieve runs over [1, 10⁸],
  [10⁷, 10⁹] and (10⁹, 10¹⁰] (all 50 521 668 primes p ≡ 1 (24) there): R(p) = 0 exactly at the 14 known primes
  409 … 8 813 281, none above. In (10⁹, 10¹⁰] min R = 2, attained only at **p = 1 397 190 001 = 37379² + 360 ≡ 19²
  (mod 840)** (a near-square in a Mordell class; seven more primes have R = 6; `data/z56/primet1/census_1e9_1e10.txt`).
  Since every (★)-zero p ≡ 1 (4) is ≡ 1 (24), this re-certifies "exactly 14 (★)-zeros among p ≡ 1 (4) ≤ 10¹⁰".
  No zero among the 25 000 consecutive p ∈ 𝒫₂₄ above 10¹² and 10¹³ (min R = 36).
* **T1 control.** R*(m²) = R(m²) = 0 at 199 odd squares (gcd(m, 6) = 1; m < 400 and 10⁶ < m < 10⁶ + 200), per-prime engine
  with and without the gcd(u, B) = 1 condition (`t1_control.txt`).
* **PC1 (positive control).** 𝓛 refitted without p mod 13: the pipeline detects p mod 13 (11 df) on C with F = 5 319,
  LR = 2 327 (p < 10⁻³⁰⁰).
* **PC2 (power; planted NB signal on C, detection at the strictest Holm level 0.05/32, 20 simulations each).** Balanced
  binary invariant multiplying E[Y] by e^β: P-cont power 0.25 at β = 0.1 %, **1.00 at β = 0.2 %**; P-tail power 0.40 at
  β = 0.5 % (tail OR 0.955), **1.00 at β = 1 % (tail OR 0.90)**. Hidden subclass of density π with E[Y] multiplied by ρ:
  detected with power 1.00 (both tests) for (π, ρ) = (10⁻², ½), (10⁻³, ½), (10⁻³, ¼), (10⁻⁴, ¼), (10⁻⁴, 0.1)
  (`pc2.tsv`). Analytic check: SE of a balanced binary effect on r is 2/√N = 0.0016, i.e. 0.0016·√(1/μ̄ + 1/k̂) ≈ 0.04 % of
  E[Y] (μ̄ ≈ 20, k̂ = 58.5); MDE(80 %, two-sided α = 0.05/32) ≈ (3.42 + 0.84)·0.04 % ≈ 0.18 % of E[Y]. **So on the bulk data every named invariant is screened
  down to effects of ≈ 0.2 % of E[Y] (continuous) and tail odds ratios of ≈ 1.1 per SD.**

### 4.3 Amendment batteries (§3.9): what survives a complete *known* model (EVIDENCE)
All on data never used before the respective amendment was written (tables in `data/z56/primet1/`).

| family | A-block, h = 2, null 𝓛⁺ (cont / tail p_Holm) | A5, h = 2, null 𝓛⁺⁺ | A6, h₃′, null 𝓛⁺⁺⁺ (exact L-values) |
|---|---|---|---|
| G1 h(−4p) / G1′ its part beyond Q₀ | < 1e−300 / 5e−20 | G1′: 3e−35 / 0.31 | (in the null) |
| G2 v₂ h(−4p) | 1 / 0.075 | 1 / 0.075 | 1 / 1 |
| G3 3, 5 ∣ h(−4p) | 1 / 1 | 1 / 1 | 1 / 1 |
| G4 h(p) > 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| G5 L(1, χ_p) beyond Q₀ | 0.13 / 1 | 0.38 / 1 | (in the null) |
| G6 regulator, period | 4e−9 / 0.14 | 5e−4 / 1 | **0.11 / 1** |
| G7 n(p) | 9e−21 / 1 | local, not retested | — |
| G8 ord_p 2 | 1 / 1 | 1 / 1 | 1 / 0.11 |
| G9 ord_p 3 | 1 / 0.83 | 1 / 0.66 | 1 / 1 |
| G10 x³ − x − 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| G11 x⁴ − x − 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| G12 Hecke angles | 1 / 1 | 0.86 / 1 | 1 / 1 |
| G13 Sato–Tate 11a1 | 1 / 1 | 1 / 1 | 1 / 1 |
| G14 deeper p-adic depth | (in 𝓛⁺: rank 0) | local | — |
| G15 (q/p), 1009 ≤ q ≤ 1061 | 0.0041 / 1 | 0.0022 / 1 | **0.28 / 1** |
| G16 p ± 1 (with τ₃(p+1) in null) | 1e−52 / 0.53 | 3e−53 / 0.31 | **3e−48** / 1 |
| G17 near-square (a₁, Γ) / G17′ (Γ only) | < 1e−300 / 5e−44 | G17′: 0.40 / 1 | G17′: 1 / 1 |
| G6 given G17 | 0.0015 / 1 | — | — |

Reading (EVIDENCE): (i) the strong G1/G5/G15 effects are L-value effects; once the exact L(1, χ_dχ_p), d ∈ {1, −4, 8, −8}
(the genus-layer fields) are in the null, G6 and G15 fall below Holm significance; G1 itself is ≈ +4.6–4.8 % of E[Y]
per SD conditionally on the exact BM term (larger h(−4p) ⇒ more solutions; only +0.18 %/SD under 𝓛, whose truncated BM
proxy is collinear with it), a *known-type* main-term effect absent from the pre-registered 𝓛 (𝓛 had only the BM
L-value); (ii) the near-square effect is carried by a₁ (the ordinary p − m²), and the generalised near-square Γ adds
nothing (A5, A6); (iii) all tail effects of G7–G10 disappear with local terms in the logistic null; (iv) the non-congruence
families without local shadow — G2, G3, G4, G12, G13 — are null in every battery; G8–G11 (power residuosity of 2 and
3, Frobenius in the S₃ and S₄ fields) are null once their local shadows are in the null. **G16 is the only family that
survives A6.**

**Dissecting G16 (A7–A9).** Removing the u = 1 slice exactly (outcome z′ = (Y − τ₃(p+1))/s(μ̂)) and putting the local
p-adic data of p ∓ 1 at q ≤ 1000 into the null:

| test | sample (role) | p + 1 part beyond 1000 | p − 1 part beyond 1000 (ω_{>1000}(p−1), log P⁺(p−1)/L) |
|---|---|---|---|
| A9 | h₃′ (exploratory) | F = 0.66, p = 0.52 | F = 14.1, p = 7e−7; +0.030, +0.025 z/SD |
| A9 | **B₂₃ (confirmatory, fresh)** | F = 1.25, p_Holm = 0.29 | **F = 4.96, p_Holm = 0.014; +0.025, +0.027 z/SD** |
| A9 | High 10¹²–10¹³ (n = 25 000) | F = 0.25 | F = 0.14 (n.s.); +0.023, +0.026 z/SD (same sign and size) |

(1 z/SD ≈ 22 % of E[Y] per SD, so the p − 1 effect is **≈ +0.5–0.6 % of E[Y] per SD of each feature**.) The p + 1 signal
was the u = 1 ticket plus local data. The p − 1 residual is real at the 1 % level on fresh data but tiny; it is not a sum
of F-type q-local effects (those decay like 1/q and have the opposite sign for p ≡ 1 (q), `RESIDUE_HARDNESS.md` Lemma 2), and
we have no mechanism for it. Under the pre-registered rule (Holm-significant AND nominally significant with the same sign
at another height) it **fails the second clause** (High: same sign, n.s.; the High sample has power only for ≳ 5× this
effect). Status: **weak candidate, unexplained, ≈ 0.5 % of E[Y]**.

### 4.4 Secondary blocks (EVIDENCE)
* **S1 (heights; 𝓛 extrapolated, recalibrated on log μ̂).** Bulk2 hash-sample (791 211 primes, 10⁹–10¹⁰): significant
  G5, G6, G7, G8, G9, G10, G14, G15, G16 (`s1a_tests.tsv`); High (25 000 primes): G6, G7, G14, G16. Out-of-range use of 𝓛
  leaves local structure (n(p), p-adic depth, the shadows of G8–G10) in the residual; all signs of G16 agree with C.
  G1's sign flips at High (−0.8 % vs +0.2 % per SD under 𝓛).
* **S2 (hardest 0.01 % of (10⁹, 10¹⁰]; 5 052 hard primes, 15 156 matched controls).** Holm-significant: G1 (OR 0.90 per
  SD: small h(−4p) ⇒ hard), G6 (large regulator ⇒ hard), G7 (OR 2.05: large n(p) ⇒ hard), G16 (P⁺(p+1) large ⇒ hard,
  OR 2.1: the u = 1 ticket); post-hoc G17 (a₁ large ⇒ hard, OR 1.15). Null: G2 (raw 0.02), G3, G4, G5, G8–G13, G15. The
  extreme tail is explained by the same list as the bulk: L-values (BM + genus), near-squares, small-prime residue
  patterns, the u = 1 ticket.
* **S3 (the 14 zeros vs 50 matched controls each).** No family Holm-significant (smallest: G7 p = 0.024, G6 p = 0.055).
  Per-zero values (`s3_s3_zerofeat.tsv`): v₂ h(−4p) ∈ {2, 3, 4, 5}, h(p) = 1 except 577 (h = 7, near-square 24² + 1),
  i₂ ∈ {2, …, 900}, all four S₄-root counts occur — the zeros share no non-congruence invariant value.
* **S4 (omnibus gradient boosting, D → C, 200 permutations).** All families: out-of-sample R² = 0.096 (null max −0.092),
  AUC 0.681 (null max 0.507), driven by the local/ticket families. **S4b (shadow-free families G2, G3, G4, G8, G9, G10, G12,
  G13): R² = 0.00019, AUC 0.517**, both above all 200 permutations (p = 1/201) — a detectable but negligible nonlinear
  signal; S4b's residual and hard flag come from 𝓛, whose omissions (genus L-values; local shadows of G8–G10 via p − 1 and
  (p/23)) are visible to these features, and the confirmatory batteries A5/A6 with complete nulls find nothing in these
  families. Assessment: S4b measures 𝓛's incompleteness, not a global mechanism.
* **S5 (HC at 10¹², 9 936 primes ≡ 1 (24); 72 with HC > 7).** Significant: G6, G7, G16 (the same explanatory list:
  near-squares/L-values, small-prime residue pattern, p ± 1). Null: the shadow-free families.

### 4.5 The invariant-free test T2T (Amendment 3; EVIDENCE)
Correlation of the out-of-sample Pearson residuals of A1 (tickets 4Cp + 1) and A2 (tickets p + u), local model fitted on
the other half:

| sample | n (eval) | ρ̂ [99 % CI] | σ̂²_H = mean[(A1−μ₁)(A2−μ₂)]/mean[μ₁μ₂] (99 % upper) | within-family dispersion φ₁, φ₂ |
|---|---|---|---|---|
| S₃ (10⁸–10⁹) | 176 733 | −0.0050 [−0.0111, +0.0012] | −6.4·10⁻⁴ (≤ −7·10⁻⁵) | 2.55, 1.58 |
| High (10¹²–10¹³) | 12 474 | −0.012 [−0.035, +0.011] | −1.0·10⁻³ (≤ 6.4·10⁻⁴) | 3.73, 2.58 |

Planted control: σ_H = 0.05 and 0.1 are recovered (σ̂² = 0.0025, 0.0100); σ_H = 0.02 is at the noise floor. The pre-specified
test (H₀: ρ ≤ 0.005) is not rejected (p = 0.99999). **Reading (EVIDENCE):** each ticket family is strongly overdispersed
(φ = 1.6–3.7: a ticket with many divisors produces several hits), but the two disjoint ticket families are *uncorrelated*
(slightly negative) given local data. A hidden global factor multiplying all event rates by e^H has SD(H) ≲ 1.1 % at
10⁸–10⁹ (from the CI of ρ̂: σ²_H ≤ ρ̂_hi·√(φ₁μ₁φ₂μ₂)/(μ₁μ₂) ≈ 1.2·10⁻⁴) and ≲ 2.5 % at 10¹²–10¹³. A T1-like
subclass (density π, both families multiplied by ρ) has Var(e^H) ≈ π(1 − ρ)², so at 10⁸–10⁹ such a subclass with
ρ = 0 must have density π ≲ 1.2·10⁻⁴, and with ρ = ½ density ≲ 5·10⁻⁴. This bound needs no list of invariants. The
overdispersion of R (φ ≈ 1.5) is within-family (lottery tickets with many divisors), not a common factor.

### 4.6 Synthesis: the explanatory ledger of (★)-hardness (EVIDENCE + Assessment)
Every significant association found in this lane falls into one of five known or mechanical classes:
1. **local residue data** at small q (one-hot classes, p-adic depth G14, the non-additive pattern n(p) (G7), the local
   shadows of G8–G11);
2. **L-value main terms**: the BM term E·L(1, χ_p)² (`BM_LVALUE.md`) and the genus-layer L-values, notably
   L(1, χ_{−4p}) ∝ h(−4p) (≈ +4.6–4.8 % of E[Y] per SD conditionally on the exact BM term; G1), plus their tails beyond Q₀ (G1′, G5, G15);
3. **near-squares** (a₁ of √p, i.e. p − ⌊√p⌋²; G17, and the regulator/period signal G6, absorbed once L-values and a₁
   are modelled);
4. **tickets**: the u = 1 slice 2τ₃(p + 1) (G16's p + 1 part);
5. one **unexplained residual**: the large-prime structure of p − 1, ≈ +0.5 % of E[Y] per SD (A9; fails replication at
   10¹²–10¹³ for lack of power).
No class-group, power-residue, non-abelian Frobenius, Hecke-angle or Sato–Tate invariant carries information beyond
these, at an MDE of ≈ 0.2 % of E[Y] and tail OR ≈ 1.1 per SD (§4.2), and the invariant-free T2T bounds any common hidden
factor to SD ≲ 1–2.5 %.

## 5. Verdict, screens, FRONTIER text

**Verdict: narrowed (a clean null with power analysis; EVIDENCE).** In the tested ranges (10⁷–10¹⁰ in bulk, 10¹²–10¹³
samples) there is no global invariant of p with residual predictive power for R(p), for hard primes or for the zeros,
beyond the known explanations (local data, BM and genus-layer L-values, near-squares, the u = 1 ticket), with one tiny
unexplained residual (§4.3, p − 1). (★)-hardness looks like **local main term × lottery**: the overdispersion is
within ticket families and the two disjoint ticket families are uncorrelated (T2T). What this buys: (a) a "prime T1"
would have to be invisible to every invariant listed (G1–G17) at the 0.2 % level and to the T2T common-factor test at the
1–2.5 % level in these ranges, or to act only above 10¹³ or on a set of density ≲ 10⁻⁴; (b) the known model should be
extended by the genus-layer L-value L(1, χ_{−4p}) (h(−4p)), the single largest omitted main-term effect we found
(≈ +4.6–4.8 % per SD given the exact BM term). What it does not buy: anything at a fixed prime (B6); a statistical null can never exclude a
measure-zero mechanism (a structured family of density 0, like the squares among integers, is invisible to every test
here unless it is sampled).

**FRONTIER §4 hard screens** (this is a statistical lane, not a proof mechanism):
1. *T1 squares:* respected — R*(m²) = 0 control passes; the tests concern primes only, and T1 is exactly the kind of
   all-ticket common factor T2T would detect if it existed at positive density among primes. Pass (as a control).
2. *8/131:* not applicable (no positivity mechanism is proposed).
3. *Tied modulus:* not applicable; T2T is the statistical shadow of the tie (it tests whether ties at different tickets
   are coupled; they are not, beyond local data).
4. *Fixed p:* fails by design — every statement is distributional over p (B6).

**Proposed FRONTIER §7.15 addition** ("prime T1"):
> *(z56 PRIMET1, `Z56_PRIMET1.md`; EVIDENCE.)* A pre-registered, held-out search over 17 invariant families — h(−4p) and
> its 2-, 3-, 5-parts, h(p), regulator and Pell period, L(1, χ_p) beyond q ≤ 1000, least non-residue, ord_p 2 and ord_p 3
> (power residuosity), Frobenius in x³ − x − 1 and x⁴ − x − 1, Gaussian/Eisenstein Hecke angles, the Sato–Tate angle of
> 11a1, deeper p-adic depth, Legendre symbols beyond 1000, smoothness of p ± 1, generalised near-squares — with invariants
> computed on 6.7·10⁶ primes p ≡ 1 (24) in [10⁷, 10¹⁰] (exact R; plus 25 000 at 10¹²–10¹³, the hardest 0.01 % of
> (10⁹, 10¹⁰], the 14 zeros, HC at 10¹²) finds no global invariant beyond the known explanations: local data, the BM and genus-layer L-values (h(−4p)
> is a ≈ +4.7 %/SD main-term effect (given exact BM) missing from the BM-only model), near-squares (a₁ of √p) and the u = 1 ticket 2τ₃(p+1).
> MDE ≈ 0.2 % of E[R] and tail OR ≈ 1.1/SD. One unexplained residual: large prime factors of p − 1, ≈ +0.5 %/SD.
> An invariant-free test (correlation of the disjoint ticket families 4Cp + 1 and p + u) bounds any common hidden
> multiplier to SD ≲ 1.1 % (10⁸–10⁹), 2.5 % (10¹²–10¹³): the overdispersion of R is within-family. Census re-certified
> by an independent sieve: no (★)-zero in (10⁸, 10¹⁰]; min R = 2 in (10⁹, 10¹⁰] at 1 397 190 001 = 37379² + 360.

**Bottom line.** We looked for a non-lottery mechanism behind (★)-hardness in the way the kickoff asked, and with
enough data to see effects of a fifth of a percent. Everything that predicts hardness beyond the pre-registered local
model turned out to be either a main-term ingredient the model had left out or a mechanical part of the count. The one
left over is a half-percent effect of the large prime factors of p − 1, with no mechanism. The two disjoint families of
divisor events are uncorrelated given local data. That is what a lottery predicts, and not what a prime T1 would do at
positive density. None of this bears on any single prime, and none of it touches the open question of ES.

## 6. Review record
*(to be filled)*

## 7. Commands and reproducibility
Scratch directory S (outside the repo; ≈ 1 GB; every file regenerable). All runs used `ulimit -v` 2–8 GB and `timeout`;
P = `uv run --with numpy --with scipy [--with cypari2] [--with statsmodels] [--with scikit-learn] python scripts/…`.
```
gcc -O2 -o S/rsieve scripts/z56_primet1_rsieve.c; gcc -O2 -o S/rone scripts/z56_primet1_rone.c; gcc -O2 -o S/cfper scripts/z56_primet1_cfper.c -lm
S/rsieve 1 100000000 > r_1e8.bin; S/rsieve 10000000 1000000000 > r_1e7_1e9.bin; S/rsieve 1000000000 10000000000 > r_1e9_1e10.bin
                                                     # 0.5 s, 21 s, ~6 min; binary records (uint64 p, uint16 R)
P z56_primet1_split.py r_1e7_1e9.bin bulk1 4 0,1,2   # D, C, h2;  h3' and S3: splitmix64 mod 16 (see §3.9)
P z56_primet1_split.py r_1e9_1e10.bin bulk2 64 1,2,3
scripts/z56_primet1_high.sh S                        # 20 000 + 5 000 consecutive p ≡ 1 (24) above 10^12, 10^13 (rone, 8-way)
P z56_primet1_feat.py <set>_p.npy feat_<set>.npy 6   # families G1–G16 (PARI; quadclassunit GRH-conditional)
S/cfper < <set>_p.txt > cf4_<set>.txt                # CF period, a1, Gamma
P z56_primet1_local.py fit bulk1_h0.npy model_D.npz  # 𝓛 (also --drop13 for PC1; on bulk2_h2 for S2/A9)
P z56_primet1_local.py predict model_D.npz <set>.npy pred_<set>.npy
P z56_primet1_tests.py pred_h1.npy feat_h1.npy cf_h1.txt primary_C          # §4.1 primary block
P z56_primet1_tests.py pred_b2h1.npy feat_b2h1.npy cf_b2h1.txt s1a --notail --nulllogmu ; (same on pred_high: s1b)
P z56_primet1_amend.py pred_h2.npy feat_h2.npy cf4_h2.txt amendH2           # Amendment 1 (A-block); on C: amendC
P z56_primet1_amend2.py pred_h2.npy feat_h2.npy cf4_h2.txt a5H2              # A5
P z56_primet1_feat2.py h3p_p.npy feat2_h3p.npy ; P z56_primet1_amend3.py pred_h3p.npy feat_h3p.npy feat2_h3p.npy cf4_h3p.txt a6H3   # A6
P z56_primet1_g16.py pred_s3t.npy model_D.npz a7S3 ; P z56_primet1_g16b.py pred_h3p.npy model_D.npz a8H3        # A7, A8
P z56_primet1_g16c.py pred_h3p.npy model_D.npz a9H3 ; P z56_primet1_g16c.py pred_b2h3.npy model_B2.npz a9B23   # A9
P z56_primet1_s2.py select model_B2.npz r_1e9_1e10.bin s2 ; P z56_primet1_s2.py test s2 feat_s2.npy cf4_s2.txt  # S2
P z56_primet1_s3.py r_1e8.bin s3 S/cfper ; P z56_primet1_s4.py pred_h0.npy feat_h0.npy cf_h0.txt pred_h1.npy feat_h1.npy cf_h1.txt s4.tsv 200
P z56_primet1_s5.py data/z53/hchyp/stat_1e12_X2048.txt.hc feat_s5.npy cf4_s5.txt s5.tsv
S/rone < s3t_p.txt > s3t_rone.txt ; P z56_primet1_t2t.py s3t_rone.txt t2t_S3 --sieve s3t.npy ; (high: t2t_high)  # T2T
P z56_primet1_pc1.py pred_h1_drop13.npy ; P z56_primet1_pc2.py pred_h1.npy pc2.tsv 20                       # PC1, PC2
S/rone g < sq_in.txt                                  # T1 control (odd squares)
```
Committed outputs (`data/z56/primet1/`, 0.3 MB): every test table named in §4 (`primary_C_*`, `amend*`, `a5H2_*`, `a6H3_*`,
`a7*`, `a8H3_*`, `a9*`, `s1a_*`, `s1b_*`, `s2_s2.tsv`, `s2_hardest_1e9_1e10.tsv` (the 5 052 hardest primes with R, μ̂, PIT),
`s3_*`, `s4.tsv`, `s5.tsv`, `t2t_*`, `pc1.txt`, `pc2.tsv`), `census_1e9_1e10.txt`, `t1_control.txt`,
`local_model_D_coefs.tsv`.
