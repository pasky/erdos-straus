# AGENT REPORT O73 — residue dispersion (RD) (branch `side-agent/residue-dispersion`)

Deliverable: `EXCEPTIONAL_LARGESIEVE7.md` (LS7), scripts `scripts/largesieve7_*.py`.
Checkpoint 1; not reviewed. ES is not solved; (DCC)/(A*) are **not** proved.

## Results

1. **Triple parametrisation (Lemma 1.1, PROVED, elementary).**
   `ℛ(M) = {−u/v mod M : gcd(u,v)=1, 4uv | M+1}`. With `t = (M+1)/(4uv)`
   the class `−4D` (`D = u²t`) also equals `−4u²t` and `−1/(4v²t)`, so
   `H* ≤ min(max(u,v), 4u²t, 4v²t)`. **Residue pinning (Lemma 1.2):** for `p | M` and
   class `≡ a (mod p)`: `4uvt ≡ 1`, `u ≡ −av`, `v²t ≡ −1/(4a)` — the residue fixes
   two of the three coordinates mod p as functions of the third. Exact check for all
   `M < 20000`.
2. **Theorem 3.1 — (RD) at one prime for ℛ(M) classes (PROVED, given Shiu 1980
   Thm 1).** `μ^{ℛ,>}_a(p) ≤ Cγ^{−5}(log p)^6 p^{−1/12}` for every residue a, uniformly
   in X, short cofactors included. Proof: dyadic boxes in (u,v,t). If some
   coordinate is long, the cofactor runs through a progression mod 4×(other two),
   and a damped Shiu+Rankin bound (Lemmas 2.1–2.2) plus the pinned pair count
   `≤ 2VT/p + 2min(V,T)` do the job. If none is long, all coordinates are
   `≤ p^{1+o(1)}` with `UVT ≥ p²/32`, and the pinning beats the weight
   `p/(UVT)` trivially. The "one cofactor per divisor" problem of LS6 §6.2 does not arise.
3. **Proposition 4.1 — (RD) as stated in LS6 is FALSE for several primes (PROVED;
   the fibre version uses the fundamental lemma).** The cut `H* > max_{p∈P} p^{1/4}` sees only
   the largest prime. One label `−1/k`, `k ≈ 2(max P)^{1/4}`, puts mass
   `≫ (max P)^{−1/4}/log z` on one residue vector. That beats
   `(log N)^C Π_{p∈P} p^{−γ₀}` once P has `> 1/(2γ₀)` primes of similar size.
   Fix: the cut must scale with `P̄ = ΠP`.
4. **Theorem 4.3 (PROVED, given Shiu).** With the product cut `H* > P̄^{κ}`, (RD) holds
   for ℛ(M) classes with **long cofactors** `n ≥ P̄^{1/2+η}`:
   `≤ C_η(log P̄)^6γ^{−5}4^{|P|}(P̄^{−κ/3} + P̄^{−η/2})`. For short cofactors
   `n < P̄^{1/2}` a single class weighs `≍ 1/n`, so this case is open in both directions
   (Remark 4.2, Assessment). Those witnesses have to be handled inside the (DCC)
   combinatorics.
5. **Proposition 5.1 — the H*-cut form of (RD) fails already at ONE prime once (a,D)
   classes are present (PROVED, elementary).** Take the (a,D) class with `a = pq`,
   `D = ℓ`. It has `H* ≥ pq/(4ℓ+1)` (mod its rough modulus `pqℓ`), sits on the residue
   `−4ℓ (mod p)` (a small-height residue), and has mass `≍ 1/(γℓ)`. This is harmless:
   LS6's route needs dispersion only for residues **outside** the deterministic
   small-height sets `R_P(H₀)`. The correct statement is the **residue-cut (RD′)**.
   The H*-cut implies (RD′), so items 2 and 4 give (RD′) for ℛ(M).
6. **Fibres (Cor 6.1).** All bounds hold for the fibre sums on average over c. The
   rough-modulus subfamily obeys them for every c. A single exceptional event uniform
   over all (P,a) is **not** proved: a fixed c can make the fibre family dense.

## Not done / open

* (RD′) for (a,D) and Case-A classes. §5 sketches the same pinning: Case A pins both
  m and m′ mod p. The long regimes need damped divisor-in-progression inputs
  (ElT Prop 1.4-type for Case A). Not written.
* Short cofactors `n < P̄^{1/2}` with several primes (Remark 4.2).
* The (DCC) assembly (LS6 §6.1 overlap combinatorics). Also whether the c-averaged
  form of (RD′) suffices there.
* The exponent 1/12 is lossy. Numerics (EVIDENCE) suggest the truth is `p^{−1/4}`,
  attained by the least-height label just above the cut.

## Labels used
PROVED (Lemmas 1.1, 1.2, 2.2, Props 4.1, 5.1, Cor 6.1); PROVED given Shiu's theorem
(Lemma 2.1, Thms 3.1, 4.3); Assessment (Remark 4.2, §5 (a,D)/Case A, §6 DCC
sufficiency); EVIDENCE (§7).

## Replay
See the `## Replay` section of LS7 (three scripts, all < 40 min under `ulimit -v 8000000`).
