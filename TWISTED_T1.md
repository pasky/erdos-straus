# TWISTED_T1 — "T1 of order k": twisted Erdős–Straus targets, anchors, and cubic obstructions (task O182, spark relay I)

Status: in progress (O182). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on DRINFELD_ES.md (O181, CLAIMED, under review R181), KUDLA_ES.md §1, FUNCTIONFIELD_ES.md. Scripts
`scripts/tw_*`, memos `BRAINSTORM/bsI_*.md`.

Notation. For a field K ⊇ μ_m and ζ ∈ μ_m primitive, (a, b)_ζ ∈ Br K[m] is the cyclic algebra; for a place v,
⟨a, b⟩_v := inv_v (a, b)_ζ ∈ (1/m)ℤ/ℤ (identified with ℤ/m). For a twisted target λ = Σ c_i/X_i we put
u_i := X_i/c_i, so λ = Σ 1/u_i is the Bright–Loughran surface, and α(u) := (−u₁/u₃, −u₂/u₃)_ζ (DRINFELD_ES §2).

## 0. Iteration log
(I1) Brief's candidate: over F_q[T] with c₁ + c₂ + c₃ = 1 "all three denominators of minimal degree" might pin the
∞-invariant. **Killed (Lemma 1.1): that configuration never occurs when deg A ≥ 1** — the prime power P must divide
a denominator. Hypothesis violated by the idea: "the degree coordinate is free". Modification: isolate the exact
algebraic condition under which a normalisation pins an invariant (§2, Anchor Lemma) and look for places where it
can hold with order m ≥ 3.

## 1. Function fields: the c₁ + c₂ + c₃ = 1 case is vacuous; the ∞-invariant is a determinant

Setting (DRINFELD_ES §3): ES_q^c(A, P): A/P = c₁/X₁ + c₂/X₂ + c₃/X₃, X_i ∈ F_q[T] monic, deg X_i ≥ n − k
(n = deg P, k = deg A ≥ 1, P monic, P = Q^e with Q irreducible, Q ∤ A), c ∈ (F_q^*)³, m | q − 1 odd.

**Lemma 1.1 (all-minimal configuration is impossible; PROVED).** Under the setting, at least one X_i has degree
≥ n > n − k. In particular no solution has all three denominators of the minimal degree n − k, whatever c is.
*Proof.* v_Q(A/P) = −e. If v_Q(c_i/X_i) ≥ −e + 1 for all i then v_Q(Σ) ≥ −e + 1, contradiction. So some X_i has
v_Q(X_i) ≥ e, deg X_i ≥ e·deg Q = n. ∎
(For k = 0, A = 1, the all-minimal configuration exists — e.g. X₁ = X₂ = X₃ = P when c₁ + c₂ + c₃ = 1 — but this
is the degenerate "1/n" problem.) So the hoped-for degeneration of the degree character does not exist: Lemma 3.2
of DRINFELD_ES always applies. Its formula has a symmetric form:

**Proposition 1.2 (∞-invariant = a determinant; PROVED).** Write d_i = deg X_i and fix a generator of
F_q^*/F_q^{*m} ≅ ℤ/m, w_i := class of c_i. For every solution u of ES_q^c, the odd-order (order m) part of
inv_∞ α(u) equals, up to a global sign convention,
`χ_∞(u) = det [[1, 1, 1], [w₁, w₂, w₃], [d₁, d₂, d₃]] = w₁(d₂ − d₃) + w₂(d₃ − d₁) + w₃(d₁ − d₂)  (mod m).`
*Proof.* At ∞ (uniformiser 1/T), a = −u₁/u₃ has sign −c₃/c₁ and valuation d₃ − d₁; b = −u₂/u₃ has sign −c₃/c₂ and
valuation d₃ − d₂. Tame symbol {a, b}_∞ = (−1)^{v(a)v(b)} sgn(a)^{v(b)} sgn(b)^{−v(a)}; discarding ±1 (order 2,
m odd): (c₃/c₁)^{d₃−d₂}(c₃/c₂)^{d₁−d₃}; taking logs gives (w₃ − w₁)(d₃ − d₂) + (w₃ − w₂)(d₁ − d₃), which expands
to the determinant. ∎
(It agrees with DRINFELD_ES Lemma 3.2 whenever the minimal-degree c's sum to 1, which Lemma 1.1 and the leading-term
identity guarantee; the determinant form is manifestly antisymmetric under relabelling, as α is.)

**Corollary 1.3 (exact scope of the function-field order-m T1; PROVED from DRINFELD_ES Thm 3.3).** At P = Q^m, every
Type I/II-shaped solution satisfies det(1, w, d) ≡ 0 (mod m). This is a condition on the vector of degrees only;
it is vacuous iff all w_i are equal (c_i/c_j ∈ F_q^{*m}), i.e. iff the twist is trivial mod m-th powers.
(R182 repair D8: "vacuous" = the linear form is identically 0; that the condition bites on *realised* degree
vectors is DRINFELD_ES's EVIDENCE tables, not part of this proof.)
*Proof.* Thm 3.3 + Lemma 3.1 + reciprocity give χ_∞(u) = 0; if the w_i are not all equal, the linear form
d ↦ det(1, w, d) is non-zero on ℤ³ (e.g. d = (1,0,0) gives w₂ − w₃ or a permutation is ≠ 0). ∎

## 2. The anchor calculus: which normalisations can pin an order-m invariant

(I2) Abstracting what T1 uses: a place where a *normalisation* of the denominators (positivity, monic, primary,
congruence) pins inv_v α to a constant, and a reciprocity argument. Below: exact conditions.

Fix a place v of K ⊇ μ_m, V_v := K_v^*/K_v^{*m}, and the Hilbert pairing ⟨·,·⟩_v : V_v × V_v → ℤ/m.
It satisfies ⟨a, a⟩ = ⟨a, −1⟩; **for odd m it is alternating** (−1 = (−1)^m), for m = 2 it is symmetric
but not alternating at v where ⟨−1, −1⟩_v ≠ 0 (v real, v = 2 over ℚ). A *normalisation* at v is a subgroup
N_v ⊂ K_v^* in which the denominators X_i are required to lie; N̄_v is its image in V_v. Put
`τ₁ := −c₃/c₁, τ₂ := −c₃/c₂` (the *twisted targets*; for ES, c = (1,1,1), τ₁ = τ₂ = −1).

**Lemma 2.1 (anchor lemma; PROVED, linear algebra).** As X ranges over N_v³, the value inv_v α(X/c) is constant
iff N̄_v is isotropic (⟨N̄_v, N̄_v⟩ = 0) and τ₁, τ₂ ∈ N̄_v^⊥. The constant is then ⟨τ₁, τ₂⟩_v, which for odd m equals
`⟨c₁, c₂⟩_v + ⟨c₂, c₃⟩_v + ⟨c₃, c₁⟩_v.`
*Proof.* α(X/c) = (τ₁r, τ₂s) with r = X₁/X₃, s = X₂/X₃; as X ranges over N_v³, (r, s) ranges over all of N_v²
(take X₃ = 1). By bilinearity inv_v = ⟨τ₁, τ₂⟩ + ⟨τ₁, s⟩ + ⟨r, τ₂⟩ + ⟨r, s⟩. Constancy with r = 1 (resp. s = 1)
forces τ₁ ⊥ N̄ (resp. τ₂ ⊥ N̄), and then ⟨r, s⟩ = 0. Converse clear. For odd m, ⟨−x, y⟩ = ⟨x, y⟩ and
⟨c₃/c₁, c₃/c₂⟩ expands, by antisymmetry and ⟨c₃, c₃⟩ = 0, to the cyclic sum. ∎
(This is the *normalisation-only* anchor; the equation itself may pin further invariants — e.g. the partner
vanishing at λ in the proof of Thm 3.2 and Principle (β) below. R182 repair D6: formerly pointed to a
non-existent "Lemma 2.4".)

**Corollary 2.2 (catalogue of natural normalisations; PROVED).**
(a) v real, m = 2, N_v = ℝ_{>0} (positivity): N̄ = 0, anchor ⟨τ₁, τ₂⟩_∞ = ½ iff τ₁, τ₂ < 0 (e.g. all c_i > 0).
This is the ES anchor: ⟨−1, −1⟩_∞ = ½ (Hamilton quaternions).
(b) v complex: V_v = 0, no anchor of any order.
(c) v = ∞ of F_q(T), N_v = monic (Hayes sign): V_v ≅ F_q^*/F_q^{*m} × ℤ/m (sign × degree), N̄ = ⟨T⟩ is
**Lagrangian** (order m in a non-degenerate alternating space of order m², isotropic as ⟨T, T⟩ = ⟨T, −1⟩ = 0).
So τ_i ⊥ N̄ forces τ_i ∈ N̄ and the anchor is ⟨N̄, N̄⟩ = 0; otherwise the invariant is the degree character of
Prop 1.2. **No twist by constants anchors anything at ∞ over F_q(T).** (DRINFELD_ES §3 "degree unpinnable", now as
a one-line structural fact.)
(d) v tame finite, N_v = O_v^* ("v-unit"): N̄ = units, again Lagrangian ⇒ anchor 0 or non-constant.
(e) v tame finite, N_v = 1 + 𝔪_v ("≡ 1 mod v"): a pro-ℓ group with ℓ ∤ m, hence m-divisible: N̄ = 0, and every
τ gives a pinned anchor ⟨τ₁, τ₂⟩_v (non-zero only if some τ_i has v(τ_i) ≢ 0 mod m).
(f) v = λ = (1 − ζ₃) over ℚ(ζ₃), m = 3, N_v = ±(1 + 3O_λ) ("x ≡ ±1 mod 3", the cubic-reciprocity *primary*
normalisation up to the cube −1): N̄ = U^{(2)}K^{*3}/K^{*3} has order 9 in V_λ (order 3^{2+2} = 81) and is isotropic
because ⟨U^{(i)}, U^{(j)}⟩ = 0 for i + j > pe/(p − 1) = 3; hence Lagrangian, anchor 0 or non-constant.
(R182 repair D7: the general conductor bound is quoted from memory and was not checked against a source; the
instance used here is verified by R182 from the norm-residue definition (`scripts/review_tw_zw.py`):
⟨1+λ², 1+λ³⟩_λ = 0, hence ⟨U^{(2)}, U^{(2)}⟩ = 0; the bound is sharp, ⟨1+λ, 1+λ²⟩_λ ≠ 0. Hand proof of the
instance: 1+λ³ ∈ U^{(3)} = U^{(pe/(p−1))} has an unramified Kummer extension, so it pairs trivially with units.)
*Proof.* (a), (b) standard. (c) tame symbol: ⟨T, c⟩ = c^{±1}, ⟨c, c'⟩ = 0 for constants. (d) tame symbol of two
units is 1; ⟨π, u⟩ = ū^{±1}, so units = units^⊥. (e) clear. (f) the bound on ⟨U^{(i)}, U^{(j)}⟩ is the standard
conductor estimate for the p-th Hilbert symbol (Fesenko–Vostokov Ch. IV; Serre, *Local Fields*, XIV); orders from
|K^*/K^{*p}| = p^{2+[K:ℚ_p]} and U^{(4)} ⊂ K^{*3} (U^{(i)} ⊂ K^{*p} for i > pe/(p − 1)). Isotropic of order
√|V| in a non-degenerate alternating space ⇒ Lagrangian. ∎

**Proposition 2.3 (an anchor needs a ramified constant algebra; PROVED).** Suppose the anchors at the normalised
places S are pinned (Lemma 2.1) and the total anchor A_S := Σ_{v∈S} ⟨τ₁, τ₂⟩_v is non-zero. Then the constant
cyclic algebra (τ₁, τ₂)_ζ ∈ Br K is ramified at some w ∉ S (reciprocity: Σ_all v ⟨τ₁, τ₂⟩_v = 0).
Consequences: (i) **F_q(T), constant twists: never** — (τ₁, τ₂) is a symbol of two constants, unramified
everywhere (tame symbols of units; also at ∞), so it is 0 in Br F_q(T). (ii) **ℚ(ζ₃), unit twists c_i ∈ μ₆: never**
— units are tame-trivial at all v ∤ 3, and at λ ⟨ζ^a, ζ^b⟩ = ab⟨ζ, ζ⟩ = ab⟨ζ, −1⟩ = 0. So the brief's
"ζ₃ as an order-3 target" does not anchor: for odd m a single target t never anchors (⟨t, t⟩ = 0); two
independent constants with ⟨τ₁, τ₂⟩ ≠ 0 are needed. (iii) ES over ℚ: (−1, −1) = Hamilton quaternions, ramified at
{∞, 2}: anchor ∞, *partner* 2.
**Principle (Assessment, made precise by 2.1–2.3).** "The T1 obstruction for target −1 has order 2" is literally:
the anchor is ⟨−1, −1⟩, which is non-zero only because the m = 2 Hilbert symbol is not alternating. For odd m an
order-m T1 needs (α) a pinned normalised place v₀ (Lagrangian normalisations — monic, unit, primary — never pin a
non-zero value), and (β) a partner place w where the constant algebra (τ₁, τ₂) ramifies but the *equation*
forces inv_w α(u) = 0 on all integral points (for ES: w = 2, forced by the numerator 4 — BL).

## 3. A genuine order-3 T1 over the Eisenstein integers (anchor at 2, partner at λ)

(I3) Prop 2.3 says what to build: a normalised tame place v₀ with N̄ = 0 (Cor 2.2(e)), twist constants with
⟨τ₁, τ₂⟩_{v₀} ≠ 0, and a wild partner where the *numerator* kills the invariant (as 4 = 2² does for ES at 2).
Over K = ℚ(ω), ω = ζ₃, O = ℤ[ω], λ = 1 − ω (v_λ(3) = 2, v_λ(9) = 4), take v₀ = (2) (inert, residue field F₄)
and numerator 9.

**Normalisation.** x ∈ O is *2-primary* if x ≡ 1 (mod 2O). Every x prime to 2 has exactly two 2-primary
associates ±x (the units ±ω^j map onto F₄^* = {1, ω, ω²}): 2-primary is the Eisenstein analogue of positivity /
monic — a choice of associate up to the cube −1. (R182 repair D3: more precisely it is the kernel of reduction
at the anchor, the analogue of the kernel of sign; unlike positivity/monic it also **excludes denominators
divisible by the anchor prime 2**.)

**Definition (TES).** For n ∈ O prime to 6: TES(n) is the equation
`9/n = ω/x + ω²/y + 2/z,  x, y, z ∈ O 2-primary.`
Here c = (ω, ω², 2), u = (x/ω, y/ω², z/2), α(u) = (−u₁/u₃, −u₂/u₃)_ω ∈ Br K[3]. For a prime π ∤ 6 and n = π^e,
a solution has *Type I shape* if (v_π(x), v_π(y), v_π(z)) is a permutation of (≥ e, 0, 0), *Type II shape* if a
permutation of (0, ≥ e, ≥ e) (the ES shapes).

**Lemma 3.1 (local condition at 2; PROVED).** If TES(n) is solvable then n ≡ 1 (mod 2). *Proof.* Reduce mod 2:
9/n ≡ 1/n, and ω/x + ω²/y + 2/z ≡ ω + ω² = −1 ≡ 1 (mod 2). ∎ (So the associate of n is fixed; every cube
n = m³, m prime to 2, satisfies it, since F₄^* has exponent 3.)

**Theorem 3.2 (cubic reciprocity law and order-3 T1 for TES; PROVED).** Let n ∈ O, n ≡ 1 (mod 2), gcd(n, 6) = 1.
(a) For every solution of TES(n): Σ_{π | n} inv_π α(u) = −⟨ω, 2⟩₂ ≠ 0 in (1/3)ℤ/ℤ.
(b) **(T1₃.)** If n = π^{3k} (k ≥ 1; R182 repair D1: formerly only π³) with π prime, π ∤ 6, then TES(n) has no
solution of Type I or Type II shape at π.
(c) If n = π is prime, every solution has inv_π α(u) = −⟨ω, 2⟩₂ (a fixed non-trivial cubic residue value).
*Proof.* Compute inv_v α(u) at every place.
*v = (2) (anchor).* x, y, z ∈ 1 + 2O₂ = U^{(1)}, a pro-2 group, hence 3-divisible: u_i ≡ 1/c_i modulo cubes.
By Lemma 2.1 (N̄ = 0), inv₂ α = ⟨c₁, c₂⟩ + ⟨c₂, c₃⟩ + ⟨c₃, c₁⟩ = ⟨ω, ω²⟩ + ⟨ω², 2⟩ + ⟨2, ω⟩ = 0 + 2⟨ω, 2⟩ −
⟨ω, 2⟩ = ⟨ω, 2⟩₂ (units pair trivially at a tame place). The tame symbol {ω, 2}₂ = ω mod 2, whose cubic class in
F₄^* is ω^{(4−1)/3} = ω ≠ 1. So inv₂ α ≠ 0.
*v = λ (partner).* The c_i are λ-units and n is a λ-unit, so u_i ∈ O_λ. If u₂ + u₃ = 0 (any labelling), α(u) =
(−u₁/u₃, 1) = 0. Otherwise relabel so that v_λ(u₁) is maximal (this changes α by a sign, DRINFELD_ES Thm 2.2 proof)
and apply the Steinberg decomposition (DRINFELD_ES Lemma 2.1): α = (y, −1) + (x, y), x = (9/n)u₁ − 1. Since
v_λ(9u₁/n) ≥ 4, −x ∈ U^{(4)} = (U^{(2)})³ (for i > e/(p − 1) = 1, the p-th power map U^{(i)} → U^{(i+e)} is
bijective; Neukirch, ANT II (5.5)–(5.8)), so x = (−1)³·(−x) is a cube and (x, y) = 0; (y, −1) = 0 as −1 is a
cube. So inv_λ α = 0. **This is where the numerator 9 = (unit)·λ⁴ is used** (3 = (unit)·λ² does not suffice).
*v tame, v ∤ 6n.* The u_i are v-integral and 9/n is a v-unit: DRINFELD_ES Thm 2.2 (i) verbatim — either
x ≡ −1 is a unit and the symbol is ±1, or all u_i are units and the symbol is 1 or y ≡ 1 — so inv_v α ∈ ½ℤ/ℤ,
hence 0 in (1/3)ℤ/ℤ.
*v complex.* Br ℂ = 0.
Hilbert reciprocity (Σ_v inv_v = 0 for α(u) ∈ Br K) now gives (a), and (c) is (a) with one place. For (b):
DRINFELD_ES Thm 3.3's proof (a tame valuation argument at Q, using only v_Q(λ) = −m, Q-integrality of the u_i and
m-th powers in k(Q)^*) applies verbatim at π with m = 3, giving inv_π α(u) = 0 for Type I/II shapes,
contradicting (a). (Same for π^{3k}: the symbols are y^{±3k}.) ∎

**Numerics (EVIDENCE; `scripts/tw_eis_solve.py`, `scripts/tw_eis_scan.py`; every solution verified exactly;
inv_λ obtained as −Σ_tame by reciprocity, the reciprocity code itself checked on 400 random pairs with a ∈ U^{(4)}:
Σ_tame = 0 in all).** Search: all solutions having some denominator X with N(X − c_i n/9) ≤ 30 (the ES regime,
E = 9X − c_i n small). (R182 repair D4: as implemented, X = round(c_i n/t) + δ with N(δ) ≤ B; R182's exact window
N(tX − c_i n) ≤ N(t)B reproduces the TES and (9;1,1,1) rows identically and the t = 3 control as primes 658/301,
cubes 308/164/1504, π⁶: 0 of 56. R182 repair D2: R182 computed inv_λ directly from the norm-residue definition —
0 on every TES point — and cross-checked reciprocity on random pairs with non-trivial λ-symbol.)
| target | n | #n | Type I | Type II | other | invariants (2, π, λ) |
|---|---|---|---|---|---|---|
| TES (9; ω, ω², 2) | split primes, N ∈ [307, 1471] | 8 | 117 | 44 | 0 | all (1, 2, 0) |
| TES | π³, N(π) ∈ {7, 13, 19, 31, 37} | 5 | **0** | **0** | 87 | all (1, 2, 0) |
| control: no anchor (9; 1, 1, 1) | primes / cubes | 8 / 5 | 51 / 42 | 9 / 6 | — / 96 | all 0 |
| control: no partner (3; ω, ω², 2) | primes / cubes | 8 / 5 | 660 / 306 | 299 / 164 | — / 1493 | inv₂ = 1; (π, λ) vary |
Every tabulated prime has Type I/II solutions (not every prime in a window: §5, R182 repair D5); every cube has
only "other"-shape solutions (e.g. those inherited from π:
9/π = Σ c_i/x_i ⇒ 9/π³ = Σ c_i/(π²x_i), shape (2, 2, 2)); in particular TES(π³) is globally, hence locally,
solvable (R182 repair D5: PROVED whenever TES(π) is solvable — π 2-primary gives π² ≡ 1 (mod 2), so (π²x_i) is
a solution; TES(π) itself is EVIDENCE). Both hypotheses of Thm 3.2 are needed: dropping the anchor (c = 1) or the partner (numerator 3)
restores Type I/II solutions at cubes.
*Exponent law (EVIDENCE, same search):* n = π² (N(π) = 7): Type I 2, II 1; n = π⁴: Type I 1; n = π⁶ (B = 20):
Type I/II 0 of 57; inert cubes n = 5³, 11³: Type I/II 0 of 46, 0 of 192. As predicted by the Remark after Thm 4.1 below
(T1₃ holds at π^e iff 3 | e — "iff" only in the sense that the proof's symbol y^{±e} is a cube iff 3 | e).

## 4. The general principle: T1_m = anchor + partner + tame vanishing (odd m)

**Theorem 4.1 (T1_m template; PROVED).** Let K be a number field, m ≥ 3 odd, μ_m ⊂ K, ζ ∈ μ_m primitive.
Data: a numerator t ∈ O_K, twists c ∈ (O_K ∖ 0)³, a finite set S of finite places with normalisations
N_v ⊂ K_v^* (v ∈ S), and n ∈ O_K prime to S, to m and to t·c₁c₂c₃. Equation TW(n): t/n = Σ c_i/x_i,
x_i ∈ O_K, x_i ∈ N_v for v ∈ S. Assume:
(A) [anchor] for v ∈ S, N̄_v is isotropic and τ₁ = −c₃/c₁, τ₂ = −c₃/c₂ lie in N̄_v^⊥ (Lemma 2.1);
(P) [partner/wild] for every v | m with v ∉ S: c_i are v-units and v(t) ≥ i_v, where U_v^{(i_v)} ⊂ K_v^{*m};
(U) [tame] for every finite v ∉ S, v ∤ mn: c_i are v-units.
Put A_S := Σ_{v∈S} ⟨τ₁, τ₂⟩_v. Then:
(a) every solution satisfies Σ_{v | n} inv_v α(u) = −A_S;
(b) if A_S ≠ 0, n = π^e with π prime, π ∤ m, and m | e, TW(n) has no solution of Type I or Type II shape at π;
*Remark (R182 repair D10: formerly item (c) under the PROVED label).* If m ∤ e, the proof's local symbol at π for
Type I/II shapes is y^{±e}, which the argument does not constrain (observation, not a theorem).
*Proof.* As Thm 3.2: v ∈ S by (A) and Lemma 2.1; v | m, v ∉ S by (P) (the u_i are v-integral, so choosing u₁ of
maximal valuation, −x = 1 − (t/n)u₁ ∈ U^{(i_v)} is an m-th power, as is −1); tame v ∤ n by (U) and DRINFELD_ES
Thm 2.2(i); archimedean v: Br ℂ = 0, and real places have Br ℝ[m] = 0 for odd m; reciprocity gives (a); at π the
Thm 3.3 computation gives symbols ±y^{e} or ±y^{−e} (Type II, resp. the only non-trivial Type I case), which are
m-th powers when m | e (the sign is an m-th power since m is odd). ∎
*Remarks.* (1) For m = p prime, i_v = ⌊p·e_v/(p − 1)⌋ + 1 suffices (Neukirch II (5.5)); for ℚ(ω), v = λ:
e = 2, i_λ = 4, i.e. 9 | t. (2) S may be empty: then A_S = 0 and (a) says Σ_{v|n} inv_v α = 0 — the odd-order
twisted version of Thm 2.2 (no T1). (3) **Over a function field the template is void for constant twists**
(Prop 2.3(i)) — and ∞ must be in S (the denominators are integral only away from ∞), where the only natural
normalisation (monic) is Lagrangian with free degree. (4) The template does **not** cover ES itself (m = 2):
there the anchor is ⟨−1, −1⟩_∞ (non-alternating), tame places only give inv ∈ ½ℤ/ℤ (no information for m = 2),
and the vanishing at the wild partner 2 would need v₂(t) ≥ 3, whereas t = 4 has v₂ = 2; ES's T1 rests on the finer quadratic analysis (KUDLA_ES Thm 1.2 / BL). So ES's T1 is the m = 2
member of a family whose odd members are *strictly easier* to prove (Assessment; R182 repair D13: m = 2 is
outside the template, so "family" is an analogy).

**Corollary 4.2 (what an order-m T1 needs, in one line).** Odd m: a non-zero anchor needs a place where the
normalisation is *not* Lagrangian (Cor 2.2: monic / unit / primary never qualify; congruence normalisations
"≡ 1 mod v" at tame v do), plus a constant algebra (τ₁, τ₂) ramified there and at a partner place where the
equation forces vanishing. m = 2 additionally allows the non-alternating real anchor — the ES case.

**Proposition 4.3 (the partner must be wild; PROVED).** In the setting of Thm 4.1 with (A) and (U), if A_S ≠ 0
then some place w ∉ S with w | m has ⟨τ₁, τ₂⟩_w ≠ 0. Consequently: (i) (R182 repair D11: the template is defined
for number fields; this item needs its function-field version — integrality away from ∞, ∞ ∈ S with the monic
normalisation, (A), (P), (U) as before — under which it reduces to Cor 2.2(c) plus "every place is tame") over a
global function field of characteristic p ∤ m **no** order-m T1 of this template exists, for any twists (for
m = p the template is vacuous: μ_p = 1 in characteristic p) — the *odd-m analogue* of FUNCTIONFIELD_ES's absence
of an odd-square obstruction, and the reason DRINFELD_ES §3's T1 is only a degree-class one. (R182 repair D11: it
is **not** the reason for the m = 2 statement of FUNCTIONFIELD_ES: m = 2 is outside the template (Remark 4.1(4)).
For m = 2 the reason is on the anchor side: (−1, −1) is split over F_q(T) (Prop 2.3(i) works for every m), and for
q ≡ 3 (mod 4) the monic normalisation is not even isotropic for m = 2 (⟨T, T⟩_∞ = ⟨T, −1⟩_∞ ≠ 0), which yields
the degree-dependent sign of (J)4 / FUNCTIONFIELD_ES Prop 4.1, consistent with (J)18's "pinned degree".)
(ii) over number fields the partner lies above m. ES (m = 2): anchor ∞ (real), partner 2
(wild). TES (m = 3): anchor 2 (tame, congruence-normalised), partner λ (wild).
*Proof.* Hilbert reciprocity for the constant algebra: A_S = −Σ_{w∉S} ⟨τ₁, τ₂⟩_w. For finite w ∉ S, w ∤ m
(including w | n, as n is prime to c and m): τ₁, τ₂ are w-units by (U), and the tame symbol of two units is
trivial. Archimedean w: Br ℂ = 0, and real places do not occur (μ_m ⊂ K, m ≥ 3 forces K totally complex; for
m = 2 they may occur — the ES anchor). So the non-zero term is at some w | m. In a function field with p ∤ m
every place is tame. ∎
*Caveat (scope).* Prop 4.3 concerns the template (normalisation-only anchors + integral points with unit twists
outside S). A T1 produced by a different mechanism (e.g. forced non-zero invariants at a place by the equation
itself, as in ES at 2 for m = 2) is not excluded by it. In function fields ∞ must lie in S (denominators are
not ∞-integral); (A) at ∞ for the monic normalisation holds iff sgn τ_i ∈ F_q^{*m}, and then A_S = 0 by the same
reciprocity; otherwise inv_∞ is the degree character of Prop 1.2 — exactly the non-template contribution.

## 5. Census of TES at primes (EVIDENCE) and the quadratic part

**Census** (`scripts/tw_eis_census.py 60 6000`, log `logs/tw_census_60_6000.txt`): all 2-primary split primes π
with 101 < N(π) ≤ 6000 (746 primes; R182 repair D12: the script includes **no** inert primes, its inert branch
is empty; R182 ran the 10 inert p ∈ [5, 71] separately: all solved, 117 I + 47 II, all (1, 2, 0)): 5849 Type I + 1968 Type II solutions in the window
N(X − c_i n/9) ≤ 60, **every one with invariants (inv₂, inv_π, inv_λ) = (1, 2, 0)** (R182 reproduced this and the 18 failures exactly,
inv_λ checked directly; Thm 3.2(c), and the partner
vanishing, on 7817 points). 18 primes (9 conjugate pairs, N(π) ∈ {103, 151, 193, 211, 367, 409, 769, 2029, 2239})
have no solution in the window; for N = 103, 151 none also with N(X − c_i n/9) ≤ 600 and with all X of
N(X) ≤ 20000 (`run(..., wide=20000)`). The "wide" search adds **no** solution even for primes with many (N = 307,
439): solutions live in the ES-like regime E = 9X − c_i n small, although TES has no size condition.
`scripts/tw_eis_classify.py 60 3000`: the window failures occur only for π with χ_π(ω) ≠ 0 and χ_π(2) ≠ 0 (cubic
characters), but most such π are solved (13–14 per class); no clean congruence obstruction. **Open:** is TES(π)
solvable for all primes π ≡ 1 (mod 2), π ∤ 6? (EVIDENCE leans "not proven either way"; the analogue of ES.)
**Quadratic part** (`scripts/tw_eis_quad.py 30`): μ(K) = μ₆, so BL's Br Ũ/Br K also has the quaternion class
α_{−1}. On TES solutions at 7 primes its invariant at π takes both values 0 and ½ (e.g. N = 439: 27/27), inv_λ = 0,
inv₂ = inv_π: no quadratic anchor (as Cor 2.2(e) predicts: U^{(1)} at (2) is not 2-divisible, normalisation does
not pin the 2-part). So the window failures are not explained by the algebraic Brauer group (Assessment: BL's
generator set; the integral model's further classes were not examined).
