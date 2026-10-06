# Hostile review R60 of CEILINGS_UNIFIED.md (branch side-agent/unify-ceilings)

Reviewer branch: side-agent/review-unify. Status: IN PROGRESS.

## Verdict summary (filled in per claim)

## Defects

### Claim 1 — Prop 1.1 (`log(1/δ*(T)) ≫ 𝓛³`): **SOUND** (given the note)

Re-derived line by line against `paper/es-threequarter-note.tex`:
* Atoms are POINTWISE_HAAR events. For `A=(k,ℓ,u,v)`, `M=kℓ≡3 (4)`, `A_M=uvw`;
  since `4A_M≡1 (M)`, `v^{-1}≡4uw`, so `−uv^{-1}≡−4u²w (M)` with `D=u²w | A_M²`.
  Hence every atom is an event `E_{M,D}` with `M=kℓ≤KX≤X^{1+κ}=T`. ✔ (checked
  numerically from scratch: `scripts/review_unify_atoms.py`).
* Unit Haar: `ℓ>X^{1/2}>K`, so `ℓ∤L_K`; `n mod ℓ` (uniform on `(ℤ/ℓ)^×`) is
  independent of `c=n mod L_K` and across `ℓ`. Atom residue `−uv^{-1}` is a unit
  mod `ℓ` (`uv<z_j²<ℓ`). Activation depends only on `c` (`k|L_K`). Note Lemma 2.2
  gives distinct projections at fixed `ℓ`. So the exact product
  `∏(1−f_c(ℓ)/(ℓ−1)) ≤ e^{−μ_c}` holds. ✔
* Note Cor 4.3 is stated "uniformly in all `c`" (not only reduced), with
  `μ_c ≥ a_h t² h(J_c)`; for unit `c`, `J_c=K(K)` and Lemma 3.2 gives
  `h ≍ log K ≍ κt`. ✔ Constants depend only on `κ` (fixed, e.g. 1/480) and `D`.
* Normalisation `n≡1 (24)`: `9∈K(K)` so `3|L_K`; `L_K` odd so `n mod 8` independent;
  conditioning keeps `c` a unit. Factor `φ(24)=8` trivial. ✔

Minor point only: D1 below (label of the two-sided sandwich).
