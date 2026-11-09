# Z68 U7F — hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** The narrowed/inconclusive verdict is justified; no universal mechanism is proved.
Reviewed `side-agent/z68-u7f` at `11cd0e4da1e2c8a69cb05713e5562df4ac7a650d`, including Z60 item 4/Lemma 7 and the mandatory screens.
The principal lemmas and all decisive prime counts survive. The new ω≤2 refinement fails at a mandatory **U₇-positive composite**, which the falsifier table omits.

## Per-claim audit

| Claim | Classification | Independent finding |
|---|---|---|
| Lemma 1(a,b), symmetric/lcm forms | CORRECT | Set y=(n+x+z)/(xz); 8 divides xyz. Both outer letters cannot be even; an odd outer letter permits the required orientation. Positivity uses n≥1. |
| Lemma 1(c), four types and U⁽⁸⁾ | CORRECT | For n≡1 (8), x+z≡7 forces exactly one even letter. Type 0 supplies an outer multiple of 8; types 4/2/6 require 8∣y for U⁽⁸⁾. Pair orientation and the y=1 caveat matter. |
| Lemma 1(d), sum–product form | CORRECT | k odd and k²−4m=j² force j odd; m>0 implies j<k. Thus (k±j)/2 are positive integers, not merely rational roots. |
| Lemma 1′, hyperbola/CF | CORRECT | Inverse residues give ab=1 or f+1 exactly; direct rational expansion verifies all three CF cases. Independently checked 17,190 identities. |
| Lemma 2, eight divisor/subgroup tests | CORRECT | Complementary divisor residues and the Klein four group give the stated exclusions. The norm-form implications are necessary only, correctly distinguished from S_H membership. |
| Prop 3.2, whole mod-8 representation classes | CORRECT | The displayed square family satisfies the identity, and signs/swapping cover all 16 odd classes. This says nothing against prime-only/admissibility-filtered rules. |
| Prop 3.6, smooth-part reduction | CORRECT | Exact valuations give s_r=r+1; L_r∣M/(r+1) gives Q_r≡1. Divisors e and eQ have square-point residue data, so a successful divisor needs a proper rough factor. Outer letters only. |
| §3.1 bounded-both-outer-letters obstruction | CORRECT | The progression p≡1 modulo the stated common modulus reduces every candidate to n=1; Dirichlet applies to the unit class. One bounded letter is not excluded. |
| §3.5 enumerated large-y candidates | CORRECT, limited scope | For p≥17, y≥p−2 and xz≥2 imply xyz−x−z≥2y−3>p. Therefore x=z=1, y=p+2 is the only possibility. The r>p+1 boundary also checks. This does not classify all controlled factorizations. |
| §3.4 “under no other natural map” | WRONG as written | T₇={3,5,6} is invariant under n↦2n mod 7. If a uniform-in-f exclusion was intended, formulate and prove that instead. |
| §2/§4 prime census and single types | CORRECT | A new unordered-pair engine independently reproduces all three bounds through 10⁹, including complete no-prime lists and the 12 single-type primes. |
| Conjecture B | Honest CONJECTURE, prime-only | Stronger witness restriction; not proved strictly stronger as a prime existence predicate. Composite extension is false at 196065, even though U₇ holds there. |
| §3.3/§3.7 and §6 strategy conclusions | CORRECT-WITH-FIX | Basic equidistribution errors and explored failures do not exclude cancellation across moduli, admissibility-filtered norm rules, or growing outer letters. “The one ... input a proof must control” exceeds Prop 3.6. |
| §5 growth and Conjecture A heuristics | Assessment only | Labels are appropriately non-theorem. Summability for the B model suggests finitely many exceptions, not zero exceptions. Finite prime-witness failures do not rule out an eventual prime-witness theorem. |

### Proof checks beyond the table

For Lemma 2, direct substitution into xyz−x−z=n agrees with D and ¬F for all 19,552 primes p≡1 (8) through 10⁶: zero mismatches, exactly 43 primes fail all applicable families.
The outer-3 line needs its stated p≡1 (3) hypothesis. A hypothetical zero with p≡2 (3) is already excluded by (4,(p+7)/12,3), so the necessary-condition consequence is sound.
All eight Z₇ composites fail the applicable small-shift tests; 51 odd squares through 101² fail them and have no U₇ witness.
Prop 3.2 covers 16/16 classes; Prop 3.6 independently checks at all seven indicated primes below 2·10⁹, with zero violations.
The compact-null-set assertion in §3.4 can be justified by CRT over prime f≡7 (8): each removes at least 3/f of the residues and the corresponding reciprocal-prime sum diverges. This gives no prime-avoidance theorem.

## Independent census

`scripts/z68_xrev_u7f_census.c` enumerates x≤z and y≥2 using y≤(N+2x)/x² and z≤(N+x)/(xy−1), then includes y=1 separately.
It tests both orientations, sieves primality and distinct-factor counts, and does not use the lane's f/divisor-of-(f+1) enumeration.

| N | Primes p≡1 (8) | U₇ zeros | No prime witness | No ω≤2 witness | Single-type primes |
|---|---:|---:|---:|---:|---:|
| 10⁷ | 165976 | 0 | 66 | 0 | 12 |
| 10⁸ | 1439970 | 0 | 118 | 0 | 12 |
| 10⁹ | 12711220 | 0 | 231 | 0 | 12 |

All no-prime lists agree element-for-element with the archives; the type lists agree where archived (10⁷ and 10⁹).
The 12 single-type primes, including y=1, are exactly the memo's lists, with counts 3/3/4/2 for types 0/4/2/6.
The independent 10⁹ run takes 76 seconds and peaks at 2,076,100 KiB RSS; one compute process, `ulimit -v 6000000` and timeout 1800 throughout.

| Spot prime | All witness moduli f, exhaustive through 2p+1 | Types / prime witnesses |
|---|---|---|
| 2521 | 87 | Type 2 only; no prime witness; r=2. |
| 21841 | 575, 2431, 21975, 22167 | Type 6 only; no prime witness; ω values 2,3,3,2. |
| 66529 | 39, 1623, 2559, 7415, 13311, 13647 | Types 2 and 6; no prime witness. |
| 225289 | 287, 967, 5495, 37679 | Type 6 only; prime witness 967. |

None of these four has a y=1 word. The bound is exhaustive: when f>n, r=f−n is a proper divisor of f+1, hence r≤(f+1)/2 and f≤2n+1.

## Falsifier audit

| Screen | Result |
|---|---|
| F1 odd squares | CORRECT. A hit forces gcd(n,f)=1 and (n/f)=−1, impossible for a square. The extra ω restriction cannot rescue squares. |
| F2 12 C-even R₈ zeros | All 12 independently receive ω≤2 witnesses, with f≤2239. Do not identify R₈ with U⁽⁸⁾. Both factorization restrictions differ from U⁽⁸⁾: p=17 has prime witnesses 7 and 23 but no U⁽⁸⁾ word; p=2521 has only f=87 and no U⁽⁸⁾ word. The historical count 45 is read from Z59, not independently recounted here. |
| F3 285 nonsquare composites | Exactly the eight listed Z₇ numbers are U₇-zero. Of the other 277, **276 have an ω≤2 witness; 196065 does not**. Current F3 is accurate about Z₇ but incomplete about the new refinement. |
| F4 14 (★)-zero / 38 𝔊*-zero primes | Every listed prime independently receives an ω≤2 witness (f≤1735 / 1967 respectively). The four requested spot primes and their claimed types check as above. |

**New mandatory boundary:** 196065=3²·5·4357 has exactly one witness, f=13079=11·29·41, r=120, with word (120,109,15).
Exhaustive scanning to 392131 and a separate fixed-n unordered-word enumeration agree; the latter gives only {15,120}, y=109, including the y=1 search.
Thus ω≤2 is genuinely stricter than U₇ on composites, including this F3 control. This is **not** a counterexample to prime-only Conjecture B and does not refute ES.
The excluded residues need explicit scope: U₇ at n≡5 (8) is elementary via f=n+2,r=2; nothing here establishes the ω≤2 refinement on that omitted class.

## Required fixes, in priority order

1. **MAJOR, F3/§4.3/§6:** Record 196065 and its unique three-distinct-prime witness; say the refinement fails on one additional mandatory composite beyond Z₇. Keep Conjecture B strictly prime-only; do not advertise survival of all composite controls.
2. **MAJOR, §3.4:** Delete or precisely qualify the false “no other natural map” assertion (T₇ is a counterexample). Also say the complement move can leave U₇ entirely: at p=17, {4,3}→{4,7} has sum 11, not 7 mod 8; this is not merely a change between the four allowed types.
3. **SCOPE, §6:** Replace “the one non-congruence input a proof must control” with a statement about the explored small-outer-letter strategy on the progression in Prop 3.6. The proposition does not constrain every possible proof. Make the elementary n≡5 (8) reduction explicit when narrowing the lane's original p≡1 (4) target.

## Concrete directions not killed by §3

- Test moving-r witnesses f=3q^e (then 5q^e, etc.) on the prime-witness-free tail, retaining powers: neither bounded-both-letter obstruction nor the prime-f counterexamples kill this family. Classify actual failures before claiming it exhausted.
- Use simultaneous factorizations of p+1 and p+2 with valuation/gcd admissibility, required only when N(u,v) is prime; Prop 3.2 excludes none of these filtered representation rules.
- Explore growing k in Lemma 1(d), or cancellation across f with square-sensitive weights. Per-modulus Weil errors are not a theorem excluding such methods. No claim here that these directions will work.

## Reproduction / limits

Extract the reviewed branch's `data/z68/u7f/` and `data/z58/screens/` to `/tmp/xrev_U7F/`; compile the C script with `gcc -O3 -Wall -Wextra -Werror`.
Run it at 10000000, 100000000, 1000000000, saving `independent_1e7.txt`, `independent_1e8.txt`, `independent_1e9.txt` there.
Then `ulimit -v 6000000; timeout 1800 uv run --with sympy python scripts/z68_xrev_u7f_checks.py /tmp/xrev_U7F` checks lists, algebra, spots, and every screen.
No provider/auth/quota error occurred. Non-decisive least-f growth and pattern statistics were not separately recounted; no asymptotic claim is certified by this review.
