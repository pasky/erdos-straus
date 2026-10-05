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

