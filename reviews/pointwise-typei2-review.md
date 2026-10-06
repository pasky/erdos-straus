# Review R69 of POINTWISE_TYPEI2.md (task O69, branch side-agent/typei-sterile)

Reviewer: hostile side agent R69 (branch side-agent/review-typei2). Reviewed
author commit `5c66f67`. Status: in progress.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm A (i) | SOUND-AFTER-REPAIRS (D1: the "every p>2X_r" form is overstated; limsup statement fine) |
| Thm A (ii), (iii) | SOUND (re-derived Steps 1–5 line by line, incl. the `v_q(4X!)` perturbation fix) |

## Re-derivation notes

### Theorem A

Definitions checked against notes (36.1) (`𝓑_p`: `k≤⌊2p/3⌋`, `c≤⌊(2p+k)/4k⌋`,
`(p,ck)=1`), POINTWISE_TYPEI §0 (`M_{c,k}`, `ck_min`, hard = `p≡1 (24)`).

* (i) `p>2X`, `ck≤X` ⇒ `(c,k)∈𝓑_p`: `4ck≤4X<2p≤2p+k` ✓, `k≤X<p/2≤2p/3` ✓,
  `p∤ck` as `p>X≥c,k` ✓. See D1 for the membership `p∈⋃Cl` itself.
* Step 1: `Cl(κ)` is clopen (defined mod `4ckF`); `Σ_r` compact ✓.
* Step 2: root uniqueness ✓ (`−4V=x_q²` fixes V); q=2 or `q|V` gives unit
  `N_V(x_q)` ✓. Perturbation: `N_V(x+q^T)=q^T(2x+q^T)`, q odd, x unit ⇒
  `v_q=T` exactly ✓; other `V'` keep valuation since `T>v_q(N_{V'}(x))` ✓.
  `𝒞⊂Σ_r` needs `B≥r`, `E_2≥3`, `E_3≥1` ✓ (but see D1 about units at q>B).
* Step 3: the repair is correct and needed: `x*≡y (mod 4ck)` at a perturbed q
  needs `T>v_q(4ck)`, and `ck≤X` ⇒ `4ck | 4·X!` ⇒ `v_q(4ck)≤v_q(4X!)<T` ✓.
  Valuation comparison in all three cases ✓; `(d,4ck)=1` from `d≡−y` ✓.
* Step 4: integrality (`E_q>n_{c,k,q}` ⇒ `f|Q`; `f | a²+4ck²` since
  `a∈𝒞`) ✓; values at q≤B are q-units: `N(Qt+a)≡N(a) (mod q^{E_q})` and
  `v_q(N(a))=n<E_q` ✓; q>B: degree `1+2m'<q` where m' = #distinct V ≤ m ✓,
  leading coefficient `Q·∏Q²/f_V` prime to q ✓. Distinctness: same V ⇒ same
  polynomial; different V ⇒ different leading coeff or constant ✓.
* Step 5: `N=f·R`, R prime > B ≥ X, so R coprime to f and to 4ck; also
  `R≠p` since `p∤4ck²`. Target divisors are `d`, `dR` ✓. The cofactor
  computation `dR≡−p ⟺ e≡−p (mod 4ck)` (using `N≡p² (mod 4ck)`) ✓.
* (iii): `X_r` finite ⇒ apply (ii) with `X=X_r−1` ⇒ limsup ≥ X_r ✓.
  Sterile point from `X_r=∞`: nested nonempty closed sets
  `Σ_r∖⋃_{K_X}Cl` in compact `Σ_r`, finite intersection property ✓ (the
  one-line proof "Cl open, Σ_r compact" is terse but correct).

## Defects

**D1 (MINOR) — Thm A(i), §0 definition of Σ_r.** `Σ_r⊂Ẑ^×` is defined as a
set of *unit* points, but a prime p is not a unit in `ℤ_p`, so "p∈Σ_r" (§0,
Step 5) is literally false. Harmless for (ii) (only q≤B matter), but it
matters for (i): a finite covering of `Σ_r` (units) is a covering mod
`M=lcm(4ckF)`; a prime p with `p|M` (i.e. `p|F` for some F in the covering)
reduces to a non-unit residue and is not guaranteed to be covered — and
indeed `p∉Cl(c,k,F)` whenever `p|F` (would need `p|4ck²`). So "for every
hard p with `n_p=r` and `p>2X_r`" is not proved; it holds for
`p>max(2X_r, max F over the covering)`. *Repair:* state (i) with that
threshold (or "for all but finitely many p"); `C*(r)≤X_r` (a limsup) is
unaffected. Also say "p∈Σ_r" means `p mod M ∈ Σ_r mod M` for the relevant
moduli / define membership via the components at q≤r.
