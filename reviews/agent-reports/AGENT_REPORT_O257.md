# AGENT REPORT O257 — spark relay on O253 SHARP 1+2: non-congruential lifts + numerator-model laboratory

Main file `NONCONG_LIFTS.md`; memos `BRAINSTORM/z28_{slice_vs_witness_level,espectrum_share,complete_levels,
matched_profile,size_information,lottery_margin}.md`; scripts `scripts/z28_*` (C solver `z28_lab.c`); logs `logs/z28_*`.
Branch merged `side-agent/amplify-exception` and later `main` (R266 attribution repair applied: O253 Thm 3.2 is the
classical Mordell–Schinzel / ET Prop 1.6 obstruction, campaign T1). **ES is not solved; no total law was found.**

## SHARP:
1. **Thm 2.6 (PROVED, elementary; numerically confirmed): a proved 4-vs-8 separation in the lift language.** Let 4 | k,
   ℓ ∤ k odd prime, x_{ℓ,2} ∈ Ẑ the point "2 at ℓ, 1 at every other prime (incl. 2)". For every k ≥ 8, x_{ℓ,2} lies in
   *no* Type I/II witness class; for k = 4 it is covered iff ℓ ∈ {3, 5}, exactly by Mordell's slices (1, 6, e = 7) and
   (1, 5, c = 2, e = 3) / (2, 5, e = 7). Consequence: no level divisible by a prime ℓ ≡ ±3 (8) is *complete* (= visibility
   suffices for transport) — for k ≥ 8 including ℓ = 3, 5; for ES for every such ℓ ≥ 11. The mechanism is an
   archimedean inequality b₀(k − 4/g) ≤ 3 on the slice (size of the numerator), not a reciprocity law. Check: slices
   a ≤ b ≤ 300, k ∈ {4, …, 32}, ℓ < 60 — hits exactly the four Mordell classes.
2. **Complete-level dictionary (CERTIFIED).** "Visibility is sufficient at level L" ⟺ L complete. k = 4: complete levels
   ≤ 1600 are 7-smooth, and a 7-smooth L is complete iff (3 | L ⟹ 8 | L) and (7 | L ⟹ 24 | L) (≤ 6000; "if" PROVED).
   k = 8, 12: no complete level ≤ 400k. Since every Mordell-class prime is a square modulo every 7-smooth level, **the
   only 4-specific resource of the lift picture (Mordell completeness) is exhausted exactly on 𝓜**.
3. **Level dichotomy (PROVED; T1 part classical).** A congruence-mediated lift valid on the class of p mod M forces
   kab | M and p ≢ □ (mod M). Slice-level M ⟹ O253 Cor 3.3; polynomial lifts collapse (Schinzel); the only escape is a
   level growing with the source's size d′ — and the natural such lifts (exact sharing of the factored number) transport
   only the e-spectrum (Prop 1.4: four share relations, validity ⟺ (θ, e) ∈ Spec(p)).

## What was done
* §1: Def 1.1 (slice-level / witness-level), Thm 1.2, Prop 1.3 (polynomial collapse; archimedean lifts → NEAR_SQUARE),
  Prop 1.4 (exact-share lifts = e-spectrum transport).
* §2 laboratory: exact E_k, 7 ≤ k ≤ 25, primes ≤ 10⁸ in 30 s (agrees with O194/O197 and PW Table 1 — known data);
  exception profiles (squares mod small levels, large lqnr); margin f_k/log³p (k = 4 ×2.2 over k = 8 in mean, min 23 vs 4);
  complete levels; adelic single-prime points; Thm 2.6.
* §3: Lemma 3.1 (matched profile ⟹ B-smooth witnesses visible); fixtures 97, 193, 313, 3361, 5209 and all 273 Mordell
  primes ≤ 10⁵: 0/1347 matched sources total, visibility sufficient at 0 sources, 30% of visible witnesses transport.
* §4: model screen at exceptions of k = 8, 12, 16 (matched soluble sources with many visible witnesses, none transports);
  size-information permutation test: source sizes carry no signal about p's divisor events (EVIDENCE).

## Honest scope
* Thm 1.2(ii) and Prop 1.3 are classical in substance (T1 / Schinzel); new is the slice/witness-level split.
* §2.4 "only if" direction and "no complete level ≤ 400k for k = 8, 12" are finite computations; Thm 2.6 covers only
  ℓ ≡ ±3 (8); for ℓ ≡ ±1 (8) (7, 17, 23, …) completeness through ℓ is open (EVIDENCE: scans show uncovered points).
* The model screen refutes only threshold-free laws (R207 D1 / R266 D-41).
* No total E-valued law; no positive ES statement.

## Sparks (not pursued)
* Extend Thm 2.6 to x_{ℓ,r}, r = least non-residue: Case A becomes L = ckas − (a + c)/b₀ with L | a + rc, which
  bounds L ≤ poly(r); with n(ℓ) < √ℓ + 1 this would prove "for k = 4 complete levels are exactly the 7-smooth ones
  of the rule" (full classification), and an analogous statement for every 4 | k.
* For k = 8: is there *any* complete level (supported on 2 and primes ≡ ±1 (8))? Thm 2.6 + one more point at ℓ = 7
  (scan: r ∈ {3, 5} uncovered) would give "k = 8 has no complete level", a clean structural reason for E_8 ≠ ∅-type
  behaviour of covering arguments.
* Witness-level lifts that are not exact-share (target number shares only the factor d′ with the source) — the size
  test says they are lotteries; a version with a reciprocity-forced factor (à la (J)64 windows) is untested.
* Numerator-size inequality as the 4-specific input: the inequality b₀(k − 4/g) ≤ 3 is where 4 differs from 8 — look for
  other ES arguments whose only 4-specific step is such a size inequality (e.g. the (J)57 Fano pigeonhole).

## R-rows
| Row | Content |
|---|---|
| Deliverable | NONCONG_LIFTS.md §1–§4; 6 memos; report. |
| Best result | Thm 2.6 (PROVED) + complete-level dictionary (CERTIFIED/PROVED parts). |
| Obstruction | Thm 1.2 / Prop 1.3 / Prop 1.4: non-congruential = witness-level = B2; exact sharing erases sizes. |
| Fixtures | 97, 193, 313, 3361, 5209: 0 total matched sources, 0 share transports (335 witnesses); Mordell ≤ 10⁵: 0/1347 total. |
| Odd-square control | T1 asserted at every level in z28_complete_levels.py (0 covered square classes); det ⟹ visible asserted at 20 365 transports. |
| Resources | one session; ≤ 2 cores except one 5-process burst of the Python adelic test (≈ 1 min, flagged); ≈ 1.5 CPU-h; logs < 30 kB. |
