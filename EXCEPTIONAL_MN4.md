# EXCEPTIONAL_MN4 — the m/p density transition under Selberg's eigenvalue conjecture (task O117)

Status labels as in DISCOVERIES.md. References: MN2 = `EXCEPTIONAL_MN2.md`, MN3 = `EXCEPTIONAL_MN3.md`,
TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` ((D)32; Thm 8.1 = ET's (OPEN-I) under (SEL)), ET = Elsholtz–Tao
arXiv:1107.1010v6. `L = log N`. `g(x) := x/φ(x)`.

## 0. Plan (work in progress)

Target. CONDITIONAL on (SEL) (all levels, even nebentypus — the TTL §5 hypothesis, now needed for levels
that also involve m):
* Thm I_m: `Σ_{N/2<p≤N} f_{I,m}(p) ≪ N(L² + L log² m)/m + N m^{−0.35}/L` uniformly for `4 ≤ m ≤ L^5`;
* Thm L'': `ρ_rep(m,N) ≪ (L³ + L² log² m)/m + m^{−0.35}` uniformly in m (for `m > L^5` this already follows
  unconditionally from MN3 Thm L', see Lemma 0.1);
* Thm S (sharp order): with MN2 Thm U, the transition for m/p is at `log N ≍ m^{1/3}`.

**Why m ≤ L^5 suffices (Lemma 0.1, PROVED, elementary from MN3 Thm L').** If `m > L^5` then
`(L³ + L² log² m) log L/m ≪ m^{−0.35}`, so MN3 Thm L' already reads `ρ_rep ≪ m^{−0.35}`.
*Proof.* `L ≤ m^{1/5}`, so `L³ log L/m ≤ m^{3/5}·log m/m = m^{−2/5} log m ≪ m^{−0.35}` and
`L² log² m log L/m ≤ m^{−3/5} log³ m ≪ m^{−0.35}`. (MN3 Thm L' needs `log m ≤ L/10`, `L ≤ m^{1/2}`; for
`log m > L/10` MN2 Lemma 3.5 is used unchanged, see §9.) ∎

Consequence: in the conditional argument every factor `m^{O(1)}` in a *remainder* term is `L^{O(1)}`, and
TTL's proof already tolerates `L^C` losses in remainders (layers `k ≤ C₁ log L` go to Brun–Titchmarsh).
The real work is (i) the m-scaled main terms must carry exactly `1/m`, with no `m/φ(m)` loss (the sieve
cannot sieve by `ℓ | m`, which inflates the sieve product by `m/φ(m)`; it must be paid by the coprimality
gain `φ(m)/m` of the masses, MN3 Prop 2.3), and (ii) the spectral input must be checked for the new
level/discriminant `(md, −4md)`.

## 1. Set-up for general m (PROVED; ET Prop 2.2 with 4 → m)

Let `m ≥ 4`, n ≥ 2. A Type I m-solution of n is `m/n = 1/x + 1/y + 1/z` with `n | x`, `(n, yz) = 1`;
`f_{I,m}(n)` is their number. ET Prop 2.2 and its proof (ET p. 12) go through verbatim with 4 replaced
by m: writing `x = ndx'`, `y = dy'`, `z = dz'` with `x', y', z'` coprime, `m d x'y'z' = y'z' + n x'y' + n x'z'`,
hence `x' = ab`, `y' = ac`, `z' = bc`, `c | a+b`, and with `e := (a+b)/c`, `f := macd − n = (na+c)/b`:

  `mabd = ne+1`, `ce = a+b`, `macd = n+f`, `ef = ma²d+1`, `bf = na+c`   (1.1)

(direct check: `mabd = mad(ce−a) = (n+f)e − (ef−1) = ne+1`; `bf = c·ef − af = c(ma²d+1) − af = na + c`).
The map (x,y,z) ↦ (a,b,c,d,e,f) is injective (ET Prop 2.2, uniqueness, normalised by gcd(a,b,c) = 1), and
(a,c,d) determine the rest given n. The swap y ↔ z is a ↔ b. If `a ≤ b` then `c ≤ ce = a+b ≤ 2b`, so
`f = (na+c)/b ≤ n + 2 ≤ 2n`. Hence, with

  `w_{c,m}(n) := #{(a,d,f) ∈ ℕ³ : f | ma²d+1, n = macd − f, 0 < f ≤ 2n}`,

**Lemma 1.1.** `f_{I,m}(n) ≤ 2 Σ_{c≥1} w_{c,m}(n)` (n ≥ 2), and `n` has a Type I m-solution only if some
`w_{c,m}(n) ≥ 1`. ∎

Conversely every w_{c,m}-tuple gives, with `e := (ma²d+1)/f`, `b := ce − a`, the identities (1.1)
(the check above runs backwards), so `b = (na+c)/f ≥ a/2`; this is TTL §8.0 with 4 → m.
**Coprimality facts** (used throughout): `(f, m) = (e, m) = 1` (as `ef ≡ 1 mod m`), hence
`(n, m) = 1` (`n ≡ −f mod m`); for `ℓ | d`, `ℓ ∤ n` (`n ≡ −f`, `f | ma²d+1 ≡ 1 mod ℓ`). So **no sieving prime
may divide md**, and the m-loss of the sieve product must be paid by the masses (§3).

**Exponents.** For n ≍ N write `a = N^α`, `b = N^β`, `c = N^γ`. Then `acd ≍ N/m`, `e ≍ N^{β−γ}`
(`e = (a+b)/c`, m-free), `f ≍ N^{1+α−β}` (`bf = na + c`, m-free), `d ≍ N^{1−α−γ}/m`. Since
`m ≤ L^5` in the conditional part (Lemma 0.1), m shifts only the exponent of d, by `≤ 5 log L/L`.
