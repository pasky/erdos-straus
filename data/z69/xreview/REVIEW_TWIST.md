# Z69 TWIST hostile cross-model review — ACCEPT-WITH-FIXES
Reviewed `side-agent/z69-twist` at `6e2e8eee3`, including both late additions. **ES is OPEN.**
No provider/auth/quota error occurred. I independently re-derived the elementary proofs; no external theorem is decisive for the accepted kills.
The sterility theorems and restricted I23 counterexamples survive. The principal risk is false-negative interpretation of I9/I17/I24/I12, not faulty descent.

## A. Per-claim audit
| Claim | Classification | Independent derivation / check |
|---|---|---|
| Lemma V and Corollary V | CORRECT | Minimal odd M gives integral odd M′=2bcd−M≠0; a′=M′²/(bd)>0 and a′+b=c(2M′+1) force M′>0. Then MM′=bd(b−c)<M². No coprimality/primality assumption is hidden. Checked 32,810 unrestricted pairs for odd M≤1001. |
| Original #11 M⁴-divisor question | CORRECT, genuinely closed | If v divides M⁴ and v≡−M² modulo 2M+1, put g=gcd(v,M²), a=v/g, b=M²/g. Prime valuations give ab divides M²; g is invertible modulo 2M+1, so a+b≡0, contradicting V. Direct divisor enumeration also passes for every odd M≤1001. |
| T10 / Pell corollary | CORRECT | Each prime factor q of f has (−d/q)=1. Thus (d/f)=−1, while reciprocity gives (d/f)=(d/p) since f≡−p modulo 4d. If p divides 4a²d+1 then (d/p)=+1, contradiction. Independently regenerated all 6,718 points, no violations. Jacobi extension needs n≡1 (4), as finally stated. |
| Vieta involution ι | CORRECT | Direct expansion gives ee′=4b²d+1, n′e′+1=4a′bd, preserved gap, and inverse equal to itself. It acts on the extended signed locus, NOT everywhere on positive solutions. |
| Strict descent D | CORRECT | With a>b, 2b≤ce−1 and n+e≤2e−2 imply c+b(n+e)≤ce²−(c+1)(e−1)<ce²; this is exactly n′<n. |
| Root classification R | CORRECT | Minimal positive n descends to n′≤−3, e′≥3, a′<0, yielding the stated root. Reversing produces n=4bcd−ε>0 and a>0. Since αbd=(νε−1)/4 and ν+ε=2j, each gap has finitely many roots. |
| Gap/conic corollaries | CORRECT | j=1,3,5 have no roots; the displayed root for j=4m+3 works for m≥1. Eliminating n,e gives the stated conic and Vieta exchanges. Independently recovered the exact 38 sterile gaps through 301 and walked complete descents of 97 solutions with n≤1001,j≤101. |
| Square-slice corollary | CORRECT | For prime p, L²=pe+1 implies L=kp±1. For k≡1 (4), (kp+1)/2 is odd and kp+2 divides e, so V applies. This parametrisation is NOT valid for arbitrary composite n; the memo correctly supplies n=21 as a counterexample. |
| Lemma P | CORRECT | Finiteness follows from (x−1)(z−1)≤n+1, with the x=1 edge also bounded. Swap-fixed words satisfy x(xy−2)=n; for primes ≥5 only x=1 survives. Independently checked n≤2000, including the 11 words at both 9 and 105. |
| P′ / Remark C / odd-word kill | CORRECT | Mod-8 product (xy−1)(zy−1)=ny+1 separates A/B; substitutions produce the stated Type-I/II certificates. Orientation and c odd are necessary and now included. Independent words through 2000 pass; full original census rerun through 2·10⁷ reproduces 635,170 primes, 154 B-empty primes, and sole B∪(★) zero 409. |
| I23 coefficient/lift dictionary | CORRECT in stated scope | Rationalising 1/α gives BOTH coefficient equations. gcd(ph²−g²,h)=1 makes integrality equivalent to m dividing n. Negative m is essential and included. Scope is termwise positive unit-fraction traces in Z[√p], not every ring/trace descent. |
| Truncation T / certified I23 kill | CORRECT | For H≥1, a large lift is nonzero and its error from ±√p is <n/(H²√p). The triangle inequality gives exactly the two thresholds. Independent factor-pair enumeration found all 647 ES triples at 37 primes; signed-divisor enumeration of small lifts and exact sign-aware quadratic comparisons prove no lifts at 36 primes; only 5 survives. Original checker also rerun in full. |
| I17 dictionary and census completeness | CORRECT | Swap [4ac−1,4a,e], then shear by c: [e,2(b−a),c²e−1], discriminant −4p. Also e≤a+b≤ab+1=(p+e)/4+1, hence e≤(p+4)/3: good-class enumeration is exhaustive at d=1, not height-truncated. |
| I24 / I12 algebraic reductions | CORRECT; NOT general kills | I24 is the t=ab identity with 2≤a+b≤t+1<4t. I12 follows from 4k(p+u)=4kp+1+D and gcd(4k,D)=1. Finite independent checks pass. Neither identity excludes adaptive t or uncontrolled-cofactor forcing. |
| I6 PROVED parts | CORRECT | The count has leading term x log²x/8: discard bounded a/b at O_K(x log x), squeeze the remainder against 4abd using a,b≥K, then K→∞. Partial summation gives the Abelian asymptotic. Character orthogonality gives E/O exactly. These prove no completion obstruction. The explicitly unchecked automorphic identifications remain unverified quotations, not accepted theorems. |
| Late Type-II polynomial parametrisation | CORRECT-WITH-FIX (scope) | Substitution a=ce−b gives n=e(4bcd−1)−4b²d. For the surrounding n≡1 (4) domain add e≡3 (4); unrestricted positive parameters also produce other residues. Finite checks pass. It excludes only this fixed-(b,c,d) two-root construction, not hidden nonlinear transport in other coordinates. |
| Late (W) census and tail | CORRECT finite computation | A separate unordered-outer-letter engine reproduces the FULL 10⁹ census and every tail entry, using <501 MB. Exactly 15,810 square zeros and sole non-square zero 105; ≤2/≤6 counts are 4/52, last 111969/4808265. Independent divisor enumeration also verifies all 20 block minimisers. (W) remains CONJECTURE. |

## B. Registered kills, power, and false negatives
Checkpoint `2f761573e` contains K-I9/K-I17/K-I23 before their result commit. Final disclosures of changes are substantially honest; pre-registration does not validate an unsound rejection criterion.
| Item | Decisive versus bounded | Adjudication / concrete surviving test |
|---|---|---|
| IDEAA #11 | DECISIVE | Lemma V kills the exact slice, without a range caveat. No more slice searching needed. |
| I10 | DECISIVE for the specified substitution | Every d is excluded when p divides 4a²d+1. This is not a theorem against all Pell-assisted constructions. |
| IDEAA #10 | NECESSARY CONDITION ONLY | Nonsquare d is not killed; (1033,1,132) survives with f=e=23. A next experiment can restrict to (d/p)=−1 and test an explicit nonlinear d-selection rule, rather than re-test square d. |
| I9 / K-I9 | BOUNDED, underpowered null | Full class-matched rerun reproduces z=−0.55,−0.73,−0.65,+0.47. Neither run is the registered random, size-matched design; controls overlap and sometimes are hard primes. Within 3σ is non-rejection, not equivalence. With 145 cases the nominal 3σ difference is ≈0.12 (roughly 0.16 for 80% detection); 9–20 cases have very little power. Further test: disjoint controls in the same class and within a factor two, preregister an effect bound and a q-to-word construction; classify unmatched small primes separately. |
| I17 / K-I17 | DECISIVE against two exact invariances; BOUNDED otherwise | Full reruns reproduce G=1232, genus total=6034, J/ℓ overlaps 72/378, null 0/339, intersection 730, chance 260. J fails the registered beyond-chance criterion; ℓ DOES NOT: 378>260. The post-hoc null resemblance has no variance/test and is not a registered kill. Priority follow-up: compute the entire stabiliser/translation-overlap profile, with inversion-symmetric norm-matched nulls; then test d=3,5 with the correct 4d-divisibility condition. |
| I23 / K-I23 | DECISIVE in the specified lift model | The original bounded search did not fire K-I23; the later rigorous truncation repairs this. A single p=13 suffices; all 36 failures are certified. Testing below 400 rather than 2000 is adequate for this existential falsifier. Maximal-order or non-termwise trace variants are outside this result. |
| I24 | ONE-TRANSPORT FAILURE / RE-ENCODING | Fixed t cannot transport a solution to d+1. Nothing rules out changing t. Further concrete test: for actual solutions test t′=t−1,t,t+1 with s′=4(d+1)t′−p, requiring s′²−4t′ a nonnegative square and positive integral factors; report coverage, not a general no-go. |
| I5 | DECISIVE on O_p; OPEN on T_p | p=73 alone kills the all-odd certificate-fixed involution. The exhibited cross-n map does not address a fixed-p map on T_p. Any proposed new map should first be checked on complete T₇₃ and T₄₀₉ with certificate fixed points; more raw parity counts do not test this. |
| I6 | UNTESTED, not killed | No completion law was proposed/tested. A concrete next step is an S-transformation with boundary/shadow terms for the d=1 fibre, then d=3; only afterwards ask whether summing levels has a law. Low priority is an assessment, not mathematical evidence. |
| I12 | PRESCRIBED-PART REDUCTION ONLY | The requested target-only/cofactor experiment remains undone. For CRT-chosen u, retain residual (p+u)/D and enumerate divisor products targeting −1 modulo 4u separately from full-group coverage. Showing the forced D is a covering class does not refute that experiment. |
The reported ~1.5-hour lane, with no I6 test and no adaptive I24/cofactor I12 experiment, cannot support exhaustion of a 4–5-hour survivor-push box. The useful by-products do not change that scope.

## C. Falsifier audit
| Screen | Result |
|---|---|
| F1 odd squares | Sterility/Jacobi and parity entries are compatible; independent full census finds no C-certificate at any odd square ≤10⁹. But “I9: Y=0” is FALSE: 29²=1²+840·1² is primitive. Correct discriminator: in a primitive square representation every q dividing X is coprime to 840Y and has (840/q)=+1, so Q=0. Restrict the I17 genus-character comment to tested d=1; arbitrary −4dn needs separate hypotheses. |
| F2 all 12 R₈ zeros | y divisible by 8 is exactly the C-even star line, unlike the full certificate union. Independently found an odd-C star witness at each archived zero; no R₈-positivity claim follows. I did not independently re-certify their R₈ absence. The original small-range census's 286 zeros is a different sample, not this screen itself. |
| F3 all 285 composite zeros | Independent word enumeration confirms no star word and C nonempty at 284/285, failing only at 105. Thus (W) legitimately bypasses most R-zeros; its explicit 105 exclusion is indispensable. The square-slice primality caveat is correct. |
| F4 all 14 star / 38 G* zero primes | Independent enumeration finds C nonempty at every listed prime and no star word at all 14 star zeros. The 409 witness (1,117,2,1,59) checks exactly. No claim of positivity for the narrower vanishing line is made. These are compatibility checks, not a HOT LEAD. |

## D. Required fixes, in priority order
1. Replace the ambiguous “dead on the triaged twists” umbrella with “three specified proposals refuted; other directions narrowed, bounded-null, or untested.” In particular I24/I12 reductions are NOT decisive kills of their adaptive versions.
2. State explicitly that K-I17 did not fire for ℓ under the registered criterion; 378 versus 339 has no calibrated null significance. Preserve I9's non-rejection/power warning everywhere, including any downstream summary.
3. Correct F1's Y=0 assertion and scope its I17 genus-character claim to d=1. Include actual F2–F4 compatibility of the new (W) target, rather than treating all late objects as n/a.
4. Add e≡3 (4) to the late Type-II parametrisation when claiming the n≡1 (4) locus; retain the fixed-parameter limitation on its no-two-root remark. Do not convert “free parameters over all n” into an obstruction at prescribed p.
5. Replace “the minimum grows steadily” by “prime-block minima are nondecreasing in this range; all-n minima fluctuate” (8→6 and 19→18). Neither pattern controls a later exception. Record the two late additions accurately in the review log, which currently says only the tail was added after round three.
6. Record the shortfall/unrun follow-ups; do not claim the survivor directions were exhausted. Keep I6's memory-based automorphic statements outside the PROVED label unless sourced and normalised.

## Reproduction and verdict
New independent scripts: `scripts/z69_xrev_twist_check.py` and `scripts/z69_xrev_twist_census.c` (no campaign enumerator imported).
Run Python with `uv run --with sympy python scripts/z69_xrev_twist_check.py /tmp/xrev_TWIST`, after archiving the target screens there.
Build C with `cc -Wall -Wextra -Werror -O2 scripts/z69_xrev_twist_census.c -lm -o /tmp/xrev_TWIST/independent_census`; run with `1000000000`.
Both finish successfully. Original matched-I9, both I17 scripts, full I23 certificate, and 2·10⁷ odd-word census also rerun successfully.
All computations used `ulimit -v 6000000`, command timeouts ≤1800 seconds, and at most two concurrent compute processes.
**ACCEPT-WITH-FIXES.** Accept V, T10, the fixed-gap theorems, P/P′, the restricted I23 kill, and the finite (W) data. Do not accept a blanket death verdict for the remaining twists. No result settles ES.
