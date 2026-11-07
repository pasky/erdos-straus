# Z63_EUCLID — an arithmetic index on the complex of all Euclidean paths (board item astra-2)

**ES is OPEN; nothing here proves or disproves it, (MS), (MS-U₇), SQ₅ or (S).** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Scripts `scripts/z63_euclid_*`, data
`data/z63/euclid/`. Brief: `z52bbriefs/z63_lanes.md` §EUCLID (+ z58 common rules, z53 depth brief).

*Status: CHECKPOINT 1 (skeleton; kill test pre-registered before any computation).*

Notation. HJ = negative (Hirzebruch–Jung) continued fraction n/A = [[b₁,…,b_r]], b_i ≥ 2, r = r(n/A);
L_r(n) = {A ∈ (0,n) : gcd(A,n) = 1, r(n/A) = r}; length-3 words n/A = [[v,t,u]] ⟺ tuv − u − v = n, A = tu − 1
(DEDEKIND_ES Lemma 1.1). S = [[0,−1],[1,0]], T = [[1,1],[0,1]], S(b) := T^b S = [[b,−1],[1,0]]. Γ := Γ₀(n)/±1.
χ_n(γ) := (d/n) (Jacobi) for γ = [[a,b],[c,d]] ∈ Γ₀(n).

## 0. Mandatory falsifier table (for the target (S) and the homological index EUC-H of §2; re-stated at the end)

| screen | behaviour | where primality / non-squareness enters |
|---|---|---|
| **F1 odd squares** | χ_{m²} ≡ 1 (trivial character), so the index is identically 0 at squares and no length-3 loop carries index — T1 is built in (DEDEKIND Prop 3.1). | In the non-triviality of the class χ_n ∈ H¹(Γ₀(n); F₂): χ_n ≠ 0 ⟺ n not a square. This is the *only* place. |
| **F2 C-even / numerator 8** | The index is supported on *all* χ = −1 length-3 words (five DEDEKIND slices: 4 ∣ t, u, v, A or A*), not on the (★) line or its C-even half. R₈ zeros near 10¹⁰ have R ≥ 12, hence (S) holds there (the (★) words are five-slice words). An argument working "verbatim on the C-even sub-line" is not what EUC-H proposes. | — (no C-parity input; the slice union is used). |
| **F3 composites** | χ_n is a non-trivial character of Γ₀(n) at every odd non-square n, so EUC-H treats composites like primes. This is consistent with the data: (S) has **no known counterexample** (0 violations among non-square n ≡ 1 (4) < 10⁹, HJ_DEEP EVIDENCE 3.1 + R174); the lone SQ₅ exception 105 has L₃(105) = ∅ (a (W)-failure, not an (S)-failure). The 285 (★)-zero composites and Z₇ all satisfy (S). | Not needed for (S) (Assessment: (S) is plausibly true for all non-squares); needed only for (W) at primes, which is trivial for p ≡ 1 (4) (bsG_primes_trivial: words (2,2,·), (3,·,4)). |
| **F4 known zeros** | The 14 (★)-zero primes, the 38 𝔊*-zero primes and the R₈ zeros all satisfy (S) (to be re-verified by script, §3). (S) has no known zero, prime or composite. | — |

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

## 4. Computations
(pending)

## 5. Verdict
(pending)
