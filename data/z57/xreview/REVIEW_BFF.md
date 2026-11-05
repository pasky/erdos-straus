# Z57 BFF hostile cross-review

**Verdict: ACCEPT-WITH-FIXES.** The exact reformulations survive independent derivation and testing.
The numerical extension is supported by sound code and consistent logs, with substantial partial reruns.
The literature/obstruction narrative needs correction; “narrowed” is defensible only as reformulation, not analytic progress.
**ES remains OPEN; neither eventual G* positivity nor a new pointwise ES theorem is proved.**
Reviewed `side-agent/z57-bff` at `95792e9e1e26754a5f8b72eb2c0837f0bb517de6`, including its memo, scripts and data.

## Per-claim findings

| Claim | Classification | Independent derivation / finding |
|---|---|---|
| Lemma 1.1, shift bijection | CORRECT | Put d=4nC−1: dm=p+n. Conversely divisibility gives positive integral m,C and the original equation; the inverse preserves ordered n. Since p is odd, n,m have opposite parity, so the two unordered witnesses have distinct d. |
| Lemma 1.2, five equivalent HIT tests | CORRECT | A witness has n≤(d+1)/4<d, hence n=n_d. The quotient (d+1)/(4n_d), when integral, is the unique inverse residue C_d. Swap coordinates for the C test. If 4n_dC_d=kd+1 then k≥1 and k≡1 mod 4, giving branches d+1,5d+1,… and both stated product thresholds. Multiples of p cannot hit. |
| Lemma 1.3 / Theorem 1 cutoff | CORRECT | With P≤Q, d_P=(p+P)/Q. For P≤p^(1/3), Q>(Pp)^(1/4) gives d_P<p^(3/4)+1; for larger P, d_P≤p/P+1<p^(2/3)+1. Conversely m>p/d and n≤(d+1)/4 imply m⁴>np when d⁴(d+1)≤4p³. Thus the equivalence includes the G* test, and d≤p^(3/5) is sufficient, not necessary. |
| Lemma 1.4, Jacobi obstruction | CORRECT | gcd(n,d)=1. Write n=2^k u; if k>0, d≡7 mod 8 removes the factor 2. Reciprocity gives (u/d)=(−1/u)(−1)^((u−1)/2)=1. Thus (−n/d)=−1, and p≡−n mod d plus p≡1 mod 4 gives (d/p)=−1. |
| Corollary 1.5, odd squares | CORRECT | A hit forces gcd(N,d)=1 even for composite N, whereas (M²/d)=1 contradicts the preceding Jacobi computation. Define composite-input HIT by divisibility (or require gcd(N,d)=1 before writing inverses). This rules out this solution shape, not ES at squares. |
| Lemma 1.6, levels 1–3 | CORRECT | Divisors are sub-multiset products. Mod 4, failure excludes prime residue 3. Mod 8, failure excludes 7 and coexistence of 3 with 5, leaving {1,3} or {1,5}. Mod 12, failure excludes 11 and coexistence of 5 with 7, leaving {1,5} or {1,7}. These are precisely the splitting classes for the stated primitive norm forms. |
| Lemma 1.6, primitive representation step | CORRECT | For N=4Cp+1 at C=1,2,3, N is coprime to the relevant discriminant. Class-number-one forms of discriminants −4,−8,−12 give the primitive criterion; no ramified-prime exception arises here. For C=1, parity gives a odd, b=2s and p=t(t+1)+s²; gcd(a,b)=gcd(2t+1,s). |
| §2.1, exact character identity / main term | CORRECT | Expand each divisibility indicator by additive orthogonality and sum n over divisors of (d+1)/4. Uniqueness of n_d prevents multiple hits per d. Since 1/(4k−1)=1/(4k)+O(k^−2) and Στ(k)/k=(1/2)log²K+O(log K), A(D)=(1/8)log²D+O(log D). Substitution D=p^(3/5) gives 9/200. This is not a proven prime-conditioned mean. |
| §0, Burgess D/4 asymptotic | CORRECT-WITH-FIX | For d=4j+3, χ(d)=χ(j+3·4^−1 mod p), a shifted interval sum. Burgess's uniform shifted estimate gives power saving for D≥p^(1/4+ε) (take D≤p, as sufficient here). Half the D/4 candidates are non-residues, hence D/8, **not D/4**: see required fix 1. |
| §0, no known positive proportion below p^(1/4) | WRONG as written | The unrestricted claim is contradicted by Banks–Garaev–Heath-Brown–Shparlinski, Theorem 2.1 [1], which gives positive density already at p^(1/(4√e)+ε). Their theorem does not itself give the same result in d≡3 mod 4. Separate these statements. |
| §2.2, logarithmic obstruction | CORRECT | Set q=lcm(4,1,…,D₀). Any p≡1 mod q has (p/d)=1 for every eligible d≤D₀, hence no hit. Linnik [3] gives q<p≪q^L and log q∼D₀. Choosing D₀≈2 log p₀ yields p∈[p₀,p₀^C′] and c log p≤D₀ for sufficiently small fixed c. |
| §2.3, S1–S3 implications | CORRECT | S1 selects the first branch because the next is (5d+1)/4; S2 is Lemmas 1.1–1.3. For S3, nonmembership in S_C supplies a level-C solution. If outside G*, Q⁴≤Pp≤Qp implies Q≤p^(1/3), but 4C≤p^(1/3) forces PQ>p/(4C)≥p^(2/3), contradiction. |
| §2.2 / §4, “decisive range d≤p^(1/3)” | GAP | No equivalence or reduction to that range is established. The proved sufficient range is p^(3/5), and the exact range is p^(3/4)+1 with membership. Derivative-test limitations do not eliminate larger d. |
| §2.2, universal sieve limitations | GAP | The asserted K=o(log X/log log X) ceiling and “cannot show <1” are not proved or sourced. They may describe a contemplated implementation, not all upper-bound sieves. |
| §3, least prime QNR ≥5 at all zeros | WRONG literally | Eight zeros have (2/p)=−1, beginning with p=37. The script explicitly starts primes at 3: its statistic is least **odd** prime QNR. |
| §3, exhaustive C decider | CORRECT for stated inputs | Integer cutoff correction and unsigned-128 membership are safe at B≤6·10¹². Sieve starts at max(q²,ceil(lo/q)q), marks odd multiples, and covers all eligible primes. Early exit preserves existence. A final even hi is harmless because it terminates the interval. |
| §3, certification / first-hit evidence | CORRECT within audit scope | Reruns and independent checks below agree; full 10¹² exhaustion was not repeated. The tail prediction ≈6·10^−14 is explicitly a model, not a certificate or proof of finitely many zeros. |

## Required fixes, priority order

1. **Correct the factor two in the Burgess count (summary Lemma 1.4).** There are D/4+O(1) integers
   d≡3 mod 4 below D, so the non-residue count is **D/8+O(D^(1−δ))**, not D/4.
2. Replace the blanket below-p^(1/4) ignorance claim with the actual distinction: unrestricted positive density
   at exponent 1/(4√e)+ε is known [1]; asymptotic equidistribution in this particular progression follows above
   1/4 from [2]. Neither result proves HIT positivity. Do not identify a known sufficient threshold with a necessary obstruction.
3. Qualify “decisive range” as an attack choice, not a theorem. Replace universal sieve-impossibility language
   by “no pointwise estimate supplied by this approach.” “Narrowed” must not mean larger-d routes have been killed.
4. Rename the local statistic “least odd prime QNR” throughout; separate the standard least-nonresidue Burgess
   bound from any claim excluding the prime 2 (supply an appropriate source if retaining that stronger formulation).
5. Preserve the explicit limitations on the computation/model. The finite certificate is not evidence strong enough
   to certify the tail prediction; the present review independently exhausts only the ranges stated below.

## Numerical audit and reproducibility

All shell commands ran with `ulimit -v 6000000` (initial status used a lower limit) and explicit timeouts.
Audit script: `scripts/z57_xrev_bff_audit.py`; archive root used: `/tmp/xrev_BFF`.
The script streams small enumerations; no large Cartesian arrays are allocated.

- Recompiled `z57_bff_decide.c` with `cc -O3 -Wall -Wextra … -lm` (only an unused-variable warning).
- **Actual exhaustive rerun [5,10⁹]: 25,423,491 primes, exactly the same 38 zeros; last zero 564,661,441.**
  Maximum first-hit d=787,439 at p=231,507,061 agrees. This covers the small zeros and the decisive extra zero.
- Independent ordered-small-coordinate / C enumeration at all 609 primes p≡1 mod 4 up to 10⁴:
  2,882 G* solutions, no mismatches with the d cutoff enumeration.
- Independent hyperbola/branch/Jacobi tests: 39,682 (p,d) cases, 570 hits, plus 50 odd-square controls; all agree.
- Primitive norm tests: 342 prime/level pairs, including all 38 zeros at all three levels; all agree.
- Parsed all 192 decider blocks: contiguous coverage [5,10¹²], sums 18,803,924,340 primes and 38 zeros.
  The three extension sums are 1,831,497,005; 7,595,037,851; 9,149,866,209, exactly as reported.
  Independently rescanned every d through the reported first hit at all 192 extremal primes; all agree.
  This checks those witnesses/minimalities, **not** each block's asserted maximum or every prime above 10⁹.
- Actual upper-endpoint rerun [999,999,900,001,10¹²] and independent SymPy primality / integer witness scan:
  1,788 primes, no zeros, maximum first-hit d=3,455 at p=999,999,980,701; agreement.
- All 22,582 sample first hits independently checked, including G* membership and minimality.
  Sample sizes 10,819 / 9,613 / 2,150; means .109366 / .097338 / .087800;
  medians .059640 / .053013 / .084510; maxima .492109 / .502925 / .344762 agree.
  Near 10⁸, 9 missing recorded prime-d hits plus 2 recorded corner hits agrees with the stated 11.
- Actual least prime QNR is 2 at zeros 37,157,1621,4357,12301,184837,434437,571741.

Reproduce after extracting the reviewed branch's scripts/data into `/tmp/xrev_BFF`:
```sh
ulimit -v 6000000; timeout 20s cc -O3 /tmp/xrev_BFF/scripts/z57_bff_decide.c -lm -o /tmp/xrev_BFF/decide
ulimit -v 6000000; timeout 180s /tmp/xrev_BFF/decide 5 1000000000 > /tmp/xrev_BFF/rerun_le1e9.txt
ulimit -v 6000000; timeout 180s uv run --with sympy scripts/z57_xrev_bff_audit.py /tmp/xrev_BFF
```

## Sources checked directly

[1] Banks–Garaev–Heath-Brown–Shparlinski, *Density of non-residues in Burgess-type intervals and applications*,
[arXiv:math/0607692v3](https://arxiv.org/pdf/math/0607692), Theorem 2.1, p.3:
|Σ_{n≤N}(n/p)|≤(1−δ)N for p^(1/(4√e)+ε)≤N≤p. Their following remark explicitly warns about rational progressions.
[2] Elkies, [*The Burgess bound on short character sums*](https://people.math.harvard.edu/~elkies/M229.09/burgess.pdf),
Theorem (5), p.5: uniform bound N^(1−1/r)p^((r+1)/(4r²))(log p)^(1/(2r)) for shifted sums, r≥2.
[3] Tao, [*254A Notes 7*](https://terrytao.wordpress.com/2015/02/22/254a-notes-7-linniks-theorem-on-primes-in-arithmetic-progressions/),
Theorem 1: a primitive residue class modulo q contains a prime ≪q^O(1). No optimal exponent is needed here.

**Disposition:** retain Lemmas 1.1–1.6, the exact identities and finite computational results;
correct the Burgess normalization/literature claims and narrow the negative assessments before synthesis.
