# Hostile review R40 of EXCEPTIONAL_SPW.md (branch side-agent/spw-proof, O40)

Reviewer branch: side-agent/review-spw. Reviewed commit: 5bc4f0d (merged).
Scripts (from scratch, no reuse of the author's code): `scripts/review_spw_*.py`.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Definition match with IF2 §9 | MATCH (Thm 3.2 even refutes the weaker (P1)+(P2)) |
| Thm 3.2 (σ ≲_C (log N)^{−1/2}) | **SOUND** (D2, D3 minor) |
| exact certificates N=300 / N=1150 | **SOUND** — 72/185 reproduced exactly; 0.3811325 independently |
| Cor 3.3 | **SOUND** |
| Lemma 1.4 (weak SPW suffices) | **SOUND** (D4 minor: "quasi-polynomial" should be N^{o(1)}) |
| Lemma 1.1, 1.2, 1.3 | **SOUND** (D1: Note superseded by Thm 3.2) |
| §2: Lemma 2.1, 2.2, Prop 2.3, exact A(N) values | **SOUND** (D5, D6 minor); A(150..400) reproduced |

**Overall: SOUND-AFTER-MINOR-REPAIRS.** The headline (fixed-σ SPW of IF2 §9 is
false for every fixed C, σ at large N; certified σ ≤ 72/185 < 2/5 at N = 300)
stands. No FATAL/MAJOR defect. Weak SPW remains open, as the author says.

Not re-checked (all labelled EVIDENCE by the author): HL LP h = 0.1889 at D = 10;
Monte-Carlo ratios of §2; local LP values at N ≥ 3300. No external source is
cited by the new results (Bernstein's inequality and Fejér's kernel are
standard and were re-derived). Process note: `git merge --ff-only
side-agent/spw-proof` was impossible (main had moved); I used a plain merge
into my review branch.

## Per-claim notes

### Definition match (SPW vs IF2 §9)
IF2 §9 (lines 422–428): (P1) exact profile mod every d ≤ N/2; (P2) R(s) ≤ 1 − σ
for every class of modulus d > CN; (P3) |R(s) − c(s)| ≤ Δ₀ for N/2 < d ≤ CN;
R ≥ 0 summable on ℤ. EXCEPTIONAL_SPW.md uses D = ⌊N/2⌋ (same set of d), the
same strict inequality d > CN and the same normalisation 1 − σ. Thm 3.2 and
Lemma 3.1 use only (P1)–(P2), so they refute a *weaker* hypothesis than SPW —
a fortiori SPW. **MATCH.**

### Theorem 3.2 — re-derived line by line
1. *Projection.* ρ(x) = Σ_{y≡x (e)} R(y) ≥ 0. Points of ℤ/e are classes of
   modulus e > CN, so ρ ≤ 1 − σ by (P2). For d | e, class sums of ρ mod d are
   R(b mod d) = c(b,d), which are the class sums of 1_W (W = {1..N} ⊂ ℤ/e,
   e > N). ✔
2. *Pinning.* Class sums mod d | e determine ρ̂(k) exactly for (e/d) | k;
   ∃ d | e, d ≤ D, with (e/d) | k ⟺ gcd(k,e) ≥ e/D (take e/d = gcd(k,e)).
   I verified the converse too (the profile span contains *no other*
   character) numerically on 7 (e, D) pairs by SVD rank
   (`review_spw_basic.py` (b)). For m₀ ≤ |k| ≤ M, |k| | L_M | e so
   gcd(k,e) = |k| ≥ m₀ = e/D. ✔ (M < e/2, so representatives are unique.)
3. *m₀ bound.* e < CN + L_M ≤ (C+1)N, m₀ = e/D ≤ (C+1)(2D+1)/D ≤ 2C+3 once
   D ≥ C+1. ✔
4. *Fejér.* K = (1/(e(M+1)))·(sin(π(M+1)x/e)/sin(πx/e))² ≥ 0, ΣK = 1,
   K(x) ≤ e/(4(M+1)x²) from sin(πx/e) ≥ 2|x|/e on |x| ≤ e/2; two-sided tail
   ≤ 2·e/(4(M+1))·Σ_{t≥a}t^{−2} ≤ e/(2(M+1)(a−1)). All checked numerically
   for 4 (e, M) pairs, every x and every a (`review_spw_basic.py` (c)). ✔
5. *Degree.* T̂ = K̂·f̂ vanishes for |k| > M (Fejér) and for m₀ ≤ |k| ≤ M
   (pinning), so T is the sample of a real trig polynomial of degree
   n ≤ ⌈m₀⌉ − 1 < m₀ (real because f real, K even). ✔
6. *Sup bound.* K∗ρ ∈ [0, 1−σ], φ ∈ [0,1] ⇒ T ∈ [−1, 1−σ] on samples. With
   period-1 variable θ, ‖T′‖ ≤ 2πn‖T‖; nearest sample within 1/(2e) ⇒
   ‖T‖ ≤ 1/(1 − πn/e) ≤ 1/(1 − πm₀/e). ✔
7. *Edge tails.* The set {x_in − y : y ∉ W} is the arc [r+1, e−N+r] of ℤ/e,
   i.e. one-sided runs starting at distance r+1 and N−r ≥ r+2; the set
   {x_out − y : y ∈ W} is the arc [−r−N, −r−1], i.e. runs starting at r+1
   and e−N−r > (C−1)N − r ≥ r+1 (needs 2r+1 < (C−1)N, which is the stated
   range). Each side is a *one-sided* tail ≤ e/(4(M+1)r); the author's
   two-sided bound e/(2(M+1)r) is valid (slightly wasteful). ✔
8. *Jump + Bernstein.* T(x_in) ≤ −σ + ε, T(x_out) ≥ −ε, ε = e/(2(M+1)r);
   |θ_out − θ_in| = (2r+1)/e. Gives σ ≤ e/((M+1)r) + 2πm₀(2r+1)/(e − πm₀). ✔
9. *Optimisation.* a/r + b r with a = e/(M+1), b = 4πm₀/e: at
   r = √(a/b) = e/√(4πm₀(M+1)) each term is √(ab) = 2√(πm₀/(M+1)); total
   4√(πm₀/(M+1)) plus O(m₀/e) and rounding. r ≍ N/√M = o(N), admissible for
   fixed C > 1 once √M ≫ (C+1)/(C−1). ✔
10. *M ≍ log N.* L_M = e^{ψ(M)}, ψ(M) ~ M, so the largest M with L_M ≤ N is
   ~ log N. Hence σ ≤ (4√(π(2C+3)) + o(1))·(log N)^{−1/2}. ✔

**Verdict Thm 3.2: SOUND.** Uniformity: the constant is explicit in C
(≍ √C), N₀ depends on C through the admissibility √M ≫ (C+1)/(C−1) and
D ≥ C+1 only. No circularity; no use of (P3). The theorem is correctly
labelled PROVED. (Minor presentation points: D6, D7 below.)

### Exact local certificates (§3)
Rebuilt from scratch (`scripts/review_spw_cert.py`): my own dual LP on ℤ/e
(variables a_{d,b} on classes mod d | e, d ≤ D, and z ≥ 0 on classes mod
e′ | e, e′ > CN, Σz = 1, z-cover ≥ g pointwise, maximise Σ_{n≤N} g(n)),
solved with HiGHS, coefficients rounded to rationals, then **the bound
1 − Σ_W g / Σ z recomputed in exact `Fraction` arithmetic** with the cover
re-derived exactly (for e = 630, 2310 the only divisor > CN is e itself, so the
optimal cover is z = g⁺). Logic re-checked: for any R with (P1)–(P2),
Σ_{n≤N} g(n) = Σ a_{d,b} c(b,d) = ⟨g,R⟩ ≤ ⟨g⁺,ρ⟩ ≤ (1−σ)Σg⁺. ✔

| N | e | my LP | my exact certificate | author |
|---|---|---|---|---|
| 300 | 630 | 0.389189 | **σ ≤ 72/185** (identical rational) | 72/185 |
| 1150 | 2310 | 0.381132 | σ ≤ 0.381132545 (rounded up; 3843-digit denominator) | 0.3811324… ≤ 0.381133 |

**Verdict: SOUND** (both reproduced independently; my N = 1150 rational differs
from the author's in the 8th digit only because of a different rounding of the
dual — both are valid upper bounds, and both lie below 0.381133). The LP
values at N = 3300, 4400, 9100 are labelled EVIDENCE and were not re-run.

### Corollary 3.3 (Flat margin)
Re-derived. Since e > CN > N, every class mod e meets [1,N] in ≤ 1 point, so
(F1) gives F_e ≤ 1 on W, ≤ 0 off W; (F3)/(F4) at modulus e give
F_e ≥ M_F/e + s₀ on W, ≥ M_F/e − 1 off W (this also forces s₀ ≤ 1, used
implicitly). ρ := 1_W − F_e + M_F/e then lies in [M_F/e, 1−s₀] on W and
[M_F/e, 1] off W, and its profile mod d | e, d ≤ D is that of 1_W because
the constant M_F/e has class sums M_F/d = those of F_e by (F2). K∗ρ(x_in) ≤
1 − s₀φ(x_in) ⇒ T(x_in) ≤ (1−φ) − s₀φ ≤ −s₀ + ε(1+s₀) ≤ −s₀ + 2ε;
T(x_out) ≥ −ε; T ∈ [−1, 1]. So s₀ ≤ 3ε + Bernstein term; with the r of
Thm 3.2 this is 3√(πm₀/(M+1)) + 2√(πm₀/(M+1)) = 5√(…) ≤ 6√(…)
(re-optimising r gives 2√(6πm₀/(M+1)) ≈ 4.9√(…)). Needs t ≥ 0 (stated).
**Verdict: SOUND.**

### Lemma 1.4 (weak SPW suffices for IF2 Thm 5.2)
Checked against IF2 Thm 5.2 (lines 253–291) and Prop 9.1 (lines 433–461).
(1) Thm 5.2 hypotheses: t, 1/Δ ≥ e^{−S_A}, s₀ ≥ N^{−A₁}; conclusion
log(N/B) ≤ S′ + log((1+Δ(1+c))/t), so with t ≥ e^{−S_A}, Δ ≤ e^{S_A} the cap
is S′ + O(S_A) — still (log N)^{3/4}(log log N)^{3/4}. ✔ (2) Prop 9.1 with
σ small: θ = σ/(2(σ+τ+1/(2C))) ≥ σ/(2(1+τ+1/(2C))), t = θ/2, s₀ = σ/2,
Δ = 6θ + Δ₀ ≤ 3 + Δ₀; nothing in its proof needs σ bounded below. So
σ_N ≥ c₀e^{−S_A} with c₀ = 4(1+τ+1/(2C)) gives t ≥ e^{−S_A}, and
s₀ = σ_N/2 ≥ N^{−A₁} for large N because S_A = o(log N). ✔ (3) The
mixing step R := (1 − 1/(2K))λ_N + R′/(2K): (P1) by linearity; a class of
modulus > CN > N has λ_N-mass 1 iff it meets [1,N], else 0; so full classes
get ≤ 1 − η/(2K), sparse ones ≤ K/(2K) = 1/2; (P3) deviation scales by
1/(2K). ✔ (σ = min(η/(2K), 1/2) = η/(2K) since η ≤ 1 ≤ K.)
**Verdict: SOUND** as a PROVED implication; the conclusion — Thm 5.2 is not
refuted, only the fixed-σ route — is correct. Caveat (D3): the label in the
§0 table and §4 should say explicitly that the *constants* in the cap of
Thm 5.2 then grow (cap S′ + O(S_A)), and that Δ_N ≤ e^{S_A}/2 must be read
with S_A for the *same* A.

### §2 BDW
* **Lemma 2.1** re-derived: R(s) ≤ (KQ′/e + 1)·AN/(KQ′) ≤ AN/e + AN/(KQ′); the
  author writes N/K for the last term, valid once K ≥ A (harmless). Medium
  classes: R(s) ≤ AN/(D+1) < 2A, c(s) < 3, so Δ₀ = 2A + 2 works (A ≥ 1). SOUND.
* **Lemma 2.2** (Farkas for an affine slice of a box): SOUND.
* A*(N) = 3/2 − 3/N for every even N ∈ [12, 60] by exact enumeration
  (`review_spw_basic.py` (d)).
* LP optimum = A*(N): my own LP on ℤ/L₀ (`review_spw_bdwlp.py`) gives exactly
  1.25, 1.2857, 1.3125, 1.3333, 1.35 at N = 12, 14, 16, 18, 20. EVIDENCE confirmed.
* **Prop 2.3** re-derived: window side Σ_n dE_d(n) = dΣ_bE_d² = r_d(d − r_d);
  conditional expectation E[dE_d | x mod g₀] = g₀E_{g₀} and CRT independence
  ⇒ E[dE_d·d′E_{d′}] = r_{g₀}(g₀ − r_{g₀}). Brute-force verified on ℤ/L₀ for
  N = 12, 14, 16, 18 for all pairs d, d′ (`review_spw_bdw.py` (i)). The
  window-side sum over d = D − k, k < (D−1)/3 gives D³/27 − O(D²); E g² ≤ D³/4;
  ratio 4D^{3/2}/(27N) → 0.0524√N, so "c = 0.05 for N ≥ N₀" is right.
  Exact values recomputed from scratch with exact rational comparison of
  squares: A(150) ≥ 1.5514, A(200) ≥ 1.7730, A(300) ≥ 2.2009, A(400) ≥ 2.4965
  (rounded down) — match the author's 1.551, 1.773, 2.200, 2.496. **SOUND.**
* The Assessment "any SPW measure has relative density ≳ √N somewhere on ℤ/L₀"
  is in fact PROVED (project R to ℤ/L₀; the projection has the window profile,
  so max ≥ A(N)·N/L₀). Could be upgraded (D5).

### Lemmas 1.1–1.3
* **1.1** (b) re-derived: for e ∤ Q′, g = gcd(e,Q′) < e, the k-orbit visits each
  residue of s mod g in ℤ/Q′ once per Q′/g steps, so R(s) ≤ (g/e + 1/K)ρ(s mod g);
  g ≤ D uses (P1), D < g ≤ CN uses (P3), g > CN uses (P2) with g/e ≤ 1/2.
  (N + (2+Δ₀)CN)/T ≤ 1/2 ✔. SOUND (the §0 "⟺" is an equivalence only up to
  ε and the clip at 1/2, as the parenthesis says).
* **1.2** SOUND (∂ shifts profiles by b ↦ b − 1; ∂λ_N = δ₁ − δ_{N+1}).
* **1.3** (i) and the reflection identity {(−y−1)/d} = 1 − 1/d − {y/d} verified
  exhaustively in exact arithmetic (N < 40, d < 45, |b| < 50;
  `review_spw_basic.py` (a)); κ_d = N/d recomputed by hand; (P2)/(P3)
  bookkeeping ✔ (U(s) ≤ (N−2m)/e + (N−2m)/J). SOUND. The Note's deduction
  h ≥ 0.175 is correct but now superseded (D1).

## Defects

No FATAL or MAJOR defects found. All MINOR:

**D1 (MINOR; Lemma 1.3 Notes, "forces h ≥ 0.175", "HL depends on N only
through D and E₀").** Combined with Thm 3.2, Lemma 1.3 gives much more: for
E₀ = CN, 1 − (N−2m)/(CN) − 2h ≤ σ*(N) → 0 with m ≥ (D−1)/2, so the HL optimum
satisfies h ≥ 1/2 − 1/(4C) − o(1) (= 3/8 at C = 2) as D → ∞. The D = 10
value h = 0.1889 is a small-D artefact of the same kind as §2's BDW lesson.
*Repair:* add this remark; say HL with h bounded below 1/2 − 1/(4C) is false
for large D, so HL can serve only weak SPW.

**D2 (MINOR; Thm 3.2 Remark (ii), "it needs log N ≫ 50/σ²").** The bound is
< σ only when M + 1 > 16πm₀/σ² with m₀ = e/D ≥ 2C, i.e. M ≳ 200/σ² at C = 2
(M ≈ log N). *Repair:* "log N ≳ 16πm₀/σ² ≈ 200/σ² at C = 2".

**D3 (MINOR; Thm 3.2 statement).** The (1 + o(1)) hides the admissibility
condition 2r + 1 < (C−1)N (needs √M ≫ (C+1)/(C−1)) and the O(m₀/e) terms.
*Repair:* state the fully explicit inequality actually proved,
σ ≤ e/((M+1)r) + 2πm₀(2r+1)/(e − πm₀) for every integer 1 ≤ r <
min(N−1, (C−1)N−1)/2, then the asymptotic; this makes the C-dependence visible.

**D4 (MINOR; §0 table and §1 Lemma 1.4, Remark (iii)).** "quasi-polynomially
small / large" is a misnomer: e^{±S_A} = e^{±O((log N)^{3/4}(log log N)^{3/4})}
= N^{±o(1)}, i.e. *sub-polynomial*. "Quasi-polynomial" is usually read as
e^{(log N)^{O(1)}}, e.g. e^{(log N)²}, which Thm 5.2 does **not** tolerate.
*Repair:* write "N^{o(1)} (precisely ≥ c₀e^{−S_A})". Also say that the resulting
cap is S′ + O(S_A) (constants grow), not Thm 5.2's constant.

**D5 (MINOR; §2 Consequence).** "any SPW measure must have relative density
≳ √N somewhere on ℤ/L₀" is labelled Assessment but is PROVED by Prop 2.3
(the projection of R to ℤ/L₀ has the window profile). *Repair:* relabel.

**D6 (MINOR; Lemma 2.1 proof).** The last term is AN/(KQ′); bounding it by N/K
needs A ≤ Q′ (true; say so). Cosmetic.

**Ledger note (not an author defect).** IF2 §9's Assessment "suggests
SPW(2, 2/5 − ε, O(1)) holds for all N" and the bold sentence after Prop 9.1
("SPW(C, σ, Δ₀) with fixed C, σ > 0 … implies the 3/4 cap") are now a vacuous
implication. IF2 and ledger (D)26 should point to weak SPW (EXCEPTIONAL_SPW
Lemma 1.4) and mark fixed-σ SPW as refuted (Thm 3.2).
