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

* **D4 (MINOR) — Lemma 1.2(iv).** By the D1 argument, m = 3 is impossible for prime P (some denominator has
  degree ≥ n > n − k). So under NC, m = 1 in every characteristic. State this. It simplifies §1 and the engine
  description ("X = the unique denominator of degree n − k").

### C2. Lemma 1.3 (e-slice criterion, all characteristics) — SOUND (minor hypothesis to state)

Re-derived both directions independently.
(⇐) 1/X + (a+b)/(κPX) = (P+E)/(PX) = A/P. κ = (a+b)/E is monic. The NC case split (P ∤ a; P | a, P ∤ b;
P | a, b) is correct. The last case uses gcd(E, P) = 1, which holds because P is prime, P ∤ A, and P ∤ X
(since deg X < n).
(⇒) Write Y = g·y, Z = g·z with gcd(y, z) = 1 and all of them monic. Then yz | N := PX, and a := N/y, b := N/z,
κ = g give back (Y, Z). y + z ≠ 0 except in char 2 with y = z = 1, and that case forces E = 0.
Computational cross-check: the solver S2 (`scripts/review_ffl_solve.py`, built on this criterion) agrees with
the criterion-free brute force S1 (enumerate X, Y, solve for Z) on every irreducible P for
(q, A, n) ∈ {(5,T,2), (5,T,3), (7,T,2), (3,T²,3), (3,T²+1,3), (4,T²,3)}, with identical failure lists.
* **D5 (MINOR).** The lemma (and §1 notation) should state n ≥ k (needed for deg X = n − k ≥ 0) and that P is
  irreducible (used for gcd(E, P) = 1 and for P ∤ X). §1 says "P monic irreducible", but n > k is first
  stated only in Thm 5.3 / 6.4.

### C3. Proposition 1.4 — SOUND

(i), (ii) are direct identities, re-verified by hand and on random monic P in the right classes for
q ∈ {3, 4, 5, 7, 9} (`scripts/review_ffl_identities.py`, log `data/review_ffl_identities_log.txt`).
(iii) The residue bookkeeping is correct: F₂: P(0) = 1 = −1. F₃: {1, 2} = {−2, −1}. F₄: −2 = 0, so only
P(0) = 1 is free. F₅: {4, 3}.
(iv) The identity is correct. The splitting "2·1/(−2X₀P/r)" is for odd characteristic. In char 2 one can use
1/u = 1/(u+1) + 1/(u(u+1)) applied to u = X₀P/r. The document only says "e.g.", so this is acceptable.
* **D6 (MINOR).** Line 31 says "Without any sign condition the problem degenerates (§1.4)". Prop 1.4(iv) proves
  this only for k = 1. Say "for k = 1" or prove it for general k.

### C4. Theorem 6.1 (F₂, A = T²) — SOUND

Re-derived. P(0) = P(1) = 1. In the case P ≡ 1 + T (mod T²): R = (P+T+1)/T² is monic of degree n − 2 with
R(1) = 1, so (T+1) | R + 1. Then cP + R + 1 = c(P + T + 1) = cT²R gives the identity. The degrees n − 2,
2n − 3 ≥ n, 3n − 5 ≥ n hold for n ≥ 3. At n = 3, c = 1 and that is fine. The Type II datum (1, R, c, 1),
E = T + 1, is consistent with P = T²R − E. Machine check: the explicit (X, Y, Z) of the proof satisfies
A·XYZ = P(XY + YZ + ZX), is monic, and satisfies NC for **all 4717 irreducible P of degree 3..15** over F₂
(`scripts/review_ffl_identities.py`). No defects.

### C5. Proposition 4.1 (Type II sign law) and the §4 "no obstruction" conclusion — formula SOUND; conclusion GAP (overclaimed label)

**The formula.** I re-derived it. Ef = Aacd·E − E = Aad(a+b) − E = Aa²d + P. Since f ≡ −1 (mod a), we get
(a²/f) = 1. (−1/ℓ) = ((−1)^{(q−1)/2})^{deg ℓ}, since (q^m − 1)/(q − 1) ≡ m (mod 2) for odd q. Reciprocity for
monic coprime f, Ad gives (Ad/f) = (−1)^{((q−1)/2)·deg f·deg Ad}·(f/Ad), and f ≡ −1 (mod Ad). The exponents add
up to ((q−1)/2)((1+deg f)(1+deg Ad) − 1). Note deg f ≥ k ≥ 1 always holds, so the excluded case deg f = 0 never
occurs. Also P ∤ f, since P | f would force P | Aa²d.
Machine check, from scratch and reciprocity-free (Jacobi symbol by factoring f and Euler's criterion),
`scripts/review_ffl_sign.py`, log `data/review_ffl_sign_log.txt`: I enumerated all Type II data on irreducible P
for (q, A, n) = (3,T,4), (3,T,5), (3,T²,5), (3,T²+1,5), (5,T,4), (5,T²+1,4), (7,T,4), (9,T,3), (9,T+2,4),
(11,T,3). That is 11 558 data, 0 mismatches, and q ∈ {9, 11} were not in the author's check. The identity
Ef = P + Aa²d was asserted on every datum.

**The conclusion** (lines 124–136, "PROVED at the level of Type II classes … There is no obstruction class of
monic P in F_q[T] for any q"):
* **D7 (MAJOR, overclaimed label / ill-defined statement).**
  (a) "Obstruction class" is never defined, so "PROVED" has no precise content. What is actually proved is narrower:
  *the Mordell / ET Prop 1.6 mechanism does not transfer.* For q ≡ 1 (mod 4) every Type II datum imposes (P/f) = +1.
  Perfect squares M² satisfy this for every datum, so squares are not excluded from any Type II family. For
  q ≡ 3 (mod 4), squares are excluded exactly from the data with deg f or deg Ad odd.
  (b) **"for any q" includes even q.** In char 2, Prop 4.1 is meaningless: there is no Jacobi symbol (one would
  need the Artin–Schreier symbol), and nothing in §4 applies. The claim is unproved there.
  (c) The sketch "a P could be obstructed only if (P/f) = −1 for every monic f; the only candidates are P = uM²"
  quantifies over all monic f. The admissible f are only those of the form Aacd − 1, with (a, c, d) coupled to P
  through P = Aabd − E. The step from "for every admissible f" to "for every monic f" is not justified. It is
  also irrelevant to irreducible P, which are never of the form uM².
  (d) It reads as contradicting §6.3, which says char ≥ 5 *does* have an obstruction to finite coverings (the size
  class P ≡ 1). The intended meaning is "no *quadratic-residue* obstruction".
  *Repair:* Replace the conclusion with: "PROVED (q odd): the sign in Prop 4.1 is +1 for all Type II data if
  q ≡ 1 (mod 4), and for the data with deg f, deg Ad both even if q ≡ 3 (mod 4). Consequently squares are never
  excluded by the Type II sign condition, and the Mordell square-class argument against finite coverings has no
  analogue. Assessment: no quadratic obstruction is expected. Char 2: not addressed." Drop "for any q" and drop
  the "every monic f" sketch, or prove it for the admissible f.
* **D8 (MINOR).** "q ≡ 3 (mod 4): every class keeps the families with deg f and deg Ad both even". This is true as
  a statement about degrees, but for a *linear family* (Lemma 6.2) with type-2/3 terms, f depends on P and deg f
  moves with n. So the sign of a fixed family alternates with the parity of n. The sentence should say that the
  sign of a family is a function of (class mod W_F, parity of n). That is the precise sense in which "no
  congruence controls it".
* The bias data (i) were spot-checked against the author's failure list for q = 7, n = 6. The P(0) values are
  2, 1, 1, 1, as stated. The tilt numbers (ii) were not re-computed (EVIDENCE, low stakes).

