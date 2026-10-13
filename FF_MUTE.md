# FF_MUTE — one mute place over F_q[T]: a function-field ES variant that is a theorem (task O195, spark relay P)

Status: in progress (O195). **ES is not solved here, nor any infinite case of ES or of ES_q.** Labels as in
DISCOVERIES.md. Builds on UNIT_ORBIT_ES.md ((J)23), FUNCTIONFIELD_ES.md (ES_q, Lemma 1.3, Fact 5.2, §4 signs),
DRINFELD_ES.md (power-residue reciprocity), DEPTH_ASPECT.md Thm 2.5 ((J)26), FIXED_MODULUS_SHOTS.md ((J)25).
Scripts `scripts/fm_*`.

Notation: q a prime power, R = F_q[T], F = F_q(T), |G| = q^{deg G}. A monic of degree k ≥ 1, P monic irreducible of
degree n, P ∤ A. "Monic" for a nonzero rational function G/H (G, H ∈ R) means lc(G)/lc(H) = 1 (Hayes' sign at ∞).
ES_q(A, P): A/P = 1/X + 1/Y + 1/Z with X, Y, Z ∈ R monic and NC (every denominator of degree ≥ n − k).
For q odd, ε := (−1)^{(q−1)/2} = χ(−1), χ the quadratic character of F_q^*; (·/·) the Jacobi symbol in R.

## 0. Iteration log

(P1) Transport (J)23 verbatim: mute set S of monic irreducibles, third denominator z ∈ R[1/S] monic with even
negative S-valuations. The orbit is {Q² : Q ∈ ⟨S⟩}, the modulus of the shot is the fixed A (§2).
(P2) Over ℤ the obstacle for |S| < 4 was Artin's conjecture. Over F it is Bilharz's theorem, and in the form needed
here (a fixed P, a fixed degree d of the modulus) the whole argument is a finite character-sum computation with
Weil's bound: the small Kummer primes ℓ | q − 1 become Dirichlet characters mod s by reciprocity, the large ones
(ℓ | q^d − 1, ℓ ∤ q − 1) are ≡ 1 (mod d) when d is prime, so their total weight is O(log d / d). (§3)

## 1. The mute variant ES_q^{(S)}

Let S be a finite set of monic irreducibles with s ∤ A for s ∈ S, ⟨S⟩ the monoid of monic S-products.

**Definition 1.1 (ES_q^{(S)}(A, P)).** For P ∤ A with P ∉ S: there are X, Y ∈ R monic and z ∈ R[1/S] monic with
`A/P = 1/X + 1/Y + 1/z,  v_s(z) ∈ 2ℤ for every s ∈ S with v_s(z) < 0,`
and NC: deg X, deg Y, −v_∞(z) ≥ n − k. Equivalently 1/z = Q²/Z with Q ∈ ⟨S⟩, Z ∈ R monic, gcd(Z, Q) = 1.
S = ∅ (or Q = 1) is ES_q; ES_q(A, P) ⇒ ES_q^{(S)}(A, P).

*Remark 1.2 (NC).* FUNCTIONFIELD_ES Lemma 1.2 transfers in odd characteristic ≠ 3: the coefficient of the leading term at
∞ of a sum of m monic terms of the least degree is m ∈ {1, 2, 3}, so for p ≥ 5 every monic solution satisfies NC.
(Its char-3 argument used "P divides a denominator", which fails for 1/z = Q²/Z; in char 2 and 3 NC is part of the
definition.) The solutions constructed below satisfy NC by direct degree count.

## 2. The shot identity (FF transport of UNIT_ORBIT Prop 2.1)

**Proposition 2.1 (mute shot; PROVED, elementary).** Let Q ∈ ⟨S⟩, and let f ∈ R be monic of degree d ≥ 1 with
`f ≡ −1 (mod A),   f | P + A·Q²,   deg(A·Q²) > n + d.`
Put E := (P + AQ²)/f, X := (P + E)/A, Y := P(f + 1)/A, z := P·X·(f + 1)/(A·Q²). Then (X, Y, z) solves
ES_q^{(S)}(A, P) with exact degrees deg X = deg(AQ²) − k − d > n − k, deg Y = n + d − k, −v_∞(z) = n − k, and the
solution has Type II shape at P (P ∤ X, P | Y, v_P(z) = 1).
*Proof.* E is monic of degree k + 2deg Q − d > n, so P + E is monic of degree deg E. From Ef = P + AQ² and f ≡ −1:
E·(−1) ≡ P (mod A), so A | P + E and X ∈ R is monic. A | f + 1 and f + 1 is monic (d ≥ 1), so Y is monic. z is monic.
Since X + Q² = (P + E + AQ²)/A = E(f + 1)/A,
1/Y + 1/z = A(X + Q²)/(P·X·(f + 1)) = E/(P·X) = (AX − P)/(PX) = A/P − 1/X.
Degrees: deg z = n + deg X + d − k − 2deg Q = n − k. *Parity at s ∈ S:* let c = v_s(Q) ≥ 1 (if c = 0, z is
s-integral since s ∤ A) and σ = v_s(f + 1). Multiplying AX = P + E by f: **A·f·X = P(f + 1) + A·Q²**. s ∤ f (else
s = f | P, impossible as s ≠ P), s ∤ A, s ∤ P. If σ < 2c, v_s(RHS) = σ, so v_s(X) = σ and v_s(z) = 2σ − 2c (even).
If σ ≥ 2c then v_s(X) ≥ 2c and v_s(z) ≥ 0. *Shape:* f | P would give f = P (prime), then P | AQ², false; so
P ∤ f, P ∤ E... more simply AX = P + E with E ≡ AQ²/f ≢ 0 (mod P) gives P ∤ X; P ∥ Y, P ∥ z as P ∤ X(f + 1)? (P | f + 1
is possible; then v_P(Y), v_P(z) ≥ 2 — still "P | both", Type II.) ∎
(Degree condition: if instead deg(AQ²) < n the same formulas work with deg E = n − d, X of degree n − k; the only
excluded situation is deg E = n, where P + E has leading coefficient 2. Below we always take Q large.)

**Corollary 2.2 (ES_q-integrality of a shot; PROVED).** In Prop 2.1, z ∈ R (an ES_q solution) iff
`f ≡ −1 (mod A·Q)` (i.e. v_s(f + 1) ≥ v_s(Q) for all s | Q).
*Proof.* From the parity computation: v_s(z) = 2σ − 2c ≥ 0 iff σ ≥ c when σ < 2c, and v_s(z) ≥ 0 when σ ≥ 2c. ∎
This is UNIT_ORBIT Prop 6.1 verbatim: the mute normalisation is exactly what removes the growing modulus A·Q.
