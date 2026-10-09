# AGENT REPORT O108 — the m/φ(m) loss and the Type I log log N

Branch `side-agent/et-typei-loglog`. Deliverable: `EXCEPTIONAL_MN3.md`; scripts
`scripts/emn3_coprime.py`, `emn3_modes.py`, `emn3_identities.py` (+ `.out.txt`). One self-review was
run (deep reviewer: no FATAL; 5 MAJOR, all in §3 and all repaired by weakening or fixing the text;
it confirmed Prop 2.3 and Theorem L').

## Results

**(ii) m/φ(m) loss: REMOVED (PROVED rel. ET Thm 7.1, BT, Shiu, PV; effective).**
* Prop 2.3 proves ET Prop 1.4 with the coprimality gain:
  `Σ_{a≤A,b≤B} τ(kab²+1) ≪ (φ(k)/k)·AB log·Λ`, with `Λ = O(1)` unless the linear variable is
  `< k^{1/3}·polylog` (and `Λ ≤ 1 + log(1+k)` always).
* Two changes produce it:
  1. Keep the indicator `(m₀,k) = 1` that ET's `ρ ≤ 1∗χ` drops.
  2. Use Pólya–Vinogradov in the small-q range, and Kronecker-symbol PV after reciprocity in the
     large-q range, in place of the period bounds.

  Every term then carries `W_{2k}(B) ≪ (φ(k)/k) log B`.
* **Theorem L'**: `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}`. MN2 Thm L had `/φ(m)`.
* The remaining gap to Thm U is now `(log log N)^{1/3}` in the threshold. Before it was
  `(m log m/φ(m))^{1/3}`.
* EVIDENCE: `scripts/emn3_coprime.py` shows the normalised average tracks `φ(k)/k`.

**(i) Type I log log N (ET's open conjecture, = MN2's `log L`): NOT removed.**
* PROVED: ET's 3-coordinate parametrisations give exactly the progression moduli
  `4ad, 4bd, 4ab, 4acf, 4cdf` (+ twins). The completeness of this list is EVIDENCE only (generic
  Gröbner elimination).
* PROVED: all these moduli are `≥ N^{1−η}` on a region R_bad of area 1/6 of the small-c slice.
  We read this as the precise form of ET's "no similar trick" remark. That reading assumes the
  divisor mass is log-uniform, which is an Assessment.
* Assessment: Weil/Kloosterman counting with one fixed coordinate reduces the bad region to R**
  (area 7/72: `a ≥ √N`, `e, f ≥ N^{2/3}`, `d ≤ √N`).
* PROVED, elementary: `ef − 4a²d = 1` ⟺ `[[e,2a],[2ad,f]] ∈ SL₂(ℤ)`, and the prime is the linear
  form `2cM₂₁ − M₂₂`. For fixed d these points are parity-restricted lifts of Heegner points of
  discriminant −4d on X₀(d).
* A sufficient target on R** is (H**): equidistribution mod q of these Heegner points, averaged
  over `d ≤ √N`, in the joint level–discriminant aspect.
* Five naive approaches are checked to fail on R_bad/R**:
  1. BT on a single progression;
  2. BDH/Montgomery–Hooley via Cauchy–Schwarz (fails by a power of N);
  3. a one-variable Selberg sieve;
  4. Weil counting with one fixed coordinate;
  5. Erdős's trick.
* Theorem 3.8 (PROVED, conditional on the level-of-distribution hypothesis LD for the small-c
  Type I weights): LD ⟹ `Σ_{p≤N} f_I(p) ≪ N log² N`.
* The m-analogue (`LD_m`) is only a proposed extension. The self-review flagged the necessary
  care: the primes dividing m must be excluded, and the remainder allowance must be scaled by m.

**Literature:** web search found no later removal of ET's log log. The closest work is
Huang–Vaughan (binary case) and Elsholtz–Planitzer 2020 (k fractions). This was search-limited, not
a full citation crawl.

## Proposed ledger text (follow-up to (D)31 / MN2)
EXCEPTIONAL_MN3:
* Theorem L' (PROVED rel. ET Thm 7.1, BT, Shiu, PV; effective):
  `ρ_rep ≪ (L³ + L² log² m) log L/m + m^{−0.35}`. This removes MN2's m/φ(m) loss via a coprimality
  version of ET Prop 1.4 (Prop 2.3).
* The Type I log log is not removed. Its obstruction is located: R_bad (area 1/6, PROVED geometry)
  and R** (7/72, Assessment).
* Sufficient target: Heegner equidistribution (H**). LD ⟹ ET's conjecture (Thm 3.8, PROVED
  implication).

## For the parent's review
* Check Prop 2.3(b) against ET pp. 30–32, in particular the `(m₀,k)=1` indicator and the
  non-partition split (squares counted twice, which is harmless for an upper bound).
* Check the Prop 2.5 tiny-box exponents.
* Prop 3.3 areas: 1/6 and 7/72 (the self-review confirmed both).
