# Z56_FAMATTACK — joint attack on positivity of the full (★) count R(p)

Status: z56 lane FAMATTACK (brief `z52bbriefs/z53_depth.md` + `z56_lanes.md` §3). Internal; internally reviewed only
(§8). **ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famattack_*`, data
`data/z56/famattack/` (8 MB).

## 0. Summary

**Verdict: narrowed** (with a modest main-term strengthening). The target — R(p) ≥ 1 for every large prime p ≡ 1 (4) —
is **not** proved. The lane combined the tools jointly and asked specifically whether the *union over windows* gives an
inequality that no single window gives. It does not, in any form found here, and the data say why: the windows are
linked, but **positively**.

* **Prop T (PROVED, unconditional, effective; §2.1).** Tiling Thm U over finitely many thin u-strips gives
  **M_gen(p) ≥ (64/(45π⁴) − ε)·log²p ≈ 0.01460·log²p** for p ≥ p₀(ε), i.e. 2.13 × Thm U's 2/(3π⁴). The same tiling of
  GENUSX Thm X windows gives an exact-class density main term **≥ (28/(75π⁴) − ε)log²p ≈ 0.00383 log²p** (1.97 × c_X)
  with T_u = O(p^{−δ}log p) on every tile (Prop T′). Both are ≈ 2.5–10 % of the full mean 3/(2π²)·log²p ≈ 0.152 log²p.
* **Thm J (PROVED reduction; §2.2).** The joint decomposition over a tiling 𝒯: R(p) ≥ Σ_t M^cls_t + Σ_t E_t, with
  E_t = T_w + T_uw the exact-divisor layers. So the joint attack reduces (FA ⇐) to the **tiled exact-layer bound**
  (CU_𝒯): Σ_t E_t(p) ≥ −(1 − ε)Σ_t M^cls_t(p). Combining tools moves only the main term; the residual is the union of
  the same exact layers that were open window by window.
* **Lemma L (PROVED; §2.3): the complete list of exact cross-window links** for windows in the shift variable u
  (each window's count is a function of the factorisations of its own integers p + u): (a) the switch, which
  makes the hit matrix symmetric (H_jk = H_kj) — a positive link; (b) privacy of primes ℓ > |u − u′|; (c) small-prime
  congruences (B1); (d) the χ_p-parity law per integer, which forces only the BM coset; and, at density level, (e)
  global order-≥3 drivers are O(p^{−δ}) on Thm X tiles. None of these can force a hit in one window from emptiness of
  another (Assessment, scoped in §2.3).
* **Prop V (PROVED, elementary; §2.4).** A pointwise single-p variance bound across windows that excludes R(p) = 0 is
  itself a weighted first-moment lower bound for R(p); CROSSO-type dual-large-sieve variance bounds over p give a single
  prime only the whole sum. "Pointwise via variance" is not an easier target.
* **Falsifier F1 (EVIDENCE, pre-registered; §3.2).** On 108 397 + 48 139 primes (all p ≡ 1 (4) in
  [10⁸, 1.04·10⁸] and [10⁹, 1.002·10⁹]) plus a 23 928-prime hold-out at 1.2·10⁹, exact window counts show:
  windows in C (disjoint integer sets {4Cp + 1}) are **positively** associated (within-p-mod-840 correlations up to +0.48,
  surviving L(1, χ_p) controls: up to +0.45); zero events are positively associated (P(both empty)/product = 1.24–2.12;
  u-window MH odds ratio 1.8–1.9); the residual off-diagonal covariance is positive (+3 % to +31 % of the total residual
  variance). Two pairs crossed the pre-registered −4 s.e. line. C-windows (3,4) are both congruence-determined
  (4uB ≤ p^{0.4}), so their sign is a Haar-measure property of residues (B1). The other, u-windows 0 and 1 (−0.06,
  z ≈ −14), was pushed: it halves under finer
  local controls (−0.024 at 1330 residue columns), is not explained by medium-prime competition (privacy), and lives
  between the small-u lines and a single neighbouring window — a congruence-scale effect of size −0.02…−0.08 in
  correlation, against positive associations up to +0.4. **"Compensation through disjoint windows" is killed at the
  resolution of the data** (EVIDENCE; it cannot kill a pointwise theorem).
* **Global drivers depress all windows together (EVIDENCE; §3.4).** At 965 near-square primes p = m² + k near 10⁹, every
  u- and C-window is depressed (pooled per-window ratios 0.81–0.95 of matched generic means; total 0.86). The T1 deformation is cross-window.
* **Calibration (CERTIFIED; §3.5).** Among n ≡ 1 (4), n ≤ 7 999 801: R(n) = 0 at exactly 13 primes (the known ones),
  all 1 413 odd squares, and **285 non-square composites**, with no decline per decade (60, 95, 97 in the decades from
  10⁴). At these the genus main term is up to M_gen = 24.3 (n = 810 001 = 241·3361) while R*(n) = 0; at the prime zero
  8 813 281, M_gen = 29.1. So "genus main term + non-squareness" cannot carry any union argument; primality must enter
  beyond the Jacobi character.
* **Model scale (Assessment; §3.6).** Pure Poisson with hits ~ Poisson(c log²p): the full count (c ≈ 0.081 measured)
  predicts ≈ 11.8 zero primes in total (observed 14); the best tiled genus family (c = c_tile/2 = 0.0073) predicts
  ≈ 10¹⁴ zeros with expected-tail-count crossover near 10⁵⁷. Only families with mean close to the full count have a
  checkable threshold.

**Where it stops (§4).** Every joint inequality found reduces to (CU_𝒯), which is a pointwise lower tail for a sum of
positively associated Poisson-like counts with total mean ≍ log²p — B2 in tied form. The step that would make the union
work is a *negative* association (repulsion) mechanism between exact layers of different windows at one p; the only
negative links that exist (privacy, congruence competition) act on sizes or small primes, not on the class mod 4u.

## 1. Statements attacked

R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1); R is even for odd n (u ≠ B) and R(n) = 2·#{u < B}.

* **(FA)** ∃p₀: R(p) ≥ 1 for all primes p ≡ 1 (4), p > p₀. (CERTIFIED: R(p) = 0 at exactly 14 primes p ≡ 1 (4) below
  10¹⁰; largest 8 813 281.) Not proved.
* **(FA-W), joint-window form.** Partition the solution set into windows 𝒲_j (size conditions on u, B, C), R = Σ_j R_j,
  main terms M_j, remainders X_j = R_j − M_j. FA ⇐ Σ_j X_j ≥ −(1 − ε)Σ_j M_j with Σ_j M_j → ∞. Question (brief): does the
  joint structure give this when no single window does?
* **(CU_𝒯)** (defined in §2.2): Σ_{t∈𝒯} E_t(p) ≥ −(1 − ε)Σ_t M^cls_t(p) for p > p₀. CONJECTURE-strength, not claimed.
  It is the tiled form of CROSSU's (CU).

Why not already closed: Thm U / Thm X / CROSSF / CROSSO / CROSSU each treat one window family. No previous memo treats
the union, the cross-window dependence, or tiles the Burgess windows (GENUSLVAL Remark (1) mentions only a single-window
large-sieve variant). Closed items used, not redone: one-step hyperbola, Fejér/E–T, Cauchy–Schwarz in the function
variable, low-conductor universality, Fourier minorants with proper-subgroup support (CROSSF §2.4(a)).

## 2. Proved

### 2.1 Proposition T (tiling the Thm U windows; PROVED, unconditional, effective)

**Statement.** For every ε > 0 there is an effective p₀(ε) such that every prime p ≡ 1 (4), p ≥ p₀(ε), satisfies
  M_gen(p) ≥ (64/(45π⁴) − ε)(log p)² ≈ 0.014601·(log p)².
More generally, for τ = τ_r = (r+1)/(4r) (r ≥ 3 fixed) the constant is (8/π⁴)·|Ω_τ| − ε with
  Ω_τ := {(a, b) : τ²/(1 − τ²) < a < (1 − τ)/(1 + τ), τ(1 + a) < b < 1 − a}, |Ω_{1/4}| = 8/45.

**Proof.** Inputs: `Z53_GENUSLVAL.md` Lemma 2.3, Props 2.4, 2.5 and the argument of §2.7, used *verbatim per window*.
(i) *Per-window bound.* For fixed exponents (α₀, α₁, β, γ) satisfying (C1) γ < 1 − α₁, (C2) β > τ(1 + α₁) + 4ε′,
(C3) α₀ > τ²(1 + α₁) + 3ε′ (τ = τ_r + rε′), GENUSLVAL §2.7 proves
  Σ_{u∈𝒰}Σ_{w∈𝒮_u∩(Y,X]} 𝔤(u, w) ≥ (c(α₀, α₁, β, γ) − o(1))(log p)²,  c = (8/π⁴)(γ − β)(α₁ − α₀),
where 𝔤(u, w) ≥ 0 is the total genus weight of the two pairs (u, 2w), (2w, u) ∈ 𝒫(p); this is exactly the displayed
chain "M_gen(p) ≥ Σ_{u∈𝒰}Σ_w (genus weight …) ≥ (γ − β)log p·Σ_u H_uL/φ(u) − O(p^{−δ}log²p) ≥ …" with its first
inequality removed. The o(1) is effective and depends only on (r, ε′, α₀, α₁, β, γ).
(ii) *Tiling.* Fix η > 0 and a partition τ²/(1 − τ²) + η = a₀ < a₁ < … < a_K = (1 − τ)/(1 + τ) − η of mesh h. For strip
i put (α₀, α₁) = (a_{i−1}, a_i), β_i = τ(1 + a_i) + 5ε′, γ_i = 1 − a_i − ε′. (C1), (C2) hold by construction; (C3)
needs a_{i−1}(1 − τ²) > τ² + τ²h + 3ε′, which holds for all i once η(1 − τ²) > τ²h + 3ε′; β_i < γ_i needs
a_i < (1 − τ − 6ε′)/(1 + τ), true for ε′ small given the margin η.
(iii) *Disjointness.* Strips have disjoint u-ranges (U₀ < u ≤ U₁ with U = p^{a}), and the pairs (u, 2w) (odd first
entry) and (2w, u) (even first entry) of different (u, w) are distinct. All terms of M_gen are ≥ 0 (GENUSLVAL §1). So
  M_gen(p) ≥ Σ_{i=1}^K Σ_{u∈𝒰_i}Σ_w 𝔤(u, w) ≥ Σ_i (c_i − o(1))(log p)²,
a finite sum (K fixed before p → ∞), hence ≥ (Σ_i c_i − o(1))(log p)² with effective o(1).
(iv) *Limit.* Σ_i c_i = (8/π⁴)Σ_i (γ_i − β_i)(a_i − a_{i−1}) is a Riemann sum (right endpoints) of
(8/π⁴)∫(1 − a − τ(1 + a))da over [a₀, a_K], up to O(ε′); letting h, η, ε′ → 0 and r → ∞ (τ → 1/4) it tends to
(8/π⁴)|Ω_{1/4}|, and |Ω_{1/4}| = ∫_{1/15}^{3/5}(3/4 − 5a/4)da = [3a/4 − 5a²/8]_{1/15}^{3/5} = 9/40 − 17/360 = 8/45.
All choices are made before p → ∞, so for each ε one finite tiling suffices. ∎

*Remarks.* (1) Thm U's single rectangle has (γ − β)(α₁ − α₀) ≤ 1/12; the strip union has area 8/45 ≈ 0.178, ratio 2.13.
(2) GENUSLVAL Remark (1)'s Heath-Brown-large-sieve variant (α₀ → 0, Assessment there) would tile to area 9/40,
c ≈ 0.01848 (Assessment; not proved here). (3) Share of the full mean: 0.01460/(3/(2π²)) = 9.6 %. If every parity /
squarefree / residue subfamily on the same Burgess region were genus-exact (Assessment), the ceiling of this region
in the ordered-pair plane is (3/π²)|Ω ∪ Ω^T| ≈ 0.0979 (64 %) (`data/z56/famattack/tiling.txt`, grid estimate). The
remaining third needs w-windows below (4up)^{1/4} or u ≥ p^{3/5}, where Burgess gives nothing. (4) T1 audit: the
square-sensitive step is GENUSLVAL Prop 2.4(2) in each strip; at n = m² every strip's S_{η_{u,1}} = S_1 cancels exactly
(GENUSLVAL §2.8), consistent with M_gen(m²) = 0.

### 2.2 Proposition T′ and Theorem J (the joint reduction; PROVED)

**Prop T′.** Same construction with GENUSX Thm X's conditions (C1) γ < 1 − α₁, (C2*) β > 2α₁ + τ + 4ε′, (C4) α₁ < 1/5
plus (C3): the strip region is Ω_X = {1/15 < a < 1/5, 2a + 1/4 < b < 1 − a} (τ → 1/4), |Ω_X| = [3a/4 − 3a²/2]_{1/15}^{1/5}
= 9/100 − 13/300 = 7/150. For every ε > 0 there is a finite tiling 𝒯 with, for p ≥ p₀(ε),
  Σ_{t∈𝒯} M^cls_t(p) ≥ (28/(75π⁴) − ε)(log p)² ≈ 0.003833 (log p)²,  Σ_t |T_{u,t}(p)| = O(p^{−δ}log p).
(GENUSX's single-window optimum is c_X = (8/π⁴)·121/5120 ≈ 0.001941; 7/150 ÷ 121/5120 = 1.97.)
*Proof.* As Prop T, with Thm X applied per strip (finitely many; each gives T_u = O(p^{−δ_t}log p), take δ = min δ_t;
M^cls_t = M_t + T_{u,t} and M_t ≥ (c_t − o(1))log²p by (i) above). M^cls ≥ 0 termwise (A ∈ {0,1}, B^gen ≥ 0). ∎

**Theorem J (joint reduction).** For a finite tiling 𝒯 of Prop T′, and every prime p ≥ p₀,
  R(p) ≥ Σ_{t∈𝒯} R_t(p) = Σ_t M^cls_t(p) + Σ_t E_t(p),  E_t := R_t − M^cls_t = T_{w,t} + T_{uw,t},
with Σ_t M^cls_t ≥ (28/(75π⁴) − ε)log²p. Hence (CU_𝒯) ⇒ R(p) ≥ (ε·28/(75π⁴) − o(1))log²p ⇒ (FA).
*Proof.* R(p) counts all ordered triples; the tiles' families are disjoint subsets of 𝒫(p) (Prop T (iii)), so
R ≥ Σ_t R_t. GENUSX Lemma 1: R_t − M_t = T_u + T_w + T_uw and M^cls_t = M_t + T_u, so R_t − M^cls_t = T_w + T_uw. ∎

*Reading (Assessment).* "All tools jointly" = Thm U + Thm X on every tile + disjoint union. What is left is exactly the
union of the per-tile exact-divisor layers. The union helps only if those layers compensate across tiles; §2.3 lists every
exact link and §3 measures the dependence.

### 2.3 Lemma L (the exact cross-window links; PROVED) and what they can force (Assessment)

Use *ordered* u-windows: a partition ℕ = ⊔_j W_j, R_j(n) := #{(u, B, C) : u ∈ W_j} and H_jk(n) := #{(u, B, C) : u ∈ W_j,
B ∈ W_k}.

**Lemma L.** For odd n:
(a) R_j(n) = Σ_{u∈W_j} #{m | n + u : m ≡ −1 (mod 4u)}, a function of the factorisations of the integers {n + u : u ∈ W_j}
    only; the integer sets of different windows are disjoint.
(b) (switch) H_jk = H_kj, and R_j = Σ_k H_jk = Σ_k H_kj. Each solution (u, B, C) with u ∈ W_j, B ∈ W_k (j ≠ k) is counted
    once in R_j and once in R_k; it is a divisor event of three integers, n + u = B(4uC − 1), n + B = u(4BC − 1),
    4Cn + 1 = (4uC − 1)(4BC − 1).
(c) (privacy, `SYNTHESIS_SPARKS8.md` Lemma 2.3) a prime ℓ ∤ u − u′ divides at most one of n + u, n + u′; in particular a
    prime ℓ > max W_j ∪ W_k − min W_j ∪ W_k divides at most one integer of the two windows.
(d) (parity) for a prime p, ((p + u)/p) = (u/p), so p + u has an odd number of prime factors ℓ with (ℓ/p) = −1 iff
    (u/p) = −1; every hit divisor m ≡ −1 (4u) of p + u has (m/p) = −1 (CROSSO Lemma 1.1 / Lemma CT).
*Proof.* (a) For fixed u, n = 4uBC − u − B ⇔ B | n + u and m := (n + u)/B ≡ −1 (mod 4u) (then C = (m + 1)/(4u));
this is the trial form of FRONTIER §2.1, valid for every odd n (no gcd condition is needed in the triple form).
(b) (u, B, C) ↦ (B, u, C) is an involution of the solution set (the equation is symmetric in u, B); it maps
{u ∈ W_j, B ∈ W_k} onto {u ∈ W_k, B ∈ W_j}. The three factorisations are expansions of 4uBC − u − B = n.
(c) ℓ | (n + u) − (n + u′) = u − u′. (d) Multiplicativity of the Legendre symbol, and the cited lemma. ∎

*What the links can force (Assessment, with the scoped facts used).* (b) is a positive link: a hit in W_j with B ∈ W_k is a
hit in W_k. It moves solutions between windows; it never creates one. (c) is the only exact *negative* link between
different integers; it constrains which integer a large prime divides (sizes), not its class mod 4u — and the class is
what a hit needs. (d) forces a non-residue prime factor in every p + u with (u/p) = −1, which by (d) places divisors in
the BM coset {χ_{−4u} = −1}; that layer is already pointwise free (FRONTIER §2.4, (J)103 Prop 2.2) and is inside Thm U.
Small-prime congruences are B1. At density level, the global order-≥3 driver of all windows — the order-k Kummer
symbol of p (EXACTSPIN Lemma 4.1) — contributes O(p^{−δ}) on Thm X tiles (Thm X / Prop T′), so it cannot link windows
there either way. Nothing in (a)–(d) relates *the class mod 4u of a divisor of n + u* to the class mod 4u′ of a divisor of
n + u′ for u ≠ u′ beyond small primes and quadratic parity; this is CLASS_FORCING Thm 2.1 / §3 "privacy" in cross-window
language. No theorem excluding other links is claimed.

### 2.4 Proposition V (single-p variance is a first moment in disguise; PROVED, elementary)

Let R_j ≥ 0, M_j > 0, w_j ≥ 0 (j = 1…J) be reals, V ≥ 0.
(i) If Σ_j w_j(R_j − M_j)² ≤ V then Σ_j w_jM_jR_j ≥ ½(Σ_j w_jM_j² − V).
(ii) If all R_j = 0 then Σ_j w_j(R_j − M_j)² = Σ_j w_jM_j². Hence a pointwise variance bound excludes R = 0 iff
     V < Σ_j w_jM_j², and then (i) gives the weighted first-moment bound Σ_j (w_jM_j)R_j ≥ ½(Σ_j w_jM_j² − V) > 0.
(iii) (extraction from an average) If Σ_{p∈𝒫}|X(p)|² ≤ V_𝒫 over a set 𝒫 of primes, the only pointwise consequence is
     |X(p₀)|² ≤ V_𝒫; to exclude X(p₀) = −M(p₀) one needs V_𝒫 < M(p₀)², i.e. an average variance per prime below
     M(p₀)²/|𝒫|.
*Proof.* (i) (R − M)² = R² − 2RM + M² ≥ M² − 2RM; multiply by w_j and sum. (ii), (iii) immediate. ∎
*Reading.* "Pointwise via a single-p variance" over windows cannot be easier than a weighted lower bound for R(p)
itself (a positivity statement of B2 strength); CROSSO Lemma 4.1's variance, Σ_p ≤ x·V₈(x), would need
V₈ < M²/π(x) — far beyond HV. With Poisson windows, E Σ_j w_j(R_j − M_j)² = Σ_j w_jM_j < Σ_j w_jM_j² needs M_j > 1, so a
variance criterion must also use windows of mean > 1 (EVIDENCE: F1 windows have var/mean 1.1–4.7, §3.2).

## 3. Computed

### 3.1 Engine and validation (CERTIFIED for the stated ranges)

`scripts/z56_famattack_wcount.c`: exact R(n) for odd n by factoring n + u (segmented sieve) for u ≤ (√(4n + 5) − 1)/4
(u < B forces 4u² + 2u − 1 ≤ n), enumerating divisors m ≡ −1 (4u) with B = (n + u)/m > u, and asserting
4uBC − u − B = n for each hit; output R and a 5×5 grid of unordered solutions by ia = ⌊10 log u/log n⌋ (u = min(u, B)),
ic = ⌊5 log C/log n⌋ (clamped to 0…4). Validation: equals brute force at every odd n ≤ 3001
(`scripts/z56_famattack_brute.py`); `range 5 10⁷` returns R = 0 at exactly 409, 577, 5569, 9601, 23929, 83449, 102001,
329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 (the 14 known zeros); R = 0 at all odd squares tested.
`scripts/z56_famattack_mgen.c`: exact M_gen(n) and R*(n) by pair enumeration (square-class test mod q = 4uB, weight
s(q)/φ(q)); checks: M_gen(m²) = 0 (9801, 25, 1002001), R*(p) = R(p) at p = 1000009 (20).
Commands: `gcc -O2 -o wcount scripts/z56_famattack_wcount.c -lm`; `wcount range 100000000 104000000`,
`wcount range 1000000000 1002000000`, `wcount range 1199000000 1200000000`; outputs `data/z56/famattack/wcount_*.txt.gz`.

### 3.2 F1: cross-window association (EVIDENCE; pre-registered in checkpoint 1)

Data: all primes p ≡ 1 (4) in [10⁸, 1.04·10⁸] (N = 108 397), [10⁹, 1.002·10⁹] (N = 48 139); hold-out [1.199·10⁹,
1.2·10⁹] (N = 23 928). No zero of R in any. Scripts `z56_famattack_assoc.py`, `_ext.py`, `_lcontrol.py`, `_split.py`,
`_lead01.py`; outputs `data/z56/famattack/{assoc_F1*,ext,lcontrol,split,lead01}.txt`.

F1's u-windows are by u = min(u, B) ∈ [p^{k/10}, p^{(k+1)/10}), k = 0…4: their "own" integers p + min(u, B) are
disjoint across windows, but each solution also involves p + max(u, B) and 4Cp + 1 (Lemma L(b)); the C-windows are by
⌊5 log C/log p⌋ and have disjoint integers 4Cp + 1.

Window means (10⁹): u-windows 15.3, 9.0, 6.1, 3.5, 0.87 (var/mean 4.7, 1.2, 1.1, 1.4, 1.7); C-windows 14.1, 9.1, 6.5,
3.9, 1.2 (var/mean 2.3, 1.5, 1.8, 1.3, 0.50). Total unordered mean 34.7 (var/mean 3.1).

| pair (10⁹) | raw | within p mod 840 | + L(1,χ_p), L(1,χ_{−4p}) and residues ≤ 31 |
|---|---|---|---|
| u (0,1) | −0.063 | −0.064 (z −14) | −0.065 |
| u (1,2) / (2,3) / (3,4) | +0.10 / +0.26 / +0.45 | +0.08 / +0.24 / +0.42 | +0.06 / +0.21 / +0.40 |
| C (1,2) / (1,3) / (2,3) | +0.50 / +0.37 / +0.38 | +0.48 / +0.34 / +0.35 | +0.45 / +0.27 / +0.27 |
| C (3,4) | +0.10 | −0.05 (z −11) | −0.06 |

(s.e. ≈ 1/√N = 0.0046; 10⁸ and the hold-out agree in sign and size: `assoc_F1.txt`, `assoc_F1_holdout_1p2e9.txt`.)
Zero events: P(W₃ = W₄ = 0)/(P(W₃ = 0)P(W₄ = 0)) = 1.25 (10⁸), 1.31 (10⁹), 1.32 (hold-out); Mantel–Haenszel odds ratio
within p mod 840: 1.87, 1.82, 1.89. C-windows (pairs with both zero rates in (1 %, 99 %)): ratios 1.24–2.12; their MH
odds ratios are degenerate (0.90, 0, undefined) because C-window 4 is nearly constant within a class mod 840. Residual off-diagonal covariance share after the L-value
controls: u-windows +2.6 % / +5.9 %, C-windows +26.5 % / +31.0 % (10⁸ / 10⁹). The covariates explain R² ≈ 0.33–0.37 of the
total (corr(total, log L(1, χ_{−4p})) = +0.36, corr(total, log L(1, χ_p)) = −0.24; the χ_p sign is the one BM_LVALUE's
T(p) ∝ L(1, χ_p)² predicts).

**Decision (per the pre-registered rule).** Two pairs crossed −4 s.e. within p mod 840.
*C-windows (3,4)* (−0.15 at 10⁸, −0.05 at 10⁹, −0.06 hold-out): both windows have C ≥ p^{0.6}, i.e. 4uB ≤ p^{0.4}·(1 + o(1)),
so each count is a function of p modulo the moduli 4uB ≤ p^{0.4}, i.e. congruence data. Their correlation over primes is a
property of the distribution of residues (CRT competition between cheap pairs; RESIDUE_HARDNESS), which by B1 carries no
pointwise link. Not pursued further.
*u-windows (0,1)* was pushed as a lead:
* it is congruence-sensitive: with one-hot residues of p mod 8, 3, …, 31 it is −0.049; refining to residues mod 16, 9,
  25, 49, 11, …, 31 −0.038; with 32, 27, 25, 49, 121, 169 and all primes 17…97 (1330 columns) −0.024 (z −5.2; 10⁸: −0.027);
* it is not medium-prime competition: S₀, S₁ = numbers of (u, ℓ) incidences with ℓ ∈ (64, 10⁴] in windows 0, 1 have
  corr(S₀, S₁) = −0.098 (privacy is visible), but the partial correlation of W₀, W₁ given S₀, S₁ and their log-masses is
  −0.062 (unchanged);
* it couples window 0 (u ≤ p^{0.1}, the HC lines, dominated by divisor-richness of p + u: within window 0 the
  C ≥ p^{0.6} and C < p^{0.6} parts correlate +0.50/+0.57) with the C < p^{0.6} part of window 1 only (−0.06…−0.07);
  window 0's correlations with windows 2–4 are within ±0.05 under every control and |r| ≤ 0.006 under the 1330-column
  residue control.
Reading (Assessment): a short-range congruence/positional competition between the small-u lines and the next window
(primes ℓ ≤ p^{0.2} placed in p + u for u ≤ p^{0.1} versus p^{0.1} < u ≤ p^{0.2}), of size −0.02…−0.08, against positive
associations up to +0.45 elsewhere. It is not a compensation mechanism for the total (the total's residual variance
exceeds the sum of window variances). Verdict: **the "disjoint windows compensate" hypothesis is killed at this
resolution**; the data show reinforcement.

### 3.3 Why C-windows (disjoint integers 4Cp + 1) are positively linked

By Lemma L(b) each hit is a divisor event of n + u, n + B and 4Cn + 1 at once. A divisor-rich n + u with small u (an HC
line) produces hits at every scale of C (its divisors m = 4uC − 1 of all sizes), so C-windows built on disjoint
integers 4Cp + 1 still share the integers n + u. Within window 0 the two C-halves correlate +0.50…+0.57. No coordinate
system makes all three integers of a hit window-disjoint (they are tied by the three factorisations of Lemma L(b)).

### 3.4 Near-square primes (EVIDENCE; FRONTIER §4 item 15)

965 primes p = m² + k, k ∈ {1, 5, 9, 13, 21, 45, 105}, p ∈ [10⁹, 1.2·10⁹] (`z56_famattack_nearsq_gen.py`,
`_nearsq.py`, `data/z56/famattack/nearsq_profile.txt`); expected counts from generic primes at 10⁹ in the same class mod
840. Ratio observed/expected: total 0.86 (k = 1: 0.80; k = 5: 0.79; k = 105: 0.91); per u-window 0.81–0.90, per C-window
0.81–0.95 (all k pooled); no zero. The deficit is spread over all windows: the near-square deformation of T1 is a
global (all-window) driver, so it is not diversified away by a union.

### 3.5 Composite non-square zeros and the genus main term (CERTIFIED counts; EVIDENCE readings)

All n ≡ 1 (4), 5 ≤ n ≤ 7 999 801 (the run hit its 1700 s timeout there; range recorded as reached): R(n) = 0 at 1 711 n:
13 primes (the known ones ≤ 8·10⁶), 1 413 odd squares (all of them), 285 non-square composites
(`data/z56/famattack/zeros_n1mod4_le8e6.txt`, `compzeros_summary.txt`). Per decade (by ⌊log₁₀ n⌋ = 1…6): 1, 8, 24, 60,
95, 97 (the last decade only to 8·10⁶). The composite zeros were known to exist (BRAINSTORM `z52b_fingerprint.md`
#88–#89); new here are the counts to 8·10⁶ and their genus masses: exact M_gen(n) at all 299 non-square zeros n ≡ 1 (4) below 8.9·10⁶ (285 composites, 14 primes incl. 8 813 281;
`mgen_nonsquare_zeros.txt`; R*(n) = 0 at all): composite median 8.0, maximum 24.25 (n = 810 001 = 241·3361), 22.9
(2 956 321 = 211·14011), 21.7 (752 257 = 11²·6217); the 14 prime zeros have M_gen from 4.0 (409) to 29.1 (8 813 281).
Matched controls (`mgen_zero_vs_controls.txt`, 24 triples near 4–8·10⁶): composite zeros mean M_gen/log²n 0.047, the
next composite ≡ same mod 420 0.062, the next prime ≡ 1 (4) 0.156.
*Reading.* A union-over-windows argument whose only square-sensitive input is "n is not a square" (e.g. Thm-U-type genus
lower bounds, which GENUSLVAL §2.8 expects to extend to non-squares with local factors) must fail at these n: there
X(n) = −M_gen(n) with M_gen up to 24. Primality has to enter the transfer step itself.

### 3.6 Model scale (Assessment)

Expected tail count T(x) = ∫_x^∞ e^{−c log²t}dt/(2 log t) of zero primes under hits ~ Poisson(c log²p)
(`z56_famattack_model.py`, `model_crossover.txt`): c = 0.0808 (full count, measured mean/log²p at 10⁸–10⁹): 11.8 zeros
in total (observed 14), T = 1 at 10^{3.8} (the observed tail to 8.8·10⁶ is fatter: mean variation across p);
c = 0.0073 (tiled genus family, c_tile/2): 1.1·10¹⁴ zeros, T = 1 at 10^{57}; c = 0.00924: 10^{44.6}; c = 1/(3π⁴):
5.6·10³⁰ zeros, T = 1 at 10^{124.1} (reproduces CROSSF). A provable family is "checkable" only with a mean near the full
count's; Prop T's 9.6 % is far from that.

## 4. Where it stops — the step that would make it work

1. *Main terms.* Burgess tiles give ≤ 9.6 % of the mean (Prop T); with Thm X's class control, 2.5 % (Prop T′). The
   uncovered part needs w-windows shorter than (4up)^{1/4} or u > p^{3/5}; Burgess gives nothing there.
2. *Residual.* By Thm J, FA ⇐ (CU_𝒯). The union of tiles helps only through cross-tile dependence of the exact layers.
3. *Dependence.* Lemma L lists all exact links: switch (positive), privacy (negative, sizes only), congruences (B1),
   parity (BM coset only). The data (F1) show net positive association, which makes the joint empty event *more* likely
   than independence.
4. *Missing ingredient.* A mechanism producing **negative association of the exact class layers across windows at one
   p** — "if the divisors of p + u miss −1 mod 4u for all u ∈ W_j, then some divisor of p + u′, u′ ∈ W_k, hits −1 mod 4u′".
   Assessment: by CLASS_FORCING Thm 2.1 and the privacy lemma, such a mechanism cannot come from reciprocity, small primes
   or Chebotarev data; it would have to see the classes of large private primes of *different* integers jointly. No tool
   doing that is known. Absent it, (CU_𝒯) is a pointwise lower-tail statement for a sum of positively associated
   Poisson-like counts with mean ≍ log²p — B2 in tied form.
5. *Escape hatches left open by the scoped statements.* (i) windows defined by non-size conditions (e.g. by the
   factorisation type of p + u), for which Lemma L(a)'s disjointness changes; (ii) signed combinations across windows
   (not sums of counts), e.g. theta-quotient identities (FRONTIER §2.3) mixing levels; (iii) a Type II family with a
   free variable not attached to p (FAMDESIGN (iii)), where cross-window dependence could differ.

## 5. Screens (FRONTIER §4) for the best idea (Thm J + union over tiles)

1. **T1 (odd squares):** passes for the main term (Prop T inherits GENUSLVAL §2.8: every tile's genus sum vanishes at m²);
   the residual (CU_𝒯) is false at squares (R = 0), as it must be. Composite non-squares (§3.5) show the transfer must use
   primality beyond non-squareness — not satisfied by any argument here.
2. **8/131:** the main-term side is 4-specific through the (★) parametrisation; the residual statement is not proved, so
   no false numerator-8 claim arises; no step here is numerator-uniform in the sense of (J)41. Not tested further.
3. **Tied modulus:** **fails** — the residual is exactly the tied event (divisor of p + u in −1 mod 4u); the union adds
   no untied variable (Lemma L).
4. **Fixed p:** passes — Props T, T′, J and Lemma L hold at each prime; F1 and the variance criterion (Prop V) are about
   one p (the cross-prime statistics are diagnostics only). (B6: CROSSO's large sieve gives nothing pointwise, Prop V(iii).)
Test primes (item 14): all 14 (★)-zero primes have R = 0 in every window (engine), M_gen 4.0–29.1 (§3.5).

## 6. Proposed FRONTIER text (do not edit FRONTIER here)

*§7.3 / §7.4 addendum (z56 FAMATTACK).*
* **Tiling (PROVED, unconditional, effective; `Z56_FAMATTACK.md` Prop T).** Thm U over finitely many thin u-strips:
  M_gen(p) ≥ (64/(45π⁴) − ε)log²p ≈ 0.0146 log²p (2.13 × Thm U); Thm X tiles give M^cls ≥ (28/(75π⁴) − ε)log²p ≈ 0.0038
  log²p (1.97 × c_X) with T_u = O(p^{−δ}log p) (Prop T′). Share of the full mean: 9.6 % resp. 2.5 %.
* **Joint reduction (PROVED; Thm J).** All of Thm U, Thm X and the disjoint union reduce (★) to the tiled exact-layer
  bound (CU_𝒯): Σ_t (T_w + T_uw)_t ≥ −(1 − ε)Σ_t M^cls_t.
* **Union over windows (Lemma L, PROVED; Prop V, PROVED; F1, EVIDENCE).** Exact cross-window links are the switch
  (positive), privacy (sizes only), congruences (B1) and χ_p-parity (BM coset). Pointwise variance criteria are
  first-moment lower bounds in disguise. At 10⁸–1.2·10⁹ (≈ 180 000 primes) window counts are positively associated
  (C-windows up to +0.45 after L-value controls; joint-empty odds ratio ≈ 1.9); the one negative pair (−0.02…−0.06) is a
  congruence-scale effect. Near-squares depress every window. Assessment: a union argument needs a negative-association
  mechanism for class layers of different integers at one p; none is known.
* **Calibration (CERTIFIED).** 285 non-square composite n ≡ 1 (4) ≤ 8·10⁶ have R(n) = 0, with M_gen up to 24.3
  (810 001 = 241·3361): any transfer step must use primality beyond non-squareness.

*§6 dead-end line.* (z56) Positivity from the union over windows, or from a pointwise variance across windows →
`Z56_FAMATTACK.md` Lemma L, Prop V, F1: links are positive or congruence/size-only; variance = first moment.
Non-size windows and signed cross-level identities not covered.

## 7. Bottom line

Combining Thm U, Thm X, the switch, the spin dictionary and dual-large-sieve variance does not prove (★) at a single prime.
What it buys: the provable genus main term roughly doubles (Prop T: 0.0146 log²p; Prop T′: 0.0038 log²p of exact-class
density), and a clean statement of what the joint attack reduces to (CU_𝒯). The brief's specific hope — that windows
built on disjoint integers p + u cannot all fail together — has no exact mechanism behind it (Lemma L), cannot be routed
through a pointwise variance (Prop V), and is contradicted in the data: windows reinforce one another (F1), global drivers
such as near-squareness depress them all at once, and composite non-squares with genus mass up to 24 are empty. The step
that would make a union argument work is a negative-association mechanism for the classes of large private prime factors
of different integers at one prime; nothing in the campaign or the literature checked here provides it. ES remains OPEN.

## 8. Review

(pending: hostile reviewer subagent; findings and fixes will be recorded here.)
