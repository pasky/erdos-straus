# R286 — hostile review of LOWER_TAIL_FABLE.md (O274, model FABLE)

Reviewer: R286 (side agent, branch side-agent/review-tail-fable). Author files merged from side-agent/lower-tail-fable.
From-scratch scripts: `scripts/review_r286_*.py` (no reuse of `z43_fable_*`).

(in progress — verdicts filled in claim by claim)

## Claim A — SHARP 2: Thm 1.1 (canonical two-target form) and Lemma 2.7

**Verdict: Thm 1.1 SOUND. Lemma 2.7 SOUND (re-proved; a sharper Type I form noted). Companion forms (1.3), (1.4),
(2.1)–(2.3), (2.6) SOUND; (2.5) FALSE as stated (D1); §1 last remark contradicts Lemma 2.7 (D4).**

*Re-derivation.* Type II: if d = 4muw − 1 divides N = mp + u, put v = N/d; then mp = 4muvw − u − v, so
u + v = m(4uvw − p), i.e. e := 4uvw − p = (u+v)/m ∈ ℤ_{>0}, and 1/(uvw) + (u+v)/(mpuvw) = (p+e)/(puvw) = 4/p.
Type I: if d = 4muw − p > 0 divides N, h = N/d gives hp + mp + u = 4hmuw, so 1/(muw) + 1/(hpmw) + 1/(huw) = 4/p.
Converse: for p ∤ x the fraction (4x − p)/(px) is reduced; the classical two-unit-fraction criterion (coprime
U, V | px with (4x − p) | U + V) splits by whether p | U (Type I: U = pm, V = u, x = muw) or not (Type II), and
re-indexing gives the certificate. Every step checks.

*From-scratch test* (`scripts/review_r286_canon.py 3000 25`, own divisor/Jacobi/Kronecker code, exact Fractions):
all 8 334 unordered solutions of 4/p = 1/x + 1/y + 1/z for the 211 primes p ≡ 1 (4), p < 3000, enumerated
completely via (ay − b)(az − b) = b²; every one has exactly 1 or 2 p-divisible denominators; **every solution maps to
a certificate of its own type** (21 088 certificates; the stated reconstruction returns exactly that solution) and
**every certificate in the window m, u < 25 (6 105 Type I + 3 854 Type II = 9 959, matching the author's count)
reconstructs to one of the enumerated solutions, of the claimed type**. 0 failures. (Caveat on test power: every
p < 3000 has both a Type I and a Type II solution, so a per-prime *existence* comparison would be vacuous; the
solution↔certificate maps above are the non-vacuous test.)

*Lemma 2.7 re-proof.* (II) d ≡ −1 (mod 4mu) gives gcd(d, mu) = 1 and m⁻¹ ≡ 4uw (mod d), so p ≡ −4u²w and
(p/d) = (−1/d)(w/d) = −(w/d); d ≡ −1 (mod 4w) gives (w/d) = +1 (odd part by reciprocity, 2-part via d ≡ 7 (8) when
w is even). (I) From mp ≡ −u and p ≡ 4muw (mod d): m(p² + 4u²w) ≡ 0 and 4m²w ≡ −1 (mod d); gcd(m, d) | p, so for
p ∤ mu we get (−w/d) = 1, (w/d) = −1, and (w/d) = (p/w) (Kronecker; reciprocity with d ≡ −p (mod 4w), 2-part via
(2/·) being even under n ↦ −n mod 8). In particular **the Type I level is never w = 1**. Additionally (reviewer,
PROVED by the same computation, verified on all 14 712 Type I certificates from solutions, p < 3000):
**(p/d) = −(p/mu)** for Type I, so the non-residue of a Type I certificate is carried by d·m·u jointly as well as by w;
(p/d) = +1 in exactly half (7 356) of the cases. p = 13, (m, u, d) = (2, 1, 3), w = 2 confirmed.
Numerically 0 violations of either half of Lemma 2.7 on all certificates (from solutions and window).

*Companion forms.* (1.4) is a literal re-indexing (δ = u, (d+1)/4 = muw). (1.3) holds with the relabelling
(u, w) ↦ (m, w): d | 4m²w + 1 and d ≡ −p (mod 4mw); converse d = 4uwk − p gives the Type I certificate (u, k, w).
(2.2) II and (2.3) II: count-level bijection with Type II certificates verified for every p < 400
(`scripts/review_r286_forms.py`): #witnesses = #certificates at all 37 primes. (2.3) I follows from (1.3) by passing
to the complementary divisor (ff′ = 4u²w + 1 ≡ 1 mod 4uw turns −p into −p⁻¹). (2.6) correct for prime e ≠ p.
