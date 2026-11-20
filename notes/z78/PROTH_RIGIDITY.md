## §0

Result: For bounded positive integers `P,L,K`, only finitely many `m≥1` admit a menu of at most `K` rational-function ES triples in `T=2^(Lj)` covering the whole eventual core `s=PLj` of `n=(4^m−1)2^s+1`, even with arbitrary pointwise selection; the analogous sparse claim is false, since two fixed polynomial triples cover `s=B·2^v` for infinitely many `m` whenever `3∤B`.
Label: PROVED (rel. Siegel's integral-points theorem, the Mordell–Schinzel primitive-square obstruction via ET's quotation in `EXPONENT_COVERING.md` Theorem 1.2 (not accessed directly), the finite van der Waerden theorem for menus, and the underlying `Proth15.lean` lemmas `cls_7_3`/`cls_7_5`).
Scope: Rigidity of the denominator formulas, not nonexistence of ES solutions at any integer. The sparse counterexample refutes the strongest “only finitely many `m`” menu analogue for `3∤B`; the case `3|B` is not settled here. The profinite discussion is not a determination of ET/divisor coverability. No bound on the degrees, heights or coefficient denominators of the input triples is assumed.
Review: cross-model (Claude Opus, `data/z78/xreview/REVIEW_PROTH_ALLM_OPUS.md`; F10 incorporated).
Triage: BARRIER-SCOPED.
STATUS delta: none.

# Rigidity of polynomial ES certificates on a bounded-period Proth core

## 1. A finite set of normalized shapes

**Proposition 1.** Fix integers `P≥1`, `b≥2`. Let `a>0` be rational and let `X_i(T) ∈ Q(T)` (`1≤i≤3`) give positive integral denominators for `4/(1+aT^P)` at every `T=b^j` for sufficiently large integers `j`. The threshold and all coefficients may depend on `a`. Then the `X_i` are polynomials. Put `F_i(U)=X_i(a^(−1/P)U)`, using the positive real root. The ordered triples `(F_1,F_2,F_3)` belong to a finite set depending only on `P,b`.

**Proof.** Divide a rational function into a polynomial part and a proper fraction. At integral arguments the polynomial part has bounded denominator, and the proper fraction tends to zero as the argument tends to infinity. Integrality at infinitely many such arguments forces the proper fraction to vanish there, hence identically. The ES equation likewise holds identically, by clearing denominators at infinitely many points.

Write `N=1+aT^P`. Each `X_i` is eventually positive, and indeed positive everywhere on `[0,∞)`: if there were any nonnegative root among them, to the right of the last such root all three are positive, and at least one reciprocal diverges to `+∞` on approach to the root. Their sum `4/N` stays finite. In particular `r_i=X_i(0)>0`, with `Σ 1/r_i=4`.

Order the degrees `d_1≤d_2≤d_3`. At positive infinity the slowest-decaying positive reciprocals cannot cancel, so `d_1=P`. Now `1/X_2+1/X_3=(4X_1−N)/(NX_1)` has decay of order `T^(−d_2)` and a nonzero polynomial numerator. Thus `d_2≤2P`. Similarly `1/X_3=[4X_1X_2−N(X_1+X_2)]/(NX_1X_2)` gives `d_3≤4P`. Take `B=4P`.

For any polynomial of degree at most `B`, Lagrange interpolation at `b^J,b^(J+1),…,b^(J+B)` expresses its value at zero as a sum of the sampled values with weights

`w_h = ∏_{0≤k≤B, k≠h} (−b^k)/(b^h−b^k)`.

The common scale `b^J` cancels. Taking `C` a common denominator of these weights and `J` past the integrality threshold gives `C r_i ∈ Z_{>0}`. There are only finitely many such triples: the positive integers `e_i=C r_i` satisfy `Σ 1/e_i=4/C`; after ordering them increasingly the smallest is at most `3C/4`, the next is bounded by twice the reciprocal of the positive residual after fixing the first, and the last is determined. This is the only step that needs a whole block of successive integral samples, rather than infinitely many isolated ones.

Fix one possible ordered tuple `r_i`. In the complex coefficient space of polynomials `F_i` of degree at most `B` with `F_i(0)=r_i`, impose the coefficient equations

`4F_1F_2F_3 = (1+U^P)(F_1F_2 + F_1F_3 + F_2F_3)`.

This affine algebraic set is bounded. Otherwise choose a sequence with some coefficients unbounded, with the largest coefficient modulus tending to infinity. For nonzero coefficients `c_ik` of degree `k≥1`, take `ρ=min |c_ik|^(−1/k)` for each tuple. Then `ρ→0`; after substitution `U=ρV`, every nonconstant coefficient has modulus at most one, and at least one has modulus exactly one. Pass to a subsequence with a common such index and with all rescaled coefficients convergent. The limiting polynomials `G_i` still have `G_i(0)=r_i`; at least one is nonconstant. The target has become `1`, so `Σ 1/G_i=4` identically. At infinity the nonconstant reciprocals vanish and the remaining constants contribute a proper subsum of `Σ 1/r_i=4`, impossible by positivity of the `r_i`. No positivity of the *complex* coefficients was used.

A bounded complex affine algebraic set is finite: by the constructible image theorem each coordinate projection is constructible in the affine line, hence either finite or cofinite, and a bounded projection cannot be cofinite. Take the product of the finite projections. The normalized `F_i` satisfy the displayed equations with one of finitely many allowed constant tuples; the proposition follows. ∎

## 2. The moving coefficient `a_m=4^m−1`

**Theorem 2 (bounded-period core).** Fix `P,L≥1`. For only finitely many `m≥1` are there `X_i ∈ Q(T)` such that for every sufficiently large integer `j` the three `X_i(2^(Lj))` are positive integers solving ES for `N_j=1+(4^m−1)2^(PLj)`. The same holds with `P,L` chosen separately for each `m` from bounded ranges. There is no restriction on how the triple or its threshold depends on `m`.

**Proof.** Apply Proposition 1 with `b=2^L`, `a=a_m`. Separate its finitely many normalized shapes into two cases.

1. **A degree outside `P Z`.** Fix a shape with a nonzero coefficient `c` at such a degree `k` and, if it occurs at all, a realizing index `m₀`. For every `m` realizing it, both `ca_m^(k/P)` and `ca_(m₀)^(k/P)` are nonzero rationals. Thus `(a_m/a_(m₀))^(k/P)` is rational. Taking prime valuations shows `a_m/a_(m₀)` is a rational `d`-th power, `d=P/gcd(P,k)>1`. For a prime `p|d`, write `a_(m₀)=D v₀^p` with `D` positive and `p`-th-power-free. Then `a_m=D v^p` for a positive **integer** `v`: each valuation of `a_m` is nonnegative and congruent to the corresponding valuation of `D∈Z` modulo `p`.

   For fixed `D,p` there are only finitely many such `m`. For odd `p`, the integral points `(v,2^m)` lie on `Y²=D X^p+1`, a hyperelliptic curve of genus `(p−1)/2≥1` (squarefree right side). For `p=2`, split `m=2h+r`, `r=0,1`; the integral points `(2^h,Dv)` lie on `Y²=D(4^r X^4−1)`, a squarefree quartic of genus one. Siegel's integral-points theorem applies to each of these fixed curves; the indicated points distinguish the indices in each case. This proves finiteness, not a computed cutoff.

2. **Only degrees in `P Z`.** Each original `X_i` lies in `Q[T^P]=Q[N]`, where `N=1+a_m T^P`. Write it as `H_i(N)` and take an integer `M≥2` clearing all coefficient denominators of the three `H_i`. Write `M=2^e M'` with `M'` odd. For arbitrarily large `j` (multiples of the order of `2` modulo `M'` if `M'>1`), `N_j≡4^m (mod M')` and `N_j≡1 (mod 2^e)`. The single class `R (mod M)` specified by these congruences is a unit square: use the roots `2^m` and `1` on the respective factors. Integrality at **one** sampled `N_j` in `R` implies integrality of `H_i(n)` for **every** integer `n` in `R`, by reduction of `M H_i(n)` modulo `M`. Positivity for all sufficiently large `n` follows from eventual positivity along the samples; the ES identity is a polynomial identity in `n` since substitution `n=1+a_m T^P` is injective. Indeed `M H_i(R+Mt)≡M H_i(R)≡0 mod M` coefficientwise, so `H_i(R+Mt)∈Z[t]`. This would solve the primitive square class `R` by integer polynomials. It contradicts the Mordell–Schinzel obstruction as stated in the proof of [`EXPONENT_COVERING.md`, Theorem 1.2](../../EXPONENT_COVERING.md#1-setup-and-the-compactness-criterion), specifically its assertion for **all** polynomial-solvable classes at a profinite **unit** square, not just the seven ET classes. Thus this case occurs for no `m`.

The finite union over shapes, and then over any bounded choices of `P,L`, is still finite. ∎

**Reading the quantifiers.** On a bounded-period partition of the exponents it suffices that the branch through `s=0` modulo that period uses the indicated formula on its entire eventual progression. For instance, a formula rational in `2^(s/d)` with bounded positive integral `d` on `s≡0 (mod H)` with bounded `H` restricts to the theorem with `P=d`, `L=H` by taking `s=dHj`. Rational dependence on `2^m` or on `m` in the coefficients causes no problem: fix `m` first. The other branches need not be polynomial or even specified. The theorem supplies neither a counterexample to ES nor an all-`s` construction. The next result addresses choices from a bounded menu without assuming any partition rule.

## 3. A bounded menu, with arbitrary selection

**Theorem 3.** Fix `P,L,K≥1`. Replace the single triple in Theorem 2 by at most `K` triples in `Q(T)^3`, all allowed to depend on `m`. At each sufficiently large `j`, require **some** triple to work at `T=2^(Lj)`, with no restriction on the rule selecting it. Still only finitely many `m` are possible. The bound on `K` is uniform in `m`; no bound on formula complexity or on moduli in the selection rule is needed.

**Proof.** Induct on `K`, simultaneously for all fixed `P,L`. The empty menu covers nothing. Color every sufficiently large `j` by a working triple. Set `B=4P`, `b=2^L`. By the finite van der Waerden theorem there is a window length `W=W(K,B+1)` within which every such coloring contains a monochromatic progression of length `B+1`. In disjoint successive windows choose such progressions. Some fixed triple and step `1≤t≤W` recur infinitely often (for this `m`). This triple is positive integral and solves ES at infinitely many points, so the first parts of Proposition 1 apply: it is polynomial, solves ES identically, has positive constants and degree at most `B`. On a monochromatic block with step `t`, the interpolation proof applies with ratio `b^t` and first argument `b^J`; the weights do not depend on `J`. Thus its constants and its normalized shape lie in finite sets depending only on `P,L,K`: take the union of the constant-term lists for `b^t`, `1≤t≤W`, and apply the same bounded-variety argument as before. In particular these lists are independent of *all* the menus and selection rules.

If the selected shape has a nonzero degree outside `P Z`, Theorem 2's power-class argument gives only finitely many `m` for that shape, even under this weaker sampling hypothesis. Otherwise the selected triple is `H_i(N)`. Crucially the **polynomials `H_i` themselves** now come from a fixed finite list: write the normalized `F_i(U)=G_i(U^P)` and take `H_i(n)=G_i(n−1)`. Shapes of this type that occur give `H_i∈Q[n]` since `X_i∈Q[T]` and `a_m` is rational. These `H_i` depend on the normalized shape only, not on `m`. Choose `M` clearing their coefficient denominators. Put `h=ord_(M')(2)` for the odd part `M'>1` of `M`, and `h=1` if `M'=1`. On `j=h u` with `u` sufficiently large the class of `N_j mod M` is a primitive square as in Theorem 2. The chosen triple cannot work even once there, since integrality there would make the whole class polynomial-solvable. Hence the remaining `K−1` triples cover the entire eventual subcore with `P` unchanged and `L` replaced by `Lh`. Only finitely many `h` are possible by the finite list of `H_i`. Apply induction for each of these finitely many values of `Lh`. This proves the assertion. ∎

In particular, a bounded number of rational formulas on a bounded-root-exponent zero core cannot give an infinite-`m` solution even by switching from point to point. This does **not** exclude menus of growing size, formulas genuinely requiring unbounded root exponents, or searches for divisors at each input. Arbitrarily many off-core cases are harmless to the statement if a bounded menu handles the whole eventual zero core.

## 4. Polynomial dependence on the exponent as a second variable

**Corollary 4.** In Theorem 3 one may also include triples of bivariate polynomials in `Q[J,T]`, evaluated at `(J,T)=(j,2^(Lj))`. In fact any such triple working at infinitely many samples is independent of `J`.

**Proof.** Fix `m` and such a triple `A_i(J,T)`. Any nonzero polynomial `S(J,T)=Σ q_k(J)T^k` is eventually nonzero on the samples: its highest nonzero `T`-term dominates there, since every power of `j` is beaten by `2^(Lj)`. Hence the cleared ES equation, true at infinitely many samples, holds in `Q[J,T]`. The same dominance test shows the leading `T` coefficient of each `A_i` is positive at every sufficiently large real `J`, since the sample values are positive infinitely often. Fix such a `J`: all three specialized polynomials in `T` are eventually positive, so the rightmost-root argument of Proposition 1 shows they are positive on `[0,∞)`. Their constant terms `r_i(J)=A_i(J,0)` are thus eventually positive polynomials of `J` with `Σ 1/r_i(J)=4`. Let `J→∞`. Each nonconstant polynomial has reciprocal tending to zero, so the constant reciprocals alone sum to `4`. The sum over the nonconstant reciprocals would then be zero already at each finite sufficiently large `J`, impossible unless that set is empty. Thus the three `r_i` are fixed positive constants. As `J` ranges over all sufficiently large real numbers, the normalized triples lie in the finite variety of §1 for these constants (the degree bound follows from the same positivity at `T→+∞`). Consequently every coefficient polynomial in `J` takes finitely many values there and is constant. Discard the menu members that work only finitely often and apply Theorem 3. ∎

This last argument requires *polynomial* dependence in the two variables; it makes no assertion for arbitrary quotients in `Q(J,T)`.

## 5. Sparse exponent limits and the missing square-unit obstruction

The interpolation step in Theorem 3 uses a monochromatic block of `B+1` consecutive indices `j`, so it does not apply to `j=B·2^v`. The sparse set has a different, explicit profinite limit-set description; importantly, a fixed shift does **not** recover exponent zero.

**Proposition 5.1 (PROVED, tail exponent limit set).** Fix `B≥1` and an integer shift `a`, and define

`E_{B,a} := ⋂_{V≥1} closure_{Ẑ}{B·2^v+a : v≥V}`.

Then

`E_{B,a} = {μ∈Ẑ : μ_2=a, (μ_ℓ)_{ℓ odd}=(a+B·2^ω)_{ℓ odd} for some ω∈Ẑ}`,

where `2^ω` denotes the compatible family of odd-adic unit powers obtained by continuous extension of `v↦2^v`. In particular, every `μ∈E_{B,a}` has `μ_2=a`; and `0∉E_{B,a}` for every fixed `a` and `B≥1`.

**Proof.** In `Z_2`, `2^v→0`, so the 2-component is `a`. Any point in the intersection of tail closures is the limit of a sequence `v_i→∞`; compactness gives a profinite limit `ω` of a subsequence, and the odd-adic components converge compatibly to `a+B·2^ω`. Conversely every `ω∈Ẑ` is the limit of positive integers `v_i→∞`, so its displayed image belongs to every tail closure. This proves the formula, retaining the coupling of the odd-adic components through the *same* `ω`. If `0∈E_{B,a}`, its 2-component forces `a=0`. But for any odd prime `ℓ∤B`, the ℓ-component is `B·2^ω`, a unit multiple of `B` in `Z_ℓ`, hence nonzero, contradiction. ∎

This tail intersection is not the closure of the entire sequence: the latter also contains its finite initial terms and may contain `0` when `a=−B·2^v` for some fixed index `v`.

For `k=4^q−1`, the familiar unit-square point of the full exponent family occurs at exponent `0`, but Proposition 5.1 shows that no fixed shift of `B·2^v` has that point in its tail limit set. Thus the square-unit argument at exponent zero does not prove a finite-cover obstruction for these sparse progressions. Conversely, this does **not** prove finite coverability: a different point of `E_{B,a}` could map under `μ↦k·2^μ+1` into `Sq^×`, or the limit set could meet the sterile set through nonsquare points.

**Exact finite-cover test (PROVED, rel. `EXPONENT_COVERING.md` Theorem 1.4).** For odd `k` and fixed `B,a`, set `Λ_{k;B,a}={k·2^μ+1:μ∈E_{B,a}}`, with the 2-component interpreted as `1`. A finite eventual covering of `k·2^(B·2^v+a)+1` by ET and divisor classes exists iff `Λ_{k;B,a}` avoids the sterile set `S′` of that theorem. In particular, `Λ_{k;B,a}∩Sq^×≠∅` is a sufficient obstruction to such a covering. The criterion is exact but does not decide the intersection for general `k,B,a`; no computation or ES conclusion is claimed here.

The sparse sequence has eventually periodic residues modulo every fixed integer (the odd part is controlled by powers of `2` modulo the finite exponent order, while the 2-primary part stabilizes). That fact alone supplies no uniform interpolation block in the original index `j`, nor any bound on the size of a rational-function menu. Extending Theorem 3 to sparse progressions remains open in general.

## 6. Sparse rigidity fails: two fixed polynomial triples

**Proposition 6.1 (PROVED; refutation of the strongest sparse analogue).** Fix any positive `B` with `3∤B`. For every `m≡2 (mod 3)` and every `v≥1`, let `k=4^m−1` and `n=k·2^(B·2^v)+1`. Then `n` is covered by the following menu of two fixed polynomial ES triples (independent of `B,m,v`):

- on `n≡3 (mod 7)`: `((2n+1)/7, 2n, 2n(2n+1)/7)`;
- on `n≡5 (mod 7)`: `((2n+4)/7, 2n, n(n+2)/7)`.

The coordinates are positive integers on their respective classes, and the ES identity holds identically on each class. Consequently, for every `3∤B`, infinitely many `m` admit a menu of size `2` covering the entire sparse progression `s=B·2^v` (indeed the same menu works for all such `m`). Thus the “only finitely many `m`” conclusion of Theorem 3 is false if its full eventual core is replaced by this sparse progression.

**Proof.** Since `m≡2 (mod 3)`, `4^m≡4^2≡2 (mod 7)`, so `k≡1 (mod 7)`. Since `3∤B`, `s=B2^v` is congruent to `1` or `2` modulo `3`; hence `2^s≡2` or `4 (mod 7)` and `n≡3` or `5 (mod 7)`. For `n=7r+3`, the first displayed triple is precisely `(1+2r, 6+14r, 6+26r+28r²)`, as in the underlying Lean lemma `ESProth15.cls_7_3`; for `n=7r+5`, the second is `(2+2r,10+14r,5+12r+7r²)`, as in `ESProth15.cls_7_5`. This proves the claim. Also, either residue is a quadratic nonresidue modulo 7, so these values are outside the odd-square classes mod 840; `CONJS_GEN.md` Theorem 2 independently supplies a good word there. ∎

For `3|B`, this particular modulus cannot work: `s≡0 (mod 3)`, and for `m≡0,1,2 (mod 3)` respectively, `n≡1,4,2 (mod 7)`, all quadratic residues. No alternate odd modulus giving a fixed ES menu for every such `B` is established here. This limitation does not affect the counterexample to the proposed blanket sparse rigidity statement, already given by `B=1`.
