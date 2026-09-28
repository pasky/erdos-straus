# Short seed escapes: exact depth-3 classification, and why no depth bound can hold

Notation is that of [SIGNED_REFACTOR.md](SIGNED_REFACTOR.md): `p=4t+1` is
prime, the seed is `σ=(t,-2pt,-2pt)`, vertices are signed triples with
`4/p=1/x+1/y+1/z`, and edges join triples sharing a denominator. The **seed
distance** `dist(p)` is the least number of edges from `σ` to an all-positive
vertex. Labels: **PROVED**, **CONDITIONAL** (proved from a named
hypothesis), **EVIDENCE** (finite computation), **CONJECTURE**.

Summary.

1. **PROVED (Theorem 1).** `dist(p)≤3` iff one of three explicit
   divisor conditions holds: the two-move criterion (9) or one of the
   families **A** (negative-fibre transfer) and **B** (Type II swap).
   No other depth-3 mechanism exists. The implementation is validated
   against a brute layered BFS through nonpositive vertices for every prime
   `p≡1 (4)` below `3·10^4` and a sample to `3·10^5`. The positive vertices
   reached by escapes of exactly 2 and 3 edges agree exactly.
2. **CONDITIONAL on Schinzel's Hypothesis H (Theorem 2).** For every `k`
   there are infinitely many primes `p=24q+1` (q prime) such that **every
   vertex within distance k of the seed is nonpositive**. So `dist(p)` is
   unbounded; the empirical "distance ≤3" pattern is not a theorem to be
   proved, and no bounded-depth argument from the seed can prove ES for
   `p≡1 (24)`. Under the (stronger) Bateman–Horn conjecture for the
   same finite family, the number of such `p≤N` is `≫_k N/(log N)^{C_k}`.
3. **PROVED (Theorem 3 + Corollary).** Every prime outside Mordell's six
   hard classes mod 840 has `dist(p)=2`. Standard upper-bound sieves give
   `#{p≤N: dist(p)>2} ≪ N/(log N)^{2.02}` and
   `#{p≤N: dist(p)>5} ≪ N/(log N)^{3.04}`. These are polylogarithmic
   savings. Under Bateman–Horn, Theorem 2 shows that nothing better than
   polylogarithmic can hold.
4. **EVIDENCE.** All 10 known distance-3 primes below `5·10^6` escape
   through family A. So does every prime `p=24q+1` with q prime,
   `q≤10^11`, that fails (9). The search continues to `q≤10^13`; no prime of
   distance `≥4` has been found (§5).

The signed character theorem (2a) used below is, in substance, Bright–Loughran
(2020), Thm 1.2 with Thm 1.5 (the local-invariant computation for the
Erdős–Straus surface); its signed-graph form and proof are in
SIGNED_REFACTOR §2.

## 1. Facts used

These are proved in SIGNED_REFACTOR.md.

* **(F1)** `-2pt` lies in no vertex except `σ`. Every neighbour of `σ` contains `t`.
* **(F2)** Every vertex has one p-divisible denominator (Type I) or two
  (Type II), each of p-adic valuation exactly one.
* **(F3) Type I chart.** Choose any p-free coordinate `x=t+a` of a Type I
  vertex. Its p-divisible coordinate is `p(ph-t)`, and the vertex is
  `(t+a, p(ph-t), (t+a)(ph-t)/e)`, with `e=(4a-1)h-a≠0` and `e | (t+a)²`.
  Every vertex has a positive p-free coordinate `≤2t`.
  In a chart with `1≤t+a≤2t`, the vertex is all-positive iff `a≥1` and `h≥1`.
  Symmetric form: `e | (t+a)² ⇔ e | (ph-t)²`.
* **(F4)** The fibre of a negative p-free denominator has at most one vertex.
* **(F5)** By (2a), a Type II p-divisible bucket (nonzero label) is wholly
  positive or wholly nonpositive.
* **(F6)** A positive denominator `z≤t` lies in no positive vertex, since
  `1/z≥1/t>4/p`.

A positive p-free `z` is **productive** if its fibre contains a positive
vertex. For `t<z≤2t`, put `q_z=4z-p`. Then `z` is productive iff some
positive `D|z²` satisfies

```
D ≡ -z (mod q_z)     [Type II exit (z, p(z+D)/q_z, p(z+z²/D)/q_z)]
D ≡ -1/4 (mod q_z)   [Type I exit (z, (p²D+pz)/q_z, (z²/D+pz)/q_z)].
```

This is the classical anchor criterion. For `z>2t`, the fibre has at most two
vertices; they are found from the interval (10) of SIGNED_REFACTOR §5,
without factoring.

## 2. Theorem 1: the complete list of escapes of length at most 3

**Theorem 1 (PROVED).** Let `p=4t+1` be prime. Then:

* `dist(p)≤2` iff **(9)** holds: some `h>0` with `h|t²` has a positive
  `D|(ph-t)²` with `D≡-h (mod 4h-1)`.
* `dist(p)≤3` iff (9), (A), or (B) holds:

**(A) negative-fibre transfer.** There are `c>0`, `c|t²`, and `d>0`,
`d|(pc+t)²`, with `d≡-c (mod 4c+1)`. Put `a=(d+c)/(4c+1)`, `x=t+a` with
`p∤x`, and `w=x(pc+t)/d`. Then `x` or `w` is productive. The path is

```
σ → (t, -p(pc+t), -t(pc+t)/c) → (x, -p(pc+t), w) → positive vertex ∋ x or w.
```

**(B) Type II swap.** Choose a signed `δ|t²` with `δ≠±t`, and put
`V1=(t, p(δ-t), p(t²/δ-t))`. For `m∈{δ-t, t²/δ-t}`, the Type II fibre of
`pm` has at most two vertices, found by the two-candidate rule of
SIGNED_REFACTOR §5. The other vertex `V2=(x',pm,pn')` must have a productive
p-free coordinate `x'`.

*Proof.* By (F1), the first layer `L1` is the t-fibre minus σ. By (F6), it is
nonpositive. Its vertices are:

* Type I, `(0,h)` in the chart, with `x=t`. Here `e=-h`, so `h=±d` and
  `d|t²`. The vertex is `V1(h)=(t, p(ph-t), -t(ph-t)/h)`. Its p-free entry
  `-t(ph-t)/h` is negative for both signs of h.
* Type II, `(t,pm,pn)` with `(m+t)(n+t)=t²`, i.e. `m=δ-t`.

*Distance 2.* A positive P adjacent to `V1∈L1` shares some `z≠t`, by (F6).
For `V1(h)`, the negative p-free entry is impossible. So `z=p(ph-t)` needs
`h>0`, and P is a positive vertex of the bucket. By (F3) this means an
`a≥1` with `e|(t+a)²`. By the symmetric form, this is (9). For a Type II `V1`,
both p-divisible buckets are nonpositive by (F5).

*Distance 3.* Let `σ-V1-V2-P` with `V2` nonpositive and not in `L1`. Then
`V2` shares with `V1` some `z1≠t`. We use one more fact from SIGNED_REFACTOR
§2: a p-divisible denominator has label 0 (Type I) or a nonzero label
(Type II), never both. So `V2` has the same type as the bucket of `z1`, and
a Type I `V2` sharing `p(ph-t)` lies in the chart column h.

* `V1=V1(h)` and z1 is the negative p-free entry. By (F4), `V2=V1`; this is
  impossible.
* `V1=V1(h)`, `h>0`, and `z1=p(ph-t)`. Chart `V2` with p-free
  `x2∈[1,2t]`. Nonpositivity forces `a≤0`, so `x2≤t`. Then
  `e=a(4h-1)-h<0`, so the third entry is negative. P cannot contain `x2`, by
  (F6), nor the negative entry. It could contain `p(ph-t)`, but then P is
  adjacent to V1 and was counted at distance 2.
* `V1=V1(-c)`, `c>0`, and `z1=-p(pc+t)`. Chart `V2=(a,-c)` with
  `x2∈[1,2t]`. If `a≤0`, then `e=c(1-4a)-a>0`; the third entry is negative
  and `x2≤t`, so V2 is dead. If `a≥1`, then `E:=-e=(4c+1)a-c>0`, and both
  p-free entries are positive. The p-divisible entry is negative, so P
  contains `x2` or `w2`. By the symmetric form, `E|(t+a)²` iff `E|(pc+t)²`.
  Setting `d=E` gives (A).
* `V1` is Type II and `z1=pm`. Then `V2` is the other vertex of that Type II
  fibre, and it is nonpositive by (F5). Its second p-divisible entry has a
  residue label, since both labels of a nonpositive Type II vertex are
  residues (2a). By (F5), that bucket is nonpositive. Hence P contains the
  p-free `x'`. This is (B).

Conversely, every listed path is legal. ∎

**Consequences.**

* A two-move escape through a Type II first step is impossible, as already
  known. A three-move escape through a *positive* Type I bucket (`h>0`) is
  impossible unless a two-move escape exists.
* The only new depth-3 mechanisms are the transfer through the negative
  buckets `h=-c` (A) and the Type II swap (B).
* In A, `d≤(pc+t)²` ranges over divisors, so `a` can be large. Anchors with
  `a>t` are the same vertices charted from their other positive p-free
  entry `w∈(t,2t]`.

**Validation (EVIDENCE for the implementation, not needed for the proof).**
`scripts/depth3_validate.py` uses the exact lazy fibres of
`pointwise_fibres.py`. It computes the complete sets `Pos2` and `Pos3` of
positive vertices ending a seed path of exactly 2, respectively 3, edges
whose intermediate vertices are **nonpositive**. These are the escape-relevant
layers. They are not the full BFS layers: at `p=73`, a third positive vertex
at graph distance 3 is reached only through a positive intermediate vertex.
It compares them with the sets generated by the families. The results are:

| range | primes | mismatches |
|---|---|---|
| all `p≡1 (4)`, `13≤p<3·10^4` | 1610 | 0 |
| every 5th `p≡1 (4)`, `2·10^4≤p<3·10^5` | 2371 | 0 |
| the 10 known distance-3 primes | 10 | 0 |

### Which families the known distance-3 primes use (EVIDENCE)

All ten distance-3 primes below `5·10^6` escape through A. They have many
A-hits, 12–23 each. The Type II swap B also succeeds at `513529`, `710089`,
`1083289`, and `3389929`. None escapes through B alone. Typical successful
transfers are:

| p | (c, d, a) of successful A-transfers exiting at x=t+a |
|---|---|
| 297049 | (2,160,18), (2,196,22), (2,448,50), (2,700,78), (3,361,28), (6,169,7) |
| 513529 | (2,16,2), (2,169,19), (2,880,98), (6,19,1), (12,1458,30), (18,128,2) |
| 3942409 | (1,19,4), (1,209,42), (1,289,58), (2,520,58), (2,1744,194) |

The recurring transfers are **forced by congruences**. For `t≡2 (mod 4)`:
`16 | (2p+t)²=(9t+2)²` and `16≡-2 (mod 9)`. So `(c,d)=(2,16)` always gives the
anchor `t+2`, with modulus 7. Similarly, `(6,144)` always gives `t+6` when
`t=6q` with q odd. Whether the anchor is then productive is a factorization
event.

## 3. Theorem 2: under Hypothesis H the seed distance is unbounded

**Hypothesis H (Schinzel).** Let `f_1,…,f_m∈Z[y]` be irreducible with
positive leading coefficients. Suppose no prime divides
`f_1(y)⋯f_m(y)` for every integer y. Then there are infinitely many y
with all `f_i(y)` prime.

**Theorem 2 (CONDITIONAL on H).** For every `k≥0` there are infinitely many
primes `q` with `p=24q+1` prime such that every vertex at graph distance `≤k`
from the seed is nonpositive. In particular `dist(p)>k`.
If Bateman–Horn holds for the finite family below, there are
`≫_k N/(log N)^{C_k}` such `p≤N`.

The proof is a graph version of Schinzel's obstruction to polynomial
identities. H makes every integer met within distance k factor *formally*,
i.e. as polynomial values in q. Then every prime met has a Legendre symbol
mod p computable from a constant, and a congruence choice makes all of them
`+1`. The character theorem (2a) then forbids positivity.

### 3.1 A generic profinite base point

Let `𝒫` be the set of primitive irreducible `g∈Z[X]` with positive leading
coefficient, enumerated as `g_1,g_2,…`. Put `P(X)=24X+1`.

**Lemma 1.** There is `q* = (q*_ℓ) ∈ ∏_ℓ Z_ℓ` with the following properties:

1. every `q*_ℓ` is a unit, and `24q*_ℓ+1` is a nonzero square unit in `Z_ℓ`;
2. every `q*_ℓ` is transcendental over Q, so `g(q*_ℓ)≠0` for all
   `g∈𝒫`;
3. for each `g∈𝒫`, `v_ℓ(g(q*_ℓ))=0` for all but finitely many ℓ.

*Proof.* For `ℓ=2,3`, every unit works for (1): `24u+1≡1` mod 8,
respectively mod 3, is a square. For `ℓ≥5`, let `n(ℓ)` be the largest n with
`Σ_{i≤n} deg g_i < (ℓ-3)/2`. Choose a residue `r mod ℓ` with the following
properties:

* `r≢0`;
* `24r+1` is a nonzero quadratic residue;
* r is not a root of `g_1,…,g_{n(ℓ)}` mod ℓ.

The first two conditions leave `(ℓ-3)/2` residues. At most
`Σ_{i≤n(ℓ)}deg g_i` are excluded. Lift r to a transcendental element of
`r+ℓZ_ℓ`; algebraic elements form a countable set. Hensel's lemma
keeps `24q*_ℓ+1` a square. Since `n(ℓ)→∞`, each g is avoided at all large ℓ. ∎

Fix q*, and define `C_g=∏_ℓ ℓ^{v_ℓ(g(q*_ℓ))}`, a positive integer.
For example, `C_X=C_P=1`.

### 3.2 Admissible q and formal numbers

Let `S⊂𝒫` be finite with `X,P∈S`. Let Λ be a finite set of primes
containing 2, 3, every prime dividing some `C_g` (`g∈S`), every prime
`≤Σ_{g∈S}deg g`, and every prime dividing a leading coefficient.
Let `E_ℓ>max_{g∈S} v_ℓ(g(q*_ℓ))`, and put `M=∏_{ℓ∈Λ}ℓ^{E_ℓ}`.

An integer q is **(S,Λ)-admissible** if the following hold:

* `q≡q*_ℓ (mod ℓ^{E_ℓ})` for all `ℓ∈Λ`;
* for every `g∈S`, `r_g:=g(q)/C_g` is a prime outside Λ;
* the `r_g` are pairwise distinct;
* q exceeds a threshold depending only on (S,Λ); it is used below for
  sign and valuation stabilisation.

Then `v_ℓ(g(q))=v_ℓ(C_g)` for `ℓ∈Λ`. Also `r_X=q` and `r_P=p`.

**Lemma 2 (H supplies admissible q).** H implies that there are infinitely
many (S,Λ)-admissible q.

*Proof.* Fix `q̃≡q*` mod M, and put `f_g(y)=g(My+q̃)/C_g`.

* **Integrality.** The Taylor coefficients `g^{(j)}(q̃)/j!` are integers.
  Hence every non-constant coefficient is divisible by
  `M^j`, which is divisible by `C_g`. The constant term `g(q̃)` is divisible by `C_g`.
  So `f_g∈Z[y]`. It has positive leading coefficient. It is primitive: for
  `ℓ∈Λ` its constant term is an ℓ-unit (next bullet), and for `ℓ∉Λ` its
  leading coefficient `lc(g)M^{deg g}/C_g` is. Being irreducible over Q, it
  is irreducible over Z.
* **Primes in Λ.** Here `g(My+q̃)≡g(q̃)` mod `ℓ^{E_ℓ}`, so `f_g(y)`
  is an ℓ-unit.
* **Primes outside Λ.** Neither `lc(f_g)` nor `C_g` is divisible by ℓ.
  So `∏f_g` is nonzero mod ℓ, of degree `<ℓ`, and has a non-root.

Thus there is no fixed prime divisor. Large H-solutions y give distinct
`r_g`, since distinct elements of 𝒫 are non-proportional. ∎

A **formal number** over (S,Λ) is a rational function of the form

\[
 \varphi=\varepsilon\prod_{\ell\in\Lambda}\ell^{\alpha_\ell}
 \prod_{g\in S}(g/C_g)^{\beta_g},\qquad \varepsilon=\pm1.
\]

It is a **formal integer** if all exponents are nonnegative. At admissible q,
`φ(q)=ε∏ℓ^{α_ℓ}∏r_g^{β_g}` is read off as a prime factorization.
The primes are pairwise distinct.

**Lemma 3 (fibre closure).** Let Z be a formal integer over (S,Λ). There
are finite `S'⊇S` and `Λ'⊇Λ`, and a finite set `𝒱(Z)` of triples of formal
integers over (S',Λ'), with the following property. For every
(S',Λ')-admissible q, every vertex whose denominators include `Z(q)` is the
value at q of a member of `𝒱(Z)`.

*Proof.* At `z=Z(q)`, the fibre consists of the triples (z,y,w) with
`1/y+1/w=(4z-p)/(pz)`.

* **The quantity 4Z−P.** It is a nonzero polynomial in `Q[X]`, since
  `z=p/4` is impossible. Factor it as `κ∏h_i^{e_i}` with `h_i∈𝒫` and
  `κ∈Q^×`. Adjoin the `h_i` to S. Adjoin the primes of κ and of the `C_{h_i}`
  to Λ. Then `4z-p` and `pz` are formal.
* **Reduction.** Distinct primes make the reduced form `r/s` formal.
  The exponents are minima, and s is normalised positive. For large q, signs
  of polynomial values are those of their leading coefficients.
* **Divisors.** Every vertex has `ry-s=D`, a signed divisor of `s²`.
  At admissible q, D is the value of one of finitely many formal integers
  dividing `s²` formally.
* **New denominators.** For each such D with `D+s≢0`, factor `D+s` in
  `Q[X]` as above, and adjoin its factors and constants. Treat `s²/D+s`
  the same way. Then `y=(D+s)/r` and `w=(s²/D+s)/r` are formal numbers.
  If they are integers, they are formal integers, since the primes are distinct.

Only finitely many D occur. None of this depends on q beyond admissibility.
The constants `C_h` are fixed once and for all by q*. ∎

Enlarging (S,Λ) keeps everything already fixed. The constants `C_g` depend
only on q*. Each old exponent `E_ℓ` may be kept or increased, and the
congruence `q≡q*_ℓ (mod ℓ^{E_ℓ})` only becomes finer. New primes, including
those `≤Σdeg g` and those dividing new leading coefficients, are simply
adjoined to Λ. Old thresholds are kept by taking the maximum. Hence
`(S',Λ')`-admissibility implies `(S,Λ)`-admissibility.

Apply Lemma 3 to every denominator of every triple, starting from
`σ=(6X,-12XP,-12XP)` over `S_0={X,P}` and `Λ_0={2,3}`. After k rounds,
this gives finite `S_k`, `Λ_k`, and `𝒱_k`. By induction on the
distance, every vertex within distance k of σ is the value of a member of
`𝒱_k`, for every `(S_k,Λ_k)`-admissible q.

### 3.3 Every prime met has character +1

Enlarge `Λ_k` by the primes dividing the nonzero integers

\[
 H_g=24^{\deg g}\,g(-1/24),\qquad g\in S_k\setminus\{P\}.
\]

`H_g≠0`, because g is irreducible and not associated to P.
Let q be admissible for the enlarged set. The following hold:

* **ℓ∈Λ_k.** `(2/p)=1` since `p≡1 (8)`, and `(3/p)=(p/3)=1`.
  For `ℓ≥5`, `(ℓ/p)=(p/ℓ)`, and `p≡24q*_ℓ+1` is a nonzero square mod ℓ by
  Lemma 1(1).
* **g∈S_k\{P}.** Since `24q≡-1 (mod p)`, `24^{deg g}g(q)≡H_g (mod p)`.
  Also `(24/p)=1`, and every prime of `C_g` and of `H_g` is in Λ.
  Hence `(r_g/p)=(g(q)/p)(C_g/p)=(H_g/p)=1`. This needs `p∤H_g`, which
  holds for q large.
* **Signs.** `(-1/p)=1`.

Take any vertex within distance k. Take its two same-valuation coordinates
and remove p from them, giving A and B. Each is `±` a product of primes of
character `+1`, so `(AB/p)=+1`. By (2a) the vertex is not all-positive.
Lemma 2 gives infinitely many admissible q. This proves Theorem 2. ∎

**Remarks.**

* **Scope.** The proof uses no property of the seed except that its
  denominators are formal. The same holds for any bounded-radius
  exploration of the graph from formally given vertices. In particular it
  holds for every "universal" path built from divisors that exist for all p
  in a residue class.
* **Relation to Schinzel's theorem.** Schinzel's theorem rules out
  polynomial identities on square classes. Theorem 2 adds, under H, that
  divisor-dependent branches cannot help at any bounded depth either: H
  forces all those divisors to be formal.
* **Consequence for strategy.** A proof of the seed-component conjecture
  cannot proceed by bounding the escape length. This sharpens the assessment
  in SIGNED_REFACTOR §7 from heuristic to a conditional theorem.
* **Why H is used only in a finite form.** For a fixed k, only H for the
  explicit finite family `{f_g : g∈S_k}` is needed.

**What the construction does *not* give.**

* It gives no explicit small example. The family `S_k` is large, so the
  Bateman–Horn density `(log N)^{-|S_k|}` is tiny. Actual depth-4 primes, if
  they exist in computable range, must come from *partial* genericity; see
  §4.
* It says nothing about the whole seed component, which is finite for each
  p. ES itself is untouched.

### 3.4 A consistency check of the mechanism

In the class forced by Lemma 1, the always-available transfer
`(c,d)=(2,16)` reaches the anchor `x=t+2=2(3q+1)`, with modulus 7.
Suppose `3q+1=2^j r` with r prime. Then `r≡2^{-j}p (mod 7)`. This is a
residue, since `(2/7)=1`.
Every divisor of `x²` is then a residue mod 7, while both targets
`-1/4≡5` and `-x` are non-residues. So the branch fails, exactly as the
character argument predicts. Numerically, this branch succeeds only when
`3q+1` has a non-residue prime factor mod 7, or when p is a non-residue
mod 7. The latter never occurs among survivors of (9): all survivors are
residues mod 5 and 7, in Mordell's hard classes.

## 4. Theorem 3: unconditional upper bounds for the exceptional sets

Theorem 2 gives, under Bateman–Horn, `#{p≤N: dist(p)>k} ≫ N/(log N)^{C_k}`. In
the other direction, a standard upper-bound sieve proves a polylogarithmic
saving.

**Lemma 4 (explicit short paths).** Let `p=4t+1` be prime.

1. **(H-branch, 2 edges.)** Let `h|t²` and `K=4h-1`. Suppose `m=ph-t` has a
   prime factor `ℓ≡-1/4 (mod K)`. Then `D=ℓ` satisfies (9), since
   `-h≡-1/4 (mod K)`. The path is
   `σ, (t,pm,-tm/h), (pm,(m+ℓ)/K,(m+m²/ℓ)/K)`.
2. **(X-branch, 5 edges.)** Let `d|t²` and `K=4d-1`. Suppose `z=t+d` has a
   prime factor `ℓ≡-1/4 (mod K)`. Then there is the path
   `σ,B1,B2,(2t,2t,-pt), (z,-pt,tz/d), (z,(p²ℓ+pz)/K,(z²/ℓ+pz)/K)`.
   Here `B1,B2` are the bridge vertices of SIGNED_REFACTOR (1). The fourth
   vertex is the point `(a,h)=(d,0)` of the chart axis (8).
3. **(forced, 2 edges.)** Let `p≡17 (mod 24)`. Then t is even and
   `t≡1 (mod 3)`, so `6 | 7t+2 = 2p-t`. Thus `h=2` divides `t²`, and `D=12`
   divides `(2p-t)²` with `12≡-2 (mod 7)`. Criterion (9) holds.
   This is Mordell's `p≡2 (mod 3)` identity seen in the chart.
4. **(forced, 2 edges.)** If `p≡5 (mod 8)`, then t is odd, and `ℓ=2` divides
   `3t+1`. So `dist(p)=2`.
5. **(forced, 2 edges; review repair.)** Let `p≡1 (mod 24)`, so `6|t`, and
   let p be a non-residue mod 5 or mod 7. Write `m=ph-t`. The certificate
   `D` of (9) is forced:

   | class | h | D | reason |
   |---|---|---|---|
   | `p≡3 (5)` | 1 | 5 | `t≡3 (5)`, so `5|3t+1`, and `5≡2 (3)` |
   | `p≡2 (5)` | 2 | 5 | `t≡4 (5)`, so `5|7t+2`, and `5≡-2 (7)` |
   | `p≡3 (7)` | 6 | 63 | `m=23t+6`; `3|m` and `t≡4 (7)` give `21|m`; `63≡-6 (23)` |
   | `p≡5 (7)` | 3 | 63 | `m=11t+3`; `t≡1 (7)` gives `21|m`; `63≡-3 (11)` |
   | `p≡6 (7)` | 4 | `m/14` | `m=15t+4`; `t≡3 (7)` gives `14|m`; `D≡4·14^{-1}≡-4 (15)` |

6. **(forced, 5 edges; subsumed by 3 but kept as a check.)** If `p≡2 (mod 3)`,
   then `t≡1 (mod 3)`, and the anchor `t+1` has the Type II exit with `D=1`.

**Corollary (PROVED).** Every prime outside Mordell's six classes
`p≡1,121,169,289,361,529 (mod 840)` has `dist(p)=2`. These are exactly
`p≡1 (24)` with p a residue mod 5 and mod 7. The seed-component
conjecture, and every question about its distance, concerns only these
classes. They are the classical hard classes, so this gives no new
information about ES. It shows that the seed reproduces Mordell's
identities within two moves.

All identities are verified by `scripts/depth5_branches.py`, which builds and
checks every path for each prime in a range. For `p<3·10^6`, every prime outside Mordell's six
classes has an H-branch or a forced branch. The only primes with no
branch at all lie in the class 1 mod 24: 689 of its 26983 primes. The branch
list is sufficient, not necessary: all of these primes have `dist≤3`.

**Theorem 3 (PROVED, modulo a standard sieve theorem).** Put

\[
 \kappa_2 = \sum_{h\mid 36}\frac1{\varphi(4h-1)}\approx 1.023,\qquad
 \kappa_5 = 2\kappa_2\approx 2.046 .
\]

Then

\[
 \#\{p\le N:\ \mathrm{dist}(p)>2\}\ll \frac{N}{(\log N)^{1+\kappa_2}},
 \qquad
 \#\{p\le N:\ \mathrm{dist}(p)>5\}\ll \frac{N}{(\log N)^{1+\kappa_5}} .
\]

*Proof.* By Lemma 4(3,4), `dist(p)>2` forces `p≡1 (mod 24)`. Lemma 4(5)
could also restrict the residues mod 5 and 7; this only changes constants. Then `6|t`,
so `d|t²` for all nine `d|36`. Moreover:

* `dist(p)>2` implies that no H-branch with `h|36` applies;
* `dist(p)>5` implies, in addition, that no X-branch with `d|36` applies.

In terms of p:

* `ℓ|ph-t` iff `p≡-(4h-1)^{-1} (mod ℓ)`, since `4(ph-t)=p(4h-1)+1`;
* `ℓ|t+d` iff `p≡1-4d (mod ℓ)`.

Thus each branch excludes one residue class of p modulo every prime ℓ in a
fixed class mod `4h-1` (resp. `4d-1`). Apart from finitely many ℓ, the classes
excluded by different branches are distinct. For example, H(h) and X(h)
coincide only if `ℓ|8h(2h-1)`.

Sift the *integers* `n≤N`, `n≡1 (mod 24)`, rather than the primes. This
avoids Bombieri–Vinogradov. For each prime `ℓ>3` not dividing any of the
moduli `4h-1`, and not among the finitely many coincidence primes, remove:

* the class `n≡0 (mod ℓ)`, since p is prime;
* the `ω(ℓ)` branch classes above.

In total `1+ω(ℓ)` classes are removed. By the prime number theorem in
progressions, `Σ_{ℓ≤z}ω(ℓ)(log ℓ)/ℓ = κ log z+O(1)`, where κ is the sum of
`1/φ(4h-1)` over the branches used. This is a sieve problem of dimension
`1+κ`. The large sieve (Montgomery), or Selberg's upper-bound sieve
(Halberstam–Richert, *Sieve Methods*, Thm. 5.1), both with the trivial level
of distribution for integers in progressions, gives

\[
 \ll N\prod_{\ell\le \sqrt N}\Bigl(1-\frac{1+\omega(\ell)}{\ell}\Bigr)
 \ll\frac{N}{(\log N)^{1+\kappa}} .
\]

The moduli are `4h-1∈{3,7,11,15,23,35,47,71,143}`. For `dist>2`, the branches
are the nine H-branches, giving `κ=κ_2`. For `dist>5`, each modulus is used
twice, by H(h) and X(h), giving `κ_5`. ∎

**Remarks.**

* The case `h=1` alone gives exponent `3/2`: `(3p+1)/4` has only prime
  factors `≡1 (mod 3)`. This is the half-dimensional sieve in the shape of
  Dahan (arXiv:2608.24035) Thm 4.14. Equivalently, `(3p+1)/4` is
  *primitively* represented by `x²+xy+y²`. A matching lower bound would need
  FHRSS-type input (arXiv:2504.20289); it is not claimed.
* These bounds are far weaker than the ES exceptional-set bounds of
  DISCOVERIES.md (A): `N exp(-c(log N)^{2/3}…)` unconditionally, and
  `exp(-c(log N)^{3/4})` internally. Bounded seed distance is a much more
  restrictive certificate than an arbitrary ES solution. By Theorem 2 it can
  only ever have a polylogarithmic, not a quasi-polynomial, saving: under
  Bateman–Horn the exceptional set is `≫_k N/(log N)^{C_k}`.
* **Open.** Does the exponent `c_k` tend to infinity? For `t≡0 (mod 6)`, a
  constant chart edge `(a,h)` is forced for *every* such t iff
  `e=4ah-a-h` divides `gcd_{t∈6Z}(t+a)² = gcd(a,6)²`. For nonzero a,h,
  `|e|≥3|a|-1` and `|e|≥3|h|-1`, so `|a|,|h|≤12`. Exhausting this finite
  range, indeed `0<|a|≤10^5`, gives **no off-axis solution** (`h≠0`). This
  is PROVED. On the other axis,
  `a=0`, the forced edges are exactly `h|36`. Thus, for the whole class
  `p≡1 (24)`, the forced constant anchors at the first levels are just the
  axis values `a,h|36` used above. Finer classes, e.g. `t≡2 (mod 4)`, give a
  few more, such as `(c,d)=(2,16)`. If only boundedly many constant anchors
  are forced at every depth, the heuristic exponent stays bounded; this
  suggests, but does **not** prove, that `c_k` is bounded. **CONJECTURE/heuristic.**

## 5. Search for depth ≥4 (EVIDENCE; in progress)

The pipeline is exhaustive for depth ≤3:

* `scripts/depth3_sieve.cpp` runs the exact criterion (9) for
  `t=sq`. It uses a-intervals for large h, and full 64-bit factorizations
  otherwise.
* `scripts/depth3_batch.py` runs families A and B on the survivors, using
  `depth3.py`. The verdict `>=4` requires certified factorizations. Primes
  above `2^64` get a Pocklington certificate.

| family | range | fail (9) | dist 3 | dist ≥4 |
|---|---|---|---|---|
| `t=6q`, all q (q, 24q+1 prime) | `q≤10^8` | 217 | 217 | 0 |
| same | `10^8<q≤10^10` | 5304 | 5304 | 0 |
| same | `10^10<q≤10^11` | 25232 | 25232 | 0 |
| `t=6q`, p a residue mod 5 and 7 (lossless by Lemma 4(5)) | `10^11<q≤10^13` | running | | |

For `q≤10^9`, the class-restricted sieve (`hard`) reproduces the unrestricted
survivor list exactly (1054 primes, identical sorted output).

Among the 5304 survivors with `q≤10^10`, the number of distinct productive
A/B anchors has median about 14. The minimum is 2, attained twice.

## Replay

```sh
cd scripts
(ulimit -v 8000000
 timeout 600 uv run python depth3_check.py            # regression checks
 timeout 900 uv run python depth3_validate.py 13 30000 --jobs 8
 timeout 600 uv run python depth5_branches.py 13 3000000
 timeout 60  uv run python depth3.py --all 297049)
g++ -O3 -march=native -std=c++17 -pthread -o /tmp/d3sieve depth3_sieve.cpp
/tmp/d3sieve 6 1 1000000000 8 hard > /tmp/surv.txt    # (9)-survivors, t=6q
uv run python depth3_batch.py /tmp/surv.txt --jobs 8   # families A,B on survivors
```
