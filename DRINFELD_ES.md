# DRINFELD_ES — degree-k Diff-parity over F_q(T): rank-k Drinfeld modules, the ∞-coordinate, and odd-degree descent (task O181, spark relay H)

Status: in progress (O181). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on LDP_DEEP.md (O177, CLAIMED, under review), KUDLA_ES.md (reviewed), FUNCTIONFIELD_ES.md / _ES2.md
(reviewed), FUNCTIONFIELD_ES3.md (O173, branch side-agent/ff-sterile-point). Memos `BRAINSTORM/bsH_*.md`, scripts
`scripts/bsH_*`.

Notation (FUNCTIONFIELD_ES §1): R = F_q[T], q = p^r, A monic of degree k_A, P monic irreducible of degree n.
Type II datum (a, b, c, d) of P: monic, gcd(a, b) = 1, c | a + b, E := (a + b)/c, P = A·a·b·d − E; the
**Type II modulus** is f := A·a·c·d − 1 (monic, f ≡ −1 mod Aad), and E·f = P + A·a²·d (FF Prop 4.1).
For k | q − 1, (x/g)_k is the k-th power residue (Jacobi) symbol in μ_k ⊂ F_q^*, g monic (Rosen, *Number Theory
in Function Fields*, Ch. 3). F_∞ = F_q((1/T)).

## 0. Iteration log
(I1) Orchestrator's construction: a degree-k chart in which ES_q certificates are reduced norms from the definite
degree-k algebra D_{P,∞}^{(k)} (inv_P = 1/k, inv_∞ = −1/k; endomorphism algebra of supersingular rank-k Drinfeld
modules at P). Simplest degree-k CM datum attached to a certificate: the Kummer element f^{1/k}. §1 computes its
local behaviour at P. Result: always split at P for odd k (§1, Thm 1.3) — the order-k analogue of Diff = {P} is
Diff = ∅.

## 1. The k-th power law of Type II moduli

**Lemma 1.1 (constant symbols are degree characters; PROVED, elementary).** For λ ∈ F_q^*, k | q − 1 and g monic,
(λ/g)_k = (λ^{(q−1)/k})^{deg g}. *Proof.* For g = ℓ prime of degree d, (λ/ℓ)_k ≡ λ^{(q^d−1)/k} and
(q^d − 1)/(q − 1) = 1 + q + … + q^{d−1} ≡ d (mod q − 1); λ^{(q−1)/k} has order | k. Multiplicativity in g. ∎

**Prop 1.2 (k-th power law; PROVED).** Let k | q − 1, ε_k := (−1)^{(q−1)/k} ∈ {±1}. For every Type II datum of P,
`(P/f)_k = ε_k^{(1 + deg f)(1 + deg Ad) − 1}.`
For k = 2 this is FUNCTIONFIELD_ES Prop 4.1. **For k odd (q odd), ε_k = 1, so (P/f)_k = 1: P is a k-th power
residue (Jacobi sense) modulo every Type II modulus.**
*Proof.* gcd(f, Aad) = 1 since f ≡ −1 (mod Aad); E f = P + Aa²d gives P ≡ −Aa²d (mod f). Reciprocity for monic
coprime x, y (Rosen Thm 3.5): (x/y)_k = ε_k^{deg x·deg y}(y/x)_k; Lemma 1.1 gives (−1/y)_k = ε_k^{deg y}. Then
(−1/f)_k = ε_k^{deg f}; (Ad/f)_k = ε_k^{deg Ad·deg f}(f/Ad)_k = ε_k^{deg Ad·deg f}(−1/Ad)_k = ε_k^{deg Ad(1 + deg f)};
(a/f)_k² = (ε_k^{deg a deg f}(−1/a)_k)² = 1. Multiply. ∎

**Theorem 1.3 (Kummer CM data of certificates are ordinary at P; PROVED from Prop 1.2).** Let k be odd, k | q − 1,
f a Type II modulus of P (P ∤ f). Then (f/P)_k = 1, i.e. P splits completely in F(f^{1/k}). Consequently
F(f^{1/k}) (whenever it has degree k) does **not** embed into the central division algebra D of degree k over F
with Ram(D) = {P, ∞} (any invariants of exact order k): f^{1/k} is never a "supersingular endomorphism at P".
*Proof.* (f/P)_k = ε_k^{deg f·n}(P/f)_k = 1 by Prop 1.2 (ε_k = 1). A degree-k field K embeds in a central division
algebra of degree k iff K ⊗ F_v is a field at every v ∈ Ram(D) (Pierce §13.3 / Reiner Thm 32.15: local degree
[K_w : F_v] must be a multiple of the local index, here k). At P, (f/P)_k = 1 and P ∤ f mean that x^k − f splits
over F_P, so K ⊗ F_P ≅ F_P^k. ∎
*Contrast (KUDLA_ES Thm 1.4, (J)13).* Over ℚ a Type II certificate gives (−f/p) = −1: p is inert in ℚ(√−f), the CM
point is supersingular, Diff(T) = {p}. Over F_q[T] the degree-2 analogue is supersingular only on the
degree-parity sub-families of q ≡ 3 (mod 4) (FF Prop 4.1), and the degree-k analogue (odd k) **never**.

**Numerics (EVIDENCE; `scripts/bsH_kpower_law.py`, own F_p[T] arithmetic in `scripts/bsH_ff.py`; every datum is
re-verified as an ES_q solution A·XYZ = P(XY + YZ + ZX)).** k = 3:
| q, A, n | P | #P | #P with N_II = 0 | #Type II data | (P/f)₃ ≠ formula | (f/P)₃ = 1, ω, ω² | control (g/P)₃ (random monic g, same deg) |
|---|---|---|---|---|---|---|---|
| 7, T, 3 | irreducible | 112 | 45 | 241 | 0 | 241, 0, 0 | 82, 90, 69 |
| 7, T, 4 | irreducible | 588 | 116 | 2596 | 0 | 2596, 0, 0 | 902, 846, 846 |
| 7, T², 4 | irreducible | 588 | 513 | 192 | 0 | 192, 0, 0 | 72, 56, 64 |
| 13, T, 3 | irreducible | 728 | 453 | 813 | 0 | 813, 0, 0 | 269, 298, 246 |
| 7, T, 3 | Q³ (Q ≠ T linear) | 6 | 0 | 42 | 0 | 42, 0, 0 | — |
| 13, T, 3 | Q³ | 12 | 4 | 38 | 0 | 38, 0, 0 | — |
| 7, T, 4 | Q² (control k = 2, q ≡ 3 mod 4) | 21 | 17 | 8 | 0 | — | — |
**T1_k reversed (EVIDENCE + PROVED mechanism).** Cubes are *enriched*, not sterile: mean N_II = 7.0 at Q³ vs 2.15 at
irreducible P (q = 7, n = 3), 3.2 vs 1.12 (q = 13). Mechanism: Prop 1.2 imposes (P/f)₃ = 1, a condition of
probability ≈ 1/3 for prime P and automatic for P = Q³, so k-th powers gain a factor ≈ k. Over ℚ the forced value is
(p/f) = −1, so squares get factor 0 (T1). The sign of the effect is the order of the target −1 in F_q^*/F_q^{*k}.

## 2. The ES_q surface carries Brauer classes of order q − 1 over the base — and they vanish on monic integral points

Bright–Loughran (arXiv:1908.02526, Prop 2.5, 2.6; checked in `sources/`): for the surface
U_λ : u₁u₂u₃ = λ^{−1}(u₁u₂ + u₁u₃ + u₂u₃), i.e. λ = 1/u₁ + 1/u₂ + 1/u₃, over any field k (their proof uses purity
and Br G_m² ≅ ℚ/ℤ(−1); in characteristic p we only use the prime-to-p part, Assessment), Br Ũ/Br k is
represented by α_ζ = (−u₁/u₃, −u₂/u₃)_ζ, ζ ∈ μ(k). Over ℚ, μ = ±1 and only the quaternion class exists; over
ℚ(ζ_m) the order-m classes exist but corestrict to constants on ℚ-points (LDP_DEEP A.1). **Over F = F_q(T),
μ(F) = F_q^* = μ_{q−1}: the ES_q surface (λ = A/P) has Brauer classes of order q − 1 defined over the base
itself.** No corestriction is needed, so LDP A.1 does not apply. This is the most direct candidate for a
"degree-k Diff-parity" on ES_q.

**Lemma 2.1 (Steinberg decomposition; PROVED, valid over any field with μ_m ⊂ k).** For every point u of U_λ with
u₁u₂u₃(u₂ + u₃) ≠ 0, put x := λu₁ − 1, y := −u₂/u₃. Then in Br k,
`α_ζ(u) = (y, −1)_ζ + (x, y)_ζ.`
*Proof.* With s = −u₁/u₃ = y·(u₁/u₂): (s, y) = (y, y) + (u₁/u₂, y) and (y, y) = (y, −1). Next
u₁/u₂ = [u₃/(u₂ + u₃)]·[u₁(u₂ + u₃)/(u₂u₃)]. Since 1 − y = (u₂ + u₃)/u₃, the first factor is (1 − y)^{−1}, and
((1 − y)^{−1}, y) = −(1 − y, y) = 0 (Steinberg). The second factor is u₁(1/u₂ + 1/u₃) = u₁(λ − 1/u₁) = x. ∎
(Over ℚ, λ = 4/n: α(u) = (−u₂/u₃, −1) + (4u₁/n − 1, −u₂/u₃).)

**Theorem 2.2 (integral vanishing of the odd part; PROVED).** Let q be odd, A monic, P = Q^e a power of a monic
irreducible Q (e ≥ 1, Q ∤ A), and let u = (X, Y, Z) be a monic NC solution of A/P = 1/X + 1/Y + 1/Z. Then for every
ζ ∈ μ_{q−1} and every place v of F, inv_v α_ζ(u) ∈ ½ℤ/ℤ. In particular, **for every odd m | q − 1 the class
α_ζ(u) (ζ of order m) is zero in Br F**: the odd-order part of the Brauer group of the ES_q surface carries no
information at all on monic integral points.
*Proof.* Relabelling changes α_ζ(u) at most by a sign: the identity (a, b)_ζ = (−b/a, 1/a)_ζ (BL §2; it follows
from (a, a) = (a, −1) and bilinearity) gives invariance under cyclic shifts, and (b, a) = −(a, b). Since only
2-torsion is claimed, we may relabel at each place. The term (y, −1)_ζ is killed by 2. For β = (x, y)_ζ use the tame symbol
{x, y}_v = (−1)^{v(x)v(y)} x^{v(y)} y^{−v(x)} mod 𝔪_v (inv_v is its image in k(v)^*/k(v)^{*m}).
(i) Finite v = ℓ ≠ Q. Choose u₁ with v_ℓ(u₁) maximal. If v_ℓ(λu₁) ≥ 1 (true if v_ℓ(u₁) ≥ 1 or ℓ | A), then
x ≡ −1 (mod ℓ) is a unit and {x, y} = (−1)^{v(y)}·(−1)^{0} = ±1. Otherwise all u_i are ℓ-units and ℓ ∤ A; y is a
unit; if v(x) = 0 the symbol is 1, and if v(x) > 0 then λu₁ ≡ 1, so 1/u₂ + 1/u₃ = x/u₁ ≡ 0, u₂ ≡ −u₃ and y ≡ 1,
symbol 1.
(ii) v = ∞. By NC exactly one denominator has degree n − deg A (FUNCTIONFIELD_ES Lemma 1.2); take u₁ of larger
degree. Then deg(λu₁) > 0, so x has sign 1 (λu₁ is monic) and y = −u₂/u₃ has sign −1; {x, y}_∞ = ±1.
(iii) v = Q: Σ_v inv_v β = 0 and (i), (ii) give 2·inv_Q β = 0. ∎
*Remarks.* (1) The places ℓ | A are not special: the ES "2-adic" place of ℚ has no odd-order analogue. (2) The
two places where the proof uses ES specifically are exactly the target −1 (x ≡ −1 at (i)) and the sign
normalisation (ii). With target λ' ∈ F_q^* of order m, (i) gives λ'^{v(y)}, a genuinely order-m local invariant —
see §4. (3) P with several prime factors: (i), (ii) still hold; only the sum over v | P is forced to be 2-torsion.

**Corollary 2.3 (Type II: the P-invariant is the Kudla symbol; PROVED).** For a Type II datum (X, Y, Z) =
(abd, acdP, bcdP) of prime P, inv_P α_ζ(u) = (−f/P)_m (ζ of order m, value in μ_m), f = Aacd − 1.
*Proof.* Lemma 2.1 in the labelling (u₁, u₂, u₃) = (X, Y, Z): x = λX − 1 = (AX − P)/P = E/P (AX − P = Aabd − P =
E), y = −Y/Z = −a/b. At P: v_P(E) = 0 (deg E < n, E ≠ 0),
v_P(x) = −1, y a P-unit, so {x, y}_P = y = −a/b. From P | Aabd − E and E·f = P + Aa²d: b ≡ E(Aad)^{−1} and
Aa²d ≡ Ef (mod P), so −a/b ≡ −Aa²d/E ≡ −f (mod P). ∎
So **Theorem 1.3 (odd m) is the BL reciprocity law of the order-m class**, and FUNCTIONFIELD_ES Prop 4.1 (m = 2) is
its quadratic part; over ℚ the same computation gives inv_p α = (−f/p) = −1, i.e. BL Thm 1.2 = KUDLA Diff = {p}.

**Numerics (EVIDENCE; `scripts/bsH_bl_classes.py`: all solutions via the Lemma 1.3 divisor criterion, tame symbols at
every place incl. ∞, normalised by norms to F_q; Weil reciprocity checked on every point).**
| q, m, A, n, P | #P | #solutions | reciprocity failures | local invariants observed |
|---|---|---|---|---|
| 7, 3, T, 3, irreducible | 112 | 801 | 0 | all 0 at every place |
| 7, 3, T², 4 / T²+1, 4 / T(T+1), 4 | 588 each | 672 / 883 / 899 | 0 | all 0 |
| 13, 3, T, 3 | 728 | 2829 | 0 | all 0 |
| 7, 3, T, 3, P = Q³ | 6 | 277 | 0 | all 0 |
| 7, 6, T, 3 | 112 | 801 | 0 | only 0 and 3 (= ½), at ∞ and P only |
| 13, 4, T, 3 | 728 | 2829 | 0 | only 0 and 2 (= ½), at ∞ and P only |

## 3. The engine is real: twisted targets give an order-m "T1 on degree classes" — and degree is why it never sterilises

Construction (iteration I2). Theorem 2.2's proof used the ES target only through x ≡ −1 at finite places and
through sign normalisation at ∞. To test whether the order-m reciprocity can act at all, twist the target:
**ES_q^c(A, P): A/P = c₁/X + c₂/Y + c₃/Z, X, Y, Z monic, all degrees ≥ n − deg A** (c ∈ (F_q^*)³; c = (1,1,1) is
ES_q). Writing u_i = X_i/c_i, it is the same surface λ = Σ 1/u_i, so α_ζ = (−u₁/u₃, −u₂/u₃)_ζ is defined, but the
integral points now have signs 1/c_i at ∞. By leading terms the minimal degree is exactly n − deg A, and the c_i of
the minimal-degree terms sum to 1.

**Lemma 3.1 (finite places still trivial; PROVED).** For ES_q^c with P = Q^e and ℓ ≠ Q finite, inv_ℓ α_ζ(u) ∈ ½ℤ/ℤ.
*Proof.* Theorem 2.2 (i) verbatim: it used only λ = Σ 1/u_i and integrality of u_i at ℓ (u_i = X_i/c_i is
integral). ∎
**Lemma 3.2 (the ∞-invariant is a degree character; PROVED).** Assume some denominator has degree > n − deg A
(automatic unless c₁ + c₂ + c₃ = 1, which holds for no c in the table below) and label it u₁. Then x = λu₁ − 1
has sign 1/c₁ and v_∞(x) = n − deg A − deg X₁ < 0; y = −(c₃/c₂)X₂/X₃. The odd part of inv_∞ α_ζ(u) is the class
of `c₁^{deg X₂ − deg X₃}·(c₃/c₂)^{deg A + deg X₁ − n}` in F_q^*/F_q^{*m}.
*Proof.* Tame symbol {x, y}_∞ = (−1)^{v(x)v(y)} sgn(x)^{v(y)} sgn(y)^{−v(x)}; drop the signs ±1 (odd part). ∎
**Theorem 3.3 (order-m T1 on degree classes; PROVED).** Let m | q − 1 be odd, P = Q^m, and u a solution of ES_q^c whose
Q-shape is Type I (v_Q = (≥ m, 0, 0) up to order) or Type II ((0, ≥ m, ≥ m)). Then inv_Q α_ζ(u) = 0 for ζ of
order m. Hence (Lemma 3.1, reciprocity) the odd part of inv_∞ α_ζ(u) vanishes: **primitive solutions at m-th powers
lie in the degree classes where the character of Lemma 3.2 is trivial**. For prime P there is no such restriction.
*Proof.* Write v_i = v_Q(u_i). Type II, label u₁ = the Q-free one: v_Q(x) = −m. Since 1/u₂ + 1/u₃ = x/u₁ has
valuation −m, and v₂, v₃ ≥ m: if v₂ ≠ v₃ the sum would have valuation −max(v₂, v₃) < −m. So v₂ = v₃, y is a
Q-unit, and {x, y}_Q = ±y^m ∈ ±k(Q)^{*m}. Type I, label u₁ = the Q-divisible one (v₁ ≥ m, v₂ = v₃ = 0): y is a unit,
v(λu₁) = v₁ − m ≥ 0. If v(x) = 0 the symbol is 1. If v(x) > 0, then x/u₁ = (u₂ + u₃)/(u₂u₃) has valuation
v(x) − v₁ ≥ 0. If v(x) > v₁, u₂ ≡ −u₃ and y ≡ 1; if v(x) = v₁ then v(λu₁) = 0 forces v₁ = m and the symbol
±y^{−m} is an m-th power up to sign. Odd part: 0 in both cases. ∎
For c = (1,1,1) the character of Lemma 3.2 is trivial on the odd part, so Theorem 3.3 is empty — consistent with
Theorem 2.2.

**Numerics (EVIDENCE; `scripts/bsH_twisted.py`: complete solution sets, every solution verified, Weil reciprocity
and inv_ℓ = 0 for ℓ ≠ Q asserted on every point), q = 7, A = T, n = 3, m = 3 (ω = 2):**
| c | P | #P | #P unsolvable | (shape, inv_Q, inv_∞): counts |
|---|---|---|---|---|
| (1,1,1) | irreducible | 112 | 21 | I (0,0) 1680; II (0,0) 723 |
| (1,1,1) | Q³ | 6 | 0 | I (0,0) 354; II (0,0) 126; other (0,0) 351 |
| (1,1,2) | irreducible | 112 | 4 | I: (0,0) 402, (1,2) 431, (2,1) 431; II: (0,0) 212, (1,2) 137, (2,1) 137 |
| (1,1,2) | Q³ | 6 | 0 | I (0,0) 82; II (0,0) 30; other: (0,0) 96, (1,2) 54, (2,1) 54 |
| (1,2,4) | irreducible | 112 | 6 | I: 180, 230, 240; II: 70, 103, 75 (inv_Q = 0, 1, 2) |
| (1,2,4) | Q³ | 6 | 0 | I (0,0) 18; II (0,0) 17; other: 28, 25, 26 |
So the twisted problem carries a genuine order-3 reciprocity (inv_Q = −inv_∞ ∈ ℤ/3, non-constant at primes), and
at cubes it confines the Type I/II solutions to inv = 0, exactly as Theorem 3.3 says; non-primitive solutions
(inherited from Q) still carry all values.

**Why it never sterilises (Assessment, with the PROVED ingredient Lemma 3.2).** Over ℚ, T1 is total because
ℝ^*/ℝ_{>0} = ±1 and positivity pins the archimedean coordinate, so the forced invariant (p/f) = −1 is a constant.
Over F_q(T), F_∞^*/U₁ ≅ F_q^* × ℤ (sign × degree). Sign normalisation pins F_q^*, but the **degree coordinate
cannot be pinned** by any ES-type positivity — solutions need denominators of many degrees. Order-m invariants
at ∞ of sign-normalised data are therefore degree characters (Lemma 1.1, Lemma 3.2), and a k-th power obstruction
can only remove degree classes, never all solutions. ES_q itself has target −1, whose order-m image is trivial
for odd m (Thm 2.2), so for ES_q even the degree-class restriction is empty.

## 4. Number-field side: odd-degree descent (O177 sparks 1, 3) — closed

**Prop 4.1 (odd-degree subfields see only cosets; PROVED, elementary).** Let G = (ℤ/M)^* = Gal(ℚ(ζ_M)/ℚ),
F' ⊂ ℚ(ζ_M) with H = Gal(ℚ(ζ_M)/F'), K' ⊃ F' quadratic inside ℚ(ζ_M) with H' = Gal(ℚ(ζ_M)/K') (index 2 in H), and
η the character of K'/F'. If 𝔞 is an ideal of F' prime to M with N𝔞 = f, then f mod M ∈ H and η(𝔞) = −1 ⟺
f mod M ∈ H ∖ H'. Hence "η(𝔞) = −1 ⟺ f ≡ −1 (mod M)" holds for all such 𝔞 iff H ∖ H' = {−1}, i.e. H = {±1},
F' = ℚ(ζ_M)⁺, K' = ℚ(ζ_M), [F' : ℚ] = φ(M)/2 — even for every ES modulus M = 4cd > 4.
*Proof.* Art_{ℚ(ζ_M)/ℚ}(N𝔞) = Art_{ℚ(ζ_M)/F'}(𝔞)|… ∈ H (norm compatibility of Artin maps), and η(𝔞) is the image
of Art_{ℚ(ζ_M)/F'}(𝔞) in H/H'. ∎
So an odd-degree F' (spark 1) sees f only modulo H' with |H ∖ H'| = φ(M)/(2[F':ℚ]) ≥ 2: a coset condition plus the
splitting condition f ∈ H (which the certificate does not force). The full ray condition needs F' = ℚ(ζ_M)⁺.
**Prop 4.2 (norm descent goes the wrong way; PROVED).** Let F be any number field of odd degree r with
β, β' ∈ O_F, ββ' − 4c²dp = 1, β ≡ β' ≡ −1 (mod 4cd·O_F). Then N(β) ≡ N(β') ≡ −1 (mod 4cd) and
N(β)N(β') = (1 + 4c²dp)^r = 1 + 4c²d·(p·R_r), R_r := ((1 + 4c²dp)^r − 1)/(4c²dp): a rational Type II certificate for
n' = p·R_r, not for p. ES(n') follows from ES(p), not conversely. *Proof.* All conjugates of β are ≡ −1 mod 4cd.∎
Moreover O_F-certificates are cheap when O_F has units of norm −1 ((J)1, other_rings Prop 3.3), so they carry no
information about p. **Verdict: odd-degree descent is closed with proof** (Prop 4.1 for parity, Prop 4.2 for
certificates). Function-field remark: for the Carlitz cyclotomic field K_M of F_q(T), the inertia group at ∞ is
F_q^* ⊂ (R/M)^* (Hayes) and the real subfield K_M⁺ has degree Φ(M)/(q − 1), which is **odd** e.g. for M
irreducible of odd degree d ((q^d − 1)/(q − 1) ≡ d mod 2). So the A.4.2 parity obstruction disappears over
F_q(T), but Prop 4.2 applies verbatim (norms give certificates for P·R_r); and Gal(K_M/K_M⁺) ≅ F_q^* is cyclic of
order q − 1 with −1 its element of order 2 — the target −1 again only touches the 2-part (§2).

## 5. Forcing via rank-k supersingular class sets — genus-vacuous (Assessment with PROVED ingredients)

Candidate mechanism: D = D_{P,∞}^{(k)} (inv_P = 1/k, inv_∞ = −1/k; End⁰ of supersingular rank-k Drinfeld modules
over F̄_P, Gekeler 1991), non-trivial class set (mass ≈ ∏_{i<k}(|P|^i − 1)/…). A "forcing" statement would read:
some maximal order of D contains an element with prescribed characteristic polynomial (encoding a certificate).
(a) For degree-k CM data attached to ES_q certificates, Thm 1.3 shows the natural Kummer datum f^{1/k} is split at
P, so it does not embed in D at all; the Type II quadratic datum embeds into the quaternion D^{(2)} only on the
q ≡ 3 (4) degree-parity sub-families (FF Prop 4.1).
(b) For data that do embed, the total number of optimal embeddings over the genus is (class number of the order)
× (product of local embedding numbers) — Eichler's trace/mass formula, valid for definite orders over global
function fields (Gekeler; Wei–Yu, "Mass formula of division algebras over global function fields", from memory,
not checked). Its positivity is local. So "∃ maximal order containing the datum" is equivalent to the existence
of the polynomial datum plus congruences: the genus vacuity of LDP_DEEP B.1 in rank k. The class layer (B2)
is untouched.
(c) Ramanujan complexes (Lubotzky–Samuels–Vishne 2005, built from exactly these D) give expansion on the
supersingular rank-k isogeny complex: path-existence at length ≍ log of the number of vertices, i.e. data of
size |P|^{O(1)} — barrier B3, as for Pizer graphs (bsC_isogeny_ramanujan).
