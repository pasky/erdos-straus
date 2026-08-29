# Wave-16 hostile review: §46 endpoint bulk

## Verdict

**SOUND-AFTER-REPAIRS.** I found no analytic or bookkeeping gap in Lemma 46.1, Theorem 46.2, Corollary 46.3, Lemma 46.4, or `verify.py (as)`. The only repairs are status-register corrections required by §47: literal (40.28) and raw-count (37.19) are refuted, while the implication-antichain wall (47.16) replaces them. The pair estimates (40.19) and (37.27) remain **OPEN**.

## Graded checklist

| # | grade | finding |
|---|---|---|
| 1 | **CONFIRMED** | Block injectivity and progression occupancy are correct. Same-block cross-cell terms vanish when `p>W` for `(W,2W]` (hence certainly when `p>2W`), but inter-block terms need not vanish. §46 does not lose them: global prefix/wedge bounds include them, (46.13) retains every residual pair, Failure log 46.5 identifies them, and `(as)` records them in the far corner. |
| 2 | **CONFIRMED** | The supported-cell counts, all `W/p+1` uses, the global cell-diagonal proof, and the optimization to `W1 ~ L^5 loglog L/(log L)^2` check out. The diagonal estimate is uniform over the full prime range and is independent of, not double-counted with, Theorem 42.2. |
| 3 | **CONFIRMED** | The `1/C` large-`c` diagonal gain and the resulting scope `c>=z, m<=zW1` are valid. The proof does not claim the false stronger tail `m>zW1`; (46.17) correctly explains why the incidence mass does not have the same `1/C` gain. |
| 4 | **CONFIRMED** | (46.13) is exactly equivalent, at `O(Lambda^2)` level, to (40.19) after the proved region and global diagonal are removed. Mixed proved/open collisions are controlled by the two-vector inequality and do not leak out of the equivalence. |
| 5 | **CONFIRMED** | `(as)` uses the same least representative, prime-implied deletion, roughness, endpoint, and `kappa` conventions as `(ao)/(ar)`. Its five ordered rational corners resum exactly and its implementation is streaming by residue bucket, with no incidence Cartesian array. The fresh full default run is green and reproduces the printed default table. |
| 6 | **REPAIRED** | Status lines in §§37, 40, 42, 45, and 46 now point to §47 and distinguish the refuted unreduced hierarchy from open antichain wall (47.16). Every repair is flagged `(wave-16 review repair)`; §46 still states (40.19)/(37.27) are **OPEN**. |

## 1. Injectivity and inter-block bookkeeping

For a prime `p` and a dyadic block `(W,2W]`, define

\[
 N_p(a;W)=\#\{m:W<m\le 2W,\ G_{m,p}>0,\ m\equiv a\pmod p\}.
\]

The full integer interval contains at most

\[
 N_p(a;W)\le \left\lfloor {W\over p}\right\rfloor+1.
\]

Consequently `p>W` already gives `N_p<=1`; the requested `p>2W` condition is more than sufficient. For a bucket with coefficients `g_1,...,g_n`,

\[
 \left(\sum_jg_j\right)^2-\sum_jg_j^2
 \le (n-1)\sum_jg_j^2
 \le {W\over p}\sum_jg_j^2.
\]

This is precisely (46.14). It proves only an intra-block statement. Cells from `(W,2W]` and `(W',2W']` can differ by a multiple of `p`, even if both blocks are separately injective. The section handles that honestly:

* Theorem 46.2 applies occupancy to the whole prefix `[1,T]`, not block by block, so all inter-block pairs internal to either closed prefix/wedge are included.
* The proved union in (46.11) is bounded by the residue-vector inequality `(x+y)^2<=2x^2+2y^2`, which also controls intersections and mixed pairs between its two pieces.
* The open set `B` in (46.13) is not dyadically restricted. Its ordered sum contains both same-block and separated-block collisions.
* Failure log 46.5 explicitly refuses to promote Lemma 46.4 to a global dyadic sum.
* In `(as)`, `open-local` is `sum_j[(sum block_j)^2-sum block_j(g^2)]`, while `open-far` is `(sum all open)^2-sum_j(sum block_j)^2`; these are respectively all ordered same-block and all ordered different-block cross-cell pairs.

There is therefore no hidden use of cross-block injectivity.

## 2. Occupancy, diagonal, and the `W1` optimization

For a prefix, the analogous exact bound is

\[
 \#\{1\le m\le T:m\equiv a\pmod p\}\le T/p+1.
\]

Cauchy in each bucket gives

\[
 \mathcal V(\mathscr A(T,C))
 \le \sum_p{1\over p}(1+T/p)
       \sum_{m\le T,c(m)\ge C}G_{m,p}^2
 \le (1+T/z)\mathcal D(\mathscr G_C).
\]

This includes the difficult `p<=2W` corner: no injectivity is asserted there, and its multiplicity is paid explicitly through `1+T/p` or `W/p`.

For the global diagonal, all cofactors in one `(m,p)=(4c^2s,p)` cell lie in one progression modulo `4c`, so

\[
 G_{4c^2s,p}\le {2\over z}+{L\over2c}.
\]

Using `G^2<=G(2/z+L/(2c))` and expanding one copy of `G` gives exactly

\[
 \mathcal D(\mathscr G_C)
 \le {2\over z}\sum_{i:c_i\ge C}{\kappa_i\over M_i}
 +{L\over2}\sum_{i:c_i\ge C}{\kappa_i\over M_ic_i}.
\]

A retained atom has at most `omega(M)<=L/log z` endpoint orientations. The zero-charge bound `sum_{M,D}1/M << L^3/log z` therefore yields

\[
 \sum_i{\kappa_i\over M_i}\ll {L^4\over(\log z)^2}.
\]

For the second sum, write `M=4Rc-1>=3Rc`, count `s|rad(R)`, and safely enlarge the actual range `R<=(X+1)/(4C)` to `R<=X`:

\[
 \sum_{i:c_i\ge C}{\kappa_i\over M_ic_i}
 \ll {L\over\log z}
      \sum_{R\le X}{2^{\omega(R)}\over R}
      \sum_{c\ge C}{1\over c^2}
 \ll {L^3\over C\log z}.
\]

This recovers (46.3). The argument uses no subdivision of `p`, so it is uniform for every endpoint prime `z<p<=X/z`. It also does not invoke Theorem 42.2: that theorem bounds full energy in a prescribed fixed-`s` fibre, whereas Lemma 46.1 bounds the all-`s` cell diagonal. No term is added twice.

With `C=1`, the leading prefix cost for `T>>z` is

\[
 {T\over z}{L^4\over\log z}.
\]

Equating it to `Lambda^2=L^6/(log L)^2` gives

\[
 T\asymp z\,{L^2\log z\over(\log L)^2}
 \asymp {zL^2\over\log L}
 \asymp {L^5\log\log L\over(\log L)^2}=W_1.
\]

The second term of (46.9) is smaller. Thus the claimed gain over `W0~L^3/(log L)^2` comes from combining global Frobenius control with bucket occupancy; it does not come from pretending that all larger blocks are injective.

## 3. Large-`c` wedge

The relation `pq=4Rc-1<=X` does force `R<=(X+1)/(4c)`, but merely truncating the harmonic `R,c` mass does not create a useful power saving. The actual `1/C` comes from the additional `1/c` in the pointwise cell bound, making `sum_{c>=C}c^{-2}<<1/C`.

From (46.9), the leading large-`c` condition is

\[
 {T\over z}{L^4\over C\log z}\ll\Lambda^2,
\]

or `T << C W1` up to fixed constants. At the claimed boundary `C=z`, `T=W2=zW1`,

\[
 {W_2\over z}{L^4\over z\log z}
 =W_1{L^4\over z\log z}\asymp\Lambda^2.
\]

The other term is `O(L^6/(log L)^3)`, below the target. Hence the proof gives exactly `c>=z, m<=zW1`. It does not reach residual cells with `m>zW1`, even when `c>=z`.

## 4. Exactness of (46.13)

The sets in (46.11) partition all endpoint cells. The proved side has `V(A)=O(Lambda^2)`. Positivity gives `V(B)<=V_end`, while

\[
 V_{\rm end}\le2V(A)+2V(B).
\]

Therefore `V_end=O(Lambda^2)` if and only if `V(B)=O(Lambda^2)`. Next,

\[
 V(B)=D(B)+C_{\rm bulk},\qquad
 0\le D(B)\le D(G_1)=o(\Lambda^2).
\]

Both directions now follow by nonnegativity. The mixed `A`--`B` term is not in (46.13), but it is not leakage: once `V(A)` and `V(B)` are bounded, Cauchy bounds it through the displayed two-vector inequality. Conversely, a bound for the full endpoint immediately bounds the positive subenergy `V(B)` and hence `C_bulk`.

## 5. Computational audit

`check_as()` independently rebuilds the endpoint matrix with the same conventions as `(ao)` and `(ar)`:

* least `D` in each intrinsic residue fibre;
* deletion when the projected class is prime-implied;
* composite `z`-rough `M=3 mod 4`;
* the same conditioned `kappa` product through `Y`;
* endpoint orientation `c<p`, with `q=M/p>z`, `q<4R`;
* unique `m=4c^2s` and coefficient `G[m,p]+=kappa/q`.

It buckets by `(-m^{-1} mod p)`, so division by `p` reproduces the endpoint mass `kappa/(pq)`. Its five pieces are `A^2`, ordered `2AB`, aggregated-cell `D(B)`, ordered same-block cross-cell pairs, and ordered different-block cross-cell pairs. Their exact rational sum is asserted against the independently fixed `(ar)` total.

Fresh command:

```text
uv run --with sympy,numpy,scipy python verify.py
```

Result: **all checks passed**, elapsed `1:51.85`, maximum resident set `329768 KB`. The three default `(as)` rows exactly match (46.7). The code stores retained maps, coefficient rows, and residue buckets; it forms no incidence-pair or Cartesian array. `ES_FULL_SCAN=1` was skipped because the harness has no selective-block entry point and that flag activates unrelated full scans as well.

The control-byte scan of `notes.md` reports zero. `verify.py` was not modified; the full run includes its own `ast.parse` checks.

## 6. Register repairs

The in-place repairs explicitly state:

* (40.19) and (37.27) remain **OPEN**;
* literal (40.28) and raw-count (37.19) are **REFUTED** by §47, not open;
* implication reduction preserves the void, and (47.16) is the replacement **OPEN** wall;
* proving (40.19) would not by itself prove (47.16), (33.16), or `H_PF'`.

No theorem statement or computational code required repair.
