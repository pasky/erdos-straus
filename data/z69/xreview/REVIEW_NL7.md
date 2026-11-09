# NL7 hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN; U₇ at all primes is not proved.**
Reviewed `side-agent/z69-nl7` at `f4c4112d5dfea2c3794b17899428ff1a0f0193f2`, including scripts/data and the specified Z60/Z68 context.
The formal obstruction theorems survive independent proof reconstruction. The claimed exhaustive square-class census does not: it silently tests only units. Some summary/filter wording also drops an essential hypothesis.

## Per-claim audit

| Claim | Classification | Independent audit |
|---|---|---|
| Lemmas 1–3, witness equivalence | CORRECT | All three divisor/letter bijections, the y=1 exception, Jacobi coprimality, letter bounds and large-letter reduction check out. Existing selftest rerun: zero mismatches below 1500. |
| Lemma 4, mathematical statement | CORRECT | q>c ensures q∤c. Divisors c′q^ε and complementary divisors transfer modulo 8L; this also preserves (e+1)/L modulo 8 in the z-position. Choose any nonzero odd representative m of the square root. No unit hypothesis is needed. |
| Lemma 4 “all odd n<4·10⁵” census | CORRECT-WITH-FIX | Original counts reproduced exactly, but `is_odd_square_mod` rejects gcd(n,8cL)>1 and the loop omits n=1. Full independent check gives larger counts, still zero counterexamples; details below. |
| Lemma 5 / admissible H system | CORRECT (conditional implication) | After division by cᵢ, each small prime sees a constant nonzero residue; for ℓ>C*, the product retains its degree <ℓ and cannot vanish everywhere. Affine substitution preserves ℚ-irreducibility; admissibility forces primitivity. Repeated/associated factors cause no problem. |
| Lemma 6 / Theorem ID | CORRECT | A largest real root of X forces a later root of Z where X<0, contradiction; symmetry removes Z-roots, then positivity excludes Y-roots. The identities give XY−1,YZ−1>0. All specializations in the integer/U₇ class are positive, including negative parameters. |
| Corollaries 6.1–6.3 | CORRECT | Positivity prevents leading cancellation; degrees sum to deg P. The quartic factor classification and μP+1 irreducibility argument check. In 6.3 all three stated moduli preserve integrality and 8-divisibility; Hensel/CRT uses unit squares at odd primes and 1 modulo 8. |
| Theorem NL | CORRECT, CONDITIONAL on H | Constants are chosen non-circularly. Quadratic point count leaves a square class avoiding all gⱼ-roots at new primes. LC handles old primes/T₀; c_P=1. H controls every required factor, not merely E. Degrees ≥3 exceed the letter bound, degree 2 forces a bounded letter, degree 0 dies by Lemma 4, and degree 1 would yield an impossible polynomial word. |
| Theorem NL-W | CORRECT, CONDITIONAL on H | f≤2p+2 handles high degree; quadratic/constant f forces a bounded letter. Adding the linear factor of F+1 makes xy=ρπ a finite menu of polynomial pairs; Lemma 7 plus the Sign Lemma excludes the remaining linear case. |
| Rule definition and Corollaries G/P/Q/J | CORRECT-WITH-FIX (summaries) | §4.1 correctly requires nonzero restrictions. Gaussian/normalized Bezout, both Pell solutions, fixed-index CF convergents/unit powers, and fixed-coordinate norms are polynomial on the stated curves. This does NOT include arbitrary adaptive indices or arbitrary norm-solving data. K6/§6 lose the nonzero-restriction caveat; fix below. |
| Proposition 3.4 / Corollary 3.6 | CORRECT, CONDITIONAL on H | Smooth projective quartic double cover has genus 1; subtract ≤2 infinity points and ≤4 branch points to obtain (ℓ−5−2√ℓ)/2 square classes. Finite rational-function menus become polynomial words, necessarily type (2,2,0) here, with an integer constant letter when actually used. Reduction only; IRR supplies the extra exclusion in 3.6. |
| Theorem NL⁺ | CORRECT, CONDITIONAL on H | E(0)≠0 bounds the initial smooth factors. The pre-K finite polynomial menu bounds denominators; actual denominators are C*-smooth. The Sign Lemma excludes zero-at-0 factors in the used shifts. Thus 8D divides t, specialization gives positive integer letters with 8∣XY at P(0)=1: contradiction. No circular modulus enlargement found. |
| Lemma 8 / Theorem NL-J | CORRECT, CONDITIONAL on H for NL-J | Eisenstein/positivity, μ=6 as the sole reducible P₁+μ, and the H∣64 contradiction for μP₁+1 all check. LC′ makes F₁,F₂ actual primes ≡1 modulo 3. Every divisor of p+6 is then 1 modulo 3, excluding x=6 or z=6; y=6 is separately removed by Lemma 4. |
| Proposition SG | CORRECT | Both signs verified symbolically and numerically. Positive/integral letters and 8∣x hold on exactly the stated sufficient classes. It is a legitimate quartic boundary example, not a mechanism for general primes. Classical-parametrization attribution is missing; see below. |
| §5 direct attacks | CORRECT-WITH-FIX (scope) | Coprime mutual-divisibility converse, restricted descent bijection, sign-mismatch algebra and size obstruction are sound. Failure of these ansätze does not exclude adaptive combinations or other descents. “No Vieta-type involution exists” is justified only for a single-coordinate root exchange. The order-4 observation supplies no new word; §5.6's “all prime factors split” also needs a ramified/non-unit qualification. |
| Headline numerical examples | CORRECT on rerun | Three R-G failures and least letter 6 reproduced; quartic 26 primes with 2 J-failures/8 c-failures reproduced. SG and certificate totals reproduced. Larger zero-failure censuses were not independently rerun and remain finite evidence, not theorem support. |
| “narrowed” verdict / labels | CORRECT-WITH-FIX | Supported only conditionally on H and within the displayed scopes. Quartic reduction is not failure; witnesses are not covered by NL-J. No general U₇ or ES proof appears. SG does not establish literature priority. |

## Decisive computations

Independent code: `scripts/z69_xrev_nl7_check.py` (no lane-library imports; bounded ~40 MB sieve).
For 3≤n<400000 odd, the same eleven L and c≤200:

| Position | Original unit-square cases | Full square-class cases | Full square cases with a word | Complementary cases / with word |
|---|---:|---:|---:|---:|
| x | 120550 | 133140 | 0 | 1262820 / 448318 |
| z | 120550 | 133140 | 0 | 1262820 / 365130 |
| y | 106207 | 143259 | 0 | 1106590 / 352414 |

Including n=1 adds six square-class cases per position, all without words.
Concrete omissions: n=9,L=6,c=3,q=5 has n=3² modulo 144; n=9,L=3,c=4,q=7 is the y-case modulo 96.
Correct odd-prime criterion: if vℓ(n)<a for ℓᵃ∣M, require vℓ(n) even and the remaining unit a quadratic residue; vℓ(n)≥a is allowed. Rejecting every non-unit is not this criterion.
SG: exact symbolic identities for ε=±1; 3175 positive and 3175 negative admissible s with |s|<200000 checked. Lane SG run reproduces 71 primes with 5∣s and first p=85030560001.
Primality rerun: 26 quartic primes, 71 SG primes, all factors used for headline failures; 85 recursive Lucas certificates and 8 factor occurrences above 2⁶⁴, matching the memo. Above-2⁶⁴ census tests outside these certificates remain BPSW evidence.
NL-J rerun: shifts factored for μ≤3000, only P₁+6 reducible; LC′ at every odd prime <400; 138 triple-prime samples, zero x/z=6 hits, 87 y=6 hits; 1406 joint-rule prime samples, zero failures. The 138/1406 counts are not unconditional prime certificates above 2⁶⁴.

## Falsifier table

| Screen | Independent outcome / interpretation |
|---|---|
| F1 odd squares | Jacobi obstruction and Lemma 4 transfer are valid. SG contains no square; independently checked numerically and immediate from (4s²)²<n<(4s²+1)² for s≠0. |
| F2 12 C-even R₈-zeros | All 12 independently re-witnessed for U₇; no SG members. Obstruction-to-subline transfer is logically correct. SG has 8∣x, so it actually lies in the numerator-8 A-half U⁽⁸⁾; it does NOT demonstrate escape from that restriction. This is distinct from the C-even B-subline. |
| F3 285 composite zeros | All 285 tested: 277 U₇-positive; exhaustive f≤2n+1 search leaves exactly Z₇. None belongs to SG. Lemma 4 works at composites; the H theorems construct primes and make no universal composite assertion. |
| F4 14 (★)-zero / 38 𝔊*-zero primes | All 14 and all 38 independently re-witnessed; none belongs to SG. A polynomial-rule failure is not a U₇ failure. The table claims no positive rescue by the obstruction. |

## Required fixes, priority order

1. **Scope:** repair K6 in §§0/7 and the “must either” dichotomy in §6. Require every restricted Eᵢ to be nonzero, or explicitly include identically vanishing expressions as another escape. Example: S−1 on p=t²+1 is identically zero; “a letter divides S−1” imposes no restriction there. §4.1 acknowledges this, but the summaries cannot omit it.
2. **Certification:** fix/rename `is_odd_square_mod`, include n=1 or state n≥3, and replace the “non-square” counts/coverage claims using the corrected table. Alternatively retain the old numbers explicitly as UNIT-square-only checks. The mathematical Lemma 4 needs no repair.
3. **SG prior art and F2 scope:** cite ET explicitly and record 8∣x ⇒ U⁽⁸⁾. With D±=s²±2εs+2, SG is exactly ET Type II (2.13)–(2.15) with a=1, b=4D+, c=(4D++1)/63, d=D−, e=63. Thus the parametrization and factorization templates are classical; do not infer novelty from thinness alone. Priority for this precise progression is unestablished, rather than disproved merely by the ET mapping.
4. **Peripheral exclusions/wording:** limit §5.1 to single-coordinate Vieta exchange; retain other failed attacks as failed ansätze, not impossibility results. In §5.6 restrict the splitting statement to prime factors coprime to the modulus and handle ramification separately (p=17,L=1 gives p+L=18; 2 does not split in any of the four listed fields). In Remark 3.5(a), either supply the attributed elliptic-curve argument excluding polynomial Pell data on P₁ or say “not supplied here”; a prior review's assertion is not a proof available to the reader. This is not needed for NL-J itself.

The “non-congruence” distinction for SG can be made rigorous without a novelty claim: on s≡±18 modulo 126, n=16s⁴+1 is a unit square locally at 2,3,7 (values 1,1,2); at any other prime choose s≡0. CRT/Hensel therefore supplies family members square modulo any prescribed modulus. No finite collection of fixed polynomial-solvable primitive n-classes can cover the whole integer family. This does not put it outside ET's general Type-II parametrization.

## Source checks and reproduction

H's actual admissibility condition checked in Bodin–Dèbes–Najib, [Introduction](https://arxiv.org/html/1902.08155v1); its §1.2 also states the Capelli criterion used in Corollary 6.2. This paper does not prove H over ℤ.
ET checked in primary PDF `sources/elsholtz-tao-1107.1010.pdf`, [arXiv:1107.1010](https://arxiv.org/abs/1107.1010), Proposition 1.9 and equations (2.13)–(2.22): fixed polynomial n-congruence families versus the general Type-II parametrization must not be conflated.
Commands: `uv run python scripts/z69_xrev_nl7_check.py collapse`; `uv run --with sympy python scripts/z69_xrev_nl7_check.py algebra`; `uv run --with sympy python scripts/z69_xrev_nl7_check.py screens SOURCE_ROOT` (SOURCE_ROOT contains the archived screen files).
Also reran lane scripts `selftest`, `verify_fail` (three R-G examples), `quartic` (J/c, j=1..249), `nlj`, `sg_examples`, `certify` from an isolated archive.
All commands used `ulimit -v 6000000`, timeouts ≤1800 seconds, and at most two compute processes. **No provider/auth/quota error occurred.**

**Final: ACCEPT-WITH-FIXES; retain the conditional “narrowed” verdict, not a HOT LEAD.**
