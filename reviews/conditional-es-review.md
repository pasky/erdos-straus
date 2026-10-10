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
