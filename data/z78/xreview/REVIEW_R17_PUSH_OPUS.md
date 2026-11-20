Result: Cross-lab hostile review of `notes/z78/R17_PUSH.md` (commits `main..a4642c42d`). The r≥919 sterile-line threshold survives, but only after fixing one real proof gap in the P₅ step. With the fix, the binding prime 929 totals 498628 ppm and the margin there falls from 935 to 834 ppm. Every other proof checked is correct. The point-5 depth-11 result was reproduced independently.
Label: Assessment (review). Reviewer: **Claude Opus (Anthropic)**, running as a Claude Code subagent. No other model was called. There were no provider, auth or quota errors; the web search used to check the BBR statement worked.
Scope: Math and code review of §§1–7. Own replays at r=911, 919 and 929, plus samples. This is not a full-range independent recomputation of every new table over 17≤r<7219. The inherited SE/ZL/z77 inputs were not re-derived.
Triage proposal: RECORD stands at **r≥919** once the P₅-order fix (F1) is applied. Until then the §7 table and the 929 row must not be promoted as written.
STATUS delta: As the author proposes ("every prime r≥919"), with the label "PROVED (computer-assisted, relative to SE/ZL/z77 incl. their libm condition, and BBR 2012 Thm 1.2)". The §7 table row should become `929 | 51669 | 531 | 15489 | 56553 | 359154 | 3072 | 12164 | 498628`.

# 1. Verdict in one paragraph

The per-parent survival map in `z78_deep.step` is used at P₅ on a set that is **not** a union of depth-2 parents. That set is what remains after L1, P₃ *and* Q₃, and Q₃ boxes are depth-3 cylinders. The bound "≤2⌈T/r²⌉ killed children per alive parent ⇒ loss ≤ lv·2⌈T/r²⌉/r" is therefore unjustified as coded. The note's own §5 text ("process higher P without Q beyond depth 3") describes the valid order, but the code does not follow it.

Fix: apply the P₅ step to A₂ = nonsq − L1 − P₃, which is a union of depth-2 cylinders and inverse-stable, and subtract Q₃ afterwards. With the fix (`scripts/z78_xr_p5order.py`, and independently `scripts/z78_xr_budget.py`):
* the failure set is unchanged: the largest failing prime is still 911;
* every prime in [919,7219) still passes;
* the tightest prime is still 929, where the P₅ term rises from 56452 to 56553 ppm and the total from 498527 to 498628 ppm;
* the exact margin at 929 is 834.04 ppm (nonsquare mass 464/929).

The steps at K≥7 are unaffected. After P₅ the alive set is a union of depth-3 cylinders, and at 929 the per-parent branch is not even selected for K≥7 (§4).

I checked all the other mathematics line by line and found it correct (§3). Exact enumeration also shows that the depth-3 part of the ledger is loose by about four orders of magnitude; F2 quantifies this and gives a cheap route below 919.

# 2. Findings

**F1 (proof gap, fixable, non-fatal): the P₅ per-parent step runs after Q₃.**
* Where: `z78_deep.budget2`, `lv=F(r-1,2*r)-sum(parts[:3])`, then `step(3,lv,…)`.
* Why it fails: let S be the alive set, a union of depth-3 cells. Over a depth-2 parent containing n_P<r cells of S, the large-shift centres can kill up to min(n_P, 2⌈T/r²⌉) cells. That is not ≤ (2⌈T/r²⌉/r)·n_P.
* Valid alternative: A₂(1−x) − s/r³ − Q₃ ≥ … (`z78_xr_p5order.py`).
* Effect, author vs. corrected, ppm:

| r | P₅ author | P₅ corrected | total author | total corrected | verdict |
|---:|---:|---:|---:|---:|---|
| 907 | 55085 | 55508 | | | |
| 911 | 53220 | 53785 | | | still fails |
| 919 | 54081 | 54829 | 472662 | 473410 | passes, margin 26047 |
| 929 | 56452 | 56553 | 498527 | 498628 | passes, margin 834.04 |

* Over 211<r<7219 the failure set is identical: 108 primes, largest 911.
* Required: change the code (or add a note erratum and a regenerated `check.txt`), the §7 table, and the §5 sentence, so that the order L1, P₃, P₅-step, Q₃ en bloc is the one actually implemented.

**F2 (strong recommendation, EVIDENCE): exact depth-3 unions are cheap and remove nearly all of the depth-3 charge.**

My independent engine `scripts/z78_xr_exact.c` computes the exact L1∪P₃∪Q₃∪P₅ marginal union. It uses its own splits and factoring: Pollard–Brent plus MR, no shared sieve. It takes 49 s at r=929 and under 0.6 GB.

At 911, 919 and 929, compared with the author's bound:

| r | L1 | P₃ cells | Q₃ cells | P₅ cells | Q₃ (author) | P₅ (author, corr.) |
|---:|---:|---:|---:|---:|---:|---:|
| 911 | 95 | 324 | 954 | 1504 | 15723 ppm | 53785 ppm |
| 919 | 77 | 226 | 866 | 1536 | 15610 ppm | 54829 ppm |
| 929 | 48 | 458 | 888 | 1570 | 15489 ppm | 56553 ppm |

* L1 and P₃ agree exactly with the author.
* Exact Q₃+P₅ costs ≈2+2 ppm at each of these primes, against the author's ≈70000 ppm. At 929 there are only 837 Q₃ data and 1335 P₅ data.
* Feeding the exact depth-3 mass into the author's own K≥7 chain gives the exact-depth3 ledger (`budget_exact.txt`):
  * passes at 757, 811, 853, 887, 907, 911, 919 and 929, with margins 1764 / 47680 / 32321 / 48338 / 83854 / 63302 / 96481 / 72872 ppm;
  * fails at 701 and below, because the P≥7 bounds exceed 1.
* So a full exact-depth-3 sweep over 701<r<919 would very likely lower the threshold into the 750s, conditional on review of my engine.
* Validation of the engine: it reproduces `R17_EXACT.md`'s `union.tsv` at all 41 primes 17..211 (all four columns), and the depth-3 totals of all 38 `rtree*_d3.txt` files. Its P data dumps at r=17 equal the complete M17B lists for K=5, 7, 9 and 11.
* The engine is unreviewed, so this is EVIDENCE for the author to pursue, not a certificate.

**F3 (libm dependence at the binding prime, quantified).** The new tables (p3, p5, q3, qcap, qrows, qscan/qleft, p5fine, p7, layer, local, pack) are integer-only. I grepped them; `z78_p5fine.c` includes `<math.h>` but never uses it. Inherited, libm-dependent ingredients at 929:

| ingredient | amount at 929 |
|---|---:|
| SE/ZL `bound(P,·)` rows that win at K≥17 | ≈16748 ppm |
| higher-Q tables | 3072 ppm |
| tails (ZL Lemma 1.2 constants through PL) | 12164 ppm |
| total | ≈31984 ppm |

* Against the corrected 834 ppm margin, the author's 929 certificate breaks if those inherited rows understate their values by about 2.6% in aggregate.
* With exact depth-3 (F2) the margin is 72872 ppm, and the inherited rows could be wrong by more than 200% without effect.
* The libm condition is not removed by z78. The STATUS label must keep it, as the author's §0 already says.

**F4 (form): labels, stale text, ordering prose.**
* §0 says "PROVED … relative to SE/ZL/z77", but the theorem also uses BBR (packed small shifts) and Dirichlet (§2). Add both.
* §§3–4 are internally labelled CERTIFIED with "independent review owed / pending". This review covers part of that (§4 below), not all of it.
* §§3–5 still quote the superseded checkpoints 5521, 4159 and 1447 as "PROVED/CERTIFIED checkpoint". Mark them superseded, or a reader may take them as live thresholds.
* §5's "Process higher P without Q beyond depth 3" contradicts the implementation (F1).
* Minor:
  * "the mission's 917 includes the endpoint 7219" is jargon;
  * the comment in `z78_p5.c` ("one factor even if u<Y+1? use thresholds below instead") and the one in `z78_p7.c` ("see runtime guards / note") are stale;
  * the note's prose is extremely compressed; e.g. §5's survival map should state explicitly that the alive set must be a union of depth-(D−1) cylinders, which is exactly the hypothesis F1 violates.

# 3. Mathematics checked (all correct unless stated)

* **§1 tails.** Per term, d log(term/√N)/d log N ≤ α−½+β/log N ≤ −0.02+2/(800 ln 2) = −0.01639 < −1/64. One step of two exponents adds 2 ln r > 8 ln 2 to log N, giving a factor ≤ 2^{−1/8} < 12/13. P mass ≤ (2/√r)·0.014·13 = 0.364/√r. Q: −0.24+2/(100 ln 2) = −0.2111 < −1/5, giving a factor ≤ 2^{−8/5} < 1/3 and mass ≤ 2·0.00001·1.5. The code matches (`F(364,1000*isqrt(r))+F(3,100000)`), and the start indices match (P breaks at n≥2^800, Q at n≥2^100).
* **§2 Dirichlet construction.**
  * (r/ℓ) = (−ℓ/r) for ℓ≡3 mod 4, and −ℓ≡u is a nonsquare, so r^{(ℓ−1)/2} ≡ −1 mod ℓ with an odd exponent.
  * With a=c=1, d=(ℓ+1)/4 and b=(N+1)/ℓ: 4bd = N+1+b, so e=b+1=a+b.
  * b, d and e are units because u≢1 mod r.
  * The centre is −a/b = −ℓ mod W.
  * Hence the boxes are dense and any sterile set is nowhere dense. The key-period obstruction is also correct.
* **§2 nonregularity.** Correct. Each nonsquare prefix of length L has an accepted extension of length <L+s. Distinct prefixes give distinct words, so there are ≥(r−1)r^{L−1}/2 of them. The ZL tails give #Λ_D ≤ ε_D r^D with ε_D→0, because the exponents are ≤0.48<½ (P) and ≤0.76<1 (Q). For fixed s, Σ_{D<L+s} ε_D r^D ≤ r^s·max ε·r^L = o(r^L). The safety-automaton corollary is also correct: in a finite DFA, either every live state has a killing word of length <s, which gives measure 0, or a closed live state exists, which gives a full sterile cylinder and contradicts density.
* **§3 quintic sieve (`z78_p5.c`).**
  * The PL compression is applied correctly: a greedy g≤e, with residual exponent h costing 2h+1.
  * The rough-part bound τ(x²) ≤ 3^{⌊log₄₀₉₇ x⌋} holds because every prime factor is >4096.
  * The factor 2 applies iff g²>e.
  * The large-shift cap counts alive first digits by complete blocks plus a remainder, and is then doubled; this is valid because the alive digit set is inverse-stable.
  * Overflow guards are adequate.
* **§4 exact P₃ (`z78_p3_exact.c`).** The divisor-triple enumeration with a²≤M pruning, the large-e (a,c,d) loop and the identities e·f = N+4a²d and 2a²d ≤ N (re-derived) are all correct. My engine reproduces L1 and the P₃ marginal at 911, 919 and 929 exactly.
* **§4 Q₃ (`z78_q3.c`, `z78_qcap.py`).**
  * The small-f class is −1/4 mod f and gcd(M,f)=1. The factor 2 belongs on the small-f side only.
  * The both-large bin bound c²d ≤ (n+h)²/(4(tE−1)) follows from ef·4c²d = (F+f)²+4c²d, which gives f | F²+4c²d.
  * The qcap index ↔ (E,T) mapping matches `zbudget`.
* **§5 BBR.** The statement was verified at the source: hal-02572796, Thm 1.2, |Δ(x)| ≤ 0.764 x^{1/3} log x for x≥9995. The interval main term is ≤ H(log m+2γ) and the endpoint error ≤ 1.528 m^{1/3} log m. The code rounds upward (ln m ≤ 0.694·bitlen, 2γ < 1.16, 1.53). The lower endpoint is ≥ ⌊n/8⌋ ≥ 9995 when that branch is taken. Only consecutive M are used (P side).
* **§5 knapsack lemma.** I re-proved it:
  * θ of every item fits the capacity (θ log M < i log 2), so the greedy optimum earns ≥ θ log τ(M²);
  * blocks of 2u+1 exponents at the boundary prime; each block, with the unfunded exponents fixed, has ≤2 values of h₀|g²;
  * ⌈(2v+1)/(2u+1)⌉ ≤ 4(2v+1)^{1−β}, because (2v+1)^β ≤ 1+2βv < 2u+3 ≤ 3(2u+1).
  * In the implementation, h/32 ≥ 1−θ, the per-prime majorant uses v≤b and ω(M)≤l, and the sum is 8·A^l·Στ(M).
* **§5 Q rows (`z78_qrows.c`).** V = F²+4c²d is coprime to u=4cd in-cell, so f₀|g with g≤u is unique in its class and the count is ≤ τ(V/g). The rough part costs 2^Ω, the result is capped at diam+1, and the direct test is used when diam<64. `qscan` and `qleft` cover complementary rectangles (same h formula, threshold 128).
* **§5 layer back-determinant (`z78_layer.py`).**
  * (a,d) row: the cofactor e lies in the unit class −N mod 4ad, the index range is ≤ 1+V₁(w_c−1)/f₀², and the lower bound is e ≥ (n/2)/(4A′C′D′−1).
  * (c,d) row: the cofactor class is −1 mod 4cd.
  * (a,c) row: only the progression length is used.
  * The orientation doubling, the hi-bucketing and the loop truncations are all valid.
  * The step map's three branches are valid, subject to F1.
* **§7 p5fine `test()`.** h = h₀y^i with i∈{0,1,2}. The i=2 case is the inverse image of i=0 under h↔M²/h. For i=1 and y=1, both h₀ and g²/h₀ lie in the class −g mod e. The covering still holds when y | g.
* **§7 p7.** Prime-power hits are counted one per copy, each leftover copy costs 3 ≥ (2h+1)^{1/h}, and g₂ is a divisor, so M/g₂ majorises the rough part. Absorption is charged with factor 2, and the r⁴ saturation is valid.
* **§6 point 5, depth 11.** Every identity checks: Mb = N+e; WJ = pMa+qe, so MH = qW/17+J; eS = J+pW/17; b(pMc+D) = W(pNc/W+H), so WS = pMc+D.
  * Size chain: e = Nk/(Mc−k) and pMc ≥ W−4 give qe/W ≤ 2pqW/(17(W−4−2p)) < 3/5 for W≥1000.
  * From that: J < (5/2)pMa/W and H ≤ 12W/(17M), so J(Hd)²(Ha) ≤ (5p/2)(12/17)³W²/16 ≈ 0.2748W² for p=5.
  * The three-index cover is complete for a≤b, and both (p,q) orders are searched.

# 4. Independent computations (own scripts, all under `ulimit -v 2000000`, one worker)

| what | script | result |
|---|---|---|
| Replay `z78_deep.py` | — | identical to `data/z78/check.txt` (5.5 s) |
| Own ledger re-implementation | `z78_xr_budget.py` | equals the author on every component except P₅, which differs exactly by F1 |
| Exact depth-3 unions | `z78_xr_exact.c` | §2 F2; full agreement with `union.tsv` at 17..211 and with the trees |
| Per-shift lemma logic vs exact #h | `z78_xr_perM.c` | 0 violations (counts below) |
| Layer/packed sanity vs exact (N=23⁷) | `z78_xr_layercheck.c`, `z78_xr_layercmp.py` | bounds ≥ exact at every j (sanity only) |
| Determinism replays | author binaries | p3/17, q3/17, p5fine/900, p7/900, qrows/517, layer/66, point/check and point 11_1_J are all identical |
| Point-5 depth 11 | `z78_xr_point.py` | 0 hits in all six runs (counts below) |
| Point engine tests | `z78_xr_point.py test`, `z78_xr_pointe2e.py` | exact set equality (counts below) |

Per-shift tests (`z78_xr_perM.c`), all with 0 violations:
* p5 and p5fine at r = 929, 919 and 911, e < r². My p5fine per-shift sums equal the author's `p5fine` j=0 column *exactly* (2263859, 2213244, 2174492).
* q3e and q3f at 929.
* p7 at 503 (e < 2²²) and 599 (e < 2²¹).
* The exact class counts are 10³–10⁴ times smaller than the bounds.

Point-5 depth-11 runs (`z78_xr_point.py`):
* The J mode uses a different reconstruction from the author's: e | B, then M | gcd(A, N+e).
* The Hd mode uses its own root windows.
* Results for (1,5) and (5,1), modes Ha / Hd / J: 0 hits in each run, X = 4258519. Run times were 4–133 s.

Point-engine tests:
* `test`: 9330 domain comparisons with synthesized endpoints (r=17, K=5, 7, 9) give exact set equality: 598/302/1270 positive hits.
* `pointe2e`: own and author engines at the theorem cutoff, r ≤ 103. All sets agree, but the test is **vacuous**: no P box at depth ≥3 contains any of 5, 1/5, 3, 1/3, 2, 1/2, 4, 1/4 at any tested r. The size theorem is therefore verified by proof only, not by a positive end-to-end hit.

# 5. Scope and what is not checked

* Not re-derived: the inherited z77 `moment`, `tau_sum`, `cap`/`divcap`, `tau_major`, z77 routes/fine, the SE/ZL decimal tables and PL's tail constants. I used them as given.
* Not recomputed in full: the new tables over all 916 primes. Only the samples above were recomputed.
* Not reviewed: my own engines (z78_xr_*). F2 is EVIDENCE until they are.
* All-depth sterility at 17 and ES remain open; the note scopes this correctly.
