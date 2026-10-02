# Hostile review: EXCEPTIONAL_TWIN.md §§0–5 (branch side-agent/twin-windows @ b708bd1)

Reviewer: side agent (worktree-0003). Scope: `EXCEPTIONAL_TWIN.md` §§0–5,
`reviews/agent-reports/AGENT_REPORT_O1.md`, `scripts/twin_*.py`,
`data/twin/`, as of commit b708bd1 (copied into this worktree). Context
read: ET Prop 2.4, Thm 2.5, Thm 2.7, Lemma 2.8, Lemma 2.9, Lemma 3.1,
Cor 3.6; EB §§1–2, Lemma 4.1–4.2.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects are numbered
T1, T2, … with severity (FATAL / HIGH / MEDIUM / LOW / COSMETIC).

## Summary table

(filled in at the end)

## Item reviews

### 1. Lemma 1.1 (forced classes are Jacobi non-residues) — SOUND

Re-derived. `gcd(A,4A−1)=1`; `D = sr² | A²` ⟺ `sr | A` (v_p check:
`1+2v_p(r) ≤ 2a_p` ⟺ `v_p(r) ≤ a_p−1` for p | s), so `M ≡ −1 (mod 4s)`.
`(−4D|M) = (−1|M)(s|M) = −(s|M)` (r coprime to M). For odd s:
`(s|M) = (M|s)(−1)^{(s−1)/2·(M−1)/2} = (−1|s)·(−1)^{(s−1)/2} = 1`. For
`s = 2s'`: `8 | M+1` so `(2|M)=1`. Correct, and classical (the Mordell /
Schinzel "squares are never covered" obstruction). Replay:
`twin_jacobi_check.py 20000` → `159390 classes checked, 0 with Jacobi != -1`
(matches the quoted count; script exits 1 on a counterexample).

### 2. Cor 1.2, Lemma 1.3 (QR base) — SOUND

Cor 1.2: `(n|M) = Π(n|p)^e = 1`. Lemma 1.3: (1) every W-smooth M divides
Q₀ and is odd, `c ∈ R_W` is a nonzero QR at each of its primes ⇒ Cor 1.2.
(2) the CRT factor at odd `p^e ∥ Q₀` has `p^{e−1}(p−1)/2` elements;
`Σ_{3≤p≤W} log(2p/(p−1)) = (π(W)−1)log 2 + log log W + O(1)`. (3) for
`1 ≤ e' ≤ e`, a class `a mod p^{e'}` has probability `p^{e−e'}/(p^{e−1}(p−1)/2)
= γ(p)/p^{e'}` or 0. Product structure ⇒ independence. Fine.

### 3. Lemma 2.1 (leak), Lemma 2.2 (inflation) — SOUND

Lemma 2.1: under `Q'` the base is always in R, so a non-avoider satisfies
some `E_C`; (R1) forces `S(C) ≠ ∅`; by (U) every requirement of C except the
one at `ℓ(C)` (exponent 1) is decided before window `j(ℓ(C))`, so the final
residue lies in `F_ℓ(h)`, impossible at a light coordinate. The union bound
gives exactly `Σ_ℓ E[p_ℓ 1{heavy}]`. Lemma 2.2: chain rule over base and
windows; at a light coordinate a class mod `ℓ^e` (`e ≤ E_ℓ`) has conditional
probability `≤ ℓ^{E−e}/(ℓ^E(1−δ_ℓ))`, at a heavy one `ℓ^{−e}`; partial powers at
the base by marginalisation. Correct. (Note: the lemma bounds the law of the
*full* `Q'` history, which is what Lemma 2.4 needs; see T3.)

### 4. Theorem 2.3 (capped sequential sieve limit) — SOUND

Checked the two flagged points line by line.

* *f̃ is λ-level in `x_L`.* `f̃(x_L) = E_U[ν | h, x_L]` by the tower property
  (`σ(h, x_L) ⊆ σ(H_{<j+1})`). Given h the window residues are independent
  under U, so each term `a_i 1[n ≡ b_i (d_i)]` contributes
  `a_i·c_i(h)·Π_{ℓ∈T_i∩L} P_U(n ≡ b_i (ℓ^{e}) | x_ℓ)·Π_{ℓ∈T_i∩H} P_U(n ≡ b_i (ℓ^e))`;
  the heavy factors are constants. So `f̃ = Σ_T f̃_T` with `T ⊆ T_i ∩ L`,
  weight `≤ λ`. Prop 2.4's hypotheses (`p ≤ 1/4`, `p < 1` on the coordinates
  it sees; `f̃/f̃(0) ≥ 0`, value 1 at 0) hold for the light set, which may
  depend on h — harmless, Prop 2.4 is applied fibrewise.
* *Transition.* U given `(h, x_L = 0)`: light residues uniform off `F_ℓ(h)`,
  heavy residues and higher digits uniform and independent — exactly `Q'`.
  `P_U(x_L = 0 | h) ≥ Π(1−δ_ℓ) > 0`, so f̃(0) is defined; no (NDE) needed.
* *Induction in non-log form.* (2.2) is stated as an inequality between
  expectations (not `−log g ≤ E Σ Φ` as in ET Thm 2.7), and holds for every
  history, avoiding or not. Then
  `RHS_j(h) = e^{−Φ_j(h)} E_{Q'}[RHS_{j+1} | h] ≤ e^{−Φ_j(h)} f̃(0) ≤ E f̃ = g_j(h)`.
  The `f̃(0) = 0` case is covered by the same chain. Base case: membership in 𝒜
  is a function of the final history, so `g_{J+1} ≥ 1_𝒜`.
* *Final Jensen.* `E[1_𝒜 e^{−S}] = Q'(𝒜)·E[e^{−S}|𝒜] ≥ Q'(𝒜) exp(−E[S 1_𝒜]/Q'(𝒜))`;
  with `Q'(𝒜) = 1−𝔏 ≥ 1/2` and `S ≥ 0`, `≥ ½ e^{−2E S}`. Correct; (2.1)
  follows with `log 2` and the factor 2. Windows/coordinates above `e^λ`:
  f̃ ignores them (ET Step 0), but heavy ones there still count in 𝔏 —
  consistent with Lemma 2.1 (sum over all ℓ ∈ 𝒫).

The heavy-uniform variant is *necessary* here (not cosmetic): BBMST's
partially distorted heavy fibres (below) would break the identity
"`Q'` transition = U given `x_L = 0`" on which the Prop 2.4 step rests.

**BBMST citation (what is borrowed).** Verified against arXiv:1811.03547
(Balister, Bollobás, Morris, Sahasrabudhe, Tiba, *On the Erdős covering
problem: the density of the uncovered set*, Invent. Math. 228 (2022)
377–414), definition (5) and Theorem 3.1. There, at step i, fibres with
`α_i(x) ≤ δ_i` are fully conditioned, and fibres with `α_i(x) > δ_i` are
*capped* (non-removed points multiplied by `1/(1−δ_i)`, removed points
down-weighted), not left undistorted; Theorem 3.1 bounds the failure mass by
`η = Σ_i min{M_i^{(1)}, M_i^{(2)}/(4δ_i(1−δ_i))}` and gives
`P₀(R) ≥ (1−η) exp(−2/(1−η)·Σ_d ν(d)/d)` with `ν(d) = Π(1−δ_j)^{−1}`. Borrowed:
(a) the threshold idea, (b) the second-moment control of the bad mass
(`M^{(2)}/δ`, here via Markov), (c) the convexity step converting the
distorted measure back to uniform with a factor `2/(1−η)` (here: Jensen
with `Q'(𝒜) ≥ 1/2`), (d) the `(1−δ)^{−1}` inflation weight (here Γ). New
here: combining it with ET Prop 2.4 for general level-λ majorants (BBMST
only bound the uniform density of the uncovered set, i.e. the majorant
`1_𝒜`), and the heavy-*uniform* variant. The distortion method itself
originates with Hough (Ann. Math. 181 (2015)).

**T1 (LOW; §2 intro, AGENT_REPORT "Two new ingredients").** Quote: "The
device is the 'distortion' trick of Balister–Bollobás–Morris–Sahasrabudhe–
Tiba (Erdős covering problem): condition the sequential measure only where
the hit probability is small, and let the remaining (heavy) hits *leak*."
No bibliographic reference, and the description misstates BBMST (heavy
fibres are capped-distorted there, not undistorted). Fix: cite
arXiv:1811.03547 / Invent. Math. 228 (2022), def. (5), Thm 3.1 (and Hough
2015 for the method); state the variant explicitly and why it is needed.

