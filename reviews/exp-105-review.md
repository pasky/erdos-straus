# R253 — hostile review #1 of O239 (EXP_105.md, branch side-agent/exp-105 @ fe4ec16a)

Reviewer branch side-agent/review-exp-105-2. From-scratch scripts (no z14_/z8/ec_cover imports):
`scripts/review_r253_cert.py` (tree-certificate checker), `scripts/review_r253_closed.py` (closed-form window identities),
`scripts/review_r253_mu0.py` (generic μ = 0 window search, cross-check of Prop 2.4–Cor 2.8).

## Summary verdicts
| Claim | Verdict |
|---|---|
| Thm 2.6 — ES for every 7·4^s + 9 (59 leaves, 40 windows) | **SOUND** |
| Thm 2.2 — ES for every 3·4^s + 1 (9 leaves) | **SOUND** |
| Thm 2.3 — ES for every 3·2^m + 1 (+ cert_c6_k1) | **SOUND** |
| §2 window construction (identity, integrality, periodicity) | **SOUND** |
| Closed form of the Thm 2.2 window | SOUND (MINOR: firing set mis-stated, D3) |
| Obs 2.1 | SOUND (MINOR stale sentence elsewhere, D2) |
| Prop 2.4, Cor 2.5 | **SOUND** |
| Prop 2.7 | **SOUND** |
| Cor 2.8 (sterility of μ = 0 for the six families, z14 menu, unsplit pieces) | **SOUND** for the stated menu; the caveat's parenthetical about split numerators is unproved (MINOR D1) |
| Labels | appropriate (PROVED computer-assisted; scope "relative to the z14 window menu" stated) |
| Novelty | no prior proof of ES for 3·2^m + 1 or 7·4^s + 9 found (brief web search; Assessment) |

No FATAL or MAJOR defects.

## 1. Thm 2.6 / 2.2 / 2.3 — certificate replay (independent)

**Semantics re-derived.** Window: n = c₀4^s + k, m = c₀4^j t − k, n + m = c₀4^j(4^r + t), so x = (n+m)/4 =
c₀4^{j−1}(4^r + t) ∈ ℤ (j ≥ 1) and 4/n − 1/x = m/(nx). For d₁, d₂ | N = nx with m | d₁ + d₂:
y = (N/d₂)·(d₁+d₂)/m, z = (N/d₁)·(d₁+d₂)/m are integers and 1/y + 1/z = m/N. N = 2^E·(odd part of c₀)·n·∏Y_i,
E = 2j − 2 + v₂(c₀), with ∏Y_i = 4^r + t (cyclotomic: homogenised Φ_{2e}, e | h, h odd, h | r; SG: a⁴ + 4w⁴ with
a = 2^{r/2}; 4b⁴ + w⁴ with b = 2^{(r−1)/2}). Periodicity of all piece residues mod m on a leaf u mod L: n needs
ord_m(4) | L; code 0 needs h | L, h | u − j and ord_m(4) | L/h; codes 1/2 need ord_m(2) | L/2 and the right parity of
u − j. My checker asserts exactly these (stricter than "P | L" in z14_check, equivalent), finds its own relation (own
search over disjoint subsets × 2-power on either side), then rebuilds integer d₁, d₂ for every s and verifies.
II2/I3 (ET Prop 1.9 shapes as used in EXPONENT_COVERING) and their identities re-verified symbolically (sympy `cancel`);
D_q: q prime, ord_q(4) | L, q | n_u, ES(q) by an independent search, scaled.

**Coverage.** Tree parsed as DFS preorder of prime splits; exact Haar measure Σ 1/L = 1 (Fractions) for all three
certificates, no trailing tokens; for every s ≤ 1500 exactly one leaf contains s.

**Results** (`review_r253_cert.py c0 k cert 1500`):
* (3, 1): 9 leaves {W 3, P 3, D 2, I 1}, measure 1, explicit verified solutions for all s ≤ 1500; the leaf did not apply
  only at s = 0 (n = 4, solved by search).
* (6, 1): 2 leaves {I 1, D 1}; all s ≤ 1500; exception s = 0 (n = 7). Note the I3 leaf uses f = 3 | c₀ (n ≡ 1 mod 3
  constant) — legitimate; my first draft wrongly required q ∤ c₀.
* (7, 9): 59 leaves {W 40, P 7, D 4, I 8}, matches the text; all s ≤ 1500; exception s = 0 (n = 16).
* For s > 1500 every leaf applies generically: windows need only r = s − j ≥ 1; I3's 2-adic condition stabilises once
  2s ≥ v₂(4cd) ≤ 3; II2 positivity b > 0 holds as soon as n > a·f (all f ≤ 10⁵ here). Hence the proofs are complete.
* Mutation tests (D 11→13, one window h 9→3, one II2 prime 61→67, truncated file): all rejected.
* The author's own checker also replays (z14_check 7,9 --explicit 60: OK).

**T1 / squares.** Odd squares in the families: 7·4^s + 9 = □ ⟺ (a−3)(a+3) = 7·4^s ⟹ s ∈ {0, 2} (16, 121) — derived by
hand (coprime halves u, v with v − u = 3, uv = 7·4^{s−1}) and confirmed numerically to s < 1500; 3·2^m + 1 = □ only at
m ∈ {0, 3, 4} (4, 25, 49). Leaves: 121 (s = 2) ∈ D₁₁ (u = 2 mod 3060); 25 = 6·4 + 1 ∈ D₅; 49 = 3·16 + 1 ∈ D₇;
4, 16, 7 solved directly. No ET class is ever asked to contain a square; windows never cover them either. OK.

**Outside the ET/divisor menu.** (7, 9): c₀ = 7 odd, k = 9 ≡ 1 (8), 7 + 9 = 16 ⇒ EXP_NEAR_SQUARE Lemma 3.1 hypotheses
hold ⇒ μ = 0 is a unit-square point, no finite ET + divisor covering (via (J)22 Thm 1.4). (3, 2^m): EXPONENT_COVERING
Cor 1.5, k = 3 = 4 − 1. Both families are genuinely beyond ET + divisor coverings; the μ = 0 leaf of each certificate is
an sg1 window (m = 11 resp. 19), as Prop 2.7 predicts. Mordell-hardness: 7·4^s + 9 ≡ 121 (mod 840) for even s ≥ 2,
3·4^s + 1 ≡ 529 (mod 840) for 6 | s — both checked by hand (CRT mod 8, 3, 5, 7).
