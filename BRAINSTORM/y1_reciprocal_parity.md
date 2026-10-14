# y1_reciprocal_parity — reversal-fixed words and the parity of the two fibres (O209)

## Idea
In the hyperbolic dictionary (y1_gamma8_trace) a word is a marked three-letter Zagier cycle. The natural involutions of
hyperbolic classes are inversion γ ↦ γ⁻¹ (reversal of the cyclic word), transposition and conjugation by diag(1, −1).
Sarnak's *reciprocal geodesics* (classes conjugate to their inverse) are the fixed points. A deterministic parity
mechanism (H-B) would be: an involution on X_p preserving χ whose fixed points are counted, plus a second invariant
forcing N₋ odd.

**Fact R1 (PROVED, elementary).** On X_n the induced involution is (t, u, v) ↦ (t, v, u) (M_w^T is conjugate to
M_{(t,v,u)}; transposition and diag(1, −1)-conjugation give the same map on marked words), it preserves χ ((−A/n)(−A*/n)
= (AA*/n) = 1). Fixed points: u = v, tu² − 2u = n, so u | n. For n = p ≥ 5 prime the **only reversal-fixed word is (p + 2, 1, 1)**
(R209 repair: at p = 3 also (1, 3, 3), with χ = +1; |X₃| = 8), with A = p + 1 and χ = (−1/p). Hence |X_p| is odd (p ≥ 5)
and **N₋(p) ≡ [p ≡ 3 (mod 4)] (mod 2)** (also at p = 3). (R209 repair: (p + 2, 1, 1) has trace −2, so it is parabolic, not a
reciprocal closed geodesic; we only use the word reversal.) The fixed word is exactly the trivial certificate for p ≡ 3 (4) (SIGN_IDENTITY Lemma 1.2), and for p ≡ 1 (4) parity gives nothing.
**Fact R2 (EVIDENCE).** No finer congruence: for primes p ≡ 1 (4) below 10⁶, N₋(p) mod 8 is equidistributed over
{0, 2, 4, 6} (counts 4780/5021/4873/4949 for p ≡ 5 (8); 4896/4805/4835/5016 for p ≡ 1 (8); census `si_census.c`).
**Fact R3 (PROVED).** The other "Klein" symmetry of the cubic (rotation with u = t, bsA_fricke_vieta F2) changes n except
on a thin set, and rotation flips χ on whole cells (CHI_FLIP rotation law), so it does not act on X_p with a fixed sign.

## Literature
Sarnak, *Reciprocal geodesics*, Clay Math. Proc. 7 (2007); Zagier reduction; PARITY_FIXED_P.md (O165) for the general
H-B parity screen.

## Barrier screen
H-B (parity at fixed p) collapses for this involution (other involutions are not excluded here): it has one fixed point, already a Mordell certificate (B1 class
p ≡ 3 (4)); mod-4/8 information is equidistributed (R2). T1: at n = m², (m² + 2, 1, 1) has χ = +1, consistent.

## Cheap numerics
R2 from the 10⁶ census (one pass, tiny output).

## Assessment
Negative (PROVED R1/R3, EVIDENCE R2): the reversal involution of the hyperbolic dictionary reproduces only the p ≡ 3 (4) certificate.
Promise 0/5.
