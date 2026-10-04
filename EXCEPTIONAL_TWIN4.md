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
corresponding term in ν (TW3 (6.2), E10). So `C_r ≤ 3·(4/3)^{4r}`
suffices. ∎

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
