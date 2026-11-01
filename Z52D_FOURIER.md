# Z52D_FOURIER — cluster C9 (rank_O) = A02 (rank_A): bounded-exponent Fourier/character obstruction of the window event

**ES is OPEN; nothing here proves or disproves it.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) /
EVIDENCE / CONJECTURE / Assessment. These results are internal and have only been reviewed internally (§8).
Members: Z3003 Z2940 Z2941 Z2512 Z3002 Z2964 Z1787 (rank_O C9); Z0648 Z0674 Z2926 (extras in rank_A A02).
Scripts `scripts/z52d_fourier_*.py`; data `data/z52d/fourier/` (≈ 16 MB).
Prior work this builds on: BRAINSTORM/z45_siegel_dichotomy §5.2 (it refuted a single-odd-character *phase-separation*
inverse lemma at 31121/43); rank_O's `z52d_rank_O_charobs.py` (it split subgroup kills into χ_{−e} / other real / non-real);
CAP_BOUNDED (J)83 Lemma 1.1, Cor 1.2 (Jacobi transfer, window parity law).

## 0. Bottom line

The cluster hoped for three things:
(a) every obstructed window is explained by *one bounded-order character* carrying a fixed share η of the Fourier mass;
(b) at hard primes *one character is shared across windows*;
(c) that character is "exceptional" and repels failure elsewhere, as in Linnik / Deuring–Heilbronn.

* **(a) Refuted in the form an obstruction witness needs.** L(B, η) is the *signed* lemma (the character must push towards
  failure, c(χ) ≥ η > 0).
  * Thm B (PROVED): at a forced prime window q with (q−1)/2 free of primes ≤ B, no χ ≠ 1 of order ≤ B has c(χ) > 0.
  * CERTIFIED: 2,110 such obstructed windows with full generated subgroup, for every B ≤ 952. Under Dickson's conjecture
    this extends to every B (Prop B′). Two certified windows have boxes covering 94 % and 91 % of the group, so box size
    is not the reason.
  * Thm C (PROVED): the same in abstract cyclic groups, where the box image can be the whole group minus the target. There
    the obstruction sits on characters of order ≍ |G|.
  * Census (EVIDENCE, 56,590 forced obstructed windows with H = G): L(12, 0.1) fails at ≈ 40 % (≈ 48 % for odd χ). With
    box ≥ |G| it fails at 58–67 %.
  * The *unsigned* variant (|c| ≥ η, closer to Z3003's pigeonhole witness) mostly holds in the data: 93–100 % for B = 2,
    η = 0.1. It holds only through the BM character χ_{−e}, which at forced windows pushes towards *success* (Prop 1). It is
    refuted for η > 1/63 (B ≤ 292, CERTIFIED), and for every B and η conditionally on Dickson (Prop B″).
  * The any-order variant is not refuted; §3.6 says why it seems uninformative (Assessment).
* **(c) The real layer is (I)7 plus genus twists.**
  * By the Jacobi transfer ((J)83 Lemma 1.1), the window's BM character χ_{−e} = (·/e) equals χ_p = (·/p) on every prime
    factor of N_e.
  * Prop 1 (PROVED): its normalised obstruction mass is exactly
    **c(χ_{−e}) = (e/p)·∏_{s|N_e, (s/p)=−1}(2b_s+1)⁻¹**. It obstructs only at unforced windows.
  * Every other odd real character is χ_{−e}·ψ with ψ an even real (genus) character of the window. That is not (I)7; it
    is the same kind of object as FRONTIER §7.3's "other genus characters" (Assessment).
  * Prop 2 (PROVED): every subgroup obstruction has a 2-power-order witness.
* **(b) The only shared character found is χ_p (the BM layer).**
  * This "only" is Assessment: we tested fixed primitive characters of conductor ≤ 200 and the χ_{−e} family.
  * Hard primes do have more χ_p kills at unforced windows. Per 500 windows: +20.0 raw, +18.7 adjusted (t = 5.5);
    restricted to e ≥ 200, +16.4 raw / +15.2 adjusted (t = 4.7). This locates rank_O's real-layer excess precisely. It is
    largely what the hard set's selection (small BM main term) implies.
  * At forced windows χ_p is silent, and no hard-prime class is significantly *larger*. Poverty-type: +2.1 raw / +1.3
    adjusted (t = 0.8). Genus-twist kills: −2.3 raw / −2.6 adjusted (t = −2.3). Non-real kills: −0.9 raw / −1.2 adjusted
    (t = −2.0). Hard primes simply have fewer forced windows: −4.7 raw / −5.3 adjusted (t = −3.6).
  * No fixed Dirichlet character covers more than 16 % of any prime's forced obstructed windows. Hard primes are not more
    coherent than controls.
* **(c′) No repulsion.** The forced-window success rate does not rise with χ_p's exceptionality. On 400 random primes the
  partial correlation is −0.04 [−0.14, +0.06]. The outcome-selected hard/control set gives −0.18 [−0.34, −0.02].

**Verdict: narrowed to collapse.**
* The signed bounded-order inverse sub-route is **dead** (theorem + certificate; Dickson for all B). The unsigned version
  survives only as a restatement of Prop 1.
* The sub-route "one exceptional character / Deuring–Heilbronn" is **dead as stated, at EVIDENCE level**. The only
  window-uniform character found is χ_p (BM), and no repulsion is seen.
* What remains: §7.3-type genus twists at composite windows, §7.4, and the poverty-type B2 core. That core is ≈ 84 % of
  forced obstructions at hard and control primes alike (82–84 %).
* Recommendation (Assessment): fold C9 into §7.3; it is not a separate avenue.

## 1. Statements attacked

**Setting** (FORCED_WINDOW; CAP_BOUNDED §1).
* p ≡ 1 (mod 4) prime; window e ≡ 3 (mod 4), 3 ≤ e < 3p, p ∤ e; N = N_e = (p+e)/4; b_s = v_s(N); G = (ℤ/e)^*.
* gcd(N, e) = 1, since a common prime would divide 4N − e = p.
* The window *succeeds* iff −1 ∈ {a·b⁻¹ mod e : a, b coprime, ab | N}, i.e. iff some δ ∈ ∏_s [−b_s, b_s] has
  ∏ s^{δ_s} ≡ −1. This is an honest Type II solution with x = N (cap 0).
* *Forced* means (e/p) = −1 (Jacobi). H := ⟨prime factors of N⟩ ≤ G.
* An obstructed window is *subgroup-type* if −1 ∉ H. It is *poverty-type* (rank_O's name) if −1 ∈ H but the box misses −1.
  "Poverty" here is this definition, not a statement about box size.
* *Hard* primes are the 14 (★)-zeros ≤ 10¹⁰ together with the 16 primes ≤ 10⁷ with the largest m_II (least window
  hitting −1; z45 census).

**Statements.**
* **(a) Inverse lemma.**
  * L(B, η) (rank_A A02 lane; signed): every obstructed window with H = G has χ ≠ 1, ord χ ≤ B, with c(χ) ≥ η (normalised
    mass, §2).
  * Variants: L_odd (χ also odd); L_abs (|c(χ)| ≥ η); any-order (B = ∞).
* **(b) Shared character** (Z2940 (c), Z3003 "next", Z1787 "next"): at hard primes the obstructed windows are explained by
  ONE character, more than at controls.
* **(c) Real layer = (I)7?**
* **(c′) Deuring–Heilbronn analogue** (Z2941, Z2940 (c)): if χ_p is exceptional, the windows χ_p cannot touch get easier.

## 2. The exact identity and its bookkeeping (PROVED, elementary)

**Definitions.** For χ ∈ Ĝ:
* D_b(z) = Σ_{|j|≤b} z^j. It is real on |z| = 1: D_b(e(θ)) = 1 + 2Σ_{j≤b} cos 2πjθ.
* F(χ) = ∏_{s | N} D_{b_s}(χ(s)), and M = F(1) = ∏(2b_s+1) (the box size, counted with multiplicity).
* **c(χ) := −χ(−1)F(χ)/M.**

The map (a, b) ↦ δ with δ_s = v_s(a) − v_s(b) is a bijection between coprime pairs with ab | N and the box. Since
F(χ) = Σ_δ χ(∏ s^{δ_s}), orthogonality gives

  r(−1) := #{δ : ∏ s^{δ_s} ≡ −1} = φ(e)⁻¹ Σ_χ χ(−1) F(χ),  r(1) = φ(e)⁻¹ Σ_χ F(χ).  (2.1)

* For squarefree N this is Z3003's formula. The signed kernel that rank_A asked for at prime powers is the D_b above.
* The scan checks (2.1) against a direct count at every window (|difference| < 10⁻⁶·M; it is an assertion in
  `z52d_fourier_scan.py`).

**Corollary 2.2 (even/odd split).**
Σ_{χ odd} c(χ) = φ(e)(r(1) − r(−1))/(2M), and Σ_{χ even, ≠1} c(χ) = 1 − φ(e)(r(1)+r(−1))/(2M).
*Proof.* From (2.1), Σ_odd F = (φ/2)(r(1) − r(−1)) and Σ_even F = (φ/2)(r(1) + r(−1)). Divide by M, using the signs in
the definition of c. ∎

* At an obstructed window Σ_{χ≠1} c = 1. The split between even and odd characters is fixed by φ r(1)/M. The even share is
  negative once φ r(1) > 2M.
* At (31121, 43) the two largest masses sit on **even** characters of order 7 (c = 0.200 each). The odd characters carry
  0.467 in total; the largest odd one is 0.095, at order 42.
* So a "share of the Fourier mass" is a fragile notion; we test L, L_odd and L_abs.

## 3. Proved statements

### 3.1 The transfer (known: CAP_BOUNDED (J)83 Lemma 1.1; reproduced)
**Lemma T.** For every prime s | N: (s/e) = (s/p). Hence (N/e) = (N/p) = (e/p).
*Proof.*
* Odd s. First, s ∤ e (§1). Jacobi reciprocity with e ≡ 3 (4) gives (s/e) = (−1/s)(e/s) = (−e/s). Next, s | p + e gives
  −e ≡ p (mod s), so (−e/s) = (p/s). Finally (p/s) = (s/p), since p ≡ 1 (4).
* s = 2. Here 8 | p + e, so e ≡ −p (mod 8). The symbol (2/·) is invariant under x ↦ −x mod 8.
* The last claim: 4N ≡ e (mod p). ∎

**Cor T′ (window parity law = window form of (I)7; (J)83 Cor 1.2).** Every success (a, b) has (ab/p) = −1.
*Proof.* (a/e) = (−b/e) = −(b/e), so (ab/e) = −1. Lemma T turns this into (ab/p) = −1. ∎

### 3.2 Prop 1 — the exact BM share of the Fourier mass (PROVED; elementary; new as a formula)
Let χ_{−e} := (·/e) (Jacobi). It is odd, since e ≡ 3 (4). Then

  **c(χ_{−e}) = (e/p) · ∏_{s | N, (s/p) = −1} (2b_s + 1)⁻¹.**

*Proof.*
* By Lemma T, χ_{−e}(s) = (s/p).
* D_b(1) = 2b+1 and D_b(−1) = (−1)^b. Hence F(χ_{−e}) = ∏_{(s/p)=1}(2b_s+1) · ∏_{(s/p)=−1}(−1)^{b_s}.
* The sign factor is ∏_{(s/p)=−1}(−1)^{b_s} = (N/p) = (e/p), by Lemma T.
* Since χ_{−e}(−1) = −1, c = F/M. ∎

*Consequences.*
* χ_{−e} *kills* the window (c = 1) iff every prime factor of N is a QR mod p. That forces (e/p) = 1.
* **The BM character never obstructs a forced window.** At forced windows c(χ_{−e}) = −∏(2b_s+1)⁻¹ < 0.
* Across windows, χ_{−e} is the single character χ_p evaluated on the prime factors of the consecutive integers
  N = (p+3)/4, (p+7)/4, …. It is the only window-uniform character family we know (Assessment, §4.2). The reason
  individual factors see nothing else: by CLASS_FORCING Prop 5.1(c), the only individual-factor link to p is this quadratic
  one, and by Thm 5.2 no Galois datum of p forbids a class for an individual factor.
* CAP_BOUNDED Thm 1.3 (CONDITIONAL on Dickson) is the extreme case: all windows ≤ M are unforced, and all are χ_p-killed.

*Checks.*
* CERTIFIED: on all 158,724 obstructed windows of both scans, χ_{−e} kills a forced window 0 times, and sign c(χ_{−e}) ≠ (e/p) occurs 0 times.
* The exact rational value of Prop 1 was recomputed with sympy at 8 windows (`certify_thmB.txt`), and by the reviewer at
  400 random windows (§8).

### 3.3 Real layer; 2-primary subgroup obstructions (PROVED)
**Prop 2.**
* (i) Every *odd* real character of G is χ_{−e}·ψ with ψ even real. On prime factors of N it equals (·/p)·ψ.
* (ii) For any character ψ of G, ψ(N) = ψ(p/4) depends only on p mod e (CLASS_FORCING Thm 2.1(a)).
* (iii) Suppose an odd χ is trivial on H, and let u be the odd part of ord χ. Then χ^u is odd, trivial on H, and has
  2-power order. So the least order of a killing character is a power of 2.

*Proof.* (i) χ·χ_{−e} is real and even; apply Lemma T. (ii) 4N ≡ p (mod e). (iii) χ^u(−1) = (−1)^u = −1. ∎

*Reading.*
* The odd real layer is {BM} ∪ {BM twisted by an even genus character ψ ≠ 1 of e}. The twists exist only at composite e.
* ψ = 1 is (I)7 (§3.2). The twists are not (I)7. They are the window analogue of §7.3's "other genus characters" — the same
  kind of object, not the same sum, since §7.3 works in level coordinates (Assessment).
* Even real characters also carry signed mass (§2), but by Cor 2.2 they cannot separate −1 from 1.
* EVIDENCE: kills that use no real character have least orders 4, 8, 16, 32 only. There are 855 such windows in the
  hard/control scan and 912 in the random scan. Being a 2-power is Prop 2(iii); the counts and the maximum 32 are data.

**Prop 3** (known; CAP_POINTWISE (J)64). At a forced *prime* window q, −1 ∈ H.
*Proof.* (N/q) = −1 gives a factor s with (s/q) = −1. In the cyclic group of order q − 1 = 2·odd, a non-square has even
order. So s^{ord(s)/2} = −1. ∎
* Hence subgroup-type obstructions at forced windows occur only at composite e. They come from genus twists or from
  2-power characters. The scans have 0 exceptions.

### 3.4 Thm B and Props B′, B″ — bounded-order inverse lemmas fail at arithmetic windows
**Theorem B (PROVED).**
* *Hypotheses:* q is a forced prime window at p, and every prime factor of (q−1)/2 exceeds B.
* *Claim:* every χ ≠ 1 of (ℤ/q)^* with ord χ ≤ B equals χ_{−q}, and c(χ_{−q}) = −∏_{(s/p)=−1}(2b_s+1)⁻¹ < 0.
* *Consequence:* if the window is obstructed, L(B, η) and L_odd(B, η) fail there for every η > 0, and
  L_abs(B, η) fails for every η > ∏_{(s/p)=−1}(2b_s+1)⁻¹.

*Proof.* Since q ≡ 3 (4), q − 1 = 2m with m odd. A divisor d ≤ B of 2m has no odd prime factor ≤ B, so d ∈ {1, 2}. The
order-2 character is χ_{−q}; apply Prop 1. ∎

**CERTIFIED** (`z52d_fourier_scan.py` + `z52d_fourier_thmB_count.py`; spot-checked independently with sympy and no Fourier
code in `z52d_fourier_certify.py`).
* *Count.* In the hard/control scan, 2,110 windows are forced prime windows with (q−1)/2 prime, obstructed, and H = G. They
  involve 35 distinct q, up to q = 1907 (p = 102001, N = 3·7·1237). This refutes signed L(B, η) for every B ≤ 952.
  The random scan has 3,184 more (q ≤ 983).
* *Box size is not the reason.*
  * (p, q) = (5211721, 479): N = 2·3·5²·7·17·73, M = 1215 = 2.54|G|. The box image is 449 of the 478 residues; −1 is
    missed; H = G. Refutes B ≤ 238.
  * (1714441, 503): N = 2⁶·3·7·11·29, M = 1053 = 2.10|G|, image 455 of 502. Refutes B ≤ 250.
  * In total, 57 (hard/control) and 190 (random) Thm B windows have M ≥ |G|.
* *Unsigned.*
  * At 2,066 of the 2,110 windows, |c(χ_{−q})| = 1/3: one p-non-residue factor, so L_abs(2, η ≤ 1/3) *holds* there.
  * The smallest value is 1/63, at (1005913, 587): N = 3·5³·11·61. The p-non-residue factors are 5³, 11 and 61, so
    |c| = 1/(7·3·3); the Prop 1 value −1/63 was checked exactly. This refutes L_abs(B, η) for η > 1/63 and B ≤ 292.

**Prop B′ (CONDITIONAL on Dickson's conjecture for two linear forms).** For every B there are infinitely many (p, q) as in
Thm B with N prime and ⟨N⟩ = G.
*Proof.*
1. Dirichlet gives a prime q > 3 with q ≡ 3 (mod 8) and q ≡ 2 (mod ℓ) for each odd prime ℓ ≤ B. Then ℓ ∤ q − 1 and
   (q−1)/2 is odd, so every prime factor of (q−1)/2 exceeds B.
2. Let g be a primitive root mod q and N₀ an odd integer ≡ g (mod q). Put p₀ = 4N₀ − q ≡ 1 (mod 8),
   f₁(t) = 8qt + p₀ and f₂(t) = 2qt + N₀. Then f₁ = 4f₂ − q.
3. The pair is admissible. At ℓ = 2 both forms are odd. At ℓ = q they are ≡ 4g and g, both nonzero. At any other ℓ ≥ 3
   each form has one root, so at most 2 < ℓ classes are excluded.
4. Dickson gives infinitely many t with p = f₁(t) and N = f₂(t) both prime. Then p ≡ 1 (mod 8), and
   (q/p) = (p/q) = (4g/q) = −1, so the window is forced. Also N = (p+q)/4 ≡ g, so H = G.
5. The box is {1, N, N⁻¹}. It misses −1 because ord g = q − 1 > 2. ∎

**Prop B″ (CONDITIONAL on Dickson for two linear forms).** For every B and every odd k there are forced windows as in
Thm B with |c(χ_{−q})| = 3^{−k}. Hence L_abs(B, η) fails for every B and every η > 0.
*Proof.*
1. Take q as in Prop B′ with also q > 2k + 2. Let g be a primitive root.
2. By Dirichlet, take distinct odd primes r₂, …, r_k ≡ g (mod q), and put C = r₂⋯r_k.
3. Take n₀ odd with n₀ ≡ g (mod q), and set f₂(t) = 2qt + n₀ and f₁(t) = 4C f₂(t) − q.
4. Admissibility, prime by prime:
   * ℓ = 2: both forms are odd.
   * ℓ = q: f₂ ≡ g and f₁ ≡ 4Cg, both nonzero.
   * ℓ = r_i: f₁ ≡ −q ≢ 0, and f₂ has one root.
   * every other ℓ ≥ 3: at most 2 roots.
5. Dickson gives infinitely many t with p = f₁(t) and N₁ = f₂(t) prime. Then p ≡ 1 (mod 8) and N = C·N₁, which has k
   distinct prime factors, all ≡ g (mod q).
6. The window is forced: (q/p) = (p/q) = (4N/q) = (g/q)^k = −1, since k is odd.
7. The box image is {g^j : |j| ≤ k}. It misses −1 = g^{(q−1)/2}, since k < (q−1)/2. Also H = G.
8. By Lemma T every factor s has (s/p) = (g/q) = −1, so Prop 1 gives |c(χ_{−q})| = 3^{−k}. ∎

### 3.5 Thm C — abstract groups, box image up to G ∖ {τ} (PROVED)
**Theorem C.** Let G = ℤ/m with m even and target τ = m/2. Take k < m/2 generators, all equal to 1, each with budget 1.
* The multiset size is 3^k. The image is {−k, …, k}: 2k + 1 residues, which is m − 1 (everything except τ) when
  k = m/2 − 1.
* The box misses τ, and H = G.
* Every χ_r of order d ∈ [2, B] has |c(χ_r)| ≤ (ρ_B/3)^k, where ρ_B = max(1, 1 + 2cos(2π/B)) < 3.
* The odd character χ_1, of order m, has c(χ_1) ≥ 1 − 4π²k/(3m²).

*Proof.* F(χ_r) = (1 + 2cos 2πr/m)^k. A character of order d has angle j/d with gcd(j, d) = 1.
* d = 2: the factor is −1.
* d ≥ 3: 1 + 2cos(2πj/d) ∈ [−1, 1 + 2cos(2π/d)] ⊂ [−1, 1 + 2cos(2π/B)].
* χ_1: χ_1(τ) = −1, and (1 + 2cos x)/3 ≥ 1 − x²/3. Then apply Bernoulli. ∎

So for k > log(1/η)/log(3/ρ_B) and m > 2k, L, L_odd and L_abs all fail. The obstruction sits on characters of order ≍ |G|:
Bohr / low-frequency structure, not bounded order. `thmC_check.txt` checks (m, k) = (40, 19), (100, 49), (400, 60) and
(400, 199); the last has image 399/400.

### 3.6 The any-order version (Assessment; not refuted)
* "Some χ ≠ 1 has c(χ) ≥ 0.2" holds at 98–100 % of obstructed windows with H = G (§4.1).
* The median of max c is between 0.42 and 1.0, depending on box size, and is larger for smaller boxes.
* Proposed reason, for the *magnitude* only: Dirichlet simultaneous approximation on Ĝ gives χ ≠ 1 with every phase
  θ_s(χ) ≲ |G|^{−1/ω}. When (2b_s+1)|G|^{−1/ω} ≪ 1 this gives |F(χ)| ≈ M, independently of the target.
* This does not explain the *sign*. The parity of the pigeonholed χ is not controlled, and at 31121/43 no odd χ even
  clears the half-turn separation threshold (z45 §5.2).
* So the any-order version is open. It is not refuted here, and we do not see how it could carry target information
  beyond B2 itself.

## 4. Computations (EVIDENCE unless marked CERTIFIED)

**Prime sets.**
* Hard set: 30 primes.
* Controls: 116 primes, the nearest 2 below and 2 above each hard p in the same class mod 840, excluding primes with
  m_II ≥ 31 (`z52d_fourier_primes.py`). Matching mod 840 fixes (ℓ/p) for ℓ ≤ 7. For 409 and 577 only 2 controls exist
  (both above, and of larger size).
* Windows: 3 ≤ e ≤ 2000, e ≡ 3 (4), e < 3p, p ∤ e; 72,738 windows in total (`scan_hardctrl_E2000.jsonl.gz`). At p = 409
  and 577 only e < 3p is used, so counts are normalised **per 500 windows**.
* Random set: 400 primes p ≡ 1 (24) in [10⁶, 10⁷] (`z52d_fourier_random.py`, seed 52041), e ≤ 1000; 100,000 windows.

**Window classes per 500 windows** (F = forced, U = unforced):

| | F-ok | F-sub | F-pov | U-ok | U-sub | U-pov |
|---|---|---|---|---|---|---|
| hard (30) | 13.9 | 36.2 | 186.6 | 3.2 | 207.9 | 52.1 |
| control (116) | 17.3 | 39.6 | 184.8 | 5.9 | 187.4 | 64.9 |

Subgroup kills per 500 windows, hard vs control:

| kill class | hard | control |
|---|---|---|
| U by χ_{−e} | 195.7 | 175.4 |
| U by genus twist only | 10.6 | 10.5 |
| F by genus twist | 32.7 | 35.1 |
| non-real only, F + U | 3.5 + 1.6 | 4.5 + 1.5 |

### 4.1 Inverse lemma (a)
Share of obstructed **forced** windows with H = G at which L(B, η) holds (all χ | odd χ):

| set (n) | B=2, η=.1 | B=6, η=.1 | B=12, η=.1 | B=12, η=.2 | B=24, η=.2 |
|---|---|---|---|---|---|
| hard (5,036) | .33 \| .32 | .51 \| .45 | .61 \| .52 | .47 \| .36 | .57 \| .48 |
| control (19,437) | .33 \| .31 | .52 \| .45 | .62 \| .52 | .48 \| .37 | .58 \| .49 |
| random (32,117) | .34 \| .32 | .51 \| .45 | .63 \| .52 | .48 \| .36 | .59 \| .50 |

* **Unsigned, B = 2, η = 0.1:** L_abs holds at .99 (hard), .98 (control) and .93 (random). All of it comes from |c(χ_{−e})|.
* **Large boxes.** Forced windows with H = G and box at least the group size:

  | box condition | set | obstructed / windows | L(12, .1) holds (all \| odd) |
  |---|---|---|---|
  | M ≥ φ(e) | hard + control | 265 / 1,190 | .33 \| .25 |
  | M ≥ φ(e) | random | 1,137 / 4,711 | .42 \| .34 |
  | M ≥ 2φ(e) | hard + control | 23 / 512 | .22 \| .17 |
  | M ≥ 2φ(e) | random | 194 / 2,290 | .37 \| .34 |

* At unforced windows L(2, .1) holds at 97–100 %. That is χ_{−e} again, and Prop 1 fixes its share.
* **Small groups** (`smallgroups.jsonl`; exhaustive enumeration with an integer-checked float Fourier count):
  * Setting: ℤ/m with m ≤ 46 even, k ≤ 4 generators of budget 1, every multiset with full subgroup.
  * m = 46 (q = 47): L(12, .1) holds for .37 / .46 / .44 of obstructed configurations at k = 2 / 3 / 4, and L(12, .2) for
    0. This case is not independent evidence: with (q−1)/2 prime it is Thm B's mechanism (only the real character has
    bounded order), without the forcing constraint.
  * m = 42, k = 4 (42,924 obstructed configurations): .72 and .16.

### 4.2 Cross-window sharing (b) (`z52d_fourier_xwin.py`)
**Method.** For each primitive ψ of conductor f ≤ 200, induced to every window with f | e, count the obstructed windows
where c(ψ) ≥ η.

**Coverage of forced obstructed windows, η = 0.15.**
* The best single ψ covers on average 10.1 % (hard) vs 10.7 % (control); the maxima are 16.0 % vs 14.8 %.
* Hard primes' mean rank is 57.9, against 72.5 expected.
* Measured only on windows where ψ is defined (best ψ with ≥ 8 such windows), the share is 0.79 vs 0.78 — no difference.
* The best ψ is (·/3) at 29 of 30 hard primes and (·/5) at 329617. These are odd real characters at windows 3 | e
  (resp. 5 | e), i.e. genus twists in Prop 2's sense.
* At η = 0.3: 7.5 % vs 8.1 % on average; maxima 11.0 % vs 13.1 %.

**Structural remark (Assessment).** A fixed ψ is defined only at windows f | e, which have relative density ≤ 1/3. The only
family defined at every window that we know is χ_{−e}, and it exists because of the transfer to χ_p (§3.2).

**Where the hard-prime excess sits** (`z52d_fourier_excess.py`).
* Method: OLS with covariates qr (share of ℓ ∈ [11, 97] with (ℓ/p) = 1) and mean ω(N_e); per 500 windows; t-statistics
  are classical OLS and ignore the matched design.
* Each cell gives raw / adjusted difference and the adjusted t.

| class | all windows | e ≥ 200 |
|---|---|---|
| U-sub by χ_{−e} | +20.0 / +18.7 (t = 5.5) | +16.4 / +15.2 (t = 4.7) |
| U-pov | −12.9 / −11.3 (t = −4.4) | −13.7 / −12.1 (t = −4.4) |
| F-all (number of forced windows) | −4.7 / −5.3 (t = −3.6) | −1.9 / −2.4 (t = −1.5) |
| F-pov | +2.1 / +1.3 (t = 0.8) | +2.3 / +1.8 (t = 1.0) |
| F-sub, genus twist | −2.3 / −2.6 (t = −2.3) | −1.8 / −2.0 (t = −1.7) |
| F-sub, non-real | −0.9 / −1.2 (t = −2.0) | −1.0 / −1.2 (t = −1.9) |
| F-ok | −3.5 / −2.8 (t = −3.3) | −1.4 / −0.9 (t = −1.2) |

*Reading.*
* The shared-character excess is entirely χ_p at unforced windows: the window-level face of a small BM main term. That is
  close to tautological given how the hard set was chosen, since those primes have few successes.
* Forced windows show no hard-prime excess in any obstruction class.
* The F-ok deficit is mostly selection: m_II-hard primes fail at every e < m_II ≤ 107, and the deficit shrinks for
  e ≥ 200.

### 4.3 Repulsion (c′) (`z52d_fourier_repulsion.py`)
**Definitions.** x = the share of unforced windows killed by χ_p (χ_p's "exceptionality" on the window integers);
y = the forced-window success rate.

**Results.**
* Random 400: corr(x, y) = +0.040 [−0.059, +0.137]. Partial correlation given forced mean log M and qr: −0.039
  [−0.136, +0.060].
* Hard + control (146 primes; outcome-selected): corr = −0.392. Partial: −0.182 [−0.335, −0.018]. If anything, exceptional
  χ_p goes with *harder* forced windows, matching z45's "pretence makes primes harder on average".

No Deuring–Heilbronn-type repulsion is visible.

## 5. Verdict for C9 / A02
**Narrowed to collapse.**
* **Killed.**
  * (a) in its signed bounded-order form, which is what an obstruction witness needs: Thm B (PROVED; CERTIFIED for
    B ≤ 952, also with box image 94 % of G; Dickson for all B) and Thm C (abstract).
  * The unsigned form at fixed η, for all B: Prop B″ (Dickson); CERTIFIED only for η > 1/63.
* **Killed at EVIDENCE level.** (b)/(c′) in the form of a non-BM shared exceptional character (§4.2–4.3).
* **Reduced.** The odd real layer is (I)7 (BM; exact share Prop 1; silent at forced windows) plus genus twists (Prop 2).
  The twists are §7.3's kind of object (Assessment).
* **Not refuted.** The any-order version (§3.6).
* **Surviving, unchanged.**
  * §7.3 and §7.4.
  * The poverty-type B2 core: 186.6 of 222.8 forced obstructions per 500 windows at hard primes, and 82 % at controls.
* **Z3003's identity.** It remains a correct *exact* certificate of failure. Any inverse theorem built on it would have to
  describe order-≍|G| Bohr structure (Thm C) together with a target-aware sign (31121/43), which is B2 itself (Assessment).

## 6. Proposed FRONTIER changes (not applied)
* **§7.3, append:** *(z52d, `Z52D_FOURIER.md`.)*
  * In window coordinates (e ≡ 3 (4), N = (p+e)/4), the BM character χ_{−e} carries exactly
    c = (e/p)∏_{s|N,(s/p)=−1}(2b_s+1)⁻¹ of the normalised Fourier obstruction mass (PROVED, via (J)83's transfer). It
    obstructs only unforced windows.
  * Every other odd real obstruction is χ_p twisted by an even genus character of the window, the window analogue of this
    item's other genus characters (Assessment). Subgroup obstructions are 2-primary (PROVED).
  * A signed bounded-order character inverse lemma is false (Thm B: PROVED; CERTIFIED for B ≤ 952; Dickson for all B).
  * No non-BM character is shared across the forced windows of hard primes, and no Deuring–Heilbronn repulsion appears
    (EVIDENCE: 30 hard / 116 matched / 400 random primes).
  * So the "regime split / exceptional character" cluster (C9/A02) reduces to this item plus B2 (Assessment).
* **§6 dead ends, add:** "Signed bounded-order Fourier/character inverse for window obstructions (Z3003 route): false
  (`Z52D_FOURIER` Thm B, C). The only shared character found is χ_p (BM), which is silent at forced windows. No repulsion
  (EVIDENCE). The any-order version is open but carries no target information known to us."

## 7. Reproduction
Run everything from `scripts/` with `ulimit -v 8000000`.
1. *Prime lists.* `python z52d_fourier_primes.py` → `primes.json`; `python z52d_fourier_random.py` → `random400.txt`.
2. *Scans.* Run `xargs -P8 -I{} sh -c 'python z52d_fourier_scan.py 2000 {} > /tmp/scan/{}.jsonl'` over hard ∪ control,
   and the same with `1000` over `random400.txt`. This takes ≈ 3 + 9 min on 8 cores.
3. *Compaction.* Concatenate each set, then run `python z52d_fourier_compact.py <in> <out.gz>`. It keeps the
   top-character lists with conductor ≤ 200.
4. *Analyses.*
   * `z52d_fourier_analyze.py <scan>` → `analyze_*.txt`
   * `z52d_fourier_thmB_count.py <scan>` → `thmB_count_*.txt`
   * `z52d_fourier_xwin.py <scan> 0.15|0.3`
   * `z52d_fourier_excess.py <scan> [200]`
   * `z52d_fourier_repulsion.py <scan>`
   * `z52d_fourier_smallgroups.py 46` (6 s)
   * `z52d_fourier_thmC_check.py`
   * `uv run --with sympy python z52d_fourier_certify.py` → `certify_thmB.txt`

## 8. Review
A hostile reviewer subagent (fresh context) checked every proof step and re-derived the key numbers independently: Prop 1
on 400 random windows, the 31121/43 profile, the Thm B examples, the Thm B count, the large-box counts and all tables. It
found Lemma T, Cor T′, Cor 2.2, Props 1–3, Thm B, Prop B′ and Thm C correct.

Fixed after review:
* **Signed vs unsigned.** The signed/unsigned distinction is now explicit. The unsigned version mostly *holds* in the data,
  only via χ_{−e}. Prop B″ was added for the unsigned case.
* **Any-order version.** Downgraded from "killed" to open (§3.6).
* **Thm C.** Now states the multiset size and the image size. Our check: the image reaches G ∖ {τ}, so this is not poverty.
  The reviewer's "image < m/2" was an error.
* **Wording.** "Poverty is not the reason" is now "box size is not the reason", with the image coverage given.
* **Unsupported claim.** "Hard primes' extra forced failures are poverty" was not supported and is replaced by the
  class-by-class table. Genus-twist and non-real kills are now separated.
* **Selection effects.** Now disclosed: the control filter m_II < 31, an e ≥ 200 rerun, per-500-window normalisation, and
  the note that the hard/control repulsion figure comes from an outcome-selected sample.
* **Scan bug.** `p % e` was used where `e % p` was meant, and e < 3p was not enforced. Both are fixed and every scan was rerun.
* **Labels and citations.** The pointwise freedom of BM (FRONTIER §2.4, "Related exact reductions", (J)103 Prop 2.2) is a
  main-term statement. For individual factors we now cite CLASS_FORCING Prop 5.1(c) and Thm 5.2, not Thm 2.1. "Odd real"
  replaces "real" where meant. "Only shared character" is labelled Assessment. Prior work (z45 §5.2, rank_O charobs) is
  credited. Minor number fixes: 2.10/2.54, median 0.42–1.0.
* **Reproducibility.** `z52d_fourier_random.py`, `z52d_fourier_thmC_check.py` and `z52d_fourier_thmB_count.py` were added.
