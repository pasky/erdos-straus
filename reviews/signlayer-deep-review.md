# R175 — hostile review of O175 (SIGNLAYER_DEEP.md + BRAINSTORM/bsB_*.md)

Reviewer: R175 (branch side-agent/review-signlayer). Author files merged from side-agent/spark-signlayer.
From-scratch scripts: `scripts/review_sl_*.py` (own F₃[T] arithmetic; nothing imported from `scripts/bsB_*`).
Data: `data/review_sl_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| SIGNLAYER Lemma 1.1 (Case B on the slice = finite search per level K; L'', r, g' forced by (h₁, h₁', K)) | SOUND (re-derived; brute-force verified against direct factorisation of D); MINOR wording defects D1–D3 |
| §2 complete enumeration, CERTIFIED through K = 17 / 19 | SOUND-AFTER-REPAIRS: counts and exact measures reproduced independently through K = 13; the translation "K ≤ 17 ⇒ all N ≤ 18 (j ≤ 17), every L', g" is wrong (D4, MAJOR) |
| Covered measure 0.333 → 0.4906, "≈ 50 % stays uncovered" | numbers SOUND (exact rationals through K = 13); labels EVIDENCE/Assessment acceptable after D5–D6 |
| Lemma 3.1 (symmetries u ↦ u⁻¹, u(T) ↦ u(−T)) | (i) SOUND; (ii) true but the written proof has a GAP (needs FF2's QR degree parity) (D7) |
| "x* orbit = the four height-1 slice points" | FALSE as stated (six height-1 points; two are covered) (D8) |
| Lemma 3.2 (degree imbalance at x*) | SOUND; "necessarily lopsided" slightly overclaimed (D9) |

(Memo verdicts follow in later sections.)

## SIGNLAYER Lemma 1.1 — SOUND

*Dependence on FF2.* The lemma takes as input FF2 §0.2's Case B reduction (validity of a family at x_u ⟺ D = 1 + T^k a0 b0
= 1 + T^{N+1}L'g has a monic divisor E with E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L')), which R166 re-derived and found
SOUND, and which only uses x ≡ 1 at every prime ≠ T (so it holds at every slice point x_u, not only x*). Note
lc E = 1 because the two terms of the Case B sum have different degree, so the cofactor E' is monic as well. I accept
the reduction. Lemma 1.1 is valid only for the **sub-slice u ≡ 1 (mod T), u ≢ 1 (mod T²)** (v(0) ≠ 0). This is
where h₁(0) ≠ 0 is used (D5).

*Re-derivation.* E = −1 + L'h, E' = −1 + L'h' (from E ≡ −1 mod L'; this also holds for E' because D ≡ 1 mod L').
EE' = D ⟺ L'hh' − h − h' = T^{N+1}g. E ≡ −u (mod T^{N+1}) ⟺ L'h ≡ −Tv, so h = Th₁ with h₁L' ≡ −v (mod T^N) and
h₁(0) ≠ 0. Reducing the identity mod T gives T | h'. (The proof says "same for E'". That step needs this one-line
argument, which the proof leaves out. MINOR, D2.) So h' = Th₁' and T h₁h₁'L' − h₁ − h₁' = T^{N+γ}g', where
N + γ = K + 1. The leading term T h₁h₁'L' cannot cancel. This gives a + b + deg L' = K + deg g', i.e.
a + b + deg L'' = K. Since gcd(g', T) = 1, Tg' | h₁ + h₁'. That gives r and (I), (II). r ≠ 0, because r = 0 forces
h₁h₁'L'' = T^K with all three factors T-free, so K = 0 and h₁ = h₁' = 1, contradicting h₁(0) = −h₁'(0).
deg r ≤ max(a, b) − 1 − deg g' < a + b. So L'' = quo(T^K, h₁h₁') and r = L''h₁h₁' − T^K are forced. **In addition,
g' = (h₁ + h₁')/(T r) is forced**, so the whole tuple is a function of (h₁, h₁', K). This is how the enumeration
uses it; the statement lists g' as a free coordinate. The admissible N are exactly ⌈K/2⌉ + 1 ≤ N ≤ K + 1, from
0 ≤ γ = K + 1 − N ≤ N − 1. The cylinders for different N are nested, so the union over N is the N₀ cylinder,
N₀ = max(2, ⌈K/2⌉ + 1). D = 1 + T^{K+2}L'g' does not depend on N. The converse direction checks out. As a
by-product, j = 0 (N = 1) is impossible: it would force K = 0. This proves one of FF2's unproved "consequences"
(R166 D5) on the slice.

*Bound.* deg L' = deg g' + deg L'' ≤ (max(a, b) − 1) + (K − a − b) ≤ K − 1. The stated "deg L' ≤ 2K" is true but
loose (MINOR, D3).

*Independent machine check* (`scripts/review_sl_caseB.py brute 6 3`, `data/review_sl_brute_6_3.txt`). For every
N ≤ 6, 0 ≤ γ ≤ N − 1, monic T-free L' of degree ≤ 3 and every monic g' | L', I factored D = 1 + T^{N+1+γ}L'g'
completely, by trial division with my own irreducibles. For each monic divisor E with E(0) = −1, E ≡ −1 (mod L')
and v(0) ≠ 0, I recorded (N, γ, L', g', E). Result: **126 families**, identical as a set to those predicted by
Lemma 1.1 (enumerating (h₁, h₁') with K ≤ 10 and expanding over N). Nothing is missing and nothing is extra. So
Lemma 1.1 is correct both as algebra and as a search reduction.

**D1 (MINOR, wording).** "correspond bijectively to tuples (h₁, h₁', g', L'', r)". The bijection is with the data
(N, γ, L', g', E). A Case B *family* also carries (a0, b0, types), and many (a0, b0) share the same L = lcm and
g = gcd. Also, g' and L'' are functions of (h₁, h₁', K). Repair: "with the divisor data (N, γ, L', g', E); moreover
the whole tuple is determined by (h₁, h₁', K)".
**D2 (MINOR).** Proof: write the line "mod T, h' ≡ 0, so h' = Th₁'".
**D3 (MINOR).** Replace "deg L' ≤ K + max deg h ≤ 2K" with the sharp bound deg L' ≤ K − 1 − min(a, b).

## §2 complete enumeration (CERTIFIED through K = 17 / 19) — SOUND-AFTER-REPAIRS

*Completeness per level.* By Lemma 1.1, every Case B family on the sub-slice at level K comes from a pair of monic
(h₁, h₁') with h₁(0) = −h₁'(0) ≠ 0 and a + b ≤ K. The author's enumeration (`bsB_caseB.c`, read: it loops over
exactly these pairs and then applies the forced L'', r, g') is therefore complete per level, **given FF2's Case B
reduction**. CERTIFIED is an acceptable label for "no Case B family at x*_c with K ≤ 19", conditional on the
correctness of one C implementation for K = 14..19.

*Independent reproduction* (`scripts/review_sl_caseB.py enum 13`, Python, own arithmetic, 55 s; output
`data/review_sl_caseB_K13.txt`). Solutions per K = 2..13: 2, 4, 10, 8, 8, 4, 24, 12, 14, 36, 104, 48. This is
**identical** to the author's list. Exact union measures (Haar on v ∈ F₃[[T]]^*):
1/3 (K ≤ 2..4), 11/27 = 0.4074 (K ≤ 5..7), 37/81 = 0.4568 (K ≤ 8, 9), 113/243 = 0.4650, 343/729 = 0.4705,
349/729 = 0.4787, 1051/2187 = 0.4806 (K ≤ 10..13). These agree with the author's 0.333, 0.407, 0.457, 0.465, 0.471,
0.479, 0.481. x*₁, x*₂ and ι(x*_c) = 1/(1 − cT) are uncovered for all K ≤ 13. (K ≤ 15 run: see the addendum below
if it completed.) Sanity: the K = 2 pair is FF2's cylinder family, as the author says.

**D4 (MAJOR, overclaimed certified range).** §2, bullet 3: "x*₁ and x*₂ are not covered by any Case B family with
K ≤ 17, **i.e. with N ≤ 18 (j ≤ 17) and every admissible L', g**". This is false as a translation.
K = N + γ − 1 and γ ranges over 0..N − 1. So K ≤ 17 contains a family with given N only if γ ≤ 18 − N. "Every
admissible g" (γ up to N − 1) needs 2N − 2 ≤ 17, i.e. **N ≤ 9 (j ≤ 8)**. With K ≤ 19 it is N ≤ 10 (j ≤ 9), which
the "Update" paragraph states correctly. The same slip is repeated in AGENT_REPORT_O175 if it quotes "N ≤ 18";
check it. Repair: "complete for all families with N + γ ≤ 18; in particular for all N ≤ 9 (j ≤ 8) with every
admissible L', g (deg L' ≤ K − 1 is automatic)". The comparison with FF2's range (deg L' ≤ 7, j ≤ 8) remains
correct: K ≤ 17 contains it.

**D5 (MINOR, scope of "the slice").** Lemma 1.1, the measures, and "random slice points" all refer to the sub-slice
u = 1 + Tv with v(0) ≠ 0, i.e. u ≡ 1 + cT (mod T²), c ≠ 0. It is normalised to measure 1. The rest of FF2's slice
x ≡ 1 off T (u(0) = 2, or u ≡ 1 mod T²) is not treated: the derivation uses h₁(0) ≠ 0. Repair: say "sub-slice" (or
define "slice" this way in §1) wherever measures are quoted.

**D6 (MINOR→MAJOR for the narrative; labels).**
(a) §1 "Consequence for the heuristic": "the naive expected number of solutions at a fixed point is
Σ_K poly(K)·3^{−K}-type, **convergent**". Lemma 1.1 refutes FF2's specific divergence argument: the sum over
ℓ = deg L' is truncated at ℓ ≤ K − 1, and D does not depend on N. But Lemma 1.1 does **not** by itself give
convergence. A level-K solution covers a cylinder of measure (1/2)·3^{−⌈K/2⌉}, not 3^{−K}. The only a priori bound
on #sol(K) is the number of (h₁, h₁') pairs, ≈ K·3^{K}, and with that bound the expected-count sum diverges. The
convergence rests on the **observed** growth #sol(K) ≈ 3^{K/4} (ratio ≈ 1.3–1.5 per two levels, versus the
critical 3 per two levels). That is EVIDENCE, not a consequence of the lemma. Repair: state the expected-coverage
sum as Σ_K #sol(K)·3^{−K/2}. Say it converges iff #sol(K) = o(3^{K/2}) (with summable excess), and note that the
data (not Lemma 1.1) suggest this.
(b) "Reading" §2: "O(3, T²) ∩ slice has positive measure" also needs Case A to be absent on the sub-slice. The
support for that is four points with deg a0, b0 ≤ 3. It is labelled EVIDENCE, but it is very weak; say so. Also,
the limit "≈ 0.5" is an extrapolation of a monotone sequence (0.4806 at K ≤ 13, 0.4906 at K ≤ 19) whose increments
are not shown to be summable. Assessment is the right label, and "appears to converge to ≈ 0.5, not 1" should
read "the increments are consistent with a limit well below 1".

## §3 Lemma 3.1, the x* orbit, Lemma 3.2

### Lemma 3.1 — (i) SOUND; (ii) true, but the written proof has a GAP (D7)
(i) Swapping h₁ and h₁' swaps E and E', and E' ≡ −u⁻¹ (mod T^{N+1}) because D ≡ 1. The swapped tuple satisfies
(I)–(III) for v~ = (u⁻¹ − 1)/T, and v~(0) = −v(0) ≠ 0. Correct.
(ii) **D7 (MINOR, proof gap).** "(I)–(II) are homogeneous under this [σ: T ↦ −T, then rescale each factor by
(−1)^{deg}]." That is not automatic. Apply σ to (I) and rescale h₁, h₁' to monic: this gives
h₁~ + ε_aε_b h₁'~ = (…)·T g~' r~ with ε_f = (−1)^{deg f}, so (I) survives only if **a ≡ b (mod 2)**. Matching the
r~ forced by (II), (−1)^K σr, against the one forced by (I) then needs **deg E = 1 + a + deg L' even**. Both facts
are true for q = 3: FF2's quadratic-reciprocity parity (proved, R166-checked) gives deg E, deg E', deg D all even.
But they do not follow from the homogeneity that the proof invokes. A cleaner proof works on (E, E', D) directly:
deg D even ⇒ σD = 1 + T^{K+2}(±σL')(±σg') with monic factors, and deg E, deg E' even ⇒ σE, σE' are monic. So σ
maps families to families. Repair: cite FF2's parity in the proof, and note that the lemma is proved for q ≡ 3
(mod 4) (q = 3), not "for odd q with the obvious changes". Machine check (`scripts/review_sl_sym.py 11`): every
solution with K ≤ 11 has a ≡ b (mod 2) and deg E even. Invariance of the K ≤ 11 covered set under u ↦ u⁻¹ and
u(T) ↦ u(−T) holds on all 1458 depth-7 test points.

### "The x* orbit is {1 ± T, 1/(1 ± T)}: the four slice points whose u is a rational function of height 1" — FALSE (D8)
**D8 (MINOR, but it is the only structural feature §3 names).** The degree-1 rational functions with u(0) = 1 and
v(0) ≠ 0 are u = (1 + αT)/(1 + βT) with α ≠ β ∈ F₃. There are **six**, not four. The extra two,
u = (1 ± T)/(1 ∓ T) (v = ∓(1 + T + T² + …), digit prefix (c, 2) with c = ∓1), lie in the cylinder of the K = 2
family and are **covered** (`review_sl_sym.py` output). So "height 1" does not single out the x* orbit, and it does
not by itself make a point sterile. The Assessment "the only visible special feature of x* is height 1" needs
rewording: the orbit consists of the height-1 points with u or 1/u a *polynomial*, or equivalently the height-1
points outside the K = 2 cylinder. The proposed "product formula" route has to explain why
(1 ± T)/(1 ∓ T) is covered while 1 ± T is not.

### Cross-validation (b) — confirmed independently
At u = 1 + T + T² + 2T³ + T⁵ + T⁶ + 2T⁸ + T⁹ + 2T¹⁰ + T¹², my enumerator finds exactly the stated solution: K = 10,
h₁ = T³ + T² + T + 2, h₁' = T⁵ + 2T⁴ + 2T³ + T + 1, g' = (T + 1)², L'' = T² + 1, r = T² + 2,
L' = T⁴ + 2T³ + 2T² + 2T + 1. It covers at N = 6 (and also at N = 7, 8). I did not run FF2's searcher.

### Lemma 3.2 — SOUND (D9 minor)
Re-derived. (III) at v = c: h₁L' = −c + T^N y. Substituting into (*) gives −(1 + cT)h₁' − h₁ ≡ 0 (mod T^N), using
K + 1 ≥ N. If the sum vanishes, then c = −1, h₁ = (T − 1)h₁', g'r = h₁', r | T^K, r = 1 (monic, since g' and h₁'
are monic), and (T − 1)g'²L'' = T^K + 1. That fails at T = 1 because 2 ≠ 0. Otherwise
N ≤ deg(h₁ + (1 + cT)h₁') ≤ max(a, b + 1), and K = a + b + deg L'' ≤ 2N − 2 gives the two alternatives. Correct.
**D9 (MINOR).** "So a covering family at x* is necessarily lopsided (one of E, E' has much larger degree)". The
second branch b ≥ a + deg L'' allows a = b when L'' = 1. In that case deg E = deg E'. Repair: "lopsided unless
L'' = 1 and a = b".

## Memo bsB_rayclass_norm_pullback — items 1–3 SOUND; scope of the headline GAP (D10, MAJOR for the campaign ledger)

*Item 1* (hypercube = divisor lattice of N = (tp + 1)/4). Re-derived. d_K = −tp ≡ 1 (mod 4) is fundamental.
ω = (1 + √−tp)/2 has coordinate 1 on the basis element ω, so no rational prime divides it. A prime ℓ | N has
−tp ≡ 1 (mod ℓ) (for ℓ = 2: tp ≡ 7 mod 8, which is exactly when N is even), so ℓ splits, and only one of the two
primes above ℓ divides (ω). SOUND. *Small mismatch:* WR Remark 10.4 speaks of the divisors of (1 + √−tp) = (2)(ω).
When tp ≡ 3 (mod 8), (2) is inert and those divisors have norms d and 4d. The memo's ω-version is the one
matching GI Prop 4.1 (m'' | (tn + 1)/4·…), so this is fine, but say that it is a different (better) normalisation.

*Item 2* (only χ∘N enters). As a statement about detectors it is correct, and essentially tautological. The
indicator of {𝔪 : N𝔪 ≡ −1 (t)} is f∘N for a function f on (ℤ/t)^*. Its Fourier support on G is therefore
contained in the characters trivial on ker N, i.e. {χ∘N}. L(s, χ∘N_{K/ℚ}) = L(s, χ)L(s, χχ_K) (Artin induction
of a restricted character), and θ_{χ∘N} = Σ_n χ(n)(Σ_{d|n} χ_K(d)) qⁿ is a twisted weight-1 Eisenstein series.
SOUND.

*Item 3* (on G[1+σ] the norm is the genus character χ_p). Re-derived. 𝔞𝔞̄ = (N𝔞) with generators ±N𝔞 (units ±1;
−tp ≠ −3, −4), so [𝔞]^{1+σ} = 1 in G ⟺ N𝔞 ≡ ±1 (mod t). The genus product formula on norms coprime to tp
(product over the prime discriminants of −tp) gives (N𝔞/t) = (N𝔞/p), and (−1/t) = −1. SOUND. Independent
check (`scripts/review_sl_rayclass.py`): for all reduced forms of discriminant −tp, t ∈ {3, 7, 11, 15, 19, 23, 31,
35, 39, 43} and p ∈ {5, …, 61}, 2.83·10⁶ represented m coprime to tp, 3.97·10⁵ of them ≡ ±1 (mod t): 0 violations
of (m/t) = (m/p) or of (m/p) = ±1. This covers non-principal classes too, unlike the author's check of random
norms.

**D10 (MAJOR as a ledger statement; the memo text is partly careful).** The brief asks whether this is a theorem
about *all* ray-class mechanisms or only about Hecke-L/Eisenstein inputs. **It is only the latter, plus a
reduction of the target.** What is proved is:
(a) the truth value of the hypercube event at fixed (t, p) is a function of the residues mod t of the prime
factors of N (with exponents), so the *target statement* contains no ray-class information beyond N; and
(b) any *linear character detector* of the event (Fourier expansion on G, Hecke L-functions, theta series,
Chebotarev densities of the event) uses only χ∘N, i.e. Dirichlet data mod t and mod 4tp.
It does **not** show that ray-class arithmetic is useless as a *proof method* when p varies. A Chebotarev or
equidistribution argument in the ray class fields of the varying K_p = ℚ(√−tp), used to force a *family* of N's
to have prime factors in prescribed classes, is not a detector of the event at fixed (t, p) and is untouched by
item 2. Iteration 1 dismisses this only by "no common field, B6/H-A", which is a barrier citation, not a proof.
Iteration 2 ("class ⇒ norm … WR Prop 10.3 shows is genus-shadow only") **cites the wrong result**. Prop 10.3 is
about classes in Cl(O), where the norm mod ℓ is a class invariant only up to squares. In the ray class group G the
norm mod t *is* a class invariant (that is Remark 10.4's whole point), so a "class ⇒ norm" mechanism in G is not
genus-shadow-only. It is useless only because, by (a), anything it proves about the event can be pushed forward
along N to a statement about residues mod t. That push-forward argument is the correct reason, and the memo
should give it.
Repair: (1) state the theorem as "(a) + (b) at fixed (t, p)"; (2) replace the Prop 10.3 citation in iteration 2 by
the push-forward argument; (3) in DISCOVERIES/ledger, record Remark 10.4's escape as "closed for fixed-(t, p)
character/L-function/Eisenstein inputs; varying-p ray-class Chebotarev arguments remain classified under
B6/H-A (barrier, not theorem)". "Promise 0/5" is acceptable as an Assessment.
Minor: T1 bullet "at p = k²" is outside the memo's own hypothesis (p prime). Say "at n = k² in GI Prop 4.1".
