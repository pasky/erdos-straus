# R268 — hostile review of O258 SYNTHESIS_SPARKS8 (synthesis VIII)

Reviewer: R268 side agent. Status: IN PROGRESS. Scripts: `scripts/review_r268_*.py` (from scratch; author scripts not reused).

## Summary verdicts
(filled in as checks complete)

## Defects
(numbered below)

---
## Claim A — SHARP census (§2.4, Conj. 2.5 evidence): **SOUND** (independently reproduced to 10⁸ in full)

**Re-derivation (reviewer's own "t-form", different from both the author's window and divisor forms).** From
c p + a + 1 = 4acd: w := 4cd − 1 | cp + 1 ⇒ w | 4d(cp + 1) − p·w = p + 4d; put g := (p + 4d)/w, so g(4cd − 1) = p + 4d, i.e.
4d(cg − 1) = p + g. With t := cg − 1: **b = 1 line ⟺ ∃ t ≥ 1, g | t + 1, 4t | p + g** (c = (t+1)/g, d = (p+g)/(4t), and
a = (cp+1)/w is integral because c(p + 4d) ≡ cp + 1 (mod w)). For p = 4i + 1 this is: g ≡ 3 (4) and i ≡ −(g+1)/4 (mod t), and
d ≥ 1 is automatic. Completeness: g ≤ t + 1 and 4t ≤ p + g give **t ≤ (p + 1)/3**, and since g < 4t, g must be the least residue
of −p mod 4t, so the per-p decision is O(p) trivial operations. (The author's bounds m ≤ (p + 4)/3 for the window form and
d ≤ (p + 3)/8 for the divisor form were also re-derived: the window bound from 4a ≤ p + m ≤ p + a + 1; the divisor bound from
g ≡ 3 (4), hence g ≥ 3, and 3(4d − 1) ≤ p + 4d. Both are correct.)
c = 1 line: p = 4i + 1, a + b ≡ 3 (4), i ≡ −(a+b+1)/4 (mod ab); per-p completeness via a ≤ b ⇒ a(4a − 2) ≤ p, b | p + a.

**Engine** `scripts/review_r268_census.py` (numpy residue-class sieve over all p at once for t ≤ T₀ and ab ≤ T₀, then a
complete per-p decision for the primes the sieve leaves). Logs `logs/review_r268_census_1e7.txt`, `logs/review_r268_census_1e8.txt`.
* **Full independent run to 10⁸** (13 s, T₀ = 5·10⁴): 2 880 504 primes p ≡ 1 (4) ≤ 10⁸ (= 332 180 + 2 548 324, matching the
  author's two logs). b = 1 failures **exactly {193, 2521, 66529}**; c = 1 failures **exactly the 14 primes 409, 577, 5569, 9601,
  23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281** (9 of them ≤ 10⁶); intersection **empty**.
* `scripts/review_r268_brute.py` (log `logs/review_r268_brute.txt`): pure triple loop over (a, c, d) vs t-form, all n ≡ 1 (4),
  5 ≤ n < 300: 0 existence mismatches; (c, d)-enumeration finds 0 solutions at 193, 2521, 66529 (and agrees with the t-form count
  at the neighbours 197, 2549, 66541: 5, 13, 13).
* `scripts/review_r268_spot.py` (log `logs/review_r268_spot.txt`): 400 random primes p ≡ 1 (4) in (10⁷, 10⁸]: explicit b = 1 and
  c = 1 witnesses found by a third method (factor p + 4d, resp. divisors of p + a) and verified in exact rationals
  4/p = 1/x + 1/y + 1/z. At each of the 3 b = 1 failures an explicit c = 1 witness, and at each of the 14 c = 1 failures an
  explicit b = 1 witness, verified exactly (e.g. 66529: (a, b, d) = (5, 26, 128) on c = 1; 8813281: (a, c, d) = (1111585, 14, 2)
  on b = 1).
* T1 / 105 controls: both lines fail at every odd square 9, …, 529 and at 105 (confirmed).
* k = 8 analogue (c n + a + 1 = 8acd; n + a + b = 8abd), own code: over **all primes 5 ≤ p < 8000**: b = 1 fails at 60, both
  fail at 34 incl. 131 and 241 — **matches** (the count is 61 / 35 if p = 3 is included; see defect m1).

---
## Claim B — Props 1.2–1.5, Lemma 1.6, DFI paragraph, §1.7 table

**Prop 1.2: SOUND-AFTER-REPAIRS** (defect m2). The bijection (x, y) = (a, b), N = 4cd is a rewriting; re-derived. The b = 1
bullet adds "w ≤ (cn + 1)/2", which is false for odd n ≡ 3 (4): at n = 3 the only b = 1 solution is (a, c, d) = (1, 2, 1) with
w = cn + 1 = 7. The side condition is also unnecessary (any w ≡ −1 (4c), w | cn + 1 gives d = (w+1)/(4c) ≥ 1, a ≥ 1).
**Prop 1.3: SOUND.** Re-derived independently (reviewer's t-form above is the same identity with t := cg − 1); the "Reading"
(b = 1 ⟺ a coordinate ≡ 0 (4); c = 1 ⟺ N ≡ 0 (4); union fails ⟺ every even coordinate has v₂ = 1 and v₂(N) ≤ 1) is correct
for primes p > 3 (MP-pairs are coprime there: gcd | p and p | x, y forces p = 3). The T1 sentence cites ET Prop 1.6, which is
stated for *Type II solutions* (n ∤ x, i.e. abd coprime to n); the MP statement needs vanishing of the *equation*
cn + a + b = 4abcd without coprimality (defect m3). Reviewer check (`scripts/review_r268_squares.py`): no solution of the
equation, any gcd, at every odd square 9 … 841 — so the statement is right, but the citation does not literally cover it.
**Prop 1.4: SOUND-AFTER-REPAIRS** (defect m4). (a) "0 ≤ (k+1)y − n < y" fails at the endpoint y = n/k (value y, least residue 0);
harmless for prime n. (b) The displayed correspondence "MP(p) ∩ {x < y} ↔ {(x, s) : x | s + 1, s | p + x}" is wrong as stated:
the right-hand set maps onto ALL of MP(p) (reviewer check, primes 5 … 219: image = MP(p) exactly, and 747 of 1449 image points
have x ≥ y). Either drop "∩ {x < y}" (correct and cleaner: MP(p) ↔ {(x, s)}, s = (p + x)/y) or add the condition (s − 1)x < p.
(c) The proof's "x | (k + 2)n − ... i.e." is a placeholder; the clean line is (k+1)(n + y) = (k + 2)n + x.
**Prop 1.5: SOUND.** Re-derived: (4cud − 1)ε = cp + u, and (4cdu − 1)(4cdv − 1) = 4c²dp + 1 ⟺ cp + u + v = 4cuvd. The
"what fails" paragraph is correctly labelled Assessment.
**Lemma 1.6: GAP (label).** First sentence (CRT density Σ 1/(xy) ≍ 1; for primes it is Σ 1/φ(xy), still ≍ 1) is PROVED and
trivial. The "Consequently any completion count … leaves an error ≍ (XY)^{1/2}" part is NOT a theorem: (i) the "complete
exponential sum S(h, k) of length ≍ XY" is never defined — the moduli xy vary with the pair, so there is no single completion;
(ii) the triangle-inequality computation gives an *upper* bound (XY)^{1/2+o(1)} for one particular strategy, not a lower bound
on the error of "any completion"; (iii) "needs cancellation across frequencies" is a heuristic conclusion. Defect M1.
**DFI paragraph: GAP (misdescribed citation).** Checked against sources/dfi-1997-kloosterman-fractions.pdf. DFI's bounds are
stated "for any positive integer a" but are **explicitly a-dependent**: Thm 1 has the factor (1 + a/MN)^{1/2}, Thm 2 the factor
(a + MN)^{3/8}, Thm 3 (a + MN)^{14/29}; the paper itself says the improvement over the trivial bound needs "a ≪ MN, a condition
usually satisfied in applications". So "uniform in the numerator a" is inaccurate; with a ≍ p it is nontrivial only for boxes
with MN ≳ p (Thm 2 needs roughly MN ≫ p and M, N not too unbalanced), and trivial for boxes XY = o(p). Second error: DFI's
saving is a *bilinear* saving over varying moduli n — it is precisely cancellation across many incomplete sums with different
moduli, not "at the level of a single S(h, k)". Defect M2.
**§1.7 table: SOUND-AFTER-REPAIRS** — rows 1, 3, 4 fine as Assessment; row 2 must be rewritten per M2 (fixed a = p is part of
the obstruction for every box with XY = o(p)). The four-coordinate equivalence itself is sound.

---
## Claim C — §2.1, Lemma 2.2, Lemma 2.3, per-j statistics

**§2.1: SOUND.** Re-derived: with a = s, c = j, s(4jd − 1) = jp + 1; since jp ≡ j (mod 4j) for p ≡ 1 (4), s ≡ −(j+1) = 3j − 1
(mod 4j); conversely gcd(3j − 1, 4j) = 1 for j even, so the class pins w ≡ −1 (mod 4j), and w ≥ 4j − 1 ≥ 3 gives d ≥ 1. For odd j,
3j − 1 is even ⇒ s = 2 ⇒ 4j | 3j − 3 ⇒ j = 1. (So the precise statement: odd prime s forces j even; s = 2 occurs only at j = 1,
p ≡ 5 (8).) Reviewer data: 0 odd-prime support-1 successes at odd j ∈ [3, 23], all p ≡ 1 (4) ≤ 10⁶.
**Lemma 2.2: SOUND.** (a) re-derived line by line: (−cp/w) = 1, (−1/w) = −1, (c′/w) = (w/c′)(−1)^{(c′−1)/2} = 1 using w ≡ −1 (c′)
and (w−1)/2 odd, (2/w) = 1 when 2 | c (w ≡ 7 (8)), reciprocity (w/p) = (p/w) for p ≡ 1 (4); gcd(w, p) = 1 needs gcd(d, p) = 1
(stated). (b) (−4d/·) is periodic mod 4d (−4d ≡ 0 (4) is a discriminant), and (−4d/p) = (d/p). Burgess exponent 1/(4√e) and
GRH (Ankeny/Bach ≤ 2 log²p) are correctly quoted. Reviewer check (`scripts/review_r268_perj.py`): 2075 divisor-form hits for p ≡ 1 (4)
< 4000, all with (w/p) = −1; 29 636 levels with (d/p) = −1, all with χ_{−4d}(p + 4d) = −1.
**Lemma 2.3: SOUND** (trivial). The p + 4d version holds already for odd ℓ > D (p + 4d is odd), so "ℓ > 4D" is merely weak.
The "Reading" is an Assessment (unlabelled) — defect m5.
**Per-j statistics: SOUND (EVIDENCE).** Reviewer's own recomputation (all 39 175 primes p ≡ 1 (4) ≤ 10⁶, j ≤ 24): rates
0.128, 0.389, 0.474, 0.523, …, 0.907 (identical to 3 decimals); pairwise joint/product mean 1.0040, max 1.269 at (j, j′) = (1, 4),
min 0.937; all 24 fail at 10 primes vs 6.57 predicted. All match the author.

---
## Claim D — Lemma 3.1 (§3) and Lemma 4.1 / Cor. 4.2 (§4)

**Lemma 3.1: SOUND.** (a) 4K ≡ q (mod p), (4/p) = 1. (b) u ≡ −v (q) ⇒ (uv/q) = (−1/q) = −1; transfer re-derived: for an odd prime
s | K, (s/p) = (p/s) = (−q/s) = (−1/s)(q/s) = (−1/s)(s/q)(−1/s) = (s/q) (q ≡ 3 (4)); for s = 2 | K one has 8 | p + q and the two
2-symbols agree in both cases p ≡ 1, 5 (8) — the lemma is fine for even K too. Reviewer check (`scripts/review_r268_jacobi.py`):
13 500 prime windows (q < 80, p < 2·10⁴), (a) 0 exceptions; 30 996 ordered = 15 498 unordered cap-0 certificates (exactly the
author's count), (b) 0 exceptions. The "Reading" / verdict (iii) is Assessment and reasonable.
**Lemma 4.1: SOUND** (re-derived; the side-number form f | p² + 4c²d, f ≡ −p (4c|d|) is ET (2.9) + (2.6), and conversely
a := (p + f)/(4cd) recovers ET (2.7) since gcd(f, 4c²d) = 1). Credit: it is the (J)52 three-bit law χ·s_∞ = −1 specialised to the
Type I side number (as the header says) and the ET Prop 1.6 reciprocity mechanism. Reviewer check: primes p ≡ 1 (4) < 3000,
c < 5, 0 < |d| < 30, gcd(p, cd) = 1, all divisors f: 4772 positive and 10 787 signed points, 0 exceptions; odd squares 9 … 441:
0 positive points, 3–48 signed points each. (Author's counts 1934 / 2816 / "2–13 each" use a different enumeration convention,
not documented — defect m6.)
**Cor. 4.2: SOUND-AFTER-REPAIRS.** The |d|-preserving obstruction is an immediate, correct consequence. The sentence "the only
involutions are coordinate permutations" is an overclaim: in reciprocal coordinates the ES surface is the plane
X + Y + Z = 4/p, with a large group of (birational/affine) involutions. What is true is that the equation is multilinear, so
there is no Vieta-type involution in a single variable (defect m7).
**§6 credit (MINOR, m8):** §6 lists Lemma 4.1 under "Genuine new content"; it should be listed as a repackaging of (J)52 / ET
Prop 1.6 (the brief's expectation), with the only new element Cor. 4.2's use of it to close (iv).
