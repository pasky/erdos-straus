# z52b pass 1 — batch U02 (§2 untried; 207 items) — INCOMPLETE (86 items still non-compliant)

- Outcomes (207): nothing 102, covered 12, interesting 7, needs-compute 44, skipped 42.
- Interesting (7): Z1054 (one denominator divisible by p ⇒ (y/p)(z/p) = −1, 10656/10656); Z1568 (C≤200 slice-failure set = {409,577,5569,9601} for p≤10⁴); Z0968 (Tunnell A keeps +0.30 partial after mod-8 and class numbers); Z2983 ((6/p) = (2/p)(3/p) adds +0.06 out of sample); Z1342 ((−C/p)=+1 slices succeed 22% vs 14%); Z1471 ((a/p) = −1 for all 2044 winning divisors; reduces to (C/a)=+1); Z1483 (Type I with d=1 has zero hits despite h(−4)=1).
- Open: 86 lines are still skipped or needs-compute without a run, so the batch is NOT complete under pass1_U_fix.md. The list is in data/z52b/pass1/outcome_U02.jsonl (outcome in {skipped, needs-compute}, summary not starting with "NOT PROCESSED").
- Records: data/z52b/pass1/outcome_U02.jsonl; scripts/z52b_p1_U02_*; data/z52b/pass1/U02/*.json.

## Z1054 — one denominator divisible by p (interesting)

`scripts/z52b_p1_U02_f.py`. Solutions from `esols`, p=1 mod 4, p<5000, 15555 solutions. If exactly one denominator is divisible by p, the other two satisfy (y/p)(z/p) = −1 in all 10656 cases ((−1,+1) 5903, (+1,−1) 4753). Derivation so far: x = pa, 4a−1 = ph, h·yz = a(y+z), yz·h² = a(s+a)²/s with s = hy−a, so (yz/p) = (as/p). Next: prove (as/p) = −1 is forced.

## Z1568 — C-form exceptional set (interesting)

Definition: p=1 mod 4 with no proper divisor d of 4Cp+1 with d ≡ −1 mod 4C, for every C ≤ 200. For p ≤ 10⁴: exactly {409, 577, 5569, 9601} (`scripts/z52b_p1_U02_f.py`, data/z52b/pass1/U02/fix_f.json). With C ≤ 60, p in (10⁴, 6·10⁴] gives 19141, 23041, 23929, 26209, 46237, 49669 (not comparable: smaller C range). Next: extend to p ≤ 10⁶ with C ≤ 200 and test a local obstruction at 2 or at primes dividing C.

## Z0968 — Tunnell counts beyond class numbers (interesting)

A(n)=r_{1,2,8}(n), B(n)=r_{1,2,32}(n), p=1 mod 4, p<2000 (n≈300). Raw corr(resU, A) = −0.31, corr(resU, B) = −0.30, corr(resU, A−2B) = −0.08. A(p)=0 for every p≡5 mod 8 and never for p≡1 mod 8 (`scripts/z52b_p1_U02_h.py`). Controlling (2/p), log h(−8p), log h(−4p): partial corr(resU, A) = +0.30, corr(resU, B) = +0.30. Item's ρ≈+0.18 not reproduced. Next: check definitions against final_checks.json.

## Z2983 — conductor-24 interaction (interesting)

Out-of-sample R² of residual log U (p=1 mod 4, 100<p≤3·10⁴) on residue-class indicators, cumulative over moduli: q=8: 0.57; q=23: 0.63; q=24: 0.73 (`scripts/z52b_p1_U02_o.py`). The step at q=24 is the quadratic character (6/p) = (2/p)(3/p): on the mod-8 + mod-3 base it adds +0.06 out of sample (0.421 → 0.478; `scripts/z52b_p1_U02_p.py`), with corr(residual, (6/p)) = −0.26. The repo has no (6/p) or (2/p)(3/p) term (git grep). Next: test with all Legendre symbols and class numbers on p ≤ 10⁵.

## Reproduce

Helper: scripts/z52b_p1_U02_lib.py (esols, validated against f4_all_30000 for n<3000). Scripts: z52b_p1_U02_{Z0081,a,b,c,d,e,f,fp,g,h,m,n,o,p}.py.

## Z1342 — quadratic sign and slice success (interesting)

`scripts/z52b_p1_U02_q.py`. C ≤ 12, p = 1 mod 4, p < 2000: P(slice success | (−C/p)=+1) = 0.222 (n=1062); P(success | (−C/p)=−1) = 0.140 (n=700). Next: control for (C/p) and (−1/p) jointly.

## Z1471 — winning divisors are non-residues (interesting)

`scripts/z52b_p1_U02_r.py`. For all 2044 divisors a of 4Cp+1 with a ≡ −1 mod 4C (C ≤ 12, 300 primes p < 2·10⁴), (a/p) = −1. Reciprocity with p ≡ 1 mod 4 gives (a/p) = (p/a) = −(C/a), so the claim is equivalent to (C/a) = +1, which is not proved here. Next: prove it; check against p < 10⁶.

## Z1483 — d = 1 has no Type I certificates (interesting)

`scripts/z52b_p1_U02_q.py`. Type I(d,c,p): ∃ f | p² + 4c²d, 1 < f < N, f ≡ −p mod 4cd. For 10 primes near 10⁴ and c ≤ 60: d=1: 0 hits; d=2: 72; d=3: 24; d=5: 20; d=7: 19. Consistent with Z3030 (0 of 1600). Next: prove d=1 is empty (genus argument on Z[2ci]) or find a counterexample.
