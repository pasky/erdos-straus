# LATTICE_MEETING — moving the slice in Cl(−4p): the meeting point, composition moves, and what a descent can see (O251)

Status: CLAIMED (O251 checkpoint 1; reviewer pass on 074c1b47: 1 FATAL + 5 MAJOR, all repaired, marked R-O251; R262 hostile review: no FATAL, M1/M2 + minors repaired, marked R262 repair). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on ASTRA_BRIDGE Thm 3.4 (branch side-agent/astra-bridge): for a slice g ≡ 3 (4), gcd(g, p) = 1, h = (g+1)/4,
ρ² ≡ −p (mod g), L_ρ(g) = {(M, Y) : Y ≡ ρM (mod g)}; Claude points (2k, Y), k | h; Astra points (m, 1); ES = (2k, 1).
Throughout p ≡ 1 (mod 4) is prime. Scripts `scripts/z23_*`.

## 0. Iteration log
(I1) First target: a cap descent Y → Y′ < Y by composition 𝔤 → 𝔤𝔩 in Cl(−4p) ending at Y = 1. Before building moves,
asked where they could end. Answer (§1): the end set (Y = 1 points over *all* slices of Cl(−4p)) is a finite,
explicitly enumerable set, and it is **empty** for 99 primes p ≤ 10⁶ (13, 37, 97, 181, 193, …). So no walk inside
Cl(−4p) can terminate for those p, whatever its moves. Hypothesis of the obstruction: the walk stays in ℤ[√−p]
(ET parameter d = 1 / square). Modification: allow other targets on the same lines — Thm 1.4: *all* of Type II at slice g is
"(−4k²p mod g) | k", at split slices the square-class meeting Y_k² ≡ d, d | k ("height √d"); 98 of the 99 primes are
rescued on split slices, but p = 3361 has no Type II solution on any slice lattice of ℤ[√−p] (§1.4, R-O251).
(I2) Built the composition move (§2.1) and looked for an invariant carrying k | h along it. Found instead that the
ES predicate is a function of the norm alone (Cor 1.5): the class enters only through the norms it produces. Hypothesis of this
obstruction: the walk's state is an ideal (class) — modification: carry extra state (h's divisors). Controlled lifts
u ≡ 1 (mod 4h) keep h | h′ (§2.2) but ES only propagates *down* that tower.
(I3) Fixed-line reduction (§2.3): for k | 6 admissibility of coprime first coefficients is a genus property, not
preserved by all reduction moves (genus regime = B1; R262 repair); for k ∤ 6 the
walk needs ray-class data mod 4k = the B2 datum itself. (I4) Looked for two forced slots: impossible (§3).
(I5) Numerics (§4): the class-group walk reaches any nonempty target in a few steps (expander), so the walk adds
nothing; existence is the whole problem.

## 1. The meeting locus is finite, explicit, and sometimes empty

**Proposition 1.1 (d = 1 meeting locus; PROVED, elementary).** For p ≡ 1 (4) prime the following sets are in
explicit bijection:
(i) ES points of Thm 3.4(c): (g, ρ, k) with (2k, 1) ∈ L_ρ(g), k | h, over all slices g ≡ 3 (4);
(ii) triples (a, b, k) ∈ ℤ³_{>0} with **a + b = k(4ab − p)**, via g = 4ka − 1, D := (4k²p + 1)/g = 4kb − 1;
(iii) pairs (a, g) with **g | p + 4a²**, g ≡ −1 (mod 4a), via m := (p + 4a²)/g = 4ab − p, k = (g+1)/(4a).
The ES solution is the symmetric triple **4/p = 1/(ab) + 1/(pka) + 1/(pkb)**: window m = 4x − p, x = ab, and the
two slices g = 4y/p − 1, D = 4z/p − 1 (ET Type II with ET's d = 1, c = k). The set 𝓜(p) is finite:
(4a − 1)(4b − 1) ≤ 4p + 1, so min(a, b) ≤ (1 + √(4p+1))/4, max(a, b) ≤ (p+1)/3, k ≤ a + b.
*Proof.* (i)⇔(ii): (2k, 1) ∈ L_ρ(g) with k | h ⟺ g | 4k²p + 1 and 4k | g + 1 (ρ ≡ (2k)⁻¹ is then a root). Put
g = 4ka − 1; gD ≡ 1 and g ≡ −1 (mod 4k) give D = 4kb − 1. Expanding (4ka − 1)(4kb − 1) = 4k²p + 1 gives
4kab − a − b = kp. Conversely such (a, b, k) gives the factorisation. The identity: (kp + a + b)/(pkab) =
k(p + 4ab − p)/(pkab) = 4/p. (ii)⇔(iii): with m = 4ab − p, gm = 16ka²b − 4kap − 4ab + p = 4a(4kab − kp − b) + p =
4a² + p. Conversely, g ≡ −1 (mod 4a) and gm = p + 4a² give m ≡ −p (mod 4a), so b := (p + m)/(4a) ∈ ℤ_{>0}, and
4a(a + b) = 4a² + p + m = m(g + 1) = 4a·km. Finiteness: m ≥ 1 and m | a + b give 4ab − p ≤ a + b. ∎

**Corollary 1.2 (T1 and the classical covering; PROVED).** (a) For n = c², c odd, the analogue of 𝓜 is empty:
g ≡ 3 (4) has a prime factor ℓ ≡ 3 (4); ℓ | c² + (2a)² forces ℓ | c and ℓ | a, contradicting g ≡ −1 (mod 4a). (b) If p ≡ 2 (3) then (a, g) = (1, 3) ∈ 𝓜(p). So 𝓜(p) = ∅ forces p ≡ 1 (12).

**Certified computation (CERTIFIED; `scripts/z23_meet.py`, exhaustive for *existence* by Prop 1.1's bound on
min(a, b), every point checked as an exact ES identity).** Among the 39 175 primes p ≡ 1 (4), p ≤ 10⁶, **𝓜(p) = ∅ for
exactly 99**: 13, 37, 97, 181, 193, 541, 673, 757, 1033, 1093, 1297, 1621, 1777, 2293, 2473, 3361, 3877, 6481, … (22 below
10⁴, 23 in (10⁴, 10⁵], 54 in (10⁵, 10⁶]); all ≡ 1 (12). (R-O251 repair: the scan a ≤ √p + 2 sees each unordered {a, b} at least once
(≈ 9 % in both orientations; R262 repair); its mean count over p ≤ 10⁵ is 13.35, the unordered mean 12.19, the full
*ordered* locus mean 24.37 — reviewer recounts.)
Odd squares ≤ 10⁶: all empty. Independent cross-check (k-scan of `scripts/z23_shape.py`'s `least_k` up to the proven
bound k ≤ a + b ≤ (p+4)/3, divisors g ≤ √(4k²p+1)): identical emptiness verdict on all 1125 primes p ≡ 1 (4) ≤ 2·10⁴ (25 empty).
Extension (`scripts/z23_split.py 10000000 60`, 165 s, same existence scan): 160 primes p ≡ 1 (4) ≤ 10⁷ have 𝓜(p) = ∅
(61 in (10⁶, 10⁷]): emptiness keeps thinning in proportion but does not stop.

**Consequence for the O251 descent (PROVED from Prop 1.1 + certified list).** For each of the 99 primes, no sequence of
moves inside the slice lattices of ℤ[√−p] (composition, reduction, translation, Vieta partner) can end at a point
(2k, 1) with k | h: there is none. Claude points (2k, Y), Y > 1, k | h, exist at every split slice (any k | h, Y ≡ 2kρ).
So "Y = 1 reachable for every p" is **false** in Cl(−4p); it is a lottery among finitely many candidates (B1/B2:
Prop 1.1(iii) is "p + 4a² has a divisor ≡ −1 (mod 4a)", a = 1, …, √p/2).

### 1.3 All of Type II at one slice; the lattice reading at height √d

**Theorem 1.4 (slice criterion, all ET d; PROVED — a repackaging of the ET Type II description, ET Prop 2.6 in
sources/elsholtz-tao-1107.1010.pdf, in the 4-parameter form (abd, acdp, bcdp), cp + a + b = 4abcd, of EXP_OPEN row II-ad).**
Let g ≡ 3 (4), gcd(g, p) = 1, h = (g+1)/4, and for k | h put d_k := (−4k²p) mod g ∈ [0, g−1]. Then the map
k ↦ (a, b, c, d) = (h/k, (p+m)/(4ad), k/d_k, d_k), m = (p + 4a²d)/g, is a **surjection** from {k | h : d_k ≥ 1, d_k | k}
onto the Type II solutions (x, y, z) = (abd, acdp, bcdp) with y = ph, p ∤ x. In particular **ES has a Type II solution with
y = ph ⟺ ∃ k | h with d_k | k.** (R-O251 repair: an earlier version said "bijection"; it is not injective — p = 29,
g = 15: k = 2 and k = 4 both give (x, y, z) = (8, 116, 232).)
*Proof.* If d := d_k | k, put a = h/k, c = k/d; then h = acd, g = 4acd − 1 and 4a²d ≡ −16a²k²p = −(4h)²p ≡ −p (mod g),
so g | p + 4a²d, g ≡ −1 (mod 4ad); exactly as in Prop 1.1(iii)⇒(ii) (with 4ad in place of 4a), m ≡ −p (mod 4ad),
b ∈ ℤ_{>0} and a + b = c(4abd − p), i.e. cp + a + b = 4abcd: the identity 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp).
(p ∤ x is automatic: p | x, y, z would give 4 = Σ 1/(·/p) ≤ 3; R262 repair.)
Conversely every Type II solution with p ∤ x has this form for some (a, b, c, d) (ET Prop 2.6); y = ph gives h = acd;
(4acd − 1)(4abd − p) = 4ad(4abcd − cp − b) + p = 4a²d + p gives g | p + 4a²d, so for k := cd,
−4k²p ≡ 4k²·4a²d = (4acd)²d ≡ d (mod g), and d ≤ k < g, so d_k = d | k and k maps to the solution. ∎
*Check* (`scripts/z23_alld.py 6000 3000`, 25 s): all primes p ≡ 1 (4) ≤ 6000, all slices g ≤ 3000 at which −p is a square
(89 117): the image set of the map equals the brute-force set of Type II solutions with y = ph (δ | (ph)²,
δ ≡ −ph mod g, ASTRA_BRIDGE Prop 3.2) — 0 set mismatches; 5894 slices carry ES; every solution checked exactly.
(This check covers split g only; the proof does not use a root. R262 repair: the reviewer's from-scratch check
`scripts/review_r262_slice.py 6000 3000` over **all** 286 750 slices g ≡ 3 (4) ≤ 3000, gcd(g, p) = 1, p ≡ 1 (4) ≤ 6000, split
or not, found 0 mismatches: 5 894 split + 1 991 non-split ES slices, 1 889 non-injective collisions.)

**Lattice reading (split slices only).** If −p is a square mod g with root ρ, d_k = Y_k² mod g where Y_k ≡ 2kρ is the
height class of the vertical line M = 2k of L_ρ(g) (Claude's overflow class). Then: Astra/Thm 3.4 ES = height Y = 1
(d = 1); Claude's capped points = heights Y with rad Y | h; a general Type II solution at a split slice = a line whose
height class satisfies **Y_k² ≡ d (mod g), d | k** — formally the point (2k, √d) (√d + 2k√−p has relative norm d + 4k²p in
ℚ(√−p, √d)). For a Type II solution, −p ≡ 4a²d (mod g), so its slice g is split **iff d is a square modulo g** (g ≡ −1
mod 4ad is prime to 2ad); for non-square d this can fail at both slices g, D, and then the solution is invisible in every
slice lattice of ℤ[√−p] (§1.4). d = s² reduces to d = 1 ((a, b, c) ↦ (as, bs, cs)).
**What the criterion uses (vs WINDMILL Prop 10.3).** d_k is the residue −4k²p mod g, and k ranges over divisors of
(g+1)/4: a function of (g, p mod g) and the factorisation of g + 1. B2 verbatim.

**Corollary 1.5 (the ES predicate on slice ideals factors through the norm; PROVED).** For a primitive ideal 𝔤 ⊂ ℤ[√−p]
with N𝔤 = g ≡ 3 (4), gcd(g, 2p) = 1, let E(𝔤) := "some Type II solution has y = p(g+1)/4". Then E(𝔤) ⟺ **∃ k | (g+1)/4,
d | k with g | 4k²p + d**; in particular E is constant on the primitive ideals of norm g (one per root ρ mod g), which in
general lie in several classes.
*Proof.* Thm 1.4, and d_k = d with d | k ≤ h < g ⟺ g | 4k²p + d. ∎
*Reading (Assessment; R-O251 repair: an earlier version presented this as proving class-group methods irrelevant —
a non sequitur, since E is defined through y = p(g+1)/4 and so trivially depends on g only).* What the corollary does
show: a mechanism whose state is the class of 𝔤 can influence ES only through *which norms* it produces; the class
alone, without the norm, decides nothing. It does not exclude class data constraining or guiding the norms produced
(e.g. via representations by a form); no such constraint relevant to the divisor event was found here.

### 1.4 Rescues of the empty primes (CERTIFIED; `scripts/z23_rescue.py 1000000 200`, `scripts/z23_split.py 1000000 60`)
For each of the 99 primes with 𝓜(p) = ∅, the least ET parameter d with a Type II solution (exhaustive in a for each d,
checked exactly): d = 2 for 96 primes, d = 3 for 31081, d = 5 for 3361 and 7681. **Lattice visibility (R-O251 repair of a
FATAL slip: an earlier version claimed all rescues sit on slice lattices of ℤ[√−p]).** Requiring a *split* slice (g or D
with −p a square mod it): 98 of the 99 primes have such a Type II solution (least such d: 2 for 88, 3 for 8, 5 for 2);
**p = 3361 has none** (and it is the only such prime ≤ 10⁷: of the 160 empty-𝓜 primes ≤ 10⁷, 159 have a split-slice
Type II solution with d ≤ 60 — least such d: 2 for 148, 3 for 9, 5 for 2): exhaustively over all d ≤ (p+1)/3 its Type II solutions are exactly (a, b, c, d) = (5, 34, 1, 5)
(slices 99, 679) and (1, 29, 10, 29) (slices 1159, 33639), and −3361 is a non-square modulo each of these four slices.
So at p = 3361 **no Type II solution is visible in any slice lattice L_ρ(g) ⊂ ℤ[√−p]** (CERTIFIED): the Astra–Claude
lattice framework of ASTRA_BRIDGE Thm 3.4 misses Type II entirely there (Type I solutions are not addressed).
Independent brute force (all x ∈ (p/4, p/2], δ | x², in `z23_split.py`): the Type II solutions of 3361 are exactly
4/3361 = 1/850 + 1/(3361·25) + 1/(3361·170) and 1/841 + 1/(3361·290) + 1/(3361·8410) (841 = 29²), none with a split slice.
E.g. p = 13: (a, b, c, d) = (1, 2, 1, 2), 4/13 = 1/4 + 1/26 + 1/52, slice g = 7 | 13 + 8, split (−13 ≡ 1 = 1² mod 7), height
class Y_2² ≡ 2 (mod 7).

## 2. Coordinates of the moves

**2.1 Composition (PROVED, standard Dirichlet composition).** L_ρ(g) = gℤ + (ρ + √−p)ℤ = 𝔤_ρ, the point (M, Y) being
the element Y + M√−p. For gcd(g, ℓ) = 1 and β = u + v√−p ∈ 𝔩_σ, multiplication by β maps 𝔤_ρ → 𝔤_ρ𝔩_σ = (gℓ)_{ρ'}
(ρ' ≡ ρ (g), ρ' ≡ σ (ℓ)) by (M, Y) ↦ (uM + vY, uY − pvM). A Claude point (2k, Y) goes to a point with even M iff vY is
even (R262 repair: Y may be even); the new line is k' = ku + vY/2, and it is a Claude line iff 4k' | gℓ + 1. Nothing in the map relates k' to the
divisors of (gℓ + 1)/4 (Cor 1.5: only g, ℓ and the factorisation of gℓ + 1 matter).

**2.2 The controlled lift and downward closure (PROVED).** For u ≥ 1: h | h' := (gu + 1)/4 ⟺ u ≡ 1 (mod 4h)
(as g ≡ −1 mod 4h). Then for every k | h, d_k(gu) ≡ d_k(g) (mod g), and since an ES value d_k(gu) | k is < g:
**ES via (k, d) at gu ⇒ ES via the same (k, d) at g.** Conversely ES via (k, d) at g lifts to gu iff gu | 4k²p + d. So
for fixed (k, d) the ES slices are the divisors of N_{k,d} := 4k²p + d that are ≡ −1 (mod 4k): the controlled lifts
carrying ES via (k, d) stay inside this congruence-filtered divisor set of one integer (with the extra quotient
condition u ≡ 1 mod 4h), and ES propagates only *down* them. A lift never creates ES on
an old line; ES at gu on a *new* line k' ∤ h is an independent event (B2).

**2.3 Vieta partner = Gauss reduction on a fixed line (PROVED).** Fix k. Points (2k, Y) of L_ρ(g) with partner
D := (4k²p + Y²)/g are the positive definite forms [g, 2Y, D] of discriminant −16k²p (order of conductor 2k in
ℚ(√−p)); translating Y ↦ Y + tg and swapping g ↔ D are the Gauss reduction moves (SL₂(ℤ) action, class fixed). The
point is a Claude point at slice g iff g ≡ −1 (mod 4k), and its partner D ≡ −Y² (mod 4k) is again a Claude slice iff
Y² ≡ 1 (mod 4k). Hence:
(a) for k | 6 ((ℤ/4k)^* of exponent 2): all values coprime to 4k of one primitive form of disc −16k²p are congruent
mod 4k (for values m₁ = N(α₁)/N𝔞, m₂ = N(α₂)/N𝔞, m₁m₂ = N(α₁ᾱ₂/N𝔞) is a value of the principal form x² + 4k²py² ≡ x² ≡ 1),
so "first coefficient ≡ −1 (mod 4k)" is a class (genus) property **for first coefficients coprime to 4k**. It is *not*
preserved by every reduction move: translations can make Y even and the new first coefficient non-coprime to 4k
(R-O251 repair, reviewer's example p = 5, g = 43, k = 1, Y = 61: [43, 122, 87] → [43, 36, 8] → [8, −36, 43]). ES with d = 1
on the line k ⟺ 4k²p + 1 has a divisor ≡ −1 (mod 4k) — for k = 1: a prime factor ≡ 3 (mod 4) (B1; heuristically
failing with probability ≍ (log p)^{−1/2}, by analogy with Landau's density for integers — not proved for 4p + 1);
(b) for k ∤ 6, a swap move leaves the Claude set unless Y'² ≡ 1 (mod 4k): the walk must use the specific heights,
i.e. ray-class (mod 4k) information, exactly the escape route of WINDMILL Prop 10.3 — and that information is the
B2 datum "divisor of 4k²p + d in a class mod 4k".
Note [g, 2, D] with g ≤ D is already reduced: the ES forms on line k are reduced forms with b = 2, i.e. the
factorisations of 4k²p + 1; the cap/overflow Y of a Claude point is b/2 of a (not necessarily reduced) form.

## 3. The slots of a meeting point: at most one forced slot (goal 3)

A Type II solution (ET Prop 2.6, 4-parameter form) is (x, y, z) = (abd, acdp, bcdp) with cp + a + b = 4abcd. It has three *slots*:
the window m = 4x − p with coordinate x, and the slices g = 4acd − 1, D = 4bcd − 1 with coordinates y/p = acd = h,
z/p = bcd = h_D. Call a slot (modulus μ, coordinate u) **forced at a prime ℓ | μ** if (u/ℓ) = −1: then, ℓ being an odd
prime (no congruence on ℓ needed; R262 repair), the image of u in (ℤ/ℓ)^* has even order and −1 ∈ ⟨u⟩ ⊆ ⟨primes of u⟩ (this is the group step of
CAP_POINTWISE Thm 1.1).

**Proposition 3.1 (parity budget; PROVED).** (a) Slices are never forced: 4h ≡ 1 (mod g) gives (h/ℓ) = 1 for every
prime ℓ | g, and likewise for D. (b) The window is forced at ℓ | m exactly when (p/ℓ) = −1 (4x ≡ p mod m). (c) Hence
a Type II point has at most one forced slot, and the meeting point (2k, 1) of Thm 3.4 — whose slot g is a slice —
is never forced at g. The same holds at a Type I level e (x = pH, 4H ≡ 1 mod e: ASTRA_BRIDGE Prop 5.1(b)).
*Proof.* Immediate from the displayed congruences and quadratic characters being multiplicative. ∎
**Reading (Assessment).** The question "is there a point with two forced slots?" has answer no for structural
reasons: the slice congruence 4·(coordinate) ≡ 1 is the defining equation of a slice. The only forced slot is the
window, and Claude's forced results (CAP_POINTWISE, CAP_DOWN) are window results; the meeting needs, in addition, the
slice event k | h (Thm 3.4) or d_k | k (Thm 1.4), which is +1-parity at every prime of g. A parity mechanism (hatch
H-B) would have to act on a non-quadratic invariant of the slice (4-rank / Rédei symbol), about which nothing is
proved here; WINDMILL 10.3 limits class functions of N𝔞 mod t to the genus shadow, and Cor 1.5 is only
norm-dependence of E (R262 repair M1: an earlier sentence re-stated the retracted Cor 1.5 non-sequitur). Prop 3.1
itself is near-definitional (every slice coordinate is 4⁻¹ mod its modulus).

## 4. Numerics: the class-group walk is free; existence is everything (goal 4)

Since E(𝔤) depends only on N𝔤 (Cor 1.5), "walk to Y = 1" can only mean: on a fixed line k (forms of disc −16k²p,
§2.3), walk in the class group of the order of conductor 2k from the start class to an **ES class**: a class containing a
form [g, 2Y, D] with g ≡ −1 (4k), Y² ≡ d (mod g), d | k (so g | 4k²p + d *and* d is a square mod g). (R-O251 repair: an
ES slice g | 4k²p + d at which d is a non-square mod g is an ES event with **no** class on this line — e.g. p = 541,
k = 2: (d, g) = (2, 39), (2, 111), √2 exists mod neither — so the target set here is a proper subset of the divisor event.)
*Check* (`scripts/z23_cayley.py 3000 40 1,2,3,5`, 5 s; generators: prime forms of norm ℓ ≤ 40, both orientations;
multi-source BFS from the ES classes, reporting the *worst* start class). R262 repair: z23_cayley drops an edge when
its composition routine skips (non-coprime leading coefficients), so its distances are **upper bounds** in a subgraph;
the reviewer's exact re-run (`scripts/review_r262_cayley.py`, HNF ideal multiplication, same generators) gives the
exact values quoted in the last column:
| line k | primes p ≤ 3000 | mean #classes | lines with **no** ES class | exact worst-start distance to an ES class (when one exists and is reachable) |
|---|---|---|---|---|
| 1 | 211 | 55.5 | 55 | ≤ 4 (1: 41, 2: 91, 3: 22, 4: 2) |
| 2 | 211 | 111.0 | 72 | ≤ 7; 2 lines (p = 193, 577) with an unreachable coset |
| 3 | 211 | 144.6 | 109 | ≤ 6; 2 lines (p = 1061, 1493) with an unreachable coset |
| 5 | 211 | 268.6 | 153 | ≤ 5 |
(R262 repair M2: an earlier sentence called the unreached classes "a code limitation, not a mathematical statement".
False: at (k, p) = (2, 193), (2, 577), (3, 1061), (3, 1493) the prime forms of norm ≤ 40 generate only an index-2
subgroup of the class group (h = 16, 32, 104, 88), all ES classes lie in one coset, and no walk with these generators
reaches the other coset; ⟨ℓ ≤ 40⟩ ≠ Cl on 17 of the reviewer's 844 (k, p) lines.) T1: odd squares c² ≤ 3000 — no ES class on any tested
line, as Cor 1.2(a) proves. The Gauss-reduction "descent" of §2.3 is trivial in practice: from the least-root window
shot (`scripts/z23_descent.py 20000 1000`) every starting form [g₀, 2Y, D] was already reduced (1565/1565 lines,
p ≤ 2·10⁴), so reduction moves nothing; 629 of them were ES at the start.
**Reading.** With the fixed generators ℓ ≤ 40, an ES class (when one exists) was within ≤ 7 steps of every class in
the subgroup they generate; but ℓ ≤ 40 is far below the JMV/Bach regime ((log|Δ|)^{2+ε} ≈ 115–200, Bach 6 log²|Δ| ≈
700–1200 here), need not generate Cl, and JMV predicts nothing for it (R262 repair). The theorem: under GRH, Cayley
graphs of Cl(O) for an imaginary quadratic order O of discriminant Δ, with generators *all* ideals of prime norm
≤ (log|Δ|)^{B}, B > 2, prime to the conductor, are expanders (Jao–Miller–Venkatesan, J. Number Theory 129 (2009)
1491–1504, Thm 3.2), so any nonempty target is reached in O(log|Δ|) steps. Here Δ = −16k²p, so the generator bound and
the step count depend on k. Hence "reach an ES class on line k within O(log(k²p)) moves *with those generators*" is
**equivalent** (on GRH, line by line) to "the line carries an ES class", i.e. to the B2 event
"4k²p + d has a divisor g ≡ −1 (mod 4k) for some d | k with d a square mod g" (for "Y = 1" itself: d = 1). On the d = 1 locus of Cl(−4p) this fails for all k at the 99
certified primes of §1; per line it fails with frequency 26 % (k = 1) … 73 % (k = 5) at p ≤ 3000.
The walk contributes reachability, never existence.

## 5. Verdict (O251)

1. **Meeting locus (PROVED + CERTIFIED).** Thm 3.4(c)'s meeting set (2k, 1) is the finite set {a + b = k(4ab − p)}
   (Prop 1.1) and is **empty for 99 primes p ≤ 10⁶** (13, 37, 97, …; all ≡ 1 mod 12). So no descent in the slice
   lattices of ℤ[√−p] can terminate at height 1 for those p.
2. **The right meeting set (PROVED, Thm 1.4).** Type II with y = ph ⟺ ∃ k | h with (−4k²p mod g) | k (a surjection
   onto the solutions, not a bijection); at split slices: height class Y_k² ≡ d (mod g), d | k (formally (2k, √d)).
   89 117 split slices checked. The 99 primes are rescued at d = 2 (96), 3 (1), 5 (2); 98 of them on a split slice,
   but **p = 3361 has no Type II solution on any slice lattice of ℤ[√−p]** (CERTIFIED, §1.4).
3. **Norm-only predicate (PROVED, Cor 1.5; its reading is Assessment).** The ES predicate on slice ideals of norm g
   is "∃ k | (g+1)/4, d | k: g | 4k²p + d"; a class-based mechanism can act only through the norms it produces. Composition moves are, for ES, the
   integer moves g → gℓ; controlled lifts (u ≡ 1 mod 4h) propagate ES only downwards (§2.2).
4. **Fixed-line reduction (PROVED, §2.3).** Claude points on line k = forms [g, 2Y, D] of disc −16k²p; admissibility
   (for coprime first coefficients) is a genus condition iff k | 6 (B1 regime), else it is the B2 datum; reduction
   moves need not preserve admissibility (§2.3(a) repair).
5. **Parity budget (PROVED, Prop 3.1).** Slices and Type I levels are unforced at every prime; a Type II point has at
   most one forced slot (the window). No "two forced slots" point exists.
6. **Walks (EVIDENCE + literature).** With generators ℓ ≤ 40: exact worst-start distance ≤ 4–7 whenever an ES class
   exists in the generated subgroup (p ≤ 3000, k ∈ {1, 2, 3, 5}); 4 lines have an unreachable index-2 coset (R262).
   Under GRH, with generators all prime-norm ideals ≤ (log|Δ|)^{2+ε} prime to 2k (Δ = −16k²p; JMV 2009 Thm 3.2),
   "reach an ES class within O(log|Δ|) moves" is
   equivalent to existence of an ES class on the line (a sub-event of the B2 divisor event); the descent contributes no existence information.
**Assessment.** The lattice-meeting / class-group-walk route to ES, as posed, gives no existence mechanism (items 3–6):
the walk's state (an ideal class, or a form) enters the target predicate only through the norms it produces, the
predicate itself is "4k²p + d has a divisor ≡ −1 (mod 4k), d | k" (B2, with B1 for k | 6), and at p = 3361 no Type II
target lies in the slice lattices of ℤ[√−p] at all, so any Cl(−4p)-confined Type II mechanism must fail there. What would reopen it: a move whose
*output norm* is forced to have h′ with a prescribed divisor structure *and* p mod g′ in the box S_{g′} — i.e. a
joint-factorisation identity (hatch H-A), not a class-group statement. ES is not solved; no infinite case claimed.
