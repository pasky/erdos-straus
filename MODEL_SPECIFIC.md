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
156 (m = 12). [m = 4 to 10⁸ for n ≡ 1 mod 4: DEDEKIND/HJ_DEEP SQ₅ evidence.]

*Reading (the sharp point).* After the T1 character is accounted for, ES's five-slice lottery has **no residual
congruence obstruction at all**: its success set is literally {χ = −1}. For 8/n (same surface, same T1) the success set
is a 7/12 sub-union of χ = −1 cells — a second, non-character condition on (t, u, v) mod 8, which is exactly what fails
at 131 and 241 (and at 113, 257, 353, … where 8/p survives through other shapes). So the B7 sibling 8/n differs from ES
already on the most structured piece of the solution set, and in a precise way: **for ES "T1 is the only local
obstruction" is true on the length-3 ball as an identity, for 8/n it is false on the same ball.** A proof of
λ(p) ≤ 3 (a statement about quadratic non-residues in the Farey metric, with no reference to the numerator) would prove
ES and would *not* prove 8/n — it is model-specific input of the kind B7 demands.
