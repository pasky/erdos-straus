# s7_window_lottery — the least cap-0 window m₀(p) is a congruence-modulated independent lottery (O247, mandatory (i))

## Idea
Wave Z closed thin families by windows whose exponent budget is *forced* by an algebraic factorisation of n − k.
For a prime p the brief asks whether *any* positive-density mechanism forces the budget at some window, and whether
the least cap-0 window m₀(p) is a polylog lottery or has structure (Mordell-hard classes, least non-residues).
Exact invariant: by CAP_DOWN Lemma 1.1 at cap 0 (c_s ≤ 2b_s ⟺ d | K²) and the Type II normal form
(x prime to p, p | y, p | z), for a prime p ≡ 1 (4)

  **m₀(p) := min{4x − p : 4/p = 1/x + 1/y + 1/z, p ∤ x, p | y, p | z} = min{m ≡ 3 (4) : ∃ d | K_m², d ≡ −K_m (mod m)}, K_m = (p+m)/4**

(R-O247 review fix: the first version took the minimum over all solutions with p ∤ x and identified m₀ with 4·x_min − p;
that is false, since a Type I solution can have p ∤ x — e.g. 4/16921 = 1/4233 + 1/6511516 + 1/5619249474036 has 4x − p = 11
while the least Type II window is 15.) The windows m = 3, 7, 11, … are the consecutive integers K_m = K₃, K₃ + 1, K₃ + 2, …

## Literature
Mordell's six classes mod 840 (Mordell 1967, Diophantine Equations §30); e-slice form and its B2 reduction:
reviews/redteam-automorphic-2.md Thm 2.2 (fixed finite slice sets fail i.o. under H); "−1 ∈ ⟨q mod c : q | K_c⟩"
is Dahan arXiv:2608.24035 Prop 4.8 ((J)64 prior art). The quantity x_min(p) − p/4 appears implicitly in every
Type II search; no distributional study of it was found in the campaign files (grep "x_min", "least window").

## Barrier screen
* B1/T1: m₀ is +∞ at every odd square (CAP_DOWN T1 for Lemma 1.1). Checked: no odd square ≤ 10⁷ has a cap-0 window
  m ≤ 400 (`s7_window_controls.py`); also none for n = 105 and n = 3985 (the CAP_DOWN anomaly).
* B2: a window m fires iff K_m has a divisor ratio ≡ −1 (mod m) (e-slice form). For a fixed finite window set W,
  redteam-automorphic-2 Thm 2.2(iii) gives infinitely many failing primes under H. Explicit instances (CONDITIONAL on
  Dickson's prime k-tuples conjecture): `s7_dickson_classes.py` finds residue classes r mod L in which every window
  m ≤ M fails when each rough part (p+m)/(4S_m) is prime, for M = 11, 27, 47, 63, 99 (e.g. r = 1000000434889 for M = 99);
  Dickson admissibility holds because L contains every prime ≤ M (> #forms). So m₀ is unbounded under Dickson.
* B6: nothing averaged; the statistics below are descriptive only.

## Cheap numerics (scripts/s7_window_excess.py, s7_window_shuffle.py, s7_window_controls.py)
* All 332 180 primes p ≡ 1 (4) ≤ 10⁷ have m₀(p) ≤ 107; records (p, m₀): (73, 7), (1129, 11), (1201, 23), (21169, 31),
  (67369, 35), (87481, 63), (1430641, 71), (8803369, 107). m₀/log²p ≈ 0.4–0.5 at the records.
* Histogram ≤ 10⁶ (39 175 primes): m₀ = 3: 34 635; 7: 3 551; 11: 584; 15: 131; 19: 113; 23: 96; 31: 33; larger: 32.
* **Mordell split (PROVED, below; checked to 10⁷).** m₀(p) ≥ 11 only for p in the six Mordell-hard classes mod 840.
  Mean m₀ is 3.33 off those classes and 8.98 on them (≤ 10⁶).
* **Independence test (EVIDENCE).** Conditional permutation test: split K_m = S_m R_m (S_m = part on primes ≤ B),
  permute the rough parts R_m among primes in the same block of 2000 primes, same m, same R_m mod m and same bit length
  (so K' ≡ K (mod m) and all small-prime/congruence structure of p is kept, but rough parts of different windows
  become independent). Tail counts #(m₀ > M), M = 3, 7, 11, 19, 27, 35, 47, primes ≤ 10⁶:
  actual 4540, 989, 405, 161, 57, 20, 7; shuffled (B = 47, four runs) 4536–4561, 958–995, 391–416, 149–167, 47–56,
  15–21, 3–9; (B = 13) 4540–4572, 1008–1056, 427–456, 175–200, 55–67, 17–23, 3–7.
  A naive model conditioning only on p mod 8 and the Legendre symbols (p/ℓ), ℓ | m, under-predicts the tail 3–9×
  (M = 19: 48 vs 161): within the resolution of four shuffles, the correlation between windows is carried by the shared
  small prime factors (ℓ | K_m ⟺ p ≡ −m (mod ℓ)), i.e. by B1/Haar-CRT data (no residual correlation detected; not a proof
  that none exists).

**Proposition 1 (Mordell's theorem in window form; PROVED, elementary).** Let p ≡ 1 (4) be prime outside the classes
1, 121, 169, 289, 361, 529 (mod 840). Then m₀(p) ∈ {3, 7}.
*Proof.* Write K = K_m. (a) p ≡ 2 (3): m = 3, K ≡ 2 ≡ −1 (mod 3), d = 1. (b) p ≡ 5 (8): m = 3, 8 | p + 3 so K is even,
d = K/2 gives K + d = 3K/2 ≡ 0 (mod 3). Remaining: p ≡ 1 (24). (c) p ≡ 2 (5): m = 3, 5 | K, K ≡ 1 (3), d = 5 ≡ −1.
(d) p ≡ 3 (5), p ≡ 1, 2, 4 (7): m = 7, 2 | K and 5 | K (p + 7 ≡ 0 mod 8 and mod 5), K ≡ 2p (mod 7), −K ≡ 5, 3, 6;
take d = 5, 10, 20 (d | K²: c₂ ≤ 2 ≤ 2b₂, c₅ = 1). (e) (p/7) = −1, p ≡ 1 (8): m = 7, K even, −K ≡ −2p ∈ {1, 4, 2}
for p ≡ 3, 5, 6 (mod 7): d = 1, 4, 2. The excluded classes are exactly p ≡ 1 (24), p ≡ ±1 (5), p ≡ 1, 2, 4 (7). ∎

## Assessment
EVIDENCE + PROVED (Prop 1) + CONDITIONAL (Dickson classes). The least window is a lottery in the precise sense that,
once the congruence (small-prime) structure of the consecutive integers K₃, K₃ + 1, … is fixed, the rough parts act as
independent draws; there is no residual correlation with the Mordell-hard classes beyond the congruence data that
defines them (within the test's resolution), and no positive-density forcing mechanism is visible. m₀(p) grows like a small power of log p at the
records. Answer to (i): "is m₀ ~ log p or structured?" — structured exactly to the extent of B1, lottery beyond.
