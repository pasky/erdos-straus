# AGENT_REPORT_O274 — sustained open attack on the single-integer lower tail (model FABLE)

Branch `side-agent/lower-tail-fable`, worktree 0039. Main file `LOWER_TAIL_FABLE.md`; scripts
`scripts/z43_fable_{forms,canon,hj,graph}.py`. Checkpoint 1 (first natural stopping point).

## SHARP

* *(R286 repair: SHARP 1's "why ES^□ had to be provable" is withdrawn — ES^□ is proved by an infinite modulus-4 shot
  family, not by this count — and the k-th-power ladder holds only for prime k (k = 4 borderline, k ≥ 6 composite above the
  line). SHARP 3's equivalences are with ES₅ (five-slice ES); only "pair ⟹ ES(p)" is proved. (2.5) and the CM claim were
  false and are repaired. See reviews/lower-tail-fable-review.md.)*
* **SHARP 1 (framing, Assessment — not a theorem).** The *index calibration* of §3.2: pooling cells mu | U
  at a fixed modulus 4U gives τ₃(U)·log p divisor-tries. A target coset −H ⊂ (ℤ/4U)^× can be hit by
  counting only if [G : H] ≲ τ₃(U). For H = squares, [G:H] = 2^{ω(U)+O(1)} ≪ τ₃(U) — and that relaxation
  (ES^□, (J)28) is a theorem. For ES the target {−1, −p} has H = 1, [G:H] = |G| ≫ τ₃(U). This is a
  one-line quantitative reason why the square relaxation *had* to be provable and ES is not reachable by any
  pooled counting, and it defines a ladder (H = k-th powers) whose provable rung is exactly k = 2.
* **SHARP 2 (PROVED, elementary; mostly a re-indexing).** Canonical two-target form: for p ≡ 1 (4),
  ES(p) ⟺ ∃ m, u ≥ 1 such that mp + u has a divisor ≡ −1 (mod 4mu) [Type II] or ≡ −p (mod 4mu) [Type I].
  Same integer, same modulus, two targets. Lemma 2.7: the forced non-residue sits on the divisor d for
  Type II ((p/d) = −1) but on the *level* w = (d+p)/(4mu) for Type I (d itself can be a residue:
  p = 13, (m,u,d) = (2,1,3)). Checked on 9 959 certificates.
* **SHARP 3 (PROVED relative to DEDEKIND_ES Thm 4.5; odd branches re-proved).** Legendre form:
  ES(p) ⟺ ∃ r ≥ 1 and A | p + r with A ≡ −1 (mod r) and (A/p) = −1; the "4" of ES is absorbed into the
  Legendre symbol, and for odd (A, r) the sign is exactly "A ≡ 3 (4) or r ≡ 3 (4)". Symmetrised: ES(p) ⟺
  the coprime mutual-shift graph G_p (edge t—e iff te | p + t + e, colour (e/p)) has a bichromatic edge;
  the vertex condition is sign-free, T1 is entirely in the colouring. Census to 3000: G_p is usually
  disconnected (sporadic 2/3-cliques), comp(1) has ≍ log² p vertices and a QNR vertex in 209/211 cases.

## What was done

1. Re-derived from scratch the complete certificate structure at a prime (both types), verified against brute
   force (`z43_fable_forms.py`, `z43_fable_canon.py` with explicit unit-fraction reconstruction, 0 mismatches
   to 400), and recorded six equivalent symmetric forms (§2): reciprocal divisibility "K | p + e, e | p + uK",
   the one-line "Ke | uK + αe + β", the W − □ form, the square-root-of-minus-cofactor form.
2. Mechanism audit (§3), construction-first, each attempt pushed to the point where a barrier hypothesis is
   met and the evading modification named: Thue/lattice (size is free, sign is T1, divisibility is the
   lottery), fixed-modulus pooling (index calibration), p's canonical data (a² + b² / CM group orders are
   killed by "every certificate divisor is ≡ 3 mod 4"; Pell convergents; ord_p; non-CM #E(𝔽_p)),
   non-abelian Frobenius (the second condition is a factorisation, not a Chebotarev class), involutions
   (the only visible one is free; f_II even), descent (multilinear equation, no Vieta), identities (B1).
3. Legendre/HJ form and mutual-shift graph (§2.8–2.9) with a census.

## Outcome

No new mechanism; ES is not solved and no case of it is claimed. The audit confirms the campaign's map from
an independent derivation: every construction ends at a tied-modulus divisor event at a single integer, or at
a pooled count τ₃(U) log p ≪ |(ℤ/4U)^×|. Precise statements and labels are in LOWER_TAIL_FABLE.md §4.

## Checks for the parent

* The even branches of the Legendre form (r ≡ 0, 2 mod 4) are taken from DEDEKIND_ES Thm 4.5 / Cor 4.6; I
  re-proved only the two odd branches with explicit solutions. The numerical check (`z43_fable_hj.py`,
  211 primes, r ≤ 400) only shows the form always *finds* a certificate and that the 2-adic reading of the sign
  is exact on odd pairs; it cannot falsify sufficiency of the even branches.
* Lemma 2.7's Type I proof sketch is terse; the statement is numerically verified (all certificates with
  m, u < 25, p < 3000), including even levels via the Kronecker symbol.

## Sparks

See LOWER_TAIL_FABLE.md §5: (1) is ES_{Q³} a one-prime theorem or a lottery (calibrates the ladder);
(2) unconditional lower bound on |comp(1)| in G_p; (3) a mediant/edge-to-edge move in G_p; (4) census of
minimal Type I level versus ℓ(p).
