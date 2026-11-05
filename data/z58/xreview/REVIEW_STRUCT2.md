# z58 hostile cross-model review — STRUCT2

Reviewed `side-agent/z58-struct2` at `b7c218df4e50273a996cb4f54ed934e2d779871e` (`Z58_STRUCT2.md`, scripts/data, and STRUCT/WILDCARD dependencies).
**Verdict: ACCEPT-WITH-FIXES.** Theorem B and the genuine positive-integral non-BM failure at 4545 survive independent checking. The mandatory falsifier table and final no-go rhetoric do not survive unchanged. ES remains OPEN.

## Per-claim findings

| Claim | Classification | Finding / required qualification |
|---|---|---|
| B(i), smooth over ℤ | CORRECT | In every residue characteristic a Jacobian entry is nonzero: if K vanishes, ∂F/∂a = −1; otherwise Kabc = 0 forces another entry to be −1. The relative hypersurface Jacobian criterion gives smoothness. |
| B(ii–iii), scaling/product/D | CORRECT | Both maps and inverses check. State t ∈ ℚ× in (ii). D is reduced, smooth, and isomorphic to 𝔸² over ℚ; it is not an omitted singular boundary. |
| B(iv), Pic/units | CORRECT | The (b,c,f)-chart gives ord_E(f)=1. Localization sends the generator f of the nonconstant units on X∖E onto E, killing Pic and leaving only constant units on X̄. |
| B(v), Brauer group | CORRECT | Purity applies over ℚ; the residue kernel is exactly ℤ/2. No class is lost at D; see the separate boundary check below. |
| B(vi), π₁ and étale–BM | CORRECT | π₁(S₁)=1 can be proved directly without the cited plane-curve theorem; the reduced c-meridian kills the remaining ℤ in X°. |
| B(vii–viii), local signs/BM | CORRECT | Hilbert-symbol calculation and sign freedom work, including even n and p=2. For K=8 the obstruction is □∪2□, not merely squares for even n. |
| Lemma C | CORRECT | f,g≥K−1 gives a+b≤2nc/(K−2). For K=4, 1≤4abd−n≤n, abd≤n/2, c≤a+b≤2abd≤n. |
| Prop F | CORRECT | Restriction is the full fibre generator, with lattice condition c₀∣C. Exactly the odd-valuation primes of n not dividing c₀ allow sign changes. For 4545: obstructed iff 505∣c₀. |
| Prop T / intermediate ℬ_c | CORRECT | Over ℚ, ker(rec)=ℚ×ℝ>0; all finite coordinate components become one positive integer. Fixing a,c,d forces integral positive b. Real coordinates need not equal their finite common values. |
| Thm 4.1, 4545 | CORRECT | Independent exhaustive count is zero; an explicit BM adelic point also satisfies the ET condition, including at 2. Details below. |
| §4 finite-field densities/inheritance | CORRECT | Re-derived the (p−1)³ coprime count and both unrestricted counts; checked p=3,5,7,11. Independent parent counts/residue tests agree. |
| §4 statistical explanation | Assessment, not a theorem | Counts support a populated tail, not a calibrated probability or causal explanation. Full fitted models were not rerun; their stated failure to fit tails is appropriately disclosed. |
| §5.1 CONV-II equivalence | CORRECT | With the stated positive region, odd n≥3, and the 4545 exception, this is precisely the IHP-with-BM formulation. |
| §5.2 fixed sub-region counterexamples | CORRECT-WITH-FIX | The explicit failures check. They refute an unqualified implication, not an eventual theorem above 10¹⁷. Keep the qualifications in every summary. |
| §5.3 fibration discussion | CORRECT-WITH-FIX | The cited theorems do not directly supply the desired positive integral points. “Would need equidistribution” is not established necessity; replace with “one possible additional input is equidistribution”. |
| F1 | CORRECT | Non-squareness enters exactly through an odd valuation (at 2 as well for K=4). |
| F2 | CORRECT-WITH-FIX | The table substitutes 22 small full-N⁽⁸⁾ zeros for the mandatory 12 R₈ zeros. All 12 mandatory parameters actually have full-N⁽⁸⁾ points with c>1. These are different screens. |
| F3 | CORRECT-WITH-FIX | The 285 are failures of the c=1 surface, not of X_n: independently found X_n points for 284; only 4545 remains, and its count is exhaustively zero. State this explicitly. |
| F4 | WRONG as written | “On S_n … they are non-BM failures” is false for all 38 𝔊*-zeros: only the 14 (★)-zeros are S_n failures. At 37, (u,B,C)=(1,2,5) is a positive S₃₇ point. All 38 have X_n points. |

## Independent proof checks: boundary, Brauer group, topology

Set f=Kacd−1. On U=X∖E≅𝔸³∖{Kacd=1}, purity embeds Br(U)/Br ℚ into H¹(𝔾_m²,ℚ/ℤ). The rational basepoint splits this as constant characters plus two order-two coordinate classes. The explicit cyclic/quaternion algebras realize every summand; no surjectivity of a truncated purity sequence is assumed.
On E, a=−nc and ord_E(f)=1, so the residue of (χ,f)+ε₁(−f,−a)+ε₂(−f,−c) is χ+ε₁[n]+ε₂[−1]+(ε₁+ε₂)[c]. Independence of the nonconstant [c] forces ε₁=ε₂ and χ=ε₁[−n]. The remaining generator differs from (−f,−nac) only by a constant algebra. Pic X̄=0 and constant geometric units imply Br₁(X)/Br ℚ=0.
**D={c=0}:** generically a is a unit, v_D(−nac)=1, and (−f)|_D=1. Thus the quaternion residue is [1]=0. Also D⊂U (f=−1 there), so the proof already includes D rather than silently working only on X°. At {a=0} the residue is likewise [1]=0; at E, −nac=n²c² is a square. Codimension-two intersections introduce no missing condition by purity on the regular X.
For topology, V=ℂ²∖{xy=n} has V∩{x≠0}≅ℂ××(ℂ∖{n}) via (x,xy). Adding {x=0} kills the x-meridian and leaves π₁(V)=ℤ generated by xy−n. The S₁ chart obtained by removing {u=0} is such a V; adding {u=0} kills that last generator. Consequently π₁(X°)=ℤ, detected by c. Adding the smooth reduced divisor D kills it. Geometrically simply connected X has no additional finite-étale descent obstruction.
At odd primes dividing f, integrality forces n,a,c to be units and −nac≡a², so the symbol is +1. If p∣ac, −f≡1. Otherwise the only possible odd-prime contribution is (−f/p)^v_p(n). At 2, 1−Kacd is either a square or in 5ℚ₂×², giving exactly B(vii). Sign freedom at one odd-valuation prime cancels the constant real sign −1. These arguments establish both numerator statements, not just sampled evidence.

## Independent arithmetic checks

Reproducer: `scripts/z58_xrev_struct2_check.py` (standard library only; no imports of lane enumerators). Run against an archive of the reviewed branch with `ulimit -v 4000000; timeout 1800 uv run python scripts/z58_xrev_struct2_check.py /tmp/xrev_STRUCT2`.
Its exhaustive enumerator orders a≤b, uses Ka²d≤n+2a and n/(Kad)<b≤(n+a)/(Kad−1), tests c=(a+b)/(Kabd−n), then restores a↔b symmetry. These bounds follow directly from c≥1, rather than assuming the lane's counts or witness cutoffs.

| Check | Independent result |
|---|---|
| N₄(4541), N₄(4545), N₄(4549) | 56, **0**, 48 |
| N₄(1515), N₄(909), N₄(45) | 23, 20, 4; respectively no c or d divisible by 3, 5, 101 |
| Numerator 8 | N₈(35569)=0, N₄(35569)=46; exactly 22 odd-prime N₈ zeros through 35569, independently enumerated |
| Fixed sub-region misses | Confirmed at 342049 (3∣d), 161281 (4∣a), 395137 (5∣c), 389401 (5∣d), 359297 (4∣d); underlying N₄ counts 96,32,76,112,102 |
| Count files | 2,001 rows n≡1 mod 4 through 8001 independently match N₄, c=1, and coprime counts; rerunning the lane C engine reproduces all 30,000 rows through 119997 byte-for-byte |
| Coprime tail | Recomputed from those reproduced files: 88 non-square coprime zeros, 83 divisible by 3, remaining five divisible by 5 |
| Local symbols | 61,427 K=4 and 61,553 K=8 independently generated integral local samples, including even n: zero mismatches |
| Mandatory screens | Explicit full-N₈ witnesses at all 12 F2 primes; full-N₄ witnesses at all 38 F4 primes and 284/285 F3 composites |

The independent small-prime N₈-zero list is 3,5,11,17,19,53,101,113,131,241,491,739,1061,1129,1249,2081,2531,3169,3221,3361,5281,35569. I did not independently rerun the interval (35569,10⁹], the 12 R₈-zero certifications, or every row of the SA table; none is needed for the counterexamples used here.
For an explicit F2 distinction, at n=10156800001 the full numerator-8 point is (a,b,c,d)=(2,640518919,7,1). Indeed 8abcd=a+b+nc; c=7>1, so this does not contradict R₈(n)=0. The script prints all 12 witnesses (all c>1).

**4545 at every place.** Take P∞=(1,4546/3,1,1), and P_p=(1,4546/(4d_p−1),1,d_p), with d₃=2, d₅=3, and d_p=1 otherwise. All coordinates are positive rationals and each P_p is p-integral: the sole exceptional denominator for d=1 is 3, handled by d₃=2. At 3,5,101, a,b,d are units, exactly the ET condition gcd(abd,4545)=1 locally. At 2, b has valuation 1 but n is a unit, so ET coprimality imposes no restriction; requiring every coordinate to be a 2-adic unit would be a different condition.
The signs at 2,3,5,101 are respectively +,+,+,−; all other finite signs are +. The real sign is −, so the total product is +. In particular this proves BM non-emptiness **with ET coprimality**, not merely unrestricted local solubility. Combined with N₄(4545)=0 and π₁=1, the claimed positive-integral BM/étale–BM failure is genuine. It is not an unrestricted integral Hasse failure: X_n has non-positive integral points.

## Literature checked at the source

- [Colliot-Thélène–Skorobogatov, book](https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf), Thms 3.7.1–3.7.2, equations (3.11)–(3.12): exactly the left-exact purity sequences used. Regular divisors and invertibility of the torsion primes are required; all hold over ℚ here. No purity assertion over ℤ at 2 is being used.
- [CT–Harari](https://arxiv.org/pdf/1209.0717), Thm A / 3.5: simply connected almost-simple homogeneous generic fibre, connected reductive stabilizers, split fibres, local section/isotropy, and constant Brauer evaluation at the omitted place. The full theorem does **not** require Br X=Br k (that is an abstract-level special case). No application to the displayed fibres is established.
- [CT–Xu](https://arxiv.org/pdf/0712.1957), Thm 3.7(b): noncompactness of each almost-simple factor at a place in S₀; conclusion is S∪S₀-integrality and approximation only outside S₀. This supports the omitted-place warning, not a positive-region theorem for X_n.
- [Derenthal–Wei](https://arxiv.org/pdf/1311.3914), Thms 1.1–1.2: specific norm-form families, with explicit unboundedness/component conditions at infinity. These are not general existence theorems for arbitrary split torus fibrations.
- [Harpaz](https://arxiv.org/pdf/1511.04876), Thms 1.0.1 and 3.1.12: pencils f(t,s)x²+g(t,s)y²=1 over ℙ¹, square-class Condition (D), local valuation/splitness conditions and vertical-Brauer orthogonality. The memo correctly does not claim these hypotheses for X_n; leave “needs non-trivial norm data” as an assessment, not a universal impossibility theorem.
- [Harpaz–Wittenberg](https://arxiv.org/pdf/1409.0993), Thm 1.3 and introduction: smooth proper varieties, zero-cycles/rational points, not integral points in Ω.
- [CT–Wittenberg](https://arxiv.org/pdf/0911.3539), Thm 4.1(a): for nonzero a≢±4 mod 9, no integral BM obstruction to three cubes. The nearest-analogue description is supported at theorem level. [Ghosh–Sarnak](https://arxiv.org/abs/1706.06712) directly confirms the almost-all/infinite-failures abstract statement, not that every failure is beyond BM.
The Duke–Schulze-Pillot analogy remains explicitly unverified at theorem level here, as it is in the memo; retain that label and the primitive spinor-representation hypothesis. Nothing in the main proof depends on it.

## Required fixes, in priority order

1. **MAJOR — repair F2/F3/F4 and their summaries.** F2's 12 large R₈ zeros all admit full-N₈ points; distinguish them from the 22 small full-family prime zeros. Say 284 of 285 F3 parameters have X_n points. Restrict the “S_n non-BM failures” clause of F4 to the 14 (★)-zeros, not all 38 𝔊*-zeros.
2. **MAJOR — preserve the scoped conclusion everywhere.** Replace the bottom-line “so BM-level information cannot carry (MS-II)” by “BM non-emptiness alone is not a sufficient criterion at all parameters; these examples do not exclude an eventual theorem, including one above 10¹⁷”. Remove necessity from “would need equidistribution”. In F2, replace “the difference is quantitative” by the weaker, already admitted statement that size versus additional arithmetic structure is undecided.
3. **MINOR — Prop T does detect emptiness, tautologically.** Replace the bottom-line “not seen by the (χ, coordinate) Brauer classes” by “seen only tautologically by the subgroup of Prop T”. Its asserted equivalence says its Brauer set at 4545 is empty. This is compatible with Br X being insufficient, but not with saying those open-variety classes see nothing.
4. **MINOR — retain positivity and ET scope.** Qualify shorthand “integral Hasse failure” by Ω; state ET coprimality as gcd(abd,n)=1 rather than an all-prime unit condition. Add t∈ℚ× to scaling. Cite the theorem-level sources above when promoting the literature discussion.

**Final decision:** ACCEPT-WITH-FIXES; “narrowed” is warranted. Bank Theorem B, Prop F/T with their exact scope, and the 4545 counterexample after the narrative fixes. Do not bank a general no-go for BM-based eventual existence or a compulsory counting/equidistribution route.
