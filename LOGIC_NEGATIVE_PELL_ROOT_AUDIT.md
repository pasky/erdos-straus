# Audit: negative Pell at the ES-failing prime in the joint PID

**Verdict: accept at the distinguished prime, not as a universal Pell axiom.** Relative to the existing tower and square-class obstruction (`LOGIC_JOINT_PID_TREE_AUDIT.md`, `LOGIC_SPLIT_SQUARE_TEST.md`), the change of root below gives one countable external PID satisfying IOpen, internal unbounded Dirichlet, universal TS, NR and Lagrange, with `P≡1 mod 840` a positive infinite prime, `¬ES(P)`, and a positive primitive solution of `X²−PY²=−1`. No Pell step is needed on any subsequent edge. There is no inference about ordinary counterexamples. Here are the checks specific to the replacement.

### 1. Factorial row, order, signs (PROVED)

Write `C=u²−v²`, `D=2uv`, `Y=u²+v²`, `L=Da+Cb`. The ring is `E=ℚ[u,v,a,b]/(L−1)`, with `P=a²+b²`, `X=Ca−Db`. Over either `K=ℚ` or `ℚ(i)` this is a primitive linear relation over the UFD `K[u,v]`, hence defines a domain. On inverting `D`, it is `K[u,v,1/D,b]`. Each of `u,v` is prime upstairs: at `u=0` the quotient is `K[v,v⁻¹,a]` with `b=−1/v²`, and at `v=0` it is `K[u,u⁻¹,a]` with `b=1/u²`. They are distinct. Nagata now gives factoriality; a global unit on the chart is `c u^j v^k`, whose orders at these two primes must both vanish. Thus the two unit groups are exactly the respective scalar groups. The same row argument gives geometric integrality, and its two row charts cover since `L=1`. In particular `Frac(E)` is rational of transcendence degree **three**.

For an explicit order take `v` positive above `ℚ`, `u` positive above `ℚ(v)`, and `a` positive above `ℚ(u,v)` (above all old elements), solving `b=(1−Da)/C`. Then `C,D>0`, `b<0`, `X,Y,P` positive infinite. The sign of `b` does not matter for TS; use `−b` if needed. Every positive-degree polynomial in `a` over `ℚ(u,v)` has infinite magnitude in this order. Elements of `E` constant in that variable lie in `ℚ[u,v,1/D]∩ℚ[u,v,1/C]=ℚ[u,v]`, from the two polynomial row charts and `gcd(C,D)=1`. Successive dominance shows that its standard-bounded elements are just `ℚ`. This is the required root order, not an order obtained from a finite-place embedding.

The exact Gaussian identity is `(a+ib)(u+iv)²=X+iL`. Taking norms gives `X²+1=PY²` in `E`. Thus `1=(PY)Y−X·X`: primitivity of `(X,Y)` is **unimodularity**, already with explicit coefficients, in any integral pullback containing the coordinates. Also `(a,b)` is unimodular by the original row. Squaring the Pell unit gives a nontrivial positive Pell solution at this same `P`. The identity alone does not show leastness; `LOGIC_PELL_UNIT_GROUP.md` proves it by classifying the units through the tower. Neither result gives a universal Pell scheme.

### 2. The other projection and the special fibre (PROVED)

With `A=ℚ[a,b]` the equation is `H−1=0`, `H=b u²+2a uv−b v²`. On `D(b)` it is monic up to a unit in `u`, over `A[1/b,v]`. On `D(a)` put `v=u+w`; the coefficient of `u²` is `2a`. Both charts are free of rank two over the corresponding polynomial ring in the free coordinate. These charts cover **Spec E**, not Spec A: `(a,b)E=E`. They prove flatness over A but not faithful flatness over the whole plane (the origin is missed). They prove injectivity of `A→E` and, separately, `E∩F=A`, `F=Frac(A)`: a fraction in F lying in either monic chart has no nonconstant basis term even after passage to F, so its constant polynomial coefficient is in the corresponding `A[1/b]` or `A[1/a]`. Intersect those localizations in F. Flatness alone would not give this contraction.

In `E/(P)`, `a²=−b²`. Explicitly `1=(Da+Cb)²=b[(C²−D²)b+2CDa]`, so **b is a unit** here. Put `j=a/b`; then `j²=−1`. The row becomes `b(u+jv)²=1`. Setting `t=u+jv` gives an isomorphism, on the entire fibre,

```
E/(P) ≅ ℚ(i)[t,t⁻¹,v],    j=i,  b=t⁻²,  a=i t⁻²,  u=t−iv.
```

The inverse sends `i→a/b`, `t→u+(a/b)v`. This proves primality and nonunitness of `P` without confusing generic irreducibility with absence of vertical components. In generic-fibre language `κ((P) in A)=ℚ(i)(b)`, `b` is nonsquare by its odd order at `b=0`, and the generic ring is `κ(√(1/b))[v]`; it is integral, **not geometrically integral**. Flatness over `A/(P)` gives the needed injection into it. Upstairs `a+ib=0` sets `a=−ib`, with quotient `ℚ(i)[(u−iv)^{±1},v]` (a Laurent variable and a free one); conjugation gives the other sign. The factors are distinct, even comaximal since `(a,b)=1`. Modulo `P` the Pell root is exactly `X=j`, by `j(Da+Cb)=Ca−Db`; on `a+ib=0` it is `−i`, not `+i`. Also `Y=t(t−2jv)≠0` on this fibre. Thus neither Pell coordinate is divisible by `P` (and the rational-prime persistence with injective residue-field maps preserves these nonzero residues).

### 3. Positive ES triples descend (PROVED)

Over `F`, the discriminant of `H` as a binary quadratic is `4P`, nonsquare since `a²+b²` is prime in **A**. Thus the associated graded ring of `E⊗F` by total `(u,v)`-degree is the domain `F[u,v]/(H)` (principal initial ideal). Degrees of nonzero products add, degree zero means F. At the degree valuation the reciprocals of positive-degree denominators vanish; all remaining denominators are constants. Since reduction embeds F, these constants already sum in reciprocals to the full old target `4/P`. Subtract in the original ordered field: any omitted term would be strictly positive. Thus all denominators belong to `E∩F=A`. The second descent is the circle `A=ℚ[S][a,b]/(a²+b²−S)` with `S=P`: over `ℚ(S)` the leading form `a²+b²` is irreducible since `−1` is nonsquare. Apply the same argument; monic normal form gives `A∩ℚ(S)=ℚ[S]`. It is the *generic* degree filtration in each descent, not a degree test on the rank-one special fibre.

### 4. Integral square-unit marks and finite-prefix density (PROVED)

On `Y≠0`, matrix inversion gives a polynomial localization chart with **independent** coordinates `u,v,X`:

```
a=(CX+D)/Y²,   b=(C−DX)/Y²,   P=(1+X²)/Y².
```

For each large odd `q`, sample `(u,v)` uniformly subject to `Y≠0`, and independently `X` uniformly subject to `1+X²` a nonzero square. The number of pairs is `q²−1` if `−1` is nonsquare, `(q−1)²` otherwise. The number of allowed `X` is `(q−1−#roots_q(−1))/2`: parametrize `w²−X²=1` by `s=w+X∈𝔽_q^×`, remove `w=0`, and divide by two. The inverse chart is unique, so the largest root atom is `O(q⁻³)`, exactly what the existing finite-prefix proof requires in dimension three. Equivalently the square pullback has the rational chart `X=(s−s⁻¹)/2`, `Y√P=(s+s⁻¹)/2`. Do **not** adjoin `√P` to the ordered base. Lift the three independent root coordinates transcendently in the selected cylinders; `Y` stays a unit and `P` remains square by odd Hensel. All four original coordinates and `X,Y` are integral at these places.

At each finite exception (including 2 and the prime divisors of 840), work in this same chart in an integral open near `(u,v,X)=(1,0,0)`. There `Y=P=1` at the center; take the neighborhood deep enough to have `P≡1 mod q^{v_q(840)}` and a unit square (`1 mod 8` suffices at 2). Choose the coordinates independently transcendental in the open, never equal to the center. This does **not** impose `P≡1 mod q` at infinitely many places, which would defeat parsimony for `P−1`. If prescribing a different primitive square class, locally choose a square unit `π` in that class, set `X=0`, and take `Y` a signed inverse square root of `π`. Odd local norm maps represent every unit `Y=u²+v²` (smooth finite-field norm lift); at 2 choose the sign making `Y≡1 mod 4`, choose `v=0` or `2` to leave `Y−v²≡1 mod 8`, and take its square root. Perturb this local center as before. This only prescribes congruences and squarehood, not the exact local value of P.

### 5. Tower interface and scope

**PROVED relative to the cited tower lemmas.** Rebuild the finite tree from this root, keeping every later edge and acceptance rule. Its fixed-prefix union bound uses the new `O(q⁻³)` root mass and the same child masses; its tail rules never change an old mark. Thus every root coordinate belongs to the adelic pullback `R`; `P` is a permanent rational-stage prime with valuation zero at every mark, hence prime **as written** in `R`. It is already Gaussian-split so the TS fork never targets an associate of it. The stage proofs of countability, floors, PID, Dirichlet, TS, NR, four squares and positive ES descent apply unchanged. Section 3 completes descent to polynomials in `P`; marked integrality and positivity at infinite `P` would solve its primitive square class by polynomials, excluded as in `LOGIC_SPLIT_SQUARE_TEST.md`. Only the ES denominators are specialized, not the Pell witness.

Even the optional residue-field prescription of `LOGIC_PRESCRIBED_FIELD_AT_P.md` has the required starting embedding: `Frac(E/PE)=ℚ(i)(t,v)`, so use **two** independent elements of the prescribed infinite-transcendence-degree field. Both Gaussian components have this same fraction field over the real fibre; the later prescription edges and their ordinary mark charts are unchanged. The named residue `X` cannot be chosen independently: it already equals `a/b=i` modulo `P`. In the optional pseudofinite instance one can name a nonresidue by `v−1` instead, by initializing `v` as `1+` the specified transcendental nonresidue and choosing `t` independently.

**Falsifiers.** F1: at an ordinary square `P=m²>1`, `(mY−X)(mY+X)=1` precludes a positive integral Pell witness. The proof never requires one there. F2: no numerator-8 theorem. F3: primality here is in the nonstandard PID, not a specialization theorem at composite inputs. F4: no change to any ordinary exceptional-set count.

**CERTIFIED finite regression, not proof of the tower:** `(ulimit -v 800000; timeout 60 env UV_OFFLINE=1 uv run --no-sync python scripts/z74_negative_pell_root.py)`.
