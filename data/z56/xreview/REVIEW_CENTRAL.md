# CENTRAL cross-model hostile review

Reviewed `side-agent/z56-central` at `8366744b90f5bb99a12c1172f520f1b9c7214a78`, not the working-tree version.
**Verdict: ACCEPT-WITH-FIXES (two minor fixes).** No gap found in the principal reductions or upper bound.
The verdict **narrowed**, with a small pointwise strengthening, follows. ES remains OPEN.

## Per-claim findings

| Claim | Classification | Independent check / qualification |
|---|---|---|
| L(i), exact central-band decomposition | CORRECT | Reflection leaves at most one pair; harmonic and integral-main errors are O(1). |
| L(ii), exponent-pair bound | CORRECT | Saito et al. Lemma 19 applies, including partial blocks; dyadic summation gives the stated exponent. |
| L(iii), EPC specialization | CORRECT, CONDITIONAL | Substituting (ε′, 1/2+ε′) gives 1/4−δ/2+O(ε′); logarithm is absorbable. |
| L1, CNT_unif ⇒ SID | CORRECT, CONDITIONAL | O(log x) bands, harmonic-centering error O(y/L), saving η′<min(η,2δ). |
| L1′, polynomial position dependence | CORRECT, CONDITIONAL | δ=min(η/(4B+2),1/8) balances η−4Bδ against 2δ; common threshold is explicit. |
| L2, SID ⇔ saving for the whole central band | CORRECT, CONDITIONAL | Rearrange L(iii); does not imply cancellation-free control of sub-bands. |
| L3, unconditional broad-band range | CORRECT | TY pair gives θ=8093/28960; require 6387/28960<δ<1/4 and sufficiently small ε. |
| L3, finite A/B search | CORRECT / reproduced | Lengths 0–9, six seeds; maxima 8093/28960, 14848/53141, 155/556 agree. No optimality beyond that finite set. |
| U, TW ⇒ CNT_unif | CORRECT | Fourier normalization, residue signs, main-term identity, uniform taper and tail estimates checked below. |
| E and E1, converse and equivalence | CORRECT, CONDITIONAL | EPC is needed only off the central band; uniformity in t and exponent losses survive. |
| P, Hooley-Δ upper bound and E1 consequence | CORRECT relative to cited result | Primary Cor. 1.2 really gives the short-interval exponent 5/2; covering uses two log-unit intervals. |
| P2, localized Fejér implication | CORRECT | Positive kernel, H-normalization and covering yield U|I|(log log U)^(5/2), not loss-free DC. |
| H, Hessian rank/determinant | CORRECT | Both diagonal entries are nonzero and their product equals Φ_hn²; rank is exactly one. |
| CNT_unif “contains CNT” (§1) | CORRECT-WITH-FIX | Direct specialization requires K large enough for the fixed fourth-root range; it is not literal for arbitrary K≥1. |
| §8 numerical identities and Tables 8.1–8.2 | Agreement, with minor range fix | All statistics reproduce; residual independently recomputed at all 2,400 inputs; sample-length prose is inaccurate. |

## Proof audit details

1. **L:** Q⊂P3 because k≤L forces m>x/k≥L′. A remaining pair has L<k<L+Ly/x,
   an interval shorter than one, and its allowed m interval has length y/k<1. Thus D=2P1+P2+R, R∈{0,1}.
   Since P1=yH(L)−F_L, the residual is exactly
   R+2y(H(L)−log L−γ)−[(x+y)log(1+y/x)−y]. Both analytic corrections are O(1).
   Lemma 19 bounds each ψ-sum by x^(κ/(κ+1))N^((λ−κ)/(κ+1))+N²/x;
   λ≥κ, L²/x≤1, and there are O(log x) blocks. The L1/L1′/L2 deductions preserve all-x and all-y quantifiers.
   For L3, multiplying the exponent inequality by 4(κ+1) gives
   (1/2−δ)<(1−3κ)/(4(λ−κ)); the cited rational threshold follows exactly.
2. **U:** log(d/√n)=log(d/e)/2, so inversion uses D_(t/2), not D_t.
   In ζ(s)=1+1/(s−1)−s∫₁∞{v}v^(−s−1)dv, the constant terms vanish outside supp g;
   paired pole terms give ∫_[−log√u,log√u]g=∫g. The remainder has the displayed g±g′ signs
   and is bounded by 2u^(−1/2)e^V(‖g‖₁+‖g′‖₁).
   The divisor-coordinate shift is at most y/(2x)≤w, so both sandwich directions hold even when θ approaches 1.
   Tapers have bounded variation, Fourier L¹ norm O(log(2/w)), and derivative norms O_j(w^(1−j)).
   With w=x^(−c/2), the omitted |t|>2x^c tail is O_j(yx^(ε−(j−1)c/2)).
   Remaining errors are y^(1−η)log x+yx^(−c/2)+yx^(δ−1/2)+y/A, giving η′<min(η,2c).
   The t=0 Ω restriction and c≤1/2 reduction make the harmless bounded errors absorbable.
3. **E:** Reflection replaces the two tails by 2cos(t log(m²/x)), with phase-freezing error
   O(|t|yD/x). Abel summation costs only 1+|t| per dyadic block, since variation is O(|t|).
   Thin central bands number O(x^(η/8)log x); freezing their weights costs O(|t|x^(−η/8)yx^ε).
   Euler summation leaves two zeta terms; its cutoff terms cancel exactly because L′²/x=x/L².
   Pairing the poles before t→0 gives log x+2γ, and the derivative estimate for G(u) is uniform there.
   The three principal losses yield savings 2δ−4c, η/2, η/2−4c in powers of y.
   For c=min(η/16,δ/4), all exceed or equal min(δ,η/4); the remaining errors are smaller.
   E1 therefore preserves existence of positive exponents, not their numerical values.
4. **P/P2:** F(X)=X has no fixed prime divisor. At t=1, β=1 and δ(t,1)=1,
   hence Cor. 1.2 gives y(log log x)^(5/2). θ≤e² needs at most two Δ_H intervals.
   F_H≥4H/π² on a centered arc of length 1/H, so its count is
   O(|E1⁺|/H+C₀U^(1−η)); covering by at most 2H|I| arcs gives P2.
   Since 1/H≤2U^(−η), the advertised scale follows, retaining the explicit loglog loss.

## Primary sources independently read

Downloaded PDFs, rather than relying on `LIT_CHECK.md` or earlier reviewers:
- https://arxiv.org/pdf/2312.15642 — p.15, Lemma 19: parameters, partial-sum uniformity and both error terms agree.
- https://arxiv.org/pdf/2306.05599 — p.2 EPC; p.3 Lemma 1.1 (1.6): all four TY pairs agree, with +ε.
- https://arxiv.org/pdf/2512.05652 — p.2 Cor. 1.2: x^ε≤y≤x and exponent t+1+δ(t,1)/2 agree.
- https://arxiv.org/pdf/1209.0872 — Conj. 3 and Thm 1: substitutions at y=x^(1/4) give 5/16 and 11/36, not a saving.
- https://jtnb.centre-mersenne.org/item/10.5802/jtnb.669.pdf — p.254, (1.12)–(1.13): Ω term and Jutila conjecture agree.
The “not established” literature claims remain search-limited assessments, not proofs of impossibility.

## Computation audit

Every shell invocation used `ulimit -v 6000000` and explicit `timeout`; arrays remain small and checks stream inputs.
- Regenerated `inputs.txt` and `stats.txt`: both byte-identical to the branch's files.
- Recompiled C with `-O2 -Wall -Wextra`; reran first input of all 12 family/scale groups plus one test input.
  Three 10¹⁰ samples used direct bands; higher scales used the documented proxy. Every shared printed field agrees.
- Reran all 15 test inputs: all shared fields agree; max |Ec|=19.2957, max |Ec|/√y=2.5453052, at the stated primes.
- `scripts/z56_xrev_central_check.py` independently uses exact integer roots for rational-power cutoffs and
  60-digit harmonic/log arithmetic for all 2,400 residuals: maximum **0.631850009559724373225881**,
  at x=10000000651, δ=0.20. Every residual agrees to the stored 4-decimal precision.
- The same checker factors each n at x=100000007, y=200 (a different algorithm from the C hyperbola loop):
  D=3668, central count=217, D−Main=−247.0226, Ec=−60.2514; all four direct bands and F_L values agree.
- Ran the exact-rational pair search: the three leading values and δ threshold reproduce.
The full 10¹²–10¹⁶ datasets were not recomputed; their statistics were, plus one raw sample per family/scale.
Floating residuals are numerical checks, not interval-arithmetic certificates; this does not affect the proved identity.
Checker: `ulimit -v 6000000; timeout 180s uv run --with sympy python scripts/z56_xrev_central_check.py /tmp/xrev_CENTRAL`.

## Required fixes, in priority order

1. **Minor, quantifiers (§1):** qualify “CNT_unif contains CNT” by “for K large enough depending on c₁,c₂”.
   Here y/x^(1/4)=2U/(p+2U)^(1/4) approaches values in [2c₁,2c₂]; choose
   K>max(1,2c₂,1/(2c₁)). In particular K=1 does not literally include y=2U≈2x^(1/4).
   No change to L/U/E or the fixed-K equivalence is needed.
2. **Minor, evidence (§8 Table 8.1 introduction):** replace “other families have y within 1% of the first”.
   `sq12` and `nsq12` have y=2000–2188, a **9.4%** increase. The table entries and stored ranges are correct.

CONDITIONAL labels correctly retain EPC; TW is a hypothesis, not an established asymptotic.
The fixed tied/prime CNT problem is not killed or shown equivalent to SID; uniform length-decoupled CNT_unif is the calibrated object.
The Hessian/Voronoi discussion remains appropriately scoped, and no upper bound is presented as positivity or an ES proof.
