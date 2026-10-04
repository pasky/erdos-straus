# EXCEPTIONAL_TWIN3 — the cross-label hypothesis (H_O^≠) (task O5)

Status: **checkpoint 1 (task O5): (H_O) proved, so TW2 Cor 5.2 is unconditional (internal check only; awaiting parent review).** Labels follow
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
3. *Lenstra / Coppersmith–Howgrave-Graham–Nagaraj.* When `km ≤ j^{1−ε}`
   there are O(1) divisors of A² per class mod j, so `max_r v_j(r) ≪ log L`.
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
constant `C₀ ≥ 6`.

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
`q ≤ (2y)^{B+2}` holds because `km ≤ j^B ≤ (2y)^B`. With `y_i = 2^{i−1}m`,

    Σ_{j>m} j^{−1−α}τ(A²) ≪ (km/φ(km)) Σ_{i≥0} y_i^{−α}(log 2kmy_i)²
                         ≪ (k/φ(k)) m^{−α} (a²/α + a/α² + 1/α³),

with `a = log(2km²) ≪ log 2k + log m`, using `m/φ(m) ≤ 2` and TW2 §4's
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

Cover `(M₁, X]` by at most 2L dyadic blocks `(y,2y]` with `y ≥ M₁/2 > q`.
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
`X ≥ j`. With all variables in `[1,X]` and prime to j, put

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
reduced fractions) and divisible by j. So `max(u,v)·max(u′,v′) ≥ j/2`, and
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

**Theorem 4.1 ((H_O), hence (H_O^≠); PROVED).** In Setting 3.0,

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
* The proof never separates same-label from cross-label pairs. TW2 Lemma 5.4
  ((H_O^=)) is used only for its prime-power reduction and its k-sum
  bookkeeping. The cross-label part (H_O^≠) is not attacked separately: it
  is absorbed into the two bounds above.
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
  mod 4·(the two short variables) avoids that. This needs the largest of
  u, v, t to be `≥ A^{1/3}`, which holds once `m > (kj)^{C₀}`; smaller
  partners are handled by the quarantine `min(x,1)² ≤ x`.

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
* (2.1) holds in every row, with a factor 5–13 to spare.
* What is *not* tested: the Brun–Titchmarsh constant of Lemma 3.1 (it is
  asymptotic: `log L` at `y/q ≥ w₂/16`), the fibre law P, and k > 1.

## Replay

```
# Lemma 3.2 table (~3 min, < 1 GB)
uv run --with numpy python scripts/twin3_short_sums.py 600 101 1009 10007
# §5 system table (X = 1e9: ~10 min, ~1.3 GB for the spf sieve to 2.5e8)
uv run --with numpy python scripts/twin3_system.py 1e9 1 1009 10007 100003
```
