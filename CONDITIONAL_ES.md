# ES for large primes conditional on a standard conjecture? (task O127)

Status: IN PROGRESS. Labels as in DISCOVERIES.md. ES is not proved here, and (checked against
`LITERATURE_2026.md`, which has no such entry) ES is not known even under GRH.

## 1. Exact divisor-in-progression forms

Notation: ET = Elsholtz–Tao, arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`), §2.
For a prime p every positive solution of `4/p = 1/x+1/y+1/z` is of Type I (p divides exactly
one denominator) or Type II (exactly two): p cannot divide all three, since `1/x'+1/y'+1/z' = 4`
has no positive solution.

**Lemma 1.1 (Type I, slice a = 1; PROVED).** Let n ≥ 1. The following are equivalent.
1. There are t ≥ 1 and a factorisation `tn + 1 = m·m''` with `m ≡ m'' ≡ −1 (mod t)` and `4 | m`.
2. There are c, f, g ≥ 1 with `c(fg − 1) − f = n` and `fg ≡ 1 (mod 4)`.
3. There are c, f ≥ 1 with `cf | n + c + f` and `f·(n+c+f)/(cf) ≡ 1 (mod 4)`.

If they hold, then with `d = (fg−1)/4`, `b = (n+c)/f` (an integer) one has
`4/n = 1/(bdn) + 1/(cd) + 1/(bcd)`.

*Proof.* (2⇔3): put `g = (n+c+f)/(cf)`; `c(fg−1) − f = n` is `cfg = n+c+f`.
(1⇔2): the identity `(gc − 1)(gf − 1) = g(gcf − c − f) + 1` shows that (2) gives (1) with
`t = g`, `m = gf − 1`, `m'' = gc − 1`. Conversely, given (1), put `f = (m+1)/t`, `c = (m''+1)/t`
(positive integers since m, m'' ≥ 1 are ≡ −1 mod t); then `t(tcf − c − f) + 1 = tn + 1`, i.e.
`cft − c − f = n`, and `ft − 1 = m ≡ 0 (mod 4)`.
Solution: with `d = (fg−1)/4` we have `4cd = c(fg−1) = n + f` and `fg = 4d + 1`. Then
`f | n + c` because `n + c = c(fg − 1) − f + c = f(cg − 1)`, so `b = cg − 1 ≥ 0`, and b ≥ 1
unless c = g = 1, which would give n = −1. Finally
`1/(bdn) + 1/(cd) + 1/(bcd) = (c + bn + n)/(bcdn)` and `c + n(b+1) = c + ncg = c(1 + ng)`, while
`4bd = (cg−1)(fg−1) = gn + 1` (the identity above). So the sum is `c(1+ng)/(bcdn) = 4bd/(bdn) = 4/n`. ∎

This is ET Prop 2.3 (second and fifth bullets) at a = 1, i.e. the points of ET's variety Σ_I
with a = 1 (`4bd = ne + 1` with e = g, `ce = 1 + b`); the factorisation form (1) is the
"tp+1 has a divisor ≡ −1 (mod t)" statement of the brief, made exact: **the cofactor is then
automatically ≡ −1 (mod t)** (`m·m'' ≡ 1`), and the only side condition is `4 | m` (equivalently
`tn ≡ 3 (mod 4)` together with the choice of which factor carries the 4).

**Lemma 1.2 (general Type I and Type II; ET Prop 2.3/2.7, PROVED there).**
* Type I: ES(n) holds if there are t, a, b ≥ 1 with `4ab | tn + 1` and `a + b ≡ 0 (mod t)`;
  solution `(abdn, acd, bcd)` with `4abd = tn+1`, `ct = a+b`.
* Type II: ES(n) holds if there are e, a, b ≥ 1 with `4ab | n + e` and `a + b ≡ 0 (mod e)`;
  solution `(abd, acdn, bcdn)` with `4abd = n+e`, `ce = a+b`
  (check: `4/n − 1/(abd) = e/(abdn) = (a+b)/(abcdn)`).
Every Type I (resp. II) solution of a prime n arises this way (ET Props 2.2, 2.6).

Lemma 1.1 is the case a = 1 of the Type I statement (then `b = m''`, `4d = m`). Note
`m, m'' ≥ t − 1` forces `t ≤ n + 2`, and `gcf ≈ n`: all parameters are bounded by n + 2.

**EVIDENCE (`scripts/cond_divisor_forms.py`, and `scripts/cond_hard_I1.py 2000000`).** Every solution found is
rebuilt and `4/p` checked in exact rationals.
* The slice (I1) of Lemma 1.1 alone solves every prime 3 ≤ p < 3000; the Type II slice a = 1
  (`b | (p+e)/4`, `b ≡ −1 (mod e)`) fails for p = 193, 2521.
* (I1) solves all 4519 Mordell-hard primes (p a square mod 840) below 2·10⁶, with
  `t ≤ 367` (maximum at p = 830041).

So the single two-variable condition **"cf | p + c + f for some c, f (with the mod-4 side
condition)"** is the natural target; it is a representation problem for the cubic polynomial
`P(c,f,g) = cfg − c − f` (Lemma 1.1(2)).

## 2. The scale constraint: detectors must work at main term p^{o(1)}

Write `f(p)` for the number of ordered positive solutions of `4/p = 1/x+1/y+1/z`.

**Lemma 2.1 (PROVED relative to ET Thm 1.1 and (1.4)).** `Σ_{p≤N} f(p) ≪ N log²N log log N`
(ET, display after Thm 1.1; the campaign's (D)32b improves this to `≪ N log² N`). Hence for
every λ > 0, `#{p ≤ N : f(p) > λ} ≪ N log²N log log N/λ`; in particular for fixed δ > 0 all but
`O(N^{1−δ} log³N)` primes p ≤ N have `f(p) ≤ N^δ`. (Markov.)

**Definition 2.2.** An *ES-detector* is, for each large prime p, a finite set `𝔗_p` (the target)
and a map `Φ_p : 𝔗_p → Sol(p)` whose fibres have size ≤ μ(p). A hypothesis H *drives* the
detector if H implies, for every large p, `#𝔗_p ≥ M(p) − R(p)` with explicit `M(p) > R(p)`.

**Proposition 2.3 (PROVED, given Lemma 2.1).** If H drives an ES-detector with `R(p) ≤ M(p)/2`,
then `M(p) ≤ 2μ(p) f(p)`; hence for every δ > 0, `M(p) ≤ 2μ(p) p^{δ}` for all primes outside a
set of counting function `O(N^{1−δ} log³ N)`. If μ(p) ≤ p^{o(1)} (every natural parametrisation
of solutions by lattice points, Heegner points, matrices `γ = (e 2a; 2ad f)` etc. is O(1)-to-one
or `p^{o(1)}`-to-one by the divisor bound), then `M(p) ≤ p^{o(1)}` for almost all p.

*Proof.* `#𝔗_p ≤ μ(p)·#Sol(p) = μ(p) f(p)`, and `#𝔗_p ≥ M − R ≥ M/2`. Apply Lemma 2.1. ∎

*Consequence (the scale constraint).* Every equidistribution statement whose main term for the
target is a power `p^η` of p — this includes every shrinking-target theorem proved or provable
from GLH/GRH/Lindelöf in the range where its main term dominates its error (§4) — is excluded
as a driver, unless it is applied to a family whose map to solutions is `p^{η−o(1)}`-to-one.
A driver must establish positivity of a count whose main term is `p^{o(1)}` (heuristically
`≍ log² p` for the slice (I1), §3.1). This is the precise sense of the brief's "near-Planck
scale". It is a statement about the *output*, so it holds whatever the hypothesis H is.

**Remark 2.4 (what "near-Planck" excludes, and what it does not).** Prop 2.3 does not exclude
hypotheses whose *errors* are power-small relative to a polylog main term (e.g. a count
`Σ w(x)` normalised so that `M ≍ log² p` and `R ≪ p^{−η}`). It excludes the standard mechanism
"main term ≍ (size of family)×(measure of target), error ≪ (size of family)^{1−η}", because that
mechanism needs `M ≥ (size)^{η}` and the family must have size `≥ p^{c}` to contain the
witnesses, which have parameters up to p (§1: `gcf ≈ p`). Small families (size `p^{o(1)}`) are
the congruence/bounded-witness regime and are excluded by POINTWISE_SIZE Thm C (under H) and
POINTWISE_OMEGA13 Thm 5.1 (unconditionally, witness moduli `≥ exp((log p)^{1/4−o(1)})` i.o.).
