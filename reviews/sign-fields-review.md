# R235 — hostile review #1 of O232 (SIGN_FIELDS.md, BRAINSTORM/z8_*.md, data/z8/)

Reviewer: R235 (side-agent/review-sign-fields). Merged side-agent/sign-fields at 069d5e83 (README conflict resolved by
keeping both sides). From-scratch scripts: `scripts/review_r235_cert.py` (certificate checker, sympy, no ec_cert/z8
imports), `scripts/review_r235_brute.py` (independent ES solver via (ay − d)(az − d) = d²), further `scripts/review_r235_*.py`.

**Repairs applied (R235 only):** SIGN_FIELDS.md D1, D3, D4, D5, D6 (+ ν-odd strengthening), D7, D8, D9 and memo
z8_eight_failures_frobenius D7, each marked "(R235 repair)". Author's last commit (86675a30, agent report caveat) predates the
review; no author activity during the review. No change to any certificate or claim label.

**Overall: no FATAL defect. Headline Thm 1.3 is SOUND (independently re-certified). One MAJOR (D5: wrong u ≡ 3 (4)
parenthetical inside Thm 2.2(d); conclusion survives, strengthened). Rest MINOR.**

## Summary verdicts
(filled in progressively; see sections below)

| claim | verdict |
|---|---|
| Thm 1.3 (ES for all 4^s + k, nine k) | SOUND (label PROVED, computer-assisted, justified) |
| Lemma 1.1 (non-trivial k ≡ 9 mod 24 for c₀ = 1) | SOUND |
| Lemma 1.2 (no integer unit-square points, c₀ = 1) | SOUND |
| §1.4 OPEN list, k = 105 hardness, Λ₁₀₅ ∩ Sq^× = ∅ at L = 360 | SOUND-AFTER-REPAIRS (D3, D4 minor) |
| §1.4 mixed point μ* for k = 105 (EVIDENCE) | SOUND as EVIDENCE |
| Prop 2.1 (ν-slots as Frobenius set C_ν) + decompositions | SOUND |
| Thm 2.2 (a)–(c) | SOUND (D6 minor hypothesis) |
| Thm 2.2 (d) uniqueness of 4 | SOUND-AFTER-REPAIRS (D5: the u ≡ 3 (4) parenthetical is wrong) |
| §2 numerics, 8/131, 8/241 | SOUND-AFTER-REPAIRS (D7: χ sign at 131, word count) |
| Prop 3.1 (single level sees only r mod 4u) | SOUND (trivial; D8 wording) |
| §3 Consequence, §4 Chebotarev-in-family | SOUND as Assessment (relies on O225 Lemma 4.2, under R228) |
| Novelty | modest, correctly self-assessed (D1 sharpening) |

## 1. Theorem 1.3 — headline

**Independent checker** (`scripts/review_r235_cert.py 300`). Semantics re-derived from the JSON: n_s = 4^s + c,
class (M, r), x, y, z ∈ ℚ[n] given low-degree-first. For every class of all nine certificates:
1. 4xyz − n(xy + yz + zx) = 0 in ℚ[n] (sympy expansion): all 30 classes pass.
2. Integrality: with D = lcm of coefficient denominators, D·p ∈ ℤ[n] and D·p(n) mod D is D-periodic in n, so
   checking n = r + Mt for t < D/gcd(D, M) is exhaustive (different method from ec_cert's finite differences): pass.
3. Positivity: largest real root R of each coordinate (sympy real_roots), positive leading coefficients; class used only
   when n > R, else falls back to brute force: pass.
4. Periodicity (re-derived): write M = 2^e M′. For s ≥ ⌈e/2⌉, 4^s ≡ 0 (mod 2^e) so n_s ≡ c (mod 2^e); and
   n_{s+L} − n_s = 4^s(4^L − 1) ≡ 0 (mod M′) iff M′ | 4^L − 1 (checked: pow(4, L, M′) = 1). Hence n_s mod M depends only
   on s mod L for s ≥ S₀ = max⌈e/2⌉ (S₀ = 1 for k = 225 because of M = 2716 = 4·679, else 0). Coverage of the L residues
   from S₀ on: pass; redundant direct check n_s ≡ n_{s+L} ≡ n_{s+7L} (mod M): pass.
5. Exact integer verification of a class solution for every s ≤ 300: pass. Only s = 0, k = 225 (n = 226, even) needed
   brute force: (57, 6442, 41492922).
6. Independent brute force (no certificate) for s ≤ 20 for all 13 offsets k ≡ 9 (mod 24), k ≤ 297
   (`review_r235_brute.py 20`): all solvable.
The author's checker `ec_cert.py` (run with MMAX = 600) also passes all nine — consistent with the claim.

**T1 / square control.** Squares in the families come from (a − 2^s)(a + 2^s) = k. Complete list (s ≥ 0):
k = 9: s = 2, 25 = 5²; k = 57: s = 3, 121 = 11²; k = 129: s = 6, 4225 = 65²; k = 153: s = 2, 169 = 13²;
k = 201: s = 5, 1225 = 35²; k = 225: s = 3, 289 = 17²; none for k = 81, 177, 249. My checker confirms each of these is
covered by a **divisor class** D_q with q | a (D₅, D₁₁, D₅, D₁₃, D₅, D₁₇ respectively) — real solutions obtained by
scaling ES(q), not a polynomial ET family "solving" a square (which would contradict Mordell/Schinzel). No non-D class
contains a square member (the ec_cert T1 test to s < 20000 also passes). Note that k = 81 is a square but 4^s + 81 is never
a square (factor pairs (1,81), (3,27) give 2^{s+1} ∈ {80, 24}).

**Mordell-hard members.** Recomputed residues mod 840 for s ≥ 2: k = 57: s ≡ 3 (6) → 121; 153: s ≡ 2 (6) → 169;
177: s ≡ 5 (6) → 361; 225: s ≡ 3 (6) → 289, s ≡ 0 (6) → 121; k = 9, 81, 129, 201, 249: no hard members. Matches §1.3.
**Survey list.** k ≡ 9 (mod 24), k ≤ 300: 9, 33, …, 297 = 13 offsets; 9 certified + 4 OPEN — consistent.

Verdict Thm 1.3: **SOUND**. Defects are presentational only (see D1, D2 below).

## 2. Lemma 1.1, Lemma 1.2

**Lemma 1.1.** For s ≥ 2, c₀4^s ≡ 0 (mod 16), so n_s ≡ k (mod 8); 4 ≡ 1 (mod 3) gives n_s ≡ c₀ + k (mod 3). Mordell's six
classes 1, 121, 169, 289, 361, 529 (mod 840) are all ≡ 1 (mod 24), and every odd n outside them is ES-solvable by
Mordell's identities. For c₀ = 1: k ≡ 1 (8), k ≡ 0 (3) ⟺ k ≡ 9 (24). Correct. (Implicitly k odd; s ∈ {0, 1} are finitely
many members and are irrelevant to "non-trivial".) **SOUND.** Note "non-trivial" only means "not killed by Lemma 1.1";
five of the nine certified k are nevertheless Mordell-trivial for all s (D1).

**Lemma 1.2.** Re-derived: with EXPONENT_COVERING's conventions (2-component of ν(μ) is the constant k, odd components
4^μ + k), for ℓ ≥ 0 the odd components are the odd integer N = 4^ℓ + k ≥ 4, which has an odd prime factor q, so ν(ℓ)_q is
not a unit — squareness is not even needed (the author's "N = s² with s a power of 2" detour is correct but redundant). For
ℓ = −a < 0, (1 + k4^a)/4^a is a q-adic unit for all odd q iff the odd integer 1 + k4^a is 1, impossible for k ≥ 1. **SOUND.**
It only excludes *integer* ℓ; non-integer μ ∈ Ẑ can still be unit-square points — the doc says so ("(EH)" is checked
separately by the screen). Fine.

## 3. §1.4 OPEN offsets and k = 105 (`scripts/review_r235_k105.py`)

* Integer square points (search ℓ ∈ [−79, 79]): k = 33: ℓ = 2 (7²), 4 (17²), −2 (23²/16) ✓. k = 105: 2, 3, 4, −2 ✓.
  **k = 273: ℓ = 2 (17²) AND ℓ = 4 (4⁴ + 273 = 529 = 23²) — the doc omits ℓ = 4 (D3).** k = 297: ℓ = 3 (19²) ✓.
* k = 105: every member s ≥ 2 lies in Mordell's hard set, all six residues occur (checked s < 400) ✓; n_s ≡ (2^s)² (mod 105) ✓.
* Unit-square screen, L = 360 (own code, same logic: survivor ⟺ for every prime q < 3·10⁶ with q | 4³⁶⁰ − 1, n_s mod q is a
  non-zero QR). **0 survivors**; in fact primes ≤ 181 already suffice. The deduction Λ₁₀₅ ∩ Sq^× = ∅ is valid: for any
  μ ∈ Ẑ, ν(μ)_q mod q = 4^{μ mod ord_q 4} + 105, so the residue s = μ mod 360 transfers the kill. **CERTIFIED, SOUND.**
* k = 33 screen: for L = 180, 360, 720 the only survivor is s ≡ −2 ✓, and ord₂₃(4) = 11 so D₂₃ needs 11 | L ✓. But for
  L = 60 and 120 there is a second survivor (s ≡ 34 mod 60, s ≡ 94 mod 120) — a mixed point (≡ 4 at 3, 5; ≡ 2 mod 4),
  killed once 9 | L. "At every L tested" is therefore true only if no L with 9 ∤ L ≥ 60 was tested (D4). (It actually
  supports the author's mixed-point picture.)
* Mixed point μ* for k = 105: 124 ≡ (4 mod 8, −2 mod 9, 4 mod 5) ✓; 844 ≡ (4, −2, 4, 4) mod (8, 9, 5, 7) ✓.
  ord₁₈₁(4) = 90 = 2·3²·5, μ* ≡ 34 (mod 90), n ≡ 85 (mod 181), (85/181) = −1 ✓. ord₉₁₉(4) = 153, μ* ≡ 106 (mod 153),
  n ≡ 551 ≡ −4·2²·23 (mod 919), and 4·2·23 | 920: μ* lies in the ET family II2 (a, d, f) = (2, 23, 919) ✓.
  The reading "q with ord_q(4) a 2·3-power ⇒ n ≡ (41/4)²" is right only for ord = 3^b or 2·3^b (needs 4 ≡ −2 mod 2^a, a ≤ 1);
  "2·3-power" should be spelled "of the form 3^b or 2·3^b" (part of D4). The adaptive-covering Haar measures are EVIDENCE
  produced by author code; not replayed (scope: EVIDENCE only, claim is explicitly weak and not a certificate).

## 4. §2 — Prop 2.1, Thm 2.2 (`scripts/review_r235_words.py 2000`, `scripts/review_r235_t1.py 60`)

**Decompositions** re-derived from AA* = tn + 1, Av = n + u, A*u = n + v: e.g. ν | u = νw:
tn + A* + 1 = tn + tv = t(n + v) = tuA* = νtwA*, giving ν/n = 1/(wA*) + 1/(tnw) + 1/(tnwA*); ν | A = νw:
nA* + n + v = ntv + v = v(tn + 1) = vAA* = νwvA*. Exact-rational check of all u/v/A/A* slots for every word of every prime
< 2000 and odd square ≤ 59², ν ∈ {3, 4, 5, 7, 8, 12}: 0 failures.

**Prop 2.1.** Re-derived: ν | u impossible (gcd), ν | A excluded, ν | v ⇒ ν | Av = n + u excluded; ν | t ⟺ ν | tu = A + 1;
ν | A* ⟺ (multiplying tv − 1 by the units u, A) (A + 1)(n + u) ≡ uA ⟺ An ≡ −(n + u). Combined with A ≡ −1 (mod u) and
CRT (gcd(ν, u) = 1) this is the stated C_ν. The two ν-classes are distinct since u ≢ 0 (mod ν). Brute-force comparison of
"ν divides a slot" with "A mod ν ∈ C_ν" on every word satisfying the hypotheses (primes < 2000 + odd squares ≤ 59²,
ν ∈ {3, 4, 5, 7, 8, 12}): **0 mismatches. SOUND.** (Note: "ν-word" = ν divides a *single* slot; split divisibility, e.g.
3 | t, 4 | A* for ν = 12, is not a ν-word — fine as a definition, but say so.)

**Thm 2.2 (a)–(c).** (a): odd A | m² + u, gcd(m, u) = 1 ⇒ every prime r | A has (−u/r) = 1, r ∤ 4u, so splits in ℚ(√−u);
σ_A fixes √−u while c moves it. ✓ (b): conductor of ℚ(√−u) divides 4u | νu when 4 | ν; u = 1 forces i ∈ ℚ(ζ_ν) ⟺ 4 | ν ✓.
(c): Chebotarev (Dirichlet + one quadratic condition suffices) gives r ≡ −1 (mod νu), (−u/r) = 1; m odd with
m² ≡ −u (mod r) exists; A = r, t = (r + 1)/u ≡ 0 (mod ν), v = (m² + u)/r: tuv − u − v = Av − u = m² ✓. **SOUND.**
Numerics: ν-words at odd squares 3² … 59²: 0 for ν = 4, 8, 12; 782/521/280 for ν = 3/5/7 ✓. Among coprime ν-words at
odd squares (ν = 3, 5, 7, 11) every odd-A one has √−u ∉ ℚ(ζ_{νu}), **including A*-slot ones** (which (a) does not
address). Reason (reviewer): for ν odd, gcd(ν, u) = 1, √−u ∈ ℚ(ζ_{νu}) ⟺ √−u ∈ ℚ(ζ_u), and then χ_{−u}(A) = χ_{−u}(−1) = −1
for every A ≡ −1 (mod u), contradicting splitting: the whole level is empty for odd A, not just the t-slot. Worth stating.

**Thm 2.2 (d).** For u ≡ 1 (mod 4), n ≡ 1 (mod 4): n + u ≡ 2 (mod 4), so the A*-class −(n + u)/n is ≡ 2 (mod 4), not a
unit mod ν; the coprime slot set is the single element c of the c-fibre (a coset of (ℤ/ν)^×, size φ(ν)); χ_{−u} is
non-trivial on that coset's group because √−u ∉ ℚ(ζ_u) but ∈ ℚ(ζ_{4u}); so forbidden half has relative size 1/2; c is in
it; equality ⟺ φ(ν) = 2 ⟺ ν = 4 (given 4 | ν). ✓ And Σ_u = ℚ(ζ_u, √−u) = ℚ(ζ_{4u}) for u ≡ 1 (4), so "4-word ⟺ σ_A = c
on Σ_u" ✓. **But the u ≡ 3 (mod 4) parenthetical is wrong (D5)**: then n + u ≡ 0 (mod 4), so the hypothesis ν ∤ n + u
of Prop 2.1 fails for ν = 4 and the v-slot opens: for odd A, v = (n + u)/A has v₂(v) = v₂(n + u) ≥ 2, so **every** odd-A
word at an odd level u ≡ 3 (4) is a 4-word, and (reciprocity) has χ = (A/n) = −1. Checked: 355 such words at primes
p ≡ 1 (4) < 2000, all with 4 | v and χ = −1. So at u ≡ 3 (4) the 4-slot set is the *whole* c-fibre = the whole forbidden
set — the identity "4-slots = T1-forbidden set" holds at every odd u, it is not "even smaller".

**8/131, 8/241.** Own brute force: 8/131 and 8/241 have no representation as a sum of three unit fractions ✓. Words
(t, u ≤ v): 22 for 131 (doc: 21), 16 for 241; 4-slot words 14 (131) and 6 (241) ✓; every slot value divisible by 4 is
≡ 4 (mod 8), no 8-slot ✓. But 131 ≡ 3 (mod 4): all 14 4-slot words of 131 have (A/131) = **+1** (the other 8 have −1), so
"(χ = −1)" is false with the convention χ(w) = (A/n); DEDEKIND Thm 4.5 and Thm 2.2(d) are stated for n ≡ 1 (mod 4) only.
At 241 ≡ 1 (mod 4) all six have χ = −1 ✓.

## 5. §3 non-genus layer, §4 Chebotarev-in-family

**Layer inclusions.** Quadratic subfields F ⊂ Σ_u ↔ order-2 characters ψ of G = Gal(Σ_u/ℚ) (G abelian); F imaginary ⟺
ψ(c) = −1; F splits every r ⟺ ψ(⟨σ_r⟩) = 1. Such ψ exists ⟺ c ∉ ⟨σ_r⟩G² (characters of the elementary 2-group
G/⟨σ_r⟩G² separate points). ✓ genus-clean ⇒ group-clean ⇒ clean (sub-products lie in ⟨σ_r⟩) ✓.

**Prop 3.1.** A odd, A | p + u ⟺ A = ∏ r^{a_r}, 0 ≤ a_r ≤ v_r (r ∤ u automatically since r | u, r | p + u ⇒ r | p, p > u
prime); level-u admissibility (A ≡ −1 mod u) and χ = −1 ⟺ σ_A = c on Σ_u ⊂ ℚ(ζ_{4u}) (O225 (i)–(ii), consistent with my
§4 re-derivation for u ≡ 1 (4) and with the u ≡ 3 (4) reciprocity check). So existence is the predicate "c ∈ {∏σ_r^{a_r}}",
a function of the multiset {(r mod 4u, v_r)}. **SOUND, and as trivial as labelled.**

**D8-type caveat (wording).** "no Frobenius in any non-abelian extension … Rédei symbols do not enter" is true of the
*decision function*, not of the *input*: which r divide p + u = m² + (k + u) as m varies is governed by
representation by the principal form of disc −4(k + u), i.e. by Frobenii in the ring class field of ℚ(√−(k + u))
(dihedral over ℚ). That constraint (product of the chosen prime-ideal classes is trivial in Cl) can a priori correlate the
σ_r's. The Consequence paragraph argues it cannot force anything beyond genus because H ∩ Σ_uF ⊂ genus field — that is the
right argument but it is only sketched (and rests on O225 Lemma 4.2, under R228). It is labelled Assessment, which is
correct; the phrase "do not enter" in Prop 3.1 should be "do not enter the decision function; they can only constrain its
input, and (Assessment) only through the genus field".

**§4.** Algebra checked: r | p + u, r ≡ −1 (mod u) ⟺ u ≡ −p (mod r), u | r + 1; with u < r, u = r − (p mod r); σ_r = c on
Σ_u adds (−u/r) = −1 ✓. (F1)–(F4) are correct reductions to B1/B2/B3/B6 at the level of Assessment; no claim stronger than
Assessment is made. SOUND as Assessment.

## 6. Novelty and literature
* Thm 1.3: a direct transfer of (J)22's method (EXPONENT_COVERING Thm 1.4, ec_cert format) from k·2^m + 1 to 4^s + k. No
  prior result on ES for families 4^s + k found (cursory web search, 2 queries; not exhaustive). Real content limited to
  k = 57, 177, 225 (D1). The observation that these are near-square families out of reach of polynomial families in m is
  correct (NEAR_SQUARE Thm 2.2) and is the interesting framing.
* Prop 2.1/Thm 2.2: a Galois-language restatement of DEDEKIND Thm 4.5 + FOUR_SPECIFIC Prop 1.1 ((−M/g) for g ≡ −1 mod M).
  New and clean: (b) "∀u ⟺ ℚ(i) ⊂ ℚ(ζ_ν)" and (d). **Possible upgrade (not claimed by the author):** (c) with u = 1 proves
  for *every* ν with 4 ∤ ν that some odd square m² has a t-slot ν-word (r prime ≡ −1 mod ν, r ≡ 1 mod 4, r | m² + 1); I
  checked that t-slot words give explicit ν/n decompositions on 260 test cases. If a t-slot word is a "Type I/II
  solution" in (J)46's sense, this upgrades (J)46 SHARP 2's failure half from CERTIFIED (M = 3, 5, 6, 7, 11, 19) to PROVED
  for all 4 ∤ M. Worth one sentence after checking the (J)32 Type correspondence.
* Mixed points: the CRT-gluing description is a correct and useful way to name the residual exponents; Filaseta–Finch–Kozek
  analogy flagged as from memory (not checked by me either).

## Defects
**D1 (MINOR, presentation/novelty; SIGN_FIELDS §1 Thm 1.3 and AGENT_REPORT headline).** Five of the nine offsets
(k = 9, 81, 129, 201, 249) have **no** member in Mordell's six classes mod 840 for s ≥ 2, so ES for them is an immediate
corollary of Mordell's classical mod-840 theorem (plus s = 0, 1 by hand); the certificates just re-encode that. Of the
other four, the hard-class members are for k = 153 *all* multiples of 13 (4² + 153 = 13², ord₁₃4 = 6) and for k = 225 the
s ≡ 3 (6) ones are multiples of 17 — divisor classes. The genuinely non-classical content is: k = 57 (s ≡ 9 mod 30, class
mod 2015), k = 177 (s ≡ 5 mod 6, class mod 39), k = 225 (s ≡ 0 mod 6 via mod 39, s ≡ 9, 21 mod 24 via mod 2019, 2716).
Repair: state in Thm 1.3 that for k ∈ {9, 81, 129, 201, 249} the result is Mordell's theorem, and headline the four
offsets with hard-class members.

**D2 (MINOR, label hygiene; SIGN_FIELDS Thm 1.3 statement).** "certificates checked by ec_cert.py" — ec_cert's T1 test
is a sanity check, not a proof step; the proof is identity + integrality + positivity + periodicity + coverage + small
cases. Also ec_cert uses m₀ = v₂(M) (= 2 for k = 225) where ⌈v₂(M)/2⌉ = 1 suffices — harmless (conservative). No repair
needed beyond optionally noting that the k = 225 class mod 2716 is an I1 class whose 2-part needs s ≥ 1.

**D3 (MINOR; SIGN_FIELDS §1.4 first bullet list).** k = 273 has a second integer square point 4⁴ + 273 = 23² (factor pair
(7, 39) of 273). Repair: "k = 273: 4² + 273 = 17², 4⁴ + 273 = 23²".

**D4 (MINOR; SIGN_FIELDS §1.4, k = 33 parenthesis and mixed-point bullet).** (a) "the screen leaves exactly s ≡ −2 (mod L)
at every L tested" — false at L = 60, 120 (extra survivor s ≡ 34 mod 60, a mixed point); state the tested L list, or say
"for every L divisible by 9 tested (180, 360, …)". (b) "ord_q(4) a 2·3-power" → "ord_q(4) ∈ {3^b, 2·3^b}".

**D5 (MAJOR — wrong statement inside a PROVED theorem; SIGN_FIELDS Thm 2.2(d), parenthetical "for u ≡ 3 (mod 4) the whole
c-fibre is forbidden and the ratio below is even smaller").** For ν = 4, n ≡ 1 (4), u ≡ 3 (4): 4 | n + u, Prop 2.1 does not
apply, and every odd-A word at level u is a 4-word via 4 | v (and has χ = −1). So for ν = 4 slot set = forbidden set also at
u ≡ 3 (4). Repair: restrict (d) explicitly to u ≡ 1 (mod 4), and replace the parenthetical by "for u ≡ 3 (mod 4),
4 | n + u, Prop 2.1 does not apply; there the v-slot makes every odd-A word a 4-word, and the whole c-fibre is both the
4-slot set and the forbidden set — so the coincidence for ν = 4 holds at every odd u (= DEDEKIND Thm 4.5). For other 4 | ν
at u ≡ 3 (4) the slot set is a proper subset (not analysed)." The headline conclusion (uniqueness of 4) survives and is
in fact strengthened.

**D6 (MINOR; Thm 2.2 preamble).** "every odd A at level u has σ_A ∈ Gal(Σ_{ν,u}/ℚ(√−u))" needs gcd(A, ν) = 1 (σ_A undefined
otherwise). Add the hypothesis; also note in (a) that for ν odd the conclusion is stronger (whole level empty, see §4).

**D7 (MINOR; SIGN_FIELDS §2 "The failures", memo z8_eight_failures_frobenius).** 131 ≡ 3 (mod 4): its 4-slot words have
(A/131) = +1, not −1; the sign-field "forbidden half" language of (d) is for n ≡ 1 (mod 4). Repair: "14 carry a 4-slot
(for n ≡ 3 (4) these are the words with (A/n) = +1, i.e. (−A/n) = −1)", and state the word-count convention (21 vs. the
reviewer's 22 words (t, u ≤ v) — say which word is excluded and why).

**D8 (MINOR; SIGN_FIELDS Prop 3.1 last sentence, memo z8_no_redei_abelian_levels).** Rephrase "Rédei symbols … do not
enter" as "do not enter the decision function" and note that the input (which r divide p + u in a family) is governed by
ring-class-field Frobenii; the reason this cannot force non-genus cleanness is the Assessment in the Consequence paragraph.

**D9 (MINOR; Thm 2.2 closing sentence "full T1 ⟺ 4 | ν … is, on the t-slots, …").** Add "for odd A coprime to ν"; the
⇒ direction of (J)46's *full* T1 (all five slots, even A) is not re-derived here — only the t-slot part.
