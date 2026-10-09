# POINTWISE_MORDELL13D — closing exceptional root classes with a complete-witness hybrid DFS (task O103)

Status: work in progress (side agent O103, branch `side-agent/r13-hybrid-close`). Labels as in DISCOVERIES.md.
Continues POINTWISE_MORDELL13C (§6 Thm 6.1, §8 Comp 8.3 and plan).

## 1. The C complete-witness engine `scripts/m13d_wit.c`

Input: a node `x + Lℤ` (`4 | L`, `gcd(x,L)=1`, `L < 2¹²⁶`), optional `req` (a prime power exactly dividing L).
Output: all (or the first) ET classes (seven families, `mordell_lib` conventions) with modulus `M | L`
(and `req | M`) containing the node. Same mathematics as `m13c_witness.py` (13C §2), reorganised:

* **(A) II3 / I2 / I3** (`(a,d,f)` with `f` odd, `gcd(f,4ad)=1`, `M = 4adf | L`, `x ≡ −f (4ad)`): loop over odd
  `f | L`; then `m = 4ad` divides `G_f = gcd(L_f, x+f)`, `L_f` = part of L coprime to f; enumerate
  `a·d = Q | G_f/4` and test `f | x+4a²d` (II3), `f | ax+d` (I2), `f | x²+4a²d` (I3).
  Equivalent to 13C's loop (pairs (a,d), `f | gcd(K_c, ·)`, `f ≡ −x (4ad)`): both say `f·4ad | L`, `gcd(f,4ad)=1`.
* **(B) I1 / II1 / I4** (modulus `m = 4Q | L`): `f0 = −x mod m`, `g0 = −x⁻¹ mod m` (`x⁻¹` taken mod L).
  I1 `(a,d,f)`, `ad=Q`, `f | am+1`, `f ≡ −x (m)`: either `f = f0` or `g = (am+1)/f = g0` (13C §2); in both cases
  `h ∈ {f0,g0}` must divide `am+1`, i.e. `a ≡ −m⁻¹ (mod h)`, enumerated among divisors `a | Q`.
  II1 / I4 `(a,b,e)`, `ab = Q`, `e | a+b`, `e = f0` resp. `g0`: since `a+b ≥ e`, `min(a,b) ≤ 2Q/e` — scan the sorted
  divisors of `L/4` up to `2Q/e`.
* **(C) II2** `(a,d,f)`: `f | L`, `f ≡ 3 (4)`, `ad | A = (f+1)/4`, `x ≡ −4a²d (f)`. Per L, A is factored
  (trial division + Miller–Rabin + Pollard rho, 128-bit) and the residues `−4a²d mod f` are tabulated.
* 128-bit arithmetic, `mulmod` exact for moduli `< 2¹²⁷`. The Miller–Rabin test (20 prime bases) is used only
  to *factor* A in (C); a wrong "prime" verdict could only lose II2 witnesses (never create a false one —
  every witness is re-checked by the tree checkers).

**`req` (used inside the DFS).** If a node `x mod L` is known to lie in no class with `M | L`, a class covering
a child `y mod Lp` with `M | Lp` must have `v_p(M) = v_p(Lp)`; `req = p^{v_p(Lp)}` restricts the search accordingly.

**Validation.** (i) every unit `x` mod `L ∈ {9240, 10920, 65520, 720720}` (156288 nodes): full witness sets of
the C engine and `m13c_witness.witness_all(first=False)` agree — **0 mismatches**.
(ii) random open leaves of the 13C §8.2 tree (in progress, see below).
