# z31 — Analytic NT: single-n problems with constant/polylog expected counts (least witnesses, 2^k + p, covering systems, Linnik–Gallagher) (O261 field memo 10)

Labels as in DISCOVERIES.md. Read (agent D, verbatim): Heath-Brown–Puchta Thm 1 (`hbp_powers2.txt`); Erdős's 2^k + p covering
statement via a secondary source (`erdos_2kp.txt`). Least-witness bounds: (memory), as in POINTWISE_OMEGA §8 and
LITERATURE_2026. This memo answers the brief's question "which mechanisms prove a POINTWISE existence statement with only
polylog many expected solutions?" across analytic NT.

## (a) Counterparts (expected count per target in brackets)
1. **Least quadratic non-residue / least primitive root / Linnik's least prime in AP** [≍ polylog in a window of polylog
   length]: n(p) ≪ p^{1/(4√e)+ε} (Burgess), ≪ log² p under GRH (Ankeny; Bach 2 log² p); g(p) ≪ log⁶ p under GRH (Shoup);
   least prime ≡ a (mod q) ≪ q^5 (Xylouris). All (memory).
2. **n = 2^k + p** [≍ Σ_k 1/log n ≍ constant]: Romanoff: positive density; Erdős 1950: an arithmetic progression of odd n with
   no representation, by covering congruences ("Using covering congruences I proved that there is an arithmetic progression
   of odd numbers no term of which is of the form 2^k+p", secondary). Sierpiński numbers (78557·2^n + 1 always composite) —
   same mechanism.
3. **Linnik–Gallagher: even n = p₁ + p₂ + 2^{k₁} + … + 2^{k_K}**: Heath-Brown–Puchta Thm 1: "Every sufficiently large even
   integer is a sum of two primes and exactly 13 powers of 2" (pointwise). [count ≍ (n/log² n)·(log n)^{K}·(…) — power.]

## (b) Mechanisms and the pattern
* (1) is pointwise with polylog counts **only under GRH**, and the event is a *character value at a fixed modulus* (χ_p(n) = −1,
  χ of order ℓ, χ mod q): detectable by Dirichlet L-functions, whose zeros control every short window. Unconditionally only
  power windows (Burgess, Linnik).
* (2) shows the converse phenomenon: a constant expected count, **no single-prime local obstruction**, and yet infinitely many
  failures, forced by a finite set of moduli acting on the periodic orbit k ↦ 2^k mod m (covering system).
* (3) is pointwise because the count has a power main term (Goldbach part), with the polylog part (powers of 2) riding on it.

## (c) Relation to B2
* **Least-witness problems: closest ANALOGUE in size, blocked by F3.** B2's events are not character values at a fixed modulus:
  the modulus 4C (E1) / 4d (E2) moves with the solution. GRH controls every fixed-modulus character sum, and the campaign
  PROVED that GRH alone does not reach a polylog cap by the window route ((J)85/(J)91: GRH + EQ gives (log₂p)^{13/2}, GRH + S
  gives (log₂p)^{9/2}, GRH alone does not reach (log₂p)^{O(1)}), and ES itself is not known under GRH. The ES sign layer
  *is* a least-witness event (the QNR of z31_complexity), which is why it is the easy layer (F6).
* **2^k + p / covering: ANALOGUE on the failure side.** It shows "polylog count + no local obstruction ⇏ existence" whenever the
  parameter runs through a *periodic* orbit mod fixed primes (then finite congruence data can cover all parameters). For ES the
  parameters (C, divisor) are not periodic orbits of a fixed map, and a congruence can never forbid a divisor in a class
  except via a character: the only finite-modular obstruction is T1 (squares, a character obstruction), which is void at
  primes (F4). The campaign's sterility results ((J)26, (J)54, (J)70) are the ES analogue of covering systems *for coverings
  of ES itself* (no finite ET covering), not for ES-failures. Assessment: this supports "ES failures, if any, are not
  covering-type", but proves nothing.
* **Heath-Brown–Puchta: blocked by F2** (needs a power-size main term to absorb the polylog factor).
**Answer to the brief's priority question (Assessment):** across analytic NT, every pointwise theorem with ≤ polylog expected
count that I (and agent D) could find is a fixed-modulus character event, and it is conditional on GRH. No unconditional or
conditional pointwise theorem with polylog count and a tied modulus was found (agent D item 10: none).

## (d) Verdict: least witnesses — ANALOGUE (F3 blocks); 2^k + p / Sierpiński — ANALOGUE (failure mechanism unavailable to ES
at primes); HBP — ANALOGUE (F2). **NOT SHARP.**
