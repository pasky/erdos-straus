# POINTWISE_WINDOW2 — two windows (`a_min(p)≥11`) beyond EH; the parity question as a theorem

Task O29 (branch `side-agent/window-parity`). Builds on `POINTWISE_WINDOW.md`
(Thm W1, Thm W2, Lemma 1.2, §§6–7) and `POINTWISE_SIZE.md` §§8–11.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
**Model-PROVED** = proved inside an explicitly defined axiomatic model (§3),
not a statement about the primes.

Status: in progress.

## 0. Results at a glance

(filled in at checkpoint)

## 1. Exact form of the two-window problem

Throughout, p is a Mordell-hard prime, so `p≡1 (24)` and `(p/3)=(p/7)=+1`
(the six Mordell classes mod 840 are squares mod 3, 7 and 8).
`n_3=(p+3)/4`, `n_7=(p+7)/4`, so **`n_7=n_3+1`** (consecutive integers; in
particular `gcd(n_3,n_7)=1`).

**Lemma 1.1 (PROVED).** For hard p, `a_min(p)≥11` iff windows 3 and 7 both fail.
Window 3 fails iff `n_3` has no prime factor `≡2 (3)` (POINTWISE_WINDOW §1).

**Lemma 1.2 (norm-form reformulation; PROVED).** For hard p the F1-failure of
both windows ("both clean") is equivalent to: `n_3` is primitively represented by
`a²+ab+b²` and `n_3+1` is primitively represented by `c²+cd+2d²`.
So "both clean" ⟺ `p=4n−3` with `(n, n+1)` a pair of consecutive integers
which are norms of primitive elements of `Z[ω]` and `Z[(1+√−7)/2]`, i.e. an
integral point of the quaternary quadric
`c²+cd+2d² − (a²+ab+b²) = 1` with `4(a²+ab+b²)−3` prime.

*Proof.* Both fields have class number 1. A prime r is inert in `Q(√−3)` iff
`r≡2 (3)` (including r=2), and inert in `Q(√−7)` iff `(r/7)=−1` (2 splits since
`−7≡1 (8)`). A positive integer coprime to the discriminant is a primitive norm
iff it has no inert prime factor. `3∤n_3` and `7∤n_7` because `p≡1 (21)`. ∎

This is exactly the shape of Friedlander–Iwaniec's hyperbolic PNT (FI09,
archived now: `sources/window2/fi09-hyperbolic-pnt.{pdf,txt}`), where
`p∓2` are sums of two squares, i.e. `x_1²+…+x_4²=p` on the quadric
`x_1x_4−x_2x_3=1`. FI09's lower bound needs level `θ<1` close to 1;
Sedunova 2026 (arXiv:2609.28200, archived) confirms it is still open
unconditionally and gets only `P_7` (square-free distances, ≤7 prime
factors) from the unconditional level `x^{1/6}` of `r(n−2)r(n+2)`.
The best unconditional "one complete absence + one almost-prime" result is
Nath–Xie (arXiv:2501.16723, archived): `p=m²+n²+1` with `Ω(p+2)≤9`, by a
semi-linear × linear vector sieve.
