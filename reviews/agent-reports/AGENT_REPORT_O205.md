# AGENT_REPORT_O205 — exact identities for the ES sign (Gross–Keating / Brandt / mock-modular route to SQ₅), checkpoint 1

Main file: SIGN_IDENTITY.md. Scripts: scripts/si_census.c (weighted N± census), si_fit.py (exact-relation screen),
si_uvform.py, si_cells.py, si_diff.py. Branch side-agent/sign-identity. **ES is not solved, nor any infinite case.**

## SHARP:
1. **Size class: the ES sign counts are d₃-objects, so no GL(2) modular generating function exists (Thm 2.2, PROVED).**
   Σ_{n≤X} N₋(n) ~ (15/32)·X log²X/2 (240 of 512 cells mod 8; N₊: 80/512), while |X_n| ≪ n^{1/2+ε}. Growth at cusps
   (non-cuspidal weight > 1), sup-norm bounds (weights ≤ 2) and Rankin–Selberg (cusp weight ≥ 5/2) then exclude every
   finite sum of holomorphic modular forms of any weight in ½ℤ_{>0}, any level/character, as generating function of
   N₋, N₊, S or |X_n| — independently of T1. Steering consequence: any exact identity must be GL(3)-sized (rank-3 divisor
   type, sums over unboundedly many levels, or s-derivatives), and **Prop 2.3** (PROVED) kills the finite GL(k)-Eisenstein
   part (twisted d_k combinations, any k) using T1 at all square *shapes* ℓ^{2a} (prime squares alone do not suffice:
   3 − d(n)). GL(3) *cuspidal* contributions are not excluded (would need Sym^{2a} averages).
2. **Both signs are |Diff| = 1 special cycles, at the two bad fibres of X₀(2p) (Prop 4.1, PROVED; moduli reading
   Assessment).** Every word of X_p gives pure i, j with Gram T_w = t·diag(v, u) − [[1,−1],[−1,1]] (det tp); Diff(T_w) = {p}
   iff χ = −1 (Eichler level 2 in B_{p,∞}, char p) and = {2} iff χ = +1 (Eichler level p in B_{2,∞}, char 2). With an
   arithmetic Siegel–Weil formula on X₀(2p) (CONDITIONAL), the family sum is N₋^μ log p + N₊^μ log 2: SQ₅(p) ⟺ "not in ℚ·log 2"
   (transcendence-separated form). Screen: the family is a level-t Fourier projection + hyperbola restriction with t
   unbounded (B2), so the dictionary relocates the lottery to the family. Novelty modest (cf. (I)6 GZ "x = 2" shape, DIFF_DEEP).

## Results (labels)
* PROVED: Lemma 1.1 (X_n ≅ {(u,v): uv | n+u+v}; χ = (−uv/n) for gcd(uv,n)=1; |X_n| ≪ n^{1/2+ε}); Lemma 1.2 (N₋ ≥ 1 for
  n ≡ 3 (4), 5 (8); Chebotarev/Dirichlet-uniform prime certificates via q ≡ 3 (4), p ≡ −1 (q)); Lemma 2.1 (averages);
  Thm 2.2; Prop 2.3; Prop 4.1(a)–(d).
* PROVED relative to Waldspurger + twist root numbers: Prop 2.4 (no weight-3/2 eigenform has zero set {N₋ = 0}).
* CONDITIONAL: log-separation (§4), on an arithmetic Siegel–Weil formula at the bad fibres of X₀(2p) of KRY/SSY shape.
* EVIDENCE: §3 — no linear relation of 8 weighted sign counts with a 48-column dictionary (H(kn), KH sums Σ_s H(kn − js²),
  twisted σ₀/σ₁, shifted τ, six ternary theta series) on odd n ≤ 12 000 per class mod 8 (exact rank mod 2⁶¹−1);
  census cross-checked against cf_census for n ≤ 10⁵; Lemma 1.1 on all 35 184 words n ≤ 1500; Prop 4.1(b) on all 50 003
  words n ≤ 2000.
* Assessment: mock (harmonic Maass) extension of Thm 2.2 not proved; GK genus-3 reading of path lattices (2-adic
  realizability in Hom(E,E′) not checked).

## Hypotheses of STRONG_APPROX Thm 9.1 violated, and outcome
* "Finite fixed-level Eisenstein" → all holomorphic forms (cusp, any weight): dead by size (Thm 2.2).
* "Rank 2 (σ-type)" → any rank d_k: dead by T1 at square shapes (Prop 2.3).
* "n-local main term" → Waldspurger/genus-character-at-n: dead for eigenforms (Prop 2.4); GROWING_IDENTITIES (J)10 already
  covers the genus-character-at-n identity (H-B spin event).
* "Fixed level" → growing-level Kudla family (§4): exact dictionary, but the family is the divisor-in-class lottery.

## Sparks (not pursued)
* GL(3) cuspidal identities: is N₋ (or S) orthogonal to all GL(3) Maass cusp forms in a Rankin–Selberg sense? A
  Voronoi/Kuznetsov-on-GL(3) treatment of Σ_t τ_{−1,t}(tn+1) twisted by the cell character might show the "cuspidal
  part" is not an identity either (needs Sym² averages).
* Trace form: each word gives M = [[n, −A*],[A, −t]] ∈ SL₂(ℤ), i.e. a form [A, −(n+t), A*] of discriminant (n − t)² − 4
  (Pell-type discriminants as in Sarnak's Σ h(t²−4)). χ = (−A/n) is a value of that form; a Markoff/prime-geodesic style
  count over hyperbolic conjugacy classes with trace ≡ −t... unexplored.
* Zero-set fishing for combinations (not eigenforms) of weight-3/2 forms vanishing exactly on {m²} ∪ {105}: cheap
  numerics, but Prop 2.4's mechanism suggests whole classes of zeros; low prior.
* Singular moduli: certificates are the x = 4 terms of the Gross–Zagier factorization of J(−4A, −4A*) with AA* = tp + 1;
  "collisions" without the level-t condition are plentiful — the t | A+1 condition is the whole content.
