# Second independent hostile cross-lab review (Claude Opus): QB cap bound, `notes/z80/BEYOND_34.md` §§5–7, 10–11

Reviewer: Claude Opus (Anthropic), second cross-lab referee. Author: GPT-6.2 Astra lane. Object: `notes/z80/BEYOND_34.md`
at `side-agent/z80-beyond-34` (HEAD 6c9d497e1), read with `git show`; I did not check its files out into this
worktree. The first Opus QB review (`data/z80/xreview/REVIEW_BEYOND_34_QB_OPUS.md`) was read **only after** my verdict
had been written down (§7). Everything here is an internal review only. **ES in ℕ is OPEN. Nothing here proves ES, cap
zero, or a bounded cap.**

## Verdict

| result | verdict |
|---|---|
| **QB (unconditional)**: for every fixed ε>0, log(1+e*(n)) ≪_ε (log R)^ε, R = rad n → ∞ | **ACCEPT-WITH-FIXES** (presentation/scope only; no mathematical gap found). PROVED, **ineffective**, rel. Maynard Thm 1.1, large sieve, Linnik, Dickman, TZ Thm 1.4/Stark (deg 2), plus the internal z75 §§1, 4a and Lemma 6 |
| **QB (GRH)**: ≪_ε (log₂R)^ε | **ACCEPT-WITH-FIXES**. CONDITIONAL on Dirichlet GRH, used only for the height of q; still ineffective |
| **Lemma 5** (§5), **Lemma 6** (§6) | **ACCEPT** |
| **Theorem Q** (§7, GRH, coefficient 2) | **ACCEPT** (re-derived; superseded by QB-GRH, keep only as an intermediate) |

I found no failing line. Below, each claim is re-derived from the definitions, not from the note's paraphrase.

## 1. Is the bounded object exactly the STATUS/z75/z78 relaxation? Yes

Source definition: `EXPONENT_CAP.md` Def 1.1. ES^{(y,e)}(n) asks for 4/n = 1/x+1/y+1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, and
every ℓ with v_ℓ(z)<0 must satisfy ℓ ∤ 2n, ℓ | y, v_ℓ(z) even and v_ℓ(z) ≥ −2e. Then e*(n) = least such e. STATUS §1B
states the same thing: den z = r², r odd, (r,n)=1, rad r | y, v_ℓ(r) ≤ e. z75 §§1, 4a and z78 §4 use this same
definition. QB's packet meets every clause:
* **x, y integral.** x = K′ = (R+qb)/4 is odd, because R ≡ 1 (8) and qb ≡ 3 (8), so R+qb ≡ 4 (8). y = RA₀ with
  A₀ = (K′+d₁)/(qb), which is integral because d₁ ≡ −K′ mod the squarefree qb (§3 below).
* **Identity.** 1/K′ + 1/(RA₀) + d₁/(RK′A₀) = 1/K′ + (K′+d₁)/(RK′A₀) = 1/K′ + qb/(RK′) = 4/R.
* **Denominator support.** den z | d₁, and every prime of d₁ divides K′: this holds for g's primes, for 3 (3 | K′),
  and for every v_i (forced by b). Also gcd(K′, Rqb) = 1, since a prime of K′ dividing qb would divide R, while q and the
  r are ≡ 3 resp. 1 (mod 4) and are not 1 (mod 8), unlike the primes of R. So the denominator primes are odd and prime to
  n. No extra freedom in x or y is used.
* **Valuations.** For p^c ∥ K′ and w = v_p(d₁): if w > c, then v_p(A₀) = c (p ∤ qb) and v_p(z) = 2c−w; if w = c, then
  v_p(z) ≥ 0. Hence every denominator prime divides A₀ | y. Parity: w−2c = L_o·v_p(g) + 2L·a_p − c ≡ v_p(g) − c ≡ 0
  (mod 2), because L_o is odd and v_p(g) ≡ c (mod 2). This includes p = 3, where v₃(g) = 2δ + (c mod 4).
* **Cap.** (w−2c)/2 ≤ (5L_o + 2L)/2, because v_p(g) ≤ 5 and a_p ∈ {0,1}. The bound is independent of c.
* **The convention is the same.** The cap is on v_ℓ(r), where den z = r². z75 §1 uses this, and so do the note's formula
  "cap = half the overflow" and my script (which checks den z = ∏p^{(w−2c)^+} by exact gcd).
* **n versus R.** Scaling by n/R multiplies x, y, z by an integer supported on primes of R. These are coprime to den z,
  so the reduced denominator and the condition rad r | y are unchanged (checked exactly at n = R² and n = R·p, §5D).
* **All n > 1.** Non-hard radicals (a prime factor ≢ 1 (8), including 2 and 3) have an integral triple, which scales,
  so e* = 0. The theorem is therefore about all n > 1, not just primes. The constant is in terms of R, as in z75 and z78.

**No silent weakening found.**

## 2. Cited inputs against their published hypotheses

* **Maynard, arXiv:2006.06572v2, Thm 1.1.** I fetched the arXiv PDF. The conditions are Q₁Q₂² < x^{1−100ε},
  Q₁¹²Q₂⁷ < x^{4−100ε}, Q₁²⁰Q₂¹⁹ < x^{10−100ε}, with a fixed residue a. The bound is
  Σ_{q₁≤Q₁,(q₁,a)=1} Σ_{q₂≤Q₂,(q₂,a)=1} |π(x;q₁q₂,a) − π(x)/φ(q₁q₂)| ≪_{a,ε,A} x/(log x)^A.
  * The note's application: Q₁ = 48Y₁ = 48y^{.03}, Q₂ = 2Y₂ = 2y^{.475}, at x = y and x = 2y, with a = 1.
  * The three exponents are .980 / 3.685 / 9.625, below 1 / 4 / 10 with fixed slack. ✓
  * a = 1 with (q₁q₂, 1) = 1 is trivially satisfied. Reducing to the fixed residue 1 is exact: for primes r > 3 and
    (d,6) = 1, 1_{4d|r−1} − 1_{8d|r−1} − 1_{12d|r−1} + 1_{24d|r−1} = 1_{d|r−1}·1_{r≡5 (24)}. I checked the residues mod 24.
    The main coefficient is (1/2 − 1/4 − 1/4 + 1/8)/φ(d) = 1/(8φ(d)). ✓
  * For each fixed j, (d₁,d₂) ↦ (jd₁, d₂) is injective, so the pair sum is dominated by Maynard's double sum. ✓
  * Uniformity: Q₁, Q₂ are fixed powers of x and a is fixed. The constant depends only on ε′ and A, and both are fixed.
    The only cost is that the constant is **ineffective** (Siegel–Walfisz inside Maynard), and the note says so.
* **Dickman.** Y_i = y^{.03}, y^{.475} against z = U^{ε/2} = y^{ε/20000}, so the ratios are u = 600/ε and 9500/ε,
  fixed for fixed ε. Ψ(Y,Y^{1/u}) ~ ρ(u)Y holds for fixed u. Coprimality to 6 follows from Σ_{e|6} μ(e)Ψ(Y/e, z)
  ~ ρ(u)Y/3. The z-smooth numbers not dividing L₀ cost Y·Σ_{p^j>z, j≥2} p^{−j} = o(Y). The density ρ(600/ε) is tiny
  but fixed, so the dependence on ε goes only into ≪_ε. ✓
* **Pigeonhole on t₀.** There are ≫_ε y/log y triples (d₁,d₂,r), t₀ = (r−1)/(d₁d₂) ≤ 2y^{.495}, and each r arises at most
  τ(r−1) = y^{o(1)} times for fixed t₀. This gives ≥ y^{.504} distinct r with r−1 = t₀d₁d₂ | t₀L₀² = L, and
  log L ≤ log 2y + 2ψ(z) ≪ U^{ε/2} + log U. ✓ The level > 1/2 is essential: with P = y^θ the large sieve gives
  M^{2−2θ} bad characters, against list density V^{−.999}, so θ > 1/2 is needed. BV (θ < 1/2) would not do, as the note
  says.
* **Linnik for q.** The modulus is [D₀, R] with log D₀ ≪ U^{ε/2} + log U = o(log R), giving log q ≤ C₀ log R. Effective.
  ✓ The compatible class with (q/R) = −1 exists: at primes of R dividing D₀, (q/p) = (−1/p) = 1 is constant, and since
  D₀ < R some prime of R lies outside D₀, where the symbol is free by CRT. ✓
* **GRH height for q.** The estimate is z78 §4's *smooth* explicit formula with error O(√X log(RD₀X) + √X log²X +
  log RD₀), at X = (log R)²D₀⁴(1+U)¹⁰. The main term X/(2φ(D₀) log X) beats √X log R ≍ (log R)²D₀²U⁵ by a factor
  ≍ D₀U⁴ → ∞, and log X = O(U) with U = log₂R. ✓ The smoothing matters: an unsmoothed √X log² error loses a factor
  log R and would fail.
* **TZ Thm 1.4 over ℚ** (cyclotomic, conductor 4q). This is used for the v-lists in (V^{1/2}, V] with V = exp(CU) a
  large power of 4q. The error is *relative* to Li(V) − ϑLi(V^β). With the trivial effective bound 1 − β ≫ q^{−1/2−o(1)}
  (Stark/TZ (1.4) at degree 2, or Page), each list has ≥ V/((4q)² log V) ≥ V^{.999} primes once C/C₀ is large. ✓ Any
  1 − β ≥ q^{−O(1)} would suffice, so this input is robust.
* **Multiplicative large sieve** (Davenport ch. 27), Σ_{m≤M} Σ*_χ |Σ_{n≤N} a_nχ(n)|² ≤ (N+M²)Σ|a_n|².
  * The setup: a_n counts ordered l-tuples from 𝒞 with product n ≤ (2y)^l ≤ M², so Σa_n² ≤ l!P^l.
  * Markov at |S(χ)| > P/2 gives #bad ≤ 2M²(4l/P)^l.
  * With l ≤ U³ = y^{3/A}, log(P/4l) > .502 log 2y, so the exponent is ≤ .996 log M + O(log y) ≤ .997 log M (since
    log M ≥ CU ≫ A log U). ✓
  * The bound holds for any fixed coefficient set, so letting 𝒞 depend on R and the colour is legitimate. ✓
* **Not used:** Gallagher, Page–Siegel (beyond the deg-2 β bound), Minkowski II (QB has index j = 1 and needs no
  Minkowski step; only §7/Q uses Minkowski II, correctly), BV (only Lemma 5/Q), and the shifted-smooth "r−1 | L" input
  (this is *constructed* via Maynard + Dickman, not cited).
* **Hidden dependences.**
  * The thresholds and constants depend on ε through ρ(600/ε) and Maynard's ε′. That is the ≪_ε.
  * q enters only through log q ≤ C₀U; the "group" enters only through Q ≤ 2^k.
  * Nothing depends on R beyond U, apart from the colour choice of 𝒞, which the large sieve handles uniformly.
  * Ineffectivity is the only extra cost. Under GRH the bound stays ineffective as written, because Maynard is still used.

## 3. Re-derivation of the construction and the optimisation; circularity check

**Dependency order.** ε → U → (y, z, L₀) → Maynard gives t₀, L and the set 𝒫. Then (R/r) is tested on 𝒫: any −1 sends
us to the planted carrier. Otherwise the colour partition fixes 𝒞 and δ. Next comes q (from L and R), then h_q and k,
then V (from C₀U), then the lists, then the random v_i (from 𝒞 via the bad-character set), then b (from the v_i, q, R
and 𝒞), then K′ and g, and finally the binary digits of −g^{−L_o} at q. **The graph is acyclic.** The step I suspected
was "digits are needed before b". It is not: *every* v_i is put into K′, and the basis covers all of U = (𝔽_q^*)²
(v₀^{2L} = h is a generator). So whatever g turns out to be, its correction exists with a_i ∈ {0,1}.

**Local congruences** (d₁/K′ = g^{L_o}∏v_i^{2La_i}):
* **mod q.** (g/q) = (K′/q) = (R/q) = (q/R) = −1, using g/K′ ∈ ℚ^{*2}, 4K′ ≡ R (q) and R ≡ 1 (4). Then −g^{−L_o} ∈ U,
  because q ≡ 3 (4) and L_o is odd.
* **Surjectivity of the 2L-th power map.** v ↦ v^{2L} maps 𝔽_q^* onto U because gcd(L, Q) = 1. This holds since Q is
  odd and q ≡ −1 at every odd p | L. So the residues ρ_i exist.
* **mod r | b.** K′ ≡ R/4, so g ≡ 9^δ(R/4)·W^{−4}. The colour gives g^{(r−1)/4} = −1, and since (r−1)/4 is odd and
  divides the odd L_o, g^{L_o} = −1. Also v^{2L} = 1, because r−1 | L and v ≠ r.
* **Combining.** q ∤ b and b is squarefree, so CRT applies. ✓
* **Mod 8 and mod 3.** An even product of r ≡ 5 (24) is ≡ 1 (24), so qb ≡ 3 (8) and qb ≡ 2 ≡ −R (3). This gives
  K′ odd and 3 | K′. ✓ If R ≡ 2 (3), the planted carrier at 3 applies, since (3/R) = (R/3) = −1.

**Even-product support.**
* E[ψ(b) | even] = ∏(1+ψ(r))/2 + ∏(1−ψ(r))/2, exactly, since P(even) = 1/2.
* Each factor product has modulus ≤ exp(−(P ∓ Re S)/4) ≤ e^{−P/8}, by √t ≤ e^{(t−1)/2}.
* Inversion gives positive mass on every unit class once 2φ(D′)e^{−P/8} < 1. This holds because log D′ ≤ kCU = O(U²)
  and P ≥ y^{.503} = U^{5030}. ✓
* The nonprincipal ψ mod D′ have primitive inducer m | D′, m > 1, which is a product of chosen v_i. The random choice
  excludes every bad conductor with probability ≥ 1 − Σ_j (kV^{−.002})^j. ✓

**The optimisation.** The cap is ≤ 3.5L. The planted fallback gives log cap ≪ log r ≪ A log U. Hence
log(1+e*) ≤ log L + O(1) ≪ U^{ε/2} + log U ≪_ε U^ε. The (log R)^ε comes purely from z = U^{ε/2} in L₀ = lcm(1..z), and
the Dickman density at a fixed ratio forces z to be a fixed power of y. **There is no optimisation of q against L.**
* q's height enters only log y = A log U and log D′ = O(U²), and both are dominated.
* L enters q only through log D₀ = o(U).
* So there is no circularity between q, L, the cofactors and the modulus they must avoid. The v_i avoid R, q and 𝒞
  automatically (v ≡ 3 (4), v ≢ 0 (q), v > V^{1/2} > 2y). The v_i ⊥ R point needs saying under GRH (fix F1).

**Test inputs** (all handled):
* *n prime.* R = p.
* *n = p².* R = p, and the packet is scaled by p (checked exactly).
* *Many small prime factors.* R = 73·97·193·241·313·337 etc. was run (§5). The only R-dependence is χ_R, the colour,
  and the primes of R that may divide D₀; that last case is handled by the Jacobi-constancy argument.
* *The prime 2.* K′ is odd, A₀ is even, and there is no denominator at 2.
* *Primes of n.* The denominator is coprime to R.

**Theorem Q (§7) re-derived.**
* log(X/B₀^{k−1}) = 2u/(k+1) + (1−η)log D + O(k + log u + log L).
* With log D ~ k log k, k ~ 2√(u/((1−η)log u)) and u ~ 2t, this is 2√(1−η)·√2·√(t log t), which tends to 2√(t log t)
  as η ↑ 1/2.
* The note's "coefficient 2 in √(t log t) units" is right.
* Lemma 5 uses BV at modulus ≤ 48y^θ with θ < 1/2, which is within range. The product count is
  ≥ (θ − 1/A − o(1))·log D. ✓

## 4. Consistency with recorded barriers

* **EXPONENT_CAP Thm 2.1 / Cor 2.2 (archimedean wall).** This bounds the window by 2nQ₁²(n+Q₁²) with Q₁² = den z.
  Here den z ≈ ∏_{p|K′} p^{O(L)} ≥ K′^{≫1}, so the wall is satisfied. No contradiction.
* **Prop 3.1 (coverage needs e ≥ (log h)^{1−o(1)}).** That is a covering model with group order equal to the window.
  QB does not cover the group mod b; it hits the single target −1 by the colour structure (g^{L_o} = −1 for every b).
  The only covered group is U at q, with log q ≪ U. Outside its hypotheses.
* **z78 §§2–3 certificate floors.** These concern the deletion/Minkowski certificate with generators dividing a height-X
  window. QB has no deletion and index 1, and its generators are planted into K′ through b. Outside their hypotheses,
  as the note says (§§7, 11).
* **FRONTIER l. 1345.** exp((log₂R)^ε) is far above (log₂R)^{O(1)}, so it is consistent.

## 5. Independent computation

My script, written independently of the lane's: `scripts/z80_xrev_qb_opus2.py`. It runs in 3 min, single process:
`ulimit -v 6000000; timeout 1800 uv run --offline --no-project python -B scripts/z80_xrev_qb_opus2.py`. Output:

```
A: primes p=1 (840) <1e6: 395  composites: 8  without integral triple found: []
B: planted-carrier fallback packets: 3006  of which exact rational: 2150  max cap 966936686  (synchronised set size 70)
C: theorem-order packets  L=1467088458836  |sync|=70 : {'tried': 26, 'ok': 14, 'nofit': 10, 'nofactor': 2, 'multi': 14, ...}
   e.g. R=10513 q=11 basis=[251, 7, 379] b = product of 12 cofactor primes, bits=[0] cap=1650474516190 <= bound 2384018745608
D: tiny-L packets (post-hoc basis among factors of K'): 64  full Fraction reconstructions: 25  cap range (45, 1454953)
F2: 8/131 has no integral triple: True ;  8/241: True
F1: (n/q) != -1 for all q<5000 at n = m^2 ...
```

* **A. e* by brute force from the definition.** Cap 0 means an integral triple. e*(n) = 0 at all 395 primes p ≡ 1 (840)
  below 10⁶ and at 8 composites (73·97, 73², 97²·193, 73·97·193·241, 1201², 17401609, 3·7²·73, 4545). Each triple is
  verified with Fractions.
  * As expected, small n **cannot falsify** an upper bound on e*: ES is verified far beyond this range.
  * The honest falsification target is therefore the packet algebra, tested in C and D.
* **B. Planted fallback (z75 §1 at a synchronised r with (R/r) = −1).** 3006 radicals. 2150 were checked by exact
  rational reconstruction: identity, den z a square, odd, prime to R, rad | y, cap = (j−1)/2 ≤ (q′−3)/4. The other 856 had
  a huge j and were checked modularly.
* **C. Theorem order.** L = 4·7·11·13·17·19·23·31·37·43, with 70 synchronised primes r ≡ 5 (24), r−1 | L. The order is:
  colour, then q, then the basis v_i^{2L} ≡ h^{2^i} fixed **before** b, then the least even b by a numpy DP hitting
  −R/q mod D′, then K′ (factored) and g, then digits by discrete log. Checks:
  * all preconditions are asserted;
  * every v_i | K′;
  * d₁ ≡ −K′ mod qb by modular powering;
  * v_p(K′+d₁) = c computed mod p^{c+1};
  * den exponents even and ≤ the cap bound.

  Result: 14 packets, all with multi-prime b (up to 12 cofactor primes), digit patterns {}, {0} and {1}, and
  cap/L ≤ 1.125. Full rationals are infeasible at this L, since d₁ has about 10¹³ digits.
* **D. Full exact reconstructions.** Tiny L ∈ {364, 6916, 1293292}, with q ∈ {11, 59, 83, 107}. Here the basis is chosen
  post hoc among the factors of K′; this is legitimate for testing the packet algebra, not the order. 25 full Fraction
  reconstructions check:
  * 4/R = 1/x + 1/y + 1/z exactly;
  * den z = ∏p^{(w−2c)^+}, a perfect odd square, coprime to R;
  * rad | y, with the maximal valuation equal to the cap;
  * scaling to n = R² and n = R·p.

  All caps were ≥ 45, so no accidental ES claim arises.
* **Toy deviations (stated).**
  * q is chosen with gcd(L, (q−1)/2) = 1 directly. This is what the proof uses; q ≡ −1 mod rad(3L)_odd is only a
    sufficient device.
  * 𝒞 is restricted to the (R/r) = +1 primes of one colour. At |𝒫| = 70 the all-(+1) branch essentially never occurs,
    exactly as in the theorem, where it is the worst case.
* **Falsifiers.**
  * **F1.** At an unreduced odd square, (n/q) never equals −1, so QB cannot run there. It runs on rad n and yields capped,
    non-integral packets scaled by n/R, never cap 0.
  * **F2.** A complete search confirms that 8/131 and 8/241 have no integral triple. In every packet R+qb ≡ 4 (8), so
    (R+qb)/8 is never integral. No numerator-8 consequence.
  * **ES.** Nothing implies ES: caps are positive and huge, and only overflow parity is controlled.
* **Lane script replay.** `scripts/z80_beyond34.py` runs in 0.4 s and reproduces its stated counts (8266 / 2802 / 18 and
  the R = 241 binary packet). Its binary check is modular only (no full reconstruction); my D supplies full ones.

None of this tests Maynard, the large sieve or TZ asymptotically.

## 6. Required fixes (none mathematical)

1. **(§11, v-lists.)** "All lists consist of primes coprime to R and disjoint from 𝒞" needs its reason. Under GRH,
   V = (log R)^C can be below the primes of R, so size is no argument. The reason is v ≡ 3 (4), whereas R's primes are
   ≡ 1 (8) and 𝒞 ⊂ 1 (4). Also note that v_i ≠ 3 and v_i ∤ q.
2. **(§11, notation.)** The §10 reset defines j as the bad-conductor support size, yet §11 ends with "correct −g^{L_o}
   with j = 1", which is §6's subgroup index. Write "index 1" there.
3. **(§0/QB label.)** Keep "ineffective" for **both** forms. GRH is used only for the height of q, and Maynard is still
   invoked. Do not let STATUS read the GRH form as effective.
4. **(§11, CERTIFIED line.)** The R = 241 binary example is a modular check only. Cite an exact-reconstruction replay as
   well (e.g. this review's §5D, or the first review's 154 packets) for the packet algebra.
5. **(STATUS delta, already in the note; confirm at export.)**
   * Retain z75's effective e* ≤ exp(C√(log R log log 3R)) as the best *effective* bound.
   * Add QB as the ineffective asymptotic, and QB-GRH as superseding Q and the z78 2√2 line.
   * State that b, the window qb and den z are unbounded in R. This keeps Thm 2.1 and Prop 3.1 readers from seeing a
     contradiction.
6. **(Optional.)** Remark that QB needs no Minkowski II and no deletion. That is the precise point of departure from the
   z75/z78 certificates.

## 7. Comparison with the first Opus review (read after the above)

The first review also accepts in substance, and the two reviews agree on every mathematical step: inclusion–exclusion to
a = 1, the Maynard exponents, the colour-before-q order, the DAG, the smooth GRH error, the large-sieve exponent, and the
even-product inversion. Its required fixes (ineffectivity, label completeness, U/j/k notation, the χ_G constancy) have
been applied in HEAD and I confirm them. Differences:
* **Possibly missed.** It did not note the GRH-regime reason why the v_i are coprime to R (my fix 1), or the residual j
  clash at the end of §11 (fix 2).
* **Effectivity under GRH.** It says the GRH form "may be effective in principle". As written it is not, because
  Maynard's constant is used in both forms (fix 3). No disagreement, only a sharper label.
* **Computation.** Its order-faithful check found 15 packets at q = 11. Mine found 14, at L ≈ 1.5·10¹² with up to 12
  cofactor primes in b, so the two are comparable. Its exact check ran 154 packets at L = 9100; mine ran 25 at three tiny
  L. The two exact checks are independent and consistent.

**Bottom line.** QB is a correct theorem about the capped relaxation, rel. the cited (published) inputs and the internal
z75 lemmas: log(1+e*(n)) ≪_ε (log R)^ε unconditionally (ineffective), ≪_ε (log₂R)^ε on Dirichlet GRH. It is not ES and
not cap 0.
