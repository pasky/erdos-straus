# EXCEPTIONAL_TWIN3 — the off-diagonal term (H_O) of the two-prime Λ² cap (task O5)

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| (2.1), Lemma 2.1 | small partners `m ≤ (kj)^{C₀}`: paid for by their first moment, `≪ α^{−3}(log L)^{O(1)}` | PROVED (review: SOUND) |
| Lemma 3.1 | largest-variable reduction; Brun–Titchmarsh over the prime partner | PROVED (SOUND) |
| Lemma 3.2, Cor 3.3 | second moments of the short sums; `Σ_a V² ≪ (log L)^6` | PROVED (SOUND) |
| Lemma 3.4 | large-partner part `≪ (log L)^{O(1)}` | PROVED (SOUND) |
| **Thm 4.1, Cor 4.2** | **(H_O) holds, so TW2 Cor 5.2 (two-prime Λ² cap `≪ L^{3/4}(log L)^{O(1)}`) is unconditional** | PROVED (SOUND after repair E5) |
| (H_O^≠), (H_O^=) as un-quarantined pair sums; H_div | no longer needed for Cor 5.2 | **bypassed, open as stated** (review E5) |
| Lemmas 6.1, 6.2 | any-arity noise stability with codegree stars; free codegree quarantine | PROVED (internal; not yet reviewed) |
| Prop 6.3, 6.4 | ≥ 3 large primes reduced to star sums; ternary case proved except one residual | reduction PROVED (internal); residual OPEN |

Review: `reviews/exceptional-twin3-review.md` (branch `side-agent/review-twin3`;
repairs E1–E8 applied).

Earlier status lines:
* §§1–5: (H_O) proved, so TW2 Cor 5.2 is unconditional.
* §6: the noise-stability input holds for any arity (Lemmas 6.1–6.2,
  PROVED). The full ES family (≥ 3 large primes) is reduced to arithmetic
  star sums (Prop 6.3); the residual (3a)–(3c) is OPEN.
* §6.3 (checkpoint 3), ternary moduli: everything is reduced to one
  residual, namely balanced partner primes × balanced divisor triples
  (BFI range). Labels follow
`DISCOVERIES.md`. Notation follows `EXCEPTIONAL_TWIN2.md` (TW2), Setting 3.0:
`L = log X`, `w₂ = L^8`, `α = L^{−1/4}`, `ρ_j = j^{−α}`, fibre law P (TW2 §3),
`A = (M+1)/4`, binary moduli `M = kjm` (k w₂-smooth, j, m primes `> w₂`).

## 1. Setup

**What is open (TW2 §5).** Theorem 5.1 bounds the two-prime Λ² saving by
`C_B L^{3/4}(log L)^C + 11 E_P Σ_{j>w₂} ρ_j S_j(c)`, with
`S_j = Σ_a ν_j(a) min(deg_c(j,a),1)²`. Corollary 5.2 (cap `≪ L^{3/4}(log L)^{O(1)}`)
needs

    (H_O)   E_P Σ_{j>w₂} ρ_j S_j(c) ≪_B α^{−3}(log L)^{O(1)}.

TW2 Lemma 5.4 proves the same-candidate part (H_O^=) and splits off the
prime-power classes. What remains (TW2 §5.1, as redefined after review D7):

**(H_O^≠) (OPEN in TW2).** Take pairs of active binary classes through j
that agree mod j and whose candidate-rational sets `{4D, D/A, 1/(4D̄)}`
are disjoint. Then

    E_P Σ_{j>w₂} ρ_j j^{−1} Σ_{such pairs} x_C x_{C′} ≪ α^{−3}(log L)^{O(1)}.

**H_div (TW2 §5.5, cleanest form; OPEN in TW2).** Put `w_j(A) = j/A` for
`A ≡ 4^{−1} (mod j)`, `A ≤ X`, and
`v_j(r) = Σ_A w_j(A)·#{D | A² : λ(D) light, D ≡ r (mod j)}`. Then

    Σ_{j>w₂} (ρ_j/j) Σ_{r mod j} v_j(r)² ≪ L^{3/4}(log L)^{O(1)},

where pairs sharing a candidate rational are removed.

**What averaging is allowed.** Only the ρ-weighted average over j is needed,
not a bound for each j. Three facts about the weights matter:
* `ρ_j = j^{−α}` is `≥ L^{−C}` only for `log j ≤ C L^{1/4} log L`. Above that
  range the trivial bound `S_j ≤ w_j` is enough. So effectively
  `j ≤ X^{o(1)}`.
* `Σ_{j>w₂} ρ_j/j ≍ log L`, but `Σ_{j>w₂} ρ_j (log j)^i/j ≍ (i−1)! α^{−i}`.
  So for each j the budget is `(log j)^2` times a polylog, plus `(log L)^{O(1)}`
  for j-uniform bounds.
* S_j is quarantined: `min(deg,1)² ≤ deg`. Any sub-family of classes whose
  *first moment* `E_P Σ_j ρ_j w_j^{sub}` is `≪ α^{−3}(log L)^{O(1)}` needs no
  equidistribution input at all. This holds, for example, for partners
  `m ≤ (kj)^{O(1)}`, whose divisor mass is `≍ (log kj)^3`, not `L^3`.
Activity in the fibre is handled as in TW2 Lemma 5.4(ii): it costs
`Γ(lcm)/lcm`, then AM–GM over `(k,k′)`. We may also drop the primality of
j and m where only upper bounds are needed.

**Candidate routes (one sentence each).**
1. *Small/large partner split.* Classes with `m ≤ (kj)^C` are handled by
   their first moment (Shiu along the top prime, as in TW2 Lemmas 4.1/5.4).
   For `m > (kj)^C`, write `D | A²` as `A = uvt`, `D = u²t`. The largest of
   u, v, t is `≥ A^{1/3}`, which is long enough for Brun–Titchmarsh over the
   prime m in a class mod 4·(product of the other two). The residue mod j
   then depends only on the two short variables. So everything reduces to
   second moments of explicit two-variable sums `Σ_{v²t≡c (j)} 1/(vt)` and
   `Σ_{u/v≡ρ (j)} 1/(uv)`, which elementary box counting controls.
2. *Multiplicative characters mod j.* `Σ_{D|A²} χ(D)` is multiplicative in
   A (`1+χ(p)+χ(p)²` at p). Fourth moments of `L(1,χ)` then give the
   mean square over χ. The difficulty is the short A-ranges `m ≈ w₂`.
3. *Lenstra / Coppersmith–Howgrave-Graham–Nagaraj (heuristic; not proved
   here and not used).* Plausibly (via CHN, since `A² ≤ j^{4−2ε}`), when
   `km ≤ j^{1−ε}` there are O(1) divisors of A² per class mod j, so `max_r v_j(r) ≪ log L`.
   Against the first moment `(log j)^2 log L` this already fits the
   `α^{−3}` budget.
4. *Large sieve / Barban–Davenport–Halberstam in j.* Use this only if route
   1 leaves a residual with a fixed sequence across j.
5. *Weil bounds for incomplete sums of `c·x^{−2} mod j`.* Use this only if
   the elementary box count in route 1 turns out too weak.

Route 1 is tried first (§2 onward).

## 2. Small/large partner split; first moment of the small part

Throughout, only classes with `u = v = 1` (moduli `M = kjm`, `j ≠ m` primes
`> w₂`, k w₂-smooth) are treated. The prime-power classes are split off as
in TW2 Lemma 5.4 (D5): `S_j ≤ S_j^{(11)} + 3w_j^{pp}`, with
`E_PΣ_jρ_jw_j^{pp} ≪ L³/w₂ + w₂^{−1/2}(log L)^{O(1)}`. Fix an absolute
constant `C₀ ≥ 6` (`C₀ ≥ 5` suffices for Lemma 3.1; review E8).

**Definition.** A binary class `−4D mod kjm` through j is *small* (at j) if
`m ≤ (kj)^{C₀}`, *large* if `m > (kj)^{C₀}`. Write `deg_c(j,a) = x(a) + z(a)`
for the parts coming from small and large active classes. Let `w_j^{sm}(c)`
be the binary mass at j of the small active classes.

Since `min(x+z,1) ≤ min(x,1) + z` and `min(x,1)² ≤ x`,

    S_j^{(11)} ≤ 2 Σ_a ν_j(a) x(a) + 2 Σ_a ν_j(a) z(a)² = 2 w_j^{sm}(c) + 2 Σ_a ν_j(a) z(a)².   (2.1)

This holds with no restriction on labels. Pairs sharing a candidate,
deadly values and cross pairs are all included. The z-part is §3.

**Lemma 2.1 (first moment of the small part; PROVED).** In Setting 3.0,

    E_P Σ_{j>w₂} ρ_j w_j^{sm}(c) ≪_{B,C₀} α^{−3}(log L)^{O(1)}.

*Proof.* On supp P we have `ν ≤ (8/7)U` (unary densities ≤ 1/8). By TW2
Lemma 3.2(1), a class `−4D mod kjm` is active with probability `≤ 4Γ(k)/k`,
and each modulus carries at most `τ(A²)` classes. So the left side is at
most `4(8/7)² Σ_k (Γ(k)/k) Σ_j (ρ_j/j) Σ_{m small} τ(A_{kjm}²)/m`. Split
by which prime is on top.

*(a) `m < j` (j top).* The B-hypothesis `M ≤ j^{1+B}` gives `km ≤ j^B`.
Swap the sums: we need `Σ_{m>w₂} m^{−1} Σ_{j>m} j^{−1−α} τ(A²)`. Since A is
linear in j, apply TW2 Lemma 3.3 with `q = km`, the variable j running over
all integers, on dyadic blocks `(y,2y]` with `y ≥ m/2`. Its hypothesis
`q ≤ (2y)^{B+2}` is only needed on non-empty blocks. There some j in the
block satisfies `km ≤ j^B ≤ (2y)^B`. Blocks with `km > (2y)^B` contain no
admissible j and are dropped (review E1). With `y_i = 2^{i−1}m`,

    Σ_{j>m} j^{−1−α}τ(A²) ≪ (km/φ(km)) Σ_{i≥0} y_i^{−α}(log 2kmy_i)²
                         ≪ (k/φ(k)) m^{−α} (a²/α + a/α² + 1/α³),

with `a = log(2km²) ≪ log 2k + log m`. This is an upper bound for
`log(2km·y_0)` since `y_0 = m/2`. The step uses `(m/2)^{−α} ≤ 2m^{−α}`,
`m/φ(m) ≤ 2`, and TW2 §4's
`Σ_t (a+t log 2)² 2^{−αt} ≪ a²/α + a/α² + 1/α³`. Now sum over primes
`m > w₂`, using `Σ_m m^{−1−α}(log m)^i ≪ (i−1)!α^{−i}` for `i ≥ 1` and
`≪ log L` for `i = 0`. The result is
`≪ (k/φ(k))(log 2k)² α^{−3} log L`.

*(b) `j < m ≤ (kj)^{C₀}` (m top).* The B-hypothesis gives `kj ≤ m^B`. Fix
j and apply TW2 Lemma 3.3 with `q = kj` and variable m on dyadic blocks
`(y,2y]`, `j/2 ≤ y ≤ (kj)^{C₀}`. The hypothesis `q ≤ (2y)^{B+2}` holds.
Each block contributes `Σ_{m∈(y,2y]} τ(A²)/m ≪ (kj/φ(kj))(log 2kjy)²
≪ (k/φ(k))(C₀+2)²(log 2kj)²`, and there are at most `2C₀ log 2kj` blocks.
Hence `Σ_{m small, m>j} τ(A²)/m ≪_{C₀} (k/φ(k))(log 2kj)³`, and

    Σ_j (ρ_j/j)(log 2kj)³ ≤ 4Σ_{j>w₂} j^{−1−α}((log 2k)³ + (log j)³) ≪ (log 2k)³ log L + α^{−3}.

(Primality of m was not used in (b), which is an upper bound.)

*Sum over k.* Both cases give `≪ (k/φ(k))(log 2k)³ α^{−3} log L`, and
`Σ_k Γ(k)(log 2k)³/φ(k) ≪ (log L)^{O(1)}` by TW2 (3.1). ∎

**Remark 2.2.** Lemma 2.1 covers every class whose top prime is j, and also
the m-top classes with `m ≤ (kj)^{C₀}`. The budget `α^{−3}` is used in
full. It comes from `Σ_j ρ_j(log j)^3/j`: the divisor mass of these classes
is `(log kj)^3`, not `L^3`. Only the large classes, with
`A ≥ (kj)^{C₀+1}/4`, need equidistribution mod j (§3).

## 3. The large classes: reduction to two-variable sums mod j

Fix a prime `j > w₂` and an odd w₂-smooth k with `(k,j) = 1`. Let 𝓜 be the
set of primes `m > (kj)^{C₀}` with `kjm ≤ X` and `kjm ≡ 3 (mod 4)`. For
`a mod j` put

    V(a) = V_{j,k}(a) = Σ_{m∈𝓜} m^{−1} #{D | A_m² : −4D ≡ a (mod j)},   A_m = (kjm+1)/4.

This counts every class, with no activity, label or family restriction, so
it is an upper bound.

**Parametrisation (TW2 Lemma 5.3).** The divisors `D | A²` correspond
bijectively to the triples `(u,v,t)` of positive integers with `A = uvt`,
`(u,v) = 1`, `D = u²t` (`D/A = u/v` in lowest terms, `t = A/(uv)`); then
`D̄ = A²/D = v²t`. All of u, v, t are prime to kj, because `4A ≡ 1 (mod kj)`.
Since `4uvt ≡ 1 (mod j)`,

    −4D ≡ −u/v ≡ −1/(4v²t) (mod j),   and   −u/v ≡ −4u²t (mod j).        (3.1)

**Lemma 3.1 (largest-variable reduction; PROVED).** For L large, every `a mod j` satisfies

    V(a) ≤ 2 log L · [R₁(a) + R₂(a) + R₀(a)],
    R₁(a) = Σ_{(u,v)=1, −u/v ≡ a} 1/φ(uv),
    R₂(a) = Σ_{−1/(4v²t) ≡ a} 1/φ(vt),
    R₀(a) = Σ_{−4u²t ≡ a} 1/φ(ut),

where all variables are positive integers `≤ X`, prime to j.

*Proof.* Assign each triple of a class counted in V(a) to its largest
coordinate, breaking ties in the order t, u, v. The largest coordinate ψ
satisfies `ψ³ ≥ A ≥ (kj)^{C₀+1}/4`.

*t largest.* By (3.1) the residue is `−u/v`, so it depends only on `(u,v)`.
Fix the coprime pair `(u,v)` and put `q = 4uv`. The triples with these u, v
correspond bijectively to the `m ∈ 𝓜` with `q | kjm+1` and
`A_m ≥ uv·max(u,v)`. The first condition is one reduced class of m mod q.
The second gives `m > M₁ := max((kj)^{C₀}, (4uv·max(u,v) − 1)/kj)`. Then
`M₁ ≥ q·w₂/8`:
* if `max(u,v) ≥ (kj)²`, then `M₁ ≥ q·kj − 1`;
* otherwise `q < 4(kj)^4` and `M₁ ≥ (kj)^{C₀} ≥ q(kj)^{C₀−4}/4`.

Cover the range `(M₁, X/(kj)]` of m by at most 2L dyadic blocks `(y,2y]`
with `y ≥ M₁/2 > q`: the first block is `(M₁/2, M₁]` (which only adds
terms), and ℓ₀ below is computed at `y = M₁/2` (review E3).
Brun–Titchmarsh in the Montgomery–Vaughan form
(`π(x+y;q,b) − π(x;q,b) < 2y/(φ(q)log(y/q))` for `y > q`) gives

    Σ_{m} 1/m ≤ (2/φ(q)) Σ_{i=0}^{2L} 1/(ℓ₀ + i log 2) ≤ (2/φ(q))(1 + 1.5 log(1+2L)) ≤ 4 log L/φ(q),

where `ℓ₀ = log(M₁/(2q)) ≥ log(w₂/16) ≥ 1`. Finally `φ(4uv) ≥ 2φ(uv)`.

*u largest.* By (3.1) the residue is `−1/(4v²t)`, so it depends only on
`(v,t)`. Fix `(v,t)` and drop the coprimality of u and v (an upper bound).
Each m with `vt | A_m` gives at most one triple, namely `u = A_m/(vt)`, and
`u ≥ max(v,t)` gives `A_m ≥ vt·max(v,t)`. The same argument with
`q = 4vt` gives the bound `2 log L/φ(vt)`.

*v largest.* By (3.1) the residue is `−4u²t`. The argument with `q = 4ut`
gives `2 log L/φ(ut)`. ∎

The point of the lemma is that the large partner m is now spent: the
residue mod j depends only on the two *short* variables, and each of them
carries the harmonic weight `1/φ`. No equidistribution of divisors of
`A_m` over m was used. Only Brun–Titchmarsh in the class of m mod 4·(the
short product) was needed, and this class is long because `ψ ≥ A^{1/3}`.

**Lemma 3.2 (second moments of the short sums; PROVED).** Let j be prime and
`X ≥ 2` (`X ≥ j` is not needed). With all variables in `[1,X]` and prime to j, put

    r₁(ρ) = Σ_{(u,v)=1, u ≡ ρv (j)} 1/(uv),      r(c) = Σ_{v²t ≡ c (j)} 1/(vt).

Then

    Σ_{ρ mod j} r₁(ρ)² ≤ ζ(2)² + C(log X)²((log X)²/j + (log j) j^{−1/2}),
    Σ_{c mod j} r(c)²  ≤ ζ(2)²ζ(3)² + C(log X)²((log X)²/j + (log j) j^{−1/3}),

with C absolute.

*Proof.* **The function r.** Write `N = v²t` and `ϱ(N) = Σ_{v²t=N} 1/(vt)`.
Then `Σ_c r(c)² = Σ_{N≡N′ (j)} ϱ(N)ϱ(N′)`. We bound the diagonal and the
off-diagonal separately.

*Diagonal `N = N′`.* Write `v = ga`, `v′ = gb` with `(a,b) = 1`. Then
`a²t = b²t′` forces `t = b²s` and `t′ = a²s`. The weight is
`1/(g²a³b³s²)`, so the diagonal is at most `ζ(2)²ζ(3)²`.

*Off-diagonal `N < N′`.* Here `N′ ≡ N` and `N′ > N ≥ 1`, so `N′ > j`. The
off-diagonal part is therefore at most

    2 Σ_N ϱ(N) · sup_c Σ_{N′≡c, N′>j} ϱ(N′),   with Σ_N ϱ(N) ≤ (1+log X)².

For the sup, cover `[1,X]²` by dyadic boxes `v ∈ [V,2V)`, `t ∈ [T,2T)`;
only boxes with `V²T > j/8` meet `{v²t > j}`. In a box:
* for fixed v, t lies in one class mod j, so the box has `≤ V(T/j+1)` points;
* for fixed t, `v² ≡ c/t` has `≤ 2` roots mod j, so the box has
  `≤ 2T(V/j+1)` points.

So the box has `≤ 2VT/j + 2min(V,T)` points, each of weight `≤ 1/(VT)`, and
contributes `≤ 2/j + 2/max(V,T)`. There are `≤ (2+log₂X)²` boxes. Those with
`max(V,T) = M` number `≤ 2log₂M + 2` and need `M³ ≥ V²T > j/8`. Hence

    sup_c Σ_{N′≡c,N′>j} ϱ(N′) ≤ 2(2+log₂X)²/j + Σ_{M=2^i > (j/8)^{1/3}} (4i+4)/2^i ≪ (log X)²/j + (log j) j^{−1/3}.

**The function r₁.** The diagonal is `Σ 1/(uv)² ≤ ζ(2)²`. Two distinct
coprime pairs with `u ≡ ρv`, `u′ ≡ ρv′` have `uv′ − u′v` nonzero (distinct
reduced fractions) and divisible by j. So `max(u,v)·max(u′,v′) ≥ |uv′−u′v| ≥ j`, and
one of the two pairs has height `max ≥ (j/2)^{1/2}` (TW2 Lemma 5.5).
Charge each unordered pair to such a member. The off-diagonal is then at
most `2(1+log X)² sup_ρ Σ_{u≡ρv, max(u,v) ≥ (j/2)^{1/2}} 1/(uv)`. In a
dyadic box `[U,2U)×[W,2W)`, fixing u fixes v mod j and vice versa, so the
box holds `≤ UW/j + min(U,W)` points and contributes
`≤ 1/j + 1/max(U,W)`. Boxes meeting the height condition have
`max(U,W) ≥ (j/8)^{1/2}`. Summing as before gives
`≪ (log X)²/j + (log j) j^{−1/2}`. ∎

**Corollary 3.3 (PROVED).** For L large, `j > w₂ = L^8`, k as above, and
`X = e^L`:

    Σ_{a mod j} V_{j,k}(a)² ≤ C (log L)^6.

*Proof.* `n/φ(n) ≤ 2 log L` for `n ≤ X` and L large, and
`φ(xy) ≥ φ(x)φ(y)`. So `R₁(a) ≤ (2log L)² r₁(−a)`. The map `a ↦ c`
(`c = −1/(4a)` for R₂, `c = −a/4` for R₀) is a bijection of the nonzero
residues, so `R₂(a) ≤ (2log L)² r(c)`, and likewise for R₀. By Lemma 3.1
and `(x+y+z)² ≤ 3(x²+y²+z²)`,
`Σ_a V(a)² ≤ 3(2log L)^6 [Σ_ρ r₁(ρ)² + 2Σ_c r(c)²]`. By Lemma 3.2 with
`j > L^8`, the bracket is `≤ ζ(2)²ζ(3)²·3 + C L²(L^{−6} + 8(log L) L^{−8/3}) ≪ 1`. ∎

So for large partners the mass at each vertex is spread out: although
`Σ_a V(a) ≍ L² log L`, the second moment is only polylogarithmic. This
includes the hub vertices (deadly values) and every pair sharing a label.

**Lemma 3.4 (the large part of (2.1); PROVED).** In Setting 3.0,

    E_P Σ_{j>w₂} ρ_j Σ_a ν_j(a) z(a)² ≪ (log L)^{O(1)}.

*Proof.* A class kjm with `u = v = 1` constrains `y_j` only mod j. So
`z(a)` depends only on `a mod j`. Summing ν_j over the lifts of a residue
mod j gives at most `(8/7)/j` on supp P (unary density ≤ 1/8). The same
holds for vertices modulo `j^{e_j}`, as in TW2 Lemma 5.4. Also
`ν_m ≤ (8/7)/m`, and the probability that two classes with cofactors
`k, k′` are both active is `≤ 4Γ(lcm)/lcm` (TW2 Lemma 3.2(1)). Hence, with
`V_{j,k}` from §3 (which counts all classes, active or not),

    E_P Σ_a ν_j(a) z(a)² ≤ 4(8/7)³ j^{−1} Σ_{a mod j} Σ_{k,k′} (Γ(lcm)/lcm) V_{j,k}(a) V_{j,k′}(a)
                        ≤ 4(8/7)³ j^{−1} Σ_k (Γ(k)h(k)/k) Σ_a V_{j,k}(a)².

The second line is AM–GM, with
`Σ_{k′}Γ(lcm(k,k′))/lcm(k,k′) ≤ Γ(k)h(k)/k` (TW2 Lemma 5.4(ii)). By
Corollary 3.3, `Σ_a V_{j,k}(a)² ≤ C(log L)^6` uniformly in j and k. Then
`Σ_k Γ(k)h(k)/k ≪ (log L)^{O(1)}` (TW2 Lemma 5.4(iii)) and
`Σ_{j>w₂} ρ_j/j ≪ log L`. ∎

## 4. Assembly: (H_O) holds; the two-prime Λ² cap is unconditional

**Theorem 4.1 ((H_O); PROVED).** In Setting 3.0,

    E_P Σ_{j>w₂} ρ_j S_j(c) ≪_B α^{−3}(log L)^{O(1)}.

*Proof.* `S_j ≤ S_j^{(11)} + 3w_j^{pp}` (TW2 Lemma 5.4, D5), and the
prime-power part is `o(1)` there. Then `S_j^{(11)}` is bounded by (2.1),
Lemma 2.1 (`≪ α^{−3}(log L)^{O(1)}`) and Lemma 3.4 (`≪ (log L)^{O(1)}`). ∎

**Corollary 4.2 (TW2 Cor 5.2 made unconditional).** In Setting 3.0
(ℛ(M)-families, `M ≤ X`, `M ≤ P(M)^{1+B}`, at most two prime factors above
`w₂ = (log X)^8`, twins included), every admissible Λ² majorant g of level
`λ ≤ A₀L` has `saving(g²) ≪_{A₀,B} L^{3/4}(log L)^{O(1)}`.

*Proof.* TW2 Theorem 5.1 together with Theorem 4.1. ∎

**Remarks.**
* **(H_O^≠) is bypassed, not proved (review E5).** In TW2, (H_O^=) and
  (H_O^≠) are *un-quarantined* pair sums (parts of `q_j = Σ ν deg²`), and
  the route was `S_j ≤ q_j`. So (H_O^=) + (H_O^≠) ⇒ (H_O), not
  conversely. Here `q_j` is bounded only for large–large pairs
  (Lemma 3.4). Small–small and small–large pairs are paid for through
  `min(x,1)² ≤ x`, which says nothing about `Σ x_C x_{C′}`. Hence
  (H_O^≠) and H_div, as stated in TW2 §5 and §1 here, remain **open as
  stated**. They are no longer needed for Cor 5.2. TW2 Lemma 5.4 is used
  only for its prime-power reduction and its k-sum bookkeeping.
* H_div (TW2 §5.5) was only a sufficient condition and is bypassed. Its
  weights `j/A` include all `A ≡ 4^{−1} (j)` down to `A ≍ j`, where `j/A ≍ 1`.
  The real system has `j/A ≍ k/m ≤ k/w₂`, and the quarantine lets small
  partners be paid for by their first moment.
* Where the budget goes. The `α^{−3}` comes only from Lemma 2.1, i.e. from
  `Σ_j ρ_j (log j)³/j`: the divisor mass of classes whose partner is at
  most polynomial in kj. The large partners cost only `(log L)^{O(1)}`. So
  this route does not lower the exponent 3/4. The cap `L^{3/4}` is the
  diagonal/unary scale (TW2 Lemma 4.1) in any case.
* Why this was missed (TW2 §5.4–5.5). The obstacle there was the
  j-dependence of the first-element masses `1/m₀(θ,k)` once the divisor
  side is summed first. Summing over the partner prime first in the class
  mod 4·(the two short variables) avoids that. The largest of u, v, t is
  always `≥ A^{1/3}`. What `m > (kj)^{C₀}` buys is `M₁ ≥ q·w₂/8`: the
  Brun–Titchmarsh range for m is longer than the modulus
  `q = 4·(short product)`, which can be as large as `≈ 4(kj)^4` (review
  E8). Smaller partners are handled by the quarantine `min(x,1)² ≤ x`.

## 5. Numerics (EVIDENCE, toy scale)

**Lemma 3.2** (`scripts/twin3_short_sums.py`, Y = 600: all variables are at
most Y, so `X = Y`). The bound columns are `ζ(2)²ζ(3)² = 3.91` and
`ζ(2)² = 2.71`.

| j | Σr | Σr² | diag | off | rand | Σr₁ | Σr₁² | diag₁ | off₁ | rand₁ |
|---|---|---|---|---|---|---|---|---|---|---|
| 101 | 48.3 | 25.5 | 3.81 | 21.7 | 23.1 | 33.8 | 12.8 | 2.50 | 10.3 | 11.3 |
| 1009 | 48.7 | 5.94 | 3.81 | 2.13 | 2.35 | 34.1 | 3.23 | 2.50 | 0.739 | 1.150 |
| 10007 | 48.7 | 3.96 | 3.81 | 0.151 | 0.237 | 34.1 | 2.54 | 2.50 | 0.040 | 0.116 |

The diagonals sit at the proved constants. The off-diagonals are *below*
the random prediction `(Σ)²/j` in every row; the proof's bound
`L²(L²/j + j^{−1/3}log j)` is far from tight.

**Corollary 3.3 and (2.1) on the real system** (`scripts/twin3_system.py`,
X = 1e9, k = 1, every prime partner `m ≥ 3`, all `D | A²`, no fibre). This
is a toy test: `C₀ = 1` (small means `m ≤ j`), whereas the proof needs
`C₀ ≥ 6` and `j > L^8`, which is out of numerical reach. Column V2 is
`Σ_a V(a)²`.

| j | small: mass | V2 | max | rand | large: mass | V2 | max | rand | `Σmin(V,1)²` | (2.1) RHS |
|---|---|---|---|---|---|---|---|---|---|---|
| 1009 | 36.3 | 7.14 | 1.13 | 1.30 | 48.5 | 3.66 | 0.46 | 2.33 | 15.4 | 79.8 |
| 10007 | 58.8 | 5.63 | 0.95 | 0.35 | 20.5 | 0.18 | 0.14 | 0.04 | 7.3 | 118.0 |
| 100003 | 109.2 | 17.1 | 1.17 | 0.12 | 0 | 0 | 0 | 0 | 16.4 | 218.3 |

Reading:
* The large-partner second moment is O(1) and falls with j, while its mass
  is 20–50. This is the spreading claimed by Cor 3.3, in which `Σ_a V²` is
  polylogarithmic although `Σ_a V ≍ L² log L`.
* The small part has `Σ V² ≫ (Σ V)²/j`, because of the deadly values (here
  m starts at 3, so the hubs carry weight up to 1/3). That is why §2 pays
  for it with its first moment and no equidistribution claim.
* (2.1) holds in every row, with a factor 5–16 to spare (79.8/15.4,
  118.0/7.3, 218.3/16.4; review E6).
* What is *not* tested: the Brun–Titchmarsh constant of Lemma 3.1 (it is
  asymptotic: `log L` at `y/q ≥ w₂/16`), the fibre law P, and k > 1.

## Replay

```
# Lemma 6.1/6.2 exact check (3 seeds x 400 trials, ~1 min each, < 1 GB)
for s in 1 2 3; do uv run --with numpy python scripts/twin3_kary_check.py 400 $s; done
# Lemma 3.2 table (~3 min, < 1 GB)
uv run --with numpy python scripts/twin3_short_sums.py 600 101 1009 10007
# §5 system table (X = 1e9: ~10 min, ~1.3 GB for the spf sieve to 2.5e8)
uv run --with numpy python scripts/twin3_system.py 1e9 1 1009 10007 100003
```

## 6. Three or more large primes (task O5, part 2)

### 6.1 Arbitrary arity: noise stability with codegree terms

**Setting 6.0.** This is Setting 1.0 of TW2 with *events* in place of edges.
An event E is a partial assignment `E = {(ℓ, c_E(ℓ)) : ℓ ∈ S(E)}`,
`|S(E)| ≥ 2`, and it *occurs* at y iff `y_ℓ = c_E(ℓ)` for all `ℓ ∈ S(E)`.
Put `π_E = Π_{ℓ∈S(E)} ν_ℓ(c_E(ℓ))` and `w_ℓ = Σ_{E: ℓ∈S(E)} π_E`. A *star*
σ is a nonempty partial assignment contained in some event. Let `V(σ)` be
its coordinate set, `π_σ = Π_{(ℓ,c)∈σ} ν_ℓ(c)`, and `ρ̃^{σ} = Π_{ℓ∈V(σ)} ρ̃_ℓ`.
Its *codegree mass* is

    D_σ = Σ_{E ⊇ σ} π_{E∖σ}      (π_∅ = 1).

So `D_{(ℓ,a)} = deg(ℓ,a)`, and `D_σ ≥ 1` if σ is itself an event.
Hypothesis:

    (H_δ)   Σ_{ℓ∈S(E)} w_ℓ ≤ δ ≤ 1/16 for every event E.

**Lemma 6.1 (noise stability, any arity; PROVED).** In Setting 6.0, for every
`ρ̃ ∈ [0,1]^{index}`,

    log (Z₂(ρ̃)/Z₁²) ≤ (1 + 25δ) Σ_{σ star} π_σ ρ̃^{σ} D_σ².                  (6.1)

For graph systems the stars are vertices (`D = deg`) and edges (`D = 1`).
Then (6.1) is exactly TW2 (1.2). For hyperedges the new terms are the
stars with `2 ≤ |σ| < |S(E)|`. They are the codegree hubs of
POINTWISE_OMEGA2 §10.4, which now appear as explicit squared masses.

*Proof.* We repeat TW2 Theorem 1.4 with three changes.

*(i) Local lemma.* In the doubled system each event E gives `E, E′`.
Take `x_F = 2P(F)`. Then `Σ_{F∈Γ(E)} x_F ≤ 4Σ_{ℓ∈S(E)} w_ℓ ≤ 4δ`, so the
hypothesis of TW2 Lemma 1.1 holds. For an event B depending on
`Y_ℓ, ℓ ∈ T`, part (2) gives `P(B|A_𝓢) ≤ P(B)exp(5Σ_{ℓ∈T}w_ℓ)`.

*(ii) Derivative identity.* TW2 Lemma 1.3 holds verbatim with
`F = {a : some E ∋ (j,a) has y_{S(E)∖j} = c_E}`, and likewise F′.

*(iii) Numerator.* `ν_j(F∩F′) ≤ Σ_a ν_j(a) Σ_{E,E′∋(j,a)} 1[B_{E,E′}]`,
where `B_{E,E′} = {y_{S(E)∖j} = c_E, y′_{S(E′)∖j} = c_{E′}}`. B depends on
`T = S(E)∪S(E′)∖{j}`, and `Σ_T w ≤ 2δ`, so the conditional factor is
`≤ e^{10δ}`. Let `T(E,E′)` be the set of `m ≠ j` with `c_E(m) = c_{E′}(m)`.
For each `m ∈ T(E,E′)` with common value c, the coupling gives
`P = κ_mν_m(c) + (1−κ_m)ν_m(c)² ≤ ν_m(c)²(1 + κ_m/ν_m(c))`. Every other
coordinate contributes its product of marginals, or less. Hence

    P(B_{E,E′}) ≤ π_{E∖j} π_{E′∖j} Π_{m∈T(E,E′)} (1 + tρ̃_m/ν_m(c_m))      (κ = tρ̃)
               = Σ_{U ⊆ T(E,E′)} t^{|U|} π_{E∖j}π_{E′∖j} Π_{m∈U} ρ̃_m/ν_m(c_m).

For fixed U put `σ = {(j,a)} ∪ {(m,c_m) : m ∈ U}`, a star contained in
both E and E′. Then `π_{E∖j} = π_{E∖σ} Π_{m∈U}ν_m(c_m)`, and the
`(E,E′,U)` sum is a sum over stars `σ ∋ (j,a)` of
`t^{|σ|−1} Π_{m∈U}(ρ̃_mν_m(c_m)) D_σ²`. So

    ν-numerator ≤ e^{10δ} P(A_{−j}) Σ_{σ: j∈V(σ)} t^{|σ|−1} (π_σ/ρ̃_j) ρ̃^{σ} D_σ².

*(iv) Denominator and integration.* As in TW2,
`E[ν_j(F)|A_{−j}] ≤ e^{5δ}w_j ≤ e^{5δ}δ`. Hence
`∂_{κ_j}log Z₂(tρ̃) ≤ (1+25δ) Σ_{σ∋j} t^{|σ|−1}(π_σ/ρ̃_j)ρ̃^σ D_σ²`.
Multiply by `ρ̃_j` and sum over j. Each star is then counted once from
each of its `|σ|` coordinates, and `∫₀¹ t^{|σ|−1}dt = 1/|σ|`. ∎

This proves the log-form of TW Conjecture 6.8 for arbitrary arity, *without
any codegree hypothesis*: the codegree terms are part of the bound.
Whether they are small is an arithmetic question (§6.3).

**Lemma 6.2 (free codegree quarantine by promotion; PROVED).** In Setting
6.0, call a star σ with `|σ| ≥ 2` a *codegree hub* if `D_σ > 1` and σ is
not itself an event. To *promote* σ, delete all events `E ⊇ σ` and add σ
as an event. Promote hubs repeatedly, in any order, until none is left.
This terminates in a system 𝓔⁺ with the following properties:
1. `A⁺ ⊆ A` (avoiding σ implies avoiding every `E ⊇ σ`), and every `w⁺_ℓ ≤ w_ℓ`,
   so (H_δ) persists;
2. `D⁺_τ ≤ min(D_τ, 1)` for every star τ of 𝓔⁺ with `|τ| ≥ 2`, and
   `D⁺_τ ≤ D_τ` for `|τ| = 1`. Every star of 𝓔⁺ is a star of 𝓔 (with
   `D_τ ≥ 1` if τ is a promoted event);
3. consequently

       log (Z₂⁺/Z₁⁺²) ≤ (1+25δ) [ Σ_{|σ|=1} π_σ ρ̃^σ D_σ² + Σ_{|σ|≥2} π_σ ρ̃^σ min(D_σ,1)² ],

   with D computed in the original system.

*Proof.* *Monotonicity of one promotion.* Let `τ ⊆ σ`. The new event σ
adds `π_{σ∖τ}` to `D_τ`, and the deleted events remove
`Σ_{E⊇σ}π_{E∖τ} = π_{σ∖τ}D_σ`. Since `D_σ > 1`, `D_τ` decreases. If
`τ ⊄ σ`, the new event does not contain τ, and `D_τ` can only lose terms.
The same computation with `τ = (ℓ,a)` summed over a shows that `w_ℓ` does
not increase. After the promotion `D_σ = 1`. The number of events strictly
decreases (a hub has `D_σ > 1`, hence at least two events contain it), so
the process terminates.

*Final state.* Every star τ with `|τ| ≥ 2` has one of three forms:
* τ is an event; any other event `E ⊋ τ` is redundant and is deleted
  (this does not change A⁺ and only lowers D). Then `D⁺_τ = 1`, and
  `D_τ ≥ 1` in the original system by monotonicity read backwards;
* τ is not an event, and `D⁺_τ ≤ 1` because τ is not a hub;
* in both cases `D⁺_τ ≤ D_τ` by monotonicity.

(3) follows from Lemma 6.1 applied to 𝓔⁺. The stars of 𝓔⁺ are sub-stars
of events of 𝓔⁺, which are stars of 𝓔. ∎

Together with TW2 Lemma 2.2 (unary quarantine of vertex hubs, cost
`2Σρ_ℓ(p_ℓ + S_ℓ)`), and since passing to `ν⁺` multiplies `ν_ℓ` by
`(1−p_ℓ)/(1−p⁺_ℓ) ≤ e^{2w_ℓ}` (because `p⁺_ℓ − p_ℓ ≤ w_ℓ ≤ 1/16`), so that
`π_σ` grows by at most `e^{2Σ_{V(σ)}w} ≤ e^{2δ}` under (H_δ) (uniformly in
the arity), the fibre log-ratio of any-arity class systems is
controlled by

    Σ_ℓ ρ_ℓ(p_ℓ + S_ℓ) + Σ_{|σ|≥2} e^{2δ} π_σ ρ^σ min(D_σ, 1)².              (6.2)

The edge terms of TW2 (2.1) are the stars σ that are binary events, with
`D_σ = 1`. Codegree hubs cost nothing beyond their capped square. Unlike
vertex hubs they need no change of the unary law, because promotion keeps
them as events. So the POINTWISE_OMEGA2 codegree-hub obstruction (§10.4)
does not block the Λ² route; it only produces the star sum (6.2).

*Check (EVIDENCE that the algebra is right).*
`scripts/twin3_kary_check.py` computes `log(Z₂/Z₁²)` exactly on random
hypergraph systems: 3–5 coordinates of size 3–7, events of arity 2–4, half
of them forced through a common sub-star (codegree hubs), random ν and
ρ̃. Over seeds 1–3, 1200 trials, 276 satisfy (H_δ):
* Lemma 6.1: `lhs ≤ (1+25δ)·rhs` always, with largest ratio 0.949;
* Lemma 6.2(3) after promotion: likewise, with largest ratio 0.949.

Under (H_δ), promotions rarely occur (6 of the 1200 systems promoted;
the script does not record how many of these satisfied (H_δ)). Hubs with
`D_σ > 1` need `π_σ < δ`, whereas the toy alphabets are small.

### 6.2 What changes for three or more large primes (reduction; Assessment)

**No cheap reduction to the binary case.**
* *Projection to the two largest primes* replaces a class mod `kℓ₁ℓ₂ℓ₃` by
  the class mod `kℓ₁ℓ₂` that contains it. This is monotone (avoiders
  shrink), but each event's probability grows by the factor ℓ₃, and the
  projected classes are no longer of the form `−4D′ mod M′`, `D′ | A′²`.
  Lemma 5.3's labels, Shiu on `A = (M+1)/4` and the good events of TW2
  §3 all fail.
* *Paying for ≥3-prime events unweighted* (local lemma:
  `Ξ ≤ Ξ_binary + O(Σ_{E k-ary} P(E))`) costs their total fibre mass. That
  mass has the cubic order of the whole system, far above `α^{−3}`.
* So the ρ-weighting must be kept for every arity. This is what Lemmas 6.1
  and 6.2 allow.

**Proposition 6.3 (reduction; PROVED as an implication).** Drop "at most
two primes above w₂" from Setting 3.0, keep `M ≤ P(M)^{1+B}`, and let the
fibre law P satisfy, for every `c ∈ supp P`:
* `p_ℓ(c) ≤ 1/8`;
* (H_δ) with `δ = 1/16` for the any-arity class system of c.

Then every admissible g has

    saving(g²) ≤ A₀L^{3/4}/2 + log‖dP/dU_F‖_∞ + C·E_P[ Σ_ℓ ρ_ℓ p_ℓ + Σ_ℓ ρ_ℓ S_ℓ + Σ_{|σ|≥2} π_σ ρ^σ min(D_σ,1)² ].

*Proof.* TW2 Lemma 2.1, then TW2 Lemma 2.2 (vertex quarantine; its
proof uses only `w_ℓ ≤ δ/2` and is arity-free), Lemma 6.2, and Lemma 6.1.
With the `e^{2δ}` inflation of (6.2), the constant is C = 11. ∎

**Status of each input for the full ES family (Assessment).**
1. *Fibre law and (H_δ).* TW2 §3 carries over. Its stages 1–2 use only
   w₂-smooth moduli. G_L must be strengthened to
   `w_ℓ ≤ δ·log ℓ/L` for all `ℓ > w₂`; then
   `Σ_{ℓ∈S(E)} w_ℓ ≤ δ·log M/L ≤ δ`. By Markov this needs
   `Σ_{ℓ>w₂} L²E w_ℓ²/(log ℓ)² = o(1)`. The any-arity second moment is
   `E w_ℓ² ≪ L^6(log L)^{O(1)}/ℓ²` (the TW2 Lemma 3.4 split by top prime).
   This is `o(1)` once `w₂ = L^{10}` (not with `L^8`). Raising w₂ to
   `L^{10}` leaves Lemmas 3.1–3.4 intact up to constants. **Routine; not
   written.**
2. *Unary terms and stars that are whole events* (`D_σ = 1`): these give
   `Σ_C P(C) ρ^{S(C)} ≤ Σ_C P(C) ρ_{P(M_C)}`, i.e. Shiu along the top prime
   exactly as in TW2 Lemma 4.1 (unary case, with `q = M/P ≤ P^B`), giving
   `≪ α^{−3}(log L)^{O(1)}`. **Essentially proved** (ET Lemma 3.1 and TW2
   Lemma 4.1 already cover all ℛ(M)).
3. *Vertex stars `S_ℓ` and codegree stars* `2 ≤ |σ| < |S|` (modulus
   `Q_V = Π_{ℓ∈V}ℓ`, rest `R = M/(kQ_V)` composite). The §§2–3 template
   applies with j replaced by `Q_V` and the prime partner m replaced by R.
   The residue at V is still `−u/v mod Q_V` (TW2 Lemma 5.3). There are
   two sharp points:
   * **(3a) small partners.** The first moment
     `Σ_V (ρ^V/Q_V)Σ_{R ≤ (kQ_V)^{C₀}} τ(A²)/R` is fine if R is summed with
     its w₂-rough density (`Σ_R 1/R ≍ log(kQ)/log w₂`). In the top-prime
     case this needs Shiu along the *prime* top variable (a
     Brun–Titchmarsh–Shiu bound for `τ((kRj+1)²/16)` over primes j).
     Summing j over all integers, as Lemma 2.1(a) does, loses one factor
     `1/α` once R is composite, giving `α^{−4}/log L ≈ L/log L`. A
     shifted-prime Shiu bound (sieve plus divisor switching) is standard
     in spirit but not written here.
   * **(3b) large partners.** Lemma 3.1 used Brun–Titchmarsh over the
     *prime* m. For composite R, the long-variable sum over w₂-rough R in
     a class (fundamental lemma of the sieve) has weight `≍ L/log L`
     instead of `log L`. Corollary 3.3 then needs Lemma 3.2's r-bound
     sharpened from `j^{−1/3}` to `j^{−1/2+o(1)}`. This looks feasible:
     boxes with `V²T ≤ j^{1+η}` contain at most `(8V²T/j + 1)·max τ(N)`
     points with `VT ≥ j^{1/2}`. **Not done.**
   * **(3c) the sum over V.** `Σ_{|V|=s} ρ^V/Q_V ≤ (Σ_ℓ ρ_ℓ/ℓ)^s/s! ≤ (log L)^s/s!`.
     For s large, each extra prime in V brings another factor
     `ρ_ℓ/ℓ`, so the total over s is `≤ e^{log L}·(…) = L·(…)`. That
     would be too large, unless the per-V bound decays in s. The large
     part should decay, since each pair of short variables is spread over
     `Q_V ≥ w₂^s` residues. The first-moment (small) part should be
     bounded by `Σ_C P(C)Σ_{V⊆S(C)} ρ^V·1[R_V small]`, which is again
     `2^{r}`-type. **This is the main open bookkeeping point.**

**Verdict (Assessment).** Lemmas 6.1–6.2 show that the *probabilistic*
obstruction is gone for every arity. This is TW Conjecture 6.8 in log
form, with codegree hubs costing nothing beyond their capped squares.
What separates the full ES family from Corollary 4.2 is purely arithmetic:
the star sums (3a)–(3c). The binary proof of §§2–3 is the s = 1,
prime-partner case of the same template.

### 6.3 Ternary moduli (fixed B): what the template proves, and the exact residual

Here the family is Setting 3.0 with "at most two" replaced by "at most
three" primes above w₂, and the ternary moduli are `M = kℓ₁ℓ₂ℓ₃`
(prime-power cases split off as in TW2 Lemma 5.4). The star sum of
Prop 6.3 has, per class, at most 3 vertex stars, 3 pair stars and 1 whole
event. **So (3c) is trivial for r = 3**: the factor `2^r` is 8.

**Proposition 6.4 (ternary star sums: proved parts; PROVED modulo the same
inputs as §§2–3).** In this setting, each of the following contributes
`≪_{B,C₀} α^{−3}(log L)^{O(1)}`:
1. *Pair stars* `V = {ℓ₁,ℓ₂}`: here `Q = ℓ₁ℓ₂` and the partner is the
   single prime `ℓ₃`.
2. *Vertex stars at j with a small partner* `R = ℓ_aℓ_b ≤ (kj)^{C₀}`.
3. *Vertex stars at j with an unbalanced large partner*:
   `ℓ_b > (kjℓ_a)^{C₀}` (`ℓ_a < ℓ_b`).

*Proof sketch.* All three follow the §§2–3 template line by line.

(1) Replace j by `Q = ℓ₁ℓ₂` and `ρ_j` by `ρ_{ℓ₁}ρ_{ℓ₂}`.
* *Small* `ℓ₃ ≤ (kQ)^{C₀}`: Shiu along the top prime. If it is `ℓ₁`, take
  `q = kℓ₂ℓ₃ ≤ ℓ₁^B` and get `α^{−3}` from the ℓ₁-sum, while the
  `ℓ₂, ℓ₃` sums cost `(log L)²`. If it is ℓ₃, take `q = kQ`; then
  `(log kQ)³` against `Σρ_{ℓ₁}ρ_{ℓ₂}/Q` gives `α^{−3}log L`.
* *Large* `ℓ₃`: Lemma 3.1 holds verbatim mod Q, with Brun–Titchmarsh over
  the prime ℓ₃ (`(Q,4uv) = 1`). Lemma 3.2 holds mod the squarefree Q:
  `v² ≡ c` has ≤ 4 roots mod Q, and distinct `N ≡ N′ (Q)` give `N′ > Q`.
  So `Σ_{a mod Q} V² ≪ (log L)^6`, and `Σ_{ℓ₁,ℓ₂} ρρ/Q ≪ (log L)²`.

(2) The proof of Lemma 2.1 goes through. The partner sum
`Σ_{R=ℓ_aℓ_b} 1/R ≤ (Σ_ℓ 1/ℓ)² ≪ (log L)²` is polylogarithmic because R
has exactly two primes. (The loss `1/α` of §6.2 (3a) needs an unbounded
number of partner primes.)
* j top: Shiu along j with `q = kR ≤ j^B` gives
  `Σ_R R^{−1}P(R)^{−α}(log P(R))²/α ≪ α^{−3}log L`.
* `ℓ_b` top: Shiu along `ℓ_b` with `q = kjℓ_a ≤ ℓ_b^B`, giving
  `(log kj)³·Σ1/ℓ_a`.

(3) Regard `kℓ_a` as the cofactor. Lemma 3.1 holds with `k → kℓ_a`
(`(kℓ_a, j) = 1`) and Brun–Titchmarsh over the prime ℓ_b, because
`ℓ_b > (kℓ_a j)^{C₀}`. Corollary 3.3 then gives `Σ_a V_{ℓ_a}² ≪ (log L)^6`
for each ℓ_a. Cauchy–Schwarz over ℓ_a with weights `1/ℓ_a` costs
`(Σ1/ℓ_a)² ≪ (log L)²`. Activity is handled with cofactor k only. ∎

**The exact residual (OPEN): balanced partners.** Vertex stars at j from
ternary classes with

    R = ℓ_aℓ_b > (kj)^{C₀},   ℓ_a < ℓ_b ≤ (kjℓ_a)^{C₀}.

Write `D | A²` as `A = uvt`, with ψ the largest coordinate and `q` four
times the product of the other two. Lemma 3.1's step (sum over the
partner in one class mod q) now needs the prime `ℓ_b` (ℓ_a fixed), or the
pair `(ℓ_a,ℓ_b)`, to be equidistributed in a class mod q. Two cases:
* *`ψ ≥ 8w₂(kjA)^{1/2}`, PROVED in the same way.* Then `q ≤ 4A/ψ` and
  `ℓ_b ≥ (4A/kj)^{1/2}` give `ℓ_b ≥ q·w₂`. Brun–Titchmarsh over ℓ_b for
  fixed ℓ_a applies, and Lemma 3.2 plus Cauchy–Schwarz over ℓ_a finish
  as in (3).
* *Balanced triples: all of u, v, t below `8w₂(kjA)^{1/2}`.* Then
  `q ≍ A^{1/2±}` is comparable to or larger than both partner primes. Each
  class of `ℓ_b` mod q has O(1) elements in range, so the first-element
  problem of TW2 §5.4 returns, now for products of two primes in
  progressions to moduli `q ≈ (ℓ_aℓ_b)^{1/2+}`. That is the
  Bombieri–Friedlander–Iwaniec range, where only averages over q are known.
  Here we need the average over the q's that occur (`q = 4·(two short
  divisors)`, weighted by `1/φ`), which BFI does not supply directly.

*Why the cap does not rescue it.* The first moment of this part is the
τ-mass of balanced triples, a positive proportion of `L³`. Unlike the
binary case, a composite partner keeps the τ-mass at full size
`(log A)^2` even when the partner pair is balanced.

**Size check (Assessment).** For hubs (small labels) and composite
partners, `V(hub) ≍ (log L)²/height`, so hubs saturate the cap only for
`height ≲ (log L)²`. Those vertices cost `≪ (log L)^{O(1)}/j` per j. They
are harmless; the residual is the bulk, not the hubs.
