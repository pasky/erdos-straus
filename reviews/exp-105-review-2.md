# EXP_105 (O239) — hostile review #2 (R254), round 1

**Repairs applied (round 2, R254; after merging R253's branch side-agent/review-exp-105-2 and side-agent/exp-105).**
D1 and the novelty sentence of D6 were already applied by R253. Applied by R254 in EXP_105.md, marked '(R254 repair)':
D2 (Obs 2.1: corrected non-contradiction reason), D3 (Prop 2.4: "near μ = 0" made precise, fixed *odd* primes, 2-power
remark), D4 (§2: explicit definition of the z14 window menu incl. unsplit Y-pieces; Cor 2.8 statement scoped to it;
compactness step spelled out incl. ET/D_q/n-splitting at μ = 0), D5 (Cor 2.5 EVIDENCE sentence → PROVED by Cor 2.8),
D6 (pointer to EXPONENT_COVERING §5.4). AGENT_REPORT_O239 Caveats: menu pointer, novelty, review status.
Correction to my D4 text: R253 is right that the magnitude bound does NOT extend to sub-products mixing primes of both SG
numerators (my "the magnitude bound to sub-products" was too generous); the R253-repaired caveat in Cor 2.8 stands.

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

**Obs 2.1 mechanism (n-piece not needed).** `review_r254_cert.py 3 1 cert_c3_k1.txt 100 --no-n` (n removed from the
window piece list): OK — confirmed for (3, 1). For (7, 9) the n-piece IS needed elsewhere (the m = 103 leaf at
u = 272 mod 612 fails without it); the μ = 0 leaf itself works without n (closed form above). Obs 2.1 only claims the
former, so no defect — but see D1 for the stale "plus the n-piece" in the Thm 2.2 *Significance* paragraph.

**Outside the ET/divisor menu.** (7, 9): 4 ∤ 7, 9 ≡ 1 (8), 7 + 9 = 4² ⇒ EXP_NEAR_SQUARE Lemma 3.1 (re-read on main):
ν(0) is a profinite unit square (odd components 16, 2-component k = 9 ≡ 1 mod 8), so by EXPONENT_COVERING Thm 1.4
(+ T1 via Mordell/Schinzel as quoted by ET, not re-accessed by me) no finite ET + divisor covering exists. 3·2^m + 1:
Cor 1.5 with k = 3 = 4 − 1. The odd half 6·4^s + 1 has c₀ ≡ 2 (4), no unit-square point, and is indeed ET-covered
(2 leaves) — consistent. Mordell-hardness claims re-computed: 7·4^s + 9 ≡ 121 (mod 840) for every even s ≥ 2;
3·4^s + 1 is Mordell-hard iff s ≡ 0 (6) (≡ 529 mod 840); 6·4^s + 1 never. All as stated.

## 2. Prop 2.4 / Cor 2.5 (re-derived)
At s ≡ 0 (mod P) one has 4^s ≡ 1 (mod m), so every piece's residue equals its S-integer limit: n → c₀ + k = 4^J,
Y = 4^r + t → 4^{−j}R, R = 1 + 4^j t (odd). m = c₀4^j t − k ≡ −k ≡ 3 (mod 4). For an odd prime q | c₀R: q | R ⇒
4^j t ≡ −1 ⇒ m ≡ −c₀ − k = −4^J; q | c₀ ⇒ m ≡ −k ≡ c₀ − 4^J ≡ −4^J (mod q). In particular q ∤ m, so all odd
pieces are units, and (q/m) = (m/q)(−1)^{(q−1)/2} = (−1/q)(−1)^{(q−1)/2} = +1. A relation d₁ ≡ −d₂ gives
(d₁d₂/m) = (−1/m) = −1, so the total 2-exponent i of the limit of d₁d₂ must be odd with (2/m) = −1. ✓.
Cor 2.5: J ≥ 2 ⇒ c₀ ≡ 7 (8). j ≥ 2 ⇒ m ≡ −k ≡ 7 (8), (2/m) = 1. j = 1: t odd ⇒ m ≡ 3 (8) but E = 0 and Y odd, so
no 2-power is available (n → 4^J has even exponent); t even ⇒ m ≡ 7 (8). ✓ (The "split by fixed primes" clause is safe
even for the prime 2: (2/m) = −1 forces j = 1, t odd, Y odd — see D3.)

## 3. Prop 2.7 / Cor 2.8 (re-derived + from-scratch search)
Re-derivation of the S-integer limits at μ = 0 (h | j etc. is exactly the condition that the window's parity/h-class
contains 0):
* code 0 (t = w^h, h | j): Y_e = 4^{−jD_e/h}·G_e with G_e = hom-Φ_{2e}(1, w·4^{j/h}) odd, ∏G_e = R. Even 2-power,
  odd divisor of R ⇒ symbol +1; 2^E needs (2/m) = −1 ⇒ j = 1 ⇒ h = 1 ⇒ Cor 2.5.
* code 1 (t = 4w⁴, j even): pieces 2^{−j}(1 ± w2^{j/2+1} + 2w²2^j)… even 2-power ⇒ +1; (2/m) = 1 anyway.
* code 2 (t = w⁴, j odd): pieces 2^{−j}G±, G± = 1 ± w2^{(j+1)/2} + w²2^j odd: odd 2-exponent, symbol (2/m).
  j ≥ 3 or w even ⇒ m ≡ 7 (8), (2/m) = 1 ⇒ sterile. j = 1, w odd ⇒ m ≡ 3 (8): survives. ✓
Cor 2.8: Jacobi ⇒ exactly one A-atom (A₊ and A₋ each have symbol −1). Relation ⇔ GU + 2V ≡ 0 (mod m) with
U, V disjoint, UV | c₀4^J, G = 2w² ± 2w + 1; 0 < GU + 2V ≤ c₀4^J(2w² + 2w + 3) < m = 4c₀w⁴ − k for large w ✓.

`review_r254_mu0.py 9 8` (pure modular limits, FULL sign/2-power search, no Jacobi shortcut; cross-checked against
residues at actual exponents s ≡ 0 mod P for 14–22 windows per family): every window of the menu with j ≤ 9,
w ≤ 8, h ∈ {1,3,5,7,9,15} (codes 0/1/2) whose class contains 0, plus sg1/j = 1/odd w up to the magnitude bound:
| (c₀, k) | windows containing 0 | relations |
|---|---|---|
| (15,1), (31,33), (7,57), (63,1), (47,17), (55,9) | 189–192 each | **none** |
| (3,1) / (7,9) / (23,41) / (39,25) | 192 each | only sg1 j = 1 w = 1: m = 11 / 19 / 51 / 131 |
Exactly as claimed.

Compactness step (Cor 2.8 "⇒ no finite covering"): {s ≥ s₀} is dense in Ẑ, a finite union of clopen classes covering
it is all of Ẑ, so some class must contain 0; ET classes cannot (Thm 1.4/T1), D_q cannot (q | 4^J impossible), and
no z14 window can (above). The z14 search code also splits n by fixed small primes q; at μ = 0 that is vacuous
(q | n on a cylinder containing 0 ⇒ q | 4^J). ✓ — but the text should say so (D4).

## 4. Defects
None FATAL, none MAJOR.

**D1 (MINOR) — EXP_105 §2, Thm 2.2 *Significance*:** "one window shape (the Aurifeuille/Sophie-Germain factorisation
of 4^r + 1 plus the n-piece) removes the obstruction" contradicts the corrected Obs 2.1 (n-piece not needed; verified by
my `--no-n` replay). *Repair:* delete "plus the n-piece".

**D2 (MINOR) — Obs 2.1, last sentence:** "a window class is a congruence class in s and contains no integer square n"
is false as written (the μ = 0 class s ≡ 0 (36) of 7·4^s + 9 contains s = 0, n = 16 = 4²; s = 0 is merely outside the
window's validity range r ≥ 1) and is not the reason there is no contradiction: Mordell/Schinzel/ET Prop 1.6 restrict
*polynomial-in-n* solutions on *n-residue classes*; a window identity is neither, and if a window class contained an odd
square it would simply give a valid solution for it. *Repair:* "Not a contradiction: T1 / Thm 1.4 concern classes of n
solvable by polynomials in n; a window class is a clopen set of exponents whose identity is not polynomial in n."

**D3 (MINOR) — Prop 2.4 statement:** "near μ = 0" should be made precise ("on the cylinder s ≡ 0 (mod P), where all
residues equal the S-integer limits"), and "split by fixed primes" should read "by fixed odd primes" or note that a
split-off 2-power is harmless because (2/m) = −1 forces j = 1, t odd, Y odd. The proof's "except the 2-powers" is then
literally correct.

**D4 (MINOR) — Cor 2.8 / Status paragraph / report SHARP 3, scope:** "the z14 window menu" is defined only implicitly
(by the code `make_windows`/`pieces_at`). State it in the text: windows m = c₀4^j t − k, j ≥ 1, t ∈ {w^h (h odd),
4w⁴, w⁴} for all w ≥ 1; pieces 2^i (|i| ≤ E), odd primes of c₀, n (optionally split by fixed primes), the
*unsplit* cyclotomic/SG factors of 4^r + t; and add the one-line remarks that n-splitting is vacuous at μ = 0 and that
ET/D_q classes miss μ = 0. Note Prop 2.4 is stated for split Y while Cor 2.8's finite check is for unsplit SG pieces
(the caveat is there; the Jacobi part does extend to splits by fixed odd primes, the magnitude bound to sub-products —
the author says so, but "not enumerated" should be in the statement, not only in the caveat).

**D5 (MINOR) — Cor 2.5 paragraph:** "(15, 1), (31, 33), (7, 57), (63, 1) no window found (EVIDENCE: up to 4744
windows …)" is superseded by Cor 2.8 (PROVED for the menu). *Repair:* add "(now PROVED for the z14 menu, Cor 2.8)".

**D6 (MINOR) — novelty:** EXP_105 makes no literature statement for Thm 2.3/2.6. EXPONENT_COVERING §5.4 (2026-10-13,
non-exhaustive) found no prior "ES for all k·2^m + 1"; my quick web search (Jina, 2 queries) found nothing either.
*Repair:* one sentence pointing to §5.4 ("no prior statement found; non-exhaustive").

## 5. Bottom line
The headline is sound: ES holds for every 7·4^s + 9 and every 3·2^m + 1 (PROVED, computer-assisted), independently
re-verified by a from-scratch checker (exact measure-1 partition of Ẑ, every leaf proved on its whole cylinder,
explicit solutions for all s ≤ 1500, mutation-tested). The Jacobi sterility results (Prop 2.4–Cor 2.8) re-derive
correctly and are confirmed by an exhaustive limit search; their scope ("relative to the z14 window menu") is stated
but should be made explicit in the text (D4). Only MINOR wording repairs are needed.
