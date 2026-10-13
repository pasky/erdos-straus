# AGENT_REPORT O183 — spark relay J: T1-bearing ES variants provable at primes (checkpoint 1)

Main file: `T1_TEMPLATE.md`. Memo: `BRAINSTORM/bsJ_mute_place_unit_orbit.md`. Scripts: `scripts/t1t_*`.
ES is not solved; no infinite case of ES over ℤ is claimed.

## SHARP:
1. **A T1-bearing ES variant whose solvability at every prime follows from GRH (Artin), with the T1 step explicit.**
   V_φ: 4/n = 1/x + 1/y + 1/z over ℤ[φ], all σ₁(·) > 0, σ₂-signs mixed. T1 at squares PROVED (Cor 2.2); V_φ(p) for
   every prime p ≠ 5 CONDITIONAL on GRH (Thm 3.1); EVIDENCE: all 78 496 primes < 10⁶ solved by an explicit formula
   (Prop 1.2), no odd square m² (m < 2000) solved by it.
2. **Exact dictionary (PROVED, Thm 1.3):** unit-Type-II solutions of V_φ(n) ⟺ some a_k = n + 4φ^{2k+1}, k ∈ ℤ, has a
   prime factor 𝔮 with (n/𝔮) = −1. Over ℤ (η = 1) this is the classical one-shot family "p + 4 has a prime factor
   ≡ 3 (mod 4)"; V_φ extends it along an *infinite unit orbit*. ES's lottery (finitely many shots) becomes an Artin
   problem (infinitely many shots, with a Chebotarev condition in K(√p) carrying the T1).
3. **Short uniform proof of all local invariants of the BL class on integral points over any number field
   (PROVED, Thm 2.1):** tame places 0; places above 2 give 0 for numerator 4 (two-line proof, any ramification:
   the all-units case gives an *unramified* extension); Type I/II shapes at even-exponent primes give 0; real
   places give ½ iff the three signs agree. Corollary: sign-pattern ES over K is T1-bearing iff the number of
   positivity-pinned real places is odd (and no real place is unpinned) — explains why totally positive ES over real
   quadratic fields is easy (other_rings Prop 3.3: two anchors cancel) and gives a **natural** T1-bearing variant
   with infinite units: plain positive ES over a field with ONE real place, e.g. ℤ[∛2] (EVIDENCE: all p < 3000 solved
   by the unit mechanism; squares not).

## What was done
* §0 (J2): over ℚ the anchor/partner swap (anchor 2 by congruence, partner ∞ by sign pattern) gives a T1 but the
  search stays finite and fails at many primes (complete enumeration) — B1–B3 hypotheses still met.
* §1: V_φ, Lemma 1.1 (Cl_{4∞₁} ≅ ℤ/2, character χ_{−φ}), Prop 1.2 (explicit solutions), Thm 1.3 (criterion; T1 for
  the mechanism). Full-T1 evidence: general search at 9, 49, 81, 121 (0 solutions Type I/II at all primes of n among
  1449), at primes plenty.
* §2: Thm 2.1 / Cor 2.2 (PROVED). Checked: all 1035 solutions in `t1t_phi_inv.py` have non-zero invariants only at
  σ₁ and primes of n (tame symbols computed directly).
* §3: Thm 3.1 (CONDITIONAL, GRH via Lenstra 1977; the positivity of Lenstra's density with our Frobenius
  conditions is my own check — please verify), barrier screen (B2 hypothesis "modulus part of the solution" fails
  for unit divisors; B3/B6: infinite search at fixed p; B5 respected).
* §4: one-real-place version, ℤ[∛2]; plan for an unconditional theorem.

## Caveats for the reviewer
* Thm 3.1 depends on Lenstra's theorem with Frobenius conditions; I did not re-read Lenstra's paper (no PDF in
  sources/); the entanglement check is an Assessment.
* The rank-≥4 unconditional route (§4) is a plan, not a result; the x^{3(r+1)/(4r)} count is my sketch.
* Thm 2.1(c) re-proves Bright–Loughran's 2-adic vanishing by a different route; worth an independent check
  (it is used for every K).
* §1's full-T1 table is now implied by Cor 2.2; the table is a consistency check of the code.

## Sparks (not pursued)
* S1: write Thm 1.3 for ℤ[∛2] (Cl_{4∞} is a 2-group > ℤ/2: sub-product condition) and for r₁ = 1 fields in general.
* S2: unconditional ES_K(p) for all p over a field with r₁ = 1 (or |P| odd + mute places) and unit rank ≥ 4,
  via Gupta–Murty/Harper–Murty with the extra congruence ℓ mod 4p — check whether their sieve accepts it.
* S3: TES (O182) has no real place, so its anchor is 2-adic and the unit group of ℤ[ω] is finite: the N = 103, 151
  window failures fit "finite orbit ⇒ lottery". Prediction: TES over a field with infinite units (e.g. ℚ(ζ₉) or
  ℚ(ω, √2)) behaves like V_φ (solvable at every prime, GRH-provably).
* S4: what is the ℤ-analogue of a "mute place"? Over ℤ[1/S] the place S is not mute (it adds an anchor or kills
  T1); a quantitative version would ask for a fixed-p family of rank ≥ 1 of "universal divisors" — over ℤ only
  congruence-forced divisors exist (B1). A precise no-go statement would close the template's transfer question.
