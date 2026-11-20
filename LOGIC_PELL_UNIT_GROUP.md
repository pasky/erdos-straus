# The fundamental Pell unit at the ES-failing prime

```
Result: in model M3, R[√P]ˣ={±z^j : j∈ℤ standard}, z=X+√P·Y. The positive negative-Pell solutions at P are exactly z^(odd>0),
        so (X,Y) is coordinatewise least, and both of its coordinates are infinite.
Label: PROVED (internal), relative to LOGIC_NEGATIVE_PELL_ROOT_AUDIT.md and LOGIC_JOINT_PID_TREE_AUDIT.md.
Scope: units over the single prime P of M3. No universal Pell or least-solution principle, and no cofinal Pell growth;
       separate from M1/M2. No standard counterexample. ES is OPEN.
Review: cross-lab (Opus) data/z74/xreview/REVIEW_PELLMODELS_OPUS.md, ACCEPT (only this block added).
Triage: HEADLINE (with LOGIC_NEGATIVE_PELL_ROOT_AUDIT.md; strengthens the STATUS §E joint-PID item)
STATUS delta: optional half-line on the joint-PID bullet, proposed in the review, §5 item 3.
```
*(z74 Opus xreview fix: added this §0 block.)*

**PROVED in the model of `LOGIC_NEGATIVE_PELL_ROOT_AUDIT.md`, relative to its joint tower lemmas.** In the ordered quadratic field extension take `t=+√P`, and put `z=X+tY`. Then

```
                   R[t]ˣ = { ±z^j : j ∈ ℤ }.
```

Here `ℤ` is the **external standard** group of integers. With both coordinates positive, the negative-Pell solutions correspond exactly to `z,z³,z⁵,…`; the nontrivial positive-Pell solutions to `z²,z⁴,z⁶,…`. In particular `(X,Y)` simultaneously minimizes both coordinates at norm `−1`. This is the same `P` and the same `R` with IOpen, internal Dirichlet, TS, NR, Lagrange and `¬ES(P)`. We calculate in a quadratic extension to classify pairs of elements **of R**; we do not insert a square root of `P` into the PID or into the tower.

## 1. Root units

Recall the row `Da+Cb=1` with `C=u²−v², D=2uv`, `Y=u²+v²`, `X=Ca−Db`, `P=a²+b²`. The root `E` is a rational-constant UFD with `P` prime, so `P` is not a square in its fraction field (its `P`-valuation is one). Thus `E[t]` is a domain, free on `1,t`. The conjugation `σ(t)=−t` gives `zσ(z)=X²−PY²=−1`, in particular `z⁻¹=tY−X` is regular **without** localization.

On inverting `Y` there is an isomorphism

```
E[t,1/Y] = ℚ[u,v,1/Y][z,z⁻¹].
```

Indeed start with an independent Laurent variable `Z` on the right. Set `X=(Z−Z⁻¹)/2`, `t=(Z+Z⁻¹)/(2Y)`, `a=(CX+D)/Y²`, `b=(C−DX)/Y²`. Then `Da+Cb=1`, `Ca−Db=X`, and `t²=(1+X²)/Y²=a²+b²`. These substitutions and `Z↦X+tY` are inverse maps. As `Y` is irreducible in **ℚ[u,v]**, the chart units are precisely `c Y^h z^j` with `c∈ℚˣ`, `h,j∈ℤ` (polynomial UFD localization and independent Laurent variable). But `Y` is not a unit in **E[t]**: its value is zero at the complex point `(u,v,a,b,t)=(1,i,0,1/2,1/2)`. If a global unit has chart expression `c Y^h z^j`, division by the global unit `c z^j` makes `Y^h` a global unit. For `h≠0` this makes `Y` a unit, using the inverse if necessary. Hence `h=0`. This proves `E[t]ˣ=ℚˣ z^ℤ`; it does not need `Y` prime upstairs or `E[t]` factorial.

## 2. Unit descent on every edge

Write `A⊂B` for a rational-stage edge and `F=Frac(A), G=Frac(B)`. `P` stays prime in the rational-stage UFD `B` by the tower lemmas, hence is nonsquare even in `G`. Choose `t` consistently in one ordered real closure of the union. Write `K=F(t)`, an **ordered field**. First check (i) the scalar-extended generic ring `B⊗_A K` has unit group `Kˣ`; then (ii) check `B∩F=A`. Together these give `B[t]ˣ=A[t]ˣ`: the generic ring is `(A\{0})⁻¹B[t]⊂G(t)`, and

```
B[t] ∩ K = (B ∩ F) ⊕ t(B ∩ F),
```

by independence of `1,t` over **G**. Apply this contraction to a unit **and its inverse**. Thus neither a factoriality assertion for the quadratic rings nor an unramified base-change assertion at `(P)` is involved.

* **Floor, progression, free prescription, identity.** The nonidentity ones are polynomial lines, not function fields: over K their units are constants, and comparison of polynomial coefficients gives `B∩F=A`. The chosen floor lies in an ordered extension but its actual stage generator is transcendental, not the whole real closure. A skipped task adds nothing.
* **Bézout row.** For a primitive pair `g,h` in A the generic row `gU+hV=1` is a polynomial line over K. On the two rational charts the constant ring intersection in F is `A[1/g]∩A[1/h]=A` since A is a UFD and `g,h` are coprime. Trivial rows can be skipped. Only one pivot is needed *generically*, not for that intersection.
* **NR cone `DH=V²+s`.** Over K this injects by `H=(V²+s)/D` into `K[D,D⁻¹,V]` (the primitive linear relation over `K[D,V]` generates the kernel). A unit maps to `cD^j`, `c∈Kˣ`. The chart variable `D` is a nonunit before localization: its quotient is `K[V,H]/(V²+s)≠0`. Thus `j=0` by the same powers-and-inverse argument as for Y. In particular no irreducible-special-fibre argument is necessary. For contraction over A, substitute for H: reducing every mixed `D,H` monomial gives an expansion in `D^j` (`j≥0`) and `H^l` (`l>0`) over `A[V]`. On the chart the latter have distinct negative powers `D^(−l)` with coefficients divisible by `(V²+s)^l`. A constant in F therefore comes from the degree-zero `D` coefficient in `A[V]`, hence from A.
* **Accepted TS circle, Lagrange sphere.** Over K filter `K[W₁,…,W_m]/(ΣW_j²−s)` by total degree (`m=2,4`). The associated graded is `K[W₁,…,W_m]/(ΣW_j²)`, a domain: for `m=2`, `−1` is still nonsquare in the ordered K; for `m=4` the quadratic form has rank four whereas a product of two linear forms has rank at most two. The principal leading ideal assertion follows by multiplying highest forms before passage to the quotient. Consequently degrees add and a unit and its inverse both have degree zero, so belong to K. An affine point on the circle over K would not by itself split its torus at infinity. Monic normal form in the last coordinate over the rational base A gives `B∩F=A` by comparison after passing to F. A skipped TS fork, or normalization of an already split prime at the end, adjoins no ring elements. Nothing here weakens the prime tasks for TS or NR.
* **Optional algebraic residue prescription.** For `PH=f(V)` with `f` monic of degree `n≥2`, the generic ring is `K[V]`, since `P` is invertible **in K**. A rational-stage normal form is `Σ_{0≤j<n} V^j h_j(H)`, `h_j∈A[H]` (monic division in V). Substitute `H=f(V)/P`: the nonzero blocks have distinct leading degrees `j+n deg(h_j)` modulo n. Only a constant `h₀∈A` can survive if the result is in F. This covers the quadratic residue variant as well; it puts no `1/P` in the stage ring. See `LOGIC_PRESCRIBED_FIELD_AT_P.md` for the hypotheses ensuring `P` persists during these tasks.

The calculation is for the edges actually present in `LOGIC_JOINT_PID_TREE_AUDIT.md` and the indicated prescription. For example a *different*, universal Pell tower adjoining a conic with leading form `U²−PV²` would have a split leading form over K; this proof would **not** apply there.

## 3. Union, integral pullback and all signs

In the directed union `A∞[t]`, a unit and its inverse occur together at a finite stage, hence the stage computation gives exactly `ℚˣ z^ℤ`. The prescribed PID is an integral **subring** `R⊂A∞` with `R∩ℚ=ℤ`. Both `z=X+tY` and `z⁻¹=−X+tY` belong to `R[t]` because `X,Y∈R`. If a unit of `R[t]` equals `c z^j`, then `c,c⁻¹∈R[t]∩ℚ=ℤ` by uniqueness of the two coefficients. Thus `c=±1`. In particular *all* its units have norm `±1`, with `N(±z^j)=(−1)^j`. Localizing a chart, embedding a fraction field in `ℚ_q`, or using a real closure for an order never makes its extra elements units of `R[t]`.

Even passing to the integral closure of `R` in `Frac(R)(t)` does not enlarge this unit group. Indeed an element `h=r+s t`, with `r,s∈Frac(R)`, integral over R is integral over a rational stage containing the finitely many coefficients of its monic equation and the numerators and denominators of `r,s`. In that stage UFD A, normality and conjugation give `2r, r²−P s²∈A` by trace and norm. Since `2∈Aˣ`, `r∈A` and `P s²∈A`; primality of P and UFD valuations give `s∈A` (even at P, `1+2v_P(s)≥0` implies `v_P(s)≥0`). Thus a unit of the integral closure and its inverse belong to `A∞[t]`, so it is `c z^j`. Now `c,c⁻¹` are rational and integral over R, hence in R by normality of the PID. Again `c=±1`. This does not identify the two **rings**, just their unit groups.

Finally `X>0, Y>0`, `t>0` and `z=X+√(1+X²)>1`. For `w=x+ty` of norm `−1` with `x,y>0`, `w>0`, `σ(w)=−1/w`, and

```
x=(w−w⁻¹)/2,        y=(w+w⁻¹)/(2t).
```

Hence `w>1`, so it is **+**`z^j` for a positive odd standard j, and conversely all such powers have positive coordinates. Both expressions strictly increase for `w>1`: the difference in the numerator of the second at `w₂>w₁>1` is `(w₂−w₁)(1−1/(w₁w₂))>0`. The first is immediate. Thus `j=1` gives the unique coordinatewise least pair `(X,Y)`; every other positive pair has **both** coordinates larger. For norm `+1`, `x=(w+w⁻¹)/2, y=(w−w⁻¹)/(2t)`; positivity of both again selects exactly the positive even powers. The least nontrivial one is `z²=(2X²+1)+t(2XY)`. These leastness statements are internal comparisons against *every* solution in the model; their proof needs no internal exponentiation function, division algorithm for units, or Archimedean bound on `log w / log z`.

**Not cofinal.** There is no greatest positive solution of either sign (multiply the unit by `z²`), but all their coordinates are in E: expand a standard power using `t²=P`, or use `z⁻¹=−X+tY` for negative powers. A subsequent progression variable is chosen above the whole field then present and is integral at every mark. It therefore gives a single bound **in R** for all these coordinates. Leastness at this counterexample is genuine; neither cofinal Pell growth in R nor a least-solution principle at *all* primes has been proved.

**Scope checks.** F1: no integral specialization of the negative-Pell witnesses at ordinary squares `m²>1` is asserted. F2/F3/F4: no numerator-eight or composite-input transfer or ordinary-prime count. The conclusion concerns a particular nonstandard prime with least negative-Pell solution and no ES triple.
