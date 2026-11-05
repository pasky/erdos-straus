# Z58_TRYO — tryhard lane O on (★): 4uBC − u − B = p  — no proof of the full statement; almost-all theorem PROVED

Lane TRYO, wave z58. Fresh attack (no FRONTIER / Z5* memos read). Only external data used: `data/z58/screens/`.
Scripts `scripts/z58_tryo_*`, data `data/z58/tryo/`.

𝔐 := {1, 121, 169, 289, 361, 529} mod 840 (Mordell's classes); "p ∈ 𝔐" means p prime in one of these classes.

**Bottom line.** The full statement ("every sufficiently large prime p ≡ 1 (24), in particular every large p ∈ 𝔐, has a
solution of (★)") is NOT proved. What is proved here:
* Lemmas 1.1–1.4 (PROVED, elementary): equivalent forms of (★), incl. "∃ coprime u, B with 4uB | p+u+B" and
  "∃ u: p+u has a divisor ≡ −1 (mod 4u)"; a sufficient character-kernel criterion for failure (converse false).
* Thm 2 (PROVED, using only the arithmetic large sieve + Mertens in progressions to fixed moduli):
  #{p ≤ X prime : (★) has no solution} ≪_A X (log X)^{−A} for every A. Same for the C-even subfamily and for all
  integers n ≤ X.
* Props 3.1–3.2 (PROVED, Dirichlet/Linnik): no finite set of congruence identities covers 𝔐; there are infinitely
  many p ∈ 𝔐 with no solution having uB < (1/L₀ − o(1)) log p, L₀ a Linnik exponent (possibly vacuously). Plus CERTIFIED: the
  least-non-residue route is dead (each prime q ∈ [11, 47] is a non-residue of some 𝔐-zero of (★)).
* Round 2 (§8, pointwise): no forcing mechanism found. PROVED: square levels ⟺ forms Ax²+2sxy+By² of disc −4p with
  A ≡ −1 (4s²), which lie in the non-principal genus (Lemmas 8.1–8.2); weak pointwise Prop 8.7. CERTIFIED: (★) for all 355 096 166 primes p ∈ 𝔐 ∩ (10¹⁰, 3·10¹¹].
  EVIDENCE: small levels independent; no Chebotarev law among the tested cubic/quartic/octic symbols; primality
  appears to act only locally (heuristic; prime vs coprime-composite zero rates comparable in a small sample).
* EVIDENCE (§5): for hard p the solution is "C small, uB ≈ p/(4C)" or "u small": min u ≤ 469 for all 179 468 primes
  p ∈ 𝔐, p ≤ 10⁸, except the 9 𝔐-zeros; min C reaches 41 027; min uB reaches ≈ p/4.

## §0 Falsifier ledger (first stated in commit 231cda77, REVISED after it; re-stated at end in §7)

Changes vs. 231cda77: (i) the claimed equivalence "failure ⟺ every u has an odd character mod 4u killing all primes
of p+u" is WITHDRAWN (only ⇐ holds; Lemma 1.2(c) is a counterexample to ⇒); (ii) (C) now also covers integers
(Thm 2(b)); (iii) the F4 range "q ∈ [5, 47]" is corrected to q ∈ [11, 47] inside 𝔐 (409, 577 are not in 𝔐).

Attack: (A) reduce (★) to "∃ u, B ≥ 1 with 4uB | p+u+B" and to a character-kernel criterion; (B) try to cover primes
p ∈ 𝔐 by identities attached to one quadratic non-residue prime q (least-non-residue route); (C) prove the strongest
honest weaker statement (almost all primes) by a large sieve on primes.

* (F1) odd squares n = m². (A): for n = m² the witness character is ψ_u = (−4u/·) for every u (Lemma 1.3). For a prime
  p the identity (q/p) = ψ_u(q) on primes q | p+u still holds but (·/p) is a character mod p, so ψ_u is not forced to
  be a witness — this is where primality enters (A), and it is *only* a non-obstruction, not a proof.
  (C): the sieve classes −u (mod ℓ), ℓ ≡ −1 (4u), contain no squares; for n = m² the argument is valid but vacuous
  (it bounds a set of size √X by X/(log X)^A). Theorem 2 is a counting statement; it never certifies an individual n.
* (F2) C-even part. Thm 2 holds verbatim for C even (Thm 2(c)) — that is an almost-all statement, consistent with the 12
  C-even zeros in [10¹⁰, 1.1·10¹⁰]. Nothing about individual p is derived.
* (F3) 285 composite zeros: Thm 2(b) for integers is again only a density bound; consistent.
* (F4) 14 prime zeros: kill route (B) (§3). Thm 2 is consistent (finite/sparse exceptions allowed).

No HOT LEAD.

## §1 Reformulations (PROVED)

Throughout u, B, C ∈ ℤ_{≥1}. Lemma 1.1 (i)–(iv) hold verbatim for any positive integer n in place of p; only the
gcd claim uses that p is prime.

**Lemma 1.1.** The following are equivalent:
(i) 4uBC − u − B = p for some u, B, C ≥ 1;
(ii) (4uC − 1)(4BC − 1) = 4Cp + 1 for some u, B, C ≥ 1 (i.e. 4Cp+1 has a divisor d ≡ −1 (mod 4C));
(iii) there are u ≥ 1 and a divisor d of p + u with d ≡ −1 (mod 4u);
(iv) there are u, B ≥ 1 with 4uB | p + u + B.
Moreover any solution has gcd(u, B) = 1.

*Proof.* (i)⇔(ii): (4uC−1)(4BC−1) = 16uBC² − 4uC − 4BC + 1 = 4C(4uBC − u − B) + 1. Conversely a divisor d ≡ −1 (4C)
of 4Cp+1 has cofactor e with de ≡ 1 and d ≡ −1, so e ≡ −1 (mod 4C); write d = 4uC−1, e = 4BC−1, u, B ≥ 1 because
d, e > 0. (i)⇔(iii): (i) says p + u = B(4uC − 1); put d = 4uC − 1. Conversely d | p+u, d = 4uC − 1 (d > 0 so C ≥ 1),
B := (p+u)/d ≥ 1 gives Bd − u = p. (i)⇔(iv): (i) says p + u + B = 4uB·C, and conversely C := (p+u+B)/(4uB) ≥ 1
since p+u+B > 0. Coprimality: g = gcd(u,B) divides 4uBC − u − B = p, so g ∈ {1, p}; if g = p then
u, B ≥ p and 4uBC − u − B ≥ u(4B−1) − B ≥ p(4B−1) − B = B(4p−1) − p ≥ 4p² − 2p > p. ∎

Note: in (iv) no size condition is needed — **every** pair (u, B) gives a congruence identity
"p ≡ −(u+B) (mod 4uB) ⇒ (★) solvable". Hence the solvable primes are exactly the union of the classes
−(u+B) mod 4uB.

**Lemma 1.2 (character-kernel criterion).** Fix u ≥ 1, n ≥ 1, and let n' be the largest divisor of n coprime to 2u.
Let H ≤ G := (ℤ/4uℤ)^× be the subgroup generated by the classes of the primes q | n'.
(a) If some odd character χ mod 4u is trivial on every prime q | n', then n has no divisor d ≡ −1 (mod 4u).
(b) If n has a divisor d ≡ −1 (mod 4u) then −1 ∈ H; and −1 ∈ H iff no odd χ mod 4u is trivial on H.
(c) The converse of (a) is FALSE in general: n = 33, u = 5 (4u = 20): H = ⟨11, 3⟩ ∋ 11·3² ≡ 19 ≡ −1, so no odd χ is
 trivial on H, yet the divisors 1, 3, 11, 33 are ≡ 1, 3, 11, 13 (mod 20).
Consequently: if for every u ≥ 1 some odd χ_u mod 4u is trivial on all primes of (p+u)', then (★) fails at p; and if
(★) fails at p then −1 ∉ D_u for every u, where D_u ⊆ H_u is the set of divisor classes of (p+u)'.

*Proof.* A divisor d ≡ −1 (4u) is coprime to 2u, hence divides n', and its class lies in H. (a) χ(d) = 1 ≠ −1 = χ(−1).
(b) The first claim was just shown. If −1 ∉ H, the image of −1 in G/H has order 2, so some character of G/H is −1 on it;
lifted to G it is odd and trivial on H. Conversely an odd χ trivial on H gives χ(−1) = −1 ≠ 1, so −1 ∉ H.
(c) direct check (also `uv run python`: divisors of 33 mod 20 = [1, 3, 11, 13]). ∎

**Lemma 1.3 (squares, F1).** If n = m² and d | m² + u, d ≡ −1 (mod 4u), then gcd(m, d) = 1 (a common prime would divide
u, but d ≡ −1 (4u) is coprime to u), so −u ≡ m² is a nonzero square mod every prime of d and the Jacobi symbol
(−u/d) = 1; but (−u/d) = −1 for every d ≡ −1 (4u). Hence (★) never holds at squares, and the odd character
ψ_u := (−4u/·) (a character mod 4u) is a witness in Lemma 1.2 for every u.

*Proof.* Write u = 2^a v, v odd. (−1/d) = −1 (d ≡ 3 (4)); if a ≥ 1 then 8 | 4u so d ≡ −1 (8) and (2/d) = 1;
(v/d) = (d/v)(−1)^{(v−1)/2·(d−1)/2} = (−1/v)(−1)^{(v−1)/2} = 1. So (−u/d) = −1. For prime q | m²+u, q ∤ 2u:
(−u/q) = 1, i.e. ψ_u(q) = 1. ∎

**Lemma 1.4 (prime p).** Let p ≡ 1 (8) be prime and 1 ≤ u < p. For every prime q | p+u with q ∤ 2u:
(q/p) = (p/q) = (−u/q) = ψ_u(q) (reciprocity, p ≡ 1 (4); then p ≡ −u (mod q)). If (u/p) = −1, then p+u has a prime
factor q ∤ 2u with ψ_u(q) = −1, so ψ_u is NOT a witness in Lemma 1.2(a) at this u.
*Proof.* An odd prime q | u with q | p+u divides p, impossible as q ≤ u < p; so p+u = 2^a m with gcd(m, 2u) = 1.
Then −1 = (u/p) = ((p+u)/p) = (2/p)^a (m/p) = (m/p) = ∏_{q|m} (q/p)^{v_q(m)}, so some q | m has (q/p) = −1 = ψ_u(q). ∎
This is the only place where primality of p visibly breaks the square obstruction: for p ∈ 𝔐 all u composed of
2, 3, 5, 7 have (u/p) = 1, which is one reason (heuristically) why 𝔐 is hard. It does NOT give a solution: it only excludes the witness
χ_u = ψ_u, while (ℤ/4u)^× has φ(4u)/2 odd characters.

## §2 Almost all primes (PROVED)

**Theorem 2.** (a) For every A > 0: #{p ≤ X prime : (★) unsolvable} ≪_A X (log X)^{−A}.
(b) The same holds for #{n ≤ X : (★) unsolvable with p replaced by n}.
(c) For every A > 0: #{p ≤ X prime : (★) has no solution with C even} ≪_A X (log X)^{−A}.

Tools (standard, unconditional):
* **Arithmetic large sieve** (Montgomery 1968; constant N + Q² by Montgomery–Vaughan 1973; e.g. Iwaniec–Kowalski,
  §7.4; Montgomery, Topics in Multiplicative Number Theory, LNM 227, Thm 3.x / Montgomery–Vaughan, Mathematika 20
  (1973)): if 𝒜 ⊆ (M, M+N] ∩ ℤ and for each prime ℓ ≤ Q the set 𝒜
  avoids ω(ℓ) < ℓ residue classes mod ℓ, then |𝒜| ≤ (N + Q²)/L, L = Σ_{r≤Q} μ²(r) ∏_{ℓ|r} ω(ℓ)/(ℓ − ω(ℓ)).
* **Mertens in progressions, fixed modulus k, gcd(a,k)=1:** Σ_{ℓ≤y, ℓ≡a (k)} 1/ℓ = (log log y)/φ(k) + O_k(1) and
  Σ_{ℓ≤y, ℓ≡a (k)} (log ℓ)/ℓ = (log y)/φ(k) + O_k(1).

*Proof of (a).* Let Q = X^{1/2} and S = {p prime, Q < p ≤ X, (★) unsolvable at p}.
For a prime ℓ ≤ Q put Ω(ℓ) = {0} ∪ {−u mod ℓ : u ≥ 1, 4u | ℓ+1}.
*Claim: no p ∈ S is in Ω(ℓ) mod ℓ.* p ≡ 0 (ℓ) forces p = ℓ ≤ Q. If p ≡ −u (ℓ) with 4u | ℓ+1, then d := ℓ divides p+u
and d ≡ −1 (4u), so by Lemma 1.1(iii) (★) is solvable (explicitly C = (ℓ+1)/(4u), B = (p+u)/ℓ). Contradiction.
*Size.* For ℓ ≡ 3 (4): the u with 4u | ℓ+1 are the divisors of (ℓ+1)/4, all in [1, (ℓ+1)/4] ⊂ [1, ℓ−1], so the
classes −u are pairwise distinct and nonzero: ω(ℓ) = 1 + τ((ℓ+1)/4) ≤ 1 + (ℓ+1)/4 < ℓ. For ℓ = 2 or ℓ ≡ 1 (4):
4u ∤ ℓ+1, ω(ℓ) = 1 < ℓ.
Fix U ≥ 1 and let n_U(ℓ) = #{u ≤ U : ℓ ≡ −1 (mod 4u)} (so n_U(ℓ) ≤ ω(ℓ) − 1) and
h(ℓ) = (1 + n_U(ℓ))/ℓ ≤ ω(ℓ)/ℓ ≤ ω(ℓ)/(ℓ − ω(ℓ)). Extend h multiplicatively to squarefree r. Then L ≥ G(Q) :=
Σ_{r≤Q} μ²(r) h(r). Put κ = κ_U := 1 + Σ_{u≤U} 1/φ(4u).
By Mertens in progressions (finitely many moduli 4u, u ≤ U; residue −1):
 (M1) Σ_{ℓ≤y} h(ℓ) = κ log log y + O_U(1), (M2) Σ_{ℓ≤y} h(ℓ) log ℓ = κ log y + O_U(1), (M3) Σ_ℓ h(ℓ)² ≤ (U+1)² Σ 1/ℓ² = O_U(1).
*Lower bound for G (Rankin).* Let K ≥ 1 (chosen below, depending on U only), y = Q^{1/K}, δ = 1/log y, and restrict to
r with all prime factors ≤ y (P⁺(r) ≤ y):
 G(Q) ≥ F − T, F := Σ_{P⁺(r)≤y} μ²h(r) = ∏_{ℓ≤y}(1 + h(ℓ)), T := Σ_{r>Q, P⁺(r)≤y} μ²h(r) ≤ Q^{−δ} ∏_{ℓ≤y}(1 + h(ℓ)ℓ^δ).
For ℓ ≤ y, t = log ℓ/log y ∈ [0,1] and ℓ^δ = e^t ≤ 1 + (e−1)t, so 1 + hℓ^δ ≤ (1+h)(1 + (e−1)h t) ≤ (1+h)exp((e−1)h t).
Hence T ≤ e^{−K} F exp((e−1) Σ_{ℓ≤y} h(ℓ) log ℓ / log y) = F exp(−K + (e−1)κ + O_U(1/log y)) by (M2).
Choose K := ⌈(e−1)κ⌉ + 1; then for Q large T ≤ F e^{−1/2}, so G(Q) ≥ (1 − e^{−1/2})F. By (M1), (M3),
log F = Σ log(1+h) ≥ Σ h − ½Σ h² = κ log log y + O_U(1), so F ≫_U (log y)^κ ≫_U (log Q)^κ (K depends on U only).
*Conclusion.* |S| ≤ (X + Q²)/L ≤ 2X/G(Q) ≪_U X (log X)^{−κ_U}, and the exceptional primes ≤ X number
≤ |S| + Q ≪_U X (log X)^{−κ_U}. Since φ(4u) ≤ 2u, κ_U ≥ 1 + ½ Σ_{u≤U} 1/u ≥ 1 + ½ log U; given A pick U with
κ_U ≥ A. ∎
(b) Same proof with S ⊆ (0, X] ∩ ℤ, Ω(ℓ) without the class 0, ω(ℓ) = τ((ℓ+1)/4) for ℓ ≡ 3 (4) and 0 otherwise
(classes with ω = 0 are allowed in the large sieve; they contribute factor 1), h(ℓ) = n_U(ℓ)/ℓ, κ = Σ_{u≤U} 1/φ(4u).
(c) Use only u with 8u | ℓ+1: then C = (ℓ+1)/(4u) is even; n_U(ℓ) = #{u ≤ U : ℓ ≡ −1 (8u)}, κ = 1 + Σ_{u≤U}1/φ(8u)
≥ 1 + ⅛ log U. ∎

**Corollary 2.1 (short intervals).** Fix ε > 0 and a class a mod 840 with gcd(a, 840) = 1. For X large, every interval
(X, X + H], H = X^{7/12+ε}, contains ≫ H/log X primes p ≡ a (840) at which (★) is solvable.
*Proof.* Run the proof of (a) with 𝒜 = exceptional primes in (X, X+H] (N = H, Q = H^{1/2}; class 0 is avoided since
p > X > Q): |𝒜| ≤ 2H/G(Q) ≪_U H (log H)^{−κ_U} = o(H/log X) once κ_U > 1. Huxley's prime number theorem in short
intervals, in the form valid for progressions to a fixed modulus (Huxley's zero-density estimate
N(σ, T, χ) ≪ T^{12(1−σ)/5+ε} for each of the finitely many χ mod 840 plus the classical zero-free region, via the
explicit formula exactly as in Huxley, Invent. Math. 15 (1972) for ζ), gives ≥ (1/φ(840) − o(1)) H/log X primes ≡ a (840) in (X, X+H]. ∎ (PROVED modulo that standard input.)

Remarks. (1) Primality enters only through the class 0 (one extra unit of κ). The proof never certifies a given p;
it is fully consistent with (F1)–(F4). (2) Only *prime* d = ℓ are used; composite d would give more classes but
modulus-ℓ sieving only sees prime moduli. (3) This is the (★)-specific analogue of classical almost-all results for
Erdős–Straus (Vaughan 1970 has the much stronger exp(−c(log X)^{2/3}) for ES in general); not new in spirit.

## §3 What cannot work (PROVED / EVIDENCE)

**Prop 3.1 (no finite covering, PROVED).** For any finite set 𝒫 of pairs (u, B) there are infinitely many primes
p ∈ 𝔐 not in any class −(u+B) mod 4uB, (u,B) ∈ 𝒫.
*Proof.* Let L = lcm(840, 4uB : (u,B) ∈ 𝒫). Every prime p ≡ 1 (mod L) is in 𝔐 and satisfies p ≡ 1 (mod 4uB), while
1 ≢ −(u+B) (mod 4uB) because 0 < u + B + 1 ≤ uB + 2 < 4uB. Dirichlet gives infinitely many such p. ∎

**Prop 3.2 (PROVED, using Linnik's theorem with exponent L₀; L₀ = 5.18 by Xylouris, Acta Arith. 2011; L₀ = 5 in
Xylouris' 2018 Bonn dissertation).** There are infinitely many primes p ∈ 𝔐 such that every solution of (★) at p
(if any — the statement may be vacuous for some of them) has uB > (1/L₀ − o(1)) log p.
*Proof.* Take 𝒫 = {(u,B): uB ≤ Y}; lcm{4uB : uB ≤ Y} = 4·lcm(1..Y) = exp(Y(1+o(1))) (PNT), and for Y ≥ 7 this is
divisible by 840. By Linnik the least prime p ≡ 1 (mod L) is ≪ L^{L₀} = exp((L₀+o(1))Y). By Prop 3.1's
argument p has no solution with uB ≤ Y, and Y ≥ (1/L₀ − o(1)) log p. As Y → ∞ these p are distinct
infinitely often since p > L → ∞. ∎
(The data say the truth is far larger: min uB reaches ≈ p/4, i.e. C = 1 is the only solution, §5.)

**3.3 Least-non-residue route (route B) — dead (CERTIFIED from screens data).** Idea: if p is a non-residue mod some
prime q, cover {p ∈ 𝔐 : (p/q) = −1} by identities of modulus 840·q^k. By Lemma 1.1(iv) such a covering would have no
size condition, so it would solve every 𝔐-prime that is a non-residue mod q. But the 𝔐-zeros of (★) are non-residues:
5212561 mod 11; 5569 mod 13, 17, 19, 37, 41, 43, 47; 9601 mod 23, 29, 31; 1724209 mod 59, 61, 67, 73, 79 … — so for
every prime q ∈ [11, 47] (and many more) no such covering exists for (★). (409 and 577 show the same for q = 7, 5 —
Mordell's coverage of non-residues mod 5, 7 needs the other ES families.) Any proof must use moduli that grow with p.

## §4 Why the remaining step is the whole problem (analysis, no claim)

By Lemma 1.2, failure at p means: for every u, no divisor class of (p+u)' is −1 mod 4u (implied by, but weaker than,
"the primes of p+u lie in the kernel of an odd character mod 4u"). For p = m² the kernel form holds with ψ_u for all u
simultaneously. For a prime p, Lemma 1.4 excludes the witness ψ_u when (u/p) = −1, but leaves φ(4u)/2 − 1 other odd
characters, and also the non-kernel failure mode of Lemma 1.2(c). To rule all of them out one needs information on the
*distribution of the prime factors of p+u in classes mod 4u* for a single p and many u ≤ p^θ (data: u ≤ 469 suffices
to 10⁸). That is a statement about the factorisation of the specific short interval (p, p + p^θ] — not accessible to
sieve or L-function methods for individual p. The dual formulation Lemma 1.1(ii) (divisors of 4Cp + 1) bounds C
instead of u, and these are different problems (data: min u ≤ 469 but min C reaches 41 027). Every relaxation that is provable (Thm 2) is a counting statement.

## §5 Data (CERTIFIED computations; scripts in `scripts/z58_tryo_*`)

* `minu_1e8.txt` (`z58_tryo_minu.c`): all 179 468 primes p ∈ 𝔐, p ≤ 10⁸: m(p) = least u with p+u having a divisor
  ≡ −1 (4u). Unsolvable exactly at the 9 𝔐-zeros of `star_prime_zeros.txt` (independent cross-check of the screen).
  Otherwise m(p) ≤ 469 (record p = 53 325 721, d = 11 255, C = 6, B = 4 738); 46 % have m = 1.
  Records: 26 (19 441), 131 (427 249), 410 (4 160 641), 469 (53 325 721).
* `minC_1e8.txt` (`z58_tryo_minC.c`, label "u=" there means C; full factorisation via trial division + Pollard rho):
  least C: max 41 027 at p = 85 664 329 (d = 2 953 943). Same 9 zeros.
* `minuB_2e7.txt` (`z58_tryo_minuB.c`): least uB (= least modulus of a hitting identity); the file logs records of
  Y/log p; the last record holder has Y = 835 986 at p = 3 341 881 (≈ p/4, i.e. only C = 1 works) — so Prop 3.2's log p is very far from the truth.

## §6 Status of claims

| claim | status |
|---|---|
| Lemma 1.1 equivalences, gcd(u,B)=1 | PROVED |
| Lemma 1.2 (a),(b),(c) (odd χ trivial on primes of (p+u)' ⇒ no hit; converse false) | PROVED |
| Lemma 1.3 squares fail | PROVED |
| Lemma 1.4 (u/p) = −1 ⇒ ψ_u not a witness | PROVED |
| Thm 2 (a)(b)(c) almost all, ≪_A X(log X)^{−A} | PROVED (standard large sieve + Mertens in APs) |
| Cor 2.1 short intervals | PROVED modulo Huxley PNT in short intervals for fixed-modulus APs |
| Lemma checks (1.1 (iii)⇔(iv), 1.3, 1.4) | numerically verified, `scripts/z58_tryo_check_lemmas.py` |
| Prop 3.1, 3.2 | PROVED (Dirichlet; Linnik with any exponent L₀) |
| §3.3 route B dead | CERTIFIED (screen data) |
| Lemma 8.1, 8.2 (square levels ↔ forms, genus) | PROVED |
| Prop 8.7 (square obstruction broken at level ≤ n₂(p)) | PROVED (Burgess; GRH: Ankeny–Bach) |
| §8.2–8.4 independence / no tested Chebotarev law / primality-local (heuristic) | EVIDENCE |
| §8.6 (★) for all p ∈ 𝔐 ∩ (10¹⁰, 3·10¹¹] | CERTIFIED |
| full statement for all large p | NOT PROVED |

## §7 Falsifier ledger at the end (after hostile review)

No HOT LEAD. Nothing here proves (★) for any individual prime not already checked numerically.
* (F1) squares: Lemma 1.3 (with the gcd step) shows the failure; Thm 2 is a counting bound, vacuous on squares
  (√X of them); Lemma 1.4 is the identifiable step where primality ((u/p) = −1 for some u) breaks the square witness
  ψ_u — and it is insufficient (Lemma 1.2(c), other odd characters).
* (F2) C-even: Thm 2(c) is an almost-all statement, consistent with the 12 C-even zeros in [10¹⁰, 1.1·10¹⁰].
* (F3) composites: Thm 2(b) is a density bound for integers, consistent with the 285 composite zeros.
* (F4) 14 prime zeros: kill the least-non-residue covering route for every q ∈ [11, 47] inside 𝔐 (§3.3); my
  engines independently reproduce the 9 𝔐-zeros ≤ 10⁸ (§5).
Hostile review (subagent, this lane): no FATAL/MAJOR issues; all MINOR/NIT items addressed in the final commit.
Round-2 hostile review: no FATAL; one MAJOR (§8.4 labelled PROVED → now heuristic) and MINOR/NITs, all addressed.

## §8 Round 2 — pointwise attack (one fixed prime p)

Brief for round 2: almost-all statements don't count; find a mechanism forcing a hit at one fixed p, or prove pointwise
partial results. **Outcome: no pointwise mechanism found; one CERTIFIED pointwise range (§8.6); the mechanisms tried are
reduced to equivalent statements or refuted by data.** Details below.

### 8.1 Mechanism A: binary quadratic forms of discriminant −4p (where primality has global structure)

**Lemma 8.1 (square levels = forms; PROVED).** For s ≥ 1, (★) has a solution with u = s² iff there is a positive
definite form Ax² + 2sxy + By² of discriminant −4p (i.e. AB − s² = p) with A ≡ −1 (mod 4s²); then C = (A+1)/(4s²).
*Proof.* p + s² = AB ⟺ (2s)² − 4AB = −4p, and Lemma 1.1(iii) with d = A, u = s². ∎

**Lemma 8.2 (genus; PROVED).** For p ≡ 1 (4) prime, D = −4p has exactly two genera (genus characters χ_{−4}, χ_p with
χ_{−4}χ_p = 1 on represented values prime to D). A form as in Lemma 8.1 represents A ≡ 3 (4), so it lies in the
NON-principal genus. At C = 1 more generally: (★) at level C = 1 ⟺ the principal ideal (1 + 2√−p) of ℤ[√−p] has a
prime-ideal divisor in the non-principal genus ⟺ 4p+1 has a prime factor q ≡ 3 (4) (since χ_p(q) = χ_{−4}(q)).
*Proof.* Genus theory for D = −4p (two prime discriminants −4 and p). A ≡ 3 (4) gives χ_{−4}(A) = −1. For q | 4p+1,
(−p/q) = 1 so q splits; the genus of a prime ideal above q is read off from χ_{−4}(q). ∎

What this buys: hits at square levels / C = 1 are exactly "ideal divisors of explicit principal ideals landing in the
non-principal genus". Primality enters as "two genera, the non-principal one has h(−4p)/2 classes". For n = m² the
analogue fails by Lemma 1.3. **Why it does not force a hit (EVIDENCE/heuristic):** each class of the non-principal genus
contributes ≈ (log p)/√p expected hits (a primitive representation A of the class gives an attached root s uniformly
distributed mod A; one needs |s| ≤ √A/2 and 4s² | A+1), and there are ≈ √p classes, so the total is ≈ log p — a
polylog quantity with no pigeonhole slack; composition of forms randomises s (CRT), destroying "s small".
Level u is expressible by quadratic Dirichlet characters only when (ℤ/4u)^× is elementary 2-abelian, i.e. 4u | 24,
u ∈ {1, 2, 3, 6} (same for C); only u = 1 and C = 1 are genus conditions for disc −4p. For all other levels the condition d ≡ −1 (4u) needs non-quadratic characters, which no genus/Legendre information sees.

### 8.2 Mechanism B: forcing between levels (EVIDENCE: none)

`scripts/z58_tryo_levels.c`, `data/z58/tryo/levels_1e6_3e7.txt`: for the 55 369 primes p ∈ 𝔐 ∩ [10⁶, 3·10⁷] and the
24 levels u = 1..12 (p+u) and C = 1..12 (4Cp+1), the co-failure ratios P(fail_i ∧ fail_j)/(P(fail_i)P(fail_j)) for
i ≠ j lie in [0.98, 1.11]: the levels behave independently; no level's failure forces another's success. 47 of the
55 369 primes fail all 24 levels. A forcing law among small levels would show up as a ratio ≈ 0; there is none.

### 8.3 Mechanism C: Chebotarev / higher-residue laws (EVIDENCE: none among those tested)

A law "p fails ⇒ p splits completely in L" for a non-abelian L would give a non-congruence pointwise theorem. Tested on
the 9 𝔐-zeros: cubic, quartic, octic residuosity of 2, 3, 5, 7, 11, 13, −1, −3, 6, 10 mod p — no symbol is trivial at all
9 zeros except the forced ones (−1 quartic since p ≡ 1 (8); −1 cubic). In particular 2 is a quartic residue at 8 of 9
(not at 1 724 209), so "2 not a quartic residue ⇒ (★)" is false. p = x² + 24y², x² + 48y², x² + 72y² at all 9 zeros,
but 24, 48, 72 are idoneal, so these are congruence consequences of p ∈ 𝔐 (one class per genus).

### 8.4 Where primality acts, quantitatively (heuristic remark + EVIDENCE)

Whether level u hits depends only on the multiset of classes in G_u = (ℤ/4u)^× of the prime factors of (p+u)'
(Lemma 1.2). The only constraint p imposes on that multiset beyond its product (≡ (p+u)' mod 4u, local) is the
quadratic one of Lemma 1.4: (q/p) = ψ_u(q), whose product is (u/p) = (2/p)^a (p/v) (u = 2^a v) — again determined by
p mod 4u. Characters
of order ≥ 3 mod 4u are invisible to Legendre information (their analogue (−u/q)_k, for q ≡ 1 (k) and −u not a k-th power
(nor of the form −4·(4th power) when k = 4), is an Artin symbol of the non-abelian field ℚ(ζ_k, (−u)^{1/k}), not a
function of q mod 4u). Heuristically, then, primality acts at each level only through local data — whereas the square
obstruction (Lemma 1.3) is global. (Not a theorem: k-th power relations (p/q)_k = (−u/q)_k do exist.)
Data (`scripts/z58_tryo_legeffect.c`, `data/z58/tryo/legeffect_1e6_3e7.txt`, p ∈ 𝔐 ∩ [10⁶, 3·10⁷]): failure rate at
level u given (u/p) = +1 vs −1: u = 11: 0.756 vs 0.475; u = 13: 0.914 vs 0.732; u = 17: 0.856 vs 0.659; u = 26:
0.848 vs 0.700 — a non-residue u roughly doubles the hit probability (hit ratios ≈ 2.2, 3.1, 2.4, 2.0), consistent with
Lemma 1.4, but does not force a hit.
**Primes vs non-square composites (EVIDENCE).** Among n ≤ 8·10⁶ (composite-zero file covers n ≤ 7 999 801), n ≡ 1 (4), gcd(n, 105) = 1: zero rate for primes
13/269 758 = 4.8·10⁻⁵, for non-square composites 20/643 882 = 3.1·10⁻⁵ (20 = composite zeros coprime to 210, from
`composite_zeros_le8e6.txt`; largest 3 210 601 = 19·37·4567; 15 of them in 𝔐). So, in this small sample (13 vs 20 events; zeros cluster at small n, where primes
are denser), primality per se gives no detectable advantage:
the operative properties are non-squareness and the local data; most composite zeros (214/285) are divisible by 3,
a local defect primes > 3 don't have. A pointwise proof for primes is therefore, in substance, a pointwise statement
about the factorisations of n+u for large non-square n with prescribed local data.

### 8.5 Meta-obstruction to counting proofs (heuristic, not a theorem)

R(p) = Σ_{d ≡ 3 (4)} #{u | (d+1)/4 : p ≡ −u (mod d)} (Lemma 1.1(iii)), main term ≍ log² p. A counting proof for one p
would need the error in this sum — a sum over moduli d up to ≈ p of indicator functions of p mod d at resolution 1/d —
to be o(log² p). The pointwise-in-p techniques listed here (exponential sums in p/d, Kloosterman/Weil bounds on the modular
hyperbola xy ≡ 1 (p) with x, y ≡ −1 (4C), large sieve) has errors that are powers of p or at least larger than polylog
at this resolution; the modular-hyperbola count for one level C has main term ≈ log p/C against Weil error ≈ p^{1/2}.
So pointwise existence needs an algebraic forcing mechanism, and §8.1–8.4 indicate none exists at the level of genus,
small levels, or Chebotarev data. This is the honest state of round 2.

### 8.6 CERTIFIED pointwise range

`scripts/z58_tryo_range.c` (for each p ∈ 𝔐 in range: least u ≤ 10⁵ with a divisor d ≡ −1 (4u) of p+u, factoring by
trial division to 1000 + Pollard rho + 12-base Miller–Rabin (bases 2..37, deterministic below ≈ 3.18·10²³); every reported solution is
re-verified as 4uBC − u − B = p in 128-bit arithmetic).
**CERTIFIED: (★) holds for every prime p ∈ 𝔐 with 10¹⁰ < p ≤ 3·10¹¹** — 355 096 166 primes in four contiguous runs
(`data/z58/tryo/range_{a,b,c,d}.txt`: [10¹⁰, 5.5·10¹⁰] 58 344 306, (5.5·10¹⁰, 10¹¹] 56 111 206, (10¹¹, 2·10¹¹]
121 533 478, (2·10¹¹, 3·10¹¹] 119 107 176), hard = 0, VERIFYFAIL = 0. Largest least-u: 316 at p = 53 499 061 849 (d = 447 455,
C = 354, B = 119 563); other run maxima: 263 (p = 60 921 814 801), 158, 289 (p = 219 564 149 401). Least-u > 2⁸ occurs for at most one
p per run (1, 1, 0, 1). Sanity: on [1, 10⁸] the same engine returns exactly the 9 𝔐-zeros as HARD.

### 8.7 The one pointwise statement that does follow (PROVED, weak)

**Prop 8.7.** For every prime p ≡ 1 (mod 8) there is a prime u ≤ n₂(p) (the least quadratic non-residue mod p;
n₂(p) ≪_ε p^{1/(4√e)+ε} by Burgess, n₂(p) ≤ 2 log² p under GRH by Ankeny–Bach) such that p + u has a prime factor q ∤ 2u
with ψ_u(q) = (−u/q) = −1. In other words the square obstruction of Lemma 1.3 (ψ_u kills every prime factor of n+u, at
every level u) is broken for primes at a level u ≤ n₂(p).
*Proof.* u := n₂(p) is prime and odd (2 is a residue as p ≡ 1 (8)), u < p, (u/p) = −1; apply Lemma 1.4. ∎
This is necessary, not sufficient, for a hit at u: (ℤ/4u)^× still has φ(4u)/2 − 1 = u − 2 other odd characters and the
non-kernel failure mode of Lemma 1.2(c). The 𝔐-zeros have n₂(p) ∈ {11, 13, 17, 19, 23} (§3.3), so the statement is
consistent with F4, does not apply to squares (for n = m², the Jacobi symbol (u/n) = 1 for every u, matching
Lemma 1.3), and says nothing at F2/F3 level.
(For the C-side there is no analogue: ∏_{q | 4Cp+1} (q/p)^{v_q} = ((4Cp+1)/p) = 1 always.)

### 8.8 Falsifier ledger for round 2
* (F1) Lemma 8.1/8.2 give no hit at squares (Lemma 1.3); Prop 8.7 does not apply to squares (Jacobi (u/m²) = 1 ∀u). No round-2 mechanism produces a hit, so none can produce one at a square.
* (F2) Nothing in round 2 is specific to C even or odd; nothing claims a hit for all p.
* (F3) §8.4 data: zero rates of primes and of non-square composites coprime to 105 are comparable — a warning that any
  argument using "p prime" only through non-squareness + local data must still explain the 20 coprime composite zeros
  (largest 3 210 601) by "sufficiently large".
* (F4) Prop 8.7 holds at all 14 zeros (n₂ ∈ {5, 7, 11, 13, 17, 19, 23}) and yields no hit there — consistent.
No HOT LEAD.
