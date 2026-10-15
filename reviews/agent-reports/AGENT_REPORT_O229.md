# AGENT_REPORT_O229 — bounded cap with a growing mute set, PM-II, SQ_± (wave Z-e)

Branch `side-agent/cap-growing`. Deliverables: `CAP_GROWING.md` (deep file), memos `BRAINSTORM/z5_*.md` (5, indexed in
BRAINSTORM/README.md), scripts `scripts/z5_*.py`. **ES is not solved; no infinite case of ES is claimed.**

## SHARP:
1. **The exponent cap is a sieve-dimension knob (CAP_GROWING Prop 1.3, Thm 1.4; PROVED relative to Bombieri–Vinogradov
   + Montgomery's large sieve).** The Type II certificate cube extends to the rational point (c, d) = (c₀R², d₀/R²)
   ("overflow cube"): for prime ℓ = 4c₀d₀j − 1, rad R | c₀ ∥-wise in K, p ≡ −4c₀²d₀R² (mod ℓ) gives an exact solution
   with den z = R², rad R | y. Hence ES^{(y,e)} (cap e, free mute set = R200 M1's regime) fails for
   ≪ N exp(−c_e (log N)^{(e+2)/(e+3)}) primes: e = 0 is Vaughan's 2/3, every e ≥ 1 beats it (3/4, 4/5, …) ((R230 repair D1): within the prime-modulus large sieve; ES's own record is 3/4, so only e ≥ 2 exceeds it).
2. **Prime-modulus SQ_±: χ = (n/ℓ) — a free genus filter (Lemma 3.1, PROVED) — and CONJECTURE PM-SQ_±** (every non-square
   n ≡ 1 (8) has a word with A = ±prime and χ = −1): 0 exceptions to 10⁶, robust against residue stacking to ≈10¹³
   (contrast PM-II's 3361). Calibration: its class mass is only ≍ log X, so the prime-modulus large sieve gives the "easier" signed twin a
   weaker exponent (1/2 < 2/3) ((R230 repair D6): a statement about the method, not a hardness proof).

## Results by goal
* Goal 1 (R200 M1). Pointwise: OPEN; every construction (fixed-field x-orbits, Pell unit of ℚ(√n), polynomial
  families, Pell-orbit (e+1)-freeness) reduces to the known class-group-across-fields layer + a Wieferich-type layer
  (CAP_GROWING §4, memos z5_fixed_field_orbits, z5_pell_unit_T1 — negative, with small PROVED lemmas). On average:
  Thm 1.2 (shots, (e+1)/(e+2)) and Thm 1.4 (overflow cube, (e+2)/(e+3)). Barrier hypothesis exploited: per-modulus
  class count (dimension), honestly within B6.
* Goal 2 (PM-II). Vaughan's classes are prime-modulus Type II certificates (Lemma 2.1) ⇒ PM-II fails for
  ≪ N exp(−c (log N)^{2/3}) primes (Cor 2.2). Failures are ≡ 1 (mod 12) and QR mod 7; h = 3, 7 are the only covering
  moduli ≤ 2·10⁴ (CERTIFIED). The loglog note's gain does not transfer (composite moduli).
* Goal 3 (SQ_±). Prop 3.2: exponent 1/2 almost-all; power saving is beyond the large sieve for all three problems
  (ω(ℓ) = (log ℓ)^{O(1)}; Assessment). No pointwise strengthening: genus forcing via ψ_u(n + u) only covers non-residue
  classes (B1).

## Checks run
z5_cap_classes.py 2e6 (class mass; 140 exact solutions), z5_cube_overflow.py (3 194 exact overflow-cube solutions,
Def 1.1 prime by prime), z5_sqpm_prime.py 1e6 (0 exceptions, 0 squares marked), z5_sqpm_verify.py (400 random n to 1e11,
independent search + exact identity), z5_sqpm_adversarial.py (Q = 13, 23, 31), z5_pm_cover.py 2e4.
Not done: odd-square T1 control for the overflow cube beyond the proof (classes −4c₀²d₀R² are QNRs mod ℓ ≡ 3 (4), so
squares are never hit — PROVED: (d₀/ℓ) = 1 for d₀ | ℓ + 1 by reciprocity, CAP_GROWING Thm 1.4 T1); a C rerun of PM-SQ_± to 10⁷; uniformity of c_e in e.

## Points for the hostile reviewer
* Thm 1.4's BV step (weights ∏(1−1/s)/φ, the extra non-divisibility ℓ ≢ −1 mod 4s²) and the injectivity of
  (c₀, d₀, R) ↦ c₀²d₀R² are where errors would hide; Thm 1.2's Lemma 1.1 is the template.
* Cor 2.2 relies on the description of Vaughan's classes in paper/vaughan-loglog-note.tex §1 (k = 1), not on a re-read of
  Vaughan 1970.

## Sparks (not pursued)
1. Overflow cube with *composite* multipliers kℓ (loglog-note trick) — should give (e+2)/(e+3) with a (log log)^{1/(e+3)} gain.
2. PM-SQ_± to 10⁷ in C; does the least |u| stay ≤ 10? Is there a Dickson-conditional "no finite u-set" theorem (shift
   slots n + u)?
3. Let e grow with N: track c_e to see whether e ≍ log log N already gives exp(−c log N/ log log N)-type savings.
4. Fixed-field orbits: compute ord(ε mod m_k) for small D₀ to make the "ring class group kills CL luck" heuristic precise.
