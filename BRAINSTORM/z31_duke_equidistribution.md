# z31 — Duke-type equidistribution of Heegner points / CM points; small-scale and shrinking targets (O261 field memo 4; DEEP)

Labels as in DISCOVERIES.md. Read: Duke 1988 Thm 1 (`sources/lit2026g/duke1988.txt`, research agent C, verbatim). Others
abstract-level (Humphries–Radziwiłł arXiv:1910.01360; ELMV arXiv:0708.1113). Builds on WINDMILL_REDUCTION (ray classes mod t
see the ES condition fully, Prop 10.3), ASTRA_BRIDGE Thm 3.4 (E4), DFI rows of PARITY_AUDIT.

## (a) Counterpart and an exact dictionary (Lemma 4.1, PROVED, elementary)

Duke, Invent. Math. 92 (1988) 73–90, **Thm 1**: for fundamental d → −∞ and a fixed nice Ω ⊂ SL₂(ℤ)\H,
#(Λ_d ∩ Ω)/#Λ_d = μ(Ω) + O(|d|^{−δ}) (δ > 0, ineffective). Λ_d = Heegner points, #Λ_d = h(d) ≍ |d|^{1/2±ε}.

**Lemma 4.1 (E4 in Heegner-point language; PROVED).** Let p ≡ 1 (4), k ≥ 1, and g ≡ 3 (4) with 4k | g + 1 and
g | 4k²p + 1; put ρ ≡ (2k)^{−1} (mod g) (so ρ² ≡ −p (mod g)), s := (2kρ − 1)/g, m' := (4k²p + 1)/g. Then
γ = [[g, ρ], [−2k, −s]] ∈ SL₂(ℤ) maps the Heegner point z = (−ρ + i√p)/g of discriminant −4p to w = (−2kp + i√p)/m'.
Equivalently, the ES shot (2k, 1) ∈ L_ρ(g) of ASTRA_BRIDGE Thm 3.4(c) is the ideal factorisation
(1 + 2k√−p) = 𝔞·𝔞' in ℤ[√−p] with N𝔞 = g ≡ −1 (mod 4k). Hence
  **ES-shot(p) ⟺ ∃ k ≥ 1: the principal ideal (1 + 2k√−p) has an ideal divisor of norm ≡ −1 (mod 4k).**
*Proof.* det γ = −gs + 2kρ = 1. gz + ρ = i√p and −2kz − s = (2kρ − sg − 2ki√p)/g = (1 − 2ki√p)/g, so
w = gi√p/(1 − 2ki√p) = g(i√p − 2kp)/(1 + 4k²p). The ideal statement: 4k²p + 1 = N(1 + 2k√−p) and g | 4k²p + 1 is odd and prime to p. The element 1 + 2k√−p
is primitive (no rational integer > 1 divides it), so its ideal divisors of norm g are exactly the 𝔞_r = (g, √−p − r) with
1 + 2kr ≡ 0 (mod g), i.e. the single root r ≡ −(2k)^{−1} = −ρ (the other root branch of ASTRA_BRIDGE). Conversely any ideal
divisor of norm g ≡ −1 (mod 4k) gives such a (g, ρ). ∎ (Numerical check of the matrix
identity on all 24 shots with p ∈ {13, …, 2521}, k ≤ 5: `scripts/o261/heegner_shot_check.py`, 0 mismatches.)

## (b) Pointwise status / mechanism
Duke's theorem is pointwise in d (every large d), via Iwaniec's bound for Fourier coefficients of half-integral weight forms
(Waldspurger/Kohnen–Zagier link to Weyl sums over Λ_d). Small-scale versions (balls of radius |d|^{−θ}) are known for almost all
d or under GRH/Lindelöf (Humphries–Radziwiłł; abstract only, exponent not verified). ELMV (Ann. Math. 173 (2011)): Linnik's
ergodic method, pointwise under a splitting condition. All have **power-size point sets** (h(d) ≍ |d|^{1/2}) and **targets
that are regions of a fixed quotient** (SL₂(ℤ)\H, or a fixed-level X₀(N)).

## (c) Does it apply to B2? (Assessment, with the PROVED dictionary above)
1. **F3 — the target is not a region.** By Lemma 4.1 the ES condition is on the *ideal* 𝔞 (a representative), not on its class
   [𝔞] ∈ Cl(−4p) or on the position of the Heegner point in SL₂(ℤ)\H: "N𝔞 ≡ −1 (mod 4k) and 𝔞 | (1 + 2k√−p)". The modulus 4k
   is attached to the generator 1 + 2k√−p — tied modulus. Duke equidistributes classes (and, via Hecke characters, ideals of
   bounded norm in ray classes); "divides this particular element" is a divisor condition, not a Hecke-character condition.
   (Consistent with WINDMILL_REDUCTION Prop 10.3: classes see only the genus shadow, ray classes mod t see the event fully
   as a restatement.)
2. **F2 — scale.** Even if one fixes the representative problem, the expected number of ES shots among the h(−4p) ≍ √p
   reduced Heegner points is polylog (Σ_g r(g) d((g+1)/4)/g over reduced g ≤ √(4p/3), heuristic). A shrinking target of
   measure (log p)^{O(1)}/√p is far below any equidistribution scale |d|^{−δ} known, and below the √-scale where even
   GRH-level small-scale results stop (variance heuristics). The "target" is also not a ball but a union of ≍ √p arithmetic
   cells.
3. **What does work at Heegner scale:** the sign layer — (A/p) = ψ is a genus character, and genus theory is equidistributed
   trivially. F6 again.

## (d) Verdict: ANALOGUE (B2 = a divisor condition on ideals of ℤ[√−p] dividing 1 + 2k√−p; Duke = class/region statistics of
the same ideals). Mechanism transfer **NOT SHARP**: blocked by F3 first (not a region), F2 second (polylog vs √p points).
