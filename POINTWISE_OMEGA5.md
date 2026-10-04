# HC(a,B) and the inverse-square problem (task O13)

Labels follow the house rules. ES is not solved here or anywhere.
Notation as in `POINTWISE_OMEGA4.md` (O4) §4.2 and §7: a vertex set O
at free primes `ℓ_1,…,ℓ_{j+1}` (all `>y`), `q:=∏ℓ_i` (squarefree, odd,
`q>y²`), CRT class `c mod q`, `κ:=−c` (a unit mod q). Atoms are written
`(s,a,b)` with **s squarefree** (O3 Lemma 2.1: this is a bijection onto
atoms), `M=4sab−1`, `q|M`, `a≡κb (q)`, `M=q·m·n′` with m the Π-part and
n′ the rest of the rough part; `P(e∖O)=1/φ(n′)≤2/n′` (n′ has `≤k`
prime factors, all `>y`), `n′≥y`. Survival: `m|4sa²+1`.

## 0. Summary (filled in as the work proceeds)

* §1 (PROVED). The obstruction of O4 Prop 7.3/§7.5 — the count
  `#{t≤t_0 : w·t̄² mod q ≤ Y}` beyond the Weil range — is **not** what
  HC needs. HC sums over *atoms*, and atoms have squarefree s. Then
  `(s,t) ↦ st²` is injective, so the relevant count is
  `#{(s,t): s squarefree, s≤Y, t≤t_0, st²≡w (q)} ≤ Yt_0²/q+1`,
  pointwise in w, with no divisor loss and no Kloosterman input.

## 1. The squarefree lifting lemma (PROVED)

**Lemma 1.1.** Let `q≥1`, `w∈ℤ`, `X≥1`. Then

```
#{(s,t)∈ℕ² : s squarefree, st²≤X, st²≡w (mod q)} ≤ X/q + 1.
```

*Proof.* Every positive integer n has exactly one factorisation `n=st²`
with s squarefree. So the pairs inject into
`{n≤X : n≡w (q)}`, which has at most `X/q+1` elements. ∎

**Corollary 1.2 (O4's core count, corrected).** In O4 Prop 7.3 a ray
`(a,b)=t(u,v)` (`gcd(u,v)=1`, `h=uv`) carries the atoms `(s,tu,tv)` with
`4hst²≡1 (q)`. Only squarefree s give atoms (other s give the same
`(M,D)` as an atom with smaller s and larger t, Lemma O3 2.1), so the
count O4 needs is

```
N^sf(q,w;t_0,Y) := #{t≤t_0, s≤Y squarefree : st²≡w (q)} ≤ Yt_0²/q + 1 ≤ Y/(4h) + 1
```

for `t_0≤(q/(4h))^{1/2}`, `w=(4h)^{−1}`. O4's target was `≪𝓛^B·Y·h^{−a}`;
this gives it with `a=1` whenever `Y≥h`, and with the absolute bound 2
when `Y<h`.

*Remark (why O4 met a Weil-range problem).* O4 counted every t with the
least residue `s_t:=w t̄² mod q ≤ Y`, squarefree or not. For non-squarefree
`s_t` the triple `(s_t,tu,tv)` is the *same atom* as some `(s′,t′u,t′v)`
with `s_t t²=s′t′²`, so O4's count over-counts each atom by up to
`#{t: t²|n}`, which can be `T^{c/log𝓛}`. The over-counted problem is
genuinely beyond Weil (and is what the literature in §5 addresses);
the atom count is elementary.
