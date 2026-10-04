# EXCEPTIONAL_TWIN4 — the Λ² cap for moduli with r large primes (task O12)

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| Thm 1.1 | k-ary noise stability (goal 1) = TW3 Lemmas 6.1 + 6.2; no codegree hypothesis; PO2 Lemma 10.2 not needed | PROVED (TW3, reviewed) |
| **Lemma 2.3**, Cor 2.4 | rough-partner Brun–Titchmarsh: `Σ_{R≡b (q), x<R≤2x, Ω(R)≤s, P⁻(R)>w} 1/R ≤ 3(s+1)ΣH^i/(φ(q)log(x/q))` (large sieve) | PROVED |
| Prop 3.1 | reduction to star sums, bounded arity, constants `e^{O(r)}` | PROVED as an implication |
| Lemma 4.1 | fibre law with `G_L^{(r)}` (`w_ℓ ≤ δ_r`); `w₂ = L^8` suffices for fixed r (closes TW3 review E11) | PROVED |
| Lemma 5.1, Cor 5.2 | whole-event stars `≪ α^{−3}(log L)^{r+O(1)}`; prime-power classes `o(1)` | PROVED |
| Lemma 5.3 | small partners, every star V | PROVED |
| **Lemmas 6.1–6.4** | large partners, every star V: largest-variable reduction with Lemma 2.3 in place of BT; box counting mod squarefree Q | PROVED |
| **ternary residual `ℓ_b < w₂q`** (goal 2) | closed by Lemma 6.1: an upper-bound sieve for the whole partner R; **no BFI input needed** | PROVED |
| **Thm 7.1** (goal 3) | Λ² cap `≪ L^{3/4}(log L)^{3r+O(1)}` for `M ≤ P(M)^{1+B}` with ≤ r primes above `(log X)^8`, r fixed | PROVED (internal; review `reviews/exceptional-twin4-review.md`: SOUND, nits F1–F4 applied) |
| Prop 9.1 | explicit r-dependence `(C_B log L)^{Cr}`: cap `L^{3/4+O(ε)}` for `r ≤ ε log L/log log L` | PROVED (bookkeeping) |
| **Lemma 9.2**, Cor 9.3 | unweighted payment for any low-mass subfamily (LLL, `x_G = 2^{|S(G)|}P(G)`); classes with `ω_L(M) ≥ 330 log L` cost `o(1)` | PROVED |
| §9.3 | middle range `ε log L/log log L < r < 330 log L` (the bulk): needs an off-diagonal second moment at short-partner stars, efficient per prime (multi-prime H_O^≠) | OPEN (sharp failure point) |
| **Lemma 10.1** | smooth-dominated sums: Cauchy–Schwarz + Rankin on smooth k + Shiu along k | PROVED |
| **Thm 10.4** | for fixed r the cap holds **without the B-hypothesis** (also with arbitrary classes having `ω_L ≥ 330 log L` added) | PROVED (internal; not yet reviewed) |
| §8 | Lemma 2.3 exact on 1228 cases (worst ratio 0.13); former residual = 80–86% of toy ternary mass, second moment ≈ random | EVIDENCE |

Notation follows `EXCEPTIONAL_TWIN2.md` (TW2), Setting 3.0, and
`EXCEPTIONAL_TWIN3.md` (TW3): `L = log X`, `α = L^{−1/4}`, `ρ_ℓ = ℓ^{−α}`,
fibre law P, `A = (M+1)/4`, classes `−4D mod M`, `D | A²`.

## 1. Goal (1): the k-ary noise-stability bound is already proved

The k-ary analogue of TW2 Thm 1.4 asked for in the task is TW3 Lemma 6.1
(any arity, **no codegree hypothesis**: the codegree terms are part of the
bound) together with TW3 Lemma 6.2 (codegree hubs quarantined for free by
promotion). Both were reviewed SOUND (`reviews/exceptional-twin3-review.md`
R2.2–R2.3). Restated for events of support ≤ r:

**Theorem 1.1 (= TW3 Lemma 6.1 + 6.2; PROVED, reviewed).** In TW3 Setting
6.0 with every `|S(E)| ≤ r` and `Σ_{ℓ∈S(E)} w_ℓ ≤ δ ≤ 1/16`, after
promotion of codegree hubs,

    log(Z₂⁺/Z₁⁺²) ≤ (1+25δ)[ Σ_{|σ|=1} π_σρ̃^σD_σ² + Σ_{2≤|σ|≤r} π_σρ̃^σ min(D_σ,1)² ].

Each event has at most `2^r − 1` stars, so for fixed r the "lower-support
terms" are a bounded number of star sums per class.
POINTWISE_OMEGA2 Lemma 10.2 (the hypergraph moment lemma) is therefore
**not needed**: TW3's derivative proof never expands clusters, and the
codegree condition of TW Conj 6.8 is replaced by the capped squares
`min(D_σ,1)²`. Everything left is arithmetic: bounding the star sums
(TW3 Prop 6.3) for the ES classes. That is §§2–6.

## 2. Goal (2): the ternary residual `ℓ_b < w₂q` closes by an upper-bound sieve

**The observation.** In the residual, `R = ℓ_aℓ_b` lies in one reduced
class mod `q`, and `ℓ_b < w₂q`. Hence `ℓ_a = R/ℓ_b > R/(w₂q)`: *the partner
R is itself rough* to level `(R/q)/w₂`. And `R/q` is large: `R/q ≈ ψ/(kj)`,
ψ the largest of u, v, t. So the residual does not ask for products of two
primes *in APs to moduli beyond √R* (an asymptotic, BFI-type question).
It asks only for an *upper bound* for rough integers in one progression
of length `R/q ≫ 1`. The large sieve (the same tool that proves
Montgomery–Vaughan's Brun–Titchmarsh) gives that, losing only constants
and a polylog (review F1).

More generally: do not split R at all. Split R into its Z-smooth part d
(bounded number of prime factors, all > w₂, harmonic sum ≤ (log L)^{s−1})
and its Z-rough part n, and sieve n in its class mod q. This handles every
number s of partner primes at once.

**Lemma 2.1 (large sieve; Montgomery 1968, Montgomery–Vaughan 1973, arithmetic
form).** Let 𝒩 be a set of integers in an interval of N consecutive
integers, and suppose that for each prime `p ≤ Q`, 𝒩 avoids `ω(p)` residue
classes mod p. Then `|𝒩| ≤ (N + Q²)/J`, with
`J = Σ_{d≤Q} μ²(d) Π_{p|d} ω(p)/(p − ω(p))`.

**Lemma 2.2 (van Lint–Richert; standard).** For `q ≥ 1` and `Q ≥ 1`,
`Σ_{d≤Q,(d,q)=1} μ²(d)/φ(d) ≥ (φ(q)/q) Σ_{d≤Q} μ²(d)/φ(d) ≥ (φ(q)/q) log Q`.

**Lemma 2.3 (rough-partner Brun–Titchmarsh; PROVED).** Let `s ≥ 1`,
`w ≥ 2`, `q ≥ 1`, `(b,q) = 1`, and `x ≥ q·2^{s+1}`. Let `𝓡_s(w)` be the set
of integers all of whose prime factors exceed w and with `Ω(R) ≤ s`. Put
`Y = x/q`, `Z = Y^{1/(s+1)}`, `H = Σ_{w<p≤Z} 1/(p−1)` (`H = 0` if `Z ≤ w`).
Then

    Σ_{R∈𝓡_s(w), x<R≤2x, R≡b (q)} 1/R ≤ 3(s+1)(1 + H + … + H^{s−1}) / (φ(q) log Y).

*Proof.* For R in the sum write `R = d·n`, d the product of the prime
powers of R at primes `≤ Z`, n the rest. If `Ω(d) = Ω(R)` then
`R = d ≤ Z^s = Y^{s/(s+1)} < x`, impossible; so `Ω(d) ≤ s − 1`,
`d ≤ Z^{s−1}`, and `n > 1` has all prime factors `> Z`. Also `(d,q) = 1`
since `(R,q) = 1`, so `n ≡ b d̄ (mod q)` and `n ∈ (x/d, 2x/d]`.

Fix d. Write `n = n₀ + qk` with `n₀` the least positive element of the
class. The admissible k form a set in an interval of `N ≤ x/(dq) + 1`
consecutive integers, and for each prime `p ≤ Z` with `p ∤ q` they avoid
the single class `k ≡ −n₀ q̄ (mod p)` (where `p | n`). Lemma 2.1 with
`Q = Z`, `ω(p) = 1` for `p ∤ q` and `ω(p) = 0` for `p | q`, and Lemma 2.2:

    #{n} ≤ (x/(dq) + 1 + Z²) / ((φ(q)/q) log Z).

Since `d ≤ Z^{s−1}`, `x/(dq) = Y/d ≥ Y/Z^{s−1} = Z²`, and `Y/d ≥ 1`. So the
numerator is `≤ 3x/(dq)` and `#{n} ≤ 3x/(d φ(q) log Z)`. Each such R
has `1/R < 1/x`. Summing over d,

    Σ 1/R ≤ (3/(φ(q) log Z)) Σ_d 1/d,

where d runs over Z-smooth integers with prime factors `> w` and
`Ω(d) ≤ s − 1`. Then `Σ_d 1/d ≤ Σ_{i<s} (Σ_{w<p≤Z} Σ_{e≥1} p^{−e})^i =
Σ_{i<s} H^i`. Finally `log Z = log Y/(s+1)`. ∎

*Remarks.* (i) For `s = 1` (R prime) the bound is `6/(φ(q) log(x/q))`:
Brun–Titchmarsh up to the constant. (ii) Neither the primality of the
partner nor its splitting is used, only `Ω(R) ≤ s` and roughness `> w`.
(iii) For `Z ≤ X` and `w ≥ L` (L large), Mertens gives
`H ≤ log(log Z/log w) + 1 ≤ log L`.

**Corollary 2.4 (dyadic sum).** Under the hypotheses of Lemma 2.3 with
`w = w₂ ≥ L`, any `x₀ ≥ q·2^{s+1}` and `x₀ ≤ X`, for L large,

    Σ_{R∈𝓡_s(w₂), x₀<R≤X, R≡b (q)} 1/R ≤ 12 s(s+1) (log L)^{s} / φ(q).

*Proof.* Blocks `(2^i x₀, 2^{i+1}x₀]`, `0 ≤ i ≤ 2L`, with `Y_i = 2^iY₀`,
`log Y₀ ≥ (s+1)log 2`. Then `Σ_i 1/log Y_i ≤ Σ_{i≤2L} 1/((s+1+i)log 2)
≤ (1/log 2)(1 + log(2L+1)) ≤ 2 log L`, and
`Σ_{i<s} H^i ≤ s(log L)^{s−1}` by Remark (iii) (for `H ≥ 1`; trivially
otherwise). ∎

## 3. Setting and reduction for r large primes

**Setting 3.0^{(r)}.** Fix `B ≥ 0`, `A₀ ≥ 1` and an integer `r ≥ 2`. As TW2
Setting 3.0 (same `W₁ = L^{1/2}`, `w₂ = L^8`, α, ε, Γ, fibre coordinates =
primes `≤ w₂`), except that **at most r distinct prime factors of M exceed
w₂**. For a class C (`−4D mod M`) let `S(C)` be the set of primes `> w₂`
dividing M, `k = k(C)` the w₂-smooth part, and call C *squarefree-large*
(sf) if every `ℓ ∈ S(C)` divides M exactly once, *prime-power* (pp)
otherwise. Classes with `|S(C)| = 0` are small, `|S(C)| = 1` unary,
`|S(C)| ≥ 2` events. In a fibre c an event class is *active* iff
`c ≡ −4D (mod k)`; it then gives the event
`E_C = {(ℓ, −4D mod ℓ^{e_ℓ(C)}) : ℓ ∈ S(C)}` (lifted to the coordinate
alphabets `ℤ/ℓ^{e_ℓ}` as in TW2 §1).
All constants below may depend on r, B, A₀.

**Fibre law.** TW2 §3 with one change: `G_L` is replaced by

    G_L^{(r)}:  for every prime ℓ > w₂,  p_ℓ(c) ≤ 1/8  and  w^U_ℓ(c) ≤ δ_r := (21/32)^r/(16r),

where `w^U_ℓ(c) = Σ_{active event classes C ∋ ℓ} Π_{ℓ'∈S(C)} ℓ'^{−e_{ℓ'}(C)}`.
On `supp P` (ν ≤ (8/7)U) this gives `w_ℓ ≤ (8/7)^r w^U_ℓ ≤ (3/4)^r/(16r)`.

**Proposition 3.1 (reduction, bounded arity; PROVED as an implication).**
In Setting 3.0^{(r)}, suppose the fibre law satisfies TW2 Lemma 3.2 and
`supp P ⊆ G_L^{(r)}`. Then every admissible g (`g ∈ V_{λ/2}`, `g ≥ 1` on the
avoiders, `λ ≤ A₀L`) has

    saving(g²) ≤ A₀L^{3/4}/2 + 4L^{1/2} + C_r E_P[ Σ_ℓ ρ_ℓ p_ℓ + Σ_{σ star} π_σ ρ^σ min(D_σ,1)² ],

the star sum over all stars (`|σ| ≥ 1`) of the active event system of c,
computed with the fibre's own ν.

*Proof.* TW2 Lemma 2.1 (tilting; `log‖dP/dU_F‖ ≤ 4L^{1/2}` by TW2 Lemma
3.2(2), whose proof only involves small classes and the good events).
Then TW2 Lemma 2.2 (vertex quarantine at `D_{(ℓ,a)} ≥ 1`). Its proof is
arity-free (TW3 Prop 6.3, review R2.4) except for the inflation: passing to
`ν⁺` multiplies each point mass by `≤ 4/3`, so `π⁺_E ≤ (4/3)^{|S(E)|}π_E`
and `w⁺_ℓ ≤ (4/3)^r w_ℓ ≤ 1/(16r)`. Hence `Σ_{ℓ∈S(E)} w⁺_ℓ ≤ 1/16` for
every event, and `p⁺_ℓ ≤ p_ℓ + w_ℓ ≤ 1/4`. Then TW3 Lemma 6.2 (promotion;
keeps (H_δ), δ = 1/16) and TW3 Lemma 6.1 (`1 + 25δ ≤ 2.57`). The quarantined
vertex terms are `≤ S_ℓ`-type terms with `min(D,1)²` (TW2 Lemma 2.2), the
unary factor is `≤ 2Σρ_ℓ(p_ℓ + S_ℓ)`, `ρ̃ ≤ (4/3)ρ` per coordinate, and
every star term of the quarantined system is at most `(4/3)^{3r}` times the
corresponding term in ν (TW3 (6.2), E10). Collecting factors,
`C_r = e^{O(r)}`. ∎

**Splitting the star sum.** Every star σ is `σ = (V, a)`: a nonempty set V
of large primes and residues `a` at V, contained in some event. Write
`Q_V = Π_{ℓ∈V} ℓ`, `ρ^V = Π_{ℓ∈V}ρ_ℓ`, and split
`D_σ = D^{=}_σ + D^{sf}_σ + D^{pp}_σ`: the events equal to σ (each
contributes `π_∅ = 1`), the sf events strictly containing σ, and the pp
events strictly containing σ. Since
`min(x+y+z,1)² ≤ 2·min(x,1) + 2min(y,1)² + 6z`,

    Σ_σ π_σρ^σ min(D_σ,1)² ≤ 2·T_ev + 2 Σ_V ρ^V T_V^{sf} + 6·T_pp,        (3.1)

    T_ev  = Σ_{active event classes C} ρ^{S(C)} π_{E_C}      (whole events),
    T_V^{sf} = Σ_a π_{(V,a)} min(D^{sf}_{(V,a)}, 1)²           (proper stars),
    T_pp  = Σ_V ρ^V Σ_a π_{(V,a)} D^{pp}_{(V,a)} ≤ 2^r Σ_{active pp event classes C} π_{E_C}.

(For the last: `Σ_a π_{(V,a)} D^{pp}_{(V,a)} = Σ_{pp C, S(C)⊋V} π_{E_C}`,
`ρ ≤ 1`, and a class has `< 2^r` subsets V.) In `T_V^{sf}` only sets V with
`|V| ≤ r − 1` and partners `R = M/(kQ_V)`, a product of `s ≥ 1` distinct
large primes outside V, occur.

So the r-prime cap follows from four first/second-moment bounds:
`E_P Σρ_ℓp_ℓ` (TW2 Lemma 4.1, unchanged), `E_P T_ev`, `E_P T_pp`, and
`E_P Σ_V ρ^V T_V^{sf}`, each `≪ α^{−3}(log L)^{O_r(1)}` (§§5–6).

## 4. The fibre law for r large primes

TW2 stages 1–2 (`G_s`, `Av(c_s)`, Lemmas 3.1, 3.2(1) for `P′`) involve only
small classes and are unchanged. Only `P′(G_L^{(r)}) ≥ 1/2` needs a proof.
Then TW2 Lemma 3.2 holds verbatim (inflation `4Γ(k)/k`, cost `4L^{1/2}`).

**Lemma 4.1 (`G_L^{(r)}` is likely; PROVED).** For fixed r and L large,
`P′(G_L^{(r)}) ≥ 1/2`. In fact `Σ_{ℓ>w₂} E′(w^U_ℓ)² ≪_r L^6(log L)^{O(r)}/w₂`.

*Proof.* The unary part (`p_ℓ ≤ 1/8`) is TW2 Lemma 3.4 verbatim (unary
classes `kℓ^v` do not depend on r). For `w^U_j`, expand the square. A pair
of classes with cofactors `k, k′` is jointly active with `P′`-probability
`≤ 2Γ(lcm)/lcm` (TW2 Lemma 3.2(1)). If `f(k) := Σ_{C∋j, k(C)=k} m_C ≤
(k/φ(k))F_j` for all k, where `m_C = Π_{ℓ∈S(C)}ℓ^{−e_ℓ}` and every
modulus carries `≤ τ(A²)` classes, then
`E′(w^U_j)² ≤ 2F_j² Σ_{k,k′}(Γ(lcm)/lcm)(k/φ(k))(k′/φ(k′)) ≪ F_j²(log L)^{O(1)}`
(an Euler product over `p ≤ w₂` as in TW2 (3.1)). Split the classes through
j by the top prime P of M (`M ≤ P^{1+B}`):
* *`P = j`.* `τ(A²) ≤ C_ε M^{ε} ≤ C_ε j^{1/256}`, and the other large prime
  powers give `Σ ℓ^{−e} ≤ (2 log log X)^{r−1}` each. So
  `F_j ≪ j^{−1+1/256}(log L)^{r}`.
* *`P ≠ j`, `P² | M`.* `τ(A²) ≤ C_ε P^{1/256}`, `Σ_{P>j}P^{−2+1/256} ≪ j^{−1+1/256}`,
  so `F_j ≪ j^{−2+1/256}(log L)^{r}`.
* *`P ≠ j`, `P ∥ M`.* Put `q = M/P ≤ P^B` (it contains `j^v`, k and the other
  large prime powers). TW2 Lemma 3.3 along P on dyadic blocks `y ≥ j/2`
  (at most 2L of them; hypothesis `q ≤ (2y)^{B+2}` on nonempty blocks)
  gives `Σ_P τ(A²)/P ≪ (q/φ(q))L³`. Multiply by `j^{−v}` and the other
  `ℓ^{−e}` and sum: `F_j ≪ j^{−1}L³(log L)^{r}` (using
  `q/φ(q) ≤ (k/φ(k))·2^{r}`).

Hence `E′(w^U_j)² ≪ j^{−2}L^6(log L)^{O(r)}`, and by Markov and a union
bound `P′(∃ j: w^U_j > δ_r) ≤ δ_r^{−2}Σ_{j>w₂}E′(w^U_j)² ≪_r L^6(log L)^{O(r)}/w₂ = o(1)`. ∎

*Remark.* TW3 §6.2 item 1 asked for `w₂ = L^{10}`, because it wanted the
arity-uniform condition `w_ℓ ≤ δ log ℓ/L`. For fixed r the per-vertex
condition `w_ℓ ≤ δ_r` suffices (an event has ≤ r coordinates), and
`w₂ = L^8` is enough. This closes review item E11 (the "unwritten any-arity
fibre law") for every fixed r.

## 5. First-moment terms

On `supp P`, `ν ≤ (8/7)U`, and a class with cofactor k is active with
probability `≤ 4Γ(k)/k` (TW2 Lemma 3.2(1)). So for any family 𝒞 of event
classes and weights `β_C ∈ [0,1]`,

    E_P Σ_{C∈𝒞 active} β_C π_{E_C} ≤ 4(8/7)^r Σ_{M} (Γ(k)/M) τ(A_M²) max_{C mod M} β_C.     (5.1)

(Valid for any `β_C ≥ 0`; below it is also used with `β_C ≤ 2^r`; review F2.)

Prime sums (TW2 §4): for `i ≥ 1`, `Σ_{ℓ>w₂}ℓ^{−1−α}(log ℓ)^i ≪ (i−1)!α^{−i}`;
`Σ_{w₂<ℓ≤X} 1/ℓ ≤ log L`; `Σ_{ℓ>w₂} ℓ^{−1−α} ≪ log L`.

**Lemma 5.1 (top-prime Shiu sum; PROVED).** Let `𝓜` be the sf moduli
`M = kP q₀` of the family with `|S(M)| ≤ r`, P the top prime, `q₀` the
product of the other large primes (`ω(q₀) ≤ r − 1`). Then

    Σ_{M∈𝓜} (Γ(k)/M) τ(A_M²) P^{−α} ≪_{B,r} α^{−3}(log L)^{r+O(1)}.

*Proof.* Fix k and `q₀`; let `p₂` be the largest prime of `q₀` (`p₂ = w₂`
if `q₀ = 1`). Put `q = kq₀ ≤ P^B`. TW2 Lemma 3.3 along P (all integers),
on dyadic blocks `(y,2y]`, `y_i = 2^{i−1}p₂`, exactly as TW3 Lemma 2.1(a):

    Σ_{P>p₂} P^{−1−α}τ(A²) ≪ (q/φ(q)) p₂^{−α}(a²/α + a/α² + 1/α³),   a = log(2qp₂) ≤ log 2k + r log p₂.

Multiply by `1/q₀` and sum: `p₂` with weight `p₂^{−1−α}(log p₂)^i` gives
`≪ α^{−i}` (`i ≥ 1`) or `log L` (`i = 0`), and each of the `≤ r − 2` other
primes of `q₀` gives `≤ log L`. With `q/φ(q) ≤ 2(k/φ(k))`, the result is
`≪_r (k/φ(k))(log 2k)²α^{−3}(log L)^{r−1}`. Sum over k with TW2 (3.1). ∎

**Corollary 5.2 (whole events and prime powers; PROVED).**
1. `E_P T_ev ≪ α^{−3}(log L)^{r+O(1)}`;
2. `E_P T_pp ≪_r L³(log L)^{O(r)}/w₂ + w₂^{−1/2} = o(1)`.

*Proof.* (1) For sf classes, `ρ^{S(C)} ≤ ρ_P = P^{−α}`; apply (5.1) and
Lemma 5.1. pp classes have `ρ ≤ 1` and are covered by (2).
(2) By (5.1) with `β = 1` it suffices to bound `Σ_{pp M}Γ(k)τ(A²)/M`.
As in TW2 Lemma 5.4 (prime powers): if the top prime P has `P² | M`, use
`τ ≤ C_εP^{1/256}` and `Σ_e P^{−e} ≤ 2P^{−2}` (e ≥ 2); the rest of M
(k and ≤ r − 1 large prime powers `ℓ^e`, `ℓ < P`) gives
`Σ_kΓ(k)/k · (Σ_{ℓ<P,e}ℓ^{−e})^{r−1} ≪ (log L)^{O(1)}(2 log L)^{r}`, so the
sum is `≪ (log L)^{O(r)} Σ_{P>w₂} P^{−2+1/256} ≪ w₂^{−1/2}`. If `P ∥ M` and some
other `ℓ² | M`, TW2 Lemma 3.3 along P (`q = M/P ≤ P^B`, ≤ 2L dyadic
blocks) gives `Σ_P τ/P ≪ (q/φ(q))L³`, and `Σ_ℓ ℓ^{−2} ≪ 1/w₂` together with
`≤ log L` for each remaining prime gives `≪ L³(log L)^{O(r)}/w₂`. ∎

**Lemma 5.3 (small partners; PROVED).** Fix `C₀ ≥ 6`. Call an sf class
small at V if its partner `R = M/(kQ_V) ≤ (kQ_V)^{C₀}`, and let `x_V(a)` be
`D^{sf}_{(V,a)}` restricted to such classes. Then

    E_P Σ_{V} ρ^V Σ_a π_{(V,a)} x_V(a) ≪_{B,C₀,r} α^{−3}(log L)^{2r+O(1)}.

*Proof.* `Σ_a π_{(V,a)}x_V(a) = Σ_{active C small at V} π_{E_C}`, so by (5.1)
the left side is `≤ 4(8/7)^r Σ_M (Γ(k)/M)τ(A²) Σ_{V⊊S(M), R_V small} ρ^V`.
Fix M (sf) with top prime P, and V.
* *(a) `P ∈ V`.* `ρ^V ≤ P^{−α}`. At most `2^r` sets V; Lemma 5.1 gives
  `≪ α^{−3}(log L)^{r+O(1)}`.
* *(b) `P ∉ V`.* Then `P | R`, so `P ≤ R ≤ (kQ_V)^{C₀}`. Fix k, V and
  `R′ = R/P` (a product of `≤ r − 2` large primes `< P`), and put
  `q = kQ_VR′ ≤ P^B`. TW2 Lemma 3.3 along P on the dyadic blocks with
  `p₂/2 ≤ y ≤ (kQ_V)^{C₀}` (at most `C₀ log₂(kQ_V) + 2` blocks; review F2), each block
  `≪ (q/φ(q))(log 2qy)²` with `log 2qy ≤ (C₀+1) log(2kQ_V) + log R′ ≤ (2C₀+2)log(2kQ_V)`
  (as `R′ ≤ R ≤ (kQ_V)^{C₀}`), gives
  `Σ_P τ(A²)/P ≪_{C₀} (k/φ(k))(log 2kQ_V)³`. Sum `1/R′` over its primes
  (`≤ (log L)^{r−2}`), then over V with weight `ρ^V/Q_V`:
  `(log 2kQ_V)³ ≤ (v+1)²((log 2k)³ + Σ_{ℓ∈V}(log ℓ)³)`, and
  `Σ_{ℓ>w₂} ρ_ℓ(log ℓ)³/ℓ ≪ α^{−3}`, `Σ_ℓ ρ_ℓ/ℓ ≪ log L`, give
  `Σ_{|V|=v} (ρ^V/Q_V)(log 2kQ_V)³ ≪_r ((log 2k)³ + α^{−3})(log L)^{v}`.

Both cases give `≪_r (k/φ(k))(log 2k)³α^{−3}(log L)^{2r}`; sum over k by
TW2 (3.1). ∎

This is TW3 Lemma 2.1 for all V. As noted in TW3 Prop 6.4(2), the only
loss for composite partners is `Σ_R 1/R ≤ (log L)^{s}`, polylogarithmic
because R has a bounded number of primes.

## 6. Large partners: second moments for every star

Fix a set V of `h ≥ 1` primes `> w₂` (`h ≤ r − 1`), `Q = Q_V`, and an odd
w₂-smooth k prime to Q. Let `𝓡_{Q,k}` be the set of integers R with all
prime factors `> w₂`, `Ω(R) ≤ r − h`, `R > (kQ)^{C₀}`, `kQR ≤ X`,
`kQR ≡ 3 (4)`. (It contains every large sf partner at V.) For `a mod Q` put

    V_{Q,k}(a) = Σ_{R∈𝓡_{Q,k}} R^{−1} #{D | A_R² : −4D ≡ a (mod Q)},   A_R = (kQR+1)/4.

For `h = 1`, `Ω(R) = 1` this is TW3's `V_{j,k}`. For `h = 1`, `Ω(R) = 2` it
contains the ternary residual.

**Lemma 6.1 (largest-variable reduction mod Q, any partner; PROVED).** For
L large, every `a mod Q` satisfies

    V_{Q,k}(a) ≤ 6r²(log L)^{r} [R₁(a) + R₂(a) + R₀(a)],

with `R₁, R₂, R₀` as in TW3 Lemma 3.1 but with congruences mod Q and all
variables `≤ X` and prime to Q.

*Proof.* As in TW3 Lemma 3.1, write `D | A²` as `A = uvt`, `(u,v) = 1`,
`D = u²t`; `u, v, t` are prime to kQ (`4A ≡ 1 mod kQ`), and (3.1) of TW3
holds mod Q. Assign each triple to its largest coordinate ψ (ties: t, u, v).

*t largest.* The residue is `−u/v mod Q`. Fix `(u,v)`, `q = 4uv`; then
`(q,kQ) = 1`, and the R counted lie in the single reduced class
`R ≡ −(kQ)^{−1} (mod q)` and satisfy `A_R ≥ uv·max(u,v)`, `R > (kQ)^{C₀}`.
Each R gives at most one triple. *Claim:* every such R is `≥ x₀ := 2^{r}q`.
If `q ≤ 2^{−r}(kQ)^{C₀}` this is `R > (kQ)^{C₀}`. Otherwise
`max(u,v) ≥ (q/4)^{1/2}` gives `4A_R ≥ q^{3/2}/2`, so
`R/q ≥ q^{1/2}/(2kQ) − 1 ≥ 2^{−r/2−1}(kQ)^{C₀/2−1} − 1 ≥ 2^{r}`, since
`C₀ ≥ 6` and `kQ > w₂ → ∞`. Corollary 2.4 (with `s = r − h ≤ r − 1`,
`w = w₂`, `x₀ ≥ 2^{s+1}q`) gives `Σ_R 1/R ≤ 12r²(log L)^{r−1}/φ(q)`, and
`φ(4uv) ≥ 2φ(uv)`.

*u largest* (residue `−1/(4v²t)`, fix `(v,t)`, `q = 4vt`, drop `(u,v) = 1`;
`u = A_R/(vt)` is determined by R) and *v largest* (residue `−4u²t`,
`q = 4ut`) are identical, with `A_R ≥ vt·max(v,t)` resp. `ut·max(u,t)`. ∎

*This is where the ternary residual closes.* TW3 fixed `ℓ_a` and applied
Brun–Titchmarsh to the prime `ℓ_b` in its class mod q, which needs
`ℓ_b ≥ w₂q`. Lemma 2.3 sieves the whole partner R in its class mod q.
The only length condition is `R/q ≥ 2^{s+1}`, and it holds for every
large partner (`R > (kQ)^{C₀}`, `C₀ ≥ 6`, L large; review F4b). No
asymptotic for primes or almost-primes in progressions to large moduli
(BFI) is needed: the question was an upper-bound question all along.

**Lemma 6.2 (second moments mod a squarefree Q; PROVED).** Let Q be
squarefree with `h` prime factors, all `> w₂`, and let `X ≥ 2`. With all
variables in `[1,X]` and prime to Q, and `r₁, r` defined as in TW3 Lemma
3.2 with congruences mod Q,

    Σ_{ρ mod Q} r₁(ρ)² ≤ ζ(2)² + C(log X)²((log X)²/Q + (log Q)Q^{−1/2}),
    Σ_{c mod Q} r(c)²  ≤ ζ(2)²ζ(3)² + C·2^h(log X)²((log X)²/Q + (log Q)Q^{−1/3}).

*Proof.* TW3 Lemma 3.2 verbatim, with three facts about Q in place of the
prime j (review R2.5 checked them for `Q = ℓ₁ℓ₂`): (i) `v² ≡ c/t (mod Q)`
has `≤ 2^h` roots (CRT); so a box has `≤ 2^h T(V/Q + 1)` points for fixed t;
(ii) distinct `N ≡ N′ (mod Q)` with `N, N′ ≥ 1` have `max(N,N′) > Q`;
(iii) for distinct reduced fractions with `u ≡ ρv`, `u′ ≡ ρv′` (ρ a unit,
since u, v are units), `Q | uv′ − u′v ≠ 0`, so the product of heights is
`≥ Q` and one height is `≥ Q^{1/2}`; and fixing u fixes v mod Q. ∎

**Corollary 6.3 (PROVED).** For L large and every V, k as above,
`Σ_{a mod Q} V_{Q,k}(a)² ≤ C_r(log L)^{2r+4}`.

*Proof.* As TW3 Cor 3.3: `1/φ(xy) ≤ (2log L)²/(xy)` for `x, y ≤ X`;
`a ↦ c` is a bijection of the units mod Q (and `V(a) = 0` for non-units,
since `−4D` is a unit mod Q); `(x+y+z)² ≤ 3(x²+y²+z²)`; Lemma 6.2 with
`Q > w₂ = L^8` and `X = e^L` makes the brackets `≪ 2^r`. ∎

**Lemma 6.4 (large part; PROVED).** Let `z_V(a)` be `D^{sf}_{(V,a)}`
restricted to classes with partner `R > (kQ_V)^{C₀}`. Then

    E_P Σ_V ρ^V Σ_a π_{(V,a)} z_V(a)² ≪_r (log L)^{3r+O(1)}.

*Proof.* An sf class constrains `y_ℓ` (`ℓ ∈ V`) only mod ℓ, so `z_V(a)`
depends only on `a mod Q`, and the lifts of a residue mod Q carry total
mass `≤ (8/7)^h/Q`. Each class contributes `≤ (8/7)^{r}/R` to z, and a
pair of classes with cofactors `k, k′` is jointly active with probability
`≤ 4Γ(lcm)/lcm`. So, as in TW3 Lemma 3.4 (AM–GM and
`Σ_{k′}Γ(lcm)/lcm ≤ Γ(k)h(k)/k`, TW2 Lemma 5.4(ii)),

    E_P Σ_a π_{(V,a)} z_V(a)² ≤ 4(8/7)^{3r} Q^{−1} Σ_k (Γ(k)h(k)/k) Σ_{a mod Q} V_{Q,k}(a)²
                            ≪_r Q^{−1}(log L)^{2r+O(1)}

by Corollary 6.3 and TW2 Lemma 5.4(iii). Finally
`Σ_{|V|=h} ρ^V/Q_V ≤ (Σ_{ℓ>w₂}ρ_ℓ/ℓ)^h ≪ (log L)^h`, `h ≤ r − 1`. ∎

## 7. Assembly: the Λ² cap for moduli with at most r large primes

**Theorem 7.1 (r-prime Λ² cap; PROVED, internal).** Fix `r ≥ 2`, `B ≥ 0`,
`A₀ ≥ 1`. For ℛ(M)-families with `M ≤ X`, `M ≤ P(M)^{1+B}`, and at most r
distinct prime factors of M above `w₂ = (log X)^8` (twins, triplets, …,
dominant moduli and prime powers included), every admissible Λ² majorant g
of level `λ ≤ A₀L` has

    saving(g²) ≪_{A₀,B,r} L^{3/4}(log L)^{3r+O(1)}.

*Proof.* Fibre law: TW2 §3 with `G_L^{(r)}` (Lemma 4.1; TW2 Lemma 3.2
then holds verbatim). Proposition 3.1 reduces the saving to
`A₀L^{3/4}/2 + 4L^{1/2} + C_r E_P[Σρ_ℓp_ℓ + star sum]`. The unary term is
TW2 Lemma 4.1 (`≪ α^{−3}(log L)^{O(1)}`). Split the star sum by (3.1):
* `T_ev`: Cor 5.2(1), `≪ α^{−3}(log L)^{r+O(1)}`;
* `T_pp`: Cor 5.2(2), `o(1)`;
* `T_V^{sf}`: with `D^{sf} = x_V + z_V` (small/large partners),
  `min(x+z,1)² ≤ 2x + 2z²`. The x-part is Lemma 5.3
  (`≪ α^{−3}(log L)^{2r+O(1)}`), the z-part is Lemma 6.4
  (`≪ (log L)^{3r+O(1)}`).
With `α^{−3} = L^{3/4}` the total is `≪ L^{3/4}(log L)^{3r+O(1)}`. ∎

For `r = 2` this is TW3 Cor 4.2 (with a different log-power). For `r = 3`
it closes the ternary residual of TW3 §6.3 and supersedes TW3 Prop 6.4
(SKETCH) by a proof.

**Corollary 7.2.** Within the class of Λ² forced-class sieves whose
moduli `M ≤ X` satisfy `M ≤ P(M)^{1+B}` and have a bounded number of
prime factors above `(log X)^8`, the saving is capped:
`saving ≪ L^{3/4+o(1)}`. So such sieves cannot give an exceptional-set
exponent θ > 3/4. This is the ET Lemma 2.9 translation (level `λ ≍ L`;
TW review T7), inherited as in EXCEPTIONAL_TWIN.md §5; Theorem 7.1 is
uniform in `λ ≤ A₀L` (review F3). ∎

### 7.1 What is left for "all polynomially bounded moduli" (Assessment)

Theorem 7.1 is uniform only for fixed r. A modulus `M ≤ X` can have up to
`L/(8 log L)` primes above `w₂`. The r-dependence is:
* `C_r = e^{O(r)}` (inflation factors in Prop 3.1, `δ_r`, `2^r` subsets);
* `(log L)^{O(r)}` from partner harmonic sums
  `Σ_R 1/R ≤ (Σ_{w₂<ℓ≤X}1/ℓ)^s` and from `Σ_V ρ^V/Q_V ≤ (log L)^h`;
* Lemma 4.1 needs `L^6(log L)^{O(r)}/w₂ = o(1)`.
So the proof gives `saving ≪ L^{3/4+O(ε)}` for
`r ≤ ε log L/log log L`, after tracking constants (not done; the
factorials `1/s!`, `1/h!` in the harmonic sums would help). The range
`ε log L/log log L < r ≤ L/(8 log L)` is not covered. There the partner
sums `Σ_R 1/R` over all w₂-rough R are `≍ L/log w₂` (TW3 §6.2 (3a)–(3c)),
and a different bookkeeping is needed, e.g. charging each class only to
stars V containing its top few primes, or raising w₂ with r. The
B-hypothesis is also still assumed. Neither point is a BFI-type
obstruction: the arithmetic inputs used here (Shiu along the top prime,
large sieve for rough partners, box counting mod Q) are all upper bounds.

## 8. Numerics (EVIDENCE, toy scale)

**Lemma 2.3, exact** (`scripts/twin4_rough_bt.py A 1e6`): `s ∈ {1,2,3}`,
`w ∈ {2,5,30,100}`, nine moduli q up to 10007, three x up to 10⁶, five
random units b each: 1228 cases, worst `lhs/bound = 0.128`. (The proof's
constant 3(s+1) and the `log Z = log Y/(s+1)` loss are generous.)

**The former residual on a toy ternary system** (`… B 1e9 1009 10007`):
`M = jR`, `R = ℓ_aℓ_b` (primes ≥ `w₀ = 11`, `≠ j`, `ℓ_a ≤ ℓ_b`, so
`R = ℓ²` is included; review F4a), `jR ≤ 10⁹`,
`jR ≡ 3 (4)`, toy `C₀ = 1` (R > j), all `D | A²`, k = 1, no fibre. Each
triple is put in TW3's proved part if `ℓ_b ≥ w₀q`, else in the former
residual.

| j | #R | part | mass `ΣV` | `ΣV²` | max V | random `(ΣV)²/j` |
|---|---|---|---|---|---|---|
| 1009 | 53612 | proved | 10.24 | 1.016 | 0.425 | 0.104 |
| 1009 | 53612 | residual | 40.61 | 1.826 | 0.082 | 1.635 |
| 10007 | 4893 | proved | 3.09 | 0.139 | 0.155 | 0.001 |
| 10007 | 4893 | residual | 18.94 | 0.052 | 0.015 | 0.036 |

Reading: the former residual carries most of the ternary mass (80–86%),
as TW3 §6.3 predicted. So it could not have been dropped. Yet its second
moment is within a factor 1.5 of random, and its max is small. The proved
part has the larger max: it contains the hub `a = −1` (`u = v = 1`,
`q = 4`), which every R hits. Its second moment is polylogarithmic, as
Lemma 6.1 allows (`R₁(−1) ≥ 1`). Not tested: k > 1, the fibre law, `C₀ ≥ 6`,
`j > L^8` (out of numerical reach).

## Replay

```
# Lemma 2.3 exact check (~40 s, < 1 GB)
uv run --with numpy python scripts/twin4_rough_bt.py A 1e6
# toy ternary table (~15 s, ~1.2 GB for the spf sieve to 2.5e8)
uv run --with numpy python scripts/twin4_rough_bt.py B 1e9 1009 10007
```

## 9. Uniformity in r (task O12, part 2a)

Write `ω_L(M)` for the number of distinct primes `> w₂` dividing M, and
`H₁ = Σ_{w₂<ℓ≤X} 1/ℓ ≤ log L`.

### 9.1 Range I: explicit r-dependence

**Proposition 9.1 (PROVED; bookkeeping).** In Theorem 7.1 every implied
constant is `≤ (C_B log L)^{C r}` (C absolute, `C_B` depending on B only),
uniformly in `2 ≤ r ≤ log L`, provided Lemma 4.1 holds, i.e.
`δ_r^{−2}L^6(log L)^{Cr}/w₂ = o(1)`. Hence, for
`r ≤ ε log L/log log L` with `ε ≤ ε₀` small absolute,

    saving(g²) ≪_{A₀,B} L^{3/4 + Cε}.

*Proof.* Collect the r-dependence of each step. Shiu's constant (TW2 Lemma
3.3) depends only on B. All the remaining losses are listed here:

| step | loss |
|---|---|
| Prop 3.1 (inflations `(8/7)^r(4/3)^{3r}`, `1+25δ`) | `e^{O(r)}` |
| `δ_r^{−1} = 16r(32/21)^r` (Lemma 4.1 threshold) | `e^{O(r)}` |
| harmonic sums over other large primes (Lemmas 4.1, 5.1, 5.3, Cor 5.2) | `(2log L)^{r}` |
| `2^r` subsets V (3.1), Lemma 5.3 | `2^r` |
| Lemma 5.1: `a ≤ log 2k + r log p₂`, so `a² ≤ 2(log 2k)² + 2r²(log p₂)²` | `r²` |
| Lemma 5.3(b): `(log 2kQ_V)³ ≤ (v+1)²(…)` | `r²` |
| Lemma 2.3 / Cor 2.4: `12 s(s+1)(log L)^{s}` | `r²(log L)^{r}` |
| Lemma 6.1 squared, Lemma 6.2 (`2^h` roots), Lemma 6.4 (`(8/7)^{3r}`, `Σ_V ρ^V/Q_V ≤ (log L)^h`) | `e^{O(r)}(log L)^{3r}` |

The product is `≤ (C_B log L)^{Cr}`. In Lemma 4.1 the requirement is
`e^{O(r)}(log L)^{O(r)}L^6/L^8 = o(1)`, true for
`r ≤ ε₀ log L/log log L`. Finally `(C_B log L)^{Cr} ≤ L^{Cε(1+o(1))}`. ∎

### 9.2 Range III: moduli with ≥ C₁ log L large primes are free

**Lemma 9.2 (unweighted payment; PROVED).** Let `𝓔₁` be the event system
of a fibre c, after vertex quarantine and promotion, with law `ν⁺` and
`Σ_{ℓ∈S(F)} w⁺_ℓ ≤ 1/32` for every `F ∈ 𝓔₁`. Let `𝓔₂` be a further finite
family of events (any arity), and put
`y_ℓ = Σ_{G∈𝓔₂, G∋ℓ} 2^{|S(G)|}P_{ν⁺}(G)` and `m₂ = Σ_{G∈𝓔₂} 2^{|S(G)|}P_{ν⁺}(G)`.
If `Σ_{ℓ∈S(F)} y_ℓ ≤ 1/32` for every `F ∈ 𝓔₁`, `y_ℓ ≤ 1/32` for every ℓ, and
`m₂ ≤ 1`, then with `A⁺ = A₁⁺ ∩ {no 𝓔₂ event}`

    Ξ_c(A⁺) ≤ Ξ_c(A₁⁺) + 3m₂.

*Proof.* `P(A⁺∩A⁺′) ≤ P(A₁⁺∩A₁⁺′)`, and `P(A⁺) = P(A₁⁺)P(no 𝓔₂ | A₁⁺)`
(the unary factors are common). Apply TW2 Lemma 1.1 in the `ν⁺`-product
space to `𝓑 = 𝓔₁ ∪ 𝓔₂`, with `x_F = 2P(F)` on `𝓔₁` and
`x_G = 2^{|S(G)|}P(G)` on `𝓔₂`. *Hypothesis.* For `F ∈ 𝓔₁`,
`Σ_{Γ(F)}x ≤ Σ_{ℓ∈S(F)}(2w⁺_ℓ + y_ℓ) ≤ 3/32`. So `Π_{Γ(F)}(1−x) ≥ 1/2`, and
`P(F) = x_F/2` is enough. For `G ∈ 𝓔₂`,
`Σ_{Γ(G)}x ≤ Σ_{ℓ∈S(G)}(2w⁺_ℓ + y_ℓ) ≤ |S(G)|·(1/16 + 1/32)`. Every
`x ≤ 1/8`, so `Π(1−x) ≥ exp(−(8/7)(3/32)|S(G)|) ≥ 2^{−|S(G)|}`. *Conclusion.*
Order `𝓔₂ = {G₁, G₂, …}`. Lemma 1.1(1) with
`𝓢 = 𝓔₁ ∪ {G_1,…,G_{i−1}}` gives `P(G_i | A₁⁺ ∩ Ḡ_{<i}) ≤ x_{G_i}`. Hence
`P(no 𝓔₂ | A₁⁺) ≥ Π_i(1 − x_{G_i}) ≥ exp(−(8/7)m₂)`. Then
`Ξ(A⁺) ≤ Ξ(A₁⁺) + (16/7)m₂`. ∎

TW2 Lemma 2.1 accepts any nonempty `A⁺_c ⊆ A_c`, so Lemma 9.2 lets a
low-mass subfamily be added to *any* system already controlled, paying
only its total (2^{|S|}-inflated) mass. No ρ-weight and no arity bound are
needed.

**Corollary 9.3 (PROVED).** Let `r₂ = C₁ log L`, `C₁ = 330`. Adding to any
family of Setting 3.0^{(r)} (or of Prop 9.1) all classes with
`ω_L(M) ≥ r₂` (no B-hypothesis for them) changes the saving bound by
`o(1)`, provided the fibre law also conditions on the event
`G_III = {m₂(c) ≤ L^{−1}}`, where `m₂` is computed with `U` in place of `ν⁺`
and the factor `4^{|S|}` in place of `2^{|S|}` (as `ν⁺ ≤ (4/3)(8/7)U ≤ 2U`).

*Proof.* On `G_III`, `y_ℓ ≤ m₂ ≤ L^{−1}`, so `Σ_{ℓ∈S(F)}y_ℓ ≤ r/L ≤ 1/32` for
`F ∈ 𝓔₁`, and Lemma 9.2 applies. It costs `3m₂ ≤ 3/L`. It remains to show
`P′(G_III^c) = o(1)`. Then the fibre-law bookkeeping of TW2 Lemma 3.2 is
unchanged (`P′(G_L ∩ G_III) ≥ 1/2`). By TW2 Lemma 3.2(1) for `P′`,

    E′m₂ ≤ Σ_C (2Γ(k)/k)·4^{ω_L}/M_L = 2 Σ_{M≤X, ω_L(M)≥r₂} Γ(k)τ(A²)4^{ω_L(M)}/M
        ≤ 2 (Σ_M τ(A²)²Γ(k)²/M)^{1/2} · (Σ_{M≤X} 16^{ω_L(M)}1[ω_L(M)≥r₂]/M)^{1/2}

(activity `2Γ(k)/k` times event mass `1/M_L`, `M_L = M/k`; ≤ τ(A²) classes
per modulus; Cauchy–Schwarz).
*First factor.* `Γ(k)² ≤ 9^{ω(k)}` and Cauchy–Schwarz again give
`≤ (Σ_{A≤X}τ(A²)⁴/A)^{1/4}(Σ_{M≤X}81^{ω(M)}/M)^{1/4} ≪ L^{81/2}` (Euler
products: `τ(p²)⁴ = 81`). *Second factor (Rankin).* For `y > 0`,
`Σ_M 16^{ω_L}1[ω_L ≥ r₂]/M ≤ y^{−r₂}Σ_M (16y)^{ω_L(M)}/M
≤ y^{−r₂}·2log w₂·exp(16y(H₁ + 1))`. With `y = r₂/(16 log L)` this is
`≪ log L·(16e log L/r₂)^{r₂} = log L·L^{−C₁log(C₁/(16e))}`, and
`C₁ log(C₁/16e)/2 ≥ 330/2 > 81/2 + 2`. So `E′m₂ ≪ L^{−2}` and Markov
gives `P′(m₂ > L^{−1}) = o(1)`. ∎

### 9.3 The middle range `ε log L/log log L < r < C₁ log L` (Assessment)

This range is **not** covered, and it is the bulk. With the ρ-weights,
the effective moduli have large part `≤ e^{O(1/α)}`, and the number of
their primes in `(L^8, e^{L^{1/4}}]` is Poisson-like with mean
`log(L^{1/4}/(8log L)) ≈ (1/4)log L`. So most of the `α^{−3}` mass lies at
`r ≍ log L`. There every loss of the form `c^r` with `c > 1` is a power of L.

*What is lossy, and what is genuine.*
1. Inflation factors `(8/7)^r, (4/3)^r`: *removable*. They come from the
   coarse thresholds `p_ℓ ≤ 1/8`, `w_ℓ ≤ δ_r`. In good fibres
   `p_ℓ, w_ℓ ≪ L^{4}/ℓ`, so `Π_{ℓ∈S}(1−p_ℓ)^{−1} = 1 + O(rL^4/w₂) = 1+o(1)`
   (TW3 already notes `e^{(4/3)w_ℓ}`). This needs a polynomial-decay G_L.
2. Harmonic sums `(log L)^s` without `1/s!`: *removable*. Prime variables
   are unordered.
3. **The first moment for small partners (Lemma 5.3) over `2^r` subsets V:
   genuine for this method.** `min(x,1)² ≤ x` loses the factor `1/D`. The
   *diagonal* part of the star sum is `Σ_C π_{E_C} Σ_{V⊊S}ρ^V/R_V =
   Σ_C π_{E_C}(Π_{ℓ∈S}(ρ_ℓ + 1/ℓ) − ρ^S)`, which is harmless:
   `Π(ρ_ℓ+1/ℓ) ≤ ρ^S(1+o(1))` for `r ≤ L`. This is TW Conj 6.8's main term.
   The first-moment bound instead pays `Σ_{V: R_V small}ρ^V`, i.e. `≈ 2^r`
   per class. So the middle range needs an **off-diagonal second moment
   at stars with short partners**. Namely, for V and partners
   `R ≤ (kQ_V)^{C₀}`, a bound on
   `Q_V^{−1}Σ_{(R,D)≠(R′,D′), −4D≡−4D′ (Q_V)} 1/(RR′)` that is efficient
   per prime (`1 + o(1)` per prime of V, summed over V). This is the
   multi-prime analogue of TW2's (H_O^≠). It was bypassed for r = 2
   because there the first-moment loss was affordable (TW3 Remark,
   "Where the budget goes"). For short partners (`A ≤ Q^{C₀+1}`) the
   divisor labels `−u/v mod Q_V` have height comparable to `Q_V^{1/2}`,
   so neither Lemma 2.3 nor box counting applies. It is a genuine
   equidistribution question for divisors of `(kQR+1)²/16` mod `Q`,
   averaged over `Q`. **OPEN.**
4. Range III (Cor 9.3) shows that the very-many-prime tail is not the
   problem. What blocks the full family is item 3, in the window
   `r ≍ log L`.

## 10. Removing the B-hypothesis for fixed r (task O12, part 2b)

**Setting 3.0^{(r)}_*.** Setting 3.0^{(r)} *without* `M ≤ P(M)^{1+B}`: all
Case-B classes with `M ≤ X` and `ω_L(M) ≤ r`. Write `M = k·M_L`, k
w₂-smooth, `M_L` the large part. Split the classes with `ω_L ≥ 1`:
* **(D) smooth-dominated:** `k > M_L²`;
* **(H) high power:** not (D), and `ℓ^{12} | M` for some `ℓ > w₂`;
* **(G) good:** the rest. Then `M_L ≤ P^{11r}` (≤ r prime powers with
  exponent ≤ 11, P the top prime), so `M ≤ M_L³ ≤ P(M)^{33r}`: **(G)
  satisfies the B-hypothesis with `B = 33r − 1`.**

So for fixed r the B-hypothesis only excludes (D) and (H). (D) is the
regime "small top prime relative to M": the w₂-smooth cofactor carries
most of M. Smooth numbers are sparse, but Shiu along the top prime is
not available there, because the modulus `M/P` exceeds the length.
Instead we run Shiu along k itself (now the modulus `M_L` is short) and
pay for the smoothness of k with Rankin.

**Lemma 10.1 (smooth-dominated sums; PROVED).** Let `i ∈ {1,2}`, and let G
be multiplicative with `0 ≤ G(p^e) ≤ C(1+3e)` for `p ≤ w₂`, `G(p^e) = 0`
for `p > w₂` (e.g. `Γ`, `Γ·2^{ω}`, `Γ·τ_Γ`). For odd `m ≥ 1` with
`(m, k) = 1`,

    Σ_{k>m², k≡k₀ (4)} G(k)τ(A_{km}²)^i / k ≪_{i,C} (log L)^{c_i} (m/φ(m))^{1/2} m^{−1/(2 log w₂)},

with `A_{km} = (km+1)/4` and `c_i` depending only on i and C. The same
bound without the factor `m^{−1/(2log w₂)}` holds for the sum over all
k when `m = 1`.

*Proof.* Dyadic blocks `(K,2K]`, `K ≥ m²`. Put `u = log K/log w₂`.
Cauchy–Schwarz splits a block into `(Σ_{k∈(K,2K] smooth}G(k)²/k)^{1/2}`
times `(Σ_{k∈(K,2K]}τ(A_{km}²)^{2i}/k)^{1/2}`.
*Rankin* (k odd, so `p ≥ 3`; `η = 1/log w₂`, `p^{η} ≤ e`): the first sum is
at most `K^{−η}Π_{3≤p≤w₂}(1 + Σ_e G(p^e)²p^{−e(1−η)}) ≤ e^{−u}(log L)^{c}`.
The series at `p = 3` converges since `e/3 < 1`.
*Shiu along k* (all integers k). `A = (km+1)/4` runs over one class mod m,
in an interval of length `mK/4 ≥ m³/4`. So `m < (mK/4)^{1−β}` and
`x^β < y` hold with `β = 1/4` for K large; small K are trivial. Shiu's
theorem with `F(n) = τ(n²)^{2i}` (`F(p^l) ≤ 9^{il}`, `F(n) ≪ n^{o(1)}`)
gives `Σ_{k∈(K,2K]} F(A) ≪ (Km/φ(m))(log 2K)^{9^i−1}`. Hence a block
contributes `≪ (log L)^{c}(m/φ(m))^{1/2}e^{−u/2}(log 2K)^{(9^i−1)/2}`. Write
`log 2K ≤ 2u log w₂` and sum over `K = 2^t ≥ m²`:
`Σ_t e^{−u/2}u^{c′} ≪ log w₂ · e^{−u₀/3}` with `u₀ = 2log m/log w₂`. And
`e^{−u₀/3} ≤ m^{−1/(2log w₂)}`. For `m = 1` sum over all blocks. ∎

**Lemma 10.2 (first moments of (D) and (H); PROVED).**
1. `Σ_{(D) moduli} Γ(k)τ(A²)/M ≪ (log L)^{O(1)}`;
2. `Σ_{(H) moduli} Γ(k)τ(A²)/M ≪ L^{−3}`.

*Proof.* (1) Write `M = km`, `m = M_L ≥ w₂` (odd), and apply Lemma 10.1
(i = 1, G = Γ) for each m. Then
`Σ_{m≥1}(m/φ(m))^{1/2}m^{−1−1/(2log w₂)} ≪ log w₂`. (2) Cauchy–Schwarz:
`(Σ_{M≤X}τ(A²)²Γ(k)²/M)^{1/2} ≪ L^{81/2}` (proof of Cor 9.3), times
`(Σ_{M≤X, ℓ^{12}|M, ℓ>w₂} 1/M)^{1/2} ≤ (2L·w₂^{−11})^{1/2} ≪ L^{−43}`. ∎

**Lemma 10.3 (fibre law without B; PROVED).** In Setting 3.0^{(r)}_*,
`P_QR(G_s) ≥ 1/2` and `P′(G_L^{(r)}) ≥ 1/2` for L large. Hence TW2 Lemma 3.2
holds (inflation `4Γ(k)/k`, cost `4L^{1/2}`).

*Proof.* B entered TW2 Lemma 3.4 only through pointwise τ bounds (review
D3(b),(c)) and Shiu along the top prime (D3(a)).
* *Small classes (`M = k`, no B now).* `E_QR T ≤ Σ_k Γ(k)2^{ω(k)}τ(A_k²)/k
  ≪ (log L)^{O(1)}` by Lemma 10.1 (m = 1). This is better than TW2's
  `L^{1/32+o(1)}`. For `μ_p`: expand the square, use AM–GM on
  `τ(A_k²)τ(A_{k′}²)`. The `k′`-sum gives `(log L)^{O(1)}p^{−1}` (TW2), and
  for `k = pk″` the proof of Lemma 10.1 (i = 2) gives `p^{−1/2}` from each
  Cauchy–Schwarz factor: Rankin with the factor at p, and Shiu along k″
  in a class mod p (valid for `k ≥ p^{4/3}`). For `k < p^{4/3} ≤ w₂²`, TW2's
  pointwise `τ(A²) ≤ C_εk^{ε}` gives `≤ L^{1/16}`. So
  `E_QRμ_p² ≪ L^{1/16}(log L)^{O(1)}p^{−2}`, as in TW2, and
  `Σ_{p>W₁}p^{1/2}Eμ_p² ≪ L^{1/16+o(1)}W₁^{−1/2} = o(1)`.
* *(G) unary and event classes:* B holds with `B = 33r−1`, so TW2 Lemma
  3.4 and Lemma 4.1 above apply verbatim.
* *(H) classes:* by Markov on the first moment,
  `P′(∃ℓ: p^{(H)}_ℓ + w^{U,(H)}_ℓ > δ_r/3) ≤ 3δ_r^{−1}·r·2·(Lemma 10.2(2)) = o(1)`.
* *(D) classes through j* (unary or events). Put
  `f_j(k) = Σ_{m: j|m, k>m²} τ(A_{km}²)/m`. As in TW3 Lemma 3.4,
  `E′(w^{U,(D)}_j)² ≤ 2Σ_k(Γ(k)h(k)/k)f_j(k)²`. Cauchy–Schwarz over m gives
  `f_j(k)² ≤ (Σ_{j|m}1/m)(Σ_{j|m}τ(A_{km}²)²/m)` with
  `Σ_{j|m, ω_L(m)≤r}1/m ≤ 2j^{−1}(2log L)^{r}`. Then Lemma 10.1 (i = 2,
  `G = Γh`; `h(k) ≪ (log L)^{O(1)}τ_Γ(k)`) for each m gives
  `E′(w^{U,(D)}_j)² ≪ (log L)^{O(r)}j^{−1}Σ_{j|m}(m/φ(m))^{1/2}m^{−1} ≪ (log L)^{O(r)}j^{−2}`.
  The same holds for the unary density `p^{(D)}_j`. Markov and
  `Σ_{j>w₂}j^{−2} ≪ w₂^{−1}` give `o(1)`. ∎

**Theorem 10.4 (r-prime Λ² cap without the B-hypothesis; PROVED, internal).**
Fix `r ≥ 2`, `A₀ ≥ 1`. For ℛ(M)-families with `M ≤ X` and at most r
distinct prime factors above `w₂ = (log X)^8` (no condition relating M to
its top prime), every admissible Λ² majorant of level `λ ≤ A₀L` has

    saving(g²) ≪_{A₀,r} L^{3/4}(log L)^{O_r(1)}.

The same holds if the family also contains arbitrary classes with
`ω_L(M) ≥ 330 log L` (Cor 9.3).

*Proof.* Fibre law: Lemma 10.3 (plus `G_III` of Cor 9.3 if the
many-prime classes are present). Prop 3.1 applies to the whole active
system, because the per-vertex bounds hold for all three types. Split
`D_σ = D^{(G)}_σ + D^{(D,H)}_σ` and use
`min(x+y,1)² ≤ 2min(x,1)² + 2y`:
* (G) part: §§5–6 and Cor 5.2 with `B = 33r − 1`. Those lemmas use B only
  for the classes they sum over.
* (D,H) part: `≤ 2Σ_σπ_σD^{(D,H)}_σ ≤ 2^{r+1}Σ_{active (D,H) C}π_{E_C}`.
  Its `E_P` is `≪ 2^r(8/7)^r·4·Lemma 10.2 ≪ (log L)^{O(1)}`.
* Unary term `Σρ_ℓp_ℓ`: (G) by TW2 Lemma 4.1 with `B = 33r−1`; (D), (H) by
  Lemma 10.2.
The many-prime classes are added by Lemma 9.2 at cost `o(1)`. ∎

**Remark 10.5 (what (D) teaches).** For moduli dominated by their
w₂-smooth part, the heuristic worry is that `τ(A²)` is as large as
`(log X)²` while the ρ-weight sees only the small large part. That would
make the *diagonal* term itself too big. It does not happen: by Lemma 10.1
the smooth cofactor's sparsity (Rankin, `e^{−u}`) beats every power of
`log k`. The whole (D) family has polylogarithmic *unweighted* first
moment, so it needs no ρ-weight and no equidistribution at all. The
"gapped/QR-base machinery" of TW is not needed for it.
