# EXCEPTIONAL_MN4 — the m/p density transition under Selberg's eigenvalue conjecture (task O117)

Status labels as in DISCOVERIES.md. References: MN2 = `EXCEPTIONAL_MN2.md`, MN3 = `EXCEPTIONAL_MN3.md`,
TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` ((D)32; Thm 8.1 = ET's (OPEN-I) under (SEL)), ET = Elsholtz–Tao
arXiv:1107.1010v6. `L = log N`. `g(x) := x/φ(x)`.

## 0. Summary

Results (§§4–5), CONDITIONAL on (SEL_m) (§2.2: no exceptional eigenvalues for `Γ₀(mdq²)` with even nebentypus
mod q; implied by Selberg's conjecture for all `Γ₁(M)`; TTL's hypothesis family, now with levels divisible by m):
* Thm I_m: `Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L² + L log² m)/m + N m^{−0.35}/L` uniformly for `4 ≤ m ≤ L^5`;
* Thm L'': `ρ_rep(m,N) ≪ (L³ + L² log² m)/m + m^{−0.35}` uniformly in m (for `m > L^5` this already follows
  unconditionally from MN3 Thm L', see Lemma 0.1);
* Thm S (= Thm 5.2, sharp order): with MN2 Thm U, the transition for m/p is at `log N ≍ m^{1/3}`.

Unconditional status (§6): nothing changes for the lower side (MN3 Thm L' stays best; the Kim–Sarnak strip of
TTL §9 transfers unchanged); new unconditional ingredients are the m-uniform gain lemmas of §3 and the
parity-free level-md normalisation of §2. Self-review issues (from the drafts of §§2–3) are listed at the
ends of §2 and §3; in particular §3.2(c) is false in all ranges and is used only for `D, F ≥ L^{100}`.

**Why m ≤ L^5 suffices (Lemma 0.1, PROVED, elementary from MN3 Thm L').** If `m > L^5` then
`(L³ + L² log² m) log L/m ≪ m^{−0.35}`, so MN3 Thm L' already reads `ρ_rep ≪ m^{−0.35}`.
*Proof.* `L ≤ m^{1/5}`, so `L³ log L/m ≤ m^{3/5}·log m/m = m^{−2/5} log m ≪ m^{−0.35}` and
`L² log² m log L/m ≤ m^{−3/5} log³ m ≪ m^{−0.35}`. (MN3 Thm L' needs `log m ≤ L/10`, `L ≤ m^{1/2}`; for
`log m > L/10` MN2 Lemma 3.5 is used unchanged, see §9.) ∎

Consequence: in the conditional argument every factor `m^{O(1)}` in a *remainder* term is `L^{O(1)}`, and
TTL's proof already tolerates `L^C` losses in remainders (layers `k ≤ C₁ log L` go to Brun–Titchmarsh).
The real work is (i) the m-scaled main terms must carry exactly `1/m`, with no `m/φ(m)` loss (the sieve
cannot sieve by `ℓ | m`, which inflates the sieve product by `m/φ(m)`; it must be paid by the coprimality
gain `φ(m)/m` of the masses, MN3 Prop 2.3), and (ii) the spectral input must be checked for the new
level/discriminant `(md, −4md)`.

## 1. Set-up for general m (PROVED; ET Prop 2.2 with 4 → m)

Let `m ≥ 4`, n ≥ 2. A Type I m-solution of n is `m/n = 1/x + 1/y + 1/z` with `n | x`, `(n, yz) = 1`;
`f_{I,m}(n)` is their number. ET Prop 2.2 and its proof (ET p. 12) go through verbatim with 4 replaced
by m: writing `x = ndx'`, `y = dy'`, `z = dz'` with `x', y', z'` coprime, `m d x'y'z' = y'z' + n x'y' + n x'z'`,
hence `x' = ab`, `y' = ac`, `z' = bc`, `c | a+b`, and with `e := (a+b)/c`, `f := macd − n = (na+c)/b`:

  `mabd = ne+1`, `ce = a+b`, `macd = n+f`, `ef = ma²d+1`, `bf = na+c`   (1.1)

(direct check: `mabd = mad(ce−a) = (n+f)e − (ef−1) = ne+1`; `bf = c·ef − af = c(ma²d+1) − af = na + c`).
The map (x,y,z) ↦ (a,b,c,d,e,f) is injective (ET Prop 2.2, uniqueness, normalised by gcd(a,b,c) = 1), and
(a,c,d) determine the rest given n. The swap y ↔ z is a ↔ b. If `a ≤ b` then `c ≤ ce = a+b ≤ 2b`, so
`f = (na+c)/b ≤ n + 2 ≤ 2n`. Hence, with

  `w_{c,m}(n) := #{(a,d,f) ∈ ℕ³ : f | ma²d+1, n = macd − f, 0 < f ≤ 2n}`,

**Lemma 1.1.** `f_{I,m}(n) ≤ 2 Σ_{c≥1} w_{c,m}(n)` (n ≥ 2), and `n` has a Type I m-solution only if some
`w_{c,m}(n) ≥ 1`. ∎

Conversely every w_{c,m}-tuple gives, with `e := (ma²d+1)/f`, `b := ce − a`, the identities (1.1)
(the check above runs backwards), so `b = (na+c)/f ≥ a/2`; this is TTL §8.0 with 4 → m.
**Coprimality facts** (used throughout): `(f, m) = (e, m) = 1` (as `ef ≡ 1 mod m`), hence
`(n, m) = 1` (`n ≡ −f mod m`); for `ℓ | d`, `ℓ ∤ n` (`n ≡ −f`, `f | ma²d+1 ≡ 1 mod ℓ`). So **no sieving prime
may divide md**, and the m-loss of the sieve product must be paid by the masses (§3).

**Exponents.** For n ≍ N write `a = N^α`, `b = N^β`, `c = N^γ`. Then `acd ≍ N/m`, `e ≍ N^{β−γ}`
(`e = (a+b)/c`, m-free), `f ≍ N^{1+α−β}` (`bf = na + c`, m-free), `d ≍ N^{1−α−γ}/m`. Since
`m ≤ L^5` in the conditional part (Lemma 0.1), m shifts only the exponent of d, by `≤ 5 log L/L`.

## 1A. Design of the transfer (working notes; superseded by §§2–4 once written)

* **Normalisation (no parity).** For general m use `Q = [f, 2mad, mde]`, disc `4m²a²d² − 4fmde = −4md`,
  level `md`, root `z_Q = (−mad + i√(md))/f`, `w = z/(md) = (−a + i/√(md))/f`, sieve functional
  `n = c·B/2 − A`. The full set `{[A,B,C] : B² − 4AC = −4md, A > 0, B ≡ 0 (2md), C ≡ 0 (md)}` equals the
  set of these forms (a ∈ ℤ free), and it is `Γ⁰(md)`-stable (z-side: `md | t` gives `B' ≡ 0 (2md)`,
  `C' = Q(t,s) ≡ 0 (md)`), so TTL's parity bookkeeping (`Γ(2q)`, `M = 4dq²`) is replaced by
  `Γ(q)`, `M = mdq²`. For m = 4 this is TTL's set under `Y ↦ 2Y` (level 4d instead of d; harmless).
* **Separation** (TTL Lemma 2.2): `4md | disc(Q − Q')` for two such forms, and by TTL Lemma 2.1
  `disc(Q−Q') = 8md(cosh − 1)`, so `cosh ≥ 3/2` again — uniformly in m.
* **m enters remainders only polynomially** (`(md/A)^{1/2}` spectral, `m^{1/2}A/D` Weil); as `m ≤ L^5`
  these are `L^{O(1)}` and are absorbed by TTL's `L^C` (layers `k ≤ C₁ log L` → Brun–Titchmarsh).
  The crossing is `D = A` with `δ := |log(A/D)|/L` (TTL's `|2α−1+γ|` up to `O(log L/L)`).
* **Main terms need the gain.** Sieve products lose `g(2mcs) ≤ 2g(m)g(c)g(s)`; masses must carry
  `φ(m)/m`. Sources of the gain: divisors `f, e` of `ma²d+1` are coprime to m (MN3 Prop 2.3 with
  `k = m·…`; for `Σρ_{md}(f)/f`: `ρ_{md}(f) = 0` unless `(f,m) = 1`); in Prop 7.1 the main term
  `X_a ≍ Dφ(ma²)/(ma²)` carries it explicitly. Note `Σ_{x≤X} 1/φ(mx) ≍ log X/φ(m)` has **no** gain, so
  every Brun–Titchmarsh sum must take its gain from a variable coprime to m (f, e, or the divisor
  of `ma²d+1`), never from the modulus alone.

## 2. The spectral and Weil side for general m

Throughout, `t := md`, `4 ≤ m ≤ L^5`, `L := log N`; class counts have TTL §4's orbifold weights.
`h(Δ)` below counts **primitive** proper classes of discriminant `Δ`. Constants are uniform in m.
Statements invoking TTL's spectral argument are relative to its cited Sobolev and large-sieve results.

### 2.1. Separation and invariance — PROVED

**Lemma 2.2_m.** Put `𝓕_t = {[U,B,V] : B²−4UV = −4t, U>0, 2t | B, t | V}`.
This is exactly `{[f,2ta,te] : ef−ta²=1, e,f>0, a∈ℤ}`. Distinct forms satisfy
`cosh dist(z_Q,z_Q') ≥ 3/2`, also after `w=z/t` or `u=z/(tq)`.
The same assertion holds for `[e,2ta,tf]` (the e-cusp).

*Proof.* `4t | disc(Q−Q')`, while TTL Lemma 2.1 gives
`disc(Q−Q') = 8t(cosh dist−1)`. Equality at zero implies identical roots and hence identical forms.
Thus every positive value is at least `4t`. Interchanging e and f preserves the entire set.
Consequently TTL §§4.1–4.4 apply with exactly the same separation constant, independently of m.

For `γ_z=[[p,v],[r,s]]∈Γ⁰(t)`,
`B'=2Upv+B(ps+vr)+2Vrs` is divisible by `2t`, and `V'=Uv²+Bvs+Vs²` by t.
This proves stability under `Γ⁰(t)`; the inverse gives equality, not merely inclusion.
On the z-side the sieve group is `Γ⁰(t)∩Γ(q)`; on the w-side it is
`H_q=Γ₀(t)∩Γ(q)`, provided `(q,t)=1`. Indeed conjugation sends γ_z to `[[p,v/t],[tr,s]]`.
For odd q, reduction of forms modulo q preserves both functionals
`n_f=cB/2−U` and `n_e=cB/2−V/t`. These are exactly n in their respective cusps.
Here stability concerns the **uncut** set with `q|n`; positivity/size conditions on a,n are imposed by weights,
not asserted to be group invariant.

There is no extra middle-coefficient parity restriction for either even or odd m.
If t is even, ef and n are odd; if t is odd, n need not be odd. Always `(ef,t)=1` and `(n,t)=1`.
Exclude 2 from the sieve even when `2∤t`; do not claim it never divides n in that case.
For spectral sequences sieve only `ℓ>ℓ₀`, `ℓ∤2mcd` (excluding c ensures the usual dimension-one upper density).

### 2.2. Groups, hypothesis, and variance — CONDITIONAL on (SEL_m)

Passing to Möbius groups, adjoin `−I` without changing the quotient. With `u=w/q`,
`H_q` becomes `G_{M,q}={γ∈Γ₀(M): γ₁₁≡γ₂₂≡±1 (q), with the same sign}`,
where `M=tq²=mdq²`. Conversely every such matrix conjugates back into `±H_q`.
The infinity cusp has width **1**, and `G_{M,q}⊇Γ₁(M)`.
For odd q>1,
`Γ₀(M)/G_{M,q}≅(ℤ/q)×/{±1}` and
`L²(G_{M,q}\ℍ)=⊕_{χ mod q, χ(−1)=1}L²(Γ₀(M)\ℍ,χ)`.
For q=1 use the single trivial character and index 1, not `φ(1)/2`.

**(SEL_m).** For every level `M=mdq²` under consideration, every even character modulo q,
and squarefree `(q,2md)=1`, the weight-zero Laplacian with that nebentypus has no eigenvalue in `(0,1/4)`.
This is implied by Selberg's conjecture that the nonconstant spectrum on `Γ₁(M)\ℍ`
has bottom at least `1/4`, for **all** positive integers M: each character space embeds in that space.

The DI/Drappeau input applies without changing its level-uniform constant: character conductor
`q₀|q|M`, infinity is singular, and `μ(∞)=1/M`. There is no requirement `(q,M)=1` (it would be impossible!).
The needed coprimality is `(q,t)=1` for the reduction/group construction, not for the large sieve.
At weight zero, `W_{0,it}(4πny)=2√(ny)K_{it}(2πny)`, so Drappeau's `√n ρ(n)` is one half
of the coefficient in TTL's `√y K` convention: no missing power of n.
The bound is `(K²+q₀^{1/2}M^{-1}N₀^{1+ε})‖a‖²` for cusp forms and the full Eisenstein integral.
Verified against [Drappeau, §4.2.2, (4.23)–(4.25)](https://arxiv.org/html/1504.05549#Thmthm1);
the current HTML calls this “Proposition 1”, whereas TTL cites the earlier numbering “Proposition 4.7”.

Thus TTL Proposition 5.1, Steps 0–7, applies verbatim with this group and
`𝓛=log(2+1/(λY)+1/Y+M)`, giving
`‖(1−Δ)P₀‖₂² ≪ 𝓛^C[(λ/Y)(1+q^{1/2}M^{-1}(𝓛/λ)^{1+ε})+λ²/Y]`.
As there, require `Y≤λ𝓛^{-3}`; arbitrary λ>0 is allowed by periodisation.
Here `Y/λ≍1/(A√t)`, so this hypothesis holds in the bad-region cells for large N.
Small boxes not satisfying it are not covered by this stated variance estimate.

### 2.3. Local densities — PROVED

**Lemma 6.1_m.** For `ℓ∤2t`, write `χ_t(ℓ)=(−t/ℓ)`. Then
`g_{c,d,m}(ℓ)=(ℓ−1)/(ℓ²+χ_t(ℓ)ℓ)` if `ℓ∤c`, and
`g_{c,d,m}(ℓ)=(1+χ_t(ℓ))/(ℓ+χ_t(ℓ))` if `ℓ|c`.
Extend multiplicatively to squarefree `(q,2t)=1`. With `Λ(q)` the sieve-restricted orbits under H_q,
`#Λ(q)/vol(H_q\ℍ)=g_{c,d,m}(q)#Λ(1)/vol(H_1\ℍ)`.
The formula is identical for the e-cusp.

*Proof.* The quadric `B²−4UV=−4t` has `ℓ²+χ_tℓ` points: U≠0 gives `ℓ(ℓ−1)`,
and U=0 gives `ℓ(1+χ_t)`. If c≠0, imposing `U=cB/2` forces B≠0 and determines V uniquely,
so gives ℓ−1 points. If c=0 it gives `ℓ(1+χ_t)` points.
For the e-cusp impose `V=tcB/2`; exactly the same counting argument applies.
Reduction of `Γ⁰(t)` onto `SL₂(ℤ/q)` is surjective. For each prime, the nondegenerate quadric
is one orbit: its stabiliser has size `ℓ−χ_t`, giving orbit size `ℓ²+χ_tℓ`.
TTL Lemma 6.1's weighted orbit–stabiliser argument and CRT now prove the assertion, including imprimitive
integral forms (their reductions here are still nondegenerate).
For `(q,c)=1`, `|SL₂(𝔽_ℓ)|g(ℓ)=(ℓ−1)(ℓ−χ_t)≤ℓ²`, hence `#Λ(q)≤q²#Λ(1)`.
Without `(q,c)=1` replace this bound by `2^{ω(q)}q²#Λ(1)`; the density identity itself remains exact.

### 2.4. Per-d count — CONDITIONAL on (SEL_m)

**Theorem 6.2_m.** Take squarefree `(q,2mcd)=1`, and compatible smooth boxes in
`u_Q=(−a+i/√t)/(qf)`, with `λ≍A/(qF)`, `Y≍1/(qF√t)` and the hypothesis of 2.2.
“Compatible” means the weight in the original variables is fixed when q changes.
Put `𝔐_{d,m}=(#Λ(1)/vol(H_1\ℍ))∫ψ_q dμ`; the integral is independent of q since scaling is an isometry.
For any fixed `0<ε≤1/2`,
`|Σ_{Q∈𝓕_t, q|n}ψ_q(u_Q)−g_{c,d,m}(q)𝔐_{d,m}|`
`≪_ε 𝓛^C q #Λ(1)^{1/2}[A√(md)(1+A/(qF))+F^{1+ε}(md)^{-1/2}]^{1/2}`.
The same theorem holds with F=e and `n=cB/2−V/t` in the e-cusp.
If primes dividing c are allowed in q, insert `2^{ω(q)/2}` in the error instead.

*Proof/changes.* Apply TTL Corollary 4.4, 2.3, and the variance formula of 2.2. Here
`λ/Y≍A√t`, `λ²/Y≍A√t·A/(qF)`, and
`q^{1/2}/(MY)=F/(q^{1/2}√t)`.
The last term multiplied by `λ^{-ε}` is
`≪F^{1+ε}t^{-1/2}q^{ε−1/2}A^{-ε}≤F^{1+ε}t^{-1/2}` for A≥1.
This corrects TTL's intermediate assertion `λ^{-ε}≤F^ε`, which alone requires q≲A;
the final error does **not** require that extra hypothesis. Use `#Λ(q)≤q²#Λ(1)` and take square roots.
As in TTL, this is an absolute error, not a uniform relative estimate for an individual d.

### 2.5. Class counts — PROVED

**Lemma 6.3_m (slightly stronger bound).** With the primitive-class convention specified above,
`#Λ_{d,m}(1)≤h(−4t)+1_{t≡3 (4)}h(−t)≪√t log(2t)`.
Consequently
`Σ_{d≤D}#Λ_{d,m}(1)≪m^{1/2}D^{3/2}log(2mD)`.
In particular the requested `≪_ε m^{1/2+ε}D^{3/2}log²(2mD)` holds.

*Proof.* From `ef−ta²=1`, `(f,ta)=1`. The content of `[f,2ta,te]` is therefore either 1 or 2.
Content 2 can occur only for odd a and `t≡3 (4)`; division by 2 then gives a primitive form of
 discriminant −t. For example m=7,d=a=1,e=4,f=2 gives `[2,14,28]`.
Thus TTL's assertion of primitivity cannot simply be transferred to odd m.

In each of these integral SL₂-classes there is **at most one** Γ⁰(t)-orbit meeting 𝓕_t.
Indeed write `G=[[U,B/2],[B/2,V]]`, so `det G=t`. Modulo every prime dividing t this matrix is nonzero
and has rank one; choose a representative with U a unit modulo t (CRT and an SL₂-change).
If `Q∘γ∈𝓕_t`, then the second column of `γᵀGγ` is zero modulo t; hence the second column of γ
lies in `ker(G mod t)`. This kernel has the unique projective generator `(-U^{-1}B/2:1)`.
Second columns in `ℙ¹(ℤ/t)` parametrize right cosets modulo Γ⁰(t), proving the claim.
There is no additional parity index 6 in this normalisation. Orbifold weighting can only reduce the count.
The standard uniform class-number bound `h(Δ)≪√|Δ|log(2|Δ|)` and summation over d finish the proof.

For comparison, retaining only `t|V` as in TTL gives the looser factor
`r(t)≤∏_{p^v∥t}p^{⌊v/2⌋}` multiplying the two class numbers. Keeping also `2t|B` removes r(t):
it forces the radical line, rather than merely an isotropic line. This avoids an unnecessary loss from r(md).

### 2.6. Fixed-a Poisson/Weil count — PROVED

**Proposition 7.1_m (K_a).** Put `k=ma²`, `F=kD/E`; take squarefree `(q,ma)=1`.
With TTL Proposition 7.1's smooth weights and `d=(ef−1)/k`,
`S_a(q)=g'_{c,a,m}(q)X_a+R_a(q)`, where
`X_a=(φ(k)/k²)∫∫W₁(x/E)W₂((xy−1)/(kD))dxdy`
`=Dφ(k)/k·(∫W₁(v)dv/v)(∫W₂(v)dv)≍Dφ(k)/k`,
`g'(ℓ)=(ℓ−1)/ℓ²` for `ℓ∤c`, `g'(ℓ)=1/ℓ` for `ℓ|c`, and
`|R_a(q)|≪2^{ω(q)}τ(k)²(qk^{1/2}+D/E+D/F)`.
The asymptotic notation assumes nonnegative fixed weights with positive integrals.

*Proof/changes.* The exact identity remains
`an=ma²cd−af=c(ef−1)−af=f(ce−a)−c`.
Since `(a,q)=1`, the second congruence is `f(ce−a)≡c (q)`; `(q,k)=1` gives CRT with `ef≡1 (k)`.
Repeat TTL Proposition 7.1, steps (ii)–(v), replacing its modulus called m by k throughout.
The q-local counts are ℓ−1 or ℓ as above; Poisson zero frequency gives X_a.
The axes give `2^{ω(q)}τ(k)(D/E+D/F)`; Weil's general prime-power bound, including powers of 2,
gives `≪2^{ω(q)}τ(k)q√k` off the axes, which is bounded by the displayed error.
No extra parity condition is needed: the proposition even allows `2|q` when ma is odd.
For the campaign use the simpler sieve set `ℓ>ℓ₀`, `ℓ∤2mac`.
Here d varies, so it cannot be part of a fixed excluded-prime modulus; pointwise, `ℓ|d` still implies `ℓ∤n`.
The factor `φ(k)/k=(φ(m)/m)∏_{p|a,p∤m}(1−1/p)` retains the required m-coprimality gain.

### 2.7. Cell remainders and cusp margins — PROVED / CONDITIONAL as indicated

Let `AD≍N/(mc)`, `δ=|log(A/D)|/L`; for D<A, `D/A=N^{-δ}` exactly for the scale parameters.
All estimates below are normalised by the geometric mass scale AD, **not** a claimed lower bound
for the actual number in each cell. Normalising instead by `ADφ(m)/m` costs only `m/φ(m)`.
Weighted divisor averages, `τ(ma²)≤τ(m)τ(a²)`, and the sieve weights cost `L^C m^{C'}` at most.
Within `R_bad(2η₁)`, m only shifts exponent relations by `O(log m/L)`; retain
`E,F≥m^{-C}N^{c₀}`, `c₀=1/2−3η₁`, and `α≥1/3−2η₁−O(log m/L)`.
Choose fixed ε,η₁ sufficiently small in the following absolute-margin estimates.

**Common spectral estimate (CONDITIONAL).** Cauchy–Schwarz and 2.5 give
`Σ_{d≍D}#Λ_{d,m}(1)^{1/2}≪m^{1/4}D^{5/4}L^{1/2}`.
Summing 2.4 over d and sieve q≤Q therefore gives, after renaming ε,
`𝓡_spec/(AD)≪L^C Q²[(mD/A)^{1/2}(1+A/F')^{1/2}+F'^{1/2+ε}/A]`.   (2.7)
Here F' is the selected cusp divisor; this is the precise m-version of TTL's starting estimates.

**(b1), D≥A (PROVED).** Summing 2.6 over a≍A and q≤Q gives
`𝓡_Weil/(AD)≪L^C m^{C'}[Q²m^{1/2}A/D+QN^{-c₀}]`
`≪L^C m^{C'}Q²N^{-δ}`.
For the last step use `δ≤1/3+4η₁+O(log m/L)<c₀` for sufficiently small η₁.
In particular with `Q=N^{δ/4}`, the axis term is still `≤m^{C'}N^{-1/3}`.

**(b2), D<A, e-cusp (CONDITIONAL).** In this region `E=e≲A` and `A/E≲c`
(the allowed b≥a/2 suffices). For the layers `δ≥2γ+O(1/L)`, γ=log c/L,
`N^{-δ/2}(1+A/E)^{1/2}≪N^{-δ/2}c^{1/2}≤O(1)N^{-δ/4}`.
Also `E^{1/2+ε}/A≪A^{-1/2+2ε}`. Since
`A≍(N/(mc))^{1/2}N^{δ/2}`, this is `≪m^{C'}N^{-δ/4}` with a fixed absolute margin.
Thus (2.7) is `≪L^C m^{C'}Q²N^{-δ/4}`. Layers δ<2γ use TTL's BT alternative with modulus mad;
that main-term argument is separate from this spectral statement.

**(b3), D<A, both cusp divisors ≳A (CONDITIONAL).** Use
`F'=min(e,f)≤(ma²d+1)^{1/2}≪√m A√D`.
The first term of (2.7) is `≪√m N^{-δ/2}`. For the second,
`F'^{1/2+ε}/A≪m^{1/4+ε}N^{2ε}D^{1/4}A^{-1/2}`
`≪m^{3/8+ε}N^{2ε−(1−γ)/8−3δ/8}`.
This is both `≪N^{-1/9}` (using m≤L^5 and sufficiently small ε,η₁) and
`≪m^{C'}N^{-δ/4}`, since the latter comparison leaves a fixed margin `(1−γ+δ)/8−2ε`.
Thus the required remainder is `≪L^C m^{C'}Q²N^{-δ/4}`.
TTL's stronger displayed `Q²N^{-δ/2}` does not follow uniformly from its `F'^{1/2+ε}` bound;
the weaker exponent here is exactly sufficient for its chosen κ=1/4.

**(b5), D<A, f-cusp (CONDITIONAL).** Write `v=β−1>0`. When `v≤δ/2+O(1/L)`,
`F=f≲A`, `A/F≍N^v`, so
`N^{-δ/2}(1+A/F)^{1/2}≪N^{-δ/4}`.
The cusp term is `F^{1/2+ε}/A≪A^{-1/2+ε}≪m^{C'}N^{-δ/4}`, as in (b2).
Again (2.7) is `≪L^C m^{C'}Q²N^{-δ/4}`. For v>δ/2, the complementary BT modulus is
`mcdf≍N^{2−β}`: the m cancels using `acd≍N/m`. Its logarithmic saving remains ≍1/(vL).

**Assessment (assembly).** All four pre-sieve bounds are `L^C m^{C'}Q²N^{-κδ}` with
`κ=1` in (b1), `κ=1/4` in (b2),(b3),(b5). With TTL's `Q=N^{κδ/4}` they become
`L^{C''}N^{-κδ/2}` since m≤L^5; there is no nonpolynomial m-loss.
The spectral hypothesis `A√(md)≥𝓛³` and the absolute cusp margins hold throughout these cells.
Layers `δL≲log L` remain assigned to BT. This establishes remainder transfer, not the separate
weighted-mass/BT main-term estimates needed for the final m-uniform theorem.

**Sanity check (finite, not a proof).** Inline `uv run python`, 4 GB memory cap, 40-second timeout,
for `4≤m≤16`, `1≤d≤6`, `|a|≤3`, and good primes through 13:
`PASS: 20526 separation pairs; 2548 local-density cases (both cusps); 124 content-2 forms encountered.`

**Issues found**
- Odd m permits content-2 forms; add the `h(−md)` classes. Keeping the full middle-coefficient condition removes r(md).
- The clean `q√#Λ(1)` error requires `(q,c)=1`; otherwise insert `2^{ω(q)/2}`. The campaign sieve already excludes c.
- TTL's intermediate `λ^{-ε}≤F^ε` is not general; keeping `q^{-1/2}` repairs it without restricting q.
- TTL (b3)'s stronger `N^{-δ/2}` claim is not justified by its displayed ε-loss; `N^{-δ/4}` preserves exactly its assembly κ.
- No new parity obstruction or nonpolynomial m-dependence occurs; for odd md, exclude 2 without asserting n is odd.

## 3. Masses and Brun–Titchmarsh with the coprimality gain

Put `h = φ(m)/m`, `H = 2^{ω(m)}`, `T = L^{100}`, and `ρ_{md}(f) = #{x mod f : mdx²+1 ≡ 0 (f)}`. Constants below are absolute unless a dependence is displayed. Throughout, `4 ≤ m ≤ L^5`, and N is sufficiently large. In particular `H = L^{o(1)}`, `g(m) = L^{o(1)}`; we may use the weaker bounds `H, g(m) ≤ L`. Dyadic end intervals of bounded size are included by positivity. The cutoff T is deliberately generous.

**Assessment.** A literal, all-ranges version of TTL Lemma 8.3(c) with the factor h is not available and is in fact false. The correct transfer uses a large-D, large-F lemma, treats the remaining ranges separately in Brun–Titchmarsh, and removes **all `D ≤ T`**, not just `D ≤ 64`, from the spectral assembly. This modification costs `O(NL²/m)` and avoids a spurious `log m` in each spectral cell.

### 3.1. Brun–Titchmarsh outside the bad region (B1)

**PROVED.** For `P ∈ {ab, acf, cdf}`, let `𝒮_P(N)` denote the MN4 §1 tuples with prime `N/2 < n ≤ N` and respectively `mab`, `macf`, `mcdf ≤ N^{1−η₁}`. For fixed `0 < η₁ < 1/2`,

`#𝒮_P(N) ≪ η₁^{−1} NL²/m`.

*Proof.* The exact fibres are as follows.
* Fix `(a,c,f)`. Necessarily `(f,ma)=1` (not necessarily `(f,2ma)=1`); `d ≡ −(ma²)^{−1} (mod f)`, and n runs injectively through one class modulo `macf`.
* Fix `(c,d,f)`. There are `ρ_{md}(f)` classes of a modulo f, and each gives one injective progression modulo `mcdf`. In particular `(f,md)=1` whenever the root count is nonzero.
* Fix `(a,b,c)`. Here `e=(a+b)/c`, `(e,mab)=1`, and `d ≡ (mab)^{−1} (mod e)`. Consequently `n=(mabd−1)/e` runs injectively through one class modulo `mab`. The number of possible c is at most `τ_m(a+b) := #{e | a+b : (e,m)=1}`. Also `a ≤ 2b`.

BT bounds a fibre of multiplicity ρ and modulus q by `ρ[2N/(η₁Lφ(q))+1]`. Non-reduced residue classes contribute at most one prime each. Since `φ(mx₁⋯x_r) ≥ φ(m)∏φ(x_i)`, it suffices to bound the following three harmonic masses by `O(hL³)`:

`U_acf = Σ_{a,c,f≤3N,(f,m)=1} 1/(φ(a)φ(c)φ(f))`,
`U_ab = Σ_{ab≤3N,a≤2b} τ_m(a+b)/(φ(a)φ(b))`,
`U_cdf = Σ_{c≤3N} 1/φ(c) Σ_{d,f≤3N} ρ_{md}(f)/(φ(d)φ(f))`.

For the first, expand `1/φ(f) = f^{−1}Σ_{r|f} μ²(r)/φ(r)`. MN3 Lemma 2.1 gives
`Σ_{f≤X,(f,m)=1} 1/φ(f) ≤ W_m(X) Σ_r 1/(rφ(r)) ≪ h log X`
when `X≥ω(m)+2`; use `X=3N`. The two unrestricted harmonic sums are `O(L)`.

For `U_ab`, 3.2(b) below gives `O(h log(2B))` per dyadic `(A,B)` box with `B≥T`. There are `O(L²)` boxes, so these total `O(hL³)`. If `B<T`, then `A≪T` because `a≤2b`; the ordinary TTL 8.3(b), with `τ_m≤τ`, gives total `O((log T)³)`. This is absorbed in `hL³`.

For `U_cdf`, 3.2(c) gives `O(h)` per `(D,F)` box with `D,F≥T`, hence `O(hL²)` before the c-sum. For `F<T`, use `ρ_{md}(f)≤4τ(f)` and
`Σ_{f≤2T} τ(f)/φ(f) ≪ (log(2T))²`;
this follows by expanding g and using `τ(rs)≤τ(r)τ(s)` and `Σ τ(r)/(rφ(r))<∞`. Thus these ranges total `O(L(log L)²)`. For `D<T`, the pointwise bound in 3.2(c) is `Σ_{f≍F}ρ_{md}(f)/φ(f) ≪ log(2md)`, giving the same total `O(L(log L)²)`. Since `g(m)(log L)²=o(L)`, both are absorbed in `hL²`. Finally sum over c.

The additive fibre terms total `O_ε(N^{1−η₁+ε})`: there are `O(X log²(2X))` triples with product at most X, and the root/divisor multiplicities are `O_ε(N^ε)`. Taking `ε<η₁/2`, this is absorbed in `NL²/m`. Multiplying the harmonic bounds by `N/(η₁Lφ(m))` proves the assertion. ∎

### 3.2. Weighted divisor and root sums (B2)

**PROVED (b).** If `B≥T`, then

`Σ_{a≍A,b≍B,a≤2b} τ_m(a+b)g(a)g(b) ≪ hAB log(2B) + A√B log(2B)`.

In particular this is `O(hAB log(2B))` in that range. For `B<T`, the ordinary bound `O(AB log(2B))` remains valid.

*Proof.* For any n let v be its largest divisor coprime to m. Then `τ_m(n)=τ(v)`, and pairing divisors of **v**, not of n, proves
`τ_m(n)≤2#{e|v:e≤√v}≤2#{e|n:e≤√n,(e,m)=1}`.
Thus the needed small-divisor inequality does survive; its justification must use the m-free part.

Fix a with `a≤4B`, put `Z=√(6B)`, and expand `g(b)=Σ_{l|b}μ²(l)/φ(l)`. The preceding inequality gives
`Σ_{b≍B,l|b}τ_m(a+b) ≤ 2Σ_{e≤Z,(e,m)=1}[B(l,e)/(le)+1] ≪ (B/l)τ(l)W_m(Z)+Z`.
To check the harmonic estimate, expand `(l,e)=Σ_{t|(l,e)}φ(t)`: only `(t,m)=1` contribute, and the resulting term is `(φ(t)/t)W_m(Z/t)≤W_m(Z)`. Since `Z≥ω(m)+2`, MN3 Lemma 2.1 gives `W_m(Z)≪h log(2B)`.

Multiply by `μ²(l)/φ(l)` and sum `l≤2B`. The series `Σ τ(l)/(lφ(l))` converges, whereas `Σ_{l≤2B}1/φ(l)≪log(2B)`. Finally `Σ_{a≍A}g(a)≪A`. This proves the stated estimate. In the range `B≥T`, the relative error is `O(g(m)/√B)=o(1)`; for smaller B discard coprimality and apply TTL 8.3(b). ∎

**PROVED (c).** Uniformly for `T≤D,F≤3N`,

`Σ_{d≍D} g(d) Σ_{f≍F} ρ_{md}(f)/φ(f) ≪ hD`.

This covers every retained bad-region cell of TTL (b2),(b5): there `F≥N^{1/2−3η₁}` (with harmless polylogarithmic adjustments) and `D≤N^{1/2}L^{O(1)}`. The proof also gives explicit errors before their absorption.

*Proof: character mean square.* Let `χ_d=(−4md/·)`, `S_d(Y)=Σ_{r≤Y}χ_d(r)/r`. For `D≥T` and every Y,

`Σ_{d≍D}|S_d(Y)|² ≪ D`, and consequently `Σ_{d≍D}|L(1,χ_d)|² ≪ D`.

For `Y≤Y₀=D/log²(2D)`, expand the square. Even `rr'` contribute zero. For odd `rr'`, `χ_d(rr')=(−m/rr')(d/rr')`; if `(m,rr')>1` the coefficient is zero, otherwise it has absolute value one. Square `rr'` contribute `O(D)`, because `Σ_{rr'=square}1/(rr')<∞`. For nonsquare `rr'`, PV for the nonprincipal Jacobi character modulo `rr'` gives an inner sum `O(√(rr')log(2rr'))`. Thus the off-diagonal is `O(Y log(2Y))=O(D)`. PV is valid also for imprimitive characters (MN3 Lemma 2.2). For `Y>Y₀`, PV in r and partial summation give
`S_d(Y)=S_d(Y₀)+O(√(mD)log(2mD)/Y₀)=S_d(Y₀)+O(1)`.
The last bound uses `m≤L^5`, `D≥L^{100}`, and `D≤3N`. The same argument permits `Y=∞`. This checks uniformity in m; TTL's bounded-D shortcut would not do so.

*Proof: a coprime convolution estimate.* Local root counting gives
`ρ_{md}(f) ≤ 4·1_{(f,m)=1}(1*χ_d)(f)` and `ρ_{md}(rf')≤2^{ω(r)}ρ_{md}(f')` for squarefree r.
For odd primes this is Hensel's lemma; primes dividing md give no roots. At 2 the root count is at most four, and increasing the exponent by one increases it by at most two. This also proves the second inequality at 2.

Put `V=C√(mD)log(2mD)` with C the PV constant and `J=log(2mD)`. For `u≥1`, Dirichlet's hyperbola decomposition and inclusion–exclusion give

`Σ_{f≤u,(f,m)=1}(1*χ_d)(f) ≪ hu|L(1,χ_d)| + J√(HVu)`.

Here are the error details. Sum first over the χ-variable `r≤U`; the coprime count in the other variable is `hu/r+O(H)`. The complementary hyperbola has absolute value at most `2Vu/U`, and replacing `S_d(U)` by `L(1,χ_d)` costs at most `huV/U`. Taking `U≈√(uV/H)` works when `u≥V/H` and gives `O(√(HVu))`. If `u<V/H`, discard the coprime restriction and use
`Σ_{f≤u}(1*χ_d)(f)=uS_d(u)+O(u) ≪ uJ`;
PV implies `|S_d(u)|≪J` for all u. Since `√(HV/u)>H≥1`, the claimed bound follows also in this case. All coefficients of `1*χ_d` are nonnegative.

Now expand `1/φ(f)` and use the squarefree-r inequality. The convergent series `Σ 2^{ω(r)}√r/(rφ(r))` gives

`Σ_{f≍F}ρ_{md}(f)/φ(f) ≪ h|L(1,χ_d)| + J√(HV/F)`.

Terms with `F/r<1` obey the same estimate after summation, since then only `f'=1` can occur and their total is bounded by a constant times `F^{−1/2}`. Cauchy–Schwarz, `Σ_{d≍D}g(d)²≪D`, and the mean square just proved yield

`Σ_{d≍D}g(d)Σ_{f≍F}ρ_{md}(f)/φ(f) ≪ D[h + J√(HV/F)]`. (3.2.1)

*Proof: the complementary range.* Averaging directly in d gives another estimate. For `(f,m)=1`, each unit x modulo f determines `d≡−(mx²)^{−1} (mod f)`. Expanding `g(d)` with `d=lt`, terms with `(l,f)>1` vanish; the remaining terms give
`Σ_{d≍D}g(d)ρ_{md}(f) ≪ φ(f)[D/f+log(2D)]`.
Coprime inclusion–exclusion on a dyadic f-interval therefore gives

`Σ_{d≍D}g(d)Σ_{f≍F}ρ_{md}(f)/φ(f) ≪ D[h+H/F]+F log(2D)`. (3.2.2)

If `F≤D/L^{20}`, (3.2.2) proves the assertion. Otherwise (3.2.1) does: using `H≤L`, `J≪L`, its relative error is at most `O(L^{14}D^{−1/4})`, which is `o(h)` for `D≥L^{100}`. This proves (c).

For completeness, in all ranges the same expansion, without the coprime restriction, and `Σ_{f≤u}(1*χ_d)(f)=uS_d(u)+O(u)` prove the pointwise estimate `Σ_{f≍F}ρ_{md}(f)/φ(f)≪log(2md)` used in 3.1. ∎

### 3.3. Weighted Type I masses (B3)

**PROVED, relative to MN3 Prop 2.3.** Write `M(a,d)=ma²d+1`, and assume `L²≤A≤N`, `1≤D≤N`.

(a1) If `D≥A`, then `Σ_{a≍A,d≍D}τ(M(a,d))g(a)≪hADL`. If `D<A`, then
`Σ_{a≍A,d≍D}τ(M(a,d))g(d) ≪ hADL[1+min(log(2m), m^{1/6}log(2mD)/√D)]`.
In particular the bound is `O(hADL)` when `D≥T`.

(a2) If `A,D≥N^{1/4}`, then `Σ_{a≍A,d≍D}τ(M(a,d))g(a)g(d)≪hADL`.

(b) If `D,F≥T` and `F≤K₀A`, with K₀ fixed, then
`Σ_{d≍D}g(d) #{(a,f):a≍A,f≍F,f|M(a,d)} ≪_{K₀} hAD`.
The identical statement holds with e instead of f.

We also need the following substitute for the discarded low-D cells:
(a3) If `D≤T` and `A≥N^{0.3}`, then `Σ_{a≍A,d≍D}τ(M(a,d))g(a)g(d)≪hADL log(2m)`.

*Proof of (a1).* For `D≥A`, expand g(a), writing `a=ra'`. Apply MN3 2.3(a), with coefficient `k=mr²`, linear length `2D`, quadratic length `max(2,2A/r)`, and exponent parameter 40. Its coefficient-size condition follows from `k·max(2,2A/r)²≪mA²≪D^{40}`. Also `2D≥ω(k)+2`, since `D≥L²`. The gain `φ(k)/k≤h`, and summation with weight `μ²(r)/φ(r)` uses `Σ1/(rφ(r))<∞`.

For `D<A`, expand g(d), writing `d=td'`, and apply MN3 2.3(b) with `k=mt`, linear length `max(2,2D/t)`, quadratic length `2A`. Now `k·max(2,2D/t)≪mD≪A^{40}` and `2A≥ω(2k)+2`. Its two bounds for Λ are, up to absolute constants,
`1+log(2mt)` and `1+m^{1/6}t^{2/3}log(2mD)/√D`.
Sum them separately with `1/(tφ(t))`; both the logarithmic series and the series with `t^{2/3}` converge. Taking the smaller bound proves (a1). Thus `log(1+k)` is not paid as `log m` in the retained layers.

*Proof of (a2).* Expand both weights, `a=ra'`, `d=td'`, with coefficient `k=mr²t`. The tails `r>√A` or `t>√D` are at most
`O_ε(N^ε AD(A^{−1/2}+D^{−1/2}))=o(hAD)`;
here use the divisor bound for `M≪N^4`, counting multiples by `O(A/r)`, `O(D/t)`, and `Σ_{r>R}1/(rφ(r))≪1/R`. Choose ε sufficiently small.

On the remaining ranges, both shortened lengths are at least `N^{1/8}`. If `D≥A`, the condition for MN3 2.3(a) is `O(mtA²)≤(2D/t)^{40}`; if `D<A`, that for 2.3(b) is `O(mr²D)≤(2A/r)^{40}`. Each left side is `O(L^5N^3)`, while the appropriate right side is at least `N^5`; the ω-conditions also hold. In the quadratic case use the second Λ-bound:
`Λ≪1+m^{1/6}r^{1/3}t^{2/3}log(2mr²D)/√D`.
Its weighted sum is `O(1+m^{1/6}log(2mD)/√D)=O(1)`, since the r- and t-series, including the extra `log r`, converge. Every application retains `φ(k)/k≤h`. This proves (a2), without a `log m` loss.

*Proof of (b).* Each `(d,f)` permits at most `ρ_{md}(f)(A/f+1)≤(1+2K₀)Aρ_{md}(f)/f` values of a. Apply 3.2(c), using `1/f≤1/φ(f)`. Divisor symmetry proves the e-version.

*Proof of (a3).* Expand both weights as before and discard only `r>√A` by the divisor bound; its contribution is `o(hAD)`. For every remaining r and every `t≤2D`, apply MN3 2.3(b). The quadratic length is at least `√A≥N^{0.15}`, while `k·max(2,2D/t)≪mr²D≤L^{105}A`; exponent 40 therefore suffices, as does the ω-condition. Use `Λ≪1+log(2mr²t)` and sum with `1/(rtφ(r)φ(t))`. The logarithms of r and t have convergent weighted sums, leaving only `O(log(2m))`. ∎

### 3.4. The large-c part (B4)

**PROVED, relative to MN3 Prop 2.3 and its Prop 2.5 block estimates.** For fixed η>0, the tuples with `c>N^η` contribute

`≪ η^{−1}N(L²+L log² m)/m + N m^{−0.35}/L`.

*Proof.* Since `macd=n+f≤3N`, this range has `mad<3N^{1−η}`. Fix `(a,d,f)`; `(f,mad)=1`, and n lies in one class modulo mad. BT now gives `O(N/(ηLφ(mad)))` per divisor f. This bounds tuple multiplicity, not merely the number of represented primes.

Here are the changed lines in the proof of MN3 2.5. Its expansion `1/φ(ad)≪(ad)^{−1}Σ_{s|a,t|d}1/(st)`, substitution `a=sa'`, `d=td'`, `k=ms²t`, and its regular/tiny split are unchanged. In each dyadic ad-block, the regular part of the weighted divisor sum is

`≪ h Σ_{s,t}(st)^{−2}[L²+L log²(2ms²tL)] ≪ h[L²+L log² m+L log² L] ≪ h[L²+L log² m]`.

The first inequality follows exactly as there: apply 2.3(a) when the linear side dominates, and 2.3(b) otherwise; Λ is bounded except for `O(log(2k)+log L)` quadratic-side boxes, on which it is `O(log(2k))`. The conditions hold with exponent 30 whenever the longer side is at least `k^{1/28}`; finitely many bounded k can be covered by increasing the constant. The displayed summation also shows why **the hypothesis `L≤√m` of MN3 2.5 is unnecessary here**: replace its use of `log L≤log m` by `L log² L≪L²`.

Replace its final `Σ_j1/j≪log L` by `Σ_{O(L) blocks}1/(ηL)≪η^{−1}`. Multiplication by `N/φ(m)` gives the required regular contribution.

For precision, the tiny weighted mass in an ad-block X, proved in MN3 2.5 by the divisor bound and grouping `u=st`, is
`E(X)≪m^{0.013}min(1,(X/m^{0.072})^{−0.85})`, and `Σ_X E(X)≪m^{0.014}`.
For `X≤N^{1/2}`, the BT denominator is actually `≍L`, because `m≤L^5`; thus their total count is at most
`N m^{0.014}/(Lφ(m)) ≪ N m^{−0.35}/L`.
For `X>N^{1/2}`, the displayed tail gives `Σ E(X)≪m^{0.08}N^{−0.425}`. Even using the weaker BT denominator `≳1`, its contribution is absorbed by `NL²/m`. These are precisely the tiny-box estimates, now with the necessary logarithmic saving rather than the old denominator bound by 1. ∎

### 3.5. Sieve main terms and the bands (B5)

**PROVED (main-term accounting, relative to the transferred local-density/counting formulas).** Suppose the m-versions of TTL Props 7.1 and Thm 6.2 supply the usual model masses and remainders. Remove `D≤T` as described below. Then the sieve main terms are

`≪ (κδL)^{−1}(N/m)L` per layer, and `≪(κδL)^{−1}N/m` per cell in (b2),(b5).

There is no factor `g(m)`. All the bands, including the enlarged low-D region, cost `O(NL²/m)`.

*Proof: sieve denominator.* For a sequence with fixed `s∈{a,d}`, sieve only by `ℓ>ℓ₀`, `ℓ∤2mcs`. The transferred densities ν satisfy `1/ℓ−2/ℓ²≤ν(ℓ)≤1/ℓ`. With `M=2mcs` and `z=N^{κδ/8}`, the Selberg denominator obeys
`G(z)≥c h(M)log z`, where `h(M)=φ(M)/M`.
Here is a uniform elementary justification. Restrict its Euler factors to allowed primes `ℓ≤z^ε` for a sufficiently small absolute ε. In the probability measure on their squarefree products with weights `∏ν(ℓ)/(1−ν(ℓ))`, the expected `log r` is at most `Σ_{ℓ≤z^ε}ν(ℓ)logℓ≤Cε log z`. Markov's inequality puts at least half the Euler-product mass at `r<z`. The unrestricted product over these allowed primes is
`∏(1−ν(ℓ))^{−1} ≫ log z ∏_{ℓ|M,ℓ≤z^ε}(1−1/ℓ) ≥ h(M)log z`,
by Mertens and convergence of the `O(ℓ^{−2})` local discrepancies. Bounded z is covered by `G(z)≥1`. The omitted fixed primes cost only an absolute constant.

*Proof: fixed-a sequences.* Put `K=ma²`. Their zero-frequency mass is
`X_a=(φ(K)/K²)∫∫W₁(x/E)W₂((xy−1)/(KD))dxdy ≪ Dφ(K)/K`.
This is simply the number `φ(K)` of pairs `ef≡1 (mod K)` divided by `K²`, times an integral of size `KD`. Moreover
`g(2mca)φ(ma²)/(ma²)≤2g(c)`.
Thus, after summing `a≍A`, `c≍C`, a single cell has sieve-weighted model mass `O(CAD)=O(N/m)`. Summing its `O(L)` divisor cells gives `O((N/m)L)` per layer. This exhibits the cancellation directly, without replacing this model by an unweighted mass.

*Proof: fixed-d sequences.* At q=1 the transferred counting formula gives `X_σ≤#σ+|r_σ(1)|`, also for nonnegative smooth weights. Since `g(2mcd)≤2g(m)g(c)g(d)`, 3.3(a1), with `D≥T`, gives
`Σ_σ g(2mcd)#σ ≪ g(m)C·hADL ≪ (N/m)L`
for a whole layer. In the (b2),(b5) cells, use 3.3(b) instead: `F'∈{E,F}≤K₀A` and `F'≥N^{1/2−3η₁}`, giving `O(N/m)` per cell. Multiplication by `1/log z=8/(κδL)` proves the claims.

The term involving `r_σ(1)` is a remainder, not a new main term. Multiplication by `g(2mcs)≪(log L)^3` is absorbed in the polylogarithmic remainder allowance. In particular a transferred bound `L^C(N/m)N^{−κδ/2}` remains of that form after this multiplication, and is negligible for `δL≥C₁log L`, with C₁ sufficiently large. This statement does not replace the separate proof of the transferred spectral remainder.

*Proof: ordinary bands.* For `D≥T`, the bands `|β−(α+γ)|≤C₀/L` and `|β−1|≤C₀/L` have, respectively, e or f at most `K₀A`; each is also at least the bad-region lower bound. By 3.3(b) each cell, summed over `c≍C`, contains `O(hCAD)≤O(N/m)` tuples. There are `O(L)` such cells per c-block and `O(L)` c-blocks, giving `O(NL²/m)` even without primality.

*Proof: all low-D cells, including `D≤64`.* Do **not** use a per-cell character bound. For `D≤T`, `c≍C≤N^η`, the relation `mCAD≍N` ensures `A≥N^{0.3}` for fixed small η and large N. Aggregate all divisors f and use 3.3(a3). Fixing `(a,d,f)`, BT in c gives at most
`O(C g(mad)/(1+log C))`
prime values n when `C≥2`; for bounded C the trivial bound `O(C)` is sufficient and is smaller than the same expression up to a constant. Hence an entire `(C,D)` block costs
`≪ [C g(m)/(1+log C)]·hADL log(2m) ≪ (N/m)L log(2m)/(1+log C)`.
There are `O(log T)=O(log L)` D-blocks, and the reciprocal-log weights over the C-blocks total `O(log L)`. Therefore **all** `D≤T` cost
`O((N/m)L log(2m)(log L)²)=O(NL²/m)`.
This is the required aggregated repair of the bounded-D band and also removes the entire range where the character mean-square argument is not uniform in m. ∎

### Issues found

* The literal all-ranges `hD` root-sum bound is false: for a fixed d (e.g. d=2), choose m by CRT so that `−md≡1` modulo every odd prime power up to `2F`. Then the odd squarefree f in `(F,2F]` have `ρ_{md}(f)=2^{ω(f)}`, and their weighted sum is at least a positive constant times `log F`, whereas `hD≤D`. To justify that growth, the Dirichlet series of `1_{f odd}μ²(f)2^{ω(f)}` is `ζ(s)²E(s)`, with E absolutely convergent for `Re s>1/2` and `E(1)>0`; convolution with the elementary divisor summatory formula gives `Σ_{f≤x,f odd}μ²(f)2^{ω(f)}∼E(1)x log x`. Taking a dyadic difference and using `1/φ(f)≥1/(2F)` gives the asserted lower bound. Taking N sufficiently large makes such m admissible under `m≤L^5`. The large-range statement and the explicitly treated small ranges above are essential.
* Pairing e with `n/e` need not preserve coprimality to m. Nevertheless the required small-divisor inequality for `τ_m` is true: pair divisors of the largest m-coprime divisor of n instead, as proved in 3.2(b).
* PV in the character variable introduces `√m`; the TTL bounded-D argument cannot be declared uniform. Removing `D≤L^{100}` repairs this without changing the target bound.
* MN3 2.5's stated hypothesis `L≤√m` cannot simply be imported. Section 3.4 repairs its logarithmic comparison and obtains the tiny-box `1/L` from BT itself.
* No mass/BT issue remains in this section after these changes. The m-dependent spectral/Weil remainder formulas and local densities are inputs to 3.5, not proved here; a proof of the complete conditional theorem must establish them separately. No existing repository file was changed.

## 4. Assembly: Theorem I_m (CONDITIONAL on (SEL_m))

**Theorem 4.1 (= Thm I_m; CONDITIONAL on (SEL_m) of §2.2; relative to the results cited in TTL Thm 8.1,
MN3 Prop 2.3/2.5, and §§1–3 here).** There is an absolute `N₀` such that for `N ≥ N₀` and `4 ≤ m ≤ L^5`:
`Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L² + L log² m)/m + N m^{−0.35}/L`.

*Proof.* TTL Thm 8.1's proof, steps (1)–(5), with the following replacements (all constants absolute;
fix η, η₁ small as in TTL). By Lemma 1.1, bound `Σ_c Σ_{N/2<p≤N} w_{c,m}(p)` (a count of tuples (c,a,d,f)).
* (1) `c > N^η`: §3.4 — `≪ η^{−1}N(L² + L log² m)/m + N m^{−0.35}/L` (replaces MN3 Thm 3.8(1)).
* (2a) some modulus `mab, macf, mcdf ≤ N^{1−η₁}`: §3.1 — `≪ η₁^{−1}NL²/m`. The remaining tuples have
  `c ≤ N^η`, all seven moduli `≥ N^{1−η₁}` up to the factor `m ≤ L^5`, so their exponents lie in
  `R_bad(η₁ + O(log L/L)) ⊂ R_bad(2η₁)`, and `e, f ≥ N^{1/2−3η₁}` (e, f have m-free exponents, §1).
* (2b-low) `D ≤ T = L^{100}`: §3.5 last part (aggregated Brun–Titchmarsh in c) — `≪ NL(log L)³/m`.
* (2b) `D > T`, smooth cells of side `O(1/L)` in `(α, β)`; `δ := |log(A/D)|/L`, `k := ⌊δL⌋`, c-block `c ≍ 2^j`.
  Bands (`|β−(α+γ)| ≤ C₀/L`, `|β−1| ≤ C₀/L`): §3.5 — `≪ NL²/m`. Off the bands, the treatments (b1)–(b5) of
  TTL with: (b1) Prop 7.1_m (§2.6) and §2.7(b1); (b2) (`k ≥ 2j`) Thm 6.2_m in the e-cusp, §2.7(b2), and
  (`k < 2j`) (b4); (b3) Thm 6.2_m, §2.7(b3) (relative remainder `Q²N^{−δ/4}`, κ = 1/4 as in TTL);
  (b4) for fixed (a,d,f) the n with `c ≍ 2^j` lie in one class mod `mad` in an interval of length
  `≤ mad·2^{j+1}`, so BT gives `≪ 2^j g(m)g(a)g(d)/j`, and §3.3(a2) (`A, D ≥ N^{1/4}` for `δ ≤ 1/3`,
  since `AD ≥ N^{1−η}L^{−5}`) gives a layer cost `≪ 2^j g(m)·hADL/j ≍ (N/m)L/j` (`h g(m) = 1`, `m2^jAD ≍ N`);
  (b5) f-cusp Thm 6.2_m / §2.7(b5) if `k' ≤ k/2`, else BT on `mcdf ≍ N^{2−β}`: per cell
  `Σ_{c≍2^j}Σ_{d≍D}Σ_{f≍F} ρ_{md}(f)·N/φ(mcdf) ≤ N g(m)·Σ_c g(c)/c·D^{−1}Σ_d g(d)Σ_f ρ_{md}(f)/φ(f) ≪ N g(m)h/m = N/m`
  by §3.2(c) (`D, F ≥ T`), with the saving `C/k'` from `log(N/(mcdf)) ≫ k'`.
* (3) Selberg sieve per sequence: §3.5 — main terms `≪ (κδL)^{−1}(N/m)L` per layer ((b1), (b3)) and
  `≪ (κδL)^{−1}N/m` per cell ((b2), (b5)), **with no factor m/φ(m)** (the sieve loss `g(2mcs)` is paid by the
  gain h of the masses: §3.3, and explicitly `g(2mca)φ(ma²)/(ma²) ≤ 2g(c)` in (b1)). Remainders (§2.7):
  `≪ L^C m^{C'}Q²N^{−κδ}` relative to the geometric mass, with `Q = z² = N^{κδ/4}`, i.e. `≪ L^{C''}N^{−κδ/2}`
  as `m ≤ L^5`; this is `≪ C/k` once `k ≥ C₁ log L`.
* (4) Layers `k ≤ C₁ log L`: (b4) on every cell, `≪ Σ_{j≤ηL}(C₁ log L)(N/m)L/j ≪ (N/m)L(log L)²`.
* (5) Summation exactly as TTL (5), every term multiplied by `1/m`: TTL Lemma 1.1 gives
  `Σ_{j,k≤L}(N/m)L·min(1/j, C/k) ≪ NL²/m`; (b5) `≪ ηNL²/m`; (b2) with `k < 2j`: `≪ NL²/m`.
Adding (1), (2a), (2b-low), bands and (5): the claim (`(log L)³ ≪ L`, `L log² m ≥ 0`). ∎

*Remarks.* (i) For m = 4 this is TTL Thm 8.1 restricted to `(N/2, N]` (the `log² m`, `m^{−0.35}` terms are
O(1) multiples of the main term). (ii) Where m enters: only through `h = φ(m)/m` (main terms, cancelling the
sieve's `g(m)`) and polynomially in remainders. The restriction `m ≤ L^5` is used only to absorb `m^{C'}`
into `L^{C}` and `2^{ω(m)}, g(m) ≤ L^{o(1)}` into lower-order terms; it costs nothing by Lemma 0.1.

## 5. The lower side without log L, and the sharp-order transition (CONDITIONAL on (SEL_m))

`ρ_rep(m,N)` = proportion of m-representable primes in `(N/2, N]` (MN2 Thm L); `A := L/m^{1/3}`.

**Theorem 5.1 (= Thm L''; CONDITIONAL on (SEL_m)).** For all `m ≥ 4`, `N ≥ 16`:
`ρ_rep(m,N) ≪ (L³ + L² log² m)/m + m^{−0.35}`, i.e. `ρ_rep ≪ A³ + A² m^{−1/3} log² m + m^{−0.35}`.
*Proof.* Cases.
(i) `log m > L/10`: MN2 Lemma 3.5 gives `ρ_rep ≤ e^{CL/log L}/m`. If `L ≥ L₀ := e^{20C}` then
`CL/log L ≤ 10C log m/log L ≤ 0.65 log m`, so `ρ_rep ≤ m^{−0.35}`; if `L < L₀` then either `ρ_rep = 0` or
`m ≤ 3e^{L} < 3e^{L₀}` (MN2: `L ≥ log(m/3)` if `ρ_rep > 0`), and the claim is trivial (RHS ≫ 1).
(ii) `log m ≤ L/10`, `m > L^5`: Lemma 0.1 (MN3 Thm L'; `L ≤ m^{1/5} ≤ m^{1/2}`), unconditional.
(iii) `m ≤ L^5` (so `log m ≤ L/10` for N ≥ N₀): `π*(N) ≫ N/L`; Type II primes: MN2 Prop 3.2, `≪ (N/L)(L³ + m^{0.02})/m`;
Type I primes: at most `Σ_{N/2<p≤N} f_{I,m}(p)`, Theorem 4.1 for `N ≥ N₀`. Divide by `π*(N)`;
`m^{0.02}/m ≤ m^{−0.35}`. For `N < N₀` the claim is trivial as in (i) (m ≤ L^5 bounded). ∎

**Theorem 5.2 (sharp order of the transition; CONDITIONAL on (SEL_m) for the lower half only).**
For every `ε ∈ (0,1)` there are `c_ε, A_ε > 0` and `m_ε` such that for all `m ≥ m_ε` and `N ≥ 16`:
* (lower; CONDITIONAL on (SEL_m)) `log N ≤ c_ε m^{1/3}` ⟹ `ρ_rep(m,N) ≤ ε`;
* (upper; PROVED unconditionally, MN2 Thm U, ineffective) `log N ≥ A_ε m^{1/3}` ⟹ `ρ_rep(m,N) ≥ 1 − ε`.
So under (SEL_m) the density transition for m/p sits at `log N ≍ m^{1/3}`, with matching orders on
both sides (absolute constants; only the window constants `c_ε, A_ε` depend on ε).
*Proof.* Lower: Thm 5.1 with `A ≤ c_ε`: `ρ_rep ≤ C(c_ε³ + c_ε² m^{−1/3}log² m + m^{−0.35}) ≤ ε` for `c_ε = (ε/3C)^{1/3}`
and `m ≥ m_ε`. Upper: MN2 Thm U (`ρ_exc = 1 − ρ_rep`), valid for all `m ≥ 4`. ∎
(`m ≥ m_ε` is needed only for the lower half, to make `m^{−0.35}` and `m^{−1/3}log² m` small; for bounded m the
transition question is about bounded N and is not asymptotic.)

*Remarks.* (i) Theorem 5.1 gives the profile bound `ρ_rep ≪ A³` for `m^{−0.11} ≪ A ≪ 1` (the other two terms
are then smaller), the same shape as the small-A end of the EVIDENCE fit `1 − exp(−κA³)` of MN2 §2.
That fit is evidence only. (ii) MN2 Conj C2 (no sharp threshold) is untouched: nothing here says whether
`ρ_rep` has a limit profile `F(A)`.

## 6. What is unconditional

* Unconditional and new here (PROVED): Lemma 1.1 (reduction for general m); §2.1 (separation and
  parity-free invariance for the level-md Heegner forms `[f, 2mad, mde]`, all m); §2.3, §2.5, §2.6 (local
  densities, class counts `≪ √(md) log`, the (K_a) count with modulus `ma²`); §3 (Brun–Titchmarsh masses with
  the exact `φ(m)/m` gain, uniform for `m ≤ L^5`; §3.4 also drops MN3 Prop 2.5's hypothesis `L ≤ √m` in that
  range). §3.2(c) needs `D, F ≥ L^{100}`: the all-ranges version is **false** (Issues in §3).
* Unconditionally the lower side remains MN3 Thm L': `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}`, i.e. the
  transition is pinned to `c(m/log m)^{1/3} ≤ log N ≤ A m^{1/3}` (the `(log m)^{1/3}` gap is the BT `log L`
  at `L ≍ m^{1/3}`). The SEL-free part of the argument fails exactly as in TTL §9: the strip near `d = a`
  where Kim–Sarnak's exceptional eigenvalues beat the saving has positive width in `log(A/D)/L`, independent of
  m (m enters only through `L^{O(1)}` factors), and a positive-width strip still costs `log L`.
* (SEL_m) is used only in Prop 5.1 of TTL (via Thm 6.2_m) for `Γ₀(mdq²)` with even nebentypus mod q; it is
  implied by Selberg's conjecture `λ₁ ≥ 1/4` for all `Γ₁(M)`, and is the same hypothesis family as TTL's
  (levels `4dq²` there), now also with levels divisible by m.

## Replay

```
PYTHONPATH=scripts uv run python scripts/emn4_checks.py      # ~10 s; output scripts/emn4_checks.out.txt
```
Finite checks (not proofs): Lemma 1.1 by brute force (m ≤ 12, p < 120); separation §2.1 (min cosh = 3/2
exactly, attained: the constant is sharp); local densities §2.3 for both cusps; content-2 forms for
t ≡ 3 (4) (§2.5); EVIDENCE for the §3.2(c) gain: the ratio `Σ_{d≍D} g(d) Σ_{f≍F} ρ_{md}(f)/φ(f) / (hD)`
stays in `[1.05, 1.34]` (D = F = 300) while `h = φ(m)/m` ranges over `[0.21, 1]` (m = 4 … 2310, 7, 143, 1009);
the raw sum tracks h. Proof-level claims (§§2.2, 2.4, 2.7, 3, 4, 5) are not machine-checked.
