# Z64_EQUIV — statements equivalent to ES-at-primes / (MS) / U₇ / (S) / CONV-II in other fields (wave z64, lane EQUIV)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results; internal review, an Opus stand-in cross-review and an Astra retro cross-model
review (fixes applied, §8). Brief: `z52bbriefs/z64_lanes.md` §EQUIV (+ z58 common
rules, z53 depth brief). Scripts `scripts/z64_equiv_*`, data `data/z64/equiv/` (source excerpts with URLs, theorem numbers
and access dates in `data/z64/equiv/sources/*.md`, gathered by three research subagents; decisive items re-read by me,
marked ✔).

**Verdict: narrowed.** No HOT LEAD. One genuinely new precedent class for the Z63 catalogue (prime-degree Hurwitz
existence, a claimed 2026 theorem proved in residue characteristic p), a dictionary of fourteen cross-field rows (ten
proved equivalences, one proved implication chain, three quoted rows) with their native tools screened, and a scoped explanation of why every *formula-level* dictionary is
circular.

## 0. Bottom line

1. **Z63_PRECEDENT missed one precedent class with a prime/composite shape analogous to ES's** (an analogy, not an
   identity: ES itself has no square obstruction; the restricted certificate predicates R, (★) do, and R(p) even has
   exceptional primes). It is the Hurwitz
   existence problem in prime degree (§3.2, ✔). Every compatible branch datum of degree p over S² is realisable:
   * Edmonds–Kulkarni–Stong asked this in 1984 (Trans. AMS 282, p. 774, p. 787).
   * Song–Wen–Zhang claim a proof (arXiv:2609.20572, Thm 1.1, Sep 2026, unrefereed). Their mechanism is
     **construction in residue characteristic p followed by lifting**. Primality enters through the regular subgroup
     C_p ≤ S_p (their Lemma 2.5).
   * For **every** composite degree there is an explicit non-realisable datum (EKS Prop. 5.7; V by subagent from a
     scan; independently confirmed computationally by the cross-model reviewer for every factorisation d = ab, d ≤ 12).
   * Some families are realisable exactly at the degrees x² + y² (Petronio's survey, Thm 3.13). These contain all
     primes ≡ 1 (4) and fail on a density-1 set of degrees.
   Z63 also omitted classes that the repository knows elsewhere: Elkies-type sign forcing, Legendre's negative Pell,
   realisation theorems (Deuring–Waterhouse) and finite-criterion universality (15/290). The Holzer/Minkowski O(1)
   window is a sharper row of a class Z63 already has (A6). §3.1 tabulates them with sources.
2. **None of the prime-exact mechanisms transfers** (§3.3; Assessment, with one CONDITIONAL lemma). Each uses
   primality at a step ES has no counterpart for:
   * a geometric statement over an algebraically closed field of characteristic p (Hurwitz);
   * a group of units plus unique factorisation (Pell, two squares);
   * an archimedean sign of one value (Elkies).

   ES needs a ℤ-point (an arithmetic witness). Lemma H (CONDITIONAL on the SWZ theorem): no family of branch data has
   prime-degree realisability equivalent to R(p) ≥ 1. The revised gap statement is in §3.4.
3. **Fourteen dictionary rows** (§4): ten equivalences proved with exact quantifiers (E1–E10), one proved
   implication chain (E11) and three quoted rows (E12–E14). They span:
   * numerical semigroups (k-Frobenius numbers);
   * stacky curves;
   * Riemann surfaces and 2-orbifolds (Lemma A: ES(n) ⟺ some (X, G) has |G|(n − 4) = n(2g − 2), for every odd
     n ≥ 5. The statement for hyperbolic 2-orbifolds is Ian Agol's comment on MathOverflow 267209 (Z0153). New here: the
     proof of the all-signature direction, with its 15 sporadic odd n, and the standard form (c));
   * singularity theory (lct);
   * pretzel links and Seifert manifolds;
   * lens spaces and definite fillings (new: the (★) chains whose canonical plumbing is not b₂-minimal in the sense
     of Aceto–McCoy–Park are exactly those with C = 1, a *middle* (−4) vertex, or u = 4 or B = 4, an end (−4)
     vertex);
   * Lorenzini's critical polynomial (the critical-group discriminant form *is* the (S) sign);
   * SL₂(ℤ), Farey edges and toral automorphisms;
   * cyclotomic Frobenius classes and ℤ[√−p] ideals;
   * Fermat-curve quotients (new: (★) triples are lcm-balanced and always cyclically realisable);
   * q-series;
   * TFNP.
   Each comes with its catalogue ID where one exists (`ES_CONNECTIONS_TODO.md`).
4. **Why they are circular** (§5; Assessment, with two PROVED pieces: the type-I observation and Lemma R). Every
   native existence tool met falls into one of four types:
   * (I) realisation from parameter data: the data are the certificate;
   * (II) universality or density theorems, which hold only after a relaxation that is T1-blind or averaged
     (Lemma R: each proved relaxation holds at odd squares or is only an average);
   * (III) obstruction theorems, which give non-existence only;
   * (IV) structure theorems on a canonical p-object, which are the only non-circular type. All the instances known
     to the repo are already screened.

   An escaping equivalence must have type (IV), with a structure theorem that sees primality.
5. **FRONTIER §4 screens** (§6): every row inherits T1 / 8/131 / composite behaviour verbatim, so the screens bite on
   tools. All type-(I)–(III) tools fail "fixed p, non-circular". The type-(IV) candidates are those of Z63_EUCLID /
   RAYCLASS / supersingular memos, unchanged.
6. **Single-prime push on the top rows E6/E7** (§5.1; classical theorems plus an exact check on 9.9·10⁶ words). The
   best topological invariant of L(p, A), the Dedekind sum / Rokhlin invariant, reduces the (S) sign to fixed mod-4
   cells of the plumbing weights. This re-derives DK Thm 4.5 and leaves the five-slice existence problem untouched.
   Negative, as predicted.

## 1. Mandatory falsifier table (F1–F4; data `data/z58/screens/`)

An *equivalence* is the same statement in other coordinates, so it inherits F1–F4 verbatim — but only inside its
proved domain and for its own target. The prime-only rows E1, E2, E10 (and E6, E11 at primes) are not established
equivalences at composites, so their composite-screen cells describe the native tools, not an inherited statement. The screens therefore bite
on the **native tool** of the target field. Column entries say what the field's best native tool does on each screen.

Convention for the cells: a "type I" tool needs the certificate as input, so on every screen it returns exactly the
truth value of the target, with no independent force. "blind" means the tool's hypotheses do not depend on the
screened property, so applied verbatim it would prove the target on the screened set too, where the target is false.

| row (§4) | F1 odd squares | F2 C-even / 8/131 | F3 composites (285 R-zeros; Z₇; 4545) | F4 known zeros (14 (★), 38 𝔊*) | verdict |
|---|---|---|---|---|---|
| E1 k-Frobenius | inverse theorems (Rosales Thm 1.11; odd g = F(2, g+2)) hold at m²: blind (Lemma R(c)) | no inverse theorem controls k mod 4, let alone the parity of C = (k+1)/4 | inverse theorems are primality-blind | no tool output distinguishes them | circular / relaxation (II) |
| E3 orbifold χ, Aut(X) | ES has no T1, so nothing to screen; the (★)-version would need the signature (uBC, pBC, puC) = certificate | numerator 8: the same Lemma A for 8/n (casework changes only in r = 4, 5) | Selberg's lemma is input-blind | type I | circular (I) |
| E4 lct | 4/m² ∈ lct(ℂ²): blind (Lemma R(b)) | the diagonal stratum for 8/131 is empty (8/131 has no 3-term representation), but the full lct statement holds there: blind | blind | blind | relaxation (II) |
| E5 pretzel / Seifert | invariants are computed from (x, y, z) | type I | type I | type I | circular (I) |
| E6 lens space / plumbing | statement-level: no Jacobi −1 class at m². Tools (Donaldson, d, Lisca, AMP) are obstructions; Lisca's rational balls *exist* at squares | the AMP non-minimality locus is C = 1 or 4 ∈ {u, B} (C otherwise arbitrary); it does not separate C even from C odd | obstruction tools are not primality-specific | no obstruction applies to an absent chain | obstruction (III) |
| E7 Lorenzini (W)/(S) | (W) holds at m² for 3 ∤ m (PROVED) and for all odd 25 ≤ m² < 10⁹ (census, EVIDENCE): blind. Wang–Lu density is averaged | the critical-group sign law (A/p) = −(−1/p) on Type II words is numerator-blind | (W) holds at 284 of the 285 supplied composite R-zeros and fails at 105, so the (W) tools are blind on most (not all) of that screen | blind | relaxation (II) |
| E8 SL₂ / Farey / cat map | SL₂(ℤ) structure is p-blind | type I | type I | type I | circular (I) |
| E9–E10 ray class / ℤ[√−p] | genus layer free (SPARKS9 Prop 2.2); class-level forcing not available | covered in RAYCLASS | covered | covered | covered (IV) |
| E11 Fermat quotients | genus formula only | type I | type I | type I | circular (I) |
| E12 q-series | Thm K is T1-exact; single-coefficient positivity is not available | covered (AUTOMORPH) | covered | covered | covered |
| E13 Hurwitz / dessins | uniform data = signature | type I | type I | type I | circular (I) |
| E14 TFNP | a syntactic totality proof is a parity / pigeonhole / potential argument (Z62 P0, Z61) | covered | covered | covered (Z62: uniform parity refuted by the 14 zeros) | covered |
| §3.3 Hurwitz prime degree (precedent) | composite degrees fail (EKS 5.7); ES itself has no square failures, and the square failures of the restricted predicates (R, (★)) have no Hurwitz counterpart | — | Lemma H: prime-degree realisability carries no (★) information (CONDITIONAL) | R(409) = 0 while every degree-409 datum is realisable (SWZ) | no transfer |

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
  * Frobenius numbers (Z1970), Brieskorn–Pham lct (Z0155), Hurwitz existence (Z0171), dessins (Z0167, Z1922),
    pretzel/Seifert (Z0158);
  * weighted projective lines (Z1991), Lorentzian polynomials (Z2606);
  * plumbings / lens spaces (DEDEKIND_ES, bsA_*), Lorenzini (HJ_DEEP), SL₂ / Farey (Z63_EUCLID), TFNP (z31).

  Most of these were never *proved* as equivalences with exact quantifiers. The z52d avenue layer judged them
  "circular" item by item, without a stated reason.
* The prime-degree Hurwitz theorem, Aceto–McCoy–Park's definite-filling classification and rational blowdown are
  absent from the repository: `git grep` finds 0 substantive hits for "rational blow", "Aceto", "Wewers" and
  "prime-degree conjecture" outside this lane. (One stray substring match for "Aceto" in a JSON file; one citation
  of Obus–Wewers in `sources/lorenzini/`.)
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
| **(Ch) characteristic-p construction + lifting** | Hurwitz existence in prime degree: "Let p be a prime. Every branch datum of degree p satisfying (1.1) is realized by a connected branched cover Σ_g → S²" (Song–Wen–Zhang arXiv:2609.20572v1 Thm 1.1; **claimed, unrefereed**; question of EKS 1984 p. 774, p. 787; verified computationally for p < 32, arXiv:2512.06545) | ✔V | P1 (every prime p, every datum); P3 (no identity; stable reduction in char p, Henrio moments, Wewers lifting); P4 (if correct) | varies with the datum and is **not** O(1) in general, even for three-branch-value genus-0 data: for p = 4a + 1 prime the passport ([3ᵃ, 1ᵃ⁺¹], [2²ᵃ, 1], [p]) has Catalan(a) realisations (Astra retro review: rooted plane full binary trees, edges subdivided); the Euclidean family below has ≍ r₂(d)/8 (inferred). No P2 pass is claimed | the monodromy group contains a regular C_p, with normaliser C_p ⋊ 𝔽_p^× (SWZ Lemma 2.5); the cover is built in characteristic p. Composite failure: EKS Prop 5.7, for every d = ab the datum {[a,…,a], [b+1,1,…,1], [a, a(b−1)]} is non-realisable (V by the subagent from a scan of EKS, quoted in `precedent_comb.md` §1a; independently confirmed computationally by the cross-model reviewer for d ≤ 12) | **no** (0 hits) |
| (Ch′) prime-exact via norms | Petronio, Winter Braids LN 7 (2020) Thm 3.13: (S², S², d, 3; [2,…,2,1], [4,…,4,1], [4,…,4,1]) realisable iff d = x² + y² with x, y of different parity; Thm 3.14 (x² + xy + y²) | V | P1 at primes ≡ 1 (4); P3 fails (two-squares identity, class (R)) | ≍ r₂(d)/8 (inferred) | Fermat/Gauss representation by a norm form; fails on a density-1 set of composite d | no |
| (Sg) sign / reciprocity forcing | Elkies, Invent. Math. 89 (1987) Thm 1: "Let S be a finite set of primes. Then E has a supersingular prime outside S" | V | P1, P3, P4; fails P2 | power: the window is an iterated exponential (Elkies, Astérisque 198–200 (1991)); best unconditional count π₀(x) ≥ log₃x/(log₄x)^{1+δ} (Fouvry–Murty 1996 Thm 1) against a heuristic ≍ √x/log x | an archimedean sign of P_ℓ(J)P_{4ℓ}(J) < 0 plus (−1/ℓ) = −1 forces an odd number of non-residue prime factors. Needs a real embedding | yes: `TORSION_FIRING.md` §4, upgrades items 271–272; repo verdict "reproduces the genus layer only" |
| (U) unit group + unique factorisation | Legendre: x² − py² = −1 solvable for every prime p ≡ 1 (4) (Niven–Zuckerman–Montgomery §7.8 Ex. 12) | V2 | P1, P4; P3 fails (algebraic); P2 n/a (infinite solution group; one class) | one solution class | (x₀ − 1)(x₀ + 1) = py₀² with p prime admits only two coprime splittings, and minimality kills one. Fails at squares and at composites 205, 221, 305, 377, 505, … (OEIS A031398; recomputed by the subagent) | yes: `DETERMINISTIC_EXISTENCE.md` §4 row 9, z52 β′; absent from Z63's table |
| (H) Minkowski window with O(1) count | Holzer, Canad. J. Math. 2 (1950) 238: solutions with \|x\| < √(bc), \|y\| < √(ca), \|z\| < √(ab) once Legendre's residue conditions hold | V | P1, P2 (O(1): box volume ≍ abc against index abc), P4; P3 borderline (pigeonhole + descent) | O(1) | none: the obstruction is local (Hilbert symbols), not square-type | covered in kind by Z63 A6 (Thue/Minkowski, B4 signed solutions) |
| (RT) realisation theorems | Waterhouse, Ann. Sci. ÉNS 2 (1969) Thm 4.1: for q = p every \|t\| ≤ 2√p is a Frobenius trace | V | P1, P4; P3 fails (CM lifting) | power (≍ H(t² − 4p) ≈ √p) | primality makes "every t" clean (prime powers restrict p \| t) | Deuring: 98 hits, never as a precedent row |
| (FC) finite-criterion universality | 15-theorem (Bhargava, Contemp. Math. 272, Thm 1); 290-theorem (Bhargava–Hanke preprint, Thm 1) | V | P1, P3, P4 (290: unpublished); fails P2 | power (r_Q(n) ≈ n^{1−ε}) | none; needs ≥ 4 variables (ternary forms are never universal) | catalogue tag FIFTEEN only |
| (RG) unipotent rigidity | Oppenheim (Margulis); polynomial rate only for algebraic ternary forms (Lindenstrauss–Mohammadi–Wang–Yang arXiv:2305.18271 Thm 1.1) | V/V2 | P1 (qualitative), P3, P4; fails P2 | power | irrationality of Q | no |
| (EF) Egyptian-fraction Fourier / constructive | Croot, Annals 157 (2003); Bloom (arXiv 2021) Thms 2–3; Liu–Sawhney (arXiv 2024) Thms 1.1–1.3; Graham, J. Austral. Math. Soc. 3 (1963) Thm 1 (every n > 77); Breusch/Stewart (odd denominators; via Graham, Proc. LMS 14 (1964)) | V (Breusch/Stewart V2) | P1 for a prescribed set or colouring; P3, P4; fail P2 | exponential / thick | none (density or colour classes) | Croot/Bloom cited 190/172 times, not as Z63 rows |
| (open, H-tier) | Lehmer: τ(n) ≠ 0 (open; verified n < 8.16·10²³, Derickx–van Hoeij–Zeng arXiv:1312.6819 Cor 1.2); Hadamard conjecture (smallest open order 2396 per Egan–Kotsireas–London–Ó Catháin arXiv:2610.27175 §4; V, recent survey, not re-checked by me) | V | — | Lehmer: a *non-existence* conjecture (expected number of zeros finite) | — | Lehmer: Mahler-measure sense only |

*Reading (Assessment).*
* Z63's three literal classes (Sv, S, M2-W) and its comparators (T, R, M4, I) stay correct as far as they go.
* The (Ch) row is the one omission that changes the picture. In literal terms, its P2 status depends on the datum,
  and its proof is a 40-page unrefereed preprint, so it is not entered as a Tier-A pass.
* What matters is its *shape*: "true at every prime, false at every composite by an explicit construction, and proved
  by an argument in which p is the characteristic". This is an analogy with ES's restricted predicates, not ES's own
  shape (ES has no known failure at all). Z63 §3.5 records no such shape among the results it reviewed. §3.3
  tests whether it transfers.

### 3.2 The (Ch) precedent in detail (✔ read from arXiv:2609.20572v1 and the API records of 1010.2888, 2512.06545)

* **Statement.** SWZ Thm 1.1, quoted above. The abstract says: "The three-point case is constructed in residue
  characteristic p … Wewers's lifting theorem produces a three-point Galois cover in characteristic zero. The quotient
  by a point stabilizer has degree p and the prescribed three ramification profiles. The fusion and realization
  results of Edmonds–Kulkarni–Stong then give the assertion for an arbitrary number of branch values."
* **Where primality enters.**
  * Lemma 2.5: for P ≤ S_p generated by a p-cycle, C_{S_p}(P) = P and N_{S_p}(P) = P ⋊ 𝔽_p^×.
  * The lifting interface (Thm 4.8, stated for odd p) works over an algebraically closed k of characteristic p, with
    G ≤ S_p, p ∥ |G| and a regular subgroup P = C_p.
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

*Scope.* The lemma is deliberately weak. It concerns only families with degree exactly p, and it uses only the
conclusion of SWZ (SWZ Thm 4.8 is stated for odd p; p = 2 is handled separately in their §8). For data in which all
but one profile has at most one nontrivial cycle it is unconditional, by Chenakkod–Faraco–Gupta arXiv:2103.01580v4
Cor 9.6 (read directly in the Astra retro review). It does not exclude an equivalence restricted to the large-prime
(MS) domain.

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

**Ranking.** (Falsifier behaviour of each row's native tools: §1 table.) Rows are ranked by how much a field-native
tool could plausibly do. A row ranks higher if the target
field (a) has an active community working on exactly the transported question, and (b) has a non-trivial structure
theory for the transported objects. Pure relabellings rank lowest. "Type" refers to the tool classes of §5:
* I = realisation from data (circular);
* II = universality only after a T1-blind or averaged relaxation;
* III = obstruction-only;
* IV = structure theorem on a canonical p-object.

| rank | ID | equivalence (proved in §4.x) | field | native tool(s) | might / might not apply | type | catalogue |
|---|---|---|---|---|---|---|---|
| 1 | E7 | (W)(n) ⟺ n ∈ d_{A₃}(ℤ³_{≥2}) (Lorenzini's critical polynomial of the path A₃); **for non-square n ≡ 1 (4): "L₃(n) contains a Jacobi −1 word" (= (W)(n) ∧ (S)(n), the DK five-slice form) ⟺ some x ∈ ℤ³_{≥2} with d_{A₃}(x) = n has critical-group discriminant form ⟨A/n⟩ of Jacobi symbol −1**; CONV-II(n) ⟺ some multiple cn is a formal A₃-value with middle weight ≡ 0 (mod 4c) | graph theory (arithmetical/critical structures) | Lorenzini Prop 6.3 (congruence slices); Wang–Lu EJC 33(3) #P3.80 Thm 5 (density 1 for every graph, via Dirichlet + AP unions) | active published open question ((W) = Lorenzini Ex. 6.2(a)), but the proved tools are fixed-pair slices (HJ_DEEP Lemma 3.2 bars finite coverings) and density | II | HJ_DEEP §3 (W); the pairing reading is new |
| 2 | E6 | for primes p ≡ 1 (4): (W)(p) ∧ (S)(p) ⟺ ∃ q, (q/p) = −1, such that L(p, q) bounds the negative-definite linear plumbing with **three** spheres of Euler numbers ≤ −2 (HJ length 3); its boundary linking form has Legendre class (q/p). **The C = 1 line of (★) (with u, B ≥ 2) = the chains (−B, −4, −u): the middle vertex is configuration (a) of Aceto–McCoy–Park, so these L(p, 4u − 1) are not b₂-minimal. At primes, the non-b₂-minimal (★) chains are exactly those with C = 1 or 4 ∈ {u, B}.** Relaxation T(p): "∃ q, (q/p) = −1, L(p, q) bounds some smooth negative-definite X with b₂ ≤ 3" is implied by (W)∧(S)(p) and also by length-≤ 2 chains, which are not ES certificates (for p ≡ 5 (8) already b = 2 works), so T carries no ES content | low-dimensional topology | Donaldson diagonalisation, Heegaard Floer d-invariants, Lisca (b₂ = 0), Greene changemakers, AMP / Fung–Park forbidden configurations | all are **obstructions** (non-existence) or classifications of minimality; existence comes from Kirby constructions, i.e. from words. Lisca is the topological mirror of T1 (rational balls exist only over squares) | III | DEDEKIND_ES, bsA_lens_*; the AMP / rational-blowdown reading is new |
| 3 | E1 | (★)(p) ⟺ p is the largest integer having exactly k representations by some numerical semigroup ⟨u, B⟩ with k ≡ 3 (mod 4) (generalised Frobenius number g_k = (k+1)uB − u − B) | numerical semigroups | Beck–Robins Thm 3; Popoviciu; inverse theorems (Rosales et al., Math. Scand. 94 (2004) Thm 1.11: every g is a 3-generator Frobenius number; odd g = F(2, g + 2)) | inverse results exist but only for relaxed shapes (3 generators, or k = 0); none controls k mod 4 | II | Z1970 (verbatim; Popoviciu Z1972) |
| 4 | E3 | **Lemma A:** for every odd n ≥ 5, ES(n) ⟺ 4/n − 1 is the Euler characteristic of a closed orientable 2-orbifold ⟺ ∃ compact Riemann surface X (g ≥ 2) and finite G ≤ Aut(X) with \|G\|(n − 4) = n(2g − 2) | Riemann surfaces, Fuchsian groups | Riemann existence, Selberg's lemma / Fox, Kulkarni genus spectrum | realisation needs the signature, which is an Egyptian representation | I | Z0153 / Agol's comment on MO 267209 (statement for hyperbolic 2-orbifolds), Z0171, Z0167; new: the proof of the all-signature direction (15 sporadic odd n) and the standard form (c) |
| 5 | E4 | ES(n) ⟺ 4/n = lct₀(x^a + y^b + z^c) for some a, b, c ≥ 1 (n ≥ 5) | singularity theory / birational geometry | Kollár (16.1), (3.2); ACC (Hacon–McKernan–Xu); Kuwata, Prokhorov | the full lct question is trivially true: 4/n ∈ lct(ℂ²) for all n ≥ 6 (Lemma R(b)); ES is the diagonal stratum, about which the field says nothing pointwise | II | Z0155 |
| 6 | E11 | for odd primes p (p ≥ 5): (★)(p) ⟹ ∃ N and a quotient y^N = t^α(1 − t)^β of the Fermat curve F_N with three branch points of ramification indices (x, y, z), 1/x + 1/y + 1/z = 4/p (genus 1 + uBC(p − 4)/2) ⟹ ES(p). **(★) triples are lcm-balanced and always cyclically realisable** (Lemma F) | arithmetic geometry (Fermat curves, cyclic covers) | Jacobi sums / Weil for the Jacobians; genus formula | the genus formula is the only link; point counts are irrelevant to existence | I | Z0167 / Z1922 neighbourhood; Lemma F is new |
| 7 | E8 | (★)(n) ⟺ n is the upper-right entry of T^u(−L^{−4C})T^B (u, B, C ≥ 1) ⟺ ∃ γ = [[a, n], [c, d]] ∈ SL₂(ℤ), c ∈ 4ℕ, a, d ≥ 1, a ≡ −1 (mod c) ⟺ some Anosov map γ = [[a, n], [c, d]] of T² **with upper-right entry n, c ∈ 4ℕ and a, d ≥ 1** sends the c-torsion point (1/c, 0) to its negative, c being its own lower-left entry (the bare Anosov/torsion condition is not equivalent: [[−1, 9], [4, −37]] negates (1/4, 0) but R(9) = 0) | dynamics / Farey / SL₂(ℤ) | Farey graph, periodic orbits of cat maps, Ghys–Rademacher linking | SL₂(ℤ) structure is p-blind; the tied modulus (c is an entry of γ) is B2 verbatim | I | FRONTIER §2.1 SL₂ form; Z63_EUCLID |
| 8 | E5 | ES(n) ⟺ ∃ x, y, z ≥ 1 with n·det P(x, y, z) = 4xyz (pretzel link) ⟺ the Seifert fibred double branched cover M(0; (x,1), (y,1), (z,1)) has rational Euler number of absolute value 4/n | knot theory / Seifert manifolds | determinant, signature, Montesinos classification | invariants are computed from (x, y, z) | I | Z0158 (verbatim) |
| 9 | E2 | (★)(p) ⟺ O(p) ≅ ω ⊗ π*O_{ℙ¹}(4C) on the stacky line ℙ(u, B) | algebraic geometry of stacks | Riemann–Roch / Serre duality (denumerant symmetry) | a degree identity | I | Z1991 (verbatim) |
| 10 | E9 | (★)_C(n) ⟺ 4Cn + 1 has a divisor in the ray class of complex conjugation in Cl_{4C·∞}(ℚ) ≅ Gal(ℚ(ζ_{4C})/ℚ) ⟺ a sub-multiset of the Frobenius elements of its prime factors multiplies to complex conjugation | algebraic NT (CFT) | Chebotarev, CFT existence | moving field ℚ(ζ_{4C}); the genus layer is free and the class layer is B2 | IV (covered) | Z62_INVERSEF; Z60_RAYCLASS |
| 11 | E10 | for p ≡ 1 (4) and C = c²: (★)_{c²}(p) ⟺ some ideal 𝔞 \| (1 + 2c√−p) of ℤ[√−p] has N𝔞 ≡ −1 (mod 4c²) | algebraic NT (imaginary quadratic fields) | class group of ℚ(√−p), Heegner/CM | ideal divisors of one principal element; no class-group input enters | IV (covered) | Z60_RAYCLASS §6 (S₁, square t₀) |
| 12 | E12 | R_t(n) = coefficient of a Kronecker theta quotient (Thm K) | modular / q-series | modularity, Hecke-type double sums, Serre–Stark | single-coefficient positivity is not available | II | METAPLECTIC_ES; Z1681 |
| 13 | E13 | ES(n) ⟺ ∃ three-point branched cover of S² with uniform branch data (x, y, z) and (2g − 2)/N = 1 − 4/n | Hurwitz problem / dessins | Riemann existence; Hurwitz existence theory | uniform data = signature (Lemma A). The **prime-degree** theorem is about degree p, not about 4/p (Lemma H) | I | Z0171, Z0167 (+ Z1922) |
| 14 | E14 | if ES is true, ES-SEARCH ∈ TFNP; a syntactic class membership (PPA / PPP / PLS) would be a proof of totality | complexity | parity, pigeonhole, potential principles | reduces to Z62 (parity), Z61 (pigeon, transport) | — | z31_complexity |

### 4.1 Proofs (all PROVED unless labelled; sanity checks `scripts/z64_equiv_checks.py` → `data/z64/equiv/checks.txt`, 0 failures)

**E1 (k-Frobenius).**
* For coprime u, B ≥ 1, the largest integer with exactly k ≥ 0 representations N = xu + yB (x, y ≥ 0) is
  g_k(u, B) = (k + 1)uB − u − B. Sources: Beck–Robins arXiv:math/0204037 Thm 3; Beck–Kifer, Integers 11 (2011) A24
  Thm 1 (with "exactly" = "at most"). Both V by subagent. Brute-force check (i): u, B ≤ 13, k ≤ 6, 805 cases.
* With k = 4C − 1 this is 4CuB − u − B, which is the (★) shape.
* For a prime p every (★) solution has gcd(u, B) = 1. Indeed gcd(u, B) divides 4uBC − u − B = p, and gcd = p would
  force u, B ≥ p, hence 4uBC − u − B ≥ 4uB − u − B ≥ 2uB ≥ 2p² > p. So (★)(p) ⟺ ∃ coprime (u, B) and k ≡ 3 (mod 4) with
  p = g_k(u, B). ∎
* Inverse results: every positive g is the Frobenius number of some ⟨n₁, n₂, n₃⟩ (Rosales et al. Thm 1.11), and every
  odd g = F(2, g + 2). Both hold at every odd square: they are input-blind relaxations (§5 type II).

**E2.** On ℙ(u, B) (u, B coprime) one has Pic = ℤ·O(1), ω ≅ O(−u − B) and π*O_{ℙ¹}(1) ≅ O(uB). Hence
O(p) ≅ ω ⊗ π*O(4C) ⟺ p = 4CuB − u − B. ∎ (Catalogue Z1991, verbatim; a degree identity.)

**E3 = Lemma A.** For every odd n ≥ 5 the following are equivalent:
* (a) ES(n);
* (b) 4/n − 1 = χ^orb(O) for some closed orientable 2-orbifold O;
* (c) ∃ compact Riemann surface X of genus g ≥ 2 and finite G ≤ Aut(X) with |G|(n − 4) = n(2g − 2).

*Proof.*
* **(b) ⟺ (c).** If G acts on X then χ(X) = |G|·χ^orb(X/G) (Riemann–Hurwitz), so (c) gives χ^orb = −(n − 4)/n.
  Conversely, a closed orientable 2-orbifold with χ^orb < 0 is ℍ/Γ for a cocompact Fuchsian group Γ. Γ has a
  torsion-free normal subgroup Γ′ of finite index (Selberg's lemma: Γ is a finitely generated subgroup of
  PSL₂(ℝ), linear in characteristic 0). Then X = ℍ/Γ′ and G = Γ/Γ′ give (c).
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
    {15, 21, 23, 39, 45, 47, 75, 95, 105, 111, 115, 117, 119, 165, 273}. The largest odd sporadic n is 273. In the s < 0 sporadic cases every value is ≤ 6888 (even, attained at
    (2, 3, 7, 41)); with s > 0 (n < 120) and s = 0 (n even), the script's NMAX = 10⁵ is exhaustive for odd sporadic n.
    (Not every r = 4 value is bounded: (2, 2, q, nq) gives unbounded odd n = 4q − 1, and (2, 3, 6, m) unbounded even
    n = 4m; neither is sporadic.) The internal review reran it with NMAX = 10⁸ and got
    the same list. ES holds at each of them: all are below
    Salez's 10¹⁷, and `scripts/z64_equiv_orbifold.py` also prints an explicit 3-term representation for each.

∎ *Prior work.* (a) ⟺ (b) restricted to triangle orbifolds is catalogue item Z0153 / analogues-0153 (MathOverflow
267209, quoted there). New here are the automorphism form (c) and the exclusion of every other signature.

*Corollary.* For primes p ≡ 1 (4) only r = 3 occurs: 4/p is never a two-term Egyptian fraction, and no such p
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
  class for p ≡ 1 (4) is the Legendre class (A/p). For p ≡ 3 (4) the sign ± flips the symbol, so everything below is
  stated for p ≡ 1 (4).

Hence "L₃(p) contains a Legendre −1 word" ⟺ ∃ q with (q/p) = −1 and len(p/q) = 3, i.e. L(p, q) = ∂X(p, q) with
b₂ = 3. This is (W)(p) ∧ (S)(p), the DEDEKIND_ES five-slice form. (S) alone is an implication and holds vacuously
where L₃ = ∅, e.g. at 5 and 105. The internal review flagged the earlier "(S) ⟺" as false.

* **C = 1 line.** The (★) solutions with C = 1 and u, B ≥ 2 are exactly the length-3 chains with middle weight 4,
  i.e. plumbings (−B, −4, −u) (u = 1 or B = 1 gives a formal word of HJ length 2). AMP Thm 1.1(iii)(a) is the single
  vertex of weight −4, and its (iv) lists X(4, 1) (✔ read). By AMP (i) ⟺ (iii), these L(p, A) admit negative-definite
  fillings with b₂(X) < 3.
* **Full non-minimality locus at primes.** A (★) chain (−B, −4C, −u) with u, B ≥ 2 and odd p contains an AMP
  configuration iff C = 1 (middle −4) or 4 ∈ {u, B} (end −4). The configuration list was re-read from the AMP PDF page image by the cross-model reviewer; (e) and (f) correct the
  earlier transcription. The cases:
  * (b), (c), (g): need a −2 or −3 in the middle, impossible because 4C ≥ 4;
  * (d), a non-adjacent pair of −2's: needs u = B = 2, so p = 16C − 4 is even;
  * (e), an isolated −3 plus an adjacent (−2, −2) pair, and (f), an adjacent (−3, −3) pair: every adjacent pair of
    the chain contains the middle −4C, so neither occurs;
  * (h)–(j): length 4, so they do not fit in a 3-chain.

  The reviewer's induced-subgraph test on all 41 718 (★) chains at primes ≤ 4·10⁴ found only (a), with 0 mismatches. Example: p = 89, (u, B, C) = (4, 3, 2), chain
  (−3, −8, −4). **So the AMP non-minimality reading is not specific to the C = 1 line.** (X(4, 1) is the piece
  replaced in a Fintushel–Stern rational blowdown; that standard reading is quoted from memory and used in no proof.)
* **Relaxation T(p).** (W)∧(S)(p) ⟹ T(p) is immediate from the plumbing. But T(p) also follows from any non-residue q with
  len(p/q) ≤ 2. For example p/q = [[a, b]] with p + 1 = ab and (b/p) = −1; such a q exists whenever p + 1 has a
  divisor b ∈ [2, (p + 1)/2] with (b/p) = −1. For every p ≡ 5 (8), b = 2 already works, since (2/p) = −1. Those chains are not ES certificates. So the topologically natural
  relaxation loses the content. The ES content is "the *canonical* plumbing has exactly three vertices", a
  continued-fraction condition that smooth-topology tools see only through minimality criteria (AMP).
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
* Hence "L₃(n) contains a Jacobi −1 word" (= (W) ∧ (S) at n, for non-square n ≡ 1 (4)) ⟺ some x with d_{A₃}(x) = n has critical-group
  discriminant form of Jacobi symbol (A/n) = −1. The symbol does not depend on the generator: q(k·g) = k²q(g) and
  (k²/n) = 1. Reading the word backwards gives the same class, (A/n) = (A*/n) (HJ_DEEP Prop 4.1).
* CONV-II and U₇ in this language. By HJ_DEEP Prop 2.1, Type II solutions at n are formal words K(a, 4cd, b) = cn
  (letters a, b ≥ 1). So CONV-II(n) ⟺ ∃ c ≥ 1 such that cn is a formal A₃-value with middle weight ≡ 0 (mod 4c).
  U₇(n) ⟺ ∃ g, x, z ≥ 1 with n = K(x, g, z) = xgz − x − z and 8 | xg. This is the T-form of Z60_LOPEZ Lemma 7(i),
  gn + 1 = (xg − 1)(zg − 1), with middle weight g at n itself; the cross-model reviewer checked it equals U₇ on all
  odd n < 1600. (An earlier sentence here, "the same A₃-value statement at gn with middle weight ≡ 0
  (mod lcm(8, g))", was false: n = 105, g = 2, K(3, 24, 3) = 210.)

∎

**E8.**
* With T = [[1, 1], [0, 1]], L = [[1, 0], [1, 1]] and c = 4C: T^u(−L^{−c})T^B = [[cu − 1, cuB − u − B], [c, cB − 1]]
  (check (ii): 10 632 solutions).
* Conversely, if γ = [[a, n], [c, d]] ∈ SL₂(ℤ) with c ∈ 4ℕ, a ≥ 1 and a ≡ −1 (mod c), then ad ≡ 1 forces d ≡ −1, and
  T^{−(a+1)/c} γ T^{−(d+1)/c} = [[−1, 0], [c, −1]]. This recovers (u, B) = ((a + 1)/c, (d + 1)/c), both ≥ 1.
* On T² = ℝ²/ℤ², γ(1/c, 0)ᵀ = (a/c, 1) ≡ (a/c, 0), which equals −(1/c, 0) iff a ≡ −1 (mod c). The torus form keeps
  the restrictions upper-right entry n, c ∈ 4ℕ, a, d ≥ 1 (they give trace ≥ 6, so γ is Anosov); without them the
  equivalence fails, e.g. γ = [[−1, 9], [4, −37]] is Anosov and negates (1/4, 0), but R(9) = 0.

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

**E11 = Lemma F.** Let p be an odd prime (nonvacuous cases p ≥ 5; at p = 2, (u, B, C) = (1, 1, 1) gives indices
(1, 2, 2), i.e. only two branch points) and (u, B, C) a (★) solution, with (x, y, z) = (uBC, pBC, puC) and N = puBC.
* (a) lcm(x, y) = lcm(y, z) = lcm(z, x) = N.
* (b) There are a, b, c ∈ ℤ/N with a + b + c = 0, gcd(a, N) = N/x = p, gcd(b, N) = N/y = u and gcd(c, N) = N/z = B.
  The cover is connected because gcd(a, b, N) divides gcd(p, u) = 1. Hence the cyclic cover y^N = t^a(1 − t)^b of ℙ¹
  (a quotient of the Fermat curve F_N) has ramification indices
  x, y, z over 0, 1, ∞, and 2g − 2 = N(1 − 4/p) = uBC(p − 4).

*Proof.*
* (a) gcd(u, B) = 1 (E1), and p ∤ uBC since u, B, C < p. Indeed p + B = u(4BC − 1) ≥ 3u and p + u ≥ 3B give
  u + B ≤ p, and p + u = B(4uC − 1) ≥ 4uC − 1 gives C < p. Then lcm(uBC, pBC) = BC·lcm(u, p) = N, and the other two
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

## 5. Native tools: four types, and why formula-level dictionaries are circular (Push 2)

Every row E1–E13 is a **formula dictionary**. Explicit formulas in the certificate parameters (u, B, C) or (t, u, v)
or (x, y, z) produce the field object, and explicit formulas read the parameters back off it. Every native existence
tool met in this lane belongs to one of four types. The types are judged by what the tool takes as input and what
it concludes.

*Status of this section: the classification into four types is an **Assessment**. Only the type-I observation and
Lemma R (with its consequence) are PROVED.*

**Type I: realisation from parameter data.** Examples: Riemann existence; Selberg's lemma; Kirby/plumbing constructions;
Waterhouse–Honda–Tate; Steinitz; Freedman; the CRT step of Lemma F. Such a theorem says "for every admissible datum
δ there is an object O(δ)". In each row δ is the certificate itself:
* the signature in E3/E13;
* the chain in E6;
* (x, y, z) in E5/E11;
* (u, B, C) in E2/E8.

*Observation (PROVED, trivial).* If Φ(n) ⟺ ∃ δ ∈ Δ(n) with O(δ) realised, and a type-I theorem realises every δ,
then Φ(n) ⟺ Δ(n) ≠ ∅. That is the original statement. So type I contributes nothing to existence.

**Type II: universality or density after a relaxation.** Examples: Rosales et al. Thm 1.11; lct ∈ HT₂; Lorenzini
Prop 6.3 slices; Wang–Lu density; Kulkarni's genus spectrum; and Hurwitz realisability at prime degree (§3.3), whose
relaxation is "drop the arithmetic".

**Lemma R (T1-blindness of the proved relaxations).** Let m ≥ 3 be odd.
* (a) (W) holds at m² for every m with 3 ∤ m: (t, u, v) = (2, 2, (m² + 2)/3). PROVED. For 3 | m, the evidence is
  HJ_DEEP's census (EVIDENCE there; independently reproduced to 10⁹ by R174): its exception set below 10⁹ is E_W,
  which contains no square except 9. `scripts/z64_equiv_wsquares.py` finds no exception among odd m ≤ 2000. Its
  attempt at a finite fixed-pair cover of all odd squares fails; the uncovered residues are multiples of 3,
  consistent with HJ_DEEP Lemma 3.2.
* (b) 4/m² is the log canonical threshold of a plane-curve germ: 4/n = lct₀(x^a y^b (x + y³)) with n = 3a + b + 3,
  a ≥ 1, b ≥ 0, b ≤ a + 1 and a ≤ b + 3 (b = 0 is needed for n = 6 and 9). This is Kollár's HT₂ formula (3.2) with (c₁, c₂) = (1, 3), V by subagent. I re-derived it
  by the toric computation. The rays (1, 0), (0, 1), (1, 1), (2, 1), (3, 1) give 1/a, 1/b, 2/(a + b + 1),
  3/(2a + b + 2), 4/(3a + b + 3). Under b ≤ a + 1 and a ≤ b + 3 the last is the minimum. The internal review checked
  this for all a, b < 60. The ranges cover every n ≥ 6. PROVED, relative to the standard lct formula for Newton-non-degenerate
  plane curves (Kollár Thm 15).
* (c) m² is the Frobenius number of the two-generator semigroup ⟨2, m² + 2⟩ (Rosales et al. Lemma 1.1; check:
  2(m² + 2) − 2 − (m² + 2) = m²). PROVED.
* (d) Wang–Lu's theorem is a density statement (averaged; B6).

Meanwhile (★), U₇ and CONV-II fail at every odd square, and L₃(m²) has no Jacobi −1 word (T1). (S) itself is
quantified over non-squares only.

*Consequence (PROVED).* No relaxation in (a)–(c) implies any of these four statements. Each is true at odd squares,
where the target is false. Any proof that passes through such a relaxation needs a square-sensitive input elsewhere.
This is Z63 Lemma 1's logic applied to the other fields.

**Type III: obstructions.** Examples: Donaldson; Heegaard Floer d-invariants; Lisca; AMP / Fung–Park; ACC for lct;
EKS non-realisability; Hasse–Weil upper bounds. These prove non-existence. To use one for ES, a *hypothetical
failure* ¬(★)(p) would have to produce an object with a forbidden property. In E1–E13 every object is built from a
certificate, and a failure supplies none (Assessment). So type III enters only through canonical p-objects (type IV).
In the reverse direction, Lisca's theorem is the topological mirror of T1 (E6).

**Type IV: structure theorems on a canonical p-object.** These are objects defined from p alone that exist at every
input, squares included:
* the level-p presentation complex of Γ₀(p) (Z63_EUCLID);
* Cl(ℚ(√−p)) and ray class groups (Z60_RAYCLASS);
* supersingular isogeny graphs (bsC_*);
* the family {L(p, q)}_q of lens spaces, equivalently the set Λ₃(p) = {A ∈ (ℤ/p)^× : len(p/A) = 3}, whose
  intersection with the non-residues is (S) (E6/E7; this is SDEEP's target set).

Only this type can be non-circular. Every instance found here is already a repo target with its own screening memo.

### 5.1 Push on the top-ranked rows E6/E7 at a single prime: the topological invariant of the sign

**Question.** E6/E7 attach to p the canonical set Λ₃(p) of A with len(p/A) = 3, i.e. the lens spaces L(p, A) with a
three-vertex canonical plumbing. Can a topological or Dedekind-sum invariant of L(p, A) do more than restate the
Jacobi sign? In particular, can it separate the non-residue A from the residue A on Λ₃(p) at primes, as opposed to
at odd squares?

**Computation** (`scripts/z64_equiv_signclass.py` → `data/z64/equiv/signclass.txt`; exact).
* (1) The Barkan–Hirzebruch–Zagier formula 12 n s(A, n) = A + A* + n·Σ(b_i − 3) holds for all 362 852 words with odd
  n ≤ 20 000 and gcd(A, n) = 1. Specialised to length 3 it reads 12 n s(A, n) = t(u + v) − 2 + n(t + u + v − 9).
* (2) Rademacher's congruence 12 n s(A, n) ≡ n + 1 − 2(A/n) (mod 8) holds on the same words.
* (3) Combining (1) and (2): (A/n) is a polynomial function of the letters mod 8. The table matches the direct
  Jacobi symbol on all 9 913 628 words with odd n ≤ 3·10⁵.
* (4) The table is in fact a function of (t, u, v) mod 4. Its 20 sign −1 cells are listed in the data file.

**Reading.** This is exactly DEDEKIND_ES Thm 4.5 / Cor 4.1 (the sign is a mod-4 function of the letters) and
BRAINSTORM/bsA_wu_rokhlin_sign Thm W (the sign is the Wu square, equivalently the mod-8 Rokhlin invariant of the
lens space). Here it is re-derived independently, through the Dedekind-sum (Casson–Walker / d-invariant) route.
* At a single prime, the best topological invariant of L(p, A) reduces the (S) sign to a **fixed congruence class
  of the plumbing weights mod 4**.
* So "L₃(p) has a −1 word" ⟺ "p has a length-3 word in one of the fixed mod-4 cells". That is the five-slice problem
  DK already screened (FRONTIER §2.1, (J)105: the five-slice BM main term 45/(8π²)).

The topology contributes the T1-exactness (no word of an odd square lies in the −1 cells; Wu rigidity, Thm W2) and
nothing on existence. **Outcome: no new information. The push confirms that the E6/E7 tools stop at the sign layer,
as the type-III verdict predicts.**

**Shape of an escaping equivalence (Assessment).** A useful new equivalence must
* (i) attach to p a canonical object O(p) that exists unconditionally and also at m²;
* (ii) have a structure theorem in its field forcing a sub-object S ⊂ O(p) that maps to a certificate;
* (iii) let that theorem use a property of O(p) that differs between primes and squares.

The Hurwitz theorem has (i)–(iii) for its own target (O(p) = S_p with its regular C_p), but its sub-object is not
arithmetic (§3.3). Of the rows above, only E6/E7 (Λ₃(p)) and E9/E10 have (i). None has (ii).

## 6. Four FRONTIER §4 hard screens for the best items

| item | T1 squares | 8/131 | tied modulus | fixed p |
|---|---|---|---|---|
| E7 / E6 (Λ₃(p), critical-group sign) | built into the statement (Jacobi −1 is impossible at m²); the native relaxations are T1-blind (Lemma R); the best invariant (Dedekind/Rokhlin, §5.1) reduces the sign to mod-4 cells | the sign law (A/p) = −(−1/p) on Type II words is numerator-blind; C even vs C odd is invisible to the graph and the topology | the middle letter t = 4C is a vertex weight, and the tie is the same | yes (pointwise statements), but no forcing tool |
| (Ch) Hurwitz prime degree (precedent) | composite degrees fail; there is no square-specific failure | n/a | n/a (no modulus) | yes; but the witness is not arithmetic |
| E3 (Lemma A) | ES itself has no T1 | 8/n analogue: 8/n − 1 as χ^orb is the same equivalence with 8 (Lemma A's proof is numerator-specific only in the r = 4, 5 casework) | not applicable (no modulus) | circular |

## 7. Verdict, proposed FRONTIER text, bottom line

**Verdict: narrowed.** No HOT LEAD.

**Strengthened (small, PROVED):**
* Lemma A (orbifold χ and automorphism ratio ⟺ ES for every odd n ≥ 5);
* Lemma F ((★) triples are lcm-balanced and cyclically realisable);
* E7's identification of the (S) sign with the critical-group discriminant form;
* E6: at primes, the (★) chains whose canonical plumbing is not b₂-minimal (Aceto–McCoy–Park) are exactly those with
  C = 1 or 4 ∈ {u, B};
* §5.1: an independent Dedekind-sum derivation of DK Thm 4.5 (EVIDENCE + classical theorems; nothing new);
* Lemma R (the proved relaxations are T1-blind).

**Narrowed:**
* every formula dictionary is circular for type-I/II/III tools (§5);
* the new precedent class (Ch) does not transfer to arithmetic witnesses (§3.3, Lemma H CONDITIONAL).

**Surviving:** only type-IV structure theorems on canonical p-objects, all already screened elsewhere in the repo.

**Proposed FRONTIER text** (§3 after the z63 precedent paragraph, or §7 z64 block; not applied here):
> *(z64, `Z64_EQUIV.md`; internal.)* A precedent class missing from Z63 is the Hurwitz existence problem in prime
> degree:
> * every compatible branch datum of degree p over S² is realisable (Edmonds–Kulkarni–Stong's question; claimed
>   theorem of Song–Wen–Zhang arXiv:2609.20572, unrefereed, proved in residue characteristic p via a regular
>   C_p ≤ S_p);
> * every composite degree has non-realisable data (EKS Prop 5.7).
>
> It is the one result of the shape "true at every prime, false on explicit composites" found here (claimed and
> unrefereed) whose proof is neither an identity, nor a unit-group or norm-form argument (Legendre's negative Pell,
> two squares), nor a count. Primality acts on a geometric/group-theoretic object, and prime-degree realisability carries
> no (★) information (Lemma H, conditional). Z64_EQUIV §4 proves ten cross-field equivalences and one implication
> chain, among them:
> * ES(n) ⟺ some Riemann surface has an automorphism group with |G|(n − 4) = n(2g − 2) (n odd ≥ 5);
> * the (S) sign = the critical-group discriminant form of Lorenzini's A₃;
> * at primes, the (★) chains with non-b₂-minimal lens-space plumbing (Aceto–McCoy–Park) are exactly C = 1 or
>   4 ∈ {u, B}.
>
> Their native tools are realisation theorems (circular), T1-blind or averaged relaxations (Lemma R), or obstructions.
> Only structure theorems on canonical p-objects (Γ₀(p), class groups, Λ₃(p)) can be non-circular; no new one was
> found.

**Bottom line.** Re-expressing ES, (★), (S), U₇ or CONV-II in other fields is easy, and the repo's catalogue already
held most of the forms. This lane proved ten equivalences and one implication chain with exact ranges. Every native existence tool met is of
one of three kinds: it realises objects from the very data that constitute a certificate; it proves a relaxation
that also holds at odd squares (or only on average); or it obstructs. The one genuinely new item is on the precedent
side: prime-degree Hurwitz existence, a 2026 claimed theorem with a prime/composite shape *analogous* to that of
ES's restricted predicates (not ES's own shape), proved by
construction in characteristic p. Its primality acts on S_p and on covers over an algebraically closed field, not on
a ℤ-point. So it widens the catalogue of how primality can force existence, without giving B2 a template. Any future
equivalence worth a lane must attach a canonical object to p and come with a structure theorem that distinguishes
primes from squares. None was found.

## 8. Review log

**Internal hostile review** (deep-mode subagent, model anthropic/claude-opus-5-5, on commit 82051268d; the default
`review` tool and the default deep model were unavailable because of a usage limit). Verdict: ACCEPT-WITH-FIXES, no
FATAL.

*Re-verified by the reviewer:*
* Lemma A's full case analysis; the orbifold enumeration (rerun with NMAX = 10⁸, identical list; reachable n ≤ 6888);
* Lemma F, including the bounds and ℓ = 2;
* E1, E2, E5, E8, E9, E10;
* the lct formula (all a, b < 60); (W) at squares for 3 ∤ m; E_W;
* R(409) = 0;
* the SWZ quotes (Thm 1.1, Lemma 2.5, Thm 4.8, abstract, acknowledgment), AMP Thm 1.1(iii)(a) and (iv), and the
  Hadamard order 2396.

*Findings and fixes:*
1. MAJOR: "(S) ⟺ …" in E6/E7 was false, because (S) is an implication that holds vacuously where L₃ = ∅ (n = 5,
   105). **Fixed:** E6/E7 now state "L₃(n) contains a Jacobi −1 word" = (W) ∧ (S).
2. MAJOR: "C = 1 ⟺ plumbing contains a (−4) vertex" was false as an iff. Counterexample: p = 89, chain (−3, −8, −4).
   **Fixed:** "middle (−4) vertex". Added the full non-minimality locus at primes, C = 1 or 4 ∈ {u, B}, with proof.
3. MAJOR: "fourteen equivalences proved" was an overclaim. **Fixed:** ten proved equivalences (E1–E10), one
   implication chain (E11), three quoted rows (E12–E14).
4. MAJOR: the FRONTIER text called SWZ "the one verified …" result. **Fixed:** now "claimed, unrefereed", and unit
   group / norm-form arguments are excluded explicitly.
5. MAJOR: `sources/precedent_nt.md` had been committed empty. **Fixed:** committed.
6. MAJOR: the four-type classification was presented as PROVED. **Fixed:** labelled Assessment; only the type-I
   observation and Lemma R are PROVED.
7. MAJOR: the brief was only partly met (no falsifier column, no single-prime push on E6/E7). **Fixed:** the §1 table
   is rewritten with native-tool behaviour per screen, and §5.1 adds a concrete push (exact Dedekind-sum computation
   on 9.9·10⁶ words). Its outcome is negative: it reproduces DK Thm 4.5.
8. MINOR: Lemma R(b) re-derivation was incomplete. **Fixed:** all toric rays are listed.
9. MINOR: (W)-at-squares labels. **Fixed:** PROVED for 3 ∤ m; census-backed EVIDENCE otherwise; E_W "conjecturally
   complete".
10. MINOR: the wsquares script's docstring and output overstated the covering. **Fixed:** the failure of the cover is
    recorded.
11. MINOR: orbifold script. **Fixed:** bound n ≤ 6888 stated, dead loop removed, Selberg's lemma alone used for
    (b) ⟹ (c).
12. MINOR: E7 generator independence and U₇ notation. **Fixed.**
13. MINOR: novelty. "0 substantive hits" now, with the stray matches named. Lemma A's triangle-orbifold form is
    credited to Z0153 / MathOverflow 267209.
14. MINOR: §0 no longer counts Holzer as an omitted class. (EF) is marked V/V2.
15. MINOR: Lemma H's scope is stated; SWZ Thm 4.8 is for odd p; the CFG Cor 9.6 subcase is unconditional.
16. MINOR: T(p) holds trivially at p ≡ 5 (8) via b = 2. **Added.**
17. MINOR: Lemma F connectedness (gcd(a, b, N) = 1). **Added.**

**Cross-model review** (`data/z64/xreview/REVIEW_EQUIV.md`; Opus standing in for the cross-model reviewer; verdict
ACCEPT-WITH-FIXES). The reviewer independently re-derived Lemma A, Lemma F, E1–E11, the AMP locus and Lemma H, and
confirmed the SWZ / Petronio / AMP / Lorenzini sources. All eight required fixes are applied:
1. **E7's U₇ sentence was false** (n = 105: K(3, 24, 3) = 210). It is replaced by the correct T-form: U₇(n) ⟺
   n = K(x, g, z) with 8 | xg.
2. **Catalogue IDs corrected.** E1 = Z1970 (Popoviciu Z1972); E2 = Z1991; E5 = Z0158; E13 and dessins = Z0167
   (+ Z1922). The wrong IDs Z0394–Z0402, Z0417 and Z0418 are removed, as is the claim "Seifert: no row". Novelty is
   lowered accordingly: E1, E2, E5 and E13 were already catalogue rows.
3. **MO 267209 is credited to Ian Agol's comment** (hyperbolic 2-orbifolds). New in Lemma A is only the
   all-signature proof (with its 15 sporadic n) and form (c).
4. **AMP configurations (e) and (f) re-transcribed from the PDF image**, and the E6 locus proof rewritten. The locus
   theorem is unchanged.
5. **Quantifiers p ≡ 1 (4)** (resp. non-square n ≡ 1 (4)) added to E6 and E7.
6. **Lemma A:** the largest odd sporadic n is 273; the bound 6888 is an even value.
7. **Lemma R(b):** b ≥ 0 is allowed (needed for n = 6 and 9). The T1 wording is corrected: (S) is defined only for
   non-squares.
8. **EKS Prop 5.7** now cites the reviewer's computational confirmation for d ≤ 12.

The falsifier-table F2 cell for E6 is also reworded. The verdict is unchanged.

**Cross-model retro review (Astra)** (`data/z64/xreview/REVIEW_EQUIV_ASTRA.md`; verdict ACCEPT-WITH-FIXES; E1–E10,
Lemma A (with an independent exhaustive signature analysis), Lemma F, Lemma R and conditional Lemma H re-derived; all
four lane scripts replay byte-identically; independent check `scripts/xrev_retro_equiv_astra.py`). All four required
fixes applied:
1. Domains explicit: E8's torus clause keeps upper-right entry n, c ∈ 4ℕ, a, d ≥ 1 (counterexample [[−1, 9], [4, −37]],
   R(9) = 0); E11/Lemma F restricted to odd primes (p = 2 gives two branch points); §1 notes that inheritance of
   screens holds only inside each row's proved domain (E1/E2/E10 are prime-only).
2. Hurwitz: the "O(1) for rigid genus-0 data" count is deleted (Catalan(a) realisations of a genus-0 passport at
   p = 4a + 1); "ES's exact prime/composite shape" / "ES's square failures" replaced by an analogy with the restricted
   predicates (ES itself has no square obstruction). Lemma H's Chenakkod–Faraco–Gupta subcase restated as read.
3. The 6888 bound scoped to the s < 0 sporadic signatures (memo and `scripts/z64_equiv_orbifold.py` docstring;
   output unchanged).
4. F3: (W) holds at 284 of the 285 composite R-zeros and fails at 105; "blind on the 285" became "blind on most".
