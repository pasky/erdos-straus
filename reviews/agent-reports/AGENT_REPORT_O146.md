# AGENT REPORT O146 — brainstorm: hatches H-A / H-B head-on (forced correlations and parity at fixed p)

Branch `side-agent/bs-correlations`. Three memos under `BRAINSTORM/`, scripts `scripts/bs_corr_*`, small logs
`logs/bs_corr_*`. **ES is not solved; no memo is LIVE.**

**(a) `BRAINSTORM/corr_joint_factorisation.md`: forced joint factorisation (H-A). Verdict: COLLAPSES to B5/T1
at the forcing step; PARTIAL as a sharp reformulation.**
* Composition identities among slice integers hold identically in n. Two of them are recorded:
  `(p+4a²d)(4c²dp+1) = p(4acd−1)² + 4d(cp+a)²` and the II{a,d}·II{b,d} identity (PROVED, symbolic).
* They only re-encode "one solution lies in several slices". Prop 3.1 (PROVED, trivial): "all slices empty"
  is consistent with every relation valid for all n, because it is realised at odd squares.
* The informative part is an exhaustive computation (two independent enumerators). For 2 ≤ n ≤ 10⁶,
  V_I(n) ∪ V_II(n) = ∅ exactly at the perfect squares and at the two even non-squares 288 and 336.
  Odd composites behave like primes, with f ≥ 14 on [10⁵, 3·10⁵].
* So the only realised all-empty patterns are the genus ones. **CONJECTURE SQ** (odd n: V(n) = ∅ ⟺ n square)
  is the minimal honest form of H-A. It is stronger than ES and still a growing-family problem.
* Strongest reason: forcing via relations is refuted by squares; what remains is "non-principal χ_n forces a
  hit".

**(b) `BRAINSTORM/corr_parity_layers.md`: parity-breaking at fixed p (H-B). Verdict: COLLAPSES to B3 at the
size layer.**
* Every II{a,d} slice falls into exactly one of five classes: hit / N prime / quadratic sign obstruction /
  higher-order obstruction / size-limited.
* Data at three primes near 10⁵–4·10⁶ plus the control 1001²:
  * at the square, every composite slice is quadratically obstructed (the genus character χ₋₄d, PROVED);
  * at primes about 20% of slices are sign-compatible, uniformly in scale, but only ≈1% of those hit.
* So the parity/sign layer is where T1 lives and it has power-size mass. A perfect parity-breaking input
  would change the expected count only by O(1). The polylog scarcity lives in the size layer, a Planck-scale
  divisor-in-moving-class event (H-A, B3).
* Long families (V ≍ p) face error ≍ V^{1/2} against main term log³p. Families with main term ≥ V^{1/2}
  have only polylog many members (Assessment).
* Strongest reason: parity is mis-targeted; the bottleneck is size, not sign.

**(c) `BRAINSTORM/corr_typeI_typeII_joint.md`: joint Type I ∪ Type II at one p. Verdict: COLLAPSES (confirms
H-G quantitatively).**
* Lemma 3.1 (twin slices, PROVED): if `e | a+b` and `e² ≡ 1 (mod 4ab)`, then the (a,b,e)-slice is solvable
  for Type I iff it is for Type II. Checked: identical twin counts (4158 each) over 2021 primes.
* Over the 2021 primes p ≡ 1 (24) in [10⁵, 3·10⁵], log f_I and log f_II have correlation 0.75. The bottom-5%
  sets overlap 10× above independence.
* A residual correlation of ≈ 0.58 survives the quadratic profile to 100, residue classes, L(1,χ_p) and
  quartic/cubic symbols (no non-abelian signal). It drops to 0.34 once C-slice congruence data modulo 4ab ≤ 2000
  are added.
* Strongest reason: the forced correlation is positive, so the union does not hedge.

**For the parent.**
* The one possibly reusable output is CONJECTURE SQ with its data. Hostile-check targets: the enumeration
  bounds in `scripts/bs_corr_vempty.c` (`4a²d ≤ n+2a`, `4acd ≤ 2n+2`); the independent check is
  `scripts/bs_corr_vempty_check.py`, ≤ 400.
* SQ is a strengthening, not a route. Its use is as a test bed: an H-A mechanism that needs primality
  beyond non-squareness is suspicious.
* The odd-n extension of the SQ scan is done: all 4 498 919 odd non-squares in (10⁶, 10⁷] have V(n) ≠ ∅
  (`logs/bs_corr_vempty_odd_1e7.txt`). So SQ is EVIDENCE for odd n ≤ 10⁷.
