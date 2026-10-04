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
