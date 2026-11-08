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
  all of those ≤ 5 285 401 except 4545 = 3²·5·101 DO have a Type II solution with c > 1; the Type II equation itself
  fails, for n ≡ 1 (4), n ≤ 5 285 401, exactly at the odd squares and at 4545. (For composite n the equation is only
  the arithmetic content of REAL(n) up to the side condition gcd(abcd, n) = 1 — e.g. Type II(105) holds via
  (3,9,4,1) but REAL(105) fails; for primes there is no such gap, Lemma 2.4.) So a proof "for primes" of Type II must fail at 4545 and at
  squares — a sharp test for any argument (it need not succeed at every composite where Type II happens to hold).
* **(F4) 14 primes** ≤ 10¹⁰ with no (★)-solution (`star_prime_zeros.txt`) **and the 38 primes with R_𝔊*(p) = 0**
  (`gstar_zeros.txt`). CERTIFIED (§4): every one of the 14 has a Type II solution with c ≥ 2 (e.g. p = 409:
  (a,b,c,d) = (1,117,2,1)); every one of the 38 has a Type II witness (`data/z66/hstarf/gstar38_typeII.txt`, e.g.
  37: (1,5,2,2); 157: (1,45,2,1); 564661441: (3,49100995,2,1)); the 12 F2 primes too (`r8_12_typeII.txt`, e.g.
  10156800001: (1,2770036364,3,1)). So the realisation problem survives F2 and F4 (for primes, gcd(abcd,p) = 1 is
  automatic, Lemma 2.4, so these are REAL witnesses).

Survival of all four with a proof would be a HOT LEAD. **No proof is claimed** (see §7–§8 for what was attempted and
exactly where it fails).

## §1 Definitions and classical facts (p odd prime, p ≡ 1 mod 4 unless said otherwise)

ES(p): 4/p = 1/x + 1/y + 1/z, x ≤ y ≤ z positive integers. Since p | xyz and p ∤ (all three) [4 = 1/X+1/Y+1/Z is
impossible], either p divides exactly one of x, y, z (**Type I**) or exactly two (**Type II**).

**Lemma 1.1 (parametrisation of Type II; PROVED, standard).** For ANY integer n ≥ 5, the solutions of 4/n = 1/x+1/y+1/z
with n | x, n | y, gcd(z, n) = 1 are exactly (x, y, z) = (bcdn, acdn, abd) with 4abcd = a + b + nc AND gcd(abd, n) = 1.
For n = p prime the side condition is automatic (Lemma 2.4).
Proof. (⇐) clear (the side condition gives gcd(z, n) = 1). (⇒) x = nX, y = nY: 4XYz = z(X+Y) + nXY, so z | nXY, hence z | XY. Put g = gcd(X,Y), X = gX₁,
Y = gY₁: 4gX₁Y₁z = z(X₁+Y₁) + ngX₁Y₁, so X₁ | zY₁ ⇒ X₁ | z, likewise Y₁ | z, so z = X₁Y₁w and 4gX₁Y₁w = w(X₁+Y₁) + ng.
Put h = gcd(w, g), w = hw', g = hg': 4hg'X₁Y₁w' = w'(X₁+Y₁) + ng' with gcd(w', g') = 1, so w' | n. But w' | z and
gcd(z, n) = 1, so w' = 1, and 4hg'X₁Y₁ = X₁ + Y₁ + ng'. Take a = Y₁, b = X₁, c = g', d = h. ∎
For prime n = p, "gcd(z,p) = 1" is "p ∤ z", so Lemma 1.1 parametrises all of Type II.

**Lemma 1.2 (equivalent divisor forms of Type II; PROVED).** For any n ≥ 1, (i)–(iv) below are equivalent; (v) is
equivalent to (i) with the extra condition gcd(abd, n) = 1 (automatic for prime n by Lemma 2.4; for composite n
(i) can hold while (v) fails, e.g. n = 6, (a,b,c,d) = (1,1,1,2)):
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
d = (n + (a+b)/c)/(4ab). (i)+[gcd(abd,n)=1] ⇔ (v): Proposition 2.3 below, via (E) with gcd(m_∞, n) = 1 and Lemma 1.1. ∎

Forms (ii) and (iii) are both "a value of a binary quadratic form of discriminant −4dn has a divisor in a prescribed
class": 4a²d + n = d·(2a)² + n·1² is a value of [d,0,n], and 4c²dn + 1 = dn·(2c)² + 1 is a value of [1,0,dn].
Sub-families: c = 1 in (i) is (★); a = 1 in (ii) is "n + 4d has a divisor ≡ −1 (mod 4d)"; d = 1 in (ii) is
"(2a)² + n has a divisor ≡ −1 (mod 4a)". None of the three sub-families suffices alone (§4).

## §2 The realisation problem REAL(n) and its equivalent forms

**Setting.** Let n ≥ 5. For a finite group A with gcd(|A|, n) = 1 and a Galois A-cover Y → ℙ¹ branched over
{0, 1, ∞} with ramification orders (m₀, m₁, m_∞) (the orders of the stabilisers over 0, 1, ∞; a "triangle cover",
i.e. a regular dessin), let X := Y ×_{ℙ¹} ℙ¹ be the pull-back (normalised) along the cyclic ℤ_n-cover π_n: ℙ¹ → ℙ¹_t of degree n
branched exactly over t = 0 and t = 1 (e.g. t = z^n/(z^n − 1), the n-th power map followed by a Möbius map;
π_n is unramified over t = ∞).

**Definition (REAL(n)).** REAL(n) holds iff there are A, Y as above such that X satisfies
      2g(X) − 2 = |A|·(n − 4).                                                      (R)
(For a prime p: |G| = n|A| = |ℤ_p × A| for the group G = ℤ_p × A acting on X, so (R) reads |G|(p − 4) = p(2g − 2);
G need not be the full Aut(X).)

**Lemma 2.1 (PROVED).** Since gcd(|A|, n) = 1, X is connected, X → ℙ¹_t is Galois with group G = ℤ_n × A, and
X/G = ℙ¹ with exactly three branch points of orders (n·m₀, n·m₁, m_∞) [over t = 0, 1, ∞]. Riemann–Hurwitz gives
2g(X) − 2 = n|A|·(1 − 1/(nm₀) − 1/(nm₁) − 1/m_∞), so
      (R)  ⇔  1/m₀ + 1/m₁ + n/m_∞ = 4.                                              (E)
Proof. The function fields of Y and of the ℤ_n-cover are linearly disjoint over ℂ(t) (coprime degrees), so the
compositum X has degree n|A| and is Galois with group ℤ_n × A. The stabiliser of a point of X over t = 0 is the
cyclic group generated by (a generator of ℤ_n, stabiliser in A), of order lcm(n, m₀) = n m₀ since gcd(m₀, n) = 1
(m₀ divides |A|); similarly n·m₁ over t = 1; over t = ∞ the cover π_n is unramified so the order is m_∞. ∎

**Theorem 2.2 (PROVED).** For a prime p ≥ 5 the following are equivalent:
 (a) REAL(p);
 (b) AB(p): there is a compact Riemann surface X with an ABELIAN group G ≤ Aut(X), X/G ≅ ℙ¹ with three branch
     points, and |G|(p − 4) = p(2g(X) − 2);
 (c) CYC(p): there is a CYCLIC group G = ℤ_N as in (b); concretely a superelliptic curve w^N = z^α(z − 1)^β with
     p | N, gcd(α, β, N) = 1 (connectedness) and gcd(α, N) + gcd(β, N) + gcd(α + β, N) = 4N/p;
 (d) Type II(p): 4abcd = a + b + pc has a solution in positive integers;
 (e) ES(p) has a solution with p dividing exactly two of the denominators.
Proof. (e)⇔(d) is Lemma 1.1. (c)⇒(b) trivial. (b)⇒(e): the signature (x, y, z) of X/G satisfies
1/x + 1/y + 1/z = 4/p (Riemann–Hurwitz), so it is an ES solution; in an abelian group g₃ = (g₁g₂)^{-1} kills
lcm(ord g₁, ord g₂), hence each period divides the lcm of the other two; if p divided exactly one period that period
could not divide the lcm of the other two (coprime to p); p cannot divide all three (then 4 = 1/X + 1/Y + 1/Z ≤ 3);
so p divides exactly two. (d)⇒(a): put (m₀, m₁, m_∞) := (bcd, acd, abd). Then
1/m₀ + 1/m₁ + p/m_∞ = (a + b + pc)/(abcd) = 4, i.e. (E). Each of m₀, m₁, m_∞ divides the lcm of the other two:
bcd | lcm(acd, abd) = ad·lcm(b, c) ⇔ gcd(b, c) | a, and similarly acd | lcm(bcd, abd) ⇔ gcd(a, c) | b,
abd | lcm(bcd, acd) ⇔ gcd(a, b) | c; all three hold because gcd(a,b) = gcd(a,c) = gcd(b,c) (first assertion of
Prop. 2.5, whose proof is independent of this theorem). So the abelian group A := ℤ_{m₀} ⊕ ℤ_{m₁} ⊕ ℤ_{m_∞}/⟨(1,1,1)⟩
is generated by the images e₀, e₁ of the first two basis vectors, e₀ + e₁ + e_∞ = 0, and ord(e_i) = m_i exactly:
the order of the image of (1,0,0) is gcd(m₀, lcm(m₁, m_∞)) = m₀. Hence the triangle group Δ(m₀, m₁, m_∞) maps onto A
with torsion-free kernel and Y := ℍ/ker (or ℂ/ker, ℙ¹ in the Euclidean/spherical cases) is a triangle A-cover with
these orders. gcd(|A|, p) = 1 because p ∤ abcd (Lemma 2.4). By Lemma 2.1, (E) gives (R). (a)⇒(e): Lemma 2.1 gives
the ES solution (pm₀, pm₁, m_∞) with gcd(m_∞, p) = 1 (m_∞ divides |A|). (d)⇒(c): Proposition 2.5. ∎

**Proposition 2.3 (PROVED; Lemma 1.2 (v)).** For n ≥ 5: (E) has a solution (m₀, m₁, m_∞) ∈ ℕ³ with
gcd(m_∞, n) = 1 iff ∃ m₀, m₁: (4m₀m₁ − m₀ − m₁)/gcd(m₀m₁, m₀ + m₁) = n; and for n = p prime, every solution of (E)
has gcd(m_∞, p) = 1 and is of the form (bcd, acd, abd) with 4abcd = a + b + pc. [For composite n, REAL(n) ⇔
4abcd = a + b + nc has a solution with gcd(abcd, n) = 1, by Lemma 1.1 and the construction in Theorem 2.2; this
is stronger than the bare equation.]
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
(CERTIFIED: `scripts/z66_hstarf_cyclic.py --all` checks (H1),(H2) for EVERY Type II solution with p < 10⁵
(217 781 solutions, all pass; an earlier ad-hoc run did the same for p < 3·10⁵, 785 696 solutions), and for the
selected signature of each prime with N ≤ 3000 it confirms by brute force over (α, β) ∈ (ℤ/N)² that ℤ_N really
realises it.)

**Explicit model.** With (a, b, c) pairwise coprime (divide the solution by γ: (a,b,c,d) ↦ (a/γ, b/γ, c/γ, γ²d)
preserves the equation), N = abcdp, and X: w^N = z^α (z − 1)^β with gcd(α, N) = a, gcd(β, N) = b,
gcd(α + β, N) = cp (such α, β exist by Harvey's theorem, and also directly by CRT). Then
g(X) = 1 + (N − a − b − cp)/2 and 2g − 2 = N − 4abcd = N(p − 4)/p. For p = 5, (a,b,c,d) = (1,2,1,1): N = 10, gcds (1, 2, 5), e.g. w¹⁰ = z(z − 1)⁴,
genus 1 + (10 − 1 − 2 − 5)/2 = 2 (a hyperelliptic genus-2 curve with a ℤ₁₀ of automorphisms); for p = 13: X is the pull-back of the (2,4,4)-quotient of the
square torus along z ↦ z¹³ (signature (26, 52, 4)); for p ≡ 2 (mod 3): Y = ℙ¹ with A = ℤ_{(p+1)/3}.

**Remark 2.6 (Euclidean and spherical Y).** Solutions of (E) with Y non-hyperbolic: spherical signatures give only
(1, (p+1)/3, (p+1)/3) (p ≡ 2 mod 3); Euclidean ones give p ∈ {7, 13, 19} only ((3,6,2) and (4,4,2) for p = 7; (4,2,4)/(2,4,4) for 13; (2,3,6) for 19).
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
S_q := {−a·c^{-1} mod q : ac | (q+1)/4} (§5). For p = m² the set of non-residues is empty. A non-trivial Jacobi character
(·/p) is thus necessary input for any proof; it need not be the only use of primality.

**Proposition 3.2 (PROVED). PSL₂(𝔽_p) never acts on a Riemann surface with |G|(p − 4) = p(2g − 2) and genus-0
quotient** (any number r of branch points). Proof. The only element order of PSL₂(𝔽_p) divisible by p is p itself.
Riemann–Hurwitz for a genus-0 quotient with periods m₁, …, m_r reads Σ 1/m_i = r − 3 + 4/p. Let k be the number of
periods equal to p; the other r − k periods are coprime to p, so k/p ≡ 4/p modulo fractions with denominator coprime
to p, i.e. k = 4 + jp with j ≥ 0. The remaining periods are ≥ 2, so r − 3 − j = Σ_{m_i ≠ p} 1/m_i ≤ (r − 4 − jp)/2,
i.e. r ≤ 2 − j(p − 2), impossible for r ≥ 3. ∎
**Caveat (found by the hostile check, which falsified a stronger claim in an earlier draft): for ℓ ≠ p the group
PSL₂(𝔽_ℓ) CAN act with such a signature** — e.g. PSL₂(𝔽₁₉) is generated by x = [[0,1],[18,0]], y = [[1,1],[12,13]]
of orders 2, 5 with xy of order 10, signature (2, 5, 10), Σ = 4/5, genus 343 (certified by exhaustive multiplication
in the review). Moreover non-abelian groups can realise Type I signatures, which no abelian group can: PSL₂(𝔽₄₁)
with x = [[0,1],[40,0]], y = [[0,6],[34,17]] has signature (2, 4, 20), Σ = 4/5, genus 3445, and 20 ∤ lcm(2, 4)
(second review pass; both examples re-verified by `scripts/z66_hstarf_psl2.py`: orders and full generation by BFS). So the *signature* of a general action with |G|(p − 4) = p(2g − 2) is an ES triple of Type I
or II; a signature admits an abelian (equivalently cyclic) realisation iff it is Type II (Theorem 2.2) — abelian ⇒
Type II, but non-abelian actions can be Type II too (PSL₂(𝔽₁₉) above). The
existence question is in every case the Diophantine one; Dickson's classification of subgroups is never needed.
(Outlook, not pursued: a non-abelian realisation problem — e.g. groups ℤ_p ⋊ A or PSL₂(𝔽_ℓ) with ℓ ≡ ±1 (mod p) —
could capture Type I as well and thus be equivalent to full ES(p); its square-failure property would then be lost.)

**Proposition 3.3 (PROVED by example). The non-Galois (Hurwitz-type) version does NOT fail at squares.**
Define HUR(n): ∃ N with gcd(N, n) = 1 and a transitive triple (σ₀, σ₁, σ_∞) ∈ S_N³, σ₀σ₁σ_∞ = 1, with every cycle
of σ₀ and of σ_∞ of length coprime to n, such that the pull-back of the corresponding degree-N cover along π_n
(the two branch values of π_n placed at the branch points of σ₀ and σ_∞, the third at that of σ₁ — a relabelling of
the Setting's t = 0, 1, ∞) has 2g − 2 = N(n − 4). The pull-back is connected (coprime degrees ⇒ linearly
disjoint function fields), the monodromy of σ₀^n has as many cycles as σ₀ when all cycle lengths are coprime to n,
and Riemann–Hurwitz gives ℓ(σ₀) + ℓ(σ_∞) + n·ℓ(σ₁) = 4N (ℓ = number of cycles). Then HUR(9) holds:
`scripts/z66_hstarf_hur.py` finds N = 8, σ₀ an 8-cycle, σ₁ of cycle type (6,1,1), σ_∞ of type (4,2,1,1)
(σ₁ = (0 1 3 4 7 2 5 6) in one-line notation; all cycle lengths 8, 4, 2, 1 of σ₀, σ_∞ are coprime to 9 and gcd(8, 9) = 1),
so Y has genus 1 and ℓ(σ₀) + ℓ(σ_∞) + 9ℓ(σ₁) = 1 + 4 + 27 = 32 = 4N;
the pulled-back curve has genus 1 + 8·5/2 = 21 and a ℤ₉-action. (The same script shows the Galois example for n = 5:
N = 2, w² = z(z⁵ − 1).)
Consequently HUR (this relaxed cycle-count condition) is strictly weaker than REAL and cannot be "the" realisation
problem: the square obstruction is a property of the signature (unit-fraction) equation and is invisible to this
cycle-count condition (other Hurwitz-type formulations were not examined). (In particular the
2026 prime-degree Hurwitz theorem cannot be transported directly.)

**Proposition 3.4 (PROVED). Characteristic-p constructions have the wrong genus.** Let Y → ℙ¹ be a tame
A-cover in characteristic p with orders (m₀, m₁, m_∞) over t = 0, 1, ∞ and X → Y an A-equivariant Artin–Schreier
ℤ_p-cover branched over the A-orbits above t = 0 and t = 1 (conductors c₀, c₁ ≥ 1). Then 2g(X) − 2 = p(2g(Y) − 2) +
(p − 1)|A|((c₀+1)/m₀ + (c₁+1)/m₁) > p(2g(Y) − 2) + (p − 1)|A|(1/m₀ + 1/m₁) = the characteristic-0 value. So for a FIXED tame signature
(m₀, m₁, m_∞) satisfying (E), the characteristic-p curve with the same group, quotient and branch locus has strictly
larger genus than the characteristic-0 target (it would need c₀ = c₁ = 0). This rules out the naive transport "same
data in characteristic p, then lift"; it does not exclude other characteristic-p constructions with different
ramification data, which were not explored.

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
    38, 78, 64 for the list in order); all 38 𝔊*-zero primes and all 12 F2 primes have a Type II witness
    (`t12 -first`, files `gstar38_typeII.txt`, `r8_12_typeII.txt`, each line re-checks 4abcd = a + b + pc).
* `scripts/z66_hstarf_subfam.c` and ad-hoc checks: the sub-families fail individually —
  a = 1 ("p + 4d has a divisor ≡ −1 mod 4d") fails at p = 193, 2521, 66529 (exhaustive: d ≤ (p+2)/4 suffices since
  for larger d the only candidate divisor is 4d − 1 | p + 1; the `subfam` scan with d ≤ 3000 missed 193 only because
  of its cap; `scripts/z66_hstarf_a1.c` is the exhaustive check, confirming 193, 2521, 66529);
  d = 1 ("(2a)² + p has a divisor ≡ −1 mod 4a") fails at 133 primes ≤ 3·10⁶, the first being p = 13 (exhaustive
  bound a ≤ √((p+2a)/4), i.e. a ≤ 867 for p ≤ 3·10⁶);
  c = 1 = (★) fails at the 14 F4 primes. So none of the three one-parameter sub-families suffices alone (their
  union, or some other proper sub-family, might — not tested beyond §4's depth statistic).
* `scripts/z66_hstarf_abelian.py`: brute force over 2-generated abelian groups ℤ_m × ℤ_k (|G| ≤ 400) and generating
  pairs: the signatures with Σ = 4/n found are exactly the Type II triples for n = 5, 13, 17; for n = 9, 25 the
  naive abelian problem HAS solutions ((3,18,18) and (10,25,50)), but they violate the prime-like refinement
  (third period not coprime to n) — which is why REAL(n) carries that refinement for composite n.
* `scripts/z66_hstarf_cyclic.py --all`: Harvey's criterion holds for every Type II triple (count printed by the
  script; `data/z66/hstarf/cyclic_all_1e5.txt`); brute-force realisation check for N ≤ 3000 passes.
* `scripts/z66_hstarf_jacobi.py`: (ab/p) = (q₁/p) = (jd/p) = −1 on all 31 745 Type II solutions with p ≤ 2·10⁴
  (Prop. 5.2); the c = 1 mirror sub-equation 4abm + a + b = p has no solution for 7 primes ≤ 2·10⁴ (5, 13, 17, 97, …).
* `scripts/z66_hstarf_depth.c` (`data/z66/hstarf/depth_2e6.txt`, `depth_1e8.txt`): for EVERY prime p ≡ 1 (4),
  p ≤ 10⁸ (2 880 504 primes), the Type II solution with the smallest product m = ad has m ≤ 25; the records are
  m = 1 (p = 5), 2 (13), 4 (193), 25 (p = 3361: (a,b,c,d) = (5,34,1,5)) and no new record up to 10⁸; mean of the
  minimal m is 1.245. Cross-checked with an independent sympy enumeration at 14 primes near 10⁸.
  **EVIDENCE (not a theorem):** "every prime p ≡ 1 (4) satisfies one of the 87 conditions
  '4a²d + p has a divisor ≡ −1 (mod 4ad)', ad ≤ 25". A very rough (uncalibrated) heuristic — treating the 87 conditions as independent and "no divisor in the class" as
  "no prime factor in the class" — puts the number of failures below X at X/(log X)^{1+D}, D = Σ_{ad ≤ 25} 1/φ(4ad)
  = 92911/15840 ≈ 5.87, i.e. O(1) below 10⁸ but unbounded (the conditions are correlated and partly redundant, e.g.
  (a,d) = (1,4) and (2,1) both concern p + 16, so the true exponent may differ). The finite covering is therefore
  expected to fail eventually (like HC(p) ≤ 64); it is NOT proposed as a theorem, only as the measured search depth.
* `data/z66/hstarf/typeII_zero_all_5e6.txt`: scan of ALL n ≡ 1 (4) (prime or not) for the Type II equation, up to
  the 1800 s timeout; certified range n ≤ 5 285 401. Zeros: exactly the 1149 odd squares and n = 4545. So below
  5.3·10⁶ the only non-square n ≡ 1 (4) without a Type II solution is 4545.

## §5 Proof attempts (what was tried, what is PROVED, where it breaks)

### 5.1 A covering formulation without side conditions, and the sharp form of the obstruction

**Proposition 5.1 (PROVED).** For n ≥ 5: Type II(n) ⇔ ∃ (a, d, j) ∈ ℕ³ with n ≡ −(j + 4a²d) (mod 4adj).
Proof. N := 4a²d + n. "N ≡ −j (mod 4adj)" ⇔ j | N and N/j ≡ −1 (mod 4ad) ⇔ q := N/j is a divisor of N in the
class −1 (mod 4ad) (and conversely j := N/q). Apply Lemma 1.2(ii). In terms of (a,b,c,d): j = (a+b)/c. ∎
So REAL(p) says: p lies in one of the residue classes −(j + 4a²d) mod 4adj. (The c = 1 sub-family (★) is j = a + b
with … ; the classical identities are the small moduli: (a,d,j) = (1,1,3) covers p ≡ 5 (12), (1,2,3) covers 13 (24),
(2,1,1)… etc.) **No finite set of these classes covers all primes** (PROVED): the class 1 (mod 4adj) is never covered, because
Prop. 5.1 (whose proof is valid for every n ≥ 1) would give a solution of 4abcd = a + b + c, impossible since
4abcd ≥ 4abc > 3abc ≥ a + b + c; so primes ≡ 1 mod lcm(moduli) escape (Dirichlet). This is the
Schinzel-type barrier: the proof must choose moduli of size growing with p.

**Proposition 5.2 (PROVED; the obstruction in its sharpest form).** Let p ≡ 1 (mod 4) be prime and 4abcd = a + b + pc
with gcd(a, b, c) = 1 (primitive; every solution is a multiple of a primitive one, §2). Then
   (ab/p) = −1,   (q₁/p) = −1 for q₁ = 4acd − 1,   (jd/p) = −1 for j = (a+b)/c.
Proof. (q₁/p): as in Theorem 3.1, −p ≡ (2a)²d (mod q₁) gives (p/q₁) = −(d/q₁) = −1 and reciprocity (p ≡ 1 mod 4)
gives (q₁/p) = (p/q₁) = −1. (jd/p): j ≡ −p (mod 4ad) and j | p + 4a²d, j odd (j ≡ −p ≡ 3 mod 4), gcd(a, j) = 1
(a common prime would divide a and a + b = cj, hence b, hence by the equation c — contradicting primitivity). So
(p/j) = (−4a²d/j) = −(d/j). Write d = 2^k d', d' odd. j ≡ −p (mod 4d') and reciprocity give (d'/j) = (j/d')·
(−1)^{(d'−1)/2} = (−p/d')(−1)^{(d'−1)/2} = (p/d'); if k ≥ 1 then 8 | 4d, j ≡ −p (mod 8) and (2/j) = (2/p).
Hence (p/j) = −(2/p)^k (p/d'), and by reciprocity (p/j) = (j/p), (p/d') = (d'/p): (j·2^k·d'/p) = (jd/p) = −1.
(ab/p): a + b ≡ 4abcd (mod p) gives jd = d(a+b)/c ≡ 4abd² (mod p), so (ab/p) = (jd/p) = −1. ∎
(CERTIFIED on all 31 745 solutions with p ≤ 2·10⁴ by `scripts/z66_hstarf_jacobi.py`, no violation.)
For n = m² all three symbols are +1, which re-proves Theorem 3.1. Consequence for any proof: it must *produce* a
quadratic non-residue of p of a very specific shape (q₁ = 4acd − 1 dividing 4a²d + p). Burgess gives non-residues
below p^{1/(4√e)+ε}, but nothing forces one of that shape.

### 5.2 The mirror class

For (a, d) fixed with gcd(ad, p) = 1 (true for all Type II parameters, Lemma 2.4) let N = 4a²d + p. Divisors q > 1 of N
with q ≡ +1 (mod 4ad) satisfy (q/p) = +1, those with q ≡ −1 (mod 4ad) satisfy (q/p) = −1 (same computation as in
Prop. 5.2; for p | a the symbols can vanish, e.g. p = 5, a = 5, d = 1, N = 105, divisors 5 and 21). Writing q = 4acd + 1 (c ≥ 1), q | N ⇔
q | pc − a, i.e. the mirror class corresponds to the equation 4abcd + a + b = pc with b ≥ 0 (b = 0 is the trivial
family a = pc, q = N/p). **Assessment (not a theorem): this gives no leverage here** — on the divisors of a single integer N_{a,d} the
symbol (q/p) is a function of q mod 4d only, i.e. it merely relabels the two classes; I found no weighted or averaged
divisor sum to which a character-sum bound (Pólya–Vinogradov/Burgess) applies with an adequate error term. (The script `z66_hstarf_jacobi.py` also
tabulates the c = 1, b ≥ 1 sub-case 4abm + a + b = p, which has no solution for 7 primes ≤ 2·10⁴; this is only a
curiosity.)

### 5.3 Primality versus non-squareness

Theorem 3.1 (the q₁-symbol obstruction) only uses that n is not a square; Proposition 5.2's forms (ab/p) = (jd/p) = −1
DO use primality (through gcd(a, j) = 1 and Lemma 2.4) and fail for composite n: for n = 105, (a,b,c,d) = (3,9,4,1)
is a primitive solution with (ab/n) = (jd/n) = 0. The computation of §4 shows the Type II equation
fails for the non-square n = 4545 = 3²·5·101, so "n ≡ 1 (mod 4), n not a square" is NOT sufficient at small n.
`data/z66/hstarf/typeII_zero_all_5e6.txt` (scan of all n ≡ 1 (4) ≤ 5 285 401, §4): 4545 is the ONLY non-square
exception in that range (EVIDENCE). The natural conjecture is therefore "Type II(n) for every non-square n ≡ 1 (mod 4),
n ≠ 4545" (EVIDENCE only). Since the conjectured exception set contains a non-square, neither primality nor
non-squareness alone can be the whole mechanism; the data merely suggest that the decisive global input is the
non-triviality of the Jacobi character (·/n) (the q₁-obstruction of Theorem 3.1) together with a "largeness"
condition, 4545 plausibly being a small-number accident (few candidate moduli, and 9 | n reduces the local densities).

### 5.4 Why the group-theoretic tools in the brief do not bite (PROVED statements)

* The group acting in REAL(p) is ℤ_p × A, and the witness can always be taken abelian, indeed cyclic (Thm 2.2,
  Prop 2.5); any other group realising such a signature (e.g. PSL₂(𝔽₁₉) for p = 5, see Prop 3.2's caveat) realises a
  Type II triple that is also realised cyclically. PSL₂(𝔽_p) itself is excluded (Prop 3.2). Dickson's subgroup
  classification therefore never enters.
* The Frobenius character formula for the number of generating triples with prescribed orders in a cyclic (or
  abelian) group is elementary and reduces exactly to the gcd equation gcd(α,N) + gcd(β,N) + gcd(α+β,N) = 4N/p: the
  "counting" is the Diophantine problem itself; nothing is gained.
* The naive characteristic-p construction produces the wrong genus (Prop 3.4); non-Galois pull-backs do not see the obstruction
  (Prop 3.3), so the prime-degree Hurwitz theorem has no analogue here: realisability of REAL(p) is an arithmetic
  (unit-fraction) condition on three integers, not a monodromy condition.

### 5.5 What a proof must do (reduction, PROVED equivalence)

REAL(p) ⇔ ∃ q ≡ 3 (mod 4) with p mod q ∈ S_q := {−a·c^{-1} mod q : ac | (q+1)/4} (Lemma 1.2(iii) rewritten:
q = 4acd − 1, p c + a ≡ 0 mod q). |S_q| ≤ τ₃((q+1)/4) = q^{o(1)} and S_q ⊂ {non-residues mod q}; for prime q,
p ∈ S_q forces (q/p) = −1. Heuristically Σ_{q ≤ Q} |S_q|/q ≍ (log Q)³, so a prime p "should" be covered by
≍ (log p)³ moduli q ≤ p (consistent with the counts in §4: R⁻(8813281) = 64). Membership p ∈ S_q is the statement
"q divides pc + a with ac | (q+1)/4", i.e. a divisor-in-arithmetic-progression condition on the shifted numbers
pc + a; for c = 1 it is "p + a has a divisor ≡ −1 (mod 4a)". So REAL(p) for all p is exactly the shifted-divisor
problem that the analytic approaches attack; the geometric packaging (superelliptic curves w^N = z^α(z−1)^β with
N | 4p·(gcd sums)) adds no new invariant. I found no route that avoids this reduction (an assessment of the
constructions tried, not a no-go theorem).

### 5.6 Partial results actually PROVED here (all classical in substance)

For completeness, from Prop. 5.1 with small (a, d, j): REAL(p) holds for p ≡ 5 (mod 12) [(a,d,j) = (1,1,3)],
p ≡ 13 (mod 24) [(1,2,3)], p ≡ 7 (mod 8) [(2,1,1)], p ≡ 5 (mod 8) [(a,b,c,d) = (2,1,1,(p+3)/8)], p ≡ 2 (mod 3)
[(a,b,c,d) = (1,(p+1)/3,1,1), Y = ℙ¹], and whenever (p+1)/2 has a divisor ≡ 3 (mod 4) [(★), u = 1], or p + 4 has a
divisor ≡ 3 (mod 4) [(a,d) = (1,1)], or p + 2 has a divisor ≡ 7 (mod 8) [(★), u = 2], or 2p + 1 = δk with δ ≡ 5,
k ≡ 7 (mod 8) [(a,b,c,d) = (1, δ, 2, (k+1)/8); this is a c = 2 solution, not (★): p = 409 has it but no (★)].
None of these reaches the residue classes p ≡ 1, 121, 169, 289, 361, 529 (mod 840) in general, as expected.

## §6 Summary of the lane

PROVED: a clean realisation problem REAL(p) (pull-back of a prime-to-p triangle cover along z ↦ z^p with
2g − 2 = |A|(p − 4)) which is equivalent to the full Type II family of Erdős–Straus, hence implies ES(p); cyclic
groups always suffice (superelliptic model); REAL fails at odd squares via a Jacobi-symbol obstruction whose sharp
form is (ab/p) = −1 for every solution; PSL₂(𝔽_p) in its own characteristic, the naive fixed-data characteristic-p construction, and the
non-Galois Hurwitz condition are each shown not to capture REAL(p) (other-characteristic PSL₂(𝔽_ℓ) does act, even
with Type I signatures); an unconditional covering formulation p ≡ −(j + 4a²d) (mod 4adj).
CERTIFIED: Type II for all p ≡ 1 (4) ≤ 2·10⁷; the four falsifiers behave as stated; sub-families (a=1, d=1, c=1)
each fail somewhere; for n ≡ 1 (4), n ≤ 5 285 401, the Type II equation fails only at odd squares and at 4545.
OPEN / NOT PROVED: REAL(p) for all large primes. No HOT LEAD. The honest conclusion is that (assessment, not a no-go theorem) each of the geometric or
group-theoretic dressings tried here of 4/p = 1/x + 1/y + 1/z with p | x, p | y collapses to the same shifted-divisor problem.

## §7 Relation to prior repository work (as reported by the cross-model review; those memos were not read in this lane)

The review states that Z64_EQUIV Lemma A already gives the automorphism/genus-ratio equivalence with ES and its
Lemma F realises the (★) sub-family cyclically; that Z65_LIFT Prop E excludes abelian Type I actions and proves the
cyclic p-Sylow structure, and its Prop O gives a scoped signature-transparency obstruction; and that Z57_BFII
Lemma 1.1 / Prop 2.2 / Cor 2.3 / Prop 3.2 already contain the divisor forms, the S_q = −T_q description, the Jacobi
obstruction with square failure and the finite-modulus barrier, with a census of all odd n ≤ 10⁷ showing 4545 as the
sole non-square exception. Accordingly, the incremental content of this memo is: **cyclic sufficiency for every full
Type II signature (Prop. 2.5)**, the explicit prime-to-p pull-back presentation REAL(p), the (ab/p) = −1 form of the
obstruction, the scoped negative results (Props 3.2–3.4), and the depth statistic; the census and the obstruction are
independent rediscoveries.

## §8 Cross-model review (branch side-agent/z66-xrev-hstar, `data/z66/xreview/REVIEW_HSTARF.md`) — fixes applied

Verdict ACCEPT-WITH-FIXES. Fixed: (1) the false converse "Type II iff abelian" (now: abelian/cyclic realisation iff
Type II); (2) branch labels in Prop 3.4 (orbits above 0 and 1, conductors c₀, c₁); (3) coprimality hypothesis
gcd(ad, p) = 1 in §5.2 and "PROVED-empty" downgraded to an assessment; (4) "and nowhere else" / "only place" primality
rhetoric removed (§0, §3); (5) §5.6 parameter labels: (2,1,1) covers 7 (mod 8), the 2p + 1 = δk condition is the c = 2
solution (1, δ, 2, (k+1)/8), not (★); (6) §4: d = 1 failures start at p = 13, a = 1 failures at 193 (exhaustive bounds
stated); (7) the mandatory 38 𝔊*-zero screen added (38/38 witnesses) plus explicit witnesses for the 12 F2 primes;
(8) HUR script now tests gcd(L, n) = 1 and gcd(N, n) = 1; (9) universal "every dressing collapses" statements marked
as assessments; (10) §7 credits prior work as reported. Conclusion unchanged: equivalence established, existence
unproved, no HOT LEAD.

## §9 Falsifiers re-stated

* **F1 (odd squares):** REAL(m²) is false (Theorem 3.1: the q₁-symbol obstruction, valid for every non-square n;
  the sharper (ab/p) = −1 of Prop. 5.2 is prime-only). Every argument in §5 either uses this Jacobi symbol explicitly or is a verbatim covering congruence
  that squares avoid; no argument for primes is claimed that would survive at squares.
* **F2 (C-even sub-equation fails above 10¹⁰):** REAL(p) is equivalent to the FULL family (all a, b, c, d; all
  parities), Theorem 2.2; the C-even/c = 1 sub-families are not what REAL(p) realises; explicit full-family witnesses
  for the 12 primes are in `data/z66/hstarf/r8_12_typeII.txt` (these are numerator-4 witnesses, not repairs of the
  C-even sub-family).
* **F3 (285 (★)-free composites):** the Type II equation (REAL's arithmetic content for primes; for composites REAL
  needs in addition gcd(abcd, n) = 1) has solutions for all of them below 5 285 401 except 4545, and fails at 4545 —
  so no claim of a proof "for all n ≡ 1 (4)" is made, and a proof for primes must fail at 4545 (and at squares) — §5.3.
* **F4 (14 (★)-free primes ≤ 10¹⁰ and 38 𝔊*-zero primes):** all 14 have Type II solutions with c ≥ 2 and all 38 have
  Type II witnesses (§4), so REAL(p) holds for them; likewise for the 12 F2 primes.

Nothing in this memo proves the Erdős–Straus conjecture or any new case of it; the conjecture remains OPEN.
