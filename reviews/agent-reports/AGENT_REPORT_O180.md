# AGENT_REPORT_O180 — spark relay G: Lorenzini's A₃ question (W), Wu/Stern side topics

Branch `side-agent/lorenzini-w` (merged side-agent/spark-hj-brainstorm and main at start). Deep file `LORENZINI_W.md`; 10 memos
`BRAINSTORM/bsG_*.md` (indexed in BRAINSTORM/README.md); scripts `scripts/bsG_*`. Lorenzini sources in `sources/lorenzini/`.
**ES is not solved, and (W) is not proved.**

## SHARP
1. **Even half of Lorenzini's question settled (LORENZINI_W Thm 9.1, PROVED).** Every even n ≥ 16 except 510 is xyz − x − z (x,y,z ≥ 2).
   Lorenzini (JNT 257 (2024), Prop 6.3(a)) left n = 2^m − 2, m odd, open. Six fixed-pair families with moduli 9, 72, 13, 27, 109, 592 cover all
   odd m mod 36 (a Sierpiński-type covering of the exponent). The proof is by hand from the table, and explicit solutions are checked for odd m ≤ 4001.
   (W) is now *exactly*: odd n ≡ 3, 9, 11 (mod 12) with n + 2 prime (minus the 6 known odd exceptions).
   (R184: independently re-proved SOUND; brute force to 10⁸ agrees. Novelty: not found in the literature — R184 repair, D8, see the honesty note.)
2. **Deflationary for ES (Prop 8.1, PROVED, trivial in hindsight):** (W) at primes p ≡ 1 (4), p ≥ 13 holds by (2,2,(p+2)/3) (p ≡ 1 (3)) or
   (3,(p+7)/12,4) (p ≡ 5 (12)). So **interior-SQ₅(p) ⟺ (S)(p)**: HJ_DEEP's sign-free half carries no ES content at primes. Future relays
   should attack (S) on p ≡ 1 (12) directly. The (3,·,4) word is the classical p ≡ 2 (3) identity (sign −1). The (2,2,·) word has sign +1.
   (R184 repair, D4/D5: hence (S)(p) is PROVED for p ≡ 5 (12). Both words are Lorenzini's own z = 2 / z = 4 slices, so Prop 8.1 strengthens his 6.3(c); it is not new.)
3. **Square shadow (Lemma 3.1, PROVED):** T1 acts *partially* on (W). At n = m² the middle letter is ≢ 0 (4) and ≢ 7 (8), and ≢ 3 (4) if m is even.
   At n = km², it is ≢ 0 (mod 4k). The record-low R(n) (number of solutions) are squares of smooth numbers (R(2310²) = 4 vs mean ≈ 104). Still,
   all squares except 1, 9 are values (Prop 3.3). HJ_DEEP's "(W) is T1-free" should read "(W)'s *existence* has no T1 obstruction".
4. **Short-block law (EVIDENCE):** for every n < 10⁸ outside E_W some solution has an outer letter ≤ 12 (x*(n) ≤ 12; records 17:3, 51:4, 126:6,
   1379:12). Heuristic CONJECTURE: x*(n) ≪ log n / log log n.

## Other results
* Forms F1–F4 of (W) (PROVED, brute-force checked): xz | n + x + z; a ceiling-function form; −n mod d | d+1; a modular-hyperbola/SL₂ form.
* Sterile set (§4): S ∩ Z = {−1}; S is infinite with −1 as an accumulation point (Thm 4.2, PROVED: ν(ℓ, ℓ−1) ∈ S for every prime ℓ ≥ 3).
  So no compactness argument proves (W). Finite-level Cor 4.4: (W) for all n outside 11 550 classes mod 151351200. (R180 repair, D2: now self-contained CERTIFIED by `scripts/review_lw_cor44.c`, 16 s; no dependence on R174's 10⁹ enumeration.)
* Prop 6.1 (PROVED; the input is the Titchmarsh divisor theorem, which is a theorem (Linnik; Halberstam via BV) — R180 repair, D3. Baseline: Lorenzini 6.3(b) already gives ≪ N/log N, D4): #{exceptions ≤ N} ≪ N exp(−c√log N), via the large sieve with growing dimension.
* Stern coding made exact (Prop 7.1, PROVED): V_{A_k}(2) = {s(N) : popcount N = k+1}. Lorenzini's lists L_{A₃}, L_{A₄} are reproduced to 10⁸ and L_{A₅}, L_{A₆} to 10⁷
  (`scripts/bsG_Ak.c`).
* Lens/d-invariants: by Hirzebruch–Zagier/Myerson (checked on 4 353 pairs), 12 s(q,n) = (q+q*)/n + Σ(b_i − 3). Dedekind-sum and Floer invariants see the letter sum, not
  the HJ length. No topological route.
* Negative screens: no Weinberger/class-group exponent structure (the quadratic field moves with the slice); the modular-hyperbola count has the
  B3 gap; consecutive-block pigeonhole needs large prime factors, which is an H-B-type lower-bound problem.

## Honesty / scope notes
* Thm 9.1's novelty: I checked Lorenzini (2022 preprint = JNT 2024) and Wang–Lu (EJC 33(3) (2026) #P3.80, which calls finiteness open for general G; R184 repair, D3).
  (R184 repair, D8.) R184 did the wider search. It covered the 7 Semantic-Scholar citers of Lorenzini's paper (4 arXiv texts grepped), Lorenzini's 2025 preprints
  and web/OEIS/MathOverflow searches, and found nothing on the even case. Google Scholar lists 9 citers, so 2 were not seen. Phrase it as "not found in the literature". Prop 8.1's (3,·,4) family is in the fixed-pair menu that Lorenzini's (c) underuses (he covers only n ≡ 2, 8 (9) within n ≡ 1 (4)).
* Prop 6.1 is a sketch at the standard level of rigour (Montgomery large sieve, elementary-symmetric lower bound, Titchmarsh–Linnik). A reviewer should check the
  e_k ≥ (G^k/k!)(1 − O(k²/G²)) step and the constant bookkeeping. (R180: checked SOUND. The step is now stated exactly, as k!e_k ≥ G^k − C(k,2)TG^{k−2} with T → 0, repair D3.)
* Thm 4.2's case analysis is by hand. It is cross-checked by `scripts/bsG_dev.c` for ℓ ≤ 29 (moduli ≤ 10⁵).
* ~~Cor 4.4 depends on R174's `scripts/review_hj_ws.c` enumeration to 10⁹~~ (R180 repair, D2: only n < 2M ≈ 3·10⁸ matters, and it is checked directly by `scripts/review_lw_cor44.c`).
* (R180 repairs D1, D5, D6.) The F2 diagonal case needed y ≥ 2. The §5 heuristic sum is Σδ_x = (½ + o(1))X, not (1 + o(1))X. There are cosmetic fixes in §§5, 7, 8.

## Sparks (not pursued)
* Transfer Vaughan's ES density method (non-CRT composite moduli) to (W), aiming at N exp(−c log^{2/3} N).
* Covering-of-exponent for other sparse families inside the odd residue: n with n + 2 = prime of special form (Fermat-like p = 2^k + 1 ⟹ n = 2^k − 1, Mersenne-type
  n = 2^k − 1 with 2^k + 1 prime). These are one-parameter families where Thm-9.1-type coverings may exist.
* (W_k) for A₄–A₆: the analogue of Thm 9.1 for Lorenzini's L_{A₄} etc. (even residues and 2-power families) is probably equally cheap.
* (S) at primes p ≡ 1 (12): the short-block analogue for −1 words (least outer letter of a Jacobi −1 word), compared with SYNTHESIS's first-witness statistics.
* Is every sterile point ≡ −1 at all but finitely many primes? (EVIDENCE: yes in the probe.)
