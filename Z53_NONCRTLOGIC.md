# Z53_NONCRTLOGIC — which oracle primitives escape the formal-genericity barrier B1, and what escaping buys

ES is OPEN; nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Lane NONCRTLOGIC of wave z53
(`z52bbriefs/z53_depth.md`, `z53_lanes.md` §NONCRTLOGIC). Scripts `scripts/z53_noncrtlogic_*`, data `data/z53/noncrtlogic/`.

*Status: final draft (checkpoint 1 committed earlier); hostile review: see §10.*

## 0. Verdict (preliminary)

**Narrowed, with two barrier-strengthening theorems.** (A) Theorems M/C of `POINTWISE_SIZE.md` extend to programs that call
*arbitrary* finite-valued oracles (any function of p with values in a fixed finite set — Frobenius classes in fixed fields,
power-residue symbols, h(p) mod m, any predicate), with **no extra hypothesis beyond H for a finite polynomial family**. This
closes the "fixed non-abelian Frobenius information" item (E3) of `POINTWISE_SIZE.md` §4.2, which was open (a proposed
Schinzel–Chebotarev hypothesis H_K is not needed). (T) Theorem C (the formal odd-square principle) holds not only for linear
P but for **every** primitive irreducible P with P(0) = 1 and no positive real root, at explicit "trap points"; the proof is
Hilbert reciprocity in Q(β), β a root of the reversed polynomial. Consequences: any bounded use of the full continued-fraction /
Pell / unit data of √p (killed at p = q² + 1: long cycles elsewhere are irrelevant), of ⌊c·p^θ⌋ for rational c, θ, of
ord_p(a), of the factorisations of p ± 1, fails for infinitely many p ≡ 1 (24) (CONDITIONAL on H). At a trap point every
polynomial value is a quadratic residue mod p (unconditional), so the escape boundary is exactly **"produce a non-polynomial
integer carrying a quadratic non-residue"**; the cheapest such primitive with full factorisation control is the least
non-residue n_p, and procedures seeded by it reduce, value by value, to bounded procedures on the r-generic line (FRONTIER
§7.9). Numerically a non-residue seed doubles to triples forest-certificate rates, but only through parity; conditioned on
parity the tied-class divisor event is not more likely (§6, EVIDENCE). Taxonomy in §5, verdict in §7, proposed FRONTIER text in §8.

## 1. Precise statements attacked

Notation as in `POINTWISE_SIZE.md` §1: 𝒫 = primitive irreducible h ∈ ℤ[X] with positive leading coefficient; programs
(P1)–(P8), extended programs with primitives (F9); formal run at (P, q*), q* ∈ Ẑ; admissible q; Theorem M (transfer),
Theorem C (formal odd-square principle, linear P, square-mimicking q*), Lemma CT (every positive solution of 4/p,
p ≡ 1 (4), has a p-free denominator with a prime factor ℓ, (ℓ/p) = −1).

* **(S1) Oracle taxonomy.** For each candidate primitive g (the brief's list: ⌊p^θ⌋, least quadratic non-residue n_p,
  least primitive root, ord_ℓ(p), ord_p(2), CF/Pell data of √p, h(±p), regulator, Legendre/Jacobi symbols of p + u, prime
  factors of p ± 1), decide: **killed** — there is a polynomial family P and a point q* at which (i) g has formal
  (finite-menu) semantics on the admissible set and (ii) Theorem C's conclusion holds, so that every correct witness-producing
  program using g (plus bounded computation) fails i.o. under H; or **escapes** — for every such (P, q*), g has no such
  semantics. Prove sufficient criteria for both.
* **(S2) Second half of E1/E2.** For escaping primitives, what factorisation control do they give, and does it reach the
  tied-class event B2? Test the cheapest one (CERTIFIED where possible) at the test primes and controls.
* **(S3)** Is "long Pell cycle" itself an escape?

**Why not already closed.** POINTWISE_SIZE proves Theorem C only for linear P (Remark 2 there: "for deg P ≥ 2 … a FAIL output
must be certified another way"; `BRAINSTORM/gon_fermat_certificates.md`: "the extension to quadratic P is not proved"), leaves E3
open (§4.2: "Whether fixed non-abelian information escapes is therefore open here"; (J)96 = `MODP_RECIPROCITY.md` Prop 2.1
covers only fixed finite witness *sets*, not adaptive factoring procedures; `BRAINSTORM/nonab_frobenius_redei.md` proves E3 only
CONDITIONAL on H_K), and lists ⌊p^θ⌋, n_p, orders as E2 without a criterion. `Z52D_PELLCYCLE.md` kills only the root menu
R3 ∪ U in the forest ("Arbitrary functions of the cycle data … are not covered"). Nothing in FRONTIER §6 or the closed list
treats oracle programs or nonlinear trap families.

## 2. Theorem A — finite-information oracles do not escape (PROVED; existence CONDITIONAL on H)

**Definition.** A *finite-information oracle* is an instruction `b ← O(r₁, …, r_k)` where O: ℤ^k → 𝒜 is an **arbitrary**
function (not necessarily computable) into a finite set 𝒜 ⊂ ℤ fixed with the program; b is then an ordinary register.
The **formal tree** of a program Π at (P, q*) is the formal run of `POINTWISE_SIZE` §1.2 in which every oracle instruction
branches into |𝒜| children, child a continuing with b = a. It is *defined* if every branch is defined, *finite* if it is a
finite tree (equivalently, by König's lemma, every branch halts). S, Λ, the exponents E_ℓ and the thresholds of the tree are
the unions / maxima over all its nodes (finitely many).

**Theorem A.** Let Π be an extended program with finite-information oracles whose formal tree at (P, q*), C_P = 1, is defined
and finite.
(a) There is q₀ such that for every admissible q (for the union data S, Λ, E), p = P(q) is prime and the actual run of Π on p
equals the formal run along the branch selected by the actual oracle answers, evaluated at q; in particular the output is
the formal output of that branch at q.
(b)–(d) The existence statements of Theorem M(b)–(d) hold verbatim for the union family S.
(e) If moreover Π is correct and witness-producing, and either P is linear and q* square-mimicking and universally
nondegenerate (Theorem C's setting) or (P, q*) is a trap point (Theorem T below), then there are explicit finite S′ ⊇ S,
Λ′ ⊇ Λ such that **every (S′, Λ′)-admissible q has Π(P(q)) = FAIL**; under H for S′ there are infinitely many such q.

*Proof.* (a) Induction along the actual run, with invariant "the actual registers equal the formal registers of the current
tree node, evaluated at q". All non-oracle steps are Theorem M(a)'s steps verbatim (the thresholds are finitely many: one per
node of the finite tree). At an oracle step the actual arguments are the formal arguments evaluated at q, so the actual
answer is some a ∈ 𝒜; the actual run moves to child a, whose register b = a agrees. Lists and loops: same lists, same
iterations. The run reaches a leaf after finitely many steps because the tree is finite. (b)–(d): admissibility for the union
data is an H-type condition on one finite family; Theorem M(b)–(d)'s proofs use only the family and the point.
(e) Apply the proof of Theorem C (or of Theorem T) to Π′ = Π followed by FACTOR of the output denominators, with S′, Λ′ the
union over all leaves of the enlargements made there. At an admissible q the actual output is the formal output of *some*
leaf, evaluated at q; its p-free denominators factor into primes of Λ′ and formal primes r_h(q), h ≠ P, all of which are
quadratic residues mod p (Theorem C's computation for linear P; Lemma T4 below at trap points). If the output were SUCCESS,
correctness would make it a positive solution, contradicting Lemma CT(a). ∎

*Remarks.* (1) No hypothesis on how the answers are distributed is used: the answers need not be equidistributed or even
consistent; each branch is killed on the common admissible set. In particular no Schinzel–Chebotarev hypothesis H_K is
needed. (2) The answer set must be finite *per call*; the number of calls must be bounded along every formal branch (this is
what "finite tree" means).

**Corollary A1 (E3 closed at the witness-procedure level).** Fixed non-abelian Frobenius data — FROB_K(p) or FROB_K(r) for any
formal prime r and any fixed finite Galois K/ℚ, m-th power-residue symbols (a/p)_m of formal a, Artin symbols, "is 2 a cube mod
p", "p = x² + 27y²?", the class of p in any fixed ray class group — and every other bounded-output datum (h(±p) mod m,
⌊p^θ⌋ mod m, signs/comparisons of non-formal quantities against formal ones, Legendre/Jacobi symbols (u/p) and (p + u / m) of
formal u, m) are finite-information oracles. Every correct witness-producing program whose formal tree at q*_univ (P = 24X + 1)
is finite fails for infinitely many p ≡ 1 (24), CONDITIONAL on H for one finite family (PROVED implication). This answers
POINTWISE_SIZE §4.2 (E3) negatively, without H_K.

**Corollary A2 (divisor-valued oracles).** Suppose an oracle value g(p) always divides a formal register value F (F ≠ 0
formally). At admissible q, g(p) is then one of the formal divisors of F (the list DIVISORS(F) of `POINTWISE_SIZE` (F5)), so
g = "the j-th formal divisor", j ≤ |DIVISORS(F)| — a finite-information oracle. Hence killed (CONDITIONAL on H). Instances:
ord_p(a) and the index (p − 1)/ord_p(a) for every fixed (or formal) a — at p = 24q + 1 with q prime, ord_p(2) ∈ {q, 2q, 3q,
4q, 6q, 12q} and *which* one is a non-abelian Frobenius datum, irrelevant by Theorem A; ord_m(a) for formal m (it divides
φ(m), formal once m is FACTORed: φ(K∏r_h^e) = φ(K)∏r_h^{e−1}(r_h − 1) with r_h − 1 = (h − C_h)/C_h polynomial);
gcd(p − 1, ·), the multiplicative structure of F_p^× (cyclic of order p − 1, formal). ord_ℓ(p) for fixed ℓ is a congruence.

**Corollary A3 (bounded advice).** For every bounded witness-producing program Π and every B, the program "Π with B bits of
arbitrary advice depending on p" fails i.o. (CONDITIONAL on H): advice is a finite-information oracle with |𝒜| = 2^B.
(Upper side, Assessment: if X_win(C) of POINTWISE_SIZE §8 holds, log₂(C log p) bits of advice — the index of a successful
window — suffice for a bounded per-window program, so the "advice complexity" of ES witnesses is between ω(1) and
O(log log p) conjecturally.)

## 3. Theorem T — trap families: Theorem C for nonlinear P (PROVED; existence CONDITIONAL on H)

**Setting.** P ∈ 𝒫 of degree n ≥ 1 with **P(0) = 1** and **no positive real root**. Let R(X) := XⁿP(1/X) ∈ ℤ[X] (monic,
since R's leading coefficient is P(0) = 1; irreducible, as the reversal of an irreducible polynomial with nonzero constant
term; R(0) = lc(P) =: a). Let β be a root of R, K = ℚ(β), O_K its ring of integers (β ∈ O_K). For q ∈ ℤ put π_q := 1 − qβ.
Then N_{K/ℚ}(π_q) = ∏_j (1 − qβ_j) = qⁿR(1/q) = P(q) (for q ≠ 0; trivially for q = 0). For h ∈ ℤ[X] of degree d let
h^∨(X) := X^d h(1/X) ∈ ℤ[X]. For x ∈ K^× let T(x) be the set of real places of K together with the finite places v | 2x.

*Linear sanity check.* P = 24X + 1: R = X + 24, β = −24, K = ℚ, π_q = 1 + 24q = p. Everything below then reduces to
Theorem C.

**Lemma T1 (the prime 𝔭_q).** If p = P(q) is prime, then 𝔭 := π_qO_K is a prime ideal of norm p, O_K/𝔭 ≅ F_p, and qβ ≡ 1
(mod 𝔭). For h ∈ ℤ[X] of degree d with p ∤ h(q): (h(q)/p) = [β/𝔭]^d · [h^∨(β)/𝔭], where [x/𝔭] ≡ x^{(p−1)/2} (mod 𝔭) is
the quadratic residue symbol.
*Proof.* |N(π_q)| = p is prime, so π_qO_K is prime of residue degree 1. π_q = 1 − qβ ∈ 𝔭 gives qβ ≡ 1, so β is a unit mod
𝔭. Writing h = Σ c_k X^k, β^d h(q) = Σ c_k β^{d−k}(qβ)^k ≡ Σ c_k β^{d−k} = h^∨(β) (mod 𝔭). The Legendre symbol of h(q) mod p
equals the residue symbol of h(q) at 𝔭 (O_K/𝔭 = F_p), and [·/𝔭] is multiplicative with [β/𝔭]^{−d} = [β/𝔭]^d. ∎

**Lemma T2 (Hilbert reciprocity).** Let x ∈ O_K, x ∉ 𝔭, p odd, 𝔭 ∤ 2x. Then [x/𝔭] = ∏_{v∈T(x)} (x, π_q)_v (quadratic
Hilbert symbols of K).
*Proof.* Product formula ∏_v (x, π_q)_v = 1 over all places of K (Hilbert reciprocity; standard, e.g. Neukirch, *Algebraic
Number Theory*, Ch. VI Thm 8.1 — theorem number quoted from memory, not re-checked). Complex places contribute 1. A finite
v ∉ T(x), v ≠ 𝔭 is odd, and x, π_q are v-units there ((π_q) = 𝔭), so (x, π_q)_v = 1. At 𝔭, x is a unit and π_q a uniformiser,
so (x, π_q)_𝔭 = [x/𝔭] (tame symbol at an odd place). All symbols are ±1. ∎

**Definition (trap point).** q* ∈ Ẑ is a *trap point for P* if for every prime ℓ and every place v | ℓ of K,
1 − q*_ℓ β ∈ (K_v^×)². (Squares are open in K_v^×, so for each ℓ there is E with: q ≡ q*_ℓ (mod ℓ^E) ⇒ 1 − qβ ∈ (K_v^×)² for
all v | ℓ.) Then P(q*_ℓ) = N(1 − q*_ℓβ) is a unit square in ℤ_ℓ for every ℓ, so a trap point is square-mimicking for P; in
particular C_P = 1 and every admissible p is ≡ 1 (mod 8) and ≡ 1 (mod 3).

**Lemma T3 (real places).** If q > 0 then π_q is positive at every real place of K. *Proof.* A real embedding σ sends β to a
real root β_σ of R, and 1/β_σ is a real root of P, hence negative; so 1 − qβ_σ > 1. ∎

**Lemma T4 (QR-transparency at trap points; PROVED, unconditional).** Let q* be a trap point, x ∈ O_K∖{0}, and let Λ_x be the
set of rational primes below the finite places of T(x), with precisions E_ℓ as in the definition. Then for every integer
q > 0 with q ≡ q*_ℓ (mod ℓ^{E_ℓ}) (ℓ ∈ Λ_x), P(q) = p prime and p > 2|N(x)|: [x/𝔭_q] = 1. Consequently, for every h ∈ ℤ[X]
and every such q (Λ enlarged by Λ_β ∪ Λ_{h^∨(β)}) with p ∤ h(q): **(h(q)/p) = +1.**
*Proof.* By the choice of q, π_q ∈ (K_v^×)² at every finite v ∈ T(x); by Lemma T3 also at real v. So every symbol in Lemma
T2 is 1. The consequence is Lemma T1 with x = β and x = h^∨(β) (h^∨(β) ≠ 0 unless R | h^∨, i.e. h is a multiple of P; then
p | h(q)). ∎

*Reading.* At a trap point **every polynomial value is a quadratic residue** mod p — exactly what is true at an odd square
m² for every integer prime to m. Primality of the values is not needed for this; it is needed only to make a procedure's run
formal (Theorem M).

**Lemma T5 (existence of universally nondegenerate trap points; PROVED).** For every P as in the setting there is a trap
point q* that is nondegenerate for every h ∈ 𝒫, with q*_2 ∈ 8ℤ₂ and q*_3 ∈ 3ℤ₃.
*Proof.* (i) *Small or bad primes.* If ℓ | 2a·disc(R), or ℓ ≤ L₀ (any fixed bound ≥ 3), take q*_ℓ ∈ ℓ^{e_ℓ}ℤ_ℓ, e_2 = 3,
e_ℓ = 1 (ℓ odd). Then 1 − q*_ℓβ ∈ 1 + ℓO_v (ℓ odd: a square by Hensel, residue 1) resp. 1 + 8O_v (ℓ = 2: x² = 1 + 8z is
solved by x = 1 + 2y with y² + y = 2z, which has a root by Hensel since y ≡ 0 is a root mod 𝔪_v and 2y + 1 is a unit).
(ii) *Good primes* ℓ ∤ 2a·disc(R). Then ℓ ∤ [O_K : ℤ[β]], the places v | ℓ correspond to the irreducible factors R_i of
R mod ℓ (degrees f_i), and for c ∈ F_ℓ the residue of 1 − cβ at v is a nonzero square in F_{ℓ^{f_i}} iff its norm
P_i(c) := ∏_{R_i(ρ)=0}(1 − cρ) is a nonzero square in F_ℓ (x ∈ F_{ℓ^f}^× is a square iff x^{(ℓ^f−1)/2} = N(x)^{(ℓ−1)/2} = 1).
Moreover P ≡ ∏_i P_i (mod ℓ), the P_i are irreducible, pairwise non-associate, of degree f_i (ℓ ∤ a) with P_i(0) = 1. By
Hensel (ℓ odd), every q ∈ ℤ_ℓ with q mod ℓ ∈ G_ℓ := {c ∈ F_ℓ : P_i(c) ∈ (F_ℓ^×)² ∀ i} satisfies the trap condition at ℓ. By
Weil's bound for multiplicative character sums of squarefree non-constant polynomials (|Σ_c χ(g(c))| ≤ (deg g − 1)√ℓ;
standard), expanding ∏_i (1 + χ(P_i(c)))/2 gives |G_ℓ| ≥ ℓ/2^n − n√ℓ − n → ∞.
(iii) *Nondegeneracy.* Enumerate 𝒫 = (h_j)_{j≥1}. For good ℓ let k(ℓ) be the largest k with Σ_{j≤k} deg h_j < |G_ℓ|; pick
c_ℓ ∈ G_ℓ that is a root mod ℓ of none of h_1, …, h_{k(ℓ)} (each h_j is primitive, so nonzero mod ℓ). In every case pick
q*_ℓ in the chosen ball (ℓ^{e_ℓ}ℤ_ℓ or c_ℓ + ℓℤ_ℓ, both uncountable) outside the countable set of roots of all h_j. Then
h_j(q*_ℓ) ≠ 0 for all j, ℓ; and ℓ ∤ h_j(q*_ℓ) as soon as k(ℓ) ≥ j, i.e. for all but finitely many ℓ since |G_ℓ| → ∞. ∎

**Theorem T (formal odd-square principle at trap points).** Let P be as in the setting, q* a trap point for P nondegenerate for
every h ∈ 𝒫 (Lemma T5), and Π a correct witness-producing extended program (finite-information oracles allowed) whose formal
tree at (P, q*) is defined and finite. Then there are explicit finite S′ ⊇ S and Λ′ ⊇ Λ such that every (S′, Λ′)-admissible
q has **Π(P(q)) = FAIL** (PROVED). Under Hypothesis H for {f_h(y) = h(M′y + q̃)/C_h : h ∈ S′} there are infinitely many such q,
all with P(q) ≡ 1 (mod 24) (CONDITIONAL on H).
*Proof.* As Theorem C / Theorem A(e). Let Π′ append FACTOR of the output denominators; S′ its polynomial set; Λ′ = Λ ∪ {2, 3}
∪ Λ_β ∪ ⋃_{h∈S′∖{P}} Λ_{h^∨(β)} ∪ {primes of the constants K_A, C_h} ∪ ⋃_ℓ Λ_ℓ, with the E_ℓ of Lemma T4 (and the original E_ℓ,
whichever is larger). At an admissible q beyond all thresholds (in particular p > 2|N(x)| for the finitely many x used), the
actual output is the formal output of some leaf at q (Theorem A(a)). A p-free denominator has prime factors of two kinds:
primes ℓ of constants (ℓ ∈ Λ′; (ℓ/p) = +1 by Lemma T4 with h = ℓ constant) and formal primes r_h(q) = h(q)/C_h, h ≠ P
((r_h/p) = (h(q)/p)(C_h/p) = +1 by Lemma T4 twice). So every prime factor is a residue, contradicting Lemma CT(a) (p ≡ 1 (4)) if
the output were a SUCCESS; by correctness the output is FAIL. Existence: Theorem M(b) (whose proof needs only C_P = 1 and
nondegeneracy, not linearity). Admissible p ≡ P(q*) is a unit square at 2 and 3, hence ≡ 1 (8), ≡ 1 (3). ∎

**Examples of trap families** (all with P(0) = 1, no positive real root): 24X + 1 (Theorem C); **X² + 1** (β = ±i; the trap
condition at 2 is 8 | q, at 3 it is 3 | q, at 5 it is q ≡ 0, ±… — q ≡ 0 always works); kX² + 1 (k ≥ 1); 2X² + 1; X⁴ + 1;
cyclotomic Φ_N(dX) (N ≥ 2, d ≥ 1); LXᵇ + 1 when irreducible; 2X³ + 2X + 1. Non-examples: X² − 3X + 1 (positive real roots — the
real place breaks Lemma T4, see §4); X² + 4 (P(0) ≠ 1; indeed p = q² + 4 ≡ 5 (8) for odd q, and one of q ± 2 is always a
non-residue mod p since (q+2)(q−2) ≡ −8).

### 3.1 Corollaries

**Corollary T1 (Pell/CF data; answers S3).** Let p = q² + 1 with 24 | q (q ≥ 8). Then the complete reduction cycles of √p and
(1 + √p)/2 (all P_k, Q_k, a_k, the period lengths 1 and 3, all convergent numerators/denominators ≤ p + 2), the fundamental unit
ε_p = q + √p, ⌊√p⌋ = q, ⌊c√p⌋ for rational c, and the sign of {√p} − θ for rational θ are given by fixed polynomials in q on
the class (`Z52D_PELLCYCLE.md` Lemma 1.4; Lemma D). Hence every correct witness-producing program that uses these primitives
(plus bounded computation and finite-information oracles) and has finite formal tree at a trap point for X² + 1 fails for
infinitely many primes p = q² + 1 ≡ 1 (24) (CONDITIONAL on H). This covers **arbitrary program-computable functions of the
cycle data**, the gap left open by Z52D_PELLCYCLE (which killed the forest root menu R3 ∪ U). *Long cycles are not an escape:*
a correct ES procedure must also succeed at the short-cycle primes q² + 1, and there its cycle-data input is frozen. The same
holds for √(kp) for any single fixed k ≥ 1 on the trap family kX² + 1 (√(k(kq²+1)) = √((kq)² + k) is of Richaud–Degert type,
√(m² + r) = [m; 2m/r, 2m] with r | 2m).

**Corollary T2 (archimedean primitives).** (i) For rational c_j, θ_j > 0 (j ≤ k), let b = lcm of the denominators of the θ_j
and N a prime ≡ 1 (mod b). On P = Φ_N (trap family), c_jP(q)^{θ_j} = G_j(q) + c_{j,0} + ε_j(q) with G_j ∈ ℚ[X], c_{j,0} ∈ ℚ and
ε_j(q) → 0 of eventually constant sign (binomial series of (1 + q⁻¹ + … + q^{1−N})^{θ_j}), so each ⌊c_jp^{θ_j}⌋ has formal
semantics on a congruence class (Lemma D plus Prop A of POINTWISE_SIZE). Hence programs using any finite collection of
⌊c_jp^{θ_j}⌋ with rational c_j, θ_j are killed (CONDITIONAL on H). (ii) **Necessary condition (PROVED, elementary):** if
⌊c·p^θ⌋ (c, θ > 0 real) agrees with one of finitely many polynomials G_1, …, G_m ∈ ℚ[X] at infinitely many q with p = P(q)
(deg P = n, lc P = L), then nθ ∈ ℤ and c·L^θ ∈ ℚ. (Some G_i agrees infinitely often; c·P(q)^θ = cL^θq^{nθ}(1 + O(1/q)) is
within 1 of G_i(q), so deg G_i = nθ and lc G_i = cL^θ.) Consequently **⌊p^θ⌋ for irrational θ, ⌊log p⌋, and the pair
(⌊√p⌋, ⌊√(2p)⌋) have no formal semantics on any polynomial family** (the pair would need L and 2L to be squares). Individually,
⌊√(2p)⌋ is killed on 2X² + 1. So archimedean escape is cheap — but see §5.

**Corollary T3 (QNR-valued oracles escape every trap point; PROVED).** If an oracle O satisfies (O(p)/p) = −1 for all primes p
(e.g. n_p, the least primitive root g_p ≥ n_p, the least prime ℓ ≡ a (mod m) with (ℓ/p) = −1), then for every trap family
P, every polynomial G ∈ ℚ[X] and every trap point, O(P(q)) ≠ G(q) for all q in a refined trap class with P(q) prime and q
large: by Lemma T4 G(q) (cleared of denominators, whose primes are added to Λ) is a residue. So such O has no finite-menu
formal semantics at any trap point. Conversely (Lemma CT + Lemma T4) any program that succeeds at a trap prime must have
computed a **non-polynomial integer with a non-residue prime factor**. This is the exact escape boundary of B1 at trap points:
*escape ⟺ generation of a non-formal quadratic non-residue.*

## 4. First falsifier (CERTIFIED computations)

**(F1) Lemma T4 on actual primes** — `scripts/z53_noncrtlogic_trapcheck.py 4000 13 12`
(output `data/z53/noncrtlogic/trapcheck_T4000_L13_B12.txt`). q = 120120·t (t ≤ 4000; M = 8·3·5·7·11·13), p = P(q) prime; test
polynomials h = a + bX (|a|, |b| ≤ 12) and 147 quadratics; "predicted +1" when every prime of 2·lc(P)·Res(R, h^∨) is ≤ 13.

| family P | primes p | h predicted +1 | symbol tests | violations |
|---|---|---|---|---|
| X² + 1 | 557 | 432 | 240 624 | **0** |
| 2X² + 1 | 538 | 368 | 197 984 | **0** |
| 3X² + 1 | 554 | 396 | 219 384 | **0** |
| X⁴ + 1 | 290 | 161 | 46 690 | **0** |
| Φ₅ | 307 | 223 | 68 461 | **0** |
| Φ₆ = X² − X + 1 | 602 | 444 | 267 288 | **0** |
| 2X³ + 2X + 1 | 408 | 272 | 110 976 | **0** |
| X + 1 | 1093 | 700 | 765 100 | **0** |
| *control* X² − 3X + 1 (positive real roots) | 567 | 370 | 209 790 | 86 184 |
| *control* X² + 1, q ≡ 4 (mod 8) | 578 | 432 | 249 696 | 95 948 |
| *control* X² + 1, q ≡ 24 (mod M) (odd trap conditions violated) | 590 | 432 | 254 880 | 83 190 |
| *control* X⁴ + 1, q ≡ 4 (mod 8) | 301 | 161 | 48 461 | 17 458 |

For h *not* predicted, the share of −1 is 0.48–0.50 in every family (the statement is not vacuous). Each control violates
exactly one hypothesis of Lemma T4 and fails massively.

**(F2) End-to-end toy for Theorem T at X² + 1** — `scripts/z53_noncrtlogic_gausstoy.py 20000000 5000` (output
`data/z53/noncrtlogic/gausstoy_2e7.txt`). Program Π_CF: q := ⌊√p⌋ (CF datum a₀); for windows e ∈ {3, q − 1, 2q − 1} search
coprime a, b with ab | N = (p + e)/4, e | a + b, and output the explicit Type II solution (checked exactly with rationals).
At p = q² + 1, q = 120t, the formal family is {X² + 1, X, X + 1, X + 2, X² + 4} (relevant trap primes 2, 3, 5). Admissible t
(t, 120t + 1, 60t + 1, 3600t² + 1, p all prime), t < 2·10⁷: **322 found, Π_CF = FAIL at 322/322** (Theorem T predicts FAIL).
Controls (first 5000 prime p = q² + 1 in the same class, formal values unconstrained): success 3064 (61 %); every success has a
non-residue prime in N (Lemma CT) and occurs at a window whose formal value is composite (3064/3064).

**(F3) Independent (★) census cross-check** (by-product of §6, `scripts/z53_noncrtlogic_qnrseed.py`, exhaustive
enumeration of all (u, B, C) by the trial form B = (p + u)/(4uC − 1), u ≤ B, smallest-prime-factor sieve): among primes
p ≡ 1 (24) in [300, 5·10⁶), R(p) = 0 exactly at 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209,
1726201 — the twelve census zeros of FRONTIER §2.1 in that range (CERTIFIED by one more engine).

## 5. The taxonomy (answers S1)

"Killed" = every correct witness-producing program that uses the primitive (with any bounded computation and any
finite-information oracles) and has a finite formal tree at the stated point fails for infinitely many p ≡ 1 (24),
CONDITIONAL on H for one finite family (the transfer itself is PROVED). "Escapes" = PROVED to have no finite-menu formal
semantics where stated.

| primitive (brief's list and relatives) | status | mechanism / point | label |
|---|---|---|---|
| p mod M; ord_ℓ(p) for fixed ℓ; (u/p), ((p+u)/m) for formal u, m | killed | congruence / finite information; q*_univ | Thm C, Thm A |
| fixed non-abelian Frobenius (FROB_K, (a/p)_m, "2 a cube", p = x² + 27y²?), Artin symbols, h(±p) mod m, any predicate, comparisons | killed | finite information; **E3 closed** without H_K | Thm A, Cor A1 |
| ord_p(a) (fixed or formal a), (p − 1)/ord_p(a), ord_m(a), gcds with p − 1 | killed | divisor of a formal value | Cor A2 |
| prime factors / factorisation of p − 1, p + 1, any fixed f(p) | killed | formal FACTOR | Thm M, C, T |
| ⌊c·p^θ⌋, any finite set with c, θ ∈ ℚ_{>0} | killed | formal on the trap family Φ_N (N prime, b \| N − 1) | Thm T, Cor T2(i) |
| ⌊√(kp)⌋ and the full CF/Pell/unit data of √(kp) (and (1+√(kp))/2 when relevant) for **one** fixed k | killed — **long cycles irrelevant** | formal on the trap family kX² + 1 (Richaud–Degert) | Thm T, Cor T1 |
| Cornacchia data: the representation p = x² + ky² for one fixed k ≥ 1 | killed | (x, y) = (1, q) on kX² + 1 | Thm T, Cor T4 |
| ⌊√(2p)⌋ alone | killed | trap family 2X² + 1 | Cor T2 |
| (⌊√p⌋, ⌊√(2p)⌋) jointly; CF data of √p and √(2p) jointly; ⌊p^θ⌋, θ ∉ ℚ; ⌊log p⌋; ⌊R_p⌋ | **escape**: no formal semantics on any polynomial family | leading-coefficient obstruction | Cor T2(ii), PROVED |
| n_p, least primitive root g_p, least prime ≡ a (m) with (ℓ/p) = −1, any QNR-valued oracle | **escape every trap point** | values are non-residues; trap points are QR-transparent | Cor T3, PROVED |
| h(±p), regulator, discrete logs (as unbounded integers) | open (not proved formal on any trap family; not proved to escape) | Siegel growth makes constancy impossible; exact polynomiality not excluded unconditionally | Assessment |

**Corollary T4 (Fermat/Cornacchia certificates; PROVED transfer, CONDITIONAL on H).** For fixed k ≥ 1, a prime p has at most
one representation p = x² + ky² with x, y > 0 (for k = 1 up to order) (standard; e.g. Cox, *Primes of the form x² + ny²* —
uniqueness of representation by the principal form, statement from memory). On the trap family p = kq² + 1 (kX² + 1 ∈ 𝒫,
P(0) = 1, no real roots) the representation is (1, q) (or (q, 1)), a formal value. So the route of
`BRAINSTORM/gon_fermat_certificates.md` — "find p = Q(u, v) by geometry of numbers, then a bounded Theorem-M procedure" — fails
i.o. under H for every fixed principal form x² + ky²: the step left open there ("Theorem C is PROVED only for linear P; the
extension to quadratic P is not proved") is Theorem T. (Forms with many representations let the procedure *choose* — that
choice is again a "which divisor" event; not covered.)

**Answer to S3 (long cycles).** Not an escape (Cor T1, CONDITIONAL on H). Correctness is a for-all-p requirement, and the
adversary uses the short-cycle primes q² + 1; a procedure that branches on "period > K" is using a finite-information oracle.
Long cycles help only together with an escaping primitive that handles the short-cycle primes — and then the burden is on that
primitive. The CF *norms* Q_k of √p are moreover QNR-blind at every prime (JOINT_BUDGET Prop 4.2: ℓ | Q_k, ℓ ∤ B ⇒ (p/ℓ) = 1),
so by Lemma CT they can never be the non-residue source of a certificate, at any cycle length; only partial quotients and the P_k
(uncontrolled integers below 2√p) can.

## 6. Second half (S2): what the escaping primitives buy

**Proposition S (n_p-seeding reduces to the r-generic line; PROVED, existence CONDITIONAL on H).** Let Π call n_p (any number
of times) and otherwise use formal primitives and finite-information oracles. Fix a prime r ≥ 5 and P = 24X + 1. Call q* ∈ Ẑ
*r-generic* if 24q*_ℓ + 1 is a nonzero square mod ℓ for every prime 3 ≤ ℓ < r and a non-square mod r. Then every prime
p ≡ 24q* + 1 (mod 24∏_{3≤ℓ≤r} ℓ) has n_p = r ((2/p) = 1 as p ≡ 1 (8), (ℓ/p) = (p/ℓ) as p ≡ 1 (4)); so n_p has constant formal
semantics at q*, and Theorem A applies: if Π's formal tree at an r-generic universally nondegenerate q* is finite, Π(p) is its
formal output at every admissible q. Hence an n_p-seeded procedure proves ES for all large p only if, for **every** prime r and
every such r-generic point, its formal output is SUCCESS. Theorem C does not decide this (r is a non-residue, and formal values
h(q) with v_r(H_h) odd are non-residues), which is exactly why n_p escapes.
* For congruence-only seeding the answer is known: by (J)70 = `STERILE_LOWER.md` Thm 6.3 (PROVED, computer-assisted), for every
  prime r ≥ 2^{21.4375} no finite set of ET Prop 1.9 classes covers all large primes with least non-residue r; so every
  procedure that, given n_p = r, certifies by a finite menu of ET Prop 1.9 classes fails i.o. (unconditional: Dirichlet
  supplies the primes). Every r ≤ 13 *is* covered at level 1, r = 17 open ((J)70 Comp 4.1, FRONTIER §7.9).
* With FACTOR the question is FRONTIER §7.9's (uniform multiplicity / sterility on the r-generic line). **So the cheapest
  escaping primitive with complete factorisation control (n_p is a prime) buys exactly the quadratic layer, and what remains is
  the r-generic sterility problem — a B2-type statement** (Assessment, matching FRONTIER's own reading of §7.9).
* n_p is by definition a function of the Legendre symbols (ℓ/p) of small primes ℓ; so are g_p and every "least prime with a
  prescribed symbol". These primitives are the quadratic layer, delivered unboundedly (CLASS_FORCING Thm 2.1: the quadratic
  layer never determines the class). Archimedean escapers (Cor T2(ii)) deliver integers with *no* factorisation control —
  E1 lottery tickets.

**EVIDENCE (the seed supplies the colour, not the divisor event).**
1. *Forest roots: colour factor vs divisor-class factor* (`scripts/z53_noncrtlogic_rootparity.py 1000000 3000000 61`,
   `scripts/z53_noncrtlogic_rootparity_deep.py A B LMIN 113 3000`; outputs `data/z53/noncrtlogic/rootparity_*.txt`). For a prime
   root ℓ of F_p, an edge to a larger neighbour w is w | p + ℓ with w ≡ −p (mod ℓ); writing p + ℓ = w·w′ one has w′ ≡ −1 (mod ℓ)
   and χ(w) = χ(ℓ)χ(w′) (as p + ℓ ≡ ℓ mod p), so **a bichromatic larger edge at ℓ ⟺ p + ℓ has a divisor w′ ≡ −1 (mod ℓ), w′ < (p + ℓ)/ℓ, with
   (w′/p) = −1** (conversely such w′ gives the edge {ℓ, (p + ℓ)/w′}, since then w ≡ −p (mod ℓ)) — a tied-class divisor event; it needs p + ℓ to have a non-residue prime factor ("not F1" in POINTWISE_SIZE
   §8–9 language). A non-residue root ℓ makes (p + ℓ/p) = −1, so p + ℓ always has one (Lemma 9.1 there: seeded windows are
   never F1). Measured (each prime root ℓ in the range at each prime p):

   | sample | root | instances | P(any bichromatic edge) | via smaller nbr | via larger nbr | P(p+ℓ not F1) | P(larger bichrom \| not F1) |
   |---|---|---|---|---|---|---|---|
   | the 3000 primes p ≡ 1 (24) in [10⁶, 1.34·10⁶], ℓ ∈ [5, 113] | residue | 41 911 | 0.174 | 0.036 | 0.155 | 0.478 | **0.324** |
   | same | non-residue | 42 089 | 0.348 | 0.264 | 0.214 | 1 | **0.214** |
   | 3000 deeply square-mimicking p ((ℓ/p) = 1 ∀ ℓ < 29; p ≤ 6.0·10⁷), ℓ ∈ [29, 113] | residue | 28 848 | 0.093 | 0.004 | 0.091 | 0.302 | **0.301** |
   | same | non-residue | 34 152 | 0.285 | 0.180 | 0.160 | 1 | **0.160** |

   (Mordell-hard primes in [10⁶, 3·10⁶), ℓ ∈ [11, 61], direct neighbours: P(bichromatic) 0.174 residue vs 0.453 non-residue.)
   A non-residue root doubles to triples the certificate rate. The gain is (a) smaller-neighbour edges r = (−p mod ℓ),
   r | p + ℓ — congruence events between p mod ℓ and p mod r whose colour is fixed by the sign identity (B1 data; their
   probability ≍ Σ_{r<ℓ} 1/r·(…)/ℓ decays as the root grows), and (b) the removal of F1. **Conditioned on not-F1, the
   tied-class factor is *not* improved by seeding — it is lower (0.214 vs 0.324; 0.160 vs 0.301)**, consistent with a residue
   p + ℓ carrying an even, hence typically larger, number of non-residue prime factors. So the seed supplies parity and nothing
   about the class (EVIDENCE; the explanation is an Assessment).
2. *Which (★) certificates use n_p* (`scripts/z53_noncrtlogic_qnrseed.py`, `data/z53/noncrtlogic/qnrseed_*.txt`): all
   43 433 primes p ≡ 1 (24) in [300, 5·10⁶), all (★) solutions. For each small prime ℓ the share of solutions with ℓ | uBC is
   larger when ℓ is a non-residue than when it is a residue (e.g. ℓ = 11: 0.216 vs 0.185 on [10⁶, 5·10⁶)), and larger still when
   ℓ = n_p (0.267) — consistent with Lemma CT (every certificate needs a non-residue) plus the absence of smaller competing
   non-residues, both quadratic-layer facts. P(some (★) solution uses n_p) = 0.960 ([300, 10⁶)) and 0.978 ([10⁶, 5·10⁶)): the
   n_p-seeded sub-count is *more* often zero (2–4 % of primes) than the full count (12 zeros among 43 433 primes) — seeding
   restricts the lottery, it does not force it. The CF-norm generator s_p (least prime ≡ ±3 (8) dividing a norm of √(2p), a
   non-residue by construction) equals n_p for 70 % of primes and is used by a (★) solution slightly less often (0.945).
3. *Test primes* (`scripts/z53_noncrtlogic_forestroot.py 4 5000`, `data/z53/noncrtlogic/forestroot_d4.txt`; BFS depth ≤ 4,
   ≤ 5000 vertices): at the 14 (★)-zero primes plus 193, 2521, 66529, 3361, 5101441, a bichromatic edge is reached from the
   root n_p at 10/19, from 1 at 11/19, from the least residue prime at 4/19; at 400 Mordell-hard primes < 10⁷: 279, 370, 313/400.
   At 131 trap-family primes q² + 1 (24 | q; *actual* primes, not admissible): 124/131 from n_p, 128/131 from 1 — the trap is
   formal; actual near-square primes are easy, as Theorem T predicts (failure needs all formal values prime). Odd-square control
   (n = m², 10 values): no bichromatic unit edge from root 1 (T1), and n_p does not exist.

## 7. Verdict

**Narrowed, with a strengthened barrier** (Assessment; the theorems are PROVED, the infinitely-many-failures conclusions
CONDITIONAL on H).
* *New theorems.* Theorem A (finite-information oracles; E3 closed without H_K); Corollary A2 (divisor-valued oracles: orders);
  Lemma T4 (QR-transparency of trap points, unconditional); Lemma T5 (universal trap points for every P ∈ 𝒫 with P(0) = 1 and no
  positive real root); Theorem T (Theorem C for all such P — the first nonlinear instance of the formal odd-square principle in
  the repo); Corollaries T1–T4 (Pell/CF/unit data of one radicand, rational-archimedean primitives, Cornacchia certificates,
  QNR oracles).
* *What it buys.* B1's "does not rule out" list shrinks: E3 is gone; E2 is now characterised at trap points — escape ⟺ a
  non-polynomial integer carrying a quadratic non-residue; the brief's list sorts as in §5. Z52D_PELLCYCLE's remaining gap
  ("arbitrary functions of cycle data") and `gon_fermat_certificates.md`'s open step are closed (CONDITIONAL on H).
* *What survives.* (i) QNR-valued primitives (n_p, g_p, …): reduce value-by-value to the r-generic line (Prop S) — open with
  FACTOR (FRONTIER §7.9); (ii) archimedean primitives with irrational relations (no control); (iii) class numbers/regulators
  as integers (status open); (iv) E1 searches and E4 Boolean/counting certificates (untouched, as before).
* Not obtained: any lower-bound mechanism. The lane's honest answer to "a lower-bound mechanism not built from congruence data":
  the only *controlled* non-congruence input that the logic admits is the quadratic layer (non-residues), and that is exactly
  the layer CLASS_FORCING shows is not the class.

**FRONTIER §4 hard screens** for the best positive idea in reach (n_p-seeded certificates):
1. *T1 squares:* passes — n_p does not exist at m² (and Lemma T4 is the precise reason every formal mechanism fails there and at
   trap points).
2. *8/131:* not applicable to the no-go theorems (Lemma CT holds for every numerator 4 | m via (J)41's full T1, so Theorems A/T
   kill numerator-8 programs too — consistent, since barriers are allowed to be numerator-uniform). The n_p-seeded forest
   certificate is 4-specific through the five-slice sign law.
3. *Tied modulus:* **fails** — after seeding, the certificate event (a divisor w′ ≡ −1 (mod ℓ) of p + ℓ that is a
   non-residue) is the B2 event; §6 EVIDENCE 1 shows the seed removes F1 but does not raise the class factor.
4. *Fixed p:* passes (n_p is pointwise; Lemma T4 is pointwise at each admissible p).

## 8. Proposed FRONTIER text (do not edit FRONTIER directly)

*For §3 B1, replace the "Does NOT rule out" bullet by:* "(z53, `Z53_NONCRTLOGIC.md`.) Theorems M/C extend to programs with
arbitrary finite-valued oracles — fixed non-abelian Frobenius data, power-residue and Artin symbols, h(p) mod m, any predicate —
under H alone (Thm A; the old E3 item is closed without a Schinzel–Chebotarev hypothesis), to divisor-valued oracles such as
ord_p(a) (Cor A2), and to every nonlinear family P ∈ 𝒫 with P(0) = 1 and no positive real root (Thm T, via Hilbert reciprocity
in ℚ(β), β a root of XⁿP(1/X); at its trap points every polynomial value is a quadratic residue mod p, unconditionally). Hence the
full Pell/CF/unit data of √(kp) for one fixed k (long cycles are irrelevant: the kill is at Richaud–Degert primes kq² + 1),
⌊c·p^θ⌋ for rational c, θ, and Cornacchia representations by x² + ky² are all inside B1 (CONDITIONAL on H). *Does NOT rule out:*
(E1) p-dependent growing searches; (E2′) primitives producing non-polynomial integers with a quadratic non-residue factor —
at trap points this is exactly the escape condition; the cheapest, n_p, reduces value-by-value to the r-generic line (§7.9);
archimedean primitives with irrational relations ((⌊√p⌋, ⌊√(2p)⌋), ⌊p^θ⌋ with θ ∉ ℚ) escape but carry no factorisation
control; class numbers as integers are unresolved."

*For §6 (dead ends), add:* "Bounded procedures using fixed non-abelian Frobenius data, orders ord_p(a), Pell/CF/unit data of one
radicand (any cycle length), ⌊c·p^θ⌋ (c, θ ∈ ℚ), or Fermat/Cornacchia representations by one principal form → killed under H →
`Z53_NONCRTLOGIC.md` Thms A, T."

*For §7.9, add:* "This is also the exact residue of the non-CRT question for the cheapest escaping primitive: procedures seeded
by the least non-residue reduce, for each value r, to bounded procedures on the r-generic line (`Z53_NONCRTLOGIC.md` Prop S)."

**Bottom line.** The logic angle gives a clean map rather than a mechanism. Every primitive whose information about p is
bounded, divides something polynomial, or becomes polynomial on *some* family with P(0) = 1 and no positive real root is dead
under H — this now includes non-abelian Frobenius data (no H_K needed), multiplicative orders, the entire Pell/continued-fraction
data of √p however long its cycle, rational powers ⌊c·p^θ⌋, and Cornacchia representations. The reason is one unconditional
lemma: at such "trap points" every polynomial value is a quadratic residue mod p, so the formal world looks like an odd square.
Escaping is therefore *equivalent* to manufacturing a non-polynomial integer with a non-residue factor. That is cheap — the
least non-residue does it with perfect factorisation control — but what it buys is precisely the quadratic layer: n_p-seeded
procedures reduce to the r-generic sterility problem, and numerically a non-residue seed doubles to triples forest-certificate
rates only through parity (and small congruence coincidences); conditioned on parity, the tied-class divisor event is no more
likely — in fact less. ES remains open; target 5's obstruction is now sharply "the
class beyond the quadratic layer", i.e. B2.

## 9. Reproducibility

All commands under `timeout` and `ulimit -v 6000000`, from the repository root; `uv run --with sympy --with gmpy2 [--with numpy]`.
```
python scripts/z53_noncrtlogic_trapcheck.py 4000 13 12   > data/z53/noncrtlogic/trapcheck_T4000_L13_B12.txt   # ~1 min
python scripts/z53_noncrtlogic_gausstoy.py 20000000 5000 > data/z53/noncrtlogic/gausstoy_2e7.txt             # ~3 min
python scripts/z53_noncrtlogic_qnrseed.py 300 1000000 47 data/z53/noncrtlogic/qnrseed_3e2_1e6.json           # ~2 min
python scripts/z53_noncrtlogic_qnrseed.py 1000000 5000000 47 data/z53/noncrtlogic/qnrseed_1e6_5e6.json       # ~10 min
python scripts/z53_noncrtlogic_rootparity.py 1000000 3000000 61                                               # seconds
python scripts/z53_noncrtlogic_rootparity_deep.py 1000000 3000000000 29 113 3000 > data/z53/noncrtlogic/rootparity_deep.txt  # ~2 min
python scripts/z53_noncrtlogic_rootparity_deep.py 1000000 3000000000 5 113 3000  > data/z53/noncrtlogic/rootparity_generic.txt
python scripts/z53_noncrtlogic_forestroot.py 4 5000 data/z53/noncrtlogic/forestroot_d4.json                   # seconds
```
(The `.txt` files are the printed outputs; the qnrseed `.txt` files hold stdout of the corresponding runs.)

## 10. Review log
TODO (hostile review pending).
