# ZF0 part 3 — completed first steps

Nine items: 7 interesting, 2 nothing, 0 covered/needs-compute/skipped; individual records are in `data/z52b/pass2/ZF0_part3.jsonl`.
Interesting: Z0016, Z0272, Z0524, Z2708, Z2814, Z2834, Z2860.
Bounded negative/diagnostic results: Z0076, Z3063.
CERTIFIED means exact finite computation, not a claim about all ES inputs.
ES remains OPEN. The new Brauer calculation below deserves independent mathematical review.

## Z0016 — what Mason/abc actually bounds

**PROVED.** `SIZE_CONJECTURE.md` contains no occurrence of “Mason” or “abc”; the previous covered verdict was false. Over a field of characteristic different from 2, rearrange ES as

`A + B = D`, with `A=nxy`, `B=nxz`, `D=yz(4x−n)`.

For nonzero polynomial denominators and n, divide by `G=gcd(A,B,D)`. The resulting a,b,c are pairwise coprime. Provided they are not all derivative-zero, Mason–Stothers gives

`max(deg(nxy),deg(nxz),deg(yz(4x−n))) − deg G ≤ deg rad(ABD/G³) − 1 ≤ deg rad(nxyz(4x−n)) − 1`.

A nondegenerate equality example over every odd-characteristic function field is `n=3T−1`, `(x,y,z)=(T,T(3T−1),3T−1)`: its primitive triple is `(T,1,T+1)`, so max degree 1 equals radical degree 2 minus 1. The script checks the polynomial identity and cancellation symbolically. The derivative proviso is essential: a/b=y/z, so a constant or p-th-power y/z makes this application degenerate. This is a radical-dependent inequality, not an upper bound for the largest denominator in terms of deg n alone.

**CONDITIONAL (integer abc).** For the same primitive positive integer triple,
`max(A,B,D)/G ≤ Kε rad(ABD/G³)^(1+ε)`.
The constant Kε cannot be set to 1; computing abc qualities is not a test proving/disproving abc.

**PROVED diagnostic.** The exact certificate `n=4abC−a−b` has `(x,y,z)=(abC,aCn,bCn)`. The primitive additive triple above is exactly `(a/g,b/g,(a+b)/g)`, `g=gcd(a,b)`: both n and C disappear. Thus varying C makes ES denominators arbitrarily large without changing this abc quality. For polynomial C and constant a,b the Mason derivative hypothesis fails altogether.

**CERTIFIED.** 232598 exact ES solutions with 1≤a≤b≤200, 1≤C≤12 and 2≤n≤10^6 give 12232 distinct primitive additive triples; max n=999946, max denominator=2395430400. The largest quality is 1.4265653296 at (3,125,128), radical 30; 573 sampled solutions have quality >1.

Reproduce: `uv run --with sympy python scripts/z52d_p2_ZF0_Z0016_abc.py`; exact counts/maximum quality are in `data/z52b/pass2/ZF0/Z0016/abc.json`.

## Z0076 — an actual non-UFD sector search

**CERTIFIED bounded experiment.** In `Z[sqrt(−5)]`, use the closed 90-degree sector `a>0, 5b²≤a²`, and require **all three** denominator norms `a²+5b²≤B`. Enumerate x≤y in lexicographic coefficient order and compute z exactly by conjugate division; retain y≤z and check the same sector/norm bounds. The searches use B=100,400,2500,10000,40000 and every split rational prime p≤1000. The necessary real-part inequality is `p≤4sqrt(2B)/3`, so larger primes are certified impossible in this bounded cone, not unsearched.

At B=40000, within that nonvacuous range, principal splitting classes 1,9 mod20 have 9/13 successful primes, 51 unordered triples (50 genuinely nonrational); nonprincipal classes 3,7 mod20 have 9/19 successful primes, 51 triples (36 nonrational). Every successful prime in each group has a nonrational solution. Failures are respectively `{229,241,281,349}` and `{107,163,167,223,227,263,283,307,347,367}`. These are bounded-search failures only. The norm cutoff and the perfect confounding with p mod4 preclude attributing this difference to the class group.

Reproduce: `gcc -O2 -o /tmp/z52d_Z0076 scripts/z52d_p2_ZF0_Z0076_search.c`, then `/tmp/z52d_Z0076 40000`. Full split-prime rows and example triples: `data/z52b/pass2/ZF0/Z0076/B40000.json`.

## Z0272 — maximal orders, and a precise units statistic

**Definition.** For each squarefree 2≤D≤100 use `O_K=Z[ω]`, `ω=sqrt D` for D≡2,3 mod4 and `ω=(1+sqrt D)/2` for D≡1 mod4. Require all denominators totally positive and all basis coefficients bounded by H. Count unordered genuinely nonrational triples. “Units needed” means a (D,p) pair has such a triple but **no** such triple with all three denominator norms different from 1. This is a bounded denominator-unit statistic, not a claim that a construction cannot multiply by a unit: the latter has no canonical meaning without choosing an orbit representative.

**CERTIFIED.** H=64, all 60 fields and all 168 primes p≤1000: 414 successful (D,p) pairs and 2232 triples, in 64.67 seconds. Seven unit-only pairs: `(29,2),(51,2),(53,2),(55,3),(70,3),(91,3),(97,3)`. The largest successful p is 67. H=32 gives 217 successful pairs and 820 triples, making cutoff sensitivity explicit. The search uses exact integer positivity and maximal-order multiplication, not floating-point embeddings. At this height many large p are excluded by positivity before any pair search; this is deliberate bounded-height scope, not evidence of unrestricted failure.

**PROVED.** For p≥5, a totally positive ES denominator is >p/4>1 in both embeddings. A totally positive unit has norm 1 and cannot satisfy this. Hence no totally positive solution at p≥5 can contain a unit denominator, at any height. In fact, for any p≥2 a nonrational totally positive norm-one unit has integral trace at least 3, so its smaller embedding is at most `(3−sqrt 5)/2<1/2≤p/4`: it cannot occur either. All seven unit-only pairs therefore use the rational denominator 1, as the recorded examples confirm. The proposed statistic measures only this p=2,3 phenomenon, not genuine quadratic units or a higher-prime bottleneck.

Reproduce: `uv run --with numpy --with sympy python scripts/z52d_p2_ZF0_Z0272_search.py 64`; `data/z52b/pass2/ZF0/Z0272/result_H64.json` contains every successful pair, count and example.

## Z0524 — residue-restricted early exit to one million

**PROVED.** Under gcd(n,q)=gcd(r,q)=1 the necessary rule is `3n≡4r (mod q)`. If q has a factor 2 or 3 there are no admissible n at all. Thus among 2≤q≤12 only q=5,7,11 need work. Each n coprime to q has a unique admissible r.

For each such n search x≡r, `n/4<x≤3n/4`. Put A=4x−n, B=nx. Recursively enumerate only divisors `d|B²`, `max(1,Ax−B)≤d≤B`, and stop on the first y=(B+d)/A, z=(B+B²/d)/A satisfying integrality and the residue condition. A successful proper divisor m of n gives a solution at n by scaling, so we reuse existence without enumerating again. This preserves the required residue by the local rule. B² uses 128-bit arithmetic. No arbitrary denominator cutoff is used in the exact run.

**CERTIFIED to n=10^6.** q=5: 799999 admissible n, 687 failures; q=7: 857142 admissible, 4771 failures; q=11: 909090 admissible, 21782 failures. Measured wall times per q are 13.34, 103.58, 421.92 seconds, concurrently. Every admissible residue r has an exact counterexample, so none of these (q,r) is universal even after the local rule. A second complete run stores every failure and separately counts gcd(n,6)=1: q=5 has 674 failures among 266665 admissible n, q=7 has 4423/285713, q=11 has 17792/303029. Every residue still has a failure in this stratum (first examples are at most 53). Its per-q times are 6.04,76.66,412.74 seconds. In `exact.txt` and `exact_stratified.txt` the counter named `unresolved` is an exhaustive failure count because x_steps=0; only the preliminary bounded run uses that name literally.

Reproduce: `gcc -O2 -fopenmp -o /tmp/z52d_Z0524 scripts/z52d_p2_ZF0_Z0524_search.c`; `/tmp/z52d_Z0524 1000000 0`. At most three OpenMP workers are active (four-thread cap). `exact.txt` contains the first exact run; `exact_stratified.txt` and `summary.json` contain the final per-residue and coprime-to-6 counts, with complete `failures_q*_N1000000_steps0.csv` lists. `exact_progress.txt` and `stratified_progress.txt` record measured timings. `run.txt` is the preliminary 32-x-step run and explicitly labels unresolved cases, never failures. `scripts/z52d_p2_ZF0_Z0524_validate.py` independently enumerates y (without factoring) for n≤200 and agrees on all 20 (q,r) rows; the summary script validates every stored failure's admissibility and reconciles all counts.

## Z2708 — actual ray classes and finite congruence lists

**PROVED.** For positive divisors, the appropriate ray group over Q has modulus `4C·∞` and is `(Z/4C)^×`; omit the real place and it becomes the quotient by ±1, which loses precisely the target sign. A prime factor ℓ of N=4Cp+1 has Artin class ℓ mod4C in `Q(ζ_(4C))`; a certificate is a **subset product** of these classes equal to −1. Frobenius of p alone modulo4C does not decide it: N always has class +1. `B2_ACROSS_FIELDS.md §1 (E1)` states the divisor reformulation but does not give the requested ray group/coverage table, so the previous “covered” citation was inadequate.

**CERTIFIED finite forcing table.** For each C≤20 the JSON lists the cyclic factors of the ray group, every d|840 with d≡−1 mod4C, and every reduced residue r mod840 for which some such d divides 4Cr+1. These are exactly the classes forced by the capped 840-smooth factor data, not all potentially coverable classes. Their union covers 148/192 reduced classes; it misses all six Mordell-hard classes `{1,121,169,289,361,529}` and 38 of Mordell's other 186 classes.

For a nonempty explicit covering at **every** C, also take d=4C−1. The condition is p≡−1 mod d. The data lists all reduced classes p mod `4C(4C−1)` satisfying it, not just a formula. This makes the extra modulus required by a known divisor explicit. There is no claim that a finite table classifies the factorization lottery for all primes.

Reproduce: `uv run --with sympy python scripts/z52d_p2_ZF0_Z2860_classes.py`; see `data/z52b/pass2/ZF0/Z2708/classes.json`.

## Z2860 — K_T, exact forcing classes and prime counts

**PROVED.** Define `K_T= compositum_(1≤t≤T) Q(sqrt(−t),ζ_t)`. For T=1,…,12 these equal Q(ζ_M), with

`M=4,8,24,24,120,120,840,840,2520,2520,27720,27720`.

For example i and sqrt(−2) generate ζ8, adding ζ3 gives ζ24; the subsequent odd cyclotomic factors give the stated list. Thus Frobenius is exactly p mod M, for p∤M.

To remove ambiguity about “level”, the certificate family tested is explicitly `E_C: ∃d|4Cp+1, d≡−1 (mod4C)`, 1≤C≤T (the c=1 family). This is not an assertion about every possible Type I/II family. The field gives the capped smooth factor `s=gcd(4Cp+1,M)`. Since [N]=1 mod4C and s is coprime to4C, CLASS_FORCING Prop 3.2 reduces to `−1∈Σ(s)`: using the opaque cofactor adds nothing, since complementation inside s converts its criterion back to the same one. Equivalently some d|M satisfies d≡−1 mod4C and `p≡−(4C)^−1 mod d`. This is an **exact abstract-factorization forcing rule**, not a theorem that no other arithmetic argument can force E_C.

**CERTIFIED.** `classes.json` explicitly enumerates every forcing Frobenius residue for each T, its exact density, and checks every unramified prime ≤10^6, also conditioning on p≡1 mod4. At T=12, 4748/5760 classes force a certificate (2374/2880 in the hard p≡1 mod4 stratum); 64747 of 78493 unramified primes are certified, including 32375 of 39174 hard primes. The p≡1 mod M class always survives. These densities concern the specified Galois-forcing layer, not actual bounded-level success probability.

Reproduce with the same script as Z2708. All integer divisibility witnesses are direct consequences of the recorded forcing d and are independently checked in the script's exact congruence test.

## Z2814 — four A1 nodes, nine nef pencils, two Weyl-chamber orbits

**PROVED, symbolic verification.** For n≠0, the projective cubic of `GEOMETRY_ES.md §2` has precisely four coordinate singularities. Their affine-chart Hessian determinants are nonzero; each is A1. Its minimal resolution is the complete-quadrilateral blow-up of P² at six rational points, indexed by edges ij of K4. Write H²=1, E_ij²=−1. The effective roots are

`R_i=H−Σ_(j≠i) E_ij`, with Gram matrix `−2 I_4`.

The ambient canonical-orthogonal root system is E6 (72 roots). The nodal subsystem is **4A1**, not a “root system of nine lines”. There is no E6 root orthogonal to all four nodal roots. The nine irreducible (−1)-curves are the six E_ij and the three `H−E_ij−E_kl` for opposite edges; these map to the six coordinate edges and three M_k of the cubic. The script substitutes all nine line equations and solves the gradient equations in all four charts using sympy.

**PROVED/CERTIFIED lattice enumeration.** Every nef conic class F=aH−ΣbE satisfies F²=0, −K·F=2, b≥0. Cauchy gives a≤3; exhaustive enumeration and nonnegative intersection with the nine (−1)-curves and four R_i leaves exactly:

* six `H−E_ij`;
* three `2H−Σ_(e not in {ij,kl}) E_e`, with {ij,kl} a perfect matching.

All nine pencils are defined over Q. They are basepoint-free line pencils through one blown-up point or conics through four points with no collinear triple. The S4 symmetry of the complete quadrilateral, embedded in W(E6) and preserving the effective root chamber, has orbits of size 6 and 3. Fixing the distinguished affine boundary node leaves S3 and splits these into 3+3+3: the F1, F2, F3 pencils in `GEOMETRY_ES.md §3.1`. Full W(E6) acts on the 27 generic conic classes, not on these nine nef classes of a fixed effective chamber; conflating these actions would give a false orbit statement. An independent full Weyl enumeration now verifies all 51840 elements: the stabilizer of the oriented four-root set has order 24, its unoriented 4A1 normalizer has order 384 and is `(C2)^4 ⋊ S4` (the four commuting node reflections and the node permutations), the respective configuration orbits have sizes 2160 and 135, and the generic conic orbit has size 27. The 24-element stabilizer again gives nef orbits 6+3 (1.89 seconds).

For a coordinate edge E_ij, the moving residual class is `−K−E_ij−R_i−R_j=H−E_kl`; omitting the fixed node components is the common source of a wrong conic count. For an opposite-edge line M the class is simply −K−M. Type I vs Type II is **not** a geometric orbit distinction: both can lie in F1 and are distinguished by integral p-divisibility in the same split hyperbola `( (4t−n)y−nt )((4t−n)z−nt)=(nt)²`. The three orbit types organize fibres, not separate ES types or new existence mechanisms.

Reproduce: `uv run --with sympy python scripts/z52d_p2_ZF0_Z2814_lattice.py`, then `uv run python scripts/z52d_p2_ZF0_Z2814_weyl.py`; exact roots, Hessians, lines, classes and orbits are in `data/z52b/pass2/ZF0/Z2814/lattice.json`, and the full group census is in `weyl.json`.

## Z2834 — the algebraic class and a compatible positive adelic point

**PROVED derivation (new; independent review requested).** Take n=3861, k=4 and
`S:4xyz−n(xy+yz+zx)=4`. Put q=4y−n, d=qz−ny, d′=qx−ny, u=4d, v=4d′. On q≠0,

`uv=f(q)=n²q²+(2n³+64)q+n⁴`,
`disc(f)=256Δ`, `Δ=n³+16=57557166397=31·167·857·12973`.

The two roots are conjugate over L=Q(sqrt Δ). Over the algebraic closure the open surface `uv=f(q), q≠0` has Picard group Z, generated by one component u=0 of a root fibre, with the other root component its negative (`div u=D1+D2`). Its only nonconstant units are powers of q. Restoring q=0 in S adds one irreducible line, of principal divisor q and multiplicity one; localization therefore leaves Pic unchanged. Galois swaps D1,D2, so `Pic(Sbar)=Z_sign` and `H¹(Q,Pic(Sbar))=Z/2`. S has rational points, e.g. `(4,0,−1/n)`. Consequently

`Br_1(S)/Br(Q)=Z/2`, generated by `B=(Δ,d)`.

Purity checks B directly: along d=0 its residue field contains sqrt Δ; along q=0 d=−n²/4 is a nonzero unit; nowhere else can it ramify. B is not constant: at ℓ=31 the integral points `(4/t,0,−t/n)` with t a unit realize either Legendre symbol (t/31), hence either invariant.

**Full-group derivation, not just algebraic (two models).** Projection to (y,z) exhibits S as the affine modification of A² along the smooth hyperbola `H:d=(4y−n)z−ny=0` at the two transverse points where `4+nyz=0`. The hyperbola is G_m with coordinate q=4y−n; its two base points have residue field L. Thus S is obtained by blowing up these points and deleting the strict transform of H. Compactifying gives `Bl_(P+,P−)(P¹×P¹)`, with boundary classes `F_y,F_z,F_y+F_z−E+−E−`; this independently recovers the sign Picard lattice. These are the same standard modification/purity tools explicitly scoped in `BRAUER_TWISTS.md §§2.2–2.3`, applied here to a different surface.

Restrict a Brauer class to `V=A²\H`. Purity and `Br(A²)=Br(Q)` inject its nonconstant part into `H¹(H,Q/Z)`. Every residue there is `χ+ε(q)`, with χ a constant character and ε∈{0,1}: the geometric invariant group is Z/2 and the rational point q=1 splits off constant characters. Extension over either exceptional line requires specialization at the degree-two base point to vanish over L. The residue of A=(−q,−d) along H is (−q); it specializes to zero because at a root q₀ of f,

`−q₀=((nq₀+n²)/8)²`.

It is geometrically nonconstant, since −q is not a square in Qbar(q). Subtracting εA from an arbitrary class leaves a constant residue character χ with χ|_L=0, so χ is either zero or the quadratic character of L/Q. The latter is exactly the residue of B=(Δ,d). Both A and B extend and have order two; therefore

`Br(S)/Br(Q)=(Z/2)²`, generated by A and B.

In particular the possible order-four extension is excluded by the explicit order-two lift A, rather than silently assumed away. As a geometric check, the projective cubic closure has three split A1 nodes at infinity; resolving gives a rational six-component boundary cycle. Its residue complex gives `Br(Sbar)=Q/Z(−1)`, again with invariant subgroup Z/2. This is a mathematical purity/cohomology derivation, not a computer certification of a Brauer group.

**PROVED local construction, CERTIFIED exact evaluations.** At the positive real point `(n,(4+n³)/(2n²),n)`, `(inv A,inv B)=(1/2,0)`. At 2 use
`(x,y,z)=(2,4,2(2n+1)/(16−3n))`; both invariants are 1/2. At 31 use `(4/3,0,−3/n)`: the invariants are `(0,1/2)`. At every other odd prime not dividing n use `(4,0,−1/n)`: both invariants vanish (for A, n is a unit and B has d=1). At 3,11,13 use `y=1, z=(n+1)/(4−n), x=4+nz`, again d=1 and both invariants zero. All these points are integral at the indicated place. Thus both A and B, and every sum of them, satisfy reciprocity on a positive-integral adelic point.

The script checks the equation, integrality and Hilbert symbols at every prime dividing `2nΔ`, and additionally every prime <100. The formulas prove the statement at every remaining prime; the extra sample is not being substituted for that proof. At 2 one indeed has the forced relation inv A=inv B=1/2 at this point; the odd ramified prime 31 supplies precisely the compensating B evaluation. Checking A alone would miss this needed compatibility.

**CERTIFIED positivity separately.** Re-running the complete divisor enumeration of `scripts/z52_bank_pencil.c` at (3861,4) gives zero positive integer triples. The x range is `966≤x≤2896`; for each x all divisor pairs of `(nx)²+4(4x−n)` are tested. Together with the Brauer derivation this is a failure of the positive-integral Brauer–Manin sufficiency statement for this particular affine integral model, not an ES counterexample and not a new claim about unrestricted integral points (negative/zero coordinates are allowed in the local constructions).

Reproduce: `uv run --with sympy python scripts/z52d_p2_ZF0_Z2834_local.py`; and `gcc -O2 -o /tmp/z52d_Z2834 scripts/z52_bank_pencil.c; /tmp/z52d_Z2834 count 4 3861 3861`. Results: `data/z52b/pass2/ZF0/Z2834/local.json`, `positive.txt`.

## Z3063 — concrete bounded formulas and the exact transfer boundary

**PROVED formulation.** For fixed B define
`Φ_B(n): ⋁_(1≤C≤B) ∃a,b [a,b≥1 ∧ n=4Cab−a−b]`.
For an individual integer n≥2 the quantifiers can be bounded by `a,b≤(n+1)/3`: from b≥1, n≥(4C−1)a−1, and symmetrically for b. Thus Φ_B(n) is decidable by finite search. Bounded quantifier complexity does **not** make `∀n≥2 Φ_B(n)` a decidable arithmetic sentence; the bound on witness size still grows with n. Replacing fixed C by `C|P(n)` does not repair this: divisibility has an existential multiplier, and finite search for each n is not a uniform truth-decision theorem.

**Concrete transferable local sentence.** In the valued-field language with valuation-ring predicate O:
`∀n∈O ∃a,b∈O^×: n=4ab−a−b`.
For every residue characteristic p>3 choose a residue a avoiding `{0,1/4,−n}` and lift it; then `b=(n+a)/(4a−1)` is a unit. Hence the sentence holds both in Q_p and F_p((t)); it is a legitimate fixed-sentence Ax–Kochen transfer example, already proved directly. It has no positivity and its witnesses need not be global integers. The local ES polynomial sentence is even more vacuous: x=y=z=3n/4 solves it in the valuation ring for p>3 and n≠0.

**PROVED nontransfer check.** Neither the polynomial subring F_p[T] nor positivity on Z is part of that valued-field statement. Degree-bounded polynomial certificates can be encoded by finitely many coefficient variables over F_q and decided by finite enumeration for each q, but Ax–Kochen does not identify those polynomial rings with Z. In fact the ring sentence `∃u,v: uv=1 ∧ u²≠1` is false in Z and true in F_q[T] for q>3, so any nonprincipal ultraproduct with q→∞ differs elementarily from Z already on units. Łoś only transfers to the ultraproduct actually constructed; it supplies no bridge to integer ES. This answers the specified logical first step without a generic “too meta” dismissal.
