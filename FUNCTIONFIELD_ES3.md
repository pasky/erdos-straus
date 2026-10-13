# FUNCTIONFIELD_ES3 — the sterile point x*_c of ES₃(T²): structure of Case B, complete-range searches (O173)

Status: in progress (O173). Builds on FUNCTIONFIELD_ES.md (linear families §6.2, Lemma 6.2) and FUNCTIONFIELD_ES2.md
(§0.1 compactness criterion, §0.2 Case A proof, Case B normal form (****), Conjecture 0.2; R166 repairs).
Scripts `scripts/ff3_*`, data `data/ff3_*`. ES over Z is not touched; this is the F_q[T] model only.

Setting throughout (unless stated): q odd, A = T^k with k ≥ 2, c ∈ F_q^*, and the slice point
x*_c ∈ R̂^*: x*_c ≡ 1 at every prime ℓ ≠ T, x*_c ≡ u := 1 + cT (mod T^∞).
More generally a *slice point* x_u has x ≡ 1 off T and x ≡ u (mod T^∞) for a unit power series u.

## 0. Iteration log

* (I1) Fast exact search (`scripts/ff3_caseB.c`, C, own F_p arithmetic). For each (L', j) the Case B divisor is
  forced to be the least CRT residue ρ (or ρ' for the cofactor), and the gcd-part g' is then forced too
  (g' ≡ −(T^{N+1+γ}L')^{−1} mod ρ, and deg ρ > deg L' is proved in Lemma 1.2). So each (L', j, branch) costs one
  extended gcd and no factoring. Result at x*_c: 0 families for deg L' ≤ 13, j ≤ 14, c = 1, 2 (R166 had ≤ 7, ≤ 8).
* (I2) The same search at random slice points u ≡ 1 + cT (mod T²) (200 points, deg L' ≤ 9, j ≤ 10) finds hits,
  and the hits at large deg L' all have large N and γ close to j. This contradicts the R166/O166 heuristic
  "expected number of covering families diverges over ℓ = deg L' at fixed N". §2 proves why: at fixed N the
  degree of L' is bounded (Lemma 2.1), so per level N there are finitely many families.
* (I3) At u = 1 + cT exactly, Lemma 2.3 bounds N ≤ 4 deg L' − 1. So a search over all j for each deg L' ≤ L0 is a
  *complete* exclusion of all families with deg L' ≤ L0 (any N). Running for L0 = 13.

## 1. Case B at slice points, and why the search is exact

**Lemma 1.1 (families at a slice point; PROVED; restates FUNCTIONFIELD_ES2 §0.2 (F1), (F2) with proofs).** Let
F = (E; t_a, a0; t_b, b0) be a linear family, L = lcm(a0, b0) = T^j L', g = gcd(a0, b0) = T^γ g' (T ∤ L'g'),
N := k + j − 1. F is valid at the slice point x_u iff (i) E ≡ −u (mod T^{N+1}) and E ≡ −1 (mod L'), and (ii)
E | s, lc(s) = lc(E), s ≠ 0. Under (i): gcd(E, T·L) = 1, P ≡ 1 and X ≡ T^{−k} (mod E), and each a0, b0 is a unit
mod E. Hence s ≡ a0 + b0 (both types in {0,1}), ≡ T^{−k}(a0^{−1} + b0^{−1}) (both in {2,3}): **Case A**,
E | a0 + b0; or s ≡ a0 + (T^k b0)^{−1} (mixed): **Case B**, E | 1 + T^k a0 b0 = 1 + T^{N+1+γ}L'g' =: D, and lc(s) = 1
(distinct types), so E is monic and so is E' := D/E.
Conversely every monic E | D satisfying (i), with g' | L', 0 ≤ γ ≤ j, is a valid Case B family
(a0 = T^γ g', b0 = T^j L', types 0 and 2) for all n ≥ n_F.
*Proof.* A·a0, A·b0 | P + E ⟺ T^k L | P + E, and P ≡ u (mod T^{k+j}), P ≡ 1 (mod L') at x_u. Since u(0) ≠ 0,
T ∤ E; E ≡ −1 (mod L') gives gcd(E, L') = 1. x_u ≡ 1 at every prime of E gives P ≡ 1 (mod E), so
T^k X = P + E ≡ 1. A prime dividing a0 and E would divide X, but T^k X ≡ 1 (mod E). The residues of the four
types follow (P ≡ 1, X ≡ T^{−k}), and a0 b0 = Lg. The converse is Lemma 6.2 of FUNCTIONFIELD_ES read backwards. ∎

**Lemma 1.2 (the divisor and g' are forced; PROVED).** Assume moreover u(0) = 1 (true at x*_c). Let ρ, ρ' be the
least residues mod T^{N+1}L' of the classes {≡ −u mod T^{N+1}, ≡ −1 mod L'} and {≡ −u^{−1}, ≡ −1}. In Case B,
E = ρ or E' = ρ'. Moreover deg ρ, deg ρ' > deg L', so g' is the least residue of −(T^{N+1+γ}L')^{−1} modulo
ρ (resp. ρ').
*Proof.* E' ≡ D·E^{−1} ≡ −u^{−1} (mod T^{N+1}) and ≡ −1 (mod L'). deg D = N + 1 + γ + l + deg g' with
l := deg L', γ ≤ j = N + 1 − k ≤ N − 1 and deg g' ≤ l, so deg D ≤ 2(N + 1 + l) − 2 and one of E, E' has degree
< N + 1 + l, hence equals its least residue. ρ + 1 = L'h with h ≢ 0 (as u ≢ 1 mod T^{N+1}… if u ≡ 1 the class
is −1 and ρ = −1 is not monic of positive degree). If h were constant, L'h ≡ 1 − u ≡ 0 (mod T) would force
T | L'. So deg ρ ≥ l + 1; same for ρ'. Finally ρ | D ⟺ T^{N+1+γ}L'g' ≡ −1 (mod ρ), and T, L' are units mod ρ. ∎

So the exact Case B search at x_u is: for each monic L' (T ∤ L'), j, branch, compute ρ, require it monic, compute
v = −(T^{N+1}L')^{−1} mod ρ, and for γ = 0..j test whether t_γ = v·T^{−γ} mod ρ is monic of degree ≤ l and
divides L'. `scripts/ff3_caseB.c` does exactly this. Sanity: at u = 1 + T + 2T² it re-finds the O166 family
E = T² + 2T + 2 (L' = 1, j = 2) and E = T² − T − 1 (j = 1, γ = 1); at random u it reproduces the O166 covered mass
(51/300 random lifts of 1 + T (mod T³) hit with deg L' ≤ 5, j ≤ 5, against the exact union mass 0.185).
