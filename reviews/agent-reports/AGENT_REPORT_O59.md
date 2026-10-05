# AGENT REPORT O59 — H_LS∞ for forced families via sparsity (checkpoint 1)

Branch `side-agent/hls-sparse`. Document: `EXCEPTIONAL_LARGESIEVE3.md`.
Script: `scripts/largesieve3_checks.py` (EVIDENCE only; replay in the doc).

## Results

1. **Theorem 1.1 (smooth–rough splitting; PROVED, elementary).** For any
   threshold z, a large sieve (any rational frequencies, any weights) is
   capped by `β log N + log ρ + log E_{c∼π_s}𝓡_{2+2β}(π_c)`, where
   `π_s` is any measure on the z-smooth avoider set with density `≤ ρ`
   and `π_c` any measure on the z-rough fibre `𝒜_c`. The z-smooth
   coordinates need **no Fourier or level information** — Hausdorff–Young
   in the smooth coordinate turns them into a pure density cost (the
   mechanism of LS Thm 4.1's base, applied to an arbitrary correlated
   base). A level-split variant (Rem 1.1(c)) is LS2 Prop 5.2 with the
   smooth coordinates removed from both hypotheses.
2. **Lemma 2.1 (PROVED; K2 §§2–4 inputs, Case A via ElT Prop 1.4).** The
   z-smooth part has a measure with `log ρ ≤ 16𝔐(z) + O(1)`
   (`𝔐(z) ≪ (log z)³(log log z)³`): K2's sequential law conditioned on
   no leak, no coordinate with `p_ℓ > 1/2`, and bounded total mass.
   Affordable up to `z = exp((log N)^{1/4})`.
3. **Theorem 3.1 (PROVED, same inputs).** For every mixture in which each
   modulus has at most one prime factor `> exp((log N)^{1/4})` (any number
   of smaller primes, any modulus size, no B), **every** CRT-admissible
   large sieve — any rational frequencies, any denominators, any level —
   saves `≤ C(log N)^{3/4}(log log N)³`. This strictly extends LS Cor 4.2
   (ET Cor 3.4 slices) and closes (E1) for all frequencies whose
   high level comes from primes `≤ exp((log N)^{1/4})`.
4. **§4: the exact residual.** H_LS∞ for forced families ⇔ (H_rough): a
   correlation-decay statement for the fibre measures at primes
   `> exp((log N)^{1/4})`, needed only for classes with **≥ 2** such
   primes. Lemma 4.1 (two-copy form, PROVED): it suffices to have product
   decay of the two-copy correlations `P_S = E_{σ⊗σ}Π_{ℓ∈S}h_ℓ` and of the
   sup `s_S`. Lemma 4.2 (PROVED): the symmetric LLL/Kotecký–Preiss route
   fails for forced families because of **residue concentration** — the
   class `−4 mod M` lies in ℛ(M) for every `M ≡ 3 (4)`, so the
   conditional mass at residue −4 mod p is `≍ (log N)^{3/4}`, not small,
   although the average mass is `p^{−1+o(1)}`. Any proof must use the
   top-prime (sequential) order or average over residues. §4.3
   (Assessment): every one-step operator bound we tried (Young,
   Riesz–Thorin, global Hausdorff–Young) loses; the π-average must stay
   inside the `ℓ^{p'}` norm.

## Not achieved

* (H_rough) for classes with two or more primes above `exp((log N)^{1/4})`
  — the general forced-family H_LS∞ stays a CONJECTURE. No escape for an
  actual forced family was found; the band-family escape (LS2 Thm 8.5)
  needs dense bundles that forced families do not have, and in rough
  fibres the remaining obstacle is correlation decay, not density.
* Composite Gallagher kernels: Thm 1.1's density idea does not touch the
  factor `1 + Nh/(W_K−h)` (it reproduces LS2 Thm 9.1's shape); nothing new.

## Suggested ledger entry (for the parent)

(D)27 candidate: "Large sieve over mixtures: small primes cost only density
(LS3 Thm 1.1, Lemma 2.1); rough-slice mixtures (≤ 1 prime above
`exp((log N)^{1/4})` per modulus) capped at `C(log N)^{3/4}(log log N)³`
for every large sieve (Thm 3.1). PROVED (internal, unreviewed). H_LS∞
reduced to (H_rough) for classes with ≥ 2 rough primes; symmetric cluster
expansion obstructed by residue concentration (Lemma 4.2)."

Points for a hostile reviewer: Theorem 1.1's HY step with a non-uniform
base (density factor exactly ρ, via `(p−1)p'/p = 1`); Lemma 2.1's use of
(Q2)/(Q3) (K2's caps are `ℓ^{−1/2}`; heavy coordinates are allowed on the
good event as long as `y_ℓ ∉ F_ℓ` and `p_ℓ ≤ 1/2`); Theorem 3.1's claim
that the rough-slice activated sets are K2's `p_ℓ` for `ℓ > z` (all
cofactors z-smooth); the partial-summation bound for `J`.
