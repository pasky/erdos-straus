# z52d Pass 2 — finisher batch ZF1 (60 items: previous record `needs-compute` or a stub)

1. Counts: nothing 51, interesting 8, covered 1 (Z0729: Pomerance–Weingartner Table 1 verifies 8/n to 10¹³), needs-compute 0, skipped 0.
2. Interesting: Z1894 (Lean proof of ES for all 3·2^s+1), Z2776 (I3(3^k+2) by period-12 covering; PROVED sterile point of 3^k−2), Z2835 (Mordell-locus Brauer–Manin obstruction on non-square pencil fibres, Thm 1(b)), Z2306 (parity-invisible certificates; p = 1044877 has only invisible ones), Z2080 (44 % of Var R(p) is the edge line #{d | p+1 : d ≡ 3 (4)}), Z2418 (3/4 exceptional-set note can be made effective), Z3054 (Siegel inventory: Goldfeld a power too weak, Tatuzawa nearly suffices), Z0077 (cyclic-cubic Galois-orbit ES: inert p reduce to Tr(1/z) ∈ 4ℤ).
3. New tools: `scripts/z52d_p2_ZF1_fastU.c` (exact U(p) via Type I/II divisor parametrisation, ~p^0.9 instead of linear-with-spf; validated vs the count program to 1.75·10⁸), `…_words1.c` (single-n word census), `…_segcount.c` (segmented U(n)), `…_verifykernel.c` / `…_cellkernel128.c` (filter verification benchmarks), `…_Lproxy_top.c`.
4. Corrections to earlier records: decade minimum of U/log³p on [10⁵,10⁶) is 0.0233 at 471241 (not 0.0278); verification cost is flat per integer (Mihnea–Dumitru: [10¹⁷,10¹⁸] in ~2 weeks), not √p-growing; Z0804 small-h(−4p) mechanism does not recur beyond 193.
5. Work split: items run by the batch owner (U/census/verification group, 12) and six sub-shards S1–S6 (per-shard notes in `data/z52b/pass2/ZF1/parts/`); outcomes in `data/z52b/pass2/outcome_ZF1.jsonl` (lint: 0 flagged).

# ZF1 shard S1 (8 items) — summary
Outcomes: nothing 8 (Z1448, Z1549, Z2077, Z2094, Z2356, Z2395, Z2400, Z2411); interesting 0; needs-compute 0; covered 0; skipped 0.
Premise failures: Z2094 (no Hooley GRH theorem for x²+y²+z³ exists; positive problem open per Jagy–Kaplansky 1995).
Numerical by-products worth reusing (all EVIDENCE/CERTIFIED, see outcome_S1.jsonl):
* Z2411: Var R/mean R over primes ≡ 1 (4) = 3.91, 4.57, 5.38, 6.14 at X = 10⁶…10⁹ (≈ +0.33 log X; extends Z3109 from 10⁵ to 10⁹).
* Z2356: (★) zero set to 10⁸ = 4999 odd squares + 1009 non-squares (24 primes); non-square zeros per decade 7,20,68,145,239,299,229.
* Z2077: Bach–Sorenson-type triangle-inequality certificate on D_{-1}(4Cp+1) ≡ full-coset cover (B4); fires for ~95 % of primes, mostly C ≤ 3.
* Z2400: share of Σ R(p) at witness level ≤ X^θ ≈ θ²; fraction of primes with least witness level > X^{1/2} is 10⁻⁴ at 10⁸.
No `interesting` items, hence no detail sections.


# ZF1 shard S2 — interesting items

## Z2418 — the 3/4 exceptional-set theorem can be made effective (Assessment)
**What.** Line audit of `paper/es-threequarter-note.tex`: Siegel–Walfisz enters only via Bombieri–Vinogradov
(eq. BV, saving (log x)^{−26}) in the lower bound of Thm `supply`; moduli are q = 4uv ∈ (4X^{1/24}, 4x^{1/3}].
BMOR's explicit PNT-in-AP (arXiv:1802.00085) is unusable there (needs x ≥ exp(0.03√q log³q) for q > 10⁵).
An effective BV that excludes multiples of one Landau–Page modulus r1 (Akbary–Hambrook arXiv:1309.2730 Thm 1.2,
explicit c0 = 48.83, + effective zero-free region) suffices: if r1 ≤ (log x)^{1.9} BMOR Prop 1.11
(β ≤ 1 − 40/(√q log² q)) makes the exceptional term x^{β1} ≤ x·exp(−(log x)^{0.04}); otherwise drop the triples
with r1 | 4uv from the (nonnegative) lower-bound sum, losing a fraction ≪ (log x)^{−1.9+ε} of the main term.
**Numbers / reproduce.** No computation; read `data/z52b/pass2/ZF1/Z2418/effectivity.md` §§1–4 against the note,
l. 297–307 and 497–541.
**Why it might matter.** The flagship internal theorem is stated as "ineffective because of BV"; the sketch removes
that caveat cheaply (same for the log log and m/n notes, which use BV the same way — not re-derived). It does NOT give
any calibration: N·exp(−c(log N)^{3/4}) → ∞, so no version can certify "no counterexample below X" (§5).
**Next.** Write the lemma into the note and get it reviewed; optionally make Shiu's constant explicit.

## Z3054 — Siegel inventory: Goldfeld is a power too weak; Tatuzawa nearly suffices (Assessment)
**What.** All ES-side Siegel uses (table: `data/z52b/pass2/ZF1/Z3054/siegel_inventory.md`). The only L(1,χ) LOWER
bound is inside Pollack IJNT 2014 Thm 1.4 (CAP_DOWN Cor 2.1, e*(n) ≪ n₀^{1/4+ε}; ASTRA_BRIDGE q₀(p) ≪ p^{1/4+ε}):
it needs L(1, χ_{−4n₀}) ≫ W^{−ε²/640L²}. Goldfeld–Oesterlé (h(D) > (1/55) log|D| ∏…, verified) gives only
n₀^{−1/2+o(1)} — making the argument run would push the exponent from 1/4+ε to ≥ 640/ε². Tatuzawa
(L(1,χ) ≥ (ε/10)q^{−ε} with one possible exception) instead gives effectivity outside ≤ 1 (n ≡ 1 (8)) resp. ≤ 2
(n ≡ 5 (8)) unknown square classes n₀. Other Siegel uses: BV-based notes (removable, Z2418), Siegel's integral-point
theorem in INVOLUTION_ES2 (different theorem), BM main term (needs upper bounds only).
**Reproduce.** Read Pollack §4 (`sources/pollack_ijnt2014_generalsplit6.pdf`, l. ~1195–1390 of pdftotext output).
**Why it might matter.** It answers "is the ineffective→effective route blocked?": no, but Goldfeld is not the tool;
no ES main term needs an L(1,χ) lower bound at all, so a Goldfeld-type auxiliary L-function has no slot.
**Next.** Remark in CAP_DOWN Cor 2.1 + reviewer check of ξ⁺ in case (b).


## Z2835 — non-square pencil fibres: the class (−q, −d) also obstructs on the Mordell locus 4k + n³ = □ (interesting)

**What.** Z52_BANKED §1(a) shows that 𝒜 = (−q, −d) lies in Br S_{n,k} (S_{n,k}: 4xyz − n(xy+yz+zx) = k, q = 4y − n,
d = qz − ny) when k = m², and for non-square k is unramified exactly when 4k + n³ is a square. The item asked for the zero
table at non-square k and a comparison with BM predictions.

**Numbers (CERTIFIED, complete searches, `scripts/z52_bank_pencil.c`, odd n).**
* Zeros of S_{n,k}(ℕ): k = 2: 9, 21, 57, 65, 117, 201, 297, 425, 945, 3465, 12597, 25221, 26961 (n < 5·10⁴);
  k = 3: **only n = 13**; k = 5: 21, 57; k = 6: none; k = 7: 9, 33, 45, 57, 129, 417, 1245, 2805, 2925 (none in (10⁴, 5·10⁴)).
  Square controls (n < 10⁴): k = 1: 1262, k = 4: 1250, k = 9: 417 zeros among 4996 odd n. So non-square fibres have only
  sporadic zeros, with no killed residue class.
* The single k = 3 zero is the only odd n ≤ 10⁴ with 4k + n³ a square (13³ + 12 = 47²). At (13, 3) all 133 901
  local symbols (−q, −d)_ℓ at ℓ-integral places of 19 995 random rational points are +1. The controls (17,3), (21,3),
  (13,2), (13,7) have −1 at some places (`data/z52b/pass2/ZF1/Z2835/bm_local_13_3.txt`).

**Theorem 1(b) (PROVED here, elementary; the same Hilbert-reciprocity scheme as Z52_BANKED Thm 1(a)).** Let s be odd,
n ≥ 1 odd, and k = (s² − n³)/4 ≥ 1 (so n ≡ 1 (4)). Assume gcd(n, k) = 1, and that (−n/ℓ) = +1 for every prime ℓ | s with ℓ ∤ k.
Then S_{n,k}(ℕ) = ∅.
*Proof.* Take a positive integral point. Then q, d > 0, so inv_∞ = −1. Finite places:
* ℓ ∤ qd: the symbol is trivial.
* Odd ℓ | q: then ℓ ∤ n (otherwise ℓ | y and ℓ | k), and (I3) gives −d ≡ (n/2)², a unit square.
* Odd ℓ | d, ℓ ∤ q, ℓ | k: (I2) forces ℓ | y, so −q ≡ n, and n is a square mod ℓ because s² ≡ n³.
* Odd ℓ | d, ℓ ∤ qk: −q ≡ n²y²/k. The key identity is dd′ = (ny + 2k/n)² − k(s/n)². It gives (k/ℓ) = 1 if ℓ ∤ s. If ℓ | s,
  then k ≡ −n³/4, so (k/ℓ) = (−n/ℓ) = 1 by hypothesis.
* ℓ = 2: q is odd. If −q ≡ 5 (8), then dd′ is odd by the same identity (for n ≡ 1 (8) k is even and ny + 2k/n is odd; for
  n ≡ 5 (8) k is odd and dd′ ≡ kq (mod 4)), so the symbol is +1.
The product of all local symbols is then −1, which contradicts Hilbert reciprocity. ∎
*Check* (`scripts/z52d_p2_ZF1_Z2835_mordell.py 3001 1000000`, complete search with the general bound x²(4x − 3n) ≤ k).
There are 55 861 Mordell-fibre pairs with n ≤ 3001 and k ≤ 10⁶. Under the hypothesis, 13 682 of 13 682 are empty
(both n ≡ 1 and n ≡ 5 (8)). Without it, many are still empty: 17 829 of 31 548 (57 %) with gcd = 1 and a "bad" prime ℓ | s,
(−n/ℓ) = −1. A bad ℓ = 3 makes points easy: only 111 of 5 635 such pairs are empty. Adjacent non-Mordell controls (n, k + 1..3) are empty only
2.5 % of the time (298 of 11 986).

**Why it might matter for ES (Assessment).** On the k-pencil, 𝒜 obstructs on two loci: {k = □} (Thm 1(a), positive
density in n for each square k) and the Mordell locus {4k + n³ = □} (Thm 1(b)). For fixed non-square k the second locus is
the finite set of integral points of s² = n³ + 4k (Siegel), so "non-square fibres are BM-free" holds only up to finitely
many n per k. At k = 0 the second locus is exactly {n = □}, i.e. the odd squares of T1. So T1 is the k → 0 limit of the
Mordell-locus obstruction. At k = 0 the proof itself breaks: gcd(n, k) = n, the case ℓ | n fails, and U_n is singular. A
prime p is never on the k = 0 Mordell locus, which matches FRONTIER §7 item 15 (no prime T1).

**Reproduce.** `gcc -O2 -Iscripts -o /tmp/pencilk scripts/z52d_p2_ZF1_Z2835_pencilk.c; uv run --with sympy python
scripts/z52d_p2_ZF1_Z2835_mordell.py 3001 1000000 /tmp/pencilk`, and `uv run --with sympy python
scripts/z52d_p2_ZF1_Z2835_bm13.py`. For the zero tables run `scripts/z52_bank_pencil.c` with `first k 9 9999 2 1`.

**Next step.** Check whether the 57 % residual emptiness on bad-prime Mordell fibres is a BM obstruction to *bounded*
integral points (strong approximation): solutions need a bad prime ℓ | d with y ≡ −2k/n² (mod ℓ). Also compute the full
Br S_{n,k} at sporadic zeros (e.g. k = 2, n = 3465) to see whether any other class exists.



## Z0077 — Galois-orbit ES Tr_{K/Q}(1/x) = 4/p in cyclic cubic fields: a positivity mod-4 obstruction (shard S5)

**What.** For K cyclic cubic and x ∈ O_K totally positive, Tr(1/x) = s₂(x)/N(x), so the item's equation is p·s₂(x) = 4N(x).
* PROVED (elementary). If p is inert in K, p | N(x) forces p | x; with x = p·y the equation becomes Tr(1/y) = 4 — independent of p.
  Conversely any totally positive z ∈ O_K with Tr(1/z) = 4k gives x = p·k·z for every p (and every n). So all inert p are solvable or none is.
* PROVED. If 2 is inert in K and every totally positive unit is a square (true for conductors 7, 9, 13, 19, where the units have all
  sign patterns), then no totally positive unit u has 4 | Tr(u⁻¹): with u = w², Tr(u⁻¹) = Tr(v)² − 2s₂(v), v = w⁻¹, s₂(v) = ±Tr(w), so
  4 | Tr(u⁻¹) needs Tr(w̄) = Tr(w̄⁻¹) = 0 in F₈, impossible (the trace-0 Frobenius orbit of F₈^× is inverse to the trace-1 orbit, and Tr(1) = 1).
* EVIDENCE. Box search |coords| ≤ 60 in Z[θ] (≈ 4.1–5.9·10⁵ totally positive elements per field; conductors 7, 9, 13, 19): Tr(1/z) is
  an integer for 187 / 166 / 74 / 51 elements with residues only 1, 2, 3 (mod 4); 4 | Tr(1/z) never occurs. With signs allowed (box 25)
  4 | Tr(1/z) occurs 258 / 426 / 116 / 68 times. Polynomial census X³ − aX² + mcX − c (roots positive, Σ1/x_i = m, irreducible, D > 0),
  a ≤ 70: cyclic (D = □) counts for m = 1…16 are 18, 17, 11, **0**, 8, 6, 4, **0**, 6, 2, 3, **0**, 2, 2, 2, **0**; non-cyclic totally real
  counts are 1788–20968 for every m including 4 | m. In all 75 cyclic hits (m ≤ 11) Tr(z)·Tr(1/z) ≢ 0 (mod 4).
* EVIDENCE. Primes p ≤ 10⁴ solved in the box: exactly split primes (cond. 7: 13, 29, 41, 43, 71, 83, 97, 113, 127, 139 = all split p ≤ 139;
  cond. 9: 17, 19, 37, 53, 73, 89, 107, 109, 127; cond. 13: 5, 31, 47, 53, 73, 79, 83, 103; cond. 19: 7, 11, 31, 37, 83, 107, 113, 163, 179,
  191, 293); no inert or ramified prime.
* CONJECTURE. For every cyclic cubic field and totally positive z ∈ O_K with Tr(1/z) ∈ ℤ: 4 ∤ Tr(1/z) (stronger: Tr(z)Tr(1/z) ≢ 0 mod 4).
  Then the Galois-orbit ES fails for every inert prime (2/3 of all primes), and the obstruction needs both positivity and cyclicity.
  It is not a 2-adic condition on the discriminant alone (D ≡ 1 mod 8 is attainable with 4 | m, a, c odd).

**Reproduce.** `uv run --with numpy python scripts/z52d_p2_ZF1_Z0077_tr4.py 60` (add a 2nd arg for all signs; `SPLIT2=1` for
conductors 31, 43, 73); `gcc -O2 scripts/z52d_p2_ZF1_Z0077_poly.c -lm -o poly && ./poly 70 16`. Data: `data/z52b/pass2/ZF1/Z0077/`.

**Why it might matter for ES (Assessment).** It has no direct bearing on ES over ℤ: the item's "reformulation" premise is false. It is a
clean toy where positivity + a reciprocity-type parity blocks a whole Chebotarev class of primes, which is exactly the kind of
obstruction Bright–Loughran rule out for ES. A proof would be a useful calibration example for "positivity obstructions" (FRONTIER §1, T1).
**Next.** Prove the conjecture: am − 9 = Tr(u), u = (z − σz)²/(z·σz) totally positive with N(u) = (Δ/c)², or compute Hasse invariants of Tr(y v²).



# ZF1 / shard S6 — interesting items

Summary (8 items): interesting 4 (Z2306, Z2080, Z2776, Z1894), nothing 4 (Z3072, Z2902, Z1887, Z1797).
* Z1894: MENU_STERILITY Theorem C (ES for all 3·2^s + 1) fully machine-checked in Lean (`lean/ES/ES/Proth3.lean`).
* Z2776: I3(3^k + 2) ≥ 1 for all k ≥ 3 except k = 4 (period-12 exponent covering); 3^k − 2 has a PROVED sterile limit point.
* Z2306: parity-invisible certificates are ≈ 1/5 on average; p = 1044877 has only parity-invisible ones (cut N^{1/3}).
* Z2080: 44 % of Var R(p) comes from the edge lines u = 1 / B = 1 (divisors of p + 1); the interior is near-Poisson.

## Z2306 — Parity problem: which ES certificates are invisible to a sieve? {#Z2306}

**What.** For a prime p and level C put N_C = 4Cp + 1, q = 4C, r_C = #{d | N_C : d ≡ −1 (mod q)} (FRONTIER §2.1
divisor form). Split N_C = s·r with s the N^{1/3}-smooth part and r the rough part (all prime factors > N^{1/3}, so
Ω(r) ≤ 2).

* **Lemma (PROVED, elementary).** Since N_C ≡ 1 (mod q), r ≡ s⁻¹ (mod q). If Ω(r) ≤ 1, every divisor of N_C is d or
  d·r with d | s, hence r_C > 0 ⇔ ∃ d | s with d ≡ −1 or d ≡ −s (mod q): success is a function of (s, C), i.e. of
  data a sieve of level N^{1/3} sees. The only extra information is how r = r₁r₂ splits when Ω(r) = 2 — Selberg's
  parity datum (a sieve cannot tell Ω(r) = 1 from Ω(r) = 2).
* **Numbers (EVIDENCE; `scripts/z52d_p2_ZF1_Z3072_omega.c`, tables in `data/z52b/pass2/ZF1/Z3072/summary.txt`).**
  - Same sieve stratum, different parity: τ(s) = 2, C ∈ [10,100): P(success) = 0.0058 (Ω(r)=1) vs 0.0360 (Ω(r)=2);
    τ(s) = 1: 0 vs 0.0227; τ(s) ∈ [3,4]: 0.028 vs 0.070; τ(s) ∈ [5,8]: 0.069 vs 0.122 (300 primes > 10⁹, C ≤ 10⁵).
  - Liouville marginal is blind: P(success | λ(N_C) = +1) = P(… = −1) = 0.00022 at 10⁹ (also at 10⁶), because
    λ(N) = λ(s)λ(r) flips sign with s.
  - Fraction of successful levels decided by s (visible): 85.5 % (10⁹, C ≤ 10⁵), 80.7 % (all C, 3642 primes in
    [10⁶, 1.1·10⁶]), 82.1 % (all C, 282 primes near 10⁷); by Ω(N): 46 % at Ω = 2, 64 % at 3, 80 % at 4, ≥ 99 % at Ω ≥ 7.
  - **p = 1044877** (≡ 757 mod 840) has exactly 5 certificate levels C = 1, 3, 68, 3958, 130610, and every one is
    parity-invisible, e.g. N₁ = 29·167·863 with d = 167 (z = 161), N₃ = 5²·263·1907, N₆₈ = 3²·5·7·683·1321 (d = 9247 =
    7·1321), N₃₉₅₈ = 5·31663·104491, N₁₃₀₆₁₀ = 3·11·31663·522439. It is the only such prime among 3642 in [10⁶, 1.1·10⁶];
    none among 282 near 10⁷ (min 4 visible levels) or 450 near 10⁹ restricted to C ≤ 10⁵.
* **T1 is not a parity phenomenon** (PROVED, elementary): for n = m² odd the sequence C ↦ 4Cm² + 1 has the same local
  densities ρ(ℓ) = 1 (ℓ ∤ 2m) as C ↦ 4Cp + 1, yet r_C = 0 for every C and every Ω — the obstruction is the quadratic
  class of the divisor relative to q (genus), not the parity of Ω.

**Why it might matter.** Parity costs ES on average only ≈ 1/5 of the certificates, so it is not the main barrier; but
it is not negligible pointwise: there are primes (1044877) where a level-N^{1/3} sieve sees no certificate at all, so a
pure-sieve proof of R(p) > 0 at this cut is impossible (Assessment: unless it raises the cut or uses bilinear/type-II
information on r = r₁r₂).

**Reproduce.** `gcc -O2 -o omega scripts/z52d_p2_ZF1_Z3072_omega.c -lm; ./omega 275001 < data/z52b/pass2/ZF1/Z3072/primes_1e6_full.txt`
(lines `P p #successC #visibleC`; ~3 min), then `python3 scripts/z52d_p2_ZF1_Z3072_summ.py <out>`.

**Next.** Scan the cut z = N^θ (θ = 1/4 … 1/2; θ = 1/2 makes every certificate visible trivially) and count zero-visible
primes in [10⁶, 10⁷] to see whether parity-invisible primes thin out with p.

## Z2080 — Linnik/Bredihin dispersion vs. ES: where the dispersion inequality sits, and the ES second moment by level C {#Z2080}

**Literature (read).** Friedlander–Iwaniec, *On a theorem of Bredihin and Linnik*, arXiv:1807.06648 (5 pp.): new proof of
Bredihin's S(x) = #{p ≤ x, p ≡ 3 (8), p = a² + b² + 1} = c·x/log x + O(x(log log x/log x)²), originally obtained by
extending Linnik's dispersion solution of the Hardy–Littlewood problem n = p + x² + y² (Linnik's book, ch. 7). In the
modern proof the dispersion step is replaced by two inputs: (i) Dirichlet divisor switching (their (2.2)–(2.4)):
λ(n) = Σ_{a|n, a≤y} χ(a) + Σ_{b|n, b<n/y} χ(b), smoothed so only b < 2√X occur; (ii) the Bombieri–Friedlander–Iwaniec
estimate (their (3.1)): Σ_{q ≤ √x (log x)^A, (q,a)=1} |π(x; q, a) − π(x)/φ(q)| ≪ x(log log x/log x)², **for a fixed
residue a ≠ 0**, constant depending on a. In Linnik's problem the residue is n (fixed) and the long variable is the
prime p ≤ n — the average over p is native to the problem.

**ES side (Assessment + PROVED bookkeeping).** R(p) = Σ_{(u,C)} 1[p ≡ −u (mod 4uC − 1)] (trial form): at a fixed p there
is no long prime variable at all, and the residue −u is tied to the modulus. After divisor switching the moduli needed
are ≤ √(4Cp) for level C, i.e. up to ≈ p^{2/3} even after choosing the best of the three symmetric pairings; so even
the p-averaged count Σ_{p≤X} R(p) is beyond BV (level 1/2) and violates BFI's fixed-a hypothesis. Only an almost-all
statement could come out of a dispersion argument, and those are known (Vaughan; FRONTIER §1).

**Second moment by C (EVIDENCE; `scripts/z52d_p2_ZF1_Z2080_disp.c`, `…_analyse.py`; all 30 899 / 27 101 primes
p ≡ 1 (4) in [10⁷, 1.1·10⁷] and [10⁸, 1.01·10⁸]).** With S = R/2 (unordered (★) solutions):
* Var S / E S = 2.28 (10⁷), 2.70 (10⁸); after removing p mod 840 class means 1.67, 2.08; mod 9240: 1.49, 1.88.
* Per level (10⁷): C = 1: Var/Mean 3.81, C = 2: 2.64, C = 3..8: 1.3–1.8; dyadic buckets 33 ≤ C < 2.6·10⁵: 0.96–1.10 (Poisson),
  the few top buckets (C ≳ 5·10⁵, near the C ≈ p/4 end) under-dispersed 0.5–0.9. At 10⁸: C = 1: 4.96, C = 2: 3.14.
  Cross-level covariances carry 33 % (10⁷) / 38 % (10⁸) of Var S although mean pairwise correlation is only 0.012.
* **The over-dispersion has an exact source:** the edge lines u = 1 or B = 1 are B(4C − 1) = p + 1, i.e.
  E(p) = #{d | p + 1 : d ≡ 3 (mod 4)} unordered solutions (PROVED, one line) — a Titchmarsh-divisor-problem object.
  E has mean 5.3 / 6.0 and Var/Mean 5.5 / 7.3 and explains 44 % of Var S at both heights; the interior S − E has
  Var/Mean 1.69 / 1.94 (1.39 / 1.65 after mod 840), and corr(E, S − E) = −0.13.
  Smooth weights vanishing at the simplex boundary (Z2902) reproduce this: Var/Poisson (unordered-shot null) drops from
  2.5–2.9 (sharp R) to 0.95–1.25, and the Mordell-hard-class deficit of R (0.74–0.78 of the mean) almost disappears (0.91–0.99).

**Why it might matter.** The part of R(p) that fluctuates wildly is exactly the part a Linnik/BV dispersion argument
*can* handle on average (Σ_p τ-type(p+1) is the Titchmarsh divisor problem, solved by BV/BFI with fixed residue
a = −1); the interior is nearly Poisson but has tied residues. A lower-tail heuristic should model R = E(p) + (interior),
S = R/2 = E + interior, with E controlled by the divisor structure of p + 1 and the interior close to Poisson (index ≈ 1.4–1.9
  by level counts, ≈ 1.0–1.25 with boundary-vanishing smooth weights).

**Reproduce.** `gcc -O2 -o disp scripts/z52d_p2_ZF1_Z2080_disp.c; ./disp 10000000 1000000 > d.txt` (0.7 s);
`uv run --with numpy --with sympy python scripts/z52d_p2_ZF1_Z2080_analyse.py d.txt edge`. Outputs:
`data/z52b/pass2/ZF1/Z2080/analysis_1e7.txt`, `analysis_1e8.txt`.

**Next.** Fit the zero-probability of the interior part alone (index ≈ 1.5 Poisson) against the census zeros of (★).

## Z2776 — I3 on c·3^k + d by exponent coverings: 3^k + 2 closes; 3^k − 2 has a PROVED sterile point {#Z2776}

**Setting.** I3(n): n = tuv − u − v with t, u, v ≥ 3 (I3_DEEP_FABLE §5.5, where 2^k ± 1, 2^k ± 3, 7·2^k − 1, 5·2^k − 1,
3·2^k + 1 were closed). Fixed-word classes with two fixed coordinates: **E** (u, v fixed): uv | n + u + v; **L** (t, u
fixed): (tu − 1) | n + u. Search: `scripts/z52d_p2_ZF1_Z2776_i3cover.py c b d B Ls [partial]` (moduli sharing primes with
b or c handled exactly; periods L ≤ 5040 at B = 3000, ≤ 720 at B = 12000; cover re-verified by direct division for
k ≤ 400; positive controls 2^k ± 1, 3·2^k + 1 reproduce FABLE's theorems with shorter periods, L = 36, 12, 12).

**Results (CERTIFIED / PROVED, computer-assisted; `data/z52b/pass2/ZF1/Z2776/cover_B3000.jsonl`, `partial_B12000.jsonl`).**
* **I3(3^k + 2) ≥ 1 for every k ≥ 3, k ≠ 4**: three L-words, period 12 — (t,u) = (3,3) [8 | n + 3, k odd],
  (4,4) [15 | n + 4, k ≡ 2 (4)], (13,7) [90 | n + 7, k ≡ 0 (4)]; zeros only at k = 0, 1, 2, 4 (n = 3, 5, 11, 83).
* Also closed: 5·3^k − 1 (2 words, L = 12), 2·3^k + 1 (2 words, L = 12); 2·3^k − 1 and 10^k ± 1 lie in a single
  residue class (n ≡ 5 mod 12, resp. a fixed class mod 18 / 12) and are covered by one word — congruence families, trivial.
* **Not closed** (coverage statements for k ≥ K0 = 14; below that brute force, zeros listed in the jsonl): 3^k − 2 (all
  k ≢ 1 mod 240 covered by 12 words, small I3 zeros k = 2, 3; residual k ≡ 1), 5·3^k + 1 (residual k ≡ 1, 2 mod 48),
  3^k − 1 (residual k ≡ 1 mod 48), 3^k + 1 (residual k ≡ 1, 2, 3, 15, 22 mod 60), 5^k ± 1 (not covered at B = 3000).

**The residual classes are neighbourhoods of tiny I3 zeros.** Their profinite limit point is (n_{k₀} at every prime ≠ 3,
d at 3) with n_{k₀} ∈ {1, 2, 4, 10, 16, 46} an I3 zero (3^1 − 2, 3^1 − 1, 3^1 + 1, 3^2 + 1, 5·3 + 1, 5·9 + 1). No E- or L-word
with modulus ≤ 3·10⁶ contains any of these six points (`scripts/z52d_p2_ZF1_Z2776_point.c`,
`limit_points_M3e6.txt`; positive controls (83, 2), (11, 2) found at m = 129, 21; the program printed a spurious trailing
"none" after hits in its first version, fixed; the point (28, 1) of 3^k + 1 is covered at
m = 17, so the k ≡ 3 residual there is a period/supply artefact).

**Proposition (PROVED here).** Let P ∈ Ẑ be 1 at every prime ≠ 3 and −2 at 3 (the limit of 3^k − 2 as k → 1 away from 3
and k → ∞ 3-adically). No E- or L-word class contains P. Hence for no L is {3^k − 2 : k ≡ 1 (mod L)} covered by finitely many
two-fixed-coordinate I3 classes.
*Proof.* Write the modulus as 3^a·w, 3 ∤ w. **E**: P ∈ class ⟺ uv | … ⟺ uv ≡ 0, u + v ≡ −1 (mod w), u + v ≡ 2 (mod 3^a).
So u, v are the roots of X(X + 1) mod every ℓ^e ∥ w and of X(X − 2) mod 3^a; the roots are distinct mod ℓ, so prime power by
prime power one of u, v is ≡ 0 and the other ≡ −1 (resp. 2). As uv = 3^a w exactly, u = 3^a w₁, v = w₂ (w = w₁w₂, after
renaming) with V := w₂ ≡ −1 (w₁), V ≡ 2 (3^a), U := 3^a w₁ ≡ −1 (V). a = 0: V | U + 1, U | V + 1, U, V ≥ 3 is impossible. w₁ = 1:
V | 3^a + 1 but V ≥ 3^a + 2. Otherwise U + 1 = rV with r ≡ −1 (w₁), r = j w₁ − 1: j = 1 gives V = 3^a + (3^a + 1)/(w₁ − 1),
forcing (3^a + 1)/(w₁ − 1) = 2, w₁ = (3^a + 3)/2 ≡ 0 (mod 3) — contradiction; j ≥ 2 gives V < 3^a + 2 — contradiction.
**L**: (tu − 1) | n + u at P ⟺ u ≡ −1 (w), u ≡ 2 (3^a), tu − 1 = 3^a w. Then t = xw − 1 and w(xu − 3^a) = u + 1. a = 0:
tu − 1 | u + 1 impossible for t ≥ 3. a ≥ 1, u = 2 + 3^a z (z ≥ 1): w = 1 forces u = (3^a + 1)/(x − 1) ≤ 3^a + 1 < u; x = 1
gives w = 1 + (1 + 3^a)/(2 + 3^a(z − 1)), i.e. z = 1, w = (3^a + 3)/2 ≡ 0 (mod 3) — contradiction — or z ≥ 2, 1 < w < 2;
x ≥ 2 gives w < 1. ∎ (The closure of {3^k − 2 : k ≡ 1 mod L} contains P: take k ≡ 1 mod L·ord_w 3 and k ≥ a.)

**Why it might matter.** It is the I3 analogue of the ET sterile point μ = 0 of 3·2^s + 1 (EXPONENT_COVERING Cor 1.5):
fixed-word exponent coverings are complete *except* at limit points mimicking a tiny I3 zero, and there they provably fail;
whether a window/moving word (polynomial in X = 3^{(k−1)/2}, n = 3X² − 2 on k odd) closes the class is the I3 version of
the (J)74 question. **Next:** search moving words for n = 3X² − 2, X = 3^j (I3 analogue of the Sophie-Germain window), and
prove sterility of the points (2, −1), (4, 1), (16, 1) by the same root-splitting argument.

## Z1894 — Lean: MENU_STERILITY Theorem C (ES for every 3·2^s + 1) fully formalised {#Z1894}

**What.** `lean/ES/ES/Proth3.lean` (≈ 230 lines, imports `ES.Basic` + Mathlib; added to `ES.lean`) proves
`ESProth3.proth3 : ∀ s : ℕ, ES.ESProp (3 * 2 ^ s + 1)` with axioms [propext, Classical.choice, Quot.sound] only, no
`sorry`; compiles in ≈ 9 s (Lean 4.34.1, Mathlib d13f23b7 via `lake env` of a built checkout; log
`data/z52b/pass2/ZF1/Z1894/lean_check.txt`). Structure exactly as Theorem C: generic `window` lemma (CAP_DOWN Lemma 1.1:
n + m = 4K, K² = de, m y₀ = K + d, m z₀ = e + K ⟹ (K, n y₀, n z₀)), `sophie_germain` 4(Y+1)⁴ + 1 = f₊(Y+1) f₊(Y),
`sg_window` (the eight m = 11 rules, (b, c) per X mod 11, divisibility decided in ZMod 11), the ET classes mod 7 and 15,
divisor classes 5, 7, 61 by scaling, and `pow_mod_period` for 2^s mod 7, 15, 11, 61.
**Why it matters.** Pass 1 estimated "days of Lean work"; the whole theorem took well under an hour, so every thin-family
theorem of the (J)62–(J)80 type (finite ET covering + polynomial window identities) is cheap to machine-check — a
certificate format that a referee need not trust. Same pipeline gave the 15·2^s + 1 off-core theorem (Z1797).
**Next.** Formalise (J)80 (63·2^s + 1) and (J)75 (7·4^s + 9) with the same `window` lemma; generate the ET-class part
automatically from the certificate JSON as in `scripts/z52d_p2_ZF1_Z1797_gen_lean.py`.
