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
(I2) Groupoid of all classical moves (reversal, rotation, scaling): χ-flips at fixed n occur inside components, via
even numerators or odd-letter rotations; they close up at the same n rarely (box search, §2).

## 1. The sign is the 2-adic isotropy of the path form (PROVED, classical local theory)

For a nondegenerate ternary quadratic form Q over ℚ and a place ℓ (ℓ prime or ∞) put ε_ℓ(Q) = −1 if Q is anisotropic
over ℚ_ℓ, +1 otherwise. Facts used: (F1) a ternary form is anisotropic at an even number of places (Hilbert reciprocity
for its even Clifford algebra C₀(Q), a quaternion algebra ramified exactly where Q is anisotropic); (F2) for odd ℓ, a
ℤ_ℓ-unimodular ternary lattice is isotropic, and ⟨a, b, ℓ^k c⟩ (a, b, c ∈ ℤ_ℓ^*) is anisotropic iff k is odd and
(−ab/ℓ) = −1 (standard, e.g. Cassels, *Rational Quadratic Forms*, Ch. 4; Serre, *Course in Arithmetic*, IV.2).

**Theorem 1.1.** For every positive word w of odd n: **χ(w) = −ε₂(Q_w).** More precisely, for odd primes ℓ,
ε_ℓ(Q_w) = (−A/ℓ)^{v_ℓ(n)}, and ε_∞(Q_w) = −1.
*Proof.* G_w is positive definite (leading minors v, A* = tv − 1, n are positive), so ε_∞ = −1. Let ℓ be odd. If ℓ ∤ n,
L_w ⊗ ℤ_ℓ is unimodular (det n), so ε_ℓ = 1 by (F2). (R-O198 repair: A* need not be an ℓ-unit when ℓ ∤ n, e.g. (3,1,2).)
If ℓ | n: the sublattice ⟨e₁, e₂⟩ has Gram [[v, −1], [−1, t]] of determinant A*, an ℓ-adic unit (A* | tn + 1 and ℓ | n).
Hence over ℤ_ℓ it splits off orthogonally and is ≅ ⟨1, A*⟩ (binary unimodular, ℓ odd), and L_w ⊗ ℤ_ℓ ≅ ⟨1, A*, n/A*⟩.
With ℓ^k ‖ n, (F2) gives ε_ℓ = −1 iff k odd and (−A*/ℓ) = −1; and (−A*/ℓ) = (−A/ℓ) because AA* ≡ 1 (mod ℓ).
So ε_ℓ = (−A/ℓ)^k in all cases. Multiplicativity of the Jacobi symbol: χ(w) = (−A/n) = Π_{ℓ | n} (−A/ℓ)^{v_ℓ(n)} =
Π_{ℓ odd} ε_ℓ(Q_w). By (F1), Π_{all ℓ} ε_ℓ = 1, i.e. ε₂ · (−1) · Π_{ℓ odd} ε_ℓ = 1. ∎
CERTIFIED (`scripts/cf_lib.py` Hilbert symbols, diagonal form ⟨v, vA*, A*n⟩): χ = −ε₂ on all 39 921 words with letters
≤ 40 and n odd; for prime n < 1200, χ = −1 ⟺ Q_w anisotropic at n on all 9 924 words (0 exceptions; R-O198 repair of the count —
26 750 is the number of words over all odd n < 1200 scanned).

**Corollary 1.2 (conceptual reason for the mod-8 sign law).** ε₂(Q_w) depends only on the ℤ₂-isometry class of L_w,
which (det odd, so L_w ⊗ ℤ₂ unimodular) is 2-adically locally constant in G_w (Hensel); so χ is a 2-adically locally
constant function of the word, **independent of n** and uniform over boundary words. That the period is 8 is DK Cor 4.1 /
MODEL_SPECIFIC Lemma 3.0′ (also seen directly: χ is constant on each of the 320 odd-n cells mod 8, letters ≤ 40). Thm 1.1
explains *why* a Jacobi symbol at n is a function of 2-adic data: it is the 2-adic local invariant of a Brauer class,
transported by reciprocity. [Conway–Sloane's oddity formula is the same fact
for lattices: oddity(L₂) − Σ p-excess ≡ 3 (mod 8).]

**Corollary 1.3 (dictionary; PROVED).** Let n = p be an odd prime and w ∈ X_p. TFAE: (i) w is an ES five-slice
certificate (MODEL_SPECIFIC Thm 3.1(a)); (ii) χ(w) = −1; (iii) Q_w is anisotropic over ℚ_p; (iv) **Q_w is isotropic over
ℚ₂**; (v) the conic Q_w = 0 has ℚ₂-points (and ℚ_ℓ-points for every finite prime ℓ ≠ p); (vi) **C₀(Q_w) ≅ B_{p,∞}**, the definite
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
letters < 25), χ never changes. **So in the uniform normalisation χ = (−A/n), scaling preserves χ**; DK's formula is correct, its
"flip" is normalisation-dependent. (R-O198 repair: the earlier blanket "no known move flips χ" was wrong — rotation does,
Prop 1.5, e.g. (3,5,3)₃₇, χ = −1 ↦ (5,3,3)₃₉, χ = +1 — but rotation changes n.)
(c) More generally any move with Q_{w′} rationally similar to Q_w preserves χ and the whole ramification set of C₀; any
move with L_{w′} ⊗ ℤ₂ similar to L_w ⊗ ℤ₂ preserves χ.

**Proposition 1.5 (rotation law; PROVED by finite cell check, `scripts/cf_rotation_law.py`, asserted on all 192 cells).** Rotation w = (t, u, v) ↦ w′ = (u, v, t)
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
  "certificate region" Ω₂ := {w₂ ∈ X_n(ℤ₂) : inv₂ β(w₂) = 0} (for fixed n mod 8: the 60 χ = −1 cells mod 8 of that class; 240 over the four odd classes) carries a Brauer–Manin obstruction
  to positive integral points. At non-square n some ℓ has v_ℓ(n) odd and inv_ℓ takes both values on X_n(ℤ_ℓ) (A ranges over
  all units mod ℓ), so **there is no BM obstruction** (from β) to a positive integral point in Ω₂.
* **SQ₅ in this language (CONJECTURE, = MODEL_SPECIFIC C1 restated):** for odd non-square n ∉ {5, 105} (plus the
  n ≡ 3 (4) cases, which are trivial), *the Brauer–Manin obstruction from β is the only obstruction to positive integral
  points of X_n lying in the 2-adic region Ω₂.* (n = 105: X_105 has no interior point at all, HJ_DEEP (W).)
* *Assessment.* (R-O198 repair: X_n(ℤ_{>0}) is finite, so this is an *existence statement with a prescribed 2-adic
  congruence condition*, not strong approximation.) It is akin to integral Hasse-principle-with-BM statements for a Markoff-type
  affine cubic (projective closure tuv = w²(u + v + nw), boundary triangle at w = 0). Statements of this exact shape are
  known to **fail** in general for Markoff-type log K3 surfaces (Ghosh–Sarnak integral Hasse failures; Loughran–Mitankin,
  failures not explained by BM — from memory, not re-checked here), and Bright–Loughran Thm 1.9 (LITERATURE_AUTOMORPHIC)
  says BM does not control SA on the ES surfaces U_n. So no general theorem applies; SQ₅ would be a *specific* existence statement
  with an exceptional set {105} ∪ squares (boundary words included). Proved here: β supplies the T1 obstruction; that it is
  the *only* obstruction is the conjecture. The reformulation makes "χ-flip" = "change of inv₂ β", a 2-adic local quantity.

## 2. The move groupoid: what flips, and where (EVIDENCE + elementary PROVED statements)

Moves considered (`scripts/cf_groupoid.py L NMAX [odd]`): reversal (t, u, v) ↦ (t, v, u) (same n); rotation and inverse
rotation (n ↦ n + u − t etc.); scaling down (a | u, v: (t, u, v) ↦ (at, u/a, v/a), n ↦ n/a) and up. By Cor 1.4 and
Prop 1.5, along any chain χ changes only at rotations with all letters odd and t ≢ u (mod 4), or across a step whose
numerator is even (χ undefined there, ε₂ of an even-determinant lattice is unconstrained).
* **2.1 (EVIDENCE).** Letters ≤ 60, numerators ≤ 10⁵, all moves: 20 284 components; 7 numerators n have two words of
  different χ in one component: n = 11, 79, 89, 93, 233, 419, 439 (89, 233 primes ≡ 1 mod 8). Example (BFS path):
  (6,18,1)₈₉ → (18,1,6)₁₀₁ → (9,2,12)₂₀₂ → (2,12,9)₁₉₅ → (6,4,3)₆₅ → (4,3,6)₆₃ → (12,1,2)₂₁ → (3,4,8)₈₄ → (8,3,4)₈₉,
  χ: +1 → … → −1 (subscript = numerator). In this box every flip chain found passes through an even numerator.
* **2.2 (EVIDENCE).** Restricting to odd numerators: 0 flips with letters ≤ 60 / n ≤ 10⁵; with letters ≤ 130 / n ≤ 10⁶,
  278 014 components (R-O198 repair: seeds now also parity-filtered; first run reported 967 703) and exactly 2 flips, at the *composites* n = 125 = 5³ and 1119 = 3·373, both via the odd-letter
  rotation flip of Prop 1.5. (At the cell level mod 8 the odd-move groupoid admits a consistent ±1 labelling g with
  χg invariant, but g is not a function of n mod 8 — 29 cell components, 12 component/n-class pairs carry both labels —
  so the absence of odd flips is not a congruence theorem, just rarity of chains closing up at the same n.)
* **2.3 (PROVED, elementary, for this class of maps only): fixed chains are surface-restricted cell maps.** A fixed finite chain of these moves (fixed
  factors a_i) is a map Φ(w) = D·P·w (P a permutation matrix, D a diagonal matrix of fixed positive rationals) on a
  congruence-defined domain. Unless D·P is the identity or the reversal, K(Φ(w)) = K(w) is a nontrivial equation of degree ≤ 3 (e.g. linear, u = t, for a rotation)
  (the monomial tuv is multiplied by det D, the linear part −u − v is permuted/rescaled), so Φ preserves n only on the
  curve Z_Φ ∩ X_n. On that curve, whether Φ flips χ is a function of w modulo 8·(denominators of D) (Cor 1.2). Hence a
  fixed chain is an ES mechanism only through the Diophantine event "X_p ∩ Z_Φ has a positive point in a flipping cell" —
  a Diophantine condition on a curve, not a map defined on all of X_p. (Nonlinear maps and input-dependent chains are
not covered.) (The example chain of 2.1 is Φ(t, u, v) = (8v, t/2, 2u/9), and
  Z_Φ: tuv = 7u + 9v − 9t/2; it passes through (6, 18, 1).)
* *Reading.* "Leaving X_n" is not what flips χ (χ is n-free, Cor 1.4(a)); what flips it is a change of the 2-adic class of
  the path lattice, which classical moves effect only at odd-letter rotations or through even determinants; in the boxes
  searched such composites return to the same n rarely. Proved scope: no *fixed* chain of classical moves is an
  n-preserving flip on all of X_n (2.3); general maps are not excluded.
  This sharpens HJ_DEEP C3 / MODEL_SPECIFIC C3: the earlier "scaling is the only flip" was a normalisation artefact.

## 3. Constructions tried against the 2-adic form of the problem

**3.1 Mordell's moduli inside the HJ ball (PROVED, elementary; known in substance).** Let p ≡ 1 (mod 4) be prime and q
prime with (q/p) = −1. The integer A = q is the A-value of a word of p iff t₀ := (−p⁻¹ mod q) ∈ [1, q] divides q + 1 (then
t = t₀, u = (q + 1)/t₀, v = ((tp + 1)/q + 1)/t ≥ 1; A* = (tp+1)/q ≡ −1 (mod t) automatically since AA* ≡ 1). Such a word
has χ = (−q/p) = −1, an ES certificate. Since (p/q) = −1, t₀ runs over the quadratic non-residues (q ≡ 1 mod 4) resp.
residues (q ≡ 3 mod 4) of q. **Exactly for q ∈ {3, 5, 7} every such class divides q + 1** (q = 3: {1} | 4; q = 5: {2, 3} | 6;
q = 7: {1, 2, 4} | 8); for q = 11 the classes t₀ = 5, 9 fail (p ≡ 2, 6 mod 11), q = 13 fails, q = 17 fails (non-residues {3,5,6,7,10,11,12,14} vs divisors {1,2,3,6,9} of 18), and for q ≥ 19,
d(q + 1) ≤ 2√(q + 1) < (q − 1)/2. *q = 2* (R-O198 repair): if p ≡ 5 (8), t₀ = 1 | 3 and (1, 3, (p + 3)/2) is a word with
A = 2, χ = (−2/p) = −1.
So: *if 2, 3, 5 or 7 is a non-residue mod p, the word (t₀, (q+1)/t₀, ·) is a certificate* — Mordell's 840 (= 8·3·5·7) in HJ form;
the residual primes are p ≡ □ (mod 840), the T1 classes. CERTIFIED (`scripts/cf_mordell_check.py`): all primes p ≡ 1 (mod 4) < 10⁶, q ∈ {3, 5, 7} non-residue ⟹ the word exists and has χ = −1 (0 failures). No new content (B1), but it locates where a "Vinogradov-type"
argument would have to start: the least non-residue q_p ≥ 11 is the hard case.
**3.2 Vinogradov's trick does not transfer (Assessment).** Vinogradov's q_p < √p + 1 uses that the set of "small" integers
is closed under the operation m ↦ ⌈p/q⌉q − p and that χ is multiplicative on it. The A-set of X_p is L(p) = {A : t₀(A) | A + 1},
t₀(A) = −p⁻¹ mod A; it is not closed under products or under any Euclid step (A ∈ L(p), A′ ∈ L(p) ⇏ AA′ mod p ∈ L(p)), and
the only operations on it that are uniform in p are the Klein symmetries and the cell-preserving maps of §2. Given a
non-residue q ≥ 11, a certificate with A = qk needs t₀(qk) | qk + 1, a divisor-in-class event (H-A).

## 4. The signed sum Σχ over X_n, and the census to 10⁶

**4.1 Census (CERTIFIED by exhaustive enumeration, `scripts/cf_census.c` + `cf_census_summary.py`; enumerator checked
against the brute-force `cf_lib.words` for all odd n ≤ 300).** All positive words (boundary words included), all odd
n ≤ 10⁶:
* the **only** odd non-square n ≤ 10⁶ with χ ≡ +1 on X_n(ℤ_{>0}) is **n = 105** (|X_105| = 11, all boundary words, all +1);
  in particular n = 5 is not exceptional once boundary words count ((4, 1, 2), χ = −1);
* all 499 odd squares 9 ≤ m² ≤ 10⁶ have χ ≡ +1 (mean |X_{m²}| = 70.7) — T1 control;
* 19 552 primes p ≡ 1 (8): mean N₋/|X_p| = 0.606, minimum 4/37 at p = 2521 (the ES "hardest small prime" of MODEL_SPECIFIC §5.2).
* χ ≡ −1 on all of X_n happens for 38 odd n ≤ 10⁶, all ≡ 3 (mod 4) (15, 311 (prime), 455, 495, …): so the correct
  form is **"χ is not identically +1 on X_n ⟺ n non-square, n ≠ 105"** (R-O198 repair: "non-constant" is false, e.g. n = 15;
  the same wording issue affects MODEL_SPECIFIC C1/C3, where it is meant for n ≡ 1 (4)). This holds for all odd n ≤ 10⁶ (= MODEL_SPECIFIC C1 with boundary words;
HJ_DEEP has the interior version to 10⁸/10⁹).

**4.2 Exact facts about S(n) = Σ_{X_n} χ = |X_n| − 2N₋ (PROVED).** (a) At primes p ≡ 1 (4), N₋ is even and |X_p| odd:
reversal (t, u, v) ↔ (t, v, u) preserves χ and its only fixed point is (p + 2, 1, 1) (u = v forces u(tu − 2) = p), with
A = p + 1, χ = (−1/p) = +1. (b) At n = m², S = |X_n|. (c) By Thm 1.1, S(n) = −Σ_{w ∈ X_n} ε₂(Q_w): a count of the
integral points of X_n weighted by a 2-adic cell function, i.e. Σ over the 320 cells c mod 8 of ±#(X_n(ℤ_{>0}) ∩ c).
*No closed formula found (Assessment).* For fixed t the t-fibre sum is a divisor sum of tn + 1 in classes mod 8t; the
sum over t is the (★)-family. A Dedekind/HZ formula sees r − r′ (DK (D3)) and the residue of 12ns(A, n) — both
cell/2-adic data — and Σ_A (A/n)s(A, n) = 0 for even characters; nothing in that toolbox singles out the length-3 ball.
Parity is no help: N₋/2 is even for 1162 and odd for 1222 primes p ≡ 1 (8) < 10⁵. Size check (B3): even an exact
formula would have to prove S(p) < |X_p| where |X_p| ≍ log² p on average with no pointwise lower bound beyond (W).
