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

## Defects

(none yet)
