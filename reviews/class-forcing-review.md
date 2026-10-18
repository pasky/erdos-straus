# R272 — hostile review of O263 (CLASS_FORCING.md, branch side-agent/class-forcing @ ec15ff50)

Reviewer scripts: `scripts/review_r272_*.py` (from scratch; author's z33 scripts not reused). ES is not solved.

## Summary verdicts (filled in progressively)
| claim | verdict |
|---|---|
| Thm 2.1 (a)(b)(c)(i)–(iii), Table 2.2 | SOUND (D3 cosmetic) |
| Thm 2.1(c)(iv) + bold summary + slogan | GAP → SOUND-AFTER-REPAIRS (D2) |
| Lemma 3.1, Prop 3.2 | SOUND (D5, D6 minor) |
| Thm 3.4 | SOUND (D4 minor; re-checked from scratch, 0 firings) |
| Thm 6.1 + Hypothesis HC | **FATAL as stated** (HC is false; Thm 6.1's conclusion is false) — SOUND-AFTER-REPAIRS with the D1 repair |

## Defects

**D1 (FATAL) — §6, Hypothesis HC and Theorem 6.1: the compatibility condition only controls Ω ∩ ℚ(ζ_M); the abelian
part of Ω can force a congruence p ≡ a (mod q) at a prime q > B that kills admissibility / creates a certificate.**
Counterexample (checked in `scripts/review_r272_thm61_cex.py`): D = 1, B = 6 (≥ 4D + 2), q = 7 > B, Ω = ℚ(ζ₇),
C = Frob class of p ≡ −4 ≡ 3 (mod 7). Since 7 ∤ M, Ω ∩ ℚ(ζ_M) = ℚ, so C is "compatible with p ≡ 1 (mod M)" in the
sense of Thm 6.1 (and primes p ≡ 1 (M), p ∈ C exist: 15552001, 33696001, …). But for every p ∈ C, 7 | p + 4 and
7 ≡ −1 (mod 4): w = 7 is a certificate at d = 1 (exact ES solution (x,y,z) = (a, 2ap, 2p), a = (2p+1)/7, verified for
all 1497 such primes p < 2·10⁵). So (i) the conclusion "infinitely many p ∈ C with no certificate at levels ≤ D" is false,
and the "Consequently no theorem of the form 'every prime with Frob_p|Ω ∈ C has a certificate at level ≤ D' exists for
such C" is false (here it does exist, trivially). (ii) HC itself is false as stated: take f₀ = 1 + Mk, f₁ = (f₀ + 4)/s₁,
Ω = ℚ(ζ₇), C as above; the system is admissible and C is compatible with f₀ in HC's sense, yet 7 | f₁(k) whenever
Frob_{f₀(k)} ∈ C. The proof of Thm 6.1 hides this: "admissibility" is checked for the forms alone, never for the forms
restricted to the k-classes selected by C|_{Ω ∩ ℚ^{ab}} (conductor primes > B).
*Repair.* (a) Restate HC with the correct local condition: let Ω₀ = Ω ∩ ℚ^{ab}, of conductor m; C|_{Ω₀} selects a set
A ⊂ (ℤ/m)^×; require some k₀ with f₀(k₀) mod m ∈ A such that the system {f_i(k₀ + m j)}_j is admissible. (b) In Thm 6.1
require B ≥ every prime dividing the conductor m of Ω₀ and e_q ≥ v_q(m), and "C compatible with p ≡ 1 (M)" to mean
C|_{Ω₀} = {1} (Ω₀ ⊂ ℚ(ζ_M)). Then the proof goes through (k-classes selected by C are k ≡ anything mod primes > B), and
the honest reading is: *Frobenius data = its abelian (congruence) shadow + a non-abelian part; the congruence part is B1
and may well cover whole classes (as above); only the non-abelian part is (conditionally) useless.* §9's verdict bullet
and AGENT_REPORT ("for every finite Galois Ω and class C compatible with p ≡ 1 (M)") must be amended accordingly.

**D2 (MAJOR, label/overclaim) — Thm 2.1(c)(iv) and the bold summary after (c); AGENT_REPORT "multiquadratic (+ℚ(ζ_n)) for
all standard data"; slogan "reciprocity forces parity, never class".** (b) is correct and is the real content: Frob_p|Ω sees
[p] only through F = Ω ∩ ℚ(ζ_t), an abelian subfield of ℚ(ζ_t), i.e. a *quotient of p mod t* (congruence data). But the
claim that F (or Ω^{ab}) is multiquadratic for "Smith/Koymans–Pagano governing fields" is not a property of governing fields
at all: a governing field is not canonical — any finite Galois Ω′ ⊇ Ω (e.g. Ω′ = Ωℚ(ζ₁₆) or Ωℚ(ζ₅), still 2-extensions)
governs the same invariant, and then F ⊇ ℚ(ζ₁₆) ∩ ℚ(ζ_t) resp. ℚ(ζ₅) ∩ ℚ(ζ_t) sees [p] mod 16 resp. mod 5 in full (cyclic
quotients C₄ ⊄ G/G²). Even the minimal 2-power governing fields in the literature need not have multiquadratic Ω^{ab}
(an abelian 2-extension of ℚ can be cyclic quartic, e.g. ℚ(ζ₅), or contain ℚ(ζ₁₆)); I could not access Smith (2017) or
Koymans–Pagano to check their specific constructions (no PDFs in sources/; not needed for the defect). Also (i) itself gives
p mod ℓ — a cyclic, non-quadratic quotient — so "parity" is already inaccurate there (the author does write "and p mod n").
*Repair.* Delete the multiquadratic claim in (iv) (or label it CONJECTURE "for the specific fields of [ref], unchecked");
replace the bold summary by the true statement of (b): **"any Frobenius datum of p sees [N] ∈ G only through a quotient of
p mod t (congruence data), and is equidistributed independently of [p] beyond that quotient; for the data (i)–(iii) the
quotient is G/G² × (p mod gcd(n, t))-type."** The slogan should read "reciprocity data of p = congruence data of p plus an
independent non-abelian part", not "parity, never class". Since [N] is itself a function of p mod t (Thm 2.1(a)), nothing
downstream breaks.

**D3 (MINOR) — Thm 2.1, proof of (a).** "4N ≡ p, cp + 1, p, 1 (mod t)" is wrong for the first two lines (N ≡ p mod 4d and
N = cp + 1; 4N ≡ 4p, 4(cp+1)). Should read "N ≡ p (mod 4d), N = cp + 1, 4N ≡ p (mod e), 4N ≡ 1 (mod e)". Also the e-slice
column requires e odd (true: e ≡ 3 (mod 4) since p ≡ 1 (4)); and for the c-line with c odd, N = cp + 1 is even, so [N] ∉ G —
the event concerns odd divisors only; say so.

Table 2.2 recomputed from scratch (`scripts/review_r272_table22.py`): all 30 rows × 6 columns identical. Verdict:
**Thm 2.1 (a),(b),(c)(i)–(iii): SOUND (D3 cosmetic). (c)(iv) + slogan: GAP → SOUND-AFTER-REPAIRS (D2).**
(c)(i) re-derived: Gal(ℚ(ζ_ℓ, a_i^{1/ℓ})/ℚ) = (ℤ/ℓ)^k ⋊ (ℤ/ℓ)^×, [u, v] = (u−1)v exhausts (ℤ/ℓ)^k for any u ≠ 1 (needs ℓ ≥ 3 and
independence in ℚ(ζ_ℓ)^×/ℓ-th powers, which follows from independence in ℚ^× for ℓ odd). (ii) D₄ with commutator of order 2
needs a ≠ ±□ AND a ≠ −4b⁴ (the latter is the author's Sophie-Germain remark; it should be added to the hypothesis of (ii),
not only to the remark, since then Ω = ℚ(i) is abelian). (iii) fine for genuinely dihedral Rédei fields
(Q(√a, √b) biquadratic); degenerate a = b cases are cyclic quartic — say "biquadratic Q(√a,√b)" as hypothesis.

## §3 — Lemma 3.1, Prop 3.2, Thm 3.4
Re-derived. Lemma 3.1 is the product formula plus Dirichlet; Prop 3.2 ⟸ (Σ(s) ∪ Σ(s)·g_L ⊂ Σ(N) for every factorisation of
L, since L itself is a divisor) and ⟹ (L prime is an abstract compatible configuration) are correct *for the abstract notion
of "forced"* (note: realising "L prime" by an actual prime p in the class needs two linear forms prime simultaneously —
that is exactly HC's job in §6, not Dirichlet's). Thm 3.4 re-proved: at p ≡ 1 (M), v_q(N_i(p)) = v_q(N_i(1)) for q ≤ B,
t | 4·D! | M gives [N_i(p)] = [N_i(1)], so the forced set is ⊂ Σ(N_i(1)) and the three size arguments (4d−1 ∤ 4d+1;
4c − 1 > c + 1; e | a + b ≤ (1+e)/4 + 1 < e) are right. **From-scratch check** (`scripts/review_r272_thm34.py`; forced set
built directly from trial division, all four lines, signed e-slices with L in a, in b or in neither): 8 primes p ≡ 1 (M)
each for (D, B) = (6, 26), (12, 50), (12, 5), (20, 82) (M up to ~10¹⁰⁶): **0 forced firings**; positive control (random
p ≡ 1 (4) ~ 4·10¹², same code): 446 firings. Modulus/c-line question raised by the author: for c odd, cp + 1 is even and
v₂(cp+1) = v₂(c+1) because 2^{e₂} > 16D(D+1) > c + 1; only odd divisors can be ≡ −1 (mod 4c), so the 2-part is harmless.
q^{e_q} > 4D + 1 already suffices for Thm 3.4; the stronger q^{e_q} > 16D(D+1) ≥ t·N_i(1) is what Thm 6.1 needs (it makes the
cofactor's class mod t constant along p = 1 + Mk: t | M/s_i). Say this explicitly.
Verdicts: **Lemma 3.1 SOUND; Prop 3.2 SOUND (D5, D6 minor); Thm 3.4 SOUND (D4 minor).**

**D4 (MINOR) — Thm 3.4 proof**: "Σ(s) ∪ Σ(s)·g_L is the set of classes of divisors of N₁" is false when the B-rough part of N₁
is composite (e.g. B = 5, d = 12: N₁ = 49, forced set {1, 49} vs divisors {1, 7, 49}). Only "⊂" is needed and true. Repair:
replace "is" by "is contained in". Also explain the role of 16D(D+1) as above.

**D5 (MINOR) — Prop 3.2 / §3 preamble**: "s known from p mod M_B, e_q large" is false for the (positive-density) p with
v_q(N) ≥ e_q. Repair: define s := ∏_{q ≤ B} q^{min(v_q(N), e_q)} (what p mod M_B actually reveals) and let the opaque cofactor
absorb the rest; the criterion and the proof are unchanged (L = prime remains an admissible abstract completion once
q^{e_q} | N, as the adversary may take v_q(N) = e_q). Lemma 3.1 also contains a garbled fragment "(for t ∤ … :".

**D6 (MINOR, unproved assertion inside a PROVED item) — Prop 3.2, sentence "for |H| ≥ 3 and k ≥ 2 it can still fail for every
choice of images (the adversary has k − 1 free coordinates)".** No proof, and the quantifier ("for every choice of images")
is not what the parenthesis supports (it supports "for some choices"). Repair: delete, or state "for some image patterns"
with an explicit example, labelled Assessment.
