# s4_kudla_green_infinity — signed words are the archimedean (Green-function) Fourier coefficients; at odd squares every certificate-shaped T has Diff = {∞} (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Cross-combination (J)13 (Kudla Diff-parity) × (J)45 (Maslov /
c_∞) × s4_three_bits_meta (L1, three-bit law).

## Idea
In Kudla's incoherent setting ((J)13, KUDLA_ES) the binary index of a word is T_w = [[tv − 1, 1], [1, tu − 1]]
(det tn; TWO_FIBRES, (J)39 Prop 4.1 up to equivalence), and the coefficient of E′(τ, 0) at T is a sum over the
places of Diff(T) = {v : the local space C_v does not represent T}. The incoherent collection is positive definite at
∞. For positive definite T, Diff(T) is finite and the coefficient is a supersingular intersection number; for T not
positive definite, ∞ ∈ Diff(T) and the coefficient is the *archimedean* term (derivative of the archimedean Whittaker
function, i.e. the Green-function/height contribution; Kudla, Ann. of Math. 146 (1997), §§ 10–14; Kudla–Rapoport–Yang,
*Modular forms and special cycles on Shimura curves*, Ann. of Math. Studies 161 (2006), Ch. 2–3).

## Statements
**K1 (PROVED, from L1).** T_w is positive definite ⟺ w is positive. (tv − 1 > 0 and det tn > 0 force t > 0, tv > 1;
then u > 0 as in L1. For signed w: t < 0 gives det < 0 (indefinite); t > 0 with tv < 1 gives negative definite.)
So **∞ ∈ Diff(T_w) ⟺ w is signed.**

**K2 (PROVED relative to (J)13's finite Diff formula, *given* the three-bit law for signed words, which is CERTIFIED for all words of odd n ≤ 1001 and should follow from TRANSPORT Thm 3.1 plus a finite 2-adic cell check not redone here).** At an odd
square n = m², for every word w with gcd(A, n) = 1: no ℓ | n lies in Diff (all v_ℓ(n) even, (J)13), no ℓ ∤ 2n does,
and 2 ∉ Diff ⟺ w is a certificate (the 2-adic condition sees w only through its ℤ₂-class, and the cell law is a
statement about w mod 8). |Diff| is odd. Hence:
 * positive words at m²: Diff = {2} (never certificates — T1);
 * **certificate words at m²: Diff = {∞} — they exist (signed family, s4_three_bits_meta R₂) and are all signed.**
So at odd squares the ES-shaped (certificate) Fourier coefficients of E′(τ, 0) are *purely archimedean*; at a prime p
the certificate coefficients are Diff = {p} (supersingular, finite). T1 in Kudla's language: **the certificate
condition can be met at a square only by moving the defect to the real place.**

## Construction attempt
Archimedean coefficients are explicit (exponential-integral / incomplete-Gamma functions of the eigenvalues of T,
KRY Ch. 2). Could a positivity statement about the *archimedean* part of a generating function force a finite
(Diff = {p}) certificate at primes? E.g. "Σ_{certificate T} a(T) q^T has its archimedean part ≤ total, the total is
an Eisenstein coefficient > 0 at primes"? Screen: the Eisenstein total at T is a genus quantity (Siegel–Weil,
(J)13 Prop 2.4′), so it cannot see which words exist (B2), and the split finite/archimedean is the split
positive/signed — which by s4_three_bits_meta P3 is a split between two lotteries of the same kind. No forcing.

## Barrier screen
B2 (word existence is the divisor lottery), B6 (Eisenstein totals are genus averages), T1 (K2 is T1 itself).
Harness: K1–K2 are numerator-free (they concern X_n and the 2-adic certificate region of 4); for 8/n the eight-slice
region is not a level set of the 2-adic Hilbert invariant ((J)32), so the analogue of K2 is false-as-a-dictionary
for 8 — consistent with (J)41's requirement that a working input be 4-specific.

## Cheap numerics
No new script: K1 = L1 (checked in `scripts/s4_signed_nadic.py`, 0 violations); the certificate ⟺ (χ = −1 xor signed)
law for all words of odd n ≤ 1001 is the numerical input to K2's "2 ∉ Diff ⟺ certificate" (0 violations).

## Assessment
Exact dictionary (PROVED, modest novelty: a re-reading of (J)13 with L1): **signed certificates = Kudla's archimedean
coefficients; T1 = "at squares, certificates live only at ∞".** It explains why every geometric/automorphic object
"sees T1" (they include the ∞-term), but gives no forcing. Promise 1/5.
