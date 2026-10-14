# y7_free_inert — the free slices of M/p are exactly the inert primes of ℚ(√−M) iff M ∈ {4, 6, 7} (O215, goal (b))

## Idea
A slice with e ∈ {1, 2} is *free*: its condition e | a + b is met by a = b = 1 (e = 2: c = 1; e = 1: c = 2), so it fires
whenever its N = (p+e)/M (Type II) or (pe+1)/M (Type I) is an integer. Free classes of p mod M: −1, −2, −2⁻¹. Compare
with the classes where p is inert in K_M = ℚ(√−M), i.e. χ_{−M}(p) = −1.

## Result (PROVED; exhaustive for M ≤ 60 in `scripts/y7_free_inert.py`, and |free| ≤ 3 forces φ(M) ≤ 6 in general)
The uncovered ("hard") classes mod M are exactly ker χ for an odd quadratic character χ mod M iff **M ∈ {4, 6, 7}**
(χ = χ_{−4}, χ_{−3}, χ_{−7}); for M = 3 every class is free. So for M ∈ {4, 6, 7}:
**M/p is trivially solvable at every prime inert in ℚ(√−M), and the open problem is exactly the split primes**
(p = x² + y², x² + xy + y², x² + xy + 2y² respectively). For 4 this is the classical reduction to p ≡ 1 (mod 4).
Why 7: χ_{−7}(−1) = −1 and χ_{−7}(2) = +1 (2 splits), so −1, −2, −2⁻¹ all lie in the non-residues {3, 5, 6}, which they
fill. For 11, −2 and −2⁻¹ are squares mod 11 (2 is inert in ℚ(√−11)), so the free slices hit split classes and leave 4
of the 5 inert classes hard; 8 has one free class (7) of 4; 12 has one (11) of 4.

## Comparative table (failure data: PW Table 1 to 10¹²–10¹⁸, census to 10⁸; T1 from y7_full_t1)
| M | free/units | hard = split in ℚ(√−M)? | full T1 | identity core at 840 (y7_mordell_levels) | failures (odd p ∤ M) |
|---|---|---|---|---|---|
| 3 | 2/2 | — | no | ∅ | none |
| 4 | 1/2 | **yes** | **yes** | squares | none (≤ 10¹⁸) |
| 5 | 3/4 | no ({1}) | no | class of one mod 420 | none (≤ 10¹⁸) |
| 6 | 1/2 | **yes** (ℚ(√−3)) | no | 11 classes | none (≤ 10¹³) |
| 7 | 3/6 | **yes** | no (shot subfamily only) | class of one mod 105 | none (≤ 10¹³) |
| 8 | 1/4 | no | yes | squares + 17 | 3, 11, 17, 131, 241 |
| 11 | 3/10 | no | no | (at 9240) 28 classes | 37 |
| 12 | 1/4 | no | yes | squares + 38 | 20 primes |
P_free(M) ("hard ⟺ split in ℚ(√−M)") holds for 4, 6, 7 and fails for 8, 11, 12; the failure-free 5 also fails it
(its hard set is the single class 1, even smaller). So P_free is not necessary for being failure-free.

## Barrier screen
P_free is a statement about which residue classes are trivial: B1. It is a description, not an input: on the split
primes nothing is gained. It does give 7/p a "Fermat-type" reduction like 4/p, so a 7-proof could start from
p = N(π), π ∈ ℤ[(1+√−7)/2] (class number 1). See y7_split_norm.

## Assessment
PROVED (elementary). Description only. It is the cleanest true sense in which 7 is "4's sibling": both reduce
to the primes that split in their own class-number-one field, and only for 4, 6, 7 is the reduction exact.
