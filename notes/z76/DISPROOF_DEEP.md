Result: Vieta descent gives sterile non-BM fibres at every even c with n=c²+1, counting gives them for almost all primes both at c=⌊p^α⌋ (fixed 0<α<1) and at c=⌊(log p)^4⌋, and the full BM test upstairs already inherits coordinate reconstruction downstairs.  Label: PROVED (relative to Z58_STRUCT2 Prop F and z75's open BM result)
Scope: Positive integral fixed-c Type II fibres of the regular model, not nonexistence of unrestricted Type II or ES solutions; the square-cover result distinguishes inherited unrestricted BM from an intrinsic bounded obstruction. ES is open.
Review: cross-model (Astra lane; Opus `data/z76/opus_review/REVIEW_OPUS.md`, responses `FOLLOWUP.md`)
Triage: BARRIER-SCOPED (fibres); separate record in `DISPROOF_COMP.md`
STATUS delta: none for theory; see `DISPROOF_COMP.md` §0 for the record proposal.

# 1. Descent in the parameter: a positive quadratic shift

Use the **whole regular fibre** Y_{n,c}: 4abcd=a+b+nc, with n,c fixed, a,b,d positive integers. Here “non-BM sterile” means no such point, but nonempty positive-real/integral-finite Brauer set for the ordinary Brauer group of this fibre. For odd n, this last condition is exactly s(n)∤c, with s the squarefree kernel (Z58_STRUCT2 Prop F). This is not the Brauer group of the coordinate-deletion open used in §3 below.

**Theorem 1.** For every even c≥2 the fibre at **n=c²+1** is non-BM sterile. In particular c=⌊√n⌋. More generally, for each fixed positive odd r, all but O_r(log(2X)) even c≤X coprime to r give non-BM sterile fibres at **n=c²+r**.

*Proof.* Put e=4abd−n=(a+b)/c. Eliminating b gives

    c² + 4da² + e+r = 4ade c,      b=ce−a.                   (1)

Now **vary c as well as a**, keeping the positive integers d,e and r fixed. The two Vieta replacements are c↦4ade−c and a↦ce−a. Both preserve positive integral solutions of (1): the products of the two roots are 4da²+e+r and (c²+e+r)/(4d), respectively, and the root sums are integral. Evenness of c is preserved, and the complementary root in a supplies b>0 throughout. This is not a Vieta move within X_n or within a single fibre.

Whenever a replacement strictly lowers a+c make it; termination gives c≤2ade and a≤ce/2. Write x=c, y=2√d a, v=e√d, w=min(x,y) and t=max(x,y)/w. At termination 1≤t≤v by these two inequalities. Hence

    e+r = (2vt−t²−1)w² ≥ (2v−2)w² ≥ 8e√d−8,                 (2)

since w≥2 and the quadratic is increasing on [1,v]. The case d=e=1 is impossible: then (1) reads (c−2a)²=−(1+r). In particular e≤(r+8)/7, √d≤(r+8+e)/(8e). For r=1 we must have e≤1; yet e≡−n≡3 mod 4 since c is even. There are **no** solutions. Moreover n is strictly between c² and (c+1)² and (n,c)=1, so the BM set is nonempty. These failures include infinitely many in-𝔐 composites (e.g. impose c≡0 mod 840, c≡5 mod 13, so 13 divides c²+1). No prime-values conjecture for c²+1 is used. The reviewer noted that r=5,9,17,21 also give sterility for every even c: at 5,9 the bound on e excludes e≡3 (4); at 17,21 it forces e=3, d=1. Writing h=c/2 then gives (h−3a)²=8a²−(3+r)/4, a nonsquare modulo 8 (respectively 3 or 2). For these extra shifts require (c,r)=1 and sufficiently large c for the non-BM conclusion.

For general r, (2) leaves only finitely many d,e. For each, v>1 and (2) bounds w, while t≤v bounds the other coordinate. Thus all orbits issue from finitely many explicitly enumerable reduced pairs. The two linear involutions on (c,a) have product of determinant 1 and trace 4de²−2>2. Every reduced word in them alternates, so the orbit is contained in the sequences of powers of this product on the seed and its reflection (both signs of the exponent). The eigenvalues are λ,λ⁻¹ with λ>1. Neither coefficient of a seed in the eigenbasis can vanish: the preserved homogeneous quadratic form in (1) vanishes on the eigenlines but equals −(e+r) on the orbit. The norm of the pair thus grows exponentially in both tails. On positive solutions with c≤X, a<ec≤eX; hence only O_r(log(2X)) terms occur. For sufficiently large c, n lies strictly between successive squares; coprimality ensures s(n)∤c. This proves the claim. ∎

For the opposite sign there need not be any scarcity: at n=c²−1 every even c gives a=b=c/2, d=e=1. Here the positive-defect argument in (2) degenerates. At a nonempty positive shift r=3 there really is a hyperbolic orbit (seed c=2,a=1,d=2,e=1, alternately increase c and a). The z75 cutoff cannot give Theorem 1: if c²≤n<(c+1)² and c is large then j=⌊n/c⌋=c+O(1) and M(j)≥j²/16−1>c. This applies to any representation c=⌊n/j⌋ as well, since then j=n/c+O(n/c²+1). The small computations `scripts/z76_fibre_checks.py` compare a direct exhaustive (a,d) loop and a different (e,a) loop at 18 shifts, every even c≤200; these are sanity checks, not extrapolations. Output `data/z76/disproof/theory.txt`.

# 2. Two distinct ways to go *below* square-root height

**Theorem 2 (every input, freely chosen height).** Uniformly for n≥2, 1≤C≤n, the number of integers c∈[C,2C] whose Y_{n,c} has a positive integral point is

    ≪_ε (n/C)^{1/2} n^ε.

Thus for every fixed 1/3<α<1, every sufficiently large odd nonsquare n has non-BM sterile fibres for a proportion ≥1−1/s(n)−o(1) of the integer heights c∈[n^α,2n^α]. At primes the proportion tends to one. This is a count, not a prescribed choice of c.

*Proof.* Sort a≤b; ce=a+b≤2b, and 4abd=n+e≤n+2abd implies 2abd≤n. Thus acde≤n. With D=√(n/C), either e≤D or ad≤D. For fixed e, 4abd=n+e gives ≪_ε n^ε factorizations and c=(a+b)/e is determined. For fixed t=ad≤D there are τ(t) choices of a,d; e|(n+4a²d) by (4acd−1)e=n+4a²d. This gives ≪_ε n^ε possibilities (all numbers factored have polynomial size in n), and c is determined. Sum the two bounds. Remove the multiples of s(n) using Prop F; the error relative to the length tends to zero when α>1/3 by taking ε sufficiently small. For the strip comparison only, take α<2/3: then c≪n^{2/3−δ} with δ>0 so c<M(j) for any strip containing the pair (j∼n/c). ∎

**Theorem 3 (prescribed height, almost all inputs).** Fix 0<α<1, set c(n)=⌊n^α⌋. Of X≤n≤2X, at most

    O_α(X^{1−α/2} log²(2X))

have a positive integral point on Y_{n,c(n)}. In particular for a density-one subset of primes (also within each fixed reduced progression), the **prescribed** fibre is non-BM sterile. An exceptional set is allowed and the estimate is not uniform as α→0.

*Proof.* Write L=X^α, β=1/α>1. Then c≍_α L and c^β≤n<(c+1)^β. As above ade≤2X/c, giving O_α((X/L)log²(2X)) possible triples (a,d,e), by summing the divisor hyperbola bound for the number of products ≤O(X/L). For a fixed triple n=4ade c−4a²d−e is a **line in c**. To be counted requires

    |g(c)| ≪_α L^{β−1},     g(t)=t^β−4ade t+4a²d+e.

On the height interval g″(t)≫_α L^{β−2}. For a function with second derivative ≥κ>0, each connected piece of {|g|≤h} has length ≤4√(h/κ): compare the value at the midpoint to the average at both ends, whose difference is ≥κ(length)²/8 and ≤2h. There are at most two pieces by convexity. Thus each triple contributes O_α(√L) integers c, each fixing n. Multiply the bounds. For large primes c<p, Prop F always passes, and the prime-number theorem in a fixed progression makes the exceptional count negligible. ∎

**Polylogarithmic heights (second-pass corollary).** Even with c(n)=⌊(log n)^A⌋ for fixed A>3 (natural logarithms), the prescribed fibre is non-BM sterile for density-one primes. The number of exceptions among *all integers to sterility* on [X,2X] is O_A(X/(log X)^{A−2}). To see this, acde≤n gives O_A(X(log X)^{2−A}) triples (a,d,e) as before. Fix such a triple with a point in the shell; 4ade≪X/(log X)^A. For two admissible heights their inputs on its line differ by |n₂−n₁|=4ade|c₂−c₁|. The mean value theorem on [X,2X] gives

    |c₂−c₁| < 1 + O_A((log X)^{A−1}/X) · 4ade · |c₂−c₁|.

For large X the coefficient of |c₂−c₁| on the right is <1/2, hence |c₂−c₁|<2: at most two integer heights. This proves the bound and it is o(X/log X) for A>3. Prop F again supplies the positive-integral BM set at every prime in range. This density-one conclusion doesn't project to an R-zero: it describes the failure of **one specified height**. None of these arguments treat c=1 on an infinite nonsquare family.

# 3. Square Kummer covers: the obstruction downstairs cannot disappear

Here switch to V=S_n°, X_n° or U_n° of `notes/z75/DISPROOF_OBSTRUCT.md`, deleting all coordinate zeros, and its adelic domain D (original model integral at every finite place, coordinates positive at infinity, units almost everywhere). Fix a simultaneous coordinate-root torsor of level m; π_a:W_a→V ranges over its rational twists. For the question *with the whole Br upstairs* the answer, for **every** m including 1 and 2, is

    D ∩ ⋃_a π_a(W_a(𝔸)^Br) ≠ ∅    iff    the original model has a positive integral point.       (3)

This is precisely the “Sharper opposite endpoint” of `notes/z75/DISPROOF_OBSTRUCT.md` §3 (refining Z58_STRUCT2 Prop T) plus functoriality, not a secondary obstruction. Indeed functoriality gives π_a(W_a(𝔸)^Br)⊂V(𝔸)^Br. For each original coordinate x, let Q_x be the positive integer from the finite valuations. Pair with the classes (χ,x) where χ ranges over characters of 2-power conductor, of **unbounded order**. After division by Q_x, local reciprocity sends the normalized idèle to x₂/Q_x (up to inversion) in ℤ₂^×; at odd places it is a unit and the characters are unramified, at infinity it is positive. Orthogonality gives x₂=Q_x. The equation at 2 therefore holds on those integers. Conversely any positive integral point lifts diagonally to the twist given by its coordinates. This proves (3), even using only pullbacks in the forward direction. For an arbitrary finite torsor use its fibre at the point as twisting torsor in the converse. In particular every twist has empty restricted BM image at 4545 on X (k=4) and 131,241 on U (k=8). The global failures have independent no-shortcut checks in z75, `data/z75/obstruct/controls.txt`. No restriction to a finite subgroup of Br on either side follows from (3).

**An explicit single algebra on the proposed square-level lift.** In the z75 one-prime m=2 patch let x=B on S, b on embedded X, or z=nBC on the image in U. Use the square twist normalized by the rational point P before repair. It has a unit y with y²=x/x(P) (the original coordinates and the arrangement coordinates are related by invertible integral monomial transformations up to constants). On **any** lift of this patch y_v is ±1 except at q where it is ±q. This patch cannot choose a different twist to evade the test: a rational ratio locally square everywhere is a rational square (even valuations and positive sign). Choose a prime L≡1 mod 4 with (q/L)=−1 by reciprocity and Dirichlet. The quaternion **(L,y)** belongs to Br(W_a)[2] because y is a unit. All local signs contributed by −1 are + (L≡1 mod 4: at L, −1 is a square, at 2 the symbol (L,−1)₂=+1, at the remaining places both entries are units at odd primes or L is real-positive). At q we get (L,q)_q=−1. Thus this one algebra rejects **every** lift of that patched point. One can take (n,k,q,L)=(4545,4,11,13), (131,8,7,5), (241,8,7,5).

This is not a new explanation of *emptiness for all patches*. In fact the displayed detector itself comes from an order-four class: extend the Legendre character of conductor L as twice a quartic character ψ of that conductor; π_a^*(ψ,x/x(P))=(2ψ,y). It is invisible to the downstairs order-two test, not to the order-four test. Using q⁴ in the original repair (with the level-four local power condition) makes y_q=±q² and avoids this detector **on the level-two cover only**. On a level-four lift let z⁴=x/x(P) and now choose L≡1 mod 8 with (q/L)=−1. Then (L,z) detects it again: local fourth roots of unity do not affect the signs (in particular those at L are squares, and L is a square at 2). A subgroup of pullbacks at **fixed bounded order downstairs** cannot explain these nonsquare failures by z75 §3. A genuinely additional question is whether a prescribed test of **bounded Brauer exponent upstairs**, uniform over all rational twists of a specified finite cover, suffices at any of the failed inputs. (Or specify a subgroup complementary to the inherited classes; a quotient modulo pullbacks alone need not have a pairing on nonorthogonal points.) We do not decide that question. The suggested alternative that finite geometric exponent alone makes *unrestricted* Br upstairs blind is false by (3); the opposing interpretation as a new secondary cohomological obstruction does not follow either.

# 4. Unrestricted searches and matched controls

`DISPROOF_COMP.md` gives the independent certificates for the new R₈ record, control arm construction, exact caliper/dropout counts, full raw-data pointers, and replay. The exact p mod 1,058,400 match preserves a large late-witness difference for p=m²+1 (367/699 vs 128/699), a weaker difference for smooth p−1, and little consistent difference for prime 12p+1. Excluding the moduli that a square shift cannot hit reverses the first comparison. The **actual new zero** lies outside both the square-shift and 61-smooth strata. No 15th R-zero or 4th Type A zero was found among the 7,723 distinct exact-fallback primes or on the two hard-feature panels. No composite counterexample or independent large-prime *full ES* count is claimed; R/R₈ are not full counts.

Reproduce theory checks: `ulimit -v 6000000; timeout 180 uv run --offline --no-project python scripts/z76_fibre_checks.py`. Scope screens: squares may already fail BM on the regular fibre, and numerator 8 is tested computationally rather than assumed to behave like 4; the record survives as a full 8/p positive, while (3) is tautological even at the known unrestricted failures. No prime-point existence statement is deduced from an average.
