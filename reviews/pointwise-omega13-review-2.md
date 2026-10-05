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

