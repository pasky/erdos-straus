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
