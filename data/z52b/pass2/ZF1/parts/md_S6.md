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
* Per level: C = 1: Var/Mean 3.81, C = 2: 2.64, C = 3..8: 1.3–1.8, every dyadic bucket C ≥ 32: 0.96–1.09 (Poisson).
  Cross-level covariances carry 33 % (10⁷) / 38 % (10⁸) of Var S although mean pairwise correlation is only 0.012.
* **The over-dispersion has an exact source:** the edge lines u = 1 or B = 1 are B(4C − 1) = p + 1, i.e.
  E(p) = #{d | p + 1 : d ≡ 3 (mod 4)} unordered solutions (PROVED, one line) — a Titchmarsh-divisor-problem object.
  E has mean 5.3 / 6.0 and Var/Mean 5.5 / 7.3 and explains 44 % of Var S at both heights; the interior S − E has
  Var/Mean 1.69 / 1.94 (1.39 / 1.65 after mod 840), and corr(E, S − E) = −0.13.
  Smooth weights vanishing at the simplex boundary (Z2902) reproduce this: Var/Poisson drops from 5.0–5.9 (sharp R) to
  1.9–2.4, and the Mordell-hard-class deficit of R (0.74–0.78 of the mean) almost disappears (0.91–0.99).

**Why it might matter.** The part of R(p) that fluctuates wildly is exactly the part a Linnik/BV dispersion argument
*can* handle on average (Σ_p τ-type(p+1) is the Titchmarsh divisor problem, solved by BV/BFI with fixed residue
a = −1); the interior is nearly Poisson but has tied residues. A lower-tail heuristic should model R = E(p) + (interior),
with E controlled by the divisor structure of p + 1 and the interior close to Poisson with index ≈ 1.4–1.9.

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
* **Not closed:** 3^k − 2 (all k ≢ 1 mod 240 covered by 12 words; residual k ≡ 1), 5·3^k + 1 (residual k ≡ 1, 2 mod 48),
  3^k − 1 (residual k ≡ 1 mod 48), 3^k + 1 (residual k ≡ 1, 2, 3, 15, 22 mod 60), 5^k ± 1 (not covered at B = 3000).

**The residual classes are neighbourhoods of tiny I3 zeros.** Their profinite limit point is (n_{k₀} at every prime ≠ 3,
d at 3) with n_{k₀} ∈ {1, 2, 4, 10, 16, 46} an I3 zero (3^1 − 2, 3^1 − 1, 3^1 + 1, 3^2 + 1, 5·3 + 1, 5·9 + 1). No E- or L-word
with modulus ≤ 3·10⁶ contains any of these six points (`scripts/z52d_p2_ZF1_Z2776_point.c`,
`limit_points_M3e6.txt`; positive controls (83, 2), (11, 2) found at m = 129, 21; the point (28, 1) of 3^k + 1 is covered at
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
