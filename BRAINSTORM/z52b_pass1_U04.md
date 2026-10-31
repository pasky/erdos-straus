# z52b Pass 1 — batch U04 (207 untried §2 items)

**Summary (counts):** 207 items: skipped 106, covered 50, needs-compute 35, nothing 14, interesting 2.
**Interesting:** Z0866 (primitive ES failures confined to p≡1 mod 12 up to 2·10⁴: 56/555 vs 0/570 in class 5 mod 12);
Z1652 (Y. Wang, arXiv:1406.6963: almost-prime rational points on the Cayley cubic via circle method + torsors; possible fibre/class restriction).
**Nothing with a computed negative:** Z0785 (Neumann–Setzer p = u²+64 vs hard primes), Z1343/Z1444/Z0545 (subgroup/Kneser
gate: −1 in the generated subgroup but no witness, 6476 pairs), Z1508/Z2514/Z2977/Z3143 (no Hecke-type ratio relation for f(ℓp)/f(p)), Z2985 (no closure of the hard set under prime factors).
**Items needing compute (spelled out in outcome_U04.jsonl):** 35, e.g. Z1394 (run length to 10⁸), Z0705 (max log(minz/p)/log p to 10⁷), Z1369, Z2471, Z2696.

Repro: `scripts/z52b_p1_U04_*.py`; data in `data/z52b/pass1/U04/`; outcomes `data/z52b/pass1/outcome_U04.jsonl`.
Literature checks (arXiv API, abstracts): 1406.6963, 2504.10992, 2302.02143 (Tall; the item's "Clift" attribution is wrong),
2605.05075, 1511.01285, 1901.08503 (Wilsch: blow-up of P³ outside planes, not a log Fano threefold like U_n),
1908.02526, 1107.1010, 1603.04246, 1701.00265, 1604.01041, 1904.13109 and others (all exist as cited).

## Interesting items

### Z0866 — primitive solutions fail only on p ≡ 1 (mod 12) (up to 2·10⁴)
- **Observed.** Primes p ≡ 1 (mod 4), p ≤ 20 000: 1125 checked; 1069 have a primitive solution
  (gcd(x,y,z)=1 with x≤y≤z, 4/p = 1/x+1/y+1/z). 56 fail. All 56 are ≡ 1 (mod 12).
  Among 555 primes ≡ 1 (mod 12) there are 56 failures (10.1%); among 570 primes ≡ 5 (mod 12) there are 0.
  Fail residues mod 24 are only {1, 13}, i.e. no further restriction from 24; mod 5, 7, 9 the failures are spread over all residues.
- **Cross-check.** The recomputed list matches the repo's `variants.json` head (13, 37, 97, 181, 193, 277, 373, 541, 673, 757, 853, 1033, 1093, 1297, 1621, …) and the total 110 up to 10⁵ in the repo.
- **Secondary invariants tried.** Whether 2, 3, 5, 7 are cubic/quartic/sextic residues mod p (within 1 mod 12): the largest split is ≈2σ (e.g. 5 a 4th power: 9/136 fail vs 47/419 otherwise). No obvious secondary invariant.
- **Why it might matter.** A clean 3-adic dichotomy would say primitivity of ES certificates has a local obstruction at 3 for
  p ≡ 1 (mod 3) only in some cases, and the residue class 5 (mod 12) might be fully covered by primitive solutions (a partial
  every-prime statement, if provable). Whether this is genuinely new relative to the repo's fingerprint-0198 is a fair question (the
  repo had only the 110-prime list and "failures concentrate on 1 mod 12").
- **Next.** (a) Find a primitive family for p ≡ 5 (mod 12) (or show a 3-adic reason none can be primitive-free); (b) examine the first failures
  for a local obstruction at 3 (e.g., whether any primitive solution forces 3 | x y z structure).
- **Reproduce.** `uv run --with sympy python scripts/z52b_p1_U04_primitive.py 20000` (≈8 s; writes
  `data/z52b/pass1/U04/primitive_check_20000.json`); the class/residue breakdown is an inline one-liner over that JSON;
  `python3 scripts/z52b_p1_U04_prim_cubic.py` gives the character split (`prim_cubic_split.json`).
- **Labels.** The 56/555 vs 0/570 split is EVIDENCE (computed, p ≤ 2·10⁴). The statement "all failures are 1 mod 12" is EVIDENCE to 2·10⁴; not proved.

### Z1652 — Cayley cubic, almost-prime points (arXiv:1406.6963)
- **Observed.** Wang's paper (abstract checked: "density of rational points on Cayley's cubic surface whose coordinates have few prime factors", circle method + universal torsors) is the nearest published result to an ES-relevant almost-prime statement on the same surface. The item title ("saturation number") is misleading.
- **Why it might matter.** The cayley memo (`BRAINSTORM/cayley_markoff_cm.md` §P1) identifies the ES cubic with the Cayley cubic (ES(n) ⟺ integral point with y₃ = −n). A count of points with bounded-Ω coordinates on that cubic could in principle be restricted to the fibre y₃ = −p, or to a residue class of one coordinate, which is what the item asks.
- **Next.** Read Wang's main theorem; decide whether his count survives restriction to a single fibre n = p (the rational points are in a 1-parameter family of n-fibres after the affine chart); if yes, check whether the residue class of one coordinate is controllable. This is a literature/theory lane, not a computation.
- **Labels.** Literature lead only (abstract checked; no main theorem read). Assessment: no ES consequence established.

## Notes on the batch
- Several items were duplicates of earlier fingerprint/variants results (Z0693, Z0704, Z0720, Z0793, Z0865, Z0898, Z0964, Z0920, Z0858 …); these are marked `covered` with the repo file or JSON that already holds the number. Two numbers in the item text were off (Z0693 correlations; Z0721 "2⁴ | p−1" claim: v₂ ranges 3..7 among the eight hard primes, all in Mordell's classes 1, 121, 361 mod 840).
- Z2049's attribution to Clift is wrong: arXiv:2302.02143 is Tall's proof for n = 2^m·23+7.
- Z2687 (Harpaz) and Z2114 (Dao, arXiv:2504.10992): verified abstracts; non-density/BM mechanisms do not transfer to existence, as noted in the outcome lines.
- Not done (honest): Z1670/Z2480/Z2699 (Derenthal Cox-ring lookup), Z0705 (C-level compute to 10⁷), Z1394 (10⁸ scan).
