# MODEL_SPECIFIC — what makes 4/n special among m/n? (task O197, spark relay R, after B7)

Status: in progress (O197). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on TES_FINITE.md §5 (O194: Schinzel 8/n has the same ℚ-surface, real anchor and order-2 T1 as ES, no BM
obstruction at 131, 241, yet no solution there — barrier B7), BRAINSTORM/ident_numerators.md (O145),
POINTWISE_MN.md (Jacobi lemma for 4 | m), DEDEKIND_ES.md (five HJ slices), FIXED_MODULUS_SHOTS.md (certificate cube).
Scripts `scripts/ms_*`, data `data/ms/`.

Notation. f_m(n) = #{(x, y, z) ∈ ℕ³ : x ≤ y ≤ z, m/n = 1/x + 1/y + 1/z}. "m fails at n" ⟺ f_m(n) = 0.

## 0. Iteration log
(R1) Literature first: the large-m picture is Pomerance–Weingartner (PW, arXiv:2511.16817, in sources/): a first-moment
count gives mean ≍ (log p)³/m; failures exist for all large m. Their Table 1 lists all failures for m ≤ 15 up to
10¹²–10¹⁸. So "why do 4, 5 have no failures while 8 fails at 241" has a first, purely quantitative answer (mean ∝ 1/m)
that must be separated from any structural one. Plan: measure the structure that survives normalisation by the mean.

## 1. Censuses (CERTIFIED by complete search; cross-checked against PW Table 1)

Engine `scripts/ms_census.c` (written from scratch): x ≤ y ≤ z, n/m < x ≤ 3n/m, A = mx − n, B = nx reduced by
g = gcd(A, B), (A'y − B')(A'z − B') = B'², all divisors d ≤ B' of B'² with d ≡ −B' (mod A'); every solution is
re-verified in 128-bit integers ((mxy − ny − nx)·z = nxy). Complete for every n (Prop 1.1 of TES_FINITE).
Checks: 4/131 = 32, 4/241 = 8, 8/127 = 23, 8/239 = 58 solutions (TES_FINITE's numbers); m = 12, all n ≤ 3000: the
19 failures of PW Table 1 below 3000.

**Failing primes p ≤ 10⁸ (m ≤ 20, m = 24; `data/ms/prime_fail_1e8.txt`; m = 21–23 to 10⁷ in `prime_fail_1e7.txt`).**
| m | # failing primes | largest failing prime ≤ 10⁸ | | m | # | largest |
|---|---|---|---|---|---|---|
| 4 | 0 | — | | 15 | 23 | 20521 |
| 5 | 0 | — | | 16 | 37 | 83449 |
| 6 | 0 | — | | 17 | 16 | 2081 |
| 7 | 0 | — | | 18 | 47 | 35281 |
| 8 | 5 | 241 | | 19 | 15 | 353 |
| 9 | 3 | 19 | | 20 | 62 | **2763601** |
| 10 | 7 | 181 | | 21 | 26 | 14051 (≤10⁷) |
| 11 | 2 | 37 | | 22 | 53 | 14543 (≤10⁷) |
| 12 | 20 | 12241 | | 23 | 45 | 31771 (≤10⁷) |
| 13 | 9 | 281 | | 24 | 154 | 620929 |
| 14 | 8 | 353 | | | | |
Agreement with PW Table 1 (prime entries, m ≤ 15) is exact. New here (to my knowledge; PW stop at 15): m = 16–24 lists;
m = 20 fails at the prime 2763601 ≡ 1 (mod 840), after a gap from 90001.
**T1 control (odd squares k² ≤ 10⁸, gcd(k, 2m) = 1):** all solvable for m = 4–11, 13, 15; exceptions 25 (m = 12),
841 = 29² (m = 14), 9, 121 (m = 16) — all in PW's table or small. (Squares are solvable by "other-shape" solutions.)

**Observation 1.1 (EVIDENCE).** The multiples of 4 have far longer failure tails than their neighbours:
last failure 241 (m = 8) vs 2 / 19 (m = 7, 9); 12241 (12) vs 37 / 281 (11, 13); 83449 (16) vs 20521 / 2081;
2763601 (20) vs 353 / 14051; 620929 (24) vs 31771 (23). Among m ≡ 0 (mod 4), m = 4 is the only one with no failure.

## 2. 8/n is the all-even half of 4/n (PROVED, elementary) — the "parity sub-lottery"

**Lemma 2.1.** Let n be odd. (a) Every solution of 4/n = 1/x + 1/y + 1/z has either all of x, y, z even or exactly one
of them odd. (b) (x, y, z) ↦ (2x, 2y, 2z) is a bijection from the solutions of 8/n onto the all-even solutions of 4/n;
hence f_4(n) = f_8(n) + f_4^{odd}(n), f_4^{odd} := number of solutions with exactly one odd denominator.
(c) For a prime p ∤ 6 in ET/PW coordinates (Type I: x, y, z = abdp, acd, bcd, 4abd = pe + 1, a + b = ce; Type II:
abd, acdp, bcdp, 4abd = p + e, a + b = ce; a, b, c pairwise coprime) a solution is all-even ⟺ d is even.
*Proof.* (a) v₂(4/n) = 2. Three odd denominators: the sum has odd numerator over odd denominator, v₂ = 0. Two odd
(x, y), z even: v₂(1/x + 1/y) ≥ 1 > −v₂(z) = v₂(1/z), so v₂(sum) = −v₂(z) < 0. (b) 8/n = Σ 1/u_i ⟺ 4/n = Σ 1/(2u_i).
(c) If d is even all three are even. If d is odd, all-even needs two of a, b, c even (each denominator is a product of
two of a, b, c times d, p odd), impossible for pairwise coprime a, b, c. (Pairwise coprimality: PW Prop 2.1/2.3
proof, a = gcd(x′, y′) etc. with gcd(x′, y′, z′) = 1.) ∎
EVIDENCE (`ms_census` parity filter): the all-even filter of 4/p reproduces the 8/p failure list {3, 11, 17, 131, 241}
exactly (p ≤ 10⁵), and per prime f_4^{even}(p) = f_8(p) for all 2261 primes ≤ 2·10⁴ (0 mismatches); 2 or 3 odd
denominators: 0 solutions at every prime. The all-even share of ES solutions is 0.444 (p ≤ 2·10⁴), 0.448 on
(10⁴, 2·10⁴]. **The one-odd sub-lottery alone never fails: f_4^{odd}(p) ≥ 1 for every prime 3 ≤ p ≤ 10⁸ (5 761 454
primes), and every odd square ≤ 10⁸ has a one-odd solution and an all-even one.** (For p ≡ 3 mod 4 this is trivial:
e = 1, x = (p+1)/4; the content is p ≡ 1 mod 4.)
*Reading.* ES(p) = [8/p] ∨ [one-odd 4/p]. At 131 and 241 ES lives entirely on the one-odd half (32 and 8
solutions). The sibling 8/n is not a "different equation with the same surface", it is literally a sub-lottery of ES
at the same n (d even), of about 45% of ES's mean, and B7 says this sub-lottery has non-T1 failures. The parity split
is m-specific (for m = 8 the analogous decomposition is into 16/n and the rest).

## 3. The five length-3 slices: m = 4 is the unique numerator whose slices are cut out by a character

Setting (DEDEKIND_ES §1, §4). A *word* is (t, u, v) ∈ ℤ³_{≥1} with tuv − u − v = n (n odd ≥ 3), A = tu − 1 ≥ 1,
A* = tv − 1, AA* = tn + 1, gcd(A, n) = 1; for t, u, v ≥ 2 these are the length-3 Hirzebruch–Jung fractions
n/A = [[v, t, u]], the others are the boundary words. Put **χ(w) := (−A/n)** (Jacobi). The five **m-slices**:
`S_m: m | tu − 1, or m | tv − 1, or m | t, or m | u, or m | v.`
**Lemma 3.0 (PROVED; generalises DEDEKIND Cor 1.2/Thm 4.5 from 4 to m, algebra checked in `ms_slices.c`).** Every
word in S_m gives a solution of m/n: (I) m | A, d = A/m: m/n = 1/(A*dn) + 1/(vd) + 1/(A*vd) [since
c + n(b+1) = mbcd reads v(1 + nt) = A·A*·v]; (I′) u ↔ v; (T) t = mc: m/n = 1/(uvc) + 1/(ucn) + 1/(vcn) [n + u + v =
mcuv]; (U) u = mw, f = tv − 1: m/n = 1/(wf) + 1/(tnw) + 1/(tnwf) [n + v = mw·f]; (V) u ↔ v. ∎ (Every hit found in
the runs below was verified exactly in 128-bit arithmetic; no degenerate denominators occurred.)

**Theorem 3.1 (PROVED: finite cell computation, relative to DEDEKIND Cor 4.1 = Rademacher's congruence).**
(a) **m = 4: a word lies in S_4 ⟺ χ(w) = −1**, for every odd n (for n ≡ 1 mod 4 this is DEDEKIND Thm 4.5; for
n ≡ 3 mod 4 it is new in this form, with χ = (−A/n) = −(A/n)).
(b) 4 | m, m ≥ 8: S_m ⊊ {χ = −1}. The inclusion is (a) since m | X ⇒ 4 | X; it is proper for every such m: the word
(t, u, v) = (4, 1, 2) (n = 5, A = 3, χ = −1) is in S_4 but in no S_m (3, 7, 4, 1, 2 are not divisible by m), and
by (a)+(Cor 4.1) its whole cell mod 8 is χ = −1. Cell fractions mod lcm(8, m): S_m fills 140/240 = 7/12 of the χ = −1
cells for m = 8, 2304/6480 = 16/45 for m = 12, 600/1920 = 5/16 for m = 16.
(c) 4 ∤ m, m ≥ 5: S_m contains χ = +1 words, namely t = m and (u, v) = (2, 3) if m ≡ 1, 5 (mod 8), (1, 2) if
m ≡ 2, 6, (1, 1) if m ≡ 3, 7 (gcd(A, n) = 1 holds identically: for u = 1, n = (m − 1)v − 1 ≡ −1 mod A; for (2, 3),
n = 3A − 2 with A odd). For 5 ≤ m ≤ 15 the slices fill the same fraction of both χ-halves (0.712, 0.489, 0.563,
0.421, 0.333, 0.391, 0.339, 0.251, 0.251 for m = 5, 6, 7, 9, 10, 11, 13, 14, 15): S_m is χ-blind.
Hence **m = 4 is the only numerator m ≥ 4 for which "the word certifies m/n" is a function of χ alone.**
*Proof.* Cor 4.1 makes χ a function of (t, u, v) mod 8 (with n mod 8 determined by the cell); slice membership is a
function of (t, u, v) mod m; enumerate all cells mod lcm(8, m) (`scripts/ms_cells.py`, output `data/ms/cells.txt`).
(a): 240/240 χ = −1 cells in S_4, 0/80 χ = +1 cells. (b), (c) as stated. Cor 4.1 itself was re-checked against
sympy's Jacobi symbol on all 129 538 words with t, u, v < 60 (interior and boundary), 0 mismatches. ∎

**Corollary 3.2 (the length-3 lottery: character for 4, sub-character for 8).** For odd n:
`[S_4(n) ≠ ∅] ⟺ [some length-3 word of n has (−A/n) = −1]` ("a quadratic non-residue −A in the Farey ball of
radius 3"; = λ(p) ≤ 3 of DEDEKIND Cor 4.6 for p ≡ 1 mod 8). For m = 8 the same character condition is necessary
but **not sufficient**: at n = 131 and 241 there are 22 resp. 7 words with χ = −1 (they are the ES five-slice
certificates found by `ms_slices 4 131 one`), but no word in S_8 — and indeed no solution of 8/n at all.
EVIDENCE (`data/ms/slices_1e5.txt`, primes ≤ 10⁵): S_m(p) = ∅ for **0** primes (m = 4), **0** (m = 5), 25 (m = 6,
last 35911), 10 (m = 7, last 12601), 23 (m = 8, last 83449; true 8/p failures among them: 3, 11, 17, 131, 241),
156 (m = 12). Extended to 10⁷ (`data/ms/slices{4,8}_1e7.txt`): S_4(p) ≠ ∅ for all 664 578 primes ≤ 10⁷; S_8(p) = ∅ at
27 primes, the last four 211681, 215297, 252001, 259201, none in (259201, 10⁷]. So S_8 is itself a lottery that
empirically wins eventually; the 4-specificity of Thm 3.1 is structural (what the obstruction *is*), not a claim that
S_8 fails infinitely often. [m = 4 to 10⁸ for n ≡ 1 mod 4: DEDEKIND/HJ_DEEP SQ₅ evidence.]

*Reading (the sharp point).* After the T1 character is accounted for, ES's five-slice lottery has **no residual
congruence obstruction at all**: its success set is literally {χ = −1}. For 8/n (same surface, same T1) the success set
is a 7/12 sub-union of χ = −1 cells — a second, non-character condition on (t, u, v) mod 8, which is exactly what fails
at 131 and 241 (and at 113, 257, 353, … where 8/p survives through other shapes). So the B7 sibling 8/n differs from ES
already on the most structured piece of the solution set, and in a precise way: **for ES "T1 is the only local
obstruction" is true on the length-3 ball as an identity, for 8/n it is false on the same ball.** A proof of
λ(p) ≤ 3 (a statement about quadratic non-residues in the Farey metric, with no reference to the numerator) would prove
ES and would *not* prove 8/n — it is model-specific input of the kind B7 demands.

## 4. Identities (Mordell classes) and the three cube shots for m/n

**4.1 Covering by ET-shaped identities (CERTIFIED computation, `scripts/ms_cover.py`, `data/ms/cover.txt`).** Atoms:
Type II (u, v, w), M = m·uvw − 1, class n ≡ −u·v⁻¹ (mod M); Type I (a, d, f), K = m·ad, f | ma²d + 1, class
n ≡ −f (mod K) (PW Cor 2.2/2.4; every prime in the class has a solution). U_m(L) := unit classes mod L hit by no atom
with modulus dividing L.
| m | #U_m(840) (squares) | #U_m(9240) (squares) | #U_m(120120) (squares) |
|---|---|---|---|
| 4 | 6 (6) — exactly Mordell's {1, 121, 169, 289, 361, 529} | 34 (30) | 204 (180) |
| 5 | 2 (1) | 10 (5) | 10 (5) |
| 6 | 12 (1) | 84 (3) | 372 (12) |
| 7 | 4 (1) | 10 (1) | 50 (5) |
| 8 | 35 (6) | 243 (30) | 1707 (180) |
| 9 | 114 (6) | 1006 (30) | 8390 (90) |
| 12 | 50 (6) | 381 (30) | 3392 (180) |
(Units: 192, 1920, 23040. L is tailored to the moduli 4k − 1 and 8; for odd m it is not the natural level, so only the
4-vs-8 comparison is fair.) For m = 4 the uncovered set is the square coset plus a thin remainder (24 of 204 at
120120); **for m = 8 the square coset is still uncovered (T1) but 1527 of the 1707 uncovered classes are non-squares**.
131 (≡ 131 mod 840: non-residue mod 3 and 7) and 241 lie in uncovered *non-square* classes for m = 8 at every level
tested, while for m = 4 both classes are covered at level 840. So: yes, the large 8/n failures sit in classes no
small identity reaches — but the relevant fact is that for 8/n those classes are not T1 classes.

**4.2 The three shots through the cube point (1, 1, 1) (`scripts/ms_shots.py`, `data/ms/shots_1e6.txt`).** With
h = m·cdj − 1 the cube of FIXED_MODULUS_SHOTS §1 generalises verbatim (h | pj + c ⟺ h | p + mc²d ⟺ h | mdj²p + 1); the
lines through (1, 1, 1) are the shots p + 1, p + m, mp + 1, firing iff they have a divisor h ≡ −1 (mod m), h > 1.
Primes ≤ 10⁶ at which all three fail: **942 (m = 4**, reproducing (J)25), **102 (m = 5)**, 4308 (m = 8; including 131
and 241), 11386 (m = 12). So the three shots are not a candidate never-failing condition even for ES; they are a
measure of "first-ticket" strength, and here m = 5 beats m = 4 by a factor 9 (no T1 for m = 5).

## 5. The count law and the "luck" of m = 4 (EVIDENCE + Assessment)

**5.1 Mean.** (`ms_stats.py`, `data/ms/stats.txt`; complete counts, all primes ≤ 2·10⁴, `data/ms/counts_m*.txt`.)
m·mean f_m / (4·mean f_4) on primes in [10⁴, 2·10⁴): m = 5: 1.16, 6: 0.95, 7: 1.09, 8: 0.90, 9: 0.93, 10: 0.88,
11: 1.02, 12: 0.80, 13: 0.95, 14: 0.86, 15: 0.92, 16: 0.74, 17: 0.90, 18: 0.70, 19: 0.92, 20: 0.77, 22: 0.73, 24: 0.71.
So **mean f_m ≈ c_m (log p)³/m with c_m within ±30% of c_4** (PW's first-moment heuristic; ET for m = 4); c_m is
largest for prime m (5, 7, 11) and smallest for m with many divisors (12, 16, 18, 20, 22, 24). The per-window ratio is
stable from p ≈ 300 on. (mean f_4/log³p drifts 0.227 → 0.158 between [100, 300) and [10⁴, 2·10⁴): lower-order terms;
the smooth fit used below is a log³p + b log²p, for m = 4: 0.0717 log³p + 0.818 log²p.)

**5.2 Where the low counts sit** (`ms_classes.py`, `data/ms/classes.txt`; normalised count r = f/fit, p ∈ [10³, 2·10⁴)).
Mean r on the class of one mod 840 / other square classes / non-squares: m = 4: 0.27 / 0.33 / 1.02; m = 8: 0.23 /
0.26 / 1.02; m = 12: 0.18 / 0.22 / 1.02; m = 5: 0.41 / 0.75 / 1.01; m = 7: 0.32 / 0.62 / 1.01. Minimum r: 0.11 (m = 4,
p = 2521, f = 9), 0.19 (m = 5), 0.11 (m = 7), **0.02 (m = 8**, p = 3361, f = 1), 0 (m = 12). By p mod 8 (m = 8): 0.47,
0.64, 0.95, 1.94 for p ≡ 1, 3, 5, 7 — the order of the least admissible slice e₀ = 8 − (p mod 8) (both Type I and
Type II e-slices need e ≡ −p mod 8). Correlations of r across numerators (`ms_corr.py`, `data/ms/corr.txt`) follow the
divisor lattice: (4, 8) 0.88, (8, 16) 0.89, (4, 12) 0.83, (6, 12) 0.90, (5, 20) 0.67, but (4, 5) 0.41, (4, 7) 0.32 —
hardness is inherited along m | m′ (4 | m: the square coset is T1-suppressed, POINTWISE_MN Lemma 1.1(d)).

**5.3 A pooled failure-rate model and the "luck" of 4** (`ms_tail.py`, `data/ms/tail_1e7.txt`; Assessment).
Bin all primes 100 ≤ p ≤ 10⁷ of every m ∈ {8, 12, 16, 20, 24} (pool 4 | m) resp. the 15 other m ≤ 23 by the fitted
mean μ_m(p); the empirical failure rate F(μ) falls from 0.3–0.5 (μ < 4) to 2.5·10⁻² (μ ∈ [12, 15)), 2.5·10⁻³
(μ ∈ [20, 25)), 2.6·10⁻⁴ (μ ∈ [30, 40)), and ≤ 10⁻⁵ beyond μ = 40 (4 | m; the 4 ∤ m pool is 2–5 times lower
throughout). Leave-one-out validation predicts each sibling's number of failures (p ≥ 100) within a factor ≈ 1.3
in the 4 | m pool (m = 8: 1.5 predicted / 2 observed; 12: 9.0/12; 16: 33.9/27; 20: 55.5/50; 24: 123/140) and within a
factor ≈ 3–4 in the 4 ∤ m pool (e.g. 15: 4.5/15, 19: 19.1/5).
Applied to m = 4 (μ₄(p) from 2.4 at p = 5 to 24 at p = 97, ≈ 510 at 10⁷): **expected number of failing primes
5 ≤ p ≤ 10⁷: 0.95 (4 | m curve) or 0.54 (4 ∤ m curve), of which ≤ 0.02 above p = 100**. Same for m = 5: 1.35 / 0.76;
m = 6: 2.5 / 1.35; m = 7: 3.0 / 1.6 (all observed: 0 failing primes).
**Assessment.** (i) Above p ≈ 100 ES's mean count is already ≥ 24 and its failure-free record is the expected
outcome (expected ≤ 0.02 failures, uniformly whichever pool is used). (ii) The whole "luck" of 4 is at p < 100, where
the model expects ≈ 0.5–1 failure, i.e. P(no failure) ≈ 0.4–0.6 — not remarkable — and m = 5, 6, 7 are equally (or
more) lucky there, so this small-p luck is not 4-specific (combined m = 4–7: 3.4–7.8 expected, 0 observed: the
pooled curve, built from large-m data at p ≥ 100, overestimates failures at tiny p for small m). (iii) 8/n's failures
at 131 and 241 are the expected outcome of its mean (≈ 13 at p ≈ 200) and its T1-suppressed square coset; m = 8 is the
4 | m pool's best-predicted member. **So the count model explains why ES and 8/n differ empirically without any
4-specific structure: B7's sibling fails because its lottery is ≈ 2.2× smaller, and ES passes because its lottery is
large from p ≈ 100 on.** The structural 4-specificity of §3 is a different matter: it concerns which certificates
exist, not how many.
**Last-failure fits.** Inverting P(fail) ≈ exp(−K(log p)³/m) (PW's Poisson form) at the observed last failures gives
K_eff ≈ 0.27 (m = 8), 0.135 (12), 0.125 (16), 0.09 (20), 0.136 (24) — not constant, so the pure (log p)³/m form
does not predict last failures to better than a factor ≈ 2 in log L(m); the binned μ-model above is the usable form.
*Independent word-level check of Thm 3.1* (`scripts/ms_words_check.py 1500`, sympy Jacobi, every slice solution
verified in exact rationals; `data/ms/words_check.txt`): all words of all odd n ≤ 1500 — m = 4: 23450 χ = −1 words, all
in S_4; 10980 χ = +1 words, none in S_4. m = 8: 11839 of the 23450 χ = −1 words in S_8, no χ = +1 word. m = 12: 6448
of 23450. m = 5: 14625/23450 of χ = −1 words and 6602/10980 of χ = +1 words (χ-blind).

## 6. B7 screen: which ES sufficient conditions survive the passage to 8/n?

"Survives" = the m = 8 analogue never fails beyond the true 8/n failures; "fails" = it fails at further primes, or the
model-independent formulation holds at 131/241 although 8/n has no solution there.
| condition (ES form) | ES record | 8/n analogue | 8/n record | verdict |
|---|---|---|---|---|
| five slices S_4 ⟺ some length-3 word with (−A/p) = −1 (λ ≤ 3) | no failure, primes ≤ 10⁷ (here), SQ₅ to 10⁸ (campaign) | S_8 | fails at 27 primes ≤ 10⁷ (113, 257, 353, …, 259201 beyond the 5 true failures); χ-form holds at 131, 241 | **4-specific (Thm 3.1)** — candidate |
| one-odd sub-lottery (d odd) | no failure, primes ≤ 10⁸ | one-odd part of 8/n | fails at 3, 11, 17, **59**, 131, 241, **449** (≤ 10⁶) | 4-specific — candidate, but no structure known |
| Type I alone | no failure 3 ≤ p ≤ 10⁶ (campaign: 10⁸) | Type I of 8/n | fails exactly at {3, 11, 17, 131, 241} (≤ 10⁶) | survives — not a discriminator |
| Type II alone | no failure 3 ≤ p ≤ 10⁶ | Type II of 8/n | fails at 22 primes, last 35569 | fails |
| three cube shots (1, 1, 1) | fails at 942 primes ≤ 10⁶ | p+1, p+8, 8p+1 | fails at 4308 | not a candidate for either |
| identities mod 840 | uncovered = 6 square classes | same atoms, m = 8 | 35 uncovered, 29 non-square (131, 241 among them) | 4-specific, but finite-level (B1) |
(`data/ms/type_only_1e6.txt`, `slices_1e5.txt`, `shots_1e6.txt`, `cover.txt`.)

*Reading.* Two genuinely 4-specific never-failing conditions emerge. The first (five slices) comes with a reason
(Thm 3.1: the certificate set on the length-3 ball is exactly the χ = −1 half, so the T1 character is the only
congruence obstruction there); the second (one-odd half) is so far only a numerical fact. Type I alone is the most
robust piece for **both** numerators (for 8/n, Type I fails only where 8/n fails), so it cannot carry 4-specific
input by itself.

## 7. Construction notes: what Thm 3.1 asks a proof to do (Assessment)

(C1) *Same surface, different targets.* For every m the five m-slices live on the same affine cubic
X_n: tuv − u − v = n (positive integral points; t-fibres are the hyperbolas (tu − 1)(tv − 1) = tn + 1). Only the target
set of cells mod lcm(8, m) changes. For m = 4 the target is a full fibre of χ = (−A/n), which is a function of the
cell mod 8 (DEDEKIND Cor 4.1); for m = 8 it is a 7/12 part of that fibre. At n = 131 the image of X_131(ℤ_{>0}) in
the cells mod 8 meets {χ = −1} (22 words) but misses all 35 S_8-cells. Hence **"the positive points of X_p reach every
cell mod 8 allowed by χ" is false** (at 27 primes ≤ 10⁷ at least), and an ES proof through X_p cannot be an
equidistribution-mod-8 statement for its points without p-dependent error control (B3: the main term is only
≍ log² p points); it must use that the ES target is a whole χ-fibre. ES-five-slices(n) ⟺ χ is not identically +1
on X_n(ℤ_{>0}), and (for n ≡ 1 mod 4, words with gcd(A, n) = 1) CONJECTURE SQ₅ ⟺ **χ is constant on X_n(ℤ_{>0}) only for n a
square or n = 105.** This is a
rigidity statement of the T1 kind, with the T1 locus as its only (conjectural) exception set — exactly the shape
B7 leaves open.
(C2) *Iteration (barrier hypotheses).* B1/B5: χ-constancy at squares is T1 itself, so no congruence argument proves
SQ₅ (it is false at squares) — the statement must see n's factorisation, which X_n's points do (via tn + 1). B2: for
each fixed t, "X_n has a t-point with χ = −1" is "tn + 1 has a divisor A ≡ −1 (mod t) with cofactor ≡ −1 (mod t)
and (−t/A)·ε = −1", a divisor-in-a-character-half condition with modulus 4t: still a lottery per t, now with the
modulus moving with t (H-A). For t = 3 and p ≡ 1 (mod 8) it reduces (computed in passing) to "(3p + 1)/4 has a
prime factor ≡ 2 (mod 3)", a classical ET class, so small t give nothing new; the content is the union over t.
B6: the χ-sum over X_p is a pointwise object (no averaging over p). B7: passed by construction (Thm 3.1).
(C3) *A deterministic shape that would suffice.* A χ-flipping move on X_n — a map w ↦ w′ between positive points
(possibly of bounded HJ length > 3, where the five-slice theorem has length-r analogues via Cor 4.1) with
χ(w′) = −χ(w) for non-square n — would prove ES on the slices. Known moves preserve χ: u ↔ v (A ↔ A*, AA* ≡ 1),
and multiplication by 4; DEDEKIND §8 found only a scaling flip needing composite n. Not found here either.
