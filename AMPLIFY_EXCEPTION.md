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

**Theorem 1.3 (iterated / branching laws; PROVED).** Let σ assign to each p ∈ P_E a set σ(p) ⊆ E of *distinct*
successors, T(p₀) the forward closure (law applied again to every output; for a composite output apply it to its
prime factors, which lie in P_E by (K3)). In-degree r: every q lies in σ(p) for at most r values p ∈ T(p₀).
(a) *Super-linear scale, bounded branching ⟹ polylog, never suffices.* If |σ(p)| ≤ b and every q ∈ σ(p) has
q ≥ p^{λ₁}, λ₁ > 1, then T(N) ≤ 2 (log N/log p₀)^{log b/log λ₁}. If moreover all outputs are primes of 𝓜 (otherwise
Remark 1.2 already applies), E′ := T(p₀) satisfies (K1)–(K4′) and is σ-closed; so no such law, of any (b, λ₁),
can yield a contradiction with the listed facts.
(b) *Linear scale: the exact threshold b ≥ rA.* Suppose every p ∈ T has ≥ b successors in (p, A p] (A > 1 fixed)
and in-degree ≤ r. Then T(N) ≥ (r/b)(N/p₀)^{β}, β = log(b/r)/log A. If b/r ≥ A then T(N) ≫ N/p₀, contradicting (K4)
(indeed density 0): the law suffices. If b/r < A, there is a σ-closed configuration of primes of 𝓜 above 10^17 with
exactly these out/in-degree constraints and T(N) ≍ N^{β′}, β′ < 1, consistent with (K1)–(K4′): never suffices.
(c) *Additive gaps.* If every p ∈ P_E has a successor in (p, p + f(p)], f nondecreasing, then the chain
p₀ < p₁ < … gives T(N) ≥ (N − p₀)/f(N) − 1. Hence the law suffices if for every c > 0,
liminf_N f(N) exp(−c (log N)^{2/3}) = 0 (e.g. f(p) = exp(o((log p)^{2/3})), or exp(o((log p)^{3/4})) with (K4′)).
If f(N) ≥ C exp(c₁(log N)^{2/3}), the guaranteed count N/f(N) does not violate (K4) (for c₀ ≤ c₁) — no counting
contradiction. (A σ-closed *prime* model with these gaps needs primes ≡ 1 (840) in intervals of length f(p);
unconditionally available for f(p) ≥ p^{7/12+ε} (Huxley-type zero density for L(s,χ) mod 840; cited from memory).)
(d) *What replaces bounded branching.* Combining (a)–(c): a law suffices only if, from the forced structure, F is
dense *at the scale of its own outputs* — ≥ A·r new exceptions per factor A of growth, or a forced exception in
every window of length exp(o((log p)^{2/3})). Any law with fixed b and output scale ≥ p^{1+ε} is polylog.

*Proof.* (a) Every element of generation k (k applications) is ≥ p₀^{λ₁^k}; elements ≤ N need
k ≤ K := log(log N/log p₀)/log λ₁, and generation k has ≤ b^k elements; Σ_{k≤K} b^k ≤ 2b^K. (K1): outputs > p₀ >
10^17; (K2): primes of 𝓜 (all ≡ 1 (4)); (K3): primes; (K4′): polylog ≪ N exp(−c(log N)^{3/4}). (b) Let T_k be the
set of elements reachable in exactly k steps; T_k ⊆ (p₀, A^k p₀]. Edges leaving T_k number ≥ b|T_k| and land in
T_{k+1}; each element receives ≤ r edges, so |T_{k+1}| ≥ (b/r)|T_k| and T(A^k p₀) ≥ (b/r)^k. For b/r ≥ A, T(N) ≥
(r/b) N/p₀ while (K4) gives E(N) = o(N). Model for b/r < A: pick δ > 0 with b/r < A/(1+δ)², put X₀ = p₀,
X_{k+1} = A X_k/(1+δ), J_k = [X_k, (1+δ)X_k]; take m_k := ⌈(b/r)^k⌉·r ≥ b-many-compatible primes ≡ 1 (840) in J_k
(PNT in progressions: J_k contains ≫ δX_k/log X_k of them, ≫ m_k since (b/r)^k ≤ (X_k/p₀)^{β″}, β″ < 1), and join each
level-k prime to b level-(k+1) primes in round-robin so that in-degrees are ≤ r. Every child c of p satisfies
p ≤ (1+δ)X_k < X_{k+1} ≤ c ≤ (1+δ)X_{k+1} = A X_k ≤ A p. The count is ≍ N^{β′} with β′ = log(b/r)/log(A/(1+δ)) < 1.
(c) p_{i+1} − p_i ≤ f(p_i) ≤ f(N) while p_i ≤ N. ∎

**Theorem 1.4 (composite outputs; PROVED).** (a) (K4) bounds *all* exceptional integers, so composite outputs count
in Thm 1.1 at full weight; no conversion is needed. (b) Composite → prime conversion is lossy by a logarithm: if
R ⊆ E has R(N) elements ≤ N, then P_E ∩ [1, N] has ≥ log R(N)/log(1 + log₂N) elements (an integer ≤ N supported
on s given primes is determined by ≤ s exponents ≤ log₂N). Sharp: R = {p₀^k} has R(N) ≍ log N and one prime.
(c) From a single seed, a composite output n ∈ E either is a power of p₀ (≤ log N/log p₀ of them up to N) or forces a
*new* exceptional prime (a prime factor ≠ p₀, by (K3)). So every composite-output law of growth beyond log N is in
fact a prime-amplification law (via the prime-factor map), and must be judged by Thm 1.3 on primes, with the
log-loss of (b) when only composites are forced. (d) The converse closure fails: P_E-smooth integers need not lie
in E, so a law cannot be iterated through products (p, q ∈ P_E ⇏ pq ∈ E); a law applied to a composite n ∈ E may use
only "every prime factor of n is in P_E", which is weaker than n ∈ E.

**Theorem 1.5 (disjunctive / block laws; PROVED).** Suppose every p₀ ∈ P_E yields a family 𝔅(p₀) of blocks with
B ∩ E ≠ ∅ for every B ∈ 𝔅(p₀).
(a) E(N) ≥ τ_N := the least size of a set hitting every block B ⊆ [1, N], and τ_N ≥ #{B ⊆ [1,N]}/μ_N, where μ_N is
the maximal number of such blocks containing one integer. Thm 1.1 applies to τ_N; Thm 1.3 applies with "successor"
replaced by "hit of a block" (the hit is an unknown element of E, so the law must be available at *every* element
of E, which it is if stated for all p₀ ∈ P_E, using (K3) for composite hits).
(b) (Route D.) If every p ∈ P_E has a block Q(p) ⊆ [2, p) with Q(p) ∩ E ≠ ∅, then P_E = ∅ (least element of E is
prime, by (K3); its block contains a smaller element of E). This needs neither (K1) nor (K4).
(c) Disjoint blocks of bounded length L inside every window (p, p + f(p)] give Thm 1.3(c) with f + L.
*Proof.* (a) E ∩ [1,N] hits every block inside [1,N]; a hitting set of size τ hits ≤ τμ_N blocks. (b),(c) immediate. ∎
