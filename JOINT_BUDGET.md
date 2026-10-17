# JOINT_BUDGET — joint-factorisation families for every prime: the algebraic budget at general p (task O254)

Status: checkpoint 1 (O254, hatch H-A, direction 3); report reviews/agent-reports/AGENT_REPORT_O254.md. **ES is not solved here, nor any new infinite case of it.**
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

**Remark 1.2 (positivity is what blocks the quadratic side; PROVED).** The only place Theorem A uses more than Gauss's
lemma is d > 0. If signed slices were allowed (d = −w², the signed relaxation), X² + 4c²d = (X − 2cw)(X + 2cw) splits
identically in p — the archimedean sign is exactly the obstruction to an algebraic budget on the Type I side, matching
(J)52's "positivity is T1's anchor".

**Corollary A.1 (forced certificates at free p are re-indexed ET classes; PROVED).** Call a certificate on the row θ
*algebraically forced* if its divisor f (RT2 notation) is a polynomial f ∈ ℚ[u, X] with f | N_θ in ℚ[u, X]. Then f is,
up to a constant, g₁(u) or g₁(u)·N′ with g₁ | g. For each fixed u the class condition f mod q_θ(u) ∈ R_θ(p) is then a
condition on p modulo a modulus M(u) depending only on u, i.e. the family is a u-indexed union of ET congruence classes
{p mod M(u) ∈ R(u)}.
*Proof.* Divisors of g·N′ in ℚ[u, X] are products of divisors of g with 1 or N′ (N′ irreducible, Theorem A). f = g₁:
p-free, so "f mod q_θ(u) ∈ R_θ(p)" depends on p only through p mod q_θ(u) (RT2: R_θ(p) depends on p mod q_θ). f = g₁N′:
N′(u, p) mod q_θ(u)·den is a function of p mod q_θ(u)·den. ∎

**Remark 1.3 (coordinates that depend on p as well; PROVED).** If all four ET coordinates are polynomials Θ(u, X)
(not only the slice θ), then for each fixed u the family is a polynomial ET family in n = X alone, i.e. an ET identity in n,
integral and positive exactly on a union of congruence classes mod some M(u) (for X large). So the conclusion of Cor A.1 holds for every
family polynomial in (u, p) with p free. Theorem A says where the splittings of such identities come from: only from
slice coordinates that depend on p (e.g. d = (p + e)/(4ab) makes 4c²dp + 1 = (4acd − 1)(4bcd − 1)), i.e. from the
classical identities themselves.

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
**Corollary 3.3 (the budget gap; PROVED part + Assessment).** (PROVED) (3.1) at H = {1} needs Σ_s 2v_s(K) ≥ |H₀| − 1;
if H₀ = (ℤ/m)^× this is 2Ω(K) ≥ m − 2, impossible once m > 2 log₂ K + 2. So structure-free certificates exist only at
windows m = O(log p), or when every prime of K has small order mod m (|H₀| small: the z22 / CAP_DOWN Prop 1.3 shape
m | s^j ± 1, which Lemma 3.1 pins to a congruence class).
(Assessment) Forcing Ω(K) ≥ E by a congruence on the window (F | K, Ω(F) = E, F ≥ 2^E) puts m in the class −p mod 4F,
whose least element is ≥ F for a proportion ≥ 3/4 of residues p mod 4F; there 2Ω(K) ≥ m − 2 would need the unforced
cofactor to supply ≥ (2^E − 2)/2 − E prime factors. The forced budget grows like log m, the structure-free need like m:
an exponential gap. Algebraic factorisation (thin families) closes it only because m stays fixed (11, 19, …) while the
factor residues are functions of the family parameter mod m.

## 4. Non-polynomial auxiliaries (V4–V6)

**4.1 Reciprocity forcing gives a coset, never a class.** At a prime window m with (m/p) = −1, (J)64 forces
(K/m) = −1, hence −1 ∈ H₀ = ⟨primes of K⟩. This is the only forcing known that is T1-safe and needs an unbounded
search (so POINTWISE_SIZE Thm C does not apply). But it fixes only the image of S in H₀/H₀²: K = s prime with
s ≢ −1 (mod m) a non-residue gives Σ_m(K) = {1, s^{±1}} ∌ −1, for every prime m ≥ 7, m ≡ 3 (4). Whether such K occur
for every bounded set of windows is (J)83 Thm 1.3 (CONDITIONAL on Dickson: yes). Higher reciprocity (cubic, quartic
residue symbols) would fix the image in H₀/H₀^ℓ; by Prop 3.2 a class needs the full box, so any finite set of
power-residue symbols leaves the same gap (Assessment).

**Proposition 4.2 (archimedean / ℚ(√p) auxiliaries give only unforced windows; PROVED).** Let p ≡ 1 (4) be prime and
m odd, positive, prime to p, with p + m = c·w² (c, w ≥ 1, gcd(w, m) = 1). Then the window m is Jacobi-forced
((K/m) = −1) iff (c/m) = −1 iff (c/p) = −1. In particular every window built from a near-square (m = w² − p), a
continued-fraction norm of √p (m = |P_k² − pQ_k²|, gcd(Q_k, m) = 1) or any m | A² − pB² with gcd(B, m) = 1 has
(p/m) = +1 and is unforced.
*Proof.* 4K = p + m ≡ p (mod m) and p ≡ cw² (mod m), so (K/m) = (p/m) = (c/m). Reciprocity (p ≡ 1 (4), m odd positive):
(p/m) = (m/p), and m ≡ cw² (mod p) gives (m/p) = (c/p). For m | A² − pB²: p ≡ (A/B)² (mod m). ∎
*Reading.* Forced windows are exactly the m with (p/m) = −1, i.e. an odd number of primes inert in ℚ(√p) divide m to
an odd power; every object built from the
arithmetic/archimedean geometry of ℤ[√p] (CF of √p, Pell units, small norms, "next square" windows) produces only
split/ramified windows. This is the structural reason why near-square primes (many small norms) are hard ((J)53/(J)55)
and why CF/Pell auxiliaries cannot supply the forcing (candidate (i), CF/Pell part, closed).

**Proposition 4.3 (Fermat-type auxiliaries are anti-forcing; PROVED).** Let p be an odd prime and (a, b, c, d, e) a
Type I or Type II point (RT2 §2.0). Then the ET class modulus 4ab does not divide p − 1; if p ≡ 1 (4) it does not divide
p + 1 either.
*Proof.* Type II: 4abd = p + e, so p ≡ −e (mod 4ab); Type I: 4abd = pe + 1, so pe ≡ −1 (mod 4ab). If 4ab | p − 1 then in
both cases e ≡ −1 (mod 4ab), so 4ab ≤ e + 1 ≤ a + b + 1 (e = (a+b)/c), impossible for a, b ≥ 1. If 4 | 4ab | p + 1 then
p ≡ 3 (4). ∎
*Reading.* Modulo any divisor k of p − 1, p looks like n = 1, and 4/1 is not a sum of three unit fractions (notes
Prop 77.3). Auxiliaries that hand over a divisor of p − 1 — ord_p(g), the Lucas rank of apparition when (D/p) = 1,
Pocklington/primality-certificate data, factors of p − 1 — pin p to the sterile point locally; they can enter a
certificate only through moduli not dividing p − 1. Divisors of p^k − 1 with k ≥ 2 (the cyclotomic menu C_k:
4ab | p^k − 1, i.e. ord_{4ab}(p) ≤ k) are allowed, but a bounded menu C_{≤k₀} is a bounded witness-producing program
(FACTOR p^j − 1, j ≤ k₀; test divisors), so by POINTWISE_SIZE Thm C it fails for infinitely many p ≡ 1 (24),
CONDITIONAL on H. Numerics in §6.

**Remark 4.4 (p is a non-square modulo every Type II class modulus; PROVED).** For p ≡ 1 (4) and every Type II point, p is not a square
mod 4ab; hence ord_{4ab}(p) is even (Prop 4.3 is the case k = 1). *Proof.* Lemma CT (POINTWISE_SIZE §2; in the coordinates
(abd, acdp, bcdp) after removing g = gcd(a, b), which changes ab by g²) gives (ab/p) = −1. If p ≡ t² (mod 4ab), then
(p/ℓ) = 1 for every odd ℓ | ab, and if 2 | ab then 8 | 4ab and p ≡ 1 (8), (2/p) = 1; with p ≡ 1 (4) Jacobi reciprocity gives
(ab/p) = (2/p)^{v₂(ab)}(p/odd(ab)) = 1: contradiction. ∎ So the cyclotomic depth k*(p) is always even, and a bounded
cyclotomic menu C_{≤k₀} is "4ab | p^k − 1 for some even k ≤ k₀" plus the class condition: a divisor event on the fixed
polynomials p^k − 1.

## 5. The obstruction theorem (exact scope)

**Definition 5.1.** A *joint-factorisation (JF) family* on a set of primes P assigns to p ∈ P an auxiliary vector
u = u(p) ∈ ℤ^r and a Type I/II point whose ET coordinates are Θ(u, p) for a fixed Θ ∈ ℚ[u, X]⁴ satisfying the ET identity
on the relation locus. Its *auxiliary relation* is one of:
(R0) none — u ranges over a congruence/positivity region and the rule only selects u;
(R1) polynomial: p = φ(u), φ ∈ ℤ[u];
(R2) reciprocity-guided: u contains a window or level m chosen by prescribed residue symbols (m/p)_ℓ;
(R3) archimedean / ℚ(√p): windows m with p + m = c·w² or m | A² − pB² (near squares, CF norms of √p, Pell data);
(R4) divisibility: u | p^k − 1 for some k ≤ k₀ (factors of p ± 1, ord_p(g), Lucas ranks of apparition) — with the
certificate's class modulus 4ab built from such u.

**Theorem 5.2 (JF trichotomy).** Every JF family is, according to its relation:
(a) *(R0), (R2)–(R4), and (R1) with a variable of degree 1 and constant coefficient (i.e. p free in Θ):* a u-indexed union
of ET congruence classes (Remark 1.3); no p-independent slice acquires an algebraic factor depending on p (Theorem A); the
relation only selects which classes are tried. Firing at p is the moving-modulus event
"p mod M(u) ∈ R(u) for some u". [PROVED]
(b) *(R1), φ* irreducible:* an ET identity in n, missing infinitely many primes of every square class. [PROVED; (J)79 +
Mordell–Schinzel]. *(R1), r = 1:* density 0. [PROVED] *(R1), φ linear in u_r with non-constant coefficient α(u′):*
firing ⟺ α(u′) | p − ψ(u′), an unforced divisor event (Prop 2.1(c)). [PROVED reduction]
(c) *(R2):* the forced information is the image of ⟨primes of K⟩ in H₀/H₀^ℓ (genus/character data); for ℓ = 2 it never
determines −1 ∈ Σ_m(K) (§4.1), and every bounded window set fails infinitely often [CONDITIONAL on Dickson, (J)83 Thm
1.3]; structure-free completion needs Ω(K) ≥ (|H₀| − 1)/2 (Prop 3.2, Cor 3.3). [PROVED + CONDITIONAL]
(d) *(R3):* every window is unforced, (p/m) = +1 when c = 1 (Prop 4.2). [PROVED]
(e) *(R4):* no class modulus divides p − 1 (or p + 1 when p ≡ 1 (4)) (Prop 4.3); p is a non-square mod every class
modulus (Remark 4.4); a bounded menu (k₀ fixed) is a bounded witness-producing program and fails for infinitely many
p ≡ 1 (24) [CONDITIONAL on H, POINTWISE_SIZE Thm C]. [PROVED + CONDITIONAL]
In the brief's words: every JF family of type (R0)–(R4) is polynomial in n ((b)), genus-detectable ((c), (d), and the
mod-(p^k − 1) sign of (e)), thin ((b)), or fires only through an unforced divisor event ((a), (b) last case, (e)).
**Not covered (the residual H-A core):** (R1) with φ* reducible and φ of degree ≥ 2 in every variable; (R4) with k₀
growing with p; (R2) windows chosen by an unbounded rule *together with* a structured K (the (J)64/(J)66 regime, where the
cap is proved but cap 0 is the lottery); and any auxiliary not of polynomial, character, archimedean-ℚ(√p) or
divisibility type (none is known that is canonically attached to every prime).

## 6. Numerics (all re-runnable; outputs in data/z26/)

* `scripts/z26_checks.py` (data/z26/checks.txt; 14 s): (a) Theorem A — sympy factor_list of all seven side shapes for 60
  random polynomial slice choices in (u₁, u₂): 0 violations. (b) Prop 3.2 — 3000 random (m, K), m prime < 80: (3.1) held
  in 374, Σ_m(K) = H₀ in all 374 (brute force). (c) Prop 4.2 — 368 689 windows (CF norms of √p and near-square windows
  w² − p, primes p ≡ 1 (4) < 2·10⁵, hypotheses as stated): all (p/m) = +1. (A first run flagged 5 windows with p | m,
  outside the hypotheses; the check now enforces gcd(m, p) = 1.) (d) Remark 4.4 — all 3188 Type II points of primes
  p ≡ 1 (4) < 3000: p is a non-square mod 4ab in every case.
* `scripts/z26_cyclo_depth.py 300000 hard` (data/z26/cyclo_depth_3e5_hard.txt; 130 s): all 765 Mordell-hard primes
  (p mod 840 ∈ {1, 121, 169, 289, 361, 529}) ≤ 3·10⁵, all 28 153 Type II points enumerated (window form), each checked
  exactly against 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp); Prop 4.3 violations 0; odd squares ≤ 3·10⁵ with a Type II point: 0
  (T1 control). Cyclotomic depth k*(p) = min ord_{4ab}(p): histogram {2: 268, 4: 86, 6: 87, 8: 21, 10: 119, 12: 99, 14: 4,
  16: 28, 18: 17, 20: 2, 22: 13, 24: 2, 28: 6, 30: 8, 40: 2, 42: 2, > 60: 1} — always even (Remark 4.4) and unbounded in
  range (p = 210 961 has k* > 60; 296 041 and 80 809 have 42). EVIDENCE that every bounded cyclotomic menu fails, as Thm C
  predicts under H; at N = 2·10⁴ the maximum was 22.

## 7. The budget, quantified

| setting | window | forced data on K | needed for cap 0 | outcome |
|---|---|---|---|---|
| 3·2^s + 1 ((J)74) | m = 11 fixed | K = 3F₊F₋, residues of F± functions of X mod 11 | −1 = product of ≤ 2 blocks | PROVED (thin) |
| 63·2^s + 1 ((J)80) | moving gap 3Φ₆-type | n + 4a²d = 63(Y+3)(Y²−3Y+9) | gap = cyclotomic factor | PROVED (thin) |
| general p, (R0)/(R1c) | any | p-free content only (Thm A) | −1 ∈ Σ_m(K) | unforced divisor event |
| general p, (R2) forced window | (m/p) = −1 | one bit: (K/m) = −1 ⇒ −1 ∈ H₀ | box: Σ 2v_s(K) ≳ #H₀ (Prop 3.2) | cap ≤ (m−3)/4 proved (CAP_DOWN 1.3), cap 0 lottery |
| general p, congruence-forced F | m ≡ −p (4F) | F with Ω(F) = E | m ≤ F + 1 ⇒ one ET class (Lemma 3.1) | B1 |
| general p, (R3) | near-square/CF | p + m = c w² | (c/p) = −1 | c = 1: never forced (Prop 4.2) |
| general p, (R4) | 4ab | p^k ≡ 1 | k even, unbounded (§6) | B2 under H |

The thin families succeed because the window is FIXED while the auxiliary (X, Y) moves: residues of algebraic factors
mod the fixed window are then functions of the auxiliary, and a covering in the auxiliary closes the family. For
general p the window must move (any fixed finite window set fails, conditionally), and Theorem A removes all algebraic
factors; what remains is one character bit (forcing) against a box that needs ≍ #H₀ exponent units.
