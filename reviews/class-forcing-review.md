# R272 — hostile review of O263 (CLASS_FORCING.md, branch side-agent/class-forcing @ ec15ff50)

Reviewer scripts: `scripts/review_r272_*.py` (from scratch; author's z33 scripts not reused). ES is not solved.

## Summary verdicts (filled in progressively)
| claim | verdict |
|---|---|
| Thm 2.1 (a)(b)(c)(i)–(iii), Table 2.2 | SOUND (D3 cosmetic) |
| Thm 2.1(c)(iv) + bold summary + slogan | GAP → SOUND-AFTER-REPAIRS (D2) |
| Lemma 3.1, Prop 3.2 | SOUND (D5, D6 minor) |
| Thm 3.4 | SOUND (D4 minor; re-checked from scratch, 0 firings) |
| Lemma 4.1 | SOUND (weak but valid lower bound; brute force gives larger η) |
| Prop 4.2 | SOUND-AFTER-REPAIRS (D7 minor) |
| Prop 5.1 | SOUND (add −4d ∉ ℚ^{×n} to (c)) |
| Thm 5.2 | SOUND |
| Cor 5.3 | GAP → SOUND-AFTER-REPAIRS (D8 major: literal statement false, contradicts WINDMILL 10.2/10.3 R164 caveat) |
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

## §4 — Lemma 4.1, Prop 4.2 (target-Davenport)
Lemma 4.1 re-proved (Σ(S) = {x^j : |j| ≤ (n−1)/2} ∌ x^n; any H ∋ x^{±1} contains −1; t = 4q, q ≡ 3 (4): x = (−1, g) has order
q − 1 = 2n, n odd, x^n = (−1, −1)). **SOUND.** From-scratch brute force (`scripts/review_r272_eta.py`, DFS over multisets with
inherited pruning, all subgroups via ≤ 3 generators; `logs/review_r272_eta.txt`) shows the bound is valid but weak:
η((ℤ/28)^×) ≥ 4 (Lemma: 2; witness {3, 3, 19, 19}), η((ℤ/44)^×) ≥ 7 (Lemma: 4; witness {7⁴, 19³}, cap-limited),
η((ℤ/20)^×) ≥ 2 (Lemma n/a). Also checked (`scripts/review_r272_eta_pos.py`): for all d ≤ 150, η((ℤ/4d)^×) ≥ 1 ⟺ exp(G) > 2,
which is the unproved "i.e." at the end of Prop 4.2 (one-line proof to add: η ≥ 1 ⟺ ∃S with −1 ∈ ⟨S⟩ ∖ Σ(S)).
Literature: the document cites none. I am not aware of η under this name; closest standard notions are the Davenport
constant / Olson constant and the *critical number* (Diderrich–Mann, Gao–Hamidoune: sets of ≳ 2√|G| *distinct* elements avoiding
small-subgroup obstructions have Σ = G) — the latter is the relevant comparison for squarefree N and shows that repetition
(used essentially in Lemma 4.1) is what makes η large; with distinct classes the needed count is O(√|G|). Not checked against
sources (none in sources/). The conclusion of Prop 4.2 does not depend on the size of η: forced supply ≤ 1 already kills
every level with η ≥ 1. **Prop 4.2: SOUND-AFTER-REPAIRS (D7).**

**D7 (MINOR) — Prop 4.2.** (a) "≥ η(G) + 1 ≥ (q − 1)/2 escaping factors at a prime level q" needs q ≡ 3 (mod 4) (Lemma 4.1's
hypothesis); for q ≡ 1 (4) the same construction gives only odd(q − 1) − 1 (= 0 at Fermat primes 5, 17, 257, …). (b) "for
H = ker χ₋₄ it is 0 (z29(b))" holds only for total-product data (s = 1, g_L = [p]); once the smooth part is known the cofactor
can escape ker χ₋₄ (e.g. p + 4d = 3·L forces L ≡ 3 (mod 4)). (c) "the Davenport route needs ≥ η(G) + 1 escaping factors" should
read "a criterion of the form '> k escaping factors per subgroup ⟹ −1 ∈ Σ' must have k ≥ η(G)". (d) add the one-line proof
of "η(G) ≥ 1 ⟺ exp(G) > 2" (or cite the check above). Label "PROVED" otherwise fine.

## §5 — Prop 5.1, Thm 5.2, Cor 5.3
Prop 5.1 re-proved: (a) ℓ | p + 4d ⟹ p ≡ −4d (ℓ) ⟹ (−4d/ℓ) = (p/ℓ) = (ℓ/p) (p ≡ 1 (4)), and the Kronecker symbol (−4d/·) is a
character mod 4d. (b) is the tautology p ≡ −4d (mod ℓ) read in K_{n,d}; the "(N/π)_n = (4d/π)_n" sentence is the triviality
N ≡ 4d (mod p) (correct, harmless; the primary-normalisation details of n-th power reciprocity are skipped but not used).
(c) correct for n an odd prime with −4d ∉ ℚ^{×n} (if −4d is an n-th power, e.g. n = 3, d = 2, K_{n,d} = ℚ(ζ_n) and the datum
is trivial — add the hypothesis) and for n = 4. From scratch (`scripts/review_r272_sec5.py`): (a) on all (p, d, ℓ), p ≡ 1 (4)
< 2·10⁴, d ≤ 60: 140 310 triples, 0 violations (author reports 140 287 — a 23-triple counting difference, immaterial); the
Sophie-Germain claim (p/ℓ)₄ = (b/ℓ) for d = b², ℓ ≡ 1 (4), ℓ | p + 4b²: 7531 cases (b ≤ 7), 0 violations. **Prop 5.1 SOUND.**
Thm 5.2 re-proved: ℓ unramified in Ω and odd ⟹ Ω(i) ∩ ℚ(ζ_ℓ) = ℚ, so Gal(Ω(i)ℚ(ζ_ℓ)/ℚ) = Gal(Ω(i)/ℚ) × (ℤ/ℓ)^×; choose a
lift of C fixing i (possible by compatibility) times −4d mod ℓ (a unit as ℓ ∤ 2d); Chebotarev + infinitely many such ℓ
(Dirichlet). **SOUND.** (It is a statement about one factor; the multiset question is correctly deferred to §6.)

**D8 (MAJOR, misapplied citation) — Cor 5.3.** The literal statement "knowing [𝔩] ∈ Cl(K) for every factor … determines the
odd-part class of ℓ mod t only modulo squares" is false, and contradicts the very R164 repair of WINDMILL Prop 10.3 it cites
("On the divisor set alone the class map is injective (10.2), so there the class does determine m"). Concretely, for
N = tp + 1 and m | N with m ≤ √N the form [m, 2, N/m] of discriminant −4tp is *reduced*, so its class determines m itself
(checked: all 15 312 such divisors, t ∈ {3,7,11,15,19}, p < 3000, `scripts/review_r272_sec5.py` (3)). What Prop 10.3 proves is
the weaker, correct statement: *no function on Cl(K) equals N𝔞 mod ℓ^k beyond G/G² for all ideals 𝔞 of a class* (norms of
principal ideals are x² + tpy² ≡ x² mod ℓ^k, all squares occurring). Repair: restate Cor 5.3 as "(i) N𝔞 mod t is a class
invariant only modulo squares (odd part; ≤ characters mod 8 at 2); (ii) knowledge of [𝔩] *as an abstract element of Cl(K)
up to automorphism / via 2^∞-structure data* (what Rédei/Smith/Koymans–Pagano methods produce) yields only the χ-shadow;
(iii) a concrete class (reduced form) on the divisor hypercube determines ℓ itself — that is knowing the factorisation (B2)".
Also drop "(or of any line's N, via the divisor hypercube of a fixed principal ideal)": only N = tp + 1 (c-line with K =
ℚ(√−cp)) has the principal ideal (1 + √−cp) of norm N; no such ideal is exhibited for p + 4d or the e-slices. Label: PROVED
after restatement (i)–(iii), with (ii) needing a precise formulation of "abstract class data" or downgrade to Assessment.

## §6 — HC stated precisely; Thm 6.1 (supplement to D1)
HC as written: "admissible system f₀,…,f_r; Ω, C with C|_{Ω∩ℚ(ζ_{lead f₀})} = class of f₀(0) ⟹ infinitely many k with all f_i(k)
prime and Frob_{f₀(k)}|Ω ∈ C". **Inconsistent** (D1: Ω = ℚ(ζ₇), C = {−4 mod 7}, f₁ = (f₀+4)/s). Precise consistent form
(Bateman–Horn–Chebotarev): let Ω₀ = Ω ∩ ℚ^{ab} with conductor m, A ⊂ (ℤ/m)^× the residues whose Artin symbol on Ω₀ lies in
C|_{Ω₀}. *If there is k₀ with f₀(k₀) mod m ∈ A such that the system j ↦ f_i(k₀ + mj) (0 ≤ i ≤ r) is admissible, then there
are infinitely many k ≡ k₀ (mod m) with all f_i(k) prime and Frob_{f₀(k)}|Ω ∈ C.* For Ω = ℚ it is Dickson; the non-abelian
part of C imposes no local condition (Ω ∩ ℚ(ζ_n) ⊂ Ω₀ for every n), so this is the standard heuristic and is consistent.
With this HC and the D1(b) hypothesis (B ≥ every prime | m, e_q ≥ v_q(m), C|_{Ω₀} = 1), the rest of the proof of Thm 6.1
checks: the forms N_i(1+Mk)/s_i lie in ℤ[k] since s_i | M; for q ≤ B, f_i(k) ≡ f_i(0) = B-rough part of N_i(1) ≢ 0 (q); for
q > B the leading coefficients (M/s_i, M/(4s_i), eM/(4s_i)) are q-units and the number of forms 1 + 2D + 2#{e ≤ D, e ≡ 3 (4)}
< 4D + 2 ≤ B < q; and t | M/s_i (this is where q^{e_q} > 16D(D+1) ≥ t·N_i(1) is used) makes [f_i(k)] = [f_i(0)] mod t, so
Σ(N_i) = Σ(s_i) ∪ Σ(s_i)[L_i(1)] ⊂ Σ(N_i(1)) ∌ −1 (Thm 3.4). It is the four-line + Chebotarev extension of B1_LINE Thm 4.2
(same p ≡ 1 (M_σ) mechanism). **Verdict: FATAL as stated; SOUND-AFTER-REPAIRS (CONDITIONAL on the corrected HC).**

## §7 — EVIDENCE, recomputed from scratch
`scripts/review_r272_census.py 1000000 200` (own SPF sieve to 6·10⁶, own divisor/subgroup/forced code; every A-certificate
converted to (x,y,z) = (ad, acdp, cdp) and checked with exact fractions — all 39 171; `logs/review_r272_census_1e6.txt`):
| tier | author | reviewer |
|---|---|---|
| primes p ≡ 1 (4), 5 ≤ p ≤ 10⁶ | 39 175 | 39 175 |
| A failures | 193, 2521, 66529, 252001 | identical |
| Gen failures | 0 | 0 |
| F₁₀ / F₃₀ / F₁₀₀₀ failures | 734 / 43 / 4 | 734 / 43 / 4 (identical first/last lists) |
| X2 failures | 73 (1321, 1489, 2521, …, 981601) | 73, identical first 8 and last 3; 193, 66529 pass, 2521 fails |
| odd squares 9…998001 | 499, all tiers fail | 499, all tiers fail (Gen included) |
F₁₀₀₀ = A exactly is forced (p + 4d < 1000², so at most one prime factor > 1000). The T1 explanation (every unit ℓ | m² + 4d
has χ_{−4d}(ℓ) = 1, χ_{−4d}(−1) = −1) is correct. Haar densities (`scripts/review_r272_haar.py`, own sampler, p ≡ 1 (4) in
[10¹⁶, 2·10¹⁶] coprime to primes ≤ max(B, D) + 1; `logs/review_r272_haar.txt`): F_{10,200} 1.76 % (n = 20000; author 1.80 %),
F_{30,200} 0.13 % (26/20000; author 0.22 % from ~9/4000 — within sampling error, but the author's figure has ±50 % relative
error and should carry n), F_{10,1000} 0.82 % (33/4000; author 1.10 % = 44/4000, ~1.7σ), F_{1000,200} 0/4000 (author 0/4000).
**§7: SOUND as EVIDENCE**; suggest quoting the binomial uncertainty for the Haar figures.

## Novelty and labels
* Thm 3.4 is the classical "congruence (ET/Mordell-type) coverings never contain p ≡ 1 (mod M)" obstruction, essentially
  JOINT_BUDGET Prop 4.3 (4ab ∤ p − 1) + B1_LINE §4 in forced-factor language; unconditional, correctly PROVED, low novelty.
  **D9 (MINOR, attribution):** it is *not* a specialisation of LONGSHOT_PIGEONHOLE Thm 2.2 (an upper-density bound for
  TCC_θ certificates at p ≡ 1 (q₀), relative to PNT/Brun–Titchmarsh/Shiu) nor of POINTWISE_SIZE Thm C (CONDITIONAL on H,
  about arbitrary correct bounded procedures); say "analogue of" / "same profinite point as".
* Thm 6.1 extends B1_LINE Thm 4.2 (after D1 repair). Prop 4.2's "no pooling" is SS8 Lemma 2.3 verbatim (correctly cited).
* Thm 2.1(a), Lemma 3.1 are trivial (correctly flagged "trivial" for 3.1); Thm 2.1(b) is standard Chebotarev-in-compositum.
* The genuinely useful dictionary content: Prop 5.1(a) factor-by-factor link (already SS8 Lemma 2.2(b) in product form) and
  the §7 tier census. Overall: a closing (negative) dictionary, as the author says; no overclaim of ES progress anywhere.
