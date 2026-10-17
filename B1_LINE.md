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
a = 1 or b = 1, and conjectures Type A ∪ Type B covers all primes (checked to 104729). López 2404.01508 also has (verified, `sources/lit2026f/Lopez-2024-TypeB-Thm7.md`): Thm 7 = the divisor form
(p ≡ −4d mod 4dn − 1, i.e. SYNTHESIS_SPARKS8 Prop 1.3); Thm 4 / Type B = the c = 1 line (★); Conjecture 1 = "Type A ∪
Type B covers every prime" (= O258's union observation). Gardes' thesis lists 2521, 66529 as problem primes (per R268 M4).
**Re-scoped novelty:** the b = 1 line, its divisor form, the exceptions 193/2521/66529 and the union conjecture are López's.
Potentially new here: the census beyond 10⁸ (§2), the pair genus law in this form (§1), the smooth-(p − 1) structure
theorem and the Dickson obstruction for the least shift (§4), and the heuristic model (§3). Not found: the claim that
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

## 2. Census (EVIDENCE; complete decisions)

**2.1 All primes p ≡ 1 (4) ≤ 10¹⁰** (`z29_census`, segmented factor tables, least s with a hit, exact fallback over all
s ≤ 1 + √(p + 1) when no hit with s ≤ 512; logs `logs/z29_census_1e10.txt`). Prime counts per range sum to
227 523 275 = π(10¹⁰; 4, 1), confirmed by an independent segmented Eratosthenes count (`pcount`, not kept).
| range | primes p ≡ 1 (4) | b = 1 failures | fallback calls | max least s (at) |
|---|---|---|---|---|
| ≤ 10⁸ | 2 880 504 | 193, 2521, 66529 | 3 | 119 (1 683 049) |
| (10⁸, 5·10⁹] | 114 594 477 | 0 | 0 | 111 (277 977 001) |
| (5·10⁹, 10¹⁰] | 110 048 294 | 0 | 0 | 104 (6 098 002 681) |
Distribution of the least s, ≤ 10¹⁰ (log₂-bins [2,4), [4,8), …): 2.07·10⁸, 1.84·10⁷, 1.82·10⁶, 1.28·10⁵, 4 211, 94, 0.
The least hitting s does NOT grow with p (records 119 ≤ 10⁸, ≤ 111 above). Every global record from p = 73 on is at
p ≡ 1 (24), as Prop 1.4 demands.

**2.2 Primes with smooth p − 1 up to 10¹⁵** (`z29_smooth X Y S`: all p = m + 1 ≤ 10¹⁵ with m Y-smooth and 4 | m; bounded
search s ≤ 2000 by Pollard–Brent factorisation; `logs/z29_smooth_1e15.txt`).
| Y | primes | of which p ≡ 1 (8) | unresolved (no hit s ≤ 2000) | max least s (p ≡ 1 (8)) | max least s (p ≡ 5 (8)) |
|---|---|---|---|---|---|
| 11 | 14 173 | 12 781 | 193, 2521, 66529 only | 95 (at 345 601) | 3 |
| 13 | 41 146 | 36 517 | same three | 95 | 3 |
| 17 | 99 549 | 87 216 | same three | 95 | 3 |
| 19 | 216 882 | 187 500 | same three | 95 | 3 |
For the three, s ≤ 2000 exceeds 1 + √(p + 1), so "unresolved" is a complete failure decision. Every other smooth-(p − 1)
prime up to 10¹⁵ has a b = 1 solution with s ≤ 95 (positives are certified by the exhibited pair; no completeness needed).
**The hardest smooth primes are small.** Among 2.2·10⁵ primes with 19-smooth p − 1, the least shift never exceeds the value
95 reached at 345 601 = 2⁹·3³·5² + 1, although these primes are profinitely as close to
the T1 point 1 as primes of that size can be. So smoothness of p − 1 is a small-p effect: it makes small pairs (s, t) dead,
and at large p there are enough pairs with a large prime factor (Cor 1.3, §3).

## 4. Why the hard primes have smooth p − 1: the T1 point 1 at small shifts

For σ ≥ 3 let M_σ := Π_{ℓ ≤ σ + 1} ℓ^{e_ℓ}, e_ℓ := ⌊log_ℓ(σ + 1)⌋ + 1 (so v_ℓ(M_σ) > v_ℓ(m) for every m ≤ σ + 1). Call s the
*shift* of a pair {s, t} with s < t (the min coordinate of Lemma 1.1).

**Proposition 4.1 (p ≡ 1 mod M_σ freezes the small shifts; PROVED).** Let p ≡ 1 (mod 4) be prime with M_σ | p − 1, and let
3 ≤ s ≤ σ. Put Q_s := (p + s)/(1 + s). Then Q_s is an integer, Q_s ≡ 1 (mod s), all prime factors of Q_s exceed σ + 1, and
the b = 1 pairs with shift s are exactly the divisors t > s of p + s = (1 + s)·Q_s with
  t ≡ −1 (mod s)  and  4 | st.
Writing t = g·m with g | 1 + s and m | Q_s, this is m ≡ −g⁻¹ (mod s). In particular:
(a) every pair whose two coordinates both divide M_σ is dead (no Haar-small pair survives);
(b) if Q_s is prime, there is no pair with shift s;
(c) a pair with shift s exists only if Q_s has a divisor m in one of the classes −g⁻¹ (mod s), g | 1 + s, g ≢ −1 (mod s)
    or m ≢ 1 — a divisor-in-a-class event (B2) for an integer Q_s ≡ 1 (mod s) whose primes are all > σ + 1.
*Proof.* p + s = (1 + s) + (p − 1) and v_ℓ(p − 1) ≥ v_ℓ(M_σ) > v_ℓ(1 + s) for ℓ ≤ σ + 1, so (1 + s) | p + s and
Q_s = 1 + (p − 1)/(1 + s) ≡ 1 (mod ℓ) for all ℓ ≤ σ + 1; for ℓ | s also ℓ ∤ 1 + s and v_ℓ((p − 1)/(1 + s)) ≥ v_ℓ(M_σ) > v_ℓ(s),
so Q_s ≡ 1 (mod s). By Lemma 1.1 a pair with shift s is a divisor t > s of p + s with u := (p + s)/t ≡ −1 (mod s) and
4 | st. Now t·u = (1 + s)Q_s ≡ 1 (mod s), so u ≡ t⁻¹ and u ≡ −1 ⟺ t ≡ −1 (mod s). With t = gm (gcd(1 + s, Q_s) = 1),
t ≡ −1 ⟺ m ≡ −g⁻¹. (a) If s, t | M_σ then p ≡ 1 (mod st), so st | 1 + s + t, impossible for 3 ≤ s < t. (b) If Q_s is prime,
m ∈ {1, Q_s} and m ≡ 1 (mod s) in both cases, so g ≡ −1 (mod s) with g | 1 + s, g ≤ 1 + s. Then g = s − 1 and s − 1 | s + 1,
so s = 3, g = 2, t ∈ {2, 2Q_3}. Then t ≡ 2 (mod 4) and s = 3, so 4 ∤ st. (c) is the restatement. ∎

**Theorem 4.2 (least shift is unbounded under Dickson; CONDITIONAL on Dickson's prime k-tuples conjecture).** For every σ
there are infinitely many primes p ≡ 1 (4) such that the b = 1 line has no pair of shift ≤ σ.
*Proof.* Consider the linear forms in k: p = 1 + M_σ k and Q_s = 1 + (M_σ/(1 + s))k for 3 ≤ s ≤ σ. At k = 0 all forms equal 1, so
no prime divides all their values: the tuple is admissible. Dickson's conjecture gives infinitely many k with all forms
prime. For those, p ≡ 1 (mod M_σ), hence p ≡ 1 (mod 4), and Prop 4.1(b) kills every shift s ≤ σ. (Shifts s with s ≢ 0, 3
(mod 4) carry no pair anyway, Lemma 1.1.) ∎
*Reading.*
* This is B2's "fixed finite slice sets fail i.o. under H" (redteam-automorphic-2 Thm 2.2), now in its sharpest b = 1 form.
  The extremal primes are exactly those with p − 1 divisible by the full M_σ (the T1 point 1 in Ẑ) and with every shifted
  cofactor Q_s prime. **This is the mechanism behind "the three failures have p − 1 11-smooth".** Smoothness of p − 1
  freezes every small shift into the rigid form Q_s ≡ 1 (mod s) and kills all pairs supported on small primes (Prop 4.1(a)).
  What remains at shift s is one divisor-in-a-class event for Q_s.
* Unconditionally, Prop 4.1 explains the census records. 22 010 483 881 (least shift 215, §2) has p − 1 = 2³·3²·5·7·11·19·23²·79,
  and every prime < 41 is a QR mod p.
* Theorem 4.2 does NOT reach the full line. The full line uses all shifts s ≤ 1 + √(p + 1). A Dickson-type construction would
  need ≍ √p simultaneous prime cofactors, and the forms 1 + (M/(1+s))k cannot all be prime for s up to a power of p (the
  modulus M_σ would exceed p). So B2's finite-slice obstruction does not apply to the line itself. The line can only fail by a
  large deviation of many independent large-shift events (§3).
(Check of Prop 4.1: `z29_freeze_check.py 2·10⁹`, all primes p ≡ 1 (mod M₇ = 176 400) and (mod M₁₁ = 64 033 200) below
2·10⁹: 16 719 + 47 shift-s pairs, the two descriptions agree exactly; in all 2 776 + 24 cases with Q_s prime there is no
pair; `logs/z29_freeze_check.txt`.)
