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
so no contradiction can be derived from the law and the listed facts alone. (R266 repair: two strengths occur. *Per-law*:
for the given law σ a model E′ exists (Thm 1.3(a), E′ = T(p₀)). *Shape-level*: some law with the stated
properties has a model (Thm 1.3(b) model, Thm 1.3(d)); this shows only that the stated properties do not force
a contradiction.)

*Prior art (R266 repair).* Thm 1.3(a) is test 3 and Thm 1.4(d) is test 1 of Astra's POSITIVE_ES_RESEARCH_RESET.md
§4 (d7300f8); its test 2 (a Rankin bound: the multiplicative semigroup of a sparse prime set is still sparse)
complements Thm 1.4(b),(c), and its "sharper first target" Σ_{P_E}1/p = ∞ is the criterion Thm 1.1(c) improves.
The all-witness transport hypothesis and the remark that a known-soluble factor makes the lift a proof of W(p) ≠ ∅
(Thm 2.2(b), Prop 2.1(a)) are in Astra EXCEPTION_PROPAGATION_GLOBAL.md §1, §8. Astra's
EXCEPTION_PROPAGATION_OPERATIONS.md §5–6 repairs every witness at 97 (and 157 → 313) by target-dependent positive
recombination; those lifts use the known targets at p, so they are not determined lifts and do not contradict
§3.1. Thm 3.2 is classical in substance (see there).

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
**prime** successors, T(p₀) the forward closure (law applied again to every output). In-degree r: every q lies in
σ(p) for at most r values p ∈ T(p₀). (Scope repair after review: the size hypotheses below are on *prime*
successors. A composite output n ≥ p^{μ} may have small prime factors — σ(p_i) = {p_i² p_{i+1}} has superlinear
outputs yet reaches every p_i — so a composite-output law must first be rewritten as a prime law, via Thm 1.4(c),
with the size hypotheses re-verified for the extracted prime factors.)
(a) *Super-linear scale, bounded branching ⟹ polylog, never suffices* (core v1.1 (ii): successors ≥ p^{μ}). If
|σ(p)| ≤ b and every q ∈ σ(p) has q ≥ p^{μ}, μ > 1, then T(N) ≤ (K+1)·max(b,1)^K + 1 with
K = log(log N/log p₀)/log μ; i.e. T(N) ≪ (log N)^{log b/log μ}·log log N for b ≥ 2 and ≪ log log N for b = 1. If moreover all outputs are primes of 𝓜 (otherwise
Remark 1.2 already applies), E′ := T(p₀) satisfies (K1)–(K4′) and is σ-closed; so no such law, of any (b, μ),
can yield a contradiction with the listed facts.
(b) *Linear scale: the exact threshold b ≥ rA.* Suppose every p ∈ T has ≥ b successors in (p, A p] (A > 1 fixed)
and in-degree ≤ r, with b > r. Then T(A^k p₀) ≥ (b/r)^k for all k ≥ 0, i.e. T(N) ≥ (r/b)(N/p₀)^{β} for N ≥ p₀,
β = log(b/r)/log A. (For b ≤ r nothing beyond T(N) ≥ #{k : A^k p₀ ≤ N}-type chain bounds is forced.) If b/r ≥ A then T(N) ≫ N/p₀, contradicting (K4)
(indeed density 0): the law suffices. If b/r < A, there is a σ-closed configuration of primes of 𝓜 above 10^17 with
exactly these out/in-degree constraints and T(N) ≪ N^{β′} + log N, β′ < 1, consistent with (K1)–(K4′): never
suffices (for b ≤ r the model has bounded level sizes and T(N) ≍ log N).
(c) *Additive gaps.* If every p ∈ P_E has a successor in (p, p + f(p)], f nondecreasing, then the chain
p₀ < p₁ < … gives T(N) ≥ (N − p₀)/f(N) − 1. Hence the law suffices if for every c > 0,
liminf_N f(N) exp(−c (log N)^{2/3}) = 0 (e.g. f(p) = exp(o((log p)^{2/3})), or exp(o((log p)^{3/4})) with (K4′)).
If f(N) ≥ C exp(c₁(log N)^{2/3}), the guaranteed count N/f(N) does not violate (K4) (for c₀ ≤ c₁) — no counting
contradiction. (A σ-closed *prime* model with these gaps needs primes ≡ 1 (840) in intervals of length f(p);
unconditionally available for f(p) ≥ p^{7/12+ε} (Huxley-type zero density for L(s,χ) mod 840; cited from memory).)
(d) *Growing branching at super-linear scale (core v1.1 (ii)).* If every successor of p is ≥ p^{μ} (μ > 1) and
|σ(p)| ≤ p^{δ}, then T(N) ≤ (K+2)·N^{δ/(μ−1)} (K as in (a)). Hence such a law can contradict (K4) only if
δ ≥ μ − 1, i.e. the branching must be at least a fixed power p^{μ−1−o(1)} of the parent. Conversely one step suffices if p has ≥ r·p^{λ} e^{−o((log p)^{2/3})}
prime successors in (p, p^{λ}] (in-degree ≤ r): F is then dense at scale p^{λ}. Between δ = μ − 1 and these
dense laws the outcome depends on how the successors are distributed (not settled here).
(e) *What replaces bounded branching.* Combining (a)–(d): a law suffices only if, from the forced structure, F is
dense *at the scale of its own outputs* — ≥ A·r new exceptions per factor A of growth (slowly growing successors,
μ → 1), a forced exception in every window of length exp(o((log p)^{2/3})), or power branching p^{≥ μ−1} at
scale p^{μ}. Any law with fixed b and successors ≥ p^{μ}, μ > 1, is polylog.

*Proof.* (a) Every element of generation k (k applications) is ≥ p₀^{μ^k}; elements ≤ N need
μ^k ≤ log N/log p₀, i.e. k ≤ K, and generation k has ≤ b^k elements;
Σ_{k≤K} b^k ≤ (K+1)max(b,1)^K. [(d): every q ≤ N in T other than p₀ has a parent ≤ q^{1/μ} ≤ N^{1/μ}, so
T(N) ≤ 1 + T(N^{1/μ})·N^{δ/μ}; unrolling until the argument drops below p₀ (≤ K+1 times) gives T(N) ≤ (K+2) N^{δ(1/μ + 1/μ² + …)} ≤
(K+2)N^{δ/(μ−1)}.] (K1): outputs > p₀ >
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
on s given primes is determined by ≤ s exponents ≤ log₂N). Sharp: R = {p₀^k} has R(N) ≍ log N and one prime (as a
statement about the inequality; p₀^k ∈ E is not known — R266 repair).
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
of E, which it is if stated for all p₀ ∈ P_E, using (K3) for composite hits). Caveat (review): when a hit is
composite, the law is re-applied to its prime factors, whose sizes need not satisfy the size/degree hypotheses of
Thm 1.3; those hypotheses must be verified for the extracted primes, not for the hit.
(b) (Route D.) If every p ∈ P_E has a block Q(p) ⊆ [2, p) with Q(p) ∩ E ≠ ∅, then P_E = ∅ (least element of E is
prime, by (K3); its block contains a smaller element of E). This needs neither (K1) nor (K4).
(c) Disjoint blocks of bounded length L, consisting of primes (R266 repair: a composite hit has prime factors far
below p, so the chain would not continue), inside every window (p, p + f(p)] give Thm 1.3(c) with f + L.
*Proof.* (a) E ∩ [1,N] hits every block inside [1,N]; a hitting set of size τ hits ≤ τμ_N blocks. (b),(c) immediate. ∎

---------------------------------------------------------------------------------------------------------------

## 2. Obstruction theorems (what classes of laws can never work)

**Proposition 2.1 (an (A)-law is a total reduction; (a) PROVED, elementary; (b) Assessment).** A law "p₀ ∈ E ⟹ F(p₀) ⊆ E" with
F(p₀) defined from p₀ alone (input-only) is the same statement as the family of reductions
"ES(q) ⟹ ES(p₀)" for q ∈ F(p₀). Consequently: (a) if some q ∈ F(p₀) is *known* to be soluble, the law (if proved)
is a proof of ES(p₀); (b) if F(p₀) satisfies (1.1), F(p₀) necessarily contains integers covered by the
small-modulus Elsholtz–Tao classes used in Vaughan's sieve (otherwise F(p₀) ⊆ the sieve's avoider set, whose
count is the bound in (K4)), so the law, made explicit, turns an *explicit small-modulus witness* at some q into a
witness at p₀. The amplification route therefore does not avoid proving ES(p₀): it relocates the difficulty into
the reduction step, which must turn small-modulus data at q into a witness at p₀ (cf. Thm 2.3).
*Proof.* (a) Contrapositive of the law at that q. (b) is an Assessment, not a theorem: it presupposes that the
bound (K4) is proved as an upper bound for the avoider set of an explicit family of soluble classes, so that any F
obeying (1.1) must meet that family. This is the structure of Vaughan's large-sieve argument as we recall it
(cited from memory, not re-verified here); with that structure the argument is: if F(p₀) avoided all the classes it
would obey the same upper bound and (1.1) would fail (Thm 1.1(b)). ∎

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

**Theorem 2.3 (squares refute primality-blind ET-valued proofs; PROVED, scope as stated).** Let 𝓛 be a law
(either route) together with a *proof* that, from witnesses at the members of F(n) (resp. Q(n)), produces an
Elsholtz–Tao Type I or II witness at n (in ET's sense: n divides exactly the prescribed denominators and is
coprime to the others), using no property of n beyond those shared by a specific odd square n = m² in the law's
stated domain. If every member of F(m²) (resp. Q(m²)) is verified soluble, the proof is invalid, because m² has
no ET Type I/II witness (ET Prop 1.6). Example (route D, domain 𝓜): Q(n) = prime factors of (n² − 1)/4,
n = 121 = 11² ≡ 121 (mod 840) ∈ 𝓜: Q(121) = {2, 3, 5, 61}, all soluble, while 121 has no Type I/II witness. So a
valid proof of this recombination law must use primality of p (or produce non-ET solutions at composites).
The *congruence-mediated* case is made quantitative in Thm 3.2: such a step fails exactly when the class of p
modulo the input moduli contains an odd square — which, for p ∈ 𝓜, is the typical situation.
*Proof.* Apply the proof verbatim at n = m²: its hypotheses hold, its conclusion contradicts ET Prop 1.6. ∎
(Review repair: the earlier version asserted this for arbitrary F without a verified instance and used n = 25,
which is outside 𝓜.)

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

**Theorem 2.5 (numerator models; CERTIFIED, `scripts/z25_models.py` → `logs/z25_models.txt`).**
For k/n = 1/x + 1/y + 1/z the same parametrisation, transports and divisor closure hold with 4 replaced by k, and
genuine prime exceptions exist: k = 8: E_8 ∩ primes < 2000 = {2, 3, 11, 17, 131, 241}; k = 12: 16 primes, the largest
1873 (counts for 8 ≤ k ≤ 25 in the log; for k ≥ 7 the prime 2 is exceptional since k/2 > 3, but small primes are
not all exceptional, e.g. 10/5 = 1 + 1/2 + 1/2). Computed exactly:
(a) the square law "p ∈ E_k ⟹ p² ∈ E_k" fails: 8/11 has no solution, 8/121 = 1/18 + 1/99 + 1/2178; for 8 ≤ k ≤ 25
and exceptional p < 400, p² is exceptional only at (11,2), (12,5), (13,2), (14,2), (14,29), (15,2), (16,2), (16,3),
(16,11), (17,2), (17,3), (18,2), (19,2), (20,2), (20,3), (20,11), (20,41), (21,2), (22,2), (22,3), (22,5), (22,7),
(22,53), (23,2), (23,3), (23,5), (23,7), (24,2), (24,3), (24,5), (24,7), (24,13), (24,17), (24,103), (25,2), (25,3),
(25,13), and is soluble in all other cases;
(b) the *truncated* recombination law "every prime factor q > k of (p² − 1)/4 is in S_k ⟹ p ∈ S_k" fails for every
k ∈ [10, 25] (e.g. k = 10, p = 61: (61² − 1)/4 = 930 = 2·3·5·31, 10/31 soluble, 10/61 not). This refutes only the
truncated law: the untruncated k-analogue is vacuous in these models because 2 ∈ E_k. The {(p−1)/2, (p+1)/2} law
(no truncation) fails for every k ∈ [8, 25] except 9 (e.g. k = 8, p = 131); (R266 repair: these populations are
the exceptional p > 3k, as in the script; without that restriction the {(p∓1)/2} law fails also at k = 9 (p = 19:
9/9, 9/10 soluble, 9/19 not) and the truncated law also at k = 8, 9, vacuously, e.g. k = 8, p = 17);
(c) for k = 8 there is no exceptional prime in (241, 2000), so every k-uniform law forcing an exceptional prime
successor in (p, 8p] is false at p = 241 (8·241 = 1928). This refutes only laws whose window was exhausted.
Consequence: a proof of any of these law shapes must use the numerator 4 (cf. numerator blindness (J)41); a
k-uniform argument is refuted by these finite computations (R266 repair: only one whose validity range includes the
tested p, i.e. without a threshold p > p₀(k); cf. R207 D1 on (J)41).

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
*Proof.* (a) (Review repair: "every p′" means every *prime* p′ in the class, by Dirichlet infinitely many; at
composite members the transferred triple is still a solution of 4/p′ but need not be ET-normalised, e.g. slice
(1,2,3), H = 8, Type I works at 7 and gives (60, 6, 12) at 15 with gcd(15, 6·12) > 1.) If 4ab | p′ + e for two
primes p′ of the class differing by a multiple of αH′ only — take p′ and p′ + tαH′ with gcd(t, 4ab) = 1, both prime
(R266 repair: such t exist — fix t mod each odd ℓ | 4ab, ℓ ∤ αH′, outside the residues 0 and −p′(αH′)^{−1}, possible
as ℓ ≥ 3, note 2 | αH′, then apply Dirichlet) —
then 4ab | tαH′, so 4ab | αH′; if 4ab | p′e + 1 for both, 4ab | tαH′e with gcd(e, 4ab) = 1, so 4ab | αH′. Conversely
if p has a witness with H | αH′ the same slice works at every prime p′ of the class (d = (p′+e)/H resp. (p′e+1)/H
is a positive integer, and for prime p′ every solution is ET). (b) Totality must hold
whatever witness the source happens to have. ∎

**Fixture test (CERTIFIED, `scripts/z25_gate.py fixtures`; entries "source(×α): passing/all source witnesses").**
No source is total at any fixture; at 3361 the source 281 (3361 = 12·281 − 11) passes **0 of 17** witnesses.
(Rerun after review with g = 24 included: adds 313 ← 13 (×24): 1/4; log `logs/z25_gate_fixtures.txt`.)
Scope: "total" here is the core's notion — works for *every* supplied source witness. A proof that a favourable
source witness always exists, or a procedure that examines *all* witnesses at the source, is not excluded by
these counts.
```
97 89(x1):5/10 101(x1):9/16 103(x1):14/27 107(x1):8/25 109(x1):9/15 43(x2):3/14 47(x2):10/34 53(x2):8/13 29(x3):3/7 31(x3):6/19 23(x4):4/21 17(x6):2/4 11(x8):2/9 13(x8):1/4
193 181(x1):4/17 191(x1):15/67 197(x1):14/23 199(x1):31/42 97(x2):5/8 101(x2):6/16 61(x3):1/11 67(x3):2/17 47(x4):5/34 31(x6):3/19 23(x8):4/21 17(x12):2/4
313 307(x1):12/40 311(x1):20/79 317(x1):14/34 151(x2):9/31 157(x2):11/24 101(x3):4/16 103(x3):6/27 107(x3):8/25 79(x4):20/37 53(x6):8/13 13(x24):1/4
3361 3359(x1):25/423 3371(x1):9/77 3373(x1):7/66 1117(x3):9/64 1123(x3):10/48 839(x4):15/194 419(x8):5/81 421(x8):1/16 281(x12):0/17
5209 5197(x1):9/104 2609(x2):10/40 1733(x3):8/59 1301(x4):7/38 1303(x4):10/53
233689 116849(x2):34/167 77893(x3):27/197 77899(x3):85/225
```

**Theorem 3.2 (the T1 adversary: invisible witnesses; PROVED; classical in substance).** (R266 repair:
attribution.) This is the Mordell–Schinzel square-class obstruction in local form: a witness slice with H | L is a
polynomial ES identity on the class p mod L, and "a primitive congruence class n = r mod q which is a perfect square
cannot be solved by polynomials (this also follows from Proposition 1.6)" (Elsholtz–Tao p. 8, citing Mordell and
Schinzel; ET p. 6: this rules out finite covering-congruence strategies); in the campaign it is T1, DISCOVERIES (C)2
and (C)7. Only the CRT normalisation below and the recombination reading (Cor 3.3) are added here.
Let p be an odd prime (more generally: odd p and an ET-normalised witness; R266 repair) and L ≥ 1. If p is congruent to a
square modulo L (for odd p this is automatically an *odd* square when 2 | L; for odd L replace m by m + L), then
*no* ET witness at p has modulus H dividing L. Consequently a source witness w′ with p ≡ □ (mod αH′(w′)) is
*invisible*: no determined lift (Thm 3.1) can use it, and the recombination law from that source is not
provable by determined lifts. For p ∈ 𝓜 prime (p ≡ 1 (8), (p/3) = (p/5) = (p/7) = 1) every source witness whose
αH′ is supported on {2, 3, 5, 7} ∪ {ℓ : (p/ℓ) = 1} is invisible; e.g. a source n′ ≡ 3 (4) has the witness H′ = 4
(Type II, a = b = 1, e = 1), invisible whenever α is {2,3,5,7}-smooth (as for all α | 24 used here). (Review
correction: for general α it can be visible — p = 1201 = 17·71 − 6, source 71, αH′ = 68 supports the Type I witness
(1, 17, 6, 53) at 1201.)
*Proof (repaired after review: ET normalisation at the square).* Suppose p has an ET witness with slice (a,b,c),
e = (a+b)/c, H = 4ab | L. Note: since p is prime the witness is ET-normalised, so p ∤ x = abd (Type II) resp. p ∤ yz = (acd)(bcd)
(Type I); hence p ∤ ab, and p ∤ c in Type I. In Type II also p ∤ e: e ≥ p would give 4ab ≤ p + e ≤ 2e ≤ 2(a + b), so
a = b = 1 and e ≤ 2 < p. Choose, by CRT, an odd m with m² ≡ p (mod L) and additionally
m ≢ 0 (mod ℓ) for every prime ℓ | c·e not dividing L (for ℓ | L, ℓ ≠ p, this is automatic, since
m² ≡ p ≢ 0 (mod ℓ); if p | L then p ‖ L and p | m, and one uses p ∤ ab, p ∤ e (Type II), p ∤ c (Type I) recorded
above — R266 repair).
Put n = m², so n ≡ p (mod H). Type II: d′ = (n + e)/H is a positive integer and (x, y, z) = (abd′, nacd′, nbcd′)
solves 4/n (direct check: the sum is c(n + e)/(nabcd′)); gcd(n, ab) = gcd(p, ab) = 1 and gcd(n, d′) | gcd(n, e) = 1,
so gcd(n, x) = 1: an ET Type II solution of an odd square. Type I: d′ = (ne + 1)/H, (x, y, z) = (nabd′, acd′, bcd′);
gcd(n, abd′) = 1 because H d′ ≡ 1 (mod n), and gcd(n, c) = 1 by the choice of m: an ET Type I solution. Either
contradicts ET Prop 1.6. ∎

**Corollary 3.3 (joint recombination; PROVED; folklore-level application of T1 — R266 repair).** Combining several sources (any finite Q(p), any number of shifts,
all supplied witnesses jointly) pins p modulo L = lcm(α_iH′_i). Since "p ≡ □ (mod L)" is a local condition at each
prime power of L (for odd p and 2-powers: p ≡ 1 (8) is a square mod every 2^k), the lcm of invisible moduli is
invisible. Hence a joint determined recombination over Q(p) that must work for *every supplied tuple* of source
witnesses is total **only if some single source in Q(p) has no invisible witness at all** (necessary, not
sufficient). Caution (review): joint lifts are genuinely stronger than single ones on *visible* inputs —
moduli that fail individually can pass jointly (p = 17: 8 and 12 fail, lcm 24 passes); the corollary only says
that invisible inputs cannot be rescued by combination.

**Numerics (CERTIFIED, `scripts/z25_sqadv.py`, `z25_joint_run.py`).** (i) Consistency of the lemma: for every
fixture p ≤ 5209, none of p's own ET moduli H has p ≡ □ (mod H). (ii) Every source (all primes (p + j)/g,
|j| ≤ 12, g | 24) at every fixture ≤ 5209 has ≥ 2 invisible witnesses (e.g. 3361 ← 281 (×12): 11 of 17 invisible;
97 ← 43 (×2): 11 of 14). (iii) The joint search finds an adversarial tuple at every fixture ≤ 5209 (all 5–14
sources at once; e.g. at 97 with 14 sources the lcm of the chosen moduli is 2^6·3^2, and 97 ≡ 1 (mod 8), 97 ≡ 4² (mod 9);
313 now with 11 sources incl. 13 (×24); logs `logs/z25_joint.txt`, `logs/z25_sqadv.txt`).
So route (D) through congruence-mediated recombination that must accept any supplied witnesses is not total at
any fixture ≤ 5209, for the exact reason T1: the adversary feeds witnesses whose moduli only see residues of p that are
squares. A route-(D) law must use an input that sees a *non-residue* prime of p, and no such input is forced by
"q ∈ S".

**All Mordell-class primes p < 10^5 with v = (p+1)/2 prime (CERTIFIED, `z25_gate.py mordell 100000`,
log `logs/z25_gate_mordell.txt`):** 49 such p; the single-source law "W(v) ≠ ∅ ⟹ W(p) ≠ ∅" is total through
determined lifts at **0 of 49** (and never completely empty either: a positive fraction, typically 15–50%, of
v's witnesses lift).

### 3.2 The square law p₀ ∈ E ⟹ p₀² ∈ E (idea 3)

By (K3) composites built from one seed are powers of p₀ (Thm 1.4(c)), so the first composite law to test is
"W(p²) ≠ ∅ ⟹ W(p) ≠ ∅". It is total-or-not depending only on *mixed* solutions.
**Proposition 3.4 (PROVED / EVIDENCE as marked).** Let p ≥ 3 be prime.
(a) (PROVED) For x ≤ y ≤ z with 4/p² = 1/x + 1/y + 1/z let (v_p) be the sorted p-adic valuations. Patterns with
p² ∤ any denominator are impossible; patterns (≥2, 0, 0) and (≥2, ≥2, 0) are ET Type I/II for n = p² and are
excluded by ET Prop 1.6; patterns with all v_p ≥ 1 are p·W(p). So W(p²) ≠ ∅ ⟹ W(p) ≠ ∅ fails only through *mixed*
solutions (pattern (≥2, 1, 0)). (EVIDENCE, `z25_square_patterns.py`, p < 80) only (2,1,0), (2,1,1), (2,2,1) occur,
and mixed solutions exist for every p < 80.
(b) (PROVED) Mixed solutions are produced by: m ≡ 3 (4) with **p ∤ m** (review repair: without it the output
can be non-mixed, e.g. p = 5, m = 75, A = B′ = 25 gives (25, 50, 10)), z = (p² + m)/4 (then p ∤ z, so p ∤ AB′, and
p ∤ A + pB′, hence v_p(u) = 2, v_p(v) = 1, v_p(z) = 0), A, B′ | z with A + pB′ ≡ 0 (mod m):
4/p² = 1/z + 1/u + 1/v, u = p²(z/A)(A + pB′)/m, v = p(z/B′)(A + pB′)/m. These are divisor events of the
*quadratic* numbers (p² + m)/4, unrelated to p's own events (linear: p + e, pe + 1).
(c) (PROVED) Reciprocity kills m = 3 when p ≡ 1 (3): every prime ℓ | (p² + 3) has (−3/ℓ) = 1, so all divisors of z
are ≡ 1 (3) and A + pB′ ≡ 2 (3). (Mordell-type; m = 7, 11, … do occur, e.g. p = 13, z = 44, m = 7.)
(d) (EVIDENCE) The naive descent 4/p = 1/(pX) + j/X (j = (4X − 1)/p, X = x/p²) works for only ≈ 25–45% of mixed
solutions (`z25_mixed_check.py`). (CERTIFIED) In the numerator model k = 8 the law is false: 8/11 ∉ S_8 while
8/121 = 1/18 + 1/99 + 1/2178 (a mixed solution); likewise for all exceptions p < 400 of 8 ≤ k ≤ 14 except (11, 2), (13, 2), (14, 2), (14, 29) (R266 repair).
*Assessment.* A proof of the square law must be 4-specific and must exclude mixed solutions at exceptional p —
a fresh B2 lottery at (p² + m)/4. Even if proved it gives F(p₀) = {p₀^k}, growth log N (Thm 1.4).

### 3.3 The progression law (idea 2) — total, but only into a relaxation

**Proposition 3.5 (PROVED; folklore-level).** Let M_X = lcm{H = 4ab ≤ X}. If p₀ ∈ E then every n with n ≡ p₀
or n·p₀ ≡ 1 (mod M_X) lies in E_X := {n : n has no ET witness with H ≤ X}. (Thm 2.2(a).) Growth: ≥ N/M_X − 1 elements up to N
— far beyond (1.1) — but into the relaxation E_X ⊋ E.
**Obstruction (PROVED).** The law cannot be upgraded to E on any positive proportion of the progression without
proving ES(p₀): by (K4), #{n ≤ N, n ≡ p₀ (M_X), n ∈ E} ≤ C₀N exp(−c₀(log N)^{2/3}) = o(N/M_X) once
log M_X ≤ (c₀/2)(log N)^{2/3}; so the upgraded law would contradict (K4) (Thm 1.1), i.e. it is ES(p₀) itself.
The visible obstruction at p₀ is exactly the finite set of classes of modulus ≤ X (B1/B3); the progression
members acquire fresh large-modulus witnesses (B2). The hypothesis "finite data" cannot be violated here: what p₀
"knows" is only its residues, and by Thm 3.2 no ET witness of p₀ has modulus supported on primes ℓ with
(p₀/ℓ) = 1 (and on 2 when p₀ ≡ 1 (8)) (R266 repair: replaces "carry no information at all"). Under core §5 this
progression law is in the "NOT SUCCESS" category (classical congruence progression), listed only as a relaxation.
