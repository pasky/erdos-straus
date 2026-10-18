# z31 — Graph theory, percolation and the probabilistic method (O261 field memo 11)

Labels as in DISCOVERIES.md. All external statements here are classical textbook facts (memory; Alon–Spencer); no new sources.
Builds on (J)72 (sterility = percolation; windowed König lemma; counting-only certificates collapse to the union bound),
(J)77, FORCED_WINDOW §4 (Poisson/Erdős–Rényi model), (J)1 ("the lottery is Poisson-class with no rigidity").

## (a) Counterpart
For fixed p let G_p be the bipartite "shot graph": left vertices = parameters C (E1) or d (E2), right vertices = divisors w of
4Cp + 1 (resp. p + 4d), and an edge is *good* if w ≡ −1 (mod 4C) (resp. 4d). B2 ⟺ G_p has a good edge. In a random model
(edges good independently with probability 1/φ(4C)), #good edges is ≈ Poisson(μ), μ ≍ (log p)² (EVIDENCE: R(p) = 44, 52, 68
at p ≈ 10⁸, 10⁹, 10¹⁰), and P(no good edge) ≈ e^{−μ}: summable over p, so the model predicts finitely many failures —
exactly the ES heuristic, and exactly why E2 (smaller μ) has three failures and (★) has 14 ≤ 10¹⁰.

## (b) What graph/probability theory proves pointwise
* **Janson / second moment** bound P(no good edge) ≤ exp(−μ + Δ/2) — in a *random* model only. For a fixed p there is no
  probability space: the "randomness" is p itself, and the tools convert to statements about almost all p (F1).
* **Lovász Local Lemma** proves that *all* bad events can be avoided simultaneously (P(∩ Ā_i) > 0). B2 needs the opposite: that
  not all good events fail. LLL points the wrong way; its constructive versions (Moser–Tardos) likewise.
* **Deterministic arithmetic percolation** — the closest genuine analogue — is open in the classical cases: e.g. the Gaussian
  moat problem (walk to infinity on Gaussian primes with bounded steps; (memory), open), and the campaign's own sterility
  questions (Conjecture 0.2 over F₃[T]; r = 17 sibling conjecture, (J)77). (J)72 PROVED that counting-only certificates
  collapse to the union bound, i.e. the probabilistic method in its counting form cannot certify a deterministic instance.

## (c) Transfer
Blocked by F1 (no randomness at a fixed p; every probabilistic tool becomes an almost-all statement) and by direction (LLL is
an avoidance tool). The F2 polylog count is what makes the Poisson heuristic convincing and simultaneously what makes
union/second-moment bounds useless pointwise (μ ≍ (log p)² gives P(fail) ≈ p^{−c log p}: plenty for summability over p,
nothing at one p).

## (d) Verdict: ANALOGUE (B2 = "a sparse arithmetic random-like graph has an edge"; deterministic versions are open
problems). **NOT SHARP.**
