# z58 WILDCARD cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** The certified central censuses survive both reruns and an independent sieve. Lemmas 4.1–4.4 are correct. Two small model-description errors need correction; there is no new mechanism and no implication that ES is settled.

Reviewed `side-agent/z58-wildcard` at `18393f5f0fdcb6924b89bcbbe1b297f24b6f6f15`, especially `Z58_WILDCARD.md`, the census/count/model engines, and archived screens. No reliance on the lane's previous review verdict. All shell calls used `ulimit -v 4000000` and timeouts ≤1800 s; at most two compute jobs ran concurrently.

## Per-claim findings

| Claim | Classification | Independent finding |
|---|---|---|
| Full N_II: only odd non-square zero ≤10¹⁰ is 4545 | CORRECT / CERTIFIED | Recompiled current engine and reran all three intervals through 10¹⁰. Every record, histogram, count and witness maximum agrees after normalizing changed header labels. Independent progression sieve through 10⁸ also finds exactly {4545}. |
| No odd prime zero ≤10¹⁰ | CORRECT / CERTIFIED | Follows from the stronger non-square census and compositeness of 4545; does not depend on correctness of primality flags. |
| Numerator 8 / d-even zeros ≤10⁹ | CORRECT / CERTIFIED | Reran all three archived intervals: exactly 129 non-square zeros, 22 prime / 107 composite, last prime 35569, last composite 1239315. Independent sieve through 10⁸ matches the entire list. |
| d-odd zeros ≤10⁹ | CORRECT / CERTIFIED | Full rerun and independent sieve through 10⁸ match {13,301,445,685,1981,3105,4545,9121}; all six archived late witnesses verify. |
| Coprime census ≤10⁸ | CORRECT / CERTIFIED | Rerun matches 142 zeros, all 1 mod 4, last 21754425; 137 divisible by 3 and the remaining five divisible by 5. This is bounded evidence, not a proof of CONV-II-15. |
| F4: 14 + 38 + 12 prime entries | CORRECT / CERTIFIED | Fresh explicit witness construction succeeds at every entry. Maximum least f: 239, 239, 295 respectively. These are screen-entry counts, not a claim of 64 distinct primes. |
| F2: numerator-8 witnesses at 12 R8 zeros | CORRECT / CERTIFIED | Independent K=8 construction succeeds at all 12, maximum least f=1311. The obstruction of its c=1 sub-line does not transfer to the full family at these primes. |
| F3: 285 composite screen entries | CORRECT / CERTIFIED | Independent construction supplies witnesses for all 284 other than 4545; maximum least f=1319. Exact enumeration proves the exception has none. |
| Lemma 4.1: numerator nesting | CORRECT | d↦kd preserves the equation and has integral inverse precisely on k-divisible d. No coprimality assertion is smuggled in. |
| Lemma 4.2: scaling bijections / lifting | CORRECT | Both substitutions and inverses preserve positivity, integrality and the equation on exactly the stated divisibility domains. The non-coprime iff lifted statement also holds; details below. |
| Lemma 4.3: Jacobi obstruction / twisted T1 | CORRECT | Re-derived from reciprocity, including the gcd conditions. Odd divisors s of K/4 need not be squarefree. This proves inclusion of an infinite obstruction family, not exhaustion. |
| Lemma 4.4: trivial class and S3 necessity | CORRECT | All three divisibility-to-witness constructions work, including positivity of b. The coprime n=3 mod 4 construction is valid. Squares and 4545 satisfy S3. |
| S3 sieve upper bound | CORRECT as stated | For primes ℓ=3 mod 4 other than 3, the three forbidden roots are distinct; dimension is 3/2. Only an upper bound follows, not a lower bound or pointwise positivity. |
| Prior prime genus nonprincipality | CORRECT in quoted scope | χ_u has a nontrivial p-component and ψ* has conductor dividing 4u with p∤u, so twisting cannot remove it. For n=4545,u=505 the component disappears: −nu=−1515². The full prior analytic Theorem G is not re-certified here or needed for the census verdict. |
| K=12–24 auxiliary ladder censuses | PARTIALLY CHECKED | All stored LATE identities and P/C flags checked, but no fresh full-range negative census for these K. The prime/square-twist argument is valid. Their published zero totals remain dependent on the audited lane engine and archived runs. |
| Count samples / fitted numerical model | CORRECT as descriptive output | Refit reproduces `ladder2.txt` byte-for-byte. Independently counted the first/middle/last prime of each sample, all six K, including c=1 counts: exact agreement. Not a full recount of both samples. |
| “bin-by-bin within factor about 2–3” on 𝔐 | CORRECT-WITH-FIX | False literally: K=8 decade 4 is 1/0.25≈4; K=12 decade 5 is 7/1.46≈4.8. Zero observations admit no finite multiplicative agreement statement. |
| K=4 extrapolation beyond fitted x-range | CORRECT-WITH-FIX | Fitted maximum x≈107.7; K=4 decade 5 has x≈103.0 and is still inside. Decades 6–7, not every value beyond 10⁵, exceed the range. |
| HOT TARGET / strengthened verdict | ACCEPT | Explicitly statement-level, bounded-range and prior-target language; mechanism is inconclusive and B2 unchanged. It is not a mechanism-level HOT LEAD, proof of eventual positivity, or proof of ES. |

## Proof audit

1. **Nesting and scaling.** For N=nk, (a,b,c,d)↦(a,b,kc,d/k) sends N-solutions with k|d to n-solutions with k|c; its displayed inverse is exact. Dividing the equation by k gives the second map (a/k,b/k,c,kd), inverse (ka,kb,c,d/k). Independently enumerated full solution sets verify both equalities and numerator nesting for n∈{5,9,15,21,45,101,505}, k=1,…,11.
2. **Non-coprime lifting.** With f=4acd−1, a and c are units modulo f; bf=cn+a implies gcd(n,f)=1. If ℓ|N and ℓ|a, reduction modulo ℓ forces ℓ|b; likewise with a,b interchanged. Thus every common factor of abd and N triggers one inverse scaling. Conversely both lift types introduce a common ℓ-factor in abd. Positivity without a divisibility hypothesis does not inherit: 5→4545 is a genuine counterexample.
3. **Twisted T1.** If f=−1 mod 4t, write t=2^v t₀. The factor (2/f)=1 when v>0; reciprocity for t₀ cancels the two signs since f=−1 mod t₀ and f=3 mod 4. Hence (t/f)=1. Apply with t=(K/4)ac and K/4, divide their Jacobi symbols to obtain (ac/f)=1. Since −n=a/c mod f is a unit, (n/f)=−1. For n=sm², s odd dividing K/4, (s/f)=1, while gcd(m,f)=1 is forced by the same unit identity. Contradiction. This also proves all ordinary odd squares are zeros.
4. **Necessary condition.** A prime ℓ=3 mod 4 dividing (n+1)/2, n+4, or 4n+1 supplies respectively (a,c)=(1,1), (a,d)=(1,1), or (c,d)=(1,1), with remaining parameter (ℓ+1)/4. The given numerator for b is positive and divisible by ℓ. If n=1 mod 4 these three forms are odd, so absence of such primes means every factor is 1 mod 4. Their congruences give n=−1,−4,−1/4 and hence a nonzero quadratic residue. For squares, the displayed coprime sums of two squares prohibit any 3 mod 4 prime factor. For 4545, 2273,4549,18181 independently test prime and 1 mod 4.
5. **Other elementary claims.** The reciprocal identity follows by a common denominator abcd n; at primes non-coprimality would give 4 as a sum of three positive unit fractions, impossible. If K>n+2, then a+b+nc≤(n+2)abcd<Kabcd. The complete-modulus examples 3,7,15 and the missing K=8 targets check directly. The ES implication remains conditional on the cited Mordell/Salez reduction, not a new result here.

## Census trust boundary and independent computation

The archived engine uses f=Kacd−1 and the exact target congruence −n=a/c mod f. Enumerating ac|(f+1)/K exhausts every witness at each scanned f. In coprime mode gcd(a,n)=gcd(d,n)=1 suffices: gcd(f,n)=1 then implies gcd(b,n)=1. The d-odd filter is applied both in the bitmap and fallback.

For the exact fallback, put e=(a+b)/c and q=Kab. Sorting a≤b loses no solution. Necessarily (Ka−1)b≤n+a and Ka²≤n+2a. Since q>a+b, there is at most one positive e≤a+b congruent to −n modulo q; when the residue is zero there is no candidate. Testing e|(a+b) and setting d=(n+e)/q is therefore exhaustive, not a witness-cutoff heuristic. This re-derives the bounds used by both implementations.

I inspected arithmetic and range handling at 10¹⁰: LP64 counters hold 4.5 billion tests, products in the actual loops fit 64 bits, the segmented prime sieve starts at max(q²,ceil(s/q)q), and corrected integer-square checks are safe at this scale. Half-open interval endpoints 10⁸,10⁹,10¹⁰ are even, so they lose no odd boundary case. The omitted n=1 is covered by T1. This is not an audit of arbitrary near-2⁶⁴ CLI inputs.

The independent C implementation instead eliminates b: **n≡−4a²d mod (4acd−1)**. It enumerates every acd=m with f≤40000 and marks arithmetic progressions directly in a 50 MB parity-flag array; no modular inverses, target bitmaps, primality sieve, or lane code are reused. Residual non-squares receive an independently written exhaustive symmetric fallback. Through 10⁸ it finds 4999 odd squares (n≥3), one full zero, eight d-odd zeros, and 129 d-even zeros. Every zero list matches, not just its size.

The original K=4 runs through 10¹⁰ reproduce the exceptional late n=302812197 with (a,b,c,d)=(1,2,1,37851525), and no unresolved non-square in [10⁹,10¹⁰). Independently checked **267527 archived LATE witnesses** and **281782 total LATE/ZERO P/C flags** across all K files. Fresh screen witnesses use the progression identity and verify Kabcd=a+b+nc explicitly. Screen inputs are the committed lists; their original (★), 𝔊*, R8 zero classifications were not re-proved here.

## Model and required fixes, in priority order

1. Replace “bin-by-bin within a factor of about 2–3” by “most positive-count bins are within a few-fold; worst observed/fit ratio is about 4.8; zero bins are included in the deviance.” Keep deviance 65.5/23 and the poor-fit warning. Neither fitted model is validated for pointwise use.
2. Replace “K=4 values beyond 10⁵ lie outside” by “the decade-6 and decade-7 K=4 predictions lie outside the fitted x-range”; decade 5 remains inside.
3. Desirable clarification, not a census blocker: 0 observed against a fitted mean 0.00964 is extremely weak compatibility (Poisson zero probability ≈0.9904). Nested numerators share primes/events, so a literal independent-Poisson significance interpretation of the nominal df is not justified. The memo currently does not claim such significance.

The P1 fit reproduces A=−0.180, B=0.2498, deviance 408.6/33, K4 expected total 5.37. P2 reproduces A=0.416, B=0.3148, deviance 65.5/23, K4 expected total 0.00964. The samples match their populations, and zero bins are included; the superseded selected-bin fit is correctly excluded. The ≈3000–4500 solution extrapolation at 10¹⁷ is arithmetic under an unvalidated mean model, not certification.

## Reproduction artifacts

Committed reviewers: `scripts/z58_xrev_wildcard_independent.c` and `scripts/z58_xrev_wildcard_check.py`. Extract the reviewed branch's lane files and screens into `/tmp/xrev_WILDCARD`; compile the census and independent C programs with `gcc -O2 -Wall -Wextra` (`-lm`). Run the memo's K4/K8/d-odd/coprime census commands into `rerun_<suffix>.txt` there, then the independent binary with `100000000 40000 > independent.txt`. Under `ulimit -v 4000000`, use `timeout 1800` for each run and `timeout 600 uv run python scripts/z58_xrev_wildcard_check.py /tmp/xrev_WILDCARD`. Run the archived `z58_wildcard_ladder2.py` from the extraction directory and compare to `ladder2.txt`. Temporary raw outputs are not committed, per lane instructions.

**Bottom line:** accept the census, elementary lemmas and honestly scoped target selection; fix the two model sentences before copying them downstream. No theorem about all primes, eventual zeros, or a new mechanism is established.
