# HARD_PAIR — why 193 and 2521 are hardest in both worlds (task O264, cheap check)

Status: in progress (unreviewed). **ES is not solved here; nothing below proves any case of ES.** Labels as in
DISCOVERIES.md. Memos `BRAINSTORM/z34_*.md`; scripts `scripts/z34_*`; logs `logs/z34_*` (tiny).
Throughout p ≡ 1 (mod 4) is prime. Type A = López's b = 1 line (B1_LINE): cp + a + 1 = 4acd, the solution
4/p = 1/(ad) + 1/(acdp) + 1/(cdp). Astra source (q, m, s): q ≡ 3 (4), qs = pm² + 1, h = (q+1)/4, rational point
4/p = m²/(sh) + 1/(psh) + 1/(ph) (ASTRA_BRIDGE Lemma 1.3); genuine ⟺ gcd(m, h) = 1.

## 0. Iteration log
(I1) Read B1_LINE, ASTRA_BRIDGE §1–4, LATTICE_MEETING §1. Observation: Astra's source equation pm² + 1 = qs is
López's dual-coordinate Type A equation cp + 1 = Qa (B1_LINE §5(c)) with c = m², minus the congruence Q ≡ −1 (mod 4c).

## 1. Goal 1: Type A in Astra's coordinates (PROVED, elementary)

**Definition 1.1.** A *generalized source* of p is a triple (q, c, s) of positive integers with q ≡ 3 (mod 4) and
qs = pc + 1. Put h := (q + 1)/4 and P(q, c, s) := (sh/c, psh, ph). For a slice q with gcd(q, p) = 1 let
c_q ∈ [1, q − 1] be the least positive residue of −p⁻¹ (mod q).

**Theorem 1.2 (one equation, three side conditions; PROVED).** Let p ≡ 1 (4) be prime.
(a) For every generalized source, 4/p = c/(sh) + 1/(psh) + 1/(ph), and gcd(c, s) = 1.
(b) Astra's sources are exactly the generalized sources with c = m² a perfect square (Astra's twist m).
(c) P(q, c, s) is integral ⟺ c | h. The generalized sources with c | h are in bijection with the Type A solutions
    (a, c, d) via (q, c, s) = (4cd − 1, c, a), d = h/c, and then P(q, c, s) = (ad, acdp, cdp).
(d) At a fixed slice q, c runs through the class −p⁻¹ (mod q). Hence Type A has a solution with López divisor
    w = q ⟺ c_q | h, and N₁(p) = #{q ≡ 3 (4) : gcd(q, p) = 1, c_q | (q + 1)/4} (each such q gives one solution).
(e) Slice q carries an Astra source ⟺ c_q is a square unit mod q; it then carries genuine sources (gcd(m, h) = 1).
    An Astra source is integral on arrival (Astra's x = sh/m² ∈ ℤ, i.e. "scalar removal") ⟺ m² | h ⟺ c_q = m².
*Proof.* (a) c/(sh) + 1/(psh) + 1/(ph) = (pc + 1 + s)/(psh) = s(q + 1)/(psh) = 4/p; qs − pc = 1 gives the gcd.
(b) Definition (ASTRA_BRIDGE Lemma 1.3). (c) gcd(c, s) = 1, so c | sh ⟺ c | h. If c | h put a = s, d = h/c: then
q = 4cd − 1 and qa = cp + 1 is cp + a + 1 = 4acd, and sh/c = ad, psh = acdp, ph = cdp. Conversely a Type A solution
has (4cd − 1)a = cp + 1, a generalized source with c | cd = h. (d) qs = pc + 1 ⟺ c ≡ −p⁻¹ (mod q) (then s ∈ ℤ_{>0});
c | h and h < q force c = c_q. Two Type A solutions with the same q have the same c = c_q, d = h/c_q, a = (c_q p + 1)/q.
(e) The source condition q | pm² + 1 is m² ≡ c_q (mod q). Genuine lifts: gcd(q, h) = 1 (4h ≡ 1 mod q), so CRT picks
m in the root class with m ≡ 1 mod every prime of h. Integrality: by (c) with c = m², m² | h; then m² ≡ c_q and
m² ≤ h < q give m² = c_q. ∎

**Corollary 1.3 (what Type A failure means for Astra; PROVED).** If Type A fails at p then
(i) no Astra source, genuine or not, on any slice is integral on arrival (m² ∤ h always);
(ii) in particular (m = 1, c_q = 1 ⟺ q | p + 1) every odd prime factor of p + 1 is ≡ 1 (mod 4):
    194 = 2·97, 2522 = 2·13·97, 66530 = 2·5·6653;
(iii) at every split slice q, reducing Astra's twist square modulo the slice, m² ↦ c_q (a move that leaves the
    slice and y = ph fixed but in general leaves the square class of integers), never lands on a divisor of h;
(iv) every ES solution of p (in particular every exit of an Astra route) is Type I, or Type II with both ET
    parameters a, b ≥ 2 (ET form (abd, acdp, bcdp)); none has López's shape (du, dv, duv).
The converse of (i) is false, and so is "Type A fails ⟺ no genuine source on any slice" (genuine sources exist on
every split slice, and every p has split slices: any prime q ≡ 3 (4) with (q/p) = −1).
*Proof.* (i)–(iii) are Thm 1.2(c)–(e). (iv): Type A is ET Type II with b = 1 (or a = 1 by symmetry). ∎

**Reading.** In the slice residue c_q all four notions are one-residue conditions:
| condition on c_q = −p⁻¹ mod q | object | barrier |
|---|---|---|
| c_q ∈ (ℤ/q)^{×2} | Astra source on slice q | B1 (local) |
| c_q ≡ (2k)² (mod q) for some k ∣ h | Claude ES shot (2k, 1) ∈ L_ρ(q) (d = 1 locus) | B2 |
| c_q ∣ h (as an integer) | Type A (b = 1) with López divisor q | B2 |
| c_q = m², m² ∣ h | Astra source integral on arrival | B2 ∩ square |
So Type A is Astra's source equation with the square condition on the twist dropped and an integrality condition
imposed. Astra needs the class of c_q to be a square; Type A needs its least representative to divide h. These are
different (one local, one archimedean/divisor) conditions on the same residue, and neither implies the other.
*Check* (`scripts/z34_dict.py 100000 100000`, 64 s, `logs/z34_dict_full_1e5.txt`): all 4 783 primes p ≡ 1 (4) ≤ 10⁵.
Type A by the pair form (B1_LINE Lemma 1.1): 75 658 solutions, each checked as an exact identity with c = c_q and c | h.
Independently, the slice scan of all q ≡ 3 (4), q ≤ 2p (≥ the bound 4cd − 1 ≤ p + 4d ≤ (3p + 3)/2) gives exactly the same
slice set for every p (Thm 1.2(d)). An independent scan of Astra sources (m ≤ √((p+7)/12), all q | pm² + 1,
q ≡ −1 (mod 4m²)) gives exactly the c-square subset (Thm 1.2(e)). Failures: 193, 2521, 66529 only. 53 716 Type A
solutions sit on split slices (inside some L_ρ(q)) and 21 942 (29 %) on non-split slices (no Astra source there).
22 627 are integral Astra sources (c square). **314 primes ≤ 10⁵ have Type A but no integral Astra source** (73, 313,
337, 409, 577, …, 3361, …): the one-way implication of Cor 1.3(i) is strict.

## 2. Goal 2: hardness scores, rank correlations, and the local profile (EVIDENCE + Assessment)

**2.1 Scores** (`scripts/z34_scores.c`, all 39 175 primes p ≡ 1 (4) ≤ 10⁶, 2.4 s; cross-checked against brute force for
every p ≤ 1500 by `scripts/z34_check_scores.py`, 0 mismatches; output regenerable, not stored). Hardness orientation in brackets.
* N₁(p): Type A solutions (B1_LINE Lemma 3.1) [small = hard];
* f_II(p): Type II solutions, ordered, ET form 4abcd = a + b + pc (logic of `bs_prob_fII.c`) [small];
* m₀(p): least Type II window 4x − p (s7_window_lottery) [large];
* S(p): distinct slices g carrying a lattice ES point (2k, 1), k | h (LATTICE_MEETING Prop 1.1; S = 0 ⟺ 𝓜(p) = ∅,
  reproducing its 25 empty primes ≤ 2·10⁴) [small];
* e₀(p): least Type I level e (an ES solution containing p(pe + 1)/4; ASTRA_BRIDGE Thm 2.1, n = 1) [large];
* L_I(p): Type I levels e ≤ 199 carrying ES [small].
The first four are Claude-side (Type II) quantities; S, e₀, L_I are the quantities Astra's exits are read in
(ASTRA_BRIDGE §4: Astra exits are Type I levels e ≤ 143 or lattice/Type II windows). Each score becomes a size-normalised
hardness percentile u (mid-rank among the 1001 nearest primes; for fixtures, among primes in [p/2, 2p]).

**2.2 Rank correlations** (Spearman of u over the 36 626 primes in [5·10⁴, 10⁶]; `logs/z34_ranks_1e6.txt`).
| | N₁ | f_II | m₀ | S | e₀ | L_I | smooth part of p−1 |
|---|---|---|---|---|---|---|---|
| N₁ | 1 | 0.80 | 0.20 | 0.49 | 0.13 | 0.43 | 0.35 |
| f_II | | 1 | 0.21 | 0.54 | 0.16 | 0.52 | 0.39 |
| m₀ | | | 1 | 0.15 | 0.19 | 0.21 | 0.10 |
| S | | | | 1 | 0.02 | 0.23 | 0.34 |
| e₀ | | | | | 1 | 0.29 | 0.13 |
The profile cell (χ_p(ℓ), ℓ = 3, 5, 7, 11, 13, and p mod 8) within size blocks of 5000 primes explains this share of
var(u): N₁ 27 %, f_II 30 %, m₀ 47 %, S 79 %, e₀ 38 %, L_I 36 %. Residual correlations after removing the cell means:
N₁–f_II 0.72, f_II–S 0.49, N₁–S 0.35, f_II–L_I 0.38, but m₀ and e₀ residuals are ≈ 0 against everything
(m₀–e₀ −0.09; −0.20 inside p ≡ 1 (24)). Reading (Assessment):
* the *count* scores (N₁, f_II, S, L_I) share a large non-local component beyond the profile. All of them count
  divisor events in overlapping families of shifted integers (p + 4d for N₁, p + 4a² for S; d = a² is common). This is the B2
  lottery seen through several windows, not a new invariant;
* the *least* scores m₀, e₀ are first-success times of short lotteries; given the profile they are close to independent;
* S (the d = 1 locus) is the most profile-driven score: 79 % of its variance is congruence data.

**2.3 The fixtures** (band percentile u in [p/2, 2p]; band sizes 25, 230, 301, 4408; raw (N₁, f_II, m₀, S, e₀, L_I)).
| p | p − 1 | raw | u: N₁ f_II m₀ S e₀ L_I |
|---|---|---|---|
| 193 | 2⁶·3 | 0, 4, 7, 0, 3, 3 | 1.00 1.00 0.96 0.96 0.40 0.92 |
| 2521 | 2³·3²·5·7 | 0, 6, 23, 2, 15, 4 | 1.00 1.00 1.00 0.94 0.98 0.98 |
| 3361 | 2⁵·3·5·7 | 1, 4, 3, 0, 7, 5 | 0.99 1.00 0.43 0.99 0.85 0.95 |
| 66529 | 2⁵·3³·7·11 | 0, 20, 31, 12, 3, 7 | 1.00 1.00 1.00 0.81 0.38 0.95 |
| 5209 | 2³·3·7·31 | 7, 28, 11, 10, 19, 5 | 0.86 0.88 0.98 0.69 0.99 0.96 |
| 233689 | 2³·3·7·13·107 | 5, 50, 11, 8, 7, 8 | 1.00 0.99 0.98 0.95 0.87 0.94 |
193 is *not* Type-I-hard (e₀ = 3: Astra's own e = 3 exit, H = 145). 2521 is hard everywhere.

**2.4 Astra's fixture tests are Claude's scores.** Checked against the Astra text (d7300f8, read-only):
* POSITIVE_ES_RESEARCH_RESET §3.2 "Exact test 4: at p = 193 … there is no primitive Type-II target with a = 1, even with
  c and d unrestricted". ET a = 1 is Type A (by the a ↔ b symmetry). So Astra's 193 Type-II-descent obstruction is
  literally N₁(193) = 0 (Cor 1.3(iv)); its "complete tuples (2,5,1,5), (2,13,1,2)" are our f_II(193) = 4 (ordered).
* TWIST_HEIGHT_COMPRESSION §3.2 "five permanently blocked anchors" at 2521: A = 631, …, 635 with k = 3, 7, 11, 15, 19
  are the Type II windows m = 3, …, 19 with K = (p + m)/4, i.e. m₀(2521) = 23. TWIST_FLOOR_CERTIFICATE_GATEWAY §6.2 "the initial
  level [e = 3] is fully sterile, … the fivefold move exits" at H_S = (15p + 1)/4: Type I levels 3, 7, 11 fail and
  e₀(2521) = 15, exactly our e₀.
* POSITIVE_ES_RESEARCH_RESET: "Only p = 97, 193, 3361 are exhausted". All three have S = 0 (𝓜 = ∅), and they are the only
  ones with S = 0 among Astra's fixtures 97, 193, 313, 1129, 2521, 3361, 5209, 15241, 233689 (S = 0, 0, 6, 4, 2, 0, 10, 4, 8).
So the overlap is partly *definitional*: when Astra certifies that a fixture is hard, its certificate is a failure of
a Type II sub-line (a = 1, small windows, d = 1) or of small Type I levels. Those are the same events that Claude's
scores count.

**2.5 The shared local profile** (`scripts/z34_smooth_cell.py`, `logs/z34_smooth_cell_1e6.txt`). Every fixture except
5209 and 233689 has 13-smooth p − 1, and all three Type A failures have 11-smooth p − 1. For p ≡ 1 (4) prime,
ℓ | p − 1 ⟹ (ℓ/p) = (p/ℓ) = 1, so smooth p − 1 means maximal small-prime QR-richness, and in addition the T1 point-1
freezing of B1_LINE Prop 4.1 (exact divisibility, finer than the QR pattern). Among the 676 primes 50 < p ≤ 10⁶ with 13-smooth
p − 1: mean u = 0.73 (N₁), 0.77 (f_II), 0.62 (m₀), 0.68 (S) against 0.5 for all primes; 23 % are top-5 % in N₁. Joint
top-5 % in N₁ and S: 4.9 % of the smooth cell against 0.63 % of a size-matched random sample (×8). Inside the cell this is
still 1.7× the product of the cell marginals (2.9 %), and N₁–m₀ is 2.5× (8.3 % vs 3.3 %).
**Verdict on goal 2 (Assessment).** The overlap at 193/2521 needs no extra structural coincidence. It decomposes into
(i) the shared local profile: small p with 11-smooth p − 1, i.e. the T1 point 1 in Ẑ on the small primes. This multiplies the
chance of joint extremeness by about 8;
(ii) the shared B2 input: the count scores read divisor events of the same shifted integers, which leaves residual
rank correlations of 0.35–0.7 after the profile is removed;
(iii) definitional overlap: Astra's fixture certificates are failures of exactly these Type II/Type I sub-lines.
193 and 2521 are then the most extreme draws of this correlated lottery at small p. Two of the three Type A failures
also sit in the hard tail of every other Claude score. That is what (i)+(ii) predict, not a further coincidence.
The one non-mundane residue: 193 is easy at Type I (e₀ = 3), so Astra's 193 hardness lives at a fixed retained level
(e = 31), not at the least level.

## 3. Goal 3: does this suggest a new mechanism? (Assessment)
No. Mundane outcome. Thm 1.2 puts Astra's sources, Claude's ES shots and López's Type A on one residue,
c_q = −p⁻¹ mod q per slice. Astra's condition on it is local: c_q is a square class. The other two are divisor
conditions on representatives: c_q ≡ (2k)², k | h, or c_q | h. The local condition is satisfiable on half of all
prime slices for every p. The divisor conditions are B2 events whose supply is the factorisation of h = (q + 1)/4,
equivalently of the shifted integers p + 4d. The hardest primes of both campaigns are where the local profile is most
T1-like (p − 1 smooth: all small primes are QR and the small shifts are frozen, B1_LINE Prop 4.1) and the B2 draws
at the few remaining small shifts all fail. Both campaigns see the same draws because their hardness certificates
(a = 1, short windows, d = 1, small Type I levels) are the same sub-lines. The one possible lead is the Type-I/Type-II
split: 193 and 66529 are Type-I-easy (e₀ = 3) while Type-II-extreme, and the least-score residuals m₀–e₀ are slightly
*negative* inside p ≡ 1 (24) (−0.20). So a fixture that is hard on both sides (2521, 5209) is a genuinely double draw,
not a single cause. That is EVIDENCE of near-independence of the two ET types given the profile, and it suggests no
mechanism. The unified table of §1 is a dictionary, not an existence tool. Nothing here advances ES.

## 4. Verdict (O264)
* PROVED (elementary): Astra's source equation and López's Type A are one equation, qs = pc + 1. Astra requires c = m², Type A requires
  c | (q + 1)/4, and an Astra source is integral on arrival iff both hold (Thm 1.2). Type A failure ⟹ no Astra source
  on any slice is integral on arrival, and the odd part of p + 1 has only primes ≡ 1 (4) (Cor 1.3). The converse fails (314
  primes ≤ 10⁵). "Type A fails ⟺ no genuine source" is false (genuine sources always exist).
* EVIDENCE (≤ 10⁶): hardness scores correlate (Spearman 0.2–0.8). The local profile explains 27–79 % of the variance;
  the count scores keep 0.35–0.7 residual correlation (shared shifted-integer factorisations, B2), and the least
  scores are nearly independent given the profile.
* Assessment: 193/2521 are hard in both worlds because of (i) 11-smooth p − 1 at small p (the T1 point 1), (ii) the shared
  B2 lottery, and (iii) Astra's fixture certificates being Claude's sub-line failures (a = 1 at 193; windows 3–19 and Type I
  levels 3–11 at 2521). There is no extra structural coincidence and no new mechanism. ES is not solved.
