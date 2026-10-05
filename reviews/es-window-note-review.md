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

## Defects
