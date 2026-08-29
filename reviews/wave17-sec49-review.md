# Wave 17 hostile review: §49

**Verdict: CONFIRMED-AFTER-REPAIRS**

The refutation survives the full quantifier chain.  Every grid edge is a genuine §37-retained, implication-maximal intrinsic atom; the diagonal matching is admissible for (47.16); all off-diagonal extension ratios are exactly one in the same `T_0=1` space; and the rare full-grid class gives a direct super-base lower bound for the ordinary factorial moment of `H^†`.  The repairs make the moment quantifier explicit, expose the prime-supply constant, and narrow the no-escape language to the two formulations actually refuted.

## 1. Quantifier match — REPAIRED

Section 47.4's exact repaired hierarchy is:

> There should be fixed `C,D>0` such that, for every large `X`, every compatible
> `S⊂A*` with `1≤|S|<m`, where `m` is an even integer in
> `[DΛ,DΛ+2]`,
> $$
> \sum_{B\in\mathcal A^*\setminus S\atop
>       B\sim S,\ (M_B,Q_S)>1}w_B\Gamma_S(B)\le C\Lambda.\tag{47.16}
> $$

Here `Λ=L^3/log L`, `Q_S` is the selected-modulus lcm, `w_B` is the probability conditional on `T_0=1`, and `Γ_S(B)` is the exact shared-coordinate collapse.  `A*` is §47's notation for the implication antichain called `A^†` in §49.

Section 37 first says “Condition on `T_0=1`,” defines `H` in that conditioned space, and then asks for fixed `C,D>0` and an even

$$m\in[D\Lambda,D\Lambda+2]$$

such that

$$\mathbb E(H)_m\le(C\Lambda)^m.\tag{37.19}$$

Thus the corresponding repaired target is exactly

$$\mathbb E((H^\dagger)_m\mid T_0=1)\le(C\Lambda)^m,$$

not an unconditional moment and not a new probability space.

The negation is complete.  For every fixed `C,D`, every sufficiently large `X`, and every admissible even `m`, §49 takes `t=m−1` and the diagonal

$$S=\{A_{ii}:1\le i\le t\}.$$

Its moduli `q_i p_i` are squarefree and pairwise coprime, the events all prescribe the same integer residue `−8`, and hence `S` is compatible.  Also `|S|=m−1<m`.  The proof works for every possible even `m` in the interval, so it defeats even an existential choice of moment order.  Theorem 49.5 was repaired to say **every** even integer explicitly.  This is marked `(wave-17 review repair)`.

The quarantine coordinate change does not alter this conclusion.  In the `m`-coordinate of §37, each class is multiplied by the compatible unit `P_z^{-1}`.  Divisibility projections, CRT compatibility, event containment, and extension ratios are invariant under this common coordinatewise dilation.

## 2. Atom membership and maximality — CONFIRMED

Take

$$M=q_i p_j,\qquad q_i\equiv3\pmod8,\quad p_j\equiv5\pmod8.$$

Then `M≡15≡7 (mod 8)`, so

$$A_M=(M+1)/4$$

is even.  Hence `D=2|A_M^2`, and Lemma 18.1 supplies the intrinsic class

$$-4D\equiv-8\pmod M.$$

This is exactly the requested Lemma-18.1 supply at `M≡7 (mod 8)`.

### §37 retention rules

The only applicable §37 operations are quarantine survival (`z`-rough modulus), intrinsic-class deduplication via the least `D`, and deletion when a composite class projects to a retained intrinsic prime class.  There is no extra composite-modulus window in §37.3: a `z`-rough intrinsic composite atom with modulus at most `X` survives unless prime-implied.

All grid primes exceed `z`, so `M` is `z`-rough.  In the hierarchy construction `M=O_D(L^6)<e^L=X`; in the moment construction `M<4z^2<X`.  Thus both grids lie in the retained modulus range.

At `q≡3 (mod 8)`,

$$
\left(\frac{-8}{q}\right)
=\left(\frac{-1}{q}\right)\left(\frac2q\right)^3
=(-1)(-1)^3=+1.
$$

Lemma 21.2 says every intrinsic unit class at the prime modulus `q` has Legendre sign `−1`.  This excludes **every** possible prime-modulus intrinsic representative in the class `−8`; it is not merely an argument against `D=2`.  Equivalently, although `(q+1)/4` is odd and `D=2` itself fails, no alternative `D=2+jq` dividing `((q+1)/4)^2` can produce the same intrinsic class, because that would contradict the sign lemma.

A prime `p≡5 (mod 8)` is `1 (mod 4)`.  Intrinsic moduli have the form `M=4A−1≡3 (mod 4)`, so the system has no prime-modulus atom at `p` at all.  Therefore no prime divisor triggers §37.3's deletion.

For canonical deduplication,

$$-4D'\equiv-8\pmod M\iff D'\equiv2\pmod M.$$

Among positive representatives, `2` is the least.  Since it divides `A_M^2`, the canonical label is exactly `δ_M(−8)=2`; deduplication cannot remove the class.

### Implication maximality

The proper divisors of the squarefree semiprime `M` are `1,q,p`.  Modulus `1` is not an intrinsic modulus.  The class `−8 mod q` is absent by the sign computation, and modulus `p` is absent because `p≡1 (mod 4)`.  Theorem 49.1 therefore leaves no proper retained container, so every `A_ij` belongs to `A^†`.  This proves maximality in the antichain, not merely membership in the unreduced family.

The argument is unchanged whether `q_i≤Y` or `q_i>Y`: `Y` determines conditioning, not prime-implied retention.  If `q_i≤Y`, `−8` is an allowed conditioned class; if `q_i>Y`, that coordinate is unconditioned.

## 3. Theorem 49.1 — CONFIRMED

For full integer cylinders,

$$E_{M,r}=\{n:n\equiv r\pmod M\}.$$

If `E_{M,r}⊆E_{m,s}`, then varying `n=r+kM` forces every multiple of `M` to vanish modulo `m`, hence `m|M`, and taking `k=0` gives `r≡s (mod m)`.  Conversely those two congruences plainly imply containment.  Thus

$$E_{M,r}\subseteq E_{m,s}\iff m\mid M\ \text{and}\ r\equiv s\pmod m.$$

Since `r≡−4δ_M(r) (mod M)`, `s≡−4δ_m(s) (mod m)`, and `4` is a unit modulo every participating odd modulus, projection is equivalent to

$$\delta_M(r)\equiv\delta_m(s)\pmod m.$$

If `M=tm` and both moduli are `3 (mod 4)`, then `t≡1 (mod 4)` and direct substitution gives

$$A_M=tA_m-(t-1)/4,$$

while projected classes give `D=D'+jm`.  The divisibility conditions `D|A_M^2`, `D'|A_m^2` and survival of both atoms are separate membership requirements, exactly as stated in (49.3).

At equal modulus, containment requires equal residue.  Deduplication makes that the same atom; distinct classes are disjoint.  The criterion is applied only to atoms surviving §37's prime deletion.  Formula (49.4) then keeps precisely the inclusion-largest events, i.e. the divisibility-minimal compatible moduli.  Finite descent through a proper divisor reaches a kept event, proving the pointwise union and void identity (49.5), including on the `T_0=1` fibre.

## 4. Theorem 49.4 residue profile — CONFIRMED

Choose `q≡3 (mod 8)` and `p≡5 (mod 8)` in

$$(3X^{1/2}/4,\ 4X^{1/2}/5).$$

Fixed-modulus PNT supplies both for every sufficiently large `X`, and

$$X/2<qp<16X/25<X.$$

They exceed the polylogarithmic `Y` and `z`.  By Check 2, the atom `E_{qp,−8}` is retained and maximal.  Set `g=M=qp`, `a=−8`.  This is a reduced residue because `M` is odd.

Since `2g>X`, an atom counted by `W_g^†` must have modulus exactly `g`; no larger multiple fits below `X`.  These atoms are unconditioned and all have weight `1/M`.  There are at most

$$F(M)\le\tau(A_M^2)=M^{o(1)}$$

of them, while the `a` bin contains at least the displayed maximal atom.  Therefore

$$
\frac{\varphi(g)W^\dagger_{g,a}}{W^\dagger_g}
\ge\frac{\varphi(M)}{F(M)}=M^{1-o(1)}.
$$

This violates every absolute-`C` version of `C/φ(g)`.  The concentration is in the implication antichain itself.  The section correctly limits this theorem: it does not rule out a profile averaged over `g`, or one restricted to a sufficiently small range of `g`.

## 5. Theorem 49.5 arithmetic — REPAIRED

### 5.1 Hierarchy half

For the diagonal matching, CRT gives

$$Q_S=\prod_{i=1}^tq_ip_i,
\qquad a_S\equiv-8\pmod{Q_S},$$

because the moduli are pairwise coprime and every selected class is the projection of the same integer `−8`.  For `i≠j`, `q_i p_j|Q_S`, and the projection of `a_S` is exactly the class of `A_ij`.  Hence

$$\bigcap_{A\in S}A\subseteq A_{ij}.$$

The numerator and denominator in (49.17) are therefore the same conditioned event.  Their ratio is exactly one.  Proposition 47.1 gives the same result locally: every exponent of the candidate already occurs at equal level in `Q_S`, so all factors in (47.5) are one.  Conditioning contributes no residual factor on an old coordinate.

With `t=m−1`, each required residue class contains

$$
\pi(B_DL^3;8,a)-\pi(z;8,a)
=\left(\frac{B_D}{12}+o(1)\right)\frac{L^3}{\log L}
$$

primes.  The subtracted count is `o(Λ)` because

$$z=L^3\log\log L/\log L=o(L^3).$$

Thus `B_D>12D` supplies at least `m−1` primes of each type for all large `L`.  This constant bookkeeping was inserted into §49 and marked `(wave-17 review repair)`.  Products are at most `B_D^2L^6<X`.  The diagonal moduli are squarefree and pairwise coprime, `|S|=m−1<m`, and

$$\mathcal L^\dagger(S)\ge t(t-1)>C\Lambda$$

because `t∼DΛ` and `Λ→∞`.

### 5.2 Moment prime supply

Now

$$t=\left\lfloor\frac{m}{2\log(2z)}\right\rfloor
\sim\frac{D L^3}{6(\log L)^2}.$$

In either class modulo eight,

$$
\pi(2z;8,a)-\pi(z;8,a)
\sim\frac{z}{4\log z}
\sim\frac{L^3\log\log L}{12(\log L)^2}.
$$

The available-prime count divided by `t` is asymptotic to `log log L/(2D)`, so it tends to infinity.  The two mod-8 classes are disjoint, and enough distinct `q_i,p_j` exist.  Every product lies in `(z^2,4z^2)`, hence is `z`-rough and far below `X`; Check 2 proves all `t^2` edges retained and maximal.

### 5.3 Conditioned forcing probability

Let

$$R=\prod_iq_ip_i,\qquad C_R=\{n\equiv-8\pmod R\}.$$

`T_0` conditions only primes `z<q≤Y`, `q≡3 (mod 4)`.  At a conditioned `q_i`, the forbidden intrinsic classes all have Legendre sign `−1`, while `−8` has sign `+1`; thus the prescribed class is allowed and `f(q_i)<q_i`.  The `p_i≡1 (mod 4)` coordinates are never in `T_0`.  Independence of prime coordinates gives exactly

$$
\Pr(C_R\mid T_0=1)
=\frac1R\prod_{q_i\le Y}\frac{q_i}{q_i-f(q_i)}
\ge\frac1R.
$$

This formula also handles the possibility that some `q_i>Y`: those coordinates simply contribute no conditioning factor.  The inequality direction is correct; conditioning away other classes increases the probability of the specified allowed class.

### 5.4 Factorial lower bound

On `C_R`, every edge event is a projection, so `H^†≥t^2`.  Also

$$R\le(2z)^{2t},\qquad 2t\log(2z)\le m.$$

Since

$$\frac{t^2}{m}\asymp\frac{m}{(\log z)^2}\to\infty,$$

we have `t^2≥2m` for large `X`.  For `u≥2m`, each of the `m` falling-factorial factors is at least `u/2`, so `(u)_m≥(u/2)^m`.  Therefore

$$
\mathbb E((H^\dagger)_m\mid T_0=1)
\ge\frac{(t^2)_m}{R}
\ge\left(\frac{t^2}{2}\right)^m(2z)^{-2t}.
$$

After division by `(CΛ)^m`, its logarithm is at least

$$m\log\frac{t^2}{2C\Lambda}-2t\log(2z).$$

The second term is at most `m`, while

$$
\frac{t^2}{\Lambda}
\gg_D\frac{\Lambda}{(\log z)^2}
\asymp\frac{L^3}{(\log L)^3}\longrightarrow\infty.
$$

Hence the logarithm tends to `+∞`.  This is a direct lower bound for the ordinary reduced factorial moment, not merely failure of the one-step proof.

## 6. First-moment and ledger claims — CONFIRMED

With conditional weights `w_A≥0`, subset inclusion immediately gives

$$\mu^\dagger\le\mu=O(\Lambda).$$

Every tail prime atom is implication-maximal: its prime modulus has no participating proper divisor.  The tail prime subsystem has mass `μ_P=Θ(L^2)` by (37.6), so

$$\Theta(L^2)=\mu_P\le\mu^\dagger\le O(\Lambda).$$

The section correctly does **not** claim `μ` or `μ^†` is `Θ(Λ)`.  Void equality preserves (37.18), while taking a subfamily can only decrease atom counts, degrees, modulus products, and coefficient-ledger upper bounds.

The stated divisor-cube deletion mass is also exact.  In Theorem 47.2 all cube primes exceed `Y`, so the weights are unconditioned.  Put `x_i=1/p_i`, `s=Σx_i`.  Odd-subset mass is

$$
\frac1{2q}\left(\prod_i(1+x_i)-\prod_i(1-x_i)\right).
$$

Subtracting the singleton mass `s/q` leaves only odd degrees at least three, hence `O(s^3/q)`.  The maximal singleton semiprimes retain mass `s/q`, so this particular reduction loses relative mass `O(s^2)=o(1)`.  Section 49.2 honestly records that no general constant-factor lower bound `μ^†≫μ` follows.

## 7. Escape and scope audit — REPAIRED

The four original checks are correct: orientation, prime-deletion survival, exact conditioned ratio one, and direct moment failure all survive review.

Additional escape routes required explicit scope language:

* **Bounded `ω(M)` does not help (47.16) or the ordinary moment:** every grid atom is a semiprime, so `ω(M)=2`.
* **A weighted or tilted count is not refuted.**  Suppressing grid weights would no longer be Proposition 37.3's ordinary hit count and needs a new pointwise minorant argument.
* **The existing conditioning does not thin a forced cross edge.**  A redesigned selector that makes grid atoms impossible could be a different construction, but it must preserve a useful exact mean and pay §37's modulus/ledger budget.  The theorem does not rule it out.
* **Blind deletion is unjustified:** removing grid events can enlarge the void, so an odd-Bonferroni polynomial for the smaller event family is not automatically below the full void indicator.  Equality would require a separate collective-redundancy proof.
* **No universal reduction no-go is proved.**  Theorem 49.1 exhausts single-cylinder containment.  It does not prove the antichain is irredundant under every possible collective union reduction.  Also, diagonal-intersection containment in a cross edge does not imply that the cross edge itself is redundant in the union.

These boundaries are now stated in Self-review 49.6 and marked `(wave-17 review repair)`.  The valid conclusion is severe but scoped: (47.16) and the ordinary `H^†` factorial moment are dead.  A different closure-aware pointwise minorant remains logically possible.

## 8. Register and supersession sweep — CONFIRMED

The refutation leaves all required entries untouched:

* `(40.19)` and therefore the unresolved part of `(37.27)` remain open;
* `(33.16)` remains open;
* `H_PF′` remains open;
* only the repaired hierarchy and ordinary reduced factorial-moment route are closed.

A sweep of every `47.16` and `(37.19)` occurrence shows the wave-17 merge already added second-level §49 pointers in §§37, 40, 42, 45, 46, and 47.  No stale line still advertises the repaired hierarchy or reduced moment as open.  The local §47 presentation of (47.16) remains as the historical proposed statement and its assessment immediately points to §49.  No extra pointer repair was needed.

The closing §49 assessment explicitly says that a different pointwise minorant proving (33.16) remains open and makes no claim against Erdős–Straus itself.

## 9. Computational block and hygiene — CONFIRMED

`verify.py (av)` was audited line by line.

* `implication_reduce` enumerates proper divisors and applies exactly Theorem 49.1's test `(d,residue mod d)`.
* Every deleted atom is checked to lie directly in a final retained maximal cylinder.  This proves union/void equivalence symbolically without allocating a full-period array.  The `D mod d` assertion independently checks the canonical-divisor form of (49.2).
* Exact `Fraction` weights reproduce the retained conditional mass share and all `W^†_{g,a}` bins; the maximum normalized profile is exactly `220` at `g=943`.
* The small hierarchy toy enumerates compatible selected sets and computes each extension as the exact ratio of conditional CRT probabilities.
* The `2×2` grid checks all four `D=2` classes are in the reduced family, merges selected moduli `15,143` to `−8 mod 2145`, and obtains ratio one for both cross moduli `39,55`, total load `2`.
* The implementation is memory-bounded: divisor enumeration and compatibility-pruned states replace full residue periods.

The full required command

```text
uv run --with sympy,numpy,scipy python verify.py
```

completed successfully.  `verify.py` was not modified and still passes `ast.parse`.  The control-byte scan of `notes.md`, `verify.py`, and the new review/report files reports zero forbidden bytes.

## Final grades

| Mandatory check | Grade |
|---|---|
| 1. Quantifiers, admissible `S`, same conditioned space | REPAIRED |
| 2. Atom membership, §37 retention, and antichain maximality | CONFIRMED |
| 3. Theorem 49.1 implication criterion | CONFIRMED |
| 4. Antichain residue-profile refutation | CONFIRMED |
| 5. Hierarchy and factorial-moment arithmetic | REPAIRED |
| 6. First-moment mass/ledger claims | CONFIRMED |
| 7. Escape and scope audit | REPAIRED |
| 8. Register and supersession pointers | CONFIRMED |
| 9. Block `(av)`, full verification, and hygiene | CONFIRMED |

**REFUTATION CONFIRMED.**  Repository disposition: **CONFIRMED-AFTER-REPAIRS**.  The repairs clarify quantifiers, constants, and scope; they do not change the semiprime-grid construction or either refutation proof.
