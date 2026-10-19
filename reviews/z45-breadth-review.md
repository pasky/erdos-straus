# Z45 breadth review — mathematics and verdict calibration

Reviewed range: `42327de0..462290885b8cd715126dd3fc9735ae71726aac94` (all eight commits, nine memos, and their mathematical/computational support). Context: `FRONTIER.md` §§3–4,6. This is an independent review, not an endorsement of the memos' self-reviews.

## Decision

**No fatal error found in the central new mathematical claims.** The requested exact examples reproduce. In particular, the smooth-locus double cover, quadratic function-field classification, Cox-model theorem, 8/131 decomposition, and 31121/43 counterexample survive scrutiny. Their significance is substantially narrower than “nine partial approaches to ES.” Most are successful falsifications of proposed approaches, elementary reformulations, or finite diagnostics.

**No memo merits a promise score above its own for proving ES.** Étale descent has the strongest genuinely live *obstruction-side computation*: compute the extra Brauer classes upstairs with image-integrality. Its existing 2/5 already recognizes that. I would reduce critical chaos from 2/5 to **1/5 as an ES route**, while retaining its value as a rigorous model diagnostic. The remaining seven 1/5 scores are appropriate upper bounds, not evidence of seven developed routes.

The main corrections are scope/label corrections, not repairs of failed central proofs:

1. `z45_euler_systems.md:138`: **kernels of the trace maps are not a loophole** in Lemma 3.2. Those maps are already arbitrary homomorphisms. Annihilating Euler operators or nonfaithful extraction can escape; noninjective traces alone cannot.
2. `z45_recent_pointwise_tools.md:33`: explicitly assume **p ≡ 1 (4)** before claiming `(P²−p)/4` is an integer for odd P. The later trace theorem has this hypothesis; the opening Lucas dictionary should too.
3. `z45_critical_chaos.md:239`: the summability boundary needs a remainder hypothesis, not merely `μ∼c(log p)^d`. At `dβ=ac^β=1`, `μ=log p` diverges whereas `μ=log p+√log p` gives a convergent prime sum. The existing “absent extra logarithmic savings” caveat points in the right direction but is not a precise hypothesis.
4. Separate **“tested construction collapses”**, **“new side theorem”**, and **“unspecified possible future theory.”** Repeated PARTIAL labels and “new-theory” headings blur these categories. An unspecified class-sensitive theorem equivalent to the missing ES lower tail is not partial progress toward that theorem.

None of these points invalidates the principal computations or supplies an ES contradiction.

## 1. Étale descent

**Central claims: sound, relative to the stated standard geometric inputs. This is the most substantial new memo.**

### Fundamental groups and covering

The line-arrangement calculation is the right calculation, not an inference from rationality. The four projective lines are in general position. Their complement has commuting meridians with `h+l₁+l₂+l₃=0`. Retaining the exceptional divisor above each `H∩L_i` imposes `h+l_i=0`. Substitution gives `2h=0`, hence geometric `π₁(X)=Z/2`. Adding E kills h; contracting the simply connected exceptional curve does not introduce loops. Thus `π₁(Ũ)=π₁(U)=1` is credible for the stated interiors. The determinant check alone would only compute an abelianization; the preceding arrangement argument is essential and is present.

For `Y_d: mdABC=n(A+B+C)`, the map `(dBC,dAC,dAB)` is correct. In particular

`dA²=(m/n)yz−y−z`

and its cyclic analogues prove finiteness and generate the even invariant ring. Simultaneously vanishing derivatives force `A=B=C≠0` and contradict the cubic. The sign involution has only the origin as a fixed point. The degree-two quotient is therefore étale off the node, and the computed fundamental group makes it universal there. The squareclass is `[xyz]`; at an axis it extends as `[-a]`, not as the unnormalized equation `w²=xyz`.

The exceptional multiplicity `3E` in `div(xyz)` correctly explains why the cover is not étale on the resolution. These distinctions are load-bearing and handled correctly.

### Arithmetic and Brauer assertions

I checked the proof structure of the good-base and full-Z statements. Normality plus generic restriction excludes hidden generically trivial covers; the sections control constant ramification. Over `Z[1/2n]`, the explicit split double cover and trivial action on its Z/2 deck group support the asserted product. For odd n, reduced generically smooth special fibres plus the hypersurface S2 property support normality of the literal full-Z model. These are geometric proofs, not computational certificates.

The ordinary smooth-locus Brauer computation is consistent with the BL data in `GEOMETRY_ES.md` §1: `[E]=−2[L]`, `Pic(X̄)=Z/2`, and purity across `E≅P¹` leaves geometric Br unchanged. The symbols `(c,xyz)` realize the algebraic classes; the invariant geometric order-two class is lifted by α. The global-squareclass construction kills the former by reciprocity and balances α at the chosen prime dividing n and infinity. Axes are legitimate **local** points with smooth generic image. No signed global solution is being transported to a positive one.

The conclusion is deliberately only `Br(X)` plus finite descent. It does **not** imply orthogonality to all of `Br(Y_d)`. The memo correctly retains this gap. Likewise the étale–Brauer equality on U and Ũ depends on geometric simple connectedness, not merely on their being rational surfaces.

### 3361 certificate and calibration

Reran the complete factor enumeration and independent x,y enumeration: **15 unordered points, 12 squareclasses**, exactly the listed classes. Each squarefree class has an odd prime factor outside `{3361}`. Consequently every associated quadratic twist ramifies outside `2·3361`. Pulling back the good-model torsor along an S-section would give an S-unit squareclass, so none of these points can be a section of that smaller model. This is a valid and useful false-obstruction diagnostic. It is not an obstruction to ES and not a proof that covering coordinates must be integral.

The ordinary-BM/finite-descent adeles at 8/131 and 8/241 also check. A failure of BM on **one** twist would not decide either input: the union over all positive twists matters. The finite bound on twists occupied by actual solutions is not a bound on adelically surviving twists.

**Verdict:** retain 2/5 for the obstruction-side problem, with no ES-score increase. Compute `Br(Y_d)` and its evaluations before another broad descent survey. Strengthen precise comparison/purity citations before promoting this to a permanent theorem ledger; the current reference-from-memory is not itself verification of a theorem number. No claim of literature priority is warranted by a repository search.

## 2. Transfer logic

**Five-curve theorem: checked and sound.** For irreducible `P=T²+bT+c`, the unique minimal denominator is `X=T+x`; `E=(x−b)T−c`. Constant E gives `c=−1,−2`. In the linear case, equal-degree divisor pairs are equal and cannot work because `gcd(E,PX)=1`. Unequal degrees force `lc(E)=1`, so `x=b+1`. At the root T=c the four divisors evaluate to `1,v,cv,cv²`, with `v=c+b+1`. Their six pair sums give exactly the five conditions claimed, with repeats. Each locus has at most q coefficient pairs. The argument works in odd extension fields too; the numerical independent-engine comparison only tests prime fields and should not be mistaken for extension-field verification.

**All-characteristic NC estimate: checked.** At least one denominator is divisible by P, so at most two can have degree `d−k`. Their monic leading coefficients force exactly one such denominator, including characteristic two under NC. For each X there are two P-divisibility patterns for a,b; the candidate E divides one nonzero polynomial of degree at most 2d, with its scalar fixed by the leading-coefficient requirement. The deliberately loose `2·64^d q^(d−k)` bound is valid. Dividing by the fixed-d irreducible count gives `O_d(q^(−k))`. This is **fixed d**, not a statement uniform in growing d and not the fixed-numerator integer asymptotic.

Reran the toy: **474 small irreducibles compared to the separate divisor engine, no mismatch**; q=503 gives 1,250 successes out of 126,253. Large rows evaluate the proved formula rather than independently searching all denominators.

**Vaughan compression: valid and standard.** E_L is a uniformly computable finite set because ES is a bounded search. Given L, compute its cardinality and decode a fixed-length rank. Conditional prefix-freeness incurs only constant interpreter overhead; no extra logarithmic rank-length term is needed. Vaughan's quoted bound then gives `K(p|L)≤L−cL^(2/3)+O(1)`. This is an enumeration corollary, not an efficiently computed invariant, arithmetic inverse theorem, or route to contradiction. The least-counterexample O(1) observation underscores that limitation.

The AKE/PAC/overspill distinctions are sound: a local valued-field sentence does not express simultaneous integer integrality and positivity; `∏F_q[T]` need not be `K[T]`; an arbitrary PA model is not an elementary extension of standard arithmetic; overspill reaches some nonstandard initial interval, not every prescribed nonstandard p. The bounded-search formulation of ES and the finite-population recovery argument also check.

**Novelty/calibration:** `BRAINSTORM/ff_erdos_straus.md` already contains the large-q negative result. The NC extension and explicit quadratic locus are useful side results; rank coding is folklore. The memo acknowledges this. Keep 1/5; HT is the existing lower-tail hypothesis renamed, not a new conditional reduction.

## 3. Critical chaos

**The bounded-variance and Cox zero-law proofs survive review.** This is not just a numerical saturation claim.

For even m, coprime unordered splittings contribute `2^ω(m)/2`, and `φ(km)=kφ(m)` for k=4,8. Grouping by squarefree kernel produces local weights `E_q=1+O(q⁻²)` and `O_q=2/q+O(q⁻²)`. Thus `∏(E_q²+O_q²)` converges and Walsh orthogonality gives uniformly bounded variance. The s=1 coefficient is deterministic: T itself is not exactly centered, but the variance formula excludes that coefficient correctly.

Bounded variance **alone would not justify** the asserted zero law. The memo supplies the needed stronger argument: `||T_H||_(2r)=O(log²(2r))`, obtained by splitting primes at 2r and dominating even moments coefficientwise. This yields uniform exponential integrability. Together with L² convergence it legitimizes

`P(Z_H=0)=e^(−A_H) E[e^(T_H)] ∼ C_k e^(−A_H)`.

The finite nonzero limiting constant can also absorb the deterministic square-kernel contribution if the comparison Poisson law is normalized to the actual mean rather than the principal mass A_H. Fixed finite sign conditioning preserves the argument. Summability over primes and the first Borel–Cantelli conclusion need no independence between heights.

**What this does not prove:** no bounded variance theorem for the actual divisor-count error, no arithmetic Poisson hole law, and no exclusion of critical correlations in the remaining class/height data. The model *assumes* conditional Poisson occupancies. At squares the all-plus-sign configuration is a deterministic diagnostic, not a positive-probability infinite-sign event. The 2048-state calculation is a conditional-expectation projection, and conditional Jensen has the direction stated: its zero probability is a lower bound for the full Cox mixture.

Reran the entire model, including the variance and CRT tables. Its numerical probabilities remain floating-point EVIDENCE. The CRT-Bernoulli model does not inherit the full infinite-sign T1 property and does not reproduce the full ES failure set. The proposed growing-order inverse-moment estimate would indeed eliminate all sufficiently large arithmetic zeros, but proving it is essentially the missing extreme-tail theorem.

**Novelty/calibration:** the L(1)-scale shared-sign model already appears in `BRAINSTORM/anal_euler_product_law.md:3–13`; the rigorous Walsh/exponential-moment calculation is a real increment. It is a negative result about that model, not evidence for a new positive mechanism. Recommend **1/5 for ES**, not 2/5. Tighten the boundary summability statement noted above.

## 4. Interlacing and stability

**Yes: the forest-signing claim is precisely trivial switching equivalence on trees.** Root each component and recursively assign vertex signs. Then `A_s=D_s A D_s`. In fact the particular signing `χ(u)χ(v)` is a switching coboundary on *any* graph. Cycles alone cannot repair that encoding. The memo explicitly says all this and attributes gauge removal to elementary classical facts; it does not actually present it as a new MSS theorem.

The nontrivial diagnostic is failure of the proposed class projection. At p=1097, the four primes of `4p+1` are all 3 mod 4, so the target sector is `e₁+e₃`, vanishing at `(i,i,i,i)`. At p=2521, the two target divisors 87 and 1275 produce `z²+z⁴`. Both are exact counterexamples to stability preservation, not counterexamples to ES. The character-matrix average `x²−2ax+1` is non-real-rooted when `|a|<1`; real-rooted leaves therefore do not suffice. The C₂ toy classification follows by real specialization to three active variables. The matching/Laplacian and degree-one detectors merely put the already-unknown count into a polynomial coefficient/root.

Reran all 16 fixtures, componentwise characteristic-polynomial checks, and the independent edge enumerations. No discrepancy. The full squarefree example is particularly useful because the nonsquarefree unrestricted divisor polynomial need not even be stable initially.

**Calibration:** keep 1/5 at most. Archive the displayed constructions as **collapsed**, rather than treating an unspecified vector-valued lift as a partially developed ES method. The group-algebra recurrence is the familiar divisor dynamic program. There is no root-crossing estimate independent of the target predicate.

## 5. Euler systems

**Finite-support lemma: correct, elementary, and very narrow.** If `a_K=0` for all sufficiently large K and `T_k(a_(k+1))=a_k`, descending induction gives every a_k=0. The variant with `E_k(a_k)` requires injectivity of E_k on the relevant classes. No injectivity of T_k is used. Thus the sentence treating trace kernels as an escape should be removed or clarified; it contradicts the actual scope of the proof.

The positive-support bound `C≤(p+2)/4` is immediate from `p=4CuB−u−B`. The full-Type-II bound also checks: `p/4<x≤p/2`, `Y≤2x/(4x−p)≤(p+3)/6`, and `C=gcd(Y,Z)≤Y`. The canonical `C=cd` reconstruction uses `gcd(x,4x−p)=1`, valid because x<p. This extends the finite-support screen beyond the star line legitimately.

The multiplicative-level gcd formula and no-common-certifying-divisor consequence are correct. So are the ramified/unramified cyclotomic-unit norm formulas, centered Stickelberger distribution, and the 3361 counterexample to the obvious p-twist. The Heegner trace relation is correctly restricted to inert auxiliary primes prime to the existing conductor, with the separate coefficient prime distinguished from p. A nonzero seed and a positive integral extraction are still missing.

Reran both full-Type-II engines and the star engine. At 3361 the levels are C=5 and 290; the star tower is `0,1,0,0,…`, and the group-ring projection from 25 to 5 is not the required distribution. These demonstrate failure of *these* identifications, not an impossibility theorem for Euler systems.

**Calibration:** keep 1/5. The lemma is an elementary fact about eventually zero inverse systems, not new Euler-system technology. Ordinary Euler systems need not be faithful certificate detectors; their Euler operators need not be injective. A separate auxiliary conductor or nonfunctorial extraction is a genuine logical escape, but no arithmetic construction realizing it is supplied.

## 6. Prime-T1 duals

**The 8/131 count is correct:** 33 first-denominator fibres, 6 quadratic-kernel obstructions, 0 higher-only obstructions, and **27 budget holes**. I reran the full scan and the independent divisor/BFS toy. The six quadratic conductors and their one-fibre coverage reproduce. At x=17, `b=2227=17·131`, the bounded divisor residues mod 5 are `{1,2,4}`, missing target 3, while the generated subgroup is the entire unit group. This really excludes every kernel-annihilating character, not just the six tested quadratic ones. A faithful quartic character still detects the bounded-image hole, exactly as the memo says.

The quotient minima and overflow distance have the advertised restricted meanings. The BFS equivalence follows by splitting each exponent into its allowed part and overflow; it is not a shortest arithmetic proof or a Kolmogorov-complexity measurement. Calling B failures “solely” exponent failures should be read relative to the subgroup relaxation: a formal added exponent is not itself a new legitimate divisor of the original integer, let alone a sorted solution.

The Dirichlet escape theorem is also sound: a nonresidue p mod q has even order, so its powers contain −1 in the cyclic group. But q can exceed the finite window, and the powers can exceed the divisor budget. It therefore cannot exclude a prime T1 in a different, budget-sensitive language. The compatibility correction is right: literal pullback compatibility across every modulus divisible by 4 forces induction from modulus 4; T1 uses a varying reciprocity formula instead.

The complete scan reproduces all 53 supplied failures and the selected controls. Root-component failure is correctly separated from full five-slice failure; the square obstruction does not exclude mixed/scaled square solutions.

**Novelty/calibration:** `CAP_POINTWISE.md:109–128,202–227` already isolates subgroup freedom versus exponent budget. The new contribution is the finite anatomical census and restricted dual hierarchy. The δ≤1 target has no independent prime evidence when existing ES verification already supplies δ=0. Keep 1/5; no score increase for repackaging the cap gap.

## 7. Siegel dichotomy

**The 31121/43 counterexample is valid.** With `K=3·7²·53`, primitive root 3 gives logarithms `1,35,10` mod 42. The signed exponent box has 45 vectors and 37 residues; its complement is `{4,11,14,40,42}`. All odd-character phase costs are at least `25/42>1/2`. Hence the proposed weak single-character inverse criterion fails on an actual forced window, despite box cardinality exceeding group order. The boundary example at 9833/67 is also checked. Neither is an ES exception.

The phase-separation implication itself is valid, including the extremal-face qualification at equality. The Fourier formula counts exponent vectors, not distinct residues, and the memo uses the correct interpretation. Refuting this particular half-turn criterion does **not** refute all single-character arguments, let alone multicharacter inverse theory. The text generally preserves that distinction; retain it in summaries.

The three character objects really differ. Free-prime pretence of χ_p, characters of a tied window group, and an exceptional real character cannot be substituted for one another. The favourable exceptional-zero contribution increases certain free-prime window counts but supplies neither the factor multiset of K nor its target box membership. The sign bookkeeping and the conditional scope of the two-world statements are appropriate. None of the cited averaged statements recovers the prescribed arithmetic target.

Rebuilt and ran the C window census through 10⁷: **byte-for-byte equality** with the retained compressed CSV. Reran the Python analysis, including its 333 independent audits, fixture counts against the separate single-prime engine, and the entire phase-hole toy. All passed; 27 nonseparable toy failures reproduce. I did not regenerate the separate full f_II binary census; its spot-audit checks were rerun.

**Novelty/calibration:** the general dichotomy and anti-Siegel orientation are already in `hardness_law.md`, `bsB_sterile_pretentious.md`, and the balance/cap work. The local inverse counterexample is a worthwhile new negative diagnostic. Keep 1/5. Correlations and near-square strata do not furnish a causal or pointwise law; additional phase classification without an all-window arithmetic implication remains taxonomy.

## 8. Program synthesis

**Finite claims reproduce, but the mathematical novelty is small.** Reran all 924 programs and the independent verifier/extrapolation in a temporary output directory. All non-timing JSON fields and the certificate CSV match. The frozen policy has the reported 9,733 original certificates; the extra fixture overlaps the extrapolation, giving 82,887 distinct primes through 10⁷. The elementary parent baseline wins the mean and the held-out larger-range normalized tail. Factoring/generating whole divisor lists is correctly excluded from the charged metric, not silently claimed to be cheap.

The parent test follows from `p+r=qv`, so `p+r+v=(q+1)v`; no factoring is needed. The three certificate identities, their numerator-k generalizations, and the fixed-H sterile progression check algebraically. Parent cost is H₄−1, not H₄; even after that one-unit adjustment the data support the stated **finite** `H₄≤2(log p)²` claim.

**Relation to X_win must be stated precisely.** Searches in the pre-change tree locate `POINTWISE_SIZE.md:1132–1168,1332–1348`, `BRAINSTORM/greedy_algorithm_dynamics.md:57`, and `FRONTIER.md:527`. The campaign already proposes `a_min≪log p` and has data to 10⁸ and beyond. The new statistic is not literally identical: bounding both endpoints of a five-slice word implies a window `a_min≤2H₄`, but a small unrestricted window need not yield two small word endpoints. Also log² is not log. Thus this is a distinct constrained stopping-time formulation of the **old growing-search question**, not a rediscovered proof and not simply the same conjecture with a new name.

The elementary fixed-H obstruction does not refute a growing log² cutoff: its modulus itself grows exponentially in H. Conversely a finite census in which all endpoints are bounded by a small absolute number does not demonstrate an asymptotic escape from a finite menu. The named hard cases were training inputs; their success is not held-out evidence. The actual larger interval is held out and still favors the baseline.

**Calibration:** keep 1/5. The useful result is a negative synthesis benchmark and a factor-free search statistic. No drift/ranking invariant or new arithmetic scheduling advantage emerged. Do not upgrade this because it uses a different computational vocabulary.

## 9. Recent pointwise tools

**Pasten sterile embedding: correct and doubly blocked.** `a²=4Cp` forces `a=±2pk`, `C=pk²`. Every prime divisor of the odd number `a²+1` is 1 mod 4, so every divisor has the wrong mod-4 class. Independently, C≥p lies outside the positive star range. This rejects exactly the literal embedding, not other polynomial families or all height methods.

**BHV class claim: correct with the stated exclusions.** For odd `ℓ∤QD`, the ratio α/β lies in the split torus of order ℓ−1 or the norm-one torus of order ℓ+1. Exact rank t therefore gives `ℓ≡(D/ℓ) mod t`. BHV gives a primitive divisor for t>30; it does not choose inertness, and says nothing about division of the unrelated integer tp+1. Ordinary integer Zsigmondy supplies the plus class. The missing intersection is real, not an error caused by treating all reciprocity information as parity-only.

The trace-count converse checks: from `ℓ≡−1 mod4C`, reciprocity gives `(C/ℓ)=1`, including the 2-part, hence `(p/ℓ)=−1`. The Cayley map `P↦(P+√p)/(P−√p)` bijects F_ℓ with the norm-one torus minus 1. Exactly φ(t) traces have order t, and CRT supplies odd lifts not divisible by p. This is precisely an equivalence to already-existing prime certificates, not an independent way to force them. The index-4 embedding `U₄(1,−2Cp)=1+4Cp` only controls order 4, as advertised.

Reran the complete retained experiment: 80 small primes, the selected hard/near-square cases, both trace engines, controls, and Pasten substitutions. Counts reproduce. I spot-checked the retained primary statements for Pasten 2024/2026 and the polynomial extension, Green–Sawhney, Grimmelt–Merikoski, Koymans–Pagano, and the Smith source framework; the quoted scopes used to reject direct transfer are consistent. BHV's t>30 claim is corroborated by the retained Voutier correction, not independently proved or checked against the inaccessible primary BHV PDF. “PROVED (literature)” must continue to mean an attributed input, not a review of those entire proofs.

**Novelty/calibration:** `TORSION_FIRING.md:235–245` and `BRAINSTORM/y3_lucas_dickson_trace.md:9–15` already contain the primitive-divisor/order analogy and coupling problem. The source update, literal Pasten no-go, and exact trace multiplicity are increments. The correct observation that some modern factorization theorems are genuinely pointwise is useful, but does not make them class-sensitive on the prescribed side integer. Keep 1/5; add the missing p≡1 (4) assumption to the opening dictionary.

## 10. Cross-memo conclusions and verification record

The memos mostly **do acknowledge** their folklore and campaign predecessors. Do not manufacture a novelty violation where the text expressly disclaims one. The danger is downstream compression: turning “new to this repository” into new mathematics, “Cox-model theorem” into arithmetic tail control, “kernel-dual exclusion” into absence of all prime T1, or “PARTIAL” into an active ES mechanism.

| Memo | Own score | Review: ES promise | Actual retained value |
|---|---:|---:|---|
| étale descent | 2 | 2, obstruction-side only | Explicit universal cover; model-integrality trap; concrete remaining Brauer computation |
| transfer logic | 1 | 1 | Quadratic locus/NC extension; correct transfer and coding distinctions |
| critical chaos | 2 | 1 | Rigorous rejection of criticality in this particular BM surrogate |
| interlacing | 1 | 1 at most | Exact instability counterexamples; signing construction closed |
| Euler systems | 1 | 1 at most | Narrow finite-support screen; no compatible extraction |
| prime-T1 dual | 1 | 1 | Measured subgroup/budget separation; not an inverse theorem |
| Siegel dichotomy | 1 | 1 | Counterexample to the specified local inverse criterion |
| program synthesis | 1 | 1 | Reproducible benchmark, baseline wins; old growing-search bottleneck |
| recent tools | 1 | 1 | Accurate pointwise-versus-class distinction and intersection dictionary |

For form and substance, the most useful revision is to put one short **new result / old ingredient / failed construction / genuinely open next calculation** box at each memo's start. The repeated 17-screen tables are not independent evidence. Definitions, elementary identities, external theorem quotations, exact computations, and extrapolation should remain visibly different evidentiary categories. No extra positive result follows from the sheer number of certificates or archived source lines.

All review executions used `ulimit -v 8000000`, bounded timeouts, and `uv` for Python; NumPy runs used `OPENBLAS_NUM_THREADS=1`. Scripts were inspected first: sparse/componentwise matrices, bounded coefficient loops, fibre-at-a-time subgroup sets, and O(H) sieves, not unbounded Cartesian products. Existing independent engines already covered the requested arithmetic checks, so no redundant permanent test was added.

Reexecuted successfully:

- `z45_etale_descent_check.py`, `z45_transfer_logic_toy.py`, `z45_interlacing_stable_check.py`, `z45_euler_systems_scan.py`, `z45_recent_pointwise_tools_scan.py`, `z45_critical_chaos_model.py` (180-second limits).
- `z45_prime_t1_dual_scan.py` and `z45_prime_t1_dual_toy.py` with `uv run --with python-flint` (240/60-second limits).
- `z45_program_synthesis_search.main()` and `z45_program_synthesis_verify.main()` with both OUT paths redirected to a fresh temporary directory; compared outputs excluding CPU timings (180-second limit).
- C Siegel window census at 10⁷, comparison to `gzip -cd .../windows.csv.gz`, and `z45_siegel_dichotomy_analyze.py` after compiling its single-prime audit executable (240/300-second limits).

Reruns left the retained research/data files unchanged. These executions verify finite assertions; the geometric, probability, and function-field generalizations were reviewed by their arguments. I did not independently referee every cited external paper or the campaign's pre-existing deep inputs. **No ES lower-tail mechanism, proof, or disproof emerges from this batch.**
