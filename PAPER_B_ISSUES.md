# Issues found while transcribing the pointwise-obstruction paper (task b)

Each item says where it is, whether it affects a proof, and what the paper does.
None of them invalidates a stated theorem.

1. **EST page reference (citation only).** DEPTH3 §3, DISCOVERIES (G)7 and
   reviews/wave34-hostile-review.md cite the Elsholtz–Tao "odd-square" remark as
   "p. 5 of arXiv:1107.1010". In the archived v6 PDF
   (`sources/elsholtz-tao-1107.1010.pdf`) the remark is on page 6. It is the
   paragraph after Proposition 1.6 in §1. The paper cites "§1, remark after
   Proposition 1.6".

2. **FORMAL_CLOSURE (C1) wording (presentation; both engines are correct).**
   (C1) says "every candidate D≠−s satisfying (A) and (B) gives a triple (Z,y,w)∈𝒱".
   (A) and (B) only make y integral. w=(s²/D+s)/r needs the same test for the
   complementary divisor s²/D. At a real prime the two tests coincide when
   gcd(r(q),s(q))=1, but in the formal setting the values r(q), s(q) need not be
   coprime: an aux value can share a prime with s(q). The verifier
   (`formal2_verify.py`) and the hostile reviewer's engine both require D and s²/D
   to pass (review step 5). The paper states the condition for both D and s²/D.

3. **FORMAL_CLOSURE §1.1, small redundancy.** The step "(B) ⇔ c_r | K" quotes
   gcd(c_r,n_h)=1. That fact is not needed: y = (D+s)(q)/r(q) = K(q)/c_r exactly,
   because the factors n_h^{β_h} cancel as rational numbers. The paper uses the
   shorter argument. The conclusion is unchanged.

4. **Theorem F's base class q0 is not a square class (scope of an explanation, not
   a gap).** The FC "Remark (characters)" says square residues were chosen "wherever
   the residue was forced to be non-generic". In fact `24 q0 + 1` is a quadratic
   **non-residue** modulo 870 of the 2036 primes of Λ (checked directly from
   `certificate.json.gz`). So the "every prime met is a square mod p" explanation of
   (C4) does not literally apply to Theorem F. Nonpositivity (C4) is verified
   directly, as FC says, so the theorem is unaffected. The paper says this
   explicitly and does not present Theorem F as an instance of the square-class
   mechanism. DEPTH3 Theorem 2 *is* such an instance.

5. **DEPTH3 Theorem 3, sieve citation.** It quotes "Halberstam–Richert, Thm 5.1"
   for Selberg's upper-bound sieve. The book is not in `sources/`, so the theorem
   number could not be checked. The paper cites the book without a theorem number
   and calls the result "standard upper-bound sieve of dimension κ".

6. **DEPTH3 Theorem 3, attribution of the half-dimension lemma (credit precision).**
   Dahan's Lemma 4.2 (arXiv:2608.24035) concerns divisors of M congruent to −1
   modulo 4m. DEPTH3 applies the idea to divisors of N² in an arbitrary class c
   modulo an odd K. There the squares ℓ² make the fixed points of r ↦ c r^{-1}
   harmless. This is a correct adaptation. The paper states it as a lemma
   "adapted from Dahan, Lemma 4.2" with its own two-line proof.

7. **LITERATURE_2026 author name.** arXiv:2509.00128 is cited as
   "Mihnea–Bogdan". The authors are Spiridon Mihnea and Bogdan C. Dumitru, as in
   the archived PDF. The paper uses the correct names.

8. **SIGNED_REFACTOR §5, interval width for z<0.** The claim "width less than 1/3"
   is correct, but only through the bound R + 1/(pt) > 1/t, which the text does not
   state. With the cruder bound R > 4/p alone, the width is only below 5/12. Either
   way it is below 1, which is all that is used. The paper gives the 1/t step.

9. **DEPTH3 summary item 4 (an unverified per-family claim).** It says every one
   of the 1113907 survivors p=24q+1, q≤10^13, escapes "through family A". The
   committed text supports this only for the 10 distance-3 primes below 5·10^6
   and for the 5304 survivors with 10^8<q≤10^10, where all transfers were
   enumerated (DEPTH3 §2 tables). The batch logs for the other ranges are not in
   the repo, and `depth3.py` may stop at a first hit, so "through A" could not be
   checked for every prime. The paper claims distance 3 for all 1113907 and the
   (A)-escape only for those two sets.

10. **DEPTH3 Theorem 2, "explicit finite family" (wording).** The family S_k
    depends on the profinite base point q*. Lemma 1 chooses q* non-constructively
    (transcendental lifts), so the family is finite but not exhibited. The paper
    says "a finite set depending on k and on the base point". An effective version
    would need a fixed-point construction like the one FORMAL_CLOSURE uses for
    Theorem F.

11. **The positive witness of the astra result requires Dickson for the
    restricted tuple (precision; affects STATUS.md/DISCOVERIES wording).**
    Dickson for the 159 original forms gives infinitely many sterile seed
    components. It does not by itself put infinitely many of them in the
    subprogression n≡507 (mod 857) that carries the positive solution. Astra
    checks that the restricted tuple is admissible, so Dickson for the restricted
    159 forms gives the "positive solution outside the sterile component"
    conclusion. The paper states it this way. STATUS.md's one-line summary
    ("it exhibits a positive ES solution outside the sterile component") is fine
    as a description, but strictly that conclusion is conditional on the
    restricted tuple.

12. **Self-review findings fixed in the paper itself, not in the sources.** The
    paper's chart converse first omitted `t+a≠0`; SR (6) has it. Its first
    formal-frame lemma stated "distinct formal integers have distinct values"
    without fixing a finite set and threshold. The paper also first omitted
    C_P=1 in the formal-fibre lemma and the unit condition on the base point.
    FC/DEPTH3 have these, implicitly or explicitly. All four are corrected in the
    paper.

No mathematical gap was found in the proofs transcribed: SR §§1–5, DEPTH3
Theorems 1–3, Lemmas 4–5 and the Corollary, FC Propositions 1–2 and §2.3,
WINDMILL Lemmas 1, 3, 4, Proposition 5 and Theorem 7, and SIZE_CONJECTURE
Lemmas A, B and E. Every proof was re-derived line by line, and the algebraic
identities were checked symbolically (`/tmp/pb/sym.py`, reproduced in the
report).
