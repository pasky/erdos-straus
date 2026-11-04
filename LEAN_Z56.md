# LEAN_Z56 — Lean formalisation: coordinate-form certificates, HC, Theorem Q, Prop 3.1 (wave z56, lane LEAN)

**ES is OPEN; nothing here proves it.** All statements below are machine-checked in Lean 4 (v4.34.1) + mathlib
(`d13f23b7…`, same pin as Z1546). There is no `sorry`, no `native_decide`, and no axiom beyond Lean's standard three.
File: `lean/ES/ES/HC.lean` (namespace `ESHC`; the paper proofs are written step by step in its module doc comment, in
the order the Lean proofs follow). Axiom audit and sanity examples: `lean/ES/ES/AxiomsHC.lean`.

## Discrepancies / scope findings (read first)

**No discrepancy was found.** Every repo statement formalised here was accepted as stated. Lean shows that some
hypotheses are not needed:

1. **FABLE Theorem 1** (`LOWERTAIL_ROUND2_FABLE.md` §1.1, second form) is proved in **both** directions for every
   n ≡ 1 (mod 4), with no coprimality and no primality. The brief only asked for (⇐).
2. **Z53_UPPER Lemma 1.1 (U)/(T)** needs no hypothesis c ≥ 2. For c = 0 both sides are false. For c = 1 the
   divisor d = cu − 1 = 0 cannot occur, because a word with tu = 1 does not exist.
3. **HCKILL Lemma 1.1** ("HC > 4 ⟺ p + 4 ∈ S and 4p + 1 ∈ S") holds for every n ≡ 1 (mod 8), prime or not. The
   sanity example n = 9 shows this: 13 and 37 are in S, so HC(9) > 4.
4. **UPPER2 Prop 3.1 (a), (b)** need neither primality nor p > 7. The six words and their integrality follow from the
   stated congruences alone. Primality and p > 7 are used only in (c), to get p coprime to 105.
5. **Theorem Q** is proved as stated: 4 ∣ m and p = 5m² + 1 prime imply p ≡ 1 (8), 12 ∣ m, p + 4 ∈ S, 4p + 1 ∈ S and
   HC(p) ≥ 7. The least member p = 6481 (m = 36) is checked as an example.

## Definitions (Lean ↔ paper)

| Lean | paper |
|---|---|
| `Word n t u v := 0<t ∧ 0<u ∧ 0<v ∧ t*u*v = n+u+v` | word (t, u, v) of n: tuv − u − v = n (FABLE §1.1) |
| `InC n x := 4 ∣ x ∨ (x+n) % 8 = 0` | x ∈ 𝒞_n (x ≡ 0 (4) or x ≡ −n (8)) |
| `Slot t u v := 4∣t ∨ 4∣u ∨ 4∣v ∨ 4∣t*u−1 ∨ 4∣t*v−1` | the five slots (t, u, v, A, A*) |
| `IsCoord n x := ∃ t u v, Word n t u v ∧ (t=x ∨ u=x ∨ v=x)` | x is a coordinate of a word of n |
| `HCle n X := ∃ x ≤ X, InC n x ∧ IsCoord n x` | HC(n) ≤ X (HC = least coordinate in 𝒞_n, FABLE §3.1); "HC(n) > X" is `¬ HCle n X` |
| `Fires n x := (∃ d ∣ n+x, x ∣ d+1) ∨ (∃ d ∣ x*n+1, x ∣ d+1)` | line x fires (HCKILL §0) |
| `S N := 0<N ∧ ∀ prime q ∣ N, q % 4 = 1` | S (HCKILL §0) |

`ES.ESProp n := ∃ x y z > 0, 4xyz = n(xy+yz+zx)` comes from Z1546 (`ES/Basic.lean`; `ES.ESProp_iff_rat` gives the
equivalence with 4/n = 1/x + 1/y + 1/z).

The Lean statements in `HC.lean` that use `t*u − 1` match the paper exactly: every word has tu ≥ 1, so the natural
subtraction is exact.

## Statements, all PROVED

### (a) Coordinate-form certificate ⟹ ES

* `ES_of_slot (0<n) (Word n t u v) (Slot t u v) : ESProp n`: the **five slot formulas**, each an explicit identity.
  - t = 4s gives (suv, nsu, nsv).
  - v = 4w gives (wA, nwt, nwtA); u = 4w is the same with u and v swapped.
  - A = tu − 1 = 4a gives (av, avA*, naA*); A* = 4a is the same with u and v swapped.

  These are the same formulas as `scripts/z52_bank_i3c_check.py`'s `slot_identity` and FOREST_DEEP_FABLE Cor C. Each
  is checked by `linear_combination` from A·v = n + u, A·A* = tn + 1 and A* + 1 = tv (`Word.numer`,
  `Word.numer_mul`).
* `slot_iff_coord (n%4=1) (Word n t u v) : Slot t u v ↔ (InC n t ∨ InC n u ∨ InC n v)`: **FABLE Theorem 1, both
  directions**. The proof reduces to `core8`, the finite check over (ℤ/8)³ done by `decide`, which is FABLE's 160-cell
  certificate L1. The reduction casts the word equation, A, A* and both predicates into ZMod 8.
* `ES_of_coord`, `ES_of_isCoord`, `ES_of_HCle`: for n ≡ 1 (4), a word with a coordinate in 𝒞_n gives `ESProp n`. In
  particular HC(n) < ∞ ⟹ ES(n).
* `ES5_iff_HC_finite`: for n ≡ 1 (4), ES₅(n) (some word has a slot) ⟺ HC(n) < ∞ (FABLE §3.1).
* **Z53_UPPER Lemma 1.1:**
  - `coordU_iff n c`: (∃ t v, Word n t c v) ⟺ ∃ d, d ∣ n + c ∧ c ∣ d + 1 (line U).
  - `coordT_iff n c`: (∃ u v, Word n c u v) ⟺ ∃ d, d ∣ cn + 1 ∧ c ∣ d + 1 (line T).
  - `isCoord_iff_fires`: IsCoord n x ⟺ Fires n x.
  - `ES_of_lineU` and `ES_of_lineT` give the line form of "certificate ⟹ ES": c ∈ 𝒞_n, a divisor d ≡ −1 (mod c) of
    n + c (resp. cn + 1) ⟹ ESProp n.

### (b) Theorem Q (Z54_HCKILL §2.1)

* `theoremQ (4 ∣ m) (p = 5m²+1) (p prime) : p % 8 = 1 ∧ 12 ∣ m ∧ S (p+4) ∧ S (4p+1) ∧ ¬ HCle p 6`. The last conjunct
  is HC(p) ≥ 7.
* `theoremQ_no_line4`: 4 is not a coordinate of any word of such p, i.e. line 4 does not fire.
* Ingredients:
  - `S_sq_add_one`: j even ⟹ j² + 1 ∈ S, via mathlib `ZMod.mod_four_ne_three_of_sq_eq_neg_one`.
  - `S_mul`, `S_five`.
  - The identities p + 4 = 5(m² + 1) and 4p + 1 = 5((2m)² + 1).

### (c) HCKILL Lemma 1.1

* `HC_gt_four_iff (n%8=1) : ¬ HCle n 4 ↔ (S (n+4) ∧ S (4n+1))`.
* Ingredients:
  - `dvd_mod_four_of_S`: every divisor of an element of S is ≡ 1 (4), by induction on the factorisation.
  - `exists_dvd_three_iff`: an odd N has a divisor ≡ 3 (4) ⟺ N ∉ S.
  - `InC_small`: for n ≡ 1 (8), 𝒞_n ∩ [1, 6] = {4}.
  - `HCle_four_iff`, `HCle_six_iff`: HC(n) ≤ 4 ⟺ HC(n) ≤ 6 ⟺ 4 is a coordinate.
* Small values:
  - `HC_gt_two`: HC ≥ 3 for n ≡ 1 (4).
  - `HC_gt_three`: HC ≥ 4 for n ≡ 1 (8).

### (d) Z54_UPPER2 Proposition 3.1

* `prop31a`: for p ≡ 5 (8), the word (1, 3, (p+3)/2) and HC(p) = 3 (`HCle p 3 ∧ ¬ HCle p 2`).
* For p ≡ 1 (8), each word is stated exactly as in the paper, Nat-division formulas included:

  | Lean | condition | word | conclusion |
  |---|---|---|---|
  | `prop31b_mod3_2` | p ≡ 2 (3) | (1, 4, (p+4)/3) | HC = 4 |
  | `prop31b_mod7_3` | p ≡ 3 (7) | (2, 4, (p+4)/7) | HC = 4 |
  | `prop31b_mod7_5` | p ≡ 5 (7) | (4, 2, ((4p+1)/7+1)/4) | HC = 4 |
  | `prop31b_mod5_3` | p ≡ 3 (5) | (3, 7, (p+7)/20) | HC ≤ 7 |
  | `prop31b_mod5_2` | p ≡ 2 (5) | (7, 3, ((7p+1)/20+1)/7) | HC ≤ 7 |
  | `prop31b_mod7_6` | p ≡ 6 (7) | (1, 8, (p+8)/7) | HC ≤ 8 |

  Here "HC = 4" is `HCle p 4 ∧ ¬ HCle p 3`.
* `HC_le_eight_of_nonresidue`: p ≡ 1 (8) and p a non-residue mod 3, 5 or 7 ⟹ HC(p) ≤ 8.
* `prop31c`: for every prime p > 7, p ≡ 1 (4), p mod 840 ∉ {1, 121, 169, 289, 361, 529}, HC(p) ≤ 8. ES at such p
  follows through `ES_of_HCle`.
* `cls840` is the CRT core, checked by `decide` over Fin 840.
* `prop31c_classes`: the six excluded classes are exactly the residues ≡ 1 (8) that are quadratic residues mod 3, 5
  and 7.

## Axioms (`lean/ES/ES/AxiomsHC.lean`, `#print axioms`)

31 theorems are audited.

* 26 report `[propext, Classical.choice, Quot.sound]`.
* `coordU_iff`, `HC_gt_two` and `HC_gt_three` report `[propext, Quot.sound]`.
* `cls840` and `prop31c_classes` depend on no axioms.

The Z1546 audit in `ES/Axioms.lean` is unchanged. There is no `sorry` and no `native_decide`; `core8`, `cls840` and
`prop31c_classes` use kernel `decide`.

Sanity examples, all checked:
* the word (7, 2, 15) of 193 gives `ESProp 193` through Theorem 1 (level 7 ≡ −193 (mod 8));
* Theorem Q at m = 36, p = 6481;
* HC(9) > 4 through Lemma 1.1 at a non-prime.

## Not formalised

* The Jacobi-symbol form of Theorem 1, (uv/n) = −1 ⟺ …, which uses FOREST_DEEP_FABLE Theorem A.
* The infinitude statements: Bunyakovsky for 720k² + 1 and K(4).
* The census and certified computations.
* The coordinate bound Lemma 1.2 of Z53_UPPER.

## Build

```
cd lean/ES
# .lake/packages copied from a sibling worktree at the same pins (or `lake exe cache get`)
systemd-run --user --scope -p MemoryMax=16G timeout 3600 lake build    # ~15 s once mathlib oleans are present
```
As recorded in LEAN_Z1546 (re-confirmed in z56), `ulimit -v 16000000` makes Lean abort ("failed to create thread"), so a cgroup memory cap was
used instead. `.lake/` is gitignored.
