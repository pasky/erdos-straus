# AGENT_REPORT_O238 — Synthesis VI over wave Z (checkpoint 1)

Branch side-agent/synthesis-six. Deep file SYNTHESIS_SPARKS6.md; memos BRAINSTORM/s6_*.md (9, indexed in BRAINSTORM/README.md);
scripts scripts/s6_*; certificate data/s6_cert105_et.json (2 KB).

**SHARP:** ES holds for every n = 4^s + 105 (s ≥ 0) — (J)62's open, Mordell-hard-for-all-s offset — PROVED (computer-
assisted). (J)62's 13-class ET covering at L = 360 leaves exactly s ≡ 34 (mod 90); ONE exponential window class closes it:
for u ≡ 32 (mod 151), n = 256u³ + 105, x = 64(u³+1), A = (64u³ + 2u² − 2u + 66)/151, y = nA, z = 32n(u+1)A solves
4/n = 1/x + 1/y + 1/z (one-line identity: 4x − n = 151 and 2(32u+33)(u² − u + 1) = 151A), and s ≡ 34 (mod 45) gives
u = 4^{(s−4)/3} ≡ 32 (mod 151). The class is CAP_DOWN Lemma 1.1 at the window 151 = 4⁴ − 105 with the divisor ratio
2⁻⁵/(4^{r/3} + 1): the budget is forced by the cyclotomic factorisation of 4^r + 1. The class s ≡ 34 (45) is an ordinary
residue class (even of n_s mod 4⁴⁵ − 1), but the identity is not polynomial in n (it uses u = ((n − 105)/256)^{1/3}). So (J)62's
"mixed points" are sterile only for menus of polynomial-in-n (fixed-parameter) ET identities: that is the violated
hypothesis of EXPONENT_COVERING Thm 1.4. Mixed point μ* ↔ the cube-root parameter u (3-adic component −2).
Relay suggestion: exponential classes for k = 33, 273, 297 (Sophie-Germain/difference shapes, Type I exponential classes;
k = 33's residual is at μ = −2, where 4^{s+2} − 1 would be the natural factorisation).

## Results
* Thm 1.1 (PROVED, computer-assisted): ES for all 4^s + 105. Checker `scripts/s6_cert105_check.py data/s6_cert105_et.json 1500`
  (sympy; re-verifies every ET identity, integer-valuedness, positivity, periodicity, no odd square in non-divisor classes,
  coverage of s mod 360, the exponential identity, and exact solutions for all s ≤ 1500; < 1 s). Certificate built by
  `s6_cert105_make.py` (z8 seeding, 13 classes; ~1 min). Search driver `s6_hybrid105.py 105 360 2000 20000 1e15 7 45`.
* (i) s6_unique_forced_cap0 (PROVED): the forced bit gives cap 0 for every K only at m = 3. s6_divisor_pigeonhole (PROVED):
  |P| > (q−1)/2 ⟹ cap 0; structure-free strengthenings need Ω(K) ≳ q/4 (Cauchy–Davenport, sharp).
* (i) × numerators, s6_numerator_windows (PROVED only-if; EVIDENCE for existence): the self-generated mute set works for
  every ν/n; at odd squares forced windows are impossible iff-direction proved for 4 | ν, ν ≡ 3 (4), ν = □ — a strictly
  larger set than (J)46's T1 numerators (window shape is more T1-rigid than ES_ν).
* (iii) s6_witness_onesided: (q/p) = −1 is not necessary for cap 0 at q (non-square d); cap-0 rates 34 % vs 18 % (EVIDENCE).
* (iv) s6_ydual_windows: 𝒟_e(M) is the y-window (fixed mute set ⟹ almost-all side); x-windows own their mute set (pointwise).
* (v) s6_mixed_points_cuberoots: sterility is menu-relative (Assessment; 105 instance PROVED).
* Negatives: s6_window_independence (gcd(K_m, K_m′) | (m − m′)/4 — almost coprime mute sets; independence only heuristic), s6_exp_classes_primes (algebraic
  budget forcing needs a thin family; for primes it is B2).
* For ES at primes nothing new: cap 0 at a window stays B2. No claim about ES or any infinite set of primes.

## Self-review (codex deep, R-O238) — repairs applied
No FATAL; theorem re-verified (identity by hand, 4¹⁰ ≡ 32, coverage {34,124,214,304} mod 360, all moduli odd). MAJOR repaired:
numerator-window forcing needs K odd (counterexample ν = 4, n = 5, m = 67); Cauchy–Davenport count must exclude zero log-images;
the exp class is a congruence class (mod 4⁴⁵ − 1) — the novelty is the non-polynomial identity; window independence is a
heuristic. Minor: u ≥ 1 in Lemma 1.0; checker's 2-part assumption (all moduli here odd).

## Honest caveats for the reviewer
* The 13 ET classes are produced by (J)62's z8 code (`ec_cover.certificate`); my checker re-verifies them independently from
  the JSON, but a from-scratch reviewer checker would be good.
* The exponential class contains no squares by the global Lemma-1.1 T1 (CAP_DOWN §3), not by a congruence: n ≡ 59 (mod 151)
  is a QR. Numerically no square for u < 3·10⁷ on the class.
* Whether NEAR_SQUARE Thm 2.2's witness argument extends to families m = 16u^{3/2} was not examined (not needed for Thm 1.1).
* The "primes to 10⁶" triple-check rule does not apply to a family theorem; the exact check to s = 1500 and the symbolic
  identity replace it.

## Sparks (not pursued)
1. Exponential classes for k = 33, 273, 297 and the full k ≡ 9 (24) list; c₀ ≠ 1 families; other bases (3^s, 5^s).
2. A general theorem: for n_s = b^s + k, coverings by ET + exponential classes exist iff ??? (an Ẑ-criterion with
   "algebraic points" added to the limit set — the exponential analogue of EXPONENT_COVERING Thm 1.4).
3. Does (J)54's sterile Mordell point admit an exponential/algebraic family through it (non-sterility for richer menus)?
4. Window-shape T1 existence direction for ν ≡ 2 (4) and non-square ν ≡ 1 (4) (Dirichlet), and its meaning for ES_ν.
5. Polynomial ES families on cubic/sextic families n = c·u³ + k: a classification analogous to NEAR_SQUARE Thm 2.2.
