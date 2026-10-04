# EXCEPTIONAL_TWIN3 — the cross-label hypothesis (H_O^≠) (task O5)

Status: **work in progress (step 1: setup only).** Labels follow
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
