# EXCEPTIONAL_MN3 — the lower side of the m/n transition: the m/φ(m) loss and the Type I log log (task O108)

Status labels as in DISCOVERIES.md. Notation as in EXCEPTIONAL_MN2.md (MN2): `L = log N`,
`ρ_rep(m, N)` = proportion of m-representable primes in (N/2, N]; ET = Elsholtz–Tao,
arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`); PV = Pólya–Vinogradov; BT = Brun–Titchmarsh.

## 0. Summary

(filled in at the end)

## 1. What ET say is open

ET Thm 1.1: `Σ_{p≤N} f_I(p) ≪ N log² N log log N` versus `≫ N log² N`; `Σ_{p≤N} f_II(p) ≍ N log² N`.
ET p. 5: "The double logarithmic factor log log N … arises from technical limitations to our method
(and specifically, in the inefficient nature of the Brun–Titchmarsh inequality (A.10) when applied to
very short progressions), and we conjecture that it should be eliminated." ET §9 p. 36 (Type II):
"the ability to take one of these quantities [ade, acd, ab] to be significantly less than N allows us
to avoid the inefficiencies in the Brun–Titchmarsh inequality … that led to a double logarithmic loss in
the Type I case. (Unfortunately, it does not seem that a similar trick is available in the Type I case.)"
[The pdf text reads "Type II case" in the parenthesis; from context (Type II *has* the trick) it means
Type I.] So the open statement is precisely

  (OPEN-I)  `Σ_{p≤N} f_I(p) ≪ N log² N`.

Origin of the loss (ET §8): with `p = 4acd − f`, `f | 4a²d+1`, `acd ≍ N`, ET fix (a, d, f) and count
primes `p ≡ −f (mod 4ad)` by BT, `≪ N/(φ(4ad) log(2 + N/ad))`; the block `ad ≍ N/2^j` (i.e. c ≍ 2^j)
costs `N log² N/j`, and `Σ_{j≤log N} 1/j = log log N`. Only `c ≤ N^ε` matters: the blocks
`c > N^ε` cost `N log² N log(1/ε)`.

## 2. The m/φ(m) loss (MN2 open point (ii)): removed

Throughout §2, `W_K(y) := Σ_{n≤y, (n,K)=1} 1/n`.

**Lemma 2.1 (coprime harmonic sums; PROVED, elementary).** For `K ≥ 1`, `y ≥ 2`:
(a) `W_K(y) ≤ 1 + log y`; (b) `W_K(y) ≤ C (φ(K)/K) log y · e^{2ω(K)/y}`, so `W_K(y) ≪ (φ(K)/K) log y`
when `y ≥ ω(K)`.

*Proof.* (a) trivial. (b) Every n counted has all prime factors `≤ y` and none dividing K, so
`W_K(y) ≤ Π_{p≤y, p∤K}(1−1/p)^{−1} = Π_{p≤y}(1−1/p)^{−1} · Π_{p|K, p≤y}(1−1/p)`
`= Π_{p≤y}(1−1/p)^{−1} · (φ(K)/K) · Π_{p|K, p>y}(1−1/p)^{−1}`; Mertens, and
`(1−1/p)^{−1} ≤ e^{2/p} ≤ e^{2/y}` for `p > y ≥ 2`. ∎

**Lemma 2.2 (character sums; PROVED, standard).** (a) For odd non-square q and any integer h with
`(h,q) = 1`, every `A ≥ 1`: `|Σ_{a≤A, a odd} (ha/q)| ≤ C √q log q` (Jacobi symbol).
(b) For `k, a ≥ 1`, `x ≥ 1`: `|Σ_{q≤x, q odd} (−ka/q)| ≤ C √(ka) log(2ka)`.

*Proof.* (a) `a ↦ (a/q)` is a Dirichlet character mod q, non-principal as q is not a square (if
`p^{2v+1} ∥ q`, choose a ≡ non-residue mod p, ≡ 1 mod q/p^{2v+1}). PV holds for every non-principal
character mod q with `≪ √q log q` (for χ induced by primitive χ* mod q*, with r the product of the
primes of q not dividing q*: `Σ_{n≤x}χ(n) = Σ_{g|r} μ(g)χ*(g) Σ_{n≤x/g}χ*(n)`, and
`τ(r)√q* ≤ 2√(q/q*)√q*`). Odd a: `Σ_{a≤A}χ(a) − χ(2)Σ_{a≤A/2}χ(a)`. (b) With `D = −4ka`, the Kronecker
symbol `χ_D` is a real character mod `4ka`, non-principal since D is not a square (D < 0), with
`χ_D(q) = (4/q)(−ka/q) = (−ka/q)` for odd q and `χ_D(q) = 0` for even q; apply PV. ∎

**Proposition 2.3 (ET Prop 1.4 with the coprimality gain; PROVED rel. ET Thm 7.1).** Fix `l ≥ 1`.
Let `k ≥ 1`, `A, B ≥ 2`.
(a) If `kB² ≤ A^l` and `A ≥ ω(k) + 2`: `Σ_{a≤A, b≤B} τ(kab²+1) ≪_l (φ(k)/k) AB log A`.
(b) If `kA ≤ B^l` and `B ≥ ω(2k) + 2`: `Σ_{a≤A, b≤B} τ(kab²+1) ≪_l (φ(k)/k) AB log B · Λ`, where
`Λ = 1 + min( log(1+k), k^{1/6} log(2kA)/A^{1/2} )`.

(Compare ET Prop 1.4: `AB log(A+B) log(1+k)`, and MN2 Lemma 3.3: `Λ` with `1[A < k log⁴]`, both without
`φ(k)/k`. The two changes: keep the coprimality `(m, k) = 1` that ET's bound `ρ ≤ 1 ∗ χ` discards,
and use PV in the q-ranges where ET used the period bound — then *every* term, main and error,
carries the factor `W_{2k}(B)`.)

*Proof.* (a) For fixed b, ET Thm 7.1 (= Cor 7.4) for `P(a) = kb²a + 1` (coefficients `≤ A^l`,
`ρ(p^j) ≤ 1`, and `ρ(m) = 0` unless `(m, kb²) = 1`): `Σ_{a≤A} τ(P(a)) ≪_l A Σ_{m≤A} ρ(m)/m ≤ A W_k(A)`;
Lemma 2.1(b); sum over b.
(b) For fixed a, Thm 7.1 for `P_{ka}(b) = kab²+1` (degree 2, coefficients `≤ B^l`, `ρ(p^j) ≤ 4` — ET
p. 30): `Σ_{b≤B} τ(P_{ka}(b)) ≪_l B Σ_{m≤B} ρ_{ka}(m)/m`. Writing `m = 2^j m₀`, `ρ(m) = ρ(2^j)ρ(m₀) ≤
4ρ(m₀)`, so `Σ_{m≤B} ρ_{ka}(m)/m ≤ 9 Σ_{m₀≤B odd} ρ_{ka}(m₀)/m₀`. For odd `m₀`:
`ρ_{ka}(m₀) ≤ 1[(m₀,k) = 1] Σ_{q | m₀} (−ka/q)`. (If `(m₀, ka) = 1` this is ET p. 31: for `p^j ∥ m₀`,
`ρ(p^j) = 1 + χ(p) ≤ Σ_{i≤j} χ(p)^i` with `χ(p) = (−ka/p) = ±1`. If `(m₀, k) = 1 < (m₀, a)`, then
`ρ_{ka}(m₀) = 0` (`P ≡ 1` mod `p | a`), and the right side is `Π_{p^j∥m₀} Σ_{i≤j} (−ka/p^i) ≥ 0`, the factors
with `p | a` being 1. If `(m₀, k) > 1` both sides vanish.) **This indicator is the only new input; ET drop
it.** Inserting and writing `m₀ = qn`:
`Σ_{m₀≤B odd} ρ_{ka}(m₀)/m₀ ≤ Σ_{q≤B odd, (q,k)=1} (−ka/q) W(B/q)/q`, `W := W_{2k}`,
where `W(B/q) ≤ W(B)` and `q ↦ W(B/q)/q` is positive and decreasing. Sum over `a ≤ A`, call it T, and
split the q-range at `1 ≤ Q₁ ≤ Q₂ ≤ B`:
* squares `q = r²`: `(−ka/r²) ≤ 1`, contribution `≤ A W(B) Σ_r r^{−2} ≪ A W(B)`;
* non-squares `q ≤ Q₁`: `(−ka/q) = (−k/q)(a/q)` with `(−k/q) = ±1` (as `(q,2k) = 1`); restricted to
  odd a (terms with `(a,q) > 1` vanish on both sides) Lemma 2.2(a) gives `≪ √q log q`; contribution
  `≪ W(B) Σ_{q≤Q₁} q^{−1/2} log q ≪ W(B) √Q₁ log Q₁`;
* non-squares `Q₁ < q ≤ Q₂`: trivially `≤ A W(B) Σ_{Q₁<q≤Q₂} 1/q ≤ A W(B)(1 + log(Q₂/Q₁))`;
* all `q > Q₂`: for each a, Abel summation with Lemma 2.2(b) (terms with q even or `(q,ka) > 1` are 0
  on both sides) gives `≪ √(ka) log(2ka) · W(B/Q₂)/Q₂`; contribution `≪ W(B) A^{3/2} k^{1/2} log(2kA)/Q₂`.
Choice 1: `Q₁ = min(B, A²/log²(2A))`, `Q₂ = min(B, max(Q₁, kA))`: T ≪ A W(B)(1 + log(1+k)) (if `Q₂ = B`
the last range is empty; `log(kA log²(2A)/A²) ≤ log(1+k) + O(1)`).
Choice 2: `Q₁ = Q₂ = min(B, A k^{1/3})`: T ≪ W(B)(A + A^{1/2}k^{1/6} log(2kA)).
So `T ≪ A W(B) Λ`, and `W(B) = W_{2k}(B) ≪ (φ(k)/k) log B` by Lemma 2.1(b) (`φ(2k)/2k ≤ φ(k)/k`). ∎

*Remark 2.4.* The gain is exact in order: for `n ≡ 1 (mod k)` all divisors are coprime to k, and
`Σ_{a,b} τ(kab²+1) ≍ (φ(k)/k)·AB log(AB)` is the heuristic size (EVIDENCE: §2.6 numerics).
