# R265 — hostile review of O255 (PARITY_AUDIT.md, branch side-agent/parity-audit)

Reviewer: R265 side agent. Reviewed commit: 282afc57. Scripts: `scripts/review_pa_*` (from scratch).
Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim 7 — census EVIDENCE (§5): **SOUND**

Recomputed from scratch in C (`scripts/review_pa_census.c`, log `logs/review_pa_census_1e6.txt`, 5.4 s, 1 core)
and Python (`scripts/review_pa_small.py`), using only the definitions in §0 (not the author's scripts).
All numbers reproduce exactly:
* (a⁴) fails (u ≤ √p + 2, which suffices by the u ↔ B symmetry of 4uBC − u − B = p) at exactly the 9 primes
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321 among the 39 175 primes p ≡ 1 (4) ≤ 10⁶. Independent
  O(p log p) brute force over (u, B) confirms R(409) = R(577) = R(5569) = 0. Least u: median 1, 99th pct 5, max 131
  at p = 427249 (confirmed).
* ES-five u-side, p ≡ 1 (8): 19 552 primes, 0 failures, 17 573 with least u ≤ 2 (89.88 %), median 1, 99th pct 5,
  99.9th pct 11, max 17 at p = 196561. p ≡ 1 (840): 395 primes, 238 at u ≤ 2 (60.25 %). Exactly 3 primes need
  u ≥ n_p.
* Windows (q < 3p; note neither event can hold for q > (p+4)/3 since d ≥ q − 1 and u + v ≤ K_q + 1): sub-event
  fails at 8272 primes, full target −1 event at 2458; max least q for the sub-event 141 971.
* T1 control: 499 odd squares 9 ≤ m² ≤ 10⁶, no (a⁴) hit at u ≤ m + 2.

Minor: "(a) hit" at odd squares (§5 T1 bullet) is undefined for composite n (ψ = Jacobi? the class layer alone?).
State which symbol was used (defect m1).

## Claim 3 — Lemma 2.1 (trial count): **SOUND** (minor sharpening suggested)

Re-derivation. (u, C) ↦ B = (p + u)/(4uC − 1) is a bijection onto solutions; B ≥ 1 ⟺ 4uC − 1 ≤ p + u, which forces
u ≤ (p+1)/3 (the text's "u ≤ p" is harmless). |𝓡| = Σ_{u ≤ (p+1)/3} ⌊(p+u+1)/(4u)⌋ = (p/4) log p + O(p) ✓.
Inner sum Σ_{C ≤ X} 1/(4uC − 1) = (1/(4u))(log X + O(1)), X = (p+u+1)/(4u); summing (1/(4u)) log(p/u) over
u ≤ p/3 gives (log p)²/8 + O(log p) ✓. The Fourier split E(p) is the standard 1[m | n] − 1/m ✓.

From-scratch numerics (`scripts/review_pa_lemma21.py`): R via (u, f) divisor count equals an independent (u, B)
brute force for all 77 primes < 400 and at p = 10007. At p = 10⁴+7, 10⁵+3, 10⁶+3, 10⁷+19 I get M = 10.343, 16.172,
23.329, 31.811 and |𝓡|/((p/4) log p) = 0.922, 0.937, 0.948, 0.955, R = 22, 20, 16 (10⁷+19 not recomputed) — exactly
the author's values. M − (log p)²/8 ≈ −0.04 log p, |𝓡| − (p/4) log p ≈ −0.181 p: consistent with the O-terms.

Minor (m2): the U-version M_U(p) = (log U)(log p)/4 − (log U)²/8 + O(log p) is true but, at the polylog U where it
is used, the O(log p) error (= γ·log p/4 + …) is of the same order as the "main" term up to a factor log log p
(numerically at U = 10 the error is ≈ 0.13 log p against a main term 0.58 log p). Cleaner and sharper:
M_U(p) = (log p/4)·H_U + O((log U)² + 1), |𝓡_U| = (p/4)·H_U + O(U), H_U = Σ_{u≤U} 1/u.
Minor (m3): "restricting u does not shrink 𝓡" — it shrinks it by the factor log U/log p (≍ log log p/log p at
polylog U); the point (still ≍ p, not polylog) is right, the wording "does not shrink" is loose. Also the claim is
parametrisation-dependent: it says the *naive* (u, C) trial set stays of size ≍ p; it is not a theorem that every
complete-sum treatment of (a⁴) at polylog U must face ≍ p trials (Verdict (iii) should say "for the (u,C)/(u,B)
parametrisations", see Claim 8).

## Claim 2 — exact single-p events (§0) and Lemma 0.1: **SOUND**

Re-derived: (tu − 1)(tv − 1) = t(tuv − u − v) + 1 = tp + 1 ✓; min(u,v) ≤ (√(tp+1) + 1)/t ≤ √(p+1) + 1 ✓ (the
bound is decreasing in t); AB ≡ 1 (mod p) gives ψ(A) = ψ(B) so the u ↔ v swap preserves the sign ✓; hence
E_a(p; √p + 2) ⟺ ES-five(p) given (J)9 Thm 4.5 ✓. (a⁴): (4uC − 1)(4BC − 1) = 4Cp + 1 ✓, min(u,B) ≤ (√(4p+1)+1)/4 ✓,
two-variable form R(p) = #{(u,B) : 4uB | p + u + B} ✓, swap form (cofactor of g ≡ −1 (mod 4C) in 4Cp + 1 is again
≡ −1 (mod 4C)) ✓. Window conditions match CAP_POINTWISE Thm 1.1 (i)–(iii) ✓.
Minor (m4): the "class/size layer" of (a) alone is trivially satisfiable (u = 1, A = any divisor of p + 1;
(u−1)(v−1) = p + 1 always has solutions). The text says so only in §5; say it in §0 where the two layers are
introduced, otherwise "two layers" suggests both are obstacles.

## Claim 4 — Lemma 3.2: **SOUND** (two cosmetic remarks)

Re-derived. χ_{−4u} = Kronecker (−4u/·) is a character mod 4u because −4u ≡ 0 (mod 4) is a discriminant, and it is
odd because −4u < 0 ✓. For ℓ | m² + u, ℓ ∤ 2u: (−u/ℓ) = 1 ✓; any f ≡ −1 (mod 4u) is coprime to 4u so all its prime
factors are such ℓ ✓. Prime case: −u ≡ p (mod ℓ) and reciprocity for p ≡ 1 (4) ✓. Free χ-shadow at p ≡ 1 (8) ✓;
p = 13, u = 5 counterexample ✓ ((5/13) = −1, 18 = 2·3², χ_{−20}(3) = +1).
From scratch (`scripts/review_pa_lemma32.py`): no hit for any square m² (m < 300, odd *and even*), u ≤ 60; 92 143
pairs (p ≡ 1 (8) < 4·10⁴, QNR u < 200) all have the required ℓ; 362 counterexamples for p ≡ 5 (8) < 2000, u < 50.
Minor (m5): oddness of m is never used — the lemma holds for every square. Minor (m6): in the prime-case sentence
add "u < p" (needed for ℓ ≠ p, as in the χ-shadow paragraph).

## Claim 6 — Dyachenko 2511.07465 assessment (row E4, §4): **SOUND** (one fairness repair)

Checked against `sources/dyachenko-2511.07465.pdf` (pdftotext). Abstract (l.25) and intro (l.71, 95, 112) cite
"Theorem 10.21"; §10 is "Experimental data [tab.3]" and contains no theorems; the claim is Theorem 9.21 (p. 28) ✓.
9.21(III) defines L = {(u,v) : ub′ + vc′ ≡ 0 (mod g)} with b′ = b/g_b, c′ = c/g_c built from (b, c, δ) satisfying
(I), which already includes (4b − 1)(4c − 1) = 4Pδ + 1 — i.e. a solution is an input ✓. Prop 9.25 is the elementary
"a lattice with diagonal period d′ meets every d′ × d′ box" ✓. The return step (§9.10, l.1550; "Connection with
§7.3", l.1633) needs v with u² − v² = 4A/α, a factorisation of 4A/α in a parity/size class — the divisor event,
not proved ✓. Lemmas/Theorems D.33, D.16 exist (the paper calls them both "Lemma" and "Theorem"; cosmetic).
MINOR (m7): the quotation of §11 is truncated in a way that slightly over-favours the audit: the sentence reads
"is certainly not proven **constructively** in the present work", and the next bullet claims "for any fixed odd
prime P, the existence of a solution is strictly proven". Quote both. Read literally, "for any fixed P" is
"for all P", i.e. ES for P ≡ 1 (4), and is exactly what 9.21(III) does not deliver; the paper is internally
inconsistent rather than conceding. Repair: replace the E4 quote by the two bullets verbatim and add that remark.

