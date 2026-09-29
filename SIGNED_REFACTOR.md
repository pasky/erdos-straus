# The signed seed: two hubs and an arithmetic incidence model

**The seed-component conjecture remains open.** This continuation proves an
input-defined bridge, identifies the arithmetic types of denominator fibres,
and gives exact coordinates in which Type I positivity is a positive-quadrant
condition. The latest deductions bound Type II fibres by two vertices and
remove large p-free denominators from any putative sterile transmitting core.
They neither prove seed reachability of a positive vertex for every
prime nor find a counterexample to that conjecture.

Throughout, `p=4t+1` is prime. **Type I means one p-divisible denominator;
Type II means two.** Denominators are signed, nonzero integers. The original
graph joins distinct unordered triples sharing a denominator.

## 1. The seed reaches both unit-residual hubs

There is an unconditional three-edge path

\[
\begin{split}
 &(t,-2pt,-2pt),\\
 &(t,-t(p+1),-pt(p+1)),\\
 &(2t,2t+1,-pt(p+1)),\\
 &(2t,2t,-pt).
\end{split}                                                    \tag{1}
\]

The shared denominators are respectively `t`, `-pt(p+1)`, and `2t`.
Every row sums reciprocally to `4/p`; for the middle bridge use
`2t+1=(p+1)/2`. Consequently the seed component contains the **entire fibres**
at both `t` and `-pt`, with residuals `-1/(pt)` and `1/t`.

These are the only integral anchors whose reduced residual numerator is
`+1` or `-1`. Such an anchor would complete an integral two-term identity,
and

\[
 4/p=1/u+1/v\quad\Longleftrightarrow\quad
 (4u-p)(4v-p)=p^2.
\]

Both factors are `3 mod 4`. The only possibilities are negative divisors
`-1,-p,-p²`; the middle choice gives zero denominators, and the others give
`{u,v}={t,-pt}`. Thus (1) reaches every integral three-term refinement of
**either term** of the unique signed two-term identity

\[
                       4/p=1/t-1/(pt).
\]

For `T=τ(t²)`, the two fibres have exactly `3T` and `T` vertices, respectively,
and are disjoint. Indeed, unordered decompositions of `±1/s` correspond to
signed divisors of `s²`, modulo complementary-divisor exchange. Excluding
zero denominators removes the divisor `-s`; the divisor `+s` is the remaining
fixed point. The count is `τ(s²)`, and `τ((pt)²)=3τ(t²)`.

All vertices in these two fibres are nonpositive. Their abundance alone
is not an exit argument.

## 2. The p-adic colours are rigid

**Lemma.** Every signed vertex has exactly one or two p-divisible
denominators, each with valuation exactly one at p.

Clearing denominators shows that at least one is p-divisible. If all three
were, multiplication by p would express 4 as a sum of three reciprocals of
nonzero signed integers, each at most 1. With exactly one p-divisible
coordinate, its valuation must be one. With two, unequal valuations would
leave an uncancelled valuation below `-1`; thus if either valuation exceeds
one, both do. Writing the remaining coordinate as x then gives

\[
 |4/p-1/x|\le 2/p^2.
\]

This forces `x>0` and `x≤p²/(4p-2)<p/2`, whence
`0<|4x-p|≤2x/p<1`, a contradiction.

For a p-divisible denominator `pm`, define its label

\[
                         \lambda(pm)=4m-1\pmod p.
\]

At a Type I vertex `(x,y,pm)`, reduction after multiplication by p gives
`4m=1 mod p`, so `λ=0`. At a Type II vertex `(x,pm,pn)` it gives

\[
                  (4m-1)(4n-1)=1\pmod p.                    \tag{2}
\]

In particular the two nonzero labels are inverse. **No p-divisible
denominator can be shared by the two types.** Type changes must preserve
a p-free denominator. The inversion orbit in (2) is preserved along a
Type II move retaining a p-divisible denominator, but is **not** an invariant
of a whole component.

The seed is the **only** Type II vertex with label 1. Indeed, label 1 gives
`m,n≡-2t mod p`, so `|m|,|n|≥2t`. The p-free coordinate x is positive because
`4=p/x+1/m+1/n` cannot hold with `x<0`. Hence

\[
                       |4-p/x|\le 1/t.
\]

For `x≤t`, equality is possible only at `x=t` with `m=n=-2t`; for `x≥t+1`,
`4-p/x≥3/(t+1)>1/t`. This proves uniqueness. In particular `-2pt` occurs
in **no other vertex**: every nontrivial first move preserves t.

### Quadratic colour detects positivity exactly

**Attribution (see [LITERATURE_2026.md](LITERATURE_2026.md) §1).**

* **Theorem (2a) is not new.** It is Bright–Loughran, *Brauer–Manin
  obstruction for Erdős–Straus surfaces*, Bull. LMS 52 (2020),
  arXiv:1908.02526, Theorems 1.2 and 1.5 (p. 2), specialised to `n=p`.
  Their Lemma 3.4 (p. 11) evaluates the local invariant. Combining these
  with the signed valuation lemma above gives (2a).
* **The positive direction** goes back to Yamamoto (1965), per BL
  Appendix A.
* **The labels λ and the §8 chart symmetry** are Elsholtz–Tao coordinates
  (arXiv:1107.1010, equations (2.1), (2.7), (2.18) and (2.21)), on positive
  points.
* **The Type I/II rigidity** is Jiang, arXiv:2609.09204v1, Thm 3.2, in the
  positive case. Jiang's v2 is withdrawn.

What follows is a self-contained elementary proof, not a priority claim.

**Signed character theorem.** Select the two coordinates with the same
p-adic valuation, and remove their factors of p if necessary. Call the
resulting integers A,B. Then

\[
 \left(\frac{AB}{p}\right)=
 \begin{cases}
 -1,&\text{the triple is all-positive},\\
 +1,&\text{the triple has a negative denominator}.
 \end{cases}                                                \tag{2a}
\]

Thus A,B have opposite quadratic characters **exactly** in the positive
case. This is not a character heuristic for arbitrary integer triples;
it uses the exact signed ES identity.

**Proof for Type I.** Write the p-divisible denominator as pm and put
`u=|m|`. The residual is `R/u`, with R positive. If `m>0`, then
`R≡3 mod4` and `4u-pR=1`; if `m<0`, then `R≡1 mod4` and `pR-4u=1`.
Quadratic reciprocity gives, for each prime `ell|u`,

\[
                  (\ell/R)=(\ell/p).
\]

For odd ell, use `-R≡p^{-1} mod ell` in the first case and
`R≡p^{-1} mod ell` in the second. For ell=2, reduction modulo 8 gives the
same equality. Jacobi symbols with denominator 1 have value 1.
For the two p-free coordinates x,y, put `D=Rx-u`. Then
`D|u²`, `D≡-u mod R`, and `Dy=ux`. Also `(u/p)=1`, since
`m≡1/4 mod p` and `(-1/p)=1`. Consequently `(xy/p)=(D/p)`.

If `m>0,D>0`, both x,y are positive, and
`(D/p)=(D/R)=(-u/R)=-1`, since `4u≡1 mod R`.
If `m>0,D<0`, write `d=-D`; then `d≡u mod R`, giving
`(D/p)=(d/R)=1`. These are the mixed-sign pairs. If `m<0`, both signs
of D give character +1: here `(-1/R)=1` and `4u≡-1 mod R`.
This proves (2a) for Type I.

**Proof for Type II.** At a positive p-divisible denominator `pu`, the
residual is `(4u-1)/(pu)`. Its factor corresponding to the p-free coordinate
is a signed divisor D of `u²`, satisfying `D≡-pu mod(4u-1)`.
Every prime factor of u has Jacobi symbol +1 modulo `4u-1`.
For an all-positive vertex D is positive, so
`1=(-pu/(4u-1))=-(p/(4u-1))`. Reciprocity gives
`(lambda(pu)/p)=-1`.

A nonpositive Type II vertex has a negative p-divisible coordinate `-pu`.
Now the residual numerator is `4u+1`. Every signed divisor of `u²` has
Jacobi symbol +1 modulo `4u+1`; hence its required congruence gives
`(p/(4u+1))=1`, and therefore `(lambda(-pu)/p)=1`.
Finally (2) implies `n lambda(pm)=m mod p`, so
`(lambda(pm)/p)=(mn/p)`. This proves (2a) for Type II. ∎

**Graph consequence.** A Type II p-divisible bucket is entirely positive
or entirely nonpositive according as its nonzero label is a nonresidue
or residue modulo p. Thus a Type II move retaining a p-divisible denominator
**cannot cross the positivity boundary**. This is stronger than invariance
of the inversion sector alone. Type I buckets need not have this property.

## 3. An exact bipartite denominator graph

Use two sets of nodes:

* a signed p-free denominator `x`;
* a signed nonzero integer `m`, prime to p, representing the denominator `pm`.

Join them precisely when

\[
 f=(4x-p)m-x\ne0,\qquad f\mid px^2.                         \tag{3}
\]

The corresponding triple is

\[
                         (x,pm,pxm/f).                     \tag{4}
\]

**Retain only nodes incident to at least one edge.** An unused denominator
is not a graph component: for example, the eligible value `p=5,x=-1`
has an empty fibre. This qualification is necessary for the component
correspondence below.

**Proof of exactness.** Put `q=4x-p`. Since `gcd(q,x)=1`, also
`gcd(q,f)=1`. The relation `qm=f+x` shows that
`f|pxm` is equivalent to `f|px²`. Thus (3) gives integral nonzero (4),
and its reciprocal identity follows directly. Conversely, every vertex
has a p-free and a p-divisible coordinate by §2, and their remaining
coordinate forces (3).

Each original triple gives a connected star of one or two incidence edges.
Each incidence edge determines its triple uniquely. Therefore **components
of this bipartite graph correspond exactly to components of the original
refactor graph**: a walk in either graph converts to a walk in the other,
possibly with repeated triples. Edge distances need not be preserved.

The incidence is Type I precisely when `p|f`, since the third coordinate
in (4) is then p-free. This is equivalent to `λ(pm)=0`. Otherwise it is
Type II. A positive triple corresponds exactly to

\[
                             x>0,\quad m>0,\quad f>0.       \tag{5}
\]

### A sharper complete enumeration bound

Every vertex has a **positive p-free denominator `x≤2t=(p-1)/2`**.

For Type II, `4=p/x+1/m+1/n` forces `x>0` and `p/x≥2`, so `x≤2t`.
For Type I, write

\[
 m=ph-t,\qquad R=4/p-1/(pm)>0.
\]

If `m<0`, then `R>4/p`. If `m>0`, its residue class forces
`m≥3t+1`, so `R≥3/(3t+1)`. The positive terms among the two p-free
reciprocals sum to at least R, so one of their denominators is at most
`2/R`. In the two cases this is respectively less than `p/2` or at most
`2t+2/3`; its integrality proves the bound.

Thus the entire graph can be independently enumerated by (3), taking

\[
 1\le x\le 2t,\qquad f=\pm p^j d,\quad j\in\{0,1\},\quad d\mid x^2.
\]

Retain integral nonzero `m=(x+f)/(4x-p)` and reconstruct (4). This restricts
only the **chosen** anchor, not the other coordinates. It is an exact
finite enumeration, not a height-limited search.

## 4. Type I becomes a positive-quadrant problem

For a Type I incidence set

\[
 x=t+a,\qquad m=ph-t,\qquad e=(4a-1)h-a=4ah-a-h.
\]

The residual at `pm` is `(4h-1)/(ph-t)`, and
`4(ph-t)-p(4h-1)=1`: these are coprime determinant-one coordinates, even
when signs change. Also `f=pe`, so the complete integrality condition is

\[
 e\ne0,\qquad e\mid(t+a)^2,\qquad x\ne0,\quad p\nmid x.    \tag{6}
\]

The corresponding Type I triple is

\[
 \left(t+a,\;p(ph-t),\;\frac{(t+a)(ph-t)}{e}\right).         \tag{7}
\]

For admissible coordinates, **(7) is positive if and only if `a≥1,h≥1`**.
The forward implication follows from `x>p/4` and `pm>0`. Conversely,
`a,h≥1` imply `e≥3a-1>0`, so all three entries are positive.

This is a bipartite coordinate chart: retaining a p-free denominator
retains a, and retaining the p-divisible denominator retains h. It models
the Type I subgraph, not the Type II transfers as well.

The seed unconditionally reaches two explicit divisor sets on its axes:

\[
 \begin{array}{ll}
 a=0:& h=\pm d,\quad d\mid t^2,\ d>0,\\
 h=0:& a=\pm d,\quad d\mid t^2,\ d>0,\ a\ne-t.
 \end{array}                                                \tag{8}
\]

The first row is exactly the Type I part of the t-fibre; here `e=-h`.
The second is the `-pt` fibre; here `e=-a` and
`a|(t+a)²` is equivalent to `a|t²`. Its nonzero complementary pair cannot
contain a p-divisible entry: otherwise both entries would be divisible
by p, contradicting `1/t>2/p`. Thus the p-free condition introduces no
further exclusions in the second row.

In these coordinates the bridge between the axes is explicit:

\[
 (a,h)=(0,-t)\ \longrightarrow\ (t,-t)\
                         \longrightarrow\ (t,0),
\]

retaining first h, then a. The Type II seed attaches at `a=0`.
This reaches both axes without assuming any positive witness.

**The missing transfer theorem.** One must force the component generated
by (8), allowing the actual Type II incidences (3), to reach (5).
For a Type I exit this means an admissible edge in the positive quadrant
of (6). Merely counting axis divisors does not do it; nor does the
symmetry of `e=4ah-a-h` imply symmetry of the divisibility condition, whose
right side is `(t+a)²`, not `(t+h)²`. No unproved transposition is being
used as a graph move. This is the current constructive foothold, not a
replacement conjecture asserting a uniform path-length bound.

### Exactly which two-move seed exits are possible

The character theorem removes the Type II branch from this question.
Every first move preserves t (§2); t is too small to occur in a positive
vertex. A positive p-divisible denominator at a first-step Type II vertex
has a residue label, so its entire bucket is nonpositive. At a first-step
Type I vertex the only possible retained positive exit denominator is
`p(ph-t)`, with `h>0` and `h|t²`. Thus **a two-move seed exit exists if and
only if**, for some positive divisor h of t², the rational number

\[
                         \frac{4h-1}{ph-t}                  \tag{9}
\]

has a positive integral two-term decomposition. This is an exact reduction
for every prime `p=4t+1`, not just for the sparse-seed experiments.

A useful legal excursion in the other direction is also explicit. Choose

\[
 c>0,\quad c\mid t^2,\qquad d>0,\quad d\mid(pc+t)^2,
 \qquad d\equiv-c\pmod{4c+1}.
\]

Put `a=(d+c)/(4c+1)`. The path from the seed to Type I coordinates
`(0,-c)` and then `(a,-c)` consists of two legal edges. Its new positive
p-free denominator is `t+a`; its p-divisible denominator remains negative.
A further character-mismatching refactor would necessarily be positive by
(2a). The transfer itself does **not** guarantee that mismatch.

## 5. Rigidity of transmitting fibres

These bounds hold for every prime `p=4t+1`. They give exact pruning and
factorization-free moves, **not a reason that the remaining core must exit**.

### Type II fibres have at most two vertices

Fix a Type II denominator `pm`, and write the other two coordinates as
`x,pn`. Put `K=4m-1` and `A=4-1/m≥3`. The identity gives

\[
 nK\equiv m\pmod p,\qquad x=\frac{p}{A-1/n}.
\]

There is exactly one representative `n₀` of this nonzero residue class in
`[-2t,2t]`. Every other representative has `|n|≥2t+1=(p+1)/2`. For those
representatives, with `η=2/(p+1)`,

\[
 \left|x-\frac{pm}{K}\right|
 \le\frac{p\eta}{A(A-\eta)}
 \le\frac{2p}{9p+3}<\frac14.
\]

Thus all noncentered representatives force the **same** integer x: the
nearest integer to `pm/K`. Each x determines n uniquely. Together with the
centered representative, this gives at most two vertices in the entire
fibre, whether positive or nonpositive.

This is also a complete factorization-free construction. Test exactly:

1. `n=n₀`, with `x=pmn/(4mn-m-n)` integral;
2. `x=nearestInteger(pm/K)`, with `D=Kx-pm≠0` and `D|m²`, giving `n=mx/D`.

Discard inadmissible candidates and deduplicate. The second divisibility
condition is sufficient because `gcd(K,m)=1`; from `D=Kx-pm`, it follows
that `D|mx` whenever `D|m²`. This does not presume that the two divisors of
a double fibre have ratio `4m`: at `p=6089,m=-60`, the actual factors
`D=-16,225` are a counterexample to that tempting strengthening.

**Moreover, `|m|≥2t` makes the denominator private.** If both quotients
satisfy `|m|,|n|≥2t`, then `|1/m+1/n|≤1/t`. For `x≥t+1`,
`4-p/x≥3/(t+1)>1/t`, impossible. For `x≤t`, the opposite gap is at least
`1/t`, with equality only at the seed `x=t,m=n=-2t`. Hence the partner of
any fixed large m lies in `[-2t,2t]`, where its residue class has only one
representative.

Consequently the Type II graph using **only p-divisible retained
coordinates** has components of at most three vertices: an isolated
vertex, an edge, or a three-vertex star. A nontrivial block has a central
vertex with both quotients in `[-2t,2t]`; each outer vertex has a large,
private quotient. This bound does not apply after allowing moves retaining
p-free coordinates. By the signed character theorem, each such block is
wholly positive or wholly nonpositive.

### P-free denominators outside the small interval cannot hide a chain

Fix a p-free denominator `z<0` or `z>2t`. Type II is impossible there.
The other p-free denominator x is positive and at most `2t`, and the
remaining coordinate is `pm`, with `m≤-t` or `m≥3t+1`. Put
`R=4/p-1/z`. Every possible x lies in the exact interval

\[
 \frac1{R+1/(pt)}\ \le x\ \le\frac1{R-1/[p(3t+1)]}.       \tag{10}
\]

Each integer in (10) determines the last denominator; testing its
integrality exhausts the fibre without factoring z.

* For `z<0`, `R>4/p`, so the interval width is less than `1/3`:
  **the entire fibre is empty or a singleton**.
* For `z>2t`, use `R≥(4t+3)/(p(2t+1))`. The width is at most
  `(2t+1)²/((t+1)(3t+2))<2`, so there are **at most two vertices**.
* For `z≥p`, the stronger `R≥3/p` makes the width at most
  `p²/((3t+1)(9t+2))<1`: the full fibre is again empty or a singleton.

**Update (WINDMILL.md §2.7, Theorem 7, proved):** for `2t<z<p` the fibre
is also empty or a singleton. So every p-free denominator outside `[1,2t]`
lies in at most one signed vertex.

For a **nonpositive** vertex with `z>2t`, both p-free coordinates are
positive, so `m<0`. The upper endpoint in (10) improves to the strict
bound `x<1/R`. This interval has width at most

\[
 \frac{(2t+1)^2}{(4t+3)(t+1)}<1.
\]

Thus there is at most one nonpositive vertex at any such z. In particular,
**starting from a nonpositive vertex, a move retaining a p-free z outside
`[1,2t]` either is impossible or immediately reaches positivity**. This subsumes the large p-free
singleton calculation in terminal square-lift examples; growing that
coordinate cannot create a long hidden signed escape route.

### Exact lazy exhaustion, with unknown status kept separate

`scripts/pointwise_fibres.py` implements these constant-candidate fibres.
At a Type I p-divisible anchor it additionally uses

\[
 |a|\le\left\lfloor\frac{4t^2+|h|}{|4h-1|}\right\rfloor,
 \qquad 1-t\le a\le t,
\]

which follows from `|(4h-1)a-h|≤(t+a)²≤4t²`. When short, this interval
exhausts **both signs** of the fibre; otherwise the search uses the full
signed-divisor equation. Fresh factors must be certified below `2^64`;
known factors may be stripped from larger integers first. Divisor and
vertex budgets are explicit, and partially processed fibres are never
cached as complete. Returned fibres are immutable, and public inputs must
be integers, including arbitrary start vertices.

The BFS emits `FOUND` with a shortest positive path, or `STERILE` only
when every denominator in the entire start component has been expanded.
Unsupported or budget-exhausted work is `UNKNOWN` (exit 2); an externally
interrupted run has no exhaustion verdict. Unused labels are not starts.
Tests compare every bucket against independent complete graphs, including
empty labels, and exhaust known nonseed sterile components, including the
nine-vertex cyclic one at `10477`.

**The existence gap is unchanged:** no closure contradiction for the seed
core, and no exhausted sterile seed component, has been obtained. The new
bounds remove entire classes of possible transmitting branches; they do
not supply a character-changing divisor in the remaining ones.

## 6. Exact checks and scope

The auxiliary claim that *all two-negative vertices belong to the seed
component* is false, even for primitive Type II vertices. At the hard prime
`p=1009`, the vertex `(-366267,-6054,242)` is isolated. The checker below
exhausts all three of its divisor fibres, independently of any height bound.
This is **not** a counterexample to the seed-component conjecture.

### Beyond the two unit fibres

A targeted sparse-seed search found `p=2271767935369`, with
`q=(p-1)/24=94656997307` also prime. There is **no positive vertex adjacent
to any vertex in either the t-fibre or the -pt-fibre**. Nevertheless there
is a three-edge seed escape. The negative-fibre transfer above uses

\[
                  c=4,\quad d=26^2,\quad a=40.
\]

It reaches the Type I vertex `(a,h)=(40,-4)`. Retaining `x=t+40` then gives
the positive Type II vertex

\[
 (567941983882,\;p\cdot3572092160,\;p\cdot98151160656640).
\]

Here `4x-p=159`, and the Type II divisor certificate is
`20669558=2*7*13*337²`, a divisor of `x²` congruent to `-x mod159`.
This last refactor enters a **nonresidue-labelled** Type II bucket, exactly
as (2a) requires. A second such example, `p=772045387369`, escapes using
`c=2,d=700`, reaching `a=78` before the positive step.

The checker exhausts the short-exit criteria, **not these entire large
graphs**. Thus it proves minimum seed distance 3 from (9) and the supplied
path. The -pt-fibre exclusion is not a claim about all two-edge paths
starting at the vertex `(-pt,2t,2t)`: such a path could first retain `2t`
instead of `-pt`. No uniform three-move conjecture is inferred.

For these sparse inputs `t=6q`, the divisors h in (9) are `c q^j`,
`c|36`, `j=0,1,2`. The largest ones need no huge factorization. In any
positive Type I pair choose `x=t+a≤2t`; then

\[
                0<e=(4a-1)h-a\le(t+a)^2.
\]

For `h≥q²`, we have `h>t` and `e-(t+a)²` strictly increases for `1≤a≤t`.
The checker tests each admissible a and stops only when this necessary
inequality fails. For `q≥13` it fails by `a=16`, since the difference there
is at least `27q²-192q-272>0`. All other h require only factorizations of
linear forms in q after removing the known factor q. The dual-fibre test
similarly factors `t+d`, `d|t²`, by removing known factors before working
on the remaining linear factor. Every fresh factorization is guarded
below `2^64`, where the primality checks are deterministic. Resource
limits or unsupported inputs are errors, never graph counterexamples.

These examples defeat direct exits from the two-fibre core, not the seed
conjecture. The character theorem supplies a sharper target: **force a
legal refactor with opposite quadratic colours on the same-valuation
pair**. It does not yet force the required integral divisor.

```sh
(ulimit -v 524288
 timeout 60s uv run python scripts/pointwise_seed_check.py
 timeout 60s uv run python scripts/pointwise_forms_check.py
 timeout 60s uv run python scripts/pointwise_escape_check.py
 timeout 60s uv run python scripts/pointwise_fibres_check.py
 timeout 30s uv run python scripts/pointwise_incidence.py 297049
 timeout 30s uv run python scripts/pointwise_fibres.py 297049)
```

The incidence enumerator stores an SPF array, actual vertices, and sparse
buckets used by the existing BFS; it keeps the `p≤300000` resource cap.
It reproduces the full old enumeration, including the 1143 vertices and
minimum distance 3 at `297049`. The tests also check (1), both full hub
fibres, the p-colours, coordinate reconstruction and positivity equivalence,
and (8). None of these finite checks supplies the missing universal exit.

## 7. Survey of seed-exit distances (finite evidence, 2026-09-26)

**Literature check (arXiv, through 2026-09-26).** No proof of Erdős–Straus
has appeared. The only recent "proof" claim (Dyachenko, 2511.07465) was
already audited (`reviews/external-auro-zera-lean-wave20.md`). New since the
last wave: 2609.09204 (counting Type I/II solutions; *does not address the
conjecture*; v2 since withdrawn). Its characters are conditional criteria
modulo `4n−p`, not (2a). (2a) itself is Bright–Loughran 2020; the comparison
is in [LITERATURE_2026.md](LITERATURE_2026.md) §1(b). 2608.16977's "Erdős–Straus" item is the unrelated
1977 binomial-divisibility question.

**Survey.** `scripts/pointwise_seed_survey.py` runs the exact lazy BFS from
the seed; `scripts/pointwise_two_move.py` tests the two-move criterion (9)
directly, and every certificate it returns is checked as an exact rational
identity, so no factorization certification is needed for FOUND.

| range | primes | distance 2 | distance 3 | ≥4 / sterile |
|---|---|---|---|---|
| all `p≡1 (4)`, `p<3·10^5` | 12980 | 12979 | 1 (`297049`) | 0 |
| `p≡1 (24)`, `3·10^5<p≤5·10^6` | 40244 | 40235* | 9 | 0 |
| `p=4kq+1`, `q` prime `>10^9`, `k=1,2,6` | 3×300 | all | 0 | 0 |

\* 1938 of these exceeded the BFS divisor budget (`UNKNOWN`) and were
settled by (9). The nine distance-3 primes are 513529, 710089, 1083289,
1103449, 1708009, 2469289, 3389929, 3942409, 4762489. Every distance-3 prime
found has `t=6q` or `t=6qr` with `q,r` prime (squarefree cofactor, so `t²` has few
divisors), matching the sparse-seed construction of §6.

**What the h=1 branch is.** For `h=1`, (9) is `3/(3t+1)`. Since
`3/n=1/y+1/z` with positive y,z is equivalent to a positive divisor
`D|n²` with `D≡-n (mod 3)`, it holds for `n=3t+1≡1 (mod 3)` **iff
`3t+1=(3p+1)/4` has a prime factor `≡2 (mod 3)`**. This fails for
3052 of the 12980 primes above; all ten distance-3 primes are among them.

**Assessment (not a theorem).** Each fixed-h branch of (9) is a
single-shift divisor-class condition of exactly the kind that has infinitely many
failures (cf. the `c=7` obstruction in 2608.24035, and notes §5/§9.3). A
bounded-depth proof of the seed conjecture would therefore need a covering
by the `τ(t²)` branches `h|t²` (plus depth-3 transfers) that works for every p. That
is a restricted form of the classical ES criterion, not an easier problem.
The survey supports "distance ≤3" as a working conjecture, but that
conjecture **implies ES for primes `p≡1 (4)`**, so it cannot be cheaper than ES itself.
A proof must use global structure of the seed component, not path length.

**Update (DEPTH3.md).** The depth ≤3 escapes are now classified exactly: (9),
negative-fibre transfers A, and Type II swaps B (Theorem 1). Every prime
`p≡1 (4)` below `10^12` has distance ≤3. But **under Schinzel's Hypothesis H the seed
distance is unbounded** (DEPTH3 Theorem 2): for every k, infinitely many
`p=24q+1` have an entirely nonpositive radius-k ball around the seed. This
turns the assessment above into a conditional theorem.

## 8. Looking for global structure: three candidates, none closes

The seed conjecture implies ES for all primes `p≡1 (4)`, so a proof must
create positivity globally. Three candidate mechanisms were tested.

**(i) Parity / Zagier-type counting.** For all 383 primes `p≡1 (4)` below
6000, each of the counts total, positive, nonpositive, and positive or
nonpositive Type I or Type II is odd about half the time. There is no free
parity invariant. A natural second involution also fails. At fixed x, divisor
complementation `f↦x²/f` on Type II incidences is exactly the swap of the two
p-divisible coordinates. On Type I incidences it sends the class `-1/4` to
`-p²/4 (mod 4x-p)`, so it leaves the set.

**(ii) Size.** Complete enumeration of all 3018 primes `p≡1 (4)` below
`6·10^4` (`scripts/pointwise_components_survey.py`) gives the following. Sterile
(positive-free) components have sizes 1…16, with counts decaying roughly
geometrically:
`194311, 25302, 4137, 1361, 598, 266, 169, 74, 66, 25, 16, 5, 3, 3, 2, 1`.
The largest is 16 vertices, at `30637`. The seed component always holds at
least 58% of all vertices, and its minimum size grows with p (304 in
`[2^14,2^15)`). The largest sterile size also grows, but slowly. 58699
non-seed components contain positive vertices. This suggests the clean
**size conjecture: every component with more than `K(p)=O(log p)` vertices
contains a positive vertex**. It is consistent with the data, but it is no
easier to prove than ES.

**Update: refuted in practice (see [SIZE_CONJECTURE.md](SIZE_CONJECTURE.md)).**
"Dead hubs" (an anchor `x=t-k` all of whose prime factors are `1 mod 4k+1`)
give certified sterile components of size about `3^r/2`. At
`p=274159709010072908384347957` a certified **30035-vertex sterile component
is larger than the certified seed component (10155 vertices)**, so no size
threshold can force seed exits. The asymptotic `O(log p)` form is not formally
disproved, since sterility of an infinite family is unproved. The 58% seed
share also does not persist (0.36 near `2^30`). The same file proves
**Lemma E (sign flip)**: an anchor `t+a` (`a>=1`) with a prime factor
`= -1 (mod 4a-1)`, or a Type I bucket `h>=1` whose `m=ph-t` has a prime
factor `= -1 (mod 4h-1)`, has an empty fibre or contains a positive vertex.

**(iii) Colour.** By (2a), a component is sterile iff every Type I vertex
satisfies `(xz/p)=+1` and every Type II vertex `(mn/p)=+1`. Each p-free
denominator carries a coin-like Legendre colour, so sterility requires many
coincidences at once. That explains the geometric decay in (ii), but only
heuristically. No colour invariant separates the seed component. On a
sample of `p∈[1000,12000]`, 3223 of 3543 sterile components contain
non-residue primes, and 67 contain p-free denominators of both colours. Every
seed component contains both colours, as do many sterile and positive
components.

**A symmetric form of the Type I chart (proved).** Put `A=4a-1`,
`H=4h-1`, `x=(p+A)/4`, `m=(pH+1)/4`, `e=(AH-1)/4`. Then `Hx=m+e` and
`gcd(H,e)=1` (since `AH-4e=1`), so

\[
 e\mid x^2 \iff e\mid m^2 .
\]

The integrality condition (6) is therefore symmetric between the two
coordinates of the chart: `e` must divide the square of either retained
denominator. In these terms (2a) reads: for `e|x²` with
`e≡-1/4 (mod 4x-p)`, `(e/p)=sign(e)`. The identity was checked on
`3·10^7` pairs `(a,h)`.

**Where this leaves the problem.** At every reachable anchor x, a positive
exit is the classical event "some divisor of `x²` lies in the class `-1/4`
modulo `4x-p`". Hub denominators are built from divisors of t, all of which
are residues mod p (`ℓ|t ⇒ (ℓ/p)=(p/ℓ)=1`). This is the principal-genus trap
of POINTWISE.md §2 in a new guise. Escape needs fresh primes from factoring
new shifts `t+a`, and controlling those factorizations for *every* p is
exactly the problem the exceptional-set machinery handles only on average.
None of (i)–(iii) supplies that control.
