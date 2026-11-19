# Ordinary-prime and weak-arithmetic checks after z73

**ES remains open in the ordinary integers.** Two different questions drove this round: can one *produce* an ES triple from another arithmetic witness, and can one *prove* that a specified method cannot do this universally? The counterexamples below are counterexamples to methods, not to ES. All proofs have only internal review.

## A positive transfer and its limit

At `p=9565921`, both proposed denominators fail at the two root-eligible shifts 11 and 23. Nevertheless the same factorization `199291=323·617` gives triples for both `(p+11)/12=797161` and `p`: `323≡−1 mod 3`, `323+617=20·47`. The target triple is `(2391492,741550195920,1416521581680)`. Its first entry is 12 times the smallest *possible* donor slot. At `p=6206649121` both candidate denominators fail at 11, 23 **and** 47, and even the donor fails at its minimum slot. See `SIGNED_ROOT_TRANSFER.md`. For a correction changing only one denominator, `Z74_ONE_SLOT.md` proves an obstruction: if `p=kQ−d` with `d>0` and `p∤kQ`, the changed donor slot must already be divisible by `p`. `Z74_PRIMITIVE_TRANSFER.md` exhibits successes and distinguishes the reverse direction.

A separate exhaustive falsifier: for `p=214729`, **every** divisor `D|(p−1)/4` fails in **both** prescribed slots `(p+c)/4` and `p(pc+1)/4`, `c=4D−1`, with no sign filter. There are exactly 16 such `D`. `DIVISOR_SHIFT_CERTIFICATE.md` is unconditional; the infinitude statement in `DIVISOR_SHIFT_DOUBLE_MISS.md` assumes Dickson. `CF_ADDITIVE_NEIGHBOUR.md` distinguishes complete denominators of √p (their prime factors split) from their additive neighbours (which can supply actual triples). `CF_SHIFT_SLOTS.md` gives an exact short-period failure and replay.

## What polynomial formulas cannot do

`GAUSSIAN_PELL_MENU.md`: fix a finite list of triples of rational-coefficient **polynomials**, using a representation `p=a²+b²` and any fixed finite number of integral solutions of `x²−py²=−1`. Even if a selector may choose **any** such input tuple and any entry of the list after seeing `p`, there is a computable `M` divisible by 840 such that the number of successful primes `p≤B, p≡1 mod M` is `O_menu(B^(3/4) log(2B))`. Since that progression contains asymptotically `B/(φ(M) log B)` primes, the relative density of misses there is one. This is about the **output formulas for whole triples**; it does not rule out choosing divisors, Euclidean algorithms, or ES solutions outside the menu. For Pell data alone, `PELL_ES_MENU_NOGO.md` and `PELL_ES_MULTI_MENU.md` give an entire progression of misses. `PELL_ES_MULTI_HEIGHT.md` quantifies the coefficient-size cost at fixed degree and arity.

`PELL_RATIONAL_MENU_AUDIT.md` and `PELL_RAMIFIED_MENU_AUDIT.md` separate unconditional ordinary-prime results for restricted rational formulas, the conditional general-prime result, and an unconditional construction at prime powers. Do not label the general rational-function result at primes unconditional. `PELL_REMAINDER_SELECTOR.md` and `PELL_RESIDUE_INTERFACE_AUDIT.md` give the other boundary: with a free choice of power, a normalized Pell coordinate runs through every residue modulo `n^k`. This encodes a bounded choice; it does not tell us which choice solves ES.

## Model-theory boundary

`LOGIC_PELL_UNIT_GROUP.md`: the distinguished ES-failing nonstandard prime of the joint PID construction can have a least positive negative-Pell witness with both coordinates infinite; the negative solutions are explicitly the positive odd powers of a fundamental unit. `LOGIC_NEGATIVE_PELL_TS_TEST.md` is a **separate** normal open-induction model with Lagrange, positive Pell for all positive nonsquares, and negative Pell and two squares for all positive irreducibles `1 mod 4`. Do not transfer external factoriality or prime-element Dirichlet to that second model.

`LOGIC_LAG_END_MULTIPLE.md` and `LOGIC_LAGRANGE_END_TEST.md`: one end extension preserves the old prime and ES failure, and adds a common multiple of **every positive element of the old ring**, while retaining open induction and Lagrange. Its new positive cutoffs do not all have common multiples. Compatibility in an iterated construction is an open step, not an automatic consequence of the one-step theorem. None of these results proves independence from PA or ZFC.

## Exact replays

```
uv run --offline --no-project python scripts/cf_shift_slots.py
uv run --offline --no-project python scripts/divisor_shift_certificate.py
uv run --offline --no-project python scripts/signed_root_transfer.py
uv run --offline --no-project python scripts/pell_residue_interface_audit.py
```

These check finite certificates; the infinite statements rely on the proofs and named theorems cited in the individual notes.
