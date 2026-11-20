# Cross-lab hostile review (Claude Opus) of the NR-model notes (Astra, z72–z74)

Reviewed at `55757e2d2`. ES is OPEN. This review is internal and has not been externally refereed. I re-derived every
load-bearing step myself. Astra's audits were read but not trusted: three of the eight notes are themselves audits, and I
reviewed their claims directly. Context: `REVIEW_JOINT_NR_TS_OPUS.md`, whose lemma L2 (single descent lemma) and L3
(square-class obstruction) I reuse below.

**Theme.** Countermodels of weak arithmetic in which ES fails at a nonstandard prime `P≡1 (840)` while a non-residue
certificate holds. The certificate is **NR**, the sentence of `Z65_LOGIC2.md` §1: `d=4k′+3, d≥1, x²+p=dy, ud+vp=1`. The NR
notes in this lane fall into three groups.
* **(a) Non-square-profile models.** These are Bézout domains and **not** PIDs. `P` is ≡1 modulo almost every standard
  prime and is a non-residue at sparse "test" primes. Here NR holds with **standard** prime moduli, universally in the
  sparse versions.
* **(b) The NR-stage PID.** `LOGIC_ES_RIGIDITY_NR.md`. Its NR moduli at `P` are necessarily nonstandard.
* **(c) Combining (a) with universal TS.** Only partial results exist.

## 1. Verdicts

| Note | Kind | Verdict |
|---|---|---|
| `LOGIC_NONSQUARE_PROFILE.md` | one-prime thickening; IOpen+Bézout+Dirichlet+NR(P)+¬ES(P) | ACCEPT-WITH-FIXES (scope of "NR") |
| `Z73_NONSQUARE_ADELIC_REVIEW.md` | audit of the above; proves **¬universal NR** there | ACCEPT-WITH-FIXES (dependency stated) |
| `LOGIC_UNIVERSAL_NR_AUDIT.md` | sparse sign primes: **universal NR, standard moduli**, Bézout | ACCEPT-WITH-FIXES (replay pointer) |
| `LOGIC_NORM_BASE_NR_AUDIT.md` | same + `P=X²+Y²`, X,Y∈R; **universal TS fails** | ACCEPT |
| `LOGIC_STANDARD_PRIME_SIGNS.md` | all sign words at standard q for nonassociate primes; QR_std fails | ACCEPT |
| `LOGIC_ES_RIGIDITY_NR.md` | descent lemmas; PID with universal NR (nonstandard moduli) | ACCEPT-WITH-FIXES (citation, sketch) |
| `LOGIC_ADAPTIVE_SPARSE_NR.md` | sparse kernels for an adaptive TS tower | ACCEPT as scoped (self-labelled CONDITIONAL) |
| `LOGIC_CIRCLE_ORDINARY_AUDIT.md` | ordinary-place induction through circle stages | ACCEPT |

No claim is WRONG. No note overclaims anything about standard ES, PA, ZFC, IE₁ or IΔ₀.

## 2. Per-claim tables

### `LOGIC_NONSQUARE_PROFILE.md` (NP) and its audit `Z73_NONSQUARE_ADELIC_REVIEW.md` (AR)
| # | Claim | My re-derivation | Verdict |
|---|---|---|---|
| NP1/AR1 | **Compressed-modulus lemma.** Fix `N≥2`. Count the parameterized ET Prop 1.9 classes with `N∣m` and `r≡1 mod m/N`, with the factor 4 kept. There are `O_ε(N^{4/5+ε})` of them, and `m≤512N¹¹` | I checked every row of the encoding table against ET pp. 7–8 (archived PDF). For example, in II-2 one has `c(4a²d+1)−af=a+c`. In I-3 one has `h(1+4c²d)−Jc′f=h+Jc′` with `J=C²D`. For two distinct slots the product is ≤`N²`. For I-2 it is `F²AB=NF`; for I-3 it is `F²C²D≤N²`. Ordering `Lx≥My≥Hz` gives `e²(zt)(xz)(xt)=(ex·zt)²≤(9/4)N⁴`. Fixing each of the four small parameters gives positive factorization targets of polynomial size. For the `xt` bucket, positivity of both factors follows because `4xtz≤M` would give `4xyzt≤My`. | CORRECT |
| NP2 | `N=1`: no class contains 1 | A family class containing 1 contains odd squares `t²≡1 (m)`. These would have Type I/II solutions, contradicting ET Prop 1.6. | CORRECT |
| NP3/AR2 | Haar thickening keeps survival ≥`δ/2`. The order of quantifiers is: fix the finite support `S` first, then the depth `K`. | A new hit needs `v_q(m)>K`, so `N≥(q^{K+1}/512)^{1/11}→∞`. The `S`-smooth tail of `ΣN^{−1/5+ε}` tends to 0. The unit-Haar factor at ℓ is `ℓ/(ℓ−1)`. `U` is closed, and Portmanteau gives the limit mass as ≥ the limsup. | CORRECT |
| NP4 | The profile is componentwise transcendental, with `π_q≡1 (q)` for all `q≠ℓ` | The laws are nonatomic, and we discard a null set of algebraic coordinate values. | CORRECT |
| NP5/AR3 | Restricted adelic evaluations, the tail Dirichlet rule, Bézout via the **residual** content, IOpen, and no PID | The fibre `P=1` is geometrically integral and rational, with pivots nonzero mod `P−1`. Content: `m_q=min(v_q(u),v_q(v))` has finite support because `Uu+Vv=1`, and a CRT syzygy correction finishes. `P−1` is divisible by every `q≠ℓ`. | CORRECT |
| NP6 | ¬ES(P) via `LOGIC_MARKED_SECTIONS.md` (E) | Correct relative to MARKED_SECTIONS, which I spot-checked: the λ₀+f(T)c repair is sound. **Independent route:** L2 descent. Every stage here is a line, row or Dirichlet edge with a gr-domain, so any positive triple lies in `ℚ[P]`. Integrality at the marks makes the class `T≡π (D)` polynomially solvable. ET Prop 1.9 plus Dirichlet then puts `π` in a family class, which contradicts `π∈U`. | CORRECT (fix F3) |
| NP7/AR4 | NR **at P** with `d=ℓ`: `x²≡−π_ℓ (ℓ)`, `(x²+P)/ℓ∈R`, `u=(1−vP)/ℓ∈R` | The full ring witnesses are verified. | CORRECT |
| NP8 | The Outcome says "the NR certificate holds" | It holds only as the **instance at P**. Universal NR **fails** in this model (AR5). | CORRECT-WITH-FIX (F1) |
| AR5 | **¬NR(Q)** for `Q=1+8ℓ(P−1)`, even with nonstandard witnesses | `Q` is a permanent prime of `A` and a unit everywhere: it is `≡1 (q)` for `q≠ℓ`, `≡1 (ℓ)`, and `≡1 (64)` at 2. So it is a square unit at every place. The marked section of the witness tuple gives `d>0` on `T>1` (the real tower over `P>1` is connected and `x²+Q>0`). CRT gives `t²≡Q(π) (BD)`, and then `n=1+(t²−1)/B`, `Q(n)=t²`, `n≡π (D)`. A prime `s≡3 (4)` dividing `d` would then satisfy `(x/t)²≡−1 (s)`. L2 descent **cannot** replace the section here, because NR witnesses need not descend. | CORRECT rel. MARKED_SECTIONS (F2) |
| NP9/AR | PID boundary: one square-valued change at a fresh `q≡−ℓ⁻¹ (4d)` is caught by II-2 with `a=1`, `f=ℓq` | `χ_{−d}(q)=χ(−1)χ(ℓ)=(−1)(−1)`. Verified for 64 pairs `(ℓ,g)`. | CORRECT |

### `LOGIC_UNIVERSAL_NR_AUDIT.md` (UN), `LOGIC_NORM_BASE_NR_AUDIT.md` (NB), `LOGIC_STANDARD_PRIME_SIGNS.md` (SP)
| # | Claim | My re-derivation | Verdict |
|---|---|---|---|
| UN1/SP3 | A stage prime is a non-square in the **geometric** function field. `k` nonassociate primes give a geometrically integral `2^k` cover. | The ambient ring is normal (smooth). In characteristic 0, `(A/s)⊗ℚbar` is reduced, so the order is 1 on every geometric component, and nonassociate primes share no component. The multiquadratic criterion follows. A splitting divisor is harmless (`Σχ(P²+1)=−1` was checked for all odd q<400). | CORRECT |
| UN2/NB1/SP3 | There are `q^h/2+O(q^{h−1/2})` negative-sign tuples, and the projection `B_q` has size ≥`q/3` (≥`q/2^{k+1}`) | Lang–Weil applies to the fixed cover, with an **upper** bound of `q^{h−1}` per fibre over `P` (`(q+1)q^{h−2}` when projecting by `X²+Y²`; fibre count `q−χ(−1)` checked). The projection is checked on examples. | CORRECT |
| UN3/SP2 | Loss when releasing a depth-0 test prime is `≪ D_S c⁻¹ q^{−α}/(1−q^{−α})∏_S(1−r^{−α})⁻¹` | The class probability at the test prime is `1/(|B_q|q^{e−1})≤3q^{−e}`. We choose `q` *after* `S` is fixed, and there is no sum over unrestricted primes. | CORRECT |
| UN4/SP4 | The product law is not adapted to the samples. Survival is ≥1/2. Integrality almost everywhere comes from the two prefix schedules. | The schedule depends only on finite task data. Weak convergence holds on cylinders. | CORRECT |
| UN5/SP5 | Every nonstandard `R`-irreducible is a scheduled `A`-prime **element** with valuation 0 everywhere. Distinct positive `R`-primes are not `ℚ^×`-associates. | If `v_l(p)>0`, then `p=l·(p/l)`. A factorization in `A` normalizes by one rational. `s₂=ks₁` forces `v_r(k)=0` everywhere, so `k=±1`. | CORRECT |
| UN6/SP6/SP7 | **Universal NR with standard prime moduli.** In SP: every finite sign word holds at infinitely many `q≡3 (4)`. | Each task repeats infinitely often, with a fresh test prime each time. `−s` is a square mod `q`; the witnesses `y=(x²+s)/q` and `u=(1−vs)/q` lie in `R`. | CORRECT |
| SP8 | QR_std (`Z65_LOGIC2.md` §1) fails | We have `R/PR↪A/PA` because `PA∩R=PR`. Every stage of `A/PA` has a purely transcendental fraction field over ℚ, since one row pivot survives over the generic point of `P=0`. So `√−q∉A/PA`. | CORRECT |
| UN7/NB/SP9 | ¬ES(P) | Same as NP6: correct relative to MARKED_SECTIONS, and also independently by L2 descent to `ℚ[P]`. | CORRECT (F3) |
| NB2 | Exact-norm lifts: Hensel on a unit partial at odd primes; at 2, `y∈4ℤ₂` and `π₂≡1 (8)`. Algebraic independence of `X,Y`. | `ℚ(x,y)⊇ℚ(π_l,y)`, which has transcendence degree 2. | CORRECT |
| NB3 | Binary descent of positive triples to `ℚ[P]` | I re-derived it: `FG=P²x²`, `L∣k4^{−j}P^{i+j}+P²/4≠0`, and the divisor fact (`uv−c` is irreducible for `c≠0`; conjugation swaps `u,v`). L2's base check is a shorter proof. | CORRECT |
| NB4/NB5 | TS **at P** holds. **Universal TS fails** at the Dirichlet prime `Q=1+4Z`. | `Q` stays prime in `A[i]`, since a row entry survives modulo `Q`. If `Q=a²+b²`, then `Q∣a±ib`, so `Q²∣Q`. | CORRECT |
| UN8 | "the bounded checker `/tmp/z73-compression-check.py` also passes" | That path is outside the repository and cannot be replayed. | FIX (F4) |

### `LOGIC_ES_RIGIDITY_NR.md` (ER)
| # | Claim | My re-derivation | Verdict |
|---|---|---|---|
| ER1 | Line rigidity: the positive sector is clopen because each coordinate is ≥`1/c`; take the limit at `+∞`. A row descends through `A[1/u]∩A[1/v]=A`. | — | CORRECT |
| ER2 | Binary quadratic descent (cases `i+j=2,1,0`; `D(4y−P)=P²+4λ` has no real quadratic factor) | I re-derived every case. | CORRECT |
| ER3 | The complete unary non-descending list (menu C) is `u=1+k²/2`, `4λ=u²−1` | The quartic factorization is redone in the table. The identity was checked exactly at 1.85·10⁶ rational points. | CORRECT |
| ER4 | The NR stage `DH=V²+s` over ℚ for **every** positive `s`. `D` is prime. Nagata applies. `B∩F(D)=A[D]`. Bounded elements and units are constant. | `V²+s` is irreducible over an ordered `F` because `s>0`. The Gaussian version needs `s` prime (`LOGIC_CIRCLE_AUDIT.md` (ii)); it is not used here. | CORRECT |
| ER5 | Two-step descent through the NR stage | Correct. L2 gives it in one step (gr = `F[D,V,H]/(DH−V²)`). | CORRECT |
| ER6 | An external PID with IOpen, universal NR and ¬ES(P), with `P=X²+Y²` | The model is correct. Its "simultaneous-choice details" paragraph is a sketch. The full proof is `LOGIC_JOINT_PID_TREE_AUDIT.md` §§1–4, which has strictly more task types. The result is a **sub-case of the Opus-accepted joint PID**. The final step cites "Mordell–Schinzel (ET, discussion preceding Prop. 1.9)". The quote is accurate (ET p. 8), but the proof should rest on L3. | CORRECT-WITH-FIX (F5) |
| ER7 | §4: zero caught mass for the non-descending list at the profiles `T_q=0 (q≠ℓ)` | I re-derived the argument: `λ=(k/4)²(k²+4)` has even `v_ℓ`; `gcd(n,λ)=1`; `w∣g`; `f≡3 (4)` and `f∣n²+4λ`, so `(−e/f)=1`; reciprocity gives `−(n/e₀)`; and `(n/e₀)=1`. Tested on 30 integral specializations: every one has `(n/e₀)=−1`, as the proof forces. | CORRECT |
| ER8 | §4: "pulling back under `T↦1+T²` costs only a bounded factor by Hensel" | The density of the push-forward is unbounded near `P_ℓ=1`. The factor is bounded (≤2) on `{T unit}`, and that set contains the non-square region where the claim is used. | CORRECT-WITH-FIX (F6) |

### `LOGIC_ADAPTIVE_SPARSE_NR.md` (AS) and `LOGIC_CIRCLE_ORDINARY_AUDIT.md` (CO)
| # | Claim | My re-derivation | Verdict |
|---|---|---|---|
| AS1 | Sparse release law, with `q_j≥2^{2j}` and survival ≥3/4 | Same estimate as UN3, with the Haar factor `q/(q−1)`. | CORRECT |
| AS2 | Fixed-node kernels have TV `O_v(1/q)` to uniform on `V_v(𝔽_q)` | The fibre counts are exact: `q+1` (norm, `q≡3 (4)`), `q` (row chart), `q−1` (Dirichlet on `D(mQ)`), `q+1` (circle on `D(s)`). TV contracts under kernels, and the complement of a proper subvariety is `O(1/q)`. | CORRECT |
| AS3 | Borel–Cantelli: integrality almost everywhere on the sparse set. Second Borel–Cantelli: infinitely many honest negative signs for each fixed node and element. The construction is over the countable set of nodes, not paths. | `Σ1/q_j<∞`; the columns are independent for a fixed node. Joint sign patterns are correctly **not** claimed. | CORRECT |
| AS4/CO8 | Split TS normalization: `p=c h h̄`, `c` a rational Gaussian norm, finitely many split imbalances | Same as `LOGIC_CIRCLE_AUDIT.md` §3. It needs all-place integrality almost everywhere, and the notes say so. | CORRECT |
| AS5 | Circle descent via the Laurent form `K(i)[u,u⁻¹]` | — | CORRECT |
| CO1–CO3 | `s̄≠0` in `C=A/(P−1)`. The new H-fibre is geometrically integral. Avoidance on the conic (a test of degree `d` meets it in ≤`2d` points, out of `q−χ(−1)`) gives invariant (3). | — | CORRECT |
| CO4 | Integral lifts with one transcendental parameter. At 2 the target must be `1 (4)`: `y∈4ℤ₂` or `2+4ℤ₂`. | — | CORRECT |
| CO5–CO7 | Rows and Dirichlet steps interleave. `R_j`-irreducible ⇔ `A_j`-prime with unit marks. Rational primes persist, and the inert target splits only upstairs. Hilbert-90 descent of factoriality. | — | CORRECT |
| AS6 | **A joint non-PID model with universal NR (standard moduli) + universal TS + Dirichlet + ¬ES(P)** | Both notes label this unproved. I checked the interfaces between the sparse half (AS) and the ordinary half (CO) and found **no obstruction**. (i) The two halves use disjoint place sets, and every non-sparse prime is a deep release with `π_l≡1 (l)` and `π_l` transcendental. (ii) The sparse kernels never read ordinary data. Path decisions read only old values, which are fixed. (iii) All-place integrality almost everywhere is the union of AS3 and CO invariant (2). (iv) Dirichlet outputs are units at both kinds of place. (v) ¬ES follows by L2 descent, using the circle gr-domain. No note assembles the two halves, and a referee could not check the theorem from either note alone. | CONDITIONAL (**assembly owed**; no gap found) |

## 3. Finite computations, re-run independently
* My checker is `scripts/z74_xrev_nrmodels_checks.py 3000` (stdlib only). Command:
  `(ulimit -v 6000000; timeout 1800 uv run --offline --no-project python …)`. It runs in 27 s and every check passes.
  * **A.** All 108,342 ET Prop 1.9 parameterized classes with `m≤3000`. No class contains 1 (`N=1`). Each of the 66,962
    admissible rows `(class,N)` was pushed through the note's forward encoding. In each case the weighted identity holds, the
    slot products are ≤`N²`, the variables are ≤`2N²` and `m≤512N¹¹`. 30,294 of these rows have `gcd(N,m/N)>1`. The II-3
    regression `(11,2,247)`, `N=143`, also passes. This engine is independent of Astra's literal-vs-inverse comparison.
  * **B.** Character and fibre facts, all-32-word realization for five slots at every `q≡3 (4)` in `(60,200)`, and projection
    bounds.
  * **C.** Menu C (ER3) and the Jacobi chain (ER7).
  * **D.** The II-2 square-change example (NP9).
* I replayed `scripts/z73_compression_audit.py`: the same family counts (204/142/61/206/206/102/131), 628 non-coprime rows,
  and survival 1/6 with deep sum 1/12. I replayed `scripts/z73_prime_sign_audit.py`: all 32 words at q=43,47,59,71, with
  minimum projection sizes 10,10,14,16. Both agree with the notes.
* None of these computations is load-bearing. The asymptotic count is proved algebraically (NP1).

## 4. Labels, scope and dependencies
* The models in group (a) are **Bézout, not PIDs**. The notes say this correctly every time. They are different models
  from the joint PID, so **do not combine their axioms with it**. In particular, "universal NR with standard moduli" and
  "external PID" are never proved together. They cannot hold together at a `P` that is a square at every standard place.
* **Dependencies.** AR5 (¬universal NR in the one-prime model) depends on the marked-section lemma
  `LOGIC_MARKED_SECTIONS.md`. That lemma is not cross-reviewed; I spot-checked its repair step. All the ¬ES(P) conclusions in
  this lane instead hold **independently** by L2 descent plus ET Prop 1.9.
* **Master files.** None of the eight notes is cited by name in STATUS, WAVES or FRONTIER. What those files say indirectly
  is accurate: the joint-note Variant is a gap, and "NR kills every arc counter-model" refers to arcs only. Two things are
  missing (§6): the standard-modulus NR result, and the status of the Variant.

## 5. Required fixes, in priority order. I applied all of them, tagged "(z74 Opus xreview fix)".
* **F0 (process).** Add a §0 block to all eight notes.
* **F1 (NP8).** The Outcome of `LOGIC_NONSQUARE_PROFILE.md` says that "the NR certificate holds". Restrict this to the
  instance at `P`, and point to AR §4, where universal NR fails.
* **F2 (AR5).** State in `Z73_NONSQUARE_ADELIC_REVIEW.md` §4 that ¬NR(Q) relies on `LOGIC_MARKED_SECTIONS.md` for the witness
  tuple, which does not descend.
* **F3 (NP6, UN7, SP9).** Add a remark that ¬ES(P) also follows from the L2 descent to `ℚ[P]`, independently of
  MARKED_SECTIONS.
* **F4 (UN8).** Replace the `/tmp/z73-compression-check.py` pointer with replayable scripts.
* **F5 (ER6).** Point the obstruction at L3 (self-contained) and quote ET exactly. Mark the local-choice paragraph as a sketch
  whose proof of record is `LOGIC_JOINT_PID_TREE_AUDIT.md`, and note that the model is subsumed by the joint PID.
* **F6 (ER8).** Restrict the bounded-factor claim to unit `T_ℓ`.
* **F7 (AS6).** In the ADAPTIVE and CIRCLE_ORDINARY notes, and in the Variant of `LOGIC_JOINT_NR_TS.md`, state the interface
  check and that **assembly is owed**. Their label stays CONDITIONAL.

## 6. Recommended master-file changes (for the orchestrator)
* **STATUS.md.** Current line (§1, under the joint-PID item): `the Proof map in \`LOGIC_JOINT_NR_TS.md\` and
  \`LOGIC_JOINT_PID_TREE_AUDIT.md\` (Opus-reviewed). Its "ordinary prime moduli" Variant is a gap, not a result.` Replace it
  with:
  `… (Opus-reviewed). Its non-PID "ordinary prime moduli" Variant is CONDITIONAL (assembly of LOGIC_ADAPTIVE_SPARSE_NR.md +
  LOGIC_CIRCLE_ORDINARY_AUDIT.md owed). In separate Bézout (non-PID) models, universal NR holds even with standard prime
  moduli, and QR_std fails (LOGIC_UNIVERSAL_NR_AUDIT.md, LOGIC_STANDARD_PRIME_SIGNS.md; Opus-reviewed).`
  This adds one line, which keeps the item within 6 lines.
* **WAVES.md**, z74 `R` line. Current: `The joint note's ordinary-prime NR Variant is a GAP. Other z74 items are not
  cross-reviewed.` Replace with: `The joint note's ordinary-prime NR Variant is CONDITIONAL (assembly owed). The NR-model
  notes are ACCEPT/ACCEPT-WITH-FIXES (REVIEW_NRMODELS_OPUS.md). Other z74 items are not cross-reviewed.`
* **FRONTIER.md**, Z65 paragraph. Current: `a natural true principle that kills every arc counter-model is the non-residue
  certificate NR.` Rewrite in place: `NR kills every arc counter-model, but not descent countermodels. Universal NR holds in
  the z73–z74 PID and Bézout countermodels (LOGIC_JOINT_NR_TS.md; with standard moduli LOGIC_UNIVERSAL_NR_AUDIT.md) (z74).`
* FRONTIER "Post-z73 result" paragraph. After `its ordinary-prime NR Variant is a gap`, add: `(an unassembled conditional
  sketch; see REVIEW_NRMODELS_OPUS.md)`.

## 7. Verdict
All eight notes are mathematically sound within their stated scopes. The central new facts are robust, and I re-derived
each of them:
* the compressed-modulus count `O(N^{4/5+ε})`;
* that a non-square sparse sign profile delivers **universal NR with standard prime moduli** in an IOpen + Bézout + Dirichlet
  model with ¬ES(P) (UN, SP);
* that the one-prime profile provably **fails** universal NR (AR5);
* that the norm-base model fails universal TS (NB5).

None of this bears on ES in ℕ, which remains OPEN. The only open combination in this lane is the non-PID joint model. Its
two halves check out, but it remains CONDITIONAL until someone writes the assembly.
