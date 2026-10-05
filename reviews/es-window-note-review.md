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

**Brute force (from scratch, `scripts/review_r41_halfset.py`)**: for every a≡3 (4),
3≤a≤63, the number of selections equals 2^β(a) with β from (eq. beta), every S_σ has
size φ(a)/2, and every x≤20000 coprime to a with −1∉Rat_a(x) (Rat computed from the
u/v definition) has C(x)⊆S_σ for some σ (no exception, ~1.6·10⁵ cases). The window
criterion (Rat condition ⇔ a/(px)=1/y+1/z solvable, by direct search over y) holds for
all primes p≡1 (4), p<1200, and all a<3p (39 645 pairs); Lemma 2.6 checked there too;
Remark 3.2(i) example (a=7,x=17,p=61) confirmed.

## Defects
