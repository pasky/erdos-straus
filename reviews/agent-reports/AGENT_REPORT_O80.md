# AGENT REPORT O80 — Mordell-type coverings mod a new prime r (branch `side-agent/mordell-13`)

Checkpoint 1. Main file: `POINTWISE_MORDELL.md`. Scripts: `scripts/mordell_*.py`. Data:
`data/mordell/`.

## Results

1. **Theorem 3.1 (PROVED by finite computation; independent re-check required).**
   Let p be prime with `(p/13)=−1`.
   (a) If `(p/11)=+1`, ES holds for p unless `p≡112561 (mod 240240)`.
   (b) In general, ES holds for p unless `p mod 720720 ∈ {112561, 352801, 380881, 418321,
   473761, 483841}`.
   Certificates: `data/mordell/cert_r13_np_240240.json` (20 ET classes),
   `data/mordell/cert_r13_main_720720.json` (31 classes); checker `scripts/mordell_check.py`
   (stand-alone, sympy only: polynomial identity, positivity for n>1, integer-valuedness on each
   residue class mod L; negative controls fail as they should). This extends Salez's single-prime
   filter `S_13={0,5,6,8,11}` to the residues 2, 7 mod 13 up to the listed exceptional classes.
   Novelty: modest (a two-prime filter); I found no published statement of it.
2. **No complete covering found** for either variant of r=13.
   * main (`(p/13)=−1`, any `(p/11)`): the T-generic analysis (§2: points with `x_q=1` off
     T={11,13}; classes become rigid, finitely many boxes per T-level) leaves only the cell
     `x≡2 (11), x≡2 (13)`; ≈25% of that cell stays uncovered after all classes with M≤10⁶ and the
     complete II1/II2/I4 enumeration to T-level `11³·13³`.
   * **Computation 4.1 (CERTIFIED, one engine):** the point `x*` (`x*_11=x*_13=2`, `x*_q=1` else)
     lies in no ET class with modulus ≤10⁶ and in no II1/II2/I4 class with {11,13}-part
     dividing `11³·13³`. Hence every finite covering of `Σ_13` (main) needs a class of modulus
     `>10⁶` (PROVED from 4.1 by compactness + Dirichlet).
   * **Conjecture 4.2:** `x*` is sterile, so no finite set of polynomial ES identities covers the
     Mordell-hard primes with `(p/11)=(p/13)=−1` (ET Prop 1.9 completeness + compactness).
   * np (`(p/11)=+1`): no structured obstruction found (T-generic for |T|≤3, c-generic and
     c²-generic points all covered); the best-first tree search (Mmax=10⁷, primes ≤100) has open
     Haar mass 5.5·10⁻⁷ of `Σ_13^{np}` after 16800 nodes, still decreasing slowly. Undecided.
3. **Theorem C does not explain the main-variant obstruction**: `x*` is not square-mimicking
   (non-residue at 11 and 13); the Jacobi/character constraints are satisfiable. The mechanism is
   the TYPEI2 one (rigidity at T-generic points), and as for TYPEI2's `x̂_9`, sterility is open.
4. **r=17** (EVIDENCE): the one-prime T-generic cells `x_17≡5, 7 (mod 17)` (with `x_q=1` for all
   q≠17) are untouched by all classes with M≤10⁵; complete II-family boxes up to `17⁴` cover
   only 4.5% of them. Candidate sterile point of the simplest shape (twist at r only).
   r=11: survivors `x_11∈{2,6}`; T={11,13}-cells (2,2),(2,7) survive at M≤10⁵.

## Background runs (completed, recorded in POINTWISE_MORDELL §4.1)

* Rigid II1/II2/I4 to T-level `11⁴·13⁴`: finished; no box contains `x*`; the (2,2) cell stays
  24.76% uncovered (24.88% at level 3).
* np tree search: finished at its 30000-node cap; open mass 4.10·10⁻⁷, no covering.

## What would settle it

* Negative (main r=13, or r=17): prove a tail bound for the number of rigid boxes per T-level
  (all seven families; §2.1 gives the rigid forms for II1/II2/I1/I4, the others analogous), so
  that the uncovered measure in the cell stays positive ⇒ sterile point ⇒ no finite covering.
  For r=17 the problem is one-dimensional (u∈ℤ_17), the cleanest test case.
* Positive (np r=13): a better search (per-node targeted class search with unbounded moduli,
  not table-based); the current table method is capped by Mmax.

## Replay

```
PYTHONPATH=scripts uv run python scripts/mordell_check.py data/mordell/cert_r13_np_240240.json
PYTHONPATH=scripts uv run python scripts/mordell_check.py data/mordell/cert_r13_main_720720.json
PYTHONPATH=scripts uv run python scripts/mordell_cert.py 13 main 100000000 720720 /tmp/c.json   # regenerate
PYTHONPATH=scripts uv run python scripts/mordell_cover.py 13 main 100000000 2,3,11,17,13,19,23  # §1
PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 1000000 13 3 11,13       # §2 (~16 min)
PYTHONPATH=scripts uv run python scripts/mordell_rigid.py 11,13 3                 # §4 (~30 s)
uv run python scripts/mordell_cellcov.py 3 /tmp/o80_rigid_11,13_3.pkl /tmp/o80_boxes_1000000_11,13_3.pkl
PYTHONPATH=scripts uv run python scripts/mordell_point.py 1000000 11:2:8 13:2:8   # Comp 4.1 (~15 min)
PYTHONPATH=scripts uv run python scripts/mordell_point.py 1000000 17:5:8   # Comp 5.1 (~15 min)
PYTHONPATH=scripts uv run python scripts/mordell_rigid.py 17 4; PYTHONPATH=scripts uv run python scripts/mordell_tgen.py 100000 17 2 17
MORDELL_I1CAP=1e11 PYTHONPATH=scripts uv run python scripts/mordell_dfs.py 13 np 10000000 100 3 30000 /tmp/t.json
```
