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

## 2. Defects

(in progress)
