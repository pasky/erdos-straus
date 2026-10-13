# CHI_FLIP — χ-flipping moves on X_n: tuv − u − v = n (task O198, spark relay S)

Status: checkpoint in progress (O198). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on MODEL_SPECIFIC.md (O197, CLAIMED: Thm 3.1, C1, C3), DEDEKIND_ES.md (DK), HJ_DEEP.md, BRAINSTORM/bsA_*.
Scripts `scripts/cf_*` (library `cf_lib.py`).

Notation. A *word* is w = (t, u, v) ∈ ℤ³_{≥1} with K(w) := tuv − u − v = n, n odd ≥ 1 (all positive points of X_n,
boundary words included). A = tu − 1, A* = tv − 1, AA* = tn + 1 (so A, A* ≥ 1 and gcd(A, n) = gcd(A*, n) = 1).
χ(w) := (−A/n) (Jacobi). Path form: Q_w(x, y, z) = v x² + t y² + u z² − 2xy − 2yz, Gram matrix
G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]], det G_w = n (DK / bsA_selling_sandpile: Greene's linear lattice).
(For the path order: G_w is the plumbing matrix of [[v, t, u]] with middle letter t.)

## 0. Iteration log
(I1) First target: an intrinsic description of χ that makes the move question well posed independently of n.
Found: χ is minus the 2-adic Hasse/isotropy sign of Q_w (Thm 1.1, Hilbert reciprocity). Consequence: χ is a function
of the word alone (not of n), and DK's "scaling flip" is an artefact of using (A/n) instead of (−A/n) (Cor 1.4).
(I2) Groupoid of all classical moves (reversal, rotation, scaling): χ-flips at fixed n occur inside components, but only
along chains through even numerators (box search, §2).

## 1. The sign is the 2-adic isotropy of the path form (PROVED, classical local theory)

For a nondegenerate ternary quadratic form Q over ℚ and a place ℓ (ℓ prime or ∞) put ε_ℓ(Q) = −1 if Q is anisotropic
over ℚ_ℓ, +1 otherwise. Facts used: (F1) a ternary form is anisotropic at an even number of places (Hilbert reciprocity
for its even Clifford algebra C₀(Q), a quaternion algebra ramified exactly where Q is anisotropic); (F2) for odd ℓ, a
ℤ_ℓ-unimodular ternary lattice is isotropic, and ⟨a, b, ℓ^k c⟩ (a, b, c ∈ ℤ_ℓ^*) is anisotropic iff k is odd and
(−ab/ℓ) = −1 (standard, e.g. Cassels, *Rational Quadratic Forms*, Ch. 4; Serre, *Course in Arithmetic*, IV.2).

**Theorem 1.1.** For every positive word w of odd n: **χ(w) = −ε₂(Q_w).** More precisely, for odd primes ℓ,
ε_ℓ(Q_w) = (−A/ℓ)^{v_ℓ(n)}, and ε_∞(Q_w) = −1.
*Proof.* G_w is positive definite (leading minors v, A* = tv − 1, n are positive), so ε_∞ = −1. Let ℓ be odd. The
sublattice ⟨e₁, e₂⟩ has Gram [[v, −1], [−1, t]] of determinant A*, an ℓ-adic unit (A* | tn + 1). Hence over ℤ_ℓ it splits
off orthogonally and is ≅ ⟨1, A*⟩ (binary unimodular, ℓ odd), and L_w ⊗ ℤ_ℓ ≅ ⟨1, A*, n/A*⟩. If ℓ ∤ n this is unimodular,
ε_ℓ = 1. If ℓ^k ‖ n, (F2) gives ε_ℓ = −1 iff k odd and (−A*/ℓ) = −1; and (−A*/ℓ) = (−A/ℓ) because AA* ≡ 1 (mod ℓ).
So ε_ℓ = (−A/ℓ)^k in all cases. Multiplicativity of the Jacobi symbol: χ(w) = (−A/n) = Π_{ℓ | n} (−A/ℓ)^{v_ℓ(n)} =
Π_{ℓ odd} ε_ℓ(Q_w). By (F1), Π_{all ℓ} ε_ℓ = 1, i.e. ε₂ · (−1) · Π_{ℓ odd} ε_ℓ = 1. ∎
CERTIFIED (`scripts/cf_lib.py` Hilbert symbols, diagonal form ⟨v, vA*, A*n⟩): χ = −ε₂ on all 39 921 words with letters
≤ 40 and n odd; for prime n ≤ 1200, χ = −1 ⟺ Q_w anisotropic at n on all 26 750 words (0 exceptions).

**Corollary 1.2 (conceptual reason for the mod-8 sign law).** ε₂(Q_w) depends only on the ℤ₂-isometry class of L_w,
which (det odd, so L_w ⊗ ℤ₂ unimodular) is 2-adically locally constant in G_w (Hensel); so χ is a 2-adically locally
constant function of the word, **independent of n** and uniform over boundary words. That the period is 8 is DK Cor 4.1 /
MODEL_SPECIFIC Lemma 3.0′ (also seen directly: χ is constant on each of the 320 odd-n cells mod 8, letters ≤ 40). Thm 1.1
explains *why* a Jacobi symbol at n is a function of 2-adic data: it is the 2-adic local invariant of a Brauer class,
transported by reciprocity. [Conway–Sloane's oddity formula is the same fact
for lattices: oddity(L₂) − Σ p-excess ≡ 3 (mod 8).]

**Corollary 1.3 (dictionary; PROVED).** Let n = p be an odd prime and w ∈ X_p. TFAE: (i) w is an ES five-slice
certificate (MODEL_SPECIFIC Thm 3.1(a)); (ii) χ(w) = −1; (iii) Q_w is anisotropic over ℚ_p; (iv) **Q_w is isotropic over
ℚ₂**; (v) the conic Q_w = 0 has ℚ₂-points (and ℚ_ℓ-points for every ℓ ≠ p); (vi) **C₀(Q_w) ≅ B_{p,∞}**, the definite
quaternion algebra ramified at p (the endomorphism algebra of supersingular curves in characteristic p); explicitly
B_{p,∞} ≅ (−A*, −vA*p). Otherwise C₀(Q_w) ≅ B_{2,∞} (Hurwitz quaternions).
At n = m² (odd): every ε_ℓ = +1 for odd ℓ (v_ℓ(n) even), so every word has C₀(Q_w) ≅ B_{2,∞}: **T1 = "a positive ternary
lattice with cyclic discriminant group of square order cannot ramify at an odd prime".** (Cyclicity is essential: the
2×2 minor of G_w equal to 1 forces discriminant group ℤ/n; non-cyclic lattices of determinant m² can ramify at q | m.)
*Reading.* ES five-slice(p) ⟺ the cubic surface X_p has a positive integral point whose path form is 2-adically
isotropic; equivalently, whose even Clifford order (a Gorenstein order of reduced discriminant 4p, Gross–Lucianovic) lies
in B_{p,∞}. This is the bsA_selling_sandpile D3 genus statement upgraded from the p-adic genus to the rational class,
and extended uniformly to all odd n.

**Corollary 1.4 (χ is n-free; scaling preserves χ; PROVED).** (a) For words w ∈ X_n, w′ ∈ X_{n′} (n, n′ odd):
χ(w)χ(w′) = ε₂(Q_w)ε₂(Q_{w′}). So whether a move "flips" is a property of the two 2-adic lattices only; leaving X_n
through odd composite numerators confers no extra power per se.
(b) Scaling DK 8.3: (v′, at, u′) ↦ (av′, t, au′) (numerator m ↦ am, a odd). Then Q′(x, y, z) = a·Q(x, y/a, z), a rational
similarity, so ε₂ (indeed every ε_ℓ) is unchanged and **χ(w′) = χ(w)**. Direct check: χ_{am}(A) = (−A/a)(−A/m) =
(1)·χ_m(A) since −A ≡ 1 (mod a). DK 8.3/HJ_DEEP C3 called scaling "the only flip" because they used (A/n), which differs
from χ by (−1/n); the a ≡ 3 (mod 4) condition there is exactly that normalisation. CERTIFIED: 43 200 scalings (a < 12,
letters < 25), χ never changes. **So in the uniform normalisation χ = (−A/n), no previously known move flips χ.**
(c) More generally any move with Q_{w′} rationally similar to Q_w preserves χ and the whole ramification set of C₀; any
move with L_{w′} ⊗ ℤ₂ similar to L_w ⊗ ℤ₂ preserves χ.

**Proposition 1.5 (rotation law; PROVED by finite cell check, `cf_t4`).** Rotation w = (t, u, v) ↦ w′ = (u, v, t)
([[v, t, u]] ↦ [[t, u, v]], n′ = n + u − t), both numerators odd: χ(w′) = −χ(w) **iff t, u, v are all odd and t ≢ u (mod 4)**
(then n ≢ n′ mod 4). Otherwise χ is preserved (in particular whenever n ≡ n′ (mod 4), recovering DK 8.2). The flip is not a
function of (n, n′) mod 8. Since rotation changes n, it is not a move on X_n.

**Proposition 1.6 (χ is the evaluation of an Azumaya algebra on X_n; T1 is its Brauer–Manin obstruction; PROVED
except where labelled).** The ternary form Q_{t,u,v} has determinant tuv − u − v = n, a constant, on the whole surface
X_n. Hence over X_n ⊗ ℤ[1/2n] it is a nondegenerate ternary form, and its even Clifford algebra 𝒞 = C₀(Q) is an Azumaya
quaternion algebra on X_n ⊗ ℤ[1/2n] (standard: even Clifford algebra of a regular ternary form; Knus, *Quadratic and
Hermitian forms over rings*, IV). Write β = [𝒞] ∈ Br(X_{n,ℚ}). For w ∈ X_n(ℤ), inv_ℓ β(w) = 0 for ℓ ∤ 2n (Azumaya over ℤ_ℓ),
inv_∞ β(w) = ½ on the positive cone (positive definite), and Thm 1.1 is literally Σ_v inv_v β(w) = 0.
* **T1 as Brauer–Manin.** At odd n = m², inv_ℓ β(w_ℓ) = 0 for *every* ℓ-adic integral point w_ℓ, ℓ | m (Thm 1.1's local
  formula: ε_ℓ = (−A/ℓ)^{v_ℓ(n)} with v_ℓ(n) even). So on the positive real cone, BM reciprocity forces inv₂ β = ½: the 2-adic
  "certificate region" Ω₂ := {w₂ ∈ X_n(ℤ₂) : inv₂ β(w₂) = 0} (= the 240 χ = −1 cells mod 8) carries a Brauer–Manin obstruction
  to positive integral points. At non-square n some ℓ has v_ℓ(n) odd and inv_ℓ takes both values on X_n(ℤ_ℓ) (A ranges over
  all units mod ℓ), so **there is no BM obstruction** (from β) to a positive integral point in Ω₂.
* **SQ₅ in this language (CONJECTURE, = MODEL_SPECIFIC C1 restated):** for odd non-square n ∉ {5, 105} (plus the
  n ≡ 3 (4) cases, which are trivial), *the Brauer–Manin obstruction from β is the only obstruction to positive integral
  points of X_n lying in the 2-adic region Ω₂.* (n = 105: X_105 has no interior point at all, HJ_DEEP (W).)
* *Assessment.* This is an integral strong-approximation-with-BM statement at the single place 2 for a Markoff-type
  affine cubic (projective closure tuv = w²(u + v + nw), boundary triangle at w = 0). Statements of this exact shape are
  known to **fail** in general for Markoff-type log K3 surfaces (Ghosh–Sarnak integral Hasse failures; Loughran–Mitankin,
  failures not explained by BM — from memory, not re-checked here), and Bright–Loughran Thm 1.9 (LITERATURE_AUTOMORPHIC)
  says BM does not control SA on the ES surfaces U_n. So no general theorem applies; SQ₅ would be a *specific* SA statement
  with an exceptional set {5, 105} ∪ squares. The value of the reformulation is that it isolates the only obstruction
  as Brauer–Manin, and makes "χ-flip" = "change of inv₂ β", a 2-adic local quantity.

## 2. The move groupoid: what flips, and where (EVIDENCE + elementary PROVED statements)

Moves considered (`scripts/cf_groupoid.py L NMAX [odd]`): reversal (t, u, v) ↦ (t, v, u) (same n); rotation and inverse
rotation (n ↦ n + u − t etc.); scaling down (a | u, v: (t, u, v) ↦ (at, u/a, v/a), n ↦ n/a) and up. By Cor 1.4 and
Prop 1.5, along any chain χ changes only at rotations with all letters odd and t ≢ u (mod 4), or across a step whose
numerator is even (χ undefined there, ε₂ of an even-determinant lattice is unconstrained).
* **2.1 (EVIDENCE).** Letters ≤ 60, numerators ≤ 10⁵, all moves: 20 284 components; 7 numerators n have two words of
  different χ in one component: n = 11, 79, 89, 93, 233, 419, 439 (89, 233 primes ≡ 1 mod 8). Example (BFS path):
  (6,18,1)₈₉ → (18,1,6)₁₀₁ → (9,2,12)₂₀₂ → (2,12,9)₁₉₅ → (6,4,3)₆₅ → (4,3,6)₆₃ → (12,1,2)₂₁ → (3,4,8)₈₄ → (8,3,4)₈₉,
  χ: +1 → … → −1 (subscript = numerator). Every flip chain found passes through an even numerator.
* **2.2 (EVIDENCE).** Restricting to odd numerators: 0 flips with letters ≤ 60 / n ≤ 10⁵; with letters ≤ 130 / n ≤ 10⁶,
  967 703 components and exactly 2 flips, at the *composites* n = 125 = 5³ and 1119 = 3·373, both via the odd-letter
  rotation flip of Prop 1.5. (At the cell level mod 8 the odd-move groupoid admits a consistent ±1 labelling g with
  χg invariant, but g is not a function of n mod 8 — 29 cell components, 12 component/n-class pairs carry both labels —
  so the absence of odd flips is not a congruence theorem, just rarity of chains closing up at the same n.)
* **2.3 (PROVED, elementary): fixed chains are surface-restricted cell maps.** A fixed finite chain of these moves (fixed
  factors a_i) is a map Φ(w) = D·P·w (P a permutation matrix, D a diagonal matrix of fixed positive rationals) on a
  congruence-defined domain. Unless D·P is the identity or the reversal, K(Φ(w)) = K(w) is a nontrivial cubic equation
  (the monomial tuv is multiplied by det D, the linear part −u − v is permuted/rescaled), so Φ preserves n only on the
  curve Z_Φ ∩ X_n. On that curve, whether Φ flips χ is a function of w modulo 8·(denominators of D) (Cor 1.2). Hence a
  fixed chain is an ES mechanism only through the Diophantine event "X_p ∩ Z_Φ has a positive point in a flipping cell" —
  a lottery of the B2 type, never a deterministic map. (The example chain of 2.1 is Φ(t, u, v) = (8v, t/2, 2u/9), and
  Z_Φ: tuv = 7u + 9v − 9t/2; it passes through (6, 18, 1).)
* *Reading.* "Leaving X_n" is not what flips χ (χ is n-free, Cor 1.4(a)); what flips it is a change of the 2-adic class of
  the path lattice, which classical moves effect only at odd-letter rotations or through even determinants, and the
  composite returns to the same n only by coincidence. **No n-preserving move with a deterministic domain flips χ.**
  This sharpens HJ_DEEP C3 / MODEL_SPECIFIC C3: the earlier "scaling is the only flip" was a normalisation artefact.

## 3. Constructions tried against the 2-adic form of the problem

**3.1 Mordell's moduli inside the HJ ball (PROVED, elementary; known in substance).** Let p ≡ 1 (mod 4) be prime and q
prime with (q/p) = −1. The integer A = q is the A-value of a word of p iff t₀ := (−p⁻¹ mod q) ∈ [1, q] divides q + 1 (then
t = t₀, u = (q + 1)/t₀, v = ((tp + 1)/q + 1)/t ≥ 1; A* = (tp+1)/q ≡ −1 (mod t) automatically since AA* ≡ 1). Such a word
has χ = (−q/p) = −1, an ES certificate. Since (p/q) = −1, t₀ runs over the quadratic non-residues (q ≡ 1 mod 4) resp.
residues (q ≡ 3 mod 4) of q. **Exactly for q ∈ {3, 5, 7} every such class divides q + 1** (q = 3: {1} | 4; q = 5: {2, 3} | 6;
q = 7: {1, 2, 4} | 8); for q = 11 the class 5 fails, q = 13 fails, and for q ≥ 17, d(q + 1) ≤ 2√(q + 1) < (q − 1)/2.
So: *if 3, 5 or 7 is a non-residue mod p, the word (t₀, (q+1)/t₀, ·) is a certificate* — Mordell's 840 (= 8·3·5·7) in HJ form;
the residual primes are p ≡ □ (mod 840), the T1 classes. No new content (B1), but it locates where a "Vinogradov-type"
argument would have to start: the least non-residue q_p ≥ 11 is the hard case.
**3.2 Vinogradov's trick does not transfer (Assessment).** Vinogradov's q_p < √p + 1 uses that the set of "small" integers
is closed under the operation m ↦ ⌈p/q⌉q − p and that χ is multiplicative on it. The A-set of X_p is L(p) = {A : t₀(A) | A + 1},
t₀(A) = −p⁻¹ mod A; it is not closed under products or under any Euclid step (A ∈ L(p), A′ ∈ L(p) ⇏ AA′ mod p ∈ L(p)), and
the only operations on it that are uniform in p are the Klein symmetries and the cell-preserving maps of §2. Given a
non-residue q ≥ 11, a certificate with A = qk needs t₀(qk) | qk + 1, a divisor-in-class event (H-A).
