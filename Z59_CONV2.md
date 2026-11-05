# Z59_CONV2 — what the extra Type II variables buy at one p: the robustness is already in a one-parameter line (the c = 1 ∪ a = 1 union); no pointwise mechanism (verdict: narrowed + new target)

**ES is OPEN; nothing here proves or disproves it.** Lane CONV2 of wave z59 (`z52bbriefs/z59_lanes.md` §CONV2; rules
`z58_lanes.md` "Common rules" + falsifier table; `z53_depth.md` with z53 → z59). Scripts `scripts/z59_conv2_*`, data
`data/z59/conv2/` (< 2 MB). Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Status: final draft, hostile review pending (§8).

Notation. For odd n and K ≡ 0 (mod 4): N^{(K)}(n) = #{(a,b,c,d) ∈ ℕ⁴ : K·abcd = a + b + nc}; N_II = N^{(4)}.
Coordinate lines: **c = 1** (= (★), count R(n)); **a = 1** (∪ b = 1 by the a ↔ b symmetry; López's "Type A", B1_LINE's
"b = 1 line"); **d = 1**. U := (c = 1) ∪ (a = 1). For a witness f ≡ −1 (mod K): m_f = (f+1)/K, D_f = {a mod f : a | m_f}.
r(m) := the largest r with r² | m. 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^×.

**Verdict in one paragraph.** No pointwise mechanism was found; B2 did not move. What *was* found:
1. The brief's "two one-parameter lines" (c = 1 and a = 1) are, exactly, **one** one-parameter family of tied divisor
   events: some Tn + 1 has a divisor ≡ −1 mod L_T, with L_T = T for 4 | T and 4T otherwise (Lemma 1, PROVED). On the
   integers they share, one line's events contain the other's (in both natural coordinate systems). So "joint failure
   of two lines" is the failure of a single line, and complementarity on shared integers is impossible (Prop 3.1).
2. **This single line already passes F3**: among odd non-squares ≤ 10¹⁰ it vanishes only at 105 and 4545 (CERTIFIED).
   The full family vanishes only at 4545. So the F3-robustness that z58 attributed to the extra Type II variables is
   carried by a one-parameter line. The c- and d-variables add a log p to the count (Theorem G of Z57_BFII) and remove
   the single exception 105, but they are not what makes the family pass the screens (EVIDENCE + PROVED structure).
3. What c buys at one p, exactly (Prop 2.1): on the canonical integers 4mp + 1 the modulus relaxes from 4m to
   4m/r(m) (never below 2√(4m): the tie is at worst a square root), and per modulus 4u there are τ(u) integers c²p + u
   instead of one. Locally, the union recovers Mordell's complete Type II moduli {3, 7, 15}; (★) alone has only {3}
   (Prop 2.2). That local fact alone explains exactly the 5 (★)-zero primes outside 𝔐; the 9 in 𝔐 need non-local
   rescue.
4. Covering/forcing across c by inheritance or the numerator ladder is empty at primes (Prop 4.1, PROVED). On shared
   integers the c-lines are nested (larger c dominates), so the c-lines again collapse to one line (Prop 4.2).
5. Numerator 8 is *not* clean for the union: U⁽⁸⁾ has 547 odd non-square zeros ≤ 10⁸ (45 primes, last 3 869 153).

New target: **CONJECTURE U** (§1). It is a strictly stronger, two-variable version of CONV-II. It is López's Conjecture 1
at primes; the composite profile and the one-line form are new here.

## 0. Mandatory falsifier table (committed at checkpoint 1 in `a5b7c183`; final form)

Objects: the U-line (the new target) and the mechanisms examined in §§2–4.

| screen | behaviour | label |
|---|---|---|
| **F1 odd squares** | U ⊂ Type II, so U(m²) = 0 (every witness f has (n/f) = −1, Z57_BFII Prop 2.2). Lemma 1(iii) reads T1 per integer: on Tn + 1 the modulus L_T is the one that forces (n/f) = −1 (T odd: (T/f) = 1 needs f ≡ −1 mod 4T; T ≡ 2 (4): f ≡ 7 (8) is needed for (2/f) = 1; 4 ∣ T: mod T suffices). Hence at n = m² every prime of Tm² + 1 lies in ker χ_{−T}, a subgroup of (ℤ/L_T)^× not containing −1. Any proof must produce a prime ℓ ∣ Tp + 1 with (ℓ/p) = −1 and then the class −1; the first step is where non-squareness enters. Nothing in §§2–4 supplies the second step. | PROVED |
| **F2 numerator 8** | U⁽⁸⁾ = (c = 1 line of 8/n = R₈) ∪ (a = 1 line of 8/n) has **547 odd non-square zeros ≤ 10⁸: 45 primes (last 3 869 153) and 502 composites (last 89 530 945)**. An argument that applies verbatim to numerator 8 proves a false statement unless its threshold is ≥ 3 869 153 (primes) or ≥ 89 530 945 (all odd non-squares). K = 4 differs locally: its union has the complete moduli 3, 7, 15, K = 8 has none (f = 7: target set {1} for both lines). | CERTIFIED (≤ 10⁸) |
| **F3 composites** | **U vanishes at exactly two odd non-squares ≤ 10¹⁰: 105 = 3·5·7 and 4545 = 3²·5·101.** For n ≡ 3 (4) it holds always (Lemma 1(vii)). Compare (★): 285 composite zeros ≤ 8·10⁶; a = 1 alone: 35 zeros ≤ 10⁵ (32 composite). Of the 285 (★)-composite zeros, 51 are rescued by the complete moduli 7, 15 of U (local); 234 are not (176 divisible by 3, 15 coprime to 105) and are still rescued. Both U-zeros are divisible by 15, so "U for odd non-squares coprime to 15" has no exception ≤ 10¹⁰. | CERTIFIED (≤ 10¹⁰) |
| **F4 known zeros** | U ≥ 1 at all 14 (★)-zero primes (least a = 1 T: 2 at 11 of them, 5, 6, 5 at the others) and at the a = 1 zeros 193, 2521, 66529 ((★) at T = 8, 44, 8). No prime zero of U ≤ 10¹¹ (B1_LINE: a = 1 fails ≤ 10¹¹ only at those three). By Prop 3.1 every rescue of a (★)-zero by a = 1 is on an integer Tp + 1 with 4 ∤ T. The 12 R₈-zeros have R(p) ≥ 12; 24 of the 38 𝔊*-zeros have R ≥ 1 and the other 14 are the (★)-zero primes just treated; hence U ≥ 1 at all of them. | CERTIFIED + PROVED |

## 1. Precise statements and the one-line lemma

**Lemma 1 (one-line forms; PROVED, elementary).** Let n be odd.
* (i) R(n) ≥ 1 ⟺ ∃ T ≡ 0 (mod 4) such that Tn + 1 has a divisor f ≡ −1 (mod T).
* (ii) The a = 1 line is non-empty ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod 4T).
* (iii) **U(n) ≥ 1 ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod L_T), L_T := T if 4 | T, 4T otherwise.**
* (iv) (shift form) R(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod 4y); a = 1 ⟺ ∃ y ≡ 0 (4): n + y has a divisor
  ≡ −1 (mod y). So U(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod L_y), with the *same* profile.
* (v) (full family) N_II(n) ≥ 1 ⟺ ∃ m ≥ 1: 4mn + 1 has a divisor ≡ −1 (mod 4m/r(m)) ⟺ ∃ k ≥ 1: n + 4k has a divisor
  ≡ −1 (mod 4k/r(k)).
* (vi) (target sets at a witness f) c = 1: −n ∈ D_f; a = 1: −n ∈ D_f⁻¹ = 4D_f; d = 1: −n ∈ {4a² : a | m_f};
  full: −n ∈ {a/c : ac | m_f} = {4a²d : ad | m_f}.
* (vii) For n ≡ 3 (mod 4), (a,b,c,d) = (1, 1, 2, (n+1)/4) lies on the a = 1 line, so U(n) ≥ 1.
* (viii) (raw form) U(n) ≥ 1 ⟺ ∃ D ≡ 0 or 3 (mod 4), 3 ≤ D ≤ (4n+4)/3, such that r := (−n mod D) ≠ 0 divides
  ⌊D/4⌋ + 1. (For D ≡ 3 this is the (MS) d-form of (★); for D = 4b it is the a = 1 line.)

*Proof.* (i) With T = 4C, (Tu − 1)(TB − 1) = T(TuB − u − B) + 1 = Tn + 1. Conversely, if f ≡ −1 (mod T) divides
Tn + 1, its cofactor g is ≡ −1 (mod T) (fg ≡ 1), and u = (f+1)/T, B = (g+1)/T ≥ 1 solve 4uBC − u − B = n.
(ii) a = 1 reads b(4cd − 1) = cn + 1. With T = c, f = 4cd − 1 ≡ −1 (mod 4T) divides Tn + 1. Conversely put
d = (f+1)/(4T), b = (Tn+1)/f.
(iii) If 4 | T, then f ≡ −1 (mod 4T) implies f ≡ −1 (mod T); combine (i) and (ii).
(iv) Z57_BFII Lemma 1.1(e): f | n + 4a²d with f ≡ −1 (mod 4ad). For c = 1, f = 4ad − 1 and 4a²d ≡ a (mod f), so the
event is "n + a has a divisor ≡ −1 (mod 4a)". For a = 1 it is "n + 4d has a divisor ≡ −1 (mod 4d)" (López). For 4 | y,
a divisor ≡ −1 (mod 4y) is ≡ −1 (mod y).
(v) The (c,d)-slice is f | 4c²dn + 1, f ≡ −1 (mod 4cd), and the (a,d)-slice is f | n + 4a²d, f ≡ −1 (mod 4ad). For
fixed m = c²d the weakest modulus is at c = r(m), since c | c′ implies 4m/c′ | 4m/c, and every c with c² | m divides
r(m). Conversely, f ≡ −1 (mod 4m/r(m)) gives c = r(m), d = m/r(m)², a = (f+1)/(4cd) ≥ 1, b = (cn + a)/f. The (a,d)
statement is the same with k = a²d.
(vi) Z57_BFII Lemma 1.1(d), with 1/c ≡ 4·(m_f/c) because 4m_f ≡ 1 (mod f).
(vii) 4·1·1·2·(n+1)/4 = 2n + 2 = 1 + 1 + 2n.
(viii) Z58_CONVF (E5): solutions ↔ (a, b, e) with e | a + b and 4ab | n + e, d = (n+e)/(4ab). With a = 1, b ≥ 1: 4b | n + e
and e | b + 1. Since 1 ≤ e ≤ b + 1 < 4b for b ≥ 1, e is the least positive residue of −n mod D := 4b, and
⌊D/4⌋ + 1 = b + 1. For c = 1 use the (MS) d-form (`Z58_SUMMARY.md` preamble; d = 4uC − 1, r = u):
(d + 1)/4 = ⌊d/4⌋ + 1 for d ≡ 3 (4). The range bound is d ≤ (4n+1)/3, resp. 4b ≤ n + b + 1. CERTIFIED cross-check:
(iii), (iv), (viii) and direct enumeration agree for every odd n ≤ 1500 (`z59_conv2_rawform.py`). ∎

**CONJECTURE U (two-line converse of T1).** Every odd non-square n ∉ {105, 4545} has U(n) ≥ 1. Equivalently, some
Tn + 1 has a divisor ≡ −1 (mod L_T).
* CERTIFIED for n ≤ 10¹⁰ (§5).
* At primes this is López's Conjecture 1 (Type A ∪ Type B covers every prime; arXiv:2404.01508, quoted via B1_LINE §0).
  So it is not new as a prime statement. New here: the composite profile (F3), the F2 profile, and the one-line form.
* U ⟹ CONV-II, because N_II(105) ≥ 1 via c = 2 (Z57_COMPLEMENT §4.6).
* (MS-U), i.e. U(p) ≥ 1 for primes p > 10¹⁷ in 𝔐, implies (MS-II), hence ES relative to Mordell + Salez.

## 2. What the extra variables buy at a single p

**Proposition 2.1 (exact accounting; PROVED).** Fix an odd n.
* (a) *Square-root tie.* In the (c,d)-system every Type II event lives on an integer 4mn + 1 (m = c²d) and has modulus
  L = 4cd. Here L² = 16c²d² = 4d·(4m) ≥ 4·(4m). So the modulus never drops below 2√(4m): the extra variables relax the
  tie from linear to at worst square-root, never to a bounded modulus (consistent with B-fin: no fixed-modulus shot
  family).
* (b) *Shots per modulus.* N_II(n) ≥ 1 ⟺ ∃ u ≥ 1, ∃ c | u: c²n + u has a divisor ≡ −1 (mod 4u). The c = 1 line uses
  only n + u (c = 1), the a = 1 line only u²n + u (c = u). So the full family offers τ(u) integers per modulus 4u, the
  union U two.
* (c) *Lines collapse to profiles.* On a shared integer 4mn + 1 the c-line events are nested: c | c′ ⟹ the c-event
  implies the c′-event. So the full family is the single line m ↦ E(4mn + 1, 4m/r(m)) (Lemma 1(v)). Likewise U is the
  single line T ↦ E(Tn + 1, L_T) (Lemma 1(iii)).

*Proof.* (a) Arithmetic. (b) From Z57_BFII Lemma 1.1(e), f | cn + a with f ≡ −1 (mod 4ac). Multiply by c (a unit
mod f): f | c²n + ac. Put u = ac. Conversely a = u/c and d = (f+1)/(4u). (c) is the proof of Lemma 1(v). ∎

**Proposition 2.2 (local content: complete moduli; PROVED + CERTIFIED).** Call f *complete* for a family if its target
set is all of −{Jacobi-non-residue units mod f}.
* For U the complete moduli include 3, 7, 15. Indeed D₇ ∪ D₇⁻¹ = {1, 2, 4} and D₁₅ ∪ D₁₅⁻¹ = {1, 2, 4, 8}, the same as
  for full Type II (Z57_BFII Prop 3.1).
* For (★), D₇ = {1, 2} and D₁₅ = {1, 2, 4}, so among f ≤ 15 only f = 3 is complete for (★).
* Hence U(n) ≥ 1 whenever n is a Jacobi non-residue mod 3, 7 or 15 with gcd(n, 105) = 1 at the relevant modulus. This
  is Mordell's Type II covering, and U contains all of it.

CERTIFIED consequences (`data/z58/screens/`, one-off computation recorded in §5):
* Exactly the 5 (★)-zero primes *outside* 𝔐 (409, 577, 23929, 329617, 1134241) are non-residues mod 7 or 15.
* So U rescues them locally (e.g. 409 ≡ 3 (mod 7): f = 7 = 4·2·1 − 1 divides 2·409 + 1, which is a = 1 at T = 2).
* The 9 in 𝔐 are residues mod 3, 5, 7, so no complete modulus applies. U rescues them non-locally (least T = 2, 5, 6, …).
* Of the 285 (★)-composite zeros, 51 are rescued locally. The other 234 have no usable complete modulus (176 are
  divisible by 3), yet U still holds at all of them.

*Reading (Assessment).* The F3/F4 gap between (★) and U has two parts:
* a *local* part: (★) is Mordell-incomplete at 5 and 7;
* a *count* part: the a = 1 events on T ≢ 0 (mod 4) add trials in every residue class, including the Mordell-hard ones.

Neither part is a pointwise mechanism inside 𝔐. The local part is B1 (finite congruence covering). The count part is
the B3 lottery with more tickets.

## 3. Joint failure of two one-parameter lines

**Proposition 3.1 (nesting on shared integers; PROVED).**
* (a) T-system: for 4 | T, every a = 1 event on Tn + 1 (divisor ≡ −1 mod 4T) is a (★) event on Tn + 1 (≡ −1 mod T).
  At solution level, the map (1, b, 4C, d) ↦ (4d, (n + 4d)/f, 1, C), f = 16Cd − 1, is a bijection from
  {a = 1 solutions with 4 | c} onto {(★) solutions with 4 | u}. Both use the same witness f.
* (b) Shift system: for 4 | y, every (★) event on n + y (≡ −1 mod 4y) is an a = 1 event (≡ −1 mod y).
* (c) Hence U(n) = 0 ⟺ the single profile line of Lemma 1(iii) fails. A (★)-zero is rescued by the a = 1 line only
  through integers Tn + 1 with 4 ∤ T. An a = 1 zero is rescued by (★) only through integers n + y with 4 ∤ y.

*Proof.* (a) The first sentence is Lemma 1(iii). For the bijection: f = 4·c·d − 1 = 16Cd − 1 divides 4Cn + 1 ⟺ f
divides n + 4d, because 4C(n + 4d) = 4Cn + 16Cd ≡ 4Cn + 1 (mod f) and gcd(4C, f) = 1. Then (u, B, C) = (4d, (n+4d)/f, C)
satisfies (4uC − 1)B = f·B = n + 4d = n + u, i.e. 4uBC − u − B = n. The inverse sends (4d, B, 1, C) to
(1, (4Cn+1)/f, 4C, d). (b) is immediate. (c) follows. ∎

*Data* (`z59_conv2_rescue.py`, T ≤ 60). The 14 (★)-zero primes are rescued by a = 1 events at least T = 2 (11 primes),
5 (83449, 8 813 281) and 6 (102001), all with 4 ∤ T, as (c) requires. The a = 1 zeros 193, 2521, 66529 are rescued by
(★) events at least T = 8, 44, 8.

**What a complementarity mechanism would have to do (Assessment, backed by PROVED structure).**
* By Prop 3.1 it can only couple *different* integers: Tp + 1 with 4 | T against T′p + 1 with 4 ∤ T′.
* For different integers gcd(Tp + 1, T′p + 1) | T − T′ (privacy lemma, FRONTIER §3). So any coupling through common
  prime factors uses primes ≤ |T − T′|, i.e. residues of p modulo numbers far below the integers involved.
* For any *fixed finite* set of events (T, f), the class p ≡ 1 (mod 840·∏f) kills them all at once (Z57_BFII Prop 3.2
  argument: f | Tp + 1 then forces f | T + 1, impossible for f ≡ −1 (mod L_T), T ≥ 4; T ∈ {1, 2, 3} also fails by
  direct check).
* So joint failure of finitely many events is always realisable by congruences (positive density of primes, Dirichlet).
  The measured association between the two lines is positive (Z57_COMPLEMENT: STAR–B1 residual correlation +0.48 to
  +0.55 at 10⁸–10¹³). That has the same sign and the same structure as COMPLEMENT's C-parity halves of (★), which are
  also families on disjoint sets of integers Tp + 1 sharing p's local data.

**Answer to the brief (scoped).** There is no mechanism making the two lines fail jointly "only rarely" beyond trial
count:
* on shared integers joint failure is forced (nesting, PROVED);
* on private integers the measured coupling is positive (EVIDENCE);
* finite event sets fail jointly on congruence classes (PROVED).

The observed rarity (no prime joint zero ≤ 10¹¹; composite joint zeros {105, 4545} ≤ 10¹⁰) is the B3 lottery: the
union is one line with more tickets per residue class.

*Which part of the profile matters (EVIDENCE, `A1CMASK` runs, odd non-squares n ≡ 1 (4) ≤ 10⁷).* Restricting the a = 1
part of U to classes of T mod 4:

| allowed T mod 4 for the a = 1 part | non-square zeros of U ≤ 10⁷ |
|---|---|
| {1, 2, 3} (full U) | 2 (105, 4545) |
| {1, 2} | 6 (105, 4545, 5481, 10305, 95505, 147609) |
| {2, 3} | 9 |
| {1, 3} | 18 |
| {2} | 24 |
| {3} | 66 |
| {1} | 63 |

No single residue class of T carries the rescue. Every class contributes, which fits a count effect rather than one
structured cheap slice.

## 4. Covering / forcing across c (inheritance, numerator ladder)

**Proposition 4.1 (inheritance is empty at primes; PROVED).** Call a map φ(a,b,c,d) = (λa, λb, λ_c c, λ_d d) with
λ, λ_c, λ_d ∈ ℚ_{>0} an *equation-scaling transport* from (n′, K′) to (n, 4) if
4·abcd − a − b − nc evaluated at φ(a,b,c,d) equals λ·(K′·abcd − a − b − n′c) identically, i.e. K′ = 4λλ_cλ_d and
n′ = nλ_c/λ. Every map of Z58_WILDCARD Lemmas 4.1, 4.2(a), 4.2(b), ET dilation, their inverses and compositions is such
a transport (composed with a ↔ b if needed); each sends the solutions at (n′, K′) in its domain (where φ is integral)
bijectively onto a sub-family of solutions at (n, 4) defined by divisibility conditions.
* (a) Let p be an odd prime. If a transport from (n′, K′) to (p, 4) has non-empty image, then p | n′; in particular
  n′ ≥ p. So no solution at a prime is ever transported from a smaller integer (n′ = 1 is excluded anyway:
  N^{(K)}(1) = 0, since K·abcd ≥ 4abc > a + b + c).
* (b) In particular N_II(p)[k | c] = N_II(pk)[k | d] = N^{(4k)}(pk) for every k ≥ 1. For k = p·s² with s odd, the right
  side vanishes by twisted T1 (Z58_WILDCARD Lemma 4.3, pk = (ps)²). So no Type II solution at a prime has p | c. Also
  p ∤ a, b, d (Z57_BFII Lemma 1.0).
* (c) So any inheritance or ladder argument for N_II(p) ≥ 1 must first prove an equivalent statement about a sub-family
  at p or at a multiple of p. No smaller source exists. For composite n the sources n/ℓ are smaller, which is why
  inheritance explains part of F3 there (Z58_WILDCARD) but not at primes.

*Proof.* The identity forces equal scalings of a and b (coefficients of a, b) and then the stated relations
(coefficients of c and abcd); WILDCARD's maps satisfy it by their proofs, and compositions of transports are transports.
(a) Write v = v_p. From n′ = pλ_c/λ, v(n′) = 1 + v(λ_c) − v(λ). Suppose v(n′) = 0, so v(λ) = 1 + v(λ_c). At a prime p
every solution has p ∤ a and p ∤ d (Z57_BFII Lemma 1.0: p ∤ abd). If v(λ) ≥ 1, every image has a = λa′ with a′ ∈ ℤ,
hence v(a) ≥ 1: empty. If v(λ) ≤ 0, then v(λ_c) ≤ −1 and v(λ_d) = v(K′) − v(λ) − v(λ_c) = v(K′) − 2v(λ) + 1 ≥ 1, so every
image has v(d) ≥ 1: empty. (b) Apply Lemma 4.2(a) with N = pk, then Lemma 4.1 with the factor k on d,
which turns (pk, 4) with k | d into (pk, 4k). For k = p·s², pk = (ps)² and N^{(4k)}((ps)²) = 0 by Lemma 4.3 with the
twist s₀ = 1. ∎

**Proposition 4.2 (c-lines collapse; PROVED).** The c-line at n (solutions with c fixed) is the set of events
E(4c²dn + 1, 4cd), d ≥ 1. If c²d = c′²d′ =: m and c | c′, the c-event on 4mn + 1 implies the c′-event (the modulus
4m/c′ divides 4m/c). Every c with c² | m divides r(m), so on each integer 4mn + 1 all c-line events are implied by the
r(m)-event, and the union of all c-lines is the single line m ↦ E(4mn + 1, 4m/r(m)). In particular "all c-lines fail"
is one line failing, and covering across c on shared integers is impossible. Different m are private integers:
gcd(4mn + 1, 4m′n + 1) divides 4(m − m′). ∎

*Reading (Assessment).* The brief asked whether inheritance or the ladder gives a genuinely pointwise covering across
c. At primes the answer is no (Prop 4.1). The c-lines do not complement each other on shared integers (Prop 4.2).
Different integers are private, and they couple only through p's residues modulo small numbers. That is B1 data, blind
at the T1 point (Z57_BFII Prop 3.2). What remains is the familiar B2 statement for a single line (U, or the full
m-profile line).

## 5. Computations

**Engine.** `scripts/z59_conv2_lines.c`.
* Target-set bitmaps for any union of lines (mask: 1 = c = 1, 2 = a/b = 1, 4 = d = 1, 8 = full), for any K ≡ 0 (mod 4).
* The a = 1 part can be restricted to classes of c = T mod 4 via env `Z59_A1CMASK`.
* For each n: least witness f ≤ FMAX. Non-squares without a witness go to the exact (a, b)-loop K·ab·d = n + e,
  e | a + b, with line filters on (a, b, c, d) (WILDCARD's exact path plus filters).
* Odd squares are zeros by T1 and are only counted.

**Validation.**
* `scripts/z59_conv2_check.py`: an independent brute force (direct enumeration of (★) and a = 1 solutions; no
  witnesses, no target sets) gives identical zero lists for c = 1, a = 1 and U, for K = 4 and K = 8, on all odd
  n ≡ 1 (4) ≤ 2·10⁴. Engine runs used FMAX = K − 1 (every n through the exact path) and FMAX = 2000.
* Every LATE witness in the data files was re-verified (K·abcd = a + b + nc, f = K·acd − 1, line membership): 3 079 + 10 131
  lines, 0 bad.
* `scripts/z59_conv2_rawform.py`: Lemma 1(iii), (iv), (viii) against enumeration for all odd n ≤ 1500.
* The c = 1 and a = 1 zero lists reproduce the known ones: (★) primes 409, 577, 5569, 9601, … and a = 1 primes 193,
  2521, 66529.

| run | result | file |
|---|---|---|
| K = 4, U, odd n ≡ 1 (4) ≤ 10⁹, FMAX 2·10⁴ | non-square zeros **105, 4545**; 1 237 exact-path n; max least witness 19 991 (n = 798 060 705), primes 15 231 | `union_K4_1e9_mod1.txt` |
| same, (10⁹, 5·10⁹) and [5·10⁹, 10¹⁰) | **no zero**; 4 578 + 5 553 exact-path n; primes max least witness 17 279, 18 983 | `union_K4_1e9_5e9_mod1.txt`, `union_K4_5e9_1e10_mod1.txt` |
| K = 4, U, odd n ≡ 3 (4) ≤ 10⁶ | no zero (Lemma 1(vii) proves it) | — |
| K = 4, c = 1 / a = 1 / U / full, n ≤ 10⁵ | 105 / 35 / 2 / 1 non-square zeros | — |
| K = 8, U⁽⁸⁾, odd n ≡ 1 (4) ≤ 10⁸ | 547 non-square zeros (45 primes, last 3 869 153; last composite 89 530 945) | `union_K8_1e8_mod1.txt`, `union_K8_primes_1e8.txt` |
| K = 4, U with a = 1 restricted by T mod 4, n ≤ 10⁷ | §3 table | — |

The census is one engine plus an independent brute force on the low range. The (10⁹, 10¹⁰) range has no second
engine (one-engine CERTIFIED, as for WILDCARD's 10¹⁰ census, which bounds the full family only).

## 6. Verdict, falsifier table restated, proposed FRONTIER text, bottom line

**Verdict: narrowed (mechanism) + strengthened (target).**
* *Narrowed.* PROVED scoped no-gos:
  * no complementarity between the c = 1 and a = 1 lines on shared integers (Prop 3.1);
  * no complementarity between c-lines on shared integers (Prop 4.2);
  * inheritance and the numerator ladder are empty at primes (Prop 4.1);
  * the Type II tie is never weaker than a square root (Prop 2.1(a)).
  
  The only cross-integer coupling is local (privacy), and the measured association is positive.
* *Strengthened (target).* CONJECTURE U: a one-parameter line with only two non-square zeros ≤ 10¹⁰ (CERTIFIED). It
  is strictly stronger than CONV-II and has one variable fewer. So the next mechanism search can be run on a
  two-variable problem (T, f), not a four-variable one.
* *Not achieved.* No pointwise lemma for U, (MS-II) or (MS). B2 is unchanged.

**Falsifier table, final.** As in §0.
* F1: T1 holds per integer Tn + 1 via ker χ_{−T}.
* F2: U⁽⁸⁾ is false up to 3 869 153 at primes and up to 8.95·10⁷ at composites.
* F3: {105, 4545} ≤ 10¹⁰.
* F4: all known zeros are rescued.

None of the mechanisms in §§2–4 survives as a mechanism. They are structure theorems.

**Proposed FRONTIER text (for the integrator; do not edit FRONTIER here).**
* §2.4 / ladder: "(MS-U): U(p) ≥ 1 for primes p > 10¹⁷ in 𝔐, where U = (c = 1) ∪ (a = 1) is the single line ∃T: Tp + 1
  has a divisor ≡ −1 (mod L_T), L_T = T (4 | T), 4T (else) (`Z59_CONV2.md` Lemma 1). (MS) ⟹ (MS-U) ⟹ (MS-II). U has no
  odd non-square zero ≤ 10¹⁰ except 105 and 4545 (CERTIFIED); U⁽⁸⁾ fails at 45 primes ≤ 10⁸ (last 3 869 153)."
* §6: "(z59) Complementarity of coordinate lines of Type II: impossible on shared integers (nesting,
  `Z59_CONV2.md` Props 3.1, 4.2); inheritance/numerator ladder empty at primes (Prop 4.1). The F3-robustness of Type II
  is already carried by the one-parameter line U."
* §7 item 18: replace "a fixed-p argument using c ≥ 2" by "a fixed-p argument for the U-line (Lemma 1(iii)); c ≥ 2 is
  not needed for the screens".

**Bottom line.** The brief asked what the extra Type II variables buy at a single p. The answer is less than hoped.
Their famous robustness under the falsifiers is already present in the union of two one-parameter lines. That union is
literally one line: Tp + 1 must have a divisor ≡ −1 modulo T or 4T. It fails at no odd non-square up to 10¹⁰ except 105
and 4545. What c adds at fixed p is a square-root relaxation of the tie on integers 4mp + 1 with square factors in m,
and τ(u) instead of two integers per modulus. That is a log p more trials, not a mechanism. The two lines cannot
complement each other on the integers they share. On their private integers they are coupled only through p's residues
modulo small numbers, and the measured coupling is positive. Inheritance and the numerator ladder never transport
solutions *to* a prime from anything smaller. The wall is B2 for one line. The useful outcome is a sharper, smaller
target: CONJECTURE U.

## 7. Reproduction

All runs under `ulimit -v 4000000` and `timeout ≤ 1800`.
```
gcc -O2 -o /tmp/z59l scripts/z59_conv2_lines.c -lm
/tmp/z59l 4 3 1 1000000000 20000 0 1          > data/z59/conv2/union_K4_1e9_mod1.txt         # ~1 min
/tmp/z59l 4 3 1000000000 5000000000 20000 0 1 > data/z59/conv2/union_K4_1e9_5e9_mod1.txt     # ~3 min
/tmp/z59l 4 3 5000000000 10000000000 20000 0 1 > data/z59/conv2/union_K4_5e9_1e10_mod1.txt   # ~3 min
/tmp/z59l 8 3 1 100000000 8000 1 1            > data/z59/conv2/union_K8_primes_1e8.txt
/tmp/z59l 8 3 1 100000000 8000 0 1            > data/z59/conv2/union_K8_1e8_mod1.txt
for m in 15 6 12 10 4 8 2; do Z59_A1CMASK=$m /tmp/z59l 4 3 1 10000000 4000 0 1 | grep -c ZERO; done
python3 scripts/z59_conv2_check.py 20000 4 /tmp/z59l data/z59/conv2/union_K4_*.txt data/z59/conv2/union_K8_*.txt
python3 scripts/z59_conv2_check.py 20000 8 /tmp/z59l
python3 scripts/z59_conv2_rawform.py 1500
uv run --with sympy python scripts/z59_conv2_rescue.py 60 data/z58/screens/star_prime_zeros.txt 193 2521 66529 105 4545
python3 scripts/z59_conv2_localsplit.py > data/z59/conv2/localsplit.txt      # §2.2 complete-moduli split
```

## 8. Review record
(pending)
