# Hostile review R93 of POINTWISE_MORDELL17B.md (task O93)

Reviewer: R93 (branch `side-agent/review-m17b`). Document reviewed at the merge of
`side-agent/r17-explicit-tail` into this branch. From-scratch scripts: `scripts/review_m17b_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (union = P ∪ Q; U ⊂ P, Q⁻¹ = Q, odd levels) | SOUND |
| Lemma 2.1 (cover, `acde ≤ n`, recovery formulas) | SOUND |
| P-enumerator completeness; D_P(K), K ≤ 13 | SOUND. Sets equal to two from-scratch engines for K ≤ 11; count equal at K = 13 |
| Computation 3.1 (ρ₁, ρ₂) | SOUND. Both reproduced exactly; the §3 table level-7 measure is wrong (m3) |
| Theorem 4.1 (reduction) | SOUND as a statement (its hypothesis is the inequality `T_P + T_Q < ρ₁`) |
| Theorem 4.1 table / "constant 1.41 suffices" | **SOUND-AFTER-REPAIRS (M1)**: 1.41 is inadmissible, C_max = 1.40980 |
| Conjecture 4.2 | SOUND-AFTER-REPAIRS (label, m7) |
| Lemma 5.1 | SOUND (hidden `17 ∤ ab`, harmless; m4) |
| §5 prose, Assessment 5.2 | GAP in the obstruction analysis (m5, m6). The conclusion "no unconditional sterile point" stands |

No FATAL defects. Overall: the CONDITIONAL outcome is correct, and every number except the ones listed below was reproduced
independently.

## Claim (1): Lemma 2.1 and the P-enumerator

**Re-derivation of `acde ≤ n`.** For an N-point of `Σ^II_n` (`4abcd = a+b+nc`, `e = (a+b)/c`), dividing
by c gives `4abd = n+e`. As `c ≥ 1`, `e ≤ a+b ≤ 2b ≤ 2abd` (using `a ≤ b`, `a, d ≥ 1`), so
`4abd ≤ n + 2abd`, `abd ≤ n/2`, and `acde = ad(a+b) ≤ 2abd ≤ n`. Only the equation and positivity are
used. Then `e²·(ad)(ac)(cd) = (acde)² ≤ n²`. If all four quantities exceeded their thresholds the product
would be `> X_e² X_ad X_ac X_cd ≥ n²`. So the cover is correct. VERIFIED.

**Recovery formulas.** `e`: `4abd = n+e` (above). `ad`: `ef = n+4a²d` with `f = 4acd−1` (ET (2.19)/(2.20)
area; re-derived: `e(4acd−1) = 4acde − e = 4ad(a+b) − e = 4a²d + (4abd − e) = 4a²d + n`). `ac`: from
`b(4acd−1) = a + nc`. `cd`: `(4acd−1)(4bcd−1) = 16abc²d² − 4cd(a+b) + 1 = 4cd(4abcd − a − b) + 1 = 4c²dn + 1`.
All four are correct, and each regime recovers the whole point from the pair plus a divisor. VERIFIED.

**Code reading (`m17b_penum.py`).** The thresholds are exact integers with `Xo⁴·Xcd ≥ n²` asserted. In each regime the
loops cover all pairs with product ≤ X, and all divisors of the factored number. Skipping `17 | d` (ad), `17 | c` (ac)
and `17 | cd` (cd) is legitimate, since such points are discarded anyway. The `e`-regime restriction `a² ≤ abd` is
implied by `a ≤ b`. Every output is re-checked against the equation. No defect found.

**Independent test.** `scripts/review_m17b_brute.c` is a naive scan that does *not* use the cover. For every `a ≤ b`
with `4ab ≤ n+a+b`, `e` is forced to be the least positive residue of `−n mod 4ab`, since `0 < e ≤ a+b < 4ab`.
Then `d = (n+e)/(4ab)`, `c = (a+b)/e`, and the equation is checked in 128-bit.
Results, compared with `m17b_penum.py` **as sets of (a,b,c,d)**:
* K = 1, 3, 5, 7: 2, 32, 121, 258 data; set-equal.
* K = 2, 4, 6: 0 data (consistent with M17 Lemma 1.3).
* K = 9: 604 data; set-equal (naive scan, 2 cores, ≈ 6 min).
* K = 7, 9 also with the second engine `scripts/review_m17b_k11.c` (below); set-equal.

For K = 11 the naive scan is too slow (≈ n log n). `scripts/review_m17b_k11.c` is a second from-scratch engine that is
complete by its own argument and uses no external factoriser:
* `a ≥ 50`: naive scan over `(a,d)`. For each, `b` runs over the short interval forced by `1 ≤ e = 4abd − n ≤ a+b`.
* `a < 50`: from `acde ≤ n`, either `e ≤ X = 10⁷` or `cd ≤ n/(aX)`. For `e ≤ X`, the numbers `n+e` are factored by a
  segmented sieve, and all divisors `d` of `(n+e)/(4a)` are tried. For `cd ≤ n/(aX)`, `f = 4acd−1 | nc+a` is tested directly.
(In the K = 11 data, 420 of the 836 points have `a < 50`, so both parts matter.)

**Code reading, `factor`.** Coreutils `factor` gives a Miller–Rabin probable-prime verdict, then a Lucas
proof (`PROVE_PRIMALITY`). A wrong "prime" verdict would lose divisors and so lose data; for K ≤ 11 the
independent engines exclude this. For K = 13 the R93 engine agrees in count (below).

## Claim (3): Lemma 1.1 and Theorem 4.1

**Lemma 1.1, re-derived.** The pieces are as follows.
* Q⁻¹ = Q as sets of boxes. A (Q)-datum has `4abd − 1 = 17^k e`, so `17 ∤ b` and the box is `−4a²d ≡ −a/b`. The reflection
  `(b,a,c,d)` is again an N-point of `Σ^I` (equation (2.3) is symmetric in a, b) with the same `e`, so it is also a (Q)-datum,
  with box `−b/a = (−a/b)⁻¹`. Hence Q⁻¹ ⊂ Q, and so `NB_Q ≤ 2D_Q`. My union code confirms this: every in-cell Q box is also a Q⁻¹ box.
* √Q = ∅: M17 Lemma 1.3 (reciprocity). My union code asserts that `−4a²d` is a non-residue for every Q-datum (k ≤ 5).
* U ⊂ P in the cells: M17 Lemma 5.2. The P-box lies at level `⌈(α−β)/2⌉`, at some K, and it is counted by the P-union whatever K is.
  Since U⁻¹ = (U-box meeting C_7)⁻¹ and P is inversion-closed, U⁻¹ is covered too. My union code finds no new U/U⁻¹ box at any level.
* P-boxes sit at level `(K+1)/2`, and only odd K occur (M17 Lemma 1.3). The nested boxes for `α ≤ K/2` (M17 Lemma 2.3) are
  dominated by the one of lowest level, `⌈K/2⌉`. Q occurs only at odd k. So T_Q starts at k = 9 and T_P at K = 11 (level 6).
* Measure: a level-L box has cell-relative measure `17^{1−L}`; for P, `17^{(1−K)/2}`. Correct.
* Strict `T_P + T_Q < ρ` gives a covered measure below 1, so the complement in `C_5` is nonempty. Inversion maps the union to
  itself and `C_5` to `C_7`, so `C_7` follows. Correct.
Verdict: SOUND.

**Theorem 4.1 table, recomputed** (`scripts/review_m17b_tail.py`, closed-form geometric sums, mpmath). C_max = (ρ − T_Q)/(2S),
where `S = Σ_{K≥K0 odd} 17^{θK+(1−K)/2}`:

| θ | 0.25 | 0.30 | 0.35 | 0.40 | 0.42 | 0.45 |
|---|---|---|---|---|---|---|
| K0 = 13, ρ₁ | 619.21 | 87.888 | 11.768 | **1.40980** | 0.56866 | 0.12750 |
| K0 = 15, ρ₂ | 2553.0 | 272.96 | 27.533 | 2.4845 | 0.89479 | 0.16926 |

(θ is taken as an exact rational, e.g. 2/5.)

`T_Q = 1.4106·10⁻³` (θ_Q = 3/5, C = 1) and `0.0765` (3/4), as claimed. The polynomial variants are also as claimed:
2K³ → 4.005·10⁻⁴, K⁴ → 2.64·10⁻³, K⁵ → 3.49·10⁻², and Conj. 4.2 (2K³, 3k³) → 4.007·10⁻⁴.
The data ratios `D_P/17^{0.4K}` match as well.
Several table entries are rounded **up**: 87.9, 11.8, **1.41**, 0.569, 0.128, 273, 2.49. In particular the headline
constant fails. At θ = 2/5, C = 1.41, K0 = 13: `T_P + T_Q = 0.677230 > ρ₁ = 0.677133`. See defect M1.

## Claim (4): Lemma 5.1 and the §5 obstruction

**Lemma 5.1, re-derived.** The lemma silently assumes `17 ∤ ab`. If `17 | ab`, then 17 is not a unit mod `m = 4ab`, and
"residue classes mod ord_m(17)" is meaningless. Such pairs exist (`17 | a`, `17 | b`, `17 ∤ cd`), but their boxes are
`≡ 1 (mod 17)` (M17 Lemma 5.1 remark), so they do not meet the cells and the gap is harmless. Under `17 ∤ ab`:
* `0 < e ≤ a+b < 4ab`, so `e` is the least positive residue of `−17^K`, and `17^K ≡ −e` fixes K mod `ord_m(17)`.
* There is one class per admissible `e`.
* Nesting inside a class holds: same `(a,b,c)`, and only `d` varies with K.
SOUND.

It is also *weaker than available*. By M17 Lemma 5.1(ii), **every** box of the pair `(a,b)`, for every K and every class,
is the ball of radius `17^{−(K+1)/2}` around `−a/b`. So all boxes of a pair are nested, and
`T_P ≤ 2 Σ_{(a,b)} 17^{(1−K_min(a,b))/2}`, with a single term per pair. Pairs with an admissible `K ≤ 11` (or `≤ 13`)
contribute nothing at all. This is not a defect of the lemma. But the sentence "This is the same sum as
`Σ_K 17^{(1−K)/2} NB_P(K)`, only reorganised" is wrong: the Lemma 5.1 sum is ≥ the NB-sum, not equal to it (defect m4).

**§5 prose.** Three statements in it need correction:
* "Averaging over K gives no unconditional gain" (bold) is a heuristic judgement, not a proved statement. It is unlabelled
  and should be an Assessment (m5).
* "Pairs with `ord_{4ab}(17) = L` … live at levels `≲ L/2`" is not right. The first admissible K lies in
  `[K_min, K_min + L)` with `K_min ≈ log_17(4ab) ≤ L`. That gives `K < 2L`, i.e. level `≲ L`, not `L/2` (m5).
* "Mostly inside the exact range" is unproved (m5).

**Assessment 5.2.** It is labelled correctly. I checked the following pieces.
* The Nicolas–Robin form `τ(M) ≤ M^{1.5379 log 2/log log M}` is the standard one (I could not access the paper; this is
  from memory).
* The arithmetic is right, assuming `M ≈ n^{1.8}`: `1.066·1.8 ≈ 1.92`, `log log M > 19.2` ⇒ `K ≈ 4·10⁷`. That assumption
  should be stated.
* "the tail series converges only once" is loose wording: convergence never depends on a finite set of terms. What is
  meant is that the terms are not summable to below ρ₁ before that K.

More substantively, the "precise obstruction" ignores the extension of Lenstra's theorem by Coppersmith–Howgrave-Graham–Nagaraj
(Math. Comp. 2008, from memory, not accessed): divisors of M in a class mod `s ≥ M^{1/4+ε}` number `O_ε(1)`. In the `ad` regime
(`M ≍ n`, modulus `4ad`) this covers all pairs with `ad ≥ n^{1/4+ε}`. Those are almost all of the `≍ n^{2/5} log n` pairs.
The remaining `n^{1/4+o(1)}` pairs are negligible against `n^{2/5}`. The `ac` regime is similar: the failing pairs number
`≲ n^{0.35}`. The `cd` regime is worse, because there `M ≈ c²dn` and the modulus is `4cd`; it would need a rebalanced cover.
So the honest bottleneck is different from the one stated:
1. the `e`-regime, an average of `τ_3((n+e)/4)` over a short interval `e ≤ n^{2/5}` (Shiu type), together with the `cd` regime;
2. the explicit constants (of CHN and of the short-interval divisor sums).
These would at best give `D_P ≪ n^{2/5}(log n)^{O(1)}` with explicit but large constants. That needs `θ > 2/5`, and from
the table a tiny constant at θ ≈ 0.45, or exact data up to large K. So the *conclusion* (no unconditional sterile point
within reach) stands, but the stated obstruction should be revised (m6).

Verdict (4): Lemma 5.1 SOUND (hidden hypothesis `17 ∤ ab`, harmless). §5 prose: SOUND-AFTER-REPAIRS (labels and
imprecisions). Assessment 5.2: GAP in the obstruction analysis (CHN), conclusion unaffected.

## Claim (5): Conjecture 4.2 label

The heading reads "Conjecture 4.2 (explicit, EVIDENCE)". The statement is a CONJECTURE, and the data are EVIDENCE for it.
The heading should read "Conjecture 4.2 (CONJECTURE; EVIDENCE: …)" (m7). The numbers are right:
* `D_P/2K³` = 1.00, 0.59, 0.48, 0.38, 0.41, 0.31, 0.33. The bound is attained with equality at K = 1.
* `D_Q/3k³` = 0.67, 0.90, 0.65, 0.69.
* `2k³` fails for Q at k = 3 and k = 7.
The Q part rests on four data points, one of which is at 90%. A pointwise conjecture with a tight constant is fragile under
the random model, which predicts fluctuations. The theorem needs much less, e.g. `D_P, D_Q ≤ K⁵`: tail 0.035 ≪ ρ₁.
Suggest stating the weaker, more robust form as the main conjecture, keeping 2K³/3k³ as an observation.
Verdict: SOUND-AFTER-REPAIRS (label).

## Claim (1) continued: D_P(11) and Claim (2): exact unions

**D_P(11) = 836: VERIFIED as a set.** `review_m17b_k11.c` (parts A0/A1/B; ≈ 15 CPU-min) gives 836 points, set-equal to `m17b_penum.py 11`.

**Unions (independent code `scripts/review_m17b_union.py`).** P-data come from my own engines (K ≤ 11). Q- and U-data come from the R83
engine `review_m17_enum.c` (S and U modes), which is independent of the O93 author. The union is computed by maximal-box
reduction with exact fractions, in both cells.
* Levels ≤ 5: uncovered `56561/83521`. Equal.
* + Q/U level 7: `16346035/24137569`. Equal.
* + P level 6 (K = 11): **ρ₁ = 16344335/24137569. Equal**, in both C_5 and C_7. Level 6 has 161 in-cell boxes, of which 100 are new. Equal.
* U and U⁻¹ never contribute a new box. Q and Q⁻¹ give identical box sets. √Q never occurs.
* Table §3, level-7 row: "272 (P 178, Q 94) | 6.6·10⁻⁶" is inconsistent. 272 boxes of level 7 have measure
  `272·17⁻⁶ = 1.127·10⁻⁵`. The Q part alone is `94·17⁻⁶ = 3.89·10⁻⁶` (my run), and the P part is `178·17⁻⁶ = 7.37·10⁻⁶`
  (= ρ₁ − ρ₂). So 6.6·10⁻⁶ matches neither (m3).
Verdict (2): ρ₁ SOUND (reproduced exactly). ρ₂: see below.

**D_P(13) = 1463 and ρ₂: VERIFIED.**
* `scripts/review_m17b_k13.c` is the K = 11 engine with `A0 = 20000`, `X = 10⁸`, and compressed sieve storage. It reproduces
  K = 9 and K = 11 as sets. At K = 13 it gives **1463** points, which equals the author's count. (The author's K = 13 point
  set is not in the repo, so I compared counts only.) Run time ≈ 12 CPU-min.
* The union with my P-data through K = 13 gives **ρ₂ = 961421/1419857, equal**, in both cells. Level 7 has 485 in-cell
  boxes, of which 272 are new (P 178, Q 94). That is a measure of 1.127·10⁻⁵ (confirms m3).

## Defects

**M1 (MAJOR, numerical headline; trivial repair).** The headline constant is rounded up and is not admissible.
* Where: §4 Theorem 4.1 table (θ = 0.40, C = 1.41); the "In words" paragraph ("constant 1.41 … suffices", "the needed
  constant 1.41"); AGENT_REPORT_O93 items 3 and the summary.
* What is wrong: with θ = 2/5 and K0 = 13, the exact C_max is `(ρ₁ − T_Q)/(2S) = 1.409796…`. At C = 1.41,
  `T_P + T_Q = 0.677230 > ρ₁ = 0.677133`, so the hypothesis of Theorem 4.1 fails.
* Repair: state C ≤ 1.40 (or "C < 1.4097"), and round every "largest admissible C" *down* (see m2).
  `m17b_tail.py` should print floor-rounded values.

**m1 (MINOR, label).** Computation 2.2 calls `D_P(13) = 1463` "CERTIFIED by one engine". This review supplies the
second engine (count agreement, `review_m17b_k13.c`), so it may now read "CERTIFIED (O93 engine + R93 engine)".
Also store the K = 11 and K = 13 point sets in the repo (or their hashes), so that later checks can compare sets, not
only counts. (sha256 of the sorted R93 sets: see the Replay section.)

**m2 (MINOR).** The other table entries are rounded up as well: 87.9 (exact 87.888), 11.8 (11.768), 0.569 (0.5687),
0.128 (0.12750); in the K0 = 15 row 273 (272.96) and 2.49 (2.4845). The K0 = 15, θ = 0.42 entry "—" should read 0.894.
Repair: round down throughout.

**m3 (MINOR).** §3 table, level-7 row: "measure added 6.6·10⁻⁶" is wrong. The 272 new boxes (P 178, Q 94) have measure
`272·17⁻⁶ = 1.127·10⁻⁵`, consistent with ρ₀ − ρ₂. Repair: 1.13·10⁻⁵ (P 7.37·10⁻⁶, Q 3.89·10⁻⁶).

**m4 (MINOR).** Lemma 5.1 has two problems.
* It needs `17 ∤ ab`, since otherwise 17 is not invertible mod 4ab. Pairs with `17 | ab` only give boxes `≡ 1 (mod 17)`,
  outside the cells, so state this exclusion.
* "This is the same sum as `Σ_K 17^{(1−K)/2} NB_P(K)`, only reorganised" is false. The Lemma 5.1 bound is ≥ that sum.
  By M17 Lemma 5.1(ii) all boxes of a pair `(a,b)` (any K, any class `e`) are concentric at `−a/b`, so
  `T_P ≤ 2Σ_{(a,b)} 17^{(1−K_min(a,b))/2}`, with one term per pair. That is the correct first-occurrence form; pairs with
  `K_min ≤ 11` contribute 0.
* Repair: state the pair form, and replace "same sum" with "an upper bound for".

**m5 (MINOR, labels and statements in the §5 prose).**
* "Averaging over K gives no unconditional gain" and "Any unconditional statement placing K_e … is again … a bound on D_P(K)"
  are judgements; label them Assessment.
* "Pairs with `ord_{4ab}(17) = L` … live at levels `≲ L/2`" should be `≲ L`, since `K_first < K_min + L ≤ 2L`.
* "Mostly inside the exact range" is unsupported; drop it or give data.

**m6 (MINOR, Assessment 5.2 imprecise).**
* (a) The Nicolas–Robin step silently takes `M ≈ n^{1.8}`; state it. "the tail series converges only once …" should say
  the *terms* are not small before that K; convergence does not depend on finitely many terms.
* (b) The obstruction overlooks Coppersmith–Howgrave-Graham–Nagaraj (divisors in a class mod `s ≥ M^{1/4+ε}` are
  `O_ε(1)`). That covers most `ad` and `ac` pairs. The real bottleneck is the `e`-regime (short-interval `τ_3` sums), the
  `cd` regime, and the explicit constants, which would give at best `n^{2/5}(log n)^{O(1)}`.
* Repair: revise the "precise obstruction" accordingly. The conclusion (CONDITIONAL; no unconditional sterile point) is unchanged.

**m7 (MINOR, label).** "Conjecture 4.2 (explicit, EVIDENCE)" should read CONJECTURE, with the data as EVIDENCE.
* The Q half rests on four data points, one at 90% of the bound.
* The K = 1 case is attained with equality.
* Consider promoting a robust sufficient form (e.g. `D_P, D_Q ≤ K⁵` for K ≥ 13 / k ≥ 9; tail 0.035) to the main conjecture.

**m8 (cosmetic).** §2 says `X_cd ≈ n^{0.3}` keeps `4c²dn+1 < 10²⁵`. At K = 13 (`X_cd ≈ 6·10⁴`) the value reaches
`≈ 1.5·10²⁶`. This is harmless, since `factor` is GMP-based; fix the number or drop the remark.

## Replay

```
ulimit -v 8000000; mkdir -p /tmp/r93 && cd /tmp/r93; W=<worktree>
gcc -O2 -o brute $W/scripts/review_m17b_brute.c; gcc -O2 -o k13 $W/scripts/review_m17b_k13.c
gcc -O2 -o r83enum $W/scripts/review_m17_enum.c
for K in 1 3 5 7; do ./brute $K 1 0 | sort > b$K.txt; done
./brute 9 2 0 > x0 & ./brute 9 2 1 > x1; wait; sort x0 x1 > b9.txt                 # ~6 min/core
(./k13 A0 11 2000 10000000; ./k13 A1 11 2000 10000000; ./k13 B 11 2000 10000000) | sort -u > b11.txt   # 20 s
(./k13 A0 13 20000 100000000; ./k13 A1 13 20000 100000000; ./k13 B 13 20000 100000000) | sort -u > b13.txt  # ~12 min, 3.3 GB
for k in 1 2 3 4 5 7; do ./r83enum S $k > S$k.txt; ./r83enum U $k > U$k.txt; done     # U 7 ~ minutes
uv run python $W/scripts/review_m17b_union.py . 1,3,5,7,9,11 7      # rho_1
uv run python $W/scripts/review_m17b_union.py . 1,3,5,7,9,11,13 7   # rho_2
uv run --with mpmath python $W/scripts/review_m17b_tail.py           # Thm 4.1 table
```
sha256 prefixes of the sorted R93 sets (lines `a b c d`): K = 11 `19cbd5acdd8af29a`, K = 13 `2ec22df715d4108e`.
(`review_m17b_k11.c` is the first version with A0 = 50, X = 10⁷, used for the K = 11 set check.)
