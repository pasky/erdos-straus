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
