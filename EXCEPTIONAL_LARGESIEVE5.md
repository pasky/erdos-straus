# EXCEPTIONAL_LARGESIEVE5 — the covering count (CC) for residue-dense multi-rough classes (task O67)

Status: **in progress** (agent O67, branch `side-agent/astar-dense`).
Labels as in `DISCOVERIES.md`. Notation: LS4 = `EXCEPTIONAL_LARGESIEVE4.md`
(all its notation is used: Setting 4.0, Lemma 5.1, (A*), (CC)), LS3, LS =
`EXCEPTIONAL_LARGESIEVE.md`, K2 = `EXCEPTIONAL_KARY2.md`.

## 0. Plan and summary (updated as the work proceeds)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | caps are inherited by subfamilies: it suffices to prove the all-level cap for the **full** forced family `𝔊_X` (all classes of the four types with modulus ≤ X), uniformly in X | PROVED (trivial) |
| Lemma 1.2 | **rational labels**: every forced class is `−r/s mod G` with `r, s ≤ G²`; two classes with *different* labels that agree mod g have height product `≥ g/2` | PROVED (elementary) |

## 1. Two elementary reductions

**Lemma 1.1 (monotonicity in the family; PROVED).** Let `𝔊 ⊆ 𝔊'` be finite
families. If every CRT-admissible N-large-sieve bound for `𝒜(𝔊')` saves
at most `S`, then so does every CRT-admissible bound for `𝒜(𝔊)`.
Likewise for the Hölder/(H_rough) route of LS3–LS4: a measure π on
`𝒜(𝔊')` with the required Rényi bounds serves for 𝔊.

*Proof.* `𝒜(𝔊') ⊆ 𝒜(𝔊)`. Let `M'` be a common multiple of the periods
and of the frequency denominators. A CRT-admissible bound `Z ≤ 1/L` for
𝔊 has `L ≤ F_w(π)` for every probability π on `𝒜(𝔊) mod M'` (LS §1), in
particular for every π on `𝒜(𝔊') mod M'`; so `L ≤ F*_w(𝔊')`, and the cap
for 𝔊' (which is a lower bound on `1/F*_w(𝔊')` relative to N) applies.
For the Hölder route the cap is proved by exhibiting one π supported on
the avoider set; a π on `𝒜(𝔊')` is supported on `𝒜(𝔊)`, and projecting
to a coarser modulus does not change `π̂` at frequencies whose
denominators divide it. ∎

So (A*) is needed only for the fibre laws of the **full** family `𝔊_X`
(every ℛ(M), (a,D), Case-A class with modulus ≤ X, plus selectors), with
bounds uniform in X. In particular no adversarial sub-selection of
moduli has to be handled: every sum over classes through a prime is a
complete sum over cofactors (this is what makes divisor-in-progression
averages over moduli available below). Fibres at a smooth part c are
still full in the rough direction (all rough cofactors occur).

**Lemma 1.2 (rational labels and compatibility; PROVED).** Every class of
the four types can be written `b ≡ −r/s (mod G)` with integers `r ≥ 0`,
`s ≥ 1`, `gcd(s,G) = 1`; call the rational `λ = −r/s` (in lowest terms) a
*label* of the class and `H(λ) = max(|r|, s)` its height. Labels can be
chosen with:
* ℛ(M), `A = (M+1)/4`, class `−4D`, `D | A²`, `D' = A²/D`:
  `λ = −4D` if `D ≤ A`, else `λ = −1/(4D')` (then `D' < A`); `H(λ) ≤ M+1`.
  (`4A ≡ 1 (M)` gives `D' ≡ 1/(16D)`, so `−1/(4D') ≡ −4D (mod M)`.)
* (a,D), `G = 4ag`, class `−(4D+a)`: `λ = −(4D+a)`, `H ≤ 4g² + a ≤ G²`.
* Case A, `G = 4rh`, `m·m' = 4rh² + 1`, class `−1/m`: since
  `4rh² ≡ 0 (G)`, `m m' ≡ 1` and `−1/m ≡ −m' (mod G)`; take
  `λ = −1/m` if `m ≤ m'`, else `λ = −m'`; `H ≤ √(4rh²+1)+1 ≤ G`.
* selector `0 mod p`: `λ = 0`, `H = 1`.

**Compatibility.** If two labels `λ₁ = −r₁/s₁ ≠ λ₂ = −r₂/s₂` (as rationals)
satisfy `λ₁ ≡ λ₂ (mod g)` (with `gcd(s₁s₂, g) = 1`), then
`g | r₁s₂ − r₂s₁ ≠ 0`, so `H(λ₁)H(λ₂) ≥ g/2`. Consequently a residue class
`c mod g` contains **at most one** label of height `< √(g/2)`.

*Proof.* The label formulas are the displayed congruences (for ℛ(M):
`16DD' = 16A² ≡ 1 (M)`; for Case A: `m m' ≡ 1 (G)`). Compatibility:
`λ₁ ≡ λ₂` means `r₁s₂ ≡ r₂s₁ (g)`, and `|r₁s₂ − r₂s₁| ≤ 2H₁H₂`. Two labels
of height `< √(g/2)` in one class would have `H₁H₂ < g/2`. ∎

*Why labels.* Classes with the **same** label λ (any moduli) have the same
residue at every common prime; at a point `y` their membership is
governed by the single set `Z_λ(y) = {p : y ≡ λ (mod p^{e_p})}`. So
coincidences between classes are of two kinds: *same label* (exact,
product-type, the "structured" case of LS4 §3.2) and *different labels*,
which by Lemma 1.2 cost height: one of the two labels is `≥ √(g/2)`.

## 2. Replacing the threshold conditioning by an exponential tilt

LS4 obtains (B) by conditioning the capped fibre law on the global event
`G_B = {Σ_ℓ w_ℓp̃_ℓ ≤ B} ∩ 𝒜` (Prop 4.1). For (A*) at large support this
is a bad choice (§3): `Σ_ℓ w_ℓp̃_ℓ` is moved by *every* coordinate (see
Remark 3.1), so a sharp threshold couples all coordinates, and the
pivotal method of LS4 (which takes absolute values pointwise in the coins)
cannot see the smoothing that makes the true correlation small. An
exponential tilt gives (B) equally cheaply and has **product structure**.

**Setting 2.0.** Q' is the capped fibre law of LS4 Setting 4.0 (caps
`δ_ℓ ≤ 1/2`), `Y(x) = Σ_ℓ w_ℓ p̃_ℓ(x)` with `w_ℓ ∈ [0,1]`, `𝒜` the avoider
set, and

    σ_tilt(x) := Q'(x)·1_𝒜(x)·e^{−2Y(x)} / Z,    Z = E_{Q'}[1_𝒜 e^{−2Y}].

**Proposition 2.1 ((B) for the tilted law; PROVED).**
`E_T 𝓡_2((σ_tilt)_T) ≤ Z^{−2}`, and `Z ≥ Q'(𝒜)·exp(−2E_{Q'}[Y]/Q'(𝒜))`.
In particular if `Q'(𝒜) ≥ 3/4` then
`log E_T𝓡_2((σ_tilt)_T) ≤ (16/3)E_{Q'}Y + 2 log(4/3)`.

*Proof.* By Lemma 1.1 of LS4,
`E_T𝓡_2 = E_{σ⊗σ}Π_ℓ(1+w_ℓh_ℓ) = Z^{−2}E_{Q'⊗Q'}[Φ(x)Φ(x')Π_ℓ(1+w_ℓh_ℓ)]`,
`Φ = 1_𝒜e^{−2Y} ≥ 0`. The tilting identity of LS4 Lemma 2.1 holds with any
non-negative functional of the pair path inserted (LS4 §4: `dQ/d(Q'⊗Q') =
Π_ℓZ_ℓ`), so this equals `Z^{−2}E_Q[Φ(x)Φ(x')Π_ℓ(1+w_ℓη_ℓ)]`. As in Prop
4.1, `η_ℓ ≤ p̃_ℓ(x)/(1−p̃_ℓ(x)) ≤ 2p̃_ℓ(x)`, so `Π(1+wη) ≤ e^{2Y(x)}`, and
`Φ(x)e^{2Y(x)} ≤ 1`, `Φ(x') ≤ 1`. Lower bound: Jensen,
`Z = Q'(𝒜)E[e^{−2Y}|𝒜] ≥ Q'(𝒜)e^{−2E[Y|𝒜]}` and `E[Y|𝒜] ≤ EY/Q'(𝒜)`. ∎

So in Theorem 4.2 of LS4 one may use `σ_c := σ_tilt` for the fibre law
`Q'_c` (on the event `leak_c ≤ 1/4`, `Q'_c(𝒜_c) ≥ 3/4`), with the
collision bound `log E_T𝓡_2 ≤ 6m_c + 1` in place of `2B_c + log 4`;
the rest of the proof of Thm 4.2 is unchanged, and the open input becomes

> **(A\*_tilt)** for c off an exceptional event of probability ≤ 1/32 and
> every θ ≠ 0 with z-rough denominator, `|σ̂_tilt,c(θ)| ≤ Π_{ℓ∈supp θ}Kℓ^{−γ}`.

(Lemma 5.1 / Thm 5.2 of LS4 also hold for σ_tilt: their proof only uses
that the weight is a function of the activated sets and of
avoider-membership, and that nothing changes when no pinned value meets
`R_ℓ`; `e^{−2Y}` is such a function. So the residue-sparse case is not
lost.)

The advantage: `e^{−2Y} = Π_q e^{−2w_q p̃_q}` is a **product of local
factors**, each moved by an activation at q only by a factor
`e^{−2w_q·O(1/q)}`. A change of activation at a top q is therefore
*paid* by `w_q/q` (or by the coin at q), never by a global threshold.

**Remark 2.2 (why not the threshold; Assessment).** For the full family,
for every rough ℓ and every residue `a mod ℓ` there are many tops `q > ℓ`
with a class `(λ, ℓq)`, `λ ≡ a (ℓ)` (the sets `Λ(ℓq)`, `q` varying, cover
`ℤ/ℓ`). Such a class is matched off its top as soon as `x_ℓ ≡ a`, so
**every** value of every rough coordinate changes the activated sets at
many later tops and moves `Y` by `≍ (log)^{O(1)}/ℓ`. Under `σ_B` a change
at ℓ can therefore flip `1_{G_B}` without any further coincidence, and
LS4's pivotal bound (which takes `|·|` pointwise in the coins) only yields
`|σ̂_B(θ)| ≲ 2^{|S|}(log)^{O(1)}/(min_{ℓ∈S}ℓ·B)`: one prime of decay, not
`Π_{ℓ∈S}`. The *true* coefficient is presumably product-small (a smooth
threshold of a sum of weakly dependent terms has `|S|`-th mixed
differences of size `Π_ℓ δ_ℓ`), but the pivotal method cannot see this.
With the tilt, the `|S|`-th mixed difference of `e^{−2Y}` *is* a product
when `Y` is additive across the S-coordinates, and every activation at a
top q enters with the factor `≤ 2w_q/q`.

## 3. The label-partition form of the covering count (product model)

To isolate the arithmetic, consider the **product model** of LS4 §3.2:
`S` a finite set of primes `> z`, `v` uniform on `Ω_S = Π_{ℓ∈S}ℤ/ℓ`,
and the other rough coordinates `y` uniform and independent (the path
law dominates this up to `Π(1+2p^{−1/2})` per matched class, LS4 Lemma 2.1
inflation; transfer to the fibre law is §6). Coordinates are taken
squarefree for readability (prime powers change nothing below but
notation). The family is the full family of Lemma 1.1, restricted to rough
parts; `Λ(G)` is the set of labels of classes of modulus G, and a class
`(λ,G)` is *matched* by a point `u` if `u ≡ λ (mod p)` for all `p | G`. Let

    E_S = {(v,y) : ∀ℓ ∈ S ∃(λ,G), ℓ | G, (λ,G) matched by (v,y)}.

For a label λ and a point u let `Z_λ(u) = {p : u_p ≡ λ (mod p)}`.

**Lemma 3.1 (label partition; PROVED).** For every `(v,y) ∈ E_S` there
are a partition `S = U_1 ⊔ … ⊔ U_k` and **distinct** labels `λ_1,…,λ_k`
such that `v ≡ λ_j` on `U_j`, and for each j a class `(λ_j, G_j)` with
`G_j ∩ U_j ≠ ∅`, matched by (v,y). For such a class,
`G_j ∩ S ⊆ U_j ∪ CS_j`, where

    CS_j := {q ∈ S∖U_j : λ_{j(q)} ≡ λ_j (mod q)}   (j(q): the block of q)

depends only on the partition and the labels. Consequently

    P(E_S) ≤ Π_{ℓ∈S} ℓ^{−1} · Σ_{(U_j)} Σ_{(λ_j) distinct} P_y(∀j ∃ m_j :
             (λ_j, Q_jm_j) a class for some Q_j ⊆ U_j∪CS_j with Q_j∩U_j ≠ ∅,
             y ≡ λ_j on m_j).

*Proof.* Pick for each ℓ a matched witness class through ℓ, let λ(ℓ) be
its label (then `v_ℓ ≡ λ(ℓ)`), and group S by λ(ℓ). For `q ∈ G_j ∩ S` the
class being matched gives `v_q ≡ λ_j`; also `v_q ≡ λ_{j(q)}`, so either
`q ∈ U_j` or `λ_j ≡ λ_{j(q)} (q)`. Given the partition and labels, `v` is
determined on S, the event `{v ≡ λ_j on U_j ∀j}` has probability exactly
`Π_S ℓ^{−1}` (independent coordinates), and the remaining conditions
concern y only. Union bound over partitions and labels. ∎

*Remarks.* (a) Same-label coincidences have disappeared: all classes with
one label act through the single residue vector `λ mod S` — this is the
exact form of LS4 §3.2's "structured coincidences collapse".
(b) What is left are **cross-label coincidences** at S-primes (`CS_j`;
an S-prime in `CS_j` is *free* for block j: no `1/q` is paid for it) and
at outside primes (two witness moduli sharing an outside prime p need
`λ_j ≡ λ_{j'} (p)`). By Lemma 1.2 every cross-label coincidence at p
forces `H(λ_j)H(λ_{j'}) ≥ p/2`, and two distinct labels coincide at no
more than `log(2H(λ_j)H(λ_{j'}))/log z` primes `> z`.

## 4. What the label reduction leaves: three correlation inputs

By Lemma 3.1, (CC) in the product model reduces to bounding, for each
partition `S = ⊔U_j` and distinct labels `λ_j`,

    Σ_{(λ_j)} P_y(∀j : block j has a witness)  ≤  Π_{ℓ∈S} K ℓ^{1−γ}.     (4.1)

(The `Π ℓ^{−1}` is already exact; the slack per S-prime is `ℓ^{1−γ}`.)
Write `Mass(Q') := Σ_m |Λ(Q'm)|/m` (m over rough squarefree outside
cofactors, `Q'm ≤ X`); by Shiu's theorem in progressions (A runs over an
AP mod Q') plus `τ(A²) ≤ A^{O(1/log log A)}` for the short range,
`Mass(Q') ≤ C(log X)³ + Q'^{O(1/log log Q')}` (standard; this is the
uniform first moment used in K2/KARY3). Three kinds of correlation remain.

**(C1) Same-label coincidences — solved exactly** (Lemma 3.1: they
collapse to one residue vector). In particular the "structured families"
of LS4 §3.2 (`−4d` over all `Q ⊆ S`) cost `Π_ℓ τ(F²)/ℓ` with no
cover-counting.

**(C2) S-coincidences (free S-primes).** Block j may use any
`Q_j ⊆ U_j ∪ CS_j`; the union bound over `Q_j` costs `2^{|U_j|+|CS_j|}`
and `|CS_j| ≤ |S|`. Trivially this gives a factor `≤ 2^{2|S|}` per block,
i.e. `≤ 4^{|S|}` per S-prime: harmless iff `|S| ≤ (1/2 − γ)log₂ z`.
Lemma 1.2 shows each cross-label S-coincidence at q forces
`H(λ_j)H(λ_{j(q)}) ≥ q/2`, so (C2) is a statement about how often a
label can be congruent, at many S-primes, to *other labels of the same
configuration*. (Big groups — `≥ log₂ q` distinct labels of one
configuration congruent mod one prime q — are the only case not
absorbed by the per-prime slack.)

**(C3) Outside sharing.** Witness moduli of different blocks may share
outside primes p, which requires `λ_j ≡ λ_{j'} (p)`. Without using this
compatibility, the union bound over which blocks share which primes gives
`Π_{p ≤ X}(1 + (2^k − k − 1)/p) ≤ (C log X/log z)^{2^k}` (k = number of
blocks): harmless iff `2^k log log X ≲ (log N)^{1/4}`. With
compatibility the shared primes of a pair of labels are among the
`≤ log(2HH')/log z` prime factors of `num(λ_j − λ_{j'})`, which would make
(C3) negligible — **but only if the weights can be summed with p fixed
first**, and the witness weight of a label is not uniform in the modulus
(see (S) below).

**Corollary 4.2 (product model, tiny supports; PROVED modulo the Mass
bound above).** If `|S| ≤ c₀ log log N` (`c₀` small absolute) and
`log X ≤ z^{γ/8}`, then in the product model
`P(E_S) ≤ Π_{ℓ∈S} K ℓ^{−γ}` with `K = z^{γ/2}` for `N ≥ N₀(γ)`.

*Proof.* Lemma 3.1; Bell(|S|) partitions; per block the label sum is
`≤ Σ_{Q ⊆ S}Mass(Q·e) ≤ 2^{|S|}(C(log X)³ + M_S^{o(1)})` for each fixed
set e of shared outside primes; (C3) without compatibility costs
`(C log X/log z)^{2^{|S|}}`. Altogether
`P(E_S) ≤ Π_{ℓ∈S}ℓ^{−1}·|S|^{|S|}·(2^{|S|}C(log X)³)^{|S|}·M_S^{o(1)}
·(C log X)^{2^{|S|}}`, and with `2^{|S|} ≤ (log N)^{c₀}` every factor is
`≤ z^{γ/4}` per S-prime once N is large (`ℓ > z`). ∎

This is far from what (A*) needs (`|S|` up to `(log N)^{3/4}`), and it is
stated only to calibrate: **the whole difficulty of (CC) is (C2) and (C3)
for configurations with many distinct labels.**

**(S) Why pointwise divisor-in-residue-class bounds do not suffice
(Assessment, with the computation).** For `λ = −4D` and a fixed part Q',
`λ ∈ Λ(Q'm) ⟺ Q'm ≡ −1 (mod 4D^♮)`, `D^♮ = Π p^{⌈v_p(D)/2⌉}`. Hence the
witness weight `ν(λ,Q') = Σ_m [λ ∈ Λ(Q'm)]/m` splits as
* a **long** part (`m ≥ 4D^♮`): `≤ 2(1+log X)/D^♮`, uniform in Q' — these
  witnesses behave like random residues, and (C2), (C3) for them are
  harmless (the label sum converges and congruence conditions mod p cost
  `≍ 1/p` on average by Lemma 1.2 and Shiu in progressions);
* a **short** part: at most one `m < 4D^♮` (namely `m ≡ −1/Q' mod 4D^♮`),
  contributing up to 1, **for every label, however high**.
Short witnesses are classes whose label height exceeds the outside
cofactor; for such classes the label is (nearly) determined by the
modulus, and the sup over residue classes of `#{D | A² : D ≡ c}` is
attained. Lenstra / Coppersmith–Howgrave-Graham–Nagaraj bound this count
by `O(1)` only when the prescribed modulus exceeds `A^{1/2+ε}`, which
removes the `τ(A²)` but **not** the lack of decay in the shared modulus g:
in (C2)/(C3) one needs `Σ_{g | L}(weight of labels ≡ c mod g) ≪ 1`
summed over the `2^{ω(L)}` divisors g of the already-constrained part L,
and with short witnesses each g can carry weight `≍ 1`. So the
remaining input is an **averaged** label–pair correlation statement
(averaging over the moduli and labels of *both* blocks), not a pointwise
divisor bound. The random-residue model predicts (4.1) with
`K = (log X)^{O(1)}` for all |S| (each overlap costs exactly what its
compatibility saves; LS4 §3.2's heuristic), and no ES configuration
violating it is known.

> **(LCH) label-correlation hypothesis** (CONJECTURE; sufficient for (CC)
> in the product model). For every finite set S of primes `> z`, every
> partition `S = ⊔_{j≤k}U_j` and every choice of witness S-parts, the sum
> over distinct labels `λ_1,…,λ_k` and witness moduli of
> `Π_j[λ_j ∈ Λ(G_j)]·[compatibility at every shared prime]/lcm(outside parts)`
> is `≤ Π_j (C(log X)^C)^{|U_j|}·2^{O(|S|)}`.
