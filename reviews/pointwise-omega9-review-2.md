# Review R34b of POINTWISE_OMEGA9.md (reviewer 2 of 2: assembly and interfaces)

Reviewed: branch `side-agent/omega9-exponent` at `9a21ffc` (checkpoint 1,
after R34a repairs), merged into `side-agent/review-omega9b`. Scope: (i)
character-coefficient identity, (ii) Lemma 2.1, (iii) interface O8 Thm 3.4 →
Thm 1.1, (iv) exponent chain to 1/7, (v) Thm 2.3's constant, (vi) repaired
O8 §6. Theorem 1.1's analytic core and the Gallagher quotation are reviewer
1's (R34a/R34 reviewer 1); touched here only where the interface needs it.

## Summary verdicts

(filled in claim by claim below; final table at the end)

## Claim-by-claim

### (i) Coefficient identity, Thm 1.1 items 1–3 — SOUND

Re-derivation. `f=B·1[n≡1 (Q)]` on `G=(ℤ/QD)^*`; by CRT `n↔(n_Q,n_D)`,
`χ=χ_Qχ_D`, and f vanishes unless `n_Q=1`, so
`c(χ)=φ(QD)^{-1}Σ_{n_D}B(n_D)χ̄_D(n_D)·χ̄_Q(1)=E_D[Bχ̄_D]/φ(Q)` (needs
`gcd(Q,D)=1`, which follows from `gcd(d_i,Q)=1`). Note c is *independent
of χ_Q*: all `φ(Q)` lifts of a given `χ_D` carry the same coefficient. For
the exceptional zero this is harmless because the class is `a=1`
(`χ̄(1)=1`), so the subtracted `x^{β_1}/β_1` always has the sign of
`c(χ)`; Cases A/B correctly split only on `χ_D`. Item 1: the mean of
`1[n≡b_i (d_i)]χ̄_D` over units mod D is `χ̄_D(b_i)/φ(d_i)` if `χ_D` is
trivial on `{n≡1 (d_i)}` (⇔ cond `χ_D | d_i`), else 0. Item 3: for real
`χ_D` induced by ψ (f|D), `χ_D=ψ` on units mod D, so
`E_D[Bχ̄_D]=E_D[Bψ]=Σ_{f|d_i}c_iψ(b_i)/φ(d_i)`, which is exactly PO Thm
4.1's `μ_ψ` (PO line 373) and O8 Lemma 3.3's `E[Bψ]`. Haar measure in O8
is uniform on units mod `ℓ^{e_ℓ}` (O8 header), and `D | ∏ℓ^{e_ℓ}`, so
`E_Haar = E_D` on functions of n mod D: the measures agree.

From-scratch check `scripts/review_o9b_chars.py` (→ `data/review_o9b/chars.txt`):
`Q=5`, `D=8·9·7·11` (even and non-squarefree conductors included, unlike the
author's squarefree toy), 26 random signed cells, all 5760 characters built
from discrete logs. Seeds 1–3: (a) direct DFT vs `E_D[Bχ̄_D]/φ(Q)` agree to
`2·10^{-16}`; (b) no nonzero coefficient with cond `χ_D ∤` every `d_i` or cond
`>Z`; (c) `|c(χ)| ≤ E|B|/φ(Q)` (slack ≥0.09), `c(χ_0)=μ/φ(Q)`; (d) all 62 real
χ with nontrivial `χ_D`: `c(χ)=μ_ψ^{PO}/φ(Q)` to `2·10^{-16}`; (e) `χ↦χ*`
injective (5760 distinct); (f) `S(x)=Σc(χ)ϑ_{QD}(x;χ)` exactly at `x=2·10^4`.

### (ii) Lemma 2.1 and `A ≤ 1.03` — SOUND

`B^-:=max(−B,0)`: where `B<0`, `B^-=−B ≤ F−B` because `F≥0`; where
`B≥0`, `B^-=0 ≤ F−B` because `B≤F`. So `E|B|=EB+2EB^- ≤ EB+2E[F−B]`. The
negative part of B is thus controlled by the one-sided error alone; no
bound on `|B|` or `M_1` is needed (only `F≥0`; `F≤1` is not used). In Thm
2.2, O8 Thm 3.4's proof gives `E[F−B]≤δ/100` and `μ≥0.99δ`, so
`η=1/99`, `A≤1+2/99≈1.0202≤1.03`. `A` is a property of the *function* B
(Haar ℓ¹ norm), not of a cell representation, so the R34a MAJOR 2
phenomenon (representation-dependent `M_1`) cannot reappear here.
`B≤F` for O8 Lemma 6.1's choice of `u_j` holds because Lemma 3.1 holds
for *arbitrary* real `u_j` (re-derived: `F−B=Σ_iA_i(Σ_{j<i}A_je_j)²`).

From-scratch check `scripts/review_o9b_brw_l1.py` (→ `data/review_o9b/brw_l1.txt`):
300 random toy systems (3–5 coordinates on `ℤ/q`, `q≤4`, 2–6 single-value
events of support ≤2), `u_j` random Gaussian or Efron–Stein truncations:
`min(F−B)=0`, `B^-≤F−B` pointwise, and `E|B|≤(1+2η)EB` in all 230 trials
with `EB>0` (max excess `1.1·10^{-16}`, rounding).

### (iii) Interface O8 Thm 3.4 / Lemma 6.1 / Lemma 3.3 → Thm 1.1 — SOUND (one MINOR)

Checked hypothesis by hypothesis, with `Q:=Q_Π·ℓ_aux`, `ℓ_aux∈(R,2R]`,
`R=max(T,max d_i)`:
* `gcd(d_i,Q)=1`: cell moduli are products of `ℓ^{e_ℓ}` over free primes,
  which are `ℓ∈(z,T]∖Π` (O2 Lemma 11.2), so coprime to `Q_Π`; `ℓ_aux>max d_i`
  so `ℓ_aux∤d_i`. Hence also `gcd(Q,D)=1`, needed for (i).
* `gcd(b_i,d_i)=1`: Lemma 6.1 expands into unit cells (coordinates uniform
  on units mod `ℓ^{e_ℓ}`). ✓.
* `B(n)≤1[W(n)>T]` on `n≡1 (Q)`, `(n,D)=1`: O2 Lemma 4.3 (I) needs only
  `n≡1 (Q_Π)` and "no event at n" (re-read; no coprimality needed), plus
  `B≤F`; the class mod `Q_Π ℓ_aux` is a subclass. ✓.
* `μ>0`, twist: Lemma 3.3 needs `w_ℓ≤1/(64k)` (Lemma 11.2 with
  `c_0=1/(64k)`) and `E[F−B]≤EF/100` (EL via Cor 4.2's `k_0`; Lemma 6.1's error
  `e^{1/2}·2·4^{−k_0}≤4·2^{−k_0}` ✓). Its quantifier (`gcd(f,Q)=1`, `f|d_i`)
  is exactly Thm 1.1's; enlarging Q by `ℓ_aux` only shrinks the ψ-family.
  Lemma 3.3's "f odd squarefree" holds since `2∈Π` (`840|Q_Π`), so f is odd,
  and real primitive odd conductors are squarefree. `μ_ψ` agrees (see (i)).
* Conductors `≤Z`: Thm 1.1 uses `Z=Q·max d_i`, so the `ℓ_aux` factor is
  inside Z: `log Z ≤ log Q_Π + log 2R + log max d_i ≤ log Q_Π+2(3k+2d+1)𝓛`
  using `max d_i≤T^{3k+2d}` (cells on `≤3k+2d` free primes, `ℓ^{e_ℓ}≤T`). ✓.
* `p>T`: `p≡1 (ℓ_aux)`, `p≠1` ⇒ `p>2ℓ_aux>T`; `p≡1 (840)` ⇒ hard. ✓.
* `A≤Z^{1/4}`: `A≤1.03`. ✓.

**MINOR m1 (Thm 1.1 proof, "x ≥ C·A·Z^3" and Case A's R_1 step).** Case A
needs `|R_1| ≤ 2AμZ³/φ(Q) ≤ λμx/(100φ(Q))` with only
`λ ≫ Z^{−1/2}(log Z)^{−2}`, i.e. `x ≫ A·Z^{7/2}(log Z)^2`, not `x≥C·A·Z^3` as
listed. The conclusion is unaffected (the hypothesis gives
`log x ≥ C'log Z` with C' arbitrary, so e.g. `x≥Z^5≥A Z^{4.75}`), but the
displayed consequence should read `x ≥ C·A·Z^{4}` (or "`x≥Z^5`").
(Reviewer 1 owns the analytic core; flagged here as an interface item.)

### (iv) Exponent chain to 1/7 — SOUND

Recomputed (z=𝓛², ET: `S≤S*≪𝓛^4log𝓛`, O2 Lemma 11.1 ✓):
`k≤𝓛/(2log𝓛)`; `b=⌈log₂4T²⌉≈2.89𝓛`; `w=kb≍𝓛²/log𝓛`;
`k_0=⌈3S log₂e+log₂(400m²(S+1))⌉` with `log m≤(k+2)𝓛≍𝓛²/log𝓛`, so
`k_0≍S*≍𝓛^4log𝓛`; `d=4C_Hwk_0≍𝓛^6` (the `log𝓛` of S* cancels the
`1/log𝓛` of k — which is why no `log log p` appears, unlike O8 Thm 6.3);
junta term `2(3k+2d+1)𝓛≍𝓛^7`; `log Q_Π≤(π(z)+64k²S*)𝓛+4≍𝓛^7/log𝓛`
(`|𝓑|≤kS*/c_0`, `c_0=1/(64k)`). So `log Z≪𝓛^7`, Thm 1.1 with `A≤1.03`
gives `log p≪𝓛^7`, and `log W>𝓛≥(log p/C)^{1/7}`.

**Bottleneck.** It is the *junta* term `d·𝓛` (cells on `≤3k+2d` free primes,
each costing up to 𝓛 in `log max d_i`), not the quarantine: `log Q_Π` is
smaller by a factor `≍log𝓛` (and by a constant ≈860 in the tally).
Note that `log Q_Π ≍ 𝓛^7/log𝓛` is the same quantity that bounds the Haar
side, O2 Thm 11.3 (`log(1/δ*)≪𝓛^7/log log T`, from `8k²S*𝓛`). So after
Thm 1.1 the prime-side certificate matches the *Haar-side certificate* up
to `log𝓛`; going below 1/7 needs d down (ESW) **and** the quarantine
down, as the "Next" item says. Correct.

From-scratch tally `scripts/review_o9b_exponents.py`
(→ `data/review_o9b/exponents.txt`, constants 1, `C_H=5`): local log-log
slopes at `𝓛=10^{12}`: k 0.96, w 1.96, `k_0` 4.04, d 6.00, `log Q_Π` 6.96,
`d𝓛` 7.00, `log Z` 7.00; the junta term is ≈860× `log Q_Π`.

Not an issue but worth stating: K (hence `log(1/δ)≍S`) now enters only via
`1+log A=O(1)`; neither `M_1`, nor `m`, nor Lemma 6.1's third bullet is used
anywhere in Thm 2.2. (Lemma 6.1's ℓ¹ bound is dead weight for O9.)

### (v) Thm 2.3's constant `1/log2` — SOUND (one MINOR)

Unconditionally, O2 Lemma 11.1 gives
`S* ≤ C log𝓛·(3+𝓛)·Σ_{sr'²≤T}τ(4sr'²+1)/(sr')`; Wigert
(`τ(n)≤2^{(1+o(1))log n/log log n}`, `n≤4T+1`) and `Σ1/(sr')≪𝓛²` give
`log S* ≤ (log2+o(1))𝓛/log𝓛` — the constant `log2` is explicit because a
*single* τ appears. Every cost term is `≤𝓛^{O(1)}(S*+1)`: `log Q_Π` (via
`64k²S*𝓛`), `d≪w(S*+k𝓛)`, `log ℓ_aux`; and Thm 1.1 has `log p≪log Z` with
an absolute constant. So `y:=log₂p ≤ log S*+O(log𝓛) ≤ (log2+o(1))𝓛/log𝓛`.
Inversion: `y≤𝓛` ⇒ `log y≤log𝓛` ⇒ `𝓛 ≥ (1/log2−o(1))·y·log𝓛 ≥
(1/log2−o(1))·y·log y`, and `log W>𝓛`. ✓. The halving of the old
`1/(2log2)` is exactly the removal of the square `K·log Z` (`K≍S*`).
Inputs: (G), Page, O2/O8 machinery; ET not used. ✓.

**MINOR m2 (Thm 2.3 proof).** "Wigert's `log S*≤(log2+o(1))𝓛/log𝓛`" is
attributed implicitly to O2 Lemma 11.1, whose statement only says
`exp(O(log T/log log T))`. Cite the one-line derivation above (single τ
in the sum, Wigert's constant) so that the `log2` is checkable; O8 Thm 4.4
has the same gap in wording.

