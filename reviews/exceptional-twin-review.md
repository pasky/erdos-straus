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

### 9. §2.4 numerics (EVIDENCE) — SOUND-AFTER-REPAIRS (labels/wording)

Replays run here (all ≤ 8 GB, ≤ 3 min each):
* `twin_capped.py 100000 100 300 0.2 all cap` — byte-identical to
  `data/twin/capped_X1e5_W300_k0.2_cap.txt` (leak 0, no heavy coordinate).
* `… 100 0.2 all cap` — identical to the W = 100 file (0.6410 / 46%).
* `… 30 0.2` — identical except the header line (the saved file predates
  the `cap1/4=` header field).
* `… 30 0.5` (not saved by the author) — expected leak 25.4674, realised
  100%: confirms the "25.5" quoted.
Table values (0.056/4%, 0.070/5%, 5.67/100%, bands 31–255 and 32–127) match
the data files. The script correctly forbids the full lifted class
`c mod ℓ^v` inside `ℤ/ℓ^{E}`, samples the QR base, and asserts Lemma 1.3(1).

**T3 (LOW; §2.4 "Theorem-compatible caps", §0 row, AGENT_REPORT
"EVIDENCE").** Quote: "Theorem-compatible caps `δ_p = min(1/4, p^{−0.2})`".
§2.3 fixes `δ_ℓ = ℓ^{−1/2}`, and Cor 2.5 / Lemma 2.6 are proved only for that
choice. The extension to `δ_ℓ = min(1/4, ℓ^{−κ})`, κ ∈ (0,1), is asserted
only inside the numerics bullets ("Lemma 2.6 needs `Σ p^{−1−κ/2} < ∞`,
Cor 2.5 needs `Σ ℓ^{κ−2+ε} < ∞`"). It is true (Lemma 2.6: take the
large-divisor exponent `−1+κ/2` as in ET Cor 3.6; Cor 2.5: Markov with
`δ = ℓ^{−κ}`; γ' ≤ 4/3 still holds because δ ≤ 1/4), but it should be a
stated remark after Cor 2.5, with W₀ = W₀(B,κ). Without it, "theorem-
compatible" overstates.

**T4 (LOW; §2.4 "So at X = 10⁵ the theorem's hypothesis 𝔏 ≤ 1/2 already
holds with W = 300, for the full system including twin classes").** The
numerics have unbounded B (all M ≤ X, so `B` up to `log X/log W − 1`), while
W₀ is a function of fixed B; and at W = 300, X = 10⁵ every cofactor is
`< 334`, so the system is very sparse. The run shows the leak hypothesis is
*attainable* at toy scale; it does not test whether W₀ must grow with X
(EB review D13's concern, which the proof answers only for fixed B). Say
so. Also cosmetic: the bullet "The theorem-compatible runs … are in the
table below" sits *below* that table; and the κ = 0.5 run should be saved
(`data/twin/capped_X1e5_W30_k0.5.txt`) since it is quoted.

### 10. Lemma 3.1 (u-form) and Lemma 3.2 (sign constraint) — SOUND

Lemma 3.1 from EB Lemma 4.1: `A_q = srk`, `4srk = qℓ+1`; mod ℓ `r ≡ (4sk)^{−1}`,
value `−r/k ≡ −(4sk²)^{−1}`; mod q, `4sk(nk+r) ≡ 4sk²n+1`, 4sk a unit. The
statement omits "s squarefree"; harmless: for non-squarefree s the triple
corresponds to `D = s'(tr)²` with the same u and the same value, so the *set*
is unchanged. Second form: `q | 4un+1` ⟺ `q | u − N` for `(n,q) = 1`; the
congruence `q ≡ −ℓ^{−1} (4sk)` presupposes `(ℓ,4sk) = 1`, which follows from
`4sk | qℓ+1`. Lemma 3.2: Lemma 1.1 at `M = qℓ`, `(ℓ,q)=1`:
`(n|q)(v|ℓ) = (−4D|q)(−4D|ℓ) = −1`; `v ≢ 0` since `gcd(D,M)=1`. Correct.
(For prime-power tops `qℓ^v`, v odd gives the same sign at ℓ; v even gives
`(n|q) = −1` for every active q — not claimed, fine.)

Heuristic 3.3 is correctly labelled HEURISTIC; (E_δ) OPEN. Not graded.

### 11. §4.1 interface and Lemma 4.0 (prime-power second moment) — SOUND

The prime-power transition (full-fibre conditioning on `ℤ/ℓ^{E_ℓ}`) keeps
Lemma 2.1 (a decided condition forbids its lifted class, impossible at a
light coordinate) and Lemma 2.2 (class mod `ℓ^e`: `≤ (1−δ)^{−1}ℓ^{−e}`).
Lemma 4.0: for `M = qℓ^v` activation is `n ≡ −4D (q)`, a history event; it
forbids one class mod `ℓ^v` (density `ℓ^{−v}` in `ℤ/ℓ^{E}`), so
`p_ℓ ≤ Σ_v ℓ^{−v}N_{ℓ,v}`; Lemma 2.4's argument bounds `E N_{ℓ,v}²` (uses only
`q ≤ ℓ^B`, `A ≤ ℓ^{1+B}`, Lemma 2.2); Minkowski over `≤ 1+B` values of v.
Correct, for any processing order in which every cofactor prime precedes ℓ
(true for singletons, resolved η-windows and the in-window order of V). The
bound `r < (1+B)(1+η)` and the `101·103·109` example (≡ 3 mod 4; 101, 103,
109 all in `(e^{4.252}, e^{5.315}] = (70, 203]` for η = 1/4, W = 30) check.
T2 applies here too.

### 12. Proposition 4.1 (low range, singleton windows) — SOUND

At a singleton window f̃ depends on one bit; `E f̃ ≥ (1−p)f̃(0)`, and f̃(0) is
the `Q'` transition, so the step of Thm 2.3 holds with
`Φ = −log(1−p) ≤ (4/3)p` (p ≤ 1/4); heavy ⇒ leak. Profile: Lemma 2.2 + the
Lemma 2.6 sum over `M ≤ e^{(1+B)s₁}` (twin and prime-power M included, via
`Γ(q) ≤ Γ(M)`). Cost `2·(4/3)·K'((1+B)λ^{1/4})³`. Correct; no λ-level
property is needed, so the shape of M is irrelevant.

### 13. Lemma 4.2 and Corollary 4.3 (top range) — SOUND

Lemma 4.2 re-derived: `E_σ g_ℓ = E_U[g_ℓ(r−1)] ≤ ε_ℓ E_U g_ℓ⁺ + m_ℓ δ_ℓ ≤
m_ℓ(ε_ℓ+δ_ℓ)` and `Σ m_ℓ ≤ c₀` because f ≥ 0 at the product point where every
`g_ℓ` is minimal (needs f ≥ 0 on the *whole* product — given, ν ≥ 0 on ℤ).
Only one-coordinate marginals of σ enter, so σ may be any coupling.

Cor 4.3 (the flagged use on residues): `log ℓ > λ/2` on V, so each term of ν
meets at most one V-prime; `f(y_V) = E_U[ν | h, y_V]` is `c₀ + Σ g_ℓ(y_ℓ)` on
the residues `y_ℓ = n mod ℓ^{E_ℓ}` (higher powers in ν's moduli are
integrated out), `f ≥ 0`, `E_U f = g_V(h)`. σ = in-window sequential capped
law: each marginal is a mixture of uniform laws on sets of density `≥ 1−δ_ℓ`
(light) or uniform (heavy), so `ε_ℓ ≤ δ_ℓ/(1−δ_ℓ) ≤ 2δ_ℓ`, TV defect `≤ δ_ℓ`
(convexity), `δ_ℓ ≤ e^{−λ/4}`. `E_σ f = E_{Q'}[g_next | h]`, so the step holds
with `Φ = log(1+3e^{−λ/4})`, independent of the window's mass. Twin/prime-
power conditions inside V are decided at their top prime in the in-window
order, so the leak bookkeeping (Lemma 2.1 with sub-steps) and Lemma 4.0
apply. The remark after Lemma 4.2 (Λ² with two V-primes per term defeats
any `1+O(max p)` bound) is correct in substance; "level 2" there means
"two primes per factor" — reword (cosmetic). Notation clash: δ_ℓ is both
the cap and Lemma 4.2's TV parameter (cosmetic).

### 14. Theorem 4.4 — SOUND-AFTER-REPAIRS (presentation)

Mathematics checked: windows = singletons on `(W, e^{λ^{1/4}}]`, EB η-windows
cut to `(e^{λ^{1/4}}, e^{λ/2}]` (cutting refines windows, and refinement
preserves "resolved": the top prime stays alone in its sub-window), V, then
singletons above `e^λ` (invisible). Middle cost: Lemma 2.6 + EB Thm 2.5
computation from `s = λ^{1/4}` gives `≪ η^{−1}λ^{3/4}(1+log(K(1+B)³))`; low
range `≪_B λ^{3/4}`; V: `O(e^{−λ/4})`. Leak via Lemma 4.0 + Cor 2.5.
`λ ≥ (2log W)^4` gives `λ^{1/4} > log W` and `λ/2 > log W`. Conclusion holds.

**T5 (MEDIUM; Thm 4.4 proof, "Theorem 2.3 applies: its induction step in
each window is, respectively, the singleton inequality, ET Prop 2.4,
Lemma 4.2").** Theorem 2.3 is stated in the setting of §2.1 — all
conditions satisfy (U) for the window partition, and the step is ET
Prop 2.4 on hit indicators. Neither holds for V: conditions with two
V-primes violate (U) for V, the V-transition is not a product law, and the
step is an inequality `E_U f ≥ E_σ f/(1+…)` on residues, not
`E f̃ ≥ f̃(0)e^{−Φ}`. Lemma 2.1 likewise assumes (U). The extension is routine
(the proof of Thm 2.3 only uses: a transition law σ_j(h), an inequality
`g_j(h) ≥ e^{−Φ_j(h)} E_{σ_j(h)}[g_{j+1}]`, and a leak lemma for whatever
order decides each condition), but the headline theorem currently cites a
theorem outside its hypotheses. Fix: state "Theorem 2.3′ (abstract
sequential step)" with those three inputs, and Lemma 2.1′ for in-window
sequential orders; then Prop 4.1, Cor 4.3 and the middle windows are
instances.

**T6 (LOW; Thm 4.4 "Fix B and W = W₀(B)").** W₀(B) was defined in Cor 2.5
from Lemma 2.4's constant; Lemma 4.0's constant is larger by `(2+B)²`, so
W₀(B) must be re-chosen (or defined in Cor 2.5 with Lemma 4.0's constant).
Trivial, but the theorem as written uses the wrong W₀.

### 15. §4.4 residual, §4.5 Conjecture 4.5_r and routes — labels SOUND

Conj 4.5_r is labelled OPEN and routes 1–4 HEURISTIC; route 5 is Lemma 4.2.
The sufficiency claim ("4.5_r for `r = ⌊(1+B)(1+η)⌋` would remove the
residual") is plausible given T5's abstract step: the conjecture is of the
right form `E_U f ≥ e^{−Φ}E_σ f`, the k-ary densities `π_T(h)` have
`Q'`-means bounded by Lemma 2.2, and the leak is covered by Lemma 4.0 for
the in-window order. Not graded further. Minor: the conjecture's hypothesis
"unary forbidden sets with `p_ℓ ≤ 1/4`" should say whether activated k-ary
classes count towards the cap (σ is "capped", so heavy ℓ are possible).
The `101·103·109` argument that 4.5_2 alone is insufficient is correct.

### 16. §5 (global) and AGENT_REPORT_O1 — SOUND-AFTER-REPAIRS (scope wording)

The report's labels, numbers and repairs list match the document at
b708bd1; "Where a hostile reviewer should look first" is accurate and all
four points check out (items 4, 5, 7, 13).

**T7 (LOW; §5 "Proved here", report "Global").** The family hypothesis of
Thm 4.4 depends on λ (resolvedness is required only for top primes in
`(e^{λ^{1/4}}, e^{λ/2}]`), while the ET Lemma 2.9 conversion produces
`λ = Λ₀ + log T + log(1/Eν)`, which depends on ν. The θ-statement is correct
if the hypothesis is required for all `λ ∈ [Λ₀, (A+1)L + S]`, or for the
families named in the bullets (all gapped; all moduli with top prime
`≤ e^{λ^{1/4}}` or `> e^{λ/2}`) read with that λ-range. Say which.

**T8 (LOW; §5 "Not covered" 3).** Quote: "(a,D)-classes and Case-A classes:
… For these, ET Cor 3.6 still covers the dominant part." A family mixing
balanced ℛ(M) classes (Thm 2.7/4.4) with dominant (a,D)-classes (ET
Cor 3.6) is covered by *neither* theorem — caps do not add over unions of
families (the avoider set is the intersection). State that the two results
cover their families separately.

**S1 (suggestion, not a defect).** The ℛ(M)-only restriction of the QR base
is likely removable cheaply. Use the *square base*: `n mod p^e` a unit square
for every `p^e ∥ Q₀`, including `p = 2` (inflation `γ(2) = 8`). A class mod G
that contains no integer square has, by CRT, some `p^e ∥ G` at which its
residue is a non-square, so the square base avoids it. Lemma 1.1 is the case
of ℛ(M). For (a,D)-classes I checked numerically here (`a ≤ 40`, `D ≤ 300`,
12,000 classes `−(4D+a) mod 4a·g(D)`): none contains a square mod G, as
expected from the Mordell / Elsholtz–Tao obstruction. Case-A was not
checked. This removes only the base obstruction. Lemma 2.4 and the gapped
structure for (a,D)-moduli still have to be done.

## Summary table

| item | statement | verdict | defects |
|---|---|---|---|
| 1 | Lemma 1.1 | SOUND | — |
| 2 | Cor 1.2, Lemma 1.3 | SOUND | — |
| 3 | Lemma 2.1, 2.2 | SOUND | (T2) |
| 4 | Thm 2.3 + BBMST attribution | SOUND | T1 (LOW) |
| 5 | Lemma 2.4 | SOUND | T2 (LOW) |
| 6 | Cor 2.5 | SOUND | — |
| 7 | Lemma 2.6 | SOUND | — |
| 8 | Thm 2.7 | SOUND | — |
| 9 | §2.4 numerics (EVIDENCE) | SOUND-AFTER-REPAIRS | T3, T4 (LOW) |
| 10 | Lemma 3.1, 3.2 | SOUND | — |
| 11 | §4.1, Lemma 4.0 | SOUND | (T2) |
| 12 | Prop 4.1 | SOUND | — |
| 13 | Lemma 4.2, Cor 4.3 | SOUND | cosmetic |
| 14 | Thm 4.4 | SOUND-AFTER-REPAIRS | T5 (MEDIUM), T6 (LOW) |
| 15 | §4.4–4.5 labels | SOUND | — |
| 16 | §5, report | SOUND-AFTER-REPAIRS | T7, T8 (LOW); S1 |

**Overall.** No FATAL or HIGH defect. The core claim stands: the capped
measure with the QR base makes the (η,B)-gapped door unconditional for each
fixed B (Thm 2.7). The flagged points (Thm 2.3 λ-level after averaging heavy
indicators; final Jensen with `Q'(𝒜) ≥ 1/2`; Lemma 2.4 uniformity in W;
Lemma 2.6 transplant; Cor 4.3 on residues) all check. The one MEDIUM item
(T5) is presentation: Thm 4.4 cites Thm 2.3 outside its stated hypotheses,
and needs an abstract sequential-step version. The status labels in §0 can
stay PROVED once T5 and T6 are repaired.

Replays run: `twin_jacobi_check.py 20000` (0 counterexamples, 159,390
classes); `twin_capped.py` at (X, W, κ) = (10⁵, 300, 0.2 cap), (10⁵, 100,
0.2 cap), (10⁵, 30, 0.2), (10⁵, 30, 0.5), all matching the saved data or
the quoted value. (a,D) square check for S1: an ad-hoc 10-line sympy loop,
not committed.
