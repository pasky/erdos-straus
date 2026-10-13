# bsB_root_number_parity — "a sign forces a point": the BSD-parity template vs the ES sign (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
The one famous mechanism where a **sign** deterministically forces **existence** is parity: a root number −1
(a product of local signs) forces odd p^∞-Selmer corank (Dokchitser–Dokchitser, Nekovář — unconditional), hence a
Selmer element; with finite Ш, a rational point of infinite order. The engine is an alternating (Cassels–Tate)
pairing making the "non-point part" have square order, so parity is local. ES has exactly a local sign (the genus
bit at n, = the orthant, `bsB_orthant_sign`). Is there a group 𝒮(n) with (i) certificates ↪ 𝒮(n), (ii) dim 𝒮(n)
mod 2 computable locally and odd at non-squares, (iii) an alternating pairing on the non-certificate part?

## Screen of the template, step by step
1. *Rational points are free.* The ES surface 4xyz = n(xy + yz + zx) is rational over ℚ with real points in the
   positive orthant; its rational points are dense there. So any parity/Selmer mechanism (which produces
   **rational** points) yields nothing: the ES content is integrality (class layer) + orthant (sign).
   (`elliptic_fibration_es.md` reached the same "integrality vs rationality" wall on the elliptic pencils.)
2. *Integral analogue of Selmer parity.* The natural F₂-object is the sign-blind set D*(n) with the genus bit.
   A Cassels–Tate-type statement would be "#(class −1) ≡ (local formula) (mod 2)". **Test** (`scripts/bsB_parity.py`,
   primes p ≡ 1 (4) in [10⁵, 2·10⁶], W(p) from `scripts/bsB_wcount.c`): P(W(p) odd) lies in [0.473, 0.520] across
   all 32 local classes (p mod 8 and Legendre symbols at 3, 5, 7, 11); overall 0.499. **The parity of the
   certificate count is not locally determined** (R175 repair, D18: precisely, not determined by p mod 8 and the
   Legendre symbols at 3, 5, 7, 11; EVIDENCE; same verdict as WR §6, DK C5 on 1100 sub-counts).
   (Assessment:) There is no involution with locally-counted fixed points on the certificate set — consistent with INVOLUTION_ES
   (finite-menu involutions barred) and DK C3 (reversal is fixed-point-free on L₃(p)).
3. *Where the alternating pairing would have to live.* In parity theorems the square-order part (Ш) is a
   cohomology group of a *fixed* Galois module; here the would-be module changes with n (moving modulus t, the
   factorisation of tn + 1). No fixed Galois module carries the divisor data (B2/WR Prop 10.3): the only fixed-
   module part is genus theory, i.e. the one sign bit, which is (i) for free and gives no point.
4. *Modification (violate "fixed module")*: take the module E[2] of a family of elliptic curves E_t with
   2-Selmer controlled by the factorisation of tn + 1 (e.g. congruent-number-type curves y² = x(x − 1)(x + tn),
   whose 2-descent reads off divisors of tn + 1 and tn). 2-Selmer elements = divisors d with local
   solvability (Legendre/Hilbert-symbol conditions on d and its cofactor) — that is the **sign layer of all
   divisors**, never "d ≡ −1 (mod t)" (an odd-order condition for prime t, `bsB_redei_oddpart` item 1; R175: for composite t the A₂-part can be finer). So even
   with growing families the parity engine sees exactly the genus shadow.

## Literature
T. & V. Dokchitser, "On the Birch–Swinnerton-Dyer quotients modulo squares", Ann. Math. 172 (2010); Nekovář,
"Selmer complexes", Astérisque 310 (2006); Cassels, "Arithmetic on curves of genus 1, IV", Crelle 211 (1962);
Bright–Loughran (2020); Heath-Brown, Invent. Math. 111 (1993) (2-Selmer of congruent-number curves via divisors).

## Assessment
Template screened: a parity engine needs (a) points that are rational, not integral-in-a-cone, and (b) a fixed
module; ES offers neither, and 2-descent on growing families reproduces only the genus shadow (item 4,
Assessment; the general statement "2-Selmer conditions are Hilbert-symbol conditions" is standard). Parity of
W(p) is locally unpredictable (EVIDENCE). Promise 0/5. The template is the right *shape* for H-B (sign ⇒
existence) and recording why it fails here is the value.
