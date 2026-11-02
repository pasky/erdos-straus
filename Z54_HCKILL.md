# Z54_HCKILL — kill side of the HC hierarchy: HC(p) > X infinitely often without Dickson

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane: HCKILL (wave z54, gap 3, kill side). Scripts `scripts/z54_hckill_*`, data `data/z54/hckill/`.

*Checkpoint 1 skeleton — sections marked (TODO) are being filled.*

## 0. Statements attacked

Notation. For p ≡ 1 (mod 8), 𝒞 = {x ≥ 4 : 4 | x or x ≡ 7 (mod 8)} = {4, 7, 8, 12, 15, 16, 20, 23, 24, …}; line x
*fires* if N_x^e = p + x or N_x^l = xp + 1 has a divisor ≡ −1 (mod x); HC(p) = least firing x
(LOWERTAIL_ROUND2_FABLE §3.1, Z53_HCSHIFTS §1). S = {n ≥ 1 : every prime factor of n is ≡ 1 (mod 4)}.

* **K(X)** (kill at window X). There are infinitely many primes p ≡ 1 (mod 8) with HC(p) > X.
  Known: K(X) for every fixed X, CONDITIONAL on Dickson (FABLE Prop 3.3(a)); for growing X ≍ log p/log log p,
  CONDITIONAL on a non-standard uniform Bateman–Horn bound (HCSHIFTS Prop W2). Unconditionally: nothing.
* **K(4) ⟺ P(4,15)** (exact, §1): there are infinitely many primes p ≡ 1 (mod 8) with p + 4 ∈ S and 4p + 1 ∈ S.
  (Since the next element of 𝒞 is 7, K(4) = K(5) = K(6).)

## 0.1 Why this is not already closed

The only kill mechanism on record is FABLE Prop 3.3 / HCSHIFTS Thm W: make every window integer "constant × prime"
(Dickson), which Thm W shows hits a wall at X ≍ log p for fixed families. Thm W's scope remark explicitly leaves open
**subgroup confinement** (HCSHIFTS Lemma C(a)): a line does not fire if all prime factors of its integer lie in a
subgroup H ∌ −1 of (ℤ/x)^×. This lane attacks K(X) through confinement: (i) algebraically (norm-form identities, which
need no primality of window integers at all), and (ii) analytically (sieve), and asks which steps are sieve-tractable.

## 0.2 First lemma (checkpoint 1)

**Theorem Q (PROVED, elementary).** Let m ≡ 0 (mod 4) and suppose p = 5m² + 1 is prime. Then p ≡ 1 (mod 8) and
HC(p) ≥ 7, i.e. line 4 does not fire. Hence K(4) holds CONDITIONAL on the Bunyakovsky conjecture for the single
polynomial f(k) = 720k² + 1 (every prime 5m² + 1 with 4 | m has 3 | m, so p = f(m/12)).

*Proof.* p + 4 = 5(m² + 1) and 4p + 1 = 5((2m)² + 1). For m even, m² + 1 and (2m)² + 1 are odd and are sums of two
coprime squares, so every prime factor ℓ of them has −1 ≡ (square) (mod ℓ), i.e. ℓ ≡ 1 (mod 4); also 5 ≡ 1 (mod 4).
So p + 4, 4p + 1 ∈ S, every divisor of them is ≡ 1 (mod 4), and none is ≡ −1 (mod 4): line 4 does not fire. 4 | m gives
5m² ≡ 0 (mod 16), so p ≡ 1 (mod 8). If 3 ∤ m then 5m² + 1 ≡ 2·1 + 1 ≡ 0 (mod 3), so a prime p > 3 forces 3 | m, i.e.
12 | m. f(k) = 720k² + 1 is irreducible with f(0) = 1, so it has no fixed prime divisor and Bunyakovsky applies. ∎

CERTIFIED (`data/z54/hckill/fam_5m2p1_hc_1e12.txt`, engine `scripts/z53_hcshifts_hc.c list 128 4096`): all 5 719 primes
p = 80s² + 1 ≤ 10¹² have HC(p) ≥ 7; HC distribution 7: 5117, 8: 481, 12: 94, 15: 21, 16: 1, 20: 4, 23: 1. The share
HC = 7 (89.5 %) matches the generic share P(HC = 7 | HC > 4) = 111 635/125 059 = 89.3 % of the z49 census to 10⁸.

(TODO: §1 exact reductions; §2 the algebraic (quadratic-family) mechanism and its wall; §3 sieve analysis — which
steps are sieve-tractable, exact level deficits; §4 literature; §5 numerics with controls; §6 screens; §7 FRONTIER text.)
