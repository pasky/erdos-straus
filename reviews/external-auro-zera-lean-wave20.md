# External review: "auro-zera" Lean formalization of Erdős–Straus (wave 20)

**Artifact:** `sources/auro-zera/auro-zera-proof.lean` (1212 lines, Lean 4 +
Mathlib), fetched 2026-08-29/30 from
github.com/Suro-One/auro-zera_Erdos-Straus_proof.
**Companion citation audited:** Dyachenko, arXiv:2511.07465
(`sources/dyachenko-2511.07465.pdf`).
**Reviewer protocol:** full read of the Lean source; exact-rational replay of
every explicit witness and one instantiation of each identity family;
mod-840 class arithmetic replayed; the load-bearing external citation pulled
and its Conclusion read. The file was NOT compiled (no local Mathlib
toolchain; compilation status is therefore **unverified**, though the
tactic-level structure is plausible).

## Verdict

**This is not a proof of the Erdős–Straus conjecture.** It is a clean
formalization of the classical identity/case-split layer plus **one axiom
(`good_divisor_exists`) that is exactly the open content of the conjecture**,
invoked for precisely the residue classes (squares of units mod 840) where
the conjecture has always been open. The top-level theorem
`ErdosStraus_conjecture` is proved *from that axiom*; naming it "the
conjecture" and titling the repo a proof is an overclaim by the campaign's
register. The file's own comments are more honest than its header.

## What checks out (replayed here)

1. **Explicit witnesses are correct.** 4/2521 = 1/636 + 1/69748 + 1/131876031
   and 4/66529 = 1/16637 + 1/58254900 + 1/507708871715100 (exact rationals).
2. **The identity families are sound algebra.** The ED2 skeleton
   (A·δ = b·c, 4bc = b + c + Pδ ⇒ 4/P = 1/A + 1/(bP) + 1/(cP)) and the
   constructor ((4αsr−1) | (4αs²+P) ⇒ ES(P)) replay exactly (checked at
   (P,α,r,s) = (73,1,2,1)). The divisor-pair bridge (u,v | p·(p+r)/4,
   r | u+v ⇒ ES p) is the classical two-unit-fraction criterion.
3. **The mod-840 case split is complete.** Squares of units mod 840 are
   exactly {1,121,169,289,361,529} (replayed), all ≡ 1 (mod 24); the 23
   non-hard residues ≡ 1 (mod 24) are covered by the five ED2
   specializations (spot-checked 73+4 = 7·11).
4. The "rigidity cascade" contrapositives (exceptional P ⇒ P+4 is a sum of
   two squares, etc.) are correct consequences of the families.

## The two failure points

1. **The axiom is the conjecture.** `good_divisor_exists` asserts a witness
   pair for every "rigid" hard prime — i.e. for exactly the primes on which
   every fixed and semi-adaptive family fails. Rigidity is a Π-statement
   (quantified over ALL levels of three infinite families), so the file's
   empirical note "the axiom has no known instance" cannot be certified for
   any individual prime by finite search; the axiom's domain is precisely
   the set nobody can exhibit members of NOR prove empty. Assuming a witness
   there assumes Erdős–Straus for the hard core. (The file admits this in
   §6/§12 comments: "the one remaining sorry-equivalent".)
2. **The external justification is misquoted.** The header and §6 claim
   "Dyachenko 2025 (arXiv:2511.07465) proves (W) unconditionally with
   r = O(log p)". Dyachenko's own Conclusion (p. ~end, replayed verbatim
   from the PDF) states: *"The general case: namely, when P runs over
   infinite sets, is certainly not proven constructively in the present
   work; the sections of Appendix D that use Dirichlet's theorem and finite
   coverings are conditional in nature."* The Lean file's §5b comment even
   concedes this ("the infinite case is conditional") — directly
   contradicting its own header. The arXiv abstract's "central result states
   that for every prime P ≡ 1 (mod 4) there exists a representation"
   overstates the paper's own conclusion. (The paper also credits "various
   AI models" for assistance.) So the chain is: theorem ← axiom ← citation
   whose source disclaims the needed statement.

## Reconciliation with the campaign (notes.md §1–§55)

The file's *structure* reproduces, in Lean, several objects this campaign
has mapped at theorem level — and nothing in it contradicts any campaign
result; on the contrary:

- Their **hard residues** {squares of units mod 840} = the campaign's hard
  progression territory (§19 conventions; all ≡ 1 mod 24).
- Their **`hshift`/`hed1`/`huk` cascade layers** are fixed and
  shift-parametrized divisor families — the kind walled by the campaign's
  escape theorems (§17.3 residue-one escape, Theorem 48.5): no bounded
  system of them can cover the hard classes, which is exactly why their
  case split needs the axiom for the residue.
- Their **Schinzel-vs-divisor-adaptive observation** (§5c comments) matches
  the campaign's frontier framing (§50): adaptive divisor existence per p is
  the open atom; standard technology audits (Bateman–Horn per-p, GRH
  compositum, EH) fail exactly there.
- Their **axiom (W)** is the unbounded-modulus cousin of the campaign's
  falsifiable hypotheses H_MOD(A)/H_SPF(A) (§50.7, §51). The campaign's
  quantified versions are strictly more informative: (i) §51/§53 prove the
  hypotheses hold outside explicitly small exceptional sets (the almost-all
  layer their file lacks entirely); (ii) **§54 (this wave) proves their
  hoped-for uniform bound shape is partly impossible**: witness moduli
  ≥ c·log p occur infinitely often (Linnik-effective), so any true
  witness-modulus bound is at least logarithmic — consistent with their own
  measured statistic r ≤ 0.457·log²p (their data suggests the truth for
  their r-statistic is ≈ log², squarely in the H_MOD(A), A ∈ [1,2] window,
  which §54 leaves open and §51 bounds almost-everywhere).
- Their **rigid primes** = the campaign's conspiracy set (§44/§48 census
  primes are concrete near-instances: 2521 — their one sporadic — is the
  campaign's depth-111 conspiracy prime).
- Their `not_ES_sum_two_squares` (exceptional P ⇒ P+4 a sum of two squares)
  is the mod-4 shadow of the campaign's square-class phenomenon (§21:
  every perfect square avoids the complete intrinsic system; Prop 8.1).

**Bottom line:** the Lean file is a competent formalization of the
*unconditionally easy* 5/6-plus-identities layer, a correct formal
isolation of the hard core as one axiom — and an overclaimed title. Its
axiom sits exactly on the campaign's mapped frontier; the campaign's §51–§54
results quantify (almost-all + two-sided + effective) what the file can only
assume. No campaign statement needs revision in light of it. The Dyachenko
paper is worth keeping archived as a source of the ED2 identity family
(cousin of the campaign's §4/§16 supply), not as an existence theorem.

**Labels:** everything above marked "replayed" is Computational (exact);
the compilation status of the Lean file is Unverified; the characterization
of Dyachenko's results rests on his own quoted Conclusion (verbatim
extract).
