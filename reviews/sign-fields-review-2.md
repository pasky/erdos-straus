# R236 — hostile review #2 of O232 (SIGN_FIELDS.md, BRAINSTORM/z8_*.md, data/z8/)

Reviewer: R236 (round 1, no edits to author files). Merged `side-agent/sign-fields` at 25fa4b4a (README conflict resolved
as a union of both tables). From-scratch scripts: `scripts/review_r236_cert.py` (certificate checker, sympy only, no
ec_cert/z8 import), `scripts/review_r236_misc.py` (Lemma 1.1 offsets, mod-840 table, integer square points, T1 control,
independent ES search s ≤ 10), further `scripts/review_r236_*.py` below.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 1.3 (ES for all 4^s + k, nine k) | SOUND (independently re-certified); MINOR wording/novelty issues |
| Lemma 1.1 | SOUND (MINOR: s ∈ {0,1} handled only by the certificates) |
| Lemma 1.2 | SOUND statement, proof has a slip at ℓ = 0 (MINOR) |
| §1.4 OPEN list / square points / k = 105 screen / mixed points | SOUND-AFTER-REPAIRS (MINOR D5–D8); screen re-certified |
| Prop 2.1 | SOUND (MINOR: non-unit A*-class) |
| Thm 2.2 (a)–(c) | SOUND (reformulation of classical T1, D11) |
| Thm 2.2 (d) + "uniqueness of 4" | SOUND-AFTER-REPAIRS — **MAJOR D9**: u ≡ 3 (4) parenthetical false; uniqueness only for coprime slots at u ≡ 1 (4) |
| 8/131, 8/241, 11/37 | data SOUND (counts off by one, D10); interpretation overreaches (D12: 8/113 solvable without 8-slot) |
| §3 Prop 3.1 + Assessment | SOUND (MINOR D13, D14) |
| §4 Assessment | SOUND |
| novelty | modest; nothing found in literature on 4^s + k |

No FATAL defects. MAJOR: D9; D12 (interpretive). Remaining thirteen MINOR.

## 1. Theorem 1.3 — SOUND

**Independent certificate check** (`review_r236_cert.py data/z8/*.json 300`). The JSON field semantics (n = k·b^s + c with
json-k = 1 = c₀, json-c = the offset; x, y, z coefficient lists in n, low→high) were re-derived from the data (e.g.
k = 9, D₅: x, y, z = 2n/5, 4n/5, 4n; 5/2n + 5/4n + 1/4n = 4/n). For every class of all nine files I checked:
1. 4xyz − n(xy + yz + zx) ≡ 0 in ℚ[n] (sympy, exact).
2. Integrality by a *different* method from ec_cert's forward differences: with D = lcm of coefficient denominators,
   D·p ∈ ℤ[n], so p(n) ∈ ℤ is a condition on n mod lcm(M, D); all residues ≡ r (mod M) enumerated.
3. Positivity: leading coefficient > 0 and largest real root < 1 for every polynomial (n_pos = 1 everywhere — all
   coefficients turn out non-negative; positivity is automatic).
4. Periodicity, re-derived: write M = 2^a M′, M′ odd. For 2s ≥ a, 4^s ≡ 0 (mod 2^a), and 4^s mod M′ has exact period
   ord_{M′}(4); so n_s mod M is purely periodic in s ≥ ⌈a/2⌉ with period ord_{M′}(4). Checked ord_{M′}(4) | L for every
   class (the only even modulus is 2716 = 4·679 in k = 225, needing s ≥ 1; ord_{97}(4) = 24 = L).
5. Coverage of every s ∈ [s₀, s₀ + L) (s₀ = 0, or 1 for k = 225).
6. For s ≤ 300 the class formula evaluated at the actual integer n_s, checked as positive integers satisfying the identity
   (in particular s = 0, n = 1 + k even, is covered by a class in every file — no brute-force exceptions needed).
Result: all nine COVERED. The author's own `ec_cert.py` also passes on all nine (to m = 600; it uses a more conservative
m₀ = 2 for k = 225, harmless).

**Independent brute force** (`review_r236_misc.py` (e)): an independent ES search (x near n/4, then (ay − b)(az − b) = b²
over divisors) finds a solution for every s ≤ 10 for all 13 offsets k ≡ 9 (24), k ≤ 300 (including the four OPEN ones).

**T1 control.** All integer square points 4^ℓ + k = □ (finite: (t − 2^ℓ)(t + 2^ℓ) = k) for the nine k:
k = 9: 25 (ℓ = 2); 57: 121 (3); 129: 4225 = 65² (6); 153: 169 (2); 201: 1225 = 35² (5); 225: 289 (3); 81, 177, 249: none.
Each lies in a **D** (divisor) class of its certificate (D₅, D₁₁, D₅, D₁₃, D₅, D₁₇ respectively), and my check 6 evaluated
the actual solution there. Moreover every non-D class r (mod M) of every certificate is a *non-square* residue class mod M
(exhaustive over s mod M; `misc` (d)), consistent with T1 / Yamamoto — no family "proves" anything impossible.

**Mordell-hard members** re-derived from n_s mod 840 (period 6 for s ≥ 2): 57 (s ≡ 3 (6), 121), 153 (s ≡ 2, 169), 177 (s ≡ 5,
361), 225 (s ≡ 0, 3, i.e. 0 mod 3: 289, 121); 9, 81, 129, 201, 249 never hard. Matches the text.

Defects:
- **D1 (MINOR, novelty/wording, Thm 1.3 + abstract use).** Five of the nine k (9, 81, 129, 201, 249) are immediate from
  Mordell's mod-840 theorem (every n_s with s ≥ 2 avoids the six classes; certificate = D₅ ∪ II2 mod 15), and k = 153 is
  Mordell + the divisor class 13 | n_s (s ≡ 2 mod 6). Only k = 57, 177, 225 use a genuinely non-Mordell ET class
  (moduli 11/31/2015; 39; 39/2019/2716). Repair: say so explicitly in Thm 1.3 ("k = 9, 81, 129, 201, 249: Mordell;
  153: Mordell + D₁₃; 57, 177, 225: genuine coverings"), so the headline is not read as nine new results.
- **D2 (MINOR).** "These are near-square infinite families … on which polynomial families in m provably cannot cover"
  is true of the full family m² + k, not of the subfamily m = 2^s, and the exponential subfamily has only O(log X)
  members below X; the sentence should not suggest the certificate defeats the Z_k^□ obstruction — it sidesteps it
  (as (J)22 does). Repair: one clause "(the exponential subfamily is thin; the covering is of Sierpiński type, (J)22)".
- **D3 (MINOR, Lemma 1.2 proof, ℓ = 0).** "the odd components are the odd integer N = 4^ℓ + k": for ℓ = 0, N = 1 + k is
  even. The statement is still true for all odd k ≥ 3, but for k = 4^j − 1 (k = 3, 15, 63, …) ν(0) *is* a unit square at
  every odd q and is excluded only by the 2-adic condition x₂ = k ≡ 1 (mod 8) in Sq^× (EXPONENT_COVERING §1). Repair:
  "ℓ = 0: 1 + k a unit at all odd q forces 1 + k = 2^j; square at all odd q forces j even; then k ≡ 3, 7 (mod 8),
  violating x₂ ≡ 1 (8)" (or restrict the lemma to k ≡ 1 mod 8, where 1 + k ≡ 2 mod 8 is never a power of 4).
- **D4 (MINOR, Lemma 1.1).** The lemma is stated for s ≥ 2; members s = 0, 1 are covered only by the certificates (they
  are, check 6). One clause suffices.

## 2. §1.4 OPEN offsets, k = 105, mixed points — SOUND-AFTER-REPAIRS (EVIDENCE parts correctly labelled)

Re-derived (`review_r236_misc.py` (b),(c); `review_r236_screen.py`, own screen: primes q < 3·10⁶ with 4^L ≡ 1 (q), residue
s killed if 4^s + k ≡ 0 or a non-residue mod q; validity: ν(μ)_q mod q depends only on μ mod ord_q(4) | L):
* Non-trivial offsets ≤ 300: exactly 13, k ≡ 9 (24) ✓; 9 certified + {33, 105, 273, 297} ✓ (the OPEN status itself is
  search EVIDENCE; I did not re-run the class search).
* k = 105: n_s mod 840 for s ≥ 2 runs through all six Mordell classes {1, 121, 169, 289, 361, 529} ✓; n_s ≡ 4^s (mod 105) ✓.
* Screen k = 105, L = 360: 28 admissible primes, **no residue survives** ⇒ Λ₁₀₅ ∩ Sq^× = ∅ ✓ (2-component 105 ≡ 1 (8)
  is a unit square, so only odd q matter — correct).
* Screen k = 33, L = 360: exactly s ≡ 358 ≡ −2 survives ✓; at L = 3960 (11 | L) nothing survives ✓ (so the square half
  (EH) also holds for k = 33 — the text could say so).
* Mixed point: 124 mod 360 and 844 mod 2520 are the CRT of (4 at 2, 5, 7; −2 at 3) ✓. q = 181: ord 90 = 2·3²·5,
  μ* ≡ 34 (90), n ≡ 85, non-residue ✓. q = 919: ord 153 = 3²·17, μ* ≡ 106 (153), n ≡ 551, non-residue ✓ (necessary for the
  claimed II2 class; the specific family (2, 23, 919) not re-checked). "No ET class of modulus ≤ 2·10⁶ hits it" and the
  adaptive-lifting measures: not re-run (EVIDENCE, labelled as such).

Defects:
- **D5 (MINOR, factual omission, §1.4 first bullet list).** k = 273 has a second integer square point 4⁴ + 273 = 529 = 23²
  (besides 4² + 273 = 17²). Repair: add it.
- **D6 (MINOR, overreading).** "Same pattern as (J)22 §4.2: every OPEN k has an integer square point" is not
  discriminating here: 6 of the 9 *certified* k also have one (9: 25; 57: 121; 129: 65²; 153: 169; 201: 35²; 225: 289).
  Only 81, 177, 249 have none. Repair: state the full table, or drop the "pattern" sentence (in the memo z8_exp_near_square_cover
  too).
- **D7 (MINOR, wording).** "at q with ord_q(4) a 2·3-power, n ≡ 4⁻² + 105": true only for ord = 3^b or 2·3^b (μ* ≡ 4 ≡ −2
  needs 2^a | 6); for ord = 4·3^b, 8·3^b the value is generic. Repair: "ord_q(4) ∈ {3^b, 2·3^b}".
- **D8 (MINOR).** "every member [of 4^s + 105] lies in one of Mordell's six hard classes" — for s ≥ 2 (s = 0, 1 give 106,
  109). Add "(s ≥ 2)".

## 3. §2 numerator sign fields — Prop 2.1 SOUND; Thm 2.2 (a)–(c) SOUND; (d) SOUND-AFTER-REPAIRS (one false parenthetical)

**Re-derivations.** Write A·A* = t(tuv − u − v) + 1 = tn + 1, Av = n + u, A*u = n + v.
* Slot decompositions (all five) re-derived: e.g. ν | u = νw: tn + A* + 1 = AA* + A* = A*tu, so
  1/(wA*) + 1/(tnw) + 1/(tnwA*) = A*tu/(tnwA*) = ν/n ✓; ν | A = νw: nA* + n + v = v(nt + 1) = vAA* ✓; ν | t = νw:
  t/n = (n + u + v)/(nuv) = 1/(uv) + 1/(nv) + 1/(nu) ✓ (this is the "(J)32" slot — the text should just display it).
  `review_r236_slots.py` checks all five in exact rationals for every word of all primes < 600 and odd squares < 40².
* Prop 2.1: ν | v ⟹ ν | n + u ✓; ν | t ⟺ A ≡ −1 (ν) ✓; ν | A* ⟺ uA(tv − 1) = (A + 1)(n + u) − uA ≡ 0 ⟺ An ≡ −(n + u)
  (ν) ✓; t-slot and A*-slot classes coincide only if ν | u ✓. Numerically: 9 502 (word, ν, side) coprime instances,
  ν ∈ {3, 4, 5, 7, 8, 12}, 0 misclassifications. Note: when gcd(ν, n + u) > 1 the class −(n + u)/n is not a unit and
  C_ν reduces to {−1}; the definition of C_ν should say "(the second class only if gcd(ν, n + u) = 1)". MINOR.
* Thm 2.2(a)–(c): odd r | m² + u, gcd(m, u) = 1 ⇒ r ∤ u and (−u/r) = 1 ✓; σ_A fixes √−u; c moves it ✓. (b) conductor of
  ℚ(√−u) divides 4u ✓, u = 1 forces i ∈ ℚ(ζ_ν) ⟺ 4 | ν ✓. (c) Σ_{ν,u} = ℚ(ζ_{νu}) · ℚ(√−u) linearly disjoint, Chebotarev
  gives r ≡ −1 (νu) split in ℚ(√−u); then t = (r + 1)/u ≡ 0 (ν), Av − u = m² ✓. Numerics: 0 violations of (a) (odd A,
  coprime) at odd squares 3² … 59²; words with a ν-slot at these squares: ν = 4, 8, 12: 0; ν = 3: 411, 5: 273, 7: 140 ✓.
* Thm 2.2(d) for u ≡ 1 (mod 4), 4 | ν: Gal(ℚ(ζ_{νu})/ℚ) = (ℤ/ν)^× × (ℤ/u)^×; on the c-fibre b = −1 the character of
  ℚ(√−u) (u = u′s², u′ ≡ 1 (4)) is χ_{−4}(a)·(−1/u′) = χ_{−4}(a): half/half ✓; A*-class ≡ −(1 + u) ≡ 2 (4) non-unit ✓;
  coprime slot = {a ≡ −1}, size 1/φ(ν); 1/φ(ν) = 1/2 with 4 | ν ⟺ ν = 4 ✓.
* 8/131, 8/241, 11/37 (own word enumerator, u ≤ v): every 4-slot value is ≡ 4 (mod 8) at 131 and 241 ✓; no 8-slot, no
  11-slot at 37 ✓; own exhaustive search (x ≤ 3n/ν) confirms 8/131, 8/241, 11/37 have no 3-term solution ✓.

Defects:
- **D9 (MAJOR, Thm 2.2(d) parenthetical and the following bold sentence).** "for u ≡ 3 (mod 4) the whole c-fibre is
  forbidden and the ratio below is even smaller" is false for ν = 4, and the bold claim "for every other T1-numerator
  (8, 12, 16, …) it is a proper Chebotarev subset of the forbidden half" is false at some levels. For n ≡ 1 (4) and
  u ≡ 3 (4), 4 | n + u, so Prop 2.1's hypothesis ν ∤ n + u fails for ν = 4: every odd A gives 4 | v = (n + u)/A, i.e.
  **every** c-fibre element is a 4-word (v-slot) — word set = forbidden set = whole fibre, the coincidence holds. The same
  happens for ν = 8 (resp. 12, …) at every level u with ν | n + u (e.g. n ≡ 1 (8), u ≡ 7 (8): 8 | v for every odd A;
  checked for all words of primes p ≡ 1 (8) below 400). So "ν = 4 is unique" is a statement about the *coprime*
  slot set at levels u ≡ 1 (4) only; with the v/u-slots (non-coprime) numerators 8, 12, … also realise the full
  forbidden set on the levels u ≡ −n (mod ν). Repair: delete the parenthetical; replace by "for u ≡ 3 (4), 4 | n + u and
  the v-slot makes every odd A a 4-word (the whole c-fibre, = the forbidden set); for general 4 | ν the same holds at
  levels ν | n + u"; restrict the bold sentence to "levels u ≡ 1 (4) with ν ∤ n + u".
- **D10 (MINOR, counting bug in `scripts/z8_numerators.py`).** `words()` loops t ≤ n + 1 and misses the word
  (n + 2, 1, 1) (A = A* = n + 1). Hence "21 words of 131 / 14 with a 4-slot" should be 22 / 15 (the missed word has
  A = 132 ≡ 4 (8), so the 8/131 conclusion is unaffected), "9 words of 37" should be 10, and ν-slot counts at squares for
  odd ν (e.g. 3 | m² + 2) are slightly undercounted. Conclusions unaffected. Repair: range(1, n + 3).
- **D11 (MINOR, novelty).** (a)–(c) are the classical quadratic-reciprocity T1 argument (Yamamoto/Schinzel-type: ν/n with
  4 | ν has no polynomial-family solution on square classes) restated as a containment ℚ(√−u) ⊂ ℚ(ζ_{νu}); label is
  correct (PROVED, elementary) but it is a reformulation, not new information — say so next to "(J)46 SHARP 2".
- **D12 (MINOR→MAJOR-for-interpretation, 8/131 reading).** "all forbidden-half Frobenii land in the complementary
  ℚ(ζ_{8u})-class" explains the absence of *8-slots*. But "no word of p has an 8-slot" is **not** equivalent to "8/p
  unsolvable": own check over primes p < 700 (`review_r236_slots.words/es3`) finds 8/p solvable with no 8-slot at
  p = 113, 257, 353, 593 (e.g. 8/113 = 1/18 + 1/66 + 1/11187, 11187 = 99·113); for ν = 5 the equivalence held (p < 700).
  So the failure of 8/131, 8/241 is the absence of 8-slots **plus** the absence of the other (split-slot) solutions,
  and the sign-field picture accounts only for the first part. Repair: state "8-slot ⟹ 8/p solvable, not conversely
  (8/113)" and present the 8/131 data as "consistent with", not "explains". (Unsolvability of 8/131, 8/241, 11/37 itself
  re-checked independently.)

## 4. §3 non-genus layer — Prop 3.1 SOUND (trivial); Consequence SOUND as Assessment, with a sharper reason available

Re-derivation: an odd A at level u satisfies A ≡ −1 (u) ⇒ gcd(A, u) = 1, so A = ∏ r^{a_r} over odd r ∤ u, r | p + u,
0 ≤ a_r ≤ v_r; t = (A + 1)/u ≥ 1 and v = (p + u)/A ≥ 1 automatically. χ(w) = (A/p) = (p/A) = (−u/A) (p ≡ 1 (4)), the
ℚ(√−u)-character at A; with A ≡ −1 (u) this is "σ_A = c on Σ_u ⊂ ℚ(ζ_{4u})", a function of A mod 4u ✓.
- **D13 (MINOR, Prop 3.1 scope).** The statement is about words with *any* v; if "level u carries a word" is read with
  the census convention u ≤ v (NEAR_SQUARE_EXIST §1), the size condition A ≤ (p + u)/u enters and the event is no longer
  a function of (σ_r, v_r) alone. Repair: "(words with this u, v arbitrary; the mirror word lives at level v)".
- **D14 (MINOR, Assessment could be made a lemma).** The sentence "the only constraints … that hold for all m in a
  congruence class are (i), (ii)" is heuristic (Schinzel-H-type independence). The natural non-abelian candidate — the
  class-group relation ∏[𝔯]^{a} = [(m + √−K)] = 1 in Cl(F) for the prime ideals over the r | m² + K — projects to
  Gal(Σ_u/ℚ) only through H_F ∩ ℚ^{ab} = the genus field of F (Σ_u is abelian over ℚ). That is the precise reason Rédei /
  4-rank data cannot produce a *forced* constraint on the σ_r beyond genus, and is provable; suggest stating it, and keep
  "only constraints" as Assessment.

## 5. §4 Chebotarev-in-family — SOUND (Assessment, correctly labelled)

The reduction for a prime A = r re-derived: u ≡ −p (r), 1 ≤ u ≤ r + 1, u | r + 1; χ = −1 ⟺ (−u/r) = −1. Since
−u ≡ p (mod r), the condition simplifies to **(p/r) = −1 and (−p mod r) | r + 1** — cleaner than the stated form
(equivalent: −d ≡ p). MINOR suggestion only. (F1)–(F4) are reasonable reductions to B1/B2/B3/B6; no claim exceeds
Assessment.

## 6. Novelty / literature

Jina web searches ("Erdős–Straus … n = 4^k + c", "… powers of 2 special forms") found nothing on ES for 4^s + k; the method
is EXPONENT_COVERING (J)22 with base 4 and offset k (the text says so). Elsholtz–Tao classes and Mordell 1967 are the
only external inputs; Bertók–Hajdu and Filaseta–Finch–Kozek are analogies (FFK flagged "from memory" — not accessible
here either, not checked). Novelty: the certified families are new to my search but modest (D1); §2 is a Galois
reformulation of T1 (D11) with one genuinely informative point (the 1/φ(ν) vs 1/2 count at u ≡ 1 (4)); §3–§4 negative
Assessments.

## 7. Agent report (AGENT_REPORT_O232)

- **D15 (MINOR).** SHARP 1 and the "Caveats" bullet repeat the false u ≡ 3 (4) statement (D9) and "for 8, 12, … it is a
  proper Chebotarev subset" without the level restriction. Repair as D9.
- Report claims "independent brute force for s ≤ 8"; I extended this to s ≤ 10 for all 13 offsets (pass).
