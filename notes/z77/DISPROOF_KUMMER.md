Result: The one-prime repair with exponent mM lifts to a rational twist of the level-m coordinate cover and defeats **every** M-torsion Brauer class there, even over the bad local twist.  Label: PROVED (rel. absolute purity, local and global reciprocity, and z75 prime selection)
Scope: Outer-integral, positive adeles on S_n°, X_n°, U_n° at k=4,8 in the nonsquare-kernel range below; m,M fixed, twist allowed to depend on the data. Not unrestricted étale–BM, not an integral point, not a disproof of ES.
Review: none (cross-review pending)
Triage: BARRIER-BROAD (bounded upstairs tests on finite covers of these opens)
STATUS delta: Proposed sharpening to §1D, open-surface row: “The same D-point defeats the full M-torsion upstairs on a rational twist of each finite group torsor of bounded geometric monodromy exponent m, for every fixed (m,M); unbounded exponents are different.”

## 1. A negative answer to the bounded-obstruction question

Use the conventions of `notes/z75/DISPROOF_OBSTRUCT.md` §§1–3. In particular D means integral on the **original** affine equation at every finite place, in the coordinate open at every place, positive at infinity, and integral on the **open** at almost all places. Write s for the squarefree kernel of the positive integer n. Assume s≠1 for k=4 and s∉{1,2} for k=8. Take V to be the coordinate-deletion open in any of

    S: k u B C = n+u+B,     X: k a b c d = a+b+nc,     U: k x y z = n(xy+xz+yz).

**Theorem.** Fix m,M≥2. Adjoin m-th roots of the arrangement units (z75 §2), or equivalently of the original coordinates, and allow rational twists. There exists a single rational twist π:W→V and a point T∈W(𝔸) with π(T)∈D and T orthogonal to Br(W)[M]. In fact for S **every** z75 repair with q^{mM} works provided q≡−1 mod k, q∤mMn(n+1), and −n is an mM-th power mod q. This means existence of a *choice of local lifts*, not that arbitrary lifts give the same evaluation. The construction is uniform in the classes and their conductors. Equivalently it handles order dividing M modulo constants: subtract the value at the rational base point. It does not assert existence of a point on each twist. At a failed input the set in question is the **union** of the images over twists; one twist suffices.

In particular no such obstruction explains 4545 on X (4), 131 or 241 on U (8), or any of the nonsquare odd R₈ zeros on S (8). For the cited failed inputs the global negative decisions are from the independent exhaustive checks in z75–76, not from the theorem. ES in ℕ remains open.

### A local evaluation fact

Let O=ℤ_q, K=ℚ_q, F=𝔽_q, q∤M. On a smooth finite-type O-scheme 𝒴, take two O-sections whose reductions lie in one split-torus component Y≅𝔾_m^r of the special fibre. Suppose the reductions differ coordinatewise by M-th powers in F^×. Then **every** β∈Br(𝒴_K)[M] has equal values in Br(K) at the two generic points of the sections.

Here and below Br is the cohomological Brauer group. Lift β to H²(𝒴_K,μ_M) by the Kummer sequence. Removing the other components in the special fibre if necessary, the localization boundary and codimension-one absolute purity give a residue in H¹(Y,ℤ/M). Pullback by a section sends this to the residue in H¹(F,ℤ/M) of β evaluated on its generic point: the section meets the smooth special fibre with multiplicity one (transverse base change for purity). The residue detects the class in Br(K)[M], since Br(O)=Br(F)=0. Finally, for every γ∈H¹(Y,ℤ/M), evaluation is unchanged between the stated reductions. Translate the first point to the identity, then pull the translated character back by coordinatewise [M]. Its geometric H¹ class is zero, since geometric prime-to-q H¹ of a torus is generated over the algebraic closure by the coordinate Kummer characters, killed by [M]. Thus this pullback comes from F by Hochschild–Serre and is constant on Y(F). No assumption that F contains μ_M is needed. This proof compares even classes with **nonzero vertical residue**; compactifying and declaring the evaluations zero would not do that.

### Proof of the theorem

Choose q as stated (infinitely many by `notes/z75/DISPROOF_OBSTRUCT.md` §3, applied with exponent 2mM if necessary). Set B₀=(n+1)/q and C₀=(q+1)/k. The rational point P=(1,B₀,C₀) on S is positive and integral outside q. Normalize the twist by P. With x,y,z all invertible, its equation over ℚ is

    n+x^m+B₀(y^m−(q+1)z^m)=0,                 (1)
    u=x^m,   B=B₀ y^m,   C=C₀(z/(xy))^m.

Indeed this adjoins the m-th roots of the normalized u,B and uBC. The point above P is P̃=(1,1,1). Over K choose α^m=−n with α mod q an M-th power (Hensel applied to an mM-th root). Choose λ^m=(q+1)⁻¹ with λ≡1 mod q. A useful **line on the local twist** is

    L: t ↦ (α,t,λt),      t∈𝔾_m.                          (2)

The repaired point downstairs has C′=C₀, B′=B₀ q^{mM}, u′=(n+B′)/(k B′ C₀−1). Here B′ has valuation mM−1 and u′ reduces to −n. There is a lift

    T_q = (w, q^M, w q^M),     w^m=u′,   w≡α mod q,

again by Hensel. All other components are P̃. We compare values at P̃ and T_q for any β∈Br(W_K)[M] in **three equalities**:

1. **P̃ to L(1).** Use the model in the three-dimensional split torus over O given by q(n+x^m)+(n+1)(y^m−(q+1)z^m)=0. The special fibre has y^m=z^m; the component y=z is a split two-torus with coordinates (x,y). Smoothness there follows from the unit z-derivative (the hypersurface is flat, or use the relative Jacobian criterion). Both sections reduce on this component, to (1,1) and (α mod q,1). By the local fact their evaluations agree.
2. **L(1) to L(q^M).** Restrict β to (2). On 𝔾_{m,K}, every Brauer class of order dividing M is a constant plus (χ,t) with Mχ=0. Indeed the residue at 0 gives χ, the character symbol splits the residue map, and the kernel extends over 𝔸¹_K and is constant by homotopy invariance. At 1 and q^M the values agree. This step crosses a real change of valuation; it is not local constancy on a ball.
3. **L(q^M) to T_q.** Set Y=y/q^M, Z=z/q^M in the torus. The second model is n+x^m+(n+1)q^{mM−1}(Y^m−(q+1)Z^m)=0. The special fibre has x^m=−n, smooth by its x-derivative. The component x=α mod q is a split torus with coordinates (Y,Z). Our points reduce to (1,1) and (1,α mod q). The same local fact applies.

It follows that β(T_q)=β(P̃) locally, **for the full local M-torsion**, a stronger equality than for restrictions of global classes. The two smooth models include the needed sections; their generic fibres are both (1). We never suppose the diagonal projective Fermat twist has good reduction at q or that its boundary residues vanish. Returning to global classes, all other local values are unchanged; the diagonal evaluation sums to zero by reciprocity. The image lies in D by construction.

For X use (a,b,c,d)=(u,B,1,C); for U use (x,y,z)=(uBC,nuC,nBC). In each case twist the target coordinate cover by the image of P. The normalized target units pull back to monomials in the normalized source coordinates, so the map lifts over ℚ from (1) by the same monomials in their roots (c-root=1 for X). Project T by this morphism. Integrality, positivity and the adelic restriction hold on the image; every target M-torsion class pulls back to M-torsion, so there is no computation of the target group to assume. ∎

### Consequences and checks on the scope

* There **are** genuinely non-pullback classes. For example, on (1) for even m, the quaternion (x,y) extends over W (two units), and is geometrically nonconstant. On the smooth affine diagonal surface with y=0 restored, over ℚ̄ its residue at y=0 is the squareclass of x in the function field of the curve n+x^m=(q+1)B₀ z^m. This is a smooth geometrically irreducible affine Fermat curve (smooth projective closure, irreducible by Bézout); x has simple zeros at x=0 there, so is not a square. These zeros may be used to test its function field even though x=0 is not on the original open. In contrast every class from Br(V) on V=S° has geometrically trivial pullback for even m: z75 §2 generates modulo constants by character classes (geometrically zero) and quaternion symbols of pairs of arrangement units (whose entries become squares over ℚ̄). Thus already m=M=2 really tests more than inherited classes, including if pullbacks of unbounded-order downstairs classes are allowed. The calculation does not require a description of the entire Fermat-surface Brauer group.
* **Beyond the displayed Kummer torsor.** At given V,m,M the same downstairs adelic point passes the following test for **every** finite ℚ-group torsor E→V of geometric monodromy exponent dividing m: some rational twist of E admits an adelic lift orthogonal to its entire M-torsion. Indeed normalize E by its fibre at P (the image of P on the target if V≠S). Pull this twist back to the normalized level-m cover W of V. Its geometric monodromy is trivial because the image of π₁(W̄) is mπ₁(V̄), with π₁(V̄)=Ẑ(1)^r, as computed in z75 §2. Twisting by constants does not change this kernel. Since W is geometrically connected, this finite étale pullback descends from a finite étale ℚ-scheme by the arithmetic π₁ sequence; it has a rational point over P̃ by normalization. It therefore has a section. Under the resulting W→E^tw morphism, M-torsion pulls back to M-torsion. No assumption of abelian **arithmetic** monodromy is made. In particular finitely many covers and finitely many prescribed exponents can be handled simultaneously by taking common multiples. This still does not treat a class of unbounded order or a single adelic point for the unbounded tower: q, P and W may change. The unrestricted coordinate-reconstruction result in z76 §3 stands.
* Numerical calibration is not needed for the local proof: e.g. at m=M=2, q=11 for n=4545,k=4 (−n≡9≡5⁴ mod 11), q=7 at n=131,k=8 (−n≡2≡2⁴ mod 7), q=7 at n=241,k=8 (−n≡4≡3⁴ mod 7). Unlike q², the q⁴ repair always admits an orthogonal lift at this level. At odd squares the Chebotarev step fails: a square root of −n is incompatible with q≡−1 mod 4, q∤n. At k=8 the same issue arises for twice a square ((−2/q)=−1). This is a constraint on the construction, not a claim that these all obstruct on U.
