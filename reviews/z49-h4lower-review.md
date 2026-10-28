# Hostile review: H4_NOT_POLYLOG.md (branch side-agent/z49-h4lower, commit 69126d93)

Reviewer: cross-model hostile review, wave z49 (branch side-agent/z49-rev-h4lower).
Object: Theorem 1. Unconditionally, infinitely many primes p ≡ 1 (mod 840) have no forest edge whose larger
endpoint lies in [4, exp((log p)^{1/13})], and they also have A_min(p) > exp((log p)^{1/13}). Under GRH the exponent
is 1/7. Corollary: FOREST_H4 Conjecture H₂ is false.

## Verdict: **SOUND** (minor repairs only)

I found no fatal or major defect. Every step of the chain checks out:
Lemma 2 (encoding) → Lemma 3 (mass) → Lemma 4 (graded LLL) → energy lemma (10) → Lemma 5 (BRW and coefficient
budget) → Lemma 6 (twist) → Lemma 7 (transfer).

I re-derived each step by hand and checked the decisive finite identities with my own scripts, written from scratch:
- `scripts/z49_revh4_check.py` → `data/z49_revh4/checks.json`
- `scripts/z49_revh4_encoding.py` → `data/z49_revh4/encoding.json`

The theorem is PROVED relative to one internal and unrefereed input, OMEGA10 Thm 3.4 / OMEGA11 Lemma 1.1, and the
document says so in its headline. It does not touch ES existence, and it correctly says so.

## Item-by-item findings on the eight requested points

**(1) Lemma 2: encoding, safe point, omitted edges. Correct.**
- For u < v ≤ H < p, an edge forces gcd(u,v) | p, so the endpoints are coprime. The edge condition uv | p+u+v is then
  exactly the reduced class −a−v mod av, and av ≤ H² = T.
- The covering class −d mod A is reduced because d | A+1.
- n = 1 meets E_(a,v) only at (1,2) and (2,3), and meets C_(A,d) only at (2,1) and (3,2). I re-enumerated this to
  H = 300.
- Neither (2,1) nor (3,2) is in G_A: G₂ = ∅, and (−2/3) = +1.
- At p ≡ 1 (mod 24) the two omitted edges are non-certifying. For {1,2}, t = (p+3)/2 ≡ 2 (mod 4). For {2,3},
  t ≡ 1 (mod 4) and tv−1 ≡ 2 (mod 4). Checked for 10⁴ residues.
- I also ran the encoding on actual primes, every p ≡ 1 (mod 840) below 3·10⁷ (9,632 primes), at H = 20:
  - the brute-force edge set on [1,H] equals the set of congruence events hit, with zero mismatches;
  - avoiding the shadow family C implies avoiding every G_A, with zero failures;
  - 592 primes avoid both families, and the ones I spot-checked have H₄, A_min ≥ 23.

**(2) Lemma 3: inflated mass. Correct.**
- The conditional Haar probability is φ(Q)/φ(lcm(m,Q)) = φ(gcd(m,Q))/φ(m). I verified this by brute force in 1,374
  cases, with even Q included.
- Both gcd identities hold, with 0 failures in 4·10⁵ random tests:
  - gcd(av, a+v+1) = gcd(a(a+1), a+v+1), since av ≡ −a(a+1) (mod s);
  - gcd(dk−1, d+1) = gcd(d+1, k+1).
- The divisor-sum steps are standard: Σ τ(n)τ(n+1) ≪ X log²X, and the Σφ(q) expansion.
- Numerically, at H = 64…2048, (3)/L⁴ falls from 0.048 to 0.035 and (4)/L³ falls from 0.118 to 0.092. These are upper
  bounds with room to spare; the true growth is about L³ and L², respectively.

**(3) Energy lemma: applies verbatim.**
- OMEGA11 Lemma 1.1 is stated for any family of events that fix initial segments of free digits, under any product
  measure, with absolute weights Λ_{ℓ,i} = λ_ℓ^{i+1} and the hypothesis ∏λ^{2v_ℓ(E)} ≤ 2, i.e. m ≤ T. That is exactly
  what the document uses.
- Prime 2. In OMEGA11 the atoms had odd M, so 2 was never a coordinate. Here 2-adic digits above 2³ are genuine
  uniform binary coordinates. The lemma is prime-agnostic, and n ≡ 1 (mod 8) is exactly a "fixed initial digits"
  situation.
- The first-free-index shift is handled by OMEGA11's own remark λ^{i₀+1}λ^{2(v−i₀−1)} ≤ λ^{2v}. Absolute weights are
  the stronger and the needed form.
- **Independent check:** I computed the exact digit-level Efron–Stein energy on 120 random systems of real congruence
  cylinders. The coordinates were 2-adic digits 3..5 on the fibre n ≡ 1 (mod 8), 3-adic and 5-adic digits 0..1, and
  the 7-adic digit 0. Moduli went up to T ∈ {64,…,1600}, with absolute weights 2^{log m_U/(2ℒ)}.
  - Maximum weighted energy: 0.980 unconditioned, 1.000 when conditioned on a cylinder (attained by constant F).
  - A single tight 2-adic cylinder (m = T = 64) gives 0.915.
- No violation was found. This is evidence for finite algebra, not proof.

**(4) Lemma 5: coefficient budget. Correct.**
- I re-derived the BRW identity. The cross term 2Σ A_i F_{<i} Σ_{j<i} A_j u_j vanishes because A_i F_{<i} A_j = 0 for
  j < i. My numerical check gives a maximum discrepancy of 1.4·10⁻¹⁴, using random u_j.
- The counts are right:
  - at most d digit sets for each m_U = d, so at most R² sets with m_U ≤ R;
  - sup‖f^{=U}‖ ≤ 2^{|U|} ≤ m_U;
  - hence K(u_j) ≤ R⁴, K(B) ≤ 1+N+2N²R⁴+N³R⁸, and D ≤ T³R².
- τ ≪ ℒ(S+ℒ), because log N ≤ 2ℒ.
- E(F−B) ≤ S e^{−3S}/(100(S+1)) ≤ δ/100.
- The unweighted K is the right norm for (17).

**(5) Lemma 6: real-character twist. Correct.**
- Real primitive conductors have a 2-part dividing 8 and a squarefree odd part. Since 8 | Q, f ∤ Q′ forces an odd
  ℓ₀ ∤ Q′, and ℓ₀ ≠ r.
- E[F′ψ] = 0, because F′ and ψ_rest do not depend on the ℓ₀ digits and the Legendre symbol mod ℓ₀ has mean 0 on units.
- The bound runs as follows:
  - |E[Fψ]| ≤ E[F′−F] ≤ Σ_{E∋ℓ₀} p_{ℓ₀}(E)·P(E∖ℓ₀ ∩ F′);
  - (9) gives the factor 1.033;
  - w_{ℓ₀} ≤ c follows from (7), because a_{ℓ₀} = 0.
- So |E[Bψ]| ≤ (0.017 + 0.010)δ ≤ 0.03μ, well inside μ/4.
- The cell-mean vanishing for f ∤ q_i holds for Haar measure on units, by primitivity.

**(6) Lemma 7: transfer and Siegel zero. Correct.**
- (14) is correctly formulated with one global exceptional pair, which depends on x through U = exp(c₀√log x). I
  re-derived the step the document sketches:
  - complex and non-exceptional zeros at height ≤ exp(a√log x) satisfy β ≤ 1 − c/log(q(|t|+2)), which is
    1 − O(1/√log x);
  - a per-modulus Landau exceptional zero that is not the global Landau–Page one satisfies β ≤ 1 − c/log U, so it
    contributes x·exp(−(c/c₀)√log x).
  - So only the global (ψ,β) survives, and it enters exactly for f | q.
- Case f | Q′. Then ψ ≡ 1 on the fibre, so ν = μ exactly. Using (15) and f ≤ Q′,
  λ = 1 − x^{β−1}/β ≥ ½·min(1, (1−β)log x) ≥ c/Q′.
  - Numerically, the minimum of λ/min(1,(1−β)log x) over 0 < 1−β < 1/2 and log x ≥ 4 is 0.509.
  - The error in (14) is absolute (it carries no factor 1−β). Choosing √log x ≫ log K + 3S + 2log Q′ therefore beats
    K·x·e^{−c₁√log x}, and (18) really does give positivity.
- Case f ∤ Q′. |ν|·x^β/β ≤ (μ/4)·2x.
- Primes p ≡ 1 (mod r), r > T, are coprime to every cell modulus, because cells use only primes ≤ T. Hence B(p) ≤ F(p)
  holds at every counted prime.

**(7) Exponent chain. Correct.**
- Unconditional:
  - S ≤ S♯ ≪ L⁴ log L;
  - log Q ≪ ℒ²S♯ ≪ L⁶ log L, from the charging Σ_ℓ H_{v_ℓ} ≤ Ω(m) ≪ ℒ, with each (ℓ,a) step paid by
    ℒw_ℓ/(c(a+1));
  - log D + log K ≪ L⁵ log L;
  - so log p ≪ (L⁶ log L)², and κ < 1/12; 1/13 is admissible.
- GRH: the error O(K√x log²) needs only log x ≫ L⁶ log L, so κ < 1/6; 1/7 is admissible.
- p > r > T = H² gives infinitely many distinct primes.

**(8) Corollaries. Correctly scoped.**
- H₂ is stated in FOREST_H4 l.262 for all primes p ≡ 1 (24). It is refuted.
- The FOREST_DEEP_FABLE §6 attachment gap and its sign-free form both bound v and w = (p+v)/A by (log p)^C, with
  v ≥ 4 (v ≡ 0 mod 4 or 7 mod 8). So the larger endpoint lies in the forbidden box, and both are refuted.
- The polylog covering statement is refuted.
- u_min, v07min, López and H_(★) bound only one endpoint, so they are untouched, as the document says.
- The hard-prime controls reproduce exactly with my own code: (5,5), (7,7), (5,5), (29,29), (29,29), (17,34),
  (19,37), (26,39), (51,111).

## Defect list

**Fatal:** none. **Major:** none.

**Minor (presentation and labelling):**
1. **Effectivity mislabelled.** (15) only needs 1−β ≥ c₂/f. That follows from the *effective* Page/Landau bound
   1−β ≫ f^{−1/2}(log f)^{−2}, which is already cited in POINTWISE_OMEGA9 §1. Siegel's theorem is unnecessary. As far
   as I can see the theorem is effective, so "the unconditional result is ineffective" is false modesty. It is
   harmless, but it should be corrected so that nobody downstream thinks Siegel is a load-bearing input.
2. **Citation for (14).** Davenport ch. 20 states the formula with a per-modulus Landau exceptional zero. The global
   one-exception version needs the Landau–Page threshold 1−c/log U. The document's derivation paragraph is correct (I
   re-derived it), but a precise modern statement should be cited, e.g. Montgomery–Vaughan I §11.3.
3. Lemma 3, proof of (3): "s ≤ 3v" should read s ≤ 2v. The bound is correct either way.
4. **Dependency visibility.** The headline correctly says "relative to the internally proved energy lemma". Any
   FRONTIER/BREADTH entry must keep that qualifier, because OMEGA10 Thm 3.4 is internal and unrefereed.
5. **Unused room (remark).** Importing the classical Gallagher theorem (G), as in OMEGA9 Thm 1.1, would give
   log p ≪ log Z, i.e. κ < 1/6 unconditionally. The document's choice not to do so is stated, so this is not a defect.
6. The §7 sentence "This also lower-bounds the ordinary certificate-survival probability δ(H)" should say "under
   prime-Haar with n ≡ 1 (mod 24)". This is implicit but worth making explicit.

## Assessment
- This is a genuine new theorem. It improves FOREST_DEEP_FABLE Prop 3.2(b) (c·log p) and FOREST_H4's
  log p·log log log p to exp((log p)^{1/12−o(1)}), and it refutes the campaign conjecture H₂.
- It is consistent with the parent's CRT heuristic, which predicts exponent 1/2. The proved exponents 1/12 and 1/6 sit
  below it, with no tension.
- It says nothing about ES or ES₅ existence.

Reproduction (each run under `ulimit -v 8000000`):
```
timeout 900 uv run --with numpy python scripts/z49_revh4_check.py > data/z49_revh4/checks.json      # ~10 s
timeout 600 uv run --with sympy python scripts/z49_revh4_encoding.py 20 30000000 > data/z49_revh4/encoding.json
```

---

## Follow-up review of commit fb71a959 (Gallagher transfer, Lemma 7b, and the effectivity repair)

Scope: only the diff `git show fb71a959`, i.e. the new Lemma 7b, the effectivity claims, the citation repairs and the
new headline κ < 1/6.

### Verdict: **SOUND**, relative to (G) and the internal energy lemma. Minor wording items only.

### What I checked

**1. (G0)/(G1) against the archived source.** I extracted MV III Theorem 28.19 from
`sources/omega9/montgomery-mnt3.pdf` (pp. 229–230) with pdftotext.
- The non-exceptional right side matches the source verbatim:
  x·exp(−log x/(κ log Q)) + (log x/log Q)²·x/Q.
- The exceptional form also matches:
  - the summand ϑ(x;χ₁) + x^{β₁}/β₁;
  - the right side (1−β₁)(log x)·x·[exp(−log x/log Q) + log x/(Q log Q)];
  - the prefactor multiplies both terms;
  - the second term carries no κ in the exponent.
- The draft's parameter-range slip and its missing height restriction are handled by fixing κ_G as in POINTWISE_OMEGA9
  §1, which was reviewed earlier.

**2. Parameter choice in 7b.** The source requires U^{6c} ≤ x and U ≥ Z. With U = x^{1/(κ_G B₀)} and x = Z^C:
- U^{6c} ≤ x holds iff κ_G B₀ ≥ 6c;
- U ≥ Z holds iff C ≥ κ_G B₀;
- the (G0) error is then C_G·𝒜·μx/φ(Q′)·[e^{−B₀} + (κ_G B₀)²/U], which is below 1/100 of the main term for a
  fixed large B₀.

All error terms are relative to μ because |c(χ)| ≤ E|B|/φ(Q′) = 𝒜μ/φ(Q′), with 𝒜 ≤ 1 + 2/99 by B⁻ ≤ F−B. So neither
S nor K enters log x. That is why (16b) has no S or K term and is linear in log Z, which is correct.

**3. Exceptional case.**
- In the (G1) regime, 1−β₁ < 1/(κ_G log U), so u = (1−β)log x < B₀. Then max(u,1) ≤ B₀ gives (23).
- **Case A** (f | Q′):
  - ψ ≡ 1 on the fibre, because odd real primitive conductors are squarefree and 8 | Q′. So c(χ) = μ/φ(Q′) exactly.
  - λ ≥ min(u,1)/2 is the bound from OMEGA9; my earlier numerical minimum for the ratio was 0.509.
  - By (15) and f ≤ Q′ ≤ Z, min(u,1) ≫ Z^{−1/2}(log Z)^{−2}, and the induced-to-primitive correction is
    R₁ ≪ Z³𝒜μ/φ(Q′). So x = Z^C with C ≥ 4 (and ≥ κ_G B₀) already beats R₁, and the document's "C > 5" suffices.
- **Case B** (f ∤ Q′): Lemma 6 gives |c(χ)| ≤ μ/(4φ(Q′)), so the depleted main term is at least μx/(2φ(Q′)).
- An exceptional character that does not appear in the expansion is harmless.

**4. Interfaces.**
- Overlapping moduli. A cell combined with n ≡ 1 (mod Q′) is a coset modulo lcm(Q′,d_i) ≤ Z, so c(χ) ≠ 0 forces
  cond χ ≤ Z.
- The map χ ↦ χ* is injective, so at most Z² coefficients are nonzero.
- log ℕ ≤ log Q′ + 1.04D ≪ Z.
- Every counted prime is ≡ 1 (mod r), hence exceeds T, so it avoids all cell primes and B(p) ≤ F(p) holds there.

**5. Effectivity, ordinary-PNT route.** I fetched the author-hosted MV I chapter 11 and checked the cited statements:
- Cor 11.10 (Page, p. 369) and Cor 11.12 (p. 370), which gives 1−β₁ ≥ c/(q^{1/2}(log q)²).
- Theorem 11.16 and Cor 11.20, equations (11.32) and (11.34), p. 381.
- The statement on p. 380 that the constants in Thms 11.3, 11.4, 11.16 and Cor 11.17 are effectively computable.

Cor 11.12 is stated only for an "exceptional" zero in MV's per-modulus sense. The added sentence is right that any
other real zero obeys the stronger zero-free-region bound 1−β ≫ 1/log f, so (15) holds for every real zero. Combined
with my earlier global-exception derivation, the κ < 1/12 route is effective as claimed.

**6. Effectivity, Gallagher route.** I believe this claim is correct: Gallagher's theorem is the engine of the
effective Linnik theorem, and its proof uses only the log-free density estimate and Deuring–Heilbronn, both effective.
However, the document asserts that "all constants used in (G) … are effective" with no source line, and MV III does
not state effectivity next to Thm 28.19.

### Minor items (no repair is blocking)
- **n1.** Add one sentence and a reference for the effectivity of (G). For example: the Linnik exponent is effectively
  computable (Heath-Brown 1992; Xylouris), and those proofs use exactly this log-free density plus
  Deuring–Heilbronn input.
- **n2.** "Thus even the worst Siegel-zero class…" in Lemma 7 should now read "exceptional-zero class". The document no
  longer uses Siegel's theorem, and the term invites the misreading that it does.
- **n3. Labelling for downstream citation.** The headline κ < 1/6 rests on (G), checked only in the MV III draft
  formulation, and on the internal OMEGA10 energy lemma. FRONTIER and BREADTH should record both results:
  - κ < 1/12, relying only on published MV I statements plus the energy lemma;
  - κ < 1/6, relative to (G) plus the energy lemma.

  The document already does this; downstream summaries should not collapse the two.
