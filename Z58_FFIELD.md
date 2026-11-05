# Z58_FFIELD — the function-field analogue of (★)/(MS) over F_q[T]

Status: wave z58, lane FFIELD (brief `z52bbriefs/z58_lanes.md` §FFIELD, rules `z52bbriefs/z53_depth.md` with z53 → z58).
**Checkpoint 1.** Internal, not yet reviewed. **ES is OPEN; nothing here proves or disproves ES, (★) or (MS).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_ffield_*`,
data `data/z58/ffield/` (< 2 MB).

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
| **F4 known zeros** | At fixed n and large q a positive proportion of irreducible P of degree n are zeros (z51 Cor 3.5′ applies verbatim, §2.3); data q = 7, 11: 8–10 % of irreducible quartics, 1.3–1.4 % of sextics. So any F_q[T] proof of MS_q needs a degree threshold N₀(q) that tends to ∞ with q; Lang–Weil/Chebotarev in q can never give positivity at a fixed degree. | PROVED (rel. Chebotarev, as in z51); CERTIFIED (data) |

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

*To do (next):* q = 7, n = 10; q = 3, n = 18 (split run); §3 what F_q[T] tools give at fixed q; §4 where irreducibility
enters (factor structure of the composite zeros; roughness control); F2 analysis; verdict.
