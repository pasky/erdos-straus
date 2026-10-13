# AGENT_REPORT_O199 — ES certificates as quaternion orders (spark relay T), checkpoint 1

Main file: CONSTRUCTIVE_ES.md. Scripts: scripts/ce_* (ce_lib.py exact even-Clifford/order arithmetic; ce_check_lemma11.py,
ce_check_thm12.py, ce_test1.py, ce_test2.py, ce_classes.py, ce_ss.py, ce_ss2.py, ce_check_prop31.py, ce_spine.py,
ce_rank.py, ce_rank2.py, ce_hecke.py, ce_t1_check.py). Branch side-agent/constructive-es (chi-flip and main merged in).
**ES is not solved, nor any infinite case.**

## SHARP:
1. **Five-slice ES certificates = path-shaped edges of the supersingular 2-isogeny graph (Thm 1.2, Thm 2.1, Cor 2.2;
   PROVED, class counts CERTIFIED).** C₀(L_w) (discrd 4p) sits with index 2 in a *unique* order E(L_w) and equals its
   even-trace part; for χ = −1, E(L_w) is an **Eichler order of level 2 in B_{p,∞}** (two maximal overorders = the two
   endpoint curves); for χ = +1 it is an Eichler order of level p in B_{2,∞}. The map L ↦ E(L) is a bijection
   𝔊⁻_p (ternary lattices of det p anisotropic at p) ⟷ X₀(2)^{ss}/⟨Frob, w₂⟩, with L ≅ (End(E,C)⁰)^#(p);
   |𝔊⁻_p| = #orbits checked for 8 primes p ≡ 1 (12) ≤ 193. ES-five(p) ⟺ some edge lattice has a path basis ⟺ some
   supersingular E carries trace-zero i, j with ij + ji = −2, deg i·deg j = tp + 1, (1 − i)(1 − j) ∈ t·End E.
   (Bijection is known in substance — Brzezinski/Lehman/Gross–Lucianovic style; the ES identification is new.)
2. **The middle letter t is a Frobenius distance (Prop 3.1, Cor 3.2).** θ_{L(E,C)} counts trace-zero endomorphisms of
   p-divisible degree / p; for a certificate, ε = −(1 + ij) has ε² = −tp, i.e. an isogeny E^{(p)} → E of degree t compatible
   with C. t = 1 ⟺ 𝔽_p-rational spine edge; spine certificates exist (p ≡ 1 mod 8) ⟺ p + 1 has a prime factor ≡ 3 (mod 4)
   (5013/19552 primes p ≡ 1 (8) < 10⁶ have none).
3. **Spectral no-go for χ-flip transfers (5.1–5.2).** Lattice operations (sub/super, Kneser ℓ-neighbours incl. ℓ = 2,
   duals, rescaling) preserve χ (PROVED). The neighbour-Hecke modules ℂ[𝔊⁺_p], ℂ[𝔊⁻_p] share **no cusp eigenvalue**
   (T₃ at p = 97, 193, 241, 313, 409; T₅ at 97, 193; EVIDENCE; explanation via JL + opposite Atkin–Lehner signs is
   Assessment from memory). Hence at these p every Hecke-equivariant map from the always-non-empty χ = +1 side to the
   certificate side factors through the constant: it transmits only the main term (B3/B6 in spectral form). An H-D flip
   must be non-linear / non-Hecke-equivariant.

## Results (labels)
* PROVED: Lemma 1.1 (2-adic isotropy ⟺ residues mod 4 not all equal; finite check); Thm 1.2 (Eichler ladder; finite local
  check over all 64 odd-unimodular diagonal ℤ₂-classes); Thm 2.1 (bijection; uses Gross–Lucianovic, Deuring); Cor 2.2
  (four equivalent forms of ES-five); Prop 3.1/Cor 3.2/3.3 (Frobenius distance, spine slice); Prop 4.1 (certificate ⟹
  explicit maximal orders, presentation (−A*, −tpA*), three non-residues A, A*, uv, in poly(log p) time without factoring);
  Prop 4.2 (polylog-t ES-five ⟹ deterministic maximal orders/QNR modulo factoring); 5.1; 5.4 T1 control.
* CERTIFIED: class-count equality (8 primes); r_L(m) = #{ε : nrd ε = mp} (456 lattices); overorder ladders (151 words at
  5 primes, 49 words at n = 9, 25, 49); spine criterion (4466 primes < 2·10⁵).
* EVIDENCE: spectral disjointness (5 primes); certificates not among the smallest orders at hard primes p = 1009, 1129,
  1201, 1801, 2521 (ranks by min(E⁰): 1, 1, 3, 1, 10; at 2521 the CM(−11) edges are non-certificates).
* Assessment: answer to the task's equivalence question — ES-five(p) is poly-time equivalent to "some level-2 Eichler order
  of B_{p,∞} has a trace-zero basis of Gram [[A,u,1],[u,uv,v],[1,v,A*]]" and to the endomorphism / lens-space-plumbing /
  λ(p) ≤ 3 forms; it is NOT equivalent to existence of a non-residue / maximal order / supersingular curve (all always
  true); no unconditional small-element theorem (Kaneko, Chevyrev–Galbraith, Goren–Love) constrains the exact
  off-diagonal pattern, which is where the certificate lives (5.3, B3).
* Not done: numerics to 10⁵ with full class enumeration (my enumerator is ~1 min at p ≈ 2500; done to 2521 on hard
  primes); literature statements for Pizer/Ibukiyama/Bröker/KLPT/Goren–Love are from memory (sources/ not checked).

## Sparks (not pursued)
* Theta lift of the path indicator: Θ^±(z) = Σ_{w ∈ X_p, χ(w) = ±1} θ_{L_w}(z) ∈ M_{3/2}(4p). ES ⟺ Θ⁻ ≠ 0. Is Θ⁺ + Θ⁻
  (all words) or Σ_w χ(w)θ_{L_w} a recognisable form (e.g. a combination of Cohen–Eisenstein / class-number generating
  functions)? Constant term is S(p) of CHI_FLIP §4.2.
* Since the Hecke route is closed (5.2), look for a *non-linear* correspondence 𝔊⁺ → 𝔊⁻ that is still natural: e.g. via
  the even sublattice L_e (det 4p) and its other overlattices, or via the dual of a level-4 Eichler order; screen with 5.1.
* Descent in t along the Frobenius-distance filtration: does a certificate at distance t force one at smaller t on a
  neighbouring edge (line graph of the 2-isogeny graph)? Numerics on the edge graph with ce_classes + neighbours.
* Composite n: the same dictionary puts words of n in B_{Ram,∞}, Ram ⊂ {ℓ : v_ℓ(n) odd} of odd size; n = 105 (χ ≡ +1) is
  the case where none of the four candidate algebras gets a path edge — a quaternionic description of the exception.
