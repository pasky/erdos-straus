# Hostile cross-lab review of `notes/z80/PROTH_CORE.md` Round 2 (§§4–7), commit 233394a8d

**Reviewer:** Claude Opus (Anthropic), signed below. **Author:** GPT-6.2 Astra lane (OpenAI). This is the cross-lab review that §0 lists as owed for Round 2.
**Scope:** every change in `git log 31238fe3d..` (the single commit 233394a8d). That covers the note's §0 edits and §§4–7; `scripts/z80_proth_r2.py`; `data/z80/proth/r2/{cover-11,transfer}.json` and `replay.txt`; `lean/ES/ES/ProthFiveTower.lean` with its `ES.lean` import; and `data/z80/lean/five-build.log`. §§1–3 were reviewed in `REVIEW_PROTH_CORE_OPUS.md` and are not re-reviewed here.

## Verdict: ACCEPT WITH MINOR REVISIONS

* **Correctness.** I found no mathematical error in Theorems 6–11, the primitive-layer refinement or the Lean file. Every step was re-derived by hand (§2). Brute force with independent code agrees everywhere (§3).
* **Revisions concern framing.**
  * Two "theorems" draw their ES content from the classical rule "n has a divisor ≡3 mod 4 ⇒ ES", not from anything new. These are the gcd rule of Thm 9 and the ES content of Thm 11.
  * Theorem 11's "density one" converges at a practically vacuous rate.
  * §0 Label, Triage and STATUS delta were not updated properly for Round 2.
  * The replay script overstates what it tests.
  * Several sentences are garbled or understate hypotheses.
* **ES claim.** Nothing here is, or is presented as, a proof of ES or of ES for all large primes. No CLAIMED flag is needed.

Proposed triage for Round 2:
* Thm 9 (first sentence): RECORD-minor, i.e. a refinement of the Thm 4 zero class on a sub-progression. It does **not** need a separate STATUS row.
* ε-part of Thm 9: DATA/NULL.
* Thms 6–8 and the primitive layer: DATA / BARRIER-SCOPED.
* Thm 10: NULL (an identity generalising Thm 5).
* Thm 11: METHOD/NULL.
* `core_five_tower`: DATA (formal specialisation).

---

## 1. Replays (author's command, assertions on, `ulimit -v 6000000`)

| command | result |
|---|---|
| `timeout 300 uv run --offline --no-project python -B scripts/z80_proth_r2.py` (repo root) | prints exactly `replay.txt`; exit 0; ≈1 s. Note: it must be run from the repo root. From `scripts/` it crashes on the relative path `data/z80/proth/indices.json`. |
| `cd lean/ES; systemd-run --user --scope -p MemoryMax=16G timeout 1500 lake env lean ES/ProthFiveTower.lean` | compiles in 3.8 s; `core_five_tower` depends on [propext, Classical.choice, Quot.sound]. No `sorry` or `native_decide`. The committed `five-build.log` shows the full 8935-job build succeeding. |

## 2. Hand verification, item by item

**Theorem 6 (formal quotient).** Correct.
* Write ℤ[S]=⊕_orbits ℤ[C_o]. Then (σ−1)ℤ[S]=⊕I_C, and I/⊕I_C≅ℤ^{t−1} via orbit sums of total zero.
* ⊕I_C/(σ−1)I ≅ ℤ[S]/(I+ker(σ−1)). Here ker(σ−1) is spanned by the orbit norms, each of augmentation o, so this quotient is ℤ/o. The extension splits because ℤ^{t−1} is free.
* The author's "phase" map Σ i·v_{σ^iC} kills (σ−1)I. For v=(σ−1)y the phase is Σy=aug(y) mod o, and the wrap term carries the coefficient o.
* The specialisation steps are all right:
  * D₁=1;
  * B₃/B₁=3=B₁ when 3∤h, so every unit-index B_a lies in R₁;
  * B₁/B₋₁=2;
  * D_{−a}=−2^{−a}D_a.
* *Wording:* "In particular C=R₁ in the transitive case" silently needs 3∤h. The data show this hypothesis is essential: [C:R₁]=6 at h=9,27 and 2 at h=3, all transitive. Restate the hypothesis in that sentence.

**Primitive layer.** Correct.
* p∤Φ_{p^j}(2), since Φ_p(2^{p^{j−1}})≡Φ_p(2)≡1 mod p. So every prime of N has ord(2)=p^j, and the root differences are units. The product identity for B_{p^v b} therefore holds at prime powers, by Hensel/unit-difference factorisation.
* Hence proj R_h = proj R₁ at N (R₁ ∋ B_a needs 3∤h, which holds for p≥5; say so).
* For 7^j and 23^j: ord_{49}(2)=21 and ord_{529}(2)=253 (2¹¹≡461 mod 529). So ord is odd, S=±Q, and the displayed identity p=−2^{−ΣQ}(∏_Q D_a)² is right: Φ_h(1)=p, φ(h) is even, and |Q| is odd.
* "By Theorem 1 it *suffices* …": by Theorem 1 and this paragraph it is in fact an **iff**. −1∈R_{p^j} iff p∈proj_{N_i}R₁^{(p^i)} for every i≤j. Say "iff".
* "This odd norm follows because …" is garbled. It means the product over the p^v lifts.

**Theorem 7.** Correct.
* Equal gcd at h implies equal gcd at d. The lift of a mod d with gcd g via units mod h/g is right.
* 2=B₁/B₋₁∈R_h, so 2^d∈R_h. By LTE ord_{q^E}(2^d)=q^{E−e}, the kernel of U(A)→U(M) is cyclic of order A/M, and 2^d generates it.
* The global index formula [G:R]=[U(A):π_A R]·[U(J):R∩(1×U(J))] is standard.
* The quoted special cases check out:
  * v₇(2^h−1)=1+v₇(h) for 3|h;
  * v₇₃(2^h−1)=1+v₇₃(h) for 9|h;
  * [U(7):R₃]=2 (R₃=⟨2⟩);
  * [U(511):R₉]=6.

**Theorem 8.** Correct.
* gcd(M,N)=gcd(M,p)=1. Also p∤N: if ord_p(2)∤d then N≡1 mod p.
* The p lifts a+td cover every class mod p exactly once, so gcd multisets match. gcd(pa,h)=p·gcd(a,d).
* At N, w=2^d is a primitive p-th root at every prime. The chain ∏V_i^{p^{f−1−i}}=(r^{p^f−1},1) closes because p^f a≡a mod d.
* Inverting p^f−1 on ℓ-primary parts with ℓ∤p^f−1, then cancelling, gives the splitting.
* *Overstatement in the Assessment:* "At squarefree conductors even the inter-layer coupling cannot just be dropped: the cyclic chain loses p^f−1." This is a loss **of the proof method**, not a demonstrated coupling. In all 55 Thm-8 instances I computed (h≤151), the split defect [π_M R×π_N R:R] is exactly 1 (§3). Reword it as a method limitation, and quote that the data contain no example of nontrivial coupling.

**Theorem 9 (refined cover + ε-statement).** Correct.
* *Cover.* T′=3T is genuinely needed: one K row (P=234360, odd test modulus 1005051599559) fails 4^T≡1 but passes 4^{3T}≡1. Small s<64 transfer because T|T′.
* *gcd rule.* g|2m+1 and g|s−1 give 2^{2m+s}≡1 and 2^s≡2 mod 2^g−1, so q|n with q≡3 mod 4, and the triple is right.
  * **But this is exactly the classical "divisor ≡3 mod 4 ⇒ ES" rule (the D-row mechanism) with the divisor 2^g−1.** Say so. It is not a new ES mechanism.
* *ε-construction.* I re-derived each step:
  * a≡5 mod 8 ⇒ v₂(ord_a 2)=2;
  * gcd(o,O′)=4: odd primes of O′ avoid a−1. For primes of M∩O this is the gcd(z−1,gcd(M,O))=1 check; for ℓ∈S, ℓ∤3+2¹⁴; at the remaining primes, a≡2. Primes ℓ′|ℓ−1 that lie in M are not in D;
  * b≡14 mod O′ and b≡o/2 mod o are compatible mod 4;
  * h≡21 mod 2T′ ⇒ m≡11 mod T′ and 3∥h (9|T′);
  * ℓ|2m+1 via h≡−2 mod ℓ;
  * ℓ∤L, so s≡1 mod ℓ meets L|s with relative probability 1/ℓ, independently by CRT;
  * z79 Thm 2 Test 2 applies (a≥4, a|h+1, 2^b≡−a mod h, L=2 divides b, (d,6)=1, j=1, h≥9), with density one on every fixed progression.
* *Simplification:* gcd(M,z−1)=1 outright (my check). So D=1 and the whole "ℓ≡2 mod D / new orders introduce no prime of D" clause is vacuous. Replace it with the checked fact.
* *Value:* z79 Thm 2 already gives density-one good words, hence ES, on L|s for these m. The ε-part therefore upgrades "density one" only to "periodic coverage >1−ε", with a positive-density periodic remainder that always contains 0 mod lcm(2m+1,L). The note says this. It is not STATUS material (see Fix 1).

**Theorem 10.** Correct, and elementary.
* n+u=kz^e=A·v and t=(A+1)/u give the word.
* z is odd, so n≡1 mod 8 for even e.
* z≡−k mod 4 gives tv≡−3≡1 mod 4. The triple (ADn,uD,AuD) satisfies 4AD=1+nt.
* The phrase "choose z=−1 at odd p|u" is misleading: z=tu−1≡−1 mod u is *forced*. Only the other primes are a choice.

**Theorem 11.** Correct.
* 97 has order 2 mod 112. Take the odd-part power of a lift. A 2-element acting on an odd set fixes a point. Chebotarev supplies a positive-density set of q≡97 (112) with a root. Then CRT independence, Chebyshev, and v≡t≡7 mod 8.
* The prime-parameter variant (omit q|F(0)+14, probabilities 1/(q−1), PNT in fixed APs) is fine.
* Sanity check: if G|P²+14 had odd degree, a real root α would give P(α)²=−14. So the hypothesis automatically excludes square polynomial values, consistent with (−14/q)=−1.
* **Substantive caveats that the note must state:**
  1. **ES content is classical/trivial.** The same Chebotarev argument with −1∈(ℤ/4)^× gives, for every odd-degree F, primes q≡3 mod 4 dividing F(x) for density-one x, hence ES by the 3-mod-4 divisor rule, with **no** congruence restriction on F(x). For F=840X+1 it is classical that ES holds on a density-one subset of n≡1 mod 840 (Vaughan 1970). Even more crudely, Landau shows that integers with no prime factor ≡3 mod 4 have density 0. Only the **fixed word shape** (outer letter 14, prime A≡97 mod 112) is new. The Assessment phrase "a set of n of lower density 1/840 there in the integers" should be replaced by this comparison, and the sentence is garbled anyway.
  2. **The rate is practically vacuous.** The q≡97 mod 112 primes with a root form roughly a 1/48·(1/deg-ish) share of all primes. The proportion of x missing every pool prime ≤Q decays like ∏(1−1/q) ≈ (log Q)^{−δ} with δ≈1/50–1/100. Empirically (§3), with pool q≤4000 the hit share is 1–4% of x<6000; the trivial 3-mod-4 rule with divisors <2000 hits 37–65%. This is not an error, but "relative density one" should carry the remark "with exceptional proportion ≍(log x)^{−δ}, δ small", or similar.

**Lean (`core_five_tower`).**
* `five_lift` correctly proves 5^{i+1}∣2^{2·5^i}+1. The witness polynomial is the (5ac−1)⁵+1 expansion.
* `core_of_doubling` needs h≥5, odd, coprime to 3 and h∣2^b+1, all discharged.
* `Core h` uses u=2(2^h−1), so the multiplier is 4^m−1 with m=(5^{i+1}+1)/2. It is a core-progression statement, not all-s. The scope sentence in §4 is accurate and honest ("not new mathematical scope").

## 3. Independent checks (reviewer code in this directory; no repository script imported; PARI only for factoring, discrete logs, SNF/HNF, znorder and kronecker)

* **`opus_r2_groups.py 151` → `opus_r2_groups_151.out`** (≈30 min, < 100 MB). Group model: full discrete logs in every cyclic block of U(2^h−1), with the index taken as the HNF determinant.
  * (T6) Smith normal form of I/(σ−1)I equals ℤ^{t−1}⊕ℤ/o for **all** odd 3≤h≤151.
  * Specialisation, for 70 odd h≤151 (timeouts at 107, 121, 131, 139, 145):
    * 3∤h: [C:R₁]=1 in all 45 cases, including t=3,4,6 orbits. This is **stronger than proved**: the ±⟨2⟩ bound of 2 is never attained, and the free part always dies.
    * 3|h: [C:R₁] is 2 (17 cases) or 6 (8 cases).
    * In every case R₁ contains 3 and 2 whenever 3∤h.
  * (PL) 34 pure prime-power layers with p≥5: proj R_h = proj R₁ at Φ_h(2) in all of them, with [C_N:projR₁]=1 and [U(N):projR_h]=1. This includes 5, 25, 125, 7, 49 and 23. "7∈projR₁ ⇔ −1∈projR₁" was tested in the claimed S=±⟨2⟩ case. Both memberships are in fact true at every tested layer.
  * (T7) 94 (h,d) pairs: [U(A):im R_h]=[U(M):R_d] and ord_A(2^d)=A/M in all.
  * (T8) 55 instances: the split defect is 1 every time.
* **`opus_r2_cover.py` → `opus_r2_cover.out`** (< 1 s, 48 MB).
  * (1) Coverage by a different algorithm, a CRT-fibre sieve with L=3825360·130169. The rows with P|3825360 leave exactly one fibre (0 mod 3825360). The ℤ/130169 sieve on it leaves exactly {0}. **Uncovered residues mod L = [0]**, and no row contains 0.
  * (2) Every row re-checked from first principles at m=11, 11+T′ and 11+2T′, using n mod the row's own modulus:
    * Mordell's six classes are listed by hand;
    * W rows use the **actual Jacobi symbol (A/n)=−1** rather than the 8|(n+t)tuv proxy;
    * K/II/D rows are reduced mod Q.
    There are 0 failures.
  * (3) Actual integers: 1200 real triples or real Jacobi signs at s≥64. These are taken at m=11 and at m=11+ord(4 mod Q_odd) when that order is ≤2500 (111 rows); 67 rows were tested only at m=11.
  * (4) gcd rule: 42 920 real triples for m≤150, s≤1500. Side conditions: 36|T′, 23|T′, 23|L, 4|O, 2^O≡1 mod M, gcd(z,M)=gcd(z−1,gcd(M,O))=1, and also gcd(z−1,M)=1 (D=1).
* **`opus_r2_poly.py` → `opus_r2_poly.out`.**
  * (10) 40 000 cases (odd k≤201, t≤400, even e≤16): identity, real triple, nonsquare, and actual Jacobi (z/n)=−1. Odd e=3 control: the sign fails in 90/190.
  * (11) Five admissible F, including a non-monomial odd cubic and an even-degree F with an odd factor of F+14: roots exist for a positive share of q≡97 (112), and every hit gives a real word, Jacobi −1 and a real triple. Controls (8x+1)², 840x²+1 and 840x⁴+1: zero roots, as reciprocity predicts. The rate comparison with the trivial 3-mod-4 rule is as in §2.
* **Not independently replayed.** The ε-construction cannot be instantiated: computing ord_a(2) needs a factorisation of a−1 for a ~600-digit prime a. I verified it by hand and checked every finite side condition. The checks run on the same machine as the author's, but with fully independent code.

## 4. Form and process findings

1. **§0 Triage was not updated** for Round 2. Add the classes proposed above.
2. **§0 Label "Round 2 additionally uses LTE, Dirichlet–Mertens, Chebotarev…"** LTE is elementary and not a "rel." item. The real external dependencies are missing: z79 Thm 2 Test 2 with its density theorem (for Thm 9), and PNT in APs (for Thm 11). The per-theorem labels are fine.
3. **STATUS delta:** I recommend **no STATUS change for Round 2**. By the AGENTS §3 test, a number theorist who reads only STATUS misses nothing important:
   * the modulus refinement 3825360→L applies on a sub-progression and still leaves L|s;
   * the ε-coverage is weaker in density terms than the existing density-one result.
   At most, add a parenthetical to the Thm 4 row.
4. **Replay overstatement.** `scripts/z80_proth_r2.py` computes **no** index, although the replay line reads "formal and evaluated orbit … tests":
   * `orbit()`'s `solve` is only fed vectors that are (σ−1)(e_a−e_c) by construction, so it is tautological and never tests the ℤ/o torsion;
   * `old()` checks the kernel order and lift existence, not the index equality;
   * `primitive()` checks identities only.
   The proofs do not depend on it. Still, reword the Falsifiers/replay paragraph ("identity and side-condition checks; no index computation"), or cite this review's index checks. The script should also resolve paths relative to `__file__`.
5. **Garbled or underspecified sentences** (fix):
   * "This odd norm follows because …" (§4);
   * "it suffices" should be "iff" (§4);
   * "In particular C=R₁ in the transitive case" needs the explicit 3∤h hypothesis;
   * "hence a set of n of lower density 1/840 there in the integers" (§7);
   * "choose z=−1 at odd p|u" is forced, not chosen (Thm 10).
6. **Notation clash.** L is the 3-power period in z79 Thm 2 and the period 497943285840 in Thm 9. Both appear in the Thm 9 proof chain, so rename one (e.g. 𝓛 or P₉). Similarly S denotes both (ℤ/h)^× and the prime set in §6, and T′ reuses T.
7. **Observation worth recording (EVIDENCE, not claim).** For 3∤h the data give C=R₁ in every case through h≤151, and at every tested 7-, 23- and 49-layer both −1 and p lie in proj R₁. If this can be proved (a circular-unit relation that kills the free ℤ^{t−1} after specialisation), it would settle the "second factor" uniformly. The note's Assessment should mention that the bound of 2 is never attained in the data.

## 5. Recommended fixes (all minor)

1. §0: add the Round 2 triage. Correct the Label's dependency list (z79 Thm 2, PNT in APs). Drop the Round 2 STATUS delta, or reduce it to a parenthetical.
2. Thm 9: identify the gcd rule as the classical 3-mod-4-divisor rule with q=2^g−1. Replace the D-clause by "gcd(M,z−1)=1 (checked), so no congruence on ℓ is needed beyond ℓ∤2LMO(2+2¹⁴)(3+2¹⁴)". Add this check to the replay.
3. Thm 11 / Assessment: state that the ES conclusion (as opposed to the word shape) already follows from the 3-mod-4 rule, or from Vaughan for linear F. Add the (log x)^{−δ} rate caveat. Rewrite the "lower density 1/840" sentence.
4. Thm 8 Assessment: present the p^f−1 loss as a limitation of the method, and record that the split defect was 1 in all 55 computed cases.
5. §4: "suffices" → "iff"; state 3∤h explicitly in the C=R₁ and "already belong to R₁" sentences; fix the "odd norm" sentence.
6. Replay: reword what `z80_proth_r2.py` certifies (no index computations; `orbit()` solve is tautological). Make paths independent of the working directory.
7. Rename the clashing symbols L, S and T′.

None of these affects the truth of any stated result. Round 2 may be marked cross-reviewed once the fixes are applied.

— Claude Opus (Anthropic), hostile cross-lab reviewer, Round 2 of `notes/z80/PROTH_CORE.md`, commit 233394a8d.
