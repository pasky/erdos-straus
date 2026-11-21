# Hostile cross-lab review (Claude Opus), round 2 — `notes/z80/ES_JUGULAR.md` §§6–9 and new §0

Author lane: GPT-6.2 Astra. Reviewer: Claude Opus. The scope is commits `main..521c20803`, concentrating on what is new
in `521c20803`: §0 (rewritten), §6 (parity tests), §7 (Theorem E), §8 (Theorem F), §9 (Corollary G), the E–G falsifier
paragraph, and `data/z80/jugular/r2/*` with the eight new scripts. §§1–5 were covered by
`REVIEW_ES_JUGULAR_OPUS.md` and `REVIEW_ES_JUGULAR_D_OPUS.md`. I checked here only that the fixes from those reviews
are present in `93e2729`/`3efcb41`. They are: the 4^{ω} BT weight, the Σχ_Δ ideal count, the O(√X log X) triple count,
the sharpness control and the trap remark.

## 0. Verdict

* **No FATAL and no MAJOR mathematical error in §§6–9.** I re-derived E, F and G line by line. I also checked F's
  arithmetic premises numerically on 2950 actual Type I solutions, and the §6 data by independent brute force and
  partial byte-for-byte replay (§5 below).
* **One MAJOR substance/significance issue (E).** Theorem E is correct. However, its advertised features ("optimal",
  "cap zero on a planted inert coset", "working shift ≥ exp(c√log p)") are all dominated by the classical one-block
  Type II identity with a single *nonsquare* planted block g≡−1 (mod q). Leading the §0 Result with "an optimal ternary
  packet" therefore misleads. E must be demoted, or the domination stated explicitly.
* **MEDIUM form/scope issues:**
  * §0 Result conflates G's p-scale exponent with D/F's q-scale thresholds, and it misuses "rough".
  * G is labelled PROVED relative to an *unmerged* internal branch, and its pointer is dangling in this tree.
  * The §0 Review line does not record that §§6–9 were unreviewed. It should now cite this file.
* **MINOR:** wording of "every primitive Type I tuple"; F has no sharpness control; one falsifier line (E-F2) is a
  non-sequitur; the §6 CERTIFIED block does not state its independent-check coverage; a dangling pointer to
  `BEYOND_34.md`; small replay-documentation gaps.

Recommended triage stays **BARRIER-SCOPED**, with **STATUS delta: none**. D+F together are the substantive content
("every solution at the selected primes leaves the small-prime profile in a specified squarefree kernel"). G is a
one-step strengthening of Lane 7. E is a METHOD-level remark. §6 is NULL/DATA.

---

## 1. §7, Theorem E (cap-zero packet)

### 1.1 Correctness — verified
* **Algebra.** h generates the squares (order Q), and g_i ≡ h^{3^i}. Balanced ternary with k digits covers an interval
  of 3^k ≥ Q consecutive exponents, so every square, and in particular −L (L nonsquare, q≡3 (4)), equals ∏g_i^{ε_i}.
  Then A=∏_{ε=+1}g_i and B=L·∏_{ε=−1}g_i satisfy q|A+B. D=GL/(AB) is the product of the unused blocks, and C=(A+B)/q.
  With (a,b,c,d,e)=(A,B,C,D,q) one has 4abd=n+e and a+b=ce, so 4/n=1/(ABD)+1/(nACD)+1/(nBCD). Equivalently
  4ABCD=A+B+nC, i.e. **N_II(n)≥1** in the Z58 sense. For prime n, ABD=(n+q)/4<n, so this is genuine Type II. q∤L
  follows from (n/q)=−1. ✔
* **k=⌈log₃Q⌉ and the optimality counting** (square blocks, each used once in A, B or neither, L indivisible): there are
  at most 3^k ratios. The set of ratios is closed under inversion, so putting L in A instead of B adds nothing. L cannot
  be unused because −1 is a nonsquare. Hence 3^k≥Q. ✔ This holds *in that model*.
* **Moving instances (CRT/Linnik).** g_i≡1 (M) with M=lcm(840,1..j)≤q makes G odd and coprime to M, so
  gcd(M,4G)=4. The condition −q≡1 (4) is compatible with p≡1 (8). The class is reduced, its modulus has log
  O(k log(Mq))=O(log²q), and Linnik gives log p=O(log²q). So q≥exp(c√log p). p≥4G−q>q. ✔
  * Numerical check, q=1019: k=6 and the packet covers all 509 squares. I found a prime p≈10^{40.3} in the planted
    class with p≡1 (840) and (q/p)=−1, and verified the identity.
  * The repository's `packet.txt` (M=1, q<1000, 19704 reconstructions) agrees.
* **Falsifier F3 at 4545** is logically right. E's output is an N_II point, and N_II(4545)=0: I re-checked this by
  direct enumeration of 4abcd=a+b+nc, e≤4n. So E's hypotheses cannot hold at 4545. Note that 4545 *does* have 840
  solutions with exactly two 4545-multiple denominators (`comp.csv`, confirmed by brute force). The distinction
  between N_II and "k=2 bin" is therefore essential and correctly drawn.

### 1.2 MAJOR — E is dominated by a one-block classical identity
Plant a *single nonsquare* block g≡−1 (mod q), g≡1 (mod M), g>2q. Take (a,b,c,d,e)=(g,1,(g+1)/q,L,q):
then 4abd=4gL=n+q and a+b=g+1=cq, for **every** n≡−q (mod 4g). There is no Legendre condition, no ternary
packet and no coset.
* I verified the identity for 2999 consecutive members of the window at q=1019, g=731641.
* With p≡1 (840) and (p/q)=−1 imposed by CRT, I found a prime with log q/log p=0.257. In general Linnik on a modulus
  ≪q⁴ gives **q≥p^{c}**, against E's exp(c√log p).
* The window density is ≈1/(4g)≈1/(4Mq), against E's 1/(4G)≈(Mq)^{−k}.

The only role of "square blocks" is to *define* the model in which ternary is optimal. Nothing in §7 motivates
excluding nonsquare blocks: their residuosity mod q is unrelated to p's profile. In B2_ACROSS_FIELDS terms the cap-0
event is Rat_q(K)∩{−1,−p}≠∅, and a planted g≡−1 hits the target −1 directly. Consequences:
* "The block count is optimal" must be qualified **in the same sentence** as "among square-block packets". Otherwise it
  reads as a statement about planted cap-0 certificates in general, and there it is false (one block suffices).
* "Thus the working shift can be ≥exp(c√log p)" should be dropped or replaced by the trivial p^{c}.
* The §0 Result should not lead with E. Suggested replacement: "On positive-density least-nonresidue profiles every
  Type I and Type II solution has a prescribed squarefree kernel with a prime factor above exp(q^{β}) (D/F). At almost
  all p the smallest denominator has a prime to exact first power above exp((log p)^{1−o(1)}) (G, rel. Lane 7).
  Remark E: ternary is the optimal square-block cap-0 packet, but a single nonsquare block already covers whole
  windows."
* Triage of E: METHOD-CX/NULL ("square-alphabet packets are a self-imposed restriction"), not a theorem worth a
  headline.

### 1.3 Minor
* "every n≡1 (4)" is redundant, since 4|n+q and q≡3 (4) already force it. Harmless.
* Falsifier E-F2 ("restrict E to q≡3 (8) at p≡1 (8): (p+q)/4 is odd…") states a fact but not its relevance to 8/131,
  8/241 or R₈. Either say "E never touches numerator 8; in this sub-case not even an 8-window exists", or drop it.
* `notes/z80/BEYOND_34.md` is cited but does not exist on this branch. It lives on `side-agent/z80-beyond-34`. Give the
  branch and commit, as is done for Lane 7.

## 2. §8, Theorem F (Type I, cofactor product m=ab)

### 2.1 Premises — verified symbolically and numerically
* ET Type I in the note's orientation is 4abd=pe+1, a+b=ce, with denominators pabd, acd, bcd. The coprime
  representation is canonical: cd=gcd(y,z), a=y/cd, b=z/cd, d=x/(pab). Hence m=ab=lcm(y,z)/gcd(y,z) is
  **intrinsic to the solution**, and "every primitive Type I tuple" really means "every Type I solution" (§2.4).
* Identities: ef=4a²d+1 and bf=pa+c with f=4acd−p>0. Also x_min=acd≤3p/4, and c≤pb makes acd the smallest.
* (d/p)=−1 (T10): I re-derived it for p≡1 (8) via (−d/f)=1, f≡3 (4), f≡−p (4d) and Jacobi reciprocity. Hence
  (ab/p)=(d/p)=−1, since 4abd≡1 (p) and p∤ab.
* Numerical check: for all 129 primes p≡1 (8) below 4000, all **2950** Type I solutions were reconstructed. Every one
  satisfies the coprime ET form, (d/p)=(ab/p)=−1, acd=min≤3p/4, f>0, ef=4a²d+1 and bf=pa+c. There were 0 violations.
* On the profile (all odd l≤Y except q are residues, 2 is a residue since p≡1 (8), and Z≤Y), a Z-smooth sf(m) forces
  q|sf(m). ✔

### 2.2 Main-term budget — verified, exponent 1/15 correct
At fixed coprime (a,b) there are τ(a+b) choices of e, each giving one reduced class mod 4ab (e odd, (e,ab)=1). The
profile-relative cost is ≤C₀2^{ω(ab)}/φ(ab). Cauchy–Schwarz in the box with α=1/log Z:
* First factor: coprime pairs with ab=m contribute 2^{ω(m)}·4^{ω(m)}=8^{ω(m)}, giving (log Z)^8. The mandatory q
  contributes ≪1/q, since q^{α}≤e. At l>Z only even total exponents occur, and they have bounded mass because
  2−2α>1. The result is ≪(log Z)^8/q before the root, and stays true if coprimality is dropped.
* Second factor: Σ_b τ(a+b)²/b≪log³(3B), via τ²≤τ₄ on an interval of length ≤4B.
* Dyadic sum: Σ_{i≤j}2^{−α(i+j)/2}j^{3/2}≪α^{−1}·α^{−5/2}=(log Z)^{7/2}, plus a loglog factor from m/φ(m).
* Total: q^{−1/2}(log Z)^{4+7/2}loglog=q^{−1/2+15β/2+o(1)}, which is o(1) iff β<1/15. ✔ The constants are uniform in q.

### 2.3 Large-m tail (the "two-root" step) — verified
* T<m≤√X: BT with modulus 4m≤4√X and ≪m^{ε} classes. The tail over m=s h² converges. ✔
* √X<m≤X^{3/2}: there are O(1+X/m) integers per class. Over s h² this gives X^{3/4+ε}+X^{3/4}=o(X/log X). ✔
* m>X^{3/2}: b≤pa+c≤2Xa, so a≫X^{1/4}. Write a=s₁u², b=s₂v². For each (a,d) with ad≤X and each e|4a²d+1 one has
  (a,e)=1 and e odd. If (s₂,e)>1 there is no root. Otherwise there are ≤2^{ω(e)} roots of s₂v²≡−a (e), because
  square roots of a unit modulo an odd prime power are ≤2. The range is v≤√(eX/(ad)), from b≤ce and c≤X/(ad).
  * Count per (a,d): ≪X^{ε}(1+√(X/(ad))).
  * Summing over d: ≪X^{1+ε}/a.
  * Summing over a=s₁u² with u≫X^{1/8}: X^{7/8+ε}=o(X/log X).
  * Each (a,d,e,v) fixes (b,c,p). ✔
* All three m-ranges together cover every m. Taking X→∞ before T→∞ is legitimate. Finite truncations have natural
  densities. ✔

This closes the gap flagged in round 1's "next step". The tail is controlled through b's square part, not through
the large Type I modulus, as the note says.

### 2.4 Minor
* Write "every Type I solution (in its canonical coprime ET representation)". As written, "every primitive Type I
  tuple" invites the misreading that imprimitive solutions are exempt.
* The sentence "In the first factor keep coprimality, q|ab and Z-smooth kernel, extending to all a,b" is
  self-contradictory as worded. Say "drop the box; keep q|ab and the smooth-kernel condition (coprimality optional)".
* There is no sharpness control for F analogous to D's. One exists for some q: a=1, b=q, an odd e|q+1 with e≡3 (4)
  (e.g. q=11, e=3), and p≡−e^{−1} (4q) in the profile class give a Type I point with sf(m)=q on a positive-density
  class. Add it, or state that none was checked.
* Name BT and CRT-PNT explicitly in F's "rel." list. "§5 inputs" is opaque in a header label.

## 3. §9, Corollary G

### 3.1 Correctness rel. Lane 7 — verified
I read `notes/z80/EXTREME.md` §1 at `62fefacf8` on `side-agent/z80-extreme`. The sparse-set transfer bounds the number
of *solutions*, hence of primes, with x∈S by ≪(X|S|)^{1/2}log^{C/2}X, for arbitrary S⊂[1,2X]. G's step:
1. Let ℓ=P⁺(x)>Y. Either v_ℓ(x)=1, or x∈S_Y={x≤2X : ℓ²|x for some ℓ>Y}.
2. |S_Y|≤Σ_{ℓ>Y}⌊2X/ℓ²⌋≪X/Y.
3. The transfer then gives ≪XY^{−1/2}log^{C/2}X=O_A(X/log^A X), because Y=exp((log X)^{1−o(1)}). ✔

The "one letter of acd/abd carries ℓ to first power" remark, the diagonal selection over q, "every κ<1" and the
trivial "κ=1 impossible" are all fine.

### 3.2 MEDIUM — label, pointer and attribution
* `notes/z80/EXTREME.md` does **not exist** on this branch. G is a PROVED label resting on an unmerged sibling branch,
  so merge order matters. AGENTS §3 reserves "PROVED rel." for published theorems. Write **"PROVED rel. internal
  `EXTREME.md` §1 (Opus-reviewed, branch side-agent/z80-extreme@62fefacf8)"** or "CONDITIONAL on EXTREME §1". Add a
  consistency obligation: if EXTREME §1 is downgraded, G follows (AGENTS §5).
* "Supremal stretched-log exponent 1 for the smallest denominator" in the §0 Result is **Lane 7's own headline**,
  verbatim in substance. JUGULAR adds only valuation one. The §0 Result must attribute it, or claim only the v_ℓ=1
  upgrade.
* The §0 Result chains "every solution … has a rough squarefree kernel, with supremal stretched-log exponent 1". This
  invites the reading that D/F's kernels have p-scale primes. They do not: D/F thresholds are exp(q^{β}), constants in
  p. Split the two statements.
* **"Rough" is the wrong word.** "y-rough" standardly means *all* prime factors exceed y. D/F/G give *one* large prime
  (non-smooth), and in G one with exact valuation 1. Use "non-Z-smooth" or "has a prime factor >Z". The commit
  message of `eefb785` has the same issue.

## 4. §6, parity tests

### 4.1 Claims — independently reproduced (CERTIFIED stands)
* **Rank.** From the raw CSVs, with my own parser and elimination (not `z80_parity_audit.py`), the 3426×11 matrix
  (I,II,Rodd,R8,U7,HJ3g,HJ3b,HJ5g,HJ5b,h/4,1) has rank **11 over F₂ and 11 over F₃**.
  * The deduction "no nontrivial affine congruence mod 24" is valid. If c≢0 (8), divide out the 2-power of c and
    reduce to F₂. Otherwise c≢0 (3), so use F₃.
  * h(−4p)≡0 (4) at all 3426 primes, consistent with p≡1 (8).
  * The class-number column: an independent count of reduced forms matches `counts_1e8` at 20 random p<2·10⁶.
* **Residue supports.** I, II, ES, R, U7 and all four HJ columns attain all 24 residues. Rodd attains 23 and R8 21,
  consistent with the note only naming "R".
  * No column is never-zero mod m.
  * No count mod m is a *non-constant* function of h mod 32: I cross-joined `class.tsv` with `residues.tsv` and found
    no row that is h32-determined and has more than one residue.
* **§6.5.** 409 and 329617 are prime. ord₄₀₉(2)=204=(p−1)/2 and ord₃₂₉₆₁₇(2)=164808=(p−1)/2. R(409)=R(329617)=0 in
  `words.csv`. ✔
* **Panel composition** matches `z80_jugular_inputs.py`: the 14 (★) prime zeros, 285 composite zeros ≤8·10⁶, Z₇,
  17401609, 50 odd squares 3²…101², 131 and 241, plus the 38 `gstar_zeros`. The last are not mentioned in §6.4.
* **High controls.** All 14 rows of `high.txt` are prime, so "strict II = full Type II" there is legitimate.

### 4.2 Independent counts and replays (bounded, single process, ulimit -v 6e6)
* **Brute-force full ES by (x, divisors of (px)²), binned by number of n-multiples**, unordered N and Jacobi(first):
  * primes 2521, 3361, 4201, 5881, 7561, 9241;
  * composites 4545, 57, 81, 1465, 3865, 2025.

  All **12 rows match** `prime.csv`/`comp.csv` exactly (e.g. 4545: bins (1251,840,36,0)).
* **Independent Type II engine** (sympy factoring; e≤√p branch plus acd≤p/√p branch, own dedupe by (x,y,z)):
  2521 → (3,−1,3,0); 10156800001 → (207,−69,117,−5); 10917229157 → (237,−69,145,12). These match `highII.csv`
  (N, Jacobi, parity, χ₋₄).
* **Byte-for-byte replays** of the shipped C engines (compiled per REPLAY):
  * `hj` on the first 300 inputs;
  * `prime -f` on 43 primes, including the three largest;
  * `composite 4` on 120 composites ≤10⁶;
  * `strict` on the same 120;
  * `composite 8 241` on small8;
  * `word` on 60 random inputs plus 2 high controls;
  * `huge` and `hii` on 2521 and 2 high controls.

  All are **identical**. HJ3 N columns in `hj.csv` and `words.csv` agree on **all 3794** inputs, not just the 3426
  primes that the audit asserts. HJ5 of `hj.csv` and `high5.csv` agree at 2521.

### 4.3 Minor
* The CERTIFIED block in §6 should state its independent-check coverage in the note itself (AGENTS label rule), not
  only in REPLAY. Coverage: z52d cross-check of II and R inside the audit, HJ3 two-engine, 2521 overlap, and this review.
  * **Gap:** HJ5 at the 12 high controls has one engine plus the 2521 overlap. "Exact" is fine; "independently
    checked" would not be.
* §6.1's "every listed … count takes value zero mod … somewhere" includes columns identically 0 by construction. For
  example, the ordered sign weight is set to 0 in `z80_parity_weights.h`. Say so, or exclude them.
* §6.4 should say what the "285 small composite zeros" are zeros *of*, and mention the gstar zeros.
* REPLAY: the prime/composite split of `inputs.txt` and the source of the 12 "old R8 controls" are described but not
  scripted. `z80_parity_audit.py` contains dead code (`or (j in (2,) and o and False)`), and it skips the j=1 and j=4
  (unordered) HJ3 cross-check without comment.
* Calibration: full rank on 3426 rows is the generic outcome. The test only kills exact linear laws in these 11
  columns, which the note concedes. It is not evidence against parity mechanisms.

## 5. §0 and master-file hygiene
* The §0 **Review** line still cites only the A–C and D reviews. Until this file is cited, §§6–9 are formally
  "cross-review owed". Replace it with: "…; `REVIEW_ES_JUGULAR_R2_OPUS.md`, E–G and §6 (accepted mathematically; E
  significance and §0 wording fixes owed)."
* The §0 **Label** list for F should name BT and T10, and for G the internal dependency (§3.2).
* No master files were touched on the branch (STATUS/WAVES/FRONTIER unchanged). ✔ STATUS delta "none" is right. At
  export, a FRONTIER §6 one-liner could record the E domination ("square-block cap-0 packets need ⌈log₃Q⌉ blocks;
  irrelevant, since one nonsquare block g≡−1 (q) covers whole windows").

## 6. Required fixes (before this round counts as cross-reviewed)
1. E: qualify "optimal" as "among square-block packets". Add the one-block identity (g,1,(g+1)/q,L,q) explicitly, and
   drop or replace the exp(c√log p) shift claim.
2. §0 Result: do not lead with E. Separate D/F (q-scale thresholds) from G (p-scale, Lane 7's exponent). Replace
   "rough".
3. G: change the label to rel. internal EXTREME §1 with branch and commit, and state the consistency dependency.
   Attribute "supremal exponent 1" to Lane 7.
4. §0 Review line: cite this file.
5. F: "every Type I solution", and fix the "keep coprimality … extending to all" wording.

Optional: F sharpness control; §6 coverage sentence; E-F2 rewording; BEYOND_34 branch pointer; REPLAY split script.

## Appendix — replay of the independent checks (scripts kept outside the repo, by request)
```
# Type II independent count (sympy), ~20 s for the three inputs:
#   for e<=isqrt(p)+1: K=(p+e)/4; a|K, b|K/a, b>=a, gcd=1, e|a+b -> (abd, pacd, pbcd)
#   for a*c*d<=p//(isqrt(p)+1)+1: b=(pc+a)/(4acd-1), b>=a, gcd=1, c|a+b, e=(a+b)/c, 4abd==p+e
# one-block identity: q=1019, M=840, g≡-1 (q), g≡1 (M), g>2q -> g=731641;
#   for L in 1..2999: n=4gL-q, (a,b,c,d)=(g,1,(g+1)/q,L): 4xyz==n(xy+xz+yz)
# brute ES: for x in (n/4,3n/4], g=4x-n, s=nx, δ|s², δ<=s, g|s+δ and g|s+s²/δ
```
