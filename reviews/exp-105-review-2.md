# EXP_105 (O239) — hostile review #2 (R254), round 1

Reviewer: R254 (side-agent/review-exp-105). Round 1: no edits to the author's files. From-scratch scripts:
`scripts/review_r254_cert.py` (certificate checker), `scripts/review_r254_small.py` (independent small-member search),
`scripts/review_r254_closedform.py` (closed forms of the μ = 0 Sophie-Germain leaves). None imports z14_/z8/ec_cover.

## Summary verdicts
| Claim | Verdict |
|---|---|
| Thm 2.2 (ES for all 3·4^s + 1) | **SOUND** (certificate replayed from scratch; MINOR wording D1) |
| Thm 2.3 (ES for all 3·2^m + 1) | **SOUND** |
| Thm 2.6 (ES for all 7·4^s + 9) — HEADLINE | **SOUND** (PROVED, computer-assisted, label justified) |
| Obs 2.1 | SOUND-AFTER-REPAIRS (D2: wrong/false justification sentence; mechanism claim itself verified) |
| Prop 2.4 / Cor 2.5 | **SOUND** (re-derived; MINOR precision D3) |
| Prop 2.7 / Cor 2.8 | **SOUND relative to the z14 menu** (re-derived + from-scratch exhaustive μ = 0 search); MINOR D4 (menu must be defined in the text; n-splitting) |
| Labels / scope / novelty | SOUND; MINOR D5 (stale EVIDENCE sentence), D6 (literature sentence) |

No FATAL or MAJOR defects found.

## 1. Certificate replay (from scratch)

**Checker design** (`review_r254_cert.py c0 k cert SMAX`). Independent parser of the DFS-preorder stream; a leaf is the
cylinder {s ≡ u mod L}, built by CRT from the per-prime digits (split on ℓ refines μ_ℓ mod ℓ^e to mod ℓ^{e+1}, so the
leaves of a well-formed tree are pairwise disjoint), and the exact Haar measures of the leaves are summed in `Fraction`
(must equal 1 ⇒ the leaves partition Ẑ, hence every s ≥ 0 lies in exactly one leaf; additionally asserted for every
s ≤ SMAX). Every leaf is then proved valid on its WHOLE cylinder for s ≥ s₀(leaf):
* `D q`: q prime, ord_q(4) | L, q | c₀4^u + k ⇒ q | n_s on the cylinder; ES(q) solved explicitly and scaled.
* `P a d f` (ET II2): re-derived: with c = (f+1)/(4ad), e = (n + 4a²d)/f, b = ce − a one has 4abd = (f+1)e − 4a²d = n + e,
  hence cn + a + b = c(n + e) = 4abcd, i.e. 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn). Needs f ≡ −1 (4ad), f | n + 4a²d on the
  cylinder (ord_{q^e}(4) | L for each prime power of f — prime powers allowed, stricter than needed) and b > 0
  (s₀ computed exactly from c(n + 4a²d) > af).
* `I c d f` (ET I3): a = (n+f)/(4cd), b = (n² + 4c²d + nf)/(4cdf); integrality needs gcd(f, 4cd) = 1, n ≡ −f (4cd),
  f | n² + 4c²d; the 2-part of n mod 4cd is constant once 2s + v₂(c₀) ≥ v₂(4cd) (s₀ computed), odd part periodic with
  ord(4) | L checked.
* `W m j code w h` (window): m = c₀4^j t − k with t = w^h / 4w⁴ / w⁴; x = (n + m)/4 = c₀4^{j−1}(4^r + t), r = s − j ≥ 1;
  N = nx = 2^{2j−2+v₂(c₀)} · (odd primes of c₀) · n · ∏Y_i with Y_i the homogenised cyclotomic factors Φ_{2e} (e | h)
  of X^h + w^h (X = 4^{r/h}) or the Sophie-Germain pair (X² ± 2Xw + 2w²) (X = 2^{r/2}, r even) /
  (2X² ± 2Xw + w²) (X = 2^{(r−1)/2}, r odd); all three factorisations re-verified symbolically. With d₁, d₂ disjoint
  sub-products of these pieces (d₁ may carry 2^i, i ≤ E) and m | d₁ + d₂: y = N(d₁+d₂)/(md₂), z = N(d₁+d₂)/(md₁)
  (identity re-verified symbolically: 1/y + 1/z = m/N = 4/n − 1/x). The residues of every piece mod m depend only on
  s mod P, P = h·ord_m(4) (code 0) or 2·ord_m(2) (codes 1, 2), and the h | r / parity condition is constant on the
  cylinder since h, 2 | P; the checker asserts P | L and searches its OWN relation (3^{#pieces}·(E+1) sign patterns).
* Exceptions s < s₀ are solved directly (independent divisor search).
* Sanity: for every s ≤ SMAX an explicit (x, y, z) is built from the unique covering leaf (window relation re-found on
  the actual integers) and 4xyz = n(xy + yz + zx) is verified exactly.

**Results** (`ulimit -v 8000000`, SMAX = 1500 for all three certificates):
| certificate | leaves | D/P/I/W | measure | exceptions | explicit s ≤ 1500 |
|---|---|---|---|---|---|
| cert_c3_k1 (3·4^s + 1) | 9 | 2/3/1/3 | 1 | {0} (n = 4) | 1500 OK |
| cert_c6_k1 (6·4^s + 1) | 2 | 1/0/1/0 | 1 | {0} (n = 7) | 1500 OK |
| cert_c7_k9 (7·4^s + 9) | 59 | 4/7/8/40 | 1 | {0} (n = 16) | 1500 OK |

Counts match the text (59 leaves, 40 windows, 7 II2, 8 I3, 4 D). Mutation tests (wrong window code at the μ = 0 leaf,
wrong II2 prime, wrong D prime, wrong split prime, wrong I3 modulus) are all rejected by my checker.

**Independent small search** (`review_r254_small.py`, per-x divisor search with Fraction verification, no certificate):
ES solutions for 7·4^s + 9, s ≤ 11 and 3·2^m + 1, m ≤ 30 — all found.

**T1 / squares.** 7·4^s + 9 = y² ⇔ (y−3)(y+3) = 7·4^s; parity + (b − a = 3, ab = 7·4^{s−1}) leaves only s = 0 (16)
and s = 2 (121 = 11²). 3·2^m + 1 = y² ⇔ (y−1)(y+1) = 3·2^m: m ∈ {0, 3, 4} (4, 25, 49). Covering leaves: s = 2 of
(7, 9): `D 11` (u = 2 mod 3060); 49 = 3·4² + 1: `D 7`; 25 = 6·4 + 1: `D 5`; n = 16, 4: direct. All odd squares are
handled by divisor leaves (genuine solutions), never by a polynomial ET class — no T1 conflict.

**Closed forms of the μ = 0 leaves** (`review_r254_closedform.py`, derived by hand and verified symbolically).
For s even, b = 2^{(s−2)/2}, A± = 2b² ± 2b + 1 (A₊A₋ = 4^{s−1} + 1), m = 4c₀ − k, x = c₀A₊A₋:
y = c₀nA₋(c₀ + A₊)/m, z = nA₊A₋(c₀ + A₊)/m, valid whenever m | c₀ + A₊. (3, 1): m = 11, period 20, fires at
s ≡ 0, 6 (mod 20) (A₋-version at s ≡ 10, 16); (7, 9): m = 19, period 36, fires at s ≡ 0, 8 (mod 36) (A₋: 18, 26).
At μ = 0 (b → 1/2): c₀ + A₊ → c₀ + 5/2 = m/2 exactly for both, confirming Obs 2.1's mechanism (the n-piece is not
needed). The author's displayed closed form for Thm 2.2 (relation nA₊ + 1 ≡ 0 mod 11) is a different but equally
valid relation (n → 4: 4·5/2 + 1 = 11); I verified it is consistent.
