# z52b pass 1 — batch U02 (§2 untried; 207 items) — INCOMPLETE after fix pass

- Outcomes (207): nothing 56, covered 8, interesting 3, needs-compute 26, skipped 114 (of which 64 NOT PROCESSED).
- Interesting: Z1054 (exactly one denominator divisible by p ⇒ (y/p)(z/p) = −1 in 10656/10656 cases, p<5000); Z1568 (no divisor ≡ −1 mod 4C for any C≤200 among p≤10⁴ gives exactly (409, 577, 5569, 9601)); Z0968 (Tunnell A(p) keeps +0.30 partial correlation with residual U after (2/p), h(−8p), h(−4p); raw −0.31 is a mod-8 split).
- Status: the fix rules (2026 pass1_U_fix.md) were applied to 58 items (re-run or looked up and replaced). 64 items were never processed (batch time budget) and are marked skipped with an explicit NOT PROCESSED flag. 76 skipped/needs-compute lines remain that do not meet the fix rules (generic items with no precise version, and ES items whose step was not run). This batch is NOT complete; the parent should reassign the open list.
- Proved side facts: Z0259 (no repeated denominators for p≡1 mod 4, 4-line lemma), Z0868 (≥2 even denominators for odd n, 2-adic lemma), p | xyz for every solution (4xyz = p(xy+yz+zx)).
- Records: data/z52b/pass1/outcome_U02.jsonl; scripts scripts/z52b_p1_U02_*; data data/z52b/pass1/U02/.


## Z1054 — exactly one denominator divisible by p (interesting)

`uv run --with sympy --with numpy --with scipy python scripts/z52b_p1_U02_f.py`. Solutions from `esols` (scripts/z52b_p1_U02_lib.py), p=1 mod 4, 5 < p < 5000, 15555 solutions in total.
If exactly one denominator x is divisible by p (all others not), the other two satisfy (y/p)(z/p) = −1 in all 10656 cases: (−1,+1) 5903, (+1,−1) 4753. Two-divisible cases show both signs (scripts/z52b_p1_U02_e.py). Derivation so far: x = pa, 4a−1 = ph, and h·yz = a(y+z); yz·h² = a(s+a)²/s with s = hy − a, so (yz/p) = (as/p). Next: show (as/p) = −1 is forced.

## Z1568 — C-form exceptional set (interesting)

Definition used: p=1 mod 4 with no proper divisor d of 4Cp+1 with d ≡ −1 mod 4C, for every C ≤ 200. Among p ≤ 10⁴ this is exactly {409, 577, 5569, 9601} (data/z52b/pass1/U02/fix_f.json). Beyond that: with C ≤ 60, p in (10⁴, 6·10⁴] gives 19141, 23041, 23929, 26209, 46237, 49669. Next: extend the test to p ≤ 10⁶ and test for a local obstruction at 2 or primes dividing C.

## Z0968 — Tunnell counts beyond class numbers (interesting)

A(n)=r_{1,2,8}(n), B(n)=r_{1,2,32}(n) (lattice counts), p=1 mod 4, p<2000 (n≈300): raw corr(resU, A) = −0.31, corr(resU, B) = −0.30, and corr(resU, A−2B) = −0.08. A(p)=0 for every p≡5 mod 8 and never for p≡1 mod 8, so the raw correlation is the mod-8 split. Controlling (2/p), log h(−8p), log h(−4p): partial corr(resU, A) = +0.30, corr(resU, B) = +0.30. The item's ρ≈+0.18 was not reproduced; definitions likely differ. Next: check against final_checks.json.

## Reproduce

- Helper: scripts/z52b_p1_U02_lib.py (esols, validated against f4_all_30000 for n<3000).
- Scripts: z52b_p1_U02_{Z0081,a,b,c,d,e,f,fp,g,h}.py. Data: data/z52b/pass1/U02/*.json.
