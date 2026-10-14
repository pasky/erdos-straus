# R213 — hostile review of CAP_TWO.md (O214, spark relay Y6)

Reviewer: R213 (side agent, branch side-agent/review-cap-two). Reviewed commit: side-agent/cap-two as merged at start.
From-scratch scripts: `scripts/review_r213_*.py` (none reuses `y6_*`).
Repairs applied: (none yet — filled in at the end if the author is quiet).

## Summary verdict per claim

| Claim | Verdict |
|---|---|
| Thm 1.1 (k = 1 cap-2 shots ⟺ W_n, c odd) | SOUND-AFTER-REPAIRS (m1: Q₁ odd must be a hypothesis) |
| Thm 1.2 (one equation, two cells; fibre picture) | SOUND-AFTER-REPAIRS (m1(b) false "other solutions" bullet; m6 halves overlap as shot sets; m7 fibre picture is a necessary condition) |
| Prop 2.1 (a)(b)(c) (slices finite, orbits infinite) | SOUND |
| §2 Reading "O204 contrast is a slicing effect" (Assessment) | SOUND-AFTER-REPAIRS (m6: wording) |
| Thm 4.1 (D-face, (i)(ii)(iii)) | SOUND |
| Thm 4.1 Example (c, w) = (1, 1) | SOUND-AFTER-REPAIRS (m2: missing gcd(a, n) = 1) |
| Prop 5.1 (finite exponent-2 budget ⇒ finite slice) | SOUND (m4: stale citation in (c)) |
| §6 no polynomial families (MARKOFF Thm 5.1 transfer) | SOUND (transfer is verbatim after μ ↦ x/2, N(η) = 4n) |
| §6 fibre EVIDENCE + Assessment | SOUND-AFTER-REPAIRS (m5: "positive proportion" overclaim) |
| §3 EVIDENCE (coverage of primes < 10⁶) | SOUND-AFTER-REPAIRS (m3: 13 402 → 13 401; "need exponent 2" overstated) |
| T1 location | SOUND |
| §7 verdict "ES^{(y,2)} at k = 1 not easier than ES^{[2]}" | SOUND as Assessment (correctly labelled; not PROVED) |

No FATAL, no MAJOR defect found. All PROVED algebra re-derived by hand and brute-forced; all numerical claims I
re-ran agree exactly except one count (m3) explained by tie-breaking.

## Checks performed

**C1 (Thm 1.1, both directions, brute force; `scripts/review_r213_dict.py 200 100000`, 2.7 s).**
Side A enumerates EVERY k = 1 shot datum (odd 3 ≤ n ≤ 200, g ≤ 10⁵, g ≡ 3 mod 4, Q = K·Q₁ with rad Q₁ | K and
v_ℓ(Q₁) ≤ 3 incl. ℓ = 2, gcd(Q, n) = 1), builds the shot solution x, y, z, asserts 4/n = 1/x + 1/y + 1/z exactly and
tests ES^{(y,2)} membership DIRECTLY from EXPONENT_CAP Def 1.1 (den z = q², q odd, gcd(q, n) = 1, rad q | y,
v_ℓ(q) ≤ 2). Side B enumerates all (a, B, c) with c, B odd, g = caB − 1 ≤ 10⁵ and solves W_n for n by the congruence.
Results: 876 k = 1 shots lie in ES^{(y,2)}; 876 canonical W_n points (c, B squarefree coprime, 4 | a,
gcd(caB, n) = 1); the two sets of (n, g, Q₁) are IDENTICAL, the map is injective, and den z = Q₁² for every member.
Among ALL 4 484 c-odd W_n points (no squarefree / coprime / 4 | a restriction) "E ≡ 3 (4) ⟺ 4 | a" holds without
exception. The n = 41 and n = 5 examples of Thm 1.2 re-derived by hand (g = 35, E = 75 / 675; g = 81, E = 1).
Hand re-derivation of the proof of Thm 1.1: correct, including the mod-4 argument.
BUT: 617 further k = 1 shots satisfy the literal CAP_TWO definition "k = 1, rad Q₁ | Q₀, v_ℓ(Q₁) ≤ 2" with Q₁ EVEN
(e.g. n = 3, g = 7, Q = 8, Q₁ = 4; n = 11, g = 23, Q₁ = 18). They are NOT in ES^{(y,2)} (q even), and they are not
in the image of W_n with c, B odd. → defect m1.

## Defects

**m1 (MINOR; Notation line and Thm 1.1 (⇒)).** The Notation says "Q₁ = Q/Q₀ (overflow, odd)" as if oddness were
automatic, and the definition of "k = 1 cap-2 shot" omits it; in the widened (Q-even) family Q₁ can be even
(617 such k = 1 shots with rad Q₁ | Q₀, v_ℓ(Q₁) ≤ 2 for n ≤ 200, g ≤ 10⁵). The (⇒) proof silently uses c, B odd.
*Repair:* define "k = 1 cap-2 shot" with "Q₁ odd" explicitly (it is exactly what ES^{(y,2)} membership requires:
q odd), and in (⇒) say "c, B odd since Q₁ is odd".
