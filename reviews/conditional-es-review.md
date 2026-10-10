# R127 — hostile review of O127 (`CONDITIONAL_ES.md` §§1–9, reports O127/O127b, `scripts/cond_*`)

Reviewer: R127 side agent (branch `side-agent/review-conditional`). Author files merged from
`side-agent/conditional-es`. All numerics below are from FROM-SCRATCH code
(`scripts/review_r127_*`), not from the author's scripts. Sources checked: ET
(`sources/elsholtz-tao-1107.1010.pdf`, text-extracted), BL (`sources/bright-loughran-1908.02526.pdf`).

## Summary verdicts (per claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (slice, lift to ES solution) | SOUND |
| Dual form (§6) and remainder form (§7.5) | SOUND-AFTER-REPAIRS (minor: coprimality in the "iff") |
| Prop 2.3 / Lemma 2.1 (scale constraint) | (see §2 below) |
| Cor 4.1 / Remark 4.2 | (see §4 below) |
| Thm 6.1 | (see §6 below) |
| Prop 7.1 | (see §7 below) |
| Prop 7.2 | (see §7 below) |
| Prop 7.3 | (see §7 below) |
| Prop 9.1 + §9 Assessment | (see §9 below) |
| §8 EVIDENCE S(5101441) = 1 | (see §8 below) |

## 1. Lemma 1.1 — SOUND

Re-derived by hand:
* (1)⇒(2): with `f=(m+1)/t`, `c=(m''+1)/t`: `(tf−1)(tc−1) = tn+1` ⇔ `tcf − c − f = n`; `4 | m = tf−1`
  ⇔ `tf ≡ 1 (4)`. (2)⇒(1) by the identity `(gc−1)(gf−1) = g(gcf−c−f)+1`. Cofactor ≡ −1 automatic. ✓
* Lift: `d=(fg−1)/4 ≥ 1` (fg = 1 forces n = −1); `n+c = f(cg−1)`; `4bd = (cg−1)(fg−1) = gn+1`;
  `c + n(b+1) = c(1+ng)`; so the sum is `4/n`. ✓ `t ≤ n+2` from `(t−1)² ≤ tn+1`. ✓
* Dictionary to ET Type I at a = 1 (`b = m''`, `4d = m`, `ct = 1+b`). ✓

**From-scratch brute force** (`scripts/review_r127_lemma11.py 200`): for every 1 ≤ n < 200 the three
forms (1), (2), (3) give *identical* solution sets (as (c,f,g) triples; form (1) enumerated
independently over all (t, m)), all 600 solutions rebuilt and `4/n` checked in exact rationals,
0 failures; the "cofactor automatic" assertion never fired. The dual form of §6 ("least positive
residue g of −n⁻¹ mod m divides m+1", m ≡ 0 (4), gcd(m,n)=1) and the first remainder form of §7.5
(`(cm−n) | (m+1)`) agree with solvability for every odd 1 < n < 200. (Note: in the dual form the
witness g of Lemma 1.1 need not be the least residue — g = m+1 is possible — but then t = 1 also
works, so the equivalence holds; checked numerically.)

Side fact: no slice solution with `n | c` exists for any 3 < n < 200; for primes p > 3 it is
impossible (p | c forces p | f and then `pl(pg−1)… = 2`-type contradiction), so `S'(p) = S(p)`
exactly, not "up to O(1)" (§7.4) — MINOR, harmless.

## 8. §8 EVIDENCE and the full Type I / II counts — SOUND (EVIDENCE confirmed); new data

From-scratch tool `scripts/review_r127_counts.c` (gcc -O2): (a) `S(p)` by *direct* enumeration of
all pairs (c, f) with `(c−1)(f−1) ≤ p+1` (a different algorithm from the author's dual-form scan);
(b) the FULL ordered solution count `f(n)` of `4/n = 1/x+1/y+1/z` by enumerating `x ≤ y ≤ z`,
`x ∈ (n/4, 3n/4]`, and all divisors u ≤ B' of `B'²` (`1/y+1/z = A'/B'`, `(A'y−B')(A'z−B') = B'²`),
each sorted triple weighted by its number of permutations and classified by how many coordinates
n divides; `f_I = #(exactly one)/3`, `f_II = #(exactly two)/3` (ET (1.4)). Validation: the tool
reproduces ET's list `f(2..8) = 3, 12, 10, 12, 39, 36, 46` exactly, and `S` matches the Python
brute force of §1 at 13, 29, 193. Output: `data/review_r127/counts.txt` (2.3 s total).

| p | S(p) (slice) | the slice solution (c, f, g) | f(p) | f_I(p) | f_II(p) |
|---|---|---|---|---|---|
| 2521 | 1 | (2, 87, 15) | 54 | 12 | 6 |
| 5569 | 1 | (17, 7, 47) | 162 | 34 | 20 |
| 21169 | 1 | (4, 31, 171) | 222 | 38 | 36 |
| 43969 | 1 | (20, 31, 71) | 300 | 60 | 40 |
| 5101441 | **1** | (890, 39, 147): `147p+1 = 5732·130829` ✓ | 798 | **188** | **78** |

* **S(5101441) = 1 is CONFIRMED independently** (EVIDENCE), with exactly the author's witness
  (g = 147, m = 5732, m'' = 130829).
* Also confirmed: S = 3 at 943009 and 830041 (least g = 367 at 830041 ✓), S = 2 at all 11
  primes listed in §8 (1201, …, 2922529); the slice (I1) solves every prime 3 ≤ p < 3000 (429
  primes); the Type II a = 1 slice fails exactly at p ∈ {193, 2521} below 3000 ✓.
* Not re-checked: the full 20513-prime scan below 10⁷ (the table's means/minima) — too costly with
  the independent O(p log p) algorithm; spot checks above all agree.
* **New EVIDENCE (answers the author's "suggested next step").** At the slice-singleton primes the
  full counts are *not* O(1): `f_I(5101441) = 188` (`≈ 0.79 log²p`), `f_II = 78`; at the four
  smaller singletons `f_I ∈ [12, 60]`, `f_II ∈ [6, 40]`. So the a = 1 slice is a thin (≈ 1/188 at
  p = 5101441) and fragile part of a Type I family of normal polylog size. The report O127b's
  conditional "if those are also O(1) … ES at hard primes is decided at Planck scale with no
  margin" does **not** occur at these primes. This supports §8's own recommendation (state any
  conjecture for full Type I ∪ II) and weakens nothing else. (R127 repair: a sentence recording
  this has been added below §8's "Reading" — see repairs list.)
