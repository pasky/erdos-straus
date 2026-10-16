# z23 — the class-group walk is free (expander), so descent = existence (O251)

## Idea
Measure what a walk adds: on line k, BFS in the class group (generators: prime forms ℓ ≤ 40) from every class to the
nearest ES class.
## Literature
Jao–Miller–Venkatesan, "Expander graphs based on GRH with an application to elliptic curve cryptography", J. Number
Theory 129 (2009) 1491–1504: under GRH, class-group Cayley graphs with generators of norm ≤ (log|Δ|)^{2+ε} are expanders.
## Barrier screen
B2: the walk reaches *any* nonempty target in O(log|Δ|) steps; the only question is non-emptiness = B2 event per line.
B6 irrelevant (fixed p). T1: no target at squares.
## Cheap numerics
`scripts/z23_cayley.py 3000 40 1,2,3,5`: worst-start distance ≤ 4 (k = 1), ≤ 8 (k = 2), ≤ 6 (k = 3), ≤ 5 (k = 5) when an ES
class exists; lines without ES classes: 26 % … 73 %.
## Assessment
EVIDENCE + conditional literature. Negative: "Y = 1 within O(log p) moves" ⟺ (GRH) existence on the line.
