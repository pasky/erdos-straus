# BRAINSTORM — Farey neighbours, Ford circles and continued fractions for Type I (O144, angle a)

Labels as in DISCOVERIES.md. ET coordinates: Type I ⟺ `4abd − pe = 1`, `a + b = ce` (a ≤ b, gcd(a,b,c) = 1).

## 1. Idea and exact dictionary

**Lemma A.1 (PROVED, elementary).** Put N = 4ad. Type I solutions of a prime p correspond bijectively to triples
(N, a, e) with
`4 | N`, `a | N/4`, `e | aN + 1`, `N | pe + 1`, `a ≤ b := (pe+1)/N`, gcd condition,
and then `c = (a+b)/e = (p + (aN+1)/e)/N`.

The **Farey form:** `Nb − pe = 1` says that e/N < b/p are Farey neighbours, so their Ford circles are tangent.
If moreover N < p and b < p, then e/N is the left parent of b/p in F_p, and (b−e)/(p−N) is the right parent.
So in this range:
> Type I(p) ⟺ some Ford circle C(b/p) of denominator p has a left parent e/N such that 4 | N and e | aN + 1
> for some a | N/4.

*Proof.* From `4abd = pe + 1` and `a + b = ce` we get `e(cN − p) = aN + 1`, so e | aN + 1 and
`c = (p + (aN+1)/e)/N`. Conversely, given (N, a, e), the equation `aN + pe + 1 = ceN` holds as soon as
`N | pe + 1`. Note `N ≤ 2p + 2` (from e ≤ a + b ≤ 2b). ∎
Checked: `scripts/bs_farey_dict.py` reproduces f_I(p) exactly for all 1005 primes 5 ≤ p ≤ 8000 (zero
mismatches against `spec_typecount`).

**Continued-fraction form.** For fixed N the minimal e is `e₀ ≡ −p⁻¹ (mod N)`. Up to the parity convention, this is
the denominator of the penultimate convergent of p/N (a continuant of its CF). Every admissible e is
`e₀ + kN`. So Type I(p) says: "for some N ≡ 0 (mod 4), a translate of the penultimate-convergent denominator of
p/N divides aN + 1 for a divisor a of N/4".

**Level-d (brief's) form.** Write f = 4acd − p (Lemma 2.1 of POINTWISE_SPECTRAL). Then
`[[e, 2a], [2ad, f]] ∈ SL₂(ℤ)`, i.e. C(e/2ad) and C(2a/f) are tangent Ford circles, with the condition
`4ad | f + p`. These are the integral points of `X_d : ef − 4da² = 1` with a congruence modulo a coordinate. This is
exactly the Q_d / X_d object of DISCOVERIES (I)1, (I)7.

What would have to be true for a CF mechanism to prove ES: some theorem forcing, for every p, a CF word whose
continuants (N, e) satisfy the multiplicative event `e | aN + 1` with a | N/4. Zaremba-type theorems control the
*sizes* of the partial quotients, not divisibility among continuants.

## 2. Literature anchor

* Zaremba's conjecture (1971): every q is the denominator of some b/q with all partial quotients ≤ A (A = 5).
  It is open for general q. Bourgain–Kontorovich, Ann. of Math. 180 (2014) 137–196, prove it for almost all q
  (A = 50, density one; title and abstract verified online). Huang, GAFA 2015 (arXiv:1310.3772, verified
  title/abstract) gets A = 5, density one. Both are thin-semigroup circle-method results (orbits of
  ⟨[[0,1],[1,a]] : a ≤ A⟩).
* From memory, unverified: Niederreiter settled powers of 2, 3, 5. For prime q only partial-quotient bounds of
  order log q / log log q (Korobov, Moshchevitin–Shkredov-type) are known.

## 3. Barrier screen

* **B2 (divisor-class reduction).** Fix N (or (a, N)). The condition is "the integer aN + 1 has a divisor in the
  class −p⁻¹ (mod N)". That is a one-integer slice of redteam-2 Lemma 2.1, with θ = (a, d). The Farey/Ford
  language relabels the slices; it does not merge them. The Ford-circle picture adds geometry (tangency) that is
  automatic: tangency is det = 1, which is the equation itself.
* **B1.** For fixed N the condition depends only on p mod N: e₀ = −p⁻¹ mod N, and the CF of p/N is a function
  of p mod N once the integer part is removed. So any CF statement about finitely many N is a congruence
  covering (Thm M/C), and it fails at square-mimicking primes.
* **B5 / T1.** At n = m² the step "e | aN + 1 with e ≡ −n⁻¹ (mod N)" has no solution, by ET 1.6. That is
  genus: every prime divisor of aN + 1 = (2a)²d + 1 has (−d/e) = 1. ET's proof of Prop 1.6 turns this, together
  with e ≡ −m⁻² (mod 4ad), into a reciprocity contradiction. A CF theorem applies equally to n = m² (the Farey
  structure of m²/N has nothing special). So the step that must fail at odd squares is precisely the divisor
  event, never any CF/Zaremba input.
* **B6 / H-F (Zaremba).** BK and Huang are "almost all q" statements. Even a Zaremba theorem for every prime p,
  which is open, would give one b with bounded quotients. Its parents (e, N) have no reason to satisfy
  e | aN + 1. Heuristic: e is spread over [1, N], so the chance is ≍ τ(N)/N·log N per N. The bounded-type
  condition keeps only ≍ p^{2δ_A − 1} of the p − 1 fractions b/p, on average over p (Hensley; δ_A is the
  Hausdorff dimension of A-bounded type). It only *thins* the family, so the expected count drops by a factor
  p^{2δ_A − 2} relative to the L³ total, the opposite of what is needed (B3).
* **B4.** Nothing new: small e are small-modulus coverings (e = 1 is p ≡ 3 (4); e = 3 is the classical mod-3
  slice).
* **T7.** Kloosterman equidistribution of (N, N̄/p) (Weil) controls e₀(N) only on boxes of side ≥ p^{1/2+ε}. The
  divisor event lives at scale O(1) in e mod (aN+1). So it is an average leak.

## 4. Experiments (`scripts/bs_farey_dict.py`)

| primes | f_I mismatch | primes with no solution in the F_{p−1} range (N < p, b < p) | mean share of solutions in that range | primes with no a = 1 solution |
|---|---|---|---|---|
| 5 ≤ p ≤ 8000 (1005) | 0 | {5, 17, 41, 241} | 0.43 | 0 |

So the "pure Ford-circle-of-denominator-p" form (N < p, b < p) is not equivalent to Type I. It misses 5, 17, 41
and 241 in this range. EVIDENCE that it misses no other prime ≤ 8000; no claim beyond. The full form needs
N up to 2p + 2.

## 5. Viability Assessment

**COLLAPSES to B2 (and B1 for finitely many N) at the step "e | aN + 1".** The Farey/Ford/CF language is an exact
relabelling of the e-slices / Q_d points. Zaremba/BK inputs are almost-all (B6). Even pointwise they control
sizes of partial quotients, which the divisor event does not see, and they shrink the main term (B3).

By-product: Lemma A.1 (PROVED, elementary; novelty low, a restatement of ET Prop 2.2). The "Ford circle of
denominator p" form covers all primes 8000 > p ∉ {5, 17, 41, 241} (EVIDENCE).
