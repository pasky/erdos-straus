# EXCEPTIONAL_KARY2 — the 3/4 cap without the B-hypothesis, for ℛ(M), (a,D) and Case-A classes (task O14)

Status: **checkpoint 1 (draft, not yet reviewed).** Labels follow
`DISCOVERIES.md`. Notation follows `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_TWIN.md` (ETw), `EXCEPTIONAL_TWIN4.md` (TW4) and
`EXCEPTIONAL_THETA.md` (ET).

## 0. Summary

(filled in at the end)

## 1. Where EK Theorem 4.5 uses B, and where it does not

EK Thm 4.5 is assembled from EK Thm 4.1 (abstract sequential limit with
random costs), the base (ETw Lemma 1.3), singleton steps below `e^{s₁}`
(ETw Prop 4.1), sequential blocks `(e^s, e^{2s}]` with EK Thm 2.5 as the
step inequality, one linear block `(e^{λ/2}, e^λ]` (ETw Cor 4.3), and the
leak (EK Lemma 4.3). The hypothesis `M ≤ P(M)^{1+B}` enters at exactly
three places:

* **(B1) block first moment** (EK Lemma 4.2′, Step 3): the partial
  summation runs over `M ≤ e^{2(1+B)s}`;
* **(B2) singleton first moment** (ETw Prop 4.1): the same over
  `M ≤ e^{(1+B)s₁}`;
* **(B3) second moment / leak** (ETw Lemmas 2.4, 4.0, used in EK Lemma
  4.2(3) and 4.3): the pointwise bound `τ(A_q²) ≤ ℓ^{o(1)}`, valid because
  the cofactor q of the top prime power is `≤ ℓ^B`; and the constants
  `W₀(B)`, `C(B)`.

Everything else is B-free:
* EK Thm 2.5 is arithmetic-free and has no arity bound;
* EK Thm 4.1, ETw Thm 2.3′, ETw Cor 4.3 are B-free;
* the base: `Q₀` may be astronomically large; only `log(Q₀/|R|) = O(W)`
  enters (ETw Lemma 1.3(2));
* the leak mechanism (Lemma 2.1′ of ETw: every class is decided at its
  top prime) is B-free.

**The number of large primes per modulus never enters.** The level
gives d-locality (`d = ⌊λ/s⌋` block primes per term of ν), and EK Thm 2.5
accepts patterns of any arity. The arithmetic inputs are first moments
(sums over *all* classes with top prime in a range) and the second moment
of `p_ℓ` (a sum over cofactors). Neither sees `ω(M)`. This is the
difference from the Λ² route of TW4, where `ω_L(M)` controls the
noise-stability losses (`2^r`, `(log L)^r`).

So, to drop B, it suffices to replace (B1)–(B3) by bounds over *all*
classes with `P(G) ≤ y`, and over all cofactors of `ℓ^v`. That is §§3–4.
To add (a,D)- and Case-A classes, the base must also avoid their
W-smooth classes; that is §2.

## 2. The three class types and the square base

**Definition 2.0 (forced-class families).** A *class* is `n ≡ b (mod G)`.
The three types, with the multiplicity bounds used below:

* **ℛ(M)** (notes Lemma 18.1): `M ≡ 3 (mod 4)`, `A = A_M = (M+1)/4`,
  classes `−4D (mod M)`, `D | A²`. At most `τ(A²)` classes per M.
* **(a,D)** (ET Lemma 3.2): `a, D ≥ 1`, `g = g(D) = Π p^{⌈v_p(D)/2⌉}`,
  class `−(4D+a) (mod G)`, `G = 4a·g`. Since `#{D : g(D) = g} ≤ 2^{ω(g)}`,
  a given pair `(a,g)` carries at most `2^{ω(g)}` classes, and a given
  modulus G at most `μ_{aD}(G) := Σ_{ag = G/4} 2^{ω(g)} ≤ τ(G)²` classes.
* **Case A** (ET §3, "Case A"): `d = r h²` with r squarefree, `g(d) = rh`,
  `m | 4d+1`, class `−m^{−1} (mod G)`, `G = 4rh`. At most `τ(4rh²+1)`
  classes per pair `(r,h)`, and
  `μ_A(G) := Σ_{4rh = G} τ(4rh²+1)` per modulus.

Every class of each type is forced for every `n ≥ 1` (notes Lemmas 16.1,
18.1; ET Lemma 3.2; ET §3 Case A). A *family* 𝔊 is any finite set of
classes of these types, mixed arbitrarily, with **no condition on the
moduli** (no B, no dominant prime, any number of primes at any scale).

**Lemma 2.1 (no squares in ℛ(M)- and (a,D)-classes; PROVED).**
1. No residue of an ℛ(M)-class is a square mod M.
2. No (a,D)-class contains a perfect square `x² ≥ 1`. Hence no residue of
   an (a,D)-class is a square mod G.

*Proof.* 1. Let `c ≡ −4D (mod M)`. By ETw Lemma 1.1, `gcd(D,M) = 1` and
`(−4D|M) = −1`. If `c ≡ x² (mod M)`, then `gcd(x,M) = 1` and the Jacobi
symbol would be `(x²|M) = 1`.
2. Let `n = x² ≥ 1` lie in the class. By ET Lemma 3.2, with
`n + 4D + a = 4agj` (`j ≥ 1` as `n ≥ 1`), `M = (n+4D)/a = 4gj − 1` is
`≡ 3 (mod 4)`, `D | A_M²` and `n ≡ −4D (mod M)`. By part 1, n is not a
square mod M; but n is a perfect square. Contradiction. If a residue c of
the class were a square mod G, say `c ≡ x² (mod G)` with `1 ≤ x ≤ G`, then
the perfect square `x² ≥ 1` would lie in the class. ∎

**Lemma 2.2 (no squares in Case-A classes; PROVED).** Let `d = rh²`,
r squarefree, `m | 4d+1`, `G = 4rh`. Then `−m^{−1} (mod G)` is not a
square mod G.

*Proof.* `gcd(m, 2rh) = 1` since `m | 4rh²+1`, so `m^{−1}` exists mod G.
Suppose `−m^{−1} ≡ y² (mod G)`. Then `y²m ≡ −1 (mod 4rh)`, so
`gcd(y, G) = 1`.
* *Mod 4:* y is odd, `y² ≡ 1 (mod 8)`, so `m ≡ −1 (mod 4)`. In particular
  `m ≥ 3` and `(−1|m) = −1`. If r is even, `8 | G` and `m ≡ −1 (mod 8)`,
  so `(2|m) = 1`.
* *Mod p, p | r odd:* `y²m ≡ −1 (mod p)` gives `−m ≡ (y^{−1})² (mod p)`, so the Legendre symbol
  `(−m|p) = 1`. Let `r_o` be the odd part of r (squarefree). Then the
  Jacobi symbol `(−m|r_o) = 1`.
* *Mod m:* `4rh² ≡ −1 (mod m)` gives `−r ≡ ((2h)^{−1})² (mod m)`, with
  `gcd(2h, m) = 1`. So the Jacobi symbol `(−r|m) = 1`.

Now compute `(−r|m)` otherwise. `(−r|m) = (−1|m)(2|m)^{[r even]}(r_o|m)
= −(r_o|m)`. By reciprocity for coprime odd positive `r_o, m`, with
`(m−1)/2` odd, `(r_o|m) = (m|r_o)(−1)^{(r_o−1)/2}`, and
`(m|r_o) = (−1|r_o)(−m|r_o) = (−1)^{(r_o−1)/2}`. So `(r_o|m) = 1` and
`(−r|m) = −1`, a contradiction. (`r_o = 1` is included: both symbols are
then 1.) ∎

**Lemma 2.3 (square base; PROVED).** Fix `W ≥ 3`. Let `Q₀` be a common
multiple of `8·P_W` and of the W-smooth parts of all moduli of 𝔊 (`P_W`
the product of the primes ≤ W). Put

    R_W^□ = { c mod Q₀ : c mod p^e is a unit square for every p^e ∥ Q₀ }.

1. (R1) Every `c ∈ R_W^□` avoids every class of 𝔊 whose modulus is
   W-smooth.
2. `log(Q₀/|R_W^□|) = 3 log 2 + Σ_{3≤p≤W} log(2p/(p−1)) ≤ 2W`.
3. (R2) Under the uniform law on `R_W^□`, residues at distinct primes are
   independent, and `P(c ≡ a (mod p^e)) ≤ γ(p)/p^e` for `p^e | Q₀`, with
   `γ(p) = 2p/(p−1)` for odd p and `γ(2) = 8`.

*Proof.* 1. Let the class be `b (mod G)`, G W-smooth, so every `p^e ∥ G`
divides `Q₀`. If `c ≡ b (mod G)` and c is a unit square mod every
`p^e ∥ Q₀`, then by CRT `b ≡ c` is a square mod G, contradicting Lemma 2.1
or 2.2. 2. By CRT `R_W^□` is a product. Unit squares mod `p^e` (p odd)
are a fraction `(p−1)/(2p)` of the residues; mod `2^e`, `e ≥ 3`, a
fraction `1/8`. And `Σ_{3≤p≤W}log(2p/(p−1)) ≤ π(W)log 3 + O(1)`.
3. As ETw Lemma 1.3(3): a single residue `a mod p^e` has probability at
most `1/(#unit squares mod p^e) = γ(p)/p^e`. ∎

ETw Remark 1.4 observed this numerically for (a,D) and Case-A classes
(no square mod G in 12,000 resp. 16,406 classes) and said no proof was
written. Lemmas 2.1(2) and 2.2 are that proof. `scripts/kary2_square_check.py`
re-checks both lemmas by brute force (§7).

From here on `Γ(m) = Π_{p | m} γ'(p)`, with `γ'(p) = γ(p)` for `p ≤ W`
and `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` for `ℓ > W`. So `Γ(m) ≤ 8·3^{ω(m)}`,
Γ is submultiplicative, and by the chain rule (ETw Lemma 2.2, with Lemma
2.3(3) at the base) `Q'(n ≡ b (mod m)) ≤ Γ(m)/m` for every m and b.
