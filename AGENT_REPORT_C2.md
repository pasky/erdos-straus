# AGENT_REPORT_C2: superlinear Ω-result for W(p) (PROVED modulo TZ Cor. 1.4) (checkpoint 1)

Branch `side-agent/pointwise-omega`. All work is in this worktree; nothing
has been merged. The deliverable is `POINTWISE_OMEGA.md`.

## Outcome

**Theorem 5.1.** For infinitely many Mordell-hard primes,
`W(p) ≥ (log p)^2·exp(−C log log p/log log log p)`. In particular:

* `W(p) > (log p)^{2−ε}` i.o. for every ε;
* `W(p)/log p → ∞` along a sequence;
* for every large T, `log L_h(T) ≤ T^{1/2+o(1)}`.

**Status: PROVED modulo one cited source (TZ Cor. 1.4 together with the McCurley-region statement quoted on TZ p. 1; review D1); effective.** The cited theorem is
Thorner–Zaman, Math. Z. 306 (2024), Cor. 1.4 (arXiv:2108.10878v2). Its
statement was read in the archived PDF/text under `sources/lit2026/`.

* Siegel zeros are handled; there is no caveat.
* Chang's theorem is not used.
* The previous record was `(5/8−ε) log p` (POINTWISE_SIZE Thm 11.2).
* This refutes `H_MOD(A)` (notes (51.19)) for every `A<2`. Before, only
  `A<1` was refuted.

## The proof

1. **Prime-local reduction (Lemma 2.1).** Impose the class of one modulo all
   prime powers `≤T` of primes `≤y`, with `y=T^{1/2+o(1)}≥√T`. Every
   surviving modulus `M≤T` then has exactly one free prime ℓ. The residual
   system is "`n mod ℓ ∉ F_ℓ`", with
   `F_ℓ={−4D mod ℓ : D|A_{mℓ}², m | 4D+1}`.
2. **The new input (Lemma 2.3, PROVED).** The sieve mass satisfies
   `S=Σ|F_ℓ|/(ℓ−1) ≤ T^{o(1)}`.
   * Write `D=sr²`, `A=srk`. The congruences force `m | r+k`, and this saves
     the factor m.
   * The crude bound underlying POINTWISE_SIZE Lemma 11.7 is
     `S≤T^{1/2−η+o(1)}`. That was exactly the bottleneck of Assessment 11.6,
     which therefore stopped at a linear range.
   * Numerically `S≈0.054(log T)^{2.5}` for T up to `10^6`.
3. **Brun pure-sieve minorant.** The minorant is a Bonferroni truncation of
   degree `J≍S`. Its moduli are `Q·d` with `log ≤ 3y`. Its ℓ¹-mass is `e^S`
   and its mean is `≥ e^{−2S}`.
4. **Transfer (Theorem 4.1, a general criterion).** This uses Thorner–Zaman
   Cor. 1.4, a Linnik-range PNT with relative error that is scaled by the
   exceptional factor λ, i.e. with Deuring–Heilbronn built in.
   * Lemma 3.2 shows that at most one "severe" real character exists across
     the whole family of moduli, via McCurley's region applied to lcm's of
     two moduli.
   * Case A: its conductor divides Q. Then λ is common to all terms and
     cancels.
   * Case B: otherwise. Then a twisted mean appears, and it is small.
   * Result: `log p ≪ log Z·S ≈ y·T^{o(1)} = T^{1/2+o(1)}`.

Note on the brief's step (ii). PNT uniform only for `q≤exp(c√log x)` would
give back the linear range. The Linnik range `x≥q^{12}` is essential.

## Precise obstruction above exponent 2 (§6)

* **Prop 6.1 (PROVED).** Every prime-local class-of-one design has
  `log p ≥ (1/√3−o(1))√T`. So exponent 2 is the ceiling of this method.
* **Hypothesis H_MIN(θ).** A pointwise congruence minorant for the
  non-prime-local residual system, with:
  * modulus budget `T^{θ+o(1)}`;
  * `log(mass/mean) ≤ T^{o(1)}`;
  * a twist condition.

  This is a purely combinatorial CRT statement in which primes do not enter.
  **Theorem 6.2 (PROVED modulo Thm 3.1):** H_MIN(θ) implies `W > (log p)^{1/θ−ε}`. A
  polylogarithmic H_MIN gives `W > exp(c(log p)^{1/(2A)})`. So the
  correlation wall (iv) is the only remaining gap: (ii) and (iii) are solved
  by Theorem 4.1.
* **Prop 6.3 (PROVED, raw atom list).** Event-level Bonferroni fails for
  `θ<1/2` at degrees `4.2θ²(log T)² ≲ J ≤ T^θ`. The cause is hub classes
  (`−4`, `−4d²`, …), on which `K_{r,r}` many two-prime atoms fire together.
  * EVIDENCE: after deleting atoms implied by single-prime atoms, 51–65% of
    the multi-prime atoms remain. Hub classes `−16, −36, −12` keep about 300
    irredundant edges each at `T=10^5`.
  * That the deduplicated hub graphs contain `K_{r,r}` asymptotically is
    **not** shown.

## Self-review

A reviewer subagent ran a deep, hostile review. Its findings:

* The exponent-2 argument survives. It checked the citation lines and
  Lemmas 2.1, 2.3 and 3.2, Theorem 4.1, and the Bonferroni sign.
* Six defects were found in §§0, 5 and 6. All six are repaired, in commit
  "self-review repairs":
  * Prop 6.3 was false without an upper bound on J;
  * Theorem 6.2's polylogarithmic exponent should be `1/(2A)`;
  * a twist constant was off (0.7 → 0.69);
  * a sign `(−1)^r` was missing;
  * distinctness of the primes now uses `p>Q`;
  * the headline transfer bound needed its `K·max(log Z,K)` form.
* The scripts now exit nonzero on failure. Atoms with a prime-power free
  part are now separated from genuinely multi-prime atoms.

## Things the parent should check hardest

1. The citation: Thorner–Zaman Cor. 1.4 together with Remark 1.5 and the
   McCurley quotation, in `sources/lit2026/arxiv-2108.10878-thorner-zaman-pntap.txt`
   lines 37–39 and 121–131. In particular, check that the O-term is relative
   to `λx/φ(q)`, with absolute constants.
2. Lemma 3.2 (uniqueness of the severe character across a family) and the
   Case A/B split in Theorem 4.1.
3. Lemma 2.3, especially the involution and the identity `m | r+k`.
   `pointwise_omega_check.py lemma` checks the algebra. Lemma 2.1 is checked
   by `local`, with 0 mismatches.

## Suggested ledger entries (for the parent to place)

* **(H)-new.** Theorem 5.1: `W(p) ≥ (log p)^{2−o(1)}` i.o. and
  `log L_h(T) ≤ T^{1/2+o(1)}`. Label: PROVED modulo Thorner–Zaman Cor. 1.4;
  effective.
* **(H)-new.** Lemma 2.3: the prime-local mass is `T^{o(1)}`. Label: PROVED.
* **(H)-new.** Theorem 4.1, the transfer criterion. Label: PROVED modulo the
  citation.
* **(D)-new.** Prop 6.1: the prime-local ceiling is exponent 2. Label:
  PROVED.
* **(E)-new.** H_MIN(θ) is the exact sufficient input above exponent 2
  (Theorem 6.2). Label: PROVED implication; the hypothesis is open.
* **(F).** `H_MOD(A)` is refuted for `A<2` (PROVED modulo TZ Cor. 1.4 with the McCurley statement; no GRH, no Siegel caveat). This updates notes Cor. 54.2.

## Possible next steps (awaiting parent decision)

* **(a) Haar polylog bound.** `δ*(T) ≥ exp(−(log T)^{O(1)})` via the local
  lemma with a polylogarithmic class-of-one quarantine. This is step (i) of
  the brief and the open input of POINTWISE_SIZE §7.3(i). It needs a
  per-prime version of Lemma 2.3, namely
  `w_ℓ := Σ_{atoms ∋ ℓ} P(atom) ≤ (log T)^C/ℓ` uniformly in ℓ. That looks
  feasible but technical. It would be a Haar-level result only, so it would
  make the RA-heuristic input rigorous but would not prove anything about
  primes.
* **(b) Attack on H_MIN(θ), θ<1/2.** This needs a hub-adapted hypergraph
  minorant. It is a genuine research problem.
* **(c) Type-I frame (`ck_min`, Thm 11.2′).** An analogous prime-local
  analysis might give `(log p)^{2−o(1)}` there as well. Not attempted.

Replay: see `POINTWISE_OMEGA.md` § Replay. All scripts run in under 30
minutes at a 12 GB limit.

---

# Checkpoint 2 (tasks (c) then (a)); §§1–6 unchanged

New material is in `POINTWISE_OMEGA.md` §8 (Type I), §9 (Haar), and §0 item 5. A
deep self-review was run; no fatal gap was found and all of its findings are
repaired (last commit).

## (c) Type-I frame (`ck_min`), §8

**Answer: no `(log p)^{2−o(1)}` for `ck_min` by congruence methods, and there
is a precise reason.**

| Result | Status |
|---|---|
| Lemma 8.1. For p ≡ 1 (24), `ck_min(p) ≥ n_p`, the least quadratic non-residue. Genus forcing, notes Thm 48.1. | PROVED |
| Cor 8.2 (joint). Infinitely many hard p with `W ≥ (log p)^{2−o(1)}` **and** `ck_min ≥ (log p)^{1−o(1)}`. Uses Theorem 5.1's primes, which are QR mod all ℓ ≤ y. | PROVED modulo TZ |
| Prop 8.3. A complete Type-I certificate (class a mod L) forces `ℓ \| L` **and** `(a/ℓ)=1` for every prime 5 ≤ ℓ ≤ T. This sharpens notes Thm 56.2. | PROVED |
| Cor 8.4. Any fixed-period congruence minorant for `ck_min > T` (the analogue of Thm 4.1) can only fire at primes with `n_p > T`. So the congruence-certifiable Type-I depth is exactly `n_p`. | PROVED |
| Thm 8.5 (new). `ck_min(p) ≫ log p · log log log p` i.o. This is the first superlinear Type-I result, beating Thm 11.2′'s 5/12. Lau–Wu Prop 5.1 supplies primes ≡ 1 (4) that are QRs mod every q ≤ δ log x log₃ x; the self-review found it in the archived source. Effectivity not claimed. | PROVED modulo Lau–Wu Prop 5.1 (archived author PDF; their proof follows Graham–Ringrose, and we did not check it) |

The obstruction:
- Proving `ck_min > (log p)^{1+δ}` i.o. by congruences would beat every known Ω-result for the least non-residue, both unconditional (`log p·log₃ p`) and under GRH (`log p·log₂ p`).
- It would also exceed the random-model maximum `log p·log log p` (Assessment).
- Under GRH, Ankeny's bound caps the congruence route at `O((log p)²)`.
- Beyond `n_p`, slice vanishing is a factorisation event (no divisor in the target grade). That puts it behind the slice dimension barrier (Assessment).

EVIDENCE: `ck_min ≥ n_p` holds for all 385 primes p ≡ 1 (24) below 30000, with equality for 238 of them. The engine reproduces the notes (48.12) records.

## (a) Haar side, §9 (Haar only; nothing about primes)

| Result | Status |
|---|---|
| Lemma 9.1 (structural). Every surviving atom M = m·r with m \| 4D+1 has `m ≤ r²+1`. There is an exact `(s,r',v)` parametrisation of single-prime atoms, so `F_ℓ^{full}` is independent of T. | PROVED |
| Lemma 9.2. After any class-of-one quarantine, the global surviving mass is `≪ (log T)^4 log log T`, uniformly in z. | PROVED modulo Elsholtz–Tao Prop 1.4 (archived; `T^{o(1)}` without it) |
| **Theorem 9.3 (new, unconditional): `log(1/δ*(T)) ≤ T^{1/3+o(1)}`.** Improves POINTWISE_SIZE Lemma 11.7 (`T^{1/2+o(1)}`). Construction: quarantine at T^{1/3+ε}; the T^{o(1)} bad primes (g > 1/4, counted via Lemma 9.2) are quarantined too; single-coordinate events handled exactly; pair events by the local lemma under the conditioned product measure. | PROVED |
| Theorem 9.4. Under the per-prime Hypothesis H_PP(z) (`w_ℓ ≤ log z/(8 log T)` for all primes ℓ > z), δ*(T) ≥ exp(−π(z) log T − O((log T)^4 log log T)). With z = (log T)^C this is the polylog bound of step (i). | PROVED implication, modulo Elsholtz–Tao Prop 1.4 for the polylog mass; H_PP open |

H_PP is open. The exact gap is a congruence saving at **fixed** ℓ: it needs equidistribution of `(4sr')^{-1} mod ℓ` against divisor weights, which is Kloosterman/Henriot-type, as in notes Thm 31.3.
- The uniform form `ℓ·w_ℓ ≤ (log T)^C` is false. Linnik primes ℓ ≡ −1 (mod 4P) have `|𝓡(ℓ)| ≥ (3^K−1)/2`.
- EVIDENCE:
  - `|F_ℓ^{full}| ≈ (log ℓ)^{2+}` for 10² < ℓ < 4·10⁴.
  - The multi-prime per-prime mass is small: `max ℓ·w^{multi}_ℓ = 0.68` at T = 10⁵, z = 300.
  - The full H_PP ratio drops below 1 only at z ≈ T^{0.6} for accessible T, so the polylog regime is not tested numerically.

What this means (Assessment):
- Under RA, Theorem 9.3 predicts `W > (log p)^{3−ε}`.
- On the prime side, the same construction is exactly H_MIN(1/3), which would give exponent 3. Event-level Bonferroni on the raw atom list is blocked (Prop 6.3). H_MIN(1/3) itself is open.

## Files

- `POINTWISE_OMEGA.md` §§0, 7 (Type-I pointer), 8 and 9, and Replay.
- `scripts/pointwise_omega_check.py`: new `typeI` command.
- `scripts/pointwise_omega_haar.py`: new script; includes `F_full`.
- `data/pointwise_omega/{Ffull,haar_1e5,haar_1e6}.txt`.
- `sources/lit2026/lau-wu-least-quadratic-nonresidue.{pdf,txt}`, plus README.

Stopping for parent review. I have received no forwarded repairs for §§1–6 yet.

---

# Round 2 review repairs (§§8–9)

The reviewer's round 2 (`reviews/pointwise-omega-review.md`, "Round 2") is
SOUND-AFTER-REPAIRS; all items are mathematically sound. Repairs applied:

* **R2-1.** Theorem 9.4 and §0 now carry the label "modulo Elsholtz–Tao Prop 1.4 for the polylog mass". The table above is updated too.
* **R2-2.** H_MIN(1/3) is now described as open, not "blocked".
* **R2-3.** Cor 8.4 has a scope note: the proof uses only a≡1 (24).
* **R2-4.** The premise in Lemma 9.2's weight bound is dropped.
* **R2-5.** Lau–Wu bibliographic data added: Int. J. Number Theory 4 (2008), no. 3, 423–435, doi:10.1142/S1793042108001432.
* **R2-6 (= D5 residue).** The report title no longer says "unconditional".
* **R2-7.** New finite-T remark after Theorem 9.4.
  * Theorem 9.3 has no numerical instance.
  * H_PP holds literally at (10⁵, 10³) and (10⁶, 3·10³), so Theorem 9.4 gives rigorous finite-T Haar bounds there. These are labelled EVIDENCE-level certificates.

Ready for merge. Ledger and STATUS updates are left to the parent.
