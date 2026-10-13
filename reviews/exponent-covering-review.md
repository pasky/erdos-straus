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
