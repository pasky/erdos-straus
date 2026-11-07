# Z63_EUCLID — an arithmetic index on the complex of all Euclidean paths (board item astra-2)

**ES is OPEN; nothing here proves or disproves it, (MS), (MS-U₇), SQ₅ or (S).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Scripts `scripts/z63_euclid_*`, data
`data/z63/euclid/`. Brief: `z52bbriefs/z63_lanes.md` §EUCLID (+ z58 common rules, z53 depth brief).

*Status: final (checkpoint 1 committed with kill test KE1 before any computation; internal hostile review done, §10,
fixes applied). KE1 was not evaluated exactly as registered; the post-hoc high-loop independence was observed (§4).
Verdict: **NARROWED**, with a precise missing lemma (§6). No HOT LEAD.*

Notation. HJ = negative (Hirzebruch–Jung) continued fraction n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A);
L_r(n) = {A ∈ (0,n) : gcd(A,n) = 1, r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1
(DEDEKIND_ES Lemma 1.1). S = [[0,−1],[1,0]], T = [[1,1],[0,1]], S(b) := T^b S = [[b,−1],[1,0]]. Γ := Γ₀(n)/±1.
χ_n(γ) := (d/n) (Jacobi) for γ = [[a,b],[c,d]] ∈ Γ₀(n).

## 0. Mandatory falsifier table (for the target (S) and the homological index EUC-H of §2; re-stated at the end)

| screen | behaviour | where primality / non-squareness enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1 (trivial character), so the index is identically 0 at squares and no length-3 loop carries index — T1 is built in (DEDEKIND Prop 3.1). | In the non-triviality of the class χ_n ∈ H¹(Γ₀(n)/±1; F₂) (n ≡ 1 (4)): χ_n ≠ 0 ⟺ n not a square. This is the *only* place. |
| **F2 C-even / numerator 8** | The index is supported on *all* χ = −1 length-3 words (five DEDEKIND slices: 4 ∣ t, u, v, A or A*), not on the (★) line or its C-even half. (S) holds at the 12 R₈ zeros near 10¹⁰ (explicit words, §7). An argument working "verbatim on the C-even sub-line" is not what EUC-H proposes. | — (no C-parity input; the slice union is used). |
| **F3 composites** | χ_n is a non-trivial character of Γ₀(n) at every odd non-square n, so EUC-H treats composites like primes. This is consistent with the data: (S) has **no known counterexample** (0 violations among non-square n ≡ 1 (4) < 10⁹, HJ_DEEP EVIDENCE 3.1 + R174); the lone SQ₅ exception 105 has L₃(105) = ∅ (a (W)-failure, not an (S)-failure). The 285 (★)-zero composites and Z₇ all satisfy (S). | Not needed for (S) (Assessment: (S) is plausibly true for all non-squares); needed only for (W) at primes, which holds for every prime p ≡ 1 (4), p ≠ 5 (bsG_primes_trivial: words (2,2,(p+2)/3) for p ≡ 1 (3), (3,(p+7)/12,4) for p ≡ 5 (12); L₃(5) = ∅). |
| **F4 known zeros** | The 14 (★)-zero primes and the 38 𝔊*-zero primes satisfy (S) (HJ_DEEP/R174 census to 10⁹); the 12 R₈ zeros do too (explicit words, §7). (S) has no known zero, prime or composite. | — |

## 1. Precise statements attacked

* **(S) (CONJECTURE; HJ_DEEP §3).** For every non-square n ≡ 1 (mod 4) with L₃(n) ≠ ∅ there is A ∈ L₃(n) with (A/n) = −1.
  At primes p ≡ 1 (4), p > 5, (S)(p) ⟹ interior five-slice ES(p) (DEDEKIND Thm 4.5) ⟹ ES(p); (W)(p), i.e. L₃(p) ≠ ∅, is
  automatic there (bsG_primes_trivial; L₃(5) = ∅).
  (S) is weaker than (MS) (it uses five slices, of which (★) is one) and sign-only: "T1 is the only obstruction for words".
* **(EUC) — the lane's question.** Construct a finite complex K(n) out of *all* Euclidean (HJ/Farey) paths of n, a cochain/
  index with a computable total, such that only length-3 χ = −1 cells can carry index outside a known part, and prove the
  total non-zero at every non-square n ≡ 1 (4) (or every large prime p ≡ 1 (24)).
* **Why not already closed.** Closed: local-invariant indices are cell sums (BRAINSTORM/s5_reciprocity_forcing Prop R);
  conjugacy-type weights of a single word depend only on (t, u+v) (Z62_PARITY Thm R); finite feature dictionaries
  (Z62_PARITY KT1/H2/H3, DEDEKIND C5); sign-reversing injections (HJ_DEEP C5: 1 385 counterexamples). **Not closed:** weights
  coming from *relations between different words* (Lemma P0 (b)/(d): weights depending on neighbouring non-certificate
  cells), i.e. an index living in the homology of a complex in which all Euclidean paths of n are glued together.
  Z62_PARITY §4.5 lists "relations between words" as open. EUC-H below is the canonical such complex.

## 2. The canonical complex: all Euclidean paths of n glued in the level-n (orbifold) Farey complex

**Lemma E1 (dictionary; PROVED, elementary).** Let n ≥ 3 be odd, A ∈ (0,n) coprime to n, n/A = [[b₁,…,b_r]]. Then
γ_A := S·S(b₁)S(b₂)⋯S(b_r) lies in Γ₀(n), and its lower-right entry is ≡ −A⁻¹ (mod n). Hence, for n ≡ 1 (mod 4),
**χ_n(γ_A) = (A/n).** The map γ ↦ χ_n(γ) is a homomorphism Γ₀(n) → {±1} trivial on −I (n ≡ 1 (4)), i.e. a class
χ_n ∈ H¹(Γ; F₂), and χ_n = 0 ⟺ n is a square.
*Proof.* M := S(b₁)⋯S(b_r) = [[K(b₁..b_r), −K(b₁..b_{r−1})],[K(b₂..b_r), −K(b₂..b_{r−1})]] = [[n, −A′],[A, −A″]] with
A′ := K(b₁..b_{r−1}); det M = 1 gives A·A′ ≡ 1 (mod n). S·M = [[−A, A″],[n, −A′]] has lower-left n ≡ 0 and lower-right
−A′ ≡ −A⁻¹. (−A⁻¹/n) = (−1/n)(A/n) = (A/n). The lower-right entry mod n of a product of elements of Γ₀(n) is the
product of the lower-right entries, and (·/n) is multiplicative, so χ_n is a homomorphism; it is trivial iff (d/n) = 1 for all
units d iff n is a square. ∎

So the **Euclidean path complex of n** is the presentation complex of Γ₀(n)/±1 obtained from its Schreier (coset) graph in
PSL₂(ℤ) = ⟨S, T⟩ (vertices P¹(ℤ/n), edges the S- and T-moves, 2-cells the relators S² and (ST)³ at every coset). Up to
the orbifold points this is the Farey tessellation modulo Γ₀(n). Its H₁(·; F₂) is the *group* homology
H₁(Γ₀(n)/±1; F₂) = F₂^{e₂ + 2g + c − 1}, so order-2 elliptic classes are retained. Each Euclidean path of n/A becomes a
closed walk [γ_A] (read the letters S T^{b₁} S ⋯ T^{b_r} S from the base coset), and the index of a loop is ⟨χ_n, [γ_A]⟩.
All p − 1 paths of a prime p live in one complex with H₁ of dimension ≈ p/6.
*Total index.* The integer count Σ_A [χ_n(γ_A) = −1] = φ(n)/2·[n ≠ □] is known and T1-native. However, its reduction
mod 2 is 0 at every prime p ≡ 1 (4), so it is **not** a non-zero total for the F₂-index studied below. Integer balance
information of this kind is not imposed in Prop E3 (§5).
For non-square n ≡ 1 (4) with L₃(n) ≠ ∅: (S)(n) ⟺ **χ_n does not annihilate V₃(n) := span{[γ_A] : A ∈ L₃(n)}** ⊂
H₁(Γ; F₂). (At n = 105, L₃ = ∅: (S) is vacuous and V₃ = 0.)
*Attribution.* All of this is classical: the continued-fraction/matrix dictionary, Schreier graphs and modular symbols
(Manin, 1972: the CF expansion writes a path as a sum of Manin symbols), the quadratic character of Γ₀(n) through the
lower-right entry, and the Eisenstein-type Hecke eigenrelation (cf. Mazur, *Modular curves and the Eisenstein ideal*,
1977; cited from memory, not checked here). Only the application to the ES certificate set is new.

**What a Euclidean index (Lemma P0 (d)) would be here.** An F₂-relation in H₁(Γ; F₂)
  Σ_{A ∈ L₃(n)} c_A [γ_A] = κ + Σ_j d_j [γ_{B_j}]  (κ a canonical class, B_j in an explicit "known" set with computable symbols)
gives Σ_{A ∈ L₃} c_A [(A/n) = −1] ≡ χ_n(κ) + Σ_j d_j[(B_j/n) = −1] (mod 2); if the right side is provably 1, a certificate
exists. The weights c_A are *not* local: they solve a linear system in the whole complex (they depend on all other paths).
This is exactly the escape left open by Prop R / Thm R. Such a relation, produced uniformly in n, **is** the astra-2 index.

**Lemma E2 (Hecke eigenrelation; PROVED).** For a prime ℓ ∤ n (n ≡ 1 (4)), T_ℓ* χ_n = (ℓ + 1)·χ_n in H¹(Γ; F₂). In
particular, for odd ℓ, χ_n vanishes on T_ℓ(H₁(Γ; F₂)): every odd Hecke image has χ = 0. As known data these images
only add a subspace on which χ vanishes; their combined effect with the other known classes is computed in §4.2.
(For ℓ = 2, χ∘T₂ = χ holds for every such n, whatever (2/n) is.)
*Proof.* With ΓαΓ = ⊔_i Γα_i, α = diag(1,ℓ), α_i ∈ {[[1,k],[0,ℓ]] : 0 ≤ k < ℓ} ∪ {[[ℓ,0],[0,1]]}, (T_ℓφ)(γ) = Σ_i φ(α_iγα_{σ(i)}⁻¹).
For γ = [[a,b],[c,d]] with n ∣ c and α_i = [[x_i,y_i],[0,z_i]], the lower-right entry of α_iγα_j⁻¹ is (z_i x_j d − z_i y_j c)/ℓ ≡
d·z_i x_j/ℓ (mod n). The factor z_i x_{σ(i)}/ℓ is 1 unless exactly one of i, σ(i) is the coset [[ℓ,0],[0,1]]; σ is a bijection, so
either all factors are 1 or exactly one is ℓ and one is ℓ⁻¹. Writing χ additively, (T_ℓχ)(γ) = (ℓ+1)χ(γ) + χ(ℓ) + χ(ℓ⁻¹) =
(ℓ+1)χ(γ) in F₂. For ℓ odd this is 0. ∎

## 3. PRE-REGISTERED KILL TEST KE1 (registered at checkpoint 1, before any computation)

Script `scripts/z63_euclid_h1.py` (to be written): for each n in the test set, build the Schreier graph of Γ₀(n) on
P¹(ℤ/n) under right multiplication by S, T; compute H := H₁(Γ₀(n)/±1; F₂) by Reidemeister–Schreier (generators = non-tree
edges, relations from S² and (ST)³ at every coset); compute the classes [γ_A] by tracing the words S T^{b₁}S ⋯ T^{b_r}S; verify
Lemma E1 (lower-right entry, χ = (A/n)) on every computed word.
Sets: 𝒮(n) = {[γ_A] : A ∈ L₃(n)} (short loops; reversal pairs A, A* kept separately), 𝒦(n) = known part =
{[γ_B] : B ∈ L₁ ∪ L₂(n)} ∪ {[γ_B] : 1 ≤ B ≤ 30, gcd(B,n) = 1} ∪ {classes of the parabolic T and of the elliptic generators}.
Test set: all primes p ≡ 1 (24), p ≤ 3000 (main population); controls: odd squares ≤ 3025; Z₇ ∩ [1, 4545] = {105, 1465, 3865,
4545}; the (★)-zero primes 409, 577; composites from `composite_zeros_le8e6.txt` ≤ 3000.
Statistic: the relation space Rel(n) := {(c, d) : Σ c_A [γ_A] = Σ d_B [κ_B]} restricted to relations with c ≠ 0, modulo
*forced* relations. "Forced" is fixed now: relations that hold identically for all n in the population as a formal consequence
of the words (to be listed explicitly if any appear, e.g. [γ_A] = [γ_{A*}] if reversal acts trivially mod 2).
**KE1 kill (EUC-H is DEAD as an index mechanism in this complex) if:** at ≥ 90 % of the main-population primes, every relation
with c ≠ 0 is forced, i.e. dim(span 𝒮 ∩ span 𝒦) and the internal rank deficit of 𝒮 are fully explained by forced relations
(the short loops are otherwise F₂-independent of each other and of the known part). Then no relative-boundary identity
supported on short loops plus a known part exists at those n, and any index must give non-zero weight to loops with
*unknown* (uncomputed) χ-values, i.e. it is not an index with computable total. **KE1 survives** if non-forced relations
linking 𝒮 to 𝒦 occur at > 10 % of primes; then they are examined for a uniform law (and checked at squares/Z₇).
Secondary statistic (recorded, not a kill): whether χ_n restricted to span 𝒮 is determined by χ_n on span 𝒦 at any n.

## 4. Computations

### 4.1 KE1 — generic Euclidean loops are linearly free (post-hoc form; the registered form was not evaluated cleanly)

**Script** `scripts/z63_euclid_h1.py` (pure Python, < 1 min per run). Built-in assertions, all passing on every input:
(a) Lemma E1 at matrix level (lower-left ≡ 0, lower-right·A ≡ −1 (mod n), χ = (A/n));
(b) coset count = [PSL₂(ℤ) : Γ₀(n)/±1] = n∏_{q|n}(1 + 1/q), using the P¹(ℤ/n) normal form (g, d·(c/g)⁻¹ mod n/g)
with g = gcd(c, n). The reviewer also checked this normal form against brute unit-orbit enumeration for all odd n ≤ 101;
(c) dim H₁(Γ₀(n)/±1; F₂) = e₂ + 2g + c − 1 from the classical formulas for μ, e₂, e₃, c, g;
(d) a cocycle representative of χ_n computed independently from exact coset matrices (χ of every Schreier generator
R_x·s·R_{xs}⁻¹ ∈ Γ₀(n)), which vanishes on every relator and reproduces (A/n) on every computed loop.
**Height.** For A ∈ (ℤ/n)^*, h(A) := min{max(a, b) : A ≡ ±a·b⁻¹ (mod n), 1 ≤ a, b, gcd(b, n) = 1}. For a length-3 word
with v a unit mod n (always at primes), n = vA − u gives A ≡ u·v⁻¹, so h(A) ≤ max(u, v). "Low" short loops: h(A) ≤ HIGH;
"high" (generic): h(A) > HIGH.
**Known part 𝒦.** Cusp classes (T-cycles), order-2 and order-3 elliptic classes, and the loops of every A ≤ BMAX and of
every A with HJ length ≤ 2. 𝒦 and the short set are defined independently, so a length-3 loop with A ≤ BMAX is in both.
*Review fix F1:* the first version omitted such loops from 𝒦; all data and counts below are regenerated.

**Runs.** Commands: `BMAX=b HIGH=h python3 scripts/z63_euclid_h1.py pop 20000` and the control list; data in
`data/z63/euclid/ke1_*.tsv`. Columns: rank data, the number of relations involving high loops (nhighrels), and the number
of "index relations" (nidxrels): relations whose known side has odd χ, which force an odd number of χ = −1 short loops.

| population | inputs | short loops | high loops | rank increase from high loops | inputs with a relation involving a high loop | inputs with an index relation |
|---|---|---|---|---|---|---|
| primes p ≡ 1 (24) ≤ 2·10⁴, BMAX 30, HIGH 60 | 267 | 12 764 | 2 584 | **2 584** | **0** | 262 |
| same, BMAX 10, HIGH 20 | 267 | 12 764 | 7 244 | **7 244** | **0** | 214 |
| controls, BMAX 30 / 10 | 108 | 1 966 | 366 / 1 022 | 366 / 1 022 | 0 / 0 | 31 / 18 |

Controls: the (★)-zero primes 409, 577, 5569, 9601; Z₇ ∩ [1, 12145] = {105, 1465, 3865, 4545, 10305, 12145}; the first 40
non-square composite R-zeros (57 … 12681, from `composite_zeros_le8e6.txt`); all 58 odd squares 9 … 13689. That is 102
distinct levels; 105, 1465, 3865, 4545, 10305, 12145 are listed twice. dim H₁ ≈ 0.167–0.178·p at the primes.

**Reading (CERTIFIED for the listed inputs).** At every input, the classes of the high short loops are linearly
independent modulo span(𝒦 ∪ low short loops) in H₁(Γ₀(n)/±1; F₂). No F₂-relation involves a generic length-3
Euclidean loop together with 𝒦, the low loops or the other high loops. Squares, composites, Z₇ and the (★)-zero primes
show the same independence behaviour as primes. At squares χ ≡ 0, so relations carry no sign there.
*Null model (M5).* This is what random vectors would do. At p = 2953 (BMAX 10) the quotient H₁/span(𝒦 ∪ low) has
dimension 493 − 15 − 17 = 461, and only 16 high vectors are added. For uniformly random vectors, the probability of any
dependence is < 2^{16−461} ≈ 2^{−445}. So the experiment is finite evidence that **no unusually structured relation**
ties generic short loops to the rest. It does not show a surprising arithmetic obstruction.
*The relations that do occur* all involve only low loops. Examples, read off the data, not classified exhaustively:
(i) the identity [γ_A]_short = [γ_A]_known when A ≤ BMAX is itself a length-3 word. If (A/p) = −1 this is a trivial
index relation: the certificate is explicit. This accounts for most of the 262/267.
(ii) Euclid-step identities, e.g. at p = 2953: [γ₃₇₀] = [γ₁] + [γ₂] + [γ₇] + [γ₈] + [γ₁₄₇₇]. Here p/370 = [[8, 53, 7]],
370 ≡ 7/8 and 7 | p + 1, so the identity transports the known symbol (7/p) = −1 to the low certificate 370.
(iii) The A = 3 family {[γ₁], [γ_{(p+1)/2}], [γ₃], [γ_{(p+2)/3}]}, present at every p ≡ 1 (3).
Index relations are absent (BMAX 30) only at 3049, 3889, **5569, 9601** (two (★)-zero primes) and 18481. With BMAX 10
they are absent at 53 primes.

**KE1 status (honest).** The registered kill (§3) asked whether every relation with c ≠ 0 is "forced", i.e. a formal
identity holding for all n of the population, with the list to be fixed explicitly. That list was never fixed. Relations
of type (ii) hold only on residue classes of p, so by the literal registered definition they are **not** forced.
The raw count of index-positive inputs is 46/46 primes ≤ 3000 (BMAX 30). That count also includes the explicitly forced
overlap identities of type (i), so it does **not** count non-forced relations. A classification and count of the
non-forced relations was not carried out. Hence KE1's literal outcome is undetermined, and **KE1 is reported as "not
evaluated as registered"**; it did not fire. The registered follow-up ("examine for a uniform law") was carried out in a
post-hoc form, the height classification above. It found that every relation lives on bounded-height loops, and that
generic loops have none. The verdict below rests on this post-hoc observation together with Prop E3, not on KE1's
literal kill clause.

### 4.2 KE2 (secondary, NOT pre-registered): Hecke-equivariant fakes

Script `scripts/z63_euclid_hecke.py` adds Hecke operators T_ℓ on H₁. Coset representatives are [[1,k],[0,ℓ]] and
[[ℓ,0],[0,1]]; elements are re-expressed as S/T-words by the Euclidean algorithm, with T-powers walked in closed form
along cusp cycles; every Schreier generator's class is checked against its basis vector. The script computes
E := {ψ ∈ H¹ : ψ∘T_ℓ = (ℓ+1)ψ, ℓ ∈ {2,3,5,7,11,13}}. Run: `BMAX=10 HIGH=20 LS=2,3,5,7,11,13 python3
scripts/z63_euclid_hecke.py <the 89 primes p ≡ 1 (24) ≤ 6000>` → `data/z63/euclid/ke2_hecke_6000_B10_H20.tsv` (≈ 7 min).
* χ_p ∈ E at all 89 primes, a numerical check of Lemma E2 including ℓ = 2. dim E = 3 at 78 primes and 5, 7, 9, 11 at
  3, 4, 3, 1 primes.
* E contains the word-local class ψ₀, the restriction of the character S, T ↦ 1 of PSL₂(ℤ), with ψ₀(γ_A) = r + 1 + Σb_i
  mod 2 (`scripts/z63_euclid_psi0.py`: cocycle and Hecke eigenclass at 73, 409, 1009, 2017). On all p − 1 loops,
  span(E|loops) ∩ span(word features {1, r, Σb_i, χ, #even letters, b₁, b_r, ell-count}) has dimension exactly 2 (= ⟨χ, ψ₀⟩)
  at 16 tested primes 193 … 2953 (`data/z63/euclid/ke2_featurefit.txt`, raw rows with parameters). The remaining
  dimension(s) of E are not combinations of *these* features. That shows only that this feature dictionary fails, not
  that they are non-local in general; the classes are not identified.
* *Affine dimension* of {ψ ∈ E : ψ|_𝒦 = χ|_𝒦}: 0 at 68 primes (there 𝒦 and the Hecke equations determine χ, so all its
  values, including those on generic loops, are computable by finite linear algebra), and
  1, 2, 3 at 16, 4, 1 primes. **Hecke-equivariant fakes** (ψ in this affine space with ψ = 0 on all length-3 loops)
  exist at 14/89 primes. With ψ = χ also on the low loops and ψ = 0 on the high ones, they exist at 15/89 primes.

## 5. Theorems and their scope

**Prop E3 (fake-cocycle criterion; PROVED, linear algebra).** Let H be a finite-dimensional F₂-space, χ ∈ H*, and
𝒦, 𝒞 ⊂ H finite (known classes, candidate certificate classes). Then the following are equivalent:
(i) every ψ ∈ H* with ψ|_𝒦 = χ|_𝒦 satisfies ψ(c) = 1 for some c ∈ 𝒞;
(ii) χ does not vanish on span 𝒦 ∩ span 𝒞.
*Proof.* (ii)⇒(i): take v ∈ span 𝒦 ∩ span 𝒞 with χ(v) = 1; then ψ(v) = χ(v) = 1 and v is a sum of elements of 𝒞, so
ψ(c) = 1 for one of them. (i)⇒(ii): if χ vanishes on W := span 𝒦 ∩ span 𝒞, put ψ(k + c) := χ(k) for k ∈ span 𝒦,
c ∈ span 𝒞; this is well defined (k + c = k′ + c′ ⇒ k − k′ ∈ W ⇒ χ(k) = χ(k′)) and linear; extend to H. Then ψ = χ on
𝒦 and ψ = 0 on 𝒞. ∎
**Corollary E3′ (scope).** Consider an argument of the shapes of Lemma P0 (a)–(e) on the Euclidean path complex of n which
uses χ_n only (1) as a class in H¹(Γ₀(n)/±1; F₂) and (2) through its values on a fixed known set 𝒦. Such an argument
proves the same conclusion for every ψ with ψ|_𝒦 = χ_n|_𝒦. Hence it can force a χ = −1 length-3 loop only if
χ_n ≠ 0 on span 𝒦 ∩ span 𝒞(n), where 𝒞(n) = {[γ_A] : A ∈ L₃(n)}.
For the 𝒦 of §4.1 at the tested inputs, span 𝒦 ∩ span 𝒞 = span 𝒦 ∩ span 𝒞_low. Indeed, if k = c_low + c_high, then
c_high ∈ span(𝒦 ∪ 𝒞_low) ∩ span 𝒞_high = 0. So (CERTIFIED for those inputs and that 𝒦):
* at every tested prime, a class ψ can be chosen that agrees with χ_p on 𝒦 and on all low length-3 loops and takes
  **arbitrary prescribed values on the generic (high) length-3 loops**. An argument of this kind can certify only
  low-height certificates;
* a fake ψ that agrees with χ_p on 𝒦 and vanishes on *all* length-3 loops exists only where the low menu contains no
  certificate tied to 𝒦: at 5/267 primes (BMAX 30: 3049, 3889, 5569, 9601, 18481) and 53/267 (BMAX 10).
**Scope limits (review M3).** This is a statement about the tested known sets and levels only. It does **not** cover
larger known sets. For example, adjoining *all* loops of height ≤ 20 at p = 1009 (510 loops, rank 125 of dim H₁ = 169)
makes the high short loops dependent: rank increment 7 of 10 (reviewer's computation, reproduced by
`scripts/z63_euclid_allheight.py` → `data/z63/euclid/allheight_1009.txt`). The three relations pair short loops whose
labels multiply to a low-height number. For instance p/29 = [[35,5,6]] and p/35 = [[29,6,6]] with 29·35 = p + 6, and
the 4-term relation {23, 44, 344, 351}. They are homological shadows of the label identity A·v ≡ u for a word (v,t,u),
and they carry exactly the χ-product (u/p) given by multiplicativity (EVIDENCE, one prime). So structured relations do
exist once the known set contains long low-height loops. They re-express multiplicativity of the labels and do not by
themselves force a sign. Nor does it cover other complexes through which χ
factors, integer-valued or balance information (§2), group-generation / quotient arguments, or arguments that use
further structure of χ. Low-height certificates are the bounded-height (B1-type) menu. The FRONTIER B1 barrier
(Thm C, CONDITIONAL on Hypothesis H, and the unconditional quantitative witness-modulus bound) concerns bounded
witness procedures. That this specific menu fails infinitely often is an Assessment by analogy, not proved here.

**Hecke structure (Lemma E2 + KE2).** Hecke equivariance is an extra property of χ outside Cor E3′'s scope. The data
show that it largely **removes** the fake-cocycle obstruction: the affine space of Hecke-equivariant ψ agreeing with χ
on 𝒦 is {χ} at 68/89 primes, and Hecke-equivariant fakes exist at only 14/89. A "Hecke-equivariant linear argument" at
such a prime would have to prove that every admissible ψ, i.e. χ itself when the space is {χ}, is non-zero on some short
loop. That is a reformulation of (S). At those 68/89 tested levels, 𝒦 and the Hecke equations determine χ and permit
computation of all its values by finite linear algebra. What KE2 does **not** supply is a *uniform* proof that some
short-loop value is non-zero. The computation does not show that such a uniform proof cannot exist (Assessment).

**Remark E5 (what the Euclidean complex contributes; Assessment, with proved pieces).**
(1) *Easy side.* The integer total φ(n)/2·[n ≠ □] is T1-native and computable (PROVED), but it is 0 mod 2 at primes
p ≡ 1 (4). It is not an F₂ index, and Prop E3 does not use it.
(2) *Transport.* For the tested 𝒦, H₁ of the level-n complex offers no relation that links generic short loops to
anything (§4.1). The other visible handle is the multiplicative label A ≡ u/v ∈ (ℤ/n)^*: by Lemma E1 the index is the
quadratic character of the label. Its signs are the mod-8 cells of DEDEKIND Thm 4.5, and existence in a cell is B2
(HJ_DEEP Prop 4.1). This approach therefore needs additional arithmetic structure or additional known classes.
(3) *Non-abelian refinements.* (S)(n) ⟺ G₃(n) := ⟨γ_A : A ∈ L₃(n)⟩ ⊄ ker χ_n (trivial). χ_n factors through
Γ₀(n) → B(ℤ/n) → (ℤ/n)^* (PROVED). Whether a group-generation argument (e.g. showing that G₃(n) has a large image)
could help is not excluded here.

## 6. Verdict

**NARROWED.** No HOT LEAD. ES, (MS), SQ₅ and (S) remain open.
* **PROVED:** Lemma E1 (dictionary, n ≡ 1 (4): HJ paths of n give distinguished loops [γ_A] in the level-n presentation
  complex, not all loops; index
  χ_n(γ_A) = (A/n); χ_n ≠ 0 ⟺ n ≠ □); Lemma E2 (Hecke eigenrelation χ∘T_ℓ = (ℓ+1)χ); Prop E3 (fake-cocycle criterion)
  and Cor E3′ as scoped.
* **CERTIFIED (§4.1):** in H₁(Γ₀(n)/±1; F₂), generic (height > HIGH) length-3 loops are F₂-independent modulo the known
  part 𝒦 and the low length-3 loops. This holds at all 267 primes p ≡ 1 (24) ≤ 2·10⁴ and at the 102 control levels.
  The counts are 7 244 high loops at the primes for BMAX 10 (2 584 for BMAX 30; the two sets overlap) and 1 022 / 366 at
  the controls, with rank deficit 0 in every case. This matches a random-vector null model (§4.1): finite evidence
  against structured relations, not a surprise. Index relations occur only through the low menu: at 262/267 (BMAX 30)
  and 214/267 (BMAX 10) primes.
* **KE1:** not evaluated as registered. The "forced" list was never fixed, and the type-(ii) relations are not formal
  identities in n. The raw 46/46 index-positive count includes forced overlap identities and does not count non-forced
  relations. The post-hoc height version supports the verdict for the tested levels and known sets (§4.1).
* **KE2 (secondary; CERTIFIED for 89 primes ≤ 6000):** χ_p ∈ E (dim 3 generically). At 68/89 primes, Hecke
  equivariance plus 𝒦 determines χ, so all its values can be computed by finite linear algebra. It supplies no uniform
  proof that some short-loop value is non-zero.
* **Precise missing lemma (for this restricted linear approach, not a necessary condition for every proof of (S)).**
  *A relation, uniform in p ≡ 1 (24), in H₁(Γ₀(p)/±1; F₂) (or in another complex through which χ_p factors) that links
  generic length-3 loops to classes of computable χ.* By Prop E3 this means an a-priori element of span 𝒦(p) ∩ span 𝒞(p)
  with χ_p = 1, for a known set 𝒦(p) that is specified independently of the certificates. Other proposed escapes use
  structure beyond (1)–(2) of Cor E3′, such as Hecke structure, integer balance, group generation, or the multiplicative
  labels u/v. For the tested 𝒦 and levels, the first option has no instances beyond the bounded-height menu (§4.1).
  Enlarging 𝒦 does create relations (p = 1009, §5). No infinite failure of the low menu is proved.

## 7. Falsifier table (final; for EUC-H and Prop E3)

| screen | EUC-H index | where primality / non-squareness enters |
|---|---|---|
| F1 odd squares | χ_{m²} ≡ 0: no index anywhere; T1 automatic. The 58 squares tested show the same H₁-independence *behaviour* as primes. | only in χ_n ≠ 0 |
| F2 C-even / numerator 8 | Support = all χ = −1 length-3 words (five slices), not (★) or its C-even half. (S) holds at all 12 R₈ zeros in [10¹⁰, 1.1·10¹⁰]: explicit interior χ = −1 words, `scripts/z63_euclid_r8check.py` → `data/z63/euclid/r8_zeros_S_witness.txt` (CERTIFIED). | — |
| F3 composites | Behaves as at primes: 40 composite R-zeros and Z₇ tested, same independence. (S) has no known composite counterexample. The cross-model reviewer found explicit χ = −1 length-3 words at 284 of the 285 composite R-zeros. 105 has no L₃ word, so (S) is vacuous there and 105 has **no** certificate. A non-squareness-only argument is not refuted by data. | not needed for (S) (Assessment) |
| F4 known zeros | (★)-zero primes 409, 577, 5569, 9601 tested, same structure. At 5569 and 9601 the BMAX-30 menu yields no index relation. (S) holds at all 14 (★)-zeros and all 38 𝔊*-zeros (≤ 10⁹ census of HJ_DEEP/R174) and at the R₈ zeros. | — |

## 8. Proposed FRONTIER text (do not edit FRONTIER here)

*§6 (z63 EUCLID):* Board item astra-2 (an index on the complex of all Euclidean paths), canonical version. For
n ≡ 1 (4), the HJ path of n/A gives a distinguished loop γ_A in the presentation complex of Γ₀(n)/±1, with
χ_n(γ_A) = (A/n), and χ_n ≠ 0 iff n is not a square.
CERTIFIED (267 primes p ≡ 1 (24) ≤ 2·10⁴, 102 control levels; `Z63_EUCLID.md` §4): generic (height > 20 or > 60)
length-3 loops are F₂-independent of the cusp and elliptic classes, of the loops of small A, and of the low-height
length-3 loops. This is as expected for random vectors. By the fake-cocycle criterion (Prop E3), at these finite levels
and for these known sets, index arguments that use χ only as a class with known values can certify only bounded-height
(menu) certificates. Enlarging the known set creates relations (p = 1009), and no infinite failure of the menu is
proved. Hecke equivariance plus the known set determines χ at 68/89 tested levels, but gives no uniform non-vanishing
proof (KE2). Odd Hecke images have χ = 0 (Lemma E2). Possible reopenings, not necessary conditions: a uniform relation
linking generic short loops to computable classes, or an input on the labels u/v ∈ (ℤ/p)^* (B2).

## 9. Bottom line

The complex of all Euclidean paths of n exists canonically: the presentation complex of Γ₀(n)/±1, essentially the
Farey tessellation modulo Γ₀(n). For n ≡ 1 (4), every HJ path of n/A gives a distinguished loop there, and its index is
the quadratic character (A/n). T1 is built in: the character is trivial exactly at squares. But, for the tested levels
and known sets, the loops that matter, those of length 3, carry no relations with the known part beyond a
bounded-height menu. At every tested level, the generic length-3 loops are
independent of the small loops, the cusp and elliptic classes, and the low-height short loops, as random vectors would
be. By linear algebra (Prop E3), an index argument that uses χ only as a class with known values on such a set can
therefore reach only bounded-height certificates there. Larger known sets do create relations (p = 1009), and no
infinite failure of the menu is proved. Adding Hecke equivariance determines χ at most tested levels, so its values
become computable, but this gives no uniform proof that one short-loop value is non-zero. Possible escapes, not proved
necessary for every proof of (S): a uniform relation tying generic short loops to computable classes, or an input on the
multiplicative labels u/v of the words, which is B2.

## 10. Internal hostile review (done) and fixes

Reviewer subagent (deep mode) over the commit range of this lane: 1 FATAL, 6 MAJOR, 4 MINOR. All were applied.
* **F1 (FATAL):** 𝒦 omitted length-3 loops with A ≤ BMAX. Fixed, and all data regenerated. The fake counts changed
  drastically: all-short fakes 176 → 5 (BMAX 30) and 215 → 53 (BMAX 10); index relations 91 → 262 and 52 → 214;
  KE2 fakes 23 → 14. The high-loop independence was unaffected.
* **M1:** height at composites must use unit b; fixed (controls' high counts 202/906 → 366/1022, still independent).
* **M2:** "KE1 fired" was not established under the registration. The memo now says it was not evaluated as registered.
  The verdict was changed from DEAD to NARROWED.
* **M3:** conclusions scoped to the tested 𝒦; counterexample to "all bounded-height loops" recorded (p = 1009).
* **M4:** affine dimensions reported; "χ∘T₂ = χ re-expresses (2/p) = 1" removed (false: it holds for all n); Hecke
  conclusions downgraded to Assessment.
* **M5:** random-vector null model added. **M6:** the total φ(n)/2 is 0 mod 2, so it is not an F₂ total.
* **m1–m4:** domain qualifications (p ≠ 5, n = 105 vacuous); orbifold/presentation-complex wording; vacuous assertion
  removed, coset and dimension assertions added, raw feature-fit rows saved; attribution paragraph added.
The reviewer reproduced the H₁ runs at 2953, 9601, 1465, 2401, the Hecke runs at 409, 1009, 2017, the ψ₀ checks and the
12 R₈ witnesses. It checked Lemmas E1 and E2 and Prop E3 / Cor E3′ (span decomposition) as correct.

## 11. Cross-model review (`data/z63/xreview/REVIEW_EUCLID.md`: ACCEPT-WITH-FIXES) — fixes applied
The reviewer independently re-derived E1, E2 and E3/E3′ and found them correct. It reproduced the ranks at five primes
with independent code, the Hecke runs, the p = 1009 enlargement computation and the R₈ witnesses. It also verified (S)
on all F2/F3/F4 screens, finding 284 explicit witnesses among the 285 composite zeros, with 105 vacuous.
Required fixes applied:
(1) Hecke: at 68/89 levels, 𝒦 and the Hecke equations determine χ and permit computation of all its values. The memo now
says only that no *uniform* non-vanishing proof is supplied (§4.2, §5, §6, §8, §9).
(2) Scope: §§6, 8, 9 now say "for these finite levels and known sets", keep the p = 1009 enlargement counterexample,
note that no infinite failure of the low menu is proved, and no longer present the missing generic-loop relation as
necessary for every approach.
(3) KE1: kept as "not evaluated as registered". The raw 46/46 index-positive count is separated from the (unperformed)
count of non-forced relations.
(4) Notation: the missing lemma uses H₁(Γ₀(p)/±1; F₂). "HJ paths give distinguished loops" replaces the literal
equivalence with loops. The n ≡ 1 (4) hypothesis is stated in the exported statements. F3 row: 105 has no certificate.
