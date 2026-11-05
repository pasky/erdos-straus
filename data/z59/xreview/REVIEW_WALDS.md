# z59 cross-model hostile review — WALDS

**Verdict: ACCEPT-WITH-FIXES.** The Gaussian-twist filter survives independent derivation and source checking; “narrowed”, not “dead”, follows. The finite-sweep summaries conflate ambient spaces and contain false rank/count statements. These require correction before promotion. ES and (MS) remain OPEN.

Reviewed `side-agent/z59-walds` at `09adb6301789d22ca33d8d9879617907d0894247`, not an edited working copy. Independent implementation: `scripts/z59_xrev_walds_check.py`; PARI 2.17.2 through cypari2. All computations used `ulimit -v 4000000`, command timeouts ≤1800 seconds, at most two concurrent compute processes.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| W1(i), separation of square-orbit anchors | CORRECT | Finite Hecke decomposition, prime-power recurrence, and the finite-set Dedekind argument genuinely separate different eigensystems. All rough squares, not merely prime squares, are used. |
| W1(ii–iii), Gaussian-twist filter | CORRECT | Waldspurger Cor. 2 has the required local-square hypothesis and does **not** require (H2). The twist is `φ ⊗ ψχ_{−4}`, not generally `φ` or `φ ⊗ χ_p`. |
| W2 | CORRECT | Follows from W1; at n=1 the anchors already vanish. The classical/automorphic central normalisations have identical zero sets. |
| W1′, one line per eigensystem | CORRECT | The quadratic-form identity factors over C; the sign can depend on t but not on f. The nonzero-L anchor, or alternatively (H2), must remain attached to the conclusion. |
| W3, root numbers | CORRECT | For squarefree t in C1, t≡1 mod 8 and `(t/q)=1` at conductor primes, hence the quadratic-twist root-number multiplier is 1. Sign −1 gives coefficient vanishing only with the stated factorisation hypothesis. |
| W4(a–d) | CORRECT | (a),(d) use Cor. 2 without division by a possibly zero anchor L-value; (b),(c) require (H2) for every summand. Non-cancellation, not positivity of each L-value, controls a sum. |
| W5 | CORRECT | Take the maximum of the two eventual thresholds. This equivalence presupposes effectiveness and does not make every validity proof circular. |
| W0 | CORRECT relative to TERNARY F | A zero positive-weight genus average forces every class's representation number to vanish. Nonnegative mixtures and termwise recipe lattices follow. |
| “123 full-space runs; 121 match” | WRONG as written | There are 123 recorded comparisons: **118 full-space + 5 cusp-space**, covering **121 distinct (L,D)** pairs at 24 levels. The match count itself is 121/123, but its ambient-space description is wrong. |
| “15 nonzero kernels, all rank 1” | WRONG as an unqualified full-space finite statement | At `(840,105)` and `(840,840)`, B=8000, the full-space restricted kernels have rank **5**. Replacing these by rank-1 cusp-space runs is not merely increasing B. |
| Every valid proxy vanishes on C1∩[1,B] | CORRECT-WITH-FIX | Finite rank-zero certificates imply this without saturation. The lane's saved certificates rely on cusp space for **five** characters at L=840, not three; see the repaired scope below. |
| Gauss-exceptional rational identification/completeness | EVIDENCE, honestly labelled | Few Hecke eigenvalues and a bounded curve search do not certify the full eigensystem span, irrational components, or stabilisation beyond B. |
| 57/238 and 54/238 coefficient zeros | CORRECT | Both independently reproduced. The conversion of all coefficient zeros into L-zeros remains CONDITIONAL on identification and an L-nonzero anchor. |
| 13 unconditional L-zeros | CORRECT-WITH-FIX | All 13 rank lower bounds reproduced; **six**, not 13, are in M. The body states this correctly; the introduction/FRONTIER compression does not. |
| CKRS-based eventual failure | CONJECTURE, honestly labelled | The source states a prime-twist conjecture, not a theorem or a prescribed-class result. Positive-constant residue-class refinement and rational G are additional restrictions explicitly acknowledged. |
| “Narrowed”; no closure of E1/ES | CORRECT | Neither finite zeros nor invalid small-level lines exclude eventual effectiveness at other levels, multi-eigensystem cancellation, or the listed escapes. |

## Proof and source audit

1. For a good prime ℓ and ℓ∤m, Shimura's formula gives `b1=(λℓ−ψ(ℓ)(−1/ℓ))b0`; for j≥1 it gives `b(j+1)=λℓ*bj−ψ(ℓ)^2*ℓ*b(j−1)`. Thus the square coefficients are `a(1)Aφ(m)` with the displayed Euler factor. The middle Legendre symbol really vanishes in the second recurrence.
2. TERNARY F removes E on C1 and the t=1 unary contribution. A unary series with t>1 dividing N cannot contribute at m² when `(m,2N)=1`. Consequently T1* yields `Σ cφ Aφ(m)=0` on every rough integer m, including 1.
3. Distinct nonzero isotypic summands differ at infinitely many good primes: otherwise their “almost all primes” definitions coincide, contradicting directness. Subtracting the relation at ℓm eliminates one summand; enlarging the forbidden-prime set makes induction legitimate. Hence every cφ=0.
4. In Waldspurger's notation, k=3 and `χ0=ψχ_{−4}`. Apply Cor. 2 at (1,t), using t/1 a square at every prime dividing 4N: `a(t)^2 L(Gφ,1/2)=0`. This proves the filter without (H2), BSD, sign assumptions, or numerical L-values. Squarefree t>1 excludes every remaining unary support.
5. Applying that corollary at (t,t0) gives `x_t²=κ_t x_t0²` as an identity of polynomial functions on the eigenspace. The polynomial ring is a domain, proving W1′. Under (H2), the local factors of Theorem 1 are constant at bad primes on C1 and equal 1 at good primes for squarefree arguments, proving W4(b).

Sources independently inspected:
- [Waldspurger 1981 scan](https://mate.dm.uba.ar/~nsirolli/files/waldspurger.pdf), cached primary pages 376–379 and 484: unary complement, Prop. 1/2, χ0, (H2), Theorem 1, Cor. 2. The last proof paragraph explicitly removes (H2) in a fixed 2-adic square class. At k=3 his central L-value is classical `L(G,1)/π`, consistent with the memo.
- [Purkait, JTNB 26 (2014)](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.865.pdf), Theorem 2.1, p.237: explicitly reproduces Shimura 1973 Theorem 1.7 with the exact character and powers used here. The original Shimura JSTOR scan was inaccessible; **this formula was checked through its explicit published reproduction, not claimed as a fresh reading of the 1973 original**. Waldspurger p.378 independently gives the compatible local generating function.
- Iwaniec–Kowalski, primary p.377, Prop.14.20: coprime-conductor twist multiplier `χ(r)ψ(q)τ(ψ)^2/r`; for a quadratic character and trivial original character this is `χ_t(−q)`. Its coprimality condition holds here.
- [CKRS, math/0012043](https://arxiv.org/abs/math/0012043), primary Conjecture 1, equation (25): `c_E>0`, exponent 3/4 and logarithmic exponent −5/8; no residue-class refinement. [W. Zhang, §1](https://math.mit.edu/~wz2113/math/online/Kconj.pdf), p.4, states Gross–Zagier–Kolyvagin: analytic rank ≤1 implies equality with MW rank. Its contrapositive certifies the rank≥2 L-zeros; no BSD assumption. Original GZ/Kolyvagin papers were not re-read.

## Independent exact computations

No lane module or census file enters the matrix/twist implementation. It calls `mfinit`, extracts exact coefficients, computes both the kernel-image rank and the independent identity `rank([A;C1])−rank(A)`. Small R-zero witnesses are checked by enumerating u and divisors B in `n=(4uC−1)B−u`; the complete bounded R-zero rows use a separate direct sieve of this identity.

| L,D; space; B | dim / square-row rank | C1 indices / T1-image rank | Rank after R-zero rows |
|---|---|---|---|
| 168,168; full; 40000 | 22 / 9 | 715 / 1 | 0, already from witnesses |
| 420,21; full; 10000 | 56 / 21 | 72 / 1 | 0, already from witnesses |
| 560,280; cusp, good squares; 40000 | 41 / 16 | 857 / 1 | 0, already from witnesses |
| 840,105; full; 8000 | 108 / 45 | 59 / **5** | **0 using all 77 R-zero rows** |
| 840,840; full; 8000 | 108 / 45 | 59 / **5** | **0 using all 77 R-zero rows** |
| 840,105; cusp, good squares; 16000 | 85 / 25 | 115 / 1 | 0, already from witnesses |

At (168,168), coefficients at `(1969,2641,5161,5569,9601)` are `(0,8,−8,−8,8)` in the chosen basis; zero primes 57/238, of which 36 in M. At (560,280), zero primes 54/238, of which 28 in M. At (420,21), the corresponding coefficients are `(−128,0,64,0,0)`: **composite witnesses matter; the two small prime zeros do not kill this line**.

The twists were formed in two stages, `(E84⊗χ_{−168})⊗χ_p`, unlike the lane's direct twist. For `p=337,457,1009,1129,1201,1297,1801,2473,2713,3217,4057,4201,4729`, PARI returns `[2,2]`, root number +1, and two rational points, checked on the curve. The M-members are exactly `1009,1129,1201,1801,4201,4729`. The unconditional conclusion is finite failure of everywhere non-vanishing, not failure of eventual non-vanishing.

The W0 sanity script was also rerun: 2106 primitive diagonal forms, 574 missing all tested odd squares, zero C1 counterexamples. This is a rerun, not an independent genus computation. The large-conductor numerical F4 L-values and complete curve-box search were not independently recomputed; neither is needed for the accepted proof or finite certificates.

Reproduction: `ulimit -v 4000000; timeout 900 uv run --with cypari2 python scripts/z59_xrev_walds_check.py matrices L D B SPACE` for the six table rows; use subcommand `twists` for all 13 rank checks, and `screens /tmp/xrev_WALDS` after extracting the lane's screen, logic-zero and walds data. Commands are sequential or at most two in parallel.

## Falsifier audit

| Screen | Finding |
|---|---|
| F1 odd squares | PASS. W1 explicitly uses them, including products of large primes; the C1 restriction and Gaussian twist are essential. No claim that a(1)=0 alone removes a central-zero eigensystem. |
| F2 12 R8-zeros | PASS with finite-screen limitation stated. Independently filtered all 12: the four M-primes are exactly 10301993881, 10529331121, 10532106649, 10868474401. R8-support implies square vanishing; for a nonzero single line, Cor.2 forces L-zeros at these witnesses. For multiple lines only cancellation is required. No coefficients at these large primes were computed. |
| F3 285 composite zeros | PASS but incomplete presentation. Exactly **15/285** are in M and all 15 are squarefree. The larger LOGIC list has exactly 18 M-composites through 10^10, all squarefree, ending at 17401609, agreeing with the memo. The other 270 screen entries are outside M, not automatically outside every level-dependent C1. The table should not silently substitute the 18-entry enlarged M-list for the mandatory 285-entry screen. |
| F4 14 R-zero / 38 G*-zero primes | R-zero invalidity checks PASS; G* discussion is MISSING. Independent counts: 9/14 and 20/38 lie in M. All 14 R-zero primes occur among the 38 G*-zeros, so a proved R-support invalidity witness also invalidates G*-support. The additional 24 G*-zeros are not automatically R-zeros and cannot be used against R-support without further checking. Add this distinction explicitly. |

## Required fixes, in priority order

1. **Correct every sweep summary/title/FRONTIER compression.** Say 121 distinct quadratic-character pairs, 123 comparisons = 118 full + 5 cusp. Explicitly retain the two full-space rank-5 exceptions; “all rank 1” describes the substituted cusp runs, not the reported full sweep. Saved cusp-only validity certificates concern D=1,8,21,105,840 at L=840. This review newly certifies the **full** spaces for D=105,840 through **B=8000** using all R-zero rows; adopting those certificates leaves only D=1,8,21 restricted to the TERNARY class. Do not extend the new full-space certificate to B=16000.
2. **Fix the 13/6 quantifier everywhere.** There are 13 unconditional C1-prime failures, **six in M**. Keep the eventual/non-eventual distinction and the conditional status of the larger coefficient-zero lists.
3. **Complete the falsifier table** with the 15-of-285 and 14/38 support distinctions just given; no “survives all four” conclusion is warranted or needed.
4. **Make certificates reproducible outside the author's worktree.** `z59_walds_halfint.py` and `z59_walds_diag.py` hard-code worktree-0044; replace with a repository-relative or explicit data root. Shell drivers pipe through grep without pipefail, potentially hiding failed computations. Preserve per-run space, B, row policy and exit status in any regenerated comparison.

With these repairs, the accepted outcome is a correct relative theorem plus scoped finite no-go certificates and a separately labelled conjectural obstruction to single-line effectiveness—not a solution of ES, (MS), or the general cusp-proxy problem.
