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
X_{k+1} = A X_k/(1+δ), J_k = [X_k, (1+δ)X_k]; m₀ = 1, m_{k+1} = max(b, ⌈b m_k/r⌉) (so m_k ≪ (b/r)^k + b); take m_k
primes ≡ 1 (840) in J_k (PNT in progressions: J_k contains ≫ δX_k/log X_k of them, ≫ m_k since
b/r < A/(1+δ)), and join the level-k primes to level k+1 by listing the b·m_k edge slots parent by parent and
assigning them cyclically to the m_{k+1} ≥ b children: a parent's b slots hit distinct children, and each child
receives ≤ ⌈b m_k/m_{k+1}⌉ ≤ r edges. Every child c of p satisfies
p ≤ (1+δ)X_k < X_{k+1} ≤ c ≤ (1+δ)X_{k+1} = A X_k ≤ A p. The count is ≪ N^{β′} + log N with β′ = log(b/r)/log(A/(1+δ)) < 1.
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

---------------------------------------------------------------------------------------------------------------

## 2. Obstruction theorems (what classes of laws can never work)

**Proposition 2.1 (an (A)-law is a total reduction; PROVED, elementary).** A law "p₀ ∈ E ⟹ F(p₀) ⊆ E" with
F(p₀) defined from p₀ alone (input-only) is the same statement as the family of reductions
"ES(q) ⟹ ES(p₀)" for q ∈ F(p₀). Consequently: (a) if some q ∈ F(p₀) is *known* to be soluble, the law (if proved)
is a proof of ES(p₀); (b) if F(p₀) satisfies (1.1), F(p₀) necessarily contains integers covered by the
small-modulus Elsholtz–Tao classes used in Vaughan's sieve (otherwise F(p₀) ⊆ the sieve's avoider set, whose
count is the bound in (K4)), so the law, made explicit, turns an *explicit small-modulus witness* at some q into a
witness at p₀. The amplification route therefore does not avoid proving ES(p₀): it relocates the difficulty into
the reduction step, which must turn small-modulus data at q into a witness at p₀ (cf. Thm 2.3).
*Proof.* (a) Contrapositive of the law at that q. (b) Vaughan's proof bounds E(N) by the number of n ≤ N avoiding an
explicit family of classes (each class ⊆ S by an explicit identity); if F(p₀) avoided all of them it would obey
the same upper bound and (1.1) would fail (Thm 1.1(b)). ∎

**Theorem 2.2 (slice isolation: witness transports never amplify; PROVED).** Call (a,b,c) the *slice* of a witness
and let 𝒢 be the graph on primes with q ~ p iff some witness w ∈ W(q) transports to W(p) by one of the two known
transports (H(w) | q − p keeping the Type, or H(w) | pq − 1 switching it; any finite chain of these).
(a) The transports are symmetric with the slice fixed: W_{abc}^{Type}(q) ≠ ∅ and H | q − p ⟺ W_{abc}^{Type}(p) ≠ ∅
and H | q − p (same for the switched form). Hence exceptional primes are isolated vertices of 𝒢.
(b) Any law proved through such transports with an applicability condition depending on W(q) (e.g. "for all
w ∈ W(q), H(w) | p₀ − q or H(w) | p₀q − 1") has F(p₀) = E ∪ {q ∈ S : …} = E under the hypothesis, i.e. it is the
tautology E ⊆ E. With an input-only F(p₀), proving it means proving that every soluble q ∈ F(p₀) has a witness
whose modulus H(w) divides p₀ − q or p₀q − 1 — a divisor event with modulus part of the solution (B2), and, by
Prop 2.1(a), a proof of ES(p₀) as soon as one q ∈ F(p₀) is known to be soluble.
*Proof.* (a) Type II at q: Hd = q + e; if H | q − p then H | p + e and d′ = (p + e)/H ≥ 1. Type I at q: Hd = qe + 1;
H | q − p gives H | pe + 1. Switched: if H | pq − 1, then p(qe + 1) ≡ e + p and p(q + e) ≡ 1 + pe (mod H), so Type I at
q gives Type II at p and vice versa; d′ is automatically a positive integer. Each implication is reversible (the
conditions are symmetric in p, q), so q has a witness in slice (a,b,c) compatible with p iff p has one compatible
with q. An exceptional p has no witness in any slice, hence no edge. (b) As stated. ∎

**Theorem 2.3 (squares refute primality-blind ET-valued laws; PROVED).** Let 𝓛 be a law (either route) whose proof
produces, from witnesses at the members of F(n) (resp. Q(n)), an Elsholtz–Tao Type I or II witness at n, and which
never uses that n is prime (all steps are identities/congruences valid for every odd n ∈ 𝓜 with the same
definition of F(n), Q(n)). Then 𝓛 is false: for n = m² (m odd) there are no Type I/II witnesses (ET Prop 1.6),
while for small m every member of F(m²) (resp. Q(m²)) is soluble (finite check). Example: Q(n) = prime factors
of (n² − 1)/4, n = 25: Q = {2, 3, 13}, all soluble; n = 25 has no Type I/II witness.
In particular every **congruence-mediated** recombination (the output witness lies in an ET class determined by
the input slices, so the step is a containment of residue classes, valid at every integer of the class) is
refuted by odd squares. Escape requires an essentially *prime* input at p (reciprocity at p, the field 𝔽_p,
irreducibility), or outputs that are not Type I/II at composite n.
*Proof.* A containment of residue classes C ⊆ C_ET holds at all integers of C, including any odd square in C;
odd squares lie in no ET class. ∎

**Theorem 2.4 (no free lunch for route D; PROVED).** For a recombination scheme Q, let
P_free(Q) := {p prime : every q ∈ Q(p) is soluble by a *known* theorem (q ∉ 𝓜, q has a prime factor ≢ 1 (4),
q even (2 ∈ S), q ≤ 10^17)}. On P_free(Q) the recombination law "Q(p) ⊆ S ⟹ p ∈ S" *is* ES(p).
(a) Q(p) = {(p−1)/2, (p+1)/2}: P_free ⊇ {p ≡ 9 (mod 16)} (then (p−1)/2 is even and (p+1)/2 ≡ 5 (8) ∉ 𝓜) —
half of all Mordell-class primes. So this D-law is exactly as hard as ES on p ≡ 9 (16), i.e. on a set of
Mordell-hard primes of relative density 1/2.
(b) Q(p) = prime factors of (p²−1)/4: P_free ⊇ {p : every odd prime factor of (p²−1)/4 is ∉ 𝓜}, a sieve set of
dimension 2·(1/32) (heuristically infinite, ≍ x/(log x)^{1+1/16}); on it the law is ES.
*Proof.* On P_free the hypothesis of the law is a theorem, so the law's conclusion is p ∈ S. (a) p ≡ 1 (8) for
p ∈ 𝓜; p ≡ 9 (16) gives (p+1)/2 ≡ 5 (mod 8), while 𝓜 ⊆ {≡ 1 (8)}. ∎
So a recombination law can be easier than ES only if, for every p, Q(p) contains members whose solubility is not
already known — i.e. the information has to come from witnesses at *hard* q, and Thm 2.4 shows the natural
schemes do not guarantee this.

**Theorem 2.5 (numerator models: exceptions are isolated; CERTIFIED, `scripts/z25_models.py`, `z25_common.py`).**
For k/n = 1/x + 1/y + 1/z the same parametrisation, transports and divisor closure hold with 4 replaced by k, and
genuine prime exceptions exist (k = 8: E_8 ∩ primes < 2000 = {11, 17, 131, 241}; k = 12: 15 primes up to 1873;
counts for 8 ≤ k ≤ 25 in the script log). In these models, computed exactly:
(a) the square law fails: 8/11 has no solution, 8/121 = 1/18 + 1/99 + 1/2178; p² is soluble for every exceptional p < 400 with
8 ≤ k ≤ 14 except (k, p) = (14, 29);
(b) the recombination law fails: e.g. k = 10, p = 61: 10/61 has no solution while every prime factor > k of
(61² − 1)/4 = 930 (namely 31) is soluble; failures for every k ∈ [10, 25] (the primes ≤ k are trivially exceptional
for k ≥ 7, so they are excluded from Q); the {(p−1)/2, (p+1)/2} law fails for every k ∈ [8, 25] except 9 (e.g. 8/131);
(c) exceptions are isolated: for k = 8 the four exceptional primes 3 < p < 2000 have no exceptional successor beyond 241
up to 2000; growth laws of Thm 1.3 type are false in these models.
Consequence: any proof of an amplification or recombination law must use the numerator 4 specifically (the
same point as numerator blindness (J)41); a k-uniform argument is refuted by a finite computation.

---------------------------------------------------------------------------------------------------------------

## 3. Deliverable 2 — construction attempts

### 3.1 Affine-source recombination and its exact gate (route D, idea 4)

Setting: a prime source n′ and p = αn′ + β (α, β small integers; v = (p+1)/2 is α = 2, β = −1; u = (p−1)/2 is
never prime). A source witness w′ with slice (a′,b′,c′), modulus H′ = 4a′b′, e′ = (a′+b′)/c′ pins
n′ ≡ −e′ (Type II) or n′ ≡ −e′^{−1} (Type I) (mod H′), hence pins p modulo αH′, and nothing else.

**Theorem 3.1 (exact gate; PROVED).** Call a *determined lift* any rule that, from w′ alone, chooses a target slice
(a,b,c) and a Type such that the resulting ET witness exists at *every* p ≡ p (mod αH′) (d being the quotient).
(a) A determined lift from w′ exists iff p has an ET witness whose modulus H = 4ab divides αH′.
(b) Hence "W(n′) ≠ ∅ ⟹ W(p) ≠ ∅" is provable by determined lifts iff *every* witness w′ ∈ W(n′) has this property:
for each source witness, the number N_θ(p) = p + e (Type II) or pe + 1 (Type I) must have the divisor 4ab with
4ab | αH′(w′) and (a+b)/c = e — a divisor event whose modulus is part of the (source) solution: the B2 gate.
(c) The fixed-H transports of the core are the special case α = 1, H = H′.
*Proof.* (a) If 4ab | p + e for all p in a class mod αH′, subtracting two members gives 4ab | αH′; if 4ab | pe + 1
for all of them, 4ab | αH′e and gcd(e, 4ab) = 1, so 4ab | αH′. Conversely if p has a witness with H | αH′ the same
slice works on the whole class (d = (p′+e)/H resp. (p′e+1)/H stays a positive integer). (b) Totality must hold
whatever witness the source happens to have. ∎

**Fixture test (CERTIFIED, `scripts/z25_gate.py fixtures`; entries "source(×α): passing/all source witnesses").**
No source is total at any fixture; at 3361 the source 281 (3361 = 12·281 − 11) passes **0 of 17** witnesses.
```
97 89(x1):5/10 101(x1):9/16 103(x1):14/27 107(x1):8/25 109(x1):9/15 43(x2):3/14 47(x2):10/34 53(x2):8/13 29(x3):3/7 31(x3):6/19 23(x4):4/21 17(x6):2/4 11(x8):2/9 13(x8):1/4
193 181(x1):4/17 191(x1):15/67 197(x1):14/23 199(x1):31/42 97(x2):5/8 101(x2):6/16 61(x3):1/11 67(x3):2/17 47(x4):5/34 31(x6):3/19 23(x8):4/21 17(x12):2/4
313 307(x1):12/40 311(x1):20/79 317(x1):14/34 151(x2):9/31 157(x2):11/24 101(x3):4/16 103(x3):6/27 107(x3):8/25 79(x4):20/37 53(x6):8/13
3361 3359(x1):25/423 3371(x1):9/77 3373(x1):7/66 1117(x3):9/64 1123(x3):10/48 839(x4):15/194 419(x8):5/81 421(x8):1/16 281(x12):0/17
5209 5197(x1):9/104 2609(x2):10/40 1733(x3):8/59 1301(x4):7/38 1303(x4):10/53
233689 116849(x2):34/167 77893(x3):27/197 77899(x3):85/225
```

**Theorem 3.2 (the T1 adversary: invisible witnesses; PROVED).** Let p be odd and L ≥ 1. If p is congruent to a
square modulo L (for odd p this is automatically an *odd* square when 2 | L; for odd L replace m by m + L), then
*no* ET witness at p has modulus H dividing L. Consequently a source witness w′ with p ≡ □ (mod αH′(w′)) is
*invisible*: no determined lift (Thm 3.1) can use it, and the recombination law from that source is not
provable by determined lifts. For p ∈ 𝓜 prime (p ≡ 1 (8), (p/3) = (p/5) = (p/7) = 1) every source witness whose
αH′ is supported on {2, 3, 5, 7} ∪ {ℓ : (p/ℓ) = 1} is invisible; e.g. every source n′ ≡ 3 (4) has the invisible
witness H′ = 4 (Type II, a = b = 1, e = 1).
*Proof.* Let m be odd with m² ≡ p (mod L). If p had a witness with H | L, the same slice would give an ET witness
at every n ≡ p (mod H) (Thm 3.1(a)), in particular at n = m², contradicting ET Prop 1.6 (odd squares have no
Type I/II solutions). ∎

**Corollary 3.3 (joint recombination; PROVED).** Combining several sources (any finite Q(p), any number of shifts,
all witnesses jointly) pins p modulo L = lcm(α_iH′_i). Since "p ≡ □ (mod L)" is a local condition at each prime
power of L, the lcm of invisible moduli is invisible. Hence a joint determined recombination over Q(p) is total
**only if some single source in Q(p) has no invisible witness at all.** Disjunction over many shifts does not help.

**Numerics (CERTIFIED, `scripts/z25_sqadv.py`, `z25_joint_run.py`).** (i) Consistency of the lemma: for every
fixture p ≤ 5209, none of p's own ET moduli H has p ≡ □ (mod H). (ii) Every source (all primes (p + j)/g,
|j| ≤ 12, g | 24) at every fixture ≤ 5209 has ≥ 2 invisible witnesses (e.g. 3361 ← 281 (×12): 11 of 17 invisible;
97 ← 43 (×2): 11 of 14). (iii) The joint search finds an adversarial tuple at every fixture ≤ 5209 (all 5–14
sources at once; e.g. at 97 with 14 sources the lcm of the chosen moduli is 2^7·3^2, and 97 ≡ 1 (mod 8), 97 ≡ 7² (mod 9)).
So route (D) through congruence-mediated recombination is dead at every fixture, for every witness choice
pattern, for the exact reason T1: the adversary feeds witnesses whose moduli only see residues of p that are
squares. A route-(D) law must use an input that sees a *non-residue* prime of p, and no such input is forced by
"q ∈ S".
