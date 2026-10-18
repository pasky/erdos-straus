# MODP_RECIPROCITY — higher reciprocity in the mod-p coordinates; Gaussian-representation certificates (task O265)

Status labels as in DISCOVERIES.md. **ES is not solved, here or anywhere.** Memos: BRAINSTORM/z35_*.md. Scripts: scripts/z35_*.
Spark relay on O263 (CLASS_FORCING.md) sparks 1 and 4. Notation: p ≡ 1 (4) prime, p = a² + b², a odd, b even (a, b > 0
unless said otherwise); i_p := a·b⁻¹ mod p (a square root of −1 mod p; replacing b by −b gives −i_p, i.e. π ↔ π̄);
(x/p)_4 := x^{(p−1)/4} mod p ∈ μ₄(F_p) = {±1, ±i_p}.

## 0. Iteration log
* v0 (brief's idea). "In mod-p coordinates the modulus is p and the small objects are the certificate parameters; their n-th
  power symbols mod π are independent data, so maybe the target w ≡ −1 (mod 4d) is a power-class statement mod π."
  §1 writes the b = 1 line in mod-p / least-residue coordinates (m, g, d) with 4md = p + g. Screen result: the residue-symbol
  content of a certificate is (i) quadratic part: a function of the parameters mod 8 (Jacobi), i.e. the T1 sign, (ii)
  quartic part: a function of (a, b) modulo the parameters (Gauss–Dirichlet–Burde), a genuine extra datum — but the event does
  not depend on it. The target is additive (an equation of height 1), not multiplicative. Modification → v1.

## 1. The b = 1 line in mod-p (least-residue) coordinates, and the residue-symbol content of one certificate

**Proposition 1.1 (three faces of the b = 1 line; PROVED, elementary; (ii) is (J)85's least-residue form specialised, (iii)
the Type II e-slice of CLASS_FORCING §1).** For p ≡ 1 (4) the following are equivalent:
(i) ∃ d ≥ 1 and w | p + 4d with w ≡ −1 (mod 4d), w < p + 4d (López Type A; SS8 Prop 1.3);
(ii) ∃ m ≥ 1 such that the least positive residue g_m := (−p mod 4m) divides m + 1;
(iii) ∃ g ≡ 3 (mod 4) such that (p + g)/4 has a divisor m ≡ −1 (mod g).
The bijection is (d, w) ↦ (m, g) = (cg − 1, (p + 4d)/w) with c := (w + 1)/(4d); inverse d = (p + g)/(4m), c = (m + 1)/g,
w = 4cd − 1. In all three forms the certificate is one equation **4md − g = p, g | m + 1** in three positive integers; it is
the *height-one* solution of the congruence 4md ≡ g (mod p).
*Proof.* (4cd − 1)g = p + 4d ⟺ 4d(cg − 1) = p + g. From (i): g := (p + 4d)/w; as w ≡ 3 (4) and p + 4d ≡ 1 (4), g ≡ 3 (4),
g ≥ 3, so m = cg − 1 ≥ 2, 4m | p + g and g | m + 1; since 0 < g ≤ m + 1 < 4m, g is the least residue g_m. Conversely (ii)
gives c = (m + 1)/g, d = (p + g)/(4m) ≥ 1, w = 4cd − 1 with wg = p + 4d, and w < p + 4d as g > 1 (g = 1 would need
p ≡ −1 (4)). (iii) is (ii) read with g fixed. ∎ (`scripts/z35_checks.py` (1): the (d, w)- and (m, g)-sets coincide for all
1125 primes p ≡ 1 (4) < 2·10⁴.)

*Regimes.* md ≈ p/4 and g ≤ m + 1. (R1) m ≤ X bounded: the event is "p mod 4m ∈ {−g : g | m + 1}", a congruence (B1).
(R2) d ≤ X bounded: CLASS_FORCING Thm 6.1 (HC). (R3) the balanced range m, d = p^{1/2 + o(1)}, where m, d, g are of the same
size as a, b — the only place where p's Gaussian data and the certificate live on one scale.

**Proposition 1.2 (residue-symbol content of one certificate; PROVED).** Let (m, g, d, c, w) be as in Prop 1.1, write
d = 2^s d′, m = 2^r m′ (d′, m′ odd).
(a) *(Quadratic part = parameters mod 8.)* (w/p) = −1; (g/p) = (−d/g); (d′/p) = (−g/d′); (m′/p) = (−g/m′); (2/p) = (−1)^{(p²−1)/8}.
So every quadratic symbol mod p of certificate data is a Jacobi symbol among the parameters (and p mod 8): **the sign layer is
not a free datum of p once the parameters are given** — it is the T1 sign (ET Prop 1.6; CLASS_FORCING Lemma 2.2(a)).
(b) *(Quartic part = Gaussian data modulo the parameters.)* (w/p)_4·(g/p)_4 = (2/p)·(d/p)_4 in μ₄(F_p). For an odd prime
q ≠ p, (q/p)_4 ≡ [q/π]_4 (mod π) is a function of (a mod q, b mod q) (and of the choice π ↔ π̄): for q ≡ 1 (4), q = c_q² + d_q²
(c_q odd), **Burde's law** (p/q)_4(q/p)_4 = ((a c_q − b d_q)/q) when (p/q) = 1 [Burde, J. reine angew. Math. 238 (1969);
`z35_checks.py` (2): 2158 pairs, 0 violations], with (p/q)_4 a function of p mod q; for q ≡ 3 (4), [π/q]_4 ≡ π^{(q²−1)/4} =
(π̄/π)^{(q+1)/4} (mod q), a function of the point (a : b) ∈ P¹(F_q). Hence the quartic symbols of w, g, d, m are functions of
(a, b) modulo 16·rad(mdg) — data of p NOT determined by p mod anything (Thm 2.1(c)(ii) of CLASS_FORCING: Frob_p in
ℚ(i, q^{1/4}) is non-abelian information).
(c) *(The event ignores (b).)* The certificate condition (4md − g = p, g | m + 1) involves only integers; (b) is a
consequence of it, never an input. (`z35_checks.py` (3): the identity in (b) and (w/p) = −1 on all 2716 certificates p < 5000.)
*Proof.* (a) Jacobi reciprocity with p ≡ 1 (4): (x/p) = (p/x) for odd x > 0; p ≡ −4d (mod g) (as m ≡ −1 (g)), p ≡ −g (mod d′)
and (mod m′) (as 4md = p + g). (w/p) = −1 is CLASS_FORCING Lemma 2.2(a) (SS8). (b) wg ≡ 4d (mod p) and 4^{(p−1)/4} = 2^{(p−1)/2}.
The q ≡ 3 (4) formula: in ℤ[i]/(q) ≅ F_{q²}, π^q ≡ π̄, so π^{(q²−1)/4} = (π^{q−1})^{(q+1)/4} = (π̄/π)^{(q+1)/4}; quartic
reciprocity [q/π]_4 = [π/q]_4 for primary π and q ≡ 3 (4) (Ireland–Rosen Thm 9.9.? / Lemmermeyer Thm 6.9) transfers it. ∎

**Answer to goal (1) of the brief.** In mod-p coordinates the decisive condition is the *height-one* equation 4md − g = p
(equivalently: the least residue −p mod 4m divides m + 1). Its residue-symbol content splits into a quadratic part, which is
forced and equals the T1 sign (a), and a quartic part, which is genuine Gaussian information (b) but is an *output* of a
certificate, not a criterion for one (c). The target w ≡ −1 (mod 4d) is additive — "w lies in an arithmetic progression of
difference 4d inside [1, p)" — whereas power classes are cosets of multiplicative subgroups of F_p^×. So **no**: the target is
not a power-class statement mod π; reciprocity enters only through the quadratic sign it already forces.
