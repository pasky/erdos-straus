# Review R48b of POINTWISE_OMEGA13.md (reviewer 2 of 2: analytic inputs + assembly)

Scope: Lemma 3.3(A) (Nair–Tenenbaum input), Lemma 3.3(B), assembly of Thm 3.4,
Cor 3.5 and interface checks I1–I3, §1–2 EVIDENCE numbers.
Reviewed: branch side-agent/beyond-fifth @ 4539218.

## Verdicts (in progress)

### Lemma 3.3(A) — first display: SOUND; second display: GAP (easy repair, D1)

Source check (sources/nair-tenenbaum-1998.pdf, Thm 1 p.125; sources/henriot-1102.1643.pdf (1.1)):
NT Thm 1 needs Q=∏Q_j with no fixed prime divisor, `F∈M_k(A,B,ε)` with
**`0<ε<1/(8g²)`** (Henriot's quotation: `ε≤αδ/(12g²)`), range `x^{4g²ε}≤y≤x`,
`x≥c_0‖Q‖^δ`; RHS is `y∏_{p≤x}(1−ρ(p)/p)Σ_{n_1⋯n_k≤x}F(n)ρ_{Q_1}(n_1)⋯ρ_{Q_k}(n_k)/(n_1⋯n_k)`;
constant depends on A,B,ε,δ,k,g,D only. Class M_k: `F(a_1b_1,…)≤min(A^{Ω(a)},B a^ε)F(b)`
for `(a_1⋯a_k,b_1⋯b_k)=1`.

Re-derived for `Q_1=n`, `Q_2=4n−1`, g=2: irreducible, coprime, `Disc(4n²−n)=1`,
no fixed prime divisor (Q(1)=3 odd, Q(2)=14 prime to 3), `ρ(2)=1`, `ρ(p)=2` (p odd),
`ρ_{Q_1}≡1`, `ρ_{Q_2}(n_2)=1_{n_2 odd}`; so the RHS is `≤y∏(1−ρ(p)/p)·Σ_{n_1≤x}τ(n_1²)/n_1·Σ_{n_2≤x}f_2(n_2)/n_2`
(the product constraint `n_1n_2≤x` only helps). `F=τ(n_1²)f_2(n_2)` with
`f_2(p^k)=β·2^{[p≤Y]}·p/(p−1)` (k-independent, ≤8) is separately multiplicative, so
`F(ab)=τ(a_1²)f_2(a_2)F(b)` and `τ(a_1²)f_2(a_2)≤min(8^{Ω(a)},B_ε a^ε)` for **every** ε>0,
with A,B,ε uniform in T,Y,β (since β≤2, `2^{ω_Y}≤2^ω`). Evaluation:
`x(log x)^{−2}·(log x)^3·(log x)^β(log Y)^β ≪ x(log x)²logY` (the doc writes
`(log x)^β logY`; it should be `(log x/logY)^β(logY)^{2β}=(log x)^β(logY)^β`, harmless since
`(logY)^{β−1}≤e` for `Y≤T`). Summing `1/M` over dyadic blocks: `𝓛³logY`. **SOUND.**

Second display: the doc multiplies by `(3/2)^{Ω_Y(M)}`. Then `F(1,3^k)≍(3/2)^k`,
and `(3/2)^k≤B·3^{kε}` for all k forces `ε≥log(3/2)/log3≈0.37`, while NT allows only
`ε<1/32` (g=2). So **this F is not in any admissible class `M_2(A,B,ε)`**; the
remark "Euler factor 1+O(1)/p" addresses the wrong hypothesis. See D1 (repair is
easy and leaves the bound `𝓛³(logY)^4` intact).

### Lemma 3.3(B) — SOUND (minor wording, D3)

Re-derived line by line: (i) for `M=ℓm`, `gcd(M,M')/ℓ^{min v}` divides `gcd(m,m')`
(also when `ℓ²|M`), and `φ(g)≤g=Σ_{e|g}φ(e)`; summing over D gives `Σ_D H P_H=w(M)/M`, so
`B_2(ℓ)≤Σ_eφ(e)V(eℓ)²` ✓. (ii) CS in k with `Σ_{k≤T}1/k≤𝓛+1` ✓. (iii) `N=eℓk` is
the atom modulus M itself, `φ(e)/(e²ℓ²k)=φ(e)/(eℓN)≤1/(ℓN)`, at most `τ(N/ℓ)≤τ(N)` pairs
(e,k), `Σ_{ℓ|N,ℓ>Y}1/ℓ≤ω(N)/Y` ✓. (iv) Ξ: CS with `w²τω≤τ(A²)²·H²(M/φ)²τ²`, and
`Σ_{A≤T}τ(A²)^4/A≍𝓛^{81}` (→ 40.5 = the doc's "4.5+36"), the other factor
`≪(logY)^{O(1)}𝓛^{8β^4}`, `β^4−1≍1/log𝓛` so `𝓛^{O(β^4−1)}=O(1)`. Hence
`Ξ≪𝓛^{C_0}(log𝓛)^{O(1)}`, `C_0` absolute; the `(logY)^{O(1)}` with `Y=𝓛^{C_0+4}` is
only polylog in 𝓛, so not circular. Uniform in T. ✓

From-scratch numerics (`scripts/review_o13b_lemma33.py`, exact `B_2(ℓ)` by brute-force
pair sums, β=1+1/log𝓛):

| T | Y | Σ_{ℓ>Y}B_2 exact | Σ_eφ(e)V(eℓ)² | (𝓛+1)Ξ/Y |
|---|---|---|---|---|
| 2000 | 20 / 100 / 400 | 267 / 15.3 / 0.52 | 360 / 18.8 / 0.63 | 4.0e5 / 1.3e5 / 3.3e4 |
| 20000 | 20 / 100 / 400 | 2437 / 221 / 16.4 | 3390 / 294 / 21.4 | 4.6e6 / 1.8e6 / 5.0e5 |

The chain of inequalities holds in every case (by 3–5 orders of magnitude at the last
step — the bound is valid, just very lossy; this is why `Y=𝓛^{C_0+4}` with `C_0≈50`).
Also `S_H^β/(𝓛³logY)≈0.06–0.09`, cost `/(𝓛³(logY)^4)≈0.002–0.012` at these T,
consistent with (A).

### Theorem 3.4 assembly — SOUND-AFTER-REPAIRS (D1, D2)

Powers re-tracked: `η=(3/4)log(1+1/log𝓛)≍1/log𝓛`, `logY=(C_0+4)log𝓛≍log𝓛`.
`E[logQ_end]≤log8+(1/η)·O(𝓛³(logY)^4)=O(𝓛³(log𝓛)^5)`; `E[S_res]=O(𝓛³log𝓛)`;
`P(late bad)≤η^{−2}(𝓛+1)Ξ/Y=O((log𝓛)^{O(1)}𝓛^{C_0+1}/𝓛^{C_0+4})→0`. Three bad events of
probability ≤1/4 each ⇒ a good realisation exists; Lemma 1.1 on the fibre gives
`log(1/δ*)≤logQ+(4/3)S_res`. So the explicit bound is `log(1/δ*)≪𝓛³(log𝓛)^5`
(the doc's `(log𝓛)^{O(1)}` can be made explicit). Events with `M|Q` have probability 0 on
the fibre (Lemma 3.1) and must simply be dropped before applying Lemma 1.1 (which
assumes `supp E≠∅`); harmless, but say it. `β≤e^{1/3}` and `η≤1/4` hold for 𝓛≥e^{3}.
`Y≤T` (needed in Lemma 3.3(A)) holds for large T.

Normalisation mismatch (D2): POINTWISE_HAAR §0 defines `δ*` with Haar measure
**normalised in `n≡1 (24)`**, while Thm 3.4 speaks of "n∈Ẑ^×" and the process starts
from `Q=8`, `r≡1 (8)`. These are different quantities and "exponent 3" combines an upper
bound on one with a lower bound on the other. It is repairable: ℓ=3 is always stepped at
a=0 (initially `w̃_3≫η`), revealing the unique square class 1 mod 3, so every
realisation has `r≡1 (24)` and the bound holds for the HAAR δ* too; equivalently start at
`Q=24,r=1` and note `p_0(E)=(1+(−d|3))P_H(E)≤2P_H(E)` for `3|M`, absorbed by the factor
`2^{u_0}` that 3 no longer contributes. Lemma 3.2(b)'s sentence "p_0=P_H (M odd, so the
class mod 8 is irrelevant)" needs this amendment.

