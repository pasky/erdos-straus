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

**2.1 All primes p ≡ 1 (4) ≤ 10¹¹** (`z29_census`, segmented factor tables, least s with a hit, exact fallback over all
s ≤ 1 + √(p + 1) when no hit with s ≤ 512; logs `logs/z29_census_1e10.txt`, `logs/z29_census_1e11.txt`). Prime counts sum to 227 523 275 = π(10¹⁰; 4, 1)
(confirmed by an independent segmented Eratosthenes count, `pcount`, not kept) and to 2 059 020 280 = π(10¹¹; 4, 1) (the
known value, OEIS A091115 — from memory, not re-checked). **No b = 1 failure in (66529, 10¹¹].**
| range | primes p ≡ 1 (4) | b = 1 failures | fallback calls | max least s (at) |
|---|---|---|---|---|
| ≤ 10⁸ | 2 880 504 | 193, 2521, 66529 | 3 | 119 (1 683 049) |
| (10⁸, 5·10⁹] | 114 594 477 | 0 | 0 | 111 (277 977 001) |
| (5·10⁹, 10¹⁰] | 110 048 294 | 0 | 0 | 104 (6 098 002 681) |
| (10¹⁰, 5.5·10¹⁰] | 933 583 091 | 0 | 0 | 215 (22 010 483 881) |
| (5.5·10¹⁰, 10¹¹] | 897 913 914 | 0 | 0 | 116 (58 441 300 009) |
Distribution of the least s, ≤ 10¹⁰ (log₂-bins [2,4), [4,8), …): 2.07·10⁸, 1.84·10⁷, 1.82·10⁶, 1.28·10⁵, 4 211, 94, 0.
The least hitting s grows only slowly: record 119 ≤ 10⁸, then 215 at 2.2·10¹⁰ (unbounded under Dickson, Thm 4.2). Every global record from p = 73 on is at
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

## 3. The heuristic model: main term, dispersion, and a finite-failure prediction

**Lemma 3.1 (incidence form and main term; PROVED, elementary, as PARITY_AUDIT Lemma 2.1).** For p ≡ 1 (4) prime,
  N₁(p) = #{(c, d) ∈ ℕ² : (4cd − 1) | p + 4d},
and each incidence is a distinct ES solution (ad, acdp, cdp). The Haar main term is
  M₁(p) := Σ_{c,d ≥ 1, 3(4cd − 1) ≤ p + 4d} 1/(4cd − 1) = (log p)²/8 + O(log p)
(the factor 3: every incidence has cofactor g = (p + 4d)/w ≡ 3 (mod 4), so g ≥ 3).
For the c = 1 line, PARITY_AUDIT's R(p) = #{(u, B, C) : 4uBC = p + u + B} has the same main term (log p)²/8. But (u, B, C)
and (B, u, C) give the same triple {uBC, pBC, puC}, so the number of distinct (★) solutions is N_{c1}(p) = (R(p) + ε)/2,
ε ∈ {0, 1}, with main term (log p)²/16.
*Proof.* By SYNTHESIS_SPARKS8 Prop 1.3 (López Thm 7), with w = 4cd − 1: w | cp + 1 ⟺ w | p + 4d, because 4cd ≡ 1 (mod w)
gives 4d(cp + 1) ≡ p + 4d (mod w) and gcd(w, 4d) = 1; then a = (cp + 1)/w ≥ 1. Distinctness: 8d ≤ p + 3 and a < p, so
p ∤ x = ad while p | y, z. So x is identified, z = min(y, z) = cdp, a = y/z, d = x/a, c = z/(dp). Main
term: d ≤ (p + 3)/8, and for fixed d, c runs to (p + 4d + 3)/(12d), giving Σ_c 1/(4cd − 1) = (1/(4d))(log(p/(12d)) + O(1)) +
O(1/d²); summing, Σ_{d ≤ (p+3)/8} (1/(4d)) log(p/(12d)) = (log p)²/8 + O(log p). For (★): the swap (u, B) ↦ (B, u) is an
involution on R's incidences with at most one fixed point (u = B forces u | p, u = 1, 2 = p + 2 − 4C·… impossible: u = B = 1
needs 4C = p + 2, odd), and swapped incidences give the same unordered triple. ∎
(Numerically M₁ = 13.3, 19.8, 27.6 at p = 10⁵, 10⁶, 10⁷, against (log p)²/8 = 16.6, 23.9, 32.5, so the O(log p) term is
≈ −0.3 log p. The class p ≡ 1 (24) runs ≈ 13 % above the unconditioned M₁: 22.3 against 19.8 at 10⁶.)
**So the b = 1 line has twice as many independent trials as (★).** Per distinct solution, the main terms are (log p)²/8 and
(log p)²/16. Empirically (class samples, `logs/z29_classes.txt`): N₁/(log p)² = 0.117, 0.124, 0.131, 0.135 at p ≈ 10⁶, 10⁸,
10¹⁰, 10¹² (p ≡ 1 (24)), and N_{c1}/(log p)² ≈ 0.070–0.074. The ratio N₁/N_{c1} is 1.67, 1.69, 1.78, 1.85, tending to 2 as
the O(log p) terms fade. Add Prop 1.4 (the b = 1 nontrivial class p ≡ 1 (24) is half the size of the (★) class p ≡ 1 (8)),
and this answers "why is the shift-4d family far more robust than (★)": **twice the main term (the b = 1 incidences are
asymmetric; (★) incidences come in swapped pairs) and half the exposed classes.** Class hardness hits both lines equally
(below). It is not the explanation.

**3.2 Dependence on the smooth part of p − 1 (EVIDENCE).** Mean N₁/(log p)² in the classes p ≡ 1 (mod M_σ) (§4), at
p ≈ 10¹²: 0.135 (M = 24), 0.127 (M₅ = 1800), 0.117 (M₇ = 176 400), 0.108 (M₁₁ = 64 033 200). So p ≡ 1 (M₁₁) costs 20 % of the
mean, and (★) loses 16 % in the same classes. The loss is the Haar mass of the pairs frozen by Prop 4.1. It is O(log p) in
absolute terms (pairs with one coordinate ≤ σ), hence a vanishing fraction of (log p)²/8 as p → ∞.

**3.3 Dispersion and the zero tail (EVIDENCE; `z29_model.py`, all 15 648 primes p ≡ 1 (24) ≤ 10⁶ plus 20 000 / 4 000
consecutive p ≡ 1 (4) from 10⁸ / 10¹⁰; `logs/z29_model.txt`).** N₁ is overdispersed: var/mean = 1.2–2.3 at p ≤ 10⁶,
2.7 at 10⁸, 3.2 at 10¹⁰. Clumping comes from p + s with many divisors. The relative spread √(D/μ) still shrinks:
0.33, 0.25, 0.22. Model: N₁ | p ~ negative binomial with the bin mean (scaled by log² p) and dispersion D, so
P(N₁ = 0) = D^{−μ/(D−1)}. Back-test ≤ 10⁶ (bins with ≥ 30 primes): predicted zeros 1.18, observed 2 (2521, 66529);
predicted #{N₁ ≤ 2} = 16.4, observed 33. So the model underestimates the lower tail by a factor ≈ 2 (up to 5 in the largest
bins). The same model for (★) (class p ≡ 1 (8)): predicted zeros 3.4, observed 7 in the same bins. That is the same factor 2,
so the model is consistently optimistic by about 2 for both lines.
**3.4 Prediction.** With μ = 0.125 (log p)² and D = 3.24 (the largest observed), the expected number of b = 1 failures
beyond X is 0.037 (X = 10⁶), 1.1·10⁻⁴ (10⁸), 1.4·10⁻¹⁰ (10¹¹). Depressing μ by 20 % everywhere (every prime treated as
in the hardest class M₁₁) gives 0.68, 0.013, 8·10⁻⁷. Even with the factor 2–5 tail correction, the expected count beyond
10¹¹ is < 10⁻⁵. For (★) the same model gives 1.8 (beyond 10⁸) and 0.003 (beyond 10¹¹), or 50 / 0.86 with the 20 % depression;
tested in §3.6.
**3.6 Out-of-sample test on (★) (EVIDENCE; `Z29_LINE=2 z29_census`, complete, `logs/z29_census_c1_1e10.txt`).** The same engine
reproduces the 14 (★) failures ≤ 10⁸ of PARITY_AUDIT/O258 exactly and finds **no (★) failure in (10⁸, 10¹⁰]** (225 million
primes; max least shift 343). The NB model predicted ≈ 1.7 failures there (≈ 3.5 with the small-p factor-2 correction).
P(0 | mean 1.7) ≈ 0.18 and P(0 | 3.5) ≈ 0.03. So at large p the model is, if anything, pessimistic: the small-p tail
inflation does not seem to persist. Combined with §3.4, the b = 1 prediction (< 10⁻⁴ failures beyond 10⁸) is conservative.
(This also extends PARITY_AUDIT's (★) census from 10⁸ to 10¹⁰: still exactly 14 failures.)
**Conjecture 3.5 (finitely many b = 1 failures; CONJECTURE, heuristic + EVIDENCE to 10¹¹).** The b = 1 line (López's Type A)
holds for every prime p ≡ 1 (mod 4) except 193, 2521, 66529. Heuristic basis: main term (log p)²/8 (Lemma 3.1) and
overdispersion D = O(1) give P(fail) ≈ exp(−c (log p)²). The only known mechanism for correlated failure, Dickson-type
freezing (Thm 4.2), acts on O(σ) shifts, costs only O(log p · log σ) of the mean, and cannot be applied to all ≍ √p shifts.
*Caveat (Assessment).* The negative-binomial model is calibrated only up to 10¹⁰ and is known to be optimistic by about 2 in
the tail. No proof idea follows from it: it is the polylog lottery of B3 with a better constant.

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
