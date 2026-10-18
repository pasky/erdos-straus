# SYNTHESIS_SPARKS9 — the lower tail at a single prime (task O271, synthesis IX over waves AA–AB, (J)84–(J)99 + O268/O269/O270)

Status: O271 working draft. **ES is not solved here or anywhere; no infinite case of ES for primes is claimed.** Labels as in
DISCOVERIES.md. Memos `BRAINSTORM/s9_*.md`; scripts `scripts/s9_*`; tiny logs `logs/s9_*`. Branches O268
(bm-corrected-count), O269 (metaplectic-es), O270 (exp-fifteen) were read only (`git show`), not merged; their statements are
cited as "under review".

Notation. Words: W(n) = {(t, u, v) ∈ ℤ³_{≥1} : tuv − u − v = n} (equivalently (tu − 1)(tv − 1) = tn + 1). (★) = c = 1 line =
words with 4 | t; R(p) = #(★)-words. b = 1 line (López Type A). M_BM = O268's BM-corrected singular series.

## 0. Iteration log
(to be filled step by step)
(I1) Mandatory (iv), union over ET sub-lines. Put both lines on ONE numerator-free set W(p) (Lemma 1.1 below; the word
coordinates and the five-slice sign are DEDEKIND_ES Thm 4.5's, the line dictionary is SPARKS8 Prop 1.3 in word form). Tested the
brief's "negative correlation" hope: it is false (corr +0.37–0.39), and the whole correlation is the shared size |W(p)|
(partial corr 0.35 → 0.01 after controlling log |W|). Barrier hypothesis met: "the two lines are draws from one finite set"
— the union's robustness is additive main terms on a common size variable, nothing forced.

## 1. Deep item 1: the union is a 2-adic thinning of one numerator-free set (mandatory (iv))

**Lemma 1.1 (level-c bijection; PROVED, elementary).** For n, c ≥ 1 the map (c, g, s) ↦ (cs, cg − 1, 1) is a bijection
from {words of n with first coordinate c, cs > 1} onto {words (T, U, 1) of cn with c | T, T > 1}.
*Proof.* (T, U, 1) ∈ W(cn) ⟺ U(T − 1) = cn + 1. For T = cs: c(n + s) = (cn + 1) + (cs − 1), and gcd(c, cs − 1) = 1, so
cs − 1 | n + s; g := (n + s)/(cs − 1) satisfies cgs − g − s = n. Conversely g(cs − 1) = n + s gives
cn + 1 = c(n + s) − (cs − 1) = (cs − 1)(cg − 1); cg − 1 ≥ 1 unless c = g = 1, which would give n = −1. ∎

**Corollary 1.2 (all lines on one set; PROVED; SPARKS8 Prop 1.3 in word coordinates, now for every odd n).** For odd n and
k ≥ 1, the c = 1 line of k/n (n + a + b = kabd) holds ⟺ some word of n has k | t; the b = 1 line of k/n (cn + a + 1 = kacd)
holds ⟺ some word of n has k | v (equivalently k | u). Hence **the two-line union for k/n ⟺ some word of n has a coordinate
≡ 0 (mod k).** *Proof.* c = 1: (t, u, v) = (kd, a, b). b = 1: (kcd, a, 1) ∈ W(cn) with c | kcd; Lemma 1.1 maps it to
(c, g, kd) ∈ W(n), and back. ∎
Checks (`scripts/s9_words.py 801 61`, brute force against the original definitions): all odd n ≤ 801, 0 failures; the k = 8
union fails at exactly 34 primes < 8000 incl. 131, 241, reproducing SPARKS8 (I2)'s count (`scripts/s9_words.c`, K = 8).

**Sign (DEDEKIND_ES Thm 4.5, cited).** For w ∈ W(n), X = tu − 1, Y = tv − 1, XY = tn + 1 ≡ 1 (mod n) and gcd(X, n) = 1, so
σ(w) := (X/n) = (Y/n) is well defined; σ ≡ +1 at odd squares. For n ≡ 1 (4), σ(w) = −1 ⟺ one of the five 2-adic conditions
4 | tu − 1, 4 | tv − 1, 4 | t, 4 | u, 4 | v (ES-five). The union is the last three. (A direct three-line proof of
"4 | t or 4 | v ⇒ σ = −1": with X ≡ 3 (4), (X/n) = (n/X) = (−1/X)(t/X) = −(t/X), and (t/X) = 1 because t = 4C,
X ≡ −1 (mod C′) for the odd part C′ of C and X ≡ −1 (mod 8) when C is even; same for 4 | v with Y.) Checked:
`scripts/s9_sign.py 6000` — 9 752 union words at primes ≡ 1 (4), all σ = −1; 0 words with σ = −1 at odd squares.

**Proposition 1.3 (EVIDENCE; `scripts/s9_words.c`, `s9_union_stats.py`, `s9_thinning.py`; logs `logs/s9_union_1e6.txt`,
`logs/s9_union_1e7.txt`).** Over primes p ≡ 1 (4), A = #{words with 4 | t} (= R(p)), B = #{words with 4 | u or 4 | v},
U = #{some coordinate ≡ 0 (4)}, W = |W(p)|:
* (★) failures: 17 primes ≤ 10⁶ (all residues; as O268), of which 9 are ≡ 1 (4), plus 5 in (10⁶, 10⁷] (1134241, 1724209,
  1726201, 5212561, 8813281) — 14 primes ≡ 1 (4) ≤ 10⁷, exactly (J)90's 14 ≤ 10¹⁰;
  b = 1 failures 193, 2521, 66529; union failures: none ≤ 10⁷ (all reproduce (J)89/(J)90).
* corr(A, B) after standardising within (2000-prime window) × (p mod 24): **+0.367 (≤ 10⁶), +0.387 ((10⁶, 10⁷])**. Primes with
  A = 0 have B at **0.59×** its cell mean; the bottom 1 % of A/E[A] have B at 0.71–0.75×. **No negative correlation: if (★)
  fails, b = 1 is pushed down, not up.**
* Partial correlation of A/L², B/L² (L = log p) given one-hot(p mod 840), log p, log of the 47-smooth parts of p ± 1:
  0.352 / 0.393; **adding log W: 0.031 (≤ 10⁶) / 0.011 ((10⁶, 10⁷])**. The shared factor is the size of the common set.
* W/L² ≈ 0.95 → 0.91 (mean), 1 %-quantile ≈ 0.52–0.53, min W = 43 (p > 10⁵). U/W ≈ 0.42–0.44 (mild dependence on p mod 3, 5, 8).
  Given W, U behaves like a thinning of the W/2 mirror pairs (t, u, v) ~ (t, v, u): Var(U − πW)/E[πW(1 − π)] = 2.4–2.7
  (≤ 10⁶), 2.8–3.8 ((10⁶, 10⁷], growing with W) against 2 for exact mirror-binomial — modest, growing overdispersion.
* T1 control: 1 081 odd squares in [10⁶, 10⁷]: U = 0 and σ ≡ +1 for all; W/L² = 0.45 (all σ = +1), against W₊/L² = 0.31,
  W₋/L² = 0.61 at primes.
**Assessment.** The union's lower tail factors as (size of the numerator-free set W(p)) × (2-adic thinning). No identity
couples the two lines beyond sharing W; given W they are near-independent. The deterministic part is only the sign
σ (T1); the size W is itself a B2 lottery (each word is a divisor of a shifted integer p + u in the class −1 mod u). The
numerator k enters only through "coordinate ≡ 0 (mod k)", which makes the k = 8 failures (131, 241) the same mechanism
with a thinner sieve (π₈ < π₄): no 4-specific forcing is visible here. No route; closes (iv) negatively.

(I2) Mandatory (ii), Thm K × BM class. Asked which piece of O269's E_t ± O_t is BL's class. Answer (§2): one odd quadratic
character χ_{−t} ∈ O_t together with the principal character ∈ E_t — the level-coordinate twin of O268 Thm 1.1 (χ_{−4uB} at p).
Construction attempt: use the BM layer as a positivity statement for an explicit coefficient (τ(N) − σ_{χ_{−t}}(N)) and try to
prove it positive at every non-square. It IS positive at every non-square, trivially (least non-residue; Prop 2.2) — so the
BM layer is pointwise free, and the whole difficulty is the class lottery inside the coset {χ_{−t} = −1} (index φ(t)/2).
Barrier hypothesis met: "genus/sign data only" (Prop 10.3 / (J) theme "sign layer easy, size layer hard"), now proved in
Thm-K coordinates. Hecke/Eisenstein positivity bounds σ_{χ_{−t}} = r_{−t}/w from BELOW, i.e. pushes against ES (O269 C6).

## 2. Deep item 2: the BM layer of Theorem K is χ_{−t}, and it is pointwise free (mandatory (ii))

Setting: 4 | t, N = tn + 1 (n odd), χ_{−t} = (−t/·) the Kronecker character, real and odd (χ_{−t}(−1) = −1), a character
mod t. O269 Thm K (under review on side-agent/metaplectic-es): R_t(n) = D⁻_t(N) − β_t(n), D⁻_t(N) = #{d | N : d ≡ −1 (t)}.

**Proposition 2.1 (PROVED, elementary).** (a) D⁻_t(N) ≤ #{d | N : χ_{−t}(d) = −1} = (τ(N) − σ_{χ_{−t}}(N))/2, where
σ_χ(N) = Σ_{d|N} χ(d); the right side is > 0 iff N has a prime factor ℓ with (−t/ℓ) = −1 (ℓ inert in ℚ(√−t)).
(b) Restricting the orthogonality expansion 1[d ≡ −1 (t)] = φ(t)⁻¹Σ_χ χ(−1)χ(d) to {1, χ_{−t}} gives the level-BM main term
M^{lev}_t(n) := (τ(N) − σ_{χ_{−t}}(N))/φ(t) ≥ 0 (principal: in E_t; χ_{−t}: in O_t).
(c) (T1 in level coordinates) For n = m² odd and every 4 | t: every prime ℓ | N = 1 + tm² has (−t/ℓ) = +1, so
σ_{χ_{−t}}(N) = τ(N) and M^{lev}_t(m²) = 0 = D⁻_t(N).
(d) σ_{χ_{−t}}(N) = R_{−t}(N)/w_{−t} for gcd(N, t) = 1 (Dirichlet: total number of representations of N by a system of
binary forms of discriminant −t; here gcd(tn + 1, t) = 1 automatically).
*Proof.* (a) χ_{−t}(d) = χ_{−t}(−1) = −1 for d ≡ −1 (t); the count of divisors with χ = −1 is (τ − σ)/2 since χ(d) = ±1 for
d | N (gcd(N, t) = 1); if some prime ℓ | N has χ(ℓ) = −1 then d = ℓ counts, and conversely a divisor with χ = −1 has such a
prime factor. (b) Orthogonality. (c) ℓ | 1 + tm² ⇒ −t ≡ (m⁻¹)² (mod ℓ). (d) Classical. ∎

**Proposition 2.2 (the BM layer holds at every non-square; PROVED).** For odd n: ∃ t ≡ 0 (4) with M^{lev}_t(n) > 0 ⟺ n is
not a perfect square. A witness: ℓ := the least prime with (n/ℓ) = −1, t := the least multiple of 4 with t ≡ −n⁻¹ (mod ℓ);
then t ≤ 4ℓ, ℓ | tn + 1 and (−t/ℓ) = −1.
*Proof.* ⇐: if n is not a square, the Jacobi-type symbol ℓ ↦ (n/ℓ) is a non-principal real character on primes (via
reciprocity, a character mod 4n), so ℓ exists. t exists by CRT (ℓ odd, ℓ ∤ n), t ≤ 4ℓ. Then ℓ | tn + 1, and −t ≡ n⁻¹ (mod ℓ),
so (−t/ℓ) = (n⁻¹/ℓ) = (n/ℓ) = −1. ⇒: Prop 2.1(c). ∎
So the witness level is ≤ 4ℓ(n) ≪_ε n^{1/(4√e)+ε} (Burgess), ≪ (log n)² under GRH (Ankeny/Bach).
Check (`scripts/s9_level_bm.py 200000 200`, `logs/s9_level_bm.txt`): all 99 776 odd non-squares ≤ 2·10⁵ — 0 witness failures
(max ℓ = 71); 223 odd squares — no 4 | t ≤ 200 with an inert prime factor of tm² + 1. At the witness level an actual (★) word
exists for 72.1 % of n (the class lottery, see below).

**Reading (Assessment).** The two dual slicings of the one triple sum Σ 1[4uBC − u − B = n] put BL's class in two places:
pair slicing (fix (u, B), sum over C): χ_{−4uB}(n) (O268 Thm 1.1); level slicing (fix t = 4C, sum over divisors): χ_{−t}(d)
(Prop 2.1). In both, the BM layer alone is pointwise trivial at non-squares (here Prop 2.2; there "∃ uB with (−uB/p) = −1",
quantified by O268 Thm 2.2). What remains is the position of a divisor d of N inside the coset {χ_{−t} = −1}, which consists of
φ(t)/2 classes of which exactly one (−1) is good — the X part, i.e. all characters mod t other than 1, χ_{−t}. Hence:
* an "explicit Dirichlet-coefficient positivity" route (σ_{χ_{−t}} = R_{−t}/w; Hecke/Eisenstein lower bounds for representation
  numbers) controls only the BM layer, and in the wrong direction (it bounds M^{lev}_t from above);
* the lower-tail question H⁻_BM is the class lottery inside a coset of size φ(t)/2, with no fixed-integer packaging: the
  integers tn + 1 are pairwise almost coprime (gcd | t − t′; (J)89 Lemma 2.3), so any divisor-sum of one integer F(n) that
  reproduces R(n) needs F divisible by essentially all tn + 1 (Assessment; B2 restated).
Numerator check: for 8/n the same computation uses χ_{−t} with 8 | t and gives the same witness (any non-square), while 8/131,
8/241 fail — the BM layer is numerator-blind, as it must be ((J)41).
