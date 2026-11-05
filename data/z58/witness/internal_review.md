# Hostile internal review — Z58_WITNESS.md

**Verdict: REJECT as written.** Lemma 1.1 and the bounded-coordinate exclusion in Proposition 3.1 survive review, and nearly all the numerical census claims reproduce. However, the stated W does not imply (MS), its falsifier table does not respect its hypothesis, the claimed PROVED escape from the least-nonresidue barrier is not proved, and one CERTIFIED statistic uses the wrong least nonresidue. These are repairable defects, not evidence against ES. **ES remains open.**

Locations below refer to the reviewed 254-line version of `Z58_WITNESS.md`. No memo, script, or other repository file was changed.

## Findings

1. **MAJOR — W assumes positivity instead of implying it.** **Location:** §5, lines 163–166; W's falsifier table, lines 182–185; §6, lines 206–226.

   W quantifies only over primes **with R(p) ≥ 1**. It says that existing solutions admit a small coordinate; it says nothing at any prime with R(p)=0. Thus it cannot supply the missing positivity in (MS). “W ⟹ (MS) on its domain” merely repeats the domain restriction and does not give an implication on the actual (MS) domain. “Strictly stronger” is consequently unjustified. In particular, W as written is not falsified by the 14 prime zeros: they are excluded by its hypothesis. Squares and composites are outside its prime domain as well; extending the positivity-conditional formulation to them still excludes their zeros.

   **Fix:** distinguish `W_size: R(p)>0 ⇒ s(p)≤log²p` from an existence conjecture, e.g. `W_positive: every prime p≡1 (4), p>8,813,281, has a solution with min(u,B,C)≤log²p`. The latter genuinely implies (MS). State which conjecture each screen tests, and preserve the distinction in the FRONTIER export. Define s(p)=∞ at R(p)=0 if inequalities involving s are to include zeros. Proposition 3.1 proves absence of small-coordinate solutions, not that its infinitely many constructed primes have R(p)>0; its examples do have solutions, but Dickson alone does not establish that additional assertion.

2. **MAJOR — the “PROVED” escape from the n_p barrier is not a proved non-implication.** **Location:** §1, lines 40–42; §5, lines 169–171 and 182; §6, lines 206–233.

   Lemma 1.1 gives lower bounds on products/moduli. It does not prove that W has no further implications for n_p. A small coordinate need not make a modulus comparably small, so the lemma supplies no *direct polylogarithmic* n_p bound from W. That is weaker than “W implies no bound,” “free of,” or “immune to” the barrier. Also, the cited SPARKS9 proposition supplies a BM-negative divisor at C≤ℓ(p), not necessarily at C≤log²p. Its proof does not make the first half of the **polylog-menu** problem free unless the required bound on ℓ(p), or another argument, is available.

   **Fix:** replace the PROVED non-implication with: “The direct modulus-size consequence of Lemma 1.1 does not apply to a bound on the least coordinate; no improved least-nonresidue bound from W is known here.” Explicitly distinguish the unconditional C≤ℓ(p) BM relaxation from a relaxation inside W's menu. “GRH-strength” should mean a polylogarithmic least-nonresidue consequence on the stated domain, not an equivalence to GRH.

3. **MAJOR — a prime factor in the target residue class is not necessary.** **Location:** §0 F1, line 12, final sentence.

   A qualifying **divisor** can be composite, with no prime factor in its target class. Concrete counterexample inside 𝔐: p=4561 is prime, p mod 840=361, and (u,B,C)=(2,117,5) is a solution. Here d=39≡−1 (mod 8), while p+u=4563=3³·13². Neither prime factor is −1 mod 8. The nonresidue factor 13 carries the Jacobi sign but is not in the target class.

   **Fix:** require “a divisor d≡−1 (mod 4u), whose factorization necessarily contains a nonresidue prime.” Do not replace the divisor-in-class problem by the stronger prime-factor-in-class problem. Likewise, a proof must respect the Jacobi obstruction; it need not contain an explicit intermediate Jacobi-sign construction rather than an indirect counting argument.

4. **MAJOR — rooting counts use the least odd nonresidue, not n_p.** **Location:** §3, lines 105–107; §4, line 150; `scripts/z58_witness_loc.py`, function `n_p`.

   The function unconditionally skips 2. The hard sample includes primes p≡5 (8), where n_p=2. The discrepancy changes the claimed prime-level counts at p=27,034,597, whose listed unordered solutions are (1,2,3,379,325) and (2,380,769,9). Both pair products are even; hence both are rooted at n_p=2. The script instead uses 5 and reports no root.

   Independently recomputed correct counts are **46/103**, not 45/103, and **18/45**, not 17/45. The control count remains 338/341. The failure count in §4 is **57/103**, not 58/103. The qualitative “misses most hard primes” conclusion survives.

   **Fix:** handle 2 in `n_p` (return 2 for p≡5 mod 8 on this prime domain), regenerate rooting statistics, and update all affected counts. Alternatively, consistently rename this statistic “least odd nonresidue,” but do not identify it with n_p outside p≡1 (8).

5. **MAJOR — finite records do not kill arbitrary polylogarithmic rules.** **Location:** §1, line 42; §2, line 54; §5, lines 169–171; §6, lines 196–198, 218–219, 231–232.

   Records such as d_min≈p/29 at one finite p do not establish a polynomial asymptotic tail or rule out O((log p)^A) for unspecified A and constant. A least-nonresidue consequence is a formidable open target, not an impossibility theorem. Similarly, the finite data do not show that every “small-u” or “small-C” rule fails; a quantitative bound and domain must be specified. Proposition 3.1 addresses fixed coordinate cutoffs conditionally, not arbitrary growing cutoffs.

   **Fix:** say “large finite-range records” or “records of the displayed polynomial scale,” and identify the specific refuted bounds (for example, unit-coefficient log²p bounds in the individual orderings). Keep the general polylogarithmic modulus target open, while recording its least-nonresidue consequence. Replace “dead on data” and “only ordering not dead” accordingly.

6. **MAJOR — the heuristic support extrapolates beyond what either calculation supplies.** **Location:** Proposition 3.1 scope, lines 128–129; §5, lines 172–177.

   If a uniform probabilistic upper bound P(s(p)>S)≲p^(−κ log(S+1)) were valid, the prime sum would indeed converge when κ log(S+1)>1, and exp(1/0.17)=358.652 is correctly approximated by 360. But the moderate-U, three-decade fit is not such a bound. The semi-local script also conditions on R>0 and uses the geometric decade midpoint, not an individual-p probability law. A summable extrapolation for the entire population would conflict with Dickson's infinitely many fixed-S avoiders. Introducing a distinct “bulk” population needs an explicit qualification/model, not an inference that this fit controls all but finitely many primes.

   More importantly, Proposition 3.1 only forces s>S (or no solution), not s≍S: it gives no upper bound at all. Dickson is a fixed-tuple conjecture; the expressions with 2log²X forms ignore the changing progression L_S, singular series, and uniformity in S. They do not establish a rare tail of precisely log p/log log p scale, much less bound all other tails.

   **Fix:** label the summation as a deliberately nonuniform extrapolation, not a consequence about actual exceptional primes. Replace “Dickson-type primes add a tail with s≍…” by “a further unproved variable-S heuristic suggests obstructions at least on this scale; neither their sizes nor an upper tail are controlled.” Conclude only that these observations do not presently furnish a counterexample to W, not that every relevant tail stays below log²p.

7. **MINOR — the fixed-D limit is valid, but the stated proof of a proper limit law is incomplete.** **Location:** §2, lines 50–53; §2.1, lines 70–76; exported line 220.

   For fixed D, the avoider event is periodic modulo lcm(840,{d≤D:d≡3 mod 4}); prime equidistribution in reduced residue classes gives the asserted limiting CRT density. Cite the prime number theorem in arithmetic progressions for ordinary counting proportions, rather than Dirichlet's infinitude theorem alone. Fixed-D convergence does not by itself show tightness, convergence of the mean log d_min, or the fitted survival law for growing D.

   A short repair proves tightness: restrict to prime moduli ℓ≡3 (4), ℓ∤840, for which −1∈H_ℓ. CRT gives δ_𝔐(D)≤∏(1−1/(ℓ−1)) over those ℓ≤D; divergence of their reciprocal sum makes this product tend to zero. This establishes a proper finite-valued limiting distribution, but not convergence of its logarithmic mean.

   **Fix:** add this argument (or state only the fixed-cutoff result), cite the appropriate prime-distribution theorem, and keep the finite-range fit separate from the limiting density and moment claims.

8. **MINOR — other F1 arguments need precise hypotheses.** **Location:** §0 F1, line 12; §5 F1, line 182; §4, lines 145–148.

   Being a square mod 840 does not make an arbitrary p a square mod an arbitrary fixed M, and an output divisor need not divide M. Thus the displayed “trivial” proof of the fixed-congruence obstruction is not valid as written. The conclusion for a rule selecting a fixed d or fixed (u,C) from p mod M is repairable: consider input residue 1 mod M, let d be its fixed output modulus, and take primes p≡1 modulo lcm(M,840,d). Such primes exist by Dirichlet and cannot lie in H_d.

   “Every divisor d of m²+u has (−u/d)=1” is false: for m=3,u=3,d=3 the symbol is 0, and even divisors do not have an ordinary Jacobi denominator. For odd d coprime to m the symbol is +1; target divisors automatically satisfy the required coprimality. The 4Cm²+1 statement is correct.

   Finally, nontrivial two-square representations do occur at squares: 25=3²+4². The count of representable composite zeros refutes existence of a representation as a sufficient criterion, not every use of representation data. “Only uniqueness could separate primes” is not an exhaustive conclusion from the tests.

   **Fix:** use the repaired CRT argument, restrict the Jacobi identity to eligible odd coprime divisors, and say the tests find no useful relation of the specific forms tested. Do not advertise two-square existence as inherently square-killing.

9. **MINOR — F4 miscounts which 𝔊* zeros have witnesses.** **Location:** §0 F4, line 15; §5 F4, line 185.

   The 38 𝔊* zeros include all 14 (★) zeros. Only **24** have witnesses and finite s(p). The final table at line 212 already gets this right. “At the 38 … witnesses exist” and “at the 38 … s(p) is small” are false.

   **Fix:** write “at the 24 𝔊* zeros with R(p)>0” in both places. Resolve the threshold statements together with Finding 1: the existing positivity-conditional W needs no exclusion threshold for R=0 inputs, whereas the stronger existence version does.

10. **MINOR — statistical agreement is promoted to a mechanism/joint law.** **Location:** §2.1, lines 73–81; §3, lines 91–104; §6, lines 199–204.

    A larger zero-count probability than exp(−E) does not establish positive association of all firing events. Agreement of four minimum-coordinate probabilities with the simplex prediction does not establish the full joint uniform-simplex law. Near-unit variance/mean does not establish a Poisson distribution or independence of centre events. Centre solutions can share a u or a C; “centre solutions involve distinct integers” is not generally true. The quoted KS p-values reproduce, and their existing dependence caveat is appropriate, but the hard/control samples also have different size ranges (especially the ≥10⁶ sample) and different residue-class restrictions.

    **Fix:** use “consistent with clustering,” “minimum-coordinate distribution approximately matches,” and “centre counts have near-Poisson dispersion.” Present the boundary-empty/centre-lottery account as an interpretation, not an established causal mechanism. Treat the half-dimensional small-u law as a heuristic/fit unless an applicable asymptotic theorem is supplied. Do not imply the nominal CF “≈2σ” comparison accounts for within-prime dependence.

11. **NIT — numerical and definition-level corrections.** **Locations:** §2, line 51; §2.1, lines 75–76; §3, line 96; §4, lines 137 and 141–142; §6, line 200.

    From the exact survivor counts in `surv_1e8_1e9.txt`, −log S/log²D equals **0.0853484, 0.0870536, 0.0879633, 0.0869025** at D=1000,3162,10000,100000. The listed 0.0868 is wrong; use **0.0871**. With four decimal rounding the first value is **0.0853**, not 0.0854. The overall 0.087 empirical description remains reasonable.

    Non-𝔐 mean log d is 1.905 in the 10^7.5 bucket, so “1.906 throughout” should be “about 1.906.” The observed control central-solution fraction is **47.7%**, not the theoretical simplex value 49% used as a control description in §6. The CF code excludes X=1, whereas the memo does not state that restriction; add “X>1” for the CF test. Write the minus continuant as **4uCB−u−B**, or define c=4C. Say “two unordered solutions (four ordered triples)” at the record prime to match the definition of R.

    **Fix:** make these literal corrections; no change to the corresponding broad numerical conclusions is required.

12. **NIT — several advertised commands are not executable as written.** **Location:** §7, lines 240, 244–245; §3, line 87.

    `z58_witness_surv.py` parses its first arguments with `int`, so `1e8 1e9 3e6` raises ValueError. The loc and CF scripts likewise reject `1e6`/`1e7` as the integer PMIN. Also, `tri1e9_R6.txt` contains the 14 zero rows, not the claimed census summary line; that program prints its summary to stderr.

    **Fix:** use decimal integer arguments and say the retained tri output reproduces the zero *set*, or retain/cite its stderr summary. Mark schematic commands as pseudocode where appropriate.

## Proof audit: what passes

### Lemma 1.1

The proof is sound on its stated domain. For a prime solution, u,B≤(p+1)/3<p, gcd(u,B) divides p and hence equals 1, and u+B is odd. These facts justify application of the pair-character identity in `BM_CORRECTED_COUNT.md` Theorem 1.1. Its elementary proof is valid: −4uB≡(u−B)² modulo u+B, with gcd(u−B,u+B)=1, and the negative discriminant character is odd. Periodicity then gives χ_{−4uB}(p)=−1. For p≡1 (4), this is (−4uB/p)=(uB/p). For p≡1 (8), (2/p)=1, so an **odd** prime factor of uB has negative Legendre symbol. The two d-modulus assertions follow from Lemma A.1(b) and reciprocity exactly as stated.

Thus **q_min≥4n_p is correct**, as are the d_min and coordinate-product bounds. In fact uB is even, so the argument on this domain even yields q_min≥8n_p; the weaker printed bound is harmless. The proof does not justify the broader non-implication language discussed above.

### Proposition 3.1

Every exclusion step checks out. The asserted divisibilities of L_S give integral q_u and r_C and q_u≡1 mod 4u. Once q_u>u+1, its primality makes the divisors exactly g or gq_u with g|(u+1); none has residue −1 modulo 4u because u+1<4u−1, including u=1. The u-form is the correct consequence of Lemma A.1, and u↔B really does exclude B≤S.

For C, r_C≡1 mod 4C and r_C>4C+1 give divisors with residues of g|(4C+1). The only possible target g in the relevant size interval is 4C−1, which is coprime to 4C+1 and greater than 1. The divisor/level form therefore excludes C≤S. A sufficient explicit size condition is p>max((S+1)²,4S+2); in fact it is automatic for k≥1 since L_S≥4S(4S+1).

The 2S+1 forms are primitive, positive-slope, distinct linear forms. Their slopes divided by L_S are 1, 1/(u+1), and 4C/(4C+1); these are distinct. At k=0 every form is 1, proving admissibility. Dickson therefore supplies infinitely many positive k. The qualification about s at zeros and positivity is Finding 1, not a failure of the small-coordinate exclusion.

The raw d/u/C/pair equivalences and the Farey/SL₂ determinant identity also check out. The determinant is 1+4C(4uBC−u−B−p); its value 1 gives the claimed equation and Farey difference. The stated loose 1.93 p^(2/3) modulus bound is compatible with the elementary product bounds.

## Computational verification

All shell invocations used `ulimit -v 6000000` followed by `timeout` of at most 180 seconds. There were at most two concurrent compute jobs. Computations streamed data or used small bounded collections; no Cartesian-product arrays were built. Temporary compiled executables were used for the requested checks. The full 10⁹/10¹⁰ censuses were **not** rerun.

- Compiled `scripts/z58_witness_scan.c` with `gcc -O2 -o /tmp/rv_scan … -lm` and fed every prime in column 4 of `dickson.txt`. Columns 8 and 10 give:

  | S | p | u_min | C_min | s |
  |---|---:|---:|---:|---:|
  | 1 | 9,241 | 2 | 5 | 2 |
  | 1 | 15,121 | 2 | 9 | 2 |
  | 1 | 51,241 | 2 | 2 | 2 |
  | 2 | 1,202,041 | 6 | 6 | 6 |
  | 2 | 1,564,921 | 6 | 4 | 4 |
  | 2 | 2,532,601 | 4 | 6 | 4 |
  | 3 | 94,807,441 | 11 | 11 | 11 |
  | 3 | 2,682,912,961 | 8 | 6 | 6 |
  | 3 | 26,678,957,761 | 5 | 4 | 4 |

- Independently recomputed each L_S and used SymPy to verify **all** 2S+1 forms for **all nine** listed instances, including all S=2 and S=3 examples. All are prime. Re-ran `z58_witness_dickson.py 4 3000000`: the entire stored output reproduces, including L₄=1,113,840 and no S=4 example in that k range.
- Independent Python brute force over all u≤(p+1)/3 and all C with 4uC−1≤p+u exactly matches the complete listed solutions for p=1,021,441; 1,095,481; 1,201,201; 1,336,729; 1,952,449. Their ordered R values are respectively 2,4,4,4,4.
- Reproduced the claimed four-ordering validation for **all 1,125 primes p≡1 (4)≤20,000**, using an independent symmetry-bounded u,C brute force: zero mismatches. Also compared the compiled solution enumerator against independent brute force for **all 3,000 odd n≤6000**: zero mismatches.
- For p=413,490,001, the compiled solution enumerator returns the two stored unordered triples. Independently enumerating divisors of p+u for every u≤10,167, the exact bound from 4u²−2u≤p with u≤B, returns exactly **(241,2134,201)** and **(458,1101,205)**. Therefore **s=201 is complete**, not merely an upper bound. The ratios are s/log²p=0.5106301127, s/log p=10.13097491, and m3/p^(2/3)=0.3491088368.
- Re-ran all **87 distinct primes** appearing in `agg1e9_records.txt`: all 15 scan columns match every stored record row. Small-range enumeration and the streamed hard file reproduce the full s-record sequence 1,2,3,5,11,16,18,36,44,67,201. The last two record primes are 42,691,489 and 413,490,001.
- Summary bucket counts sum to **25,423,491** primes and **14** zeros. The retained hard file gives exactly the 14 stated zero primes. The tri file contains the same 14 R=0 rows and **270** primes with 1≤R≤4. The six Mordell mean-log-d values match. The least-nonresidue equality percentage is **240,065/1,054,600=22.763607%**, correctly rounded to 22.8%.
- The twelve large-census DONE counts sum to **202,099,784**. The compressed tail has **21** distinct rows, **18** in 𝔐. Its maximum is **s=97 at p=1,708,503,889**, with u_min=97 and C_min=118, and max s/log²p=**0.2146301918**. Re-ran the u/C scan for **all 21** primes: every stored minimum matches. The “no zeros” statement is consistent with the retained totals: the runner counts only rows with both witnesses in DONE, and its total equals the asserted complete prime count. This is a finite computational claim, not a conclusion about primes beyond 10¹⁰. The archived summaries alone are not a replacement for independently rerunning that whole census.
- Streaming the hard file gives Mordell s>32 counts **1,2,11** in the three decades, yielding the displayed frequencies with the positive-R denominators 18,139; 158,955; 1,408,113. The 1.4·10⁻⁶ frequency above 10⁹ is consistent with 18 divided by the approximately 12.63 million Mordell primes predicted by the class proportion; an exact Mordell denominator is not retained in the DONE file, so that precision should not be called independently certified here.
- Survival probabilities at D=1000 are **833/51,111=1.630%** and **23,985/1,408,113=1.703%**. The large-range ratios −log S/E at D=1000,10000,100000 are **0.83750,0.76729,0.71100**. κ_u=0.124–0.135 at U=32–128, κ_C around 0.10, the reported κ_s fit, and the three u>1 frequencies agree with `semilocal_1e6_1e9.txt`; its normalization is log of the geometric decade midpoint. The 0.087 fit has the small corrections in Finding 11.
- Checked the identities and primality of all entries in the hard/control solution files. Hard subset sizes **103/188** and **45/82**, control size **341/8493**, C-even fractions **0.478723/0.439024/0.495114**, all displayed simplex minimum probabilities, and central-only prime counts **75/103** and **35/45** reproduce. Independent tied-CDF KS calculations give **4.12080·10⁻²¹** and **5.75587·10⁻¹¹**. Boundary mean/dispersion are **13.03226/3.25090**, centre **11.87390/1.16013**, boundary-empty fraction **1/341=0.00293255**; centre dispersion at t=0.15 is **1.08577**. Rooting is the substantive numerical exception in Finding 4.
- Re-ran the CF/two-square comparison: all six printed rows reproduce. The claimed percentages are correct for the script's **X>1 CF** and **X>2 divisibility** tests, subject to the interpretive limitations above.
- All 12 R₈-zero entries in `samples_scan.txt` have the claimed s split: **eleven with s=1**, and **p=10,532,106,649 with s=5**. Among the 24 solvable 𝔊* zeros, log(m3)/log p ranges from **0.156863 to 0.686649**, with median **0.434011**, matching the final table.
- Re-ran the scanner on all **285 composite zeros**: all four orderings return none, with the d search exhaustive for these inputs. Independent factorizations give least-prime-factor counts **214 at 3, 36 at 5, 15 at 7**, and maximum least factor **443 at n=897,961**. Exactly **57** are sums of two squares and **26** have all prime factors ≡1 mod 4, as claimed.

**Bottom line:** keep the lemma, the conditional finite-menu exclusion, and the verified data. Repair W's quantifiers before presenting it as an (MS) target; correct the rooting computation; and demote the asserted barrier immunity, asymptotic tail exclusions, and causal heuristics to their actual evidentiary scope.
