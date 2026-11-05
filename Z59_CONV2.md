# Z59_CONV2 — what the extra Type II variables buy at one p: the two-line union is a one-parameter target that passes F3 (checkpoint 1)

**ES is OPEN; nothing here proves or disproves it.** Lane CONV2 of wave z59 (`z52bbriefs/z59_lanes.md` §CONV2; rules
`z58_lanes.md` "Common rules" + falsifier table; `z53_depth.md` with z53 → z59). Scripts `scripts/z59_conv2_*`, data
`data/z59/conv2/`. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Status: **checkpoint 1** (statements, falsifier table, first lemma, first computation). Not yet reviewed.

Notation. For odd n and K ≡ 0 (mod 4): N^{(K)}(n) = #{(a,b,c,d) ∈ ℕ⁴ : K·abcd = a + b + nc}; N_II = N^{(4)}.
Lines: **c = 1** (= (★), count R(n)); **a = 1** (∪ b = 1 by the a ↔ b symmetry; López's Type A, B1_LINE's "b = 1 line");
**d = 1**. For a witness f ≡ −1 (mod K) put m_f = (f+1)/K and D_f = {a mod f : a | m_f}.

## 0. Mandatory falsifier table (checkpoint 1; restated at the end)

The object of this lane is the *mechanism* question of the brief; the statement-level object that came out of the first
hour is the **two-line union U := (c = 1) ∪ (a = 1)**, which Lemma 1 shows is a *single* one-parameter family of tied
divisor events (§1). Table for U (and, where different, for the brief's (MS-II)):

| screen | behaviour of U / of the mechanisms examined | label |
|---|---|---|
| **F1 odd squares** | U is a sub-family of Type II, so U(m²) = 0 (every witness f has (n/f) = −1, Z57_BFII Prop 2.2). Lemma 1(iii) shows *why* the modulus profile L_T is what it is: L_T is exactly the modulus that makes (n/f) = −1 forced on the integer Tn + 1 (T odd: (T/f) = 1 needs f ≡ −1 mod 4T; T ≡ 2 (4): mod 8·T/2 = 4T; 4 | T: mod T). Any proof must produce a divisor with (n/f) = −1, i.e. use non-squareness. | PROVED |
| **F2 numerator 8** | The numerator-8 union U⁽⁸⁾ = R₈-line ∪ (a = 1 line of 8/n) **fails** at 45 primes ≤ 10⁸ (last 3 869 153; `union_K8_primes_1e8.txt`) and at 153 odd non-squares ≤ 2·10⁴ (brute force). An argument that applies verbatim to numerator 8 must have threshold ≥ 3 869 153. The K = 4 union instead has the complete moduli 3, 7, 15 (same as full Type II, §1), K = 8 has none. | CERTIFIED (≤ 10⁸) |
| **F3 composites** | **U vanishes at exactly two odd non-squares ≤ 10⁹: 105 and 4545** (all n ≡ 1 (4); n ≡ 3 (4) is trivial, Lemma 1(vii)). Compare: (★) alone 285 composite zeros ≤ 8·10⁶; a = 1 alone 35 zeros ≤ 10⁵ (32 composite). So adding the T ≢ 0 (mod 4) events of the a = 1 line removes all but two composite zeros. | CERTIFIED (≤ 10⁹; 10¹⁰ running) |
| **F4 known zeros** | U ≥ 1 at all 14 (★)-zero primes (a = 1 witnesses, CONVF) and at the a = 1 zeros 193, 2521, 66529 ((★) witnesses); no prime zero of U ≤ 10¹¹ (B1_LINE census of the a = 1 line + (★) at its three zeros). By Lemma 1(iii) every rescue of a (★)-zero by the a = 1 line happens on an integer Tp + 1 with 4 ∤ T. | CERTIFIED + PROVED |

## 1. Precise statements and the first lemma

**Lemma 1 (one-line form of the two lines; PROVED, elementary).** Let n be odd.
* (i) R(n) ≥ 1 ⟺ ∃ T ≡ 0 (mod 4) such that Tn + 1 has a divisor f ≡ −1 (mod T).
* (ii) the a = 1 line is non-empty ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod 4T).
* (iii) U(n) ≥ 1 ⟺ ∃ T ≥ 1 such that Tn + 1 has a divisor f ≡ −1 (mod L_T), where L_T := T if 4 | T and L_T := 4T
  otherwise. On the shared integers (4 | T) the a = 1 events are contained in the (★) events.
* (iv) (shift form) R(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod 4y); a = 1 ⟺ ∃ y ≡ 0 (4): n + y has a divisor
  ≡ −1 (mod y); so U(n) ≥ 1 ⟺ ∃ y: n + y has a divisor ≡ −1 (mod L_y), the *same* profile. On shared integers (4 | y)
  now (★) ⊂ (a = 1).
* (v) (full family) N_II(n) ≥ 1 ⟺ ∃ m ≥ 1: 4mn + 1 has a divisor ≡ −1 (mod 4m/r(m)) ⟺ ∃ k ≥ 1: n + 4k has a divisor
  ≡ −1 (mod 4k/r(k)), where r(m) is the largest r with r² | m. Every Type II event on the integer Tn + 1 (T = 4c²d) has
  modulus L = 4cd with L² = 4dT ≥ 4T: **the tie is never weaker than a square root.**
* (vi) (target sets at a witness f) c = 1: −n ∈ D_f; a = 1: −n ∈ D_f⁻¹ = 4D_f; d = 1: −n ∈ 4·{a² : a | m_f};
  full: −n ∈ {a/c : ac | m_f} = {4a²d : ad | m_f}. The complete moduli of U are 3, 7, 15 (D₇ ∪ D₇⁻¹ = {1, 2, 4},
  D₁₅ ∪ D₁₅⁻¹ = {1, 2, 4, 8}), the same as for full Type II (Z57_BFII Prop 3.1).
* (vii) For n ≡ 3 (mod 4), (a,b,c,d) = (1, 1, 2, (n+1)/4) lies on the a = 1 line, so U(n) ≥ 1.

*Proof.* (i) (★) with T = 4C: (Tu − 1)(TB − 1) = T(TuB − u − B) + 1 = Tn + 1; conversely a divisor f ≡ −1 (mod T) of
Tn + 1 has cofactor g ≡ −1 (mod T) (fg ≡ 1), and u = (f+1)/T, B = (g+1)/T ≥ 1 solve (★). (ii) a = 1: b(4cd − 1) =
cn + 1, so with T = c, f = 4cd − 1 ≡ −1 (mod 4T) divides Tn + 1; conversely d = (f+1)/(4T), b = (Tn+1)/f. (iii) If 4 | T,
f ≡ −1 (mod 4T) implies f ≡ −1 (mod T); combine (i), (ii). (iv) Z57_BFII Lemma 1.1(e) with c = 1: f = 4ad − 1 | n + a
(u-form); with a = 1: f ≡ −1 (mod 4d), f | n + 4d (López). (v) (c,d)-slice f | 4c²dn + 1, f ≡ −1 (mod 4cd), and the
(a,d)-slice f | n + 4a²d, f ≡ −1 (mod 4ad); for fixed m = c²d the weakest modulus is at c = r(m) (if c | c′ then
4m/c′ | 4m/c), and conversely f ≡ −1 (mod 4m/r(m)) gives c = r(m), d = m/r(m)², a = (f+1)/(4cd). (vi) Z57_BFII Lemma 1.1(d)
with 1/c ≡ 4·(m_f/c) (as 4m_f ≡ 1 mod f); the complete-moduli check is finite. (vii) 4·1·1·2·(n+1)/4 = 2n + 2. ∎

**CONJECTURE U (two-line converse of T1).** Every odd non-square n ∉ {105, 4545} has U(n) ≥ 1, i.e. some Tn + 1 has a
divisor ≡ −1 (mod L_T). CERTIFIED for n ≤ 10⁹ (§2). At primes this is López's Conjecture 1 (Type A ∪ Type B; López
arXiv:2404.01508; B1_LINE §0) — not new as a prime statement; the composite profile and the one-line form are new here.
CONJECTURE U ⟹ CONV-II (N_II(105) ≥ 1 via c = 2, Z57_COMPLEMENT), and (MS-U) (U at primes > 10¹⁷ in 𝔐) ⟹ (MS-II) ⟹ ES
relative to Mordell + Salez.

**Why this matters for the brief (Assessment).** The brief asks what the extra Type II variables buy at a single p. Lemma 1
says the robustness of the full family against F3 is *already present* in a one-parameter family: (★) ∪ (a = 1) is a
single sequence of integers Tn + 1 (all T, not only 4 | T) with a modulus profile L_T ∈ {T, 4T}. The c- and d-variables of
the full family relax the modulus further (to 4m/r(m)) but are not needed to pass F1–F4 in the tested range. So the
mechanism question can be asked for a *two-variable* problem: why does every non-square n ∉ {105, 4545} have some T for
which Tn + 1 has a divisor in the class −1 mod L_T?

## 2. Computations (checkpoint 1)

Engine `scripts/z59_conv2_lines.c` (target-set bitmaps for any union of lines, any K; least witness f ≤ FMAX; exact
(a,b)-loop fallback with line filters for non-squares without a witness). Validation `scripts/z59_conv2_check.py`: an
independent brute force (direct enumeration of (★) and a = 1 solutions, no witnesses) gives identical zero lists for
c = 1, a = 1 and U, K = 4 and K = 8, all odd n ≡ 1 (4) ≤ 2·10⁴, both with FMAX = K − 1 (every n through the exact path)
and FMAX = 2000; every LATE witness in the data files re-verified (K·abcd = a + b + nc, line membership).

| run | result |
|---|---|
| K = 4, U, odd n ≡ 1 (4) ≤ 10⁹, FMAX 2·10⁴ | non-square zeros **105, 4545** only; 1 237 n resolved by the exact path; max least witness 19 991 (n = 798 060 705), primes 15 231 (p = 417 131 269) |
| K = 4, U, odd n ≡ 3 (4) ≤ 10⁶ | no zero (Lemma 1(vii) proves it) |
| K = 4, c = 1 / a = 1 / U / full, n ≤ 10⁵ | 105 / 35 / 2 / 1 non-square zeros (c = 1 list starts 57, 105, 177, …; a = 1: 33, 105, 145, 193, …) |
| K = 8, U⁽⁸⁾, primes ≤ 10⁸ | 45 prime zeros, last 3 869 153 |
| K = 8, U⁽⁸⁾, odd n ≡ 1 (4) ≤ 10⁶ | 395 non-square zeros (42 primes) |

## 3. Plan after checkpoint 1
1. Extend the K = 4 union census to 10¹⁰ (running) and the K = 8 union to composites ≤ 10⁸ (F2 composite profile).
2. Mechanism: why do the T ≢ 0 (mod 4) integers rescue the (★) composite zeros? (local profile of the 285; the role of the
   complete moduli 3, 7, 15 shared by U and the full family but absent for (★) alone).
3. The brief's three questions as scoped results: (a) what c buys at one p (Lemma 1(v): square-root tie; τ(u) integers
   c²p + u per modulus 4u); (b) joint failure of the two lines — nesting on shared integers (Lemma 1(iii)) vs. private
   integers; (c) covering/forcing across c (inheritance, ladder): scoped no-go.
