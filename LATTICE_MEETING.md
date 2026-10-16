# LATTICE_MEETING — moving the slice in Cl(−4p): the meeting point, composition moves, and what a descent can see (O251)

Status: in progress (O251). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on ASTRA_BRIDGE Thm 3.4 (branch side-agent/astra-bridge): for a slice g ≡ 3 (4), gcd(g, p) = 1, h = (g+1)/4,
ρ² ≡ −p (mod g), L_ρ(g) = {(M, Y) : Y ≡ ρM (mod g)}; Claude points (2k, Y), k | h; Astra points (m, 1); ES = (2k, 1).
Throughout p ≡ 1 (mod 4) is prime. Scripts `scripts/z23_*`.

## 0. Iteration log
(I1) First target: a cap descent Y → Y′ < Y by composition 𝔤 → 𝔤𝔩 in Cl(−4p) ending at Y = 1. Before building moves,
asked where they could end. Answer (§1): the end set (Y = 1 points over *all* slices of Cl(−4p)) is a finite,
explicitly enumerable set, and it is **empty** for 99 primes p ≤ 10⁶ (13, 37, 97, 181, 193, …). So no walk inside
Cl(−4p) can terminate for those p, whatever its moves. Hypothesis of the obstruction: the walk stays in ℤ[√−p]
(ET parameter d = 1 / square). Modification: let the walk change the order/field — ES Type II with ET parameter d
is the meeting set of the forms pM² + dY² (disc −4dp), §1.3.

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

**Certified computation (CERTIFIED; `scripts/z23_meet.py`, exhaustive by Prop 1.1's bound, every point
checked as an exact ES identity).** Among the 39 175 primes p ≡ 1 (4), p ≤ 10⁶, **𝓜(p) = ∅ for exactly 99**:
13, 37, 97, 181, 193, 541, 673, 757, 1033, 1093, 1297, 1621, 1777, 2293, 2473, 3361, 3877, 6481, … (22 below 10⁴,
23 in (10⁴, 10⁵], 54 in (10⁵, 10⁶]); all ≡ 1 (12). Mean |𝓜(p)| over p ≤ 10⁵: 13.4. Odd squares ≤ 10⁶: all empty.

**Consequence for the O251 descent (PROVED from Prop 1.1 + certified list).** For each of the 99 primes, no sequence of
moves inside the slice lattices of ℤ[√−p] (composition, reduction, translation, Vieta partner) can end at a point
(2k, 1) with k | h: there is none. Claude points (2k, Y), Y > 1, k | h, exist at every slice (any k | h, Y ≡ 2kρ).
So "Y = 1 reachable for every p" is **false** in Cl(−4p); it is a lottery among finitely many candidates (B1/B2:
Prop 1.1(iii) is "p + 4a² has a divisor ≡ −1 (mod 4a)", a = 1, …, √p/2).

### 1.3 All of Type II on one vertical line: the meeting point at height √d

**Theorem 1.4 (slice criterion, all ET d; PROVED — a lattice repackaging of ET Prop 1.3 / EXP_OPEN row II-ad).**
Let g ≡ 3 (4), gcd(g, p) = 1, −p a square mod g, h = (g+1)/4, ρ any root. For k | h let Y_k ≡ 2kρ (mod g) be the
height class of the vertical line M = 2k of L_ρ(g) (Claude's overflow class) and
  d_k := Y_k² mod g = (−4k²p) mod g ∈ [0, g−1]   (independent of the root ρ).
Then the map k ↦ (a, b, c, d) = (h/k, ·, k/d_k, d_k) is a **bijection** between {k | h : d_k ≥ 1, d_k | k} and the Type II
solutions (x, y, z) with y = ph, p ∤ x, namely x = abd, z = bcdp, b = (p + m)/(4ad), m = (p + 4a²d)/g.
*Proof.* If d := d_k | k, put a = h/k, c = k/d; then h = acd, g = 4acd − 1 and 4a²d ≡ −16a²k²p = −(4h)²p ≡ −p (mod g),
so g | p + 4a²d, g ≡ −1 (mod 4ad); exactly as in Prop 1.1(iii)⇒(ii) (with 4ad in place of 4a), m ≡ −p (mod 4ad),
b ∈ ℤ_{>0} and a + b = c(4abd − p), i.e. cp + a + b = 4abcd: ET's Type II identity 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp).
Conversely by ET Prop 1.3 every Type II solution with p ∤ x is (abd, acdp, bcdp) with cp + a + b = 4abcd and
gcd conditions making (a, b, c, d) unique; y = ph gives h = acd; then g = 4acd − 1 | p + 4a²d (expand
(4acd − 1)(4abd − p) = 4ad(4abcd − cp − b) + p = 4a²d + p), so −4k²p ≡ 4k²·4a²d = (4acd)²d ≡ d (mod g) for k := cd,
and d < g, so d_k = d | k. The two maps are mutually inverse (k = cd, a = h/k). ∎
*Check* (`scripts/z23_alld.py 6000 3000`, 25 s): all primes p ≡ 1 (4) ≤ 6000, all slices g ≤ 3000 with a root (89 117):
the set of k with d_k | k reproduced exactly the set of Type II solutions with y = ph found by brute force over
δ | (ph)², δ ≡ −ph (mod g) (ASTRA_BRIDGE Prop 3.2) — 0 mismatches of sets; 5894 slices carry ES; every
solution checked as an exact identity.

**Reading.** On the vertical line M = 2k of L_ρ(g): Astra/Thm 3.4 ES is the point at height Y = 1 (d = 1); Claude's
capped points are heights Y with rad Y | h; a general Type II solution is the line's height class Y_k satisfying
**Y_k² ≡ d (mod g) with d | k**: formally the lattice point (2k, √d). Indeed √d + 2k√−p has relative norm d + 4k²p ≡ 0
(mod g) in ℚ(√−p, √d): the ET parameter d is the field ℚ(√−dp) ⊂ ℚ(√−p, √d), and ET's (2c, 1) point of the slice lattice
of ℤ[√−dp] (4c²dp + 1 = gD) is (2k, √d)/√d. d a perfect square s² reduces to d = 1 ((a, b, c) ↦ (as, bs, cs)), so
the Type II set of p is ⋃_{d₀ squarefree} 𝓜_{d₀}(p), one finite set per imaginary quadratic field ℚ(√−d₀p).
**What the criterion uses (vs WINDMILL Prop 10.3).** d_k is the residue −4k²p mod g, i.e. the class of the element
2k√−p in O/𝔤 ≅ ℤ/g squared — *finer* than the ideal class of 𝔤 and finer than any ray class mod a fixed modulus;
and k ranges over divisors of (N𝔤 + 1)/4. So the ES predicate on ideals 𝔤 is "some divisor k of (N𝔤+1)/4 has
(−4k²p mod N𝔤) | k": a function of (N𝔤, p mod N𝔤) and the factorisation of N𝔤 + 1 — not of the class [𝔤]. B2 verbatim.

**Corollary 1.5 (the ES predicate on ideals factors through the norm; PROVED).** For a primitive ideal 𝔤 ⊂ ℤ[√−p] with
N𝔤 = g ≡ 3 (4), gcd(g, 2p) = 1, put E(𝔤) := "some Type II solution has y = p(g+1)/4" (equivalently some ES point
(2k, √d) on a vertical line of L_ρ(g), Thm 1.4). Then E(𝔤) depends only on g: E(𝔤) ⟺ **∃ k | (g+1)/4, d | k with
g | 4k²p + d**. In particular E is constant on the primitive ideals of norm g (one per root ρ mod g), which in general lie in
several ideal classes; no function of the class [𝔤] ∈ Cl(−4p), nor of its ray class modulo any fixed modulus, enters.
*Proof.* Thm 1.4: d_k = (−4k²p) mod g is root-free, and d_k = d with d | k ≤ h < g ⟺ g | 4k²p + d. ∎
*Reading.* The class group is not merely "unable to see" the meeting condition (WINDMILL Prop 10.3: classes see only
the genus shadow); in the slice coordinates the meeting condition **does not involve the class at all**. A
composition/class-group walk 𝔤 → 𝔤𝔩 is, for the purpose of ES, the integer walk g → gℓ. The Claude overflow Y_k
(the *least* height on the line) is root-dependent for composite g, but ES is not a statement about least heights.

### 1.4 Which fields rescue the empty primes (CERTIFIED; `scripts/z23_rescue.py 1000000 200`)
For each of the 99 primes with 𝓜(p) = ∅, the least ET parameter d with a Type II solution (exhaustive in a for each d,
solution checked exactly): d = 2 for 96 primes, d = 3 for 31081, d = 5 for 3361 and 7681. In the lattice picture (Thm 1.4) the
rescue still happens on a slice lattice L_ρ(g) ⊂ ℤ[√−p], but at **height √d** instead of 1: the vertical line k = cd
has Y_k² ≡ d (mod g), d ∈ {2, 3, 5}, d | k. So ASTRA_BRIDGE Thm 3.4(c)'s meeting point (2k, 1) is the square-d part
of ES only, and it misses all Type II solutions at these 99 primes; the correct meeting set is the *square-class*
meeting Y_k² ≡ d | k of Thm 1.4. E.g. p = 13: (a, b, c, d) = (1, 2, 1, 2), 4/13 = 1/4 + 1/26 + 1/52 (slice g = 4acd − 1 = 7 | 13 + 8 = p + 4a²d).

## 2. Coordinates of the moves

**2.1 Composition (PROVED, standard Dirichlet composition).** L_ρ(g) = gℤ + (ρ + √−p)ℤ = 𝔤_ρ, the point (M, Y) being
the element Y + M√−p. For gcd(g, ℓ) = 1 and β = u + v√−p ∈ 𝔩_σ, multiplication by β maps 𝔤_ρ → 𝔤_ρ𝔩_σ = (gℓ)_{ρ'}
(ρ' ≡ ρ (g), ρ' ≡ σ (ℓ)) by (M, Y) ↦ (uM + vY, uY − pvM). A Claude point (2k, Y) goes to a point with even M iff v is
even; the new line is k' = ku + vY/2, and it is a Claude line iff 4k' | gℓ + 1. Nothing in the map relates k' to the
divisors of (gℓ + 1)/4 (Cor 1.5: only g, ℓ and the factorisation of gℓ + 1 matter).

**2.2 The controlled lift and downward closure (PROVED).** For u ≥ 1: h | h' := (gu + 1)/4 ⟺ u ≡ 1 (mod 4h)
(as g ≡ −1 mod 4h). Then for every k | h, d_k(gu) ≡ d_k(g) (mod g), and since an ES value d_k(gu) | k is < g:
**ES via (k, d) at gu ⇒ ES via the same (k, d) at g.** Conversely ES via (k, d) at g lifts to gu iff gu | 4k²p + d. So
for fixed (k, d) the ES slices are the divisors of N_{k,d} := 4k²p + d that are ≡ −1 (mod 4k): the "tower" of
controlled lifts is the divisor lattice of one integer, and ES propagates only *down* it. A lift never creates ES on
an old line; ES at gu on a *new* line k' ∤ h is an independent event (B2).

**2.3 Vieta partner = Gauss reduction on a fixed line (PROVED).** Fix k. Points (2k, Y) of L_ρ(g) with partner
D := (4k²p + Y²)/g are the positive definite forms [g, 2Y, D] of discriminant −16k²p (order of conductor 2k in
ℚ(√−p)); translating Y ↦ Y + tg and swapping g ↔ D are the Gauss reduction moves (SL₂(ℤ) action, class fixed). The
point is a Claude point at slice g iff g ≡ −1 (mod 4k), and its partner D ≡ −Y² (mod 4k) is again a Claude slice iff
Y² ≡ 1 (mod 4k). Hence:
(a) for k | 6 ((ℤ/4k)^* of exponent 2) *every* reduction move preserves Claude-admissibility, which is then a genus
condition on the form; ES with d = 1 on the line k is "some *reduced* form [g, 2, D] of disc −16k²p lies in the genus
g ≡ −1 (4k)" ⟺ 4k²p + 1 has a divisor ≡ −1 (mod 4k) — for k = 1: a prime factor ≡ 3 (mod 4) (B1: fails with
probability ≍ (log p)^{−1/2} by Landau);
(b) for k ∤ 6, a reduction move leaves the Claude set unless Y'² ≡ 1 (mod 4k): the walk must use the specific heights,
i.e. ray-class (mod 4k) information, exactly the escape route of WINDMILL Prop 10.3 — and that information is the
B2 datum "divisor of 4k²p + d in a class mod 4k".
Note [g, 2, D] with g ≤ D is already reduced: the ES forms on line k are reduced forms with b = 2, i.e. the
factorisations of 4k²p + 1; the cap/overflow Y of a Claude point is b/2 of a (not necessarily reduced) form.

## 3. The slots of a meeting point: at most one forced slot (goal 3)

A Type II solution (ET Prop 1.3) is (x, y, z) = (abd, acdp, bcdp) with cp + a + b = 4abcd. It has three *slots*:
the window m = 4x − p with coordinate x, and the slices g = 4acd − 1, D = 4bcd − 1 with coordinates y/p = acd = h,
z/p = bcd = h_D. Call a slot (modulus μ, coordinate u) **forced at a prime ℓ | μ** if (u/ℓ) = −1: then, ℓ ≡ 3 (4) being
prime, the image of u in (ℤ/ℓ)^* has even order and −1 ∈ ⟨u⟩ ⊆ ⟨primes of u⟩ (this is the group step of
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
H-B) would have to act on a non-quadratic invariant of the slice (e.g. the 4-rank / Rédei symbol of the slice
lattice), where WINDMILL Prop 10.3 and Cor 1.5 already show the class carries no information about the meeting.

## 4. Numerics: the class-group walk is free; existence is everything (goal 4)

Since E(𝔤) depends only on N𝔤 (Cor 1.5), "walk to Y = 1" can only mean: on a fixed line k (forms of disc −16k²p,
§2.3), walk in the class group of the order of conductor 2k from the start class to an **ES class** (a class
containing a form [g, 2Y, D] with g ≡ −1 (4k), g | 4k²p + d, d | k).
*Check* (`scripts/z23_cayley.py 3000 40 1,2,3,5`, 5 s; generators: prime forms of norm ℓ ≤ 40, both orientations;
multi-source BFS from the ES classes, reporting the *worst* start class):
| line k | primes p ≤ 3000 | mean #classes | lines with **no** ES class | worst-start distance to an ES class (when one exists) |
|---|---|---|---|---|
| 1 | 211 | 55.5 | 55 | ≤ 4 (1: 32, 2: 94, 3: 28, 4: 2) |
| 2 | 211 | 111.0 | 72 | ≤ 8 (mostly 2–3; 3 cases with an unreached remainder) |
| 3 | 211 | 144.6 | 109 | ≤ 6 (2 cases with an unreached remainder) |
| 5 | 211 | 268.6 | 153 | ≤ 5 |
("Unreached remainder": the composition routine skips a step when the class's first and last coefficients both
share ℓ; a code limitation, not a mathematical statement.) T1: odd squares c² ≤ 3000 — no ES class on any tested
line, as Cor 1.2(a) proves. The Gauss-reduction "descent" of §2.3 is trivial in practice: from the least-root window
shot (`scripts/z23_descent.py 20000 1000`) every starting form [g₀, 2Y, D] was already reduced (1565/1565 lines,
p ≤ 2·10⁴), so reduction moves nothing; 629 of them were ES at the start.
**Reading.** When an ES class exists on a line, it is a few generator steps from *every* class — as it must be:
class-group Cayley graphs with generators of norm ≤ (log |Δ|)^{2+ε} are expanders under GRH (Jao–Miller–Venkatesan,
J. Number Theory 129 (2009) 1491–1504), so any nonempty target set is reached in O(log |Δ|) steps. Hence "Y = 1 within
O(log p) moves" is **equivalent** (on GRH, line by line) to "the line carries an ES class", i.e. to the B2 event
"4k²p + d has a divisor ≡ −1 (mod 4k) for some d | k". On the d = 1 locus of Cl(−4p) this fails for all k at the 99
certified primes of §1; per line it fails with frequency 26 % (k = 1) … 73 % (k = 5) at p ≤ 3000.
The walk contributes reachability, never existence.
