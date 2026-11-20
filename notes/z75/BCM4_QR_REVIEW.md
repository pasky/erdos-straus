# Review record for BCM4_QR

```
Result: The independent Opus reviewer found no fatal error in the QR construction or dyadic obstruction at commit 787e92e36; this records its checks and the author's disposition.
Label: Assessment
Scope: Internal cross-model read of the weak-arithmetic result, not external refereeing or a priority search.
Review: cross-model (anthropic/claude-opus-5-5, functions.review, review range 787e92e36^..787e92e36)
Triage: DATA
STATUS delta: none
```

The reviewer was asked for a mathematically hostile read focused on (R), unramified 2-torsion, order of marks/tree, and the dyadic obstruction. Its first sentence: **“I found no fatal error.”** Below is a summary of its response, not a transcript.

* The character-extension lemma factors the defect of (R) through the image of the horizontal residue map. Vertical primes have ramification index one, and their characters agree on restricted classes. There is no squareclass independence assumption about normalized prime generators.
* Purity, geometric comparison for the line and `SL₂`, Hochschild–Serre, and Kummer give lifting of unramified classes from **2-torsion** constants. Merely having no transcendental Brauer classes would not suffice.
* The root edge preserves rational factoriality and kills only the requested class at its pivot. The sphere edge only needs Gaussian descent **over the fraction field**, followed by Nagata at the old primes. The final root tasks realize the kernels, and fresh lines ensure nontriviality. The marks/tree are not circular.
* The dyadic local symbols in the proof give precisely both supplements and the prime reciprocity signs. The normalized pivots are all the nonstandard primes. Polynomial descent and the primitive-square-class obstruction still exclude ES at `P`.
* The dyadic kernel is prime idempotent; its nonzero proper extension after old localization cannot be finitely generated. The proposed CRT translation would identify this localization with the upper algebra.

The reviewer requested fuller dependency citations, explicit orders for the fresh lines, row-chart and prefix-unit details, and clarification of which prior sphere hypotheses may be dropped. These are applied in `BCM4_QR.md`. The §0 note distinguishes the Target B theorem from the scoped obstruction for Target A. The reviewer also suggested a toy numerical sign check; the worked finite-prime check in §5 is not used to justify the theorem. Promotion and any broader priority check remain the orchestrator's decision.
