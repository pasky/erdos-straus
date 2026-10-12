# Brainstorm O147(c): étale cohomology, Galois representations and point counts mod ℓ; cubic residues

ES is not solved; nothing here proves any case of it. Script: `scripts/bs_nonab_points.py`.

## 1. Idea

Attach to the fixed-n ES variety U_n : 4xyz = n(xy + yz + zx) (affine cubic surface; BL's object), or to
the family over n, an ℓ-adic Galois representation. Use its traces, i.e. point counts mod ℓ or
Frobenius traces of a Deligne sheaf over the n-line, as non-abelian or "motivic" input. Possible routes:
(i) a trace-function / Katz–Sarnak equidistribution over n mod ℓ; (ii) a hidden non-abelian Galois
action (on lines, on H²) whose Frobenius at p decides integral points; (iii) higher power-residue
obstructions in the spirit of T1, e.g. cubic residues at cubes n = m³.

## 2. Literature anchor

Bright–Loughran, Bull. LMS 52 (2020), arXiv:1908.02526: U_n, its compactification, Brauer group, BM
(campaign-checked: GEOMETRY_ES). Lang–Weil, Deligne Weil II: generic. Katz, trace functions (from memory).

## 3. Results

**Prop 3.1 (PROVED, elementary; EVIDENCE check ℓ ≤ 13).** For every prime ℓ and every n,
`#U_n(𝔽_ℓ) = ℓ² + 1` if ℓ ∤ n (ℓ odd), and `3ℓ² − 3ℓ + 1` if ℓ | n.
The same holds over 𝔽_{ℓ^k} with ℓ^k in place of ℓ.

*Proof.* The equation is linear in x: x·g(y, z) = −n·yz with g = n(y + z) − 4yz.
* Pairs (y, z) with g ≠ 0 give exactly one x each.
* If g = 0, a solution needs yz = 0 (n ≠ 0), and then n(y + z) = 0 forces y = z = 0. This pair allows
  all ℓ values of x.
* For ℓ ∤ 2n, the zero set of g is the hyperbola (4y − n)(4z − n) = n², which has ℓ − 1 points.

Total: ℓ² − (ℓ − 1) + ℓ = ℓ² + 1.
For ℓ | n the equation becomes xyz = 0, which has 3ℓ² − 3ℓ + 1 points.
For ℓ = 2 the first formula still holds: n odd gives xy + yz + zx = 0 over 𝔽₂, with 5 = 2² + 1 points.
`scripts/bs_nonab_points.py` reproduces the formulas for ℓ ∈ {3, 5, 7, 11, 13} and several n. ∎

**Cor 3.2 (PROVED).** The compactly supported cohomology of U_n has constant point counts: the zeta
function of U_{n,𝔽_ℓ} is that of 𝔸² ⊔ pt, for every n prime to ℓ. So no Frobenius eigenvalue depends on
n, and any trace function of the family over the n-line is constant on the set ℓ ∤ n. This matches
GEOMETRY_ES: the toric model, with the nine boundary lines rational, so H² of the compactification is a
permutation module with trivial Galois action. The fixed-n variety carries **no non-abelian or
non-Tate Galois representation** whose Frobenius at p could decide anything. Routes (i) and (ii) have no
input object.

**Prop 3.3 (EVIDENCE, brute force, all x ≤ y ≤ z).** Odd cubes have Type I and Type II solutions, so
there is no cubic analogue of ET Prop 1.6. Counts (I, II):

| n | 27 | 125 | 343 | 1331 | 2197 | 3375 |
|---|---|---|---|---|---|---|
| (I, II) | (6, 3) | (10, 6) | (26, 10) | (52, 20) | (53, 24) | (28, 14) |

Squares 9, …, 225 and 729 = 27² give (0, 0), as ET predict. The T1 obstruction is purely quadratic.
Lemma CT / ET Prop 1.6 use the quadratic character only. Cubic or higher residue symbols supply no further
obstruction at perfect powers that are not squares, so they have no "hidden obstruction" role and no
dual "hidden sufficiency" role. Square classes stay the hard core (also POINTWISE_SIZE §4.2, E3
reciprocity remark in MORDELL13E §2).

## 4. Barrier screen

* **B1–B4.** No mechanism survives to be screened. Prop 3.1/Cor 3.2 show that the ℓ-adic object
  carries only local solubility, which BL Thm 1.8 already gives for all n. Local solubility holds at odd
  squares, so it fails T1.
* **B5.** Prop 3.1 holds verbatim at n = m², where Type I/II solutions do not exist. So any
  cohomological statement about U_n mod ℓ is true at odd squares, and the step that is false at m² must
  lie elsewhere. (At n = m², ES(m²) does hold via ES(m), using non-Type-I/II solutions; consistent.)
* **B6.** Trace-function averages over n would be T7 leaks even if they were non-constant.

## 5. Viability Assessment

**COLLAPSES at step "attach a non-trivial Galois representation" (Cor 3.2: the motive of U_n is
constant mixed Tate).** The cubic-residue sub-idea **collapses** too: there is no cubic T1 analogue (Prop 3.3).
By-products: Prop 3.1 (PROVED, a crisp exact formula, `#U_n(𝔽_ℓ) = ℓ² + 1`; novelty: probably folklore,
not found in BL from memory); Prop 3.3 (EVIDENCE).
