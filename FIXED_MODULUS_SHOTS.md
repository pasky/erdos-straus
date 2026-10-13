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

**EVIDENCE (`scripts/fms_three.py 1000000`).** Among the 78 496 primes 5 ≤ p < 10⁶ the shots p + 1, p + 4, 4p + 1
fail at 10 438, 9 841, 18 992 primes; all three fail jointly at 942 primes (first: 193, 673, 2377, 2473, 2521,
…); every fired shot gives an exactly verified ES solution through Thm 2.1(a) + Lemma 1.1. T1 control: all 499 odd
squares < 10⁶ fail all three (as Remark 2.5 proves). So the three lines together are a finite set of shots that do
not cover the primes (as expected: each fails with probability ≍ (log p)^{−1/2}).

## 3. Per-modulus coverage: the ES "orbit" is a divisor box (PROVED) — the exact ES/ES^{(S)} dictionary

The O186 mechanism (reviewed form): a Gupta–Murty sieve produces a prime r ≡ 3 (mod 4) with (n/r) = −1 and
[F_r^* : ⟨S⟩] ≤ 2; then −n/4 ≡ Q² for some Q ∈ ⟨S⟩ (a discrete-log condition), and r | n + 4Q² certifies. The
analogous object in ES is the set of residues of p that a FIXED modulus h can certify.

**Theorem 3.1 (exact coverage).** Let h ≡ 3 (mod 4), k = (h + 1)/4, and p coprime to h. Then p has a cube point
with divisor h iff
`−p ≡ c·j^{−1} (mod h) for some c, j ≥ 1 with cj | k,`
i.e. p mod h ∈ A_h := −Box(k), Box(k) := {c/j : cj | k} ⊂ (ℤ/h)^*. |A_h| ≤ τ₃(k) = #{(c, j, t) : cjt = k} =
h^{O(1/log log h)}, and A_h lies in the Jacobi-symbol −1 class (Remark 2.5).
*Proof.* Lemma 1.1 (with t = d) and h | pj + c ⟺ −p ≡ c/j (j is a unit mod h since j | k). ∎

**Corollary 3.2 (ES = ES^{(S)} with bounded discrete logs; PROVED).** Let S be a finite set of odd primes and r a
prime with k = (r + 1)/4 an S-unit, k = ∏_{q∈S} q^{κ_q}. Write residues of ⟨S⟩ mod r as ∏ q^{e_q}. Then
* ES (prime certificate h = r): p is certified iff −p ≡ ∏_{q∈S} q^{e_q} (mod r) with **|e_q| ≤ κ_q** for all q;
* ES^{(S)} (O186 Prop 2.1 with g = r): p is certified iff −p ≡ 4Q² = ∏ q^{e_q} (mod r) with **e_q ≡ κ_q (mod 2)**,
  no bound (4 ≡ k^{−1} = ∏ q^{−κ_q} mod r, and 4Q² ≡ ∏ q^{2s_q − κ_q});
* a given ES^{(S)} certificate (Q, r), Q = ∏q^{s_q}, has vector e = 2s − κ; it is an ES certificate with the same
  D = Q² iff also |e_q| ≤ κ_q, i.e. 0 ≤ s_q ≤ κ_q, i.e. Q | k, i.e. r ≡ −1 (mod 4Q) — O186 Prop 6.1.
*Proof.* First bullet: c/j has exponent vector e = v(c) − v(j) with c j | k; conversely for |e_q| ≤ κ_q take
c = ∏ q^{max(e_q,0)}, j = ∏ q^{max(−e_q,0)} (cj | k). Second: O186 Prop 2.1. Third: |2s_q − κ_q| ≤ κ_q ⟺ 0 ≤ s_q ≤ κ_q. ∎
So at the same prime r, ES^{(S)} sees the whole coset ∏q^{κ_q}·⟨S⟩² (size ≍ r when ⟨S⟩ is large mod r), while ES
sees a box of ∏(2κ_q + 1) ≤ (2 log r + 1)^{|S|} elements: **the ES certificate is the ES^{(S)} discrete-log condition
with every exponent bounded by the valuation of (r + 1)/4.** For general r the box Box(k) is the "orbit" of the
divisors of k — never a group, size ≤ τ₃(k).

**Assessment 3.3 (consequence for Artin-type sieves).** A Gupta–Murty/Heath-Brown argument certifies a fixed p by
finding ONE prime r in a fixed Chebotarev set such that p mod r lies in a structured set of r-density ≫ 1 (a coset of
a subgroup of bounded index). In ES the set at r is A_r, of r-density ≤ τ₃(k)/r = r^{−1+o(1)} (Thm 3.1), and it is
never a coset of a large subgroup (it is a bounded box). The expected number of certifying primes r ≤ R for a given
p is Σ_r |A_r|/r ≍ (log R)³ — the polylog lottery (B3) — and restricted to r with S-smooth (r + 1)/4 it converges
(there are ≪ (log R)^{|S|} such r ≤ R, each of mass ≤ (log r)^{|S|}/r): the convergent S-lottery of O186 Thm 6.2(i),
now as an exact statement about each r.

## 4. Type I: the same cube with residue −p, and the unified box criterion (PROVED)

Type I := p divides exactly one of x, y, z.

**Lemma 4.1 (Type I cube).** For v, w, f ≥ 1 put g := 4vwf − p. If g > 0 and g | pv + f, then with u = (pv + f)/g,
`x = p·uvw,  y = wf·u,  z = wf·v`
solve 4/p = 1/x + 1/y + 1/z (p | x); this is a Type I solution iff p ∤ uvwf. Conversely every Type I solution
arises so. For Type I points gcd(g, 2pvwf) = 1, and
`g | pv + f  ⟺  g | p² + 4wf²  ⟺  g | 4v²w + 1.`
*Proof.* 1/y + 1/z = (u + v)/(wfuv) and 4/p − 1/x = (4uvw − 1)/(puvw); they agree iff p(u + v) = f(4uvw − 1) iff
u(4vwf − p) = pv + f. Converse: x = px′, y = Gu, z = Gv, gcd(u, v) = 1; then px′(u + v) = (4x′ − 1)Guv, and
gcd(uv, (u + v)p) = 1 (p ∤ yz) gives x′ = uvw; then pw(u + v) = (4x′ − 1)G with gcd(w, 4x′ − 1) = 1 gives G = wf, so
p(u + v) = f(4uvw − 1): the point (v, w, f). p | uvwf would put p | y or p | z; so p ∤ g (else p | 4vwf), g odd, and
gcd(g, vwf) | p forces gcd(g, vwf) = 1. With 4vwf ≡ p (mod g): 4wf(pv + f) ≡ p² + 4wf², 4vw(pv + f) ≡ p(4v²w + 1). ∎
*Check (`scripts/fms_typeI.py 4000`):* for all primes 5 ≤ p ≤ 4000 the Type I cube (enumerated along the (w, f)
line, wf ≤ p) reproduces the brute-force Type I solution sets exactly, and every brute-force Type I solution
decomposes as in the converse.

Lines (all with residue **−p**, not −1): (v, f) fixed: N = pv + f, divisor g ≡ −p (mod 4vf); (w, f) fixed:
N = p² + 4wf² (the campaign's Type I form), g ≡ −p (mod 4wf); (v, w) fixed: N = 4v²w + 1 (independent of p),
g ≡ −p (mod 4vw). Through (1,1,1): p + 1 (the same shot as Type II's (c, j) = (1,1) line), p² + 4 (never fires: a
sum of two coprime squares has no divisor ≡ 3 mod 4), and the constant 5 (never fires for p ≡ 1 mod 4). So Type I
adds no new modulus-4 shot, and every Type I line has modulus 4 × (product of the fixed pair).

**Theorem 4.2 (unified box criterion).** For an odd prime p and Box(k) := {c·j^{−1} : c, j ≥ 1, cj | k}:
* ES(p) has a Type II solution with divisor h ⟺ h ≡ 3 (mod 4) and −p ∈ Box((h + 1)/4) (mod h);
* ES(p) has a Type I solution with divisor g ⟺ g ≡ −p (mod 4), gcd(g, p) = 1, and −p ∈ Box((g + p)/4) (mod g)
  (realised by some (v, f) with p ∤ uvwf).
*Proof.* Type II: Thm 3.1. Type I: g | pv + f ⟺ −p ≡ f/v (mod g) (gcd(g, v) = 1), and 4vwf = g + p ⟺ vf | (g+p)/4
with w the cofactor. ∎ (The Type I bullet needs the side condition p ∤ uvwf of Lemma 4.1 for the solution to be of
Type I; without it one still gets an ES solution.)
So **every ES certificate of a prime is "−p lies in a divisor box modulo h"**, the box being that of (h + 1)/4
(Type II) or (h + p)/4 (Type I). A box has ≤ τ₃ elements and no group structure; in ES^{(S)} the box is replaced by
a coset of the group ⟨S⟩² (Cor 3.2). This is the precise form of B2 at the level of a single modulus.

## 5. Construction attempts (each: which hypothesis of §2–§4 it tried to violate, and the outcome)

(C1) *Cyclotomic / Lucas forcing.* Primes dividing Φ_m(a) are ≡ 1 (mod m); primitive divisors of Lucas sequences
are ≡ (Δ/r) (mod m). Idea: choose the shot so that its prime factors are forced ≡ −1 (mod 4M) by a fixed quadratic
Frobenius condition (a T-adic-forcing analogue). Outcome: fails. In the cube the certifying divisor must divide the
specific number N = p + 4c²d (or pj + c, 4dj²p + 1), whose factorisation is fixed by p; Thm 2.1 shows that whether a
divisor h of an affine shot certifies depends only on (α, β, h), and is the congruence h ≡ −1 (mod 4M). A forced
congruence would have to come from N itself being a cyclotomic-type value, but N = αp + β with p arbitrary has no
such structure, and making D = c²d a cyclotomic value (N = Φ_m(t) needs 4D = Φ_m(t) − p) forces only r ≡ 1 (mod m)
with m ≍ log N, against the needed modulus 4cd ≥ 2√D ≍ √N.
(C2) *p-dependent shots* (D' | p ± 1, so that N ≡ ∓1 mod D'). Then "h ≡ −1 (mod 4D')" becomes "the cofactor
≡ ±1 (mod D')" — the same growing modulus on the other divisor. No gain (Thm 2.1 applies to h = N/e).
(C3) *S-smooth (r + 1)/4* (to make the box a long orbit segment). Cor 3.2: the ES box is the ES^{(S)} coset with
exponents |e_q| ≤ v_q((r+1)/4) ≤ log_q r; its size is polylog(r). Even when the box contains a whole subgroup
⟨q⟩ mod r (possible only if ord_r(q) ≤ 2v_q((r+1)/4) + 1 = O(log r)), the subgroup has O(log r) elements.
(C4) *Composite certificates h = r·u with u from a structured infinite set* (u ∈ ⟨S⟩, to recover a discrete log).
h must divide the fixed shot N, so u ranges over divisors of N: finitely many. Moving the shot with u moves the
modulus (Thm 2.1/Cor 2.2).
(C5) *Type I* (residue −p, box of (g + p)/4, p-dependent): §4. Same cube structure, no new modulus-4 shot; the box
still has ≤ τ₃ elements.
(C6) *Non-affine shots.* All cube lines are affine in p except the Type I line p² + 4wf². A uniform polynomial shot
N(p) with the firing condition at a fixed h needs every root of N mod h to be −c/j with cj | (h + 1)/4; along each
coordinate direction of the cube this forces N(−c/j) ≡ 0 identically, i.e. N has a cube-line affine factor
(Assessment; the non-uniform case is not classified here).
(C7) *The orchestrator's sharpening* ("prime r in a fixed class + a discrete-log condition, bounded modulus"):
answered exactly by Cor 3.2 (the discrete log must lie in the box of (r + 1)/4) and by Prop 6.1 below (r ≤ p + (p+2)²/4).

## 6. The no-go theorem with exact scope

**Proposition 6.1 (finiteness at fixed p; PROVED, elementary).** Every Type II certificate divisor of p satisfies
h ≤ p + (p + 2)²/4, and every Type I divisor satisfies g < 3p². In contrast ES^{(S)}(p) has infinitely many solutions (Q unbounded) and
the O186 sieve finds its certificate prime r in [X/2, X] with X → ∞.
*Proof.* Type II: h | p + 4c²d and cd ≤ p/4 + 1/2 (Lemma 1.1), so h ≤ p + 4(cd)² ≤ p + (p + 2)²/4. Type I:
p(u + v) = f(4uvw − 1) with u + v ≤ 2uv and 4uvw − 1 ≥ 3uvw gives wf ≤ 2p/3, and g | p² + 4wf², so
g ≤ p² + 4(wf)² < 3p². ∎

**Theorem 6.2 (no infinite fixed-modulus family for ES; PROVED, scope stated).** Let p be an odd prime.
(i) (*Affine shots, any role of a single divisor.*) For every affine shot αp + β, the divisors h that certify Type II
solutions through it are exactly the h ≡ −1 (mod 4M), M ∈ 𝓜(α, β), up to < 4μ⁵ sporadic ones; every M ≥ √H/2
(Thm 2.1, Cor 2.2). Hence for a fixed modulus 4M₀ there are finitely many shots (height ≤ 4M₀²); for M₀ = 1 exactly
p + 1, p + 4, 4p + 1 (Cor 2.3); for a fixed Chebotarev firing set of density δ there are finitely many (Cor 2.4).
(ii) (*Per modulus, no family at all.*) For every h the set of residues p mod h certified by h (Type II) is the
divisor box −Box((h + 1)/4), of size ≤ τ₃((h+1)/4) = h^{o(1)} (so it contains no coset of a subgroup of order > τ₃);
Type I uses the box of (h + p)/4 (Thms 3.1, 4.2).
(iii) (*Finiteness.*) The certifying moduli of p form a finite set bounded by O(p²) (Prop 6.1: Type II h ≤ p + (p+2)²/4, Type I g < 3p²).
*Exact scope.* (i) covers certificates read off one divisor of one affine form (both the h-role and the cofactor
role, since Thm 2.1 applies to any divisor coprime to 2αβ); (ii)–(iii) cover every Type I/II solution, i.e. every
solution of ES(p) for p prime. Not covered: mechanisms whose certificate is a *joint* condition on several primes of
one or several shots (B4 territory: e.g. "−1 ∈ Σ_e(N)" with ≥ 2 primes), and non-uniform polynomial shots (C6).
*Reading (Assessment).* O186's ES^{(S)} works because (a) it has infinitely many solutions at fixed n, so the
certifying prime can be pushed to infinity where Gupta–Murty counts beat the exceptions, and (b) at each prime r the
certified residues form a coset of ⟨S⟩², of density ≍ 1. ES fails both: (iii) and (ii). The "growing modulus" of B2
and O186 Prop 6.1 is, at the level of one modulus, the replacement of a group (the S-orbit) by a divisor box, and at
the level of one p, the finiteness of ES(p). Any Artin-type route to ES must therefore use joint multi-prime
conditions (B4) or a non-Type-I/II encoding — neither of which is an "infinitely many fixed-modulus shots" mechanism.

