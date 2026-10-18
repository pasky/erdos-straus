# z38_brauer_character — BL's quaternion class is the Kronecker character χ_{−4uB} in the pair expansion (O268)

**Idea.** Make O260 spark 4 / R277 D3 exact: evaluate Bright–Loughran's generator α = (−x/z, −y/z) of Br U_n/Br ℚ ≅ ℤ/2 on the
rational points P_{u,B} = (uBC, nBC, nuC), C = (n+u+B)/(4uB) ∈ ℚ, attached to every (★)-pair, and locate it in the
orthogonality expansion 1[n ≡ −(u+B) (mod 4uB)] = φ(q)^{−1}Σ_χ χ(n)χ̄(a).

**Result (PROVED, BM_CORRECTED_COUNT Thm 1.1).** α(P_{u,B}) = (−B/n, −B/u); inv_∞ = −1, inv_ℓ = 1 off 2nuB, inv₂ = 1 when C is
2-integral, inv_p = (−uB/p) = χ_{−4uB}(p) for n = p. The elementary identity χ_{−4uB}(−(u+B)) = −1 ((u+B) | (u−B)² + 4uB)
shows that the term of χ_{−4uB} in the expansion is −χ_{−4uB}(n)/φ(q) = (inv_∞·inv_p)/φ(q): principal + Brauer character
= φ(q)^{−1}(1 + inv_∞ inv_p), the Borovoi–Rudnick / Colliot-Thélène–Xu density factor with Br/Br₀ = ℤ/2. The strong form
"genus indicator = BM invariant" is refuted: the genus indicator uses all s(q) = 2^{ω_odd(uB)+2} real characters mod q (log₂ s(q) independent conditions), BL's
class is exactly one of them (answering R277's "is BL's symbol a product of the genus characters?": it is a single one).
The same holds on the full Type II family 4abcd − a − b = cn (character χ_{−4ab}, independent of c, d), and on BL Rem 1.10's
numerators m with 4 | m (e.g. 8/n; false for m = 3). Interpretation as a BR factor is valid at integral points only;
at non-hit rational points the invariants at ℓ | 2uB are dropped (heuristic density replacement).

**Literature.** Bright–Loughran, arXiv:1908.02526, Thms 1.2, 1.6, Lemmas 3.4, 3.5, 3.8, Cor 1.3, Rem 1.10; Borovoi–Rudnick,
Invent. Math. 119 (1995) (density with BM factor); Colliot-Thélène–Xu, Compositio 145 (2009). Campaign: PARITY_AUDIT Lemma 3.2
(χ-shadow), B1_LINE Lemma 1.2 (pair genus law) — now one statement.

**Barrier screen.** Not a mechanism: a dictionary. T1: vanishes at squares by construction (Thm 1.1(4)). B3/B6 untouched.
Thm 9.1/Prop 10.3: it is exactly the genus-vs-ray-class split, with BL's class the geometric part of the genus.

**Cheap numerics.** `scripts/z38_bm_dictionary.py 400`: Hilbert symbols at all places, exact rationals, 9 440 pairs, 372 hits,
odd squares: all identities pass.

**Assessment.** PROVED dictionary (new as an exact statement; ingredients are BL's lemmas and a two-line identity). Value:
it singles out M_BM as the canonical BM-corrected main term (memo z38_mbm_unconditional).
