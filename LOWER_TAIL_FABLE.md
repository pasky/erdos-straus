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
