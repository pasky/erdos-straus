# The signed seed: two hubs and an arithmetic incidence model

**The seed-component conjecture remains open.** This continuation proves an
input-defined bridge, identifies the arithmetic types of denominator fibres,
and gives exact coordinates in which Type I positivity is a positive-quadrant
condition. It neither proves seed reachability of a positive vertex for every
prime nor finds a counterexample to that conjecture.

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

## 5. Exact checks and scope

The auxiliary claim that *all two-negative vertices belong to the seed
component* is false, even for primitive Type II vertices. At the hard prime
`p=1009`, the vertex `(-366267,-6054,242)` is isolated. The checker below
exhausts all three of its divisor fibres, independently of any height bound.
This is **not** a counterexample to the seed-component conjecture.

```sh
(ulimit -v 524288
 timeout 60s uv run python scripts/pointwise_seed_check.py
 timeout 60s uv run python scripts/pointwise_forms_check.py
 timeout 30s uv run python scripts/pointwise_incidence.py 297049)
```

The incidence enumerator stores an SPF array, actual vertices, and sparse
buckets used by the existing BFS; it keeps the `p≤300000` resource cap.
It reproduces the full old enumeration, including the 1143 vertices and
minimum distance 3 at `297049`. The tests also check (1), both full hub
fibres, the p-colours, coordinate reconstruction and positivity equivalence,
and (8). None of these finite checks supplies the missing universal exit.
