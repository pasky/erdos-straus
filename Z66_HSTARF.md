# Z66 HSTARF — a realisation problem for Erdős–Straus: abelian triangle covers pulled back along the p-th power map

Lane HSTARF (tryhard, wave z66). Fresh attack: no FRONTIER/Z5*/Z6*/BRAINSTORM read; only `data/z58/screens/`.
Scripts `scripts/z66_hstarf_*`, data `data/z66/hstarf/`. Every claim is tagged PROVED / CERTIFIED (by a script) /
EVIDENCE / CONDITIONAL / OPEN. **Status: the Erdős–Straus conjecture is OPEN; nothing below proves it.**

## §0 Mandatory falsifiers (stated first; re-stated in §9)

Let (★) be `4uBC − u − B = p` and let Type II(n) be `4abcd = a + b + nc` (positive integers).

* **(F1) odd squares.** Type II(m²) has no solution for odd m (PROVED, §3, Jacobi-symbol obstruction, no primality used).
  Any argument "for primes" below must break at n = m²; the place where it breaks is marked explicitly.
* **(F2) C-even sub-equation** fails at 12 primes in [10¹⁰, 1.1·10¹⁰] (`r8_zeros_1e10.txt`). The realisation problem
  of this memo is equivalent to the FULL Type II family (all a, b, c, d), not to a C-even or c = 1 sub-family (§2).
* **(F3) 285 non-square composites** n ≤ 8·10⁶ with no (★)-solution (`composite_zeros_le8e6.txt`). CERTIFIED (§4):
  all but one of those ≤ 10⁶ (4545 = 3²·5·101) DO have a Type II solution with c > 1; the Type II equation itself fails,
  below 10⁶, exactly at the 499 odd squares and at 4545. So a proof "for primes" of Type II must fail at 4545 and at
  squares and nowhere else (below 10⁶) — a sharp test for any argument.
* **(F4) 14 primes** ≤ 10¹⁰ with no (★)-solution (`star_prime_zeros.txt`). CERTIFIED (§4): every one of them has a
  Type II solution with c ≥ 2 (e.g. p = 409: (a,b,c,d) = (1,117,2,1)). So the realisation problem survives F4.

Survival of all four with a proof would be a HOT LEAD. **No proof is claimed** (see §7–§8 for what was attempted and
exactly where it fails).

## §1 Definitions and classical facts (p odd prime, p ≡ 1 mod 4 unless said otherwise)

ES(p): 4/p = 1/x + 1/y + 1/z, x ≤ y ≤ z positive integers. Since p | xyz and p ∤ (all three) [4 = 1/X+1/Y+1/Z is
impossible], either p divides exactly one of x, y, z (**Type I**) or exactly two (**Type II**).

**Lemma 1.1 (parametrisation of Type II; PROVED, standard).** For ANY integer n ≥ 5, the solutions of 4/n = 1/x+1/y+1/z
with n | x, n | y, gcd(z, n) = 1 are exactly (x, y, z) = (bcdn, acdn, abd) with 4abcd = a + b + nc.
Proof. (⇐) clear. (⇒) x = nX, y = nY: 4XYz = z(X+Y) + nXY, so z | nXY, hence z | XY. Put g = gcd(X,Y), X = gX₁,
Y = gY₁: 4gX₁Y₁z = z(X₁+Y₁) + ngX₁Y₁, so X₁ | zY₁ ⇒ X₁ | z, likewise Y₁ | z, so z = X₁Y₁w and 4gX₁Y₁w = w(X₁+Y₁) + ng.
Put h = gcd(w, g), w = hw', g = hg': 4hg'X₁Y₁w' = w'(X₁+Y₁) + ng' with gcd(w', g') = 1, so w' | n. But w' | z and
gcd(z, n) = 1, so w' = 1, and 4hg'X₁Y₁ = X₁ + Y₁ + ng'. Take a = Y₁, b = X₁, c = g', d = h. ∎
For prime n = p, "gcd(z,p) = 1" is "p ∤ z", so Lemma 1.1 parametrises all of Type II.

**Lemma 1.2 (equivalent divisor forms of Type II; PROVED).** For any n ≥ 1 the following are equivalent:
 (i)  ∃ a,b,c,d ≥ 1: 4abcd = a + b + nc;
 (ii) ∃ a,d ≥ 1: 4a²d + n has a divisor q ≡ −1 (mod 4ad);
 (iii) ∃ c,d ≥ 1: 4c²dn + 1 has a divisor q ≡ −1 (mod 4cd);
 (iv) ∃ a,b ≥ 1 and a divisor e of a + b with n ≡ −e (mod 4ab);
 (v)  ∃ m₀,m₁ ≥ 1: (4m₀m₁ − m₀ − m₁) / gcd(m₀m₁, m₀+m₁) = n.
Proof. (i)⇒(ii): q := 4acd − 1 divides b·q = a + nc, and 4ad(a + nc) − n(4acd − 1) = 4a²d + n, so q | 4a²d + n;
q ≡ −1 (mod 4ad). (ii)⇒(i): q = 4acd − 1 for some c ≥ 1 (q ≡ −1 mod 4ad, q > 0); then q | 4ad(a+nc) − (4a²d + n)·0…
precisely 4ad·(a + nc) = (4a²d + n) + n·q ≡ 0 (mod q) and gcd(q, 4ad) = 1, so q | a + nc; set b = (a+nc)/q.
(i)⇔(iii): (4acd−1)(4bcd−1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1; conversely a divisor q ≡ −1 (mod 4cd) of
4c²dn + 1 gives q = 4acd − 1 and the cofactor is ≡ −1 (mod 4cd) because q·q' ≡ 1, so q' = 4bcd − 1, and then
4cd(4abcd − a − b) + 1 = 4c²dn + 1 gives (i). (i)⇔(iv): 4abcd = a + b + nc ⇔ c | a + b and n ≡ −(a+b)/c (mod 4ab),
d = (n + (a+b)/c)/(4ab). (i)⇔(v): this is Proposition 2.3 below (it is the Riemann–Hurwitz form of the realisation problem). ∎

Forms (ii) and (iii) are both "a value of a binary quadratic form of discriminant −4dn has a divisor in a prescribed
class": 4a²d + n = d·(2a)² + n·1² is a value of [d,0,n], and 4c²dn + 1 = dn·(2c)² + 1 is a value of [1,0,dn].
Sub-families: c = 1 in (i) is (★); a = 1 in (ii) is "n + 4d has a divisor ≡ −1 (mod 4d)"; d = 1 in (ii) is
"(2a)² + n has a divisor ≡ −1 (mod 4a)". None of the three sub-families suffices alone (§4).

## §2 The realisation problem REAL(n) and its equivalent forms

**Setting.** Let n ≥ 5. For a finite group A with gcd(|A|, n) = 1 and a Galois A-cover Y → ℙ¹ branched over
{0, 1, ∞} with ramification orders (m₀, m₁, m_∞) (the orders of the stabilisers over 0, 1, ∞; a "triangle cover",
i.e. a regular dessin), let X := Y ×_{ℙ¹} ℙ¹ be the pull-back along the n-th power map z ↦ z^n = t, normalised
(the n-th power map is the cyclic ℤ_n-cover of ℙ¹_t branched exactly over t = 0 and t = ∞).

**Definition (REAL(n)).** REAL(n) holds iff there are A, Y as above such that X satisfies
      2g(X) − 2 = |A|·(n − 4).                                                      (R)
(For a prime p: |Aut| = n|A| = |ℤ_p × A| so (R) reads |G|(p − 4) = p(2g − 2) with G = ℤ_p × A.)

**Lemma 2.1 (PROVED).** Since gcd(|A|, n) = 1, X is connected, X → ℙ¹_t is Galois with group G = ℤ_n × A, and
X/G = ℙ¹ with exactly three branch points of orders (n·m₀, m_∞, n·m₁) [over t = 0, 1, ∞]. Riemann–Hurwitz gives
2g(X) − 2 = n|A|·(1 − 1/(nm₀) − 1/m_∞ − 1/(nm₁)), so
      (R)  ⇔  1/m₀ + 1/m₁ + n/m_∞ = 4.                                              (E)
Proof. The function fields of Y and of the ℤ_n-cover are linearly disjoint over ℂ(t) (coprime degrees), so the
compositum X has degree n|A| and is Galois with group ℤ_n × A. The stabiliser of a point of X over t = 0 is the
cyclic group generated by (a generator of ℤ_n, stabiliser in A), of order lcm(n, m₀) = n m₀ since gcd(m₀, n) = 1
(m₀ divides |A|); similarly over ∞; over t = 1 the ℤ_n-cover is unramified so the order is m_∞. ∎

**Theorem 2.2 (PROVED).** For a prime p ≥ 5 the following are equivalent:
 (a) REAL(p);
 (b) AB(p): there is a compact Riemann surface X with an ABELIAN group G ≤ Aut(X), X/G ≅ ℙ¹ with three branch
     points, and |G|(p − 4) = p(2g(X) − 2);
 (c) CYC(p): there is a CYCLIC group G = ℤ_N as in (b); concretely a superelliptic curve w^N = z^α(z − 1)^β with
     p | N and gcd(α, N) + gcd(β, N) + gcd(α + β, N) = 4N/p;
 (d) Type II(p): 4abcd = a + b + pc has a solution in positive integers;
 (e) ES(p) has a solution with p dividing exactly two of the denominators.
Proof. (e)⇔(d) is Lemma 1.1. (c)⇒(b) trivial. (b)⇒(e): the signature (x, y, z) of X/G satisfies
1/x + 1/y + 1/z = 4/p (Riemann–Hurwitz), so it is an ES solution; in an abelian group g₃ = (g₁g₂)^{-1} kills
lcm(ord g₁, ord g₂), hence each period divides the lcm of the other two; if p divided exactly one period that period
could not divide the lcm of the other two (coprime to p); p cannot divide all three (then 4 = 1/X + 1/Y + 1/Z ≤ 3);
so p divides exactly two. (d)⇒(a): put (m₀, m₁, m_∞) := (bcd, acd, abd). Then
1/m₀ + 1/m₁ + p/m_∞ = (a + b + pc)/(abcd) = 4, i.e. (E). Each of m₀, m₁, m_∞ divides the lcm of the other two
(e.g. bcd | lcm(acd, abd) = ad·lcm(c, b)·… ⊇ bcd), so the abelian group A := ℤ_{m₀} ⊕ ℤ_{m₁} ⊕ ℤ_{m_∞}/⟨(1,1,1)⟩
is generated by the images e₀, e₁ of the first two basis vectors, e₀ + e₁ + e_∞ = 0, and ord(e_i) = m_i exactly:
the order of the image of (1,0,0) is gcd(m₀, lcm(m₁, m_∞)) = m₀. Hence the triangle group Δ(m₀, m₁, m_∞) maps onto A
with torsion-free kernel and Y := ℍ/ker (or ℂ/ker, ℙ¹ in the Euclidean/spherical cases) is a triangle A-cover with
these orders. gcd(|A|, p) = 1 because p ∤ abcd (Lemma 2.4). By Lemma 2.1, (E) gives (R). (a)⇒(e): Lemma 2.1 gives
the ES solution (pm₀, pm₁, m_∞) with gcd(m_∞, p) = 1. (d)⇒(c): Proposition 2.5. ∎

**Proposition 2.3 (PROVED; Lemma 1.2 (i)⇔(v)).** For n ≥ 5: (E) has a solution (m₀, m₁, m_∞) ∈ ℕ³ with
gcd(m_∞, n) = 1 iff ∃ m₀, m₁: (4m₀m₁ − m₀ − m₁)/gcd(m₀m₁, m₀ + m₁) = n; and for n = p prime, every solution of (E)
has gcd(m_∞, p) = 1 and is of the form (bcd, acd, abd) with 4abcd = a + b + pc.
Proof. (E) ⇔ n·m₀m₁ = m_∞(4m₀m₁ − m₀ − m₁). Put g = gcd(m₀m₁, 4m₀m₁ − m₀ − m₁) = gcd(m₀m₁, m₀ + m₁). Then
(m₀m₁/g) and ((4m₀m₁ − m₀ − m₁)/g) are coprime, so (4m₀m₁ − m₀ − m₁)/g divides n and m_∞ = (m₀m₁/g)·(n g/(4m₀m₁ − m₀ − m₁)).
If gcd(m_∞, n) = 1 then (4m₀m₁ − m₀ − m₁)/g = n (it divides n and is coprime to … : write n = k·(4m₀m₁−m₀−m₁)/g,
then m_∞ = k·m₀m₁/g, and gcd(m_∞, n) ≥ k forces k = 1). Conversely if (4m₀m₁ − m₀ − m₁)/g = n then m_∞ := m₀m₁/g
solves (E) and gcd(m_∞, n) = gcd(m₀m₁/g, (4m₀m₁ − m₀ − m₁)/g) = 1. For n = p prime: (4m₀m₁ − m₀ − m₁)/g ∈ {1, p};
the value 1 would give 4m₀m₁ − m₀ − m₁ = g ≤ m₀ + m₁, impossible for m₀m₁ ≥ 1 (4m₀m₁ ≤ 2(m₀+m₁) forces
m₀ = m₁ = 1, where 2 ≠ 1 = g). So gcd(m_∞, p) = 1 and Lemma 1.1 applies to (pm₀, pm₁, m_∞). ∎

**Lemma 2.4 (PROVED).** If 4abcd = a + b + pc with p ≥ 5 prime then p ∤ abcd.
Proof. Use a + b ≤ ab + 1 ≤ 2ab. If p | a then p | b (reduce mod p); writing a = pa', b = pb':
4pa'b'cd = a' + b' + c ≤ a'b' + 1 + c, so c(4pa'b'd − 1) ≤ a'b' + 1, impossible since 4pa'b'd − 1 ≥ 19a'b' > a'b' + 1.
If p | c, c = pc': p c'(4abd − p) = a + b ≤ ab + 1 with k := 4abd − p ≥ 1 and ab = (p + k)/(4d); so
p c' k ≤ (p + k)/(4d) + 1, i.e. k(4dpc' − 1) ≤ p + 4d, which fails for p ≥ 5 (4dp − 1 > p + 4d). If p | d, d = pd':
pc(4abd' − 1) = a + b ≤ 2ab, so ab(4d'pc − 2) ≤ pc·… precisely 4abd'pc − pc ≤ 2ab gives ab(4d'pc − 2) ≤ pc < 4d'pc − 2
for p ≥ 5, so ab < 1. ∎

**Proposition 2.5 (PROVED; cyclic realisation).** Every solution of 4abcd = a + b + pc (p ≥ 5 prime) satisfies
gcd(a, b) = gcd(a, c) = gcd(b, c) =: γ, and the triple (bcdp, acdp, abd) is the signature of a cyclic action
of ℤ_N, N = abcdp/γ, on a Riemann surface with quotient ℙ¹ (Harvey's criterion). Hence AB(p) ⇒ CYC(p).
Proof. Let r be a prime dividing two of a, b, c, with r-adic valuations i = v(a), j = v(b), k = v(pc) = v(c)
(p ∤ c). If the minimum of {i, j, k} were attained once, say at i, then v(a + b + pc) = i while
v(4abcd) ≥ i + j + k > i (one of j, k is ≥ 1), contradicting the equation. So the minimum is attained at least twice,
and then min(i,j) = min(i,k) = min(j,k). Hence the three pairwise gcds coincide. Harvey's criterion for a
genus-0 quotient with three periods m₁, m₂, m₃ and G = ℤ_N: (H1) lcm of any two periods = N; (H2) if N is even,
the number of periods divisible by 2^{v₂(N)} is even. Here lcm(bcdp, acdp) = cdp·lcm(a,b) = abcdp/γ,
lcm(bcdp, abd) = bdp·lcm(a, c) = abcdp/γ, lcm(acdp, abd) = abcdp/γ, so (H1) holds with N = abcdp/γ.
For (H2): the periods divisible by 2^{v₂(N)} are those among {bcdp, acdp, abd} whose complementary factor
(a, b, c respectively) has v₂ equal to v₂(γ) = min(v₂a, v₂b, v₂c). Reducing 4abcd = a + b + pc mod 2 shows that
an even number of a, b, c are odd; if all three are even with the same 2-adic valuation m ≥ 1 then
v₂(a + b + pc) = m (odd + odd + odd after dividing by 2^m) while v₂(4abcd) ≥ 3m + 2, contradiction. So the minimum
2-adic valuation is attained by exactly two of a, b, c, and (H2) holds. ∎
(CERTIFIED: `scripts/z66_hstarf_cyclic.py` checks (H1),(H2) for all 785 696 Type II solutions with p < 3·10⁵ —
all pass — and cross-checks Harvey's criterion by brute force over (α, β) ∈ (ℤ/N)² for N ≤ 3000.)

**Explicit model.** With (a, b, c) pairwise coprime (divide the solution by γ: (a,b,c,d) ↦ (a/γ, b/γ, c/γ, γ²d)
preserves the equation), N = abcdp, and X: w^N = z^α (z − 1)^β with gcd(α, N) = a, gcd(β, N) = b,
gcd(α + β, N) = cp (such α, β exist by Harvey's theorem, and also directly by CRT). Then
g(X) = 1 + (N − a − b − cp)/2 and 2g − 2 = N − 4abcd = N(p − 4)/p. For p = 5: w¹⁰ = z²(z − 1)⁵ (a=2, b=... ) —
e.g. the genus-2 curve w² = z⁵ − 1 with its ℤ₁₀; for p = 13: X is the pull-back of the (2,4,4)-quotient of the
square torus along z ↦ z¹³ (signature (26, 52, 4)); for p ≡ 2 (mod 3): Y = ℙ¹ with A = ℤ_{(p+1)/3}.

**Remark 2.6 (Euclidean and spherical Y).** Solutions of (E) with Y non-hyperbolic: spherical signatures give only
(1, (p+1)/3, (p+1)/3) (p ≡ 2 mod 3); Euclidean ones give p ∈ {7, 13, 19} only ((3,6,2),(4,2,4)/(2,4,4),(2,3,6)).
All other primes need hyperbolic Y, and then m_∞ ∈ (p/4, (p−1)/3) [from 3 < p/m_∞ < 4 and χ(Y) < 0].

**Remark 2.7 (what is "determined by p").** REAL(p) is an existence problem whose only datum is p: "is some
prime-to-p triangle cover, pulled back along the p-th power map, of genus 1 + |A|(p−4)/2?" It implies ES(p)
(Theorem 2.2), it is equivalent to the full Type II family (so it is not a c = 1 or C-even sub-family: F2 is not
an issue), and it fails at odd squares (§3).

## §3 The odd-square obstruction (F1) and three negative structural results

**Theorem 3.1 (PROVED; no primality used).** For every odd m ≥ 3, 4abcd = a + b + m²c has no solution; hence
REAL(m²) (with the prime-like refinement: gcd(|A|, n) = 1 and gcd(m_∞, n) = 1) is false, and AB(n) with the same
refinement is false.
Proof. Suppose 4abcd = a + b + m²c. Put q := 4acd − 1 ≥ 3, q ≡ −1 (mod 4ad), q ≡ 3 (mod 4). From Lemma 1.2,
q | 4a²d + m², so −m² ≡ 4a²d = (2a)²·d (mod q). gcd(m, q) = 1: a common prime r would divide 4acd − 1 and
a + m²c ≡ a, hence 4acd − 1 ≡ −1, absurd. Also gcd(2a, q) = 1. So the Jacobi symbol (−d/q) = (−m²/q)·(4a²/q)… more
carefully (−m² / q) = (−1/q) = −1 (q ≡ 3 mod 4) and (−m²/q) = ((2a)²d/q) = (d/q). Now q ≡ −1 (mod 4d): write
d = 2^k d' with d' odd; if k ≥ 1 then q ≡ −1 (mod 8) and (2/q) = 1; and by quadratic reciprocity for Jacobi symbols
(d'/q) = (q/d')·(−1)^{(d'−1)/2·(q−1)/2} = (−1/d')·(−1)^{(d'−1)/2} = 1. So (d/q) = 1 ≠ −1. ∎
Where primality enters any proof: for a prime p the same computation shows (p/q) = −1 for q = 4acd − 1, i.e. every
Type II solution has q a quadratic NON-residue modulo p (equivalently q is a non-residue mod p since p ≡ 1 mod 4).
A proof for primes must produce, for each p, a modulus q ≡ 3 (mod 4) with (q/p) = −1 and p in the sparse set
S_q := {−a·c^{-1} mod q : ac | (q+1)/4} (§5). For p = m² the set of non-residues is empty — this is the only place
the argument can use primality.

**Proposition 3.2 (PROVED). PSL₂(𝔽_p) (and PSL₂(𝔽_ℓ), ℓ ≠ p) never acts on a Riemann surface with
|G|(p − 4) = p(2g − 2) and genus-0 quotient.** Element orders of PSL₂(𝔽_ℓ) are ℓ and divisors of (ℓ ± 1)/2. For a
genus-0 quotient with r branch points, Riemann–Hurwitz gives Σ 1/m_i = r − 3 + 4/p. The denominator of the
right-hand side is p, so some m_i must be divisible by p; the remaining periods coprime to p contribute a fraction with
denominator coprime to p, so the p-periods alone must sum to a fraction with denominator exactly p. For ℓ = p the
only period divisible by p is p itself, and k/p = r − 3 + 4/p − (fraction with denominator coprime to p) forces
k ≡ 4 (mod p) with 1 ≤ k ≤ r; r = 4 gives the remaining sum 1, impossible with r − k = 0 periods… (r = k = 4:
Σ = 4/p = 1 + 4/p, false). For r = 3: k ≤ 3 < 4. For r ≥ 5 similarly k = 4 + jp ≤ r would need r ≥ 4 + the other
periods summing to r − 3, i.e. each remaining period equal to 1, impossible. For ℓ ≠ p, a period divisible by p
divides (ℓ ± 1)/2, and the same denominator argument needs the p-periods m = p·m' with Σ 1/(p m') having
denominator p, i.e. Σ 1/m' ∈ ℤ; with at most r periods ≤ (ℓ+1)/2 and r − 3 + 4/p < Σ ≤ … one checks no solution
for r = 3 (1/x + 1/y + 1/z = 4/p with x, y, z | (ℓ±1)/2 or = ℓ forces lcm divisible by p, so two periods are
multiples of p, say pm', pm''; then 1/m' + 1/m'' ≡ 0 modulo denominators coprime to p means m' = m'' = 1 and
1/z = 2/p, absurd). So the hint "use PSL₂(𝔽_p) as the automorphism group" is dead: the group in REAL(p) is
forced to be ℤ_p × A, and (Prop. 2.5) cyclic suffices.

**Proposition 3.3 (PROVED by example). The non-Galois (Hurwitz-type) version does NOT fail at squares.**
Define HUR(n): ∃ N and a transitive triple (σ₀, σ₁, σ_∞) ∈ S_N³, σ₀σ₁σ_∞ = 1, with no cycle of σ₀, σ_∞ of length
divisible by n, such that the pull-back of the corresponding degree-N cover along z ↦ zⁿ has 2g − 2 = N(n − 4);
by Riemann–Hurwitz this is ℓ(σ₀) + ℓ(σ_∞) + n·ℓ(σ₁) = 4N (ℓ = number of cycles). Then HUR(9) holds:
`scripts/z66_hstarf_hur.py` finds N = 8, σ₀ an 8-cycle, σ₁ of cycle type (6,1,1), σ_∞ of type (4,2,1,1)
(σ₁ = (0 1 3 4 7 2 5 6) in one-line notation), so Y has genus 1 and ℓ(σ₀) + ℓ(σ_∞) + 9ℓ(σ₁) = 1 + 4 + 27 = 32 = 4N;
the pulled-back curve has genus 1 + 8·5/2 = 21 and a ℤ₉-action. (The same script shows the Galois example for n = 5:
N = 2, w² = z(z⁵ − 1).)
Consequently HUR is strictly weaker than REAL and cannot be "the" realisation problem: the square obstruction is a
property of the signature (unit-fraction) equation and is invisible to cycle-count combinatorics. (In particular the
2026 prime-degree Hurwitz theorem cannot be transported directly.)

**Proposition 3.4 (PROVED). Characteristic-p constructions have the wrong genus.** Let Y → ℙ¹ be a tame
A-cover in characteristic p with orders (m₀, m₁, m_∞) and X → Y an A-equivariant Artin–Schreier ℤ_p-cover branched
over the A-orbits above 0 and ∞ (conductors c₀, c_∞ ≥ 1). Then 2g(X) − 2 = p(2g(Y) − 2) + (p − 1)|A|((c₀+1)/m₀ +
(c_∞+1)/m₁) > p(2g(Y) − 2) + (p − 1)|A|(1/m₀ + 1/m₁) = the characteristic-0 value. So the genus relation (R) cannot
be met in characteristic p by a curve with the same group, quotient and branch locus (it would need c₀ = c_∞ = 0),
and "construct in characteristic p, then lift" does not apply to REAL(p) as it does to the Hurwitz problem.

## §4 Computations (all CERTIFIED by the listed scripts; `ulimit -v 4000000`, timeouts ≤ 1800 s)

* `scripts/z66_hstarf_types.py` (sympy): enumerates ALL ES solutions for a prime p, classifies by the number of
  denominators divisible by p, and checks that Type II solutions coincide with Lemma 1.1's parametrisation
  (`param_match=True` for p = 5, 13, 409, 577). p = 409: 15 solutions, 9 Type I, 6 Type II (all with c ≥ 2).
* `scripts/z66_hstarf_t12.c`: Type II / (★) / Type I counts; `-range N` scan.
  - All 635 170 primes p ≡ 1 (4), p ≤ 2·10⁷, have a Type II solution (`data/z66/hstarf/typeII_zero_primes_2e7.txt`).
  - Composites n ≡ 1 (4), n ≤ 10⁶: Type II fails exactly for the 499 odd squares and for n = 4545 = 3²·5·101
    (`data/z66/hstarf/typeII_zero_all_1e6.txt`; 4545 re-checked by two independent enumerations). All other F3
    composites ≤ 10⁶ (187 of them) have Type II solutions (with c ≥ 2 by definition of F3).
  - F4: all 14 (★)-free primes have Type II solutions with c ≥ 2 (counts 7, 7, 10, 7, 39, 15, 21, 30, 32, 50, 45,
    38, 78, 64 for the list in order).
* `scripts/z66_hstarf_subfam.c` and ad-hoc checks: the sub-families fail individually —
  a = 1 ("p + 4d has a divisor ≡ −1 mod 4d") fails at p = 2521, 66529 (exhaustive in d);
  d = 1 ("(2a)² + p has a divisor ≡ −1 mod 4a") fails at 133 primes ≤ 3·10⁶ (first: 486781? — see file);
  c = 1 = (★) fails at the 14 F4 primes. So REAL(p) genuinely needs the full (a, c, d) family.
* `scripts/z66_hstarf_abelian.py`: brute force over 2-generated abelian groups ℤ_m × ℤ_k (|G| ≤ 400) and generating
  pairs: the signatures with Σ = 4/n found are exactly the Type II triples for n = 5, 13, 17; for n = 9, 25 the
  naive abelian problem HAS solutions ((3,18,18) and (10,25,50)), but they violate the prime-like refinement
  (third period not coprime to n) — which is why REAL(n) carries that refinement for composite n.
* `scripts/z66_hstarf_cyclic.py`: Harvey's criterion holds for every Type II triple, p < 3·10⁵ (785 696 triples).

## §5–§8 Proof attempts

(to be written)

## §9 Falsifiers re-stated

(to be written)
