# z62 cross-model hostile review — PARITY

**Verdict: ACCEPT-WITH-FIXES.** “Narrowed” is defensible for the tested finite dictionaries, not as a death certificate for river/conjugacy-class parity arguments. ES remains OPEN.
Reviewed `side-agent/z62-parity` at `b6f8a3a458c61028fb70f3d3d901d1137a69f7c7`; initial registration: `c6dd22f9`.
Independent algebraic review plus bounded reruns; all commands used `ulimit -v 4000000`, timeouts 30–300 seconds (none >1800).

## Per-claim audit

| Claim | Classification | Independent derivation / finding |
|---|---|---|
| P0(a), involutions | CORRECT | Each involution partitions finite S into singletons and pairs. Thus #F_cert ≡ #Fix σ − #K; push multiplicities through Φ. Disjointness and oddness are now present. |
| P0(b), handshake | CORRECT | Sum of degrees is 2E, so the number of unknown odd vertices has the parity of the known ones. Push these vertices through Φ. Explicitly require a finite graph; maximum degree 2 is stronger than needed. |
| P0(c), Morse | CORRECT | For a genuine acyclic discrete Morse matching on a finite complex, matched adjacent-dimensional cells cancel in χ; only critical cells remain. Subtract known critical contributions and group the rest by certificate. |
| P0(d), Stokes | CORRECT | Acyclicity over the chosen coefficient ring supplies ∂c=z; ⟨ω,z⟩=⟨δω,c⟩, supported on mapped cells. Filling independence follows already from ⟨δω,c−c′⟩=⟨ω,∂(c−c′)⟩=0; no H₂ argument is needed. |
| P0(e), Lefschetz | CORRECT | Alternating chain trace equals alternating homology trace: boundary contributions cancel in adjacent dimensions. Subtract known diagonal terms and push remaining signed coefficients through Φ. The explicit diagonal-support hypothesis repairs the earlier fixed-cell mistake. |
| P0 opening “exactly when” / “necessity” | CORRECT-WITH-FIX | The bookkeeping identity is correct; the claimed converse is false. Nonzero I is sufficient, not necessary for existence or for every argument using these structures. Two disjoint edges, each with one known endpoint and one certificate endpoint, have I=2=0 in F₂; following either known endpoint still finds a certificate. Localize to one component to obtain a useful nonzero index. |
| P1 | CORRECT | An empty sum is zero, over either ring. Consequently nonvanishing cannot cover a certified zero in its asserted domain. This does not forbid exact identities, eventual positivity, or a prime-only construction. U₇ positivity gives ES, not (MS) without a further implication. |
| Observation A | CORRECT, for prime p | det γ=1; F=[c,d−a,−b] for γ=[[a,b],[c,d]] is preserved by γ. Discriminant is (tr γ)²−4. Since a_form=4C divides b_form, a determinant-one shear sends b_form to −b_form, proving ambiguity. Primitivity uses primality: gcd(F)=gcd(4C,p)=1, since opposite-parity u,B give p≥8C−3>4C for a prime certificate. State the prime hypothesis explicitly if this observation is reused for composites. |
| Lemma R | CORRECT | Put m=v−u=2k+ε. Substitution x→x−ky gives b′=tε and c′=−n−t(m²−ε)/4=σ−t(σ²−ε)/4. This remains valid for negative m and m=0. |
| Theorem R | CORRECT | Direct multiplication gives top row (tσ−1,−t), bottom row (tuv−n,−1)=(σ,−1); det S(u)=1. No primality is used. Also F_w∘S(u)=[σ,−tσ,t], directly explaining the proper-form equivalence. |
| Corollary R′ | CORRECT as explicitly scoped | Conjugate matrices have identical class invariants; the displayed normal form depends only on (t,σ). Q(1,u)=σ−tσu+tu²=−n. “Independent of p” means **at fixed (t,σ)**, not independent of the p-dependent set of occurring pairs. Marked/level data and arbitrary weights on unbounded pairs remain unexcluded. |
| KT1 finite exact analysis | CORRECT, finite CERTIFIED result | Full row rerun agrees; independent binary elimination gives nullity 98. Quotient rerun gives 16 patterns, 95 per-word identities, 3 excess directions, all represented on ALLX and valid on held-out data. This is not a theorem about arbitrary river weights. |
| KT1 predictive kill / main-line death | CORRECT-WITH-FIX | The >60% predictive kill does **not** fire. The alternative always-odd/boundary clause supports a negative finding for the implemented dictionary only. Theorem R supplies no replacement impossibility theorem. |
| KT2 | CORRECT, model-relative EVIDENCE | Full C≤40 rerun agrees exactly: 503 hits; all-pair expectation 501.9±14.1, z=0.08; coprime expectation 490.1±13.4, z=0.96. The registered 3σ criterion fires. Independence/uniform-choice assumptions define a comparison model, not a proved probability law for deterministic midpoints. |
| H2 | CORRECT, finite CERTIFIED linear algebra | Rerun: rational pattern rank=mod-P rank=42, 56 patterns, word kernel 126. Augmented count kernel is 126 at M=840, so inclusion plus rank_Q≥rank_P proves equality over Q. At M=13440, kernel 129 has only three extra, feature-free empty-training-class vectors. No claim about all signed indices follows. |
| H3 | CORRECT, finite scope | Full TSV is byte-identical; independent nullity is 36. Within-pool contributions count edges twice; the exceptional duplicate datum is A=tu−1. This tests fibre-degree weights, not arbitrary Stokes/nonlocal constructions. |

## Pre-registration and numerical checks

The checkpoint commit genuinely precedes the KT1/KT2 result commits. It registered C≤40 and the 100000/200000 split.
KT1 nevertheless changed cycle parity to half-cycle bits, the second centre to **some** ambiguous form, and regular-CF period to marked HJ length. These are material feature changes, now honestly disclosed; the original feature battery was not executed literally.
The full rerun has **2212** primes, **1181/1031** train/test. Every generated row matches the archived TSV after controls are excluded/deduplicated.
Independent divisor enumeration verifies STAR_one+STAR_hj equals the u=1 divisor-family parity on every prime: odd on **18/2212**, zero on **1026/1031** test primes. The second four-feature class-majority fit achieves **830/1031=80.5%**. Thus the predictive clause fails substantively, not merely because the zero combination was allowed.
The registration also says “no single W_w is constant ... on any fixed class”; many implemented columns are identically zero. Excluding trivial columns requires an explicit quotient convention, not an implicit reinterpretation of that clause.
The alternative registered always-odd/non-certificate explanation can justify retiring this **modified finite dictionary**. It cannot justify retiring the main line of all single-word conjugacy weights.
KT2's C≤40 rerun has **385** primes, **11096** forced-pair cases, **4304** symmetric cases, **291/385** primes with a forced certificate versus **378/385** with any certificate at C≤40. Numerical agreement does not establish equality to a random distribution or rule out conditional enrichment.
The supplied symbolic/numeric verifier also passes: **18048** words of odd n≤1500, zero matrix/cycle/shear failures. A separate direct (u,v) enumeration agrees with the source's divisor-based word generator for **all odd n≤501**.

## Mandatory falsifier table audit

| Screen | Finding |
|---|---|
| F1 odd squares | Correct for STAR/U₇ and the stated coprime Type II support: weighted sums vanish. Independently checked small odd squares in the word audit. Full ES need not vanish. **Qualification needed:** I(m²)=0 is forced only if the identity is defined there; a genuinely prime-only ML-P construction has no required square value. The final ML-P row drops this qualification. |
| F2 numerator 8 / C-even | All **12** listed R₈ zeros and their full R counts rerun exactly with the separate z57 decision engine; **4** lie in 𝔐. R>0 at each, so a uniformly positive STAR-supported index covering these inputs must use C-odd support. Correct distinction between R₈ and U⁽⁸⁾/U₇ in §0; the latter valuation qualification matches FRONTIER §4. Thresholds matter: none of these near-10¹⁰ zeros refutes an assertion starting above them. H2 really does not test (−1)^C. |
| F3 285 composites | Separate direct R sieve through 9·10⁶ reproduces all **285** listed non-square composite zeros through 7999801. Uniform identities must vanish there; prime-only identities need not. The stated Z₇ exception set is consistent with FRONTIER, but I did not independently rerun the complete U₇ composite census. “Identities are uniform in n” in the final table is valid for Theorem R, not automatically for a hypothetical parity law fitted on primes. |
| F4 14 STAR and 38 𝔊* primes | Separate R sieve reproduces all **14** STAR zeros (**9** in 𝔐). All **38** 𝔊* zeros checked: 34 via the archived independent z56 C engine, four <1000 by small-word enumeration. Exactly **24** have positive STAR support. **The memo omits 𝔊* entirely from both mandatory tables.** Add: 𝔊*-supported indices vanish on all 38; STAR indices need vanish only on the 14; U₇/full Type II have no known prime zero. No inference from a 𝔊* zero to empty STAR support is valid. |

Theorem R itself correctly says the screens are not existence tests for an algebraic identity. No HOT LEAD or “survives all four” result has been established.

## Attribution

Checked the actual repository sources, not just the memo's bibliography:
- `WINDMILL.md` Lemma 1 already gives the involution weighted count; `BRAINSTORM/invol_topological.md` Lemma T gives the topological bookkeeping. P0 is a restatement/repair plus explicit Morse/Stokes cases, not a new obstruction theorem.
- `WINDMILL_REDUCTION.md` §3 already tests Legendre/SQUFOF midpoint bias; §5.2 identifies ambiguous certificate forms; §8 has T+2=tτ and the joint-factorization constraint. Observation A is rediscovery; KT2 is a useful differently-sliced replication, now credited correctly.
- `BRAINSTORM/z52b_pass1_H05.md` **Z1665** already records the word form and trace-dependent discriminant; **Z1700** gives T^u[[−1,0],[t,−1]]T^v. Cyclic conjugation already removes the separate u,v dependence. Theorem R is a useful explicit conjugator, not a new phenomenon.
- `BRAINSTORM/invol_windmill_signature.md` already keeps arbitrary weighted identities open; `invol_sign_identities.md` Prop S warns that fixed real-character signs fail on square residue classes. “Jacobi-type is natural” is only an Assessment, not an unexplored forcing mechanism.
- Late discovery of these sources is candidly disclosed, but the stated “read before computing” plan was not honoured. The attribution paragraph should preserve WINDMILL_REDUCTION §1's own CONDITIONAL/general-range qualification for the Zagier/rivers dictionary.

## Required fixes, priority order

1. **Remove the unsupported broad death/necessity conclusions.** Replace “declare the main line dead on the strength of Theorem R” and the Bottom line's “a parity proof would still need ... beyond a single word's conjugacy class” by “the tested finite dictionaries produced no useful exact index; arbitrary functions of (C,u+B), including conjugacy-class weights, remain open.” The theorem proves dependence, not inadequacy. Harmonize §§4.1, 5 and the proposed FRONTIER text with Cor R′'s correct caveat.
2. **Repair P0's converse.** State that these finite constructions yield a weighted identity and nonzero total suffices; do not characterize every proof using these structures by nonvanishing of this particular global total. Say finite graph and acyclic Morse matching explicitly.
3. **Keep the registration verdict literal.** Predictive KT1 kill failed; feature changes were post-registration; the alternative boundary/always-odd limb only retires the implemented finite feature space. KT2 passes its registered empirical criterion under the stated baseline models.
4. **Complete and scope the falsifiers.** Add the 38/24 𝔊* distinction. Condition square/composite requirements on the domain of the identity, and support-enlargement requirements on including the certified zeros. In particular qualify §4.5's blanket “uniformly non-zero ... beyond STAR” and the final ML-P square/F2 rows for thresholded or prime-only claims.
5. Keep KT2 as “no enrichment detected under these baselines/range,” not a theorem of random-rate behaviour; retain the corrected prior-work attribution and its source qualifications.

## Reproduction record

Sources were extracted with `git archive` to `/tmp/xrev_PARITY`; no reviewed branch files were modified.
Reruns (each separately timeout-limited, Python via `uv run`):
- `z62_parity_river.py 200000`, `z62_parity_gf2.py kt1_rerun.tsv 100000`, `z62_parity_quot.py kt1_rerun.tsv 100000 840 200000`.
- `z62_parity_legendre.py 30000 40`; output identical to `kt2_legendre_3e4_C40.txt`.
- `uv run --with sympy python scripts/z62_parity_verify.py 1500`; signed script `200000 100000 840` and separately `13440`.
- `z62_parity_nonlocal.py 200000`; full output identical to `h3_nonlocal_2e5.tsv`.
- Compiled archived `z58_screens_rstar.c` (`9000000`), `z57_synth_dec8.c` (each of the 12 singleton screen intervals), and `z56_famdesign_decide.c` (each 𝔊* singleton ≥1000); reviewed loop bounds and allocations before running.
- `scripts/z62_xrev_parity_audit.py /tmp/xrev_PARITY` independently checks table agreement, binary ranks, predictive fits, the divisor identity, small-word enumeration and screen outputs. All assertions pass; temporary logs stay outside git.

**Bottom line:** accept the algebra, the repaired index bookkeeping and the reproducible finite negative evidence after the fixes above. Do not record a theorem excluding single-word conjugacy parity, a literal successful predictive KT1 kill, or a new forcing mechanism.
