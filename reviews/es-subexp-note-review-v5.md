# Referee report R64 — `paper/es-subexp-note.tex` v5

Branch reviewed: `side-agent/subexp-paper-v5` (merged into `side-agent/referee-subexp-v5`).
Scope: everything new/changed in v5 (C1–C11 of AGENT_REPORT_O64): intro/abstract, §§11–13, §14, bib.
§§2–10 unchanged from v4 (refereed R56) — only cross-references checked.

STATUS: IN PROGRESS

## Verdicts per claim

**C1 — §11 preamble, imports (A1)–(A3) from [TQ].** SOUND.
Checked against `paper/es-threequarter-note.tex`: (A1) = Lemma 2.2 (`lem:CRT`; distinctness proof
re-derived: `|uv'-u'v|<z_j^2<ℓ` ⇒ `(u,v)=(u',v')`, then `k≡k' (4uv)`, `4uv>4H²>K` ⇒ `k=k'`);
(A2) = Cor 4.3 (`cor:fibremass`, stated for *every* residue c, reduced ⇒ `≍t³`) with Lemma 3.2
(`h(𝒦(K)) = (2/π²)log K+O(1)`); (A3) = Lemma 8.1 + Thm 8.2 (`Q_r` identities, ledger
`log q_max ≤ C_θBt³+r(1+κ)t`, `log T_abs ≤ C_L t⁴`, integer mean for `log N ≥ C_0 t⁴`).
Enlarging `D_B` is harmless in [TQ] (its two conditions on `D_B` are monotone; `c_a=c_v/2` does not
depend on `D_B`; only `C_L, C_0` grow). `X = T^{1/(1+ϰ)}` gives `K_X X ≤ T`; `ℓ > X^{1/2} > K_X`
so `ℓ ∤ L_K`, hence the independence claim. From-scratch check
`scripts/review_r64_atoms.py`: 43 880 atoms in scaled-down families (`z²<ℓ`, `4H²>K`) — zero
residue collisions, `≤ z²` atoms per ℓ, multiplier identity exact (Fractions) on members of each
atom class, activity rule `k | u+cv`, and Bonferroni `Q_r` identities/inequalities (even r
majorant, odd r minorant).

**C2 — Prop 11.1 (Haar lower bound without loss).** SOUND.
Given c: `P(H=0|c)=∏(1-f_c(ℓ)/(ℓ-1)) ≤ e^{-μ_c} ≤ e^{-at³}`; uses (A1) (distinct residues ⇒
`I_ℓ` Bernoulli) and (A2) for every unit c. Conditioning on `n≡1 (24)`: `L_K` is odd (all
`k≡1 (4)`), `3|L_K` (9∈𝒦), so the condition fixes `c mod 3` and an independent `n mod 8` —
the uniform-in-c bound survives. `W(n)>T` ⇒ no atom (modulus `≤K_X X≤T`). Correct; the
md's factor 8 is indeed unnecessary.

**C3 — Thm 11.2 (typical size).** SOUND (modulo [TQ] and Page's theorem, as labelled).
Re-derived: prime count `≤ y + Σ_{p≤x} ν_X(p)`; Case A uses (A3) integer mean with
`log x ≥ C_0t⁴` (forced by `c_1`), and `e^{c_at³/2} ≥ log x`. Case B: `t⁴ ≪ (log log x)^{4/3}` so
all moduli and `Σ|c_i|` are `exp(O((log log x)^{4/3}))`, inside the Page range; the split
`p ≤ √x` / `p > √x` is correct; non-coprime terms are `≤ Σ|c_i| ω(q_i) log x` (the stated bound
is cruder but fine); main terms `x E_*[ν_X(1-εχ̃₁)]` (primitive χ₁ ⇒ class integral is
`χ₁(a)/φ(q)·1[q₁|q]`), `ν_X ≥ 0` on `Ẑ^×` by periodicity, `|1-εχ̃₁| ≤ 3`;
`E_*ν_X ≤ P(H=0)+E(H)_{r+1}/(r+1)! ≤ e^{-at³}+(2eC_ut³/(r+1))^{r+1}` with
`m!e_m(p) ≤ (Σp)^m`, `Σ f_c/(ℓ-1) ≤ 2μ_c`; with `r+1 ≥ D_B t³ ≥ 2e²C_u t³` the tail is
`≤ e^{-(r+1)} ≤ e^{-D_B t³} ≤ e^{-at³}`. Error `x e^{-c_3√log x/2} ≤ π(x) e^{-at³}` because
`e^{at³} ≤ (log x)^{2a/c_a}` in Case B. Note Case B does not use [TQ]'s moment theorem, only (A2).
Page's form (11.1): I could not access Davenport (not in `sources/`); from memory the
statement (Davenport Ch. 20, (9)–(13)) matches, including that the exceptional character is
primitive mod `q₁ | q` and unique for the range. Disclosure in the text is adequate.

## Defects
(to be filled)
