# Z62_PARITY — index / parity / fixed-point existence at a single prime (lane PARITY, wave z62)

**ES is OPEN; nothing here proves or disproves it, or (MS), (MS-U₇), U₇.** Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results, internally reviewed only.
Scripts `scripts/z62_parity_*`, data `data/z62/parity/`. Brief: `z52bbriefs/z62_lanes.md` §PARITY.

*Status: final; internal hostile review done (§6), fixes applied. Verdict: **narrowed** — no HOT LEAD.*

Notation as in FRONTIER §2 / `Z60_SUMMARY.md`: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} ((★)); 𝔐 = {1, 121, 169, 289,
361, 529} ⊂ (ℤ/840)^×; U₇(n): some f ≡ 7 (8) with (−n mod f) | f + 1; Z₇ = the eight composite U₇-zeros; "hard primes" =
primes p ≡ 1 (24) (and p mod 840 ∈ 𝔐 where stated).

## 0. Mandatory falsifier table (for the *framework* of §1 and the main line of §3; re-stated at the end)

| screen | behaviour of a parity/index mechanism (§1) | where primality / non-squareness must enter |
|---|---|---|
| **F1 odd squares** | If the forced set (Fix τ minus a disjoint known part K, or the critical/terminal cells) consists of (★)/U₇/Type II certificates, these families are empty at m² (T1), so the identity forces I(m²) = 0 — the easy side must vanish at squares. (This is *not* automatic for full-ES support: odd squares have ES solutions, e.g. 4/9 = 1/3 + 1/18 + 1/18.) | In the evaluation of the easy side I(p) (Zagier: #Fix σ = #{p = x(x+4z)} = 1 uses primality). Assessment: a quadratic-character (Jacobi-type) easy side is the natural T1-compatible candidate, but square-vanishing does not force that shape, and not every Jacobi expression vanishes at squares. |
| **F2 C-even / numerator 8** | An index with support in R₈ cannot be uniformly non-vanishing: R₈(p) = 0 at 4 primes in 𝔐 near 10¹⁰ (Lemma P1). For U₇-supported indices the relevant screen is FRONTIER's: at in-domain U⁽⁸⁾ failures the U₇ targets beyond U⁽⁸⁾ (v₂((f+1)/8) < v₂(r) < 3) must be used (threshold qualifications as there). | The support must reach beyond the 8-line (for (★): the C-odd part; for U₇: the non-U⁽⁸⁾ targets). |
| **F3 composites** | Uniform-in-n identities: at the 285 composite R-zeros (8 U₇-zeros Z₇) the easy side must vanish too (it may: divisor-type terms). Prime-only identities: no constraint, but then primality is used in the identity itself. | Divisor-type easy side (extra terms at composites) or prime-only identity. |
| **F4 known zeros** | Exact (no threshold) identities supported on (★) are possible only if their easy side vanishes at the 14 (★)-zero primes; **uniform non-vanishing on (★) support is refuted** (Lemma P1). U₇ / U_II / full Type II have no known prime zero. Note: a U₇-supported index would give ES(p) (U₇ ⊂ Type II), not (MS) itself. | — |

## 1. The framework and its necessary condition

**Lemma P0 (index necessity; PROVED, elementary — essentially WINDMILL Lemma 1 and `BRAINSTORM/invol_topological.md`
Lemma T, which already cover Sperner/Tucker/mod-2 degree/Smith/Lefschetz–Hopf; the Morse (c) and Stokes (d) forms are
only spelled out here).** Let Cert(p) be the certificate set of a family (e.g. (★), U₇). Each of the following
argument shapes yields a weight w: Cert(p) → ℤ (or F₂) with Σ_c w(c) = I(p), where I(p) is the quantity the argument
must evaluate; the argument proves Cert(p) ≠ ∅ exactly when it proves I(p) ≠ 0 (resp. odd):
(a) two involutions σ, τ on a finite set S with a **disjoint** decomposition Fix τ = F_cert ⊔ K_p and a map
Φ: F_cert → Cert(p) (Zagier / Heath-Brown): w(c) = |Φ⁻¹(c)|, I = |Fix σ| − |K_p| (mod 2); the argument needs
|Fix σ| − |K_p| ≡ 1;
(b) a graph of max degree 2 (PPA / handshake) whose odd-degree vertices are a known set ⊔ a set mapped to Cert(p):
I = #known (mod 2);
(c) a Morse matching on a finite complex K whose critical cells are known cells ⊔ cells mapped to Cert(p):
I = χ(K) − Σ_known (−1)^{dim} (over ℤ, w signed by dimension);
(d) Stokes: an acyclic K, a 1-cochain ω with δω supported on 2-cells mapped to Cert(p), and a 1-cycle z with
⟨ω, z⟩ = I ≠ 0: for every 2-chain c with ∂c = z, Σ_e c(e)δω(e) = I (individual weights depend on the filling, the total
does not: two fillings differ by a 2-cycle ∂b, and ⟨δω, ∂b⟩ = ⟨δδω, b⟩ = 0);
(e) Lefschetz–Hopf for a cellular self-map f, **provided** every nonzero diagonal coefficient of the cellular chain map
f_# outside a known set of cells occurs on cells mapped to Cert(p): I = L(f) − Σ_known (−1)^{dim}(diagonal coefficient).
(Without this hypothesis diagonal coefficients need not correspond to setwise-fixed cells: the degree-2 map of the
one-vertex one-edge circle has L = −1.)
*Proof.* (a) |S| ≡ |Fix σ| ≡ |Fix τ| = |F_cert| + |K_p|. (b) handshake. (c) the Morse complex has the same Euler
characteristic. (d) I = ⟨ω, ∂c⟩ = ⟨δω, c⟩ and δω vanishes off certificate cells. (e) Hopf trace formula. ∎
So any argument of these shapes is a **weight on certificates with a computable non-zero total** ("deterministic
weighted count"); the novelty can only be in where w comes from (in (b)–(d) w may depend on neighbouring
non-certificate cells).

**Lemma P1 (uniform non-vanishing must avoid families with prime zeros; PROVED, trivial).** If Σ_{c ∈ 𝒜(p)} w(c) = I(p)
for every prime p ≡ 1 (4), then I(p) = 0 wherever 𝒜(p) = ∅. Hence an exact identity supported on (★) must have I = 0 at the
14 (★)-zero primes (9 in 𝔐; `data/z58/screens/`), and one supported on R₈ must have I = 0 at the 4 R₈-zero primes in 𝔐
near 10¹⁰; such identities may exist, but cannot be *uniformly* non-vanishing. A (★)-supported index argument for (MS)
therefore needs an easy side that vanishes at the known zeros and is provably non-zero beyond a threshold (unusual for
parity identities, not excluded); otherwise the support must be enlarged (U₇ / U_II / full Type II: no known prime zero;
these give ES(p), and (MS) only via an extra implication back to (★)). ∎

## 2. Precise statements attacked

* **(PAR)** Find (K_p, Cert, w-source) as in Lemma P0 with I(p) ≠ 0 for all primes p ∈ 𝔐 (beyond a stated threshold)
  and I(m²) = 0 for odd squares, with a proof of the evaluation of I. Open; this lane tests concrete new objects.
* **Prior parity work in the repo (read before computing; attribution).** WINDMILL (Lemma 1, §3 ≈ 7 000 weights),
  WINDMILL_REDUCTION (O164: Zagier = dihedral symmetry of Conway rivers (§1); Legendre/SQUFOF midpoints carry no ES bias
  (§3); X-certificates as ambiguous forms of discriminant T² − 4 (§5.2); T + 2 = tτ (§8); infinite-menu windmills on the
  modular hyperbola (§9); congruence sub-counts of E(p) parity-random (§6)), INVOLUTION_ES/ES2 ((J)2), Z52D_PARITY,
  PARITY_FIXED_P, DEDEKIND_ES (HJ dictionary, Jacobi sign = mod-4 class), BRAINSTORM `invol_*`, `y2_parity_involution`,
  `s3_words_parity`, `bsB_zolotarev_transpose`, `z52b_pass1_H05` (Z1665: word topographs, disc depends only on c(u+B);
  Z1700: γ = T^u [[−1, 0],[c, −1]] T^B, from which cyclic conjugation already gives class dependence on (c, u+B)),
  board astra-2 / fable-2. *I located WINDMILL_REDUCTION §3/§5.2 and Z1665 only after KT1/KT2 had run (my initial
  `git grep` listing was truncated); Observation A below is theirs, KT2 is a replication on the (★) slice, and
  Theorem R is an explicit form of what Z1700's factorisation implies.*
* **Why not already closed.** Closed: finite-menu affine involutions on X(p) ((J)2 Thm 6.1, CONDITIONAL on BH); finite
  affine group menus (Z52D_PARITY Thms C, D); fixed-feature weight dictionaries (WINDMILL §3, invol_windmill_signature
  E1–E3, board astra-3 LP certificates); cheap signs on U₇ words (board, fable). Not closed: weights from
  topograph/river structure *as weights in a parity identity* (WINDMILL_REDUCTION tested the rivers' forced objects,
  not river-weighted counts), cochain (Stokes) forms (d), signed indices over the ℚ-span, and indices supported on U₇.
  These are what §3–§4 test.

## 3. Main line and PRE-REGISTERED kill test (checkpoint 1)

**Observation A (PROVED, one line; = WINDMILL_REDUCTION §5.2 and Z1665, rediscovered).** For (u,B,C) a (★) triple, the matrix
γ = [[4Cu−1, p],[4C, 4CB−1]] ∈ SL₂(ℤ) is an automorph (U = 1) of the binary form F = [4C, 4C(B−u), −p], which is
**ambiguous** (first coefficient divides the middle one), primitive, of discriminant Δ = t² − 4, t = tr γ = 4C(u+B) − 2
(Δ = 16C²(B−u)² + 16Cp = 16C(C(u+B)² − (u+B)) because 4CuB − u − B = p). So (★) certificates are ambiguous forms of
Richaud–Degert discriminant t² − 4 representing −p, i.e. **fixed points of Gauss's class inversion** on the topograph —
exactly the role Zagier's τ-fixed points play. A Zagier/Legendre-type proof would need the *other* half: a finite set of
forms/rivers on which this inversion acts, plus a second involution σ with a computable fixed set.

**Main line.** Topograph/river structures attached to the certificate forms (cycle of F, its second ambiguous centre,
principal-class membership, period parity) are the natural source of a non-local weight w in Lemma P0. If such a
structure supported an index, some *river-weighted* certificate count would have a parity that is a function of p's
coarse data.

**KILL TEST KT1 (pre-registered before any computation).** For all primes p ≡ 1 (24), p ≤ 2·10⁵ (≈ 2 230 primes), compute
for every unordered (★) certificate and every unordered U₇ word a battery of river weights (≥ 8 bits: cycle length of F
mod 2, [F ~ principal], [second ambiguous centre of F's cycle has leading coefficient ≡ −1 mod 4C], [−F ~ F], period
of the regular CF of the fixed point mod 2, and their products), giving count vectors W_w(p) mod 2. **The main line is
DEAD if no GF(2) combination of the W_w(p), fitted on the primes ≤ 10⁵, predicts W(p) mod 2 = a function of
p mod 840 on the held-out primes in (10⁵, 2·10⁵] with agreement > 60 %, and no single W_w is constant on the primes
of any fixed class mod 840.** It is also DEAD if the only always-odd combinations are explained by a non-certificate
central point (the WINDMILL §3.5 pattern).

**KT2 (Legendre forced divisor; secondary).** For N_C = 4Cp + 1 (C ≤ 40), the reflection of the principal cycle of
discriminant N_C has a second centre which (when N(ε) = +1) is an ambiguous form giving a parity-forced divisor a_C | N_C.
Dead if the rate of a_C ≡ −1 (mod 4C) is within 3σ of the random-divisor baseline (no enrichment ⟹ the river forces a
divisor but not its class: B2 in river coordinates).

**Escape hatch to examine if KT1/KT2 kill:** (i) indices supported on U₇ / full Type II whose easy side carries the
quadratic character (fable-2 / astra-2 remnants); (ii) the Stokes form (d) with a p-dependent acyclic complex (HJ trie /
Farey complex), where the weights are filling-dependent and are not a fixed dictionary.

## 4. Computations

### 4.1 KT1 — river weights on certificate forms: exact form fires; literal 60 % clause met only by explained near-identities

Run: `python3 scripts/z62_parity_river.py 200000 <extras>` → `data/z62/parity/kt1_river_2e5.tsv` (all **2 212** primes
p ≡ 1 (24) ≤ 2·10⁵, then control rows: the 12 (★)-zeros < 3·10⁶ (7 of them repeat main-loop primes), Z₇, 68 odd squares;
3.5 s). The analysis scripts deduplicate and bound the population to p ≤ 2·10⁵: **train p ≤ 10⁵ (1 181 primes), test
(10⁵, 2·10⁵] (1 031)** (the first version double-counted 6 controls; the nullity below is unchanged). Columns: for each
family STAR ((★), unordered), U7 (unordered U₇ words), ALLX (all unordered words of X(p) = {tuv − u − v = p}) and each of
8 weights and their 28 pairwise products, the count W_w(p). Checks: 2·STAR_one = R(p) against brute force (4 random
primes and the zeros), ALLX_one = brute-force unordered |X(n)| (11 values), U7_one = 0 exactly at squares and Z₇,
> 0 at all 12 (★)-zeros; the reviewer independently re-enumerated all words to n = 500 and checked the U₇ flag against
the residue-divisor definition (0 discrepancies).

*Deviations from the pre-registered feature list (disclosed):* Gauss cycles of indefinite forms have even length, so
"cycle length mod 2" was replaced by **half-length mod 2** (`half`) and **half-length mod 4 ≥ 2** (`q4`); "second ambiguous
centre ≡ −1 (mod 4C)" was implemented as "**some** ambiguous form of the cycle has |a| ≡ −1 (mod t)" (`ambm1`); and the
"regular-CF period of the fixed point" was replaced by **the HJ length of p/A mod 2** (`hj`), which is *not* a conjugacy
invariant but a marked-position feature of the word (e.g. the STAR words (8,1,14) at p = 97 and (8,2,13) at p = 193
share (t, u+v) = (8, 15) but have different `hj`). The other weights (`half`, `q4`, `prin`, `neg`, `amb`, `sym`,
`ambm1`) are functions of the proper class and t.

*Exact-identity analysis* (`scripts/z62_parity_gf2.py`, `scripts/z62_parity_quot.py`: GF(2) nullspace of
[counts | class indicators mod 840] on the training primes, quotiented by per-word identities; 16 distinct per-word
patterns, per-word identity space dim 95): **prime-level nullspace dim 98 = 95 trivial + 3** (reviewer recomputed 98 on the
clean population). The 3 excess identities all hold on the test primes and all live on ALLX; on interior words
(t, u, v ≥ 2) each is ≡ 0 and the constant sits on boundary words, explained exactly: e.g.
Σ_ALLX (1 + [t = 1] + hj) ≡ #{u = 1 words} + #{HJ-length-1 words} = τ(p + 1) + 3 ≡ 1 (the length-1 words (2, 1, p+1),
(p+2, 1, 1), (1, 2, p+2) are not certificates for p ≡ 1 (4)). No exact identity involves STAR or U7 non-trivially.

*Predictive clause (the reviewer's finding).* The pre-registered kill was phrased as "no combination predicts a
function of p mod 840 with > 60 % held-out agreement". Taken literally, that clause is **not** met:
(i) STAR_one + STAR_hj is 0 on 1 026/1 031 test primes (99.5 %); it is exactly
#{d | p + 1 : d ≡ 3 (mod 4), (p+1)/d > 1} mod 2 (CERTIFIED: 0 mismatches on all 2 212 primes), i.e. the parity of the
u = 1 subfamily of (★) (B(4C − 1) = p + 1), a divisor-type count of p + 1 that is even unless (p+1)/2's divisors ≡ 3 (4)
are unpaired (odd at 18 of 2 212 primes); (ii) the reviewer's class-majority fit of
STAR_one + STAR_ambm1 + STAR_hj + STAR_ambm1·hj (= #{u = 1 STAR words with ambm1 = 0} mod 2, again supported on the
u = 1 subfamily) reaches 80.5 %, because p mod 840 partly determines which small primes divide p + 1. Both are
*mostly-even* counts of an explicit divisor family of p + 1; neither is an odd index, and neither involves a river
weight in an essential way (`hj`/`ambm1` only select boundary words). **Verdict on KT1 (Assessment):** the exact-identity
version fired; the predictive clause was met only by these explained near-identities. I declare the main line dead on
the strength of Theorem R below (which makes every conjugacy-type river weight provably a function of (t, u+v)), and
record this as a deviation from the letter of the pre-registration.

**Lemma R (PROVED).** For a word (t, u, v) of n with σ = u + v, ε = σ mod 2, the substitution x ↦ x − ky,
k = ⌊(v−u)/2⌋, carries F_w = [t, t(v−u), −n] to G(t, σ) := [t, tε, σ − t(σ² − ε)/4] (with m = v − u = 2k + ε the new
constant term is t(k² − mk) − n = −t(m² − ε)/4 − n, and n = t(σ² − m²)/4 − σ; valid for m < 0 and m = 0).

### 4.1′ Theorem R — the certificate matrix is conjugate to the length-two HJ word (t, u+v) (PROVED)

**Theorem R.** Let n ≥ 1 and (t, u, v) ∈ ℕ³ with tuv − u − v = n, σ := u + v. With S(b) := [[b, −1],[1, 0]],
  **S(u)⁻¹ · [[tu − 1, n],[t, tv − 1]] · S(u) = S(t)S(σ) = [[tσ − 1, −t],[σ, −1]].**
In particular the (★) matrix of (u, B, C) is SL₂(ℤ)-conjugate to S(4C)S(u+B), and the U₇ matrix of a word (r, x, y) to
S(x)S(r+y).
*Proof.* S(u)⁻¹ = [[0, 1],[−1, u]]. γ_w S(u) = [[(tu−1)u + n, −(tu−1)],[tσ − 1, −t]], and multiplying on the left by
S(u)⁻¹ gives [[tσ − 1, −t],[−(tu−1)u − n + u(tσ − 1), (tu − 1) − tu]] = [[tσ − 1, −t],[tuv − n, −1]], and tuv − n = σ. ∎
(Reproducible check: `uv run --with sympy python scripts/z62_parity_verify.py 1500` — symbolic identity, the matrix
identity, reduced-cycle equality F_w ~ Q = [σ, −tσ, t] and Lemma R for all 18 048 words of odd n ≤ 1 500, 0 failures.
Earlier ad-hoc runs (not archived) also found F_w ~ G for 26 761 words and F_w ~ Q for 15 208 words of primes ≡ 1 (24)
< 5·10⁴ resp. 3·10⁴.)
*Antecedents:* WINDMILL_REDUCTION §5.2/§8 (discriminant (tσ − 2)² − 4, T + 2 = tτ) and Z1700 (γ = T^u[[−1, 0],[t, −1]]T^v,
whose cyclic conjugation gives the class dependence at once). Theorem R is the explicit elementary conjugacy formula;
its value here is as a *scoping* statement for parity/index weights.

**Corollary R′ (PROVED, scoped).** Any function of the SL₂(ℤ)-conjugacy class of the word matrix — trace; the proper
class, unmarked oriented reduced cycle and river of its form (cycle length, ambiguous/symmetric forms in it, principal
membership, [−F ~ F]); the closed modular geodesic and its length (distinguishing primitive geodesics from iterated
traversals); the *conjugacy-invariant* Rademacher symbol Ψ (not the Rademacher function Φ, which is not a class
invariant) and hence linking numbers with the trefoil; SL₂(ℤ) orbital integrals with a fixed test function — is a
function of (t, u+v) = (4C, u+B) alone, independent of p. The p-dependence of a word is entirely in *which* (t, σ, u)
occur: p = tuv − u − v ⟺ Q_{t,σ}(1, u) = −p for the fixed form Q_{t,σ} = [σ, −tσ, t]. **Not covered:** marked data
(positions, starting points of cycles, e.g. `hj`), conjugacy in Γ(N) / Γ₁(N) for N depending on the certificate
(TRACE's Γ(4C) structure), test functions depending on p, and relations between different words. **Also not
claimed:** that weights which are arbitrary functions of the unbounded pair (C, u+B) cannot carry a parity law — no
theorem here excludes that; KT1 tests only the listed finite feature space.

### 4.2 KT2 — Legendre's parity-forced divisor of N_C = 4Cp + 1: no class enrichment (EVIDENCE)

*Replication:* WINDMILL_REDUCTION §3 already found the Legendre/SQUFOF midpoint to be a certificate only at the random
rate on a Type I slice (N = tp + 1, t odd: 2.2 % of midpoints vs 14.6 % for any divisor pair) and on the e-slice; the
run below is the (★) slice t = 4C with an explicit per-(p, C) baseline.

`python3 scripts/z62_parity_legendre.py 30000 40` → `data/z62/parity/kt2_legendre_3e4_C40.txt` (C ≤ 40 as
pre-registered; a first run used C ≤ 30, `…_C30.txt`). 385 primes p ≡ 1 (24) ≤ 3·10⁴. The principal cycle of
discriminant N_C is reflection-symmetric; its second centre is an ambiguous form (a parity-forced nontrivial divisor
pair of N_C; 11 096 pairs (p, C); exactly one distinct forced pair each, no overlap with the symmetric case — reviewer)
or a symmetric form (N(ε) = −1; 4 304 pairs). Baseline model: the forced pair is a uniformly random nontrivial divisor
pair of N_C (probability q_{p,C} of the class −1 mod 4C; expectation Σq, variance Σq(1−q)); second model: uniformly
random among *coprime* pairs (all forced pairs observed are coprime).

| C ≤ | forced in class | baseline (all pairs) | z | baseline (coprime pairs) | z |
|---|---|---|---|---|---|
| 30 | 483 | 483.8 ± 13.7 | −0.06 | 471.3 ± 13.0 | +0.90 |
| 40 | 503 | 501.9 ± 14.1 | +0.08 | 490.1 ± 13.4 | +0.96 |

(The first version quoted ± 21.3 from a wrong variance formula; corrected.) **No enrichment** under either model
(EVIDENCE, stated range): the parity mechanism forces *a* divisor; nothing here indicates it prefers the (★) class.
291/385 primes get a forced certificate at some C ≤ 40 — one ticket per C, sparser than (★) itself (378/385 have some
(★) certificate with C ≤ 40). KT2's kill condition (within 3σ of baseline) is met.

### 4.3 Escape hatch H2 — signed (ℤ-valued) indices with quadratic-character signs: no relation (EVIDENCE)

`uv run --with sympy python scripts/z62_parity_signed.py 200000 100000 {840, 13440}` → `data/z62/parity/h2_signed_2e5.txt` (also 6·10⁴:
`h2_signed_6e4.txt`). Per word, 10 base signs — the Jacobi symbols (z/p) for z ∈ {t, u, v, u+v, A = tu−1, A* = tv−1,
tuv} and (−1)^t, (−1)^u, (−1)^v — their 45 products and 1; signed counts S_w(p) over STAR, U7, ALLX (168 columns). A
*rational* linear relation Σ c_w S_w(p) = g(p mod M) on the 1 181 training primes p ≡ 1 (24) ≤ 10⁵ was sought, modulo
per-word identities (56 distinct per-word sign patterns). Computation over F_P, P = 2⁶¹ − 1, with a rank sandwich:
the exact rational rank of the pattern matrix is 42 (sympy) = its F_P rank, so the rational per-word identity space W_ℚ
has dimension 126 = dim W_P; the rational kernel K_ℚ of the count matrix satisfies W_ℚ ⊂ K_ℚ and dim K_ℚ ≤ dim K_P.
**Result: prime-level nullspace = per-word identity space exactly (dim 126) for M = 840; excess 0.** For M = 13 440
(384 classes) the 3 excess vectors are supported only on class indicators of classes with no training prime (trivial).
Since dim K_P = 126, K_ℚ = W_ℚ: no ℚ-combination of these 42 independent signed counts equals a function of p mod 840
on the training primes (and none mod 13 440 beyond empty classes) — this extends the board's fable check (six single
signs on U₇ words, constancy only) to the full ℚ-span with class functions. *Scope note:* (−1)^t ≡ +1 on STAR, so H2 does
not test C parity on (★) (that would need (−1)^{t/4}).

### 4.4 Escape hatch H3 (cheap form) — non-local graph-degree weights: no relation (EVIDENCE)

Lemma P0(b)/(d) allows weights depending on *other* words. Cheapest instance: w(c) = number of other words sharing a
datum with c (same u, v, t, u+v, A, uv, tu), neighbours taken in all of X(p) or in the family.
`python3 scripts/z62_parity_nonlocal.py 200000` → `data/z62/parity/h3_nonlocal_2e5.tsv`; analysis with
`z62_parity_gf2.py … 100000 840`. **All 36 nullspace directions are trivial**: 34 columns are identically even
(handshake within a pool, or fibres closed under the family, e.g. a t-fibre with 4 | t is entirely (★)), and 2 are the
coincidence A = tu − 1. No combination involving a non-trivial column is a function of p mod 840.

### 4.5 What the kills leave open (Assessment unless marked)

* PROVED (Theorem R / Cor R′): all *conjugacy-type* data of a single word is a function of (t, u+v). Weights may still be
  arbitrary functions of the word (the word determines p = tuv − u − v), of marked data, of Γ(N)-level data, or of
  relations between words; none of these is excluded by a theorem here. What this lane tested in those directions
  (finite feature spaces: KT1's `hj`, H2's Jacobi signs, H3's fibre degrees) shows no relation with p's residue class.
* An index with uniformly non-zero easy side must be supported beyond (★) (Lemma P1); U₇ support yields ES(p), not (MS).
* **A sufficient construction that nobody has (ML-P).** *A finite set S_p ⊇ U₇-words(p), computable from p, with
  involutions σ, τ such that Fix τ = F_cert ⊔ K_p (F_cert mapped to U₇ words), |Fix σ| − |K_p| provably odd at every
  large prime p ∈ 𝔐 (e.g. Fix σ a factorisation of p), and τ neither an equation symmetry on a Zariski-dense piece
  (WINDMILL Prop 2) nor a finite affine menu ((J)2).* This is one sufficient shape (Lemma P0(a)), not a necessary form of
  every parity proof. No candidate was found; every structure tried (river of the certificate form, Legendre's principal
  cycle, Jacobi-signed and fibre-degree counts) either reduces to conjugacy data (Theorem R) or showed no class bias /
  relation in the tested ranges.

## 5. Verdict

**Narrowed.** No HOT LEAD; no new forcing mechanism. B2 did not move.
* **Dead / negative (EVIDENCE or CERTIFIED in the stated finite ranges and feature spaces):** the main line — river
  weights of certificate forms in a parity identity (KT1: exact version fired; the literal predictive clause was met
  only by explained divisor-of-(p+1) near-identities, see §4.1; declared dead on the strength of Theorem R, a recorded
  deviation); Legendre's parity-forced divisor of 4Cp + 1 shows no class enrichment (KT2: z = +0.08 / +0.96 at C ≤ 40);
  Jacobi-signed word counts have no ℚ-relation with class functions mod 840 (H2); fibre-degree weights are
  handshake-trivial (H3).
* **Proved:** Lemma P0 (restatement, with the Morse/Stokes forms and the correct disjointness / Lefschetz hypotheses),
  Lemma P1 (trivial), Lemma R, **Theorem R: S(u)⁻¹[[tu−1, n],[t, tv−1]]S(u) = S(t)S(u+v)** (explicit form of Z1700's
  factorisation), Cor R′ (all SL₂(ℤ)-conjugacy data of a word are functions of (t, u+v)).
* **Survives (not excluded by anything here):** arbitrary weights in (C, u+B) or in the word beyond the tested feature
  spaces; marked/position data; Γ(N)-level conjugacy; relations between words (ML-P is one sufficient shape); easy sides
  with thresholds.

### Falsifier table (re-stated for the final state)
| screen | KT1 / Cor R′ weights | KT2 Legendre divisor | H2 Jacobi-signed indices | (ML-P) |
|---|---|---|---|---|
| F1 squares | at m² the STAR/U7 families are empty, so any weighted count is 0 | forced divisors exist at m² too (no class preference seen anywhere) | (z/m²) ∈ {0, +1}; families empty at m² | easy side must vanish at m²; Jacobi-type is the natural (not forced) shape |
| F2 C-even | conjugacy weights see C only through t = 4C; C mod 2 is one fixed feature among (C, u+B) | the (★) slice includes C even; no separation built in | (−1)^t ≡ 1 on STAR: C parity untested | support must reach beyond the 8-line (C odd for (★); non-U⁽⁸⁾ targets for U₇) |
| F3 composites | identities are uniform in n; nothing prime-specific | — | — | prime-only identity or divisor-type easy side |
| F4 zeros | (★)-supported identities must vanish at the 14 zeros (Lemma P1) | at the 14 zeros no C ≤ 40 gives a certificate (they are (★)-zeros) | — | U₇ support (no known prime zero); yields ES(p), not (MS) |

### FRONTIER §4 hard screens for Theorem R
Theorem R is an identity, not an existence mechanism: the four screens are **not applicable** (it neither proves nor
predicts certificates). Reading: it moves the tie out of the conjugacy class — the class is that of the fixed word
(4C, u+B) — and leaves all of it in the position datum Q_{4C,σ}(1, u) = −p.

### Proposed FRONTIER §6 text (do not edit FRONTIER here)
*(z62 PARITY) Topograph / river / closed-geodesic weights of certificates in parity identities → every SL₂(ℤ)-conjugacy
invariant of a word matrix is a function of (t, u+v): S(u)⁻¹[[tu−1, n],[t, tv−1]]S(u) = S(t)S(u+v) (`Z62_PARITY.md`
Theorem R; explicit form of `z52b_pass1_H05` Z1700). Finite river-weight dictionaries give no parity law (KT1, primes
≤ 2·10⁵); Legendre's parity-forced divisor of 4Cp + 1 shows no (★)-class enrichment (KT2, replicating
WINDMILL_REDUCTION §3 on the (★) slice); Jacobi-signed word counts satisfy no ℚ-relation with class functions mod 840
(H2); fibre-degree weights are handshake-trivial (H3). Not excluded: arbitrary weights beyond these finite feature
spaces, marked/Γ(N)-level data, relations between words.*

### Bottom line
Every parity/index argument of the standard shapes is a weighted certificate count with a computable non-zero total
(Lemma P0). The natural geometric source of weights — the river/topograph of the certificate's own form — is p-free:
the certificate matrix is conjugate, by S(u), to the length-two Hirzebruch–Jung word (4C, u+B) (Theorem R), so all
conjugacy-type weights are functions of (C, u+B); the finite dictionary of them tested here carries no parity law.
Legendre's classical parity-forced divisor of 4Cp + 1 hits the (★) class at the random rate, and Jacobi-signed and
fibre-degree indices satisfy no relation with p's residue class. A parity proof would still need an involution built
from data beyond a single word's conjugacy class (ML-P is one sufficient shape); no candidate is known.

## 6. Internal hostile review (done) and fixes
Reviewer subagent (deep mode), commit range 8c4b5166..: 8 MAJOR, 4 MINOR, no FATAL; all applied:
(1) KT1's literal 60 % clause is met by near-identities (STAR_one + STAR_hj at 99.5 %, a class-majority fit at 80.5 %) →
§4.1 now reports this, explains both as divisor-of-(p+1) counts of the u = 1 subfamily (CERTIFIED identity), and records
the "dead" verdict as a deviation resting on Theorem R; (2) feature deviations disclosed, `hj` identified as a
marked-position feature; (3) Lemma P0(a) needed a disjoint decomposition and the oddness requirement, ML-P demoted to a
sufficient shape; (4) Lefschetz hypothesis made explicit; (5) Theorem R/Cor R′ no longer claimed to exclude arbitrary
(C, u+B)-weights or to force "relations between words"; (6) falsifier tables rescoped (Lemma P1 = uniform non-vanishing;
full-ES support is not square-vanishing; U₇ support gives ES not (MS); F2 for U₇ per FRONTIER; (−1)^t ≡ 1 on STAR);
(7) KT1 population deduplicated (2 212 primes, split 1 181/1 031; nullity 98 unchanged); (8) KT2 variance corrected
(± 13.7, not ± 21.3), coprime-pair baseline added, run at the pre-registered C ≤ 40; (9) Rademacher symbol vs function;
(10) H2 rank sandwich with exact rational rank 42 archived; (11) Z1700 credited; (12) explicit conjugator S(u) and a
verification entry point (`scripts/z62_parity_verify.py`). The reviewer reproduced the TSVs, the 26 761-word cycle check,
H2 (126/0), H3 (36 trivial) and KT2's forced-pair structure.
