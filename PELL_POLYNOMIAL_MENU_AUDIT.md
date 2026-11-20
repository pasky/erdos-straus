# Ordinary primes: finite polynomial menus fed arbitrary negative-Pell witnesses

(§0 block: z74 Opus xreview fix)
```
Result: independent proof that a finite polynomial menu over ℚ[P,X,Y] fed arbitrary integral Pell solutions has
        O(√B) hit integers ≤B in 1 mod M; an engineered nonidentity prime hit p=142211032321 ≡ 1 mod 840.
Label: PROVED (rel. Siegel's integral-point theorem, ineffective; or the thin-set count of §2). §4 CERTIFIED (exact,
       trial-division primality; independently recomputed).
Scope: polynomial finite menus; not a statement about ES; rational functions and auxiliary search not covered.
Review: cross-model (Claude Opus), data/z74/xreview/REVIEW_PELLNOGO_OPUS.md — ACCEPT-WITH-FIXES (§0, citation precision).
Triage: BARRIER-SCOPED
STATUS delta: none
```

**PROVED (unconditional no-go, not failure of ES).** Fix finitely many triples `G=(G₁,G₂,G₃)` in `ℚ[P,X,Y]`. Fix any `M` divisible by 840 and a common coefficient denominator. Call an integer `p>1` a hit if for *some* integer pair `x²+1=p y²` and *some* menu entry the three values are positive integers with reciprocal sum `4/p`. Among `p≤B`, `p≡1 mod M`, there are `O_menu(√B)` hit **integers** by the curve argument below (not an effective Siegel bound). In particular a relative natural density one of the primes in that fixed progression defeats the whole menu, even with unrestricted choice of the Pell solution. Nothing limits `x,y` in the statement. Primality is only needed for the final density interpretation.

## 1. Identities: no hits in the progression

Work in `S=ℚ[P,Y][X]/(X²+1−P Y²)`, a domain, with the monic basis `1,X`. Discard an entry with an identically zero denominator. Form `H=4G₁G₂G₃−P(G₁G₂+G₁G₃+G₂G₃)` **in S**.

If `H=0`, pass to the generic fibre over `F=ℚ(P)` and filter by total `(X,Y)` degree. The associated graded is `F[X,Y]/(X²−P Y²)`, a domain since `P` is nonsquare in F. Lower terms cannot change the principal leading ideal. Thus minus degree is a valuation, degree zero in the fibre ring means F, and in `4/P=Σ1/G_i` taking the residue drops precisely the nonconstant denominators. Since the valuation is trivial on F, the constant denominators already give the entire reciprocal sum in F. Their difference from the full sum is an identity of rational functions, hence the omitted reciprocals sum to zero at **every point where all denominators and P are nonzero** (clear the denominators). In particular, if there is even one positive hit, none were omitted. One must not claim that every signed identity consists of fibre constants: `(P/4,X,−X)` is a counterexample.

Now `S∩F=ℚ[P]` by monic normal form. Moreover reducing by `X²=P Y²−1` introduces **no coefficient denominators**, so the descended polynomials `g_i(P)` still have coefficient denominators dividing M. If all `g_i(p)>0` at a hit, this holds throughout the real interval `(0,∞)`: on the common positive locus the identity bounds each `g_i(s)≥s/4`, so that nonempty open locus is also closed in `(0,∞)`. For `p≡1 mod M`, integrality of `g_i(p)` gives integrality of `g_i(1)` by reduction of `M g_i` modulo M. This would give `4=Σ1/g_i(1)≤3`. **On the class 1 no Mordell–Schinzel or ET theorem is needed.** It is the descended identity that is evaluated at 1; no positive Pell pair at 1 is required.

## 2. Nonidentities: thin projection, not a claim that all hits disappear

If `H≠0`, its zero locus on the integral affine surface S has dimension at most one. A vertical component contributes at most one rational P-value, however many Pell pairs it contains. Reduce, normalize horizontal curves, omit finitely many singular/intersection points and take smooth projective models with the nonconstant map `P:C→ℙ¹`. A ℚ-irreducible curve that is not geometrically irreducible has no smooth rational points: geometric components are conjugate and a rational point must be on all of them. No geometric-integrality assumption on **the whole zero locus** is needed.

Every remaining cover has degree `d≥2`. Degree one would identify `ℚ(C)` with `ℚ(P)`, giving rational functions `X(P),Y(P)` with `X²+1=P Y²`. Specialize at a negative rational value avoiding their finitely many poles: the left side is positive and the right side nonpositive. This also rules out a rational point at infinity of the generic *projective* conic (there it would force P square). Thus the projected rational points are in a thin set of `ℚ` in the usual type-I/type-II sense. Merely saying “density zero among integers” is **not** enough for density relative to primes. The classical quantitative Hilbert irreducibility estimate for integer parameters in a fixed thin subset of the affine line (`O(√B log B)`, Serre, *Lectures on the Mordell–Weil Theorem*, chapter on the large sieve and Hilbert irreducibility) suffices. (z74 Opus xreview fix, precise references: Serre, *Lectures on the Mordell–Weil Theorem*, Vieweg 1989, §13 Thm 1 gives `B^{1/2}(log B)^γ`, `γ<1`, and §9.7 gives `O(B^{1/2})` via Siegel — section numbers as cited in Paredes–Sasyk, arXiv:2202.10420v2, pp. 1–3. Paredes–Sasyk Thm 1.1 itself gives an **effective** `O(√B)` for each irreducible `G(T,Z)`, as used in `PELL_ES_MENU_NOGO.md`; the "not an effective Siegel bound" caveat in the headline refers only to the §3 route.) It counts distinct P-values, not solutions in a box involving X or Y.

## 3. Independent count: Siegel once, then elementary estimates

This route does not need quantitative HIT. It is **not wholly elementary**: it uses Siegel's integral-point theorem. On the smooth projective model of a fixed horizontal component remove the **distinct geometric poles of P**, obtaining a curve finite over `𝔸¹_P` (normalization of the affine line in its finite function-field extension). Rational lifts with integer P are S-integral on this affine curve for one fixed finite set of primes: choose finitely many algebra generators integral over `ℚ[P]`, clear the coefficient denominators of their monic equations, and evaluate. A rational number integral over `ℤ[1/N]` lies in that same ring. In particular this count does not require integrality bounds on the original affine coordinates, even near omitted points of their parametrization.

By Siegel there are only finitely many such points if the genus is positive or there are at least three geometric poles. Otherwise, in the presence of a rational point the genus-zero projective model is `ℙ¹` over ℚ. Write `P=f(A,B₀)/g(A,B₀)` in primitive homogeneous parameter coordinates, with coprime integral forms of the same degree `d≥2` and no common projective zero. Use a different letter `T` for the height cutoff here. Two elementary bounds when `1≤P≤T` is integral:

* `g(A,B₀)` is a nonzero divisor of a fixed nonzero integer. Indeed the gcd of the two form values divides a fixed resultant bound on coprime coordinates (homogeneous Bézout identities for powers of each coordinate). Integrality gives `g|f`.
* `max(|A|,|B₀|)≪T^(1/d)`: the maximum of the absolute form values on the real unit sup-norm boundary has a positive **minimum**, by absence of common zeros. Rescale; use `|f|≤T |g|` and the fixed bound on `|g|`.

With **one pole**, it is rational and `g` is a scalar times a `d`th power of a rational linear form. The integer parameters lie on finitely many fixed lines in this box, giving `O(T^(1/d))` points. With **two rational poles**, `g` is a product of powers of two independent rational linear forms, so both primitive integral linear-form values are confined to finite nonzero sets. This gives `O(1)`. With **two conjugate poles**, `g` is a scalar times a power of an irreducible integral binary quadratic `Q`; hence `Q(A,B₀)=m` lies in a finite list of nonzero levels. Definite forms give finitely many points. For an indefinite form `Q=hA²+kAB₀+lB₀²`, its discriminant `D=k²−4hl>0` is nonsquare and `h≠0`. The algebraic integer `α=2hA+kB₀+B₀√D` has fixed nonzero norm `n=4hm`. Its two real absolute values are `O(T^(1/d))`, so `|α|` also has a reciprocal-polynomial lower bound. At fixed sign, two distinct such values have ratio `r>1` in increasing absolute order, with `1≤|N(α'−α)|=|n|(r−1)²/r`. Thus their magnitudes grow by a fixed factor: `O(log(2T))` choices, without assuming a fundamental-unit algorithm. The map from the integer pair to α is injective. This exhausts the poles and proves the asserted `O(√T)` bound, with fixed-menu constants. PNT in the fixed progression gives the denominator `∼T/(φ(M) log T)`. There is no uniform bound in the degree, coefficients, M or menu size claimed here.

## 4. Accidental hard-class hit (CERTIFIED)

Here is a nonidentity in which the Pell coordinate is used as a putative factor of `(P+3)/4`. Fix `c=867140441`, `K=(P+3)/4`, and use the single polynomial triple

```
(K,  Pc(Y+1)/3,  PcY(Y+1)/3).
```

Away from zero denominators, the last two reciprocals sum to `3/(PcY)`, and the required residual is `3/(PK)`. Hence it works in positive rationals **exactly on `K=cY`**, not identically on the surface. This is a horizontal cut, `X²=4cY³−3Y²−1`, not a constant menu for one vertical input. The cubic has no repeated root (`Y=0,1/(2c)` both fail), hence this example's integral hits are finite by Siegel. The denominator modulus is absorbed by `M=840`. At

```
p=142211032321,    x=15461460,    y=41,
```

`p≡1 mod 840`, `x²+1=41²p`, `K=41c`, `3|y+1`. The triple is `(35552758081,1726437121946560709854,70783921999808989104014)`. Trial division through `⌊√p⌋=377108` certifies primality. One way to find it was to choose `y=41`, require `x≡0 mod 420` and `x²≡−1−3y² mod y³`, and test the resulting p; then fix `c=K/y`. This is an engineered witness, not evidence of infinitely many prime exceptions. The two-term split is the familiar ET-type factor split; it is the *accidental tying of its factor to the Pell coordinate* that matters here.

**Scope / falsifiers.** F1: evaluation at 1 excludes identities; this does not assert failure of ordinary ES at odd squares. F2: no numerator-eight transfer is asserted. F3: the counting bound even includes positive composite parameters on the progression. F4: an ES solution from a different rule at any prime is entirely compatible; no claim about restricted-zero lists. Polynomial representatives and finite menus are essential hypotheses here. Variable-denominator rational functions, inequalities with auxiliary search, and infinite menus are not excluded by this proof.
