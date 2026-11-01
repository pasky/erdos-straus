# Z53_WILDCARD — from-scratch attack on the tied divisor event

**ES is OPEN; nothing here claims it proved or disproved.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Status: **Checkpoint 1 (idea list, pre-FRONTIER)**. Lane rule: ideas generated before reading
FRONTIER §§3–4, §6; the barrier check comes in §4 below.

## 0. The statement attacked

(★) For a prime p ≡ 1 (mod 24) find positive integers u, B, C with p = 4uBC − u − B; equivalently (PROVED, trivial)
any one of
* ∃ C and d | 4Cp+1 with d ≡ −1 (mod 4C);
* ∃ u and d | p+u with d ≡ −1 (mod 4u) (then B = (p+u)/d, C = (d+1)/(4u));
* ∃ coprime u,B with u | p+B, B | p+u and 2^{2+v₂(uB)} | p+u+B;
* ∃ d ≡ 3 (4) such that ρ_p(d) := (−p mod d) ∈ [1,d−1] divides (d+1)/4.

Necessary condition (PROVED, 5 lines, §2.1): any such d has (d/p) = −1. For n = q² an odd square every candidate
fails because (−u/d) = −1 for every d ≡ −1 (4u) while every divisor of q²+u has (−u/d)=+1 (this is the T1 wall
restated; proof in §2.1).

## 1. Idea list (generated from scratch, before reading FRONTIER §§3–4/§6)

Each with a first concrete test. (Status filled in later sections.)

1. **Full Type II family, not only (★).** Deriving Mordell/Elsholtz–Tao Type II from scratch gives
   hp = 4ahkC − a − k (h,a,k,C ≥ 1); (★) is h = 1. Equivalent forms (PROVED §2.2): ∃ a,h: hp+a has a divisor
   ≡ −1 (mod 4ah); ∃ a,C: p+4a²C has a divisor ≡ −1 (mod 4aC); ∃ g, h|g: 4ghp+1 has a divisor ≡ −1 (mod 4g);
   ∃ t ≡ 3 (4), a,b with ab | (p+t)/4 and t | a+b. Expected count ≍ log³p (vs log²p for (★)); the modulus of the
   divisor condition is relaxed from 4u to u/a when a² | u/4 (e.g. p+4a² needs only a divisor ≡ −1 mod 4a).
   Test: which p ≡ 1 (24) (and which non-squares n) have Type II but no (★); compare minimal parameters.
2. **Type I family** tp+1 = 4abC with t | a+b (derived §2.3); a=1 slice: (tp+1)/4 has a divisor ≡ −1 (mod t).
   Dual to Type II a=1 slice ((p+t)/4 has a divisor ≡ −1 mod t). Test: same census.
3. **Characterise the (★)/Type-II exceptional set among non-squares.** If the only n ≡ 1 (24) without Type II are
   squares, primality is used only through non-squareness; otherwise the extra exceptions show exactly what a proof
   must use. Test: census n ≤ 10⁶–10⁷.
4. **r-spectrum R(n) = {r : rn+1 has a divisor ≡ −1 (mod r)}** (r=1,2 always; ES ⟺ R(p) ∩ 4ℤ ≠ ∅; for squares
   R(q²) ⊆ {r ≡ 1,2 (4)}, PROVED §2.1). Test for a composition law / multiplicative structure on R(n) numerically.
5. **Covering-system view**: the APs {n ≡ −(u+B) mod 4uB} must cover all primes ≡ 1 (24); large sieve with
   non-CRT targets on composite moduli — compare with Vaughan/Elsholtz exceptional-set bounds (density only;
   expected dead for individual p, but check whether the half-dimensional structure (d/p) = −1 adds anything).
6. **Genus/ray-class reformulation**: d | 4Cp+1 ↔ ideal divisors of (1+2√(−Cp)); condition d ≡ −1 (4C) is a ray
   class condition, (d/p) = −1 a genus condition. Test whether anything beyond genus theory is captured.
7. **Polynomial identities in a quadratic-form parametrisation of p** (forms outside the principal genus never take
   square values, so T1 does not forbid them a priori). PROVED dead by degree count (§2.4): only congruence menus.
8. **Mutual-divisibility graph / Vieta-type moves**: u | p+B, B | p+u. Checked: no Vieta jump (equation linear in
   each variable); the ratio r = (p+u+B)/(uB) classifies edges, ES needs 4 | r.
9. **Sierpiński/Proth slice** C = 2^j: p·2^{j+2}+1 needs a divisor ≡ −1 (mod 2^{j+2}). Test numerically whether
   this slice alone always succeeds for small p (expected not).
10. **Davenport-constant / zero-sum argument** on the multiset of prime residues of p+u in (ℤ/4u)*: only bites when
    ω(p+u) ≳ |G|; fails for typical u. Noted, not pursued.
11. **Probabilistic/LLL, Chevalley–Warning, circle method, modular forms**: all reduce to counting with error ≫ log²p
    or give mod-p information without size control. Dead on first inspection (reasons in §2.5).

## 2. Derivations

(to be filled in, one per section: 2.1 Jacobi obstruction and (d/p) = −1; 2.2 full Type II; 2.3 Type I;
2.4 degree-count kill of identities; 2.5 one-line kills)

## 3. Computations

(scripts/z53_wildcard_*, data/z53/wildcard/)

## 4. Barrier check against FRONTIER §§3–4, §6

(after the computations)

## 5. Verdict / proposed §7 text

(pending)
