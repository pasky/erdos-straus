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
escape (free pairs, Cor 1.3) that the c = 1 line provably lacks. This is the first structural b = 1 vs (★) difference.

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
For the c = 1 line ((★): pairs (x, y), both odd, with 4 | N(x, y)) one has (xy/p) = −1 for every pair and every p ≡ 1 (4).
*Proof.* Write r ≡ −S − T. Since p ≡ −T (mod S′) and p ≡ −S (mod T), Jacobi gives (p/S′) = (−T/S′) and
(p/T) = (−S/T) = (−1/T)(2/T)^k(S′/T) = −(2/T)^k (S′/T), as T ≡ 3 (4). Reciprocity with (T − 1)/2 odd gives
(S′/T) = (T/S′)(−1/S′) = (−T/S′). Hence (p/S′T) = −(2/T)^k (−T/S′)² = −(2/T)^k. If k ≥ 3 then T ≡ −p (mod 8), so
(2/T) = (2/p). If k = 2 then (2/T)^k = 1 = (2/p)^k. Since p ≡ 1 (4), (ℓ/p) = (p/ℓ) for odd ℓ, so (S′T/p) = −(2/p)^k. Then
(ST/p) = (2/p)^k (S′T/p) = −1. For c = 1: (p/x) = (−y/x), (p/y) = (−x/y). Since x + y ≡ −p ≡ 3 (4), exactly one of x, y is
≡ 3 (4), so (−1/x)(−1/y) = −1, and reciprocity contributes (−1)^{(x−1)(y−1)/4} = +1. ∎
(Check: `z29_genus.py`, all 12 717 b = 1 pairs and 5 710 c = 1 pairs at p < 2·10⁴: 0 violations; free pairs (below) occur
only in the class (p mod 8, k mod 2) = (5, 1); `logs/z29_genus.txt`.) (ST/p) = −1 is O258 Lemma 2.2(a) in pair coordinates.
The new content is the split into S′T and the 2-adic factor.

**Corollary 1.3 (the 2-adic escape; PROVED).** Call a b = 1 pair *free* if (S′T/p) = +1. Free pairs exist only for
p ≡ 5 (8) and are exactly the pairs with v₂(S) odd (≥ 3). They are the only solutions whose existence needs no odd
non-residue of p. In particular:
(a) If every odd prime ℓ ≤ Y is a QR mod p and p ≡ 1 (8), then every b = 1 pair has a prime factor > Y in S′T.
(b) The c = 1 line has no free pairs. At every p ≡ 1 (4), every (★) pair has a prime factor ℓ | xy with (ℓ/p) = −1.
*Reading.* For the b = 1 line, p ≡ 5 (8) makes 2 a non-residue that every pair with 8 ∥ S, 32 ∥ S, … may use. In the
Haar model these pairs form a fixed positive proportion of the mass, and they are indifferent to QR-richness of p (§3). The
census agrees: **every b = 1 failure, and every record of the least shift s, is at p ≡ 1 (mod 8)** (§2). The c = 1 line can
never use 2: its 2-adic modulus is exactly 4, and every odd p is a square mod 4.
