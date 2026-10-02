# Beyond exponent 3? The pair-codegree gap G_pair

Task O4. Labels follow the house rules. ES is not solved here or anywhere;
nothing below bears on whether `W(p)<∞`. Notation as in `POINTWISE_OMEGA.md`
(PO) and `POINTWISE_OMEGA2.md` (O2): `W`, atoms `(M,D)`, `A_M=(M+1)/4`,
survival, Settings 1.0/3.0/10.0, `Δ_O`, Lemmas 1.2, 10.1, 10.2, Theorem 10.3,
Lemma 11.2, Prop 11.4, §11.4 (G_pair).

**Status: work in progress (checkpoint 0).**

## 0. Plan and the two observations

G_pair (O2 §11.4) is a *circularity*: the support-truncation level L of
O2 Thm 10.3 is `≍` the total event mass Σ, the pair codegrees must be
`≲1/L`, and quarantining the `−4D` hubs as ordinary singles raises Σ by
more than L. Two observations break it.

1. **Decoupling (§1).** Prime-local forbidden classes need not be events of
   the truncated minorant. They can be imposed on the base measure by a
   separate Brun pure sieve, composed with the main minorant coefficient by
   coefficient. Their mass then costs only `O(S_hub)` in `log(M_1/μ)` and
   `O(S_hub)` extra primes per modulus. It does **not** enter the main
   truncation level. This is option (i) of G_pair.
2. **The hub classes are the small-height rationals (§2).** Every atom is a
   triple `(s,a,b)` with `4sab=M+1` and class `−a/b ≡ −4sa² ≡ −1/(4sb²)`
   mod M. Fixing two of `s,a,b` and letting the third run gives a class that
   is the same rational `−u/v` at every M of a progression mod `4uv`-ish.
   There are three such families (Prop 10.6's `−4d²` is one of them).
   Numerically, the heavy pairs are exactly classes `≡−u/v` with small `uv`.

What remains is an upper bound (Lemma B, §3) for pair codegrees of classes
that are *not* small-height rationals.
