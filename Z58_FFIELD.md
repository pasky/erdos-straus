# Z58_FFIELD — the function-field analogue of (★)/(MS) over F_q[T]

Status: wave z58, lane FFIELD (brief `z52bbriefs/z58_lanes.md` §FFIELD, rules `z52bbriefs/z53_depth.md` with z53 → z58).
**Final draft (checkpoint 1 + §§3–5).** Internal; hostile review pending. **ES is OPEN; nothing here proves or disproves ES, (★) or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_ffield_*`,
data `data/z58/ffield/` (≈ 3 MB).

**Verdict: narrowed** (FF tools do not break B2; the large-q direction is dead by Cor 3.2), with the model confirmed
as a faithful laboratory (§5). Main facts: Lemma 1.2 (T1), Prop 3.1 (residue-blind local densities, also over ℤ),
Cor 3.2 (q-uniform proofs impossible), Prop 3.3 (avoiders below level n/2), Lemma 4.1 + Table 4.1 (q = 3: irreducible
zeros only at degrees 6–12 among ≤ 18, all ≡ 1 mod T³ − T).

Prior work this lane builds on (`git grep` done; not redone): `EXSET_FUNCTION_FIELD.md` (z51, the U_q analogue: colour at
∞, T1, mass = shape count, word maps finite flat, Chebotarev large-q limit, **Thm 3.5/Cor 3.5′: at fixed n and large q a
positive proportion of irreducibles have no nontrivial word**, Thm 3.9 exp(−cn²), fixed-q obstructions §4.3);
`FUNCTIONFIELD_ES*.md`, `FF_MUTE.md`, `DRINFELD_ES.md` (polynomial-numerator ES_q(A, P), mute places, coverings).
What is new here: the exact (★)/(MS) analogue (a strict sub-union of U_q, with the parity of n built in), its census with
all four z58 falsifiers, the sub-line (numerator-8) analogue, and the primality/roughness diagnostics.

## 0. MANDATORY FALSIFIER TABLE (checkpoint 1; re-stated at the end)

The "idea" of this lane is the *function-field model itself* as a generator: does the F_q[T] analogue of (MS) behave
like (MS), and does any tool special to F_q[T] (Weil/RH, Lang–Weil, Chebotarev in q) prove it?

| screen | behaviour of the F_q[T] analogue (★)_q / MS_q | status |
|---|---|---|
| **F1 odd squares** | R_q(g²) = 0 for every monic g (Lemma 1.2: every (★)_q witness has colour (−r/d) = −1 forced at ∞, impossible when −r ≡ g² mod d). All squares are zeros in every run. Non-squareness enters at exactly this step (the Jacobi symbol at the divisor d). | PROVED; CERTIFIED (runs) |
| **F2 C-even sub-line** | F_q[T] has only one "2-adic" quadratic character for monic data (degree parity at ∞), so there is no literal (2/·) split. The natural half-mass sub-lines s = deg t ≡ 1 (4) and ≡ 3 (4) keep **irreducible zeros where the full family has none**: q = 3, n = 14: 9 resp. 3; n = 16: 15 resp. 0 (full family: 0, 0). The single-t-degree line s = 1 (the "C = 1" analogue) has 29 070 irreducible zeros at n = 16. | CERTIFIED (q = 3, n ≤ 16) |
| **F3 composites** | Non-square composite zeros persist: q = 3, n = 4, 6, …, 16: 6, 27, 48, 87, 67, 51, 15; irreducible zeros 0, 3, 3, 6, 3, 0, 0. An argument using non-squareness only would prove a false statement in the model. | CERTIFIED |
| **F4 known zeros** | At fixed n and large q a positive proportion of irreducible P of degree n are zeros (z51 Cor 3.5′ applies verbatim, §2.3); data q = 7, 11: 8–10 % of irreducible quartics, 1.3–1.4 % of sextics. At q = 3 the irreducible zeros (degrees 6–12) are a finite-looking sporadic set (none at 14, 16, 18). So any F_q[T] proof of MS_q needs a degree threshold N₀(q) that tends to ∞ with q; Lang–Weil/Chebotarev in q can never give positivity at a fixed degree. | PROVED (rel. Chebotarev, as in z51); CERTIFIED (data) |

Assessment (checkpoint 1): the model is a **faithful toy** of (MS) — it reproduces all four falsifiers — which is
exactly why it does not obviously escape B2: §§3–4 test whether its extra tools do.

## 1. The analogue, precisely

Setting: q = p^r ≡ 3 (mod 4), R = F_q[T], "positive" = monic (Hayes' sign), ε = χ(−1) = −1. Reciprocity (Rosen Thm 3.3,
as recalled in `EXSET_FUNCTION_FIELD.md` §1.1): for coprime monic a, B, (a/B)(B/a) = ε^{deg a·deg B}; (c/B) = χ(c)^{deg B}.

**Dictionary (Assessment, justified by Lemmas 1.1–1.3).**

| ℤ | F_q[T] |
|---|---|
| p prime, p ≡ 1 (mod 4) [(−1/p) = 1] | P monic irreducible, deg P = n **even** [(−1/P) = ε^n = 1] |
| u, B, C ≥ 1 | u, v, t monic |
| t = 4C, i.e. v₂(t) ≥ 2 (forces the colour) | deg t odd (forces the colour at ∞) |
| (★): 4uBC − u − B = n | (★)_q: t u v − u − v = f, deg t odd |
| d = 4uC − 1 ≡ 3 (4), r = (−p mod d) ∈ [1, d), r ∣ (d+1)/4 | d = tu − 1 monic, r = (−f mod d) **monic**, r ∣ d + 1, deg d − deg r odd |
| C even (numerator 8, v₂(t) ≥ 3) | no literal analogue (one ∞-adic character); proxy: deg t mod 4 sub-lines |

**Definition 1.0.** For monic f of degree n, R_q(f) := #{(t, u, v) monic : tuv − u − v = f, deg t odd}.
**MS_q(N₀):** every monic irreducible P with deg P even and ≥ N₀ has R_q(P) ≥ 1.

**Lemma 1.1 (parity bookkeeping; PROVED).** If n = deg f is even, every (★)_q word has deg u + deg v odd (exactly one of
u, v has odd degree; ℤ: exactly one of u, B is even, since u + B ≡ −n ≡ 3 (mod 4)), and the trivial word (f + 2, 1, 1)
is excluded. For n odd the trivial word has deg t = n odd, so R_q(f) ≥ 1 for all f: odd n is the analogue of p ≡ 3 (4),
which is classically trivial. *Proof.* deg t + deg u + deg v = n with deg t odd. ∎

**Lemma 1.2 (bijection with the d-form, colour, T1; PROVED).** (i) (t, u, v) ↦ d := tu − 1 is a bijection from (★)_q
words of f onto monic d with r := (−f mod d) monic, r ∣ d + 1, deg((d+1)/r) odd, and deg d ≤ n; inverse u = r,
t = (d+1)/r, v = (f + r)/d. (ii) For such d, (−r/d) = −1. (iii) Hence R_q(g²) = 0 for every monic g.
*Proof.* (i) tuv − u − v = f ⟺ v(tu − 1) = f + u, so d ∣ f + u, and deg u < deg d (deg t ≥ 1)
makes u the least residue of −f mod d; u ∣ d + 1 = tu. Conversely given d, r: v := (f + r)/d is monic (f + r is monic
of degree n ≥ deg d, deg r < deg d) and tuv − u − v = (d + 1)v − r − v = f. (ii) gcd(r, d) = 1 since d ≡ −1 (mod r).
(−1/d) = ε^{deg d}, (r/d) = ε^{deg r deg d}(d/r) = ε^{deg r deg d}(−1/r) = ε^{deg r deg d + deg r}; product exponent
(deg d + 1)(deg r + 1) − 1 is odd because deg d − deg r = deg t is odd (so one of deg d, deg r is odd). (iii) For a
prime ℓ ∣ d, ℓ ∤ r (gcd), so ℓ ∤ g, and −r ≡ g² (mod ℓ): (−r/ℓ) = 1 for all ℓ ∣ d, so (−r/d) = 1, contradicting (ii). ∎
(This is z51 Lemma 1.1 + Thm 1.3 specialised to the t-colour; the integer counterpart is Z57_SYNTH Lemma A.1.)

**Lemma 1.3 (u = 1 line = sums of two squares; PROVED).** For n even, (★)_q words with u = 1 or v = 1 exist iff f + 1 has
a monic irreducible factor of odd degree. (ℤ: u = 1 words exist iff (n + 1)/2 has a prime factor ≡ 3 (mod 4).)
*Proof.* v = 1: f + 1 = u(t − 1) with deg t odd; deg u = n − deg t is odd. So such words ⟺ f + 1 has a monic divisor of
odd degree < n ⟺ (n even) f + 1 has an odd-degree irreducible factor. Same for u = 1 by symmetry. ∎
So "all factors of f + 1 have even degree" ⟺ f + 1 = N_{F_{q²}[T]/F_q[T]}(g)·(unit), the analogue of "only primes
≡ 1 (4)": the Landau-type density ≍ n^{−1/2} is the same phenomenon.

## 2. Census (CERTIFIED)

Engine `scripts/z58_ffield_enum.c` (C; enumerates every (★)_q word of every shape, inner loop linear in the
largest-degree variable; classifies every f as square / irreducible / composite by a product sieve). Validated in mode
U against z51 Table 2.1 (q = 3, n = 3..10: non-square U-failures 5, 6, 6, 21, 3, 21, 0, 12 and irreducible ones 3, 3,
0, 3, 0 at n = 5, 6, 7, 8, 10 — exact match). Mass check: the mean of R_q over all f equals the shape count
n(n + 2)/4 exactly in every run. Command: `gcc -O2 -o z58ff scripts/z58_ffield_enum.c && ./z58ff q n star
data/z58/ffield/star_q{q}_n{n}`; summaries `*.sum`, zero lists `*.zeros`.

**Table 2.1 (q = 3; zeros of R_q and of sub-lines).** #irr = number of monic irreducibles of degree n.

| n | #irr | full: irr / comp / sq | s ≡ 1 (4): irr | s ≡ 3 (4): irr | s = 1: irr | mean R: irr / all |
|---|---|---|---|---|---|---|
| 4 | 18 | 0 / 6 / 9 | 0 | 0 | 0 | 10.0 / 6 |
| 6 | 116 | 3 / 27 / 27 | 3 | 9 | 3 | 18.4 / 12 |
| 8 | 810 | 3 / 48 / 81 | 15 | 3 | 18 | 30.4 / 20 |
| 10 | 5 880 | 6 / 87 / 243 | 15 | 18 | 126 | 45.1 / 30 |
| 12 | 44 220 | 3 / 67 / 729 | 15 | 6 | 688 | 62.8 / 42 |
| 14 | 341 484 | **0** / 51 / 2 187 | 9 | 3 | 4 482 | 83.4 / 56 |
| 16 | 2 690 010 | **0** / 15 / 6 561 | 15 | 0 | 29 070 | 107.0 / 72 |

**Table 2.2 (larger q).** Full family.

| q | n | irr zeros / #irr | comp zeros / #comp | mean R irr / all |
|---|---|---|---|---|
| 7 | 4 | 49 / 588 (8.3 %) | 252 / 1 764 | 7.05 / 6 |
| 7 | 6 | 280 / 19 544 (1.43 %) | 2 422 / 97 762 | 14.05 / 12 |
| 7 | 8 | 707 / 720 300 (0.098 %) | 13 041 / 5 042 100 | 23.41 / 20 |
| 7 | 10 | 938 / 28 245 840 (3.3·10⁻³ %) | 40 096 / 254 212 602 | 35.08 / 30 |
| 11 | 4 | 363 / 3 630 (10 %) | 1 441 / 10 890 | 6.60 / 6 |
| 11 | 6 | 3 674 / 295 020 (1.25 %) | 29 315 / 1 475 210 | 13.21 / 12 |

Observations (EVIDENCE): (a) at q = 3 the irreducible zeros stop after n = 12 while composite zeros continue — the
ℤ picture (14 prime zeros ≤ 8.8·10⁶ vs 285 composite zeros ≤ 8·10⁶); (b) irreducibles carry a "singular series"
excess of R that shrinks as q grows (ratio 1.49 at q = 3, 1.17 at q = 7, 1.10 at q = 11); (c) R_q(P) mod 3 is
equidistributed over irreducibles (no Chevalley–Warning-type congruence to exploit).

## 2.3 Large q, fixed n (PROVED relative to Chebotarev, by citation)

(★)_q at even n is a union of word shapes (s, a, b), s odd, that excludes the trivial shape (n, 0, 0). z51
Cor 3.5′ (`EXSET_FUNCTION_FIELD.md` §3.5) therefore applies verbatim: for each even n there are c′_n > 0, C′_n with
#{P irreducible of degree n : R_q(P) = 0} ≥ c′_n qⁿ − C′_n q^{n−1/2} for every odd q (so for q ≥ q₀(n) a positive
proportion). Reason: R_q(P) is the number of F_q-points in the fibre over the point P of a finite flat generically étale
map ⊔_σ A^n → A^n (a 0-dimensional fibre — Lang–Weil has nothing to act on); the boundary n-cycle of the monodromy is
fixed-point-free on every non-trivial shape fibre and acts as an n-cycle on the roots of P.

## 3. What the F_q[T] tools give

### 3.1 Local densities are blind to residuosity; where primality enters the main term

**Proposition 3.1 (PROVED, elementary).** Let ℓ be a monic prime of R, Q = |ℓ|, f₀ ∈ R/ℓ. Then
#{(x, y, z) ∈ (R/ℓ)³ : xyz − y − z = f₀} = Q² + 1 if f₀ ≠ 0, and Q² − Q + 1 if f₀ = 0.
The same holds over ℤ for 4xyz − y − z ≡ n (mod ℓ), ℓ odd prime (substitute x ↦ 4x).
*Proof.* For a pair (x, y) with xy ≠ 1 there is exactly one z. Pairs with xy = 1 (Q − 1 of them) need f₀ + y = 0;
if f₀ ≠ 0 exactly one such pair (y = −f₀, x = −1/f₀) and then every z works (Q solutions); if f₀ = 0, none
(y ≠ 0). Total Q² − (Q − 1) + Q resp. Q² − (Q − 1). ∎ (Checked numerically for Q ≤ 11.)

*Consequences.* (a) The local word density at a prime ℓ ∤ f is (1 + Q⁻²) **whatever f is mod ℓ** — in particular
the same for quadratic residues and non-residues. So no product of local densities at finite places can separate
irreducibles from rough squares; T1 is invisible place by place and lives only in the reciprocity coupling with ∞
(Lemma 1.2(ii)). This is the F_q[T] face of the closed "low-conductor universality" item (FRONTIER §6).
(b) At ℓ | f the density drops to 1 − Q⁻¹ + Q⁻² (and no witness d is divisible by ℓ: ℓ | d, d | f + r would
give ℓ | r | d + 1). That is where primality enters the *main term*: an irreducible P has no small prime factor.
Heuristically E[R_q | P irreducible]/E[R_q] → ∏_ℓ (1 + |ℓ|⁻²) = ζ_A(2)/ζ_A(4) = (1 − q⁻³)/(1 − q⁻¹)
= 1.444, 1.163, 1.099 for q = 3, 7, 11 (EVIDENCE: observed 1.487 at (3, 16), drifting down roughly like 1.444 +
0.7/n; 1.171 at (7, 8); 1.101 at (11, 6)). (c) It is also where the composite zeros come from (§4.2).

### 3.2 Large q: Chebotarev sees irreducibility, and it is not enough

(Answer to brief (c).) For fixed P the solution set is 0-dimensional: R_q(P) = #X_P(F_q), where
X_P = ⊔_σ φ_σ⁻¹(P) is the fibre over the F_q-point P of the finite flat, generically étale word map
⊔_{σ = (s,a,b), s odd} A^n → A^n of degree Σ_σ n!/(s!a!b!) (z51 Lemma 3.2). There is no positive-dimensional
variety for Lang–Weil to act on; X_P has an F_q-point iff Frob_P has a fixed point on some shape fibre. Irreducibility
of P is *not* a geometric property (P splits over F̄_q); it enters only as the cycle type (n-cycle) of Frob_P on the
roots, i.e. through Chebotarev in the joint cover (word fibres × roots). z51 Cor 3.5′ exhibits an element of the joint
geometric monodromy group that is an n-cycle on the roots and fixed-point-free on every non-trivial shape fibre;
hence (§2.3) a positive proportion of irreducible P of each even degree n fail for q ≥ q₀(n).

**Corollary 3.2 (PROVED rel. Chebotarev as in z51 Thm 3.3).** For no N₀ does MS_q(N₀) hold for all q ≡ 3 (mod 4):
the threshold of any true MS_q statement must satisfy N₀(q) → ∞. In particular any F_q[T] argument whose estimates
improve with q at fixed degree (Lang–Weil, Deligne, large-q Chebotarev, Sawin–Shusterman-type k < √q/(pe) ranges)
cannot prove MS_q by itself. Empirically (CERTIFIED): last irreducible zero degree ≥ 12 at q = 3 (none at 14, 16),
zeros at n = 8 for q = 7 (707), at n = 6 for q = 11 (3 674).

*Remark (lc-free variants fail F3).* If the shift's leading coefficient is free, or only required to be a square
(the colour is then unchanged, since χ(lc) = 1), z51 Prop 1.7(ii)'s single Weil sum over the q unit shifts proves a
witness for **every** non-square f once q > (n + 1)². Such a mechanism sees only geometric data (“w² = −f is
irreducible”) and would, in the monic model, prove positivity at the composite zeros of Table 2.1: it fails F3 there,
and it has no ℤ analogue (positivity leaves the single unit 1).

### 3.3 Fixed q: RH gives the level, not the event

**Proposition 3.3 (avoiders below level n/2; PROVED relative to the Riemann hypothesis for Dirichlet L-functions of
F_q[T], Weil; e.g. Rosen, *Number Theory in Function Fields*, Thm 4.8).** Let M be monic with deg M ≤ (1/2 − δ)n, ω(M)
its number of distinct prime factors. For n ≥ n₀(q, δ) the number of irreducible P of degree n with no (★)_q witness
d dividing M is ≥ q^n/(2n·2^{ω(M)}). With M = M_m := lcm of all monic polynomials of degree ≤ m this holds whenever
deg M_m ≤ (1/2 − δ)n, i.e. for m up to ≈ log_q n: **no menu of witnesses of degree ≤ m ≈ log_q n covers all large P**.
*Proof.* If P ≡ g² (mod M) with gcd(g, M) = 1, then for every d | M a witness would give −r ≡ g² (mod d), contradicting
Lemma 1.2(ii). The unit squares mod M form a subgroup of index 2^{ω(M)} (q odd: (R/ℓ^e)* is cyclic of order Q − 1
times a p-group). Dirichlet with RH: #{P irreducible, deg n, P ≡ a (M)} = q^n/(nΦ(M)) + O(deg M·q^{n/2}/n) for each unit a.
Summing over the Φ(M)/2^{ω(M)} square classes, the error is O(deg M·q^{n/2}Φ(M)/(n2^{ω})) and Φ(M) ≤ q^{deg M} ≤
q^{(1/2−δ)n}, so the main term wins for large n. ∎
This is the F_q[T] version of SYNTH Prop A.3 (B1), with the RH-explicit range. It is also sharp in spirit: by RH every
non-square P has a non-residue prime of degree ≤ 2 log_q n + O(1) (z51 §5.1), so the colour data are exhausted at
logarithmic degree, while witnesses for the hardest P must be found among moduli whose joint lcm exceeds the
equidistribution level. A sieve on residue classes of P saves at most a power of n (dimension κ: Mertens product), while
#irreducibles is q^n/n: the gap is exponential, exactly the integer B2/B6 situation (z51 §4.2–4.3 for U_q).

### 3.4 A structure ℤ lacks: composition

**Lemma 3.4 (PROVED).** If φ is monic of odd degree k and (t, u, v) is a (★)_q word of f, then (t∘φ, u∘φ, v∘φ) is
a (★)_q word of f∘φ (degrees multiply by k, so deg t∘φ stays odd; monic is preserved), and distinct words give
distinct words. Hence R_q(f∘φ) ≥ R_q(f); a zero of R_q of the form f∘φ (deg φ odd) forces f to be a zero.
Only decomposable P (a q^{O(n/k + k)}-sparse set) are reached; no integer analogue. Not pursued.

## 4. The laboratory at fixed q (CERTIFIED computations, EVIDENCE readings)

### 4.1 Complete census of irreducible zeros at q = 3 to degree 18

**Lemma 4.1 (q = 3 "Mordell lemma"; PROVED).** If P is irreducible of degree n ≥ 2 and P(c) = −1 for some c ∈ F_q,
then R_q(P) ≥ 1 (word t = T − c + 1, u = 1, v = (P + 1)/(T − c); deg t = 1). At q = 3, F_3^* = {±1}, so every
irreducible zero satisfies P ≡ 1 (mod T³ − T): *P is a quadratic residue at every degree-1 prime* — the analogue of
Mordell's classes 𝔐 (the squares mod 840). ∎

Independent engine `scripts/z58_ffield_decide.gp` (per-P u-form decider: for monic u of degree a ≤ (n − 2)/2, factor
P + u and test its divisors d ≡ −1 (mod u), a < deg d < n − a, deg d − a odd; WLOG deg u < deg v), run by
`scripts/z58_ffield_census3.gp` on all P ≡ 1 (mod T³ − T), one representative per translation orbit T ↦ T + c
(R_q is translation invariant). It reproduces the word-enumeration zeros exactly at n = 10, 12, 14, 16.

**Table 4.1 (q = 3, CERTIFIED).** Irreducible zeros of R_3 by degree: n = 2: 0, 4: 0, 6: 3, 8: 3, 10: 6, 12: 3,
**14: 0, 16: 0, 18: 0** (n = 18: 14 348 907 candidates, 2 689 596 irreducible, 896 556 orbit representatives, all
decided; 8.4 min). So at q = 3 the last irreducible zero has degree 12 among degrees ≤ 18 (|P| = 3¹⁸ ≈ 3.9·10⁸).
The 15 zeros (5 orbits) are listed in `data/z58/ffield/star_q3_n{6,8,10,12}.zeros`; each has P − 1 divisible by
T³ − T, P + 1 a product of even-degree primes (Lemma 1.3), and 0–2 non-residue quadratic primes out of 3
(`scripts/z58_ffield_irrzeros.py`).
For q = 7 the zeros persist much longer: 49, 280, 707, **938** irreducible zeros at n = 4, 6, 8, 10 (rate 8.3·10⁻²,
1.4·10⁻², 9.8·10⁻⁴, 3.3·10⁻⁵; n = 10 is a complete 7¹⁰-word enumeration, 12 min). Consistent with Cor 3.2: the
threshold grows with q.

### 4.2 Composite zeros: the same structure as over ℤ

q = 3 non-square composite zeros: 6, 27, 48, 87, 67, 51, 15 at n = 4..16. Factor types (`z58_ffield_factor.py`): at
n = 16 all 15 have at least two distinct linear factors (types like 1·1·2·12, 1·1²·1⁶·2·5); at n = 12, 14 there is a
thin tail of *rough* squarefree composites with two factors (types 2·10, 3·9, 2·12). Over ℤ the 285 composite zeros
≤ 8·10⁶ behave the same way (computed here from `data/z58/screens/`): smallest prime factor 3 for 214, ≤ 13 for 274,
and only 11 have all prime factors > 13 — all with two or three factors (e.g. 2641 = 19·139, 810001 = 241·3361).
Reading (Assessment): composite zeros are mostly explained by Prop 3.1(b) (small factors lower the local density and
forbid all d sharing them); the rough tail is the genuine B2-type residue, in both rings.

### 4.3 Targeted maximal-avoidance classes (FF version of the DISPROOF search)

`scripts/z58_ffield_target.gp`: P = 1 + M·h, M = lcm of all monic polynomials of degree ≤ 2 (deg 12), optionally
times K₃ irreducible cubics; such P avoid every witness d | M (colour lemma; confirmed: no first witness of degree ≤ 2
ever occurs). q = 3, exhaustive in h (CERTIFIED):

| n | M | irreducible P | zeros | max a* |
|---|---|---|---|---|
| 14, 16, 18, 20, 22 | M₂ (deg 12) | 6, 12, 219, 1 464, 13 044 | 0 | 1, 1, 3, 3, 4 |
| 24 | M₂ | 105 496 | 0 | 3 |
| 26, 28, 30 | M₂·(4 cubics) (deg 24) | 3, 18, 139 | 0 | 1, 2, 3 |

No zero in the hardest small-modulus classes up to degree 30 (|P| = 3³⁰ ≈ 2·10¹⁴) within these (small) families.

### 4.4 The least witness cofactor a* is tiny, in both rings

a*(P) := least deg u over witnesses (u the smaller cofactor; ffdec searches a increasing). Full census at q = 3
(orbit representatives of P ≡ 1 mod T³ − T; all other irreducibles have a* = 0): max a* = 3, 3, 3, 4 at n = 10,
12, 14, 16, 18 (two orbits with a* = 4 at n = 16, four at n = 18; logs `data/z58/ffield/census3_q3_n10-18.log`). Integer analogue (`scripts/z58_ffield_zleastu.py`,
least u with p + u having a divisor ≡ −1 mod 4u, primes p ≡ 1 (4) < 3·10⁶, zeros excluded): max least u = 4, 19, 78,
131, 110 for p < 10³, …, 10⁷ (the bound 10⁷ is the decade; data stop at 3·10⁶). Heuristic (Assessment): a* fails to
be ≤ A only if all ≈ q^A shifts P + u, deg u ≤ A, lack a suitable divisor, each with probability ≳ 1/n (e.g. P + u
irreducible); so max a* ≈ log_q(n/log n) + O(1), i.e. |u| ≈ (log|P|)/(log log|P|) up to constants — in ℤ terms "least
u ~ polylog p". The divisor d itself is large (a divisor of P + u), so this does not conflict with d_min ≥ n_p. This is
a conjecture for the WITNESS lane, not a result.

### 4.5 The F2 proxies

F_q[T] has a single “2-adic” character for monic data, so the ℤ split C odd / C even (v₂(t) = 2 vs ≥ 3) has no
faithful image. Proxies (q = 3, irreducible zeros, n = 6..16): s ≥ 3 (drop the smallest t-degree, as C even drops C = 1):
3, 3, 9, 3, 0, 0 — it stops with the full family; s ≡ 3 (4): 9, 3, 18, 6, 3, 0; s ≡ 1 (4): 3, 15, 15, 15, 9, 15 — does
*not* stop by n = 16; s = 1 alone: 3, 18, 126, 688, 4 482, 29 070 (fixed-t-degree lines fail polynomially often,
B1). So the model does contain half-mass sub-lines that keep failing above the last full-family zero (the F2
phenomenon), but which sub-line fails is not predicted by a 2-adic analogy. Any FF argument must use the full
union of s, or at least s ≡ 3 (4) as well as s ≡ 1 (4).

## 5. Verdict, falsifiers re-stated, proposed FRONTIER text

**Answers to the brief.**
(a) *True/false?* MS_q is false at every fixed degree for large q (Cor 3.2, positive proportion). At fixed q it is
consistent with all data: at q = 3 the last irreducible zero has degree 12 and none occur at 14, 16, 18 (complete) or in
the maximal-avoidance classes to degree 30; at q = 7 zeros persist to degree 10 at least. CONJECTURE: for each q ≡ 3 (4)
there is N₀(q) with MS_q(N₀(q)), and N₀(q) → ∞. Literature: ES over F_q[T] with a polynomial numerator is studied
internally (`FUNCTIONFIELD_ES*.md`; their web search found no published 3-term treatment); no published (★)-type
analogue was searched for again in this lane (not verified beyond the z51/O161 searches).
(b) *T1 and composites:* T1 holds (Lemma 1.2, PROVED); composite zeros exist and have the integer structure (§4.2).
(c) *Large q:* R_q(P) is the point count of a 0-dimensional fibre of a finite flat cover; Lang–Weil is vacuous;
Chebotarev sees irreducibility only as an n-cycle, and the boundary n-cycle is fixed-point-free on every shape:
positivity fails at a positive proportion (§3.2).
(d) *Fixed q:* B2 reappears exactly. RH gives the level (equidistribution of P modulo d of degree < n/2) and
logarithmic least non-residues; Prop 3.3 shows that this level is exactly where avoiders still exist. Local densities
are blind to residuosity (Prop 3.1). No F_q[T] tool found gives one event at one P.

**Verdict: narrowed** (for the FF route as a proof generator; dead for the large-q direction by Cor 3.2) — and the
model is confirmed as a **faithful, cheap laboratory** for (MS) (F1, F3, F4 reproduced; zero concentration on
“Mordell-type” residue classes; composite-zero structure; small least witness cofactor). No HOT LEAD.

**Falsifier table (final).**

| screen | result |
|---|---|
| F1 | T1 PROVED in the model (colour at ∞); squares zero in every run. Any FF argument must use non-squareness at the Jacobi symbol (−r/d); Prop 3.1 shows it cannot come from local densities. |
| F2 | No faithful image of C-parity; the proxy s ≡ 1 (4) keeps irreducible zeros above the last full zero (to n = 16), s ≥ 3 and s ≡ 3 (4) do not. Arguments must not work on one residue class of s. |
| F3 | Composite zeros persist (15 at n = 16, q = 3), mostly small-factor ones plus a rough two-factor tail, as over ℤ. Lc-free/Weil-sum mechanisms prove positivity at every non-square and therefore fail F3. |
| F4 | Large q: positive-proportion irreducible zeros at each degree, so no q-uniform argument; fixed q: zeros at degrees ≤ 12 (q = 3), ≥ 10 (q = 7). An argument must have a q-dependent degree threshold. |

**Proposed FRONTIER text** (§5.2 “Function fields” bullet; do not edit FRONTIER here): *“(z58, `Z58_FFIELD.md`.) The
exact F_q[T] analogue of (★)/(MS) — monic words tuv − u − v = P with deg t odd, deg P even, q ≡ 3 (4) — reproduces
T1, the composite zeros (small-factor dominated, with a rough tail, as over ℤ) and Mordell-type concentration of
prime zeros (at q = 3 every irreducible zero is ≡ 1 mod T³ − T). CERTIFIED: at q = 3 the irreducible zeros have
degrees 6–12 only among degrees ≤ 18. PROVED: local word densities are residue-blind (Q² + 1 solutions mod every
ℓ ∤ f, also over ℤ); avoiders of every witness modulus of degree ≤ ≈ log_q n exist (RH); at fixed degree and large q a
positive proportion of primes fail (z51 Cor 3.5′), so any FF proof needs N₀(q) → ∞. No FF tool gives a single event;
B2 reappears verbatim.”*

**Bottom line.** Over F_q[T] the (MS) analogue is a faithful toy: it has T1, composite zeros, a sporadic and
finite-looking set of prime zeros concentrated in the residue-square classes, and a least witness cofactor of
logarithmic degree. The function-field extras do not break B2. Lang–Weil has nothing to count (the fibre is
0-dimensional), large-q Chebotarev proves the *opposite* at fixed degree, RH supplies exactly the equidistribution
level at which avoiders still exist, and local densities cannot see residuosity. The useful outputs are the scoped
facts (Prop 3.1, Cor 3.2, Prop 3.3, Lemma 4.1), the cheap laboratory, which can test any proposed ℤ mechanism to
|P| ≈ 10¹⁴ in minutes, and two cross-lane pointers. For WITNESS: “least u is polylog” holds in both rings in the
tested range. For MORDELL: zeros sit in the residue-square classes in both rings.
