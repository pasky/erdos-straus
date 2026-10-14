# y4_oneodd_slices — the one-odd half of the five slices (O212, goal (b))

## Idea
(J)32 Lemma 2.1: ES = [8/n] ⊔ [one-odd 4/n] (one-odd ⟺ d odd in ET coordinates). (J)32 Thm 3.1: the five slices
S₄ = {χ = −1}. Combine: which χ = −1 words give one-odd certificates, and is the one-odd slice set a cleaner
4-specific object (a "one-odd SQ₅")?

**Lemma 1 (PROVED, parity bookkeeping).** Let w = (t, u, v) be a word of odd n (tuv − u − v = n, A = tu − 1,
A* = tv − 1) and X ∈ {A, A*, t, u, v} a slot with 4 | X, giving the (J)32 Lemma 3.0 solution. That solution has
exactly one odd denominator iff v₂(X) = 2, and all denominators even iff v₂(X) ≥ 3.
*Proof.* (T) t = 4c: n + u + v = 4cuv forces u + v odd; denominators uvc, ucn, vcn: if c even all even; if c odd,
exactly one of ucn, vcn is odd (u, v of opposite parity) and uvc is even. (U) u = 4w: n + v = 4w(tv − 1) forces v odd;
f = tv − 1; denominators wf, tnw, tnwf: w even ⇒ all even; w odd ⇒ exactly one of f, t is odd (v odd), so exactly one
of wf, tnw is odd and tnwf is even. (I) A = 4d: t, u odd; A* = tv − 1 has parity opposite to v; denominators A*dn,
vd, A*vd: d even ⇒ all even; d odd ⇒ exactly one of A*, v odd, so one odd denominator. (I′), (V) symmetric. ∎
So S₄ = S₄^{odd} ∪ S₈ with S₄^{odd} := {some slot ≡ 4 (mod 8)}, S₈ = {some slot ≡ 0 (mod 8)} (the (J)32 S₈).
Both are unions of cells (t, u, v) mod 8.

**Cell split (CERTIFIED, `scripts/y4_oddslice_cells.py 801`, 16 242 words, every slice solution exactly verified and
its parity checked, 0 violations of Lemma 1).** The 240 χ = −1 cells mod 8 split as 100 one-odd-only, 100 S₈-only,
40 both. **S₄^{odd} and S₈ are both 140/240 of the χ-fibre: same cell size.** Neither class is a function of
n mod 16, (2/n), (t/n) or ((2A/n), n mod 8) (all mixed in the table).

**Not a lattice invariant (EVIDENCE + standard classification).** By (J)33, χ = −1 ⟺ Q_w is ℚ₂-isotropic. Q_w has odd
determinant n, so it is a unimodular ℤ₂-lattice, determined over ℤ₂ by (det class, oddity) [Conway–Sloane SPLAG
Ch. 15 §7]. Computed oddity on all χ = −1 words of n ≤ 401 (`scripts/y4_oddity.py`): the oddity is
determined by n mod 8 (7, 5, 3, 1 for n ≡ 1, 3, 5, 7). Hence at fixed n all χ = −1 words have ℤ₂-isometric Q_w, yet
all three classes occur: **one-odd vs all-even is not a ℤ₂-invariant of Q_w; it depends on the marking (the word/basis).**
So there is no "one-odd" analogue of (J)33's isotropy description: the 2-adic local data stop exactly at χ.

## Census (`scripts/y4_oddslice.c`, every hit verified in 128-bit with parity check)
* **S₄^{odd}(p) ≠ ∅ for every prime 3 ≤ p ≤ 10⁷ (664 578 primes)**, while S₈(p) = ∅ at 27 of them (3, 11, 17, 113, 131,
  241, 257, …, 259201 — reproducing (J)32). Odd squares k² ≤ 10⁶: S₄^{odd} = S₈ = ∅ (T1, as forced by S₄ = {χ = −1}).
* The full one-odd ES half (`ms_census 4 10⁶ p 1`): no failing prime ≤ 10⁶ (reproduces (J)32 to 10⁶); one-odd 8/p
  (`ms_census 8 10⁶ p 1`) fails at 3, 11, 17, 59, 131, 241, 449.
* **Composite exceptions:** odd non-squares n ≤ 2·10⁵ with S₄(n) ≠ ∅ but S₄^{odd}(n) = ∅: 321 = 3·107, 4545, 5481,
  8745, 9121 = 7·1303, 13041, 25305, 57481, 169425 (9 values; S₄(n) = ∅ only at 105). So "S₄^{odd} ≠ ∅ ⟺ S₄ ≠ ∅" is
  FALSE in general; at primes both hold to 10⁷.
* Why one-odd wins at small t (PROVED for the I-slices): for p ≡ 1 (mod 8) and t ≡ 3 (mod 8), tp + 1 ≡ 4 (mod 8), so v₂(tp + 1) = 2
  (R-O212: not v₂(t+1) for general odd t; p = 41, t = 7 gives 5 vs 3), so every I-slice at t ≡ 3 (8) (in particular t = 3) is one-odd; S₈ via I needs t ≡ 7 (8).
  Least t of a one-odd hit is ≤ 4 for 98% of the first 3000 primes ≡ 1 (mod 8), versus 86% for S₈ (tail to t ≥ 20:
  4 vs 43). The asymmetry between two equal-size cell sets is a small-t effect, not a congruence obstruction.

## Literature
Lemma 2.1 of MODEL_SPECIFIC (O197); DEDEKIND_ES Thm 4.5 / (J)32 Thm 3.1; (J)33 CHI_FLIP Thm 1.1; Conway–Sloane,
SPLAG, Ch. 15 (2-adic genus symbols, oddity).

## Barrier screen
B1: S₄^{odd} is a union of cells mod 8 — a congruence target on X_p's points; B5/T1: empty at squares (inherits from χ).
B2: per t it is "tp + 1 has a divisor A ≡ −1 (t) with v₂ = 2 and cofactor ≡ −1 (t)", a moving-class lottery.
Numerator-blindness: S₄^{odd} is 4-specific (no 8-analogue: the 8/n one-odd half already fails at 59, 449), but it is
a strict sub-lottery of the χ-fibre with no character description — it is LESS structured than SQ₅, not more.

## Assessment
PROVED: Lemma 1 (parity = v₂ of the slot). CERTIFIED: cell split 100/100/40. EVIDENCE: S₄^{odd}(p) ≠ ∅ for p ≤ 10⁷;
9 composite exceptions ≤ 2·10⁵. Verdict on goal (b): the one-odd half is **a description, not an input**. It is
4-specific, but it has no character/2-adic description (it is not a ℤ₂-invariant of Q_w), and its never-failing
behaviour at primes rests on the same small-t lottery as S₈, which fails. A "one-odd SQ₅" would be strictly harder than SQ₅
and false at composites like 321, so SQ₅ remains the cleaner target.
