# R128 — hostile review of O128 (`POINTWISE_TYPEII_SPECTRAL.md`)

Reviewer branch `side-agent/review-typeii-spec`; merged `side-agent/typeii-spectral` at review start.
From-scratch scripts: `scripts/review_t2s_*.py`. ET = `sources/elsholtz-tao-1107.1010.pdf` (read via pdftotext).

## Summary verdicts (filled in progressively)

| # | Claim | Verdict |
|---|---|---|
| 1 | Lemma 1.1 parametrisations, duality table | SOUND (bijection verified); MINOR wording defects D1, D2 |
| 2 | Prop 2.1 / Lemma 2.2 Heegner + separation | SOUND (bound has slack: min cosh = 3 observed) |
| 3 | Prop 2.4 / 2.5 exact incidence | SOUND-AFTER-REPAIRS (D3: shell also contains non-primitive points) |
| 4 | §3 averaged check, constant 0.05 | |
| 5 | §4.4 gap (Young bookkeeping) | |
| 6 | Lemma 6.1 / Cor 6.2 / 6.3 genus | |
| 7 | §5 numerics | |

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
