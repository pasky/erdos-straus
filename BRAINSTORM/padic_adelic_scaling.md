# Brainstorm O149(a): p-adic / adelic analysis of ES — local data are blind to p mod q

ES is not solved; nothing here proves any case of it. Scripts: `scripts/bs_padic_counts.py`
(unordered counts f_I, f_II), `scripts/bs_padic_classbias.py` (class-bias and parity tables).

## 1. Idea

Study the ES solution set of 4/n at all places at once. Possible routes:
* (i) an "adelic volume" main term, of the form σ_∞·∏σ_ℓ (local densities, Igusa zeta functions, p-adic
  integration), bounded below at every prime p, plus an integrality step;
* (ii) p-adic interpolation of the count f(n): ℓ-adic continuity on residue classes, Mahler expansions, an
  ℓ-adic measure;
* (iii) an "adelic positivity + integrality" mechanism beyond Brauer–Manin.

To prove ES, route (i) would need the local data to track the fluctuations of f(p). Route (ii) would need an
interpolation whose values carry archimedean (positivity) information.

## 2. Literature anchor

* Bright–Loughran, Bull. LMS 52 (2020), arXiv:1908.02526 (campaign-checked, GEOMETRY_ES §1). The Brauer–Manin
  set of U_n is non-empty for every n ≥ 2, so "BM is the only obstruction" is literally ES(n).
* Igusa local zeta functions and the rationality of Poincaré series (Igusa; Denef). Mahler's theorem: a function
  ℤ_ℓ → ℤ_ℓ is continuous iff its Mahler coefficients Δ^k F(0) tend to 0. Both from memory, standard.
* Moerman, *Generalized Campana points and adelic approximation on toric varieties*, arXiv:2407.03048. It defines
  "M-points", which generalise integral, Campana and Darmon points. Existence was checked by web search
  (abstract only); the content is not verified beyond the abstract.
* Markoff surfaces (Ghosh–Sarnak; Loughran–Mitankin, from memory) are log-K3 affine cubics. They fail the
  integral Hasse principle infinitely often with no Brauer–Manin explanation. So no general "adelic positivity
  ⇒ integral point" theorem can hold for this class of surfaces (red team H-F).

## 3. Results

**Prop A (scaling lemma; PROVED, elementary).** Let 𝒰_n : 4xyz = n(xy+yz+zx) over ℤ.
* For a prime ℓ, write n = u·ℓ^v with u ∈ ℤ_ℓ^×. Then (x,y,z) ↦ (ux,uy,uz) is an isomorphism of ℤ_ℓ-schemes
  𝒰_{ℓ^v} ⊗ ℤ_ℓ ≅ 𝒰_n ⊗ ℤ_ℓ.
* For n > 0, scaling by n gives an isomorphism U_1(ℝ) ≅ U_n(ℝ) that preserves the positive octant.

*Proof.* Substituting gives 4u³x'y'z' = uℓ^v·u²(x'y'+…). Divide by the unit u³. ∎

**Cor A1 (PROVED).** Take any invariant that depends only on the isomorphism class of the local integral model
𝒰_n ⊗ ℤ_ℓ: the counts #𝒰_n(ℤ/ℓ^k), the local density σ_ℓ, the Igusa zeta function, the Berkovich space over
ℚ_ℓ, or the tropicalisation over ℚ_ℓ. Such an invariant depends only on v_ℓ(n). In particular, for every prime
p ≥ 5:
* at ℓ ≠ p it is the invariant of 𝒰_1 ⊗ ℤ_ℓ, independent of p;
* at ℓ = p it is the invariant of the base change of the *single* ℤ[π]-scheme 4xyz = π(xy+yz+zx) along
  π ↦ p. So it is a function of p alone (for the point counts, of the residue field size). It does not see
  p mod q for any q ≠ p.

Hence every product heuristic σ_∞·∏_ℓ σ_ℓ(p), and every ℓ-adic-integration main term built from the local models
of U_p, takes the same value on all primes of comparable size, whatever p mod 840 is.

**EVIDENCE (bs_padic_classbias.py, all 470 primes in [3000, 7000]).** The real counts depend strongly on p mod q:

| class | mean (f_I+f_II)/log³p |
|---|---|
| p ≡ 1 (8) / 3 / 5 / 7 (8) | 0.088 / 0.170 / 0.126 / 0.291 |
| (p/3) = +1 / −1 | 0.140 / 0.202 |
| (p/7) = +1 / −1 | 0.160 / 0.181 |
| square classes mod 840 (11 primes) / all others | 0.046 / 0.173 |

The factor is ≈ 3.3 between p ≡ 1 and p ≡ 7 (mod 8), and ≈ 3.8 between the square classes mod 840 and the
other classes.

**Interpretation (Assessment).** The residue-class signal is invisible to every local model. It enters only
through *global* objects restricted to local places:
* the ℚ-structure of U_p, i.e. the diagonal embedding;
* Brauer classes, i.e. BL's α_p. The scaling isomorphism of Prop A does not carry α_p to α_1. The local
  evaluation of α_p at ℓ | 2d depends on p mod 4d through Hilbert reciprocity. This is the genus character
  (−d/p) of GEOMETRY_ES Prop 5.1.

So the first-order fluctuation of f(p) is already a reciprocity phenomenon, not a local one. Odd squares are
the extreme case: Type I/II vanish there for reciprocity reasons (ET Prop 1.6), while all local data agree with
those of nearby primes.

**Prop B (ℓ-adic interpolation carries no positivity; PROVED, elementary).** Let F: ℕ → ℤ_{≥0}, with F(m²) = 0
for every odd m. This holds for F = f_I, f_II, or any count of solutions with n dividing exactly one or exactly
two denominators. Fix a prime ℓ and suppose F restricted to {primes} ∪ {odd squares} extends ℓ-adically
continuously at the points m². Then for every j there is a K such that ℓ^j | F(p) for every prime p in an
ℓ-adic unit square class mod ℓ^K.

*Proof.* Every unit square class mod ℓ^K contains an odd square: replace m by m + ℓ^K if needed, and for ℓ = 2
note that the unit squares mod 2^K are the classes ≡ 1 (mod 8). Continuity at that square gives
F(p) ≡ F(m²) = 0 (mod ℓ^j). ∎

So ℓ-adic (and ℤ̂-adic) continuity can only produce *divisibility* on exactly the hard classes, never F(p) ≥ 1.
Positivity is an archimedean statement. ES would even force F(p) ≥ ℓ^j on all the hard classes mod ℓ^K. The
data point the other way: the hard classes have the *smallest* counts.

EVIDENCE that f_I, f_II are not 2-adically continuous at 9, at the levels tested: among primes
p ≡ 9 (mod 2^K) in [3000, 7000], all four parity patterns of (f_I, f_II) occur for K ≤ 7. This tests only
j = 1 and K ≤ 7. It is not a proof of discontinuity.

**Prop C (denominator / M-point form; PROVED, elementary; folklore in substance).** Let V = U_1, i.e.
1/X + 1/Y + 1/Z = 4. Then:
* ES(n) ⟺ V(ℚ)_{>0} ∩ (1/n)ℤ̂³ ≠ ∅, via x = nX;
* the sets B_n = V(ℚ)_{>0} ∩ (1/n)ℤ̂³ are monotone under divisibility;
* ES ⟺ every prime p ≥ 5 is the exact common denominator of some positive rational point of V. Note that
  V(ℤ)_{>0} = ∅ because Σ1/X ≤ 3.

In the s-coordinates of GEOMETRY_ES §2.2, this is an M-point condition on (ℙ², complete quadrilateral) in
Moerman's sense. At each prime ℓ, the multiplicities (m_1, m_2, m_3, m_S) of a primitive point (s_1:s_2:s_3)
with the lines s_i = 0 and S = Σs_i = 0 must satisfy m_i ≤ m_S + v_ℓ(n) − 2δ_{ℓ,2}. (This is a restatement of
"4s_i | nS".) So ES(p) asks for a positive M-point for a structure that differs from a fixed one only at the
single place p.

## 4. Barrier screen

* **B1.** Routes (i) and (ii) are congruence/Haar data by Cor A1. Local invariants are p-independent at ℓ ≠ p,
  and ℓ-adic continuity is a congruence property mod ℓ^K. So Theorem M / Prop A of POINTWISE_SIZE apply
  directly.
* **B2.** The fluctuation of f(p) lives in the global ℚ-structure, i.e. in the slice divisor events. No local
  object sees which N_θ(p) has a divisor in the right class.
* **B3.** The adelic main term is ≍ log³p ≤ p^{o(1)}, so it passes the scale constraint. It fails one step
  earlier: it does not even predict the class means (factor ≈ 3–4 above).
* **B5 / T1.** At m², the local data at every ℓ ∤ m coincide with those at primes. The step that fails at
  odd squares is "local positivity ⇒ a Type I/II point". Composite descent is automatic in Prop C (B_m ⊂ B_{m²}),
  so T1 is passed only trivially, by restatement.
* **B6 / T7.** Counting M-points of bounded height on toric pairs (Moerman; Pieropan–Smeets–Tanimoto–
  Várilly-Alvarado, from memory) counts Σ_n f(n): an average over n.
* **"Beyond BM".** Other functorial obstructions (étale-BM, descent by tori) reduce to BM for rational
  surfaces (Harari/Skorobogatov-type results, from memory, unverified for this open, singular surface).
  Markoff-type surfaces show that unexplained failures occur in this class.

## 5. Viability Assessment

**COLLAPSES to B1 (local data) and B2/B6 (global data) at step "local densities ⇒ pointwise count".**
Strongest reason: by Prop A, every local invariant of U_p is literally independent of p mod q, while f(p) varies
by a factor > 3 across classes mod 8.

By-products:
* Prop A / Cor A1 (PROVED): local blindness to residue classes.
* Prop B (PROVED): ℓ-adic interpolation forces divisibility, not positivity, on the hard classes.
* Prop C (PROVED, folklore in substance): ES as an M-point / denominator problem on a fixed surface. This is a
  possible bridge to the Campana/M-point literature, but every known theorem there is an average count.
