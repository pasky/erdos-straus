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

