# Wave 18 hostile review: §52 per-slice sieve

## Overall verdict

**SOUND-AFTER-REPAIRS.**  Theorem 52.1, Corollary 52.2, and Proposition 52.3 survive a full hostile replay.  I found no theorem-level gap, missing logarithmic loss, or false quantifier.  The fixed-slice exponent is exactly `1+2/phi(h)`; only the growing-modulus proposition loses the stated epsilon fraction.  All default and `ES_FULL_SCAN=1` constants replay.

I made one low-severity honesty repair at `notes.md:19130-19138`: the old sentence “Each norm is factored once per test” could be read as global deduplication, but `(ay)` deliberately refactors some norms in independent panel, census, minimum, and correlation passes.  The replacement states the actual bounded-memory behavior.  No mathematical claim or verifier code changed.

## Claim verdicts

| Claim | Verdict | Hostile finding |
|---|---|---|
| Theorem 52.1, fixed-slice upper bound | **CONFIRMED** | Vanishing is contained in the sifted set, the good class has exactly two nonzero norm roots, the local density is `1/q` ordinarily and `3/q` at good primes, and a fixed-level beta-sieve gives the exact exponent `1+2/phi(h)` with no epsilon loss. |
| Corollary 52.2, no identically vanishing reduced refinement | **CONFIRMED** | For every fixed `M'`, the prime count `~X/(phi(M') log X)` eventually dominates the full-class vanishing bound.  The statement rules out eventual total vanishing, not positive-density vanishing. |
| Proposition 52.3, polylogarithmic uniformity | **CONFIRMED** | Siegel–Walfisz applies from `y=exp((log X)^epsilon)` because `h<=(log q)^(theta/epsilon)` there.  Partial summation produces exactly `(1-epsilon) log log X/phi(h)`, and the ordinary roughness factor supplies `1/phi(Q)`.  Ineffectivity is correctly declared. |
| Computational 52.4 | **CONFIRMED-AFTER-REPAIR** | Every asserted count, witness shape, and correlation replays.  The raw exponent box is correct and the scans are memory-bounded.  Only the factorization-reuse wording needed repair. |
| §52.4 walls and parity discussion | **CONFIRMED** | No pointwise `D(p)` bound, `H_SPF` case, slice union, lower bound, or nonstandard impossibility claim is smuggled in. |
| Cross-references, numbering, and hygiene | **CONFIRMED** | `(52.1)`–`(52.27)` are consecutive; the cited §44/§48/§50 statements match their use; there are no control bytes or malformed backslashes. |

## 1. Theorem 52.1 replay

### Admissibility and the contrapositive

For fixed `(c,k)`, §36 defines admissibility by

```text
(p,ck)=1,  3k<=2p,  4ck<=2p+k.
```

Only finitely many primes fail these conditions.  Thus the sentence at `notes.md:18903-18906` is correct.  For every remaining prime in the fixed class `a mod Q`, Theorem 50.1 (`notes.md:17998-18047`) needs only a prime divisor

```text
q | p^2+4ck^2,  q == -p (mod h).
```

It imposes neither first-power multiplicity, primitivity, nor a size condition on `q`.  Hence its exact contrapositive is

```text
M_{c,k}(p)=0  =>  no prime divisor q == -a (mod h),
```

as stated in (52.4).  This is a raw-slice implication, consistent with (44.4), not the primitive mass (44.4a).

### Automatic splitting, including `q|t`

Write `c=s t^2`.  Since `a` is reduced modulo `h` and every good prime has `q=-a (mod h)`, a good prime is automatically coprime to `h`; the explicit finite exclusion of `q|Q` also removes 2 and 3.  In particular a prime `q|t` cannot be good.  For every retained odd `q`, all of `2,k,t` are nonzero modulo `q`, and

```text
chi_s(q)=chi_s(-a)=chi_s(-1)chi_s(a)=(-1)(-1)=1,
(-4ck^2/q)=(-s/q)=(Delta_s/q)=1.
```

The passage through the fundamental discriminant is valid for all 2-adic cases because the evaluation prime is odd and the discarded factors are nonzero squares.  The congruence

```text
n^2 == -4ck^2 (mod q)
```

therefore has exactly two distinct roots.  Neither is zero, since `q` is coprime to `2ck`.

I explicitly attacked the `q|t` edge with `(c,k)=(45,1)`, so `s=5,t=3,h=180`.  The first active class is `a=73 mod 360`; its first good primes are `107,467,647`, all coprime to `90`, and each has exactly two roots.  The potentially troublesome prime 3 divides `t` and `h`, so it cannot occupy the reduced class `-a mod h`.

### Three local classes, not two or four

At an ordinary prime the roughness sieve removes only `0 mod q`.  At a good prime it additionally removes the two norm roots.  These classes are pairwise distinct.  For the smallest panel example `(c,k,a,h,Q)=(5,1,73,20,120)`, the first good prime is `q=7`, the roots are `1,6 mod 7`, and the removed set is exactly `{0,1,6}`.

Thus

```text
rho(q)=1                 ordinarily,
rho(q)=3                 at a good q,
```

and the extra local correction is exactly

```text
(1-3/q)/(1-1/q)=1-2/(q-1).
```

There is no double-counting of the zero class and no missing `+/-` root.

### Beta-sieve level and remainder

For squarefree `d` coprime to `Q`, the generalized residue-class sieve has

```text
#A_d = X rho(d)/(Qd) + r_d,   |r_d| <= C rho(d),
rho multiplicative,           rho(l)<=3.
```

The Chinese remainder theorem justifies this for the progression `a mod Q`.  Since `rho(d)<=3^omega(d)`,

```text
sum_{d<=D} mu^2(d) rho(d) << D(log D)^2.
```

The standard upper beta-sieve uses upper weights supported on squarefree `d<D`, with absolute value at most one, and gives the remainder form printed in (52.12).  Its dimension condition follows from fixed-modulus Mertens estimates.  Choosing

```text
D=X^(1/2),  u=log D/log z > beta_kappa,  z=D^(1/u)=X^(1/(2u))
```

with fixed sufficiently large `u` is inside the fundamental lemma.  The proof does not use the potentially invalid endpoint `u=2`.  The remainder is

```text
O(X^(1/2)(log X)^2)=o(X/(log X)^kappa).
```

The separately counted `p<=z` are also negligible because `z=X^eta` with fixed `eta<1`.  This validates the level arithmetic at `notes.md:18976-19023`; no Bombieri–Vinogradov or prime distribution remainder is hidden in it.

### Product and exact exponent

The local product is literally

```text
V(z)= product_{l<=z,l∤Q}(1-1/l)
      product_{q<=z,q==-a (h),q∤Q} (1-3/q)/(1-1/q).
```

For fixed `h`, Mertens in the reduced progression gives

```text
sum_{q<=z,q==-a (h)} 1/q = (log log z)/phi(h)+C(h,-a)+o(1).
```

Since `log((1-3/q)/(1-1/q))=-2/q+O(1/q^2)`, the second product contributes `(log z)^(-2/phi(h))`; ordinary Mertens contributes `(log z)^(-1)`.  As `z` is a fixed power of `X`, this is exactly

```text
X/(log X)^(1+2/phi(h)).
```

There is no epsilon or log-log loss in Theorem 52.1.  The constants may first depend on `a`, but there are only finitely many compatible classes modulo fixed `Q`, so taking their maximum justifies the displayed `<<_{c,k}`.

The fixed-modulus PNT/Mertens input is effective in principle for explicitly fixed `(c,k,a)`.  This does not conflict with the separately labelled ineffective growing-modulus use of Siegel–Walfisz.

## 2. Corollary 52.2 replay

Fix a reduced refinement `a' mod M'`, with `M'` fixed.  Its prime count is

```text
X/(phi(M') log X) (1+o(1)).
```

Its vanishing primes are a subset of the full `a mod Q` vanishing set.  Theorem 52.1's constant depends on `(c,k)` but not on `M'`; even if that fixed constant is large,

```text
[X/(phi(M')log X)] / [C X/(log X)^(1+2/phi(h))]
 = (log X)^(2/phi(h))/(C phi(M')) -> infinity.
```

So not all sufficiently large primes in the refinement vanish.  This argument is monotone and does not need a bound uniform in `M'`.

The quantifiers are clean: `M'` and `a'` are fixed and reduced; the claim concerns one fixed slice and rules out eventual identity on the progression.  It does **not** rule out residual vanishing on a positive-density subset, classify simultaneous slices, or give a pointwise positive slice.

## 3. Proposition 52.3 replay

Set

```text
y=exp((log X)^epsilon),  z=X^eta,  h<=(log X)^theta.
```

For every `q>=y`,

```text
h <= (log X)^theta = (log y)^(theta/epsilon)
  <= (log q)^(theta/epsilon).
```

Thus Siegel–Walfisz with fixed parameter `A=theta/epsilon` is uniform throughout `[y,z]`, including varying reduced residue `-a mod h`.  Partial summation gives

```text
sum_{y<q<=z,q==-a (h)} 1/q
 = [log log z-log log y]/phi(h)+o(1)
 = [(1-epsilon)log log X+O(1)]/phi(h)+o(1).
```

This is the sole source of the factor `1-epsilon` in (52.19).

For uniform sieving, `rho(l)<=3` and `2,3|Q`, so a coarse dimension-3 upper sieve supplies a fixed `eta>0`.  Omitting primes dividing `Q` from ordinary Mertens gives

```text
product_{l<=z,l∤Q}(1-1/l) << Q/[phi(Q)log z].
```

Multiplying by `#A ~ X/Q` yields the claimed `X/phi(Q)` normalization.  The extra-root product contributes the displayed sparse exponent.  The remainder `X^(1/2)(log X)^2`, `p<=z`, and uniformly nonadmissible small primes are absorbed because `Q,h` are polylogarithmic while `z` is a fixed power.

Siegel–Walfisz is valid for every fixed logarithmic exponent and all reduced classes, but its usual all-moduli constant/threshold is ineffective.  The proposition correctly excludes arbitrary `h=X^{o(1)}` and does not claim that the fixed-slice relative-density decay is uniform when `phi(h)` grows.

## 4. Computational audit

Block `(ay)` is at `verify.py:9125-9408`.

- `exponent_box_hit` (`verify.py:9147-9158`) starts with grade 1 and, for every `q^e||N`, multiplies by exactly `q^0,...,q^e mod 4ck`.  This is the bounded exponent box (44.4), not an unbounded generated subgroup.
- It tests raw `M_{c,k}`, matching all of §52.  It never substitutes primitive `M*`; the known `(241,7,3)` raw/primitive split is therefore harmless.
- For `ck<=30`, every hard prime is automatically admissible.  “Active” is exactly `chi_s(p)=-1`; the denominators in (52.24) match the code and §48.2.
- Panel norms are factored once per individual evaluation and the same factorization feeds both the exponent-box and good-prime tests.  Independent subtests intentionally refactor some norms.  They stream one norm at a time and retain no large factor cache.
- The gap scan stores only small unresolved sets/maps.  Canonical divisors are generated for one norm and discarded.  “Semiprime” means two distinct primes; prime powers and multiplicity-at-least-three shapes are separated correctly.
- Correlation marginals are recomputed inside the population where both genus signs are `-1`, exactly as (52.26) requires.

All asserted constants replay:

- panel `(class primes, vanishers)` is `(105,35),(66,41),(105,58),(31,24)` below 30,000 and `(297,86),(204,122),(297,163),(98,81)` below 100,000;
- good-prime counts are `413,268,208,141`;
- all 31 residual rows match (52.24);
- gap events/canonical divisors are `74/98` by 30,000 and `221/308` by 100,000;
- canonical shapes are `68/24/6` and `199/93/16` for semiprime/multi-prime/prime-power;
- the two stable anticorrelations replay as `0.5291,0.5769` for `(5,1)x(5,2)` and `0.7143,0.6993` for `(5,1)x(10,1)`.

As an independent check rather than an assertion replay, I directly enumerated literal divisors of every full-range norm for all 31 slices.  All 31 `(active,residual)` rows matched `(52.24)`; this exercises the exact divisor condition independently of `exponent_box_hit`'s residue-set implementation.

## 5. Attempted breaks

| Attack | Result |
|---|---|
| `q|t` square-factor edge, `(c,k)=(45,1)` | Failed: every good prime is reduced modulo `h`, hence coprime to `t`; direct roots were exactly two. |
| Large `phi(h)`, `(c,k)=(1009,1)` | Failed gracefully: `phi(h)=2016`, so `kappa=1.000992...`; the extra saving is tiny but positive for fixed `h`.  The proof reverts continuously toward the ordinary prime-sieve exponent. |
| Feed `chi_s(a)=+1` to Theorem 52.1, `(c,k,a)=(5,1,1)` | This would break the conclusion, as it should: genus forces vanishing, while primes `q==-a mod h` have `chi_s(q)=-1` and zero norm roots.  Hypothesis (52.2) explicitly excludes this class. |
| Force endpoint level `log D/log z=2` | The text does not do this.  It chooses fixed large `u` and `z=X^(1/(2u))`, leaving `D=X^(1/2)` and a negligible elementary remainder. |
| Merge zero with one norm root | Impossible for retained good primes: a zero root would imply `q|4ck^2`, contrary to `q∤Q`.  The local density really is three classes. |
| Require `q||N` or a primitive row | Theorem 50.1 requires only `q|N` and raw positivity.  Multiplicity and gcd `(a,b)>1` do not invalidate the unit-fraction row. |
| Let `M'` be huge | For each fixed `M'`, the extra log power eventually wins.  The corollary makes no uniform-in-`M'` claim. |
| Let `h` grow faster than polylogarithmically | Proposition 52.3 explicitly excludes this; the SW interval argument would no longer be available as printed. |

## 6. Severity-ranked defects

1. **LOW — repaired, `notes.md:19130-19138`: ambiguous factorization-reuse claim.**  The old wording could imply one global factorization per mathematical norm.  In fact independent checks refactor norms, and repeated correlation pairs can do so again.  The repaired text says exactly what is reused and why memory remains bounded.
2. **HIGH/MEDIUM: none.**  I found no incorrect theorem hypothesis, sieve exponent, AP quantifier, computational constant, or cross-reference.

## 7. Overclaim scan by label

- **Scope and outcome (`notes.md:18870-18878`): confirmed.**  “Last fixed-congruence obstruction” is supported only in the stated one-fixed-slice sense and is immediately fenced from pointwise and multi-slice readings.
- **Theorem 52.1: confirmed proved.**  Unconditional, fixed slice/class, raw mass, exact exponent.  No unadvertised SW/BV input.
- **Corollary 52.2: confirmed proved.**  Only fixed reduced refinements and eventual identity are excluded.
- **Proposition 52.3: confirmed proved, ineffective.**  The epsilon loss and polylogarithmic range are explicit; no stacking follows.
- **Computational 52.4: confirmed exact-range/informational after wording repair.**  No asymptotic fit is promoted.  “Consistent with” remains appropriately non-theorem language.
- **Assessment after (52.27): confirmed assessment only.**  It says approximate independence for many pairs and names stable counterexamples; it does not infer independence.
- **Heuristic/assessment in §52.4: confirmed.**  Bateman–Horn/Hardy–Littlewood is only a conjectural lower-bound model.  The parity sentence is about upper-bound/standard sieve methods, not an impossibility theorem for all proofs.
- **Final conclusion: confirmed.**  Relative frequency zero is fixed-class only; infinitude of residual vanishers remains open.

## 8. Cross-references and validation signature

Theorem 44.1 and (44.4) give the exact raw exponent box; (44.4a) records the primitive distinction.  Theorem 48.1 and (48.2)–(48.4) give precisely the forced/active genus split.  Theorem 50.1 and (50.4)–(50.6) need no prime multiplicity or primitive hypothesis; (50.7) is mentioned only as an unproved wall.  Lemma 29.2 has the same two-root CRT mechanism.  The 31-row active/residual counts agree with §48.2 rather than contradicting it.

Equation tags `(52.1)` through `(52.27)` occur once and in order.  Control-byte, CR/NUL, Python syntax, and `git diff --check` scans pass.

**Fully replayed:** the set inclusion, symbol/root calculation, three-class density, beta-sieve level/remainder, Mertens product, exact fixed exponent, corollary comparison, SW interval/partial summation, every required default/full regression, and an independent full-range direct-divisor census.

**Checked structurally:** the standard upper beta-sieve theorem in its usual fixed-dimension fundamental-lemma form, fixed-AP Mertens effectivity, Siegel–Walfisz uniformity/ineffectivity, all `(ay)` storage lifetimes, and the cited §29/§36/§44/§48/§50 interfaces.

Validation in `/tmp/es-rev52`:

- post-repair `uv run --with sympy,numpy,scipy python verify.py`: all checks passed; **1:19.48**, **332,852 KB** peak RSS;
- required `ES_FULL_SCAN=1` full verifier: all checks passed; **8:52.13**, **358,820 KB** peak RSS, no swap;
- independent direct-divisor 100,000 census: 31/31 rows matched; **1.55 s**, **52,932 KB** peak RSS.

— Wave-18 hostile reviewer
