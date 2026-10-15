# R253 — hostile review #1 of O239 (EXP_105.md, branch side-agent/exp-105 @ fe4ec16a)

**Repairs applied (R253, author quiet since fe4ec16a):** D1–D5 fixed in EXP_105.md, each marked '(R253 repair)'
(text-only; no certificate or theorem statement changed).

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

## 2. Closed form, Obs 2.1
* SG factorisation 4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1) (symbolic). Thm 2.2 window closed form: A₊A₋ = 4^{s−1} + 1,
  4x − n = 11, 1/y + 1/z = 11/(nx) — re-derived by hand and verified exactly (Fractions) at every firing even s ≤ 1500
  (`review_r253_closed.py`). Exact firing sets: 11 | nA₊ + 1 ⟺ s ≡ 0 (mod 20); 11 | nA₋ + 1 ⟺ s ≡ 10 (mod 20) (D3).
* Obs 2.1 mechanism: at μ = 0, c₀ + A₊ → c₀ + 5/2 = m/2 for (3,1,11), (7,9,19), (23,41,51) — checked by hand. OK.

## 3. Prop 2.4, Cor 2.5, Prop 2.7, Cor 2.8 — re-derived
* Prop 2.4: at s ≡ 0 (mod ord_m(4)), n ≡ 4^J, Y ≡ 4^{−j}R (R = 1 + 4^j t), m = c₀R − 4^J, so every odd q | c₀R has
  m ≡ −4^J (mod q) (hence q ∤ m: all pieces are units mod m — implicit in the text, D4) and (q/m) = (m/q)(−1)^{(q−1)/2} = 1
  (m ≡ 3 mod 4 from k ≡ 1 mod 4). (d₁d₂/m) = (−1/m) = −1 forces an odd total 2-exponent and (2/m) = −1. Correct.
* Cor 2.5: J ≥ 2, k ≡ 1 (8) ⇒ c₀ ≡ 7 (8); j ≥ 2 ⇒ m ≡ 7 (8); j = 1: E = 0, t odd ⇒ no 2-power piece at all
  (4^r + t odd), t even ⇒ m ≡ 7 (8). Correct.
* Prop 2.7: cyclotomic: class ⊂ {s ≡ j mod h}, μ = 0 needs h | j; Y_e homogeneous of degree φ(2e) ⇒
  Y_e(4^{−j/h}, w) = 4^{−jφ(2e)/h}·Y_e(1, w4^{j/h}), the integer factors divide 1 + t4^j = R. 'sg' needs j even, pieces
  2^{−j}·(divisor of R); 'sg1' pieces 2^{−j}·(divisor of R = 1 + 4^j w⁴), j odd, (2/m) = −1 only for j = 1, w odd. Small
  primes splitting n never occur at μ = 0 (n → 4^J). Correct.
* Cross-check (`review_r253_mu0.py`, generic search over the whole menu j ≤ 7, w ≤ 9, h ∈ {1,3,5,7,9,15}, sg, sg1, with
  all piece limits at μ = 0 and free 2^i, |i| ≤ 2j − 2): for (15,1), (31,33), (7,57), (63,1), (47,17), (55,9) **no**
  relation among 159–162 windows containing μ = 0; for (3,1), (7,9), (23,41), (39,25) exactly one: sg1, j = 1, w = 1
  (m = 11, 19, 51, 131). Every hit has the Prop 2.7 survivor shape.
* Cor 2.8: the reduction (exactly one A-atom by Jacobi; relation (2w² ± 2w + 1)U + 2V ≡ 0 with UV | c₀4^J and
  aU + 2V ≤ (a + 2)UV) re-derived; the magnitude bound holds from w ≥ 4 for (15,1) and w ≥ 7 for the five J = 3 families,
  so my generic search (w ≤ 9) covers the finite part independently. Conclusion "no finite covering by ET + divisor +
  z14 window classes" follows (finite union of clopen classes covering {s ≥ s₀} is closed, hence = Ẑ ∋ 0; μ = 0 is
  outside every ET/divisor class by EXP_NEAR_SQUARE Lemma 3.1, hypotheses checked: c₀ odd, k ≡ 1 (8), c₀ + k ∈ {16, 64}).
  SOUND for the stated menu.

## 4. Defects (all MINOR; no FATAL, no MAJOR)
**D1 (MINOR) — Cor 2.8 caveat, "(the magnitude bound still applies to such sub-products; …)".** False as a general
statement: once the SG numerators are split by fixed primes, the side carrying no "½" may contain primes of *both*
numerators (only one ½-carrying remainder may be used, the other A's split-off primes are free), so D₁D₂ can reach
c₀4^J·R = 4^J(m + 4^J) > m; the bound gives nothing (note c₀R ≡ 4^J mod m). *Evidence:* my Part B search (split
numerators, relation D₁ + 2D₂ ≡ 0) finds no relation for odd w ≤ 201 in all six families. *Repair:* replace the
parenthetical by "(the magnitude bound does NOT cover sub-products mixing primes of both numerators; EVIDENCE: no relation
for odd w ≤ 201, R253)".
**D2 (MINOR) — Thm 2.2 "Significance".** "(the Aurifeuille/Sophie-Germain factorisation of 4^r + 1 plus the n-piece)"
contradicts the corrected mechanism of Obs 2.1 (n-piece not needed). *Repair:* delete "plus the n-piece".
**D3 (MINOR) — closed form of the Thm 2.2 window.** "If 11 | nA₊ + 1 (e.g. s ≡ 0 mod 60) … (s ≡ 30 mod 60)": the exact
conditions are s ≡ 0 (mod 20) resp. s ≡ 10 (mod 20) (s ≡ 0/30 mod 60 are the certificate's leaf classes). *Repair:* state
the mod-20 conditions.
**D4 (MINOR) — Prop 2.4 proof.** Jacobi symbols of pieces presuppose gcd(piece, m) = 1; add "(in particular q ∤ m, so all
pieces are units mod m)". Also "k ≡ 1 (mod 8)" is more than needed for m ≡ 3 (4) (k ≡ 1 mod 4 suffices); harmless.
**D5 (MINOR) — Novelty not stated.** Brief web search (Jina) found no prior proof of ES for 3·2^m + 1 or 7·4^s + 9;
suggest adding "Novelty: no prior result found (Assessment)".

## 5. Not checked / limits
* ET Prop 1.9 itself: I used the II2/I3 identities as written and verified them symbolically; their attribution to ET
  was not re-read in the PDF (not needed — the identities are self-verifying).
* My checker trusts sympy `isprime`, `n_order`, `factorint` (small arguments) and `cyclotomic_poly` coefficients; piece
  products are re-verified as exact integers at every s ≤ 1500, so `cyclotomic_poly` is effectively verified.
