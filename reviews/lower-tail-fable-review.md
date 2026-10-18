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

## Claim B — SHARP 3: Legendre form (§2.8) and mutual-shift graph (§2.9)

**Verdict: GAP (MAJOR D2). The direction "(r, A) ⟹ ES(p)" is SOUND (re-proved with five explicit constructions,
including all degenerate cases). The direction "ES(p) ⟹ ∃ (r, A)" is NOT proved — it is exactly the campaign's open
five-slice statement ES₅ / λ(p) ≤ 3. The §2.8 table is incomplete and one row is wrong for even A (D3). §2.9: dictionary
SOUND for ES₅ (not ES); census numbers reproduced; two descriptive errors (D5) and the graph is Astra's forest (D6).**

*Dictionary.* For a pair (r, A) put a = (p+r)/A, b = (A+1)/r, c = r. Then p = abc − a − c, A = bc − 1, A* := ab − 1, and
p/A = [[a, b, c]]; this is DEDEKIND_ES Lemma 1.1 with [[v, t, u]] = [[a, b, c]] (a, b, c ≥ 1 allowed). The five
conditions of DEDEKIND_ES Thm 4.5 are 4 | A, 4 | A*, 4 | b, 4 | c, 4 | a. Reviewer's explicit solutions (derived
independently, each an algebraic identity given p = abc − a − c):
S1 (4 | A, D = A/4) 4/p = 1/(A*Dp) + 1/(aD) + 1/(A*aD); S2 (4 | A*, D = A*/4) 4/p = 1/(ADp) + 1/(cD) + 1/(AcD);
S3 (b = 4w) 4/p = 1/(acw) + 1/(apw) + 1/(cpw); S4 (c = 4w) 4/p = 1/(wA*) + 1/(bpw) + 1/(bpwA*);
S5 (a = 4w) 4/p = 1/(wA) + 1/(bpw) + 1/(bpwA).

*From-scratch test* (`scripts/review_r286_legendre.py 3000 1200`). The set of pairs is finite and enumerated
completely (A ≥ r − 1, and A = p + r forces r | p + 1, otherwise r ≤ p + 2): 11 655 pairs at the 211 primes
p ≡ 1 (4) < 3000, 6 557 at the 188 non-square composites n ≡ 1 (4) < 1200, 369 at odd squares. On **every** pair,
(A/n) = −1 (Jacobi) ⟺ some S_i applies, and every applicable S_i is an exact ES identity (0 failures; this
re-verifies DK Thm 4.5 *including* the degenerate words a, b or c = 1, which Thm 4.5 itself does not cover — they are
covered by DK Cor 4.6's R169 remark only for p ≡ 1 (8); for p ≡ 5 (8) the pair (r, A) = (1, 2) always exists and S2
applies since a = (p+1)/2 ≡ 3 (4)). Every prime has a pair; no odd square does (T1 control). The 2-adic reading
"(A/p) = −1 ⟺ A ≡ 3 (4) or r ≡ 3 (4)" for odd A, r: re-proved by reciprocity ((A/p) = (−r/A) and
(r/A) = (−1/r)(−1)^{(r−1)(A−1)/4}) and 1 346/1 346 QNR odd pairs consistent. "r ≡ 0 (4): sign automatic" re-proved
((r/A) = 1 because A ≡ −1 (mod r), A ≡ 3 (4)); 0 counterexamples.

So "⇐" (each pair gives ES(p)) is SOUND, relative to nothing beyond the reviewer's identities S1–S5 plus Thm 4.5's
mod-8 cell check (re-verified here on all pairs).

*The "⟹" direction is open.* The images of S1–S5 are the five DK slices: proper sub-families of Thm 1.1's
certificates (S3 is Type II with m = 1, i.e. (u+v)/e = 1; S4/S5 are Type II with one of the two coprime divisors
equal to 1; S1/S2 are Type I with a = 1). Nothing in §2.8 maps an arbitrary ES solution into one of them, and
DEDEKIND_ES Cor 4.6 states only "the five X/e-slices of ES(p) together hold ⟺ λ(p) ≤ 3" — the ledger calls this
**ES-five / ES₅** ((J)-items at DISCOVERIES l. 596–598, 1630) and lists λ(p) ≤ 3 as EVIDENCE/CONJECTURE, not as a
consequence of ES. Measured from scratch: of the 8 334 solutions at the 211 primes < 3000, **4 671 (56 %) are not
produced by any (r, A)**; at p = 2521 only 2 of 9 solutions are five-slice. So "ES(p) ⟹ Legendre form" would be a new
theorem (ES ⟹ ES₅), not a re-indexing. Since ES(p) is known for all p in range, the brute-force "0 mismatches"
of `z43_fable_hj.py` cannot test this direction (the author's own report says so for the even branches; the issue is
the whole ⟹ direction, not the even branches).
