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
| Table 1 / Lemma 2.1 | **SOUND** | compared line by line with ET arXiv v6 Prop. 1.9 and the \S10 parametrisations (sources/elsholtz-tao-1107.1010.pdf): classes, side conditions and coordinates agree (I1 b=(ne+1)/(4ad) = ET's ((n+f)/4ad)e−a). Both equivalences and positivity for all n≥1 re-derived. |
| Lemma 2.2 (i),(ii) | **SOUND** | re-derived step by step (Type I: e=(a+b)/c, 4abd=ne+1, e≡3 (4), (q/e)=1 vs (ab/e)=−1 ⇒ 2|ab ⇒ e≡7 (8); Type II: e=4abd−n, ce=a+b, same chain; gcd(ab,e)=1 because p|e,a ⇒ p|n). Only gcd(ab,n)=1 is used in (ii) (hypothesis gcd(abd,n)=1 is stronger than needed — harmless). Brute force (`review_r291_limits.py` (1)): no Type I/II point with a,b,c<45 for every odd square 9..841; positive controls 17,33,41,57,65,73 do have points. ET's own §4 indeed omits Type II ("we omit the details") — attribution correct. |
| Cor 2.3 | **SOUND** | the gcd bookkeeping per family re-derived (I1: 4ad·c=n+f; II1: 4ab·d=n+e; II2: fb=nc+a; II3: 4ad·b=n+e). Brute force: 458 065 pairs (admissible κ with entries ≤8,8,39; odd t<400 with gcd(t,P_κ)=1): t² never in the class. |
| Lemma 2.5 (rule period), 2.6 (compactness) | SOUND | standard. |
| Thm 2.7 (sterility) | **SOUND** | CRT choice of t checked (t≡2^J mod M', t²≡k mod 2^a, t≡1 at the other primes of P_κ); M(κ) | M so t² is in the class; divisor-class case correct. No Mordell/Schinzel dependence remains. |
| Prop 2.8 (integer unit-square points) | SOUND | all three cases (ℓ>0, ℓ=0, ℓ<0) and the c₀≡2 (4) case re-derived. |
| Rem 2.9 / screen for 4^s+105 | SOUND (as EVIDENCE/certified screen) | `review_r291_misc.py`: the 28 primes q<3·10⁶ with ord_q(4)|360 give a witness (q|n_s or (n_s/q)=−1) for every s mod 360. |
| Lemma 3.1 window (a),(b) | **SOUND** | (b) valuation case split re-derived; gcd(m,d)=1 follows from gcd(m,x)=1, d|x². |
| (SG),(CY),(BI) | SOUND | (BI) expansion (4abd−n)(4acd−1)=4ad(4abcd−b−cn)+n checked; CY: Σ_{e|h}φ(2e)=h for odd h. |
| Lemma 3.3 specialisation | SOUND | both directions; the worked example (15/4, 5/2, 1/2, 55/8) checked. |

### D. Section 5.1: Theorem W and its lemma chain

| claim | verdict | notes |
|---|---|---|
| Remark after Def 5.1 (rules → root families; rational functions) | SOUND | shift: on all large multiples of P one has σ|P, σ|s₀, so Y=2^{-ωt₀}·Y' with Y'=2^{s/D}; remainder argument correct. |
| Lemma 5.2 (reduction) | **SOUND** | resultant ⇒ constant gcd h on a shrunk C; m odd, gcd(m,N(Y))=1 near μ=0 (n≡n+m≡4^J mod p); polynomial divisibility by vanishing remainder (bounded denominators, R₀/(d₁d₂)→0). |
| Lemma 5.3 (Jacobi at the limit) | **SOUND** | ρ₁ρ₂ρ₃=4^{J−1}M; (q/m)=1 for q|M by reciprocity with m≡3 (4); (2/m)^{e₁−e₂}=−1. |
| Lemma 5.4 (2-adic size) | **SOUND** | v₂(k+m)=2 since m≡3 (8); roots of x have v₂=2/D; e_i=−2δ_i+2Jε_i. |
| Lemma 5.5 (Capelli) | **SOUND** | Lang, Algebra VI Thm 9.1 is exactly Capelli's criterion (X^n−a irreducible iff a∉K^p for p|n and a∉−4K⁴ if 4|n); application re-derived (−K<0 excludes p=2, v₂(K)=2 excludes odd p, u⁴|c₀ ⇒ u=1). |
| Lemma 5.6 (magnitude) | **SOUND** | both cases re-derived; note r=M/m is not an integer (harmless). |
| Thm 5.7 (Thm W) | **SOUND** | assembly correct (some δ_i=½ with i∈{1,2} because 2Jε_i is even). |
| Computation 5.8 | **SOUND (re-computed)** | own enumeration (`review_r291_limits.py` (3)): hypotheses hold (c₀ 4th-power-free; k/c₀ not a p-th power, not in 4Q⁴); w_max = 3,5,9,5,5,5 exactly as stated; **no relation** for the six families (parity of e₁−e₂ not imposed); controls give m = 11, 19, 51, 131 and (5/2, 7) for (7,9). (My first run reported 8 \"relations\" for (7,57) — all at w=1, m=28−57=−29<0, i.e. outside the theorem; the paper correctly restricts to 0<m.) |
| Cor 5.9 (constant ratio) | **SOUND** | λ_i ∈ Z_(2)∩Z[1/2]=Z; t odd/even cases re-derived. |
| Cor 5.10 (no covering) | SOUND | via Lemma 2.6 + the Remark after Def 5.1. |

So the whole chain re-derives without gaps under its stated hypotheses (polynomial x,y,z in a single
root 2^{s/D}, constant gap or constant ratio).

## Defects

(numbered; FATAL / MAJOR / MINOR)

### E. Section 5.2: the family 15·2^s+1 beyond Prop 5.12

| claim | verdict | notes |
|---|---|---|
| Lemma 5.13 (limit conditions for (BI)) | **SOUND** | f′ constant ⇒ c constant ⇒ b=(cn+a)/f′ is exactly II2(a,d,f′) (f′+1=4acd, and f′ | cn+a ⇔ f′ | n+4a²d since gcd(4ad,f′)=1) ⇒ excluded by Thm 2.7; f constant ⇒ constant gap ⇒ Thm W/Comp 5.8. Capelli step, v=1, u≥3, u≡3 (4) (15≡−1 (8), u^p≡u (8)) re-derived. (C2): X=4ad·b(1)−16 ∈ Z_(ℓ) with ℓ^{v_ℓ(ad)} | X+16; 2-adic: roots of n+4a²d are 2-adic units so v₂(X)≥v₂(f(0))≥0; XX′=16+4a²d. All correct. |
| Lemma 5.14 (boxed equation) | **SOUND** | the new bounds re-derived case by case (m₂=1: a≤21, m₁≤100, P≤120; m₂≥2, P≥5: a≤6, P≤36; P=1,2,3,4: a≤81,25,29,9). Own enumeration in the box a,m₁<3000 (d bounded by m₂≥1): exactly **39** solutions; 31 with a,d odd; 15 | 4a²d+1 only at (1,11), quotient 3. Actual maxima: a=81, m₁=36, m₁d=40 (the stated 100/120 are a-priori bounds, true). |
| Thm 5.15 | **SOUND** (as a statement about the menu (BI) with b, c themselves integer-valued) | u≡3 (8) ⇒ 4a²d≡4 (8) ⇒ a,d odd, q=ad; X=m₁ad−16, X′=m₂ad−1, m_i≥1; expansion to a(m₁m₂d−4)=m₁+16m₂ checked. Sanity: for c₀=63 the u≡3 (8) branch is inhabited by Lemma 4.3 (u=3, a=5, d=17 odd, X=21, X′=84), consistent. |
| Rem 5.16 (integrality hypothesis) | SOUND | (a,b,c,d)↦(a/h,b/h,c/h,h²d) preserves x,y,z and the Type II identity (both sides scale by 1/h); h=5 on Lemma 4.3 gives a=1, d=425, b(1)=c(1)=1/20 — checked. The scope caveat is stated honestly in the lemma, the theorem and the abstract ("one branch of the moving-gap binomial menu"). |
| Rem 5.17 (open branch) | EVIDENCE/Assessment — OK, but see m3 | |

### F. Side claims (Remarks), checked by `review_r291_misc.py`

All correct: Rem 4.2(iii) (3·2^s+1 Mordell-hard iff 12|s, then 529 mod 840; prime list s=1,…,189);
Rem 4.5 (63·2^s+1 Mordell-hard iff 4|s; only squares s=0,8 — also re-derived by hand); 7·4^s+9 even s≥2
≡121; 15·2^s+1, 3|s ⇒ ≡121; Rem 4.11 (k≡9 (24) list; k∈{9,81,129,201,249} never Mordell-hard for s≥2;
k=153 Mordell-hard exactly at s≡2 (6), covered by D₁₃); 4^s+105 square points; Rem 4.10(i) (q=18837001
prime, ord_q(4)=45, (n_s/q)=−1 on s≡34 (45)); 10^18 thresholds (s≤53, s≤29).
ET p. 6 quote ("a finite set of covering congruence strategies") verified in the arXiv PDF.
Not accessed by me: Mihnea–Dumitru (arXiv:2509.00128), Salez, Yamamoto, Lang (Capelli statement checked
from memory of the standard statement), Izotov/FFK.
