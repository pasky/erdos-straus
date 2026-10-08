# R95 — hostile review of POINTWISE_MORDELL13B.md (task O95)

Reviewer: side agent R95 (branch `side-agent/review-m13b`). Reviewed author commit: merge of
`side-agent/r13-diophantine` at review start. All numerical checks are from-scratch scripts
`scripts/review_m13b_*.py` (no use of `mordell_lib`, `mordell_check`, or `m13b_*`).

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Thm 3.1 (x* in II3 (8,33,11999) and I2 (125,88,11999); Conj 4.2 false) | SOUND |
| Lemma 1.1 (box conditions, 7 families, at x(u)) | SOUND |
| Lemma 1.2 (reciprocity parities at x*) | SOUND |
| Lemmas 2.1–2.4, Cor 2.5 (ES level, M_T≤N≤M_T², recoverability) | SOUND |
| §4 enumeration (x* only in the two data, N≤4·10⁷) | SOUND (independently re-run to N≤4·10⁵; author boxes re-verified) |
| §4 coverage table | SOUND-AFTER-REPAIRS (labelling, defect 1) |
| §5 Comp 5.1 ((2,15), (2,1/7) in no II3/I3/I1 class, e≤10⁸) | SOUND (independently re-run; the λ-cap is vacuous, defect 5) |
| Report: small-height k=4 survivors (2,15), (2,1/7), (2,−7/3) | SOUND as EVIDENCE |

## Claim-by-claim

### Theorem 3.1 — SOUND
Re-derived from the *statement* of ET Prop 1.9 (sources/elsholtz-tao-1107.1010.pdf, p.8) and the
explicit Σ-points of ET §10 (p.37–38) with the maps π^I=(abdn,acd,bcd), π^II=(abd,acdn,bcdn)
(ET (2.22) and the line after (2.9)). `scripts/review_m13b_thm31.py`:
* II3 `(a,d,e)=(8,33,11999)`: `(4ad,e)=1`; `M=4ade=12670944=2⁵·3·11·13²·71`, `r=−4a²d−e mod M=12650497`;
  `r≡1 (mod 6816)`, `r≡2 (mod 1859)` → x* ∈ class. Σ^II-point
  `(a,(n+e)/4ad,(n+4a²d+e)/4ade,d,e,(n+4a²d)/e)` satisfies all nine relations (2.13)–(2.21)
  identically in n (sympy), and `4/n=1/x+1/y+1/z` identically. b,c,f are linear in n with positive
  coefficients and integral at r and r+M ⇒ integral on the whole class and positive for all n≥1.
* I2 `(125,88,11999)`: `(4ac,f)=1`; CRT of `−f mod 4ac`, `−c/a mod f` gives `M=527956000`, `r=426568001`,
  `M_T=1859`, x* ∈ class; Σ^I-point satisfies (2.1)–(2.9); b,d,e integral and positive on the class.
* Prime `p=12650497` (≡2 mod 11, 13): solution reproduced exactly.
* Hand facts in the proof: 11999=71·13², 12001=11·1091, 8449=71·119, 4225=25·13², 12000/96=125 — correct.
* Conj 4.2 (POINTWISE_MORDELL.md l.193) says literally "x* … lies in no ET Prop 1.9 class" — refuted.
  The "In particular" (no finite covering) part is NOT refuted, and the author correctly says only
  "reopened". Comp. 4.1 (M≤10⁶) is not contradicted (both moduli >10⁶). Label "PROVED" is fair.

### Lemma 1.1 — SOUND
`scripts/review_m13b_lem11.py N seed bias`: classes built literally from the ET Prop 1.9 statement
(I3: all square roots of `−4c²d mod f` by brute force, CRT with `−f mod 4cd`); for each random P the
full set `{u mod M_T : x(u) ∈ class}` is compared with the table. Parameters carry random powers of
11, 13 in every slot; "bias" draws f′/e′ among divisors of the relevant polynomial so that the T-free
conditions hold (otherwise almost all sets are empty and the test is vacuous — the author's own
check has the same weakness only mildly: 3605 memberships / 14000). Seeds 7 (400/family) and 11
(1500/family): **0 mismatches**; non-empty u-sets: I1/I2/I4/II1/II3 1500 each, I3 834, II2 42 (II2 weakly
exercised, but its condition is a one-line CRT). The u=2 specialisations (`f_T∣2a²d+1` etc.) follow
since `f_T` is odd. Hand re-derivation of each row agrees (II3 uses `(ad)′∣a²d`, `(ad)_T∣4a²d`).

### Lemma 1.2 — SOUND
Re-derived; the proof only uses that u is a non-residue mod each q∣M_T (so it holds for every such u,
not just u=2). Brute force (same script, all hits u∈L with `(u/q)=−1` for all q∣M_T): 0 parity
failures in 2816 tested hits (I1 616, I2 647, I3 353, I4 555, II1 698, II2 43, II3 604).
Minor wording: in (i) "q∤g" is not needed; (i) holds for any m′ (MORDELL17 Lemma 1.3), (ii) needs `q∤g`.

### Lemmas 2.1–2.4, Corollary 2.5 — SOUND
Re-derived all four identities by hand (each reduces to `jBg=j(4a′d′m−1)=B(λa′+m)` or the analogue;
integrality of j uses `gcd(m,g)=1` from `4a′d′m≡1 (g)`). Note: only the T-free conditions are used,
so the lemmas hold for every T-generic datum, not only those containing x(u) (the statement of 2.1
assumes more than it uses — harmless).
`scripts/review_m13b_sec2.py 150 5`: for 150 random T-generic data per family (random 11/13-powers in
all slots; T-generic = literal ET class has a residue ≡1 mod M′), the forward maps give an exact
solution of `4/N`, `M_T ≤ N ≤ M_T²` holds, and the reviewer's own inverse maps (canonical: a′,d′
T-free, `e_T=B`, `(ab)_T=N`, …; `review_m13b_enum.invert`) recover the datum: **0 failures / 1050**.

### §4 enumeration — SOUND
* `scripts/review_m13b_enum.py 400000`: own ES enumerator (x-loop + divisors of q²) and own
  canonical inversion for all 20 T-units N ≤ 4·10⁵. ES-solution counts equal the author's `es_N.txt`
  counts for every N (9, 4, 24, 218, 24, 204, 672, 918, …, 11896, 10182, 7465, 1399). Every box from my
  data appears in the author's box set (0 missing). x* lies only in the two Thm 3.1 data (N=1859).
* The author's inverter is *not canonical* (no requirement that a′,d′ are T-free or `e_T=B`), so it
  outputs extra genuine data (e.g. boxes with `M_T=17303` already at N≤1859) and re-finds the
  Thm 3.1 data at N=24167, 314171. These are the same data, not new "dilations" (see defect 2).
  Harmless for soundness: every candidate is tested exactly.
* `scripts/review_m13b_authorboxes.py`: all 209295 boxes in the author's 32 `inv_*.pkl` re-verified
  against my literal ET classes (0 failures); coverage from them reproduces 15/143, 970/20449,
  135639/2924207 exactly. My own data (N≤4·10⁵) independently give 15/143 with the same survivor set
  `{2,57,79}×{15,28,54,132,145}`, and 1273/20449 at k=3 (≥ 970, consistent with a smaller N bound).
* Independent CERTIFIED by-product (my engine, N≤4·10⁵, `review_m13b_cover.py`): at resolution 11³13³
  every point of the T-generic target with `x_13` a non-residue mod 13 is covered except inside
  the (2,2) cell — confirms the author's `m13b_cover.py 3` claim.
* Clean corollary worth stating (since `N≤M_T²`): the enumeration to 4·10⁷ is *complete for every box
  level M_T ≤ 6324* (my independent run to 4·10⁵ certifies this for M_T ≤ 632), i.e. M_T ∈ {11,13,121,143,169,1331,1573,1859,2197}: x* lies in no T-generic class
  of those levels except the two of Thm 3.1.

### §5 targeted search, Computation 5.1 — SOUND
Own program `scripts/review_m13b_target.c` (different method: no discrete log, **no T-level cap**). Key
observation: the box condition `e≡−u_q (mod q^{v_q(ad)})` forces `v_q(a)+v_q(d) ≤ v_q(e+u_q)` (and =0 if
q∣e), so all T-parts are enumerated exhaustively for each `e=4a′d′m−1`. Conditions re-derived from
ET Prop 1.9: II3 `e′∣4a²d+1`, `e_T∣u+4a²d`; I3 `f′∣4c²d+1`, `f_T∣u²+4c²d`; I1 `f∣4a²d+1`.
* Validation (`review_m13b_target_validate.py`): 150/150 random II3/I3/I1 data from my §4 run recovered
  at their box residue; at x* it finds (8,33,11999).
* Runs at X=10⁸ (3.05·10⁹ (a′,d′,m) triples each): `(2,15)`: 0 hits; `(2,1/7)` (u₁₃=7⁻¹ mod 13¹⁶): 0 hits.
  **Comp 5.1 confirmed.**
* `review_m13b_points.py`: (2,15), (2,1/7), (2,−7/3) lie in none of the 209295 re-verified author boxes nor
  my boxes; x* lies in exactly the two Thm 3.1 boxes. (EVIDENCE for the report's x** candidates.)
* I did not review the U/I2 targeted program `m13b_target2.c` (Comp 5.1 does not use it).

## Defects

1. **MINOR (labelling), §4 coverage table, rows k=2 and k=3.** Only k=4 is marked "incomplete: needs N
   up to F²", but k=2 already needs N up to (11²13²)² ≈ 4.2·10⁸ > 4·10⁷ and k=3 up to ≈8.6·10¹²; so all
   three rows are *upper bounds* on the uncovered fraction (boxes with ES level ≤4·10⁷ only), and the
   k=2 survivor list may shrink. *Repair:* mark all three rows incomplete (or state "ES level ≤4·10⁷"
   in the column header and drop the k=4-only note); state completeness for M_T ≤ 6324 explicitly.
2. **MINOR, §4 bullet "x\*" ("they reappear at N=1859·13^k via dilation").** At N=24167, 314171 the
   engine re-finds the *same* parameter triples (8,33,11999), (125,88,11999) because the inversion is
   non-canonical; there is no dilated datum. *Repair:* "they are re-found at N=24167, 314171 by
   non-canonical inversion (same data)"; mention in the m13b_invert docstring that candidates are a
   superset of the canonical inverse images.
3. **MINOR, Lemma 1.2 (i).** "and q∤g" belongs to (ii), not (i).
4. **MINOR, Lemma 2.1 hypothesis.** "with x(u) in the class" — only the T-free conditions are used;
   state the lemma for T-generic data (as Cor 2.5 does) to avoid suggesting a dependence on u.
5. **MINOR, Comp 5.1 statement.** The cap `v_11(λ),v_13(λ)≤20` is vacuous for e≤10⁸: since
   `v_q(ad) ≤ v_q(e+u_q) ≤ log_q(7e+1) < 8` (for u₁₃=1/7, `v_13(e+1/7)=v_13(7e+1)`), `v_q(λ)≤2v_q(ad)<16`.
   *Repair:* state Comp 5.1 as "no II3/I3/I1 class with e≤10⁸" (no T-level restriction), citing this bound.
   Also say explicitly that II2 and the U/I2 families are *not* covered by Comp 5.1, so x\*\* is EVIDENCE only.
