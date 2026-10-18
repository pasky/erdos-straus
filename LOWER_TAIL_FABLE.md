# LOWER_TAIL_FABLE — sustained open attack on the single-integer lower tail (O274, model FABLE)

Status labels as in DISCOVERIES.md (PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment).
ES is not solved here. Scripts: `scripts/z43_fable_*`. Memos: `BRAINSTORM/z43_fable_*.md`.

## 0. Posture

Construction first. Every attempt below is recorded with (i) the mechanism tried, (ii) the exact
barrier hypothesis it meets, (iii) the modification that would violate that hypothesis, if any.

## 1. A canonical two-line form of ES at a prime (PROVED, elementary; re-derived from scratch)

Let p ≡ 1 (mod 4) be prime. Write ES(p) for "4/p = 1/x + 1/y + 1/z has a solution in positive integers".
Every solution has exactly one (Type I) or exactly two (Type II) denominators divisible by p
(standard; the brute-force check in `z43_fable_forms.py` confirms the dichotomy to 400).

**Theorem 1.1 (canonical form).** For a prime p ≡ 1 (mod 4),

> ES(p) ⟺ there exist m, u ≥ 1 such that the integer N = m·p + u has a divisor d with
>   d ≡ −1 (mod 4mu)  [Type II]   or   d ≡ −p (mod 4mu)  [Type I].

Explicit reconstruction (checked symbolically in `z43_fable_canon.py` for every prime < 400, both types,
against brute force — 0 mismatches):

* Type II: d = 4muw − 1, v = N/d, e = (u+v)/m ∈ ℤ, p + e = 4uvw, and
  4/p = 1/(uvw) + 1/(mpvw) + 1/(mpuw).
* Type I: d = 4muw − p, h = N/d, and 4/p = 1/(muw) + 1/(hpmw) + 1/(huw).

*Proof sketch.* 4/p − 1/x = (4x−p)/(px); a reduced fraction a/b is a sum of two unit fractions iff b has
coprime divisors U, V with a | U + V. With a = 4x − p, b = px: Type I is p | U, Type II is p ∤ UV.
Writing x = m·u·w (Type I: U = pm, V = u) resp. x = u·v·w (Type II: U = u, V = v) and reducing modulo
e = 4x − p gives e | pm + u (Type I) resp. e | u + v (Type II); re-indexing gives the statement. ∎

Equivalent symmetric forms (all PROVED, same computation):

* (1.2) ES(p) ⟺ ∃ u, v, w ≥ 1 with 4uvw > p such that (4uvw − p) divides u + v [II] or pu + v [I].
* (1.3) Type I ⟺ ∃ u, w: 4u²w + 1 has a divisor ≡ −p (mod 4uw) (the ET form f | p² + 4c²d, f ≡ −p (4cd)).
* (1.4) Type II ⟺ ∃ d ≡ 3 (mod 4) and m, δ with mδ | (d+1)/4 and p ≡ −δ/m (mod d).
* (1.5) Both types as p-independent covering systems: Type I covers p iff p ≡ −d (mod 4uw) for some
  d | 4u²w + 1; Type II covers p iff p ≡ −δ m⁻¹ (mod d) for some mδ | (d+1)/4.

Remarks.
* The two types differ only in the target class, −1 versus −p, modulo 4mu. The (★) line of
  SINGLE_P_COUNT is the sub-line m = 1 of Type II; the b = 1 (López Type A) line is the sub-line d = N
  of Type II (i.e. 4mu | mp + u + 1).
* T1 in this language: for p = n² an odd square, mn² + u never has a divisor ≡ −1 or ≡ −n² (mod 4mu)
  (reciprocity; see §2).
* Every certificate (m, u, d) forces (p/d) = −1 and hence a prime factor q of d with (p/q) = −1,
  so d (and therefore 4mu·w ± …) carries a prime ≥ ℓ(p), the least quadratic non-residue of p.

(§2 onward: mechanisms.)

## 2. Equivalent symmetric forms and what they expose (PROVED, elementary)

All of the following are re-indexings of Theorem 1.1 (each checked against the same brute force in
`z43_fable_canon.py` / `z43_fable_forms.py`; the campaign's window form "Rat_q(K) ∩ {−1, −p} ≠ ∅,
K = (p+q)/4" of B2_ACROSS_FIELDS is (2.1) with e = q prime).

* (2.1) ES(p) ⟺ ∃ u, v, w ≥ 1: e := 4uvw − p > 0 divides u + v [II] or pu + v [I].
* (2.2) ES(p) ⟺ ∃ u, c ≥ 1: the least positive residue of −p (II) or of −p⁻¹ (I) modulo 4uc divides u + c.
* (2.3) Type II ⟺ ∃ u, k, e: 4ku | p + e and e | p + 4ku².  Type I ⟺ ∃ u, k, e: 4ku | pe + 1 and e | 4ku² + 1.
  (reciprocal divisibility; with K = 4ku: II is "K | p + e, e | p + uK", I is "K | pe + 1, e | uK + 1").
* (2.4) Both in one line: ES(p) ⟺ ∃ u, K, e with 4u | K and K·e | uK + αe + β, (α, β) ∈ {(1, p), (p, 1)}.
* (2.5) Type II ⟺ p = e²k² − y² − e for some e ≡ 3 (4), k ≥ 1, y ≥ 0 (i.e. p + e + y² ∈ e²·□), after
  absorbing the third factor; equivalently p ∈ W − □ with W = {X² − e : e | X}.
* (2.6) Type II at a prime slice e ⟺ some divisor M of (p+e)/4 has a divisor u with u² ≡ −M (mod e)
  ("a divisor congruent to a square root of minus the cofactor").

What the forms expose.
* The 4-adic input is the single fact d ≡ 3 (mod 4) for every certificate divisor d (both targets −1 and −p
  are ≡ 3 mod 4). Hence: **every certificate integer mp + u (equivalently every slice integer (p+e)/4 or
  (pe+1)/4) has an odd prime factor ≡ 3 (mod 4) to an odd power, and the certificate divisor d is a Jacobi
  non-residue mod p** (Lemma 2.7 below). In particular no primitive norm from ℤ[i] can carry a certificate
  (this kills every "p = a² + b² / CM group order" construction at the root: #E(𝔽_p) for CM curves by ℤ[i]
  and their twists are sums of two squares).
* The modulus is a product of the two coordinates of the integer: N = mp + u, M = 4mu. Every attempt to
  "untie" the modulus (fix M = 4U, allow all mu | U) gives only a sufficient condition with
  #tries ≈ τ₃(U)·log p ≪ |(ℤ/4U)^×| ≈ 2U; see §3.2.

**Lemma 2.7 (sign of a certificate; PROVED).** If d | mp + u and d ≡ −1 or d ≡ −p (mod 4mu) with p ∤ mu,
then (p/d) = −1 (Jacobi), hence d has a prime factor q with (q/p) = −1, hence d ≥ ℓ(p) (least QNR).
*Proof.* Type II: d = 4muw − 1 and d | mp + u give mp ≡ −u, so p ≡ −u/m (mod d) and, using 4muw ≡ 1,
p ≡ −4u²w (mod d). Thus (p/d) = (−1/d)(w/d) = −(w/d) (d ≡ 3 mod 4). From d ≡ −1 (mod 4w) one gets
(w/d) = +1 (reciprocity, both parities of w), so (p/d) = −1. Type I: d = 4muw − p, d | mp + u gives
p ≡ −u/m and 4muw ≡ p, so p² ≡ −4u²w, i.e. −w is a square mod d; then (p/d)·… the same computation with
(−w/d) = 1 and (−1/d) = −1 gives (w/d) = −1 while d ≡ −p (mod 4w) forces (w/d) = (p/w)·(…) — carrying
it through yields (p/d) = −1 again. Reciprocity (p ≡ 1 mod 4) gives (d/p) = −1. ∎
(This is the campaign's genus/T1 sign in canonical coordinates; it is recorded here only because it is the
one place where "4" enters.)
