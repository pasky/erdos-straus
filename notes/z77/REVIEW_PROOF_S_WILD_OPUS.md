## §0
Result: Hostile review of `notes/z77/PROOF_S_WILD.md` (commit fcba3c8cf). Theorems A and B and the panel hold as stated. The §4 corollary is a plausible re-parameterisation that I checked as a sketch only. Form fixes are listed below.   Label: Assessment
Scope: Theorem A (k=255,1023,4095), Theorem B, the §4 corollary and the U₇ panel. No claim about ES in general.
Review: Claude Opus (Anthropic), hostile. This counts as cross-lab only if the author lane was not Claude.
Triage: NULL (review)
STATUS delta: none from this file. Verdict: Theorem A **ACCEPT** (PROVED, computer-assisted); Theorem B **ACCEPT, but triage it as a corollary, not as HEADLINE**; §4 corollary **ACCEPT as a sketch**, relative to z75; panel **ACCEPT** (DATA).

## Replays
All replays ran with `ulimit -v 1000000`, `timeout ≤120`, `uv run --offline --no-project python -B`.
* `z77_proth_verify.py` reproduces the rule counts in the table and full coverage 5040 / 55440 / 720720.
* `z77_u7_panel.py` reproduces `u7-panel.txt` byte-identically (git clean). `z77_u7_follow.py` (cypari2) reproduces `u7-follow.txt`.
* **Mutation test** of the verifier, k=255: dropping an M row, shifting a W residue, perturbing an II parameter, changing the X degree 315→5, or perturbing a D prime are all **rejected**.
* **`scripts/z77_review_proth_e2e.py`** is new and independent of both the verifier and the discovery code. It works at the actual exponent s, not at residues, and produces explicit triples checked by `4xyz=n(xy+yz+zx)`:
  * `fixed 1500 150`: all 5040 classes of k=255, plus 1500 and 150 random classes of 1023 and 4095. Each class was tested at its first s≥32 and at s+H. All passed.
  * `extra`: every row of both `-extra` files passed, including all 124 K rows (12 + 112).
  * `x 13`: X rows at real s. Φ₂d(2^r) was computed by a Möbius product, with its own subset search. Every unit residue r mod h was hit and verified, for all three k (6 / 6 / 10).
* **`scripts/z77_review_small_s.py`** gives explicit ES triples for all s<32 for all three k. **The appeal to Salez is therefore unnecessary.** The D primes used are below 20000, and my e2e script solves ES(q) for them by brute force.
* **`scripts/z77_review_thmB.py`** tests Theorem B on the smaller modulus Q′ = (odd fixed-row lcm)·255·127. Here ord_{Q′}(2)=5040, J=5044, and c has 10088 bits.
  * For 720 off-core exponents s≥32 and 7 core exponents, N = c·2^s + d gets a verified triple. On the core this uses the *same* divisor A.
  * The odd lcm factors as 3²·5·7·11·13·17·19·29·31·43·71·97·109·257·281·2017.
* **`scripts/z77_review_u7_rows.py`** rechecks all 7762 positive panel rows and the 6 follow-up rows: the word identity holds, f≡7 (8), 8 | xy, and f/c is prime by trial division.

## Substance
1. **Core lemma.** I checked it by hand.
   * Since s/(mr) = p^a is odd, x^m+1 divides 2^s+1.
   * We have 4 | r, so 16 | x, and r mod h is a unit.
   * Write A = c∏F_d(x). Then A | k(2^s+1) = n+u. From A ≡ 7u−1 (mod 8u) we get t ≥ 7 and t ≡ 7 (mod 8).
   * v=1 would force n ≡ 3 (mod 8), so v ≥ 2.
   * The verifier enumerates every unit residue, and the h-path logic is correct.
   * **Simplification:** n≡1, t≡7 and u≡6 (mod 8) force v≡7 (mod 8), so 8 | tv−1. Then `4/n = 1/(Adn)+1/(ud)+1/(Aud)` with d=(tv−1)/4, and this holds identically for any n. So the X rows need neither the Jacobi sign nor Z64 Thm 2.1. State this explicitly.
2. **Fixed rules.** I re-derived the II identity (b′ = be−a) and the K identity. Freezing periodicity at s₀ is valid by induction, since 2^P times a multiple of M is still a multiple of M. The Mordell argument for composites is correct.
3. **Theorem B.** The transfer is correct.
   * c ≡ 255 and d ≡ 1 both mod Q and mod 128, and the 2-parts are ≤128 (asserted).
   * N+254 = c(2^s+1) with 255 | c.
   * N ≡ 1 (mod 8). For s<32, n_s | N, and N = 4^J at s=0.
   * The no-cover claim holds: ν(0) has odd components 4^J and a 2-component ≡ 1 (mod 8), so it lies in Sq^×.
   * **However, B is a cheap congruence lift of A.** It does not pass the STATUS test as a separate HEADLINE row. Fold it into the A row or put it in FRONTIER.
   * Q is huge only because of the s<32 multiples. My Q′ test shows that the off-core and core parts already work at J = 4+5040i.
4. **§4 corollary.** The parameters are consistent: h(J₀) ≍ log t, m = t log t, mt ≍ log H, which gives √(log H·log log H). The removed weight is exactly W. The sentence "all primes ≤y are retained … only gives log log y" is confusing and should be rewritten. The corollary is not mentioned in §0; add its label (PROVED rel. z75: BV, BT, Mertens) and its scope.

## Gaps and omitted assumptions. None is fatal; all are fixed or covered by the replays above.
* **Verifier, II rows:** it never checks b′>0. This holds implicitly because n ≥ k·2^32 > af (af < 10^10). Add the assertion.
* **Verifier, W rows:** it uses `(1+t)` for `(n+t)`. This silently relies on n≡1 (mod 8). It also tests the Jacobi sign, not one of the explicit five conditions of DEDEKIND Thm 4.5. Thm 4.5 is itself a 512-cell computer check.
* **Verifier, D and M rows:** it relies on external ES(q) and on Mordell, and checks neither. My replay covers ES(q).
* **Salez** is used for s<32, and the note calls it "published". It is an arXiv preprint. Replace it with the explicit s<32 check.
* **§0 label** lists "Salez's finite verification". Drop it, and add "Mordell (1969)".
* **Wording:** "Every integer s≥0, prime or composite" should say that *n* may be prime or composite.
* **Stray data:** `15-5040-1.json` is committed but is not part of any claim. Mark it as such in the note, or remove it.
* **Not done:** Lean formalisation. The note honestly says the result is not in Lean.
