# Hostile review R31 of POINTWISE_TYPEI.md (O31, branch side-agent/typei-ckmin)

Reviewer branch: side-agent/review-typei. Status: in progress.

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| L1.1 | SOUND |
| T6.1 | SOUND |
| §5 record ck_min(9033649)=883 | CONFIRMED (independent) |
| §6.2 formal table, C6.4 (H part) | SOUND (all 7 rows reproduced from scratch) |
| C6.4 unconditional part | SOUND-AFTER-REPAIRS (defect 1) |
| §6.1 literature | SOUND (checked against ET PDF and Salez audit text) |
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

### §6.2 formal table and Cor 6.4
From-scratch engine `scripts/review_ti_formal.py` (own valuation bookkeeping: default primes via v_ℓ(1+4ck²), prescribed
primes via v_ℓ(a²+4ck²) asserted < e; target class −p mod 4ck asserted fixed; forcedness from the Legendre symbols fixed
by the point; determinacy checked for every UNFORCED slice up to the hit — forced slices are 0 by notes Thm 48.1 and need no
determinacy). Results (all agree with the table):
* `7:3:1` → 21, (7,3), D=11; `7:5:1` → 21, D=23; `7:6:1` → 28, (14,2), D=15;
* `2:25:14 3:7:9 7:6:6` (X=2000,B=30000) → **539**, (77,7), D=43, f=3·13·43; 319 unforced slices below;
* `2:25:14 3:7:9 7:13:6` → 98, (14,7), D=183; `2:25:14 3:7:9 11:2:4` → 990, (55,18), D=119;
* `11:2:5` (X=3000,B=30000) → >3000 (1491 unforced slices, 14834 with s∉{1,2,3,6}, 24496 total);
  `11:2:4`, `11:6:4` (X=1500,B=14000) → >1500.
Hand check of the 539 witness: −p ≡ 3 (4), 43 (49), 10 (11) and 43 ≡ 3, 43, 10 resp. ✓; n_p=7 at the point ✓.
The H-step identity M=2·#{D|f: D≡−p (4ck)} when N=f·R, R prime >B, was also tested on real factorisations
(`scripts/review_ti_step5.py`, 21391 cases, 0 failures).
Note: determinacy genuinely FAILS beyond the hit for some points (e.g. `7:3:1`, e_7=1: slice (10,1) has 7²|N — but it is
forced; `3:7:9`: slice (23,76), ck=1748, has v_3=12≥9). These are all forced or beyond the stated X-range used, so no
claim is affected; but the doc should say determinacy is only needed/checked for unforced slices up to the hit.

Unconditional part (refinement at primes ℓ_i>B occurring in the covering): argument re-derived and correct in substance:
quantifier order is right (refinement depends on the given covering), B-smooth F: F|N ⟺ F|f because v_ℓ(N) is fixed for
ℓ≤B on unforced slices; certificates on forced slices never hold; F containing some ℓ_i fails as ℓ_i∤N; the refined
class is a reduced class mod Q·∏ℓ_i, so Dirichlet gives infinitely many primes, all hard with n_p=r. See defect 1.

### §6.1 literature
Checked against `sources/elsholtz-tao-1107.1010.pdf` (pdftotext): ET Type-I variety (2.6) `4acd=n+f`, (2.7) `ef=4a²d+1`,
(2.3) `4abcd=na+nb+c`; so ET (a,c,d,f) = our (j,k,c,D) — consistent with Lemma 1.1 and with the doc's
`(c_ours,k_ours,D)=(d,c,f)` for family 3. ET §10 polynomial witnesses: family 1 has c_ET=(n+f)/4ad (our k grows),
family 2 and 4 have d_ET growing (our c grows), family 3 has c,d fixed. Author's claim correct.
Salez (audit text of arXiv:1406.6307): (15d) is `p+F≡0 (4CD)`, `p²+4C²D≡0 (F)` ✓; Example 1 [15d] at p=120t−23 ✓ = slice (5,1),
D=3 (Thm 6.1 first case). Filters S_5,S_7,S_11 as quoted ✓; S_13..S_37 also miss non-residues (checked by hand: S_13 misses 2,7).
"exactly for r=5,7" should read "among Salez's listed single-prime filters (ℓ≤37)" — MINOR wording.
`scripts/review_ti_mod168.py`: no (c,k,F) with ck|42, F|21 is valid on a hard class that is a non-residue mod 7, confirming
"no (15d)-certificate is decided modulo 168 on a non-residue class mod 7".
