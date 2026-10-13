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
