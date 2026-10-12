# R161 — hostile review of FUNCTIONFIELD_ES.md (O161, branch side-agent/ff-landscape)

Reviewer: R161. Document reviewed: `FUNCTIONFIELD_ES.md` as merged from `side-agent/ff-landscape`.
From-scratch scripts: `scripts/review_ffl_*.py` (own F_q[T] arithmetic, no reuse of `ffl_*.c` / `ffl_*.py`).
Status: IN PROGRESS.

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### C1. Definition 1.1 and Lemma 1.2 (NC and monicity) — SOUND-AFTER-REPAIRS (minor)

Re-derived. Expansion at ∞: the sum of the m minimal-degree terms has leading coefficient m·1. If m ≢ 0 (mod p)
then d₁ = n − k and m ≡ 1 (mod p). This gives (i), (ii) (char ≥ 5 ⇒ m = 1) and (iv) (char 2, NC ⇒ m ∈ {1,3}).
Exhaustive small check (`scripts/review_ffl_lemma12.py`, log `data/review_ffl_lemma12_log.txt`; all monic triples
of degree ≤ 4 (q = 2), ≤ 3 (q = 3), ≤ 2 (q = 4, 5, 7)): every genuine A/P solution found has NC and m = 1.

**Definition.** Monic denominators + NC are a reasonable image of x_i > 0 and x_i > n/4. Over Z, positivity and
the bound are equivalent; here "monic" is a convention (Hayes sign), and NC is a separate condition. This is a
modelling choice and should be labelled as such (Assessment), not called "the faithful form" without argument.
Other choices give different problems: arbitrary leading coefficients with NC, or "monic" relative to another
sign function. The document does not discuss them. (MINOR, D3.)

Defects:
* **D1 (MINOR, false claim, harmless direction) — Lemma 1.2(iii).** "char 3: m = 3 (cancellation, d₁ < n − k)
  is possible for monic solutions" is **false for irreducible P**, the only case considered. Proof: P is prime and
  appears in the reduced denominator, so it divides some denominator. That denominator has degree ≥ n > n − k, so
  d₁ < n − k forces m ≤ 2. In char 3, m ∈ {1, 2} is nonzero mod 3, so d₁ = n − k. Hence **NC is automatic for
  monic solutions in every odd characteristic**, so the lemma's own title is right and (iii) is wrong. The same
  argument also shows that m = 3 cancellation is impossible in char 2. Only m = 2 remains there, and it does
  occur. An explicit example, verified by hand and by computer:
  q = 2, A = T, P = A(T²+T) + 1 = T³ + T² + 1 (irreducible),
  `T/P = 1/T + 1/(T+1) + 1/(P(T²+T))`, degrees 1, 1, 5 with n − k = 2.
  *Repair:* (iii) should say: "char 3: for irreducible P, NC is automatic (P divides some denominator, so
  m = 3 with d₁ < n − k is impossible)". In char 2, cancellation means m = 2 exactly. Also change "In char 2 and 3
  we take NC as part of the definition" to "in char 2". In line 34, "only realised in char 2 and 3" should be
  "only in char 2".
* **D2 (MINOR) — line 36** promises that "the monic-only variant M" is studied "separately (§6)". §6 never
  mentions it. Either remove the promise or add the variant. (By D1, M = ES in odd characteristic, so only char 2
  is relevant.)
* **D3 (MINOR) — "faithful form".** Label the choice of definition as Assessment and add one sentence on
  alternatives (see above).

