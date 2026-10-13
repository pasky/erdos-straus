# R199 — hostile review of CONSTRUCTIVE_ES.md (O199)

Reviewer: R199 side agent. Document reviewed: CONSTRUCTIVE_ES.md as merged from side-agent/constructive-es.
From-scratch scripts: scripts/review_ce_*.py (own Clifford/quaternion arithmetic, own class enumeration, own X₀(2) count).
No quaternion-arithmetic literature is present in sources/; all literature statements were checked from memory only
and are flagged as such.

(work in progress)

## Verdicts and checks, claim by claim

### Lemma 1.1 (2-adic isotropy) — SOUND
Re-derived the proof. It is correct: odd squares are ≡ 1 (mod 8); with odd-coordinate set S the value is
Q(x) ≡ Σ_{i∈S} a_i (mod 4); |S| = 2 is forced, and if the residues are not all equal exactly two pairs qualify.
From scratch (`scripts/review_ce_local.py`): for all 64 triples a ∈ {1,3,5,7}³ I decided isotropy by brute force
(a primitive x mod 8 with Q(x) ≡ 0 mod 8; this is enough by Hensel, because ∂Q/∂x_i = 2a_ix_i has valuation 1).
I compared that with (i) "residues mod 4 not all equal", (ii) the Hilbert symbol (−a₁a₃, −a₂a₃)₂, and (iii) the number
of nonzero x mod 2 with Q(x) ≡ 0 (mod 4), which should be 2 if isotropic and 0 otherwise. Result: 0 failures;
48 triples are isotropic and 16 anisotropic. Diagonalisability of odd unimodular ℤ₂-lattices is standard (O'Meara 93:15,
from memory). Minor: the proof's sentence about isotropy depending only on a_i mod 8 is a remark, not a step;
the brute-force check above is what actually closes the equivalence.

### Thm 1.2 (Eichler ladder) — SOUND-AFTER-REPAIRS (minor wording only)
I re-derived it and re-checked it with a stronger computation than the author's. The author's check climbs index-2
overorders one at a time. Mine (`scripts/review_ce_lib.py`, `review_ce_local.py`) lists **every** overorder of
2-power index exactly, as Λ + H with H a subgroup of the 2-part of Λ^♯/Λ (Λ^♯ is the trace dual; every overorder
lies in Λ^♯). I used my own even-Clifford arithmetic in a ℚ-orthogonal basis.
For all 64 diagonal triples I checked:
* trd(Λ) ⊂ 2ℤ;
* exactly one index-2 overorder E, with discrd(E) = discrd(Λ)/2;
* E contains an element of odd trace;
* in the isotropic case (48 triples): exactly two overorders of discrd(Λ)/4 and none larger, both contain E, and they
  equal, as sets, C₀(L⁺₁) and C₀(L⁺₂) built from the two classes x mod 2 of Lemma 1.1;
* in the anisotropic case (16 triples): no overorder beyond E.

Result: 0 failures. The global reduction to the 64 triples is also sound: overorders of 2-power index are local at 2,
and odd unimodular ℤ₂-lattices are diagonal with unit square classes mod 8.
"discrd squarefree ⟹ hereditary" (used for "discrd 2 in M₂(ℚ₂) ⟹ Eichler level 2") is a standard theorem
(Voight, *Quaternion Algebras*, ch. 23, from memory). I checked the conceptual formulas Λ₂ = ℤ₂ + J(E₂) by hand.

On path lattices (`scripts/review_ce_words.py`) I used full 2-power overorder enumeration plus a *p-adic* χ that does
not depend on CHI_FLIP: anisotropy of L_w at p, read off as (−M/p) for a 2×2 principal minor M ≢ 0 (mod p).
* For p ∈ {41, 73, 89, 97, 113} there are 151 words, 72 with χ = −1; this reproduces the author's counts exactly.
  For p ∈ {37, 61, 101, 109, 157} there are 135 more words.
* Every word has a unique index-2 overorder, of discrd 2p.
* There are 2 maximal 2-overorders (discrd p) ⟺ χ = −1, and none otherwise.
* Trace-zero elements of E lie in C₀ (so E⁰ = C₀⁰).
* p-adic anisotropy agrees with (−A/p) every time.
* 0 failures.

Wording issues → D7 (L⁺_i is not classical: B(x/2, e_i) ∈ ½ℤ; only Q is integral).

### Thm 2.1 (bijection 𝔊⁻_p ⟷ level-2 Eichler types ⟷ X₀(2)^ss/⟨Frob, w₂⟩) — SOUND-AFTER-REPAIRS (D1, D6)
**Independent recount** (`scripts/review_ce_classes.py`). Both sides are computed by methods different from the author's.
* Lattice side: I enumerate every Gram matrix that satisfies the necessary Minkowski conditions
  (a ≤ b ≤ c, 2|f|, 2|e| ≤ a, 2|d| ≤ b, abc ≤ 2p). The canonical form is the lexicographically least Gram over all bases
  that realise the successive minima. Anisotropy at p is read off as (−M/p) for a principal 2×2 minor M ≢ 0 (mod p).
* Curve side: no Vélu and no 2-torsion bookkeeping. I use the X₀(2) Hauptmodul s:
  j(τ) = (s+256)³/s², j(2τ) = (s+16)³/s, w₂: s ↦ 4096/s, Frob: s ↦ s^p.
  I checked these identities by hand: substituting s ↦ 4096/s turns (s+16)³/s into (s+256)³/s².
  The supersingular j's are the roots of Deuring's Legendre polynomial Σ C(m,i)² λ^i, found by brute force over 𝔽_{p²}.
  I then count the s ∈ 𝔽_{p²}^* lying over a supersingular j, and their orbits.

| primes | result |
|---|---|
| all 8 of the author's primes 37, 61, 73, 97, 109, 157, 181, 193 | |𝔊⁻_p| = 4, 6, 7, 9, 9, 14, 15, 15 = #orbits, identical to the author's values |
| **every** prime 5 ≤ p ≤ 139 not ≡ 1 (mod 12) (5, 7, 11, 13, …, 139; 24 primes) | |𝔊⁻_p| = #orbits in all cases, including p where j = 0 or 1728 is supersingular (X₀(2) has an elliptic point over 1728) |
| p = 1201, 2521 (`scripts/review_ce_rank.py`) | |𝔊⁻_p| = 82, 166, matching §5.5 |

So the class-count equality is CERTIFIED by me well beyond the author's range, and its restriction to p ≡ 1 (mod 12)
was not needed.

**Inputs.** Each input below was checked from memory (no source in sources/):
* Gross–Lucianovic (Math. Ann. 2009): a discriminant-preserving bijection between twisted-GL₃(ℤ) classes of ternary
  quadratic forms and isomorphism classes of quaternion rings, with Gorenstein ⟺ primitive form.
  - For positive forms the twisted action reduces to isometry, because −g has det −det g in dimension 3 and q∘(−g) = q∘g.
    The proof's phrase "isometry up to sign" is therefore fine.
  - Their discriminant is N(q) = 4·det(B-Gram), and N(cq) = c³N(q). So "c³ | 4p ⟹ c = 1" is correct.
* Deuring: level-N Eichler types ⟷ (E, C) up to the action of the two-sided ideal class group, which here is generated
  by the ideals over p (↔ Frob) and over 2 (↔ w₂). This is standard (e.g. Voight ch. 42, from memory).
  The author's phrase "End(E, C) ≅ End(E′, C′) iff in the ⟨Frob, w₂⟩-orbit" is the correct type-number statement.
* "Known in substance (Brzezinski / Lehman / Gross–Lucianovic)": I agree. The ternary-form ↔ order dictionary for
  Eichler / Gorenstein orders of level N is classical (Brzezinski 1983; Lehman 1992 for the ternary-form side;
  Ponomarev). The theorem should be labelled "PROVED (known in substance; packaging new)", not presented as new → D10.
  I could not access these sources.

**Proof defects.**
* D1: the surjectivity step uses "any certificate word w" to get the 2-adic local model. That presupposes ES-five(p),
  the very thing being encoded.
* D6: "≈ p/12 classes" should be ≈ p/16, because the ≈ p/4 points of X₀(2)^ss fall into orbits of size ≤ 4.
  At p = 2521 the count is 166 against p/16 ≈ 158 and p/12 ≈ 210.

### Explicit Gram (§2) — SOUND
Checked symbolically by hand and numerically on 286 words (`review_ce_words.py`). The identities checked:
* trd α = trd β = −2, trd γ = 0; nrd α = tv, nrd β = tu, nrd γ = uv; αβ = tγ;
* i² = −A*, j² = −A, ij + ji = −2;
* ε = −(1 + ij) = −(i + j + tγ), trd ε = 0, nrd ε = tp;
* the trace-zero sublattice has basis (j, −γ, i), whose Gram matrix is exactly adj(G_w) = [[A,u,1],[u,uv,v],[1,v,A*]].
A by-hand derivation: e₃e₂ = −e₂e₃ − 2 gives αβ̄ = −tγ − 2α, hence trd(iȷ̄) = 2, i.e. ⟨i, j⟩ = 1.

### Cor 2.2 (four forms of ES-five) — SOUND (minor wording, D8)
I re-derived every implication.
* (i) ⟹ (iv): 1 − i = −α and 1 − j = −β, so (1 − i)(1 − j) = αβ = tγ; deg i = 1 + trd α + nrd α = tv − 1 = A*.
* (iv) ⟹ (i), divisibility step: (1 + a) + (1 + b) ≡ (1 + a)(1 + b) ≡ 0 (mod t) because ab ≡ 1. Together with
  v_ℓ((1 + a)(1 + b)) ≥ 2k this forces v_ℓ(1 + a), v_ℓ(1 + b) ≥ k, and the argument works for ℓ = 2 as well.
  Brute-force check over t ≤ 60, a, b < 1500 (`scripts/review_ce_divlemma.py`): 0 counterexamples.
* (iv) ⟹ (i), the rest: the embedding is well defined because ⟨i, j | i² = −a, j² = −b, ij + ji = −2⟩ presents a
  quaternion algebra when ab ≠ 1. The images 1, i − 1, j − 1, (i − 1)(j − 1)/t of the ℤ-basis 1, α, β, γ lie in End E.
* Only CHI_FLIP Cor 1.3 (R198: SOUND) is imported.
* The "Reading" (eigenline interpretation for odd ℓ | t) is correct when i, j ≢ ±1 (mod ℓ End E). The degenerate case
  should be mentioned or the claim softened to Assessment (D8).

### Prop 3.1 (θ_L counts trace-zero endomorphisms of p-divisible norm) — SOUND
There is a shorter global proof than the author's. In E⁰-coordinates, H := adj(G) and p(E⁰)^♯ = G·ℤ³.
* G has rank 2 mod p, because v_p(det G) = 1. So H ≡ λww^T (mod p) with λw ≢ 0, and {x : p | x^T H x} = {x : w·x ≡ 0}
  has index p.
* G·ℤ³ also has index p and lies inside that set, since (Gy)^T H (Gy) = p·y^T G y. So the two sets are equal.
* r_L(m) = #{ε : nrd ε = mp} follows.

The author's local proof is also correct. Using this simpler argument would remove the need for the local p-adic forms.

### Cor 3.2 (Frobenius distance) — SOUND-AFTER-REPAIRS (D4)
These parts are correct:
* the factorisation through Frobenius: a supersingular curve has no points of order p, so an isogeny whose degree is
  divisible by p has inseparable degree divisible by p;
* ε = −(1 + ij) has nrd ε = AA* − 1 = tp (checked);
* t = 1 ⟹ the edge is 𝔽_p-rational. ε ∈ End(E, C) with ε² = −p means ε = ±(the Frobenius of an 𝔽_p-model), up to
  Aut E, so C is stable under that Frobenius. Conversely, on the spine the 𝔽_p-Frobenius has trace 0 (p ≥ 5), so
  min L = 1.

Two wording errors:
* (a) "min(L(E, C)) is the least m such that some isogeny E^{(p)} → E of degree m is compatible with C" omits the
  trace-zero condition. An element x = ψπ of the ideal over p with trd x = pk ≠ 0 has m = nrd x/p ≥ pk²/4. Since
  min L ≤ (2p)^{1/3} < p/4 for p ≥ 13, the statement is true for p ≥ 13, but only by this extra argument, which the text
  does not give.
* (b) The middle letter t is *a* Frobenius degree of the edge (e₂ has norm t), so the Frobenius distance min(L) is ≤ t,
  not = t. The reading "certificate edges with small t sit at Frobenius distance t from the spine" should say "≤ t".
  The data show this is not idle. At p = 2521, eight classes of 𝔊⁻ have min L = 1 (spine edges) and none is a
  certificate. The two certificate classes have min L = 2, while their words have t = 15 and t = 44
  (`review_ce_rank.py`).

### Cor 3.3 (spine slice) — SOUND
* Re-derived: (u − 1)(v − 1) = p + 1 and χ = (−(u−1)/p). For p ≡ 1 (8) the symbol is ((u−1)/p), and odd q | p + 1 gives
  (q/p) = (p/q) = (−1/q).
* Recount (`scripts/review_ce_spine.py`, sieve-based): for all 4466 primes p ≡ 1 (8) below 2·10⁵, the direct check
  "some divisor d of p + 1 has (−d/p) = −1" agrees with the criterion, 0 mismatches. The direct check also confirms that
  every p ≢ 1 (8) below 2·10⁵ has a spine certificate.
* Of the 19 552 primes p ≡ 1 (8) below 10⁶, **5013** have no prime factor ≡ 3 (mod 4) in p + 1. Both of the author's
  numbers are reproduced exactly.
* The density remark (≍ (log p)^{−1/2}, a Landau-type count of integers built only from primes ≡ 1 mod 4) is heuristic
  and labelled so. Fine.
