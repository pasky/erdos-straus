# z16_sibling — the sibling conjecture: three tuple balls never fill an alive cylinder (O241)

## Idea
By the windowed König lemma (z16_windowed_konig) O(3, T²) ≠ ∅ — the conclusion of Conjecture 0.2, not x*_c ∈ O (R248 repair
D10) — follows from: **no alive cylinder V of depth n ≥ 3 in X_c
has all three children equal to tuple balls** (three families of level n − 1 whose −E agree mod T^{n} on V's digits and take
all three values of the T^{n}-digit). Even "≤ 1 covered child" would give dim U_c ≥ log 2/log 3.

## Literature
Galton–Watson survival (Lyons–Peres ch. 5); second-moment/pair-correlation counts for divisors in residue classes
(function-field Lenstra/Coppersmith, FF_STERILE_PUSH Lemmas 1.4, 1.5) — the needed input would be a *pair* count.

## Barrier screen
A sibling pair at depth N + 1 is a pair of tuples with E₁ ≡ E₂ (mod T^N), E₁ ≢ E₂ (mod T^{N+1}): a two-tuple lottery. Gap
principle (STERILE_DIOPHANTINE Lemma 4.1) gives only N ≤ H₁ + H₂, no contradiction at the thirds corner (H ≈ 2N/3). Route
bounds count single tuples, so B3 recurs unless one proves pair/triple correlation bounds. Not a congruence covering (B1).

## Cheap numerics
Depth ≤ 9 (complete): no triple, two pairs among alive parents (both at depth 6). Independence model with observed (unconditional) ball masses:
expected triples beyond depth 9 ≈ Σ_d 3^{d−3}p_d³ ≈ 10⁻³ (decaying ×1/3 per level); the conditional fractions (R248 repair D9)
2/132, 10/390, 10/1140 at depths 7–9 give the same order. Weaker sufficient form (R248 repair D11): the condition only for alive
V ⊂ V₀ of depth ≥ n₁, for some alive V₀ of depth n₁.

## Assessment
CONJECTURE (EVIDENCE to depth 9). Much weaker than the union bound but not provable with present tools; it isolates a
positional input that would prove O(3, T²) ≠ ∅ (sharper per-depth counts would be another route, R248 repair D3).
