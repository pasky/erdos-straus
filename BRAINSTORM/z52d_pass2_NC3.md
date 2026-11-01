# z52d Pass 2 — batch NC3 (80 items, all Pass-1 `needs-compute`) — after lint-fix round

**Summary (80/80 outcomes in `data/z52b/pass2/outcome_NC3.jsonl`; lint 0 flagged).**
1. Counts: nothing 71, interesting 6, needs-compute 2, covered 1, skipped 0. Needs-compute: Z2865 (GPPV/Seifert Ẑ: formula not transcribed) and Z3139 (Cox ring/torsor: needs Macaulay2/Singular); neither is a CPU-cap case, and they are left open rather than relabelled.
2. Interesting: **Z2925** — the trace-zero Gross lattices of Λ_{d,m} have one-class genus for all d, m ≤ 5 (exact class enumeration of even ternary forms of det 2N², theta-series genus proxy to B = 800).
3. Interesting: **Z2782** — sign of 4-chains is a function of the entries mod 4 (6250 chains, 0 conflicts); naive rules fail; likely Barkan–Hickerson–Knuth mechanism.
4. Interesting: **Z2783** — MGO q-rational at e^{iπ/4} predicts the sign at 96.6% (baseline 69%), not via (t,u,v) mod 4.
5. Interesting: **Z3055** (prime factors of j-norms are inert, biased to ℓ ≡ −1 mod 4C), **Z3077** (sub-route failure sets: m = 6 is an exact single-character condition (−3/p) = +1; m = 8..16 leave residuals), **Z3004** (minimal level menus for Mordell-hard primes grow: 10 at P = 2·10⁴, 22 at P = 2·10⁵).

**Lint-fix round (18 flagged items).** Each was re-run with a real step: Z2809 (transport laws: only integer self-map is n ↦ kn; ES verified to 3000 in Lean), Z2811 (3-braid closure signatures; sign not a function of signature), Z2831 (Gross–Zagier vs Type I), Z2886 (core-Lean kernel check of ES(n), n ≤ 3000, axioms propext only), Z2925 (genus enumeration: interesting), Z2936 (exact T_3-projection: level-series products are Eisenstein for t = 4, 8), Z3004 (menus: interesting), Z3013 (affine cubic counts: deviation exactly q−1), Z3027 (premise undefined), Z3055 (interesting), Z3074 (premise error: no Eichler order of even level in B_{2,∞}), Z3077 (interesting), Z3090 (least-level sampling to 10⁹), Z3095 (genus theory of the 6 square classes), Z3139 (needs-compute), Z3147 (reachability characterised by divisors of 4Cp+1; 26 unreachable ≤ 2·10⁵), Z3181 (ternary classes of det ≤ 200 vs exceptions of x²+y²+7z²), Z2865 (needs-compute).

**Also re-run:** Z2736 (box/h⁺ calibration: box < h⁺ for 90% of μ), Z2811 (braid signatures), Z2812 (false premise, tr γ_w − 2 = p − t − 2).

## Interesting items

### Z2925 — one-class genus for the Gross lattices of Λ_{d,m}

*What.* Λ_{d,m} = ℤ⟨u,v⟩ (u² = −d, v² = −m, uv + vu = 1) has trace-zero lattice with norm form d b² − bc + m c² + (4dm−1) k² (checked by quaternion arithmetic). Its even Gram matrix G = [[2d,−1,0],[−1,2m,0],[0,0,2N]], N = 4dm−1, has det 2N².

*Numbers.* For d, m ≤ 5, all even positive ternary classes of det 2N² were enumerated (reduced ranges, PARI `qfisom` deduplication), and the genus proxy (theta series via `qfrep` up to B = 800) contains exactly one class for each of the 25 pairs. At B = 60 two classes looked genus-equal for (4,4) and (5,5); they are separated at B = 300.

*Reproduce.* `uv run --with cypari2 --with sympy python scripts/z52d_p2_NC3_genus.py 5` (`data/z52b/pass2/NC3/genus_Z2925.txt`).

*Why it might matter.* A one-class genus means spinor genus = genus, so representation numbers of these ternary lattices are governed by genus theory with no spinor-exception issue. This removes the Duke–Schulze-Pillot step of Z2730 for these forms. It is not an ES statement, and the link to Type I/II data still needs the (ii) divisor condition.

*Caveat.* The genus statement is rigorous only up to the enumeration and the theta-equality test (genus-equal ⇒ theta-equal, so the theta count bounds the genus count from above).

## Other interesting items (short)

### Z3004 — menus of levels grow with P
Exact minimum set of levels C ≤ CMAX covering all Mordell-hard primes p ≤ P by level-4C words: 10 for (P, CMAX) = (2·10⁴, 40), with 2 primes uncoverable; 22 for (2·10⁵, 60), with 9 uncoverable. Reproduce: `scripts/z52d_p2_NC3_cover.py`. Next: P = 10⁶, CMAX = 100, to see whether the menu grows like log P or like a power of P.

### Z3055 — prime factors of singular-moduli norms
For p ≡ 1 (24), p ≤ 1500: all odd prime factors of H_{−4p}(0) are inert in ℚ(√−p) (209/209). 71% have (−1/ℓ) = −1 (293 factors, control 50%). With C the least level, 56.5% are ≡ −1 (mod 4C) against 39.5% of inert controls; for C = 1, 73% against 50%. Reproduce: `scripts/z52d_p2_NC3_singular.py`. Next: derive the mod-4 bias from genus theory and check at p ≤ 10⁴ with size-matched controls.

### Z3077 — sub-route failure sets
For m ∈ {6, 8, 10, 12, 16}, failure sets of Type II counts up to 2·10⁶ fitted to single Legendre conditions (d/p) = ±1 with d | 4m. For m = 6, (−3/p) = +1 contains all 13 failures (no failure with p ≡ 2 mod 3). For m = 8, 10, 12, 16 the best single condition leaves 5, 17, 18, 126 failures outside. Reproduce: `scripts/z52d_p2_NC3_subroute.py` (binaries from `scripts/z32_ladder.c` in /tmp, not in the repo).

### Z2782 — sign of longer HJ chains as a mod-4 function of the entries

*What.* The 3-chain sign (A/p), A = tu − 1, is a function of (t,u,v) mod 4 for p ≡ 1 (8) (the PROVED slot lemma, FOREST_CONNECTIVITY Thm 2.1). For 4-chains (a,b,c,d) with K(a,b,c,d) = p ≡ 1 (8) and A = K(b,c,d), the sign is also a function of (a,b,c,d) mod 4.

*Numbers (p ≤ 3000).* 6250 chains, 90 residue classes, 0 conflicts. The naive rules "4 divides an entry" (1348/1730) and "4 divides a consecutive sub-continuant" (1216/1730) fail.

*Reproduce.* `uv run --with cypari2 --with sympy python scripts/z52d_p2_NC3_chain4.py 3000`; `scripts/z52d_p2_NC3_mod8.py` for the 3-chain check.

*Why it might matter.* The L-ladder (Z2852) needs a slot rule for λ(p) ≤ L. A mod-4 rule exists at L = 4 but the naive one is wrong. The likely mechanism is the Barkan–Hickerson–Knuth formula (Jacobi symbol = sign of an alternating sum of partial quotients mod 4; Girstmair arXiv:1501.00655, Tsukerman arXiv:1501.03544; read from the abstracts only).

*Next.* Derive the exact L-chain rule from the alternating-sum congruence and check it on the 4-chain table, then L = 5.

### Z2783 — MGO q-rationals at a root of unity predict the sign

*What.* The Morier-Genoud–Ovsienko q-rational of the regular continued fraction of p/A (sanity q → 1 OK), at q = e^{iπ/4}, has 36 distinct phases over the 118 words of p ≡ 1 (8), p ≤ 300. The phase-to-sign majority rule is correct for 96.6% of words (baseline 69%). The phase is not a function of (t,u,v) mod 4 (18 of 20 classes conflict). At q = i, phases are shared by both signs and 55 evaluations hit a pole.

*Reproduce.* `uv run python scripts/z52d_p2_NC3_mgo.py 300` (`data/z52b/pass2/NC3/mgo_Z2783.txt`).

*Caveats.* p ≤ 300 only; 3.4% misclassified; a CF statistic (length parity, count of entries ≡ 1 mod 4) may explain the correlation, untested.

*Next.* Test whether the phase at ζ₈ is an exact function of a CF statistic for p ≤ 10⁴.
