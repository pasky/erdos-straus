# z59 cross-model hostile review — CONV2

Reviewed `side-agent/z59-conv2` at `6dbcc6c2325d3ea6a03928fe7855742466265439`.
**Verdict: ACCEPT-WITH-FIXES.** The census, modulus lemma, and algebraic propositions survive. Three overbroad prose conclusions need correction before integration. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent derivation / check |
|---|---|---|
| Lemma 1(i)–(iii), piecewise modulus | CORRECT | `(Ta−1)(Tb−1)=Tn+1` for `T=4d`; conversely both factors are −1 mod T and yield positive coordinates. For a=1, `b(4cd−1)=cn+1`. When 4 divides T, the modulus-4T event implies the modulus-T event; otherwise only the a=1 branch occurs. No omitted T=1,2,3 case. |
| Lemma 1(iv), shift profile | CORRECT | c=1 gives `4ad−1 | n+a`; a=1 gives `4cd−1 | n+4d`, since multiplication by 4d is invertible modulo f. Thus the same piecewise profile applies, but its two branches exchange roles. |
| Lemma 1(v), full profile | CORRECT | Put `m=c²d`; every admissible c divides `r(m)=∏q^floor(v_q(m)/2)`. Hence `4m/r(m)` divides every `4m/c`. Conversely choose c=r(m), d=m/c², a=(f+1)/(4cd); invert 4cd modulo f to obtain positive integral b. The shift version interchanges the roles of a and c. |
| Lemma 1(vi), target sets | CORRECT | `−n=a/c mod f`, with `acd=m_f`; `1/c=4(m_f/c) mod f`. Setting c=1, a=1, or d=1 gives exactly the stated sets; the full set is `{4a²d: ad divides m_f}`. |
| Lemma 1(vii)–(viii) | CORRECT | The n=3 mod 4 quadruple substitutes directly. For a=1, e divides b+1 and `4bd=n+e`, with `0<e≤b+1<4b`; hence e is the unique nonzero residue −n mod 4b and `4b≤(4n+4)/3`. For c=1, D=4ad−1 and r=a; `D≤(4n+1)/3` follows from `n≥D−a≥3a−1`. The slightly larger unified bound cannot add spurious solutions because r reconstructs the coordinates. |
| Proposition 2.1(a)–(c) | CORRECT | `L²=16c²d²=4d(4m)`, so L≥2√(4m), equality exactly d=1. Multiplication of `f | cn+a` by c gives `f | c²n+u`, u=ac; c runs over divisors of u, with endpoints c=1,u for U. These integers are distinct for n>0. The profile collapse follows from Lemma 1(v). |
| Proposition 2.2, local coverage | CORRECT | Direct enumeration gives U targets `{1}`, `{1,2,4}`, `{1,2,4,8}` at f=3,7,15, precisely the negatives of Jacobi nonresidues. The c=1 targets miss a class at 7,15 and have only two of five classes at 11. Coprimality is correctly required. |
| Proposition 3.1, formal statements | CORRECT | For T=4C, `4C(n+4d)=4Cn+16Cd=4Cn+1 mod f`, f=16Cd−1; this proves the displayed bijection and its inverse. The two directional rescue restrictions, 4∤T and 4∤y respectively, follow. |
| §3 fixed finite menus; common factors | CORRECT | At p=1 mod f, a selected event would require f dividing T+1. If 4 divides T, f=T−1 or f≥2T−1, neither possible; otherwise f≥4T−1>T+1. Dirichlet applies to the unit class 1 mod `840∏f`. Also a common divisor of Tp+1 and T′p+1 is coprime to p, so divides T−T′. No growing-menu or general-dependence conclusion follows. |
| Proposition 4.1 | CORRECT | Coefficient comparison forces `K′=Kλλ_cλ_d`, `n′=pλ_c/λ`. Every image solution has p∤abd: otherwise all three ES denominators are divisible by p, giving a sum of three unit fractions equal to 4. If p∤n′, valuation gives `v(λ)=1+v(λ_c)`: positive v(λ) forces p dividing image a; nonpositive v(λ) forces `v(λ_d)=v(K′)−2v(λ)+1≥1`. Both contradict p∤abd. The k-divisibility bijection is exact; p∤c also follows from Jacobi reciprocity when f=−1 mod 4p. Scope is only the specified rational diagonal equation-scalings. |
| Proposition 4.2, divisibility and greatest event | CORRECT | c dividing c′ gives `4m/c′` dividing `4m/c`; all admissible c divide r(m), which is itself admissible. The gcd bound follows as above. Both incomparable-event examples reproduce exactly. The additional no-complementarity prose does NOT follow; see fix 2. |
| §3 “Any rescue … uses an integer the first line does not use” | WRONG as worded | n=193, T=8 gives 1545=15·103. The c=1 event succeeds via 103=−1 mod 8, but no divisor is −1 mod 32. This integer is available to BOTH T-families, and a=1 fails globally at 193. See fix 1. |
| §6 “None of them proves positivity anywhere” | WRONG | Proposition 2.2 proves U(n)>0 on its local classes; e.g. n=5 has f=3. See fix 3. |
| CONJECTURE U and “sharper target” | CORRECT-WITH-FIXES to surrounding prose | U implies CONV-II after inserting the explicit full-family witness at 105. The witness family is smaller, not proved harder to analyze. `(MS)⇒(MS-U)⇒(MS-II)` is immediate. López's archived source, arXiv:2404.01508v3, Theorems 4/7 and Conjecture 1, explicitly supplies the two prime congruences. The odd-prime specialization is correctly credited. |
| Genus gain / correlations | CORRECT attribution, not new proof | Z57_BFII §5.3 states Theorem G for genus mass, not N_II. Z57_COMPLEMENT §4.3 contains 0.483–0.548; Z57_SYNTH gives about +0.29. These inherited analytic/statistical results were source-checked, not independently re-proved/re-fitted here, and cannot justify a universal no-mechanism claim. |

## Engine and exhaustive independent computation

The reviewed C engine's target bitmap is exact for its witness cutoff: every factorization acd=(f+1)/K is visited, c is invertible modulo f, and the marked target is a/c. Symmetry justifies capturing b=1 via a=1. Bit indexing and residue signs are correct.
The fallback is exhaustive: sort a≤b; put e=(a+b)/c. Since `0<e≤a+b<Kab`, e is the unique residue −n mod Kab. Necessary bounds are `Ka²≤n+2a` and `Kab≤n+a+b`; both loop exits are monotone. The residue/divisibility test reconstructs every solution before line filtering. No witness cutoff remains on a negative decision.
All integer products, inverses, counters, and sieve indices are safe on this 64-bit host at the archived limits. The segmented primality sieve starts at max(q²,ceil(s/q)q); its q²≥end stopping condition is correct. Primality does not filter the principal census.
The three intervals `[1,10⁹)`, `[10⁹,5·10⁹)`, `[5·10⁹,10¹⁰)` have no gaps. All endpoints other than 1 are even, so half-open versus ≤ makes no difference for odd n. n=1 is an excluded square. The n=3 mod 4 branch is covered for all sizes by Lemma 1(vii).

My `scripts/z59_xrev_conv2_direct.c` uses **direct solution progressions**, not witness targets or a fallback:
- c=1: order a≤b; odd n forces b=a+1+2j, yielding `n=Ka(a+1)d−2a−1 + 2(Kad−1)j`.
- a=1, c≥2: b=cj−1, j odd, yielding `n=K(c−1)d−1 + 2(Kcd−1)h`; c=1 is already in the first loop.
- Requiring each first term ≤N gives finite exhaustive bounds on a,c,d. Every mark is a positive-coordinate solution, and every odd solution in either line is represented. Storage is one byte per odd integer, with no dense products.

| Recalculation | Result |
|---|---|
| Independent K=4, all odd non-squares ≤10⁸ | Exactly `{105,4545}`; 7.70 s, about 51 MB RSS. |
| Independent K=4, all odd non-squares ≤10⁹ | Exactly `{105,4545}`; 104.82 s, about 490 MB RSS. All 15,811 odd squares, including 1, explicitly remain unmarked. |
| Original engine replay of ALL three intervals through 10¹⁰ | Every numerical line reproduces, including all ZERO/LATE records, totals and bitmap maxima; 9.37+32.01+42.88 s. Only difference: current engine adds `# A1CMASK=15`. This is reexecution, not a second algorithm above 10⁹. |
| Independent K=8, all odd non-squares ≤10⁸ | All 819 zeros agree individually with the archives; 3.73 s, about 51 MB RSS. Class 1: 547=45 primes+502 composites, last 3,869,153 / 89,530,945. Class 3: 272=16+256, last 1,226,891 / 93,398,595. |
| All archived LATE certificates | 11,366 K=4 and 215,858 K=8 checked independently: positive coordinates, equation, f, line membership and P/C labels; zero failures. K=8 total includes the separate prime-only file. |
| Small counts / masks | Independently reproduced c=1/a=1 zeros 99/35 at n=1 mod 4 ≤10⁵; engine full count 1. All seven 10⁷ mask counts reproduce: 2,6,9,18,24,66,63. |
| Existing validation reruns | Raw/T/shift forms agree through 1500; direct brute checks for both K=4,8, all three line masks, and FMAX=K−1/2000 pass through 20,000. |

## Mandatory falsifiers

| Screen | Finding |
|---|---|
| F1 squares | CORRECT. For odd ℓ dividing Tm²+1, m is invertible mod ℓ and −T is a square; the quadratic character of −T has conductor dividing L_T and takes −1 to −1. Every odd divisor lies in its kernel, excluding the witness class. The prime reciprocity paragraph correctly restricts p=1 mod 4. Direct enumerations detect no square hit, including K=8. |
| F2 numerator 8 / 12 high R₈-zeros | CORRECT. Independent total is 819=61 primes+758 composites. Separately factored the intervals n+a and counted c=1 solutions at ALL 12 supplied primes in [10¹⁰,1.1·10¹⁰]: every archived R/R₈ pair reproduces, with min R=12 and R₈=0. For K=8, f=7 has target {1}; f=15 has {1,2,8}, so neither is complete. No universal numerator-8 positivity claim survives. |
| F3 composites | CORRECT. Of 285 supplied zeros, 51 meet the complete-modulus test; among the other 234, 176 are divisible by 3 and 15 are coprime to 105. Independent U census rescues exactly 232 of those 234. Direct full-family enumeration gives two unordered solutions at 105, including (3,3,2,3), and none at 4545. |
| F4 prime zeros | CORRECT. Recomputed least rescue T=2 at 11 star-zero primes, T=5 at 83,449/8,813,281, T=6 at 102,001; reverse rescues T=8,44,8 at 193,2521,66529. Exactly the stated five primes have complete-modulus rescues. Independent c=1 counts at all 38 G*-zeros reproduce 24 positive and the 14 star zeros. The ≤10¹¹ prime-union claim is explicitly inherited from B1_LINE §2.1, not independently certified by this review. |

## Required fixes, in priority order

1. **Restrict the §3 rescue sentence to its coordinate system and direction.** Say: “A star-zero rescued by a=1 needs 4∤T in the T-system; an a=1-zero rescued by star needs 4∤y in the shift system.” Do not infer that every rescue uses an integer unavailable to the other family in an arbitrary/common coordinate system. The n=193 example above is an explicit counterexample.
2. **Replace the unqualified c-line no-complementarity claim**, including proposed FRONTIER §6 text. At m=36, c=2 and c=3 DO rescue one another on the same indexed integer: n=31 has E₃ but not E₂; n=461 has E₂ but not E₃. The correct result is only: “All admissible events are contained in the greatest event E_r(m), and their union equals it.” Nested pairs cannot exhibit both directions of rescue; incomparable pairs can. A greatest-event reparametrization is not a proof that cross-line effects are absent.
3. Replace “None of them proves positivity anywhere” by “None proves universal positivity beyond the established local covering classes.” Proposition 2.2 must not be erased by the summary.

After these fixes, “no pointwise mechanism **found**” and “narrowed **within the specified classes**” are honest assessments. Adaptive/growing families and non-diagonal transports remain open. The sharper target and finite census are supported; a universal impossibility theorem is not.

## Reproduction

Every computation used `ulimit -v 4000000` and `timeout ≤1800`; computations were serial (one compute process). Extract the reviewed branch's scripts/data into `/tmp/xrev_CONV2` as permitted by the brief. Compile the original engine there as `original` and the committed direct C script as `direct` with `gcc -O2 ... -lm`. In that temporary directory, produce:
- `direct 4 100000000` → `direct_K4_1e8.txt`; `direct 4 1000000000` → `direct_K4_1e9.txt`; `direct 8 100000000` → `direct_K8_1e8.txt`.
- `original 4 3 LO HI 20000 0 1` for (LO,HI)=(1,10⁹),(10⁹,5·10⁹),(5·10⁹,10¹⁰) → `replay_1e9.txt`, `replay_1e9_5e9.txt`, `replay_5e9_1e10.txt`.
- `direct 4 10000000 1 M` for M=14,6,12,10,4,8,2 → `mask_M.txt`; `direct 4 100000 0 15` → `a1_1e5.txt`; `direct 4 100000 1 0` → `c1_1e5.txt`.
- From the repo: `uv run --with sympy python scripts/z59_xrev_conv2_audit.py /tmp/xrev_CONV2 /tmp/xrev_CONV2` verifies certificates, replay equality, zero lists, masks, screens and counterexamples. Final output: `ALL CHECKS PASS`.
