# Hostile cross-model review — ELL0

**Verdict: ACCEPT-WITH-FIXES. ES remains OPEN.** No provider/auth/quota error occurred.
Reviewed `side-agent/z67-ell0` at `623f6644414ce9082936afe1da7dfcbdd7494518`, not an assumed working-tree version.
I independently read ET's PDF (Prop 1.9, (2.1)–(2.21), Lemma 2.8, §3), the UCOVER dependencies, code, and screen definitions.
All compute used `ulimit -v 6000000`, timeouts ≤ 1800 seconds, and at most two active compute processes.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| S-all / Theorem S′ | CORRECT | Full 9566-prime gap rerun and all 22 small primes agree byte-for-byte with saved certificates. |
| Lemma S2′, S-tail rounding | CORRECT | Re-derived constants; independently enclosed the infinite tail in closed form. Raw dyadic endpoint conversion is outward. |
| Lemma D | CORRECT | ET (2.10) preserves a²d; the new modulus divides the old. Odd k₂ terminates at 1. |
| T-expl analytic counting | CORRECT-WITH-FIX | Counts/constants hold for all positive integral sextuples, but §4(I2)'s displayed reflection inequalities are reversed. |
| T-expl numerical certificate | CORRECT-WITH-FIX | Independent exact-cutoff/exact-maximizer audit proves total < 0.0408; production code lacks rigorous checks on its floating search window/cutoff. |
| Largest A-cd term | WRONG as printed | The asserted upper bound 0.0380 is below the actual bound 0.0380299085818…; the total 0.0408 is safe. |
| Prop R | CORRECT | Bijection holds for the reduced k₂=1 parameter events, not distinct cylinders. Automatic coprimality proof works. |
| §6 finite facts / EVIDENCE | CORRECT | Decisive survivor counts reproduced; finite survival is not promoted to infinite survival. |
| “Not closed”, strengthened+narrowed | CORRECT-WITH-FIX | Honest method-specific conclusion; summaries must retain the a′>1 qualification on a proposed R-tail route. |
| F1–F4 / no HOT LEAD | CORRECT-WITH-FIX | No positivity overclaim, but blanket F2/F4 “not applicable” omits their direct Prop-R interpretation. |

## Independent computations and proof checks

**S certificate.** Compiled the archived C enumerator and reran both complete ranges with one worker.
The gap has 9517 certificates at K=1 and 49 at K=2; worst is ℓ=379:
exact part 15/378, tail < 0.453525052244894, total < 0.493207591927434.
The small-range worst is ℓ=37, K=3, total < 0.487677517772304; ℓ=11 passes at K=7.
`z67_xrev_ell0_audit.py ... s` separately checks all 22 small primes, the ten worst gap primes, and 103, 1009, 99991.
Its 80-digit interval closed-form sum of (ak²+(2a+b)k+2b)r^k verifies the production tail is genuinely above the independent upper endpoint (difference < 10⁻³⁵).
For N≥10⁵ the normalized radicals decrease; their endpoint bounds are 1.4207, 1.01, 0.72, 1.43.
The resulting W1 constant is 7.010824<7.02 and W2 constant 9.870824<9.88, with log coefficients 1.37 and 2.44.
Thus S2′'s 2.44 log N+10.15 dominates both brackets. The infinite sum at ℓ=10⁵ is <0.365463067<0.3655 and decreases thereafter.
The geometric ratio bounds T(j+1)/T(j) for every j beyond the truncation; its polynomial factors decrease with j.
Within-level residues are deduplicated; across-level overlaps are deliberately counted repeatedly. This increases the upper bound: no disjointness or reversed union bound is assumed.
I also checked the enumerator's small/large-factor completeness splits and arithmetic range for these reruns; no overflow issue occurs.

**Dilation and ET transfer.** For k₂≥3, (a,d,f)→(ℓa,d/ℓ²,f) preserves f|4a²d+1 and positivity/integrality.
The modulus becomes 4ad/ℓ, its prime-to-ℓ part remains 4a′d′, and the residue remains −f. The cylinder inclusion is in the asserted direction.
Independent checks reproduce 64 and 242 reducible events at (ℓ,k)=(17,3),(17,4), and 104,142 at (19,3),(23,3), with no failures.
For reflection, positivity actually follows from f_new=(n²+4c²d)/f in ΣI and (4c²dn+1)/f in ΣII; both are positive integers by the defining equations.
The original proof's “4bcd−n > 4acd−n” is false when a>b. Example: n=7, sextuple (2,1,3,1,1,17), reflected f=5<17.
The corrected reflection yields P≤2B without any coprimality/primitive-point hypothesis.
For ΣI, ef≥5 gives bf≤5na/3, f≤5n/3, acd≤2n/3, and ef(cd)²(ac)≤(40/27)n³<(15/8)n³.
For ΣII, abd≤n/2 and ce≤2b give acde≤n. All eight case reconstructions and divisor arguments check against ET's equations.
The pair-count bound X(1+log X), the n≥8 simplification, and multipliers F:2, E:4, A:2 are valid.

**T-expl certificate.** Replayed `z67_ell0_tbound.py 2950 300`, then independently rebuilt all 66 τ and 51 τ₃ constants.
The audit uses an independent prime list, exact integer cutoffs p^num<r^den, and exact maximizer comparisons (a+r)^den≥(a+1)^den p^num.
It verifies the production cutoff covers every contributing prime and every exact maximizer lies in the production ±2 window; maximal exponents are 28 and 35.
It then substitutes independently enclosed constants into the level/tail sum: total <0.040797735431250; tail <3.078·10⁻⁶³⁶⁹; pair ratio <5.704·10⁻⁵².
The original log constants agree to <3.34·10⁻⁴³; ln C(.05)=4526.214251… and ln C₃(.09)=1850.514378… .
The finite-level minimum β is exactly 0.192, exceeding 2/2950; fixed-tail slopes also decrease the bound as L increases.
The affine log factor has logarithmic derivative ≤1/L, and (1−e⁻ᴸ)⁻¹ decreases. Thus the certificate extends to every L≥2950.
The mass-to-nonresidue conversion gives ≥91.84% survival, and at most 0.0408(ℓ−1) fully caught residue classes, as claimed.

**Prop R and evidence.** From fw=n+C and gcd(C,f)=1, n is coprime to f; Jacobi (n/f)=−1 forces (−f/ℓ)=−1.
Consequently ℓ∤d′C, so no solutions of R(ℓ^(2k−1)) are lost to the event side condition.
Independent literal ordered-triple enumeration matches the a′=1 events: R(17³)=24, R(19³)=16, R(23³)=10; R(409)=R(577)=R(5569)=0.
Replayed level 1 for all 302 odd primes below 2000: precisely 3,5,7,11,13 catch everything.
At ℓ=2237, 176 of 1118 nonresidues are caught and the surviving total-unit mass is 942/2236=0.4212880143… .
Replayed all 72 level-2 primes: minimum 30/506=0.05928853755… at 23; at level 3, ℓ=59 gives 31190/201898=0.1544839473… .
I did not rerun the entire large-prime ET level-1 range or all ten level-3 primes; inspected their recorded tables, and reran the decisive minima.
Compactness correctly turns survival at EVERY finite level into an uncovered profile; the finite computations alone do not establish that hypothesis.

## Falsifier audit

F1: correct. The character obstruction excludes square profiles; independent checks also give R(9)=R(25)=R(49)=R(121)=R(225)=0.
F2: no numerator-8 positivity claim, hence no contradiction. But under Prop R, campaign C is d′: the 12 R₈-zeros remove the even-d′, a′=1 level-1 subfamily, not all A-events (their full R≥12).
F3: the 285 non-square composite zeros are outside the theorem's prime-ℓ unit-profile domain. They invalidate no universal claim made here.
F4: the 14 R-zero primes have NO a′=1 level-1 A-events; the 38 𝔊*-zeros remove only that restricted representation subfamily. Neither implies all ET-events vanish, nor controls higher odd powers.
Thus the screens do not refute either mass theorem, but the memo should explain these consequences rather than imply no relation to F2/F4.

## Required fixes (priority order)

1. Make the Euler-product rigor self-contained: incorporate exact cutoff/maximizer checks like the audit, or prove certified error bounds for the floating searches. The claimed “proved window” is not supplied by concavity alone. This review independently closes that numerical gap for the actual fixed grid.
2. Correct §4(I2)'s reversed reflection inequalities using the positive quotient formulas, and replace “≤0.0380” by “<0.03803” (or “≤0.0381”). Neither repair changes ℓ₀ or 0.0408.
3. In the paragraph summary, §7 and proposed FRONTIER text, say R-bounds **together with bounds for the a′>1 analogues**, or another control of the remaining A-events, would suffice. R alone only bounds a subfamily; §5 already states the necessary qualification.
4. Expand the F2/F4 rows with the subfamily behavior above. Keep the no-positivity/no-HOT-LEAD disclaimer and all finite-depth EVIDENCE qualifications.

Replay audit: `uv run --with mpmath --with numpy --with sympy python scripts/z67_xrev_ell0_audit.py /tmp/xrev_ELL0 MODE` for MODE=s,t,r, under the stated memory/timeout limits; compile ROOT/zsw and ROOT/zlev from the archived UCOVER C sources first.
**Bottom line:** both central mass theorems survive hostile independent checking; the small-prime ET tail remains unproved. Accept after the localized rigor, algebra, rounding, and scope fixes above—not as an ES result.
