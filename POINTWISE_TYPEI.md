# Type-I `ck_min` beyond the least non-residue (task O31)

Status: IN PROGRESS (side agent O31, branch `side-agent/typei-ckmin`).

Notation as in POINTWISE_OMEGA §8 and notes §§36, 44, 48, 50, 52. A slice
is `(c,k)∈𝓑_p` (notes (36.1)); `h=4ck`, `N=N_{c,k}(p)=p²+4ck²`,
`s=sf(c)`, `χ_s=(Δ_s/·)`;
`M_{c,k}(p)=#{D>0 : D|N, D≡−p (mod h)}`;
`ck_min(p)=min{ck : (c,k)∈𝓑_p, s∉{1,2,3,6}, M_{c,k}(p)>0}`;
`n_p` = least quadratic non-residue mod p. A slice is **forced** at p if
`χ_s(p)=1` (then `M=0`, notes Thm 48.1) and **unforced** if `χ_s(p)=−1`.
"Hard" means `p≡1 (mod 24)`.

## 1. The dual (divisor) form of slice vanishing

**Lemma 1.1 (dual parametrisation; PROVED).** Let p be an odd prime and
`(c,k)` positive integers with `(p,ck)=1`. Then

```
M_{c,k}(p) = #{ j ≥ 1 : hj > p,  (hj − p) | 4cj² + 1 }.
```

Equivalently, `M_{c,k}(p)>0` iff `p = 4ck·j − D` for some `j≥1` and some
divisor `D` of `4cj²+1` with `D<4ckj`.

*Proof.* Every target divisor D is a positive integer `≡−p (mod h)`, so
`D=hj−p` with a unique integer `j`, and `D>0` forces `hj>p`, `j≥1`. Since
`hj≡p (mod D)`,

```
N = p²+4ck² ≡ h²j²+4ck² = 4ck²(4cj²+1)   (mod D).
```

`(D,2ck)=1` because `D≡−p (mod 4ck)` and `(p,2ck)=1`. Hence
`D|N ⟺ D | 4ck²(4cj²+1) ⟺ D | 4cj²+1`. ∎

So the slice-positivity set
`S_{c,k}={4ckj−D : j≥1, D|4cj²+1, 0<D<4ckj}` is the classical Type-I
parametrisation (`a=j`, notes (50.5)) and `M_{c,k}(p)=0 ⟺ p∉S_{c,k}`
(counting multiplicity). Since `N≡p² (mod h)`, the involution `D↔N/D`
preserves the target class, so `M_{c,k}(p)>0` iff some target divisor
`D≤√N` exists; `√N ≤ p+2ck²/p`, so these D are `≤ p(1+o(1))` for
`ck²=o(p²)`. In sieve language:

* for a fixed divisor value D, `D|N, D≡−p (h)` is a union of `ρ(D)`
  classes of p modulo `hD` (ρ = number of roots of `x²≡−4ck² (D)`);
* vanishing is "p avoids all these classes for all D up to `√N≍p`", a
  congruence sieve whose moduli `hD` run up to `h·p`, i.e. **beyond the size
  of the sifted variable** (see §4).
