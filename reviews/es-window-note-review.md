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

**Brute force (from scratch, `scripts/review_r41_halfset.py`)**: for every a≡3 (4),
3≤a≤63, the number of selections equals 2^β(a) with β from (eq. beta), every S_σ has
size φ(a)/2, and every x≤20000 coprime to a with −1∉Rat_a(x) (Rat computed from the
u/v definition) has C(x)⊆S_σ for some σ (no exception, ~1.6·10⁵ cases). The window
criterion (Rat condition ⇔ a/(px)=1/y+1/z solvable, by direct search over y) holds for
all primes p≡1 (4), p<1200, and all a<3p (39 645 pairs); Lemma 2.6 checked there too;
Remark 3.2(i) example (a=7,x=17,p=61) confirmed.

## Defects
