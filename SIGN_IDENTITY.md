# SIGN_IDENTITY — exact identities for the ES sign N₋(n) (task O205, wave Y-b)

Status: in progress (O205). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on CHI_FLIP.md (χ = −ε₂(Q_w)), CONSTRUCTIVE_ES.md (Eichler orders of level 2), MODEL_SPECIFIC.md Thm 3.1,
KUDLA_ES/DIFF_DEEP/LDP_DEEP ((J)13, (J)16–18), GROWING_IDENTITIES (J)10, EXACT_FORMULA (I)5, STRONG_APPROX_ES Thm 9.1.
Scripts `scripts/si_*`.

Notation (as CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, K(w) = tuv − u − v = n odd; A = tu − 1, A* = tv − 1,
AA* = tn + 1; χ(w) = (−A/n); G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]], det n. X_n = all positive words.
N_±(n) = #{w ∈ X_n : χ(w) = ±1}, S(n) = N₊ − N₋. SQ₅ (CONJECTURE): N₋(n) > 0 ⟺ n odd non-square, n ≠ 105.
Fingerprints: N₋(m²) = 0; N₋(105) = 0; N₊(n) = 0 at 38 values n ≡ 3 (4) ≤ 10⁶ (15, 311, 455, 495, …).

## 0. Iteration log
(I1) Setup: enumerator `scripts/si_census.c` with several weightings (§1).
(I2) Barrier targeted: Thm 9.1's "finite Eisenstein combination". Tried: (a) linear relations with 48 classical columns incl.
Kronecker–Hurwitz sums (§3, no relation); (b) *all* holomorphic modular forms — killed by size (d₃-type averages), not by
T1 (Thm 2.2); (c) zero-set equivalence with a weight-3/2 eigenform (Waldspurger route, hook (3)) — killed because the
root-number mechanism vanishes on whole congruence classes (Prop 2.4). (d) Gross–Keating/Kudla (hook (1)): exact
dictionary in which **both** signs are |Diff| = 1 cycles, at the two bad fibres of X₀(2p) (§4).

## 1. Exact reformulations of the sign (PROVED, elementary)

**Lemma 1.1 ((u,v)-form).** For odd n, w ↦ (u, v) is a bijection X_n → {(u, v) ∈ ℤ²_{≥1} : uv | n + u + v}, with
t = (n + u + v)/(uv), A = (n + u)/v, A* = (n + v)/u. If gcd(uv, n) = 1 then **χ(w) = (−uv/n)**; so the sign of a word
depends only on m = uv, and
  N₋(n) = Σ_{m : (−m/n) = −1} c_m(n) (+ words with gcd(uv, n) > 1),  c_m(n) := #{u | m : m | n + u + m/u},
c_m(n) a function of n mod m. Every word has (u − 1)(v − 1) ≤ n + 1, hence **|X_n| ≤ 2 Σ_{u ≤ √(n+1)+1} d(n + u) ≪ n^{1/2+ε}**.
*Proof.* tuv − u − v = n ⟺ uv·t = n + u + v; Av = (tu − 1)v = n + u. With gcd(v, n) = 1, A ≡ u·v⁻¹ (mod n), so
(−A/n) = (−uv/n). For u ≤ v: v | n + u and u ≤ √(n+1) + 1. ∎ CHECKED (`scripts/si_uvform.py 1500`): all 35 184 words of odd
n ≤ 1500 (= census total), 31 968 with gcd(uv, n) = 1, 0 mismatches. (The non-residue −uv already appears in
CONSTRUCTIVE Prop 4.1(c) for primes; the point here is that χ is a function of the product uv.)
*Reading.* SQ₅(n) asks for a product m = uv, −m a non-residue mod n, with u + m/u ≡ −n (mod m) and the size condition
t ≥ 1. Each pair (u, v) is a Mordell-type identity covering the class n ≡ −(u + v) (mod uv) with a sign fixed by
(t, u, v) mod 8 (CHI_FLIP Cor 1.2): B1/B2 shape, nothing new — but the m-grading is what §2 uses.

**Lemma 1.2 (trivial certificates; PROVED).** N₋(n) ≥ 1 if n ≡ 3 (mod 4) (word (1, 2, n + 2), A = 1) or n ≡ 5 (mod 8)
(word (1, 3, (n + 3)/2), A = 2). For a prime p ≡ 1 (mod 4) and a prime q ≡ 3 (mod 4) with p ≡ −1 (mod q), the word
(1, q + 1, (p + 1)/q + 1) has A = q and χ = (q/p) = (p/q) = (−1/q) = −1. Hence (Dirichlet + CRT) **for every modulus M
and every class r mod M with gcd(r, M) = 1, r ≡ 1 (mod 4), there are infinitely many primes p ≡ r (M) with N₋(p) ≥ 1**
(take q ∤ M, q ≡ 3 (4), and p ≡ r (M), p ≡ −1 (q)). (Mordell/CHI_FLIP §3.1 in a Chebotarev-uniform form; also true
for p split completely in any fixed number field K, taking q unramified in K — Chebotarev in K(ζ_q).)
