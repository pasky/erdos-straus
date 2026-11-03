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

## 4. Mechanism map (what each fresh angle reduces to)

(filled in §4 of the final memo: switching involution; Vieta/Markoff; incidence/pencils; Kloosterman mod p; entropy;
polynomial method; additive combinatorics of the firing u; Dedekind sums.)

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
  10⁹,…,10¹⁴ (pooled over the six prime samples: −0.9 se). The signed class c = −1: +0.3, +1.5, +1.0, +0.1, +1.0, +1.4.
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

## 6. Screens, verdict, FRONTIER text, bottom line
(to be completed)

## 7. Review log
(to be completed)
