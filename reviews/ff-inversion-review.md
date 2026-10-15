# R250 — hostile review of FF_INVERSION_CHECK.md (O244)

Reviewer: R250 (side-agent/review-ff-inversion). Reviewed: FF_INVERSION_CHECK.md at side-agent/ff-inversion cbda85ab, report
reviews/agent-reports/AGENT_REPORT_O244.md. Background checked: FUNCTIONFIELD_ES.md §1, §6.2 (Lemmas 1.2, 1.3, 6.2),
FUNCTIONFIELD_ES2.md §0.1–0.2, FUNCTIONFIELD_ES3.md Lemmas 1.1, 1.2, 2.1, FF_STERILE_PUSH Thm 3.1, FF_STERILE_SMALL §§3, 5–8
(Prop 6.1, Lemma 7.2, Thms 3.1, 5.2, 7.3, 8.1), FF_ODD_ABSENCE Thm 2.2, and Elsholtz–Tao arXiv 1107.1010
(sources/elsholtz-tao-1107.1010.pdf: Prop 1.9, §2 Props 2.2, 2.6, identities (2.1)–(2.21)).
From-scratch scripts: `scripts/review_r250_*.py` (own GF(q) arithmetic; nothing imported from `zi_*`).

**Repairs applied** (author idle since the checkpoint; all marked "(R250 repair)"): m-1 (definition of ET-type family / O_ET,
after Thm 2.5's statement), m-3 (Cor 1.3, dictionary = inclusion of validity sets), m-4 (deg e ≥ 1 in Thm 2.5's proof) in
FF_INVERSION_CHECK.md; m-2/m-5 (ledger wording, list of lines lacking "linear") in AGENT_REPORT_O244.md. m-5's two lines on
main (SYNTHESIS_SPARKS3.md:119, STATUS.md:52) are for the parent. m-6 optional, not applied.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (ET parametrisation over F_q[T]) | SOUND (brute force, 7+2 cases, sets equal) |
| Lemma 1.2 (X, E_FF; deg a ≠ deg b in Type I) | SOUND |
| Cor 1.3 (ET dictionary; linear = II1, II3, I1, I2, I3) | SOUND-AFTER-REPAIRS (m-3, wording) |
| Prop 1.4 (I4 congruence families, example, counterexample) | SOUND |
| Remark 1.5 (II2) | SOUND |
| Lemma 1.6 (3-bounded families) | SOUND (scope: m-2) |
| Lemma 2.1 (II2 never valid on a slice) | SOUND |
| Lemma 2.2 (I4 at u ⇒ Case A at 1/u) | SOUND (m-4) |
| Lemma 2.3 (Case A ball ⊆ same-E Case B ball, α + v ≥ k) | SOUND (re-proved; brute force incl. end-to-end solutions with prime P) |
| Lemma 2.4 (Case B inversion-closed) | SOUND |
| Thm 2.5 (incl. the k ≥ 3 reduction to level 2) | SOUND-AFTER-REPAIRS (m-1 definition of O_ET, m-4) |
| Cor 2.6 ((J)51, (J)56, (J)67, Conj 0.2 hold for all ET-type coverings, same constants) | SOUND-AFTER-REPAIRS (m-1: "⟺" for Conj 0.2 needs the defined O_ET) |
| §3 computations | reproduced from scratch; depth-9 tree identical in every number |

**Bottom line.** No FATAL, no MAJOR defect. The F_q[T] linear-family model does omit I4 and II2, and on the sterility slices
both are dominated by Case B exactly as claimed; the k ≥ 3 reduction is sound. The PROVED theorems (J)51, (J)56, (J)67 are true as
stated (they say "linear") and also for coverings by linear ∪ I4 ∪ II2 families, with the same constants. Not addressed (and
not claimed): coverings by polynomial families outside ET's seven types, and I4/II2 coverage off the slices (global O(q, A)).

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

**Lemma 2.1 (II2 never valid on a slice) — SOUND.** f = T^k acd − 1 ≡ −1 (mod T), so P ≡ 1 (mod f) at x_u and validity
becomes f | a + c; a + c ≠ 0 (monic, q odd) and deg(a + c) ≤ max(deg a, deg c) < deg f. Holds for every A with T | A (or any A
at the point x ≡ 1).

**Lemma 2.2 (I4 at u ⇒ Case A at 1/u) — SOUND.** T^{k+j} | u⁻¹ + e ⇔ T^{k+j} | 1 + ue; lcm(a, b)' | (ab)' | e + 1; types (0, 0):
s = a + b, lc(s) = 1 = lc(e) since deg a ≠ deg b and e is monic (forced in Type I). One unstated point: E = e has positive degree
on every slice used (e constant monic means e = 1, centre u ≡ −1, which is on no c-slice and has u₀ = −1 ∈ F₃^*), so Lemma 2.3's
"deg E ≥ 1" is satisfied (MINOR m-4).

**Lemma 2.3 (Case A ball ⊆ Case B ball with the same E) — SOUND.** Re-proved line by line: H monic T-free; E ≡ −1 mod
g'(a1b1)' gives a1'b1 | H (coprime factors), so L' = H/b1 is T-free with a1' | L'; mod E: T^vH ≡ 1, b1 ≡ −T^αa1' and b1 is a
unit (b1 | E + 1), so T^sL'a1' ≡ −1; D = 1 + T^sL'a1' monic; s = k + j + γ with 0 ≤ γ ≤ j needs exactly s ≥ k; j ≤ α ≤ j_A needs
exactly v ≤ k + α. The Case B family (E; 0, T^γa1'; 2, T^jL') then satisfies FE3 Lemma 1.1(i) on the whole Case A ball (the
L'-condition is a condition on E only). Note the original g of the Case A family plays no role (its ball is only smaller).
*From-scratch checks* (`scripts/review_r250_domination.py`, log `data/review_r250/domination.txt`): every Case A datum with
g = 1 in the degree box, the Case B datum built and all conditions asserted; **plus an end-to-end check that does not use FE3
Lemma 1.1**: a polynomial P in the Case A ball (≡ 1 modulo all T-free moduli involved; with PRIME = 1 irreducible) is solved
explicitly by the Case A family and by the Lemma 2.3 Case B family, and a P' in the I4 ball by the I4 family and by the swapped
Case B family of Lemma 2.4 (monic denominators and the identity A·XYZ = P(XY + YZ + ZX) asserted):
| q, k, slices, D, DMAX | data (unordered, g = 1) | Lemma 2.3 hyp. hold | outside hyp. | 2.3/2.4/end-to-end OK |
|---|---|---|---|---|
| 3, 2, c, 6, 9 (P prime) | 16 | 16 | 0 | 16/16/16 |
| 9, 1, u₀ ∉ F₃^*, 2, 12 (P prime) | 6 | 6 | 0 | 6/6/6 |
| 9, 1, u₀ ∉ F₃^*, 3, 12 | 14 | 14 | 0 | 14/14/14 |
| 5, 2, c, 4, 12 (P prime) | 0 | — | — | — |
| 9, 2, c, 3, 12 | 2 | 2 | 0 | 2/2/2 |
| 3, 3, c, 6, 10 | 16 | 16 | 0 | 16/16/16 |
| 3, 2, all, 4, 9 | 30 | 26 | 4 | 26/26/26 |
| 5, 2, all, 3, 8 | 28 | 24 | 4 | 24/24/24 |
| 9, 2, all, 2, 8 | 12 | 8 | 4 | 8/8/8 |
| 3, 3, all, 4, 10 | 30 | 22 | 8 | 22/22/22 |
The author's counts are ordered pairs (32 = 2·16 etc.); mine agree. The "outside" data are all off-slice (v = 0, α < k), as
the author says. Observation: on the c-slices α ≥ 2 always (α = 1 forces b1 = 1, F = 1, E = Ta1' + 1, v_T(E + 1) = 0 ≠ 1), so
Lemma 2.3 applies directly at k = 3 as well (row 3, 3, c); not needed by the document.

**Lemma 2.4 (Case B inversion-closed) — SOUND.** EE' = D ≡ 1 mod T^s, s ≥ k + j; D ≡ 1 and E ≡ −1 mod L' give E' ≡ −1; E'
monic divides D; E' is non-constant (E' = 1 would give −1/w ≡ 1). Checked in all rows above, including end-to-end.

**Theorem 2.5 — SOUND (MINOR wording m-1, m-4).** (i) k = 2: at 1/u (the (−c)-slice) FE2 §0.2 step (1) uses only
E + 1 ≡ −c'T (mod T^{k+j}), k + j ≥ 2, E | a1 + b1, E ≡ −1 mod L' — all available for F^A (with its own g) — and gives α ≥ 1,
T ∤ b1, v = 1; Lemma 2.3 then 2.4. (ii) k = 1: SS Lemma 7.2(a) (re-read; it covers lc(E) ∈ {1, 2}, and its "neither divisible\nby T" branch is Prop 6.1's argument, which forces E constant ∈ {1, 2}, i.e. u₀ ∈ F₃^*) gives α ≥ 1 at 1/u; v = 0 because
e(0) = −1/u₀ ≠ −1. **k ≥ 3 reduction — SOUND**, re-derived: (a) a level-k linear family valid at x_u is valid at level 2 with
the same data: the T-adic condition T^{k+j} | u + E implies T^{2+j} | u + E; E | a0 + b0 (Case A) and lc(s) are k-independent
(lc(s) ∈ {1, lc(a0 + b0), lc(L/a0 + L/b0)}); (b) Case B: D = 1 + T^{k+j+γ}L'g' is the level-2 D with j₂ = j + k − 2, γ₂ = γ ≤ j₂,
same ball; (c) I4: T^{k+v_T(ab)} | ue + 1 implies the level-2 condition, the other hypotheses are k-free; (d) II2: Lemma 2.1 for
every k. So covered_k(ET) ∩ Σ ⊆ covered_2(linear ∪ I4) ∩ Σ = covered_2(linear) ∩ Σ. That every k ≥ 2 theorem in question
(SP Thm 3.1, SS Thms 3.1, 5.2) is proved by certifying the level-2 union bound ("take k = 2") I checked in each proof; the
same (a)–(b) argument is in fact the rigorous form of SP's one-line justification "N(s) and the Case A exponent only grow
with k". No theorem in the list is k ≥ 3-only, so O(q, T²) ∩ Σ always has the certified positive measure.

**Corollary 2.6 — SOUND** for (J)51 (SP Thm 3.1), (J)56 (SS Thms 3.1, 5.2, 7.3, 8.1 incl. Lemma 7.4) and (J)67 (OA Thm 2.2,
whose slices P₈ ⊂ {u₀ ∉ F₃^*}, inversion-closed, k = 1), and for Conjecture 0.2 (k = 2, x*_c on a c-slice) in the direction
x*_c ∈ O ⇒ x*_c ∈ O_ET (the ⇐ direction needs m-1). The O140 Prop 4.1 remark (x ≡ 1: I4 needs Aab | e + 1 with
deg e ≤ max(deg a, deg b) < deg Aab, so e = −1, not monic; II2 needs f | a + c) is right for every A. "Same certified
constants" is right: for k ≤ 2 the ET-covered and linear-covered parts of Σ coincide; for k ≥ 3 the ET-covered part is inside
the level-2 linear-covered part, which is what the certificates bound. The "Case A terms with monic E are redundant" side
remark is right (the containing Case B balls are terms of the Case B sum). **Answer to the brief's stakes question:** the
domination argument is correct, so (J)51, (J)56, (J)67 do extend to coverings by all seven ET-type families; and independently of
that, all of them are true as stated, since they say "linear" (checked: SP Thm 3.1, SS Thms 3.1, 5.2, 7.3, 8.1, OA Thm 2.2
all say "no finite linear covering"; DISCOVERIES/STATUS headline lines for (J)51/(J)56 say "linear" too).

**§3.4 (Assessment: robustness by naive double counting)** — arithmetic re-checked (3.195 + 1.01·0.1705 = 3.367 < 4;
3.577 + 1.01·0.1750 = 3.754 < 8). Adding the full Case A mass over-counts the I4 mass at k = 1 (lc-2 Case A data have no I4
mirror), so it is conservative. Fine as Assessment; superseded by Thm 2.5 anyway.

## 2. Defects

No FATAL or MAJOR defect. The domination argument (Lemmas 2.1–2.4, Thm 2.5, Cor 2.6) is correct as written.

**m-1 (MINOR; Thm 2.5 last sentence, Cor 2.6 "Conjecture 0.2 (x*_c ∈ O ⟺ x*_c ∈ O_ET)", report item 2).** "ET-type family"
and O_ET are never defined. Thm 2.5's parenthesis "(linear, I4 or II2)" suggests ET-type := every linear family ∪ I4 ∪ II2; then
O_ET ⊆ O is trivial and "O_ET ∩ Σ = O ∩ Σ" holds. If instead it means the seven ET types *literally* (I1–I3, II1, II3 as
specific linear families, plus I4, II2), only O_ET ∩ Σ ⊇ O ∩ Σ is proved (Cor 1.3 gives ET-literal validity ⊆ linear validity,
not conversely: a general linear family, e.g. Case B (E; 0, T^γg'; 2, T^jL') with a0 ∤ b0, has ET parameters depending on P mod
something, so it is a finite union of ET-literal families at best, unproved). The no-covering theorems need only ⊇, so nothing
breaks. *Repair:* after Cor 1.3 add "Definition. An ET-type family is a linear family, an I4(a, b, e) or a II2(a, c, d) family;
O_ET(q, A) := {x : no ET-type family is valid at x}. (By Cor 1.3 this contains the seven ET types; the literal seven-type set
O_ET^{lit} satisfies O_ET^{lit} ⊇ O_ET.)" and in Cor 2.6 replace "⟺" by the defined O_ET.

**m-2 (MINOR; Lemma 1.6 scope, §4(1) "omits exactly two of the seven ET types", report ledger line).** "Exactly" is relative
to ET's list; the F_q[T] analogue of ET Prop 1.9's completeness half (every polynomially solvable class lies in one of the seven
families) is not proved, so the extension "no finite covering by ET-type families" must not be shortened to "no finite
covering". The document says this in the Scope note; the suggested ledger line should too. *Repair:* ledger line "... so
(J)51/(J)56/(J)67 hold for coverings by linear, I4 and II2 families (the seven ET types); coverings by other polynomial families
are not addressed. PROVED."

**m-3 (MINOR; Cor 1.3).** For II1, I2 (and II3, I1 when a | d etc.) the linear family's validity set is in general *larger*
than ET's class (A·lcm(a0, b0) | P + E versus A·a0·b0 | P + E). Harmless (it is the inclusion the argument uses), but "II1 =
(e; 0, b; 0, a)" reads as an equality of families. *Repair:* "II1 ⊆ (e; 0, b; 0, a) (validity sets; equality iff gcd(a, b) = 1)"
or one sentence saying the dictionary is an inclusion of validity sets.

**m-4 (MINOR; Thm 2.5 proof).** Lemma 2.3 needs deg E ≥ 1; for the I4 mirror E = e this is not stated. It holds on both slice
families (e = 1 would put the centre at u ≡ −1, off every c-slice, and u₀ = −1 ∈ F₃^*). *Repair:* add "(deg e ≥ 1, since
e = 1 forces u ≡ −1 mod T, which is in no slice of Σ)".

**m-5 (MINOR; wording elsewhere in the repo, the document's §2 "What is affected (2)").** The document asks that "no finite
covering" keep "linear" but lists no instances. Instances found by `git grep` (FF context, without "linear"):
SYNTHESIS_SPARKS3.md:119 ("ES_q ... has no finite covering for q = 3^r, r ≥ 27 ((J)26)") and STATUS.md:52 ("even where ES_q
itself has no finite covering"). All theorem statements ((J)51, (J)56, (J)67, FE §6.4, FE2 Conj 0.2) already say "linear".
*Repair (parent, on main):* insert "linear" (or "ET-type, Cor 2.6 of FF_INVERSION_CHECK") in those two lines.

**m-6 (MINOR, optional strengthening; Thm 2.5 k ≥ 3).** On c-slices α ≥ 2 always (α = 1 forces b1 = 1, F = 1, E = Ta1' + 1,
v_T(E + 1) = 0), so Lemma 2.3 applies directly at k = 3 (confirmed: row q = 3, k = 3, c in §1). Not needed given the level-2
reduction; mention only if useful.

## 3. Computations reproduced from scratch (EVIDENCE)

* **§3.1 rows** (`review_r250_lemma11.py`, naive solution loop, not the divisor method): q = 9, k = 2, n = 3, P(0) = 1: 30 primes,
  Type I 2 / Type II 4, 1 with deg E_FF ≥ n/2, 25 primes without solution — identical to the author's row; q = 5, k = 2, n = 4,
  P ≡ 1 + T: 7 primes, 4 / 0, 4, 4 — identical. Rows q = 3, n = 6, 7 and q = 9, k = 1, n = 3 not reproduced (too slow for a
  naive loop); replaced by the other cases in §1 (all primes of the degree, 1,068 solutions + these).
* **§3.2 depth-9 tree** (`review_r250_tree.py 3 9`, log `data/review_r250/tree_q3_d9.txt`; own complete enumerations, the
  completeness arguments are in the script docstring: Case A via a1'(Kb1F − T^α) = F + b1 with deg b1, deg F ≤ α − 1; Case B via
  m'wC = T^s + v, w + C = g'v, v = (−T^s) mod wC, s ≤ 16): Case A 26 balls, Case B 148, I4 26, |A ∩ B| = 2; balls without an
  inverse ball: A 26, B 0, I4 26, A + B 24, **A + B + I4 0**; every A ball and every I4 ball lies in a Case B ball (26/26, 26/26);
  survivors per c-slice at depths 3–9: 2, 6, 16, 44, 130, 380, 1130 with and without I4; x*_c alive. **Identical to
  `data/zi/tree_d9.txt` in every number.**
* **q = 5, A = T², depth ≤ 6** (`review_r250_tree.py 5 6`, `data/review_r250/tree_q5_d6.txt`): no Case A (hence no I4) balls on
  the c-slices, 42 Case B balls, all mirrored; survivors identical with and without I4 (consistent with the author's q = 5 row).
* **§3.3 table** — all rows reproduced up to the ordered/unordered factor 2 (§1 above, Lemma 2.3), plus end-to-end solutions.
* **Prop 1.4 example and the review counterexample** — `review_r250_example.py`: P irreducible, degrees 11, 4, 5,
  E_FF = T⁵ + T³ + 2T + 1; the I4(1, T, 1) class equals the validity class of (1; 0, T; 1, 1) on all primes of degree 5.

