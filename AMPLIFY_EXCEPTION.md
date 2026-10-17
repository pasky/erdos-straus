# AMPLIFY_EXCEPTION — O253, Direction 2: amplifying one exception

Status: ES is OPEN. No exceptional integer is known; ES is verified to 10^17 (Salez 2014).
Every statement "p₀ ∈ E ⟹ …" below is an implication from a (presumably false) hypothesis.
Labels as in DISCOVERIES.md. Scripts: `scripts/z25_*`. Memos: `BRAINSTORM/z25_*.md`.

Notation: W(n), S, E, P_E as in the shared core. E(N) := #(E ∩ [1,N]); for a set F, F(N) := #(F ∩ [1,N]).
Known facts used as the "contradiction targets":
* (K1) E ∩ [2, 10^17] = ∅ (published computation; only used as a base case).
* (K2) Mordell: E ⊆ 𝓜 := {n ≡ 1, 121, 169, 289, 361, 529 (mod 840)} (the Mordell identities are polynomial
  identities in n, so they hold for all integers n in the complementary classes, not only primes). Also n ∈ E ⟹
  every prime factor of n is ≡ 1 (mod 4) (a prime factor q ≡ 3 (4) gives q ∈ S, hence n ∈ S).
* (K3) divisor closure: d | n, d ≥ 2, n ∈ E ⟹ d ∈ E (scaling a witness of d).
* (K4) Vaughan 1970 (published): ∃ C₀, c₀ > 0 with E(N) ≤ C₀ N exp(−c₀ (log N)^{2/3}) for all N ≥ 2 (all n, not only
  primes). (K4′) internal (Claude, unpublished, flagged): E(N) ≪ N exp(−c (log N)^{3/4}); and the internal 2/3·loglog
  note E(N) ≪ N exp(−c (log N)^{2/3}(log log N)^{1/3}) (DISCOVERIES (A)6–7).

---------------------------------------------------------------------------------------------------------------

## 1. Deliverable 1 — the "this would suffice" theorems

Throughout, a *law* assigns to each p₀ ∈ P_E a set F(p₀) (or a successor map σ) and asserts F(p₀) ⊆ E.
"Suffices" means: the law together with (K1)–(K4) implies P_E = ∅. "Never suffices (relative to K)" means: there
is a set E′ satisfying (K1)–(K4) [and (K4′)] that is consistent with the conclusion of every law of the given shape —
so no contradiction can be derived from the law and the listed facts alone.

**Theorem 1.1 (counting; PROVED).** Let F ⊆ E (any integers, prime or composite).
(a) If for every c > 0
        limsup_{N→∞} F(N) · exp(c (log N)^{2/3}) / N = ∞,                                   (1.1)
then E ≠ ∅ contradicts (K4); hence any law that produces such an F from every p₀ ∈ P_E proves P_E = ∅ (and E = ∅,
since min E is prime). In particular it suffices that F(N) ≥ N exp(−ψ(N)) for infinitely many N with
ψ(N) = o((log N)^{2/3}) along them. With (K4′) the exponent 2/3 may be replaced by 3/4 (or by
(log N)^{2/3}(log log N)^{1/3}).
(b) (1.1) is exactly what is needed: if (1.1) fails for some c₁ > 0, then F is consistent with (K4) for every
c₀ ≤ c₁ — since c₀ is not specified by the published theorem, no contradiction follows.
(c) Σ_{n∈F} 1/n = ∞ implies (1.1), but not conversely (F(N) = ⌊N exp(−(log N)^{1/2})⌋ satisfies (1.1) and has
Σ 1/n < ∞). So the counting form is strictly stronger than "contradict Σ_{P_E} 1/p < ∞".

*Proof.* (a) If E ≠ ∅ we would have F(N) ≤ E(N) ≤ C₀N exp(−c₀(log N)^{2/3}) for all N, i.e.
F(N) exp(c₀(log N)^{2/3})/N ≤ C₀, contradicting (1.1) at c = c₀. The "in particular": exp(c(log N)^{2/3} − ψ(N)) → ∞
along the sequence. (b) If sup_N F(N) exp(c₁(log N)^{2/3})/N = C₁ < ∞ then F itself satisfies the inequality of
(K4) with (C₁, c₁), and for c₀ ≤ c₁ a fortiori. (c) Partial summation: if F(N) ≤ C N exp(−c(log N)^{2/3}) then
Σ_{n∈F} 1/n = ∫ F(t) dt/t² + O(1) ≤ C ∫ exp(−c (log t)^{2/3}) dt/t = C ∫ exp(−c u^{2/3}) du < ∞; contrapositive. For the
example: ∫ exp(−√u) du < ∞, while exp(c(log N)^{2/3} − (log N)^{1/2}) → ∞ for every c > 0. ∎

**Remark 1.2 (landing criteria; PROVED, trivial but sharp).** A *single* output suffices if it lands in a set known
to be soluble: if every p₀ ∈ P_E yields one n ∈ E with n ≤ 10^17, or n ∉ 𝓜, or n with a prime factor ≢ 1 (4), or
n < p₀ (descent: then min E would not be minimal, using (K3)), then P_E = ∅. Route (D) of the core is exactly the
"n < p₀ in a block" version of this (Thm 1.5).
