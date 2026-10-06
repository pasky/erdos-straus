# Support-aware certificates: the (N2) residual of the 1/4 ceiling (task O68)

Status: CHECKPOINT 1 (self-review R68-self by a deep reviewer: 2 FATAL scope items (old Cor 3.2, SAP) and 4 MAJOR repaired by downgrading/restating). Labels as in DISCOVERIES.md. Notation as in
POINTWISE_OMEGA14.md (O14), POINTWISE_OMEGA15.md (O15), POINTWISE_OMEGA16.md (O16): `𝓛=log T`;
fibre `H={n≡r (Q)}`; F = indicator of "no ES event `E_{M,D}`, `M≤T`"; F is periodic mod
`L:=lcm(Q, M≤T)` (a T-smooth modulus up to the primes of Q); big coordinates `X_ℓ`, `ℓ>T^{0.6}`.
`A:={n∈ℤ: n∈H, F(n)=1}` (integer avoiders). `𝒫_x:={p≤x prime, p∈H, p∤L}`, `N_x:=|𝒫_x|`,
`m_x:=Σ_{p∈𝒫_x}δ_p`.

## 0. Question

O15 Def 2.1 forbids a certificate to use that `m_x` is supported on integers in `[1,x]`, is
atomic (unit point masses) and integral. O15 §6 (N2) leaves certificates using this information
open. Here: formalise them (§1), reduce them to a question about integers only (§1–§2), and
decide what can be decided.

## 1. Definitions and two reductions

**Definition 1.1 (support-aware linear certificate, SALC).** Data:
* a *support* `S⊂ℤ∩[1,x]∩H` with `𝒫_x⊆S` (canonical: `S_z:={n≤x: n∈H, (n,P(z))=1}`, `z≤T`;
  `S_T` is the natural choice since all moduli in the problem are T-smooth up to Q);
* a finite family 𝒞 of residue classes (any moduli) with bounds `l_C≤m_x(C)≤u_C` that are true
  for the primes, and the value `N_x` (or true bounds for it).

Feasible fakes: `𝔐:={m:S→[0,1] : Σ_S m=N_x, l_C≤m(C∩S)≤u_C ∀C∈𝒞}`. The SALC is *valid* iff
`min_{m∈𝔐} Σ_{n∈S}m(n)F(n)>0` (then `m_x∈𝔐` gives a prime `p≤x` in H with `F(p)=1`). The box
`m≤1` is the LP relaxation of atomicity/integrality; the *integral* version uses `m∈{0,1}^S`.
O15 Def 2.1 is the case "S replaced by H (diffuse), no box".

**Lemma 1.2 (deep classes are box constraints or primality tests; PROVED, elementary).** Let
`C∈𝒞` with `|C∩S|≤1`. If `C∩S=∅`, the constraint is vacuous on 𝔐 (or false). If `C∩S={n}`, then
either `l_C≤0` and `u_C≥1`, and the constraint is implied by the box `0≤m(n)≤1`; or `l_C>0`
(which, being true, certifies `n∈𝒫_x`) or `u_C<1` (certifies `n∉𝒫_x`), i.e. it tests whether
that integer is a *counted* prime (a prime of S dividing L is not counted).
In particular every class of modulus `q>x` meets `[1,x]` in at most one integer.
*Proof.* `m_x(C)=1[n prime]∈{0,1}`; a true bound excluding one of the two values decides it. ∎

So a SALC that does not test primality of individual integers ("primality-blind"; a search
over specific integers is not a transfer, O15 Def 2.1) gains from moduli `>x` exactly the box,
i.e. atomicity. More generally a class with `|C∩S|=s` carries information about `s` specific
integers; information about *families* of classes needs `s` large.

**Lemma 1.3 (duality: support-aware minorants; PROVED, LP duality).** A SALC (LP version) is valid
iff there are `α∈ℝ`, `β_C,γ_C≥0` (`C∈𝒞`) and `θ_n≥0` (`n∈S`) with

```
B(n):=α+Σ_C(β_C−γ_C)1_C(n) ≤ F(n)+θ_n   (n∈S),     αN_x+Σ_C(β_Cl_C−γ_Cu_C)−Σ_nθ_n > 0 .
```

*Proof.* `min{Σ F m: m∈𝔐}` is a feasible (`m_x∈𝔐`), bounded LP; strong duality. ∎
Compared with the Haar picture (O14/O15: `B≤F` Haar-a.e. on H), the constraint is imposed only
at the integers of S, and the box adds the slack `θ_n` at cost `θ_n` (a point mass ≤ 1).
Equivalently, after scaling: `B≤0` on `S∖A` (non-avoider integers), with `θ` paying for
violations at single points.

**Remark 1.4 (primes leave the question when the bounds are Haar-type).** If every bound used
has the form `|m(C)−N_xP_H(C)|≤𝔈_C` (Haar main term, any true accuracies), then 𝔐 depends on
the primes only through `N_x` and the numbers `𝔈_C`; validity is the statement that *no*
box-bounded measure on the integer set `S∖A` of mass `N_x` has Haar class statistics on 𝒞 within
`𝔈_C`. This is a question about the integers `≤x` and the system F alone (the "integer fake
problem" IF(S,𝒞,𝔈)). Note `|S_T|/N_x≍log x/𝓛`, so the box is far from binding globally: a fake may
concentrate on a subset of S of relative density `≍𝓛/log x`.

## 2. What an integer fake must look like

A fake for a SALC must be a box-bounded measure on the *integers* of `S∖A`. The Haar fake of
O14/O15 is `N_xν` with ν the planted law; its density `dν/dP` is *deep* (it depends on whether
almost all big events are off), so restricting it to integers `≤x` requires counting integers in
sifted sets of dimension `κ≍𝓛³/log𝓛` — exactly the sieve problem below its sieving limit. The
following lemma shows that some depth is unavoidable.

**Lemma 2.1 (no monotone fake; PROVED, Harris).** Let `z∈{0,1}^n` have independent coordinates
with `P(z_b=1)=p_b∈(0,1)`, and let `ψ≥0` be coordinatewise nondecreasing with `ψ(0)=0` and
`E[ψz_b]=p_bE[ψ]` for all b (ψP has the same one-dimensional marginals as P). Then `ψ≡0`.
*Proof.* `E[ψz_b]−p_bEψ=p_b(1−p_b)E[ψ(z^{b→1})−ψ(z^{b→0})]` (the bracket depends only on the other
coordinates). Each bracket is `≥0` by monotonicity, P has full support, so equality forces
`ψ(z^{b→1})=ψ(z^{b→0})` for all z and b: ψ is constant, `=ψ(0)=0`. ∎

*Reading.* Nonnegative combinations of event classes (`n≡−4D (M)`, possibly intersected with
arbitrary small-coordinate cells) are nondecreasing in the big bits given the small coordinates.
So no fake built only from "these events hold" can match even the first-order statistics
`P(C_s∩{X_ℓ∈Ω_ℓ})` that every sieve certificate uses; the fake must also reward "these events do
*not* hold". Lemma 2.1 excludes monotone fakes, not shallow ones. For a fake given by a polynomial of
low degree in the event indicators, the integers in it can be counted by the fundamental lemma
(§3). For a deep fake, counting them is a sieve problem beyond the sieving limit.

## 3. Shallow planting (exchangeable model)

*Shallow* = density which is a polynomial of low degree d in the event indicators, i.e. a
combination of classes of modulus `≤T^d`; such a density restricted to integers is controlled
by the fundamental lemma as long as `D·T^d≤x^{1−ε}` (D = level of the certificate's classes).

**Proposition 3.1 (Charlier fake; identities PROVED, positivity EVIDENCE).** Let `N~Poisson(R)`
(number of big events on, exchangeable model) and `n≥1` odd. Put
`ψ_n(j):=1−C_n(j;R)`, `C_n(j;R)=Σ_{r≤n}C(n,r)(−1)^r(j)_r/R^r` (Charlier). Then (i) `ψ_n(0)=0`;
(ii) `E[ψ_n(N)q(N)]=E[q(N)]` for every polynomial q of degree `<n` (orthogonality of Charlier
polynomials), so `ψ_nP` has the same factorial moments up to order `n−1` as `P`; (iii) `ψ_n` has
degree n, i.e. it is the combination `Σ_rC(n,r)(−1)^{r+1}R^{−r}r!·Σ_{|Y|=r}1[all events of Y hold]`
of classes of modulus `≤T^n` — shallow. (iv) EVIDENCE (exact rational arithmetic, all
`1≤j≤4R+6n+20`; for `j` larger `C_n(j;R)<0` as n is odd): `ψ_n≥0` on ℕ iff `R≥R_min(n)` with

| n=k+1 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 21 | 25 | 31 | 41 | 61 | 81 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R_min | 1 | 2 | 5 | 9 | 13 | 18 | 23 | 28 | 33 | 44 | 56 | 74 | 104 | 169 | 236 |

(R_min = least *integer* R on the grid; for n=1, `ψ_1(j)=j/R≥0` for every R>0. `n≥31` by
bisection in R, assuming monotonicity in R. The cutoff `j≤4R+6n+20` is not proved to be beyond
the last sign change; a root bound is owed.) `R_min/n` grows slowly (2.9 at n=81; the growth
rate is not established). The deep planting needs `R≳n` (O14 Lemma 1.1); on this grid the
shallow one needs `R≲3n` for `n≤81`. On `j≤2R`, `max ψ_n` is close to 1 (1.09 at n=7, 1.000 at
n=21), but ψ_n is an unbounded polynomial, so **no global box holds**: a capped shallow fake
needs a tail modification (not done). An LP over degree-d shallow densities on the *finite
grid* `1≤j≤Jmax` (`scripts/omega17_shallow.py`; positivity beyond Jmax not certified — the
reviewer found `ψ(105)<0` for an `R=16,k=4,ψ≤4` solution with Jmax=104) finds least degree
`d=k+1` (k even) / `k+2` (k odd) when `R≥2k`; the `ψ≤4` column is finite-grid only.

**Construction 3.2 (proposed support-aware fake in the exchangeable model; NOT proved —
Assessment).** Suppose the big events are *independent of the small coordinates* (no x_s
dependence), with `N` exactly Poisson-binomial of mean R and `R≥R_min(n)`, and the multivariate
form `ψ:=1−e_n(z−p)/e_n(−p)` (which is (Prop 3.1) in the Poisson limit) is ≥0. Then
the candidate is `m(n):=λψ(z(n))1_{S_T}(n)`, supported on `S_T∖A`; for T-smooth moduli `q` with
`qT^n≤x^{1−ε}` and fewer than n big prime factors one expects class counts
`N_xP_H(C)(1+O(2^n e^{−u\log u}))`, `u=ε\log x/𝓛` (fundamental lemma term by term; the
*Haar-weighted* ℓ¹ norm of the monomial coefficients of `e_n(z−p)/e_n(p)` is `2^n`; the
unweighted norm is not bounded). **Gaps (R68 review):** (1) the box: `λ=N_x/Σ_Sψ` and
`λ max_Sψ≤1` are not proved (ψ is unbounded; needs a tail modification); (2) local densities:
T-rough integers have local factor `1/q` at primes `q>T` of a modulus, Haar on units `1/(q−1)`, so
moduli with primes `>T` must be excluded or corrected; (3) the Brun–Titchmarsh-type upper
constraints on larger moduli are not verified. Only the outline below is offered.
*Outline.* ψ is a polynomial in the event indicators with
`E[ψχ]=E[χ]` for all juntas of `<n` big coordinates (each monomial of `e_n(z−p)` has n distinct
centred factors); expand, count integers of `S_T` in each class `C∩{events of Y hold}` (modulus
`≤qT^n`) by the fundamental lemma; positivity and `ψ(0)=0` give support in `S_T∖A`. ∎
(The positivity of the multivariate ψ is only checked in the Poisson limit.)

*Assessment.* In an exchangeable model, support awareness should not help against
fundamental-lemma-accuracy information, with the obstruction again at level `n≍R`, once gaps
(1)–(3) are closed. §4 explains why even this outline does not transfer to the ES instance.

## 4. Why the ES instance resists integer fakes: the small coordinates

In the ES system the big bits are independent only *conditionally on the small coordinates*
`x_s`, with probabilities `p_ℓ(x_s)=Σ_{e at ℓ}a_e(x_s)/(ℓ−1)`, `a_e:=1[n≡−4D_e (v_e)]` (O14
Lemma 2.1; distinct residues assumed for simplicity), and conditional odds-mass
`R(x_s)≥μ*≍𝓛³/log𝓛` (O14 Thm 4.5). The deep planted law is exact because it conditions on all
of `x_s` (modulus `lcm(v≤T^{0.4})=e^{T^{0.4}(1+o(1))}`). A shallow fake must handle `x_s` with low
degree, and the certificate sees `x_s` through small classes with *very* high accuracy.

**Lemma 4.1 (no x_s-uniform exchangeable fake; PROVED).** Let `I⊂(0,∞)` be an interval and f a
polynomial with `f(0)=0`. Then `E_{N~Poisson(R)}f(N)=1` cannot hold for all `R∈I`.
*Proof.* `g(R):=Σ_jf(j)R^j/j!−e^R` is entire and vanishes on I, hence identically; comparing
coefficients, `f(j)=1` for all j, contradicting `f(0)=0`. ∎
*Scope (R68 review).* The lemma needs R to range over an interval. Actual conditional laws are
Poisson-binomial with finitely many means, and a fixed polynomial can have mean 1 at finitely
many R (e.g. `f(j)=j(j−5)²/12` at R=2 and R=3). So Lemma 4.1 is an obstacle for the
*exchangeable-Poisson heuristic* of a fixed-f fake whose conditional means spread over a range.
It is not a theorem that every shallow fake tilts the small-coordinate law.

**The same for x_s-centred shallow fakes.** `y_ℓ:=z_ℓ−p_ℓ(x_s)` is shallow (level `≤T`), so
`ψ':=e_n(p(x_s))+e_n(y)` (n odd) is shallow, `≥0` iff the multivariate Charlier ψ of Construction 3.2
is, vanishes on avoiders, and is exact on all juntas of `<n` big coordinates *given* `x_s`; but
its small-coordinate marginal is tilted by `w(x_s)=e_n(p(x_s))/Ee_n(p)≈(R(x_s)/ER)^n`.
Removing the tilt *in this construction* needs `1/e_n(p(x_s))`. We expect a polynomial
approximation of it to relative accuracy ε to need degree growing with `n` and `log(1/ε)`, which
would cost large level. This is heuristic: the degree depends on the range of R, and no lower
bound is proved.

**Assessment 4.2 (the precision requirement; heuristic).** A small class `C_s` at a prime
`q∈(y,T^{0.6}]` should shift `R(x_s)` by at most `≈w_q≤𝓛³/(2q)` (HAAR Lemma 2.3 is an upper bound
on the load, not a lower bound on individual shifts). A tilted fake would then be off on `C_s` by
a relative amount of order up to `n w_q/R≈𝓛³/(q log𝓛)`, which is polynomially and not
exponentially small in 𝓛. A certificate that is to beat the avoider density `δ*=e^{−Θ(𝓛³)}`
(CEILINGS_UNIFIED Prop 1.1) must use very high relative accuracy somewhere. Whether known
unconditional prime theorems give that accuracy on such small classes is **not** settled here.
Gallagher's estimate (as used in O9) has additional `(log x/log Q_G)²/Q_G` and
exceptional-character terms, so "`e^{−c log x/log q}`" is a model profile, not a theorem. The
conclusion "tilt detectable; untilting costs level `>x`" is therefore an Assessment about this
construction route only.
The obvious repair — use only events whose small dependence is shallow (`v∈V`, `lcm(V)≤x^ε`) —
leaves odds-mass `≪𝓛²` (the `𝓛/log y` factor of O14 Lemma 2.2 comes from all `v≤T^{0.4}`),
whose planting obstructs only `log x≲𝓛³`, the range where no avoider prime is expected anyway.

*Reading.* The Haar ceiling is a sieve-dimension statement about *one* conditional system; its
integer realisation needs the conditioning on `x_s` to be shallow, and in the ES instance it is
not. This is the precise reason why the support-aware question is not settled by "discretising
the planted law", and it does not by itself suggest a certificate either.

## 5. Atomicity (the box) and toy LPs (brief item (c))

**Lemma 5.1 (aggregation; PROVED).** Let 𝒢 be a finite partition of S such that F and every
`C∩S`, `C∈𝒞`, are unions of cells. Then 𝔐 is nonempty with `min Σ mF=μ` iff the LP in the
variables `M_G∈[0,|G|]` (`G∈𝒢`), `Σ_GM_G=N_x`, `l_C≤Σ_{G⊆C}M_G≤u_C`, has minimum `Σ_{G:F=1}M_G=μ`.
*Proof.* Aggregate (`M_G:=m(G)`) / spread uniformly (`m:=M_G/|G|` on G). ∎
So support and atomicity enter only through the **capacities** `|G|=|S∩G|` of the atoms of the
information; the diffuse problem (O15 Def 2.1) is the same LP with Haar-type capacities
`∞`. In particular the box can only bind on atoms with `|S∩G|<` (fake mass on G).

**Lemma 5.2 (capped planting; PROVED).** In O14 Lemma 1.1's setting (independent bits, odds
`r_b≤r*`, `R=Σr_b`), let `1<s≤2` and `R≥kr*+(k+1)/(s−1)`. Then the planted law ν has `ν(0)=0`,
the same ≤k-marginals as P, and `|dν/dP−1|≤s−1` on every nonzero configuration; in
particular `ν≤sP`.
*Proof.* ν−P is supported on the configurations `1_y`, `|y|≤k+1`, where (O14 Lemma 1.1's formula)
`(ν−P)(1_y)/P(1_y)=(−1)^{|y|+1}e_{k+1−|y|}(r_{∖y})/e_{k+1}(r)`, `r_{∖y}` = the odds off y. With
`e_{k+1−j}(r_{∖y})≤e_{k+1−j}(r)` and the chain `ne_n(r)≥e_{n−1}(r)(R−(n−1)r*)` (O14 proof of
Lemma 1.1, valid for `n≤k+1` since `R−kr*≥k+1`),
`e_{k+1−j}(r)/e_{k+1}(r)≤∏_{i<j}(k+1−i)/(R−(k−i)r*)≤((k+1)/(R−kr*))^j≤(s−1)^j≤s−1` for `j≥1`. ∎
(For `s=2` this is O14's `dν/dP≤2` with a slightly different hypothesis.) So a flat fake costs
only a constant factor in R: if the information atoms are configurations whose integer
capacities exceed `s·N_xP(G)`, the box is irrelevant whenever `R≥kr*+(k+1)/(s−1)` (off the zero
configuration; at 0 the density is 0). The support `S_T` has slack `|S_T|/N_x≍log x/𝓛≫2`.
Supports rough up to `z=x^θ` with `T<z<√x` have slack about `uω(u)` (`u=1/θ`, Buchstab ω;
e.g. `1+log 2` at θ=1/3), which exceeds 1; *if* the capacities of the atoms the fake uses are
Haar-like (the unproved point of §§2–4), they too only move constants. (Such supports must keep
the counted primes in `(T,z]` separately.) Only `z≥√x` (S = the primes ∪ {1}, slack ≈1) pins
the measure, and that is a search.

**Toy LP (EVIDENCE; `scripts/omega17_toylp.py`, `data/omega17/toylp.txt`).** 14 sieve primes
`17..71`, `⌊0.12ℓ⌉` resp. `⌊0.17ℓ⌉` random excluded classes (odds-mass R=1.94 resp. 2.92), true
measure = primes `71<p≤x`; information = the *exact* prime counts on all bit-cells of ≤k primes
(k-juntas), floating-point LP (HiGHS, default tolerances; values are not exact) via Lemma 5.1 with atoms = the 2^14 configurations. Minimal fake mass
on the avoider configuration (certificate exists iff >0), `x=10⁶`, seed 1 (seeds 2,3 and
`x=3·10⁵` agree):

| R | k | diffuse | S slack 8.5 / 4.2 / 2.8 / 2.3 | slack 1.94 | 1.77 | 1.63 (71-rough) | true avoiders |
|---|---|---|---|---|---|---|---|
| 1.94 | 2 | 0 | 0 | 1581 | 3568 | 5183 | 12668 |
| 1.94 | 3 | 7101 | 7101 | 7105 | 7231 | 8110 | 12668 |
| 2.92 | 3 | 0 | 0 | 0 | 465 | 1170 | 5519 |
| 4.07 | ≤3 | 0 | 0 | 0 | 0 | 0 | 2219 |

(slack := |S|/N_x; S = integers ≤x coprime to the sieve primes and to the first j small
primes.) Support awareness changes nothing until the slack drops below ≈2, then gains one
junta level, consistent with the box binding on the planted density (Lemma 5.2's regime;
global slack alone does not imply the threshold ≈2). EVIDENCE only; toy scale (`R≤4`, `k≤3`).
The `R=4.07` row is the seed-1, frac 0.22 run, appended to the data file.

## 6. Answer to the brief, and the precise residual

**(a) Formalisation.** Def 1.1 (SALC) adds to O15 Def 2.1 exactly the three forbidden items:
support S, atomicity (box `m≤1`; integral version `m∈{0,1}`), and class bounds of any form. Moduli
`>x` contribute only the box or primality tests of specific integers (Lemma 1.2); validity is
dual to support-aware minorants `B≤F+θ` on S (Lemma 1.3); with Haar-type bounds the primes drop
out and validity is a statement about integers only — the integer fake problem IF (Rem 1.4); and
support/atomicity act only through the capacities `|S∩G|` of the information atoms (Lemma 5.1).

**Does the planted fake survive?** Not literally. Its density is deep: it rewards "almost all
events off". No fake can be monotone in the events (Lemma 2.1), although this does not exclude
shallow non-monotone fakes. Restricting the planted law to integers would need counts of
integers in sifted sets of dimension `≍𝓛³/log𝓛` below the sieving limit. There are two partial
results. First, in exchangeable models a *shallow* Charlier density exists: Prop 3.1, with
positivity as EVIDENCE on an integer grid. The integer fake built from it (Construction 3.2) is
only an outline with three open gaps. Second, the planted law is *flat*
(`|dν/dP−1|≤s−1` off 0) once `R≥kr*+(k+1)/(s−1)` (Lemma 5.2, PROVED). So atomicity costs only
constants whenever the support has slack `>1` and Haar-like atom capacities. In the ES
instance the shallow outline runs into the small coordinates. The natural shallow
constructions tilt the small-coordinate law (Lemma 4.1 in the Poisson heuristic; §4), and we
have no cheap way to untilt them (Assessment 4.2, heuristic, specific to these constructions).

**Outcome.** Neither a support-aware certificate beyond 1/4 nor a support-aware planting lemma
for ES was obtained. The residual is now the following integer statement (no primes in it):

> **Conjecture SAP (support-aware planting; CONJECTURE).** Call a modulus *admissible* if all its
> prime factors divide `LQ` (so every n∈S_T is a unit mod it). Information profile `𝒥(δ)`:
> (i) `Σm=N_x`; (ii) for every admissible `2≤q≤x^δ` and every reduced class `C⊂H` mod `lcm(q,Q)`:
> `|m(C)−N_xP_H(C)|≤η_qN_xP_H(C)`, `η_q:=e^{−δ log x/log q}`; (iii) for every admissible
> `q≤x^{1−δ}` and reduced `C⊂H`: `m(C)≤2N_xP_H(C)·log x/log(x/q)`. There are `c,C,δ>0` such that
> for every fibre with `Q≤x^δ`, `T≥T_0` and `C𝓛³≤log x≤c𝓛⁴/log𝓛`, some `m:S_T∖A→[0,1]` satisfies
> `𝒥(δ)`.

*Consequence (exact scope).* SAP implies that every LP-relaxed SALC (Def 1.1 with the box) on
support `S_T` whose bounds are implied by `𝒥(δ)` is invalid in that range. It says nothing
about integral SALCs (`m∈{0,1}`), smaller supports, or information outside `𝒥(δ)`. Whether `𝒥(δ)`
contains everything the known unconditional prime theorems give is an Assessment, not a theorem.
Gallagher's estimate has additional `(log x/log Q_G)²/Q_G` and exceptional-character terms, so
`η_q` is a model profile. Support for SAP comes from the random-integer heuristic (atom
capacities Haar-like) together with Lemma 5.2, and from the toy LPs (§5).
Refuting it would require a set of non-avoider integers `≤x` that is *not* rich enough to carry a
Haar-like measure — i.e. an integer sieve beyond the high-dimensional sieving limit, the integer
analogue of the open problem. GRH-quality information (√x accuracy) lies outside SAP's scope.
We have not established √x-quality equidistribution of T-rough integers, uniformly in growing T,
even under GRH. The direct contour argument fails because the finite Euler product `∏_{p≤T}` is
huge on `Re s=1/2`, but that is only a limitation of this argument. So with GRH input even the
exchangeable outline 3.2 is not shown consistent.

**(b) INTERFREQ/SPW analogy.** Not pursued beyond the observation that Lemma 5.1 is the
pointwise analogue of the interval-count accounting there: support enters only through atom
capacities, and atoms of moduli `>x` are points.

**(c) Toy LPs.** §5: support awareness changes nothing until the slack `|S|/N_x` drops below
≈2, then gains one junta level (EVIDENCE).

## 7. Status

| item | statement | label |
|---|---|---|
| Def 1.1 | support-aware linear certificate (support, box/integrality, arbitrary true bounds) | definition |
| Lemma 1.2 | classes with `≤1` integer of S: box constraint or a test whether that integer is a counted prime | PROVED |
| Lemma 1.3 / Rem 1.4 | LP duality; with Haar-type bounds validity is an integer statement (IF) | PROVED |
| Lemma 2.1 | no nondecreasing (event-only) fake matching first-order marginals | PROVED (Harris) |
| Prop 3.1 | Charlier density `1−C_n(N;R)`: ψ(0)=0, moments `<n` exact, degree n | (i)–(iii) PROVED; positivity on the integer grid, `j≤4R+6n+20`, n≤81: EVIDENCE (exact rationals); not globally bounded |
| Construction 3.2 | exchangeable-model integer fake (outline, gaps (1)–(3)) | Assessment |
| Lemma 4.1 | Poisson: no fixed polynomial f, f(0)=0, has mean 1 on an interval of R | PROVED (its application to ES is heuristic) |
| Assessment 4.2 | tilt of the natural shallow constructions; untilting expensive | Assessment (heuristic, construction-specific) |
| Lemma 5.1 | support/atomicity enter only via atom capacities | PROVED |
| Lemma 5.2 | planted law flat: `|dν/dP−1|≤s−1` if `R≥kr*+(k+1)/(s−1)` | PROVED |
| toy LP | gain only for slack `<≈2`, one junta level | EVIDENCE |
| Conj SAP | box-bounded Haar-like measure on `S_T∖A` below `𝓛⁴/log𝓛` | CONJECTURE |

Not claimed: anything about ES; any certificate beyond exponent 1/4; any obstruction for
SALCs with GRH-quality information, non-linear certificates, or prime-supported (slack-1)
arguments (= searches).

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; OMP_NUM_THREADS=2 timeout 900 uv run --with scipy python scripts/omega17_shallow.py)   # §3 LP table (~2 min)
uv run python scripts/omega17_charlier.py > data/omega17/charlier.txt   # §3 R_min table, exact rationals (~15 min)
(ulimit -v 8000000; OMP_NUM_THREADS=2; for a in "1 1000000 0.12" "1 1000000 0.17" "2 1000000 0.12" "2 1000000 0.17" "3 300000 0.12" "1 1000000 0.22"; do timeout 1500 uv run --with scipy python scripts/omega17_toylp.py $a; done) > data/omega17/toylp.txt   # §5 (~15 min)
```
