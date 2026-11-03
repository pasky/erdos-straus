# Z55_TDO — tryhard lane TDO, Problem TD (strip sums T(h) in the fourth-root range)

Brief: `z52bbriefs/z55_tryhard.md` §Problem TD. Definitions/notation: `Z54_BILINDIV.md` §0–§2, §4.1 (T(h), E1, E1⁺,
w_k, TD(η), Theorem T). Scripts `scripts/z55_tdo_*`, data `data/z55/tdo/`.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment (one per claim).

## 0. Verdict

**TD(η) (pointwise, every prime p) is NOT proved.** What is proved:

* **Theorem A (PROVED) — TD for almost all primes, all U at once.** For fixed 0 < η < 1/8 and 0 < c₁ ≤ c₂, all but
  O(X^{1−η/4}) primes p ∈ (X, 2X] satisfy |T_{p,U}(h)| ≤ 2U^{1−η} for **every** U in the fourth-root range of p and every
  1 ≤ h ≤ U^η. (Fraction of exceptions ≪ X^{−η/4} log X.)
* **Theorem M (PROVED) — mean square over all integers n.** For every U ≥ 5, h ≥ 1, N₀ ≥ 0, N ≥ 1:
  Σ_{N₀<n≤N₀+N} |T_n(h)|² ≤ C·(N + 16U⁴)·hU·log(4U), C absolute. At N ≍ U⁴ this is the square-root size on average.
* **Lemma V (PROVED)** — the r-sums S_m(θ) of the phase are ≪ √(hU) uniformly in the frequency θ.
* Exact reformulations (PROVED, §1): one strip point per m; e(h·w) = e(−2h·u) = e(2h·B) with u < B the real roots;
  the discriminant form T(h) = Σ_D N_D e(h√D).

Honest downstream value of Theorem A: **none** for the (★) block. The almost-all-p form of the conclusion of Corollary T
(N₂ ≪ U^{1−η} for all U, for almost all p) is elementary by a first-moment count (Remark 4.3). Theorem A is the
almost-all form of TD itself, nothing more. §6 states (Assessment) where the pointwise argument stops.

## 1. Setup and exact forms

Throughout n ≥ 0 is an integer (p prime is a special case), U ≥ 5 an integer, h ≥ 1 an integer, e(x) = exp(2πix).
For m ∈ ℤ_{>0} let r_m(n) := (−n mod m) ∈ [0, m). Define

  T_n(h) = T_{n,U}(h) := Σ_{(k,m)∈ℤ²: n+2U<km≤n+4U, U²<m≤4U², (km−n)²−4m≥1} e(h√((km−n)² − 4m)).

For n = p this is T(h) of Z54_BILINDIV §1(B).

**Lemma 1.1 (one point per m; PROVED).** For U ≥ 5:
  T_n(h) = Σ_{U²<m≤4U²} f_m(r_m(n)),  f_m(r) := 1[2U < r ≤ 4U]·1[r² − 4m ≥ 1]·e(h√(r² − 4m)).
*Proof.* Put s = km − n. A lattice point with given m has s ≡ −n (mod m) and s ∈ (2U, 4U]. That interval has length
2U < U² < m, so it contains at most one such s, namely s = r_m(n) when r_m(n) ∈ (2U, 4U] (r_m(n) is the only
representative of −n mod m in [0, m) ⊃ (2U, 4U]). Then k = (n + s)/m is a positive integer. Conversely each such m gives
the lattice point (k, m). ∎

**Lemma 1.2 (phase identities; PROVED).** For a strip point put s = km − n, D = s² − 4m ≥ 1, w = √D, and
u := (s − w)/2, B := (s + w)/2 (real; u + B = s, uB = m). Then e(hw) = e(2hB) = e(−2hu), since hs ∈ ℤ. Moreover
  T_n(h) = Σ_{D≥1} N_D·e(h√D),  N_D := #{s ∈ (2U, 4U] : s ≡ D (mod 2), m := (s² − D)/4 ∈ (U², 4U²], m | n + s}.
*Proof.* w = 2B − s = s − 2u. For the second form, (k, m) ↦ (D, s) is injective (m = (s² − D)/4, k = (n + s)/m) and its
image is exactly the set counted by N_D (s² − D = 4m forces s ≡ D mod 2). ∎
The phase e(h√D) varies on the scale ≍ U/h in D (d√D/dD = 1/(2√D), D ≤ 12U²), while the ≍ 1.5U points D lie in
[1, 12U²]. So TD says: the discriminants D of the strip points are equidistributed at scale U^{1−η}·(1/h) in D, against
the phase √D. (Remark, used nowhere below.)

## 2. Lemma V: the r-sums

For m ∈ (U², 4U²] and θ ∈ ℝ put S_m(θ) := Σ_{r∈ℤ: 2U<r≤4U, r²−4m≥1} e(h√(r² − 4m) − θr).

**Lemma V (PROVED).** There is an absolute constant C_V with |S_m(θ)| ≤ C_V√(hU) for all integers U ≥ 2, h ≥ 1, all
m ∈ (U², 4U²] and all θ ∈ ℝ.

*Proof.*
* The summation range R is a set of consecutive integers r₀ ≤ r ≤ r₁ with r₀² ≥ 4m + 1 and r₁ ≤ 4U. (Empty R is
  trivial.) Put g(x) := h√(x² − 4m) − θx and w(x) := √(x² − 4m) for x > 2√m. Then
  g''(x) = −4hm/(x² − 4m)^{3/2}, so |g''(x)| = 4hm/w(x)³.
* On R, 1 ≤ w ≤ √(16U² − 4m) < 4U. For j ≥ 0 let R_j := {r ∈ R : 2^j ≤ w(r) < 2^{j+1}}. Since w is increasing, R_j is a
  set of consecutive integers; R_j = ∅ unless 2^j < 4U.
* *Length.* x = √(w² + 4m), and √(a + t) − √a ≤ t/(2√a). If r < r' are both in R_j then
  r' − r ≤ (4^{j+1} − 4^j)/(2√(4m)) = 3·4^j/(4√m). So |R_j| ≤ 3·4^j/(4√m) + 1.
* *Second derivative on R_j.* With λ_j := 4hm·2^{−3(j+1)}: λ_j ≤ |g''| ≤ 8λ_j on the real interval spanned by R_j
  (w ∈ [2^j, 2^{j+1}) there).
* *Small j (4^j ≤ √m).* Then |R_j| ≤ 3/4 + 1 < 2, so |Σ_{R_j}| ≤ 1. Such j satisfy j ≤ (log₂ m)/4 ≤ (2 + 2log₂U)/4,
  so there are at most 2 + log₂U of them.
* *Large j (4^j > √m).* Then |R_j| ≤ (7/4)·4^j/√m. The second-derivative test (van der Corput; Titchmarsh, *Theory of
  the Riemann zeta-function*, Thm 5.9: if λ ≤ |g''| ≤ αλ on [a, b] then Σ_{a<n≤b} e(g(n)) ≪ α(b − a)λ^{1/2} + λ^{−1/2},
  absolute implied constant) gives
  |Σ_{R_j}| ≪ (7/4)(4^j/√m)·(4hm)^{1/2}2^{−3(j+1)/2} + 2^{3(j+1)/2}(4hm)^{−1/2} ≪ √h·2^{j/2} + 2^{3j/2}/√(hm).
* *Sum over j.* Over 2^j < 4U both are geometric in j and dominated by the largest term:
  Σ_j √h·2^{j/2} ≪ √(hU), and Σ_j 2^{3j/2}/√(hm) ≪ U^{3/2}/(√h·U) = √(U/h), using √m > U.
* Total: |S_m(θ)| ≪ log U + √(hU) + √(U/h) ≪ √(hU), since h ≥ 1 and log U ≪ √U. ∎

Check (EVIDENCE, `scripts/z55_tdo_lemV.py`, `data/z55/tdo/lemV.txt`): sup over a 4096-point θ-grid of
|S_m(θ)|/√(hU), over 12 random m and h ∈ {1,2,3,5,8}, is 3.37, 3.31, 3.77, 4.18, 3.33 at U = 20, 50, 100, 200, 400.

Note: Lemma V fails at h = 0 (θ = 0 gives |S| ≍ U); h ≥ 1 is used.

## 3. Theorem M: mean square over n

**Theorem M (PROVED).** There is an absolute constant C such that for all integers U ≥ 5, h ≥ 1, N₀ ≥ 0, N ≥ 1,
  Σ_{N₀<n≤N₀+N} |T_n(h)|² ≤ C·(N + 16U⁴)·hU·(1 + log(4U²)).

*Proof.*
* *Finite Fourier expansion.* Regard f_m (Lemma 1.1) as a function on ℤ/mℤ via the representative r ∈ [0, m); this is
  legitimate since its support (2U, 4U] ⊂ [0, m). Then
  f_m(x) = Σ_{b mod m} f̂_m(b)e(bx/m) with f̂_m(b) = (1/m)Σ_{r∈(2U,4U]} f_m(r)e(−br/m) = (1/m)S_m(b/m).
  With x = r_m(n) ≡ −n (mod m), Lemma 1.1 gives T_n(h) = Σ_{U²<m≤4U²} Σ_{b mod m} f̂_m(b)e(−bn/m).
* *Grouping by reduced fractions.* For each pair (m, b), write −b/m ≡ a/q (mod 1) with q | m, 0 ≤ a < q, gcd(a, q) = 1.
  Given q | m and a, there is exactly one b mod m, namely b ≡ −am/q. Hence
  T_n(h) = Σ_{q≤Q} Σ*_{a mod q} C(a/q)e(an/q), Q := 4U², C(a/q) := Σ_{U²<m≤4U², q|m} f̂_m(−am/q).
* *Large sieve.* The fractions a/q (q ≤ Q, (a, q) = 1) are distinct mod 1 and pairwise ≥ 1/Q² apart on ℝ/ℤ. The dual
  large sieve inequality (Montgomery–Vaughan) gives
  Σ_{N₀<n≤N₀+N} |T_n(h)|² ≤ (N − 1 + Q²)·Σ_{q≤Q}Σ*_a |C(a/q)|².
* *Coefficients.* By Lemma V, |f̂_m(b)| ≤ C_V√(hU)/m. Hence
  |C(a/q)| ≤ C_V√(hU)·Σ_{m∈(U²,4U²], q|m} 1/m = (C_V√(hU)/q)·Σ_{l∈(U²/q, 4U²/q]} 1/l ≤ 2.39·C_V√(hU)/q,
  using Σ_{l∈(A,4A]} 1/l ≤ 1/(⌊A⌋+1) + log(4A/(⌊A⌋+1)) ≤ 1 + log 4 for A > 0.
* *Sum.* Σ_{q≤Q}Σ*_a |C(a/q)|² ≤ Σ_{q≤Q} φ(q)·5.72C_V²hU/q² ≤ 5.72C_V²hU(1 + log Q). ∎

Primality is not used. EVIDENCE (`data/z55/tdo/scan_*.txt`): the empirical mean of |T|²/U is ≈ 1.5 at every scale
(Table 6.1), i.e. the bound is the right order up to C·17·log.

## 4. Theorem A: almost all primes, all U simultaneously

**Boundary counts.** For U₀ ≥ 9 and 1 ≤ G ≤ U₀ put
  B_n(U₀, G) := #{(s, m) ∈ ℤ²: s ∈ (2U₀, 4U₀+4G], m ∈ (U₀², 4(U₀+G)²], m | n + s, and
               [s ∈ S_∂ or m ∈ M_∂]},
  S_∂ := (2U₀, 2U₀+2G] ∪ (4U₀, 4U₀+4G],  M_∂ := (U₀², (U₀+G)²] ∪ (4U₀², 4(U₀+G)²].

**Lemma 4.1 (PROVED).** For U₀ ≤ U ≤ U₀ + G and all h, n: |T_{n,U}(h) − T_{n,U₀}(h)| ≤ B_n(U₀, G).
*Proof.* By the substitution s = km − n, T_{n,U}(h) sums the unimodular phase e(h√(s² − 4m)) (independent of U) over
the set P_U := {(s, m): s ∈ (2U, 4U], m ∈ (U², 4U²], s² − 4m ≥ 1, m | n + s}; the map (k, m) ↦ (s, m) is a bijection
onto P_U. So the difference is at most |P_U Δ P_{U₀}|. Both sets lie in s ∈ (2U₀, 4U₀+4G], m ∈ (U₀², 4(U₀+G)²]. A
point of P_{U₀} \ P_U has s ∈ (2U₀, 2U] or m ∈ (U₀², U²]. A point of P_U \ P_{U₀} has s ∈ (4U₀, 4U] or
m ∈ (4U₀², 4U²]. All four sets are inside S_∂ or M_∂. ∎

**Lemma 4.2 (PROVED).** For U₀ ≥ 9, 1 ≤ G ≤ U₀, N₀ ≥ 0, N ≥ 1:
  Σ_{N₀<n≤N₀+N} B_n(U₀, G)² ≪ (N + 256U₀⁴)(G² + G log U₀ + U₀), absolute implied constant.
*Proof.* B_n ≤ B¹_n + B²_n with B¹_n := #{(s,m): s ∈ S_∂, m ∈ M₀, m | n+s} and
B²_n := #{(s,m): s ∈ S₀, m ∈ M_∂, m | n+s}, where S₀ := (2U₀, 4U₀+4G], M₀ := (U₀², 4(U₀+G)²]. Since
|S₀| ≤ 6U₀ < U₀² < m (U₀ ≥ 9), for each m at most one s in S₀ has m | n + s, as in Lemma 1.1. So, for S ∈ {S_∂, S₀} and
M ∈ {M₀, M_∂}, the count Σ_{m∈M} 1_S(r_m(n)) has the finite Fourier expansion of §3 with f_m := 1_S and
f̂_m(b) = (1/m)E_S(−b/m), E_S(θ) := Σ_{s∈S}e(θs). Grouping as in §3 (Q := 4(U₀+G)² ≤ 16U₀²):
C(a/q) = (Σ_{m∈M, q|m} 1/m)·E_S(a/q), and Σ_n(count)² ≤ (N + Q²)Σ_{q≤Q}Σ*_a|C(a/q)|². Since S is a union of at most two
intervals, Σ_{a mod q}|E_S(a/q)|² = q·#{(s, s') ∈ S²: s ≡ s' (q)} ≤ q|S|(|S|/q + 2).
* B¹ (|S_∂| = 6G, M = M₀): Σ_{m∈M₀, q|m} 1/m ≤ (1/q)(1 + log 16) < 3.8/q (ratio of endpoints ≤ 16 as G ≤ U₀). So
  Σ_q Σ_a |C|² ≤ Σ_q 14.5q^{−1}·6G(6G/q + 2) ≪ G² + G log U₀.
* B² (|S₀| ≤ 6U₀, M = M_∂, two intervals of total length ≤ 10U₀G + 5G² ≤ 15U₀G): Σ_{m∈M_∂, q|m} 1/m ≤ U₀^{−2}(15U₀G/q + 2).
  So Σ_q Σ_a|C|² ≤ Σ_{q≤16U₀²} 2[(15G/(U₀q))² + 4U₀^{−4}]·q·6U₀(6U₀/q + 2)
  ≪ G²Σ_q(1/q² + 1/(U₀q)) + U₀^{−3}Σ_{q≤16U₀²}(U₀ + q) ≪ G² + U₀.
* Combine with (x + y)² ≤ 2x² + 2y². ∎

**Theorem A (PROVED).** Fix 0 < η < 1/8 and 0 < c₁ ≤ c₂. For X ≥ X₀(η, c₁, c₂), the number of primes p ∈ (X, 2X] for
which there exist an integer U with c₁p^{1/4} ≤ U ≤ c₂p^{1/4} and an integer 1 ≤ h ≤ U^η with |T_{p,U}(h)| > 2U^{1−η}
is ≪_{η,c₁,c₂} X^{1−η/4}. The same holds with "primes" replaced by "integers".

*Proof.*
* *Parameters.* U_* := c₁X^{1/4}, κ := 2^{1/4}c₂/c₁. Every admissible U for p ∈ (X, 2X] lies in [U_*, κU_*]. Put
  G := ⌈U_*^{1−3η}⌉, H₀ := (κU_*)^η, and grid points U₀ := ⌈U_*⌉ + jG ≤ κU_* (j ≥ 0); there are ≪ U_*^{3η} of them.
  For X ≥ X₀: U_* ≥ 9 and G ≤ U_*.
* *Exceptional sets at a grid point.* Let 𝓔₁(U₀) := {n ∈ (X, 2X]: ∃h ≤ H₀, |T_{n,U₀}(h)| > U_*^{1−η}}. By Theorem M
  (N = X, U₀ ≤ κU_*, X ≍ U_*⁴), |𝓔₁(U₀)| ≤ Σ_{h≤H₀}C(X + 16U₀⁴)hU₀ log(4U₀²)/U_*^{2−2η} ≪ X·U_*^{−1+4η}log U_*.
  Let 𝓔₂(U₀) := {n: B_n(U₀, G) > U_*^{1−η}}. By Lemma 4.2, |𝓔₂(U₀)| ≪ X(G² + G log U_* + U_*)/U_*^{2−2η}
  ≪ X(U_*^{−4η} + U_*^{−1+2η}).
* *Union over the grid.* Σ_{U₀}(|𝓔₁| + |𝓔₂|) ≪ X(U_*^{−1+7η}log U_* + U_*^{−η} + U_*^{−1+5η}) ≪ X·U_*^{−η} ≪ X^{1−η/4},
  using η < 1/8 (so −1 + 7η < −η).
* *Non-exceptional n.* Given an admissible U, take the grid point U₀ ≤ U < U₀ + G (it exists: ⌈U_*⌉ ≤ U ≤ κU_*, and
  the last grid point is > κU_* − G). For 1 ≤ h ≤ U^η ≤ H₀, Lemma 4.1 gives
  |T_{n,U}(h)| ≤ |T_{n,U₀}(h)| + B_n(U₀, G) ≤ 2U_*^{1−η} ≤ 2U^{1−η}. ∎

**Remark 4.3 (downstream value; PROVED).** The almost-all-p form of the *conclusion* of Corollary T needs none of the
above. For U₀ ≤ U ≤ U₀ + G, N₂(n, U) ≤ #{(u, B) ∈ (U₀, 2U₀+2G]²: uB | n + u + B}, whose sum over n ∈ (X, 2X] is
≤ Σ_{u,B}(X/(uB) + 1) ≪ X. Markov at level U^{1−η} plus a union over ≪ U^{3η} grid points gives N₂(p, U) ≤ U^{1−η} for
all admissible U, for all but ≪ X·U^{−1+4η} primes p ∈ (X, 2X]. So Theorem A adds nothing for the (★) block. The open
content of TD is the **pointwise** (every p) statement.

## 5. Numerics (EVIDENCE)

`scripts/z55_tdo_T.c` (single p) and `scripts/z55_tdo_scan.c` (scan; U = ⌊c·n^{1/4}⌋, here c = 1; max over
1 ≤ h ≤ 8). Build: `gcc -O2 -o /tmp/z55_tdo_scan scripts/z55_tdo_scan.c -lm`.

**Table 5.1.** 200 consecutive primes from 10^e + 1 (row "all n": 300 consecutive integers from 10¹²).

| set | U | mean \|E1⁺\|/U | mean of max_h\|T(h)\|/√U | max of max_h\|T(h)\|/√U | mean over h of \|T(h)\|²/U |
|---|---|---|---|---|---|
| primes ~1e8 | 100 | 1.51 | 1.99 | 3.90 | 1.52 |
| primes ~1e10 | 316 | 1.52 | 1.92 | 3.50 | 1.45 |
| primes ~1e12 | 1000 | 1.54 | 2.01 | 3.13 | 1.53 |
| primes ~1e14 | 3162 | 1.54 | 2.00 | 3.53 | 1.53 |
| all n ~1e12 | 1000 | — | — | 3.71 | 1.58 |

Mean |T(h)|² ≈ |E1⁺| (random-phase prediction), max/√U flat in U: square-root size, as stated in the brief.
Odd squares n = a², a = 1000001, …, 1000015 (U = 1000): max_h|T(h)|/√U ∈ [0.99, 2.59], mean |T|²/U ∈ [0.70, 2.71]
(`scan_squares_e12.txt`). There is no visible anomaly at squares. That is expected, because TD is an upper bound and does
not imply ES.
Sanity check: p = 100000037, U = 100 gives |E1| = 253 and N₂ = 1, matching Z54_BILINDIV §3 (k = 5176, roots 115, 168).

## 6. Where the pointwise argument stops (Assessment)

* In Theorem M the only input is Lemma V (cancellation in r, the short variable). The average over n supplies the
  rest through the large sieve. For a single n, the large-sieve factor N + Q² is replaced by Q² ≍ U⁴ with nothing to
  divide by: the moduli m ≍ U² have Q² ≍ p.
* For fixed p, every one-variable route tried (Fourier in r then sum over m, or the reverse; Erdős–Turán in the
  residue p mod m; Weyl differencing in m) ends at ≥ |E1| ≍ U, even with square-root inputs in each variable. The
  reasons are the following.
  * The candidate set has density 1/U in m.
  * The dual frequencies ν ≍ hU² must be summed with absolute values.
  * After a Poisson step in m the problem is self-dual at the fourth-root point: the phase νp/m has second derivative
    ≍ h ≥ 1 on m ≍ U².
* A pointwise saving would need joint cancellation in a two-dimensional sum of Voronoi type, e.g.
  Σ_{ν,μ≍U} e(2√(pνμ) + …) ≪ U^{3/2−η}, against a trivial bound of U² and a square-root size of U. This is the
  N ≍ √x block of the Dirichlet-divisor Voronoi series at the strength θ ≤ 1/4 − η′. Known exponents (θ ≈ 0.315) give
  only ≈ U^{1.76} for this block.
* Status: TD is at least as hard as the pointwise asymptotic for divisor sums in intervals of length x^{1/4} (a
  heuristic equivalence, not a proved implication).

## 7. Files

* `scripts/z55_tdo_T.c`: T(h), |E1|, |E1⁺|, N₂ for a single (p, U).
* `scripts/z55_tdo_scan.c`: scan over primes or integers.
* `scripts/z55_tdo_lemV.py`: Lemma V check.
* `data/z55/tdo/scan_e{8,10,12,14}.txt`, `scan_all_e12.txt`, `scan_squares_e12.txt`, `lemV.txt`.
  Scan columns: n, U, |E1⁺|, max_h|T|, argmax h, mean_h|T|².
