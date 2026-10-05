# AGENT REPORT O43 — verify.py blocks (cu)–(cy)

Branch `side-agent/verify-blocks-2`. Only `verify.py` and `STATUS.md` (the verify.py bullet) changed.

## What was added
Each block is self-contained, deterministic (fixed seeds) and asserts with a message naming the
document and lemma. The first comment line of each block points to its document and scripts.

| block | document | what is replayed | time |
|---|---|---|---|
| (cu) | POINTWISE_OMEGA9 | Thm 1.1 character expansion, built from scratch on a toy (Q=5, D=8·9·7, 25 random signed cells, all 576 characters mod 2520): `c(χ)=E_D[Bχ̄_D]/φ(Q)`; item 1 (`c≠0 ⇒ cond χ_D | d_i`, 416 nonzero, 160 zero); item 2 (`|c|≤E|B|/φ(Q)`, `c(χ_0)=μ/φ(Q)`); item 3 (30 real twists, `c=μ_ψ/φ(Q)`); `χ↦χ*` injective; exact `S(20000)=Σc(χ)ϑ(x;χ)`. Also Lemma 2.1 (random arrays), Case A `λ≥min(u,1)/2` (grid min ratio 1.215, which matches the doc), and exponent bookkeeping: `log log Z/log L` = 7.90 … 7.045 at L = 1e3 … 1e60 (decreasing to 7); Thm 2.3 rate `log₂p/(𝓛/log𝓛)` = 0.6931 (log 2) | 2.5 s |
| (cv) | POINTWISE_XWIN §1.1 | Klein-orbit structure, `|S_σ|=φ/2`, `2^β` selections and the β bound for all a≡3 (4) ≤ 399; Lemma 1.1 by brute force (full Rat_a(x) from exponent vectors) for a ≤ 127 and x ≤ 2·10⁴ (515,870 pairs, 383,303 with −1∉Rat), plus Remark (i) | 2.4 s |
| (cw) | POINTWISE_WINDOW2 | Lemma 1.2: both norm-form equivalences checked for every n ≤ 2·10⁴; `n_7=n_3+1`, `3∤n_3`, `7∤n_7` for the 273 Mordell-hard p < 10⁵. Prop 3.7: the model is rebuilt from the text, the config set and μ match the dump, ν≥0, ν(∅)=0, all 89 visible correlations are matched (9e−15), and a 60-digit re-solve of the 89×89 support system is positive (min ν/μ 0.1542) and agrees with the dump to 7e−13 | 3.4 s |
| (cx) | EXCEPTIONAL_INTERFREQ2 | Example 3.2: identity on [−2000,2000), hybrid charge 0, written as itself it costs 1. Lemma 3.1 sign rule on 300 random representations. [scipy] Rigidity LP on Z/2520: μ(0 mod 21)=0 and μ(r mod 21)=1. Consequence for N+1 = 12, 15, 20. Lemma 9.3: `σ_C(N)` = 2/5 (C=2) and 0 (C=1) for 12 ≤ N ≤ 300. [scipy] The projected SPW LP satisfies σ_max ≤ σ_C(N) at five (N, C, Q′) with equality in every case | 2.2 s |
| (cy) | EXCEPTIONAL_LARGESIEVE2 §§8–9 | Lemma 8.1 by exact integer max-flow (Gale) on 504 band sets (l, l′ ≤ 23, η ∈ {1/8, 1/9, 1/10, 1/20}), plus a negative control (a wide band is infeasible). Prop 8.2(a): an exact Fraction measure μ=μ₁⊗μ₂ on 𝒜 mod 5005 that is uniform on every class of all 9 allowed moduli and non-uniform mod D₁ (control). [scipy] largesieve2_checks check (5) (majorant LP = 1, Lemma 8.3 polynomial); contrast LP with D₁ allowed gives 0.7714 < 1; Thm 9.1 inequality chain (*), (**) on 18 nontrivial random kernels mod 1260, using the exact best S from an LP | 14 s (check (5) ≈ 10 s) |

## Run
`ulimit -v 8000000; OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 1200 uv run --with scipy python verify.py`
→ **all checks passed**, exit 0, 4 min 9 s wall time. The five new blocks take ≈ 25 s together. Without scipy, (cx) and (cy) skip only their LP parts.

## Scope / caveats
* Every block is a finite check (toy sizes) of a step of the proof or of a certificate. None proves the theorem. Thm 1.1 (cu) is checked as an identity on one toy group. Gallagher's theorem (G) and the Page bound are not touched.
* (cu)(4) and the Thm 2.3 rate are Assessment-level arithmetic with all constants set to 1, as in (cs).
* (cw) Prop 3.7 is CERTIFIED **in the discrete model only**. The block re-checks the certificate and nothing about real sieves.
* (cx) SPW LP: σ_max ≤ σ_C(N) is the assertion. Equality is observed, not asserted.
* Not replayed: OMEGA9 PO-bookkeeping comparison (2) of omega9_charcheck (illustration only); XWIN §§1.2–2 (Thm 1.2/1.5/2.2, Lemma 2.1 MC); WINDOW2 §§3.5/6–7 LPs and the one-window exact dual (review_w2_lp.py); INTERFREQ2 §§4–6, 10; LARGESIEVE2 Prop 8.4 / Thm 8.5 numerics and Prop 9.2.
