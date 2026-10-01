# Astra companion-credit verification

Read-only review of `paper/pointwise-obstruction.tex` and `../erdos-straus-astra`. I did not modify either repository. I copied the checker and its data to `/tmp/astra_copy` and ran it there under `ulimit -v 8000000` and `timeout 900`.

## Claim-by-claim findings

1. **159 forms and exact tuple — VERIFIED, with a counting clarification.** `PRIMARY_SEED_PACKET.md:32-38` identifies `primitive(6q+a)` for 84 `a` in A and `primitive(6(4h-1)q+h)` for 75 `h` in H, and says q is counted once and p is added. Exact normalization of the JSON A/H lists shows the sole overlap between the two families is q: it occurs at `a=0` (`6q`) and `h=0` (`-6q`). The explicit q is that same form; p is distinct. Thus the union has `84+75-1+1=159` forms. The H=1 row is `18q+1`, not p. The checker confirms exact set equality for `{q,p} ∪ A-forms ∪ H-forms` and 159 entries. The paper’s “with q counted once” is correct but could spell out that q is the A=0/H=0 overlap.

2. **Local admissibility, computable threshold, eventual sterility — VERIFIED as a conditional theorem in astra’s written proof, not certified by the finite checker alone.** `PRIMARY_SEED_PACKET.md:22-30` states computable N, conditional on all 159 primes, and explicitly says N has no numerical bound. `AFFINE_SEED_CLOSURE.md:243-255` explains one common finite threshold; `PRIMARY_SEED_PACKET.md:96-104` and checker output verify local admissibility conditions. The checker verifies the finite packet/skeleton; whole-component eventual closure additionally depends on the written boundary arguments in `AFFINE_SEED_CLOSURE.md` and `ONE_PRIME_FIBRES.md`. Paper accurately says it has not independently re-derived those arguments (`pointwise-obstruction.tex:1140-1145`).

3. **Subprogression witness and algebra — VERIFIED.** Paper `pointwise-obstruction.tex:1111-1117`; astra `PRIMARY_SEED_PACKET.md:112-123`. Independently computed with SymPy (`uv run --with sympy python`): the reciprocal-sum difference factors to exactly zero; `e=(4*7-1)*32-7=857`; the product `(6q+7)(762q+32)` is zero modulo 857 for q=713 (indeed factors are 4285 and 543338, both divisible by 857); all coordinates are positive for q=713 and remain positive for k≥0. The third coordinate is an integer. The chart point lies outside the seed component only under the sterile-component hypotheses, not unconditionally.

4. **Restricted tuple admissibility — VERIFIED.** `PRIMARY_SEED_PACKET.md:112-120` explains the residue and nonvanishing checks. The copied checker returned `positive_subprogression: q=Q+M*(507+857*k)` plus the local checks. Admissibility of the restricted tuple supports an application of Dickson; it does not assert simultaneous primality without Dickson.

5. **Earlier 800-form version — VERIFIED.** `SIGNED_SEED_COUNTEREXAMPLE.md:35-62` states the 800 forms, threshold `q>(Q+16)^393600`, and the full component conclusion. Lines 64 onward give the witness `a=10,h=33,e=1277` on `n=1248+1277k`; `AFFINE_SEED_CLOSURE.md:30-37` says 302 nodes. That older explicit threshold is **not** transferred to the 159-form theorem (`PRIMARY_SEED_PACKET.md:25-30`).

6. **Packet counts, status, hash, revision — VERIFIED, with important scope caveat.** `PRIMARY_SEED_PACKET.md:67-94` gives 159 nodes, 315,642 monomials, 287-digit modulus, 91 support primes. `sha256sum data/signed-seed-primary-packet.json` is `62a886126f4605c2f5b0c89e36a4154b36bf2ec1cfa10339161aef9a2ea0c2f2`. Running the copied checker returned `VERIFIED_PRIMARY_PACKET_EVENTUAL` and those counts, plus `simultaneous_primality_proved: false` and `explicit_threshold_proved: false`. Ast(a) documents the artifact’s own historical status `SKELETON_CLOSED_NOT_COMPONENT` (PRIMARY_SEED_PACKET.md:93-94; JSON line 2); the component result relies on later mathematics, not the checker alone. Commit `a036064` exists, timestamp 2026-10-01 11:06:04 +0200. The 159-form reduction itself is commit `43913c4` (10:58:54), and later astra commits updated related docs (`f7b38a3` at 12:50:27; `a79e6d5` at 12:55:09). I checked the packet blob at both `43913c4` and `a036064`: each hashes to the cited SHA, so `a036064` does pin this exact packet data. It is a valid artifact revision even though it is not the first 159-form commit.

7. **One-prime fibres, outer-anchor bounds, Type II rigidity — VERIFIED.** `ONE_PRIME_FIBRES.md:9-21, 104-115` gives the one-prime finite exhaustion and states no primality assumption for affine anchor/partner; `AFFINE_SEED_CLOSURE.md:126-149, 199-230` uses outer-anchor privacy, both Type II quotient directions, and the noncritical Type II terminal leaf; `PRIMARY_SEED_PACKET.md:42-58` summarizes the replacements. The paper accurately names these at `pointwise-obstruction.tex:1133-1138`. The eventual proof is mathematical and conditional on the stated finite prime tuple, not a heuristic; the finite verifier alone does not establish its eventuality.

8. **Priority and independence — PRIORITY VERIFIED; “independently” needs qualification.** Astra’s whole-component affine packet appears in git at `f0f2e12` (2026-09-30 18:40:21), before this repo’s finalized Theorem F certificate commit `19c712c` (20:01:11); astra’s earlier 800-form result therefore predates Theorem F. Astra’s 159-form reduction is later (`43913c4`, Oct 1 10:58:54) than the formal closure proof (`19c712c`, Sep 30 20:01:11). The respective certificates are indeed different (affine packet vs polynomial frame), and paper says so (`pointwise-obstruction.tex:216-218`). But “independently” should mean independent construction/certificate and not necessarily independent mathematical toolkit: the paper explicitly says astra uses this paper’s outer-anchor theorem (`pointwise-obstruction.tex:1137`), and Type-II/outer-anchor ideas overlap. Astra’s own closure files do not, in the passages reviewed, give an explicit citation to this repo for that imported/shared theorem. Recommend “independent certificate/closure, using shared or cited auxiliary lemmas” rather than a blanket claim of mathematical independence. Do not say the 159-form version predates Theorem F; the earlier 800-form version does.

9. **Overclaim, prominence, omissions — Overall credit is prominent and the main qualifications are mostly good; revise a few points.** Abstract (lines 58-64), Intro Theorem C and following paragraph (191-218), Theorem 4.10 and remark (1101-1153), acknowledgements (1582-1588), replay appendix and bib entry (1606-1623) all prominently credit Astra and distinguish the second result. Paper explicitly says no independent re-derivation of Astra eventual closure and attributes its proof to Astra (1140-1145), a sound caveat. It correctly makes the positive point outside-component claim conditional and says Dickson for the restricted tuple is needed (1117-1122); it does not imply unconditional existence. It also correctly states the 159-packet has only computable, unquantified threshold, while the explicit huge bound belongs to old 800 packet (1123-1125). Potential issues:
   * Bib citation still has TODO author/citation wording (1583-1588, 1619-1623); fix before publication.
   * Revision a036064 may not pin the current packet revision (see #6).
   * “independently” requires scope clarification in light of explicit use of the paper’s outer-anchor theorem.
   * Numbering language “159 constant nodes (84 offsets and 75 rows)” is the source’s packet node count, not 159 independent forms added to q,p; make overlap/counting convention explicit.
   * Astra itself stresses no actual simultaneous-prime specialization is known and no numerical N is given (`PRIMARY_SEED_PACKET.md:25-30`); paper does not hide this, but an explicit nearby reminder that no actual sterile prime is known would be useful (paper says it globally at `pointwise-obstruction.tex` around its “What is not claimed” paragraph).
   * No indication found that astra’s eventual arguments are merely heuristic: docs explicitly prove a common finite bound (`AFFINE_SEED_CLOSURE.md:243-255`) and distinguish proved arguments from checker coverage. Its caveats are lack of actual prime specialization, no numeric threshold for the 159 theorem, and finite packet’s original status being only skeleton closure. Paper largely conveys these.

10. **Checker replay — VERIFIED.** In `/tmp/astra_copy`, with the requested memory/time limits, `pointwise_primary_packet_check.py` produced:

```
status: VERIFIED_PRIMARY_PACKET_EVENTUAL
packet_sha256: 62a886126f4605c2f5b0c89e36a4154b36bf2ec1cfa10339161aef9a2ea0c2f2
primary_forms: 159; constant_nodes: 159
signed_monomials: 315642
M_digits: 287; support_primes: 91
positive_subprogression: q=Q+M*(507+857*k)
simultaneous_primality_proved: false
explicit_threshold_proved: false
```

## Main correction to paper

The count is consistent: q occurs in both primitive families at a=0 and h=0, and is counted once; p is distinct and added, giving 159 distinct forms. For readability the theorem may state explicitly that this is the sole A/H overlap and q is that common form. The H=1 row is 18q+1, not p.
