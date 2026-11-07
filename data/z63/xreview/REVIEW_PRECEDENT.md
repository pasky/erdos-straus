# z63 cross-model hostile review — PRECEDENT

**Verdict: ACCEPT-WITH-FIXES.** The literal precedents and the narrow literature-gap assessment survive; the blanket transfer-barrier wording does not. ES remains OPEN.
Reviewed `side-agent/z63-precedent` at `2c2199747737ac49fba63856f3720cb02cb95d11`, independently of its internal review.
Scope: the requested decisive citations, Lemma 1, numerical non-residue claim, gap statement, and F1–F4. Other catalogue entries are not independently certified here.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| A1, Iwaniec via Costello–Watts | CORRECT-WITH-FIX | Fresh PDF, introduction: exactly `g(m) ≤ X(k log k)²`, `k=ω(m)`, for every interval of that length. V2 attribution is honest. The inferred count `≍ k² log k` is not valid for arbitrary m; see fix 4. Literal polylog precedent survives. |
| A2, AKS Lemma 4.3 | CORRECT | Author v6 states `r ≤ max{3,⌈log⁵ n⌉}`, `o_r(n)>log² n`, for integer n>1, logs base 2. Proof uses the least nondivisor of `n^⌊log B⌋ ∏_{i≤⌊log² n⌋}(n^i−1)` and LCM bound; n=2 is handled separately. It does not require primality or non-perfect-power input. |
| A3, least prime nondivisor | CORRECT | If every prime ≤x divides n, then `log n ≥ θ(x)∼x`; take x=(1+ε)log n. A genuine unconditional size squeeze, valid also at squares. |
| A4, Shoup 1992 | CORRECT | Original author PDF, Thm 1 (visually read): for irreducible f of degree n over F_p, r=ω(pⁿ−1), `p^ℓ > c r⁴(log r+1)⁴ n²` guarantees a monic irreducible θ of degree ℓ primitive modulo f. Thus enumeration is `(np)^{O(1)}`, polylog in pⁿ when p=n^{O(1)}. No ERH assumption for this theorem. |
| Shparlinski 1990 | CORRECT at V2 level | Shoup p.3 explicitly attributes an `(np)^{O(1)}` deterministic search to Shparlinski Thm 2.4, and says it need NOT produce small-degree polynomials. Bhowmick–Lê independently restate the attribution. Original MathNet metadata checked; full-text access returned 403, so no primary theorem verification is claimed here. |
| Bhowmick–Lê 1412.7373 | CORRECT, with essential conditions | Fresh PDF §1.2 contains the quoted `d∼C log_q n` existence sentence and credits Shoup. Thms 3/5/6/8 support the stated mechanisms, but Thms 5–6 are not unconditional-in-parameters density assertions; details below. |
| LLS Cor 1.2 / Thm 1.4 | CORRECT | Fresh PDF: GRH, q>3 and reduced a for Cor 1.2; q≥20000, h>1 for Thm 1.4, with the alternative p≤10⁹. Formula is exactly `((h−1)log q+3(h+1)+(5/2)(log log q)²)²`. The memo now quotes it correctly. |
| LLS density calibration | CORRECT as heuristic | `Li(X_h)/h ≍ h(log q)²/log(h log q)` asymptotically. This bound supplies a polylog-count window for polylog h, not for power-size h. It is NOT a limitation theorem about GRH. |
| KLM 2607.14515 Remark 2 | CORRECT | Fresh v1 PDF p.8 says exactly “does not bring us closer” to `p(k)≪k(log k)²`. Thm 5 assumes BOTH GRH and Hypothesis 2; its A is in (1/2,1). Its p(k,a) is the least prime **greater than a** in that class. Remark 2 concerns this technique/uniformity range, not every stronger hypothesis. |
| JPSZ 2405.08650 Thm 1.1 | CORRECT | Fresh v1 PDF: `1≤σ_A(n)≤C n^{c/log log n}`; explicit means membership in `(log n)^{O(1)}` time. Kolountzakis's N^{O(1)} enumeration is distinguished. This supports the stated calibration, not a proof that no later improvement exists. Use “best found in this survey.” |
| Lemma 1(i),(ii), PROVED | CORRECT | Independent Jacobi-symbol proof below; arbitrary κ and X cause no issue. The unbounded square inputs refute a constant-G eventual squeeze on the stated domain. |
| Input-blind squeeze exclusion | CORRECT, scoped | Applies when the combined hypotheses remain true at arbitrarily large odd squares. Does not exclude primality-sensitive squeezes or force every such squeeze to be an identity. |
| Jacobsthal sieve transfer screen | CORRECT-WITH-FIX | No direct fixed-class Jacobsthal encoding is supplied for the moving divisor condition. The universal-sounding “local-density sieves fail T1” conclusion exceeds the argument; see fix 1. |
| Function-field screen | CORRECT-WITH-FIX | `Z58_FFIELD` Cor 3.2 excludes a q-independent degree threshold, relative to its cited Chebotarev result. It does not exclude A4's fixed-q/growing-degree regime. That regime remains open, not screened out. |
| GRH non-residue implication | CORRECT-WITH-FIX | Under GRH the eventual implication to a (★) witness is equivalent to eventual **(★) positivity** on the same prime class. “Equivalent to ES” without this qualification is unsupported; full ES need not use (★). |
| Fourteen n_p values | CORRECT / recomputed | Exact list and maximum 23 agree; all 14 input primalities checked. Also independently rechecked R(p)=0 for all 14, not merely p≤10⁴. Census completeness through 10¹⁰ remains inherited. |
| §3.5 gap and narrowed verdict | CORRECT as Assessment | No reviewed row supplies the prescribed analytic moving-modulus sparse-hit theorem. This is absence of a demonstrated template, not a classification of possible proofs or a new impossibility theorem. |

## Source and parameter checks

Fresh PDFs accessed 2026-11-07, not merely the memo's saved excerpts:
- Costello–Watts: https://arxiv.org/pdf/1306.1064 — introduction (Iwaniec statement).
- AKS: https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf — Lemmas 3.1, 4.3 and proof.
- Shoup: https://shoup.net/papers/primroots.pdf — Thm 1, pp.2–3; rendered because its text encoding is corrupt.
- Shparlinski metadata: https://www.mathnet.ru/eng/sm1217 — Russian 1990 / English translation 1992; theorem checked only through Shoup.
- Bhowmick–Lê: https://arxiv.org/pdf/1412.7373 — §1.2 and Thms 3, 5, 6, 8.
- LLS: https://arxiv.org/pdf/1309.3595 — §1.2, Cor 1.2 / Thm 1.4; also Cor 1.1.
- KLM: https://arxiv.org/pdf/2607.14515v1 — Thm 5 / Remark 2.
- JPSZ: https://arxiv.org/pdf/2405.08650 — Thm 1.1 and definition of explicit.

Bhowmick–Lê: Thm 3/Cor 4 require `2 log_q n ≤ r ≤ d ≤ n`; error ε is their smooth-polynomial term plus `O(nq^(−r/2))`.
Thm 5 takes `d=(2log_q n+2log_q(1/ε)) C log(1/ε)/log log(1/ε)` and gives density error `2^{ω(N−1)} O_q(ε)`.
Thm 6 requires `ε < c/[ω(N−1)²(log ω(N−1)+1)²]` and gives density at least `c/(log ω(N−1)+1)²`.
Thus a fixed ratio d/r does not by itself supply the shrinking ε required uniformly as ω grows. Use Shoup Thm 1 for the uniform small-set existence claim, not an unconditional application of Thm 6 with arbitrary parameters. The memo's caveat avoids that error.

## Independent proof and arithmetic

For a (★) witness at n=m² put d=4uC−1; then d divides m²+u, d≡−1 (mod 4u), gcd(d,u)=1, hence gcd(d,m)=1.
Quadratic reciprocity gives `(u/d)=1`: write u=2^a v with v odd; reciprocity cancels the two signs from d≡−1 mod 4v, and if a>0 then d≡7 mod 8 gives `(2/d)=1`.
Consequently `1=(m²/d)=(−u/d)=−1`, contradiction. This proves Lemma 1(i) without relying on a quoted T1; (ii) follows since infinitely many distinct squares are unbounded.

All computational commands used `ulimit -v 6000000` and individual timeouts ≤240s; no large Cartesian arrays.
The supplied script was rerun with `uv run --with sympy`; its output is byte-identical to `qnr_zeros.txt`.
Independent Jacobi-symbol checks reproduce `7,5,13,13,7,13,23,5,23,7,13,19,11,17`.
Independent R check uses the u-form rather than factoring 4Cn+1: order u≤B, enumerate `u≤⌊(1+√(1+4n))/4⌋`, and divisors d of n+u with d≡−1 mod 4u and (n+u)/d≥u; double the count (odd n forbids u=B).
All 14 have R=0; controls 25,49,121,169 give 0; 13,73,433 give 2,2,10. Also R(4545)=0.
This checks listed inputs, not absence of additional zeros. Review scratch calculations live outside the repository in `/tmp/xrev_PRECEDENT/`.

## Mandatory falsifier audit

| Screen | Actual outcome and repair |
|---|---|
| F1 odd squares | Lemma 1 passes. “Squares have no non-residue” means no Jacobi value −1 for the square-modulus character (or no negative `(m²/ℓ)`); nonunits can still have value 0. The sieve screen requires the qualifications below. |
| F2 twelve C-even R₈ zeros | **Missing from memo's substantive check:** 8/131 is a valid threshold-free numerator calibration, but is not these twelve inputs. Independently all twelve are prime and have n_p≤29, list `7,3,23,19,29,3,3,3,5,3,13,2`. Their R₈=0 certificates are inherited; full R is positive there, so they refute only a corresponding C-even transfer, not full (★) positivity. |
| F3 285 composite zeros | Memo substitutes the stronger Type-II counterexample 4545 for the full screen. Independently all 285 are nonsquare composites and admit a prime ℓ≤41 with `(ℓ/n)=−1` (equivalently `(n/ℓ)=−1` for odd ℓ since n≡1 mod 4). Hence the non-residue layer survives at all 285 inherited R-zeros; no all-285 R census was rerun. This does not refute a prime-only implication. |
| F4 14 (★) / 38 𝔊* zeros | Fourteen check is correct and independently strengthened above. The 38 are omitted: all are prime and have n_p≤29. Their inherited 𝔊*-zero status refutes the threshold-free non-residue→𝔊* implication, not necessarily non-residue→full (★). Function-field proxies do not substitute for this distinction. |

## Required fixes, in priority order

1. **Scope the claimed barriers everywhere, especially §5 and proposed FRONTIER text.** Replace “none transfers / each fails at a screen” by “no transfer demonstrated; these are the obstructions to the particular transfers considered.” A square matching p modulo every used modulus need not exist: e.g. p=409≡3 mod 7. Square-sensitive local/genus main terms are possible; T1 does not force all sensitivity into a sieve remainder. The cited low-conductor universality theorem concerns its specified smoothed blocks, not every sieve. Likewise fixed-q A4 is not excluded by a large-q/fixed-degree counterexample. Tied moduli prevent the stated black-box application, not all reformulations.
2. **Separate (★) from ES and retain thresholds.** Repair §0's bare “equivalent to ES”; under GRH the equivalence is to eventual (★) positivity. “ES-strength” may mean sufficient for eventual ES, not a proved converse. Fourteen zeros and 8/131 refute threshold-free statements only; §5's hard-screen slogans must retain this limitation.
3. **Complete F2–F4 using the actual supplied screens.** Add the twelve C-even inputs, all 285 composites, and 38 𝔊* inputs, with the domain/subfamily qualifications in the table. Do not label 𝔊* zeros as full (★) zeros or full R-positive numerator-8 inputs as R-zeros.
4. **Correct A1's count.** For k≥2, `k² log k ≪ Lφ(m)/m ≤ L ≍ k²log²k`; the lower scale is attained for primorial-type inputs, not uniformly as an asymptotic equality. Taking k primes all >k² makes φ(m)/m→1. The upper bound is still polylog in m, so the literal precedent is unaffected.
5. **Keep provenance/novelty modest.** Mark Shparlinski as V2 unless its original theorem is opened; distinguish its small-cardinality set from Shoup's low-degree set. Say “best found” for the explicit-basis bound. The opening “five mechanism classes” is inconsistent with the three literal-pass classes later listed; T/R are explicitly not literal passes.

After these fixes, **narrowed / no HOT LEAD** is justified as a literature assessment. Lemma 1 and the fourteen-input numerical result can be retained; the sweeping sieve or fixed-q nontransfer claims must not be recorded as theorems.
