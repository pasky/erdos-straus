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
| Thm 2.5 | **Sieve-limit theorem.** Take a *prime-slice* CRT system: the conditions are independent across large primes ℓ once a small residue c is fixed. Every nonnegative majorant of level λ of its avoider set has mean ≥ `(|R|/Q₀)·exp{−19αλ − C₄ Σ_ℓ p̄_ℓ ℓ^{−α} − O(log²λ)}`, for every α>0. Here λ charges only the slice primes. The error term is O(log²λ) provided the truncated mass satisfies `μ̄ ≤ λ^{O(1)}` and `s_* ≫ 1` (true in all applications here); in general it is the explicit term of (2.4), which can be ≍ λ log λ. | PROVED |
| Cor 3.4 | Take any family of Case-B forced classes (both groupings) that are all slice conditions, with small parts k ≤ ℓ^C (C<1) and a selector admissible set. Every majorant of level `N^A`, and every Montgomery large-sieve bound, saves at most `C(A)(log N)^{3/4} + log(P/φ(P))`, where the last term is O(log log log P). So **3/4 is sharp for this class, and no power of log log N can be gained.** This assumes the final bound has the form `N·Eν + (nonnegative rounding bound)`. With the rounding bound `Σ|a_i|`, the level hypothesis follows from `Σ|a_i| < N` and family slice primes `≤ N^{O(1)}` (Lemma 2.9, from review-theta-2). | PROVED |
| Thm 2.7, Cor 3.6 | **Sequential extension.** For nonnegative CRT majorants (no large-sieve claim), the cap `C(A,C)(log N)^{3/4} + O_C(1)` holds for every Case-B forced-class family whose moduli all have a dominant prime `P(M) ≥ M^{1/(1+C)}` (C<1). The other prime factors are arbitrary (higher powers allowed) and may be shared between conditions. By Dickman, this is a positive proportion `log(1+C)` of unweighted moduli; the weighted share of the supply is conjectural. | PROVED |
| Lemma 3.7 | **H_A3 holds.** `Σ_{rh≤x} τ(4rh²+1)·rh/φ(rh) ≪ x log²x`, so Cor 3.4/3.6 cover Case-A classes too. | PROVED, using Elsholtz–Tao Prop. 1.4 (published, not re-proved) |
| Lemma 3.8 | **Balanced moduli** (`P(M) ≤ √M`, even same-scale pairs) carry `≫ (log x)³` of the Case-B supply. The open door is not lower order. | PROVED (BV + lattice lemma) |
| Thm 5.5 | **Λ² sieve limit for arbitrary systems** (no slice structure): for g ∈ level λ/2 with g ≥ 1 on A, `saving(g²) ≤ αλ/2 + Ξ_A(α)`, where Ξ_A is the noise-stability excess. This reduces balanced moduli, for Λ², to hypothesis H_MS^{Sel}. | PROVED; H_MS^{Sel} open |
| Cor 3.5 | Polylogarithmic multipliers, or multipliers whose lcm is at most N (the 2/3 note's architecture), cap the saving at `C L^{2/3}(log L)^{1/3}`. **The 2/3-loglog note is sharp for its architecture.** | PROVED (given the notes' BT upper bounds) |
| Lemma 2.9 | **Coefficient budget ⇒ level** (added by review-theta-2). A majorant with coefficient sum T and slice primes `≤ e^{Λ₀}` can be coarsened to level `Λ₀ + log T + log(1/Eν)` at most doubling its mean. | PROVED |
| §4 | Exact accounting. In both proofs the binding constraint is the pair (supply profile, budget). For the 3/4 note the budget is its coefficient sum `T_abs ≤ N^{1/2}`, which forces level `λ ≲ log N` via Lemma 2.9. For the 2/3 note it is the large-sieve level `Q² ≤ N/L_K` together with `L_𝒦 ≤ N` (Lemma 4.4). Bonferroni depth, the BV level and the selector cannot improve the exponent (PROVED). That alternatives attain the same order up to constants is EVIDENCE (§2.5). | PROVED (Lemmas 4.1–4.4), except the EVIDENCE part |
| §5 | Levers, inside the prime-slice class. Cost-per-condition, beyond-identity supply (Case B), both Case-B groupings and Bonferroni→Selberg are closed by proved statements. Adding Case A is closed via H_A3, which is proved from Elsholtz–Tao Prop. 1.4 (§3.7). Halász has a proved non-multiplicativity counterexample, but its joint route is only a model Assessment (θ* ≈ 0.52), not a closure. The ET first moment is consistent with B = 3. Open: balanced moduli (no dominant prime), multipliers larger than the slice prime, and non-selector small-modulus subsystems (H_MS). | see table §5.0 |
| §5.3 | Complete-system void among 4.05·10⁹ real primes near 10¹². The effective mass −log P(void) falls from 1.39 to about 0.80 of the first-moment mass as Q grows to 4000. There is no super-cubic effect. | EVIDENCE |
| §2.5 | Exchangeable Poisson model, tested cases. The numerically computed LP optimum (uncertified floating point) agrees with the Selberg square-majorant value 1/Σ_{j≤m/2} μ^j/j! to within 0.01 in −log. So Selberg Λ² is near-optimal there, and Bonferroni loses only a constant factor. | EVIDENCE |

**Verdict.** No route to θ > 3/4 survives inside the *dominant-prime* CRT
world, defined as follows:
* every condition's modulus has a prime factor `≥ M^{1/(1+C)}`, with C < 1
  fixed;
* the admissible set has bounded saving;
* the majorant ν is ≥ 0 on all of ℤ and ≥ 1 on the whole avoider set;
* the final bound has the form `N·Eν + Σ_i|a_i|`, i.e. rounding is
  bounded by the absolute coefficient sum;
* and **either** ν has level ≤ A·log N, **or** the family's slice primes
  are ≤ N^{O(1)}. In the second case Lemma 2.9 reduces to the first,
  because a non-trivial bound has `Σ|a_i| < N`.

This world contains the prime-slice world of Cor 3.4. The precise list of
what it excludes is §6, "What the theorems exclude".

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

(a) If μ' ≥ 1, then z ≥ 4 because q ≤ 1/4. Take the single node
`y = ⌈μ'⌉ ≤ z/4 + 1 ≤ z−1` and apply Lemma 2.1 with
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

Write Φ(w) for this right-hand side. Average over w using Jensen for exp:
`E f = E_w E_u f_w ≥ E_w e^{−Φ(w)} ≥ e^{−E_w Φ(w)}`. Then use `E_w q_g z_g = μ_g`,
and concavity of log, `E_w log(16q_g z_g+16) ≤ log(16μ_g+16)`.
Finally `e^{−2αs_g} ≤ e^{−αs_i}` on `B_g`, and `Σ_g log(16μ_g+16) ≤ G·log(16μ+16)`. ∎

### 2.4 The CRT form

**Theorem 2.5 (sieve limit for prime-slice systems; PROVED).** Take a
prime-slice system as in §1. Assume that for every `c ∈ R`:
* `|F_ℓ(c)| ≤ ℓ/4` for every `ℓ ∈ 𝒫` with `ℓ ≤ e^λ`;
* `|F_ℓ(c)| < ℓ` for every `ℓ ∈ 𝒫`, so every admissible fibre has avoiders.

Here and below μ̄ denotes the *truncated* mass `μ̄ = Σ_{ℓ∈𝒫, ℓ≤e^λ} p̄_ℓ`.
Primes above e^λ are invisible (Step 0 of Prop. 2.4), so the untruncated
mass, which may be infinite for infinite families, never enters.

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
profiles into `p̄_ℓ` and the truncated mass `μ̄`. ∎

*Size of the error term.* The last two terms of (2.4) are O(log²λ) only
when `s_* ≫ 1` and `log μ̄ ≪ log λ`. In general μ̄ can be as large as
`π(e^λ)/4`, and then the term is ≍ λ log λ. In every application below,
`μ̄ ≪ λ³`, so it is O(log²λ).

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
on the rounding term)` is therefore capped at the level of its ν. If the
rounding bound is the absolute coefficient sum `Σ|a_i|`, then Lemma 2.9
(§2.7) shows that this sum already bounds the level, provided the slice
primes are bounded. A method that proves *signed*
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

### 2.7 Coefficient budget implies level (added by review-theta-2)

The caps of Theorems 2.5 and 2.7 are stated for majorants of bounded
*level*. Interval methods such as the 3/4 note are constrained instead by
the *coefficient sum*. The note's transfer
`Σ_{n≤N} ν(n) = N·Eν + O(Σ|a_i|)` holds for every modulus, and the note
calls its modulus bound "not necessary". The following lemma, from the
hostile review `reviews/exceptional-theta-review.md` (item 3, defect SC1),
bridges the two.

**Lemma 2.9 (coefficient budget ⇒ level; PROVED in review-theta-2).** Take
a prime-slice system (§1), or the setting of §2.6. Let
`ν = Σ_i a_i 1[n ≡ b_i (mod d_i)]` satisfy ν ≥ 0 on ℤ and ν ≥ 1 on 𝒜.
Put `T = Σ_i |a_i|`, and assume every slice prime satisfies `log ℓ ≤ Λ₀`.
Then for every λ there is a majorant ν' of level ≤ λ with ν' ≥ ν pointwise
and

    Eν' ≤ Eν + T·e^{Λ₀−λ}.

In particular, the choice `λ = Λ₀ + log T + log(1/Eν)` gives `Eν' ≤ 2Eν`.

*Proof.* Leave every term of level ≤ λ unchanged.
* *Terms of level > λ with `a_i < 0`.* Drop them. This raises ν pointwise
  and raises the mean by `|a_i|/d_i ≤ |a_i|e^{−λ}`.
* *Terms of level > λ with `a_i > 0`.* List the term's slice primes in
  increasing order and keep the longest prefix of level ≤ λ. The next
  prime has log ℓ ≤ Λ₀, so the kept prefix has level `> λ − Λ₀`. Replace
  `d_i` by the divisor `d'_i` consisting of the non-slice part of `d_i`
  times the kept prime powers. Then `1[n≡b_i (d'_i)] ≥ 1[n≡b_i (d_i)]`,
  and the mean rises by at most `a_i/d'_i ≤ a_i e^{Λ₀−λ}`.

Hence ν' ≥ ν ≥ 0, ν' ≥ 1 on 𝒜, and every term of ν' has level ≤ λ. Summing
the increases gives the mean bound. ∎

**Consequence.** Combine Lemma 2.9 with Cor 3.4 or Cor 3.6. Suppose:
* the family's slice primes are at most `N^A`;
* the final bound `N·Eν + Σ|a_i|` is non-trivial, so `T < N`.

Then the saving s satisfies `s ≤ log 2 + Cλ^{3/4} + (R-term)` with
`λ ≤ (A+1) log N + s`. Hence `s ≪_{A,C} (log N)^{3/4}`.

Two exclusions remain:
* families with slice primes beyond `N^{O(1)}`, since Lemma 2.9 needs Λ₀;
* methods whose rounding bound is smaller than `Σ|a_i|`, for example bounds
  that use *which* classes meet [1,N]. These count as signed-rounding or
  non-CRT methods (§6).

`scripts/review_theta_lemmaR.py` checks the mechanics numerically.

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
`nm ≡ −1 (mod 4g(d))`. This reduction is PROVED; the derivation follows.

Case A is notes Theorem 3.1(A) (notes.md l. 84–89, 102–106): there are
`m ≡ 3n (mod 4)`, `z₀ = (nm+1)/4` and `d | z₀²` with `m | d + z₀`, and
then `4/n = 1/x + 1/y + 1/(n z₀)` with `x = (z₀+d)/m`, `y = (z₀+z₀²/d)/m`.
* *The m-condition.* m is odd, so `m | d+z₀ ⇔ m | 4d+4z₀ = 4d+nm+1 ⇔ m | 4d+1`.
* *The d-condition.* `d | z₀² ⇔ g(d) | z₀`, since `v_p(d) ≤ 2v_p(z₀) ⇔
  ⌈v_p(d)/2⌉ ≤ v_p(z₀)`. This in turn is `⇔ 4g(d) | nm+1`. Here
  `m | 4d+1` makes m a unit mod `4g(d)`, so the condition reads
  `n ≡ −m^{−1} (mod 4g(d))`. The congruence mod 4 is exactly
  `m ≡ 3n (mod 4)`, i.e. integrality of z₀.
* *Forcedness for every n ≥ 1, not only primes.* Given such n, put
  `z₀ = (nm+1)/4`.
  * x is an integer by the m-condition.
  * y is an integer because `z₀ + z₀²/d = z₀(d+z₀)/d` and `(m,d) = 1`.
  * The identity `1/x + 1/y = m/z₀` (notes Lemma 2.1) gives
    `m/z₀ + 1/(n z₀) = (nm+1)/(n z₀) = 4/n`.

Its exact union mass up to `x = 10², 10³, 4000` is 0.0280, 0.0257 and 0.0254
times `(log x)³`. That is EVIDENCE that this profile is also cubic.

The bound needed for Cor 3.4 is a weighted one. Write each d uniquely as
`d = r h²` with r squarefree; then `g(d) = rh`. The selector introduces the
weight `G/φ(G)`, so we need:

> **H_A3 (now PROVED, §3.7, from Elsholtz–Tao Prop. 1.4).**
> `Σ_{r sqfree, rh≤x} τ(4rh²+1)·(rh/φ(rh)) ≪ x(log 2x)²`.

Under H_A3 the Case-A profile is `≪ β^{−3}`, and Cor 3.4 extends to
families containing Case-A classes. The proof is in §3.7. No existing proof
uses Case A.

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
`log log log P = o((log N)^{3/4})`. Here "such" includes the hypothesis
`λ ≤ A·log N`. By Lemma 2.9 that hypothesis may be replaced by: the
rounding bound is `Σ|a_i| < N`, and the family's slice primes are
`≤ N^{O(1)}`.

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

The last term is `O_C(1)`, although Q₀ itself is not bounded. Q₀ depends on
the family and can be astronomically large, because the w₀-smooth parts of
the moduli are unbounded. Only the ratio `Q₀/|R| ≤ L'` enters, with L'
defined below and `L' ≤ e^{O(w₀^{1+C})}`. A `w₀`-smooth *modulus* is at most
`w₀^{1+C}`, so there are finitely many. Moreover **no forced class contains n = 1**, because
4/1 is not a sum of three unit fractions. So `c ≡ 1 (mod L')` lies in R,
where `L' = lcm(P_{w₀}, w₀-smooth moduli)`, and hence
`|R|/Q₀ ≥ 1/L' = e^{−O_C(1)}`.

*Proof.* Take windows `W_j = (e^{s₀C^{−j+1}}, e^{s₀C^{−j}}]` for j ≥ 1,
with `s₀ = log w₀`, so `W₁ = (w₀, w₀^{1/C}]`. Write `s_j = s₀C^{−j+1}`
for the log of the *lower* endpoint of W_j, so that `W_j = (e^{s_j}, e^{s_j/C}]`.
Attach condition C to
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

### 3.7 Case A: H_A3 holds (follow-up 2)

**Lemma 3.7 (weighted Case-A divisor sum; PROVED modulo Elsholtz–Tao
Prop. 1.4).** For `x ≥ 2`,

    Σ_{r,h ≥ 1, rh ≤ x} τ(4rh²+1) · (rh/φ(rh)) ≪ x (log x)².             (3.7)

So H_A3 holds, even without the restriction to squarefree r. The same bound
holds with the extra weight `γ(rh)` of Cor 3.6.

*Source.* Elsholtz–Tao, arXiv 1107.1010 (J. Aust. Math. Soc. 2013),
Proposition 1.4: for `A, B > 1` and every positive integer
`k ≪ (AB)^{O(1)}`,

    Σ_{a≤A} Σ_{b≤B} τ(k a b² + 1) ≪ AB log(A+B) log(1+k).

Their equation (8.2) is exactly the dyadic form of (3.7), with a = h and
d = r. It is the input of their bound `Σ_{p≤N} f_I(p) ≪ N log²N log log N`.

*Proof.* Use `n/φ(n) ≤ (π²/6)Σ_{d|n} 1/d`, which holds since the ratio of the
Euler factors is `Π(1−p^{−2}) ≥ 6/π²`. Write `r = s r'`, `h = t h'`, so that
`4rh² = (4st²)·r'h'²`. The left side of (3.7) is then at most

    C Σ_{s,t} (1/(st)) Σ_{r'h' ≤ Y} τ(4st²·r'h'² + 1),   Y = x/(st).

*Case `st ≤ √x`.* Cover the hyperbolic region `r'h' ≤ Y` by `O(log Y)`
rectangles `r' ≤ A`, `h' ≤ B` with `AB ≍ Y`, padding unit endpoints so
that `A, B ≥ 2`. Then `AB ≥ Y/2 ≥ √x/2` and `k = 4st² ≤ 4x^{3/2} ≪ (AB)^3`,
uniformly. So Prop. 1.4 applies to every rectangle and gives
`≪ AB log(A+B) log(1+k)`. Summing,
`Σ_{r'h'≤Y} τ(·) ≪ Y (log x)² log(1+4st²)`, and
`Σ_{s,t} log(1+4st²)/(st)² < ∞`.

*Case `st > √x`.* Here `Y < √x`, and `τ ≪_ε x^{ε}` gives a total of
`≪ x^{1/2+2ε}`.

*The γ-weight.* Write `γ(n)n/φ(n) = Σ_{d|n} η(d)`, with η multiplicative,
supported on squarefree d, and `η(p) = O(p^{−1} + p^{−δ})`, where
`δ = (1−C)/2`. Repeat the argument with `η(s)η(t)` in place of `1/(st)`.

* *Range `st ≤ √x`.* This needs `Σ_{s,t} η(s)η(t)log(2+st)/(st) < ∞`, which
  holds since `η(p)/p ≪ p^{−1−δ}`.
* *Tail `st > √x`.* Use `Σ_n η(n)n^{−1+δ/2} < ∞`. It gives
  `Σ_{st>√x} η(s)η(t)(x/st)^{1+ε} ≪ x^{1+ε}·x^{−δ/4}·O_C(1)`, which is
  `o(x)` for `ε < δ/4`. ∎

*Consequence.* The Case-A class mass up to modulus G, `Σ F_A(G')/G'` for
`G' ≤ G`, is at most `Σ_{4rh≤G} τ(4rh²+1)/(4rh)`, with r squarefree. By
partial summation from (3.7) its profile, with the selector weight, is
`≪ β^{−3}`. So Corollaries 3.4 and 3.6 hold for families containing Case-A
classes, with the dominant prime taken in `G = 4rh`. The "conditional on
H_A3" qualifications elsewhere in this file are now discharged. They rely
on a published but externally sourced Proposition 1.4, which was not
re-proved here.

Numerically, the Case-A union mass is about `0.0254 (log x)³` at x = 4000
(§3, `data/theta/profile.txt`), consistent with (3.7).

### 3.8 Balanced moduli carry a positive proportion of the supply (follow-up 2)

Call M **balanced** if `P(M) ≤ M^{1/2}`. These moduli lie outside Cor 3.6
for every C < 1.

**Lemma 3.8 (PROVED; standard inputs).** There are `c > 0` and `x₀` such that
for `x ≥ x₀`,

    Σ_{M≤x, M≡3 (4), P(M)≤M^{1/2}} |ℛ(M)|/M ≥ c (log x)³.

More precisely, fix any η ∈ (0, 1/480]. The moduli
`M = k ℓ₁ ℓ₂` with:
* primes `ℓ₁ ∈ (Y, Y^{1+η/2}]` and `ℓ₂ ∈ (Y^{1+η/2}, Y^{1+η}]`;
* odd `k ∈ (Y^{2η}, Y^{3η}]`;
* `Y = x^{1/(2+4.5η)}`

already contribute `≥ c(η)(log x)³`. These are *same-scale* pairs:
`log ℓ₂/log ℓ₁ ≤ 1+η`.

*Proof.*

*Structure of M.*
* Each such M satisfies `M ≤ x`.
* M is balanced: `M ≥ Y^{2+2.5η}`, so `√M ≥ Y^{1+1.25η} ≥ ℓ₂ = P(M)`.
* The triple `(k,ℓ₁,ℓ₂)` is determined by M. All primes of k are below `Y`,
  so ℓ₁ and ℓ₂ are the only prime factors of M above Y.

*Classes of ℛ(M).* For coprime `u, v ≤ z := Y^{1/8}` with `(uv,k)=1` and
`4uv | M+1`, the class `−uv^{−1} (mod M)` lies in ℛ(M) by the multiplier
identity. Distinct (u,v) give distinct classes already mod ℓ₂, because
`|uv'−u'v| < z² < ℓ₂`. Since `(uv, ℓ₁ℓ₂) = 1` automatically,

    S ≥ Σ_{k,ℓ₁} (1/(kℓ₁)) Σ_{(u,v)} Σ_{ℓ₂ ∈ I₂, ℓ₂ ≡ −(kℓ₁)^{−1} (mod 4uv)} 1/ℓ₂.

*The ℓ₂-sum.* Split `I₂` into dyadic blocks `(y,2y]`. With `q = 4uv ≤ 4Y^{1/4}`,
which is far below `y^{1/2}`, partial summation gives for each block

    Σ_{y<ℓ≤2y, ℓ≡a (q)} 1/ℓ = (1/φ(q))∫_y^{2y} dt/(t log t) + O(E**_y(q)/y),

where `E**_y(q) = max_{y≤t≤2y} max_a |π(t;q,a) − li(t)/φ(q)|`. The main
terms total `(c'_η + o(1))/φ(q)`, where
`c'_η = log((1+η)/(1+η/2))`.

For the error terms, a modulus q arises from at most τ(q) pairs. Over
`(k, ℓ₁)` with weight `1/(kℓ₁)`, of total `≪ log Y`, Cauchy–Schwarz against
Brun–Titchmarsh and the maximal Bombieri–Vinogradov theorem gives
`Σ_q τ(q)E**_y(q) ≪ y(log y)^{−10}` per block. This is the argument of the
2/3 note's mass lemma. Summed over `O(log Y)` blocks, it is `o(1)`.

*The (u,v)-sum.* By the 3/4 note's lattice lemma (eq. latlower) summed over
the φ(k) residues c mod k, exactly as in its lower `W_k` bound,
`Σ_{(u,v)} 1/(uv) ≥ (1/4)(φ(k)/k)²Λ²` with `Λ ≥ ½log z`. This needs
`z ≥ K^{20}` with `K = Y^{3η}`, i.e. `η ≤ 1/480`.

*Conclusion.* `Σ_{k∈(Y^{2η},Y^{3η}], k odd} (φ(k)/k)²/k ≫ η log Y`, and
`Σ_{ℓ₁∈I₁} 1/ℓ₁ ≫ η`. So `S ≫ η³ (log Y)³ ≍_η (log x)³`. ∎

*Numerics (EVIDENCE).* `scripts/theta_balanced_share.py` computes the share
of the weighted Case-B mass `Σ τ(A²)/M` carried by balanced moduli:

| x | 10³ | 10⁴ | 10⁵ | 10⁶ | 10⁷ |
|---|---:|---:|---:|---:|---:|
| weighted | 0.098 | 0.121 | 0.141 | 0.157 | 0.171 |
| unweighted log-density | 0.095 | 0.117 | 0.134 | 0.148 | 0.159 |

The exact deduplicated |ℛ(M)| gives the same values to about 10⁻³. Both
shares still grow slowly toward Dickman's limiting log-density
`1 − log 2 = 0.307` for the unweighted set. The weighted share stays
slightly *above* the unweighted one.

**Consequence.** The open door of §5.6(a) is not a lower-order effect.
Same-scale balanced moduli, at any fixed log-ratio 1+η, carry `≫_η (log x)³`
supply. Lemma 3.8 constructs such pairs. It does *not* by itself prove that
every window partition loses: singleton or arbitrarily narrow windows have
no internal pairs. A partition whose windows have log-widths bounded
*below* would need an additional placement argument, which is not written
out.

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

What forces `λ ≲ L` is the note's coefficient budget, not its modulus
bound. The note's transfer `N·E_CRT ν + O(T_abs)` is valid for any moduli,
and the note calls `q_max ≤ N^{1/2}` "not necessary". The real constraint
is `T_abs ≤ N^{1/2}`. Here the slice primes are ≤ X, so `Λ₀ = t ≤ L`.
Lemma 2.9 then turns any majorant on this family with coefficient sum < N
into one of level `≤ t + log N + saving` with at most twice the mean, and
the cap above applies to it.

So the binding constraint in the 3/4 proof is the following conjunction. It is
not Bonferroni depth, the BV level or the selector.

    (supply)  μ_c ≤ C_u t³ uniformly    and    (budget)  log T_abs ≤ log N,
              which forces level λ ≲ log N via Lemma 2.9.

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
e.g. Selberg, cannot improve the exponent (PROVED, Theorem 2.5). That such
replacements attain the same order up to constants is EVIDENCE only (§2.5).

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

*Remark (the rigorous reason; added after review-theta-2, A1).* The proof
above describes one construction, the unpruned supply with box `x^{ϑ'}`. By
itself that does not show that *no* use of EH can raise the profile. The
fully rigorous reason is Lemma 3.1, together with Lemmas 3.2 and 3.7 for
the other groupings and for Case A. These bound the *entire* forced-class
supply by `≪ x log²x`, so the profile is `≪ α^{−3}` independently of any
level of distribution. Theorem 2.5 (or 2.7) therefore caps every
EH-based variant on these classes at `λ^{3/4}`.

**Lemma 4.4 (2/3-loglog note: what binds; PROVED).** The note:
* splits into progressions mod `L_K`, with `log L_K ≈ K ≤ δL`;
* applies Montgomery's sieve with `Q² ≤ N/L_K`;
* has `μ_c ≤ A t² h(K)` with `h(K) ≍ log K ≤ log L`.

By Remark 2.6 and Cor 3.5, its bound cannot exceed
`exp{−C L^{2/3}(log L)^{1/3}}`. The binding inequality is
`h(𝒦) ≤ Π_{p | L_𝒦}(1+1/p) ≪ log log L_𝒦` (the note's own closing remark),
combined with the requirement `L_𝒦 ≤ N`. Vaughan/PW is the case `𝒦 = {1}`,
giving `L^{2/3}`.

The admissible set of the note is the reduced residues mod `L_K`, and the
fibre-mass upper bound is proved for those. So the R-term
`log(L_K/φ(L_K)) ≍ log log K ≪ log log L` of (2.4) also enters the cap.
It is negligible against `L^{2/3}(log L)^{1/3}`. ∎

**Binding table.**

| proof | supply profile | level / budget | binding | non-binding (cannot improve the exponent) |
|---|---|---|---|---|
| Vaughan/PW | `t²` per slice scale (k=1) | `Q² ≤ N` | profile + level → 2/3 | BV level, Rankin-tail constant |
| LL 2/3-loglog | `t² log K`, `L_K ≤ N` | `Q² ≤ N/L_K` | `h ≤ log log L_K` | the progression split itself (costs a constant) |
| 3/4 note | `t³` (`log K = κt`) | `log T_abs ≤ ½L`, which forces `rt ≲ L` (Lemma 2.9) | profile + budget → 3/4 | Bonferroni depth, BV level, selector, pruning (§76) |

---

## 5. The levers

### 5.0 Lever table

| lever (brief) | outcome | where |
|---|---|---|
| cost per condition below log X; weighting moduli by mass; `ΣF(M)/M·log M ≍ t⁴` vs `t³` | **closed** (Thm 2.5 + Lemma 3.1): mixing scales optimally is exactly the Rankin functional (2.5); the identity profile gives `λ^{3/4}` | §5.1 |
| Rankin/Halász on `x=(p+a)/4` | **not closed; model Assessment only.** The non-multiplicativity counterexample is PROVED. The multiplicative slices lead to the stacking model, whose Assessment gives θ* ≈ 0.52. No universal obstruction is proved. | §5.2 |
| beyond-identity supply / exact criterion `−1∈Rat_a(h)` / large deviations of class counts | **closed** for prime-slice systems (Lemma 3.2: the criterion *is* the (a,D) forced classes; Lemma 5.3: effective mass = mass); complete system: EVIDENCE of sub-additivity (ratio ≈ 0.80) | §5.3 |
| combining both halves / both solution types | **closed**: Case-B groupings (Lemmas 3.1–3.2), and Case A via Lemma 3.7 (H_A3 proved from Elsholtz–Tao Prop. 1.4). Theorem 2.5 needs no independence between halves. | §5.4, §3.7 |
| Elsholtz–Tao average as first-moment limit | **consistent**; the correct currency is the profile `Σp̄ℓ^{−α}`, which is exactly cubic (no loglog) | §5.5 |
| shared large primes in multipliers | **closed** for dominant-prime moduli (Thm 2.7, Cor 3.6) | §2.6 |
| balanced moduli; multipliers ≫ slice prime | **open**, but sharpened. Balanced moduli carry `≫(log x)³` (Lemma 3.8). Theorem 5.5 gives a sieve limit for Λ²-majorants on *arbitrary* systems, reducing H_MS for Λ² to the noise-stability bound H_MS^{Sel}. The toy LP shows no counterexample. | §5.6–5.8 |
| Bonferroni → Selberg/large sieve | cannot improve the exponent (PROVED, Thm 2.5). Attaining the same order up to constants is EVIDENCE (Lemma 4.2, §2.5 numerics). | §4 |

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
is cubic for Case B by Lemmas 3.1–3.2, and for Case A by H_A3, which is proved in §3.7. So the shared quadratic bit (DISCOVERIES
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
  forced classes (Case A included, via §3.7), with a bounded-saving admissible
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

### 5.7 Balanced moduli for Selberg-type majorants (follow-up 2)

This subsection proves a sieve limit with **no structural hypothesis on the
conditions**. Balanced, multi-prime and shared-prime moduli are all
allowed. The price is that the majorant must be of Selberg type, a square
`g²`. The result reduces H_MS for such majorants to a concrete
noise-stability quantity.

**Setting.** Take a finite product probability space `Ω = Π_i Ω_i` (CRT
coordinates: residues modulo prime powers, and possibly one aggregated
small coordinate). Each coordinate has a cost `s_i ≥ 0`: `s_i = log ℓ` for
a slice prime ℓ, and 0 for coordinates that are free and not charged.
`A ⊆ Ω` is an arbitrary event (the avoider set of an *arbitrary* condition
family). Let `V_κ` be the span of functions of `ω_T` over sets T with
`Σ_{i∈T} s_i ≤ κ`; since this family of T is down-closed, `V_κ` is the sum
of the Efron–Stein components `H_T`.

**Theorem 5.5 (Selberg-type sieve limit for arbitrary systems; PROVED).**
Let `g ∈ V_{λ/2}` with `g ≥ 1` on A, so `ν = g²` is a majorant of level λ.
Then for every α > 0,

    E g² ≥ e^{−αλ/2} · P(A)² / P(ω ∈ A, ω' ∈ A),                      (5.1)

where ω' is the ρ-correlated copy: independently for each i, `ω'_i = ω_i`
with probability `ρ_i = e^{−α s_i}`, and otherwise `ω'_i` is a fresh
sample. Equivalently, `saving(ν) ≤ αλ/2 + Ξ_A(α)`, where

    Ξ_A(α) := log [ P(A ∩ A'_α) / P(A)² ] ∈ [0, log(1/P(A))].

*Proof.* `E[g1_A] ≥ P(A)`. Since `g ∈ V_{λ/2}`,
`E[g1_A] = ⟨g, Π_{V}1_A⟩ ≤ ‖g‖·‖Π_V 1_A‖`. Next,

    ‖Π_V 1_A‖² = Σ_{c(T)≤λ/2} ‖(1_A)_T‖² ≤ e^{αλ/2} Σ_T e^{−αc(T)}‖(1_A)_T‖²
               = e^{αλ/2} ⟨1_A, T_ρ 1_A⟩ = e^{αλ/2} P(A ∩ A').

Here `T_ρ` is the noise operator; it acts on `H_T` by `Π_{i∈T}ρ_i`. ∎

It covers Selberg's Λ² sieve, where `g = Σ_{d} λ_d 1[d | ·]` with `λ₁ = 1`
equals 1 on A. Like Theorem 2.5 it is a statement about CRT means. It may
be applied fibrewise over zero-cost coordinates, followed by Cauchy–Schwarz
over fibres.

**Corollary 5.6 (slice systems; PROVED).** For a prime-slice system,
fibrewise, `Ξ_{A_c}(α) = Σ_ℓ log(1 + ρ_ℓ p_ℓ(c)/(1−p_ℓ(c)))
≤ Σ_ℓ ℓ^{−α}p_ℓ(c)/(1−p_ℓ(c))`. The identity is exact, since coordinates
factor. If `p_ℓ(c) ≤ 1/4` (as in Theorem 2.5), this is at most
`(4/3)Σ_ℓ p_ℓ(c)ℓ^{−α}`. So
Theorem 5.5 reproduces the Rankin functional for Λ²-majorants. Theorem 2.5
already covers *all* majorants of slice systems.

**Proposition 5.7 (derivative formula; PROVED).** Take a slice prime ℓ.
Condition on all other coordinates of both copies ("the rest"). Let `F, F'`
be the sets of residues at ℓ that would complete some condition in copy 1
and copy 2 respectively, and `p = |F|/ℓ`, `p' = |F'|/ℓ`. Put

    Cov_ℓ = |F∩F'|/ℓ − pp',
    J_ℓ = ρ_ℓ(1 − |F∪F'|/ℓ) + (1−ρ_ℓ)(1−p)(1−p').

Then

    ∂/∂ρ_ℓ log P(A∩A'_ρ) = E[ Cov_ℓ / J_ℓ | A ∩ A'_ρ ].

Along `ρ_ℓ = t ℓ^{−α}` (t from 0 to 1, zero-cost coordinates fixed at ρ = 1),

    Ξ_A(α) = Ξ_A^{fib} + ∫₀¹ Σ_ℓ ℓ^{−α} E_{μ_t}[Cov_ℓ/J_ℓ] dt,         (5.2)

with `μ_t` the joint law conditioned on `A∩A'`. Here
`Ξ^{fib} = log(E_c P(A_c)²/(E_c P(A_c))²) ≥ 0` is the fibre-variance term.

*Proof.* Given the rest, the joint avoidance probability at ℓ is
`J_ℓ·1[rest avoids conditions not involving ℓ, in both copies]`. J is affine
in ρ_ℓ with slope `Cov_ℓ`, and dividing by `P(A∩A')` produces the
conditioned expectation. ∎

**What (5.2) suggests about balanced moduli (Assessment 5.8, heuristic).**
Bound `|F∩F'|` by a sum over pairs of conditions (C, C') through the same
residue b at ℓ. This is a union bound, so it gives an upper estimate, not an
identity. There are four parts.

* *(D) Diagonal, C = C'.* The rest of C must hold in *both* copies, which
  costs about `Π_{ℓ'∈S(C)∖ℓ}(ρ_{ℓ'} + (1−ρ_{ℓ'})/ℓ')`. The leading term,
  in which all coordinates are shared, integrates in t to `P(C)·M_C^{−α}`.
  This is the H_MS term with full-modulus cost, balanced C included.

  The lower-support terms are corrections and are not negligible
  identically. For example, a single forbidden residue mod 15 at α = 1 has
  `Ξ = 0.01015`, versus `P(C)M^{−α} = 1/225 = 0.00444`, by the exact formula
  `P(A∩A') = 1 − 2p + pΠ_i[θ_i + (1−θ_i)ρ_i]`.
* *(R) Distinct C, C' with overlapping rests.* These are partially
  ρ-suppressed and are not analysed here.
* *(O) Off-diagonal, C ≠ C' with disjoint rests.* These are not
  ρ-suppressed. Per residue b their contribution is about `θ·min(1, m_b)²`,
  where `m_b` is the expected number of conditions through (ℓ, b) with rest
  set, and θ = 1/ℓ.
  * Values b with small `m_b` contribute negligibly.
  * Values with `m_b ≳ 1` ("deadly values", e.g. `b ≡ −4D` for small D)
    behave like single-slice classes at ℓ, of cost log ℓ.

  `scripts/theta_deadly_values.py` (`data/theta/deadly_values.txt`)
  measures a first-moment surrogate. The tested moduli all have a
  *dominant* prime, since q ≤ 4000 < ℓ; balanced moduli are not sampled.
  The surrogate does not evaluate the conditioned covariance, the
  `J_ℓ^{−1}` factor, or the overlap classes. It was run at ℓ ≈ 10⁴, 10⁵,
  10⁶ with cofactors q ≤ X:
  * there are only 9–45 deadly values per prime;
  * the off-diagonal quantity `S_sq = Σ_b min(1,m_b)²` is about
    0.2–0.6·(log ℓ)², rising slowly with X (+4–20% from X=10³ to 4·10³);
  * the uncapped `Σ_b m_b`, the "sum over coordinates" mass, is about
    1–1.7·(log ℓ)² and grows like log X.

  *If* `S_sq ≪ (log ℓ)²(log λ)^{O(1)}` held for all moduli, balanced ones
  included, the off-diagonal part of Ξ would be
  `≪ Σ_ℓ ℓ^{−1−α}(log ℓ)²·polylog ≍ α^{−2}·polylog`. That is subdominant
  to the diagonal `α^{−3}`. This is a conditional Assessment; the premise is
  only tested for dominant-prime moduli.
* *(S) Small primes.* Primes below `w = λ^{3+ε}` must be treated as
  zero-cost coordinates. Otherwise they are nearly determined by the rest,
  and each contributes its full void cost. The w-smooth subsystem then
  enters through the fibre term `Ξ^{fib}` and the density of nonempty
  fibres. Its *mass* is heuristically `∫ s² ρ_Dickman(s/log w) ds
  ≪ (log w)³`, but this weighted Dickman estimate is unproved. A mass bound
  is also not a bound on the negative log void probability.

Summing, the model predicts `Ξ ≲ α^{−3}·polylog(λ)`. The cubic part comes
from the diagonal, i.e. the H_MS functional. That means saving
`≲ λ^{3/4}·polylog(λ)` for Λ²-majorants *including balanced moduli*.

**Hypothesis H_MS^{Sel}** (named; open; falsifiable). For the complete
Case-B (and Case-A) forced-class system with moduli ≤ e^λ, take the
*global* noise-stability excess of Theorem 5.5. Primes ≤ λ⁴ have ρ = 1, so
their contribution, including the fibre term `Ξ^{fib}` and the empty-fibre
density, is part of `Ξ_A`. The hypothesis is

    Ξ_A(α) ≪ α^{−3}(log λ)^{O(1)}   uniformly for λ^{−1} ≤ α ≤ 1.

Under H_MS^{Sel}, Theorem 5.5 caps Selberg-type majorants (g² with
`g ≥ 1` on A) at `λ^{3/4}(log λ)^{O(1)}` for *all* moduli, balanced
included. This is an exponent ceiling, not H_MS's precise functional.

A fibrewise version alone would not suffice. For example,
`A = {c = c₀} × Ω_large` has `Ξ = 0` in every nonempty fibre, yet
`g = 1_{c=c₀}` saves `log Q₀`.

**Missing ingredients.** These are the identified obstacles, and none is
proved here. The list is not claimed to be exhaustive; (D)'s lower-support
terms, (R), and (S) also need control.
1. *A correlation inequality.* Under the jointly conditioned law μ_t, the
   probability that the rest of a condition is set must be at most its
   unconditioned value. In an independent-indicator model (one Bernoulli per
   (prime, residue)) this is Harris/FKG: the coupled pair measure is a
   product of positively correlated binary pairs, avoidance is decreasing,
   and setups are increasing. The CRT model is one-hot per prime instead.
   One-hot laws are not FKG, so a transfer is needed.
2. *Lower bound for J.* `J_ℓ ≥ c` needs `p_ℓ, p'_ℓ ≤ 1/4` for all
   configurations of the rest, with large primes only. This fails on rare
   configurations, which need a separate tail bound.

**Why Theorem 2.7's window method does not extend directly (Assessment).**
Same-scale pairs carry cubic mass (Lemma 3.8). Windows wide enough to keep
the level charge `19α_jλ` per window affordable leave such pairs internal,
where they would have to be paid at full price. Windows narrow enough to
separate them multiply the level charge by the number of windows. Theorem 5.5
avoids both problems, because its level charge `αλ/2` is paid *once*, but
it covers only Λ²-majorants.

### 5.8 Toy LP: pair conditions versus single conditions (follow-up 2; EVIDENCE)

`scripts/theta_pair_lp.py` compares two systems on 5 coordinates:
* a *pair system*, with coordinates uniform on ℤ/5, which forbids r random
  value-pairs for each of the 10 coordinate pairs (AND-conditions, i.e.
  "balanced moduli");
* a *single system* of exactly the same mass, which forbids probability
  `p = mass/5` at each coordinate.

It gives the LP optimum over *all* majorants of level m (terms depending on
at most m coordinates), computed by floating-point HiGHS and not certified.
For the single system this is the exact polynomial LP in `Bin(5,p)` after
symmetrisation. It also gives the spectral projection bound from the proof
of Theorem 5.5, which caps Λ²-majorants only.

| system | mass | m=1 | m=2 | m=3 | m=4 | void −log P(A) |
|---|---:|---:|---:|---:|---:|---:|
| pair r=2 | 0.80 | 0.000 | 0.301 | 0.611 | 0.839 | 0.863 |
| single | 0.80 | 0.174 | 0.785 | 0.841 | 0.872 | 0.872 |
| pair r=3 | 1.20 | 0.000 | 0.446 | 0.841 | 1.256 | 1.369 |
| single | 1.20 | 0.274 | 0.978 | 1.227 | 1.369 | 1.372 |
| pair r=4 | 1.60 | 0.000 | 0.491 | 1.002 | 1.469 | 1.696 |
| single | 1.60 | 0.386 | 1.292 | 1.481 | 1.905 | 1.928 |

The Λ² spectral bounds for the pair systems at m = 2 and 4 are 0.274/0.715
(r=2), 0.364/1.042 (r=3) and 0.563/1.251 (r=4). The all-majorant LP can
exceed them, which is consistent.

In these sampled instances, at matched mass and level, the pair system
saves *less* than the single system, and nothing at level 1. In general,
pair systems *can* save at level 1. For example, on three fair bits,
forbidding 00 on every pair forces `Σx_i ≥ 2`, so the majorant
`(x₁+x₂+x₃)/2` has mean 3/4 and saving 0.288.

The pattern matches the H_MS picture, in which a pair is paid at the log of
its full modulus. No instance of balanced conditions beating
single-coordinate behaviour was found. Toy sizes cannot probe the
asymptotic regime, so this is weak evidence only.

---

## 6. What a θ > 3/4 proof must contain

These are consequences of Theorems 2.5 and 2.7, Lemmas 2.9, 3.1–3.2, 4.2 and
5.3.
1. It cannot be a CRT majorant over Case-B forced classes whose moduli all
   have a dominant prime `P(M) ≥ M^{1/(1+C)}` (C<1), at any level
   `N^{O(1)}`, with any weights (Cor 3.4, Cor 3.6). By Lemma 2.9 the same
   holds for any coefficient sum `< N` with rounding bounded by `Σ|a_i|`,
   provided the family's slice primes are `≤ N^{O(1)}`. The multiplier parts are
   arbitrary, including large primes shared between conditions. Nor can it
   be a large sieve over slice systems (Remark 2.6).
2. The following cannot improve the exponent (§§4, 5.3–5.4): both Case-B
   groupings, the exact a-frame criterion, Elliott–Halberstam, or a better
   Bonferroni/Selberg polynomial. Adding Case A cannot either, via H_A3
   (§3.7). This is PROVED as an upper bound. That these variants attain
   the same order up to constants is EVIDENCE (§2.5).
3. It needs one of:
   * (i) a joint use of *balanced* moduli (`P(M) ≤ M^{1/2+o(1)}`) that beats
     their mass (H_MS false in the relevant regime). These moduli carry
     `≫ (log x)³` supply (Lemma 3.8). For Λ²-majorants this would need
     H_MS^{Sel} to fail (§5.7);
   * (ii) multipliers larger than the slice primes, used without paying
     their lcm in level. No lower bound on that cost is proved;
   * (iii) a small-modulus admissible set R that is not of selector type
     and carries a large saving `log(Q₀/|R|)` of its own (H_MS again);
   * (iv) non-CRT arithmetic of the integers (Halász, Type I/II sums,
     moment methods), or signed cancellation in the rounding errors.
     §5.2 assesses (iv) via multiplicative slices at θ*, as a model only.

### 6.1 What the theorems exclude (added by review-theta-2)

This list is checked against the proofs of Theorems 2.5, 2.7 and Lemma 2.9.
Anything below lies outside the caps of Cor 3.4–3.6.

1. **Majorants not ≥ 0 on all of ℤ.** If ν is ≥ 0 only on [1,N], the
   relaxed LP is the exact count, since level-N classes restrict to point
   masses on [1,N]. See the scope remark of §2.4.
2. **Signed rounding.** This covers any bound exploiting cancellation in
   `Σ_{n≤N}ν − N·Eν`. It also covers any rounding bound smaller than the
   absolute coefficient sum `Σ|a_i|`, e.g. one that uses which classes meet
   [1,N] (§2.7).
3. **Non-CRT inputs.** Theorem 2.5 sees only the CRT law of residues. So
   Type I/II sums, arithmetic of `x = (p+a)/4` and Halász are outside.
   Also outside are majorants that are ≥ 1 only on the exceptional
   *primes* and use prime equidistribution beyond the selector
   coordinates. The theorems require ν ≥ 1 on the whole avoider set 𝒜.
   This is the model of "a sieve on the avoider set".
4. **Balanced moduli.** Cor 3.6 needs *every* modulus of the family to
   have `P(M) ≥ M^{1/(1+C)}` with C < 1 fixed. Excluded are:
   * families containing any balanced modulus (two or more comparable
     large primes);
   * moduli with `P(M) ∈ (M^{1/2}, M^{1/(1+C)})` for the chosen C, since
     the constants blow up as C → 1.

   This part carries `≫ (log x)³` supply (Lemma 3.8), so the exclusion is
   not cosmetic. For Λ²-majorants only, Theorem 5.5 reduces it to the open
   H_MS^{Sel}.
5. **Non-selector R.** The term `log(Q₀/|R|)` is uncontrolled. Pure
   small-modulus subsystems with large void are outside (H_MS). Cor 3.6
   handles the w₀-smooth part only because `w₀ = O_C(1)`.
6. **The prime-slice requirement of Cor 3.4.** Multiplier parts must avoid
   slice primes. Cor 3.6 removes this, but only for dominant-prime moduli.
7. **Level and size.** Cor 3.4/3.6 assume level ≤ A·log N. By Lemma 2.9
   this may be replaced by: coefficient sum < N, and family slice primes
   ≤ N^{O(1)}. Families with slice primes beyond N^{O(1)} remain formally
   outside.
8. **Large sieve.** Only Montgomery's large sieve over a slice system,
   fibre by fibre, is covered (Remark 2.6). No sequential or shared-prime
   large-sieve statement is made.

---

## 7. Replay

```
# §2: Lemma 2.2(c) grid, Rankin step, LP vs Selberg vs Lagrange table (~2 min)
uv run --with scipy python scripts/theta_sieve_limit.py
# §2: reduction steps (thinning + symmetrisation) by brute-force LP (~1 min)
uv run --with scipy python scripts/theta_reduction_check.py
# §3: S_B(x)/(x log^2 x) to 1e6; exact union masses of B-M, B-aD, Case A to 4000 (~3 s)
uv run python scripts/theta_profile.py 1000000          # -> data/theta/profile.txt
# §3.8: weighted share of balanced moduli to 1e7 (~10 s)
uv run python scripts/theta_balanced_share.py 10000000  # -> data/theta/balanced_share.txt
# §5.7: deadly values / off-diagonal quantity at l ~ 1e4..1e6 (~2 s)
uv run python scripts/theta_deadly_values.py           # -> data/theta/deadly_values.txt
# §5.8: toy LP, pair vs single conditions (~5 s)
uv run --with scipy python scripts/theta_pair_lp.py     # -> data/theta/pair_lp.txt
# §5.3: complete-system void among real primes (4 processes x ~150 s, < 100 MB each)
mkdir -p /tmp/theta
g++ -O2 -std=c++17 -o /tmp/theta_void_primes scripts/theta_void_primes.cpp
for i in 0 1 2 3; do /tmp/theta_void_primes 4000 $((10**12 + i*28000000000)) 28000000000 > /tmp/theta/void_$i.txt & done; wait
# merge: sum the 'voids' column and the prime counts (see data/theta/void_primes_Q4000.txt header)
```
