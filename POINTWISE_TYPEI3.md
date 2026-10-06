# Is the sign point `x̂_9` sterile? (task O72)

Status: in progress (side agent O72, branch `side-agent/sign-point-sterility`).
Builds on POINTWISE_TYPEI2.md (Theorem A, (2.2), Lemma 2.4, Lemma 3.1, Computation 3.2, Conjecture 3.4).

Notation. `x̂=x̂_w`: `w` at 2 (`w≡9 (16)`), `−1` at 7, `1` elsewhere. A certificate
at `x̂` is `(c,k,F)`, `v_7(c)` odd, `F | N=1+4ck²`, and `F≡−x̂ (mod 4ck)`, i.e.
(2.2). Write `4ck=2^t n` (`n` odd), `n=7^v m'` (`7∤m'`), `c=2^α7^a c'`,
`k=2^γ7^b k'`, so `t=2+α+γ`, `v=a+b`, `m'=c'k'`, `k_o=7^b k'` (odd part of k).
Note `4ck²=2^{t+γ} n k_o`.

## 1. Small-divisor reduction (PROVED)

**Lemma 1.1.** Let `(c,k,F)` be a certificate at `x̂_w` and `e=N/F`. For
`f∈{F,e}`:
(i) `m' | f+1` and `7^v | f−1`; in particular `n | (f+1)(f−1)`;
(ii) `f≡−w (mod 2^t)` if `f=F`, and `wf≡−1 (mod 2^t)` if `f=e`;
(iii) `2^{t+γ}·n·k_o ≡ −1 (mod f)`.
Conversely, given odd `f≥1`, a role (F or e), integers `t≥2`, `0≤γ≤t−2`, `a` odd,
`b≥0`, and `c',k'` odd, prime to 7, with (i)–(iii) for `m'=c'k'`, `v=a+b`,
then `(c,k,F)` with `c=2^{t−2−γ}7^a c'`, `k=2^γ7^b k'` and `F=f` (resp.
`F=N/f`) is a certificate at `x̂_w`.

*Proof.* `F≡−x̂ (mod 4ck)` means `F≡−1 (m')`, `F≡1 (7^v)`, `F≡−w (2^t)`. Since
`N≡1 (mod 4ck)`, `e≡F^{−1}≡−x̂^{−1}` (mod 4ck), and `x̂^{−1}` has components
`1, −1, w^{−1}`; this gives (i), (ii). (iii) is `f | N` rewritten. Conversely,
(iii) gives `f|N`, so `f` (resp. `N/f`) is coprime to `4ck` (N≡1 mod 4ck) and lies
in the class `−x̂` (resp. `−x̂^{−1}`) mod `4ck` by (i), (ii); the cofactor of
a divisor in class `−x̂^{−1}` is in class `−x̂`. `v_7(c)=a` is odd, so
`7 | sf(c)` and `s∉{1,2,3,6}`. ∎

**Consequence.** For a fixed `f`, there are finitely many certificates having
`f` as one of their two complementary divisors: `t ≤ v_2(f+w)` resp.
`t≤v_2(wf+1)`, `n` divides the explicit number `(f+1)_{odd}·7^{v_7(f−1)}`,
and `k_o | n`. So the certificates at `x̂_w` are graded by
`f_min=min(F,e)≤√N`, with a finite, fully explicit check per value of
`f_min`. Note `f_min` can be tiny while `ck` is huge (`ck=2^{t−2}n` with `n` up
to `≈f²/16`); this is how all near misses in the §5 data of POINTWISE_TYPEI2
look (`f_min` = 15, 71, 239, 407, …, with `ck` up to `4·10⁸`).

**Lemma 1.2 (f-bound ⇒ height bound; PROVED).** If `ck≤X` (and `7|c`), then
`min(F,e)≤√N<2X/√7+1`. Hence: no certificate at `x̂_w` with
`min(F,e)<Y` ⟹ no certificate with `ck≤(Y−1)√7/2≈1.3229(Y−1)`.
*Proof.* `4ck²=4(ck)²/c≤4X²/7`, and one of two complementary divisors is `≤√N`. ∎

**Search criterion (from Lemma 1.1).** Given `f`, put `R=7^{v+b}k'm' mod f`. A
certificate with divisor `f` exists iff for some admissible `(m',k',v,a)` and
`s=t+γ` we have `2^s R≡−1 (mod f)` with `⌈(s+2)/2⌉≤t≤min(s, T_role)`, where
`T_F=v_2(f+w)`, `T_e=v_2(wf+1)`. As `γ≤t−2`, `s≤2T−2≤2log₂(f+|w|)`: only
**small** powers of 2 are relevant (no discrete logarithm needed).

## 2. Computation: the f-graded search (CERTIFIED once run; see Replay)

`scripts/typei3_fsearch.c` (`r w Ylo Yhi`) runs over `f≡1 (7)`, `f≡−w (4)` in
`[Ylo,Yhi)`, factors `(f+1)_odd` by a segmented sieve, and tests Lemma 1.1
for every `m'|(f+1)_odd`, `k'|m'`, `1≤v≤v_7(f−1)`, `a` odd, both roles,
`2≤t≤T_role`, `0≤γ≤t−2`. It is complete for all certificates having a
divisor `f` in range, at any height. Hits are re-verified by the stand-alone
exact checker `scripts/typei3_verify.py`.

*Cross-check (agreement of certificate sets).* `scripts/typei3_cmp.sh r w X` compares,
for all certificates with `ck≤X`, the output of the independent ck-graded
checker `typei2_signcheck.c` with `typei3_fsearch` on `f<2X/√7+2`. At
`X=2·10⁵` the sets coincide exactly for
`(r,w)=(7,1),(7,−7),(7,25),(7,41),(7,17),(7,−15),(11,9),(19,9),(23,1),(7,9)`
(3, 0, 0, 0, 13, 35, 7, 4, 2, 0 certificates).

## 3. Scope of any sterility proof: sterile points are nowhere dense (PROVED)

**Proposition 3.1.** The set `St_7` of sterile points of `Σ_7` is closed and has
empty interior. In particular every clopen neighbourhood of `x̂_9` contains
non-sterile points (covered by certificates with `k=1`, `t=2`, height `7p`).
*Proof.* Closed: `St_7=⋂_X U_X` (proof of Thm A(iii)). Let `x∈Σ_7` and
`U={y: y≡x (mod Q)}`, `Q=2^j7^i∏_{q∈P}q^{e_q}` (P a finite set of odd primes
`≠7`); such U form a neighbourhood basis. Pick a prime `p∉P∪{2,7}` and put
`c=7p`, `k=1`, so `4ck=28p`, `t=2`, `v=1`, `m'=p`, `s=7p∉{1,2,3,6}`. Pick a prime
`F∉P∪{2,7,p}` with `F≡3 (4)`, `F≡−x_7 (7)` and `(−7p/F)=1`. This is a
condition on `F mod 28p`: `(−7/F)=(F/7)=(−x_7/7)=(−1/7)(x_7/7)=1` as `x_7` is a
non-square mod 7, and `(p/F)=(F/p)(−1)^{(p−1)/2}` (F≡3 mod 4) fixes the class
of F mod p as squares or non-squares. So Dirichlet gives such F. Then
`Cl(7p,1,F)={y≡−F (28p), y²≡−28p (F)}` meets U: at 2 the conditions are
`y≡−F≡1 (4)`, compatible with `y≡x_2≡1 (8)`; at 7, `y≡−F≡x_7 (7)`; at p and at F
(outside P) they are free congruences with a solution (`−28p` is a square mod
F); at `q∈P`, `y≡x (q^{e_q})`. By CRT, `U∩Cl≠∅`; points of `Cl` are not
sterile. ∎

*Consequence (scope).* A proof that `x̂_9` is sterile cannot be a congruence
argument modulo a fixed modulus, as in Lemma 2.1 or Lemma 3.1 of POINTWISE_TYPEI2 (those
prove sterility of a whole clopen set of slices or families, never of a point
neighbourhood). It must use that `x̂_q=1` exactly at infinitely many q. Inside the
sign family `{x̂_w}` this means that `w=9` is exact 2-adic data: by Lemma 1.1 the
2-adic depth available to a divisor `f` is `v_2(f+9)` (resp. `v_2(9f+1)`), a
quantity with no uniform bound.
