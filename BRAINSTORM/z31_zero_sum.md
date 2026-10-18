# z31 — Additive combinatorics: zero-sum theory, Davenport constants, subset products, Kneser (O261 field memo 9)

Labels as in DISCOVERIES.md. Agent E could not verify ACFKP's D_±(ℤ/n) = ⌊log₂n⌋ + 1, Erdős–Rényi's threshold or the AGP
group lemma in primary sources (`acfkp.txt`, `erdos_renyi.txt`, `agp.txt` record this) — all three are (memory) here.
Builds on BRAINSTORM/s6_divisor_pigeonhole.md (O238: pigeonhole criterion + Cauchy–Davenport sharpness, PROVED),
FORCED_WINDOW §4 (Erdős–Rényi random model), DETERMINISTIC_EXISTENCE row 14, CAP_POINTWISE Thm 1.1.

## (a) Counterpart (exact)
E3 at a window q (prime, q ≡ 3 (4)): with K = (p + q)/4 = ∏ s^{e_s},
  −1 ∈ Rat_q(K) ⟺ −1 ∈ B_q(K) := ∏_{s | K} {s^j : |j| ≤ e_s} ⊂ (ℤ/q)^*   (product set of symmetric "boxes").
(PROVED: u/v with uv | K coprime is ∏ s^{j_s} with |j_s| ≤ e_s; conversely such a product splits into coprime u, v.)
So B2-at-a-window is a **target problem for a ±-weighted subset-product (box) set in a cyclic group** — target −1, not 0.

## (b) What zero-sum / sumset theory proves
* ±-weighted Davenport (memory: ACFKP 2006): a sequence of length ≥ ⌊log₂ n⌋ + 1 in ℤ/n has a non-trivial ±-weighted
  zero-sum. Gives target **+1** (q | u − v), never −1 (s6 memo).
* Kneser / Cauchy–Davenport: |B| grows only linearly in Σ e_s in the worst case (all s in one cyclic progression); s6 Prop:
  the structure-free criterion needs Ω(K) ≳ q/4 (PROVED sharp there).
* Set version (memory: Olson; Szemerédi–Vu): a set of ≥ C√q distinct residues not in a coset of a proper subgroup has
  subset products covering the group — would give −1 with v = 1 once ω(K) ≥ C√q and the primes of K are "spread".
* Random version (memory: Erdős–Rényi 1965): r ≥ log₂|G| + log₂log₂|G| + ω(1) random elements give all subset products
  a.s.; this is the campaign's heuristic model (FORCED_WINDOW §4), not a theorem about K.
* Subgroup membership is FORCED: −1 ∈ ⟨primes of K⟩ by reciprocity at every admissible window (CAP_POINTWISE Thm 1.1, the
  (J)64 cap theorem). Zero-sum theory is precisely the theory of getting from the subgroup ⟨S⟩ to the box B — and it needs
  length ≳ log₂ q (random/dissociated), ≳ √q (spread sets), ≳ q (worst case).
* AGP (Carmichael numbers, Ann. Math. 1994; memory): uses a Davenport-constant bound to find a subset product ≡ 1 among
  primes *chosen by the prover* (many primes ℓ with ℓ − 1 smooth).

## (c) Transfer
Blocked by F2 in its sharpest form: Ω(K) ≈ log log p for typical K and ≤ log₂ p always, while the window q must be ≥ the
least admissible window (prime ≡ 3 (4), ≡ 4 − p (8), non-residue mod p), which is ≫ log p · log₃ p for infinitely many p
(Graham–Ringrose, unconditional; POINTWISE_OMEGA §8). Even the random threshold log₂ q ≈ log log p is met by K only with
probability bounded away from 1 — the lottery. The prover cannot choose K (contrast AGP): F1. The target is −1 not +1: the
"+1 vs −1" bit is the quadratic character (F6), which zero-sum theory treats as a coset choice and cannot force.

## (d) Verdict: EQUIVALENT reformulation at a fixed window (B2 = target −1 in a box product set), but the relevant theorems
(Davenport/Olson/Kneser/Erdős–Rényi) need lengths that a forced K never has: **NOT SHARP.** (Not new: s6 memo O238 already
proved the linear-sharpness; this memo adds the box-set formulation and the length ladder log q / √q / q.)
