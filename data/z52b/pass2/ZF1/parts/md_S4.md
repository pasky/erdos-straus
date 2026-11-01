## Z2835 — non-square pencil fibres: the class (−q, −d) also obstructs on the Mordell locus 4k + n³ = □ (interesting)

**What.** Z52_BANKED §1(a) shows that 𝒜 = (−q, −d) lies in Br S_{n,k} (S_{n,k}: 4xyz − n(xy+yz+zx) = k, q = 4y − n,
d = qz − ny) when k = m², and for non-square k is unramified exactly when 4k + n³ is a square. The item asked for the zero
table at non-square k and a comparison with BM predictions.

**Numbers (CERTIFIED, complete searches, `scripts/z52_bank_pencil.c`, odd n).**
* Zeros of S_{n,k}(ℕ): k = 2: 9, 21, 57, 65, 117, 201, 297, 425, 945, 3465, 12597, 25221, 26961 (n < 5·10⁴);
  k = 3: **only n = 13**; k = 5: 21, 57; k = 6: none; k = 7: 9, 33, 45, 57, 129, 417, 1245, 2805, 2925 (none in (10⁴, 5·10⁴)).
  Square controls (n < 10⁴): k = 1: 1262, k = 4: 1250, k = 9: 417 zeros among 4996 odd n. So non-square fibres have only
  sporadic zeros, with no killed residue class.
* The single k = 3 zero is the only odd n ≤ 10⁴ with 4k + n³ a square (13³ + 12 = 47²). At (13, 3) all 133 901
  local symbols (−q, −d)_ℓ at ℓ-integral places of 19 995 random rational points are +1. The controls (17,3), (21,3),
  (13,2), (13,7) have −1 at some places (`data/z52b/pass2/ZF1/Z2835/bm_local_13_3.txt`).

**Theorem 1(b) (PROVED here, elementary; the same Hilbert-reciprocity scheme as Z52_BANKED Thm 1(a)).** Let s be odd,
n ≥ 1 odd, and k = (s² − n³)/4 ≥ 1 (so n ≡ 1 (4)). Assume gcd(n, k) = 1, and that (−n/ℓ) = +1 for every prime ℓ | s with ℓ ∤ k.
Then S_{n,k}(ℕ) = ∅.
*Proof.* Take a positive integral point. Then q, d > 0, so inv_∞ = −1. Finite places:
* ℓ ∤ qd: the symbol is trivial.
* Odd ℓ | q: then ℓ ∤ n (otherwise ℓ | y and ℓ | k), and (I3) gives −d ≡ (n/2)², a unit square.
* Odd ℓ | d, ℓ ∤ q, ℓ | k: (I2) forces ℓ | y, so −q ≡ n, and n is a square mod ℓ because s² ≡ n³.
* Odd ℓ | d, ℓ ∤ qk: −q ≡ n²y²/k. The key identity is dd′ = (ny + 2k/n)² − k(s/n)². It gives (k/ℓ) = 1 if ℓ ∤ s. If ℓ | s,
  then k ≡ −n³/4, so (k/ℓ) = (−n/ℓ) = 1 by hypothesis.
* ℓ = 2: q is odd. If −q ≡ 5 (8), then dd′ is odd by the same identity (for n ≡ 1 (8) k is even and ny + 2k/n is odd; for
  n ≡ 5 (8) k is odd and dd′ ≡ kq (mod 4)), so the symbol is +1.
The product of all local symbols is then −1, which contradicts Hilbert reciprocity. ∎
*Check* (`scripts/z52d_p2_ZF1_Z2835_mordell.py 3001 1000000`, complete search with the general bound x²(4x − 3n) ≤ k).
There are 55 861 Mordell-fibre pairs with n ≤ 3001 and k ≤ 10⁶. Under the hypothesis, 13 682 of 13 682 are empty
(both n ≡ 1 and n ≡ 5 (8)). Without it, 54 % are still empty (24 731 of 45 860 with gcd = 1 and a "bad" prime ℓ | s,
(−n/ℓ) = −1). Bad ℓ = 3 makes points easy: 55 of 2 179 are empty. Adjacent non-Mordell controls (n, k + 1..3) are empty only
2.5 % of the time (298 of 11 986).

**Why it might matter for ES (Assessment).** On the k-pencil, 𝒜 obstructs on two loci: {k = □} (Thm 1(a), positive
density in n for each square k) and the Mordell locus {4k + n³ = □} (Thm 1(b)). For fixed non-square k the second locus is
the finite set of integral points of s² = n³ + 4k (Siegel), so "non-square fibres are BM-free" holds only up to finitely
many n per k. At k = 0 the second locus is exactly {n = □}, i.e. the odd squares of T1. So T1 is the k → 0 limit of the
Mordell-locus obstruction. At k = 0 the proof itself breaks: gcd(n, k) = n, the case ℓ | n fails, and U_n is singular. A
prime p is never on the k = 0 Mordell locus, which matches FRONTIER §7 item 15 (no prime T1).

**Reproduce.** `gcc -O2 -Iscripts -o /tmp/pencilk scripts/z52d_p2_ZF1_Z2835_pencilk.c; uv run --with sympy python
scripts/z52d_p2_ZF1_Z2835_mordell.py 3001 1000000 /tmp/pencilk`, and `uv run --with sympy python
scripts/z52d_p2_ZF1_Z2835_bm13.py`. For the zero tables run `scripts/z52_bank_pencil.c` with `first k 9 9999 2 1`.

**Next step.** Check whether the 54 % residual emptiness on bad-prime Mordell fibres is a BM obstruction to *bounded*
integral points (strong approximation): solutions need a bad prime ℓ | d with y ≡ −2k/n² (mod ℓ). Also compute the full
Br S_{n,k} at sporadic zeros (e.g. k = 2, n = 3465) to see whether any other class exists.

