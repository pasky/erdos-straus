# R203 — hostile review of COMPOSITION_ES.md (O203)

Reviewer: R203 side agent (branch side-agent/review-composition). Document reviewed at merge of
side-agent/composition-es @ 75ad4b51. From-scratch scripts: `scripts/review_cp_*.py`.

Status: IN PROGRESS.

## Summary verdicts

(filled in claim by claim below)

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
