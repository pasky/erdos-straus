# R199 — hostile review of CONSTRUCTIVE_ES.md (O199)

Reviewer: R199 side agent. Document reviewed: CONSTRUCTIVE_ES.md as merged from side-agent/constructive-es.
From-scratch scripts: scripts/review_ce_*.py (own Clifford/quaternion arithmetic, own class enumeration, own X₀(2) count).
No quaternion-arithmetic literature is present in sources/; all literature statements were checked from memory only
and are flagged as such.

**Repairs applied** (author quiet since the 18:08 checkpoint report): I made the necessary repairs for D1, D2, D3, D4,
D5, D6, D9 (5.1 part), D10 and D11 directly in CONSTRUCTIVE_ES.md, each marked "(R199 repair)". D7, D8 and the 5.4
wording are left to the author. AGENT_REPORT_O199.md is not edited; its "three non-residues A, A*, uv", "poly(log p)"
(Prop 4.2) and "not among the smallest orders" lines inherit D3, D5 and D2.

## Summary verdicts

| Claim | Verdict | Notes |
|---|---|---|
| Lemma 1.1 | **SOUND** | brute-force re-check on 64 triples |
| Thm 1.2 (Eichler ladder) | **SOUND** (minor wording D7) | full 2-power overorder enumeration, 64 triples + 286 words + 49 square words |
| Explicit Gram (§2) | **SOUND** | |
| Thm 2.1 (bijection) | **SOUND-AFTER-REPAIRS** (D1 hidden ES-five hypothesis in surjectivity; D10 attribution) | class counts re-CERTIFIED independently for 35 primes (all 5 ≤ p ≤ 139, plus 157, 181, 193) |
| Cor 2.2 (four forms) | **SOUND** (D8 minor) | |
| Prop 3.1 | **SOUND** | shorter global proof given |
| Cor 3.2 | **SOUND-AFTER-REPAIRS** (D4: trace-zero; distance ≤ t) | |
| Cor 3.3 + counts | **SOUND** | 4466 / 5013 / 19 552 reproduced |
| Prop 4.1 | **SOUND-AFTER-REPAIRS** (D3 non-residue sign; D2 selective EVIDENCE) | |
| Prop 4.2 | **GAP → repaired** (D5: p^{o(1)}, not poly(log p)) | |
| 5.1 | **SOUND**; line-graph remark is unproved (D9) | |
| 5.2 | **EVIDENCE confirmed** (spectra reproduced); consequence SOUND after D11 | JL explanation plausible, from memory |
| 5.3 | Assessment, correctly labelled (D6) | |
| 5.4 | **SOUND** (wording, D9) | |
| 5.5 | counts reproduced; **bold conclusion false at 3 of 5 primes** (D2, MAJOR) | |
| Literature (§4) | acceptable as "from memory"; Chevyrev–Galbraith vs Goren–Love attribution doubtful | none used in proofs |

There are no FATAL defects. The MAJOR defects are D1 (repairable hidden hypothesis), D2 (misread evidence) and
D5 (complexity overclaim). The headline dictionary (Thm 1.2, Thm 2.1, Cor 2.2) stands. ES is not solved, and none of
the claims says otherwise.

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

### Thm 1.2 (Eichler ladder) — SOUND (minor wording D7)
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
| **every** prime 5 ≤ p ≤ 139 (32 primes, 26 of them ≢ 1 mod 12) | |𝔊⁻_p| = #orbits in all cases, including p where j = 0 or 1728 is supersingular (X₀(2) has an elliptic point over 1728) |
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

### Prop 4.1 (certificate ⟹ explicit B_{p,∞}-data) — SOUND-AFTER-REPAIRS (D3)
* (a), (b), (d): correct and deterministic.
  - Finding E(L_w) means testing 15 candidates; finding L⁺_{1,2} means testing 7 vectors x mod 2. Both are trivially
    polynomial.
  - For (b) I checked j′ = j − i/A*, nrd j′ = tp/A*, and (−A*, tv) = (−A*, 1 + A*) = 1.
* (c) is wrong as worded. Here −A, −A*, −uv are the non-residues, since (−nrd x / p) = −1. These coincide with
  A, A*, uv as non-residues only for p ≡ 1 (mod 4); for p ≡ 3 (mod 4), A is a residue. The same slip appears in
  Prop 4.2 ("lens space L(p, A) with (A/p) = −1"; the dictionary actually gives (−A/p) = −1).
  Also, p ∤ uv should be stated; it is easy, since p | u forces v(tu − 1) = p + u ≡ 0 (mod p) and leads to a size
  contradiction.
* The EVIDENCE line is selective. At p = 2521 the two classes with min(E⁰) = 11 are indeed non-certificates
  (reproduced). But at the other hard primes 1009, 1129 and 1801 (all with least non-residue 11) one of the two
  min(E⁰) = 11 classes **is** a certificate (`review_ce_rank.py`).
  Example: p = 1009 has the Mordell-type word (4, 3, 92), with A = 11, t = 4 | 12 = q + 1.
  This is consistent with the author's own "t₀(q) | q + 1" criterion, but it contradicts §5.5 (see D2).

### Prop 4.2 (polylog-t ES-five ⟹ deterministic maximal orders / QNR modulo factoring) — GAP (D5)
* The implication runs: factor tp + 1 for each t ≤ (log p)^C, then enumerate divisor pairs. Enumerating the divisor
  pairs costs d(tp + 1), which in the worst case is exp((log 2 + o(1)) log p / log log p). That is p^{o(1)}, not
  poly(log p).
* Under the stated hypothesis the honest conclusion is a deterministic p^{o(1)}-time algorithm relative to a factoring
  oracle. That would still beat the unconditional Burgess-type deterministic bound, but it is not "poly(log p)".
  Getting poly(log p) needs a stronger hypothesis, e.g. a certificate whose A is reachable within polylog divisor tests.
* The "equivalence question" paragraph inherits the same error ("polynomial-time maps in both directions" is fine; the
  QNR-complexity clause is not).
* "Known only under GRH" (deterministic maximal orders, via Pizer's data plus a bound on the least prime q) is
  correct to my knowledge, from memory.

### Literature statements in §4 (all from memory; no sources available) — acceptable as flagged
These match my recollection:
* Pizer 1980: (−1, −p), (−2, −p), and for p ≡ 1 (8) (−p, −q) with q ≡ 3 (4), (p/q) = −1;
* Ibukiyama 1982: q ≡ 3 (8), (p/q) = −1 ⟺ (−p/q) = 1, r² ≡ −p (q);
* Bröker 2009: Õ(log³ p) under GRH, with (−q/p) = (p/q) for q ≡ 3 (4), consistent with Pizer;
* KLPT 2014 and EHLMP 2018: special extremal O₀ ∋ √−q;
* Kaneko 1989: d₁d₂ ≥ 4p;
* Burgess-type bound p^{1/(4√e)+ε}.

Two caveats:
* The Chevyrev–Galbraith attribution is uncertain. My recollection is that they *conjectured* (with evidence) that
  the successive minima determine the order, and that this was later proved by Goren–Love. Either confirm the
  attribution or reword as "(Chevyrev–Galbraith; Goren–Love)".
* None of these statements is used in a proof, so mis-recollection would not break any PROVED claim.

### 5.1 (lattice operations preserve χ) — SOUND; one embedded claim GAP → D9
* Sub/super-lattices, duals and rescalings preserve the rational similarity class of L ⊗ ℚ. Hence they preserve
  C₀ ⊗ ℚ and with it the χ-side. This is trivial and correct.
* The parenthetical "Kneser 2-neighbour graph on 𝔊⁻_p (= the line graph of the supersingular 2-isogeny graph, via Thm
  2.1 …)" is asserted, not proved. Two problems:
  - the vertices of 𝔊⁻_p are ⟨Frob, w₂⟩-*orbits* of edges, so at best this is a quotient of a line graph, and
    quotients do not commute with taking line graphs in general (multiplicities, loops, Frobenius-fixed edges);
  - the 2-neighbour notion for odd lattices is non-standard and has to be defined (it is, implicitly, via L⁺).
* Label it Assessment, or prove it, including how multiplicities behave.

### 5.2 (spectral disjointness) — EVIDENCE confirmed; explanation plausible (from memory); consequence SOUND-AFTER-REPAIRS (D11)
**Independent recomputation** (`scripts/review_ce_hecke.py`): my own Kneser ℓ-neighbours on my own canonical classes,
with exact characteristic polynomials (sympy).
* At p = 97, 193, 241, 313, 409, the T₃ characteristic polynomials of 𝔊⁺ and 𝔊⁻ have gcd exactly X − 4.
* At p = 97 and 193, the T₅ characteristic polynomials have gcd X − 6.
* The root ℓ + 1 is simple on both sides. For example, at p = 97 the 𝔊⁻ polynomial factors as
  (X−4)(X⁴−5X²−X+4)(X⁴−2X³−9X²+18X+1).
* Every number in the claim is reproduced.

**JL / Atkin–Lehner explanation.** This is consistent with my recollection, not re-derived. For B_{p,∞} the Brandt
involution coming from the ideal over p is −w_p (Gross), while for an unramified level prime it is +w_ℓ. So
* 𝔊⁻ sees newforms of level 2p with (w₂, w_p) = (+, −), plus level-p forms with w_p = −1;
* 𝔊⁺ sees newforms with (w₂, w_p) = (−, +).

Consistency check at p = 97:
* dim S₂^new(194) = 9 and dim S₂(97) = 7;
* the cuspidal dimensions are |𝔊⁺| − 1 = 5 and |𝔊⁻| − 1 = 8;
* the 𝔊⁻ cuspidal factor splits into two quartics.
All of this fits, although I did not verify the eigenform signs.

**Suggested strengthening.** Given these JL facts, strong multiplicity one already shows that the two modules share no
*full*-Hecke cusp eigen-system for **every** p, since newforms of level 2p with different AL signs, or of different
levels, have different eigenvalue systems. So "every map equivariant for all T_ℓ, ℓ ∤ 2p, factors through the constants"
is PROVED-modulo-JL-citation for all p. The single-T₃ statement needs the computed spectra.

**Needed hypothesis in "Consequence (PROVED, given the computed spectra)".** The step requires that the eigenvalue ℓ + 1
is simple on both sides. This is true: Ramanujan–Deligne gives |a_ℓ| ≤ 2√ℓ < ℓ + 1 for cusp forms, and my
characteristic polynomials confirm it. But it has to be said; it is D11. With that added, the linear-algebra deduction
is correct: T_ℓ is self-adjoint for the mass inner product, so constants map to constants and the cuspidal part maps to 0.

### 5.3 (shape screen) — Assessment, correctly labelled; D6 (p/12 → p/16) applies.

### 5.4 (T1 control) — SOUND
* `scripts/review_ce_t1.py` uses exact 2-power overorder enumeration on all 49 words of n = 9, 25, 49. Every C₀(L_w)
  has discrd 4n, a unique index-2 overorder of discrd 2n, and no larger 2-power overorder. 0 failures.
* The "no 𝔊⁻_{m²}" sentence holds for path lattices: CHI_FLIP gives χ ≡ +1 at squares.
* Note, though, that non-path lattices of determinant m² *can* have C₀ ramified at odd ℓ | m. Example: ⟨1, 3, 3⟩ at
  n = 9, where C₀ ⊂ B_{3,∞}. The sentence "the whole supersingular/2-isogeny picture is empty at odd squares" is true
  only for the χ-dictionary of path words. Reword (MINOR, folded into D9).

### 5.5 (numerics) — counts reproduced; bold conclusion false at 3 of 5 primes (MAJOR, D2)
`scripts/review_ce_rank.py` reproduces the counts:
* |𝔊⁻_p| = 69, 76, 82, 122, 166 at the five hard primes, with 5, 8, 5, 8, 2 path classes;
* 4–10 path classes out of 7–44 classes for p ≡ 1 (24) ≤ 601.

The ranks are reported **0-indexed** ("number of classes strictly ahead", ties broken arbitrarily). By ordinary
1-indexed rank, the first path class by min(E⁰) is at position 2, 2, 4, 2, 11. Moreover:
* at p = 1009, 1129 and 1801 the first path class has min(E⁰) = 11 = n_p, tied for the *smallest possible* value;
* at those three primes one of the two CM(−11) edges is a certificate.

So the bold conclusion "certificates are not among the 'smallest' orders at hard primes" is false at 3 of the 5 hard
primes. It holds only at 1201 (min(E⁰) values 11, 11, 13, then 17, which is the path class) and at 2521.

The min(L) ranking is dominated by ties. For example, at 2521 eight classes have min L = 1, and they cannot be
certificates there by Cor 3.3, because 2522 = 2·13·97.

The data actually support this narrower statement: the CM(−n_p) edge is a certificate exactly when the Mordell-type
congruence for q = n_p holds (t₀(q) | q + 1), which is a residue condition on p. That is what Prop 4.1 already says.

## Numbered defects

**D1 (MAJOR; repair is easy) — Thm 2.1, surjectivity step: a hidden hypothesis.**
"E^{ev} ⊗ ℤ₂ ≅ C₀(L_w ⊗ ℤ₂) for any certificate word w" presupposes a certificate at p, i.e. ES-five(p). As written,
the bijection, and the (iii) ⟹ (ii) direction of Cor 2.2 that relies on it, is proved only at primes that already have
a certificate.
*Repair:* use the purely local Thm 1.2(b). For any isotropic odd unimodular ℤ₂-lattice, e.g. ⟨1, 1, 3⟩, the order
E(⟨1,1,3⟩) ⊗ ℤ₂ is Eichler of level 2, and C₀(⟨1,1,3⟩) ⊗ ℤ₂ is its even-trace part. All level-2 Eichler orders of
M₂(ℚ₂) are conjugate, so E^{ev} ⊗ ℤ₂ ≅ C₀(⟨1,1,3⟩ ⊗ ℤ₂). The rest of the argument is unchanged.

**D2 (MAJOR) — §5.5, the Summary point (4), the report's EVIDENCE line and Prop 4.1's EVIDENCE: misreading of own data.**
* At 1009, 1129 and 1801 a certificate class attains min(E⁰) = n_p = 11, the smallest value present.
* The ranks are 0-indexed.
* "Certificates are not among the smallest orders at hard primes" holds only at 1201 and 2521.

*Repair:* restate as follows. "At 3 of the 5 hard primes a certificate sits at a CM(−n_p) edge, namely when the
Mordell-type congruence for q = n_p holds (e.g. 1009: word (4, 3, 92), A = 11). At 1201 and 2521 it does not, and there
the first certificate class is 4th resp. 11th by min(E⁰). Whether a privileged order is a certificate is decided by the
congruence data of its CM discriminant, not by its size." Also state that the ranks are 0-indexed, or convert them.

**D3 (MINOR) — Prop 4.1(c), Prop 4.2 (lens space).**
The non-residues are −A, −A*, −uv. They equal A, A*, uv only for p ≡ 1 (4).
*Repair:* write "(−A/p) = (−A*/p) = (−uv/p) = −1", note p ∤ uv, and change "(A/p) = −1" to "(−A/p) = −1".

**D4 (MINOR) — Cor 3.2 / reading after Cor 3.3.**
* Add "trace-zero" to the description of min L, or add the remark that non-trace-zero x have nrd x / p ≥ p/4 > min L
  for p ≥ 13.
* Replace "Frobenius distance t" by "Frobenius distance ≤ t (t is the degree of one compatible Frobenius-factor)".
  Counter-data: at p = 2521 the certificates have min L = 2 but t = 15 and t = 44.

**D5 (MAJOR) — Prop 4.2: complexity overclaim.**
Enumerating the divisors of tp + 1 is not poly(log p); d(n) can be exp(c log n / log log n).
*Repair:* replace "poly(log p)" by "p^{o(1)} (more precisely (log p)^{O(1)}·max_{t ≤ (log p)^C} d(tp + 1))". Make the
same change in the "Equivalence question" paragraph and in the Summary (2) / report wording.

**D6 (MINOR) — "≈ p/12 classes" (§2 Reading, §5.3).**
The correct size is ≈ p/16: there are ≈ p/4 points of X₀(2)^ss, in orbits of size ≤ 4. At p = 2521, |𝔊⁻| = 166.

**D7 (MINOR) — Thm 1.2(b) wording.**
* L⁺_i is integral only as a quadratic form: B(x_i/2, e_k) ∈ ½ℤ. Say "Q-integral (non-classical)".
* State that C₀(L⁺₁) ≠ C₀(L⁺₂). I verified this on all 48 isotropic triples.

**D8 (MINOR) — Cor 2.2 Reading (eigenlines).**
Add "when i, j ≢ ±1 (mod ℓ End E)", or label the paragraph Assessment.

**D9 (MINOR) — 5.1 "= the line graph of the supersingular 2-isogeny graph" (unproved; quotient issues) and 5.4 "empty at
odd squares" (true only for the path-word dictionary).**
*Repair:* label 5.1's claim as Assessment, and qualify 5.4.

**D10 (MINOR) — Thm 2.1 attribution and range.**
* The bijection is known in substance (Brzezinski; Lehman; Gross–Lucianovic; Ponomarev). The document should say so,
  not only the report.
* The certified class-count range can be extended: R199 checked all primes 5 ≤ p ≤ 139 plus the author's eight; the
  restriction to p ≡ 1 (mod 12) is unnecessary with the Hauptmodul count.

**D11 (MINOR) — 5.2 "Consequence".**
Add the needed step: ℓ + 1 is a simple eigenvalue on both sides. This follows from Ramanujan–Deligne, or directly from
the computed characteristic polynomials.
Optionally add the full-Hecke version, which holds for all p modulo the JL/AL citation.
