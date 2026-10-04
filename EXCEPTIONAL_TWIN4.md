# EXCEPTIONAL_TWIN4 — the Λ² cap for moduli with r large primes (task O12)

## 0. Status at a glance

(in progress; filled in at the checkpoint)

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
Montgomery–Vaughan's Brun–Titchmarsh) gives that, losing nothing.

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
  `p₂/2 ≤ y ≤ (kQ_V)^{C₀}` (at most `C₀ log(kQ_V) + 1` blocks), each block
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
The only length condition is `R/q ≥ 2^{s+1}`, and it always holds. No
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
exponent θ > 3/4. ∎

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
