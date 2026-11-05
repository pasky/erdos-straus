# Z58_WILDCARD — the full Type II family as target: converse of T1, numerator ladder, falsifier table

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Lane WILDCARD of wave z58 (`z52bbriefs/z58_lanes.md`, common rules `z53_depth.md` with z53 → z58).
Scripts `scripts/z58_wildcard_*`, data `data/z58/wildcard/`. **Status: CHECKPOINT 1** (falsifier table + statement +
first census). Later sections to be filled.

## 0. Mandatory falsifier table (checkpoint 1; re-stated at the end)

Chosen lead: **(i)+(ii) — the full Elsholtz–Tao Type II family N_II(n) := #{(a,b,c,d) ∈ ℕ⁴ : 4abcd = a + b + nc} as the
target, with its converse-of-T1 statement** (§1). (★) is the c = 1 line (u, B, C) = (a, b, d). N_II(p) ≥ 1 ⟹ ES(p)
(4/p = 1/(abd) + 1/(acdp) + 1/(bcdp)); so (MS-II) below is *weaker* than (MS) and still sufficient.

| screen | behaviour of the idea (target CONV-II / MS-II) | status |
|---|---|---|
| **F1 odd squares** | N_II(m²) = 0 for every m (QNR-witness lemma, Z57_BFII Prop 2.2/Cor 2.3: every witness f has (n/f) = −1). The statement is *exactly* "T1 is the only obstruction" — non-squareness is the hypothesis, and the step using it is the one where a witness modulus f with (n/f) = −1 must exist (genus level: Theorem G's "ψ*χ_u is never principal because the conductor of χ_u contains the squarefree kernel of n"). | PROVED (squares fail); CERTIFIED controls |
| **F2 numerator 8 / C-even** | The C-even half of (★) is the c = 1 line of numerator 8; the full numerator-8 Type II family N_II^{(8)} (= the d-even half of N_II, Lemma 2.1 below) has, among odd non-squares ≤ 10⁹, exactly **22 prime zeros (last 35 569) and 107 composite zeros (last 1 239 315)**, none in (1.24·10⁶, 10⁹]. At the 12 R₈-zeros in [10¹⁰, 1.1·10¹⁰] N_II^{(8)} has witnesses f ≤ 1311. So the numerator-8 analogue of CONV-II is (empirically) *also* eventually true: the F2 trap of (MS) (sub-line false at 10¹⁰) **does not transfer** to the full family; an argument that works verbatim for numerator 8 is not refuted at any threshold ≥ 35 569 (primes) / 1 239 315 (all odd non-squares). What distinguishes C odd from C even is no longer needed — what *is* needed is the c ≥ 2 lines: the c = 1 sub-line of numerator 8 is false at 10¹⁰. | CERTIFIED (≤ 10⁹) |
| **F3 composites** | (★) has 285 composite non-square zeros ≤ 8·10⁶. N_II has **one** odd non-square zero ≤ 10¹⁰: **4545 = 3²·5·101** (CERTIFIED, extends Z57_BFII's 10⁷ and notes §61's 10⁶). Of the 285 (★)-composite zeros, 284 have N_II ≥ 1 (least witness ≤ 1319). Partial explanation (PROVED, Lemma 2.2): solutions *scale* n → nk when k | c or k | d, so composites inherit witnesses from divisors. Removing inheritance (ET's coprimality gcd(abd, n) = 1): 142 odd non-square zeros ≤ 10⁸, **every one divisible by 3 or 5**, all ≡ 1 (4), last 21 754 425. So primality is used, beyond non-squareness, **only through gcd(n, 15) = 1 (coprime form) or not at all (N_II form, sporadic 4545)**. | CERTIFIED |
| **F4 known zeros** | N_II ≥ 1 at all 14 (★)-zeros and all 38 𝔊*-zeros (least witness ≤ 239), at the 12 R₈-zeros (≤ 295); no prime ≤ 10¹⁰ has N_II = 0 (CERTIFIED, §3). The statement has **no known prime zero at all**, so it needs no threshold above them; but any proof via the (★) sub-line must fail there (they are zeros of the c = 1 line), i.e. the argument must genuinely use c ≥ 2. | CERTIFIED |

**Verdict on the screen (Assessment, checkpoint 1):** the *statement* CONV-II survives all four screens far better than
(MS): no prime zero, one composite sporadic, squares exactly obstructed, numerator-8 analogue also eventually true. This
is a statement-level HOT property, **not a mechanism**: no argument is supplied yet, and the pointwise wall (B2) for the
single residue sequence (n mod f)_f is unchanged in kind (Z57_BFII §5). Whether a *mechanism* exists that sees only
non-squareness is the question for §4.

## 1. Precise statements (labels)

* **CONV-II (CONJECTURE).** For every odd n ≥ 3 that is not a perfect square and n ≠ 4545, N_II(n) ≥ 1.
  CERTIFIED for n ≤ 10¹⁰ (§3; T1 gives ⊇ for squares, PROVED).
* **CONV-II-cop (CONJECTURE).** For every odd non-square n with gcd(n, 15) = 1 there is (a,b,c,d) with 4abcd = a+b+nc
  and gcd(abd, n) = 1 (a genuine ET Type II solution). CERTIFIED for n ≤ 10⁸.
* **(MS-II) (CONJECTURE; sufficient for ES with Mordell + Salez, PROVED relative to them as for (MS)).** Every prime
  p > 10¹⁷ with p mod 840 ∈ 𝔐 has N_II(p) ≥ 1. Weaker than (MS) (c = 1 ⊂ all c). CERTIFIED for p ≤ 10¹⁰ (all odd p).
* **CONV-II(K) (CONJECTURE, K ≡ 0 mod 4).** N_II^{(K)}(n) := #{K abcd = a+b+nc} vanishes at odd squares (PROVED, same
  QNR lemma) and at only finitely many odd non-squares. K = 8: zero set ≤ 10⁹ is squares ∪ 129 sporadics (22 prime).

## 2. Quick pass on the four leads (first falsifier each)

* (i) full Type II as target — adopted (falsifier table above). New compared with Z53/Z57: certified census to 10¹⁰,
  the numerator ladder (F2), coprime form (F3).
* (ii) converse of T1 — same object; CERTIFIED to 10¹⁰ (only 4545). Prior: notes §§60–61 (`C_SQ′`, complete to 10⁶,
  including even n: sporadics 288, 336, 4545), Z57_BFII §4.1 (odd n ≤ 10⁷).
* (iii) r-spectrum R(n) = {r : rn + 1 has a divisor ≡ −1 (mod r)}: the natural closure law (multiplicativity) is false in
  one line — 2 ∈ R(n) for every odd n (2n + 1 itself) while 4 ∉ R(409) (R(409) = 0). Other selection laws: no first
  falsifier with a better outcome found quickly. Not pursued.
* (iv) varying fields Q(√(−Cp)) / joint divisor constraints: no computation gives a quick falsifier outcome; the slice
  form of Type II (f | cn + a, f ≡ −1 mod 4ac) already *is* the joint constraint over the fields Q(√(−ac n)) …; folded
  into §4 as a mechanism question.

## 3. Computations (CERTIFIED unless stated)

`scripts/z58_wildcard_census.c` (target-set bitmaps for f ≤ FMAX, exact (a,b)-loop fallback; validated: with FMAX = 3,
6596 non-squares ≤ 2·10⁴ go to the exact fallback and the zero set is identical — {4545}; reproduces Z57_BFII's 10⁷ zero
set). `scripts/z58_wildcard_screens.py` (independent target-set recomputation, explicit (a,b,c,d) and exact Egyptian
identity check at every falsifier integer).

| run | range (odd n) | non-square zeros | max least witness (all / primes) |
|---|---|---|---|
| K = 4 | [1, 10⁸) | 4545 | 14111 / 2495 |
| K = 4 | [10⁸, 10⁹) | none | 151 406 099 (n = 302 812 197, exact fallback) / 3359 |
| K = 4 | [10⁹, 10¹⁰) | none (every non-square has f ≤ 20000) | 19711 / 3799 (p = 6 736 278 481) |
| K = 4 coprime | [1, 10⁸) | 142, all divisible by 3 or 5, last 21 754 425 | — / 2495 |
| K = 8 | [1, 10⁹) | 129 (22 primes, last 35 569; last composite 1 239 315) | — |

(to be continued: numerator ladder K = 12…24, mechanism attempts, review)
