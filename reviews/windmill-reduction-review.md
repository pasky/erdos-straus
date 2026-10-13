# R164 — hostile review of O164 `WINDMILL_REDUCTION.md` (§1–§10)

Reviewer branch `side-agent/review-windmill-reduction`; merged `side-agent/windmill-reduction` at review start.
From-scratch scripts: `scripts/review_wr_*.py` (none of the author's `wr_*` code reused).
**ES is not solved; nothing in O164 claims otherwise.**

## Summary verdicts

| item | verdict |
|---|---|
| §1 Computation 1.2 + dictionary | SOUND (re-certified independently to 20000; see D1, D2 minor) |
| §2 Lemma 2.1, Cor 2.2 | SOUND |
| §2 Computation 2.3 (15 / 267; 78 no reduced) | SOUND (reproduced exactly, independent code) |
| §2 Lemma 2.4 | SOUND-AFTER-REPAIRS (D3: positivity hypothesis missing; statement false as written) |
| §3 (EVIDENCE, negative) | not re-run (spot-check budget spent on §4); labels appropriate |
| §4 (EVIDENCE, negative) | SOUND — all six numbers reproduced exactly by independent method; extended to p ≤ 20000 (D4 minor) |
| §5.1 | SOUND as Assessment; label over-reach (D6 minor) |
| §5.2 | SOUND (t odd needed for "⇐"; automatic in the 4 | A slice — D7 minor) |
| §5.3 | GAP → SOUND-AFTER-REPAIRS (D5 MAJOR: box bound false; equivalence fails at p = 241, 769, 20521, 21841) |
| §6 (EVIDENCE) | SOUND — 211 odd / 174 even reproduced; congruence facts re-derived |
| §7 Lemma 7.1 | SOUND (matrix sign slip, D9 minor) |
| §7 matching (ii) + `wr_diag` count | SOUND numerically (2093/2212 reproduced); "face of the principal river" false (D10 minor) |
| §8 | SOUND algebra; "PROVED" should be "algebra PROVED + Assessment" (D11 minor) |
| §9 | SOUND-AFTER-REPAIRS (inherits D5; identity piece omitted, D12 minor) |
| §10 Lemma 10.1 | SOUND-AFTER-REPAIRS (D13 MAJOR: fails for content-2 forms, 134/320 certificates) |
| §10 Comp. 10.2 | SOUND (reproduced; actually PROVABLE — proof supplied, D14) |
| §10 Prop 10.3 core (norm mod ℓ is a class invariant only mod squares; t | 24) | SOUND |
| §10 Prop 10.3 boxed scope "every mechanism that factors through classes" | GAP → SOUND-AFTER-REPAIRS (D15 MAJOR: contradicts 10.2 as worded) |
| §10 ring-class remark | provable negative; mis-describes ray class groups, which *do* escape (D16) |

**Overall.** No FATAL defect. Four MAJOR defects (D3, D5, D13, D15), all with local repairs that leave every conclusion
of the document (all negative / Assessment-level) intact. Labels are generally honest; the main over-reach is the boxed
scope sentence of Prop 10.3. All key numbers (§1 to 20000, §2's 15/267 and 78, §4's six counts, §6's 211/174, §7's
2093/2212, §10's 320 and zero collisions) were reproduced with independent code.


## §1 — Zagier windmill ↔ rivers

**Independent check** (`scripts/review_wr_zagier.py lo hi`). h⁺(p) is computed *without* the river map R: Gauss-reduced
indefinite forms of disc p, cycles of the standard ρ-operator (Buchmann normalisation), canonical cycle representative.
Then: ζσ-cycles on X(p) are enumerated, each cycle's forms `[y,x,−z]` are reduced to a class; checked that (a) each cycle is
contained in one class, (b) cycles ↔ classes is a bijection, (c) `#cycles = h⁺(p)`, (d) `2·|cycle| = ` R-period of the river
(R as defined in the doc, implemented separately), (e) ζ maps the cycle of C onto the cycle of `[a,−b,c]` = C⁻¹ and is
self-paired iff C is principal; ζ is verified to be an involution of X(p).
Result: **0 failures for all 1125 primes p ≡ 1 (4), p < 20000** (author: p ≤ 1300). p = 1297 reproduces
h⁺ = 11 and cycle lengths `[11,11,11,11,13,13,17,17,21,21,37]` (doc writes `[11,…,37]`, consistent). Class numbers
h(229)=3, h(257)=3, h(401)=5, h(577)=7 agree with tables.

The "Reading" paragraph: `σρσ = σζ = ρ⁻¹` and `ζρζ = σζ = ρ⁻¹` verified by hand. Fixed points: ζ fixes exactly
`x = y` (middle piece), giving `(1,1,(p−1)/4)` ↦ principal form; σ fixes `y = z` ↦ `[a,b,−a]`. Correct.
Genus theory: disc p prime ⇒ one genus, 2-rank 0, h⁺ odd, principal class the only ambiguous one. Correct.

Verdict: **SOUND**, with two minor presentation defects (D1, D2).

## §2 — class-group form of Type II

**Re-derivation of Lemma 2.4.** `B = 4gb`, `B² − 4kc = −4gp` ⇒ `kc = g(p + 4gb²)`. `4gb | k+1` ⇒ `gcd(k,g) = 1` ⇒ `g | c`,
so `c = ge`, `ke = p + 4gb²` (the doc asserts `c = ge` without this one-line reason; fine). `ke ≡ p`, `k ≡ −1 (mod 4gb)`
⇒ `4gb | p + e`. `N = (p+e)/4`, `bg | N`, `α = N/(bg)`, `β = b`. `4N ≡ p ≡ −4gb² (mod e)` ⇒ `4gb(α+β) ≡ 0 (mod e)`;
`e ≡ −p (mod 4)` is odd and a common prime of e and bg divides `ke − 4gb² = p`, so `e | α+β` once `p ∤ bg`.
The bound `bg < p`: with `X = 4gb`, if `bg ≥ p` then `X ≥ 4p`, `e ≥ X − p ≥ 3X/4`, `k ≥ X−1`, so
`(3X/4)(X−1) ≤ ke = p + Xb ≤ X/4 + X²/4`, i.e. `X ≤ 2`, contradiction. Correct. Integrality of y, z and the identity
are then immediate. **But all of this uses `k > 0` (hence `c, e, N > 0`)**, which Lemma 2.4 does not state — see D3.

**Bound `b ≤ (p+1)/3` (Comp. 2.3, g = 1).** `k ≥ 4b−1`; if `4b > p` then `e ≥ 4b − p`; `(4b−1)(4b−p) ≤ p + 4b²` ⇔
`12b² ≤ 4b(p+1)`. For `4b ≤ p` the bound is automatic. So the search range is exhaustive. Correct.

**Independent computation** (`scripts/review_wr_esforms.py 20000`, enumerates for each b the smaller of the two cofactors
in its residue class): 267 primes; **no ES-form for exactly 15** = {97, 193, 673, 1033, 1297, 1777, 2473, 3361, 6481, 7681,
7753, 8017, 9433, 12433, 15313}; **78 with no reduced ES-form** — both match the doc. Lemma 2.4's explicit formula
verified exactly (Fractions) on 11575 positive ES-forms, p < 3000, g ≤ 5 (doc: 4360 instances; different enumeration).

Cor 2.2's equivalence `4b | p+e ⇔ 4b | k+1` (for `p ∤ b`): both directions force e odd and `gcd(e,b) | p`; correct.

## §3–§4 — negative EVIDENCE (spot-check of §4)

`scripts/review_wr_typeI.py 3000 6 6` decides membership of a factor pair in the class of `[c,p,−cd]` by **Gauss reduction**
(no river walk): a pair `{f, g = D/f}` is "in the class" if one of its four ambiguous forms `[±f, f, ·]`, `[±g, g, ·]`
reduces to the class of `[c,p,−cd]`. Result: 46 primes, 1655 (c,d) cases, 1244 ambiguous classes, **1941 / 5896** pairs in
class, **20 / 82** certificate pairs in class — every number in §4 reproduced. (Using only `[f,f,·]`, f < √D, gives
1316/5896 and 8/82: the four forms of one pair can lie in two different narrow classes, so §4's "ambiguous forms on a river
↔ factor pairs" is not a bijection — D4.) Extension to all 267 primes p ≡ 1 (24) ≤ 20000, c, d ≤ 6: 11178/40443 = 27.6% of
pairs vs 89/456 = 19.5% of certificate pairs; restricted to primitive pairs 31.4% vs 23.9%. The "no enrichment" EVIDENCE
holds up (if anything mild depletion).

## §5 — structural items

**5.2.** `AB − pt = 1` ⇒ disc of `[p, B−A, −t]` is `(B−A)² + 4(AB−1) = T² − 4`. "⇒" of `A ≡ B ≡ −1 (t) ⇔ T ≡ −2 (t), t | B−A`
is clear; "⇐" gives `2A ≡ −2 (t)`, so needs t odd. In the slice `4 | A`, p ≡ 1 (4): `−pt ≡ 1 (4)` ⇒ `t ≡ 3 (4)`, odd. Fine (D7).

**5.3 (defect found).** `A ↦ A + kp` (t ↦ t + kB) and `B ↦ B + lp` are commuting integral symmetries — correct. But the
claim "in each orbit only the representative with `A, B ≤ p + O(1)` can satisfy `t | A+1, t | B+1`", and the resulting
equivalence "X-slice ES(p) ⟺ some `A ∈ [1,p)`, `4 | A`, `B = A⁻¹ mod p` with `t | A+1, B+1`", are **false**. Derivation:
if `B ≥ p` then `pt = AB − 1 ≥ pA − 1` ⇒ `t ≥ A`, and `t | A+1` forces `t = A+1`; symmetrically `A ≥ p` forces `t = B+1`,
`A = p + (p+1)/B`. The correct bound is `max(A,B) ≤ p + (p+1)/min(A,B)`, not `p + O(1)`. For p ≡ 1 (24) the case `B ≥ p` is
impossible (`4 | A | p+1` contradicts `p+1 ≡ 2 (8)`), but `A ≥ p` occurs: it is exactly the **v = 1 family**
`u(t−1) = p+1`, `u ≡ 3 (4)` (exists iff `(p+1)/2` has a divisor ≡ 3 (4)). Example p = 97: `(t,u,v) = (15,7,1)`, `A = 104 > p`,
`B = 14`, `AB − pt = 1456 − 1455 = 1`, `15 | 105`, `15 | 15`; its box representative `A mod p = 7` is not ≡ 0 (4).
`scripts/review_wr_Eset.py 30000` (direct enumeration of E(p)): 447 of the 3473 certificates for the 385 primes p ≡ 1 (24)
≤ 30000 lie outside the box, all in the v = 1 family; for **p = 241, 769, 20521, 21841 every certificate is outside the box**
(p = 241: E = {(23,11,1)}, A = 252), so the stated equivalence fails there. See D5.

**5.1.** The p ↦ −p algebra is fine. The rest (no cycles on the definite side, available involutions are class-group
involutions, fixed points = genus data) is heuristic and should not sit under a PROVED header (D6).

## §6 — parity of |E(p)|

`scripts/review_wr_Eset.py 30000` reproduces: 385 primes, |E(p)| odd for **211**, even for **174**. `|E(m²)| = 0` checked
for odd m < 300 (doc: odd squares). "|X(p)| always odd": the involution u ↔ v on `{tuv − u − v = p}` has fixed points
`u(tu−2) = p` ⇒ only `(p+2,1,1)`; correct (but note the symbol clash: this X is not §1's Zagier set X(p) — D8). For
p ≡ 1 (24), `4 | A` ⇒ `t ≡ u ≡ 3 (4)`, and `v ≡ 3 (4) ⇔ 4 | B`: re-derived, correct. The 283-sub-count search was not
re-run (EVIDENCE, negative; low stakes).

## §7–§9

**Lemma 7.1.** `σ_k[a,b,c] = [−c/k, b, −ka]`: disc `b² − 4ac` preserved, simple, involution (`k | −ka`), fixed points
`[a,b,−ka]`, `Δ = b² + 4ka²`. Correct. The matrix description is off by a sign: `−(1/k)·φ(ky, x) = [−c/k, −b, −ka]`; the map
is `−(1/k)·φ∘W` with the Fricke matrix `W = [[0,−1],[k,0]]` (det k), not `[[0,1],[k,0]]` (D9; same slip in Obs. 1.1 for σ).

**Diagonal transport (ii).** Re-derived the k-range: `(k+1)² ≥ 16g²b² = 4g(k² − p) ≥ 4(k²−p)` ⇒ `3k² − 2k − 1 ≤ 4p`. Correct.
`scripts/review_wr_diag.py 200000`: **2093 of 2212** primes p ≡ 1 (24) < 2·10⁵ have no diagonal certificate; no odd square
< 2·10⁵ has a coprime one — both reproduced. But every certificate has `p > 4g = disc/4`, while river faces of disc 16g have
values `≤ 16g/4 = 4g` (`a|c| = (D − b²)/4`); so p is a value of the principal form, never a face *on the river* (D10).

**§8.** With `A = tu−1`, `B = tv−1`: `A − B = t(u−v)`, `T + 2 = t(u+v)`, `4p = t(τ² − β²) − 4τ` ⇔ `p = tuv − u − v`. Correct.

**§9.** Inherits D5 (box). Automorphisms of the curve `xy = 1` over 𝔽_p are `A ↦ cA^{±1}` (the `−c` variants are already
included; 2(p−1) maps, not "p−1 pieces"). "Any fixed point it creates is a root of a fixed quadratic" omits the identity piece
(c = 1, exponent +1), which fixes its whole region (D12). "Lemma 4.1" and (§5.3) "Prop 4.2(d)" refer to INVOLUTION_ES.md, not
this file — say so.

## §10 — Bhargava cubes / class shadow

**Lemma 10.1.** `[m,2,m'']` has disc `4 − 4(tp+1) = −4tp`; `𝔪 = ℤm + ℤ(1+ω)` (ω = √−tp) is an O-module of index m with norm
form `[m,2,m'']`; `𝔪𝔪'' ⊆ (1+ω)` always, and `𝔪𝔪'' = (1+ω)·(m, m'', 2, 1+ω)`. **Equality fails when m and m'' are both
even**: then `[m,2,m'']` is non-primitive (content 2), 𝔪 is not invertible in `O = ℤ[√−tp]` (conductor 2 since
`−tp ≡ 1 (4)`), and the form is not in Cl(−4tp). This is not a corner case: `scripts/review_wr_cube.py 5000 39` finds
**134 of the 320 certificates** have m'' even (m ≡ 0 (4), tp+1 ≡ 0 (8)). They are `2·[m/2, 1, m''/2]`, i.e. classes of
Cl(−tp) for the maximal order, with generator (1+ω)/2. See D13.

**Computation 10.2 — reproduced, and in fact PROVABLE.** Independent definite reduction: 760 (p,t) cases, **0 non-trivial
collisions**, exceptions only {1,N}, {2,N/2}, 320 certificates in 320 distinct classes — matches. A general proof (valid for
forms of any content, all p, t): if `Q₁ = [m₁,2,m₁'']` ~ `Q₂`, then Q₁ primitively represents m₂: `(m₁x+y)² + tp·y² = m₁m₂`.
If `m₁m₂ < tp` then y = 0, x = ±1, m₂ = m₁. Since Q ↦ Q'' = [m'',2,m] ~ Q∘diag(1,−1) preserves equivalence, the same holds if
`m₁''m₂'' = N²/(m₁m₂) < tp`. Otherwise `tp ≤ m₁m₂ ≤ N²/tp < tp + 3`, and as m₁, m₂ | N = tp+1 this forces `m₁m₂ = N`,
`m₂ = m₁''`; then the representation of m₁'' with the right root needs `y = ±1`, `(m₁x ± 1)² = 1`, and checking the middle
coefficient (`≡ −2` vs `2 (mod 2m₁'')`) leaves only `m₁ or m₁'' ∈ {1, 2}`. ∎ So 10.2 can be relabelled PROVED (D14).

**Proposition 10.3.** The core computation is right: principal norms are `x² + tpy² ≡ x² (mod ℓ)`, every nonzero square occurs
(y = 0), hence `[𝔞] ↦ N𝔞·(ℤ/ℓ)^{*2}` is the only norm-residue class invariant; for composite odd t the shadow is
`N𝔞 mod (ℤ/t)^{*2}`, i.e. the tuple of `(m/ℓ)`, and `m ≡ −1 (t)` is a class predicate iff `(ℤ/t)^*` has exponent 2 iff `t | 24`.
`review_wr_cube.py` part (b) confirms for 5 (p,t,ℓ) that each primitive class of disc −4tp, *and of disc −4tp·ℓ² (ring class
group of conductor ℓ)*, takes exactly one square class of values mod ℓ. Bhargava's parametrisation (projective cubes mod
SL₂(ℤ)³ ↔ balanced triples mod `(I_i, δ) ↦ (κ_iI_i, κ₁κ₂κ₃δ)`, group ≅ Cl × Cl) is quoted correctly from memory (source PDF
not in `sources/`; not checked against the paper). **But the boxed scope claim is overstated** (D15, D16):
(1) by 10.2 the class map is injective on the divisor set, so on that set *any* function of 𝔪 — including `[m ≡ −1 (t)]` —
*is* a function of `[𝔪]`. What 10.3 proves is narrower: no function F on Cl satisfies `F([𝔞]) = [N𝔞 ≡ −1 (t)]` for *all*
ideals 𝔞 coprime to t (unless t | 24); a class mechanism that knows the labelled hypercube `∏𝔮_i^{ε_i}` (i.e. the factorisation
of tp+1) escapes, and that is B2 again. (2) Fixed-point counts of the `S₃ ⋉ (ℤ/2)³` action on `{(C₁,C₂,C₃): ΣC_i = 0}` are
not only 2-/3-rank data: e.g. the transposition fixes `C₁ = C₂`, a set of size h. (3) The ring-class remark: "I do not expect
it to help, but I have not proved that" — it **is** provable by the same two lines: in any order of K, principal norms of
elements prime to ℓ are squares mod ℓ (ℓ ramified in K, norm form `≡ (x + y·(trace)/2)²`), and all squares occur. But the
description "(O/f)^*/(ℤ/f)^* records the residues of generators" is what *ray* class groups do: in `Cl_{(t)}(K)`, 
`𝔞 ↦ N𝔞 mod t` is a well-defined homomorphism onto a subgroup of `(ℤ/t)^*` (α ≡ 1 mod* t ⇒ Nα ≡ 1 (t)), so ray class
groups *do* see the full condition. This is the correct form of the doc's own "κ_i restricted to a congruence subgroup".

## Defects (numbered; FATAL / MAJOR / MINOR)

**D1 (MINOR, §1 "Reading", line "The principal cycle has odd length L_1/2 (because |X(p)| = Σ_C L_C/2 …)").**
The oddness of `|X(p)|` is itself obtained from ζ having a unique fixed point — i.e. Zagier's argument. So the sentence
"Zagier's proof is the statement *the principal river has odd half-period*" is a *reformulation*, not an independent
proof route: in the doc the odd half-period is derived from Zagier, not vice versa. Repair: say explicitly that the
odd half-period is equivalent to (and here deduced from) the ζ-fixed-point count; an independent proof is Smith's /
Legendre's continuant-palindrome argument (cite where it shows the principal period is odd for p prime ≡ 1 (4)).

**D2 (MINOR, §1 Computation 1.2 / "Reading" label).** The Reading is "PROVED given 1.2's structure", but 1.2 (i)–(iii) is
only CERTIFIED for p ≤ 1300 (now p < 20000 by R164). As written, the general dictionary is CONDITIONAL on a statement
proved nowhere in the doc. It is in fact a known theorem (folklore; e.g. the literature on "Zagier's one-sentence proof
and reduction of binary quadratic forms"); either give a reference or a proof sketch (each ζσ step is a composite of
R-steps, by Observation 1.1, and covers exactly two R-steps), or relabel the general statement CONDITIONAL/folklore.

**D3 (MAJOR — false as stated, trivial repair; §2 Lemma 2.4 statement, and AGENT_REPORT_O164 Results item 2).**
Lemma 2.4 says "a form `[k,B,c]` of discriminant −4gp"; it omits *positive definite* (Cor 2.2 has it). Without it the
statement is false — it would prove ES for every p: `[−1, 4g, −g(p+4g)]` has disc `16g² − 4g(p+4g) = −4gp`, `4g | B`,
`B | k+1 = 0` (script part (c)). The proof silently uses `k > 0` (positivity of e, N, y, z). Repair: insert
"**positive definite** (i.e. k > 0)" in Lemma 2.4 and in the report's restatement; add the one-line reason
`gcd(k, g) = 1 ⇒ g | c` for `c = ge`.

**D4 (MINOR, §4 sentence "Ambiguous forms on a river ↔ factor pairs of D").** Not a bijection: a coprime pair `{f, D/f}`
carries up to four ambiguous forms `[±f,f,·]`, `[±D/f, D/f, ·]` which can fall into two narrow classes; non-primitive pairs
(gcd(f, D/f) > 1) lie on no primitive river yet are counted in the denominator 5896 (688 of them). The conclusion is unaffected
(primitive-only baseline: 37.3% vs 30.8% at the doc's range). Repair: state the convention ("a pair is on the river if any of
its ambiguous forms is") and report the primitive-only ratio too.

**D5 (MAJOR, §5.3 "only the representative with A, B ≤ p + O(1)" and "X-slice ES(p) ⟺ some A ∈ [1, p) …"; propagates to
§9 first paragraph "unique box representative A, B ≤ p + O(1)" and `H_p = {(A, Ā) : 1 ≤ A < p}`).** False as stated: the
v = 1 family `u(t−1) = p+1` has `A = p + (p+1)/B ≥ p`; 447/3473 certificates (p ≡ 1 (24), p ≤ 30000) are of this kind and
p = 241, 769, 20521, 21841 have *only* such certificates. Repair: replace "p + O(1)" by `max(A,B) ≤ p + (p+1)/min(A,B)`, and
state the equivalence as "X-slice ES(p) ⟺ [a box point with 1 ≤ A, B < p] **or** [(p+1)/2 has a divisor u ≡ 3 (mod 4)]
(the v = 1 family, A = p + (p+1)/B)". In §9 either enlarge H_p by these boundary points or note that the v = 1 family is a
trivially explicit divisor family of p+1 outside the hyperbola picture. The qualitative conclusions of §5.3/§9 survive.

**D6 (MINOR, §5.1 header "PROVED for the Type II slices of Lemma 2.4").** Only the sign-flip algebra is proved. "A finite
reduction-closed set of forms is a union of classes" is false or vacuous as written (definite classes are infinite; the set of
reduced forms is reduction-closed and finite but not a union of classes), and "the reduction-type involutions available are
class-group involutions" is an unproved heuristic. The parenthetical "(always available)" for signed solutions is also not
proved from the formula given. Repair: split into "PROVED: sign flip p ↦ −p" and "Assessment: …", fix the union-of-classes
sentence (e.g. "a finite set of reduced forms carries no SL₂(ℤ)-action, so reduction gives no rotation").

**D7 (MINOR, §5.2 "equivalent to T ≡ −2 (mod t) and t | B − A").** The reverse implication needs t odd; add "(t is odd:
4 | A and p ≡ 1 (4) force t ≡ 3 (4))".

**D8 (MINOR, §6 "|X(p)| is always odd").** X(p) here means `{(t,u,v): tuv − u − v = p}`, not §1's Zagier set; rename
(e.g. `X'(p)`) or define it.

**D9 (MINOR, §7 Lemma 7.1 "Atkin–Lehner/Fricke matrix `[[0,1],[k,0]]`"; §1 Obs. 1.1 "σ(φ) = −φ∘(e₂, e₁)").** Sign slip:
`−φ∘(e₂,e₁) = [−c,−b,−a]`, but σ is `[−c, b, −a]`; use `(e₂, −e₁)` (det 1). Likewise σ_k = `−(1/k)·φ∘[[0,−1],[k,0]]`
(the standard Fricke matrix). The "equivalent to the negative" conclusion is unaffected.

**D10 (MINOR, §7 (ii) "Here p is a face value of the principal river of disc 16g").** False: river faces of disc 16g have
values ≤ 4g, while every diagonal certificate has `p > 4g` (k-range ⇒ `4gb² ≤ p/3`; checked: 0 exceptions below 2·10⁵).
Repair: "p is a value of the principal form x² − 4gy² of disc 16g (off the river)".

**D11 (MINOR, §8 header "PROVED, algebra").** The algebra is proved; "no free joint factorisation / no H-A gain" is an
Assessment. Relabel.

**D12 (MINOR, §9).** (a) inherits D5; (b) the −c variants duplicate `A ↦ cA^{±1}`; (c) the identity piece fixes everything
on its region, so "any fixed point it creates is a root of a fixed quadratic" needs "non-identity pieces"; (d) "Lemma 4.1",
"Prop 4.2(d)" are INVOLUTION_ES.md references — cite the file.

**D13 (MAJOR, §10 Lemma 10.1 "`𝔪𝔪'' = (1+√−tp)`", "certificates are exactly ideal divisors … (Heegner discriminant
−4tp)"; Computation 10.2 "the 320 classes … of Cl(−4tp)"; Bhargava "balanced triple").** When m and m'' are both even
(134 of the 320 certificates in the doc's own range) the form `[m,2,m'']` has content 2, 𝔪 is a non-invertible ideal of
ℤ[√−tp], `𝔪𝔪'' = (1+ω)(2,1+ω) ≠ (1+ω)`, the cube is not projective, and the class is not in Cl(−4tp). Repair: split by
the parity of m'': for m'' odd keep the statement; for m'' even use `O_K = ℤ[(1+ω)/2]`, the form `[m/2, 1, m''/2]` of
disc −tp, the ideal `(m/2, (1+ω)/2)` and `δ = (1+ω)/2`. Prop 10.3's argument applies verbatim in Cl(−tp) (norm form
`x² + xy + ((1+tp)/4)y² ≡ ((2x+y)/2)² (mod ℓ)`), so §10's conclusions survive.

**D14 (MINOR, §10 Computation 10.2 label).** CERTIFIED undersells it: the injectivity (with exactly the exceptions {1,N},
{2,N/2}) has a short general proof (given in the §10 body above). Relabel PROVED and include the proof; keep the
computation as a check.

**D15 (MAJOR, §10 Prop 10.3 boxed conclusion "every mechanism that factors through classes of forms or cubes … can test
`m ≡ −1 (mod t)` only through its quadratic shadow"; "The full condition is class data only when t | 24").** As stated this
contradicts 10.2: on the divisor set the class map is injective, so `[m ≡ −1 (t)]` *is* a function of the class there. The
correct (and proved) content is: (i) no function F on Cl(−4tp) satisfies `F([𝔞]) = [N𝔞 ≡ −1 (t)]` for all ideals 𝔞 ⊥ t of
the class unless `(ℤ/t)^*` has exponent 2; equivalently (ii) any test that depends on the ideal only through its class and
must be correct for *every* ideal of that class sees only the genus characters `(·/ℓ)`, ℓ | t. A mechanism that uses the
class *together with the labelled divisor hypercube* (equivalently, the factorisation of tp+1) escapes, and is B2. Also the
parenthetical "fixed-point counts (which are 2- and 3-rank data of Cl)" omits counts like h (the transposition on
`{ΣC_i = 0}` fixes h triples). Repair: restate the boxed sentence as (i)/(ii) and add one sentence on the hypercube.

**D16 (MINOR, but important for direction; §10 Assessment "ring class group … records the residues of generators. It does
not record norms beyond squares, so I do not expect it to help, but I have not proved that").** (a) The negative statement
for ring class groups is provable in two lines (every order: principal norms prime to ℓ are squares mod ℓ since ℓ | tp is
ramified; all squares occur). Upgrade to PROVED. (b) "records the residues of generators" is the description of *ray*
class groups; and for those the conclusion flips: in `Cl_{(t)}(K)` the map `𝔞 ↦ N𝔞 mod t` is a well-defined homomorphism
(α ≡ 1 mod* t ⇒ Nα ≡ 1 (t)), so the certificate condition is ray-class data. Say explicitly that ray class groups mod t
(= the doc's "κ_i restricted to a congruence subgroup") are the minimal class-type structure that escapes 10.3, and that
on them the problem is "does the divisor hypercube of (1+ω) meet the coset `N ≡ −1 (t)`" — an equivalent restatement,
not progress.
