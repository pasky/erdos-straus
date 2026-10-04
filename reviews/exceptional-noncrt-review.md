# Hostile review — EXCEPTIONAL_NONCRT.md (task O11, checkpoint 1)

Subject: branch `side-agent/noncrt-inputs-2` @ becb4ca — `EXCEPTIONAL_NONCRT.md`,
`reviews/agent-reports/AGENT_REPORT_O11.md`, `scripts/noncrt_checks.py`,
`data/noncrt/checks_m8.txt`. Checked against EXCEPTIONAL_THETA.md (ET-file:
Prop 2.4, Thm 2.5, Lemma 2.9, Cor 3.4, §6.1) and Elsholtz–Tao 1107.1010.
Reviewer branch: `side-agent/review-noncrt`.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered N1, N2, …

## Items

### 1. Prop 2.1 (Boolean sieve limit with high-level Walsh tail) — **SOUND**

Checked line by line.
* `|y^S(0)| = Π_S p_i` ⇒ `f_lo(0) ≥ 1 − r₀`; `E|y_i| = 2p_i(1−p_i)` +
  independence ⇒ `E|f_hi| ≤ r₁`; `E f_hi = 0` since every S in f_hi is
  nonempty (s(∅) = 0 ≤ λ). Correct.
* f_lo depends only on `x_V` (every S with s(S) ≤ λ lies in V). `f ≥ 0` ⇒
  `f_lo ≥ −|f_hi|` ⇒ (conditioning on x_V) `f_lo ≥ −h`. Correct.
* Thinning: with w fixed, `y_i = u_i w_i − p_i` is affine in u_i, so the
  multilinear expansion of `f_{lo,w}` has monomials `u^{S'}`, `S' ⊆ S ∩ Z`,
  multidegree in Λ. `h_w` depends only on `u_Z` (u∘w vanishes off Z).
* Symmetrisation: `Q(k) = E[f_{lo,w} | K = k]` because the iid Bern(q_g) law of
  u is uniform on each count-fibre; hence `Q ≥ −H` on the support. The
  Λ'-reduction only changes Q off the support (0 is in the support). Correct.
* Interpolation: `c_j L Q = c_j L (Q+H) − c_j L H ≤ |c_j L|(Q+H) + |c_j L|H`
  uses only `Q + H ≥ 0` at grid (= support) points; extending the grid sum to
  the full support uses `Q + 2H ≥ H ≥ 0`. Gives
  `1 − r₀ ≤ e^{Φ(w)}(E_u f_{lo,w} + 2E_u h_w)`. Correct.
* Averaging over w: `(1−r₀)E_w e^{−Φ(w)} ≥ (1−r₀)e^{−E_wΦ(w)}` needs
  `1 − r₀ ≥ 0`, which the proof handles (r₀ ≥ 1 trivial). ET Step 5 then
  applies verbatim (bands need `q_g ≤ 1/4`, guaranteed by `p_i ≤ 1/4` for all i).

No defect. (Prop 2.1 is a genuine, clean extension of ET Prop 2.4.)
