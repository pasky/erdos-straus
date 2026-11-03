# Z55_CROSSU — cross-u cancellation of the tied class events at fixed p: fresh angles, the class index, and what they reduce to

Status: z55 lane CROSSU (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z55_lanes.md` § CROSSU; reading list
restricted to `Z54_EXACTSUM.md` §0/§7, `Z53_GENUSX.md` §0/§4, `Z54_EXACTSPIN.md` §0/§8 — FRONTIER §§3–4 read only after
the tests, per kickoff). Internal; internal hostile review applied (§7). **ES is OPEN; nothing here proves or disproves
ES or (★) at any infinite set of primes, and no cancellation mechanism was found.** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z55_crossu_*`, data `data/z55/crossu/` (< 1 MB).
Notation from `Z53_GENUSX.md` §1 (cited **GX**).

## 0. Checkpoint log
* cp1 (161491b2): §1–§3, falsifier F1 (10⁹–10¹⁴), skeleton.
* cp2 (6c5f909b): mechanism map §4, falsifier F2, screens/verdict.
* cp3: internal hostile review (`data/z55/crossu/review_hostile.md`, 13 findings, "major revision") applied: the
  §4.1 "rigidity" claim rescoped (its |□_u| = 2 counterexample is acknowledged), switching and entropy statements
  corrected, all tool discussions relabelled Assessment, class-specific model variances, pairs test re-implemented
  with a set-valued null and bootstrap uncertainty, every quoted number regenerated from the stated populations.

## 1. Setting and the precise statement attacked

p ≡ 1 (mod 4) prime (the identities of §3 hold for every odd n ≡ 1 (4) with the stated gcd conditions). Window
(U₀, U₁, Y, X), family 𝔉 = {(u, w)}: u squarefree, u ≡ 1 (4), U₀ < u ≤ U₁, gcd(u, p) = 1; w odd squarefree in (Y, X],
gcd(w, up) = 1. Shell 𝔖 = {(u, w) ∈ 𝔉 : w | p + u}; level divisor d := (p + u)/(2w) (odd, gcd(d, u) = 1; GX writes w″).
𝔖₃ := {(u, w) ∈ 𝔖 : d ≡ 3 (4)}. Exact and genus layers (GX §1, level form):
  R_𝔉 = 2·#{(u,w) ∈ 𝔖₃ : d ≡ −1 (mod u)},   G_𝔉 = 2·Σ_{(u,w)∈𝔖₃} 1[−d ∈ □_u] / |□_u|,   □_u := (ℤ/u)^{×2}.
Standing range assumption (GX §4): Y ≥ U₁ and 8U₁X ≤ p, so d > 4U₁ ≥ u on 𝔖 (GX Lemma 4.1). Throughout u > 1
(U₀ ≥ 1); all j-statements exclude u = 1.

**Statement attacked (CONJECTURE; not claimed).**
  (CU)  R_𝔉(p) − G_𝔉(p) = o(log² p) as p → ∞ through primes p ≡ 1 (24), on a window family with M_𝔉 ≫ log² p.
*CONDITIONAL implication:* (CU) together with Theorem U of `Z53_GENUSLVAL.md` (M_𝔉 ≥ (c − o(1)) log² p with c > 0 on
its admissible windows, PROVED; GX cites it) and (X-w) (G_𝔉 − M_𝔉 = o(log² p), open), all three on one common
admissible window, gives R_𝔉 = M + (G − M) + (R − G) > 0, i.e. (★), for all large p. The numerical window of §5 is
not asserted to satisfy Theorem U's hypotheses. The kickoff asks for ANY mechanism producing cancellation of R − G *summed
over u at fixed p*, tested first numerically at 10⁹–10¹². Weaker sub-targets considered: (CU′) R_𝔉 ≥ εG_𝔉 for all large
p; (CU″) the same for a twisted or signed variant that still implies (★).

## 2. Why this is not already closed

* z54 EXACTSUM (Theorem N) closes *n-uniform block bounds* for the conductor/frequency blocks; EXACTSPIN closes direct
  complete-fibre averaging and fixed-order reconstruction. Both leave "cross-u cancellation inside a dyadic slice" as
  the surviving Assessment route. This lane looks for a *structural* reason (involution, descent, incidence,
  modular-hyperbola, continued-fraction) rather than a block-by-block estimate.
* The closed items (hyperbola dualization at fixed conductor; Cauchy–Schwarz in the function variable; low-conductor
  universality; bounded-order inverse lemmas; finite menus) are estimates within a *fixed* fibration. The ingredient
  tried here is to change the fibration (over d, over the level t, over the modular hyperbola mod p, over SL₂ words)
  and ask whether the class event becomes a non-tied event in some coordinates. §3 shows that in every coordinate
  system the per-point weight is a function of one residue, the class index j of Lemma A.

## 3. The class index (PROVED; the specific finite checks performed are listed in §5.1)

**Lemma A (class index).** Let (u, w) ∈ 𝔖 with u > 1, d = (p + u)/(2w). Let ū_d ∈ [1, d) be the inverse of u mod d
and put j := (u·ū_d − 1)/d. Then
 (a) j ∈ ℤ, 1 ≤ j ≤ u − 1, and j·d ≡ −1 (mod u), i.e. j ≡ −d^{−1} (mod u);
 (b) class hit (d ≡ −1 (mod u)) ⟺ j = 1;  genus (−d ∈ □_u) ⟺ j ∈ □_u;
 (c) (p prime) with d̄ := d^{−1} mod p in [1, p): d̄ = (2w + jp)/u, (d·d̄ − 1)/p = ū_d, and j = ⌊u·d̄/p⌋; equivalently
     (−p mod d)·(−p^{−1} mod d) = 1 + j·d, where −p mod d = u. Exactly: d̄/p = j/u + 2w/(up).
*Proof.* (a) u ū_d ≡ 1 (mod d) gives j ∈ ℤ; 1 ≤ ū_d ≤ d − 1 gives 0 < uū_d − 1 < ud, so 0 ≤ j < u, and j = 0 forces
uū_d = 1, impossible for u > 1. Reducing u ū_d = 1 + jd modulo u: jd ≡ −1. (b) From jd ≡ −1: d ≡ −1 ⟺ j ≡ 1; and
−d ∈ □ ⟺ −d^{−1} ∈ □ ⟺ j ∈ □. (c) 2wd = p + u gives u ≡ −p (mod d), hence ū_d ≡ −p^{−1} (mod d), and 0 < u < d
gives −p mod d = u; so u ū_d = 1 + jd is the displayed product identity. Next, e := (2w + jp)/u is an integer:
u | 2w + jp ⟺ j ≡ −2w·p^{−1} (mod u), and jd ≡ −1 with 2wd ≡ p (mod u) gives j ≡ −d^{−1} ≡ −2w p^{−1}. Then
d·e = (2wd + jpd)/u = (p + u + jpd)/u = (p(1 + jd) + u)/u = p ū_d + 1 ≡ 1 (mod p), and 1 ≤ e < p because
2w + jp < up ⟺ j ≤ u − 1 (as 2w < p). So e = d̄, (dd̄ − 1)/p = ū_d, and u d̄ = 2w + jp with 0 < 2w < p gives
j = ⌊u d̄/p⌋ and d̄/p = j/u + 2w/(up). ∎

*Reading.* On 𝔖 the class residue −d mod u, the inverse of u mod d, the inverse of d mod p and the second ceiling
remainder of (p, d) (Lemma B) all *determine* the same integer j ∈ [1, u) by the formulas above. The exact layer is
R − G = 2Σ_{𝔖₃} f_u(j), f_u(j) := 1[j = 1] − 1[j ∈ □_u]/|□_u|.

**Lemma B (SL₂/continued-fraction form).** (u, w) ∈ 𝔖 is a class hit iff the ceiling (Hirzebruch–Jung) Euclidean
algorithm on (p, d) terminates in three steps, p = 2w·d − u, d = t·u − 1, u = u·1, with t = (d + 1)/u, and t ≡ 0 (4) on
𝔖₃; equivalently [[p, −(2wt − 1)], [d, −t]] = M(2w)M(t)M(u) with M(a) = [[a, −1], [1, 0]], and d·(2wt − 1) = tp + 1.
In general the second ceiling remainder of (p, d) is (−d) mod u = j^{−1} mod u (so hits ⟺ second remainder 1).
*Proof.* p = 2wd − u with 0 < u < d is the first ceiling step; the second is d = ⌈d/u⌉u − r₂ with r₂ = (−d) mod u, and
r₂·j ≡ (−d)(−d^{−1}) = 1 (mod u) by Lemma A(a). r₂ = 1 ⟺ j = 1 ⟺ d = tu − 1. The matrix product is a direct
multiplication; its determinant identity reads d(2wt − 1) − tp = 1. t ≡ 0 (4): d ≡ 3 (4), u ≡ 1 (4) give
tu = d + 1 ≡ 0 (4). ∎

**Lemma C (twisted layers).** For an integer c put (summands with gcd(c, u) > 1 are zero by convention)
  N_c := 2·#{(u,w) ∈ 𝔖₃ : j ≡ c (mod u)},   G_c := 2·Σ_{𝔖₃, gcd(c,u)=1} 1[j ∈ c·□_u]/|□_u|,
  E_c := 2·Σ_{𝔖₃, gcd(c,u)=1} 1/φ(u).
Then N₁ = R_𝔉, G₁ = G_𝔉; for each u, Σ_{c ∈ (ℤ/u)^×} N_c|_u = Σ_c G_c|_u = 2·#𝔖₃|_u; and for c > 0
  N_c = 2·#{(u, w, t) : (u,w) ∈ 𝔉, d ≡ 3 (4), c·d + 1 = u·t}
     = 2·#{representations 1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup) with (u,w) ∈ 𝔉, (p+u)/(2w) ≡ 3 (4)},
while N_{−1} counts the *signed* representations 1/p = 1/(2wt′u) + 1/(2wt′p) − 1/(t′up) (d = ut′ + 1).
*Proof.* j ≡ c ⟺ cd ≡ −1 (mod u) ⟺ cd + 1 = ut; with 2wd = p + u, 2w(ut − 1) = c(p + u), i.e. 2wtu = cp + cu + 2w;
divide by 2wtu·cp. For c = −1, −d + 1 = ut with t < 0; write t = −t′. The coset sums are the orthogonality of the
cosets of □_u. ∎
*Reading.* G_𝔉 is the average of the square-twisted layers N_{x²} with the genus weights; each N_c is an ES-type
representation count (c = 1: type II for 4/p after t = 4C; c = −1: the signed count). So (CU) says the hit class c = 1
is not special among the c-twisted ES equations at fixed p.

## 4. Mechanism map: what each fresh angle reduces to

Each candidate mechanism of the kickoff was worked through in the coordinates of §3 before any numerics. Labels per
item; "Assessment" items record that the named standard tools do not yield the target and that no alternative was
found — they are not theorems excluding a mechanism.

**4.1 Weights on the shell (PROVED, elementary; scope stated).** Write q_u := |□_u| = φ(u)/2^{ω(u)}. The weight f(P) :=
f_{u(P)}(j(P)) of a point P ∈ 𝔖₃ takes the values 1 − 1/q_u (hit), −1/q_u (genus non-hit), 0 (off-genus), and
R − G = 2Σ f. By Lemma A, j is given in each coordinate system by
  j = −d^{−1} mod u = (u·(u^{−1} mod d) − 1)/d = ((−p mod d)(−p^{−1} mod d) − 1)/d = ⌊u·(d^{−1} mod p)/p⌋
  = ((−d) mod u)^{−1} mod u,
so every re-fibration of the sum (over u, over w, over d, over the level t = ū_d, over the modular hyperbola (d, d̄)
mod p, over SL₂ words) is the same sum of the same weights — a tautology, recorded only to fix what a mechanism must do.
*Elementary weight bound.* If every u in the window has q_u ≥ 3 (true for U₀ ≥ 5: among squarefree u ≡ 1 (4), only
u = 5 has q_u = 2), then f ≥ 2/3 at hits and f ≥ −1/3 at genus non-hits, so (i) no bijection σ of 𝔖₃ has
f∘σ = −f at a hit, and (ii) cancelling the weight of one hit pointwise needs at least 2 genus non-hits, and at least
q·(1 − 1/q_u) of them if their moduli all have q_{u′} ≥ q. At q_u = 2 (u = 5, windows with U₀ < 5) a hit and a genus
non-hit have opposite weights ±1/2 and a sign-reversing bijection can exist (reviewer's example p = 1 007 633 689,
U₁ = 5). *Growth of q_u (PROVED, elementary; cross-model review fix 1).* For squarefree odd u,
q_u/√u = ∏_{ℓ|u} (ℓ − 1)/(2√ℓ) ≥ (1/√3)(2/√5) = 2/√15, since every factor with ℓ ≥ 7 exceeds 1 and 3, 5 occur at most
once. Hence on a window with U₀ → ∞ (e.g. the standard U₀ ≈ p^{1/12}), q_min := min_{u ∈ 𝒰} q_u ≥ (2/√15)√U₀ → ∞.
Consequently, for any fixed K, once q_min > K + 1 a hit (weight ≥ 1 − 1/q_min) cannot be cancelled exactly by K genus
non-hits (total magnitude ≤ K/q_min): bounded-size exact zero-sum groups containing a hit are excluded on moving
windows for all large p. Only a *fixed* lower cutoff that admits u = 21 (q = 3) need not have growing q_min. *Scope.*
This is a pointwise, exact-cancellation obstruction for bounded groups; it says nothing about large groups,
approximate or grouped cancellation, or positivity inequalities. In particular it does **not** close
"pairing/switching/descent" as a class; it quantifies what such a map would have to do.

**4.2 Switching w ↔ d (PROVED identity; Assessment on use).** Where d is odd squarefree in (Y, X] with gcd(d, up) = 1,
(u, d) ∈ 𝔖 with level w; it lies in 𝔖₃ iff w ≡ 3 (4). On that domain the switch is a partial involution of 𝔖 with
index j′ ≡ 2p^{−1}·j^{−1} (mod u). (Proof: 2wd ≡ p (mod u) gives w^{−1} ≡ 2d p^{−1}, so −w^{−1} ≡ 2p^{−1}(−d) =
2p^{−1}j^{−1}.) So a hit goes to a hit iff u | p − 2, and to a genus non-hit iff 2p ∈ □_u and p ≢ 2 (mod u) — the
switch *can* reverse the sign of a hit's weight (reviewer's example p = 1 063 647 049, u = 89: (89, 23343, 22783, j = 1)
↔ (89, 22783, 23343, j = 32), weights +43/44 and −1/44). It is not weight-negating in general, and it acts on the
index multiset at fixed u by j ↦ 2p̄/j, a unit-group map that preserves the subgroup □_u setwise iff 2p ∈ □_u and
otherwise sends □_u to the coset 2p̄□_u (the switchable points are merely permuted, so the genus count of the
switchable multiset is unchanged in either case). *Assessment:* no
cancellation follows; whether a signed combination of a point and its switch has smaller fluctuation was not tested.

**4.3 Vieta/Markoff moves (PROVED, scoped).** With x = u, y = 2w, z = t the hits are the positive integer points of
S_p : xyz = x + y + p, and N_c those of S_{p,c} : xyz = cx + y + cp (Lemma C). Each variable occurs to degree 1, so for
any two fixed coordinates the third is determined: there is no coordinate-fibre involution of Vieta type (change one
coordinate, fix the other two), and the only coordinate permutation preserving S_p is x ↔ y (the u ↔ 2w symmetry,
which leaves the family). S_p is fibred by conics in three ways ((zx − 1)(zy − 1) = zp + 1 at fixed z, etc.), whose
integer points are divisor pairs. *Scope.* Transformations moving several coordinates at once are not excluded.

**4.4 Incidence geometry of the divisor surface (PROVED identity; Assessment on use).** In the (d, u)-plane the shell
points {(d, u) : d | p + u} are the lattice points on the pencil of lines u = kd − p through (0, −p); hits are those on
the pencil d = 4Cu − 1 through (−1, 0). The intersection of the lines with parameters (k, C) is a lattice point iff
4Ck − 1 | 4Cp + 1 (the C-form). *Assessment:* incidence bounds between the shell points and the pencil lines are
upper bounds of polynomial size; they neither bound R − G by o(log² p) nor give positivity.

**4.5 Fixed-p Kloosterman equidistribution (Assessment).** The modular hyperbola mod p is the standard object with a
fixed-p equidistribution statement carrying a power saving (Weil). Lemma A(c) places the hit there: (u, w) is a hit
iff d̄/p = 1/u + 2w/(up), and in general d̄/p = j/u + 2w/(up) — within 2X/(up) of the bottom of the bin [j/u, (j+1)/u),
the only non-determined datum being the bin index j. The completion bound for incomplete Kloosterman sums gives
#{d ∼ D : d̄/p ∈ I} = D|I| + O(p^{1/2} log² p); it is informative only for |I| ≫ p^{1/2+ε}/D, whereas the hit is one
integer value of d̄ per shell point and the shell is a sparse set (expected size ≍ U₁ log p out of D, selected by the
Diophantine condition −p mod d ≤ U₁; this expected size is a heuristic at fixed p except on the EXACTSUM windows).
With a target of size O(log² p) these particular estimates do not apply; the hybrid Weyl sums Σ_d e(h₁p/d + h₂d̄/p)
over the sparse set were not estimated here, and EXACTSUM's Theorem N (n-uniform blockwise bounds) does not by itself
exclude them. No alternative estimate was found.

**4.6 Entropy / union bounds (Assessment).** A hit is the congruence p ≡ −u (mod d) with d = 4uC − 1 ∈ [p^{1−γ}, p^{1−β}].
K hits with pairwise coprime moduli determine p modulo ∏d_i, which exceeds p once K(1 − γ) > 1 (the lower scale
p^{1−γ} must be used; with the upper scale the reviewer's example p = 1 007 633 689, hits d = 7419 and 134963, has
coprime product < p although K = 2 > 1/(1 − 1/3)). This counts integers n ≤ N with a prescribed hit tuple (a B6
average over n); at a fixed p it is void.

**4.7 Polynomial / determinant method (Assessment).** Upper bounds for integer points of S_p in a box are of
polynomial size in the box; the target is a lower bound of size 1 against a main term of size log² p.

**4.8 Continued fractions / Dedekind sums (PROVED identities; Assessment on use).** By Lemma B the hits are the d for
which the ceiling Euclidean algorithm on (p, d) has length 3. On 𝔖, with s(h, k) the Dedekind sum, s(d, u) = −s(j, u)
(as d ≡ −j^{−1} (mod u) and s(h̄, k) = s(h, k), s(−h, k) = −s(h, k)), and Rademacher reciprocity with u ≡ −p (mod d) gives
s(d, u) = s(p, d) + (u/d + d/u + 1/(ud))/12 − 1/4 (both checked numerically in the review); the hit is the extreme
value s(d, u) = −s(1, u) = −(u − 1)(u − 2)/(12u). *Assessment:* Heilbronn–Porter statistics of the Euclidean algorithm
at fixed numerator average over all d < p; length-3 expansions are ≍ log² p events (heuristically) out of p, below
the resolution of those averages as stated in the literature.

**4.9 Additive combinatorics of the firing set (EVIDENCE; §5.2).** Pair statistics of hits (gcd of the two u, gcd of
the two d, closeness of the u, divisibility u | u′) are within bootstrap uncertainty of a genus-weighted random
sample of the same size; the tests found no structure beyond the 1/φ(u) weighting.

**4.10 Correlation with a fixed multiplicative function (PROVED, scoped).** On 𝔖₃ reciprocity gives (d/p) = −(j/u)
(Jacobi symbol; GX Lemma 2 / B5: (d/p) = −1 at hits and at all genus points). So (·/p) is constant on each genus
coset at fixed u and cannot distinguish the hit class from the other classes inside □_u; its weighted inner product
with the exact layer is −(R − G) itself. A fixed f(u) or f(w) reweights fibres; no reweighting that exposes
cancellation was found (Assessment).

**4.11 Positivity transfer (CU′) (Assessment).** Positivity of the full (★) count would follow from any map taking
some genus point (u, w, x), x ≠ ±1, to a hit anywhere (non-empty genus support suffices); R_𝔉 ≥ εG_𝔉 would need
targets inside the family and a uniform bound on the weighted multiplicity of the map. The natural move t ↦ t x̄² (mod d) transports d | x² + pt to d | 1 + pt′ but
loses the second condition d ≡ −1 (mod t′): the transported point has the right modulus but an uncontrolled class
(a class-changing transfer, FRONTIER §4 item 11). No transfer found.

## 5. Falsifiers (EVIDENCE; identities CERTIFIED on the runs as stated)

### 5.1 F1: the twisted layers at 10⁹–10¹⁴
Engine `scripts/z55_crossu_engine.c` (compile `gcc -O2 -o /tmp/z55cu scripts/z55_crossu_engine.c -lm`; window as GX §5: (U₀,U₁,Y,X) = (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4); shell
enumeration as `z53_genusx_engine.c`). On every point of 𝔖₃ it computes j and checks: u·(u^{−1} mod d) = 1 + jd
(`badj`); Lemma A(c) — d^{−1} mod n = (2w + jn)/u, (d·d̄ − 1)/n = u^{−1} mod d, j = ⌊u d̄/n⌋ — whenever d^{−1} mod n
exists (`badA`, `nA`); Lemma B — ((−d) mod u)·j ≡ 1 (mod u) (`badB`). All three counters are 0 on all 1 339 runs
(3 014 093 points of 𝔖₃; nA = 3 014 093, i.e. d was invertible mod n on every point, including composites and
squares). Lemma C's representation identity is not machine-checked (it is a two-line algebraic consequence). R, G and
the shell counts were compared by hand with `z54_exactspin_engine` on the first n of each list (identical); no
comparison artifact is stored. Outputs: N_c, G_c, E_c and the class-specific model variance
V_c := 4Σ_{𝔖₃, j ∈ c□_u}(1/q_u)(1 − 1/q_u) (independent points, j uniform in its coset; V₁ = VRG of EXACTSPIN) for
c ∈ {1,…,12, 16, 25, −1, −2, −3, −4}; j/u histogram (10 bins). Driver `scripts/z55_crossu_run.py`, stats
`scripts/z55_crossu_stats.py`; data `data/z55/crossu/main.tsv`, `stats.txt`. Samples (the z53/z54 lists): 200 random
primes ≡ 1 (24) at 10⁹ and 10¹⁰, 150 each at 10¹¹–10¹⁴ (1 000 primes); 150 odd squares at 10⁸; 60 near-squares at 10¹⁰
and 10¹²; the 19 hard primes (14 (★)-zero + item-14 primes); 50 composites at 10¹⁰.

Findings (z_c := Σ(N_c − G_c)/√ΣV_c over a sample; "sd-ratio" := sd(N_c − G_c)/√mean V_c; all ranges are over the 18
classes and the six random-prime samples, read off `stats.txt`):
* mean(N_c − G_c) ∈ [−0.67, +0.59]; sd-ratio ∈ [0.875, 1.177]; z_c ∈ [−2.49, +1.91]. For the hit class c = 1:
  z = +1.54, −1.59, −0.01, −1.72, −1.88, +0.14 at 10⁹,…,10¹⁴; sd-ratio 1.04, 1.05, 0.97, 0.93, 0.92, 0.95. Pooled
  over the 1 000 primes: z₁ = −1.61, z₋₁ = +2.16, z₂ = −0.12, z₄ = −0.05, z₁₂ = +2.04, z₂₅ = +2.35; the 18 pooled values
  lie in [−1.78, +2.35]. Under the independent-fibre model the 18 classes are not independent of each other (they
  share the same shell), but three |z| ≈ 2 among 18 is unremarkable.
* Cross-class correlations: the largest |ρ| among the 153 pairs of classes is 0.24, 0.22, 0.21, 0.27, 0.24, 0.24 at
  10⁹,…,10¹⁴ (n = 200, 200, 150, 150, 150, 150), against ≈ 0.24–0.28 for the maximum of 153 independent sample
  correlations (√(2 ln 306)/√n) — a heuristic benchmark scale, not a calibrated null test (the classes share the
  shell). No pair involving c = 1 exceeds 0.26.
* Index marginal: the pooled j/u histogram (10 bins, all 𝔖₃ points) has maximum deviation from 0.1 of 0.0018, 0.0035,
  0.0014, 0.0009, 0.0008, 0.0005 at 10⁹,…,10¹⁴ (N up to 1.6·10⁶). Restricted to genus points the histogram is not
  flat (e.g. bins 0.108, 0.103, 0.102, 0.093, 0.097, 0.097, 0.094, 0.106, 0.100, 0.102 at 10¹²): the perfect squares
  j = x² < u all lie in □_u and sit at small j/u, and the remaining shape is that of the quadratic residues of
  composite u ≡ 1 (4), which was not analysed. These are binned marginals only; they do not test uniformity on every
  unit class at each u.
* Controls. Odd squares n = m²: N_c = G_c = V_c = 0 on every square for exactly the seven classes
  c ∈ {1, 4, 9, 16, 25, −1, −4}, i.e. those with Jacobi symbol (c/u) = +1 for every u ≡ 1 (4) coprime to c (e.g.
  (9/21) = 0, and such summands are zero by the Lemma C convention). This is forced (PROVED,
  elementary): the identity of §4.10 holds for every odd n ≡ 1 (4) coprime to d, (d/n) = −(j/u), and at n = m² the left
  side is +1, so (j/u) = −1 on all of 𝔖₃ — in particular the genus is empty (GX Lemma 3.3) and no class with (c/u) = +1
  is populated. The remaining eleven classes fluctuate with sd-ratio
  ∈ [0.84, 1.08] as at primes — the T1 vanishing is a property of the genus coset, not of the fluctuation of the
  exact layer. Near-squares and composites (n = 60, 60, 50): sd-ratio spreads 0.71–1.25, 0.85–1.15, 0.78–1.28,
  broadly comparable to the prime samples but wider.
  Hard primes (19): the 14 (★)-zero primes have R = 0; the five smallest have 𝔖₃ = ∅, 83449 and 102001 have one
  off-genus point (G = 0), the other seven have G = 0.10–1.90; p = 3361 has R = G = 2, p = 5101441 has R = 2, G = 1.52.
  Mean R − G = −0.39, sample sd 0.68. The family's deficit at these primes is that of a 0–26-point shell.
* G_c − E_c (genus prediction minus uniform prediction) is within ±0.08 for c = 1 at every random-prime sample.
Assessment: at these sizes the hit class is not distinguished by any of the tested statistics from the other 17
classes of the index; the tests detect residue-class bias and cross-class correlation only and cannot falsify or
support an o(log² p) bound.

### 5.2 F2: structure of the firing set
`scripts/z55_crossu_pairs.py` on per-point dumps of the 300 primes at 10¹²–10¹³ (769 hits, 967 hit pairs with
u₁ ≠ u₂). Reproduction (dumps not stored, ≈ 60 MB): for each n in `data/z53/genusx/primes_1e12.txt` and
`data/z54/exactsum/primes_1e13.txt`, run `/tmp/z55cu n U0 U1 Y X DUMPDIR/n.txt` with the window from
`z55_crossu_run.window(n)` (the same values as in `main.tsv`), then `python scripts/z55_crossu_pairs.py DUMPDIR 20 200`
(seed 1). Descriptive null: |H| distinct genus points drawn
without replacement with probability ∝ 2^{ω(u)}/φ(u) (the G-weight of a hit), 20 draws per prime; this is a benchmark,
not the exact conditional law of the independent-genus model. Uncertainty: bootstrap over the 300 primes (200
resamples) of the hit-minus-null difference.
  gcd(u₁,u₂) > 1 :  hits 12.4 %  null 11.3 %  diff +1.2 %  [−1.4, +4.0]
  gcd(d₁,d₂) > 1 :  hits 22.1 %  null 19.1 %  diff +3.0 %  [−1.0, +7.6]
  |u₁ − u₂| ≤ U₁/20: hits 40.4 %  null 36.1 %  diff +4.3 %  [−0.4, +8.8]
  u | u′          :  hits  2.0 %  null  1.4 %  diff +0.6 %  [−0.3, +1.8]
(mean u: hits 1 206, null 1 402). All four differences are positive but each 95 % interval contains 0; the closeness
statistic is at the edge. EVIDENCE: no structure established; a weak excess of close-u hit pairs is not excluded by
this sample. Neither F1 nor F2 establishes or refutes (CU): they are finite descriptive experiments against heuristic
benchmarks. Data: `data/z55/crossu/pairs_1e12_1e13.txt`.

## 6. Screens, verdict, FRONTIER text, bottom line

**The four FRONTIER §4 hard screens, applied to the route "cross-u cancellation of the class index" (Assessment):**
1. *T1 (squares).* Not binding for (CU): at odd squares R = G = 0 (GX Lemma 3.3), and F1 shows the non-square twisted
   layers fluctuate at squares as at primes. The square-sensitive steps of the route are Thm U and (X-w), not (CU);
   a mechanism for (CU) need not use the character of p — which is also why the fixed-p tools that see p only
   through (·/p) do not engage it.
2. *8/131.* Not applicable to (CU) (a remainder bound); the 4 enters through t ≡ 0 (4) on 𝔖₃ (Lemma B).
3. *Tied modulus (B2).* Fails: in every coordinate of §3 the hit is one residue class mod the moving u (one value of
   d̄ mod p per shell point), and no re-fibration tried here untangles it.
4. *Fixed p.* Every identity holds at fixed p; the one standard fixed-p equidistribution with a power saving (§4.5)
   is below the required resolution.

**Verdict: inconclusive on the target; narrowed only by elementary reformulations.**
* *PROVED, structural.* Lemma A (three forms of the class index), Lemma B (length-3 ceiling expansion), Lemma C
  (twisted layers = ES-type representation counts for 1/(cp); G = their square-twisted average); §4.1 weight bound
  (no pointwise sign-reversing bijection when q_u ≥ 3; no exact cancellation of a hit by a bounded number of genus
  non-hits on moving windows, as q_u ≥ (2/√15)√U₀); §4.2 switching index j ↦ 2p̄/j; §4.3 no coordinate-fibre
  Vieta involution; §4.10 (d/p) = −(j/u). These are reformulations and small scoped facts, not closures of mechanism
  classes.
* *EVIDENCE.* At 10⁹–10¹⁴ the hit class is not distinguished from 17 other classes of the index by means, variances or
  correlations; the index marginal is flat to ±0.004; the firing set's pair statistics are within bootstrap
  uncertainty of a genus-weighted sample. These tests cannot falsify or support (CU).
* *Found no mechanism.* None of the angles in the kickoff (switching, Vieta/Markoff, additive combinatorics of the
  firing set, entropy, polynomial method, geometry of the divisor surface, fixed multiplicative functions) produced a
  cancellation or a positivity transfer. **Assessment:** what the lane leaves is the statement of what a mechanism must
  do — control the class of divisors of ≍ U different integers p + u modulo the moving u at a single p with error
  below log² p (B2 in tied form) — now with the index/Kloosterman descriptions on record.

**Proposed FRONTIER §7 text** (append to item 3, after the EXACTSPIN entry):
> *(z55, `Z55_CROSSU.md`, internal review applied.)* Cross-u cancellation of the exact class layer R − G on the Thm U
> family: fresh-angle sweep, no mechanism found.
> * *Class index (PROVED).* On a shell point (u, w) with level d, the class residue −d^{−1} mod u is the integer
>   j = (u·(u^{−1} mod d) − 1)/d ∈ [1, u) = ((−p mod d)(−p^{−1} mod d) − 1)/d = ⌊u·(d^{−1} mod p)/p⌋, and the second
>   ceiling remainder of (p, d) is j^{−1} mod u. Hit ⟺ j = 1; genus ⟺ j ∈ □_u; (d/p) = −(j/u) on 𝔖₃. The twisted
>   layers N_c = 2#{j ≡ c} are the representation counts of 1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup) (c = −1: signed
>   ES); G is their square-twisted average.
> * *Elementary facts (PROVED, scoped).* For windows with q_u = |□_u| ≥ 3 no bijection of the shell reverses the
>   weight of a hit pointwise (a hit must be balanced by ≥ 2 genus non-hits); divisor switching acts on the index by
>   j ↦ 2p̄/j (it can reverse a hit's sign; no cancellation follows); the ES surface xyz = x + y + p is multilinear,
>   so no one-coordinate Vieta involution exists. On moving windows q_u ≥ (2/√15)√U₀ → ∞, so for every fixed K a
>   hit cannot be cancelled exactly by K genus non-hits for large p (bounded exact groups excluded; large groups,
>   approximate cancellation and positivity maps are not).
> * *Assessment.* Kloosterman equidistribution mod p places the hit at d̄/p = 1/u + 2w/(up), one value per sparse-shell
>   point, below Weil resolution; incidence, determinant, entropy and Heilbronn-type statistics are polynomial-size
>   or averaged tools. No positivity transfer from genus points to hits was found.
> * *EVIDENCE (10⁹–10¹⁴, 1 000 primes + controls).* 18 classes of the index: means within ±0.7, sd-ratios 0.88–1.18,
>   |z| ≤ 2.5, largest cross-class |ρ| at the level of 153 independent correlations; index marginal flat to ±0.004;
>   firing-set pair statistics within bootstrap uncertainty of a genus-weighted sample.
> * *Survives.* (CU) itself: control of the divisors of ≍ U single integers p + u in one moving class mod u.

**Bottom line.** Every fresh coordinate system for the tied event — divisor switching, the level t, the modular
hyperbola mod p, SL₂ words and continued fractions, Dedekind sums, the c-twisted ES equations — exhibits the same
integer, the class index j ∈ [1, u), and the exact layer is Σ f_u(j) over the shell with f_u supported on {1} ∪ □_u.
A hit carries weight 1 − 1/q_u and a genus non-hit −1/q_{u′}, so pointwise cancellation needs at least two (and at
least q(1 − 1/q_u) if all moduli have q_{u′} ≥ q) genus non-hits per hit — on moving windows more than any fixed
number, since q_u ≥ (2/√15)√U₀ — and no pairing found here does it; the standard fixed-p equidistribution tool resolves d̄ mod p at scale p^{1/2}, not 1.
Numerically the hit class is not special among the classes of the index. The lane found no cross-u mechanism; it
leaves the precise target in index form. **ES remains OPEN.**

## 7. Review log

**Internal hostile review** (deep-mode subagent; `data/z55/crossu/review_hostile.md`; verdict "major revision", 13
findings). Independent numerical checks confirmed Lemmas A–C and both Dedekind identities, the engine's genus/coset/
histogram implementation (sampled against an independent enumeration), and the pooled c = 1 value. Findings applied:
1 (blocking) §4.1 rigidity claim false at q_u = 2 and overscoped → rescoped to the elementary weight bound with the
q_u ≥ 3 hypothesis, all "closure of mechanism classes" language removed from §4.1, §6, FRONTIER text, bottom line;
2 switching "changes no sign" false → corrected, domain (w ≡ 3 (4)) and partial-involution status stated;
3 entropy threshold β → γ, typical-count assertion dropped; 4 analytic/geometric exclusions → Assessment, upper-bound
wording, hybrid sums acknowledged as unestimated; 5 class-specific variances V_c added to the engine and stats;
6 all numerical ranges regenerated over the 18 classes and stated populations (sd-ratio 0.875–1.177, means ±0.67,
max |ρ| 0.27, histogram deviation ≤ 0.0035); 7 pairs script rewritten (U₁ from the window, singleton-mean bug fixed,
no-replacement weighted null, bootstrap CIs; conclusions softened accordingly); 8 histogram readings softened and
the false "j ≤ √u" parenthetical replaced; 9 orthogonality claim withdrawn, (d/p) = −(j/u) stated; 10 "same integer"
→ "determine", interval → exact equality, u = 1 excluded, Lemma C unit convention; 11 the engine's checks enumerated
precisely (Lemma A(c)/B now machine-checked on all runs; Lemma C not); 12 hard-prime description corrected; 13 labels
separated, §1 implication marked CONDITIONAL, (CU) labelled CONJECTURE, review reference fixed.

**Second hostile pass** (`data/z55/crossu/review_hostile_pass2.md`; verdict "accept with fixes"; all 13 original
findings given explicit dispositions, the q_u ≥ 3 arithmetic, the Jacobi identity (d/p) = −(j/u), the corrected
threshold, the engine checks and all quoted statistics independently re-verified). Six residual items applied:
R1 §4.1 scope sentence and bottom line (the pass-2 wording "q_min → ∞ fails in every window" was itself wrong and
is corrected by the cross-model review, see below); R2 §4.2 setwise-vs-multiset
wording; R3 the seven vanishing classes at squares (now explained as a PROVED consequence of (d/n) = −(j/u)), control
spreads stated separately, "share" not "partition"; R4 §3 heading; R5 §4.11 distinction between full-(★) positivity and
R_𝔉 ≥ εG_𝔉; R6 reproduction recipe for the pair run.

**Cross-model review** (`data/z55/xreview/REVIEW_CROSSU.md`, audit script `scripts/z55_xrev_crossu_check.py`; verdict
ACCEPT-WITH-FIXES; every PROVED claim independently re-derived, all 1 339 rows replayed field-for-field, seven
independent shell enumerations, pair run reproduced byte-for-byte). Fixes applied: (1) §4.1 — the pass-2 sentence
"q_min → ∞ fails in every window" was wrong: q_u ≥ (2/√15)√u for squarefree odd u, so on moving windows q_min → ∞ and
bounded-size exact cancelling groups containing a hit are excluded for large p (also in §6, the FRONTIER text and the
bottom line); (2) Theorem U's source corrected to `Z53_GENUSLVAL.md` with the common-window hypothesis made explicit
in §1, and the coprime-u quantifier added to the square-vanishing classes; (3) caveats kept explicit: the maximum-
correlation scale is a heuristic benchmark, the pair null is descriptive, and neither experiment establishes or refutes
(CU). No cross-u cancellation theorem or mechanism-class closure is banked.
