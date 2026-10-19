# R288 — hostile review #1 of the hardened 3/4 note (C2, O278)

Reviewer: side agent R288 (branch `side-agent/review-threequarter-1`).
Object: `paper/es-threequarter-note.tex` at author commit `5e418734`
(C2, 874 lines; compiled numbering: Thm 1.1, Rem 1.2, Lem 2.1–2.2, Lem
3.1–3.2, Lem 4.1, Thm 4.2, Cor 4.3, Thm 5.1, Lem 6.1, Lem 7.1, Thm 7.2,
§8, Rem 9.1–9.3). Changelog M1–M14: `reviews/agent-reports/AGENT_REPORT_O278.md`.

Method. Every lemma on the load-bearing route was re-derived by hand
*before* reading the earlier reviews or the author's report §2. Two
from-scratch scripts (the author's `c2_threequarter_check.py` was not
read): `scripts/review_r288_toy_crt.py` (log `reviews/r288/toy_crt.log`)
and `scripts/review_r288_arith.py` (log `reviews/r288/arith.log`); both
ALL PASS. Shiu Thm 1 was checked against the scan `sources/shiu-1980.pdf`
(own OCR of pp. 161–163). ET and PW were checked against the local PDFs/text;
Bloom–Elsholtz against arXiv:2210.04496 (downloaded); a quick independent web
search was done for later improvements.

Repairs applied: none (all defects are MINOR wording/labelling; the author
was active minutes before this review, so repairs are left to the author).

## Overall verdict

**SOUND.** I found no FATAL or MAJOR defect. The headline claim
E(N) ≪ N exp(−c (log N)^{3/4}) (Theorem 1.1, κ = 1/480 fixed, constants
absolute and ineffective) follows from the stated inputs (Montgomery–Vaughan
BT, Bombieri–Vinogradov, Shiu Thm 1) by the argument as written. All
constants are independent of N, of the fibre c, of the subfamily J and of
the moment order m. The label "Internally proved; not externally
refereed" is honest. There are 7 MINOR defects (below), none of which
touches the proof.

## Summary verdicts

| # | claim | verdict |
|---|---|---|
| 1 | Lemma 2.1 (multiplier identity) | SOUND |
| 2 | Lemma 2.2 (distinctness, CRT independence, fibre activity) | SOUND |
| 3 | Analytic inputs (8) BT, (9) BV, (10) Shiu, as stated in sources | SOUND (MINOR m4) |
| 4 | Lemma 3.1 (lattice sums) | SOUND |
| 5 | Lemma 3.2 (multiplier harmonic sum) | SOUND |
| 6 | Lemma 4.1 (weighted second incidence moment) | SOUND |
| 7 | Theorem 4.2 (supply, uniform in c and J) | SOUND |
| 8 | Corollary 4.3 (fibre masses; f_c = f_{c;J_c}) | SOUND |
| 9 | Theorem 5.1 (factorial moments, base independent of m) | SOUND |
| 10 | Lemma 6.1 (conditioned void) | SOUND |
| 11 | Lemma 7.1 + Theorem 7.2 (Bonferroni, ledger, integer count) | SOUND |
| 12 | §8 primes + Rankin ⇒ Theorem 1.1 | SOUND |
| 13 | Choice of scales / exponent 3/4 | SOUND |
| 14 | Changes M1–M14 | SOUND (no change alters the logic beyond what is re-verified here) |
| 15 | Literature claim "no known improvement of 2/3" | SOUND as a search report |
| 16 | Labels, abstract, remarks | SOUND-AFTER-REPAIRS (MINOR m1, m2, m3, m6) |

## Claim-by-claim notes (own re-derivations)

**1. Lemma 2.1.** Over the denominator nsuvw the numerators are nv, u, s;
nv+u = s·kℓ, so the sum is s(kℓ+1) = 4suvw. s ≥ 1 because nv+u > 0 and
kℓ | nv+u. uvw = (kℓ+1)/4 is coprime to kℓ, so v is invertible. Script A:
501 exact instances with `Fraction`. The attribution to ET Prop 2.7,
bullet 4 ("4abd−1 | b+nc … [82]", [82] = Vaughan) is correct (checked in
local ET PDF).

**2. Lemma 2.2.** (1) u,v,u',v' ∈ (H, z_j], so |uv'−u'v| < z_j² = x_j^{1/3}
< ℓ; hence uv' = u'v, and (u,v) = (u',v') = 1 gives equality of pairs. Then
kℓ ≡ k'ℓ ≡ −1 (mod 4uv), (ℓ,4uv)=1, so k ≡ k' (mod 4uv) with
4uv > 4H² > K ≥ k, k' ⇒ k = k'. (2) ℓ > X^{1/2} > K > y, so the ℓ are
coprime to lcm(L_K,P_y); CRT. (3) k | L_K, (v,k)=1: n ≡ −uv^{-1} (mod k) ⇔
k | u+nv ⇔ k | u+cv. Script B: 6672 toy atoms (K=13, H=2, z² < ℓ), 0 same-ℓ
collisions; negative control (H=0, i.e. 4H² > K violated) gives 2012
collisions, so the hypothesis is genuinely used. Script C: exhaustive
enumeration of Z/MZ, M = 1.5·10⁸ (K=9, y=3, ℓ ∈ {67,151,167}, 16 atoms):
at most one atom per ℓ contains n; activity ⇔ k | u+cv in all 30 fibres
inside S_y = 1; P(H=0 | c,S) = Π(1−f_c/ℓ) to 1e−16.

**3. Analytic inputs.**
* BT (8) is exactly Montgomery–Vaughan Thm 2 (x arbitrary, q < Y). The
  simplification to 4x/(φ(q) log x) for q ≤ 4x^{1/3} needs
  (2/3)log x − log 4 ≥ (1/2) log x, i.e. x ≥ 4⁶ = 4096; fine since x ≥ X^{1/2}.
* BV (9): standard π/li two-endpoint corollary of the ψ-form; the
  moduli used (≤ 4x^{1/3}) are far below the level. Ineffective, as stated.
* Shiu: the scan says f ∈ M ((i) f(p^l) ≤ A_1^l; (ii) f(n) ≤ A_2(ε)n^ε),
  0 < α, β < 1/2, (1.1) 0 < a < k, (a,k) = 1, and (2.1)
  Σ_{x−y<n≤x, n≡a (k)} f(n) ≪ y/(φ(k) log x) · exp(Σ_{p≤x, p∤k} f(p)/p)
  "as x → ∞, uniformly in a, k and y provided k < y^{1−α}, x^β < y ≤ x".
  (1.1) excludes k = 1, as the note says. The application: F = 2^ω·id/φ,
  F(p^a) = 2p/(p−1) ≤ 4, F(n) ≤ 4^{ω(n)} ≪_ε n^ε ✓; boxes (U, 21U/20],
  Y = U/20, V = 21U/20, q ≤ K² ≤ U^{1/5} < Y^{3/4}, V^{1/4} < Y ✓. See m4
  for a wording point (the "as x → ∞" threshold and dependence on f).

**4. Lemma 3.1.** Re-derived. (13): progression sum Λ'/k + O(1/H');
coprime sum by Möbius over e | k: φ(k)Λ'/k + O(τ(k)/H'). Summing the u-sum
over v adds O(Λ'/H'), absorbed in O(Λ'τ(k)/H'). Möbius over d = (u,v):
d is coprime to k (d | v, (v,k)=1), and du' ≡ −c dv' ⇔ u' ≡ −cv' (mod k) ✓;
d ≤ H uses H/d ≥ 1 ✓; d > H tail ≪ (log z)²/H ≤ 4Λ²/H ✓. Main coefficient
Π_{p∤k}(1−p^{−2}) − O(1/H) ≥ 6/π² − O(1/H) > 1/4. Relative error
≪ kτ(k)²/H ≤ 4K²/K^{10} ✓. Upper bound: m/φ(m) = Σ_{d|m} μ²(d)/φ(d)
(script 8'' exact for m < 5000), d | u with u reduced mod k ⇒ (d,k) = 1 ✓,
tails ✓, secondary terms ≤ main since Λ ≥ log H = 10 log K and
φ(k)/k ≥ (2k)^{−1/2} ✓. Toy evidence (H = 54, z = H², k ≤ 105, all
reduced c): lower ratio ≥ 0.606, upper ratio ≤ 1.51.

**5. Lemma 3.2.** φ(k)/k² = k^{-1}Σ_{d|k} μ(d)/d; k = dm ≡ 1 (4) forces d
odd and fixes m mod 4; inner sum (1/4)log(K/d) + O(1); Σ_{d odd} μ(d)/d² =
8/π² (script 4': 0.810569) ✓; Σ μ(d) log d/d² converges ✓. Script 4:
h(K) − (2/π²)log K → 0.7548. Removal bound (15) exact for all K ≤ 2·10⁴,
all p (max ratio 0.44).

**6. Lemma 4.1.** Re-derived. For coprime u,v, φ(4uv) ≥ 2φ(u)φ(v) (script
1) and 2^{ω(uv)} = 2^{ω(u)}2^{ω(v)}, so each coprime term is ≤ ½F(u)F(v)/(uv);
dropping (u,v)=1 afterwards only enlarges a nonnegative sum ✓. r² expands
to Σ_{k,k'} 1[[k,k'] | u+cv]; (c,d)=1 since d | L_J ✓; for coprime u,v this
forces (v,d)=1, so the residue −cv mod d is reduced for every v kept ✓.
Shiu in boxes: Σ_{p≤V} 2/(p−1) = 2 log log V + O(1);
exp(−Σ_{p|d} 2/(p−1)) ≤ (φ(d)/d)² (exact, from log(1−1/p) ≥ −1/(p−1);
script 2 for d ≤ 2·10⁵, equality only at d = 1) ✓. Box sum
≪ log U·φ(d)/d², O(log z) boxes ✓; d = 1 by F = 1*h, h(p) = (p+1)/(p−1),
h(p^a) = 0 (a ≥ 2) ✓. Pair sum ≤ Σ_g g^{-1}(Σ_{a ≤ K/g} 1/a)² ≪ (1+log K)³
✓ (script 5: ratio 0.137, 0.122, 0.112 for K = 50, 200, 800).

**7. Theorem 4.2.** Re-derived. Upper: BT + φ(4uv) ≥ 2φ(u)φ(v) + (12)
give ≪ (x/log x) h(J)(log z)² per block, ≪ t h(J) after dividing by x,
O(t) blocks ⇒ ≪ t² h(J). Lower: main term ≥ x Λ² h(J)/(16 log 2x) ≫ x t h(J)
(Λ ≥ log x/12). Error: triples with fixed coprime (u,v) number exactly
r_J(u,v;c) (the condition (v,k)=1 is automatic, as above); #ordered coprime
(u,v) with uv = m is 2^{ω(m)} (script 8'' exact); W(q)² ≤ 2^{ω(q/4)}Σr²;
E*(q) ≪ x/(φ(q) log x) by BT (also bounds the li main term);
Σ W²E* ≪ x t^6; Cauchy–Schwarz with BV (R = 26, log x ≥ t/2) gives
≪ x t^{−10} = o(x t h(J)) as h(J) ≥ 1 ✓. **Uniformity**: the only c- or
J-dependence is through r_J, controlled by Lemma 4.1 uniformly, and through
the residue, controlled by E* = max over reduced residues. So the bound is
genuinely uniform over data-dependent (c, J). No constant depends on c, J, x.

**8. Corollary 4.3.** Both inclusions re-derived: an active atom has
k | u+cv and (u,k) = 1 ⇒ (c,k) = 1 ⇒ k ∈ J_c, and (v,k)=1 so
(u,v) ∈ S(k,c;H,z_j); conversely a triple in f_{c;J_c} satisfies all of
(4) ((uv,k)=1 from (v,k)=1 and u ≡ −cv) ✓. (c, L_{J_c}) = 1 by definition,
1 ∈ J_c ✓. Upper bound A_h t² h(K(K)) ≤ C_u t³ with C_u = C_u(κ) ✓.

**9. Theorem 5.1.** In each fibre (and on S_y = 1, which is independent of
the ℓ-coordinates), H_X = Σ_ℓ I_ℓ with independent I_ℓ ~ Bernoulli(p_ℓ)
(this identity is pointwise, since at most one atom per ℓ contains n).
(Σ I_ℓ)_m = Σ over ordered distinct m-tuples of Π I ⇒ E = m!·e_m(p) ≤ μ_c^m.
Script C: exact agreement m ≤ 3 in all fibres. The base C_u t³ does not
depend on m, and the bound is used up to m = r+1 ≍ t³ — no hidden
m-dependence. ✓

**10. Lemma 6.1.** Re-derived. On S_y = 1, p ∤ c for p ≤ y with p | L_K, so
every k ∉ J_c has a prime factor p ∈ (y, K], p | L_K, p | c; union bound +
(15) give h(J_c) ≥ h(K(K)) − (1+log K)Z(c) ≥ (a_0 − 2Z)log K ✓. The p | c
events (p > y) are independent with probability 1/p conditionally on
S_y = 1 ✓; E e^{yZ} = Π(1 + (e^{y/p}−1)/p) ≤ exp((e−1)yΣ_{n>y}n^{−2}) ≤
e^{2(e−1)} < e⁴ (script 8 over y ∈ [2, 2000]) ✓. Constants: η = a_0/4,
a_v = a_h a_0 κ/4 (using log K ≥ κt/2), B_0 = 2a_v/η, all depending only on
κ ✓. P(H=0 | c, S) = Π(1−f_c/ℓ) ≤ e^{−μ_c} ✓. Total ≤ e^{−a_v t³} +
e^{4−2a_v t³} ≤ e^{−a_v t³/2} ✓.

**11. Lemma 7.1, Theorem 7.2.** Q_r(h) = (−1)^r C(h−1,r) by Pascal; for
even r this is ≥ 0 and ≤ C(h, r+1) when h ≥ r+1 (script D: r ≤ 30,
h < 120). Mean: E(Q_r | S) ≤ P(H=0|S) + E(H)_{r+1}/(r+1)! ≤ e^{−c_v t³} +
(eC_u t³/(r+1))^{r+1}; with r+1 ≥ D_B t³, D_B log(D_B/(eC_u)) ≥ 2c_v, and
m ↦ m log(m/(eC_u t³)) increasing for m ≥ C_u t³ (derivative
log(m/(C_u t³)) ≥ 0) ⇒ ≤ e^{−2c_v t³} ✓. Expansion: C(H,j) = Σ_{|B|=j}Π 1_{E_A}
pointwise ✓; each product with 1_{d|n} is empty or one class mod
q | 𝓜 ✓; T_abs ≤ 2^{π(y)}(r+1)|A|^r, |A| ≤ K X^{4/3} ✓; log T_abs ≤ C_L t⁴ ✓.
Counting: #{n ≤ N : n ≡ a (q)} = N/q + θ, |θ| ≤ 1 for every q ✓. Script E:
direct Σ_{n≤N} S_y Q_r(H) equals the term-by-term class count exactly, E ν
from the term sum equals exact enumeration over Z/MZ (Fractions), and
|Σ − N·Eν| ≤ T_abs, for r ∈ {0, 2}, N ∈ {10⁴, 123457, 200003}.

**12. §8.** Primes: every non-representable prime p > y has S_y(p) = 1 and
H_X(p) = 0 ⇒ ν_X(p) = 1; ν_X ≥ 0 lets one sum over all n ≤ N ✓.
t = αL^{1/4}, C_L α⁴ ≤ ½ ⇒ ledger ≤ N^{1/2} ✓; X = e^t ≥ X_a for large N ✓.
Order of constants: κ → C_u, a_h → c_v → B → D_B → C_L → α; none depends
on N ✓. Rankin: closure (p | n, p representable ⇒ n representable) ✓;
E(x) ≤ x^{1−δ}Π_{p≤x non-repr}(1−p^{−1+δ})^{−1}; δ < 1/4 so prime powers give
O(Σp^{−3/2}) ✓; partial summation and δs ≤ η_0 s^{3/4} for s ≤ L ✓; the
integral converges ✓. (E_pr(x) ≤ x e^{−c_0(log x)^{3/4}} from the prime case
after shrinking c to absorb C_* ✓.)

**13. Scales.** Saving c_a t³, cost e^{C_L t⁴}: maximise t³ subject to
C_L t⁴ ≤ L/2 ⇒ t ≍ L^{1/4}, saving ≍ L^{3/4}. The t⁴ is forced: r ≍ μ ≍ t³
(Bonferroni degree must exceed e·(mean) by a constant factor) times
log|A| ≍ t per degree. The constraint κ < 1/240 is exactly
K^{20} < X^{1/12} in (3). Sanity check: with k = 1 only (μ ≍ t²) the same
ledger gives t ≍ L^{1/3} and saving L^{2/3} = Vaughan, as the note says.

**14. Changes M1–M14** (diffed against `paper/es-threequarter-note-v1.tex`).
* M1 (no ω-cutoff): every surviving statement (inventory, distinctness,
  Thm 4.2, Cor 4.3) was re-verified above for the uncut family; v1 Cor 5.3
  already proved the same reduction. ✓
* M2 (deleted profile/Euler lemmas, ordered-atom replay): no remaining
  reference; `\ref`/`\eqref` targets all resolve (checked by grep against
  labels and by compiling). Nothing in C2 uses μ_X ≍ t³. ✓
* M3: Thm 4.2 = v1 Thm 5.2 with K fixed to ⌊X^κ⌋ (v1 allowed
  K_0 ≤ K ≤ X^κ); upper half now inline and correct. ✓
* M4: exact identity f_c = f_{c;J_c}, both inclusions ✓ (claim 8).
* M5: e⁴ ✓. M6: exact inequality, correct direction ✓ (script 2).
* M7: y < K (needed: y < K so that Z is over (y,K]; ℓ > K > y for CRT) ✓.
* M8 (+y), M9 (C_0 merged into C_L), M10 (BV sentence), M11
  (attribution) ✓. M12–M14: expository; see m1–m3, m6 below.
  None of M1–M14 changes a proof beyond what is re-verified here.

**15. Literature.** Independent check: ET §1 (local PDF, l. 103–105) quotes
Vaughan's N exp(−c log^{2/3} N); PW Thm 1.3 (local text) is exactly as quoted
(4 ≤ m ≤ (log N)², N/exp(C(log² N/φ(m))^{1/3})); Bloom–Elsholtz (arXiv PDF)
quotes E_{4,3}(N) ≤ N exp(−c(log N)^{2/3}) and Elsholtz's Theorem 3
exponent 1 − 1/(2^{k−1}−1) for m > k ≥ 3; Pomerance's 2026 talk slides
(math.dartmouth.edu/~carlp/esconjfl.pdf) still give Vaughan's
O(N/exp(c(log N)^{2/3})) as the bound. A web search (2025–26 arXiv) found
no improvement. The note's wording ("search report, not a priority claim")
is appropriate.

## Defects

No FATAL, no MAJOR.

**m1 (MINOR, abstract, sentence "Conditionally on n mod lcm(k) … ≪ (log X)³
in every conditional fibre").** (a) "lcm(k)" is undefined notation; (b) the
*upper* bound ≪ t³ uses only Brun–Titchmarsh and Lemma 3.1 (Thm 4.2, upper
half); Bombieri–Vinogradov, Shiu and Cauchy–Schwarz are used for the *lower*
bound. Repair: "Conditionally on n mod L_K (the lcm of the multipliers) the
hits at different primes are independent. Brun–Titchmarsh gives an expected
number of hits ≪ (log X)³ in every fibre, and Bombieri–Vinogradov, Shiu's
theorem and Cauchy–Schwarz give ≫ (log X)³ outside an exponentially rare set
of fibres, after conditioning on no small prime factors."

**m2 (MINOR, Remark 9.3 "numerator m").** The remark states a specific
uniform bound "E_m(N) ≪ N exp{−c(log N)^{3/4} m^{−1/4}} with absolute c" that
the note does not prove, and mixes "for fixed m" with "absolute c". Uniformity
in m would require at least BV/BT in moduli m·uv, the analogue of Lemma 3.2
for k coprime to m, and m-uniform void constants, none of which is checked
here. Repair: either drop the displayed formula, or state "for each fixed
m ≥ 4 the argument should give E_m(N) ≪_m N exp{−c_m(log N)^{3/4}}"
labelled CONDITIONAL/internal and not checked in this note. (A heuristic
count suggests a factor φ(m)^{−1/4} rather than m^{−1/4}; either way it is
not proved here.)

**m3 (MINOR, Remark 1.2, "shows that 3/4 is optimal for the architecture").**
The cited results are internal and unrefereed and were not reviewed in this
review. Repair: "Internal, unrefereed companion work [KA3, SL] claims
(CONDITIONAL on those notes) that 3/4 is optimal …".

**m4 (MINOR, (10) Shiu paraphrase).** Shiu states (2.1) "as x → ∞" with
implied constants depending on f, α, β (not explicitly "only on A_1, A_2").
For the single fixed F used here this is immaterial. Repair: "for
V ≥ V_0(α_s, β_s, F); the implied constant depends only on α_s, β_s and F",
and note that U ≥ H → ∞ puts every box beyond V_0.

**m5 (MINOR, Background, Elsholtz).** Elsholtz's exponent 1 − 1/(2^{k−1}−1)
is stated in BE (Thm 3) for m > k ≥ 3. Repair: add "(for m > k)".

**m6 (MINOR, Thm 7.2 statement).** "c_a, D_B, C_L … depending only on κ and
B": c_a and D_B depend only on κ (through C_u, c_v); only C_L (via 2^{π(y)})
depends on B. Harmless; repair optional (state dependencies precisely, which
also makes the parameter order of §1 visibly acyclic).

**m7 (MINOR, Lemma 3.1 proof, display after "This gives").** The first error
term is written Λτ(k)log z/H; the derivation gives Λτ(k)log H/H (sum of
d/(d²H) over d ≤ H). Since log H ≤ log z this is a valid (looser) bound;
no repair needed beyond optionally writing log H.

## Bottom line

Headline 3/4 claim: **SOUND** as an internally proved result. Recommended
label unchanged: "Internally proved; not externally refereed." The note is in
a state suitable for an external expert; the minor items above are wording.
