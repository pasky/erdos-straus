# z27_sparsity_hypothesis — GRH + a p-free, class-free sparsity statement ⇒ e*(p) ≤ (log₂p)^{9/2+o(1)} (O256)

**Idea.** Replace FORCED_WINDOW's Hypothesis W (p-dependent existence of a balanced q in the class −p mod P with χ_p(q) = −1)
by the weakest statement that makes the class-blind count of z27_fejer_blind_count usable in a single class.
**Result (BALANCED_LATTICE §4).**
* *Hypothesis EQ* (no p): primes in Bad₁(ε) (some character of order > 1/ε with 𝔻_S < ε) are not over-represented, beyond a
  constant factor and x^{1/2}(log x)^A, in any reduced class mod 8P(y), P(y) ≤ √x. **Thm 4.1: GRH + EQ ⇒ e*(p) ≤ (log₂p)^{13/2+o(1)}.**
* *Hypothesis S* (no p, no classes): #Bad₁(x^{−3/(2k)}) ∩ [1, x] ≤ x^{1/2}(log x)^A. **Thm 4.2: GRH + S ⇒ e*(p) ≤ (log₂p)^{9/2+o(1)}.**
  S is the uniform-discrete-log prediction (expected count ≈ x^{1/2}2^k/(2k! log x)); even its index-degenerate part
  (index ≥ x^{3/(2k)}) is open (known exponent 1 − 1/(2k) − O(1/k²), not 1/2); GRH-Chebotarev cannot reach it (error ≍ √x per ℓ).
* GRH is used only for the class/χ_p count and the small-order (Chebotarev-visible) part Bad₂.
**Literature.** FORCED_WINDOW Thm 4.3/Cor 4.4 (R264 D6–D8); CAP_INTERPOLATION Thm 4.2; Erdős–Murty, Kurlberg–Pomerance (rank-1
small-order primes); no standard named conjecture is known to me that implies EQ or S (Bad₁ is neither a Chebotarev set nor
primes in progressions).
**Barrier screen.** Cap ≥ 1 only (cap 0 = B2, Prop 5.1); step false at n = m² (no forced windows: (q/m²) = 1) — T1-compliant.
**Cheap numerics** (`scripts/z27_eqcheck.py`, data/z27/eqcheck_y7.txt; all 19 609 primes q ≡ 3 (8) ≤ 10⁶, 48 classes mod 840):
Bad₁-type q (ν < t and ord ψ_min > N^{1/k}/t) are spread evenly: χ² = 49.0 / 29.0 / 30.4 (df 47) at t = 0.3/0.5/0.7, max/mean
equal to a random relabelling. The full set ν < t (including small-order/index-degenerate q) is NOT uniform (χ² = 214 at
t = 0.3) — exactly the Chebotarev-visible part, which GRH handles. (y = 11: see BALANCED_LATTICE §6.)
**Assessment.** CONDITIONAL theorems (PROVED relative to GRH + EQ, resp. GRH + S); EVIDENCE for EQ at toy scale. The honest
answer to "W → GRH": GRH alone does not suffice by this method; GRH + a precisely isolated sparsity/equidistribution
statement about near-dependence of the first k primes mod q does.
