# Z53_PZ — R(p) ≫ log²p for almost all primes (wave z53b, side target Z2362)

**ES is open. Nothing here proves or disproves ES at any prescribed prime.** Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal review only. Scripts `scripts/z53_pz_*`, data `data/z53/pz/`.

*Status: CHECKPOINT 1 (skeleton). Sections marked TODO are in progress.*

## 0. Statement attacked

R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1). Pair form at a prime p:
R(p) = #{(u,B) : gcd(u,B) = 1, u+B odd, p ≡ −(u+B) (mod 4uB), 4uB − u − B ≤ p}.

**Target (Z2362, as briefed).** There is c > 0 with R(p) ≥ c log²p for a positive proportion of primes p ≤ X.

**What we actually aim at (stronger, a concentration statement).**
*Theorem A (target).* For every fixed ε > 0,
  #{p ≤ X prime : R(p) < (κ − ε)(log p)²} = o(π(X)),  κ = 9/(32π²) ≈ 0.0285,
(κ = 3/(32π²) from the pair fibration alone; ×3 using the two trial fibrations). Planned label: PROVED rel.
Bombieri–Vinogradov. (Mean: R ≈ (3/(2π²)) log²p ≈ 0.152 log²p, so κ is 3/16 of the mean.)

Literature (research subagent, verified from source text): the best known almost-all-primes lower bound is
Elsholtz–Tao Thm 1.8: f(p) ≫ (log p)^{(log 3)/2 − o(1)} ≈ (log p)^{0.549} on a relative-density-1 set of primes;
ET Remark 1.3: controlling Σ f_II(p)² "seems … out of reach of our methods, as the level of the relevant divisor sums
becomes too great". Elsholtz–Planitzer (arXiv:1805.02945) Thm 3: f(n) ≥ (log n)^{log 6+o(1)} for density-1 *integers*
only. So Theorem A, if correct, gives the right order log²p for almost all primes (f(p) ≥ R(p)).

## 1. Why this is not closed

The closed list concerns *pointwise* (fixed p) mechanisms. Theorem A is an averaged statement (B6 applies: it says
nothing about a prescribed p). It escapes ET's "level too great" obstruction because only a *lower* bound is needed:
R(p) ≥ N_Q(p), the count truncated to moduli ≤ Q = X^{1/4−ε}; then all pair correlations live at level
lcm ≤ Q² ≤ X^{1/2−2ε}, inside Bombieri–Vinogradov. Nothing about the large-moduli tail is needed.

## 2. First lemma (character form of the variance) — PROVED (elementary)

Let 𝒫 be a finite family of pairs P = (q_P, a_P), gcd(a_P, q_P) = 1, q_P ≤ Q, and N(p) = Σ_P 1[p ≡ a_P (q_P)].
For a primitive character ψ of conductor d put S_ψ = Σ_{P : d | q_P} ψ̄(a_P)/φ(q_P). Then
  Σ_{P,P'} φ(g_{PP'}) 1[a_P ≡ a_{P'} (mod g_{PP'})] / (φ(q_P) φ(q_{P'})) = Σ_ψ |S_ψ|²,  g = gcd(q_P, q_{P'}),
and the left side is (up to the BV error) Σ_{p≤X} N(p)²/π(X), since #{p ≤ X : p ≡ a (q), p ≡ a' (q')} =
1[compatible]·π(X)/φ(lcm) + error, φ(lcm)φ(gcd) = φ(q)φ(q'). The ψ = 1 term is M² (M = Σ 1/φ(q_P)); hence
  Var := (1/π(X)) Σ_{p≤X} (N(p) − M)² = V + o(1)·(BV error),  V := Σ_{ψ ≠ 1} |S_ψ|².
*Proof.* φ(g)1[a ≡ a' (g)] = Σ_{χ mod g} χ(a)χ̄(a') = Σ_{d | g} Σ*_{ψ mod d} ψ(a)ψ̄(a'); swap sums. ∎

**Key lemma needed (TODO, §3):** V = o(M²) for the truncated family — expected V ≪ L³ against M² ≍ L⁴.

## 3. Proof of Theorem A — TODO

## 4. Falsifier / numerics — TODO
Planned: exact sieve count of N_Q(p) on prime windows; empirical Var/M² vs Q must decrease (≈ 1/log Q);
compare with V computed from the character side.
