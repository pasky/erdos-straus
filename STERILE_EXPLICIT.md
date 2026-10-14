# STERILE_EXPLICIT — the function-field class-divisor machinery over ℤ: explicit sterile Mordell points (O219, spark relay Y9)

Status: in progress (O219). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on DEPTH_ASPECT.md §3 ((J)26 Thm 3.1, reviews R178/R187), FF_STERILE_PUSH.md (O216, Lemmas 1.1–1.6, 2.1),
POINTWISE_MORDELL17*.md (= M17, M17B, M17C, M17D), STERILE_STEER.md. Scripts `scripts/se_*`.

## 0. Iteration log

* (I1) Dictionary. O216's Case B tuples (m', g', w, C, v) with m'wC = T^s + v, w + C = g'v are *literally* the ℤ
  P-data of M17 (N-points of Σ^II_N, N = r^K): 4d·a·b = N + e, a + b = c·e. So (m', g', w, C, v) ↔ (4d, c, a, b, e),
  E = L'w − 1 ↔ f = 4acd − 1, Lemma 1.1(i) Ev = T^s + m'w² ↔ ef = N + 4a²d (ET (2.19)), and the FF degree identity
  y + t = max(a, b) ↔ the size relation ce = a + b ∈ (b, 2b]. Every FF route has a ℤ twin (§1, Table 1.2).
* (I2) Continuum steering (`scripts/se_rate.py`, EVIDENCE/Assessment). With sizes a = N^α, c = N^γ, d = N^δ, e = N^ε
  (α + γ + δ + ε = 1 up to O(1/log N), 2α + δ ≤ 1), and a divisor loss τ(m) ≤ C(η)m^η charged where no class
  bound applies, the best route exponent θ*(η) = max_pattern min_route is 0.400 (η = 0), 0.417 (0.1), 0.467 (0.2),
  0.500 (0.25), 0.533 (0.3). ET's four-regime argument tolerates only η ≈ 1/18 (its loss is η·(1 + 4/5) on top of 2/5),
  which is why (J)26's r₀ is a tower. The transplant tolerates η < 1/4. The binding corner is
  a ≈ b ≈ d ≈ N^{1/3}, e ≈ N^{1/6}: balanced triple factorisations of (N + e)/4 with a ≡ −b (mod e), exactly at the
  Coppersmith threshold for the class route (modulus e vs divisor b ≈ m^{1/2} of m = (N+e)/(4a), threshold m^{1/4}).
* (I3) Steering by the barrier: the hypothesis that binds in (I2) is "a class-divisor bound exists only above the
  Coppersmith threshold, below it one pays τ". Violate it: split the size window of the divisor into short
  subintervals. Coppersmith's lattice works in each subinterval once modulus × (number of pieces) exceeds the threshold,
  so the count of divisors of size n^β in a class mod n^ρ is ≤ n^{max(0, β(1−β)−ρ)+o(1)} (Lemma 1.3 below, elementary;
  "Coppersmith interpolation"). With it (`scripts/se_rate2.py`, `se_rate2_subsets.py`; grid EVIDENCE):
  **θ* = 2/5 exactly — ET's exponent — using no divisor bound at all except one: τ₃(N + e) ≤ C₃(η)N^η for single
  integers N + e, tolerated up to η = 0.3** (θ* = 0.400, 0.417, 0.450, 0.500 at η = 0.3, 0.35, 0.4, 0.5).
  Five class routes + the τ₃ route suffice (dropping any one raises θ* to ≥ 0.425). The only τ-dependent corner is
  e = N^{o(1)}, a ≈ b ≈ d ≈ N^{1/3}: literally the balanced triple factorisations of the integers (N + e)/4.

## 1. P-data over ℤ: identities, sizes, and the class-divisor lemma

Notation (M17 §2, DEPTH_ASPECT §3). r an odd prime, N = r^K (K odd). A *P-datum* is a positive integer tuple (a, b, c, d, e)
with **4abd = N + e, a + b = ce**, r ∤ cd, r ∤ ab (in-cell data are primitive: M17 §6 and Lemma 5.1, r-free; R187),
counted with a ≤ b; D_P(N) is their number. f := 4acd − 1, f' := 4bcd − 1. Each datum and its reflection give the P-boxes
−f, −f' (mod r^{(K+1)/2}) (M17 Lemma 2.3). The FF twin is O216's Case B tuple with (m', g', w, C, v) ↔ (4d, c, a, b, e).

**Lemma 1.1 (identities; PROVED, elementary).** For every P-datum:
(i) ef = N + 4a²d, ef' = N + 4b²d; (ii) bf = Nc + a, af' = Nc + b; (iii) ff' = 4c²dN + 1;
(iv) gcd(e, abd) = 1 and e is odd.
*Proof.* (i) e(4acd − 1) = 4ad(a + b) − e = 4a²d + 4abd − e = 4a²d + N. (ii) b(4acd − 1) = c(N + e) − b = cN + ce − b = cN + a.
(iii) (4acd − 1)(4bcd − 1) = 4c²d·4abd − 4cd(a + b) + 1 = 4c²d(N + e) − 4c²de + 1. (iv) A prime p | e with p | abd divides
4abd − e = N = r^K, so p = r, contradicting r ∤ abd; e = 4abd − N is odd. ∎
(i) is the ℤ twin of O216 Lemma 1.1(i) (Ev = T^s + m'w²); (iii) is O173/DEPTH_ASPECT (R2).

**Lemma 1.2 (sizes; PROVED).** If a ∈ [A, 2A), c ∈ [C, 2C), d ∈ [D, 2D) and a ≤ b, then
N/(16AD) < b ≤ N/(2AD), N/(32ACD) < e ≤ N/(ACD), 4ACD − 1 ≤ f < 32ACD, 4a²d ≤ 2N, and 2A²D ≤ N.
*Proof.* 4abd = N + e > N gives b > N/(4ad) > N/(16AD). e ≤ a + b ≤ 2b gives b(4ad − 2) ≤ N, and 4ad − 2 ≥ 2ad, so
b ≤ N/(2ad) ≤ N/(2AD). Then e = (a + b)/c ∈ [b/c, 2b/c]. 4a²d ≤ 4abd = N + e ≤ N + 2b ≤ 2N (b ≤ N/2). A ≤ a ≤ b ≤ N/(2AD). ∎

**Lemma 1.3 (divisors of bounded size in a residue class — Coppersmith/Howgrave-Graham by Minkowski; PROVED, elementary).**
Let n ≥ 1, s ≥ 1, σ ∈ ℤ with gcd(σ, s) = 1, and 1 ≤ D₀ ≤ D₁ real. Let m ≥ 1, k ≥ 0, w = m + k and
X := (D₁ − D₀)/(2s) + 1/2. If
  w^w · n^{m(m+1)/2} · X^{w(w−1)/2} < D₀^{mw},                                                     (Cop)
then n has at most w − 1 divisors E with D₀ ≤ E ≤ D₁ and E ≡ σ (mod s).
*Proof.* Every such E is prime to s, so E | n₁ := ∏_{p∤s} p^{v_p(n)}. Let σ₀ ∈ [0, s) be σ mod s and x̂ an integer nearest to
the midpoint of [(D₀ − σ₀)/s, (D₁ − σ₀)/s]; every E in question is E = σ₀ + s(x̂ + y) with y ∈ ℤ, |y| ≤ X. Take t ∈ ℤ with
st ≡ 1 (mod n₁) and F(y) := y + x̂ + σ₀t. Then sF(y) ≡ E (mod n₁), so E | sF(y), and E | F(y) as gcd(E, s) = 1. Hence E^m
divides g(y) for every g in the ℤ-span 𝓛 of g_i = n₁^{m−i}F^i (0 ≤ i < m) and h_j = y^jF^m (0 ≤ j < k). These have degrees
0, …, w − 1 and leading coefficients n₁^m, …, n₁, 1, …, 1, so the vectors (g_l X^l)_{l<w} of g ∈ 𝓛 form a lattice of
determinant n₁^{m(m+1)/2}X^{w(w−1)/2} in ℝ^w. By Minkowski's convex body theorem (cube [−λ, λ]^w, λ = det^{1/w}) some g ≠ 0
in 𝓛 has |g_l|X^l ≤ det^{1/w} for all l, so |g(y)| ≤ w·det^{1/w} < D₀^m ≤ E^m for |y| ≤ X, by (Cop) and n₁ ≤ n. Since
E^m | g(y), g(y) = 0. g has at most w − 1 roots and E ↦ y is injective. ∎
(m = 1, k = 1 gives: at most one such divisor if 4nX < D₀². The ℤ twin of O216 Lemma 1.5; over ℤ Minkowski replaces
LLL, as we count and do not search.)

**Corollary 1.4 (Coppersmith interpolation; PROVED).** Under the hypotheses of Lemma 1.3 except (Cop), for every integer
J ≥ 1 the number of such divisors is at most J·(w − 1) as soon as (Cop) holds with X replaced by X_J := (D₁ − D₀)/(2sJ) + 1/2.
Asymptotically (n → ∞, D₀ = n^β, s = n^ρ, D₁ = 2D₀) this gives **≤ n^{max(0, β(1−β) − ρ) + o(1)}**: a class-divisor bound
with no divisor-function loss that interpolates between the trivial bound (window/s + 1) and the Coppersmith range
ρ > β(1 − β) (O216 Lemma 1.5's ℤ form; for ρ ≤ 1/4 it is new to the campaign, and it is what removes the binding corner
of (I2)).
*Proof.* Cut [D₀, D₁] into J intervals of length (D₁ − D₀)/J and apply Lemma 1.3 to each, with the common lower bound D₀.
Asymptotics: with w = τm, (Cop) reads (1/2 + o(1)) + τ²(β − ρ − j)/2 < τβ, j = log J/log n; optimising τ = β/(β − ρ − j)
gives the condition ρ + j > β(1 − β). ∎
