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
