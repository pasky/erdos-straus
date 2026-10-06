# R80 — hostile review of POINTWISE_MORDELL.md (branch side-agent/mordell-13)

Reviewer: side agent R80 (branch `side-agent/review-mordell`). All checks below are FROM SCRATCH;
no `scripts/mordell_*` code was imported. Scripts: `scripts/review_mordell_*.py`.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 3.1(a),(b) (finite-computation theorem) | **SOUND** (independently re-certified; minor wording) |
| Computation 4.1 + "every finite covering needs modulus > 10⁶" | see §2 |
| Novelty vs Salez / Mordell / literature | see §3 |
| Labels: Conj 4.2, §5 EVIDENCE, Theorem C discussion | see §4 |

## 1. Theorem 3.1 — SOUND

### 1.1 What I re-derived
Family formulas re-derived directly from the ET varieties Σᴵ (2.1)–(2.9) and Σᴵᴵ (2.13)–(2.21)
(arXiv:1107.1010, PDF in `sources/`), with πᴵ=(abdn,acd,bcd), πᴵᴵ=(abd,acdn,bcdn):

* I1 (a,d,f), f | 4a²d+1: e=(4a²d+1)/f, b=(ne+1)/(4ad), c=(n+f)/(4ad).
* I2 (a,c,f): d=(n+f)/(4ac), b=(na+c)/f.
* I3 (c,d,f): a=(n+f)/(4cd), b=(n+(n²+4c²d)/f)/(4cd)  [from (2.6),(2.9)].
* I4 (a,b,e), e | a+b: c=(a+b)/e, d=(ne+1)/(4ab).
* II1 (a,b,e): c=(a+b)/e, d=(n+e)/(4ab).
* II2 (a,d,f), 4ad | f+1: c=(f+1)/(4ad), b=(nc+a)/f.
* II3 (a,d,e): c=(n+4a²d+e)/(4ade), b=ce−a=(n+e)/(4ad).

All coordinates are polynomials of degree ≤2 in n with positive coefficients (II3: b=(n+e)/(4ad)>0),
so x,y,z>0 for every n≥1 — slightly stronger than the document's "n>1".
The parameter order in the JSON certificates matches the §2.1 table (I1 a,d,f; I2 a,c,f; I3 c,d,f;
I4/II1 a,b,e; II2 a,d,f; II3 a,d,e); every certificate class satisfies its family side-condition.

### 1.2 From-scratch check (`scripts/review_mordell_check.py`)
* identity 4xyz = n(xy+yz+zx) verified at 12 values of n (degree ≤7 ⇒ polynomial identity);
* integrality: for n=t+Ls the coordinates are degree-≤2 polynomials in s, integer-valued on ℤ iff
  integral at s=0,1,2 — checked exactly with Fractions (no sampling);
* target set enumerated independently: units t mod L with t≡1 (24), t a QR mod 5 and 7,
  (t/13)=−1 [and (t/11)=+1 for np].

Result: np/240240: 360 targets, uncovered = {112561} exactly; main/720720: 2160 targets,
uncovered = {112561, 352801, 380881, 418321, 473761, 483841} exactly. Every certificate class covers
≥1 target (no dead classes). So the exception lists are exactly the complement of the certificate
coverage (sharp for these certificates).

### 1.3 Mordell step (`scripts/review_mordell_840.py`)
Independent check that each of the 186 non-square unit residues mod 840 lies in an ET class whose
coordinates are integral on the whole progression t+840ℤ (8 witness classes, params ≤40), and that
no candidate class covers any of the 6 squares {1,121,169,289,361,529}. Also confirms "not a square
mod 840" ⇔ "not (≡1 (24), QR mod 5, QR mod 7)" for units. Primes dividing 840·11·13 (2,3,5,7,11,13)
are trivially fine (ES known/explicit); the theorem's phrasing via "p not a square mod 840" implicitly
uses p∤840 — harmless.

### 1.4 Residue bookkeeping
(p/13)=−1 ⇔ p mod 13 ∈ {2,5,6,7,8,11}; (p/11)=+1 ⇔ p mod 11 ∈ {1,3,4,5,9}. 240240=2⁴·3·5·7·11·13
contains 8 (for ≡1 mod 8 — 16 is used), 3, 5, 7, 11, 13; 720720 adds 3². Both suffice. The stated
CRT description of 112561 (≡1 mod 16,3,5,7; 9 mod 11; 7 mod 13) is correct.

### 1.5 Exceptional classes, numerical ES
`scripts/review_mordell_exc.py 1e8`: all 248 primes ≤10⁸ in the six exceptional classes mod 720720
have an explicit, Fraction-verified ES solution (0 failures). Consistent, as expected.

### Defects for §3
1. MINOR (sharpening, Thm 3.1(a)). The (a) exception class 112561 mod 240240 lifts to three classes
   mod 720720: 112561, 352801, 592801. The main certificate covers 592801. So, combining the two
   certificates, (a) holds with exceptions only `p mod 720720 ∈ {112561, 352801}` (the (b) exceptions
   with (p/11)=+1). Suggest stating this, or remarking that (a) is not the sharpest consequence.
2. MINOR (wording). §0 says each class solves "every sufficiently large n in the class"; for these seven
   explicit parametrisations it is every n≥1 in the class (all coefficients positive). State it, since
   it removes the "B" in the compactness paragraph for the certificates used.
3. MINOR (label). "PROVED by finite computation; independent re-check pending" → can now read
   "PROVED (finite computation, independently re-checked by R80: scripts/review_mordell_check.py)".

## 2. Computation 4.1 and the "modulus > 10⁶" consequence — SOUND (bullet 1 fully re-checked; bullet 2 re-checked except F = 11³·13³)

### 2.1 Class family
I checked ET Prop 1.9 (statement p. 8 and proof §10 of the PDF in `sources/`) against the families
used. The seven families, their side-conditions and the solution formulas in §10 agree with my
re-derivation in §1.1 (e.g. ET's I1 `b=(n+f)e/(4ad)−a` = my `(ne+1)/(4ad)` since `fe=4a²d+1`).
Class moduli as used by me: I1 `4ad`; I2 `4ac·f`; I3 `4cd·f`; I4, II1 `4ab`; II2 `f`; II3 `4ade`.
ET prove (not merely assert) the converse: a primitive class solvable by polynomials has all large
primes in finitely many family classes; the word "essentially complete" (p. 8) refers to this.
So "ET class" = class of one of these seven families is the right object.

### 2.2 From-scratch re-check (`scripts/review_mordell_point.py`)
Exact membership test of `x*` (CRT residue `x* mod M`) against every class of every family with
modulus `M ≤ Mmax` (I1: all `f | 4a²d+1`; II2: all `ad | (f+1)/4`; I2/I3: all coprime triples).
* Positive control: 13-generic point `x_13=5` → hits II2 (1,2,39), II3 (1,2,39), I2 (5,1,39) at
  `Mmax=10⁴`, consistent with §1 of the document.
* `x*` (11:2, 13:2): **0 hits at Mmax = 10⁴, 10⁵ and 10⁶** (10⁶ run: 2.7·10⁷ I1, 1.5·10⁷ I4/II1,
  2.2·10⁷ II2, 9.5·10⁶ II3, 1.7·10⁵ admissible I2/I3 parameter sets). Bullet 1 CONFIRMED in full.

### 2.3 Rigid II1/I4/II2 enumeration (`scripts/review_mordell_rigid.py`)
Re-derived the rigid forms myself: for x* in an II1/I4 class (modulus 4ab, T-part F, N=4ab/F) one
needs `N | e+1`; with `e+1=Ni`, `k=(a+b)/e`: `4iabk = F(a+b+k)`, sorted `s≤t≤w` ⇒ `4ist ≤ 3F`,
finite. For II2 (`f=Fg`): `g | 4a²d+1`, `4adm=f+1` ⇒ `g | a+m`; `a+m=gj` gives
`(4dja−F)(4djm−F) = F²+4dj²`; both factors must be positive and then `j(4d−1) ≤ 2F` — finite.
(The document's §2.1 rigid forms agree.) Controls: `x_13=5` → II2 (1,2,39); `(x_11,x_13)=(1,7)` →
II2 (2,2,143); `(1,2)` → II2 (9,2,143), matching the document's §1 "13-generic" claims.
* `x*`: 0 hits for every F | 11³·13³ **except F = 11³·13³ itself**, which my pure-Python
  enumeration could not finish (≈2·10⁷ factorizations); bullet 2 is re-checked for 15 of the 16
  T-levels only.

### 2.4 Logic of the consequence
"Every finite covering of Σ₁₃ (main) by ET classes contains a class of modulus > 10⁶" follows
trivially from bullet 1 (x* ∈ Σ₁₃ must be covered by some class). The Dirichlet sentence is a
correct strengthening (a finite union of classes of modulus ≤ 10⁶ missing x* misses the class
`p ≡ x* (mod lcm)`, which contains infinitely many primes, all Mordell-hard with (p/13)=(p/11)=−1).
`x* ∈ Σ₁₃`: x*≡1 (24), square at 5, 7; `(2/13) = −1` ✓.

Defects for §4:
4. MINOR. The neighbourhood "p≡1 (mod Q), p≡2 (mod 11⁸·13⁸)" — the exponent 8 is arbitrary; the
   correct statement is "p ≡ x* modulo the lcm of the moduli" (for moduli ≤10⁶ any exponent ≥5
   suffices). Harmless; reword.
5. MINOR. Label "CERTIFIED by one engine, re-check pending" can become "CERTIFIED, two independent
   engines (R80: review_mordell_point.py at 10⁶; rigid bullet re-checked for F ≠ 11³13³)".
