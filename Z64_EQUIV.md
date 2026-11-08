# Z64_EQUIV — statements equivalent to ES-at-primes / (MS) / U₇ / (S) / CONV-II in other fields (wave z64, lane EQUIV)

**ES is OPEN.** Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Internal results, internally reviewed only. Brief: `z52bbriefs/z64_lanes.md` §EQUIV (+ z58 common
rules, z53 depth brief). Scripts `scripts/z64_equiv_*`, data `data/z64/equiv/`.

*Status: CHECKPOINT 1 (skeleton). Sections marked [TODO] are being filled.*

## 0. Mandatory falsifier table (framework level; per-row behaviour in §3)

An *equivalence* is the same statement in other coordinates, so it inherits F1–F4 verbatim: whatever ES/(★)/(S) does at
odd squares, on the C-even sub-line, at composites and at the known zeros, the transported statement does too. The
screens therefore bite on the **native tool** of the target field, not on the dictionary. For each row of §3 the
question is: *does the field's native existence tool, applied to the transported statement, distinguish p from*
* **F1** odd squares m² (R(m²) = 0, (S) and U₇ fail at m², T1);
* **F2** the C-even sub-line (R₈ zeros: 12 primes in [10¹⁰, 1.1·10¹⁰]); numerator 8 (8/131);
* **F3** the 285 non-square composite R-zeros ≤ 8·10⁶; Z₇ for U₇; 4545 for CONV-II; 105, 4545 for U_II;
* **F4** the 14 (★)-zero primes, the 38 𝔊*-zero primes?
A tool that cannot see these distinctions "proves" a false statement. (Data: `data/z58/screens/`.)

| row | F1 | F2 | F3 | F4 | verdict |
|---|---|---|---|---|---|
| [TODO: one row per equivalence of §3] | | | | | |

## 1. Precise statements attacked (all CONJECTURE unless stated)

For a prime p (or odd n):
* **ES(n):** ∃ x, y, z ∈ ℕ with 4/n = 1/x + 1/y + 1/z.
* **(★)/(MS):** R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} ≥ 1; (MS) is R(p) ≥ 1 for primes p > 10¹⁷ in 𝔐 (FRONTIER
  §2.4). Divisor form: ∃ C, ∃ d | 4Cn + 1 with d ≡ −1 (mod 4C). (MS) ⟹ ES (PROVED rel. Mordell + Salez).
* **U₇(n):** ∃ f ≡ 7 (mod 8) with (−n mod f) | f + 1 (`Z60_LOPEZ.md` Lemma 7; CONJECTURE U₇: true for every odd non-square
  n ∉ Z₇ = {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425}).
* **(S):** every non-square n ≡ 1 (4) with L₃(n) ≠ ∅ has a length-3 HJ word n/A = [[v, t, u]] (tuv − u − v = n,
  A = tu − 1, gcd(A, n) = 1) with Jacobi (A/n) = −1 (`HJ_DEEP.md` §3; (S)(p) ⟹ ES(p) via DEDEKIND_ES Thm 4.5).
* **CONV-II:** N_II(n) = #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} ≥ 1 for odd non-square n ≠ 4545 (`Z58_WILDCARD.md`).

What "equivalent in another field" means here: a statement Φ(p) about a mathematical object of field F such that
Φ(p) ⟺ (target)(p) is PROVED for every prime p in the stated class (or with an explicitly labelled finite/small loss).

## 2. Why this is not already closed

* The repo's connection catalogue (`ES_CONNECTIONS_TODO.md`, 3192 items, z52b) already lists one-line *forms* in most
  fields of the brief (Frobenius numbers Z0394, Brieskorn–Pham lct Z0155, Hurwitz existence Z0171, dessins Z0417,
  weighted projective lines Z0418, lens spaces/plumbings (DEDEKIND_ES, bsA_*), Lorenzini's critical polynomial (HJ_DEEP),
  Farey/SL₂ (Z63_EUCLID), TFNP (z31_complexity), Lorentzian polynomials Z2606, …). Most were never *proved* as
  equivalences with exact quantifiers, and the z52d avenue layer judged them "circular" without a stated reason.
* This lane (i) critically reviews `Z63_PRECEDENT.md` for missing precedent classes; (ii) proves the equivalences
  (exact ranges, exceptions); (iii) screens each field's **native existence tools** (not the dictionary) against
  F1–F4; (iv) isolates *why* formula-level dictionaries are circular and which kind of equivalence could escape;
  (v) pushes the best 1–2. Closed items (z53 brief list, FRONTIER §6) are not redone.

## 3. First lemma (PROVED + CERTIFIED finite check): ES ⟺ an orbifold-Euler-characteristic / Riemann-surface statement

**Lemma A.** For every odd n ≥ 5 the following are equivalent:
(a) ES(n);
(b) 4/n − 1 is the orbifold Euler characteristic of a closed orientable 2-orbifold;
(c) there is a compact Riemann surface X of genus g ≥ 2 and a finite group G ≤ Aut(X) with |G|·(n − 4) = n·(2g − 2).

*Proof.* (b) ⟺ (c): for G acting on X (g ≥ 2) the quotient orbifold O = X/G satisfies χ(X) = |G|·χ^orb(O)
(Riemann–Hurwitz), so (c) gives χ^orb(O) = (2 − 2g)/|G| = −(n − 4)/n. Conversely every closed orientable 2-orbifold
with χ^orb < 0 is a quotient ℍ/Γ for a cocompact Fuchsian group Γ, which has a torsion-free normal subgroup Γ′ of finite
index (Selberg's lemma, or Fox's theorem for triangle groups); X = ℍ/Γ′, G = Γ/Γ′ gives (c) since χ(X) = [Γ:Γ′]χ^orb.
(a) ⟹ (b): S²(x, y, z) has χ^orb = 1/x + 1/y + 1/z − 1 (cone orders 1 are allowed and simply omitted; for n ≥ 5 the
value is < 0). (b) ⟹ (a): an orbifold of genus h with cone orders m₁, …, m_r ≥ 2 has χ = 2 − 2h − Σ(1 − 1/m_i). Setting
χ = 4/n − 1: h ≥ 2 is impossible (χ ≤ −2); h = 1 needs Σ(1 − 1/m_i) = 1 − 4/n, impossible for r = 0 (n ≠ 4), r = 1
(m = n/4, n odd), r = 2 (1/m₁ + 1/m₂ = 1 + 4/n > 1) and r ≥ 3 (sum ≥ 3/2). For h = 0: Σ 1/m_i = r − 3 + 4/n, so
r ≤ 2 is impossible, r = 3 is ES, r ≥ 6 is impossible (Σ ≤ r/2 < r − 3 + 4/n for r ≥ 6), and:
* r = 5: Σ₅ 1/m_i = 2 + 4/n > 2 forces at least three m_i = 2, then 1/m₄ + 1/m₅ = 1/2 + 4/n, which gives only even
  n ∈ {4m₅ (m₄ = 2), 24, 48, 120}. No odd n.
* r = 4: Σ₄ 1/m_i = 1 + 4/n. If (m₁, m₂) = (2, 2) then 4/n = 1/m₃ + 1/m₄, and splitting 1/m₄ = 2·1/(2m₄) gives ES(n).
  Otherwise (sorted) m₁ ∈ {2, 3}, 1/m₁ + 3/m₂ > 1, and every remaining case has 1/m₁ + 1/m₂ + 1/m₃ > 1 with bounded m₃;
  the exact enumeration `scripts/z64_equiv_orbifold.py` (CERTIFIED, Fractions; output
  `data/z64/equiv/orbifold_sporadic.txt`) finds exactly the odd n ∈ {15, 21, 23, 39, 45, 47, 75, 95, 105, 111, 115,
  117, 119, 165, 273}, all < 10¹⁷ where ES holds (Salez; trivially also by hand). [TODO: write the bounding argument
  for the r = 4 enumeration explicitly in the final memo.]
∎ (relative to the finite enumeration and to ES at the 15 sporadic n.)

*Reading (Assessment).* (c) is "a single rational number 2n/(n − 4) is an automorphism-to-genus ratio |G|/(g − 1)".
The field's existence tools (Riemann existence theorem, Selberg's lemma, Kulkarni's genus spectrum) realise any
signature once the *signature* is given; the signature is exactly an Egyptian representation. This is the prototype of
the circularity analysed in §4 [TODO]. Catalogue neighbours: Z0171 (Hurwitz existence), Z0417 (dessins).

## 4. Plan [TODO]
1. Critical review of Z63_PRECEDENT: missed precedent classes (verified from sources; research subagents).
2. Ranked equivalence table: equivalence, field, proof, native tool, why it might/might not apply, F1–F4 row.
3. Dictionary-circularity principle and the shape an escaping equivalence must have.
4. Push the best 1–2; hostile review; verdict.
