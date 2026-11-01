# z53 NONCRTSMOOTH — independent hostile review

Reviewed `side-agent/z53-noncrtsmooth` at `c3aee5775ee23a3d52f00b4aa264fee5d8e26194`.
**Verdict: ACCEPT-WITH-FIXES.** The elementary core and all recomputed data survive; the unrestricted
fixed-modulus barrier and the identification of Type II with full ES do not. ES remains OPEN.
The lane verdict **narrowed** survives only with the scopes below; it is not a general method-impossibility theorem.

## Per-claim audit

| Claim | Classification | Independent derivation / finding |
|---|---|---|
| Lemma 3.1 | CORRECT | Expand `xy−1=4C(4uBC−u−B)`. If `p|u`, the equation forces `p|B`, impossible by size. Conversely the inverse congruence makes `Z` a multiple of p, and `2≤Z<2p` forces `Z=p`. |
| §3 widened window | CORRECT | `(1,1,(n+1)/2)` gives `Z=2n<3n` for every positive odd n, including squares. |
| Proposition 3.2 | CORRECT | `u≤(p+1)/3`, hence `x=(p+u)/B≤(4p+1)/3<4p`; similarly y. The inverse representative is therefore y. Conversely `h>0`, `4|h`, and `h|x+1` force `y≡−1 (h)`, recovering the unique triple. |
| Proposition 3.2 character sign | CORRECT | `(-4Cp/x)=1`, while `(-4C/x)=-1` since `x≡−1 (4C)`. Thus `(p/x)=-1`; reciprocity and `x≡3 (4)` give `(x/p)=-(-1/p)`. The p≡1 (4) hypothesis is present. |
| Lemma 3.3 | CORRECT | Invertibility of x modulo 4p makes two heights differ by a multiple of x; `x≥4M−1>M` gives uniqueness. A triple contributes exactly when `C|M|Cu`, giving τ(u) choices. |
| Lemma 3.4 | CORRECT | Expanding `(qu−1)(qB−1)` gives `quB−u−B=κp`. Substitute `(c,d)=(κ,q/(4κ))`; the missing ET coordinate is automatically `e=(u+B)/κ=4duB−p>0`. This characterizes Type II, not full ES. |
| Lemma 3.5 and listed admissible pairs | CORRECT | Each prime factor of a putative x has `(-κq/ℓ)=1`; the primitive odd character consequently gives both `χ*(x)=1` and `χ*(-1)=-1`. For Type II strip κ² from `κq=4κ²d`; for square cofactors strip s². An odd prime outside q with odd exponent survives in the conductor. |
| A0 | CORRECT | `C≡C₀ (ℓ)` and `4C|ℓ+1` imply `C<ℓ`, hence `C=C₀`; the converse follows by reducing the complementary divisor modulo 4C. This is a construction, not an impossibility theorem for other uses of free primes. |
| A1 | CORRECT | `(2p+1)²=4p(p+1)+1`, `q=2(p+1)`, κ=2; for p≡1 (4), q/4 is odd. The same identity holds at odd squares. |
| A2 and size calculation | CORRECT | Reciprocity gives `(-p/ℓ)=1`; one of the two roots is even and less than ℓ. Then `4ℓ|ps²+1+ℓ`. The Egyptian-fraction identity follows by a common denominator. For ℓ<p, `4H≥p/ℓ` and `s<ℓ` imply the stated logarithmic bound. GRH size remarks remain conditional assessments. |
| A2 → A3 exact criterion | CORRECT | If `s²|C′`, then `s²|ℓ+1`; writing `ℓ+1=s²w` gives `C′/s²=(p+w)/(4ℓ)`. Thus the equivalence is exact. The proposed triple satisfies `s²wB−w−B=ℓB−w=p`. It is a sufficient route to (★), not an equivalence with all (★) solutions. |
| Theorem B(a) | CORRECT | Explicitly take `y=q*((q−1)^(-1) mod p)−1`. Then `xy−1` is a positive multiple of qp and `<(q−1)qp`; hence `1≤κ≤q−2`. |
| Theorem B(b) | CORRECT | Order u≤B. Then `u≤sqrt(jX/(q−2))`; solvability of `(qu−1)B≡u (j)` forces `gcd(qu−1,j)=1`. Count one progression, sum the harmonic bound, double, and use `Σsqrt(j)≤J^(3/2)`. All constants have slack. For q not divisible by 4, explicitly extend the definition of κ or restrict the statement to 4ℕ. |
| Corollary B1 as stated | CORRECT | For `q≤sqrt(X)`, the two normalized errors are `O((log X)^(-η))` and `O((log X)^(-2−3η/2))`. This is uniform for one q(X), not a simultaneous assertion over q. |
| Unrestricted B1 restatements (§§4.4–4.5, 7) | WRONG | Dropping `q≤sqrt(X)` permits the explicit counterexample in fix 1. Also for fixed small q the threshold eventually falls below 1, so B1 alone says nothing about κ=1 there. |
| Corollary B2 | CORRECT-WITH-FIX | The per-j sum is valid, but specify the q-growth range for `o(1)`; the explicit remainder in fix 1 avoids any ambiguity. |
| Theorem C(a) | CORRECT | Fixing `C|M` leaves exactly the divisor-in-class event for `4Cp+1`. Lemma 3.3 gives the count and the total multiplicity identity. |
| Theorem C(b) | CORRECT (CONDITIONAL) | The finite set `{(c,d)=(1,C):C|M, M∈𝓜}` fits the cited theorem exactly. Checked `reviews/redteam-automorphic-2.md` Thm 2.2(iii) against `POINTWISE_SIZE.md` Thm C/Cor C1. Hypothesis H is essential to the asserted infinite failures. |
| Theorem C(c), §5 census and fixed-q data | CORRECT as finite EVIDENCE/CERTIFIED | Independently recomputed all four census samples and all 290 fixed-q rows, with exact agreement; details below. Neither linear cofactor growth nor any asymptotic zero law is certified. |
| §4.4 literature dictionary | CORRECT within stated applications | The five primary theorem statements checked below match. Free objects, density over classes, and upper bounds do not by themselves supply the tied divisor. “None reaches A3/A4” is an assessment of these uses, not a universal theorem. |
| §5.1 Poisson conclusion | GAP | A zero law for the prime-restricted count does not alone put its zeros at primes with R>0; an additional assumption on unrestricted failures or a joint zero law is needed. |
| §4.2 “ES is the union”, §7 “Writing ES as … makes this exact” | GAP / unsupported equivalence | Lemma 3.4 gives Type II. Full ES at a prime is Type I OR Type II; no converse ES ⇒ Type II is supplied. Fix 2. |

## Numerical replication

New engine: `scripts/z53_xrev_noncrtsmooth_census.cpp`. It enumerates `u≤B` and
`1≤C≤(p+2u)/(4u²)`, tests `4uC−1 | p+u`, and recovers B. It never factors `p+u` or `4Cp+1`.
A bounded SPF sieve independently classifies x,y; both orientations are counted, and divisors of u/B give closure counts.
All **18 CSV columns match exactly for 10,747 inputs**: 9,732 p24; 15 test; 600 near-square; 400 s1e7.
The auditor independently sieves the complete p24 prime list and verifies the archived second-engine coverage is complete and duplicate-free.

| Sample | R=0 | R>0, no prime coordinate | R>0, no both-prime pair | Both p^(1/4)-smooth absent among R>0 | Mean best-PM/log p |
|---|---:|---:|---:|---:|---:|
| p24 <10⁶ | 9 | 85 (max 997201) | 4614/9723 | 98.80695% | 0.434511 |
| test | 10 | 3 (2521,3361,66529) | 5/5 | 100% | — |
| near-square | 1 | 0 | 292/599 | 98.66444% | 0.522951 |
| s1e7 | 0 | 0 | 156/400 | 98.75000% | 0.518649 |

`scripts/z53_xrev_noncrtsmooth_audit.py` independently recomputes fixed-q rows by solving
`B=(jp+u)/(qu−1)` for every j≤q and admissible u, with no factorization: **290/290 exact matches**
for κ_min, N_(q/4), N_q, and CRT witnesses. Near-10⁶ means κ_min/q range from 0.131579 to 0.217105.
Existing compact-form and A2 checks also rerun successfully. The independent census additionally verifies smoothness and all closure columns, beyond the original second engine.
Commands ran with `ulimit -v 6000000`, CPU limits and wall `timeout`; the C++ engine rejects sieve lengths above 20 million.

Reproduce after extracting the reviewed branch's data into `/tmp/xrev_NONCRTSMOOTH`:
```sh
ulimit -v 6000000; ulimit -t 600
 timeout 30s g++ -O2 -std=c++17 -o /tmp/xrev_NONCRTSMOOTH/census scripts/z53_xrev_noncrtsmooth_census.cpp
 timeout 480s bash -e -c 'for f in p24 test nearsq s1e7; do /tmp/xrev_NONCRTSMOOTH/census < /tmp/xrev_NONCRTSMOOTH/data/z53/noncrtsmooth/in_$f.txt > /tmp/xrev_NONCRTSMOOTH/census_$f.csv; done'
 timeout 360s uv run python scripts/z53_xrev_noncrtsmooth_audit.py /tmp/xrev_NONCRTSMOOTH
```

## Primary-source checks

Downloaded/read the relevant statements in [Ramaré–Walker Thm 1.1](https://arxiv.org/pdf/1610.05804),
[Szabó Thms 1–3 and EOS/GRH remark](https://arxiv.org/pdf/2208.05762),
[Harman–Shparlinski Thm 1](https://arxiv.org/pdf/1408.4515),
[Shparlinski Thm 13](https://arxiv.org/pdf/1103.2879), and
[Bourgain–Garaev Thm 2](https://arxiv.org/pdf/1211.4184). Their quoted hypotheses/exponents agree.
Also read the abstracts of [Banks–Shparlinski](https://arxiv.org/abs/2610.19597),
[Klurman–Shparlinski–Teräväinen](https://arxiv.org/abs/2609.25393), and
[Shparlinski 2017](https://arxiv.org/abs/1705.06087): descriptions agree.
The historical Garaev–Karatsuba and Linnik inputs remain secondary-source citations here; neither is decisive for the verdict.

## Required fixes, in priority order

1. **MAJOR — restore the size hypothesis in every barrier/verdict/frontier restatement.**
   Write `q=q(X)∈4ℕ, q≤sqrt(X), prescribed independently of p`, with p averaged up to X (or in (X/2,X]).
   Omitting the bound is mathematically false, not merely unproved: let `P=∏_{3≤r≤X, r prime}r`, `q=2+2P`.
   Then q∈4ℕ is prescribed independently of the selected p, and for every odd p≤X,
   `x=y=q−1`, `κ=(q−2)/p` give `xy=1+κqp`. For every p∈(X/2,X], `κ<2q/X≪q/(log X)^(2+η)`.
   This also satisfies `p∤q(q−1)`. Keep the finite-q obstruction conditional on H; B1 is vacuous for fixed q eventually.
   For Cor B2's Type-II estimate, retain the explicit additional error
   `4 log X / sqrt((q−2)X) * Σ_{j|q/4} sqrt(j)` or state a range where it is o(1), e.g. q≤sqrt(X).
2. **MAJOR — replace full “ES” by “Type II” in the claimed exact union/equivalence.**
   A joint-in-q Type-II existence theorem would suffice for ES, but is not proved equivalent to it.
   Preserve `ES(p) ⇔ Type I(p) OR Type II(p)` and do not infer necessity for all ES proofs from this lane.
3. **MODERATE — repair the conditional Poisson wording.**
   To infer infinitely many prime-restricted failures *while R>0*, assume unrestricted failures are negligible
   relative to `X^(1−c+o(1))`, or assume eventual R>0, or formulate a joint zero law. The marginal law alone is insufficient.
4. **MINOR — define κ for q≥4 outside 4ℕ in B(b), or restrict its displayed domain.**

After these repairs, ACCEPT the dictionary, constructions, scoped counting barrier, conditional closure result,
and finite census; retain **narrowed**, not **dead**, and no claim of progress toward solving ES.
