# Z63_EUCLID — an arithmetic index on the complex of all Euclidean paths (board item astra-2)

**ES is OPEN; nothing here proves or disproves it, (MS), (MS-U₇), SQ₅ or (S).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Scripts `scripts/z63_euclid_*`, data
`data/z63/euclid/`. Brief: `z52bbriefs/z63_lanes.md` §EUCLID (+ z58 common rules, z53 depth brief).

*Status: final draft (checkpoint 1 committed with the pre-registered kill test KE1 before any computation; KE1 fired). Verdict: **DEAD** in canonical form; precise missing lemma stated (§6). No HOT LEAD.*

Notation. HJ = negative (Hirzebruch–Jung) continued fraction n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A);
L_r(n) = {A ∈ (0,n) : gcd(A,n) = 1, r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1
(DEDEKIND_ES Lemma 1.1). S = [[0,−1],[1,0]], T = [[1,1],[0,1]], S(b) := T^b S = [[b,−1],[1,0]]. Γ := Γ₀(n)/±1.
χ_n(γ) := (d/n) (Jacobi) for γ = [[a,b],[c,d]] ∈ Γ₀(n).

## 0. Mandatory falsifier table (for the target (S) and the homological index EUC-H of §2; re-stated at the end)

| screen | behaviour | where primality / non-squareness enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1 (trivial character), so the index is identically 0 at squares and no length-3 loop carries index — T1 is built in (DEDEKIND Prop 3.1). | In the non-triviality of the class χ_n ∈ H¹(Γ₀(n); F₂): χ_n ≠ 0 ⟺ n not a square. This is the *only* place. |
| **F2 C-even / numerator 8** | The index is supported on *all* χ = −1 length-3 words (five DEDEKIND slices: 4 ∣ t, u, v, A or A*), not on the (★) line or its C-even half. (S) holds at the 12 R₈ zeros near 10¹⁰ (explicit words, §7). An argument working "verbatim on the C-even sub-line" is not what EUC-H proposes. | — (no C-parity input; the slice union is used). |
| **F3 composites** | χ_n is a non-trivial character of Γ₀(n) at every odd non-square n, so EUC-H treats composites like primes. This is consistent with the data: (S) has **no known counterexample** (0 violations among non-square n ≡ 1 (4) < 10⁹, HJ_DEEP EVIDENCE 3.1 + R174); the lone SQ₅ exception 105 has L₃(105) = ∅ (a (W)-failure, not an (S)-failure). The 285 (★)-zero composites and Z₇ all satisfy (S). | Not needed for (S) (Assessment: (S) is plausibly true for all non-squares); needed only for (W) at primes, which is trivial for p ≡ 1 (4) (bsG_primes_trivial: words (2,2,·), (3,·,4)). |
| **F4 known zeros** | The 14 (★)-zero primes and the 38 𝔊*-zero primes satisfy (S) (HJ_DEEP/R174 census to 10⁹); the 12 R₈ zeros do too (explicit words, §7). (S) has no known zero, prime or composite. | — |

## 1. Precise statements attacked

* **(S) (CONJECTURE; HJ_DEEP §3).** For every non-square n ≡ 1 (mod 4) with L₃(n) ≠ ∅ there is A ∈ L₃(n) with (A/n) = −1.
  At primes p ≡ 1 (4), (S)(p) ⟹ interior five-slice ES(p) (DEDEKIND Thm 4.5) ⟹ ES(p); (W)(p) is automatic there.
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

## 2. The canonical complex: all Euclidean paths of n glued in the level-n Farey complex

**Lemma E1 (dictionary; PROVED, elementary).** Let n ≥ 3 be odd, A ∈ (0,n) coprime to n, n/A = [[b₁,…,b_r]]. Then
γ_A := S·S(b₁)S(b₂)⋯S(b_r) lies in Γ₀(n), and its lower-right entry is ≡ −A⁻¹ (mod n). Hence, for n ≡ 1 (mod 4),
**χ_n(γ_A) = (A/n).** The map γ ↦ χ_n(γ) is a homomorphism Γ₀(n) → {±1} trivial on −I (n ≡ 1 (4)), i.e. a class
χ_n ∈ H¹(Γ; F₂), and χ_n = 0 ⟺ n is a square.
*Proof.* M := S(b₁)⋯S(b_r) = [[K(b₁..b_r), −K(b₁..b_{r−1})],[K(b₂..b_r), −K(b₂..b_{r−1})]] = [[n, −A′],[A, −A″]] with
A′ := K(b₁..b_{r−1}); det M = 1 gives A·A′ ≡ 1 (mod n). S·M = [[−A, A″],[n, −A′]] has lower-left n ≡ 0 and lower-right
−A′ ≡ −A⁻¹. (−A⁻¹/n) = (−1/n)(A/n) = (A/n). The lower-right entry mod n of a product of elements of Γ₀(n) is the
product of the lower-right entries, and (·/n) is multiplicative, so χ_n is a homomorphism; it is trivial iff (d/n) = 1 for all
units d iff n is a square. ∎

So the **Euclidean path complex of n** is the Schreier (coset) graph of Γ₀(n) in PSL₂(ℤ) = ⟨S, T⟩ — equivalently the Farey
tessellation modulo Γ₀(n) — with 2-cells the relations S² = (ST)³ = 1; each Euclidean path of n/A becomes a closed walk
[γ_A] ∈ H₁(Γ; F₂) (read the letters T^{b₁}S⋯ from the base coset), and the index of a loop is ⟨χ_n, [γ_A]⟩. All p − 1 paths of
a prime p live in one complex with ≈ p/6-dimensional H₁; the total index Σ_A [χ = −1] = φ(n)/2·[n ≠ □] is known.
(S)(n) ⟺ **χ_n does not annihilate V₃(n) := span{[γ_A] : A ∈ L₃(n)}** ⊂ H₁(Γ; F₂).

**What a Euclidean index (Lemma P0 (d)) would be here.** An F₂-relation in H₁(Γ; F₂)
  Σ_{A ∈ L₃(n)} c_A [γ_A] = κ + Σ_j d_j [γ_{B_j}]  (κ a canonical class, B_j in an explicit "known" set with computable symbols)
gives Σ_{A ∈ L₃} c_A [(A/n) = −1] ≡ χ_n(κ) + Σ_j d_j[(B_j/n) = −1] (mod 2); if the right side is provably 1, a certificate
exists. The weights c_A are *not* local: they solve a linear system in the whole complex (they depend on all other paths).
This is exactly the escape left open by Prop R / Thm R. Such a relation, produced uniformly in n, **is** the astra-2 index.

**Lemma E2 (Hecke blindness; PROVED).** For a prime ℓ ∤ 2n, T_ℓ* χ_n = (ℓ + 1)·χ_n = 0 in H¹(Γ; F₂). Hence χ_n vanishes on
T_ℓ(H₁(Γ; F₂)) for every odd ℓ ∤ n: Hecke images carry no χ-information mod 2, and relations obtained by applying odd Hecke
operators to known classes cannot force a short χ = −1 loop.
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

## 4. Computations — KE1 FIRED: generic Euclidean loops are linearly free

**Script** `scripts/z63_euclid_h1.py` (pure Python, < 1 min per run). Built-in checks, all passing on every input:
(a) Lemma E1 at matrix level (lower-left ≡ 0, lower-right·A ≡ −1 (mod n), χ = (A/n)); (b) the coset count equals
[PSL₂(ℤ) : Γ₀(n)/±1] = n∏_{q|n}(1 + 1/q) (implicit: P¹(ℤ/n) normal form; e.g. 1764 cosets at 1465 = 5·293);
dim H₁ = e₂ + 2g + c − 1 at primes (e.g. 13 at 73, 17 at 97); (c) a cocycle representative of χ_n is computed
independently from exact coset matrices (χ of every Schreier generator R_x·s·R_{xs}⁻¹ ∈ Γ₀(n)); it vanishes on every
relator and reproduces (A/n) on every computed loop (≈ 25 000 loops).
**Height.** For A ∈ (ℤ/n)^*, h(A) := min{max(a,b) : A ≡ ±a·b⁻¹ (mod n), a, b ≥ 1}. Every length-3 word has
A ≡ u·v⁻¹ (mod n) (from n = vA − u), so h(A) ≤ max(u, v). "Low" short loops: h(A) ≤ HIGH; "high" (generic): h(A) > HIGH.
Low certificates are the bounded-height (B1-type) ones: for fixed small a, b, whether A ≡ a/b lies in L₃(p) is decided by
a congruence on p (Assessment; cf. HJ_DEEP Lemma 3.2 and FRONTIER B1).

**Runs** (known part 𝒦 = cusp classes, elliptic classes, loops of all B ≤ BMAX and of HJ length ≤ 2; commands
`BMAX=b HIGH=h python3 scripts/z63_euclid_h1.py pop 20000` and the control list; data `data/z63/euclid/ke1_*.tsv`):

| population | inputs | short loops | high loops | rank increase from high loops | inputs with a relation involving a high loop |
|---|---|---|---|---|---|
| primes p ≡ 1 (24) ≤ 2·10⁴, BMAX 30, HIGH 60 | 267 | 12 764 | 2 584 | **2 584** | **0** |
| same, BMAX 10, HIGH 20 | 267 | 12 764 | 7 244 | **7 244** | **0** |
| controls, BMAX 30 / 10 | 108 | 1 966 | 202 / 906 | 202 / 906 | 0 / 0 |

Controls: (★)-zero primes 409, 577, 5569, 9601; Z₇ ∩ [1, 12145] = {105, 1465, 3865, 4545, 10305, 12145}; the first 40
non-square composite R-zeros (57 … 12681, from `composite_zeros_le8e6.txt`); all 58 odd squares 9 … 13689 (105, 1465,
3865, 4545, 10305, 12145 are listed twice). dim H₁ ≈ n/6 (0.167–0.178·p at the primes).

**Reading (CERTIFIED for the listed inputs).** At every input, the classes of the high short loops are linearly
independent modulo span(𝒦 ∪ low short loops) in H₁(Γ₀(n)/±1; F₂): *no F₂-relation of any kind involves a generic
length-3 Euclidean loop.* All relations that do occur involve only low loops and are explicit Euclid-step identities, e.g.
at p = 2953: [γ₃₇₀] = [γ₁] + [γ₂] + [γ₇] + [γ₈] + [γ₁₄₇₇] (p/370 = [[8, 53, 7]], 370 ≡ 7/8, 7 | p + 1; it transfers the
known symbol (7/p) = −1 to the low certificate 370), and the A = 3 family {[γ₁], [γ_{(p+1)/2}], [γ₃], [γ_{(p+2)/3}]}
(present at every p ≡ 1 (3)). Squares, composites, Z₇ and the (★)-zero primes behave exactly like primes (the complex does
not see primality; at squares χ ≡ 0 so relations carry no sign).
*Index relations* (relations whose known side has odd χ, which force an odd number of χ = −1 short loops): at 91/267
(BMAX 30) resp. 52/267 (BMAX 10) primes — exactly the primes where the bounded-height menu happens to contain a
certificate tied to a known symbol; at the other 176 resp. 215 primes none exists, although every one of the 267 primes
has χ = −1 short loops ((S) holds).

**KE1 verdict.** The pre-registered kill fired in substance: at 100 % of primes with generic words, every relation with
c ≠ 0 lies in the low part. *Disclosed deviation:* the registration called relations "forced" if they are formal
identities to be listed; I classified them post hoc by height instead (low = h ≤ HIGH with HIGH = 2·BMAX), and did not
prove that every low relation is a formal identity (the two families quoted are). The conclusion drawn below uses only
the certified independence of the high loops, not the classification of the low relations.

### 4.2 KE2 (secondary, NOT pre-registered): Hecke-equivariant fakes

Script `scripts/z63_euclid_hecke.py` adds Hecke operators T_ℓ on H₁ (coset representatives [[1,k],[0,ℓ]], [[ℓ,0],[0,1]];
elements re-expressed as S/T-words by the Euclidean algorithm; T-powers walked in closed form along cusp cycles). It
computes E := {ψ ∈ H¹ : ψ∘T_ℓ = (ℓ+1)ψ, ℓ ∈ {2,3,5,7,11,13}}. Run: `BMAX=10 HIGH=20 LS=2,3,5,7,11,13 python3
scripts/z63_euclid_hecke.py <the 89 primes p ≡ 1 (24) ≤ 6000>` → `data/z63/euclid/ke2_hecke_6000_B10_H20.tsv` (6 min).
* χ_p ∈ E at all 89 primes. This checks Lemma E2 numerically, including the T₂ case. dim E = 3 at 78 primes and
  5, 7, 9, 11 at 3, 4, 3, 1 primes.
* E contains the word-local class ψ₀ (the restriction of the character S, T ↦ 1 of PSL₂(ℤ); ψ₀(γ_A) = r + 1 + Σb_i mod 2).
  `scripts/z63_euclid_psi0.py` checks that it is a Hecke eigenclass at 73, 409, 1009, 2017.
  On all p − 1 loops, span(E|loops) ∩ span(word features {1, r, Σb_i, χ, #even letters, b₁, b_r, ell-count}) has
  dimension exactly 2 (= ⟨χ, ψ₀⟩) at 16 tested primes 193 … 2953 (`data/z63/euclid/ke2_featurefit.txt`). The remaining
  dimension(s) of E are not word-local in these features (not identified; possibly a Dedekind–Rademacher-type or
  elliptic-type class — Assessment).
* **Hecke-equivariant fakes** (ψ ∈ E, ψ = χ on 𝒦, ψ = 0 on all length-3 loops) exist at only 23/89 primes. With ψ = χ
  also required on the low loops and ψ = 0 on the high ones, they exist at 15/89. So imposing Hecke equivariance
  **removes the fake-cocycle barrier at most primes**: E is so small that the known values essentially pin down χ.
  This does not give an argument, because then "every admissible ψ is non-zero on some short loop" just says
  χ_p(γ_A) = (A/p) = −1 for some A ∈ L₃(p), which is (S) itself. Hecke equivariance determines χ without telling
  us its values on generic short loops. Those values are the labels' quadratic characters (Lemma E1), i.e. B2.

## 5. Theorems

**Prop E3 (fake-cocycle criterion; PROVED, linear algebra).** Let H be a finite-dimensional F₂-space, χ ∈ H*, and
𝒦, 𝒞 ⊂ H finite (known classes, candidate certificate classes). Then the following are equivalent:
(i) every ψ ∈ H* with ψ|_𝒦 = χ|_𝒦 satisfies ψ(c) = 1 for some c ∈ 𝒞;
(ii) χ does not vanish on span 𝒦 ∩ span 𝒞.
*Proof.* (ii)⇒(i): take v ∈ span 𝒦 ∩ span 𝒞 with χ(v) = 1; then ψ(v) = χ(v) = 1 and v is a sum of elements of 𝒞, so
ψ(c) = 1 for one of them. (i)⇒(ii): if χ vanishes on W := span 𝒦 ∩ span 𝒞, put ψ(k + c) := χ(k) for k ∈ span 𝒦,
c ∈ span 𝒞; this is well defined (k + c = k′ + c′ ⇒ k − k′ ∈ W ⇒ χ(k) = χ(k′)) and linear; extend to H. Then ψ = χ on
𝒦 and ψ = 0 on 𝒞. ∎
**Corollary E3′ (scope of Euclidean index arguments).** Any argument of the shapes of Lemma P0 (a)–(e) on the
Euclidean path complex of n which uses χ_n only (1) as a class in H¹(Γ₀(n)/±1; F₂) and (2) through its values on a known
set 𝒦 of loops proves the same conclusion for every ψ with ψ|_𝒦 = χ_n|_𝒦. It can force a χ = −1 length-3 loop only if
χ_n ≠ 0 on span 𝒦 ∩ span 𝒞(n), 𝒞(n) = {[γ_A] : A ∈ L₃(n)}. By §4, at every tested input span 𝒦 ∩ span 𝒞 =
span 𝒦 ∩ span 𝒞_low (if k = c_low + c_high then c_high ∈ span(𝒦 ∪ 𝒞_low) ∩ span 𝒞_high = 0), so (CERTIFIED for the
§4 inputs):
* at 176 of the 267 primes p ≡ 1 (24) ≤ 2·10⁴ (BMAX 30) there is a **fake class** ψ ∈ H¹(Γ₀(p)/±1; F₂) that agrees with
  χ_p on every cusp and elliptic class and on every loop of A ≤ 30 or HJ length ≤ 2, and **vanishes on every length-3
  Euclidean loop**; no Euclidean index argument of the above kind can exist at those primes;
* at all 267 primes, ψ can be required to agree with χ_p on 𝒦 and on all low length-3 loops (h ≤ 60) and to take
  **arbitrary prescribed values** on the generic ones.
So, in the canonical complex, the "relations between words" escape of Prop R / Thm R exists only for bounded-height
words. These are a fixed congruence menu (B1).

**Hecke structure (Lemma E2 + KE2).** Cor E3′ covers arguments that use χ only as a class with known values. Hecke
equivariance is an extra property of χ, and it changes the picture in the following way.
(a) *Hecke relations as known data are empty.* χ(T_ℓx) = (ℓ+1)χ(x) = 0 for odd ℓ, so χ annihilates T_ℓH₁ and these
relations transport no sign (Lemma E2, PROVED). For ℓ = 2, χ∘T₂ = χ re-expresses (2/p) = 1.
(b) *Hecke equivariance as a constraint on fakes* does pin χ down: fakes in E exist at only 23/89 primes (§4.2).
The resulting "argument" is: every ψ ∈ E with ψ|_𝒦 = χ|_𝒦 is non-zero on some short loop. When that affine space is {χ},
this is (S) itself. So the Hecke-refined version is a tautology rather than an index: it needs the values of χ on generic
short loops. E|loops is spanned by the word-local classes χ, ψ₀ and non-local class(es) (§4.2). The local part is
Prop R's cell sums. Using the non-local part would need an a-priori evaluation that nobody has (Assessment).

**Remark E5 (what the Euclidean complex really contributes; Assessment, with proved pieces).**
(1) *Easy side.* The total index over all loops is Σ_A [χ_n(γ_A) = −1] = φ(n)/2·[n ≠ □] (PROVED, Lemma E1). It is
T1-native and computable. This is the genuine new feature compared with certificate-only parity counts (Lemma P0).
(2) *Transport.* Moving index from long loops to short ones needs relations. In H₁ of the level-n complex the generic short
loops have none (§4). The only transport is through the multiplicative label A ≡ u/v ∈ (ℤ/n)^* (Lemma E1: the index
is the quadratic character of the label). That is the arithmetic of the set {u/v : (v,t,u) ∈ X(n)}, whose signs are the
mod-8 cells of DEDEKIND Thm 4.5. This is B2 (HJ_DEEP Prop 4.1).
(3) *Non-abelian / π₁ refinements.* (S)(n) ⟺ the subgroup G₃(n) := ⟨γ_A : A ∈ L₃(n)⟩ ⊄ ker χ_n. Its image mod n lies
in the Borel subgroup, and χ_n reads only the diagonal character, so π₁ adds nothing to the sign question beyond the
labels (PROVED: χ_n factors through Γ₀(n) → B(ℤ/n) → (ℤ/n)^*).

## 6. Verdict

**DEAD (in its canonical form), with a precise missing lemma.** No HOT LEAD. ES, (MS), SQ₅ and (S) remain open.
* **PROVED:** Lemma E1 (dictionary: Euclidean paths of n = loops [γ_A] in the level-n Farey complex; index =
  χ_n(γ_A) = (A/n); χ_n ≠ 0 ⟺ n ≠ □); Lemma E2 (Hecke blindness, χ∘T_ℓ = (ℓ+1)χ); Prop E3 (fake-cocycle
  criterion) and Cor E3′.
* **CERTIFIED (§4):** in H₁(Γ₀(n)/±1; F₂), generic length-3 loops are F₂-independent of each other, of all
  bounded-height loops and of the cusp/elliptic classes. This holds at all 267 primes p ≡ 1 (24) ≤ 2·10⁴ and at 108
  controls (squares, Z₇, composite R-zeros, (★)-zero primes): 7 244 high loops at the primes for BMAX 10 (2 584 for
  BMAX 30; the two sets overlap) and 906 / 202 at the controls, with rank deficit 0 in every case.
  Fake classes killing every short loop while agreeing with χ_p on the known part exist at 176/267 primes (BMAX 30) and
  215/267 (BMAX 10).
* **Kill test KE1:** fired (with the disclosed height-classification deviation).
* **KE2 (secondary, not pre-registered; CERTIFIED for 89 primes ≤ 6000):** χ_p lies in the Hecke eigenspace E
  (dim 3 generically). Hecke-equivariant fakes exist at only 23/89 primes, so equivariance pins χ down, but without
  giving its values on generic short loops (§5 "Hecke structure").
* **Precise missing lemma (what an astra-2 index would need).** *A uniform-in-p relation in H₁(Γ₀(p); F₂) (or in any
  complex through which χ_p factors) linking generic length-3 loops to classes of computable χ — equivalently, by Prop E3,
  an a-priori element of span 𝒦(p) ∩ span 𝒞(p) with χ_p = 1.* §4 shows that such elements do not exist at the tested
  primes beyond the bounded-height menu. So the missing input is not topological: it must use χ_p *non-linearly*, through
  the multiplicative structure of the labels u/v, i.e. B2.

## 7. Falsifier table (final; for EUC-H and Prop E3)

| screen | EUC-H index | where primality / non-squareness enters |
|---|---|---|
| F1 odd squares | χ_{m²} ≡ 0: no index anywhere; T1 automatic. The H₁-independence of generic loops holds at squares as well (58 squares tested), so the topology is identical. | only in χ_n ≠ 0 |
| F2 C-even / numerator 8 | support = all χ = −1 length-3 words (five slices); not tied to (★) or its C-even half. (S) holds at all 12 R₈ zeros in [10¹⁰, 1.1·10¹⁰] (explicit interior χ = −1 words, `scripts/z63_euclid_r8check.py` → `data/z63/euclid/r8_zeros_S_witness.txt`, CERTIFIED) | — |
| F3 composites | behaves exactly as at primes (40 composite R-zeros and Z₇ tested: same independence). (S) has no known composite counterexample, so a non-squareness-only argument is not refuted by data. | not needed for (S) (Assessment) |
| F4 known zeros | (★)-zero primes 409, 577, 5569, 9601 tested: same structure; (S) holds at all 14 (★)-zeros, all 38 𝔊*-zeros (≤ 10⁹ census of HJ_DEEP/R174) and the R₈ zeros (via R ≥ 12) | — |

## 8. Proposed FRONTIER text (do not edit FRONTIER here)

*§6 (z63 EUCLID):* Board item astra-2 (index on the complex of all Euclidean paths). In the canonical complex, the Farey
tessellation mod Γ₀(n), the HJ path of n/A is a loop γ_A with χ_n(γ_A) = (A/n). χ_n ∈ H¹(Γ₀(n); F₂) is non-zero iff n is
not a square, so T1 is built in, and the total index φ(n)/2 is known. However, generic length-3 loops are F₂-independent
of everything else in H₁ (CERTIFIED: 267 primes p ≡ 1 (24) ≤ 2·10⁴ and 108 controls, `Z63_EUCLID.md` §4). By the
fake-cocycle criterion (Prop E3), any index argument linear in χ can reach only bounded-height certificates (a B1 menu;
index relations at 91/267 primes). Odd Hecke operators are χ-blind mod 2 (Lemma E2). Reopen only with a non-linear use
of χ_p, i.e. an input about the labels u/v ∈ (ℤ/p)^* of the words (B2).

## 9. Bottom line

The complex of all Euclidean paths of n exists canonically: the Farey tessellation modulo Γ₀(n). Every HJ path of n/A is
a loop whose index is the quadratic character (A/n). This gives exactly what a Zagier-type argument would want: a
computable, T1-native total (half of all loops carry index at every non-square n, none at squares). But the loops that
matter, those of length 3, are homologically free. At every tested level their classes are independent of each other,
of all bounded-height loops, and of the cusp and elliptic classes. So there is no relation along which index could flow
to them. Linear algebra (Prop E3) turns this into a fake-class statement: at most tested primes some class agrees with
χ_p on all known loops and still vanishes on every length-3 loop. Hecke operators do not help (odd ones are χ-blind
mod 2). An argument would have to use χ_p non-linearly, through the multiplicative labels u/v of the words. That is
B2 again.
