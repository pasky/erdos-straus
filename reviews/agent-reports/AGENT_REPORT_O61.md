# AGENT REPORT O61 (branch side-agent/third-conditional) — checkpoint 2 (R61 repairs applied)

Deliverable: `POINTWISE_OMEGA16.md` (§§0–7, Replay), scripts `scripts/omega16_{buchstab,esleast,adversary}.py`,
data `data/omega16/`.

## Main results
1. **Hypothesis LS(C)** ("Linnik's theorem for sifted sets"): every unit-class sieve system with moduli
   `≤T` and avoider density `δ>0` contains a prime `p>T` with `log p≤C(log T+log(1/δ))`. Reduces to
   Linnik for one class; log-scale random-set model.
2. **Thm 1.2 (PROVED implication, modulo NT via O13 Thm 3.4):** LS ⇒ `W(p)≥exp(c(log p)^{1/3}(log log p)^{−5/3})`
   for infinitely many Mordell-hard p. Short proof: O13's density bound + LS for one system per T.
3. **Item (i):** Haar-centred BV/EH/progression-GEH/GRH inputs for moduli `≤x` (full GRH with moduli `>x` not covered, R61 M1) through linear certificates cap at 1/4 (Prop 3.1,
   zero-error planted fake). Main-term forms of "primes in sifted sets" are too strong: AS false in the integer
   analogue (Buchstab), PS/AS heuristically false for primes by a compounding `(e^γω(u))^κ` deficit (Prop 2.1;
   numerics to 1e9 confirm compounding).
4. **Item (ii):** Hardy–Littlewood for CRT-product sets gives exactly `W=(log p)^{2±o(1)}`: every product
   subset of the ES avoider set has `log(1/δ)≍T^{1/2±o(1)}` (Prop 4.1; lower bound modulo
   Barban–Davenport–Halberstam, via the two-prime atoms `(ℓ_1ℓ_2,q)`). Extends POINTWISE_OMEGA Prop 6.1.
5. **Item (iii):** Cramér form CR(A) ⇒ LS ⇒ 1/3; the literal "any set of density δ mod Q" form is false.
6. **No uniform upper companion (§5.4, PROVED):** "`π_𝓔(x)≤xδ^{1/C}T^C`" for all systems is false (tailor a
   system to one prime `p_0∈(T,2T]`); for the ES family it would imply ES with `W≤exp(C(log p loglog p)^{1/3})`,
   so exactness of 1/3 needs a family-specific (ES-strength) hypothesis.
7. **Consistency:** LS not refuted by fakes (they are reweightings of Haar onto the complement), provably
   not reachable by linear certificates; robust to Siegel zeros and Jacobsthal effects; matches SIZE.

## EVIDENCE
* N1: Buchstab compounding for primes (κ=1,2,3, x≤1e9).
* N2: least hard prime with W>T: LS ratio 0.64–1.29 for T≤4095; the least hard p with W>4095 is
  133050918961 (W=5935, independently recomputed), ≈5× the Cramér/RA estimate. Scan of
  [1e11,2.382e11) stopped by hand: no hard p with W>8191 there; R61 confirmed 133050918961 is the least for 4095.
* N3: greedy adversarial κ-dimensional systems (z≤1000, κ≤8): LS ratio ≤1.15, adversary gains only
  ≈z^{0.85–0.9} over the random model, no visible growth in κ on this finite censored grid (3/69 unresolved).

## Self-review
Deep reviewer subagent (R-self): no FATAL; 5 MAJOR repaired — PS_log made non-vacuous (`c_0δ^C`, empty
system), Prop 3.1 restricted to Haar-centred error bounds with per-q coprimality (fake off by ≤ω(q)≤2log x;
GEH only via its progression part), Prop 2.1(b) assumptions (admissible growing shifts on `ℓ∈(y,z]`,
uniform compounding beyond fixed-tuple HL), upper companion replaced by the §5.4 falsity remark, Linnik
constants (no "C≥5/2 necessary"). Minors: BDH over units, esleast LO bound, evidence wording.

## R61 repairs (parent review `reviews/pointwise-omega16-review.md`, no FATAL)
* M1: Prop 3.1 covers GRH only truncated to moduli `≤x`; full GRH (characters of modulus `>x`, e.g. mod
  `lcm(M≤T)`) is explicitly *not* covered (open: ν's Fourier coefficients there). Fixed in §0, §3, §5.1, §7, report.
* m1: Thm 1.2 cites the realisation `(Q,r)` from the *proof* of O13 Thm 3.4, range `T≥e^{33}`.
* m2: §1 Remark (b) replaced (shifted Jacobsthal / greedy adversary gains `≈T`, absorbed by `C log T`).
* m3: N1 shift 6 = class 0 mod 3, non-unit, dropped (as already done in δ).
* m4: new §5.6 with credit to R61: (a) uniform random-points model + union bound over `≤2^{T²}` systems ⇒
  CR(2+o(1)) for all systems at once (Assessment); (b) LS PROVED by Brun–Titchmarsh for total mass `≤(1−ε)/2`.
* m5: Prop 4.1(b) relabelled PROVED (ineffective, BDH/Siegel–Walfisz); robustness to extra conditions at primes `>T`.
* m6: Thm 1.2 Remark (b) "up to log factors (exact under HAAR Conj 3.1)".

## Suggested ledger entry (DISCOVERIES.md (H)29)
29. **Which hypothesis gives 1/3 (POINTWISE_OMEGA16.md).**
    * Hypothesis LS(C) ("Linnik for sifted sets"): every finite system of unit-class events with moduli `≤T`
      and avoider density `δ>0` has an avoiding prime `p>T` with `log p≤C(log T+log(1/δ))` (Linnik's theorem
      for one class). Thm 1.2 (PROVED implication, modulo NT via the realisation in the proof of O13 Thm 3.4):
      LS ⇒ `W(p)≥exp(c(log p)^{1/3}(log log p)^{−5/3})` i.o. for Mordell-hard p; LS needed for one system per T.
    * Brief items: (i) Haar-centred BV/EH/progression-GEH/GRH input for moduli `≤x` through linear certificates
      caps at 1/4 (Prop 3.1, PROVED with O14 Thm 4.5's inputs; full GRH not covered); main-term "primes in
      sifted sets" forms are too strong (integer AS false, PROVED; primes: compounding Buchstab deficit
      `(e^γω(u))^κ`, Assessment + EVIDENCE to 1e9). (ii) LS for CRT-product sets ("HL_prod") gives exactly
      `W=(log p)^{2±o(1)}`: product subsets of the avoider set have `log(1/δ)≍T^{1/2±o(1)}` (Prop 4.1, PROVED,
      lower bound ineffective via BDH). (iii) Cramér form `log p≤log(1/δ)+A log T` ⇒ LS ⇒ 1/3; the literal
      "any set of density δ mod Q" form is false.
    * Uniform upper companions ("`π_𝓔(x)≤xδ^{1/C}T^C`" for all systems) are false (PROVED, a system tailored
      to one prime); for `𝓔_T` they would imply ES, so exactness of 1/3 needs an ES-strength hypothesis.
    * LS: CONJECTURE (Assessment: plausible). PROVED for light systems (mass `≤(1−ε)/2`, Brun–Titchmarsh; R61);
      a uniform random-points model predicts CR(2+o(1)) for all systems at once (R61). Not reachable by linear
      certificates (Prop 3.1). EVIDENCE: on the ES family `log p_min/(𝓛+log(1/δ*))∈[0.64,1.29]` for `T≤4095`
      (least hard p with `W>4095`: 133050918961, `W=5935`, confirmed by R61); greedy adversarial systems
      (two independent adversaries) stay at ratio ≤1.32, gaining `≈T` over `log p/δ`, no growth in dimension.
    * Review: `reviews/pointwise-omega16-review.md` (R61: no FATAL; M1 (GRH scope) and m1–m6 repaired).

## Points for the reviewer
* Prop 4.1(b): the BDH application (π-form on `(x/2,x]`, moduli `4q`), and the CRT-product avoidance criterion.
* Prop 3.1: scope = O15 Def 2.1 linear certificates; the fake matches all level-`≤x` statistics exactly.
* Prop 2.1(b) is an Assessment (HL heuristic), not a theorem.
* Novelty: none claimed for LS as a heuristic principle; the ES-specific content is Thm 1.2, Prop 3.1,
  Prop 4.1.
