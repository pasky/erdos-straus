# Hostile review R31 of POINTWISE_TYPEI.md (O31, branch side-agent/typei-ckmin)

Reviewer branch: side-agent/review-typei. Status: in progress.

## Summary verdicts (filled in incrementally)

| claim | verdict |
|---|---|
| L1.1 | SOUND |
| T6.1 | SOUND |
| §5 census (EVIDENCE) | CONFIRMED (record 883 + 154-prime random sample recomputed from scratch; file complete) |
| §6.2 formal table, C6.4 (H part) | SOUND (all 7 rows reproduced from scratch) |
| C6.4 unconditional part | SOUND-AFTER-REPAIRS (defect 1) |
| §6.1 literature | SOUND (checked against ET PDF and Salez audit text) |
| T2.1 | SOUND (CONDITIONAL label correct) |
| T3.1 | SOUND-AFTER-REPAIRS (defect 2; constant/asymptotic unaffected) |
| P4.1 | SOUND (minor: defect 5) |
| P4.2 | SOUND |
| L4.3 | SOUND |
| A4.4, A4.6 | Assessments, reasonable (defect 3 in A4.6 arithmetic) |
| L4.5 | label overclaim (defect 4) |
| R6.2 | (i) SOUND; (ii) GAP in sketch (defect 6), correctly flagged as sketch |

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
`scripts/review_ti_census_sample.py`: the census file contains exactly the 82887 hard primes <10^7; my engine (all slices,
forced included) reproduces (n_p, ck_min) for a random sample of 150 rows plus 12289, 92401, 414241, 9033649 — 0 mismatches.
Per-n_p maxima and all §5 table entries (fractions, counts, max ratio/max ck_min per range) recomputed from the file: match.
EVIDENCE 6.3 population count (6495 primes with n_p=7 in (10^5,3·10^6)) matches; the D≤2000 witness claim was not rerun.
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

Concrete instances (`scripts/review_ti_thm21_instance.py g r`: builds Q, a, b exactly as in the proof, replaces H by a search
for t with p and all (p²+4ck²)/A prime, then checks n_p and every unforced slice ck≤gr by direct factorisation):
g=1,r=7: p=31982111786880107424001, n_p=7, slice (7,1) M=0; g=1,r=11: p=1797590122919658552759652159465320001, n_p=11,
(11,1) M=0. g≥2 instances are out of reach (B≥max A forces Q≈10^200). Mechanism confirmed.
Uniformity check: the H-family depends on (g,r) (finite for each); "ck_min≥n_p^{2−ε} i.o." needs only ONE r≥r_0(ε) (its
infinitely many p all have n_p=r), so the finite-family claim is accurate.

### T3.1 (GRH)
Splitting in L=ℚ(i,√ℓ:ℓ≤y) ⟺ p≡1 (4), (ℓ/p)=1 ∀ℓ≤y ⇒ p≡1 (24), n_p>y ✓; conductor–discriminant bound ✓; LO/Serre GRH
error term as quoted matches my recollection of LO 1977 Thm 1.1 (`c₁(|C|/|G| x^{1/2} log(d_L x^{n_L}) + log d_L)`);
I could not access LO/Serre/Montgomery here (Lau–Wu l.72 only gives Ω(log p log₂p), no constant — the constant
1/(2log2) is the author's own derivation). See defect 2.

### P4.1, P4.2, L4.3
P4.1: ck≤Gn<n² ⇒ at most one non-residue prime factor in c (all ≥n), so unforced ⟺ c=qc' as stated ✓. P4.2: the
Prop 8.3 construction with ℓ = least prime ≥5 with ℓ∤L or (a/ℓ)=−1 gives (ℓ/p)=−1, (ℓ'/p)=1 for 5≤ℓ'<ℓ, so n_p=ℓ and
ck_min=ℓ ✓; consequence for B≥0 periodic ✓. L4.3: (b) K_s∖(H∩K_s) ≥ half of K_s = 1/4 of G_h ✓; (c) N≡p²∈kerψ∩K_s so the
single large prime factor is in H ✓; (d) common roots of x²+4c_ik_i² mod ℓ only for ℓ|4(c_ik_i²−c_jk_j²) ✓.

## Defects

1. **MINOR (Cor 6.4 unconditional proof, "Refine the formal class by p≢ any root of any N_{c,k} (ck≤X) mod each ℓ_i.
   This is possible because ℓ_i>B≥2·#slices+2").** Read literally ("any N_{c,k}, ck≤X") this is FALSE for the r=11 row:
   X=3000 has 24496 slices, 2·24496+2 > B=30000. It is true for #slices = slices with s∉{1,2,3,6} (14834 → 29670 ≤ 30000,
   barely; this is what typei_formal.py counts) and comfortably for the 1491 unforced slices. Also p≢0 (mod ℓ_i) must be
   avoided (2·#+1 excluded residues). *Repair:* refine only against roots of N_{c,k} for UNFORCED slices with ck≤X
   (certificates on forced slices never hold), state the count explicitly (r=7: 319; r=11: 1491), and say "ℓ_i > 2·#+1".
2. **MINOR (T3.1 proof, condition `2^{π(y)} ≤ x^{1/2}/(C(log x)²)`).** With θ(y) ≍ log x·log log x (as the proof itself
   notes) the error term c₁x^{1/2}θ(y) is ≍ x^{1/2} log x log log x, while the main term under this condition is only
   ≍ C x^{1/2} log x. So the inequality as written does not close. *Repair:* take
   `π(y) ≤ (log x − 4 log log x − 2 log log log x − 2 log C)/(2 log 2)`; y ∼ (1/(2log2)) log x log log x is unchanged.
3. **MINOR (A4.6).** "(log G)³ ≪ log₂p/log p … i.e. ck_min ≥ n_p+O(n_p·log₂p/log p)": from (log G)³ ≪ δ one gets
   G−1 ≪ δ^{1/3}, i.e. n_p(1+O((log₂p/log p)^{1/3})). Assessment only; fix the exponent.
4. **MINOR (L4.5 label).** The proved content is the CRT description of the events (moduli hD up to h√N > hx/2). The sentence
   "any argument that controls these events through the distribution of primes in progressions needs moduli >x" is a
   meta-statement, not a theorem. *Repair:* label that sentence Assessment (as in A4.4).
5. **MINOR (P4.1).** 𝓤_p(G) should be intersected with 𝓑_p (and (p,ck)=1); this is automatic iff Gn<n²≤p/2, which holds
   for all hard p (checked: no hard p<10^6 has n_p²>p/2; beyond, explicit Burgess/Treviño), but should be stated.
   Also "every prime of sf(c') a residue" — since ck<n², actually every prime of c' is a residue; harmless.
6. **MINOR/GAP (R6.2(ii), "So under H, C(r) is exactly the least height of a finite Type-I covering").** Passing from
   "every class fixing v_ℓ(N) for ℓ≤B is covered by B-smooth certificates" to "a FINITE covering exists" needs a compactness
   step in ∏_{ℓ≤B}ℤ_ℓ: fixing classes have unbounded depth near ℓ-adic roots of N_{c,k}, and the covering certificates there
   could use unbounded powers ℓ^e. The step can be supplied (an ℓ-adic root point p* of one slice is a common root of no
   other slice off finitely many ℓ; if p* is uncovered then, since ℓ^i mod 4ck is periodic and the other slices are locally
   constant near p*, nearby fixing classes are uncovered too, contradicting (ii); so every point of the compact space is
   covered and a finite subcover exists), but as written it is missing. Doc already says "sketch"; keep the label and add the
   argument, or keep "≤" only (finite covering ⇒ C(r) bound, plus uncovered fixing class ⇒ C(r)>X under H).
7. **MINOR (§6.1 wording).** "the literature has full single-prime coverings exactly for r=5,7" — only established for
   Salez's listed filters S_ℓ, ℓ≤37; say so.
8. **MINOR (§6.2 text).** typei_formal.py checks determinacy only for unforced slices up to the hit; determinacy genuinely
   fails beyond (e.g. point 3:7:9, slice (23,76) has v_3(N)=12≥9; point 7:3:1, forced slice (10,1) has 7²|N). The prose
   ("It asserts that this part, and every target class −p mod 4ck, is determined by the class") should say "for every
   unforced slice with ck ≤ (formal ck_min)", which is all that the H and covering arguments need.
