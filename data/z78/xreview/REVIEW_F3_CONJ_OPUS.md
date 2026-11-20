# Hostile cross-lab review of `notes/z78/F3_CONJ.md` (commits `main..4f173d41e`)

Reviewer: Claude (Anthropic), an Opus-class model running as a pi subagent. The exact model version is not visible to me.
There were no auth, provider or quota errors.
Scope of review: `notes/z78/F3_CONJ.md`, `scripts/z78_f3.c`, `scripts/z78_f3_hybrid.c`, `data/z78/*`, and all 10 commits since `main`.
Scratch: everything is in `data/z78/xreview/`. The main note was not modified.
Disclosure: two early throwaway diffs went to `/tmp/opus_f3_*`; I deleted both. An attempted write to a pre-existing
root-owned file, `/tmp/x.txt`, failed with a permission error, so that file is unchanged.

## Verdict

**No FATAL and no MAJOR mathematical defect.** I re-derived every lemma in §§1–3 and §5 by hand from the tuple identities
`mXB = T^n+V`, `X+B = TgV` and the covering criterion `pX+qB ≡ 0 (T^K)`. That covers:
* the second contact;
* all cube cases;
* the W identities;
* the orientation signs;
* the complexity bounds.

All of them hold as stated, with these labels:
* §0 Result: PROVED relative to the cited repo lemmas. The dependency list is incomplete; see D4.
* §4 census through N=38: correct and replayable. I suggest CERTIFIED relative to §§2–3; see D7.

Scope is stated correctly:
* Case B families only, at x*_c (c=1,2), for A=T², q=3, levels N≥4.
* Case A is excluded by FUNCTIONFIELD_ES2 §0.2.
* The note claims no all-level statement and nothing about integer ES. Nothing is overclaimed relative to ES.

The defects are form and precision issues, D1–D9 below. There is also one useful missed observation, D6: an exact c↔−c
symmetry, which makes the c=2 runs logically redundant.

## 1. Mathematical re-derivation (all hold)

Notation is as in the note: P=deg p, Q=deg q, P+Q=1, κ=(q−p)/T, b=n−K, δ=N−b∈{3,4}, U=T+c.

**§1 setup.**
* Orientation A means deg C₁ ≥ N and orientation B means deg w₁ ≥ N+1. These come from FF_THIRDS_CORNER Lemma 1.2 /
  Prop 2.1. The two cases are disjoint because their sum would exceed n.
* Covering ⇔ pX+qB ≡ 0 mod T^K. This is Lemma 3.1 (needs K ≤ n, i.e. N≥4). Both orientations give the same polynomial
  w₁+uC₁.
* The short-side congruences hold: A gives Mg ≡ −c (T^N), and B gives uMg ≡ c (T^N) from E' ≡ −u⁻¹. So d+y ≥ N in A and
  ≥ N−1 in B. Hence v = L−1−y ≤ n−1−N in A and ≤ n−N in B, which is < K−Q.
* Therefore deg(pMX+qV) ≥ K forces d+r+P ≥ K.
* L ≥ N > N−2 ≥ d ≥ r, so L > r+1, V is monic, and deg H = L+Q−K.
* The triangular reconstruction of X from m is correct:
  * coefficient x_i first enters at degree z+K+h+i with coefficient lc H;
  * the quadratic term only involves x_j with j>i, because P+r < L+Q;
  * the V-term lies below n+Q−r.
* Cost 3^{h+min(z,r)} ≤ 3^{N−max(d/2,N−d)} ≤ 3^{2N/3}. In fact h ≤ N−2−d, which is slightly better than the stated N−d.

**§2 ABC.**
* Mason–Stothers on pMX+qV = T^K J, after removing the U-power gcd, gives K ≤ deg rad(uMV). The steps are correct.
* Inseparable branch. ord_U F = i−j−1 in A and i+1−j in B, so exactly one of i, j is nonzero. Correct.
* j>0: TUf′−jTf = T^n(nU−jT) is nonzero also when 3|n, since it then equals −jT^{n+1}. So deg gcd(f,f′) ≤ 1.
  MX = mX² = A³ forces every prime of M to have multiplicity ≥2, so M ∈ {1, π²} with X=π.
* i>0, 3∤n: f′ = nT^{n−1}, so f is squarefree and M | U.
* Endgame for both of these cases: d+r+P ≤ 4 < K for N ≥ 4. At N=4 the windows 2d+P ≥ K and d ≤ n+Q−K are empty anyway
  (Mpool=0 in the data).
* i>0, 3|n: V = D³ divides φ = T^n+MX with φ′ = iU^{i−1}A³ coprime to V, so V=1. The parity law then gives n even, and
  U | M | T^n+1 yields 2=0. Correct.
* This branch **uses FF_ODD_ABSENCE Cor 1.7**, which is not in the §0 label (D4).

**Active-prime sharpening.**
* F′/F = Σ_{π∈R₃} e_π π′/π has simple poles on R₃ and is O(1/T) at ∞.
* F ≡ −1 mod T^K, with all polynomials T-units, so T^{K−1} divides the numerator. Hence deg R₃(F) ≥ K.
* The refinement when 3 | deg F is correct.
* "MX or V a cube ⇒ deg R₃ ≤ 1+v or 1+d < K" is correct, using d ≤ N−2 and v ≤ N−2.

**§3 W identities.** I re-derived each of the following algebraically, and checked them numerically (see §2 below):
* MH = qT^b+J and VS = pT^b+J, using T^K VS = pM·TgV + (q−p)V;
* W integral, with W(0) = κ/M(0) ≠ 0 because δ>0;
* VW = T^δHJ − κpX, using MH−VS = κT^{b+1} and δ+b+1 = K;
* pXS = T^{b+1}W − qH;
* T^δSH − W = pqg;
* pgJ = T^bW − κH.

The degree w = δ+deg S+j−d = r−v+2P−1 is correct. It needs δ > Q and deg(pMg) ≥ N, so that lc S = lc p.

**Second contact.**
* With A₀ = qB−pX, A₀² = (qB+pX)² − uBX, using 4=1 and pq=u. So mA₀²+uV = T^n(mT^{2K−n}H²−u), with D(0) = −1. Correct.
* If G is a cube, every prime of V off u(p+q) has multiplicity ≡ 0 (3), because A₀ ≡ −(p+q)X mod V and gcd(X,V)=1.
  Then R₃(F) | u(p+q)rad M has degree ≤ d+2 ≤ N < K, a contradiction. Correct.
* n ≤ z+L+Q+1+v gives v ≥ r−Q−1, hence w ∈ {0,1} in A and {0,1,2} in B.
* W is monic since lc S = lc J = lc p and lc p² = 1.
* w ≡ d+1 (2) follows from v ≡ z ≡ n.
* The counts of 3 (A) and 9 (B) monic T-unit W are correct.

**Complexity.**
* The 2/5 bound: e ≤ d+r−N and e ≤ N−d+r−v+1 give 2e ≤ 2r−v+1, then 5e ≤ 2N+1. Correct.
* The final N/3 bound: min(h, j) ≤ min(N−d−2, 2d−N) ≤ N/3. Berlekamp is deterministic over fixed F₃, and divisor
  counts are 3^{o(N)}. Correct.

**§4 near-miss family.** I verified it by hand: MB = T^{3k}+T^k−1, (1+T)X+B = T^{2k}, and gcd(TV, X−1) = T(T−1) even when
3|k. The witnesses at N = 9, 12, …, 36 (orientation B, d=k, r=k−1, v=k=r+1, w=0) all match.

**§5 sufficiency.** The surviving data give a tuple of parameter s with covering at depth N(s)+1. By FUNCTIONFIELD_ES3
Lemmas 1.1/2.1 (EE′ = D) this is a valid Case B family at level N. Necessity follows from §§1–3. Correct.

**Scope.** Integer ES is not touched. Case A at x*_c is covered by FUNCTIONFIELD_ES2 §0.2. N ≤ 3 comes from
FF_THIRDS_CORNER §2 / FUNCTIONFIELD_ES3 Lemma 2.1.

## 2. Independent computation (fresh code; shares nothing with `z78_f3*.c`)

`data/z78/xreview/brute.c` uses plain int8 coefficient arrays and assumes only Lemma 3.1. It enumerates m′ and the short
side freely, fixes the long side mod T^{Kt}, and enumerates the long side's higher digits freely. There is no
quotient/remainder shortcut and no reconstruction trick.

**Census sanity.** With Kt=1 it finds exactly **348 tuples for s ≤ 17**, the known `bsE_famcount 3 2 17` count
(`census_s4_17.txt`).

**Stage-by-stage comparison** (`compare.py`). I recomputed, from scratch and per (N, s, c, orientation):
* the counts of `z78_f3`: monicV, vbound case1/2, integralG, hits;
* the count of `z78_f3_hybrid`: near.

Results:
* N=4..15: 96 rows, lopsided patterns (plus all patterns for N ≤ 10). **0 mismatches**.
* Kt=1 full-census mode, N=4..9: 44 rows, 0 mismatches.
* Nonvacuous: 595 monicV, 14 vbound and 8 near survivors matched exactly. These include the near-miss family at N=9, 12
  and 15.
* All-pattern runs (N ≤ 10): no covering tuple in any pattern, balanced ones included. Every deep non-lopsided
  candidate was an exact w₁ = (T−1)C₁ non-tuple at c=2, as Lemma 1.2 predicts.

**Identity tests on real tuples** (`check_ids.py`). Every identity of §§1–3 was checked with K′ = actual depth:
* 348 census tuples at x*_c;
* 46 tuples at degree-2 points u = 1+cT±T²;
* 2 deep tuples at n=27, depth 14.

Checks and results:
* MH, VS, S-integrality: 1488 checks, 0 failures.
* W-integrality, VW, pXS, T^δSH−W=pqg, pgJ: 112 checks each, 0 failures.
* W(0) ≠ 0 whenever δ > 0 (76/76). It fails only at δ=0, which never occurs in the note.
* Second-contact identity: 0 failures.
* deg R₃(F) ≥ K′ whenever F′ ≠ 0: 1452/1452.
* deg R₃(G) ≥ n whenever G′ ≠ 0: 104/104.
* "G cube ⇒ deg R₃(F) ≤ d+2": 40/40.

G′=0 does occur at lower depth, so the second-contact lemma is not vacuous.

**Replay.** I rebuilt `hyb`. `hyb 4 32 1` (17 s) and `hyb 33 38 1` (7 m 38 s) are byte-identical to `data/z78/hybrid_1.txt`.
The full 4..38 run fits the 1800 s limit.

**Code audit.**
* Bit-plane add/neg/mul/divr/inc are correct.
* The triangular X-reconstruction signs are right: the e = v·lc H choice and the lin update use 2 = −1.
* The hybrid lift's J = J₀+HD class and lc D = c are correct in both orientations.
* X = ⌊T^K J/(pM)⌋ is valid in the v-window. test() re-verifies everything.
* Bit widths are fine: degrees ≤ 61 < 64 (N ≤ 31) and ≤ 79 < 128 (WIDE), and 3^40 < 2^64.

## 3. Defects and exact repairs

**D1 (minor, dangling reference).** §1 ends with "This gives the exponent in §0." The §0 Result no longer states an
exponent. *Repair:* "This route therefore costs 3^(2N/3+o(N)); superseded by 3^(N/3+o(N)) in §3."

**D2 (minor, stale heading).** "Upper search exponent 2/5 (PROVED; …)" is superseded by the later "3^(N/3+o(N))".
*Repair:* change the heading to "Upper search exponent 2/5 (PROVED; superseded below by N/3)".

**D3 (minor, notation).** "(these symbols are local to this section)" is false: b, δ, κ, S, J and W are reused in the §4
hybrid ("qT^b") and in §5 ("T^(b+1)W"). b also clashes with deg C in FF_THIRDS_CORNER. *Repair:* "these symbols are
used in §§3–5; b here is n−K, not deg C."

**D4 (label / dependencies).** The §0 label is "PROVED (rel. Mason–Stothers and the tuple lemmas in §1)". The proofs
also use:
* FF_ODD_ABSENCE Cor 1.7 (parity), in the i>0, 3|n cube case and in the §5 and hybrid filters;
* FF_THIRDS_CORNER Lemmas 1.1, 1.2, 3.1, Cor 3.2, Prop 2.1;
* FUNCTIONFIELD_ES3 Lemmas 1.1, 2.1, 2.2;
* FUNCTIONFIELD_ES2 §0.2 (Case A), for the scope.

*Repair:* replace the label with "PROVED (rel. Mason–Stothers; FF_THIRDS_CORNER L1.1, L1.2, L3.1, C3.2, P2.1;
FUNCTIONFIELD_ES3 L1.1, L2.1, L2.2; FF_ODD_ABSENCE C1.7)". Add a short Sources list.

**D5 (garbled sentence).** §3: "Also rad(uMV)≥K as above, not merely a bound on its total degree." *Repair:* "Also
deg rad(uMV) ≥ K, and indeed deg R₃(F) ≥ K (§2)." Alternatively, delete the sentence.

**D6 (missed exact symmetry; affects how the evidence is described).** Define σ(f)(T) := (−1)^{deg f} f(−T). σ is
multiplicative and preserves monic T-units and degrees.

For a tuple with the parity law z ≡ t ≡ s (2), σ preserves the tuple: σm·σw₁·σC₁ = T^n+σv₁ and σw₁+σC₁ = Tσg·σv₁. This
uses deg v₁ ≡ n, a₁ ≡ b₁ and y+t₁+1 = max(a₁,b₁).

σ also sends E ≡ −(1+cT) to σE ≡ −(1−cT) mod T^K, since y+z+a₁ is odd. So **covering tuples of x*_1 and x*_2 correspond
bijectively**, with the same level, orientation and degree pattern.

Evidence:
* I checked σ on all 348 census tuples, with c-depths swapped (`sigma_check.py`): 0 failures.
* This explains why `hybrid_1/2` and the post-parity stages of `f3_1/2` have **identical counts**.
* The c=2 witnesses are the σ-images of the c=1 witnesses, e.g. 11/12121/… ↦ 21/11111/….

So "both c" is one result, not two independent ones.

*Repair:* add a lemma ("x*_c ↔ x*_{−c} via T ↦ −T; PROVED rel. FF_ODD_ABSENCE C1.7"). Present the c=2 runs as an engine
consistency check, not independent coverage. Future runs could do c=1 only. Add a sentence to the §5 remark: the
orientations are not identified, but the two c are.

**D7 (label of the finite result).** "Finite result (EVIDENCE)" describes an exhaustive exact computation. By the AGENTS
convention this is **CERTIFIED (rel. the PROVED §§2–3 windows)**, with this coverage statement:
* `z78_f3_hybrid` is the only engine for 32 ≤ N ≤ 38;
* `z78_f3` covers N ≤ 31, with shared arithmetic;
* `zt_lop` (FF_THIRDS_CORNER) covers N ≤ 20;
* this review's independent brute covers N ≤ 15 at stage-count level;
* c=2 is equivalent to c=1 (D6).

*Repair:* relabel accordingly, and keep "not an all-level proof".

**D8 (STATUS delta wording).** "only low-deg g', with a monic T-unit determinant of degree ≤1 (A) or ≤2 (B), remains"
can be read as nearly closed. *Repair:* "Conj. 0.2 over F₃[T] (open): every covering tuple has deg g′ < N and a monic
T-unit determinant W of degree ≤1 (A) / ≤2 (B); none exists through level 38 (CERTIFIED rel. §§2–3; z78 `F3_CONJ.md`
§§2–4)."

**D9 (unlabelled interpretive remarks).** The following sentences are Assessment, not part of the PROVED content:
* §3: "This is not the old forced-E_M lottery: the small degree of W is a consequence of two independent congruences…";
* §2: "it uses only a simple zero of u, not a presumed bound on rad(E_M)".

*Repair:* prefix "(Assessment)" or trim.

Nits:
* "n=s−2" is defined twice (§1 and §2).
* §2 "at N=4 the only marginal alternative…" can be replaced by "N=4 is vacuous: 2d+P ≥ K contradicts d ≤ n+Q−K".
* The replay line omits `-std=gnu11`. It is harmless, but the source headers recommend it.
* Consider stating the measured replay time (≈8 min per c for 4..38).

## 4. Challenges and debate

1. **Is the census engine using the best proved route?** No. §3 proves a complete 3^{N/3+o(N)} search: index by H plus
   ≤ 9 W, then X | T^{b+1}W−qH. The census engine instead grows like ≈3^{0.45N}: 1.3·10⁸ trials per row at N=38. With
   the W-route and D6 (c=1 only), levels around 50–55 become feasible at the current budget. This is a recommendation,
   not a defect.
2. **There is a second structured near-miss family, not documented.** Orientation A at N=24 and 33 (n = 45, 63 = 9k′,
   k′ = 5, 7) has:
   * m = 1+T;
   * X = T^{4k′}+T^{3k′}−T^{2k′}−T^{k′}−1, from the witnesses 200002000020000100001 and 20000002…;
   * σ-images at c=2.

   It should be recorded, or explained like the §4 B-family. The next member would be at N=42.
3. **Deep balanced near-tuples exist.** At s=29 (N=15) there are genuine tuples with depth 14, against the 16 needed. They
   are balanced (a₁=14, b₁=12), i.e. they lie in the Liouville-excluded region, so they do not threaten the lopsided
   analysis. They do show that the "Liouville gap" at small s is only about 2 digits.
4. **Does the result move the target?** Modestly. It is a genuine structural sharpening:
   * case 2 is dead in both orientations;
   * W is bounded, so the ≈3^{N} lottery becomes a 3^{N/3} exact search;
   * the census extends from N=20 to N=38.

   The core obstruction is unchanged: no all-level mechanism forces X ∤ T^{b+1}W−qH. The relation pXS + qH = T^{b+1}W
   with deg W ≤ 2 is itself an S-unit-type equation. A third Mason/log-derivative contact on it, or on MW = T^δSJ+κq,
   might bound h or j. I tried this briefly and found the radical slack too large: the degrees of XSH are of order N.
   No obstruction to the attempt either. The note's Assessment (next step) is reasonably scoped.
5. **Triage.** TARGET is acceptable, given that STATUS §2 item 5 already lists Conj. 0.2. Cross-lab review is now
   supplied by this file, assuming the author lane was non-Claude. Labels should be upgraded only after D4 and D7 are
   fixed.

## 5. Replay of this review
```
cd data/z78/xreview; ulimit -v 6000000
gcc -O2 -std=gnu11 -o brute brute.c
./brute 3 14 1 tuples_all_n3_14.txt > rows_all_n3_14.txt
./brute 15 24 0 tuples_lop_n15_24.txt > rows_lop_n15_24.txt
./brute 25 28 0 tuples_lop_n25_28.txt > rows_lop_n25_28.txt      # ~5.5 min
./brute 15 18 1 tuples_all_n15_18.txt > rows_all_n15_18.txt      # ~10 min
uv run --offline --no-project python compare.py rows_all_n3_14.txt rows_lop_n15_24.txt rows_lop_n25_28.txt
# brute_gen.c = brute.c + args: e (u=1+cT+eT^2), Kt override
./brute_gen 2 15 1 census_s4_17.txt 0 1 > rows_census.txt        # 348-tuple census
./brute_gen 3 15 1 tuples_deg2_e2.txt 2 > rows_deg2_e2.txt        # (and e=1)
uv run --offline --no-project python check_ids.py census_s4_17.txt tuples_deg2_e1_tag.txt tuples_deg2_e2_tag.txt tuples_lop_n25_28.txt
uv run --offline --no-project python sigma_check.py
gcc -O3 ../../../scripts/z78_f3_hybrid.c -o hyb; ./hyb 4 32 1 | diff - <(head -116 ../hybrid_1.txt)
```
(`*_tag.txt` = the deg-2 tuple files with an `e=<e> ` prefix per line.)
