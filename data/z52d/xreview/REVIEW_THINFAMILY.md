# THINFAMILY — independent hostile review

**Verdict: ACCEPT-WITH-FIXES.** The mathematical narrowing survives; the claim that BM on minimal certificates is “killed” does not. ES remains OPEN.
Reviewed `side-agent/depth-thinfamily` at `8b1f7aaca36da6b1f95baadc9a8ee83271d7c368`, including its memo, scripts, cited local lemmas, and decisive external sources.

## Per-claim findings

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Specialisation criterion and irreducibility of n for c₀ = 3, 15, 63 | CORRECT | Clear polynomial denominators; odd moduli see Y = 1 and powers of 2 see Y = 0. Capelli excludes odd-power and exceptional fourth-power factorizations of n. |
| Thm 1: 2-power C-finite certificate gives a root family through 0 | CORRECT-WITH-FIX | Clear rational-exponent denominators before the Galois argument. Negative exponents vanish by discreteness; exponential-polynomial independence gives the polynomial identity. A stronger, simpler finish is supplied below. |
| Thm 2: irreducible smallest x gives A, A′, C | CORRECT | Degree D and gcd(n,x) = gcd(f,nx) = 1 hold. The resultant and remainder arguments produce polynomial dᵢ; all nine assignments of n and x to d₁,d₂,d₃ reduce to the five unordered cases listed. Constant/constant and separated n/x are impossible; the other three give exactly A, A′, C. |
| Lemma 2.1: f′ cannot be constant | CORRECT | The CRT square can avoid every prime in c and κ′: primes already in the modulus see an odd unit or 2^J. The two reductions give the precise coprimality hypotheses of the paper's Lemma T1(ii)/(i), respectively. |
| Prop 3: C empty | CORRECT | From c = 4gw and gcd(w,nx₁z₁) = 1 obtain w divides g, hence c = 4w²d. Then (−d/f) = 1 from n² ≡ −4w²d, but reciprocity gives −(n/d′) = −1. The even-d case correctly uses f ≡ 7 mod 8. |
| Lemma 4: A integrality, including converse | CORRECT | The Y = 0 congruences force integer c divisible by 4; Capelli and power-freeness force odd integer u. Unit roots imply integral X,X′. The odd and 2-adic z conditions are exactly those stated; together with the positive factor shape they suffice by specialisation. |
| Thm 5: A magnitude bound | CORRECT | Recomputed W² = c_o(k²c_o − 4F(k+2^E)); difference of squares gives the stated bound. Dividing the bound by k² leaves only constant and decreasing positive terms, justifying k = 1. |
| Cor 5.1(a): all A with u ≡ 3 mod 8 empty | CORRECT | Independently enumerated all divisors for all four possible (u,p); all fail the necessary congruence. No restriction on D or integer (a,d) parameters enters this argument. |
| Cor 5.1(b): approximation and per-p finiteness | CORRECT | Odd p gives a unique 2-adic root and equal valuations. The exponent is p/3; Ridout gives finiteness only for fixed p ≥ 5, not p = 3 or uniformly in p. The u = 1 representation exception is outside A's E ≥ 2. |
| Lemma 6: D-independent shape superset | CORRECT | Reciprocal roots give a monic factor of Z^D+B/A. Gauss's lemma yields positive ℓ dividing A and positive g(1) dividing A+B. This is a necessary superset, not a sufficiency claim. |
| Thm 7: A′, odd integer u | CORRECT | Odd-denominator cancellation gives dyadic X′; root valuations make X,X′ integral. Expanding (jc_o−16)(j′c_o−1) gives jj′c_o = 2^E+j+16j′ and exponent p/2. |
| Thm 7: even integer u and integer Sophie-Germain w | CORRECT | For even u, 1 ≤ t ≤ pk−1 yields c ≤ 1+17·2^t < 15·2^(pk)−1. The analogous w bound works. For odd w only t = 1 is actually possible; the larger enumeration is harmless and c = 59 fails even its necessary equations. |
| Thm 7: nonintegral dyadic u or w | CORRECT | Root valuations give v₂(X)=0, v₂(X′)=−e. Expanding XX″ gives jj′c_num−2^e j−16j′=1, hence c_num ≤ 2^e+17; y(0) requires v₂(1+φ₀) ≥ e+2. |
| Computation 8(a),(b), all-D exclusions | CORRECT | Full decisive reruns agree; independent checks of the exceptional limit hits also eliminate them. See reproduction below. |
| §2 BM calibration and minimal-sequence complexities | CORRECT as finite data | All 117 calibration sequences pass. Even-s minimal y has L=12 on 24 terms; this does not establish nonrecurrence. |
| §0/§6: “minimal certificates show no recurrence”, “void”, “sub-route killed” | GAP | No argument excludes a higher-order or later-onset recurrence, another progression, or a recurrence with different roots. Finite BM evidence cannot supply that conclusion. |
| Thm 1 scope: Corvaja–Zannier paraphrase | CORRECT-WITH-FIX | The general result requires passage to an arithmetic progression and concludes a recurrence, not necessarily a simple power sum. This citation is not used in the proved narrowing. |
| §5: 4^s+297 | CORRECT arithmetic; Assessment otherwise | 4³+297=19² and ord₁₉(4)=9. The cited compactness criterion and whole-3-line coverage do not prove that recurrences are useless; the memo labels this discussion Assessment. |
| §6 verdict “narrowed” and survivor list | CORRECT-WITH-FIX | Structural and bounded exclusions justify narrowing, not death of the cluster. Remove the BM kill claim; retain every beyond-bound and reducible-x escape listed. |

## Required fixes, in priority order

1. **Remove the unconditional BM kill language** in §0 and §6. Replace it with “No low-order recurrence was detected for minimal y on the tested even progression (24 terms, L=12); this is evidence against this fitting strategy, not an obstruction theorem.” Restrict the calibration claim to the explicitly audited rules. Likewise, observed even-s gaps alone do not prove global C-finiteness of minimal x; qualify that inference by s ≤ 60 unless a separate proof is supplied.
2. **Make Thm 1's rationality step explicit.** Restrict t to multiples of both the root-of-unity orders and every denominator of λ_j before applying Galois uniqueness. Reindex t = Hq: the bases 2^(Hλ_j) are now rational and distinct, so the coefficient polynomials are rational. The remaining discreteness and polynomial-identity steps work as stated.
3. **Repair the Corvaja–Zannier statement.** Say that on a suitable progression qn+r there is a nonzero polynomial P(n) such that P(n)F(qn+r)/G(qn+r) and G(qn+r)/P(n) are recurrences. Do not infer that the progression contains μ = 0 or that the resulting bases are powers of 2.

### Optional stronger finish to Thm 1

After obtaining x,y,z in Q[t,Y], work over K = Q(Y) and let t tend formally to infinity in 1/x+1/y+1/z = 4/n.
If all three have positive t-degree, the left side tends to zero, impossible.
If exactly two have positive t-degree, the constant coordinate must equal n/4, so the other two sum to zero; positivity on the original progression excludes this.
If exactly one has positive t-degree, the two constant reciprocals already sum to 4/n, forcing the remaining reciprocal to be zero, impossible.
Thus all three have t-degree zero. The original subsequences themselves are polynomials in Y; freezing t is unnecessary.
This independently closes the “coefficients depending on s” issue without weakening the conclusion to existence of a different specialised certificate.

## Reproduction and numerical agreement

Files were extracted from the pinned branch into `/tmp/xrev_THINFAMILY/`; every execution used `ulimit -v 6000000` and an explicit `timeout`.
The scripts allocate at most a 2 GB PARI stack individually; no dense Cartesian-product arrays were introduced.
Use `uv run --with cypari2 --with gmpy2 --with sympy python scripts/<name>` from the extracted tree (the BM module resolves its verifier beside the script).

| Script / arguments | Timeout | Recomputed result |
|---|---|---|
| `z52d_thinfamily_menuA.py 15 3000` | 2400 s | 4878 candidates, p up to 5669; four raw hits (u=1 in each menu, repeated at p=3,5); every all-D shape test empty; exit 0. |
| `z52d_thinfamily_dyadic.py 66` | 1200 s | 451713 windows; one limit hit u=1/2, c=7/8, X=5, X′=27/8; zero all-D survivors and zero explicit-D hits; exit 0. |
| `z52d_thinfamily_bm.py 60` | 600 s | 39 rule-classes × 3 coordinates: every characteristic polynomial and all 10 predictions agree; minimal even y L=12/24, odd y L=3; exit 0. |
| `z52d_thinfamily_xcheck.py` | 240 s | 2400 k-loop versus divisor comparisons, zero mismatches. |
| `z52d_thinfamily_menuA.py 63 400` | 180 s | 1018 candidates, exactly one limit hit (E,p,u,c,X,X′)=(2,3,3,1700,21,84), passing the shape superset. |
| `z52d_thinfamily_menuA.py 3 400` | 180 s | 444 candidates, 14 raw limit hits; precisely c=80 survives, with X=1,6,21 in A and X=21 in A′. |

Separate `uv run --with sympy` divisor enumeration, not the memo's k-loop, gives (u,p,c_o) = (3,3,101), (11,3,4991), (3,5,911), (3,7,8201), each with no admissible divisor pair.
Separate exact `Fraction` arithmetic over Lemma 6's finite divisor superset gives zero survivors for both menus at u=1 and for A′ at u=1/2. For the latter, φ₀=5/g with g∈{1,3,9} never equals −1 modulo 32.
The menu-A loop covers all necessary u≥3 via the exact height bound and unique odd-p Hensel residue; u=1 is p-independent and explicitly checked. The A′ bound is smaller, so that same enumeration covers its odd-integer candidates. The k-loop stopping inequalities are monotone and cannot skip a later admissible k.
The exploratory explicit-factor search 8(c) and general odd-denominator search 8(d) were not rerun: their counts are not needed for this verdict and remain EVIDENCE, not exclusions of the surviving regimes.

## Citation audit and scope

Ridout's integer exponent 1+ε is justified by the simultaneous-place formulation in P. Corvaja, *An explicit version of the theorem of Roth–Ridout*, Theorem 1, pp. 253–255: https://seminariomatematico.polito.it/rendiconti/cartaceo/53-3/253.pdf (visited).
Apply it to the rational approximant 1/u, with target 0 at infinity and β⁻¹ at 2, where β=15^(−1/p). Height is u, and the product of approximation errors is u⁻¹·|u−β|₂, giving the required exponent 1+ε. The source explicitly states ineffectivity.
The correct Corvaja–Zannier formulation is stated by Zannier himself as Theorem B, p. 429, in *Diophantine equations with linear recurrences*: https://www.numdam.org/item/10.5802/jtnb.499.pdf (visited); its reference [CZ2] identifies the cited 2002 paper. Direct retrieval of the linked original paper failed; the author’s explicit restatement supplies the checked hypotheses and conclusion.
No conditional finiteness was promoted to effective emptiness. The large bounds are finite certificates only; p=3 in A, all stated beyond-bound cases, odd-denominator A′, reducible x, and other bases remain open.
**Final disposition: accept the narrowing after the three fixes; do not record a theorem killing minimal-certificate recurrences or resolving ES.**
