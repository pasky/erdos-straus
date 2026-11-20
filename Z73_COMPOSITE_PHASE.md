# Which local conditions at a composite shift must be checked together?

Result: the two-factor phase criterion holds in every finite abelian group (so at every composite shift). Local tests at the components of a composite shift cannot replace the joint test. Minimal obstructions of unbounded size exist; prime versions are conditional on Dickson.   Label: PROVED (group criterion, 715 example, unbounded construction); CONDITIONAL on Dickson's conjecture (infinitely many prime instances for each s)
Scope: certificates through a fixed x=K. Not a shift-selection theorem, and not an ES counterexample.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P2, P19, P20 CORRECT)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**ES is open.** Two findings: (i) the two-factor sufficient test in `Z72_PAIR_PHASE.md` works at arbitrary odd composite shifts, with a different endpoint; (ii) checking it separately at prime-power components cannot replace the joint test, even at actual primes and even if any proper subset of the components succeeds. The statements about unbounded obstruction size below distinguish the unconditional group construction from the conditional prime construction.

## One joint character test (PROVED)

Let `G` be a finite abelian group, `t` an element of order 2, and `q,r∈G`. Let `V=v+1,W=w+1` for positive exponent budgets `v,w`. Write `χ(g)=exp(2πi θχ(g))` and define

```
T = min_{χ(t)=−1} V ||θχ(q)|| + W ||θχ(r)|| .
```

If `T>1`, the box `{q^i r^j : |i|≤v, |j|≤w}` contains `t`. At `T=1` it misses **exactly** when `q^V=r^W=t` and the images of `q,r` in `G/<t>` generate the direct product of cyclic groups of orders `V,W`, respectively. If `t` is not a square in `G`, a miss at equality requires `V,W` odd: an even one would express `t` as a square. Thus the z72 parity shortcut **does** extend to every ES shift `c≡3 mod 4`: some prime `3 mod 4` divides `c`, modulo which −1 is not a square. It does not extend to arbitrary involutions.

*Proof.* Put `H=<q,r>`. Characters of any subgroup of a finite abelian group extend to the group: add a generator `x`, let `m` be its order modulo the subgroup, and choose an `m`th root of the specified value at `x^m`. If `t∉H`, a character of `G/H` detecting the order-two class of `t` gives `T=0`. Otherwise put `Λ=ker(ℤ²→H/<t>)`, and label its vectors by whether they map to `t` (odd) or 1 (even). On `L=diag(V,W)⁻¹Λ` the minimum ℓ¹ length of a dual functional inducing this label modulo 2 is `2T`. Indeed, dividing such a functional by two and undoing the scaling gives angles modulo ℤ² trivial on `ker(ℤ²→H)`, half-integral on the odd coset, hence precisely a character of `H` sending `t` to −1; all such characters extend to `G`. The least ℓ∞ length `λ` of an odd vector satisfies `λ(2T)≤2` by the Gauss-basis inequality in z72 (its proof uses only the lattice and the nontrivial label, not cyclicity). A miss means `λ≥1`. Equality at `T=1` forces the scaled lattice to be an axis-aligned unit square lattice with both coordinate vectors odd. Undoing scaling gives exactly the stated orders/direct product in `G/<t>` and the two endpoint values; the converse is immediate from that rectangular lattice. ∎

Use `G=(ℤ/c)×`, `t=−1`, and any two distinct prime factors of `K=(n+c)/4` not dividing `c`. A hit gives the original denominators by z72. For the prime `1201` at the **necessary composite shift** `c=39`, `q=5,r=31`, `v=w=1`, the *joint* score is `T=1`. Here `5²≠−1 mod 39`, so the endpoint really fires. This supplies a phase proof specifically where the prime-shift version could not. It does not select a shift for general `n`.

## A pairwise-successful window without any ES triple through its first denominator (PROVED)

At the Mordell-class prime `p=3117161329` use `c=715=5·11·13`, `K=(p+c)/4=2729·285559`. All three factors named as primes (`p` and the two factors of `K`) pass trial division. At the three components, the two generators of the ratio set have signs

| modulus | 2729 | 285559 | constraint for target −1 |
|---:|---:|---:|---|
|5|−|−|`i+j=1 mod 2`|
|11|+|−|`j=1 mod 2`|
|13|−|+|`i=1 mod 2`|

Every pair of constraints is feasible with exponents in `{0,1}`. All three are inconsistent, even without any bound. These are projections of the *same* `K`: replacing `c` by a proper divisor and recomputing `K` is not what the argument does. There is even a quadratic nonresidue `(p/c)=−1` (only the factor 11 contributes a minus sign). A joint character sees the obstruction: take a character odd on −1 in each of the three factors, then multiply. It is trivial on both generators, −1 on the target, so `T=0`.

Could Type I rescue `x=K`? No. With `H=pK`, a direct completion requires `d|H²` with `d/H≡−1 mod c` (all factors are units mod `c`). The possible ratios are `p^k q^i r^j` with `i,j,k∈{−1,0,1}`. Modulo 5, `p≡4=−1`, but modulo 11 we have `p≡−4`, neither sign. Thus `k=±1` cannot attain −1 there; `k=0` has just been ruled out globally. All 27 divisors are tested in the replay. This is a counterexample to local assembly, not to ES.

## How many components can be necessary? (PROVED, with a conditional prime variant)

For **any even** `s≥2`, use `s+1` distinct odd prime moduli `ℓ₀,…,ℓ_s`, product `c`. Choose `s` distinct odd primes `q_i` such that `q_i` is −1 at `ℓ₀` and `ℓ_i`, +1 at the others (CRT and Dirichlet). With `K=∏q_i`, the target −1 imposes

```
z_i=1 mod 2    (each i=1,…,s),      Σ z_i=1 mod 2   (component 0).
```

Every proper subset has a joint solution in `{0,1}^s`, while the entire system does not. Even unbounded exponents do not help. This is an unbounded minimal obstruction, not an extrapolation of the numerical example. It does not contradict the two-*generator* theorem: the number of generators grows with `s`.

One may choose all `ℓ_j≡1 mod 105`, `ℓ₁≡3 mod 8`, all other `ℓ_j≡1 mod 8`, with `ℓ₀>17`. Fix `q_i≡1 mod 105` for `i<s`; for `q_s` impose `4q_s≡1+c mod 105` alongside the prescribed signs and oddness. The residue is a unit. As `q_s` runs through primes in this class, `n=4K−c>0` is automatically `1 mod 840` and has `(n/c)=−1`. Direct completion at `K` is **unconditionally** excluded if `n` is prime: the extra generator `n≡4 mod ℓ₀` is neither sign; since `n` can enter the ratio only with exponents −1,0,1, the direct test reduces to the inconsistent signs. **Conditionally on Dickson's conjecture**, infinitely many such `n` are prime for each `s`: fix all but `q_s`, then demand both `q_s` and `4(∏_{i<s}q_i)q_s−c` prime. These are two distinct nonconstant linear forms on a progression of difference `D=2·105c`. Both are units at primes dividing `D`. A prime dividing `∏_{i<s}q_i` does not divide `c`, so at most one residue is forbidden there; at all other primes outside `D`, at most two classes are forbidden and the prime is odd. This is admissibility, **not** an unconditional production of large standard counterexamples to ES. *(z74 Opus xreview fix: any single prime instance is a finite search. For s=2 one is ℓ=(2521,211,3361), q=(2816655498511,66076508762723), with n=744459046915736043727401721, proved prime by Pocklington, ≡ 1 (840) and (n/c)=−1. No triple contains x=K there (`scripts/z74_xrev_z72phase_checks.py composite`). Such an instance obstructs only this x, not ES at n.)*

Falsifiers: odd squares cannot satisfy the Jacobi −1 premise. No claim about the numerator-8 sub-line or (★) is used. The group lemma and sign construction need no primality of the input; excluding *all* triples at `x=K` in the construction uses primality of `n` to control divisors of `n²`. No global positivity or failure is inferred on F3/F4. Replay: `uv run python scripts/z73_crt_phase.py` (composite-group box regression and direct original-denominator test).
