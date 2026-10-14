# R209 — hostile review #1 of PHASE_DIAGRAM.md (O204, checkpoint 1)

Reviewer worktree branch `side-agent/review-phase-diagram-2`, merged `side-agent/phase-diagram` at 0e608b96.
From-scratch scripts: `scripts/review_pd_wall.py`, `scripts/review_pd_family.py` (+ further `review_pd_*` below).
None of the author's `pd_*` scripts were used or imported. **ES is not solved; nothing below changes that.**

## Summary verdicts

| Claim | Verdict |
|---|---|
| Prop 1.1 normal form k(4ab − n) = b + aQ₁²; D-face | SOUND (minor notation, m1–m2) |
| Thm 2.1(a) k-wall Q₁ ≤ (16k³n+1)/(4k−1), sharpness families | SOUND |
| Thm 2.1(b) / band √(Q₁/6n) ≤ k < Q₁²/2; "both slicings finite" | SOUND |
| Consequence: is ES^{(y,1)} / ES^{[2]} a FINITE search? | NO — R200 M1 stands (see §2 below; wording m3) |
| Prop 3.1(a) k = 1 slice of ES^{(y)} non-empty (gcd(n,15) = 1) | SOUND (hypothesis can be weakened to 3 ∤ n, m4) |
| Prop 3.1(b), Cor 3.2 (k-direction dichotomy) | SOUND-AFTER-REPAIRS (ES^□ half of Cor 3.2 is unproved as written, M1) |
| §3 EVIDENCE (pd_k1, pd_k1s) | SOUND — reproduced exactly from scratch |
| Prop 4.1 (one axis, θ = 1/(2e+2)) | SOUND (algebra); θ-reading and citations SOUND-AFTER-REPAIRS (m6, m7) |
| (rest: in progress) | |

## Claim-by-claim

### Prop 1.1 — SOUND
Re-derived by hand: g = 4ak − 1, Q = aQ₁, gcd(Q₁, k) = 1 ⇒ Q₀ = gcd(aQ₁, ak) = a. From g·m = n + 4a²Q₁² and
g ≡ −1 (mod 4a): m + n ≡ 0 (mod 4a), b := (m+n)/(4a) ∈ ℤ_{>0}, and 4akm = m + n + 4a²Q₁² = 4ab + 4a²Q₁², i.e.
km = b + aQ₁² with m = 4ab − n. Converse as in the document (expansion checked). Variant translations: y = nak and
gcd(Q₁, nk) = 1, so rad Q₁ | y ⟺ rad Q₁ | a, Q₁² | y² ⟺ Q₁ | a; ES^{(y,1)} = (Q₁ squarefree, Q₁ | a) by
EXPONENT_CAP Def 1.1. All correct. `review_pd_wall.py A` asserts (1.1) on every shot it finds (348 shots, n ≤ 101,
k ≤ 6, Q₁ ≤ 2W(k)) — found by the DEFINITION (a, Q₁ | a, k, test (4ak−1) | n + 4a²Q₁²), not via the duality.
D-face: gcd(m, n) = gcd(4λtb, n), gcd(m, b) = gcd(n, b), and 4b(b + λt³) ≡ 4b² + nt² (mod m): correct. The two
self-review counterexamples reproduce (`review_pd_family.py`).
Den z = Q₁² is used for all Q although EXPONENT_CAP Prop 1.2 is stated "for Q odd"; my exact-rational check found
den z = Q₁² on every shot including even Q₀ (m2).

### Thm 2.1(a) — SOUND (re-derived; brute force confirms; sharp)
Independent derivation: Q₁ | Q₀ gives g ≡ −1 (mod 4kQ₁) so g ≥ 4kQ₁ − 1; reducing Dg = 4k²n + Q₁² mod Q₁ gives
D ≡ −4k²n (mod Q₁); since gcd(Q₁, 2kn) = 1 (Q₁ | Q, gcd(Q, n) = 1; gcd(Q₁, k) = 1 by definition of Q₀), for
Q₁ > 4k²n the least positive such D is ≥ Q₁ − 4k²n, and (Q₁ − 4k²n)(4kQ₁ − 1) ≤ 4k²n + Q₁² expands to
(4k−1)Q₁² ≤ (16k³n+1)Q₁. Division (4k−1)(4k²n + kn) = 16k³n − kn checks the displayed form; ≤ 6k²n holds for k ≥ 1.
No hidden hypothesis (the only inputs are gcd(Q, n) = 1 and Q₁ | Q₀; D ≥ 1 is automatic).
Brute force (`review_pd_wall.py A 101 6 2.0`, 54 s): searching Q₁ up to **2·W(k)** (author: 1.3·W), odd n ≤ 101,
k ≤ 6: 348 ES^{[2]} shots, all with den z | y², max Q₁/W = 1.0000, no violation. (Same count as the author's
search to 1.3W — consistent with nothing existing in (1.3W, 2W].)
Sharpness (`review_pd_family.py`): (3, 2, 55, g = 439) attains W(2) = 55 exactly (Q₀ = 55, den z = 55²); the family
Q₁ = (16n+1)/3, g = (64n+1)/3, D = (4n+1)/3, Q = Q₁² verified for all 3 333 odd n ≡ 2 (mod 3), n ≤ 20 000
(exact solution, k = 1, Q₀ = Q₁, Q₁ = W(1)). The side family Q₁ = 4n + 3, D = 3 (Q₀ = (4n+3)(n+1)/3) also verified
on the same range. n = 59: W(1) = 315 = 3²·5·7 confirmed. Note "every n ≡ 2 (mod 3)" means odd n, i.e. n ≡ 5 (mod 6)
(n odd is global; harmless).

### Thm 2.1(b) and the band — SOUND
The cited case split of EXPONENT_CAP Thm 2.1 re-checked: kj ≥ 2Q₁² ⇒ D ≥ kj/2 ⇒ Q₀ = (4kn+j)/(4D) ≤ 2n/j + 1/(2k)
≤ (n+1)/2 (j ≥ 4). With Q₁ | Q₀, Q₁ > (n+1)/2 forces kj < 2Q₁², hence even k < 2Q₁²/j ≤ Q₁²/2. Brute force
(`review_pd_wall.py B 61 61 1.0`, 38 s): every odd n ≤ 61, odd Q₁ ≤ 61, ALL k ≤ Q₁² (i.e. twice the claimed band
edge), all divisors g ≡ −1 (mod 4kQ₁) of 4k²n + Q₁²: 172 ES^{[2]} shots, each an exact solution with den z | y²; no
k-wall violation; among Q₁ > (n+1)/2, max k/Q₁² = 0.4360 (attained (29, 126, 17), g = 8567, as the author reports);
no shot with k ≥ Q₁²/2. "Both slicings finite": fixed k ⇒ Q₁ ≤ W(k) and g ≤ 4k²n + Q₁²; fixed Q₁ ⇒ EXPONENT_CAP
Thm 2.1 — correct.

### Consequence: does Thm 2.1 make ES^{(y,1)} a FINITE search? — NO; R200 M1 is not superseded
Thm 2.1 bounds each slice, not the union. Eliminating k with k = (g+1)/(4Q₀) ≤ (g+1)/(4Q₁) in Q₁ ≤ 6k²n gives
Q₁³ ≤ (3/8)n(g+1)², and EXPONENT_CAP Thm 2.1 gives Q₁ ≥ min(√g/(2n), (g/4n)^{1/4}). So for each g the admissible
overflow window is roughly **[(g/4n)^{1/4}, (3n/8)^{1/3}g^{2/3}]**, nonempty for all large g: no a-priori bound on g
in terms of n, so ES^{[2]}(n) and ES^{(y,1)}(n) remain infinite searches (an infinite union of finite slices), exactly
as ES itself (each k-line of ES is one number, but k is unbounded). R200 M1's statement — "bounded e with growing S
is OPEN; the wall only asks rad(Q₁)^e ≳ (r/4n)^{1/4}" — stands. What Thm 2.1 adds to M1 (precise form): in any
large-Q₁ ES^{[2]} shot (Q₁ > (n+1)/2) one also has k < Q₁²/2, i.e. **Q₀ > (g+1)/(2Q₁²)**; so the R200 M1 scenario
"r ≡ −1 (mod 4P), P ≈ r^{1/4}, Q₁ | P" is admissible only with Q₀ ≫ r^{1/2} (Q₀ = gcd(Q, (r+1)/4) must carry a
cofactor λ ≫ r^{1/4} besides Q₁), and Q₁ ≤ ((3n/8)r²)^{1/3}. This narrows, but does not close, M1's open case.
The document itself does not claim global finiteness (Verdict 6 says "a union of finite searches in both
directions"), but the table cell "FINITE" and the ES row "OPEN (finite search, B2/B3)" can be misread (m3).

### Prop 3.1(a) — SOUND (re-derived)
k = 1 slice derived independently: g ≡ 3 (mod 4), g | 4n + Q₁², Q₀ := (g+1)/4, Q := Q₀Q₁ ⇒ 4Q₀ ≡ 1 (mod g) ⇒
4(n + 4Q₀²Q₁²) ≡ 4n + Q₁² ≡ 0 (mod g), so g | n + 4Q²; gcd(Q, K) = Q₀, overflow Q₁, k = 1.
Proof checked against the actual statements of UNIT_ORBIT Lemma 2.2 (needs gcd(a, M) = 1, a ≡ 3 (mod 4), a ≢ 1 mod every
odd ℓ | M — so excluding the extra residue −1 at ℓ | n is indeed free) and FROBENIUS Thm 4.2(a) (Γ_r ⊆ (F_r^*)² from
a ≡ −1 (mod s) and (r−1)/2 odd; index argument + UNIT_ORBIT Lemma 2.3 with k = 4). The changes relative to Thm 4.2 are
correct: (−4n/r) = (−1/r)(n/r) = 1; the unique square root of −4n inside the odd-order group (F_r^*)² = Γ_r gives
Q₁ ∈ ⟨S⟩ with non-negative exponents; ∏S | (r+1)/4 = Q₀; Q₀ prime to n because a_ℓ ≢ −1. The n ≡ 3 (mod 4) case
needs (r/n) = +1 rather than −1 (reciprocity with both ≡ 3 mod 4) — the document's "this is a condition on the Jacobi
symbol (r/n), adjusted at ℓ₀" covers both signs; correct. Residue counting outside {0, ±1}: ℓ ≡ 1 (4): (ℓ−5)/2
residues, (ℓ−1)/2 non-residues; ℓ ≡ 3 (4): (ℓ−3)/2 each — correct; ℓ = 5 leaves only {2, 3} (non-residues), ℓ = 3
leaves nothing. Ineffective (BV/Siegel–Walfisz), inherited — should be stated (m5).

### Prop 3.1(b) — SOUND. Cor 3.2 — SOUND-AFTER-REPAIRS (M1)
(b) is Thm 2.1(a) at k = 1 plus the verified family. Cor 3.2's fixed-Q₁ and fixed-k finiteness, and the ES^{(y)}
infinitude (infinitely many sieved primes r, each giving a distinct g = r, g ≤ 2nQ₁²(n + Q₁²) ⇒ Q₁ → ∞), are correct.
The ES^□ half ("for every odd NON-SQUARE n the k = 1 slice of ES^□ is INFINITE … (resp. Dirichlet)") has no proof
in the document and the cited SYNTHESIS_SPARKS2 Prop 2.2 concerns the fixed-modulus orbit, not the k = 1 slice with
the shot side condition gcd(Q₀, n) = 1. It is true, but needs the argument (see M1).

### §3 EVIDENCE — SOUND (exact reproduction)
`review_pd_k1.py cap 200000 13 17 29 37 97 101 9 25` (GNU `factor` batch, divisor enumeration, every shot re-verified
as an exact solution with den z = Q₁², rad Q₁ | y; 7 s): e ≤ 1 counts 0 / 5 / 6 / 0 / 2 / 13 with maxima 91, 155, 79,
431 — identical; e = 2 bit-length sets and maxima 185 761, 120 409, 152 881, 194 271, 165 649, 192 721 — identical;
n = 9, 25 empty. The n = 13 cap-2 shot (Q₁ = 49, g = 223) confirmed. `review_pd_k1.py three 1000000 40` (9 min):
least-a histogram over primes 5 ≤ p < 10⁶ identical to the document's (0: 59 504 … 21: 1, none unresolved), and
the 332-square control has no hit for any a ≤ 40 (as T1 forces: 4m² + 9^a is a sum of two coprime squares).
Labels (EVIDENCE; "infinitude heuristic only") are appropriate. Higher caps (3–11) also show hits up to 2·10⁵.

### Prop 4.1 — SOUND (algebra); the θ-column needs care (m6, m7)
Re-derived: MR ≡ 1 (mod g), gcd(M, g) = 1, so M^{2e}(4k²n + R^{2e}) ≡ 4k²nM^{2e} + 1 = N_e (mod g); g ≡ −1 (mod 4k)
gives D ≡ −R^{2e} (mod 4k); Prop 1.3's converse (needs gcd(R^e, k) = 1 ✓) gives Q₀ = MR/(4k) = λR; overflow
λR^{e+1}/gcd(λR^{e+1}, λRk) = R^e. M^{e+1} = 4kλM^e = 2λX_e ✓. `review_pd_axis.py 101 6 301 3`: 781 464 equivalence
tests (odd n ≤ 101, k, λ ≤ 6, odd R ≤ 301 prime to kn, e ≤ 3), no failure; 752 resulting shots verified as exact
solutions with Q₀ = λR, overflow R^e, den z = R^{2e}, R | y. Quoted example (n, e, k, λ, R) = (13, 1, 5, 2, 3):
g = 119, N_e/g = 17 479, D = 11 ✓. Numerically log M/log N_e at k = 10⁶, λ = 1 is 0.481 / 0.245 / 0.165 / 0.124 for
e = 0…3 → 1/(2e+2) ✓. The displayed "⟸" omits gcd(λ, n) = 1 (stated in the body; m7). Scope remark (e ≥ 2 is a
sub-family; n = 113 mixed-exponent example re-verified: Q₀ = 15, Q₁ = 75, k = 1, den z = 75²) is correct.
**Citations, checked against the source.** Lenstra, *Divisors in residue classes*, Math. Comp. 42 (1984) 331–340
(scanned copy from cr.yp.to/bib/1984/lenstra.pdf, OCR'd p. 1): main theorem ≤ 11 divisors for s > N^{1/3};
**and, "more generally", for every α > 1/4 a bound c(α) for s ≥ N^α**; "I do not know whether the same result holds
for any positive α". CHN 2008 (abstract, as verified in R200): the same 1/4 threshold with c(α) = O((α − 1/4)^{−3/2})
(improving Lenstra's dependence) and a constructive algorithm. So the 1/4 threshold is Lenstra's; CHN improved the
constant and made it constructive (m6). Both are UPPER bounds on the number of divisors of ONE integer in ONE class;
neither says anything about existence, and neither applies at θ = 1/4 exactly (M ≍ (2λ)^{1/2}(N_e/n)^{1/4}, i.e.
no α > 0 margin; the document says so). For θ < 1/4 no bound is KNOWN (Lenstra's open question) — "no O(1) bound"
in the §4 table should read "no bound known".

## Numbered defects

**M1 (MAJOR) — Cor 3.2 / Verdict 3 / §6 table row ES^□: the ES^□ k = 1 infinitude is asserted, not proved.**
Location: Cor 3.2 "(resp. Dirichlet)"; Verdict 3 "The k = 1 slice is infinite for ES^□ … (non-square n)". The shot
convention needs gcd(Q₀, n) = 1, i.e. g ≢ −1 (mod ℓ) for ℓ | n, in addition to (−4n/g) = 1, and for ℓ = 3 | n the
document's own Prop 3.1 shows the class constraints can collide. Repair (it is true; two lines): choose a prime
g ≡ 3 (mod 4) by Dirichlet in a class mod 4·rad(n) with g ≢ 0, −1 (mod ℓ) for all ℓ | n and (n/g) = −1. Possible for
every non-square n: at ℓ = 3 the only allowed class is g ≡ 1 (a residue), at ℓ = 5 both characters remain, so adjust
the character at an odd-exponent prime ℓ₀ ≥ 5 if one exists; if 3 is the only odd-exponent prime then n = 3m² ≡ 3
(mod 4) and the needed (g/n) = (g/3) = +1 is exactly g ≡ 1 (mod 3). Then −4n ≡ Q₁² (mod g) has a root, which can be
taken odd and prime to n (CRT shift by multiples of g), and Q₀ = (g+1)/4 is prime to n. Write this in Cor 3.2.

**m1 (MINOR) — §0 (Y2) notation and congruence.** "D = 7" there is the cofactor m = (n+4Q²)/g of §1, not the duality
cofactor D of Prop 1.3 (for n = 13, Q = 25, g = 359: k = 18, D = (4k²n + Q₁²)/g = 47). Also the λ = 1, j = b = 1
test is "64 + n³ has a divisor m ≡ −n (mod 4) with t = (m+n)/4 odd and the gcd side conditions", which is
"≡ 3 (mod 4)" only for n ≡ 1 (mod 4). Repair: rename (m = 7) and state the congruence as ≡ −n (mod 4) plus side
conditions.

**m2 (MINOR) — §1 / §2 check, den z = Q₁².** EXPONENT_CAP Prop 1.2 is stated for Q odd; Prop 1.1 and the checks use it
for every Q (Q₀ may be even). True on every shot I tested, and the proof of Prop 1.2 does not use parity of Q₀, but
say so. The qualifier "(when gcd(Q₀, n) = 1)" in the §2 check is vacuous under the shot convention gcd(Q, n) = 1.

**m4 (MINOR) — Prop 3.1(a): hypothesis gcd(n, 15) = 1 can be weakened to 3 ∤ n.** At ℓ = 5 | n the forced class
a₅ ∈ {2, 3} is a non-residue; if 5 has even exponent it does not affect the Jacobi symbol, if another odd-exponent
ℓ₀ ≥ 7 exists adjust there, and if 5 is the only odd-exponent prime then n = 5m² ≡ 1 (mod 4) and the required
(r/n) = −1 is exactly a₅ ∈ {2, 3}. Only ℓ = 3 is a genuine obstruction for this proof (then g ≡ 1 (mod 3) is forced,
outside Lemma 2.2). Optional repair (the stated theorem is correct as is); update the † footnote of the §6 table.

**m6 (MINOR) — §4 table and Verdict 4: attribution of the 1/4 threshold.** "θ = 1/4 — exactly the Coppersmith–
Howgrave-Graham–Nagaraj threshold" / "e = 2 … below CHN's range: no O(1) bound": Lenstra 1984 already proves the
bound c(α) for every α > 1/4 (CHN: O((α − ¼)^{−3/2}) and constructive). Repair: "the Lenstra (1984) / CHN (2008)
threshold α > 1/4"; "below it no bound is known (Lenstra's question)". Also say "θ = 1/4 on a log scale: M ≍
(2λ)^{1/2}n^{−1/4}N_e^{1/4}, so no α > 0 margin and neither theorem applies on the e = 1 line".

**m7 (MINOR) — §4 θ is a property of a parametrisation, not of a cell.** For e = 1 with k fixed, λ → ∞, θ → 1/2
(the document's Scope says 1/(2e)); for e = 0, M = 4kλ ranges up to g ≤ N₀, θ ∈ [½, 1). So the §6 table's θ column
(1/4 for ES^{[2]}, 1/2 for ES) is the minimum over the pure-power family, not an invariant. Repair: label the
column "θ_min of the Prop 4.1 family (bounded λ)" and add gcd(λ, n) = 1 to the displayed "⟸" of Prop 4.1.

**m5 (MINOR) — Prop 3.1(a), Cor 3.2: say "ineffective"** (inherited from BV/Siegel–Walfisz, as UNIT_ORBIT Thm 2.4 and
FROBENIUS Thm 4.2 state).

**m3 (MINOR) — §6 table / Verdict 2.** "k-slices FINITE" for ES^{[2]} and "OPEN (finite search, B2/B3)" for ES: add
"(each slice; the cell is an infinite union of slices — Thm 2.1 gives no bound on g in terms of n; R200 M1's
growing-S case remains open, narrowed to Q₀ > (g+1)/(2Q₁²))". Verdict 2's "solutions live in a band of slopes ½…2 in
log coordinates" is right for Q₁ > (n+1)/2 only — add that qualifier.
