# R203 — hostile review of COMPOSITION_ES.md (O203)

Reviewer: R203 side agent (branch side-agent/review-composition). Document reviewed at merge of
side-agent/composition-es @ 75ad4b51. From-scratch scripts: `scripts/review_cp_*.py`.

Status: round 1 complete.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1, Prop 1.2 (composition law, r odd/primitive/∏D \| μ, sign(Nα) = χ₋₄(\|Nα\|), no norm −1 unit) | SOUND |
| Thm 1.3 (B = 1 slot = ε_μ = 1 − 2jη̄, D = 4tj − 1, incl. depth-1 μ ≤ 2n, primitivity) | SOUND |
| Cor 1.4 (fixed-μ no-go for composition) | SOUND-AFTER-REPAIRS (M1: (a) false as worded; m1) |
| Prop 2.1 (box, δ-fibre, 𝔢_μ always of class δ, T1 at squares), Remark 2.2 (third reduced ideal) | SOUND (m2 wording) |
| Prop 3.1 (Davenport gives wrong sign; (ℤ/2)² target-sum example) | SOUND (abstract group statement, labelled as such) |
| Prop 4.1 (finite B = 1 locus, μ ≤ n² + n + (n+1)/4; Type II = d-sliced B = 1 points of V_{pd}; 99 primes) | SOUND (m3, m9) |
| Prop 5.1 (Type II ⟺ two-term Machin/arccot relation ⟺ 4csdj = pj + c + s) | SOUND (m4, m5 in the Reading) |
| §5 cross-composition EVIDENCE | SOUND as EVIDENCE (m6) |
| Census EVIDENCE (cp_census 5 1000) | SOUND — all 7 figures reproduced exactly from scratch; does not use the 1000–3000 file (m7) |
| Labels (“composition cannot help select μ” = Assessment) | SOUND-AFTER-REPAIRS (m8) |

No FATAL defect. One MAJOR (M1: a PROVED corollary false as literally worded — the B = 1 element ε_μ CAN be a
composition of V_n points at μ when N(ε_μ) ∤ μ; only “is an ES point” is excluded). ES is not claimed solved.

## Claim-by-claim

### §1 Lemma 1.1, Prop 1.2 (composition law) — SOUND
Re-derived: N(B − Aη̄) = B² − 2μAB + nA², so V_n ⟺ N α = −D; A even ⟺ y even ⟺ α ∈ O'; gcd(x, y) =
gcd(B − μA, A) = gcd(A, B); y > 0 ⟹ (x + μy)(μy − x) = ny² + D > 0 with positive sum, so the condition
“x + μy > 0” in the lemma is redundant (harmless). −ᾱ ↔ (A, 2μA − B) ✓. Product formula: expand with
η̄² = 2μη̄ − n ✓. (b): split of ℓ | D uses only ℓ odd, ℓ ∤ f (gcd(D, n) = 1 and ℓ | μ give f ≡ −n ≢ 0), and a
primitive element lies in one prime above ℓ ✓. (c): x odd, 4 | y² ⟹ N ≡ 1 (mod 4) ✓.
Note: gcd(B, n) = 1 is automatic only GIVEN gcd(D, n) = 1 (MARKOFF Thm 4.1 assumes it); without it there are
points with gcd(B, n) > 1, e.g. n = 21, μ = 7, (A, B, D) = (4, 7, 7). The lemma's target set does impose
gcd(D, n) = 1 and the two conditions are equivalent given D | μ (ℓ | D, n ⟹ ℓ | μ ⟹ ℓ | B), so no defect.
`scripts/review_cp_law.py`: brute-force points (13 values of n incl. even 26, 34, 38; μ ≤ 4n; A ≤ 24): 138
points, norm/ι_B/sign checks, 316 pair products (formula + “even products never points”), 688 triples incl.
all triples with ∏D | μ (point ⟺ primitive ∧ ∏D | μ), 3939 abstract triples testing the prime-level
primitivity criterion, 20 000 random sign-rule checks — 0 failures.

### Thm 1.3 — SOUND
Re-derived line by line: D > 0 ⟹ μ > nj + 1/(4j); D ≤ μ ⟹ μ ≤ nj + (nj + 1)/(4j − 1) ≤ nj + n (n + 1 ≤ 3nj);
so t := μ − nj ∈ [1, n], j = ⌊(μ − 1)/n⌋, D = 4tj − 1, N(ε_μ) = 1 − 4j(μ − nj) ✓. 4tμ ≡ n + 4t² (mod D) and
gcd(4t, D) = 1 ✓. Depth-1 case: μ ≤ 2n ⟺ j = 1 is included (nothing in the proof needs j ≥ 2); μ ≤ n gives no
point ✓. Primitivity of ε_μ: gcd(1 − 2jμ, 2j) = 1 ✓. The proof never uses non-square f or odd n (for μ > n,
f = μ² − n is never a square anyway). Brute force (all μ up to bound + 3n, odd n ≤ 81 and even n ≤ 60, all
even A): 216 B = 1 points, all equal to the predicted (2j, 1, 4tj − 1, nj + t), set equality with Prop 4.1(a)
enumeration — 0 failures.

### Cor 1.4 — SOUND-AFTER-REPAIRS (defect M1, m1)
The intended content (no V_n point with B = 1 at μ unless N(ε_μ) | μ; at a fixed μ, composition cannot create an
ES point) is correct and immediate from Thm 1.3. But (a) as WRITTEN — “no element of O'_μ obtained by any
operation (products, units, …) from V_n points at μ has B = 1” — is FALSE: see M1 (explicit counterexample
p = 11, μ = 18). The chain criterion in (b) re-derived: given ε_μ = uα₁α₂α₃, take 𝔡₁ = (α₁), 𝔡₂ = (α₁α₂);
conversely quotient ideals are principal with generators in O' (norms odd and prime to the conductor since
gcd(D, f) = 1), primitive (divisors of a primitive ideal) and of norm | D | μ ✓. Note D_i ≥ 3 is automatic
(no norm −1 elements), and a decomposition with r = 5, 7, … implies an r = 3 chain, so “longer chains likewise”
is superfluous. The R-O203 #3 example (n = 29, μ = 60, D = 15) is correct: D has only two prime factors, so no
chain is possible.

### §2 Prop 2.1, Remark 2.2 — SOUND (minor wording, m2)
δ is well defined (all units of O' have norm +1, Prop 1.2(c)), δ ≠ 1, δ² = 1, δ ↦ 1 in Cl(O') ✓. χ₋₄ is a genus
character on Cl⁺(O') (re-derived: for 𝔞 = (β/γ)𝔟 with β, γ ∈ O' of odd norm, χ₋₄(Nβ) = sign Nβ, so χ₋₄(N𝔞) =
χ₋₄(N𝔟)·sign N(β/γ)), χ₋₄(δ) = −1 ✓. |𝔅(μ)| = ∏(2v_ℓ + 1) ✓. (a) ✓ except wording (m2). (b) R-O203 #2 example
checked: f = 2863, N(−107 + 2√2863) = 11449 − 11452 = −3, α(−ᾱ)α = −N(α)α = 3α ✓. (c) (ε_μ) = (D, ε_μ) has class δ for
every μ ✓ — this is the real content of “B = 1 is not a class condition”. (d) (−m²/ℓ) = (−1/ℓ) ✓; also directly:
D ≡ 3 (mod 4) cannot divide m² + 4t² with gcd(D, 2t) = 1; recount: 0 ES points at the 21 odd squares 9…1849.
Remark 2.2: a₀ = 2μ − 1 for μ > n, and for μ > 2n the first convergent elements are 2η̄ − 1, 2η̄, 2jη̄ − 1 with norms
4n − 4μ + 1, 4n, 1 − 4tj (`review_cp_law.py`, 557 values of μ incl. all n < μ ≤ 2n, 0 failures); consistent with
MARKOFF Thm 4.3 (k = 3), depth-1 case μ ≤ 2n handled (j = 1, ε_μ = −(2η̄ − 1)).

### §3 Prop 3.1 — SOUND (as an abstract group statement; label already says so in §7.3)
(a) a zero-sum from Davenport is a narrowly principal ideal, all generators totally positive ✓ (one prime per ℓ ⇒
primitive). (b) the (ℤ/2)² example: 3-mod-4 primes must have χ₋₄ = −1, i.e. class in δ·ker χ₋₄; choosing δg with
χ₋₄(g) = 1 is consistent and signed subset products stay in {1, δg} ✓. It is a group-theoretic non-implication,
not an arithmetic theorem — the text says this (“Whether the example occurs in some O'_μ is not claimed”). (c) ✓.

### §4 Prop 4.1 — SOUND (nit m3)
(a) from Thm 1.3 ✓; bound μ ≤ (n + 1)t + n(n + 1)/(4t), convex in t, endpoint t = n wins over t = 1
((4n² + 5n + 1)/4 vs (n² + 5n + 4)/4) ✓ — the proof's “maximal at t = n” omits this comparison (m3). Brute force
(all μ, odd n ≤ 81, even n ≤ 60): max μ/bound = 0.54, never exceeded. (b) re-derived: B = 1 at V_{n'} ⟺
n'A² + 1 = D·g, g = 2λA − 1; with A = 2j, n' = pd: g ≡ −1 (mod 4dj) ⟺ d | λ, and h | 4dj²p + 1 ⟺ h | pj + c
(FIXED_MODULUS_SHOTS Lemma 1.1, statement checked in the repo). The constraint d ≤ (p + 1)/3 is automatic (from
(4dj − 1)² ≤ 4dj²p + 1 one even gets d ≤ (p + 2)/4). `review_cp_typeii.py 100`: for all primes 5 ≤ p ≤ 100, cube
points from the definition (enumerated via (c, d, s), j = (c + s)/(4cds − p)) = d-sliced B = 1 points of V_{pd}
computed by factoring n'A² + 1 for all j ≤ n' (214 = 214, 0 failures). Even n' = pd: Lemma 1.1/Thm 1.3 indeed never use
the parity of n; the R-O203 #5 example (p = 13, (c, d, j) = (1, 2, 1) → V₂₆ point (2, 1, 15, 30)) checks.
(c) the “99 primes < 10⁶” figure recomputed from scratch (`review_cp_typeii.py 5 1000000`: ES point at V_p ⟺ some
t ≤ (1 + √(4p + 1))/4 with a divisor ≡ −1 (mod 4t) of p + 4t², using the c ↔ s symmetry of the cube): **99**,
starting 13, 37, 97, 181, 193, 541, … ✓. Label: the equivalence is PROVED, its strategic reading is marked
Assessment ✓.

### §5 Prop 5.1 (Machin/arccot dictionary) — SOUND (minor m4, m5)
(ii): (2cd + w)(2sd + w) = (4csd² − pd) + 2d(c + s)w, w² = −pd; proportional to 1 + 2jw with factor d(c + s)/j iff
j(4csd − p) = c + s ⟺ (i) ✓. (iii): cot(θ₁ + θ₂) = (ab − 1)/(a + b) = (4csd − p)/(2(c + s)√(pd)); θ₁ + θ₂ ∈ (0, π)
where cot is injective, so (iii) ⟺ (i) ✓. Egyptian identity = (i)/(pcdsj) ✓. Checked exactly (Fractions) for
(ii)/Egyptian and at 60 digits for (iii) on all 214 cube points p ≤ 100, plus the converse ((i) false ⇒ (iii) false)
on a box c, s ≤ 5, d, j ≤ 3 for every p ≤ 100 — 0 failures. Primality of p is not used (harmless). The identity
is, as the author says, an equivalent restatement — no existence content. Todd 1949 remark is flagged “from
memory, not re-checked”; I could not access it either (no source in sources/); it is not load-bearing.

### §5 EVIDENCE (cp_cross) — SOUND as EVIDENCE (m6)
Independent recount (`review_cp_cross.py`, own divisor test): X = 120: n = 59: 14 points, 123 admissible pair
products, 0 hits; n = 101: 21 points, 199 admissible, 0 hits; X = 40 likewise 0. Matches. Triples not recounted.

### Census (cp_census 5 1000) — SOUND (EVIDENCE), m7
From-scratch recomputation (`review_cp_census.py 5 1000`, own CF code tracking convergents mod D only, own
orientation test j·x + (2jμ − 1)·y ≡ 0 (mod d′)): **166 primes, 1736 ES points, D prime 690, composite 1046,
decomposable 284, V-decomposable 41, primes with ≥ 1 decomposable 88; ES element at k = 3 (μ > 2n) / k = 1
(μ ≤ 2n) in all 1046 composite cases** — every figure reproduced exactly (log `logs/review_cp_census_5_1000.txt`).
n = 59, μ = 135: principal divisors exactly {9, 15} ✓. Lagrange is applicable: d′ < D ≤ μ < 2√f = √N for μ > n.
The document does NOT use data/cp/census_1000_3000.txt (only the agent report mentions an unfinished run);
however the directory data/cp/ does not exist in the branch at all (m7). R202's “two V-decomposable cases among
odd n ≤ 301, μ ≤ 6n” not rechecked.
Extension (reviewer's own run, EVIDENCE, not used by the document; `review_cp_census.py 1000 3000`, 51 s, log
`logs/review_cp_census_1000_3000.txt`): 262 primes, 4314 ES points, D prime 1393, composite 2921, decomposable 827
(28%), V-decomposable 124, primes with ≥ 1 decomposable 175/262, ES-element index check 0 mismatches — same picture.
(The author's own 1000–3000 run was still in progress with an empty output file when this review was written.)

### §6 barrier screen, §7 verdict, labels — SOUND-AFTER-REPAIRS (m8)
§6(ii): O/η̄O ≅ ℤ/n via √f ↦ μ (η̄ primitive, index = |N η̄| = n) and α = B − Aη̄ ↦ B ✓; B = 1 ⟺ B ≡ 1 (mod n) and
0 < B < n + 1 ✓. “Composition cannot help select μ” is labelled Assessment in Cor 1.4 (R-O203 #1), Prop 4.1(c),
§7.5 and the report ✓. One unlabelled strategic claim remains (m8). ES is nowhere claimed solved ✓.

## Numbered defects

**M1 (MAJOR — false statement as worded; substance survives). Cor 1.4(a)** (and the echo in §0 X2 “No operation
inside O_μ can change that”, §7.2 “any operation inside O'_μ cannot create an ES point” is fine).
Cor 1.4(a) says that if 4tj − 1 ∤ μ, NO element obtained from V_n points at μ by products/units/conjugation/
quotients “has B = 1”. Counterexample (`scripts/review_cp_cor14.py`, exact): n = 11, μ = 18, j = 1, t = 7,
D = 27 ∤ 18. The prime of norm 3 below (ε₁₈) is principal with generator α of norm −3, i.e. the V₁₁ point
(A, B, D, μ) = (46766, 14413, 3, 18), and ε₁₈ = 1 − 2η̄ = u·α³ with u = −32188120829134849 − 1819380158564160√313,
N u = 1, u ∈ O'. So the B = 1 element ε_μ IS a composition (unit × 3 V_n points, primitive product) — it just
is not a V_n point because 27 ∤ 18 (Prop 1.2(b) correctly says so). Census: such “non-ES compositions” (𝔢_μ =
product of three principal negative-norm ideals each of norm | μ, D ∤ μ) occur 40 times for primes p ≤ 120
(`review_cp_census.py 5 120 nonES`, log `logs/review_cp_census_nonES_5_120.txt`).
*Repair:* replace “has B = 1” by “is a V_n point with B = 1 (an ES point)”, and add one sentence: “Composition can
reach the B = 1 element ε_μ itself even when N(ε_μ) ∤ μ (e.g. n = 11, μ = 18: ε = u·α³, N α = −3); it is the
scalar condition N(ε_μ) | μ, not reachability, that fails.” This actually sharpens the paper's thesis (B = 1
is reachable; the divisibility is the whole content).

**m1 (MINOR). Cor 1.4(b)**, “obtained by composition … in the trivial sense ε_μ = ε^k·(ε^{−k}ε_μ)”: ε^k is a unit, not
a V_n point, so this is “unit × ONE V_n point”, not a composition of V_n points. *Repair:* say so (“trivially, as a
unit multiple of the B > 1 point ε^{−k}ε_μ of the same orbit”). Also “(longer chains likewise)” can be dropped: any
r ≥ 3 decomposition yields an r = 3 chain via 𝔡₁ = (α₁), 𝔡₂ = (α₁α₂).

**m2 (MINOR). Prop 2.1(a)** “The V_n points with α ∈ 𝔡 form, up to ι_B, one orbit of ε”: ι_B (α ↦ −ᾱ) maps generators
of 𝔡 to generators of 𝔡̄ ≠ 𝔡. Correct statement: “the V_n points whose α GENERATES 𝔡 form exactly one ε-orbit
(after the normalisation y > 0); ι_B maps it onto the orbit belonging to 𝔡̄.” (“α ∈ 𝔡” should be “(α) = 𝔡”.)

**m3 (MINOR). Prop 4.1(a) proof**, “convex in t, maximal at t = n”: add the endpoint comparison t = 1 vs t = n
((n + 1)(n + 4)/4 ≤ n² + n + (n + 1)/4).

**m4 (MINOR). §5 Reading**, “i.e. (by norms) (4cdj − 1)(4sdj − 1) = 4dj²p + 1”: this identity is direct algebra from
(i) (expand: 16csd²j² − 4dj(c + s) + 1 = 4dj·pj + 1); the norms of (ii) give a different identity,
(4c²d + p)(4s²d + p)j² = (c + s)²(1 + 4j²pd). *Repair:* replace “(by norms)” by “(expanding with (i))”.

**m5 (MINOR). §5 Reading**, “For d = 1 it is the real-quadratic slot ε_μ … (D = 4tj − 1 with t = c)”: under the
Prop 4.1(b) map (λ = cd = c) one gets μ = c(4sj − 1) = pj + s, so **t = s**, D = 4sj − 1 (t = c holds for the
mirror cube point (s, 1, j)). *Repair:* “t = s (or t = c for the mirror point (s, d, j))”.

**m6 (MINOR). §5 EVIDENCE**: the size-matched random baseline is also 0, so the experiment cannot distinguish
composition from chance; the sentence “Composition in ℤ[√−n] does not preserve V_n” should read “… was not observed
to produce V_n points (0 hits, as for the random baseline)”.

**m7 (MINOR). Data**: the report says “Data: data/cp/”, but data/cp/ is not in the branch (no census output
committed; census_1000_3000.txt does not exist). The document itself relies only on the p ≤ 1000 run, which I
reproduced exactly. *Repair:* commit the p ≤ 1000 census output (or drop the data/ reference) and delete the
mention of the unfinished 1000–3000 run from the report, or mark it “not used”.

**m8 (MINOR, label). §6 B3**: “composition cannot transfer the large ES^{[2]} main term to B = 1 because B = 1 is not a
class/ideal condition” is a strategic reading, not a theorem (Prop 2.1(c) proves only that 𝔢_μ has class δ for every
μ). *Repair:* prefix “(Assessment)”.

**m9 (MINOR). Notation paragraph**, “all of Type II is covered by the slices V_{nd} (Prop 4.1(b))”: Prop 4.1(b) is
stated for n = p prime (FIXED_MODULUS_SHOTS Lemma 1.1 needs p prime). *Repair:* “for n = p prime”.
