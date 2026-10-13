# FIXED_MODULUS_SHOTS — infinitely many fixed-modulus shots for ES itself? (task O191, spark relay N)

Status: in progress (O191). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on UNIT_ORBIT_ES.md (O186, CLAIMED, under review R186/R190), T1_TEMPLATE.md, STERILE_STEER §5 (O188).
Scripts `scripts/fms_*`, memos `BRAINSTORM/bsN_*.md`.

Question. ES^{(S)} (O186) is solvable at every non-square because its shots `p + 4Q²`, Q ∈ ⟨S⟩, form an infinite
family with the FIXED modulus 4 ("some prime factor ≡ 3 mod 4"). Does ES itself have such a family?

## 0. Iteration log

(N1) Put all Type II certificates into one symmetric object (the *certificate cube*, §1): a Type II solution of
ES(p) is a triple (c, d, j) with h := 4cdj − 1 dividing pj + c. The three coordinate lines of the cube are three
families of "shots" (affine forms in p), each with modulus 4 × (product of the two fixed coordinates). Mordell's
p + 4 is the (c, d) = (1, 1) line; the other two lines through (1, 1, 1) give p + 1 and 4p + 1.

## 1. The certificate cube (PROVED; elementary, a symmetric repackaging of the Type II parametrisation)

Type II := p divides exactly two of x, y, z.

**Lemma 1.1 (certificate cube).** Let p be an odd prime. For c, d, j ≥ 1 put h := 4cdj − 1. Then
`h | pj + c  ⟺  h | p + 4c²d  ⟺  h | 4dj²p + 1,`
and whenever this holds, with e := (p + 4c²d)/h,
`x = (p + e)/4,   y = p·cdj,   z = p·x·j/c`
is a Type II solution of 4/p = 1/x + 1/y + 1/z (p ∤ x). Conversely every Type II solution arises in this way
(from at least one cube point (c, d, j)). Every cube point has cd ≤ p/4 + 1/2.
*Proof.* 4cdj ≡ 1 (mod h), so cdj is a unit mod h and 4cd(pj + c) ≡ p + 4c²d, 4dj(pj + c) ≡ 4dj²p + 1: the three
divisibilities are equivalent. Since h ≡ −1 (mod 4cd) and p + 4c²d ≡ p (mod 4cd), e ≡ −p (mod 4cd): 4cd | p + e,
so x ∈ ℤ and cd | x, in particular c | x and z ∈ ℤ. From 4(x + c²d) = p + e + 4c²d = e(h + 1) = 4cdj·e we get
x + c²d = e·cdj, hence 1/y + 1/z = (x + c²d)/(p·cdj·x) = e/(px) = 4/p − 1/x. p ∤ x: cd ≤ p/4 + 1/2 (from
h ≤ pj + c) gives p ∤ 4c²d, so p ∤ e and x ≡ e/4 ≢ 0 (mod p).
Conversely let p ∤ x, y = py', z = pz'. Then e := 4x − p > 0 and e/x = 1/y' + 1/z'. Write y' = gu, z' = gv with
gcd(u, v) = 1; then x(u + v) = eguv and gcd(u + v, uv) = 1 give x = uvw and eg = w(u + v). gcd(e, x) divides
gcd(e, 4x) = gcd(e, p) = 1 (p | e would force p | x), so gcd(w, e) = 1 and w | g. Put c = u, d = w, j = g/w. Then
cdj = gu = y', h = 4y' − 1, and D := c²d = u²w = ey' − x (as ey' − x = egu − uvw = uw(u + v) − uvw). So
4(x + D) = p + e + 4D and 4(x + D) = 4ey' = e(h + 1) give h·e = p + 4c²d: the cube point (c, d, j) satisfies
h | p + 4c²d with cofactor e, and returns x, y = p·cdj = py', z = pxj/c = p·x·y'/D = pz' (j/c = y'/D) (the last
equality is (ey' − x)(ez' − x) = x²). ∎
*Check (`scripts/fms_cube.py 10000`):* for all 1227 primes 5 ≤ p ≤ 10⁴ the cube solutions coincide exactly with
the brute-force Type II solution sets (divisor-method enumeration of all solutions); the three divisibilities
agree at every cube point.

**The three lines through a cube point.** Fixing two coordinates leaves one *shot* — an affine form N(p) — and the
free coordinate is read off a divisor h of N with a congruence whose modulus is 4 × (product of the fixed pair):

| fixed | shot N(p) | firing condition | modulus | line through (1,1,1) |
|---|---|---|---|---|
| (c, d) | p + 4c²d | N has a divisor h ≡ −1 (mod 4cd) | 4cd | **p + 4** (Mordell) |
| (c, j) | pj + c | N has a divisor h ≡ −1 (mod 4cj) | 4cj | **p + 1** |
| (d, j) | 4dj²p + 1 | N has a divisor h ≡ −1 (mod 4dj) | 4dj | **4p + 1** |

(The (c, d) line is the "D-form" of O186 Prop 6.1 with D = c²d: for D = Q², d = 1, the modulus is 4Q; the (d, j)
line is the campaign's Type II form ff′ = 4c²dp + 1 with renamed letters.) Each line through (1,1,1) fires iff N
has a prime factor ≡ 3 (mod 4) (N ≡ 1 mod 4 for p ≡ 1 mod 4; for N = p + 1 ≡ 2 mod 4 use the odd part). Example
p = 13: p + 4 = 17 and 4p + 1 = 53 do not fire, p + 1 = 14 = 2·7 does: (c, d, j) = (1, 2, 1), x = 4, y = 26, z = 52.

## 2. Classification of affine shots (PROVED): the modulus grows like the square root of the height

A *shot* is an affine form N(p) = αp + β (α, β ≥ 1, as for every line of §1). For an odd h with gcd(h, αβ) = 1 and
h | αp + β, say that **h certifies through (α, β)** if p has a cube point with divisor h, i.e. ∃ c, j, t ≥ 1 with
4cjt = h + 1 and h | pj + c. This depends only on p mod h = −β/α mod h, i.e. only on (α, β, h) — not on p.
Let c₀/j₀ = β/α in lowest terms, H = max(c₀, j₀) (the height), and
`𝓜(α, β) = {c₀j₀} ∪ {D/c : c² | D} (if β = 4αD, D ∈ ℤ) ∪ {E/j : j² | E} (if α = 4βE, E ∈ ℤ).`

**Theorem 2.1 (affine shots).** Let μ = max(α, β).
(a) If h ≡ −1 (mod 4M) for some M ∈ 𝓜(α, β), then h certifies through (α, β).
(b) Conversely, if h certifies through (α, β), then h ≡ −1 (mod 4M) for some M ∈ 𝓜(α, β), or h < 4μ⁵.
*Proof.* (a) M = c₀j₀: cube point (c, j) = (c₀, j₀), t = (h + 1)/(4c₀j₀); h | αp + β = g(j₀p + c₀), gcd(h, g) = 1.
M = D/c (β = 4αD, c² | D): cube point (c, d, j) = (c, D/c², (h + 1)/(4M)), cd = M; h | α(p + 4c²d) = αp + β.
M = E/j (α = 4βE): (c, d, j) = ((h + 1)/(4M), E/j², j), dj = M; h | β(4dj²p + 1) = αp + β.
(b) Let (c, j, t) be the cube point (t = d). From h | pj + c and h | αp + β, h | αc − βj; put m = (βj − αc)/h ∈ ℤ.
As c, j ≤ (h + 1)/4 ≤ h/3, |m| ≤ μ/3. *m = 0:* βj = αc, so (c, j) = s(c₀, j₀) and 4c₀j₀ | 4cj | h + 1.
*m ≠ 0:* βj − αc = m(4cjt − 1) reads j·X = m − αc with X := 4mct − β, and with Y := 4mtj + α one checks
`X·Y = 4m²t − αβ` (expand: XY = 4mt·jX + αX = 4mt(m − αc) + α(4mct − β)).
– If 4m²t ≠ αβ: X, Y ≠ 0, so |X| ≤ 4m²t + αβ and |Y| ≤ 4m²t + αβ, whence (divide by 4|m|t ≥ 4)
c ≤ |m| + β(α + 1)/4 ≤ μ² and j ≤ |m| + α(β + 1)/4 ≤ μ²; and |X| ≤ |jX| = |m − αc| gives
4|m|ct ≤ β + |m| + αc, so t ≤ (α + β + |m|)/4 < μ. Hence h = 4cjt − 1 < 4μ⁵.
– If 4m²t = αβ and X = 0: then m = αc and β = 4mct = 4αc²t, so β = 4αD with D = c²t, M := ct = D/c ∈ 𝓜, and
h = 4cjt − 1 ≡ −1 (mod 4M).
– If 4m²t = αβ and Y = 0: 4mtj = −α, and jX = m − αc becomes −αc − βj = m − αc, so m = −βj, α = 4βj²t = 4βE with
E = j²t, M := jt = E/j ∈ 𝓜, h ≡ −1 (mod 4M). ∎
*Check (`scripts/fms_affine.py 40 60000`):* all 979 coprime pairs 1 ≤ α, β ≤ 40, all h ≤ 6·10⁴ (h ≡ 3 mod 4, coprime
to 2αβ): (a) never fails; the 5766 exceptions of (b) all satisfy h ≤ 8.5μ² (well inside 4μ⁵). For the lines
through (1,1,1) — (α, β) = (1, 1), (1, 4), (4, 1) — there are no exceptions at all below 6·10⁴.

**Corollary 2.2 (modulus ≥ √height).** Every M ∈ 𝓜(α, β) satisfies M ≥ √H/2, and |𝓜(α, β)| ≤ 1 + 2τ(H).
(c₀j₀ ≥ H; if β = 4αD then H = 4D and D/c ≥ √D since c² | D; symmetrically for E.) So outside the < 4μ⁵
sporadic divisors, a shot of height H fires only through divisors in classes −1 mod 4M with M ≥ √H/2.
*Example (O186 Prop 6.1 recovered and completed).* N = p + 4Q²: 𝓜 = {4Q²} ∪ {Q²/c : c | Q}, all multiples of Q, so
h certifies iff h ≡ −1 (mod 4Q) or h is one of the finitely many sporadic divisors (which come from other cube
points (c, d) with c²d ≡ Q² mod h).

**Corollary 2.3 (exactly three modulus-4 shots; refutes "p + 4 is the unique bounded-modulus shot").** A shot fires
through every h ≡ 3 (mod 4) coprime to 2αβ (up to finitely many h) iff 1 ∈ 𝓜(α, β) iff β/α ∈ {1, 4, ¼}, i.e.
N ∝ p + 1, p + 4 or 4p + 1. More generally the shots having some M ∈ 𝓜 dividing a given M₀ have height ≤ 4M₀² —
finitely many up to scaling.
*Proof.* If no M ∈ 𝓜 equals 1, take h ≡ 3 (mod 8), h ≡ 1 (mod every odd prime dividing some M), h prime (Dirichlet;
infinitely many, beyond 4μ⁵): h ≢ −1 (mod 4M) for every M ∈ 𝓜 (an odd prime q | M gives h ≡ 1 ≢ −1 mod q; M a
power of 2 ≥ 2 gives 8 | 4M and h ≡ 3 ≢ 7 mod 8). Second claim: from Cor 2.2, M ≥ √H/2 and M | M₀. ∎

**Corollary 2.4 (no infinite fixed-modulus family; Chebotarev form).** Let F/ℚ be finite Galois, C ⊂ Gal(F/ℚ) a
non-empty conjugation-stable set, 𝒞 the primes with Frobenius in C, δ = |C|/[F:ℚ] > 0. Call a shot *𝒞-firing* if
all but a density-zero set of r ∈ 𝒞 certify through it. Then 𝒞-firing shots have height H ≤ H₀(δ); in particular
there are only finitely many (up to scaling), and an infinite family of shots with a fixed Chebotarev (a fortiori
fixed-modulus) firing condition does not exist in ES.
*Proof.* By Thm 2.1, a 𝒞-firing shot has 𝒞 ⊂ ⋃_{M ∈ 𝓜}{r ≡ −1 mod 4M} up to density zero, so by Chebotarev and
Dirichlet δ ≤ Σ_{M∈𝓜} 1/φ(4M) ≤ (1 + 2τ(H))·max_{M ≥ √H/2} 1/φ(4M) ≪_ε H^{ε − 1/2}, which is < δ for H large. ∎

**Remark 2.5 (the T1 inside the cube; PROVED).** For a cube point, n := cj satisfies h ≡ −1 (mod 4n), and then
(−n/h) = −1 (Jacobi): (−1/h) = −1; (2/h) = 1 if n is even (h ≡ 7 mod 8); for odd n′ | n, (n′/h) = (h/n′)(−1)^{(n′−1)/2}
= 1 since h ≡ −1 (mod n′) and (h − 1)/2 is odd. As p ≡ −c/j = −cj/j² (mod h): **(p/h) = −1 for every certificate
divisor h**. At p = m² this is impossible — the cube is T1-tight, and so is every shot of §2 (B5).
In this language the three modulus-4 shots are T1-tight because m² + 1, m² + 4, 4m² + 1 are sums of two squares.

