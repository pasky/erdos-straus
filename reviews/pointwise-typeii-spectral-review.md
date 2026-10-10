# R128 — hostile review of O128 (`POINTWISE_TYPEII_SPECTRAL.md`)

Reviewer branch `side-agent/review-typeii-spec`; merged `side-agent/typeii-spectral` at review start.
From-scratch scripts: `scripts/review_t2s_*.py`. ET = `sources/elsholtz-tao-1107.1010.pdf` (read via pdftotext).

## Overall verdict

**No FATAL or MAJOR defects.** Every PROVED claim (Lemma 1.1, Prop 2.1, Lemma 2.2, Prop 2.4/2.5, Prop 3.1,
Lemma 6.1, Cor 6.2/6.3) was re-derived by hand and checked with from-scratch code; the §5 numerics were reproduced
exactly to 10⁷ by an independent sieve that was itself validated against a brute force for all n ≤ 2000. The negative
§4.4 conclusion is correctly labelled Assessment and the Young exponents (1/18, 1/6, 4/9, 1/3) check out against
the arXiv text. Eight MINOR defects (D1–D8): one counting misstatement (D3: the shell also contains non-primitive
points, ~18% extra), one hidden hypothesis (D4: genus phrasing needs p ≡ 1 mod 4), one misquoted ET average (D5), a
numerics filter artefact (D6), and wording/hypothesis caveats in the Assessment (D2, D7, D8). Nothing is claimed
toward ES, and nothing should be.

## Summary verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Lemma 1.1 parametrisations, duality table | SOUND (bijection verified); MINOR wording defects D1, D2 |
| 2 | Prop 2.1 / Lemma 2.2 Heegner + separation | SOUND (bound has slack: min cosh = 3 observed) |
| 3 | Prop 2.4 / 2.5 exact incidence | SOUND-AFTER-REPAIRS (D3: shell also contains non-primitive points) |
| 4 | §3 averaged check, constant 0.05 | SOUND (constant correctly labelled Assessment); D5 misquote of ET |
| 5 | §4.4 gap (Young bookkeeping) | SOUND as Assessment (exponents verified against arXiv 1405.5457); D7 hypotheses of Young not met, D8 overstated slogan |
| 6 | Lemma 6.1 / Cor 6.2 / 6.3 genus | SOUND as a statement about f; "equivalently genus χ_{−4d} = −1" needs p ≡ 1 (4) (D4) |
| 7 | §5 numerics | SOUND (reproduced exactly to 10⁷); D6 R-trend partly a filter artefact; predictor not re-run |

## Defects

(numbered below as found)

- **D1 (MINOR)** §1 proof of (1⇔5): "`e ≤ a+b < 4ab` unless a = b = 1 (then e ∈ {1,2} < 4)". The exception is
  spurious: `4ab − a − b = a(4b−1) − b ≥ 3b − 1 > 0` always. Repair: delete the parenthetical.
- **D2 (MINOR, wording)** §0/§1 "ET's dilation Σᴵ → Σᴵᴵ read on the SL₂ side". Under `(e,f,d) ↦ (n²e, f/n, dn)`
  the Type I det-1 identity `ef − 4a²d = 1` goes to the Type II **det-n** identity `ef − 4a²d = n` (form 2), not
  to the SL₂ identity `ff' − 4c²dn = 1`; the latter is the image of Type I's det-n² identity
  `f·(4bcd − n) − 4c²d = n²`. So the two rows of the table are not dilation images of each other; they are
  different identities with different variable roles (a,e vs c,f'). Repair: say "the dilation exchanges which
  identity is unimodular: Type I is det 1 in (a,e,f) and det n² in (c,f,f'); Type II is det n in (a,e,f) and det 1
  in (c,f,f')". The slogan "p moves into the level" is a description, not a theorem.
- **D3 (MINOR)** Prop 2.5, last sentence: the shell `T_c` Heegner points (disc −4dp, `B ≡ 0 (4d)`, `d | C`,
  `A − cB = −1`) are the solutions of form 2 **without** the condition gcd(a,c) = 1. Non-primitive points
  exist and are common: e.g. p = 29, (a,c,d) = (2,2,1), f = 15, e = 3, b = 4 — the dilation image of the primitive
  solution (1,2,1,4). From scratch: 383 non-primitive shell incidences vs 2086 primitive ones for p < 600 (~18%).
  So "exactly the Type II points with this c (and d)" is false; each non-primitive point is a Type II solution
  with (c/g, g²d), so existence is unaffected, but every count (§4.2, (TS) counting version) is an overcount
  by a factor ≈ 1/P(gcd(a,c)=1). Repair: add "with gcd(B/4d, c) = 1" or state the count is of the
  non-primitive family Σ_g f_II-type with d ↦ d/g².
- **D4 (MINOR)** Lemma 6.1 "Equivalently the Type II Heegner forms … lie in the genus 𝔊⁻_d = {χ_{−4d}(Q) = −1}",
  and §6(ii) (factorisation into `L(·,χ_{−4d})L(·,χ_p)`). χ_{−4d} is a genus character of discriminant −4dp only if
  `−4dp/(−4d) = p` is a discriminant, i.e. **p ≡ 1 (mod 4)**. For p ≡ 3 (4) it is not a class invariant: e.g. d = 1,
  the principal form x² + py² represents 1 (χ_{−4} = +1) and p + 4 ≡ 3 (4) (χ_{−4} = −1). There the genus
  character is χ_{−p}, and the lemma reads χ_{−p}(f) = (f/p) = +1; the factorisation is `L(χ_{−p})L(χ_{4d})`.
  The arithmetic statement `(p/f) = −1` is correct for all p. Repair: add "for p ≡ 1 (mod 4)" (the only case that
  matters for ES) to the genus phrasing, Cor 6.2's genus remark and §6(ii).
- **D5 (MINOR)** §3: "consistent with ET, who get ≍ N log³N for Type II". ET Thm 1.1 gives `Σ_{n≤N} f_II(n) ≍ N log³N`
  over all n, but `Σ_{p≤N} f_II(p) ≍ N log²N` over primes — the sum in Prop 3.1. (Both say average f_II(p) ≍ log³p.)
  Repair: quote the prime version.
- **D6 (MINOR)** §5: "min R = 0.43 (2¹⁶), 0.31 (2²⁰), 0.28 (2²³) … slowly widening". `t2s_numerics.py` silently
  drops classes with < 30 members, which at k = 16 (≈ 30 primes per class mod 840) removes many primes. Without
  the filter min R at k = 16 is **0.333** (p = 76441), so the trend is 0.33 → 0.31 → 0.30 → 0.28: much flatter
  than stated. Repair: state the ≥ 30 filter, or quote unfiltered values; soften "widening".
- **D7 (MINOR, hidden hypotheses in an Assessment)** §4.4 applies Young Thm 2.1 to discriminant −4dp with the
  level data `B ≡ 0 (4d)`, `d | C`, and to shells along the cuspidal geodesic γ_c. Young's theorem needs −D **odd
  fundamental**, level 1, full class group, and φ **compactly supported** on SL₂(ℤ)\H. −4dp is even (fundamental
  only if dp ≡ 1, 2 mod 4 squarefree); the level data is a congruence-subgroup (level ≍ 4d) restriction, i.e. a
  sum over part of 𝓕_{dp}, not Λ_D; and the shell periodised to Γ\H runs up the cusp to height ≍ √(dp)/(4cd) ≫ 1
  (a = 1 end). None of these weakens the negative conclusion (each makes the available theorem worse), but the text
  should say "heuristic bookkeeping with Young's error shape, under the (unproved) assumption that it extends to
  even, non-fundamental discriminants with level-4d data and non-compact shells".
- **D8 (MINOR, overstatement)** §4.4 last sentence / §0 "the obstruction is the exact-incidence nature …, not the
  strength of subconvexity". The same paragraph admits that pointwise square-root cancellation of the Weyl sums
  (error ≈ (h·area)^{1/2}) would suffice. So the correct statement is: at Sobolev scale V = |D|^{1/2} the spectral
  sum has ≍ V² = |D| terms and needs cancellation **among** the Weyl sums far beyond GLH (which bounds them only
  individually); "exact incidence" is the reason GLH-strength input is insufficient, not a proof that no
  L-function input could work. Repair: replace "not the strength of subconvexity" by "not merely the exponent of
  subconvexity: any spectral route needs cancellation across ≍ |D| spectral terms, beyond GLH" (Assessment).

### Claim 1 — Lemma 1.1 (five forms), duality

Re-derived from ET §2 (pdftotext of the PDF, eqs. (2.13)–(2.22), Prop 2.6, dilation (2.10)).
* Form 1 (ET Prop 2.6): ET give a *unique* sextuple with gcd(a,b,c)=1 and abd coprime to n; the converse
  (every such quadruple gives a Type II solution) is (2.22)+coprimality. For n = p prime p∤abd is automatic
  (else p | x, y, z and 4 = 1/x'+1/y'+1/z' ≤ 3). gcd(a,b,c) = gcd(a,c) since c | a+b. So form 1 is a
  **bijection** onto ordered Type II triples (both (y,z) orders; (a,b)↔(b,a) swaps y,z). Multiplicity 1:
  f_II(p) = #quadruples — no hidden factor.
* (1⇔3): `(4acd−1)(4bcd−1) − 1 = 4cd(4abcd − a − b) = 4c²dp` iff `4abcd = a+b+pc`; conversely
  `a = (f+1)/4cd, b = (f'+1)/4cd ≥ 1`. Bijection. (1⇔2): `4ad(ce − a) = p + e` shows b ≥ 1 automatically.
  (1⇔4) trivial. (1⇔5): e unique as least positive residue since `e ≤ a+b < 4ab`.
* **From-scratch check** (`scripts/review_t2s_brute.c`: sorted-triple enumeration + all distinct permutations,
  role assignment n∤x… gcd(x,n)=1, n|y,z — independent of every parametrisation; `scripts/review_t2s_param.py`:
  each form generates a triple set, every triple verified exactly with Fractions, no duplicates, count = brute):
  form 1 (with ET's gcd(abd,n)=1) agrees for **all 2 ≤ n ≤ 2000** (composites included; Σ f_II = 30610);
  forms 2, 3, 4, 5 agree for all primes 5 ≤ p ≤ 400. 0 mismatches. f_II(s²)=0 seen for odd squares ≤ 2000.
* Duality table: Type I `ef − 4a²d = 1`, `f = 4acd − n ≡ −n (4ad)` re-derived from ET (2.1),(2.2) ✓;
  Type I divisibility `(4acd−n) | (na+c)` ✓.

### Claim 2 — Prop 2.1, Lemma 2.2

Re-derived: disc[f, 4cdp, dpf'] = 16c²d²p² − 4dp·ff' = −4dp ✓; B ≡ 0 (2dp), C ≡ 0 (dp) ✓; root
`z = (−2cdp + i√(dp))/f`, `w = z/dp = (−2c + i/√(dp))/f` ✓; image conditions: `A ≡ −1 (mod B/p = 4cd)` forces
`f' ≡ −1` via `ff' ≡ 1` ✓. Separation: for Q, Q' in 𝓕_D, `(B−B')² ≡ 0 (4D²)`, `(A−A')(C−C') ≡ 0 (D)` so
`4D | disc(Q−Q')`, and `cosh d − 1 = disc(Q−Q')/(2·4D)` ✓ (verified numerically below).
From scratch (`scripts/review_t2s_geom.py`, primes p < 600, 2086 primitive points): min pairwise cosh over
same-(p,d) points = **3.000** (≥ 3/2 holds with slack: here B ≡ 0 (4D) and A ≡ −1 (4cd) give `8D | disc`);
in det-p coordinates `min (cosh−1)·2p = 4` (claimed ≥ 1). Separation is only asserted within fixed d — correct;
points with different d have different discriminants and no separation is claimed. Not checked: the
`#Λ_{dp} ≍ h·2^{O(ω)}` remark (inessential).

### Claim 3 — Prop 2.4, 2.5 (incidence)

Algebra re-derived: `f = 1/(Y√(dp))`, `c = −Xf/2`, `f + 1 = 4acd` ⟺ `X = −(1 + Y√(dp))/(2ad)` ✓ (Euclidean ray
from the real point −1/(2ad) ⇒ hypercycle of the vertical geodesic there ✓). Gram computation
`⟨(1,0),(1,−2c)⟩_Q = A − cB` ✓; `Q(x,y) = A|x − zy|²`, `A = √|D|/(2 Im z)` ⇒ `⟨u,v⟩ = √|D|(1 + 2c Re z)/(2 Im z)` ✓;
`sinh dist(z, {Re = x₀}) = |Re z − x₀|/Im z` ✓. For the det-p root `z = (−2ad + i√(dp))/f`:
`1 + 2c Re z = −1/f` ⇒ ⟨u,v⟩ = −1 exactly ✓. Numerically: max relative error 1e−11 over all 2086 points
(both Prop 2.4 ray and Prop 2.5 distance `arsinh(1/(c√|D|))`, left side).

### Claim 6 — Lemma 6.1, Cor 6.2, 6.3

Re-derived: `ef = p + 4a²d` ⇒ `(2ad)² ≡ −dp (mod f)`; gcd(d,f)=1 from `f ≡ −1 (4ad)`, p∤f since p | f ⇒ p | ad,
contradicting p∤x. So `(−dp/f) = 1`; `(−d/f) = (−4d/f)` and `m ↦ (−4d/m)` is a character mod 4d with value −1 at −1,
so `(−d/f) = −1` and `(p/f) = −1` ✓; f' by the a↔b symmetry (ET (2.17)) ✓. For n = s² the same argument needs
only gcd(n,f)=1, which follows from gcd(abd,n)=1 ✓, giving f_II(s²) = 0 — this is ET Prop 1.6 Type II (ET omit the
Type II details; the author's route via (2.19) is a valid fill-in). Cor 6.3 is immediate from multiplicativity
of the Jacobi symbol ✓. From scratch (`scripts/review_t2s_genus.py`): 29678 moduli f, f' for primes p < 3000,
0 violations; brute force (`review_t2s_brute.c`) gives f_II(s²) = 0 for every odd square ≤ 2000.

### Claim 4 — §3 averaged check

Prop 3.1 re-derived: for fixed (c,d,f), f ≡ −1 (4cd), gcd(f,2cd) = 1 and `f | 4c²dp+1` is one class mod f; f' ≡ −1
follows from ff' ≡ 1 (4cd); gcd(a,c) is p-independent ✓. Volume: ∫∫_{2α+δ≤1}(1−α−δ) = ½∫₀^{1/2}(1−2α)dα = 1/8 ✓;
`2·(1/4)·(1/8)·1.30·0.61 = 0.0496` ✓ (the 1/4 from f ≈ 4acd). Caveat (inside the Assessment): E[f/φ(f)] over
f ≡ −1 (mod 4acd) omits primes dividing acd, so 1.30 is slightly high; immaterial. My sieve gives block means
0.0779 (2¹⁶) / 0.0680 (2²³), matching the doc; a fit `0.05 + 0.29/log p` reproduces all three quoted means to ±0.008,
so "limit near 0.05" is a fair weak EVIDENCE statement. Moduli f reach ≍ c√(dN) > √N, so "BV/BT problem" is
meant in ET's sense (lower bound on a restricted range, BT for the upper bound) — fine as stated.

### Claim 7 — §5 numerics

From-scratch sieve `scripts/review_t2s_sieve.c` (form 4: AP in n for each (a,c,d), a ≤ b weighting — a different
loop structure from the author's (a,c,d,e) engine), validated **exactly against the brute force for all n ≤ 2000**
(composites included). Run to 10⁷ (10 s): `scripts/review_t2s_sieve.out.txt`. Every dyadic block reproduces the
author's min f_II, argmin, min f/log³p, argmin, #(d=1 empty), #(c=1 empty) exactly; means agree to ±0.0001.
f_II(p) ≥ 2 for all primes 5 ≤ p ≤ 10⁷ ✓. Smallest class means mod 840 (p ≥ 10⁵): 1, 121, 169, 361, 289, 529
(0.0368–0.0411), then 673, 601 (0.045); class 839: 0.323 ✓. R(p) with the author's definition: k = 20, 22, 23 give
min R 0.305, 0.297, 0.280 and sd 0.288, 0.301, 0.302 ✓ (see D6 for k = 16). Not re-run: the t2s_predict
E_heeg / E_avg comparison (EVIDENCE feeding an Assessment only). Also confirmed: 19 of the 20 smallest
f/log³p (p ≥ 10⁵) have p ≡ 1 (24), one ≡ 13 ✓; #(d = 1 empty) ≥ 1 in every block k ≥ 6 ✓. Trivial: §4.1 "d = 1
counts 0–98 for p ≈ 10⁶" is window-dependent (0–136 on [0.9, 1.1]·10⁶).

### Claim 5 — §4.4 gap

Source: Young, arXiv:1405.5457 (fetched; JEMS 19 (2017) is the published version, not accessed — numbering below is
arXiv's). Thm 2.1 (p. 4): for φ smooth compactly supported on SL₂(ℤ)\H with `|Δⁿφ| ≤ C(n)V²ⁿ` and **−D an odd
fundamental discriminant**, `Σ_{τ∈Λ_D} φ(τ) = h(−D)∫φ·3/π + O(‖φ‖₂D^{5/12+ε}V^{1+ε} + (DV)^{−100})`; Lindelöf for
L(u_j×χ_{−D}) and L(χ_{−D}) gives D^{1/4} ✓ (matches LITERATURE_AUTOMORPHIC.md §1). Young's strip application
(p. 5): ‖φ‖₁ ≍ V^{−1}, ‖φ‖₂ ≍ V^{−1/2}, valid for V ≪ D^{1/18−ε} ✓; Prop 1.2(1) η > 4/9 ✓.
Bookkeeping re-derived: shell of width w, length ℓ ≈ log D: `D^{1/2}wℓ ≫ (wℓ)^{1/2}D^{5/12}w^{−1}` ⟺ `w^{3/2} ≫ D^{−1/12}`
(ℓ-powers dropped) ⟺ **w ≫ D^{−1/18}**; with D^{1/4}: **w ≫ D^{−1/6}** ✓. Needed w = 1/(c√|D|) ⇒ gaps D^{4/9}, D^{1/3} ✓.
Averaging over c: the c = 1 shell fixes V = √|D|; error ≈ (ℓ log C/√D)^{1/2}D^{5/12}D^{1/2} vs main ℓ log C ✓.
Over d: per-d GLH error at w = |D|^{−1/2} is ℓ^{1/2}|D|^{1/2} ✓; even square-root cancellation over d ≤ D₀ gives
`(Σ_d dp)^{1/2} ≈ D₀p^{1/2}` ✓ ≫ log³p. Root-condition remark: `2c·2ad = f + 1` ⇒ ν ≡ (2c)^{−1} (mod f) ✓.
All conclusions are labelled Assessment in §0, §4.4 and the report ✓ — nothing here is claimed as a theorem.
