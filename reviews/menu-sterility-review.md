# R251 — hostile review #1 of O240 (MENU_STERILITY.md, memos z15_*)

Reviewer: R251 (side-agent/review-menu-sterility). Reviewed: merge of side-agent/menu-sterility at ccddde8b.
From-scratch scripts: `scripts/review_r251_proth3.py` (Theorems B/C: rules, ET classes, coverage, exact solutions),
`scripts/review_r251_brute.py` (rule-free ES search, small s). No z15_/z8/ec_cover code was imported or reused.

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem B (window-11 identity, s ≡ 0, 12 mod 40) | SOUND |
| Theorem C (ES for every 3·2^s + 1) | SOUND (minor presentation defects) |
| Theorem C vs (J)22 Cor 1.5 consistency | SOUND |
| Theorem A (witness reciprocity, unit locus, ⊇) | SOUND (passes a new 2-adic consistency test against Thm B) |
| Prop 4.1 (m ≡ 7 (8) dead at μ = 0) | SOUND-AFTER-REPAIRS (D8: positivity of d(ρ) unstated, but true) |
| Prop 4.3 (SG menu at μ = 0 finite) | SOUND (c = 3 enumeration reproduced) |
| Prop 3.1 | SOUND |
| Prop 5.1 | SOUND (elementary) |
| labels | essentially correct; minor overstatements D5, D6, D11 |

No FATAL, no MAJOR defect. **Headline (Theorem C: ES for every 3·2^s + 1) independently confirmed**: every rule
rebuilt by hand, coverage proved by hand mod 120, exact solutions s ≤ 2000, rule-free search s ≤ 60.

## Theorem B / Theorem C — independent verification

**(i) Theorem B.** Re-derived by hand from CAP_DOWN Lemma 1.1 at m = 11: K = (n + 11)/4 = 12X⁴ + 3 = 3f₊f₋
(f± = 2X² ± 2X + 1, Sophie Germain), 4/n − 1/K = 11/(nK), and 11/(nK) = 1/y + 1/z with y = n(K + d)/11,
z = nK(K + d)/(11d) for any d. With d = 9f₋: K + d = 3f₋(f₊ + 3) = 6f₋(X² + X + 2), y = 6n f₋(X² + X + 2)/11,
z = 2n f₊f₋(X² + X + 2)/11 — exactly the stated terms (sympy, script). Divisibility needed: only 11 | X² + X + 2
(n is prime to 11 on the class, d | K² so K(K + d)/d = K²/d + K ∈ ℤ[X]); X² + X + 2 ≡ 0 (11) ⟺ X ≡ 4, 6 (table of all
residues printed by the script). X = 2^{(s−4)/4}: 2 is a primitive root mod 11, 2⁹ ≡ 6, 2² ≡ 4, so s ≡ 0, 12 (mod 40). ✔
Note (not a defect): in the (a,b,c) = 3^a f₊^b f₋^c notation of Theorem C, Theorem B's d = 9f₋ is (2,0,1), while
the Theorem C table lists (0,2,1) at s ≡ 0, 12 — both fire there (script output); the table is consistent, just a
different choice.

**(ii) SG rules.** For all 27 vectors 0 ≤ a, b, c ≤ 2 I checked the identity and exact integer-valuedness of y, z on
every X mod 11 (polynomial P ∈ ℤ[X] over a constant L: L | P(r + 11j) for all j mod L). Firing residues X mod 11:
{2, 3, 4, 5, 6, 7, 8, 9}; dead: X ≡ 0 (impossible for X = 2^e), 1, 10. Via X = 2^{(s−4)/4}: dead s ≡ 4, 24 (mod 40)
exactly; every author-listed (a,b,c) fires at its residue. ✔ Positivity: f± have negative discriminant, K + d > 0. ✔

**(iii) ET/divisor classes**, each rebuilt by hand:
* n ≡ 0 (7): ES(7) = (2, 15, 210) scaled: (2n/7, 15n/7, 30n). n ≡ 0 (5): ES(5) = (2, 4, 20): (2n/5, 4n/5, 4n).
  n ≡ 0 (61): ES(61) = (16, 326, 2608·61)/… : (16n/61, 326n/61, 2608n) (identity checked).
* n ≡ 6 (7): 4/n = 7/(2(n+1)) + 1/(2n) + 7/(2n(n+1)) [numerator 7n + (n + 1) + 7 = 8(n + 1)].
* n ≡ 7 (15): x = (4n+2)/15, 4/n − 1/x = (n + 8)/(n(4n + 2)), minus 1/(4n) = 30/(4n(4n+2)) → z = 4n(2n+1)/15.
* n ≡ 13 (15): x = (4n+8)/15, remainder (n + 32)/(4n(n + 2)), minus 1/(4n) → z = 2n(n + 2)/15.
All six agree with the JSON certificate's coefficient lists; integrality on the class and non-negative coefficients
checked exactly. ✔

**(iv) Coverage.** ord₅2 = ord₁₅2 = 4, ord₇2 = 3, ord₆₁2 = 60, SG depends on s mod 40: true period lcm = **120**
(author: 360, a harmless multiple). Hand derivation: s ≡ 1 (3) → 7 | n; s ≡ 2 (3) → n ≡ 6 (7); s ≡ 3 (4) → 5 | n;
s ≡ 1, 2 (4) → n ≡ 7, 13 (15); s ≡ 0 (4) → SG unless s ≡ 4, 24 (40); the leftover s ≡ 4, 24 (40) ∧ s ≡ 0 (3) is
s ≡ 24, 84 (120), both ≡ 24 (60), and 3·2²⁴ + 1 ≡ 0 (mod 61). Script: no uncovered residue mod 120. ✔
(The memo's "s ≥ 10" restriction is a builder artefact; my checker verifies every s ≥ 1 directly.)

**(v) Exact solutions.** Script `review_r251_proth3.py 2000`: an exact Fraction-verified solution for every
1 ≤ s ≤ 2000 from the rebuilt rules; s = 0 (n = 4) is 1/2 + 1/3 + 1/6. Rule-free search `review_r251_brute.py 60`
finds an ES solution for every s ≤ 60 independently. ✔

**(vi) T1.** By hand: 3·2^s + 1 = m² ⟹ (m − 1)(m + 1) = 3·2^s with m − 1, m + 1 ∈ {2^a, 3·2^b} differing by 2 ⟹
m ∈ {5, 7} (plus n = 4 at s = 0): s ∈ {0, 3, 4}. Only s = 4 is ≡ 0 (mod 4) and it lies in the dead class s ≡ 4 (40),
handled by the divisor class 7 | 49. So no rule is asked to work at a square, and the dead residues are exactly the
neighbourhoods of X = ±1 (φ(±1) = 49), as claimed in §4.3 (whose attribution to Thm 3.3 is correct; φ has no real
root, X₀ = ±1 > ρ = −∞).

**(vii) Consistency with (J)22.** EXPONENT_COVERING Thm 1.4 + Cor 1.5 (re-read on main): ν(0) of 3·2^s + 1 is in
Sq^×, so no finite ET/divisor set covers {n_s : s ≡ 0 (mod L)} for any L. Since {s ≡ 0 (40)} contains s ≡ 0 (mod L)
for every 40 | L, the SG rule there cannot coincide (on its class) with any finite union of ET/divisor classes — and it
indeed is not polynomial in n: y has degree 8 in X with non-zero X³ coefficient (6n·f₋(X² + X + 2) contains odd powers
of X), while polynomials in n = 48X⁴ + 1 are polynomials in X⁴. The theorem is not a contradiction with Cor 1.5. ✔

**Verdict Theorem B: SOUND. Theorem C: SOUND.** (Proth primes in the family re-checked: s = 1, 2, 5, 6, 8, 12, 18,
30, 36, 41, 66, 189 for s < 200, as stated.) Defects D1–D3 below are MINOR.

**Literature / novelty (Theorem C).** Three web searches (Jina: "Erdős–Straus Proth numbers 3·2^n+1",
"Erdős–Straus n = k·2^m + 1 exponential family", "Erdős–Straus Sophie Germain Aurifeuillean") found no statement of ES
for 3·2^s + 1; standard sources (Mordell's 840-classes, ET 2011) do not contain it. Note that on s ≡ 0 (mod 12) the family
lies in Mordell's hard class n ≡ 529 = 23² (mod 840), so it is not covered by the classical congruence identities, and
the naive window m = 3 is dead for even s (all odd primes of 3Y² + 1 are ≡ 1 mod 3). Not exhaustive — the document's
"no claim of priority" is the right label.

## Theorem A (witness reciprocity) — SOUND (minor wording defects D4–D6)

Re-derived line by line:
* Witness: Lemma 1.1 gives (−4d/n) = −1; for n ≡ 1 (4) this is (d/n) = (−d/n). Lemma 1.3 gives (f/n) = −1 for n ≡ 1 (4).
  Both hold at every large u ∈ C with φ(u) ≡ 1 (8). ✔
* Choice of u: closure(C) = g + TẐ; CRT with u ≡ g (T) and u ≡ u* (ℓ^k), ℓ ∈ S, is consistent because u* ≡ g at every ℓ. ✔
  φ(u) ≡ φ(u*) (ℓ^k) ⇒ φ(u) prime to S and ≡ 1 (8). ✔
* v_q(φ(u)) = Σ_{𝔮|q} f_𝔮 v_𝔮(u − θ) for q ∉ S: φ(u) = lc·N_{A/ℚ}(u − θ), lc an S-unit, and the norm of a principal
  ideal of the maximal order — this holds for every q ∤ lc; the conductor condition in S is harmless but not needed. ✔
* (X/q)^{f} = (X/𝔮) for X ∈ 𝔽_q^× (exponent (q^f − 1)/2 = ((q − 1)/2)(1 + q + … + q^{f−1}), the second factor ≡ f mod 2). ✔
* D̃(u) ≡ D̃(θ) = α mod 𝔮 for 𝔮 | u − θ; tame symbol (α, π)_𝔮 = (α/𝔮)^{v_𝔮(π)} for 𝔮 odd, α a 𝔮-unit; Hilbert product
  formula in each component field; Π_{v∈S∪∞}(α, γ)_v = 1 because (α, γ)_v = 1 at odd v ∉ S (both units). ✔
* At v | ℓ ∈ S: γ(u − θ) = γ(u* − θ)·(u − θ)/(u* − θ) is a square (unit squares open; u* − θ invertible). At real v:
  γ > 0, u − θ_v > 0. Hence (D̃(u)/φ(u)) = (g/φ(u)) = +1 and (D(u)/φ(u)) = +1, contradiction. ✔
* Special cases: linear φ: A = ℚ, Ster = profinite unit squares (local squares everywhere ⇒ γ/q ∈ ℚ^{×2}) ✔;
  φ(u₀) = 1 integer unit points ✔; φ = m² − j, γ = 1 ⇒ Thm 3.4 (Z_K⁺: square + unit norm ⇔ unit square) ✔.

**Independent consistency test (new, `scripts/review_r251_thmA_2adic.py`, PARI via cypari).** Theorem A + Theorem B
make a falsifiable prediction: for φ = 48X⁴ + 1 the glued point X* (= 1/2 at odd ℓ, 0 at 2) lies in the closure of the
class X ≡ 6 (11) on which Theorem B's family is valid, so X* ∉ Ster(φ). A has no real places (φ > 0 on ℝ) and
φ(X*) = 1 at 2; with γ = (1/2 − θ)⁻¹ the only remaining condition is that θ/(θ − 1/2) ~ η(η − 1) (η = 2θ, 3η⁴ + 1 = 0)
be a square in A ⊗ ℚ₂ (any other admissible γ differs from this one by an element that is a local square at all odd
places, hence a global square by Chebotarev — so this is the full test). PARI: 3η⁴ + 1 is irreducible over ℚ₂ and
K(√(y(y − 3))) (y = 3η) has a single prime over 2 with e = 4, f = 2: **non-square, as Theorem A requires** (sanity
controls 17 = □, −1, 3 behave correctly). This is the first test of Theorem A against an actual identity; it passes.
(The memo/§4.2 tests use 3θ^e + 1, e = 3, 5, 7 — cyclotomic parametrisations; the SG case e = 4 was not shown; see D7.)

## Prop 4.1 (m ≡ 7 (8) dead at μ = 0) — SOUND-AFTER-REPAIRS (D8: unstated positivity step)
Re-derived: e | j, ρ = 2^{−j/e}; along s → 0 in Ẑ, U → ρ at odd q, n ≡ 4^i, K ≡ 4^{i−1} (mod m); d ≡ −K forces
(d/m) = (−1/m) = −1. Odd q | N₀ = 4^i + m satisfy (q/m) = (−m/q) = 1 ✔ (Jacobi reciprocity with m ≡ 3 (4); q ∤ m).
λ's odd primes divide K(ρ) by continuity ✔ (if q | K(U) on the class, U → ρ q-adically gives q | K(ρ)). **But the step
(d(ρ)/m) = (2/m)^{v₂(d(ρ))} silently assumes d(ρ) > 0**; if d(ρ) < 0 the conclusion flips to (2/m)^{v₂} = +1, allowing
every m ≡ 7 (8). My script `review_r251_prop41.py` confirms the sign is the whole content: for i = 1, 2, 3 and
m < 3000, the group ⟨2, odd q | N₀⟩ ⊂ (ℤ/m)^× never contains −4^{i−1} when m ≡ 7 (8), while −d(ρ) = K is trivially
reachable. The sign IS positive (repair D8): K(U) = (c2^jU^e + 1 + m)/4 has positive coefficients, so no atom has a
root on (0, ∞); each atom has constant sign there, and d > 0 at large U ⇒ d(ρ) > 0. One sentence fixes it.

## Prop 4.3 (SG menu at μ = 0 finite) — SOUND (D9 garbled sentence)
Derivation re-done: X → 1/2, f± → g±(t)/2, K ≡ 4^{i−1} (mod m(t) = 4ct⁴ − 1) ✔; irreducibility of t⁴ − 1/(4c) for
c non-square ✔ (Capelli: a or −4b⁴); N(τ) > 0 at τ = (4c)^{−1/4} ⇒ Res ≠ 0; Res = A·N + B·m with A, B ∈ ℤ[t] ⇒
m(t) | Res. From-scratch enumeration `review_r251_prop43.py 3` (27 vectors, all t up to the resultant bound): firings
exactly (t, a, x, y) = (1, 0, 2, 1), (1, 2, 0, 1) — matches the author. Scope caveat (D10): "SG menu" = cap-0 windows with
d a product of the polynomial atoms and primes of c with exponents ≤ 2; the finiteness is for that menu only.
c = 15, 63: EVIDENCE only, correctly labelled.

## Prop 3.1 — SOUND
O238 Lemma 1.0 is a genuine Type II (a, …, f) polynomial family in u (a = 1, d = 2(u² − u + 1), b = 32(u + 1),
c = (32u + 33)/151, e = 151, f = 4acd − 1; all four Σᴵᴵ relations checked symbolically, `review_r251_prop31.py`), hence
polynomial in v with u = v². Local points: no odd prime ℓ < 2000 fails (incl. ℓ = 3, 5, 7, 151); Weil count for ℓ ≥ 37
correct (two points at ∞ since 256 is a square; ≤ 6 with w = 0; ℓ − 1 − 4√ℓ − 6 > 0 for ℓ ≥ 37; bad primes only 2, 3, 5, 7).
2-adic: m even ⇒ m² + 105 ≡ 1 (8). The statement is correctly scoped (refutes the naive extension of Thm 2.2 only).

## Prop 5.1 — SOUND (trivial; labels fine)
Primes in a unit class C have counting function ≍ X/log X (Dirichlet/PNT in APs), thin sets O(X^{1−δ}); a finite ET menu
missing a sterile point misses a clopen neighbourhood. Correct and correctly called "elementary". The norm-form paragraph
is properly hedged (Assessment for d ≥ 3).

## Numbered defects (all MINOR unless stated)

**D1 (MINOR, Thm C proof (b)/(c), memo, report).** The overall period is 120 (lcm(40, ord₅2, ord₇2, ord₁₅2, ord₆₁2) =
lcm(40, 4, 3, 4, 60)), not 360; "coverage of all s mod 360 (s ≥ 10)" is correct but obscures a two-line hand proof.
*Repair:* add the hand coverage argument: s ≡ 1, 2 (3) → 7 | n, n ≡ 6 (7); s ≡ 1, 2, 3 (4) → n ≡ 7, 13 (15), 5 | n;
s ≡ 0 (4) → SG unless s ≡ 4, 24 (40); the rest is s ≡ 24, 84 (120) ⊂ s ≡ 24 (60) ⇒ 61 | n. Drop "s ≥ 10" (every s ≥ 1
is covered by these rules; s = 0 is 1/2 + 1/3 + 1/6).

**D2 (MINOR, §4 "Why it is not a contradiction").** "The class {s ≡ 0 (40)} is the n-congruence class n ≡ 4 (2⁴⁰ − 1),
n ≡ 1 (16)" — the family members are *contained in* that class (equality is false). *Repair:* "lies in".

**D3 (MINOR, Theorem C table vs Theorem B).** Theorem B's divisor d = 9f₋ is (a,b,c) = (2,0,1); the Theorem C table uses
(0,2,1) at s ≡ 0, 12. Both fire (verified), but say so, otherwise a reader checking Theorem B against the table is confused.

**D4 (MINOR, Thm A proof, zero-divisor case).** "h(u)/gcd(h(u), g^∞) > 1 for large u" is false in general (h(u) = u,
u = g^k ∈ C). Only one u is needed. *Repair:* "for some (indeed most) large u ∈ C".

**D5 (MINOR, Thm A special cases, last bullet; memo z15_witness_descent "T1: built in (squares are γ = 1/(u₀ − θ))").**
"Two variables … POINTWISE_BINARYFORM §4.1" is listed under "Special cases (all previously proved separately; Theorem A
unifies them)", but Theorem A is a one-parameter statement; and the memo's T1 sentence contradicts the R-O240 repair
(only φ(u₀) = 1 is a unit point). *Repair:* mark the two-variable bullet "analogy (Assessment)"; fix the memo sentence to
"integer points with φ(u₀) = 1; odd squares > 1 stay with Thm 3.3".

**D6 (MINOR, AGENT_REPORT/README).** "identifies one-parameter sterility with a Brauer/2-cover-descent pairing" overstates
a one-sided inclusion (Ster(φ) ⊆ sterile set). *Repair:* "shows the sterile set contains a 2-descent set".

**D7 (MINOR, §4.2 and memo z15_witness_descent "Cheap numerics").** The 2-adic test is run for 3θ^e + 1, e = 3, 5, 7
(cyclotomic parametrisations), and the memo concludes "indeed Theorem C covers it" — but Theorem C's dissolving family is
the Sophie-Germain one, φ = 48X⁴ + 1 (η = 2θ, 3η⁴ + 1 = 0, e = 4), which was not tested. *Repair:* add the e = 4 test;
reviewer's PARI computation (`scripts/review_r251_thmA_2adic.py`): η(η − 1) is NOT a square in ℚ₂(η) (single prime,
e = 4, f = 2 in the quadratic extension), exactly as Theorem A + Theorem B require; and note that by Chebotarev the
single-γ test is the complete test here (A has no real places).

**D8 (MINOR→should be fixed, Prop 4.1 proof).** The conclusion (d(ρ)/m) = (2/m)^{v₂(d(ρ))} needs d(ρ) > 0; with the
opposite sign the Proposition would be false (script `review_r251_prop41.py`: the sign carries the whole content).
*Repair:* insert "K(U) = (c2^jU^e + 1 + m)/4 has positive coefficients, so no atom vanishes on (0, ∞); hence each atom
has constant sign there and d(ρ) has the sign of d at large U, i.e. d(ρ) > 0."

**D9 (MINOR, Prop 4.3 proof; §4.3).** Garbled sentences: "For c = 3 the first case cannot occur for any c (R-O240
repair)" and "by NEAR_SQUARE Thm 3.3 (= Theorem A with not via Theorem A: φ(±1) = 49 is not a unit — R-O240 repair)".
*Repair:* "The first case never occurs (R-O240 repair): …" and "by NEAR_SQUARE Thm 3.3 (not Theorem A: φ(±1) = 49 is
not a unit — R-O240 repair)".

**D10 (MINOR, Prop 4.3 scope).** The finiteness concerns cap-0 SG windows m = 4ct⁴ − 1 with d = Π_{q|c} q^{a_q} f₊^x f₋^y,
exponents ≤ 2 (as enumerated); state this menu explicitly in the statement (the word "admissible" is undefined there).

**D11 (MINOR, label).** Theorem C is labelled "computer-assisted"; after D1 the proof is fully hand-checkable (6 ET
identities + 8 window identities mod 11 + a mod-120 case split). Keeping the label is harmless; optionally "PROVED
(hand-checkable; certificate re-verified)".

## Not checked / limits
* Mordell/Schinzel and Bruin–Stoll were not re-read (only used through EXPONENT_COVERING / as literature pointers).
* §4.1 (7·4^s + 9 stuck nodes) and §6 (function fields) not re-run (EVIDENCE / Assessment labels are appropriate).
