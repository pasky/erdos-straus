# BRAINSTORM / ident_numerators — what is special about 4? (m/n = 1/x+1/y+1/z, m = 4..13; O145 (c))

Labels as in DISCOVERIES.md. ES is not solved; neither is any m ≥ 4 analogue (Sierpiński m = 5,
Schinzel's conjecture for general m).

## 1. Idea

For m ≤ 3 the problem is trivial (m copies of 1/n, or 2/n = 1/n + 1/2n + 1/2n). For m ≥ 4, is there an m
whose analogue is *provable* by finitely many identities, and which feature of 4 drives the obstruction?
Candidates: (i) the class of one (m/1 is not a sum of three unit fractions iff m ≥ 4);
(ii) 4 | m (Jacobi sign of the Type II classes); (iii) the Type I/II dichotomy (same for every m).

## 2. Literature anchor

* Schinzel, Funct. Approx. 28 (2000): no polynomial identity for `m/(an+b)` when b is a quadratic residue
  mod a — **valid for m ≡ 0 (mod 4) only**; for m = 5 it fails (`n ≡ 7 (mod 9)` has an identity).
  Source: Schuh, arXiv:2404.01307, p. 2 (read 2026-10-12; Schinzel not accessed directly). Schuh's
  Cor. 2: for (n₁, m) = 1 and n₁ prime, identities mod n₁ need n₁ = m or n₁ ≡ 3 (4) (as stated there).
* Pomerance–Weingartner arXiv:2511.16817: Schinzel exceptions exist with `n_m ≥ exp(m^{1/3+o(1)})`
  (via LITERATURE_2026.md, already audited by the campaign).
* Campaign: POINTWISE_MN Lemma 1.1(d) (Type II class −mD is a Jacobi non-residue mod M iff-direction
  for m ≡ 0 (4); PROVED there), TRANSFER Lemma 5.1(ii) (class of one is Type-II-hard for every m),
  EXCEPTIONAL_MN (density results for all m).

## 3. Barrier screen / structural answer

**Lemma 3.1 (class of one; PROVED, elementary).** For every m ≥ 4 the profinite point 1 lies in no
ET-shaped family class. Type II (`m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)`, `sM = nv + u`, `M = muvw − 1`):
n ≡ 1 forces `M | u + v`, but `M ≥ 4uv − 1 > u + v`. Type I (`ne = mabd − 1`, `a + b = ce`; fix (a, d, e),
class mod `e·mad`): n ≡ 1 forces `mad | e + 1` and `e | a + k` with `e = madk − 1`, impossible as
`4adk − 1 > a + k`. For m = 3 both inequalities fail exactly at `u = v = w = 1`, `3/1 = 1+1+1`.
Hence (with Dirichlet, as in notes Cor 17.3.1) **no finite set of ET-shaped identities proves the
m-analogue for any m ≥ 4** — B1 holds uniformly in m. Known in substance (TRANSFER 5.1(ii), Schuh).

**What 4 | m adds (the odd-square obstruction).** For 4 | m the Jacobi computation of POINTWISE_MN
Lemma 1.1(d) puts every Type II class in the non-residues, so every square-mimicking point is
Type-II-sterile (PROVED there); Type I behaves the same way in the data below (EVIDENCE; the Type I
proof would follow ET Prop 1.6 with 4 replaced by m — not written out here). For 4 ∤ m odd squares
carry Type I/II solutions (5/9 = 1/2 + 1/36 + 1/36), Schinzel's theorem fails, and the residual
obstruction is concentrated on the class of one. So **4 is special twice: it is the least m with a
sterile class of one, and the least m where the whole square coset is sterile**; the Type I/II split
itself is m-independent and plays no role. No m ≥ 4 escapes (i), so no m is provable by identities.

B2/B3/B6 are unchanged for every m (the per-p lottery and scale constraint are m-uniform; EXCEPTIONAL_MN
"mechanism: nothing is m-specific"). B5 for m ≢ 0 (4): the odd-square test is *passed*, but the
class-of-one test (n ≡ 1 mod highly divisible L) replaces it.

## 4. Experiments (EVIDENCE; `scripts/bs_ident_mn.c`, `scripts/bs_ident_mn_classes.py`)

* **Type I/II at odd squares** (`bs_ident_mn 2 m 45`, n = s², s ≤ 45 odd, (s,m) = 1, ET coprimality):
  m = 4, 8, 12: **0** Type I/II solutions at every square (22, 22, 14 squares). m = 5, 6, 7, 9, 10, 11, 13:
  0–3 squares without, totals 79–269 Type I and 28–107 Type II solutions → `data/bs_ident/mn_squares_45.txt`.
* **m-exceptional n ≤ 3000** (`bs_ident_mn 0 m 3000`): m = 4, 5, 6: only n = 1; m = 7: {1,2};
  m = 8: {1,2,3,11,17,131,241}; m = 9: {1,2,5,11,19}; m = 10: {…,43,61,67,181}; m = 11: {1,2,3,4,37};
  **m = 12: 20 exceptions up to 2593, every one > 25 is ≡ 1 (mod 24)**; m = 13: up to 281.
  The multiples of 4 (8, 12) have the longest tails → `data/bs_ident/mn_exceptions_3000.txt`.
* **Where the hard primes sit** (`bs_ident_mn 1 m 30000`, primes 10³ < p ≤ 3·10⁴; mean f/log²p by class
  of p mod 840: class of one / other squares / non-squares): m = 4: 0.43 / 0.49 / 1.53;
  m = 5: 0.59 / **1.01** / 1.39; m = 6: 0.37 / 0.49 / 0.96; m = 7: 0.32 / **0.56** / 0.94
  (17, 66, 2994 primes) → `data/bs_ident/mn_classes_30000.txt`. For m = 4 the whole square coset
  is equally hard; for m = 5, 7 the other square classes sit roughly halfway between the class of one
  and the non-squares. (Small samples; the 'one' class has 17 primes.)

## 5. Viability Assessment

**COLLAPSES to B1 at the class of one (Lemma 3.1), uniformly in m ≥ 4.** No numerator is provable by
finitely many identities. The sharp answer to "why 4": two separate features — m ≥ 4 (sterile class
of one) and 4 | m (the square coset is sterile: Schinzel's theorem, ET Prop 1.6), the latter verified
here for m = 8, 12 (EVIDENCE) and PROVED for Type II (POINTWISE_MN). By-products: Lemma 3.1 (PROVED,
folklore-level); the m = 12 exception tail ≡ 1 (24) and the class-of-one concentration of hardness
for m = 5, 7 (EVIDENCE). Not pursued: whether, for 4 ∤ m, the per-p lottery (B2) is genuinely
easier — the scale constraint and EXCEPTIONAL_MN's m-uniform mechanism suggest not (Assessment).
