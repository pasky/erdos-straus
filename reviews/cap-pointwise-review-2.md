# R239 — hostile review #2 of O236 (CAP_POINTWISE.md), round 1

Reviewer: R239 (independent; no edits to author's files in round 1). Scripts: `scripts/review_r239_*.py`.
Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim-by-claim

### C1. Definition check / "mute-set loophole" (brief item 1) — SOUND (no loophole)
EXPONENT_CAP Def 1.1 ((J)34) contains **no mute set at all**: ES^{(y,e)}(n) asks for 4/n = 1/x+1/y+1/z, x,y ∈ ℤ_{>0},
z ∈ ℚ_{>0}, and every ℓ with v_ℓ(z) < 0 must satisfy ℓ ∤ 2n, ℓ | y, v_ℓ(z) even, v_ℓ(z) ≥ −2e. The allowed denominator
primes are solution-dependent *by definition* (FROBENIUS_FIRING Def 4.1 says so explicitly: "the allowed denominators
depend on the solution"). So "S := primes of x" is not a definitional choice the author makes; it is a construction device.
Moreover I re-derived that it is FORCED: if ℓ | den z and ℓ | y then from 1/z = (4xy − nx − ny)/(nxy) one gets
ℓ | 4xy − nx − ny ⇒ ℓ | nx ⇒ ℓ | x (ℓ ∤ n). **Every** ES^{(y,e)} solution has its denominator primes inside
gcd(x, y); so "mute primes = primes of x" is the general shape, not a loophole. Hence the statement e*(n) < q is
exactly the statement about the object defined in (J)34, neither trivialised nor strengthened.
Meaningfulness (Assessment): ES^{(y,e)} with e ≍ n^{O(1)} (or (log n)² under GRH) is a weak relaxation of ES; the
author says so (§5 last line). No overclaim found.

### C2. Thm 1.1 (prime window) — SOUND
Re-derived line by line:
* q + n ≡ 4 (mod 8) ⇒ K odd, q ≡ 3 (mod 4) (n ≡ 1 (4)). gcd(K, qn) = 1 as written. ✓
* (−K/q) = (−n/q) (as 4K ≡ n, 4 a square) = (−1/q)(n/q) = −(q/n) = +1 (Jacobi reciprocity, n ≡ 1 (4), n > 0). So
  (K/q) = −1, some s₀ | K is a non-residue; F_q^* cyclic of order 2u, u odd; ord(s₀) even ⇒ −1 = s₀^{ord/2} ∈ H. ✓
* −K ∈ H is a square ⇒ its order o | u odd ⇒ (−K)^{(o+1)/2} ∈ H is a square root of −K. ✓ Reduce exponents mod ord_q(s)
  ⇒ 0 ≤ a_s ≤ ord_q(s) − 1 ≤ q − 2. ✓
* Direct identity check (mine): 1/K + 4/(n(g+1)) + 4Q²/(nK(g+1)) = 4/n ⟺ n(g+1) + 4Q² = 4Kg ⟺ n + 4Q² = qg. ✓
  (holds for ANY Q with q | n + 4Q²).
* g ≡ 3 (4) (n + 4Q² ≡ 1, q ≡ 3); s | K ⇒ q ≡ −n (s) ⇒ gq ≡ n ⇒ g ≡ −1 (s). ✓ So v_s(g+1) ≥ 1 for every s | Q,
  and Prop 1.2's criterion with e = max a_s − 1 holds. e ≤ q − 3. ✓
* Q odd, gcd(Q, n) = 1, den z = Q₁² odd, coprime to n, rad Q₁ | rad Q | K... and | (g+1)/4 | y. ✓
Numerically confirmed from scratch (C8 below).
Small slack (not a defect): a_s ≤ ord_q(s) − 1 and in fact a_s ≤ ord_q(s²)·… one can take a_s < ord_q(s); with
b_s = v_s(K) ≥ 1 the true cap is ≤ q − 3 (Lemma 3.1). Fine.
