# Referee report R36 — paper/sieve-limits-note.tex v4 (+ es-threequarter-note sharpness remark)

Referee: hostile side agent R36 (branch side-agent/referee-sieve-v4), reviewing
side-agent/sieve-paper-v4 at ef5ae01. Change list: reviews/agent-reports/AGENT_REPORT_O36.md.

## Compile

* `pdflatex` ×3 on sieve-limits-note.tex: 62 pp., no undefined refs/citations, no multiply-defined
  labels; one 1.29pt overfull hbox (lines 3406–3413). es-threequarter-note.tex: 22 pp., clean.

## Summary verdicts (filled in progressively)

(in progress)

## Numbered points

(in progress)

### Claim 1 — §10 local-weight first moments (Lemmas 10.4–10.6, 10.8, 10.9; Rem 10.7): SOUND

Re-derived line by line:
* L 10.4 (localweight): exact identity for p^{v}≤y, S_y squarefull since p≤y<p^v; the
  (2Z/u)^k form follows with (Y,T)=(K,K^{1/2}). OK.
* L 10.5 (Zmoments): partition-by-prime argument, #{ν∈ℕ^m: max ν=t}≤m t^{m-1}, p^{-t}≤p^{-1}2^{1-t}. OK.
* L 10.6 (smoothR): checked Shiu's Thm 1 against sources/shiu-1980.pdf p.163 (scan, read as
  image): f∈M ((i) f(p^l)≤A_1^l, (ii) f(n)≤A_2(ε)n^ε), 0<α,β<1/2, 0<a<k, (a,k)=1,
  k<y^{1-α}, x^β<y≤x, x→∞. The application (x=V=(2K+1)/4, y=Y=K/4, k=q∈[2,K^{1/2}],
  class 4^{-1} mod q reduced since q odd) satisfies all of them for K≥64. Divisor
  expansion D|M, e|M ⇒ lcm(D,e)|M correct; Euler-product bound Σ_e h(e)/lcm(D,e)≤c_1Γ(D)/D and
  the Rankin tail (2^k from ω(D)≤k; h(p)p^{1/4}≤1 for p>W≥16) correct. y^{16k}≤K gives
  lcm≤K^{1/2}. OK.
* Rem 10.7: read ElT pp. 29–32 (sources/elsholtz-tao-1107.1010.pdf). Confirmed: (a) the
  proof of (7.10) (reduction to odd a,m; ranges q<A, A≤q≤kA, q>kA) never uses k≪(AB)^{O(1)} —
  the 2^l-absorption into k costs Σ_l 2^{-l}(log(1+k)+l)=O(log(1+k)), uniform; (b) slip (i) is
  real: a↦(−ka/q)1_{(a,2q)=1} is principal for square q; (c) slip (ii) is real: ElT's
  c(q)=(−1)^{(q−1)/2+m(q²−1)/8} omits (−1)^{((q−1)/2)((k'a−1)/2)}; the corrected q-function is
  the character (−ka/·) restricted to odd q, non-principal because −ka<0 cannot be (±)square
  times 2-power making it trivial (checked the cases |D|=2^e n² f). Period 8k'a≤8kA≤8q gives
  O(log B) per a uniformly. OK.
* L 10.8 (smoothA): (i) r≥K^{1/4}: (Y,T)=(K^{1/4},K^{1/8}) ⇒ Z≥u/8; R'≥K^{1/8},
  a=4h²L≤16K^{13/8}≤R'^{14}, Cor 7.4 with b=1. (ii) r<K^{1/4}: (Y,T)=(K^{3/4},K^{1/4}) ⇒ Z≥u/2;
  P=4rL²n²+1, ρ_P(p^j)=0 for p|2rL, ≤2 otherwise (Hensel), ρ_P≤ρ_{4r}; Thm 7.1 hypotheses
  (nonneg. integer coefficients ≤N², N>1, ρ(p^j)≤C) hold — checked against ElT p.28 statement;
  (7.10) with k=4s, A=2R, B=2K. Σ_s h(s)log(1+4s)/s<∞. OK.
* L 10.9 (firstnoB): tail summation (log 2K)²≤4u_t²(log y)² checks (the constant
  C_4/(8 log 2) is right up to a harmless factor from t_0−1 vs t_0); (a,D) multiplicity
  ≤2^{ω(g)} and Γ(4ag)/(4ag)≤2Γ(a)Γ(g)/(ag) OK.
Label "PROVED; Case A PROVED mod ElT Prop 1.4, Thm 7.1, Cor 7.4, (7.10)" is accurate.
* From-scratch numerics (scripts/review_r36_checks.py, EVIDENCE): (1) L 10.4 inequality holds
  for all y-smooth m≤2·10⁴, y∈{2,…,30} (equality up to 2e-15 rounding when S_y=1); (2) slip (ii):
  over 109 060 triples (k≤40, odd a≤40, q<400) ElT's c(q)(q/k'a) disagrees with (−ka/q) in
  27 167 cases, the corrected sign in 0 — the slip is real and the repair right; (3) (7.10) ratio
  Σ_{a≤30}Σ_{m≤3000}ρ_{ka}(m)/m ÷ (A log B log(1+k)) decreases from 0.93 (k=1) to 0.05
  (k≈2·10⁴): no sign of non-uniformity in k.

### Claim 2 — Thm 10.12 (noBcap), Thm 10.13 (Bcapall), Thm 10.14 (main): SOUND

* Thm 10.12 ledger re-checked: singletons (8/3)K₃′s₁³=(8/3)K₃′λ^{3/4}; blocks E m_V≤8K₃′s³,
  d_i≥λ/(2s) ⇒ ratio ≤16K₃′·16^i+4, Σ_i (λ/2^is₁)(c₁+i log16)=O(λ^{3/4}); O(log λ) blocks ⇒
  O(log²λ). Matches KA3 Thm 4.1 line by line; the needed y≥y₀(W) holds as e^{s₁}→∞.
* Thm 10.14: the proof (projection + Lemma budget with Λ₀=A log N, λ=(A+2)log N) is the v3 proof
  unchanged except for the cap; it differs from KA3 Cor 4.2's route (ET Lemma 2.9 case
  analysis) but is self-contained in this note and was refereed in v3. Statement matches KA3
  Cor 4.2 (no B, family primes ≤N^A, Σ|a_i|<N, whole-avoider majorant). The ω(N)→∞ corollary
  follows. No overclaim.
* Labels: header "PROVED; Case A PROVED mod ElT Prop 1.4, Thm 7.1, Cor 7.4, (7.10)". KA3's own
  label is "PROVED given K2/EK as reviewed"; the §10 opening paragraph states this proviso
  explicitly. Acceptable (see minor point M1 below for a suggestion).
* Thm 10.13 retained with only Prop 1.4 — consistent and correctly motivated.
