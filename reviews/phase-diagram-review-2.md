# Hostile review #2 of PHASE_DIAGRAM.md (O204) — R210, round 1

Reviewer: R210 (independent; R209's review not read before this file was written). Document reviewed:
PHASE_DIAGRAM.md as merged from `side-agent/phase-diagram`. From-scratch scripts: `scripts/review_pd2_*.py`
(no reuse of `scripts/pd_*`). No edits to PHASE_DIAGRAM.md in this round.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Prop 1.1 (normal form) + D-face | SOUND (one MINOR wording point, m1) |
| Thm 2.1 (k-wall, band, sharpness) | SOUND |
| Consequence "ES^{(y,1)} finite search?" | NOT claimed by the doc; R200 M1 stands (see §2 below; MINOR m2 on wording) |

## Claim-by-claim

### Prop 1.1 (normal form k(4ab − n) = b + aQ₁²) and the D-face — SOUND

Re-derived by hand. Forward: with j' = (m + n)/Q₀ ∈ 4ℤ (Prop 1.3) and b = j'/4, Prop 1.3(a) reads
4aD = 4kn + 4b with D = 4kb − Q₁², i.e. a(4kb − Q₁²) = kn + b ⟺ k(4ab − n) = b + aQ₁². Converse: with
m = 4ab − n and km = b + aQ₁²: (4ak − 1)m = 4a·km − m = 4ab + 4a²Q₁² − 4ab + n = n + 4a²Q₁² ✓; and
gcd(aQ₁, ak) = a·gcd(Q₁, k) = a ✓. Mute rungs: under gcd(Q, n) = 1 and gcd(Q₁, k) = 1, rad Q₁ | y = nak ⟺
rad Q₁ | a, and den z = Q₁² | y² ⟺ Q₁ | a ✓. ES line Q₁ = 1 is 4abk = a + b + nk, the d = 1 slice of Type II ✓.
D-face: a = λt (Q₁ = t | a): k(4λtb − n) = b + λt³ ✓. Side conditions: gcd(b, n) = 1 is automatic for shots
(4Q₀b = m + n and gcd(m, n) | gcd(4Q², n) = 1), m is odd, m ≡ −n (mod b), and
4b(b + λt³) = 4b² + t²(m + n) ≡ nt² + 4b² (mod m) ✓. Both self-review counterexamples (n = 9; n = 61) verified by hand.
The (Y2) example n = 13: 13 + 4·25² = 2513 = 7·359, K = 90, Q₀ = 5, Q₁ = 5, k = 18 ✓.
Numerics (`review_pd2_brute.py 61 100001`: direct enumeration of all shots Q ≤ 10⁵ odd, ES^{[2]} decided by
den z | y² on the exact solution, not via Q₁ | Q₀): 5 617 435 shots, 231 ES^{[2]}; identity (1.1),
gcd(Q₁, k) = 1, den z = Q₁² hold in all 231.

### Thm 2.1 (second archimedean wall) — SOUND

(a) Re-derived: Q₁ | Q₀ ⇒ g = 4kQ₀ − 1 ≡ −1 (mod 4kQ₁), so g ≥ 4kQ₁ − 1, and Dg = 4k²n + Q₁² mod Q₁ gives
D ≡ −4k²n, so Q₁ | D + 4k²n > 0 and D ≥ Q₁ − 4k²n. If Q₁ > 4k²n:
(Q₁ − 4k²n)(4kQ₁ − 1) ≤ 4k²n + Q₁² ⟺ (4k − 1)Q₁² ≤ (16k³n + 1)Q₁ ✓ (the 4k²n terms cancel exactly). The case
Q₁ ≤ 4k²n and the identity 16k³n + 1 = (4k − 1)(4k²n + kn) + kn + 1 ✓; W(k) ≤ 6k²n ✓ (k = 1: 16n + 1 ≤ 18n).
(b) Re-checked against EXPONENT_CAP Thm 2.1's proof: the branch kj ≥ 2Q₁² gives Q₀ ≤ 2n/j + 1/(2k) ≤ (n+1)/2
(j ≥ 4), so Q₁ | Q₀ ⇒ Q₁ ≤ (n+1)/2; otherwise k ≤ kj/4 < Q₁²/2 ✓. No hidden hypothesis (gcd(Q, n) = 1 is not used).
Band and "both slicings finite": fixed k ⇒ Q₁ ≤ W(k) ⇒ finitely many (Q₁, D); fixed Q₁ ⇒ g bounded ✓.
Sharpness: (n, k, Q₁) = (3, 2, 55): 48 + 3025 = 3073 = 7·439, Q₀ = 55 ✓. Family n ≡ 2 (mod 3):
(4n+1)(64n+1) = 256n² + 68n + 1 = 9(4n) + (16n+1)² ✓; D ≡ 3 (mod 4) ⟺ n ≡ 2 (mod 3) ✓; Q₀ = Q₁ ✓. The aside
Q₁ = 4n + 3, D = 3: Q₀ = (4n+3)(n+1)/3, so Q₁ | Q₀ ✓ (n ≡ 2 mod 3).
Numerics (`review_pd2_wall.py 101 6 20000`, duality-face enumeration with Q₁ up to 3·W(k), exact solution
check): 348 ES^{[2]} shots, all with Q₁ ≤ 1.3W(k) (none in (1.3W, 3W]), zero violations — the author's 348
reproduced; the author's "12 skipped" equals my count of gcd(Q₀, n) > 1 with gcd(Q₁, n) = 1 (46 if Q₁ is
not pre-filtered; convention only). Equality family verified exactly for all 3 333 n ≡ 5 (mod 6) < 2·10⁴ (Q₁
squarefree in 2 698), and the Q₁ = 4n + 3 family likewise. `review_pd2_brute.py 61 100001`: 0 violations of (a)
or (b) among 231 ES^{[2]} shots; max Q₁/W(k) = 1.0000, max k/Q₁² = 0.4360 at (29, 126, 17) — both author
figures reproduced.

### Consequence: is ES^{(y,1)} now a FINITE search? — NO; R200 M1 is NOT superseded

Thm 2.1 bounds each fixed-k and each fixed-Q₁ slice, but the band √(Q₁/(6n)) ≤ k < Q₁²/2 is unbounded, so it
gives no bound on g (or Q₁, or k) in terms of n alone. Concretely, ES^{[2]} shots of a fixed n sit at growing
(k, Q₁): n = 3 has (Q₁, k, g) = (1, 2, 7), (55, 2, 439), (101, 232, 93 727), (289, 2 984, 3 449 503) up to Q ≤ 10⁵;
n = 41 has 23 shots with Q₁ up to 307, k up to 1 969 (`review_pd2_brute.py`; counts keep rising when Q_max goes
3·10³ → 10⁵ for almost every n). Combined with GROWING_MUTE R201 m3 (every ES^{[2]} point with μ² − n non-square
lies on an infinite Pell orbit, A = 2k and B = Q₁ → ∞ together — consistent with the band), the ES^{[2]} search
for one n is a countable union of finite slices with no global bound. For ES^{(y,1)} (squarefree Q₁) the same holds
pending squarefreeness on orbits. Precisely: **R200 M1 ("ES^{(y,e)}, bounded e, growing S: OPEN, not a finite
search") stands for e = 1**; what is new is only that the search is confined to the band, i.e. both coordinates
must grow together (log k ∈ [½ log Q₁ − O(log n), 2 log Q₁]). The document itself never claims a global
finite search (§6 "union of finite searches in both directions" is correct), but see m2.
