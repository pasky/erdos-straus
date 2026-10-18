# AGENT REPORT O276 — the k-th power relaxation ladder (POWER_LADDER_ES.md)

**ES is not solved. Nothing here proves ES or an infinite case of ES.** Branch side-agent/power-ladder-es (merged O274's
side-agent/lower-tail-fable first, as instructed).

## SHARP:
1. **The k-ladder is flat: it carries exactly one bit, k mod 2 (PROVED, elementary).** With the exact definition
   ES_(k)(n): 4/n = 1/x + 1/y + Q^k/Z, gcd(Q, Z) = 1, Q odd, gcd(Q, n) = 1 (lowest terms is forced — Remark 1.2):
   * odd k: 4/n = 1/(2x) + 1/(2x) + Q^k/(nx), 4x = n + Q^k, Q ≡ −n (mod 4) — a finite congruence covering, Q ∈ {1, 3}
     for every prime; T1 is DEAD (odd squares and cubes solved with Type I shape). ES_{Q³} is a theorem for a trivial reason.
   * even k: ES^□ again — one Dirichlet prime r ≡ 3 (4), (n/r) = −1, r ≢ 1 mod the odd primes of k; T1 intact.
   * every rung holds at every n ≥ 2 (scaling; incidentally ES^□ holds at all odd n > 1, the ledger's "non-square" is
     the scope of the Type II-shaped construction). No rung lies "strictly between ES^□ and ES" in difficulty.
   * **Repair of LOWER_TAIL_FABLE §3.2 (O274):** its conclusion "only k = 2 is provable; k ≥ 3 needs equidistribution"
     is wrong. Index calibration must be done at the best SINGLE modulus the relaxation lets the solver choose
     (index gcd(k, g − 1): 1 for odd k, 2 for even k), not in a pooled (ℤ/4U)^× (POWER_LADDER §3, Prop 3.1).
2. **One mute prime: parity is the whole gap between a covering and Artin (PROVED per q; CERTIFIED q ≤ 10⁶).** With den z
   any power of a single prime q, a witness g ≡ 3 (4) with q primitive root (or q ≡ 3 (4), or q ≡ 2 (3)) gives a finite
   covering for all n prime to q; every q ≤ 10⁶ has one (g ≤ 179). With even exponents (ES^{({q})}) the same shot needs
   (n/g) = −1 on top of Artin — open (Thm 5.1, Prop 5.2).
3. **Order-3 variant separates T1's order from the shot index (PROVED bits + EVIDENCE).** For TES over ℤ[ω]: T1₃ ⟺ 3 | k,
   index even ⟺ 2 | k. Fixed g = −8 + ω (norm 73): k = 1 fires 412/412 primes and 412/412 cubes; k = 2: 209/412 and
   209/412; k = 3: 134/412 primes, 0/412 cubes. TES_(2) is T1-free yet no finite set of fixed shots covers it — so
   "no T1 ⟹ covering" fails inside shot families once ord(T1) ≠ 2. ES's ladder is flat because ord(T1) = 2 = the
   unavoidable 2-part of every shot index (g ≡ 3 (4)): a coincidence of the prime 2.

## Answers to the task items
1. ES_{Q³} pointwise: YES for every n ≥ 2, but by a mod-4 identity, not cubic reciprocity (cubes are bijective on (ℤ/4)^×,
   (ℤ/3)^×, F_g^× for g ≡ 2 (3); every ES-type shot prime g ≡ −1 (mod 4M) with 3 | M has g ≡ 2 (3), so cubic symbols
   are invisible over ℤ — Remark 3.2). Headline candidate: withdrawn (true but trivial).
2. Pooled counting: moot; exact index formula [G : G^k] = gcd(k,2)∏gcd(k, ℓ−1) (Prop 3.1); the relevant index is the
   single-modulus one.
3. Caps: ES_(k) is NOT a bounded-cap special case (constructions have rad Q ∤ y; the cap's rad | y tie is what the ladder
   drops); ES^{(y,e)} ⊂ ES_(2). Gradients that do interpolate (box, fixed S, cap, band) are orthogonal to k (§4).
4. Numerics (`scripts/z44_ladder.py 1000000`, 8 s): all 78 496 primes ≤ 10⁶ for k = 3, 5 (Q ≤ 3, Type I) and k = 2, 4, 6
   (max r = 131, 131, 251; Type II), exact; all 499 odd squares and 49 odd cubes ≤ 10⁶ solved for k = 3, 5; 0 shots at
   odd squares for k = 2, 4, 6; numerator 8 at 131, 241 solved for k = 2, 3, 4, 5 (explicit in §2.3). The least
   certificate over ALL solutions is trivially Q = 1 (ES ⊂ ES_(k), ES known to 10¹⁷), so only mechanism-level
   comparisons are meaningful (ES's own Q = 1 shot fails at 9 841 primes p ≡ 1 (4) ≤ 10⁶).

## Files
POWER_LADDER_ES.md (§0–§6); BRAINSTORM/z44_parity_collapse.md, z44_one_mute_odd.md, z44_tes_ladder.md,
z44_neutral_odd_mute.md (README indexed); scripts/z44_ladder.py, z44_one_mute.py, z44_tes_ladder.py; logs/z44_*.txt.
Labels: §2 Thms PROVED; §5 Thm 5.1 PROVED per q / CERTIFIED / CONDITIONAL (GRH, Lenstra 1977, citation-level);
§6 bits PROVED, table EVIDENCE; all "Reading" paragraphs are Assessments. Only 4 memos (task asked ≥ 3): the core
question collapsed early, so I did not pad.

## Sparks (not pursued)
1. Is TES_(2) (T1-free, index 2 at every shot) covered by some NON-shot identity family over ℤ[ω], or is it the first
   known "T1-free but covering-free" ES-type variant? Either answer sharpens B5 (is B5 really "T1 ⟺ no covering"?).
2. Over ℤ: numerator-m variants with odd k and gcd(k, λ(m)) > 1 (e.g. 7/n, k = 3) — is there an ES-type variant over
   ℤ with no T1 whose shot indices are all ≥ 3? That would be the ℤ-analogue of spark 1.
3. The only informative rungs are inside ES^□ (box Q ≤ B, fixed S, cap). A clean invariant: B*(p) := min Q over the
   Prop-2.1 family with Q unrestricted vs. the least r(p) — R193 shows Q < r(p); is min Q ≍ r(p) or much smaller?
4. Function-field mirror of §6: over F_q[T] with q ≡ 1 (3), does the order-2/order-3 separation produce a variant whose
   ladder is 2-dimensional and fully computable (Bilharz replaces Artin)?
