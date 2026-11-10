# Z70_LOOSE — the untested ideation leftovers (I6, I5, IDEAA #10, MINE Pell-letter residues, I9)

**ES is OPEN.** This memo proves or computes nothing that settles ES. Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal review only. Scripts `scripts/z70_loose_*`, data `data/z70/loose/`.
Status: **checkpoint 1** (statements + pre-registered kill tests; no result yet).

Notation. (★) / R(n) as in `z52bbriefs/z58_lanes.md`. Fibre form: R(n) = Σ_{d ≥ 1} r_d(4dn + 1),
r_d(N) := #{A | N : A ≡ −1 (mod 4d)} (A = 4ad − 1, B = 4bd − 1, AB = 4dn + 1 ⟺ 4abd − a − b = n).
Words: T_n = {(x, y, z) ∈ ℕ³ : xyz − x − z = n}; certificate words C_n ⊂ T_n as in `Z69_TWIST.md` Remark C.
Type I (IDEAB R2/R4): 4abd = pe + 1, ce = a + b; K3 form p ≡ −f (mod 4ad), f | 4a²d + 1.

## 0. Mandatory falsifier table (checkpoint-1 version; restated at the end)
| item | F1 odd squares | F2 C-even / R₈ | F3 composites | F4 known zeros |
|---|---|---|---|---|
| I6 (fibre laws, level sum) | the fibre coefficient r_d(4dm² + 1) = 0 for 4 ∣ 4d (T1); a transformation law is a statement about the whole generating function and is coefficient-blind — it cannot by itself use primality; must be checked that the law holds identically at squares (it will) | n/a (the law is per fibre; C-even = d even fibres) | same as F1 | same as F1 |
| I5 (involution on T_p) | |T₉| = 11 odd, C₉ = ∅ ⟹ any involution family with certificate fixed points must fail at 9 (and at 105) | the swap-even sub-counts are even at primes; a map whose fixed points are C-even certificates would prove R₈-positivity — false at the 12 R₈ zeros; record which certificate type the fixed points have | 105: |T₁₀₅| = 11, C₁₀₅ = ∅ | none needed at primes (C_p ≠ ∅ at every tested prime) |
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
also composite d). Matched decoy for each rule: a uniformly random non-square d′ with (d′/p) = −1 and
|d′ − d| ≤ max(2, 0.1 d) (d′ ≠ d when possible).
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

## 2. I6 — the fibre laws exist (quantum-modular, PROVED + verified); the level sum has NO law (PROVED, scoped)

### 2.1 Theorem F (S-transformation of a partial divisor Lambert series; PROVED, classical ingredients)
Let M ≥ 1, 1 ≤ α, β ≤ M, a = α/M, b = β/M ∈ (0, 1], and assume a, b ≠ 1 (the case needed: d = 1 is
(M, α, β) = (4, 3, 3), d = 3 is (12, 11, 11); in general the d-fibre is Φ_d = L for (4d, 4d − 1, 4d − 1)). Put
  L(z) := Σ_{A ≡ α, B ≡ β (M); A, B ≥ 1} e(ABz),   L*_{u,v}(w) := Σ_{m,n ≥ 1} e(mu + nv + mnw)   (z, w ∈ ℍ),
w := −1/(M²z), S₁ := L*_{a,b} + L*_{−a,−b}, S₂ := L*_{a,−b} + L*_{−a,b}. Then for z ∈ ℍ
  **L(z) = (M²z)⁻¹ L*_{a,b}(w) + E(z) + Ψ(z)**,
  E(z) = (i/(2πM²z))·(−γ − log(−2πiM²z) − ψ(a) − ψ(b)) + (½ − a)(½ − b)       (ψ = digamma, principal log),
  Ψ(z) = (i/(2πM²z)) ∫_{C₋} [ S₁(tw)·t/(t − 1) − S₂(tw)·t/(t + 1) ] dt,
C₋ = a ray from 0 to ∞ passing **below** t = 1 with arg(tw) ∈ (0, π) along it. Ψ continues analytically to
z ∈ ℂ ∖ (−∞, 0] (rotate C₋; the pole t = 1 is never crossed, the pole t = −1 is reached only as z → (−∞, 0) from
below), and its jump across (−∞, 0) is ∓(1/(M²z))·S₂(1/(M²z)) (residue at t = −1) — a dual partial Lambert series.
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
7 points each for (4, 3, 3) [d = 1], (12, 11, 11) [d = 3], (4, 1, 1), (12, 7, 5), including Re z ≠ 0: max relative
error 2.9·10⁻¹⁵, absolute ≤ 4·10⁻¹⁶ (double precision), plus one 34-digit mpmath check for d = 1
(`scripts/z70_loose_i6mp.py` → `i6_law_mp34.txt`, z = (0.05 + 0.15i)·16/90: |L − law| = 1.8·10⁻³⁵, relative
6.7·10⁻³⁵; the small-τ region uses the asymptotic Mellin series to 60 terms). K6a passes. A first run with a too-coarse small-τ
series (switch at |τ| < 2·10⁻³) gave 10⁻⁸ errors for M = 12; the switch was lowered to 2·10⁻⁴ (convergence check in the
log of this memo's commit), errors then 10⁻¹⁷.

### 2.2 What the period is (K6b): not a mock period — relative to this law (PROVED in that scope)
Ψ is an Eichler-type integral: substituting τ = tw, ∫_{C₋}S(tw)·t/(t ∓ 1)dt = ∫_0^{i∞}S(τ)·τ/(w(τ ∓ w)) dτ (path
rotated in ℍ), i.e. the obstruction to modularity is a Cauchy integral **of the dual partial Lambert series S₁, S₂
themselves**, and the jump of Ψ across its cut is 2πi × (S₂ at the reflected point). For a mock modular form of
weight 1 the same jump would be (a constant times) the shadow g ∈ M₁. Here S₁, S₂ are not weight-1 modular forms
of any level: for d = 1, c(N) := Σ_{mn=N}(−i)^{m+n} equals τ(N) for N ≡ 3 (4) and −τ(N) for N ≡ 1 (4) (all m, n odd;
m + n ≡ 0 or 2 (mod 4) according as mn ≡ 3 or 1), so the coefficients of S₁ = 2 Re c are ±2τ(N) on odd N, whose
partial sums over N ≡ 3 (4) grow like x log x, while every f ∈ M₁(Γ₁(L)) (and its restriction to a residue class)
has Σ_{n≤x} a_f(n) = O(x) (Eisenstein part: Σ_{dm≤x} χ(m)ψ(d) with χψ odd, one character non-trivial; cusp part
o(x)). **So relative to the natural (discrete-Fourier) transformation matrix of Theorem F the fibre is a
vector-valued quantum-modular form of Bettin–Conrey type (period analytic on ℂ ∖ (−∞, 0]), not a mock modular
form.** (Scope: a mock structure with respect to a *different* choice of the q-series part is not excluded by this
argument; Assessment: unlikely — the τ(N) content is the weight-0 Eisenstein part, whose "holomorphic projection" is
exactly this kind of quantum object.) The fibre is the odd-character weight-1 theta part (modular) plus this
quantum part (`METAPLECTIC_ES.md` Thm K; consistent).
*Literature note.* The case M = 1 (Σ τ(n)qⁿ) is Bettin–Conrey, "Period functions and cotangent sums", Algebra &
Number Theory 7 (2013) — quoted from memory, not re-checked here; Theorem F is proved above independently and does
not rely on it.

### 2.3 Lemma K and Theorem LS — the level sum G has no transformation law of finite level (PROVED)
**Lemma K (singular coefficients of G).** For coprime a₀, c ≥ 1 and w → 0 in any sector |arg w − π/2| ≤ π/2 − δ,
  G(a₀/c + w) = κ(a₀/c)·log²(1/|w|)/(−2πi w·8) + o(log²(1/|w|)/|w|),   κ(a₀/c) = 1[c odd]·μ(c)/c².
(So G(iy) ~ log²(1/y)/(16πy).) *Proof.* Split (a, b, d) into classes mod c; on a class the phase e(a₀(4abd − a − b)/c)
is constant, and the count of class members with 4abd − a − b ≤ x is (x/(8c³))log²x + o(x log²x) (the TWIST I6(a)
argument per class: Σ_{a≡α, b≡β, ab≤X}(X/(c·ab) + O(1)) = X log²X/(2c³) + O(X log X), and the −a − b perturbation
moves 4abd by at most a factor 2, handled by the same K-squeeze). Partial summation: Σ u_n e^{−ns} = s∫U(t)e^{−st}dt,
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

**Theorem LS (no law for the level sum; PROVED).** There is no finite-index subgroup Γ ⊂ SL₂(ℤ), weight k ∈ ℝ and
multiplier v : Γ → S¹ such that for every γ = (∗ ∗; c d) ∈ Γ the period h_γ(z) := G(z) − v(γ)⁻¹(cz + d)^{−k}G(γz)
satisfies h_γ(r + iy) = o(y⁻¹log²(1/y)) (y → 0⁺) at every rational r ≠ −d/c. In particular G is not modular,
mock modular (periods are analytic on ℝ minus a point), quantum modular in Zagier's sense (continuous periods), nor the
holomorphic part of a harmonic Maass form, of any real weight on any finite-index subgroup; the same holds for any
finite-dimensional vector-valued system containing G whose representation has finite image (pass to its kernel).
*Proof.* Γ has finite index, so U^j = (1 0; j 1) ∈ Γ for some j ≥ 1 (pigeonhole on the cosets ΓUⁱ). Choose a prime ℓ ∤ j
and an integer r ≥ 1 with jr ≡ −1 (mod ℓ²). Then U^j(r) = r/(jr + 1) is in lowest terms with ℓ² | jr + 1, so
κ(U^j r) = 0, while κ(r) = κ(0) = 1 ≠ 0. At z = r + iy, U^j z − U^j r = iy/((jz + 1)(jr + 1)) lies in a fixed sector
with modulus ≍ y, so by Lemma K G(U^j z) = o(y⁻¹log²(1/y)) and |(jz + 1)^{−k}| is bounded; hence
h_{U^j}(r + iy) = G(r + iy) + o(·) ~ κ(0)·log²(1/y)/(16πy), contradicting the hypothesis (r ≠ −1/j since r > 0). ∎
Contrast: each fibre e(−z/4d)Φ_d(z/4d) has κ_d(a₀/c) ∝ (finite-level data) and satisfies Theorem F — the obstruction
is exactly the **infinite** union of levels 4d. The mechanism of the proof is the vanishing of the log² singularity
at every non-squarefree or even denominator (μ(c)/c²), i.e. the arithmetic of the *three* free divisor variables.

### 2.4 Squares (F1) and verdict for I6
* F1: r_d(4dm² + 1) = 0 (T1 at 4 | 4d) is a property of coefficients; Theorem F holds identically for every
  coefficient sequence of the form ζ(s, a)ζ(s, b) and is equivalent (by Mellin) to the Hurwitz functional equations — a
  Voronoi-type summation statement. It cannot distinguish 4dm² + 1 from 4dp + 1; it does not use primality anywhere.
  Lemma K's κ is likewise insensitive to n. (Assessment.)
* **Verdict I6: narrowed / dead on the level sum.** (S1) delivered: an explicit S-transformation with boundary
  terms E and period Ψ for the d = 1 and d = 3 fibres (PROVED, verified to 10⁻¹⁵). (S2) the period is the Cauchy
  integral of the non-modular dual partial Lambert series: a quantum-modular, not a mock, structure relative to that
  law. (S3) **the levels do not sum to a law** — Theorem LS rules out every finite-index (scalar or finite-image
  vector-valued) modular / mock / quantum-modular law for G, unconditionally. What survives: laws with infinitely
  many levels kept separate (METAPLECTIC hatch H-A, the B2 coordinate) — nothing new opened. Pointwise use of any of
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

### 3.1 Stage-1 result (`scripts/z70_loose_i5.py` → `data/z70/loose/i5_stage1.txt`): all seven candidates DEAD
|T₇₃| = 23 (|C₇₃| = 8), |T₄₀₉| = 39 (|C₄₀₉| = 8), |T₉| = |T₁₀₅| = 11 (C = ∅).
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
(the swap-free part T′_p is even). At every prime with (p + 1)/2 a sum of two squares (infinitely many; 73, 409, …) a
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

**Verdict I5 (narrowed):** the seven registered natural non-affine cross-slice maps and all 400 maps of the round-2 grammar fail stage 1 on T₇₃/T₄₀₉;
Lemma P5 explains why any such map must be arithmetic in p + 1. Not killed in general (a map certificate-fixed only at
primes is not excluded), but no candidate exists. F1: T₉, T₁₀₅ have C = ∅ and odd |T| — any passing family must fail
there; F2: no candidate survived to the C-even question.

## 5. (Pell letters: below)

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

**Exact (untruncated) failures of NP (CERTIFIED by Lemma S, `typeI_np_fail_exact.txt`):** of the 21 hard primes where
NP missed with A = 2000, a full scan finds points for 15 (with a up to 102 291 — the truncation matters) but the
**d = n_p slice is exactly empty** at 102 001 (d = 23; a (★)- and 𝔊*-zero), 3 361 (d = 11), 210 961 (23),
1 063 969 (17), 27 020 569 (37), 103 819 081 (13) (all noprime primes, all ≡ 1 (24), all in 𝔐).

**Kill tests.** K10a fires for every rule (best 97.4 % < 99.9 %). K10b fires (NP fails exactly at six hard primes).
K10c: the decoy comparison is uninformative for NP — the least non-residue has no admissible smaller decoy, so every
decoy is larger and the +107 measures size (expected slice count ≍ log²p / d); Q3 is far *below* its decoys
(restricting to primes ≡ 3 (4) hurts); CF's +12.6 has the same size asymmetry and is irrelevant at 78 % coverage.
**Verdict (#10): dead as stated** (four explicit rules; fixed-d Type I slices are p-independent covering families
over a, expected size ≍ (log p)²/d — any rule p ↦ d with d ≥ n_p ≥ 11 on 𝔐 inherits a positive failure rate). F1:
Type I at a square needs (d/m²) = −1 (Lemma T10), impossible — every rule fails at squares by the Jacobi step. F4:
reported in the table. The one surviving logical possibility is a rule that is *not* a single d (a growing menu of d) —
that is the ordinary Type I union, i.e. B2.

## 6. I9 — result (EVIDENCE; registered design; one deviation + one post-hoc size check, disclosed)
Run: `uv run --with sympy python scripts/z70_loose_i9.py` (seed 7070) → `data/z70/loose/i9_run.txt`, rows
`i9_rows.json`; post-hoc `scripts/z70_loose_i9b.py` → `i9b_twosided.txt`. Disjoint controls: 20 per hard prime,
same class mod 840, uniform in [p/2, 2p], no hard-list member, no reuse (hard primes with no admissible control:
5569, 9601 (𝔊*), 9601, 23041 (noprime), 1129, 2521, 3361 (U⁽⁸⁾) — dropped from Δ).

| hard set (𝔐-members with controls) | Q hard | Q controls | Δ (stratified) ± s.e. | z | 95 % CI |
|---|---|---|---|---|---|
| (★)-zeros (9) | 0.444 | 0.524 | −0.009 ± 0.158 | −0.06 | (−0.32, +0.30) |
| 𝔊*-zeros (18) | 0.450 | 0.569 | −0.121 ± 0.115 | −1.05 | (−0.35, +0.10) |
| noprime (143) | 0.559 | 0.590 | −0.022 ± 0.041 | −0.53 | (−0.101, +0.058) |
| U⁽⁸⁾-zeros (8) | 0.636 | 0.598 | +0.157 ± 0.179 | +0.88 | (−0.19, +0.51) |
| R₈-zeros (4, F2) | 0.500 | 0.637 | −0.138 ± 0.245 | −0.56 | (−0.62, +0.34) |

* **Registered effect bound:** on the noprime set the 95 % CI is (−0.101, +0.058): it reaches −0.101, just outside the
  registered (−0.10, 0.10) band, so the equivalence criterion is **narrowly not met** (it is met for +0.10, not for
  −0.10); no effect criterion (|z| ≥ 3) fires anywhere. Reading (EVIDENCE): no detected difference; an effect of
  size ≥ 0.10 in the direction "hard primes have Q *more* often" is excluded at 95 %; a deficit of ≈ 0.10 is not.
* **q-to-word construction (registered decoy, |q′ − q| ≤ 0.1 q):** Y(q) is tiny (≈ 0.02–0.03 on controls) and equal
  to the decoy rate (noprime controls 889 pairs: McNemar b = 23, c = 20, z = +0.46). The 10 % window is empty for
  most small q (772 of the noprime-control Q-primes had no decoy) — a design flaw of the registration.
  *Deviation (disclosed):* a window-free "nearest admissible prime" decoy gave a large apparent excess on controls
  (noprime controls: Y(q) = 0.158 vs Y(q′) = 0.094, z = +5.91). *Post-hoc size check:* that decoy is
  biased upward in size for small q (Y falls like ≈ (log q)/q); with a **two-sided** decoy (mean of the nearest
  admissible prime below and above q; mean log(decoy/q) ≈ −0.02) the excess disappears: noprime controls
  1 233 pairs, Y(q) = 0.068 vs 0.061, z = +0.84; all sets |z| ≤ 1.0. So the +5.9 was a size artifact.
* On hard primes the construction essentially never fires (noprime hard: Y(q) = 0.016 on 64 two-sided pairs).

**Verdict I9 (EVIDENCE):** with disjoint factor-two-matched controls the X-coordinate classifier shows no
difference (|z| ≤ 1.05 everywhere); a q | X with (840/q) = −1 builds (★) words exactly as often as a size-matched
non-residue prime not dividing X. K9 fires (no word-building information). Nothing here is a mechanism; the
remaining untested direction is any construction using q *together with* Y (e.g. f built from q and Y) — not
pursued.
