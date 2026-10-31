# z52b Pass 1 — batch U04 (207 untried §2 items)

**Summary (counts, after the pass1_U_fix redo):** 207 items: nothing 87, covered 50, needs-compute 58, skipped 10 (restatement/meta only), interesting 2.
**Interesting:** Z0866 (primitive ES failures confined to p≡1 mod 12 up to 2·10⁴: 56/555 vs 0/570 in class 5 mod 12); Z1652 (Y. Wang, arXiv:1406.6963: almost-prime rational points on the Cayley cubic via circle method + torsors; possible fibre/class restriction).
**Computed negatives (examples):** Z0785 (Neumann–Setzer), Z0342 (Z[√2] cone), Z0562 (Pell candidates), Z0992 (heights disagree), Z1369 (Sylvester numerator stuck at 3), Z1407 (trivial giant component), Z1484 (Kronecker–Hurwitz verified, no ES trace), Z1670/Z2480/Z2699 (Derenthal: 4A1 cubic torsor has ≥2 relations, not a hypersurface), Z1965 (induction maps send no-witness primes to non-failing primes), Z2523 (class effects = Mordell classes), Z2696 (signed integer points on U_n grow slowly in B), Z0915 (partition parity null), Z1019–Z1087 (witness pipeline; see outcome lines).
**Needs-compute:** 58, each with the computation and estimate in outcome_U04.jsonl. Several are estimated at 30–60 min and should be done next (Z0786, Z1164, Z1259, Z2617, Z2868, Z2626).
**Outcome file (authoritative):** data/z52b/pass1/outcome_U04.jsonl (the earlier outcome_src/redo_src files are kept as the text source).

Repro: `scripts/z52b_p1_U04_*.py`; data in `data/z52b/pass1/U04/`.
Literature checks (arXiv API, web search, PDF): 1406.6963, 2504.10992, 2302.02143 (Tall; the item's "Clift" attribution is wrong), 2605.05075, 1511.01285, 1901.08503 (Wilsch: blow-up of P³ outside planes, not a log Fano threefold like U_n), math/0604194 (Derenthal, Table 7), math/0206100 (Corvaja–Zannier), 1703.05967 (Fink–Speyer), 1601.07066 (Corvaja–Zannier review), math/0311421 (Croot), Button 1998 (prime Markoff uniqueness; Lang 2007 prime powers), and others (existence checked).

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

## Notes on the batch (after pass1_U_fix)
- Several items were duplicates of earlier fingerprint/variants results (Z0693, Z0704, Z0720, Z0793, Z0865, Z0898, Z0964, Z0920, Z0858 …); these are marked `covered` with the repo file or JSON that already holds the number. Two numbers in the item text were off (Z0693 correlations; Z0721 "2⁴ | p−1" claim: v₂ ranges 3..7 among the eight hard primes, all in Mordell's classes 1, 121, 361 mod 840).
- Z2049's attribution to Clift is wrong: arXiv:2302.02143 is Tall's proof for n = 2^m·23+7.
- Z2687 (Harpaz) and Z2114 (Dao, arXiv:2504.10992): verified abstracts; non-density/BM mechanisms do not transfer to existence, as noted in the outcome lines.
- Still open (honest): 58 needs-compute items, including Z1394 (10⁸ scan), Z0786 (ecdata per-conductor counts), and the Derenthal-dependent Galois/torsor items that now have a negative answer for the 4A1 cubic.
- Z2866: the item says 'prime powers'; Button 1998 proves the prime case, Lang 2007 the prime-power case. Not relevant to S_{p,D} either way.
