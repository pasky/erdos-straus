# AGENT REPORT O47 — `paper/es-subexp-note.tex` v3 (exponent 1/5)

Branch `side-agent/subexp-paper-v3`. Status: **checkpoint 1 — complete draft, compiles
(pdflatex, 27 pp, no undefined refs, one 1.6pt overfull box); not yet refereed.**
`POINTWISE_HAAR.md` was not on main when I finished, so no remark on the lower bound
`log(1/δ*) ≫ 𝓛³/log 𝓛` is included.

## Main results of v3 (labels as in the paper)

* Thm 1.1 (Proved mod Gallagher [Thm 4.2 + Landau–Page 4.1] and Elsholtz–Tao Thm 3.1 =
  ET Prop 1.4, Thm 7.1, Cor 7.4, (7.10)): `W(p) ≥ exp(c(log p)^{1/5}(log log p)^{−1/5})`
  i.o.; the least hard p with `W(p)>T` has `log p ≪ 𝓛^5 log 𝓛`.
* Thm 1.2 (Proved mod Gallagher **only**; Håstad no longer needed):
  `log W(p) ≥ (1/log2−o(1)) log₂p·log₃p` i.o.
* Cor 8.2 (Proved mod ET only): `log(1/δ*(T)) ≪ 𝓛^5 log 𝓛`.
* Thm 6.5 (Proved; self-contained): energy bound C-1 — `Σ_U λ^U‖F^{=U}‖² ≤ 1` whenever
  `λ^{supp E} ≤ 2` for every cylinder event, any finite product probability space;
  Cor 6.6 energy tail `≤ 2^{−(t+1)/k}`; Thm 6.9 / Cor 6.10 digit-filtration form.

## v3 change list (for the referee)

Structure: §1 intro; §2 atoms + graded quarantine; §3 mass and charge moment (H_ω(2));
§4 Gallagher (unchanged); §5 linear transfer (fibre cells); §6 energy bound (new);
§7 residual system + sandwich; §8 assembly; §9 status.

1. **Title/abstract/intro** rewritten for 1/5; "Versions" paragraph (1/14 → 1/7 → 1/5);
   method section; literature: Lecomte–Tan 2021 cited as nearest prior art for the
   energy bound, labelled "new to us, literature search partial", no priority claim.
   Status conventions updated (inputs: Gallagher + ET; Håstad dropped).
2. **§2 (source O11 Setting 2.0, Lemmas 2.1–2.2; O12 Lemma 6.2).** Definition 2.3
   (graded quarantine `Q=8∏ℓ^{a_ℓ}`, coordinates on fibres `Ω_ℓ`, survival, events
   `E_{M,D}` indexed by surviving atoms, fibre masses). Lemma 2.4 (reduction (i), exact
   weight formula (ii), pre-quarantine bound (iii)). Lemma 2.5 (iterated graded
   quarantine with start `a_ℓ=1` for odd `ℓ≤max(𝓛,7)`; (a) LLL sums `≤c`, `w_ℓ≤c`;
   (b) `P(E)≤C_1 g/M`; (c) `log Q ≤ 1.02𝓛+7+(C_1𝓛/c)Ω_0`).
   *Deviation:* `C_1=e²` instead of O12's `e³`, via `ω(M) ≤ log M/log 3 ≤ 𝓛` (M odd)
   and `ℓ/(ℓ−1) ≤ 1+1/(𝓛−1)`; proof in the paper. The cost proof writes `Ω_0` directly
   (s₁-weights folded into `C_1`). The proof of `w_ℓ≤c` uses `a_ℓ+1≤f_ℓ`.
3. **§3 (source O12 §§1–5).** Thm 3.1 states the four ET inputs (checked against
   `sources/elsholtz-tao-1107.1010.pdf`: Thm 7.1 p. 25, Cor 7.4 p. 29, (7.10) p. 30);
   (d) stated only in ET's range `A≤B`, which is the only range used. Lemmas 3.2
   (h facts), 3.3 (parametrisation, proof included), 3.4 (block mass, `S_0≪𝓛^4`,
   unconditional `S_0≤2(1+𝓛)³τ*(4T+1)`), 3.5 (rough part), 3.6 (smooth part), Thm 3.7
   (`Ω_0≪𝓛^4 log𝓛`; unconditional `Ω_0≤𝓛S_0`). Remark 3.8 (Assessment): numerics of
   the mean of h, from O12 §7. The old Lemma "mass bound" (`S*≪𝓛^4 log𝓛`) is gone:
   the `log log T` is absorbed by the pre-quarantine.
4. **§5 transfer (source O11 Lemma 3.1, written out in full).** Theorem 5.1 now has
   `8|Q`, consistent unit cells (`b_i≡1 mod gcd(d_i,Q)`), Haar mean `E_H` over
   `H⊂(ℤ/N_0)^×`, `N_0=lcm(Q,D)`, twist condition `|E_H[Bψ]|≤μ/4`. Proof: character
   expansion via `c(χ)=E_H[Bχ̄]/φ(Q)`; item (c) splits real primitive conductors into
   `f_1|Q` and `f_2` coprime to Q; Cases A/B are now `f_2=1` / `f_2>1`; `log N_0≤2Z`.
   Rest of the v2 proof unchanged.
5. **§6 energy bound (source O10 §3.1, Thm 3.4, Cor 3.5, Cor 4.1; O11 Lemma 1.1).**
   Full proofs (Def 6.1 = G): Lemma 6.2 cover bound (degenerate cases/duplicates handled by the
   trace remark), Lemma 6.3 polarization, Lemma 6.4 matching bound for Θ, Thm 6.5
   (Q ≤ ∏(w−1), C-1), Cor 6.6 energy tail, Remarks 6.7 (sharpness; numerical, from
   R38b) and 6.8 (Boolean form `4·2^{−(t+1)/k}` vs `2·2^{−t/(20k)}`; influence bound;
   set-valued literals). Thm 6.9 (digit filtration) re-written: the proof goes
   through tail-block projections `P_{ℓ,j}` and "selections" directly (no `W_{ℓ,i}`
   spaces); same content as O11 Lemma 1.1 with general `i_0(ℓ)` built in. Cor 6.10
   (modulus-weighted tail `2^{−τ/(2𝓛)}`).
6. **§7 residual system + sandwich.** Digits of `Ω_ℓ` in base ℓ; consistent unit cells;
   new Lemma 7.1 (Haar means: `E_H=E` on cell combinations, also twisted by ψ) — this
   was implicit in O11. Cor 7.3 (LLL) now under the per-event mass hypothesis (7.1)
   instead of `w_ℓ≤1/(64k)`. `F^{(j)}` defined on the digits not fixed by `E_j`
   (filtration starting at `max(a_ℓ,v_ℓ(E_j))`, O11 Remark (ii)). `u_j` = Efron–Stein
   truncation to digit sets with `m_U≤e^τ` (O11 Cor 1.2). Lemma 7.5 (error
   `≤m²S·2^{−τ/(2𝓛)}`), Lemma 7.6 (cells of modulus `≤T³e^{2τ}`, consistent), Lemma 7.7
   (ℓ¹), Lemma 7.8 (twist: Forb is now a union of classes; bound by the
   `Ω_{ℓ_0}`-probabilities `π_i`; constants `0.0163`, `0.0166`, total `<μ/4`).
7. **§8.** Thm 8.1 (assembly, `c=1/64`, `τ=2𝓛⌈log₂(100T⁴(S_1+1)e^{3S_1})⌉` with the
   deterministic bound `S≤S_1=C_1S_0`; `log Z ≤ log Q+4τ+6𝓛+1`); proofs of Thms 1.1,
   1.2; Cor 8.2 (Haar side, `c=1/64` instead of O12's `1/8`, density computed
   explicitly); Remark 8.3 (Assessment: where 1/5 comes from; no lower bounds claimed).
8. **Removed:** §"Efron–Stein tail via the switching lemma" (binary encoding, Håstad,
   LMN, binomial median, Lemma tail, Cor el); old iterated quarantine with `Π_0={ℓ≤z}`;
   `k`, `z`, `k_0`, `t`; citation [KB]. Håstad/LMN/OD remain cited for comparison only.
   Added citation [LT] (Lecomte–Tan; bibliographic data from O10, unverified — added
   to the TODO(verify) comment).
9. README entry updated (v3 entry replaces the v2 entry; v1/v2 history kept).

## Points the referee should check hardest

* Thm 6.9's proof (coarse-space reduction to Lemma 6.2 per selection; edge weight
  `≤λ^{2v}` per prime).
* Lemma 7.1 (Haar means) and the consistency bookkeeping of Lemma 7.6 (cells of `u_j`
  use fibre-valued residues).
* Lemma 2.5(c) cost accounting with the pre-quarantine start, and `C_1=e²`.
* Theorem 5.1(c): the split `f=f_1f_2` and the zero-mean argument on H.

## Not done / open

* No independent re-run of numerics (all numbers quoted are from O11/O12/R38b and are
  labelled Assessment/evidence).
* `POINTWISE_HAAR.md` remark: omitted (not on main).
* Bibliographic TODO(verify) list unchanged apart from [LT].
