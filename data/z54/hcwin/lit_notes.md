# Literature notes (hcwin) — shifted primes, Shiu bounds, short intervals

Legend: VERIFIED = statement read in the primary source (PDF text); UNVERIFIED = secondary source / recall.

## Q1. Shiu / Nair–Tenenbaum bounds at shifted primes and linear forms

**Class M** (Shiu): f ≥ 0 multiplicative, f(p^k) ≤ A1^k, f(n) ≤ A2(ε) n^ε.
τ(n)^s, s∈[0,2], is in M: τ(p^k)^s=(k+1)^s ≤ (2^s)^k, so A1=2^s ≤ 4; f(p)=2^s. Yes, it applies.

### (a) Pollack, Glasgow Math. J. 62 (2020) 187–199, doi 10.1017/S0017089519000041 — VERIFIED
PDF: https://www.pollack-math.net/brunmultiplicative4.pdf
- **Theorem 1.1** (Brun's upper bound sieve for multiplicative functions). f ∈ M, 0<β<1/2, k ≥ 0 an integer.
  For each prime p ≤ x let E_p be a union of ν(p) ≤ k **nonzero** residue classes mod p; S = {n : n ∉ E_p ∀p≤x}.
  For x sufficiently large and x^β < y ≤ x:
  Σ_{x−y<n≤x, n∈S} f(n) ≪ (y/log x) exp( Σ_{p≤x} (f(p)−ν(p))/p ).
  Implied constant and "sufficiently large" depend **only on β, k, A1, A2(·)**.
  Remark (ii): to exclude n ≡ 0 (mod p) replace f by f·1_{gcd(n,P)=1} (still in M, same constants).
- **Corollary 1.2**: for f∈M, 0<β<1/2, x ≥ 3, y∈(x^β,x]:
  Σ_{x−y<q≤x} f(q−1) ≪_{f,β} (y/log x) exp(Σ_{p≤x}(f(p)−1)/p); twin-prime analogue with (log x)^2.
  (y = x case implicitly Barban–Levin, Dokl. Akad. Nauk.)
- **Uniformity in shift a (our derivation, not stated in paper):** for n = q+a, take E_p = {a mod p} for p ≤ √x, p∤a,
  E_p = ∅ otherwise, and f' = f·1_{(n,a)=1}. ν ≤ 1, so constant depends only on β,A1,A2 — **uniform in a**
  (any 1 ≤ |a| ≤ x/2 say). Result: Σ_{x−y<q+a≤x} f(q+a) ≪ (y/log x) exp(Σ_{p≤x,p∤a}(f(p)−1)/p) ≪ (a/φ(a))·(y/log x)exp(Σ_{p≤x}(f(p)−1)/p) if f(p) ≥ 0.
  Caveat: for forms a·q+1, Thm 1.1 cannot impose n ≡ 1 (mod a), so it loses a factor ≈ a. Use Henriot Thm 7 below instead.
- Consequence (paper, p.3): Σ_{q≤x, q−2 prime} t^{ω(q−1)} ≪_{t0} x(log x)^{t−3}.

### (b) Henriot, "Nair–Tenenbaum bounds uniform with respect to the discriminant", Math. Proc. Camb. Phil. Soc. 152 (2012) 405–424 — VERIFIED (arXiv v1 text)
arXiv: https://arxiv.org/abs/1102.1643 . Erratum: Math. Proc. Camb. Phil. Soc. 157(2) (2014) — https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/nairtenenbaum-uniform-with-respect-to-the-discriminanterratum/B0BD208D979495FE06B8192209E710EA
(erratum text NOT seen — its abstract says "all the results claimed may be recovered"; whether constants/Δ_D change: UNVERIFIED. For linear Q, D*=1 so Δ_D*=1 and the discriminant issue is moot.)
- **Theorem 4** (arXiv numbering): f∈M, Q∈Z[X] irreducible, degree g, disc D, 0<α,δ<1. Uniformly in x ≥ c0‖Q‖^δ, x^α < y ≤ x:
  Σ_{x<n≤x+y} f(|Q(n)|) ≪ Δ_D y ∏_{p≤x}(1−ρ(p)/p) exp(Σ_{g<p≤x, p∤D} f(p)ρ(p)/p); constants depend on α,δ,A,B (and g) only. ‖Q‖ = sum of |coefficients|.
- **Theorem 7** (primes): under the hypotheses of Thm 5 (Q primitive, F∈M_k(A,B,ε), ε < α/(50g(g+1/δ))), with Q(0) ≠ 0, uniformly in x ≥ c0‖Q‖^δ, x^α ≤ y ≤ x:
  Σ_{x<p≤x+y} F(|Q1(p)|,…,|Qk(p)|) ≪ (y/log x)·(Q(0)/φ(Q(0)))·Δ_D*·∏_{g<p≤x}(1−ρ(p)/p)·Σ_{n1…nr≤x} F̃(n)ρ̂_R(n)/[n1κ(n1),…].
  Constants depend at most on g, α, δ, A, B. (Proof deferred to Nair–Tenenbaum Thm 3.)
- **Application (our derivation):** Q(X)=aX+1: primitive, g=1, D*=1, Q(0)=1, ρ(p)=1_{p∤a}, ‖Q‖=a+1. Gives, uniformly for a ≤ (log x)^C (indeed a ≤ (x/c0)^{1/δ}):
  Σ_{x<p≤x+y} f(ap+1) ≪ (y/log x) exp(Σ_{p≤x, p∤a}(f(p)−1)/p).  Q(X)=X+a: same with an extra factor a/φ(a).
  For f=τ^s: Σ_{p≤x} τ(ap+1)^s ≪ x(log x)^{2^s−2}·(correction ∏_{p|a}(1+O(1/p))), uniform in a ≤ (log x)^C.
- Nair–Tenenbaum original (Acta Math. 180 (1998) 119–144): constant depends on D (per Henriot's Thm 1 restatement) — VERIFIED as quoted by Henriot; for linear forms D=1, so NT already uniform in coefficients (subject to x ≥ c0‖Q‖^δ). Prime version = NT Theorem 3 — UNVERIFIED (not opened).

### (c) Fan, arXiv 2508.06005 (v3, Dec 2025) — VERIFIED
Restates Pollack Thm 1.1 as "Theorem A" with class f(n) ≤ A1^{Ω(n)}, E_p ⊆ (Z/pZ)^×, y ∈ [x^α, x], constant depends on A1, A2, v, α.

## Q2. Titchmarsh divisor problem uniform in shift

- **Assing–Blomer–Li, "Uniform Titchmarsh divisor problems"**, arXiv 2005.13915 (Adv. Math. 2022, https://www.sciencedirect.com/science/article/pii/S0001870821005156) — VERIFIED (arXiv v1).
  **Theorem 1.1**: σ∈{±1}, f ∈ Z\{0}, max(−f,0) ≤ Y < X, X+f ≍ X (if σ=−1, f > X). Then
  Σ_{Y<n≤X} Λ(n)τ(σn+f) = c0(f)[(X+σf)log(σX+f) − (Y+σf)log(σY+f) + (2γ−1)(X−Y)] + 2c0'(f)(X−Y) + O_A(X(log X)^{−A}),
  with c_s(a) = ∏_{p|a}(1−p^{−s−1}) ∏_{p∤a}(1 + 1/((p−1)p^{s+1})). **Completely uniform in f** (constant depends only on A).
  ⇒ Σ_{p≤x} τ(p+a) = c0(a)x(1+o(1)) uniformly in 1≤|a|≤x/2 (say). NOTE c0(a) ≍ φ(a)/a, so the uniform lower bound is
  ≫ (φ(a)/a)x ≫ x/logloglog x for a ≤ (log x)^C — "≫ x uniformly" is FALSE in general (a = primorial).
- ABL intro: Titchmarsh's GRH formula x·(φ(a)/a)∏_{p∤a}(1+1/(p(p−1))) + O_a(x loglog x/log x); unconditional via BV: Rodriquez, Boll. UMI (3) 20 (1965) 358–366 and Halberstam, PAMS 18 (1967) 187–188; "only the range a ≪ x^{1/2} seems to have appeared in print [Rodriquez]". Fouvry, Crelle 357 (1985) 51–76 and BFI Acta Math 156 (1986) give O_{a,A}(x(log x)^{−A}) — dependence on a NOT uniform (O_a). Friedlander–Granville: uniform for a ≪ x^{1/4−ε} with ω(a) ≪ loglog x. — VERIFIED (as stated in ABL); originals UNVERIFIED.
- Simple self-contained alternative: lower bound Σ_{p≤x}τ(p+a) ≥ Σ_{d≤√x/(log x)^B, (d,a)=1} π(x;d,−a) and BV (max over residues ⇒ uniform in a) give ≫ (φ(a)/a)x. (standard; our derivation)

## Q3. Very short intervals [N, N+H], H = (log N)^A

(b) Pointwise asymptotic Σ_{N<n≤N+H} τ(n) ~ H log N needs Δ(N+H)−Δ(N) = o(H log N):
- Huxley, "Exponential sums and lattice points III", Proc. LMS 87 (2003) 591–609: Δ(x) ≪ x^{131/416}(log x)^{26947/8320} — VERIFIED as quoted in Ivić–Zhai arXiv 1209.0872 eq. (1.1) and Li–Yang.
- **Li–Yang**, arXiv 2308.14859 "An improvement on Gauss's circle problem and Dirichlet's divisor problem", **Theorem 1.2**: Δ(X) ≪_ε X^{θ*+ε}, θ* = 0.3144831759741… — VERIFIED (current record; preprint, publication status not checked).
- Bourgain–Watt 517/1648 (arXiv 1709.04340): **WITHDRAWN status** — arXiv comment: gap in Props 2,3, "Theorems 1, 2 and 3 lose their status as theorems". VERIFIED. Do not cite 517/1648.
- Ivić–Zhai (arXiv 1209.0872) Thm 1: Δ(x+U)−Δ(x) ≪ x^{1/4+ε}U^{1/4} (U ≪ x^{3/5}); x^{2/9+ε}U^{1/3} (U ≪ x^{2/3}) — VERIFIED; worse than θ* for asymptotics.
  ⇒ best pointwise: H ≥ N^{θ*+ε}, θ* ≈ 0.31448.
(c) Jutila, "On the divisor problem for short intervals", Ann. Univ. Turku. Ser. A I 186 (1984) 23–30 — statement VERIFIED via Ivić–Zhai Theorem B (original not opened):
  For T ≥ 2, 1 ≤ U ≪ T^{1/2} ≪ H ≤ T: ∫_T^{T+H}(Δ(x+U)−Δ(x))² dx = (1/4π²)Σ_{n≤T/(2U)} d(n)²n^{−3/2}∫_T^{T+H} x^{1/2}|exp(2πiU√(n/x))−1|² dx + O_ε(T^{1+ε}+HU^{1/2}T^ε).
  Consequence (Ivić–Zhai (2.3), with Preissmann's T log⁴T): for 1 ≤ U ≤ T^{1/2}/2 ≪ H ≤ T,
  ∫_T^{T+H}(Δ(x+U)−Δ(x))² dx ≪ HU log³(√T/U) + T log⁴ T. Jutila's conjecture: Δ(x+U)−Δ(x) ≪ x^ε√U for x^ε ≤ U ≤ x^{1/2−ε}.
  ⇒ (our derivation) Σ_{x<n≤x+U}τ(n) ~ U log x for almost all x∈[T,2T] once U/log T → ∞.
(a) Pointwise for polylog H: only trivial results known (our assessment, UNVERIFIED as "open" — no paper found):
  - Σ_{N<n≤N+H}τ(n) ≥ Σ_{d≤H}⌊H/d⌋ ≫ H log H (trivial); ≫ H log N pointwise: no result found.
  - ω(n) ≥ (1+o(1)) log H/loglog H for some n in the interval (CRT, n ≡ 0 mod primorial ≤ H) — i.e. ≍ loglog N/logloglog N; ω ≥ c loglog N or τ ≥ (log N)^c pointwise: no result found.
  - Related MO 275191 (min ω on [x, x+log^k x]): Tao comment — no known technique (even under ABC) rules out conspiracies of medium primes; pointwise polylog problems considered out of reach. VERIFIED (comment read).
  - "Every [N,N+(log N)^A] contains n with two prime factors > (log N)^A": no reference found; believed open (UNVERIFIED). Related Grimm-type results (Ramachandra–Shorey–Tijdeman) go the other way.
(d) Erdős–Kac/Turán–Kubilius in short intervals: Matomäki–Radziwiłł (Annals 183 (2016)) — almost all intervals, h→∞ (UNVERIFIED here). Turán–Kubilius pointwise in an interval of length H controls only ω restricted to primes ≤ H^{1/2}, i.e. ~ loglog H = logloglog N + O(1) prime factors (our derivation). No pointwise polylog Erdős–Kac known.

## Q4. ω on shifted primes: large deviations

- **Ford, "A Hardy–Ramanujan type inequality for shifted primes and sifted sets", Lith. Math. J. 61(3) (2021) 323–329** — VERIFIED (author PDF https://www.ford126.web.illinois.edu/wwwpapers/HR_shift.pdf).
  **Corollary 1**: a ≠ 0, s=2 if a odd, s=1 if a even. Uniformly for all k ∈ N, x ≥ 2|a| and all a ≠ 0:
  #{−a<p≤x : ω((p+a)/s) = k} ≪ (|a|/φ(|a|)) π(x) (loglog x + O(1))^{k−1}/((k−1)! log x).
  (Full uniformity in k AND a; corrects Timofeev's error for odd a.) Corollary 3: same with p+a restricted to Q(E).
  Lower bound: "not known for any k" (parity problem). Best: **Timofeev [Math. Notes 57 (1995) 522–535] Theorem 3** (case a=2):
  #{p≤x : ω(p+2) ∈ {k,k+1}} ≫ π(x)(loglog x+O(1))^{k−1}/((k−1)! log x) uniformly for 1 ≤ k ≪ loglog x (k=1: Chen). — VERIFIED as quoted by Ford; Timofeev original UNVERIFIED.
- **Fan, arXiv 2508.06005, Theorem 1.1** — VERIFIED: f∈M(A1,A2), sifted set S ⊆ [1,x] (≤ v nonzero classes E_p per p), E ⊆ P with min E ≥ p0, g∈{ω,Ω}, β = α1 (g=ω, any α1>0) or α2∈(0,p0) (g=Ω):
  Σ_{n∈S, g(n,E)=k} f(n) ≪ x(M_f(x,E)+O(1))^k e^{M_f(x,E^c)−M_ν(x)}/(k! log x) for 0 ≤ k ≤ βM_f(x,E); for E=P: x(M_f(x)+O(1))^{k−1}e^{−M_ν(x)}/((k−1)! log x), 1 ≤ k ≤ βM_f(x).
  Constants depend on A1,A2,p0 (Ω only),v,β — uniform in the shift. So k ≤ (2+ε)loglog x is covered for ω (any β); for Ω only k ≤ (2−ε)loglog x (β<p0=2).
  Corollary 1.2: Gaussian-tail upper bound for |g(n,E)−M_f| ≥ λ√M_f under a BV-type hypothesis (3). Implies Timofeev Thms 1,2.
- Rankin moment: Σ_{q≤x} z^{ω(q+a)} ≪_Z (x/log x)(log x)^{z−1}·∏_{p|a}(1+O(1/p)) for 0 ≤ z ≤ Z, uniform in a — from Pollack Thm 1.1 with f = z^ω (our derivation; Pollack states the twin-prime case p.3). Matching lower bounds for z>1 / k ≥ (1+ε)loglog x: none found (UNVERIFIED that none exist; Ford says lower bound unknown for any single k).
- Erdős–Kac for ω(p−1): Halberstam, J. London Math. Soc. 31 (1956) 14–27 (cited by Fan) — UNVERIFIED (not opened).
