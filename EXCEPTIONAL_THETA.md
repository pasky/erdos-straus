# EXCEPTIONAL_THETA — where the exceptional-set exponent stops (task a2)

Status: **outcome (B)**. This file does not prove any θ > 3/4. It proves that
the exponent 3/4 is exactly the ceiling of a precisely defined class of
architectures. That class contains Vaughan, Pomerance–Weingartner, the 2/3
loglog note and the 3/4 note. The file also gives exact accounting for the
two campaign proofs and settles the candidate levers one by one.

Labels follow `DISCOVERIES.md`. Here **PROVED** means proved in this file and
checked internally only. It is not refereed, and its novelty is unchecked.
The sieve-limit theorem (§2) may be folklore in spirit; no source was found.
"Verified numerically" never means proved.

Notation: `L = log N`, `λ = log D` (the *level* of a majorant), `X = e^t`.

---

## 0. Summary

| item | statement | label |
|---|---|---|
| Thm 2.5 | **Sieve-limit theorem.** Take a *prime-slice* CRT system: the conditions are independent across large primes ℓ once a small residue c is fixed. Every nonnegative majorant of level λ of its avoider set has mean ≥ `exp{−19αλ − C₄ Σ_ℓ p̄_ℓ ℓ^{−α} − O(log²λ)}`, for every α>0. | PROVED |
| Cor 3.4 | Take any prime-slice family of forced classes (multiplier identity, both groupings, with small parts k ≤ ℓ^C, C<1). Every majorant of level `N^A`, and every Montgomery large-sieve bound, saves at most `C(A) (log N)^{3/4}`. So **3/4 is sharp for this class, and no power of log log N can be gained.** | PROVED |
| Cor 3.5 | Polylogarithmic multipliers, or multipliers whose lcm is at most N (the 2/3 note's architecture), cap the saving at `C L^{2/3}(log L)^{1/3}`. **The 2/3-loglog note is sharp for its architecture.** | PROVED (given the notes' BT upper bounds) |
| §4 | Exact accounting. In both proofs the binding constraint is the pair (supply profile, level). Bonferroni depth, the BV level and the selector are not binding: they change constants only. | PROVED (Lemmas 4.1–4.4) |
| §5 | Levers. Cost-per-condition, beyond-identity supply, both halves and Bonferroni→Selberg are closed by proved statements. Case A needs the numerically supported bound H_A3. Halász is closed by a counterexample plus Assessment. The ET first moment is consistent with B = 3. One door stays open: multi-slice moduli and multipliers larger than the slice prime (H_MS). | see table §5.0 |
| §5.3 | Complete-system void among 4.05·10⁹ real primes near 10¹². The effective mass −log P(void) falls from 1.39 to about 0.80 of the first-moment mass as Q grows to 4000. There is no super-cubic effect. | EVIDENCE |
| §2.6 | In the exchangeable model, the exact LP optimum equals the Selberg/Christoffel value 1/Σ_{j≤m/2} μ^j/j! to 3 decimals. So Selberg Λ² is essentially optimal, and Bonferroni loses only a constant factor. | EVIDENCE |

**Verdict.** No route to θ > 3/4 survives inside the prime-slice CRT world. The
Rankin functional `inf_α[αλ + Σ p̄_ℓ ℓ^{−α}]` is an exact two-sided description
of what any such sieve can save. The lower side is the large sieve or the 3/4
note; the upper side is Theorem 2.5. The identity supply profile satisfies
`Σ p̄_ℓ ℓ^{−α} ≍ α^{−3}`, which gives λ^{3/4}. Beating 3/4 requires one of
three things:
1. conditions whose modulus has **two or more large prime factors at
   comparable scales**, used *jointly*. Theorem 2.5 does not cover these
   (hypothesis H_MS, §5.6);
2. multipliers far larger than the slice prime, without per-condition lcm
   cost (§5.6);
3. a non-CRT ingredient, i.e. arithmetic of the actual integers beyond
   residue counting.

The a-frame and multiplicative route (§5.2) is of type 3. Under its model it
sits at θ* ≈ 0.52 < 3/4.

---

## 1. Definitions

**Prime-slice CRT system.** The data are:
* a modulus `Q₀` (the *small* modulus);
* a finite set `𝒫` of primes not dividing `Q₀` (the *slice primes*);
* a set `R ⊆ ℤ/Q₀` of admissible small residues (for example the selector
  `(c,P_y)=1`, or the reduced classes);
* for each `c ∈ R` and `ℓ ∈ 𝒫`, a set `F_ℓ(c) ⊆ ℤ/ℓ` of forbidden classes.

The *avoider set* is
`𝒜 = {n : n mod Q₀ ∈ R, n mod ℓ ∉ F_ℓ(n mod Q₀) for all ℓ∈𝒫}`.

Write `p_ℓ(c) = |F_ℓ(c)|/ℓ`, `p̄_ℓ = |R|⁻¹ Σ_{c∈R} p_ℓ(c)`, and
`μ̄ = Σ_ℓ p̄_ℓ`.

A family of congruence conditions "n ≡ b (mod q₀ℓ)" with `q₀ | Q₀`, `ℓ ∈ 𝒫`
induces such a system, with `F_ℓ(c) = {b mod ℓ : b ≡ c (mod q₀)}`. Every atom
family of the 2/3 and 3/4 notes is of this form (§4).

**Majorant of level λ.** A finite real combination
`ν(n) = Σ_i a_i 1[n ≡ b_i (mod d_i)]` with:
* `ν ≥ 0` everywhere;
* `ν ≥ 1` on `𝒜`;
* the level condition `Σ_{ℓ∈𝒫, ℓ | d_i} log ℓ ≤ λ` for every i.

The level condition is implied by `d_i ≤ e^λ`, and it charges *only* the
slice primes. The small part of `d_i` is free, which is generous to the
architecture.

`Eν` is the mean over a common period, `Σ a_i/d_i`. For every N one has
`Σ_{n≤N} ν(n) = N·Eν + O(Σ|a_i|)`. Any bound for `#(𝒜∩[1,N])` that goes
through ν is therefore ≥ `N·Eν − O(Σ|a_i|)`. The *saving* of ν is
`log(1/Eν)`.

---

## 2. The sieve-limit theorem

### 2.1 Two one-dimensional lemmas

**Lemma 2.1 (binomial pmf; PROVED).** Let `ψ = Bin(z,q)` with `0<q≤1/4` and
`μ' = zq`. For every integer `1 ≤ y ≤ z−1`,
`ψ(y) ≥ (8y)^{−1/2} exp{−(4/3)(y−μ')²/μ'}`.

*Proof.* MacWilliams–Sloane (Ch. 10, Lemma 7) gives
`C(z,y) ≥ (8y(1−y/z))^{−1/2} e^{zH(y/z)}`. Hence
`ψ(y) ≥ (8y)^{−1/2} e^{−zD(y/z‖q)}`.

The bound `D ≤ χ² = (a−q)²/(q(1−q))` gives
`zD ≤ (y−μ')²/(μ'(1−q)) ≤ (4/3)(y−μ')²/μ'`. ∎

**Lemma 2.2 (node lemma; PROVED).** Keep ψ, q, μ' as in Lemma 2.1. For a set Y
of k+1 distinct integers in `[0,z]`, define
`B(Y) = max_{y∈Y} |ℓ^Y_y(0)|/ψ(y)`. Here `ℓ^Y_y` is the Lagrange basis
polynomial of Y. For every polynomial `P` of degree ≤ k with `P ≥ 0` on Y,

    |P(0)| ≤ B(Y) · Σ_{y∈Y} ψ(y) P(y).                              (2.1)

Let `B(k) = min_Y B(Y)`, with C₁ = 16e⁶. Then:

* (a) `log B(0) ≤ ½log(8μ'+8) + 2`;
* (b) `log B(k) ≤ 4log(4/3)·μ' ≤ 1.151·μ'` for every `k ≤ z`;
* (c) if `μ' ≥ 64` and `1 ≤ k ≤ μ'/16`, then
  `log B(k) ≤ (k/2)·log(C₁μ'/k) + ½log(16μ')`.

Consequently, for every `α, s > 0` and every `0 ≤ k ≤ z`,

    log B(k) ≤ 19αks + C₄ μ' e^{−2αs} + ½log(16μ'+16) + 74,   C₄ = 8e⁵.   (2.2)

*Proof.* (2.1) is Lagrange interpolation, `P(0) = Σ_y ℓ_y(0)P(y)`, together
with `P(y) ≥ 0` on Y.

(a) If μ' ≥ 1, take the single node `y = ⌈μ'⌉ ≤ z−1` and apply Lemma 2.1 with
`|y−μ'| ≤ 1`. If μ' < 1, take the node 0. Then
`ψ(0) = (1−q)^z ≥ e^{−1.151μ'}`.

(b) Take `Y = {0,…,k}`. Then `ℓ_y(0) = δ_{y0}`, so `B = 1/ψ(0) ≤ e^{1.151μ'}`.

(c) Take nodes `y_i = a + ih` (0 ≤ i ≤ k), with:
* `W = ⌈√(kμ')/2⌉`;
* `h = ⌈2W/k⌉`;
* `a = ⌈μ'⌉ − W`.

Using k ≤ μ'/16 and μ' ≥ 64:
* every node lies in `[μ'/2, 2μ'] ⊆ [1, z−1]`;
* `|y_i − μ'| ≤ W+k+1 ≤ √(kμ')`.

Lemma 2.1 then gives `ψ(y_i) ≥ (16μ')^{−1/2} e^{−4k/3}`.

Next, `|ℓ_i(0)| = Π_{j≠i} y_j/(h^k i!(k−i)!)`. Using
* `Π_{j≠i} y_j ≤ (2μ')^k`,
* `k!/(i!(k−i)!) ≤ 2^k`,
* `k! ≥ (k/e)^k`,
* `h ≥ √(μ'/k)`,

we get `|ℓ_i(0)| ≤ (4e√(μ'/k))^k`. Multiplying the two bounds gives (c),
with `16e^{2+8/3} ≤ C₁`.

For (2.2): when (c) applies, use
`(k/2)log(C₁μ'/k) ≤ αks + (C₁μ'/2e)e^{−2αs}`. This is the maximum over real k
of the difference, attained at `k = C₁μ'e^{−1−2αs}`. Otherwise use (a) or (b):
* if μ' < 64, then `1.151μ' ≤ 74`;
* if k > μ'/16 and αs ≥ 1, then `1.151μ' ≤ 18.5k ≤ 19αks`;
* if αs < 1, then `1.151μ' ≤ 8.6μ'e^{−2αs}`. ∎

`scripts/theta_sieve_limit.py` re-checks (c) on 99 binomial cases and the
Rankin step on a grid. Both have zero violations.

`scripts/theta_reduction_check.py` tests Steps 2–3 of Proposition 2.4 below
(thinning and symmetrisation) by exact LP on 40 random non-exchangeable
instances (n ≤ 7, m ≤ 3). The full minimum `W(p,m)` is always at least the
reduced quantity `E_w W_ex(|Z|, max p, m)`. The minimum gap is −3·10⁻¹⁶,
which is rounding error; equality holds for m = 1.

### 2.2 Interpolation on lower sets

**Lemma 2.3 (combination technique; PROVED; standard).** Let `Λ ⊂ ℤ_{≥0}^G` be
a lower set. Let `P_Λ` be the span of the monomials `x^a`, `a ∈ Λ`. For each
coordinate g and degree k, let `I^{(g)}_k` be Lagrange interpolation at any
k+1 distinct nodes `Y^{(g)}_k`. Put

    c_j = Σ_{e∈{0,1}^G, j+e∈Λ} (−1)^{|e|}.

Then for `Q ∈ P_Λ`,

    Q = Σ_{j∈Λ} c_j (⊗_g I^{(g)}_{j_g}) Q,   with |c_j| ≤ 2^G.

*Proof.* Put `Δ_k = I_k − I_{k−1}` (with `I_{−1} = 0`). Expanding
`Σ_{j∈Λ} ⊗_g Δ_{j_g}` gives the displayed `c_j`.

For `x^a` with `a ∈ Λ`, `Δ_{j_g} x_g^{a_g} = 0` whenever `j_g > a_g`. The box
`{j ≤ a}` lies in Λ, so the sum is `Π_g Σ_{j_g≤a_g} Δ_{j_g} x_g^{a_g} = x^a`.
No nestedness of the node sets is needed. ∎

### 2.3 The Boolean proposition

Take independent `x_i ~ Bern(p_i)` (i ∈ I) with weights `s_i ≥ s_* > 0`. A
function `f` on `{0,1}^I` is *λ-level* if `f = Σ_T f_T`, where each `f_T`
depends only on `x_T` and `Σ_{i∈T} s_i ≤ λ`.

**Proposition 2.4 (PROVED).** Assume `p_i ≤ 1/4` for every i. Let f be
λ-level with `f ≥ 0` and `f(0) ≥ 1`. Put `G = ⌊log₂(λ/s_*)⌋ + 1` and
`μ = Σ_{s_i≤λ} p_i`. Then for every α > 0,

    log(1/E f) ≤ 19αλ + C₄ Σ_{i: s_i≤λ} p_i e^{−α s_i}
                 + G·(75 + log(2+λ/s_*)) + (G/2)·log(16μ+16).        (2.3)

*Proof.*

*Step 0 (top coordinates are invisible).* A term `f_T` cannot contain any i
with `s_i > λ`. So f ignores those coordinates, and we discard them.

*Step 1 (bands).* Put `B_g = {i : 2^g s_* ≤ s_i < 2^{g+1}s_*}` for
`0 ≤ g < G`, `s_g = 2^g s_*` and `q_g = max_{i∈B_g} p_i ≤ 1/4`.

*Step 2 (thinning).* Take independent `u_i ~ Bern(q_g)` and
`w_i ~ Bern(p_i/q_g)`. Then `x_i := u_i w_i` has exactly the law of x.

Fix w, and let `Z_g = {i∈B_g : w_i = 1}` and `z_g = |Z_g|`. The function
`f_w(u) := f(u∘w)` depends only on `u_Z`. It is λ-level, nonnegative, and
satisfies `f_w(0) ≥ 1`.

*Step 3 (symmetrisation).* Average `f_w` over `Π_g Sym(Z_g)`; the law of u is
invariant under this group. Expand each term multilinearly. Every monomial
`u^S` with `S ⊆ T` has multidegree `(|S∩Z_g|)_g` in the lower set

    Λ = {j : Σ_g j_g s_g ≤ λ},

since `s_i ≥ s_g` on `B_g`. Symmetrising `u^S` gives
`Π_g C(K_g,|S_g|)/C(z_g,|S_g|)`, where `K_g = |u_{Z_g}|`.

Hence `E_u f_w = E Q(K)`, where:
* `Q ∈ P_Λ`;
* the `K_g ~ Bin(z_g, q_g)` are independent;
* `Q ≥ 0` on `Π_g{0..z_g}`;
* `Q(0) ≥ 1`.

Reducing with `Π_{i=0}^{z_g}(K_g−i) = 0` on the support, we may assume
`Q ∈ P_{Λ'}` with `Λ' = Λ ∩ Π[0,z_g]`, which is still a lower set.

*Step 4 (interpolation).* Choose the node sets of Lemma 2.2 inside
`{0..z_g}`, and apply Lemma 2.3 at the point 0. All grid points are support
points, where `Q ≥ 0`. This gives

    1 ≤ Q(0) ≤ Σ_{j∈Λ'} |c_j| Π_g B_g(j_g) · Σ_{y∈grid_j} ψ(y)Q(y)
             ≤ (2^G |Λ| max_{j∈Λ} Π_g B_g(j_g)) · E Q(K).

*Step 5 (bounds).* Use (2.2) for each g with `s = s_g` and `μ' = q_g z_g`,
together with:
* `Σ_g j_g s_g ≤ λ`;
* `|Λ| ≤ (1+λ/s_*)^G`.

This gives
`log(1/E_u f_w) ≤ 19αλ + Σ_g [C₄ q_g z_g e^{−2αs_g} + ½log(16q_g z_g+16) + 74]
+ G log 2 + G log(1+λ/s_*)`.

Average over w, using Jensen for exp and for log, and `E_w q_g z_g = μ_g`.
Finally `e^{−2αs_g} ≤ e^{−αs_i}` on `B_g`, and `Σ_g log(16μ_g+16) ≤ G·log(16μ+16)`. ∎

### 2.4 The CRT form

**Theorem 2.5 (sieve limit for prime-slice systems; PROVED).** Take a
prime-slice system as in §1. Assume `|F_ℓ(c)| ≤ ℓ/4` for every `c ∈ R` and
every `ℓ ∈ 𝒫` with `ℓ ≤ e^λ`. Let ν be any majorant of level λ, and put
`s_* = log min 𝒫`. Then for every α > 0,

    log(1/Eν) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_{ℓ∈𝒫, ℓ≤e^λ} p̄_ℓ ℓ^{−α}
                + G(75+log(2+λ/s_*)) + (G/2)·log(16μ̄+16).          (2.4)

*Proof.* Use uniform measure on `ℤ/Q_tot`, a common period. By CRT, the
coordinates `c = n mod Q₀*` (the Q₀-primary part), `n mod ℓ^{e_ℓ}` (ℓ∈𝒫) and
the rest are independent and uniform. We have
`Eν ≥ (|R|/Q₀) · avg_{c∈R} E[ν | c]`.

Fix `c ∈ R`. The hit indicators `x_ℓ = 1[n mod ℓ ∈ F_ℓ(c)]` are independent
`Bern(p_ℓ(c))`. Each term of ν, conditioned on `(c, x)`, depends only on
`x_{T_i}`, where `T_i = {ℓ∈𝒫 : ℓ | d_i}`. So `ν_c := E[ν | c, x]` is λ-level
with weights `s_ℓ = log ℓ`, satisfies `ν_c ≥ 0`, and has `ν_c(0) ≥ 1`
because `{c} × {x=0} ⊆ 𝒜`.

Proposition 2.4 applies fibrewise. Jensen over `c ∈ R` turns the fibre
profiles into `p̄_ℓ` and `μ̄`. ∎

**Remark 2.6 (large sieve, and what the theorem says).**

*Large sieve.* Montgomery's large sieve applied in a fibre gives
`Y/S_c(Q)` with `Q² ≤ Y`. Rankin's bound
`S_c(Q) ≤ Q^α Π_ℓ(1+g_ℓ ℓ^{−α}) ≤ exp{α log Q + 2Σ_ℓ p_ℓ(c)ℓ^{−α}}` shows
that its bound obeys the same functional directly. No duality is needed in
that case.

*Two-sided description.* The theorem is the converse of the large-sieve and
Rankin calculation. Up to absolute constants and O(log²λ), the best saving
of *any* level-λ CRT majorant on a prime-slice system is

    Ψ(λ) := inf_{α>0} [ αλ + Σ_ℓ p̄_ℓ ℓ^{−α} ].                      (2.5)

*Coordinates beyond the level.* Conditions at primes `ℓ > e^λ` contribute
nothing (Step 0).

*Relation to Assessment 75.7.* This is the rigorous "LP-duality" statement
that Assessment 75.7 of notes §75 called missing, for avoid-events of
product systems. The lower-tail version (target point x₀ instead of 0)
follows from the same proof by interpolating at the point `(κ_g)` with
`Σκ_g ≤ x₀`. It is not worked out here.

### 2.5 Sharpness in the exchangeable model (EVIDENCE)

`scripts/theta_sieve_limit.py` solves the exchangeable LP
`min{E Q(K) : deg Q ≤ m, Q ≥ 1_{0} on ℤ_{≥0}}` for `K ~ Poisson(μ)`. It uses
the dual on a truncated support, which is a rigorous lower bound, in a
Charlier basis. The Selberg value `[Σ_{j≤m/2} μ^j/j!]^{−1}` is an upper
bound on the LP optimum W, which equals the Christoffel function at 0.

| μ | m | −log Selberg | −log W (LP) | Lagrange, best nodes | Lagrange, recipe of Lemma 2.2 | claimed bound (c) |
|---:|---:|---:|---:|---:|---:|---:|
| 128 | 8 | 16.262 | 16.269 | 19.391 | 24.686 | 49.993 |
| 256 | 8 | 19.018 | 19.021 | 22.418 | 27.382 | 53.112 |
| 256 | 16 | 33.788 | 33.794 | 37.729 | 48.975 | 96.520 |
| 512 | 8 | 21.783 | 21.784 | 25.574 | 30.946 | 56.231 |

Three observations:
* The LP optimum equals the Selberg value to about 10⁻³. So the square
  majorant is essentially optimal among *all* degree-m majorants.
* The rigorous Lagrange bound is within a factor of about 1.15 (best nodes)
  or 1.45 (recipe) of the truth.
* Bonferroni of degree r has `E Q_r(H) ≥ P(H ≥ r+1)` (Lemma 4.2). It is
  useless until `r ≈ μ`, whereas Selberg already saves `(m/2)log(μ/m)` at
  degree m. This is a constant-factor difference after re-optimising t.

---

## 3. Supply profiles and the main corollary

**Lemma 3.1 (PROVED).** Put
`S_B(x) = Σ_{M≤x, M≡3(4)} τ(A²)·M/φ(M)`, where `A = (M+1)/4`. Then
`S_B(x) ≪ x(log 2x)²`. Consequently, for `0 < β ≤ 1`,
`Σ_{M≡3(4)} τ(A²)(M/φ(M)) M^{−1−β} ≤ C₆ β^{−3}`.

*Proof.* Write `M/φ(M) = Σ_{d|M} μ²(d)/φ(d)` and swap the sums. The inner sum
is over `A ≤ (x+1)/4` with `4A ≡ 1 (mod d)`.

* For `d ≤ x^{1/2}`: apply Shiu's theorem (as stated in the 3/4 note, §3) to
  the multiplicative function `F(A) = τ(A²)` (`F(p) = 3`) in the reduced
  class `4⁻¹ (mod d)`. This gives `≪ (x/φ(d))(log x)²`, and
  `Σ_d φ(d)^{−2} < ∞`.
* For `d > x^{1/2}`: bound trivially by `(x/d+1)·x^{1/10}`. The total is
  `≪ x^{0.61}`.

The β-bound follows by partial summation: `∫(log 2x)² x^{−1−β}dx ≪ β^{−3}`. ∎

Numerically, `S_B(x)/(x log²x)` equals 0.1067, 0.0990 and 0.0963 at
`x = 10², 10⁴, 10⁶` (`data/theta/profile.txt`).

**Lemma 3.2 (a-frame grouping; PROVED).** Let a, D ≥ 1 be arbitrary, and put
`g(D) = Π_p p^{⌈v_p(D)/2⌉}`. Note that `g(D) | D` and `D | g(D)²`. The class

    n ≡ −(4D+a)  (mod 4a·g(D))

is forced for n ≥ 1. Indeed, write `n+4D+a = 4a·g·j` with j ≥ 1. Then
`M := (n+4D)/a = 4gj−1` is ≡ 3 (mod 4), and `(M+1)/4 = gj`, so
`D | g² | A_M²` and `n ≡ −4D (mod M)`. Hence n lies in a class of ℛ(M),
which is forced by Lemmas 16.1 and 18.1.

Every Case-B witness (q, d) of Theorem 3.1(B) lies in the class with a = q,
D = d. To see this:
* `D | x²` is equivalent to `g(D) | x`;
* `q | d+x` gives `p+a ≡ −4D (mod 4a)`;
* `gcd(q, x) = 1` gives `gcd(a, g) = 1`.

So the (a,D) family is the *exact criterion* `D | x², D ≡ −x (mod a)` of
notes §§61–62, written as congruences.

Its profile is
`Σ_{a,D} (G/φ(G)) G^{−1−β} ≪ (Σ_a a^{−1−β} a/φ(a)) · (Σ_g 2^{ω(g)}(g/φ(g)) g^{−1−β}) ≪ β^{−1}·β^{−2}`,
with `G = 4a·g(D)`. This uses `#{D: g(D)=g} ≤ 2^{ω(g)}`. ∎

**Case A (the mirror half).** Case A of Theorem 3.1 reduces to the forced
classes `n ≡ −m^{−1} (mod 4g(d))` with `m | 4d+1`. The reason is that
`m | d+z₀` is equivalent to `m | 4d+1`, and `d | z₀²` is equivalent to
`nm ≡ −1 (mod 4g(d))`. This reduction is PROVED.

Its exact union mass up to `x = 10², 10³, 4000` is 0.0280, 0.0257 and 0.0254
times `(log x)³`. That is EVIDENCE that this profile is also cubic. A proof
(of a bound `Σ_{rh≤x} τ(4rh²+1) ≪ x log²x`) is not written out. Case-A
families are therefore covered by Cor 3.4 only under this numerically
supported bound (named **H_A3**). No existing proof uses Case A.

**Corollary 3.4 (the 3/4 ceiling for prime-slice forced-class architectures;
PROVED).** Fix `0 < C < 1` and `A ≥ 1`. Take a prime-slice system whose
conditions are forced classes of Lemma 16.1 (any multiplier grouping) or of
Lemma 3.2, with:
* each condition modulus `q₀ℓ` satisfying `q₀ ≤ ℓ^C`;
* `R = {c : (c,P)=1}` for some `P | Q₀`;
* `ℓ ≥ ℓ₀(C)`.

Then every majorant of level `λ ≤ A·log N` satisfies

    log(1/Eν) ≤ C₇(A,C) (log N)^{3/4} + log(Q₀/|R|).

The same bound holds for the large-sieve bound of Remark 2.6. In particular
no such architecture gives `E(N) ≤ N exp{−(log N)^{3/4}·ω(N)}` with
`ω → ∞`. A factor `(log log N)^ε` is excluded as well.

*Proof.* Three checks.
* Since `q₀ ≤ ℓ^C` and `|ℛ(M)| ≤ M^{o(1)}`, we have
  `|F_ℓ(c)| ≤ ℓ^{C+o(1)} ≤ ℓ/4`.
* For the selector-type R, `P(c ≡ b (q₀) | R) ≤ (q₀/φ(q₀))/q₀`. Hence
  `p̄_ℓ ≤ Σ_{M=q₀ℓ} |ℛ(M)|(M/φ(M))/M`.
* `ℓ ≥ M^{1/(1+C)}` gives `ℓ^{−α} ≤ M^{−α/2}`.

Lemmas 3.1 and 3.2 give `Σ p̄_ℓ ℓ^{−α} ≪ α^{−3}`. Take `α = λ^{−1/4}` in
(2.4). Here `G = O(log λ)` and `μ̄ ≪ λ³`. ∎

In practice `log(Q₀/|R|)` is `log log y` for the selector, which is
negligible. It is at most `log N` in general, and it is a *loss* for the
method, not a gain.

**Corollary 3.5 (restricted multiplier sets; PROVED given the cited upper
bounds).** Suppose a family at scale `X = e^t` uses slice primes
ℓ ∈ (X^{1/2}, X] and multipliers k ∈ 𝒦, with
`Σ_ℓ p_ℓ(c) ≤ A₀ t² h(𝒦)` for all c. This is the Brun–Titchmarsh upper half
of the mass lemmas in both notes; here `h(𝒦) = Σ_{k∈𝒦} φ(k)/k²`.

Then (2.4) with `Σ_ℓ p̄_ℓ ℓ^{−α} ≤ A₀t²h·e^{−αt/2}` gives

    saving ≤ min{ C t²h , (38λ/t)(1 + log⁺(C t³h/λ)) } + O(log²λ).

Put `t₀ = (λ/h)^{1/3}`. For t ≤ t₀ the first entry is at most
`Cλ^{2/3}h^{1/3}`. For `t = u·t₀ ≥ t₀` the second entry is at most
`Cλ^{2/3}h^{1/3}(1+3log u)/u`. Hence the supremum over t is
`≍ λ^{2/3}h^{1/3}`, where h may depend on t.

* LL note: `𝒦 = {k ≤ δ log N}`, `h ≍ log L`, giving
  `L^{2/3}(log L)^{1/3}`. **The 2/3 note is sharp for its architecture.**
* Any 𝒦 with `lcm(𝒦) ≤ N` has `h(𝒦) ≤ Π_{p|lcm}(1+1/p) ≪ log L`, so the
  same cap holds.
* 3/4 note: `h ≍ κt`, giving `λ^{3/4}`.

---

## 4. Exact accounting of the two campaign proofs

Notation: `μ_c` is the fibre mass and `r` the Bonferroni degree.

**Lemma 4.1 (3/4 note: what binds; PROVED).** The atom family `𝒜_X` of the
3/4 note is a prime-slice system with:
* `Q₀ = lcm(L_K, P_y)`;
* `𝒫 = primes in (X^{1/2}, X]`;
* `R = {(c,P_y)=1}`;
* `|F_ℓ(c)| = f_c(ℓ) ≤ ℓ^{1/3}`;
* `Σ_ℓ p_ℓ(c) ℓ^{−α} ≤ C_u t³ X^{−α/2}` (note, Cor. 3.6, upper half).

Its majorant `S_y·Q_r(H_X)` has level `λ = r·t`.

By Theorem 2.5, *every* majorant on this family has
`saving ≤ min{C t³, C(λ/t)log(Ct⁴/λ) + Cλ/t} + O(log²λ)`. With `λ ≤ A L`,
the maximum over t is `≍ L^{3/4}`, attained only for `t ≍ L^{1/4}`.

So the binding constraint in the 3/4 proof is the following conjunction. It is
not Bonferroni depth, the BV level or the selector.

    (supply)  μ_c ≤ C_u t³ uniformly        and      (level)  λ ≤ A·log N.

**Lemma 4.2 (Bonferroni depth; PROVED).** For `Q_r(h) = Σ_{j≤r}(−1)^j C(h,j)`
(r even) and any integer `H ≥ 0`, `E Q_r(H) ≥ P(H ≥ r+1)`.

If H is a sum of independent Bernoulli variables with mean μ, then
`r+1 ≤ μ − 2√μ` implies `E Q_r ≥ 3/4`. Bonferroni therefore saves nothing
below depth `μ − 2√μ`.

*Proof.* `Q_r(h) = C(h−1,r) ≥ 1` for `h ≥ r+1`, and `Var H ≤ μ`, so
Chebyshev applies. ∎

So in the 3/4 note `r ≍ t³` is forced. The ledger `log T_abs ≍ r·t` then
forces `t⁴ ≲ L`. Replacing Bonferroni by the optimal majorant (Selberg, §2.5)
changes only constants, by Lemma 4.1.

**Lemma 4.3 (level of distribution; PROVED).** The BV level ϑ enters the
3/4 proof only through `z = x^{ϑ'}` in the supply lemma, and
`μ_c ≍_ϑ' t³` for every fixed `0 < ϑ' < 1/2`. Elliott–Halberstam
(`ϑ' → 1/2`) multiplies `μ_c` by a bounded factor. The integer assembly uses
exact counts `N/q + O(1)` and no level of distribution.

*Proof.* The block mass is `≍ (log z)² h = ϑ'² t² h` (Theorem 5.2 of the note
with z replaced). ∎

**Lemma 4.4 (2/3-loglog note: what binds; PROVED).** The note:
* splits into progressions mod `L_K`, with `log L_K ≈ K ≤ δL`;
* applies Montgomery's sieve with `Q² ≤ N/L_K`;
* has `μ_c ≤ A t² h(K)` with `h(K) ≍ log K ≤ log L`.

By Remark 2.6 and Cor 3.5, its bound cannot exceed
`exp{−C L^{2/3}(log L)^{1/3}}`. The binding inequality is
`h(𝒦) ≤ Π_{p | L_𝒦}(1+1/p) ≪ log log L_𝒦` (the note's own closing remark),
combined with the requirement `L_𝒦 ≤ N`. Vaughan/PW is the case `𝒦 = {1}`,
giving `L^{2/3}`. ∎

**Binding table.**

| proof | supply profile | level | binding | non-binding (constants only) |
|---|---|---|---|---|
| Vaughan/PW | `t²` per slice scale (k=1) | `Q² ≤ N` | profile + level → 2/3 | BV level, Rankin-tail constant |
| LL 2/3-loglog | `t² log K`, `L_K ≤ N` | `Q² ≤ N/L_K` | `h ≤ log log L_K` | the progression split itself (costs a constant) |
| 3/4 note | `t³` (`log K = κt`) | `r t ≲ L` | profile + level → 3/4 | Bonferroni depth, BV level, selector, pruning (§76) |

---

## 5. The levers

### 5.0 Lever table

| lever (brief) | outcome | where |
|---|---|---|
| cost per condition below log X; weighting moduli by mass; `ΣF(M)/M·log M ≍ t⁴` vs `t³` | **closed** (Thm 2.5 + Lemma 3.1): mixing scales optimally is exactly the Rankin functional (2.5); the identity profile gives `λ^{3/4}` | §5.1 |
| Rankin/Halász on `x=(p+a)/4` | **closed as a lever beyond 3/4** (explicit non-multiplicativity counterexample, PROVED; joint route = stacking, Assessment θ* ≈ 0.52) | §5.2 |
| beyond-identity supply / exact criterion `−1∈Rat_a(h)` / large deviations of class counts | **closed** for prime-slice systems (Lemma 3.2: the criterion *is* the (a,D) forced classes; Lemma 5.3: effective mass = mass); complete system: EVIDENCE of sub-additivity (ratio ≈ 0.80) | §5.3 |
| combining both halves / both solution types | **closed** (union profile ≤ sum; Theorem 2.5 needs no independence between halves; constants only) | §5.4 |
| Elsholtz–Tao average as first-moment limit | **consistent**; the correct currency is the profile `Σp̄ℓ^{−α}`, which is exactly cubic (no loglog) | §5.5 |
| multi-slice moduli; multipliers ≫ slice prime | **open** (outside Theorem 2.5); hypothesis H_MS named; mass-cost Assessment predicts closure | §5.6 |
| Bonferroni → Selberg/large sieve | constants only (Lemma 4.2, §2.5 numerics) | §4 |

### 5.1 Truncation cost per condition

In Theorem 2.5 a condition at ℓ costs `log ℓ` of level, *whatever its mass*.
Several classes at the same ℓ cost one `log ℓ` jointly, yet in the dual they
count with their summed mass `p_ℓ`. Weighting the moduli by mass density is
exactly the choice of α in (2.5).

For the identity supply, mass up to cost s is `≍ s³` (Theorem 18.2). The
cost-weighted mass is `Σ F(M)/M·log M ≍ s⁴` (the brief's `t⁴` vs `t³`).
Spending level on the cheapest mass first is the optimisation
`max{mass(S) : Σ_{S} p·log ℓ ≤ λ}`. With mass `c·s³` up to cost s, this gives
`c^{1/4}(4λ/3)^{3/4}`. That optimisation is a heuristic; Theorem 2.5 shows
that no majorant beats this order.

Conditions whose cost is below their mass (`p_ℓ > 1/log ℓ`) exist only at
bounded ℓ. They contribute O(1) in total.

### 5.2 Rankin/Halász on the shifted integers

**Lemma 5.1 (non-multiplicativity; PROVED by example).** For a modulus a, put
`Ω_a(x) = {D mod a : D | x²}`. The set map is multiplicative,
`Ω_a(x₁x₂) = Ω_a(x₁)Ω_a(x₂)` for coprime arguments, but the failure
indicator `1[−x ∉ Ω_a(x)]` is not.

Example with a = 7:
* `Ω(2) = {1,2,4}` does not contain −2 ≡ 5, so x = 2 fails;
* `Ω(3) = {1,3,2}` does not contain −3 ≡ 4, so x = 3 fails;
* `Ω(6) = {1,2,4}·{1,3,2} ∋ 1 ≡ −6`, so x = 6 succeeds. ∎

The multiplicative pieces are the confinement slices: "all prime factors of x
lie in a subgroup H". The F1/F3 decomposition is Corollaries 70.2–70.4.

* A Rankin/Halász majorant per shift saves at most `(½+o(1))log log N` (F1)
  for fixed a. This is Theorem 70.5's `C_a/√log H` scale.
* For `a ≈ (log N)^c` it saves at most the budget large deviation
  `Q(c/log 3)·log log N`, with `Q(u) = 1−u+u log u`. This is §14.4,
  Assessment 75.5.

Joint control of J shifts is then a product of multiplicative functions of J
shifted values. That is exactly hypothesis H_STACK (§71.3), whose sieve
evaluation needs `log z ≲ L/(J log J)`.

Optimising J with the budget threshold reproduces the entropy supremum
`θ* = log3/(1+log3) = 0.5235`. The derivation: the per-shift lower tail needs
`0.91c < 1−θ`, with `J ≈ L^c`, giving `c < 0.52`. This is (D)1 again,
**Assessment**, and it lies below 3/4.

One structural observation, Assessment only. Joint F1 over many a forces p
into a fixed half of the residues modulo every prime `q ≲ A`, which is a
larger-sieve configuration. But F1 dominates F3 only for `a ≲ L^{0.21}`, so
this gains only `L^{0.2+o(1)}`.

### 5.3 Beyond-identity supply and effective mass

**(i) The exact criterion adds no CRT supply (PROVED).** By Lemma 3.2,
`{p : −1 ∈ Rat_a(x_a)}` is the union over D of the (a,D)-classes. So the CRT
void of the exact criterion *equals* the forced-class void of the (a,D)
family. Its profile is cubic (Lemma 3.2). "Failure probability per modulus
not captured by forced classes" does not exist at CRT level. It exists only
in the integer arithmetic of `x_a`, which is §5.2's route.

**(ii) Effective mass equals mass in a slice fibre (Lemma 5.3, PROVED).** In
a prime-slice fibre,
`−log P(void | c) = Σ_ℓ −log(1−p_ℓ(c)) ≤ (1+2 max p) μ_c`.

Averaged over fibres, Jensen gives `P(void) ≥ P(R)·e^{−(1+o(1))μ̄}`. A large
deviation of the class-count vector cannot raise the void rate above the
first moment: the count is a sum of independent Bernoulli variables. With
level, Theorem 2.5 caps any majorant.

**(iii) Complete system with real primes (hypothesis H_EM; EVIDENCE).**

> **H_EM**: for the complete multiplier-identity system with moduli ≤ Q, among primes,
> `−log P(void) ≤ C·μ_pr(Q)` with `μ_pr(Q) = Σ_{M≤Q}|ℛ(M)∩units|/φ(M)`.
> (Falsifiable: a ratio growing without bound would refute it.)

This was tested on all 4,045,501,204 primes in
`[10¹², 10¹² + 1.12·10¹¹)` (`scripts/theta_void_primes.cpp`,
`data/theta/void_primes_Q4000.txt`):

| Q | void fraction | μ_pr(Q) | −log void / μ_pr |
|---:|---:|---:|---:|
| 10 | 2.50e−1 | 1.00 | 1.386 |
| 80 | 7.22e−3 | 4.79 | 1.030 |
| 405 | 9.10e−5 | 10.52 | 0.885 |
| 1368 | 8.49e−7 | 17.04 | 0.820 |
| 3078 | 1.61e−8 | 22.56 | 0.796 |
| 4000 | 2.47e−9 (10 primes) | 24.60 | 0.806 |

The ratio falls and levels off near 0.8. The small-M excess (> 1) is
`−log(1−p) > p` at M = 3, 7. Beyond that the classes *clump*: the void is
larger than `e^{−mass}`. This is consistent with Theorem 31.4's `e^{−o(L³)}`
lower bound for all integers. No super-cubic effective mass is visible. The
data are consistent with H_EM and give no sign against it.

### 5.4 Both halves, both types

Theorem 2.5 takes any family of conditions. The union of Case-B classes
(either grouping) and Case-A classes has profile at most the sum, which is
cubic (Lemmas 3.1, 3.2 and H_A3). So the shared quadratic bit (DISCOVERIES
(C)6) is irrelevant to the cap: dependence can only lower the effective
mass. No independence between halves is used anywhere in §§2–3.

### 5.5 The Elsholtz–Tao first moment

ET's Theorem 1.1 gives `Σ_{p≤N} f_II(p) ≍ N log²N`, with no loglog, and
`N log²N ≪ Σ_{p≤N} f_I(p) ≪ N log²N log log N`. The loglog appears only in
the Type-I upper bound, and ET conjecture it is an artifact of
Brun–Titchmarsh. So the mean solution count per prime is `≍ (log p)³`, up to
that factor.

A cap driven by the first moment needs the *profile*, i.e. the mass weighted
by `ℓ^{−α}`. Lemmas 3.1–3.2 show the Case-B profile is `≍ α^{−3}`, with no
`log(1/α)`. This matches ET's Type-II order. The ET average is therefore
consistent with B = 3 and offers no extra loglog to harvest.

ET Theorem 1.8 also shows a typical prime has `f(p) ≥ (log p)^{0.549}`,
while the mean is `(log p)³`. The solution count is heavily skewed, which is
consistent with the clumping ratio ≈ 0.8 of §5.3(iii). Clumping can only
enlarge voids.

### 5.6 The open door: multi-slice moduli and large multipliers

Theorem 2.5 needs each condition to touch exactly one free large prime. Two
kinds of condition fall outside it.

* (a) Moduli with ≥2 prime factors at comparable large scales. They carry a
  positive proportion of the cubic supply, which is a Dickman-type fraction.
* (b) Prime-slice conditions with small part `q₀ ≫ ℓ`.

In (b), Theorem 2.5's free conditioning on `c` leaves the k-part
uncharged. The resulting bound `λ^{2/3}(log K)^{1/3}` exceeds `λ^{3/4}` only
if `log K ≫ λ^{1/4}`, i.e. multipliers far larger than the slice primes. For
`K ≫ z²` the lattice equidistribution behind the 3/4 supply also fails:
`(u,v)`-boxes of size `z² < k` no longer equidistribute mod k, so `μ_c` stops
being uniform in c. Any concrete majorant pays `lcm(k_i) ≥ K^{r(1−o(1))}`
(Bonferroni/Selberg) or one `L_𝒦 ≤ N` (progression split, Cor 3.5).

> **H_MS (named, open, falsifiable in models).** For every CRT system of forced classes
> with moduli ≤ e^λ (no slice restriction), every level-λ majorant has
> `log(1/Eν) ≤ C·inf_α[αλ + Σ_cond P(cond)·(mod cond)^{−α}] + O(log²λ)`.

**Assessment 5.4.** H_MS is what the mass-cost model predicts. Theorem 2.5 is
its single-slice case. A proof needs a dual measure for AND-events of shared
coordinates. Thinning and symmetrisation do not apply, because the hit
variables of conditions sharing a prime are dependent. Under H_MS, every
CRT-majorant architecture for ES is capped at `(log N)^{3/4}`. Without it, a
θ > 3/4 attempt *must* exploit joint multi-prime moduli or multiplier-sharing.
§5.3(iii) gives no sign that the complete system does better than its mass.

---

## 6. What a θ > 3/4 proof must contain

These are consequences of Theorem 2.5 and Lemmas 3.1–3.2, Lemma 5.3 and 4.2.
1. It cannot be a sieve or large sieve over prime-slice forced classes with
   multipliers `≤ ℓ^{C}`, at any level `N^{O(1)}`, with any weights
   (Cor 3.4).
2. Using both halves, both groupings, the exact a-frame criterion,
   Elliott–Halberstam, or a better Bonferroni/Selberg polynomial changes
   constants only (§§4, 5.3–5.4).
3. It needs one of:
   * (i) a joint use of multi-large-prime moduli that beats their mass
     (H_MS false in the relevant regime);
   * (ii) multipliers larger than the slice primes, with lcm cost below
     `r log K` per term;
   * (iii) non-CRT arithmetic of the integers (Halász/Type I–II/moment
     methods). §5.2 indicates (iii) via multiplicative slices sits at θ*.

---

## 7. Replay

```
# §2: Lemma 2.2(c) grid, Rankin step, LP vs Selberg vs Lagrange table (~2 min)
uv run --with scipy python scripts/theta_sieve_limit.py
# §2: reduction steps (thinning + symmetrisation) by brute-force LP (~1 min)
uv run --with scipy python scripts/theta_reduction_check.py
# §3: S_B(x)/(x log^2 x) to 1e6; exact union masses of B-M, B-aD, Case A to 4000 (~3 s)
uv run python scripts/theta_profile.py 1000000          # -> data/theta/profile.txt
# §5.3: complete-system void among real primes (4 processes x ~150 s, < 100 MB each)
g++ -O2 -std=c++17 -o /tmp/theta_void_primes scripts/theta_void_primes.cpp
for i in 0 1 2 3; do /tmp/theta_void_primes 4000 $((10**12 + i*28000000000)) 28000000000 > /tmp/theta/void_$i.txt & done; wait
# merge: sum the 'voids' column and the prime counts (see data/theta/void_primes_Q4000.txt header)
```
