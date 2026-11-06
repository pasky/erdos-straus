# z60 LOPEZ hostile cross-model review

**Verdict: ACCEPT-WITH-FIXES.** Core proofs survive; the narrowed verdict follows in the stated coordinates. No ES proof, pointwise rescue mechanism, or asymptotic tail-dependence theorem follows. ES remains OPEN.

Reviewed branch `side-agent/z60-lopez` at `6bcea16611101a8ebb91db22a80ebddb80694ae3`, memo `Z60_LOPEZ.md`, production scripts and archived data. Independent work used one compute process at a time, `ulimit -v 4000000`, command timeouts ≤ 300 seconds. No full 10¹⁰/10¹² census rerun is claimed.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| Lemma L: (iii), (P), (J), (X) | CORRECT | All implications re-derived, including letters 1 and f = 3; details below. |
| Jacobi dichotomy; Div⁺ dictionary; residue counts | CORRECT | Odd divisors have Jacobi +1; the only negative divisor class is v₂(r) = 1 when f ≡ 3 (8). Residue 1 is shared, not disjoint. Exhaustive checks for all 500 eligible f ≤ 2000 agree. |
| Prop E(a): inversion and scaling | CORRECT | a·4(m_f/a) ≡ 1; in n-coordinates inverse of −n is −n⁻¹, so the sign in the stated branch swap is correct. The two preserving involutions also check. |
| Prop E(b): exchangeability in law | CORRECT | Fixed-X, limiting prime distribution only. Inversion preserves the conditioning sets and swaps the entire event vector. Not an assertion of independence, finite-sample symmetry, or a link at the same prime. |
| Coupling/nonresidue lower bound | CORRECT | (p/f) = −1 and p ≡ 1 (4) give (f/p) = −1, hence an odd prime factor ℓ of f has χ_p(ℓ) = −1. This lower bound alone says nothing about covariance. |
| Prop D(f), p-independent link obstruction | CORRECT | The progression p ≡ 1 modulo the stated lcm is reduced and has infinitely many primes. r = f−1 cannot divide f+1 except f = 3, excluded by its Jacobi sign. |
| Prop D(a,T) | CORRECT, CONDITIONAL | The Dickson construction is admissible; coefficient divisibility, divisor exclusion and factors of four in the index bounds all check. No unconditional conclusion in these coordinates is justified. |
| Lemma 7(i)–(v), U₇ inclusions and squares | CORRECT | Word/divisor dictionaries, complete fallback bound, parity split, complete moduli 7 and 15 all check. Neither strictness of the conjectural MS implications nor prime existence is proved. |
| U₇ certified range/counts | CORRECT within disclosed certification model | Independent low enumeration and high slices agree; every archived LATE certificate and census footer checked. Above 10⁶ this remains one full production engine plus independent checks, not a second full census. |
| Deep-tail/bulk data | CORRECT as EVIDENCE | All 48 archived stratified obs/exp/ratio entries reproduce; a-histogram independently reproduces raw counts. Fresh independent experiment agrees with production. No every-stratum or causal inference follows. |
| López Conjecture 1 / inversion citation | CORRECT | Checked directly against live arXiv v3: Conjecture 1, Theorems 4 and 7, mutual-inverse remark, and first 10,000 primes through 104729 match. |
| “Branch A = López Type A” on the memo's odd-integer domain | CORRECT-WITH-FIX | Only the prime-domain identification is valid without qualification. López's Definition 3 includes inherited composite Type A solutions; the memo's A-line does not. See fix 1. |
| “No complementarity / no link law”; narrowed verdict | CORRECT-WITH-FIX | Main sections mostly scope this correctly, but title and final causal-sounding prose outrun the evidence. Adaptive/p-dependent mechanisms remain unexcluded. See fix 2. |

## Proof audit

**Lemma L.** For an odd divisor h of f+1, reciprocity gives (h/f) = (f/h)(−1)^((h−1)/2) = 1. Factoring x = 2ʲh then gives the stated dichotomy using (2/f). From n+x = z(xy−1), gcd(n,f) = 1. If x < f, its residue is the divisor x; if x ≥ f, y = 1 and x = f+1, whose residue is 1. Conversely (J) constructs (r,(f+1)/r,(n+r)/f); the bad 2-adic split is excluded by its sign. The identity (xy−1)(zy−1) = yn+1 proves (iii) in both directions: the complementary divisor is −1 mod T, and either 4|T or 4|(f+1)/T. For (P), take a=x when 4|y and a=x/4 when 4|x, reversing x,z if necessary. The converse constructions produce the required word. The residue union counts subtract the duplicate 1 ≡ f+1 and are correct.

**Prop E.** Work in unit classes modulo one finite L_X; the finitely many primes dividing L_X are negligible. Inversion preserves 1 mod 24 and the Mordell square subgroup modulo 840. The prime number theorem in progressions makes the relevant unit classes equiprobable in the limit. Thus every fixed-X truncated pair has a symmetric limiting law. The argument has no uniformity when X grows with the prime cutoff and no pointwise existence consequence.

**Prop D.** For its conditional part, M is divisible by (k+1)L_k; both auxiliary primes are 1 mod L_k. After removing repeated forms, their product has no fixed prime divisor because every form is 1 at t=0. Dickson supplies arbitrarily large t so q_k,Q_k > k+1. Every divisor is e or eq, e|k+1, and has residue e. For 4∤k, L_k=4k>k+2; for 4|k, the only possible positive e≤k+1 congruent to −1 is k−1, which cannot divide k+1. Translate B's shift a via k=a, A's via k=4a, B's middle parameter C via k=4C, and A's via k=c. For any fixed X and finite g(X), enlarging the construction bound to max(4X,4g(X)) contradicts the proposed implication. This does not exclude g depending on p or other kinds of joint-failure arguments.

**Lemma 7.** f=xy−1 converts 8|xy into f≡7 (8); the residue-1 boundary is handled exactly as in Lemma L. The shift and middle-letter forms follow by CRT compatibility and the product identity. All divisors of f+1 have Jacobi +1, so a hit has (n/f)=−1 and cannot be a square. For n≡3 (4), f=2n+1 and r=n+1 work. A B-word (u,4C,B) at n≡1 (4) has u+B≡3 (4), hence an even outer letter; reverse them if needed. In an A-word (4d,c,b′), b′≡3 (4), and the U₇ condition is cd even. The U⁽⁸⁾ target residues are a subset of the divisors of f+1. Listing r={1,2,4} at f=7 and r={1,2,4,8} at f=15 proves completeness. Finally f>n forces r=f−n|n+1, so every hit satisfies f≤2n+1: the exact fallback is exhaustive.

## Independent computations

- `scripts/z60_xrev_lopez_independent.c`: independent word sieve, all odd n≤10⁶, exactly Z₇ = {105,1465,3865,4545,10305,12145,39361,67425}; all 500 odd squares including 1 excluded. Production rerun agrees (its input loop omits n=1, hence 499 skipped squares).
- Direct f-search on 5,000 n≡1 (4) in [9,999,980,000,10¹⁰): every input has a witness, maximum least f=14,351; production slice agrees.
- Direct f-search on 6,000 Mordell inputs in [999,999,160,000,10¹²): every input has a witness, maximum least f=8,975; production slice agrees. These slices contain no squares. The independent high search treats an unresolved input as an error, never as a proved zero.
- `scripts/z60_xrev_lopez_archive.py`: all 342,375 LATE pairs satisfy f≡7 (8), 0<r<f, r|f+1 and f≤2n+1. All nine compressed census files have consistent footers, late/zero counts, input totals and exact square counts. Upper Mordell range: 7,071,428,573 inputs − 205,714 squares = 7,071,222,859 non-squares.
- All 48 stratified entries recomputed by streaming N_s,A_s,B_s,AB_s; histogram total 6,354,932. Raw a-ratios at X=3,6,13 are 1.449311, 4.027618, 15.810046 (joint counts 37,335; 2,346; 107), agreeing with the memo.
- `scripts/z60_xrev_lopez_tails.c`: entirely independent trial-divisor search on all 158,595 primes p≡1 (24)≤2·10⁷. At a-thresholds 3,6,13, joint counts are 1,666;137;14, raw ratios 1.376228;2.887521;10.666868, least-nonresidue-stratified ratios 0.787330;1.014691;2.375958. A fresh production run agrees on all counts and ratios. This independently recovers the bulk deficit and deep-tail excess; the X=6 stratified excess here is very small.
- Existing four-form check rerun through n=801: zero mismatches, only nonsquare zero 105. Full 10⁹ raw prime records and score-bin statistics were not independently regenerated; the archived histogram/sufficient statistics are aggregate audit trails, not independent proofs of the full raw run.

## Mandatory falsifier audit

| Screen | Independent finding | Assessment |
|---|---|---|
| F1 odd squares | No square hit in independent word enumeration; general Jacobi proof valid. Prop D's prime construction is locally square but globally nonsquare. | Correct for the defined branches/U₇; do not extend to all López Type A solutions at composites. |
| F2 C-even/numerator-8 | Directly checked all 12 `r8_zeros_1e10.txt` inputs: all have U₇ witnesses. R₈ is the C-even B-subline, not U⁽⁸⁾. U⁽⁸⁾⊂U₇ and the extra target exponents v₂((f+1)/8)<v₂(r)<3 are correct. | Mandatory control passes. The F2 row should explicitly name these 12 controls, currently relegated to F4; 547 broader U⁽⁸⁾ zeros are an additional screen, not a replacement. |
| F3 285 composite zeros | Directly checked all 285: exactly eight U₇ failures, namely Z₇; 277 rescued. Each of the eight was searched through the complete bound 2n+1. | Correct; the target does not “survive all composites” without its stated exceptions. |
| F4 14 (★)-zero / 38 𝔊*-zero primes | Direct witnesses found for every entry in both files (lists overlap); all 12 F2 primes also rescued. | Correct. Rescue of individual known primes is not a link law or a proof for all primes. |

## Required fixes, priority order

1. **Qualify the composite Type A terminology.** In notation and F1, replace unqualified “branch A = López Type A” by “the A congruence/word line, equivalent to López Type A at primes.” López's Definition 3 and composite discussion explicitly permit inherited Type A solutions at squares. Counterexample: 4/25=1/10+1/25+1/50, with (10,25,50)=(du,dv,duv), d=5,u=2,v=5; nevertheless the memo's A-line has no hit at 25. The internal congruence proofs remain valid; no extension of prime-only Theorem 7 to all odd composites is warranted.
2. **Scope headline and bottom line as carefully as §3.2.** Replace the title's blanket “no complementarity found between the branches” with “no complementarity in the tested deep-tail events; weak bulk complementarity.” Replace “They do not interact the way a link would” and “Joint failure is rare because…” with an explicitly empirical/Assessment statement about pooled exceedances. Retain fixed-X limiting scope for exchangeability, EVIDENCE for dependence, and the unconditional-f/conditional-a,T split for no p-independent first-witness law. None of these results kills adaptive or p-dependent mechanisms.
3. **Put the actual F2 control in the F2 row.** State that all 12 certified C-even R₈-zero primes in [10¹⁰,1.1·10¹⁰] are rescued by U₇, while distinguishing R₈ from the larger two-branch U⁽⁸⁾. No numerical change is required.

Live source checked: https://arxiv.org/html/2404.01508v3 (Definition 3, composite Type A discussion, Theorems 4/7, Conjecture 1 and following remarks). The conjecture and attribution are faithful; the composite naming caveat comes from this same source, not an inference from secondary summaries.

Reproduction: extract the reviewed branch's files into `/tmp/xrev_LOPEZ`; compile/run the two independent C scripts with `gcc -O2` (`-lm` for `independent.c`), passing the four `data/z58/screens/*.txt` files to `independent`. Save the tails output as `tails-independent.txt`; optionally save `z60_lopez_joint 1 20000001 0 13 3 1` as `joint-small.txt`. Run `uv run python scripts/z60_xrev_lopez_archive.py /tmp/xrev_LOPEZ`. Prefix each command with `ulimit -v 4000000; timeout 300`; do not run more than two compute processes.

**Disposition:** accept the mathematical core and one-engine CERTIFIED census with the disclosed independent checks; apply the three wording/screen fixes before integration. “Narrowed + sharper target; no mechanism; not a HOT LEAD” is supported. Waiting for parent disposition.
