# R176 — hostile review of O176 (DIFF_DEEP.md + BRAINSTORM/bsC_*.md)

Reviewer: side-agent/review-diff-deep. Merged `side-agent/spark-diff-parity` at start. From-scratch scripts:
`scripts/review_dd_*.{c,py}`. **ES is not solved anywhere; nothing below changes that.**

**Repairs applied (author quiet at end of review):** D1–D11 applied directly to DIFF_DEEP.md, BRAINSTORM/bsC_{parity_quadratic_only,
supersingular_transfer,valence_borcherds,eichler_orientation,fourier_jacobi,isogeny_ramanujan}.md and
reviews/agent-reports/AGENT_REPORT_O176.md, each marked "(R176 repair …)". DISCOVERIES.md not touched (no O176 entry yet).

No FATAL defects. Three MAJOR (D1 vacuous "level ≥ 2√h" gloss; D2 parity-theorem scope; D4 non-existent ET
bound cited, conclusions survive with repairs) and eight MINOR. All numerical claims checked were reproduced exactly.

## Verdict per claim

| Claim | Verdict |
|---|---|
| DIFF_DEEP Thm 2.1 (algebraic bijection + `4h ∣ gcd(h,G)²`) | **SOUND** (re-derived; brute force exact for all odd n ≤ 2001) |
| Thm 2.1 geometric reading | SOUND-AFTER-REPAIRS (see D-list) |
| Thm 1.1 / Cor 1.2 (supersingular transfer; ∃E vacuous) | SOUND (Diff(T') = {p} re-checked from scratch) |
| Prop 1.3 (∀E false; τ(e) maximal orders) | SOUND-AFTER-REPAIRS (τ(e) correct for all e; ET citation wrong) |
| Prop 2.2 (Gram form, involutions, k² = −4c²dp) | SOUND; last sentence (commutative identity with *this* k) FALSE as written — notation clash (D3) |
| Prop 2.3 (level free on one endomorphism, nrd x ≪ M²p) | **SOUND** (absolute constant; notation O⁰ clash, D5) |
| Prop 2.4 (exactness gap) | identity SOUND; f^{3/2} gap and lottery sum are Assessment, with a bookkeeping slip (D6) |
| bsC_parity_quadratic_only Prop 1 (as literally stated: η quadratic Hecke char., t ∈ ℚ^×, v_ℓ(t) = 1) | SOUND |
| Prop 1 "In particular…" sentence, Cor 2 second half, memo Assessment ("parity/incoherence mechanisms over any base field carry only quadratic information") | **GAP (MAJOR)**: slogan beyond the theorem; false for F-rational data (D2) |
| Cor 2 first half (f ≡ −1 (M) is a Boolean function of quadratic characters ⟺ M ∣ 24) | SOUND |
| EVIDENCE 71/9732 uncovered by the 9+9 slices | **SOUND** (reproduced exactly from scratch) |
| bsC_valence_borcherds Prop 1 (Galois-orbit obstruction) | SOUND-AFTER-REPAIRS: the cited "ET f(p) ≪ p^{o(1)}" does not exist; the divisor bound suffices (D4) |
| §2.5 canonical curve EVIDENCE (144/267; 47/76, 34/67, 30/57, 33/67) | **SOUND** (reproduced exactly; order O(q,r) verified maximal) |
| §3 / bsC_eichler_orientation Props 1–2 | SOUND (re-derived; dangling script reference, D8) |
| §4 (LD_p) as stated (exact divisibility) | SOUND (⟺ Type II(p) by Thm 1.1 + 2.1) |
| bsC_fourier_jacobi records F*(p) | SOUND (reproduced exactly, `scripts/review_dd_jacobi.c`); EZ Thm 2.2 hypotheses (D9) |
| bsC_isogeny_ramanujan, bsC_arithmetic_topology | Assessment memos; one internal inconsistency (D10) |
| §4 / report gloss "level G ≥ 2√h" as the content of (LD_p) | **GAP (MAJOR)**: the relaxed condition is vacuous |

## Checks performed

### Thm 2.1 (algebra)
Re-derivation. ET Type II: a,b,c,d ≥ 1, `4abd = n + e`, `a + b = ce`; so `4abcd = cn + a + b` and
`(4acd−1)(4bcd−1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1`. Thus h := (ff'−1)/n = 4c²d = cM (M = 4cd), M | f+1, f'+1,
so M | G and h | cG. Conversely d = h/4c², M = h/c | G gives a, b ∈ ℤ_{>0}, and `abM − a − b = nc` is the ET
equation with e = (a+b)/c — but **e ∈ ℤ needs a separate line**: from `4abd = n + (a+b)/c` and 4abd, n ∈ ℤ,
(a+b)/c ∈ ℤ. (The author's ⇐ cites "(I)4's criterion", which contains this; fine.) Minimal c: h/g divides every
valid c, so 4c² | h is weakest at c = h/g; gives 4h | g². Edge h = 0 (f = f' = 1) is excluded by 0 ∤ cG. Correct.

Brute force (`scripts/review_dd_thm21.c`, C, 0.3 s): tuple side by the naive ET loop (a ≤ b, d, e = 4abd − n,
e | a+b); triple side by c, d with h = 4c²d ≤ (n+5)² (4× the analytic bound (n+5)²/4 that I derived on the triple
side), f ≡ −1 (M), f | 1 + nh, f' ≡ −1 (M). **All odd n ∈ [3, 2001] (1000 values, 21 odd squares): the two sets of
(f, f', c) coincide exactly, 16054 tuples, no duplicates, 0 solutions at odd squares.** (Author's enumerator gives
the same total 1120 for n ≤ 301.) The "iff 4h | gcd(h,G)²" part checked independently
(`scripts/review_dd_thm21_iff.c`): all 3 556 994 factor pairs f ≤ f' of 1 + nh, 1 ≤ h ≤ n², odd n ≤ 151 — predicate ⟺
existence of c, 0 disagreements, and no predicate-true pair beyond h ≤ (n+5)²/4.

### Prop 1.3 / bsC_supersingular_transfer Prop 3
* τ(e) count: the maximal orders of M₂(ℚ_ℓ) containing the Eichler order of level ℓⁿ are the n+1 vertices of the
  geodesic segment — true for every n, so the global count is ∏(v_ℓ(e)+1) = τ(e) for **non-squarefree e as well**.
  Checked by brute force on the Bruhat–Tits tree (`scripts/review_dd_tree.py`: ℓ = 3, 5, n ≤ 4, all vertices within
  radius n+2: exactly n+1 stable lattices). The local argument (−d a unit square mod ℓ^{v} since e | 4a²d + 1, ℓ ∤ 2d;
  Hensel; idempotents ⇒ [[ℤ_ℓ, ℓ^i],[ℓ^j, ℤ_ℓ]] ⇒ Eichler of level ℓ^{i+j}) is standard and correct.

### Thm 1.1 / Cor 1.2 and the geometric reading of Thm 2.1
* Thm 1.1: ℤ⟨x,y⟩ with x² = −f, y² = −f', xy + yx = −2 is an order (yx = −2 − xy); it lies in a maximal order of
  B_T; Deuring realises every maximal order type of B_{p,∞}. ⇒: positive-definite T ⇒ x, y do not commute ⇒ they
  generate End⁰E. Correct. Its reduced discriminant is 4·det T, so p | det T is automatic on a curve (needed for the
  "h = det/p" phrasing). Correct.
* Diff(T') = {p} for every Type II pair: re-checked with my own Hilbert-symbol code on B_{T'} = (−f, −f·det T')
  (`scripts/review_dd_hilbert.py 1500`): **4025 Type II pairs of primes p < 1500, finite ramification exactly {p} in
  every case.**
* **The relaxed reading "level G ≥ 2√h" is NOT equivalent and is in fact vacuous** (`scripts/review_dd_vacuous.py
  3000 200`): for 437 of the 438 primes 5 < p < 3000 (all residues mod 24; the only miss is p = 5 at h ≤ 200) there is a
  pair (f, f') with ff' = 1 + ph, B_{T} ramified exactly at p (so it lives on a supersingular curve by Thm 1.1),
  G ≥ 2√h, and 4h ∤ gcd(h,G)², i.e. **not** a certificate. Examples: p = 73: (21, 153), h = 44, G = 22;
  p = 97: (20, 34), h = 7, G = 7; p = 1201: (39, 154), h = 5, G = 5. Per-pair counterexamples with small p:
  (f,f') = (4,9) at p = 7 (h = 5, G = 5). Thm 2.1's displayed condition is the correct one; the glosses are wrong
  (see D1).

### Prop 2.2 (`scripts/review_dd_identities.py 3001`, 27 788 Type II tuples of odd n ≤ 3001, own enumerator)
* Gram form: f = aM − 1, f' = bM − 1 ⇒ fX² + 2XY + f'Y² = M(aX² + bY²) − (X − Y)². ✓ (0 failures).
* x² = −f ≡ 1, (x + y)² = −(f + f' + 2) = −M(a + b) = −Mce ✓; trd(xy) = −2 so k = xy + 1 is trace-zero and
  nrd k = ff' − 2 + 1 = 4c²dp, k² = −4c²dp ✓ — verified in an explicit model x = i, y = i/f + j/f of (−f, −f·det T)
  (0 failures).
* bsC_typeII_commutative Lemma 1 `(2ad + k)(2bd + k) = de(1 + 2ck)` with **k² = −dn** ✓ (0 failures; re-derived:
  LHS = d(4abd − n) + 2(a+b)d·k, coefficient comparison gives exactly 4abd = n + e, a + b = ce; norms ✓ since
  ef = 4a²d + n). But DIFF_DEEP Prop 2.2 states the identity right after defining k := xy + 1 with k² = −4c²dp: **with
  that k the identity fails for all 27 788 tuples** (it forces 4abd − 4c²n = e). The memo's k is
  (xy + 1)/(2c). See D3.

### Prop 2.3 (re-derived)
O/MO ≅ M₂(ℤ/M) (p ∤ M); trd(O) = ℤ (contains 2, and O ⊗ ℤ₂ ≅ M₂(ℤ₂) has odd traces); x = x' + Mz is trace-zero
and ≡ x₀; MO ∩ B⁰ = M(O ∩ B⁰); the coset contains y with nrd y ≤ M²ρ²; y² = −nrd y ≡ 1 in O/MO and ℤ ∩ MO = Mℤ give
nrd y ≡ −1 (M); y ≠ 0 since x₀ ≢ 0. Constants: with λ_i the successive minima (squared, nrd) of O ∩ B⁰,
λ₁λ₂λ₃ ≪ det ≍ p² (Minkowski II), Kaneko (two non-commuting trace-zero elements: (−4λ₁)(−4λ₂) ≥ 4p) gives
λ₁λ₂ ≥ p/4, so λ₃ ≪ p and ρ² ≤ ¼Σλ_i ≪ p (in dimension 3 minimal vectors form a basis). **The implied constant is
absolute** (no dependence on M, x₀ or the order). SOUND. Remark: the statement is weak by design (one vector in a
coset of covolume ≍ M³p); it does not touch the second congruence or the exact-norm condition.

### Prop 2.4
y_⊥ = y − x/f, nrd y = 1/f + nrd y_⊥, det T = f·nrd y_⊥ ✓. {y ≡ y₀ (M), ⟨x,y⟩ = 1} is an affine coset of
x^⊥ ∩ MO⁰ ✓; det(x^⊥ ∩ L) = nrd(x)·det L/[L : ℤx ⊕ (x^⊥ ∩ L)]² (so "up to an index factor" is right, but the
index can be as large as ≍ f for special x, which would cut the gap to ≍ f^{1/2}; this is why it must stay an
Assessment). Thm 2.1 ⇒ h ≤ g²/4 ≤ G²/4 ⇒ nrd y_⊥ ≤ pM²/(4f) ✓; ratio f^{3/2} ✓; f ≥ M − 1 ✓.

### bsC_parity_quadratic_only
* **Prop 1 as stated is correct.** For λ | ℓ unramified (in F and for η), η_λ(t) = η(λ)^{v_λ(t)} = η(λ) (e = 1,
  v_ℓ(t) = 1), so the count is ≡ [∏η(λ) = −1] = [η((ℓ)O_F) = −1], and ℓ ↦ η((ℓ)O_F) is the restriction of η to
  𝔸_ℚ^×, a quadratic Dirichlet character (possibly trivial). Sanity example I computed by hand: F = ℚ(ζ₁₃)⁺,
  E = ℚ(ζ₁₃), η = η_{E/F}; λ | ℓ is inert in E iff k = ord(ℓ mod 13) is even, g = 6/k' (k' = order mod ±1);
  η((ℓ)) = (−1)^{g·[k even]} = −1 iff k ∈ {4, 12} iff (ℓ/13) = −1. ✓ quadratic.
* **But the hypothesis t ∈ ℚ^× (Galois-invariant data at ℓ) is essential, and the memo's scope sentences drop it.**
  Same F, E, η, a one-dimensional hermitian space ⟨π⟩ with π ∈ F generating one prime λ | ℓ (h(F) = 1): the local
  invariants above ℓ are η_{λ'}(π) = −1 iff λ' = λ and k is even, i.e. iff ℓ is **not a 4th power** mod 13. ℓ = 3
  (order 3) and ℓ = 17 ≡ 4 (order 6) are both quadratic residues mod 13, but give opposite local Diff at λ.
  So a Diff-set built from local ±1 hermitian invariants over F *does* see order-4 information about ℓ once the data
  are F-rational rather than ℚ-rational; only the parity over the whole fibre {λ | ℓ} is quadratic. The phrases "any
  Diff-set built from local ±1 invariants … depends on ℓ only through one quadratic character", "(over any base, any
  dimension)" and the Assessment "parity/incoherence mechanisms over any base field carry only quadratic
  information about the divisor" are therefore **not** what Prop 1 proves. (In ES the certificate data are rational,
  so the restricted statement is the relevant one; but a unitary/big-CM mechanism over ℚ(ζ_M)⁺ would naturally use
  F-rational data, e.g. the prime factors of f in F — exactly the case spark 4 was about.)
* Cor 2: (ℤ/M)^× has exponent ≤ 2 ⟺ M | 24 ✓; the slice descriptions are re-derived: Type II slice (c,d) ⟺
  ∃ f | 1 + 4c²dp, f ≡ −1 (4cd) (Thm 2.1); Type I slice ⟺ ∃ f | p² + 4c²d, f ≡ −p (4cd) (f = 4acd − p, ef = 4a²d + 1,
  converse needs gcd(f, 4c²d) = 1, true for p ∤ 6cd, and b = ce − a = (c + ap)/f > 0) — cross-checked against the
  direct ET definition for all 9 slices and primes 5 ≤ p < 700 (`scripts/review_dd_slices_check.py`, 1107 tests, 0
  mismatches). The step "so a mechanism … can certify ES only through slices with 4cd | 24" is not a theorem:
  "mechanism whose information about f comes from Diff-parities" is undefined. It is a sound *Assessment*.
  Citation redteam-automorphic-2 Thm 2.2(iii) (conditional on H) checked: says exactly that finite Θ₀ fails i.o.
* **EVIDENCE recomputed from scratch** (`scripts/review_dd_slices.c`, C, own sieve/factoring, 0.15 s): primes
  p ≡ 1 (24) uncovered by the 18 slices: 1/143 (< 10⁴), 8/1181 (< 10⁵), 33/3202 (< 3·10⁵), **71/9732 (< 10⁶)**;
  first 3361, 31081, 34897, 62497, 66889 — identical to the memo.

### bsC_valence_borcherds Prop 1
* Dictionary ✓: [f, 2, f'] is primitive (f odd), disc 4 − 4ff' = −16c²dp = −4Mcp; (X,Y) ↦ (X, X + Y) gives
  [f + f' + 2, 2 + 2f', f'] = [Mce, 2Mb, f'] ✓ (unimodular); C + 1 = f' + 1 = Mb = B/2 ✓.
* Galois step ✓: τ a root of a primitive form of disc D has End = O_D, so ℚ(j(τ)) has degree h(D) over K and the
  Gal(ℚ̄/LK)-orbit of the point on X₀(M) has size ≥ h(D)/[L:ℚ]; the zero divisor of F is defined over L
  (q-expansion principle). Siegel for non-fundamental D ✓ (h(D) = h(D₀)·(conductor factor) ≫ |D|^{1/2−ε}).
* **Citation defect:** "ET's f(p) ≪ p^{o(1)}" — ET (sources/elsholtz-tao-1107.1010.pdf, Prop 1.7) prove only
  f_I(n) ≪ n^{3/5+O(1/log log n)}, f_II(n) ≪ n^{2/5+O(1/log log n)}, and say explicitly (after Prop 1.7) that
  f(n) ≪ n^ε "seem[s] difficult to obtain". The argument does not need ET at all: D = −16c²dp fixes c²d, so the
  certificate points on Z(D, r) number ≤ Σ_{c²d fixed} τ(1 + 4c²dp) ≪ p^{o(1)} by the divisor bound. With that
  replacement Prop 1 is PROVED relative to Siegel (+ CM theory). (Using ET's actual f_II bound instead would weaken
  the conclusion to [L:ℚ] ≫ p^{1/10−ε}.)
* "Bruinier's converse theorem closes the loophole": Bruinier's converse theorem (LNM 1780) is proved for lattices
  splitting hyperbolic planes (as I recall it; LNM 1780 not available in sources/); X₀(M) is l = 1. I could not
  verify a version covering l = 1 — cite one or drop the sentence (MINOR; the Prop does not use it).
* EVIDENCE recomputed (`scripts/review_dd_orbit.py 3000`, own class-number count of reduced primitive forms):
  max (#certificate pairs)/h(−16c²dp) over (c,d) ∈ {(1,1),(1,2),(1,3)}, p < 3000, is 0.25 at p = 5 ✓.

### §2.5 canonical curve (`scripts/review_dd_canonical.py`, own lattice enumeration in integer coordinates)
For every p ≡ 1 (24) < 2·10⁴ I verified that Ibukiyama's O(q, r) is closed under multiplication (integral structure
constants) and has det(trd(e_a ē_b)) = p², i.e. it is a maximal order of (−p, −q). Searching O ∩ B⁰ for x, y with
⟨x,y⟩ = 1, f ≤ f' ≤ 4p and the Thm 2.1 condition: **47/76, 34/67, 30/57, 33/67 = 144/267**, identical to §2.5; every
pair found has p | ff' − 1 (asserted). (Note O⁰ here is O ∩ B⁰, not the Gross lattice; see D5.)

### Other memos (spot checks)
* bsC_eichler_orientation Prop 1: level characters χ₁, χ₂ = trd − χ₁ give χ₂(v) = −χ₁(v), distinct mod each ℓ | e
  (ℓ odd, gcd(m,e) = 1), so {χ(v)} = all 2^{ω(e)} roots of −m ✓; a² ≡ −m (e) ⟺ e | a + b ✓; (v − a)(v + a) = −ace,
  C ⊆ ker(v − a), deg ψ = ac ✓. Prop 2 = DIFF_DEEP 2.2/2.3 ✓. Numerical sanity of Prop 2.3 on Ibukiyama orders
  (`scripts/review_dd_lift.py 3000 12 40`): least nrd x ≡ −1 (M) in O ∩ B⁰ is ≤ 0.017·M²p for all p ≡ 1 (24) < 3000,
  3 ≤ M ≤ 12; λ₁λ₂/p ≥ 1 (consistent with Kaneko's ≥ 1/4).
* Prop 1.3's side facts: from-scratch Type I enumeration (`scripts/review_dd_typeI_e.py 600`, 3346 tuples, a ≤ b):
  e ≤ (p+1)² + 1 always (max e/p² = 0.347), and p ∤ e in every case (the memo asserts p ∤ e without proof; harmless —
  if p | e the count only drops, the maximal order at p being unique).
* bsC_fourier_jacobi: least-index records (73, 7) … (954409, 335) reproduced exactly.
* bsC_isogeny_ramanujan step 1 / bsC_arithmetic_topology: Assessment-only; see D10.

## Defects

**D1 (MAJOR) — the "level ≥ 2√h" gloss is a vacuous relaxation, presented as the content of (LD_p).**
Locations: DIFF_DEEP §4 ("(LD_p) asks for **level G ≥ 2√h** … 'a pair … whose congruence level is at least twice the
square root of their normalised covolume'"); report O176 SHARP bullet 1 ("ES Type II(p) ⟺ some supersingular E … whose
Gram 'level' G is ≥ 2√h"); report Spark 1 ("some O has a pair with level ≥ c·√h") and Spark 2. Thm 2.1 needs
4h | gcd(h, G)², which implies G ≥ 2√h but is far stronger: it needs g = gcd(h,G) with h/g | g/4. The relaxed
condition holds for non-certificate pairs living on supersingular curves for 437/438 primes 5 < p < 3000 (examples
above), so a theorem of the form "some O has a pair with level ≥ c√h" proves nothing. *Repair:* in §4 and the report
replace "level G ≥ 2√h" by the exact condition "h = g·t with g = gcd(h, G) and 4t | g" (equivalently 4h | g²), state
that G ≥ 2√h is necessary only and is satisfied by non-certificates for essentially every p (cite this review's
examples), and drop the "⟺" in the SHARP bullet (keep the exact divisibility form, which is correct). Spark 1 must be
rephrased in terms of the divisibility, not the size.

**D2 (MAJOR) — bsC_parity_quadratic_only: the scope sentences exceed Prop 1.** Locations: Prop 1 "In particular the
parity of any Diff-set built from local ±1 invariants … of data at a rational prime ℓ depends on ℓ only through one
quadratic character"; Cor 2 "(over any base, any dimension)"; memo Assessment "PROVED obstruction with exact scope:
parity/incoherence mechanisms over any base field carry only quadratic information"; DIFF_DEEP (H4) and §5 PROVED
bullet "parity over any base is quadratic"; report SHARP bullet 3. Prop 1 needs the local data at all λ | ℓ to come
from one t ∈ ℚ^× (Galois-invariant). For F-rational data the local Diff above ℓ sees non-quadratic information (F =
ℚ(ζ₁₃)⁺, hermitian ⟨π⟩: detects whether ℓ is a 4th power mod 13; ℓ = 3 vs ℓ = 17). And "mechanism whose information
about f comes from Diff-parities" is undefined, so the "can certify ES only through slices 4cd | 24" step is an
Assessment. *Repair:* restate Prop 1's conclusion as "for Diff-sets whose local invariants above ℓ are η_λ(t) with
t ∈ ℚ^× (in particular for any Diff built from ℚ-rational certificate data), the parity over {λ | ℓ} is χ(ℓ) for a
quadratic Dirichlet character χ"; add the F-rational counterexample as a scope remark; relabel the mechanism sentence
of Cor 2 and the memo/DIFF_DEEP/report slogans as Assessment.

**D3 (MINOR) — DIFF_DEEP Prop 2.2, last sentence: wrong k.** With k := xy + 1 (k² = −4c²dp) as defined two lines
earlier, "(2ad + k)(2bd + k) = de(1 + 2ck) in ℤ[√−dp]" is false (fails on all 27 788 tuples, n ≤ 3001). The memo's
identity uses k = √(−dp) = (xy + 1)/(2c). *Repair:* "with κ := (xy + 1)/(2c), κ² = −dp: (2ad + κ)(2bd + κ) =
de(1 + 2cκ) in ℤ[κ]".

**D4 (MAJOR, citation; conclusions survive) — "ET's f_I(p) ≪ p^{o(1)}" / "ET's f(p) ≪ p^{o(1)}" does not exist.**
Locations: DIFF_DEEP Prop 1.3 label and text, Answer paragraph ("p^{o(1)} curves"); bsC_supersingular_transfer Prop 3
label/text and Barrier B3 ("≪ p^{o(1)} objects"); bsC_valence_borcherds Prop 1 label/text and Assessment
("certificates number p^{o(1)}"); report §Results. ET Prop 1.7 gives only f_I(n) ≪ n^{3/5+O(1/log log n)},
f_II(n) ≪ n^{2/5+O(1/log log n)}, and ET call f(n) ≪ n^ε difficult (text right after Prop 1.7). *Repairs:*
(a) Prop 1.3: ≤ 2Στ(e) ≤ 2 f_I(p)·max τ(e) ≪ p^{3/5+o(1)} = o(p) by ET Prop 1.7 + divisor bound — "∀E false
for Type I for large p" survives; replace "p^{o(1)} curves" by "p^{3/5+o(1)} curves (p^{o(1)} conjecturally)".
(b) valence_borcherds: certificates on a fixed Z(D, r) (D = −16c²dp fixes c²d) number ≤ Σ τ(1 + 4c²dp) ≪ p^{o(1)}
by the divisor bound — cite that instead of ET; label "PROVED relative to Siegel".
(c) supersingular_transfer B3 bullet: "main term ≫ p^{o(1)}" → "≫ p^{3/5+o(1)} unconditionally".

**D5 (MINOR) — notation O⁰.** Prop 2.3/2.4 use O⁰ = O ∩ B⁰ (trace-zero elements of O; the proof makes x trace-zero
in O), §2.5 calls O⁰ "its Gross lattice" (standardly (ℤ + 2O) ∩ B⁰, a proper sublattice of O ∩ B⁰). The script uses O ∩ B⁰.
*Repair:* define O⁰ := O ∩ B⁰ once and delete "Gross lattice" in §2.5 (or say "trace-zero part").

**D6 (MINOR) — Prop 2.4 lottery bookkeeping.** "≍ F^{3/2}/M³ … per order" omits the covolume p of O⁰
(≍ F^{3/2}/(M³p) per order, then ×p/12 orders), and "Σ_{f ≡ −1 (M)} O(1/(Mf))" double-counts the congruence: the
density already counts x in the coset, so the per-M total is Σ_{f ≤ F} O(1/(Mf)) over all f (≍ log F/M), giving
log² F after Σ_M; summing only over f ≡ −1 (M) gives ≍ log F. Also note the index factor in det Λ_x can reach ≍ f,
which would shrink the gap to f^{1/2}. *Repair:* fix the two expressions; keep Assessment label.

**D7 (MINOR) — "∀E false" scope.** Answer paragraph of DIFF_DEEP: "the 'every curve' version is false (Type I
certificates …)" reads as if "every curve carries an ES certificate" were refuted. Only Type I configurations are
handled (memo: Type II version is Assessment, 2-part uncontrolled). *Repair:* "the 'every curve carries a Type I
certificate' version is false for large p; the Type II/union version is open (Assessment)".

**D8 (MINOR) — dangling script.** bsC_eichler_orientation "Cheap numerics": `scripts/bsC_involution_lift.py` does not
exist, and DIFF_DEEP §2 has no test of Prop 2.3. *Repair:* remove the reference or point to
`scripts/review_dd_lift.py` (this review).

**D9 (MINOR) — bsC_fourier_jacobi Prop 1 citation.** Eichler–Zagier Thm 2.2 is for holomorphic Jacobi forms on the
full Jacobi group; Kudla's genus-2 series is the derivative of an incoherent (non-holomorphic, level) Eisenstein
series. The needed fact (a(T) depends only on the class/genus of T) is R172 D8 / Kudla's local-factor formula.
*Repair:* cite that instead; also "Bruinier's converse theorem" in bsC_valence_borcherds B2 is stated for O(2,l) with
lattices splitting hyperbolic planes; I could not confirm a version covering l = 1 (X₀(M)) — source not accessed here;
give an l = 1 reference or drop the sentence.

**D10 (MINOR) — bsC_isogeny_ramanujan step 1.** "taking e large (e ≥ p^{3+ε}) puts a, b in the deterministic range":
Type I tuples have e ≤ (p+1)² + 1 (Prop 1.3) and ab = (pe+1)/4d ≪ p³, so a, b ≥ p^{2+ε} never occurs. The step is
vacuous rather than "B3". *Repair:* say so (the deterministic regime of Kane/Chevyrev–Galbraith is never reached by
ES configurations).

**D11 (MINOR, labels).** DIFF_DEEP §5 PROVED list must follow D2 (parity sentence → "PROVED for ℚ-rational data;
the general slogan is Assessment") and D4 (relative-to citations). Thm 2.1's "Geometric form" also silently uses
p | det T for x, y in a maximal order (true: the reduced discriminant of ℤ⟨x,y⟩ is 4 det T); add one line.
