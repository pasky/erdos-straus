# z5_cap_dimension — the exponent cap as a sieve-dimension knob (O229; deep file CAP_GROWING.md §1)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
R200 M1 asks about ES^{(y,e)}: bounded cap e, mute set S = rad(den z)^{1/2} unrestricted. Pointwise this is a lottery
with no archimedean wall (GROWING_MUTE, CAP_TWO). Steering: the only barrier hypothesis that a growing S honestly
violates is the *class count per modulus* — at a prime modulus ℓ ≡ 3 (4) the cap-e shots are the odd Q with
Q^{(e)} := ∏ s^{max(1, v_s(Q)−e)} | (ℓ+1)/4, and Σ_ℓ ω_e(ℓ)/ℓ ≍ (log X)^{e+1}. Feed this into Vaughan's large sieve.

## Literature
Vaughan, Mathematika 17 (1970) (ES exceptional set N exp(−c log^{2/3} N)); Pomerance–Weingartner arXiv:2511.16817
Thm 1.3 (self-contained account); Montgomery's arithmetic large sieve; Bombieri–Vinogradov with divisor-bounded
weights. Campaign: paper/vaughan-loglog-note.tex (exponent 2/3 with (log log)^{1/3}); EXPONENT_CAP Prop 1.2 (cap-e
condition g ≡ −1 mod 4Q^{(e)}).

## Result
**Upgrade (CAP_GROWING Prop 1.3 + Thm 1.4): the Type II cube with overflow (c, d) = (c₀R², d₀/R²) gives
exponent (e+2)/(e+3) (e = 0: Vaughan's 2/3; e = 1: 3/4; e = 2: 4/5); 3 194 overflow-cube solutions verified exactly.**
Shot-only version:
**Thm (CAP_GROWING Thm 1.2; PROVED relative to BV + large sieve).** #{p ≤ N : ES^{(y,e)}(p) fails}
≪_e N exp(−c_e (log N)^{(e+1)/(e+2)}). Shots alone: e = 0 → 1/2, e = 1 → 2/3 (= Vaughan, who needs the whole Type II
cube), e = 2 → 3/4 (beats Vaughan), … ES^{[2]} ("den z | y²", condition ∏ s^{⌈v_s/2⌉} | K) has local factor
1 + 2/s, i.e. exponent 2/3 — on average cap-2-with-free-S is *richer* than den z | y² (Assessment from the local
factors; not separately written out).

## Barrier screen
B6: it is an average statement and claims nothing pointwise. B1/T1: odd squares avoid every class (−4Q² is a QNR mod
ℓ ≡ 3 (4)); consistent with the ≍ √N squares. B3: irrelevant (average). Large-sieve ceiling: with ω(ℓ) ≤ (log ℓ)^{O(1)}
no fixed e gives power saving; e → ∞ is not uniform (c_e decays). Thm 9.1 / Prop 10.3: not applicable (no identity,
no form-class mechanism).

## Cheap numerics
`scripts/z5_cap_classes.py 2000000 3 200`: S₀/log X ≈ 0.28–0.30 flat; S₁ ≈ 0.018 L² + 0.21 L; S₂, S₃ grow faster;
140 random cap-3 shot solutions verified exactly (Def 1.1 prime by prime).

## Assessment
PROVED (relative to classical inputs), modest novelty: the first quantitative statement separating bounded-cap /
free-S from ES itself (on average). Not a route to ES: the cap is exactly what ES forbids (e = 0 gives 1/2 with shots).
