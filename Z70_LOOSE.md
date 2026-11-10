# Z70_LOOSE — the untested ideation leftovers (I6, I5, IDEAA #10, MINE Pell-letter residues, I9)

**ES is OPEN.** This memo proves or computes nothing that settles ES. Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal review only. Scripts `scripts/z70_loose_*`, data `data/z70/loose/`.
Status: **final** (all five items run; internal hostile review done and applied — §11). Awaiting cross-review.

**Summary.** I6: the d = 1 and d = 3 fibres satisfy an explicit S-transformation (Theorem F, PROVED; checked at
machine precision at 28 points and in multiprecision at 5 + 5 points, relative error ≤ 2·10⁻¹⁹);
its period is an integral transform of dual partial Lambert series that are not weight-1 modular (PROVED for d = 1),
but mock status is **not decided**. The level sum G has leading singular coefficients κ(a₀/c) = 1[c odd]μ(c)/c²
(Lemma K, PROVED), hence **no finite-index law whose cocycles are o(y⁻¹log²(1/y)) at rationals** (Theorem LS, PROVED) —
in particular G is not modular and not the holomorphic part of a harmonic Maass form with cuspidal shadow
(Cor. LS-M). I5: 7 registered maps + 400 grammar expressions fail on T₇₃/T₄₀₉; Lemma P5: the odd parity of T_p lives in
the divisor words of p + 1. #10: four implemented d-selection rules dead (best coverage 97.4 %; NP's slice exactly
empty at six hard primes). Pell letters: no witness-specific signal against exact decoys (the registered null was
2-adically miscalibrated; recalibrated). I9: no detected difference; no detected q-to-word information. **No HOT LEAD;
ES OPEN.**

Notation. (★) / R(n) as in `z52bbriefs/z58_lanes.md`. Fibre form: R(n) = Σ_{d ≥ 1} r_d(4dn + 1),
r_d(N) := #{A | N : A ≡ −1 (mod 4d)} (A = 4ad − 1, B = 4bd − 1, AB = 4dn + 1 ⟺ 4abd − a − b = n).
Words: T_n = {(x, y, z) ∈ ℕ³ : xyz − x − z = n}; certificate words C_n ⊂ T_n as in `Z69_TWIST.md` Remark C.
Type I (IDEAB R2/R4): 4abd = pe + 1, ce = a + b; K3 form p ≡ −f (mod 4ad), f | 4a²d + 1.

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)
| item | F1 odd squares | F2 C-even / R₈ | F3 composites | F4 known zeros |
|---|---|---|---|---|
| I6 (fibre laws, level sum) | the fibre coefficient r_d(4dm² + 1) = 0 for 4 ∣ 4d (T1); a transformation law is a statement about the whole generating function and is coefficient-blind — it cannot by itself use primality; must be checked that the law holds identically at squares (it will) | n/a (the law is per fibre; C-even = d even fibres) | same as F1 | same as F1 |
| I5 (involution on T_p) | #T₉ = 11 odd, C₉ = ∅ ⟹ any involution family with certificate fixed points must fail at 9 (and at 105) | the swap-even sub-counts are even at primes; a map whose fixed points are C-even certificates would prove R₈-positivity — false at the 12 R₈ zeros; record which certificate type the fixed points have | 105: #T₁₀₅ = 11, C₁₀₅ = ∅ | none needed at primes (C_p ≠ ∅ at every tested prime) |
| #10 (Type I, d-rule) | Lemma T10: Type I at n = m² needs (d/m²) = −1, impossible: every rule fails at squares, by the Jacobi step (uses non-squareness exactly there) | n/a (Type I is outside (★)); reported: rule coverage on the 12 R₈ zeros | Type I at composites not tested (rule defined via p's quadratic data) | coverage on the 14 (★)-zeros, 38 𝔊*-zeros, 231 noprime primes reported |
| Pell letters | statistics on witnesses only; no witness at squares | n/a | n/a | H sets = hard primes |
| I9 | in a primitive m² = X² + 840Y², every q ∣ X has (840/q) = +1 ⟹ Q = 0 (classifier silent) | Q computed on the 𝔐-members of the R₈ zeros | n/a | hard sets are the test population |

## 1. Precise statements and pre-registered kill tests (fixed before any computation of this lane)

### 1.1 I6 — completion / transformation law of the fibre generating functions
Φ_d(z) := Σ_{A, B ≥ 1, A ≡ B ≡ −1 (4d)} e(ABz) = Σ_{N ≡ 1 (4d)} r_d(N) e(Nz) (Im z > 0), and
G(z) := Σ_n R(n) e(nz) = Σ_d e(−z/4d) Φ_d(z/4d).
**Target statements.** (S1) an explicit identity relating Φ_d(z) and dual series at −1/(16d²z) with explicit
boundary (residue) terms and an explicit period function, for d = 1 and d = 3, proved and numerically verified;
(S2) the nature of the period function: is it a mock period (Eichler integral of a weight-1 modular shadow), i.e. is
Φ_d the holomorphic part of a harmonic Maass form with modular shadow?; (S3) does Σ_d produce a law for G?
**Kill tests (pre-registered).**
* K6a (correctness): the derived law must reproduce Φ_1, Φ_3 at ≥ 5 points z (incl. |z| small, Re z ≠ 0) to relative
  error < 10⁻¹⁵ (mpmath, 30 digits); failure = derivation wrong (fix, not a result).
* K6b (mock?): compute the discontinuity of the period function across its cut. If it is (up to elementary
  log-terms) a weight-1 modular form → fibre mock-modular (positive outcome, pursue). If it is a non-modular
  q-series (dual partial Lambert series) → "no harmonic completion with modular shadow" for that piece (scoped).
* K6c (level sum): compute the leading singular coefficients κ(r) of G at rationals r (G(r + iy) ~ κ(r) y⁻¹log²(1/y)
  · const). If there are r₁, r₂ in the same Γ(N)-orbit for every N with κ(r₁) ≠ 0 = κ(r₂), then G satisfies no
  quantum-modular law of any real weight and unitary multiplier on any finite-index subgroup (with period functions
  o(y⁻¹log²) at rationals) — the kill. Numerical cross-check of κ at a few r.
* Squares: verify r_1(4m² + 1) = r_3(12m² + 1) = 0 and that the law holds at those coefficients (no special
  behaviour).

### 1.2 I5 — a fixed-p non-affine cross-slice involution on T_p
**Statement.** Find σ_p : T_p → T_p, an involution, σ ≠ swap (x, y, z) ↦ (z, y, x), changing y on some word
("cross-slice"), not affine in (x, y, z), with Fix(σ_p) ⊆ C_p. (Then |T_p| odd ⟹ C_p ≠ ∅ ⟹ ES(p).)
**Kill test (pre-registered).** Stage 1: on complete T₇₃ and T₄₀₉ (and T₉, T₁₀₅ as controls) every candidate must be
a well-defined involution with all fixed points in C_p at both primes; failing candidates are dead as stated. Stage 2
(only for survivors): all primes p ≡ 1 (4) ≤ 10⁴, and it must fail (be undefined, or have a non-certificate fixed
point) at 9 and 105. Candidate list (fixed now): (σ1) the SL₂ "coset swap with unipotent correction":
γ_w = [[xy − 1, n], [y, zy − 1]] ↦ the unique word in the coset-transposed double coset nearest in a fixed norm;
(σ2) x ↔ y partial exchange (x, y, z) ↦ (y, x, (n + y)/(xy − 1)) completed by the swap where undefined;
(σ3) continuant-flip maps from the HJ continuant n = K(x, y, z) = xyz − x − z (length-3 ↔ length-3 via the identity
K(x, y, z) = K(x − 1, 1, y − 1, z)-type relations, followed by re-contraction); (σ4) any further map found during
the lane, listed in §3 before it is run on T₇₃/T₄₀₉. A candidate passing stage 1 and 2 = HOT LEAD (announce).

### 1.3 IDEAA #10 — Type I with an explicit nonlinear d-selection rule
**Statement.** A rule p ↦ d(p) (computed from p's own data, never from solutions; d non-square; (d/p) = −1
necessary by Lemma T10) such that the Type I slice at d(p) is non-empty for every prime p ≡ 1 (24).
Slice test: ∃ a ≤ A, f | 4a²d + 1, f ≡ −p (mod 4ad) (then c = (p + f)/4ad, e = (4a²d + 1)/f, b = (pe + 1)/4ad give a
Type I solution; A = 2000 fixed; coverage is a lower bound for the full slice — this truncation is part of the
rule). Rules (fixed now): R-np d = n_p (least prime non-residue); R-q3 d = least prime q ≡ 3 (4) with (q/p) = −1;
R-G Gaussian: p = a₀² + b₀² (a₀ odd), first of a₀, b₀/2^{v₂(b₀)}, a₀ + b₀, |a₀ − b₀|, a₀ + 2b₀, 2a₀ + b₀ that is
non-square with (·/p) = −1; R-CF first partial quotient a_i (i ≥ 1) of the CF of √p that is non-square with
(a_i/p) = −1 (if any in the first period); R-sm d = least non-square d with (d/p) = −1 (= least d ∈ {n_p, ...},
also composite d). Matched decoy for each rule: a uniformly random non-square d′ with (d′/p) = −1 and |d′ − d| ≤ max(2, 0.1 d) (d′ ≠ d when possible).
**Kill tests.** K10a: coverage < 99.9 % on primes p ≡ 1 (24) ≤ 10⁸ ⟹ not a forcing rule. K10b: any failure on the
14 (★)-zeros / 38 𝔊*-zeros / 231 noprime primes / 12 R₈ zeros ⟹ dead. K10c (information): rule coverage not
above the matched decoy by ≥ 3σ (McNemar) ⟹ the rule's choice of d carries no information beyond its size and
(d/p) = −1. Fixture: the engine must find (p, a, d) = (1033, 1, 132).

### 1.4 MINE open item — Pell residues modulo candidate letters
**Statement.** For witnesses (U₇ words (x, y, z) of p, from `data/z69/mine/{H,CTRL}_witnesses.txt.gz`), letters
ℓ ∈ {x, y, z}, ℓ ≥ 5, and the negative-Pell solution T² − pU² = −1: is the event
D(ℓ) = [ℓ | v for some v ∈ V], V = {T, U} ∪ {T + cU + s : 1 ≤ |c| ≤ 3, |s| ≤ 2} ∪ {T + s : 1 ≤ |s| ≤ 2},
enriched relative to (i) the **exact local null** — (T, U) mod ℓ uniform on the conic T² − pU² ≡ −1 (mod ℓ) (exact
probability per letter, no sampling) — and (ii) exact decoy letters of the same p (MINE round-2 sampler: same 2-adic
part, odd part within ±5 %, same χ_p-signature), both on H_train / H_test / controls?
**Kill test / signal criterion (MINE round 2, unchanged):** |z| ≥ 4 on H_train and same sign |z| ≥ 3 on H_test;
otherwise non-rejection. Letters ℓ ≤ 2·10⁵ (exact null computable); p ≤ 2·10¹⁰ (Pell mod ℓ via the CF of √p).

### 1.5 I9 — X-coordinate classifier, rerun with disjoint factor-two controls and a q-to-word construction
**Statement.** p ∈ 𝔐 classes, p = X² + 840Y² (primitive); Q(p) = [∃ prime q | X, (840/q) = −1]. Is Q(p) more or
less frequent on hard primes than on controls? Does such a q build words?
**Design (pre-registered).** Hard sets as in `Z69_TWIST.md` I9 (𝔐-members of: 14 (★)-zeros, 38 𝔊*-zeros, 231 noprime
primes, U⁽⁸⁾-zeros ≤ 10⁸). Controls: for each hard prime, 20 primes p′ ≡ p (mod 840) drawn uniformly at random from
[p/2, 2p], excluding all hard-list members, **without replacement across the whole design** (disjoint). Statistic:
stratified difference Δ = mean_h(Q(h) − c̄_h) with s.e. from the binomial variances; **effect bound** registered:
on the 145-member noprime set, "no effect of size ≥ 0.10" is accepted if the 95 % CI of Δ lies in (−0.10, 0.10);
"effect" if |Δ/s.e.| ≥ 3. q-to-word construction (fixed now): for the least q | X with (840/q) = −1, the candidates
f = qm, m ≤ 64, f ≡ 3 (mod 4), f ≤ (4p + 1)/3; Y(p) := [some candidate is a (★) witness: (−p mod f) | (f + 1)/4].
Decoy: for the same p, q′ = a prime with (p/q′) = −1, q′ ∤ X, q′ ≡ q (mod 8), |q′ − q| ≤ 0.1 q (nearest such),
same construction. Kill K9: Y(q) − Y(q′) not ≥ 3σ above 0 ⟹ q | X carries no word-building information beyond being
a non-residue of its size; HOT LEAD only if Y = 1 on every hard prime and the excess is significant.

### 1.6 Deviations from the registration (complete ledger; added after the internal review)
| item | registered | done | consequence |
|---|---|---|---|
| I6 K6a | ≥ 5 points each for d = 1, 3, mpmath ≥ 30 digits, rel. error < 10⁻¹⁵ | first draft: 28 double-precision points only (claimed "pass" — wrong); after review: d = 1 five points at 30 digits (rel ≤ 4.4·10⁻³⁰), d = 3 five points at **20** digits (rel ≤ 2.1·10⁻¹⁹) | criterion met; d = 3 at 20 instead of 30 digits |
| I6 K6b | discontinuity → decide mock / not mock | the jump claim was withdrawn after review; only "S₁, S₂ ∉ M₁" (d = 1) is proved | K6b inconclusive |
| I5 | σ1 "coset swap with unipotent correction, nearest in a fixed norm", σ3 "continuant-flip maps" | replaced (before any run) by the precise ρ_L, ρ_R, ρ_C, s∘ρ_C, s∘ρ_R∘s maps of §3 (the unipotent-orbit reading of σ1); σ3 was not implemented (the length-changing continuant identity M(a)M(1)M(b) = M(a − 1)M(b − 1) maps words with y = 1 to length-2 words, not to T_n) | the registered σ1/σ3 wording was not tested literally |
| #10 | R-sm (least non-square non-residue d) | not run separately: the least non-residue is prime, so R-sm = NP | none |
| #10 | GA on all primes | GA on every 30th prime (cost) | none for its verdict (coverage ≈ 0.6 %) |
| #10 | decoy uniform in the window | candidate list capped at 4 096 (only binds for huge windows, i.e. GA's large d) | GA decoys not exactly uniform |
| Pell | null = uniform on the conic mod ℓ | registered null run; then post-hoc 2-adic recalibration (§5) | registered-null "signal" reinterpreted; disclosed |
| I9 | 20 controls per hard prime | rejection sampler with a 200 000-draw budget; partial strata (listed in §6) | disclosed; strata with 0 controls dropped |
| I9 | decoy with abs(q′ − q) ≤ 0.1 q | run as registered; amended (nearest) and two-sided decoys added post hoc | both reported; diagnosis scoped |

## 2. I6 — an explicit fibre law (PROVED + verified); the level sum has no finite-index law with small periods (PROVED, scoped)

### 2.1 Theorem F (S-transformation of a partial divisor Lambert series; PROVED, classical ingredients)
Let M ≥ 1, 1 ≤ α, β ≤ M, a = α/M, b = β/M ∈ (0, 1], and assume a, b ≠ 1 (the case needed: d = 1 is
(M, α, β) = (4, 3, 3), d = 3 is (12, 11, 11); in general the d-fibre is Φ_d = L for (4d, 4d − 1, 4d − 1)). Put
  L(z) := Σ_{A ≡ α, B ≡ β (M); A, B ≥ 1} e(ABz),   L*_{u,v}(w) := Σ_{m,n ≥ 1} e(mu + nv + mnw)   (z, w ∈ ℍ),
w := −1/(M²z), S₁ := L*_{a,b} + L*_{−a,−b}, S₂ := L*_{a,−b} + L*_{−a,b}. Then for z ∈ ℍ
  **L(z) = (M²z)⁻¹ L*_{a,b}(w) + E(z) + Ψ(z)**,
  E(z) = (i/(2πM²z))·(−γ − log(−2πiM²z) − ψ(a) − ψ(b)) + (½ − a)(½ − b)       (ψ = digamma, principal log),
  Ψ(z) = (i/(2πM²z)) ∫_{C₋} [ S₁(tw)·t/(t − 1) − S₂(tw)·t/(t + 1) ] dt,
C₋ = a ray from 0 to ∞ passing **below** t = 1 with arg(tw) ∈ (0, π) along it. Ψ continues analytically to
z ∈ ℂ ∖ (−∞, 0] (rotate C₋ continuously within arg t ∈ (−π, 0]: the pole t = 1 is never crossed, the pole t = −1 is
reached only as z → (−∞, 0) from below). [Review fix: an earlier sentence asserting the jump of Ψ across (−∞, 0) was
withdrawn — it evaluated a q-series on the real boundary, and no boundary-value prescription was given.]
*Proof.* On z = iy: Mellin, ∫₀^∞ L(iy)y^{s−1}dy = Γ(s)(2πM²)^{−s}ζ(s, a)ζ(s, b) (Re s > 1). Shift the inverse
Mellin integral to Re s = c′ ∈ (−1, 0): residues at s = 1 (ζ(s, a) = 1/(s − 1) − ψ(a) + O(s − 1), with
Γ(s)X^{−s} = X⁻¹(1 − (γ + log X)(s − 1) + …), X = 2πM²y) and s = 0 (ζ(0, a) = ½ − a) give E. On the remaining line put
s = 1 − w and use Hurwitz's formula ζ(1 − w, a) = Γ(w)(2π)^{−w}[e^{−πiw/2}F(a, w) + e^{πiw/2}F(−a, w)],
F(u, w) = Σ e(nu)n^{−w}. With Γ(1 − w)Γ(w) = π/sin πw and π e^{∓πiw}/sin πw = π cot πw ∓ πi, the integrand splits into
(i) ∓πi·Γ(w)Y_N^{−w} → the exponentials e^{−Y_N}, Y_N = 2πN/(M²y), i.e. q-series in w; (ii) Γ(w)π cot(πw) and
Γ(w)π/sin(πw), on 1 < Re w < 2 the Mellin transforms of k₁(Y) = PV∫₀^∞ e^{−Yt} t/(t − 1) dt = 1/Y − e^{−Y}Ei(Y)
and k₂(Y) = −∫₀^∞ e^{−Yt} t/(t + 1) dt = e^{Y}E₁(Y) − 1/Y (from ∫₀^∞ x^{μ−1}/(1 ± x)dx = π/sin πμ, PV π cot πμ, plus the
residue ±1/Y at w = 1). Summing over N (absolutely convergent: k_{1,2}(Y) = O(Y⁻²)) gives
L(iy) = E + (2M²z)⁻¹(L*_{a,b} − L*_{−a,−b})(w) + (i/2πM²z)[PV∫S₁(tw)t/(t−1)dt − ∫S₂(tw)t/(t+1)dt]. Finally
PV∫ = ∫_{C₋} − πi·Res_{t=1} = ∫_{C₋} − πi S₁(w), which turns the q-series part into (M²z)⁻¹L*_{a,b}(w). Both sides are
holomorphic on ℍ, so the identity extends from iℝ₊. L*_{u,v}(τ) is bounded as τ → 0 in sectors (its Mellin transform
Γ(s)F(u,s)F(v,s) has no pole at s = 1 for u, v ∉ ℤ), so the integrals converge at t = 0. ∎
*Numerical check (K6a).* `scripts/z70_loose_i6law.py` → `data/z70/loose/i6_law_check.txt`: direct L vs the law at
7 points each for (4, 3, 3) [d = 1], (12, 11, 11) [d = 3], (4, 1, 1), (12, 7, 5), including Re z ≠ 0, in **double
precision**: max relative error **8.9·10⁻¹⁵** (review correction; the first draft misread the log as 2.9·10⁻¹⁵), max
absolute error 3.9·10⁻¹⁶, against term sizes ≈ 10⁻²–10⁻¹ — i.e. agreement at machine precision. Plus one 34-digit
mpmath point for d = 1 (`scripts/z70_loose_i6mp.py` → `i6_law_mp34.txt`, z = (0.05 + 0.15i)·16/90: |L − law| = 1.8·10⁻³⁵, relative 6.7·10⁻³⁵; small-τ region via the asymptotic Mellin series to 60 terms).
**K6a as registered (≥ 5 points for each of d = 1, 3 in ≥ 30-digit arithmetic, relative error < 10⁻¹⁵)**: the
first draft claimed a pass without having run it (review fix). Post-review multiprecision grids:
d = 1 (`i6_k6a_mp_d1.txt`, 30 digits, tanh-sinh): 5 points done (z₀ = 0.5i, 0.25i, 0.3 + 0.4i, −0.2 + 0.5i,
0.05 + 0.15i, z = z₀·1.6/9), relative errors 8.3·10⁻³⁴ … 4.4·10⁻³⁰ — **criterion met for d = 1**;
d = 3 (`i6_k6a_mp_d3.txt`, **20 digits** (deviation: 30-digit tanh-sinh was too slow), Gauss–Legendre, asymptotic
series below |τ| = 7·10⁻⁴): 5 points (z₀ = 0.5i, 0.3 + 0.4i, −0.2 + 0.5i, 1.0 + 0.3i, 0.13 + 0.08i, z = z₀·1.6/121), relative errors 2.2·10⁻²¹ … 2.1·10⁻¹⁹ — criterion (< 10⁻¹⁵) met at 20 rather than 30 digits. The identity itself is PROVED; the double-precision points with
relative error between 10⁻¹⁵ and 10⁻¹⁴ are at the double-precision floor. A first run with a too-coarse small-τ series (switch at |τ| < 2·10⁻³) gave 10⁻⁸
errors for M = 12; with the switch at 2·10⁻⁴ the errors fell to 10⁻¹⁷ at a test point.

### 2.2 What the period is (K6b): an integral transform of non-modular series — mock status NOT decided (Assessment + one PROVED ingredient)
Ψ is an integral transform, along the ray C₋, of the dual partial Lambert series S₁, S₂ themselves (substituting
τ = tw gives a Cauchy-type kernel τ/(w(τ ∓ w)); rotating that path to iℝ₊ would cross τ = w in the S₁ term and pick up
a residue S₁(w), so the "Eichler integral along iℝ₊" form needs that residue term — the first draft omitted it).
For a mock modular form of weight 1 the analogous period would be an Eichler integral of a modular shadow g ∈ M₁.
**PROVED ingredient:** S₁, S₂ are not weight-1 modular forms of any level — shown here for d = 1 only: c(N) := Σ_{mn=N}(−i)^{m+n} equals τ(N) for N ≡ 3 (4) and −τ(N) for N ≡ 1 (4) (all m, n odd;
m + n ≡ 0 or 2 (mod 4) according as mn ≡ 3 or 1), so the coefficients of S₁ = 2 Re c are ±2τ(N) on odd N, whose
partial sums over N ≡ 3 (4) grow like x log x, while every f ∈ M₁(Γ₁(L)) (and its restriction to a residue class)
has Σ_{n≤x} a_f(n) = O(x) (Eisenstein part: Σ_{dm≤x} χ(m)ψ(d) with χψ odd, one character non-trivial; cusp part
o(x)). **What is NOT proved (review fix):** that this excludes a mock completion. That would need a uniqueness
statement identifying any shadow with the integrand of Ψ (boundary prescription, residue accounting, choice of the
q-series part), which is not supplied; nor is a quantum-modular object (quantum set, boundary values) specified.
*Assessment:* the structure resembles the Bettin–Conrey period function of Σ τ(n)qⁿ (an analytic period on a slit
plane, built from the weight-0 Eisenstein content τ(N)) rather than a mock form; K6b is therefore *inconclusive as a
theorem* and only suggestive. The fibre is the odd-character weight-1 theta part (modular) plus this
quantum part (`METAPLECTIC_ES.md` Thm K; consistent).
*Literature note.* The case M = 1 (Σ τ(n)qⁿ) is Bettin–Conrey, "Period functions and cotangent sums", Algebra &
Number Theory 7 (2013) — quoted from memory, not re-checked here; Theorem F is proved above independently and does
not rely on it.

### 2.3 Lemma K and Theorem LS — the level sum G has no transformation law of finite level (PROVED)
**Lemma K (singular coefficients of G).** For coprime a₀, c ≥ 1 and w → 0 in any sector |arg w − π/2| ≤ π/2 − δ,
  G(a₀/c + w) = κ(a₀/c)·log²(1/|w|)/(−2πi w·8) + o(log²(1/|w|)/|w|),   κ(a₀/c) = 1[c odd]·μ(c)/c².
(So G(iy) ~ log²(1/y)/(16πy).) *Proof.* Split (a, b, d) into classes mod c; on a class the phase e(a₀(4abd − a − b)/c)
is constant, and the count of class members with 4abd − a − b ≤ x is (x/(8c³))log²x + o(x log²x). Indeed:
(i) #{class members: 4abd ≤ x} = Σ_{a≡α, b≡β, ab≤x/4}(x/(4c·ab) + O(1)) = x log²x/(8c³) + O(x log x);
(ii) K-squeeze for the perturbation: the members with min(a, b, d) ≤ K number O_K(x log x) (one coordinate bounded
leaves a two-variable divisor count), and when a, b, d > K we have a + b ≤ 2ab ≤ 4abd/(2K), so
4abd(1 − 1/(2K)) ≤ 4abd − a − b ≤ 4abd; hence the count lies between the counts of (i) at x and at x/(1 − 1/2K),
i.e. it is (1 + O(1/K))·x log²x/(8c³) + O_K(x log x); let K → ∞ (review fix: this step was abbreviated). Partial summation: Σ u_n e^{−ns} = s∫U(t)e^{−st}dt,
and s∫ t log²t e^{−st}dt = (log²(1/s) + O(log 1/|s|))/s uniformly in the sector, while an o(t log²t) remainder
contributes o(log²(1/|s|)/|s|) because |s| ≍ Re s there. Summing the classes gives the factor
S(a₀, c)/c³ = c⁻²Σ_{α,β mod c, c | 4αβ} e(−a₀(α + β)/c) (the δ-sum is c·1[c | 4αβ]). This is independent of a₀
(α ↦ a₀⁻¹α permutes the set), multiplicative in c (CRT), and the local factors are evaluated by valuations: the sum
of e(−α/ℓ^e) over α of exact valuation i is the Ramanujan sum c_{ℓ^{e−i}}(1) ∈ {1 (i = e), −1 (i = e − 1), 0}; for
ℓ odd the admissible pairs give −1 − 1 + 1 = −1 at e = 1 and 1 − 1 − 1 + 1 = 0 at e ≥ 2; for ℓ = 2 the condition is
vacuous for e ≤ 2 (full character sums, 0) and for e ≥ 3 the four surviving pairs again give 0. Hence
S/c³ = ∏ = μ(c)/c² for odd c and 0 for even c. ∎ (`scripts/z70_loose_i6kappa.py` → `i6_kappa.txt`: brute-force check of
the δ-step, a₀-independence, multiplicativity and the zero set for c ≤ 121. `scripts/z70_loose_i6sing.c` →
`i6_singular_check.txt`: G(r + iy)/G(iy) from R(n), n ≤ 3·10⁶, at y = 10⁻³ … 3·10⁻⁵ — drifts towards the predicted
values with the expected O(1/log(1/y)) lower-order terms, e.g. r = 1/3: −0.186, −0.163, −0.156 → −1/9; r = 1/2:
0.035, 0.017, 0.013 → 0; r = 1/9: ≈ 0.017 → 0; illustration only.)

**Theorem LS (no small-period law for the level sum; PROVED).** There is no finite-index subgroup Γ ⊂ SL₂(ℤ),
weight k ∈ ℝ and multiplier v : Γ → S¹ such that for every γ = (∗ ∗; c d) ∈ Γ the holomorphic cocycle
h_γ(z) := G(z) − v(γ)⁻¹(cz + d)^{−k}G(γz) (z ∈ ℍ) satisfies h_γ(r + iy) = o(y⁻¹log²(1/y)) (y → 0⁺) at every
rational r ≠ −d/c. (Equivalently for a finite-dimensional vector-valued system containing G with finite-image
representation, **provided** its cocycles satisfy the same radial bound — pass to the kernel.)
**Corollary LS-M (PROVED for cuspidal shadows; extension below).** G is neither a modular form nor the holomorphic
part of a harmonic Maass form F of real weight k on a finite-index Γ with unitary multiplier whose shadow ξ_k F is a
**cusp** form. *Proof.* If k ≥ 2 the shadow (weight 2 − k ≤ 0 cusp form) is 0 and
G itself is modular (h_γ ≡ 0). If k < 2, F⁻(z) = c_k∫_{−z̄}^{i∞} g^c(τ)(−i(τ + z))^{−k}dτ with g a cusp form of weight
2 − k, |g(τ)| ≤ C(Im τ)^{(k−2)/2}; on the vertical path τ = −x + it (z = x + iy) |τ + z| = t + y, so |F⁻(x + iy)| ≤ C∫_y^1 t^{(k−2)/2}(t + y)^{−k}dt + O(1) = O(y^{−k/2} + log(1/y) + 1) = o(y⁻¹), uniformly in x. Since F is
modular, h_γ = −F⁻(z) + v⁻¹(cz + d)^{−k}F⁻(γz), and at z = r + iy, Im γz ≍ y, so h_γ(r + iy) = o(y⁻¹): LS applies. ∎
*Extension (added after the review; PROVED modulo the standard regularised description of F⁻, quoted from memory —
Bruinier–Funke 2004 / the Bringmann–Folsom–Ono–Rolen monograph):* the same holds when the shadow g is any holomorphic
modular form of weight 2 − k (non-zero constant terms allowed). Then F⁻(z) = c·b̄₀·Y_k(y) + c′∫_{−z̄}^{i∞}(g^c(τ) − b̄₀)
(−i(τ + z))^{−k}dτ with Y_k(y) = y^{1−k} (k ≠ 1), log y (k = 1). Case split: for k > 2 the shadow has negative weight,
so it vanishes and F⁻ = 0 (G modular, h_γ ≡ 0); for k = 2 the shadow is a constant and F⁻ = O(y⁻¹); for k < 2 the
moderate-growth bound |g(τ) − b₀| ≤ C(Im τ)^{k−2} near every cusp gives, on the
same vertical path, ∫_y^1 t^{k−2}(t + y)^{−k}dt = y⁻¹∫_1^{1/y}u^{k−2}(1 + u)^{−k}du = O(y⁻¹) uniformly in x. So for k < 2,
F⁻ = O(y⁻¹ + |Y_k(y)|) = o(y⁻¹log²(1/y)) at every rational (|Y_k| = y^{1−k} = o(y⁻¹) as k < 2), and LS applies.
*Not covered:* harmonic forms of exponential growth at some cusp (weakly holomorphic shadows / principal parts),
quantum modular forms in Zagier's sense (objects defined on rational boundary points, possibly with renormalised
boundary values — their cocycles are not the upper-half-plane cocycles bounded here), vector-valued systems with
infinite-image representation or without the radial bound, and infinite-level constructions.
*Proof.* Γ has finite index, so U^j = (1 0; j 1) ∈ Γ for some j ≥ 1 (pigeonhole on the cosets ΓUⁱ). Choose a prime ℓ ∤ j
and an integer r ≥ 1 with jr ≡ −1 (mod ℓ²). Then U^j(r) = r/(jr + 1) is in lowest terms with ℓ² | jr + 1, so
κ(U^j r) = 0, while κ(r) = κ(0) = 1 ≠ 0. At z = r + iy, U^j z − U^j r = iy/((jz + 1)(jr + 1)) lies in a fixed sector
with modulus ≍ y, so by Lemma K G(U^j z) = o(y⁻¹log²(1/y)) and |(jz + 1)^{−k}| is bounded; hence
h_{U^j}(r + iy) = G(r + iy) + o(·) ~ κ(0)·log²(1/y)/(16πy), contradicting the hypothesis (r ≠ −1/j since r > 0). ∎
Contrast (PROVED by the same class-splitting, one log instead of two): the single fibre
g_d(z) := Σ_{a,b ≥ 1} e((4abd − a − b)z) = e(−z/4d)Φ_d(z/4d) has leading singular coefficient (relative to
g_d(iy) ~ log(1/y)/(8πdy)·…) κ_d(a₀/c) = c⁻¹Σ_{α mod c, 4dα ≡ 1 (c)} e(−a₀α/c) = c⁻¹e(−a₀·\overline{4d}/c) if
gcd(c, 4d) = 1 and 0 otherwise — finite-level data (it depends on c only through gcd(c, 4d) and the class of a₀
modulo c), consistent with Theorem F. Summing over d, the phases e(−a₀\overline{4d}/c) average over the units mod c
(weights ≍ 1/d) into a Ramanujan-sum-type quantity, which is how μ(c)/c² — vanishing at every non-squarefree c —
appears in Lemma K: the obstruction is exactly the **infinite** union of levels 4d. The mechanism of the proof is the vanishing of the log² singularity
at every non-squarefree or even denominator (μ(c)/c²), i.e. the arithmetic of the *three* free divisor variables.

### 2.4 Squares (F1) and verdict for I6
* F1: r_d(4dm² + 1) = 0 (T1 at 4 ∣ 4d) is a property of coefficients; Theorem F holds identically for every
  coefficient sequence of the form ζ(s, a)ζ(s, b) and is equivalent (by Mellin) to the Hurwitz functional equations — a
  Voronoi-type summation statement. It cannot distinguish 4dm² + 1 from 4dp + 1; it does not use primality anywhere.
  Lemma K's κ is likewise insensitive to n. (Assessment.)
* **Verdict I6: narrowed.** (S1) delivered: an explicit S-transformation with boundary terms E and period Ψ for the
  d = 1 and d = 3 fibres (PROVED; numerically verified — see K6a record). (S2) inconclusive as a theorem: the period is
  an integral transform of dual partial Lambert series that are not in M₁ (PROVED for d = 1), but no shadow-uniqueness
  argument excludes a mock completion. (S3) **the levels do not sum to a small-period law**: Theorem LS excludes every
  finite-index law whose cocycles are o(y⁻¹log²(1/y)) at rationals, hence (Cor. LS-M) modular forms and harmonic Maass
  forms with cuspidal shadow (and, modulo the standard regularised formula, any holomorphic shadow); other classes
  (exponential-growth harmonic forms, boundary-defined quantum forms, infinite-image vector-valued systems, laws with
  infinitely many levels — METAPLECTIC hatch H-A) are not excluded. Pointwise use of any of
  this would still need a single-coefficient statement (H-E), which these generating-function laws do not provide.

## 3. I5 — candidate involutions (precise list, committed BEFORE running them on T₇₃ / T₄₀₉)
Matrix form: w = (x, y, z) ↦ γ_w = (a n; c d) = (xy − 1  n; y  zy − 1) ∈ SL₂(ℤ); T_n ↔ {γ ∈ SL₂(ℤ): upper-right n,
c ≥ 1, a ≡ d ≡ −1 (mod c), a, d ≥ c − 1}. s = swap (x, y, z) ↦ (z, y, x) ⟺ (a, d) ↦ (d, a). L := (1 0; 1 1). The
three unipotent actions preserving the upper-right entry: left γ ↦ L^kγ (keeps a), right γ ↦ γL^k (keeps d),
conjugation γ ↦ L^kγL^{−k}. For each action the orbit of w inside T_n is finite (a, d ≥ 0 bounds k).
* **ρ_L, ρ_R, ρ_C:** order-reversal of the (finite, linearly ordered by k) orbit of w under the left / right /
  conjugation action — involutions; fixed points = middle elements of odd orbits.
* **σ_C := s∘ρ_C** (s maps C-orbits to C-orbits reversing the order, so s and ρ_C commute; an involution); fixed
  points: words whose C-orbit is s-stable with s(w) = ρ_C(w).
* **σ_R := s∘ρ_R∘s** (the mirror of ρ_R; expected to coincide with ρ_L — a consistency check of the code; it does).
  [The first draft of this bullet also floated a composite σ_LR; it was dropped before any run as not an involution.]
* **τ_xy (x ↔ y exchange):** (x, y, z) ↦ (y, x, (n + y)/(xy − 1)) on D_xy := {xy ≥ 2, (xy − 1) | (n + y)} — an
  involution of D_xy, fixed points x = y. **σ2a** := τ_xy on D_xy, τ_yz = sτ_xy s on D_yz ∖ D_xy, s elsewhere;
  **σ2b** := τ_xy on D_xy, s elsewhere. (Each must first be checked to be an involution of T_n.)
Stage-1 test: involution on T₇₃ and T₄₀₉, ≠ s, Fix ⊆ C_p at both (C_p: 4 | x, 4 | y, 4 | z, or x ≡ y ≡ 3 (4), or
z ≡ y ≡ 3 (4)). Controls T₉, T₁₀₅ (C = ∅) printed.

### 3.1 Stage-1 result (`scripts/z70_loose_i5.py` → `data/z70/loose/i5_stage1.txt`): all seven candidates DEAD |T₇₃| = 23 (|C₇₃| = 8), |T₄₀₉| = 39 (|C₄₀₉| = 8), |T₉| = |T₁₀₅| = 11 (C = ∅).
| candidate | involution on T₇₃, T₄₀₉ | #Fix at 73 / 409 | non-certificate fixed points (examples) | verdict |
|---|---|---|---|---|
| ρ_L | yes | 15 / 23 (8 in C) | (2, 2, 25), (2, 13, 3) | dead |
| ρ_R | yes | 15 / 23 | (1, 2, 74), (1, 3, 37) | dead |
| ρ_C | yes | 15 / 23 | (1, 75, 1), (2, 2, 25) | dead |
| σ_C = s∘ρ_C | yes | 5 / 5 (0 in C) | (1, 2, 74), (1, 75, 1) | dead |
| σ_R = s∘ρ_R∘s (= ρ_L) | yes | 15 / 23 | as ρ_L | dead |
| σ2a, σ2b (x ↔ y exchange) | **no** (not involutions) | — | — | dead |
The unipotent orbits are mostly singletons (their reversals fix most words); the x ↔ y exchange is an involution only on
its domain D_xy and the patching by s or τ_yz breaks it. Stage 2 not reached.

### 3.2 Lemma P5 — where the odd parity of T_p lives (PROVED; check `i5_lemma_check.txt`)
Let p ≡ 1 (mod 4) be prime. Split T_p = Triv_p ⊔ T′_p, Triv_p := words with a letter equal to 1. Then
(a) |Triv_p| = 3τ(p + 1) − 1 (odd), (b) |T′_p| is even (s acts freely on T′_p), (c) Triv_p ∩ C_p ≠ ∅ iff p + 1 has a
prime factor ≡ 3 (mod 4).
*Proof.* (a) x = 1: z(y − 1) = p + 1 (τ(p + 1) words); z = 1: symmetric; y = 1: (x − 1)(z − 1) = p + 1 (τ(p + 1)
words with x, z ≥ 2); the only overlap is (1, p + 2, 1); τ(p + 1) is even since p + 1 ≡ 2 (mod 4) is not a square.
(b) s-fixed words satisfy x(xy − 2) = p, forcing x = 1 (Lemma P). (c) p + 1 ≡ 2 (mod 4). x = 1 words (1, y, z): 4 ∤ z
(z | p + 1); 4 | y needs y − 1 ≡ 3 (mod 4), an odd divisor ≡ 3 (mod 4) of p + 1; y ≡ z ≡ 3 needs z ≡ 3 (mod 4), again
such a divisor; z = 1 symmetric; y = 1 words (x, 1, z): 4 | x needs x − 1 ≡ 3 (mod 4) | p + 1, and the type-(iii)
conditions need y ≡ 3. An odd divisor ≡ 3 (mod 4) exists iff the odd part of p + 1 has a prime factor ≡ 3 (mod 4).
Conversely such a prime q gives the word (1, q + 1, (p + 1)/q) when q ≡ 3 (mod 4) with 4 | q + 1. ∎
(Checked for all 383 primes p ≡ 1 (4) < 6000: 0 violations; 54 of them, starting 73, 193, 313, 337, 409, have no
trivial certificate.)
**Consequence.** The odd parity that a Zagier-type argument needs is carried *entirely* by the divisor words of p + 1
(the swap-free part T′_p is even). At every prime p for which p + 1 has **no prime factor ≡ 3 (mod 4)** (54 of the 383
primes p ≡ 1 (4) below 6000, e.g. 73, 409; whether there are infinitely many is not addressed here) a
certificate-fixed involution σ cannot preserve the decomposition Triv ⊔ T′: it must pair at least one divisor word of
p + 1 with a non-trivial word — i.e. it must be an arithmetic transport from divisors of p + 1 to the (MS)/(W)
certificates. That is the B2 event again in parity clothing; no such transport is known.
### 3.3 Round 2 — a grammar search (pre-registered here before running)
Lemma P5 says a candidate must move divisor words of p + 1 into T′_p. Grammar: priority gluings
σ(w) := P_i(w) for the first i with w ∈ Dom(P_i), else s(w), with (P_1, …, P_k), k ≤ 3, distinct, drawn from
{τ_xy, τ_yz, μ, μ^s, ρ_L, ρ_R, ρ_C, s∘ρ_C}, where μ: (x, 1, z) ↦ (1, x, z − 1) and (1, y, z) ↦ (y, 1, z + 1) (the
divisor-word exchange y = 1 ↔ x = 1; an involution on its domain), μ^s := s∘μ∘s. 8 + 56 + 336 = 400 maps. Stage 1:
involution on T₇₃ and T₄₀₉, ≠ s, Fix ⊆ C_p at both; stage 2: every prime p ≡ 1 (4) < 2000 and failure (not an
involution, or a non-certificate fixed point) at 9 and 105. Survivor of both = HOT LEAD.

*Result* (`scripts/z70_loose_i5grammar.py` → `i5_grammar.txt`): 400 maps; 246 are involutions on both T₇₃ and T₄₀₉
but have non-certificate fixed points at both; 154 are not involutions at either. **No stage-1 survivor.**

**Verdict I5 (narrowed):** the seven registered candidate maps and all 400 candidate expressions of the round-2 grammar fail stage 1 on T₇₃/T₄₀₉ (not all are distinct maps; many are not involutions);
Lemma P5 explains why any such map must be arithmetic in p + 1. Not killed in general (a map certificate-fixed only at
primes is not excluded), but no candidate exists. F1: T₉, T₁₀₅ have C = ∅ and odd |T| — any passing family must fail
there; F2: no candidate survived to the C-even question.

## 4. IDEAA #10 — Type I with an explicit d-selection rule: DEAD as a forcing rule (CERTIFIED failures)

**Lemma S (exact slice bound; PROVED).** Fix p and d. The Type I slice {(a, b, c, e) : 4abd = pe + 1, ce = a + b} is
non-empty iff it has a point with a ≤ b, and every such point has f := (4a²d + 1)/e ≤ p + 2 and a ≤ (p + 1)/(2d).
*Proof.* The equations are symmetric in (a, b), so swap if needed. If a ≤ b then 4a²d ≤ 4abd = pe + 1, so
fe = 4a²d + 1 ≤ pe + 2 and f ≤ p + 2/e ≤ p + 2. In K3 form f = 4acd − p with c ≥ 1, so 4acd = p + f ≤ 2p + 2 and
a ≤ (p + 1)/(2cd) ≤ (p + 1)/(2d). ∎ Hence the slice at (p, d) is decided exactly by scanning a ≤ (p + 1)/(2d) and
f ≡ −p (mod 4ad), f ≤ p + 2, f | 4a²d + 1 (`scripts/z70_loose_typeIfull.c`; fixture (1033, 132): a = 1, f = 23 ✓).

**Runs.** `scripts/z70_loose_typeI.c` (A = 2000 as registered; decoy as registered; fixture found, a = 1):
`range 5e7 2000 30 0` and `range 1e8 2000 30 5e7` → `data/z70/loose/typeI_range_*.txt` (all 719 781 primes
p ≡ 1 (24) ≤ 10⁸; the Gaussian rule GA on every 30th prime — deviation for cost, irrelevant to its verdict); `list`
mode on the hard lists → `typeI_list_*.txt`. (The two range files' first line prints a stale "a=0" for the fixture —
an argument-evaluation-order bug fixed afterwards; the fixture *was* found, as the corrected list runs show.)

| rule | coverage, p ≡ 1 (24) ≤ 10⁸ (A = 2000) | vs matched decoy (McNemar z) | (★)-zeros 14 | 𝔊*-zeros 38 | noprime 231 | R₈-zeros 12 |
|---|---|---|---|---|---|---|
| NP d = n_p (mean d 7.7, max 67) | 0.9739 | +107.9 (pooled; size-confounded, see below) | 13 | 35 | 214 | 12 |
| Q3 least prime ≡ 3 (4) non-residue | 0.9079 | −62.9 | 12 | 34 | 186 | 12 |
| CF first non-residue partial quotient | 0.7770 (846 undefined) | +12.6 | 6 | 22 | 165 | 9 |
| GA Gaussian combination | 0.006 (subsample 23 993) | +0.7 | 0 | 4 | 3 | 0 |

**Exact (untruncated) failures of NP (CERTIFIED by Lemma S, `typeI_np_fail_exact.txt`):** of the 20 distinct hard
primes where NP missed with A = 2000 (21 rows; 102 001 is on two lists), a full scan finds points for 14 (with a up to
102 291 — the truncation matters) but the
**d = n_p slice is exactly empty** at 102 001 (d = 23; a (★)- and 𝔊*-zero), 3 361 (d = 11), 210 961 (23),
1 063 969 (17), 27 020 569 (37), 103 819 081 (13) (all ≡ 1 (24), all in 𝔐; the last five are noprime primes,
102 001 is on the (★)/𝔊* lists).

**Two-element menu (exploratory, after the kill; `typeI_np_menu_exact.txt`, exact by Lemma S).** At each of the six
exact NP failures the *second* prime non-residue d gives a non-empty slice (102 001: d = 29; 3 361: 13; 210 961: 29;
1 063 969: 29; 27 020 569: 41; 103 819 081: 19). *Assessment:* for any bounded d the heuristic expected slice size
grows like (log p)²/d, so a fixed finite menu would plausibly fail only finitely often — but it is then a finite
union of p-independent covering families (p ≡ −f (mod 4ad), f | 4a²d + 1, a unbounded): proving it is exactly the
B1/B2 problem; and n_p is unbounded, so "d = n_p" is not even a bounded menu. Coverage at A = 2000 is flat in p
(0.9736 on p ≤ 5·10⁷, 0.9742 on (5·10⁷, 10⁸]) but the truncation A = 2000 confounds any trend (Lemma S allows
a ≤ (p + 1)/2d).

**Kill tests.** K10a fires for every rule (best 97.4 % < 99.9 %). K10b fires (NP fails exactly at six hard primes).
K10c: the decoy comparison is uninformative for NP — the least non-residue has no admissible smaller decoy, so every
decoy is larger and the +107 measures size (expected slice count ≍ log²p / d); Q3 is far *below* its decoys
(restricting to primes ≡ 3 (4) hurts); CF's +12.6 has the same size asymmetry and is irrelevant at 78 % coverage.
**Verdict (#10): the four implemented rules are dead as forcing rules** (K10a with the registered truncation A = 2000;
K10b for NP also *exactly*, by Lemma S, at six hard primes; GA/Q3/CF failures on hard lists are at A = 2000 only).
Nothing here excludes other single-d rules or bounded menus (*Assessment/heuristic*, not a theorem: fixed-d Type I
slices are p-independent covering families over a with expected size ≍ (log p)²/d, so any such rule is a B1/B2-type
covering statement). F1: Type I at a square needs (d/m²) = −1 (Lemma T10), impossible — every rule fails at squares
by the Jacobi step. F4: reported in the table.

## 5. MINE open item — Pell residues modulo the letters: no witness-specific signal (EVIDENCE, non-rejection)

**Runs.** `scripts/z70_loose_pell.py` (witness files of `Z69_MINE` round 2; H_train 433 primes / H_test 407 primes,
all witnesses; controls 2 520 primes ≤ 2·10¹⁰, ≤ 10 witnesses each, seed 7071): unique letters ℓ ∈ {x, y, z},
5 ≤ ℓ ≤ 2·10⁵, two exact decoys each (MINE `decoy_exact`); T, U of T² − pU² = −1 reduced mod the lcm of all moduli of
the prime (CF of √p); exact null P₀(ℓ) per letter (validated against brute-force enumeration of the conic for 300
random (p, ℓ), and the Pell residues checked to satisfy T² − pU² ≡ −1). Analysis `scripts/z70_loose_pell_an.py`;
raw records `data/z70/loose/pell_*.jsonl.gz`; tables `pell_analysis_registered.txt`, `pell_analysis_recal.txt`.

**Registered result and its diagnosis.** With the registered null (uniform on the conic mod ℓ) the real letters
showed an excess D-rate over the null on both H halves (cluster z = +4.11 train, +4.08 test) — formally the signal
criterion for "real vs null". But the **exact decoys show the same excess** (+4.54, +4.76), the real-vs-decoy contrast
is null (−0.80, −1.29), and the excess sits in the letters with v₂(ℓ) = 2 (real / decoys: train +8.60 / +8.91; test
+8.33 / +8.78; controls +11.23 / +10.94 — `pell_analysis_registered.txt`; review correction: the first draft quoted
controls from a partial run). *Lemma (PROVED):* for p ≡ 1 (8), T² = pU² − 1 forces U odd and T² ≡ p − 1 ≡ 0 (mod 8),
so T ≡ 0 (mod 4); more precisely the 2-adic solutions are T ∈ 4ℤ₂ (Haar) with U = ±√((T² + 1)/p), and their image in
ℤ/2^v (v ≥ 1) is uniform on S_v = {T ≡ 0 (mod 2^{min(v,2)}), pU² ≡ T² + 1 (mod 2^{v+1})} (U mod 2^v is fixed up to sign by U² mod
2^{v+1}; T² mod 2^{v+1} depends only on T mod 2^v; for v = 1 the image is the single point (0, 1) mod 2). The conic mod
ℓ ignores this for every v₂(ℓ) ≥ 1 (the review exhibited (9 601, 56), (28 961, 24), (59 929, 24); the second review
found that v = 1 was still uncorrected — the conic mod 2 contains the non-liftable point (1, 0); e.g. (241, 22): 2/3 →
1/3). *Post-hoc correction (disclosed):* a partial fix (v = 2 only, `scripts/z70_loose_pell_recal.py`,
`pell_analysis_recal.txt`, superseded), then the full 2-adic null (`scripts/z70_loose_pell_recal2.py`: uniform on
conic mod m × S_v for all v ≥ 1; validated against the projection of the conic mod 16ℓ for 140 random (p, ℓ) with
v₂(ℓ) ∈ {1, …, 6}, the review's examples and (241, 22) — 0 mismatches) → `pell_*_recal2.jsonl.gz`,
`pell_analysis_recal2.txt`:

| sample | letters | D real / 2-adic null (cluster z) | decoys vs null (z) | real vs decoy, null-adjusted (z) |
|---|---|---|---|---|
| H_train | 14 186 | 0.2992 / 0.3001 (−0.36) | +0.01 | −0.83 |
| H_test | 13 384 | 0.2939 / 0.2946 (−0.28) | +0.28 | −1.28 |
| controls | 51 023 | 0.3356 / 0.3384 (−2.25) | −3.02 | +1.64 |
By role (x, y, z): real vs null |z| ≤ 2.18 (H_test x-letters −2.18), real vs decoy |z| ≤ 1.98 (H_test x-letters −1.98,
not replicated on train: +1.18). By 2-adic class all |z| ≤ 1.92 except the controls' odd-letter decoys (−2.38). The
controls show a small negative drift against the null that is **shared by real and decoy letters** (−2.25 / −3.02):
the local null is still slightly miscalibrated for that population (cause not identified — possibly global
constraints on the reduction of the fundamental unit at odd primes); it is not witness-specific.
**Verdict (EVIDENCE):** for residues of T, U, T + cU + s (|c| ≤ 3, |s| ≤ 2) and T ± 1, ± 2 modulo the witness letters,
**no difference from exact decoy letters was detected**, and after the 2-adic recalibration no departure of either
from the local null meets the signal criterion. This is non-rejection for the listed relations, not equivalence
(2-s.e. on the D-rate difference ≈ ±0.008 on each H half, ignoring clustering). Scope: letters ≤ 2·10⁵ only; gcd /
ratio relations and larger shifts untested. The registered-null "signal" was a 2-adic artefact of the null.

## 6. I9 — result (EVIDENCE; registered design with disclosed shortfalls; post-hoc checks after review)
Run: `uv run --with sympy python scripts/z70_loose_i9.py` (seed 7070) → `data/z70/loose/i9_run.txt`, rows
`i9_rows.json`; post-hoc `scripts/z70_loose_i9b.py` → `i9b_twosided.txt`; review checks `scripts/z70_loose_i9c.py` →
`i9c_review.txt`. Controls: same class mod 840, uniform in [p/2, 2p], no hard-list member, no reuse anywhere,
**target 20 per hard prime, drawn by rejection with a 200 000-draw budget**. *Shortfall (review fix):* the target was
not always met — control counts per stratum: (★) {1, 6, 20×7}; 𝔊* {0, 0, 13, 15, 20×16}; noprime {0, 0, 1, 1, 15,
20×140}; U⁽⁸⁾ {0, 0, 0, 5, 6, 11, 12, 12, 16, 20, 20}; R₈ {20×4}. Strata with 0 controls (5569, 9601 (𝔊*); 9601,
23041 (noprime); 1129, 2521, 3361 (U⁽⁸⁾)) are dropped — "none obtained within the budget" (the windows contain only a
handful of class members), not a verified absence. Means below are on the **retained strata**, controls weighted
equally per stratum; s.e. from the binomial model Σ c̄(1 − c̄)(1 + 1/m) (a model-based approximation; strata with one
control get variance 0).

| hard set (retained strata) | Q hard | Q controls (stratum-weighted) | Δ ± s.e. | z | 95 % CI |
|---|---|---|---|---|---|
| (★)-zeros (9) | 0.444 | 0.454 | −0.009 ± 0.158 | −0.06 | (−0.32, +0.30) |
| 𝔊*-zeros (18) | 0.444 | 0.565 | −0.121 ± 0.115 | −1.05 | (−0.35, +0.10) |
| noprime (143) | 0.566 | 0.588 | −0.022 ± 0.041 | −0.53 | (−0.101, +0.058) |
| U⁽⁸⁾-zeros (8) | 0.750 | 0.593 | +0.157 ± 0.179 | +0.88 | (−0.19, +0.51) |
| R₈-zeros (4, F2) | 0.500 | 0.637 | −0.138 ± 0.245 | −0.56 | (−0.62, +0.34) |
(The first draft's "Q hard" column mixed in the dropped strata and pooled the controls; Δ was already stratified.)

* **Registered effect bound:** noprime 95 % CI (−0.101, +0.058) — the equivalence criterion (−0.10, 0.10) is narrowly
  **not met** (met on the + side only); no effect criterion (|z| ≥ 3) fires. Reading (EVIDENCE): no detected
  difference; an excess of ≥ 0.10 of Q on hard primes is excluded at the model's 95 % level, a deficit of ≈ 0.10 is not.
* **q-to-word construction (registered decoy, |q′ − q| ≤ 0.1 q):** Y(q) ≈ 0.02–0.03 on controls, equal to the decoy
  rate (noprime controls 889 pairs: McNemar b = 23, c = 20, z = +0.46). The 10 % window is empty for most small q (772
  noprime-control Q-primes had no decoy) — a design flaw of the registration, and a strong selection (small q dropped).
  *Deviation (disclosed):* a window-free "nearest admissible prime" decoy gave an apparent excess (noprime controls
  1 661 pairs: Y(q) = 0.158 vs 0.094, z = +5.91). *Post-hoc checks:* on the subset of 1 233 Q-primes that have an
  admissible decoy on **both** sides, the nearest decoy gives Y(q) = 0.0681 vs 0.0673 (z = +0.09) and the two-sided
  decoy 0.0681 vs 0.0612 (z = +0.84); the 428 excluded Q-primes (small q, no admissible prime below) have
  Y(q) = 0.416 vs nearest-decoy 0.171 (second-review correction: the first version printed the all-Q-control mean
  0.158 here). So the +5.9 is confined to small q where every decoy is larger than q — **consistent with
  size/selection confounding** (Y falls roughly like (log q)/q); this is a diagnosis, not a proof of zero effect.
* On hard primes the construction rarely fires (noprime hard: Y(q) = 0.016 on 64 two-sided pairs).

**Verdict I9 (EVIDENCE, non-rejection):** with disjoint, size-window controls the X-coordinate classifier shows no
detected difference (|z| ≤ 1.05 everywhere); for this q-to-word construction and its eligible sample no excess of
Y(q) over size-matched non-residue decoys was detected (K9 fires as registered). Not tested: constructions using q
together with Y, and the small-q region without admissible decoys.

## 7. Falsifier table — final
| item | F1 odd squares | F2 C-even / R₈ | F3 composites | F4 known zeros |
|---|---|---|---|---|
| I6 Theorem F / LS | Theorem F is coefficient-blind (Mellin ⟺ Hurwitz functional equations); r_d(4dm² + 1) = 0 is invisible to it; LS is a no-go, needs no primality | the C-even fibres (d even) obey Theorem F too; no positivity claimed | n/a (no positivity claimed) | n/a |
| I5 involutions | T₉, T₁₀₅ printed as controls (C = ∅, #T odd); every candidate already fails at primes | no survivor reached the C-even question | 105 control as F1 | 73, 409 are themselves the stage-1 test (B₇₃ = ∅ in `Z69_TWIST.md` P′; 409 is a (★)-zero) |
| #10 rules | Type I at m² impossible (Lemma T10): every rule fails at squares by the Jacobi step | all rules cover all 12 R₈ zeros except CF (9/12), GA (0/12) — irrelevant, rules dead | not tested (rules use p's quadratic data) | NP exactly fails at 102 001 ((★)- and 𝔊*-zero) and five noprime primes |
| Pell letters | no witnesses at squares | n/a | n/a | H sets: null |
| I9 | Q = 0 at squares (every q ∣ X has (840/q) = +1) | 𝔐-members of R₈ zeros: Δ = −0.14 ± 0.25 | n/a | hard sets: null |
No idea survives as a mechanism, so the four screens are compatibility records only. **Not a HOT LEAD.**

## 8. Verdicts (one line each)
* **I6 — narrowed.** Fibre law: PROVED (Theorem F). Mock status of the fibres: not decided. Level sum: no finite-index
  law with small cocycles (Theorem LS, PROVED), hence not modular / not harmonic with cuspidal shadow (Cor. LS-M,
  PROVED) nor with any holomorphic shadow (extension, PROVED modulo the standard regularised formula); exponential-growth,
  boundary-defined quantum and infinite-level objects are not excluded.
* **I5 — narrowed.** 407 candidate expressions (7 registered + 400 grammar) fail stage 1; Lemma P5 locates the parity
  in the divisor words of p + 1.
* **IDEAA #10 — the four implemented rules are dead** (K10a, K10b fire; NP's failures CERTIFIED exact by Lemma S).
  Other single-d rules and bounded menus are not excluded (heuristically B1/B2-type).
* **Pell letters — non-rejection** for the listed relations against exact decoys; the registered-null excess was a
  2-adic miscalibration (PROVED source; recalibrated null — see §5 for the final numbers).
* **I9 — non-rejection.** No detected Q difference (equivalence band met on the + side only); no detected
  q-to-word excess in the eligible sample (K9 fires).

## 9. Proposed FRONTIER §7 / §6 text (do not edit FRONTIER here)
> **z70 LOOSE (Z70_LOOSE.md).** (i) *I6:* the fibre series Φ_d obey an explicit S-transformation (Theorem F: Mellin +
> Hurwitz; boundary term E; period = integral transform of the dual partial Lambert series, which for d = 1 are not
> weight-1 modular) — PROVED, numerically checked; whether a fibre admits a mock completion is not decided. The level
> sum G = Σ R(n)qⁿ has leading singular coefficients κ(a₀/c) = 1[c odd]μ(c)/c² at rationals (Lemma K), so it satisfies
> **no transformation law on any finite-index subgroup whose cocycles are o(y⁻¹log²(1/y)) at rationals** (Theorem LS);
> in particular G is not modular and not the holomorphic part of a harmonic Maass form with cuspidal shadow. Automorphic
> routes through G must use objects outside that class (e.g. infinitely many levels kept separate — hatch H-A).
> (ii) *I5:* 407 candidate cross-slice maps fail at 73/409; the odd parity of T_p is carried by the 3τ(p + 1) − 1
> divisor words (Lemma P5). (iii) *IDEAA #10:* four explicit d-rules fail (d = n_p leaves the Type I slice exactly
> empty at six hard primes; Lemma S makes single-slice decisions exact). (iv) *Pell residues mod letters:* no
> difference from exact decoys detected. (v) *I9:* no detected difference with disjoint controls.

## 10. Bottom line
The five loose ends were run. The new mathematics is on I6: an explicit, verified transformation law for each fibre,
and a scoped theorem that the sum over levels admits no finite-index transformation law with small cocycles — because
the log² singularity of G vanishes at every rational with even or non-squarefree denominator (κ = μ(c)/c²), which a
finite-index group action cannot respect. Whether the fibres are mock, and whether non-standard automorphic objects
could carry G, remain open. The other four items are negative within their tested scope: none of 407
candidate expressions is a certificate-fixed involution at both 73 and 409, no working Type I d-rule among four, no Pell-letter signal, no X-coordinate signal. ES remains OPEN.

## Reproduction (all with `ulimit -v 6000000`, `timeout ≤ 1800`)
* I9: `uv run --with sympy python scripts/z70_loose_i9.py`; `… scripts/z70_loose_i9b.py`; `… scripts/z70_loose_i9c.py`.
* #10: `gcc -O2 -o t scripts/z70_loose_typeI.c -lm; ./t range 50000000 2000 30 0; ./t range 100000000 2000 30 50000000;
  ./t list <file> 2000`; exact: `gcc -O2 -o f scripts/z70_loose_typeIfull.c; ./f <"p d" file>`.
* I6: `uv run --with numpy --with scipy python scripts/z70_loose_i6law.py`; multiprecision
  `uv run --with mpmath python scripts/z70_loose_i6mp.py [M α β dps small Re(z₀) Im(z₀) [gl]]` (grids: 4 3 3 30 3e-3 …
  → `i6_k6a_mp_d1.txt`; 12 11 11 20 7e-4 … gl → `i6_k6a_mp_d3.txt`); `python3 scripts/z70_loose_i6kappa.py`;
  `gcc -O2 scripts/z70_loose_i6sing.c -lm; ./a.out 3000000`.
* I5: `python3 scripts/z70_loose_i5.py`; `uv run --with sympy python scripts/z70_loose_i5grammar.py`.
* Pell: `uv run --with numpy --with sympy --with cypari2 python scripts/z70_loose_pell.py <wit> <list> <cap> <seed> <out>`
  (witness files = `zcat data/z69/mine/{H,CTRL}_witnesses.txt.gz`; lists `data/z69/mine/{H_train,H_test,CTRL}.txt`;
  caps 0, 0, 10; seeds 7070, 7070, 7071); 2-adic null: `… scripts/z70_loose_pell_recal2.py in.jsonl.gz out.jsonl.gz`
  (the superseded partial fix is `z70_loose_pell_recal.py`); analysis `python3 scripts/z70_loose_pell_an.py <files>`.

## 11. Review log
**Internal hostile review** (deep-mode reviewer subagent over commits 07c2edca6..8c422ab8a; verdict "changes
requested", 0 FATAL, 8 MAJOR, 7 MINOR; no provider/auth/quota error). The reviewer independently re-derived Theorem F
on ℍ (Mellin residues, Hurwitz phases, kernel signs, PV = ∫_{C₋} − πi Res), Lemma K's local factors (reran
`z70_loose_i6kappa.py`), the narrow LS argument, Lemma S (reran all six EMPTY pairs and the fixture), Lemma P5
(383 primes, 54 without trivial certificate), the I5 tallies (7 failures; 246/154 grammar split) and the Pell
aggregates. Fixes applied:
1. *LS scope* — Theorem LS restated as a statement about holomorphic cocycles with the radial bound; the blanket
   "not mock / not quantum / not harmonic" claims replaced by Corollary LS-M (cuspidal shadows, proved; extended after
   the review to holomorphic shadows modulo the standard regularised formula) and an explicit "not covered" list
   (exponential-growth forms, Zagier-type boundary objects, vector-valued systems without the bound);
   "any automorphic route must…" deleted from the FRONTIER text.
2. *Theorem F jump / §2.2* — the jump assertion withdrawn; the τ = tw path-rotation residue noted; §2.2 downgraded:
   only "S₁, S₂ ∉ M₁ (d = 1)" is PROVED, mock status not decided.
3. *K6a* — max relative error corrected to 8.9·10⁻¹⁵; the registered multiprecision grid was then run: d = 1 five
   points at 30 digits, d = 3 five points at 20 digits, all relative errors ≤ 2.1·10⁻¹⁹ (`i6_k6a_mp_d{1,3}.txt`).
4. *Lemma P5 consequence* — condition corrected to "p + 1 has no prime factor ≡ 3 (mod 4)" (counterexample p = 17,
   (p + 1)/2 = 9 = 3² + 0²); "infinitely many" removed.
5. *Pell 2-adic null* — full 2-adic recalibration (all v₂ ≥ 2), validated; numbers corrected; "behave exactly like"
   → "no difference detected".
6. *I9 strata* — partial strata disclosed, means recomputed on retained strata with stratum weighting, variance model
   stated.
7. *I9 diagnosis* — same-subset comparison added (nearest decoy z = +0.09 on the 1 233-pair subset); verdict
   rephrased as "consistent with size/selection confounding", "no excess detected".
8. *#10 scope* — verdict limited to the four implemented rules; exact-failure accounting corrected (20 distinct primes,
   14 recovered, 6 empty); heuristics labelled as such.
Minor: Lemma K's K-squeeze written out; deviation ledger §1.6 added; "407 candidate expressions"; Gaussian decoy cap
disclosed; section order and table bars fixed.
