# AGENT REPORT O25 — hybrid methods (branch `side-agent/interfreq-hybrid`)

Deliverable: `EXCEPTIONAL_INTERFREQ2.md` (checkpoint 1), scripts
`scripts/interfreq2_*.py`, data `data/interfreq2/`.

## Outcome in one paragraph

The IF Rem 2.6 hybrid gap is **not closed unconditionally**, but it is
reformulated exactly and narrowed to two precise residues. A hybrid bound
equals the *exact* count of ν on [1,N] plus a penalty |a| for every large
term used with the "wrong sign" (Lemma 3.1). Positive terms on classes that
meet [1,N] maximally and negative terms on classes that meet it minimally are
free, and combinations of them can count some large classes exactly
(Example 3.2: `1[0 mod 21]` at N = 20 has charge 0). So no inequality
`B_hyb ≥ c·N·Eν` holds, and IF Thm 2.5's Selberg accounting cannot be
extended verbatim; the obstruction is the ends of [1,N], where Selberg's
minorant vanishes, and moduli just above N. Theorem 5.2 proves the 3/4 cap
(with K2's log log loss) for every hybrid whose right-signed mass at moduli
in (N/2, CN] is O(e^{O(S)}·B), *conditional on* a purely analytic, 𝒜-free
hypothesis Flat (a spread-spectrum "flat" minorant of 1_{[1,N]}). Flat is
found by LP at sampled N ≤ 100 (C = 1.5, 2; finite support) and is infeasible for C = 1 at N = 20.

## Items and labels

1. Def 1.2 (hybrid with least position-blind charge β*), Prop 2.1 (LP dual,
   weak duality per common modulus Q′; no projection, since fibre averaging
   does not preserve interval counts). PROVED.
2. Lemma 3.1 sign rule; Example 3.2 (identity checked by script). PROVED.
3. Lemma 4.1 / Lemma 6.1: every twisted window φ([1,N]) (componentwise
   affine, small-profile preserving) is dual feasible, so
   `B_hyb(ν) ≥ Σ_{n∈φ([1,N])} ν(n)`. PROVED. That averaging over them cannot
   give a cap is only an Assessment (full group G_N not determined).
4. Lemma 4.2: a class on which every dual μ vanishes has
   gcd(d, lcm(1..N/2)) > N; sampled numerics: such e | L₀ occur just above N.
   PROVED / EVIDENCE.
5. Cor 5.1: cap when free mass ≤ c·B (direct from IF Thm 2.5 + sign rule +
   dropping free negatives, Lemma 5.0). PROVED.
6. Thm 5.2: conditional cap under Flat; patches above CN, wrong-signed and
   free negative terms unrestricted; margin s₀ only needs to be ≥ N^{−O(1)}.
   PROVED implication.
7. Flat numerics (s₀, Δ table; support-size effect; C = 1 infeasible;
   medium moduli cannot be freed — margin forced to ≤ 0). EVIDENCE.
8. Toy hybrid LPs on ℤ/30030: H* ≈ 0.6–0.9 × the IF Thm 2.5 functional; the
   optimum sits in Cor 5.1's regime. EVIDENCE (tiny).
9. (H_eq): not relevant to hybrids (no per-frequency evaluation). Not
   attacked further.

## What I could not do

* Prove Flat. Selberg's minorant fails (F3) near the ends of [1,N] for every
  C; L₀-translates and twisted windows cannot move mass between classes of
  N/4-smooth modulus, so a proof needs a genuinely fractional spread
  pseudo-window. Margins decrease slowly with N (partly truncation:
  0.326 → 0.372 at N = 60 when the support grows from 11N to 17N).
* Medium moduli (N/2, CN]. Neither a cap nor a beating hybrid.

## Follow-up (checkpoint 2): Flat and medium moduli

* **Prop 9.1 (PROVED):** Flat follows from a cleaner hypothesis SPW
  ("spread pseudo-window": R ≥ 0 with the exact small-class profile of
  [1,N] and mass ≤ 1 − σ on every class of modulus > CN), by mixing
  Selberg's minorant with `1_{[1,N]} − R`; constants t, s₀ ≍ σ, so
  SPW ⇒ the 3/4 cap of Thm 5.2. Lemma 9.2: SPW ⇒ the patch-cancellation
  inequality (9.1) for all ν ≥ 0.
* **SPW not proved.** Proved partial construction: big primes
  (> √(N/2)) can be re-randomised keeping the exact profile; the
  obstruction is classes whose modulus divides lcm(1..N/4) (translates and
  twists fix them; this is the edge problem in another guise). LP: SPW
  holds at N ≤ 60 with σ ≈ 0.34–0.40 (C = 2); Flat at N = 100 has
  s₀ = 0.32 on a long support. No structural reason for failure found.
* **Medium moduli (§10):** not closed (see checkpoint 3 below).

## Checkpoint 3: review R25 repairs

* **M1.** The `med` claim was a truncation artefact and is withdrawn. New
  `scripts/interfreq2_med_periodic.py` solves the periodic relaxation on
  ℤ/Q′. Every F on ℤ projects to a feasible point of it, and its Farkas
  certificates are periodic ν ≥ 0 on ℤ. Results:
  * C = 1.5, N = 20: the sign conditions on (N/2, N] force s₀ = 0
    (a genuine obstruction);
  * C = 2, N ≤ 20: no obstruction, and finite-support witnesses with
    s₀ = 1/3 exist at N = 20, 30, 40 (support ≥ [−10N, 11N]). Hence
    Thm 5.2′ (PROVED implication): under this stronger Flat, only
    right-signed mass on (N, CN] has to be bounded;
  * sign conditions on all of (N/2, CN] are infeasible at N = 20
    (rigid modulus 21).

  Lemma 9.2's "converse" is now stated for the periodic LP only. §5, §10
  and the summary are reworded.
* **m1.** Grouped (shift-blind, not term-blind) charges are declared out of
  scope in §1.
* **m2.** The §0 row for Thm 5.2 now states the per-N parameter requirements.
  Lemma 9.3 (σ ≤ σ_C(N), due to R25 C11) was added; it explains the LP
  plateaus and the C ≤ 1 impossibility.
* **m3.** The Vaaler bound is quoted precisely, with the caveat that the
  theorem numbering was not checked against the paper.
* **SPW proof.** Not attempted beyond an Assessment. The optimum sits at
  the local bound σ_C(N), so the natural target is SPW(2, 2/5 − ε, O(1)).
  It needs a measure that spreads each small class evenly over its lifts
  to moduli > 2N, consistently for all small moduli at once; I see no
  short proof.

## Self-review (reviewer subagent, deep) — repairs applied

Thm 5.2 large-mass branch redone with K = 1+Δ(1+c) (c unrestricted);
symmetry claim downgraded to Assessment (global reflection moves classes);
Flat's R-form stated exactly; "uncapped hybrids are exactly…" replaced by
"not covered by Cor 5.1" (large free mass alone is harmless); rigidity
wording (gcd condition, "some representation has charge 0"); hypotheses of
the comparison-measure obstruction made explicit; numerics qualified as
sampled / finite-support; toy H renamed H_{Q′}; assertions in checks.

## Hostile-review targets

* Prop 2.1 / Thm 5.2: the weak-duality bookkeeping, the sign cases in the
  proof of (5.1), and the mean-side reuse (high-level terms come only from
  d > CN; λ = O(log N) because T_{>CN} ≤ N^{A₁+2} or B ≥ N).
* Lemma 6.1: the claim that φ_d preserving `I_d` is exactly what is needed
  (c(·,d) = ⌊N/d⌋ + 1_{I_d}).
* Whether Flat as stated is what the LP certifies (finite support
  [−L, N+L]; classes with d > span meet the support once; LP tolerance).

## Suggested ledger text (D)23 (for the parent to edit)

**Hybrid methods (EXCEPTIONAL_INTERFREQ2.md).** A hybrid bound (exact small
part, position-blind charges above N/2) equals the exact interval count plus
a wrong-sign penalty (Lemma 3.1); it can count some classes of modulus N+1
exactly (Ex 3.2), so no `B ≥ cNEν` holds. PROVED: cap when the free large
mass is ≤ e^{O(S)}B (Cor 5.1); every twisted window bounds the hybrid from
below (Lemma 6.1). CONDITIONAL: cap `C(log N)^{3/4}(log log N)^{3/4}` for all
hybrids with bounded right-signed mass on (N/2, CN], under the analytic
hypothesis Flat (Thm 5.2), and Flat follows from the cleaner SPW (Prop 9.1, PROVED);
Flat/SPW checked by LP at sampled N ≤ 100 (EVIDENCE). Open: SPW (LP optimum = local bound σ_C(N)); right-signed
mass on (N, CN] (and on (N/2, N] unless the stronger Flat of Thm 5.2′ holds).

## Replay

See the Replay section of `EXCEPTIONAL_INTERFREQ2.md`. Heaviest step ~8 min,
< 1.2 GB, under `ulimit -v 8000000`.
