# AGENT REPORT O152 — brainstorm: involutions, parity, topological existence

Branch `side-agent/bs-involutions`. Memos in `BRAINSTORM/invol_*.md`, scripts `scripts/bs_invol_*`. ES is
not solved; no memo is LIVE. Prior art in the repo: `WINDMILL.md` (earlier wave, ~7,000 weights tested on
primes, Prop 2: no integral affine windmill pieces). This wave adds new tests and small PROVED
propositions; it does not repeat that catalogue.

**(a) `invol_windmill_signature.md` — UNCLEAR, leaning COLLAPSES.** A Zagier-type proof is one of the few
routes the barrier map does *not* exclude. It uses p's global factorisation only when it evaluates #Fix σ,
so it evades B1/Thm C, B3, B6 and Theorem M. It passes T1 because its failing step at m² is "#Fix σ is
odd". Its whole content is an identity `W(n) ≡ D_φ(n) (mod 2)`, with W a weighted ES count and D_φ a
divisor-type count (or a binary-form count). New test, over *all* n (composites give ~3,333 constraints,
far more than the unknowns): 385 natural weights, including ET Type I/II × residues/divisibility and
pairwise ANDs (rank 200). The right sides were divisor-type mod 24/120/168, 1564 binary forms, and
Liouville-type Ω_r. The intersection with the weight span is 1-dimensional, spanned by the trivial
repeated-denominator count, which is even on all hard primes. Zagier controls pass. Also new (PROVED, one
line): `X(p)={(t,u,v): (tu−1)(tv−1)=tp+1}` has odd size for every prime p, and it contains every
divisor-form ES certificate. But its odd point (p+2,1,1) is not ES, and its ES part is odd for only 36/61
of the hard primes tested. Strongest reason: the multilinear ES equation has no infinite symmetry group
that couples slices, and no natural weight has a windmill parity signature (EVIDENCE).

**(b) `invol_topological.md` — COLLAPSES.** Lemma T: Sperner, Tucker, mod-2 degree, Smith and
Lefschetz–Hopf on a finite K(p) all reduce to weighted parity counts, or to a signed exact count, so they
reduce to (a). The weights are cells mapped to solutions. Prop K (PROVED): the solution 2-complex has
every edge in exactly one triangle, so `χ = V − 2f`. It is homotopy equivalent to the denominator–solution
incidence graph, so topology sees f(p) only with weight 2. F_q-Lefschetz and Chevalley–Warning are local
data, so they hit B1/B5. A discrete IVT needs a slowly varying function whose zeros are divisibility
events. Strongest reason: Lemma T plus Prop K.

**(c) `invol_sign_identities.md` — COLLAPSES.** Prop S (PROVED, elementary) concerns sign identities
`(−1)^{W(n)} = εψ(n)` with ET Type I/II weights that hold at odd squares. In these, ε = +1. If ψ is a
character, W(p) is even on every square class, which is exactly the hard core: such identities fail at
T1/B1. Only Liouville-type right sides survive, and the all-n test finds none among the natural weights.
Also, the parity of f(p) is the sign of the coordinate swap on ordered solutions. That set has no group
structure, so a Zolotarev-type evaluation is unavailable. Strongest reason: Prop S.

By-products for the ledger, if wanted: Prop S, Prop K, Lemma T (all PROVED, elementary). Also the odd set
X(p) and the all-n windmill-signature EVIDENCE (E1–E4).
