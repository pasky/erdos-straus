# s6_numerator_windows — the self-generated mute set for every numerator ν, and window-shape T1 (O238; (i) × (J)46/(J)62)

## Idea
CAP_DOWN Lemma 1.1 holds verbatim for ν/n: with m := νK − n, d ≡ −K (mod m), A = (K + d)/m, (x, y, z) = (K, nA, nKA/d)
solves ν/n = 1/x + 1/y + 1/z (same algebra: ν/n − 1/K = m/(nK)). Forcing (Thm 1.1′ mechanism; K ODD — R-O238 self-review: for even K the 2-exponent is bounded, c₂ ≤ 2v₂(K), and e.g.
ν = 4, n = 5, m = 67, K = 18 has (K/67) = −1 but no window solution at any cap; see CAP_DOWN Thm 1.2 for the even case):
m = ∏ q_i, q_i ≡ 3 (4), (K/q_i) = −1 for all i ⟹ −1 ∈ ⟨primes of K⟩ and −K is a square there: ES_ν^{(y,e)}(n) with e < λ(m). Since νK ≡ n (q_i),
(K/q_i) = (n/q_i)(ν/q_i): for ν = 4 the numerator is invisible ("4 is a square"); for other ν it enters.
**Theorem (window-shape T1; PROVED, Jacobi reciprocity).** Let n = a², a odd, gcd(a, ν) = 1. If 4 | ν, or ν is odd with
ν ≡ 3 (mod 4), or ν is a square, no forced window exists for ν/a².
*Proof.* At n = a², (K/q_i) = (ν/q_i), so forcing needs (ν/m) = (−1)^r (r = number of prime factors, Jacobi). ν square:
(ν/q_i) = 1. ν odd: (m/ν) = (−a²/ν) = (−1)^{(ν−1)/2}, so (ν/m) = (−1)^{(ν−1)/2·(1 + (m−1)/2)}: if m ≡ 3 (4) (r odd) this is
+1 ≠ −1; if m ≡ 1 (4) (r even) it is (−1)^{(ν−1)/2}, which must be +1, i.e. ν ≡ 1 (4). 4 | ν: m ≡ −a² ≡ 3 (mod 4), r odd;
if 8 | ν then m ≡ 7 (8) and (2/m) = 1; so (ν/m) = (ν_odd/m) = +1 by the odd case with m ≡ 3 (4) (and (4/m) = 1). ∎
So window-shape T1 holds for 4 | ν (matching (J)46's "full T1 ⟺ 4 | ν") but ALSO for ν ≡ 3 (mod 4) and square ν, where
ES_ν itself has no T1 (e.g. 3/n is always solvable): the window shape is strictly more T1-rigid than the problem.

## Literature
(J)46 (full T1 ⟺ 4 | ν), SIGN_FIELDS Thm 2.2 ((J)62: T1-clean t-slots ⟺ 4 | ν), Sierpiński's 5/n, Schinzel's ν/n.

## Barrier screen
T1 as computed. B2 for cap 0 as for ν = 4. 8/131 / TES control: for ν = 8 the forced windows at n ≡ 3 (8) need m ≡ 5 (8),
i.e. two factors q₁ ≡ 3, q₂ ≡ 7 (8) with (n/q₁) = 1, (n/q₂) = −1: exist by Dirichlet, so ES_8^{(y,e)}(131) holds at some cap;
cap 0 is again the lottery (8/131's five-slice failure is a cap-0 statement, untouched).

## Cheap numerics
`scripts/s6_numerator_windows.py 24 400 400` (odd a < 400, windows m ≤ 400 with ≤ 2 prime factors): squares with a forced
window: 0 for ν ∈ {3, 4, 7, 8, 9, 11, 12, 15, 16, 19, 20, 23, 24} (as proved); all for ν ≡ 2 (4); most for ν ∈ {5, 13, 17, 21}
(149/158, 133/183, 151/186, 67/113 within the small window range).

## Assessment
PROVED (only-if); existence for ν ≡ 2 (4) and non-square ν ≡ 1 (4) EVIDENCE (Dirichlet should give it). Clean exact
statement of where the self-generated mute set sees T1. Not a route to cap 0.
