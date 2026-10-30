# L4 — Integral and rational points; automorphic forms

## §0 Summary
- **New since 2026-09-28:** none verified in this lane; source-checked results are older audited work.
- **Transferable structural features:** explicit Brauer-class/local-invariant analysis (already used in campaign); density-of-prime signs identify an Eisenstein newform, but do not certify one prescribed coefficient.
- **Campaign verdict changes:** none. No verified result supplies a pointwise lower bound at a prescribed ES prime; B2/B6 remain.

## §1 Verified entries

### Bright–Loughran: the ES surfaces and their integral Brauer–Manin obstruction

Martin Bright and Daniel Loughran, “Brauer-Manin obstruction for Erdős–Straus surfaces,” arXiv:1908.02526v2 (last revised 12 May 2020); *Bulletin of the London Mathematical Society* 52 (2020), no. 4, 746–761, DOI 10.1112/blms.12374. Source: arXiv HTML v2, accessed 2026-10-30; excerpt: `sources/z52/points_automorphic/bright-loughran.txt`.

- **Verified statements.** Theorem 1.8: for every integer `n ≥ 2`, the Brauer–Manin set of the positive-real/integral-adic set is nonempty (hence no BM obstruction to the integral Hasse principle for this formulation). Theorem 1.9: the rational points do not have dense image in the BM set, so BM is not the only obstruction to strong approximation. Lemma 3.10 proves finiteness of integral points off the displayed exceptional lines, and in particular finiteness of positive integral points for each fixed `n`. These are results about individual fixed surfaces, not a uniform theorem solving ES for every `n`.
- **Status:** Published; the statements above were checked against the paper’s HTML. Note the explicit `n ≥ 2` range in the paper’s introduction; do not extend it to `n=1`.
- **Relation:** Already covered in `GEOMETRY_ES.md` §§1, 3, 6 and `LITERATURE_AUTOMORPHIC.md` §2; it does not change the campaign verdict.

### Linowitz–Thompson: signs of Eisenstein-newform Hecke eigenvalues

Benjamin Linowitz and Lola Thompson, “The sign changes of Fourier coefficients of Eisenstein series,” arXiv:1305.6356v1, submitted 28 May 2013. Source: arXiv abstract, accessed 2026-10-30; excerpt: `sources/z52/points_automorphic/linowitz-thompson.txt`.

- **Verified statement.** The abstract says they prove individual and statistical results on how signs of Hecke eigenvalues of an Eisenstein newform determine the newform; in particular, signs on any prime set of density greater than `1/2` determine it. This is a uniqueness/sign-pattern theorem, not positivity of each individual Fourier coefficient. No claim about an arbitrary growing-level Eisenstein combination is made here.
- **Status:** arXiv preprint; publication metadata not independently checked in this lane. Abstract accessed; theorem text not accessed.
- **Relation:** `LITERATURE_AUTOMORPHIC.md`, `METAPLECTIC_ES.md`; no new pointwise positivity input or campaign verdict change.

### Harpaz: integral points on affine-conic pencils / log K3 surfaces

Yonatan Harpaz, “Integral points on conic log K3 surfaces,” arXiv:1511.04876v2 (15 March 2017); *J. Eur. Math. Soc.* 21 (2019), no. 3, 627–664, DOI 10.4171/JEMS/847. Source: full arXiv HTML v2, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/harpaz-logk3.txt`.

- **Verified statement.** Theorem 3.1.12 gives sufficient conditions for an `S₀`-integral point on a specified pencil of affine conics: Condition (D), an appropriate integral adelic point satisfying the theorem’s local valuation and splitness conditions, and orthogonality to the vertical Brauer group. The proof adapts Swinnerton-Dyer descent-fibration and uses Green–Tao–Ziegler for admissible fibers over `Q`, avoiding Schinzel in this setting. This is a conditional-on-explicit-hypotheses existence theorem, not a theorem for arbitrary log K3 surfaces.
- **Status:** Published. The precise theorem/hypotheses were checked in source HTML.
- **Relation:** `GEOMETRY_ES.md` §§3, 6; `BRAINSTORM/z31_integral_points_cubics.md`. It does not apply to ES: fixed `U_n` has only finitely many positive integral points (indeed each fiber is finite), while ES is a value-set question over varying `n`; its available pencils are not the conic log-K3 setup with Harpaz’s hypotheses.

### Wilsch: height asymptotics on a log Fano threefold

Florian Wilsch, “Integral points of bounded height on a log Fano threefold,” arXiv:1901.08503v3 (21 May 2025); *Int. Math. Res. Not.* 2023, no. 8, 6780–6808, DOI 10.1093/imrn/rnac048. Source: full arXiv HTML v3, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/wilsch-logfano.txt`.

- **Verified statement.** Theorem 1.1 counts integral points of log-anticanonical height at most `B` on two specified open subsets of the blow-up of `P³` along a conic. It gives `N₁(B)=(20/(3ζ(2)))B log B+O(B)` and `N₂(B)=cB log B+O(B(log log B)²)`, with `c=(20/3)∏ₚ(1−2/p²+1/p³)`. Proof uses universal torsors. These are global asymptotics on fixed varieties, not pointwise lower bounds on each member of a varying family.
- **Status:** Published; theorem and constants checked in source HTML.
- **Relation:** `GEOMETRY_ES.md` §6; `LITERATURE_AUTOMORPHIC.md` §2. ES asks for a lower bound at each fixed numerator, with only `≍log²p` candidate events (B2); a height asymptotic after summing points on one fixed threefold does not supply it. ES's compactified surface is not this log Fano threefold.

### Santens: integral Manin conjecture proved for toric varieties

Tim Santens, “Manin’s conjecture for integral points on toric varieties,” arXiv:2312.13914v2 (1 August 2025); no journal reference listed in the arXiv record. Source: full arXiv HTML v2, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/santens-toric.txt`.

- **Verified statement.** The paper proposes an analogue of Manin’s conjecture for integral points of bounded height on log Fano varieties, predicts a leading constant, and proves the conjectural asymptotic for toric varieties (Theorem 1.1). The proof is harmonic analysis on universal torsors. This is a height-ordered asymptotic on fixed toric varieties, not a pointwise result across arbitrary integral models.
- **Status:** Preprint (v2). Abstract, metadata and Theorem 1.1 were accessed; no publication metadata is claimed.
- **Relation:** `GEOMETRY_ES.md` §1, Remark 1.10, and §6; `LITERATURE_AUTOMORPHIC.md` §2. The ES resolution is explicitly non-toric in the relevant integral model and has no extending torus action; see `GEOMETRY_ES.md` §1. Toric asymptotics therefore do not apply, and their averaging in height would not force a point at each numerator.

### Loughran–Mitankin: integral Hasse principle and strong approximation for Markoff surfaces

Daniel Loughran and Vladimir Mitankin, “Integral Hasse principle and strong approximation for Markoff surfaces,” arXiv:1807.10223v3 (29 April 2019); *IMRN* 2021, no. 18, 14086–14122, DOI 10.1093/imrn/rnz114. Source: full arXiv HTML v3, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/loughran-mitankin-markoff.txt`.

- **Verified statement.** The paper computes Brauer–Manin phenomena in the Markoff family. For example, Corollary 5.11 states that if a prime `p>5` divides `m−4` and `m−4` is nonsquare in `Qₚ`, then there is no BM obstruction to the integral Hasse principle for the corresponding surface (under the paper’s set-up). The paper also constructs BM obstructions to integral Hasse principle and strong approximation. Its statistical/family statements concern parameters/surface families, not all members having integral points.
- **Status:** Published; the cited corollary and surrounding setup checked in source HTML.
- **Relation:** `BRAINSTORM/z31_markoff_chen.md`, `BRAINSTORM/z38_markoff_precedent.md`, `GEOMETRY_ES.md` §6. This is a useful BM/automorphism precedent, not an ES transfer: Markoff has Vieta dynamics and its own parameter-family structure; ES has no such infinite integral orbit mechanism, and fixed `U_n` has finite positive integral points (`GEOMETRY_ES.md` §§3,6).

### Lyczak: order-five BM obstructions in log K3 families

Julian Lyczak, “Order 5 Brauer–Manin obstructions to the integral Hasse principle on log K3 surfaces,” arXiv:2005.14013v1 (28 May 2020); no journal reference identified in the arXiv record. Source: full arXiv HTML v1, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/lyczak-order5.txt`.

- **Verified statement.** Theorem 4.6 gives a complement of a hyperplane section in a degree-5 del Pezzo surface that has points over `Q` and every `Zₗ` but an order-5 BM obstruction to integral points. Theorem 4.7 counts 228 of the `11⁶−1` nonzero hyperplane reductions in that construction with an obstruction. The family supplies explicit counterexamples and a finite-field parameter count, not a pointwise existence theorem.
- **Status:** arXiv preprint; source theorem checked. Publication status not verified.
- **Relation:** `GEOMETRY_ES.md` §1 and `BRAINSTORM/z31_integral_points_cubics.md`. It demonstrates higher-order algebraic BM behavior, but ES already has its exact BM analysis (`GEOMETRY_ES.md` §1); a BM obstruction calculation does not meet B2's integral-point forcing requirement.

### Zhang: positive integral points on acyclic cluster varieties

Robin Zhang, “Positive integral points on acyclic cluster varieties,” arXiv:2503.08800v4 (28 September 2026; initially submitted 11 March 2025); no journal reference listed. Source: full arXiv HTML v4, accessed 2026-10-30; excerpt `sources/z52/points_automorphic/zhang-cluster.txt`.

- **Verified statement.** Theorem B(2) determines exact positive integral point counts for the finite-type affine varieties associated to generalized Cartan matrices, including exactly 4,400 for type E₇ and 26,952 for E₈. The proof combines effective height bounds and exhaustive computation. Corollary A gives specified infinite positive-integral families including log K3 equations `xyz=G(x,y)` in every degree greater than 3. These are structural cluster/frieze families and a finite-type exact classification, not all fibers of a general cubic surface family.
- **Status:** Preprint v4, recent revision dated 2026-09-28.
- **Relation:** `GEOMETRY_ES.md` §§2–3 and `BRAINSTORM/z31_integral_points_cubics.md`. It is genuinely new in the window but does not alter the verdict: the proved mechanisms use cluster exchange/frieze recurrence and explicit bounded enumeration; the ES affine cubic is not given such a cluster model, and no theorem supplies pointwise coverage of its numerator parameter.

## §2 Structural-feature table

| Problem | Solvable structural feature | Does ES share it? | Transfer verdict |
|---|---|---|---|
| Bright–Loughran: Brauer groups/local obstructions on each `U_n` | Explicit surface geometry and a computable transcendental Brauer class; local invariants constrain solutions and identify BM behavior. | **Partial:** ES shares the exact surface and class, but Thm 1.8 only establishes BM-set nonemptiness; B2 still asks for an actual integral point. `GEOMETRY_ES.md` §1. | **Known-dead as a standalone proof route** (`GEOMETRY_ES.md` §§1,6; `BM_CORRECTED_COUNT.md`): BM alone does not give integral points; strong approximation fails by Thm 1.9. |
| Linowitz–Thompson: identify Eisenstein newform from signs | Multiplicativity/Hecke structure turns signs across a positive-density set of primes into a uniqueness fingerprint. | **No:** ES needs positivity/existence at one prescribed prime and only polylogarithmically many candidate events; it has no supplied positive-density prime set. B6 and B2. | **None:** theorem is sign-pattern uniqueness, not positivity of individual coefficients or a lower bound for an ES coefficient; `METAPLECTIC_ES.md` already treats ES’s Eisenstein-only normal form. |

## §3 New candidates

None. The source-verified results either restate audited ES geometry or concern sign patterns across a positive-density set of primes. Neither supplies the required single-object lower bound for a prescribed prime with expected count `≍ log² p`; proposing a transfer would evade B2/B6 rather than address them.

## §4 Additional individually checked leads

### Chambert-Loir–Tschinkel: bounded-height integral points on additive-group compactifications

Antoine Chambert-Loir and Yuri Tschinkel, “Integral points of bounded height on partial equivariant compactifications of vector groups,” arXiv:0912.4751; *Duke Math. J.* 161 (2012), no. 15, 2799–2836, DOI 10.1215/00127094-1813638. Source: full arXiv HTML; excerpt `sources/z52/points_automorphic/chambert-loir-tschinkel-integral.txt`.

- **Verified scope/method.** The abstract states asymptotic formulas for bounded-height integral points on partial equivariant compactifications of vector groups. The paper sets up counts for a chosen integral model and line-bundle heights, then uses Fourier transforms, Poisson summation and height zeta functions. This is a height-ordered global count on a specified group compactification, not a pointwise lower bound in a prescribed parameter family.
- **Relation:** relevant antecedent for height-counting methods; Derenthal–Wilsch explicitly invoke it for the log-anticanonical partial compactification of `G_a^3`. It does not by itself transfer to ES's individual numerator question.

### Cao–Xu and Wei: strong approximation for toric varieties

Dasheng Cao and Fei Xu, “Strong approximation with Brauer–Manin obstruction for toric varieties,” *Ann. Inst. Fourier* 68 (2018), no. 5, 1879–1908; Dasheng Wei, “Strong approximation for a toric variety,” arXiv:1403.1035v3. Source: Wei full HTML; excerpt `sources/z52/points_automorphic/cao-xu-strong-approx.txt`.

- **Verified result.** Wei’s theorem states that for smooth toric `X` with `kbar[X]^×=kbar^×` and codimension-at-least-two closed `W`, `X\\W` satisfies strong approximation with algebraic Brauer–Manin obstruction off any chosen place `v₀`. Wei’s introduction identifies the Cao–Xu result as strong approximation with BM obstruction off all infinite places for any toric variety, without that geometric-units hypothesis. The former is checked directly; Cao–Xu is verified via Wei’s explicit bibliographic characterization, not its original text.
- **Relation:** the ES resolution discussed in `GEOMETRY_ES.md` is not toric in the relevant integral model, and approximation statements do not imply the required integral point on each prescribed ES surface.

### Colliot-Thélène–Wittenberg: affine cubic-surface Brauer groups and integral points

Jean-Louis Colliot-Thélène and Olivier Wittenberg, “Groupe de Brauer et points entiers de deux familles de surfaces cubiques affines,” *Amer. J. Math.* 134 (2012), no. 5, 1303–1327. Source: checked later-paper citations and theorem use in `sources/z52/points_automorphic/ct-wittenberg-cubic-surfaces.txt`.

- **Verified at citation level.** The full text of “Integral points on symmetric affine cubic surfaces” (arXiv:2204.13472v2), §8, explicitly applies CTW12 Theorem 4.1a to the assertion that sums of three cubes have no integral Brauer–Manin obstruction to the Hasse principle; §§7.1 and 8 also cite CTW12 Proposition 3.1 and Lemma 3.2 for boundary-residue/Brauer arguments. This is not an independent full-text audit of the 2012 original, so the source level is distinguished.
- **Relation:** a direct affine-cubic/Brauer precedent, but a no-BM-obstruction theorem is not an unconditional integral-point existence theorem and does not yield ES pointwise coverage.

### Derenthal–Wilsch: Iitaka fibrations and integral points on spherical threefolds

Ulrich Derenthal and Florian Wilsch, “Iitaka fibrations and integral points: a family of arbitrarily polarized spherical threefolds,” arXiv:2505.10245v1 (2025). Source: full arXiv HTML; excerpt `sources/z52/points_automorphic/derenthal-wilsch-iitaka.txt`.

- **Verified result.** Theorem 1.3/Proposition 4.8 gives Manin-type bounded-height asymptotics in the adjoint-rigid case and a sum of fiber contributions over the Iitaka fibration in the non-rigid case, for their specified spherical log Fano threefold family. Proof includes explicit universal-torsor counts. Their §4.3 identifies the log-anticanonical partial `G_a^3` case as previously treated by Chambert-Loir–Tschinkel.
- **Relation:** precise example of geometric organization by Iitaka fibration and height asymptotics; it is neither an ES surface theorem nor a lower bound at an arbitrary prescribed ES parameter.

### Gvirtz-Chen–Mezzedimi: potential Hilbert property for elliptic K3 surfaces

Damián Gvirtz-Chen and Giacomo Mezzedimi, “Non-thin rational points for elliptic K3 surfaces,” arXiv:2404.06844v1 (2024). Source: full arXiv HTML; excerpt `sources/z52/points_automorphic/gvirtz-chen-mezzedimi-k3.txt`.

- **Verified result.** Theorem 1.1 proves that a K3 surface over a number field with two distinct elliptic fibrations has the potential Hilbert property: after finite extension, its rational points are not thin. Theorem 4.5 classifies the K3 surfaces with a unique elliptic fibration (92 families in Picard ranks 3–12 plus rank-2 cases; rank >12 guarantees multiple fibrations). The methods use elliptic fibrations, lattices, covers and Hilbert-property descent.
- **Relation:** this is rational-point arithmetic on projective K3 surfaces after field extension, not integral points on affine log-K3 surfaces, and gives no pointwise result for ES's varying coefficient.

### Integral points on symmetric affine cubic surfaces: non-obstruction is not existence

“Integral points on symmetric affine cubic surfaces,” arXiv:2204.13472v2. Source: full arXiv HTML; excerpt `sources/z52/points_automorphic/symmetric-affine-cubic-surfaces.txt`.

- **Verified result.** Theorem 1.1 and §8 study surfaces `f(u₁)+f(u₂)+f(u₃)=n`; Theorem 8.1 gives, outside its explicitly defined exceptional set, trivial Brauer group and no integral Brauer–Manin obstruction. For the pure sum-of-cubes case, the paper applies Colliot-Thélène–Wittenberg Theorem 4.1a. Example 10.9 gives a surface failing weak and strong approximation. The paper’s conclusion is expressly absence of an integral BM obstruction, not existence of an integral point for every `n`.
- **Relation:** directly relevant affine cubic/BM literature, but leaves the same logical gap as on ES: non-obstruction is weaker than integral-point existence, still more so than a positive ES point.

## §6 Automorphic positivity: what is actually proved for one coefficient?

This section separates positivity mechanisms in fixed quadratic-form theta series from the ES count. The source audit is the existing detailed survey `LITERATURE_AUTOMORPHIC.md` §§1, 6, with primary-text checks recorded there (including Kane’s archived text and the Blomer abstract); the statements below preserve its hypotheses rather than extrapolating them.

### Fixed ternary forms: Eisenstein main term versus cusp coefficient

- **Duke–Schulze-Pillot (1990), as quoted and applied in Kane.** For a positive-definite integral ternary form `Q`, sufficiently large locally represented integers that are primitively represented by its spinor genus, subject to bounded divisibility at anisotropic primes, are represented by the individual form. Mechanism: the weighted spinor-genus theta average supplies the Eisenstein/main term, while the individual-form difference is cuspidal; class-number lower bounds make the main term dominate. This is a sufficiently-large eligible-`n` existence theorem, not coefficientwise positivity for every locally represented `n`; the cutoff is ineffective through Siegel, and spinor-exceptional square classes/local hypotheses matter.
- **Blomer (2004).** For ternary `f` of level `N`, the checked uniform estimate is `r(f,n) − r(spn f,n) = Oε(N^A n^(1/2−1/28+ε))` with effective absolute `A` (and a sharper stated dependence in the paper’s other version). It bounds the cusp deviation from the spinor-genus mean; it is not itself positivity. To infer `r(f,n)>0`, one still needs a lower bound for the mean at that `n`, including local densities/class numbers, and the error must be smaller. No asserted theorem supplies prescribed ES-shaped variables/congruences.
- **Kane (2010) / Rouse (2014).** Kane’s Theorem 1.1 is a GRH-conditional upper bound on cusp coefficients of specified weight-`3/2` plus-space forms orthogonal to unary theta lifts; it is an error estimate, not a positive lower bound. The Duke–Schulze-Pillot criterion becomes effective under GRH as described in Kane. Rouse’s Theorem 7 uses GRH for the three remaining Kaplansky ternaries; his 451 finite-test theorem separately assumes the ternary universality conjecture. Neither result says that arbitrary coefficients of an arbitrary theta series are positive.
- **What “positivity” means here:** a nonnegative Eisenstein/local-density main term is positive only when all local representation densities are nonzero; a coefficient of the full theta series counts representations and is then a nonnegative integer by definition. The analytic proof is to show main term `>` absolute cusp error. Coefficient signs of a cusp form alone do not furnish this.

### The ES coefficient is not that coefficient

For ES, the naturally defined count is `R(n)=Σ_t R_t(n)`, where `R_t(n)` counts actual positive words `(t,u,v)` with `tuv−u−v=n`; hence `R_t(n)≥0` combinatorially, and `R(n)>0` is exactly the desired representation (with the campaign’s convention). The audited exact identity in `METAPLECTIC_ES.md` §1 writes each level via divisor sums on `N=tn+1`, restricted to `N≡1 (mod t)`, plus the boundary correction `β_t`. Its even-character divisor-sum component is not a holomorphic modular form, and the odd-character/theta-quotient term does not alone equal `R_t(n)`. The full coefficient is obtained by adding the pieces and subtracting the boundary term; signs/cancellation in that decomposition do not imply positivity.

Thus `R(n)` is not currently identified as the `n`th coefficient of a fixed holomorphic cusp-plus-Eisenstein theta series with a uniform positive local-density main term and a controlled cusp error. The identity does not produce the usual fixed ternary quadratic form, and ES varies its level/index and imposes positivity via `u,v,t≥2`. Positivity of the coefficient is tautologically equivalent to finding the ES word; no cited automorphic theorem makes it positive for every prime. Neither the classical half-integral-weight methods (Duke–Schulze-Pillot, Blomer, Kane, Rouse) nor the sign-pattern theorem of Linowitz–Thompson proves the needed single-coefficient assertion for this `R(p)`.

**Assessment:** source-verified positivity mechanisms exist for eligible coefficients of specified fixed ternary forms, by positive Eisenstein/local-density main terms dominating cusp errors. They are not a transfer candidate unless an explicit ES encoding with matching local densities, uniform cusp control, and exact positivity-preserving coefficient identity is first proved. No such encoding is present in the audited work.

## §7 Not accessed / could not verify / incorrect leads

- No 2021–26 follow-up proving a new pointwise or density result on the Erdős–Straus surfaces was verified in this lane. The initial search surfaced no such result; this is not an exhaustive database search. The already-audited Bright–Loughran and geometry citations remain in `GEOMETRY_ES.md` and `LITERATURE_AUTOMORPHIC.md`.
- Gvirtz-Chen remains **NOT VERIFIED** in this lane; no primary source or theorem text has yet been checked. Cao–Xu/Wei and Colliot-Thélène–Wittenberg have now been addressed above, with Cao–Xu and CTW explicitly marked as citation-level verification rather than fresh full-original audits.
- No 2024–26 theta-lift, Kudla–Millson, mock-modular, Borcherds, Bruinier–Funke, or half-integral-weight result certifying positivity of a single coefficient in a growing-level Eisenstein-type combination was source-verified. The leads in that clause remain **NOT VERIFIED**; no claim of nonexistence.
- Linowitz–Thompson: arXiv abstract accessed but full theorem text and publication metadata not checked; accordingly only the abstract-level statement is recorded.

