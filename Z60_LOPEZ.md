# Z60_LOPEZ — López's single line U_II: no complementarity found between the branches (exchangeable in law, deep tails positively dependent); no p-independent link law; a sharper sign-free sub-target U₇ (verdict: narrowed + sharper target; no mechanism)

**ES is OPEN; López's Conjecture 1, CONJECTURE U_II, (MS-U) and the new CONJECTURE U₇ are open.** Lane LOPEZ of wave z60
(`z52bbriefs/z60_lanes.md` §LOPEZ; rules `z58_lanes.md` "Common rules" + falsifier table; `z53_depth.md` with z53 → z60).
Scripts `scripts/z60_lopez_*`, data `data/z60/lopez/` (≈ 2.5 MB). Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results are internally reviewed only (§8).

Notation (`Z59_SUMMARY.md`, `Z59_CONV2.md`). n odd ≥ 1. **Branch B** = (★) = c = 1 line = López Type B; **branch A** =
a = 1 (∪ b = 1) line = López Type A; U_II(n) ≥ 1 ⟺ A or B has a solution at n. 𝔐 = {1, 121, 169, 289, 361, 529} ⊂
(ℤ/840)^× (= the squares of (ℤ/840)^×). For f ≡ 3 (mod 4): m_f = (f+1)/4, D_f = {a mod f : a | m_f}. χ_p(ℓ) = (ℓ/p).
A *word* of n is (x, y, z) ∈ ℕ³ (letters ≥ 1 allowed) with xyz − x − z = n (Lorenzini's critical polynomial of A₃;
HJ_DEEP's formal words with middle letter y).

## Summary

1. **Lemma L (PROVED; forms mostly prior).** U_II(n) ≥ 1 ⟺ some f ≡ 3 (mod 4) with (n/f) = −1 has (−n mod f) | f + 1
   ("Jacobi form") ⟺ n has a word with 4 | x, 4 | y or 4 | z. The L_T profile of CONV2 is exactly the Jacobi completion:
   among the words with 4 | xy, the U_II words are precisely those with (n/f) = −1, the rest (x ≡ y ≡ 2 mod 4) have
   (n/f) = +1. The two López branches are the two 2-adic halves r | m_f (B) and 4 | r (A, together with the residue 1
   = 4m_f mod f) of the one residue set Div⁺(f+1) = {r mod f : r | f+1, (r/f) = 1}. (Word form and the sign ⟺ slice dictionary are DK Thm 4.5 / HJ_DEEP Prop 2.1.)
2. **Joint structure at hard primes (EVIDENCE, 6 354 932 primes p ≡ 1 (24) ≤ 10⁹, three coordinates).** No
   complementarity was found where it matters: in the deep tails (99–99.9 % quantiles) their least witnesses are
   *positively* dependent, before and after stratifying by local data and by a weighted χ_p-score (co-failure
   1.2–5.9× the conditional-independence prediction after stratification, up to 16× raw). In the bulk (≈ 94 % quantile)
   there is a mild, statistically clear *negative* dependence after stratification (ratio 0.81–0.95), consistent with
   nearby shifted integers competing for the same small prime factors (hypothesis). A plausible common driver of the tails is χ_p on small primes (both branches
   need a χ_p = −1 prime factor in the witness, PROVED; that it *causes* the dependence is a hypothesis). In the f-coordinate the two branches are even **exchangeable in
   law** (Prop E, PROVED; the residue identity is López's own remark): inversion x ↦ x⁻¹ swaps the branches at every
   modulus. No additional pointwise link was found; the rarity of joint failure looks like two small probabilities
   multiplied, times a tail dependence factor > 1. All 45 primes of the three top-15 hardness lists are in 𝔐.
3. **No link law (Prop D).** For every X there are infinitely many primes p ≡ 1 (mod 840) at which *both* branches fail
   at every witness modulus f ≤ X (PROVED, Dirichlet), and — CONDITIONAL on Dickson's conjecture — at every shift index
   y ≤ X and every middle letter T ≤ X. Hence no law "A fails up to X ⟹ B fires by g(X)" with g independent of p holds
   in any of the three coordinates (unconditionally in f).
4. **Sharper target U₇ (new statement; CERTIFIED to 10¹⁰, on 𝔐 to 10¹²).** U₇(n): *some f ≡ 7 (mod 8) has
   (−n mod f) dividing f + 1* ⟺ n has a word with 8 | xy ⟺ some n + x has a divisor ≡ −1 (mod lcm(8, x)) ⟺ some gn + 1
   has a divisor ≡ −1 (mod lcm(8, g)). Sign-free (no Jacobi condition, no branch split), T1 automatic, (★) ⊂ U₇ ⊂ U_II on
   n ≡ 1 (4), U₇ holds on n ≡ 3 (4). **Its only odd non-square zeros ≤ 10¹⁰ are 105, 1465, 3865, 4545, 10305, 12145,
   39361, 67425** (all composite, all ≡ 1 (8), each divisible by 5 or 7); **no odd prime zero ≤ 10¹⁰; no zero among the
   7 071 222 859 non-square n ∈ 𝔐 ∩ (10¹⁰, 10¹²]** (hence no non-square zero in 𝔐 up to 10¹²). On n ≡ 1 (4), U₇ = (★) ∪ (Type A with cd even): the Type A branch is needed
   only in its f ≡ 7 (mod 8) half (the other half leaves the prime 9601 and 42 zeros ≤ 10⁷).
5. **Census.** U_II at 𝔐-primes (indeed at all non-square n ∈ 𝔐) ≤ 10¹² holds by inheritance ((★) ⊂ U_II; TRYO, LADDER, MSPLUS censuses) — not recomputed;
   U₇ (stronger) recomputed on all 𝔐 inputs ≤ 10¹² (one engine + checks).

No pointwise mechanism; B2 unchanged. **Verdict: narrowed (p-independent first-witness link laws dead in the stated
scopes; no complementarity found in the deep-tail data, EVIDENCE) + sharper target (U₇).** Not a HOT LEAD.

## 0. Mandatory falsifier table (committed at checkpoint 1 in `2922557e`; final form)

Objects: (i) the lane's *idea*, a link law between the branches; (ii) the target U₇.

| screen | link law (idea) | U₇ (target) | label |
|---|---|---|---|
| **F1 odd squares** | both branches fail at every f, y, T at n = m², so any link law must use non-squareness; Prop D's constructed primes are "squares at every modulus ≤ X" (p ≡ 1 mod lcm) and kill every p-independent *first-witness* law (unconditionally in f; under Dickson in a, T). Squares alone do not exclude prime-only laws | U₇(m²) = 0: every divisor r of f+1 is a Jacobi residue mod f ≡ 7 (8), while −m² is a non-residue for f coprime to m (coprimality is forced by a hit; Lemma 7(ii)). Non-squareness enters at the first step — and that is all the target says; the existence of the witness is the open part | PROVED |
| **F2 numerator 8** | U⁽⁸⁾ (547 zeros n ≡ 1 (4) ≤ 10⁸, 45 primes, last 3 869 153; Z59_CONV2) — a law valid verbatim for K = 8 is false below these thresholds | **U⁽⁸⁾ ⊂ U₇** (Lemma 7(iv)): at f ≡ 7 (8), U⁽⁸⁾ uses only the targets r \| (f+1)/8 or 8 \| r; U₇ adds the divisors r of f+1 with v₂((f+1)/8) < v₂(r) < 3. An argument for U₇ must use these extra targets (else it proves U⁽⁸⁾, false at 547 n ≤ 10⁸). Also the two branch halves of U₇ fail at 14 resp. 12 primes ≤ 10⁸ (§4.2) | PROVED + CERTIFIED |
| **F3 composites** | 105, 4545 (U_II-zeros) have both branches failing totally | U₇-zeros = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425} ≤ 10¹⁰: composite, divisible by 5 or 7 (U₇'s complete moduli are 7 and 15, Lemma 7(v)). A proof of CONJECTURE U₇ must fail at these 8 | CERTIFIED |
| **F4 known zeros** | B fails totally at the 14 (★)-zero primes, A at 193, 2521, 66529: no one-sided law; Prop D | U₇ ≥ 1 at all 14 (★)-zero primes (rescued by Type A with cd even; census), at 193, 2521, 66529 and the 24 𝔊*-zeros with R ≥ 1 and the 12 R₈-zero primes (R ≥ 12) — by (★) ⊂ U₇ on n ≡ 1 (4); no odd prime zero ≤ 10¹⁰ (all listed prime controls rescued; the composite exceptions are F3) | PROVED + CERTIFIED |

## 1. Statements attacked

* **López's Conjecture 1** (arXiv:2404.01508v3, Conjecture 1; read from `sources/lit2026f/r270-lopez-2404.01508v3-html.md`,
  lines 431–452): for every prime p there are d, n ∈ ℕ with p ≡ −4d (mod 4dn − 1) [Type A, his Thm 7] or p ≡ −n
  (mod 4dn − 1) [Type B, his Thm 4]; verified there for the first 10 000 primes.
* **CONJECTURE U_II** (Z59_CONV2): every odd non-square n ∉ {105, 4545} has U_II(n) ≥ 1 (CERTIFIED to 10¹⁰).
  **(MS-U)**: U_II(p) ≥ 1 for primes p > 10¹⁷ in 𝔐; (MS) ⟹ (MS-U) ⟹ (MS-II); (MS-U) + Mordell + Salez ⟹ ES.
* **Lane question.** A pointwise mechanism specific to U_II: an algebraic link between a failure of one branch and a
  success of the other, e.g. a law "A has no witness of size ≤ X ⟹ B has one of size ≤ g(X)".
* *Why not closed.* CONV2 Prop 3.1 (nesting on a shared integer) and fixed finite (T, f) menus exclude only same-integer
  rescue and p-independent menus; adaptive/p-dependent links across different integers were open (Z59_SUMMARY §5.1).

## 2. Lemma L — forms of U_II, the Jacobi completion

**Lemma L (PROVED).** For odd n ≥ 1 the following are equivalent:
* (iii) [CONV2 Lemma 1(iii)] ∃ T ≥ 1: Tn + 1 has a divisor f ≡ −1 (mod L_T), L_T = T if 4 | T, else 4T;
* (P) ∃ a ≥ 1: n + a or n + 4a has a divisor ≡ −1 (mod 4a) [B at a; A at a — one modulus 4a, two integers];
* (J) ∃ f ≡ 3 (mod 4) with (n/f) = −1 (Jacobi) such that r := (−n mod f) ∈ {1, …, f−1} divides f + 1;
* (X) n has a word (x, y, z) with 4 | x or 4 | y or 4 | z.

Moreover **(dichotomy)**: for every word with 4 | xy, put f = xy − 1 (≡ 3 mod 4). Then gcd(n, f) = 1, and
(n/f) = −1 if 4 | x or 4 | y, while (n/f) = +1 if x ≡ y ≡ 2 (mod 4).

*Proof.* Two facts. (F-a) If r′ is odd, r′ | f + 1 and f ≡ 3 (mod 4), then (r′/f) = 1: by reciprocity
(r′/f) = (f/r′)(−1)^{(r′−1)/2} = (−1/r′)(−1)^{(r′−1)/2} = 1. (F-b) (2/f) = +1 for f ≡ 7 (8), −1 for f ≡ 3 (8).
* *Dichotomy.* n + x = z(xy − 1) gives −n ≡ x (mod f); gcd(x, f) = 1 since f ≡ −1 (mod x), so gcd(n, f) = 1. Write
  x = 2^j x′ (x′ odd). By (F-a), (x/f) = (2/f)^j. If 4 | x and j = 2: +1; if j ≥ 3 or (4 | y and j = 1): 8 | xy, f ≡ 7 (8),
  +1; if j = 0: +1. If x ≡ y ≡ 2 (4): j = 1, xy ≡ 4 (8), f ≡ 3 (8), (x/f) = −1. Finally (n/f) = (−1/f)(−n/f) = −(x/f).
* (X) ⟹ (J). By the symmetry x ↔ z assume 4 | x or 4 | y; f = xy − 1. If x < f then r = x | f + 1 and (n/f) = −1 by the
  dichotomy. If x ≥ f then x(y − 1) ≤ 1, so y = 1 (the case x = 1, y = 2 has no factor 4); then 4 | x, f = x − 1 ≡ 3 (4),
  r = 1 and (n/f) = −(1/f) = −1.
* (J) ⟹ (X). Put x = r, y = (f+1)/r, z = (n + r)/f ∈ ℕ. Then xyz − x − z = (f+1)z − r − z = n and 4 | xy. If neither
  4 | x nor 4 | y, the dichotomy gives (n/f) = +1, a contradiction.
* (X) ⟺ (iii). (xy − 1)(zy − 1) = y(xyz − x − z) + 1 = yn + 1. If 4 | y take T = y, f = xy − 1 ≡ −1 (mod T); if 4 | x
  (4 ∤ y), f ≡ −1 (mod 4y); if 4 | z use zy − 1. Conversely let f | Tn + 1, f ≡ −1 (mod L_T), g = (Tn+1)/f. Then
  fg ≡ 1 forces g ≡ −1 (mod T); x = (f+1)/T, z = (g+1)/T ∈ ℕ, y = T give a word, with 4 | y or (L_T = 4T) 4 | x.
* (X) ⟺ (P). 4 | y: a = x, f = xy − 1 ≡ −1 (mod 4a) divides n + a. 4 | x: a = x/4, f ≡ −1 (mod 4a) divides n + 4a.
  4 | z: same with z. Conversely f | n + a (resp. n + 4a), f ≡ −1 (mod 4a) gives the word (a, (f+1)/a, (n+a)/f) with
  4 | y (resp. (4a, (f+1)/(4a), (n+4a)/f) with 4 | x). ∎

CERTIFIED cross-check: (iii), (P), (J), (X) agree for all odd n ≤ 801; (P), (J) give exactly the non-square zeros
{105, 4545} among odd n ≤ 6000 (`scripts/z60_lopez_forms.py`).

*Reading.* In (J), branch B is r | m_f and branch A is r = 4a (a | m_f), read mod f — so A's residues are
{1} ∪ {r < f : r | f+1, 4 | r}, since 4m_f ≡ 1; their union is the residue image of the Jacobi-+1 divisors of f + 1
(F-a, F-b): every divisor of f+1 if f ≡ 7 (8); all but those with v₂(r) = 1 if f ≡ 3 (8). So the L_T profile is
not an accident of two coordinate lines: it is the **largest family of words with 4 | xy on which T1 is automatic**; the
complementary words (x ≡ y ≡ 2 mod 4) are exactly the (n/f) = +1 ones and do occur at squares (1 = 2·2·1 − 2 − 1).
*Prior art.* (X) and the sign ⟺ slice correspondence are DK Thm 4.5 (`DEDEKIND_ES.md`, five slices, letters ≥ 2, cell
enumeration) and HJ_DEEP Prop 2.1–2.2; LORENZINI_W (F3) is the sign-free interior-word precursor of (J) (letters ≥ 2,
2 ≤ ρ ≤ (f+1)/2, n + ρ ≥ 2f); (P) re-indexes CONV2 Lemma 1(iv); D_f⁻¹ = 4D_f is CONV2 Lemma 1(vi) and López's own
remark (source lines 441–447: the Type −n and Type −4d divisor sets "are mutual inverses"). New here: the direct Jacobi
proof covering letters = 1 and the statement of (J) with its Jacobi filter ("the U_II residue set is Div⁺(f+1)").
Residue counts (PROVED; checked for all f ≡ 3 (4) ≤ 2000 by the reviewer): |D_f| = |4D_f| = τ(m_f), 1 ∈ D_f ∩ 4D_f
always (never disjoint); |D_f ∪ 4D_f| = τ(4m_f) − 1 if f ≡ 7 (8), = 2τ(m_f) − 1 if f ≡ 3 (8) (the integers 1 and f + 1
give the same residue).

## 3. Joint structure of the two branches at hard primes

### 3.1 Residue-level links (PROVED)

**Prop E (inversion swaps the branches; exchangeability in law).** Fix f ≡ 3 (4) and a unit x mod f.
(a) x ∈ 4D_f ⟺ x⁻¹ ∈ D_f (since a·4(m_f/a) = 4m_f ≡ 1). Hence: *A fires at f for n ⟺ B fires at f for every n′ ≡ n⁻¹
(mod f)*; also A at f for n ⟺ B at f for n′ ≡ n/4 (mod f). In target coordinates x = −n: x ↦ x⁻¹ swaps D_f and 4D_f
and preserves their union Div⁺(f+1); x ↦ (4x)⁻¹ preserves D_f (LIT Prop I) and its conjugate x ↦ 4x⁻¹ preserves 4D_f
(4a ↦ 4(m_f/a)); x ↦ (4x)⁻¹ does not preserve 4D_f in general.
(b) Fix X and L_X := lcm(840, {f ≤ X}). The vector of B- and A-events at all f ≤ X depends only on p mod L_X, and p ↦ p⁻¹
mod L_X maps it to the swapped vector. Inversion permutes the unit classes mod L_X and fixes 𝔐 setwise (𝔐 is a
subgroup), and also the class 1 mod 24. By the prime number theorem in arithmetic progressions, the joint law of
(min(f_B(p), X⁺), min(f_A(p), X⁺)) over primes in 𝔐 (or p ≡ 1 mod 24) is symmetric, in the limit. ∎
*Data check.* P(f_B > X) = 0.3999, 0.2309, 0.09859, 0.02964 vs P(f_A > X) = 0.3998, 0.2309, 0.09850, 0.02970 at
X = 15, 35, 95, 311 (primes ≡ 1 (24) ≤ 10⁹). In the a- and T-coordinates the indices are not preserved (a ↦ m_f/a), and
the marginals differ.
*Scope.* (b) is a fixed-X distributional statement over primes; at a single p it relates p to a different residue p⁻¹,
not to p itself (no existence content). *Prior.* (a) is López's remark / CONV2 Lemma 1(vi); (b) is the branch-swapping
specialisation of the fixed-modulus frequency argument of Z58_LIT Prop I's corollary.

**Coupling lemma (PROVED; prior: Z57_BFII Cor 2.4, WITNESS Lemma 1.1).** For a prime p ≡ 1 (4), every witness f of
either branch has (p/f) = −1, hence (f/p) = −1 and a prime factor ℓ | f with χ_p(ℓ) = −1. So both f_A(p), f_B(p) ≥ n′_p
(least odd prime non-residue). One quadratic datum thus delays both branches. (A shared lower bound does not by itself
imply positive covariance; that it drives the observed tail dependence is a hypothesis.)

### 3.2 Data (EVIDENCE; CERTIFIED counts)

Engine `scripts/z60_lopez_joint.c`: for each prime p it computes, per branch, the least index in three coordinates —
a (outer letter / shift: B: p + a, A: p + 4a, divisor ≡ −1 mod 4a), f (witness modulus) and T (middle letter: B: C with
4Cp + 1, A: c with cp + 1) — by full factorisation (trial division + Pollard ρ, Miller–Rabin bases ≤ 37) or residue bitmaps (A: 4a reduced mod f).
Raw output (≈ 149 MB, not archived) has sha256 in `joint1e9_input.sha256`; the aggregate outputs are archived:
`joint1e9_stats_raw.txt` (marginals, maxima, raw ratios), `joint1e9_stats_strat.txt` + per-stratum sufficient
statistics `joint1e9_strata_suffstats.txt.gz` (N_s, A_s, B_s, AB_s), `joint1e9_stats_lscore.txt` (bin edges, per-bin
tails), `joint1e9_hardest.txt`, `joint1e9_hist_aB_aA.txt`. Reviewer checks: histogram reproduces the raw a-ratios; all
45 hard primes recomputed exactly; a fresh run on primes ≤ 2·10⁷ shows the same qualitative pattern (bulk deficit, tail
excess). The exact 10⁹ numbers are one run of one engine.
Run: all 6 354 932 primes p ≡ 1 (24) ≤ 10⁹, bounds a ≤ 3000, f ≤ 20 000, T ≤ 3000. Sanity: a_B = ∞ exactly at the 14
(★)-zero primes, a_A = ∞ exactly at 193, 2521, 66529 (matching the screens and B1_LINE).

| coordinate | max finite B | max finite A | max U_II index (min) | argmax |
|---|---|---|---|---|
| a | 469 | 291 | 37 | 2 164 801 |
| f | 19 991 | 19 979 | 14 447 | 740 856 601 |
| T | 2932 (21 > 3000) | 156 | 50 | 5 886 169 |

*Tail dependence* (`z60_lopez_jointstats.py`, `z60_lopez_strat.py`, `z60_lopez_lscore.py`): pooled ratio
obs/exp of {both indices > X}, exp = Σ_strata N_s P_s(A > X) P_s(B > X) (conditional independence):

| coordinate, X (≈ quantile of B) | none | n′_p strata (20) | p mod 5·7·11·13 (2880) | + χ_p on 17…31 (92 160) | χ_p-score, 20 quantile bins | score × p mod 35 |
|---|---|---|---|---|---|---|
| a, X = 3 (94 %) | 1.45 | 0.81 | 0.94 | 0.90 | 0.92 | 0.94 |
| a, X = 6 (99.2 %) | 4.03 | 1.31 | 1.66 | 1.43 | 1.52 | 1.34 |
| a, X = 13 (99.9 %) | 15.8 | 2.73 | 3.18 | 2.31 | 3.54 | 2.95 |
| f, X = 95 (90 %) | 1.93 | 1.17 | 1.49 | 1.32 | 1.18 | 1.34 |
| f, X = 783 (99 %) | 3.57 | 1.88 | 2.55 | 2.20 | 1.76 | 1.94 |
| f, X = 4031 (99.9 %) | 8.97 | 4.14 | 5.53 | 4.34 | 3.92 | 4.18 |
| T, X = 8 (99 %) | 5.64 | 2.22 | 2.60 | 2.17 | 2.35 | 2.35 |
| T, X = 21 (99.9 %) | 14.8 | 4.82 | 5.88 | 4.08 | 5.04 | 4.95 |
| T, X = 3 (94 %) | 1.47 | 0.82 | 0.95 | 0.92 | 0.93 | 0.95 |

χ_p-score s(p) = Σ_{3 ≤ ℓ ≤ 200} χ_p(ℓ) log ℓ / ℓ (a weighted character score — the first-prime-term approximation to
−L′/L(1, χ_p), not an estimate of log L(1, χ_p)); 20 quantile bins. n′_p strata: least odd prime non-residue ≤ 97
(catch-all > 97 is empty in this run). Across bins both marginal tails grow by a factor
≈ 30–80 from the lowest to the highest score bin, and co-failures concentrate in the top bins (none in the lowest four or
five bins at the 99 % level). Counts at the deepest X are small (59–107 joint events; T: 10), so those ratios are rough.
*Reading (EVIDENCE/Assessment).* (1) In the deep tails (99 % and 99.9 % rows) the two branches are positively dependent,
unconditionally and within every stratification tried. (1′) At the bulk threshold (a, X = 3; T, X = 3: ratios 0.82–0.95
after stratification, ≈ 3·10⁴ joint events, so a real effect; minimum 0.81) joint failure is mildly *rarer* than conditional
independence predicts — a weak complementarity, plausibly the sieve repulsion of nearby shifted integers (a prime
ℓ ≥ 17 divides at most one of p + a, p + a′ for |a − a′| < ℓ; privacy lemma — a hypothesis, not tested). It is a bulk
effect of size ≲ 20 % and reverses in the tails, where the zeros live. Positive *pooled* ratios do not imply positive
dependence in every stratum. (2) Most of the raw
dependence is absorbed by stratifying on χ_p on small primes and local data; the residual 1.2–5.9× is unexplained
(hypothesis: further χ_p / local structure). (3) Hence "the branches almost never fail together" looks like the product
of two small failure probabilities — the union roughly doubles the residue set at each f (§2) — multiplied by a tail
dependence factor > 1. In the tested deep-tail events there is no anti-correlation for a link law to explain; this is
evidence about these thresholds and strata, not a theorem excluding a pointwise mechanism.
*Hardest primes* (`data/z60/lopez/joint1e9_hardest.txt`): all 45 primes of the three top-15 lists are in 𝔐 (the
"p in 𝔐" lists duplicate them). Examples
(p: a_B, a_A | f_B, f_A | C_B, c_A): 2 164 801: 37, 44 | 2135, 879 | 6, 5; 9 744 001: 39, 36 | 3431, > 20 000 | 8, 42;
740 856 601: 6, 7 | 14 447, 14 503 | 3, 11; 5 886 169: 10, 1 | 4679, 331 | 72, 50. No visible deterministic relation
between the two branches' witnesses. The joint histogram of (a_B, a_A) is in `joint1e9_hist_aB_aA.txt`.

## 4. Link laws, and which part of the A branch matters

### 4.1 No p-independent link law

**Prop D (no p-independent link law).** Let X ≥ 1.
* (f) PROVED. Every prime p ≡ 1 (mod lcm(840, {f ≤ X : f ≡ 3 mod 4})) has no U_II witness f ≤ X (both branches fail at all f ≤ X).
  Infinitely many such primes exist (Dirichlet), all in 𝔐.
* (a, T) CONDITIONAL on Dickson's conjecture. There are infinitely many primes p ≡ 1 (mod 840) such that for all
  1 ≤ k ≤ X neither p + k has a divisor ≡ −1 (mod L_k) nor kp + 1 has a divisor ≡ −1 (mod L_k). In particular
  a_B(p) > X, a_A(p) > X/4, C_B(p) > X/4, c_A(p) > X.
* Consequently, for every g: ℕ → ℕ, the law "branch A has no witness of index ≤ X ⟹ branch B has one of index ≤ g(X)"
  (and the same with A, B exchanged) fails for infinitely many primes in 𝔐: in the f-coordinate unconditionally, in the
  a- and T-coordinates under Dickson (apply the above with X′ = max(4X, 4g(X))).

*Proof.* (f) For f ≡ 3 (4), f ≤ X: p ≡ 1 (mod f), so r = f − 1, and r | f + 1 forces f ≤ 3; at f = 3, r = 2 and (2/3) = −1,
so the Jacobi filter of (J) excludes it (directly: D₃ ∪ 4D₃ = {1}, needing p ≡ 2 mod 3). By Lemma L(J), no hit.
(a, T) Let M = lcm(840, {4k(k+1) : k ≤ X}) and consider the linear forms Mt + 1, (M/(k+1))t + 1 and (kM/(k+1))t + 1
(k ≤ X). All take the value 1 at t = 0, so their product has no fixed prime divisor; Dickson's conjecture gives infinitely
many t ≥ 1 with all values prime. Then p = Mt + 1 ≡ 1 (mod 840) is prime and p + k = (k+1)q_k, kp + 1 = (k+1)Q_k with
primes q_k, Q_k ≡ 1 (mod L_k) (as (k+1)L_k | (k+1)·4k | M) and q_k, Q_k > k + 1. Every divisor of (k+1)q_k is e or eq_k
with e | k+1, ≡ e (mod L_k); likewise for Q_k. A divisor e ≤ k + 1 with e ≡ −1 (mod L_k) needs L_k ≤ k + 2: false if
4 ∤ k (L_k = 4k); if 4 | k then e = k − 1 | k + 1 forces k ≤ 3, impossible. Lemma L(P)/(iii) translate this to the four
branch indices (B at a fails mod L_a ⊇ mod 4a; A at a is p + 4a mod 4a = L_{4a}). ∎
*Prior.* The method is CONV2's fixed-menu argument (f) and the Dickson constructions of WITNESS Prop 3.1 / DISPROOF_AVENUES
§3 Prop 3.1 (= CONVO Thm 7.7) for (★) and full Type II; the U_II statement in three coordinates is the routine
transfer. *Escape hatches (not excluded).* p-dependent or adaptive laws, and arguments that are not first-witness
implications (counting, joint-failure exclusions). Note that one-sided laws "A fails at all indices ≤ X ⟹ B fires by
g(X, p)" required for every X are refuted by the F4 data for every g, unless restricted to p beyond the known one-branch
zeros: at p = 5569 (in 𝔐) B never fires while A first fires at a = 2, so X = 1 is a counterexample. The natural
surviving form is two-sided — a joint-failure exclusion "min(index_A, index_B) ≤ g(p)" — which is U_II with a size
bound, not a reduction of it.

### 4.2 Which part of the A branch matters: U₇

**Lemma 7 (PROVED).** For odd n define U₇(n): ∃ f ≡ 7 (mod 8) with r := (−n mod f) ∈ {1, …, f−1} dividing f + 1.
* (i) U₇(n) ⟺ n has a word with 8 | xy ⟺ ∃ x ≥ 1: n + x has a divisor ≡ −1 (mod lcm(8, x)) ⟺ ∃ g ≥ 1: gn + 1 has a
  divisor ≡ −1 (mod lcm(8, g)).
* (ii) U₇(n) ⟹ U_II(n) (8 | xy ⟹ 4 | x or 4 | y). Every U₇ witness has (n/f) = −1; hence **U₇(m²) = 0** for odd m.
* (iii) U₇(n) for every n ≡ 3 (mod 4) (f = 2n + 1, r = n + 1).
* (iv) For n ≡ 1 (mod 4): every (★) word is a U₇ word, so **(★) ⊂ U₇ ⊂ U_II** (as existence predicates), and
  U₇(n) ⟺ (★)(n) or n has a Type A word with cd even;
  also U⁽⁸⁾ ⊂ U₇.
* (v) f = 7 and f = 15 are complete: U₇(n) whenever gcd(n, 7) = 1 and (n/7) = −1, or gcd(n, 15) = 1 and (n/15) = −1.

*Proof.* (i) As in Lemma L, with f = xy − 1 ≡ 7 (8) ⟺ 8 | xy: a word gives f | n + x, f ≡ −1 (mod x); if x ≥ f then y = 1,
8 | x, r = 1. Conversely x = r, y = (f+1)/r, z = (n+r)/f. Shift form: d = xy − 1 ≡ −1 (mod x) and ≡ 7 (mod 8) ⟺ d ≡ −1
(mod lcm(8, x)). T-form: (xy − 1)(zy − 1) = yn + 1 with g = y; conversely f | gn + 1, f ≡ −1 (mod lcm(8, g)) gives
x = (f+1)/g, z = (h+1)/g, h = (gn+1)/f ≡ −1 (mod g), and 8 | xg. (ii) If 4 ∤ x and 4 ∤ y then v₂(xy) ≤ 2. Jacobi: r | f+1
with f ≡ 7 (8) gives (r/f) = 1 by (F-a), (F-b); so (−n/f) = 1, (n/f) = −1, impossible for n = m² (gcd(n, f) = 1 as in
Lemma L). (iii) f = 2n + 1 ≡ 7 (8), −n ≡ n + 1 (mod f), n + 1 | 2n + 2. (iv) A (★) word is (u, 4C, B) with
n = 4uBC − u − B; n ≡ 1 (4) gives u + B ≡ 3 (4), so one of u, B is even and 8 | 4uC or 8 | 4BC — a word with 8 | xy after
possibly exchanging x ↔ z. A Type A word is (4d, c, b′) with b′ = (n + 4d)/(4cd − 1); n ≡ 1 (4) forces b′ ≡ 3 (4), so it
is a U₇ word iff 8 | 4dc, i.e. cd even. U_II words not of these shapes do not exist (Lemma L(X): 4 | y is (★), 4 | x or
4 | z is Type A). U⁽⁸⁾: its witnesses f ≡ −1 (mod 8) have targets r | (f+1)/8 or r = 8a with a | (f+1)/8 (CONV2 Lemma
1(vi) at K = 8), all divisors of f + 1. (v) f = 7: targets −r for r ∈ {1, 2, 4}, i.e. n ≡ 6, 5, 3 (mod 7), the
non-residues. f = 15: r ∈ {1, 2, 4, 8}, n ≡ 14, 13, 11, 7 (mod 15), exactly the units with (n/15) = −1. ∎

**CONJECTURE U₇.** Every odd non-square n ∉ Z₇ := {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425} satisfies U₇(n).
At primes: every odd prime has U₇ (no odd prime zero ≤ 10¹⁰; p = 2 is outside the odd domain). (MS-U₇) (U₇(p) for 𝔐-primes p > 10¹⁷) sits between: (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II), because (★) ⊂ U₇ ⊂ U_II on
n ≡ 1 (4) (implications only; strictness as statements is not claimed).
What it offers is cleanliness, not a proof: one divisor condition "(−n mod f) | f + 1, f ≡ −1 (mod 8)" with no Jacobi
filter, no branch split, no parity bookkeeping; T1 is automatic. Assessment: as a target it isolates the tied divisor
event (B2) in its plainest form; no easier proof route was demonstrated.

**Data (CERTIFIED; `scripts/z60_lopez_u7.c`, bitmap f ≤ 20 000 + exact fallback over all f ≤ 2n + 1).**

| run | result | file |
|---|---|---|
| U₇, all odd n ≤ 10⁸ | zeros exactly Z₇ (8, all composite); 4999 odd squares skipped (T1); 4976 LATE certificates | `u7_all_1e8.txt.gz` |
| U₇, n ≡ 1 (4), (10⁸, 10¹⁰] (4 chunks) | no zero (2.475·10⁹ n; n ≡ 3 (4) by Lemma 7(iii)) | `u7_mod1_chunk{0..3}.txt.gz` |
| U₇, n ∈ 𝔐, (10¹⁰, 10¹²] (4 chunks) | no zero among the 7 071 428 573 n ∈ 𝔐 (of which 205 714 odd squares, skipped as T1 zeros; both counts match the expected totals) | `u7_M_1e10_1e12_chunk{0..3}.txt.gz` |
| halves at primes p ≡ 1 (4) ≤ 10⁸: B-targets at f ≡ 7 (8) | 14 prime zeros = the 14 (★)-zero primes (as Lemma 7(iv) predicts) | `u7half_tgt1_primes_1e8.txt` |
| A-targets at f ≡ 7 (8) (residues {1} ∪ {4 \| r \| f+1}) | 12 prime zeros: 5, 53, 193, 673, 1489, 2521, 20 641, 21 841, 28 921, 66 529, 225 289, 2 654 401 (review fix: a first run omitted the residue 1 and reported 17) | `u7half_tgt2_primes_1e8.txt` |
| (★) ∪ (A with f ≡ 3 (8)), n ≡ 1 (4) ≤ 10⁷ | 42 non-square zeros (one prime, 9601); primes ≤ 10⁸: only 9601 | (rerun command §7) |
| other restrictions, all odd n ≤ 10⁶ | f ≡ 3 (8): 381 zeros (13 primes); f ≡ 15 (16): 443 (29); f ≡ 7 (16): 164 (7) | — |

*Exact fallback is complete:* if f > n then r = f − n and r | f + 1 give r | n + 1, so f ≤ 2n + 1.
*Checks* (`scripts/z60_lopez_u7check.py`): independent word enumeration (numpy slices over all (x, y) with 8 | xy) for
all odd n ≤ 10⁶ gives exactly Z₇ and no odd square with a word; all 342 375 LATE certificates (n, f) in the archived files
re-verified (f ≡ 7 (8), r | f + 1); 3000 random n ≡ 1 (4) in [10⁸, 10¹⁰] and 2000 random n ∈ 𝔐 in [10¹⁰, 10¹²] re-decided
by a plain loop over f (no bitmaps): all have witnesses. One production engine above 10⁶; the bitmap path is spot-checked,
not duplicated.

*Reading.* On n ≡ 1 (4) the two U_II branches are better described as "(★)" and "the f ≡ 7 (mod 8) half of Type A
(cd even)": this half alone rescues every (★)-zero, leaving 8 composite zeros; the other half (f ≡ 3 mod 8) leaves 9601.
Within U₇, the B- and A-target halves fail at 14 and 12 primes ≤ 10⁸, the union at none — the same "two small
probabilities" picture as §3 (Assessment; no dependence measurement was made for U₇'s halves).

## 5. Census

* **U_II at 𝔐-primes beyond 10¹⁰ (inherited, not recomputed).** (★) ⊂ U_II. R(p) ≥ 1 at all 355 096 166 𝔐-primes in
  (10¹⁰, 3·10¹¹] (TRYO), at every non-square 𝔐-integer in (17 401 609, 10¹¹] (LADDER) and in (10¹¹, 10¹²] (MSPLUS); below
  10¹⁰ CONV2's census. Hence U_II ≥ 1 at every prime in 𝔐 up to 10¹², and at every non-square n ∈ 𝔐 up to 10¹² (the U_II
  zeros 105, 4545 are not units mod 840).
* **U₇ (stronger) recomputed** on all 𝔐 inputs ≤ 10¹² and all odd n ≤ 10¹⁰ (§4.2).

## 6. Verdict, falsifier table restated, proposed FRONTIER text, bottom line

**Verdict: narrowed + sharper target; no mechanism; B2 unchanged. Not a HOT LEAD.**
* *Narrowed* (scoped). (a) No p-independent first-witness link law between the branches: PROVED in the witness-modulus
  coordinate, CONDITIONAL on Dickson in the shift and middle-letter coordinates (Prop D); one-sided laws for all X are
  refuted by F4 data. (b) The branches are exchangeable in law in the f-coordinate (Prop E, PROVED; residue identity
  prior) and share the lower bound n′_p (PROVED); deep-tail positive dependence after stratification is EVIDENCE (§3.2). So no complementarity mechanism was found where zeros
  live: no additional pointwise link was found, and the tested deep-tail events show positive pooled dependence; the only
  complementarity seen is a ≲ 20 % bulk effect.
* *Sharper target.* CONJECTURE U₇ (Lemma 7): sign-free single divisor condition, (★) ⊂ U₇ ⊂ U_II on n ≡ 1 (4); only 8
  composite zeros ≤ 10¹⁰; no non-square zero in 𝔐 ≤ 10¹².
* *Not achieved.* Any pointwise lemma for U_II, U₇, (MS-U) or (MS).

**Falsifier table, final.** F1: T1 is automatic for U₇; Prop D's primes (locally squares) kill every p-independent
first-witness link law (unconditionally in f, under Dickson in a, T). F2: U⁽⁸⁾ ⊂ U₇; a U₇ proof must use the targets
outside U⁽⁸⁾. F3: Z₇ (8 composites, each divisible by 5 or 7). F4: all listed prime controls rescued by U₇; neither
branch alone suffices.

**Proposed FRONTIER text** (for the integrator; FRONTIER not edited here).
* §2.4 / ladder: "(MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II), where U₇(n): some f ≡ −1 (mod 8) has (−n mod f) | f + 1
  (⟺ a word xyz − x − z = n with 8 | xy ⟺ some n + x has a divisor ≡ −1 mod lcm(8, x)); on n ≡ 1 (4), U₇ = (★) ∪ (Type A with
  cd even). Odd non-square zeros ≤ 10¹⁰: 105, 1465, 3865, 4545, 10305, 12145, 39361, 67425; no non-square zero in 𝔐 ≤ 10¹² (`Z60_LOPEZ.md`
  §4.2, CERTIFIED, one engine)."
* §6: "(z60) López's two branches: no p-independent first-witness link law (Prop D: unconditional in the witness modulus,
  Dickson in shift / middle-letter coordinates); inversion makes them exchangeable in law (witness-modulus coordinate); no
  additional pointwise link found; tested deep-tail events positively dependent even after χ_p / local stratification,
  only a ≲ 20 % bulk complementarity (EVIDENCE)."
* §7 item 19: "the U-line target can be replaced by the sign-free U₇ (Lemma 7); its witness is any divisor r of f+1."

**Bottom line.** The brief asked why López's two branches almost never fail together and whether one branch's failure
forces the other's success. They do not interact the way a link would: on each modulus the branches are the two 2-adic
halves of one target set (the Jacobi-positive divisors of f + 1), inversion swaps them exactly, and on primes their least
witnesses are positively dependent in the deep tails — a large n′_p or a χ_p that is +1 on many small primes delays
both (a weak negative dependence appears only in the bulk). Joint failure is
rare because it needs two unlikely events, and the dependence makes it *less* rare than independence would. A
p-independent link law is impossible (unconditionally for witness moduli, under Dickson for the other coordinates). The
useful by-product is a cleaner target: U₇ — "some f ≡ −1 (mod 8) has (−n mod f) dividing f + 1" — contains (★) on
n ≡ 1 (4), has T1 built in, and fails at no odd non-square except eight composites ≤ 10¹⁰, and at no non-square in 𝔐
≤ 10¹². The wall is still B2.

## 7. Reproduction

Every command was run under `ulimit -v 4000000`, `timeout ≤ 1800`, ≤ 4 concurrent processes (prefix omitted; for the
parallel loops use `set -o pipefail` and check each exit status — all archived chunk footers are present).
```
uv run python scripts/z60_lopez_forms.py 801
gcc -O2 -o /tmp/z60j scripts/z60_lopez_joint.c -lm
for k in 0 1 2 3; do /tmp/z60j $((k*250000000+1)) $(((k+1)*250000000+1)) 0 3000 20000 3000 > /tmp/j1e9_$k.txt & done; wait
cat /tmp/j1e9_?.txt > /tmp/j1e9.txt; sha256sum /tmp/j1e9.txt      # = data/z60/lopez/joint1e9_input.sha256
uv run --with numpy python scripts/z60_lopez_jointstats.py /tmp/j1e9.txt > data/z60/lopez/joint1e9_stats_raw.txt
Z60_DUMP=data/z60/lopez/joint1e9_strata_suffstats.txt.gz uv run --with numpy python scripts/z60_lopez_strat.py /tmp/j1e9.txt > data/z60/lopez/joint1e9_stats_strat.txt
uv run --with numpy python scripts/z60_lopez_lscore.py /tmp/j1e9.txt 200 20 > data/z60/lopez/joint1e9_stats_lscore.txt
uv run --with numpy python scripts/z60_lopez_hard.py /tmp/j1e9.txt data/z60/lopez/joint1e9
gcc -O2 -o /tmp/z60u7 scripts/z60_lopez_u7.c -lm
Z60_LATE=1 /tmp/z60u7 7 1 100000000 20000 0 0 | gzip > data/z60/lopez/u7_all_1e8.txt.gz
B=100000000; for k in 0 1 2 3; do Z60_LATE=1 /tmp/z60u7 7 $((B+k*2475000000)) $((B+(k+1)*2475000000)) 20000 0 1 | gzip > data/z60/lopez/u7_mod1_chunk$k.txt.gz & done; wait
B=10000000000; W=247500000000; for k in 0 1 2 3; do Z60_LATE=1 /tmp/z60u7 7 $((B+k*W)) $((B+(k+1)*W)) 20000 0 8 | gzip > data/z60/lopez/u7_M_1e10_1e12_chunk$k.txt.gz & done; wait
for t in 1 2; do Z60_TGT=$t /tmp/z60u7 7 1 100000000 20000 1 1 > data/z60/lopez/u7half_tgt${t}_primes_1e8.txt; done
Z60_TGT=3 Z60_FMOD=0 /tmp/z60u7 0 1 10000000 20000 0 1;  Z60_TGT=3 Z60_FMOD=0 /tmp/z60u7 0 1 100000000 20000 1 1
Z60_FMOD=8 Z60_FRES=3 /tmp/z60u7 3 1 1000000 4000 0 0   # likewise Z60_FMOD=16 Z60_FRES=15 / 7 with CLS 7
uv run --with numpy python scripts/z60_lopez_u7check.py 1000000 3000 100000000 10000000000 data/z60/lopez/u7_all_1e8.txt.gz data/z60/lopez/u7_mod1_chunk*.gz
Z60_MORD=1 uv run --with numpy python scripts/z60_lopez_u7check.py 1000 2000 10000000000 1000000000000 data/z60/lopez/u7_M_*.gz
```

## 8. Review record

**Hostile internal review** (deep-mode subagent; `data/z60/lopez/review_hostile.md`): 1 BLOCKER, 5 SERIOUS, 4 MINOR. It
verified Lemma L (all implications, letters = 1, f = 3), Prop E, Prop D (both parts, the factors of 4 in the index
bounds), Lemma 7 (i)–(v); all 342 375 LATE certificates; the census arithmetic (7 071 428 573 inputs, 205 714 squares,
7 071 222 859 non-squares); the variant counts (42 / 9601; 381, 443, 164); the raw a-ratios from the archived histogram;
all 45 hard primes recomputed; an independent word enumeration to 2·10⁵ (Z₇ exactly, no square hit); a fresh joint run
≤ 2·10⁷ with the same qualitative pattern. Fixes applied:

| # | finding | fix |
|---|---|---|
| 1 (BLOCKER) | A-half decider (TGT = 2) omitted the residue 1 = 4m_f mod f; 17 prime zeros reported, true 12 | `u7.c` fixed; A-half rerun (12 zeros, matching the reviewer); text corrected; full U₇, TGT = 3 and the joint engine were unaffected |
| 2 | per-f union counts / disjointness false (1 ∈ D_f ∩ 4D_f; 1 ≡ f + 1) | counts corrected to τ(4m_f) − 1 and 2τ(m_f) − 1; Div⁺ defined as a residue set |
| 3 | "nowhere on 𝔐", "every prime" lacked non-square / odd qualifiers | qualifiers added throughout |
| 4 | claimed equivalence of p-dependent link laws with a U_II size bound false | removed; one-sided laws refuted by F4 (p = 5569, X = 1); escape hatches listed as not excluded |
| 5 | "no mechanism" / coupling-causes-dependence overclaimed from pooled data | rephrased as "no additional pointwise link found; tested deep-tail events positively dependent"; causal readings labelled hypotheses |
| 6 | 10⁹ statistics lacked an audit trail | archived aggregate outputs, per-stratum sufficient statistics and the raw-file sha256; all stats rerun under the 4 GB cap (identical numbers) |
| 7 | falsifier shorthand lost scope; "all known zeros rescued" contradicts F3 | F1/F4 rows and §6 restatement rescoped |
| 8 | score called an L-value estimate; "deciles"; ratio ranges; n′_p truncation | renamed weighted χ_p-score (≈ −L′/L(1,χ_p) first terms), 20 quantile bins, ranges 1.2–5.9 / min 0.81; catch-all > 97 empty |
| 9 | prior art for inversion / LORENZINI F3 | Prop E(a) credited to López's remark and CONV2 Lemma 1(vi), E(b) to Z58_LIT; F3 called the interior precursor |
| 10 | fallback completeness bound, reproduction hygiene, stale comment | bound added (§4.2 and the C source); reproduction block updated; comment fixed |
