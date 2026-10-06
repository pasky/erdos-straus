# Support-aware certificates: the (N2) residual of the 1/4 ceiling (task O68)

Status: IN PROGRESS (checkpoint 0). Labels as in DISCOVERIES.md. Notation as in
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
(which, being true, certifies that n is prime) or `u_C<1` (certifies that n is not prime).
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
*not* hold" — and there is no fundamental-lemma control of the integers in such sets beyond the
sieving limit unless the dependence is polynomial of low degree (§3).

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

(`n≥31` by bisection in R, assuming monotonicity). `R_min/n` grows slowly (2.9 at n=81,
consistent with `≍log n`). The deep planting needs `R≳n` (O14 Lemma 1.1; LP-sharp up to a
constant); the shallow one needs `R≳n·(slowly growing)`. On `j≤2R`, `max ψ_n→1` (1.09 at n=7,
1.000 at n=21), so the box is harmless. An LP over all degree-d shallow densities (Poisson
model, `scripts/omega17_shallow.py`) finds the least degree `d=k+1` (k even) / `k+2` (k odd) when
`R≥2k`, and `d≈1.6k–2k` under `ψ≤4` for `R∈{16,32}`.

**Corollary 3.2 (support-aware fake in the exchangeable model; PROVED given (iv) for the
parameters used).** Suppose the big events are *independent of the small coordinates* (no x_s
dependence), with `N` exactly Poisson-binomial of mean R and `R≥R_min(n)`, and the multivariate
form `ψ:=1−e_n(z−p)/e_n(−p)` (which is (Prop 3.1) in the Poisson limit) is ≥0. Then
`m(n):=λψ(z(n))1_{S_T}(n)` is a box-bounded measure on `S_T∖A`, and its counts on every class of
modulus `q` with `qT^n≤x^{1−ε}` are `N_xP_H(C)(1+O(2^n e^{−u\log u}))`, `u=ε\log x/𝓛` (fundamental
lemma applied term by term; `‖coeffs‖_1≤2^n` after normalisation). It therefore defeats every
SALC whose bounds on such classes have relative accuracy no better than
`2^{n+1}e^{−u\log u}` and whose other bounds are upper bounds of Brun–Titchmarsh type.
*Proof sketch.* ψ is a polynomial in the event indicators with
`E[ψχ]=E[χ]` for all juntas of `<n` big coordinates (each monomial of `e_n(z−p)` has n distinct
centred factors); expand, count integers of `S_T` in each class `C∩{events of Y hold}` (modulus
`≤qT^n`) by the fundamental lemma; positivity and `ψ(0)=0` give support in `S_T∖A`. ∎
(The positivity of the multivariate ψ is only checked in the Poisson limit; Cor 3.2 is stated
conditionally on it.)

So in an exchangeable model, support awareness does **not** help against
fundamental-lemma-accuracy information: the obstruction is again at level `n≍R`. §4 explains
why this does not transfer to the ES instance.

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
So any fake of the form `f(N)` (fixed f) tilts the small-coordinate law by
`w(x_s):=E[f(N)|x_s]≠1` wherever `R(x_s)` varies, and `R(x_s)` does vary (its fluctuations are
`≍𝓛` around `μ≍𝓛³`, O14 Lemma 2.3).

**The same for x_s-centred shallow fakes.** `y_ℓ:=z_ℓ−p_ℓ(x_s)` is shallow (level `≤T`), so
`ψ':=e_n(p(x_s))+e_n(y)` (n odd) is shallow, `≥0` iff the multivariate Charlier ψ of Cor 3.2
is, vanishes on avoiders, and is exact on all juntas of `<n` big coordinates *given* `x_s`; but
its small-coordinate marginal is tilted by `w(x_s)=e_n(p(x_s))/Ee_n(p)≈(R(x_s)/ER)^n`.
Removing the tilt needs `1/e_n(p(x_s))`; a polynomial approximation of `1/R^n` on the range of
R to relative accuracy ε needs degree `≫n+log(1/ε)` in R, i.e. level `T^{0.4(n+log(1/ε))}`.

**Assessment 4.2 (the precision requirement).** A small class `C_s` at a prime `q∈(y,T^{0.6}]`
shifts `R(x_s)` by `≍w_q≤𝓛³/(2q)` (HAAR Lemma 2.3), so a tilted fake is off on `C_s` by a
relative `≍n w_q/R≍𝓛³/(q log𝓛)` — polynomially small in 𝓛. Unconditional prime information on
such a class has relative accuracy `e^{−c\log x/\log q}=e^{−c𝓛³}` (Gallagher/Vinogradov–Korobov
type, at `log x≍𝓛⁴`), and a certificate that is to beat the avoider density
`δ*=e^{−Θ(𝓛³)}` (CEILINGS_UNIFIED Prop 1.1) must use accuracy of this order somewhere. So the
tilt is detectable in principle, and the untilting costs level `T^{0.4·Θ(𝓛³)}=e^{Θ(𝓛⁴)}>x`.
The obvious repair — use only events whose small dependence is shallow (`v∈V`, `lcm(V)≤x^ε`) —
leaves odds-mass `≪𝓛²` (the `𝓛/log y` factor of O14 Lemma 2.2 comes from all `v≤T^{0.4}`),
whose planting obstructs only `log x≲𝓛³`, the range where no avoider prime is expected anyway.

*Reading.* The Haar ceiling is a sieve-dimension statement about *one* conditional system; its
integer realisation needs the conditioning on `x_s` to be shallow, and in the ES instance it is
not. This is the precise reason why the support-aware question is not settled by "discretising
the planted law", and it does not by itself suggest a certificate either.
