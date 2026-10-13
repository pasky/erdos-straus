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
solution has Type II shape at P (P ∤ X, v_P(Y) ≥ 1, v_P(z) ≥ 1).
*Proof.* E is monic of degree k + 2deg Q − d > n, so P + E is monic of degree deg E. From Ef = P + AQ² and f ≡ −1:
E·(−1) ≡ P (mod A), so A | P + E and X ∈ R is monic. A | f + 1 and f + 1 is monic (d ≥ 1), so Y is monic. z is monic.
Since X + Q² = (P + E + AQ²)/A = E(f + 1)/A,
1/Y + 1/z = A(X + Q²)/(P·X·(f + 1)) = E/(P·X) = (AX − P)/(PX) = A/P − 1/X.
Degrees: deg z = n + deg X + d − k − 2deg Q = n − k. *Parity at s ∈ S:* let c = v_s(Q) ≥ 1 (if c = 0, z is
s-integral since s ∤ A) and σ = v_s(f + 1). Multiplying AX = P + E by f: **A·f·X = P(f + 1) + A·Q²**. s ∤ f (else
s = f | P, impossible as s ≠ P), s ∤ A, s ∤ P. If σ < 2c, v_s(RHS) = σ, so v_s(X) = σ and v_s(z) = 2σ − 2c (even).
If σ ≥ 2c then v_s(X) ≥ 2c and v_s(z) ≥ 0. *Shape:* f ≠ P (else P | AQ²), so Ef = P + AQ² gives E ≢ 0 (mod P), and
AX = P + E gives P ∤ X; v_P(Y) ≥ 1 and v_P(z) ≥ 1 (both = 1 unless P | f + 1). ∎
(Degree condition: if instead deg(AQ²) < n the same formulas work with deg E = n − d, X of degree n − k; the only
excluded situation is deg E = n, where P + E has leading coefficient 2. Below we always take Q large.)

**Corollary 2.2 (ES_q-integrality of a shot; PROVED).** In Prop 2.1, z ∈ R (an ES_q solution) iff
`f ≡ −1 (mod A·Q)` (i.e. v_s(f + 1) ≥ v_s(Q) for all s | Q).
*Proof.* From the parity computation: v_s(z) = 2σ − 2c ≥ 0 iff σ ≥ c when σ < 2c, and v_s(z) ≥ 0 when σ ≥ 2c. ∎
This is UNIT_ORBIT Prop 6.1 verbatim: the mute normalisation is exactly what removes the growing modulus A·Q.

## 3. Theorem: one mute place suffices (Bilharz–Weil, effective)

Fix S = {s}, s monic irreducible of degree h ≥ 1, s ∤ A. Throughout P is monic irreducible of degree n ≥ 1 with
P ∤ sA, M := A·P·s (pairwise coprime), D := deg M = k + n + h, Φ(G) := |(R/G)^*|.

**Lemma 3.1 (reduction to three Frobenius conditions; PROVED).** Let f be monic irreducible of degree d ≥ 1, f ∤ M, with
(i) f ≡ −1 (mod A);  (ii) −P/A is a square in (R/f)^*;  (iii) s is a primitive root mod f.
Then ES_q^{(s)}(A, P) holds, by Prop 2.1 with Q = s^j, Type II shape at P.
*Proof.* (R/f)^* ≅ F_{q^d}^* is cyclic of order q^d − 1. By (iii) ⟨s² mod f⟩ is the subgroup of index gcd(2, q^d − 1),
i.e. the squares; by (ii) −P/A ≡ s^{2j₀}. Replace j₀ by j = j₀ + t(q^d − 1) with t so large that j ≥ 1 and
k + 2jh > n + d. Then f | P + A s^{2j}, and Prop 2.1 applies. ∎
(For q even, (ii) is automatic: every element of F_{2^r d} is a square.)

**Lemma 3.2 (small Kummer primes and the square condition are Dirichlet conditions; PROVED).** Let q be odd, f monic
irreducible of degree d with f ≡ −1 (mod A), f ∤ sP. Then
(ii) ⇔ (f/P) = τ := ε^{d(1+n+k)+k};
and for a prime ℓ | q − 1: s is an ℓ-th power mod f ⇔ (f/s)_ℓ = ε_ℓ^{dh}, ε_ℓ := (−1)^{(q−1)/ℓ} (= 1 for odd ℓ).
(For q even only the second statement is used; its sign is 1.)
*Proof.* (ii) ⇔ (−PA/f) = 1. DRINFELD_ES Lemma 1.1: (−1/f) = ε^d. Reciprocity for monic coprime Jacobi symbols
(Rosen, *Number Theory in Function Fields*, Thm 3.3; the same law as DRINFELD Prop 1.2): (P/f) = ε^{nd}(f/P),
(A/f) = ε^{kd}(f/A) = ε^{kd}(−1/A) = ε^{kd+k}. Multiply. Second statement: (s/f)_ℓ = ε_ℓ^{hd}(f/s)_ℓ by the ℓ-th power
law, and s is an ℓ-th power in the cyclic group (R/f)^* iff (s/f)_ℓ = s^{(q^d−1)/ℓ} mod f equals 1. ∎

**Lemma 3.3 (RH in progressions; standard).** For a nontrivial Dirichlet character χ mod a monic M' of degree D' ≥ 1,
|Σ_{f monic irreducible, deg f = d} χ(f)| ≤ (D' + 1) q^{d/2}/d. Also d·π_q(d) ≥ q^d − 2q^{d/2}, π_q(d) := #{monic
irreducible of degree d}.
*Proof.* L(u, χ) is a polynomial of degree ≤ D' − 1 (Rosen Prop 4.3) whose inverse roots have absolute value 1 or √q
(Weil), so |Σ_{deg F = d} Λ(F)χ(F)| ≤ (D' − 1)q^{d/2}. Prime powers f^{d/e}, e | d, e < d, contribute at most
Σ_{e ≤ d/2} e·π_q(e) ≤ Σ_{e ≤ d/2} q^e ≤ 2q^{d/2}. The second claim: d·π_q(d) = Σ_{e|d} μ(d/e)q^e. ∎
(This is FUNCTIONFIELD_ES Fact 5.2 in character form.)

**Lemma 3.4 (large Kummer primes, via Weil's character-sum bound; PROVED).** Let ℓ be a prime with ℓ | q^d − 1. Then
N_ℓ(d) := #{f monic irreducible, deg f = d, f ≠ s : s is an ℓ-th power mod f} ≤ (q^d/ℓ + (h − 1)q^{d/2})/d.
*Proof.* Each such f has exactly d roots α ∈ F_{q^d}, and T ↦ α induces R/f ≅ F_{q^d}, s mod f ↦ s(α); distinct f have
disjoint root sets. So d·N_ℓ(d) ≤ #{α ∈ F_{q^d} : s(α) ∈ (F_{q^d}^*)^ℓ} = (1/ℓ)Σ_{i=0}^{ℓ−1} Σ_{α: s(α) ≠ 0} ψ^i(s(α)),
ψ a character of F_{q^d}^* of order ℓ. The i = 0 term is ≤ q^d. For 1 ≤ i < ℓ, ψ^i has order ℓ and s is separable of
degree h ≥ 1, hence not a constant times an ℓ-th power in F_{q^d}[T]; Weil's bound (Lidl–Niederreiter, *Finite Fields*,
Thm 5.41) gives |Σ_α ψ^i(s(α))| ≤ (h − 1)q^{d/2}. ∎

**Theorem 3.5 (ES_q^{(s)} for every P; PROVED, effective, unconditional).** Let q be any prime power, A monic of degree
k ≥ 1, s monic irreducible of degree h with s ∤ A. Put δ := φ(q − 1)/(c_q (q − 1) Φ(A)) with c_q = 2 for q odd,
c_q = 1 for q even. For an odd prime d let m_d := ⌊d log q / log(2d + 1)⌋ and L_d := (1 + ln m_d)/(2d). Then for every
monic irreducible P of degree n ≥ 1 with P ∤ sA, the number G(d) of monic irreducible f of degree d satisfying
Lemma 3.1 (i)–(iii) satisfies
`d·G(d) ≥ (δ − L_d)·q^d − q^{d/2}·[2δ + 2^{ω(q−1)}(D + 1) + m_d(h − 1)] − δD.`
In particular G(d) > 0 as soon as L_d ≤ δ/2 and q^{d/2} ≥ (2/δ)[2δ + 2^{ω(q−1)}(D + 2) + m_d(h − 1)], which holds for every
prime d ≥ 2 log_q n + C(q, A, h). **Hence ES_q^{(s)}(A, P) holds for every such P**, with a Type II-shaped solution
whose modulus f has degree O_{q,A,h}(1) + 2 log_q n.
*Proof.* s is a primitive root mod f iff s is not an ℓ-th power mod f for every prime ℓ | q^d − 1. Split these ℓ into
ℓ | q − 1 and Λ_d := {ℓ | q^d − 1, ℓ ∤ q − 1}. For ℓ ∈ Λ_d, ord_ℓ(q) divides the prime d and is not 1, so it is d and
d | ℓ − 1; ℓ is odd (2 | q^d − 1 implies 2 | q − 1), so ℓ ≡ 1 (mod 2d). The elements of Λ_d are distinct numbers
2dj + 1, j ≥ 1, with product ≤ q^d, so |Λ_d| ≤ m_d and Σ_{ℓ∈Λ_d} 1/ℓ ≤ Σ_{j ≤ m_d} 1/(2dj) ≤ L_d. Then
G(d) ≥ G₁(d) − Σ_{ℓ ∈ Λ_d} N_ℓ(d), where G₁(d) counts f ∤ M of degree d with (i), (ii) and "s not an ℓ-th power mod f"
for all ℓ | q − 1. By Lemma 3.2 the indicator of these conditions on primes f ∤ M is
`(1/Φ(A)) Σ_{χ mod A} χ̄(−1)χ(f) · (1 + τ·(f/P))/2 · ∏_{ℓ | q−1} (1 − (1/ℓ)Σ_{i=0}^{ℓ−1} (ε_ℓ^{dh}(f/s)_ℓ)^i)`
(for q even, drop the middle factor). Expanding, the trivial character has coefficient δ and the other products are
characters mod M which are nontrivial (A, P, s are pairwise coprime; characters mod s of coprime orders ℓ multiply to
a trivial one only if each is trivial), with total absolute weight ≤ 2^{ω(q−1)}. The trivial character counts the
f ∤ M, at least π_q(d) − D/d of them. Lemma 3.3 (D' ≤ D) gives
d·G₁(d) ≥ δ(q^d − 2q^{d/2} − D) − 2^{ω(q−1)}(D + 1)q^{d/2}, and Lemma 3.4 gives
d·Σ_{Λ_d} N_ℓ(d) ≤ L_d q^d + m_d(h − 1)q^{d/2}. Subtract. For the last claim: L_d → 0, and the q^{d/2}-bracket is
linear in n (D = k + n + h; m_d = O(d)). Finally an f counted by G(d) is not s (f = s violates (iii)), so
Lemma 3.1 applies. ∎

*Remarks.* (1) Only Weil (RH for curves) is used — once through Dirichlet L-functions mod APs, once through the
character sums of Lemma 3.4. This is Bilharz's theorem (Artin's conjecture over F_q(T)) specialised to a fixed degree d
of the modulus and joined with two Dirichlet conditions; choosing d prime makes the Hooley tail trivial (Λ_d ⊂ 1 + 2dℤ).
(2) Compare ℤ (UNIT_ORBIT Thm 2.4): there |S| ≥ 4 and the Gupta–Murty sieve were needed, and the result is ineffective.
Over F the analogue of GRH is a theorem and |S| = 1 suffices, with an explicit degree bound for the certificate modulus.
Over ℤ the same argument would give ES^{(S)} with |S| = 1 under GRH (Assessment; not checked in detail).
(3) The degree of the *shot* is large: Q = s^j with j < q^d ≈ n²·C, so deg Q may be ≍ n² (vs. ES_q certificates of
degree ≤ 2n − k, §5). See §5 for whether this can be shortened.

## 4. The T1 question: anchor at ∞ = the character ε = χ(−1)

**Lemma 4.1 (sign of the shot modulus; PROVED).** Let q be odd and f monic of degree d with f ≡ −1 (mod A). Then
`(−A/f) = ε^{d(1+k)+k}.`
*Proof.* (−1/f) = ε^d; (A/f) = ε^{kd}(f/A) = ε^{kd}(−1/A) = ε^{kd+k} (reciprocity as in Lemma 3.2). ∎
(Over ℤ the analogue is (−1/r) = −1 for r ≡ −1 (mod 4): "−4 is a non-residue mod every shot modulus". This is the
mechanism T1 of UNIT_ORBIT §2. Here it holds iff ε = −1 and d(1+k)+k is odd.)

**Theorem 4.2 (exact-T1 dichotomy for the mute shot mechanism; PROVED).** Let q be odd, s ∤ A as in §3, and P any monic
polynomial of degree ≥ 1 coprime to sA. Call P *shot-solved* if some f, Q as in Prop 2.1 (with gcd(f, P) = 1) exist.
(a) If P is not a square, P is shot-solved (with f of every large prime degree d, as in Thm 3.5).
(b) If q ≡ 3 (mod 4) and k = deg A is odd, a square P = M² is never shot-solved.
(c) If q ≡ 3 (mod 4) and k is even, a square is shot-solved only through moduli f of even degree; with d odd
(e.g. the prime d of Thm 3.5) it is never shot-solved.
(d) If q ≡ 1 (mod 4), squares are shot-solved (Thm 3.5's argument with condition (ii) automatic, main term 2δ).
*Proof.* (a) Lemmas 3.1, 3.2 and Thm 3.5 used P prime only through: (·/P) is a nontrivial character mod P (true for the
Jacobi symbol iff the monic P is not a square), Jacobi reciprocity (valid for monic coprime P, f), and f ≠ P, P ∤ X in
Prop 2.1 (replace by gcd(f, P) = 1, which Prop 2.1's identity needs only for the Type II shape; the identity itself holds
for any P coprime to f... in fact gcd(f, P) = 1 is forced as f | P + AQ² and gcd(f, AQ) = 1 would give f | P ⇒ f | AQ²).
(b), (c) If a prime f' | f divides M² + AQ² with f' ∤ Q (f' ∤ Q since f' | Q would give f' = s | M, excluded), then
−A ≡ (M/Q)² (mod f'), so (−A/f') = 1 for every prime f' | f, hence (−A/f) = 1, contradicting Lemma 4.1 (= −1 when
ε = −1 and d(1+k)+k odd, i.e. k odd, or k even and d odd). (d) For P = M², (ii) reads (f/M²) = 1 = τ (ε = 1). ∎
Over ℤ the ES^{(S)} mechanism had exactly this dichotomy (UNIT_ORBIT Thm 2.4(a)/(b)); over F it holds with |S| = 1,
effectively, and **the T1 exists iff the anchor is alive: ε = χ(−1) = −1**. For q ≡ 1 (mod 4) the monic normalisation
at ∞ pins nothing (−1 is a square in F_q), consistent with FUNCTIONFIELD_ES §4 (no square-class obstruction).
