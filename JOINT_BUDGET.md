# JOINT_BUDGET — joint-factorisation families for every prime: the algebraic budget at general p (task O254)

Status: in progress (O254, hatch H-A, direction 3). **ES is not solved here, nor any new infinite case of it.**
Labels as in DISCOVERIES.md. Scripts `scripts/z26_*`, memos `BRAINSTORM/z26_*.md`.
Builds on: the slice table (reviews/redteam-automorphic-2 Lemma 2.1, "RT2"), CAP_DOWN Lemma 1.1 (window form),
MENU_STERILITY / EXP_105 / EXP_OPEN (thin families, Theorem W), NORMFORM_CUBIC (J)79, POINTWISE_SIZE Thm C/M,
STERILE_EXPLICIT/STERILE_LOWER (J)54/(J)70, CAP_BOUNDED (J)83, LATTICE_MEETING (J)82, z22_uniform_certificates.

## 0. Iteration log (construction first; each line = version → barrier hypothesis it met → modification)

(V1) *Window with an algebraically factored x for general p.* Take x = K := 3(4X⁴+1) with X free near (p/48)^{1/4},
window m = 4K − p. The SG factors F± = 2X² ± 2X + 1 have residues mod m that are NOT functions of p mod a fixed
modulus (m moves with X). Firing needs m | U + V for a pair from {3, F₊, F₋, …}; each such event is p = 4K − (U+V)/j,
i.e. p is a value of a polynomial in X: a thin set. Met: the identity is polynomial in (X, p) with p *free*. → §1
proves that with p free there is never an algebraic splitting of a side (Theorem A). Modification: tie p to the
auxiliary (V2) or use non-polynomial auxiliaries (V3–V6).
(V2) *Tie p to the auxiliary: p = φ(u).* r = 1 ⇒ thin (the SG/cyclotomic families); r ≥ 2 with irreducible top form ⇒
(J)79 collapse; split top form ⇒ the representation p = φ(u) is itself a divisor-type equation. → §2.
(V3) *Congruence-forced budget:* force a large known factor F | K by a congruence on the window (m ≡ −p mod 4F). →
§3 Lemma 3.1: every certificate supported on the forced part is an ET class; the window is ≤ F+1 and is pinned by
p mod 4F (B1). The structure-free (Kneser) threshold needs Σ 2v_s(K) ≳ |⟨S⟩| while forcing costs m ≥ F:
an exponential budget gap (§3.3).
(V4) *Reciprocity-forced choice (least non-residue window, (J)64).* T1-safe and unbounded, so Theorem C does not apply;
but the forced information is a coset of the squares only; the class −1 needs the unforced box. → §4.
(V5) *Archimedean auxiliaries (u = ⌊√p⌋, CF convergents of √p, Pell units, "square-K" windows p + m = c·w²).* →
§4.2 anti-forcing: every such window has (m/p) = (c/p); with c = 1 (squares, CF norms, Pell) the window is a residue
window, i.e. unforced in the (J)64 sense.
(V6) *Divisibility auxiliaries (ord_p(2), Lucas rank of apparition, roots mod p).* → §4.3 direction mismatch: they make
p divide an auxiliary integer; the only transfer to the moduli of ES sides is reciprocity (V4) or the congruence
p ≡ 1 (mod ord) (V3).

## 1. Theorem A: with p free, no ES side ever splits algebraically

Setting. u = (u₁,…,u_r) is an auxiliary vector *independent of p*; a polynomial slice choice is θ(u) ∈ ℚ[u]² for one of
the D-rows of RT2 Lemma 2.1, with the slice parameters positive on a non-empty open set U ⊂ ℝ^r. Write X for p. The side
numbers of RT2 are N_θ(X) ∈ {X² + 4c²d, aX + c, (eX+1)/(4a), (eX+1)/(4d), 4c²dX + 1, cX + a, X + 4a²d, (X+e)/(4a),
(X+e)/(4d)} (Type I rows first, then Type II).

**Theorem A (side irreducibility; PROVED, elementary).** For every polynomial slice choice θ(u), the side number
factors in ℚ[u, X] as N_θ = g(u)·N′(u, X) with g ∈ ℚ[u] independent of X and N′ irreducible in ℚ[u, X]
(N′ of X-degree equal to that of N_θ).
*Proof.* Linear rows: N = αX + β with α, β ∈ ℚ[u], α ≠ 0. Put g = gcd(α, β) in the UFD ℚ[u]; then N′ = (α/g)X + β/g is
primitive of degree 1 in X over ℚ[u], hence irreducible in ℚ[u][X] (Gauss). Quadratic row: N = X² + 4c²d is monic in X;
it is reducible in ℚ(u)[X] iff −4c²d is a square in ℚ(u), iff −d ∈ ℚ(u)² (c ≠ 0). A square of ℚ(u) is ≥ 0 at every
real point where it is defined, while −d < 0 on U: contradiction. Monic and irreducible over ℚ(u) ⇒ irreducible in
ℚ[u][X] (Gauss); g = 1. ∎

**Corollary A.1 (forced certificates at free p are re-indexed ET classes; PROVED).** Call a certificate on the row θ
*algebraically forced* if its divisor f (RT2 notation) is a polynomial f ∈ ℚ[u, X] with f | N_θ in ℚ[u, X]. Then f is,
up to a constant, g₁(u) or g₁(u)·N′ with g₁ | g. For each fixed u the class condition f mod q_θ(u) ∈ R_θ(p) is then a
condition on p modulo a modulus M(u) depending only on u, i.e. the family is a u-indexed union of ET congruence classes
{p mod M(u) ∈ R(u)}.
*Proof.* Divisors of g·N′ in ℚ[u, X] are products of divisors of g with 1 or N′ (N′ irreducible, Theorem A). f = g₁:
p-free, so "f mod q_θ(u) ∈ R_θ(p)" depends on p only through p mod q_θ(u) (RT2: R_θ(p) depends on p mod q_θ). f = g₁N′:
N′(u, p) mod q_θ(u)·den is a function of p mod q_θ(u)·den. ∎

**Reading.** If p is a free variable, an auxiliary parameter space — however large, however the slice parameters are
chosen as polynomials in it — adds no algebraic factorisation to any side. The algebraic budget is exactly: p-free
numbers g(u) (whose divisors are as unforced as θ itself) plus the irreducible cofactor as a single block. Firing at p is
then "p mod M(u) ∈ R(u) for some u": the moving-modulus event of B2, with no joint factorisation left to exploit. Hence
**every joint factorisation of the thin-family kind must come from an algebraic relation between p and the auxiliary**
(§2) **or from non-polynomial data** (§4). (Theorem A is also why the (J)74/(J)75/(J)80 identities need n = c₀Y^D + k.)

## 2. Tying p to the auxiliary: p = φ(u)

By Theorem A a joint factorisation needs a relation between p and u. The polynomial case is p = φ(u), φ ∈ ℤ[u₁,…,u_r],
with a polynomial ET family (A, B, C, D) ∈ ℚ[u]⁴ for n = φ(u). (This is exactly the thin-family mechanism: r = 1,
φ = c₀Y^D + k, Y = 2^{s/D}.)

**Proposition 2.1 (trichotomy for polynomial relations; PROVED, with (c) only a reduction).**
(a) *r = 1, deg φ = D ≥ 2:* the family reaches ≪ X^{1/D} integers n ≤ X, so a set of primes of density 0 (the SG,
cyclotomic and moving-gap families of (J)74/(J)75/(J)80 are of this kind, even thinner: Y runs over powers of 2). r = 1,
D = 1 is a congruence class and is Theorem A with u in place of p.
(b) *φ* (top-degree part) irreducible over ℚ:* every such family valid at one point (Type II) or at one point (Type I, (J)79
Thm 3.1, since gr ℚ[u]/(φ) = ℚ[u]/(φ*) is a domain) lies in ℚ[φ], i.e. is an ET identity in n; it covers only non-square
classes and misses infinitely many primes of every square class (Mordell–Schinzel), unconditionally.
(c) *φ of degree 1 in some variable, φ = α(u′)·u_r + ψ(u′), u′ = (u₁,…,u_{r−1}), α ∉ ℚ:* the family fires at p iff for
some u′ in its validity region α(u′) | p − ψ(u′) (with the family's remaining congruences on u′, p). This is a
moving-modulus divisibility, i.e. the B2 event for the integers p − ψ(u′), and the side factorisations it produces are
those of the ET identity in the variable u_r = (p − ψ(u′))/α(u′).
*Proof.* (a) |φ(u)| ≤ X forces |u| ≪ X^{1/D}. (b) is (J)79 Thms 1.1′/3.1 with P = φ (prime with irreducible top part).
(c) Solving for u_r: n = p is reached at (u′, u_r) iff u_r = (p − ψ(u′))/α(u′) ∈ ℤ. If α is a non-zero constant, (p
− ψ(u′))/α is a free variable up to a congruence and Theorem A applies with u′ auxiliary: no splitting beyond re-indexed
ET classes. ∎
*Example (the ET variety itself).* φ = 4ab·d − a − b (c = 1), u_r = d: α = 4ab, ψ = −(a + b); the side p + 4a²d =
(a + b)(4ad − 1) splits identically, because θ = (a, d) uses the solved variable d. Firing: 4ab | p + a + b, the classical
moving-modulus event. So in case (c) the joint factorisation exists, but only *after* the divisor event has happened.
(d) *Residual (no claim):* φ* reducible and φ of degree ≥ 2 in every variable (e.g. φ = u₁²u₂² + lower, or norm-like
products with non-linear cross terms). For r = 2 the fibres φ = p are affine curves; nothing here proves or refutes a
family of this kind. The near-square case p = u² + k is not in (d): it is linear in k, so case (c)/(Theorem A) — and its
polynomial families have square-class sterile sets ((J)55).

## 3. Congruence-forced budget and the Kneser threshold (V3)

Notation (window form; RT2 row II{a,e} / CAP_DOWN Lemma 1.1 at cap 0). For p ≡ 1 (4) and a window m ≡ 3 (4) with
gcd(m, p) = 1 put K = K_m = (p + m)/4. Then **Type II at window m ⟺ ∃ a, b ≥ 1 coprime, ab | K, m | a + b**
⟺ −1 ∈ Σ_m(K) := {∏ s^{e_s} mod m : |e_s| ≤ v_s(K)} (when gcd(K, m) = 1; positive exponents form a, negative b).
The ET identity class of a certificate (a, b, c = (a+b)/m) is p ≡ −m (mod 4ab), with d = (p + m)/(4ab).

**Lemma 3.1 (forced support pins the window; PROVED).** Let F | K be a factor forced by a congruence on the window
(m ≡ −p mod 4F). If a certificate has ab | F, then m ≤ a + b ≤ F + 1 < 4F, so m is the least positive residue of −p
mod 4F and the certificate is the single ET class p ≡ −m (mod 4ab), 4ab | 4F.
*Proof.* m | a + b > 0 and a + b ≤ ab + 1 ≤ F + 1. ∎
So a congruence-forced budget buys nothing beyond choosing one ET class: the window's freedom is used up by the forcing.
(The classification of all "self-generated" certificates — those using only K, 2^{v₂K}, p — is z22 Prop 2.1; Lemma 3.1
is the general-F version of its mechanism.)

**Proposition 3.2 (Kneser threshold; PROVED).** Let m be prime, S the set of primes of K (all prime to m), and
H₀ = ⟨S⟩ ≤ (ℤ/m)^×. If for every proper subgroup H < H₀
  Σ_{s ∈ S, s ∉ H} 2v_s(K) ≥ [H₀ : H] − 1,                                                      (3.1)
then Σ_m(K) = H₀. In particular, if (K/m) = −1 (a Jacobi-forced window, (J)64: then −1 ∈ H₀), (3.1) implies Type II at m.
*Proof.* Write (ℤ/m)^× additively (cyclic). Σ = Σ_s A_s with A_s = {−b_sℓ_s, …, b_sℓ_s} (ℓ_s = log s, b_s = v_s(K)),
0 ∈ Σ ⊆ H₀. Let H = Stab(Σ); suppose Σ ≠ H₀, so H ≠ H₀ (Σ is a union of H-cosets containing H). In G/H the image Σ̄ has
trivial stabiliser, and Kneser's theorem gives |Σ̄| ≥ Σ_s |Ā_s| − (#S − 1). If ℓ_s ∉ H and 2b_s + 1 ≥ ord(ℓ̄_s), then Ā_s is
the subgroup ⟨ℓ̄_s⟩ ≠ 0 and Σ̄ = Σ̄ + Ā_s would have non-trivial stabiliser; so for ℓ_s ∉ H, Ā_s is an injective progression
and |Ā_s| = 2b_s + 1, while |Ā_s| = 1 for ℓ_s ∈ H. Hence |Σ̄| ≥ 1 + Σ_{s ∉ H} 2b_s ≥ [H₀ : H] by (3.1); but Σ̄ ⊊ H₀/H
(Σ ≠ H₀ is a union of H-cosets inside H₀), so |Σ̄| ≤ [H₀ : H] − 1: contradiction. ∎
**Corollary 3.3 (the exponential budget gap; PROVED).** (3.1) for H = {1} needs Σ_s 2v_s(K) ≥ |H₀| − 1. At a
Jacobi-forced prime window |H₀| is even and ≥ 2·(order of a non-residue's odd part)…; in the worst case H₀ = (ℤ/m)^×
and (3.1) needs Ω(K) ≥ (m − 2)/2, whereas Ω(K) ≤ log₂ K. Forcing Ω(K) ≥ E by a congruence on the window (F | K with
Ω(F) = E) costs m ≥ F ≥ 2^E (Lemma 3.1 ranges) — so the structure-free route needs E ≥ (m−2)/2 ≥ (2^E − 2)/2: only
E ≤ 2, i.e. windows m ≤ 7, i.e. Mordell's classes. A structure-free certificate at a larger window needs an
*unforced* smooth K (a lottery: Erdős–Kac tails), or a small subgroup H₀ (s of small order mod m, which is the z22 /
CAP_DOWN Prop 1.3 shape m | s^j ± 1, pinned by Lemma 3.1).
