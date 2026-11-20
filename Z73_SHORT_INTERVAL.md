# Where the nonstandard counterexamples can occur

**§0 (z74 Opus xreview fix).**
```
Result: in the integer-landing IOpen + Bézout model of Z73_OPEN_BEZOUT.md, for every infinite a>0 and rational ε>0
        there is a prime q=1+Y² with a<q<a+a^(1/2+ε), q≡1 mod every standard k and ¬ES(q); Bertrand holds.
Label:  PROVED (internal; rel. Z73_OPEN_BEZOUT.md and Shepherdson's criterion)
Scope:  this model is NOT a PID and not externally factorial (landing-zero elements are divisible by every standard k);
        no statement about gaps between actual primes t²+1 or about standard ES; no claim about IE₁, IΔ₀, PA, ZFC.
Review: cross-lab (Opus) data/z74/xreview/REVIEW_PIDEXT_OPUS.md (rows S1–S4: CORRECT)
Triage: HEADLINE (minor variant of the STATUS §1E IOpen + Bézout row; a WAVES mention suffices)
STATUS delta: none
```

**A refinement of the absolute OI+Bézout countermodel**, not a claim about gaps between actual primes `t²+1`. The construction in `Z73_OPEN_BEZOUT.md` can be made to satisfy Bertrand's postulate. More strongly, for each *externally infinite* `a` in the nonnegative cone of the resulting countable model, and each fixed positive rational `ε`, a prime `q` of the model can be forced with

```
a < q < a + a^(1/2+ε),   q=1+Y²,   q≡1 mod every standard k,   ¬ES(q).
```

Rational powers in this display are inequalities in the ordered real closure and can equivalently be cleared to ordered-ring inequalities. This does not assert that every standard integer interval contains such a prime. In particular, the statement that *all* standard ES counterexamples are absent is not used or proved. An internal consequence for each fixed ε is that in this model the display holds above some threshold (choose any positive infinite threshold); what fails is the inference to standard arithmetic.

*Proof.* In addition to the existing stage operations, schedule each pair `(a,ε)` with `a` positive infinite in a finite stage algebra `A` (every element of the final `R` occurs in one; z74 Opus xreview fix) and `0<ε<1/2` rational; these tasks are countable. The range `ε≥1/2` follows by monotonicity. Put `α=√a`, `L=a^(ε/2)` in the old ordered real closure `K`. Adjoin a polynomial variable

```
Y=α+Lz,
```

where `z` is positive bounded with residue transcendental over the countable natural residue field of `K`, e.g. with residue between 1 and 2. Order using the Gauss extension; give `Y` landing zero. For any stage polynomial `G(Y)` of degree `d>0` and leading coefficient `b≠0`, the coefficient of `z^d` after substitution is `bL^d`, infinite: nonzero old coefficients are either rational or infinite. The fresh residue prevents cancellation at the largest scale. Hence every nonconstant polynomial in `Y` is infinite and the required bounded-elements invariant holds. This is why one may prescribe the location of the new prime at this scale, but not specify an arbitrary bounded interval for `Y` around an old ring element. As in the approximation step, adding a free variable preserves the other stage invariants.

`q=1+Y²` is prime since the ordered fraction field does not contain a square root of −1. It has landing 1. At *any* later deformation `s` prime with `e(s)≠0` remains prime: `s−e(s)∈m` implies that `T` is invertible modulo `s`, giving the old prime quotient with Laurent variable. The row operation preserves any old prime by its two charts (the row is coprime). Every later real point has `q>0`, so the semialgebraic positivity argument for ES at the landing works for each such prime; we do not require a new connected-component condition per prime. The construction even works with the norm modification in `LOGIC_NORM_SPLIT.md`: `q` already splits over the Gaussian scalar extension, and only inert primes are targeted for splitting in the real ring. An untargeted prime persists by the saturation lemma there.

The square expansion gives `0<q−a=1+2√a Lz+L² z² < a^(1/2+ε)` because `a` is infinite, `ε<1/2` is standard, and `z` is bounded. Every old positive element and every required pair is serviced. For nonstandard `a` this implies a prime in `(a,2a)`, and for each standard `a>1` Bertrand in ℕ supplies a standard prime, which remains prime in the pullback ring (`R/ℓR=𝔽_ℓ` for a standard prime). Thus Bertrand holds as a single internal axiom, not just at each numeral. These primes are cofinal in the same model and all fail ES there. No bound on standard exceptional primes, and no result about IΔ₀, PA or ZFC, follows. ∎

*Remark (z74 Opus xreview fix).* `ε>0` cannot be dropped for this shape: `LOGIC_NORM_SPLIT.md` (“Bertrand variant and a limit on the interval length”) shows that for infinite `b` with `e(b)=1` no prime `1+Y²` lies in `(b²,b²+Cb)` for any standard `C`. There is no conflict with the display, since `(b²)^(1/2+ε)=b^(1+2ε)` exceeds every `Cb`.
