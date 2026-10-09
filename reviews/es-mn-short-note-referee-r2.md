# Referee report R104 — density-transition section of `paper/es-mn-short-note.tex` (O104)

Hostile referee, round 2 (new §8 "The density transition", changed abstract / intro / open problems).
Source compared: `EXCEPTIONAL_MN2.md` + `reviews/exceptional-mn2-review-{A,B}.md`; ET = Elsholtz–Tao
arXiv:1107.1010 (`sources/elsholtz-tao-1107.1010.pdf`); PW = Pomerance–Weingartner arXiv:2511.16817v2.
From-scratch checks: `scripts/review_r104_*.py`.

(Work in progress — sections are added claim by claim.)

## 1. Upper side (Lemma 8.1 reduced model, Lemma 8.2 multiplicities, Thm 8.3, Thm U)

**Verdict: SOUND.** Statement and label of Theorem U match MN2 Thm U exactly (for every ε an
ineffective A_ε, all m ≥ 4, all N with log N ≥ A_ε m^{1/3}); no strengthening. Re-derived:

* Bonferroni: for even r, Q_r(h) = C(h−1, r) for h ≥ 1, so 1_{h=0} ≤ Q_r(h) ≤ 1_{h=0} + C(h, r+1)
  (C(h−1,r) ≤ C(h,r+1)·(r+1)/h, and C(h−1,r)=0 for h ≤ r). Checked numerically
  (`review_r104_bonf.py`).
* Reduced model: f_c(ℓ) ≤ ℓ−1 (distinct non-zero classes), Bernoulli product, elementary symmetric
  bound e_{r+1}(p) ≤ (Σp)^{r+1}/(r+1)!, Σ f/(ℓ−1) ≤ 2μ_c with μ_c = Σ f_c(ℓ)/ℓ exactly as in
  Cor 5.2; (2eC_u s/(r+1))^{r+1} ≤ e^{−(r+1)} iff r+1 ≥ 2e²C_u s. ✓.
  Cor 5.2's lower bound a_u t³/m is for (c, L_K)=1, which is exactly the reduced fibre. ✓
* Main term identity: q_B | 𝓜' (lcm k_A | L_K), a_B a unit, so P(ñ ≡ a_B (q_B)) = 1/φ(q_B). ✓
  Exceptional primes p ∈ (N/2, N]: p > X > K, so p is a unit mod 𝓜', and Lemma 3.3(1) has no
  hypothesis besides n ≥ 1. ✓
* Moduli: (1+κ)(2e²C_u s+2)(sm)^{1/3} ≤ 0.45 C_1^{-1}… uses s ≥ 1 (2 ≤ 2s) and s·(sm)^{1/3} =
  s^{4/3}m^{1/3}. ✓ t ≤ L. ✓
* Lemma 8.2: Shiu Thm 1 (F = τ⁴, F(p)=16, interval (kx,2kx] of length y = kx, modulus k ≤ y^{1−β})
  gives (kx/φ(k))·(log)^{−1}·exp(16 Σ1/p) ≍ (k/φ(k)) x t^{15}; the restriction to prime ℓ is by
  positivity. Dyadic sum: ≪ t · log t · t^{15} ≤ t^{17}. Euler product exponent 4^r. ✓
  (Needs κ ≤ 1/4 for "X^{1/2} ≥ k²"; κ = 1/480 in §2.1. ✓)
* Cauchy–Schwarz: N (C S_2 L^{−1−A'})^{1/2} = C'(r) N L^{−3} for A' = 17r+4^r+5 and t ≤ L. ✓

Minor points: see defects m1, m2 below.

## 2. Lower side (Lemma 8.4, Prop 8.5, Lemma 8.6, Prop 8.7, Lemma 8.8, Thm L)

**Verdict: SOUND (as a proof relative to ET Thm 7.1 + ET's proof of Prop 1.4); minor repairs.**
Statement, ranges, label and "effective" of Theorem L coincide with MN2 Thm L (both ranges
`log m ≤ L/10, L ≤ m^{1/2}` and `log m > L/10`; the range `log m ≤ L/10 < …, L > m^{1/2}` is, as in
MN2, not covered, which is harmless since the consequence forces L ≤ m^{1/3} eventually). No
strengthening. Re-derived:

* **PW inputs** (checked against `sources/pw.txt`): Cor 2.2 / Cor 2.4 / Lemma 7.4 / (3.2) / (3.4)
  are quoted correctly; "(a,b)=1 may be assumed" is PW p. 7 ("follows from gcd(x',y',z')=1").
  PW's unsimplified counts are Type I `(N/φ(m)) L² log L log m`, Type II `(N/φ(m)) L² log L`
  (PW pp. 6–8) — so the comparison "factor min(log m, L/log m)" against the *unsimplified* Type I
  bound is right: PW/ours = L log m/(L + log² m).
* **Lemma 8.4(a)** re-derived (g-expansion of b/φ(b); per e ≥ 2 the double sum is
  ≪ log²(2e)/e + log Y log e/e + log² Y/e; S'_m via Euler product needs E ≥ log m because
  Π_{p|m,p>E}(1−1/p)^{−1} ≤ exp(2ω(m)/E)). Numerically sane (`review_r104_harm.py`). ✓
* **Lemma 8.4(b)** re-derived: n/φ(n) ≤ e⁴ Σ_{s|n, s|P_y} μ²/φ (ω(n) ≤ 1.45y); Rankin tail
  S^{−σ}(log y)^e with S = U^{1/2}, log U ≥ y/2 gives exp(−y/(4 log y)) ≪ y^{−10}; large-u part via
  Shiu Thm 1 (F = τ₃, modulus s ≤ x^{1/1.1}, so β fixed) converges after Σ_s μ²(s)/φ(s)²; small-u
  part ≪ m^{0.01}/m. ✓ (Condensed in the paper but every step is named.)
* **Prop 8.5** re-derived: abd ≤ 2N/m (from e ≤ a+b ≤ 2ab, m ≥ 4); ET product
  ≤ m^{5/2}a^{5/2}b^{1/2}cd²e ≤ 2m^{1/2}(mabd)² ≤ 8m^{1/2}N²; min modulus ≤ 8^{2/5}m^{1/5}N^{4/5} ≤
  3N^{0.82} (m ≤ N^{1/10}); (ii) p = (macd−1)e − ma²d ✓; U = 3N^{0.82}/m satisfies log U ≥ ½log(mU). ✓
  Numerical check of the product inequality on random admissible tuples: `review_r104_typeII.py`.
  Minor: in (i) "one class modulo made" needs (e, ad) = 1 — true ((e,a) | (a,b); (e,d) | p) but not
  said (defect m3).
* **Lemma 8.6 vs ET pp. 30–32** (read in `sources/elsholtz-tao-1107.1010.pdf`): variable dictionary
  (ET linear a = our d, ET quadratic b = our a, ET case A ≤ B = our D ≤ A), (7.11) and the three
  q-ranges are quoted correctly; ET's q<A claim "sums to zero" is false for square q (principal
  character) — the paper's "harmless slip" remark is right (cost Σ_r A log B/r²). The q > kA range:
  c(q)(q/k'a) is χ_{−4}χ_8^{m'}·(·/k'a), non-principal, so mean zero ✓. PV in the middle range:
  d ↦ (d/q)1_{d odd} is a single non-principal character mod 2q for odd non-square q (the paper's
  "combination of two" is harmless). Middle cost D'log A(1+√(k/D')log(kD')) ✓. The 2^j-reduction:
  k_j = 2^j k, D'_j = D/2^j; lossy iff 4^j ≳ D/(k log²); bounding the lossy j by ET's own
  log(1+k_j) gives Σ 2^{−j} log(1+kD) over 2^j ≥ (D/(k log²))^{1/2}, i.e.
  ≪ (k log²/D)^{1/2} log(kAD) ≤ 1 for D ≥ k log⁴(kAD). ✓ ET Rem 1.5 indeed suggests PV ✓.
  Minor: the paper drops MN2's "boxes with A or D = 1 are enlarged to 2 by positivity", but
  Prop 8.7 does use boxes with A' = 1 or D' = 1 (defect m4).
* **Prop 8.7** re-derived (with ET (A.12) checked verbatim, ET p. 34–35): k = ms²t; Lemma 8.6 with
  l = 10 needs k ≤ (2A'D')^{10} ✓; lossy boxes ≤ #{dyadic D' < k log⁴(kN)} ≪ log m + log st + log L;
  weighted per block Σ(st)^{−2}[log²X + L log m log(ms²t)] ≪ log²X + L log²m ✓ (log L ≪ log m
  uses L ≤ m^{1/2}); small boxes: n ≤ 8k^{1.2}, occurrence ⇒ X ≤ m^{0.1}(st)^{1.2}, tail
  Σ_{st≥Y}(st)^{−1.94} ≪ Y^{−0.94}log Y, number of small boxes ≪ log(mst); total
  (N/φ(m))m^{0.03}log²m ≪ N m^{−0.9} ≤ (N/L)m^{−0.35} ✓. Blocks j ≤ log₂(3N) ≤ 2L for N ≥ 16 ✓.
  The paper's condensation "≪ log m+log(st)+log L lossy ones" and "occur only for (st)^{1.2}m^{0.1} ≫ X"
  keeps every load-bearing range; the dropped "number of small boxes ≪ log(mst)" is implicit in
  "in total contribute" (acceptable).
* **Lemma 8.8**: classes for Type II need mab ≤ 2N (PW (3.4)) and τ(a+b) ≤ e^{CL/log L}; the extra
  L³ from dividing by π* is absorbed into e^{CL/log L} (enlarge C). ✓ (Proof says "Type II likewise";
  acceptable.)
* **Consequence**: if ρ_rep > 0 then m ≤ 3p (Lemma 7.4 / (3.4)) so L ≥ log(m/3); L³log L/φ(m) → 0
  forces φ(m) → ∞, then L ≤ m^{1/3} eventually, the L²log²m term is ≤ (L³+log⁶m)log L/φ(m), and in
  the range log m > L/10, e^{CL/log L}/m ≤ m^{10C/log L − 1} → 0. ✓

## 3. From-scratch numerical checks (all pass)

* `review_r104_bonf.py`: Bonferroni sandwich for r ≤ 40, h ≤ 200: 0 failures.
* `review_r104_typeII.py`: 829 578 admissible Type II tuples (m < 60): abd ≤ 2p/m, (e,ad)=(e,m)=1,
  ET product ≤ 0.34·8m^{1/2}p², min modulus ≤ 8^{2/5}m^{1/5}p^{4/5}: no violation.
* `review_r104_harm.py`: Lemma 8.4(a) sum/((φ(m)/m)log³Y+log²Y) ∈ [1.03, 1.41] (Y = 600, m ∈
  {4,6,7,30,210,2310}); (b) m·Σ/(log³U+m^{0.02}) ∈ [0.34, 0.43]. Bounded, as claimed (sanity only).
* `review_r104_halfpoint.py` (independent exact decision: x-loop over (p/m, 3p/m] and
  `(Ay−B)(Az−B)=B²` divisor parametrisation; not the PW criterion): at the table's quartiles
  ρ_rep(60, e^{5.68}) = .22, ρ_rep(60, e^{7.64}) = .50, ρ_rep(60, e^{9.41}) = .76 (all primes);
  ρ_rep(64, e^{7.72}) = .48, ρ_rep(101, e^{7.59}) = .49 (all primes), ρ_rep(200, e^{11.21}) = .52
  (every 8th prime, 422 primes). Consistent with the table in §8.5 (within sampling error).

## 4. Abstract / intro / gap / numerics / literature / open problems

* **Abstract lower-side claim — SOUND.** "proportion of m-exceptional primes → 1 when
  log N/(φ(m)/log m)^{1/3} → 0" is L³log m/φ(m) → 0. Since L > m would make this ≥ m log m/… → ∞,
  eventually L ≤ m, so log L ≤ log m and L³log L/φ(m) → 0, which is Thm L's consequence. It is
  exactly Thm L's "in particular" clause (A(m log m/φ(m))^{1/3} = L(log m/φ(m))^{1/3}); weaker than,
  not stronger than, the theorem. ✓ Gap factor: upper L ≥ A_ε m^{1/3} vs lower L = o((φ(m)/log m)^{1/3})
  ⇒ ratio (m log m/φ(m))^{1/3} ✓; Cor D + PW: m^{1/3}(log m)^{4/3}/(φ(m)/log²m)^{1/3}
  = (log m)²(m/φ(m))^{1/3} ✓.
* **Abstract status sentence — MINOR overclaim** (defect m6): "relative to published divisor-sum
  bounds of Elsholtz and Tao" — Lemma 8.6 rests on a *modified proof* of ET Prop 1.4, not a published
  bound. Also "even m ≤ 300" should be "even m ∈ [60,300]" (MN2 §2.1: the rows m ≤ 24 are artefacts;
  the table and the 1.95 ± 0.05 are for [60,300]).
* **Intro Theorems U, L** — match §8 and MN2 verbatim in hypotheses/ranges/effectivity. ✓
* **§8.4 PW wording** — checked against `sources/pw.txt`: p. 2 ("between exp(m^{1/3}) and
  exp(m^{1/2}) there is a transition from 'usually false' to 'usually true'", "most prime values of n
  near this bound are exceptions"), p. 3 Poisson heuristic; PW Type I/II unsimplified counts pp. 6–8. ✓
  Pomerance 2026 talk and Elsholtz Rem 7.3 wording match novelty audit 10c §1.1 (talk: transition
  question open; Elsholtz: explicit c_{m,3}, N > N_m, ratio (Lm)^{1/12}). ✓
  One slip (defect m7): "(PW) gives 'most primes representable' only for log N ≫ m^{1/2}(log m)^{3/2}" —
  PW's saving (L²/φ(m))^{1/3} beats log L once L ≫ φ(m)^{1/2}(log m)^{3/2}, which can be smaller by
  (log log m)^{1/2}.
* **§8.5 numerics** — table entries and L_.75 − L_.25 = 3.73, 3.47, 4.26, 4.83, 4.87, 5.34 recomputed
  from MN2's quartiles ✓; window/L_.5 ∈ [0.377, 0.488] ✓ ("0.38–0.49"); factors 1.56/0.80 =
  (log300/log60)^{±…} ✓; Poisson-cube κ = ln2/1.95³ = 0.0935 ✓. Independently reproduced at four
  (m, L) points (§3). Labelled EVIDENCE ✓; Conjecture C2 verbatim from MN2, starred, CONJECTURE ✓.
  Notation clash (defect m1): κ here vs the multiplier exponent κ = 1/480 used two pages earlier in
  Lemma 8.2.
* **Open problems** — "transition gap" matches MN2 §4 (i)–(iii) ✓; "the profile" ✓. Defect m8:
  "when (log N)³ log log N/φ(m) is small most primes are exceptional (Theorem L)" — Thm L needs this
  → 0 (with m → ∞, automatic), or "sufficiently small and m large".
* **Compile**: two pdflatex passes, 25 pp., no undefined references, no overfull boxes; 6 hyperref
  "Token not allowed" warnings (math in section titles, pre-existing kind), a few underfull boxes in
  the bibliography (harmless).

## 5. Defects (all MINOR; no FATAL, no MAJOR)

* **m1** §8.5 and C2 discussion: `\kappa` reused for the Poisson-cube constant (κ = 1/480 is the
  multiplier exponent of §2.1, used in Lemma 8.2). *Repair:* rename to λ.
* **m2** Lemma 8.6 proof: "a combination of two non-principal character sums" — for odd non-square q,
  d ↦ (d/q)1_{d odd} is one non-principal character mod 2q. *Repair:* reword (harmless).
* **m3** Prop 8.5 (i): "one class modulo made" needs (e, ad) = 1; true since (e,a) | (a,b) = 1 and
  (e,d) | p with p ∤ e (as e ≤ a+b ≤ ab+1 < p). *Repair:* add the clause.
* **m4** Lemma 8.6 needs A, D ≥ 2, but Prop 8.7 applies it to dyadic boxes with A' = 1 or D' = 1.
  MN2 had the repair "enlarged to 2 by positivity" (review A D-L2); it was dropped in condensation.
  *Repair:* restore it in Prop 8.7.
* **m5** §8.3 intro: "open even for m = 4 [ET §9]". ET §9's parenthetical literally reads "it does not
  seem that a similar trick is available in the Type II case" (an evident slip for Type I, given ET
  Thm 1.1). The cleaner source is ET p. 4 after Thm 1.1 (the log log N "arises from … the Brun–
  Titchmarsh inequality … and we conjecture that it should be eliminated"). *Repair:* cite
  [ET, discussion after Thm 1.1] (keep §9 as secondary).
* **m6** Abstract: (a) "relative to published divisor-sum bounds of Elsholtz and Tao" → "relative to
  a published divisor-sum bound of Elsholtz and Tao and a modification of the proof of another";
  (b) "even m ≤ 300" → "even m ∈ [60,300]".
* **m7** §8.4: m^{1/2}(log m)^{3/2} → φ(m)^{1/2}(log m)^{3/2} (and "≫" in place of "only for … ≫"
  is fine).
* **m8** Open problem 2: "is small" → "tends to 0".
* (no defect) The labels of Theorems U and L omit BT/PNT (U) and Pólya–Vinogradov (L); these are
  classical and named in §1 "Status and novelty" / proofs. Acceptable.

## 6. Repairs applied (R104), recompiled

All eight minor defects m1–m8 were repaired in `paper/es-mn-short-note.tex`; each spot carries a
LaTeX comment `% R104 repair` (invisible in the PDF, greppable). m1 κ → λ (§8.5, C2 remark);
m2 single character mod 2q (Lemma 8.6); m3 (e,ad)=1 clause (Prop 8.5(i)); m4 box enlargement
restored (Prop 8.7); m5 log log N source → discussion after ET Thm 1.1, with the ET §9 slip noted;
m6 abstract status sentence and "even m ∈ [60,300]"; m7 φ(m)^{1/2}(log m)^{3/2}; m8 "→ 0".
Recompiled twice: 25 pp., no undefined references, no overfull boxes, no errors (same 6 hyperref
"Token not allowed" warnings as before). Rendered text of every repaired spot checked via pdftotext.

## 7. Recommendation

**ACCEPT the density-transition section (after the R104 repairs, already applied).** No FATAL or
MAJOR defect. Theorems U and L are stated exactly as in the reviewed source MN2 (no strengthening;
ineffective/effective, ranges and relative-proof labels preserved), every load-bearing step of MN2
§§1, 3 survives the condensation except one dropped MN2 repair (m4, now restored), and the abstract's
lower-side claim is precisely Thm L's "in particular" clause. Residual risk, honestly stated in the
paper: Lemma 8.6 is a proof *sketch* relative to ET's proof of Prop 1.4 (I re-checked it against
ET pp. 30–32 and agree, but it is not a line-by-line written proof); Theorem U inherits everything
from Cor 5.2, i.e. from the unrefereed 3/4 note.
