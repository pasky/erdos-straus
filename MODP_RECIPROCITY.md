# MODP_RECIPROCITY — higher reciprocity in the mod-p coordinates; Gaussian-representation certificates (task O265)

Status labels as in DISCOVERIES.md. **ES is not solved, here or anywhere.** Memos: BRAINSTORM/z35_*.md. Scripts: scripts/z35_*.
Spark relay on O263 (CLASS_FORCING.md) sparks 1 and 4. Notation: p ≡ 1 (4) prime, p = a² + b², a odd, b even (a, b > 0
unless said otherwise); i_p := a·b⁻¹ mod p (a square root of −1 mod p; replacing b by −b gives −i_p, i.e. π ↔ π̄);
(x/p)_4 := x^{(p−1)/4} mod p ∈ μ₄(F_p) = {±1, ±i_p}.

## 0. Iteration log
* v0 (brief's idea). "In mod-p coordinates the modulus is p and the small objects are the certificate parameters; their n-th
  power symbols mod π are independent data, so maybe the target w ≡ −1 (mod 4d) is a power-class statement mod π."
  §1 writes the b = 1 line in mod-p / least-residue coordinates (m, g, d) with 4md = p + g. Screen result: the residue-symbol
  content of a certificate is (i) quadratic part: a function of the parameters mod 8 (Jacobi), i.e. the T1 sign, (ii)
  quartic part: a function of (a, b) modulo the parameters (Gauss–Dirichlet–Burde), a genuine extra datum — but the event does
  not depend on it. The target is additive (an equation of height 1), not multiplicative. Modification → v1.

## 1. The b = 1 line in mod-p (least-residue) coordinates, and the residue-symbol content of one certificate

**Proposition 1.1 (three faces of the b = 1 line; PROVED, elementary; (ii) is (J)85's least-residue form specialised, (iii)
the Type II e-slice of CLASS_FORCING §1).** For p ≡ 1 (4) the following are equivalent:
(i) ∃ d ≥ 1 and w | p + 4d with w ≡ −1 (mod 4d), w < p + 4d (López Type A; SS8 Prop 1.3);
(ii) ∃ m ≥ 1 such that the least positive residue g_m := (−p mod 4m) divides m + 1;
(iii) ∃ g ≡ 3 (mod 4) such that (p + g)/4 has a divisor m ≡ −1 (mod g).
The bijection is (d, w) ↦ (m, g) = (cg − 1, (p + 4d)/w) with c := (w + 1)/(4d); inverse d = (p + g)/(4m), c = (m + 1)/g,
w = 4cd − 1. In all three forms the certificate is one equation **4md − g = p, g | m + 1** in three positive integers; it is
the *height-one* solution of the congruence 4md ≡ g (mod p).
*Proof.* (4cd − 1)g = p + 4d ⟺ 4d(cg − 1) = p + g. From (i): g := (p + 4d)/w; as w ≡ 3 (4) and p + 4d ≡ 1 (4), g ≡ 3 (4),
g ≥ 3, so m = cg − 1 ≥ 2, 4m | p + g and g | m + 1; since 0 < g ≤ m + 1 < 4m, g is the least residue g_m. Conversely (ii)
gives c = (m + 1)/g, d = (p + g)/(4m) ≥ 1, w = 4cd − 1 with wg = p + 4d, and w < p + 4d as g > 1 (g = 1 would need
p ≡ −1 (4)). (iii) is (ii) read with g fixed. ∎ (`scripts/z35_checks.py` (1): the (d, w)- and (m, g)-sets coincide for all
1125 primes p ≡ 1 (4) < 2·10⁴.)

*Regimes.* md ≈ p/4 and g ≤ m + 1. (R1) m ≤ X bounded: the event is "p mod 4m ∈ {−g : g | m + 1}", a congruence (B1).
(R2) d ≤ X bounded: a divisor event for the bounded set of integers p + 4d (CLASS_FORCING Thm 6.1 tried to bar it under
Hypothesis HC, but R272 D1 found that theorem FATAL as stated — abelian conditions at primes > B can force certificates, e.g.
p ≡ −4 (7) ⟹ 7 | p + 4, a d = 1 certificate; nothing here relies on it). (R3) the balanced range m, d = p^{1/2 + o(1)}, where m, d, g are of the same
size as a, b — the only place where p's Gaussian data and the certificate live on one scale.

**Proposition 1.2 (residue-symbol content of one certificate; PROVED).** Let (m, g, d, c, w) be as in Prop 1.1, write
d = 2^s d′, m = 2^r m′ (d′, m′ odd).
(a) *(Quadratic part = parameters mod 8.)* (w/p) = −1; (g/p) = (−d/g); (d′/p) = (−g/d′); (m′/p) = (−g/m′); (2/p) = (−1)^{(p²−1)/8}.
So every quadratic symbol mod p of certificate data is a Jacobi symbol among the parameters (and p mod 8): **the sign layer is
not a free datum of p once the parameters are given** — it is the T1 sign (ET Prop 1.6; CLASS_FORCING Lemma 2.2(a)).
(b) *(Quartic part = Gaussian data modulo the parameters.)* (w/p)_4·(g/p)_4 = (2/p)·(d/p)_4 in μ₄(F_p). For an odd prime
q ≠ p, (q/p)_4 ≡ [q/π]_4 (mod π) is a function of (a mod 4q, b mod 8q) (the 2-adic part fixes the primary associate; π ↔ π̄
conjugates the value): for q ≡ 1 (4), q = c_q² + d_q²
(c_q odd), **Burde's law** (p/q)_4(q/p)_4 = ((a c_q − b d_q)/q) when (p/q) = 1 [Burde, J. reine angew. Math. 238 (1969);
`z35_checks.py` (2): 2158 pairs, 0 violations], with (p/q)_4 a function of p mod q; for q ≡ 3 (4), [π/q]_4 ≡ π^{(q²−1)/4} =
(π̄/π)^{(q+1)/4} (mod q), a function of the point (a : b) ∈ P¹(F_q). Hence the quartic symbols of w, g, d, m are functions of
(a, b) modulo 16·rad(mdg) — data of p NOT determined by p mod anything (Thm 2.1(c)(ii) of CLASS_FORCING: Frob_p in
ℚ(i, q^{1/4}) is non-abelian information; R272 D2: O263's slogan "reciprocity forces parity, never class" is an overclaim —
the correct content is "Frobenius data of p = congruence data + an independent non-abelian part", and that non-abelian part
is exactly what this file studies).
(c) *(The event ignores (b).)* The certificate condition (4md − g = p, g | m + 1) involves only integers; (b) is a
consequence of it, never an input. (`z35_checks.py` (3): the identity in (b) and (w/p) = −1 on all 2716 certificates p < 5000.)
*Proof.* (a) Jacobi reciprocity with p ≡ 1 (4): (x/p) = (p/x) for odd x > 0; p ≡ −4d (mod g) (as m ≡ −1 (g)), p ≡ −g (mod d′)
and (mod m′) (as 4md = p + g). (w/p) = −1 is CLASS_FORCING Lemma 2.2(a) (SS8). (b) wg ≡ 4d (mod p) and 4^{(p−1)/4} = 2^{(p−1)/2}.
The q ≡ 3 (4) formula: in ℤ[i]/(q) ≅ F_{q²}, π^q ≡ π̄, so π^{(q²−1)/4} = (π^{q−1})^{(q+1)/4} = (π̄/π)^{(q+1)/4}; quartic
biquadratic reciprocity for the primary primes π and −q (Ireland–Rosen, *A Classical Introduction…*, Ch. 9 §9, Thm 2;
(N(−q) − 1)/4 = (q² − 1)/4 is even) transfers it up to the unit factor [−1/π]_4 = (−1)^{(p−1)/4} and the primary normalisation.
`scripts/z35_quartic_function.py` (`logs/z35_quartic_function.txt`): for q ≤ 37 and all p ≡ 1 (4) < 3·10⁵, (q/p)_4 (with
i ↔ i_p = a/b) is a single-valued function of (a mod q, b mod q, a mod 4, b mod 8) (q = 2: (a, b, p) mod 16), 0 conflicts;
without the 2-adic data, q ≡ 3 (4) gives ≈ 50 % conflicts (the primary-associate sign). ∎

**Answer to goal (1) of the brief.** In mod-p coordinates the decisive condition is the *height-one* equation 4md − g = p
(equivalently: the least residue −p mod 4m divides m + 1). Its residue-symbol content splits into a quadratic part, which is
forced and equals the T1 sign (a), and a quartic part, which is genuine Gaussian information (b) but is an *output* of a
certificate, not a criterion for one (c). The target w ≡ −1 (mod 4d) is additive — "w lies in an arithmetic progression of
difference 4d inside [1, p)" — whereas power classes are cosets of multiplicative subgroups of F_p^×. So **no**: the target is
not a power-class statement mod π; reciprocity enters only through the quadratic sign it already forces.

## 2. Does the non-abelian part of Frob_p act on certificates?

**Proposition 2.1 (bounded witnesses: the non-abelian part is inert; PROVED, Chebotarev).** Let Ω/ℚ be finite Galois, C a
conjugacy class of Gal(Ω/ℚ), and S a finite set of pairs (d, w) (d ≥ 1, w ≡ −1 (mod 4d)). Let M := lcm(16, all w, all 4d, the
conductor of Ω^{ab}). For every residue r mod M compatible with C (i.e. Frob_r on Ω ∩ ℚ(ζ_M) = C restricted there), the set of
primes p ≡ r (M) with Frob_p|Ω ∈ C has density |C|/(|Gal(Ω/ℚ)|·[ℚ(ζ_M) : Ω ∩ ℚ(ζ_M)]·…) > 0 in the class r (the fibre-product
count of CLASS_FORCING Thm 2.1(b)), and on it the event "some (d, w) ∈ S certifies p" is constant (it is "w | p + 4d", a
condition on p mod w). So for certificate menus with bounded witnesses, the Kummer/power-residue data of p (quartic, octic,
Eisenstein symbols of any fixed small numbers) add nothing to the abelian (congruence) data.
*Proof.* The event depends on p mod M only; Chebotarev in Ω·ℚ(ζ_M). ∎
(R272 D1 is consistent with this: the abelian part *can* force certificates — p ≡ −4 (7) — it is the non-abelian part that is
inert at bounded level.)

**Proposition 2.2 (unbounded level: the non-abelian part is complete information; PROVED, Dirichlet).** For p ≡ 1 (4) with
primary π = a + bi, let χ_π(n) ∈ {±1, ±i} be the image of n^{(p−1)/4} mod p under i_p ↦ i (a Dirichlet character of order 4
mod p). The values χ_π(q) at the primes q ≡ 3 (mod 4) determine π (hence (a, b) and p). In particular the quartic symbols of
small primes, which at each fixed q are an independent non-abelian datum (Prop 2.1), are jointly a complete invariant.
*Proof.* If χ_π(q) = χ_{π′}(q) for all primes q ≡ 3 (4), q ∤ pp′, then ψ := χ_π·χ̄_{π′} is a character mod 4pp′ that is
trivial on every such q. By Dirichlet, these primes meet every class ≡ 3 (mod 4) of (ℤ/4pp′)^×, and products of two of them meet
every class ≡ 1 (mod 4); so ψ is trivial, χ_π = χ_{π′} as characters mod 4pp′, their conductors p, p′ coincide, and equality of
the order-4 characters mod p forces equal i_p, i.e. π′ = π. (By Linnik, finitely many q — up to a power of pp′ — suffice.) ∎
*Reading.* There is no "independence barrier" for non-abelian data at unbounded level: knowing enough quartic symbols is
knowing p's Gaussian coordinates. Any reciprocity-based mechanism at growing level must therefore use (a, b) *as numbers* —
which is §3 (Gaussian-representation certificates). At bounded level (Prop 2.1) it is inert.

**EVIDENCE 2.3 (non-abelian independence at moderate level).** `scripts/z35_quartic_independence.py 2000000 40`
(`logs/z35_quartic_independence.txt`): 74 415 primes p ≡ 1 (4) < 2·10⁶, levels d ≤ 40, quartic data (q/p)_4 for
q ∈ {2, 3, 5, 7, 11, 13} (on (q/p) = 1), hit indicator of the b = 1 line at level d, stratified by p mod lcm(4d, 16, q):
240 tests, max |z| = 2.46, share |z| > 2 = 2.5 % (null ≈ 4.6 %), none > 3. Canonical quartic bit of b = 1 witnesses for
p ≡ 5 (8) (2 is a non-residue, so (2w/p)_4 = ±1 is π ↔ π̄-invariant): +1: 281 437, −1: 282 747 (50.1 % / 49.9 %). The
certificate carries a free, balanced quartic bit, and quartic data of p do not move the per-level hit rates (unlike the
quadratic sign, which is forced: Prop 1.2(a)).

## 3. Gaussian-representation certificates (goal (3))

**3.1 Correction of the premise: polynomial (a, b)-menus are already closed.** That a, b are not polynomial in p does not help:
the campaign's collapse theorems are stated in the norm-form variables themselves. POINTWISE_BINARYFORM Thm 3.2/3.2′ ((J)3):
families whose ET coordinates or (x, y, z) are polynomial/rational in (a, b) are invalid on a full square class mod M up to
a density-zero set (odd squares m² = Q(u, v) exist in every square class and sector; ET Prop 1.6). (J)78 Thm 1.1: a polynomial
Type II family in (u, v) for an irreducible binary quadratic Q that is valid at ONE point has coordinates in ℚ[Q] — i.e. it
is an ET identity in p. (J)79 Cor 3.2: the same for Type I and for every full norm form (any degree). So every "identity in
a, b" (levels d, windows m, side numbers p + 4b², p + 4ab, … chosen polynomially) is either an identity in p or invalid —
the brief's hope that (J)78/(J)79 "do not apply verbatim" is unfounded for polynomial choices. What remains open is
**non-polynomial** use of (a, b): arithmetic functions (gcd, modular inverses, continued fractions, factorisations) and
non-polynomial lifts such as X ≡ i_p (mod p) (§3.3).

**Lemma 3.2 (Gaussian anti-windows; PROVED — the local form of T1, cf. (J)84 "p is a non-square modulo every class modulus").**
Let m ≥ 1 and suppose p ≡ u² (mod m′) for a unit u, where m′ is the odd part of m, and, if m is even, p ≡ u² (mod 2^{v₂(m)+2})
(for odd m nothing at 2). Then the window m is sterile: (−p mod 4m) never divides m + 1.
*Proof.* Let g := −p mod 4m, suppose g | m + 1. Then g ≡ 3 (4) (p ≡ 1 (4)) and m ≡ −1 (mod g), so (m/g) = −1. Write
m = 2^s m′; then (m′/g) = −(2/g)^s and, by reciprocity with g ≡ 3 (4), (g/m′) = (m′/g)(−1)^{(m′−1)/2} = −(2/g)^s(−1/m′), so
(−g/m′) = −(2/g)^s. But −g ≡ p ≡ u² (mod m′) gives (−g/m′) = 1, hence (2/g)^s = −1, so s ≥ 1 is odd and g ≡ ±3 (8). For
s ≥ 1, g ≡ −p ≡ −u² (mod 2^{s+2}) with s + 2 ≥ 3 gives g ≡ −1 (mod 8): contradiction. ∎
*Gaussian supply.* p ≡ b² (mod a) and p ≡ a² (mod b) and p ≡ a² (mod 2^{v₂(b)+1}·…): every window m with m′ | a, and every
m = 2^s m′ with m′ | ab and 2^{s+2} | b² (e.g. m = ab/2, s = v₂(b) − 1), is sterile (CRT: p ≡ b² mod the a-part, ≡ a²
mod the b-part, ≡ a² mod 2^{2v₂(b)}). Numerically (below): the window m = a hits 0 of 12 979
primes and m = ab/2 also 0, against 1.25 % and 0.19 % for the same quantities borrowed from neighbouring primes.
**So the Gaussian representation supplies anti-certificates (sterile windows), never certificates** — the quadratic
shadow again pushes everything visible into the genus subgroup (CLASS_FORCING C4, (J)53/(J)55).

**Proposition 3.3 (the √−1 menu is still T1-barred for polynomial families; PROVED).** Every lift X ≡ ±i_p (mod p) gives
X² + 1 = pN (N ≥ 1), and (X, N) are not polynomial in p or in (a, b) (they move with the lift X ↦ X + tp). Let F be a family of
ET coordinates (Type I or II) polynomial (or rational) in (X, N), read at n := (X² + 1)/N, and let
V(C) := {(X, N) ∈ ℤ²_{≥1} : N | X² + 1, (X, N) ≡ (X₀, N₀) (mod M)} with X₀² + 1 ≡ N₀ (mod M) (the class n ≡ 1 (mod M), the
T1 point). Then F is not valid on all of V(C): V(C) contains points with n an odd square, beyond any bound, where ET Prop 1.6
forbids validity.
*Proof.* Take a prime s ≡ 1 (mod 4M) (Dirichlet): −1 is a square mod s² and s² ≡ 1 (mod M). Pick X with X² ≡ −1 (mod s²) and
X ≡ X₀ (mod M) (CRT; gcd(s, M) = 1), X arbitrarily large in its class mod Ms². Then N := (X² + 1)/s² is an integer with
N ≡ (X₀² + 1)·s⁻² ≡ N₀ (mod M), (X, N) ∈ V(C), and n = s² is an odd square. ∎
*Scope.* This bars families valid on a whole class; the sector refinement (validity on V(C) ∩ cone, as in POINTWISE_BINARYFORM
Thm 3.2(b)) would need the square points to be dense in direction, i.e. equidistribution of the roots X/s² of X² ≡ −1 (mod s²)
(Hooley / Duke–Friedlander–Iwaniec type input) — not checked here; recorded as an open technical point, not a route.
So "compute a square root of −1 mod p (or the Gaussian representation), then apply a polynomial ET identity" is barred in
every variant; the X-menu is not new territory. (Validity on the non-square classes n ≢ 1 (mod M) is classical one-variable
congruence territory, as in POINTWISE_BINARYFORM Remark 1.)

**EVIDENCE 3.4 (no Gaussian-canonical parameter beats neighbour controls except by the quadratic redistribution).**
`scripts/z35_gauss_menu.py 300000` (`logs/z35_gauss_menu.txt`): 12 979 primes p ≡ 1 (4) ≤ 3·10⁵; window test "(−p mod 4m) | m + 1"
and level test "p + 4d has a divisor ≡ −1 (mod 4d)" at m, d ∈ {a, b, a + b, |a − b|, (a+b)/2, ab/2, h, k (ak − bh = 1),
X₀ = least lift of ±i_p, N₀ = (X₀² + 1)/p}; control = the same quantity taken from the four neighbouring primes (same size and
shape distribution, independent of p). |z| ≤ 2.9 for all levels; windows: m = a (0 vs 1.25 %, z = −12.8) and m = ab/2
(0 vs 0.19 %) are sterile (Lemma 3.2); m = b (2.6 vs 2.1 %, z = 4.1) and |a − b| (2.2 vs 1.5 %, z = 6.9) are mildly enhanced —
both are windows where −p mod m′ is confined to a fixed square class (−a², −2a²), so the hit probability is 0 or doubled
according to a Jacobi condition (a B1-type redistribution, the same mechanism as Lemma 3.2 with the opposite sign); N₀ and the
convergent data (h, k) are neutral. (An earlier run with shifted controls m ± j showed spurious z ≈ 13 for N₀ — a residue-class
artefact of the control, recorded as a caution.)
