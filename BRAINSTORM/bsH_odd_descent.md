# bsH_odd_descent — O177 sparks 1/3: odd-degree subfields of ℚ(ζ_M)⁺ and norm descent of −1 (O181)

**ES is not solved here.** Deep version: DRINFELD_ES.md §4. Script `scripts/bsH_descent.py`.

## Idea
LDP_DEEP A.4.2 blamed N(−1) = (−1)^r = +1 for r = φ(M)/2 even. Take F' ⊂ ℚ(ζ_M)⁺ of odd degree (N(−1) = −1) or
any odd-degree field and descend F'-certificates / F'-parities to ℤ.
## Literature
Neukirch, *Algebraic Number Theory*, VI (functoriality of the Artin map); LDP_DEEP A.4; reviews/ldp-deep-review.md
(D4a: F-Gram construction needs positive definiteness).
## Statement (PROVED)
Prop 4.1: parity over F' (quadratic K'/F' inside ℚ(ζ_M)) sees f only as "f ∈ H ∖ H'", which equals "f ≡ −1" iff
F' = ℚ(ζ_M)⁺ (even degree). Prop 4.2: norms of an odd-degree O_F-certificate give (if N(β), N(β') > 0; R181 repair D8) a Type II
certificate for n' = p·R_r(p), R_r = ((1+4c²dp)^r − 1)/(4c²dp); ES(n') ⇐ ES(p), not conversely.
## Barrier screen
B2/Prop 10.3: the visible information is a coset (genus-type). B6-like: certificates for a different n.
## Cheap numerics (EVIDENCE)
All 222 (odd-degree F', quadratic K') pairs for 4 | M, 8 ≤ M ≤ 120: none has H ∖ H' = {−1} (R181 repair D7: formerly
"All 81" — `bsH_descent.py` saw only ≤ 2-generated subgroups; complete count by `scripts/review_dr_descent.py`). Identity of Prop 4.2 on 1000
random samples.
## Assessment
Closed with proof. Promise 0.
