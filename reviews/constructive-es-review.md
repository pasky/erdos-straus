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
