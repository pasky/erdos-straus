# Z55_CROSSU — cross-u cancellation of the tied class events at fixed p: fresh angles, the class index, and what they reduce to

Status: z55 lane CROSSU (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z55_lanes.md` § CROSSU; reading list
restricted to `Z54_EXACTSUM.md` §0/§7, `Z53_GENUSX.md` §0/§4, `Z54_EXACTSPIN.md` §0/§8 — FRONTIER not read before the
tests, per kickoff). Internal, internally reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES or (★)
at any infinite set of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z55_crossu_*`, data `data/z55/crossu/` (< 1 MB). Notation from `Z53_GENUSX.md` §1 (cited **GX**).

## 0. Checkpoint log
* cp1: §1 statement, §2 why not closed, §3 Lemma A (class index) + Lemmas B, C, first falsifier (§5, twisted layers,
  10⁹–10¹⁴) — committed.

## 1. Setting and the precise statement attacked

p ≡ 1 (mod 4) prime (the identities below hold for every odd n ≡ 1 (4) with gcd conditions). Window
(U₀, U₁, Y, X), family 𝔉 = {(u, w)}: u squarefree, u ≡ 1 (4), U₀ < u ≤ U₁, gcd(u, p) = 1; w odd squarefree in (Y, X],
gcd(w, up) = 1. Shell 𝔖 = {(u, w) ∈ 𝔉 : w | p + u}; level divisor d := (p + u)/(2w) (odd, gcd(d, u) = 1; GX writes w″).
𝔖₃ := {(u, w) ∈ 𝔖 : d ≡ 3 (4)}. Exact and genus layers (GX §1, level form):
  R_𝔉 = 2·#{(u,w) ∈ 𝔖₃ : d ≡ −1 (mod u)},   G_𝔉 = 2·Σ_{(u,w)∈𝔖₃} 1[−d ∈ (ℤ/u)^{×2}] / |(ℤ/u)^{×2}|.
Standing range assumption (GX §4): Y ≥ U₁ and 8U₁X ≤ p, so d > 4U₁ ≥ u on 𝔖 (GX Lemma 4.1).

**Statement attacked (CONJECTURE-strength; not claimed).**
  (CU)  R_𝔉(p) − G_𝔉(p) = o(log² p) as p → ∞ through primes p ≡ 1 (24), on a window family with M_𝔉 ≫ log² p.
With GX Theorem X (T_u → 0) and (X-w), (CU) gives R_𝔉 > 0, i.e. (★), for all large p. The kickoff asks for ANY
mechanism producing cancellation of R − G *summed over u at fixed p*, tested first numerically at 10⁹–10¹².
Weaker sub-targets considered: (CU′) R_𝔉 ≥ εG_𝔉 for all large p (positivity transfer); (CU″) the same for a twisted
or signed variant of the count that still implies (★).

## 2. Why this is not already closed

* z54 EXACTSUM (Theorem N) closes *n-uniform block bounds* for the conductor/frequency blocks; EXACTSPIN closes the
  direct complete-fibre averaging and fixed-order reconstruction. Both leave "cross-u cancellation inside a dyadic
  slice" as the surviving Assessment route. This lane attacks exactly that, by looking for a *structural* reason
  (involution, descent, incidence, modular-hyperbola, continued-fraction) rather than a block-by-block estimate.
* The closed items (hyperbola dualization at fixed conductor; Cauchy–Schwarz in the function variable; low-conductor
  universality; bounded-order inverse lemmas; finite menus) are all estimates of a *fixed* fibration. The new ingredient
  tried here is to change the fibration (over d, over the level t, over the modular hyperbola mod p, over SL₂ words)
  and ask whether the class event becomes a *non-tied* event in some coordinates. §3 shows it does not: in every
  coordinate system the per-point weight is a function of one residue, the class index j of Lemma A.

## 3. The class index (PROVED)

**Lemma A (class index).** Let (u, w) ∈ 𝔖 with u > 1, d = (p + u)/(2w). Let ū_d ∈ [1, d) be the inverse of u mod d
and put j := (u·ū_d − 1)/d. Then
 (a) j ∈ ℤ, 1 ≤ j ≤ u − 1, and j·d ≡ −1 (mod u), i.e. j ≡ −d^{−1} (mod u);
 (b) class hit (d ≡ −1 (mod u)) ⟺ j = 1;  genus (−d ∈ (ℤ/u)^{×2}) ⟺ j ∈ (ℤ/u)^{×2};
 (c) (p prime) with d̄ := d^{−1} mod p in [1, p): d̄ = (2w + jp)/u, and (d·d̄ − 1)/p = ū_d; equivalently
     (−p mod d)·(−p^{−1} mod d) = 1 + j·d, where −p mod d = u.
     In particular j = ⌊u·d̄/p⌋: j is the bin of the Kloosterman coordinate d̄/p in the partition of (0, 1) into u equal
     bins, and the hit is the lowest bin [1/u, 2/u).
*Proof.* (a) u ū_d ≡ 1 (mod d) gives j ∈ ℤ; 1 ≤ ū_d ≤ d − 1 gives 0 < uū_d − 1 < ud, so 0 ≤ j < u, and j = 0 forces
uū_d = 1, impossible for u > 1. Reducing u ū_d = 1 + jd modulo u: jd ≡ −1. (b) From jd ≡ −1: d ≡ −1 ⟺ j ≡ 1; and
−d ∈ □ ⟺ −d^{−1} ∈ □ ⟺ j ∈ □. (c) 2wd = p + u gives u ≡ −p (mod d), hence ū_d ≡ −p^{−1} (mod d), and 0 < u < d
(d > 4U₁) gives −p mod d = u; so u ū_d = 1 + jd is the displayed product identity. Next, e := (2w + jp)/u is an
integer: u | 2w + jp ⟺ j ≡ −2w·p^{−1} (mod u), and jd ≡ −1 with 2wd ≡ p (mod u) gives j ≡ −d^{−1} ≡ −2w p^{−1}.
Then d·e = (2wd + jpd)/u = (p + u + jpd)/u = (p(1 + jd) + u)/u = p ū_d + 1 ≡ 1 (mod p), and 1 ≤ e < p because
2w + jp < up ⟺ j ≤ u − 1 (as 2w < p). So e = d̄ and (dd̄ − 1)/p = ū_d. Finally u d̄ = 2w + jp with 0 < 2w < p gives
j = ⌊u d̄/p⌋. ∎

*Reading.* On 𝔖 every quantity in play — the class residue −d mod u, the inverse of u mod d, the inverse of d mod p,
the second remainder of the ceiling Euclidean algorithm on (p, d) (Lemma B) — is the same integer j ∈ [1, u). The
exact layer is R − G = 2Σ_{𝔖₃} f_u(j), f_u(j) := 1[j = 1] − 1[j ∈ □_u]/|□_u|.

**Lemma B (SL₂/continued-fraction form).** (u, w) ∈ 𝔖 is a class hit iff the ceiling (Hirzebruch–Jung) Euclidean
algorithm on (p, d) terminates in three steps, p = 2w·d − u, d = t·u − 1, u = u·1, with t = (d + 1)/u ≡ 0 (mod 4) on
𝔖₃; equivalently [[p, −(2wt − 1)], [d, −t]] = M(2w)M(t)M(u) with M(a) = [[a, −1], [1, 0]], and d·(2wt − 1) = tp + 1.
In general the second ceiling remainder of (p, d) is j^{−1} mod u (so hits ⟺ second remainder 1).
*Proof.* p = 2wd − u with 0 < u < d is the first ceiling step; the second is d = ⌈d/u⌉u − r₂ with r₂ = (−d) mod u =
(j^{−1}) mod u by Lemma A(a). r₂ = 1 ⟺ j = 1 ⟺ d = tu − 1. The matrix product is a direct multiplication; its
determinant identity reads d(2wt − 1) − tp = 1. t ≡ 0 (4): d ≡ 3 (4), u ≡ 1 (4) give tu = d + 1 ≡ 0 (4). ∎

**Lemma C (twisted layers).** For an integer c with gcd(c, u) = 1 put
  N_c := 2·#{(u,w) ∈ 𝔖₃ : j ≡ c (mod u)},   G_c := 2·Σ_{𝔖₃} 1[j ∈ c·□_u]/|□_u|,   E_c := 2·Σ_{𝔖₃, gcd(c,u)=1} 1/φ(u).
Then N₁ = R_𝔉, G₁ = G_𝔉; for each u, Σ_{c mod u} N_c|_u = Σ_c G_c|_u = 2·#𝔖₃|_u; and
  N_c = 2·#{(u, w, t) : (u,w) ∈ 𝔉, d ≡ 3 (4), c·d + 1 = u·t}
     = 2·#{representations 1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup) with (u,w) ∈ 𝔉, (p+u)/(2w) ≡ 3 (4)}   (c > 0),
and for c = −1, N_{−1} counts the *signed* representations 1/p = 1/(2wt′u) + 1/(2wt′p) − 1/(t′up) (d = ut′ + 1).
*Proof.* j ≡ c ⟺ cd ≡ −1 (mod u) ⟺ cd + 1 = ut; with 2wd = p + u, 2w(ut − 1) = c(p + u), i.e. 2wtu = cp + cu + 2w;
divide by 2wtu·cp. For c = −1, −d + 1 = ut with t < 0; write t = −t′. The coset sums are the orthogonality of the
cosets of □_u. ∎
*Reading.* The genus layer is the average of the square-twisted layers: G_𝔉 = Σ_x (weights) N_{x²}. Each N_c is an
ES-type representation count (for c = 1 the type II count for 4/p after t = 4C; for c = −1 the signed one). So
"R − G = o(log²p)" says the hit class c = 1 is not special among the c-twisted ES equations.

## 4. Mechanism map: what each fresh angle reduces to

The kickoff lists candidate mechanisms. Each was worked through in the coordinates of §3 before any numerics; the
status of each is given with its label.

**4.1 Rigidity (PROVED).** Let 𝔖₃ carry the weight f(P) := f_{u(P)}(j(P)) = 1[j = 1] − 1[j ∈ □_u]/|□_u| (so
R − G = 2Σ_{𝔖₃} f). By Lemma A the index j of a point is, in each coordinate system,
  j = −d^{−1} mod u = (u·(u^{−1} mod d) − 1)/d = ((−p mod d)(−p^{−1} mod d) − 1)/d = ⌊u·(d^{−1} mod p)/p⌋
  = (second ceiling remainder of (p, d))^{−1} mod u.
Hence: (i) every re-fibration of the sum (over u, over w, over d, over the level t = ū_d, over the modular hyperbola
(d, d̄) mod p, over SL₂ words) is the same sum of the same weights; (ii) f takes only the values 1 − 1/|□_u| (hit),
−1/|□_u| (genus non-hit), 0 (off-genus); so no bijection σ of 𝔖₃ satisfies f∘σ = −f on hits (that would need
1 − 1/|□_u| = 1/|□_{u′}|, impossible for |□_u|, |□_{u′}| ≥ 2), and more generally **no bounded-to-one map can realise
the cancellation pointwise**: a hit at modulus u can only be balanced by ≈ |□_u| = φ(u)/2^{ω(u)} genus non-hits.
Any cancellation of R − G is therefore a statement about the φ(u)/2^{ω(u)}-to-one incidence between the hit fibre
{j = 1} and the genus fibre {j ∈ □_u}, i.e. about equidistribution of j inside □_u along 𝔖₃ — which is (CU) itself.
*Scope.* This closes every "pairing", "involution", "switching" and "descent chain" mechanism as a class; it says
nothing about estimates that group ≍ u points at a time.

**4.2 Switching divisors d ↔ (p + u)/d (PROVED identity; no cancellation).** When d itself is odd squarefree in (Y, X]
with gcd(d, up) = 1, (u, d) ∈ 𝔖 with level w, and its index is j′ ≡ 2p^{−1}·j^{−1} (mod u). So the switch maps a hit
to a hit iff u | p − 2, and to a genus point iff 2p ∈ □_u; it permutes the index multiset at each u by j ↦ 2p̄/j and
changes no sign. (Proof: 2wd ≡ p (mod u) gives w^{−1} ≡ 2d p^{−1}, so −w^{−1} ≡ 2p^{−1}·(−d) = 2p^{−1} j^{−1}.)

**4.3 Vieta/Markoff moves (PROVED, scoped).** With x = u, y = 2w, z = t the hits are the integer points of the cubic
surface S_p : xyz = x + y + p (and N_c those of S_{p,c} : xyz = cx + y + cp, Lemma C). Each variable occurs to degree 1,
so for any two fixed coordinates the third is determined; there is no coordinate-fibre involution of Vieta type, and
the only coordinate permutation preserving S_p is x ↔ y (the u ↔ 2w symmetry, which leaves the family). The surface
is fibred by conics in three ways ((zx − 1)(zy − 1) = zp + 1 at fixed z, etc.), whose integer points are divisor pairs.
*Assessment:* no descent/jumping structure links different u; Markoff-type orbits do not exist here.

**4.4 Incidence geometry of the divisor surface (PROVED identity; no gain).** In the (d, u)-plane the shell points
{(d, u) : d | p + u} are the lattice points on the pencil of lines u = kd − p through (0, −p); hits are those lying on
the pencil d = 4Cu − 1 through (−1, 0). The intersection of the lines with parameters (k, C) is a lattice point iff
4Ck − 1 | 4Cp + 1 (the C-form). Incidence bounds between the ≍ U₁ log p shell points and the pencil lines are upper
bounds of polynomial size; they neither bound R − G by o(log² p) nor give positivity. *Assessment.*

**4.5 Fixed-p Kloosterman equidistribution (Assessment, with the exact obstruction).** The modular hyperbola mod p is
the one object where fixed-p equidistribution is proved with a power saving (Weil). Lemma A(c) puts the hit there:
(u, w) is a hit iff the Kloosterman coordinate d̄/p of d equals the single value (p + 2w)/(up), and in general d̄/p lies
in [j/u, j/u + 2w/(up)) — always at the bottom of a bin of length 1/u, the only randomness being the bin index j. Weil
bounds resolve #{d ∼ D : d̄/p ∈ I} only for |I| ≫ p^{1/2+ε}/D, whereas the hit is one integer value of d̄ per shell
point and the shell is a sparse (≍ U₁ log p out of D) set selected by the Diophantine condition −p mod d ≤ U₁. Counts
of size O(log² p) cannot be reached by an estimate with error ≥ p^{1/2}; the joint Weyl sums Σ_d e(h₁p/d + h₂d̄/p)
needed for the sparse set are the EXACTSUM exponential sums, closed block-wise by Theorem N. Nothing new.

**4.6 Entropy / union bounds (Assessment).** A hit is the congruence p ≡ −u (mod 4uC − 1); K hits with pairwise
coprime moduli determine p modulo a number exceeding p once K > 1/(1 − β). This bounds the number of n ≤ N with ≥ K
hits (a B6 average over n); at a fixed p it is void, since the typical p has ≍ log² p hits with coprime moduli.

**4.7 Polynomial / determinant method (Assessment).** Integer points of S_p in a box of side B: Bombieri–Pila and
Heath-Brown give upper bounds of size B^{δ}p^ε; the target is a lower bound of size 1 against a main term log² p.

**4.8 Continued fractions / Dedekind sums (PROVED identities; Assessment on use).** By Lemma B the hits are the d for
which the ceiling Euclidean algorithm on (p, d) has length 3. On 𝔖, Dedekind reciprocity gives
  s(d, u) = −s(j, u) and s(d, u) = s(p, d) + (u/d + d/u + 1/(ud))/12 − 1/4,
so the hit is the extreme value s(d, u) = −s(1, u) = −(u − 1)(u − 2)/(12u). Heilbronn–Porter statistics of the
Euclidean algorithm at fixed numerator p are averages over all d < p with errors ≫ p^{1/2}; length-3 expansions are
≍ log² p events out of p. No tool at the required resolution.

**4.9 Additive combinatorics of the firing set (EVIDENCE; §5.2).** Pair statistics of hits (gcd of the two u, gcd of
the two d, closeness of the u, divisibility u | u′) coincide with those of a genus-weighted random sample of the same
size: the firing set has no structure beyond the 1/φ(u) weighting.

**4.10 Correlation with a fixed multiplicative function (PROVED, scoped).** The Legendre symbol (d/p) is −1 at every
hit and at every genus point of 𝔖₃ (GX Lemma 2 / B5), so it is already absorbed by the genus layer; the twisted layers
N_c − G_c are orthogonal to it. A fixed f(u) or f(w) only reweights fibres and does not change the j-incidence of 4.1.

**4.11 Positivity transfer (CU′) (Assessment).** R ≥ εG would follow from a map taking genus points (u, w, x), x ≠ ±1,
to hits anywhere in the full (★) count. The natural move t ↦ t x̄² (mod d) transports d | x² + pt to d | 1 + pt′ but
loses the second condition d ≡ −1 (mod t′): the transported point has the right modulus but an uncontrolled class
("class-changing transfer", FRONTIER §4 item 11). No transfer found.

## 5. Falsifier F1: the twisted layers at 10⁹–10¹⁴ (EVIDENCE; identities CERTIFIED on the runs)

Engine `scripts/z55_crossu_engine.c` (window as GX §5: (U₀,U₁,Y,X) = (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4); shell
enumeration identical to `z53_genusx_engine.c`; R, G and the shell counts agree with `z54_exactspin_engine` on
every n checked). It computes j on every point of 𝔖₃, checks Lemma A(a),(c) (u·ū_d = 1 + jd) on each point
(`badj = 0` on all 1 339 runs), and outputs N_c, G_c, E_c for c ∈ {1,…,12, 16, 25, −1, −2, −3, −4} and the j/u
histogram. Driver `scripts/z55_crossu_run.py`, stats `scripts/z55_crossu_stats.py`; data `data/z55/crossu/main.tsv`,
`stats.txt`. Samples: the z53/z54 lists — 200 random primes ≡ 1 (24) at 10⁹ and 10¹⁰, 150 each at 10¹¹–10¹⁴; 150 odd
squares; 60 near-squares at 10¹⁰ and 10¹²; the 19 hard primes (14 (★)-zero + item-14 primes); 50 composites at 10¹⁰.

Findings (pooled z := Σ(N_c − G_c)/√ΣVRG, VRG the genus-conditioned model variance of R − G):
* Every twisted layer looks like R − G: for all 18 classes c and all prime samples, |z| ≤ 2.5, mean(N_c − G_c) within
  ±0.55, sd(N_c − G_c) = (0.9–1.1)·√(mean VRG). The hit class c = 1 has z = +1.5, −1.6, 0.0, −1.7, −1.9, +0.1 at
  10⁹,…,10¹⁴ (pooled over the 1 000 primes: z = −1.61). The signed class c = −1: +0.3, +1.5, +1.0, +0.1, +1.0, +1.4.
* Cross-class correlations of (N_c − G_c) over the samples: |ρ| ≤ 0.25 at n ≥ 150, no sign pattern between
  c and −c, c and 4c, or 1 and the square twists.
* The class index is uniform: the j/u histogram (10 bins, all 𝔖₃ points) is flat to ±0.002 at every size
  (N = 2.9·10⁵ at 10¹², 1.6·10⁶ at 10¹⁴). Restricted to genus points it shows the expected small-square excess in the
  first bin (j ≤ √u are perfect squares) and nothing else.
* Controls. Odd squares: N_c = G_c = 0 for c ∈ □ (empty genus, GX Lemma 3.3) while the non-square classes (c = 2, 3,
  …) have N_c − G_c of the same size as at primes — the T1 vanishing is a property of the genus coset, not of the
  exact layer's fluctuation. Near-squares and composites: as primes. Hard primes: R − G = −0.39 ± 0.68 (19 samples).
Assessment: no class c and no coordinate (u, d, t, d̄) distinguishes the hit class statistically at these sizes;
the data are consistent with j being uniform on (ℤ/u)^× along 𝔖₃ with no cross-u structure.

### 5.2 Falsifier F2: structure of the firing set (EVIDENCE)
`scripts/z55_crossu_pairs.py` on per-point dumps of the 300 primes at 10¹²–10¹³ (769 hits, 967 hit pairs with
u₁ ≠ u₂). Null: |H| genus points sampled with probability ∝ 2^{ω(u)}/φ(u) (exactly the G-weight), 20 repetitions.
  hits:  gcd(u₁,u₂) > 1 : 12.4 %   gcd(d₁,d₂) > 1 : 22.1 %   |u₁ − u₂| ≤ U₁/20 : 40.4 %   u | u′ : 1.97 %
  null:                   12.2 %                    19.4 %                      37.0 %           1.76 %
(pair se ≈ 1.5 %). Against a uniform shell sample the same statistics differ by factors 2–40, entirely because hits
sit at small u (mean u 1 206 vs 1 277 for the null, vs ≈ 2 500 uniform) — the 1/φ(u) weighting, not a mechanism.
Data: `data/z55/crossu/pairs_1e12_1e13.txt`.

### 5.3 Additional readings of F1
* var(R − G)/mean VRG = 1.09, 1.10, 0.94, 0.86, 0.84, 0.91 at 10⁹,…,10¹⁴ (n = 150–200; se ≈ 0.12): consistent
  with independent fibres, as in EXACTSUM §6.
* Pooled over the 1 000 random primes: Σ(N₁ − G₁)/√ΣVRG = −1.61, and for c = −1 (signed-ES class) +2.16; for c = 2
  and 4, −0.12 and −0.05. Two values of |z| ≈ 2 among 18 classes is what independent classes give.
* G − E (genus prediction minus uniform prediction) is within ±0.08 at every size: the genus coset carries no visible
  excess over the uniform prediction in these windows.
* Hard primes: the 14 (★)-zero primes have R = 0 with G = 0 at the seven smallest (empty 𝔖₃) and G = 0.1–1.9 at the
  others; p = 3361 and p = 5101441 have R = 2. The family's deficit at these primes is the deficit of a 2–26-point
  shell, not a cross-u effect.

## 6. Screens, verdict, FRONTIER text, bottom line

**The four FRONTIER §4 hard screens, applied to the route "cross-u cancellation of the class index" (Assessment):**
1. *T1 (squares).* Not binding for (CU): at odd squares R = G = 0 (GX Lemma 3.3), and F1 shows the non-square twisted
   layers N_c − G_c fluctuate at squares exactly as at primes. The square-sensitive step of the route is the genus
   lower bound (Thm U) plus (X-w), not (CU). A mechanism for (CU) need not use the character of p — which is also why
   none of the fixed-p tools (all of which see p only through (·/p) or through d̄ mod p) engages it.
2. *8/131.* Not applicable to (CU) (a remainder bound); the 4 enters through t ≡ 0 (4) on 𝔖₃ (Lemma B).
3. *Tied modulus (B2).* Fails — this is the content of §4.1/4.5: in every coordinate the hit is one residue class mod
   the moving u (equivalently one value of d̄ mod p per shell point), and no re-fibration untangles it.
4. *Fixed p.* Every identity holds at fixed p; the only fixed-p equidistribution with a power saving (Weil, §4.5) is
   below the required resolution by a factor ≍ p^{1/2}/log² p.

**Verdict: narrowed (small), inconclusive on the target.**
* *PROVED, structural.* Lemma A identifies the class residue with the branch index of the modular inverse (three
  forms), Lemma B with the length-3 ceiling Euclidean expansion, Lemma C the twisted layers as ES-type representation
  counts for 1/(cp) with G their square-twisted average. §4.1: no bounded-to-one map on the shell can realise the
  cancellation; §4.2–4.3: switching and Vieta-type moves do not exist or do not change sign. These are scoped
  closures of the "pairing/involution/descent" family of mechanisms, not of grouped estimates.
* *EVIDENCE.* At 10⁹–10¹⁴ the hit class is statistically indistinguishable from any other class of the index (18
  classes, 1 000 primes, controls), the index is uniform, the firing set is structureless beyond the 1/φ(u) weight.
  These tests can only detect residue-class bias or pair structure; they cannot falsify an o(log² p) bound.
* *Survives.* (CU) as stated; the only reformulation with a known fixed-p tool (modular hyperbola mod p) needs
  resolution of a single residue per sparse-set point. **Assessment:** the escape hatch left by §4.1 is an estimate
  that handles ≍ u shell points at once *with the modulus u moving* — a theorem on divisors of the single integers
  p + u (u ∼ U) in one moving class, with error below log² p. None is known (FRONTIER §4 item 4).

**Proposed FRONTIER §7 text** (append to item 3, after the EXACTSPIN entry):
> *(z55, `Z55_CROSSU.md`, internal review.)* Cross-u cancellation of the exact class layer R − G on the Thm U family,
> fresh-angle sweep.
> * *Class index (PROVED).* On a shell point (u, w) with level d, the class residue −d^{−1} mod u equals the integer
>   j = (u·(u^{−1} mod d) − 1)/d ∈ [1, u) = ((−p mod d)(−p^{−1} mod d) − 1)/d = ⌊u·(d^{−1} mod p)/p⌋ = inverse of the
>   second ceiling remainder of (p, d). Hit ⟺ j = 1; genus ⟺ j ∈ □_u. The twisted layers N_c = 2#{j ≡ c} are the
>   representation counts of 1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup); c = −1 is the signed ES count; G is the
>   square-twisted average.
> * *Scoped closures (PROVED).* No bijection or bounded-to-one map of the shell realises the cancellation pointwise
>   (a hit must be balanced by ≍ φ(u)/2^{ω(u)} genus points); divisor switching acts on the index by j ↦ 2p̄/j (no sign
>   change); the ES surface xyz = x + y + p is multilinear, so no Vieta/Markoff involution exists.
> * *Assessment.* Modular-hyperbola equidistribution mod p (Weil) puts the hit at a single value of d̄ per shell point
>   and is short by a factor p^{1/2}/log² p; incidence, determinant, entropy and Heilbronn-type continued-fraction
>   statistics are polynomial-size or averaged tools.
> * *EVIDENCE (10⁹–10¹⁴, 1 000 primes + controls).* All 18 tested classes of the index behave like the hit class
>   (|z| ≤ 2.5, cross-class |ρ| ≤ 0.25, index uniform to ±0.002); the firing set has the pair statistics of a
>   genus-weighted random sample. Non-square twisted layers fluctuate identically at odd squares.
> * *Survives.* (CU) itself: a theorem on the divisors of ≍ U single integers p + u in one moving class mod u.

**Bottom line.** Every fresh coordinate system for the tied event — divisor switching, the level t, the modular
hyperbola mod p, SL₂ words and continued fractions, Dedekind sums, the c-twisted ES equations — exhibits the same
single integer, the class index j ∈ [1, u), and the exact layer is Σ f_u(j) over the shell with f_u supported on
{1} ∪ □_u. A hit is worth 1 − 1/|□_u| and can only be cancelled by ≍ |□_u| genus points, so no involution, switching
or descent mechanism can work, and the only fixed-p equidistribution tool with a power saving sees d̄ mod p at
resolution p^{1/2}, not 1. Numerically the hit class is in no way special among the classes of the index. What the
lane leaves is the clean statement of what a mechanism must do: control the class of divisors of ≍ U different
integers p + u modulo the moving u, at a single p, with error below log² p — B2 in its tied form, now with the
equivalent index/Kloosterman descriptions on record. **ES remains OPEN.**

## 7. Review log
(hostile review pending)
