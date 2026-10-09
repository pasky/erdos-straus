# EXCEPTIONAL_MN3 — the lower side of the m/n transition: the m/φ(m) loss and the Type I log log (task O108)

Status labels as in DISCOVERIES.md. Notation as in EXCEPTIONAL_MN2.md (MN2): `L = log N`,
`ρ_rep(m, N)` = proportion of m-representable primes in (N/2, N]; ET = Elsholtz–Tao,
arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`); PV = Pólya–Vinogradov; BT = Brun–Titchmarsh.

## 0. Summary

* **(ii) the m/φ(m) loss — REMOVED (PROVED).** Prop 2.3: ET Prop 1.4 with the coprimality gain,
  `Σ_{a≤A,b≤B} τ(kab²+1) ≪ (φ(k)/k)·AB log(A+B)·Λ`, Λ = O(1) unless the linear variable is
  `< k^{1/3}·polylog` (then `Λ ≤ 1 + log(1+k)`). New inputs: keep the indicator `(m,k) = 1` that
  ET's `ρ ≤ 1∗χ` drops, and use Pólya–Vinogradov in both q-ranges, so that main *and* error terms
  carry `W_{2k}(B) ≪ (φ(k)/k) log B`. Hence **Theorem L'**:
  `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}` (MN2 had `/φ(m)`); the lower side now matches
  Thm U up to `(log L)^{1/3} = (log log N)^{1/3}` in the threshold, instead of `(m log m/φ(m))^{1/3}`.
  EVIDENCE for the gain: §2.6.
* **(i) the Type I log log N (ET's open (OPEN-I), also the `log L` above) — NOT removed; obstacle
  located (geometry PROVED, mass and method-exclusion claims Assessment).**
  - Lemma 3.2 (generic elimination; completeness EVIDENCE): ET's 3-coordinate parametrisations give exactly the progression moduli
    `4ad, 4bd, 4ab, 4acf, 4cdf` (+ twins `4bcf', 4cdf'`).
  - Prop 3.3 (PROVED): all of them are `≥ N^{1−η}` on a region R_bad of area 1/6 of the small-c
    slice — our reading of ET's "no similar trick" remark. On its limiting slice neither divisor e, f
    of `4a²d+1` is below a or d in exponent.
  - Lemma 3.1 (PROVED): `ef − 4a²d = 1` ⟺ `[[e,2a],[2ad,f]] ∈ SL₂(ℤ)`, with n a linear form in the
    entries; for fixed d these are (an admissible, parity-restricted subset of) Heegner points of
    discriminant −4d on X₀(d).
  - §3.4 (Assessment): Kloosterman/Weil counts with one fixed coordinate shrink the bad region to
    R** (area 7/72: `a ≥ N^{1/2}`, `e, f ≥ N^{2/3}`); positive area still costs a log log.
  - §3.5 (Assessment): on R** a sieve needs (H**), the equidistribution mod q of Heegner points of
    discriminant −4d on X₀(d) in thin strips, averaged over `d ≤ N^{1/2}` — a joint
    level/discriminant-aspect problem. Five naive approaches (BT, BDH/Montgomery–Hooley variance,
    one-variable Selberg, one-coordinate Weil, Erdős's trick) are checked to fail on R_bad/R** (§3.6;
    (H**) is a sufficient target, not a proved necessary condition).
  - Theorem 3.8 (PROVED conditional on LD): a level-of-distribution hypothesis for the small-c Type I
    weights implies (OPEN-I); an m-analogue (proposed, Remark 3.8(b)) would give
    `ρ_rep ≪ (L³ + L² log² m)/m + m^{−0.35}`.
* Literature: no later removal of ET's log log found (§3, search-limited).

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
* non-squares `q ≤ Q₁`: `Σ_{a≤A}(−ka/q) = (−k/q)Σ_{a≤A}(a/q)` with `(−k/q) = ±1` (as `(q,2k) = 1`),
  and PV for the non-principal character `(·/q)` (Lemma 2.2(a), proof) gives `≪ √q log q`; contribution
  `≪ W(B) Σ_{q≤Q₁} q^{−1/2} log q ≪ W(B) √Q₁ log Q₁`;
* non-squares `Q₁ < q ≤ Q₂`: trivially `≤ A W(B) Σ_{Q₁<q≤Q₂} 1/q ≤ A W(B)(1 + log(Q₂/Q₁))`;
* all `q > Q₂` (squares included again — harmless for an upper bound, since square terms are ≥ 0
  and were already bounded above; the split is not a partition): for each a, Abel summation with Lemma 2.2(b) (terms with q even or `(q,ka) > 1` are 0
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
`1/φ(ad) ≪ (ad)^{−1} Σ_{s|a, t|d} 1/(st)`, `a = sa'`, `d = td'`, `k = ms²t ≥ m`; the block `ad ∈ (X, 2X]`
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
`S_k/(AB log(kAB²))` divided by `φ(k)/k` stays in `[0.81, 1.12]` while `φ(k)/k` ranges over
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
So, for fixed c, the Type I solutions are an admissible subset of S_d, d ≥ 1 (positive entries,
`M₁₂` even, ET's size conditions), and the prime is a linear form in the entries. The admissible
subset is **not** Γ₀(d)-stable (parity: for d = 1, `M = [[1,2],[2,5]]`, `γ = [[1,1],[0,1]]` give
`γMγᵀ = [[10,7],[7,5]]`, i.e. a = 7/2 — R108 review); a parity-preserving subgroup such as
`Γ₀(d) ∩ Γ(2)` (or explicit congruence bookkeeping) is needed, and counting orbit lifts in boxes is
not the same as equidistribution of CM packets on the quotient.

**Lemma 3.2 (single-progression parametrisations; generic elimination + hand check — the
completeness claim is EVIDENCE: specialisations where an eliminant coefficient vanishes were not
checked systematically).** Call a parametrisation *single-progression* if three of the coordinates
a..f are fixed and n is an affine function of a fourth coordinate v that runs over a union of
residue classes (one class, or the `ρ(f) ≤ 2^{ω(f)+1}` roots in the (c,d,f) case). Among
ET's 3-coordinate parametrisations (and their twins) the moduli of the resulting progressions in n
are exactly `4ad, 4bd, 4ab, 4acf, 4cdf` (twins add `4bcf'`, `4cdf'`).
*Proof.* `scripts/emn3_modes.py` eliminates, for each of the 60 pairs (fixed triple S, free v), the
other coordinates by a lex Gröbner basis and lists the cases where n is affine in v
(`emn3_modes.out.txt`, 24 cases). Of these, 4 are not progressions (v ranges over divisors: fixing
(a,b,d) or (a,b,f) with c free needs `c | a+b`; fixing (a,b,d) or (a,c,d) with f free needs
`f | 4a²d+1`). In the other 20, the step of n per admissible step of v is: 4ab (fixed (a,b,·),
(a,c,e), (b,c,e): `e` fixed, `d ≡ d₀ (e)` resp. `f ≡ ē (4a²)`); 4ad ((a,d,·), (a,e,f): b or c free,
`b ≡ −a (e)`); 4bd ((b,d,e)); 4acf ((a,c,f): `d ≡ d₀ (f)`, `e ≡ f̄ (4a²)`, `b ≡ cf̄ − a (4a²c)`);
4cdf ((c,d,f), a free in the ρ(f) roots of `4dx²+1 ≡ 0 (f)`). ∎

**Proposition 3.3 (the bad region; PROVED, elementary).** In exponents, the moduli of Lemma 3.2 are
`4ad: 1−γ`, `4bd: 1−γ+β−α`, `4ab: α+β`, `4acf: 1+2α+γ−β`, `4cdf: 2−β`, `4bcf': 1+2β+γ−α`,
`4cdf': 2−2α+β`. All are `≥ 1−η` iff
`R_bad(η): γ ≤ η, α+β ≥ 1−η, β ≤ 2α+γ+η, β ≤ 1+η` (with `α ≤ β`).
At γ = 0 (η → 0) this is `{α+β ≥ 1, α ≤ β ≤ min(2α, 1)}`, of area **1/6** inside the slice
`{0 ≤ α ≤ 1, α ≤ β ≤ 1+α}` (area 1): `∫_{1/3}^{1/2}(3α−1)dα + ∫_{1/2}^{1}(1−α)dα = 1/24 + 1/8`.
On the limiting slice γ = η = 0, neither divisor e, f of `4a²d+1` is smaller in exponent than a or
d (`β ≥ max(α, 1−α)`, `1+α−β ≥ max(α, 1−α)`; equality on the boundary). For finite η only
`e, f ≥ N^{−O(η)} max(a, d)` holds (e.g. α = β = 0.6, γ = η = 0.05 has e below a — R108 review).

*Consequence (the naive approach fails; Assessment, mass heuristic).* ET's bound is "for each solution
cell, apply BT to one progression": a cell with `c ≍ N^γ` gains only `1/log(N/M)` with M the best
modulus. Type I mass is log-uniform in `(α, β)` and `≍ N log² N` per dyadic c-block (ET (8.2) is the
upper bound; the uniformity is the divisor heuristic), so the cells in R_bad(η) cost
`≍ (1/6)·N log² N Σ_{j ≤ η log N} 1/j`. So, granted log-uniformity of the mass, **no choice among the
7 progressions removes the log log N**; this is our reading of ET's "no similar trick" remark.
(Positive area is not by itself positive logarithmic mass; and outside R_bad a small modulus must still
be combined with weighted harmonic-sum estimates — routine, not written out.) (A rigorous lower bound for the mass of
R_bad ∩ {α < 1/2} follows from the modular-hyperbola count of §3.4; not written out.)

**3.4 Beyond progressions: complete exponential sums (Assessment — standard sketches, not written
as proofs).** Three further "one fixed coordinate" counts are available in R_bad, each giving a level
of distribution `N^{θ}` (θ > 0) for the condition `q | n` on the cell, by Weil/Kloosterman:
* (K_a) fix a: `(e,f)` lie on the modular hyperbola `ef ≡ 1 (mod 4a²)` in an `E×F` box (d is then
  determined); the class condition mod q is a conic in (e,f) mod q (`a·n = c(ef−1) − af`). Count
  `= EF·φ(4a²)/(4a²)²·(…) + O(a^{1+ε}q^{O(1)})`; main term per a is `≍ D = N^{1−α−γ}`, so this works iff
  `α < (1−γ)/2`.
* (W_e) fix e: `(a,d)` with `d ≡ −\overline{4a²} (mod e)` in an `A×D` box, plus a linear condition
  mod q on d: Weil for `Σ_a e(h\overline{4a²}/(eq))` gives error `≪ (eq)^{1/2+ε}` per e, against main
  `AD/e`; works iff `(3/2)(β−γ) < 1−γ`.
* (W_f) fix f: the same with modulus f: works iff `(3/2)(1+α−β) < 1−γ`.
At γ = 0 these leave
`R** = R_bad ∩ {α ≥ 1/2, β ≥ 2/3, β ≤ α+1/3} = {1/2 ≤ α ≤ 1, max(α, 2/3) ≤ β ≤ min(1, α+1/3)}`,
of area `1/24 + 1/18 = 7/72` (vs 1/6 for R_bad). A positive area still means a `log log N` (with a
smaller constant), so these sketches are recorded only to locate the obstacle, not as a result.
(The reciprocity `\overline{4a²}/e ≡ −ē/(4a²) + 1/(4a²e)` turns the e-average in (W_e) into (K_a), so
the simplest bilinear Kloosterman-fraction argument does not enter R**; we do not claim that no
bilinear estimate can.)

**3.5 What would suffice in R** (a sufficient research target, not a proved necessary condition;
Assessment).** In R**: `a ≥ N^{1/2}`, so
`4a² ≥ N` and the hyperbola of (K_a) is too sparse; `e, f ≥ N^{2/3}`, so (W_e), (W_f) are past the
Weil range; `d ≤ N^{1/2}`; every one-variable progression is shorter than `N^{o(1)}`·c. By
Lemma 3.1 the points of a cell with fixed d are the elements `M = [[e,2a],[2ad,f]]` of
`S_d ∩ {box}` with `M₁₂` even, i.e. (parity-restricted, cf. Lemma 3.1) lifts of the Heegner points
of discriminant −4d on X₀(d)
(`z_M = (−2a + i/√d)/e`, imaginary part `≍ 1/(E√d)`, real part in `[−2A/E, 0]`), and the sieve
condition is `q | 2cM₂₁ − M₂₂`. A Selberg sieve of any fixed level `N^θ` on R** would follow from:

  (H**) *Equidistribution, modulo q ≤ N^θ and with a power (or large log-power) saving summed over
  q, of the points of `⋃_{d≍D} S_d` in boxes of R**-shape*, i.e. of Heegner points of discriminant
  −4d on X₀(d) (level and discriminant tied) in thin strips near the real axis, on average over
  `d ≍ D ≤ N^{1/2}`, with congruence conditions.

For a single bounded d this is effective hyperbolic lattice-point counting in a congruence subgroup
(uniform spectral gap: Selberg 3/16 / Kim–Sarnak), which gives level `N^θ`. The difficulty is the
**level aspect**: error terms of effective counting grow polynomially in the index `[SL₂(ℤ):Γ₀(dq)]`,
while each d carries only `≍ A = N^α` points; crude level dependence `d^C` covers only
`α ≥ 1 − O(δ/C)`, whereas R** reaches down to `α = 1/2` (`d = N^{1/2}`). Closing R** needs a
Duke/Iwaniec-type equidistribution of Heegner points in the joint level–discriminant aspect
(averaged over d, which should help via Kuznetsov with level averaging), with congruence twists.
We did not find such a statement in the literature and do not claim it.

**3.6 Naive approaches that fail (each checked against the R_bad geometry).**
* (N1) BT on any single progression — Prop 3.3: every modulus ≥ `N^{1−η}` in R_bad.
* (N2) Cauchy–Schwarz against Barban–Davenport–Halberstam / Montgomery–Hooley (moduli `q ≍ N/C`,
  valid up to Q = N): the classes `−f (mod 4ad)` number only `≍ (N/C) log² N` among `≍ N²/C` pairs
  (q, r). The variance `≍ QN/log N = N²/(C log N)` gives error
  `(R·V)^{1/2} ≍ N^{3/2}(log N)^{1/2}/C ≫ N log N` (the main term). Fails by a power of N.
* (N3) Selberg sieve in one linear variable: level ≤ that variable's length ≤ `N^{η}` in R_bad, i.e.
  BT again.
* (N4) Complete-sum (Weil/Kloosterman) counting with one fixed coordinate — §3.4: fails on R**.
* (N5) Erdős's trick (ET Thm 7.1), which makes Prop 1.4 work without equidistribution, needs
  positivity in the *divisor*: it bounds τ by divisors below the variable length. The sieve weight
  depends on the specific divisor f through `n = 4acd − f`, and in R_bad (limiting slice) that f is
  not below the lengths of a and d (Prop 3.3, last sentence), so the trick does not apply directly.

**3.7 The conditional statement (PROVED, conditional on the hypothesis LD).** For c ≥ 1 let
`w_c(n) := #{(a,d,f) ∈ ℕ³ : f | 4a²d+1, n = 4acd − f, n/4 < acd ≤ 3n/4}`; by ET Prop 2.2 and Lemma 2.8,
`f_I(p) ≤ 2 Σ_c w_c(p)`. Put `X_c := Σ_{N/2<n≤N} w_c(n)`.

*Hypothesis LD(η₀, θ, C₀).* For each `c ≤ N^{η₀}` there is a multiplicative `h_c` on squarefree
numbers with `0 ≤ h_c(ℓ) ≤ 1 + C₀/ℓ` for all primes ℓ and `h_c(ℓ) ≥ 1 − C₀/ℓ` for `ℓ > 2`, such that
`R_c(q) := Σ_{N/2<n≤N, q|n} w_c(n) − (h_c(q)/q) X_c` satisfies
`Σ_{c≤N^{η₀}} Σ_{q≤N^θ} μ²(q) 3^{ω(q)} |R_c(q)| ≤ C₀ N log N`.

**Theorem 3.8.** LD(η₀, θ, C₀) for all large N implies `Σ_{p≤N} f_I(p) ≪_{η₀,θ,C₀} N log² N`
(i.e. ET's conjecture (OPEN-I)).

*Proof.* It suffices to treat `p ∈ (N/2, N]` and sum dyadically. Split the quadruples (a,c,d,f) by
`ad`. (1) `ad ≤ N^{1−η₀}`: as in ET (8.1), BT for `p ≡ −f (mod 4ad)` gives
`≪ N/(φ(ad) η₀ log N)` per (a,d,f) (N large), and `Σ_{ad≤N} τ(4a²d+1)/φ(ad) ≪ log³ N` (ET (8.2) over
dyadic blocks), so this part is `≪ η₀^{−1} N log² N`. (2) `ad > N^{1−η₀}`: then
`c < 3N/(4ad) < N^{η₀}`, and these quadruples are counted by `Σ_{c≤N^{η₀}} Σ_{N/2<p≤N} w_c(p)`. With
`z = N^{min(θ,1)/2} < N/2`, every such p has no prime factor `< z`. Sieve only by the primes
`ℓ ∈ 𝒫 := {ℓ > ℓ₀}`, `ℓ₀ = ℓ₀(C₀) := 2C₀ + 2`, so that `1/2 ≤ h_c(ℓ) ≤ 1 + C₀/ℓ < ℓ(1 − 1/ℓ₀)` on 𝒫
(Ω₁) and `Σ_{w≤ℓ<z} h_c(ℓ) log ℓ/ℓ ≤ log(z/w) + O_{C₀}(1)` (Ω₂(1)); omitting `ℓ ≤ ℓ₀` costs only a
factor `O_{C₀}(1)`. Selberg's upper-bound sieve of dimension 1 (Halberstam–Richert, Thm 4.1 with
Lemma 4.1) gives
`Σ_{N/2<p≤N} w_c(p) ≪_{C₀} X_c Π_{ℓ₀<ℓ<z}(1 − h_c(ℓ)/ℓ) + Σ_{q<z²} μ²(q)3^{ω(q)}|R_c(q)|`,
with `Π_{ℓ₀<ℓ<z}(1 − h_c(ℓ)/ℓ) ≪_{C₀} 1/log z` (as `h_c(ℓ) ≥ 1 − C₀/ℓ`). Finally `X_c ≤ Σ_{ad≤3N/(4c)} τ(4a²d+1) ≪ (N/c) log² N`
(ET Prop 1.4, k = 4, over dyadic boxes). Summing over c: `≪ (η₀/θ) N log² N + C₀ N log N`. ∎

*Remarks.* (a) (Assessment) By Prop 3.3 and BT — plus the routine weighted harmonic sums for the
alternative moduli — LD should only be needed for the part of w_c in cells of R_bad(η₀), and by §3.4
only in R**, where (H**) would supply it. (b) (Proposed conditional extension, not proved.) An
m-analogue `LD_m` would remove the `log L` from Prop 2.5 and give `ρ_rep ≪ (L³ + L² log² m)/m + m^{−0.35}`.
It must be formulated with care (R108 review): every supported n is coprime to m, so the primes
`ℓ | m` must be removed from the sieving set (h(ℓ) = 0 there), the remainder allowance must be
`≪ N(L² + L log² m)/m` rather than `N log N`, and the mass saving `φ(m)/m` must be tracked against
the sieve-product inflation `m/φ(m)` from the omitted primes. (c) Varying c alone gives, for each
fixed (a,d,f), a progression in c, hence level `≤ C^{1−ε}` for the c-aggregated count; this is BT,
which is exactly what is not enough (LD as stated sums `|R_c(q)|` for each c separately, which this
does not control).

## Replay

```
PYTHONPATH=scripts uv run python scripts/emn3_coprime.py 120     # §2.6, ~3 min
PYTHONPATH=scripts uv run python scripts/emn3_modes.py           # Lemma 3.2, ~5 min
uv run python scripts/emn3_identities.py                         # Lemma 3.1 / twin sanity, <1 min
```
Outputs: `scripts/emn3_*.out.txt`. Proof-level claims (Prop 2.3, Prop 2.5, Thm L', Prop 3.3,
Thm 3.8) are not machine-checked.
