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
(I2) Census engine rebuilt on the mutual-shift form (Lemma 1.1; independent of O258's window code): ≤ 10⁸ in 2 s, ≤ 10¹⁰
in ≈ 3 min on 2 cores. Exact N₁(p) counts agree with O258's brute force `s8_check_b1.py` for every p ≡ 1 (4) < 400.
(I3) Construction attempt "find the T1 escape": T1 is a Jacobi identity on pairs (Lemma 1.2). Its b = 1 version has a 2-adic
escape at p ≡ 5 (8). First reading: a b = 1 vs (★) difference. Refuted the same day: (★) has the same escape (pairs with
v₂(x) = 1), and both lines are TRIVIAL at p ≢ 1 (24) by fixed pairs (Prop 1.4). The hardness lives in p ≡ 1 (24), where
neither line has a 2-adic escape. Kept as a correct but non-discriminating lemma.

## 1. Pair coordinates and the pair genus law

**Lemma 1.1 (mutual-shift form; PROVED).** Let n ≡ 1 (mod 4). The b = 1 solutions (a, c, d) of 4/n correspond bijectively
to unordered pairs {s, t} of positive integers with
  st | n + s + t  and  4 | st,
via {s, t} = {g, 4d}, g = (n + 4d)/(4cd − 1), c = (n + s + t)/(st), a = (cn + 1)/(4cd − 1). In every such pair exactly one
coordinate (call it S) is ≡ 0 (mod 4), the other (T) is ≡ 3 (mod 4), and gcd(S, T) = 1 if n is prime. Moreover
min(s, t) ≤ 1 + √(n + 1), and with p + s = t·u the condition reads s | u + 1; so the search over s ≤ 1 + √(n+1) and t | n + s
is complete.
*Proof.* SYNTHESIS_SPARKS8 Prop 1.3 gives the bijection with ordered pairs (g, D), D = 4d, gD | n + g + D (the conditions
g | n + D, D | n + g follow). If both coordinates were even, n + s + t would be odd while st is even: so exactly one is
divisible by 4, and the unordered pair determines D. If S ≡ 0 (4) then T ≡ −n ≡ 3 (mod 4) (from S | n + T). A common prime
of s, t divides n; for n = p prime and s, t < p that is impossible (s, t ≥ p would give st > p + s + t). Finally
st ≤ n + s + t gives (s − 1)(t − 1) ≤ n + 1. ∎

**Lemma 1.2 (pair genus law; PROVED, Jacobi — the pair form of T1).** Let p ≡ 1 (4) be prime and (S, T) a b = 1 pair, S = 2^k S′,
k ≥ 2, S′ odd. Then
  (ST/p) = −1,  and  (S′T/p) = −(2/p)^k.
So for p ≡ 1 (8) the odd part S′T always contains a prime ℓ with (ℓ/p) = −1. For p ≡ 5 (8) the same holds when k is even,
but when k is odd, (S′T/p) = +1 and the non-residue is 2 itself.
For the c = 1 line ((★): pairs (x, y) with 4 | N(x, y); if 4 | x the pair is also a b = 1 pair, so let v₂(x) ≤ 1, y odd)
one has (xy/p) = −1 as well; (x′y/p) = −1 for x = 2x′ at p ≡ 1 (8), and (x′y/p) = +1 at p ≡ 5 (8).
*Proof.* Write r ≡ −S − T. Since p ≡ −T (mod S′) and p ≡ −S (mod T), Jacobi gives (p/S′) = (−T/S′) and
(p/T) = (−S/T) = (−1/T)(2/T)^k(S′/T) = −(2/T)^k (S′/T), as T ≡ 3 (4). Reciprocity with (T − 1)/2 odd gives
(S′/T) = (T/S′)(−1/S′) = (−T/S′). Hence (p/S′T) = −(2/T)^k (−T/S′)² = −(2/T)^k. If k ≥ 3 then T ≡ −p (mod 8), so
(2/T) = (2/p). If k = 2 then (2/T)^k = 1 = (2/p)^k. Since p ≡ 1 (4), (ℓ/p) = (p/ℓ) for odd ℓ, so (S′T/p) = −(2/p)^k. Then
(ST/p) = (2/p)^k (S′T/p) = −1. For c = 1 with x, y odd: (p/x) = (−y/x), (p/y) = (−x/y). Since x + y ≡ −p ≡ 3 (4), exactly one of x, y is
≡ 3 (4), so (−1/x)(−1/y) = −1, and reciprocity contributes (−1)^{(x−1)(y−1)/4} = +1. For x = 2x′: 8 | p + x + y gives
y ≡ −p − 2x′ (mod 8), and (p/x′y) = (−y/x′)(−2x′/y) = (−1/x′)(−1/y)(2/y)(−1)^{(x′−1)(y−1)/4}. The four cases
(p mod 8, x′ mod 4) ∈ {1, 5} × {1, 3} give y ≡ 5, 1, 1, 5 (mod 8) and the value −1, −1, +1, +1; multiply by (2/p). ∎
(Check: `z29_genus.py`, all 12 717 b = 1 pairs and 5 710 c = 1 pairs at p < 2·10⁴: 0 violations; free pairs (below) occur
only in the class (p mod 8, k mod 2) = (5, 1); `logs/z29_genus.txt`.) (ST/p) = −1 is O258 Lemma 2.2(a) in pair coordinates.
The new content is the split into S′T and the 2-adic factor.

**Corollary 1.3 (where the non-residue sits; PROVED).** Call a pair *free* if its odd part has Jacobi symbol +1 (so the
non-residue demanded by T1 is 2). Free b = 1 pairs exist only for p ≡ 5 (8) (v₂(S) odd ≥ 3), and free (★) pairs only for
p ≡ 5 (8) (v₂(x) = 1). For p ≡ 1 (8), every pair of either line has an odd prime ℓ | (odd part) with (ℓ/p) = −1; in
particular if every odd prime ℓ ≤ Y is a QR mod p, every pair has a prime factor > Y.

**Proposition 1.4 (the trivial classes; PROVED, folklore-level covering identities).** The b = 1 line holds for every
p ≡ 1 (4) with p ≢ 1 (mod 24): the pair (3, 4) solves p ≡ 5 (12) and (3, 8) solves p ≡ 13 (24). The (★) line holds for
p ≡ 5 (8) via (1, 2) (N = (p + 3)/2). *Proof.* 12 | p + 7, 24 | p + 11, 8 | p + 3 respectively. ∎
*Reading.* The 2-adic escape is real but it only acts in classes that fixed congruence identities already cover. All the
hardness of both lines lies in p ≡ 1 (24) (for b = 1). There both lines need an odd non-residue of p inside the pair. The
census agrees: every b = 1 failure and every record of the least shift from p = 73 on is at p ≡ 1 (24) (§2).
