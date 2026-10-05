# Hostile referee report R41 — `paper/es-window-note.tex`

Referee branch `side-agent/referee-window-note`; author branch `side-agent/window-paper`
(merged at f9202d1). From-scratch scripts: `scripts/review_r41_*.py`.

(Report built incrementally; recommendation at the end.)

## Per-claim verdicts

* **Lemma 2.1 (two unit fractions)** — SOUND. Re-derived: rgy₁z₁ = s(y₁+z₁),
  gcd(y₁+z₁, y₁z₁)=1 ⇒ y₁z₁ | s; gcd(r,s)=1 ⇒ r | y₁+z₁. Sufficiency OK.
* **Thm 2.2 (window criterion)** — SOUND. gcd(a,x) | 4x−a = p and p∤x ⇒ gcd=1;
  gcd(a,p)=gcd(4x,p)=1. Converse: case p | d₁ (d₁=pu) gives u d₂ | x and
  pu ≡ −d₂ ⇒ d₂u⁻¹ ≡ −p, so symmetric as claimed. "Not all of x,y,z divisible by p"
  is correct (would give 4 ≤ 3). (Point 1 of the author's checklist: OK.)

* **Lemma 2.3 (reciprocity)** — SOUND. (r/a)=(−1/r)(a/r)=(−a/r)=(p/r)=(r/p) for odd r;
  r=2 forces a≡7 (8). r|a ⇒ r=p impossible as r≤x<p (uses a<3p). Checklist point 2 OK.
* **Lemma 2.4 (clean ⇒ fail), Lemma 2.5 (parity), Lemma 2.6 (window 3)** — SOUND.
* **Lemma 3.1 (half-set) and count (eq. beta)** — SOUND (re-derived; brute force below).
  Orbit sizes: g,g⁻¹,−g,−g⁻¹ distinct iff g²≠±1; #{g²=1}=2^ω(a) for odd a;
  β(a)=φ/4+2^{ω−2}−1. Case g=h (same prime) uses only that −1 is a non-square. OK.
* **Lemma 4.1 (large sieve + Markov)** — SOUND given Cited Thm (LS). V·g(q) is the
  product-Bernoulli law, E log q = Λ, Markov with log Q=(log X)/2 gives ≥1/2. Constant 4 OK.
* **Thm 4.2 (fixed-set stacking)** — SOUND. Classes distinct (ℓ>y>a, |a−a'|, ℓ∤24);
  ℓ≤z<p; ℓ|p+a, ℓ odd ⇒ ℓ|x_a and ℓ∤a; Mertens-AP gives (1+J/2)loglog z+O_A(1).
* **Cor 4.3** — SOUND.
* **Thm 4.4 (uniform)** — SOUND (minor wording, D-list). Re-derived: partial summation
  of SW from y=exp(L²) gives error O(L e^{−cL}) per class; log(log z/log y)=
  L−2log L−log(5(J+1)); e^{−(L−3log L−C)}·4X = N·e^C L³/ℒ ⇒ the O(log L). The "in
  particular" needs β_tot=O(Z²)=o(JL) and (J/2)·3log L=o(JL): both fine.
* **Remark 4.5** — SOUND. Checked numerically (`scripts/review_r41_phisum.py`):
  Σ_{a≤Z,a≡3(4)}φ(a)/(Z²/π²)=1.00000 at Z=10⁶; optimum Z*=π²L/(4log2)=3.5597L,
  value −π²/(64 log 2)=−0.22248. Priority: notes Thm 14.4/14.9 bound E(N) by counting
  p failing all windows C₀<w≤W=(log N)^θ, so the attribution is fair (see minor D-point
  on "internally reviewed").
* **§5 cited results** — statements checked where a source is archived:
  semi-linear f(s)=(e^γ/πs)^{1/2}∫₁^s dt/√(t(t−1)), β=1, s∈[1,2] matches Teräväinen
  (6.4) (`sources/sieve/teravainen-1611.08585.txt` l.1446); FHRSS Thm 1.1(2) matches
  `sources/sieve/2504.20289.txt` l.34–50 verbatim in hypotheses. Linear-sieve f₁, LS,
  SW, BV, Mertens-AP: standard, correctly stated as far as I can tell from memory
  (not checked against a primary source by me either). (eq. fsemi), (eq. flin): re-derived, OK.
* **Thm 6.1 (W1)** — SOUND. Re-derived every step: n_p≡1 (210); g(ℓ)=1/(ℓ−1) and
  1−g=(1−1/ℓ)(1−(ℓ−1)⁻²); c₁ independent of ε (V(z)≥c(log x)^{−1/2} because log z≤log x);
  k<1/(1/2−ε)<3 and parity ⇒ k∈{0,2}; m≤x^{2ε}; a=4mr₁≡2 (3) so 3∤a; LS with two
  classes, Λ≤(log y)/5+O(1); a/φ(a)=2·(m/φ(m))·r₁/(r₁−1)≤4m/φ(m); Σ1/r₁=−log(1−2ε)+o(1)≤3ε;
  (1−1/ℓ)(1+ℓ²/(ℓ−1)³)=1+(2ℓ−1)/(ℓ(ℓ−1)²)≤1+3/ℓ² iff ℓ²−5ℓ+3≥0, true for ℓ≥7
  (all ℓ≡1 (3)). Step 5 arithmetic OK. Checklist points 8, 9 OK.
* **Remark 6.3 (FHRSS route)** — SOUND (hypotheses verified: a=1, gcd(1,6)=1, 2|AB,
  gcd(35,24)=1, gcd(l−A,m)=gcd(4,35)=1). Implicit step "3∤n" (else p=4n−3≡0 (3)) should
  be said; n odd ⇒ p≡1 (8). Minor.
* **Thm 7.1 (W2, on EH)** — SOUND. e_p is a genuine integer sequence; for
  ℓ∈P₃∩P₇ two reduced classes, so A_d is a sum of ∏ω(ℓ)≤τ(d) progressions; ω(ℓ)=0
  for ℓ|840 is consistent (2∤n₃, 2∉P₇; 3,5∤n₇). Cauchy–Schwarz remainder
  (x(log x)⁴·x(log x)^{−10})^{1/2} OK, the trivial |E|≪x/φ(k) suffices. s→2+2ε/(1−2ε);
  f₁≥e^γ(s−2)/s≥(e^γ/3)ε. T^{(q)}: classes 0,q/a,(q−q')/a distinct mod ℓ≥11;
  (1−3/ℓ)⁻¹≤(1−1/ℓ)⁻³(1+6/ℓ²) ⇔ ℓ≥17/3; m even allowed for q=7 and then
  a/φ(a)≤2m/φ(m); Euler factor at ℓ=2 for q=7 is a bounded constant. Union bound fine.
  Checklist points 10, 11 OK.
* **Remark 7.3 (FI09 precedent)** — GAP (wording; MINOR defects D2, D3 below). FI09
  Assumption A(θ) and Thm 2 (θ<1 "sufficiently close to 1") are quoted correctly
  (`sources/window2/fi09-hyperbolic-pnt.txt` l.103–125); Nath–Xie Thm 1.1 (x/(log x)^{5/2},
  Ω(p+2)≤9) and Sedunova's abstract match the archived txt.
* **Lemma 8.1 (quadric)** — SOUND. Norms a²+ab+b²=N(a−bω), c²+cd+2d²=N(c+dθ);
  primitive element ⇔ gcd=1 in the bases {1,ω}, {1,θ}; split-prime construction gives a
  primitive element (π_q, π̄_q non-associate for unramified split q); (−7/r)=(r/7);
  2 splits in Q(√−7) and is 3-bad (inert in Q(√−3)). 3∤n, 7∤n+1 OK. Checklist 14 OK.
* **Thm 8.2 (P1)** — SOUND (but see D4 on the label/strength). n₃ odd, n₃≡1 (5);
  one class mod 840d per sign; φ(840)=192; for A⁻, n₃≡p≡2 (3). The "consequently"
  paragraph is the standard Selberg-parity logic and is correct: the A⁻ data are
  admissible inputs with true value 0. Checklist 12 OK (modulus 840d vs BV range: D5).
* **Remark 8.3 (joint)** — SOUND. Checked: for p≡1 (3), n₇≡2 (3), n₃≡1, n₇≡2 (5),
  n₃ odd, 2∉P₇, 7∉P₃∪P₇; (p/7)=±1 is 3 classes mod 7 ⇒ main term 3li(x)/φ(840d₁d₂)
  for both signs; for p≡2 (3), 3|n₇ (so the 4 sign classes really differ). Checklist 13 OK.
* **Remark 9.1 (random model, Assessment)** — SOUND as an assessment; arithmetic
  (log Pr=−(Q/8)loglog p, threshold 8 log p/loglog p) re-derived.
* **Remark 9.2 (Dickson)** — part (a) SOUND (re-derived: (ℓ/p)=(p/ℓ)=1 for ℓ∈Λ_K,
  (2/p)=1 as p≡1 (8); (r_a/p)=(a/p)=∏(p/ℓ)=1; Lemma 2.4). Unboundedness correctly
  CONDITIONAL; admissibility delegated to PS Prop 8.4(b) — I re-checked it (take p≡1 mod a
  high power of each ℓ∈Λ_K; for ℓ∉Λ_K there are J+1<ℓ forms with unit leading
  coefficients), OK. Checklist 15 OK.
* **Remark 9.3 (data)** — VERIFIED from scratch (`scripts/review_r41_census.py`, 5 s):
  719 781 primes p≡1 (24) below 10⁸, 179 468 Mordell-hard; max a_min=107 at p=8803369,
  which is a QR mod every prime ≤37; max a_min/log p=6.6914<6.7; normalised tails for
  Z∈{3,…,23} at x=10⁶,10⁷,10⁸ have max/min−1 ≤ 8.7% (<9%). The 10¹², 10¹⁸, 10²⁴ samples
  were not re-run.
* **Remark 6.4 (W1 numerics)** — VERIFIED to 10⁹ from scratch
  (`scripts/review_r41_w1num.py`): N₃ = 244, 1945, 15912, 131924 at 10⁶…10⁹ (ratios
  0.01253, 0.01259, 0.01258, 0.01245), identical counts to POINTWISE_WINDOW.md table;
  10¹⁰, 10¹¹ not re-run. "Monotone" is not literally true (rises 10⁶→10⁷), D-list.
* **Conjecture X_win(10)** — implication to ES correct (p≢1 (24) are Mordell-easy;
  verification to 10¹⁸ cited from memory — the author flags this).
* **Remark 9.4 (block fakes)** — (ii) SOUND (embedding count of U⊔V splits as
  emb(S_U,U)emb(S_V,V); mixed splits have ΣS>θ). (i) SOUND, but its hypothesis is
  superfluous (D-list).
* **Remark 9.5 (LP fake)** — labels correct (MODEL, weakest EVIDENCE); numbers match
  POINTWISE_WINDOW2 §3.5–3.7 (12769 configs, 89 correlations/89×89, 2.6·10⁻¹⁵, 60-digit
  re-solve, 0.744128, 0.497087, θ₂∈(0.5,0.7], [0.82,1.87], 9.3·10⁴ ≈ "up to 10⁵");
  scope paragraph is not weaker than the source's. Not re-computed by me. Checklist 16 OK.

**Brute force (from scratch, `scripts/review_r41_halfset.py`)**: for every a≡3 (4),
3≤a≤63, the number of selections equals 2^β(a) with β from (eq. beta), every S_σ has
size φ(a)/2, and every x≤20000 coprime to a with −1∉Rat_a(x) (Rat computed from the
u/v definition) has C(x)⊆S_σ for some σ (no exception, ~1.6·10⁵ cases). The window
criterion (Rat condition ⇔ a/(px)=1/y+1/z solvable, by direct search over y) holds for
all primes p≡1 (4), p<1200, and all a<3p (39 645 pairs); Lemma 2.6 checked there too;
Remark 3.2(i) example (a=7,x=17,p=61) confirmed.

## Defects

### MAJOR

**M1 (abstract/intro overclaim about two windows).** Abstract, sentence "Unconditionally,
two windows run into the parity problem: we exhibit two explicit sets of primes … of which
one has window 3 failing for ≫x/(log x)^{3/2} elements and the other for none." The
evidence offered (Thm 8.2 = Theorem D) concerns *one* window and shows that parity is a
*necessary input*, which W1 then supplies; it proves nothing about two windows being
blocked. The only two-window obstruction in the note is the model computation (Remark 9.5,
weakest EVIDENCE) and Remark 8.3 (again "parity is necessary", not "insufficient"). As
written, a reader takes the abstract to claim an unconditional two-window parity barrier
about primes, which would violate the note's own labelling rule ("nothing model-level
presented as a theorem about primes"). Similarly intro after Thm D: "for which the same
mechanism needs a level of distribution close to 1; this is why Theorem C is conditional"
states a necessity that is not proved. *Repair:* rewrite the abstract sentence as e.g.
"The parity of the bad part is a necessary input: we exhibit two explicit sets of primes
with the same sieve data …, of which one has window 3 failing … and the other for none.
For two windows our method needs a level of distribution close to 1; a model computation
suggests…"; in the intro say "our method needs … this is why our proof of Theorem C is
conditional". Consider retitling "…and the role of parity".

**M2 (missing classical literature / priority context for §4).** The note never cites
Vaughan (Mathematika 17 (1970)), whose large-sieve bound E(N)≪N exp(−c(log N)^{2/3}) for
the ES exceptional set is the classical instance of exactly the mechanism of §4 (sieving
shifted primes p+a by residue conditions over many moduli simultaneously) and is cited in
the sister paper `pointwise-obstruction.tex`. Nor does Remark 4.5 mention that the
(log log N)² shape already appears in notes Thm 12.2 for the set {a_min=∞} (windows up to
δ log N). The note's tails concern the different, larger sets {a_min>Z}, so nothing is
pre-empted, but a referee/reader needs the comparison: (i) for a_min=∞ the classical
bound is far stronger than anything in §4; (ii) Theorems 4.2/4.4 are, as far as I can
tell, new as statements about the *window tail at fixed or slowly growing Z*, and their
novelty is the half-set lemma that makes the exponent exact. *Repair:* add a paragraph in
§1 or Remark 4.5 citing Vaughan 1970 (and Elsholtz–Tao for counting), notes Thm 12.2, and
stating precisely what is new. Note Vaughan's paper could not be accessed in this project
(`sources/vaughan-1970-access-log.md`), so the comparison must be stated at the level of
the published bound only.

### MINOR

**m1 (Remark 7.3, FI09 description).** "counts primes p with p−2 and p+2 both sums of two
squares": FI09's π_Γ(x) counts orbit points γi (≈ matrices in SL₂(Z)), i.e. primes
weighted by their number of representations (FI09 l.60–80: π_Γ≍x/log x, whereas the
unweighted prime count is heuristically of order x/(log x)², two half-dimensional
conditions). Say "counts, with
multiplicity, the representations p=x₁²+…+x₄², x₁x₄−x₂x₃=1, so that p∓2 are sums of two
squares". The §8 sentence after Lemma 8.1 is fine.

**m2 (Remark 7.3, "same route").** FI09 sieve one condition (b(n−2)) with the
*semi-linear* sieve, carrying the other as the weight r(n+2) (FI09 §6, l.536–560), and
remove two-prime configurations (§7). Thm 7.1 instead sifts both absence conditions at
once with the *linear* sieve at level x^{1−ε}. The "semi-linear type sieve to x^{1/2−ε}"
parenthesis is inaccurate for W2 (it describes W1). Rephrase: "the same final step
(removal of two-prime configurations with parity), but a linear sieve on both conditions
where FI09 use a semi-linear sieve with a representation-number weight".

**m3 (Thm 8.2 label).** Thm 8.2 is a direct instance of Selberg's parity example; its
proof is five lines. "Theorem" (and "Theorem D" in the intro) overstates its depth;
"Proposition" is more appropriate. Not a correctness issue.

**m4 (Thm 8.2(1), BV range).** The moduli are 840d with d≤x^{1/2}(log x)^{−B}, which
exceed BV's range by the factor 840; say "with B replaced by B+1" (W1 handles this
correctly via D=x^{1/2}(log x)^{−B}/840).

**m5 (Remark 6.3).** The step "3∤n" (else p=4n−3 is divisible by 3) and "n odd ⇒ p≡1 (8)"
should be written out.

**m6 (Remark 6.4).** "slow monotone drift": the normalised count rises from 10⁶ to 10⁷
(0.01253→0.01259, my recount) and falls afterwards; drop "monotone" or say "from 10⁷".

**m7 (Remark 9.4(i)).** The hypothesis "if the true law has at least as much mass on
{u,v}-type configurations as on ∅" is superfluous: ν=μ+μ(∅)(−[∅]+[{u,v}]) is ≥0 for any μ.
(Conversely in (ii) an actual fake needs μ(U⊔V)≥μ(∅) or a convex combination; worth saying.)

**m8 (Steps 3 of Thm 6.1 / T₁ of Thm 7.1).** #{p≤x: r²|n} ≤ x/(4r²)+1, not x/r²; the
"+1" terms add ≤π(√x). Harmless; write ≤2x/z+√x.

**m9 (§2.2 after Lemma 2.3).** "(r/a) … union of reduced classes modulo 4a": since the
Jacobi symbol (r/a) depends only on r mod a, "modulo a" is correct and simpler (the
non-principal character (·/a) of (Z/aZ)^× gives density 1/2 as a≡3 (4) is not a square).

**m10 (Thm 4.2 statement).** For p≤3 max A, Rat_a(x_a) may be undefined (gcd(x_a,a)=p
possible). Add "p>3max A" or "with the convention that the condition holds if p|x_a".

**m11 (bibliography, Notes).** `\bibitem{Notes}` calls notes.md "internally reviewed";
DISCOVERIES.md (items 1–5) records the review status of notes Thms 12.2, 14.4, 14.9 as
"not stated". Remark 4.5 attributes the (log N)^θ window tails to §14; state that this
material's review status is not recorded.

**m12 (typesetting).** The author report says "pdflatex clean: no warnings". My compile
(pdflatex ×2, 20 pp, no undefined refs) gives **19 overfull hboxes**, several large
(132 pt at l.75 — the Rat_a display; 123 pt at l.141; 97 pt at l.345; others at l.113,
128, 424, 467, 495, 568–573, 603, 617–621, 628, 662, 707, 794–797, 815, 864, 922–925,
992). Break the displays (e.g. `multline`/`split`) before circulation.

**m13 (intro, "Unconditionally we only know a_min≥7 infinitely often", Remark 9.2).** This
is a claim about the literature; qualify as "the only unconditional result we know of".

## Author's 17-point checklist (O41) — disposition

1 Thm 2.2(3) p|d₁: OK. 2 Lemma 2.3/2.4: OK. 3 half-set g=h and β(a): OK (brute force a≤63).
4 Lemma 4.1 Markov/constant 4: OK. 5 Thm 4.2 distinctness, ℓ∤p, Mertens-AP: OK.
6 Thm 4.4 SW range/errors/bookkeeping: OK. 7 Remark 4.5 Σφ~Z²/π², π²/(64log2): OK
(numerically confirmed). 8 W1 c₁ independent of ε, s∈[1+ε,2]: OK. 9 W1 Step 4 bounds:
OK (the inequality is needed and true for ℓ≥7, not ℓ≥5 as in the report; all ℓ≡1 (3)).
10 W2 e_p, |r_d|≤τ(d)max|E|, (Ω₁), s, T^{(q)}, factor bound, m even: OK. 11 union bound: OK.
12 P1(1) bookkeeping: OK (m4). 13 Remark 8.3: OK. 14 Lemma 8.1: OK. 15 Dickson (a): OK.
16 LP numbers/scope vs WINDOW2: OK. 17 numerics: census to 10⁸ and N₃ to 10⁹ re-done from
scratch and match; larger ranges not re-run.

Sources: FHRSS Thm 1.1, Teräväinen (6.4), FI09 A(θ)/Thm 2, Nath–Xie Thm 1.1, Sedunova
abstract checked against archived txt. Not checkable here (no archived copy): Iwaniec 1976,
OdC Thm 11.13 hypotheses, HR Thm 8.4, MV Cor 11.21 / IK Thm 17.1 numbering, Montgomery
1968, Mihnea–Dumitru 10¹⁸ (statements are the standard ones as far as I know; the note
already flags them "from memory").

## Recommendation

**Minor revision (accept after repairs).** I found no FATAL defect and no mathematical gap
in any proof as written in the paper: every PROVED claim was re-derived line by line, and
every finite claim that I could test (half-set lemma, β(a), window criterion vs direct
unit-fraction search, Lemma 2.6, Remark 3.2(i), census to 10⁸, W1 counts to 10⁹,
Σφ constant) was confirmed by from-scratch code. Labels are essentially right; the one
real problem is **M1**, where the abstract (and one intro sentence) presents a
one-window parity example plus a model computation as if they were an unconditional
two-window parity barrier. **M2** (missing Vaughan 1970 / notes Thm 12.2 context and an
explicit novelty statement) must also be fixed before external circulation. m1–m13 are
wording/typesetting.
