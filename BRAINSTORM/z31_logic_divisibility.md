# z31 — Logic: Presburger + divisibility (Lipshitz), decidability, Hilbert's 10th, o-minimality (O261 field memo 7)

Labels as in DISCOVERIES.md. Read by me: Lipshitz's local-to-global principle as stated by Défossez–Haase–Mansutti–Pérez,
arXiv:2308.13609 pp. 2–3 (`sources/lit2026g/lipshitz_lgp_via_dhmp.txt`). LOW 2015 abstract (agent E, `low2015.txt`).
Builds on BRAINSTORM/logic_divisibility_lgp.md (O141(d): the Type II system Φ_p is not in increasing form; its LGP fails at
odd squares) and logic_ominimal.md.

## (a) Counterpart
* **Lipshitz 1978 (Trans. AMS 235) / Bel'tyukov:** the existential theory of (ℤ, +, |, ≤) is decidable. Mechanism (DHMP p. 3):
  reduce to an equi-satisfiable system in *increasing form* — "the largest variable with respect to that ordering occurring in
  any non-trivial divisibility f | g implied by Ψ only appears in the right-hand side g" — and for such systems "Φ … has a
  solution over ℤ if and only if Φ has a solution in the p-adic integers ℤ_p for every prime p belonging to a finite set of
  difficult primes P⁺(Φ)" (local-to-global principle), glued by a generalised CRT. LOW 2015: small-model property, NEXPTIME.
* **B2 as a sentence.** E2 at a fixed p is the 2-variable existential (+, |, ≤) formula
  Φ_p(d, w): 1 ≤ d ∧ 1 ≤ w < p + 4d ∧ w | p + 4d ∧ 4d | w + 1.
  ES-for-all-primes in the E2 form is a Π₂-type sentence of (ℕ, +, |) (primality is Π₁ in |).

## (b) Status
Each Φ_p is trivially decidable (finite search: d ≤ (p + 3)/8 since 4d − 1 ≤ w ≤ (p + 4d)/3). The Π₂ sentence is false
(193). Whether the ∀∃ theory of (ℕ, +, |) is decidable: not verified by me or agent E (no claim).

## (c) What the logic view says about B2 (PROVED, elementary)
**Lemma 7.1 (E2 is a non-increasing system whose LGP fails).** (i) Φ_p is not in increasing form for any ordering: w | p + 4d
forces d ≻ w (the maximal variable must sit only on the right), and 4d | w + 1 forces w ≻ d. (ii) the divisibility part of Φ_p is
solvable in ℤ_ℓ for every prime ℓ (inequalities have no ℓ-adic meaning) and its order part is solvable over ℝ; yet Φ_p has no solution in ℤ for p = 193, 2521, 66529.
*Proof.* (i) as stated. (ii) Take d = 1, w = 3 in ℤ_ℓ: for ℓ ≠ 3, w is a unit so w | p + 4; 4 | 4 = w + 1 in every ℤ_ℓ. For ℓ = 3
take d = 1, w = 7 (7 | p + 4 in ℤ₃, 4 | 8). Order constraints: d = 1, w = 3 < p + 4. Global failure: exhaustive search
(`scripts/o261/e2_check.py`, which repeats B1_LINE's census for these three primes: None for 193, 2521, 66529; hits (1, 3) at
197, (2, 31) at 1201). ∎
*Reading.* The tied modulus (F3) is, in logic, the *cycle* d → w → d in the syntactic divisibility dependency graph, which
already rules out increasing form (the definition quantifies over all *implied* divisibilities, so acyclicity of the given
constraints is necessary, not sufficient — R-O261 minor); Lipshitz's procedure eliminates such cycles only by case-splitting one variable over a bounded
range — the finite B2 search itself. O141(d) made the same point for the full Type II system with the odd-square failures (T1);
Lemma 7.1 shows it for the 2-variable b = 1 line, where the failures are primes (no square class), so F4 is respected: LGP
failure here is not a local/character phenomenon at all.

**Hilbert's 10th / undecidability:** irrelevant to B2 (single p: bounded, decidable). **o-minimality** (logic_ominimal.md):
counting definable points (Pila–Wilkie) gives upper bounds only; it is "idle" for existence (STRONG_APPROX_ES, relative to Pila).

## (d) Verdict: ANALOGUE / exact reformulation (B2 = solvability of a cyclic, non-increasing linear divisibility system).
The known pointwise mechanism (Lipshitz LGP) applies only to increasing-form systems, which Φ_p is not. **NOT SHARP** (but Lemma 7.1 is a clean
logic-side statement of F3 that could be quoted).
