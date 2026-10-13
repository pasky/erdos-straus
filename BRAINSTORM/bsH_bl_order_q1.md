# bsH_bl_order_q1 — Bright–Loughran classes of order q − 1 live on the ES_q surface over F_q(T) and vanish on integral points (O181)

**ES is not solved here.** Deep version: DRINFELD_ES.md §2. Script `scripts/bsH_bl_classes.py`.

## Idea
BL Prop 2.6: Br Ũ/Br k ≅ μ(k) via α_ζ = (−u₁/u₃, −u₂/u₃)_ζ. Over ℚ only ζ = −1; over ℚ(ζ_m) the order-m classes
corestrict to constants on ℚ-points (bsD_brauer_cores). Over F_q(T), μ(F) = μ_{q−1}: order-(q−1) classes exist on
the base, with no corestriction. Their reciprocity law is the most direct "degree-k Diff-parity" for ES_q.
## Literature
Bright–Loughran, arXiv:1908.02526 (Props 2.5, 2.6, Lemmas 3.1–3.6; checked in sources/); tame symbols and Weil
reciprocity: Serre, *Algebraic Groups and Class Fields*, III; Rosen Ch. 7 (from memory).
## Statement (PROVED)
Steinberg identity: α_ζ(u) = (y, −1)_ζ + (x, y)_ζ, x = λu₁ − 1, y = −u₂/u₃ (any field). For monic NC solutions of
A/P = Σ1/u_i with P a prime power, every local invariant is 2-torsion; odd-order α_ζ(u) = 0 in Br F. For Type II
points inv_P α_ζ = (−f/P)_m (the Kudla symbol), recovering bsH_kth_power_law as a reciprocity law.
## Barrier screen
T1: the order-2 part is FF Prop 4.1 (degree-parity sign); the odd-order **prime-to-p** part (classes α_ζ, ζ ∈ μ_{q−1};
R181 repair D1: p-primary classes, also of odd order, are not addressed) carries no information at all — stronger than
the number-field corestriction collapse (there the individual components were non-constant). B1–B6 not engaged.
## Cheap numerics (EVIDENCE)
q = 7 (m = 3, 6), q = 13 (m = 3, 4), A ∈ {T, T², T²+1, T(T+1)}, n = 3, 4, P prime and P = Q³, Q²: 10 000+ solutions;
Weil reciprocity holds on all; odd parts identically 0 at every place; 2-parts only at ∞ and P. (R181: reproduced
independently by `scripts/review_dr_bl.py`; 15 934 solutions at odd m in DRINFELD_ES §2.)
## Assessment
PROVED negative with exact scope (monic integral points, P a prime power, q odd). Promise 1; the decomposition
pinpoints the two ES inputs (target −1, sign normalisation) — see bsH_twisted_targets.
