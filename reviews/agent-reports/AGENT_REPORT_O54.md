# AGENT REPORT O54 — verify.py blocks (cz)–(df)

Branch `side-agent/verify-blocks-3`. Seven new replay blocks in `verify.py`, written in the style of (cp)–(cy):
a comment header pointing to the document and lemma, `check_xx()` with local imports, assertions that carry
labelled messages, and a one-line summary print. All seeds are fixed, so runs are deterministic. Unless noted,
the arithmetic is exact (Fractions or integer numpy).

| block | document | what is asserted | time |
|---|---|---|---|
| (cz) | POINTWISE_OMEGA10 | Lemma 3.2 polarization `Q = E_P Θ²` exact; Thm 3.4 (QM) for **every** matching on 549 random hypergraphs (rational λ, w_E ≤ 2, 128 at w_E = 2); equality cases; C-1 and Lemma 3.1 `G_F ≤ Γ ≤ 1` on 256 systems with **non-uniform** product measures; identity (i); negative control `(5/4)^n`; Cor 4.1 as `energy^k·2^{t+1} ≤ 1` on 153 DNFs | 1.2 s |
| (da) | POINTWISE_OMEGA11 | Lemma 1.1 `G′ ≤ 1` on 359 digit systems, 68 of them conditioned (Remark (ii)); the proof's selection identity `G′ = Σ_V μ′^V‖L_V F‖²`; graded-quarantine toy (Lemma 2.1 fibre probabilities, CRT uniformity, LLL bound `P(no event) ≥ ∏(1−2P)`); Lemma 2.2 atomic iteration at T = 3000 for c = 1/8 and 1/64: the (LLL) conclusion, every charging step, the cost bound, and `P(E) ≤ s(M,D)` | 1.3 s |
| (db) | POINTWISE_OMEGA12 | Lemma 2.1 identities, injectivity and the involution on all 35 803 atoms (T = 10⁴); Lemma 1.1(a)–(c); Lemma 3.1 steps (`ℓ\|4ad ⇒ ℓ∤N`, the large-q pointwise bound); Lemma 2.2 on all 253 (A,C,B) blocks; §7 table regression (28.75 / 62.18 / 18.37 / 45.30) | 1.0 s |
| (dc) | POINTWISE_HAAR | Lemmas 1.1, 1.2 (NA) and 1.3 (inflation) by exact enumeration with biased marginals; Thm 1.4 (both bounds) on 346 systems satisfying the lopsided-LLL hypothesis, 158 of them with Δ > 0; Prop 1.5's M = 35 example | 13.5 s |
| (dd) | POINTWISE_OMEGA13 | Lemma 3.1 (a), (b) on all 258 644 atoms with M ≤ 3·10⁴ (integer Jacobi helper, cross-checked against sympy); a direct unit-square test for M ≤ 1500; Lemma 1.1 (β-weighted LLL: P(Av) bound, `P(E\|Av(S)) ≤ x_E`, outside-event bound) on 355 systems with general events, β ∈ {6/5, 4/3, e^{1/3}} | 3.4 s |
| (de) | POINTWISE_TRANSFER | Lemma 5.1 (i)–(iii) and identity (5.1) for m = 4..8 and 11, M ≤ 3000; Lemma 5.0: all 798 Type II solutions among 2921 solutions of m/p (m = 4..7, p ≤ 200) have the form (5.1), with p mod M ∈ R_m(M) | 1.3 s |
| (df) | EXCEPTIONAL_SPW | the exact certificate σ ≤ 72/185 (N = 300, e = 630). It is **embedded** and needs no scipy: g = h/185, h ∈ {−1,0,1,2}, given as 31 runs. Span membership is checked by cyclotomic divisibility Φ_{630/c} for gcd c ∈ {1,2,3}; a one-point perturbation fails it (control). The only big divisor is 630, so z = g⁺ and the bound is 1 − 113/185. With scipy, `scripts/spw_local_cert.py` re-derives 72/185 | 0.2 s |

Docs: `verify.py` docstring and the `STATUS.md` verify.py bullet are updated.

Full run: `ulimit -v 8000000; OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 uv run --with scipy python verify.py`
prints **all checks passed** (4 min 50 s wall; the new blocks take ≈ 22 s).

Scope notes (no overclaiming):
* These checks are sanity replays on small instances and are EVIDENCE only. They do not make PROVED statements
  more proved. The exception is (df), which re-verifies a certificate whose exactness is the claim.
* The (da) Lemma 2.2 replay is the *atomic* iteration with all violators raised per round. The proof allows this,
  but it is not the distinct-event variant used in `omega11_graded.py`.
* (dc) uses floats only for the final `−log P(Av)` comparison. P(Av), μ, Δ and K are exact.
