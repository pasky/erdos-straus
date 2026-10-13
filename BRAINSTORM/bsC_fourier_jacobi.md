# bsC_fourier_jacobi — certificate indices as Fourier–Jacobi coefficients (O176; O172 spark 3)

**ES is not solved here.** Labels as in DISCOVERIES.md. Script `scripts/bsC_min_jacobi_index.py`.

## Idea
Kudla's genus-2 series 𝓔(Z) = Σ_T a(T) e(tr TZ) has a Fourier–Jacobi expansion 𝓔 = Σ_m φ_m(τ, z) e(mτ'), and the
index T' = [[f, 1],[1, f']] (R172 D5/D6: a *chosen* T1-relevant index, Diff(T') = {p}) is the coefficient c_{f'}(n = f,
r = 2) of the Jacobi form φ_{f'} of index f'. Spark 3: sum the certificate coefficients over f ≡ −1 (mod 4cd) — a
twisted Jacobi coefficient sum — and look for positivity.

## Literature
Eichler–Zagier, *The theory of Jacobi forms* (Birkhäuser 1985), Thm 2.2 (c(n, r) depends only on 4nm − r² and
r mod 2m) and §2 (theta decomposition); Kudla, *Central derivatives of Eisenstein series and height pairings*,
Ann. Math. 146 (1997); Kudla–Rapoport–Yang 2006, Ch. 5 (genus-2 generating series on Shimura curves).

## Statements
**Prop 1 (fixed index = congruence family; PROVED).** Fix the Jacobi index f' and the slice (c, d), M = 4cd, with
f' ≡ −1 (mod M). Then the Type II certificates of a prime p with this (f', c, d) exist iff f' | 1 + 4c²dp and
(1 + 4c²dp)/f' ≡ −1 (mod M), i.e. iff **p lies in a fixed residue class mod f'·M** (when gcd(4c²d, f'M) allows), and
the coefficient c_{f'}(f, 2) depends only on (4ff' − 4, 2 mod 2f') = (16c²dp, 2). *Proof.* Solve for p; Eichler–Zagier
Thm 2.2. ∎ So any statement using finitely many Fourier–Jacobi indices is a finite congruence covering (B1: POINTWISE_SIZE
Thm M/C), and twisted sums over f at fixed index range over **p** (B6), not over certificates of one p.
**Prop 2 (fixed p = one coefficient per index; PROVED).** At fixed p and slice, each Jacobi index f' contributes at most
the one coefficient n = (1 + 4c²dp)/f'. The "twisted Jacobi sum over f ≡ −1 (M)" at fixed p is therefore the
certificate count itself, weighted by c_{f'}(f, 2) = (genus-invariant local factors, R172 D8) — positive on Diff = {p}
indices (Kudla, cited), so it is **positive iff a certificate exists**: a tautology, not a mechanism.

## Barrier screen
* **B1** (Prop 1): fixed index sets = congruence coverings; the least usable index must grow (EVIDENCE below).
* **B6** (Prop 1): the natural twisted sums average over p.
* **B2** (Prop 2 + R172 D8): coefficients are genus functions; the selection f ≡ −1 (M) is a representative choice.
* **T1**: at n = m² every index has even |Diff| ≠ 1 hence coefficient 0 (R172 D3), consistent.
* Thm 9.1 (fixed-level Eisenstein identities cannot certify Type I/II counts) applies to any fixed finite set of
  Jacobi indices.

## Cheap numerics (EVIDENCE; `scripts/bsC_min_jacobi_index.py 1000000`, 1 s)
Least Jacobi index F*(p) = min over Type II certificates of min(f, f'), primes p ≡ 1 (24) < 10⁶; records:
(73, 7), (193, 15), (1201, 31), (2521, 47), (3361, 99), (33289, 155), (90841, 167), (144169, 191), (167521, 259),
(225289, 279), (361321, 287), (915961, 303), (954409, 335). Slow growth, as expected from B1 (no finite index set).

## Assessment
**COLLAPSES (B1/B6 for fixed index, B2 at fixed p).** Fourier–Jacobi re-indexes the problem by the cofactor f′;
fixing f′ fixes a congruence class of p. Promise 0.
