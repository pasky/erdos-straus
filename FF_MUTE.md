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
(P3) The X8 framing "sterile points vs none" fails for q odd: the mute mechanism also has no finite covering (Prop 5.4;
in characteristic 2 it does have one, and its sterile set is Haar-null while that of DEPTH_ASPECT Thm 2.5 has positive
measure — independent R195 repairs M1, M2). The real
separation is Frobenius-firing (global character (f/P)) vs box-firing (divisors of f + 1). (§§5, 7)

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
s | P + AQ² and s | Q give s | P; R195 m2), s ∤ A, s ∤ P. If σ < 2c, v_s(RHS) = σ, so v_s(X) = σ and v_s(z) = 2σ − 2c (even).
If σ ≥ 2c then v_s(X) ≥ 2c and v_s(z) ≥ 0. *Shape:* gcd(f, P) = 1 (a prime g | f, P would divide AQ², but g ∤ A as f ≡ −1 (mod A), and
g ∤ Q as s ∤ P), so Ef = P + AQ² gives E ≢ 0 (mod P), and
AX = P + E gives P ∤ X; v_P(Y) ≥ 1 and v_P(z) ≥ 1 (both = 1 unless P | f + 1). ∎
(Degree condition: if instead deg(AQ²) < n the same formulas work with deg E = n − d, X of degree n − k; the only
excluded situation is deg E = n, where P + E has leading coefficient 2. Below we always take Q large.
Independent R195 repair m1: precisely, the construction is valid iff deg(AQ²) ≠ n + d — also for deg(AQ²) = n (E then
need not be monic, but P + E is) and for n < deg(AQ²) < n + d; in general deg X = max(n, deg E) − k and
−v_∞(z) = n − k + (max(n, deg E) + d − deg(AQ²)) ≥ n − k. The §6 least-shot counts use all these regimes.)

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
(Rosen, *Number Theory in Function Fields*, Thm 3.3 for monic irreducibles, extended multiplicatively to composite monic
arguments — independent R195 repair m3; the same law as DRINFELD Prop 1.2): (P/f) = ε^{nd}(f/P),
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
whose modulus f has degree ≤ 4 log_q n + O_{q,A,h}(1) (Bertrand's postulate; (2 + o(1)) log_q n by the prime number
theorem). *(R195 M1 repair: the original "2 log_q n + O(1)" silently assumed a prime within O(1) of 2 log_q n.)*
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
Over ℤ the same argument would give ES^{(S)} with |S| = 1 under GRH (Assessment; not checked in detail. Independent
R195 repair m4: over ℤ there is no prime-degree trick; one needs Hooley's full GRH argument for all Kummer fields
ℚ(ζ_ℓ, s^{1/ℓ}) with Brun–Titchmarsh for the middle range, combined with a congruence and a quadratic-character
condition — a Lenstra-type generalised Artin statement.)
(3) The *shot* may be high: Lemma 3.1 takes the least j ≡ j₀ (mod q^d − 1) with j ≥ 1 and 2jh > n + d − k, so
j < 2q^d + (n + d)/(2h) = O(q^d + n), i.e. deg Q = O(n⁴) (Bertrand) or n^{2+o(1)} (PNT), whereas the ES_q modulus has degree ≤ 2n − k (§5).
Numerically a few shots suffice (§6).

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
Jacobi symbol iff the monic P is not a square), Jacobi reciprocity (valid for monic coprime P, f), and "f ∤ P, P ∤ X" in
Prop 2.1. For prime f ≠ s with f | P + AQ², f | P would give f | AQ², impossible (f ≡ −1 mod A); and for every prime
ℓ | P, Ef ≡ AQ² ≢ 0 (mod ℓ), so ℓ ∤ E and ℓ ∤ X = (P + E)/A: Type II shape at every prime of P. The identity and the
parity computation of Prop 2.1 do not use primality of P.
(b), (c) If a prime f' | f divides M² + AQ² with f' ∤ Q (f' ∤ Q since f' | Q would give f' = s | M, excluded), then
−A ≡ (M/Q)² (mod f'), so (−A/f') = 1 for every prime f' | f, hence (−A/f) = 1, contradicting Lemma 4.1 (= −1 when
ε = −1 and d(1+k)+k odd, i.e. k odd, or k even and d odd). (d) For P = M², (ii) reads (f/M²) = 1 = τ (ε = 1). ∎
Over ℤ the ES^{(S)} mechanism had exactly this dichotomy (UNIT_ORBIT Thm 2.4(a)/(b)); over F it holds with |S| = 1,
effectively, and **for k odd the mechanism T1 exists iff the anchor is alive: ε = χ(−1) = −1** (for k even and
ε = −1 only odd-degree moduli are excluded at squares; (c) does not prove that every square is solved by even-degree
moduli — R195 m3). For q ≡ 1 (mod 4) the monic normalisation
at ∞ pins nothing (−1 is a square in F_q), consistent with FUNCTIONFIELD_ES §4 (no square-class obstruction).

## 5. What exactly fails when S = ∅

**Proposition 5.1 (ES_q is a bounded search; PROVED, elementary; FF form of (J)25 Prop 6.1).** Every Type II datum
(a, b, c, d) of ES_q(A, P) (FUNCTIONFIELD_ES Prop 4.1: P = Aabd − E, Ec = a + b, X = abd) has modulus
f = Aacd − 1 of degree ≤ 2n − k, and f | P + Aa²d.
*Proof.* Ef = P + Aa²d (FF Prop 4.1). deg X = n − k (NC), so 2deg a + deg d ≤ 2(n − k), deg(Aa²d) ≤ 2n − k, and
deg P = n ≤ 2n − k. ∎
So at fixed P, ES_q is a search over finitely many shots P + Aa²d (deg(a²d) ≤ 2(n − k)), each with its own modulus
condition f ≡ −1 (mod Aad). In the mute variant the shots P + AQ² are indexed by the infinite monoid ⟨s⟩ and the
modulus condition is the fixed f ≡ −1 (mod A); Cor 2.2 says a mute shot is an ES_q solution iff f ≡ −1 (mod AQ).

**Proposition 5.2 (coverage per modulus; PROVED).** Let f be monic irreducible of degree d, f ≡ −1 (mod A), f ≠ s.
(a) (mute) The residues P mod f made solvable by a mute shot with modulus f form the coset −A·⟨s² mod f⟩, of size
ord_f(s²) — equal to (q^d − 1)/2 (q odd) when s is a primitive root mod f.
(b) (ES_q, Type II) The residues P mod f for which f is the modulus of some Type II datum lie in
−A·{a²d : a, d monic, ad | (f + 1)/A} mod f, a set of size ≤ τ₃((f + 1)/A) = q^{o(d)}
(number of ordered monic factorisations (f + 1)/A = a·c·d).
*Proof.* (a) Prop 2.1: P ≡ −AQ² (mod f), Q ∈ ⟨s⟩. (b) f = Aacd − 1 forces ad | (f + 1)/A, and P ≡ −Aa²d. ∎
So a mute modulus fires on half of the unit classes (q odd; on all unit classes for q even, where squaring is bijective —
independent R195 repair M1), an ES_q modulus on a q^{−d+o(d)} fraction — FF form of (J)25's
"Box ⊆ ES^{(S)} coset".

**Proposition 5.3 (the firing condition is Frobenius for mute, a divisor condition for ES; PROVED for (a)).**
(a) For fixed P, "f fires" in the mute variant (with s primitive mod f) is the Chebotarev condition of Thm 3.5: a
Dirichlet condition mod A·P·s plus Kummer non-splitting in F(μ_ℓ, s^{1/ℓ}). The P-dependence enters only through the
quadratic character (f/P) — a global character of f, by reciprocity.
(b) For ES_q the condition is P ≡ −Aa²d (mod f) for a factorisation (f + 1)/A = a·c·d: it depends on the factorisation
of the shifted prime f + 1; no description as a condition on Frob_f in a fixed extension is known (Assessment, not a
nonexistence proof — R195 m7; same mechanism as B2 —
"the modulus is part of the solution"; the S = ∅ orbit {1} has only the single fixed-modulus shot P + A).

**Proposition 5.4 (the mute shot mechanism has no finite covering, yet solves every admissible irreducible P; PROVED;
R195 M2 repair: composite moduli handled, scope narrowed).** Let q be odd and 𝓕 any finite set of pairs (f, Q) as in
Prop 2.1 (f prime or composite; each valid on the class P ≡ −AQ² mod f, for deg P large). Let g₁, …, g_r be the distinct
primes dividing some f ∈ 𝓕. Then the P with −PA a non-square mod every g_i form a nonempty union of unit classes mod
g₁⋯g_r containing irreducible P of every large degree, and no (f, Q) ∈ 𝓕 fires on them. So **no finite set of mute
shot families covers ES_q^{(s)}(A, ·)**, although Thm 3.5 proves it at every irreducible P ∤ sA.
*Proof.* CRT over the distinct primes g_i (each (R/g_i)^* has non-squares; g_i ∤ A since f ≡ −1 mod A). Suppose
P ≡ −AQ² (mod f) and let g_i | f. If g_i ∤ Q, then −PA ≡ (AQ)² is a square mod g_i, contradiction. If g_i | Q, then
g_i = s and s | P + AQ² gives s | P, contradicting "−PA is a non-square mod s". The classes are unit classes,
so they contain irreducibles of every large degree (Fact 5.2). ∎
*Reading (scoped).* In the profinite-unit space R̂^* (FUNCTIONFIELD_ES2 §0.1, scoped to shot families), the points x with
−xA a unit non-square mod every prime g ∤ A, **including g = s**, are sterile for every shot (prime or composite
modulus: every prime divisor g of an admissible f satisfies g ∤ A, and g = s is handled as in the proof above);
this set is nonempty and Haar-null. (Independent R195 repair m6: the earlier "g ∤ As" was wrong — f = s^m with
s^m ≡ −1 (mod A) is admissible with Q = 1, e.g. q = 3, A = T, s = T + 2, f = s³ = T³ − 1 fires on P ≡ −A (mod s³);
`scripts/review_fm_sterile.py`.) Polynomials are not points of R̂^*; what matters is the
actual inputs: **no admissible irreducible P fails the mechanism** (Thm 3.5), because f ↦ (−PA/f) = ±(f/P) is a
nontrivial global character mod P and takes both values on primes f ≡ −1 (mod A) of every large degree. So the theorem
is proved by a global argument (reciprocity + Weil) that **no finite covering by shot families can replace**; this is a
statement about finite shot coverings only, not about congruence arguments in general (the proof itself uses
congruence characters). In q ≡ 3 (mod 4), k odd, the squares M² are exactly the monic inputs at which this character is
trivial, and they are exactly the non-shot-solved P (Thm 4.2). This is the FF version of B1 + B5 for the mute
*mechanism*, with the theorem on the other side. (Independent R195 repair M2: what is proved is that a mechanism with a
nonempty but *Haar-null* sterile set and no finite covering can be a theorem at every admissible P; it says nothing
about a sterile set of positive measure, which is the ES_q situation of DEPTH_ASPECT Thm 2.5.)

*Remark 5.5 (characteristic 2 has a finite covering; independent R195 repair M1).* For q even, squaring is bijective on
(R/f)^*, so if s is a primitive root mod a prime f ≡ −1 (mod A), f ≠ s, then −A⟨s² mod f⟩ = (R/f)^*: the ord_f(s)
families (f, s^j) cover every P with f ∤ P once n > k + 2h(ord_f(s) − 1) (low-shot regime), and a second such prime
f₂ covers P = f. So Prop 5.4 genuinely needs q odd; in characteristic 2 the mute mechanism has **no** sterile points
and X8's "sterile vs none" is literally right. Example: q = 2, A = T, s = T + 1, f₁ = T² + T + 1, f₂ = T³ + T² + 1 —
10 families cover every irreducible P of degree 14–17 (`scripts/review_fm_char2cover.py`, exact verification).

## 6. Numerics (EVIDENCE; all solutions verified exactly)

Scripts: `fm_poly.py` (F_p[T] arithmetic), `fm_mute.py` (orbit/discrete-log search + exact verification),
`fm_count.py` (Lemma 3.2 sign formulas and G(d) vs Thm 3.5), `fm_t1.py` (Thm 4.2 on all monic P), `fm_minq.py`
(least shot height, factorisation by sympy — independent of the orbit search). Outputs `data/fm/*.txt`.
Verification of every reported solution: A·X·Y·Zn = P(Y·Zn + X·Zn + Q²·X·Y), X, Y, Zn monic, v_s(Zn/Q²) even when
negative, NC degrees (min = n − k), Type II at P.

* **All irreducible P solved** (`fm_mute.py`, s = T + 1 unless noted; P ∤ sA): q = 3, A = T, n ≤ 7 (506 P); q = 3,
  A = T², n ≤ 10 (9379 P); q = 3, A = T² + 1, n ≤ 7; q = 3, A = T, s = T³ + 2T + 1, n ≤ 9 (3500 P); q = 5, A = T, s = T + 2,
  n ≤ 6 (3407 P); q = 5, A = T², n ≤ 7 (14 564 P); q = 7, A = T, n ≤ 6 (23 630 P); q = 11, A = T, n ≤ 4 (4134 P);
  q = 2, A = T³, n ≤ 14 (2535 P); q = 2, A = T⁴ + T + 1, s = T² + T + 1, n ≤ 13 (1371 P). 0 unsolved, 0 verification
  failures. This includes **every known ES_q failure** in these ranges (FUNCTIONFIELD_ES §3: q = 3, A = T², n = 3, 4, 5;
  q = 5, A = T, n ≤ 4; q = 5, A = T², n ≤ 7; q = 7, A = T, n ≤ 6). Least modulus degree d ≤ 7 throughout.
* **Lemma 3.2** (`fm_count.py`): 0 mismatches of both sign formulas on every f ≡ −1 (mod A) of degree d (q = 3, A = T,
  d = 7; q = 3, A = T², d = 7; q = 5, A = T, d = 5; q = 3, A = T, s = T³ + 2T + 1, d = 9; several P each).
  **G(d) tracks δq^d/d**: e.g. q = 3, A = T, d = 7: G = 40, 33, 36, 40 against 39.1; q = 3, A = T², d = 7: 13, 15, 11
  against 13.0; q = 5, A = T, d = 5: 31, 37 against 39.1. (The explicit lower bound of Thm 3.5 is negative at these
  small d — RH error terms dominate — so these counts are evidence for the main term only; the theorem itself covers
  every n by the bound with a larger prime d. For q = 3, A = T, h = 1 the bound is positive at d = 11 for n ≤ 3, d = 13
  for n ≤ 17, d = 17 for n ≤ 271, d = 23 for n ≤ 9862, d = 29 for n ≤ 307 381 — independent R195 repair m2.)
* **Thm 4.2** (`fm_t1.py`, all monic P coprime to sA): q = 3, A = T (deg P ≤ 6, f-deg ≤ 7): 0/17 squares, 468/468
  non-squares shot-solved; q = 3, A = T³: same; q = 7, A = T (deg ≤ 4): 0/41 squares, 2016/2016 non-squares;
  q = 3, A = T² (k even): 17/17 squares, all via even d only; q = 5, A = T and A = T²: 19/19 squares, 480/480 non-squares.
* **Least shot height** (`fm_minq.py`; all monic divisors f ≡ −1 (mod A) of the shot, prime or composite — R195 M3
  repair; the first version tested prime f only): the least j with P + A s^{2j} giving a valid solution of Prop 2.1's
  formulas (checked exactly) is small, with no growth trend in these ranges: q = 3, A = T, n ≤ 9: max 7, mean 0.30 at
  n = 9 (85% use j = 0, ES's own shot P + A); q = 3, A = T², n ≤ 8: max 15, mean 1.33 at n = 8 (60% j = 0); q = 5, A = T,
  n ≤ 6: max 13, mean 0.82 at n = 6 (65% j = 0). Thm 3.5's argument allows j up to O(q^d + n); the data say a few shots
  suffice (EVIDENCE, not a proof). Beyond j = 0, 2–5% of the least shots are ES_q-integral (Cor 2.2: f ≡ −1 mod A·s^j).
  (Independent R195 repair m1: these least shots include the regimes deg AQ² = n and n < deg AQ² < n + d, valid since
  Prop 2.1's construction works whenever deg AQ² ≠ n + d — see the Degree-condition remark; restricted to
  deg AQ² > n + d or < n, q = 3, A = T², n = 8 gives max 18, mean 2.31. Reproduced independently in
  `data/review_fm/minj_*.txt`.)
* **Low degrees n < k** (`fm_mute.py … nmin = 1`, `data/fm/mute_lowdeg.txt`; R195 m1): the runs above start at n = k;
  the omitted n < k (q = 3, A = T², T² + 1; q = 5, A = T²; q = 2, A = T³, T⁴ + T + 1): all 11 P solved and verified.
* The column "s-primitive-at-chosen-f" in `data/fm/mute_runs.txt` used a wrong test (R195 M4) and is not used here;
  `fm_count.py` now handles characteristic 2 (q = 2, A = T, s = T + 1: G(3) = 2, G(7) = 18 vs main term 2.7, 18.3).

## 7. Verdict (O195 checkpoint 1)

PROVED: (Thm 3.5) for every q, A, and one mute prime s ∤ A, ES_q^{(s)}(A, P) holds for **every** monic irreducible
P ∤ sA, unconditionally and effectively (certificate modulus of degree ≤ 4 log_q n + C(q, A, deg s), (2 + o(1)) log_q n by PNT); (Thm 4.2) for k odd the
mechanism is exact-T1 iff ε = χ(−1) = −1 (k even, ε = −1: odd-degree moduli excluded at squares), no T1 for
q ≡ 1 (mod 4); (Prop 5.4, q odd) the mechanism admits no finite covering by its shot families, yet is a theorem at every
admissible irreducible P (in characteristic 2 it does admit one, Remark 5.5 — independent R195 repair M1).

**Correction to the X8 framing (Assessment).** X8 hoped for "sterile points (ES_q) vs none (mute)". That is not the
separation: for q odd the mute mechanism *also* has profinite sterile points and no finite shot covering (Prop 5.4), and DEPTH_ASPECT Thm 2.5 is a statement
about profinite points (no finite linear covering), not about actual failing P. (Independent R195 repairs M1, M2: in
characteristic 2 the mute mechanism has no sterile points and a finite covering (Remark 5.5); and the mute sterile set
is Haar-null whereas Thm 2.5's has positive measure, so a measure-theoretic version of X8 — positive-measure sterile set
for ES_q vs null for mute — is not refuted by this example.) The true separation is:
**mute: the firing condition at a modulus f is a Frobenius condition whose P-dependence is a global character
((f/P) by reciprocity), so Chebotarev + RH force firing at every global P; ES_q (S = ∅): the firing set of f is the
box −A·{a²d : ad | (f+1)/A} (Prop 5.2(b)), a q^{−d+o(d)} fraction defined by the factorisation of f + 1, for which no
Frobenius description is known (not proved impossible; R195 m7).** The mute place is exactly the device that replaces "divisors of f + 1" by "a finitely
generated group reduced mod f" (Kummer theory), and that is what converts the lottery into a theorem.

Not an opening for ES (Assessment): the passage back to ES_q is Cor 2.2's growing modulus f ≡ −1 (mod A·Q) — B2,
exactly as over ℤ (UNIT_ORBIT Prop 6.1). The FF model makes no claim about ES_q(A, P) for actual P.

**The reverse question (which instances lack every mute surrogate; PROVED from Thms 3.5, 4.2).** For prime P: none —
every s ∤ AP works. Among all monic P coprime to A, for q ≡ 3 (mod 4) and k odd, the P lacking a mute *shot* for
**every** choice of s (and every S coprime to P — independent R195 repair m5 —, since the proof of Thm 4.2(b) uses only
f ∤ Q and s ∤ P) are exactly the squares; for
q ≡ 1 (mod 4) none. The certificate-size picture: ES_q Type II moduli have degree ≤ 2n − k (Prop 5.1; this bounds the modulus, not
the denominators — e.g. the E = 1 solution has a denominator of degree 3n − 2k; R195 M7 repair); the mute proof uses
modulus degree O(log n) but shot height O(q^d + n) (Thm 3.5 Remark 3), while numerically a few shots suffice (§6).
