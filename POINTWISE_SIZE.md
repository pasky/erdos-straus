# The formal-genericity obstruction as a meta-theorem, and what escapes it

Task (c), Step 1. The obstruction behind Theorem F, DEPTH3 Theorem 2,
notes Theorems 5.1/17.3 and the Elsholtz–Tao odd-square remark is stated
here as one theorem about *procedures*, and proved. Then we determine
exactly which features of a mechanism put it outside that theorem's scope.
Step 2 (mechanisms in the escaping class) is in §§7–10.

Labels: **PROVED**; **CONDITIONAL** (proved from a named hypothesis);
**EVIDENCE** (finite computation); **Assessment** (heuristic).
Erdős–Straus (ES) is not solved here, and nothing below touches it.

## 0. Results at a glance

* **Theorem M (transfer principle; PROVED, plus CONDITIONAL existence).**
  Take a deterministic procedure on input p built from:
  * ring operations;
  * floor division;
  * sign tests, including size comparisons;
  * full factorisations and divisor lists;
  * loops over the lists so produced.

  Run it *formally* at a profinite point q*, i.e. on a polynomial input,
  with every polynomial met declared to factor "generically". If this
  formal run is finite, then for every *admissible* q the actual run on
  `p=P(q)` follows it step by step. Admissible means: q lies in one
  congruence class, every polynomial met has prime value up to a fixed
  constant, and q is large. In particular the output is the formal output.
  * Under Hypothesis H for the explicit finite family met, there are
    infinitely many admissible q.
  * Under Bateman–Horn there are `≫N^{1/deg P}/(log N)^{|S|}` of them.
  * Dickson's conjecture suffices if the family is linear. Dirichlet
    (and Linnik) suffice if nothing but p is factored.
* **Corollary M1 (PROVED/CONDITIONAL).** This is the static version asked
  for in the brief. Let a predicate depend only on `p mod M` and on the
  factorisation shapes of `f_1(p),…,f_k(p)`. Then it takes its formal value
  at every admissible p.
* **Lemma CT (character trap; PROVED from notes Lemma 77.6; EVIDENCE
  p≤5000).** Let `p≡1 (4)`. In every positive solution of `4/p`, every
  denominator prime to p has a prime factor ℓ with `(ℓ/p)=−1`.
* **Theorem C (formal odd-square principle; CONDITIONAL on H).** Every
  *correct* bounded witness-producing procedure fails for infinitely many
  primes `p≡1 (24)`. Correctness matters: "output SUCCESS (1,1,1)" is
  bounded, but not correct. One fixed profinite point (DEPTH3 Lemma 1)
  serves for all procedures. The same holds for correct unbounded
  procedures whose formal run is finite at a square-mimicking point that
  is universally nondegenerate.
  *Novelty (partial; `reviews/novelty-audit-2026-10.md`).*
  * Theorem C is the procedure-level, H-conditional generalisation of known
    odd-square obstructions:
    * Elsholtz–Tao Prop 1.6 and the remark on p. 6;
    * Mordell 1969 / Schinzel 2000, square classes are not solvable by
      polynomials (as quoted in ET p. 8);
    * Yamamoto 1965;
    * Bright–Loughran Cor 1.3–1.4.
  * Its unconditional instances below are known in substance.
  * Theorem M formalises the standard generic-point / Hypothesis-H
    principle; no prior procedure-level statement was found.
* **Instances (§3).** The following are special cases:
  * Corollary 17.3.1 / Thms 5.1, 17.3 / Prop. 77.3. These are
    unconditional, from the rational point "1". With Linnik this gives
    Thm 54.1; Thm 54.3 is a genus analogue, not an instance.
  * DEPTH3 Theorem 2.
  * Theorem F, in its literal 13521-polynomial form, with the
    certificate's own congruence data. This uses the intrinsic precision
    condition (Prec); the literal match of S was verified for this
    certificate, and is not a priori.
  * The Elsholtz–Tao remark, in a precise form for procedures.
* **Scope (§4).**
  1. **Eventual-sign size comparisons of boundedly many formal quantities
     are inside the scope** (Proposition A). This covers comparisons with
     `p^θ` (more generally any Hardy-field threshold), "is there a divisor
     in `[p^θ,2p^θ]`", and the dead-denominator test of Theorem F. So
     "using the size of p" through such comparisons does *not* escape.
     Archimedean tests whose answer oscillates along every class are not
     covered. Examples are `{√p}<1/2` and other fractional-part or
     nearest-integer tests; they are E2.
  2. A correct pointwise proof of ES needs, at every square-mimicking
     point, an infinite or undefined formal run (Corollary E). This means
     one of:
     * (E1) an unbounded, p-dependent family of consulted integers;
     * (E2) primitives that are not eventually quasi-polynomial (`⌊p^θ⌋`,
       the least non-residue, orders, …), whose actual factorisations are
       then used.

     Whether fixed non-abelian Frobenius information escapes is **open**.
     A Frobenius-decorated extension is *proposed* under a
     Schinzel–Chebotarev hypothesis, but it is not proved here.
     Non-witness (Boolean) certificates are outside the scope, but
     trivially so.
  3. Quantitatively (**PROVED** modulo Chang's Cor. 11, Thms 11.2/11.2';
     notes §54 had `1/5.2` via Linnik): the multiplier mechanism
     "`W(p)≤T(p)`" fails infinitely often if `T(p)≤(5/8−ε)log p`. The
     Type-I slice mechanism "`ck_min(p)≤T(p)`" fails infinitely often if
     `T(p)≤(5/12−ε)log p`.
     **Superseded for W:** POINTWISE_OMEGA Theorem 5.1 proves
     `W(p)≥(log p)^{2−o(1)}` i.o. (modulo Thorner–Zaman), and Thm 8.5 there
     gives `ck_min≫log p·log₃p` i.o. (modulo Lau–Wu).
     These bound the *size* of the witness parameters, not the number of
     consulted objects. For window mechanisms that factor the first K
     windows, a restricted Bateman–Horn model (**Assessment**) suggests
     that formal genericity alone refutes `K(p)=o(log p/log log p)`.
* **EVIDENCE (§5).**
  * Lemma CT holds for all 15555 solutions with `p≤5000`.
  * Toy check of Theorem M/C on 331 + 323 actual admissible primes
    (`p` up to `≈2.6·10^13`). The actual output always equals the formal
    output, including the witness. At the square-mimicking point it is
    always FAIL.
  * In the same class, non-admissible primes succeed 98.5% of the time,
    always through a composite formal prime.

## 1. The transfer principle

### 1.1 Procedures

A **program** Π has integer registers and list registers, and the
following instructions.

* **(P1)** `r←c` (a constant of the program); `r←p` (the input).
* **(P2)** `r←r₁±r₂`, `r←r₁·r₂`.
* **(P3)** `(r,r')←divmod(r₁,r₂)`. This gives `r=⌊r₁/r₂⌋` and
  `r'=r₁−r₂r`; it is an error if `r₂=0`. Also `b←DIVIDES(r₁,r₂)`, the
  truth value of `r₂|r₁`.
* **(P4)** Branch on `sign(r)∈{−,0,+}`.
* **(P5)** `L←FACTOR(r)` (with `r≠0`) gives the pairs `(ℓ,v_ℓ(r))` for the
  primes `ℓ|r`, in increasing order of ℓ. `L←DIVISORS(r)` gives the
  positive divisors of `|r|`, in increasing order.
* **(P6)** List operations: empty list, append, length.
* **(P7)** `for e in L do B`, where L is not modified inside B; and
  `for i=1..c` with c constant.
* **(P8)** `halt` with a symbol from a finite alphabet and finitely many
  registers.

A **bounded program** uses only (P1)–(P8). It halts on every input, by
induction on loop nesting: every loop runs over a list fixed at entry.
Errors (divmod by 0, FACTOR(0), DIVISORS(0)) are *totalised*: they halt
with FAIL.

Derived bounded operations include:

* comparisons `r₁<r₂` and `r^b ≶ c^b p^a`;
* `r mod c`, `r₁|r₂`, gcd, valuations, primality of `r`;
* Jacobi symbols `(r/c)` for constant c;
* sorting finite lists, and membership tests.

An **extended program** may also use `while` loops, and further primitive
functions `g:Z^k→Z` (e.g. `⌊√r⌋`, the least quadratic non-residue mod r).
It is required to halt on the inputs considered.

A program is **witness-producing** if on input p it halts with `FAIL` or
with `(SUCCESS,x,y,z)`. It is **correct** if every SUCCESS output satisfies
`x,y,z≥1` and `4xyz=p(xy+yz+zx)`. Appending a bounded check makes any
witness-producing program correct, at the cost of turning bogus successes
into FAILs.

*Why witnesses.* The bounded program "halt with SUCCESS" is correct as a
Boolean predicate iff ES holds. Hence no extensional statement ("this
predicate of p is refuted") can single out bad methods. The obstruction is
a statement about procedures that produce, or certify by a bounded
computation, the solution.

### 1.2 Formal numbers and the formal run

* **Polynomials.** `𝒫` is the set of primitive irreducible `h∈Z[X]` with
  positive leading coefficient.
* **Base polynomial.** Fix `P∈𝒫`; inputs are `p=P(q)`. The main case is
  `P=24X+1`, and `P=X` gives Dirichlet-type statements.
* **Points.** A **point** is `q*=(q*_ℓ)_ℓ∈Ẑ=∏_ℓZ_ℓ`.
* **Nondegeneracy.** h is **nondegenerate at q*** if `h(q*_ℓ)≠0` for every
  ℓ, and `ℓ∤h(q*_ℓ)` for all but finitely many ℓ. Then
  `C_h:=∏_ℓℓ^{v_ℓ(h(q*_ℓ))}` is a positive integer. For a rational point
  `q*∈Z` this just says `h(q*)≠0`, and then `C_h=|h(q*)|`.
* **Universal points.** DEPTH3 Lemma 1 constructs a point `q*_univ` with
  three properties: every `h∈𝒫` is nondegenerate at it; every `q*_ℓ` is a
  unit; and `24q*_ℓ+1` is a nonzero square unit for all ℓ.

**Lemma D (formal floor; PROVED).** Let `A,B∈Q[X]`, `B≠0`, and write
`A=QB+R` with `deg R<deg B` (`R=0` if B is constant). Let D be the least
positive integer with `F:=DQ∈Z[X]`. Put `ρ:=F(q*) mod D∈{0,…,D−1}`, and let
`σ` be the eventual sign of `R/B`, with `σ:=0` when `R=0`. Define

```
⌊A/B⌋_* := (F−ρ)/D − [ρ=0 and σ<0]  ∈ Q[X].
```

Then `⌊A(q)/B(q)⌋=⌊A/B⌋_*(q)` for all large q with `F(q)≡ρ (mod D)`. In
particular this holds for all large `q≡q* (mod D)`, and also on any
congruence class satisfying (Prec) below. The remainder `A−B⌊A/B⌋_*` is
the zero polynomial iff `R=0` and `ρ=0`.

*Proof.* For such q, `F(q)≡ρ (mod D)`. Also `A(q)/B(q)=F(q)/D+ε(q)`, where
`ε=R/B` eventually has sign σ and satisfies `|ε|<1/D`. Hence
`⌊A/B⌋=(F(q)−ρ)/D+⌊ρ/D+ε⌋`.
* If `ρ≥1`, then `ρ/D+ε` lies in `((ρ−1)/D,(ρ+1)/D)⊂[0,1]` and is `<1`,
  so the last floor is 0.
* If `ρ=0`, the last floor is 0 or −1 according to σ.

The remainder is `B·(ρ/D+[…])+R`. When `R≠0` this is a nonzero polynomial,
because `deg R<deg B`. ∎

The **formal run** of Π at `(P,q*)` executes Π with registers holding
elements of `Q[X]` ("formal values") and lists of them. It starts with
`p↦P(X)` and constants `c↦c`.

* **(F2)** Ring operations are done in `Q[X]`.
* **(F3)** `divmod` uses Lemma D. A formal divisor 0 halts with FAIL.
* **(F3')** `DIVIDES(A,B)`.
  * If `B=0`, it is true iff `A=0`.
  * Otherwise write `A=QB+R` as in Lemma D, with `Q=F/D'`. It is false
    if `R≠0`. If `R=0`, it is true iff `F(q*)≡0 (mod D')`.

  This is correct for large `q≡q* (mod D')`. If `R≠0` and
  `B(q)|A(q)`, then `B(q)` divides `D'A(q)−F(q)B(q)=D'R(q)`. But
  `0<|D'R(q)|<|B(q)|` eventually, a contradiction. If `R=0`, then
  `A(q)/B(q)=F(q)/D'`, and `F(q)≡F(q*) (mod D')` on any class satisfying
  (Prec). Precision at the primes of `D'` is needed only when `R=0`.
* **(F4)** `sign` is the sign of the leading coefficient.
* **(F5)** `FACTOR(A)` (a formal `A=0` halts with FAIL):
  1. Factor `A=κ∏h^{e_h}` in `Q[X]`, with distinct `h∈𝒫` and `κ∈Q^×`.
  2. Every h must be nondegenerate at q*.
  3. Put `K_A:=κ∏C_h^{e_h}`. It is an integer, by Lemma I below.
  4. The output is the pairs `(ℓ,v_ℓ(K_A))` for `ℓ|K_A`, in increasing ℓ.
     These are followed by the **formal primes** `(h/C_h, e_h)`, in the
     eventual order of their values at large X.

  `DIVISORS(A)` (a formal `A=0` halts with FAIL) is the list of
  `d∏(h/C_h)^{j_h}` (positive `d` with `d||K_A|`,
  `0≤j_h≤e_h`), in eventual order. Distinct formal divisors are distinct
  polynomials, by unique factorisation, since the h are pairwise
  non-proportional. So the eventual order is a strict total order.
* **(F6)–(F8)** Lists, loops and output work verbatim, on formal objects.
  A `while` test is decided by (F4).
* **(F9)** An extra primitive g has **formal semantics** at the formal
  arguments `(A_1,…,A_k)` if there are `G∈Q[X]` and a modulus `M_g` with
  the following property: `g(A_1(q),…,A_k(q))=G(q)` for all large
  `q≡q* (mod M_g)`. The formal run then uses G.

The formal run is **undefined** if it executes either of:

* a FACTOR of a degenerate polynomial;
* a primitive without formal semantics.

It is **finite** if it halts. For a bounded program it is finite whenever
it is defined. At a point where every `h∈𝒫` is nondegenerate (e.g.
`q*_univ`), the formal run of a *bounded* program is always defined and
finite.

**Lemma I (integrality; PROVED).** Along a defined formal run, every
formal register A is Ẑ-integral: `A(q*_ℓ)∈Z_ℓ` for every ℓ. In each
FACTOR, `K_A∈Z`.

*Proof.* Induction along the run.

* `P(X)` and integer constants lie in `Z[X]`, and ring operations
  preserve integrality.
* **Formal floor.** It is `(F−ρ)/D−δ`. At `ℓ∤D`, `1/D` is an ℓ-unit. At
  `ℓ|D`, `F(q*)≡ρ (mod D)` in Ẑ gives `ℓ^{v_ℓ(D)}|F(q*_ℓ)−ρ`.
* **Formal primes.** `h(q*_ℓ)/C_h` is an ℓ-adic unit, by the definition
  of `C_h`. Hence `v_ℓ(K_A)=v_ℓ(A(q*_ℓ))≥0` for every ℓ. Here
  `A(q*_ℓ)≠0`, because every h is nondegenerate. So `K_A∈Z`.
* **Divisors.** They are products of these, so integral.
* **(F9) outputs.** A G that is integer-valued on a congruence class
  through q* is ℓ-adically integral there, by continuity. ∎

**Data of a finite formal run.**

* `S:={P}∪{h: h occurs in some formal FACTOR or DIVISORS}`.
* `Λ` is any finite set of primes containing:
  * the primes of `C_h` for `h∈S`;
  * the primes of every D in (F3), of every `D'` in (F3') with `R=0`, and
    of every `M_g` in (F9).

  *Remark (C3).* Every prime `ℓ∉Λ` with `ℓ≤Σ_{h∈S}deg h` has a residue
  class mod ℓ that is a root of no `h∈S`. This is **automatic** at a
  point: `ℓ∉Λ` means `ℓ∤C_h`, so `h(q*_ℓ)` is an ℓ-unit for every
  `h∈S`, and `q*_ℓ mod ℓ` is such a class. The condition only binds when
  a congruence *class* is lifted to a profinite point, as in §3.3 and in
  FORMAL_CLOSURE.
* `E_ℓ>max_{h∈S}v_ℓ(h(q*_ℓ))` and `E_ℓ≥v_ℓ(M_g)`. In addition, for every
  divmod (F3) with quotient `F/D`, and every `R=0` test (F3') with
  quotient `F/D'`, the condition (Prec) must hold:

  > **(Prec)** For every `ℓ|D`, `F mod ℓ^{v_ℓ(D)}` is constant on the ball
  > `q*_ℓ+ℓ^{E_ℓ}Z_ℓ`. A sufficient condition (not an equivalent one) is
  > `v_ℓ(F^{(j)}(q*_ℓ)/j!)+jE_ℓ≥v_ℓ(D)` for all `j≥1`.

  The condition `E_ℓ≥v_ℓ(D)` implies (Prec), but (Prec) is weaker. For
  instance, when `F/D` is a formal monomial `c∏(g/C_g)^{e_g}` (an exact
  quotient of formal integers), (Prec) already follows from
  `E_ℓ>max_g v_ℓ(g(q*_ℓ))`. Every factor `g/C_g` is then an ℓ-adic unit
  throughout the ball, constant modulo `ℓ^{E_ℓ−v_ℓ(C_g)}`. The Taylor
  condition implies (Prec), by expanding F at `q*_ℓ`. The converse fails.
  For example, take `ℓ=2`, `F=(X−a)²−2^E(X−a)` and `D=2^{2E+1}`: F is
  constant mod D on the ball, but the `j=1` term fails. Nothing below uses
  the converse.
* `M:=∏_{ℓ∈Λ}ℓ^{E_ℓ}`.

Λ may be enlarged at will, keeping q*. This only refines the congruence
class. S and the `C_h` do not change.

An integer q is **admissible** if:

1. `q≡q*_ℓ (mod ℓ^{E_ℓ})` for all `ℓ∈Λ`;
2. `r_h(q):=h(q)/C_h` is prime for every `h∈S`;
3. `q≥q_0`, a threshold that depends only on the formal run. It is
   constructed in the proof of Theorem M(a).

### 1.3 The theorem

**Theorem M (PROVED; (b)–(d) CONDITIONAL as stated).** Let Π be an
extended program whose formal run at `(P,q*)` is defined and finite, and
let `C_P=1`. Then:

**(a)** There is `q_0` with the following property. For every admissible q,
`p=P(q)` is prime and the actual run of Π on p executes the same
instructions as the formal run. Every register value is the corresponding
formal value at `X=q`, and every list is the formal list evaluated at q.
In particular the output is the formal output, evaluated at q.

**(b)** If Hypothesis H holds for `{f_h(y):=h(My+q̃)/C_h : h∈S}` (any
`q̃∈Z`, `q̃≡q*` mod M), there are infinitely many admissible q.

**(c)** If the Bateman–Horn conjecture holds for that family, then
`#{admissible q: P(q)≤N} ≫ N^{1/deg P}/(log N)^{|S|}`.

**(d)** If all `h∈S` are linear, Dickson's prime k-tuples conjecture (and
its Hardy–Littlewood form) suffices. If `S={P}` with P linear,
Dirichlet's theorem gives (b) unconditionally. Linnik's theorem (Xylouris)
gives the least prime `p≡P(q*) (mod uM)` (`u=lc P`), with
`p≪(uM)^{5.2}`. This is admissible only if it also exceeds the threshold
`q_0`. For the forced-class programs of §3.1 the formal conclusion holds
throughout the progression (no threshold), and that is how notes Thm 54.1
uses it.

*Proof.* (a) We use induction along the (finite) formal path. The
invariant is that the actual registers equal the formal registers at q.

* **Constants, p, ring operations, list operations.** Immediate.
* **Signs.** A nonzero polynomial has eventually constant sign.
* **divmod, DIVIDES.** Lemma D and (F3'). Admissibility (1) together
  with (Prec) gives `F(q)≡F(q*)` modulo D (resp. `D'`). A formal zero divisor is an actual
  zero divisor, so both runs halt with FAIL.
* **FACTOR(A).** A formal `A=0` gives an actual 0, so both runs halt
  with FAIL. Otherwise, at q, `A(q)=K_A∏_h r_h(q)^{e_h}`, and the `r_h(q)` are
  primes, by (2). Beyond a threshold, the following hold.
  * The `r_h(q)` are pairwise distinct. Distinct members of 𝒫 are
    non-proportional, so `h/C_h−g/C_g` is a nonzero polynomial.
  * Each `r_h(q)` exceeds every prime dividing the numerator or the
    denominator of `K_A`.
  * The `r_h(q)` are pairwise ordered as their eventual order says.

  Since `K_A∈Z` (Lemma I), the actual factorisation of `A(q)` is
  literally the formal one, in the same order.
* **DIVISORS.** Distinct formal divisors take distinct, eventually
  ordered values.
* **(F9) primitives.** Immediate from their definition.
* **Loops.** Same lists, so the same iterations. A `while` loop makes
  the same tests.

The formal run is finite, so finitely many thresholds occur; take
`q_0` as their maximum. Finally, `r_P(q)=p/C_P=p` is prime.

(b) This is DEPTH3 Lemma 2.

* **Integrality.** The Taylor coefficients `h^{(j)}(q̃)/j!` are integers.
  Since `C_h|M`, the coefficients of `y^j`, `j≥1`, are divisible by `C_h`.
  So is the constant term `h(q̃)`, because `v_ℓ(h(q̃))=v_ℓ(h(q*_ℓ))` for
  `ℓ∈Λ`. So `f_h∈Z[y]`.
* **Primitivity.** `f_h` is primitive. At `ℓ∈Λ` its constant term is an
  ℓ-unit. At `ℓ∉Λ`, `f_h≡C_h^{−1}h(My+q̃)` mod ℓ. This is h composed
  with an invertible affine map of `F_ℓ`, and `h≢0` mod ℓ because h is
  primitive. No condition on `lc(h)` is needed (cf. FORMAL_CLOSURE
  Prop. 2).
* **Irreducibility and sign.** `f_h` is irreducible with positive leading
  coefficient.
* **No fixed prime divisor of `∏f_h`.**
  * At `ℓ∈Λ` all values are units.
  * At `ℓ∉Λ` with `ℓ>Σdeg`, the product is a nonzero polynomial mod ℓ of
    degree `<ℓ`.
  * At `ℓ∉Λ` with `ℓ≤Σdeg`, the remark (C3) gives a residue
    `c=q*_ℓ mod ℓ` that is a root of no h. Choose y with `My+q̃≡c`.

Every H-solution y with large `My+q̃` gives an admissible q.

(c) The Bateman–Horn count of `y≤Y` is `≫Y/(log Y)^{|S|}`.

(d) Clear. For `S={P}`, note that `gcd(uM,P(q̃))=1`. ∎

**Corollary M1 (static shape predicates; PROVED, (b)–(d) as in M).** Fix
the following data:

* nonzero `f_1,…,f_k∈Z[X]` and integers `M_0,m≥1`;
* `shape_m(n):=(sign n, the multiset {(v_ℓ(n), ℓ mod m) : ℓ|n})`;
* an *arbitrary* function Φ;
* the predicate
  `𝒮(p):=Φ(p mod M_0, shape_m(f_1(p)),…,shape_m(f_k(p)))`.

Let q* be nondegenerate for P and for every irreducible factor of every
`f_i∘P`, with `C_P=1`. Then there is a formal value `𝒮*`, computed from the
formal factorisations and `q*`, with `𝒮(P(q))=𝒮*` for every admissible q.
Here we take:

* `S` = {P} ∪ the irreducible factors of the `f_i∘P`;
* `Λ` additionally containing the primes of `mM_0`;
* `E_ℓ≥v_ℓ(m)+v_ℓ(C_h)+1` and `E_ℓ≥v_ℓ(M_0)`. The latter fixes `p mod M_0`,
  which is a separate requirement.

In particular, if `𝒮*` is "fail", then under H (or under Dickson, if every
`f_i∘P` splits into linear factors) 𝒮 fails for infinitely many primes.

*Proof.* At admissible q the factorisation of `f_i(p)` is the formal one,
by the FACTOR step of Theorem M. Each `r_h(q) mod m` equals `h(q)/C_h mod m`.
This is fixed by `q mod mC_h·∏ℓ^{…}`, i.e. by (1). The constants' residues
are fixed. Φ need not be computable. ∎

The static form does **not** capture DEPTH3 or Theorem F. There, *which*
integers get factored depends on earlier factorisations. Only the
adaptive form (Theorem M) covers them. A posteriori, along admissible q,
the adaptive procedure's choices are frozen into a static list.

## 2. The character trap and the formal odd-square principle

**Lemma CT (PROVED).** Let `p≡1 (mod 4)` be prime, and let `(x₁,x₂,x₃)` be
a positive solution of `4/p=Σ1/x_i`.

* **(a)** Every `x_i` with `p∤x_i` has a prime factor ℓ with `(ℓ/p)=−1`.
* **(b)** If exactly one `x_i` is divisible by p, then `x_i/p` has such a
  prime factor.
* **(c)** If exactly two are divisible by p, the product of their
  cofactors `x_ix_j/p²` has such a prime factor. In (c) this cannot be
  sharpened to each cofactor separately: 1574 of the 4899 Type II
  solutions with `p≤5000` have a cofactor without one.

*Proof.* By notes Lemma 1.3, p divides one or two denominators. By notes
Thm 17.1 every solution has the following form, with `gcd(a,b)=1` and
`p∤abck`:

* Type II: `(abc, pack, pbck)`;
* Type I: `(ack, bck, pabc)`.

Notes Lemma 77.6 (proved there and machine-checked) gives:

* in Type II, `(ab/p)=−1`;
* in Type I, `(c/p)=−1` and `(ab/p)=−1`.

A positive integer with Jacobi symbol −1 has a prime factor with symbol −1.
Now:

* `ab` divides the p-free `abc` (Type II), and also the cofactor `abc`
  (Type I).
* `c` divides both p-free entries `ack`, `bck` (Type I).
* `ab` divides `ack·bck` (Type II). ∎

This is the prime-side reading of the one quadratic bit: Yamamoto, and
Bright–Loughran Thm 1.2/Cor 1.3, which is (2a) of SIGNED_REFACTOR. At an
odd square `n=m²`, every `ℓ∤m` has `(ℓ/n)=+1`. That is why ET Prop 1.6
(no Type I/II solutions for odd squares) is the same computation.

**Definition.** A point q* is **square-mimicking** for P if, for every
prime ℓ, `P(q*_ℓ)` is a square of a unit of `Z_ℓ`. For ℓ=2 this means
`P(q*_2)≡1 (mod 8)`. Then `C_P=1`. Two examples:

* `q*_univ` for `P=24X+1`;
* the rational point `q*=1` for `P=X`, since `1=1²`.

**Theorem C (formal odd-square principle).** Let `P=uX+v∈𝒫` be linear, and
let q* be square-mimicking for P and nondegenerate for every `h∈𝒫` (e.g.
`q*_univ`). Let Π be a correct witness-producing extended program whose
formal run at `(P,q*)` is defined and finite. Then there are explicit
finite `S'⊇S` and `Λ'⊇Λ` with the following property (PROVED): **every
`(S',Λ')`-admissible q has `Π(P(q))=FAIL`.** Under H for the family of
`S'` there are infinitely many such q; under Bateman–Horn there are
`≫N/(log N)^{|S'|}` with `P(q)≤N` (CONDITIONAL). In particular:

> **Corollary C1.** Assume H for one explicit finite family depending on
> Π. Then every correct **bounded** witness-producing program fails for
> infinitely many primes `p≡1 (mod 24)`. (At `q*_univ` the formal run of a
> bounded program is automatically defined and finite; see §1.2.)

*Proof.* Let Π' be Π followed, on a SUCCESS output, by `FACTOR(x)`,
`FACTOR(y)`, `FACTOR(z)`. Its formal run is defined and finite: q* is
nondegenerate for all of 𝒫, and the appended steps are bounded.

*Degenerate outputs.* Suppose some formal output denominator is not
eventually positive. Then at every admissible q beyond the thresholds the
output is not a positive solution, contradicting correctness. So there
are no such q, and the claim holds vacuously. Assume from now on that all
three are eventually positive.

Let `S'` be the polynomial set of Π'. Let Λ' be its Λ, enlarged by:

* 2, with `E_2≥3`, and 3 (so that `p≡P(q*_3)≡1 (mod 3)` as well);
* the primes of u;
* the primes of every constant `K_A`;
* for every `h∈S'∖{P}`, the primes of the nonzero integer
  `H_h:=u^{deg h}h(−v/u)`.

`H_h≠0`, because `h(−v/u)=0` would force `P|h`, i.e. `h=P`. Let q be
`(S',Λ')`-admissible. Π' follows Π, so `Π(p)` is the formal output of Π.
Suppose it is SUCCESS. Let `x_i` be a p-free denominator of the output; it
exists by notes Lemma 1.3. By Theorem M(a), its prime factors are of two
kinds:

* primes `ℓ∈Λ'` (the primes of its constant `K`);
* formal primes `r_h(q)` with `h≠P`, because `r_P(q)=p∤x_i`.

**Characters of ℓ∈Λ'.** For odd `ℓ∈Λ'`:
`(ℓ/p)=(p/ℓ)=(P(q*_ℓ) mod ℓ / ℓ)=+1`, because `p≡P(q*_ℓ) (mod ℓ)` is a
nonzero square. For ℓ=2: `(2/p)=+1`, as `p≡1 (8)`. Also `(−1/p)=+1`.

**Characters of formal primes.** `uq≡−v (mod p)` gives
`u^{deg h}h(q)≡H_h (mod p)`. Here `p∤H_h`, since `p=r_P(q)∉Λ'`. So
`(r_h/p)=(H_h/p)(u/p)^{−deg h}(C_h/p)=+1`, because every prime involved
lies in Λ'.

So every prime factor of `x_i` is a residue mod p, contradicting
Lemma CT(a). Hence the formal output is FAIL, or no admissible q exists
beyond the thresholds. Either way, every admissible q gives FAIL. The
counting statements are Theorem M(b)–(c) for `S'`. Admissible q have
`p≡P(q*_2)≡1 (8)` and `p≡P(q*_3)≡1 (3)`, so `p≡1 (24)`. ∎

**Remarks.**

1. **What "looks like a square" means, precisely.** At admissible q,
   every prime other than p itself that the procedure sees inside a
   factored value is a quadratic residue mod p, just
   as every `ℓ∤m` is a residue mod `m²`. The congruence and factorisation
   data of p are those of a "formal odd square". Lemma CT is the only
   input about ES, and it is the one quadratic bit (notes §10.2).
2. **Linearity of P** is used only in computing `(r_h/p)`. For `deg P≥2`,
   Theorem M still applies, but a FAIL output must be certified another
   way, e.g. directly as in Theorem F.
3. **Weak genericity.** Primality of `r_h(q)` is more than the control
   flow needs. If a value is only divided into or compared, Λ-freeness
   suffices. This is FORMAL_CLOSURE §2.3 (13521→6402 prime conditions),
   and it is the sibling project's current direction: replacing the 159
   prime conditions of its packet by checkable divisor conditions.
   Theorem C needs only the character conclusion "every prime factor of
   every factored value is a residue mod p", plus exact control flow.

## 3. The known obstructions as instances

**3.1 Congruence identities: notes Thm 5.1, Lemma 5.2, Thm 17.3,
Cor 17.3.1, Prop 77.3 (unconditional).** Let 𝔉 be a finite list of forced
classes `r_j mod M_j`, of any shape in Thm 17.3(a)–(e) or Lemma 5.2, each
with its identity. The program `Π_𝔉` tests `p mod M_j=r_j` and, if so,
outputs the identity's denominators, computed by divmod by constants. It
is bounded and never factors anything.

Run it formally at `P=X`, `q*=1`. Then `S={X}`, and the formal tests read
`1≡r_j (mod M_j)`, all false by those theorems (Prop. 77.3: such a class
would solve `4/1`). So the formal output is FAIL. Theorem M(d) gives
infinitely many primes `p≡1 (mod lcm M_j)` with `Π_𝔉(p)=FAIL`; this is
Cor 17.3.1.

The program "all multiplier moduli ≤T" consists of the congruence tests
`p mod M∈𝓡(M)`, `M≤T` (notes (58.3)). With Linnik's bound in M(d) it
gives notes Thm 54.1 verbatim, including `W(p)>log p/(5.2+o(1))`
infinitely often. Notes Thm 54.3 (Type-I slices `ck≤T`) is the analogous
unconditional statement. There the slices are not congruence classes, and
genus theory at an actual prime `p≡1 (mod R(T))` plays the role of
Lemma CT: the needed quadratic characters `χ_s`, `s≤T` squarefree, are
`+1` at p. In this language it is the character-trap argument at a
rational square point, with the needed characters forced by the
congruence instead of by H.

The class of one is a *rational* square-mimicking point. That is why no
factorisation hypothesis is needed. At `q*_univ`, Theorem C reproves that
`Π_𝔉` fails infinitely often, but only under H for the factors of the
identity denominators. Schinzel's general theorem says that no polynomial identity
covers a square class (cited via EST p. 8, refs [44], [68]). It is the
*unconditional* counterpart of Theorem C for programs with no FACTOR
instructions. Theorem C does not reprove it unconditionally.

**3.2 DEPTH3 Theorem 2.** `BFS_k` is breadth-first search from the seed
for k rounds; it outputs the first all-positive vertex. It is a correct,
bounded, witness-producing program.

* **Fibres.** The fibre of z is computed by FACTOR of `4z−p` and `pz`
  (giving the reduced `r/s`), then DIVISORS of `s²` with both signs, a
  divmod test `r|D+s`, and the two quotients.
* **Deduplication.** Done by equality tests against a visited list that is
  never modified inside its own scan loop.

Theorem C at `q*_univ` says: under H, infinitely many `p=24q+1` have
`BFS_k(p)=FAIL`, i.e. `dist(p)>k`. Put X into S if q itself is to be
prime. The proof in DEPTH3 is this proof: its "enlarge Λ by the primes of
`H_g`" is our Λ'. Its vertex-wise use of (2a) is Lemma CT(a)/(c).

**3.3 Theorem F (FORMAL_CLOSURE).** `BFS_∞` means "repeat rounds until
no new vertex appears".

* **Dead denominators.** A p-free denominator that is `<0` or `>2t` gets a
  singleton fibre (SR §5, WINDMILL Thm 7).
* **Fibres.** Every other fibre is computed by FACTOR of `4z−p` and `pz`
  (giving the reduced `r/s`), DIVISORS of `s²`, then `DIVIDES(D+s,r)` and
  `DIVIDES(s²/D+s,r)`, then the exact quotients.

This is an *extended* program (it has a while-loop). On every input it
computes the seed component exactly, and reports a positive vertex if
there is one. Its formal run at the certificate's point is the closure
computation:

| FORMAL_CLOSURE | here |
|---|---|
| (C1) closure stabilises (7883 vertices, 9 rounds) | formal run of `BFS_∞` is finite |
| (A) robust rejection when `g^β∤D+s` in `Q[X]` | (F3') with `R≠0`: false, no precision needed |
| (B) `c_r|(D+s)(q)`; (C2) every prime of every `c_r` is in Λ, with `E_ℓ≥v_ℓ(c_r)+v_ℓ(den)` | (F3') with `R=0`; (Prec) holds under (C2), see below |
| aux factors of `4Z−P` in S | S ⊇ all FACTORed polynomials (literal form) |
| (C3) no fixed prime divisor | remark (C3) of §1.2; needed here because a class is lifted |
| (C4) every vertex has a negative entry | formal output FAIL |
| (C5) seed, `C_X=C_P=1` | start of the run, `C_P=1` |
| dead test `Z>12X` etc. | (F4) comparisons |

The certificate's point is a class `q0 mod M`. Lift it to `q*∈Ẑ` by
choosing, for `ℓ∉Λ`, `q*_ℓ` off the roots of S mod ℓ. This is possible
by (C3) for `ℓ≤Σdeg`, and trivially for larger ℓ. The `C_g` are
unchanged.

**Precision (corrected after the Step-1 review, D1).** An earlier draft
said the certificate's Λ and `E_ℓ` "serve as the data of §1.2", with
§1.2 then demanding `E_ℓ≥v_ℓ(D)` for every divmod denominator. That was
false as stated. Every non-seed vertex entry is produced by an exact
divmod whose denominator can exceed the certificate's precision. The
reviewer found one entry with `v_2(den)=20` against `E_2=14`, and an
excess of 1 at `ℓ=233`. With the intrinsic condition (Prec) of §1.2, the
certificate's data do serve:

* **Monomial quotients.** The divmods of `BFS_∞` other than the `R=0`
  tests are `s²/D`, the exact quotients y and w, and the reduction
  `(4Z−P)/gcd`. All are formal monomials, so (Prec) follows from
  `E_ℓ>max_g v_ℓ(g(q*_ℓ))`.
* **The `R=0` tests.** For `DIVIDES(D+s,r)` the quotient is
  `Q=k∏C_h^β/c_r`, with `k=(D+s)/∏h^β`.
  * At `ℓ|c_r`, Gauss's lemma gives `den(k)=den(D+s)`. Hence
    `Q(x)−Q(q*)∈ℓ^{E_ℓ−v_ℓ(den)−v_ℓ(c_r)}Z_ℓ` on the ball, which is
    integral exactly under FORMAL_CLOSURE's (C2),
    `E_ℓ≥v_ℓ(c_r)+v_ℓ(den(D+s))`.
  * At `ℓ∤c_r`, D and s are formal monomials, and r is `c_r` times a
    unit on the ball, so (Prec) is automatic.

Hence the H-family of Theorem M(b) is FORMAL_CLOSURE's
`{g(My+q0)/C_g}` with the certificate's own modulus. (The reviewer
re-derived this argument; see
`side-agent/review-pointwise-size:reviews/pointwise-size-step1-review.md`,
D1.)

**The literal S.** The polynomial set of `BFS_∞` is {P} together with the
factors of `4z−p` and of `pz` over the *non-dead* z. Polynomials that
occur only in dead entries are never factored. So the match with
FORMAL_CLOSURE's 13521 polynomials is not automatic. It holds for this
certificate, as the reviewer verified: none of the 6402 entry polynomials
occurs only in dead entries, so `|S|=6402+7119=13521`.

Two qualifications.

* **Correspondence of the tests.** The FORMAL_CLOSURE engine organises
  (A)/(B) slightly differently: it pins the constant of D numerically
  modulo `L'`. We have checked the correspondence of the tests on paper,
  not by re-running their verifier against this formulation.
* **Polynomial count.** The literal form needs all 13521 FACTORed
  polynomials prime; for this certificate that is exactly
  FORMAL_CLOSURE's literal family (see above). The 6402 refinement is
  Remark 3.

The "accidental-prime gap" of FORMAL_CLOSURE is exactly an attempt to use
(F3') with `R=0` without the primes of `D'` in Λ. Theorem C is *not* what
proves FAIL here: the certificate's point is not square-mimicking at every
r-prime. FAIL is certified directly by (C4).

**3.4 The Elsholtz–Tao odd-square remark** (EST printed p. 6, right after
Prop 1.6; DEPTH3 cites it as "p. 5":
"one can only use methods that must necessarily fail when p is replaced by
an odd square … rules out … covering congruence strategies, or the circle
method").

* EST Prop 1.6 is the statement at *actual* squares.
* Lemma CT is the same computation at primes.
* Theorem C is the precise H-conditional form of the remark *for
  procedures*: a bounded witness-producing method cannot distinguish p
  from a square, because at admissible p it sees only data that a square
  would show.
* Covering congruences are §3.1.

The circle method is **not** a bounded procedure. It averages over
p-dependent ranges (feature E1 below). ET's remark about it concerns main
terms, which is an analytic sense not covered by Theorem M. The campaign's
`W(m²)=+∞` (notes Thm 58.1) is the actual-square instance for the full
harvested witness system.

## 4. Scope: what escapes

### 4.1 Size comparisons of formal quantities are inside the scope

**Proposition A (PROVED).** Let `A∈Q[X]`, `c>0` and `θ≥0` be real. Then
`sign(A(q)−c·P(q)^θ)` is eventually constant. Hence an instruction
"compare r with `c·p^θ`" has formal semantics. Theorems M and C hold for
programs using it.

*Proof.* Put `f(t)=A(t)−cP(t)^θ`; it is continuous for large real t.

* If `θ∉Q`, the exponent `θ·deg P` is irrational, while `deg A` is an
  integer, so the larger of the two leading terms dominates.
* If `θ=a/b`, we may assume `A(t)>0` eventually (otherwise `f<0`). Then
  `f(t)=0` iff `A(t)^b=c^bP(t)^a`. This is either an identity (then
  `f≡0`) or has finitely many roots. ∎

Consequently all of the following are bounded-type:

* "is the divisor d at most `√p`";
* "does `x²` have a divisor in `[p^θ,2p^θ]`", for x a formal (factored)
  quantity;
* "is this window within `p^θ` of `p/4`";
* the dead-denominator test of Theorem F.

The same proof works for any threshold in a Hardy field. Examples are
`p^θ(log p)^k`, `r_1^{θ_1}` against `c·r_2^{θ_2}`, and `log p`: what
matters is that the sign of the difference is eventually constant.
Proposition A covers **only** such eventual-sign comparisons.
Archimedean tests whose outcome oscillates along every congruence class
are not inside the scope. Examples are fractional-part or nearest-integer
tests such as `{√p}<1/2` or "`⌊p^θ⌋` is even"; they belong to E2
(below), since they implicitly use the non-formal integer `⌊p^θ⌋`.

At admissible p, the eventual-sign tests return the formal answer.
**"Use the size of p" (STATUS.md) is therefore not an escape by itself,
as far as eventual-sign comparisons go.** Size can help only
by making the set of consulted integers p-dependent and unbounded (E1), or
by producing non-polynomial integers such as `⌊p^θ⌋` (E2).

### 4.2 The escape criterion

Call Π **formally refuted** if its formal run at some point q* (with
`C_P=1`) is defined, finite and outputs FAIL. Under H, a formally refuted
program fails for infinitely many primes (Theorem M). Π **escapes** if it
is not formally refuted at any point.

**Corollary E (CONDITIONAL on H).** Let `P=24X+1` (or any linear `P∈𝒫`,
with the residue condition then read as `p≡P(q*)`). Suppose a correct
witness-producing extended program succeeds for all large primes
`p≡1 (24)`. Then its formal run at every square-mimicking, universally
nondegenerate point for P is undefined or infinite.

*Proof.* Otherwise Theorem C gives infinitely many failures. ∎

So a pointwise ES mechanism must have at least one of the following
features. They are listed with the brief's (i)–(iv).

* **(E1) Unbounded search** (brief (i); also (ii) when the interval grows).
  A loop or `while` whose formal iteration count is infinite: ranges of
  p-dependent length (`a≤p^θ`, windows `x∈(p/4,p/4+H(p)]` with
  `H(p)→∞`), or "iterate until success". *Example.* The full ES search
  "for `a≡3 (4)`, `a≤2⌊(p+1)/3⌋`, test window a" (notes Thm 61.4) escapes.
  Every finite truncation is bounded, and at `q*_univ` its formal output
  is FAIL. So the formal loop never terminates, and the meta-theorem
  never says anything about ES itself. Two routes give the formal FAIL.
  * *Via Theorem C* (CONDITIONAL on H). Theorem C gives FAIL at all
    admissible q, and H makes admissible q exist.
  * *Unconditionally*, modulo Schinzel's theorem (cited via EST p. 8).
    The window test verifies the identity, so a formal SUCCESS is a
    polynomial identity `4/P=Σ1/X_i`. Its `X_i` are eventually positive,
    and integer-valued on a congruence class by Lemma I. It would cover
    the class `p≡P(q*) (mod uM')`, which is a square class. Schinzel's
    theorem says no polynomial identity covers a square class.
* **(E2) Non-formal integers** (brief (iii)). Primitives without formal
  semantics (F9) produce integers whose *actual* factorisations are not
  fixed polynomials in q. Examples:
  * `⌊p^θ⌋` for `θ∉Z`. A polynomial cannot grow like `q^θ`, so there are
    no formal semantics on any class.
  * The least quadratic non-residue `n_p`, as a primitive on prime
    inputs p. Formal semantics would mean `n_p=G(q)` for all large q in a
    class `q*+M_gZ` with `P(q)` prime. At a square-mimicking point for a
    linear P this is impossible, **unconditionally**.
    * A nonconstant G is excluded, since `n_p<√p+1`.
    * Suppose `G=c` is constant (a prime). Pass to the subclass mod
      `lcm(M_g,8c)` that is compatible with q*, chosen so that
      `P(q)≡1 (8)` and `P(q)` is a nonzero square mod c (for c odd). This
      is possible because q* is square-mimicking at 2 and at c. By
      Dirichlet the subclass contains primes `p=P(q)`. For them,
      `(c/p)=(p/c)=+1` when c is odd (as `p≡1 (4)`), and `(2/p)=+1` when
      c=2 (as `p≡1 (8)`). So `n_p≠c`.

    Note that every
    solution exhibits a non-residue (Lemma CT; notes Lemma 77.6), so
    "use the least non-residue" is a natural E2 mechanism.
  * `ord_p(2)`, discrete logarithms, and primes in p-dependent
    intervals. Digit-based quantities need a separate check: e.g. the
    last digit of p is formal on a class.
  * Solutions of `4/n` (`n<p`) used as a black box, i.e. descent oracles.
    notes §77.6 closes the natural ones by a different argument.
* **(E3) Fixed non-abelian information: a proposed extension, not
  proved** (part of (iv)). Examples are "is 2 a cube mod p" and
  representation by a non-principal form (notes §9.3(b)).
  * **Why it is not covered.** A genuinely non-abelian Frobenius class is
    *not* determined by a congruence point. Splitting versus a 3-cycle in
    the splitting field of `X³−2` varies on every compatible progression.
    So a `FROB_K` instruction has no formal semantics in the sense of (F9),
    and Theorem M does not cover it as stated.
  * **What a covering model would need.**
    1. Admissibility would be decorated by prescribed Frobenius classes of
       the prime values `r_h(q)` in a fixed Galois `K/Q`.
    2. The prescription would have to be compatible. For instance, if
       `r_h(q)` divides `g(q)`, its Frobenius in the splitting field of g
       must have a fixed point.
    3. One would need a Schinzel–Chebotarev hypothesis `H_K` that supplies
       such q.
  * **What carries over.** Theorem C's character computation would carry
    over unchanged, because it uses Legendre symbols only. Notes Cor 9.3
    is an unconditional single-polynomial case of this kind (Chebotarev).

  We have not developed this model. Whether fixed non-abelian information
  escapes is therefore **open here**. The earlier draft claim "only
  p-dependent families of fields escape" is withdrawn.
* **(E4) Non-witness certificates** (rest of (iv)). Boolean predicates
  whose correctness is a theorem, such as "the number of solutions is
  positive" proved analytically, lie outside the meta-theorem. They are
  not refuted by it. Any proof of ES makes the (E1) brute-force search
  correct, so the meta-theorem excludes no *proof*. It excludes proofs
  whose witness comes from a procedure with a finite formal run.
  Exceptional-set statements are also untouched: formal-generic primes
  have density `(log N)^{−|S|}→0`, consistent with DEPTH3 Thm 3 and
  `E(N)=o(π(N))`.

### 4.3 How unbounded? Quantitative thresholds

* **(Q1) PROVED** (notes Thms 54.1/54.3, = §3.1 with Linnik; sharpened in
  §11).
  * **Multiplier moduli.** A congruence-only multiplier mechanism
    "`W(p)≤T(p)`" fails infinitely often if `T(p)≤(1/5.2−ε)log p`; the
    same holds for slices `ck≤T(p)`. §11 improves the constants to `5/8`
    (Thm 11.2) and `5/12` (Thm 11.2'), modulo Chang's Cor. 11.
  * **Conditional sharpening.** If the least prime `≡1 (mod m)` is
    `≪m^{1+ε}`, the threshold becomes `(1−ε)log p`.
  * **Beyond `(log p)^{1+ε}`.** The class of one cannot reach this range:
    `p≡1 (mod lcm(1..T))` forces `log p≥(1+o(1))T`. Escaping it is
    necessary, not sufficient. In the independent-model heuristic with
    the cubic intrinsic supply (notes Thm 18.2), the bound `W(p)≤(log p)^A`
    fails infinitely often for every A. That is a Step-2 matter, so we
    flag it and do not claim it.
* **(Q2) Assessment (restricted model; heuristic).** Consider the window
  program of §5, extended to the first K windows: Type II `a≤4K` and
  Type I `m≤4K`, both `≡3 (4)`. Its formal-generic primes require about
  `2K` linear forms `6q+(a+1)/4` (resp. `6mq+(m+1)/4`) to be prime up to
  bounded constants. Here Λ consists of the primes `≤8K` with bounded
  exponents, so `log M=O(K)`; we also ignore the stabilisation thresholds,
  which are polynomial in K for this family.
  * **Local factors.** Those at `ℓ∈Λ` contribute about `(e^γlog K)^{O(K)}`.
    Those at `ℓ>8K` contribute `e^{O(K)}`.
  * **Count.** A uniform Bateman–Horn heuristic predicts
    `N·exp{−2K log log N+O(K log log K)}` admissible `p≤N`. This is `≥1`
    when `K≲log N/log log N`.

  Lemma CT then makes the first K windows fail at all of them. So for
  this family, `K(p)=o(log p/log log p)` windows are heuristically refuted
  by formal genericity alone. This is a model calculation. It is not a
  bound for general mechanisms: the parameters `log M`, coefficient
  heights and thresholds need not be `O(K)` in general, and the number of
  FACTOR calls is not an intrinsic complexity measure. Mechanism-specific
  random models (Step 2) will typically demand more.

### 4.4 Map

| feature of the mechanism | inside Theorems M/C? | why |
|---|---|---|
| residues of p mod fixed moduli | yes | (P3); class of one, Dirichlet |
| factorisation shapes of fixed polynomials in p, adaptively chosen | yes | Theorem M |
| quadratic characters of everything met | yes, all `+1` at square-mimicking points | Theorem C |
| size comparisons of formal quantities (incl. vs `p^θ`, short intervals of formal divisors) | yes | Prop. A |
| floors, divisibility tests, gcds of formal quantities | yes | Lemma D, (F3'), FACTOR |
| fixed non-abelian Frobenius data | **open** (proposed extension under `H_K`) | E3 |
| p-dependent unbounded ranges / iterate-until-success | **no** | E1 (sizes: Q1 proved for multiplier/slice moduli; Q2 model for windows) |
| integers that are not eventually polynomial (`⌊p^θ⌋`, `n_p`, `ord_p 2`) and their factorisations | **no** | E2 |
| Boolean / counting certificates, almost-all statements | **no (silent)** | E4 |

## 5. Machine checks (EVIDENCE)

**Lemma CT.** `scripts/pointwise_size_ct_check.py 5000 1000` enumerates
every positive solution `x≤y≤z` for all 329 primes `p≡1 (4)`, `p≤5000`,
by the divisor method. Completeness is cross-checked against a naive
search for `p<1000`. Over the 15555 solutions (10656 Type I, 4899 Type
II) there are 0 violations of CT(a)–(c). In Type II, both cofactors have
a QNR factor in only 3325/4899 cases, so (c) cannot be split. Output:
`data/pointwise_size/ct_check_5000.txt`.

**Toy Theorem M/C.** `scripts/pointwise_size_toy_formal.py 20000000`
checks the bounded program "Type II windows `a∈{3,7,11}`, Type I windows
`m∈{3,7}` (notes Thm 3.1), full divisor search".

* **Formal data.** `P=24X+1`, and
  `S=P∪{2X+1,3X+1,6X+1,18X+1,21X+1}`, with `C=(1,4,1,1,2)`.
  `Λ={2,3,5,7,11}`, `M=55440`.
* **The formal run** is computed from the residues of q* alone. The formal
  divisors `c·r^j` are taken in eventual numerical order, i.e. by `(j,c)`.
  The *complete* output, including the witness triple, is evaluated at q
  and compared.
* **The actual run** on admissible q (all six forms prime, found by a
  sieve, `q<1.1·10^{12}`) is performed with sympy factorisations.

Results:

| point | `p*` square at | formal output | admissible q found | actual ≠ formal |
|---|---|---|---|---|
| `sq` (`q*=11585 mod M`) | all of Λ | FAIL | 331 | 0 |
| `nsq` (`q*=27425`, differs at 7) | not at 7 | SUCCESS (Type II, a=7, `d=4`) | 323 | 0 |

At the `sq` point there are also 3000 non-admissible primes in the same
class (p prime, the window values unconstrained). Of these, 2955 succeed.
For every success:

* the window's formal prime `r_h` is composite;
* the solution's p-free denominator has a QNR prime factor.

So success comes exactly from the non-formal factorisations, as
Theorem M/C predict.

A first version of this script had two defects, found by the self-review.
It enumerated formal divisors in a non-eventual order, and it compared
only the success flag and the window. At the `nsq` point it therefore
reported `d=2r²` while the actual run used `d=4`. Both defects are fixed,
and the counts above are from the fixed run. Output: `data/pointwise_size/toy_formal_2e7.txt`.
This tests the bookkeeping on a small family. It is not a test of H.

## 6. Consequences for Step 2 (plan, not results)

A candidate must be of type E1 or E2. Two notions of escape must be kept
apart.

* **Necessary escape (Corollary E).** The candidate's formal run is
  *undefined or infinite* at every square-mimicking, universally
  nondegenerate point. Undefinedness is the intended route for E2,
  infinitude for E1. This is what must be proved for each candidate.
* **Global escape (§4.2).** The candidate is not formally refuted at
  *any* point. This is stronger, and we will claim it only where it is
  proved.

Neither notion is sufficient for correctness. A candidate must also
survive the quantitative obstructions (Q1), the (Q2)-type model for its
own family, and a mechanism-specific random model. Natural candidates
are:

* short-interval and smooth-window statements with interval length
  `p^θ`, `θ>0`;
* Hooley-Δ / Erdős–Hall type divisor distribution of an unbounded set of
  windows, in moving residue classes;
* mechanisms seeded by the actual least non-residue.

These are to be developed after parent review.

# Step 2

Step 2 follows the plan of §6. §7 quantifies the multiplier-frame
heuristic flagged in the Step-1 report. §8 treats the window frame,
which is the main candidate. §9 covers mechanisms seeded by the least
non-residue. §10 is the summary.

## 7. The multiplier frame: `W(p)≤(log p)^A` is heuristically false for every A

Recall `W(p)=min{M≡3 (4): p≡−4D (mod M), D|((M+1)/4)²}` (notes (51.1),
(58.3)). Write `𝓡(M)` for the set of these classes. In §7, "hard" means
`p≡1 (24)`. (From §8.5 on, the Mordell-hard primes are named
explicitly, and §11 uses "hard" for Mordell-hard.)

### 7.1 What is exact, and what is not

**Proposition 7.1 ((a), (b) PROVED).** Let
`L(T)=lcm(24, all M≡3 (4) with M≤T)`.

* **(a)** For fixed T, the set `{p∤L(T) : W(p)>T}` is a union of unit
  classes modulo `L(T)`. Hence
  `#{p≤N hard : W(p)>T} ~ δ*(T)·π_h(N)` as `N→∞` (PNT in APs). Here
  `π_h(N)=#{p≤N, p≡1 (24)}`, and `δ*(T)` is the Haar measure of
  `{n∈Ẑ^× : n≡1 (24), n∉𝓡(M) mod M for all M≤T}`, normalised within the
  class `1 (24)`.
* **(b)** `δ*(T)≥1/φ_h(L(T))=e^{−(2/3+o(1))T}`. The inequality is the
  class of one (notes Thm 17.3(c)); the asymptotic is Lemma 11.1 (notes
  Lemma 66.2). Lemma 11.7 improves this to `e^{−T^{1/2+o(1)}}`.
* **(c) (Assessment, not proved.)** The independence exponent is
  `I(T):=Σ_{M≤T} −log(1−h_M)`, where `h_M` is the proportion of hard unit
  classes mod M lying in `𝓡(M)`. Since `h_M≍|𝓡(M)|/φ(M)` on average,
  notes Thm 18.2's cubic mass suggests `I(T)≍(log T)^3`. We have not
  re-proved this for the hard-class normalisation. Numerically the local
  exponent `d log I/d log log T` is 2.80 at `T=2^20` and rising.

(a) is the only rigorous link between δ* and primes, and it holds for
fixed T only. For `T=(log N)^A` with `A>1`, the modulus
`L(T)=e^{(2/3+o(1))T}` is far beyond N, and no distribution theorem
applies.

### 7.2 Measuring `δ*(T)`

`scripts/pointwise_size_wtail.py split` samples n from Haar measure on
Ẑ. It draws independent uniform unit residues mod `ℓ^k≤T` for every
prime ℓ, with `n≡1 (3)`; `n mod M` is obtained by CRT, and M runs upward.
*Multilevel splitting* (survivors are cloned with their drawn residues;
fresh primes are drawn per clone; the weights are divided) makes the
estimator unbiased. Unbiasedness is not accuracy, though: below about
`10^{−14}` the runs scatter by factors of 2–5, and at T=65535 two of four
runs return 0. Splitting clones up to `batch` copies of one particle, so
the estimator is very heavy-tailed. Its median lies below its mean, and
an average over a few runs therefore typically *underestimates* δ*.
Consequently the deepest rows (T≥32767, `−log δ*≈33–38.5`, and the ratio
0.74) are biased toward faster decay, and should be read as upper
estimates of `−log δ*`. At `T=127` and `T=511` an independent plain Monte
Carlo, by the reviewer, agrees with the split estimates
(`4.29e−3±1.0e−4` vs `4.21e−3`; `8.20e−5±5.2e−6` vs `8.24e−5`). Over nine
independent runs (`split4k_3`, `split16k_*`, `split64k_*`) the
batch-weighted means are:

| T | `δ*(T)` | `−log δ*` | `I(T)` | ratio | actual count, hard `p<10^9` (W>T) | `δ*·π_h(10^9)` |
|---|---|---|---|---|---|---|
| 7 | 0.500 | 0.69 | 0.69 | 1.00 | 3176725 | 3177213 |
| 31 | 0.0716 | 2.64 | 2.63 | 1.00 | 454772 | 454874 |
| 127 | 4.21e−3 | 5.47 | 6.17 | 0.89 | 25782 | 26752 |
| 511 | 8.24e−5 | 9.40 | 11.46 | 0.82 | 430 | 524 |
| 1023 | 6.05e−6 | 12.02 | 15.01 | 0.80 | 33 | 38 |
| 2047 | 2.73e−7 | 15.11 | 19.19 | 0.79 | 3 | 1.7 |
| 4095 | 7.06e−9 | 18.77 | 24.11 | 0.78 | 0 | 0.04 |
| 8191 | 9.5e−11 | 23.08 | 29.80 | 0.77 | | |
| 16383 | 7.0e−13 | 27.99 | 36.35 | 0.77 | | |
| 32767 | 3.2e−15 | 33.4 | 43.81 | 0.76 | | (noisy) |
| 65535 | ~2e−17 | ~38.5 | 52.24 | ~0.74 | | (two of four runs gave 0) |

The comparison with actual primes is exact: `pointwise_size_wtail.py
census` computes `W(p)` for all 6354932 hard primes `p<10^9`. It agrees
with `δ*·π_h` to within 4% for `T≤127`, and to within 18% at `T=511`.
This holds although `L(T)` exceeds `10^9` already for `T≈30`. A sample
of 200000 hard primes near `10^18` gives a tail of 6.4e−4 at T=255
(δ*: 7.2e−4) and 6.0e−5 at T=511 (8.2e−5). Actual primes thus fall
modestly short of δ* (up to 18% at T=511, both at `10^9` and at
`10^18`). We have not analysed this deficit; it is in the direction of
fewer large W.

Two observations.

* **The avoidance events are positively correlated.** We find
  `−log δ*≈0.77·I(T)`, stably for `4095≤T≤16383`, i.e. `δ*` exceeds the
  independence prediction `e^{−I}`. This is consistent with a
  class-of-one mechanism: a p that is ≡1 modulo many small primes escapes
  many moduli at once. We have not shown that this is the cause.
* **The decay is polylogarithmic in T.** The local exponent of
  `−log δ*` in `log T` rises from 2.26 (T≈127–1023) to 2.58
  (T≈8191–32767).

### 7.3 Assessment

**Heuristic RA (random avoider).** `#{p≤N hard : W(p)>T}≈δ*(T)π_h(N)`
whenever the right side is ≥1, uniformly in T. This is the step that
cannot be proved: it is Prop 7.1(a) used beyond the range of any
distribution theorem. The `10^9` census tests it in the regime
`L(T)≫N`.

**Assessment 7.2.** Under RA, the one-expected-exceedance level for hard
`p≤N` is the T with `−log δ*(T)≈log π_h(N)`. RA, as stated, does not
control larger individual outliers. Beyond `T=16383` we use
`−log δ*=0.774·I(T)`, with `I` computed exactly to `2^20` and
extrapolated by its second differences beyond that.

| N | `10^8` | `10^9` | `10^12` | `10^18` | `10^30` | `10^50` |
|---|---|---|---|---|---|---|
| predicted `max_{p≤N}W(p)` | 1.4e3 | 2.3e3 | 7.2e3 | 3.9e4 | 4.4e5 | 8.4e6 |
| as `(log N)^A`, A = | 2.49 | 2.55 | 2.67 | 2.84 | 3.07 | 3.36 |

Census check:

* For `p<10^8` the actual maximum is 2495 (`p=2031121`, an outlier that
  is ≡1 modulo `16·9·5·7·13·31`). The maxima of the later dyadic ranges
  are 391–1007 (notes §65).
* For `p<10^9`, three primes have `W>2047` and none has `W>4095`, against
  a prediction of `≈2250`.

**Consequences (Assessment).**

* **All exponents A.** Under RA, `W(p)>(log p)^A` for infinitely many p,
  for **every** A, as soon as `log(1/δ*(T))=T^{o(1)}`. This sub-power
  condition is weaker than polylogarithmic growth, and the measurements
  show polylogarithmic growth in the tested range.
* **The size of W.** Assume the two-sided relation `−log δ*(T)≍I(T)`
  (measured ratio ≈0.77) and `I(T)≍(log T)^3` (§7.1(c)). Then, under RA,
  the exceedance level is `log T_N≍(log N)^{1/3}`.
* **The frontier of notes §54 is heuristically empty.** It says that
  `H_MOD(A)` is open for `A≥1`. That frontier is real as a statement about
  what is *proved*: the class of one gives only a linear lower bound,
  `W>log p/5.2` in notes §54 and `W≥(5/8−ε)log p` by Thm 11.2. Nothing
  superlinear is proved here. *(Update: POINTWISE_OMEGA Theorem 5.1 now
  proves `W(p) ≥ (log p)^{2−o(1)}` i.o., modulo Thorner–Zaman Cor. 1.4.
  So `H_MOD(A)` is false for every `A<2`, and the open range is `A≥2`.)*
  But heuristically no fixed A works. Already at
  `10^30`, `W` should exceed `(log p)^3`.
* **The relevant multiplier statement.** It is of the form
  `W(p)≤exp(C(log p)^{1/3})`, not of polylog type. This assumes the
  two-sided relation of the previous bullet.
* **From a proved Haar input (Assessment; reviewer's remark).** Lemma 11.7
  proves `δ*(T)≥exp(−T^{1/2+o(1)})`. Combined with RA alone, and with none
  of the numerical extrapolation, this already predicts primes `p≤N`
  with `W(p)>T` as soon as `T^{1/2+o(1)}≤log π_h(N)`. That is, it predicts
  `W(p)>(log p)^{2−ε}` for infinitely many p, for every `ε>0`. The only
  unproved input here is RA.

This is consistent with the duality `aM=4D+p` (notes §60): a small M
means a window modulus `a≈p/M` close to p, where only the congruence
`p mod M` is used. Such a mechanism is congruence-only, and it pays for
it with the class-of-one correlations. The mechanisms that use actual
factorisations sit at the opposite end, with small window modulus (§8).

**What would make 7.2 rigorous.** Two inputs are missing.

*(Update: POINTWISE_OMEGA addresses both in part.*
* *Its Lemma 2.3 is input (i)'s mean value in the prime-local setting. It
  gives a global mass `T^{o(1)}`.*
* *Its Theorem 5.1 achieves the transfer (ii) for that prime-local system
  via Linnik-range PNT (Thorner–Zaman). This yields `W ≥ (log p)^{2−o(1)}`
  i.o.*
* *The polylogarithmic quarantine of (i) and the general transfer remain
  open. That is POINTWISE_OMEGA §6.2, H_MIN, and §9, H_PP; §9 is under
  review.)*

* **(i) A lower bound for unit avoiders.** One would need
  `log(1/δ*(T))≪(log T)^C`, the prime-compatible analogue of notes
  Thm 31.4, which is proved there for integer residues (`δ_X≥e^{−o(L^3)}`).
  The integer proof quarantines `n≡0` at small primes, and that is not
  available for units. Quarantining `n≡1 (mod ℓ^{e_ℓ})` instead kills
  every z-smooth modulus (class of one). But mixed moduli survive with
  the condition `D≡−A (mod m)`, `m` the smooth part. The Lovász
  local-lemma bookkeeping then needs a mean value for divisors of
  `((M+1)/4)²` in the class `−(M+1)/4 mod m`. We have not proved this.
* **(ii) Primes in the avoider set for moduli `L(T)≫N`.** This is RA, and
  it is beyond current technology.

Nothing here changes a proved statement of notes §54. It changes which
pointwise target is worth stating.

## 8. The window frame: conjecturally `a_min(p)=O(log p)`, just above the formal obstruction

### 8.1 The statistic and the reduction

For a prime `p≡1 (4)` and `q≡3 (4)`, put `x_q=(p+q)/4`, so that
`q=4x_q−p`. Write `Rat_q(x)={u/v mod q : uv|x, gcd(u,v)=1}` (notes
Thm 62.1). By notes **Lemma 77.1**, `4/p` has a solution with p-free
denominator `x_q` iff `Rat_q(x_q)∩{−1,−p}≠∅`. The target −1 gives Type II
and −p gives Type I. Define

```
a_min(p) := min{ q≡3 (mod 4) : p∤x_q, Rat_q(x_q) ∩ {−1,−p} ≠ ∅ },   x_q=(p+q)/4.
```

Lemma 77.1 needs `p∤x` and `gcd(x,q)=1`. The second always follows from
the first, since `4x−q=p` gives `gcd(x,q)=gcd(x,p)`. The code skips any window that
violates them.

**Theorem 8.1 (PROVED).** `ES(p)⟺a_min(p)<∞`. Consider, for a constant
`C>0`:

> **X_win(C).** For every prime `p≡1 (24)`, `p>10^18`, `a_min(p)≤C log p`.
> Equivalently, with `t=(p−1)/4`, some `s≤(C log p+1)/4` has coprime
> `u,v` with `uv|t+s` and `4s−1|u+v` or `4s−1|u+pv`.

Then X_win(C), for any C, implies the Erdős–Straus conjecture.

The fixed cutoff `10^18` matters. Since `a_min(p)≥3` always, X_win(C) is
false for `C<3/log(10^18+9)≈0.072`: `p=10^18+9` is a hard prime. The
eventual form is

> **X_win^∞(C).** `a_min(p)≤C log p` for all sufficiently large primes
> `p≡1 (24)`.

X_win^∞(C) implies ES only together with a verification up to its
(unknown) threshold. The concrete conjecture we put forward is
**X_win(10)**; §8.4 explains the choice.

*Proof.* The first sentence is Lemma 77.1. The window x is the p-free
denominator of the solution, and every solution has one. For the second:
* Mordell's identities settle all `p≢1 (24)`.
* The verification to `10^18` (Mihnea–Dumitru, as cited in notes §0)
  settles `p≤10^18`.
* Notes Lemma 1.1 reduces ES to primes. ∎

The window search is the "search over p-dependent ranges" of feature E1.
Its unbounded length is essential (Prop. 8.4). Its parameter is the
*small* end of the duality `aM=4D+p`: a small window modulus a means a
huge multiplier `M≈p/a`. So the actual factorisation of `x_q` is used,
not a congruence on p. This is the opposite end from §7.

### 8.2 Window reciprocity

**Lemma 8.2 (PROVED).** Let `p≡1 (8)` be prime, `q≡3 (4)` with
`0<q<3p`, and `x=(p+q)/4`. Then every prime `r|x` is prime to q, and the
Jacobi symbol satisfies `(r/q)=(r/p)`.

*Proof.* If `r|q`, then `r|4x−q=p`, so `r=p`; but `r≤x<p`.

* **r odd.** Jacobi reciprocity for `q≡3 (4)` gives
  `(r/q)=(−1/r)(q/r)=(−q/r)`. Then `(−q/r)=(p/r)`, because `r|p+q`. And
  `(p/r)=(r/p)`, because `p≡1 (4)`.
* **r=2.** Then `8|p+q`, so `q≡7 (8)` and `(2/q)=1=(2/p)`. ∎

This is the window form of the reciprocity collapse of notes Prop 8.1 /
Lemma 77.10. Combined with Lemma CT it gives:

**Corollary 8.3 (PROVED).** Let `q=4s−1` and `x=x_q`.

* **(a) F1.** If every prime factor of x is a residue mod p, the window
  fails for both targets. Then every element of `Rat_q(x)` has Jacobi
  symbol +1 mod q, while `(−1/q)=−1` and `(−p/q)=−(x/q)=−1`.
* **(b) Prime q.** Conversely, for prime q the prime factors of x
  generate a subgroup of `(Z/q)^×` containing −1 iff some prime factor of
  x is a non-residue mod p. (The group is cyclic of order `2m` with m odd;
  a subgroup contains −1 iff its order is even, iff it is not inside the
  squares.) So at a prime window, the *subgroup-level* failure is exactly
  F1, i.e. the Lemma CT obstruction. Any other failure is a failure of
  the exponent budget `|f_r|≤v_r(x)` (notes §70's F3).
* **(c) Small prime factors.** Let `n_p` be the least quadratic
  non-residue mod p. Every prime factor r of x with `r<n_p` is a residue
  mod q, by Lemma 8.2. Such factors never lift a window out of F1. (This
  is about prime factors of x; an arbitrary small prime need not be a
  residue mod q.)

### 8.3 The search length must be unbounded: escape, proved

**Proposition 8.4.**

* **(a) PROVED.** Fix `K≥3`, and let `Λ_K` be the primes `≤max(K,5)`.
  Suppose p, a prime `≡1 (24)`, satisfies:
  * p is a quadratic residue mod every prime `ℓ∈Λ_K`;
  * for every `a≡3 (4)`, `a≤K`, the value `(p+a)/4` equals `C_a r_a` with
    `r_a` prime and every prime factor of `C_a` in `Λ_K`.

  Then `a_min(p)>K`.
* **(b) CONDITIONAL on Dickson.** There are infinitely many such p. Fix a
  square-mimicking class of q modulo `M_K=∏_{ℓ∈Λ_K}ℓ^{e_ℓ}`, with enough
  precision `e_ℓ` that every `v_ℓ((p+a)/4)` is fixed on the class. On it,
  the `⌊(K+1)/4⌋+1` linear forms `24q+1` and `((6q+(a+1)/4)/C_a)` form an
  admissible tuple. Hardy–Littlewood gives `≫N/(log N)^{⌊(K+1)/4⌋+1}` such
  `p≤N`. This is Theorem C with the explicit linear family. So `a_min` is
  unbounded.

  An earlier draft required `C_a=2^i3^j`. That version is false for
  `K≥31`. If `p≡1 (5)`, then `5|x_19`, which forces `x_19=5`. If
  `p≡4 (5)`, then `x_11=5·3^j` and `x_31=5·2^i`, so `2^i−3^j=1`, which
  forces `p=49`. (Reviewer's argument.) Allowing `Λ_K`-primes in `C_a`
  repairs it.
* **(c)** Every truncation "windows `q≤K`" is a bounded program that is
  formally refuted at `q*_univ`. This is PROVED modulo Schinzel's theorem
  (cited), by the §4.2 E1 route: a formal SUCCESS of a window test is a
  polynomial identity. It also holds CONDITIONAL on H, via Theorem C. The unbounded search
  "q=3,7,11,… until success" has an infinite formal run there. The escape
  is in the necessary sense of Corollary E, and no bounded version
  survives.

*Proof of (a).* Let `x=(p+a)/4=C_a r`. Every prime of `C_a` lies in
`Λ_K` and is a residue mod p: p is a square mod odd `ℓ∈Λ_K`, and
`(2/p)=1`. So `(r/p)=(x/p)=(4x/p)=(a/p)`. Moreover
`(a/p)=∏_{ℓ|a}(p/ℓ)^{v_ℓ(a)}=+1`: this is the Jacobi symbol, and every
`ℓ|a` is `≤K`. So every prime factor of x is a residue mod p, and
Corollary 8.3(a) applies. ∎

(b) is Theorem C/M(d) with the explicit family. **EVIDENCE**
(`pointwise_size_amin.py formal K`). Every hypothesis of (a) is
re-checked for every accepted p: primality of p, the residue conditions,
and all prime factors of every window being residues mod p. There were
0 rejections on re-check.

| K | forms | modulus `M_K` | p found (sieve steps) | p range | `a_min` of the found p |
|---|---|---|---|---|---|
| 15 | 5 | 120120 | 730 (`3·10^6`) | `4.9·10^9 … 8.6·10^12` | all in [19, 43] |
| 19 | 6 | 1.9·10^8 | 161 (`10^7`) | `3·10^13 … 4.6·10^16` | all in [23, 51] |
| 23 | 7 | 1.3·10^10 | 50 (`3·10^7`) | `1.1·10^17 … 9.6·10^18` | all in [27, 39] |
| 27 | 8 | 9.4·10^10 | 4 (`3·10^7`) | `3.4·10^18 … 3.8·10^19` | all in [31, 35] |

A first version of the generator was faulty. It dropped square
conditions it could not satisfy root-free, and stripped Λ-factors from p
itself. Its K=19/21/23/31 output included non-primes and primes violating
the hypotheses. The table above is from the rebuilt, self-checking
generator.

So the formal adversary controls exactly the windows it fixes. The next
few windows succeed.

### 8.4 Random model and the threshold `log p/log log p` (Assessment)

**Marginals.**

* For a fixed window, the failure probability is of order
  `(log p)^{−1/2}`. Over shifted primes, notes Thm 70.9 proves the upper
  bound `≪N/(log N)^{3/2}`. Over integers, notes Thm 70.5 gives the
  matching scale `C_aH/√log H`. A pointwise-in-p lower bound is not
  claimed.
* The source is F1. By Corollary 8.3, F1 asks that x have no prime factor
  among the non-residues mod p, a set of primes of relative density 1/2.
* At `q=3`, failure *is* F1. Over Mordell-hard primes it is 0.60, 0.425,
  0.342, 0.288 at `p≈3·10^6, 10^12, 10^18, 10^24`. The fitted exponent in
  `log p` is 0.56.

**Correlations.**

* Windows are positively correlated through the quadratic-residue
  pattern of p, i.e. through `n_p` (Corollary 8.3(c)). In the `10^8`
  census, the per-window failure is 0.16–0.37 for `n_p≤11` but 0.68–0.73
  for `n_p≥30`.
* In the `10^8` census, the joint tail exceeds the independence product
  by a factor of 18 at 14 windows. That excess comes from the rare primes
  with large `n_p`. In random Mordell-hard samples of `10^4` primes at
  `10^12` and `10^18`, the joint tail matches the product of the marginals
  within sampling error up to 6–8 windows (`sample_windows`).
* The record `a_min(8803369)=107` has `n_p=41`: p is a residue mod every
  prime `≤37`.

**Model.** Treat the windows as independent, each failing with a common
probability `g(p)=c(log p)^{−1/2}`, so that
`P(a_min(p)>Q)≈g(p)^{(Q+1)/4}`. The common rate is calibrated as the
geometric mean of the *measured single-window marginals* for `q≤31`
(`sample_windows`, `10^4` Mordell-hard primes each). This gives
`g=0.351` at `10^12` and `0.280` at `10^18`, hence `c≈1.8`. The resulting
one-expected-exceedance levels over Mordell-hard `p≤N`, with
`π_M(N)≈π(N)/32`, are:

| N | `10^8` | `10^12` | `10^18` | `10^30` | `10^100` |
|---|---|---|---|---|---|
| predicted `max a_min` | 55 | 77 | 107 | 160 | 414 |
| `/log N` | 3.0 | 2.8 | 2.6 | 2.3 | 1.8 |

Three caveats. The model applies a fixed-window marginal law uniformly
to windows with growing `q≈log p`, which is not proved. It ignores the
rare correlated families (large `n_p`), which dominate the extreme tail
of the `10^8` census. And the constant is calibrated on two scales only.

The observed census maximum below `10^8` is 107 (`/log p=6.7`). Otherwise
the dyadic maxima are 47–63 (`/log p≈3–3.9`).

**Assessment 8.5.**

* **Upper threshold.** Under the model,
  `log P(a_min(p)>Q)=−(Q/8)(log log p)(1+o(1))`. The tail is summable over
  p as soon as `Q≥(8+ε)log p/log log p`. Hence, heuristically,
  **X_win^∞(C) holds for every fixed `C>0`**, with
  `a_min(p)≤(8+o(1))log p/log log p` eventually. The constant 8 is a
  model output, not a calibrated prediction.
* **Lower threshold.** The formal adversary (Prop. 8.4, with the (Q2)
  count) and the F1 adversary both produce, heuristically, `p≤N` with
  `a_min(p)≥c·log N/log log N`. So the window frame's true scale is
  `Θ(log p/log log p)`.
* **Margin.** `X_win(C)` sits above this scale by a factor `≍log log p`,
  and the formal-genericity obstruction sits exactly at it. (The
  multiplier frame of §7 needs `exp((log p)^{1/3})`.)
* **Data.** The ratio `a_min(p)/log p` stays below 10 for every hard
  `p<10^8`; the maximum is 6.69. It also stays below 10 in all samples at
  `10^12`, `10^18` and `10^24`, and for all class-of-one and
  formal-adversary primes tested (§8.5). This motivates the cutoff
  conjecture **X_win(10)**, which, unlike X_win^∞, directly implies ES
  (Theorem 8.1).

### 8.5 Numerical tests (EVIDENCE)

| family | primes | `max a_min` | `P(a_min>7)` | `P(a_min>23)` |
|---|---|---|---|---|
| all hard `p<10^8` (census) | 719781 | 107 | 0.0753 | 2.4e−3 |
| Mordell-hard `p<10^8` (census) | 179468 | 107 | 0.302 | 9.7e−3 |
| Mordell-hard, random `p∈[10^12,2·10^12)` | 30000 | 39 | 0.184 | 1.7e−3 |
| Mordell-hard, random `p∈[10^18,2·10^18)` | 30000 | 43 | 0.121 | 3.3e−4 |
| class of one, `p≡1 (lcm(24,1..23))`, `p≈10^15` | 2000 | 67 | 0.226 | 0.0165 |
| class of one, `p≡1 (lcm(24,1..41))`, `p≈10^23` | 1000 | 43 | 0.158 | 0.006 |
| formal adversary K=15 / 19 / 23 / 27 (§8.3) | 730 / 161 / 50 / 4 | 43 / 51 / 39 / 35 | 1 (all) | — / — / 1 / 1 |
| W-record primes (notes (65.2)) and the hard `p<10^9` with `W>2047` | 17 | 23 | — | 0 |

Large W does not force large `a_min`. These are 17 selected extreme
primes, so this is not a correlation study.

* **W-records have small windows.** The record `W(2031121)=2495` has
  `a_min=11`. There are three hard primes `p<10^9` with `W>2047`:
  2031121, 605531161 and 610747201 (`W=2495`, `3263`, `2071`), with
  `a_min=11`, 23 and 3.
  The class of one ruins small multipliers but leaves windows alone,
  because windows see the free prime factors of `x_q` (notes §77.1).
* **Type mix of the minimal window.** At the minimal window, `−1` (Type
  II) lies in `Rat_q` for 718191 of the 719781 hard primes `<10^8`. Only
  1590 have Type I only. The label is intrinsic: it is computed on the
  completed set. A first draft reported an order-dependent "first target
  found" split, which was wrong.

### 8.6 Position relative to known results and conjectures

* **Single windows: known.** The fixed-window laws are proved (notes
  §70): the failure scale, density-one success in compatible
  progressions, and the F1/F3 split.
* **Joint windows: the exceptional-set problem.** X_win needs the *joint*
  failure of `J≍log p` windows to be `o(1/p)` **for every p**. Its
  average version over p is the stacking hypothesis `H_STACK` of notes
  §71, with `J` growing. X_win is the pointwise version, far beyond sieve
  uniformity. It is the precise pointwise counterpart of the campaign's
  exceptional-set line.
* **Erdős–Hall type.** Per window, the relevant set is `Rat_q(x)`, with up
  to `3^{ω(x)}≈(log p)^{log 3}` elements. Divisors alone number
  `2^{ω(x)}`.
  * The window range `q≤C log p` lies inside the range
    `q≤(log x)^{log 3−ε}`. Heuristically, the ratio sets equidistribute
    there.
  * It lies outside the classical divisor range `q≤(log x)^{log 2−ε}`.
    The Erdős–Hall almost-all theorem for divisors in residue classes
    lives there (recalled from memory, not re-checked).
  * **A structural consequence.** Any mechanism that only uses
    equidistribution of *divisors* (e.g. notes Lemma 77.11's pigeonhole)
    at moduli `q≤(log p)^{log 2}` has only `≍(log p)^{0.69}` windows. That
    is fewer than the `≍log p/log log p` that formal genericity requires
    (§4.3(Q2), Prop. 8.4). Such a mechanism is heuristically refuted. The
    pointwise problem needs the ratio sets, up to moduli `≍log p`.
* **Jacobsthal / covering flavour.** By Corollary 8.3, X_win implies the
  following necessary statement. Among the `≍C log p/4` consecutive
  values `(p+q)/4`, at least one has a prime factor that is a
  non-residue mod p. This is a "no long runs of p-residue-smooth shifted
  values" statement. The formal adversary (all values prime up to
  residue constants) shows that it fails for runs of every fixed length
  K under Dickson. For lengths `o(log p/log log p)` it fails only under
  the (Q2)-type growing-K model.

## 9. Seeding by the least non-residue (E2)

Every solution exhibits a non-residue mod p: by Lemma CT, the p-free
denominator has a prime factor ℓ with `(ℓ/p)=−1`. Let `n_p` be the least
one. For Mordell-hard p it satisfies `n_p≥11`, since 2, 3, 5, 7 are
residues there.

**Lemma 9.1 (seeded windows; PROVED).** Let `n=n_p`, and let `q>0` with
`q≡−p (mod 4n)`. Then:

* `q≡3 (4)`;
* `n|x_q=(p+q)/4`;
* `(n/q)=−1` (Jacobi).

In particular a seeded window is never F1. For **prime** q, the subgroup
generated by the prime factors of `x_q` contains −1. Such a window can
fail only through the exponent budget (F3).

*Proof.* `4n|p+q` gives the first two claims, and `gcd(n,q)=1` because
`q≡−p (mod n)` and `n∤p`.

* **Odd n.** Jacobi reciprocity with `q≡3 (4)` gives
  `(n/q)=(−1/n)(q/n)=(−q/n)`. Then `(−q/n)=(p/n)`, since `q≡−p (mod n)`,
  and `(p/n)=(n/p)=−1`.
* **n=2.** This occurs when `p≡5 (8)`. Then `q≡−p≡3 (8)`, so
  `(2/q)=−1`.

No bound on q is needed. For prime q, `(n/q)=−1` makes the prime factor n
of `x_q` a non-square mod q. The group `(Z/q)^×` is cyclic of order 2m
with m odd, so any subgroup containing a non-square has even order and
contains −1. ∎

**Composite seeded windows keep subgroup obstructions.** Take
`p=349801`, so `n_p=23`, and the first seeded window `q=75`. Then
`x=(p+75)/4=23·3803`, and `(23/75)=−1` as promised. But both prime factors
have Jacobi symbol +1 modulo 15, while both targets −1 and −p have
symbol −1 modulo 15. So no exponent budget reaches either target: this is
a subgroup miss, not F3. (Reviewer's example.) The F3-only statement holds
for prime q only.

**The mechanism.** Use the seeded windows `q_j=q_0+4n_pj`, `j=0,1,…`,
where `q_0=(−p mod 4n_p)<4n_p`.

> **X_QNR(C).** For every prime `p≡1 (24)`, `p>10^18`, some `j<C log p`
> has `Rat_{q_j}(x_{q_j})∩{−1,−p}≠∅`.

As with X_win, the fixed cutoff makes X_QNR(C) false for very small C.
The heuristic statements below concern the eventual form X_QNR^∞(C).

* **ES ⇐ X_QNR(C)** (PROVED). The argument is that of Theorem 8.1.
* **Search range.** Under GRH, `n_p≤2(log p)^2` (Bach; cited, not
  re-checked), so the search is polylogarithmic: `q<8C(log p)^3`.
* **Escape, in the necessary sense of Corollary E.** This is
  unconditional, by §4.2's argument for `n_p`, which needs only
  Dirichlet. The window positions depend on
  `n_p`, which has no formal semantics at square-mimicking points (§4.2,
  E2). So the formal run there is undefined. This is *not* the global
  escape of §4.2, i.e. absence of formal refutation at every point; see
  the next item. The length must still grow (E1).
  * **Fixed n_p does not escape.** At a point that is square-mimicking
    except at one prime `ℓ_0`, the least non-residue is formally `ℓ_0`.
    The first J seeded windows then form a bounded formal program.
  * **Plausible refutation (Assessment, not proved).** For large enough
    windows, choosing the residues of the formal primes `x/(Cℓ_0)` can
    make every such window fail. So we expect X_QNR with *fixed* J to be
    formally refuted.

**Data** (`pointwise_size_amin.py seeded 100000000 20 1` and
`sample_seeded`). Mordell-hard primes. "Seeded J" means the first J
seeded windows all fail; "unseeded" means the first J windows `q≤4J−1`
all fail.

| p range | primes | seeded J=1 | J=2 | J=3 | J=5 | unseeded J=1 | J=2 | J=3 | J=5 |
|---|---|---|---|---|---|---|---|---|---|
| `10^5–3·10^6` (all) | 6355 | 0.071 | 0.015 | 6.5e−3 | 1.1e−3 | 0.60 | 0.38 | 0.15 | 0.049 |
| `10^5–10^8` (all) | 179195 | 0.058 | 9.1e−3 | 3.3e−3 | 6.0e−4 | — | — | — | — |
| `[10^12,2·10^12)` | 20000 | 0.042 | 3.3e−3 | 7e−4 | 1e−4 | 0.425 | 0.183 | 0.050 | 8.1e−3 |
| `[10^18,2·10^18)` | 20000 | 0.029 | 2.3e−3 | 3e−4 | 0 | 0.342 | 0.123 | 0.027 | 2.8e−3 |
| `[10^24,2·10^24)` | 5000 | 0.022 | 1.2e−3 | 2e−4 | 0 | 0.288 | 0.082 | 0.014 | 8e−4 |

Lemma 9.1 has 0 violations over all windows tested.

**Assessment 9.2.**

* **Single windows.** Seeded first-window failure decays like
  `(log p)^{−0.9}`; unseeded windows decay like `(log p)^{−0.56}`. Both
  are empirical fits over `3·10^6≤p≤10^24`.
  * For **prime** seeded windows, seeding removes F1 exactly, and the
    remaining F3 failure plausibly needs `x/n_p` to have few prime
    factors, i.e. probability `(log p)^{−1+o(1)}`. That is consistent with
    the fit.
  * **Composite** seeded windows (such as `q=75` above) can still fail at
    the subgroup level, and the data mix both kinds. We have not
    separated them. So the exponent 0.9 is not explained by a proved
    mechanism.
* **Joint windows.** With J windows the gain compounds. At `10^18`, two
  seeded windows fail together 50 times less often than two unseeded
  ones.
* **Scale.** The threshold is still `Θ(log p/log log p)` windows. If the
  per-window failure is `(log p)^{−1+o(1)}` (prime seeded windows, as
  above), the constant roughly halves. X_QNR^∞(C) is heuristically true
  for every `C>0`.
* **The price is size.** Seeded windows are sparse, with moduli
  `≈4n_pj`. The first successful seeded modulus has median 3.1×`a_min(p)`
  (1-in-50 subsample `<10^8`).
* **Caveat (not quantified).** Part of the seeded successes are
  congruence-forced. For instance, when `q_0=3` and `n_p≡2 (3)`, the
  window always succeeds; this is a Mordell-type identity in disguise.
  For Mordell-hard p, `n_p≥11` makes such forcing rarer.

**What E2 contributes.** Lemma CT and Cor. 8.3 identify the obstruction's
coordinate. Unseeded windows fail mainly when `x_q` has no prime factor
among the non-residues mod p. The least non-residue is the cheapest such
factor to plant, and it can be planted by a congruence on q that depends
on p. That is exactly what formal genericity cannot see.

E2 does not, however, give a deterministic mechanism. After seeding, the
success of a window still depends on the factorisation of `x_q/n_p`:
budget F3 for prime q, and subgroup structure modulo the prime factors of
composite q. This is the same kind of divisor-ratio event, with a better
empirical exponent.

## 10. Summary of Step 2

| frame | consulted objects | proved lower bound i.o. | heuristic true scale | pointwise hypothesis | status |
|---|---|---|---|---|---|
| multiplier `W(p)` (congruence-only, §7) | `p mod M`, `M≤T` | `W≥(5/8−ε)log p` (Thm 11.2, modulo Chang; notes Thm 54.1: `1/5.2`); superseded by `W≥(log p)^{2−o(1)}` (POINTWISE_OMEGA Thm 5.1) | `log W≍(log p)^{1/3}`; `W≈(log p)^{2.5–3.4}` for `10^8≤p≤10^50` | `W≤(log p)^A` | **heuristically false ∀A** (Assessment 7.2) |
| window `a_min(p)` (§8) | factorisations of `(p+q)/4`, `q≤Q` | unbounded under Dickson (Prop 8.4); for each found p, `a_min>K` PROVED | `Θ(log p/log log p)` (model; conjectural) | **X_win(10)** (cutoff `10^18`); eventual form X_win^∞(C) | X_win^∞(C) heuristically true ∀C>0 (Assessment 8.5); ratio `<10` on all data |
| seeded windows (§9) | factorisations of `(p+q)/4`, `q≡−p (4n_p)` | none beyond §8 | `Θ(log p/log log p)` windows (model; conjectural) | **X_QNR(C)** / X_QNR^∞(C) | X_QNR^∞(C) heuristically true ∀C>0 (Assessment 9.2) |

Answers to the brief's Step 2 items (a)–(d):

* **(a) Escape.**
  * X_win escapes the meta-theorem in the necessary sense, and every
    bounded truncation of it is formally refuted (Prop. 8.4(c), proved).
  * X_QNR escapes in the necessary sense, unconditionally (§9, via §4.2's
    `n_p` argument).
    Formal refutation of its fixed-J truncations is only plausible
    (Assessment, §9).
* **(b) Heuristics.**
  * The formal-genericity threshold `≍log p/log log p` lies below `C log p`
    (§4.3(Q2), Assessment 8.5).
  * The multiplier frame is refuted for all polylog bounds.
  * Divisor equidistribution in the Erdős–Hall range is too short
    (§8.6).
* **(c) Numerics.** The tested families are:
  * all hard and Mordell-hard primes `<10^8`;
  * random samples at `10^12`, `10^18`, `10^24`;
  * class-of-one primes (`≡1 mod lcm(1..41)`);
  * formal-adversary primes (`p=24q+1` with all shifted windows prime);
  * the W-record primes.
* **(d) Reductions.** ES ⇐ X_win(C), and ES ⇐ X_QNR(C), for any C. Both
  are PROVED (Theorem 8.1), using Lemma 77.1 and the verification to
  `10^18`.

**What was not obtained.** There is no unconditional partial result
beyond the trivial ones. Seeded and forced windows reproduce congruence
families. A positive-density set of p that is not a finite union of
classes, proved via size, was not found. X_win is the pointwise form of
the J-window stacking problem with `J≍log p`. Its average version is the
open exceptional-set input `H_STACK` (notes §71). We know no route to
its pointwise form. It is precisely Wall (i) of notes §10.6: divisors
hitting a moving coset in one of `≍log p` shifts. What Step 2 adds is:

* the conjectured scale of that search under explicit models:
  `≍log p/log log p` windows, versus `exp((log p)^{1/3})` in the
  multiplier parametrisation;
* the proved fact that no bounded window search suffices under Dickson;
* the coordinate of its obstruction: non-residue prime factors (Lemma CT,
  Cor. 8.3), with F1 versus F3 at prime windows.

# Step 3: unconditional Ω-results

## 11. What can be proved unconditionally on the Ω side

Throughout, "hard" means Mordell-hard (p in one of Mordell's six square
classes mod 840). Labels are as before. **Cited** marks external
theorems whose statements we read in the source, but whose proofs we did
not check.

### 11.1 The multiplier frame: `W(p)≥(5/8−ε)log p` infinitely often

Let `L*(T)=lcm(24, all M≡3 (mod 4) with M≤T)`.

**Lemma 11.1 (PROVED; this is notes Lemma 66.2, (66.5)–(66.6)).**
`log L*(T)=(2/3+o(1))T`. Notes §66 already introduced the odd part
`L(T)=lcm{M≤T, M≡3 (4)}` (so `L*=8L`) as the class period of the
twisted families. What is new here is its use with prime selection.

*Proof.* For an odd prime ℓ and `e≥1`, some `M≡3 (4)` with `M≤T` is
divisible by `ℓ^e` iff one of two things holds:

* `ℓ^e≡3 (4)` and `ℓ^e≤T` (take `M=ℓ^e`);
* `3ℓ^e≤T`. Then take `M=3ℓ^e` if `ℓ^e≡1 (4)`. If `ℓ^e≡3 (4)`, the
  first case already applies.

Hence every prime `ℓ≤T/3` divides `L*(T)`. A prime `ℓ∈(T/3,T]` divides it
iff `ℓ≡3 (4)`. Higher prime powers involve only primes `≤√T`. By the
prime number theorem for progressions mod 4,
`log L*(T)=θ(T/3)+θ(T;4,3)−θ(T/3;4,3)+O(√T log T)=T/3+T/3+o(T)`. ∎

Numerical values (rounded) of `log L(T)/T` for the odd part `L=L*/8`:
0.581 (T=10²), 0.660 (10³), 0.665 (10⁴), 0.6667 (10⁶), 0.6666 (10⁷).
For `L*` itself, add `log 8/T`: for example 0.602 at T=10², and 0.662
at 10³. The notes-§54 modulus `lcm(1..T)` has ratio `≈1.000`
(`pointwise_size_omega.py`).

**Theorem 11.2.**

* **(a) PROVED.** Every prime `p≡1 (mod L*(T))` has `W(p)>T`. For
  `T≥15` it is also hard (Mordell's classes).
* **(b) PROVED modulo a cited theorem** (Chang, *Short character sums for
  composite moduli*, J. Anal. Math. 123 (2014), Corollary 11: if
  `log ℓ=o(log q)` for every prime `ℓ|q`, then every reduced class mod q
  contains a prime `<q^{12/5+o(1)}`).
  The corollary is unconditional. Siegel zeros are handled inside its
  proof through Heath-Brown's Deuring–Heilbronn result [HB2, Cor. 2], so no
  Siegel caveat is needed here. Effectivity is neither claimed nor
  checked; notes Thms 54.1/54.3 are explicitly effective.
  The hypothesis is used far inside its safe range. For `q=L*(T)` (and
  likewise `R(T)`), `log P⁺(q)≈log T≍log log q`.
  Conclusion: `limsup_{p hard} W(p)/log p ≥ 5/8`. More strongly, the construction
  gives, in the notation of notes (58.2), `L_h(T)≤exp{(8/5+o(1))T}` for
  *all* large T. (The limsup statement alone would only give this along a
  subsequence; cf. notes Lemma 58.5.)
* **(c) Other least-prime inputs.**
  * Linnik's theorem with Xylouris's exponent `L=5` (dissertation 2011,
    as listed; cited, not checked) gives `3/(2·5)=0.30`. With the 5.2 of
    notes §54 it gives 0.288.
  * GRH, via Bach–Sorenson's bound on the least prime in a progression,
    `≤(1+o(1))(φ(q)log q)^2` (cited), gives `3/4`.
  * The conjecture "least prime `≡a (q)` is `≪q^{1+ε}`" gives `3/2`.
* **(d) Ceiling of the certified coefficient.** Any `p≡1 (mod L*(T))`
  satisfies `p>L*(T)`, so the threshold certified by this construction
  obeys `T/log p<3/2+o(1)`. This bounds the *certified* coefficient only.
  The actual `W(p)` can be larger; see the evidence below.

*Proof.*

* **(a).** `p≡1 (mod M)` for every eligible `M≤T`, and `1∉𝓡(M)` (notes
  Thm 17.3(c)). Hence `W(p)>T`. Moreover `8, 3, 5, 7 | L*(T)` for `T≥15`
  (`15≡3 (4)`), so `p≡1 (840)`, which is a Mordell class.
* **(b).** Every prime factor of `q=L*(T)` is `≤T=O(log q)`, so
  `log ℓ=o(log q)`. Chang's Corollary 11 gives a prime `p≡1 (mod q)` with
  `log p≤(12/5+o(1))log q=(8/5+o(1))T`. Then `W(p)>T≥(5/8−o(1))log p`,
  and `p>q→∞`.
* **(c).** Substitute the exponent.
* **(d).** Immediate. ∎

**Improvements over the notes.**

* **The coefficient.** Notes Thm 54.1 / (54.4) used `lcm(1..T)` and
  Linnik with 5.2, giving `limsup W/log p≥1/5.2≈0.192`. The gain comes
  from two independent sources:
  * only moduli `≡3 (4)` matter (a factor 3/2);
  * the certificate modulus is `O(log q)`-smooth, so Chang's 12/5 replaces
    Linnik's 5 (a factor ≈2.1).
* **The upper end.** Notes (58.18), `L_p(T)≤exp{(5.2+o(1))T}`, becomes
  `exp{(1.6+o(1))T}` for hard p, hence also for all p.
* **The lower limit: the class of one is optimal (Proposition 11.2'').**

  > **Proposition 11.2'' (PROVED; due to the Step-3 reviewer).** Let a
  > reduced class `c mod Q` be a complete prime certificate for `W>T`,
  > i.e. every prime `p≡c (mod Q)` has `W(p)>T`. Then
  > `log Q≥(2/3−o(1))T`.
  >
  > *Proof.*
  > 1. **The primes ≡3 (4).** By notes Thm 56.1, `P_3(T)|Q`, which
  >    contributes `θ(T;4,3)=T/2+o(T)`.
  > 2. **The class mod 3.** `𝓡(3)={2}`, so `c≡1 (mod 3)`.
  > 3. **A forced prime ≡1 (4).** Let `ℓ≡1 (4)` be prime, `ℓ≤T/3`, and
  >    `A=(3ℓ+1)/4`. Suppose some prime `r≡2 (3)` divides A. The atom
  >    `M=3ℓ`, `D=r` has class `−4r mod 3ℓ`, and
  >    `−4r≡−r≡1 (mod 3)`. If `ℓ∤Q`, this class is compatible with
  >    `c mod Q`. The combined class is reduced, since `r∤ℓ`. By Dirichlet
  >    it contains primes, which then have `W(p)≤3ℓ≤T`, a contradiction.
  >    So `ℓ|Q`.
  > 4. **The exceptional ℓ are negligible.** These are the ℓ for which
  >    `(3ℓ+1)/4` has no prime factor `≡2 (3)`. For any finite set S of
  >    primes `r≥5`, `r≡2 (3)`, they avoid the classes
  >    `ℓ≡−3^{−1} (mod r)`, `r∈S`. By PNT in progressions, their
  >    `log`-weight up to X is at most
  >    `(1/2)∏_{r∈S}(1−1/(r−1))·X+o(X)`, and this tends to 0 as S grows.
  >
  > Hence `log Q≥T/2+T/6−o(T)`. ∎

  So, to leading exponential order, the class of one `c=1`,
  `Q=L*(T)` (Lemma 11.1) is an optimal complete certificate. Notes
  Thm 56.1's `1/2` is not sharp. With Chang's exponent, no complete
  certificate does better than `5/8` by this route. A certificate class
  other than `c=1` could, however, contain a prime below Q.

**EVIDENCE.** For `T=7,15,…,63`, the least prime `≡1 (mod L*(T))` has
(the row T=7 has `p=337`, which is not Mordell-hard, since `T<15`)
`T/log p` between 1.20 and 1.64, near the conjectural 3/2. Its actual
`W(p)` is between 1.7 and 4.4 times `log p` (`data/pointwise_size/omega.txt`).

**The Type-I slice frame (Theorem 11.2'; PROVED modulo Chang Cor. 11,
cited; same proof; effectivity not claimed).** The genus-forcing
modulus of notes Thm 54.3, `R(T)=lcm(24,∏_{ℓ≤T}ℓ)`, is also smooth. So
`limsup ck_min(p)/log p≥5/12` (notes: `1/5.2`). Primes
`p≡1 (mod lcm(R(T),L*(T)))`, whose log is `(1+o(1))T`, have **both**
`W(p)` and `ck_min(p)` `≥(5/12−ε)log p` infinitely often.

### 11.2 The window frame: failure is never congruence-forced

**Lemma 11.3 (PROVED).** Let `q≡3 (4)` be a window modulus, let `Q≥1`, and
let c be a unit mod Q with `c≡1 (mod gcd(Q,4))`. Then infinitely many
primes `p≡c (mod Q)` have a Type II solution at the window `x_q=(p+q)/4`.
The same holds simultaneously for any finite set of windows.

*Proof.* By Dirichlet, choose a prime `r≡−1 (mod q)` with `r∤2qQ`.
Impose `p≡c (mod Q)`, `p≡1 (mod 4)` and `p≡−q (mod r)`. These are
compatible by CRT, and Dirichlet supplies infinitely many such primes.
Then `r|x_q` and `r≡−1 (mod q)`, so `u=r`, `v=1` gives
`−1∈Rat_q(x_q)` (Lemma 77.1; `gcd(x_q,q)=1` for `q<3p`). For several
windows, use distinct primes `r_q`. ∎

So the class-of-one mechanism of §11.1 and notes §54 has **no** analogue
for windows. Every set of primes defined by congruences contains primes
with any prescribed finite set of successful windows. A lower bound
`a_min(p)>K` must come from a *factorisation* event at each of the
`≈K/4` windows: F1, i.e. no prime factor that is a non-residue mod p
(Cor. 8.3), or a formal-prime event (Prop. 8.4).

**Proposition 11.4 (a_min(p)≥7 infinitely often; SKETCH, relying on the
cited semi-linear sieve).** There are `≫x/(log x)^{3/2}` hard primes
`p≤x` for which `(p+3)/4` has no prime factor `≡2 (mod 3)`. For these p
the window `q=3` fails (notes §6: success at q=3 iff such a factor exists),
so `a_min(p)≥7`.

*Sketch.*

1. **Parity.** For `p≡1 (3)`, `n=(p+3)/4≡1 (mod 3)`. So the number of prime
   factors `≡2 (3)` of n, counted with multiplicity, is even.
2. **The sieve.** Sift the shifted primes `(p+3)/4`, p hard, by the primes
   `≡2 (3)` up to `z=x^{1/2−ε}`. This is a half-dimensional problem.
   Iwaniec's semi-linear sieve has sieving limit `β=1`. With the
   Bombieri–Vinogradov level `D=x^{1/2−ε/2}` (`s=log D/log z>1`), it gives
   `≫_ε x/(log x)^{3/2}` survivors. (Cited: H. Iwaniec, *The half
   dimensional sieve*, Acta Arith. 29 (1976) 69–95; H. Iwaniec, *Primes of
   the type φ(x,y)+A where φ is a quadratic form*, Acta Arith. 21 (1972)
   203–234; Friedlander–Iwaniec, *Opera de Cribro*, ch. 14.)
3. **Large bad primes.** A survivor can still have prime factors `≡2 (3)`
   above z. For `ε<1/6` there are at most two, and by step 1 an even
   number, so zero or two. The survivors with exactly two are `n=m r_1 r_2`, with
   `r_i>x^{1/2−ε}` and `m≤x^{2ε}` composed of primes `≡1 (3)`.
4. **Removing them.** An upper-bound sieve on `(p, r_2)` counts these as
   `≪ε^{3/2}x/(log x)^{3/2}`. The semi-linear lower bound near `s=1`
   behaves like `(s−1)^{1/2}≍ε^{1/2}`. Small ε then leaves a positive
   proportion.

We have not written out the uniform prime-pair upper-bound sieve, the
weighted summation over m, or the constants. This is the classical
"shifted primes free of a half-set of primes" result type (cf. Linnik's
`p=x²+y²+1`). Status: **standard but unchecked here**.

**Assessment 11.5 (why the simultaneous-F1 sieve cannot give
`a_min(p)≥c log p`).** Scope: this is a barrier for the specific
construction "make every window ≤K fail by F1, via a lower-bound sieve".
It is not a theorem about all methods. Window failure can also occur
through exponent-budget failures (F3), and through non-Jacobi subgroup
failures at composite windows (§§8–9). Lemma 11.3 excludes only complete
congruence forcing.

* **A dimension barrier.** By Lemma 11.3, K consecutive windows must fail
  through K factorisation events on the shifted primes `(p+q)/4`. The
  cheapest event, F1, is half-dimensional; a prime cofactor (the formal
  adversary) is one-dimensional with parity. So the joint event is a
  lower-bound sieve problem of dimension `≥K/8` on the primes (`≈K/4`
  windows, each `≥1/2`).
  * F1 means the *complete* absence of non-residue factors. The sieve
    must therefore reach `z≈x^{1/2}`, or handle every configuration of
    large bad primes.
  * For dimension `κ>1/2` the sieving limit `β_κ>1` (`β_1=2`), and
    `β_κ` grows linearly in κ.
  * Already for `K=7` (windows 3 and 7, dimension 1), the leftover
    configurations of large bad primes are of the same order as the main
    term. A Chen-type switching argument would be needed; we have not
    attempted it.
  * For `K→∞` this sieve construction fails at every level of
    distribution, even Elliott–Halberstam (level 1). This is not a claim
    about other methods.
* **Why the combinatorial tools do not help.**
  * Maynard–Tao produces many prime values among K forms, but never all,
    and we need all K windows to fail.
  * Erdős–Rankin/FGKMT coverings produce "has a small prime factor",
    which is a dimension-0 local condition. F1 is the opposite: a global
    absence condition.
* **Conclusion.** The unconditional lower-bound construction developed
  here remains the sketch Prop. 11.4. `a_min` is unbounded under Dickson (Prop 8.4). It
  is `Ω(log p/log log p)` only under the uniform Hardy–Littlewood model
  (Assessment 8.5).

### 11.3 Why superlinear `W(p)>(log p)^{1+δ}` was not reached here (now reached: POINTWISE_OMEGA Theorem 5.1)

**Assessment 11.6 (heuristic error-budget calculation for one transfer
method; not a barrier theorem).** Consider certifying `W(p)>T` by "a
quarantine class c mod Q" plus a fundamental-lemma sieve for the
remaining atoms, transferred to primes with the known PNT-in-AP error
terms. Those errors decay like `exp(−c log x/log q)` in the Linnik range,
while the sieve needs relative error below the sifted density V. A
*sufficient* working range for this particular method is therefore
`log x≳log Q·log(1/V)/c`. That is a statement about what this error budget
supports, not a lower bound for every construction.

* **The class of one.** Here `V=1` and no sieve is needed. The least
  prime theorem (Chang) is applied directly, which gives §11.1.
* **The intermediate quarantine.** Take `p≡1 (mod Q_y)`, with all prime
  powers of primes `≤y` and `y=T^{1/2+η}`. Then every remaining modulus
  is `mℓ` with one prime `ℓ>y`, and the system becomes a *standard*
  sieve: `p mod ℓ∉F_ℓ` with `|F_ℓ|≤T^{1/2−η+o(1)}`. We have the *upper*
  bounds `log Q_y≈T^{1/2+η}` and `log(1/V)≤T^{1/2−η+o(1)}`, so the
  budget above is met once `log x≥T^{1+o(1)}`. *(Update: the bottleneck
  was the crude bound on `log(1/V)`. POINTWISE_OMEGA Lemma 2.3 shows
  `log(1/V) ≤ 2S ≤ T^{o(1)}`, by the congruence saving `m | r+k`. With
  Thorner–Zaman's Linnik-range PNT, this same route then gives
  `log x ≤ T^{1/2+o(1)}`, i.e. `W ≥ (log p)^{2−o(1)}` i.o. (POINTWISE_OMEGA
  Theorem 5.1). The sentences below record the Step-3 analysis.)* So this route, analysed
  this way, again gives only a linear range. No matching lower bound
  shows the route cannot do better. The construction does give a
  sub-exponential Haar bound (Lemma 11.7 below).
  > **Lemma 11.7 (PROVED; a sub-exponential unit-avoider bound).**
  > `log(1/δ*(T))≤T^{1/2+o(1)}`. Compare the class of one,
  > `δ*≥e^{−(2/3+o(1))T}`. This is §7's missing input (i) at a weak level.
  >
  > *Proof.* Fix `0<η<1/2` and `y=T^{1/2+η}`. Let `Q_y=lcm(24, ℓ^{e_ℓ} : ℓ≤y)`,
  > with `ℓ^{e_ℓ}≤T` maximal.
  >
  > * **Smooth moduli.** Condition on `n≡1 (mod Q_y)`. This costs
  >   `1/φ_h(Q_y)=e^{−(1+o(1))y}`, because `log Q_y=θ(y)+O(√T log T)`. It
  >   kills every y-smooth `M≤T`, by notes Thm 17.3(c).
  > * **Rough moduli.** Every other eligible `M≤T` is `mℓ` with a single
  >   prime `ℓ>y>√T` and `m<T/y<y`, so `m|Q_y`. Given the conditioning,
  >   the atoms of M reduce to the ℓ-coordinate condition `n mod ℓ∉F_ℓ`.
  >   Here F_ℓ collects the classes `−4D` with `D|((mℓ+1)/4)^2` and
  >   `−4D≡1 (mod m)`, over the eligible `m≤T/ℓ` with `mℓ≡3 (4)`. So
  >   `|F_ℓ|≤f_ℓ:=Σ_m τ(((mℓ+1)/4)^2)≤(T/ℓ)T^{o(1)}≤T^{1/2−η+o(1)}<ℓ/2`
  >   for large T.
  > * **Independence.** The coordinates mod distinct primes `ℓ∈(y,T]` are
  >   independent under Haar measure. Hence the conditional probability of
  >   avoidance is `∏(1−|F_ℓ|/(ℓ−1))≥exp(−2Σ_ℓf_ℓ/(ℓ−1))`, and this is
  >   `≥exp(−T^{1+o(1)}/y)`.
  >
  > Multiplying, `δ*(T)≥exp(−T^{1/2+η+o(1)})` for every `0<η<1/2`. ∎

* **One possible route to superlinear W (heuristic; we do not claim it
  works).** A quarantine with `log Q=L^{O(1)}`
  (`L=log T`) and conditional density `V≥exp(−L^{O(1)})`, i.e. the prime
  analogue of notes Thm 31.4. With z polylogarithmic, the rough moduli
  carry several primes. The system is then not prime-local, and the route
  would need at least the following:
  * **(i)** an LLL-type Haar lower bound. Its key input is a mean value
    for divisors of `((M+1)/4)^2` in the class `−(M+1)/4 mod m`, which is a
    lattice count in the spirit of notes Lemma 16.2.
  * **(ii)** a transfer to primes, by pointwise Bonferroni truncation with
    moduli `≤exp(L^{O(1)})`.

  Prime-side technology for (ii) exists: PNT in APs uniformly for
  `q≤exp(c√log N)`, with error `N exp(−c√log N)`, far below the needed
  `exp(−L^{O(1)})`. An exceptional (Siegel) character still needs control.
  Positivity of `1−x^{β_1−1}` is not a quantitative lower bound beating
  the error. Its twisted density would also need an actual estimate in
  this multi-prime, correlated system. Besides (i), the missing inputs
  therefore include:
  * exceptional-character control;
  * control of the accumulated Bonferroni truncation errors under the
    positive correlations of atoms that share a rough prime.

  The notes' §39 factorial-moment machinery is of this type, and is
  CLAIMED/PROVISIONAL. **We do not claim this route works**, and the list
  above is not claimed to be complete.
* **The Jacobsthal remark** (cf. notes §58.3). For *arbitrary* forbidden
  classes, one per prime `ℓ≤T`, primes below `e^{O(T)}` can be avoided
  entirely in short ranges. These are Erdős–Rankin/FGKMT-type
  constructions; they produce large prime-free gaps, not
  least-prime statements. This suggests that a density-only argument
  will not suffice, and that a superlinear proof would have to use the
  specific structure of `𝓡(ℓ)`. That is an expectation, not a theorem.

## 12. Cross-checks against the literature and the notes

* **Pomerance–Weingartner, arXiv:2511.16817v2** (archived; notes §68 audit).
  * **Thm 3.1.** It gives many exceptional primes for large numerator m.
    The method is a union bound over all Type I/II admitting classes, via
    Brun–Titchmarsh (pw.txt ll. 318–448). The upper bounds proved there
    for the covered-prime proportion are, for Type I,
    `O((log N)^3 log²m/φ(m))`, and similarly for Type II with an extra
    `log log N` factor before simplification. These are below 1/2 at
    `log N_0=(φ(m)/C log²m)^{1/3}`.
  * **m=4.** At `m=4` the corresponding mass is `≍(log N)^3≫1` (cubic
    supply, notes Thm 18.2), so the union bound is empty. This is exactly why §7 works
    with the avoider density δ*(T) and §11.1 with the class of one. Their
    Poisson heuristic (p. 3, with intensity `(log p)^3/m`; at m=4 it is
    Elsholtz–Tao Remark 1.1) is the same cubic-mass model as §7's
    independence exponent `I(T)≍(log T)^3`.
  * **Scope.** PW define no truncated statistic (W, `a_min`). For m=4
    they give no improved asymptotic exception bound and no
    truncated-statistic theorem. What they do give for m=4 is the upper
    bound (68.1), with Vaughan's 2/3, finite verifications, and the
    heuristic. Prop 8.4, Lemma 11.3 and Thm 11.2 are **not** in PW.
* **Notes §56 (certificate ceilings).** Thm 56.1: every Type-II
  congruence certificate for `W>T` contains `P_3(T)`, so
  `log Q≥(1/2+o(1))T`. Prop. 11.2'' sharpens this to `(2/3−o(1))T`, which
  matches Lemma 11.1. So the class of one is optimal to leading order.
  Thm 56.2 (Type I, `log Q≥T+o(T)`) matches Theorem 11.2' exactly.
* **Notes §58 (Jacobsthal angle).**
  * (58.18) is improved by Thm 11.2(b).
  * Lemma 58.5 says that `W(p_j)/log p_j→∞` along some sequence iff
    `liminf log L_p(T)/T=0`. Thm 11.2 gives `log L_h(T)/T≤8/5+o(1)`, so
    the superlinear question is exactly whether the liminf is 0. It is:
    POINTWISE_OMEGA Theorem 5.1 gives `log L_h(T) ≤ T^{1/2+o(1)}` (PROVED
    modulo Thorner–Zaman Cor. 1.4), so `liminf=0` and
    `W(p_j)/log p_j→∞`. Under RA
    and the two-sided assumption of Assessment 7.2, §7 predicts
    `log L_p(T)=(log T)^{3+o(1)}`, hence liminf 0 (heuristic).
  * Assessment 58.1 ("density alone gives no least-prime theorem…") is
    consistent with Assessment 11.6, which quantifies the error budget
    `log Q·log(1/V)` of one specific transfer method.
* **Notes §54.** Thms 54.1 and 54.3 are superseded in their constants by
  Thm 11.2 and 11.2' (5/8 and 5/12 instead of 1/5.2). The new constants
  come *without* a stated effectivity claim, whereas notes §54 is
  explicitly effective. The §54 proofs and statements remain correct as
  weaker, effective results.
* **Notes §6 / §70.** Prop. 11.4's window-3 event is the §6
  `q=3`-parity mechanism. Lemma 11.3 is the precise form of "the class
  of one does not transfer to windows" (§77.1's free prime factors).

## Replay

```
(ulimit -v 4000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_ct_check.py 5000 1000)   # ~20 s
(ulimit -v 8000000; PYTHONPATH=scripts uv run python scripts/pointwise_size_toy_formal.py 20000000)  # ~3 min
# Step 2, section 7 (multiplier tail); outputs in data/pointwise_size/wtail/
export PYTHONPATH=scripts; P="uv run python scripts/pointwise_size_wtail.py"
$P split 4095 20 200000 3            # ~2 min
for s in 11 12 13 14; do $P split 16383 6 50000 $s; done     # ~1 min each
for s in 21 22 23 24; do $P split 65535 10 50000 $s; done    # ~15 min each
$P census 8191 1000000000            # all hard p < 1e9, ~10 s, 12 GB limit
$P primes 1023 18 200000 5           # sample near 1e18
uv run python scripts/pointwise_size_indep.py 1048575         # I(T), ~2 min
uv run python scripts/pointwise_size_wtail_table.py           # table.txt
# Step 2, sections 8-9 (window frame, seeding); outputs in data/pointwise_size/window/
A="uv run python scripts/pointwise_size_amin.py"
$A census 100000000 [1]              # all hard [Mordell-hard] p < 1e8, ~2 min
$A windows 100000000 127             # per-window marginals / joint / by n_p, ~25 min
$A sample 12 30000 11; $A sample 18 30000 12        # Mordell-hard samples
$A class1 23 2000 3; $A class1 41 1000 4            # class-of-one primes
$A formal 15 3000000; $A formal 19 10000000; $A formal 23 30000000; $A formal 27 30000000; $A formal 31 30000000
$A sample_windows 12 10000 31 31; $A sample_windows 18 10000 32 31   # single-window marginals (8.4)
$A seeded 100000000 20 1             # seeded windows, Mordell-hard p < 1e8
$A sample_seeded 12 20000 21; $A sample_seeded 18 20000 22; $A sample_seeded 24 5000 23
PYTHONPATH=scripts uv run python scripts/pointwise_size_wrecords.py   # W-records vs a_min
# Step 3, section 11
PYTHONPATH=scripts uv run python scripts/pointwise_size_omega.py      # log L*(T)/T, least primes = 1 mod L*(T)
```
(`amin_s12.json`/`amin_s18.json` in `data/pointwise_size/window/` are earlier all-hard samples,
seeds 1/2, produced before the Mordell filter was added to `sample`; `amin_m12/m18.json` are the
Mordell-hard ones quoted in §8.5. The `frac_typeI` field of `amin_class1_*.json` was computed with
the first draft's order-dependent type label and is not used; success/failure booleans are unaffected.)
