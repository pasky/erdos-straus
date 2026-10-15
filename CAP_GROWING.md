# CAP_GROWING — bounded cap with a growing mute set (R200 M1), PM-II and SQ_± on average (task O229, wave Z-e)

Status: in progress (O229). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP (Def 1.1, Prop 1.2, Prop 3.1), GROWING_MUTE, CAP_TWO, PHASE_DIAGRAM, MARKOFF_ES §6,
BRIDGE_WORLDS §5 (PM-II), SYNTHESIS_SPARKS4 §2 (SQ_±), paper/vaughan-loglog-note.tex. Scripts `scripts/z5_*`,
outputs `data/z5/`.

## 0. Iteration log

(Z1) Goal 1 head-on (pointwise ES^{(y,e)}, e bounded, S growing). Every reformulation I tried (symmetric
divisibility 2ABD | nA² + B² + D; "m | nq² + 4, m ≡ −n mod 4 rad q"; polynomial families at fixed n via Capelli;
Pell unit of ℚ(√n)) lands on the known two layers: (i) a fibre/class-group layer (MARKOFF_ES §6, CAP_TWO §6) and
(ii) an (e+1)-free layer on a binary recurrence (Wieferich-type). Barrier hypotheses violated: B3 (no archimedean
wall ⇒ infinite main term) and B2 (no fixed slice set) — but neither violation supplies existence. Pointwise: no proof.
(Z2) Steering: the hypothesis B6 ("averages over n say nothing pointwise") is the one a growing-S argument CAN use
honestly — on average over n the cap e is a *dimension* parameter. Modification: ask how the exceptional set of
ES^{(y,e)} shrinks with e. Result (§1): Vaughan's exponent 2/3 becomes (e+1)/(e+2) — the cap is a sieve-dimension
knob, interpolating between Vaughan (e = 1) and the pointwise theorem ES^{(y)} (e = ∞).
(Z3) PM-II: Vaughan's classes are prime-modulus Type II certificates, so PM-II inherits Vaughan's bound (§2).
(Z4) SQ_±: its prime-modulus classes number only ≍ τ(ℓ²−1) per ℓ, so the same machinery gives exponent 1/2 —
the "easier" signed twin is *provably harder on average* by this method (§3).
