# R291 — hostile review #1 of `paper/es-exponential-families.tex` (O277)

Reviewer: side agent R291 (branch `side-agent/review-expfam-1`), merged author branch
`side-agent/paper-expfam` at 0ffd6163/3dbd5c00. Numbering below follows the compiled paper
(Lemma 2.1 = lem:solve, Lemma 2.2 = lem:T1, Cor 2.3, Thm 2.7 = thm:sterile, …, Prop 5.12 =
prop:15half, Lemma 5.13 = lem:iiadlimit, Lemma 5.14 = lem:boxed, Thm 5.15 = thm:iiad3,
Remark 5.16 = rem:iiadhyp).

From-scratch scripts: `scripts/review_r291_*.py` (no code shared with `c1_expfam_verify.py`).

## Status: IN PROGRESS

## Summary verdicts per claim

### A. Certificates (main theorems) — re-checked by from-scratch code

Scripts: `review_r291_et.py` (ET classes transcribed directly from ET Prop. 1.9 / §10, not
from the paper's Table 1; membership = the ET *congruences*, not mere integrality of x,y,z),
`review_r291_tables.py` (hand-transcribed Tables 3, 6, 7, 8), `review_r291_poly.py` (own
exact Q[Y] arithmetic + root-rule period/threshold derivation), `review_r291_rules.py`
(Thm 4.1, Rem 4.2(ii), Lemma 4.3, Lemma 4.8), `review_r291_c7.py` (Thm 4.6).
For every rule: identity 4xyz = n(xy+yz+zx) checked in Q[Y]; exact set of exponent
residues derived over one full period beyond a (conservative) 2-adic + Cauchy-bound
positivity threshold; claimed residues ⊆ derived residues; coverage of all residues mod the
lcm; and *every* s ≤ 200–300 solved by direct big-integer evaluation of some rule (this also
disposes of all s below my conservative thresholds).

| claim | verdict | notes |
|---|---|---|
| Thm 4.1 (3·2^s+1) | **SOUND** | 4 SG rules: derived X-residues exactly {4,6},{2,3},{8,9},{5,7} mod 11 (s-classes {0,12},{8,36},{16,28},{20,32} mod 40); 6 Step-2 identities verified; uncovered mod 120: none; all 1≤s≤300 solved; hand coverage argument re-derived (correct). |
| Rem 4.2(ii) cubic Type II | SOUND | derived s≡0,12 (mod 36), threshold s≥36 (s=12 fails, as stated). |
| Lemma 4.3 (63, s≡0 mod 24) | **SOUND** | b, c themselves integral (not just x,y,z); fails at s=0 as stated; checked s≤2000. |
| Thm 4.4 (63·2^s+1) | **SOUND** | 18 classes admissible, each claimed exponent class ⊆ ET-congruence-derived class (no class relies on integrality-only cancellation); uncovered mod 2520 = {0,840,1680}; all 1≤s≤300, s≢0 (24), solved by a table class. |
| Thm 4.6 (7·4^s+9) | **SOUND** | 22 windows (pieces, d₁,d₂ | N as polynomials, (d₁+d₂)/m integral) + 11 ET classes; lcm 9180, uncovered: none; all 1≤s≤200 solved by direct evaluation. |
| Lemma 4.8 (4^s+105 window) | **SOUND** | identity, A integral, derived class exactly s≡34 (45). |
| Thm 4.9 (4^s+105) | **SOUND** | 13 classes; uncovered mod 180 = {34,124} ⊂ {s≡34 (45)}; all 0≤s≤300 solved. |
| Thm 4.10 (nine 4^s+k) | **SOUND** | all nine tables cover all residues; every class ET-congruence-valid; s=0..300 solved. |
| **Prop 5.12 (15·2^s+1, 60∤s)** | **SOUND** | see §B. |

### B. Proposition 5.12 (new) — independent re-derivation

By hand: ord₇(2)=3; s≡1 (3): n≡2·15+1≡3 (7) → II2(1,1,7) [4ad=4 | 8, class −4≡3]; s≡2 (3):
n≡61≡5 (7) → II2(2,1,7) [8 | 8, −16≡5]. For 3|s: ord₃₁(2)=5, s≡1 (5) gives n≡31≡0, s≡2 (5)
gives n≡61≡30 = −4·1·8 (31) [II2(1,8,31): 32 | 32]. ord₁₁(2)=10: s≡3,4,5 (10) give n≡121≡0,
241≡10=−12 [II2(1,3,11): 12|12], 481≡8=−36 [II2(3,1,11): 12|12]. II2(1,5,99): 20 | 100, class
−20≡79 (99); n≡2 (11) at s≡8 (10) and n≡7 (9) for *every even* s (15·2^s≡6 (9) for even s), so
the class is s≡8 (10) unconditionally (period 30 collapses to 10). Remaining for 3|s:
s≡0,9 (10) → s≡0,9,30,39 (60). II2(2,5,39): 40|40, class −80≡37 (39), ord₃₉(2)=12,
2⁹≡5 (39), 15·5+1=76≡37 ✓ → s≡9 (12) ⊇ s≡9 (60). II2(1,3,287): 12 | 288, class −12≡275;
II2(1,24,287): 96 | 288, class −96≡191; ord₂₈₇(2)=lcm(3,20)=60; my code derives exactly
s≡39 resp. s≡30 (60). Left: s≡0 (60). All II2 coordinates are positive for n≥1 and the
moduli are odd, so no thresholds. Code (`review_r291_tables.py`): all 11 classes admissible,
claimed ⊆ derived, uncovered mod 60 = {0}, every 1≤s≤300 with 60∤s solved exactly.
Verdict **SOUND**. (The statement says s≥1; s=0, n=16, is trivially fine but 60|0 anyway.)

The paper's text "(there $n\equiv3,5\pmod 7$)" and the hand argument are correct as written.

## Defects

(numbered; FATAL / MAJOR / MINOR)
