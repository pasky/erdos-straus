# Hostile review: EXCEPTIONAL_TWIN3.md (task O5), commit 2bbe184

Subject: Theorem 4.1 ((H_O) unconditional) and Corollary 4.2 (two-prime Λ²
cap `≪ L^{3/4}(log L)^{O(1)}` unconditional in Setting 3.0), via (2.1),
Lemma 2.1, Lemmas 3.1–3.4, Cor 3.3. Context checked against
EXCEPTIONAL_TWIN2.md (TW2: Setting 1.0, Lemma 2.2, Setting 3.0, Lemmas
3.2–3.3, (3.1), Thm 5.1, Lemmas 5.3–5.4) and reviews/exceptional-twin2-review.md.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
E1, E2, … (severity: major / minor / nit).

## Item 1. Is S_j the right quantity? (2.1) bookkeeping — SOUND

* TW2 Lemma 2.2 defines `S_ℓ = Σ_a ν_ℓ(a) min(deg(ℓ,a),1)²` with
  `deg(ℓ,a) = Σ ν_m(c)` over edges of Setting 1.0 at the vertex `(ℓ,a)`,
  `a ∈ Ω_ℓ ⊆ ℤ/ℓ^{e_ℓ}`; Theorem 5.1 uses this S_j with the active binary
  classes of fibre c as edges. Counting classes with multiplicity (several
  classes can give the same edge) and ignoring the removal of unary vertices
  only enlarges deg, so every bound in TW3 on a class-indexed deg is an
  upper bound for TW2's S_j. A `kjm`-class constrains `y_j` only mod j, so it
  produces an edge at every lift of its residue; `deg(j,a)` then depends on
  `a mod j` only, and `Σ_{lifts} ν_j ≤ (8/7)/j` on supp P. Partner weight:
  `Σ_{lifts b} ν_m(b) ≤ (8/7)/m`. Both are what TW3 uses (§2, Lemma 3.4).
* Prime-power split (TW2 D5): `min(x+y,1)² ≤ min(x,1)² + 3y` re-checked
  (cases `x+y ≤ 1`; `x ≥ 1`; `x < 1 < x+y`, where `1−x² ≤ 2(1−x) < 2y`).
* (2.1): `min(x+z,1) ≤ min(x,1)+z` for `x,z ≥ 0`; `(p+q)² ≤ 2p²+2q²`;
  `min(x,1)² ≤ min(x,1) ≤ x`. Then `Σ_a ν_j(a)x(a) = w_j^{sm}(c)` by
  definition of x. Correct, with no label restriction, as claimed.
  Each binary class is counted at both endpoints, with the small/large
  split taken relative to the vertex; this is consistent (Lemma 2.1 covers
  "small at j", Lemma 3.4 "large at j", for every j).
* Numerical check (own code, item 6): (2.1) and the D5 inequality tested on
  10⁶ random `(x,y,z)` triples incl. edge cases; no violation.

## Item 2. Lemma 2.1 (first moment of the small part) — SOUND (nits E1, E2)

Re-derived line by line.
* Setup: on supp P, `ν ≤ (8/7)U` at both ends, activity `≤ 4Γ(k)/k` (TW2
  Lemma 3.2(1), k w₂-smooth — this is where "at most two primes above w₂"
  is used: every binary modulus is `kjm` with k dividing `Q_F`), `≤ τ(A²)`
  classes per modulus. Correct.
* (a) j top: `M ≤ j^{1+B}` ⇒ `km ≤ j^B`; A is linear in j with slope km, so
  TW2 Lemma 3.3 applies with `q = km` and j as the running variable.
  Blocks `(y,2y]` with `km > (2y)^B` contain no family modulus and can be
  dropped, so the hypothesis `q ≤ (2y)^{B+2}` holds on every block used.
  `Σ_i y_i^{−α}(a + i log 2)² ≤ m^{−α}·2^{α}(a²/α + a/α² + 1/α³)` and the
  prime sums `Σ_{m>w₂} m^{−1−α}(log m)^i ≪ (i−1)!α^{−i}` (`i ≥ 1`),
  `≪ log L` (`i = 0`; indeed `= E₁(8α log L)+O(1) ≈ (1/4)log L`) give
  `≪ (k/φ(k))[α^{−3}log L + (log 2k)²α^{−1}log L + …]` — at most the
  stated `(k/φ(k))(log 2k)²α^{−3}log L`.
* (b) m top, `j < m ≤ (kj)^{C₀}`: `kj ≤ m^B` gives Lemma 3.3 with `q = kj`;
  `≤ C₀log₂(kj)+2` blocks, each `≪ (kj/φ(kj))(C₀+2)²(log 2kj)²`. Then
  `(log 2kj)³ ≤ 4((log 2k)³ + (log j)³)` and `Σ_j j^{−1−α}(log j)³ ≪ 2α^{−3}`.
  Correct; m-primality indeed unused.
* k-sum: `Σ_k Γ(k)(log 2k)³/φ(k) ≪ (log L)^{O(1)}` is TW2 (3.1) with i = 3.
  The total is `≪ α^{−3}(log L)^{O(1)}` — the whole α^{−3} budget, as the
  author says (Remark 2.2). This is the only place where α^{−3} appears.
* **E1 (nit).** (a) should say explicitly that blocks with `km > (2y)^B`
  are empty and dropped; as written ("holds because `km ≤ j^B ≤ (2y)^B`")
  the reader must supply that the hypothesis is only needed on non-empty
  blocks.
* **E2 (nit).** In (a), `a = log(2km²)` vs the first block `y₀ = m/2`:
  `log(2km·y₀) = log(km²)`, so `a` is an upper bound, fine; but the stated
  intermediate `(k/φ(k)) m^{−α}(…)` silently absorbs `(m/2)^{−α} ≤ 2m^{−α}`
  and `m/φ(m) ≤ 2`. Harmless constants.

## Item 3. Lemma 3.1 (largest-variable reduction) — SOUND (nit E3)

* Parametrisation `A = uvt`, `(u,v) = 1`, `D = u²t`, `D̄ = v²t`: bijective
  (`D/A = u/v` in lowest terms ⇒ `uv | A`). `(uvt, kj) = 1` from `4A ≡ 1`.
  (3.1): `−4u²t = −u·(4ut) ≡ −u/v`; `(4u²t)(4v²t) = 16A² ≡ 1` gives
  `−4D ≡ −1/(4v²t)`. Correct (and machine-checked, item 6).
* Ties t,u,v: each triple goes to exactly one case; the case condition used
  is only "chosen variable ≥ the other two", which is what the
  `A ≥ (short product)·max(short)` constraint encodes. No double counting.
* t largest: fixed coprime `(u,v)`, `uv | A_m ⇔ kjm ≡ −1 (mod 4uv)` — one
  *reduced* class (`(4uv, kj) = 1`), and `t ≥ max(u,v) ⇔ m ≥ (4uv·max−1)/kj`.
  Bijection with m checked numerically (item 6).
* **Author flag `M₁ ≥ q w₂/8`: correct.** Branch `max ≥ (kj)²`:
  `M₁ ≥ (q(kj)²−1)/kj ≥ q·kj − 1 ≥ q w₂/8`. Branch `max < (kj)²`:
  `q < 4(kj)^4`, `M₁ ≥ (kj)^{C₀} > q(kj)^{C₀−4}/4 ≥ q w₂/8` — needs only
  `C₀ ≥ 5`. In fact BT needs only `y/q ≥ e` on every block; the log L comes
  from the ≤ 2L blocks, not from ℓ₀, so the margin is large. The role of
  C₀ is exactly to exclude `q ≈ (kj)^4` against `m ≈ w₂`, where BT fails.
* BT (Montgomery–Vaughan 1973, Thm 2: `π(x+y;q,b)−π(x;q,b) < 2y/(φ(q)log(y/q))`,
  `1 ≤ q < y`): each block `(y,2y]` contributes `< 2/(φ(q)log(y/q))`;
  `Σ_{i≤2L} 1/(ℓ₀+i log 2) ≤ 1/ℓ₀ + (log 2)^{−1}log(1+2L log 2/ℓ₀) ≤ 1+1.5log(1+2L)`;
  `2+3log(1+2L) ≤ 4 log L` for `L ≥ e^5`; `φ(4n) ≥ 2φ(n)`. Correct.
  Primality of m is essential here (without it `Σ1/m ≍ L/φ(q)` and the
  final bound becomes `L²·polylog`, over budget) — and m is prime in the
  binary setting, so fine.
* **Author flag "dropped coprimality": correct.** In the u- and v-largest
  cases `(u,v) = 1` is dropped; given the short pair and m, the long
  variable is determined (`A_m/(vt)`), so the map triple ↦ (short pair, m)
  stays injective and the bound is an upper bound.
* **E3 (nit).** "Cover `(M₁, X]` by at most 2L dyadic blocks `(y,2y]` with
  `y ≥ M₁/2`" — the range is `(M₁, X/(kj)]`, and the first block should be
  `(M₁/2, M₁]`∪… or start at `y = M₁`; as written ℓ₀ uses `M₁/2`. Harmless.

## Item 4. Lemma 3.2 and Corollary 3.3 (box counting) — SOUND (nit E4)

* r, diagonal: `v = ga, v′ = gb, (a,b)=1, a²t = b²t′ ⇒ t = b²s, t′ = a²s`,
  weight `1/(g²a³b³s²)`, sum `≤ ζ(2)²ζ(3)²`. Correct.
* r, off-diagonal: distinct `N ≡ N′ (j)`, both ≥ 1 ⇒ `max > j`; ordered
  off-diagonal `≤ 2ΣϱΣ sup_c T(c)` with `T(c) = Σ_{N′≡c, N′>j} ϱ(N′)`.
  Box `[V,2V)×[T,2T)`: `≤ V(T/j+1)` (t in one class) and `≤ 2T(V/j+1)`
  (≤ 2 square roots mod the prime j); min of the two
  `≤ 2VT/j + 2min(V,T)`; weight ≤ `1/(VT)`; meets `{v²t > j}` only if
  `V²T > j/8`, hence `max(V,T)³ > j/8`; `2i+1` boxes have `max = 2^i`.
  Correct; `Σ_{2^i>(j/8)^{1/3}} (4i+4)2^{−i} ≪ j^{−1/3}log j`.
* r₁: distinct reduced fractions with `u/v ≡ u′/v′ (j)` give
  `0 ≠ uv′−u′v ≡ 0`, so `H·H′ ≥ j` (even better than the stated `j/2`);
  charging to the higher member and the box count
  `≤ UW/j + min(U,W)` are correct.
* Cor 3.3: `n/φ(n) ≤ 2 log L` for `n ≤ X` (`e^γ log log n + O(1/loglog n)`),
  applied to u and v separately via `φ(xy) ≥ φ(x)φ(y)`; the maps
  `a ↦ −a, −1/(4a), −a/4` are bijections of nonzero residues (a = 0 gives
  empty R's). `Σ_a V² ≤ 3(2log L)²·(2log L)⁴[Σr₁² + 2Σr²]`, and with
  `log X = L`, `j > L^8`: error `≪ L^{−4} + L^{−2/3}log L`. So
  `Σ_a V_{j,k}(a)² ≪ (log L)^6` uniformly in `j > w₂` and k. Correct.
* **Numerical check (own code, `reviews/exceptional-twin3-check.py A`).**
  Besides the second moments (which reproduce the author's §5 table exactly
  at Y = 600), the script computes the quantities the proof actually bounds
  — the sup tails `sup_c T(c)`, `sup_ρ T₁(ρ)` — and the explicit box bounds:

  | j | Y | diag r (≤3.910) | sup T / box bd | diag r₁ (≤2.706) | sup T₁ / box bd |
  |---|---|---|---|---|---|
  | 101 | 600 | 3.8125 | 0.542 / 10.40 | 2.4950 | 0.377 / 5.20 |
  | 1009 | 600 | 3.8131 | 0.103 / 5.16 | 2.4954 | 0.063 / 1.58 |
  | 10007 | 600 | 3.8131 | 0.027 / 2.93 | 2.4954 | 0.022 / 0.47 |
  | 101 | 2000 | 3.8322 | 0.729 / 11.28 | 2.4982 | 0.495 / 5.64 |
  | 1009 | 2000 | 3.8329 | 0.124 / 5.28 | 2.4986 | 0.074 / 1.64 |
  | 100003 | 2000 | 3.8329 | 0.009 / 1.70 | 2.4986 | 0.005 / 0.26 |

  Also checked: off-diagonal ≤ `2·Σ·sup T` in every row. No violation; the
  box bound is loose by 10–200×, as expected. The r-diagonal approaches
  `ζ(2)²ζ(3)² = 3.910` from below as Y grows (tight constant).
* **E4 (nit).** Lemma 3.2 assumes "`X ≥ j`" — not needed; and the r₁ proof
  says `max(u,v)·max(u′,v′) ≥ j/2` where `≥ j` holds (`|uv′−u′v| ≤ HH′`).

## Item 5. Lemma 3.4 (large part of (2.1)) — SOUND

* For `u = v = 1` classes `deg^{lg}(j,·)` factors through `a mod j`;
  `Σ_{lifts} ν_j ≤ (8/7)/j` and `ν_m ≤ (8/7)/m` hold pointwise on supp P
  (`p_j ≤ 1/8` on `G_L`), so they come out of `E_P` deterministically.
* Expanding `z(a)²` over ordered pairs of classes (diagonal pair included,
  where the pair probability is `P(C active) ≤ 4Γ(k)/k`, consistent);
  incompatible residues mod `gcd(k,k′)` give probability 0 ≤ bound. Both
  active ⇔ one congruence mod `lcm(k,k′) | Q_F` ⇒ `≤ 4Γ(lcm)/lcm`
  (TW2 Lemma 3.2(1)). So `E_P Σ_a ν_j z² ≤ 4(8/7)³ j^{−1}
  Σ_{a mod j}Σ_{k,k′}(Γ(lcm)/lcm)V_{j,k}(a)V_{j,k′}(a)`. Correct.
* AM–GM: the weight `c(k,k′) = Γ(lcm)/lcm` is symmetric, so
  `Σ c V_kV_{k′} ≤ Σ_k V_k² Σ_{k′}c(k,k′)`; `Γ(lcm) ≤ Γ(k)Γ(k′)` (Γ depends on
  the prime support, factors ≥ 1) gives `Σ_{k′}c ≤ Γ(k)h(k)/k`. Correct.
* Uniformity of Cor 3.3 in k is genuine (no k enters Lemma 3.2; k enters
  Lemma 3.1 only through `(kj)^{C₀}` and `(4uv, kj) = 1`), so the k-sum is
  `Σ_k Γ(k)h(k)/k ≪ (log L)^{O(1)}` (Euler product, TW2 5.4(iii)), and
  `Σ_{j>w₂} ρ_j/j ≪ log L`. The large part does not even need ρ_j.
* Sanity of scale: the large-partner mass at j is `≍ L²log L/j` but its
  `ν`-weighted second moment is `(log L)^{O(1)}/j`; the hub `a = −1`
  (`D = A`, every m) has `V(−1) ≤ Σ_{m∈𝓜} 1/m ≤ log L`, consistent with
  the bound. Nothing hidden.

## Item 6. Theorem 4.1 / Corollary 4.2 (assembly; scope; inherited inputs) — SOUND-AFTER-REPAIRS (E5 minor)

* Assembly: `S_j ≤ S_j^{(11)} + 3w_j^{pp}` (TW2 D5, in main), (2.1),
  Lemma 2.1 (`≪ α^{−3}(log L)^{O(1)}`), Lemma 3.4 (`≪ (log L)^{O(1)}`),
  prime powers `≪ L³/w₂ + w₂^{−1/2}(log L)^{O(1)} = o(1)`. Plugged into
  TW2 Thm 5.1 (`11·E_PΣρ_jS_j`) this gives Cor 4.2. **I find no gap: (H_O)
  as defined in TW2 §5 is proved, and Cor 4.2 follows.**
* **"At most two primes above (log X)^8" — used where needed.** (i) TW2
  Thm 5.1 itself (edges are binary; no ternary classes); (ii) every binary
  modulus is `kjm` with k w₂-smooth, i.e. `k | Q_F`, which is exactly what
  the activity inflation `4Γ(k)/k`, `4Γ(lcm)/lcm` (TW2 Lemma 3.2(1)) in
  Lemmas 2.1 and 3.4 requires. Lemmas 3.1–3.2 do not need it. Not needed
  anywhere else.
* **B-hypothesis** (TW2 review D3): used in Lemma 2.1 (Shiu along the top
  prime, both cases) and inherited from Thm 5.1 / D5; Cor 4.2 states it.
  Lemmas 3.1–3.4 do not use B.
* **Inherited inputs** — TW2 Lemma 3.2(1), Lemma 3.3, (3.1), Lemma
  5.4(ii)–(iii) and the D5 split, Thm 5.1 — are all SOUND or
  SOUND-AFTER-REPAIRS in reviews/exceptional-twin2-review.md, with the
  repairs (D5) present in main's TW2. Used with the stated hypotheses.
* **E5 (minor, logic of the labels).** "Theorem 4.1 ((H_O), hence
  (H_O^≠))", the Remark "(H_O^≠) … is absorbed into the two bounds above",
  and AGENT_REPORT_O5 "That covers (H_O^≠) and gives (H_O^=) again" are
  wrong as implications. In TW2, (H_O^=) and (H_O^≠) are *un-quarantined*
  pair sums (`Σ x_C x_{C′}`, i.e. parts of `q_j = Σν deg²`), and the route
  was `S_j ≤ q_j`; so (H_O^=)+(H_O^≠) ⇒ (H_O), not conversely. TW3 bounds
  `q_j` only for large–large pairs (Lemma 3.4 is un-quarantined); the
  small–small and small–large pairs are paid by the first moment through
  `min(x,1)² ≤ x`, which says nothing about `Σ x_C x_{C′}`. So (H_O^≠) as
  stated in TW2 §5.1/TW3 §1 is **not** proved; it is **bypassed** (no
  longer needed for Cor 5.2), like H_div. Fix: "(H_O) proved; (H_O^≠) and
  H_div bypassed (no longer needed; open as stated)". Cor 4.2 is
  unaffected.

## Item 7. Exposition, numerics, replay — SOUND-AFTER-REPAIRS (nits E6–E9)

* **Replay.** `scripts/twin3_system.py 1e9 1 1009 10007 100003` reproduces
  the §5 system table exactly (~10 min); my own `partA` reproduces the
  Lemma 3.2 table at Y = 600 exactly. Own Lemma 3.1 check
  (`reviews/exceptional-twin3-check.py C`: j = 11, k = 1, C₀ = 5, 100 914
  prime partners `m ∈ (11⁵, 3·10⁶]`, 11.8M triples, 223 723 short-pair
  keys): (3.1) residue identity 0 failures; every (key, m) in the predicted
  class mod `4·(short product)` with `A_m ≥ (short product)·max` — 0
  failures; injectivity 0 failures; `M₁ ≥ q·kj/8` (the w₂-analogue) 0
  failures; on 1500 sampled keys the t-case set *equals* the predicted
  prime set and the u/v-cases are contained in it; per-key
  `Σ1/m ≤ (2/φ(q))Σ_blocks 1/log(y/q)` holds with worst ratio 0.26.
* **E6 (nit).** §5 "(2.1) holds in every row, with a factor 5–13 to spare":
  the rows give 79.8/15.4 = 5.2, 118.0/7.3 = 16.2, 218.3/16.4 = 13.3, i.e.
  5–16.
* **E7 (nit).** §1 Route 3 asserts as fact "When `km ≤ j^{1−ε}` there are
  O(1) divisors of A² per class mod j" (Lenstra/CHN). Plausible via
  Coppersmith–Howgrave-Graham–Nagaraj (`A² ≤ j^{4−2ε}`, so
  `j ≥ (A²)^{1/4+δ}`), but unproved here and unused; mark as heuristic or
  delete.
* **E8 (nit).** §4 Remark "This needs the largest of u, v, t to be
  `≥ A^{1/3}`, which holds once `m > (kj)^{C₀}`": the largest is always
  `≥ A^{1/3}`; what `m > (kj)^{C₀}` buys is `M₁ ≥ q w₂/8` (BT range longer
  than the modulus `4·short product`, which can be `≈ 4(kj)^4`). Reword.
  Likewise §2 "Fix C₀ ≥ 6" — C₀ ≥ 5 suffices (Item 3).
* **E9 (nit, ledger).** On merge: TW2 §0 / Cor 5.2 / §5.4–5.5 still say
  (H_O)/(H_O^≠) OPEN and Cor 5.2 CONDITIONAL; they need a forward pointer
  to TW3 Thm 4.1, and DISCOVERIES should record "(H_O) PROVED,
  (H_O^≠)/H_div bypassed (still open as stated)" per E5.

## Summary

| item | verdict | defects |
|---|---|---|
| 1 S_j definition, (2.1), D5 split | SOUND | — |
| 2 Lemma 2.1 (small first moment) | SOUND | E1, E2 nits |
| 3 Lemma 3.1 (largest-variable reduction, BT) | SOUND | E3 nit |
| 4 Lemma 3.2, Cor 3.3 (box counting) | SOUND | E4 nit |
| 5 Lemma 3.4 (large part) | SOUND | — |
| 6 Thm 4.1, Cor 4.2 (assembly, scope) | SOUND-AFTER-REPAIRS | E5 minor |
| 7 Exposition, numerics, replay | SOUND-AFTER-REPAIRS | E6–E9 nits |

**Bottom line.** I could not break Theorem 4.1. (H_O) as defined in TW2
§5 is proved, and Cor 4.2 — the two-prime Λ² cap
`saving(g²) ≪_{A₀,B} L^{3/4}(log L)^{O(1)}` in Setting 3.0 (`M ≤ X`,
`M ≤ P(M)^{1+B}`, ≤ 2 primes above `(log X)^8`, twins included) — is
unconditional modulo the already-reviewed TW2 inputs. The key idea (sum
over the prime partner first, in the class mod 4·(two short variables),
which is long because `m > (kj)^{C₀}`; quarantine pays for the small
partners by their first moment) is correct and the author's flagged
points all check out. The one substantive correction is E5: (H_O^≠) and
(H_O^=) in TW2's un-quarantined form are *bypassed*, not proved; the
status lines must say so. No major defect.
