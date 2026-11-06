# Z60_LOPEZ — the single-line target U_II (López's Conjecture 1): joint structure of the two branches

**ES is OPEN; López's Conjecture 1, CONJECTURE U_II and (MS-U) are open.** Lane LOPEZ of wave z60
(`z52bbriefs/z60_lanes.md` §LOPEZ; rules `z58_lanes.md` "Common rules" + falsifier table; `z53_depth.md` with z53 → z60).
Scripts `scripts/z60_lopez_*`, data `data/z60/lopez/`. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Status: **CHECKPOINT 1** (skeleton; sections marked TODO are not done).

Notation (`Z59_SUMMARY.md`, `Z59_CONV2.md`). n odd ≥ 1. **Branch B** = (★) = c = 1 line = López Type B; **branch A** =
a = 1 (∪ b = 1) line = López Type A. U_II(n) ≥ 1 ⟺ branch A or branch B has a solution at n. 𝔐 = {1, 121, 169, 289, 361,
529} ⊂ (ℤ/840)^×. For f ≡ 3 (mod 4): m_f = (f+1)/4, D_f = {a mod f : a | m_f}.

## 0. Mandatory falsifier table (checkpoint form; to be re-stated at the end)

Object: the lane's *idea* = a deterministic "link law" between the branches (if branch A fails up to X then branch B fires
by g(X), or vice versa), and the reformulations of Lemma L.

| screen | behaviour of the idea | status |
|---|---|---|
| F1 odd squares | Both branches vanish at every odd square (T1; in Lemma L(J) form: every target residue is a Jacobi **+1** divisor of f + 1, while −m² is a Jacobi −1 residue mod f ≡ 3 (4)). A link law that does not use non-squareness at an identifiable step is false at n = m² (both branches fail for every X). | PROVED (T1 in L(J) coordinates) |
| F2 numerator 8 | U⁽⁸⁾ has 547 odd non-square zeros n ≡ 1 (4) ≤ 10⁸ (45 primes, last 3 869 153) (Z59_CONV2 F2). A link law valid verbatim for K = 8 proves a false statement unless its threshold exceeds 3 869 153 (primes) / 89 530 945 (n ≡ 1 (4)). | CERTIFIED (inherited) |
| F3 composites | U_II vanishes at 105 and 4545 (≤ 10¹⁰). A link law must fail (or have its hypothesis fail) at both. | CERTIFIED (inherited; L-forms re-checked to 6000) |
| F4 known zeros | Branch B fails *totally* at the 14 (★)-zero primes; branch A fails totally at 193, 2521, 66529. So neither "B always fires" nor "A always fires" holds; a law must be genuinely two-sided. | CERTIFIED (inherited) |

## 1. Precise statements attacked

* **López's Conjecture 1** (arXiv:2404.01508v3, Conjecture 1, read from `sources/lit2026f/r270-lopez-2404.01508v3-html.md`):
  for every prime p there are d, n ∈ ℕ with p ≡ −4d (mod 4dn − 1) [Type A, his Thm 7] or p ≡ −n (mod 4dn − 1) [Type B, his
  Thm 4]. López verified it for the first 10 000 primes.
* **CONJECTURE U_II** (Z59_CONV2): every odd non-square n ∉ {105, 4545} has U_II(n) ≥ 1. CERTIFIED to 10¹⁰.
* **(MS-U)**: U_II(p) ≥ 1 for every prime p > 10¹⁷ in 𝔐. (MS) ⟹ (MS-U) ⟹ (MS-II); (MS-U) + Mordell + Salez ⟹ ES.
* **Lane question.** Is there a pointwise mechanism specific to U_II — an algebraic link between a failure of one branch
  and a success of the other — e.g. a law "branch A has no witness of size ≤ X ⟹ branch B has one of size ≤ g(X, p)"?

Why not closed: CONV2 Prop 3.1 (nesting on shared integers) and the fixed-finite-menu obstruction exclude only
p-independent menus and same-integer rescue; adaptive / p-dependent links across *different* integers are explicitly open
(Z59_SUMMARY §5 item 1).

## 2. Lemma L (equivalent forms of U_II; PROVED, checked)

**Lemma L.** For odd n ≥ 1 the following are equivalent to U_II(n) ≥ 1:
* (iii) [CONV2 Lemma 1(iii)] ∃ T ≥ 1: Tn + 1 has a divisor f ≡ −1 (mod L_T), L_T = T if 4 | T, else 4T.
* (P) (paired shift form) ∃ a ≥ 1: **n + a or n + 4a** has a divisor f ≡ −1 (mod 4a). (Branch B at a; branch A at a.)
* (J) (Jacobi form) ∃ f ≡ 3 (mod 4) with (n/f) = −1 (Jacobi) such that r := (−n mod f) divides **f + 1**.
* (X) (letter form) n = xyz − x − z with x, y, z ≥ 1 and 4 | x or 4 | y or 4 | z.

CERTIFIED cross-check: (iii), (P), (J), (X) agree for every odd n ≤ 801; (P) and (J) give exactly the non-square zeros
{105, 4545} among odd n ≤ 6000 (`scripts/z60_lopez_forms.py`).

*Proof.* TODO (written out in the final memo).

*Prior art / what is new.* (X) is the formal-word form of HJ_DEEP Prop 2.1 / DK's five slices restricted to the three
Type II slices 4 | t, 4 | u, 4 | v (HJ_DEEP; Lorenzini's critical polynomial xyz − x − z, LORENZINI_W). (P) is a
re-indexing of CONV2 Lemma 1(iv). The sign-free part of (J) is LORENZINI_W (F3). New (as far as `git grep` shows): (J) —
the profile L_T is exactly the *Jacobi completion*: among divisors r of f + 1, the U_II targets are precisely those with
(r/f) = +1; the two branches are the 2-adic halves r | m_f (B) and 4 | r (A) of this one set.

## 3. Joint structure of the branches at hard primes — TODO (first falsifier: does any p-independent or mildly
p-dependent link law survive the data?)

## 4. Link laws: what is and is not possible — TODO

## 5. Census extension — TODO

## 6. Verdict, falsifier table restated, FRONTIER text, bottom line — TODO
