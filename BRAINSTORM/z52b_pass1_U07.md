# z52b Pass 1, batch U07 (207 §2 items) — summary

Counts (207 items, all have one outcome; `data/z52b/pass1/outcome_U07.jsonl`): needs-compute 107, nothing 47, skipped 45, covered 6, interesting 2.
Interesting: **Z1917** (all nine known E_a⁴ failures ≤ 10⁶ are ≡ 1 mod 24) and **Z2347** (Riemann–Hurwitz: any group realising an ES triangle signature has order divisible by p).
Caveat: most verdicts are triage-level (repo grep, one-line algebra, or a bounded computation); about 15 literature items were located but not read (see "Not done").
Coverage caveat: many `needs-compute` items are deliberately left at "≥1 h coding/reading"; several are literature reads and should be counted as lookup-blocked, not compute-blocked.

## Interesting items

**Z1917 — residues of the (★)/E_a⁴ failures.** PARITY_AUDIT.md (~line 308) lists the nine primes ≤ 10⁶ where the E_a⁴ event fails: 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321. All nine are ≡ 1 (mod 24) (all ≡ 1 mod 8, all ≡ 1 mod 3). Under a crude model in which a random p ≡ 1 mod 4 is ≡ 1 mod 8 and ≡ 1 mod 3 with probability 1/4, the chance of all nine landing there is about (1/4)⁹ ≈ 4·10⁻⁶. Caveat: these are the E_a⁴ failures named in PARITY_AUDIT, not the full 14-element (★) list; selection effects are not modelled.
- Reproduce: `scripts/z52b_p1_U07_interesting.py`.
- Next: pull the full (★) list ≤ 10⁸ and test whether it is also confined to 1 mod 24; if so, check whether a Legendre-symbol condition on the certificate lattice forces the mod-3 class.

**Z2347 — group-order constraint from ES triangle signatures.** For a finite group G acting on a closed surface with quotient the triangle orbifold (x,y,z), χ(S) = |G|·(2 − Σ(1−1/x_i)) = |G|·(4/p − 1) when 1/x+1/y+1/z = 4/p. So 2g−2 = |G|(p−4)/p, and p | |G| (p odd prime). PROVED from Riemann–Hurwitz. Sanity check over small (p,|G|): no counterexample.
- Consequence: an ES triangle signature can only be realised by groups of order divisible by p (e.g. PSL(2,p)-type families).
- Next: which ES signatures with small p are realised by quotients of PSL(2,p) or PGL(2,p)? Use Macbeath/Hurwitz generation.
- Source caveat: the May–Zimmerman construction itself was not read.

## Scripts and data
- `scripts/z52b_p1_U07_solstats.py` (+ `data/z52b/pass1/U07/solstats_1500.json`): all solutions of 4/p=Σ1/x, p ≤ 1500 (brute-force checked for p ≤ 59).
- `scripts/z52b_p1_U07_small.py`, `_b1.py`, `_b2.py`, `_b3.py`, `_b4.py`, `_b5.py`, `_b6.py`, `_b7.py`, `_b8.py`, `_b9.py`, `_b10.py`, `_b11.py`, `_b12.py`: the capped checks behind the nothing/covered verdicts.

## Not done (honest list)
- Literature items located but not read: Z1435/Z1951 (Mordell ch. 30), Z1952 (Dickson), Z1971 (Ramírez Alfonsín), Z1564 (Obláth original), Z1661 (Erdős 1950 PDF at renyi.hu), Z2235 (arXiv 1108.6118 content), Z2672 (Jeffrey CMP 147), Z2791 (Morishita), Z2660 (Lisca math/0701610 §§2–3), Z1640/Z1660 (Tao 2011 comments, Ahmadi–Bleicher), Z1565/Z1662 (UPINT D11 bibliography), Z1637 (erdosproblems status).
- Several `skipped` items are external actions (emails, MO posts, Zulip, referee) or writing tasks, per the meta rule; a few are judgement calls (Z1103, Z1104, Z1119, Z1285, Z0205, Z1898): no ES-specific test could be stated without inventing a construction.
- Not run: any computation marked needs-compute (107 items).
