# z58 CONVF hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** The core algebra, square obstruction and fixed-dimensional exceptional-set argument survive. The all-large-prime target remains **INCONCLUSIVE**, not dead or proved. The numerical tables reproduce; novelty, calibration, barrier scope and the mandatory screens need repairs before recording the memo.

Snapshot: `side-agent/z58-convf` at `e04b53a8546df0ae52c4596b98869d3c979e0b7c`, `Z58_CONVF.md`. No author files changed. ES remains open.

## Per-claim audit

| Claim | Classification | Independent check / required correction |
|---|---|---|
| Lemma 1.1, E1–E6 | CORRECT | E2 recovers b=(cn+a)/f; multiplication by the units 4ad and c proves E3; E4 follows from fg=4c²dn+1 and recovers g≡−1 mod 4cd. E5 recovers c=(a+b)/σ and d=(n+σ)/(4ab); E6 recovers a,b=(cσ±t)/2. Specify f,σ positive. |
| “This is ET Type II”, for every odd n | CORRECT-WITH-FIX | The identity is valid, but ET Prop. 2.7 requires gcd(abd,n)=1. It is automatic at target primes, not arbitrary composites: n=69, (a,b,c,d)=(3,6,3,1) has gcd(abd,n)=3. Keep the algebraic family for all odd n and qualify the Type-II terminology. |
| Lemma 1.2 | CORRECT | Specialisations give the stated divisibilities. For the d=1 square test, n+σ>0 forces abs(t)<cσ and reduction modulo 4 forces the required parity. f²≤fg yields the bound. On the diagonal, a<p implies a divides c; c=ae gives e dividing 2, and e=1,2 contradict p≡1 mod 4. The prime-factor criterion works also for the even number n+1; the proof's “number ≡1 mod 4” wording is unnecessarily restrictive. |
| Lemma 1.3 | CORRECT (arithmetic); scope fix | f is odd, coprime to 2ad. Reciprocity gives (d'/f)=1; if d is even, f≡7 mod 8 gives (2/f)=1. Thus (n/f)=(−4a²d/f)=−1, including composite f and non-coprime candidate n (which are thereby excluded). Odd squares cannot occur. This does not prescribe how every possible proof must be organised. |
| Lemma 1.4 | CORRECT | For fixed finitely many triples, p≡1 mod 24∏f avoids each Jacobi-negative class; Dirichlet supplies infinitely many such primes. This concerns fixed triples/classes, not finitely many (a,d) with c unbounded. |
| Lemma 1.5 | CORRECT | The modulus-4 tests exclude every 3 mod 4 prime; modulus-8 subset products give the stated alternatives. For M=(p+3)/4≡1 mod 6, any 2 mod 3 prime factor permits a factorisation M=abd with a,b≡2 mod 3; hence σ=3 gives a hit. This removes the {1,5} mod 12 alternative. The remaining necessary conditions and the 273 example check. |
| Lemma 3.2 / Theorem 3.1 | CORRECT, standard sieve input | Fixed C gives distinct forbidden nonzero residues plus 0, dimension κ=1+Σ(c≤C)1/φ(4c), V(z)≍(log z)^−κ, and remainder O_C(N^1/2(log N)^C). With z=N^(1/(20κ+20)), the z term and remainder are negligible. κ→∞ gives every fixed logarithmic saving. The c=1 and even-d variants have the same proof. |
| §2 certified census and witnesses | CORRECT | All three saved outputs rerun identically; independent checks below confirm exact witnesses and several complete lists. These are finite statements, not eventual positivity. |
| §2 mean interpretation | CORRECT-WITH-FIX | Recorded means and the ≈1.7 distinct-count ratio reproduce. The proposed limiting 1/8 is an all-integer Haar calibration, not the prime-conditioned density. Correlation changes variance/zero tails, not the mean of a fixed sum of indicators. |
| §4(E) displayed “R(p)=” | WRONG as written; easy fix | It restricts to a≤b while R counts both orientations. At p=23929, R=78 but the displayed divisor/character sum is 39. Replace the left side by R(p)/2 on the target prime domain (or double the right side). |
| §4(F), “dies at Lemma 1.4” | GAP in barrier inference | A fixed (a,d) allows infinitely many f=4acd−1 as c varies. Lemma 1.4 does not prove that finitely many such divisor tests fail infinitely often at primes. Squares satisfy the conditions but are not primes. |
| §3 Remark 3.3 and §4(A)–(D),(G),(H) | Assessment only, with fixes | No pointwise construction was obtained. “At best”, “measure-zero”, “every forced factor ... same size”, and “only thin families” are not established impossibility bounds. G/H are legitimate re-encodings; the σ bound follows from σ≤a+b≤M+1. |

## Proof, source and priority details

The fixed-C sieve is not conditional on an unproved conjecture. I checked the archived primary exposition by Tao, [254A Notes 4](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), Lemma 17 / Corollary 19 and (22), in `sources/lit2026/audit-tao-254a-notes4-sieve-theory.md`. Its bounded combinatorial weights give the unweighted remainder used here; divisor-weighted Selberg versions also suffice with a larger fixed logarithmic exponent. The precise Halberstam–Richert/Friedlander–Iwaniec chapter citations were not independently page-verified; replace or supplement them with this pinpoint reference. Fixed-modulus AP Mertens estimates suffice; no uniformity in growing C is used.

**The exceptional-set theorem is prior in substance, with a direct stronger transfer.** `Z56_FAMTRY.md` Theorem A already proves X exp(−0.08√log X) for the c=1 line and its integer avoider set. For a=1, at q≡3 mod 4 take Ω_A(q)={−c⁻¹ mod q : c divides (q+1)/4}. These are distinct, and have exactly the same cardinality τ((q+1)/4) as FAMTRY's Ω_B(q)={−u mod q : u divides (q+1)/4}. A hit yields d=(q+1)/(4c), b=(cn+1)/q, both positive. FAMTRY §§3.2–3.5 depend only on these cardinalities and the common AP divisor count, so their stronger bound transfers verbatim, including interval uniformity. This is a transfer of a prior proof, not an assertion that FAMTRY literally stated the a=1 theorem, nor a logical implication between the two zero sets. Remark 3.3's “at best” cannot be advertised as a limit of prime-witness sieving generally.

**The recommended line is López's Type A, not a newly discovered stronger family.** `B1_LINE.md` §§0,2,3 already identify it, record exactly {193,2521,66529} through 10¹¹, and compare its distinct counts with (★). `BM_CORRECTED_COUNT.md` §4 treats both lines, their shared character and correlated residuals. I checked López's actual Theorem 7, Conjecture 1 and ET-coordinate identification in `sources/lit2026f/r270-lopez-2404.01508v3-html.md` ([source](https://arxiv.org/html/2404.01508v3)); they give the divisor form, union conjecture and three familiar failures, not a theorem that only three failures exist. ET Prop. 2.7 was checked in `sources/lit2026/audit-elsholtz-tao-1107.1010.txt`.

**Calibration repair.** `B1_LINE` Lemma 3.1 and its R270/frontier-review corrections already distinguish 1/f from 1/φ(f) and report N₁/log²p≈0.135 at p≈10¹², beyond the alleged limiting 0.125. For p≡1 mod 24, also impose compatibility with that progression. `BM_CORRECTED_COUNT` Theorem 2.2 gives the ordered (★) main-term constant 3/(2π²), not 1/8. Retain the measured 0.1234 and 0.1440 as finite-range ratios; do not infer an asymptotic from their proximity to 1/8 or explain differences in means by correlations.

**Autopsy scope.** Lemma 1.3 proves a necessity, not that residue-based proofs are impossible: E3 itself is an exact residue-based target. Lemma 1.4 excludes fixed finite solvable classes. It does not exclude infinite or p-dependent classes, fixed-shift divisor arguments, adaptive descent, or prime-specific arguments. In §4(B), dp must be nonsquare as stated; primality alone does not ensure this for every d. The norm and CRT observations are failures of the attempted constructions, not general no-go theorems. Preserve the final “I know no tool” assessment and remove the stronger universal wording.

## Numerical audit

Every shell command used `ulimit -v 4000000` and timeout ≤1800 s. The three lane programs were compiled with `gcc -O2`; their inspected allocations are linear in N (at most about 300 MB in these runs), not Cartesian products.

- `z58_convf_sieve.c 100000000`: **byte-identical** to `sieve_1e8.txt`; 201.59 s, 294464 KB RSS. Among scanned n≡1 mod 4, only nonsquare full-family zero 4545; prime subline zeros c=1:14, a=1:3, d=1:203, c≤2:2, c≤3:0, union:0. The printed counters are correctly disclaimed as not R(n). The code does not actually enforce a≤b, but includes every small-a orientation and only valid positive witnesses, so existence and tags remain sound.
- `z58_convf_means.c 60000000`: **byte-identical** to `means_6e7.txt`; 22.02 s, 294776 KB RSS. Final bin [16384000,60000000]: 313394 primes; means 37.32 / 43.57; ratios 0.1234 / 0.1440; minima 5 / 2. Use this exact bin rather than asserting the minimum on the slightly larger [1.6·10⁷,6·10⁷].
- `z58_convf_wit.c` on all 18 saved inputs: **byte-identical**. New `scripts/z58_xrev_convf_check.py` independently verifies all **466 quadruples**, their rational identities, E2–E6 maps and Jacobi signs. A separate σ/divisor enumerator exactly reproduces complete ordered lists at 193,409,577,2521,4545,5569 and finds no witnesses at the 16 odd squares m² with 1≤m≤31.
- Explicit complementary certificates: 409 has (1,117,2,1); 83449 has a=1 witness (1,394,5,53) and c≤3 witness (3,211,2,33); 102001 has (1,26609,6,1) and (5,232,3,22); 8813281 has (1,1111585,14,2) and (7,22502,3,14). Thus a=1 and c≤3 really are separate successes, not a claim that their intersection works.
- The reviewer script runs as `uv run python scripts/z58_xrev_convf_check.py /tmp/xrev_CONVF` after extracting the reviewed branch. It also supplies the missing positive screen certificates described next. Existing `z57_synth_dec8.c` was rerun at each of the 12 stored large R₈-zero primes, reproducing **every** R and R₈ column. The full interval census was not rerun.

## Mandatory falsifiers

| Screen | Audit |
|---|---|
| F1 odd squares | PASS for the arithmetic obstruction and density theorem. Independent finite controls agree. Fix the “no argument using n mod f” / “every proof must” extrapolation. |
| F2 C-even/(★), 12 large zeros | **MISSING/MISIDENTIFIED in the memo.** Its full-family d-even discussion is not the required c=1, d-even screen. In CONVF coordinates the screen's C is d **on c=1**. All 12 R₈ zeros and positive R counts reproduce. Moreover the reviewer finds a=1, even-d witnesses at all 12: e.g. p=10156800001 has (1,317435302,281,8). These zeros do not refute the full even-d family. Add this explicit distinction and remove the assertion that every credible full-family argument must break when d is even. The unrelated “22 zeros ≤10⁹” has no supporting file here; existing z32 logs say 21 for p>3 through 10⁸, so specify domain/source or omit it. |
| F3 285 nonsquare composite zeros | PASS with scope. Independent file tally gives exactly 71 at 1 mod 24 and 214 at 9 mod 24; the actual endpoint is 7,999,801. These are c=1 zeros, not full-family zeros. The rerun full-family sieve covers every one except 4545; independent σ enumeration confirms R(4545)=0. |
| F4 14 (★) and 38 G* zeros | **PARTIAL in memo.** The 14 are correctly handled; all saved a=1/c≤3 witnesses verify. The 38 G* zeros are not discussed at all. The reviewer constructs exact a=1 witnesses at all 38, including p=564661441: (1,28956997,2,5). This completes a finite consistency screen only, not an eventual theorem. |

## Required fixes, in priority order

1. Remove the unsupported barrier in §4(F), scope all “must/dies/at best” claims to the actual fixed-class or attempted constructions, and correct §4(E)'s factor of two.
2. Add the actual F2 screen and the omitted 38-prime F4 screen. Distinguish c=1/d-even failures from full numerator-8-family failures; do not require a density argument to discriminate individual exceptions.
3. Attribute the a=1 line, existing stronger census, calibration and union question to López/B1_LINE/BM_CORRECTED_COUNT; identify Theorem 3.1 as a standard weaker sieve corollary and give the stronger FAMTRY transfer above.
4. Replace the prime-limit 1/8 claim and correlation explanation; retain the measured ratios, exact sample interval and explicit finite-evidence labels. Qualify ET Type II at composite n and sharpen the sieve citation.

After these fixes, accept as a sound independent rederivation, finite subfamily audit and unsuccessful attack report—not a new pointwise advance or a theorem killing the surviving approaches.
