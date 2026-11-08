# Z64_EQUIV — statements equivalent to ES-at-primes / (MS) / U₇ / (S) / CONV-II in other fields (wave z64, lane EQUIV)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Brief: `z52bbriefs/z64_lanes.md` §EQUIV (+ z58 common
rules, z53 depth brief). Scripts `scripts/z64_equiv_*`, data `data/z64/equiv/` (source excerpts with URLs, theorem numbers
and access dates in `data/z64/equiv/sources/*.md`, gathered by three research subagents; decisive items re-read by me,
marked ✔).

**Verdict: narrowed.** No HOT LEAD. One genuinely new precedent class for the Z63 catalogue (prime-degree Hurwitz
existence, a claimed 2026 theorem proved in residue characteristic p), a proved dictionary of fourteen cross-field
equivalences with their native tools screened, and a scoped explanation of why every *formula-level* dictionary is
circular.

## 0. Bottom line

1. **Z63_PRECEDENT missed one precedent class that has the exact prime/composite shape ES has.** It is the Hurwitz
   existence problem in prime degree (§3.2, ✔). Every compatible branch datum of degree p over S² is realisable:
   * Edmonds–Kulkarni–Stong asked this in 1984 (Trans. AMS 282, p. 774, p. 787).
   * Song–Wen–Zhang claim a proof (arXiv:2609.20572, Thm 1.1, Sep 2026, unrefereed). Their mechanism is
     **construction in residue characteristic p followed by lifting**. Primality enters through the regular subgroup
     C_p ≤ S_p (their Lemma 2.5).
   * For **every** composite degree there is an explicit non-realisable datum (EKS Prop. 5.7).
   * Some families are realisable exactly at the degrees x² + y² (Petronio's survey, Thm 3.13). These contain all
     primes ≡ 1 (4) and fail on a density-1 set of degrees.
   Z63 also omitted, or listed only implicitly, five further classes that the repository knows elsewhere: Elkies-type
   sign forcing, Legendre's negative Pell, the Holzer/Minkowski O(1) window, realisation theorems
   (Deuring–Waterhouse), and finite-criterion universality (15/290). §3.1 tabulates them with sources.
2. **None of the prime-exact mechanisms transfers** (§3.3; Assessment, with one CONDITIONAL lemma). Each uses
   primality at a step ES has no counterpart for:
   * a geometric statement over an algebraically closed field of characteristic p (Hurwitz);
   * a group of units plus unique factorisation (Pell, two squares);
   * an archimedean sign of one value (Elkies).

   ES needs a ℤ-point (an arithmetic witness). Lemma H (CONDITIONAL on the SWZ theorem): no family of branch data has
   prime-degree realisability equivalent to R(p) ≥ 1. The revised gap statement is in §3.4.
3. **Fourteen equivalences, proved with exact quantifiers** (§4). They span:
   * numerical semigroups (k-Frobenius numbers);
   * stacky curves;
   * Riemann surfaces and 2-orbifolds (new Lemma A: ES(n) ⟺ some (X, G) has |G|(n − 4) = n(2g − 2), for every odd
     n ≥ 5);
   * singularity theory (lct);
   * pretzel links and Seifert manifolds;
   * lens spaces and definite fillings (new: the C = 1 line of (★) is the line whose plumbing contains a (−4) vertex,
     i.e. a rational-blowdown configuration of Aceto–McCoy–Park);
   * Lorenzini's critical polynomial (the critical-group pairing *is* the (S) sign);
   * SL₂(ℤ), Farey edges and toral automorphisms;
   * cyclotomic Frobenius classes and ℤ[√−p] ideals;
   * Fermat-curve quotients (new: (★) triples are lcm-balanced and always cyclically realisable);
   * q-series;
   * TFNP.
   Each comes with its catalogue ID where one exists (`ES_CONNECTIONS_TODO.md`).
4. **Why they are circular** (§5; PROVED in the scoped sense stated there, plus an Assessment). Every native existence
   tool met falls into one of four types:
   * (I) realisation from parameter data: the data are the certificate;
   * (II) universality or density theorems, which hold only after a relaxation that is T1-blind or averaged
     (Lemma R: each proved relaxation holds at odd squares);
   * (III) obstruction theorems, which give non-existence only;
   * (IV) structure theorems on a canonical p-object, which are the only non-circular type. All the instances known
     to the repo are already screened.

   An escaping equivalence must have type (IV), with a structure theorem that sees primality.
5. **FRONTIER §4 screens** (§7): every row inherits T1 / 8/131 / composite behaviour verbatim, so the screens bite on
   tools. All type-(I)–(III) tools fail "fixed p, non-circular". The type-(IV) candidates are those of Z63_EUCLID /
   RAYCLASS / supersingular memos, unchanged.

## 1. Mandatory falsifier table (F1–F4; data `data/z58/screens/`)

An *equivalence* is the same statement in other coordinates, so it inherits F1–F4 verbatim. The screens therefore bite
on the **native tool** of the target field. Column entries say what the field's best native tool does on each screen.

| row (§4) | F1 odd squares | F2 C-even / 8/131 | F3 composites | F4 known zeros | verdict |
|---|---|---|---|---|---|
| E1 k-Frobenius | inverse theorems (Rosales: every g is a 3-generator Frobenius number; odd g = F(2, g+2)) are input-blind, true at m² | level k ≡ 3 (4) is not controlled by any inverse theorem | input-blind | no tool sees them | circular / relaxation |
| E3 orbifold χ, Aut(X) | ES itself holds at m² (no T1 for ES); realisation (Selberg/Fox) needs the signature = certificate | — | — | — | circular (I) |
| E4 lct | 4/n ∈ lct(ℂ²) for all n ≥ 5 (Lemma R(c)), so the full lct statement is true at squares and everywhere | — | — | — | relaxation (II) |
| E5 pretzel / Seifert | invariants are computed from (x, y, z) | — | — | — | circular (I) |
| E6 lens space / plumbing (S) | the Jacobi −1 class is empty at m² (statement-level F1); Donaldson/HF tools are obstructions | C = 1 ↔ (−4) vertex; C even not distinguished | — | — | obstruction (III) |
| E7 Lorenzini (W)/(S) | (W) is true at m² ≥ 25 (T1-blind); Wang–Lu density theorem is averaged | — | (W) exceptions finite (to 10⁹) | — | relaxation (II) |
| E8 SL₂ / Farey / cat map | structure of SL₂(ℤ) is p-blind | — | — | — | circular (I) |
| E9–E10 ray class / ℤ[√−p] | genus layer free (SPARKS9); class-level forcing not available | — | — | — | covered (IV, RAYCLASS) |
| E11 Fermat quotients | genus formula only | — | — | — | circular (I) |
| E12 q-series | Thm K; coefficient positivity not available pointwise | — | — | — | covered (AUTOMORPH) |
| E13 Hurwitz / dessins | uniform data ↔ signature | — | — | — | circular (I) |
| E14 TFNP | totality by a syntactic principle ⟹ a parity/pigeonhole/potential argument, screened in Z62/Z61 | — | — | — | covered |
| §3.3 Hurwitz prime degree (precedent) | composite degrees fail (EKS 5.7); ES's square failures have no Hurwitz counterpart | — | Lemma H: prime-degree realisability carries no (★) information (CONDITIONAL) | — | no transfer |

No row survives all four screens with a working native tool. **No HOT LEAD.**

## 2. Precise statements attacked (all CONJECTURE unless stated)

For a prime p (or odd n):
* **ES(n):** ∃ x, y, z ∈ ℕ with 4/n = 1/x + 1/y + 1/z.
* **(★)/(MS):** R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} ≥ 1. (MS) is R(p) ≥ 1 for primes p > 10¹⁷ in 𝔐 (FRONTIER
  §2.4). Divisor form: ∃ C, ∃ d | 4Cn + 1 with d ≡ −1 (mod 4C). (MS) ⟹ ES (PROVED rel. Mordell + Salez).
* **U₇(n):** ∃ f ≡ 7 (mod 8) with (−n mod f) | f + 1 (`Z60_LOPEZ.md` Lemma 7). CONJECTURE U₇: true for every odd
  non-square n ∉ Z₇ = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425}.
* **(S):** every non-square n ≡ 1 (4) with L₃(n) ≠ ∅ has a length-3 HJ word n/A = [[v, t, u]] (tuv − u − v = n,
  A = tu − 1, gcd(A, n) = 1) with Jacobi (A/n) = −1 (`HJ_DEEP.md` §3). (S)(p) ⟹ ES(p) via DEDEKIND_ES Thm 4.5.
* **CONV-II:** N_II(n) = #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} ≥ 1 for odd non-square n ≠ 4545 (`Z58_WILDCARD.md`).

"Equivalent in another field" means here a statement Φ(p) about an object of field F such that Φ(p) ⟺ (target)(p)
is PROVED for every prime p in the stated class. Where only one direction or an explicitly labelled finite loss
holds, the row says so.

**Why this is not already closed.**
* The z52b catalogue (`ES_CONNECTIONS_TODO.md`, 3192 items) lists one-line *forms* in most fields of the brief, for
  example:
  * Frobenius numbers (Z0394), Brieskorn–Pham lct (Z0155), Hurwitz existence (Z0171), dessins (Z0417);
  * weighted projective lines (Z0418), Lorentzian polynomials (Z2606);
  * plumbings / lens spaces (DEDEKIND_ES, bsA_*), Lorenzini (HJ_DEEP), SL₂ / Farey (Z63_EUCLID), TFNP (z31).

  Most of these were never *proved* as equivalences with exact quantifiers. The z52d avenue layer judged them
  "circular" item by item, without a stated reason.
* The prime-degree Hurwitz theorem, Aceto–McCoy–Park's definite-filling classification and rational blowdown are
  absent from the repository: `git grep` finds 0 hits for "rational blow", "Aceto", "Wewers" and "prime-degree
  conjecture" outside this lane.
* Z63_PRECEDENT's table was never cross-checked against those classes.

Closed items (z53 brief list, FRONTIER §6) are not redone.

## 3. Z63_PRECEDENT reviewed: missed precedent classes

### 3.1 Method and the omissions

Z63's criteria (P1 pointwise for a prescribed input; P2 polylog or O(1) expected count in the guaranteed window; P3
no identity; P4 unconditional) and its tiers are kept. I checked its rows against the classes named in other
repository files (`DETERMINISTIC_EXISTENCE.md`, `BRAINSTORM/z52_deep_thin_pointwise_*.md`, `TORSION_FIRING.md`) and
against a fresh literature pass. Sources: `data/z64/equiv/sources/precedent_nt.md`, `precedent_comb.md`. Rows marked
✔ I re-read myself from the arXiv record or PDF.

| class (new label) | representative theorem (source, number) | ver. | P1–P4 | count in guaranteed window | where primality / non-squareness enters | in repo elsewhere? |
|---|---|---|---|---|---|---|
| **(Ch) characteristic-p construction + lifting** | Hurwitz existence in prime degree: "Let p be a prime. Every branch datum of degree p satisfying (1.1) is realized by a connected branched cover Σ_g → S²" (Song–Wen–Zhang arXiv:2609.20572v1 Thm 1.1; **claimed, unrefereed**; question of EKS 1984 p. 774, p. 787; verified computationally for p < 32, arXiv:2512.06545) | ✔V | P1 (every prime p, every datum); P3 (no identity; stable reduction in char p, Henrio moments, Wewers lifting); P4 (if correct) | varies with the datum; for rigid genus-0 data the Hurwitz number is O(1) (e.g. the Euclidean family below has ≍ r₂(d)/8 realisations, inferred) | the monodromy group contains a regular C_p, with normaliser C_p ⋊ 𝔽_p^× (SWZ Lemma 2.5); the cover is built in characteristic p. Composite failure: EKS Prop 5.7, for every d = ab the datum {[a,…,a], [b+1,1,…,1], [a, a(b−1)]} is non-realisable (V by the subagent from a scan of EKS, quoted in `precedent_comb.md` §1a; not re-read by me) | **no** (0 hits) |
| (Ch′) prime-exact via norms | Petronio, Winter Braids LN 7 (2020) Thm 3.13: (S², S², d, 3; [2,…,2,1], [4,…,4,1], [4,…,4,1]) realisable iff d = x² + y² with x, y of different parity; Thm 3.14 (x² + xy + y²) | V | P1 at primes ≡ 1 (4); P3 fails (two-squares identity, class (R)) | ≍ r₂(d)/8 (inferred) | Fermat/Gauss representation by a norm form; fails on a density-1 set of composite d | no |
| (Sg) sign / reciprocity forcing | Elkies, Invent. Math. 89 (1987) Thm 1: "Let S be a finite set of primes. Then E has a supersingular prime outside S" | V | P1, P3, P4; fails P2 | power: the window is an iterated exponential (Elkies, Astérisque 198–200 (1991)); best unconditional count π₀(x) ≥ log₃x/(log₄x)^{1+δ} (Fouvry–Murty 1996 Thm 1) against a heuristic ≍ √x/log x | an archimedean sign of P_ℓ(J)P_{4ℓ}(J) < 0 plus (−1/ℓ) = −1 forces an odd number of non-residue prime factors. Needs a real embedding | yes: `TORSION_FIRING.md` §4, upgrades items 271–272; repo verdict "reproduces the genus layer only" |
| (U) unit group + unique factorisation | Legendre: x² − py² = −1 solvable for every prime p ≡ 1 (4) (Niven–Zuckerman–Montgomery §7.8 Ex. 12) | V2 | P1, P4; P3 fails (algebraic); P2 n/a (infinite solution group; one class) | one solution class | (x₀ − 1)(x₀ + 1) = py₀² with p prime admits only two coprime splittings, and minimality kills one. Fails at squares and at composites 205, 221, 305, 377, 505, … (OEIS A031398; recomputed by the subagent) | yes: `DETERMINISTIC_EXISTENCE.md` §4 row 9, z52 β′; absent from Z63's table |
| (H) Minkowski window with O(1) count | Holzer, Canad. J. Math. 2 (1950) 238: solutions with \|x\| < √(bc), \|y\| < √(ca), \|z\| < √(ab) once Legendre's residue conditions hold | V | P1, P2 (O(1): box volume ≍ abc against index abc), P4; P3 borderline (pigeonhole + descent) | O(1) | none: the obstruction is local (Hilbert symbols), not square-type | covered in kind by Z63 A6 (Thue/Minkowski, B4 signed solutions) |
| (RT) realisation theorems | Waterhouse, Ann. Sci. ÉNS 2 (1969) Thm 4.1: for q = p every \|t\| ≤ 2√p is a Frobenius trace | V | P1, P4; P3 fails (CM lifting) | power (≍ H(t² − 4p) ≈ √p) | primality makes "every t" clean (prime powers restrict p \| t) | Deuring: 98 hits, never as a precedent row |
| (FC) finite-criterion universality | 15-theorem (Bhargava, Contemp. Math. 272, Thm 1); 290-theorem (Bhargava–Hanke preprint, Thm 1) | V | P1, P3, P4 (290: unpublished); fails P2 | power (r_Q(n) ≈ n^{1−ε}) | none; needs ≥ 4 variables (ternary forms are never universal) | catalogue tag FIFTEEN only |
| (RG) unipotent rigidity | Oppenheim (Margulis); polynomial rate only for algebraic ternary forms (Lindenstrauss–Mohammadi–Wang–Yang arXiv:2305.18271 Thm 1.1) | V/V2 | P1 (qualitative), P3, P4; fails P2 | power | irrationality of Q | no |
| (EF) Egyptian-fraction Fourier / constructive | Croot, Annals 157 (2003); Bloom (arXiv 2021) Thms 2–3; Liu–Sawhney (arXiv 2024) Thms 1.1–1.3; Graham, J. Austral. Math. Soc. 3 (1963) Thm 1 (every n > 77); Breusch/Stewart (odd denominators; via Graham, Proc. LMS 14 (1964)) | V | P1 for a prescribed set or colouring; P3, P4; fail P2 | exponential / thick | none (density or colour classes) | Croot/Bloom cited 190/172 times, not as Z63 rows |
| (open, H-tier) | Lehmer: τ(n) ≠ 0 (open; verified n < 8.16·10²³, Derickx–van Hoeij–Zeng arXiv:1312.6819 Cor 1.2); Hadamard conjecture (smallest open order 2396 per Egan–Kotsireas–London–Ó Catháin arXiv:2610.27175 §4; V, recent survey, not re-checked by me) | V | — | Lehmer: a *non-existence* conjecture (expected number of zeros finite) | — | Lehmer: Mahler-measure sense only |

*Reading (Assessment).*
* Z63's three literal classes (Sv, S, M2-W) and its comparators (T, R, M4, I) stay correct as far as they go.
* The (Ch) row is the one omission that changes the picture. In literal terms, its P2 status depends on the datum,
  and its proof is a 40-page unrefereed preprint, so it is not entered as a Tier-A pass.
* What matters is its *shape*: "true at every prime, false at every composite by an explicit construction, and proved
  by an argument in which p is the characteristic". Z63 §3.5 records no such shape among the results it reviewed. §3.3
  tests whether it transfers.

### 3.2 The (Ch) precedent in detail (✔ read from arXiv:2609.20572v1 and the API records of 1010.2888, 2512.06545)

* **Statement.** SWZ Thm 1.1, quoted above. The abstract says: "The three-point case is constructed in residue
  characteristic p … Wewers's lifting theorem produces a three-point Galois cover in characteristic zero. The quotient
  by a point stabilizer has degree p and the prescribed three ramification profiles. The fusion and realization
  results of Edmonds–Kulkarni–Stong then give the assertion for an arbitrary number of branch values."
* **Where primality enters.**
  * Lemma 2.5: for P ≤ S_p generated by a p-cycle, C_{S_p}(P) = P and N_{S_p}(P) = P ⋊ 𝔽_p^×.
  * The lifting interface (Thm 4.8) works over an algebraically closed k of characteristic p, with G ≤ S_p,
    p ∥ |G| and a regular subgroup P = C_p.
  * So the degree p is used three ways: as a characteristic, as the order of a regular subgroup, and through the
    affine normaliser.
* **Composite failure.** EKS 1984 p. 774: "If d is not prime, then there exists 𝒟 ∈ A(d) which is not the branch data
  for a connected branched covering of S²" (Prop 5.7). The degree-4 family {[3,1], [2,2], …, [2,2]} is
  non-realisable for every number of branch points.
* **Status.**
  * Pascali–Petronio (arXiv:1010.2888) state it as Conjecture 1.2.
  * Wang et al. (arXiv:2512.06545) verify all primes < 32.
  * SWZ's own introduction records Meng–Wei–Zhou calling it unresolved in May 2026.
  * SWZ acknowledge AI assistance in the initial exploration.

  Treat it as **claimed, unrefereed**. Nothing below depends on its correctness except Lemma H, which is labelled
  CONDITIONAL.
* **Consistency remark (Assessment).** If SWZ is right, then together with Petronio Thm 3.13 it re-proves Fermat's
  two-square theorem for primes p ≡ 1 (4) by p-adic geometry, and Thm 3.14 likewise the x² + xy + y² theorem. That
  is not a contradiction. It shows the (Ch) mechanism is at least as strong as the (R) class on those families.

### 3.3 Push 1: do the prime-exact mechanisms transfer? (Assessment + Lemma H)

These are the verified statements that are true at every prime of a class, false at squares and/or at explicit
infinite sets of composites, and not proved by counting. For each, where does primality enter, and does ES have the
corresponding structure?

| mechanism | object on which primality acts | ES counterpart? |
|---|---|---|
| (Ch) Hurwitz, prime degree | transitive subgroups of S_p contain a regular C_p; a cover over an algebraically closed field of characteristic p is constructed and lifted | the witness of ES is a **ℤ-point**. Over any algebraically closed field (any characteristic) the ES, (★) and Type II varieties have points trivially, so a geometric construction plus lifting yields nothing arithmetic. Hurwitz realisability is finite group theory, ultimately a permutation triple, and that is why geometry over k̄ suffices there |
| (U) Legendre, negative Pell | unique factorisation of (x₀ − 1)(x₀ + 1) = py₀², applied to the fundamental unit (which Pell supplies) | there is no group of ES certificates and no unit-like thick object with an exact factorisation rule. This is the z52 (T)-class gap; `DETERMINISTIC_EXISTENCE.md` §4 shows the Pell splitting factors the discriminant, not 4Cp + 1 |
| (R) two squares / norm forms (also Petronio Thm 3.13) | p splits in ℤ[i] (or ℤ[ω]) and the class number is 1 | R(p) is not a multiplicative representation number, and fixed-level identities fail T1 ((J)7; Z63 A8) |
| (Sg) Elkies | the archimedean sign of one value forces an odd number of non-residue prime factors | it forces only the quadratic (genus) class: "the BM layer is pointwise free" (SYNTHESIS_SPARKS9 Prop 2.2). B2 needs the class inside the coset |
| Wilson / Fermat | (ℤ/p)^× is a field's unit group | identities; barred by B1 for finite menus |

**Lemma H (CONDITIONAL on SWZ Thm 1.1; trivial).** Let (𝒟(d))_{d ≥ 2} be any family of compatible branch data over S²
with deg 𝒟(d) = d. Then the statement "𝒟(p) is realisable ⟺ R(p) ≥ 1, for all primes p ≡ 1 (4)" is false.

*Proof.* By SWZ every 𝒟(p) is realisable, while R(409) = 0 (FRONTIER §2.1, CERTIFIED). ∎

So prime-degree realisability carries no (★) information. A transfer would have to use the *mechanism* (characteristic
p, regular C_p), not the theorem. The table's first row says why the mechanism does not reach ℤ-points.

*Scope of this reading (Assessment).* It does not exclude an ES-equivalent statement about finite groups (for which
geometric methods are natural). Lemma A(c) below is such a statement ("some finite G acts on some X with
|G|/(g − 1) = 2n/(n − 4)"). Its group-theoretic side, however, is a realisation theorem for an arbitrary
signature, so its arithmetic content is again the Egyptian equation (§5, type I). No ES-equivalent statement found
here asks for a group-theoretic object of **prime degree p** whose existence is non-trivial.

### 3.4 Revised gap statement (proposed replacement for Z63 §3.5's last row; Assessment)

Z63's gap statement stands with one amendment. Pointwise existence that is *true at every prime and false on an
explicit infinite set of composites (or of squares)* does occur among verified results, in three ways:
* (Ch) geometric construction in characteristic p, with a claimed 2026 proof;
* (U)/(R) unit groups and norm forms;
* (Sg) sign forcing, at power counts.

In every case primality acts on an **algebraic structure** that has p as its characteristic, its degree or its norm.
None of the results reviewed proves an **arithmetic hit** (a ℤ-point of a moving-modulus divisor event at polylog
count) by an argument that uses primality only through such a structure. B2's cell remains empty.

## 4. The equivalence table (ranked) and proofs

**Ranking.** Rows are ranked by how much a field-native tool could plausibly do. A row ranks higher if the target
field (a) has an active community working on exactly the transported question, and (b) has a non-trivial structure
theory for the transported objects. Pure relabellings rank lowest. "Type" refers to the tool classes of §5:
* I = realisation from data (circular);
* II = universality only after a T1-blind or averaged relaxation;
* III = obstruction-only;
* IV = structure theorem on a canonical p-object.

| rank | ID | equivalence (proved in §4.x) | field | native tool(s) | might / might not apply | type | catalogue |
|---|---|---|---|---|---|---|---|
| 1 | E7 | (W)(n) ⟺ n ∈ d_{A₃}(ℤ³_{≥2}) (Lorenzini's critical polynomial of the path A₃); **(S)(n) ⟺ some x ∈ ℤ³_{≥2} with d_{A₃}(x) = n has critical-group discriminant form ⟨A/n⟩ of Jacobi symbol −1**; CONV-II(n) ⟺ some multiple cn is a formal A₃-value with middle weight ≡ 0 (mod 4c) | graph theory (arithmetical/critical structures) | Lorenzini Prop 6.3 (congruence slices); Wang–Lu EJC 33(3) #P3.80 Thm 5 (density 1 for every graph, via Dirichlet + AP unions) | active published open question ((W) = Lorenzini Ex. 6.2(a)), but the proved tools are fixed-pair slices (HJ_DEEP Lemma 3.2 bars finite coverings) and density | II | HJ_DEEP §3 (W); the pairing reading is new |
| 2 | E6 | (S)(p) ⟺ ∃ q, (q/p) = −1, such that L(p, q) bounds the negative-definite linear plumbing with **three** spheres of Euler numbers ≤ −2 (HJ length 3); its boundary linking form has Legendre class (q/p). **The C = 1 line of (★) = the chains (−v, −4, −u): the middle vertex is configuration (a) of Aceto–McCoy–Park, so these L(p, 4u − 1) are not b₂-minimal.** Relaxation T(p): "∃ q, (q/p) = −1, L(p, q) bounds some smooth negative-definite X with b₂ ≤ 3" satisfies (S)(p) ⟹ T(p); converse unknown | low-dimensional topology | Donaldson diagonalisation, Heegaard Floer d-invariants, Lisca (b₂ = 0), Greene changemakers, AMP / Fung–Park forbidden configurations | all are **obstructions** (non-existence) or classifications of minimality; existence comes from Kirby constructions, i.e. from words. Lisca is the topological mirror of T1 (rational balls exist only over squares) | III | DEDEKIND_ES, bsA_lens_*; the AMP / rational-blowdown reading is new |
| 3 | E1 | (★)(p) ⟺ p is the largest integer having exactly k representations by some numerical semigroup ⟨u, B⟩ with k ≡ 3 (mod 4) (generalised Frobenius number g_k = (k+1)uB − u − B) | numerical semigroups | Beck–Robins Thm 3; Popoviciu; inverse theorems (Rosales et al., Math. Scand. 94 (2004) Thm 1.11: every g is a 3-generator Frobenius number; odd g = F(2, g + 2)) | inverse results exist but only for relaxed shapes (3 generators, or k = 0); none controls k mod 4 | II | Z0394–Z0402 |
| 4 | E3 | **Lemma A:** for every odd n ≥ 5, ES(n) ⟺ 4/n − 1 is the Euler characteristic of a closed orientable 2-orbifold ⟺ ∃ compact Riemann surface X (g ≥ 2) and finite G ≤ Aut(X) with \|G\|(n − 4) = n(2g − 2) | Riemann surfaces, Fuchsian groups | Riemann existence, Selberg's lemma / Fox, Kulkarni genus spectrum | realisation needs the signature, which is an Egyptian representation | I | Z0171, Z0417 (forms); Lemma A with the r = 4, 5 analysis is new |
| 5 | E4 | ES(n) ⟺ 4/n = lct₀(x^a + y^b + z^c) for some a, b, c ≥ 1 (n ≥ 5) | singularity theory / birational geometry | Kollár (16.1), (3.2); ACC (Hacon–McKernan–Xu); Kuwata, Prokhorov | the full lct question is trivially true: 4/n ∈ lct(ℂ²) for all n ≥ 6 (Lemma R(b)); ES is the diagonal stratum, about which the field says nothing pointwise | II | Z0155 |
| 6 | E11 | (★)(p) ⟹ ∃ N and a quotient y^N = t^α(1 − t)^β of the Fermat curve F_N with three branch points of ramification indices (x, y, z), 1/x + 1/y + 1/z = 4/p (genus 1 + uBC(p − 4)/2) ⟹ ES(p). **(★) triples are lcm-balanced and always cyclically realisable** (Lemma F) | arithmetic geometry (Fermat curves, cyclic covers) | Jacobi sums / Weil for the Jacobians; genus formula | the genus formula is the only link; point counts are irrelevant to existence | I | Z0417 neighbourhood; Lemma F is new |
| 7 | E8 | (★)(n) ⟺ n is the upper-right entry of T^u(−L^{−4C})T^B (u, B, C ≥ 1) ⟺ ∃ γ = [[a, n], [c, d]] ∈ SL₂(ℤ), c ∈ 4ℕ, a, d ≥ 1, a ≡ −1 (mod c) ⟺ the Anosov map γ of T² sends the c-torsion point (1/c, 0) to its negative, c being its own lower-left entry | dynamics / Farey / SL₂(ℤ) | Farey graph, periodic orbits of cat maps, Ghys–Rademacher linking | SL₂(ℤ) structure is p-blind; the tied modulus (c is an entry of γ) is B2 verbatim | I | FRONTIER §2.1 SL₂ form; Z63_EUCLID |
| 8 | E5 | ES(n) ⟺ ∃ x, y, z ≥ 1 with n·det P(x, y, z) = 4xyz (pretzel link) ⟺ the Seifert fibred double branched cover M(0; (x,1), (y,1), (z,1)) has rational Euler number of absolute value 4/n | knot theory / Seifert manifolds | determinant, signature, Montesinos classification | invariants are computed from (x, y, z) | I | Seifert: 61 mentions; no row |
| 9 | E2 | (★)(p) ⟺ O(p) ≅ ω ⊗ π*O_{ℙ¹}(4C) on the stacky line ℙ(u, B) | algebraic geometry of stacks | Riemann–Roch / Serre duality (denumerant symmetry) | a degree identity | I | Z0418 |
| 10 | E9 | (★)_C(n) ⟺ 4Cn + 1 has a divisor in the ray class of complex conjugation in Cl_{4C·∞}(ℚ) ≅ Gal(ℚ(ζ_{4C})/ℚ) ⟺ a sub-multiset of the Frobenius elements of its prime factors multiplies to complex conjugation | algebraic NT (CFT) | Chebotarev, CFT existence | moving field ℚ(ζ_{4C}); the genus layer is free and the class layer is B2 | IV (covered) | Z62_INVERSEF; Z60_RAYCLASS |
| 11 | E10 | for p ≡ 1 (4) and C = c²: (★)_{c²}(p) ⟺ some ideal 𝔞 \| (1 + 2c√−p) of ℤ[√−p] has N𝔞 ≡ −1 (mod 4c²) | algebraic NT (imaginary quadratic fields) | class group of ℚ(√−p), Heegner/CM | ideal divisors of one principal element; no class-group input enters | IV (covered) | Z60_RAYCLASS §6 (S₁, square t₀) |
| 12 | E12 | R_t(n) = coefficient of a Kronecker theta quotient (Thm K) | modular / q-series | modularity, Hecke-type double sums, Serre–Stark | single-coefficient positivity is not available | II | METAPLECTIC_ES; Z1681 |
| 13 | E13 | ES(n) ⟺ ∃ three-point branched cover of S² with uniform branch data (x, y, z) and (2g − 2)/N = 1 − 4/n | Hurwitz problem / dessins | Riemann existence; Hurwitz existence theory | uniform data = signature (Lemma A). The **prime-degree** theorem is about degree p, not about 4/p (Lemma H) | I | Z0171, Z0417 |
| 14 | E14 | if ES is true, ES-SEARCH ∈ TFNP; a syntactic class membership (PPA / PPP / PLS) would be a proof of totality | complexity | parity, pigeonhole, potential principles | reduces to Z62 (parity), Z61 (pigeon, transport) | — | z31_complexity |

### 4.1 Proofs (all PROVED unless labelled; sanity checks `scripts/z64_equiv_checks.py` → `data/z64/equiv/checks.txt`, 0 failures)

**E1 (k-Frobenius).**
* For coprime u, B ≥ 1, the largest integer with exactly k ≥ 0 representations N = xu + yB (x, y ≥ 0) is
  g_k(u, B) = (k + 1)uB − u − B. Sources: Beck–Robins arXiv:math/0204037 Thm 3; Beck–Kifer, Integers 11 (2011) A24
  Thm 1 (with "exactly" = "at most"). Both V by subagent. Brute-force check (i): u, B ≤ 13, k ≤ 6, 805 cases.
* With k = 4C − 1 this is 4CuB − u − B, which is the (★) shape.
* For a prime p every (★) solution has gcd(u, B) = 1. Indeed gcd(u, B) divides 4uBC − u − B = p, and gcd = p would
  force u, B ≥ p, hence 4uBC − u − B ≥ 4p² − 2p·… > p. So (★)(p) ⟺ ∃ coprime (u, B) and k ≡ 3 (mod 4) with
  p = g_k(u, B). ∎
* Inverse results: every positive g is the Frobenius number of some ⟨n₁, n₂, n₃⟩ (Rosales et al. Thm 1.11), and every
  odd g = F(2, g + 2). Both hold at every odd square: they are input-blind relaxations (§5 type II).

**E2.** On ℙ(u, B) (u, B coprime) one has Pic = ℤ·O(1), ω ≅ O(−u − B) and π*O_{ℙ¹}(1) ≅ O(uB). Hence
O(p) ≅ ω ⊗ π*O(4C) ⟺ p = 4CuB − u − B. ∎ (Catalogue Z0418; a degree identity.)

**E3 = Lemma A.** For every odd n ≥ 5 the following are equivalent:
* (a) ES(n);
* (b) 4/n − 1 = χ^orb(O) for some closed orientable 2-orbifold O;
* (c) ∃ compact Riemann surface X of genus g ≥ 2 and finite G ≤ Aut(X) with |G|(n − 4) = n(2g − 2).

*Proof.*
* **(b) ⟺ (c).** If G acts on X then χ(X) = |G|·χ^orb(X/G) (Riemann–Hurwitz), so (c) gives χ^orb = −(n − 4)/n.
  Conversely, a closed orientable 2-orbifold with χ^orb < 0 is ℍ/Γ for a cocompact Fuchsian group Γ. Γ has a
  torsion-free normal subgroup Γ′ of finite index (Selberg's lemma; Fox for triangle groups). Then X = ℍ/Γ′ and
  G = Γ/Γ′ give (c).
* **(a) ⟹ (b).** S²(x, y, z) has χ^orb = 1/x + 1/y + 1/z − 1. Cone orders equal to 1 are omitted.
* **(b) ⟹ (a).** A genus-h orbifold with cone orders m_i ≥ 2 has χ = 2 − 2h − Σ(1 − 1/m_i). Setting χ = 4/n − 1:
  * h ≥ 2 is impossible.
  * h = 1 needs Σ(1 − 1/m_i) = 1 − 4/n. This fails for r = 0 and for r = 1 (it would need m = n/4), for r = 2
    (1/m₁ + 1/m₂ = 1 + 4/n > 1) and for r ≥ 3 (the sum is ≥ 3/2).
  * h = 0 gives Σ1/m_i = r − 3 + 4/n. Then r ≤ 2 is impossible, r = 3 is ES, and r ≥ 6 is impossible.
  * r = 5: Σ₅ > 2 forces three m_i = 2 and 1/m₄ + 1/m₅ = 1/2 + 4/n. The only solutions have n even:
    n = 4m₅, 24, 48, 120.
  * r = 4, sorted: write s = 1/m₁ + 1/m₂ + 1/m₃ − 1, so 1/m₄ = 4/n − s. If (m₁, m₂) = (2, 2) then 4/n = 1/m₃ + 1/m₄,
    and ES(n) follows by splitting 1/m₄ = 2·1/(2m₄). Otherwise:
    * if s > 0, the triple is (2, 3, 3), (2, 3, 4) or (2, 3, 5), with n < 4/s ≤ 120;
    * if s = 0, then n = 4m₄ is even;
    * if s < 0, then m₄ < 1/|s|. Here 4/m₁ > 1, 1/m₁ + 3/m₂ > 1 and 1/m₁ + 1/m₂ + 2/m₃ > 1 bound m₁ ≤ 3, m₂ ≤ 5,
      m₃ ≤ 11, so finitely many cases.

    The exhaustive enumeration (`scripts/z64_equiv_orbifold.py`, exact Fractions, CERTIFIED) gives the odd n
    {15, 21, 23, 39, 45, 47, 75, 95, 105, 111, 115, 117, 119, 165, 273}. ES holds at each of them (Salez, < 10¹⁷;
    e.g. 105: 4/105 = 1/27 + 1/945 + … is not needed, any census suffices).

∎ *Corollary.* For primes p ≡ 1 (4) only r = 3 occurs: 4/p is never a two-term Egyptian fraction, and no such p
lies in the sporadic list. So (c) is ES(p) on the nose.

**E4.** Kollár, arXiv:0805.0756 (16.1) (V by subagent): c₀(x^a + y^b + z^c) = min{1, 1/a + 1/b + 1/c}. For n ≥ 5,
4/n < 1, so ES(n) ⟺ 4/n = c₀(x^a + y^b + z^c) for some a, b, c ≥ 1. ∎ The relaxation is Lemma R(b) in §6.

**E5.** Let x, y, z ≥ 1. The pretzel link P(x, y, z) is the Montesinos link M(0; 1/x, 1/y, 1/z). Its double branched
cover is the Seifert fibred space M over S² with unnormalised invariants (x, 1), (y, 1), (z, 1) and b = 0, and its
rational Euler number e has |e| = 1/x + 1/y + 1/z. Since |H₁(M)| = |e|·xyz when e ≠ 0, det P(x, y, z) =
|H₁(M)| = xy + yz + zx. Hence n·det P = 4xyz ⟺ 1/x + 1/y + 1/z = 4/n. ∎ (Standard Seifert/Montesinos facts, stated
without a theorem number. This is a relabelling.)

**E6.**
* (i) For p/q = [[a₁, …, a_k]] (all a_i ≥ 2), L(p, q) bounds the negative-definite linear plumbing X(p, q) with
  Euler numbers −a_i, and b₂ = k. This is the standard fact recalled in Aceto–McCoy–Park arXiv:2208.02586 §1 (✔ read).
* (ii) For the word p/A = [[v, t, u]]: v − 1/(t − 1/u) = (tuv − u − v)/(tu − 1), so A = tu − 1.
* (iii) The Gram matrix M of E7 has (M⁻¹)₁₁ = A/p. So the linking form of L(p, A) on ℤ/p is ±A x²/p, whose isometry
  class for p ≡ 1 (4) is the Legendre class (A/p).

Hence (S)(p) ⟺ ∃ q with (q/p) = −1 and len(p/q) = 3, i.e. L(p, q) = ∂X(p, q) with b₂ = 3.

* **C = 1 line.** The (★) words with C = 1 are exactly the length-3 chains with middle weight 4, i.e. plumbings
  (−v, −4, −u). AMP Thm 1.1(iii)(a) is the single vertex of weight −4, and its (iv) lists X(4, 1). So these L(p, A)
  admit negative-definite fillings with b₂(X) < 3 (✔ read).
* **Relaxation T(p).** (S)(p) ⟹ T(p) is immediate from the plumbing. The converse would need every negative-definite
  b₂ ≤ 3 filling of a lens space with non-residue q to come from a ≤ 3-chain. That is not known; AMP characterise only
  when the canonical plumbing is minimal.
* **Native tools** (Donaldson, d-invariants, Lisca, AMP, Fung–Park) are obstructions or minimality criteria. Lisca's
  theorem (Geom. Topol. 2007, Thm 1.2, V by subagent: L(p, q) bounds a rational ball iff p/q ∈ ℛ, which forces
  p = m²) is the topological mirror image of T1: at squares, *rational balls* exist, while (★)-chains do not.

**E7.**
* d_{A₃}(x, y, z) := det(Diag(x, y, z) − A_{A₃}) = xyz − x − z. This is Lorenzini's critical polynomial (arXiv:2311.06367
  Ex. 6.2(a), V by subagent; HJ_DEEP §3 ✔ in-repo). (W)(n) ⟺ n ∈ d_{A₃}(ℤ³_{≥2}) by definition.
* For M = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (det n), the 2×2 minor on rows {1, 2} and columns {2, 3} is
  det [[−1, 0], [t, −1]] = 1. So coker M ≅ ℤ/n is cyclic.
* (M⁻¹)₁₁ = (tu − 1)/n = A/n (check (iv): 53 518 words). When gcd(A, n) = 1, e₁ has discriminant value A/n of order n.
  So e₁ generates, and the discriminant form is q(k·e₁) = k²A/n (mod 1).
* Hence (S)(n) ⟺ some x with d_{A₃}(x) = n has critical-group discriminant form of Jacobi symbol (A/n) = −1. The
  symbol does not depend on the generator, since (A/n) = (A*/n) by HJ_DEEP Prop 4.1.
* CONV-II and U₇ in this language. By HJ_DEEP Prop 2.1, Type II solutions at n are formal words K(a, 4cd, b) = cn
  (letters a, b ≥ 1). So CONV-II(n) ⟺ ∃ c ≥ 1 such that cn is a formal A₃-value with middle weight ≡ 0 (mod 4c).
  U₇(n) ⟺ such a word has 8 | xy (Z60_LOPEZ Lemma 7; quoted, not re-proved).

∎

**E8.**
* With T = [[1, 1], [0, 1]], L = [[1, 0], [1, 1]] and c = 4C: T^u(−L^{−c})T^B = [[cu − 1, cuB − u − B], [c, cB − 1]]
  (check (ii): 10 632 solutions).
* Conversely, if γ = [[a, n], [c, d]] ∈ SL₂(ℤ) with c ∈ 4ℕ, a ≥ 1 and a ≡ −1 (mod c), then ad ≡ 1 forces d ≡ −1, and
  T^{−(a+1)/c} γ T^{−(d+1)/c} = [[−1, 0], [c, −1]]. This recovers (u, B) = ((a + 1)/c, (d + 1)/c), both ≥ 1.
* On T² = ℝ²/ℤ², γ(1/c, 0)ᵀ = (a/c, 1) ≡ (a/c, 0), which equals −(1/c, 0) iff a ≡ −1 (mod c).

∎

**E9.**
* d ↦ Frob_d identifies (ℤ/4C)^× with Gal(ℚ(ζ_{4C})/ℚ), and d ≡ −1 ⟺ Frob_d = complex conjugation.
* Frobenius is multiplicative on divisors. So 4Cn + 1 has a divisor ≡ −1 (mod 4C) iff some sub-multiset of its prime
  factors (with multiplicity) has Frobenius product equal to complex conjugation.

∎ (Z62_INVERSEF's arrangement form.)

**E10.**
* For p ≡ 1 (4), ℤ[√−p] is the maximal order of ℚ(√−p) (discriminant −4p).
* α = 1 + 2c√−p is primitive, i.e. divisible by no rational integer > 1, and N(α) = 4c²p + 1 is odd and ≢ 0 (mod p).
  So every prime ℓ | N(α) is unramified. An inert ℓ would divide α, so ℓ splits as 𝔩𝔩̄, and exactly one of 𝔩, 𝔩̄
  divides (α), with exponent v_ℓ(N(α)).
* Hence 𝔞 ↦ N𝔞 is a bijection from ideal divisors of (α) onto positive divisors of N(α), and the (★)_{c²} condition
  transports. ∎

**E11 = Lemma F.** Let p be prime and (u, B, C) a (★) solution, with (x, y, z) = (uBC, pBC, puC) and N = puBC.
* (a) lcm(x, y) = lcm(y, z) = lcm(z, x) = N.
* (b) There are a, b, c ∈ ℤ/N with a + b + c = 0, gcd(a, N) = N/x = p, gcd(b, N) = N/y = u and gcd(c, N) = N/z = B.
  Hence the cyclic cover y^N = t^a(1 − t)^b of ℙ¹ (a quotient of the Fermat curve F_N) has ramification indices
  x, y, z over 0, 1, ∞, and 2g − 2 = N(1 − 4/p) = uBC(p − 4).

*Proof.*
* (a) gcd(u, B) = 1 (E1), and p ∤ uBC since u, B, C < p. Then lcm(uBC, pBC) = BC·lcm(u, p) = N, and the other two
  pairs are the same.
* (b) is solved by CRT one prime ℓ | N at a time, with e = v_ℓ(N):
  * ℓ = p (e = 1): take a ≡ 0, b ≡ 1, c ≡ −1.
  * ℓ | u (so ℓ ∤ pB), f = v_ℓ(u): take b ≡ ℓ^f (or 0 if f = e), a ≡ 1, c ≡ −1 − b, which is a unit. The case
    ℓ | B is symmetric.
  * ℓ | C only: three units summing to 0 exist iff ℓ is odd. But ℓ = 2 always divides uB, since u + B ≡ p (mod 2)
    is odd.
* The genus follows from Riemann–Hurwitz with e_i = x, y, z.

∎ (Check (iii): all 1998 (★) solutions at primes p ≡ 1 (4), p ≤ 3000.)

*Conversely,* any three-point cover with uniform ramification (x, y, z) and (2g − 2)/N = 1 − 4/p gives ES(p). So
(★)(p) ⟹ Φ_Fermat(p) ⟹ ES(p).

**E12–E14.** These are quoted from the cited memos and not re-proved.

