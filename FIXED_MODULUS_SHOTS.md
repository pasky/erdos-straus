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
h | p + 4c²d with cofactor e, and returns x, y = p·cdj = py', z = pxj/c = px·g/(uw)·… = p·x·y'/D = pz' (the last
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

