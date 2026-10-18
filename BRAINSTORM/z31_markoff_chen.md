# z31 — Markoff surfaces, strong approximation mod p, Chen's divisibility (O261 field memo 2; DEEP item)

Labels as in DISCOVERIES.md. Read by me: `sources/lit2026g/chen_markoff.txt` (Chen arXiv:2011.12940, pp. 6–7). Builds on
LITERATURE_2026 §(ii), LITERATURE_AUTOMORPHIC (Ghosh–Sarnak ✔), MARKOFF_ES.md ((J)36: cap-1 ES variants are integral points on
Markoff-type cubics), thin_group_orbits.md §3.

## (a) Counterpart statements (two different axes — the distinction is the point)
* **Axis 1 (fixed surface, varying reduction prime):** X : x² + y² + z² = xyz (Chen's normalisation), Γ = ⟨Vieta moves,
  permutations⟩. Statement: Γ acts transitively on X*(p) = X(F_p) ∖ {0} (BGS–Baragar conjecture). Consequence: strong
  approximation at p — every nonzero F_p-point is the reduction of a Markoff triple.
* **Axis 2 (varying surface):** X_k : x² + y² + z² − xyz = k. Statement: integral Hasse principle for X_k.
* ES's U_n : 4xyz = n(xy + yz + zx) is a **family in n** (E6), i.e. axis 2. Its projective closure is Cayley's 4-nodal cubic,
  as is the degenerate Markoff surface k = 4 (LITERATURE_2026 §(ii), our observation), but the log-K3 boundaries differ.

## (b) Pointwise status and mechanism
* **Axis 1 — PROVED for all but finitely many p (cited, read):** BGS (Chen Thm 1.2.3): (a) #{exceptional p ≤ x} = O(x^ε);
  (b) |X*(p) − C(p)| ≤ p^ε for the largest orbit C(p). **Chen Thm 1.2.5 (= Thm 5.5.4): for every p ≥ 3 every Γ-orbit on
  X*(p) has cardinality divisible by p.** Thm 1.2.6 (= 5.5.5, 5.5.7): the exceptional set is finite and explicitly bounded; for
  p ∉ E_bgs, X satisfies strong approximation at p. Mechanism: a congruence on the degree of the map from a component of a
  Hurwitz space of SL₂(F_p)-covers of elliptic curves to M_{1,1} (Chen Thm 1.3.1 = 3.5.1), i.e. *an arithmetic invariant
  of orbit sizes* (divisible by p) combined with a *giant-component* count (complement ≤ p^ε): an orbit of size ≥ p cannot
  fit in a complement of size ≤ p^ε. Effective threshold by Eddy–Fuchs–Litman–Martin–Tripeny (arXiv:2308.07579; research
  agent: UNVERIFIED value; LITERATURE_2026 quotes p > 3.45·10³⁹²).
* **Axis 2 — FALSE pointwise:** Ghosh–Sarnak (Invent. Math. 229 (2022), arXiv:1706.06712; abstract read by research agent):
  "for almost all k the Hasse Principle holds", while Hasse failures occur for ≫ √K (log K)^{−1/2} values k ≤ K
  (LITERATURE_AUTOMORPHIC, ✔); Loughran–Mitankin / Colliot-Thélène–Wei–Xu explain part of them by Brauer–Manin (UNVERIFIED
  theorem numbers). The count of integral points per orbit is power-of-log in the height (growth of Vieta orbits).

## (c) Transfer to B2 — exactly what blocks it
1. **Wrong axis.** Chen/BGS answer a *connectivity* question on a set of size ≍ p² whose non-emptiness is trivial; B2 is an
   *existence* question for one member of a family (axis 2). On axis 2 the Markoff analogue of "ES for every n" is false
   (Ghosh–Sarnak), so the Markoff world, read correctly, is evidence that pointwise integral Hasse on log-K3 families needs
   something beyond counting and beyond Brauer–Manin; it supplies no positive mechanism.
2. **No infinite group on the fibre.** The Chen–BGS argument needs a group Γ acting on the F_p-points with orbits to be
   counted. U_n(ℤ) off the lines is finite (BL Lemma 3.10) and the ES equation is linear in each variable with no Vieta
   involution (thin_group_orbits §3, PROVED there); the ES automorphism group is finite.
3. **Divisibility invariant absent.** The campaign checked orbit/component sizes of its signed ES graphs: sizes 1…16, no
   congruence pattern (SIGNED_REFACTOR §8(ii), cited in LITERATURE_2026 §(ii)). A Chen-type invariant would need a moduli
   interpretation of ES solutions as covers; the closest is the supersingular/Eichler-order dictionary ((J)33, (J)35), whose
   objects are again counted only through the genus character (F6).
4. **Scale (F2).** BGS's giant component uses |X*(p)| ≍ p²; ES has ≍ (log p)² certificates.
Where Markoff *does* meet ES: cap-1 ES variants are integral points on Markoff-type cubics ((J)36), and the e = 2 cell is a
Markoff-type class-group problem ((J)43, "not easier"). Those are relaxations, not B2.

## (d) Verdict: ANALOGUE (same surface type — Cayley cubic/log K3; different axis). Mechanism transfer: **NOT SHARP**.
The one structural lesson worth recording: Chen's is a *non-counting pointwise* argument, but it proves uniqueness of an orbit,
not existence of a point; no pointwise existence theorem for integral points on a varying family of non-homogeneous log K3
surfaces is known in this literature (research agent B and LITERATURE_AUTOMORPHIC found none).
