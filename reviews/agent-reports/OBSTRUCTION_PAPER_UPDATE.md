# paper/pointwise-obstruction.tex — update (4 Oct 2026)

Branch `side-agent/obstruction-paper-update`. Built with three pdflatex
passes: no errors, no undefined references, no overfull boxes. One underfull
vbox (page-break badness) remains; the previous version had one too. The
paper grew from 29 to 33 pp. No existing statement was strengthened. Theorem
and evidence numbers used in the replay appendix (4.13, 4.15, 5.5, 6.1) are
unchanged.

## Changes

1. **New Remark 4.16 `rem:astralater`** (at the end of §4.7, after Evidence
   4.15), labelled **reported [AS]**. It covers astra's newer results. We did
   not re-run astra's checkers for them; astra is read-only.
   * `PRIMARY_REACHABILITY.md`: for every n≥0 on q=Q+Mn, all 159 primary
     anchors are reachable by explicit nonpositive walks of ≤11 edges. No
     primality or threshold is needed. The 52 necessary divisor exclusions
     (29 A, 23 H) are included; if any fails, there is a positive vertex
     within ≤12 edges. Stated explicitly: this does not show the hypotheses
     are necessary, and it gives no sterility.
   * `PRIMARY_LEAF_RELAXATION.md`: the primality of F=(3q−553)/44 (anchor
     t−1106) is replaced by an exact leaf condition L. The theorem uses 158
     primes plus L, for large n, with no threshold. It is stated explicitly
     that this is *not* a 158-prime Dickson theorem: the composite
     realisation F=8933R still uses 159 affine primes. The actual-input
     example (p=20447316559849) is a local check, not a sterile certificate,
     and it is off the packet's progression.
   * `TWELVE_HUB_SKELETON.md` (a 237-form skeleton only) and
     `NORM_SEED_FAMILIES.md` (local three-fibre blocking, not closure). All
     9526 retained actual inputs have certified positive paths, so no sterile
     prime was found.
   * Closing sentence: Conj. 1.2 is unchanged; the stronger version remains
     astra's.
2. **New §7 "Procedures and witness sizes: companion results"**
   (`sec:companion`), labelled **reported**. The old §7 is now §8.
   * POINTWISE_SIZE Theorem M ((a) proved, (b)–(d) conditional), Theorem C
     and Corollary C1. Instances from [PS §3]: BFS_k gives Thm 4.9, and
     Thm 4.13 is the literal 13521-polynomial form. The intro's informal
     Principle is still called heuristic within the paper, with a forward
     pointer.
   * Proposition A (proved): eventual-sign comparisons with p^θ / Hardy-field
     thresholds stay inside the obstruction. Oscillating tests are not
     covered.
   * W(p) is defined via the multiplier identity, which is displayed and
     checked. POINTWISE_OMEGA3 Theorem 5.2: W(p)>(log p)^A i.o. for every A,
     proved modulo Thorner–Zaman Cor. 1.4. This is read as *evidence* that
     multiplier mechanisms need super-polylogarithmic moduli. It says nothing
     about reachability or about W<∞.
3. **Small edits.**
   * One sentence added to the abstract.
   * Intro: a pointer after the Principle, and a qualifier on "using the size
     of p".
   * "What is not claimed": a pointer to Remark 4.16.
   * §8: item (3) and the final paragraph point to §7.
   * Date changed to 4 Oct 2026.
4. **Bibliography.**
   * [AS] now lists the four new astra files.
   * New entries: [PO], [PO3] and [PS] (companion notes in this repository,
     with their review files), and [TZ] (Thorner–Zaman, Math. Z. 306 (2024),
     arXiv:2108.10878v2).

## Not done

* The new material has not been refereed.
* Authorship and the [AS] citation (referee D5) are still open.
