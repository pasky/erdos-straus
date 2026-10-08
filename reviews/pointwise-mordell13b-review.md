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
