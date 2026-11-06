# z60 SIGNED — cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** The scoped no-gos and support-proxy criterion survive independent re-derivation. The rank-5 counterexample needs the normalization/quantifier repair below; this repair works. “Narrowed; no HOT LEAD” follows. Neither ES nor (MS) is settled.
Reviewed `side-agent/z60-signed` at `206a089701a3d2f49192219b3b3bc728835df21d`, including Z59_WALDS W1/W1′ and Z58_TERNARY F, scripts, data and primary sources. No lane files modified.

## Per-claim audit

| Claim | Classification | Finding |
|---|---|---|
| S1, including W1 from prime squares | CORRECT | Real anchors, unitary Rankin–Selberg moments and the sign argument give the claimed dichotomy; no (H2) is needed for the zero implication. |
| Lemma 3.1 / S2(a), mixed quadratic characters | CORRECT-WITH-FIX | Multiplicativity and Dedekind induction work on squarefree good m; remove division by possibly zero Eψ(1). |
| S2(b), signed mixed weight 3/2 | CORRECT | Character-selective products separate genus anchors; primes and products of two primes then separate all cusp anchors. |
| S3, one character in higher weight | CORRECT | The genus dominates at squares and primes; the normalized cusp inequality is the same RS problem. |
| Higher-weight mixed support extension | CORRECT | Distinct genus square factors and distinct cusp systems remain multiplicatively independent; signed extension is not implied. |
| Rank-5 mixed signed counterexample | CORRECT-WITH-FIX | The claimed example works, but the cited proof only treated squarefree m with factors ≥11, not T1⁻ at every odd square; ratios also silently change normalization. See repair 1. |
| Cosets, §4.2 | CORRECT as CONDITIONAL | One underlying determinant/genus and (SWc) are essential. Only classwise genus conclusions and the termwise exclusion follow; no cusp/global dichotomy is established. |
| S4 / S4′ | CORRECT / honestly CONDITIONAL | Constant eventual sign on 1 mod M is enough. The explicit (Dom) hypothesis is indispensable; no general mock/Rademacher exclusion follows without it. |
| S5 support equivalence and genericity | CORRECT | Validity is exactly K ∈ W⊥; each prime outside W excludes one proper hyperplane. This is not a validity mechanism and does not control rational coefficients. |
| S5 conditional L-value dictionary | CORRECT in stated scope | W1′ anchor/(H2) assumptions and signed square roots are retained. The disjunction needs the full-line-span and W=0 hypotheses. |
| S5 signed paragraph | CORRECT-WITH-FIX | The validity cone is right, but replacing equality by inequality does not define a vector space Λ. Pointwise avoidance of the polar is only necessary, not sufficient for one common K. |
| §6.1 mixed certificates | CORRECT, independently reproduced | All three zero-restriction ranks are 0; these are finite support certificates, not signed-cone or asymptotic exclusions. |
| §6.2 correlations/signs | CORRECT as EVIDENCE, minor factual fix | Saved-row counts/correlations reproduce. The ramified-factor correction also changes prime n=193, contrary to the prose. |
| §6.3 t420 | CORRECT at stated labels | Six decisive exact rank bounds and the numerical 0.379908466069321 reproduce. Algebraic rank 0 alone does not certify central nonvanishing. |
| §4.4 / heuristic ≥5-line disjunction / verdict | Assessment, appropriately scoped | No classification theorem or simultaneous prime nonvanishing theorem is supplied; independence/CKRS remain heuristic. |

## Re-derivation and hypothesis transfer

1. TERNARY F Step 1 applies separately to each quadratic ψ: its theta lattices have the same determinant square class, good local lattices agree, and bad densities are invariant under unit-square scaling. Thus Eψ(n)=Eψ(1)Bψ(n)/Bψ(1) on C1, with Bψ>0. It does **not** assert a common B across different ψ. At a good prime square the genus factor is ℓ+1−εψ(ℓ).
2. For S1, divide the square identity by ℓ and take primes in a and −a. Oddness of the primitive unary-character combination gives E(1)≤0, and gives u=0 when E(1)=0. If E(1)<0, Siegel gives a negative main term of size at least p^(1/2−ε), while Duke gives O(p^(13/28+ε)); choose ε<1/56. Unary terms miss these primes. This proves eventual negativity, with an ineffective threshold.
3. For the cusp step use unitary λℓ=aℓ/√ℓ. Logarithmic derivatives at s=1 give first moment O(1) and cross moments δφφ′/(s−1)+O(1); prime powers contribute O(1). For bounded real G=Σcφλφ with G≤O(ℓ^−1/2), Σ|G|w=2ΣG⁺w−ΣGw=O(1), hence ΣG²w=O(1). RS makes the latter (Σcφ²)/(s−1)+O(1); all anchors vanish. Distinct newforms, not duplicate oldvectors, must index φ, as in W1.
4. WALDS W1 Steps 4–5 then carry over, not its original T1 equality hypothesis: a nonzero eigenspace implies (H1), and t∈C1 gives t/1∈Qq² for every q|4N. Corollary 2 at (1,t) gives gφ(t)²L(φ⊗ψχ−4,1/2)=0. No (H2), nonzero anchor, or unproved line identification enters this implication. The stronger one-line dictionary in S5 separately retains W1′ hypotheses.
5. S2(a): genus, unary and cusp square factors multiply over distinct good primes. Different ψ have different ε; different φ cannot agree eventually up to bounded ε-errors, by the RS second moment. Eliminating one coefficient using the relations at m and ℓm proves independence by induction, still on squarefree m after enlarging the excluded prime set.
6. S2(b): each odd quadratic ε has a distinct half-sized negative set. Reciprocal-prime divergence in its residue classes produces a product growing as T^h for the selected ψ and at most T^(h−1) for the others; cusp/m and unary terms stay bounded. Thus every Eψ(1)≤0. Any negative one dominates at primes; otherwise use primes to kill u. RS at prime squares gives Cφ=Σψcφψ=0; averaging the remaining nonnegative character combination gives Dψ=Σφcφψ=0. Expanding at (ℓ₁ℓ₂)² cancels the double-eigenvalue and εε terms. Fixing ℓ₁ in each class and applying the sign argument to ℓ₂ kills Hφ(a)=Σψcφψεψ(a), hence every cφψ. No residue-restricted RS independence is assumed.
7. In S3, the genus square term is E(1)ℓ^(2κ−2)(1+O(1/ℓ)), versus cusp O(ℓ^(κ−1)); after E(1)=0 the Hecke correction divided by ℓ^(κ−1) is O(ℓ^−1/2). The absolutely convergent genus product at primes dominates Duke. Mixed support uses distinct factors ℓ^(2κ−2)+1−εψℓ^(κ−3/2); mixed signed separation fails because their relative corrections are summable.
8. S5 is independent finite-dimensional linear algebra. A prime R-zero necessarily has S(p)∈W, so its criterion already contains the prime target. Countably many proper hyperplanes cannot cover W⊥; free coordinates may be algebraically independent over the countable coefficient field. The modular residue projection can raise the level, as acknowledged. Neither the cone version nor rational coefficients inherit this genericity argument.

## Required fixes, in priority order

1. **Repair the rank-5 proof before recording the unrestricted T1⁻ claim.** Write A₁=θ₁/10 and A₂=θ₂/8 throughout. The displayed ratio bounds concern A₂/A₁, not θ₂/θ₁: at p=17 the latter is 736/480=23/15<25/16. Use normalized genus thetas if avoiding any class-number assertion; independent PARI gives dim S_(5/2)(8,1)=dim S_(5/2)(8,χ8)=0, so these concrete theta series equal their genus averages anyway.
   A proof for **all odd m**, including prime powers, is short. For ℓ^a∥m put U=Σ(j=0..a)ℓ^(3j), V=ℓΣ(j=0..a−1)ℓ^(3j). The normalized genus factor is U−εV. Thus A₂(m²)/A₁(m²) is the product, over ℓ|m with (2/ℓ)=−1, of (U+V)/(U−V)≤(ℓ²+1)/(ℓ²−1). Its upper bound is at most ∏(ℓ odd prime, ℓ≠7)(ℓ²+1)/(ℓ²−1)=(3/2)(48/50)=36/25<3/2; here ∏(ℓ odd)(ℓ²+1)/(ℓ²−1)=ζ(2)²/ζ(4)·3/5=3/2. Hence g(m²)<0 for every odd m.
   At p≡17 mod24, bad-prime factors cancel and (2/p)=1; the normalized prime ratio is ∏[(1+ℓ^−2)/(1−ℓ^−2)]² over odd ℓ with (2/ℓ)=(p/ℓ)=−1. Every factor is ≥1 and ℓ=3 gives 25/16>3/2. This proves positivity at all such primes. The escape is real, but supplies no R-validity and no all-M-prime positivity.
2. **Keep vector spaces and cones distinct in §5.** Choose a basis of an ambient linear space of possible forms/restrictions; impose all square and R-zero inequalities in K. Do not redefine the vector space Λ by g(m²)≤0. Explicitly retain the common-K feasibility condition; “each S(p) avoids the polar” cannot replace it. This does not affect support S5.
3. **Remove a zero-denominator proof expression.** In Lemma 3.1 write Eψ(m²)=Eψ(1)∏(1+ℓ−εψ(ℓ)), obtained termwise from genus densities, rather than Eψ(m²)/Eψ(1). The zero-anchor case is central to the theorem. In Step 3 of S2(b), taking m prime in each class already suffices.
4. **Correct §6.2's ramified-factor sentence.** The (168,168) prime row n=193 has 193≤Y=200 and 193 is good. Changing its local factor from (1+1/193)^−1 to 1 multiplies P_Y(193) by 194/193. Thus prime rows are not literally unchanged, although the displayed rounded correlations/sign counts reproduce.

## Independent computation record

Committed helper: `scripts/z60_xrev_signed_check.py`; no lane script or saved zero census is imported. Runs used `ulimit -v 4000000; timeout 1800 uv run --with cypari2 python scripts/z60_xrev_signed_check.py ...`, with at most two compute processes. PARI stack: 2 GB. Exact zero enumeration uses u≤b by symmetry and 4ubC−u−b≤X, with bounded one-dimensional storage.

| Invocation | Independent result |
|---|---|
| `mixed 168 40000` | dim V=176, C1 indices=715; square-only kernel dimension 128/restriction rank 3; with zeros dimension 104/rank 0; 169 union rows. |
| `mixed 240 30000` | dim V=272, C1 indices=500; square-only dimension 222/rank 9; with zeros dimension 190/rank 0; 150 union rows. |
| `mixed 280 30000` | dim V=240, C1 indices=644; square-only dimension 184/rank 6; with zeros dimension 140/rank 0; 150 union rows. |
| `twists` | At 102001: χ21=[0,0], χ105=[2,2]; at 712321: χ21=[2,2], χ105=[0,0]; at 8813281: both [0,0]. All six root numbers +1; returned points checked on-curve. |
| `analytic` | χ21 at 102001: numerical analytic rank 0, central value 0.379908466069321, agreeing with the memo; not an interval-certified L-value. |
| `rank5` | Both cusp dimensions 0; max g(m²)/m³=−0.131090789005741 through 20000; all 289 primes 17 mod24 positive; 0/53 M-primes positive. |

The independent zero census includes n=1, whereas the lane's LOGIC zero list omits it: 169/150 zero rows here versus 168/149 there, with **identical union constraints** because 1 is already a square row. No discrepancy in the certificate.
Additional independent enumeration confirms R=0 and the stated prime/composite type for all 14 prime and 285 composite falsifiers. Saved §6.2 rows reproduce all five prime sign counts and all 15 displayed correlations; this is a data-summary check, not a new eigensystem identification. The remaining 12 twist entries and exploratory base-rate tails were inspected, not independently recomputed here.
PARI's manual explicitly calls its descent quantities unconditional. Rank ≥2 implies central vanishing by Gross–Zagier–Kolyvagin; rank upper bound 0 is **not** central nonvanishing or the Selmer dimension. The two-line exclusion still needs the stated identification/nonvanishing evidence, and finite failures cannot exclude validity beyond a larger threshold.

## Falsifier audit

| Screen | Verdict |
|---|---|
| F1 odd squares | Correct for the scoped no-gos. S1/S3 use prime squares; S2 needs composite square indices too. Rank-5 unrestricted odd-square compatibility requires repair 1. No positivity or validity follows from surviving F1. |
| F2 R8 | Inventory agrees: 12 zeros, 4 in M, largest in-M zero 10868474401. The no-gos are line-blind; S5 requires P₀≥that zero on M-containing levels. The unscreened R8 line values are explicitly admitted, not claimed to pass. |
| F3 composites | All 285 independently verified; 15 lie in M and are squarefree. Exact certificate rows include all R-zeros through B, not just primes. S5 must retain composite-zero constraints even though effectiveness is asked only at primes. |
| F4 prime/G* zeros | Counts 14/9 in M and 38/20 in M agree. Three of five saved lines are nonzero at both 5569 and 9601; t420 qualifications are preserved. The other five R-zero primes and G*-specific line values were not screened. Non-R G*-zeros cannot invalidate an R-support proxy. |

## Literature checked from source

- [Waldspurger 1981](https://mate.dm.uba.ar/~nsirolli/files/waldspurger.pdf), pp. 376–379, downloaded/read including page images: all odd k≥3; weight 3/2 uses the unary orthogonal complement; Prop. 1 decomposition, Prop. 2 implication (H1), χ₀, and Cor. 2 checked. Cor. 2 does not assume (H2); Théorème 1 does. The memo respects this distinction in its decisive claims.
- [Duke 1988](https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf), p. 78 (2.5), p. 85 Thm 5 and pp. 75–76: a(n)=(4πn)^(κ/2)ρ(n), ρ(n)≪n^(−2/7+ε), hence a(t)≪t^(κ/2−2/7+ε). Weight 3/2 is explicitly included. The negative assessment in the lane's raw research report is superseded correctly by the memo/internal review.
- [Sarnak, Nonvanishing on Re(s)=1](https://publications.ias.edu/sites/default/files/ShalikaBday2002.pdf), abstract and §1, especially (5): standard and pair L-function nonvanishing verified as stated there; with the classical simple diagonal RS pole and Deligne, this supplies the exact moments used, without a prime number theorem.
- [Lester–Radziwiłł](https://arxiv.org/pdf/1903.05811), Thms 1–2: squarefree-index sign changes, not a prime-index theorem; their stated k≥2 means weight ≥5/2, so this citation should not be read as a theorem for the weight-3/2 survivor lines. [PARI ellrank manual](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html#ellrank) confirms unconditional descent bounds and the Sha correction. Siegel and Gross–Zagier–Kolyvagin are accepted classical inputs; their original proofs were not re-audited. (SWc) and general Rademacher asymptotics remain unverified/conditional, as labelled.

**Bottom line:** accept the narrowed result after these repairs. No theorem here kills all signed proxies, all higher levels, rational multi-line cancellation, or the need for an independent validity mechanism.
