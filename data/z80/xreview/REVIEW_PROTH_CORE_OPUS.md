# Hostile cross-lab review of `notes/z80/PROTH_CORE.md` (commit a5a956009)

**Reviewer:** Claude Opus (Anthropic). The author is the GPT-6.2 Astra lane (OpenAI). This counts as the cross-lab review the note lists as owed.
**Scope reviewed:** every commit in `git log main..`, i.e. a5a956009: the note, `scripts/z80_proth_{check,index,cover,last,masks}.py`, `data/z80/proth/*`, `lean/ES/ES/ProthQuadratic.lean` and the `ES.lean` import.
**Verdict: ACCEPT WITH MINOR REVISIONS.**
- All proof-relevant claims checked out: Theorems 1–5, the index census and the falsifier table.
- Every certificate replays, and my independent re-implementations agree.
- I found no mathematical error and no scope overclaim about ES.
- The revisions requested below concern labels, wording, STATUS bookkeeping and two stale comments.

Triage as proposed: Theorems 3 and 4 and the core-range extension are RECORD. My suggestion: Theorem 1 → BARRIER-SCOPED/DATA, Theorem 5 → NULL/METHOD (see §5).

---

## 1. Replays (author's commands, assertions on, `ulimit -v 6000000`)

| command | result | time / RSS |
|---|---|---|
| `python -B scripts/z80_proth_check.py` | output identical to `data/z80/proth/replay.txt` (30×64 direct triples; all-s covers for m=13..21 with the stated periods and row counts); exit 0 | 3.1 s / 35 MB |
| `--with cypari2 python -B scripts/z80_proth_index.py check` | `199 {2: 45, 1: 132, 6: 22}`; exit 0 | 4.3 s / 63 MB |
| `lake env lean ES/ProthQuadratic.lean` (cgroup 16G) | compiles; `quadratic_transfer` depends on axioms [propext, Classical.choice, Quot.sound]; no `sorry` or `native_decide` | — |

The committed `data/z80/lean/build.log` also shows `Built ES.ProthQuadratic` and the same axiom line.

## 2. Independent checks (reviewer code, no repository script imported)

The files are in `data/z80/xreview/`.

### `opus_indep_cover.py` (output in `opus_indep_cover.out`, 69 s, 2.5 GB peak)

I wrote this from the rule definitions in z77 `PROOF_S_WILD.md` §2 and the note. For m ∈ {11, 13..21} it checks the following.

1. **Every fixed row at its actual modulus.** I derive the modulus myself; for K rows it is `4fK₀` when a K/K₀ term is used, else `4·lcm(f,K₀)`. I check periodicity `k·2^{s₀}(2^P−1) ≡ 0 (mod M)` from the least representative s₀ ≥ 64. I then check the rule at n mod M, and the W size bound `k·2^64+1+u ≥ 2A`.
2. **An actual-integer box.** Every s in **[64, 1500]** hitting each row is tested on the unreduced n. That is about three times the author's [64, 512] box, with independent triple constructions:
   - **D:** a triple for q found by my own PARI-divisor search, then scaled. q reaches 2^41−1.
   - **II:** with d=(f+1)/4ab, b′=(bn+a)/f, the denominators are (ab′d, abdn, b′bdn).
   - **K:** the denominators are (y, ny(A+B)/(fA), ny(A+B)/(fB)).
   - **W:** I check the identity n=tuv−u−v, the sign condition 8 | (n+t)tuv, n ≡ 1 mod 4 and that n is not a square. When 4 | tv−1 or 4 | A, I also check an explicit triple; otherwise only the word criterion is checked.
   - **M:** n mod 840 lies outside the 6 unit squares.

   All passed. Per m there were about 1000–2000 Mordell (M) instances, a few hundred each of D/II/K triples, and roughly 500–1800 W instances, about a third of them with explicit triples.
3. **Exhaustive coverage, by a different algorithm.**
   - Periods ≤ 2·10⁹ (m=11, 13, 14, 16, 17, 19) use a direct bytearray over the whole period.
   - The others (m=15, 18, 20, 21) use a CRT tree that splits into all residues modulo lcm(b, P) of the compatible row with the fewest missing prime factors, rather than the author's one-prime split.
   - Results: complete for every m ∈ 13..21 (155, 16085, 1382 and 577 tree nodes for m=15, 18, 20, 21). **m=11 misses exactly the residue 0 mod 3825360.**
4. **X (mask) rows.**
   - *Modular check.* I evaluate Φ₂d(x) through Φ_d(−x) (a different Möbius formula), with a CRT point x₀ ≡ 0 (mod 16) and x₀ ≡ 2^a (mod H), at **every** unit source a mod h. All rows satisfy A ≡ 7u−1 (mod 8u).
   - *Actual integers (gmpy2).* At real exponents s = e·r·o, with r ≡ 0 mod 4, r ≡ a mod h, and o ∈ {1, smallest prime of h}, I build A = c·∏Φ₂d(2^r) exactly and check A | n+u, t ≡ v ≡ 7 (mod 8), the word, and the ES triple (ADn, uD, AuD).
   - Number of instances: 40 (m=13, all 20 sources), 36 (m=14, all 18 sources), 4 each for m=15..19 and 21, and 2 for m=20. The exponents range from s=41580 up to s≈2.3·10⁸, so n has as many as about 229 M bits.

### `opus_indep_groups.py` (outputs in `opus_indep_groups_a.out` and `opus_indep_groups_bc.out`)

- **(a) Full index by complete discrete logs + HNF.** There is no ℓ² truncation. I use PARI `znprimroot`/`znlog` per prime-power block with all diagonal relations, on the factorizations in `indices.json`. Result: **agreement for all 70 of 75 odd h in [3,151]**. The other five (107, 121, 131, 139, 145) were skipped on a 120 s discrete-log timeout, not because of any disagreement. This is an independent implementation check of the census. The author's truncated method needs no large-prime discrete logs, which is why it reaches h=399.
- **(b) Theorem 1, numerically.** For h = 9, 25, 27, 49, 81 the prime-to-p part of [G:R_h] equals the product over layers N_i of the prime-to-p parts of [G_i : π_i R_h]. The p=3 cases are informative: the 2-part sits on the layer N₁=7, while the **3-part does not split** (global 3 versus product 1). This matches the note's remark that the exponent is not invertible on the cubic obstruction, and confirms Theorem 1 cannot be stated for the full group. Larger h timed out in discrete logs and were dropped.
- **(c) Certificate files.**
  - `primary.json`: all 69 rows, h = 263..399, recomputed. Checked: −1 = c·3^{|T0|}·∏(B_a/B₁)^{e_a} mod H; c | k; c ≡ 1 (16); unit indices only; 3 ∈ T0 only if 3 | h.
  - `tower-7.json`: recomputed in two ways.
    - On M = 2^729−1 with X_a = B_a³/B_{3a}, ∏(X_a/X₁)^{e_a} = 729. That is, 3⁶ ∈ C₆.
    - On the full 2^2187−1, as an explicit list of ratios B_x/B_y whose gcds with h are equal (only gcds {1,3} occur), the product is 729.
  - Also checked: 2^729 ≡ −1 (mod 2187) and 729 ≡ 3 (mod 6).
- **(d) Theorem 5:** a 64×64 grid of words, triples and non-squareness.
- **(e) Theorem 4 transfer data.**
  - 4^T ≡ 1 modulo n_{11,s} for all 1 ≤ s < 64, and modulo the odd part of every cover-11 test modulus; every dyadic part is ≤ 2^64.
  - *Falsifier:* for transferred m = 11+iT (i = 1, 2, 3) the odd-square exponent s = 2m+2 is ≥ 64. It is hit **only by D rows**. A W, M or X row there would contradict the Jacobi criterion. Consistent.
- **Also checked:** the 81 non-X rows of z79 `period-11-3825360.json` miss exactly 28 residues, including 0. The 14 rows added in cover-11 close 27 of them, as the note says.

## 3. Line-by-line mathematics

### Theorem 1 (layer splitting): correct

I re-derived each step.

- **Pairwise-coprime layers.** N_i = Φ_{p^i}(2), and p ∤ 2^{p^i}−1 because 2^{p^i} ≡ 2 (mod p). So every prime of N_i has order exactly p^i.
- **Projection.** π_M(R_h) = R_d in both directions. For 1 ≤ a < d, v_p(a) < j−1, so gcd(a,h) = gcd(a,d). Conversely, gcd(a,h) = gcd(b,h) implies gcd(a mod d, d) = gcd(b mod d, d).
- **Legality of W_a/W_b.** v_p(a+td) = v_p(a) < j−1, and v_p(pa) ≤ j−1 < j.
- **N-coordinate.** N = Φ_p(2^d), so Z[ζ_p] → Z/N, ζ ↦ 2^d, is a ring map. Then ∏_t(1 + xζ^t) = 1 + x^p (p odd) holds modulo N, prime powers included. The note's "differences are units" reasoning is right; this is a cleaner way to see it.
- **M-coordinate.** It is r^p/r′.
- **Chain.** The p-valuation of the indices rises by one per step, and both indices reach 0 mod d at the same step because their valuations are equal. With X_i = (r_i^p/r_{i+1}, 1) and r_k = 1, the telescope ∏ X_i^{p^{k−1−i}} = (r^{p^k}, 1), with k ≤ j−1.
- **Primary decomposition.** Lift and cancel the old component, then induct.

The consequence for −1 (order 2, p odd) follows. *Form:*
- Place "Assume j≥2" before the M, N notation.
- Write the telescope explicitly.
- Say "y ∈ π_N(R_h)" instead of "the new-layer image".

*Substance:* wherever the census index is 1 (every 3 ∤ h ≤ 399) the theorem is vacuous for −1. Its content is to locate the obstruction (§0 calls it BARRIER-SCOPED), which is fine.

### Index census (CERTIFIED): method correct

- A single cyclic block with x^{L/ℓ} ≠ 1 has full ℓ-image.
- The generator g with g^{o/ℓ} ≠ 1 has full ℓ-part, so g^{o/m} has order exactly m.
- x ↦ x^{o/m} realizes G_ℓ/ℓ²G_ℓ.
- The HNF determinant with diagonal relations is |Q/ℓ²Q|. Since Q/ℓ²Q has order ℓ^{Σ min(a_i, 2)}, any value below ℓ² equals |Q|.
- Stopping early at index 1 is sound.
- Factorizations are checked by product and by PARI `isprime`, which is a proof (APRCL) and not a pseudoprime test.

**Requested:** per AGENTS.md §3, a CERTIFIED label must state the independent-check coverage. Add "independent full-discrete-log HNF agreement for 70 odd h ≤ 151 (Opus review)". The script docstring ("defect has length at most one… valuation one") is stale relative to the ℓ²-truncation code; fix it. The local symbol m=ℓ^{min(2,v)} in the note collides with the multiplier index m; rename it.

### Theorem 2 (cores for 263 ≤ h ≤ 399 and h = 2187): correct, relative to z78 §§4, 6, 10

- **primary.json** uses only unit-index ratios and slots T0 ⊆ {1,3}, with 3 only when 3 | h. So the z78 §6 density argument applies unchanged, including when 9 | h. The z79 restriction for j > 1 does not arise, because no gcd-3^i ratios with i ≥ 2 are used. The note could say this in one sentence, since a reader of z79 will ask.
- **h = 2187.**
  - The certificate proves 3⁶ ∈ C₆, the X-ratio group at 3⁶, mod 2^729−1, and 3⁶ ∈ U₇ on the full modulus.
  - The checker does not test V ≡ 3 (mod N) separately. It does not need to: A·V⁶ ≡ 729 (mod H) is the asserted membership.
  - 2^729 ≡ −1 (mod 3⁷) and 729 ≡ 3 (mod 6), so −1/(9c) costs (3⁶)^{(729−3)/6} times three single slots, exactly as in z78 §10.
  - Density uses gcd-3 ratios on 3 | s, and the mod-7 fallback on 3 ∤ s.
- **Bound 6·3^{j−7} for j ≥ 7.** Start the z79 §5 lossy X→X lift from 3⁶ ∈ C₆: 3^{6·3^{l−6}} ∈ C_l. Then one lossless X→U step gives 3^{6·3^{j−7}} ∈ U_j. This is correct and improves z79's 6·3^{j−6} by a factor 3. *Form:* say explicitly that the anchor used is the M-projection (C₆), since the sentence currently reads as if it starts from U₇.

### Theorem 3 (all s ≥ 0 for m ≤ 21): correct

- **X rule.** s ≡ 0 mod 4e. Strip the h-primes from s/e to get r, with 4 | r, gcd(r,h) = 1 and s/(re) odd, so X^e+1 | 2^s+1. Distinct Φ₂d(X) for d | e divide X^e+1. With c | k, A | k(2^s+1) = n+u.
- **Residue of 2^r.** u = 2H, so 2^r mod 16H depends only on r mod h once r ≥ 4. Hence the check at 2^{a+4h} is exact.
- **v ≥ 2.** It is automatic: A ≡ 1 and k ≡ 7 (mod 8) give v ≡ 7 (mod 8), so v = 1 (c = k with the full divisor set) is impossible. 4 | tv−1 holds, so the explicit triple (ADn, uD, AuD) exists.
- **Fixed rules.** Each is sound on its whole class from s₀:
  - II needs no size condition, since b′ = (bn+a)/f ≥ 1. The z80 checker dropped z78's `k·2^64+1 > af` condition, harmlessly.
  - K divisors divide ny for every (i, b) choice.
  - W's v mod 8 is determined by n mod 8A.
- **Coverage.** The recursive split is exhaustive: rows compatible with a node, termination when P | b, and assertion failure on an empty node.
- **Small s < 64.** The z78 triples cover these, and are checked for m ≤ 30.
- **Dependence.** Theorem 3 relies on Mordell (M rows) and on the word criterion (W, X rows: DEDEKIND Thm 4.5, Z64 Thm 2.1). Both are correctly listed under "rel.".
- **Data.** Table values (e, period) match the cover files.

### Theorem 4 (transfer off 0 mod 3825360): correct

- Row validity at m ≡ 11 (mod T) follows from 4^T ≡ 1 at every odd part and dyadic parts ≤ 2^64. Both are checked, by the author and by me.
- The size bounds only grow with m.
- For s < 64, n_{11,s} | n_{m,s}, because 4^T ≡ 1 (mod n_{11,s}). I checked this independently for all 63 values of s.
- s = 0 gives n = 4^m.
- The "exactly residue 0" claim is confirmed by a bytearray over the full period.
- The no-go remark for finite square-avoiding rows is correctly scoped ("does not preclude other rules").
- **Suggestion:** add the F1 consistency fact (e) to the note. For transferred m the square exponent 2m+2 ≥ 64 falls in a D class, never in a W or M class, analogous to the z79 47-row remark.

### Theorem 5 (quadratic transfer): correct but of marginal value

- n + u = kz², A = z, v = kz.
- Residues mod 8 are 7, 6, 1, 7, 1, as stated.
- The profinite limit is right: z → −1 at odd p | u, z → 1 elsewhere, and 7u−1 ≡ 1 (mod 16), so z² → 1.
- The Lean proof checks.

However, the content is essentially "n+u has a divisor ≡ −1 mod u, by construction". It is a polynomial family of counting density Θ(√N), and as the note says it says nothing about the exponential families. "Equivalently D=(tv−1)/4 gives the triple" should read "Moreover…": it is a consequence, not an equivalence. §0 gives Theorem 5 no triage class; it should be NULL/METHOD, with no STATUS impact. None is proposed, which is correct.

### Falsifier table: accurate

- F1: (4^m−1)·2^{2m+2}+1 = (2^{2m+1}−1)², and 2m+2 < 64 for m ≤ 21.
- The "brute-force screens" row describes what the replay actually does. In particular the W firings are criterion checks, not cross-multiplied triples, and the wording "checking the W word" is honest.

## 4. Scope and labels

- I found no claim of ES in general, of all s for infinitely many m, or of an all-h core. The infinite transfer explicitly excludes positive multiples of 3825360.
- §0 "ES holds at all exponents through m=21" is ambiguous. Prefer "ES at every s≥0 for every 1≤m≤21".
- "Review: cross-review owed." After this review it should read: cross-model (Opus, this file), ACCEPT with minor revisions.
- **STATUS delta.**
  - The §1C row must change "All (4^m−1)2^s+1 (1≤m≤12)" to (1≤m≤21), with a pointer to the z80 note.
  - It must change "Open: … all s for m > 12" to "m > 21".
  - It must change the core range "2 ≤ m ≤ 131, m = 365" to "2 ≤ m ≤ 200, m = 365, 1094".
  - The transfer sentence is fine as proposed.
  - Promotion of the all-s range into §1C is a RECORD, so it needs this review only. It does not improve a published record, so one review suffices.

## 5. Minor and form issues

1. Untracked discovery inputs (`mask-*.json`, logs, `index/`) are not committed. Replay is unaffected because the cover files embed the X rows, but `z80_proth_cover.py` cannot be rerun from committed data. That is acceptable since discovery is not part of the proof; say so in a data README.
2. The `z80_proth_check.py` docstring says "Standalone", yet it imports `small`, `direct`, `mob` and `divs` from `z78_proth_check`. This is harmless, but say "standalone of discovery code".
3. The note is extremely compressed in §1 and in the quantifier paragraph of §2. The proofs are complete but hard to read; one displayed telescope formula in Theorem 1 would help considerably.
4. "Fermat" in Theorem 1 deserves one more word: 2^{p^i} ≡ 2 (mod p).

## 6. Debate: where a hostile reader would push, and the answer

- **"The ℓ² truncation could hide a larger index."** No. A result below ℓ² forces |Q| < ℓ², and the assertion fails otherwise. The independent full-log HNF agrees on 70 values of h.
- **"Coverage by a home-grown recursion could silently skip residues."** Two different algorithms, plus a full bytearray where feasible, all agree.
- **"Mask rows checked only modulo 8u might not divide n+u."** Divisibility is structural: distinct cyclotomic factors of X^e+1 with X^e+1 | 2^s+1 and c | k. I also confirmed it on actual integers with up to about 2·10⁸ bits, and modularly at every unit source.
- **"Transfer to huge m might break W size or the dyadic part."** Size only grows, and the dyadic parts are ≤ 2^64 (checked). Squares at 2m+2 land only in D rows.
- **"Theorem 1 is suspicious because the p-part is exactly where things fail."** The proof needs p^{v_p(d)} to be invertible on the element's order. My h=9, 27, 81 computations show the 3-part really does not split, which is exactly the boundary the note states.

**Final verdict: ACCEPT WITH MINOR REVISIONS.** The mathematics and certificates are correct as scoped. Revisions: the label coverage for CERTIFIED, the STATUS bookkeeping, the triage of Theorem 5, the F1 transfer remark, and the stale docstring and notation.
