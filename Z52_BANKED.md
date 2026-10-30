# Z52 lane B — banked board items and the slate's cheap tests

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (not refereed).

Sources: boards `~/.pi/boards/20261030-es-generators` and `~/.pi/boards/20261030-es-weakpoints` (memo + items + rounds).
Scripts `scripts/z52_bank_*`, data `data/z52_bank/`.

## Summary

(to be written last)

## Part 1 — banked items

### 1(a) fable-7: the pencil S_{n,k}, Lemma A, and the class (−q, −d)

Sources: generators board, `items/fable.md` (fable-1, Lemma A/B/C), `rounds/01-argon.md` (argon's proof of Lemma A),
`rounds/03-astra.md` §1 (the repaired class and local evaluation), `rounds/04-argon.md` §2.1 (2-adic audit). Everything below
was re-derived here; the proof of Lemma A is a uniform Hilbert-reciprocity argument, not argon's Jacobi computation.

**Setting.** For odd n ≥ 1 and k ∈ ℤ let S_{n,k} : 4xyz − n(xy + yz + zx) = k ⊂ 𝔸³_ℚ (k = 0 is the Erdős–Straus surface U_n
of Bright–Loughran). Put q = 4y − n, d = qz − ny, d′ = qx − ny. On S_{n,k} (one-line expansions):

  (I1) x·d = k + nyz,  (I2) d·d′ = n²y² + kq,  (I3) 4d = q(4z − n) − n²  (identically, no equation needed),

and also q·xz = k + n(xy + yz). S_{n,k} is smooth unless k ∈ {0, −n³/4} (the gradient vanishes only at (0,0,0) and at
x = y = z = n/2). For k > 0 every positive point has q > 0 and d > 0 (by the last identity and (I1)).

**Theorem 1(a) (PROVED; generalises the board's Lemma A).** Let m ≥ 1, k = m², and n odd with
  n ≡ 1 (mod 8) if m is even,  n ≡ 5 (mod 8) if m is odd,  and (n/ℓ) = +1 for every odd prime ℓ | m.
Then S_{n,k}(ℕ) = ∅. In particular (board's Lemma A) S_{n,4}(ℕ) = ∅ for n ≡ 1 (8), and S_{n,1}(ℕ) = ∅ for n ≡ 5 (8).

*Proof.* Let (x,y,z) be a point with x,y,z ∈ ℤ_ℓ on S_{n,k} at a finite place ℓ, with q, d ≠ 0. We show (−q, −d)_ℓ = +1.
* ℓ odd, ℓ ∤ qd: both entries are units, symbol +1.
* ℓ odd, ℓ | q. If ℓ | n then ℓ | y, so the equation mod ℓ gives k ≡ 0; for ℓ ∤ m this is impossible, and for ℓ | m it is
  excluded by (n/ℓ) = +1. So ℓ ∤ n and (I3) gives −d ≡ (n/2)² ≢ 0 (mod ℓ): −d is a unit square, symbol +1.
* ℓ odd, ℓ | d, ℓ ∤ q. If ℓ ∤ m: by (I2) kq ≡ −n²y², so ℓ ∤ ny (else ℓ | kq) and −q ≡ (ny/m)² is a nonzero square mod ℓ.
  If ℓ | m: (I2) gives ℓ | n²y², ℓ ∤ n, so ℓ | y and −q = n − 4y ≡ n, a nonzero square mod ℓ by hypothesis. Symbol +1.
* ℓ = 2 (q = 4y − n is odd). If −q ≡ 1 (8) it is a 2-adic square. Otherwise −q ≡ 5 (8) and it suffices that d is odd, because
  (u, w)₂ = +1 for units u ≡ 1 (4). m even, n ≡ 1 (8): y even gives −q ≡ 1 (8); y odd gives −q ≡ 5 and
  dd′ = n²y² + kq ≡ 1 + kq ≡ 1 or 5 (mod 8) (as 4 | k), so d is odd. m odd (k ≡ 1 (8)), n ≡ 5 (8): y odd gives
  −q ≡ n − 4 ≡ 1 (8); y even gives −q ≡ 5 and dd′ ≡ kq (mod 4) odd.
For a point in ℕ³ we have q, d > 0, so (−q, −d)_∞ = −1, while all finite symbols are +1: this contradicts Hilbert
reciprocity ∏_v (−q, −d)_v = 1. ∎

**The class (PROVED).** 𝒜 := (−q, −d) ∈ Br S_{n,k} for every square k = m² ≠ 0 (n odd). Proof: S is smooth, so by purity
it suffices that all residues vanish; the only possible ramification is along {q = 0} ∪ {d = 0}. {q = 0} is the line
y = n/4, x + z = −4k/n², on which −d = (n/2)² is a square. On {d = 0}, (I2) gives −q = (ny/m)², a square in the residue
field (the components are lines over ℚ(√(k(4k + n³)))); so the residue (−q)^{v(−d)} is trivial. Under the hypotheses
of Theorem 1(a) the proof above says exactly: inv_ℓ 𝒜 = 0 on all of S(ℤ_ℓ) for every prime ℓ (points with qd = 0 by local
constancy), while inv_∞ 𝒜 = 1/2 on the positive real locus. The adelic set S(ℝ)_{>0} × ∏_ℓ S(ℤ_ℓ) is non-empty
(PROVED: positive real point x = z = n, y = (k + n³)/(2n²); for any ℓ choose y with q a unit, then z with d ≡ 1 mod ℓ —
z ≡ 1 + y (mod 2) when ℓ = 2 — and x = (k + nyz)/d ∈ ℤ_ℓ by (I1)). So Theorem 1(a) is a **Brauer–Manin obstruction to
positive integral points** on a locally soluble surface, for a positive-density set of n for each square k:
density (1/8)·∏_{ℓ | m odd} (ℓ − 1)/(2ℓ) among all n. 𝒜 is not constant (inv_∞ = 0 at (0, 1, −4/n) ∈ S_{n,4}(ℚ) for n > 4).
The board proved the k = 4 and k = 1 cases (astra R3, argon R4); the uniform statement for all squares k is new here.
The class is ramified for non-square k (residue k along {d = 0}), consistent with the data below.

**Where the obstruction fails (PROVED).** For k = 4, n ≡ 5 (8): the 2-adic point (2, 4, 2(2n+1)/(16 − 3n)) has v₂(d) = 1 and
−q ≡ 5 (8), so inv₂ 𝒜 = 1/2, and 𝒜 does not obstruct; n = 5 has the solution (2, 4, 22). The full Br S_{n,4}/Br ℚ is not
computed (open, as on the board).

**Numerical checks (CERTIFIED; `scripts/z52_bank_pencil.c`, cross-checked by the brute force `z52_bank_pencil_brute.py`
on all 9 ≤ n ≤ 300 for k = 4, −4, 1: identical counts).** The complete search uses: with x ≤ y ≤ z, n/4 < x ≤ 3n/4 (for
k > 0: 4/n > 1/x and 4x³ ≤ 3nx² + k; for k = −4: 4/n − 1/x = 1/y + (1/z)(1 − 4/(nxy)) > 0 and 4/n < 3/x), and for fixed x,
m = 4x − n, (my − nx)(mz − nx) = n²x² + km, so all (y, z) come from divisor pairs of one integer (both signs enumerated).
* k = 4: S_{n,4}(ℕ) = ∅ for all 1 249 values n ≡ 1 (8), 9 ≤ n ≤ 10⁴ (complete search). For n ≡ 5 (8), 13 ≤ n ≤ 10⁵, a
  solution exists for every n **except n = 3861 = 3³·11·13** (complete search): a failure that 𝒜 does not explain
  (the board's "≠ ∅ for every n ≡ 5 (8) ≤ 1200" is correct but does not extend).
* k = 1: S_{n,1}(ℕ) = ∅ for all n ≡ 5 (8), 13 ≤ n ≤ 10⁴. Among n ≡ 1 (8) ≤ 10⁵ the zeros are exactly 9, 33, 81, 345, 825,
  921, 1305, 3777, 3969, 4809, 5889, 7161, 8361, 11025, 14505, 16617, 26025, 26385, 55425, 99825 (all divisible by 3).
  The board's Lemma C list "{9, 81, 345}" (n ≤ 400) omits 33 (two independent codes agree that S_{33,1}(ℕ) = ∅).
* Other squares (n ≤ 3000, odd n, complete search; `data/z52_bank/pencil_square_k_zeros_le3000.txt`): the residue classes
  in which *every* n fails are exactly those of Theorem 1(a): k = 9: n ≡ 13 (24); k = 16, 64: n ≡ 1 (8); k = 25:
  n ≡ 21, 29 (40); k = 36, 144: n ≡ 1 (24); k = 49: n ≡ 29, 37, 53 (56); k = 100: n ≡ 1, 9 (40). Outside them only
  sporadic zeros (e.g. k = 16: 117; k = 25: 33, 57, 133, 417).
* Local invariants (`scripts/z52_bank_bm_check.py`): on 16 000 random rational points of S_{n,k} (k ∈ {1, 4}, 20 values of n)
  the product formula holds on every point; at every place ℓ where the point is ℓ-integral, (−q, −d)_ℓ = +1 in all
  86 217 odd-place tests and in all 2-adic tests with the theorem's congruence (k = 4, n ≡ 1 (8): 2878; k = 1, n ≡ 5 (8):
  2927), while the other residue class gives −1 in about 20 % of 2-adic tests.

**External novelty check (research subagent + own reading, accessed 2026-10-30; excerpts `sources/z52/bank_lit_*.txt`).**
* Bright–Loughran, *Brauer–Manin obstruction for Erdős–Straus surfaces*, arXiv:1908.02526v2 (12 May 2020), Bull. LMS 52
  (2020) 746–761, DOI 10.1112/blms.12359 (PDF read): Thm 1.1 "there is no Brauer–Manin obstruction to the existence of
  natural number solutions"; Thm 1.2: for odd n and u ∈ ℕ³ a solution, ∏_{p|n}(−u₁/u₃, −u₂/u₃)_p = −1; Thm 1.6:
  Br U_n/Br ℚ ≅ ℤ/2 generated by (−u₁/u₃, −u₂/u₃) (transcendental); Thm 1.8: (U_n(ℝ)⁺ × ∏_p U_n(ℤ_p))^Br ≠ ∅ but is not
  everything. Only k = 0; Remark 1.10 treats m/n, not a constant-term deformation.
* Citers of BL (Semantic Scholar API, 5 records): Mitankin–Uhlemann arXiv:2411.02629v3 (semi-integral points on Markoff
  orbifold pairs), González-Avilés arXiv:2209.06653 (pinched varieties), X. Xu arXiv:2609.29250v1 and Cao–Xu
  arXiv:2610.32302v1 (ES polynomial families, mod 24 primes), plus one unparsable record. Abstracts read: none treats
  k ≠ 0 fibres or positivity-constrained BM on the ES cubic. Full texts NOT ACCESSED.
* Markoff-type cubics x² + y² + z² − xyz = k: Ghosh–Sarnak arXiv:1706.06712v3 (Invent. Math. 229 (2022)), Loughran–Mitankin
  arXiv:1807.10223v3 (IMRN 2021), Colliot-Thélène–Wei–Xu arXiv:1808.01584v4, Dao arXiv:2202.07142v4: integral Hasse
  failures and BM obstructions for a *different* cubic family, no positivity constraint. Colliot-Thélène–Wittenberg
  arXiv:0911.3539v3 (sums of cubes) and Colliot-Thélène–Xu arXiv:0712.1957: different families.
* Verdict: no source found treating 4xyz − nσ₂ = k with k ≠ 0, or the positive-integral obstruction from (−q, −d).
  This is a search result, not a proof of novelty. Assessment: the mechanism is the standard one (Hilbert reciprocity
  with the archimedean sign, as in Yamamoto/BL for k = 0), so the novelty, if any, is the regime (k = m², positive
  density, locally soluble), not the method.

**Why nothing transfers to k = 0 (PROVED except where labelled).**
1. At k = 0 the fibre is singular (at the origin) and (I2) degenerates to dd′ = (ny)². The step "ℓ | d ⇒ −q is a square
   mod ℓ" used the term kq; at k = 0 it is gone, so primes dividing d carry arbitrary invariants. Data (CERTIFIED,
   `scripts/z52_bank_k0_places.py`, all positive ES solutions of all primes 5 ≤ p < 400, all 6 labellings): the
   compensating place where (−q, −d)_ℓ = −1 is always ℓ = 2 or a prime ℓ | d (4 386 times an odd ℓ ≠ p dividing d, 3 117
   times ℓ = p, 7 233 times ℓ = 2), never a prime ℓ ∤ 2d; BL's class always compensates at ℓ = p (13 302 of 13 302).
2. Limit as k → 0 (PROVED). 𝒜 lives on the base-changed pencil k = m² (the residue along {d = 0} is k mod squares, so it
   does not live on the k-pencil itself). Over the m-line, the residue computation goes through at m = 0 on the smooth
   locus: on U_n ∖ {0}, {q = 0} is the line y = n/4, x + z = 0 with −d = (n/2)², and {d = 0} is the line y = z = 0, along
   which v(d) = 2 (d = −y²(n/x)/(1 − cy), c = (4x − n)/(nx)). So 𝒜|_{U_n∖{0}} ∈ Br(U_n ∖ {0}).
3. That limit class does not come from Br U_n (CERTIFIED by explicit points, given BL Thm 1.6). On U_5, at the place 3 the
   symbol of 𝒜 differs from that of BL's generator at P = (30/29, −12, −12) and agrees at P′ = (120/121, −12, −8);
   since Br U_5/Br ℚ = ⟨BL⟩, any class of Br U_5 differs from 0 or from BL by a constant algebra, whose local
   evaluation is constant, and 𝒜's real evaluation is non-constant. So the limit is ramified at the singular point
   (along an exceptional curve of a resolution) and gives no obstruction to anything on U_n.
4. The k-scaling (x, y, z, n, k) ↦ (λx, λy, λz, λn, λ³k) moves away from k = 0; at fixed y, gcd(K_y(±4), K_y(0)) | 4
   (board). No transport. Assessment: the theorem is a calibration of (J)97's "shape of a failure" — a sibling where
   reciprocity kills a positive-density set of n — not progress on 4/p.

### 1(b) GT1: every non-square n ≡ 1 (4) has a genus-free level

TODO

### 1(c) Three-coset Kneser bound 1 ≤ Ω_out ≤ d − 2

TODO

### 1(d) Coprime-category corrections (SQ, ES ⇒ ES₅)

TODO

### 1(e) argon-3: I3_𝒞 and Prop 3.2(b)

TODO

### 1(f) argon-6.1: median-coordinate corollary of H4_NOT_POLYLOG

TODO

## Part 2 — cheap tests

### T1 I3_𝒞 census on 4·10⁷ < p ≤ 10⁸

TODO

### T2 S_{n,−4} census, n ≤ 10⁵

TODO

### T3 ES_Q1 over ℤ[i], Gaussian primes 10⁴ < N ≤ 10⁶

TODO

### T4 Shared invariants of T2/T3 failures

TODO

## Review log

TODO
