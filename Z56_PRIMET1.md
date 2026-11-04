# Z56_PRIMET1 — is (★)-hardness a lottery? A pre-registered hunt for a global invariant ("prime T1")

Status: wave z56 lane PRIMET1 (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z56_lanes.md` §5). **ES is OPEN; nothing
here proves or disproves ES or (★).** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
This is an EVIDENCE-level lane. Scripts `scripts/z56_primet1_*`, data `data/z56/primet1/` (large intermediates kept out
of the repo in a scratch directory and regenerable by the exact commands of §7).

*(Checkpoint 1: §§1–3 written and committed BEFORE any association between an invariant and R(p) was computed. Only
engine validation (the 14 known zeros reproduced, timing) had been run at that point. Later amendments are listed in §3.9
with their reasons and their timing relative to outcomes.)*

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
*(none yet)*

## 4. Results
*(to be filled)*

## 5. Verdict, screens, FRONTIER text
*(to be filled)*

## 6. Review record
*(to be filled)*

## 7. Commands and reproducibility
*(to be filled)*
