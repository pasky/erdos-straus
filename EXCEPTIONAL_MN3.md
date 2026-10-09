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

**Proposition 2.5 (Type I count with 1/m; PROVED rel. ET Thm 7.1, BT).** For `m ≥ 4`, `log m ≤ L/10`,
`L ≤ m^{1/2}`:
`#{p ∈ (N/2,N] : p has a Type I m-solution} ≪ (N/L)·[(L³ + L² log² m) log L/m + m^{−0.35}]`.

*Proof.* For `m ≤ m₀` (absolute) this is MN2 Prop 3.4 (`φ(m) ≍ m`). Let `m > m₀`. Follow MN2 Prop 3.4:
by PW (3.2) and BT the count is `≪ Σ_{mad≤3N} τ(ma²d+1) N/(φ(m)φ(ad) log(2+N/mad))`; ET (A.12)
`1/φ(ad) ≤ (ad)^{−1} Σ_{s|a, t|d} 1/(st)`, `a = sa'`, `d = td'`, `k = ms²t ≥ m`; the block `ad ∈ (X, 2X]`
splits into `≪ L` dyadic boxes `a' ~ A'`, `d' ~ D'` (`A'D' ≍ X/st`; size-1 sides enlarged to 2 by
positivity). Take `l = 30`, so that `kA'² ≤ D'^l` when `D' ≥ max(A', k^{1/28})` and `kD' ≤ A'^l` when
`A' > max(D', k^{1/28})`; `m₀` is chosen so that `k^{1/28} ≥ ω(2k) + 2` for `k ≥ m₀`.
* Boxes with `max(A', D') ≥ k^{1/28}`: Prop 2.3 (linear variable d', quadratic a'; (a) if `D' ≥ A'`,
  (b) if `D' < A'`) gives `≪ (φ(k)/k)(X/st) log X · Λ`, with `Λ ≤ 2` unless
  `D' < k^{1/3} log²(2kX)`; at most `≪ log(2k) + log L` boxes per block are of that kind, each with
  `Λ ≤ 1 + log(1+k)`. As `φ(k)/k ≤ φ(m)/m`, the weighted block sum is
  `≪ (φ(m)/m) Σ_{s,t}(st)^{−2}[L² + L log²(2ms²tL)] ≪ (φ(m)/m)(L² + L log² m)` (`log L ≤ log m`).
* Boxes with `max(A', D') < k^{1/28}` ("tiny"): `n = ka'²d'+1 ≤ 8k^{1.11}`, `τ(n) ≪ k^{0.012}`. They
  occur in the block only if `X ≤ 4st·k^{1/14} ≤ 4m^{1/14}(st)^{8/7}`, and their weighted mass is
  `≪ Σ_{st ≥ (X/4m^{1/14})^{7/8}} τ(st)(st)^{−2}(m(st)²)^{0.012} log(2mst) ≪ m^{0.013} min(1,(X/m^{0.072})^{−0.85})`.
  Summed over blocks (BT weight ≤ 1): `≪ m^{0.014}`, so a count `≪ N m^{0.014}/φ(m) ≪ (N/L) m^{−0.35}`.
Summing the first kind over blocks `X = 3N2^{−j}/m` with BT weight `≪ 1/j`, `j ≤ 2L`:
`≪ (N/φ(m))(φ(m)/m)(L² + L log² m) log L`. ∎

**Theorem L' (lower side without the m/φ(m) loss; PROVED rel. ET Thm 7.1, BT, Shiu; effective).**
For `m ≥ 4`, `N ≥ 16`, `log m ≤ L/10`, `L ≤ m^{1/2}`:
`ρ_rep(m, N) ≪ (L³ + L² log² m) log L/m + m^{−0.35}`.
(For `log m > L/10`, MN2 Lemma 3.5 is unchanged.) Consequently `ρ_rep → 0` whenever `L³ log L/m → 0`,
i.e. `L ≤ ε(m/log m)^{1/3}`, ε → 0.

*Proof.* MN2 Prop 3.2 (Type II, `≪ (N/L)(L³ + m^{0.02})/m`) plus Prop 2.5; `π*(N) ≫ N/L`;
`m^{0.02}/m ≤ m^{−0.35}`. The consequence as in MN2 Thm L (`L ≥ log(m/3)` if `ρ_rep > 0`, so
`L² log² m log L/m ≤ (L³ + log⁶ m) log L/m`). ∎

So the gap between Thm U and the lower side is now `(log m)^{1/3}` in log N (from the BT log L alone),
instead of `(m log m/φ(m))^{1/3}`. MN2 open point (ii) is closed.

**2.6 Numerics (EVIDENCE; `scripts/emn3_coprime.py`, output `.out.txt`).** For `A = B = 120`,
`S_k/(AB log(kAB²))` divided by `φ(k)/k` stays in `[0.81, 1.11]` while `φ(k)/k` ranges over
`[0.19, 0.50]` (k = 4, 12, 60, 420, 4620, 60060, 4·1009, 4·1009·1013). Without the gain the ratio would
grow like `k/φ(k)` (×2.6). (Normalising by `log(AB)` instead mixes in the `log k` from the size of n.)

## 3. The Type I log log N (MN2 open point (i), ET's (OPEN-I)): obstruction analysis

Literature (web search 2026-10, Jina; ET's citing papers seen: Huang–Vaughan (binary Egyptian
fractions, mean values), Elsholtz–Planitzer 2020 (k unit fractions), Pomerance–Weingartner, Dahan,
Jiang (withdrawn)): **no later removal or improvement of the log log N in `Σ_p f_I(p)` was found.**
(Search-limited; not a full citation crawl.)

Notation (ET Prop 2.2, Lemma 2.8): a Type I solution of n (y ≤ z) is an N-point (a,b,c,d,e,f) of
`Σ^I_n`: `4abd = ne+1`, `ce = a+b`, `4acd = n+f`, `ef = 4a²d+1`, `bf = na+c`, with `a ≤ b`,
`b < ce ≤ 2b`, `an ≤ bf ≤ (5/3)an`, `n/4 < acd ≤ 3n/4`. Its twin (y ↔ z) is `(b,a,c,d,e,f')`,
`f' = 4bcd − n = (n²+4c²d)/f` (ET (2.9)). For a solution with n ≍ N write
`a = N^α, b = N^β, c = N^γ`; then `d ≍ N^{1−α−γ}`, `e ≍ N^{β−γ}`, `f ≍ N^{1+α−β}`, `f' ≍ N^{1−α+β}`,
and `0 ≤ α`, `α ≤ β ≤ 1+α` (from `1 ≤ f ≪ n`), `α + γ ≤ 1`.

**Lemma 3.1 (SL₂ form; PROVED, elementary).** `ef − 4a²d = 1` says exactly that
`M = [[e, 2a],[2ad, f]] ∈ SL₂(ℤ)`, and `n = 2c·M₂₁ − M₂₂`. The set `S_d = {M ∈ SL₂(ℤ) : M₂₁ = d·M₁₂}` is
the fixed set of the anti-involution `σ_d(M) = T Mᵀ T^{−1}`, `T = diag(1,d)`, and is stable under
`M ↦ γ M σ_d(γ)` for `γ ∈ Γ₀(d)`. Equivalently `(a,d,e,f) ↔` the positive definite form
`[f, 4ad, de]` of discriminant `−4d` (Heegner forms of level d and discriminant −4d with root
`β ≡ 0 (mod 2d)`, after `X ↔ Y`). (Check: `det M = ef − 4a²d`; `σ_d(M) = [[e, 2ad/d],[2a·d, f]] = M`;
`σ_d(γ) ∈ SL₂(ℤ)` iff `d | γ₂₁`; `σ_d(γMσ_d(γ)) = γ M σ_d(γ)` as σ_d is an anti-involution.)
So, for fixed c, the Type I solutions are the points of the Γ₀(d)-stable sets S_d, d ≥ 1, and the
prime is a linear form in the entries.

**Lemma 3.2 (all single-progression parametrisations; PROVED, elimination + hand check).** Call a
parametrisation *single-progression* if three of the coordinates a..f are fixed and n is an affine
function of a fourth coordinate v that runs over a union of boundedly many residue classes. Among
ET's 3-coordinate parametrisations (and their twins) the moduli of the resulting progressions in n
are exactly `4ad, 4bd, 4ab, 4acf, 4cdf` (twins add `4bcf'`, `4cdf'`).
*Proof.* `scripts/emn3_modes.py` eliminates, for each of the 60 pairs (fixed triple S, free v), the
other coordinates by a lex Gröbner basis and lists the cases where n is affine in v
(`emn3_modes.out.txt`, 24 cases). Of these, 6 are not progressions (v ranges over divisors: fixing
(a,b,d) or (a,b,f) with c free needs `c | a+b`; fixing (a,b,d) or (a,c,d) with f free needs
`f | 4a²d+1`). In the other 18, the step of n per admissible step of v is: 4ab (fixed (a,b,·),
(a,c,e), (b,c,e): `e` fixed, `d ≡ d₀ (e)` resp. `f ≡ ē (4a²)`); 4ad ((a,d,·), (a,e,f): b or c free,
`b ≡ −a (e)`); 4bd ((b,d,e)); 4acf ((a,c,f): `d ≡ d₀ (f)`, `e ≡ f̄ (4a²)`, `b ≡ cf̄ − a (4a²c)`);
4cdf ((c,d,f), a free in the ρ(f) roots of `4dx²+1 ≡ 0 (f)`). ∎

**Proposition 3.3 (the bad region; PROVED, elementary).** In exponents, the moduli of Lemma 3.2 are
`4ad: 1−γ`, `4bd: 1−γ+β−α`, `4ab: α+β`, `4acf: 1+2α+γ−β`, `4cdf: 2−β`, `4bcf': 1+2β+γ−α`,
`4cdf': 2−2α+β`. All are `≥ 1−η` iff
`R_bad(η): γ ≤ η, α+β ≥ 1−η, β ≤ 2α+γ+η, β ≤ 1+η` (with `α ≤ β`).
At γ = 0 (η → 0) this is `{α+β ≥ 1, α ≤ β ≤ min(2α, 1)}`, of area **1/6** inside the slice
`{0 ≤ α ≤ 1, α ≤ β ≤ 1+α}` (area 1): `∫_{1/3}^{1/2}(3α−1)dα + ∫_{1/2}^{1}(1−α)dα = 1/24 + 1/8`.
In R_bad both divisors e, f of `4a²d+1` exceed both a and d (`β ≥ max(α, 1−α)`,
`1+α−β ≥ max(α, 1−α)`).

*Consequence (the naive approach fails; Assessment, mass heuristic).* ET's bound is "for each solution
cell, apply BT to one progression": a cell with `c ≍ N^γ` gains only `1/log(N/M)` with M the best
modulus. Type I mass is log-uniform in `(α, β)` and `≍ N log² N` per dyadic c-block (ET (8.2) is the
upper bound; the uniformity is the divisor heuristic), so the cells in R_bad(η) cost
`≍ (1/6)·N log² N Σ_{j ≤ η log N} 1/j`. **No choice among all 7 progressions removes the log log N**;
this is the precise content of ET's "no similar trick" remark. (A rigorous lower bound for the mass of
R_bad ∩ {α < 1/2} follows from the modular-hyperbola count of §3.4; not written out.)
