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
| Thm 2.5 | **Sieve-limit theorem.** Take a *prime-slice* CRT system: the conditions are independent across large primes ℓ once a small residue c is fixed. Every nonnegative majorant of level λ of its avoider set has mean ≥ `(|R|/Q₀)·exp{−19αλ − C₄ Σ_ℓ p̄_ℓ ℓ^{−α} − O(log²λ)}`, for every α>0. Here λ charges only the slice primes. | PROVED |
| Cor 3.4 | Take any family of Case-B forced classes (both groupings) that are all slice conditions, with small parts k ≤ ℓ^C (C<1) and a selector admissible set. Every majorant of level `N^A`, and every Montgomery large-sieve bound, saves at most `C(A)(log N)^{3/4} + log(P/φ(P))`, where the last term is O(log log log P). So **3/4 is sharp for this class, and no power of log log N can be gained.** This assumes the final bound has the form `N·Eν + (nonnegative rounding bound)`. | PROVED |
| Thm 2.7, Cor 3.6 | **Sequential extension.** For nonnegative CRT majorants (no large-sieve claim), the cap `C(A,C)(log N)^{3/4} + O_C(1)` holds for every Case-B forced-class family whose moduli all have a dominant prime `P(M) ≥ M^{1/(1+C)}` (C<1). The other prime factors are arbitrary (higher powers allowed) and may be shared between conditions. By Dickman, this is a positive proportion `log(1+C)` of unweighted moduli; the weighted share of the supply is conjectural. | PROVED |
| Cor 3.5 | Polylogarithmic multipliers, or multipliers whose lcm is at most N (the 2/3 note's architecture), cap the saving at `C L^{2/3}(log L)^{1/3}`. **The 2/3-loglog note is sharp for its architecture.** | PROVED (given the notes' BT upper bounds) |
| §4 | Exact accounting. In both proofs the binding constraint is the pair (supply profile, level). Bonferroni depth, the BV level and the selector are not binding: they change constants only. | PROVED (Lemmas 4.1–4.4) |
| §5 | Levers, inside the prime-slice class. Cost-per-condition, beyond-identity supply (Case B), both Case-B groupings and Bonferroni→Selberg are closed by proved statements. Adding Case A is closed conditional on H_A3. Halász has a proved non-multiplicativity counterexample, but its joint route is only a model Assessment (θ* ≈ 0.52), not a closure. The ET first moment is consistent with B = 3. Open: balanced moduli (no dominant prime), multipliers larger than the slice prime, and non-selector small-modulus subsystems (H_MS). | see table §5.0 |
| §5.3 | Complete-system void among 4.05·10⁹ real primes near 10¹². The effective mass −log P(void) falls from 1.39 to about 0.80 of the first-moment mass as Q grows to 4000. There is no super-cubic effect. | EVIDENCE |
| §2.5 | Exchangeable Poisson model, tested cases. The numerically computed LP optimum (uncertified floating point) agrees with the Selberg square-majorant value 1/Σ_{j≤m/2} μ^j/j! to within 0.01 in −log. So Selberg Λ² is near-optimal there, and Bonferroni loses only a constant factor. | EVIDENCE |

**Verdict.** No route to θ > 3/4 survives inside the *dominant-prime* CRT
world. That world is: every condition's modulus has a prime factor
`≥ M^{1/(1+C)}`, the admissible set has bounded saving, and the final bound
has the form `N·Eν + (nonnegative rounding bound)`. It contains the
prime-slice world of Cor 3.4.

The Rankin functional `Ψ = inf_α[αλ + Σ p̄_ℓ ℓ^{−α}]` bounds what any such
sieve can save (Theorem 2.5). For the specific families of both campaign
notes, at their parameters, the notes' achieved savings match this cap up to
constants (§4). No general converse is claimed. The Case-B identity profile satisfies
`Σ p̄_ℓ ℓ^{−α} ≪ α^{−3}` (Lemmas 3.1–3.2), which gives λ^{3/4}.

Beating 3/4 requires one of the following:
1. conditions whose modulus is **balanced** (two or more large prime
   factors at comparable scales, no dominant prime), used *jointly*.
   Theorems 2.5 and 2.7 do not cover these (hypothesis H_MS, §5.6);
2. multipliers far larger than the slice prime, without per-condition lcm
   cost (§5.6);
3. a small-modulus admissible set with a large saving of its own;
4. a non-CRT ingredient: arithmetic of the actual integers beyond residue
   counting, or signed cancellation in rounding errors.

The full list is in §6. The a-frame and multiplicative route (§5.2) is of
type 4. Under its model it sits at θ* ≈ 0.52 < 3/4, which is an Assessment,
not a theorem.

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

**Proposition 2.4 (PROVED).** Assume `p_i ≤ 1/4` for every i with
`s_i ≤ λ`, and `p_i < 1` for every i. Let f be λ-level with `f ≥ 0` and
`f(0) ≥ 1`. Assume `λ ≥ s_*`, and put `G = ⌊log₂(λ/s_*)⌋ + 1` and
`μ = Σ_{s_i≤λ} p_i`. Then for every α > 0,

    log(1/E f) ≤ 19αλ + C₄ Σ_{i: s_i≤λ} p_i e^{−α s_i}
                 + G·(75 + log(2+λ/s_*)) + (G/2)·log(16μ+16).        (2.3)

If λ < s_*, f is constant, so E f = f(0) ≥ 1.

*Proof.*

*Step 0 (top coordinates are invisible).* A term `f_T` cannot contain any i
with `s_i > λ`. So f ignores those coordinates, and we discard them, as well
as coordinates with `p_i = 0` (f's restriction to `x_i = 0` is still λ-level)
and empty bands. All sets below are finite, and Λ is a finite lower set.

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
             ≤ (2^G |Λ'| max_{j∈Λ'} Π_g B_g(j_g)) · E Q(K).

If `z_g = 0`, then `K_g ≡ 0`, `j_g = 0` on Λ', and `B_g(0) = 1` (node 0).

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
prime-slice system as in §1. Assume that for every `c ∈ R`:
* `|F_ℓ(c)| ≤ ℓ/4` for every `ℓ ∈ 𝒫` with `ℓ ≤ e^λ`;
* `|F_ℓ(c)| < ℓ` for every `ℓ ∈ 𝒫`, so every admissible fibre has avoiders.

Let ν be any majorant of level λ ≥ s_*, where `s_* = log min 𝒫`. (If
λ < s_*, ν depends only on the small residue and the bound below holds
without the λ-terms.) Then for every α > 0,

    log(1/Eν) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_{ℓ∈𝒫, ℓ≤e^λ} p̄_ℓ ℓ^{−α}
                + G(75+log(2+λ/s_*)) + (G/2)·log(16μ̄+16).          (2.4)

*Proof.* Use uniform measure on `ℤ/Q_tot`, a common period. By CRT, the
coordinates `n mod Q₀*` (Q₀* is the Q₀-primary part of Q_tot), `n mod ℓ^{e_ℓ}`
(ℓ∈𝒫) and the rest are independent and uniform. We condition on
`c := n mod Q₀`, which is a function of the first coordinate. We have
`Eν = Q₀⁻¹ Σ_c E[ν | c] ≥ (|R|/Q₀) · avg_{c∈R} E[ν | c]`, since ν ≥ 0.

Fix `c ∈ R`. The hit indicators `x_ℓ = 1[n mod ℓ ∈ F_ℓ(c)]` are independent
`Bern(p_ℓ(c))`, independent of the finer digits of `n mod Q₀*`. Each term of
ν, conditioned on `(c, x)`, depends only on `x_{T_i}`, where
`T_i = {ℓ∈𝒫 : ℓ | d_i}`. So `ν_c := E[ν | c, x]` is λ-level with weights
`s_ℓ = log ℓ`, and `ν_c ≥ 0`.

The event `{c} × {x=0}` has positive probability, since every `p_ℓ(c) < 1`,
and it is contained in 𝒜. So `ν_c(0) ≥ 1`.

Proposition 2.4 applies fibrewise. Jensen over `c ∈ R` turns the fibre
profiles into `p̄_ℓ` and `μ̄`. Here μ̄ may be read as the truncated mass
`Σ_{ℓ≤e^λ} p̄_ℓ`. ∎

**Two caveats on (2.4).**

*The R-term is a saving the theorem leaves uncontrolled.* `log(Q₀/|R|)` is
part of the *upper* bound on saving. For example, `ν = 1_R` is a majorant
with no slice cost and saving exactly `log(Q₀/|R|)`.

* For the selector `R = {(c,P)=1}`, this term is
  `log(P/φ(P)) ≤ log log log P + O(1)`, which is negligible.
* If R itself encodes forced classes whose moduli divide Q₀ (pure
  small-modulus conditions), this term is the CRT void of a *non-slice*
  subsystem. Theorem 2.5 says nothing about it; see H_MS, §5.6.

*Interval-counting methods.* The theorem bounds the CRT mean Eν. A method
whose final bound for `#(𝒜∩[1,N])` has the form `N·Eν + (a nonnegative bound
on the rounding term)` is therefore capped. A method that proves *signed*
cancellation among the rounding errors `Σ_{n≤N}ν(n) − N·Eν` is outside the
scope.

**Scope remark (where the theorem stops).** ν must be nonnegative on all of
ℤ. Every sieve majorant in use satisfies this: Bonferroni truncations
`Q_r(H) = C(H−1,r)` and Selberg squares. If positivity is only demanded on
[1,N], the span of level-N class indicators already contains every function
on [1,N], since `1[n ≡ b (mod N)]` restricted to [1,N] is `δ_b`. So the
relaxed LP is the exact count, and evaluating it presupposes knowing the
avoider set. Methods of that kind are "non-CRT" (§6(iii)), not sieves.

**Remark 2.6 (large sieve, and what the theorem says).**

*Large sieve.* Montgomery's large sieve applied in a fibre gives
`Y/S_c(Q)` with `Q² ≤ Y`. Rankin's bound
`S_c(Q) ≤ Q^α Π_ℓ(1+g_ℓ ℓ^{−α}) ≤ exp{α log Q + 2Σ_ℓ p_ℓ(c)ℓ^{−α}}` shows
that its bound obeys the same functional directly. No duality is needed in
that case.

*One-sided.* Put

    Ψ(λ) := inf_{α>0} [ αλ + Σ_ℓ p̄_ℓ ℓ^{−α} ].                      (2.5)

Theorem 2.5 shows that no level-λ majorant saves more than
`C·Ψ(λ) + O(log²λ)` beyond the R-term. No converse holds in general. For
example, coordinates at primes above `e^λ` are invisible, yet they can make
Ψ as large as order λ. Attainability is claimed only for the campaign
families at their parameters (§4).

*Large sieve, averaged.* Montgomery's large sieve gives `Σ_c Y/S_c(Q)`
summed over fibres. Rankin's bound and Jensen give
`Σ_c Y e^{−Φ_c} ≥ |R|·Y·e^{−avg Φ_c}`, so the averaged profile suffices
there too. This covers the slice systems of Theorem 2.5. No sequential
large-sieve analogue of Theorem 2.7 is claimed.

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
Charlier basis. The Selberg value `[Σ_{j≤m/2} μ^j/j!]^{−1}` is the
Christoffel function at 0, i.e. the optimum over square majorants. It is an
upper bound on the LP optimum W.

| μ | m | −log Selberg | −log W (LP) | Lagrange, best nodes | Lagrange, recipe of Lemma 2.2 | claimed bound (c) |
|---:|---:|---:|---:|---:|---:|---:|
| 128 | 8 | 16.262 | 16.269 | 19.391 | 24.686 | 49.993 |
| 256 | 8 | 19.018 | 19.021 | 22.418 | 27.382 | 53.112 |
| 256 | 16 | 33.788 | 33.794 | 37.729 | 48.975 | 96.520 |
| 512 | 8 | 21.783 | 21.784 | 25.574 | 30.946 | 56.231 |

Three observations:
* In the tested cases, the numerical LP optimum and the Selberg value agree
  to within 0.01 in −log, relative 10⁻³. So the square majorant is
  near-optimal among degree-m majorants nonnegative on ℤ_{≥0}. This is
  floating-point and uncertified, so it is EVIDENCE.

  Equality does not hold in general. The Christoffel value is the optimum
  over *square* majorants only, and integer-nonnegative polynomials can do
  better. For Poisson(1/2) and degree 2, `Q(k) = (k−1)(k−2)/2` has mean
  5/8 < 2/3, the square optimum.
* The rigorous Lagrange bound is within a factor of about 1.15 (best nodes)
  or 1.45 (recipe) of the truth.
* Bonferroni of degree r has `E Q_r(H) ≥ P(H ≥ r+1)` (Lemma 4.2). It is
  useless until `r ≈ μ`, whereas Selberg already saves `(m/2)log(μ/m)` at
  degree m. This is a constant-factor difference after re-optimising t.

---

### 2.6 Sequential windows: shared large primes

Theorem 2.5 needs the slice primes to be disjoint from the small modulus. So
a large prime cannot be the slice prime of one condition and part of the
small modulus of another. The following extension removes that restriction.

**Setting.** Take a modulus `Q₀`, `R ⊆ ℤ/Q₀`, and a set 𝒫 of primes not
dividing `Q₀`, split into ordered *windows* `𝒫 = W₁ ⊔ … ⊔ W_J`. A
*condition* C is an event

    E_C = {n ≡ a_C (mod q_C), n ≡ b_{C,ℓ} (mod ℓ^{e_{C,ℓ}}) for ℓ ∈ S(C)},

with `q_C | Q₀`, `∅ ≠ S(C) ⊆ 𝒫` and exponents `e_{C,ℓ} ≥ 1`. Assume:

**(U)** the last window meeting S(C) meets it in exactly one prime `ℓ(C)`,
and `e_{C,ℓ(C)} = 1`.

Fix exponents `E_ℓ ≥ max_C e_{C,ℓ}`. The *history* before window j is
`H_{<j} = (n mod Q₀, (n mod ℓ^{E_ℓ})_{ℓ∈W_{<j}})`.
For `ℓ ∈ W_j` and a history h, let `F_ℓ(h)` be the set of `b_{C,ℓ}` over the
conditions C with `ℓ(C) = ℓ` whose other requirements are met by h. Put
`p_ℓ(h) = |F_ℓ(h)|/ℓ`. The avoider set is
`𝒜 = {n : n mod Q₀ ∈ R, n ∉ E_C for all C}`.

Let `Q_seq` be the law of the history built window by window:
* `c = n mod Q₀` is uniform on R;
* given `H_{<j}`, the residues `n mod ℓ` (ℓ ∈ W_j) are independent and
  uniform on `ℤ/ℓ ∖ F_ℓ(H_{<j})`, and the higher digits of `n mod ℓ^{E_ℓ}`
  are uniform and independent of them.

Majorants of level λ are defined as in §1, with all primes of 𝒫 charged.

**Theorem 2.7 (sequential sieve limit; PROVED).** Assume that on the support
of `Q_seq`:
* `p_ℓ(h) ≤ 1/4` whenever `log ℓ ≤ λ`;
* `p_ℓ(h) < 1` always.

Then for every choice of `α_1,…,α_J > 0`,

    log(1/Eν) ≤ log(Q₀/|R|) + Σ_j E_{Q_seq}[Φ_j(H_{<j})],               (2.6)

where `Φ_j(h)` is the right side of (2.3) for the window-j coordinates
(`ℓ ∈ W_j`, `log ℓ ≤ λ`) with probabilities `p_ℓ(h)` and `α = α_j`. A window
with `log min W_j > λ` contributes 0.

*Proof.* Let g_j be the uniform conditional expectation
`g_j(h) = E[ν | H_{<j} = h]`. Let `𝒜_{<j}` be the set of histories that lie
in R and satisfy no condition with last window < j. Such conditions are
decided by `H_{<j}`. We show by downward induction that, for `h ∈ 𝒜_{<j}`,

    −log g_j(h) ≤ E_{Q_seq}[ Σ_{i≥j} Φ_i(H_{<i}) | H_{<j} = h ].

*Base case j = J+1.* `H_{<J+1}` determines membership in 𝒜, and ν ≥ 1 on 𝒜.

*Induction step.* Fix `h ∈ 𝒜_{<j}`. Given `H_{<j} = h`, the residues
`n mod ℓ^{E_ℓ}` (ℓ∈W_j) are independent and uniform. Their digits mod ℓ are
uniform, and the higher digits are independent of those digits. So the indicators
`x_ℓ = 1[n mod ℓ ∈ F_ℓ(h)]` are independent `Bern(p_ℓ(h))`. Put

    f(x) = E[ g_{j+1}(H_{<j+1}) | H_{<j}=h, x ].

Then:
* `E f = g_j(h)` and `f ≥ 0`;
* f is λ-level on W_j, because each term of ν, after conditioning,
  depends on `x_{T_i∩W_j}` only;
* `x = 0` is exactly the event that no condition with last window j holds.
  Given `x = 0`, `H_{<j+1}` lies in `𝒜_{<j+1}`, and its conditional law is
  the `Q_seq` transition.

The induction hypothesis and Jensen give
`f(0) ≥ exp(−E_{Q_seq}[Σ_{i>j}Φ_i | H_{<j}=h]) > 0`. Proposition 2.4,
applied to `f/f(0)`, gives `E f ≥ f(0)e^{−Φ_j(h)}`.

*Conclusion.* `Eν ≥ (|R|/Q₀)·avg_{c∈R} g_1(c)`, and Jensen over `c ∈ R`
finishes the proof. In `Φ_j` the logarithmic term is concave and the rest is
linear in `p_ℓ`. ∎

**Lemma 2.8 (profile under Q_seq; PROVED).** For `ℓ ∈ W_j`,

    E_{Q_seq} p_ℓ(H_{<j}) ≤ Σ_{C: ℓ(C)=ℓ} (1/ℓ) · P(c ≡ a_C (q_C) | c∈R)
                             · Π_{ℓ'∈S(C)∖{ℓ}} 1/(ℓ'^{e_{C,ℓ'}}(1−p*_{ℓ'})),

where `p*_{ℓ'}` is the supremum of `p_{ℓ'}(h)` over reachable histories.

*Proof.* Apply the chain rule over windows. Given the past, `n mod ℓ'` is
uniform on at least `ℓ'(1−p*_{ℓ'})` residues, and the higher digits are
uniform. ∎

So Theorem 2.7 has the same shape as Theorem 2.5, with two changes:
* the profile is bounded by an inflated uniform profile, with the factors
  `(1−p*)^{−1}`;
* the level term `19α_jλ` is paid once per window.

Conditioning can also *deactivate* later conditions, so the true sequential
profile may be smaller than the bound.

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

Every Case-B witness (q, d) of Theorem 3.1(B) for a prime `p ∤ q` lies in
the class with a = q, D = d. To see this:
* `D | x²` is equivalent to `g(D) | x`;
* `q | d+x` gives `p+a ≡ −4D (mod 4a)`;
* `4x = p+q` gives `gcd(q,x) | p`, hence `gcd(q,x) = 1` and so
  `gcd(a, g) = 1`.

The coprimality is needed. For example `p = 5`, `q = 15`, `x = 5`, `D = 25`
is a witness, but `p ∉ 185 (mod 300)`.

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
times `(log x)³`. That is EVIDENCE that this profile is also cubic.

The bound needed for Cor 3.4 is a weighted one. Write each d uniquely as
`d = r h²` with r squarefree; then `g(d) = rh`. The selector introduces the
weight `G/φ(G)`, so we need:

> **H_A3 (open; numerically supported in its unweighted form).**
> `Σ_{r sqfree, rh≤x} τ(4rh²+1)·(rh/φ(rh)) ≪ x(log 2x)²`.

Under H_A3 the Case-A profile is `≪ β^{−3}`, and Cor 3.4 extends to
families containing Case-A classes. No proof is written out here; it is a
divisor sum over a binary quadratic family. No existing proof uses Case A.

**Corollary 3.4 (the 3/4 ceiling for prime-slice forced-class architectures;
PROVED).** Fix `0 < C < 1` and `A ≥ 1`. Take a prime-slice system with
*every* condition a slice condition, i.e. there are no pure small-modulus
conditions, and with:
* every condition a forced class of Lemma 16.1 (any multiplier grouping) or
  of Lemma 3.2;
* each condition modulus `q₀ℓ` satisfying `q₀ ≤ ℓ^C`;
* `R = {c : (c,P)=1}` for some `P | Q₀` (a selector);
* `ℓ ≥ ℓ₀(C)`.

Then every majorant of level `λ ≤ A·log N` satisfies

    log(1/Eν) ≤ C₇(A,C) (log N)^{3/4} + log(P/φ(P)),
    where log(P/φ(P)) ≤ log log log P + O(1).

The same bound holds for the large-sieve bound of Remark 2.6, summed over
fibres. In particular, no such architecture whose final bound is
`N·Eν + (nonnegative rounding bound)` gives
`E(N) ≤ N exp{−(log N)^{3/4}·ω(N)}` with `ω → ∞`. This includes
`ω = (log log N)^ε`, provided the selector satisfies
`log log log P = o((log N)^{3/4})`.

*Proof.* Three checks.
* Since `q₀ ≤ ℓ^C` and `|ℛ(M)| ≤ M^{o(1)}`, we have
  `|F_ℓ(c)| ≤ ℓ^{C+o(1)} ≤ ℓ/4`.
* For the selector-type R, `P(c ≡ b (q₀) | R) ≤ 1/φ(q₀)`. Hence
  `p̄_ℓ ≤ Σ_{M=q₀ℓ} |𝒞(M)|·(M/φ(M))/M`, where `|𝒞(M)|` is the number of
  family classes mod M. It is at most `|ℛ(M)| ≤ τ(A²)` for Lemma 16.1
  classes, and the (a,D)-multiplicity for Lemma 3.2 classes.
* `ℓ ≥ M^{1/(1+C)}` gives `ℓ^{−α} ≤ M^{−α/2}`.

Lemmas 3.1 and 3.2 give `Σ p̄_ℓ ℓ^{−α} ≪ α^{−3}`. Take `α = λ^{−1/4}` in
(2.4). Here `G = O(log λ)` and the truncated mass satisfies `μ̄_λ ≪ λ³`. ∎

For the 3/4 note's selector, `log(P_y/φ(P_y)) = log log y + O(1)`.

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

**Corollary 3.6 (dominant-prime forced classes; PROVED).** Fix `0 < C < 1`
and `A ≥ 1`. Consider any family of Case-B forced classes (classes of ℛ(M),
Lemma 18.1, or (a,D)-classes mod `G = 4a·g(D)`, Lemma 3.2) such that every
modulus M has a prime factor `ℓ(M) ≥ M^{1/(1+C)}`. Such a prime is the
largest prime factor, since it exceeds √M.

The other prime factors of M are unrestricted. They may be large, they may
occur to higher powers, and they may be the dominant prime of *other*
moduli of the family. Let:
* `w₀ = w₀(C)` be large;
* `Q₀ = lcm(P_{w₀}, w₀-smooth parts of all moduli)`;
* `R = {c : (c,P_{w₀}) = 1, c satisfies no condition with all primes ≤ w₀}`.

Then every majorant of level `λ ≤ A log N` (all primes `> w₀` charged)
satisfies

    log(1/Eν) ≤ C₈(A,C) (log N)^{3/4} + log(Q₀/|R|).

The last term is `O_C(1)`. A `w₀`-smooth modulus is at most `w₀^{1+C}`, so
there are finitely many. Moreover **no forced class contains n = 1**, because
4/1 is not a sum of three unit fractions. So `c ≡ 1 (mod L')` lies in R,
where `L' = lcm(P_{w₀}, w₀-smooth moduli)`, and hence
`|R|/Q₀ ≥ 1/L' = e^{−O_C(1)}`.

*Proof.* Take windows `W_j = (e^{s₀C^{−j+1}}, e^{s₀C^{−j}}]` for j ≥ 1,
with `s₀ = log w₀`, so `W₁ = (w₀, w₀^{1/C}]`. Attach condition C to
`ℓ(C) = ℓ(M)`.

*(U) holds.* ℓ(M) exceeds √M, so it occurs to exponent one. Every other
prime ℓ' of M satisfies `ℓ' ≤ M/ℓ ≤ ℓ^C`, so it lies in an earlier window or
divides Q₀.

*The hypotheses of Theorem 2.7 hold.* The number of conditions with
dominant prime ℓ is at most `Σ_{q≤ℓ^C} ℓ^{o(1)} = ℓ^{C+o(1)}`. Hence
`p*_ℓ ≤ ℓ^{C−1+o(1)} ≤ ℓ^{−(1−C)/2} ≤ 1/4` for `ℓ > w₀`.

*The sequential profile.* Write `δ = (1−C)/2`. By the n = 1 remark,
`P(c ≡ a (mod q) | R) ≤ L'·P(c ≡ a (mod q) | (c,P_{w₀})=1) ≤ L'/φ(q)`.
So by Lemma 2.8 each condition contributes at most
`L'·(M/φ(M))·γ(M)/M`, where `γ(M) = Π_{ℓ'|M, ℓ'>w₀}(1−ℓ'^{−δ})^{−1}`.

The proof of Lemma 3.1 goes through with `M/φ(M)` replaced by
`(M/φ(M))γ(M) = Σ_{d|M} h(d)`. Here h is multiplicative, supported on
squarefree d, with `h(p) ≤ 1/(p−1) + 3p^{−δ}`.

* *Shiu range* (`d ≤ x^{1/2}`): this uses `Σ_d h(d)/φ(d) < ∞`.
* *Large divisors* (`d > x^{1/2}`): the bound is
  `x^{ε}·Σ_{x^{1/2}<d≤x} h(d)(x/d+1)`. We have
  `Σ_d h(d)d^{−1+δ/2} < ∞`, since its Euler factors are
  `1 + O(p^{−2+δ/2} + p^{−1−δ/2})`. Hence
  `x·Σ_{d>√x} h(d)/d ≪ x^{1−δ/4}` and `Σ_{d≤x} h(d) ≪ x^{1−δ/2}`. With
  `ε < δ/4` the tail is `≪ x^{1−δ/4+ε} = o(x)`.

For Lemma 3.2's grouping, use submultiplicativity:
`(G/φ(G))γ(G) ≤ 2·[(a/φ(a))γ(a)]·[(g/φ(g))γ(g)]` for `G = 4a·g` with
`g = g(D)`. Both
factors have bounded mean values, so the Euler factors still have pole
orders one and two, and the profile is `≪_C β^{−3}`.

*Per window.* Since `M ≤ ℓ^{1+C} ≤ e^{2s_j/C}` for `ℓ ∈ W_j`, the window
mass is `Σ_{ℓ∈W_j} E p_ℓ ≪ s_j³`, and its profile is
`≤ e^{−α s_j}·O(s_j³)`. Choosing `α_j` optimally per window gives
`E Φ_j ≪ min{s_j³, (λ/s_j)(1+log⁺(s_j⁴/λ))} + O(log²λ)`.

*Summing.* The windows are geometric in `s_j`, and only windows meeting
`ℓ ≤ e^λ` count; there are `J ≪_C log λ` of them.
* Below the crossover `s ≍ λ^{1/4}`, the cubic branch is a geometric sum.
* Above it, write `s = λ^{1/4}C^{−k}`; the window contributes
  `O_C(λ^{3/4}C^{k}(1+k))`.
* The remainders total `O_C(log³λ)`.

So `Σ_j E Φ_j ≪_C λ^{3/4}`. The constants deteriorate as C → 1, so C is
fixed. ∎

**What Cor 3.6 adds.** Corollary 3.4 required the multiplier part to consist
of "small" primes, never slice primes. Corollary 3.6 drops this, so it
covers the *complete* Case-B forced-class family restricted to moduli with
a dominant prime.

For *unweighted* integers, Dickman gives logarithmic density
`1 − ρ(1+C) = log(1+C)` for `P(M) ≥ M^{1/(1+C)}`. The share of the
*weighted* cubic supply is not proved; it is a conjecture, since the
weights are shifted divisor counts. If it matches, the dominant-prime part
is a positive proportion `log(1+C)` of the supply, for fixed C < 1.

What is left uncovered is the **balanced moduli** (`P(M) ≤ M^{1/2+o(1)}`),
i.e. moduli with at least two comparable large primes, or with
`P(M) ∈ (M^{1/2}, M^{1/(1+C)})` for the chosen C. See §5.6.

## 4. Exact accounting of the two campaign proofs

Notation: `μ_c` is the fibre mass and `r` the Bonferroni degree.

**Lemma 4.1 (3/4 note: what binds; PROVED).** The atom family `𝒜_X` of the
3/4 note is a prime-slice system with:
* `Q₀ = lcm(L_K, P_y)`;
* `𝒫 = primes in (X^{1/2}, X]`;
* `R = {(c,P_y)=1}`;
* `|F_ℓ(c)| = f_c(ℓ) ≤ ℓ^{1/3}`;
* `Σ_ℓ p_ℓ(c) ℓ^{−α} ≤ C_u t³ X^{−α/2}`. This is the upper half of the
  note's Corollary "uniform fibre masses" (cor:fibremass), valid for all c.

Its majorant `S_y·Q_r(H_X)` has level `λ = r·t`.

By Theorem 2.5, *every* majorant on this family has
`saving ≤ log log y + min{C t³, C(λ/t)(1 + log⁺(Ct⁴/λ))} + O(log²λ)`,
where `log log y` is the selector term. With `λ ≤ A L`,
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

So in the 3/4 note `r ≫ t³` is forced. The note's ledger is an *upper*
bound `log T_abs = O(rt)`, which suffices when `t⁴ ≲ L`. The ledger is not
proved necessary, and it need not be: the necessity of `t ≲ L^{1/4}`, in the
sense that no larger saving is possible, comes from Theorem 2.5 via
Lemma 4.1, not from the ledger. Replacing Bonferroni by any other majorant,
e.g. Selberg (§2.5), changes only constants.

**Lemma 4.3 (level of distribution; PROVED).** The BV level enters the 3/4
proof only through the box size `z = x^{ϑ'}` of the supply lemma. That lemma
needs `4uv ≤ 4z²` below the BV level, so `ϑ' < 1/4`; the note takes
`ϑ' = 1/6`.

Elliott–Halberstam would allow any `ϑ' < 1/2`, which is also the
distinctness limit `z² < ℓ`. So EH multiplies `μ_c` by a factor bounded in
terms of the chosen box exponents. The order of magnitude, and the exponent,
are unchanged. The integer assembly uses exact counts `N/q + O(1)` and no level of
distribution.

*Proof.* The block mass is `≍ (log z)² h = ϑ'² t² h`. This is the
unpruned-supply theorem of the note (thm:unpruned) with `x^{1/6}` replaced by
`x^{ϑ'}`; the lattice and Brun–Titchmarsh steps are unchanged. Theorem 2.5
then caps the saving through the profile, which changes only by this
bounded factor. ∎

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
| Rankin/Halász on `x=(p+a)/4` | **not closed; model Assessment only.** The non-multiplicativity counterexample is PROVED. The multiplicative slices lead to the stacking model, whose Assessment gives θ* ≈ 0.52. No universal obstruction is proved. | §5.2 |
| beyond-identity supply / exact criterion `−1∈Rat_a(h)` / large deviations of class counts | **closed** for prime-slice systems (Lemma 3.2: the criterion *is* the (a,D) forced classes; Lemma 5.3: effective mass = mass); complete system: EVIDENCE of sub-additivity (ratio ≈ 0.80) | §5.3 |
| combining both halves / both solution types | Case-B groupings **closed** (Lemmas 3.1–3.2). Adding Case A is closed **conditional on H_A3 (weighted form)**. Theorem 2.5 needs no independence between halves. | §5.4 |
| Elsholtz–Tao average as first-moment limit | **consistent**; the correct currency is the profile `Σp̄ℓ^{−α}`, which is exactly cubic (no loglog) | §5.5 |
| shared large primes in multipliers | **closed** for dominant-prime moduli (Thm 2.7, Cor 3.6) | §2.6 |
| balanced moduli; multipliers ≫ slice prime | **open**; hypothesis H_MS named; mass-cost Assessment predicts closure | §5.6 |
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
(either grouping) and Case-A classes has profile at most the sum. That sum
is cubic for Case B by Lemmas 3.1–3.2, and for Case A under H_A3. So the shared quadratic bit (DISCOVERIES
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

### 5.6 The open door: balanced moduli and large multipliers

Theorem 2.7 and Corollary 3.6 cover every forced-class family in which each
modulus has a dominant prime `P(M) ≥ M^{1/(1+C)}`, C < 1. Two kinds of
condition fall outside:

* **(a) Balanced moduli.** These have `P(M) ≤ M^{1/2+o(1)}`, i.e. at least
  two large primes of comparable size, or many medium ones. Their share of
  the cubic supply is plausibly `≈ 1 − log 2`, by unweighted Dickman; the
  weighted share is unproved.

  The failure is quantitative. Every two primes `ℓ₁, ℓ₂` of the same scale
  occur together in some modulus `kℓ₁ℓ₂ ≤ Q`. Windows of bounded log-ratio
  therefore always contain such pairs. (U) can still be arranged, but only
  with windows of single primes or near-singletons. Then the per-window
  level charge `19α_jλ` is paid about once per prime, and the bound
  degenerates to the plain mass.

  A level-λ term that sees m primes of a scale sees about m²/2 pair
  conditions, versus m single-slice ones. However, pair hits on a clique
  are determined by only m residues. So it is unclear whether this
  "quadratic visibility" can beat the Rankin functional (see below).

* **(b) Multipliers much larger than the dominant prime.** These are
  prime-slice conditions with small part `q₀ ≫ ℓ`.

  Theorem 2.5's free conditioning leaves such a k-part uncharged. The
  resulting bound `λ^{2/3}(log K)^{1/3}` exceeds `λ^{3/4}` only if
  `log K ≫ λ^{1/4}`. For `K ≫ z²` the lattice equidistribution behind the
  3/4 supply also fails: `(u,v)`-boxes of size `z² < k` no longer
  equidistribute mod k, so `μ_c` stops being uniform in c.

  The existing architectures pay for multipliers through the term moduli
  (3/4 note: `lcm(k_i) ≤ K^r`, as an *upper* ledger) or through one
  progression modulus `L_𝒦 ≤ N` (Cor 3.5). No lower bound on the multiplier
  cost of a general majorant is proved. Atoms may share multipliers, so
  `lcm(k_i)` can be small.

> **H_MS (named, open).** For every CRT system of forced classes with moduli
> ≤ e^λ, every level-λ majorant has
> `log(1/Eν) ≤ C·inf_α[αλ + Σ_cond P(cond)·(mod cond)^{−α}] + O(log²λ)`.
> Falsifiable in small models by exact LP. It is open even for the toy
> "random pair conditions on one scale".

**Assessment 5.4.** H_MS is what the mass-cost model predicts. Theorem 2.7
does *not* prove H_MS: its bound carries a level charge per window and the
inflated sequential profile. It does yield H_MS's intended consequence, the
`λ^{3/4}` cap, for dominant-prime Case-B families (Cor 3.6).

What is missing is a dual for AND-events of *same-scale* coordinates.
Thinning needs independent hit variables, and the sequential argument needs
one undetermined coordinate per condition at the moment it is decided.
Both fail for pairs inside one window.

* Under H_MS, every CRT-majorant architecture for ES built from Case-B
  forced classes (and Case A under H_A3), with a bounded-saving admissible
  set and rounding treated in absolute value, is capped at `(log N)^{3/4}`.
* Without H_MS, a θ > 3/4 attempt *must* exploit balanced moduli jointly,
  or multiplier sharing beyond Cor 3.5.

§5.3(iii) gives no sign that the complete system does better than its mass.

**Concrete next step.** Settle H_MS for one scale with pair conditions only.
Take N primes ~e^s, one forbidden residue pair per pair of primes, and
level m = λ/s primes per term. Compute the exact LP for small N, then try a
"clique-aware" dual: mix over the number of hit pairs, conditioned on the
residues. A counterexample here would be the first architecture-level hint
of θ > 3/4.

---

## 6. What a θ > 3/4 proof must contain

These are consequences of Theorems 2.5 and 2.7, Lemmas 3.1–3.2, 4.2 and
5.3.
1. It cannot be a CRT majorant over Case-B forced classes whose moduli all
   have a dominant prime `P(M) ≥ M^{1/(1+C)}` (C<1), at any level
   `N^{O(1)}`, with any weights (Cor 3.4, Cor 3.6). The multiplier parts are
   arbitrary, including large primes shared between conditions. Nor can it
   be a large sieve over slice systems (Remark 2.6).
2. The following change constants only (§§4, 5.3–5.4): both Case-B
   groupings, the exact a-frame criterion, Elliott–Halberstam, or a better
   Bonferroni/Selberg polynomial. Adding Case A is also constants-only,
   conditionally on H_A3.
3. It needs one of:
   * (i) a joint use of *balanced* moduli (`P(M) ≤ M^{1/2+o(1)}`) that beats
     their mass (H_MS false in the relevant regime);
   * (ii) multipliers larger than the slice primes, used without paying
     their lcm in level. No lower bound on that cost is proved;
   * (iii) a small-modulus admissible set R that is not of selector type
     and carries a large saving `log(Q₀/|R|)` of its own (H_MS again);
   * (iv) non-CRT arithmetic of the integers (Halász, Type I/II sums,
     moment methods), or signed cancellation in the rounding errors.
     §5.2 assesses (iv) via multiplicative slices at θ*, as a model only.

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
mkdir -p /tmp/theta
g++ -O2 -std=c++17 -o /tmp/theta_void_primes scripts/theta_void_primes.cpp
for i in 0 1 2 3; do /tmp/theta_void_primes 4000 $((10**12 + i*28000000000)) 28000000000 > /tmp/theta/void_$i.txt & done; wait
# merge: sum the 'voids' column and the prime counts (see data/theta/void_primes_Q4000.txt header)
```
