# R290 — hostile review of O279 FRONTIER.md

Reviewer: side-agent/review-frontier. Documents: FRONTIER.md (as merged from side-agent/frontier-doc), AGENT_REPORT_O279.md.
Status: IN PROGRESS.

## Summary verdicts
(to be filled)

## Defects
(to be filled)

## Task (2): the (★) main-term constants — RESOLVED (no inconsistency; FRONTIER's framing is wrong)

**Derivation (reviewer, from scratch).** Trial form: R(n) = Σ_{(u,C)∈𝓡} 1[m | n+u], m = 4uC − 1. Note gcd(m, u) = gcd(−1, u) = 1,
so −u is a *unit* mod m.
* For **arbitrary integers n**, the density of n with m | n+u is 1/m. Hence PARITY_AUDIT's M(p) = Σ_𝓡 1/m = (log p)²/8 + O(log p)
  is the zero-frequency Fourier term, i.e. the **average of R(n) over all integers n** of size p (correct as stated, as an identity
  R = M + E with E the non-zero frequencies).
* For **primes p**, the density of primes in the unit class −u mod m is 1/φ(m). The prime-adapted trial main term is
  M_φ(p) := Σ_𝓡 1/φ(4uC − 1). For fixed u, the mean of m/φ(m) over m ≡ −1 (mod 4u) is ∏_{ℓ∤2u}(1 + 1/(ℓ(ℓ−1))); summing
  Σ_u (1/(4u))·log(p/4u)·(that factor), the u-average of the local factor at each odd ℓ is
  (1 − 1/ℓ)(ℓ²−ℓ+1)/(ℓ(ℓ−1)) + 1/ℓ = 1 + 1/ℓ², so M_φ(p) ∼ (1/8)∏_{ℓ odd}(1 + ℓ⁻²) L² = (1/8)(12/π²)L² = **(3/(2π²))L²** —
  exactly BM_CORRECTED's M₀ constant, via a different parametrisation. So the two sources describe **different quantities**:
  1/8 = all-integer average (Σ1/m), 3/(2π²) = prime singular series (Σ1/φ(m) in trial form = Σ1/φ(4uB) in pair form).
  Ratio 12/π² ≈ 1.216.

**Numerics (from scratch, `scripts/review_r290_constants.py`, log `logs/review_r290_constants.log`; R validated against brute
force for all 3 ≤ n < 403).** Windows [N, N+2·10⁵), L = log(midpoint):

| N | L²/8 | M_int=Σ1/m | M_φ=Σ1/φ(m) | M₀ (pairs) | 3L²/(2π²) | mean R, all n | mean R, primes | mean R, p≡1(4) |
|---|---|---|---|---|---|---|---|---|
| 10⁶ | 24.19 | 23.65 (0.122L²) | 29.46 (0.152L²) | 28.93 (0.150L²) | 29.41 | 25.72 (0.133L²) | 31.91 (0.165L²) | 32.26 (0.167L²) |
| 10⁷ | 32.51 | 31.85 (0.122L²) | 39.53 (0.152L²) | 39.00 (0.150L²) | 39.53 | 34.24 (0.132L²) | 42.38 (0.163L²) | 42.71 (0.164L²) |

* mean R over all n ≈ M_int + 0.15L; mean R over primes ≈ M_φ + 0.20L (both offsets stable between 10⁶ and 10⁷, i.e. genuine
  O(L) secondary terms). Ratio prime/all = 1.254 → 1.247, drifting toward 12/π² = 1.216.
* So **for primes the right leading constant is 3/(2π²)** (BM_CORRECTED Thm 2.2 / Prop 2.3), and (log p)²/8 underestimates the
  prime mean by ≈ 22 % at leading order (≈ 25 % in range). PARITY_AUDIT's E(p) therefore has a systematic **positive** mean
  ≈ (3/(2π²) − 1/8)L² ≈ 0.027L² at primes (the Ramanujan-sum terms, since p is coprime to every m).
* PARITY_AUDIT's supporting remark "(M(p) reproduces … the observed R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰, where
  (log p)²/8 = 42.4, 53.7, 66.3)" is a coincidence of three single values (sd of R at that size ≈ 1.4·√(2M) ≈ 15): the prime mean
  at 10⁸ is ≈ 0.16·L² ≈ 55. FRONTIER §2.2 repeats these three values as if they supported the constant.
* Five-slice 45/(8π²) (BOARD2_SLATE Prop 3.4): a third, different quantity (ordered five-slice pairs u, v ≥ 2, three
  even sectors automatically active). Arithmetic re-checked: 9/(8π²) + 3·(3/(2π²)) = 45/(8π²); Burgess 45/(32π²) = ¼ of it;
  PV 15/(64π²) = 1/6 of the Burgess value. Consistent with (★)'s 3/(2π²) (ratio 3.75, explained in the source). Not
  recomputed numerically from scratch (source's own fit: mean M₀/L² = 0.450 at 10⁶ vs 0.570 asymptotic, slow k ≥ 3 sector) —
  the Assessment label is appropriate.

**Verdict.** No mathematical inconsistency in the repo's *theorems*; FRONTIER's sentence "These are different expansions; the repo
does not reconcile the constants … nothing below depends on the constant" and §7 item 16 should be replaced by the resolution
above. Additionally PARITY_AUDIT (not FRONTIER's responsibility, but cited by it) should get a note on Lemma 2.1's parenthetical
and on its E2 table row ("heuristic size (log p)²/8"): 1/8 is the all-integer density; the prime heuristic is 3/(2π²).
