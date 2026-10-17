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
