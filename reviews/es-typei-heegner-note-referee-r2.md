# Referee report R118 — O118 revision of `paper/es-typei-heegner-note.tex`

Hostile internal referee (R118). Scope: new Theorem 1 (unconditional `o(N log²N log log N)`), new §9
("The exceptional spectrum on average over the level"), Theorem 2 under (SEL) or (EFF), title/abstract,
consistency. Compared against `EXCEPTIONAL_TYPEI_LOGLOG2.md`, `reviews/exceptional-typei-loglog2-review{,-B}.md`.
Internal review only; not external refereeing.

## A. Cited inputs (checked against sources)

* **DI Theorem 7** (`sources/o111/deshouillers-iwaniec-1982.pdf`, scan p. 233 = PDF p. 15): the paper's quote of
  (1.41) and of the Σ^{(q)} sentence is **verbatim correct** (`Q,N,X ≥ 1`, sum `n ≤ N`, `X^{4iκ_j}`,
  `(QN)^ε(Q+N+√N X)N`, "constant implied in ≪ depending on ε alone"). 
* **DI (8.18) misprint** (scan p. 277): confirmed. With `Y₁=√(Q+N)` the printed second line does not follow;
  with `Y₁=Q+N`, `(1+√(Y/Y₁))(Q+N+Y₁) ≍ Q+N+√(NY)+√(QY)`, which is the printed third line. SOUND.
* **Drappeau Lemma 4.10** (`sources/o116/drappeau-1504.05549.pdf`, arXiv p. 16): **verbatim correct**, as are
  the Lemma 4.9 setting (`q₀ ≥ 1`, `Y ≥ 1`, `Q ≥ q₀`, scaling matrices independent of q), the `N ≥ 1/2` of
  Prop. 4.7, and the definition of `E_{q,a}` in §4.2.3. His p. 19 remark ("q₀ appears only with negative powers in
  the error terms") is reproduced fairly. The q₀-uniformity of `≪_ε` is **flagged as our reading** both in §9
  and in the intro status paragraph. Adequate. (Drappeau also requires `χ(−1)=(−1)^κ`; for even χ, κ=0 — fine.)
