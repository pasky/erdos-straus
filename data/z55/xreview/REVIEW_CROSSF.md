# CROSSF cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** Bank the elementary identities and finite counts, not an asymptotic positivity result.
Reviewed `side-agent/z55-crossf` at `084790c6c801b81f3f2c666782f222394d0a0e28`, `Z55_CROSSF.md`.
ES and Problem CROSS remain OPEN. The main 10^124 arithmetic is correct; its universality/necessity is not established.

## Per-claim findings

| Claim | Classification | Independent check / limitation |
|---|---|---|
| Lemma 1.1, four forms | CORRECT | Congruence, factorisation, positivity of C, automatic coprimality, and least-residue condition all hold. |
| Lemma 1.2, Jacobi obstruction | CORRECT | Reciprocity gives (p/d) = −1; squares cannot hit. No squarefree requirement on d is needed. |
| Lemma 1.3(i)–(iv) | CORRECT | Exact bijections with the stated window restrictions; fixed d has at most one pair. |
| §2.1 long-u extension of Thm U | CORRECT | Inspected `Z53_GENUSLVAL` §§2.4–2.7: no U1 ≤ Y hypothesis is used. Displayed margins admit sufficiently large finite r and small ε. |
| §2.2 residual map; §2.3 fixed-d C collapse | CORRECT | u = −p mod w when u < w; C < d and 4pC ≡ −1 mod d give the unique C residue. |
| §2.4(a) minorant no-go | CORRECT, scoped | Proper-subgroup Fourier support cannot give a positive-mean pointwise class minorant. This is not a general analytic-method impossibility. |
| §3 certified counts and summary statistics | CORRECT on checked scope | Full 10^8 C-scanner rerun agrees byte-for-byte; independent counts on 512 sampled primes agree; all five exhaustive prime lists and all table statistics rechecked. |
| Zero hits and M > 0 imply failure of H⁻ | CORRECT | For every ε > 0, X = −M < −(1−ε)M. Independently certified M > 0 at every recorded exhaustive-scan zero. |
| §4 E(x), main threshold, c = .003 comparison | CORRECT as MODEL | Independent Gaussian-tail quadrature gives log10 x = 124.108562621 and 141.906500604 respectively. |
| §4(i) stronger R lower-tail formula | WRONG as written | R = 2 hits: the displayed threshold requires I(a/2), not I(a), where I(t) = 1−t+t log t. |
| §4(iv) GRH numerical comparison | CORRECT-WITH-FIX | Same E(x) = 1 prescription gives 10^39.9436; 10^42 is only a leading-exponent approximation. |
| §§0, 4–5 model/method conclusions | CORRECT-WITH-FIX | Mostly explicitly Assessment; “any admissible window,” “on the data,” and blanket falsifier/proof-threshold wording exceed the evidence. |

## Proof re-derivation

1. Put d = (p+u)/(2w). Then d ≡ −1 (4u) iff p+u+2w = 8uwC, with C ≥ 1.
   Multiplying by 4C gives 4Cp+1 = (4uC−1)(8wC−1); rearranging gives p+2w = u(8wC−1).
   Here d = 4uC−1 > u, so p ≡ −u (d) determines u as the least residue. Conversely the d-form
   gives integral w (p+u is even and d odd) and d ≡ −1 (4u). A common divisor of u,w divides p;
   since u,w < p, coprimality is automatic. All equivalences keep membership in U and W.
2. gcd(u,d) = 1 and d ≡ 3 (4); thus (p/d) = (−u/d) = −(d/u) = −(−1/u) = −1.
   Reciprocity with p ≡ 1 (4) gives (d/p) = −1. At N = m², gcd(N,d) = gcd(u,d) = 1,
   so (N/d) = +1, a contradiction. The obstruction needs non-squareness, not primality alone.
3. Fixed-u and fixed-w counts follow by dividing p+u and p+2w. For fixed C,
   d = 4uC−1 ≡ 4C−1 (16C), and the second factor recovers w; the product identity reverses the map.
   Fixed d recovers u and then w. The ≤1 assertion for fixed w additionally uses U1 < w.
4. For a pointwise minorant f, f(x) ≤ 0 off the identity, so its average is ≤ 1/|G|;
   equality forces f = δ1. If its support lies in a proper dual subgroup, f is invariant under
   a nonidentity annihilator element, forcing f(1) ≤ 0 and hence nonpositive average.
   In fact positive average forces every Fourier coefficient nonzero: writing off-identity values
   as −b_x, each coefficient has real part ≥ (f(1)−Σb_x)/|G| > 0. This concerns that minorant only.
5. Optimising the limiting coefficient gives (γ−β)(α1−α0) = (3−5α1)(15α1−1)/64,
   whose maximum is 1/12 at α1 = 1/3. Strict Thm U hypotheses give a supremum, not attainment.
   The numerical boundary window is not itself a strict Thm U window; asymptotic positivity there
   follows instead by containing strict-margin subwindows with coefficients approaching the supremum.
   Thm U is an inherited result here, not a newly certified mean asymptotic or upper bound.

## Numerical audit

Independent code: `scripts/z55_xrev_crossf_check.c` and `scripts/z55_xrev_crossf_audit.py`.
The C checker loops over w, sets u = −p mod w, and tests 8uw | p+u+2w directly, without factorising
p+u or looping over C. It uses integer-root windows, squarefree sieving, and trial-division primality.
Samples are rows floor(j(N−1)/255), j = 0,…,255: 256 at 10^8 (96 zeros), 256 at 10^10 (60 zeros).
All 512 counts agree exactly. The additional p = 10000169 has hits = 0 and direct M = 1.174218631636.
A separate modular square-class test finds positive genus summands at ALL 192,469 recorded zeros
in the exhaustive scans (not merely the sample). This verifies the finite H⁻ failure percentages.
These witnesses certify positivity exactly; the displayed full M sum is floating-point arithmetic.

| Scale | Independently checked prime-list size | Recorded zeros | Zero fraction |
|---|---:|---:|---:|
| 10^8 | 54,198 | 21,233 | .391767224 |
| 10^9 | 240,944 | 83,874 | .348105784 |
| 10^10 | 217,331 | 51,773 | .238221883 |
| 10^11 | 197,020 | 30,069 | .152619023 |
| 10^12 | 58,878 | 5,520 | .093753185 |

Segmented sieving independently verifies complete coverage (the 10^12 range ends at its last saved prime).
Total 768,371 agrees. Sample files have N = 8290,2238,535,108 and zeros = 444,79,9,0.
All table means/variance ratios reproduce. Counts outside the full 10^8 rerun and the independent sample
are audited from saved data, not all independently recounted; largest 10^15 zeros were not rerun here.
For c = 1/(3π^4), completing the square gives E(10^8) = E(10^18) ≈ 5.5835778453·10^30,
E(10^100) = 5.8942874755·10^18, peak log10 p = 63.0190379021, E = 1 at log10 x = 124.108562621.
For c = .003: E(10^8) = 1.5170100291·10^35; for c = .1: log10 x = 2.8912940633 (x ≈ 779).

## Required fixes, priority order

1. Scope 10^124 to the stated standard-window Poisson MODEL with its assumed c. A lower-bound coefficient
   is not a proved mean or an upper bound on other windows' means. Delete “for any admissible window”
   (§4(i)); change §5 “on the data” to “under this extrapolated model.” No theorem forces a proof's p0.
   E(x) = 1 is an expected-tail-count crossover, not a certified last exception; marginal Poisson laws
   alone do not specify the distribution of the last zero. Keep the explicit Assessment labels throughout.
2. Fix §4(i): for R ≥ a c log²p, use λ I(a/2) and log p0 ≈ 1/[c I(a/2)]; alternatively change the
   target to R ≥ 2a c log²p and retain I(a). The review-log claim that this is already fixed is incorrect.
3. Give the GRH model's same-integral threshold 10^39.94, or explicitly label 10^42.30 as the leading
   approximation exp(1/c), not the E = 1 computation used for 10^124. Change “attained” to “limiting supremum.”
4. Replace “not … a falsifier of anything” / “no finite-size falsifier” with “does not refute eventual
   positivity with unspecified p0.” A zero with M > 0 DOES refute H⁻ at that p and any specified threshold
   below it. Exhaustive testing to the model threshold is infeasible; that does not make rigorous
   checking of an effective proof's constants impossible. The all-large-p H⁻ target is not disproved.
5. Keep §2's methodological conclusions and unproved Kloosterman/sieve sketches non-bankable.
   Identifying divisor events does not prove no transformed average exists. The elementary minorant
   no-go concerns pointwise Fourier minorants, not all possible routes to positivity.

Reproduction: extract the reviewed branch to `/tmp/xrev_CROSSF`; run the Python audit with `uv run
--no-project --with mpmath python scripts/z55_xrev_crossf_audit.py /tmp/xrev_CROSSF /tmp/xrev_CROSSF/sample.in`;
compile the C checker with `gcc -O2 -Wall -Wextra -Werror`, feed `sample.in`, then feed all scan rows
with hits = 0 using `--witness-only`. Every shell invocation used a memory limit ≤6,000,000 KiB, a CPU limit,
and explicit `timeout` (≤160 s per executed program). All assertions and the full 10^8 comparison pass.
