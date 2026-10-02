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
*full* `Q'` history, which is what Lemma 2.4 needs; see T2.)

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

### 5. Lemma 2.4 (second moment, uniform in W) — SOUND (one precision fix)

Re-derived. `|F_ℓ(h)| ≤ #{active family pairs (q,D)} ≤ N_ℓ(n)`. Pair-of-pairs
expansion: a compatible pair is one class mod `m = lcm(q,q') ≤ ℓ^{2B}`, of
`Q'`-probability `≤ Γ(m)/m ≤ 3^{ω(m)}/m` (Lemma 2.2; γ'(2)=1, γ'(3)=3,
γ'(p) ≤ 5/2 for 5 ≤ p ≤ W, γ'(ℓ) ≤ (1−16^{−1/2})^{−1} = 4/3 above W ≥ 16).
`A_q = (qℓ+1)/4 ≤ ℓ^{1+B}` gives `τ(A_q²) ≪_{ε,B} ℓ^{ε/4}`. Pairs with given
lcm: `Π_p(2e_p+1) = τ(m²)`. Euler product `Π_{p≤ℓ^{2B}}(1+9/p+O(p^{−2}))
≪ (1+2B log ℓ)^9`. Every constant is independent of W, η and the family:
the only W-dependence would have been through Γ, and `Γ ≤ 3^ω` is
universal. This is exactly what the QR base buys (ET's base would put
`L' = e^{O(W^{1+C})}` here). Uniformity: confirmed.

**T2 (LOW; Lemma 2.4 proof).** Quote: "`|F_ℓ(h)|` is at most the number
`N_ℓ(n)` of pairs `(q,D)` with `q ∈ 𝒬_ℓ^{(B)}` …". As written N_ℓ counts *all*
cofactors `q ≤ ℓ^B`, including ones with a prime in ℓ's own window, so
`N_ℓ(n)` is not a function of `H_{<j(ℓ)}` and "`E_{Q'}`" must refer to the
law of the *full* `Q'` history (all windows). The bound is still correct
(Lemma 2.2's chain rule covers every m, and `|F_ℓ(H_{<j})| ≤ N_ℓ(n)`
pointwise), but say so, or restrict N_ℓ to the family's cofactors (all of
whose primes are in `Q₀` or earlier windows). Same remark for Lemma 4.0.

### 6. Corollary 2.5 (leak ≪ W^{−1/4}) — SOUND

`E[p 1{p>δ}] ≤ E[p²]/δ` (on `{p>δ}`, `p ≤ p²/δ`); with `δ_ℓ = ℓ^{−1/2}`,
`ε = 1/4`: `Σ_{ℓ>W} C(1/4,B) ℓ^{−5/4} ≪_B W^{−1/4}`. Uniform in η and the
family because Lemma 2.4 is. Note: the bound covers *all* ℓ > W, including
invisible ones above `e^λ`, as Lemma 2.1 requires.

### 7. Lemma 2.6 (cubic windows via the ET Cor 3.6 transplant) — SOUND

`E Σ_{ℓ∈W_j} p_ℓ ≤ Σ_C ℓ^{−1} Q'(n ≡ −4D (q)) ≤ Σ_{P(M)∈W_j} τ(A²)Γ(q)/M ≤
Σ τ(A²)Γ(M)/M`. `Γ = 1 * h`, h multiplicative on squarefrees with
`h(p) = (p+1)/(p−1) ≤ 2` (3 ≤ p ≤ W), `h(2) = 0`, `h(ℓ) = ℓ^{−1/2}/(1−ℓ^{−1/2})
≤ 2ℓ^{−1/2}` (ℓ > W). Swap sums; `d | M = 4A−1` ⟺ `A ≡ 4^{−1} (d)`, a reduced
class.
* `d ≤ x^{1/2}`: Shiu with `F(A) = τ(A²)` gives `≪ (x/φ(d)) log²x`, and
  `Σ_d h(d)/φ(d) = Π_{p≤W}(1+h(p)/(p−1))·Π_{p>W}(1+O(p^{−3/2})) < ∞`.
* `d > x^{1/2}`: `x^{ε}Σ h(d)(x/d+1) ≤ x^{ε}(x^{7/8}+x^{3/4})Σ h(d)d^{−3/4}`, and
  `Σ h(d) d^{−3/4} = Π_{p≤W}(1+O(p^{−3/4}))·Π_{p>W}(1+2p^{−5/4}) < ∞`.

So `Σ_{M≤x} τ(A²)Γ(M) ≪_W x log²x`; partial summation over
`e^{s_j} < M ≤ e^{(1+B)s_{j+1}}`, `s_{j+1} ≤ 2s_j`, gives `K((1+B)s_j)³`.
The transplant is legitimate: ET's proof uses only those two convergent
sums, never `h(p) ≤ 1/(p−1)` at small p. The W-dependence of K is through
`Π_{p≤W}`, i.e. `K(W,B) ≤ exp(O(W^{1/4}))` in the tail and `O(log W)` in
the main term — finite, as claimed. Also covers twin/prime-power M = qℓ^v
(Prop 4.1, Thm 4.4), since only `P(M) ∈ range` and `Γ(q) ≤ Γ(M)` are used.

### 8. Theorem 2.7 (unconditional gapped cap) — SOUND

Theorem 2.3 applies (Cor 2.5: `𝔏 ≤ 1/2` at `W = W₀(B)`). R-term
`log(Q₀/|R_W|) ≤ π(W₀(B))·log 3 = O_B(1)`. The light profile is bounded by
the full one (Lemma 2.6), which is EB's H_light(ii) with `K = K(W₀(B),B)`;
H_light(i) (NDE) and (iii) (heavy charge) are not needed because (2.1) has no
heavy term. EB Thm 2.5's window sum (G = 1 per window by EB Lemma 2.5a since
η < 1; `≤ 1+2log λ/η` windows; crossover `s* = (19λ/(C₄K(1+B)³))^{1/4}`;
total `≤ 380λ/(ηs*)`) then gives `C K^{1/4}(1+B)^{3/4}η^{−1}λ^{3/4} +
O(η^{−1}log λ(log λ+log K))`; doubled by (2.1), plus `log 2 + O_B(1)`. I
re-checked EB's above-crossover sum (`Σ_k(1+η)^{−k}(1+4(k+1)log(1+η)) ≤
(1+η)/η + 4(1+η)²/η`). Family: EB's η-gapped requires `P(M) > w₀`, and here
`w₀ = W = W₀(B)`, with cofactor primes ≤ W in Q₀ (EB Lemma 2.1) — consistent.
Majorants of the true avoider set `𝒜(𝔊)` are majorants of the R_W-restricted
set, so the cap applies to them. Level convention: EB charges primes
`> w₀`; here primes ≤ W are free, which is more generous to ν, so the cap
transfers.

"ET Cor 3.6 is recovered for ℛ(M)-classes": correct with `B = C`, η ≤
min(η₀, 1/C−1) (EB Lemma 2.1 scope); (a,D)-classes are not recovered, as
the text says.

