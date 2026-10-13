# R185 — hostile review of O185 EXPONENT_COVERING.md (reviewer 1 of 2, full document)

Reviewer branch `side-agent/review-expcover-1`. From-scratch scripts `scripts/review_ec_*.py`.
Repairs applied (author branch quiet): D1, D2, D3, D4, D5, D6, D7, D8, D9, D10 (wording + rerun log), D11, D12 — directly in EXPONENT_COVERING.md and the bsK memos, each marked "(R185 repair)".
Status: round 1 complete. **No FATAL defects. The headline infinite result (Thm 4.1) is SOUND**: all 11 certificates pass a
from-scratch exact checker. 2 MAJOR (D3 proof gap for "squares are sterile", repairable by citation; D12 overclaimed scope of the
Proth negative), 10 MINOR (D1, D2, D4–D11).

## Summary verdicts
| claim | verdict |
|---|---|
| Lemma 1.1 periodicity | SOUND |
| Thm 1.2 equivalence (a)⟺(b) | SOUND |
| Thm 1.2 square clause Sq ⊂ S | GAP as written → SOUND-AFTER-REPAIRS (D3) |
| Thm 1.4 (ET + divisor classes) | SOUND-AFTER-REPAIRS (D3, D4) |
| Cor 1.5 integer unit-square points | SOUND (proof wording D5); negative consequence needs D3 |
| Prop 2.1 | SOUND-AFTER-REPAIRS (D6, D7); B1 reading = Assessment |
| Prop 2.2, k = 27 table | SOUND (D8 editorial) |
| §3 dictionary | SOUND as a restatement; Skolem/B–H "exactly" overstated (D9) |
| **Thm 4.1 (ES for all k·2^m+1, 11 k)** | **SOUND** (D1, D2 wording) |
| §4.2 survey | EVIDENCE, consistent with an independent screen (D10) |
| §4.3 k = 9 near-square | SOUND |
| §5.1 S-unit | SOUND; "B1 = limit" is Assessment (D11) |
| §5.3 Proth negative | SOUND for ET/divisor (or polynomial-solvable) classes; scope overclaimed (D12) |
| §5.4 novelty | plausible; no prior found by reviewer |

### Thm 4.1 (ES for all k·2^m + 1, k ∈ {1, 9, 21, 27, 57, 171, 231, 315, 393, 495, 15015}) — **SOUND** (minor wording defects)
Independent checker `scripts/review_ec_cert.py` (sympy, exact; uses only (M, r, x(n), y(n), z(n)) from each certificate, ignores the
author's `exps`/`fam` fields and does not import any author code). For each of the 11 certificates and every class it verifies:
(i) 4xyz − n(xy+yz+zx) = 0 in Q[n] (this also confirms the coefficient lists are ascending); (ii) integer-valuedness of x, y, z on
n = r + Mt by the Pólya criterion (values at t = 0..deg) AND, as a cross-check, by reducing the cleared numerator modulo its
denominator D for all t mod D (all D ≤ 10⁶, so the cross-check was exhaustive for every class); (iii) positivity: positive leading
coefficient and exact largest real root (all bounds are ≤ 1, so positivity holds for every n ≥ 2); (iv) M = 2^s M′ with
M′ | 2^L − 1, and coverage of every m in [m₁, m₁ + 2L) with m₁ = max s (so n_m mod M is L-periodic for m ≥ m₁ for *every* class
simultaneously), plus exact evaluation of the solution at each such n_m; (v) all m < m₁ (at most 5 values per k) by an independent
ES search with exact verification. **Result: all 11 certificates PASS** (runtime ~2 s). The logic "cover at L consecutive
representatives m ≥ max s ⟹ cover all m ≥ max s" is correct (Lemma 1.1 for each class separately, all representatives ≥ every s).
Side facts re-checked (`scripts/review_ec_facts.py`): 315·8 = 2520, 15015·8 = 120120; 27·2^m+1 is prime for m ∈ {2, 4, 7, 16, 19,
20, 22, 26, 40, 44, 46, 47, 50, 56, 59, 64} (m < 80), so 27·2²⁶+1 and 27·2⁵⁰+1 are indeed prime and ≡ 529 (mod 840); the k = 27
character table of §2 is correct entry by entry, and the listed cases exhaust Z/12.
The ES-solvability of each class is fully contained in the certificate's explicit polynomial identity — the Thm 1.2 "ET classes
avoid odd squares" input (T1) is NOT used by Thm 4.1, nor is the ET/mordell_lib provenance of the classes. Label PROVED
(computer-assisted) is appropriate. Defects: D1, D2 (minor).

### Lemma 1.1 (periodicity) — **SOUND.** Re-derived; trivial.

### Thm 1.2 (compactness criterion, ET classes) — equivalence **SOUND**; square clause "Sq ⊂ S" **GAP as written, SOUND-AFTER-REPAIRS** (D3)
Re-derived both directions. (b)⇒(a): finite subcover of the compact Λ_k by clopen classes; for m ≥ s, n_m ≡ ν(m) (mod M) (odd
components equal, 2-components ≡ c mod 2^s); each of the finitely many classes has its own "sufficiently large" threshold, absorbed
in m₀. (a)⇒(b): integers m_j → ∞ are dense in Ẑ, n_{m_j} → ν(μ) componentwise (2-adically k2^{m_j} → 0), finite unions of classes
are closed. Correct. The square clause is the one that carries all NEGATIVE results (Thm 1.4's S′ ⊇ Sq^×, Cor 1.5's "no covering
for k = 4^j − 1", §3 "⟹ (EH_k)", §5.3 Proth statement). As written its proof is an appeal to an unstated "class-level form" of
ET Prop 1.6 plus a computation for moduli ≤ 3000 — neither proves an infinite statement. It IS repairable by a clean citation (D3).

### Thm 1.4 (with divisor classes) — **SOUND-AFTER-REPAIRS** (D3, D4)
D_q ∩ Sq^× = ∅ is immediate. The proof is indeed that of 1.2. Caveat D4: D_q is ES-solvable only given ES(q) for the specific prime q;
the topological equivalence is unconditional, but "covering ⇒ ES on the family" needs ES(q) for the finitely many q used (true and
checked in all certificates: the D_q identities are explicit there).

### Cor 1.5 (integer unit-square points: only k = 4^j − 1 at ℓ = 0) — **SOUND** (proof of the ℓ < 0 case garbled, D5)
Re-derived: ℓ ≥ 1 gives odd N = k2^ℓ+1 = s² with s a power of 2, so s = 1, impossible; ℓ = 0 gives k + 1 = 4^j. ℓ = −a < 0:
2^a(k + 2^a) = □ with k + 2^a odd ⇒ a even and k + 2^a = s² with s odd and a unit at every odd prime ⇒ s = 1, impossible. The
consequence "k = 4^j − 1 admits no finite ET/divisor exponent covering" is then correct GIVEN Sq^× ∩ U = ∅ (D3). With the D3 repair
it actually holds for the much larger class of ALL congruence classes solvable by polynomials (see D3) — a strengthening.

### Prop 2.1 (polynomial families glue local squares) — **SOUND-AFTER-REPAIRS** (D6, D7)
Closure = f(t₀ + TẐ) (continuous image of compact closure) and componentwise gluing: correct. Since "x ∉ (Z_q^×)²" is already
detected mod q (mod 8 for q = 2), clause (i) can be stated with e = 1 (e = 3 at 2) and clause (ii) is vacuous/circular (D6). The
"only finitely many q can do (i)" claim is FALSE without a hypothesis: f = c·g² with c a non-square gives (i) at every q with
(c/q) = −1 (D7). The B1 interpretation ("this is the mechanism behind B1") is an Assessment, not part of what is PROVED.

### Prop 2.2 + k = 27 example — **SOUND** (editorial D8)
Re-derived; A_q is a union of classes mod ord_q(2) (the q^e refinement is unnecessary for unit-squareness at odd q). The k = 27 table
was recomputed from scratch (`review_ec_facts.py`): every listed entry is correct, the five cases exhaust Z/12, each A_q is non-empty.
Note that Prop 2.2 only removes unit-square points; the actual k = 27 covering (verified) also handles non-square points.

### §3 dictionary — dictionary **SOUND** (it is Thm 1.4 + compactness, given D3); "exactly of the type of Skolem / Bertók–Hajdu" **overstated** (D9)
(EH_k) ⟺ Λ_k ∩ Sq^× = ∅ for k ≠ 4^j − 1 ✓; "coverable ⟸ (EH_k) + no sterile non-(unit-square) point, ⟹ (EH_k)" ✓. Citation checked:
arXiv:1407.6499 abstract (Bertók–Hajdu) indeed proposes a Skolem-like Hasse principle, proves it for "almost all" equations and
uses Erdős–Pomerance–Schmutz λ-moduli; Monatsh. 2018 doi 10.1007/s00605-018-1169-8 is their number-field extension ✓.
But (EH_k)'s local condition is "≡ some unit square mod M", while its global solutions are y = ±2^j: the local condition does NOT
come from the global equation k2^x + 1 = 4^j by reduction (a Skolem/B–H local condition would be k2^x + 1 ≡ 2^{2y} mod M). So (EH_k)
is strictly stronger than the B–H principle for k2^x + 1 = 4^y and is not an instance of it. "SHARP" is too strong a tag.

### §4.2 survey (EVIDENCE) — **consistent**, not reproducible from stored data (D10)
Independent necessary-condition screen `scripts/review_ec_sqscreen.py` (unit-square kill by primes q ≤ 3·10⁵ with ord_q(2) | L, L in
a fixed list of 21 values ≤ 2520): 85 of the 100 k ≡ 3 (mod 6), k ≤ 600 are square-clear (≥ 78 covered ✓); the 15 survivors are
{3, 15, 63, 255} ∪ {33, 69, 195, 273, 285, 291, 351, 435, 465, 513, 573}, and each survivor has an integer square point
k2^ℓ+1 = s² or k + 4^j = s² whose primes q | s have ord_q(2) not dividing any L in my list (e.g. 23, 47, 79, 191, 193, 383) —
consistent with the author's "OPEN = search limits around square points". k = 105 is square-clear (so it is a genuine candidate for a
non-square sterile point or simply a search-limit case; matches Spark 2).

### §4.3 (k = 9 near-square) — PROVED parts **SOUND**
Recomputed (`review_ec_xstar_check.py`): along X₂, ν_q = 289 (unit square for every q with v₂(ord_q 2) ≤ 2 — none fails for q < 5000)
and ν_q = −287 when v₂(ord_q 2) = 3. Such q are automatically ≡ 1 (mod 16) (q ≡ 9 mod 16 ⇒ 2 is a QR ⇒ v₂(ord) ≤ 2), so the claim
"unit square at every q ≢ 1 (16)" is right; first bad primes 241, 353, 433 ✓. The I1 (3, 38737, 287) class verified by my checker.
Supporting check for D3: `scripts/review_ec_etsq.py` (own implementation of the seven ET Prop 1.9 families from the ET text, not
mordell_lib; I1 restricted to 4a²d+1 ≤ 10⁶): all 51173 distinct classes of modulus ≤ 3000 are primitive and none has a square residue.

### §5.1 S-unit families — classification **SOUND** (multi-exponent Thm 1.4 transfer only sketched but routine); "B1 is the S → all-primes limit" is **Assessment/heuristic, not PROVED** (D11)
Re-derived: for u = Π p^{a_p} with all a_p ≥ v_p(M), n mod M is periodic in (a_p mod ord_{M′}(p)); integer unit-square points ⟺ k·u + c = v²
with u, v S-units (a two-term S-unit equation, finitely many solutions); S = {2,3}, k = 1: 2³+1 = 3² and 3+1 = 2² ✓.

### §5.3 uniformity / Proth — **SOUND for ET+divisor classes** (and, after D3, for all polynomial-solvable classes); bold "every fixed-slice / congruence method" **overclaimed** (D12)

### §5.4 literature / novelty — **plausible**
My web searches (Jina; "Erdős–Straus" with Fermat/Proth/k·2^n+1/exponential family) found no prior "ES for all k·2^m + 1" statement;
only congruence-class results. Not exhaustive (no MathSciNet/zbMATH access). The author's own caveat (novelty is in form, each family
lies in finitely many solvable classes) is accurate. Thm 1.2's compactness argument is standard (Sierpiński-type covering + profinite
compactness); presenting it as new is fine only as "new in the ES context".

## Numbered defects (no FATAL)
**D3 (MAJOR, repairable; Thm 1.2 square clause, line "Squares: if an ET class r (mod M) contained x ∈ Sq …").** The proof leans on an
unstated "class-level form" of ET Prop 1.6 (which is about Type I/II solution counts of a single odd square n, with coprimality
conditions) plus a finite computation (M ≤ 3000) that cannot prove an infinite statement. Everything negative in the note (Thm 1.4
S′ ⊇ Sq^×, Cor 1.5 consequence, §3 "⟹ (EH_k)", §5.1 obstructions, §5.3 Proth) depends on it. *Repair:* replace by: "All seven ET
families are primitive classes (from their side conditions: f | 4a²d+1; (4ac,f) = 1; (4cd,f) = 1 with n² ≡ −4c²d a unit mod f;
(e,4ab) = 1; 4ad | f+1; (4ad,e) = 1). If x ∈ Sq lies in such a class r + MZ, x_q is a unit for q | M, hence r is a unit square mod
every prime power of M, r ≡ s² (mod M) with gcd(s, M) = 1, and the class is a primitive class represented by the perfect square s².
By Mordell (Diophantine Equations 1969) / Schinzel (Funct. Approx. 2000), as quoted in ET p. 7–8, such a class is not solvable by
polynomials, while every ET class is (ET Prop 1.9, converse). For Sq^× primitivity is automatic, so Sq^× avoids EVERY class solvable
by polynomials." Keep ec_t1check.py as computational control only. Then strengthen Cor 1.5/§5.3 accordingly (no finite covering
of 3·2^m+1 by polynomial-solvable congruence classes + divisor classes). [Reviewer could not access Mordell's book / Schinzel 2000;
reliance on ET's quotation, as already in POINTWISE_SIZE's novelty note.]

**D12 (MAJOR-wording; §5.3 bold "ES for all Proth numbers 3·2^m + 1 is out of reach of every fixed-slice / congruence method"; also §0
bullet 3, report SHARP 4).** PROVED only for coverings by ET/divisor classes (after D3: all polynomial-solvable congruence classes +
divisor classes). "every fixed-slice / congruence method" is not proved. *Repair:* state the precise class of methods in the bold
sentence; keep the Theorem-M transfer explicitly "not checked".

**D9 (MINOR-moderate; §3 and bsK_skolem_dictionary, "exactly of the type of Skolem's conjecture and … Bertók–Hajdu").** (EH_k)'s
local condition (≡ some unit square mod M) is not the reduction of a global exponential equation; it is strictly stronger than the
B–H principle for k2^x + 1 = 4^y. *Repair:* "an exponential local–global statement analogous to (not an instance of) Skolem / B–H";
drop "SHARP" or justify it.

**D1 (MINOR; §0 bullet 4, Thm 4.1 table row k = 27, report SHARP 3).** "27·2^m+1 ≡ 529 (mod 840) for m ≡ 2 (12)" fails at m = 2
(n = 109 ≡ 109 mod 840; mod 8 periodicity needs m ≥ 3). Listing 109 next to it suggests it is in the hard class. *Repair:* "for
m ≡ 2 (12), m ≥ 14"; list 109 separately.

**D2 (MINOR; §0 bullet 4, §4 "certified by an independent checker").** ec_cert.py is independent of the ES library but written by
the same author/session. *Repair:* "checked by ec_cert.py and independently re-checked by R185 (scripts/review_ec_cert.py)".

**D4 (MINOR; Thm 1.4, "Divisor classes").** D_q is ES-solvable only given ES(q). *Repair:* add "for the finitely many q used,
ES(q) is verified (explicit in the certificate); the topological equivalence itself is unconditional".

**D5 (MINOR; Cor 1.5 proof, ℓ < 0).** "s a power of 2: k = 4^j − 4^i odd forces i = 0" is muddled: k + 2^a is odd, so s is odd and
a unit at every odd prime, hence s = 1, impossible. Same for ℓ ≥ 1 (s odd ⇒ s = 1). *Repair:* rewrite the two lines.

**D6 (MINOR; Prop 2.1 "Consequently … (i) … or (ii) …").** (ii) is circular; non-unit-squareness at q is detected mod q (mod 8 for
q = 2), so (i) can take e = 1 (3). *Repair:* "a finite covering exists only if some single prime q has f(t) ∈ {0} ∪ non-residues
(mod q) for all t ≡ t₀ (T)".

**D7 (MINOR; Prop 2.1 last sentence "Only finitely many q can do (i)").** False for f = c·g² with c a non-square (infinitely many q
with (c/q) = −1). *Repair:* add "unless f is a constant times a square in Q[t]" (Weil applies to y² = f(t) only when absolutely
irreducible).

**D8 (MINOR; Prop 2.2).** Unfinished sentence "(for q ∤ k: A_q ≠ ∅ iff ... it is a union of classes …)"; "Λ_k ∩ Sq^× = ⋂_q A_q"
conflates exponent space and target (should be ν(⋂_q A_q)). *Repair:* finish/trim the parenthesis ("a union of classes mod
ord_q(2)"); write ν(⋂ A_q).

**D10 (MINOR; §4.2 survey).** Output not stored in data/ (only certificates for the 11 headline k), so 78/4/18 is reproducible only by a
re-run. *Repair:* commit the survey log. R185 re-ran `ec_survey2.py 3 600 300000` (~20 min; log committed as
data/ec/r185_rerun_survey2_k600.txt): **78 COVER / 4 OBSTRUCTED / 18 OPEN reproduced exactly**; OPEN = {9, 33, 69, 105, 129, 147,
195, 225, 273, 285, 291, 351, 435, 465, 513, 525, 561, 573} ⊇ my 11 square-survivors, and the 7 OPEN k that are square-clear in my
screen (9, 105, 129, 147, 225, 525, 561) account exactly for 85 − 78. Every OPEN k does have an integer square point (own check),
but "with an odd prime q | s of large ord_q(2)" is wrong for k = 225 (225 + 4³ = 17², ord₁₇(2) = 8) and k = 9 (17², 5²);
*repair:* drop "of large ord_q(2)" or say "OPEN k are exactly near integer square points; the covering cost is set by the
near-square level (§4.3), not by ord_q(2) of q | s".

**D11 (MINOR; §5.1 bold sentence, bsK_sunit_limit).** "B1 is the S → all-primes limit of an S-unit obstruction" is a heuristic; the
"(Assessment: …)" parenthesis comments on style. *Repair:* label it Assessment explicitly, and give the precise version: for S = all
primes, F_S(k) = {n ≡ 1 (mod k)} is a progression and Prop 2.1 applies.
