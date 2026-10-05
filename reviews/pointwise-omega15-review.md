# Hostile review R57 of POINTWISE_OMEGA15.md (task O57, branch side-agent/beyond-ceiling)

Reviewer: side-agent/review-omega15. Reviewed state: side-agent/beyond-ceiling @ 3b0f26f
(merged into the review branch; author's document not edited).
From-scratch scripts: `scripts/review_o15_*.py` (no reuse of `omega15_pseudorandom.py`).

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (re-derived; brute-forced) |
| Thm 1.2 | SOUND (labels match O14 Thm 4.5 inputs) |
| Def 2.1 / Thm 2.2 | SOUND (Def 2.1 is narrow by design, see D-notes) |
| Lemma 2.3 | SOUND (minor bookkeeping) |
| Cor 2.4 | SOUND-AFTER-REPAIRS (proof OK; Q-reduction wrong in general; headline oversold) |
| Prop 2.5 | SOUND |
| Thm 3.1 | (pending) |
| Prop 4.1 | (pending) |
| Remark 4.2 / Assessment 4.3 | (pending) |
| Lemma 5.1 / Prop 5.2 | (pending) |
| §0, §6, §7 scope and labels | (pending) |

## Per-claim notes

### Lemma 1.1 — SOUND
Re-derived line by line. Conditional on x_s and on the bit pattern, the X_b are independent, so
`E_{δ_{1_y}}∏h_b=∏_{b∈y}β_b∏_{b∉y}γ_b`; the alternating sum over `y⊆J` factorises to
`−∏_{J}(γ_b−β_b)∏_{I∖J}γ_b` (factors with `b∈J∖I` vanish since `h_b≡1`). Bounds checked:
`|γ_b|≤(1/4+p*)/(1−p*)≤3/7<1/2` (needs p*≤1/8, stated); `e_{k+1}(r)≥1` from the O14 chain
(`n e_n≥e_{n−1}(R−(n−1)r*)≥(k+1)e_{n−1}` uses only (1.0)); `C(m,k+1)2^{−(m−k−1)}≤2^{k+1}`.
Bits with `p_b=0` (β_b undefined) carry `w_J=0`, harmless. Result `(4r*)^{k+1}` is correct.

From scratch: `scripts/review_o15_lemma11.py` builds ν from its *definition* (O14 Lemma 1.1 law
on bits, X_b uniform on ℤ/m_b conditioned on the bit, Ω_b depending on a small coordinate s),
computes `E_ρh` by summing over all bit patterns and residues (not via the closed form), exact
rationals. Seeds 1–3, 2360 instances (k∈{0,1}, n≤26 bits, random and adversarial h_b with
`|E h_b|=1/4`, `β_b=±1`): ν is a probability law with exact k-wise marginals and `ν(0)=0`
(n≤11), `E_ρh=0` whenever `|I|≤k` (47 cases), `|E_ρh|≤(4r*)^{k+1}` always (worst ratio 0.081),
and `|ρ|≤P_0 2^{k+1}≤e^{−(1−p*)R}2^{k+1}` (ratio 1.000: the σ_J charges never cancel at the
bit level for k≤1 — the TV bound is attained, see Prop 2.5).
Caveat (not a defect): toys reach only k≤1; the identity is k-independent and was checked.

### Thm 1.2 — SOUND
Checked against O14 Thm 4.5's proof: it does give `R(x)≥μ*=c_9ε³𝓛³/log𝓛` for *every* small
configuration (unit x) with `p*≤T^{−0.09}`, ε absolute (fixed in O14 Lemma 4.3), so η is
uniform in Q (log Q≤T^{0.05}), r and B. `k+1=⌊μ*/2⌋` satisfies (1.0) for T large;
`E_νB≤E_νF=0` needs only `B≤F` P-a.e. (`dν/dP≤2`, O14 m1(b)). `8r*≤T^{−0.08}` and
`(k+1)≥μ*/2−1` give `η=exp(−c𝓛^4/log𝓛)` with `c≍c_9ε³`. Remark (i): the level-D part lies in
`𝒱_k` and `E_ρ=0` there by O14 Thm 1.3 directly (no reducedness needed) — correct. Remark (ii)
fine (F is periodic, so `‖F‖_×<∞`). No hidden parameter dependence found.

### Def 2.1 / Thm 2.2 — SOUND
`m_ν=N_xν` is nonnegative, has mass N_x, accuracy `N_x|E_ρh|≤N_x(4r*)^{k+1}` on every reduced
product, and `ν(F=1)=0`. Correct. Note (feeds D-notes below): Def 2.1 lets a certificate use
*only* nonnegativity, total mass and the accuracy bounds; it may not use that `m_x` is a sum of
unit point masses at integers `≤x` (atomicity/integrality/support). The fake `N_xν` is a
diffuse measure. This is a legitimate modelling choice but it is exactly where (N2) lives, and
it should be said at Def 2.1, not only in the Reading after Cor 2.4.

### Lemma 2.3 — SOUND
Re-derived. (a) trivial. (b) characters: `Σ_χ|Σ_{p∤q}χ(p)|²=φ(q)N'` (distinct units), principal
term `N'²`. Additive: `Σ_aS(a)\overline{c_q(a)}=Σ_pΣ_ac_q(a)e(ap/q)=q·N'` (Ramanujan-sum
orthogonality, `c_q` real), giving `q(N_x−2N_xN'/φ+N_x²/φ)≥qN_x(1−N_x/φ)` because `N'≤N_x`; the
`a=0` term vanishes. All correct. From scratch (`scripts/review_o15_lemma23.py`, part A): 78
cases (Q∈{1,3,4,5,7}, x≤150, q>x prime or a product of two primes, characters built explicitly from
primitive roots): (a), both lower bounds of (b) and the identity `Σ_χ|·|²=φ(q)N'` hold.
Bookkeeping: `S(a)` is written over all `p≤x, p∈H` but must run over the primes counted by `m_x`
(m3). In Cor 2.4 the hypothesis `N_x≤φ(q')/2` is asserted via "`q'>x²`", but the case split only
gives `q'>x` (m4).

### Cor 2.4 — SOUND-AFTER-REPAIRS; is "full-orbit uniform" honest?
*Proof.* Correct given Def 2.1: shallow terms have `E_ρ=0`, deep terms (≥k+1 big primes, modulus
`>T^{0.6(k+1)}>x`) cost `≥1/2` (classes) / `≥√(N_x/3)` (characters) each by Lemma 2.3, and
`E_HB≤η·Σ_deep|c_i|`. The Q-reduction sentence is false when `v_p(q)>v_p(Q)` for some `p|Q`
(on H the p-adic digits above `p^{v_p(Q)}` are free, so a class mod q is a class mod q′
*intersected with a sub-class at p*, and a character mod q is not "a character mod q′ times a
constant") — see M2; repairable.

*The class.* Not tailored to make the result trivially true: it is exactly the standard sieve
remainder accounting `Σ_q|λ_q|·max_a|r(q,a)|` (BV/GRH-type statements are uniform in a), and the
quantitative core is Thm 1.2, not the definition. But the definition does make the
"any accuracy, GRH included" clause **vacuous**: by Lemma 2.3, for moduli `q>x` *no* true
orbit-uniform bound beats the trivial `≈1` per class (`≈√N_x` per character), and GRH's
`x^{1/2}log²` is already trivial for `q>x^{1/2}`. So Cor 2.4 really says: *a minorant whose positive
mean lives on moduli `>x` cannot be paid for with trivial per-term remainders; and if all moduli are
`≤x`, O14 Thm 4.5 applies.* The strength of the prime input plays no role at all; the
headline should say so rather than present GRH-independence as a strength (M1).
Robustness check (positive, suggested addition): *one-sided* orbit-uniform accounting is also
covered. For a deep class with `c_C>0` a certificate may use `m(C)≥0` (orbit-uniform cost
`N_xP(C)≈0`); dropping those terms gives `B'≤B≤F` with only negative deep class terms, each of
which needs an upper bound and costs `≥1/2` (some class of the orbit contains a prime). Thm 1.2
applied to B' gives the same `N_xη>1/2`. Worth one sentence, since one-sidedness is the first
thing a sieve theorist would try.

### Prop 2.5 — SOUND
(i) `|ρ_{x_s}|≤P_0Σ_Jw_J‖σ_J‖=P_02^{k+1}`, `P_0≤e^{−Σp_b}≤e^{−(1−p*)R}`, and
`(1−p*)−(ln2)/2≥0.6` needs `p*≤0.053` (true, `p*≤T^{−0.09}`; implicit). My toy runs show
`|ρ|=P_02^{k+1}` exactly (no cancellation), so (i) cannot be improved via cancellation.
(ii)–(iii) and the exponent algebra `N_xη>(1/2)(e^{0.6μ*}/4)^{s−1}` re-derived; the `s=∞` case is
right. The model (Hölder with the *true* error vector) dominates any valid Hölder certificate.

## Defects
