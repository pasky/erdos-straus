# EXCEPTIONAL_WEIGHTS — per-frequency weights below 1 (task O81)

Status: **work in progress (O81), not reviewed.** Labels follow `DISCOVERIES.md`.
PROVED means proved in this file, internal checks only. No θ > 3/4 is claimed.

Notation as in `EXCEPTIONAL_NONCRT.md` (NC), `EXCEPTIONAL_INTERFREQ.md` (IF),
`EXCEPTIONAL_KARY2.md`/`KARY3.md` (K2/K3). 𝒜 = 𝒜(𝔊) ⊂ ℤ is the avoider set of a
finite family 𝔊 of residue classes, periodic with period Q. A *majorant* is a
Q-periodic ν: ℤ → ℝ with ν ≥ 0 on ℤ and ν ≥ 1 on 𝒜 (on all of ℤ; for finite
combinations of classes the period is a multiple of Q, and we take Q to be a
common period). Fourier coefficients `ν̂(θ) = E_{n mod Q} ν(n) e(−nθ)`,
θ ∈ (1/Q)ℤ/ℤ, so `ν(n) = Σ_θ ν̂(θ) e(nθ)` and `ν̂(0) = Eν`.

*Families (R81 repair, applied by reviewer).* `M(N) = M_𝔊(N)` depends on the finite
family 𝔊 = 𝔊_N, and it **decreases** when 𝔊 is enlarged. Every statement below is
per family unless stated otherwise. Three families occur:
* **𝔊_X**, the family of the 3/4 note (`paper/es-threequarter-note.tex`, Thm
  "critical-window assembly"): the selector classes and the multiplier classes mod kℓ
  (k ≤ K) of `ν_X = S_y Q_r(H_X)`, with `X = exp(α(log N)^{1/4})`. Its avoider set is
  `𝒜_X = {n : S_y(n) = 1, H_X(n) = 0}`. Prop 5.1(a) is about 𝔊_X only.
* **𝔊_ℛ**, the Q₀ = 1 toy family of prime slices `F_ℓ = ℛ(ℓ)` (ℓ ≡ 3 (4) prime, up to
  a bound). It is used in (2.2), Prop 5.1(b),(d), §5.1, and (restricted to ℓ ≥ ℓ₀) in
  Thm 3.3. No upper bound of the form `Ne^{−c(log N)^{3/4}}` is claimed for it. Its mass
  over primes is a smaller power of log than over all moduli, so its natural sieve-limit
  exponent is below 3/4.
* **𝔉_A**, the class of all finite families of ℛ(M)-, Case-A and selector classes with
  moduli ≤ N^A (A fixed). This is the class relevant for "the door": a method may use
  any 𝔊 ∈ 𝔉_A.

For a family 𝔊 and for a class 𝔉 put

    (W_𝔊)  M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}   (N ≥ N₀),
    (W_𝔉)  min_{𝔊 ∈ 𝔉_N} M_𝔊(N) ≥ N e^{−C(log N)^{3/4}}   (N ≥ N₀, C independent of 𝔊).

"(W)" below means (W_{𝔉_A}) when we speak of the door. Thm 2.1, Cor 2.2 and Lemma 1.1
are per-family statements (any finite 𝔊).

## 0. Summary

| item | statement | label |
|---|---|---|
| Lemma 1.1 | every per-frequency bound with weights `w ≥ |W_N|` or `w ≥ |S_N|` is translation invariant, hence ≥ `M(N) = max_t #(𝒜∩(t,t+N])` | PROVED (trivial) |
| Lemma 1.2 | LP duality: best per-frequency bound = `max ⟨g,1_𝒜⟩` over `g ≥ 0`, `|Qĝ| ≤ w` | PROVED |
| Thm 2.1, Cor 2.2 | band-limited (Selberg-majorant) windows, **general majorants**: for every finite family 𝔊, the best per-frequency bound **for the window Φ_K** lies in `[M_𝔊(N), 12(K+1)M_𝔊(N)]`. So, per family, this door is capped at 3/4 **iff** (W_𝔊); for a method class using families in 𝔉_A, iff (W_{𝔉_A}) (R81 repair, applied by reviewer) | PROVED |
| Thm 3.3 | sharp weight `|S_N|` (and any w with `w(0) = N`, `w ≥ c₀|sin πNθ|` off 0), **hit-pattern majorants**, Q₀ = 1, prime slices with `|F_ℓ| ≤ ℓ^γ` (γ < 1/3), boundedly many bad primes, all `p_ℓ ≤ 1/4`, and the uniform mass hypothesis (M) (ℛ(ℓ)-slices **with ℓ ≥ ℓ₀ only**; small primes would need Q₀ > 1, not claimed — R81 repair, applied by reviewer): saving `≤ C(log N)^{3/4}`, without (H_eq) | PROVED |
| Lemmas 4.1–4.2 | smooth windows, hit-pattern majorants: (H_eq) ⇐ a characteristic-function bound (4.1); true for one prime ≥ 2|F|N/c (loss √|F|); several primes open | PROVED / (H_eq) CONJECTURE |
| Prop 5.1 | `#(𝒜_X∩[1,N]) ≤ M_{𝔊_X}(N) ≤ Ne^{−c(log N)^{3/4}}` (only for the 3/4-note family 𝔊_X; R81 repair, applied by reviewer); random-translate and greedy lower bounds (prime slices) are far below the 3/4 scale | PROVED |
| (W) | is (W_{𝔉_A}) true, i.e. `min_{𝔊∈𝔉_A} M_𝔊(N) ≥ Ne^{−C(log N)^{3/4}}`? (per-family version (W_𝔊); R81 repair, applied by reviewer) | OPEN QUESTION |
| §6 | sharp weights, general majorants: only `≥ M(N)` known (a window-averaged w ≥ 1 certificate gives nothing more, Rem 6.1) | PROVED / open |
| §5.1 | toy translate sieve (ℛ(ℓ) prime slices, N = 300, 1000): optimised translates reach savings 2.4, 3.0 (large-sieve upper bound 0.7, 0.9; random translates 12.5, 15.9): near the sieve scale, consistent with (W) | EVIDENCE |

**Verdict.** Weights below 1 split into two very different doors.
* *Hit-pattern majorants* (NC §2.5's class, Q₀ = 1 prime slices under the mass
  hypothesis (M)): the sharp weight is closed without (H_eq) (Thm 3.3): a weight that is small only near `‖Nθ‖ = 0`
  cannot hurt, because the product spectral measure of the forced classes
  cannot concentrate there (one-prime anti-concentration). Smooth windows still
  need (H_eq), reduced to a characteristic-function bound (Lemma 4.1).
* *General majorants with smooth (band-limited) windows*: the door is
  **exactly** the shift-uniform count M(N), up to a factor 12(K+1)
  (Thm 2.1). No arithmetic-free argument can cap it. A cap is equivalent to
  the arithmetic statement (W), a lower bound for the number of avoiders in
  the best window anywhere in ℤ. An escape (weights < 1 beating 3/4) exists
  iff M(N) is smaller than the sieve-limit scale. In that case the escaping
  majorant is the LP optimum, which is essentially as hard to evaluate as the
  count itself.
* Every per-frequency method is translation invariant (Lemma 1.1). So if the
  3/4 barrier can be broken at all by such methods, it is broken for every
  window simultaneously. A proof that M(N) is large would show that any
  improvement must use where the window sits, not only its length.

No θ > 3/4 is obtained or claimed.

## 1. Per-frequency bounds are translation invariant

A **per-frequency bound** with weight `w: (1/Q)ℤ/ℤ → [0,∞)` is

    R_w(ν) = Σ_θ w(θ) |ν̂(θ)|            (the θ = 0 term is w(0)·Eν).        (1.1)

It is used through an identity `Σ_n Ψ(n) ν(n) = Σ_θ ν̂(θ) Ψ̌(θ)` for a test
function Ψ ≥ 1_{[1,N]} on ℤ, with `Ψ̌(θ) = Σ_{n∈ℤ} Ψ(n) e(nθ)` and `w ≥ |Ψ̌|`.
The two cases of NC §2.5:

* *sharp:* `Ψ = 1_{[1,N]}`, `Ψ̌ = S_N(θ) = Σ_{n≤N} e(nθ)`, `|S_N(θ)| = |sin πNθ / sin πθ|`;
* *smooth window:* `Ψ(n) = Φ(n/N)`, Φ ≥ 0 integrable on ℝ, Φ ≥ 1 on [1/N, 1],
  `Σ_n Φ(n/N) < ∞`; `Ψ̌ = W_N(θ) = Σ_n Φ(n/N) e(nθ)`.

The weights `|S_N|` and `|W_N|` are < 1 on large sets of frequencies
(`|W_N(θ)| = O_A(N(N‖θ‖)^{−A})` for smooth Φ). NC Thm 2.3 needs `w ≥ 1` at
every θ ≠ 0 and does not apply.

**Lemma 1.1 (translation invariance; PROVED, trivial).** Let `w ≥ |Ψ̌|` with Ψ
as above. For every majorant ν and every t ∈ ℤ,

    R_w(ν) ≥ Σ_{n=t+1}^{t+N} ν(n) ≥ #(𝒜 ∩ (t, t+N]).

Hence `R_w(ν) ≥ M(N)` for every majorant ν, where

    M(N) = M_𝒜(N) := max_{t∈ℤ} #(𝒜 ∩ (t, t+N])                               (1.2)

is the **shift-uniform avoider count**.

*Proof.* `ν_t(n) = ν(n+t)` is a majorant of 𝒜 − t, and `|ν̂_t(θ)| = |ν̂(θ)|`, so
`R_w(ν) = R_w(ν_t) ≥ |Σ_θ ν̂_t(θ)Ψ̌(θ)| = Σ_n Ψ(n)ν(n+t) ≥ Σ_{n≤N} ν(n+t)`, using
Ψ ≥ 1_{[1,N]} and ν ≥ 0 on ℤ. Finally ν ≥ 1 on 𝒜. ∎

So no per-frequency bound — any weights, any coefficients, any majorant — can
beat the maximal number of avoiders in a window of length N anywhere in ℤ.
The same holds for every bound of the form `N·Eν + Σ_i|a_i|` (each class meets
any window in ≤ N/d + 1 points), so M(N) is a common floor of all
shift-uniform methods. `M(N) ≥ #(𝒜∩[1,N])`, and M(N) is in general much larger
than the true count on [1,N] (it is a maximum over all of ℤ, i.e. over all CRT
translates of the family).

**Lemma 1.2 (convex duality for per-frequency bounds; PROVED).** For every weight
`w ≥ 0` with `w(−θ) = w(θ)` and `w(0) > 0`,

    min { R_w(ν) : ν majorant of 𝒜 }
      = max { Σ_{n mod Q} g(n) 1_𝒜(n) : g: ℤ/Q → [0,∞), |Q ĝ(θ)| ≤ w(θ) ∀θ }.   (1.3)

*Proof.* Let `G = {g real: |Qĝ(θ)| ≤ w(θ) ∀θ}`, a compact convex set (ĝ = 0
where w = 0). For real ν, `Σ_n g(n)ν(n) = Q Σ_θ ĝ(θ) conj(ν̂(θ)) ≤ R_w(ν)`, with
equality for `Qĝ(θ) = w(θ) ν̂(θ)/|ν̂(θ)|` (any unimodular value where ν̂ = 0,
chosen conjugate-symmetric, so g is real). Hence `R_w(ν) = max_{g∈G} ⟨g, ν⟩`.
The constraint "ν majorant" is `ν ≥ 1_𝒜` pointwise on ℤ/Q (since 1_𝒜 ≥ 0). By
Sion's minimax theorem (bilinear form, G compact convex, feasible set convex),
`min_{ν ≥ 1_𝒜} max_{g∈G} ⟨g,ν⟩ = max_{g∈G} inf_{ν ≥ 1_𝒜} ⟨g,ν⟩`. The inner
infimum is −∞ unless g ≥ 0, and then it is `⟨g, 1_𝒜⟩` (attained at ν = 1_𝒜).
The max is attained (G compact); the min is attained because ν ≥ 0 and
`R_w(ν) ≥ w(0)Eν` make the sublevel sets bounded when w(0) > 0. (This is
convex/SOCP duality; "LP" below is used loosely.) ∎

*Remark.* `g(n) = Ψ(n − t)` periodised is in G (its `Qĝ` is `Ψ̌(−θ)e(−tθ)`, of modulus `|Ψ̌(θ)|` as Ψ is real), which
is the dual form of Lemma 1.1. The KARY/NC caps are the statement that, for
`w ≥ 1` at θ ≠ 0 (and the prime-slice/forced structure), G contains a g with
value `≥ N e^{−C(log N)^{3/4}}`; such g may be very rough. For weights below 1,
G consists of functions whose spectrum is (essentially) confined where w is
large, and §2 shows this confines g to be smooth at scale N.

## 2. Band-limited windows: the general-majorant door is exactly M(N)

Let K ≥ 1 and let Φ = Φ_K be Selberg's majorant of `1_{[0,1]}` with
`Φ̂` supported in `[−K, K]` and `∫Φ = Φ̂(0) = 1 + 1/K` (Vaaler, Bull. AMS 12
(1985); Montgomery, *Ten lectures*, Ch. 1). Φ ≥ 0, Φ ≥ 1 on [0,1], Φ is entire of
exponential type and `Φ(x) = O(x^{−2})`, so `Σ_n Φ(n/N)` converges absolutely.

**Lemma 2.0 (PROVED, routine).** For N ≥ 4K: `W_N(θ) = 0` unless `‖θ‖ ≤ K/N`,
and `W_N(0) = N(1 + 1/K)`.

*Proof.* Poisson (valid: Φ ∈ L¹, Φ̂ continuous with compact support, Φ = O(x^{−2})):
`W_N(θ) = Σ_k N Φ̂(N(k − θ))`. A term is nonzero only if `|k − θ| ≤ K/N ≤ 1/4`. ∎

**Theorem 2.1 (per-frequency rounding with a band-limited window ≍ the
shift-uniform count; PROVED).** For every finite family (any classes, any
moduli) and N ≥ 4K,

    M(N) ≤ min_{ν majorant} Σ_θ |ν̂(θ)| |W_N(θ)| ≤ 12(K+1)·M(⌈N/K⌉) ≤ 12(K+1)·M(N).   (2.1)

*Proof.* Lower bound: Lemma 1.1 (Φ ≥ 1 on [1/N, 1]). Upper bound: by Lemma 1.2 it
suffices to bound `⟨g, 1_𝒜⟩` for g ≥ 0 with `|Qĝ| ≤ |W_N|`. By Lemma 2.0 the
spectrum of g lies in `‖θ‖ ≤ δ := K/N ≤ 1/4`.

*Reproducing kernel.* Put `k_δ(x) = δ(sin πδx / πδx)²`, whose Fourier transform
is the triangle `(1 − |ξ|/δ)_+`, and `v = 2k_{2δ} − k_δ`. Then `v̂ = 1` on
`|ξ| ≤ δ` and `v̂ = 0` for `|ξ| ≥ 2δ`, and `|v(x)| ≤ 5δ min(1, (πδx)^{−2})`. By
Poisson, `Σ_{m∈ℤ} v(m) e(−mθ) = Σ_k v̂(θ + k)`, which equals 1 for `‖θ‖ ≤ δ`
(2δ ≤ 1/2). Since g is a trigonometric polynomial with spectrum in `‖θ‖ ≤ δ`,

    g(n) = Σ_{m∈ℤ} v(m) g(n − m)      for every n (absolutely convergent).

*Bound.* Summing over n mod Q and substituting r = n − m,

    ⟨g, 1_𝒜⟩ = Σ_{r mod Q} g(r) Σ_{m∈ℤ} v(m) 1_𝒜(r + m)
             ≤ Σ_{r mod Q} g(r) · Σ_{m∈ℤ} |v(m)| 1_𝒜(r + m),

using g ≥ 0. Cut ℤ into blocks `I_j = [jL, (j+1)L)`, `L = ⌈1/δ⌉`. Each block
meets `𝒜 − r` in at most `M(L)` points. On `I_j` we have `|v| ≤ 5δ` for
j ∈ {−1, 0}, and `|v| ≤ 5δ/(π² j'²)` with `j' = j` (j ≥ 1) or `j' = |j| − 1`
(j ≤ −2). So the inner sum is ≤ `5δ M(L)(2 + 2·π^{−2}·π²/6) ≤ 12 δ M(L)`.
Finally `Σ_r g(r) = Qĝ(0) ≤ W_N(0) = N(1+1/K)`, and `12δ·N(1+1/K) = 12(K+1)`.
M is nondecreasing, and `⌈N/K⌉ ≤ N`. ∎

**Corollary 2.2 (PROVED).** (a) For the window Φ_K there is a majorant ν of 𝒜
(a general Q-periodic function, not a hit-pattern or level-restricted one)
whose per-frequency bound is `≤ 12(K+1)M(N)`. (b) Hence, for fixed K and per-frequency
smooth rounding over general majorants, a cap of the form
`saving ≤ C(log N)^{3/4}` holds **if and only if**
`M(N) ≥ N exp(−C′(log N)^{3/4})` (with C, C′ related by `log(12(K+1))`).
This is a statement about one fixed family 𝔊 (M = M_𝔊).
(c) By Lemma 1.1, a lower bound (W_𝔊) would cap **every**
per-frequency bound with `w ≥ |W_N|` or `w ≥ |S_N|`, for every majorant class and
every window, **for methods using the family 𝔊** (or a subfamily of it, since M only
grows when classes are removed). To cap all methods using families in 𝔉_A one needs
(W_{𝔉_A}) (R81 repair, applied by reviewer).

So the "weights below 1" door for general majorants is not a door about
Fourier analysis at all: it is the shift-uniform version of the counting
problem. It is the analogue of IF Obs 1.1 (exact interval evaluation over
unrestricted majorants is the problem itself), with [1,N] replaced by the
worst window. In particular no arithmetic-free argument (Walsh tails,
comparison measures, LP caps built from level/mass hypotheses) can cap this
class unless it proves a lower bound for M(N) — a statement about the
avoider set itself.

*What M(N) is.* By CRT, t ranges over all residue vectors. In a prime-slice
system (Q₀ = 1, one prime ℓ per class set F_ℓ) M(N) is the **translate sieve**

    M(N) = max_{(c_ℓ)} #{ j ∈ [1,N] : j + c_ℓ ∉ F_ℓ (mod ℓ) for all ℓ }.     (2.2)

A class set with `N·|F_ℓ| < ℓ` has a gap of length N mod ℓ and is avoided at no
cost. In a prime-slice system of ℛ(ℓ) classes (`|ℛ(ℓ)| = ℓ^{o(1)}`, independent
primes) only moduli `≤ N^{1+o(1)}` therefore matter for M(N); for overlapping
composite moduli the CRT choices are not independent and this reduction is
not claimed. *(R81 repair, applied by reviewer.)* For the 3/4-note family 𝔊_X (not
for the ℛ(ℓ) prime slices of (2.2)) the upper bound `M_{𝔊_X}(N) ≤ N exp(−c(log N)^{3/4})`
holds, because the 3/4 note's bound is shift-uniform (Prop 5.1(a)). For the Q₀ = 1
ℛ(ℓ) toy family 𝔊_ℛ no such bound is claimed. Its mass over primes is a smaller power
of log, so 3/4 is not its natural benchmark. Whether M_𝔊(N) is that large is §5.

## 3. Sharp weights for hit-pattern majorants: capped without (H_eq)

Setting of NC §2.5: a prime-slice system with Q₀ = 1 (distinct primes ℓ ∈ 𝒫,
class sets `F_ℓ ⊂ ℤ/ℓ`, `p_ℓ = |F_ℓ|/ℓ ≤ 1/4`), and a **hit-pattern majorant**
`ν(n) = f(x(n))`, `x_ℓ(n) = 1[n mod ℓ ∈ F_ℓ]`, with biased Walsh expansion
`ν = Σ_S d_S y^S`. As in NC §2.5, `ν̂` on `Θ_S` equals `d_S·Π_{ℓ∈S} 1̂_{F_ℓ}(h_ℓ)`,
so for any weight w

    R_w(ν) = Σ_S |d_S| M_S^w,   M_S^w = Σ_{θ∈Θ_S} m_S(θ) w(θ),
    m_S(Σ h_ℓ/ℓ) = Π_{ℓ∈S} |1̂_{F_ℓ}(h_ℓ)|,   A_S := Σ_θ m_S(θ) = Π_{ℓ∈S} a_ℓ,       (3.1)

`a_ℓ = Σ_{h≠0} |1̂_{F_ℓ}(h)| ≥ Σ|1̂|²/max|1̂| = 1 − p_ℓ`. Put
`g_ℓ(n) = Σ_{h≢0} |1̂_{F_ℓ}(h)| e(nh/ℓ)` (real, since `|1̂_F(−h)| = |1̂_F(h)|`) and
`φ_ℓ(n) = g_ℓ(n)/a_ℓ ∈ [−1, 1]`.

**Lemma 3.1 (sin² lower bound; PROVED).** If `w(θ) ≥ c₀|sin πNθ|` for all θ ≠ 0,
then for every S ≠ ∅

    M_S^w ≥ (c₀/2) · A_S · (1 − |Π_{ℓ∈S} φ_ℓ(N)|).

This applies to the sharp weight `|S_N(θ)| = |sin πNθ|/|sin πθ| ≥ |sin πNθ|`
(c₀ = 1).

*Proof.* `|sin x| ≥ sin² x = (1 − cos 2x)/2`. So
`M_S^w ≥ (c₀/2) Σ_θ m_S(θ)(1 − cos 2πNθ) = (c₀/2)(A_S − Re Σ_θ m_S(θ)e(Nθ))`.
Since `m_S` is a product measure in the CRT coordinates and
`e(Nθ) = Π_ℓ e(Nh_ℓ/ℓ)`, `Σ_θ m_S(θ)e(Nθ) = Π_ℓ g_ℓ(N) = A_S Π_ℓ φ_ℓ(N)`. ∎

**Lemma 3.2 (one-prime anti-concentration; PROVED).** Let ℓ be an odd prime,
ℓ ∤ N, `F ⊂ ℤ/ℓ` with `|F| = k ≥ 1`, `p = k/ℓ ≤ 1/4`. Then
`1 − |φ_ℓ(N)| ≥ 9/(256 k²)`.

*Proof.* Let μ be the probability measure `|1̂_F(h)|/a_ℓ` on h ≢ 0. Then
`1 − |φ(N)| ≥ Σ_h μ(h)(1 − |cos(2πNh/ℓ)|)`. For `η ∈ (0,1/2]`, put
`B = {h ≢ 0 : ‖2Nh/ℓ‖ < η}`. As `h ↦ 2Nh` is a bijection of ℤ/ℓ (ℓ odd, ℓ ∤ N),
`#B ≤ 2ηℓ`. Each `|1̂_F(h)| ≤ p` and `a_ℓ ≥ 1 − p ≥ 3/4`, so
`μ(B) ≤ 2ηℓp/(3/4) = (8/3)ηk`. Off B, `1 − |cos(2πNh/ℓ)| = 1 − cos(π‖2Nh/ℓ‖) ≥ 2η²`
(`1 − cos y ≥ 2y²/π²` on [0,π]). With `η = 3/(16k)`: `μ(B) ≤ 1/2` and
`1 − |φ| ≥ (1/2)·2η² = 9/(256k²)`. ∎

**Theorem 3.3 (sharp and sin-dominated weights are capped for hit-pattern
majorants; PROVED).** Take a prime-slice system with Q₀ = 1 and `p_ℓ ≤ 1/4`.
Fix γ < 1/3 and `s_* ∈ (0, log 2]`; call ℓ *good* if `|F_ℓ|³ ≤ ℓ e^{−s_*}/2`,
*bad* otherwise (bad primes are `< (2e^{s_*})^{1/(1−3γ)}` if `|F_ℓ| ≤ ℓ^γ`; we only
assume their number and size are bounded, `B₁ := Σ_{ℓ bad} log ℓ < ∞`). Weights:

    s_ℓ = log(ℓ/(2|F_ℓ|³)) = log(1/(2p_ℓ)) − 2log|F_ℓ|   (ℓ good),
    s_ℓ = log(1/(2p_ℓ))                                    (ℓ bad);

all `s_ℓ ≥ s_*`. Let ν be a hit-pattern majorant of arbitrary level and w any
weight with `w(0) = N` and `w(θ) ≥ c₀|sin πNθ|` for θ ≠ 0. Then for every
`λ ≥ log N + B₁` NC Thm 2.3 holds with ε replaced by
`ε^w := (512/(9c₀))·e^{−λ}·R_w(ν)`:

    Eν ≥ (1 − ε^w) e^{−Φ̄(λ,α)} − 2ε^w,

Φ̄ computed with these s_ℓ. Consequently, if the system satisfies the mass
hypothesis
(M) `|F_ℓ| ≤ ℓ^γ` for good ℓ, and `Σ_ℓ p_ℓ ℓ^{−β} ≤ C_M β^{−3}` for β ∈ (0,1]
(true for ℛ(ℓ)-slices **restricted to primes ℓ ≥ ℓ₀**, `|ℛ(ℓ)| = ℓ^{o(1)}`, by ET Lemmas
3.1, 3.2, 3.7 as used in NC Cor 2.5), then every bound `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ) = N e^{−s}` with ν a
hit-pattern majorant has

    s ≤ C₉(γ, C_M, B₁, c₀) (log N)^{3/4}      (N ≥ N₀).

*Scope for ℛ(ℓ)-slices (R81 repair, applied by reviewer).* The theorem assumes
`p_ℓ ≤ 1/4` for **every** ℓ ∈ 𝒫, bad primes included. NC Prop 2.1, ET Prop 2.4 and
the r₀ step all use this. The Q₀ = 1 family 𝔊_ℛ violates it at small primes:
`|ℛ(ℓ)|/ℓ = 1/3, 3/7, 3/11, 9/23, 13/47` for `ℓ = 3, 7, 11, 23, 47`. Discarding these
primes is not WLOG: a majorant for the full family need not majorise the larger avoider
set of the reduced family. So the application to ℛ(ℓ)-slices is claimed **only for
the toy family 𝔊_ℛ^{≥ℓ₀} of primes ℓ ≥ ℓ₀**, where ℓ₀ is such that `|ℛ(ℓ)| ≤ ℓ/4` and
`|ℛ(ℓ)| ≤ ℓ^γ` for all ℓ ≥ ℓ₀, and `ℓ₀ ≥ (2e^{s_*})^{1/(1−3γ)}` (then there are no bad
primes, B₁ = 0). Covering the
small primes would need the Q₀ > 1 version, conditioning on `n mod Π_{ℓ<ℓ₀} ℓ` as in
NC Thm 2.3. That extension is not written out here, and it is **not claimed**. The ES
families, whose F_ℓ(c) depend on the fibre c, are not covered either.

*Proof.* Only NC's tail estimate (2.3) changes. Let `s(S) > λ`. Bad primes
contribute at most B₁ to s(S), and `s_ℓ < log ℓ` for good ℓ, so the good primes
of S have product `> e^{λ−B₁} ≥ N`; hence some good `ℓ₀ ∈ S` does not divide N
(and ℓ₀ ≥ 5 since p ≤ 1/4). Lemmas 3.1–3.2 with ℓ₀ give
`M_S^w ≥ (9c₀/512)·A_S/|F_{ℓ₀}|² ≥ (9c₀/512)·Π_S(1−p_ℓ)/|F_{ℓ₀}|²`. By the
choice of weights, `Π_S 2p_ℓ·|F_{ℓ₀}|² ≤ e^{−s(S)}`. Hence

    |d_S| Π_S 2p_ℓ(1−p_ℓ) ≤ (512/(9c₀)) |d_S| M_S^w e^{−s(S)},

and `Π_S p_ℓ ≤ Π_S (4/3)p_ℓ(1−p_ℓ) ≤ Π_S 2p_ℓ(1−p_ℓ)`. Summing over `s(S) > λ`,
`r₀, r₁ ≤ (512/(9c₀)) e^{−λ} Σ_S |d_S| M_S^w ≤ ε^w`. The rest of NC Prop 2.1 /
Thm 2.3 uses only `s_ℓ ≥ s_*`. For the consequence: `R_w(ν) ≤ N e^{−s} ≤ N`;
take `λ = 2 log(4N) + log(512/(9c₀)) + B₁`, so `ε^w ≤ e^{−Φ̄}/4` once
`Φ̄(λ) = o(log N)`, and conclude as in NC Cor 2.4. For Φ̄: on good primes
`e^{−αs_ℓ} ≤ 2^α ℓ^{−α(1−3γ)}`, so `Σ p_ℓ e^{−αs_ℓ} ≤ 2C_M(α(1−3γ))^{−3} + O_{B₁}(1)`;
and `s_ℓ ≤ λ` forces `ℓ ≤ (2e^{λ+s_*})^{1/(1−3γ)}` (good) =: X, so the truncated mass is
`Σ_{ℓ≤X} p_ℓ ≤ e·Σ_ℓ p_ℓ ℓ^{−1/log X} ≤ e·C_M (log X)³ + O_{B₁}(1) ≪ λ³` (β = 1/log X in (M)). With α = λ^{−1/4}
this is NC Cor 2.5's computation: `Φ̄ ≤ Cλ^{3/4} + O(log²λ)`. ∎

*What this closes.* In NC §2.5's list: the exact sharp weight `|S_N(θ)|` and
every per-frequency rounding whose weights dominate `c₀|sin πNθ|` (this
includes ψ-based Erdős–Turán/Vaaler rounding *provided* its weights, in the
normalisation (1.1), admit such a lower bound — not checked here), for hit-pattern
majorants with Q₀ = 1 and all `p_ℓ ≤ 1/4` (for ℛ(ℓ): primes ℓ ≥ ℓ₀ only), are capped at
`(log N)^{3/4}` without (H_eq). The
mechanism: a weight below 1 only near `‖Nθ‖ = 0` is harmless because the
product measure m_S cannot concentrate near `{‖Nθ‖ = 0}` — its N-th
"characteristic function" `Πφ_ℓ(N)` is bounded away from 1 by a single
coordinate.

*Not closed by §3:* smooth windows (weights tiny on all of `‖θ‖ ≫ 1/N`, so
anti-concentration is not enough; one needs equidistribution, (H_eq)); and
general (non-hit-pattern) majorants with sharp weights (they may reshape ν̂
inside Θ_S towards `‖Nθ‖ ≈ 0`; whether positivity forbids this is open).

## 4. Smooth windows for hit-pattern majorants: what (H_eq) really asks

Same setting as §3 (Q₀ = 1, hit-pattern ν), now `w = |W_N|` for a fixed window Φ
(Φ ≥ 0, Φ ≥ 1 on [0,1], Φ̂ continuous and integrable decay so that Poisson
applies). Then `W_N(θ) = Σ_k NΦ̂(N(k−θ))`, and there are `c_Φ > 0`, `N_Φ` with
`|W_N(θ)| ≥ N/3` for `‖θ‖ ≤ c_Φ/N`, N ≥ N_Φ (continuity of Φ̂ at 0, Φ̂(0) ≥ 1).
NC (2.6) / IF Lemma 4.1 need `M_S^{|W|} ≳ e^{−o(λ)} A_S` (or `N^{−A}Π(1−p)`) for
`s(S) > λ`. Write `X_S = Σ_{ℓ∈S} X_ℓ mod 1` with independent `X_ℓ = h_ℓ/ℓ`,
`P(X_ℓ = h/ℓ) = |1̂_{F_ℓ}(h)|/a_ℓ` (h ≢ 0). Then `M_S^{|W|} = A_S·E|W_N(X_S)|`, and the
"characteristic function" of X_S is `E e(kX_S) = Π_ℓ φ_ℓ(k)`.

**Lemma 4.1 (a sufficient condition; PROVED).** If

    Σ_{0<|k|≤N/c_Φ} |Π_{ℓ∈S} φ_ℓ(k)| ≤ 1/6,                                     (4.1)

then `M_S^{|W|} ≥ (c_Φ/6) A_S`.

*Proof.* Let T be Selberg's minorant of the arc `‖θ‖ ≤ c/N` (c = c_Φ) on ℝ/ℤ, a
trigonometric polynomial of degree `H = ⌈N/c⌉ − 1 ≤ N/c` with `T ≤ 1_{‖θ‖≤c/N}`,
`T̂(0) = 2c/N − 1/(H+1) ≥ c/N`, `|T̂(k)| ≤ |1̂_arc(k)| + (2c/N − T̂(0)) ≤ 3c/N`. Then
`M_S ≥ (N/3) A_S P(‖X_S‖ ≤ c/N) ≥ (N/3) A_S E T(X_S)` and
`E T(X_S) = Σ_{|k|≤H} T̂(k) Πφ_ℓ(k) ≥ (c/N)(1 − 3·(1/6))`. ∎

**Lemma 4.2 (one large prime; PROVED).** If S = {ℓ} with `ℓ ≥ 2|F_ℓ|N/c_Φ`, then
`M_S^{|W|} ≥ c_Φ/6 ≥ (c_Φ/(6√|F_ℓ|))·A_S`.

*Proof.* Fejér at a point `x₀ ∈ F` (`H' = ⌈cℓ/N⌉ ≥ 2|F|`; integer `|h| < H'` still have `‖h/ℓ‖ ≤ c/N`): the Fejér kernel is
nonnegative, so `Σ_{|h|<H'}(1−|h|/H')1̂_F(h)e(hx₀/ℓ) = ℓ^{−1}Σ_{y∈F}F_{H'}((x₀−y)/ℓ)
≥ H'/ℓ`; removing h = 0 (value p) gives `Σ_{0<|h|<H'}|1̂_F(h)| ≥ (H' − |F|)/ℓ ≥ c/(2N)`,
and these h have `‖h/ℓ‖ ≤ c/N`. Finally `a_ℓ ≤ (ℓ Σ|1̂_F|²)^{1/2} ≤ √|F|`. ∎

So for a single high prime (H_eq) holds with an affordable loss `√|F_ℓ|` (absorbed
by weights exactly as in Thm 3.3). The single-prime proof uses that the scale
`1/N` is coarse compared with `1/ℓ`. With **several** primes the target is the
density of a *sum* `X_S` near 0. A product box (all `‖X_ℓ‖ ≤ c/(N|S|)`) loses a
factor `≈ (N|S|)^{|S|−1}`, and near an arbitrary point β the one-coordinate
mass can be very small (F = {−2,−1} ⊂ ℛ(ℓ) for ℓ ≡ 7 (8): `|1̂_F(h)| = (2/ℓ)|cos πh/ℓ|`
vanishes to first order at θ = 1/2). Lemma 4.1 needs the characteristic function
`Πφ_ℓ(k)` to be `o(1/N)` on average over `0 < |k| ≲ N`. For ℛ(ℓ)-slices this is a
statement about `Σ_h |1̂_{ℛ(ℓ)}(h)| e(kh/ℓ)` for small k; the absolute value
destroys the multiplicative structure of the classes `−u/v`, and small-height
labels give **positive** correlations at small k (e.g. `{−2,−1} ⊂ ℛ(ℓ)` gives
`φ_ℓ(1) ≈ 1/3` for that pair alone), which help (H_eq) but are not summable to
≤ 1/6 in general. **Status: (H_eq) for several primes ≤ N^{O(1)} remains
CONJECTURE.** Neither a proof nor an abstract counterexample (a family whose
`X_S` avoids the `1/N`-neighbourhood of 0 for all high S) was found; depletion
would need every `|1̂_{F_ℓ}|` to avoid low frequencies, while Lemma 4.2's Fejér
argument shows that a sparse F always carries spectral mass `≥ c/N` within `c/N`
of 0.

**Relation to §2.** For hit-pattern majorants the smooth per-frequency LP value
is ≥ M(N) (Lemma 1.1). So the hit-pattern smooth door is closed if *either*
(H_eq) holds (NC §2.5, IF Lemma 4.1) *or* `M(N) ≥ N e^{−C(log N)^{3/4}}` (§5).

## 5. The shift-uniform count M(N)

By §§1–2 the whole per-frequency door, for general majorants, is the size of

    M(N) = max_{t∈ℤ} #(𝒜 ∩ (t, t+N])     (𝒜 = avoider set of the method's finite family).

**Proposition 5.1 (what is known; PROVED or cited).**
(a) `#(𝒜_X ∩ [1,N]) ≤ M_{𝔊_X}(N) ≤ N exp(−c(log N)^{3/4})` for the 3/4-note family 𝔊_X
(its bound `N·Eν + Σ|a_i|` is shift-uniform). *(R81 repair, applied by reviewer: this is
the only family for which the upper bound is claimed; it is not claimed for 𝔊_ℛ or for
other members of 𝔉_A. Members of 𝔉_A that contain 𝔊_X have smaller M.)*
(a′) *(R81 repair, applied by reviewer.)* `E_pr(N) ≤ K + y + M_{𝔊_X}(N)`, with K, y as
in the 3/4 note. The note's ν_X is ≥ 1 only on exceptional **primes** > max(K, y), so
these primes lie in 𝒜_X. The statement "E(N) ≤ M(N)" is **not** claimed: E(N) also
counts composites, n = 1 and primes ≤ max(K, y), and their membership in 𝒜_X is not
shown. E(N) itself is bounded from E_pr by the note's Rankin/semigroup step.
(b) (random/gap translates) In a prime-slice system with Q₀ = 1,
`M(N) ≥ N·Π_{ℓ: (N+1)|F_ℓ| > ℓ}(1 − p_ℓ)`.
(d) (greedy) In a prime-slice system with Q₀ = 1, for every s ≥ 1,
`M(N) ≥ ⌊min(s, N·Π_{ℓ ≤ s|F_ℓ|}(1 − p_ℓ))⌋`. For ℛ(ℓ)-slices this gives
`M(N) ≥ exp(c(log N)^{1/3})`.
(c) (equivalence) For the window Φ_K of §2 and every finite family 𝔊 (M = M_𝔊;
per family — R81 repair, applied by reviewer):
`M(N) ≤ min_ν R_{|W_N|}(ν) ≤ 12(K+1)M(N)`. Hence: *every translation-invariant
per-frequency method (any weights ≥ |W_N| or ≥ |S_N|) is capped at
`(log N)^{3/4}` ⇔ `M(N) ≥ N e^{−C(log N)^{3/4}}`, and if
`M(N) ≤ N e^{−ω(N)(log N)^{3/4}}` (ω → ∞) then some general majorant beats the
cap through a band-limited per-frequency bound.*

*Proof.* (a′) Let p > max(K,y) be an exceptional prime. Then S_y(p) = 1, because p > y
(the note, after its eq. (selector)). Also H_X(p) = 0: by the note's identity lemma a
prime > K in an atom class is representable. This is how the note gets ν_X(p) ≥ 1. So
p ∈ 𝒜_X, and the window [1,N] is one of the windows in M. (a) The first inequality is t = 0; the second: the 3/4 note's majorant
is a CRT majorant on all of ℤ and each class meets a window in ≤ N/d + 1 points.
(b) If `ℓ ≥ (N+1)|F_ℓ|`, the complement of F_ℓ on the cycle ℤ/ℓ has a gap of ≥ N
consecutive residues; choose `t mod ℓ` to put `t+1, …, t+N` in it. For the
remaining ("dense") primes take `t mod ℓ` uniform and independent (CRT); each
`t + j` then avoids all dense classes with probability `Π(1 − p_ℓ)`, so the
expected window count is `N Π_{dense}(1 − p_ℓ)`, and the maximum is at least that.
(c) Theorem 2.1 and Lemma 1.1.
(d) Start with X = [1,N] and treat the primes `ℓ ≤ s|F_ℓ|` one by one: since
`Σ_{c mod ℓ} #{x∈X : x + c ∈ F_ℓ} = |X||F_ℓ|`, some c_ℓ kills `≤ p_ℓ|X|` points, so
afterwards `|X| ≥ NΠ(1−p_ℓ)`. Shrink X to `⌊min(s,|X|)⌋` points. Every remaining
prime has `ℓ > s|F_ℓ| ≥ |X||F_ℓ|`, so some translate kills nothing. For ℛ(ℓ)-slices
`Σ_{ℓ≤x}p_ℓ ≪ (log x)³` and `|F_ℓ| = ℓ^{o(1)}`; take `log s = c(log N)^{1/3}`. ∎

For ℛ(ℓ)-slices `Σ_{ℓ≤N^{1+o(1)}} p_ℓ` is a power of log N (≍ (log N)³ over all
moduli M by Elsholtz–Tao; over primes alone a smaller power), so (b) gives only
`N e^{−(log N)^{c}}` and (d) only `e^{c(log N)^{1/3}}`. The gap between (a) and
(b)/(d) is the whole question.

**Open problem (W).** *(R81 repair, applied by reviewer: family made explicit.)* Is
(W_{𝔉_A}) true, i.e. `min_{𝔊∈𝔉_A, N} M_𝔊(N) ≥ N exp(−C_A(log N)^{3/4})` for N ≥ N₀ (equivalently:
is the 3/4 barrier valid for all translation-invariant counting methods using forced-class
families with moduli ≤ N^A)? Since M decreases as 𝔊 grows, this is a question about the
largest admissible families, not about 𝔊_X. For the toy family 𝔊_ℛ the corresponding
question should be asked at its own sieve-limit exponent, which is below 3/4.
Either answer would matter:
* a proof of `M(N) ≤ N e^{−(log N)^θ}`, θ > 3/4, would be a new exceptional-set
  bound for 𝒜 (`E_pr(N) ≤ K + y + M_{𝔊_X}(N)` if 𝔊 ⊇ 𝔊_X, see Prop 5.1(a′)), uniform over shifts;
* a proof of `M(N) ≥ N e^{−C(log N)^{3/4}}` would close the "weights below 1"
  door completely (all weights, all majorants), and would show that any
  improvement on 3/4 must use the position of the window — e.g. that [1,N]
  sits next to 0 — not just its length.

*Discussion (Assessment).* The KARY dual objects (comparison measures matching
uniform on every level-λ test function, LS2 Lemma 1.1) live on the CRT torus.
M(N) asks whether such pseudo-distributions are realised by the empirical
pattern distribution of an actual window, i.e. by one translate `c_ℓ` per
prime. A window of length N sees every residue mod ℓ ≤ N about N/ℓ times, so
all level-`≤ log(N/2)` statistics of a window are forced (IF Thm 2.2 logic); the
freedom is in correlations of combined modulus > N, where kill sets of two
primes `ℓℓ′ > N` overlap in at most `|F_ℓ||F_ℓ′|⌈N/ℓℓ′⌉` points and the choice of
translates decides which. The random choice (b) is far from optimal (§5.1
EVIDENCE), so translates do correlate kills strongly; whether up to the
sieve-limit scale is not known.

### 5.1 Toy translate sieve (EVIDENCE only)

`scripts/weights_translate_sieve.py`: family = primes ℓ ≤ 100N, ℓ ≡ 3 (4), with
`F_ℓ = ℛ(ℓ) = {−u/v mod ℓ : gcd(u,v)=1, 4uv | ℓ+1}` (Q₀ = 1). Sparse primes
(`ℓ ≥ (N+1)|F_ℓ|`) are free by Prop 5.1(b). The lower bound for M(N) comes from
coordinate ascent over the translates `c_ℓ` of the dense primes, on the
smoothed objective `Σ_j 0.3^{#kills(j)}`, with 3 restarts. The upper bound is
Montgomery's large sieve, which is shift-uniform and position-blind. The
"saving" is log(N/count).

| N | dense primes | random translates: N Π(1−p) (saving) | t = 0: #(𝒜∩[1,N]) | local search: M(N) ≥ | large sieve: M(N) ≤ |
|---|---|---|---|---|---|
| 300 | 664 | 0.0011 (12.50) | 19 (2.76) | 28 (2.37) | 155 (0.66) |
| 1000 | 2131 | 0.0001 (15.85) | 35 (3.35) | 48 (3.04) | 427 (0.85) |

Reading: optimised translates keep 10⁴–10⁵ times more of the window than
random translates. M(N) lies between the large-sieve scale and about 2–3
units of saving below it, nowhere near the random scale. The t = 0 count is
inflated by squares (which avoid every forced class). This is consistent with
(W) — translates can realise near-sieve-limit correlations — but N ≤ 1000
says nothing about exponents, and local search gives only lower bounds.
(N = 3000 was started and stopped for time.)

## 6. Sharp weights for general majorants

For `w = |S_N|` the dual g need not be smooth (`|S_N(θ)| ≥ |sin πNθ|` is ≥ 1/2 on
two thirds of the circle), so Theorem 2.1's upper bound does not apply. The
only lower bound we have is M(N) (Lemma 1.1).

*Remark 6.1 (a route that adds nothing; PROVED).* Averaging a w ≥ 1
certificate over the window — `g = N^{−1}Σ_{m≤N} g₁(· − m)` with `g₁ ≥ 0`,
`Qĝ₁(0) ≤ N`, `|Qĝ₁| ≤ 1` off 0 — is admissible for `w = |S_N|`, and gives the lower
bound `LP₁(h/N) := min{N·Eν + Σ_{θ≠0}|ν̂(θ)| : ν ≥ h/N}`, `h(t) = #(𝒜∩(t,t+N])`.
But the constant `ν ≡ M(N)/N` is feasible, so `LP₁(h/N) ≤ M(N)`: this route never
beats Lemma 1.1. (Reviewer's observation.)

So for general majorants with sharp weights we know only `≥ M(N)`; whether the
best sharp bound is ≍ M(N) (as for band-limited windows) or is capped by a
w ≥ 1–type argument is open. Either way (W) would close it. For hit-pattern
majorants §3 closes the sharp door without (H_eq).

## Replay

```
cd scripts
ulimit -v 8000000
for a in "300 30000 3" "1000 100000 3"; do timeout 10000 uv run --with numpy python weights_translate_sieve.py $a 1 0.3; done > ../data/weights/translate_sieve.txt   # ~1 min + ~70 min, <2 GB, 1 core
```
