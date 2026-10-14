# R209 — hostile review #1 of PHASE_DIAGRAM.md (O204, checkpoint 1)

Reviewer worktree branch `side-agent/review-phase-diagram-2`, merged `side-agent/phase-diagram` at 0e608b96.
From-scratch scripts: `scripts/review_pd_wall.py`, `scripts/review_pd_family.py` (+ further `review_pd_*` below).
None of the author's `pd_*` scripts were used or imported. **ES is not solved; nothing below changes that.**

## Summary verdicts

| Claim | Verdict |
|---|---|
| Prop 1.1 normal form k(4ab − n) = b + aQ₁²; D-face | SOUND (minor notation, m1–m2) |
| Thm 2.1(a) k-wall Q₁ ≤ (16k³n+1)/(4k−1), sharpness families | SOUND |
| Thm 2.1(b) / band √(Q₁/6n) ≤ k < Q₁²/2; "both slicings finite" | SOUND |
| Consequence: is ES^{(y,1)} / ES^{[2]} a FINITE search? | NO — R200 M1 stands (see §2 below; wording m3) |
| (rest: in progress) | |

## Claim-by-claim

### Prop 1.1 — SOUND
Re-derived by hand: g = 4ak − 1, Q = aQ₁, gcd(Q₁, k) = 1 ⇒ Q₀ = gcd(aQ₁, ak) = a. From g·m = n + 4a²Q₁² and
g ≡ −1 (mod 4a): m + n ≡ 0 (mod 4a), b := (m+n)/(4a) ∈ ℤ_{>0}, and 4akm = m + n + 4a²Q₁² = 4ab + 4a²Q₁², i.e.
km = b + aQ₁² with m = 4ab − n. Converse as in the document (expansion checked). Variant translations: y = nak and
gcd(Q₁, nk) = 1, so rad Q₁ | y ⟺ rad Q₁ | a, Q₁² | y² ⟺ Q₁ | a; ES^{(y,1)} = (Q₁ squarefree, Q₁ | a) by
EXPONENT_CAP Def 1.1. All correct. `review_pd_wall.py A` asserts (1.1) on every shot it finds (348 shots, n ≤ 101,
k ≤ 6, Q₁ ≤ 2W(k)) — found by the DEFINITION (a, Q₁ | a, k, test (4ak−1) | n + 4a²Q₁²), not via the duality.
D-face: gcd(m, n) = gcd(4λtb, n), gcd(m, b) = gcd(n, b), and 4b(b + λt³) ≡ 4b² + nt² (mod m): correct. The two
self-review counterexamples reproduce (`review_pd_family.py`).
Den z = Q₁² is used for all Q although EXPONENT_CAP Prop 1.2 is stated "for Q odd"; my exact-rational check found
den z = Q₁² on every shot including even Q₀ (m2).

### Thm 2.1(a) — SOUND (re-derived; brute force confirms; sharp)
Independent derivation: Q₁ | Q₀ gives g ≡ −1 (mod 4kQ₁) so g ≥ 4kQ₁ − 1; reducing Dg = 4k²n + Q₁² mod Q₁ gives
D ≡ −4k²n (mod Q₁); since gcd(Q₁, 2kn) = 1 (Q₁ | Q, gcd(Q, n) = 1; gcd(Q₁, k) = 1 by definition of Q₀), for
Q₁ > 4k²n the least positive such D is ≥ Q₁ − 4k²n, and (Q₁ − 4k²n)(4kQ₁ − 1) ≤ 4k²n + Q₁² expands to
(4k−1)Q₁² ≤ (16k³n+1)Q₁. Division (4k−1)(4k²n + kn) = 16k³n − kn checks the displayed form; ≤ 6k²n holds for k ≥ 1.
No hidden hypothesis (the only inputs are gcd(Q, n) = 1 and Q₁ | Q₀; D ≥ 1 is automatic).
Brute force (`review_pd_wall.py A 101 6 2.0`, 54 s): searching Q₁ up to **2·W(k)** (author: 1.3·W), odd n ≤ 101,
k ≤ 6: 348 ES^{[2]} shots, all with den z | y², max Q₁/W = 1.0000, no violation. (Same count as the author's
search to 1.3W — consistent with nothing existing in (1.3W, 2W].)
Sharpness (`review_pd_family.py`): (3, 2, 55, g = 439) attains W(2) = 55 exactly (Q₀ = 55, den z = 55²); the family
Q₁ = (16n+1)/3, g = (64n+1)/3, D = (4n+1)/3, Q = Q₁² verified for all 3 333 odd n ≡ 2 (mod 3), n ≤ 20 000
(exact solution, k = 1, Q₀ = Q₁, Q₁ = W(1)). The side family Q₁ = 4n + 3, D = 3 (Q₀ = (4n+3)(n+1)/3) also verified
on the same range. n = 59: W(1) = 315 = 3²·5·7 confirmed. Note "every n ≡ 2 (mod 3)" means odd n, i.e. n ≡ 5 (mod 6)
(n odd is global; harmless).

### Thm 2.1(b) and the band — SOUND
The cited case split of EXPONENT_CAP Thm 2.1 re-checked: kj ≥ 2Q₁² ⇒ D ≥ kj/2 ⇒ Q₀ = (4kn+j)/(4D) ≤ 2n/j + 1/(2k)
≤ (n+1)/2 (j ≥ 4). With Q₁ | Q₀, Q₁ > (n+1)/2 forces kj < 2Q₁², hence even k < 2Q₁²/j ≤ Q₁²/2. Brute force
(`review_pd_wall.py B 61 61 1.0`, 38 s): every odd n ≤ 61, odd Q₁ ≤ 61, ALL k ≤ Q₁² (i.e. twice the claimed band
edge), all divisors g ≡ −1 (mod 4kQ₁) of 4k²n + Q₁²: 172 ES^{[2]} shots, each an exact solution with den z | y²; no
k-wall violation; among Q₁ > (n+1)/2, max k/Q₁² = 0.4360 (attained (29, 126, 17), g = 8567, as the author reports);
no shot with k ≥ Q₁²/2. "Both slicings finite": fixed k ⇒ Q₁ ≤ W(k) and g ≤ 4k²n + Q₁²; fixed Q₁ ⇒ EXPONENT_CAP
Thm 2.1 — correct.

### Consequence: does Thm 2.1 make ES^{(y,1)} a FINITE search? — NO; R200 M1 is not superseded
Thm 2.1 bounds each slice, not the union. Eliminating k with k = (g+1)/(4Q₀) ≤ (g+1)/(4Q₁) in Q₁ ≤ 6k²n gives
Q₁³ ≤ (3/8)n(g+1)², and EXPONENT_CAP Thm 2.1 gives Q₁ ≥ min(√g/(2n), (g/4n)^{1/4}). So for each g the admissible
overflow window is roughly **[(g/4n)^{1/4}, (3n/8)^{1/3}g^{2/3}]**, nonempty for all large g: no a-priori bound on g
in terms of n, so ES^{[2]}(n) and ES^{(y,1)}(n) remain infinite searches (an infinite union of finite slices), exactly
as ES itself (each k-line of ES is one number, but k is unbounded). R200 M1's statement — "bounded e with growing S
is OPEN; the wall only asks rad(Q₁)^e ≳ (r/4n)^{1/4}" — stands. What Thm 2.1 adds to M1 (precise form): in any
large-Q₁ ES^{[2]} shot (Q₁ > (n+1)/2) one also has k < Q₁²/2, i.e. **Q₀ > (g+1)/(2Q₁²)**; so the R200 M1 scenario
"r ≡ −1 (mod 4P), P ≈ r^{1/4}, Q₁ | P" is admissible only with Q₀ ≫ r^{1/2} (Q₀ = gcd(Q, (r+1)/4) must carry a
cofactor λ ≫ r^{1/4} besides Q₁), and Q₁ ≤ ((3n/8)r²)^{1/3}. This narrows, but does not close, M1's open case.
The document itself does not claim global finiteness (Verdict 6 says "a union of finite searches in both
directions"), but the table cell "FINITE" and the ES row "OPEN (finite search, B2/B3)" can be misread (m3).

## Numbered defects

**m1 (MINOR) — §0 (Y2) notation and congruence.** "D = 7" there is the cofactor m = (n+4Q²)/g of §1, not the duality
cofactor D of Prop 1.3 (for n = 13, Q = 25, g = 359: k = 18, D = (4k²n + Q₁²)/g = 47). Also the λ = 1, j = b = 1
test is "64 + n³ has a divisor m ≡ −n (mod 4) with t = (m+n)/4 odd and the gcd side conditions", which is
"≡ 3 (mod 4)" only for n ≡ 1 (mod 4). Repair: rename (m = 7) and state the congruence as ≡ −n (mod 4) plus side
conditions.

**m2 (MINOR) — §1 / §2 check, den z = Q₁².** EXPONENT_CAP Prop 1.2 is stated for Q odd; Prop 1.1 and the checks use it
for every Q (Q₀ may be even). True on every shot I tested, and the proof of Prop 1.2 does not use parity of Q₀, but
say so. The qualifier "(when gcd(Q₀, n) = 1)" in the §2 check is vacuous under the shot convention gcd(Q, n) = 1.

**m3 (MINOR) — §6 table / Verdict 2.** "k-slices FINITE" for ES^{[2]} and "OPEN (finite search, B2/B3)" for ES: add
"(each slice; the cell is an infinite union of slices — Thm 2.1 gives no bound on g in terms of n; R200 M1's
growing-S case remains open, narrowed to Q₀ > (g+1)/(2Q₁²))". Verdict 2's "solutions live in a band of slopes ½…2 in
log coordinates" is right for Q₁ > (n+1)/2 only — add that qualifier.
