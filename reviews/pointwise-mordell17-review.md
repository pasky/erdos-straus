# Hostile review R83 — POINTWISE_MORDELL17.md (+ §2.1 table of POINTWISE_MORDELL.md)

Reviewer: side agent R83 (branch `side-agent/review-mordell17`), merged `side-agent/sterility-r17`
at d4ea35a. From-scratch scripts: `scripts/review_m17_*.py`.

Status: IN PROGRESS.

## Summary verdicts

(filled in below, claim by claim)

### Claim A — §2.1 T-generic table (POINTWISE_MORDELL) at T={17} and Lemma 1.1: **SOUND** (one simplification found)

Re-derived from scratch, starting from the *statement* of ET Prop 1.9 (arXiv:1107.1010 p. 8,
read from sources/elsholtz-tao-1107.1010.pdf), not from ET's coordinate formulas. A class `r mod M`,
`M = 17^k N`, `17∤N`, contains `x(u)` iff `r ≡ 1 (N)` and `u ≡ r (17^k)`. Family by family:

* I1 `−f mod 4ad`, `f|4a²d+1`: `4(ad)'|f+1`; box `−f mod (ad)_17`. (17|f forces 17∤ad, level 0.)
* I2 `{−f mod 4ac}∩{−c/a mod f}`, `(4ac,f)=1`: `4(ac)'|f+1`, `f'|a+c`; box `−f mod (ac)_17` or `−c/a mod f_17`.
* I3 `{−f mod 4cd}∩{n²≡−4c²d mod f}`, `(4cd,f)=1`: `4(cd)'|f+1`, `f'|4c²d+1`; box `−f` resp. the roots.
* I4 `−1/e mod 4ab`, `e|a+b`, `(e,4ab)=1`: `4(ab)'|e+1`; box `−1/e`.
* II1 `−e mod 4ab`: same conditions, box `−e`.
* II2 `−4a²d mod f`, `4ad|f+1`: `f'|4a²d+1`; box `−4a²d mod f_17`.
* II3 `−4a²d−e mod 4ade`, `(4ad,e)=1`: `T`-free part of the modulus is `4(ad)'e'`; since `(ad)'|a²d`,
  conditions `4(ad)'|e+1`, `e'|4a²d+1`; box `−4a²d−e` mod `(ade)_17`.

This is exactly the table. Splitting by where the 17 sits (I2, I3, II3 forbid both by their gcd
condition) gives exactly Lemma 1.1's types; I re-verified the I2(17|f) ↔ Q⁻¹ and the P-inversion
algebra by hand (correct). Level-0 (Lemma 1.2): all three rigid forms at `F=1` give a solution of
`4/1 = 1/x+1/y+1/z` in positive integers, impossible — correct.

Numerical confirmation (from scratch): `scripts/review_m17_brute.py` reads the classes *literally off
the Prop 1.9 statement* (CRT, all roots for I3, primitivity checked), all moduli `M ≤ 10⁶`, and
intersects with the 17-generic line, levels ≤3. Result: 295 (family, box) pairs (168 distinct boxes,
all cells); **no level-0 class**; **every one of them lies in the complete enumeration** of
`scripts/review_m17_enum.c` + `review_m17_union.py` (built from my own derivation of the types),
under the family→type map of Lemma 1.1 (I1→P; I2→U/Q⁻¹; I3→P/√Q; I4→U⁻¹; II1→U; II2→Q; II3→P/Q).
At M≤10⁵ the brute force sees 106 distinct boxes, matching the author's number.

**New observation (PROVED, reviewer): the (√Q) type is empty, and (Q) lives only at odd levels in
non-residue cells.** For a (Q)-datum, `f = 4adm−1 = 17^k g`. Since `f ≡ −1 (mod 4d)`, Jacobi
reciprocity gives `(d/f) = 1` (odd part: `(d_o/f) = (f/d_o)(−1)^{(d_o−1)/2} = 1`; 2-part: `f ≡ 7 (8)`
when `d` is even), and `(−1/f) = −1`; so `(−d/f) = −1`. As `g | 4a²d+1`, `−d·(2a)² ≡ 1 (mod g)`, so
`(−d/g) = 1`. Hence `(−d/17)^k = −1`: **k is odd and `−4a²d` is a non-residue mod 17**, so
`n² ≡ −4a²d (mod 17^k)` has no root. Consequently the I3(17|f) classes never meet the 17-generic
line, the union `P∪Q∪Q⁻¹∪U∪U⁻¹` is the whole story, and **the inversion symmetry `C_5 ↔ C_7` is
exact (no √Q caveat needed)**. Confirmed numerically: 0 √Q boxes at levels ≤5 (see Claim C).
The same reciprocity argument applied to a (P)-datum (`f=4ni−1 | 4·17^K a'²d'+1`, `f ≡ −1 mod 4d'`)
gives `(17^K/f) = −1`, i.e. **K odd** — a direct proof of "even K empty" (see defect m2).
