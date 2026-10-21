# OpenAI mathematics snapshot: ES impact source excerpts

Source URL: https://github.com/openai/math

Inspected local checkout: `/tmp/oai-math`, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Audit date: **2026-10-21**. Release/history dates are those asserted in that checkout,
not an independent authentication of the release.

**All manuscript claims: CLAIMED (OAI dump, unrefereed).** Where indicated in
`OAI_DUMP_IMPACT.md`, add “Lean-formalized per the supplied comparator”. This is
not a claim that we independently compiled or kernel-checked the formalization.

The 16 numbered excerpt files contain verbatim theorem environments from 25
manuscripts and the associated Lean scope pages where present. Family 029 also
includes its two technical propositions used for the fixed-mute-prime deduction.
Some extracted environments are cited classical inputs or intermediate theorems,
not new results of the collection. TeX macros retain their source meanings;
consult the listed source path for definitions. No PDFs are copied.

To obtain a permanent source URL, prefix a listed path with
`https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/`.
For example:
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/DirichletSevenEighths.lean

`data/z47_oai_impact/inventory.json` records manuscript/source paths and linked
comparators. `lean-audit.json` records comparator configurations, recursively
visited local OAI modules, missing imports, and lexical hits. The script does
not recursively audit Mathlib or execute Lean. All 16 distinct lexical hits in
the original 15-family scan are explanatory comments, not admitted proofs or
axiom declarations; adding 182 adds no hits. Comparator templates deliberately
contain `sorry`, and are NOT the solution modules.

Important scope discrepancies: 015 formalizes prime degree, not the quartic or
sextic companions; 027 formalizes a supporting seam-compatibility result only;
182 formalizes square differences only. For 026 the prose scope page mentions
only prime-ratio increases, but the actual comparator and solution endpoint
also include the large-gap theorem. The main impact memo uses the actual endpoint.

Reproduce the static audit (bounded memory):

```sh
ulimit -v 2000000
timeout 180 uv run python scripts/z47_oai_impact_audit.py
```

`halasz-excerpt.md` is a separately identified short external theorem excerpt,
not an OpenAI manuscript, used to justify the BM-main-term upgrade.
