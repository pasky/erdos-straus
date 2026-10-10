# AGENT REPORT O127 — ES for large primes conditional on a standard conjecture

Branch `side-agent/conditional-es`. Deliverable: `CONDITIONAL_ES.md` (checkpoint 1); scripts
`scripts/cond_divisor_forms.py`, `cond_hard_I1.py`, `cond_slice_count.py`, `cond_dual_check.py`.

## Verdict
**No standard conjecture was found to imply ES; no conditional proof is claimed.** ES is not known
under GRH (LITERATURE_2026 has no such result). What was produced:

1. **Exact divisor form (PROVED, Lemma 1.1).** ES(p) holds if some `tp+1 = m·m''` with
   `m ≡ m'' ≡ −1 (mod t)` and `4 | m`. The cofactor congruence is automatic; this is ET's Type I
   at a = 1. Equivalent forms: `cf | p+c+f` (with a mod-4 condition); p is a value of `cfg − c − f`;
   and a dual "Kloosterman fraction" form. EVIDENCE: this slice alone solves all primes < 3000
   (dual form: < 20000) and all 4519 Mordell-hard primes < 2·10⁶, with t ≤ 367.
2. **Scale constraint (PROVED relative to ET Thm 1.1; Prop 2.3).** Take any hypothesis that
   gives `#target ≥ M/2` with a `p^{o(1)}`-to-one map to solutions. Then `M ≤ p^{o(1)}` outside a
   set of `O(N^{1−δ}log³N)` primes. Power-size main terms are therefore excluded, whatever the
   hypothesis is.
3. **Heegner/CM small scale (Cor 4.1, PROVED given 2).** The Humphries–Radziwiłł ranges were
   checked in arXiv:1910.01360v2: almost-all-centres down to expected count `|D|^δ`, and the GLH
   all-centre ranges. These cannot drive ES for families with `|D| ≥ p^κ`. Covering-type
   hypotheses escape item 2 only formally (Remark 4.2, a PROVED implication: if the small-scale
   asymptotic holds, ES targets are not balls).
4. **GRH (§3.2).** In the character expansion (3.2), each χ is used at one argument. Applying GRH
   character by character therefore gives only the trivial bound, which misses by `p^{1−o(1)}`.
   Chebotarev witnesses are polylog-size, and OMEGA13 kills those. Averaged prime laws are capped
   by PRIMELAW. Parts of this are Assessment, and are labelled as such.
5. **Ranked table (§5)** gives each listed hypothesis with its mechanism and gap. The contrast
   with Borwein–Choi (xy+yz+zx, where GRH works because the count is a class number) is the
   structural reason.
6. **Theorem 6.1:** X_slice ⇒ ES. X_slice is natural, but it is ES-strength (one Type I slice),
   **not** a standard conjecture.

## Weak points for the reviewer
* Prop 2.3 only constrains drivers that give lower bounds proportional to the main term. It
  says nothing about pure existence (covering) hypotheses, or about power-small relative
  errors on polylog weighted counts (Remark 2.4). The "negative result" is about mechanisms;
  it is not a non-implication theorem.
* §3.2's "Frobenius vs. ramification" and the claim that no admissible quadric exists (§4)
  are Assessments.
* Young's and Humphries's Heegner exponents are as cited by HR; I did not re-check them.
* Steps (2)–(3) of the brief were answered qualitatively plus with the Prop 2.3 bound. The
  Kuznetsov-side fixed-p computation for the SL₂ form was not carried out; O123 owns that
  route.

## Possible next steps (if the parent wants them)
(a) Look for a quadric or homogeneous-space encoding of ES with power-many points and a
fixed-modulus congruence (the one way around Remark 4.2). (b) Quantify the lower tail of S(p)
numerically, i.e. min S(p)/log²p over hard primes up to 10⁷, as EVIDENCE for X_slice.
(c) Formalise item 4 as a theorem about "single-coefficient" uses of L-function hypotheses.
