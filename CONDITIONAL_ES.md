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
witnesses, which have parameters up to p (§1: `gcf ≈ p`). Families of size `p^{o(1)}` escape
Prop 2.3 but meet the other two constraints: bounded families are excluded by POINTWISE_SIZE
Thm C (under H), and families all of whose witness *moduli* (the q of the class `p ≡ r (mod q)`
they test; `q = cf` for (I1)) are `≤ exp((log p)^{1/4−ε})` are excluded by POINTWISE_OMEGA13
Thm 5.1 for the Type II multiplier witnesses (and by POINTWISE_OMEGA Thm 8.5,
`ck_min ≫ log p·log₃p` i.o., for Type I slices). A family such as `{g ≤ G}` with G small but
`c, f` unrestricted is not of either kind, and is not excluded by anything in this section.

## 3. The fixed-p count, and what GRH gives

### 3.1 The slice count and its character expansion

Let `S(p) := #{(c,f,g) ∈ ℕ³ : cfg − c − f = p, fg ≡ 1 (mod 4)}` (Lemma 1.1). Since `fg ≡ 1 (4)`
forces g odd, Lemma 1.1(1) gives, with `n_g := gp + 1`,

```
S(p) = Σ_{g ≤ p+2, g odd, gp ≡ 3 (4)}  #{m | n_g : 4 | m, m ≡ −1 (mod g)}            (3.1)
     = Σ_g  φ(g)^{−1} Σ_{χ mod g} χ(−4) τ_χ(n_g/4),      τ_χ(k) := Σ_{m | k} χ(m).     (3.2)
```

(3.2) is orthogonality (every divisor of `n_g` is prime to g). The principal characters give
`S_0(p) = Σ_g τ(n_g/4)/φ(g)`; heuristically `S(p) ≍ log² p` (each g ≤ p contributes
`≈ τ(n_g)/g` on average). **EVIDENCE** (`scripts/cond_slice_count.py 100000 8`): for the first
8 primes above 10⁵, S(p) ∈ [17, 42] (`S/log²p ∈ [0.13, 0.32]`); for the first 8 Mordell-hard
primes above 10⁵, S(p) ∈ [6, 16] (`[0.045, 0.12]`), least g ∈ {3, 11, 19, 23}. Both are polylog,
as Prop 2.3 requires of any driver.

**Proposition 3.1 (the cancellation needed; PROVED bookkeeping).** Write
`S(p) = S_0(p) + S_1(p)` with `S_1` the non-principal part of (3.2). Then ES(p) follows from
`|S_1(p)| < S_0(p)`. The available bounds are:
1. *Character-by-character.* `|τ_χ(k)| ≤ τ(k)`, so `|S_1(p)| ≤ Σ_{g ≤ p+2} τ(n_g/4) ≍ p log p`
   (the last sum is a divisor sum over an arithmetic progression mod p of length p,
   `≍ p log p` by Shiu/standard). Gap: a factor `≍ p/log p`.
2. *Termwise in g.* `S_1` is the sum over g of `D_g := #{m | n_g: class} − τ(n_g/4)/φ(g)`, and
   `Σ_g |D_g| ≤ S(p) + S_0(p)`. So the problem is exactly the **pointwise concentration of a
   sum of ≍ p nonnegative integer variables with total mean ≍ log² p**: S(p) ≥ 1 is a
   Poisson-scale lower-tail statement. A square-root-cancellation hypothesis in g (errors
   `≪ (Σ_g D_g²)^{1/2} ≈ (log p)^{1+o(1)}` in a random model) would suffice; anything with a
   power of p in the error does not.

### 3.2 What GRH (and BV/EH/Montgomery/Hooley-type prime statements) give

*Fixed p.* In (3.2) each character χ (mod g) occurs at **one** argument `n_g/4`. GRH for
L(s,χ) (and for L(s,χ)ζ(s), whose coefficients are τ_χ) controls weighted sums
`Σ_k τ_χ(k)w(k/X)` with errors `≪ X^{1/2}(gX)^ε` (or `X^{1/2}log²(gX)` for primes); it gives
nothing about a single coefficient beyond the trivial bound of item 1, since one coefficient
is a sum of length 1. Item 1 is therefore what "GRH applied character by character" gives, and
it misses by `p^{1−o(1)}`. Two further GRH mechanisms:
* *Least primes with prescribed Frobenius* (Ankeny, Lagarias–Odlyzko under GRH: `ℓ ≪ (log d_K)²`).
  The ES witness conditions are divisibility conditions `ℓ | N` for the specific integers
  `N = tp+1` or `p+e` (Lemma 1.2), coupled to congruences of ℓ modulo the free parameter.
  A divisibility condition `ℓ | N` is a *ramification* condition in fields like `ℚ(√N)`, not a
  Frobenius condition, and the set of ℓ with `ℓ | N` is finite, whereas a Chebotarev set has
  positive density. Where Frobenius data does help (quadratic characters such as `(ℓ/p) = −1`,
  `ℓ ≡ 3 (4)`), the witnesses produced have size `(log p)^{O(1)}` for fields of discriminant
  `p^{O(1)}`, and **multiplier mechanisms with witness moduli ≤ exp((log p)^{1/4−ε}) fail
  infinitely often** (POINTWISE_OMEGA13 Thm 5.1, unconditional). To reach moduli
  `exp((log p)^{1/4})` one needs fields with `log d_K ≥ exp((1/2)(log p)^{1/4})`, e.g.
  `ℚ(ζ_M, √p)` with `M ≈ exp((log p)^{1/4})`; Frobenius in such a field determines
  `(ℓ mod M, (p/ℓ))`, not the residue `p mod ℓ` that the witness condition needs (Assessment;
  power-residue symbols `(p/ℓ)_k` give p only modulo k-th powers).
* *Averages over p (the dual direction).* GRH/EH/BV give `π(x; q, a)` for q up to `x^{1/2}` (GRH,
  BV on average) or `x^{1−ε}` (EH). Through any forced-class (CRT) majorant they cannot beat the
  exceptional-set saving `exp(−C(log N)^{3/4}(log log N)^{3/4})`, at any polynomial level
  (EXCEPTIONAL_PRIMELAW Cor 4.2, PROVED; Montgomery's conjecture `π(x;q,a) − li(x)/φ(q) ≪
  (x/q)^{1/2+ε}` and Hooley-type variance asymptotics are prime-law inputs of this kind). And
  any average-over-p statement is blind to a set of exceptions of counting function
  `o(x^{1/2})`; it can give `E(N) = o(π(N))`-type results, never finiteness, unless supplemented
  by a pointwise input.

**Conclusion of §3 (Assessment, with the PROVED parts cited).** GRH controls primes and
L-function averages; ES(p) for fixed p is the factorisation pattern of the ≤ p+2 integers
`gp + 1` (or `p + e`). The needed cancellation is Poisson-scale and pointwise in p, which is a
different kind of statement from any listed hypothesis.

## 4. Small-scale equidistribution (Heegner points, lattice points on spheres)

**What is known (checked in the source, `arXiv:1910.01360v2`, Humphries–Radziwiłł, CPAM 2022).**
Let `Λ_D` be the Heegner points of discriminant D (`#Λ_D = h(D) = |D|^{1/2±o(1)}`).
* HR Thm 1.12(1), unconditional: for annuli with `|D|^{−1/12+δ} ≪ r < R ≪ 1` and
  `|D|^{−1/2+δ} ≪ μ(A_{r,R}) ≪ 1`, the count is asymptotic to the expectation for **almost
  all centres** w. Expected count `≥ |D|^{δ}`.
* All centres: HR Thm 1.6 (sphere) under GLH for balls of area `n^{−δ}`, `δ < 1/4`; the Heegner
  analogue is Young [You17 Thm 2.1] / Humphries [Hum18 Thm 1.24] (cited by HR; exponents not
  re-checked here). Expected count `≥ |D|^{1/2−1/4−o(1)} = |D|^{1/4−o(1)}`.
* HR §1 (end) note that even balls (r = 0) at radius `|D|^{−1/4+δ}`, expected count `|D|^{2δ}`,
  are beyond their method; Linnik/Bourgain–Rudnick-type conjectures are `|D|^{ε}`-lossy.

**Corollary 4.1 (PROVED, given Prop 2.3).** Let `Λ_{D(p)}` be any Heegner family with
`|D(p)| ≥ p^κ` (κ > 0 fixed) and let `Φ_p` map target points to ES solutions of p at most
`p^{o(1)}`-to-one. No asymptotic equidistribution statement in any of the three ranges above
(nor in any range whose expected count is `≥ |D|^{η}`, η > 0) drives an ES-detector for all
large p: Prop 2.3 forces the expected count to be `≤ p^{o(1)}` for all p outside a set of
counting function `O(N^{1−δ}log³N)`, while these ranges have expected count `≥ p^{κη}`.
The almost-all-centres results fail a second time: the ES target is a specific region
determined by p, and "almost all w" says nothing about one w.

**Remark 4.2 (covering-type hypotheses escape Prop 2.3 formally, but not usefully).** A pure
existence hypothesis ("every ball of expected count ≥ X^ε contains a point": optimal strong
approximation / covering exponent, Sarnak's letter, Sardari, Browning–Kumaraswamy–Steiner) gives
`#𝔗_p ≥ 1` without `#𝔗_p ≍ M`, so Prop 2.3 does not apply. But then the target ball would have
expected count `X^ε ≥ p^{κε}` and actual count `≤ p^{o(1)}` (Lemma 2.1, for almost all p): it
would be a *deficient* ball, contradicting the (believed, and partly GLH-proved) asymptotic for
balls at that scale. So if the asymptotic small-scale conjecture holds at expected count
`X^{ε}`, ES-targets in families of size `≥ p^κ` are never balls (or other regions of bounded
Sobolev complexity), for almost all p (PROVED implication). The targets that actually encode ES
are cut out by divisibility conditions (§1: the modulus of the congruence depends on the
point), to which ball-covering statements do not apply. Moreover, the parameter equations of §1
are split (`(gc−1)(gf−1) = gp+1`: for fixed g a hyperbola `XY = N` with `τ(N) = N^{o(1)}`
points) or have point-dependent moduli (ET's quadric `ef − dA² = 1`, A = 2a, with the condition
`f ≡ −p (mod 2dA)`); no fixed anisotropic quadric with `≥ p^κ` points on which ES is a
fixed-modulus congruence condition was found (Assessment).

## 5. The standard hypotheses, ranked, with the exact gap

"Driver" = Definition 2.2. "Prop 2.3 gap" = the mechanism's main term is a power of p, while a
driver needs main term `p^{o(1)}` for almost all p.

| H (weaker → stronger, roughly) | best mechanism toward ES(p), p fixed | outcome / exact gap |
|---|---|---|
| Selberg eigenvalue conj. (SEL) | Kuznetsov / DI spectral large sieve for the Type I SL₂ form `ef − 4a²d = 1` ((D)32) | gives `Σ_{p≤N} f_I(p) ≪ N log²N` (an average; now unconditional, (D)32b). At fixed p the Kloosterman-sum error terms are power-size in the level; Prop 2.3 gap. |
| GRH (Dirichlet, Hecke) | (a) character expansion (3.2); (b) least prime with given Frobenius; (c) primes in APs on average over p | (a) trivial bound only, misses by `p^{1−o(1)}` (Prop 3.1.1); (b) witnesses of size `(log p)^{O(1)}`: multiplier mechanisms with moduli `≤ exp((log p)^{1/4−ε})` fail i.o. (OMEGA13 Thm 5.1); ES conditions are divisibility (ramification-type), not Frobenius, conditions (§3.2); (c) capped at saving `exp(−C(log N)^{3/4+o(1)})` in E(N) (PRIMELAW Cor 4.2). |
| EH / GEH, BV, Montgomery's and Hooley's AP conjectures | prime-law / linear certificates | same as GRH (c); linear certificates capped at exponent 1/4 in the W(p) scale (OMEGA15/16). Averages over p never give finiteness of the exceptional set. |
| GLH, Lindelöf in level–discriminant aspect, GRH for Rankin–Selberg | Weyl sums of Heegner/CM points, small-scale equidistribution | all-centre range: expected count `≥ |D|^{1/4−o(1)}`; almost-all range: `≥ |D|^{δ}` and wrong quantifier. Cor 4.1: no driver for families with `|D| ≥ p^κ`. |
| Twisted Linnik / optimal strong approximation (covering exponent) | covering of balls on a quadric | escapes Prop 2.3 formally (existence, not asymptotic), but ES targets are not balls if the small-scale asymptotic holds (Remark 4.2, PROVED implication); the ES parameter varieties are split or have point-dependent moduli; no admissible quadric found (Assessment). Gap: structural, not a numerical exponent. |
| Schinzel H / Bateman–Horn (not on the list; for comparison) | prime values of polynomials in p | works *against* ES-proofs: every bounded witness procedure fails i.o. under H (POINTWISE_SIZE Thm C). |

**Contrast with a model success (Assessment, from LITERATURE_2026 (iii)).** For `xy+yz+zx = n`
(Borwein–Choi 2000), GRH suffices to remove the one possible extra exception, because the
representations are counted by a class number, `≍ n^{1/2±o(1)}`, and GRH is needed only to rule
out a Siegel zero (a power-size lower bound for the count). ES is the opposite case: by
Lemma 2.1 the full solution count is `p^{o(1)}` for almost all p, so no superfamily of ES
solutions has a class-number-size count with bounded multiplicity. This is the structural
reason why "GRH ⇒ ES" is not available by the Borwein–Choi template.

## 6. A conditional theorem with a natural, ES-strength hypothesis

**Conjecture X_slice.** For every sufficiently large prime p there are positive integers c, f
with `cf | p + c + f` and `f·(p+c+f)/(cf) ≡ 1 (mod 4)`. Equivalently (Lemma 1.1, dual form):
for some m ≡ 0 (mod 4) prime to p, the least positive residue g of `−p^{−1}` modulo m divides
`m + 1`.

**Theorem 6.1 (PROVED).** X_slice ⇒ ES(p) for all sufficiently large primes p, with an explicit
solution `(bdp, cd, bcd)` (Lemma 1.1).

X_slice is a single two-variable divisibility condition (a "Kloosterman fraction `−p̄/m` hits
the divisor set of `m + 1`" statement), but it is **not** weaker in difficulty than ES restricted
to Type I: it is one slice of it. **EVIDENCE:** X_slice holds for every prime 3 ≤ p < 3000 and
every Mordell-hard prime below 2·10⁶ (§1); counts `S(p) ∈ [6, 42]` near 10⁵ (§3.1); in the
random model `S(p)` is a sum of ≍ p rare events with mean `≍ log² p`, so
`P(S(p) = 0) ≈ exp(−c log² p)`, summable (Assessment; the true lower tail is governed by the
correlated small-modulus part, cf. the exponent-3 tail of W, so this model is only indicative).

**Why no listed hypothesis implies X_slice (the negative result, with scope).**
1. (PROVED, Prop 2.3) No hypothesis delivering a lower bound `≥ M/2` for a target with main
   term `M ≥ p^η` and `p^{o(1)}`-to-one encoding can drive X_slice (or ES) for all large p.
2. (PROVED, Cor 4.1) This covers every small-scale equidistribution theorem for Heegner/CM points
   with `|D| ≥ p^κ` in the ranges known unconditionally or under GLH, and their `|D|^ε`-lossy
   Planck-scale conjectures.
3. (PROVED citations) Prime-law inputs (GRH/EH/BV/Montgomery/Hooley) through CRT majorants are
   capped in the averaged problem (PRIMELAW), and multiplier mechanisms with witness moduli
   `≤ exp((log p)^{1/4−ε})` (which is where GRH-Chebotarev witnesses live for fields of
   discriminant `p^{O(1)}`) fail i.o. (OMEGA13).
4. (Assessment) GRH says nothing about a single coefficient `τ_χ(n_g/4)`, and (3.2) uses each χ
   once; what X_slice needs is Poisson-scale concentration, pointwise in p (Prop 3.1.2).
5. (Assessment) Covering-type hypotheses would need an ES encoding as balls on a quadric with
   power-many points; Remark 4.2 shows this is incompatible with the small-scale asymptotic, and
   none was found.

Scope of the negative result: items 1–3 are theorems about *mechanisms* (classes of arguments
or outputs), not a proof that "GRH ⇏ ES", which cannot be proved by such means. Not covered:
hypotheses producing lower bounds with power-small *relative* errors for polylog-size weighted
counts (Remark 2.4), and genuinely new non-asymptotic mechanisms.
