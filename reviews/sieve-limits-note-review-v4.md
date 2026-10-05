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

### Claim 3 — §14 (large sieves, prime laws, interval counts, hybrids): SOUND-AFTER-REPAIRS

Method: statement-by-statement comparison with LS, LS2 (incl. its "Update (KARY3, (D)24)"
header), PL, IF, IF2, KA3 §4.3 and the reviews (done with a research assistant; every defect
listed below was re-verified by me in the tex/source). Re-derived myself: Thm 14.1 (duality via
Cauchy–Schwarz + minimax, w_θ≤1/N ⇒ Parseval), Thm 14.2 (fibre lift, B≥⌊N/Q₀⌋Q₀Eν≥(N/2)Eν,
λ≤3A log N), Lemma 14.4 (LP duality; ν≥1_A forces ν≥0, so Thm 10.12 applies), Lemma 14.18
(sign rule: β*−a·c = |a|·1[wrong]; and the N=20 example: 1[7|n]−1[3∤n]+1[(n,21)=1]=1[21|n],
hybrid charge (2−14)+12=0). All statements match their sources in hypotheses, constants and
exponents (24 log log 3Q + C, 26 log log N + C; band family η=1/9, R=324; log(2+12c); etc.).
* The λ^{3/4} substitution ("PROVED via Theorem 10.12") is valid for every integer-measure result:
  in LS Thm 3.1, LS2 L1.1/Thms 2.4, 4.2, 9.1/Prop 5.1 and IF Cor 2.3/Thm 2.5 the K2 cap enters
  only as a black-box lower bound on Eν (resp. m*). Citation is incomplete though (point m3).
* Unit-measure results (Thm 14.12 PLcap, Lemma 14.4 units part, Thm 14.6 LSprimes) are honestly
  stated with (log λ)^{3/4} / (log log N)^{3/4} and "pointer level" for the improvement. But the
  abstract does not respect this (point M1).
* Thm 14.20 (hybridcap) is correctly labelled "PROVED implication, CONDITIONAL on Flat". The
  added "observation" (black-box use ⇒ C(log N)^{3/4}) is correct: in IF2's proof the cap enters
  only through log(1/Eν) after coarsening at level ≤(A+A₁+2)log N+S+λ₀, and the bootstrap
  S≥K log N ⇒ λ≤2S+λ₀ ⇒ S=O(1) closes it.
* Thm 14.7 (Gallagher) "unconditional" and dependency list (Shiu, Mertens, no ElT) match LS2
  Thm 4.3 / Rem (a).

### Claim 4 — §15 (tuple counts, truncated weights, forced zeros): SOUND-AFTER-REPAIRS

Same method (TU, TU2, KA3 §§5, 7, KA2, (D)21/(D)24/(D)25). Re-derived: Cor 15.8 (classorder):
a nonempty intersection of ≤k classes with moduli ≤N^A is one class mod an lcm ≤N^{kA}, level
≤kA log N, so Thm 10.12 at λ=max(kA log N, λ₀) gives the stated bound — the subagent-written
proof is correct and the label is earned by the note's own proof (KA3 §4.3 only points to it).
Lemma 15.15 (packing): next-fit bins give b_i b_{i+1}>Z, d>Z^{⌊m/2⌋} ⇒ m≤k−1, coprime bins ⇒
CRT — correct. Thm 15.3 constants (e+2, 2/e²) and Thm 15.20 constants (e+3, 2e+2) match TU/TU2.
Git history confirms KA3 Lemma 7.2 postdates R28, so "coordinator-checked only" is accurate.
Literal TC_θ being false is presented only as an Assessment. Defects in m8–m14 below.

## Defects (numbered; MAJOR = M, MINOR = m)

**M1 (MAJOR, presentation/overclaim; abstract l. 66–72 and intro item 6, l. 221–226).** The
abstract says "The cap [O_A((log N)^{3/4})] extends to … the large sieve for primes, … to
majorants positive only at primes, … and to tuple-count input of bounded or prime order." For
the prime-measure results the note itself proves only C_A(log N)^{3/4}(log log N)^{3/4}
(Thm 14.6 LSprimes, Thm 14.12 PLcap); the (log N)^{3/4} form is "pointer level only" (§14
preamble l. 2786–2791, KA3 §4.3 "not re-reviewed"). Intro item 6 likewise says "likewise … the
large sieve for primes (Theorem 14.6)" right after "capped at C_A(log N)^{3/4}". For prime order k
the cap is C_A[(log N)^{3/4}+k log log N] (Cor 15.12), not O((log N)^{3/4}). Since the whole
point of v4 is removing a (log log N)^{3/4} factor, the abstract must not blur it.
*Repair:* abstract: "…(twisted, multiplicative, hybrid and fibrewise forms); the large sieve
for primes and majorants positive only at primes are capped at O_A((log N)^{3/4}(log log N)^{3/4})
(and at O_A((log N)^{3/4}) at pointer level); …; tuple-count input of bounded order, and of prime
order k at O_A((log N)^{3/4}+k log log N)". Same in intro item 6.

**m1 (§14 preamble l. 2772).** "No review found a fatal or major defect" is false: the IF review
(reviews/exceptional-interfreq-review.md l. 91) has **D1 (MAJOR, scope)** (hybrids overclaimed;
repaired by restriction), and the LS review has D1 "moderate". *Repair:* "No review found a
fatal defect; the IF review found one major scope overclaim (hybrids), repaired by restricting
the claim (Rem 2.6 of IF, and §14.6 here); the other repairs were minor."

**m2 (Thm 14.7 proof sketch, l. 2988).** "at p≤W, χ²≤7, and Mertens gives 3 log W" does not
follow (7 per prime would give 7 log W). Source: χ²=(p+1)/(p−1)≤2 for odd p, ≤7 only at p=2,
plus 12𝔏 log W=o(1). *Repair:* "χ²≤2 for odd p≤W (≤7 at p=2); Mertens and 𝔏 log W=o(1) give
3 log W+C".

**m3 (citation of the λ^{3/4} substitution; l. 2782–2786 and labels of Lemma 14.4, Thms 14.5,
14.8, Prop 14.9, Thm 14.17).** Credited to KA3 §4.3, which lists only LS Thm 3.1, IF Cor 2.3, PL
and TU Cor 3.4. The LS2 upgrades come from LS2's own "Update (KARY3, (D)24)" header; IF Thm 2.5
only from (D)24. The mathematics is fine (black-box use, see Claim 3). *Repair:* cite
"[LS2, update note], (D)24" alongside KA3 §4.3; for thm:IFbudget say "substitution checked in
this note".

**m4 (Thm 14.6 header, l. 2949).** Missing "Case A as in Theorem 14.12" (source: "conditional on
PL Thm 3.1, i.e. with its Case-A proviso"). *Repair:* add it.

**m5 (Prop 14.9(1), l. 3023).** Source bound is log 2+S(max(λ₀, 2rA log N+λ(Q₀))); the max with
λ₀ is dropped. *Repair:* restore it.

**m6 (IF2 Cor 5.1 in text, l. 3237–3241).** Inherits IF Thm 2.5's "every prime of 𝒢 ≤ N^A",
which the §14.6 setup does not state; and S_A without log log is via Thm 14.17, not literally
IF2 Cor 5.1. *Repair:* add "family primes ≤N^A" and cite "[IF2, Cor 5.1] with Theorem 14.17".

**m7 (proof sketches of Thm 14.5, l. 2939, and Thm 14.17, l. 3193).** Lemma 3.x budget
(lem:budget) is invoked on a general mixture without first projecting to the family period (as
LS2 L2.3, IF Thm 2.5 and the proof of Thm 10.14 do); without it non-family primes of ν_c have no
e^{Λ₀} bound. Thm 14.17's sketch also omits the case split "s≤log(2+12c), or else T_><N/12".
*Repair:* add "after projection to the family period (as in Theorem 10.14)" and the case split.
Also Prop 14.22(1) drops IF2's caveat that τ=O(1) rests on Vaaler's bound quoted from the review
and not re-checked, and that Δ₀ must be bounded; Thm 14.11 discussion (l. 3074) says a proof
"must use (Sp) or the moment hypotheses" where LS2 says "something like" — soften. Thm 14.12
sketch (l. 3097): "the square base consists of units, since no forced class contains a unit
square" is a non sequitur (the no-square lemma gives avoidance, not unit-ness).

**m8 (§15 opening, l. 3328).** "the non-CRT inputs of Section 16, item 5": item 5 of the §16 list
is "Majorants ≥1 only on part of the avoider set"; non-CRT input is item 6. *Repair:* "item 6"
(better: \label the item).

**m9 (after Cor 15.7, l. 3465–3466).** "a saving (log N)^θ needs order k≥c(log N)^θ/log log N"
lacks "θ>3/4" (TU Cor 3.3 states it only for θ>3/4; for θ≤3/4 it is false since k=1 already
gives c(log N)^{3/4}). *Repair:* insert "for θ>3/4".

**m10 (Cor 15.8, l. 3470).** (a) needs k≥1 (k=0 makes the bound read log(1/Eν)≤0); (b) the
"PROVED given KA2/KA as reviewed" proviso of §10 is attached by the §15.3 header only to Thm 15.11
and Cors 15.12–15.13, not to Cor 15.8 which also uses Thm 10.12; (c) state "proof given here;
KA3 §4.3 only points to it". *Repair:* as stated.

**m11 (Cor 15.13, l. 3567).** "the corresponding mixed majorants" leaves implicit λ₀=A log N,
family primes ≤N^A and the allowed term types; KA3's self-review D3 asked that the family-prime
bound be stated. *Repair:* spell out the hypotheses.

**m12 (eq:window, l. 3619–3623).** The lower end L^{4θ/3−1} comes from Cor 15.8 and so needs
family moduli ≤N^A; and Prop 15.14 already narrows the window for block-sparse families.
*Repair:* add "(family moduli ≤N^A; except as narrowed by Prop 15.14)". The clause "the k-ary
ledger cannot give this (optimal at s₁=λ^{1/4})" (l. ~3610) is an unlabelled inspection claim:
mark it *Assessment* and add KA3's qualifier "for k≤L³". (Note for the parent, not the paper:
(D)24's and KA3 §0/§7's "cannot be closed from it alone" overclaim — attainability of λ^{3/4}
at λ≫L is open per KA3 itself; the paper's "would require a better level cap" is the correct
form; the ledger/KA3 wording should be aligned to it.)

**m13 (Assessment after Cor 15.18, l. 3669–3671).** "so the excess must come from multi-form
tuples": TU2 L3.1 covers only class −1, and TU2 itself exhibits other single-form tuples that
exceed CRT; TU2 Ass. 3.2 says "not pure class −1". *Repair:* "…from tuples that are not pure
class −1 (heuristically, multi-form tuples)".

**m14 (§15 "What is open", l. 3744–3754).** Missing: deciding literal TC_θ / TC^𝔄_θ on (2/3,1)
(only an Assessment so far) and θ=1; removing (log λ₀)^{3/4} from Prop 15.14. Also: ℓ₀ in
Cor 15.21 is undefined (as in TU2); "(λ₀,k)-mixed" is defined twice (Def 15.5 with slice primes,
Def 15.10 with primes >W) — rename one.
