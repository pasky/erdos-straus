# AGENT REPORT O48 (branch side-agent/beyond-fifth): checkpoint 1

Deliverable: `POINTWISE_OMEGA13.md`, `scripts/omega13_{inflation,v2,jacobi}.py`, `data/omega13/`.
The branch also merges `side-agent/haar-exponent`, to read POINTWISE_HAAR.

## Headline

1. **Haar exponent 3 (Thm 3.4, PROVED modulo Nair–Tenenbaum).**
   `log(1/δ*(T)) ≪ 𝓛³(log𝓛)^{O(1)}`.
   * With POINTWISE_HAAR Thm 2.1 (`≫𝓛³/log𝓛`) this gives `a=3`.
   * It settles POINTWISE_HAAR Conj 3.1 up to logs.
   * It improves O12's `𝓛^5log𝓛` by about `𝓛²`, and is sharper than the brief's item (iii).
2. **Prime exponent 1/4 (Cor 3.5, CONDITIONAL on three interface checks I1–I3).**
   `W(p)≥exp(c(log p)^{1/4}(loglog p)^{−B})` for infinitely many Mordell-hard p,
   modulo (G), NT and OMEGA10 Thm 3.4.
   * The quarantine now costs only `𝓛³ polylog`.
   * The junta `𝓛·S` is the sole bottleneck. A junta `≪S·polylog` would give 1/3
     conditionally.

## The three new ingredients

* **β-weighted local lemma (Lemma 1.1, PROVED, 10 lines).**
  * *Statement.* Put `x_E=β^{|supp E|}P(E)`. Then the criterion is a *constant*
    per-coordinate threshold, `Σ_{E∋ℓ}x_E≤(3/4)logβ`.
  * *What it removes.* O11 needed log-weighted thresholds `c(a+1)logℓ/𝓛`, which
    cost a factor 𝓛 per unit of mass. With `β=1+1/log𝓛` the reweighting is O(1).
* **Event classes are Jacobi non-residues (Lemma 3.1, PROVED).**
  * *Statement.* `(−4D | M)=−1`, and `(−4D|ℓ)=(−d|ℓ)` with d the squarefree part
    of D. Checked on 2.4M atoms.
  * *Consequence.* Quarantining to *random square classes* never fires a
    deterministic event, which is the generalisation of Mordell-hardness.
  * *Why it matters.* The class of one, which caused the `τ(4a²d+1)` inflation
    `𝓛³→𝓛^4` diagnosed in the O46 report, is no longer needed.
* **Martingale bookkeeping (Lemma 3.2, PROVED).**
  * *Supermartingales.* The masses `Σp_i(E)2^{u_i(E)}φ(E)` are supermartingales.
    The factor `2^{u}` pays for the square-restriction drift `(1+(−d|ℓ))`.
  * *Cost and mass.* Optional stopping gives the cost and residual-mass bounds in
    terms of Haar masses `1/φ(M)`, with no g in them.
  * *Late primes.* A pair potential `p p'·R` (R uses the agreement depth) bounds
    `E[w̃_ℓ(end)²]` by a deterministic pair sum `B_2(ℓ)`.
  * *Lemma 3.3(B).* `Σ_{ℓ>Y}B_2(ℓ)≤(𝓛+1)Ξ/Y`, by Cauchy–Schwarz plus regrouping
    `N=eℓk`. This is elementary, with no progressions. So primes `>Y=𝓛^{O(1)}` are
    never heavy (Chebyshev).
  * *Lemma 3.3(A).* The first-moment Haar sums are `≪𝓛³polylog` by Nair–Tenenbaum
    (`Q_1=n`, `Q_2=4n−1`). Henriot arXiv:1102.1643 (1.1) is quoted.

The pointwise "first-term" obstruction of O11 §4 and O12 is bypassed. Class-of-one
masses at large ℓ need pointwise ET-in-progressions bounds. Random-class masses
need only a second moment *summed over ℓ*. §2 records this explicitly, with
EVIDENCE: the pointwise ratio `ℓV♯(ℓ)/S♯` grows (6.4→9.8), while the second moment
stays below the heuristic.

## Attack points for review

* **Lemma 3.2(a)/(d), the a=0 square step.** Check
  `E[p_new]=(1+(−d_E|ℓ))p` and the pair potential with agreement depth. The R1 fix
  is already applied: ρ uses depth j, not `min(v,v')`. Optional stopping uses
  stopping times bounded by the number of steps.
* **Lemma 3.3(A).** NT hypotheses:
  * class `M_2(A,B,ε)` uniformly in T (β≤2);
  * `Q=n(4n−1)` has no fixed prime divisor;
  * the `(log x)^{β−1}≤e` bookkeeping;
  * the cost weight `logM_Y≤3logY(3/2)^{Ω_Y}`.
* **Lemma 3.3(B).** The divisibility `gcd(M,M')/ℓ^{min v} | gcd(M/ℓ,M'/ℓ)`, the
  regrouping, and the elementary Euler-product bound for Ξ.
* **Thm 3.4.** The Markov/Chebyshev union and the fibre `n≡r (Q)` with Lemma 1.1.
  `P(n≡r)=1/φ(Q)`.
* **Cor 3.5, I1–I3.** These are interface checks of O8 BRW/twist, O11 Cor 1.2 and
  O11 Lemma 3.1, all written for `x_E=2P(E)` and the class of one. Note that
  `η≍1/log𝓛<1/32`, so neighbourhood sums are smaller than before.

## Not done / next

* I1–I3, which upgrade Cor 3.5 to "PROVED modulo (G), NT, OMEGA10".
* A junta below `𝓛·S` (brief item (ii)), towards 1/3.
* §1–§2 (the class-of-one route, LPL, V2) are superseded by §3. They are kept as
  diagnosis.

Ledger and STATUS were not edited. No self-review subagent was run, so the
parent's hostile review is the first independent check.

## Checkpoint 2 (after hostile reviews R48a, R48b; both branches merged)

No FATAL findings. All repairs are applied in separate commits:

* *Lemma 1.1.* It now has the conditional bound for events outside the family, and the
  prime-side twist needs `η≤0.19` (D5). The proof of Lemma 3.2(d) has its wording fixed
  (`N·1[match]`; agreement-depth remark, m1/m2).
* *Lemma 3.3(A).* The cost weight is now `log M_Y≤logY·τ(M_Y)`, since `(3/2)^{Ω_Y}` violated
  the Nair–Tenenbaum class (D1). The bookkeeping is `(logY)^β` (D3), with explicit `C_0`.
  Ξ is uniform in Y (m5).
* *The process.* It starts with forced square steps at 3, 5 and 7, so `840|Q` and
  `r≡1 (24)` (m4/D4).
* *Theorem 3.4.* It is stated in POINTWISE_HAAR's normalisation `n≡1 (24)`, which differs
  from the `Ẑ^×` version by a factor 2 (m3/D2). The bound is explicit:
  `log(1/δ*)≪𝓛³(log𝓛)^5`. It needs NT only, not ET (D6).
* *§2 EVIDENCE.* The wording is fixed (D7).

**New §5: I1–I3 written out**, following the reviewers' sketches.
* **I1(a) BRW/EL.** `S_res` replaces S in τ, and `δ≥e^{−(4/3)S_res}`.
* **I1(b) Twist.** `|E[Fψ]|≤β^{−1}w̃_{ℓ_0}EF'≤ηEF'`, so `|μ_ψ|≤μ/4` for `η≤0.19`.
* **I2 Junta.** The digit filtration only needs uniform digits above the fibre level.
* **I3 Coset transfer.** Real characters equal 1 at the square r. Property (I) uses Lemma 3.1.

**Theorem 5.1 (PROVED modulo (G), NT, OMEGA10 Thm 3.4; Elsholtz–Tao no longer used).**
`W(p)≥exp(c(log p)^{1/4}(log log p)^{−1/4})` for infinitely many Mordell-hard p, and
`log L_h(T)≪𝓛^4log𝓛`. This supersedes O12 Thm 6.3 (exponent 1/5).

*Suggested review focus for §5:*
* I1(b): Lemma 1.1's conditional bound is applied to the subfamily avoiding `ℓ_0`, and
  `EF≥(1−η)EF'`.
* I3 Case A with `χ̄(r)`.
* I2's claim that the class enters nowhere in O11 Lemma 1.1.

*Next (if continued).* A junta `≪S_res·polylog` (brief item (ii)) would give exponent 1/3
on the prime side, matching the Haar exponent.
