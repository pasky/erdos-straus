# Hostile review R24 of EXCEPTIONAL_TUPLES2.md (O24, branch `side-agent/tc-theta`)

Reviewer branch: `side-agent/review-tuples2`. Status: **in progress (round 1).**
From-scratch scripts: `scripts/review_t2_*.py` (none reuse the author's code).

## Verdicts per claim

| claim | verdict | notes |
|---|---|---|
| Lemma 1.1 | SOUND | re-derived; brute force all ℓ ≤ 3000 (218 primes), 0 failures (`review_t2_forms.py`) |
| Cor 1.2 | SOUND | trivial from (1.1) + distinct primes; brute-forced below |
| Thm 2.1 | SOUND | (pending numeric check) |
| Thm 2.2 | SOUND | exponent bookkeeping re-derived (see §A) |
| Cor 2.3 | SOUND | |
| (1.3) | SOUND | brute force y = 35, 50; N = 50, 300, 3000: S_j = Σ_𝔄 C_T exactly (`review_t2_altsum.py`) |
| Thm 4.1 | SOUND | re-derived line by line (§B); identity Σ(−1)^j e_j^𝔄 = E a(H) verified in exact rationals |
| §5(b) | SOUND | reproduced to all 4 digits (all 25 ratios) by `review_t2_translates.py` (N = 10⁷, y = 1000, same t's) |
| Cor 6.1 | SOUND | re-derived from T1 Thm 3.1 (§C) |
| Prop 7.1 | SOUND (relative to K2 Thm 5.1 / EK machinery) | §D; hypothesis should be N-free (D4) |
| Ass. 3.2, §4 status, Ass. 6.2 | correctly labelled Assessments | data support the deficit direction (§E) |
| §5(a) | SOUND | reproduced exactly (no log-binning) by `review_t2_forced.py`: max Z11/η_K = 9.24·10² (j=8) at (10⁸,1000), 1.84·10⁵ (j=10) at (10⁸,3000) |

## A. Re-derivations

**Lemma 1.1.** D | A², D/A = r/s reduced ⇒ s | A, A = s a′, D = r a′, r | s²a′ ⇒ r | a′
⇒ A = rsm, D = r²m. 4r²m = (4rsm)(r/s) ≡ r/s (mod ℓ), s invertible as s ≤ A < ℓ.
So n ≡ −4D ⇔ ns + r ≡ 0. Form (1,1) gives D = A, −4A = −(ℓ+1) ≡ −1. Correct.
Checked by brute force (bijection onto divisors of A², the equivalence for every
residue n mod ℓ, and −1 ∈ 𝓡(ℓ)) for all 218 primes ℓ ≡ 3 (4), ℓ ≤ 3000.

**Thm 2.1.** (y/2)^{u₀} ≥ N+2 by definition of u₀, and ℓ > y/2 gives Π_U ℓ > N+1 = N·1+1,
so U ∪ V is forced zero whichever forms V uses (V may add more (1,1) primes; that only
enlarges the (1,1) group). Injectivity: U = primes of T in (y/2, y]. Ordered-tuple bound
u₀!·e_{u₀}(q) ≥ Π_{i<u₀}(σ − i·max q), max q < 2/y, and u₀ ≤ σy/4 ⇒ ≥ (σ/2)^{u₀}. Correct.

**Thm 2.2.** log y_K ≍ K^{1/2} (T1 (1.3)); u₀ ≤ 1 + log(N+2)/log(y_K/2) ≍ (log N)^{1−θ/2};
log Z_{u₀} ≥ −u₀ log(2u₀/σ) ≥ −u₀ log(2u₀ log y/c₂) =: −Λ_N ≍ (log N)^{1−θ/2} log log N.
log(1/η_K) = K/e² + log K with K ≍ (log N)^θ. Λ_N + log K ≤ K/(2e²) iff (asymptotically)
θ > 1 − θ/2 ⇔ θ > 2/3. Correct; the threshold is sharp for this construction.
Also u₀ ≤ K (needed so that TC constrains order u₀): 1 − θ/2 < θ. ✓.

**Consistency with T1 Prop 2.4 (asked in brief).** No conflict. Every forced-zero tuple has
Π_{T_φ}ℓ > Ns + r ≥ N + 1, hence Nδ_T < 1: forced zeros are "above modulus N" tuples, and
N·Z_j ≤ #{j-tuples} ≤ (ΣF)^j, which Prop 2.4's termwise bound already absorbs. For θ < 2/3
the same exponent comparison runs the other way (Λ_N ≫ K), so Thm 2.1's lower bound is
≪ η_K there; nothing in O24 contradicts Prop 2.4.

**Cor 2.3.** (1.3) at j = u₀ plus S_{u₀} − Ne_{u₀} ≥ −η_K N. Correct, and correctly labelled
as a *necessary condition*, not a refutation.

**Thm 4.1 (re-derived).** δ_T = P(T ⊆ H) under the CRT hit law; tail |T| > K costs
≤ Σ_{j>K}(eμ/j)^j ≤ e^{−K} for K ≥ e²μ. Admissibility is a per-form condition, so
Σ_{T⊆H,T∈𝔄}(−1)^{|T|} = Π_φ χ_φ(H_φ); χ_φ(G) = 1[G=∅] for admissible G (subset-closed),
|χ_φ| ≤ 2^{|G|} always. An inadmissible group has y^k ≥ Πℓ > N ⇒ k ≥ u₁. P(H = H₀) =
Π(1−p)·Π_{H₀}1/(ℓ(1−p_ℓ)) ≤ Π(1−p)·Π_{H₀}2/ℓ (p_ℓ < ½), so with the 2^{|H|} the weight 4/ℓ is
right. Per (ℓ, φ) at most one pair (fixed representatives), primes of form φ ⊆ {ℓ ≡ −1 (4rs)},
Σ4/ℓ ≤ (4/(3rs))(1+log y) ≤ u₁/2; tail Σ_{k≥u₁}W^k/k! ≤ 2(eW/u₁)^{u₁}; Σ_{(r,s)}(rs)^{−u₁} ≤
ζ(u₁)² ≤ 2. All steps check. Cor 4.2: u₁ ≍ (log N)^{1−θ/2} ≫ log y_K ≍ (log N)^{θ/2} iff θ < 1. ✓

**Brute force (`review_t2_altsum.py`, exact rationals).** Fixed representatives as in the paper
(−1 ↦ (1,1); others: smallest (rs, r)). Results:

| y, N | (i) n with inadmissible hit group | (ii) (1.3) | (iii) Σ(−1)^j e_j^𝔄 = E a(H) | Σ(−1)^j e_j^𝔄 | Π(1−p) | #{f=0}/N |
|---|---|---|---|---|---|---|
| 35, 50 | 0 | ✓ | ✓ | 0.0794 | 0.1191 | 0.180 |
| 50, 300 | 0 | ✓ | ✓ | 0.0775 | 0.0802 | 0.103 |
| 50, 3000 | 0 | ✓ | ✓ | 0.0814 | 0.0802 | 0.0853 |

(i) confirms Cor 1.2 (every inadmissible tuple has C_T = 0). The truncated alternating CRT
sum differs from Π(1−p) with **both signs** at toy scale (ε is not small here: u₁ ≥ 4(1+log y)
fails); Thm 4.1 only claims the upper bound, so no defect. Note the interval avoider count
exceeds the CRT value in all three cases (floor/Kubilius effects of small n), the sign that
TC^alt must control.

Extra (v): the pre-ε inequality of the proof, |E a(H) − P(H=∅)| ≤ Π(1−p)[Π_φ(1+Σ_{k≥u₁}e_k(w_φ)) − 1],
was checked in exact rationals at the three toy points (both signs): holds, with large slack.

**§5(b).** `review_t2_translates.py 1e7 1000 0,1e12,2.718281828e12,3.14159265e13,1e15 12`
reproduces every entry of the §5(b) table. It also gives the avoider ratio
#{f=0}/(NΠ(1−p)) = **1.223 on [1,N]** versus 1.001 / 0.998 / 0.986 / 1.005 on the translates:
the initial-segment effect is an avoider *excess* of 22% at this scale — exactly the
quantity TC^alt bounds, and a reason its factor 2 is not cosmetic (see D3).

## C. Cor 6.1 (re-derived)

T1 Thm 3.1 with Q₀ = Π_{ℓ<ℓ₀}ℓ, R = avoiders mod Q₀ (|R|/Q₀ = Π_{ℓ<ℓ₀}(1−p_ℓ) ≫ 1; p_ℓ(c) = p_ℓ
by CRT), k = 1, L₀ = λ₀ = λ, α = λ^{−1/3}. Terms: 19αλ = 19λ^{2/3}; partial summation with
μ_x ≤ C(log x)² gives Σ p_ℓℓ^{−α} ≤ 2Cα^{−2} = 2Cλ^{2/3} (+ a boundary term e^{−αλ}μ ≤ O(1));
tail e^{−λ^{2/3}}C(A log N)² = O(1) as λ ≥ log N; G = O(log λ), G-terms
O(log²λ + log λ·log log N). Hence log(1/Eν) ≤ C_Aλ^{2/3}. The inversion "saving (log N)^θ
needs λ ≥ c(log N)^{3θ/2}" is correct and, as in T1 Cor 3.3, only binds CRT-main-term
evaluations. p_ℓ ≤ τ(A_ℓ²)/ℓ ≤ 1/4 for ℓ ≥ ℓ₀ is fine. SOUND.

## D. Prop 7.1 (re-derived against K2 Thm 5.1 as written in K2 §§1, 5)

* d-locality: a level-≤λ₀ term has ≤ λ₀/s primes in (e^s, e^{2s}]; an intersection of ≤ k
  classes, each with ≤ r primes in the block, has ≤ kr. So d_i ≤ λ₀/s + kr. ✓
* The block step bound g(d) = d log(C₀(M+4d)/d) + … is increasing **and subadditive**
  (g(d)/d decreasing), which is what actually justifies splitting the cost into the λ₀/s
  part and the kr part; the paper only says "increasing". Minor (D5).
* Above e^{λ₀/2}: K2 uses a *linear* block (ETw Cor 4.3) that exploits 1-locality of
  level-λ terms; order-k terms are not 1-local there, so the replacement by a generic
  dyadic block (one extra block (e^{λ₀/2}, e^{λ₀}], s = λ₀/2, d ≤ 2 + kr) is needed and is
  correct; nothing lives above e^{λ₀} = N^A since all moduli are ≤ N^A. ✓
* kr part: ≤ kr·log(C₀(8K₃s³(log 2s)³ + 4kr)/(kr)) + O(kr) ≤ C kr log log N per block,
  O(log log N) blocks (s from s₁ ≍ λ₀^{1/4−} to λ₀). ✓ Gives C kr (log log N)².
* Reliance: the claim that the level enters K2 Thm 5.1 *only* through d-locality is K2's
  own §1 statement (K2 reviewed SOUND twice). I did not re-audit EK/ETw.

## E. Assessments (3.2, §4 status, 6.2)

Labels are correct. Supporting data the author could cite: at (10⁸, 1000), j = 8, the
pure-(1,1) forced-zero share Z11_8/e_8 = 2.1·10⁻³ and the observed T1 deficit is 0.90%
— same sign, no compensating excess, consistent with Ass. 3.2. Caveat the author should
add: T1 §5(c) found that even the `rand` control fails the TC test at y ≥ 300, so toy-scale
exceedances of η_K (§5(a)) cannot by themselves discriminate ES-structure from noise; §5(a)
is a statement about a deterministic CRT mass, which is fine, but "the multi-form tuples
would have to compensate" (§5(a), last sentence) should be read with that caveat (D6).

## Defects

(none yet)
