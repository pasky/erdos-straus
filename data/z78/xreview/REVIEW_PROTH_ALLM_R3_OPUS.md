# Hostile cross-lab review, round 3: `notes/z78/PROTH_ALLM.md` §§9–11 and `lean/ES/ES/ProthCore.lean`

Reviewer: Claude Opus subagent (Anthropic). I have not set any model ID beyond that. Author lane: OpenAI.
Range: `git log f8b8d29ee..3a2817d96`, which is fbf83186d, 861aa62ac, f02c385e7, 3630bf655, the merge 82ab3d770, and 3a2817d96.
No master files were edited and nothing was committed.

**Verdict: ACCEPT. Nothing is blocking; there are some minor form fixes (§5).** I re-derived every mathematical claim in §§9–11 by hand. I wrote two
independent replays, both fresh code with no author helpers on the checking side. The Lean package compiled in a fresh build. Nothing claims all h,
or all exponents beyond m≤10, apart from the already-known k=63, which is now Lean-checked.

## 1. §9 mechanism table (CERTIFIED, exact finite)
* `/tmp/opusr3/mech.py` is my own classifier. For each m it computes ord_h(2) by brute-force powering, tests −1∈⟨2⟩, and tests the divisors a≥4 of h+1
  with −a∈⟨2⟩. It reproduces every TSV row: h, ord, minus_in_orbit and kind, plus a and b for II. The counts are I 45, II 5, §6 3∤h 36, 3∥h 29 and
  9|h 15, for a total of 130 = |{2..131}|. The note's five table rows match the script output string-for-string. The committed TSV is identical to a
  regenerated one.
* For each II row (18:6, 25:5, 39:6, 102:6, 123:6) I checked the Theorem 8 telescope on the full H:
  2^a∏_{i<b}B_{2^i} ≡ 1−2^a. I also checked that (2^a−1)|k, that c≡1 mod 16, and that −1/c ≡ 1−2^a.
* The 9|h rows are exactly m=(9t+1)/2 for t=1,3,…,29. The claim about h=2^q−1 (3-free, ord=q odd) holds for q=3..29, and the argument is a
  correct hand proof. The Jacobi remark is also correct: H≡7 mod 12 gives (3/H)=−1, so in a cyclic group ⟨3⟩ has even order and contains −1. It
  applies at least to the §6 rows m=4, 16, 45 and 64 (H prime).
* Form: the ord_15 example has 3|h, so mechanism I is excluded for that reason anyway. The ord_35 example is the one that actually illustrates
  the point. This is harmless.

## 2. §10 Lemma 10, the norm test, and h=729
* **Lemma 10, re-derived.** gcd(M,N)|3 because N≡3 mod M, and 3∤M because d is odd.
  * At N: (1+2w)(1+2w²)=1+2(w+w²)+4=3 and (1+2w)²=1+4(w+w²)=−3.
  * Hence B₁²/(B_{1+d}B_{1+2d}) = (1,3) and (B_{1+d}/B₁)² = (1,−1/3). All four of these indices are units because d≡0 mod 3.
  * ord_{3^j}(2)=2d, so g^{2d}=1 via the §6 orbit telescope, which uses gcd(2^a−1,H)=1 for (a,h)=1. The bound gcd(2d, ord_M 3) follows.
  * I numerically confirmed (1,3), (1,−1/3), N-coordinate(W_a)=1 and M-coordinate(W_a)=X_a at h=729.
* **Norm test.** ∏_i(1+xw^i)=1+x³ is correct. W_a/W₁ = ∏_r B_{a+rd}/B_{1+rd} · B₃/B_{3a}.
  * Each pair has equal gcd: 1 for the first three ratios and 3 for the last, since 3∤a. The note is explicit that this is U extended by the
    gcd-3 orbit and not the unit-only conjecture. Good.
* **Sufficiency of 3⁶.** 2^d≡−1 (mod h), d≡3 (mod 6), so −1/(9B_m) = 2·∏(B_{2^i}/B₁)·(3⁶)^{(d−3)/6}·B₁/B_m.
  * In the unit quotient, g⁶=1 is exactly the condition for this c, because gcd(d−3,2d)=6. This is consistent with the §8 Assessment.
  * Realization: (1+X^{3ℓ})/(1+X³) = Φ_{2ℓ}Φ_{6ℓ} with fresh ℓ. These are disjoint from Φ₂ and Φ₆ (used once, product 9 at X≡2) and from the
    unit-ratio primes. The degree contains a single 3, so the construction needs 3|s.
  * For 3∤s: k≡1 mod 7 gives n≡3 or 5 mod 7, and CONJS_GEN Thm 2 then gives (S). So the density-one claim holds. c=2^m+1 divides k, and
    c≡1≡7u−1 mod 16.
* **Certificate.**
  * Author checker: `z78_proth_tower_check.py` passes.
  * Independent replay: `/tmp/opusr3/tower.py` uses a different code path. It builds W_a from B's explicitly, with no ratio helper, and checks the
    CRT coordinates. It confirms that all 161 multiplicities are positive (up to 49 digits), that ∏(W_a/W₁)^{e_a}·y⁶ ≡ 3⁶ on the full H=2^729−1,
    and that the full assembly ≡ −1. It also audits every gcd.
  * These multiplicities each require that many distinct fresh primes. The result is asymptotic, as in §6.
* **Beyond.** The author's discovery `solve(j)` plus my independent full-H check succeed for j=3, 4, 5 (5, 17 and 53 entries), and j=2 is
  trivial (3⁶≡1 mod 7). These m=14, 41, 122 were already covered by §6, so this only shows consistency (EVIDENCE). j=7 needs the factorization of
  M=2^729−1 and was not attempted. Nothing in the note claims j≥7.
* Bug (cosmetic): `z78_proth_tower.py` crashes at j=2 (`pow(Z,-1,0)` with om=0). It should special-case the empty product.

## 3. §11 Lean
* **Fresh build.** I used a new `.lake`, symlinked only `.lake/packages` to worktree 0051, and ran the mandatory
  `systemd-run --user --scope -p MemoryMax=16G timeout 1800 sh -c 'lake exe cache get && lake build'` with no ulimit.
  * Every ES module shows **Built** (none Replayed). The result is `Build completed successfully (8932 jobs)`, EXIT 0.
  * Full log: `data/z78/lean/proth_core_opus_build.txt`.
  * Environment note: `lake` is not on the sandbox PATH. A first attempt failed with `lake: not found` (exit 127). I reran with
    `PATH=$HOME/.elan/bin:$PATH` passed via `--setenv`; the log file holds that second run.
  * The author's own log `proth_core_build.txt` is incremental: other modules show "Replayed".
* **Axioms.** `proth_four_pow_core`, `core_four_pow`, `core_of_doubling`, `telescoping_*` and `proth63` use [propext, Classical.choice, Quot.sound].
  `es_of_word` uses [propext, Quot.sound]. A grep finds no `sorry`, `native_decide`, `admit` or `axiom`. ES.lean imports ES.ProthCore.
* **Statements, checked against `ESProp` (`4xyz = n(xy+yz+zx)` with x,y,z>0).**
  * `Core h` is ∃P>0 ∀s>0, P|s → InteriorGoodWord ∧ ESProp at n=(2(2^h−1)+1)2^s+1.
  * `core_of_doubling` needs h≥5, h odd, 3∤h and h|2^b+1. These are exactly the note's hypotheses.
  * `proth_four_pow_core` matches its §11 statement verbatim, with k=2^{h+1}−1.
  * `proth63` proves ∀s, ESProp(63·2^s+1).
* **Proof audit.**
  * `Reach`/`extend` use divisibility chains X^E+1 | X^{Ed}+1 | X^{Edf}+1, so no coprimality or "distinct factors" bookkeeping is needed.
  * The value mod H uses 2^h≡1. The mod-16 value is 1 because X≡0 mod 16.
  * `periodic_divisor` uses P=4E(2h)!: an odd steering d≤2h divides (2h)! and hence the odd part. That gives r≡1 mod h, r≥4, and s=rEq with q
    odd.
  * `word_of_core_divisor` gives t≡v≡7 mod 8.
  * `proth63`:
    * The 18 fixed polynomial triples are checked by `ring`.
    * Coverage uses kernel `decide`, not native.
    * The period 2^{2523}≡2^3 mod modulus63 is `decide`d (8 ∥ modulus63 is consistent with the +3 shift).
    * The cubic on 24|s uses 256²≡256 mod 340.
* **Scope.** The Lean only uses 8|n+t as a sufficient goodness condition. It does not touch density, noncovering, §4, §7 or §10, and §11 says so.
  The STATUS §1C wording already restricts Lean to k=3 and 15, so "new formalization" of k=63 is accurate. Note that STATUS line 29
  ("Lean `15·2^s+1` + `(4^m−1)2^s+1` (1≤m≤6)") is pre-existing and ambiguous. It is not part of this change, but should be disambiguated at export.

## 4. Challenges considered and rejected
* *Is h=729 secretly covered by I/II?* No: 3|h, and both mechanisms need 3∤h.
* *Does it duplicate §6?* No: §6 stops at h=261.
* *Does "PROVED" on m=365 rely on unverified factoring?* No: the checker uses only the full-H identity. Factoring of M is used only in discovery.
* *Could negative exponents hide in the certificate?* No. All e_a>0, and inverse ratios are converted via finite order, as §4 states.
* *Is −1 actually used with c a proper divisor?* Yes: c=B_m=2^m+1 divides k=(2^m−1)(2^m+1).

## 5. Required and recommended fixes, all non-blocking form fixes
1. **§0 Review:** add this file and the Opus fresh-build log `data/z78/lean/proth_core_opus_build.txt` when exporting.
2. **§0 Label:** change "§10 computer-assisted for h=729" to "…, rel. Dirichlet/Mertens in progressions and CONJS_GEN Thm 2, as §6". The density
   and 3∤s parts use these inputs.
3. **§0 Result:** the parenthetical "(the doubling-orbit core ES theorem is Lean-checked)" sits next to "density-one exponents". It should say
   "(ES on the §1 core progressions is Lean-checked; density/noncovering are not)".
4. **§11:** change "arithmetic sign condition" to "the sufficient dyadic condition 8|n+t". Cite the fresh Opus build alongside the author's
   incremental log.
5. **Triage:** §11 is a formalization of already-PROVED results plus the known k=63. Its STATUS impact is the Lean column of §1C, not a RECORD.
   §9 is DATA.
6. **§10:** change "positive multiplicities modulo the old layer" to "positive exponents, reduced modulo exp((Z/M)^×) in discovery; the identity is
   checked mod H".
7. **Optional:**
   * Make the §8 Assessment point forward to §10.
   * In §9, write "Every h≤261 and h=729 passes".
   * Guard j=2 in `z78_proth_tower.py`.
