# CONSTRUCTIVE_ES — five-slice ES certificates as Eichler orders / supersingular 2-isogenies (task O199, spark relay T)

Status: checkpoint in progress (O199). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on CHI_FLIP.md (O198, CLAIMED, under review R198: Thm 1.1, Cor 1.3), MODEL_SPECIFIC Thm 3.1, DEDEKIND_ES Thm 4.5,
DIFF_DEEP (supersingular transfer), KUDLA_ES. Scripts `scripts/ce_*` (library `ce_lib.py`: even Clifford orders,
overorders, reduced discriminants, exact arithmetic).

Notation (as in CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, tuv − u − v = n odd; A = tu − 1, A* = tv − 1, AA* = tn + 1;
χ(w) = (−A/n). Path lattice L_w = ℤ³ with Gram G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (det n), classical
(B(e_i, e_j) = G_ij, Q(x) = B(x, x)). C₀(L) = even Clifford order (Gross–Lucianovic: Gorenstein, reduced discriminant
N(Q) = 4·det G). For n = p prime, ES five-slice certificate ⟺ χ(w) = −1 ⟺ C₀(L_w) ⊂ B_{p,∞} (CHI_FLIP Cor 1.3).

## 1. The overorder ladder of C₀(L): Eichler orders of level 2 (PROVED + CERTIFIED)

**Lemma 1.1 (2-adic isotropy test; PROVED, elementary).** An odd unimodular ternary ℤ₂-lattice L ≅ ⟨a₁, a₂, a₃⟩
(a_i ∈ ℤ₂^*) is isotropic ⟺ not all a_i are congruent mod 4 ⟺ Q(x) ≡ 0 (mod 4) for some primitive x. In that case
there are exactly two classes x mod 2L with Q(x) ≡ 0 (mod 4).
*Proof.* Odd unimodular ℤ₂-lattices are diagonalisable. For x primitive with odd-coordinate set S ≠ ∅,
Q(x) ≡ Σ_{i∈S} a_i (mod 4) (odd squares ≡ 1 mod 8; even coordinates contribute 0 mod 4); |S| ∈ {1, 3} gives an odd
value, so Q(x) ≡ 0 (4) ⟺ |S| = 2 with a_i ≢ a_j (4); if the residues mod 4 are not all equal exactly two pairs qualify.
The isotropy criterion depends only on a_i mod 8 (unit square classes) and is a finite Hilbert-symbol check:
CERTIFIED for all 64 triples (`scripts/ce_check_lemma11.py`, 0 failures). ∎

**Theorem 1.2 (the Eichler ladder; PROVED, with CERTIFIED numerics).** Let L be a positive classical ternary lattice of
odd determinant n, Λ = C₀(L) (discrd 4n). Then:
(a) every element of Λ has even reduced trace, and Λ has a unique overorder E(L) of index 2; E(L) has discrd 2n and
Λ = E(L)^{ev} := {x ∈ E(L) : trd x ∈ 2ℤ};
(b) if L ⊗ ℤ₂ is isotropic, E(L) ⊗ ℤ₂ is an Eichler order of level 2 in M₂(ℚ₂), contained in exactly two maximal
orders, namely C₀(L⁺₁), C₀(L⁺₂) for the two overlattices L⁺_i = L + ℤ·x_i/2 of Lemma 1.1 (on which Q is integral,
N(Q|L⁺_i) = n); if L ⊗ ℤ₂ is anisotropic, E(L) ⊗ ℤ₂ is the maximal order of the ramified algebra;
(c) for n = p prime and χ(w) = −1 (L = L_w), **E(L_w) is an Eichler order of level 2 in B_{p,∞}**; for χ(w) = +1,
E(L_w) is an Eichler order of level p in B_{2,∞}.
*Proof.* trd(e_ie_j) = 2B(e_i, e_j) and trd 1 = 2, so trd(Λ) ⊂ 2ℤ. At odd ℓ, overorders of 2-power index change
nothing, so everything is a statement about Λ₂ = C₀(L ⊗ ℤ₂), which depends only on the ℤ₂-isometry class of the
diagonalisable lattice L ⊗ ℤ₂ ≅ ⟨a₁, a₂, a₃⟩, a_i ∈ {1, 3, 5, 7}. Finite check (`scripts/ce_check_thm12.py`, exact
arithmetic on the ℤ-orders C₀(⟨a₁,a₂,a₃⟩), all 64 triples, 0 failures): unique index-2 overorder E, discrd(E) = discrd(Λ)/2,
E contains an element of odd trace (so Λ = E^{ev}, both of index 2 in E), and the 2-power overorders of minimal
discriminant are two of discrd discrd(Λ)/4 (isotropic) resp. E itself (anisotropic). An order of discrd 2 in M₂(ℚ₂)
is hereditary, i.e. Eichler of level 2; in the division algebra discrd 2 is maximal. The two maximal overorders in the
isotropic case are C₀(L⁺_i): L ⊂ L⁺_i gives C₀(L) ⊂ C₀(L⁺_i), and N(Q|L⁺_i) = N(Q|L)/4 = n.
Conceptually Λ₂ = ℤ₂ + J(E₂): for E₂ = [[ℤ₂, ℤ₂], [2ℤ₂, ℤ₂]], ℤ₂ + J(E₂) = {[[a, b], [2c, d]] : a ≡ d (2)} = {x ∈ E₂ : trd x
even}; for the ramified maximal order, ℤ₂ + πO₂ = {trd even} (trd mod π is the trace 𝔽₄ → 𝔽₂). (c) follows from
CHI_FLIP Cor 1.3 (C₀(L_w) ⊂ B_{p,∞} iff χ = −1, else ⊂ B_{2,∞}) and (b): discrd 2p, so Eichler level 2 at 2 inside
B_{p,∞}, resp. maximal at 2 and level p at p inside B_{2,∞}. ∎
CERTIFIED (`scripts/ce_test1.py`, `ce_test2.py`): every word of p ∈ {41, 73, 89, 97, 113} (151 words): unique overorder
of discrd 2p, 2E ⊂ Λ, and #maximal overorders of discrd p = 2 exactly when χ = −1 (72 words), 0 when χ = +1 (79 words).

## 2. The bijection with supersingular 2-isogenies, and the exact ES dictionary

Write 𝔊⁻_p (resp. 𝔊⁺_p) for the set of isometry classes of positive classical ternary lattices of determinant p
anisotropic (resp. isotropic) at p, i.e. with C₀(L) ⊂ B_{p,∞} (resp. ⊂ B_{2,∞}). Each is a single genus (the p-adic class
⟨1, a, pb⟩ is fixed by (−ab/p) = ∓1, the 2-adic class by the determinant and the Hasse invariant via Lemma 1.1).

**Theorem 2.1 (PROVED; CERTIFIED class counts).** L ↦ E(L) is a bijection
𝔊⁻_p ⟷ {isomorphism classes of Eichler orders of level 2 in B_{p,∞}} ⟷ X₀(2)^{ss}(𝔽̄_p) / ⟨Frob_p, w₂⟩,
with inverse E ↦ E^{ev} = C₀(L). Moreover L(E) ≅ (E⁰)^#(p): the dual of the trace-zero lattice E⁰ = {x ∈ E : trd x = 0}
(form nrd, bilinear ⟨x, y⟩ = trd(xȳ)/2), rescaled by p. Likewise 𝔊⁺_p ⟷ Eichler orders of level p in B_{2,∞}.
*Proof.* Injectivity and well-definedness: Thm 1.2(a),(c) (E(L) is canonical, and L ≅ L′ ⟺ C₀(L) ≅ C₀(L′) by
Gross–Lucianovic: twisted-similarity classes of ternary forms ⟷ isomorphism classes of Gorenstein orders; for positive
forms of equal determinant twisted similarity is isometry up to sign). Surjectivity: let E be Eichler of level 2 in
B_{p,∞}; E^{ev} is an order (locally at 2 it is ℤ₂ + J(E₂)), of discrd 4p. Every order of discrd 4p is Gorenstein: its
Gross–Lucianovic form q has N(q) = 4p, and q = c·q′ would give c³ | 4p, so c = 1. Hence E^{ev} = C₀(q) with N(q) = 4p.
Since all Eichler orders of level 2 are locally conjugate, E^{ev} ⊗ ℤ₂ ≅ C₀(L_w ⊗ ℤ₂) for any certificate word w (Thm
1.2(c)), so q ⊗ ℤ₂ is twisted-similar to a classical form; twisted similarity q ↦ u·det(g)⁻¹·q∘g preserves "classical"
(even cross terms), so q is classical with Gram of determinant N/4 = p, positive after a sign; C₀ ⊂ B_{p,∞} gives
anisotropy at p. Then E(L) = E by uniqueness in Thm 1.2(a). The Deuring correspondence sends (E, C), C ⊂ E[2] of order 2,
to End(E, C) = {x ∈ End E : x(C) ⊂ C}, an Eichler order of level 2; every such order arises, and End(E, C) ≅ End(E′, C′)
iff (E′, C′) is in the ⟨Frob_p, w₂⟩-orbit of (E, C) (Frob_p: conjugate data; w₂: (E/C, E[2]/C), the same order seen from
the other endpoint). Finally C₀(L)⁰ = E⁰ (trace-zero elements of E have even trace), and C₀(L)⁰ has Gram adj(G) = p·G⁻¹
in the basis dual to e₁, e₂, e₃ (cofactor computation below), so L ≅ (E⁰)^#(p). ∎
CERTIFIED (`scripts/ce_classes.py` canonical Minkowski forms; `scripts/ce_ss2.py`: supersingular j over 𝔽_{p²}, the three
2-torsion x-coordinates of the canonical model, Vélu for w₂): |𝔊⁻_p| = #(X₀(2)^{ss}/⟨Frob, w₂⟩) for p = 37, 61, 73, 97,
109, 157, 181, 193 (values 4, 6, 7, 9, 9, 14, 15, 15; p ≡ 1 mod 12 so that j = 0, 1728 are ordinary).

**Explicit gram.** For the path lattice, adj(G_w) = [[A, u, 1], [u, uv, v], [1, v, A*]] (A = tu − 1, A* = tv − 1). In C₀(L_w):
α = e₁e₂, β = e₂e₃, γ = e₁e₃ have trd α = trd β = −2, trd γ = 0, nrd α = tv, nrd β = tu, nrd γ = uv, and αβ = tγ.
So i := 1 + α, j := 1 + β are trace zero with i² = −A*, j² = −A, ij + ji = −2 (⟨i, j⟩ = 1), and
C₀(L_w) = ℤ⟨1, α, β, αβ/t⟩.

**Corollary 2.2 (ES five-slice dictionary; PROVED).** For a prime p, TFAE:
(i) p has an ES five-slice certificate (a word w ∈ X_p with χ(w) = −1; MODEL_SPECIFIC Thm 3.1, CHI_FLIP Cor 1.3);
(ii) some class of 𝔊⁻_p has a *path basis*: Gram [[v, −1, 0], [−1, t, −1], [0, −1, u]] with t, u, v ≥ 1;
(iii) some supersingular 2-isogeny (E, C) over 𝔽̄_p has (End(E, C)⁰)^#(p) with a path basis; equivalently End(E, C)⁰ has a
basis of Gram [[A, u, 1], [u, uv, v], [1, v, A*]];
(iv) some supersingular E/𝔽̄_p, some t ≥ 1 and trace-zero i, j ∈ End E satisfy
  ij + ji = −2, deg i · deg j = tp + 1, (1 − i)(1 − j) ∈ t·End E.
*Proof.* (i)⟺(ii): CHI_FLIP Cor 1.3 (any positive path lattice of det p is some L_w, letters ≥ 1 automatic: det > 0
forces t > (u + v)/(uv) > 0 once u, v ≥ 1). (ii)⟺(iii): Thm 2.1. (i)⟹(iv): take a maximal order containing C₀(L_w)
(Thm 1.2(b)), i = 1 + α, j = 1 + β; (1 − i)(1 − j) = αβ = tγ. (iv)⟹(i): put a = deg i, b = deg j. Since
(1 + a)(1 + b) = nrd((1 − i)(1 − j)) ≡ 0 (mod t²) and ab ≡ 1 (mod t), for each ℓ^k ‖ t one gets ℓ^k | 1 + a and
ℓ^k | 1 + b (if x = v_ℓ(1 + a) ≤ y = v_ℓ(1 + b) and x < k, then ℓ^x a′ + ℓ^y b′ ≡ 0 (mod ℓ^k) forces x = y, and then 2x ≥ 2k).
So v := (1 + a)/t, u := (1 + b)/t are integers and (tv − 1)(tu − 1) = tp + 1 gives tuv − u − v = p. The pure quaternions
i, j (non-commuting, since det [[a, 1], [1, b]] = tp ≠ 0) generate B_{p,∞}, and e₁e₂ ↦ i − 1, e₂e₃ ↦ j − 1 extends to an
algebra embedding C₀(L_w) ⊗ ℚ → B_{p,∞} (the structure constants of C₀ are determined by traces, norms and ⟨i, j⟩),
with e₁e₃ ↦ (i − 1)(j − 1)/t ∈ End E. So C₀(L_w) ⊂ End E ⊂ B_{p,∞}, i.e. χ(w) = −1. ∎

*Reading (Assessment).* (iv) is the five-slice analogue of DIFF_DEEP Thm 2.1 (Type II: trace-zero x, y with ⟨x, y⟩ = 1
plus a numerical divisibility); here the extra condition is a **ring condition at level t**: for odd prime ℓ | t,
i and j act on E[ℓ] as involutions (i² = −a ≡ 1) and (1 − i)(1 − j) ≡ 0 (mod ℓ) says that the −1-eigenline of j equals the
+1-eigenline of i: i and j jointly preserve a cyclic subgroup C_ℓ, acting on it by +1 and −1. As always, the quantifier
"∃ E" adds nothing (supersingular transfer): (iv) holds for some E iff a word with χ = −1 exists. The content is the
**shape**: among the |𝔊⁻_p| ≈ p/12 classes (EVIDENCE: 15 at p = 193, 166 at p = 2521), the path classes are the *near-orthogonal*
ones (off-diagonal entries −1, 0, −1), of which there are ≤ |X_p| ≍ log² p on average.

## 3. The middle letter is a Frobenius distance; t = 1 is the spine (PROVED)

**Proposition 3.1.** For an Eichler order E of level 2 in B_{p,∞} and L = L(E) = (E⁰)^#(p):
p(E⁰)^# = {x ∈ E⁰ : p | nrd x}, hence r_L(m) = #{ε ∈ E⁰ : nrd ε = mp} for all m ≥ 1, i.e.
θ_L(q) = Σ_{ε ∈ E⁰, p | nrd ε} q^{nrd(ε)/p}.
*Proof.* Away from p, E⁰ is self-dual up to units (L is unimodular at ℓ ≠ p, including ℓ = 2, and E⁰ ≅ pL^# there). At p,
L_p ≅ ⟨1, a, pb⟩, so E⁰_p ≅ ⟨p, pa, b⟩ (units a, b); there both sides equal {(x, y, z) : p | z}. ∎
CERTIFIED (`scripts/ce_check_prop31.py`): r_L(m) = #{ε : nrd ε = mp} for m ≤ 12 on 456 path lattices, p < 400, 0 failures.

**Corollary 3.2 (Frobenius distance).** A trace-zero ε ∈ End E with p | deg ε factors as ε = ψ ∘ π, π: E → E^{(p)}
Frobenius, ψ: E^{(p)} → E of degree deg(ε)/p (every isogeny of p-divisible degree between supersingular curves factors
through Frobenius). So min(L(E, C)) is the least m such that some isogeny E^{(p)} → E of degree m is compatible with C
(the Frobenius distance of the edge, measured inside the Eichler order). For a certificate word w = (t, u, v):
**ε := −(1 + ij) ∈ C₀(L_w)⁰ has nrd ε = AA* − 1 = tp** (it is the element dual to e₂, ε = −(i + j + tγ)); so the middle
letter t is a Frobenius distance of the certificate edge. In particular **t = 1 ⟺ ε² = −p**: both ends are defined over
𝔽_p (Z[√−p] ⊂ End E ⟺ j(E) ∈ 𝔽_p) and C is 𝔽_p-rational — the *spine* of the 2-isogeny graph — and then
L ≅ ⟨1⟩ ⊥ M with M = [[v − 1, −1], [−1, u − 1]] a binary form of discriminant −4p.

**Corollary 3.3 (the spine slice; PROVED, elementary).** For p ≡ 1 (mod 8), there is a certificate with t = 1 ⟺ p + 1 has a
prime factor q ≡ 3 (mod 4). (Words (1, u, v) ⟺ (u − 1)(v − 1) = p + 1, χ = ((u − 1)/p); for an odd prime q | p + 1,
(q/p) = (p/q) = (−1/q); (2/p) = 1.) For p ≡ 5 (8) (2/p) = −1 and a = 2 always works; p ≡ 3 (4) is trivial (a = 1).
So the spine alone is Mordell-type congruence data plus one divisor event: it misses every p ≡ 1 (8) with
(p + 1)/2 composed of primes ≡ 1 (mod 4) (relative density ≍ (log p)^{−1/2} heuristically; e.g. p = 73: 74 = 2·37 fails
at t = 1, while (2, 4, 11) certifies 73). CERTIFIED (`scripts/ce_spine.py`): criterion = direct divisor check for all
4466 primes p ≡ 1 (8) < 2·10⁵; 5013 of the 19 552 primes p ≡ 1 (8) < 10⁶ have no spine certificate.

*Reading (Assessment).* Certificate edges with small t sit at Frobenius distance t from the spine; those with small A or A*
(e.g. Mordell's A = q ∈ {2, 3, 5, 7}, CHI_FLIP §3.1) sit at the CM points of discriminant −4q, i.e. at the "special
extremal" orders O₀ ∋ √−q used as starting points by Pizer, Ibukiyama, Bröker and KLPT. A certificate is thus an edge
that is simultaneously t-close to the spine and carries CM by −4A, −4A*, −4uv with AA* = tp + 1: three QNR-type
discriminants coupled through one Diophantine identity (the (J)1 CM dictionary, now located on the 2-isogeny graph).

## 4. Deterministic constructions of B_{p,∞}-data versus certificates (reductions, with labels)

Literature used (from memory, statements not re-derived here except where marked): Pizer (1980) explicit maximal orders —
(−1, −p) for p ≡ 3 (4), (−2, −p) for p ≡ 5 (8), and for p ≡ 1 (8) (−p, −q) with an auxiliary **prime q ≡ 3 (4),
(p/q) = −1**; Ibukiyama (1982) orders O(q, r) for primes q ≡ 3 (8) with (p/q) = −1, r² ≡ −p (q); Bröker (2009): a
supersingular j in time Õ(log³ p) under GRH, by finding the least prime q ≡ 3 (4) with (−q/p) = −1 and a root of
H_{−q} mod p; KLPT (2014) and Eisenträger–Hallgren–Lauter–Morrison–Petit (2018) start from such "special extremal" orders
O₀ ⊃ ℤ[√−q]; Kaneko (1989): two non-commuting embedded orders of discriminants d₁, d₂ force d₁d₂ ≥ 4p; Chevyrev–Galbraith
(2014): successive minima of the Gross lattice determine the maximal order. All deterministic constructions need a
quadratic non-residue (unconditionally the least one is only known to be ≪ p^{1/(4√e)+ε}).

**Proposition 4.1 (certificate ⟹ explicit B_{p,∞}-data, deterministic polynomial time; PROVED).** From a word w with
χ(w) = −1 one obtains in time poly(log p), without factoring and without any non-residue search: (a) the Eichler order
E(L_w) of level 2 and two explicit maximal orders C₀(L⁺_{1,2}) of B_{p,∞} (index-2 overlattices: solve Q_w(x) ≡ 0 (mod 4),
Lemma 1.1, and an exact 4×4 HNF); (b) a presentation B_{p,∞} = ℚ⟨i, j⟩, i² = −A*, j² = −A, ij + ji = −2, i.e. (−A*, −tpA*) (orthogonalise
j′ = j − i/A*, nrd j′ = tp/A*; equals CHI_FLIP's (−A*, −vpA*) since (−A*, tv) = (−A*, 1 + A*) = 1); (c) three non-residues A, A*, uv of p (each is −nrd of a trace-zero element of an order of B_{p,∞} prime to
p: indeed (−nrd x/p) ≠ 1 for every x ∈ B⁰_{p,∞} with p ∤ nrd x, since ℚ(x) embeds and p cannot split); (d) the
Frobenius-distance element ε = −(1 + ij), ε² = −tp.
*Converse direction (what is NOT available).* From any explicit maximal order one gets non-residues for free (c), but
not certificates: a certificate edge is a path-shaped class among ≈ p/12, and the known constructions land on edges at the
CM points of the auxiliary q, which are certificates only when the Mordell congruence t₀(q) | q + 1 holds (CHI_FLIP §3.1:
always for q ≤ 7, i.e. exactly the non-□ classes mod 840). EVIDENCE (`scripts/ce_rank2.py`): at p = 2521 (least non-residue
11) the two classes with min(E⁰) = 11 (edges at the CM(−11) curves) are not certificates; the certificates have
min(E⁰) = 29, 58 (A = 29, t = 15; A = 87, t = 44). At p = 1201 (least non-residue 11) the first certificate uses A = 17,
t = 3 | 18.

**Proposition 4.2 (complexity reading; PROVED as an implication, Assessment otherwise).** If for all p some certificate has
t ≤ (log p)^C (EVIDENCE: t_min ≤ 64 for p < 10⁶, DEDEKIND_ES), then with a factoring oracle a certificate — hence an
explicit maximal order of B_{p,∞} and a non-residue — is found deterministically in poly(log p) time (factor tp + 1 for
t ≤ (log p)^C and test divisor pairs A ≡ A* ≡ −1 (mod t)). So a polylog-t form of ES-five would yield deterministic
construction of B_{p,∞} maximal orders (Pizer/Ibukiyama data) relative to factoring — a statement currently known only
under GRH. This is DEDEKIND's complexity reading, now with the quaternionic output made explicit. There is no reduction
in the other direction: a non-residue q (even a small prime one) does not produce a certificate unless t₀(q) | q + 1.
*Equivalence question of the task (answer).* ES-five(p) is equivalent, by explicit polynomial-time maps in both
directions (Cor 2.2, Thm 2.1, and recovery of (t, u, v) from the Gram), to each of: "some Eichler order of level 2 in
B_{p,∞} has a trace-zero basis of Gram [[A, u, 1], [u, uv, v], [1, v, A*]]"; "some supersingular E has trace-zero i, j with
ij + ji = −2, deg i·deg j = tp + 1, (1 − i)(1 − j) ∈ t End E"; "some 2-isogeny lattice is the (negated) intersection lattice
of a length-3 linear plumbing, i.e. bounds a lens space L(p, A) with (A/p) = −1"; "λ(p) ≤ 3" (DEDEKIND, p ≡ 1 mod 8). It is
**not** equivalent to "∃ non-residue", "∃ maximal order" or "∃ supersingular curve" (those hold for all p; the certificate
needs the extra divisor/shape event), and it implies (with a polylog bound) deterministic QNR-finding modulo factoring.
