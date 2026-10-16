# R261 — hostile review of CAP_BOUNDED.md (O250, checkpoint 1)

Reviewer: R261 side agent (branch side-agent/review-cap-bounded, merged side-agent/cap-bounded at 6c42e1dc).
From-scratch scripts: `scripts/review_r261_*.py` (no reuse of `scripts/z22_*`).
Self-test of the checker: `review_r261_selftest.py 400 23 2` — least Lemma-3.1 cap via residue DP vs. direct
enumeration of all D₁ = ∏ s^{c_s} (c_s ∈ [0, 2b_s + 2E + 2]) checked against Def 1.1 with exact rationals:
221 (p, m) pairs, 0 mismatches.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 / Cor 1.2 | SOUND |
| Thm 1.3 (+ explicit examples) | SOUND (CONDITIONAL on Dickson, as labelled) |

## 1. Lemma 1.1, Cor 1.2, Thm 1.3

**Lemma 1.1 — SOUND.** Re-derived: s | K, s | m ⇒ s | 4K − m = p; reciprocity with (m−1)/2 odd gives
(s/m) = (−m/s) = (p/s) = (s/p). (b): 8 | p + m ⇒ m ≡ −p (8), and (2/·) depends on ±(mod 8) only. (c), (d) fine.
Negative exponents are harmless (Jacobi symbol of an inverse = symbol). **Cor 1.2 — SOUND**, including δ_p via
(p/m) = (m/p); for K odd δ₂ = 0 is forced by CAP_DOWN Lemma 3.1 (c₂ ≤ 2v₂(N) = 0), so (b)'s hypothesis is never needed.

**Thm 1.3 — SOUND (CONDITIONAL on Dickson).** Re-derived every step:
* v_ℓ(L) = v_ℓ(Λ) + 1 (+4 at ℓ = 2) and v_ℓ(m+1) ≤ v_ℓ(Λ), so ℓ | L_m for every ℓ ≤ M+1 and v₂(L_m) ≥ 5; m | Λ and
  gcd(m, m+1) = 1 ⇒ m | L_m ⇒ R_m ≡ 1 (mod 4m). 8ℓ | L ⇒ (ℓ/p) = 1 for all ℓ ≤ M+1 (incl. ℓ = 2).
* Admissibility: forms ≡ 1 (mod ℓ) for ℓ ≤ M+1; for ℓ > M+1 the leading coefficients are units, at most
  1 + ⌊(M+1)/4⌋ < ℓ roots. Forms distinct. OK.
* (R_m/p) = (p/R_m) = (−m/R_m) = (m/R_m) = (R_m/m) = (1/m) = 1, using p = (m+1)(R_m−1)+1 ≡ −m (mod R_m). OK.
* (m/p) = 1 since all prime factors of m are ≤ M. So every generator in Cor 1.2 has symbol +1 ⇒ no certificate.
* Reduction "every ES^{(y)} solution with p ∤ x has x > (p+M)/4": 4/p > 1/x forces 4x > p, m = 4x − p ≡ 3 (4),
  gcd(m, p) = gcd(x, p) = 1, and CAP_DOWN Lemma 3.1 is the complete list. OK. (Solutions with p | x but p ∤ y are
  covered by swapping x ↔ y, since both are integers in ES^{(y,e)}; only "p divides both integer coordinates"
  (Type I in both) escapes — the stated scope p ∤ x is if anything slightly conservative.)

*Explicit examples — independently CONFIRMED* (`review_r261_windows.py p M 20`; cap ≤ 20 saturates the residue sets
since λ(m)/2 ≤ 9 for m ≤ 19, so "None" = no certificate at any cap):
* M = 11: p = 807 330 585 601, 1 482 496 646 401, 2 412 770 976 001 — all prime (SymPy), ≡ 1 (8); windows 3, 7, 11:
  K_m = ((m+1)/4)·R_m with R_m prime, every generator symbol (s/p) = +1, (m/p) = +1, no certificate.
* M = 19: p = 4 714 845 095 999 745 907 201, 11 787 094 675 874 034 316 801 (BPSW probable primes; R_m likewise —
  SymPy isprime/factorint, i.e. probable-prime status only, as the author says); windows 3, 7, 11, 15, 19 all dead.
  Note: these are probable primes, so the M = 19 check is EVIDENCE-grade; Thm 1.3 does not depend on them.
* Least forced window (least prime q ≡ 3 (4) with (q/p) = −1) re-computed: 19, 23, 31 (M = 11) and 47, 47 (M = 19)
  — as claimed. Control re-run from scratch (`review_r261_control.py 11 300`, own L = 16·lcm(1..12)·∏_{ℓ≤12} ℓ =
  1 024 531 200, own cap checker): **284/300** control primes have a live window ≤ 11 — identical to the author's figure.

Remark (3) of §1 is correctly scoped (no density claim). Remark (1)'s "for these p the window picture is literally that
of n = 1" is a slogan (n = 1 is not prime / gcd conditions differ) — harmless.

## 2. Prop 2.1, Cor 2.2, Prop 2.3

**Prop 2.1 — SOUND.** Re-derived: p ≡ 4K = 2^{t+2}K′ (mod m) ⇒ uniform value ≡ 2^{a−j(t+2)}p^{j+ε}. Admissible j:
j ∈ {−1,0,1}; j ≥ 3 odd always ((j−1)b_s even); j ≥ 2 even iff all b_s even; j ≤ −2 never (no negative overflow).
I enumerated all (j, ε, a) cases by hand for (a)–(d) and recover exactly the stated lists, including the ranges
c ∈ [1, 2t+2] for 2^c + 1 (from j = 0, |a| ≤ t and from (j, ε) = (±1, ∓1)) and p + 2^c, and p² + 2^c (c ∈ [2, 2t+2];
even c excluded only because then N is a sum of two coprime squares — so the "iff" is fine either way).
The odd-square clause of (c) is right (Jacobi (K^j p^ε/m) = +1 ≠ (−1/m)).
*From-scratch brute force* (`review_r261_uniform.py 6000 2000 9`): for all primes p ≡ 1 (4) < 6000 and all windows
m ≡ 3 (4) ≤ 2000, existence of a uniform certificate (cap 0 / cap ≥ 1 split, j ≤ 9) computed directly vs. the lists
(a)–(d): **191 182 pairs, 0 mismatches.** Example (d) p = 13, m = 387, (δ₂, δ₅, δ_p) = (−1, 4, 1): rebuilt solution
x = 100, y = 13 650, z = 84/25 passes Def 1.1 at e = 1, not at e = 0. Example 4/17 = 1/5 + 1/170 + 1/34 confirmed.
Degenerate case K′ = 1 (K a power of 2) is not mentioned: then j is vacuous and (d) should be read with the j ≤ 1 values
only (MINOR, D4).

**Cor 2.2 — residue computation SOUND; the verbal conclusions are mis-labelled/over-broad (D2, D3).**
Residues mod 8 re-derived: every p-dependent N ≡ 1 (4) except 2p + 1, p + 2 ≡ 3 (8), which occur only for t ≥ 1,
i.e. m ≡ 7 (8). Correct. But:
* "p mod 8 alone forces no uniform certificate" must be read per N-family / per bounded j. Literally it conflicts with
  Prop 2.3: for EVERY prime p ≡ 1 (8) there are (Dirichlet, CRT on q mod 8p) primes q ≡ 3 (8) with (q/p) = −1, and at
  each such q a uniform certificate exists (j = o). So every p ≡ 1 (8) HAS uniform certificates; what is not forced is a
  uniform certificate of bounded j (bounded cap). (D2)
* The R-O250 paragraph "congruence forcing happens only via fixed small primes of N … beyond any finite menu the event
  is Landau-type" sits inside the ∎ of a PROVED corollary but is an Assessment (no definition of "congruence-forced",
  no proof of the dichotomy). E.g. N = 2p + 1 ≡ 3 (4) always has a prime factor ≡ 3 (4) with NO fixed prime involved; it
  is excluded only because the window must be ≡ 7 (8) — i.e. the dichotomy needs the mod-8 refinement to be even
  plausible. (D3)

**Prop 2.3 — SOUND.** Re-derived: K ≡ p/4 (mod q), (K/q) = (p/q) = (q/p) = −1, 2-part of F_q^* is {±1} ⇒ ord K = 2o,
o odd, K^o = −1; δ_s = o·b_s is admissible (o odd) with overflow (o−1)b_s (even), cap (o−1)b_s/2. "Exists iff
(q/p) = −1" correct. q | p² − 4p + 16 ⇒ q | p³ + 64 ⇒ o | 3. (U)'s "q ≡ 3 (8)" implicitly carries (q/p) = −1, which
is automatic from q | p^o + 4^o with o odd — fine.
*From-scratch check* (same script): all p ≡ 1 (8) < 6000, all primes q ≡ 3 (8) < 2000 with (q/p) = −1 (7 395 pairs):
o (odd part of ord_q(p/4)) = least odd k with q | p^k + 4^k; the j = o certificate rebuilt with exact rationals passes
Def 1.1 at exactly cap (o−1)/2·max b_s (and fails at one less when > 0); the exact least cap at q is ≤ that. 0 failures.

## 3. Lemma 3.1 and Thm 3.2

**Lemma 3.1 — SOUND (citation MINOR, D5).** p ≡ 3 (4) and p ≡ 5 (8) classical (checked: 4/p = 1/(2k+2) + 1/(p(k+1))
+ 1/(2p(k+1)) for p = 8k + 5). For p ≡ 1 (8), CAP_DOWN Thm 1.2 has no exclusion and Prop 1.3 gives (q₃ − 3)/4; so
e*(p) > C ⇒ q₃(p) > 4C + 3 ⇒ p ∈ 𝒫(4C+3). Pollack JNT 187 (2018): I read the PDF (sources/). **Theorem 1 as stated
gives only q < p**; the bound q ≤ (p+1)/2 for p ≡ 1 (4) is in its *proof* (q | a ≤ C ≤ (p+1)/2). CAP_DOWN Cor 2.2 says
"his proof"; CAP_BOUNDED Lemma 3.1 says "Thm 1". Harmless — q < p already gives 𝒫(y) ∩ [1, y] = ∅ — but cite
correctly. From scratch: q₃(p) ≤ (p+1)/2 for all p ≡ 1 (4) < 10⁶ (max q₃/p = 0.6 at p = 5) (`review_r261_sieve.py`).

**Thm 3.2 — SOUND (PROVED relative to the cited inputs; label MINOR D5).** Re-derived line by line:
* *Display.* For p ∈ 𝒫(y), p > y: every n ∈ 𝒜(N, y) is a product of residues and p ∤ n, so 𝒜 avoids ω(p) = (p+1)/2
  classes. Montgomery's arithmetic large sieve (any ω(ℓ) < ℓ; Montgomery–Vaughan constant N − 1 + Q² ≤ N + Q²) with
  L ≥ Σ_{p ∈ 𝒫(y) ∩ (y, Q]} (p+1)/(p−1) ≥ #(𝒫(y) ∩ (y, Q]) gives the display; p ≤ y excluded by Lemma 3.1. The
  exceptional set is defined with all q ≡ 3 (4), q ≤ y (not only primes in a sieve range) and p ≡ 1 (8) — consistent
  with Lemma 3.1's inclusion. OK. (Small-parameter sanity check of the display: trivially satisfied, as expected.)
* *(a).* e* > y/4 ⇒ q₃ > y + 3 ⇒ p ∈ 𝒫(y). k = π(y; 4, 3) ≥ y/(3 log y), r = ⌊log N/log y⌋, |𝒜| ≥ C(k, r) ≥ (k/r)^r;
  k/r ≥ y/(3 log N) = (log X)^{A−1}/6 = (log N)^{A−1}/(3·2^A) ✓; r log(k/r) = (1 − 1/A − o(1)) log N, the floor costing a
  factor ≤ y = X^{o(1)}. Count ≤ 2X²/X^{2−2/A−o(1)} = X^{2/A+o(1)} ✓. Needs A > 1 (k/r → ∞); non-trivial only for A > 2,
  as stated. o(1) depends on A only — uniformity fine.
* *(b).* Z := N^{1/r} = X^{2/r} ≤ X^{ε/2} = y since r ≥ 4/ε ✓; distinct r-subsets of the ≍ Z/log Z primes ≡ 3 (4) in
  (Z/2, Z] give distinct products ≤ N, so |𝒜| ≫_ε N/(log N)^r ✓; count ≪_ε (log X)^r. p ∈ (X^{1/2}, X] with
  e*(p) > p^ε ⇒ q₃(p) > 4p^ε + 3 > X^{ε/2} ✓; the sum over scales X^{2^{−k}} is a convergent geometric series in
  (log X)^r, and scales below the PNT threshold contribute O_ε(1) in total (disjoint ranges) ✓. Note: in (b) p > X^{1/2}
  ≥ y automatically for ε ≤ 1, so Pollack is not even needed there; it is needed only for the display as stated.
* *Comparison with CAP_INTERPOLATION Rem 3.2(b)*: that is a reviewer sketch (power saving for #{p ≤ N : ES^{(y,e)}(p)
  fails} once e ≥ (log N)^{1+ε}, via ω(ℓ) ≥ e + 1 from the class family 9^j at ℓ ≡ 11 (12)); Thm 3.2(a) needs A > 2 for a
  power saving. The author's Remark (3) ("weaker in range but complete, explicit Chebotarev exceptional set") is
  accurate; no contradiction between the two. Rem 3.2(a) (e = ∞: N^{3/4} log²N) is consistent with Thm 3.2 too.
* Remark (2)'s "GRH-quality" is loose: GRH gives (log p)^{2+ε}, Thm 3.2(a) gives a power saving only for exponent
  A > 2 — "GRH-quality up to the exponent" would be precise (MINOR, D6). Remark (4): density 2^{−π(4C+3;4,3)} of
  𝒫(4C+3) among p ≡ 1 (8) correct (reciprocity: (q/p) = (p/q), independent conditions on p mod q).
