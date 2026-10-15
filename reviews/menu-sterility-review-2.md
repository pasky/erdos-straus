# R252 — hostile review #2 of O240 (MENU_STERILITY.md, memos z15_*)

**Repairs applied (round 2, by R252; merged side-agent/review-menu-sterility (R251) and side-agent/menu-sterility (no new author
commits)).** MENU_STERILITY.md: R252 D1–D5, D7–D9 and R251 D1–D5, D7–D11 (Thm A zero-divisor step; two-variable bullet → Assessment;
Thm B ↔ table (2,0,1)/(0,2,1); "lie in"; Thm C hand coverage, period 120, no s ≥ 10, label "hand-checkable"; novelty search note;
Prop 4.1 positivity of d(ρ); Prop 4.3 restated for the restricted menu λ | c^∞ with a Scope paragraph (general λ: Assessment +
EVIDENCE); §4.1/§4.2/§7 adjusted; SG e = 4 2-adic test cited in §4.2; §4.3 garble + scope). Memos z15_window_jacobi_mu0,
z15_witness_descent, z15_proth_sophie_germain; BRAINSTORM/README rows; AGENT_REPORT_O240 (R251 D6 "contains", Prop 4.3 scope,
Prop 4.1 positivity, period 120, novelty). All marked "(R252 …, applied by R252)" / "(R251 Dk, applied by R252)".
Reconciliation with R251 on Prop 4.3: R251's D10 (MINOR, "state the menu") and my D7 (MAJOR) describe the same scope issue; with
the statement now restricted to λ supported on primes of c, Prop 4.3 is SOUND as stated (R251's verdict), and the general-λ
claim is downgraded to Assessment + EVIDENCE (my D7). No disagreement remains.

Reviewer: R252 (round 1, no edits to the author's files). Branch reviewed: side-agent/menu-sterility (merged at bf14ed4c).
From-scratch scripts: `scripts/review_r252_*.py` (no z15_/z8/ec_cover imports).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem B (window-11 SG identity, s ≡ 0, 12 mod 40) | SOUND |
| **Theorem C (ES for every 3·2^s + 1)** | **SOUND** (minor presentation defects only) |
| (vii) consistency with (J)22 Cor 1.5 | SOUND |
| Theorem A (witness reciprocity, unit locus) | SOUND (MINOR wording D5, D6) |
| Prop 4.1 (m ≡ 7 (8) windows dead at μ = 0) | SOUND-AFTER-REPAIRS (D4: positivity of d(ρ) is essential and unstated) |
| Prop 4.3 (SG menu at μ = 0 finite) | GAP (D7, MAJOR: proved only for λ supported on primes of c) |
| Prop 3.1 (Thm 2.2 fails for m = 16v³) | SOUND |
| Prop 5.1 (thin menus vs positive density) | SOUND |
| §4.1 7·4^s + 9 μ = 0 covered by SG(19) | SOUND (re-checked from scratch) |
| §4.3 T1 explains dead residues | SOUND for the mod-33 window menu (D9 scope) |
| Labels | correct except Prop 4.3 (D7) |

## 1. Theorem B / Theorem C (HEADLINE) — independent re-derivation

Script: `scripts/review_r252_proth3.py 2000` (sympy; ~1 min). Output (abridged):
```
Thm B identity: OK
window-11 SG rules (a,b,c) -> X residues mod 33: (0,0,2):[2,3,13,14,24,25] (0,1,2):[5,7,16,18,27,29]
  (0,2,0):[8,9,19,20,30,31] (0,2,1):[4,6,15,17,26,28] + 8 rules with a ≥ 1 (denominator 33)
s mod 40:  4 -> X≡1: NONE ; 24 -> X≡32≡−1: NONE ; all other s ≡ 0 (4) have ≥ 2 rules
author's (a,b,c) table: each valid on its class
ET identities: OK ; period: 120 ; uncovered residues mod 120: [] ; exact ES solutions s ≤ 2000: failures []
```

(i) **Identity and integrality (Thm B).** Re-derived by hand: with K = (n + 11)/4 = 3f₊f₋ (f± = 2X² ± 2X + 1; 4X⁴ + 1 = f₊f₋),
4/n − 1/K = 11/(nK), and for any d: 11/(nK) = 1/y + 1/z with y = n(K + d)/11, z = nK(K + d)/(11d). For d = 9f₋:
K + d = 3f₋(f₊ + 3) = 6f₋(X² + X + 2), so y = 6nf₋(X² + X + 2)/11, z = nf₊·6f₋(X²+X+2)/33 = 2n(4X⁴+1)(X²+X+2)/11 —
exactly the stated denominators. Needed divisibility: only 11 | X² + X + 2 (all other factors are integer polynomials);
X² + X + 2 ≡ 0 (11) ⟺ (2X + 1)² ≡ −7 ≡ 4 ⟺ X ≡ 4, 6 (mod 11). ✓. Note d = 9f₋ is the (a,b,c) = (2,0,1) rule; the table in
Thm C(a) uses (0,2,1) for the same classes — both are valid (my enumeration finds both), so no inconsistency, but the text
should say which d Theorem B uses (MINOR D1).
X = 2^{(s−4)/4}: ord₁₁(2) = 10, 2⁹ ≡ 6, 2² ≡ 4 ⟹ s ≡ 0, 12 (mod 40) ✓.

(ii) **Other window-11 rules.** All 64 vectors (a,b,c) ∈ {0..3}³ with z a polynomial were enumerated; integrality is a condition
on X mod 33 (denominators divide 33; ord₃₃(2) = 10, so it depends on s mod 40 only). Exactly the author's eight residues
{0, 8, 12, 16, 20, 28, 32, 36} mod 40 are covered, and the author's table (a,b,c) per residue is valid on each.
Residues 4, 24 (X ≡ ±1 mod 11) have NO rule with exponents ≤ 3 — consistent with §4.3 (T1 at X = ±1).
Positivity: K, d, f± > 0 for real X, so x, y, z > 0 for every integer X ≥ 1 ✓. s ≡ 0 (40) needs s ≥ 40 (X = 1/2 at s = 0); the
text's "s ≥ 4" plus s ≡ 0 (40) already implies this.

(iii) **ET/divisor classes**, rebuilt by hand (not read from the certificate) and checked symbolically:
n ≡ 0 (7): (2n/7, 15n/7, 30n); n ≡ 6 (7): (2(n+1)/7, 2n, 2n(n+1)/7); n ≡ 0 (5): (2n/5, 4n/5, 4n);
n ≡ 7 (15): ((4n+2)/15, 4n, 4n(2n+1)/15); n ≡ 13 (15): ((4n+8)/15, 4n, 2n(n+2)/15); n ≡ 0 (61): (16n/61, 326n/61, 2608n).
These match the certificate's six classes exactly. (They are ET Prop 1.9-type / divisor identities; correctness here needs only
the identity + integrality, which I checked; no appeal to ET is necessary.)

(iv) **Coverage and period.** By hand: mod 7, s ≡ 1, 2 (3) give n ≡ 0, 6; mod 15 (resp. 5), s ≡ 1, 2, 3 (4) give n ≡ 7, 13 (mod 15),
0 (mod 5). Left: s ≡ 0 (12); intersected with the SG-dead residues s ≡ 4, 24 (40) this is s ≡ 24, 84 (mod 120), both ≡ 24 (mod 60),
and 3·2^24 + 1 ≡ 0 (mod 61) with ord₆₁(2) = 60. So the true period is lcm(40, 3, 4, 60) = **120** (the author's L₀ = 360 is a
harmless multiple); the computer confirms 0 uncovered residues mod 120. Every s ≥ 1 is covered by a rule valid at that s (no
"s ≥ 10" threshold is needed; MINOR D2), and s = 0 (n = 4) is 1/2 + 1/3 + 1/6.

(v) **Exact solutions.** For every s ≤ 2000 my checker produces (x, y, z) from the rules above and verifies 4/n = 1/x + 1/y + 1/z in
exact rationals with x, y, z positive integers: 0 failures. Independent brute force for s ≤ 8 also finds solutions (sanity only).
I did not use the author's certificate file except to compare the six classes.

(vi) **T1.** 3·2^s + 1 = y²: for s ≥ 2, ((y−1)/2)((y+1)/2) = 3·2^{s−2} with coprime consecutive factors ⟹ {3, 2^{s−2}} consecutive
⟹ s = 3, 4; plus s = 0. So squares are exactly s = 0, 3, 4 (4, 25, 49) as claimed. s = 4 (X = 1) is in the SG-dead class 4 (40) and is
covered by the divisor class n ≡ 0 (7); s = 3 is not ≡ 0 (4); s = 0 has X ∉ ℤ. So no rule fires at a square. ✓ (The general
statement "48X⁴ + 1 is a square only for X = 1" is only numerically checked by the author — fine as stated, it is not used.)

(vii) **Not an ET/divisor class.** y = n(K + f₊²f₋)/11 (the s ≡ 0 (40) rule): since f₊(−X) = f₋(X), y(−X) ≠ y(X), so y is not a
polynomial in X⁴, hence not a polynomial in n = 48X⁴ + 1 (the same holds for every rule with b ≠ c, i.e. all eight used). The
d = 9f₋ form of Theorem B likewise. So the dissolving class is genuinely outside the ET/divisor menu, and Cor 1.5 (no finite
ET/divisor covering of {s ≡ 0 (L)}) is not contradicted: x = K is polynomial in n, but y, z are polynomial only in
X = ((n − 1)/48)^{1/4}. I re-read EXPONENT_COVERING Thm 1.4/Cor 1.5 on main: the hypothesis is exactly "ET and divisor classes"
(identities polynomial in n on congruence classes of n), so the logic "proved uncoverable by M₀, yet ES holds" is correct.
Small wording point: "the class {s ≡ 0 (40)} is the n-congruence class n ≡ 4 (mod 2⁴⁰ − 1), n ≡ 1 (mod 16)" should read "is the
intersection of the family with" that class (true: ord of 2 modulo (2⁴⁰ − 1)/3 is 40) (MINOR D3).

**Verdict Theorem C: SOUND.** The proof is complete and elementary once the rule table is fixed; computer assistance is only
needed for the finite residue bookkeeping, which is small enough to be done by hand (done above). Label "PROVED (computer-
assisted)" is correct; it could even be "PROVED" with the by-hand coverage argument of (iv) inserted.

## 2. Theorem A (witness reciprocity) — SOUND (minor wording repair)

Re-derived line by line.
* Witness. Lemma 1.1 gives (−4d/n) = −1 = (−d/n) for odd n; Lemma 1.3 needs n ≡ 1 (4). Ster(φ) imposes φ(u*) ≡ 1 (8) so both
  apply at the approximating u. ✓ (The Jacobi symbol with negative top D = −d is fine.)
* Valuations: φ(u) = lc·N_{A/ℚ}(u − θ), so v_q(φ(u)) = Σ_{𝔮|q} f_𝔮 v_𝔮(u − θ) for q ∤ lc — this holds for the places of the étale
  algebra (maximal order) regardless of whether ℤ[θ] is an order; the "conductor" clause added in the R-O240 repair is harmless
  but unnecessary. (X/𝔮) = (X/q)^{f_𝔮} for X ∈ 𝔽_q^× ✓. D̃(u) ≡ D̃(θ) = α (mod 𝔮) when 𝔮 | u − θ, θ 𝔮-integral for 𝔮 ∤ lc ✓.
* Tame symbol at odd 𝔮 with α a unit: (α, π)_𝔮 = (α/𝔮)^{v_𝔮(π)} ✓; places with α or γ non-units are put in S ✓.
* Reciprocity: Π_v (α, u−θ)_v = 1 per component field; (α, γ)_v = 1 off S ✓; at v | ℓ ∈ S, γ(u − θ) = γ(u* − θ)·(u−θ)/(u*−θ) is a
  square (u* − θ ∈ (A⊗ℚ_ℓ)^× because φ(u*) ∈ ℤ_ℓ^×; squares open) ✓; real places: γ ≫ 0 and u − θ > 0 (u > all real roots) ✓;
  complex places trivial ✓. The g-part identically ✓. Need φ(u) > 0 for the Jacobi symbol — u large, lc > 0 ✓.
* Choice of u: u ∈ C with u ≡ u* to high ℓ-power for ℓ ∈ S is compatible with C because u* ∈ closure(C) ✓.
* Zero-divisor step: the sentence "h(u)/gcd(h(u), g^∞) > 1 for large u" is FALSE as stated (h(u) = u, g = 2, u = 2^k), but the needed
  version holds: take u ∈ C near u* (with S₀ ⊇ primes of 2g·lc chosen first); then φ(u) is prime to g, h(u) | φ(u) (Gauss), |h(u)| > 1,
  so a prime outside g divides gcd(D̃(u), n) and (D/n) = 0. MINOR D5.
* Special cases: (deg 1) I checked that with A = ℚ the condition "γ·φ(u*)/q ∈ ℚ_ℓ^{×2} ∀ℓ, γ > 0, φ(u*) a unit" forces q/γ to be a
  rational square, hence φ(u*) ∈ Sq^× — exactly EXPONENT_COVERING's set ✓. (deg 2, γ = 1) = NEAR_SQUARE Thm 3.4's Z_K⁺ ✓ (same proof,
  re-read on main). Integer point with φ(u₀) = 1 ✓; squares > 1 correctly excluded after the self-repair.
* Stale text (MINOR D6): memo z15_witness_descent "Barrier screen" still says "T1: built in (squares are γ = 1/(u₀ − θ))", which the
  repair retracted for φ(u₀) > 1; MENU_STERILITY §7 table row "+ integer T1 points (Thm 3.3)" is correct. Also the descriptive
  "Brauer/2-descent pairing" language and the Bruin–Stoll fake-Selmer remark are interpretation (fine as Assessment), not proved
  identifications; label the "= 2-descent object" phrase Assessment.
* Consistency check (free): Theorem B's family is polynomial in X on X ≡ 6 (11), whose closure contains X* (= 1/2 at odd ℓ,
  0 at 2; 1/2 ≡ 6 mod 11), φ(X*) unit, ≡ 1 (8). So Theorem A + B ⟹ X* ∉ Ster(48X⁴ + 1). With γ forced to (ρ − θ)⁻¹ up to global
  squares (an element locally a square at almost all places is a square), this says θ(θ − 1/2) is not a square in A ⊗ ℚ₂ —
  consistent with §4.2 (the author's 2-adic test covers 3θ^e + 1, e = 3, 5, 7, not the SG algebra; not needed).

## 3. Prop 4.1 (constant windows m ≡ 7 (8) dead at μ = 0) — SOUND-AFTER-REPAIRS (missing sign step)

Re-derived: near μ = 0, n ≡ 4^i, K ≡ 4^{i−1} (mod m), gcd(m, nK) = 1, so y ∈ ℤ forces d ≡ −K and (d/m) = −1. K(ρ) = (4^i + m)/4 ✓
(2^j ρ^e = 1). Odd primes of atom values and of λ divide N₀ = 4^i + m (the case split for λ is unnecessary: q | K(U) on the class and
U → ρ q-adically in the closure give q | K(ρ) directly). For q | N₀: (q/m) = (−m/q) = 1 ✓ (m ≡ 3 mod 4).
**Gap (D4, essential but one-line):** the proof computes (d(ρ)/m) = (2/m)^{v₂(d(ρ))}, silently assuming d(ρ) > 0. If d(ρ) < 0 the
conclusion flips (my `scripts/review_r252_prop41.py`: with negative d, windows m ≡ 7 (8) DO satisfy the congruence, 3721 instances
for m < 3000; with positive d: 0 counterexamples to the claim). Repair: K(U) = (c2^jU^e + 1 + m)/4 is aU^e + b with a, b > 0, so no
factor of K has a positive real root; normalise atoms to positive leading coefficient, then atoms(ρ) > 0, and λ > 0 since d > 0 for
large U. Same for SG (K = c(4X⁴ + t⁴) has no real roots). With this line the proposition is SOUND.
Scope note: "(all m = c·2^j w − 1 with j ≥ 3 …) are dead" ✓ (m ≡ −1 mod 8). The consistency with Theorem B: m = 11 ≡ 3 (8), rules
used at s ≡ 0 (40) are (0,2,1), (2,0,1) with v₂(d(1/2)) = −3, −1 (odd) ✓; (0,0,2) (v₂ = −2) is used only at s ≡ 8, 36 (40),
not near μ = 0 ✓.

## 4. Prop 4.3 (SG menu at μ = 0 finite) — GAP (menu scope; the proof covers a restricted menu)

The resultant/Bezout argument is correct for the menu it treats: d = (Π_{q|c} q^{a_q})·f₊^x f₋^y. Checked: 4ct⁴ − 1 irreducible iff c
not a square (and c = 4^i − 1 is never a square for i ≥ 1, so that hypothesis is automatic); m(t) | N(t), Res ≠ 0 ⟹ m(t) | Res ✓;
N(τ) > 0 at the real root τ ⟹ m ∤ N ✓; derivation of N (X ≡ 1/2, f± ≡ g±/2, K ≡ 4^{i−1}) ✓.
**Defect D7 (MAJOR, scope/consistency).** Prop 4.1 allows an arbitrary constant λ (whose odd primes divide K(ρ)); Prop 4.3 silently
restricts λ to primes of c (`z15_sg_mu0_complete.py`: "atoms q | c"). But at μ = 0, K(ρ)·4 = 4^i + m(t) = c·g₊(t)·g₋(t), so λ may
legitimately carry any primes of the integers g±(t) (e.g. d = q·f₋ with q | g₊(t): q | f₊(X) on the neighbourhood X ≡ 1/2 (mod q),
and d | K²). These are constant windows near μ = 0 but N then depends on a divisor of g±(t) — not a polynomial in t, and the
resultant argument does not apply. So "the SG menu at μ = 0 is a FINITE menu (PROVED)" is proved only for the restricted menu.
Evidence check (`scripts/review_r252_sg_general.py c 301`): with the GENERAL λ (any odd D | (c g₊ g₋)², x + y ∈ {0..4}), nothing
fires for c = 15, 63, 255 (t ≤ 301), and for c = 3 only t = 1 (with extra general-λ variants D = 75, 3). So the negative EVIDENCE for
c = 15, 63, 255 survives the enlarged menu, but the finiteness claim does not have a proof for it (heuristically Σ τ(t⁴)/t⁴ < ∞
suggests finiteness — Assessment). Repair: define the SG menu explicitly as λ supported on primes of c (PROVED finite), and add the
general-λ menu as EVIDENCE (or prove finiteness for it); adjust §4.1 "Reason (PROVED, Prop 4.3)" and §4.2 "finite arithmetic
accident" accordingly. Also MINOR D8: garbled sentence "For c = 3 the first case cannot occur for any c (R-O240 repair)".

## 5. Prop 3.1 (Thm 2.2 fails for algebraic-parameter families) — SOUND

Re-derived: m = 16v³ ⟹ m² = 256u³ with u = v², so SYNTHESIS_SPARKS6 Lemma 1.0 (re-read on main: x = 64(u³+1), y = nA, z = 32n(u+1)A,
A = (64u³ + 2u² − 2u + 66)/151, u ≡ 32 (151)) is Type II (n | y, z), polynomial in v, on v² ≡ 32 (151) (32 is a QR mod 151).
`scripts/review_r252_prop31.py`: (a) for every odd ℓ < 2000 there is v mod ℓ (with v² ≡ 32 at ℓ = 151) making 256v⁶ + 105 a NONZERO
square mod ℓ (Hensel ⟹ unit square); (b) the family identity holds exactly at all 40 integers v < 3000 in the class. Weil step:
w² = 256v⁶ + 105 is smooth of genus 2 off ℓ | 2·3·5·7 (disc of av⁶ + b is supported on 2, 3, a, b), lc = 16² a square ⟹ 2 points at
∞, ≤ 6 with w = 0, so ≥ ℓ + 1 − 4√ℓ − 8 > 0 affine points with w ≠ 0 for ℓ ≥ 37 ✓. At 2: m ≡ 0 (16) ⟹ n ≡ 1 (8) ✓. Gluing over the
product Ẑ ✓. Consistency: the only integer T1 point m = 16v³, m² + 105 = □ is v = 1 (n = 361 = 19²), and v = 1 ∉ {v² ≡ 32 (151)} ✓.

## 6. Prop 5.1 (thin menus vs positive-density prime sets) — SOUND (elementary; correctly scoped)

Trivial counting + Dirichlet: a finite union of sets with O(X^{1−δ}) elements ≤ X has relative density 0 in any unit class, so the
primes in the ET-missed neighbourhood C stay missed with positive relative density. The add-on "answer to (2)" is correctly limited to
thin items; the norm-form discussion is properly labelled (PROVED d = 2 under (J)3's hypotheses; Assessment d ≥ 3). The function-field
transfer (§6) needs Dirichlet for 𝔽_q[T] (Kornblum) — true; the rest of §6 is Assessment as labelled.

## 7. §4.1 / §4.3 spot checks
* 7·4^s + 9 at μ = 0 (`scripts/review_r252_c7.py`, from scratch): n = 112X⁴ + 9, X = 2^{(s−2)/2}, K = 7f₊f₋, window m = 19; window-19
  rules with d = 7^a f₊^b f₋^c cover every s ≡ 0 (mod 90) (checked over the full period, ord₁₃₃(2) = 18) and exact solutions at
  s = 90, …, 450 ✓. So "μ = 0 of 7·4^s + 9 is covered by SG(19)" is SOUND (PROVED-level, though filed under EVIDENCE in §4.1 because
  the family as a whole is not decided — fine, but the §7 table could say "PROVED (μ = 0 neighbourhood)").
  I did not re-check the L* = 128520 / 1413720 stuck-lift numerics (EVIDENCE as labelled).
* §4.3 "T1 control explains the two dead residues (PROVED)": correct for the window-11 menu as defined — integrality of all such
  rules depends on X mod 33, the dead classes are X ≡ ±1 (mod 33), which contain the integers X = ±1 with φ(±1) = 49 and φ has no
  real root, so Thm 3.3 applies (positivity on all of ℝ). Caveat to add: Thm 3.3 says nothing about polynomial-in-X rules valid only on
  subclasses avoiding X = ±1 (e.g. additionally X ≡ 0 (mod 4)); the family X = 2^k does lie in such subclasses (k ≥ 2). So "explains"
  applies to the mod-33 window menu only (MINOR D9). Also garbled text "(= Theorem A with not via Theorem A: …)" (MINOR D8).

## 8. Labels and novelty
* Labels: Theorem C PROVED (computer-assisted) ✓; Theorem A PROVED ✓ (with D5 wording); Prop 4.1 PROVED after D4; Prop 4.3 PROVED
  only for the restricted menu (D7); Props 3.1, 5.1 PROVED ✓; §4.1 numerics EVIDENCE ✓; §4.2/§6 interpretation Assessment ✓.
  The "Status: … unreviewed" header and "no infinite case of ES for primes is claimed" are accurate.
* Novelty: quick web search (Jina; queries "Erdos-Straus conjecture Proth numbers 3*2^n+1", "Erdős–Straus equation 4/n numbers of the
  form k*2^n+1", "Erdos Straus Fermat/Mersenne numbers") found nothing on ES for 3·2^s + 1 or any k·2^s + 1 family. Not exhaustive
  (no MathSciNet/zbMATH access). Note that for this specific family the result is elementary once found: 96 of 120 residues fall to
  textbook divisor/ET identities and the rest to a single Aurifeuillean identity, so it may well be "folklore-invisible" rather than
  new — the author's "no claim of priority" is the right stance. Its campaign significance (a proved ET/divisor-uncoverable family on
  which ES nonetheless holds) is real and correctly stated.

## Defects (numbered)
* **D7 (MAJOR)** Prop 4.3 / §4.1 / §4.2 / memo z15_window_jacobi_mu0: "SG menu at μ = 0 is finite (PROVED)" covers only λ supported on
  primes of c; Prop 4.1's own menu allows λ with primes of K(ρ) = c·g₊(t)g₋(t)/4, for which N is not polynomial in t and the resultant
  argument fails. Repair: state the restricted menu explicitly in Prop 4.3; label general-λ finiteness Assessment, cite R252 numerics
  (general λ: no firing for c = 15, 63, 255, t ≤ 301; c = 3 only t = 1).
* **D4 (MINOR but essential)** Prop 4.1 proof: positivity of d(ρ) is used silently; it is needed (negative d breaks the claim). Insert:
  "K(U) = aU^e + b with a, b > 0 has no positive real root, so (atoms normalised with positive leading coefficient) every atom is positive
  at ρ > 0, and λ > 0 since d > 0 for large U; hence d(ρ) > 0."
* **D5 (MINOR)** Theorem A proof, zero-divisor step: "h(u)/gcd(h(u), g^∞) > 1 for large u" is false in general; replace by "for u ∈ C
  close to u* at the primes of 2g·lc, φ(u) is prime to g and |h(u)| > 1, so some prime ∤ g divides gcd(D̃(u), φ(u))".
* **D1 (MINOR)** Theorem B uses d = 9f₋ = (2,0,1) while Theorem C's table lists (0,2,1) for s ≡ 0, 12 (40); both valid — say so.
* **D2 (MINOR)** Theorem C(b): the true period is 120 (lcm(40, 3, 4, 60)) and no "s ≥ 10" threshold is needed; better, insert the
  by-hand coverage (mod 7 kills s ≢ 0 (3); mod 15/5 kills s ≢ 0 (4); left ∩ SG-dead = s ≡ 24, 84 (120) ⊂ s ≡ 24 (60) = n ≡ 0 (61)),
  which makes Theorem C checkable without a computer.
* **D3 (MINOR)** Theorem B "Why it is not a contradiction": "{s ≡ 0 (40)} is the n-congruence class …" → "is the intersection of the
  family with the n-congruence class …".
* **D6 (MINOR)** memo z15_witness_descent barrier screen still says squares are built in via γ = 1/(u₀ − θ) (retracted for φ(u₀) > 1);
  "2-descent/Brauer pairing" identification should be marked Assessment.
* **D8 (MINOR)** garbled sentences: Prop 4.3 "For c = 3 the first case cannot occur for any c (R-O240 repair)"; §4.3 "(= Theorem A with
  not via Theorem A: …)".
* **D9 (MINOR)** §4.3: restrict "T1 control explains the two dead residues" to the mod-33 window-11 menu (subclasses avoiding X = ±1
  are not excluded by Thm 3.3).
* Cosmetic: section order in MENU_STERILITY.md is §1, §4, §3, §5, §6, §7, then "4.3" after §7.

No FATAL defects. The HEADLINE (Theorem C) is SOUND.
