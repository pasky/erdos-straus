# R250 — hostile review of FF_INVERSION_CHECK.md (O244)

Reviewer: R250 (side-agent/review-ff-inversion). Reviewed: FF_INVERSION_CHECK.md at side-agent/ff-inversion cbda85ab, report
reviews/agent-reports/AGENT_REPORT_O244.md. Background checked: FUNCTIONFIELD_ES.md §1, §6.2 (Lemmas 1.2, 1.3, 6.2),
FUNCTIONFIELD_ES2.md §0.1–0.2, FUNCTIONFIELD_ES3.md Lemmas 1.1, 1.2, 2.1, FF_STERILE_PUSH Thm 3.1, FF_STERILE_SMALL §§3, 5–8
(Prop 6.1, Lemma 7.2, Thms 3.1, 5.2, 7.3, 8.1), FF_ODD_ABSENCE Thm 2.2, and Elsholtz–Tao arXiv 1107.1010
(sources/elsholtz-tao-1107.1010.pdf: Prop 1.9, §2 Props 2.2, 2.6, identities (2.1)–(2.21)).
From-scratch scripts: `scripts/review_r250_*.py` (own GF(q) arithmetic; nothing imported from `zi_*`).

## Summary verdicts

(filled in progressively below; see §1 per claim, §2 defects)

## 1. Claim-by-claim

**Lemma 1.1 (ET parametrisation over F_q[T]) — SOUND.** Re-derived. (i) P | no X_i: the right side has P-free denominator;
P | all: deg A ≥ 1 vs. degree ≤ 0. (ii) Type II: (AX₁ − P)/X₁ is reduced since gcd(AX₁ − P, X₁) = gcd(P, X₁) = 1; with
g = gcd(Y', Z'), gcd(y + z, gyz) = gcd(y + z, g) =: c because gcd(y + z, yz) = 1; reduced fractions with monic denominator are
unique, so X₁ = dyz and AX₁ − P = (y + z)/c (numerator not nec. monic: e = 2 occurs, e.g. FE Prop 1.4(ii)). (iii) Type I: the
right side's reduced denominator is P-free, so P | AX₁' − 1 and the rest is as in (ii). Matches ET Props 2.2/2.6 (checked in
the PDF; ET's extra normalisation "a, b, c without common factor" is not needed for existence). The statement "e = (a+b)/c" is
right; e is monic in Type I (lc(a + b) = 1 there, see Lemma 1.2) but not necessarily in Type II.
*From-scratch check* (`scripts/review_r250_lemma11.py`, log `data/review_r250/lemma11.txt`): for every monic irreducible P of
the listed degree, ALL monic solutions by a naive loop (minimal denominator X of degree ≤ n − k, then Y of the forced degree
deg M − deg N, Z solved; no divisor method, no ET input), compared as sets with the solutions generated from the Lemma 1.1
parametrisation (Type II from (a, b, d), Type I from (a, c, d)); every solution decomposed by the proof's construction:
q = 3 (k = 1, n = 3, 4; k = 2, n = 4; k = 2, n = 5 in P ≡ 1 + T mod T²), q = 5 (k = 1, 2; n = 3), q = 9 (k = 1, n = 2; k = 2, n = 3):
1,068 solutions, sets equal in every case, 0 assertion failures (P | one or two denominators, monic a, b, c, d, c | a + b,
Type I has deg a ≠ deg b).

**Lemma 1.2 — SOUND.** Type II: deg X₂, X₃ ≥ n > n − k. Type I: A·acd = c(eP + 1)/b, ce = a + b give AX₂ − P = (aP + c)/b;
lc((a + b)P + c) = lc(a + b) must be 1 (left side A·abcd monic; deg c ≤ deg(a + b) < n + deg(a + b)), and lc(a + b) = 2 ≠ 1 if
deg a = deg b (q odd). The brute force above asserts X, E_FF = AX − P, bE_FF = aP + c and deg E_FF = n − (deg b − deg a) on
every solution.

**Corollary 1.3 (ET dictionary) — SOUND** (with MINOR m-1, m-2 below). I matched the seven classes of ET Prop 1.9 to fixed
parameters: I1 ↔ (a, d, f) [n ≡ −f mod 4ad, f | 4a²d + 1], I2 ↔ (a, c, f), I3 ↔ (c, d, f), I4 ↔ (a, b, e) [n ≡ −1/e mod 4ab],
II1 ↔ (a, b, e) [−e mod 4ab], II2 ↔ (a, c, d) [f = 4acd − 1 fixed, n ≡ −4a²d mod f], II3 ↔ (a, d, e) [−4a²d − e mod 4ade]. The
labelling I1–I4, II1–II3 is the order of ET Prop 1.9 (ET do not number them; the labels are M17's). The five linear
translations re-derived from FE Lemma 1.3 (Y = κPX/a_FF, Z = κPX/b_FF): II1 = (e; 0, b; 0, a), II3 = (e; 2, ad; 0, a),
I1 = (f; 1, a; 2, ad), I2 = (f; 1, a; 0, c), I3 = (f; 3, cd; 0, c) — all correct. Note the direction: the linear family's validity
condition is A·lcm(a0, b0) | P + E, weaker than ET's A·a0·b0 | P + E (e.g. II1 needs Aab | P + e), and E | s, lc(s) = lc(E) hold
automatically when the ET solution exists (s = κE with κ monic). So ET-type validity set ⊆ linear validity set for these five —
the inclusion the coverage argument needs. The converse (every linear family is a finite union of the five ET types) is
neither claimed nor needed, but see m-1 on the definition of O_ET.

**Proposition 1.4 (I4 families) — SOUND.** d = (eP + 1)/(Aab): lc(d) = lc(e) = 1; lc(c) = lc(a + b) = 1 as deg a ≠ deg b; the
identity A·abcd = (a + b)P + c is the Type I equation. The slice form T^{k+v_T(ab)} | ue + 1, (ab)' | e + 1 is correct (x ≡ 1 at
every ℓ ≠ T means x ≡ 1 mod ℓ^∞). The single-P linear family (E_FF(P); 1, a; 0, c) is right. The review counterexample
(a, b, e) = (1, T, 1), A = T²: I4 class P ≡ −1 mod T³ = validity class of (1; 0, T; 1, 1) — re-checked by hand. The q = 3 example
(P = T⁶ + T⁴ + 2T² + T + 2, e = T + 1, a = 1, b = T) is re-verified inside `review_r250_domination.py`-style checks (identity
holds; see §3). Hypothesis gcd(e, Aab) = 1 is redundant on the classes where Aab | eP + 1 (any common factor would divide 1),
harmless.

**Remark 1.5 (II2) — SOUND.** b = (cP + a)/f is monic (lc f = 1), c | a + b is automatic from A·abcd = cP + a + b.

**Lemma 1.6 (3-bounded families) — SOUND.** Re-derived all six cases. Type I (a, c, d): b(Aacd − P) = aP + c already fails
on leading coefficients for n > deg(Aacd) (lc −1 vs +1), stronger than stated. Scope note is honest: the F_q[T] analogue of the
*completeness* half of ET Prop 1.9 ("every class solvable by polynomials lies in one of the seven families") is NOT proved, so
"exactly two types are omitted" is relative to ET's list (MINOR m-2).

**"What FE3 Lemma 1.1 classifies" (16 type pairs) — SOUND.** Same/opposite side residues re-derived (P ≡ 1, X ≡ T^{−k} mod E).

**Lemma 2.1 (II2 never valid on a slice) \u2014 SOUND.** f = T^k acd \u2212 1 \u2261 \u22121 (mod T), so P \u2261 1 (mod f) at x_u and validity
becomes f | a + c; a + c \u2260 0 (monic, q odd) and deg(a + c) \u2264 max(deg a, deg c) < deg f. Holds for every A with T | A (or any A
at the point x \u2261 1).

**Lemma 2.2 (I4 at u \u21d2 Case A at 1/u) \u2014 SOUND.** T^{k+j} | u\u207b\u00b9 + e \u21d4 T^{k+j} | 1 + ue; lcm(a, b)' | (ab)' | e + 1; types (0, 0):
s = a + b, lc(s) = 1 = lc(e) since deg a \u2260 deg b and e is monic (forced in Type I). One unstated point: E = e has positive degree
on every slice used (e constant monic means e = 1, centre u \u2261 \u22121, which is on no c-slice and has u\u2080 = \u22121 \u2208 F\u2083^*), so Lemma 2.3's
\"deg E \u2265 1\" is satisfied (MINOR m-4).

**Lemma 2.3 (Case A ball \u2286 Case B ball with the same E) \u2014 SOUND.** Re-proved line by line: H monic T-free; E \u2261 \u22121 mod
g'(a1b1)' gives a1'b1 | H (coprime factors), so L' = H/b1 is T-free with a1' | L'; mod E: T^vH \u2261 1, b1 \u2261 \u2212T^\u03b1a1' and b1 is a
unit (b1 | E + 1), so T^sL'a1' \u2261 \u22121; D = 1 + T^sL'a1' monic; s = k + j + \u03b3 with 0 \u2264 \u03b3 \u2264 j needs exactly s \u2265 k; j \u2264 \u03b1 \u2264 j_A needs
exactly v \u2264 k + \u03b1. The Case B family (E; 0, T^\u03b3a1'; 2, T^jL') then satisfies FE3 Lemma 1.1(i) on the whole Case A ball (the
L'-condition is a condition on E only). Note the original g of the Case A family plays no role (its ball is only smaller).
*From-scratch checks* (`scripts/review_r250_domination.py`, log `data/review_r250/domination.txt`): every Case A datum with
g = 1 in the degree box, the Case B datum built and all conditions asserted; **plus an end-to-end check that does not use FE3
Lemma 1.1**: a polynomial P in the Case A ball (\u2261 1 modulo all T-free moduli involved; with PRIME = 1 irreducible) is solved
explicitly by the Case A family and by the Lemma 2.3 Case B family, and a P' in the I4 ball by the I4 family and by the swapped
Case B family of Lemma 2.4 (monic denominators and the identity A\u00b7XYZ = P(XY + YZ + ZX) asserted):
| q, k, slices, D, DMAX | data (unordered, g = 1) | Lemma 2.3 hyp. hold | outside hyp. | 2.3/2.4/end-to-end OK |
|---|---|---|---|---|
| 3, 2, c, 6, 9 (P prime) | 16 | 16 | 0 | 16/16/16 |
| 9, 1, u\u2080 \u2209 F\u2083^*, 2, 12 (P prime) | 6 | 6 | 0 | 6/6/6 |
| 9, 1, u\u2080 \u2209 F\u2083^*, 3, 12 | 14 | 14 | 0 | 14/14/14 |
| 5, 2, c, 4, 12 (P prime) | 0 | \u2014 | \u2014 | \u2014 |
| 9, 2, c, 3, 12 | 2 | 2 | 0 | 2/2/2 |
| 3, 3, c, 6, 10 | 16 | 16 | 0 | 16/16/16 |
| 3, 2, all, 4, 9 | 30 | 26 | 4 | 26/26/26 |
| 5, 2, all, 3, 8 | 28 | 24 | 4 | 24/24/24 |
| 9, 2, all, 2, 8 | 12 | 8 | 4 | 8/8/8 |
| 3, 3, all, 4, 10 | 30 | 22 | 8 | 22/22/22 |
The author's counts are ordered pairs (32 = 2\u00b716 etc.); mine agree. The \"outside\" data are all off-slice (v = 0, \u03b1 < k), as
the author says. Observation: on the c-slices \u03b1 \u2265 2 always (\u03b1 = 1 forces b1 = 1, F = 1, E = Ta1' + 1, v_T(E + 1) = 0 \u2260 1), so
Lemma 2.3 applies directly at k = 3 as well (row 3, 3, c); not needed by the document.

**Lemma 2.4 (Case B inversion-closed) \u2014 SOUND.** EE' = D \u2261 1 mod T^s, s \u2265 k + j; D \u2261 1 and E \u2261 \u22121 mod L' give E' \u2261 \u22121; E'
monic divides D; E' is non-constant (E' = 1 would give \u22121/w \u2261 1). Checked in all rows above, including end-to-end.

**Theorem 2.5 \u2014 SOUND (MINOR wording m-1, m-4).** (i) k = 2: at 1/u (the (\u2212c)-slice) FE2 \u00a70.2 step (1) uses only
E + 1 \u2261 \u2212c'T (mod T^{k+j}), k + j \u2265 2, E | a1 + b1, E \u2261 \u22121 mod L' \u2014 all available for F^A (with its own g) \u2014 and gives \u03b1 \u2265 1,
T \u2224 b1, v = 1; Lemma 2.3 then 2.4. (ii) k = 1: SS Lemma 7.2(a) (re-read; it covers lc(E) \u2208 {1, 2}, and its \"neither divisible\nby T\" branch is Prop 6.1's argument, which forces E constant \u2208 {1, 2}, i.e. u\u2080 \u2208 F\u2083^*) gives \u03b1 \u2265 1 at 1/u; v = 0 because
e(0) = \u22121/u\u2080 \u2260 \u22121. **k \u2265 3 reduction \u2014 SOUND**, re-derived: (a) a level-k linear family valid at x_u is valid at level 2 with
the same data: the T-adic condition T^{k+j} | u + E implies T^{2+j} | u + E; E | a0 + b0 (Case A) and lc(s) are k-independent
(lc(s) \u2208 {1, lc(a0 + b0), lc(L/a0 + L/b0)}); (b) Case B: D = 1 + T^{k+j+\u03b3}L'g' is the level-2 D with j\u2082 = j + k \u2212 2, \u03b3\u2082 = \u03b3 \u2264 j\u2082,
same ball; (c) I4: T^{k+v_T(ab)} | ue + 1 implies the level-2 condition, the other hypotheses are k-free; (d) II2: Lemma 2.1 for
every k. So covered_k(ET) \u2229 \u03a3 \u2286 covered_2(linear \u222a I4) \u2229 \u03a3 = covered_2(linear) \u2229 \u03a3. That every k \u2265 2 theorem in question
(SP Thm 3.1, SS Thms 3.1, 5.2) is proved by certifying the level-2 union bound (\"take k = 2\") I checked in each proof; the
same (a)\u2013(b) argument is in fact the rigorous form of SP's one-line justification \"N(s) and the Case A exponent only grow
with k\". No theorem in the list is k \u2265 3-only, so O(q, T\u00b2) \u2229 \u03a3 always has the certified positive measure.

**Corollary 2.6 \u2014 SOUND** for (J)51 (SP Thm 3.1), (J)56 (SS Thms 3.1, 5.2, 7.3, 8.1 incl. Lemma 7.4) and (J)67 (OA Thm 2.2,
whose slices P\u2088 \u2282 {u\u2080 \u2209 F\u2083^*}, inversion-closed, k = 1), and for Conjecture 0.2 (k = 2, x*_c on a c-slice) in the direction
x*_c \u2208 O \u21d2 x*_c \u2208 O_ET (the \u21d0 direction needs m-1). The O140 Prop 4.1 remark (x \u2261 1: I4 needs Aab | e + 1 with
deg e \u2264 max(deg a, deg b) < deg Aab, so e = \u22121, not monic; II2 needs f | a + c) is right for every A. \"Same certified
constants\" is right: for k \u2264 2 the ET-covered and linear-covered parts of \u03a3 coincide; for k \u2265 3 the ET-covered part is inside
the level-2 linear-covered part, which is what the certificates bound. The \"Case A terms with monic E are redundant\" side
remark is right (the containing Case B balls are terms of the Case B sum). **Answer to the brief's stakes question:** the
domination argument is correct, so (J)51, (J)56, (J)67 do extend to coverings by all seven ET-type families; and independently of
that, all of them are true as stated, since they say \"linear\" (checked: SP Thm 3.1, SS Thms 3.1, 5.2, 7.3, 8.1, OA Thm 2.2
all say \"no finite linear covering\"; DISCOVERIES/STATUS headline lines for (J)51/(J)56 say \"linear\" too).

**\u00a73.4 (Assessment: robustness by naive double counting)** \u2014 arithmetic re-checked (3.195 + 1.01\u00b70.1705 = 3.367 < 4;
3.577 + 1.01\u00b70.1750 = 3.754 < 8). Adding the full Case A mass over-counts the I4 mass at k = 1 (lc-2 Case A data have no I4
mirror), so it is conservative. Fine as Assessment; superseded by Thm 2.5 anyway.

## 2. Defects

(in progress)
