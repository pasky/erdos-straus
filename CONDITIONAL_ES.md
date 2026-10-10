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
