# Z58 CONVF — tryhard lane: 4abcd = a + b + nc for all large primes p ≡ 1 (mod 24)

Status: NO PROOF (ES is open). This memo records (i) exact reformulations (PROVED), (ii) the obstruction that any proof
must pass (PROVED), (iii) new certified sub-family data, (iv) the attack lines tried and the precise step where each dies.
Scripts: `scripts/z58_convf_*`; data: `data/z58/convf/`.

## §0 Mandatory falsifiers (stated at first commit; re-checked in §6)

* **F1 (odd squares n = m²).** Every witness f = 4acd − 1 satisfies (n/f) = −1 (Lemma 1.3), so no argument that only
  uses n (mod f) can work; the step that uses non-squareness must be the one producing an f with (n/f) = −1.
* **F2 (d-even half, numerator 8).** Restricting to d even is the statement 8abcd' = a + b + nc; it has 22 prime zeros
  ≤ 10⁹ (last 35 569). An argument is only credible if the restriction "d even" visibly breaks it (e.g. it must use
  d = 1 or d odd somewhere, or the a = 1 / c = 1 sub-families with d odd).
* **F3 (4545 and the 285 composite c = 1 zeros ≤ 8·10⁶).** 4545 = 3²·5·101 ≡ 9 (mod 24); the composite c = 1 zeros are
  ≡ 1 or 9 (mod 24) (71 resp. 214 of them). Any argument that works for all n ≡ 1 (mod 24) non-square must fail at the
  71 composite c = 1 zeros ≡ 1 (24) if it only uses the c = 1 line, and must not apply to 4545 at all (threshold or
  a step using primality/non-divisibility by 9).
* **F4 (the 14 primes ≤ 10¹⁰ with no c = 1 witness).** 409 … 8 813 281. Any argument confined to c = 1 is false there.
  All 14 have witnesses with a = 1, c ∈ {2, 3} (data/z58/convf/wit_hard.txt), so an argument confined to a = 1 is
  consistent with them — but a = 1 alone has its own zeros {193, 2521, 66529}.

## §1 Exact reformulations and the obstruction (all PROVED)

Throughout n is an odd positive integer (the target is n = p prime ≡ 1 (mod 24)); a, b, c, d range over positive integers.
R(n) := #{(a,b,c,d) : 4abcd = a + b + nc}. A quadruple with 4abcd = a + b + nc gives
4/n = 1/(abd) + 1/(acdn) + 1/(bcdn) (multiply out: (cn + b + a)/(abcdn) = 4/n). This is the Elsholtz–Tao Type II family
(their Prop. 2.7; the residue-class form below is their Prop. 1.9).

**Lemma 1.1 (equivalent forms).** For fixed n the following sets are in explicit bijection; in particular R(n) > 0 iff any
one of them is non-empty.
 (E1) {(a,b,c,d) : 4abcd = a + b + nc}.
 (E2) {(a,c,d,f) : f = 4acd − 1, f | cn + a}.
 (E3) {(a,d,f) : f ≡ −1 (mod 4ad), f | n + 4a²d}.
 (E4) {(c,d,f) : f ≡ −1 (mod 4cd), f | 4c²dn + 1}.
 (E5) {(a,b,σ) : σ | a + b, 4ab | n + σ}.
 (E6) {(σ,c,d,t) : σ ≡ 3 (4), c,d ≥ 1, t ∈ ℤ, |t| < cσ, t ≡ cσ (mod 2), n = d(c²σ² − t²) − σ}.
*Proof.* (E1)⇒(E2): b(4acd − 1) = cn + a, so f := 4acd − 1 divides cn + a (and b = (cn+a)/f). (E2)⇒(E1): b := (cn+a)/f ≥ 1 and
4abcd = b(f + 1) = cn + a + b. (E2)⇔(E3): f = 4acd − 1 ≡ −1 (mod 4ad) and conversely any f ≡ −1 (mod 4ad), f > 0, is
4acd − 1 with c = (f+1)/(4ad) ≥ 1. Since 4acd ≡ 1 (mod f): multiplying cn + a by 4ad gives 4acd·n + 4a²d ≡ n + 4a²d, and
multiplying n + 4a²d by c gives cn + a·(4acd) ≡ cn + a; as gcd(c, f) = gcd(4ad, f) = 1, f | cn + a ⇔ f | n + 4a²d.
(E2)⇔(E4): similarly 4c²dn + 1 ≡ 4c²dn + (4acd)² ·… — directly: c·(4c²dn + 1)·? — use instead: with b = (cn+a)/f,
(4acd − 1)(4bcd − 1) = 16abc²d² − 4cd(a + b) + 1 = 4cd(4abcd − a − b) + 1 = 4c²dn + 1, so f | 4c²dn + 1; conversely if
f ≡ −1 (mod 4cd) divides 4c²dn + 1, write f = 4acd − 1, g = (4c²dn+1)/f; then g ≡ −1 (mod 4cd) because fg ≡ 1 and f ≡ −1,
so g = 4bcd − 1 and expanding gives 4abcd = a + b + nc. (E1)⇔(E5): from 4abcd = a + b + nc, c | a + b; put σ = (a+b)/c;
then n + σ = 4abd, so 4ab | n + σ and σ | a + b. Conversely given (a,b,σ), put d = (n+σ)/(4ab), c = (a+b)/σ. (E5)⇔(E6):
with s = a + b = cσ, t = a − b, 4ab = s² − t², so n = d(c²σ² − t²) − σ; conversely a = (cσ + t)/2, b = (cσ − t)/2 are
positive integers iff |t| < cσ and t ≡ cσ (2); σ ≡ 3 (4) is forced when n ≡ 1 (4) since c²σ² − t² ≡ 0 (4). ∎

**Lemma 1.2 (sub-lines).** In the notation of (E1)–(E4):
 (c = 1) ⇔ ∃ a: n + a has a divisor ≡ −1 (mod 4a) ⇔ ∃ d: 4dn + 1 = (4ad − 1)(4bd − 1) ⇔ ∃ d: 4dn + 1 has a divisor ≡ −1 (4d).
 (a = 1) ⇔ ∃ c: cn + 1 has a divisor ≡ −1 (mod 4c) ⇔ ∃ d: n + 4d has a divisor ≡ −1 (mod 4d).
 (d = 1) ⇔ ∃ a: n + 4a² has a divisor ≡ −1 (mod 4a) ⇔ ∃ σ ≡ 3 (4), c ≥ 1: c²σ² − σ − n is a perfect square.
 (c = d = 1) ⇔ 4n + 1 has a prime factor ≡ 3 (mod 4). (a = c = 1) ⇔ n + 1 has a prime factor ≡ 3 (4).
 (a = d = 1) ⇔ n + 4 has a prime factor ≡ 3 (4). (a = b) never occurs for n prime ≡ 1 (4).
*Proof.* Specialise Lemma 1.1; for c = 1 use that 4ad − 1 | n + a ⇔ 4ad − 1 | n + 4a²d (as 4a²d ≡ a). For the last three:
a number ≡ 1 (4) has a divisor ≡ 3 (4) iff it has a prime factor ≡ 3 (4). For a = b: 4a²cd = 2a + nc gives a | nc, and
with a ≤ b the bound f ≤ g in (E4) forces 4a²d ≤ n + 2a/c, so a < n, hence (n prime) a | c; write c = ae: 4a²de = 2 + ne,
so e | 2, e ∈ {1,2}: 4a²d = 2 + n or 2a²d = 1 + n, both impossible mod 4 for n ≡ 1 (4). ∎

**Lemma 1.3 (Jacobi obstruction = falsifier F1).** If (a,d,f) ∈ (E3) and gcd(f, n) = 1 (automatic for n prime > f, and
for f | n + 4a²d with gcd(n, 2ad) = 1 one has gcd(f,n) | 4a²d, so gcd(f,n) = 1 whenever gcd(n, ad) = 1), then the Jacobi
symbol (n/f) = −1. Consequently R(m²) = 0 for every odd m, and any proof must contain a step that produces an f with
(n/f) = −1, i.e. must use non-squareness of n.
*Proof.* f ≡ −1 (mod 4ad) gives f ≡ 3 (4), so (−1/f) = −1. Write d = 2^e d' with d' odd. By Jacobi reciprocity, since
f ≡ 3 (4): (d'/f)(f/d') = (−1)^{(d'−1)/2}; and f ≡ −1 (mod d') gives (f/d') = (−1/d') = (−1)^{(d'−1)/2}; so (d'/f) = 1.
If e ≥ 1 then f ≡ −1 (mod 8), so (2/f) = 1. Hence (d/f) = 1, and n ≡ −4a²d (mod f) gives (n/f) = (−1/f)(d/f) = −1. For
n = m² the symbol (m²/f) = 1 (gcd(m,f) = 1 as gcd(f,n) = 1), contradiction, so (E3) is empty. ∎

**Lemma 1.4 (no finite covering).** For every finite set F of triples (a,c,d), there are infinitely many primes p ≡ 1 (24)
for which no (a,c,d) ∈ F is a witness. Hence no Mordell-type argument (finitely many residue classes) can finish.
*Proof.* (a,c,d) is a witness for n iff n ≡ −4a²d (mod f), f = 4acd − 1 (Lemma 1.1). Let M = 24·∏_{F} f. Primes p ≡ 1
(mod M) exist in infinity (Dirichlet); for such p, p ≡ 1 is a square mod each f, while −4a²d is a non-square mod f
(Lemma 1.3's computation gives (−4a²d/f) = −1), so p is in none of the classes. ∎

**Lemma 1.5 (necessary conditions for failure).** If R(n) = 0 then for every (a,d): n + 4a²d has no divisor ≡ −1 (mod 4ad);
in particular no prime factor q ≡ −1 (mod 4ad). For n = p ≡ 1 (24) prime this gives e.g.: (p+1)/2, p + 4, 4p + 1 are
products of primes ≡ 1 (4); p + 2 and 2p + 1 are products of primes ≡ 1, 3 (8); (p+3)/4 is a product of primes ≡ 1, 7 (12);
each of p + 8, p + 16, 8p + 1 is a product of primes all ≡ 1,3 (8) or all ≡ 1,5 (8).
*Proof.* First sentence: Lemma 1.1 (E3). The listed cases are (a,d) ∈ {(1,1), (1,2), (2,1)} and the c = 1 / a = 1 forms of
Lemma 1.2 with modulus q ∈ {4, 8, 12}: a number N with N ≡ r (mod q) and prime factors in (ℤ/q)^× has a divisor ≡ −1
iff some sub-multiset of its prime factors has product −1; for q = 8 (N ≡ 3) this happens iff some prime is ≡ 7 or both a
3 and a 5 occur, and the product being 3 then forces "all in {1,3}"; for q = 8, N ≡ 1 it forces all in {1,3} or all in
{1,5}; for q = 12 (N = (p+3)/4 ≡ 1 (6)) it forces all in {1,5} or all in {1,7}, and (p+3)/4 having no prime factor ≡ 2 (3)
(the σ = 3 case of (E5): M = (p+3)/4 = abd with 3 | a + b is possible iff M has a prime factor ≡ 2 (3), since M ≡ 1 (3))
removes {1,5}. ∎

Remark. Lemma 1.5 is only necessary: "no sub-multiset product ≡ −1" is weaker than "all prime factors in a subgroup
avoiding −1" (e.g. 16p + 1 = q₁q₂ with q₁ ≡ 3, q₂ ≡ 7 (16) has no divisor ≡ 15 (16)). Every condition in Lemma 1.5 holds
automatically at odd squares n = m² (m² + 4 = N(m + 2i), 4m² + 1 = N(2m + i), m² + 3 = N(m + √−3), …), consistent with
Lemma 1.3–1.4: no finite list of such conditions can be contradictory.

## §2 Certified data (scripts/z58_convf_sieve.c, z58_convf_wit.c; data/z58/convf/)

Sieve of all (a,c,d,B) with n = B(4acd − 1) − 4a²d ≤ N, 4a²d ≤ N + 2a (this enumerates every solution with a ≤ b at least
once, cf. Lemma 1.2's bound), tagging each n by the sub-lines hit. N = 10⁸ (23 s at 2·10⁷, ~3 min at 10⁸):

| sub-line | prime zeros ≤ 10⁸ (p ≡ 1 mod 4, non-square) |
|---|---|
| full R(n) | none among primes; non-square composite zeros: only 4545 |
| c = 1 only | 14 (the known list; 8 813 281 is the last ≤ 10¹⁰ per screens) |
| c ≤ 2 | 2: 102001, 8813281 |
| c ≤ 3 | **0** |
| a = 1 only | **3: 193, 2521, 66529** |
| a = 1 or c = 1 | **0** |
| d = 1 only | 203 |

So the a = 1 line (∃ d: p + 4d has a divisor ≡ −1 (mod 4d)) is, empirically, much stronger than the c = 1 line (3 vs 14
zeros), and the union a = 1 ∪ c = 1 has no zero ≤ 10⁸. All 14 c = 1 zeros have a witness with a = 1 and c ∈ {2,3}
(wit_hard.txt). These are EVIDENCE only; heuristically each sub-line has ≍ log² p expected solutions and finitely many zeros.
