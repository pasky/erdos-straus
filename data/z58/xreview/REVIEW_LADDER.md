# z58 hostile cross-model review — LADDER

**Verdict: ACCEPT-WITH-FIXES (one minor code-comment correction; no mathematical or census blocker).**
Reviewed `side-agent/z58-ladder` at `dfd30e0e4e4efd04db9b4858ce6bb0797be22300`, not its earlier pre-review version.
The main proofs survive; the revised **narrowed** verdict is justified. ES and (MS) remain OPEN.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| Lemma 1.1(a), congruence converses | CORRECT | Positive solutions and hits correspond; the pair positivity condition is retained. |
| Lemma 1.1(b), symmetric size cap | CORRECT | Exact constant is `(64/9)^(1/3)`; the integer cutoff is exhaustive. |
| Lemma 1.1(c), `n_p ≤ μ(p)` | CORRECT | Both d-forms and the pair form work at primes; composite pair forms require the stated caveat. |
| Prop. 1.2, SC(D) beyond Burgess | CORRECT | Necessary consequence on primes in 𝔐 only, not an all-prime improvement or a no-go theorem. |
| Cor. 1.3, bounded D impossible | CORRECT | Dirichlet supplies arbitrarily large square-mimicking primes in class 1 mod 840. |
| Fixed-D μ-tail density | CORRECT | PNT in APs applies after adjoining 840 to the finite modulus; no growing-D uniformity follows. |
| L2^𝔐(P) ⇒ MS(P) | CORRECT | Restriction to primes is immediate; finite evidence proves no eventual assertion. |
| Zero census through 10¹¹ | CORRECT as a one-engine high-range certificate | Source/exhaustiveness audited; low census rerun; 42,832 high-range inputs independently checked pointwise. |
| μ-tail counts and fit | CORRECT as counts / Assessment | Stored totals and fit reproduce; no theorem about extremes or maxima at 10¹⁷ follows. |
| `R^(1)=R`, monotone cap ladder | CORRECT | Unique least residue identifies each d-form solution; the d cutoff is part of the relaxed definition. |
| Lemma 3.1, square obstruction for all k | CORRECT | Radical support alone forces Jacobi symbol −1; even squares are excluded too. |
| k=2 removes tested failures | CORRECT | All 36 stored cap rows reproduce; every R² count independently recomputed. |
| §4 ladder logic; §5 multiplicative transfer | CORRECT | Elementary implication and injective solution map; no new L6⇒L5 or L5⇒L4 claim. |
| `mdec.c` twelve-base MR comment | CORRECT-WITH-FIX | Implemented classifier is deterministic on uint64; the comment's larger `3.3e24` bound is false. |
| Imported OMEGA13 lower bound | Correctly qualified citation | Source Thm 5.1 has exactly the quoted exponent, conditional on its named inputs; this review does not recertify that separate proof chain. |

## Proof re-derivation and exhaustiveness

1. Put `d=4uC−1`. Then `n+u=Bd`, and `1≤u≤(d+1)/4<d`, so `u=(−n mod d)` uniquely.
   Conversely `r≥1`, `r` dividing `(d+1)/4` reconstructs positive integral `u=r,C=(d+1)/(4r),B=(n+r)/d`.
   The pair condition reconstructs `C=(n+u+B)/(4uB)≥1`; swapping u,B covers the second d-form.
2. `uB≥u+B−1` gives `n≥3(u+B)−4`. The product of `4uC,4BC,4uB` is `4(n+u+B)²≤64(n+1)²/9`.
   Therefore at least one actual modulus is at most this cube root. Scanning every integer through its floor is sufficient.
   `capof` corrects its floating estimate using 128-bit comparisons `9m³≤64(n+1)²`; no floating decision survives.
3. For a d-hit, each prime factor of r has Jacobi symbol +1 modulo d: odd ℓ follows from `d≡−1 mod ℓ` and reciprocity;
   if ℓ=2 then d≡7 mod 8. Thus `(n/d)=(-r/d)=−1` and some odd prime ℓ dividing d has `(n/ℓ)=−1`.
   At p≡1 mod 4, reciprocity gives `(ℓ/p)=−1`, hence d≥ℓ≥n_p.
4. At a prime, `p≥3uB−1` ensures u,B<p, so gcd(u,B)=1; p odd forces u+B odd. Set s=u+B.
   The odd quadratic character χ with discriminant −4uB has `χ(s)=(-4uB/s)=((2u)²/s)=1`, hence χ(−s)=−1.
   Since p≡−s mod 4uB, `(uB/p)=−1` for p≡1 mod 4. A prime factor of uB (possibly 2) is a non-residue.
   This proves the pair lower bound without importing the quaternion argument. The composite counterexample in the memo is legitimate.
5. Combining 2–4 proves SC(D)'s consequence, not its converse. For bounded D(p) choose a constant K dominating it.
   Infinitely many primes `p≡1 mod (840·∏_{ℓ≤K}ℓ)` exceed any threshold; all primes ≤K, hence all positive integers ≤K,
   are quadratic residues modulo p. Thus n_p>K and μ(p)>K (including μ=∞). This proves Cor. 1.3 with its full quantifiers.
6. The same Jacobi calculation uses only `rad(r)` dividing `(d+1)/4`; it therefore works at every finite k and at ∞.
   A square with coprime d has symbol +1, contradiction. The k=1 cutoff follows from `n≥d−(d+1)/4`.
7. In `mdec`, m≡3 mod 4 tests every d-hit; m≡0 mod 4 factors q=m/4 and enumerates **all** its divisors, with no gcd filter.
   Consequently non-unit composite pair hits are not lost. At 10¹¹ the cap is 41,431,935, and the SPF array covers every q.
   The divisor/exponent storage is ample in this range; arithmetic fits its chosen widths. Integer square correction is exact.
   Each base plus the six sorted residues enumerates every member of 𝔐 once; all squares, and only squares, are omitted.
8. For fixed D, sufficiently large p automatically satisfies pair positivity, so membership in the finite hit union is periodic.
   PNT in APs gives the conditional density among 𝔐 primes. It gives neither an error uniform in D nor the extrapolated extreme-value law.
   The transfer `(u,B,C)↦(ku,kB,C/k)` when k divides C is injective and solves kn, but produces no prime-propagation theorem.

## Independent computations

Reproducer: `ulimit -v 4000000; timeout 1800 uv run scripts/z58_xrev_ladder_check.py /tmp/xrev_LADDER`.
The input directory is an archive of the reviewed lane's scripts/data; all subprocesses are serial, memory-limited, and timed out at ≤1800 s.
The final complete run passes. The independent engines use positive-solution progression sieving, segmented Eratosthenes, and direct triples—not the decider's SPF/residue search.

- Direct triple enumeration gives identical μ(n) for **every n=1,…,25,000**, including even inputs and squares; trial-division primality also agrees.
- `mdec 1000 20000000` is byte-identical to its stored output: nine prime and eighteen composite zeros, last 17,401,609.
- `mu 100000000 420000 11` is byte-identical to `mu_1e8_Y11.txt`, including the zero list and tail statistics.
- Three disjoint 2,000,000-integer windows yield **42,832** non-square 𝔐 inputs, every one positive and pointwise identical in μ and primality:

| Inclusive interval | Primes / composites | Prime tails >100,1000,10000 | Composite tails | Maximum composite μ (n) |
|---|---|---|---|---|
| 100,000,001–102,000,000 | 3,332 / 10,930 | 683,44,0 | 2509,177,4 | 19,175 (100,707,049) |
| 98,438,000,001–98,440,000,000 | 2,439 / 11,845 | 502,27,0 | 2751,199,5 | 2,054,919 (98,438,839,489) |
| 99,998,000,001–100,000,000,000 | 2,485 / 11,801 | 539,28,1 | 2721,178,2 | 26,159 (99,998,349,361) |

- All six stored large ranges are contiguous and have exit=0; the first includes 10⁸, harmless because that endpoint is outside 𝔐.
  Independently counting the six APs and subtracting unit squares gives **713,501,433** inputs, matching 128,491,751 primes + 585,009,682 composites.
  Summed prime tail numerators are **27,024,568 / 1,660,737 / 22,757**; composite numerators **135,443,883 / 9,232,800 / 145,119**.
  This is an audit plus independent slices, **not** a second full census of (10⁸,10¹¹]; the prime/composite split outside those slices remains the lane's deterministic-MR result.
- All 36 cap rows are byte-identical on rerun; direct modular squaring independently checks every R² count, including minimum 1 at 2641.
- Finite differences independently recover fit coefficients `−0.1415209269, 0.4178619844, −0.4821257423`.
  D*(10¹¹)=398,899.22; D*(10¹⁷)=14,291,379.49, exponent 0.4208867. The complete stored fit output, including crossovers, is byte-identical.

## Falsifier audit

| Screen | Result of attack |
|---|---|
| F1 odd squares | PASS as stated: d-form Jacobi obstruction survives every exponent cap. The memo correctly does not extend prime pair-form reciprocity to arbitrary composites. |
| F2 numerator 8 | All **12** supplied R₈ zeros independently recertified by a complete symmetric-modulus progression sieve; four lie in 𝔐. Exact C-even restriction and threshold caveats are correct. |
| F2 relaxed caps | Not screened out: independently found `(n,d,r,m)` = `(10301993881,1495,289,187)`, `(10529331121,239,60,30)`, `(10532106649,79,25,10)`, `(10868474401,2207,828,276)`, and `(409,63,32,8)`, each r dividing m². The memo honestly says unestablished. |
| F3 composites | Recounted 285 total, 15 inside 𝔐, 270 outside, 265 divisible by 3/5/7. Finite zeros do not refute eventual primality-blind positivity. No necessity of the domain 𝔐 is established or now claimed. |
| F4 primes | Nine of the fourteen full-family zeros are in-domain. All 38 𝔊*-zeros checked: exactly fourteen are also full-family zeros; the other 24 have hits. Subfamily zeros give no additional obstruction to these full-family statements. |

For the independent R₈ sieve, `min(8uC−1,8BC−1,8uB)³≤512(n+1)²/49`; integer ceiling cube roots make the no-hit decisions exhaustive.
No “HOT LEAD” or “survives all four” promotion is warranted. The memo does not make one.

## Required fixes, in priority order

1. **MINOR, documentation only:** `scripts/z58_ladder_mdec.c:isprime` says the first twelve prime bases are deterministic below 3.3·10²⁴.
   Counterexample: **318665857834031151167461 = 399165290221·798330580441** passes all twelve bases (independently checked).
   Replace the comment with “deterministic for uint64” or the strict bound 318665857834031151167461. The 3.3·10²⁴ bound needs thirteen bases.
   This cannot affect the ≤10¹³ supported inputs, the ≤10¹¹ census, or any theorem. No numerical rerun is needed for that comment correction.

## Sources and scope

- [McGown–Treviño, *The least quadratic non-residue*](https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf), especially §7, verifies the Burgess scale and the conditional Bach bound; [Tao's derivation](https://terrytao.wordpress.com/2009/08/18/the-least-quadratic-nonresidue-and-the-square-root-barrier/) also gives the exponent 1/(4√e)+ε. Both were opened. The memo's current fixed-residue-class priority statement remains an Assessment, not an exhaustively verified literature theorem.
- [Sorenson–Webster, Theorem 1.1](https://arxiv.org/html/1509.00864v1#S1), opened, gives the exact twelve-/thirteen-base thresholds above.
- The internal review's former major objections are repaired in this revision. Preserve “one engine”, fixed-D versus growing-D, restricted-domain beyond-Burgess, and model-versus-bound qualifications in any FRONTIER export.
