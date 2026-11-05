# Z59_CONV2 — what the extra Type II variables buy at one p: the screen profile is already carried by the one-line union c = 1 ∪ a = 1; no pointwise mechanism found (verdict: narrowed + sharper target)

**ES is OPEN; nothing here proves or disproves it, and nothing here is pointwise progress on (MS) or (MS-II).** Lane
CONV2 of wave z59 (`z52bbriefs/z59_lanes.md` §CONV2; rules `z58_lanes.md` "Common rules" + falsifier table;
`z53_depth.md` with z53 → z59). Scripts `scripts/z59_conv2_*`, data `data/z59/conv2/` (≈ 3.4 MB). Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Status: final; internal hostile review applied (§8).

Notation. n is a positive odd integer, K ≡ 0 (mod 4), N^{(K)}(n) = #{(a,b,c,d) ∈ ℕ⁴ : K·abcd = a + b + nc}, N_II = N^{(4)}.
Coordinate lines: **c = 1** (= (★), count R(n)); **a = 1** (∪ b = 1 by the a ↔ b symmetry; López's "Type A", B1_LINE's
"b = 1 line"); **d = 1**. U := (c = 1) ∪ (a = 1). For a witness f ≡ −1 (mod K): m_f = (f+1)/K, D_f = {a mod f : a | m_f}.
r(m) := the largest r with r² | m. 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^×.

**Verdict in one paragraph.** No pointwise mechanism was found, and B2 did not move. What was found:
1. The c = 1 and a = 1 lines combine into a single one-parameter family of tied divisor events (Lemma 1(iii), PROVED):
   some Tn + 1 has a divisor ≡ −1 (mod L_T), with L_T = T if 4 | T and L_T = 4T otherwise.
   * Each half was known in one-line form: (★) as "4Cn + 1 has a divisor ≡ −1 (mod 4C)"; a = 1 as "cn + 1 has a divisor
     ≡ −1 (mod 4c)" (CLASS_FORCING, Z58_CONVF §2).
   * New here: the combined piecewise profile L_T. On the integers the two lines share, one line's events imply the
     other's, in both natural coordinate systems (Prop 3.1).
2. **This one line matches the full family's screen profile in the certified range.** Among odd non-squares ≤ 10¹⁰ it
   vanishes only at 105 and 4545 (CERTIFIED, one engine above 10⁸). The full family vanishes there only at 4545.
   * The pair {105, 4545} was already known as the joint zero set of (★) and b = 1 to 3·10⁴ (BRAINSTORM/z52d_pass2_TO8)
     and to 4·10⁶ (Z57_COMPLEMENT). The extension to 10¹⁰ is new.
   * So, in the tested range, the full family beyond U (a, c both ≥ 2) is needed only at n = 105. The a = 1 branch of U
     itself uses c ≥ 2: every rescue of a (★)-zero has c ≥ 2.
3. What the extra variables give at one p, exactly (Prop 2.1, PROVED):
   * on the canonical integers 4mp + 1 the modulus relaxes from 4m to 4m/r(m), never below 2√(4m);
   * per modulus 4u there are τ(u) integers c²p + u, against min(2, τ(u)) for U and 1 for (★);
   * the PROVED log p gain of Z57_BFII Theorem G concerns the *genus part* only, not the actual count.

   Locally, U recovers Mordell's complete Type II moduli 3, 7, 15, while (★) has only 3 among f ≤ 15 (Prop 2.2). That
   local fact accounts for exactly the 5 (★)-zero primes outside 𝔐. The 9 in 𝔐 are rescued by other witnesses.
4. Inheritance and the numerator ladder never transport a solution to a prime from a smaller integer (Prop 4.1,
   PROVED, for the class of equation-scaling monomial transports). On each shared integer the c-line events have a
   greatest element, the c = r(m) event, so the c-lines collapse to one line (Prop 4.2).
5. Numerator 8 is not clean for the union. U⁽⁸⁾ has 819 odd non-square zeros ≤ 10⁸: 61 primes (last 3 869 153) and 758
   composites (last 93 398 595).

**Sharper target: CONJECTURE U** (§1). It asks for more than CONV-II (a stricter witness family). At primes it is López's
Conjecture 1.

## 0. Mandatory falsifier table (committed at checkpoint 1 in `a5b7c183`; final form after review)

Objects: the U-line (the target that came out) and the structural statements of §§2–4.

| screen | behaviour | label |
|---|---|---|
| **F1 odd squares** | U ⊂ Type II, so U(m²) = 0: every witness f has (n/f) = −1 (Z57_BFII Prop 2.2). Lemma 1(iii) reads T1 per integer. On Tn + 1 the modulus L_T is the one that forces (n/f) = −1: for T odd, (T/f) = 1 needs f ≡ −1 (mod 4T); for T ≡ 2 (4), (2/f) = 1 needs f ≡ 7 (8); for 4 | T, mod T suffices. Hence at n = m² every **odd** prime factor of Tm² + 1 lies in ker χ_{−T}, a subgroup of (ℤ/L_T)^× not containing −1, and so does every odd divisor. At a prime p ≡ 1 (4), a witness needs an odd prime ℓ | Tp + 1 with (ℓ/p) = −1 (reciprocity, as in Z57_BFII Cor 2.4), and then the class −1. Non-squareness enters at the first step. Nothing in §§2–4 supplies the second. | PROVED |
| **F2 numerator 8** | U⁽⁸⁾ = (c = 1 line of 8/n, i.e. R₈) ∪ (a = 1 line of 8/n). Odd non-square zeros ≤ 10⁸: **n ≡ 1 (4): 547** (45 primes, last 3 869 153; 502 composites, last 89 530 945). **n ≡ 3 (4): 272** (16 primes, last 1 226 891; 256 composites, last 93 398 595). Total **819**. An argument that applies verbatim to numerator 8 proves a false statement unless its threshold is ≥ 3 869 153 for primes, ≥ 93 398 595 for all odd non-squares. Among the small moduli K = 4 and K = 8 differ: for K = 4 the union has the complete moduli 3, 7, 15; for K = 8, f = 3 is unavailable and f = 7, 15 are incomplete (f = 7: target set {1}). No global classification of complete moduli is claimed. | CERTIFIED (≤ 10⁸) |
| **F3 composites** | **U vanishes at exactly two odd non-squares ≤ 10¹⁰: 105 = 3·5·7 and 4545 = 3²·5·101** (n ≡ 1 (4) by census; n ≡ 3 (4) by Lemma 1(vii)). Compare (★): 285 composite zeros ≤ 8·10⁶; a = 1 alone: 35 non-square zeros ≡ 1 (4) ≤ 10⁵ (32 composite). Of the 285 (★)-composite zeros, 51 are rescued by U's complete moduli 3, 7, 15. The other 234 are not (176 divisible by 3, 15 coprime to 105); of these 232 are rescued by U and 2 are U's own zeros 105 and 4545. Both U-zeros are divisible by 15: "U at every odd non-square coprime to 15" has no exception ≤ 10¹⁰. A finite census is consistency, not a mechanism. | CERTIFIED (≤ 10¹⁰) |
| **F4 known zeros** | U ≥ 1 at all 14 (★)-zero primes: least a = 1 parameter T = 2 at 11 of them, T = 5 at 83 449 and 8 813 281, T = 6 at 102 001. At the a = 1 zeros 193, 2521, 66529 U holds by (★) at T = 8, 44, 8. The 12 R₈-zeros have R ≥ 12. 24 of the 38 𝔊*-zeros have R ≥ 1 and the other 14 are the (★)-zero primes. No prime zero of U ≤ 10¹¹: a = 1 fails ≤ 10¹¹ only at those three (B1_LINE census, quoted, not recomputed). By Prop 3.1 every rescue of a (★)-zero by a = 1 uses an integer Tp + 1 with 4 ∤ T. | CERTIFIED + PROVED |

## 1. Precise statements and the one-line lemma

**Lemma 1 (one-line forms; PROVED, elementary).** Let n ≥ 1 be odd; T, y ≥ 1.
* (i) R(n) ≥ 1 ⟺ ∃ T ≡ 0 (mod 4) such that Tn + 1 has a divisor f ≡ −1 (mod T).
* (ii) The a = 1 line is non-empty ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod 4T). This is known in the form
  "cn + 1 has a divisor ≡ −1 (mod 4c)": CLASS_FORCING, Z58_CONVF §2.
* (iii) **U(n) ≥ 1 ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod L_T), L_T := T if 4 | T, 4T otherwise.**
* (iv) (shift form) R(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod 4y). The a = 1 line is non-empty ⟺ ∃ y ≡ 0 (4) such
  that n + y has a divisor ≡ −1 (mod y). So U(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod L_y), with the *same* profile.
* (v) (full family) N_II(n) ≥ 1 ⟺ ∃ m ≥ 1: 4mn + 1 has a divisor ≡ −1 (mod 4m/r(m)). Equivalently, ∃ k ≥ 1: n + 4k has a
  divisor ≡ −1 (mod 4k/r(k)).
* (vi) (target sets at a witness f) c = 1: −n ∈ D_f. a = 1: −n ∈ D_f⁻¹ = 4D_f. d = 1: −n ∈ {4a² : a | m_f}.
  Full: −n ∈ {a/c : ac | m_f} = {4a²d : ad | m_f}.
* (vii) For n ≡ 3 (mod 4), (a,b,c,d) = (1, 1, 2, (n+1)/4) lies on the a = 1 line, so U(n) ≥ 1.
* (viii) (raw form) U(n) ≥ 1 ⟺ ∃ D ≡ 0 or 3 (mod 4), 3 ≤ D ≤ (4n+4)/3, such that r := (−n mod D) ≠ 0 divides
  ⌊D/4⌋ + 1. For D ≡ 3 this is the (MS) d-form of (★); for D = 4b it is the a = 1 line.

*Proof.*
* (i) With T = 4C, (Tu − 1)(TB − 1) = T(TuB − u − B) + 1 = Tn + 1. Conversely, let f ≡ −1 (mod T) divide Tn + 1. Its
  cofactor g is ≡ −1 (mod T) (fg ≡ 1), so f, g ≥ T − 1. Then u = (f+1)/T, B = (g+1)/T ≥ 1 solve 4uBC − u − B = n.
* (ii) a = 1 reads b(4cd − 1) = cn + 1. With T = c, f = 4cd − 1 ≡ −1 (mod 4T) divides Tn + 1. Conversely, d = (f+1)/(4T)
  ≥ 1 and b = (Tn+1)/f ≥ 1, also for T ∈ {1, 2, 3}.
* (iii) If 4 | T, f ≡ −1 (mod 4T) implies f ≡ −1 (mod T); combine (i) and (ii).
* (iv) Z57_BFII Lemma 1.1(e): f | n + 4a²d with f ≡ −1 (mod 4ad).
  * For c = 1, f = 4ad − 1 and 4a²d ≡ a (mod f): the event is "n + a has a divisor ≡ −1 (mod 4a)".
  * For a = 1: "n + 4d has a divisor ≡ −1 (mod 4d)" (López).
  * For 4 | y, a divisor ≡ −1 (mod 4y) is ≡ −1 (mod y).
* (v) The (c,d)-slice is f | 4c²dn + 1, f ≡ −1 (mod 4cd). For fixed m = c²d, every c with c² | m divides r(m) (compare
  exponents), so 4m/r(m) divides every admissible 4m/c: the c = r(m) condition is the weakest. Conversely, given
  f ≡ −1 (mod 4m/r(m)), put c = r(m), d = m/r(m)², a = (f+1)/(4cd) ≥ 1. Since 4cd(cn + a) ≡ 4mn + 1 ≡ 0 (mod f) and
  gcd(4cd, f) = 1, b = (cn + a)/f is a positive integer. The (a,d) version is the same with k = a²d and a = r(k).
* (vi) Z57_BFII Lemma 1.1(d), with 1/c ≡ 4·(m_f/c) because 4m_f ≡ 1 (mod f).
* (vii) 4·1·1·2·(n+1)/4 = 2n + 2 = 1 + 1 + 2n.
* (viii) Z58_CONVF (E5): solutions ↔ (a, b, e) with e | a + b and 4ab | n + e, d = (n+e)/(4ab).
  * With a = 1: 4b | n + e and e | b + 1. Since 1 ≤ e ≤ b + 1 < 4b, e is the least positive residue of −n mod D := 4b,
    and ⌊D/4⌋ + 1 = b + 1. The range is 4b ≤ n + b + 1, so D ≤ (4n+4)/3.
  * For c = 1 use the (MS) d-form (`Z58_SUMMARY.md` preamble): D = d = 4uC − 1, r = u, (d + 1)/4 = ⌊d/4⌋ + 1, and
    D ≤ (4n+1)/3.
  * CERTIFIED cross-check: (iii), (iv), (viii) and direct enumeration agree for every odd n ≤ 1500, squares and
    n ≡ 3 (4) included (`z59_conv2_rawform.py`). ∎

**CONJECTURE U.** Every odd non-square n ∉ {105, 4545} has U(n) ≥ 1. Equivalently, some Tn + 1 has a divisor
≡ −1 (mod L_T).
* CERTIFIED for n ≤ 10¹⁰ (§5).
* At primes it is López's Conjecture 1: Type A ∪ Type B covers every prime (arXiv:2404.01508; archived source
  `sources/lit2026f/r270-lopez-2404.01508v3-html.md`; B1_LINE §0).
* New here: the composite census to 10¹⁰ (previously to 4·10⁶), the F2 profile, and the combined profile L_T.
* U ⟹ CONV-II. At n = 105, (a,b,c,d) = (3, 3, 2, 3) is a full-family solution (216 = 3 + 3 + 210).
* (MS-U), i.e. U(p) ≥ 1 for every prime p > 10¹⁷ in 𝔐, satisfies (MS) ⟹ (MS-U) ⟹ (MS-II). So (MS-U) gives ES relative
  to Mordell + Salez, like (MS).
* U requires a solution with a = 1 or c = 1, so it asks for more than CONV-II. That U is *harder to prove* than CONV-II
  is not claimed. Two open universal statements are not compared here.

## 2. What the extra variables buy at a single p

**Proposition 2.1 (exact accounting; PROVED).** Fix an odd n.
* (a) *Square-root tie.* In the (c,d)-system every Type II event lives on an integer 4mn + 1 (m = c²d) with modulus
  L = 4cd. Since L² = 16c²d² = 4d·(4m) ≥ 4·(4m), with equality iff d = 1, the extra variables relax the tie from linear
  in the coefficient 4m to at worst its square root. There is no bounded-modulus family, consistent with B-fin.
* (b) *Integers per modulus.* N_II(n) ≥ 1 ⟺ ∃ u ≥ 1, ∃ c | u: c²n + u has a divisor ≡ −1 (mod 4u).
  * The c = 1 line uses only n + u (c = 1).
  * The a = 1 line uses only u²n + u (c = u).
  * So per modulus 4u the full family has τ(u) distinct integers, U has min(2, τ(u)), and (★) has one.
* (c) *Lines collapse to profiles.* On a shared integer 4mn + 1, the c-events (c² | m) all imply the c = r(m) event,
  which is one of them. So the full family is the single line m ↦ E(4mn + 1, 4m/r(m)) (Lemma 1(v)). Likewise U is the
  single line T ↦ E(Tn + 1, L_T) (Lemma 1(iii)).

*Proof.*
* (a) Arithmetic.
* (b) By Z57_BFII Lemma 1.1(e), f | cn + a with f ≡ −1 (mod 4ac). Multiplying by c, a unit mod f, gives f | c²n + ac.
  Put u = ac. Conversely, take a = u/c and d = (f+1)/(4u). Distinct c give distinct integers.
* (c) The proof of Lemma 1(v). ∎

*What this does and does not say (Assessment).* (a) and (b) are exact structure. Z57_BFII Theorem G proves a log p
larger **genus** main term for the full family; it says nothing about the actual count N_II(p). That the τ(u) integers
behave like independent extra trials is a heuristic, supported only by the observed counts (Z57_BFII §4: mean
N_II ≈ 0.076·log³p, EVIDENCE).

**Proposition 2.2 (local content: small complete moduli; PROVED + CERTIFIED).** Call f *complete* for a family if its
target set is −{Jacobi-non-residue units mod f}.
* For U, f = 3, 7, 15 are complete: D₃ = {1}, D₇ ∪ D₇⁻¹ = {1, 2, 4} and D₁₅ ∪ D₁₅⁻¹ = {1, 2, 4, 8}, the same targets as
  full Type II (Z57_BFII Prop 3.1).
* For (★), among f ≤ 15 only f = 3 is complete. The targets are D₇ = {1, 2}, D₁₁ = {1, 3} against the five QRs mod 11,
  and D₁₅ = {1, 2, 4}.
* Hence U(n) ≥ 1 whenever, for some f ∈ {3, 7, 15}, gcd(n, f) = 1 and (n/f) = −1. That is Mordell's Type II covering,
  and U contains all of it.

CERTIFIED consequences (`z59_conv2_localsplit.py` → `localsplit.txt`; data `data/z58/screens/`):
* Exactly the 5 (★)-zero primes *outside* 𝔐 (409, 577, 23929, 329617, 1134241) are non-residues mod 7 or 15. U rescues
  them through these moduli. For example 409 ≡ 3 (mod 7), and f = 7 = 4·2·1 − 1 divides 2·409 + 1: a = 1 at T = 2.
* The 9 in 𝔐 are residues mod 3, 5 and 7, so none of 3, 7, 15 applies. U rescues them with other witnesses
  (least a = 1 T = 2, 5, 6, …). Whether some larger complete modulus exists is not addressed.
* Of the 285 (★)-composite zeros, 51 are rescued through 3, 7, 15. Of the other 234, 232 are rescued by other witnesses
  and 2 (105, 4545) are U-zeros.

*Reading (Assessment).* The gap between (★) and U on the screens has a *local* part: (★) is Mordell-incomplete at 5
and 7. The rest is consistent with a count heuristic: the a = 1 events on T ≢ 0 (mod 4) add candidate events in every
residue class. No additional mechanism inside 𝔐 was found.

## 3. Joint failure of two one-parameter lines

**Proposition 3.1 (domination on shared integers; PROVED).**
* (a) T-system: for 4 | T, every a = 1 event on Tn + 1 (divisor ≡ −1 mod 4T) is a (★) event on Tn + 1 (≡ −1 mod T).
  At solution level, (1, b, 4C, d) ↦ (4d, (n + 4d)/f, 1, C), with f = 16Cd − 1, is a bijection from {a = 1 solutions
  with 4 | c} onto {(★) solutions with 4 | u}. Both sides use the same witness f.
* (b) Shift system: for 4 | y, every (★) event on n + y (≡ −1 mod 4y) is an a = 1 event (≡ −1 mod y).
* (c) Hence U(n) = 0 ⟺ the single profile line of Lemma 1(iii) fails.
  * A (★)-zero can be rescued by the a = 1 line only through integers Tn + 1 with 4 ∤ T.
  * An a = 1 zero can be rescued by (★) only through integers n + y with 4 ∤ y.
  * On a shared integer the stronger event can fail while the weaker holds, but never the reverse.

*Proof.* (a) The first sentence is Lemma 1(iii). For the bijection: f = 4·(4C)·d − 1 divides 4Cn + 1 ⟺ f divides
n + 4d, because 4C(n + 4d) = 4Cn + 16Cd ≡ 4Cn + 1 (mod f) and gcd(4C, f) = 1. Then (u, B, C) = (4d, (n+4d)/f, C)
satisfies (4uC − 1)B = fB = n + 4d = n + u, i.e. 4uBC − u − B = n. The inverse sends (4d, B, 1, C) to
(1, (4Cn+1)/f, 4C, d). The reviewer also checked equality of the two solution sets for every odd n ≤ 301.
(b) Immediate. (c) Follows. ∎

*Data* (`z59_conv2_rescue.py`, T ≤ 60). The 14 (★)-zero primes are rescued by a = 1 events at least T = 2 (11 primes),
5 (83 449, 8 813 281) and 6 (102 001), all with 4 ∤ T as (c) requires. The a = 1 zeros 193, 2521, 66529 are rescued by
(★) events at least T = 8, 44, 8.

**What is and is not excluded (scoped).**
* PROVED: complementarity on a *shared* integer is impossible, since the stronger event implies the weaker (Prop 3.1).
  Any rescue of one line by the other uses an integer the first line does not use.
* PROVED (fixed finite menus): for a fixed finite set of events (T, f), every prime p ≡ 1 (mod 840·∏f) makes all of them
  fail. Such f | Tp + 1 forces f | T + 1, which is impossible: for 4 | T, f ≥ T − 1 and T ≥ 4; otherwise
  f ≥ 4T − 1 > T + 1. This is the Z57_BFII Prop 3.2 argument; Dirichlet gives infinitely many such p.
* PROVED (common factors): gcd(Tp + 1, T′p + 1) | T − T′ (privacy lemma, FRONTIER §3). This bounds the common prime
  factors of different integers. It does **not** show that every dependence between them is local.
* EVIDENCE: the whole-family counts of (★) and b = 1 are positively associated after local controls. Z57_COMPLEMENT §4.3
  reports residual correlation 0.483 to 0.548 at 10⁸–10¹³. This measures the whole families, not their private-integer
  pieces. Z57_SYNTH reports a positive association of the same sign (≈ +0.29) between the C-parity halves of (★); those
  halves also live on disjoint sets of integers 4Cp + 1.

**Answer to the brief (scoped).**
* No mechanism making the two lines fail jointly "only rarely" was found beyond what Prop 3.1 and the menu obstruction
  say.
* The observed rarity (no prime joint zero ≤ 10¹¹; composite joint zeros {105, 4545} ≤ 10¹⁰) is *consistent with* a
  count heuristic: U is one line with more candidate events per residue class than (★). It is not explained by any
  proved statement here, and adaptive or growing arguments are not excluded.

*Which part of the profile matters (EVIDENCE, `Z59_A1CMASK` runs, odd non-squares n ≡ 1 (4) ≤ 10⁷).* The a = 1 part of
U is restricted to classes of T mod 4:

| allowed T mod 4 for the a = 1 part | non-square zeros of U ≤ 10⁷ |
|---|---|
| {1, 2, 3} (full U; T ≡ 0 is redundant by Prop 3.1) | 2 (105, 4545) |
| {1, 2} | 6 (105, 4545, 5481, 10305, 95505, 147609) |
| {2, 3} | 9 |
| {1, 3} | 18 |
| {2} | 24 |
| {3} | 66 |
| {1} | 63 |

No single residue class of T carries the rescue, which fits the count reading better than a single cheap slice.

## 4. Covering / forcing across c (inheritance, numerator ladder)

**Proposition 4.1 (no transport from a smaller integer into a prime; PROVED).**

*Setting.* Call φ(a,b,c,d) = (λa, λb, λ_c c, λ_d d), with λ, λ_c, λ_d ∈ ℚ_{>0}, an *equation-scaling transport* from
(n′, K′) to (n, K) (n′, n ≥ 1, K′, K ≡ 0 mod 4) if, as polynomials,

K·φ_aφ_bφ_cφ_d − φ_a − φ_b − n·φ_c = λ·(K′·abcd − a − b − n′c),

i.e. K′ = K·λλ_cλ_d and n′ = nλ_c/λ. Its domain is the set of solutions at (n′, K′) with
φ integral, and it maps them injectively to solutions at (n, K); composing with a ↔ b is allowed.

The following are all such transports:
* Z58_WILDCARD Lemma 4.1: (λ, λ_c, λ_d) = (1, 1, k), (n, kK) → (n, K).
* Lemma 4.2(a): (1, k, 1/k), (nk, K) → (n, K).
* Lemma 4.2(b): (1/k, 1, k), (nk, K) → (n, K).
* ET dilation: (1/g, 1/g, g²).
* Inverses and compositions with compatible endpoints.

*Statement.*
* (a) Let p be an odd prime. If a transport from (n′, K′) to (p, 4) has non-empty image, then p | n′, so n′ ≥ p.
  * So no solution at a prime is ever transported from a smaller integer.
  * n′ = 1 is excluded anyway: N^{(K)}(1) = 0, because K·abcd ≥ 4abc > a + b + c.
  * Transports from p itself or from multiples of p certainly exist. "Empty at primes" means only "no descent".
* (b) In particular N_II(p)[k | c] = N^{(4k)}(pk) for every k ≥ 1, via (a,b,c,d) ↦ (a, b, kc, d) from (pk, 4k).
  * For k = p the source integer is p², and twisted T1 (Z58_WILDCARD Lemma 4.3 with s = 1) gives N^{(4p)}(p²) = 0.
    So no Type II solution at a prime has p | c.
  * Also p ∤ abd for every solution at p (Z57_BFII Lemma 1.0).
* (c) Consequently any inheritance- or ladder-type argument for N_II(p) ≥ 1 within this class has to prove a statement
  equivalent to the non-emptiness of a sub-family at p or at a multiple of p. For composite n the sources n/ℓ are
  smaller, which is why inheritance explains part of F3 there (Z58_WILDCARD) but gives nothing at primes.

*Proof.*
* *The identity.* Comparing coefficients of a and b forces equal scalings of a and b. The coefficients of c and abcd
  then give the stated relations. WILDCARD's proofs show their maps satisfy the identity, and compositions of
  transports are transports.
* (a) Write v = v_p. From n′ = pλ_c/λ, v(n′) = 1 + v(λ_c) − v(λ). Suppose v(n′) = 0, so v(λ) = 1 + v(λ_c). Every
  solution at p has p ∤ a and p ∤ d (Z57_BFII Lemma 1.0; for every solution, not only primitive ones: otherwise p
  divides all three ES denominators).
  * If v(λ) ≥ 1, every image has a = λa′ with a′ ∈ ℤ, so v(a) ≥ 1. Contradiction.
  * If v(λ) ≤ 0, then v(λ_c) ≤ −1 and v(λ_d) = v(K′/4) − v(λ) − v(λ_c) = v(K′) − 2v(λ) + 1 ≥ 1 (p odd). So every image
    has v(d) ≥ 1. Contradiction.
* (b) 4k·abcd = a + b + pk·c ⟺ 4·ab(kc)d = a + b + p(kc). For k = p: N^{(4p)}(p²) = 0 by Lemma 4.3 (K = 4p, s = 1,
  m = p odd).
* (c) Follows from (a). ∎

The reviewer checked the count identity of (b) as complete solution sets for all odd primes p < 100 and k ≤ 7.

**Proposition 4.2 (c-lines collapse; PROVED).** The c-line at n (solutions with c fixed) is the set of events
E(4c²dn + 1, 4cd), d ≥ 1. Fix m and the admissible c (c² | m).
* If c | c′, the c-event on 4mn + 1 implies the c′-event, because 4m/c′ divides 4m/c.
* Two admissible c need not be comparable. With m = 36: at n = 31, E₃ holds (divisors 47, 95 ≡ −1 mod 48) and E₂ fails
  (mod 72); at the prime n = 461, E₂ holds (71 ≡ −1 mod 72) and E₃ fails. Both imply E₆.
* Every admissible c divides r(m), so every admissible c-event implies the r(m)-event. That event is itself admissible.
* Hence the union of all c-lines is the single line m ↦ E(4mn + 1, 4m/r(m)). "All c-lines fail" is one line failing,
  and complementarity among c-lines on a shared integer is impossible.
* For m ≠ m′, gcd(4mn + 1, 4m′n + 1) divides 4(m − m′). This bounds common factors only. ∎

*Reading (Assessment).* The brief asked whether inheritance or the numerator ladder gives a genuinely pointwise
covering across c. Within equation-scaling transports, they give no descent at primes (Prop 4.1). The c-lines do not
complement each other on shared integers (Prop 4.2). Arguments outside these classes are not excluded: adaptive
choices of c, non-monomial maps, and growing families. What remains visible is B2 for a single line (U, or the full
m-profile line).

## 5. Computations

**Engine** `scripts/z59_conv2_lines.c`.
* Target-set bitmaps for any union of lines (mask 1 = c = 1, 2 = a/b = 1, 4 = d = 1, 8 = full), for any K ≡ 0 (mod 4).
  The a = 1 part can be restricted to classes of c = T mod 4 (env `Z59_A1CMASK`).
* Per n: the least witness f ≤ FMAX by bitmap. Non-squares without one are sent to the exact (a, b)-loop
  K·ab·d = n + e, e | a + b, with line filters on (a, b, c, d). This is WILDCARD's exact path plus filters; it returns
  *some* witness, not the least.
* Odd squares are zeros by T1 and are only counted.

**Validation.**
* `scripts/z59_conv2_check.py`: an independent brute force (direct enumeration of (★) and a = 1 solutions; no witnesses
  or target sets) gives identical zero lists for c = 1, a = 1 and U, for K = 4 and K = 8, on all odd n ≡ 1 (4) ≤ 2·10⁴.
  The engine was run with FMAX = K − 1 (almost every n through the exact path) and with FMAX = 2000.
* All archived LATE witnesses were re-verified (K·abcd = a + b + nc, f = K·acd − 1, line membership): 11 366 for K = 4
  and 215 858 for K = 8, 0 bad.
* `scripts/z59_conv2_rawform.py`: Lemma 1(iii), (iv), (viii) against enumeration for all odd n ≤ 1500.
* Reproduced known lists: (★) zeros 409, 577, 5569, 9601, …; a = 1 zeros 193, 2521, 66529.
* Hostile reviewer (§8), independently:
  * reran U to 10⁸ and on [10⁹, 1.01·10⁹);
  * checked actual quadruples for 300 random n ∈ [10⁹, 10¹⁰);
  * reproduced all mask counts and the numerator-8 mod-3 census.

| run (odd non-squares) | result | file |
|---|---|---|
| K = 4, U, n ≡ 1 (4) ≤ 10⁹, FMAX 2·10⁴ | zeros **105, 4545**; 1 237 exact-path n; max least witness *among bitmap hits* 19 991 (n = 798 060 705; exact-path n have larger least witnesses, e.g. n = 291 669 has least witness 26 519); primes: max 15 231 (no prime went to the exact path) | `union_K4_1e9_mod1.txt` |
| same, (10⁹, 5·10⁹) and [5·10⁹, 10¹⁰) | **no zero**; 4 578 + 5 553 exact-path n (6 + 1 of them prime); bitmap-hit prime maxima 17 279, 18 983 | `union_K4_1e9_5e9_mod1.txt`, `union_K4_5e9_1e10_mod1.txt` |
| K = 4, U, n ≡ 3 (4) ≤ 10⁶ | no zero (Lemma 1(vii) proves it) | — |
| K = 4, c = 1 / a = 1 / U / full, n ≡ 1 (4) ≤ 10⁵ | 99 / 35 / 2 / 1 zeros | — |
| K = 8, U⁽⁸⁾, n ≡ 1 (4) ≤ 10⁸ | 547 zeros (45 primes, last 3 869 153; last composite 89 530 945) | `union_K8_1e8_mod1.txt.gz`, `union_K8_primes_1e8.txt` |
| K = 8, U⁽⁸⁾, n ≡ 3 (4) ≤ 10⁸ | 272 zeros (16 primes, last 1 226 891; last composite 93 398 595) | `union_K8_1e8_mod3.txt.gz` |
| K = 4, U with the a = 1 part restricted by T mod 4, n ≤ 10⁷ | §3 table | — |

The range (10⁸, 10¹⁰] was covered by one engine only. It is labelled CERTIFIED in the same sense as WILDCARD's 10¹⁰
census (which bounds the full family only). The reviewer's random sample and subrange rerun support it but do not
duplicate it.

## 6. Verdict, falsifier table restated, proposed FRONTIER text, bottom line

**Verdict: narrowed (scoped structure) + a sharper target. No mechanism.**
* *Narrowed.* PROVED, each in its stated scope:
  * a shared integer cannot give complementarity between the c = 1 and a = 1 lines (Prop 3.1), nor among c-lines
    (Prop 4.2);
  * fixed finite event menus fail jointly on a congruence class;
  * equation-scaling transports (inheritance, numerator ladder, dilation) give no descent into a prime (Prop 4.1);
  * the Type II tie is never weaker than a square root (Prop 2.1(a)).

  None of these excludes adaptive or growing arguments across different integers.
* *Sharper target.* CONJECTURE U: a one-parameter profile line (Lemma 1(iii)) whose only non-square zeros ≤ 10¹⁰ are
  105 and 4545 (CERTIFIED). It asks for more than CONV-II; at primes it is López's Conjecture 1. The next mechanism
  search can be posed for the pair (T, f) of one line.
* *Not achieved.* No pointwise lemma for U, (MS-II) or (MS). B2 is unchanged.

**Falsifier table, final** (as §0).
* F1: T1 per integer, via ker χ_{−T} on the odd part.
* F2: U⁽⁸⁾ has 819 odd non-square zeros ≤ 10⁸ (61 primes, last 3 869 153).
* F3: {105, 4545} ≤ 10¹⁰.
* F4: all known zeros rescued.

The structural statements of §§2–4 are theorems about the families, not mechanisms. None of them proves positivity
anywhere.

**Proposed FRONTIER text** (for the integrator; FRONTIER is not edited here).
* §2.4 / ladder: "(MS-U): U(p) ≥ 1 for primes p > 10¹⁷ in 𝔐. Here U = (c = 1) ∪ (a = 1) is the single line ∃T: Tp + 1
  has a divisor ≡ −1 (mod L_T), L_T = T (4 | T), 4T (else) (`Z59_CONV2.md` Lemma 1; the a = 1 half is the known
  'cp + 1 mod 4c' form). (MS) ⟹ (MS-U) ⟹ (MS-II). At primes U is López's Conjecture 1. Its only odd non-square zeros
  ≤ 10¹⁰ are 105 and 4545 (CERTIFIED; previously to 4·10⁶). Numerator 8: U⁽⁸⁾ has 61 prime zeros ≤ 10⁸ (all odd
  primes; last 3 869 153)."
* §6: "(z59) Coordinate lines of Type II cannot complement each other on a shared integer: the stronger event implies
  the weaker (`Z59_CONV2.md` Props 3.1, 4.2). Equation-scaling transports (inheritance, numerator ladder) give no
  descent into a prime (Prop 4.1). In the certified range the full family beyond U is needed only at n = 105."
* §7 item 18: add "a fixed-p argument for the U-line (Lemma 1(iii)) suffices for (MS-II). In the tested range the
  screens do not require the full family beyond U; the a = 1 branch of U itself uses c ≥ 2."

**Bottom line.** The brief asked what the extra Type II variables buy at a single p.
* Exactly: a square-root relaxation of the tie on the integers 4mp + 1 whose m has square factors, and τ(u) integers
  per modulus 4u instead of one or two.
* The family's good behaviour under the falsifiers, by contrast, is already present in the union of two one-parameter
  lines. That union is a single line: Tp + 1 must have a divisor ≡ −1 modulo T (4 | T) or 4T (otherwise). Up to 10¹⁰
  it fails at no odd non-square except 105 and 4545.
* The two lines cannot complement each other on the integers they share.
* Inheritance and the numerator ladder never transport a solution *to* a prime from anything smaller.
* No mechanism was found for the private integers. The data are consistent with a count heuristic, and the measured
  whole-family association is positive.

The wall is B2 for one line. The useful outcome is a sharper, smaller target, CONJECTURE U, together with a census
extension.

## 7. Reproduction

Every command under `ulimit -v 4000000` and `timeout 1800` (prefix omitted below).
```
gcc -O2 -o /tmp/z59l scripts/z59_conv2_lines.c -lm
/tmp/z59l 4 3 1 1000000000 20000 0 1           > data/z59/conv2/union_K4_1e9_mod1.txt        # ~1 min
/tmp/z59l 4 3 1000000000 5000000000 20000 0 1  > data/z59/conv2/union_K4_1e9_5e9_mod1.txt    # ~3 min
/tmp/z59l 4 3 5000000000 10000000000 20000 0 1 > data/z59/conv2/union_K4_5e9_1e10_mod1.txt   # ~3 min
/tmp/z59l 8 3 1 100000000 8000 1 1             > data/z59/conv2/union_K8_primes_1e8.txt
/tmp/z59l 8 3 1 100000000 8000 0 1 | gzip      > data/z59/conv2/union_K8_1e8_mod1.txt.gz
/tmp/z59l 8 3 1 100000000 8000 0 3 | gzip      > data/z59/conv2/union_K8_1e8_mod3.txt.gz
for m in 14 6 12 10 4 8 2; do Z59_A1CMASK=$m /tmp/z59l 4 3 1 10000000 4000 0 1 | grep -c ZERO; done
python3 scripts/z59_conv2_check.py 20000 4 /tmp/z59l data/z59/conv2/union_K4_*.txt
python3 scripts/z59_conv2_check.py 20000 8 /tmp/z59l data/z59/conv2/union_K8_*
python3 scripts/z59_conv2_rawform.py 1500
uv run --with sympy python scripts/z59_conv2_rescue.py 60 data/z58/screens/star_prime_zeros.txt 193 2521 66529 105 4545
python3 scripts/z59_conv2_localsplit.py > data/z59/conv2/localsplit.txt
```
(The plain-Python scripts need no packages; `uv run python …` works equally.)

## 8. Review record

**Hostile internal review** (deep-mode subagent; `data/z59/conv2/review_hostile.md`): 8 SERIOUS + 5 MINOR findings.
It confirmed:
* Lemma 1(i)–(viii) with their edge cases, Props 2.1, 3.1, 4.1 (valuation argument), 4.2's union formula;
* the K = 4 census (rerun to 10⁸, subrange of 10⁹, 300 random high n), all LATE certificates;
* the mask table, the rescue data, the localsplit counts, and the COMPLEMENT correlation numbers.

Fixes applied:

| # | finding | fix |
|---|---|---|
| 1 | K = 8 counts were for n ≡ 1 (4) only, but read as all odd n | ran n ≡ 3 (4) (272 zeros, 16 primes); totals 819 / 61 / 758 stated everywhere with domains |
| 2 | "234 rescued" included U's own zeros | 232 rescued + 2 U-zeros |
| 3 | bitmap maxima called maximum least witnesses | qualified "among bitmap hits"; example n = 291 669 (least witness 26 519) and the prime exact-path cases noted |
| 4 | wrong c = 1 small count (105) | 99 (n ≡ 1 (4) ≤ 10⁵) |
| 5 | F1 subgroup claim included the prime 2; reciprocity step needs p ≡ 1 (4) | restricted to odd prime factors; p ≡ 1 (4) stated |
| 6 | Theorem G attributed to the actual count | stated as genus-only; count gain labelled heuristic/EVIDENCE |
| 7 | privacy lemma and whole-family correlation turned into universal no-gos | rescoped: shared-integer domination, finite menus, common-factor bound; the rest "consistent with a count heuristic"; adaptive/growing arguments explicitly not excluded |
| 8 | FRONTIER text said c ≥ 2 unnecessary | "full family beyond U not needed in range; U's a = 1 branch uses c ≥ 2" |
| 9 | novelty overstated | credited z52d_pass2_TO8 and COMPLEMENT ({105, 4545}), CLASS_FORCING and CONVF (a = 1 one-line form), López source; new = combined profile, 10¹⁰ census, F2 profile |
| 10 | global completeness claims | restricted to f ∈ {3, 7, 15} / small moduli |
| 11 | "larger c dominates", and a reversed implication | divisibility order, incomparable example (m = 36, n = 31 / 461), all events imply the r(m) event |
| 12 | stale LATE counts and data size | 11 366 + 215 858 checked; K = 8 files gzipped, total ≈ 3.4 MB |
| 13 | min(2, τ(u)); gcd(n, f) = 1; transport endpoints; C-parity attribution (Z57_SYNTH); reproduction wrappers; rawform exit code | all applied |

A cross-model review will follow (WAIT; not merged).
