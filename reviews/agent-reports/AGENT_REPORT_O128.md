# AGENT_REPORT_O128 — Type II automorphic structure for pointwise ES

Branch `side-agent/typeii-spectral`. Main file: `POINTWISE_TYPEII_SPECTRAL.md`. Scripts: `scripts/t2s_param.py`
(identity, separation and genus checks vs brute force, p < 400), `t2s_count.c` (f_II(n) for n ≤ N), `t2s_numerics.py`
(+ `.out.txt`, p ≤ 10⁷), `t2s_predict.c` (+ `.out.txt`, per-family predictions for 30 primes near 10⁶).
Merged main once (LITERATURE_AUTOMORPHIC.md).

## Results
1. **SL₂ structure (PROVED, elementary).** Type II(p) ⟺ `ff' − 4c²(dp) = 1`, `f ≡ f' ≡ −1 (mod 4cd)` — the Type I
   identity `ef − 4a²d = 1` with p moved from the congruence (`f ≡ −p mod 4ad`) into the level (d → dp). Also
   det-p form `[[e,2a],[2ad,f]]` (Hecke T_p), divisibility duality `(4acd−1) | a+pc` vs Type I `(4acd−p) | pa+c`,
   residue form `(−p mod 4ab) | a+b`.
2. **Heegner points (PROVED).** Fixed (p,d): Type II points are Heegner points of discriminant −4dp, uniformly
   separated (cosh ≥ 3/2) at level dp (only `1/(2p)` in det-p coordinates).
3. **Exact incidence (PROVED).** Type II ⟺ `⟨u,v⟩_Q = −1`: the point lies on the shell at distance
   `arsinh(1/(c√|D|))` from the cuspidal geodesic `(∞, −1/2c)`. The shell width is `|D|^{−1/2}`, below the point
   spacing `|D|^{−1/4}`.
4. **Averaged check.** Averaging over p turns the incidence into one AP mod f (BV/BT). So Type II on average needs
   no spectral input (consistent with ET). The constant ≈ 0.05·log³ is an Assessment.
5. **Gap (Assessment, precise).** Using Young's Thm 2.1 bookkeeping, a shell of width w is reachable iff
   w ≫ D^{−1/18} (unconditional, = Young's strip range) or w ≫ D^{−1/6} (Lindelöf). Type II needs w ≍ D^{−1/2}.
   The gap is D^{4/9} (or D^{1/3} under GLH), and averaging over c and d does not close it.
6. **Genus lemma (PROVED).** Every Type II f, f' has `(p/f) = −1`, i.e. the points lie in genus χ_{−4d} = −1. This
   recovers ET Prop 1.6 for Type II (f_II(s²) = 0). The route therefore fails at n = p², as required. It also shows
   that the shell's spectral main term is false at squares: a correct method must carry the genus character.
   At reachable scales the input cannot distinguish square-mimicking primes.
7. **Numerics (EVIDENCE, p ≤ 10⁷).**
   * f_II ≥ 1 everywhere, and the dyadic minima grow (72 at 2²³). Min f_II/log³p ≈ 0.012–0.017.
   * The hard primes are the six square classes mod 840.
   * R = f_II/class-mean has min ≈ 0.28, and its spread widens slowly.
   * The d = 1 family alone fails for ~100 primes per block.
   * The fixed-p random-root Heegner predictor misses the hard primes: actual/predicted is 0.27–0.38 for them, vs
     0.9–3.5 for random primes.

## Not done / caveats
* Numerics stop at 10⁷. The C engine would do 10⁸ in about 2 min and 1.2 GB if wanted.
* §4.4 is an order-of-magnitude comparison with Young's error term (Lindelöf form included). It is not a theorem
  that no method works. §6(ii), the L-function factorisation of genus-twisted Weyl sums, is cited as standard and
  was not re-derived.
* The heuristic constant 0.05 ignores boundary/lower-order terms.

Checkpoint reached. Waiting for the parent.
