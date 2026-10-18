# z35_gaussian_qnr_linear_forms — T1 steering in ℤ[i]: what distinguishes π from α² (O265)

## Idea
Brief's steering question: what distinguishes a prime's unique primitive representation from a square's? Answer: primitive
representations of m² are i^j α² (α ∈ ℤ[i]), so every Gaussian quadratic symbol [λ/α²]_2 is +1; for a prime π half of them are
−1. So a Gaussian mechanism must consume a Gaussian non-residue. But [λ/π]_2 for λ = c + ei equals ((cb − ea)/p)·(b/p), since
i ≡ −a/b (mod π) — a rational Legendre symbol of the LINEAR FORM A = cb − ea in (a, b) (size ≍ |λ|√p). So Gaussian non-residues
are rational non-residues of linear forms in the representation, and DEDEKIND_ES Cor 4.6 (ES-five ⟺ a non-residue at Farey
distance ≤ 3, i.e. A ∈ L₃(p) = {tu − 1 : tu − 1 | p + u}) would need A = cb − ea ∈ L₃(p): a divisor event (cb − ea) | p + u, B2.

## Literature
DEDEKIND_ES Thm 4.5/Cor 4.6; POINTWISE_BINARYFORM Lemma 2.2 (Gaussian square classes detected by the norm); quadratic
reciprocity in ℤ[i] (Lemmermeyer Ch. 5).

## Barrier screen
T1 is passed (squares have no Gaussian non-residues), but the reduction to linear forms shows the Gaussian layer carries no
quadratic information beyond rational Legendre symbols of linear forms in (a, b) — which by reciprocity are functions of
(a, b) mod N(λ) (congruence data in the Gaussian variables). Membership in L₃(p) is B2.

## Cheap numerics
None needed (the reduction is an identity); the anti-window numerics (z35_anti_windows) cover the linear forms a, b, a ± b.

## Assessment
PROVED (one-line identity) — a precise answer to the T1 steering question, negative as a route.
