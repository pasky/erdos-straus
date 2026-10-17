# B1_LINE — the b = 1 line of Type II (task O259, spark relay on O258 SHARP)

Status: in progress (unreviewed). **ES is not solved here; no infinite case of ES for primes is claimed.** Labels as in
DISCOVERIES.md. Memos `BRAINSTORM/z29_*.md`; scripts `scripts/z29_*`; logs `logs/z29_*` (tiny).

Notation (O258, SYNTHESIS_SPARKS8 §§1–2). p ≡ 1 (mod 4) prime. The **b = 1 line**: cp + a + 1 = 4acd, i.e.
4/p = 1/(ad) + 1/(acdp) + 1/(cdp). Equivalent forms (PROVED in SYNTHESIS_SPARKS8 Props 1.2, 1.3):
* window form: ∃ m ≡ 3 (4), A | K_m := (p + m)/4 with A ≡ −1 (mod m);
* divisor form: ∃ d ≥ 1: p + 4d has a divisor w ≡ −1 (mod 4d), w < p + 4d;
* mutual-shift form (§1 below): ∃ s, t ≥ 1 with st | p + s + t and 4 | st·… (precisely: 4 | s or 4 | t).
N₁(p) := number of b = 1 solutions (a, c, d).

## 0. Iteration log
(I1) Literature (sources/lit2026f/SUMMARY.md, research subagent; key excerpts eyeballed). **The b = 1 line is KNOWN:** it is
López's "Type A" form (du, dv, duv) (M. A. López, arXiv:2206.10319, 2022/v4 2024, Theorem §2(c): for p = 4k + 1 a solution
of shape (du, dv, duv) exists iff ∃ t ≥ 0 and w | k + 1 + t with w ≡ −1 (mod 3 + 4t) — exactly our window form with
m = 3 + 4t, since k + 1 + t = (p + m)/4). López reports that ≤ 4369 only 193 and 2521 fail; López, arXiv:2404.01508 (2024)
§2 says 193, 2521 are the only primes < 9000 without Type A, that 66529 is "another case", identifies Type A with ET's
a = 1 or b = 1, and conjectures Type A ∪ Type B covers all primes (checked to 104729). Not found: the claim that
{193, 2521, 66529} is the complete exception list to 10⁸, or any finiteness conjecture/heuristic for it. So Conjecture 2.5
of SYNTHESIS_SPARKS8 is a (natural) strengthening of a question López left open; our census extends his computations.
