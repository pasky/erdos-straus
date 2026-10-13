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
E = T² + 2T + 2 = T² − T − 1 (L' = 1, both with j = 2, γ = 0 and with j = 1, γ = 1); at random u it reproduces the O166 covered mass
(51/300 random lifts of 1 + T (mod T³) hit with deg L' ≤ 5, j ≤ 5, against the exact O166/R166 union mass 0.198 for deg L' ≤ 5, j ≤ 5; binomial sd 0.023).

## 2. Structure of Case B: finitely many families per level, and the bound N ≤ 4 deg L' − 1 at x*

**Lemma 2.1 (the (w, C, v) parametrisation; PROVED).** Let x_u be a slice point with u ≡ 1 + cT (mod T²),
c ≠ 0 (q odd, k ≥ 2), and let (L', j, γ, g', E) be a Case B family valid at x_u; s := N + 1 + γ, L' = g'm'.
Write E = L'w − 1, E' = L'C − 1 (possible as E ≡ E' ≡ −1 mod L'), a := deg w, b := deg C. Then
(a) L'wC − w − C = T^s g', equivalently, with v := m'wC − T^s: **m'wC = T^s + v and w + C = g'v**;
(b) T ∥ w, T ∥ C, T² | v, v ≠ 0, a, b ≥ 1, deg(m'wC) = s, deg v ≤ max(a, b) − deg g';
(c) deg m' = s − a − b, deg g' ≤ max(a, b) − 2, hence **l = deg L' ≤ s − 2 − min(a, b) ≤ N + γ − 2 ≤ 2N − k − 1**.
In particular for each N there are only finitely many such families, and N + γ ≥ 3 (for k = 2: j + γ ≥ 2; so
j = 0 is impossible, which proves the O166 claim).
*Proof.* (a) EE' = D expands to L'²wC − L'(w + C) + 1 = 1 + T^s L'g'; divide by L', then by g'.
(b) E ≡ −u ≡ −1 − cT (mod T²) gives L'w ≡ −cT, so T ∥ w; E' ≡ −u^{−1} ≡ −1 + cT gives T ∥ C; then v ≡ 0
(mod T²) because s ≥ 2. If v = 0 then E + E' = −2, impossible for monic E, E' of positive degree (q odd: equal
degrees give lc 2 ≠ 0, unequal degrees give positive degree). If deg(m'wC) ≠ s then
deg v ≥ deg(m'wC) ≥ a + b > max(a, b) ≥ deg(w + C) = deg(g'v) ≥ deg v, a contradiction (a, b ≥ 1).
(c) is degree bookkeeping from (a), (b) and deg v ≥ 2; γ ≤ j = N + 1 − k. ∎
*Remark (corrects the O166 heuristic).* FUNCTIONFIELD_ES2 §0.2 argued that the expected number of covering
families diverges over ℓ = deg L'. That sum treated ℓ as free at fixed N; Lemma 2.1 shows ℓ ≤ 2N − k − 1.
With this, the same heuristic gives, at a random slice point, an expected number ≈ Σ_N poly(N)·q^{−N} of covering
Case B families of level N: a convergent sum (Assessment; §3 gives the numbers).

**Lemma 2.2 (Z + Z' ≠ 0; PROVED, q odd).** In the normal form (****) of FUNCTIONFIELD_ES2 at x*_c
(E = T^{N+1}Z − (1 + cT), (1 + cT)E' = T^{N+1}Z' − 1, Z monic, lc Z' = c), Z, Z' ≠ 0, L' | Z + Z', and Z + Z' ≠ 0.
*Proof.* Z = 0 gives E = −(1 + cT); monic forces c = −1, E = T − 1, and E ≡ −1 (mod L') forces L' = 1; then
T − 1 | 1 + T^s gives 2 = 0. Z' = 0 gives deg E' < 0. The congruences E ≡ E' ≡ −1 (mod L') read T^N Z ≡ c and
T^N Z' ≡ −c (mod L'), so L' | T^N(Z + Z'), i.e. L' | Z + Z'. Suppose Z' = −Z; lc gives c = −1. Using
E + 1 = T(T^N Z − c) and E + 1 = L'w = TL'η (η := w/T, T ∤ η by Lemma 2.1(b)), we get c − T^N Z = −L'η, and the
right side of (****) is −T^{N+1}Z² + cTZ = TZ(c − T^N Z) = −TZL'η. So (1 + cT)T^{γ−1} g' = −Zη; as T ∤ η and
T ∤ (1 + cT)g', γ ≥ 1 and v_T(Z) = γ − 1. Put Z = T^{γ−1}Z1: Z1 η = (T − 1)g'. From
L'η = T^N Z − c = T^{N+γ−1}Z1 + 1 and g' | L' we get gcd(g', Z1) = 1, so g' | η and Z1·(η/g') = T − 1. If
Z1 = 1 then L'g'(T − 1) = T^{N+γ−1} + 1, false at T = 1. If Z1 = T − 1 then Z' = −T^{γ−1}(T − 1) and
T^{N+1}Z' − 1 = −T^{N+γ}(T − 1) − 1 is not divisible by 1 + cT = 1 − T (value −1 at T = 1). ∎

**Lemma 2.3 (degree window at x*_c; PROVED).** With z = deg Z, z' = deg Z', l = deg L' at x*_c:
(i) γ + l + deg g' = N + z + z'; (ii) l ≤ max(z, z'), z ≠ z', |z − z'| ≥ N − γ ≥ k − 1;
(iii) B0 := Z + (1 + cT)Z' has v_T(B0) = γ, so γ ≤ deg B0 ≤ max(z, z' + 1);
(iv) consequently **N ≤ 2 max(z, z') − min(z, z') + 1 ≤ 4l − 1 − 3 min(z, z')**, and with Lemma 2.1:
**(N + 1)/4 ≤ l ≤ 2N − k − 1** (here l ≥ 1 always: l = 0 is impossible).
*Proof.* (i) is the degree of (****): its right side T^{N+1}ZZ' − B0 has degree N + 1 + z + z' > max(z, z' + 1)
(N ≥ 1). (ii) L' | Z + Z' ≠ 0 (Lemma 2.2) gives l ≤ deg(Z + Z') ≤ max(z, z'). Then (i) with deg g' ≤ l gives
2 max(z, z') ≥ 2l ≥ z + z' + N − γ, i.e. |z − z'| ≥ N − γ ≥ N − j = k − 1 ≥ 1. (iii) Reduce (****) mod T^{N+1}:
(1 + cT)T^γ L'g' ≡ −B0 with γ ≤ N − 1 and T ∤ (1 + cT)L'g', so v_T(B0) = γ (in particular B0 ≠ 0).
(iv) From (ii), γ ≥ N − |z − z'|; with (iii), N ≤ max(z, z' + 1) + |z − z'|, which is 2z − z' (z > z') or
2z' − z + 1 (z' > z). Finally z + z' + 1 ≤ 2l by (i)–(ii), so max(z, z') ≤ 2l − 1 − min(z, z'). ∎
*Use.* At x*_c a search over all j ≤ 4l − k for each l = deg L' ≤ L0 is a complete exclusion of every Case B
family with deg L' ≤ L0, whatever N; by Lemma 2.1 it then also excludes every family of every level N with
2N − k − 1 ≤ L0.

## 3. Searches, controls, and what x*_c really is

**Complete-range search at x*_c (EVIDENCE, computer search with independent cross-check).**
`ff3_caseB 3 2 0 13 -1 1 c` (all monic L' with T ∤ L', deg L' ≤ 13; for each, every j ≤ 4 deg L' − 2, which is
the complete range by Lemma 2.3; every γ ≤ j, both branches): **0 Case B families for c = 1 and c = 2**
(logs `data/ff3_caseB_xstar_c1.txt`, `_c2.txt`). With Lemma 2.3 this excludes every Case B family with
deg L' ≤ 13 at any level N, and by Lemma 2.1 every family of level N ≤ 8 (j ≤ 7). With the Case A theorem
(FUNCTIONFIELD_ES2 §0.2): **no linear family of level ≤ 8 and no family with deg L' ≤ 13 is valid at x*_c.** Earlier (I1): also 0 for
deg L' ≤ 13, j ≤ 14. The deg L' = 13 layer alone tested 7.8·10⁷ monic residues ρ per c (about 25 min per c on one core).
Cross-check: `scripts/ff3_check.py` (sympy factorisation of D, all monic divisors, no CRT shortcut) reproduces
the family sets of ff3_caseB exactly on small ranges, at x*_c and at random slice points, and verifies the found
families end to end (explicit irreducible P in the class, X, Y, Z monic with T²/P = 1/X + 1/Y + 1/Z and NC);
log `data/ff3_check_log.txt`.

**Control: x*_c is not visibly special (EVIDENCE; this settles R166 D6 in the negative direction).**
Random slice points that agree with x*_1 to a given T-adic precision, searched with the same complete j-range
and deg L' ≤ 9 (`scripts/ff3_ctl.sh m 40 9 0`, 40 points each):
| agreement with 1 + T | points with ≥ 1 family | mean number of families |
|---|---|---|
| mod T^4 | 7/40 | 0.35 |
| mod T^6 | 1/40 | 0.025 |
So a point that merely shares x*'s first six T-adic digits is expected to carry ≈ 0.03 Case B families of size
deg L' ≤ 9. The empty search at x*_c is exactly what a generic point of its T⁶-cylinder shows. There is no sign
of a structural obstruction at x*_c. Conjecture 0.2 looks like a *lottery statement with a convergent expected
count*: the expected number of Case B families of level N at a point is ≈ poly(N)·3^{−N}, and x*_c has none
of small level.

**Assessment (the right target is O(3, T²) ≠ ∅, not x*_c).** By Lemma 2.1 each level N carries finitely many
family-cylinders, each of Haar mass q^{−(N+1)} in the slice. Let U(m) be the slice mass not covered by
families of level ≤ m (a finite computation) and T(m) := Σ_{N ≥ m} #cyl(N)·q^{−(N+1)}. If U(m) > T(m) for one m,
some slice point is uncovered (the uncovered set is closed, and its mass is ≥ U(m) − T(m) > 0), so O(3, T²) ≠ ∅
and no finite linear covering exists — the conclusion of Conjecture 0.2, without deciding x*_c itself. An
explicit bound #cyl(N) ≤ K q^{(1−δ)N} gives T(m) ≤ K q^{−δm}/(q^{δ} − 1)·q^{δ−1}, so it suffices together with a
census showing U(m) stays above that for one moderate m (heuristically U(m) tends to a positive limit). Case A families at
generic slice points need the same bound.
What the parametrisation of Lemma 2.1 gives (PROVED, elementary): with t := deg v, the family is determined by v
and an ordered factorisation T^s + v = m'·w·C (all monic), so there are ≤ q^{t−1}·d₃(T^s + v) of them; and
min(deg E, deg E') = s − t, so their cylinders number ≤ q^{s−t}. Hence the level-N, given-γ cylinders number
≤ q^{(N+1+γ)/2 + o(N)}. This beats the needed q^{N} only for γ ≤ (1 − 2δ)N. **The whole difficulty sits in the
regime γ ≈ j = N + 1 − k, i.e. a0 and b0 both divisible by almost the full power T^j**, where s ≈ 2N, deg v ≈ N
and deg E ≈ N. A proof of Conjecture 0.2's conclusion needs a count of factorisations T^{2N} + v = m'wC with
v | w + C, deg v ≈ N, beating q^{N} by q^{−δN}. (Heuristically the count is poly(N).)

**Lemma 3.1 (only j − γ ∈ {0, 1} matters; PROVED).** If (L', j, γ, g', E) is a Case B family valid at x_u with
γ ≤ j − 2, then (L', j − 1, γ + 1, g', E) is also one, and its cylinder (E ≡ −u mod T^{k+j−1}) contains the first
one's. *Proof.* D = 1 + T^{k+j+γ}L'g' is unchanged, g = T^{γ+1}g' still divides L = T^{j−1}L', and the congruences
of Lemma 1.1(i) only weaken. ∎
So the union of the covered cylinders comes from families with s = k + j + γ ∈ {2N − k + 1, 2N − k + 2}: exactly
the regime where the elementary count of §3 gives q^{s/2} ≈ q^{N + 1 − k/2} cylinders at level N, i.e. mass
≈ q^{−k/2}·q^{o(N)} per level — no decay. **Dictionary (Assessment).** In this regime a family is a factorisation
E·E' = 1 + T^s·L'g' with E ≡ E' ≡ −1 (mod L'), i.e. a point on the hyperbola EE' ≡ 1 (mod T^s) in a box
(deg E + deg E' = s + l + deg g'). Counting such points is a Kloosterman problem modulo T^s, and the Weil/
square-root bound q^{s/2} is exactly the bound above. Deciding whether ES₃(T², ·) has a finite linear covering
(through the measure route) therefore needs a count that beats square root by q^{−δN} — the function-field
face of barrier B3. For fixed q = 3 no beyond-square-root input for this shape is known to me.
