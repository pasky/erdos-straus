<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review. The author is a GPT-6.2 Astra lane. Re-derive every stationary-phase step, range condition, exponent-pair application and rational exponent optimisation of notes/z80/R_BELOW_619.md; check cited theorems against their published hypotheses. In particular try to falsify the centered level-one upper-sieve transfer with split prime sets and its z79 Haar hypotheses; audit Type I/II/R constants, BM density and Dirichlet approximation for the large-M bound. Check F1-F4, replay and scopes. Return your full verbatim findings with verdicts for each theorem. Please use no writes; run Python only under ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B. Note no fixed-4 exponent record is claimed.

Commit log:
commit f2c0476308d36df42fbbdcee5e9619d368bde6ea
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:11:30 2026 +0100

    Transfer centered word moments with an upper sieve; gain for large numerators

 data/z80/r_below_619.txt   |  17 +++++++
 notes/z80/R_BELOW_619.md   | 109 +++++++++++++++++++++++++++++++++++++++++++++
 scripts/z80_r_below_619.py |  96 +++++++++++++++++++++++++++++++++++++++
 3 files changed, 222 insertions(+)

Review:
No substantive errors found. Every theorem in `notes/z80/R_BELOW_619.md` survives my hostile re-derivation, and the replay reproduces the recorded output exactly. What needs fixing is mostly form: §0 and the STATUS delta, priority citations, and the §1 label and wording. No fixed-4 exponent record is claimed, and none follows.

## Verdicts by theorem

**§1 — exact off-diagonal formula (1): ACCEPT.**
- Expanding the square in z79 (10) and combining Σ_c Σ_{j≡c} gives the full j-lattice. The Fejér density periodises to Σ_{|m|<H}(1−|m|/H)e(±mt).
- The prefactor W²/(TQ) equals W/J because T=WJ/Q. With t=Jy and √(C/J)=W, the identity f_a(Jy)=aW·2/(√(y+aQ/J)+√y) is exact.

**§1 — coherent stationary-lift lower bound (2): ACCEPT as a scoped lower bound on the absolute majorant only.**
- The stationary condition aW·g′(y)=mJ gives m<0 with |m|≍cH<H/2, and about aW/J such integers m.
- The phase's second derivative is ≍aW, so each integral is ≍J/√(aW) with error J(aW)^{−3/2}. This needs aW≍cHJ→∞, which holds. Hörmander I Thm 7.7.5 applies, with uniformity over the compact family as in 7.7.6.
- Summing over m and a gives (W/J)·A·√(AW)=H^{3/2}J^{1/2}.
- At the vertex, J=n^{1+r−2t}, which matches z79 (exponent 8r at t=6/19). The cost exponent is (1+7r−4t)/2=(8−25t)/2, which is 1/19 at t=6/19 and zero at 8/25.
- The example n=4P^19 checks out: J=c′P^8, A=P^4, aQ/J=P^{−2}, HQ/W=P^{−2}, T=P^12 and J/Q=P^6.
- Caveats:
  - **(a)** The amplitude lower bound |b|≫1 depends on z78 §7 and is not re-derived in the note.
  - **(b)** The statement "needs t≥8/25" carries the 6/19-vertex scalings (H, Q, |ℓ| as powers of r) to other values of t. That is an Assessment, not PROVED.
  - **(c)** The note should say plainly that 8/25 is above the current record 6801/21497≈0.31637. So absolute lifts through (10)/(11) cannot even recover the existing exponent. That makes this a METHOD-CX/NULL, at most one FRONTIER §6 line, not a barrier near 6/19.

**§2 — R_M(n)≪n^ε(1+D^{1/2}M^{−1/6}) (3): ACCEPT (elementary).**
- The block costs min(U, W, 1+B) are correct: fix a using τ(n+a); fix d using (Mad−1)(Mbd−1)=Mdn+1; fix the sum a+b, which runs over a class mod M.
- For M≤D, the inequality t₀≥D^{1/3} reduces the claim to z79 (12).
- The exact equation N+v=ad(Mv−n₀−a) holds (I also checked it on 20,000 random cases).
- The identity ad(qv−g)−qN/M = qv/M + ad(qn₀/M−g) + qa²d/M gives the width K/S+S(KU+B)/M. Here q and g are fixed for the whole block, which is the key point.
- S≫1 follows from U≪D, B≪D and M>D. The width bound D^{3/2}/(t₀²√M)≤t₀ is equivalent to t₀≥D^{1/2}M^{−1/6}. Positivity and polynomial size for the τ₃ bound hold.
- The new bound beats D^{1/3} exactly when M>n^{1/3}, and is O(n^ε) for M≥n^{3/7}. It gives no gain at M=4.

**§3 — level-one upper transfer (5): ACCEPT.**
- S(n)≥0 (an even Bonferroni truncation), G(n)≥0, and S·G=1 on primes in (X,2X].
- I tried to break the claim that the averages factorise across the split prime sets, and could not. e is z-smooth and [d,d′] is z-rough, so they are coprime. On a reduced class, classes sharing a prime with l contribute exactly zero.
- The Bonferroni tail (log log L)^{k+1}/(k+1)! with k≍log L decays faster than any power of L. The number of e's is exp(O((log L)²))=X^{o(1)}.
- The Selberg pieces are standard and correct: |λ_d|≤1, and the Mertens/Markov lower bound for the denominator (expected log h=Σlog p/p≤2c₀ log T). This gives G≪log z/(δL), so P_zG≪1/(δL).
- The error from deleting primes of l is O(L^4/z). Rounding costs Σ|c_i|T²X^{o(1)}≤X^{1−3δ/4+o(1)}.
- An attempted falsification with an adversarial single class reduces to Brun–Titchmarsh and is consistent with (5).
- **Priority (must add):** this is Ramaré's enveloping-sieve principle (Ramaré 1995; Ramaré–Ruzsa 2001; Green–Tao 2006, *Restriction theory of the Selberg sieve*). Only its use here is new.
- Remark: combined with Cauchy–Schwarz it also gives E_p Z=m+O(L^{s/2}). That is consistent, since θ<1/2 is inside the BV range.

**§4 — (6), R≥(9/(8π²)−ε)log²p and f_II≥(1/(112ζ(3))−ε)log³p: ACCEPT.**
- I re-checked the z79 Haar inputs for any use of θ beyond a polynomial bound on the modulus. The A′/§2 completion, the determinant cut k/V≪QX^ε/D (and QX^ε/(AC) when the determinant vanishes), the E error exponents, and the §11 conic bad-row count A′LX^{5(δ+2w)}/(AB) all depend only on γ, g, σ, ε and w. None uses θ.
- The conditions (4) hold: X^{2θ+o(1)} cells, and Σ|c|/φ=⟨(Z+|m|)²⟩_*=O(L^{2s}).
- Chart disjointness is verified:
  - (4ad−1)(4bd−1)=4dp+1
  - (4acd−1)(4bcd−1)=4c²dp+1
  - 4ab(4aC−1)=4a(p+a)
- Constants check out: K₂=12/π², K₃=6/(7ζ(3)). This gives 2(K₂/4)/8+(3/π²)/8=9/(8π²) and K₃/96=1/(112ζ(3)). The total over all four regions is 3/(2π²)=M₀, consistent with the "three quarters" claim.
- Numerically, over 120 primes near 2·10^5 the three charts never overlapped and covered 0.65 of R(p), which is plausible convergence toward 3/4.
- Minor gap: z79 A′ only extends **A's** conclusion to unions of cubes. Extending **E's** weighted variance to A′ cubes is asserted, not stated in z79. It is true by the same exponents, but needs one explicit sentence.

**§4 — Type I, 2C_I(25/(26v))³: ACCEPT.**
- There are Y^{26/25+o(1)} atoms. The v-fold lcm is at most 4^vX^{(26/25)vλ}<X. The Haar mass is O(L^{3v}). Markov gives O(L^{−3m}) exceptions.
- The factor 2 from the two orientations, the doubled λ endpoint and the eightfold gain in the coefficient are all correct. K.1's witness-prime BV/BT input is unchanged.

**§5 — |M_BM−M₀|≪(log log p)² outside O(π/log^A): ACCEPT.**
- The Burgess r=2 hypotheses are correct for prime modulus and give a tail of X^{−1/80+ε}.
- For ij not a square, the Jacobi character is non-principal with period dividing 8ij, which gives the U²/X term. The square case gives log Y/Y. Restricting to primes costs a factor L. |E(χ)|≤36/π².
- This is standard; cite the literature on the distribution of L(1,χ_d) (e.g. Elliott, Montgomery–Vaughan, Granville–Soundararajan).

## Form and scope issues
1. **§0:** the Result line omits the Type I constant and §5. Its Label omits K.1's BV/BT (needed for Type I) and Burgess/BM_LVALUE (for §5).
2. **STATUS delta:** it is written as instructions, not replacement row text. It must change the §1A label from "PROVED rel. BV" to "PROVED rel. PNT/Mertens (upper sieve) + z79 Haar". BV is no longer needed for the R or f_II coefficients; Type I still uses BV/BT through K.1. It should also cite the enveloping-sieve priority.
3. **Notation:** L means the Poisson length in §1 and log X in §3–5.
4. **Triage:** §1 should be METHOD-CX/NULL rather than BARRIER-SCOPED, per point (c) above.
5. **Replay:** `scripts/z80_r_below_619.py` reproduces `data/z80/r_below_619.txt` byte-for-byte from both the repo root and `scripts/`.
   - `all_counts` matches brute force for all n≤600 and M∈{1,4,8,37}.
   - F1, F3 and F4 pass. F2's 1,590,284,203,561 control is inherited from `notes/z76/DISPROOF_COMP.md`, not replayed, and is correctly labelled as such.
   - The R_M ratio lines are finite observations, not tests of (3).
6. **Pipeline:** no master files were touched, which is correct for a lane. "Review: none (cross-review owed)" is accurate.

**Overall:** this can be promoted after fixes 1–4 and a second cross-lab review. The headline gain (×4 for R, ×8 for f_II, and dropping BV from those transfers) is real.
</code-review>
