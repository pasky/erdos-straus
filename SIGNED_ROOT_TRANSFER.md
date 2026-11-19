# Two replacements from Q: an attained minimum and a failed successor

**CERTIFIED minimum at `p=9565921`, `Q=(p+11)/12=797161`.** Keep `12x`, replace the other two scaled donor slots (the convention of `SHARED_SCALED_SLOT.md`, commit `b638f1884`). The least possible shared donor value is **`x=199291`**, not merely the least in a search. Every positive donor slot exceeds `Q/4`; here the lower endpoint `⌊Q/4⌋+1` works:

```
4/Q donor: (199291, 53119620396, 17157637387908)
4/p target: (2391492, 741550195920, 1416521581680)
```

These triples satisfy their original integer equations and have exactly one slot in common after scaling by 12. Both 11 and 23 are eligible and both denominator windows miss at both shifts. No ES solver or scan of sorted triples is needed for minimality.

### Choose a divisor which is the root (PROVED)

Write `Q=4x−3`, `p=48x−47`. If `x=ab`, `gcd(a,b)=1`, `a≡−1 mod 3`, `47∤a`, and `b≡−a mod 47`, the *same factorization* supplies the two triples. At the donor shift 3 take `(A,B,D)=(1,a,b)`; at the target shift 47 take `(a,b,12)`. In each row `K=ABD`, `E=(A+B)/c`, and the triple is `(K,nADE,nBDE)`. In particular `a²≡−x≡−p mod 47`: choosing a divisor of `x` that is a root makes its complement the opposite root automatically. At the seed `a=17·19=323≡−6 mod 47`, `b=617≡6`, and `a≡2 mod 3`. The dual slot works too: writing `Y=47x−46`, `(47p+1)/4=12Y` has divisor `563≡−1 mod 47`. No new congruence is deduced from the earlier misses here.

**A prime family; scope.** Fix `a=323`, `b=617+Tj`, `T=840·11·23·47·563·599·323`, `j≥0`. Both certificates persist, including the dual hit. There are infinitely many **prime targets** by Dirichlet (`p=9565921+48·323·Tj` is primitive); this alone does not preserve primality of the donor or earlier misses. **Conditional on Dickson**, infinitely often the five forms `p,Q,L=2x−1,(11Q−10)/599,23L−22` are simultaneously prime. This *does* preserve `h=1` and both prior double misses: the seed residues give `Q≡2 (11)`, the two factors of `11Q−10` are `5,9 (11)`, `L≡14 (23)` and `23L−22≡1 (23)`. For admissibility the five seed constants `9565921,797161,398581,14639,9167341` are prime and coprime to **every** slope. At any prime dividing a slope but not all, the constant forms are units; each other form excludes at most one residue. All primes ≤5 divide all slopes. The five roots in the `x` coordinate are distinct. Thus this is a coordinated construction under the exact old failures, not an unconditional forcing theorem on that branch.

### What the two misses force at 47 (PROVED)

Suppose `p≡1 (840)`, `h=1` (`Q` prime), and both windows miss at the eligible shifts 11 and 23. `SIGNED_FACTOR_TRANSFER.md` gives `L=(Q+1)/2=r s` with just one prime occurrence `r≡5 or 14 (23)`, every prime of `s` in class 1. Thus `L` is prime to 6, `x=(L+1)/2` is integral, and `x≡1 mod 3`: residue 0 would put 3 in `Q=4x−3`, residue 2 puts 3 in `L`. Also `x≡1 mod 5` by `p≡1 mod 5`. Put `R=11Q−10`, `M=23L−22`. The new windows have base denominators `12x` and `12Y` with

```
Y=47x−46;       gcd(x,Y)=gcd(x,2);       gcd(xY, Q L R M)=1.
```

Indeed `23∤x` since `L≡5 or 14 (23)`. Against `x`, use `Q=4x−3`, `L=2x−1`, `R=44x−43`, `M=46x−45`. Even 43 cannot be shared: `43≡10 (11)` is excluded from `R` by dual failure at 11. Against `Y`, use

```
4Y−47Q=−43,   2Y−47L=−45,   47R−44Y=3,   47M−46Y=1.
```

Here `Q>43`, `L` is prime to 15 and `3∤Y`. Thus neither new cofactor can inherit a prime from any of the four old cofactors. Nor do odd primes of `Q−1=4(x−1)` help: `x,Y≡1 mod (x−1)`. The new factor in the successful transfer comes from **`L+1`**, not from `L` itself. In fact the donor at this minimum works **iff** `x` has a prime factor `2 mod 3`: its unrestricted signed products come from `Qx`, with `Q≡1 mod 3` prime. Thus a negative factor of `L+1` other than the reserved 2 is genuinely necessary here (in `x=(L+1)/2`, a further 2 also counts).

**Two obstructions to using the prime in `Q+1`.** First, `p≡−23 mod r` and `(r/23)=−1`; for `r≡1 mod 4`, reciprocity gives `(−p/r)=(23/r)=−1`. No root-eligible shift can even contain `r`, irrespective of its size. This applies to `398581` at the seed. Likewise a prime `q≡3 mod 4` dividing `Q−1` cannot enter a root-eligible shift, since `p≡1 mod q`.

Second, if `4r≥138s+23`, **no normalized Type II denominator `K=ABD` retains `r` at any shift**. Here `r≥37`: `5∤L` and 5 is the only smaller prime in the allowed classes. From `r|K`, `c=4K−p>0`, `c≤K+1`, we have `c=23+4rj`, `0≤j<2s`, `K=r(6s+j)`. Row `j=0` already fails. For `j≥1`, `r|D` would give `c≤6s+j+1<c`. Otherwise write `A=ra`, `aBD=6s+j`. Now `c | 4jB−23a`, where `B<8s≤r` and `23a≤138s+23j≤4rj`. Thus `4jB=23a`; substituting into `A+B=cE` gives `a=4jE`, `B=23E`, and coprimality gives `E=1`. This forces `6s=j(92D−1)`, impossible since all divisors of `6s` are `1,2,3,6 mod 23`. In particular this excludes the entire prime-`L` subcase: `L≡1 mod 35` from the hard class, so a prime `L` exceeds 40. This concerns the unscaled Type II slot, not arbitrary slots in Type I.

### An ordinary prime where eligibility still gives nothing

**CERTIFIED counterexample:** `p=6206649121≡1 mod 840`. The three shifts 11, 23, 47 are *all root-eligible* (`p` residues `2,14,13`) and **both** windows fail at all three. As at the seed, `Q=517220761` and `L=258610381` are prime. `R=5689428361` is prime in class 1 mod 11; `M=3209·1853549` has both primes square mod 23. At 47, `x=129305191` is prime of class 13. In `pK=12px`, `p≡x mod 47`; attaining `−1` requires an odd net exponent of `x` modulo the square subgroup, so from the two available occurrences one must use net exponent `±1`. Neither `−13` nor `−1/13` occurs in `{2^i 3^j: |i|≤2, |j|≤1}` mod 47. In the dual slot `Y=55229·110039`, the factors are `4,12 mod 47`, both squares, as are 2 and 3. Even the *donor* at `x` fails: both `Q,x≡1 mod 3` are prime, so their signed products cannot be `−1 mod 3`. This does not rule out all larger shared terms.

**Steering.** At the minimum the two requirements are a donor factor `2 mod 3` and a target signed product `−1 mod 47`; matching a factor with a square root solves both at the seed. At the counterexample the first requirement already fails. Any universal transfer must allow a different donor row there; improving a root selection at the minimum cannot suffice. Falsifier scopes: F1 odd squares cannot meet the eligibility assumptions; F2 concerns numerator 8, not claimed; F3 composite inputs need not obey the prime-slot tests; F4 restricted (★)/gstar zeros say nothing about these shared slots.

Replay: `(ulimit -v 800000; timeout 90 uv run --no-project python scripts/signed_root_transfer.py)`.
