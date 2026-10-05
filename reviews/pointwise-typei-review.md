# Hostile review R31 of POINTWISE_TYPEI.md (O31, branch side-agent/typei-ckmin)

Reviewer branch: side-agent/review-typei. Status: in progress.

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| L1.1 | SOUND |
| T6.1 | SOUND |
| §5 record ck_min(9033649)=883 | CONFIRMED (independent) |
| T2.1 | pending (proof read line-by-line: no defect found yet) |

## Notes per claim

### T2.1 (H-conditional)
Re-derived steps 1–5: A|P since ℓ^{E_ℓ}>A; a²+4ck²≡A (mod P) so f_{c,k}∈ℤ[t]; v_ℓ(N)=v_ℓ(A) for ℓ≤B (ℓ=r: N≡p²≢0, A≡1);
p≡1 (mod 4c'k) because r∤c'k (r>g); DR≡−p ⟺ A/D≡−p (mod h) checked; |𝒟|<(r−1)/2 and b↦−b injective. No fixed prime
divisor: ℓ|Q unit, ℓ>B degree argument fine. Minor: A≤1+4rg² (not g³) — harmless overestimate.

### L1.1 (dual form)
Proof re-derived: D=hj−p, N≡4ck²(4cj²+1) (mod D), (D,2ck)=1 from D≡−p (mod 4ck), p odd. Definition of M matches notes (44.2)/(44.3)
(raw count, multiplicities = distinct divisors D). From-scratch brute force `scripts/review_ti_lemma11.py`: all odd primes p<400,
c≤24, k≤11, (p,ck)=1 (19966 slices): divisor count = dual j-count, and no j solutions beyond hj−p>N (200 extra j each). SOUND.

### T6.1 (C(5)=10)
Re-derived: p≡1 (24) & (5/p)=−1 ⇒ p≡17,33 (40); certificates (5,1,D=3), and D=7 on (5,1),(10,1),(5,2) since
−20,−40,−80 ≡ 1,2,4 (mod 7) = all nonzero squares. `scripts/review_ti_thm61_cover.py`: no uncovered class mod 840.
From-scratch engine `scripts/review_ti_ckmin.py` (full 𝓑_p, forced slices NOT skipped, sympy factorint):
ck_min(193)=10, ck_min(12289)=77 (matches notes (48.12)); all 9307 hard p<2·10^6 with (5/p)=−1 have ck_min≤10, and =5 when p≡2 (5). SOUND.

### §5 record
`review_ti_ckmin.py one 9033649 900` (all slices incl. forced): n_p=43, ck_min=883. CONFIRMED.
