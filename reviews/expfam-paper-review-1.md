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

### C. Section 2 (classes, odd squares, sterility) and Section 3 (windows)

| claim | verdict | notes |
|---|---|---|
| Table 1 / Lemma 2.1 | **SOUND** | compared line by line with ET arXiv v6 Prop. 1.9 and the \S10 parametrisations (sources/elsholtz-tao-1107.1010.pdf): classes, side conditions and coordinates agree (I1 b=(ne+1)/(4ad) = ET's ((n+f)/4ad)e\u2212a). Both equivalences and positivity for all n\u22651 re-derived. |
| Lemma 2.2 (i),(ii) | **SOUND** | re-derived step by step (Type I: e=(a+b)/c, 4abd=ne+1, e\u22613 (4), (q/e)=1 vs (ab/e)=\u22121 \u21d2 2|ab \u21d2 e\u22617 (8); Type II: e=4abd\u2212n, ce=a+b, same chain; gcd(ab,e)=1 because p|e,a \u21d2 p|n). Only gcd(ab,n)=1 is used in (ii) (hypothesis gcd(abd,n)=1 is stronger than needed \u2014 harmless). Brute force (`review_r291_limits.py` (1)): no Type I/II point with a,b,c<45 for every odd square 9..841; positive controls 17,33,41,57,65,73 do have points. ET's own \u00a74 indeed omits Type II ("we omit the details") \u2014 attribution correct. |
| Cor 2.3 | **SOUND** | the gcd bookkeeping per family re-derived (I1: 4ad\u00b7c=n+f; II1: 4ab\u00b7d=n+e; II2: fb=nc+a; II3: 4ad\u00b7b=n+e). Brute force: 458\u202f065 pairs (admissible \u03ba with entries \u22648,8,39; odd t<400 with gcd(t,P_\u03ba)=1): t\u00b2 never in the class. |
| Lemma 2.5 (rule period), 2.6 (compactness) | SOUND | standard. |
| Thm 2.7 (sterility) | **SOUND** | CRT choice of t checked (t\u22612^J mod M', t\u00b2\u2261k mod 2^a, t\u22611 at the other primes of P_\u03ba); M(\u03ba) | M so t\u00b2 is in the class; divisor-class case correct. No Mordell/Schinzel dependence remains. |
| Prop 2.8 (integer unit-square points) | SOUND | all three cases (\u2113>0, \u2113=0, \u2113<0) and the c\u2080\u22612 (4) case re-derived. |
| Rem 2.9 / screen for 4^s+105 | SOUND (as EVIDENCE/certified screen) | `review_r291_misc.py`: the 28 primes q<3\u00b710\u2076 with ord_q(4)|360 give a witness (q|n_s or (n_s/q)=\u22121) for every s mod 360. |
| Lemma 3.1 window (a),(b) | **SOUND** | (b) valuation case split re-derived; gcd(m,d)=1 follows from gcd(m,x)=1, d|x\u00b2. |
| (SG),(CY),(BI) | SOUND | (BI) expansion (4abd\u2212n)(4acd\u22121)=4ad(4abcd\u2212b\u2212cn)+n checked; CY: \u03a3_{e|h}\u03c6(2e)=h for odd h. |
| Lemma 3.3 specialisation | SOUND | both directions; the worked example (15/4, 5/2, 1/2, 55/8) checked. |

### D. Section 5.1: Theorem W and its lemma chain

| claim | verdict | notes |
|---|---|---|
| Remark after Def 5.1 (rules \u2192 root families; rational functions) | SOUND | shift: on all large multiples of P one has \u03c3|P, \u03c3|s\u2080, so Y=2^{-\u03c9t\u2080}\u00b7Y' with Y'=2^{s/D}; remainder argument correct. |
| Lemma 5.2 (reduction) | **SOUND** | resultant \u21d2 constant gcd h on a shrunk C; m odd, gcd(m,N(Y))=1 near \u03bc=0 (n\u2261n+m\u22614^J mod p); polynomial divisibility by vanishing remainder (bounded denominators, R\u2080/(d\u2081d\u2082)\u21920). |
| Lemma 5.3 (Jacobi at the limit) | **SOUND** | \u03c1\u2081\u03c1\u2082\u03c1\u2083=4^{J\u22121}M; (q/m)=1 for q|M by reciprocity with m\u22613 (4); (2/m)^{e\u2081\u2212e\u2082}=\u22121. |
| Lemma 5.4 (2-adic size) | **SOUND** | v\u2082(k+m)=2 since m\u22613 (8); roots of x have v\u2082=2/D; e_i=\u22122\u03b4_i+2J\u03b5_i. |
| Lemma 5.5 (Capelli) | **SOUND** | Lang, Algebra VI Thm 9.1 is exactly Capelli's criterion (X^n\u2212a irreducible iff a\u2209K^p for p|n and a\u2209\u22124K\u2074 if 4|n); application re-derived (\u2212K<0 excludes p=2, v\u2082(K)=2 excludes odd p, u\u2074|c\u2080 \u21d2 u=1). |
| Lemma 5.6 (magnitude) | **SOUND** | both cases re-derived; note r=M/m is not an integer (harmless). |
| Thm 5.7 (Thm W) | **SOUND** | assembly correct (some \u03b4_i=\u00bd with i\u2208{1,2} because 2J\u03b5_i is even). |
| Computation 5.8 | **SOUND (re-computed)** | own enumeration (`review_r291_limits.py` (3)): hypotheses hold (c\u2080 4th-power-free; k/c\u2080 not a p-th power, not in 4Q\u2074); w_max = 3,5,9,5,5,5 exactly as stated; **no relation** for the six families (parity of e\u2081\u2212e\u2082 not imposed); controls give m = 11, 19, 51, 131 and (5/2, 7) for (7,9). (My first run reported 8 \"relations\" for (7,57) \u2014 all at w=1, m=28\u221257=\u221229<0, i.e. outside the theorem; the paper correctly restricts to 0<m.) |
| Cor 5.9 (constant ratio) | **SOUND** | \u03bb_i \u2208 Z_(2)\u2229Z[1/2]=Z; t odd/even cases re-derived. |
| Cor 5.10 (no covering) | SOUND | via Lemma 2.6 + the Remark after Def 5.1. |

So the whole chain re-derives without gaps under its stated hypotheses (polynomial x,y,z in a single
root 2^{s/D}, constant gap or constant ratio).

## Defects

(numbered; FATAL / MAJOR / MINOR)
