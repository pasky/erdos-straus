# z31 — Graph theory, percolation and the probabilistic method (O261 field memo 11)

Labels as in DISCOVERIES.md. All external statements here are classical textbook facts (memory; Alon–Spencer); no new sources.
Builds on (J)72 (sterility = percolation; windowed König lemma; counting-only certificates collapse to the union bound),
(J)77, FORCED_WINDOW §4 (Poisson/Erdős–Rényi model), (J)1 ("the lottery is Poisson-class with no rigidity").

## (a) Counterpart
For fixed p let G_p be the bipartite "shot graph": left vertices = parameters C (E1) or d (E2), right vertices = divisors w of
4Cp + 1 (resp. p + 4d), and an edge is *good* if w ≡ −1 (mod 4C) (resp. 4d). B2 ⟺ G_p has a good edge. In a random model
(edges good independently with probability 1/φ(4C)), #good edges is ≈ Poisson(μ), μ ≍ (log p)² (EVIDENCE: R(p) = 44, 52, 68
at p ≈ 10⁸, 10⁹, 10¹⁰), and P(no good edge) ≈ e^{−μ}: summable over p, so the model predicts finitely many failures —
exactly the ES heuristic (the two lines have different effective μ: E2 fails 3 times ≤ 10¹¹, (★) 14 times ≤ 10¹⁰;
(J)90).

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
Blocked by F1 (no randomness at a fixed p: the standard tools — second moment, Janson — need a probability space, and with
p as the random variable they yield almost-all statements; no deterministic pseudo-randomness input for the shot graph of a
single p is known to us) and by direction (LLL is an avoidance tool). (R-O261 repair M9: this is an Assessment, not an
exclusion of all probabilistic methods.) The F2 polylog count is what makes the Poisson heuristic convincing and simultaneously what makes
union/second-moment bounds useless pointwise (μ ≍ (log p)² gives P(fail) ≈ p^{−c log p}: plenty for summability over p,
nothing at one p).

## (d) Verdict: ANALOGUE (B2 = "a sparse arithmetic random-like graph has an edge"; deterministic versions are open
problems). **NOT SHARP.**
