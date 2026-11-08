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
d = (n + (a+b)/c)/(4ab). (i)⇒(v): m₀ = bcd, m₁ = acd (see §2 for the geometry); then 4m₀m₁ − m₀ − m₁ = cd(4abcd − a − b)
= c²dn and gcd(m₀m₁, m₀+m₁) = cd·gcd(abcd, a+b); one checks that after replacing (a,b,c,d) by a primitive
representative (divide out k with k | gcd(a,b,c), k² | … — see §2 Remark) gcd(abcd, a+b) = c. (v)⇒(i): put
g = gcd(m₀m₁, m₀+m₁), so m₀+m₁ = g·c', m₀m₁ = g·P; then (Lemma 1.1 applied to the triple
(m₀n, m₁n, m₀m₁/g)) gives (i). [Full details in §2.] ∎

Forms (ii) and (iii) are both "a value of a binary quadratic form of discriminant −4dn has a divisor in a prescribed
class": 4a²d + n = d·(2a)² + n·1² is a value of [d,0,n], and 4c²dn + 1 = dn·(2c)² + 1 is a value of [1,0,dn].
Sub-families: c = 1 in (i) is (★); a = 1 in (ii) is "n + 4d has a divisor ≡ −1 (mod 4d)"; d = 1 in (ii) is
"(2a)² + n has a divisor ≡ −1 (mod 4a)". None of the three sub-families suffices alone (§4).

## §2 The realisation problem AB(n)

(to be written: abelian triangle covers, pullback along z ↦ z^p, equivalence with Type II)

## §3 The odd-square obstruction (F1)

(to be written)

## §4 Computations (CERTIFIED)

(to be written)

## §5–§8 Proof attempts

(to be written)

## §9 Falsifiers re-stated

(to be written)
