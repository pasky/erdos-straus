# UNIT ADJ51 report

## Outcome

**Overall adjudication: CONVERGED-WITH-DIVERGENCES.**  The blind construction independently recovers both exact witness-tail exponent shapes, both windows, the Section-39 machinery replay, the effective exceptional-conductor repair needed by the class-mass chain, the Theorem-39.7 recovery, and the PW truncation.  This is an independent-construction datum only: every existing **CLAIMED/PROVISIONAL** label remains unchanged.

The frozen artifact is now tracked as `blind51.md`.  Protocol data recorded in Section 51.10:

- base: `4dcf3b7e1e10e31f529f5e2862a2aa23c0820bb6` (pre-wave 18)
- branch: `blind51`
- freeze: `7ecd7d514ae379e9c90d6a7b292d11e80840b360`
- SHA-256: `b0a4a27dba52fb563b4667427f2200cc98e670c27e8fff390aa846b1039c8b7c`

## Tail comparison

- **Definition:** same minimum of `k*l`; the inverse and non-inverse congruences agree because `v` is automatically coprime to `k*l`.  The blind B2--B3 statements explicitly count primes and independently avoid the integer-scope overclaim repaired by the wave-18 review.
- **Variant (a):** both give `exp(-c (log T)^2 log log T)` under `log N >= C (log T)^3 log log T`.  Blind uses the nearly maximal `X` with `K=(log X)^5`; Section 51 uses `X=T^(1/2)`.  This changes constants only.
- **Variant (b):** both give `exp(-c_k (log T)^3)` under `log N >= C_k (log T)^4`, with the same strict `kappa<1/240` geometric constraint.  Blind uses `X=T^(1/(1+kappa))`; Section 51 uses `X=T^(1/2)`.  Again only constants change.
- **Theorem 39.7:** both recover the prime exponent `3/4` at the top of the cubic window and then use the Theorem-16.5 semigroup transfer for all denominators.
- **PW:** both derive the square-log tail and cubic window cost.  The blind file makes explicit that PW's larger-sieve truncation counts all integers and records the general-`m` factor; this is valid and does not strengthen Section 51's `W` headline.

## Discrepancies

1. **Material blind-side effectivity overclaim.**  Blind B4.5 correctly proves effective `(34.18)--(34.19)` for a deletion-surviving subfamily, but its final perimeter sentence then calls all of Theorem 34.8 fully effective.  That does not follow: restoring the deleted triples restores the unresolved exceptional-character error.  Section 51 is correct to leave Theorem 34.8's ancillary all-low-congestion-triples absolute-error `o(1)` sentence ineffective.  This discrepancy does not weaken Theorem 51.6 or change any Section-51 label.
2. **Valid route divergence.**  Blind B4.3 proves deletion tolerance in one box count for every `r` not dividing 4; Section 51 splits the selected prime into `p<=Ck` and `p>Ck`.  Replaying the direct count gives the uniform local factor `(p-1)/(p+1)>=1/3` with no hidden factor `p`, so both close.
3. **Candidate strengthening only.**  Blind B4.2 packages one exceptional conductor across the whole outer range `X^(1/2)<=x<=X`, rather than one per dyadic block.  The top-scale Landau--Page replay is structurally sound because the logarithms are comparable, but this exact stronger formulation is not the direct statement of the checked Lenstra--Pomerance citation.  It should receive a precise citation or a full quantitative proof before promotion.
4. **No exponent or window discrepancy.**  Independent substitution into `mu=t^2 log K`, saving `exp(-c mu)`, and ledger `exp(O(mu*t))` reproduces every `(log T)^2 log log T`, `(log T)^3`, `(log T)^3 log log T`, and `(log T)^4` shape in Section 51.

## Effectivity audit

The constructions agree that Lemma 16.2 is effective; the BV lower supply in Lemma 16.3 and Theorem 34.8 is ineffective as printed; Section 39's upper moments and finite CRT/Bonferroni machinery are effective; and Theorems 16.4--16.5 become effective once the repaired class supply has an effective starting point.  Both explicitly account for characters induced from small primitive conductors and delete all progression moduli divisible by the one possible Landau--Page conductor.

The blind all-`r` deletion lemma survives maximum-severity replay and is a harmless candidate scope strengthening.  It does not improve an exponent, a window, or the effectivity perimeter actually needed downstream.

## Lenstra--Pomerance citation check

The wave-19 citation repair is accurate; no fix was needed.  Lenstra--Pomerance, JEMS 21 (2019), Lemma 11.2, is headed **“effective Bombieri--Vinogradov inequality”** and states (verbatim apart from linearized notation):

> “There are absolute, effectively computable positive numbers `c6, c7` such that for all real `x >= 3`, there is an integer `s(x) in [(log x)^(1/2), exp((log x)^(1/2))]` such that for each real `Q in [x^(1/3) log x, x^(1/2)]`,”
>
> `sum_{q<=Q, s(x) not dividing q} max_{2<=y<=x} max_{gcd(a,q)=1} |psi(y,q,a)-y/phi(q)|`
>
> `<= c6 x^(1/2) Q (log x)^5 + c6 x exp(-c7 (log x)^(1/2)).`

Its proof identifies `s(x)` with the primitive real exceptional modulus when one exists and otherwise chooses a dummy integer.  Taking `Q<=x^(1/2)/(log x)^B`, and enlarging a smaller `Q` to `x^(1/3)log x`, gives (51.20) effectively.  The maximum over `y` supplies one conductor at both endpoints of a dyadic interval before partial summation.  Section 51 correctly calls (51.20) a direct corollary, not a verbatim restatement.

## Priority repair

A marked note now sits immediately after the cubic polylogarithmic display (51.18).  It credits Dahan, arXiv:2608.24035, Theorem 4.17, as the near-simultaneous antecedent for the `(log log N)^3` exponent shape at polylogarithmic depth, while distinguishing his two-parameter `(u,a)` depth statistic with no genus gate from the minimal congruence modulus `W`.  It also contrasts Dahan's explicitly ineffective printed `o(1)` with the effective constants obtained for the Section-51 `W` tail after Lemmas 51.4--51.5.  Section 51.9 now states the shape-antecedent/statistic distinction in one explicit concluding sentence.

## Verification

`uv run --with sympy,numpy,scipy python verify.py` passed in full through block `(az)`.  `git diff --check` passed; `notes.md` has zero forbidden control bytes and zero carriage returns; the Section 5/50/51/52/53 order is unchanged; and the blind artifact's SHA-256 matches its frozen commit.

## Next wave

- If useful, formalize blind B4.3's all-`r` deletion statement; it is valid but currently unnecessary.
- Promote blind B4.2's one-outer-scale conductor only after a precise citation or a full quantitative proof.
- Do not import the blind file's overbroad “Theorem 34.8 fully effective” perimeter sentence.
