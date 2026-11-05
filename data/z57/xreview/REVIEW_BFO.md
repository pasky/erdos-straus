# Z57 BFO — independent hostile cross-review

Reviewed `side-agent/z57-bfo` at `c06fe1e0d9fa8d6324af8089b6be146f5815f47a`.
**Verdict: ACCEPT-WITH-FIXES (analytic commentary only). Theorem W is CORRECT. ES remains OPEN.**
The pointwise target is still inconclusive, not dead; W strengthens the almost-all result, not the pointwise conclusion.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Lemma 1.1, ordered shift count | CORRECT | The quotient is positive; odd n forces opposite parity, giving exactly two orderings per solution. |
| Lemma 1.2, divisor-in-class | CORRECT | From m=4sC−1 and t=(n+s)/m recover the equation; conversely use m=4oC−1. Positive divisors and odd n≥3 are essential and stated. |
| Lemma 1.3, level factorisation | CORRECT | d d′=4Cn+1 and d≡−1 mod 4C imply d′≡−1; recovered entries have opposite parity. Thus no fixed point d=d′ and the factor 2 is correct. |
| Lemma 1.4, complete-level inclusion | CORRECT | Outside G*, Q⁴≤Pp≤Qp gives PQ≤Q²≤p^(2/3), contradicting PQ>p/(4C)≥p^(2/3). Equality 64C³=p causes no gap. |
| Lemma 1.5, mod-p form | CORRECT | The only positive multiple of p below 2p is p. Opposite parity follows, and swapping entries supplies the designated odd/even labels. This is unrestricted R unless G* is added, as the memo notes. |
| Lemma 1.6, Jacobi / squares | CORRECT | Reciprocity derivation below; requires p≡1 mod 4 for the claimed Legendre sign, explicitly scoped in the memo. Recomputed all 2,080 solutions below 6,000; no violations; no solutions at 9,25,…,79². |
| Lemma 2.1, three fibrations | CORRECT | All maps invert. For fixed m, 1≤s≤(m+1)/4<m gives the unique residue r; p+r=jm and m+1=4rC imply p=4rjC−r−j. This algebra does not prove a barrier to every analytic method. |
| Lemma 2.2, genus-exact moduli | CORRECT | Odd prime factors must be 3, its exponent at most 1, and the 2-adic exponent at most 3; hence 4m divides 24. In exponent-2 groups a generated element uses each eligible prime class at most once, so the stated subgroup criterion is valid. |
| Lemma 2.3, bounded exponent | CORRECT | Prime-power Carmichael formulae give precisely the divisors of Λ(k), including k odd (only q=1,2). For a unit target class, characters of orders dividing k separate it from every other unit iff the common kernel is trivial, equivalently exponent divides k. |
| Theorem W, fixed K | CORRECT | Distinct forbidden residues, sieve denominator and Rankin lower bound all check; details below. Finite small primes are absorbed in the K-dependent constant. |
| Theorem W, every A | CORRECT | Choose a fixed K depending on A with 1+κ_K≥A, then apply W. No uniformity in growing K is used. |
| §3(v), level-K frequencies | EVIDENCE: reproduced | Seeded 12,000-prime experiment reproduces the stored file exactly. Fitted exponents 0.45,0.89,1.19 are observations, not consequences of W's upper bound. |
| §4.1, pseudo-squares | EVIDENCE: reproduced | Independent Euler-criterion computation gives q≥11 for 20/38, q≥17 for 8/38, q=2 for 8/38; seeded random comparison also reproduces exactly. Eventual pseudo-square lemmas are correctly not excluded. |
| §4.2, Burgess model | CORRECT as calibration | Reproduced 0.995,0.857,0.469 and independently obtained half-bound decades 67.2451,23.6853,9.4285. This is not a proof excluding other effective arguments. |
| §4.2, Pólya–Vinogradov applicability | CORRECT-WITH-FIX | A √q log q bound is not nontrivial at N=√q. Replace “θ≥1/2” by “fixed θ>1/2”, and retain the necessary size/constant qualification. |
| §2.6, GRH description | CORRECT-WITH-FIX | GRH is not merely an averaged-in-p input; it gives pointwise-in-modulus character-sum / least-nonresidue information. Say no implication to this divisor-in-class target was established, not that GRH only controls averages over p. |
| §5, extended certification | SUPPORTED; partially rerun | All four prime totals independently reproduced over the full intervals; all 20 recorded exceptional rows independently enumerated; four million integers rerun through the original decider. Not a second full-interval solution census. |
| §0/§6 verdict and labels | ACCEPT | Target explicitly unproved, methods' failures labelled Assessment, squares/composite evidence not promoted to a prime theorem. Neither the order≥3 route nor ES is “killed”. |

## Proof details for the decisive theorem

For d=4Cu−1 dividing 4Cn+1, gcd(d,Cn)=1 and (−Cn/d)=1.
Writing C=2^a c with c odd, reciprocity and d≡−1 mod 4c give (c/d)=1;
if a>0, d≡−1 mod 8 gives (2/d)=1. Hence (−C/d)=−1 and (n/d)=−1.
For p≡1 mod 4, (d/p)=(p/d)=−1; for n an odd square this contradicts coprimality. No primality of d is assumed.

W Step 1: for p>max(Q,64K³), every prime divisor ℓ≡−1 mod 4C would give a forbidden complete-level hit.
For ℓ>4K+1, the residues −(4C)⁻¹ are nonzero and pairwise distinct, so ω(ℓ)=1+Σ_{C≤K}1[ℓ≡−1 mod 4C]<ℓ.
Small ℓ retain only the primality exclusion 0; deleting finitely many level exclusions changes constants, not dimension.
Step 2: the arithmetic large sieve gives |P|J≤x+Q²; replacing ω/(ℓ−ω) by ω/ℓ only decreases J.
Checked the denominator via [arithmetic large sieve, Theorem 4](http://jonismathnotes.blogspot.com/2014/12/the-large-sieve-and-bombieri-vinogradov.html), including its Ramanujan-sum/Cauchy proof.
Checked the sharp analytic input in [Kedlaya, Theorem 15.5](https://kskedlaya.org/ant/chap-largesieve.html#T-large-sieve): δ-separated frequencies give N−1+δ⁻¹; reduced fractions q≤Q are Q⁻²-separated.
The original Montgomery–Vaughan PDF endpoint returned HTTP 403; these accessible sources establish the precise needed statement, not just a citation match.
Step 3: fixed-modulus prime-number theorems yield Σg(ℓ)logℓ=(1+κ_K)log y+O_K(1); partial summation yields Σg(ℓ)=(1+κ_K)loglog y+O_K(1).
Step 4: with z=Q^(1/s), σ=1/log z, the weighted tail / Euler product is at most exp(−s+(e−1)(1+κ_K)+O_K(σ)).
Choose fixed s large enough and then Q sufficiently large: at least half the Euler product remains below Q.
Since Σg(ℓ)² converges, that product is ≫_K(log z)^(1+κ_K), proving the asserted denominator lower bound.
Step 5: Q=x^(1/4), the removed O_K(x^(1/4)) primes, and κ_K≥(log K)/4 give both conclusions.
The minor order of choices “s fixed, then Q large” is legitimate; no circular uniform-in-K bound is needed.

## Computational scope and reproducibility

All shell invocations used timeout and ulimit; numerical jobs used at most 6,000,000 KiB virtual memory and bounded CPU time.
Exported the pinned branch's inputs to `/tmp/xrev_BFO`; committed independent checks are `scripts/z57_xrev_bfo_check.py` and `scripts/z57_xrev_bfo_primecount.c`.
The Python check uses P≤Q, P≤(1+√(1+4n))/4, and divisors of n+P (with a direct C scan for large P), not the source's three-region enumeration.
Its enumeration agrees with direct P,Q brute force for all 599 odd n in [3,1200); it independently verifies all 38 listed G*-zeros, last 564661441.
Every one of the 20 stored large-prime exceptional rows agrees in all five counts; HC zeros total 19, H3 zeros 14, F4 zeros 0, F4L zeros 1 among those records.
At 11406999713 it gives 23 unordered solutions (R=46), HC=6, H3=6, F4=15, F4L=0, agreeing with the memo.
The independent AP-only segmented sieve gives chunk prime counts **54014828,53548622,53169212,52845953**, total **213578615**, exactly matching all four summaries.
Original decider reruns on [a,a+999999], a=10000000001,12500000001,15000000001,17500000001 give 21747,21454,21326,21231 primes and no F4 zeros.
The second rerun reproduces the row at 12500593681. All four original full-range logs contain the expected terminal interval summary.
Code audit: early positives use proven complete-level inclusion; the fallback partitions C≥Q≥P, Q>C≥P, Q≥P>C exhaustively; integer power tests are safe in this range.
The floating division helper is safe for these ≤2·10¹⁰ inputs (roundoff far below 1/2, final integer product check); no missed-case or overflow defect found.
**Limit:** the independent prime count does not recertify solution existence for every prime. Full “no omitted F4 zero” coverage rests on the inspected original exhaustive run and code; I did not repeat that entire solution census or the inherited ≤10¹⁰ census.
The inherited composite-zero statistics (285,57,26), Theorem V, and growing-K heuristic are not new proofs here and were not independently recertified.
Seeded levelK/lqnr scripts and Burgess-calibration script rerun byte-for-byte against stored stdout; the original slow lemma script was replaced by proof checks and the independent enumeration.
Reproduce under `ulimit -v 6000000; ulimit -t 300`: `timeout 280s uv run --with sympy python scripts/z57_xrev_bfo_check.py /tmp/xrev_BFO`.
Compile the prime-count check with `timeout 20s gcc -O2 -Wall -Wextra -Werror scripts/z57_xrev_bfo_primecount.c -o /tmp/xrev_BFO/primecount`, then run with `timeout 280s` under the same limits.

## Required fixes, in priority order

1. §4.2: restrict the Pólya–Vinogradov saving claim to fixed θ>1/2 (or explicitly require √q log q=o(N)); the endpoint θ=1/2 is not covered. No finite p₀ bound follows from the displayed constants alone.
2. §2.6: replace the blanket characterization of GRH by the narrower, supported assertion that no GRH-to-target reduction was found; GRH itself has pointwise consequences.

No correction to Theorem W or Lemmas 1.1–1.6 / 2.1–2.3 is required. Bank W, retain the limited certification provenance, and keep the pointwise target OPEN.
