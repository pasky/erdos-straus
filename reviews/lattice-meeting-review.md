# R262 — hostile review of O251 (LATTICE_MEETING.md, BRAINSTORM/z23_*.md)

Reviewer: R262 side agent, branch side-agent/review-lattice-meeting, merged side-agent/lattice-meeting at start.
From-scratch scripts: `scripts/review_r262_*.py` (none reuse z23_* code).

## Verdict summary (filled in claim by claim)

## Claim-by-claim

### C1. p = 3361 (CERTIFIED) and "only such prime ≤ 10⁷"
Independent complete enumeration (`scripts/review_r262_3361.py`, sympy only for factoring/divisors).
Completeness proof used: Type II means p | y, p | z, p ∤ x. Then y, z ≥ p ⇒ 1/x = 4/p − 1/y − 1/z ≥ 2/p, so
x ≤ p/2, and x > p/4. With y = pY, z = pZ, m = 4x − p ≥ 1: (mY − x)(mZ − x) = x², mY − x > 0. So looping over all
x ∈ (p/4, p/2] and all δ | x² with δ ≡ −x, x²/δ ≡ −x (mod m) lists every ordered solution. Result for p = 3361:
exactly two unordered solutions, (x, Y, Z) = (841, 290, 8410) and (850, 25, 170) — matches the document. Slices
g = 4Y − 1, D = 4Z − 1: 1159 = 19·61, 33639 = 3·11213, 99 = 3²·11, 679 = 7·97; −3361 is a non-square modulo each
(checked by brute force over every prime-power factor); gcd(slice, p) = 1 in all four cases. ET parameter
d = gcd(x, Y, Z) is 29 resp. 5, matching (1, 29, 10, 29) and (5, 34, 1, 5).
Spot-check of the ≤ 10⁷ scan (`scripts/review_r262_meet.py`, `scripts/review_r262_split.py`, both from scratch):
* 𝓜(p) = ∅ recomputed by Prop 1.1(iii) over **all** 332 180 primes p ≡ 1 (4) ≤ 10⁷ (SPF sieve to 2·10⁷;
  a ≤ (1 + √(4p+1))/4 suffices because the locus is symmetric in a, b and (4a−1)(4b−1) ≤ 4p+1): exactly **160**
  empty, blocks 22 / 23 / 54 / 61, all ≡ 1 (12) — matches. The 99 primes ≤ 10⁶ match the document's prefix and counts.
* For each of the 160: least ET d with any Type II solution {2: 157, 3: 1, 5: 2}; least d with a solution having a
  split slice (g or D) {2: 148, 3: 9, 5: 2, none ≤ 60: 1 = **3361**} — matches the document (≤ 10⁶: 96/1/2 and 88/8/2).
* Why only the 160 can be candidates (re-derived): if 𝓜(p) ≠ ∅ there is a d = 1 solution and g | p + 4a² with
  gcd(g, p) = 1 (p | g would force p | a, but a ≤ (p+1)/3), so −p ≡ (2a)² is a square mod g. ✓
* p = 3361 rechecked a third way: ET-parameter loop over **all** d ≤ (p+1)/3 (= 1120) and all a ≤ (1+√(4dp+1))/(4d)
  returns exactly the same two solutions, both invisible.
Reason (PROVED, re-derived): for (a, b, c, d) with g = 4acd − 1, (4acd − 1)(4abd − p) = 4a²d + p, so
−p ≡ 4a²d (mod g) and g ≡ −1 (mod 4ad) is prime to 2ad; hence −p is a square mod g ⟺ d is (mod each prime power of g).
Same for D = 4bcd − 1 by the a ↔ b symmetry. ✓

**Verdict C1: SOUND.** (Visibility is *defined* as "slice g = 4y/p − 1 or D = 4z/p − 1 is split"; with that
definition the CERTIFIED label is earned — two independent complete methods here plus the author's.)

### C2. Prop 1.1 / Cor 1.2 and the 99-prime list
Re-derived line by line: (i)⇔(ii) [(2k,1) ∈ L_ρ(g) ⟺ g | 4k²p+1, ρ = (2k)⁻¹ forced; D ≡ −1 (4k) since gD ≡ 1];
(ii)⇔(iii) [gm = 4a(4kab − kp − b) + p = 4a² + p; conversely m ≡ −p (4a), 4a(a+b) = m(g+1)]; the identity
(pk + a + b)/(pkab) = 4/p; bounds (4a−1)(4b−1) ≤ 4p+1, max ≤ (p+1)/3, k ≤ a+b — all correct. Also checked that
gcd(g, p) = 1 is automatic in (iii) (needed for g to be a slice; not stated in the proof). Cor 1.2(a) (ℓ ≡ 3 (4),
ℓ | c² + (2a)² ⇒ ℓ | a, contradicting g ≡ −1 (4a)) and (b) ((a, g) = (1, 3)) correct.
Numerics: 99 empty among 39 175 primes ≤ 10⁶, 22/23/54, all ≡ 1 (12), odd squares ≤ 10⁶ all empty — reproduced.
Independent second method (no Prop 1.1): complete Type II enumeration with the criterion "𝓜(p) ≠ ∅ ⟺ some Type II
solution has gcd(x, y/p, z/p) a perfect square" (ET Prop 2.6 uniqueness + dilation d ↦ d/s²): agrees on all 1 125
primes p ≡ 1 (4) ≤ 2·10⁴.
Mean-count remark (§1, R-O251 repair): reproduced ordered mean 24.37 and scan mean 13.35 (p ≤ 10⁵), **but** the
unordered mean is 12.19, so the sentence "the scan a ≤ √p + 2 sees each unordered {a, b} once in one orientation" is
false — it sees every unordered pair at least once, ~9 % of them in both orientations (defect m1).

**Verdict C2: SOUND** (one MINOR wording defect m1).
