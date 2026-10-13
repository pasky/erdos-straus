# R185 — hostile review of O185 EXPONENT_COVERING.md (reviewer 1 of 2, full document)

Reviewer branch `side-agent/review-expcover-1`. From-scratch scripts `scripts/review_ec_*.py`.
Status: IN PROGRESS.

## Summary verdicts
(filled in below as each claim is checked)

## Defects

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
