# Z45 — Étale descent distinguishes the node from its smooth locus

## (0) Summary

**PROVED (arguments below, relative to standard comparison/purity):** the geometric étale fundamental groups are `π₁(U_n)=1`, `π₁(Ũ_n)=1`, but `π₁(U_n^sm)=ℤ/2`. The missing double cover is explicit: `Y_d: 4dABC=n(A+B+C)`, mapping to `(x,y,z)=(dBC,dAC,dAB)`; remove the origin upstairs and downstairs. It is étale only off the node, and ramifies along the exceptional curve on the resolution. Consequently ordinary finite descent and étale–Brauer on the **singular surface or its resolution** add nothing to BL. Even on the smooth locus, finite descent and its entire ordinary Brauer group simultaneously leave positive integral adeles for every `n≥2`. **The remaining uncomputed refinement is Brauer–Manin on the double-cover twists themselves**, with integrality imposed on their images, not on `A,B,C`. The numerator-8 controls have explicit BM/finite-descent adeles despite zero positive integral points. A useful warning is computationally sharp at 3361: all 15 unordered ES solutions require a double-cover twist ramified at a prime outside `2·3361`; replacing the actual integral condition by smooth reduction outside `2n` loses every solution.

**Verdict: PARTIAL; promise 2/5 for closing a genuine obstruction-theory gap, not for proving ES.** The singular/resolution finite-étale route COLLAPSES; smooth-locus cover-Brauer remains a precise uncomputed question. No claim that all possible integral obstructions have been exhausted.

**Assessment (novelty):** `git grep` finds no prior computation of these π₁ groups or this covering in the campaign. Prior coverage is `GEOMETRY_ES.md`, `BRAINSTORM/padic_adelic_scaling.md`, `s9_fibration_level.md`, `z31_integral_points_cubics.md`, and the explicitly qualified assertion in `DISPROOF_AVENUES.md §1`. This is new to this repository, not a claim of literature priority. The geometry is an elementary consequence of the classical Cayley model.

## (1) Exact dictionary and the choice of space

**Definition.** Write

- `𝒰_{m,n}: mxyz=n(xy+xz+yz)` for the integral model, and `U_{m,n}` for its rational generic fibre;
- `U=U_{4,n}`, `X=U\{0}=U^sm`, and `Ũ→U` for the blow-up of the node, with exceptional curve `E≅ℙ¹`;
- `W_{m,n}=U_{m,n}(ℝ)_+ × ∏_ℓ 𝒰_{m,n}(ℤ_ℓ)`;
- `W^sm_{m,n}=W_{m,n}∩U_{m,n}^sm(𝔸_ℚ)`.

The last intersection uses the adelic topology of the smooth generic fibre. **It does not require smooth reduction at every finite prime.** Every positive rational integral point lies in it. For comparison, `𝒳=𝒰\{zero section}` over `ℤ[1/2n]` has a stricter integral-point condition: its sections may never specialize to the node outside `2n`.

**PROVED (BL/elementary).** `ES(n) ⇔ U(ℚ)∩W_{4,n}≠∅`; positivity forces `xyz≠0`, hence the same equivalence using `X` and `W^sm`. For fixed `m,n`, all these rational surfaces are isomorphic: sending `(x,y,z)` to `(mx/n,my/n,mz/n)` gives `XYZ=XY+XZ+YZ`. The integral lattices are different. In particular the map from numerator 8 to numerator 4 is `(x,y,z)↦(2x,2y,2z)`, not an isomorphism of the integral problems.

**PROVED (geometric presentation; GEOMETRY_ES Prop. 2.1).** In `ℙ²` with homogeneous coordinates `s₁,s₂,s₃`, let `L_i={s_i=0}`, `H={s₁+s₂+s₃=0}`, and `V_i=L_i∩H`. Blow up the three `V_i` and remove the strict transforms of `L_1,L_2,L_3`. The result is `Ũ`; the strict transform of `H` is `E`. Its contraction gives `U`, and deleting it gives `X`. The exceptional curves of the three blow-ups become the three coordinate axes.

**PROVED (B2 dictionary).** A cover is not an existence theorem. On the new cover, fixing a nonzero rational `A` gives

`(mdAB−n)(mdAC−n)=n(n+mdA²)`.

After clearing denominators this is again a divisor equation with congruence conditions tied to `A,d`. It does not control the class of a divisor of one fixed integer. The familiar target `4uBC−u−B=p`, equivalently `d₀|4Cp+1`, `d₀≡−1 (mod 4C)`, remains B2; the new `d` below is a **squareclass twist**, not that divisor `d₀`.

### Proposition 1 — all geometric finite quotients

**PROVED.** Over an algebraically closed field of characteristic zero,

| space | π₁^ét (already abelian) | connected geometric finite covers |
|---|---|---|
| `U` | `1` | only itself |
| `Ũ` | `1` | only itself |
| `X=U^sm` | `ℤ/2` | itself and one double cover |
| `T₀=U∩{xyz≠0}` | `Ẑ³` | finite-index sublattices, Kummer covers |
| BL's `V⊂Ũ`, which **contains part of E** | `Ẑ²` | torus isogenies |

**Proof.** Work over `ℂ` and apply the finite-cover comparison theorem (SGA 1, Exp. XII, Thm. 5.1; reference numbering from memory); extend to characteristic zero algebraically closed fields. The complement of the four general-position lines `H,L₁,L₂,L₃` has fundamental group

`⟨h,l₁,l₂,l₃ | all commute, h+l₁+l₂+l₃=0⟩ ≅ ℤ³`.

Here the standard line-arrangement van Kampen calculation has a commutator relation at every ordinary double point and the projective meridian relation; there are no triple points. Blowing up `H∩L_i`, retaining the exceptional curve minus its two boundary points, kills its meridian `h+l_i`. Thus

`π₁(X(ℂ)) = ℤ⁴ / ⟨h+l₁,h+l₂,h+l₃,h+l₁+l₂+l₃⟩ = ℤ/2`,

generated by `h`, with `l_i=−h`. Adding `E` kills `h`, giving `π₁(Ũ)=1`. Contracting connected `E≅ℙ¹` introduces no loop: van Kampen, or descent of a finite cover trivialized on the resolution, gives `π₁(U)=1`. The torus claim is BL Lemma 2.1. The four-line complement is exactly `T₀` by `s_i=1/x_i`, with the affine equation `Σs_i=m/n`. ∎

**CERTIFIED (sanity check, not a substitute for the proof).** The four meridian relations have determinant `±2`; the script checks this exactly.

### Proposition 2 — the double cover and all its twists

**PROVED.** For every `d∈ℚ*/ℚ*²`, choose a representative and put

`Y_d: mdABC=n(A+B+C)`,  `q_d(A,B,C)=(dBC,dAC,dAB)`.

`Y_d` is smooth; `q_d:Y_d→U_{m,n}` is finite of degree two, a quotient by `(A,B,C)↦(−A,−B,−C)`, with its only fixed point at the origin. Therefore

`q_d:Y_d\{0}→U_{m,n}^sm`

is a `μ₂`-torsor. For `xyz≠0` its class is

`δ(x,y,z)=[xyz]∈ℚ*/ℚ*²`,

and the point lifts to `Y_d` exactly when `xyz/d` is a square. These are all geometrically connected nontrivial finite étale coverings over `ℚ`, up to isomorphism over the base. Covers with a larger constant field are obtained after a finite field extension from this list; arbitrary finite étale covers are disjoint unions of such pieces. `Y_d\{0}` is geometrically simply connected.

**Proof.** The defining equations verify the map. In the invariant ring,

`dA² = (m/n)yz−y−z`, and cyclically,

so all even monomials are generated by `dBC,dAC,dAB`; these satisfy precisely the cubic relation. The displayed monic equations prove finiteness. If all partial derivatives of `mdABC−n(A+B+C)` vanish, then `mdAB=mdAC=mdBC=n`, so `A=B=C≠0`; the cubic would give `nA=3nA`, impossible in characteristic zero. The involution is free away from the origin. Proposition 1 then identifies this degree-two cover as universal. The twists are classified by `H¹(ℚ,μ₂)`. On `xyz≠0`, take `w²=xyz/d` and `(A,B,C)=(w/x,w/y,w/z)`. ∎

**PROVED (boundary caution).** On `Ũ`,

`div(xyz)=2(L₁₂+L₁₃+L₂₃)+3E`.

The cover ramifies along `E`; it is **not** finite étale on `U` or `Ũ`. On an axis `(a,0,0)` of `X`, its extended class is `δ=−a`, since the fibre satisfies `A=0`, `B+C=0`, `dBC=a`. The naive equation `w²=xyz` without normalization is not the étale torsor at the axes.

**PROVED (which boundary-ramified covers have been classified).** For the resolved compactification with boundary only the three strict `L_i`, the interior is `Ũ` and there are no geometric finite covers étale on that interior. If `E` is also boundary, the interior is `X` and the sole connected nontrivial geometric cover is the displayed double cover. If the axes are also removed, the four-line complement has all finite abelian covers described by Kummer monomials in three independent units, e.g. `s₁,s₂,s₃` on `Σs_i=m/n`. This classifies covers for these **specified** boundary divisors in characteristic zero. Allowing arbitrary extra branch divisors is a different, unlimited question, not a classification of torsors on `U`.

### Arithmetic integral/log models

**PROVED (ordinary finite étale groups over the good base).** Put `S=Spec ℤ[1/2n]`, for numerator 4. Then

`π₁(𝒰_S) ≅ π₁(Ũ_S) ≅ G_{ℚ,S}`,

`π₁(𝒳_S) ≅ (ℤ/2) × G_{ℚ,S}`.

Here `G_{ℚ,S}` is the Galois group of the maximal extension unramified at finite primes outside `2n`; ramification at the real place is allowed. These are full arithmetic groups, not the assertion that arithmetic covers are trivial. The nonconstant double-cover twists extending étale over `𝒳_S` are indexed by `S`-unit squareclasses, with the remaining finite covers coming from these and finite étale base extensions.

**Proof.** The models are normal; finite covers are determined by their generic restrictions, and restriction to the generic fibre gives a surjection on π₁. The constant-cover assertions follow from Proposition 1 and a section. For `𝒳`, the section `(-1,0,0)` lifts to `(0,1,−1)` on `Y₁`, and the free quotient construction extends over `S`. Thus the geometric factor `ℤ/2` survives, the section splits the arithmetic part, and its action on `ℤ/2` is trivial. Constants and this double cover realize the indicated product; no extra cover can be invisible generically. ∎

**PROVED (an additional full-ℤ statement for the prime problem).** For odd `n`, `𝒰_{4,n}` over `ℤ` is normal and `π₁(𝒰_{4,n})=1`. Indeed the primitive irreducible hypersurface is flat and Cohen–Macaulay; each special fibre is generically smooth (at odd primes dividing `n`, it is the reduced union `xyz=0`; at 2 it is `xy+xz+yz=0`). This proves regularity in codimension one and hence normality. Every generic cover is constant and a section forces that constant extension to be unramified at every finite prime. Minkowski's discriminant theorem leaves only `ℚ`. For even `n`, first divide the equation by its coefficient content if discussing a flat integral model: the literal unprimitive equation can have unwanted vertical components. No claim about those non-flat models is needed here.

**Assessment (log scope).** “The log fundamental group over ℤ” has no unique answer without a log structure and choices at bad fibres. The natural characteristic-zero interiors and their tame boundary covers are computed above, and the actual ordinary integral model over `S` is computed exactly. No assertion about all wild logarithmic covers in residue characteristics dividing `2n` is made. Such a construction would require a separately specified integral obstruction and cannot silently replace finite étale descent on the generic fibre.

## (2) What the obstruction mechanisms actually say at one n

### Proposition 3 — on the singular model/resolution, étale–Brauer equals BM

**PROVED.** On `U` and on `Ũ`, every finite torsor is geometrically constant. After twisting it has a section, whose image is a copy of the base. A BM-orthogonal adelic point therefore lifts to a BM-orthogonal point on that copy for every finite torsor. Thus

`U(𝔸)^{ét,Br}=U(𝔸)^{Br}`, and `Ũ(𝔸)^{ét,Br}=Ũ(𝔸)^{Br}`.

Intersecting with any specified integral/real conditions preserves these equalities. BL Theorem 1.8 (with `n≥2`) therefore proves that **ordinary finite étale–Brauer descent on the singular ES model cannot disprove ES**. Proper lifting to the blow-up does not change this: BL Remark 2.11 and Corollary 2.9 identify the relevant BM condition, and a local integral point with generic smooth image lifts over a DVR by properness.

**Assessment.** This closes the previously uncomputed **finite-étale** assertion for those two spaces for an actual reason—π₁—not because their projective compactifications are rational. Rationality alone never justified that assertion. It does not classify torsors under positive-dimensional integral group schemes: for example `Pic(Ũ)=ℤ` already gives nontrivial `ℂ*`/`G_m` line-bundle torsors. Integral norm-torus descent on an auxiliary fibration, or a new log-flat construction at bad fibres, needs its own comparison theorem and is not ruled out merely by π₁.

### Proposition 4 — finite descent on the smooth locus is also non-obstructing

**PROVED.** For any positive `m,n`, `W^sm_{m,n}` survives finite descent (without Brauer groups on covers). Use `Y₁`: at every finite place take `(A,B,C)=(0,1,−1)`, mapping to `(-1,0,0)`; at the real place take `A=B=C=√(3n/m)`, mapping to `(3n/m,3n/m,3n/m)>0`. These are adelic points of `Y₁\{0}` with integral image at every finite place. Since that cover is geometrically simply connected, its finite torsors are constant and impose no further finite-descent condition. Functoriality proves the assertion.

**Important limitation.** These specific adeles are not BM-orthogonal: the pullback of BL's class has invariant `−1` at infinity and `+1` at every finite place. Finite descent is not étale–Brauer.

### Proposition 5 — even the full Brauer group of the smooth locus does not obstruct

**PROVED (relative to purity and Hochschild–Serre).** One has

`Pic(X̄)=ℤ/2`,  `ℚ̄[X]^*=ℚ̄*`,  `Br(X̄)≅ℚ/ℤ(−1)`.

Moreover `Br₁(X)/Br ℚ ≅ ℚ*/ℚ*²`, represented by `(c,xyz)`, `c∈ℚ*`; the full `Br(X)` is generated by these classes, constants, and BL's `α=(-x/z,-y/z)`.

**Proof.** BL gives `Pic(Ũ̄)=ℤ[L]` with `L·E=1`. Restriction to `E` identifies this group with `ℤ`, so `[E]=−2[L]`. The divisor sequence for deleting `E` gives `Pic(X̄)=ℤ/2` and no nonconstant units. Purity for the regular divisor `Ē≅ℙ¹` gives `Br(Ũ̄)≅Br(X̄)`, since `H¹(Ē,ℚ/ℤ)=0`; BL Proposition 2.5 gives its Galois module. Hochschild–Serre injects `Br₁(X)/Br ℚ` into `H¹(ℚ,Pic X̄)=H¹(ℚ,ℤ/2)`. The symbols `(c,xyz)` realize those cocycles: `div_X(xyz)` is twice a divisor whose class generates `Pic X̄`. Thus this injection is onto. The geometric invariant group is `ℤ/2`, already lifted by `α`. ∎

**PROVED (nonempty ordinary BM plus finite descent).** For every `n≥2`,

`W^sm_{4,n} ∩ X(𝔸)^{Br} ∩ X(𝔸)^{fin} ≠ ∅`.

Choose a prime `ℓ|n` and a nonzero-coordinate local integral point `P_ℓ` with `α(P_ℓ)=−1`, using BL Lemmas 3.6–3.7 and local density. Choose a positive squarefree integer `d` representing `δ(P_ℓ)` in `ℚ_ℓ*/ℚ_ℓ*²` (elementary approximation). At every other finite place take `(-d,0,0)`, and at infinity any positive real point. The torsor evaluations at **all** places are the localization of the same global positive squareclass `d`. Therefore they lift adelically to `Y_d\{0}` and survive finite descent, and all symbols `(c,xyz)` pair to zero by Hilbert reciprocity. On the axes `α=0` in additive notation: its restriction to the affine line is constant and agrees at the origin with the zero value in BL Remark 2.11. Only `ℓ` and infinity contribute nonzero invariants to `α`, and these cancel. ∎

**Assessment (the exact remaining issue).** This is still not a computation of `W^sm∩X(𝔸)^{ét,Br}`. One must test **all** of `Br(Y_d)` on the lifts, not merely `q_d^*Br(X)`. It would be an unjustified upgrade to infer cover-Brauer nonemptiness from Proposition 5. The exact remaining set is

`⋃_{d∈ℚ*/ℚ*²} q_d( (Y_d\{0})(𝔸)^{Br(Y_d)} ) ∩ W^sm`.

Because the cover is geometrically universal, further finite covers upstairs are constant; this expression is the full smooth-locus étale–Brauer condition. Real positivity forces `d>0`. Its emptiness/nonemptiness for all ES models, or even its complete evaluation at the numerator-8 controls, is **not determined in this memo**. This is the precise PARTIAL verdict, not a claim to have computed an unknown obstruction.

**PROVED (scope of homotopy input).** Harpaz–Schlank, *Homotopy Obstructions to Rational Points*, arXiv:1110.0164, Theorem 11.1, identifies `X(𝔸)^h=X(𝔸)^{fin,Br}` for smooth geometrically connected varieties over a number field (checked in the paper). Intersecting these equal sets with the chosen integral conditions does not create an additional generic-fibre homotopy obstruction. On `X` it reduces to the displayed cover-Brauer question; on `Ũ` it reduces to ordinary BM. The theorem is not being applied directly to singular `U`. Harpaz–Skorobogatov, arXiv:1212.6019, constructs projective counterexamples with **nonempty** étale–Brauer sets; it is not a general integral Hasse principle or an extra computable obstruction.

### Strong approximation versus one ES target

**PROVED (BL Theorem 1.9 and Lemmas 3.10–3.11).** For each fixed `n`, integral points are finite off the six exceptional lines, hence not Zariski dense. At almost all auxiliary primes `q`, their reductions cannot fill `U(𝔽_q)`, although BM permits suitable local points. This supplies smaller BM-allowed adelic opens missed by rational points and disproves strong approximation beyond BM for every `n`.

**Assessment.** It says that **some** congruence subtargets inside the integral adelic set are missed, not that the full positive target `W_{4,n}` is missed. Indeed the theorem holds also at every already-solved `n`. There is no localization procedure in its proof selecting a counterexample prime. Positivity is retained throughout our obstruction constructions at the real place; the signed axis points are only independent local components, never a signed global point “reflected” to a positive one.

## (3) Attempts, exact computations, and the numerator-8 acid test

### A. Exhaustive positive counts and cover coordinates

**CERTIFIED.** `scripts/z45_etale_descent_check.py` enumerates all `x≤y≤z` using

`n/m < x ≤ 3n/m`, `a/b=m/n−1/x` in lowest terms,

`(ay−b)(az−b)=b²`.

It also independently enumerates `x,y` for the 131/241 controls and the 3361 model-trap prime, using `y≤2nx/(mx−n)` and the unique rational value of `z`. Both engines agree. Every enumerated solution is lifted and checked exactly on its squareclass twist, using rational arithmetic. This is a new cover/integrality experiment, not a new test of the already-known divisor identity.

| m | n | unordered positive solutions | distinct twist squareclasses |
|---|---:|---:|---:|
| 4 | 9 | 6 | 3 |
| 4 | 131 | 32 | 10 |
| 8 | 131 | 0 | 0 |
| 4 | 241 | 8 | 6 |
| 8 | 241 | 0 | 0 |
| 4 | 193 | 6 | 6 |
| 4 | 409 | 15 | 11 |
| 4 | 577 | 18 | 12 |
| 4 | 3361 | 15 | 12 |

For example, the solution `(62,2139,1030998)` for `4/241` has twist `d=7471=31·241` and lift `(A,B,C)=(69,2,1/241)`. Requiring `A,B,C` to be integers would incorrectly discard it. At `4/131`, `(33,4326,6233766)` has twist `393=3·131`, already outside the `2n`-unit twist list.

**CERTIFIED (particularly useful toy obstruction).** At `p=3361`, the complete twist list is

`5,29,43693,57137,87386,97469,171411,184855,265519,339461,379793,581453`.

Every member has a prime factor outside `2p`. If a solution were a section of `𝒳` over `ℤ[1/2p]`, pulling back its étale `μ₂`-torsor would give an `S`-unit squareclass, contradiction. Thus **none of the 15 positive ES points is a section of that smooth integral model**, although all are legitimate integral points of `𝒰` with smooth generic image. This demonstrates a real false-obstruction trap in applying integral descent on a smaller model.

### B. Explicit BM and finite-descent adeles at both failures

**PROVED, with exact coordinates CERTIFIED.** For an odd prime `p∤m`, choose `t∈{1,…,p−1}` with `(-t/p)=−1`. The point

`P_p=(pt/(mt−p(1+t)), 1, t)`

is `p`-integral, its first coordinate has valuation one, and `α(P_p)=(-1/t/p)=−1`. Thus the same local calculation as BL gives:

| numerator/denominator | `P_p` | positive real point | global twist d |
|---|---|---|---:|
| 8/131 | `(-131/254,1,1)` | `(393/8,393/8,393/8)` | 262 |
| 8/241 | `(-1687/1872,1,7)` | `(723/8,723/8,723/8)` | 3374 |

Take `d` to be the squarefree part of `pmt`. Then `xyz/d` is a square in `ℚ_p`, as its unit reduction is a square and its valuation is even. At all other finite places use `(-d,0,0)`, whose torsor class is `d` and whose `α` invariant is zero. Proposition 5's proof now verifies **full ordinary BM on the smooth locus and finite descent simultaneously**, even though both positive integral sets are empty. On singular `U_{8,p}`, Proposition 3 upgrades ordinary BM to its **entire ordinary finite-étale–Brauer set**.

**Assessment (acid-test conclusion).** The constructions explain exactly why the proposed ordinary descent mechanisms do **not** explain the numerator-8 failures. They cannot legitimately be promoted into an existence theorem for numerator 4. No new obstruction claiming to distinguish 4 from 8 has been constructed. Smooth-locus cover-Brauer remains uncomputed, so the table does not claim the stronger smooth étale–Brauer sets are nonempty.

### C. What an obstruction at a prime would have to do

**PROVED (necessary shape).** A smooth-locus étale–Brauer disproof at `p` would require, for **every positive twist d**, that no adelic lift with positive integral image be orthogonal to `Br(Y_d)`. There is only one geometric covering layer; neither a nonabelian finite quotient of `π₁(X̄)` nor a further geometric finite tower exists. By Propositions 3–5 this obstruction cannot consist merely of BL's class, ordinary smooth-locus Brauer classes, or finite descent.

**Assessment.** This is a precise candidate “prime T1”: a simultaneous cover-Brauer exclusion across every possible positive squareclass, not a congruence condition for one twist. A different non-BM counting obstruction could still kill all solutions without emptying this set. Replacing “all twists” by a fixed finite menu is not justified; the examples above show why even primes outside `2p` matter. Nothing here supplies the required global exclusion or a theorem precluding it.

## (4) FRONTIER §4 screening, all 17 lines

These are **Assessments of a prospective ES proof from this route**, not objections to the geometric propositions.

| # | result | reason |
|---|---|---|
| 1 | N.A. / FAIL for Type-I/II forcing | We prove no Type-I/II existence. The cover exists at odd squares, and `4/9` has six mixed/scaled solutions. Its topology supplies no T1-breaking step. |
| 2 | FAIL as an existence mechanism | Explicit ordinary BM/finite-descent adeles also survive at 8/131 and 8/241; the arithmetic count is zero there. |
| 3 | FAIL | The covering geometry and its laws are numerator-uniform; a 4-specific integral input is missing. |
| 4 | FAIL | Fixing a cover coordinate gives the displayed moving-modulus factorization. No divisor-class lower-tail theorem is supplied. |
| 5 | PASS | All constructions and computations keep `n` fixed. No average is used to recover a prescribed prime. |
| 6 | N.A. | No main-term-minus-error estimate is asserted. A hypothetical lower bound must remain polylogarithmic, not power-sized. |
| 7 | PASS | No pointwise two-sided asymptotic or polylogarithmic absolute error is claimed. |
| 8 | N.A. | This is a classification/obstruction computation, not a finite congruence-and-factorization witness algorithm. A finite twist menu would need separate justification. |
| 9 | FAIL as an existence mechanism | Fundamental-group and ordinary Brauer data control squareclasses, not the desired single divisor class. Cover-Brauer has not been computed. |
| 10 | N.A. | No pooling of large factors across shifts. |
| 11 | PASS | Positive real components are imposed explicitly. Independent signed local components are not a signed global solution or a reflection argument. |
| 12 | PASS / N.A. | No relaxed certificate is transported. We explicitly reject replacing image-integrality by integrality of covering coordinates or smooth reduction. |
| 13 | FAIL | Vanishing of refined obstructions still does not imply an integral point; numerator 8 already refutes the singular-model shortcut. |
| 14 | PASS as a diagnostic | Full counts at 193, 409, 577, 3361 are checked; 3361 exposes the bad-model trap. No fixed slice is claimed to succeed. The larger 5101441 diagnostic is not needed for a non-witness-producing classification. |
| 15 | PASS for geometry; N.A. for counts | All π₁ and vanishing statements are independent of the Mordell class and of distance to a square. They therefore cannot explain the near-square count deficit. |
| 16 | N.A. | No transfer from a thin family. |
| 17 | N.A. / FAIL if used for forcing | No coset-covering certificate is proposed; no theorem controls residues of the large prime factors on the cover. |

## (5) A model-aware ramified-descent profile: what genuinely new theory would need

**Definition (proposed bookkeeping, not an existence theorem).** For positive squarefree `d`, let

`F_d(m,n)=# { P∈Y_d(ℚ)/{±1} : q_d(P)∈𝒰_{m,n}(ℤ), q_d(P)>0 }`,

and let `S_d(m,n)` be the BM-orthogonal adelic set on `Y_d\{0}` with exactly those **image** integrality and real conditions. Use ordered coordinates in this definition; divide by permutations for the table. Then

`F(m,n)=Σ_{d>0 squarefree}F_d(m,n)`, and `F_d>0 ⇒ S_d≠∅`.

**PROVED.** This is a disjoint squareclass decomposition of the exact positive count. Each `n` has only finitely many contributing `d`, because the positive point set is finite. For numerator 4, elementary sorted bounds `x≤3n/4`, `y≤3n²/2`, `z≤9n⁴/8` even give the crude explicit cap `d≤xyz≤(81/64)n⁷`. This is a bound on twists from actual solutions, not a bound on all adelically surviving twists or an efficient algorithm. It does not conflict with FRONTIER's sharper `O(p²)` bound on **certificate moduli**, a different object.

**First open implication (CONJECTURE-level question, not assumed).** Is `⋃_d S_d(4,n)` nonempty for every `n≥2`? What is its answer for `(m,n)=(8,131),(8,241)`? The first concrete task is the Brauer group/evaluation computation on the explicit smooth cubic `mdABC=n(A+B+C)`, not an abstract invocation of anabelian geometry. If the sets are nonempty also for the controls, refined étale descent has definitively failed to distinguish them; if not, one must isolate the precise model-sensitive class and prove it never blocks the numerator-4 models.

**Toy test (CERTIFIED + PROVED).** The entire weaker profile using `q_d^*Br(X)` instead of `Br(Y_d)` is nonempty at both numerator-8 failures (d=262 and 3374), while `ΣF_d=0`. At numerator 4 the profile records actual lifts at all listed primes; at 3361 every occupied twist lies outside the fixed-good-model Selmer list. Thus the test already refutes (i) sufficiency of the pulled-back Brauer profile, (ii) bounding twist ramification by `2n`, and (iii) naive integral coordinates upstairs. It does **not** test uncomputed extra classes in `Br(Y_d)`.

**CONJECTURE shape that would imply ES, deliberately not advertised as standard.** A model-specific one-sided principle could assert, for the numerator-4 lattices and all primes `p>p₀`,

`F(4,p) ≥ c (log p)²`, with `c>0`,

or assert existence from the appropriate nonempty refined adelic set, together with a theorem that this set is always nonempty. A finite certified census through `p₀` would finish ES. If formulated uniformly for numerator `m`, it needs an explicit `p₀(m)` or additional model hypotheses, and cannot include 8/131 or 8/241 with a positive lower bound. This is a new **required** model-sensitive lower-tail theorem, not an implication of standard BM philosophy and not established by the covering decomposition. On `Ũ` the refined set is already nonempty, so an integral Hasse principle for precisely these targets is ES itself.

### Scope of the nearby literature

**PROVED (checked statements, not application claims).** Harpaz, *Integral points on conic log K3 surfaces*, JEMS 21 (2019), 627–664, arXiv:1511.04876, Theorem 1.0.1 treats pencils

`(c₁t+d₁s)(c₂t+d₂s)x²+(c₃t+d₃s)(c₄t+d₄s)y²=1`

over `ℤ_S`, with `2,∞∈S` and seven specified independent squareclasses. It is an actual existence result via descent on norm-one tori. No isomorphism of the ES integral target to such a pencil satisfying its hypotheses is established. The coordinate conic pencils of ES are split divisor problems; simply enlarging `S` discards required local restrictions. Moreover `X` has nontrivial π₁, unlike Harpaz's simply connected log K3 definition; the resolution is the appropriate simply connected object, not a proof that his hypotheses hold.

**PROVED (BL, with literature precedent).** `Ũ` is strongly obstructed at infinity in the terminology cited by BL §3.9, and its positive integral points form a finite set for each fixed model. Therefore a height-asymptotic as `B→∞` on one fixed affine surface does not provide a lower bound as the **integral model** varies with `p`. Browning–Wilsch, arXiv:2407.16315, *Integral points on cubic surfaces: heuristics and numerics* (abstract checked), proposes density heuristics and numerical comparisons; it is not a pointwise integral Hasse theorem. Loughran–Mitankin, *Integral Hasse principle and strong approximation for Markoff surfaces*, Theorem 1.5 (as recorded in FRONTIER §2.4; not independently rechecked here; paper cited in BL [17]), supplies failures beyond BM on related log K3 surfaces, not a theorem covering the ES models. No transfer from those results is invoked.

**Assessment.** A broad “all log K3 models satisfy integral HP after étale–Brauer” conjecture is already false for the singular/resolved numerator-8 models by the explicit adeles above and π₁ triviality. A useful replacement must retain the integral lattice, real component, and a model-varying, one-sided arithmetic count. Calling that missing theorem “integral anabelian geometry” would not make it less B2-strength.

## (6) Verdict, next steps, and verification record

**Verdict — PARTIAL; promise 2/5 (Assessment).** The exact geometric calculation closes finite descent and étale–Brauer **on U and Ũ**, and closes finite descent plus ordinary Brauer on `U^sm`. It does not close étale–Brauer on `U^sm`, because the Brauer groups of its universal-cover twists and their image-integral adelic sets remain to be evaluated. No non-BM disproof invariant and no ES lower bound is produced. An existence argument based only on the closed parts collapses at numerator blindness and the unjustified local-to-global implication; slicing the cover returns B2.

**Concrete next steps (Assessment).**

1. Compute `Br(Y_d)/Br ℚ`, its dependence on `n,d`, and explicit local evaluations; begin with `(m,n,d)=(8,131,262)` and `(8,241,3374)`. Do not presume it equals the pullback of `Br(X)`.
2. Test the **whole** `S_d` profile, not one arbitrarily chosen twist; first decide the two numerator-8 cases. A failure at one d is not an obstruction to the original problem.
3. If a uniform nonemptiness proof emerges, record a scoped obstruction-side theorem rather than an ES proof. A count/class-aware single-prime input is still missing.

**Verification.** `ulimit -v 8000000; timeout 120 uv run python scripts/z45_etale_descent_check.py` completes successfully. Exact output is `data/z45_etale_descent/check.json`. The acid-test and 3361 counts have a second, independent `x,y` enumeration; the group proof and cover identities are mathematical arguments, not inferred from numerical data. The task's BL PDF §§1–3 was read via `pdftotext`; the cited Harpaz theorem and Harpaz–Schlank Theorem 11.1 were checked in full text. Temporary literature extracts are under `/tmp/z45_*`, not repository additions. No existing repository file was edited; no commit is made by this subagent.
