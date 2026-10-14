# y2 — Zamolodchikov period 5 with a frozen N: what the dynamics forces (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** Item (d) of the brief.

## Idea
In cycle order (c, h, m, h′, s), the pentagon frieze at N is the twisted Lyness recurrence
`x_{k−1}x_{k+1} = α_k x_k + β_k`, (α, β) cycling through (1,1), (N,1), (1,1), (1,N), (1,N)`
(cm = h + 1, hh′ = Nm + 1, ms = h′ + 1, h′c = s + N, sh = c + N).
This is a period-5 birational map φ_N of the (x_{k−1}, x_k)-plane (Zamolodchikov periodicity for A₂ with
coefficients; Cuntz–Holm–Jørgensen Prop. on glide symmetry). Question: does the dynamics force a term ≡ 0 (mod 4)?

## Results
* **Mod 2 forcing (PROVED; FRIEZE_ES Lemma 1.1).** Every integral orbit with N odd has exactly two even terms, and they
  are adjacent in the *frieze* order (h′, c, m, s, h). This is the Lyness parity law: over F₂ the map φ_N has a
  single 5-cycle of "integral type".
* **Mod 4 non-forcing (PROVED).** No dynamical statement on φ_N over ℤ/2^k can force a term ≡ 0 (mod 4). At N = M²
  every integral orbit has both even terms ≡ 2 (mod 4) (FRIEZE_ES Cor 1.4), while φ_{M²} ≡ φ_N mod 2^k for prime
  N ≡ M² (mod 2^k). Any forcing argument must use the archimedean/global integrality of the whole orbit and must fail at
  squares (B5).
* **Laurent phenomenon.** All terms are Laurent polynomials in (c, h) with coefficients in ℤ[N] and positive
  coefficients. Integrality of an orbit is c | h + 1, ch | N(h + 1) + c, and so on, i.e. the B2 divisor conditions.
  Positivity of the Laurent expansions gives positivity of the frieze, not integrality.

## Iteration
* *Violate "fixed N":* let N vary along a chain, e.g. the bi-infinite Farey path, whose consecutive 5-windows are
  pentagons at N_i = K(b_{i+1}, b_{i+2}, b_{i+3}). This gives every N_i trivially from three letters; the target N is
  not reached deterministically. Dead.
* *Violate "A₂":* in A₃ (hexagon) a zero mod 4 IS forced in some mod-2 patterns (pattern (0⁶): all six quiddities even,
  and in the data every such word has one ≡ 0 (4)). But a hexagon gives 4 unit fractions
  (y2_hexagon_degeneration).

## Literature
A. B. Zamolodchikov (1991), periodicity of Y-systems; Lyness 5-cycle (1942). Fomin–Zelevinsky, *Y-systems and
generalized associahedra* (2003), for A₂ periodicity (from memory). Cuntz–Holm–Jørgensen, arXiv:1909.02332 (verified
abstract), for friezes with coefficients.

## Barrier screen
B5/T1 kills every 2-adic dynamical forcing (above). B2: integrality = divisor conditions.

## Cheap numerics
Covered by `scripts/y2_even_edge.py` (mod 2 law on 5.1 M orbits) and `scripts/y2_hexagon.py` (hexagon patterns).

## Assessment
NEGATIVE with a PROVED positive kernel (mod 2 forcing). The strongest thing the A₂ dynamics forces is "an even
edge exists". The sign is the 2-adic weight of that edge and cannot be forced locally. Promise 0/5.
