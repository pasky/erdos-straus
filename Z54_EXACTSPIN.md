# Z54_EXACTSPIN — spins, Kummer and Rédei symbols over the free variable w in the exact class layer T_uw

Status: z54 depth lane EXACTSPIN (gap 2, algebraic angle). Internal; internally reviewed only (review log §9).
**ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z54_exactspin_*`, data `data/z54/exactspin/`.
Builds on `Z53_GENUSX.md` (notation, Thm X, Lemmas 1, 2, 4.1–4.6) and `Z53_GENUSLVAL.md` (Thm U).

## 0. Checkpoint log
* cp1: precise statement (§1), why not closed (§2), first lemmas (§3: spin split S₂ + S_odd, T1 localisation, order-k
  layers), first falsifier (§6: 9 500 primes 10⁹–10¹², controls).

## 1. Setting and the precise statement attacked

Notation of `Z53_GENUSX` §1: p ≡ 1 (4) prime; Thm U family 𝔉 = {(u, w)}: u ∈ 𝒰 (squarefree, u ≡ 1 (4), U₀ < u ≤ U₁),
w ∈ 𝒮_u ∩ (Y, X] (odd squarefree, gcd(w, up) = 1), γ < 1 − α₁. Shell 𝔖 = {(u, w) ∈ 𝔉 : w | p + u}; on 𝔖,
w″ := (p + u)/(2w) is odd and prime to u. Put, at a shell point,
  G_u := (ℤ/u)^× = A₂ × A_o (2-Sylow × odd part),  x := −w″ mod u ∈ G_u.
Then (GENUSX §1, level form) A_u(w) = 1[w″ ≡ 3 (4)]·1[x = 1], A_u^gen(w) = 1[w″ ≡ 3 (4)]·1[x ∈ G_u²]/|G_u²|, and
  R_𝔉 − G_𝔉 = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·(1[x = 1] − 1[x ∈ G²]/|G²|) = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·φ(u)⁻¹ Σ_{ψ mod u, ψ² ≠ 1} ψ(x).
With T_u = O(p^{−δ} log p) on Theorem X windows (GENUSX Thm X), T_uw = R_𝔉 − G_𝔉 − T_u, so T_uw and R_𝔉 − G_𝔉 differ
by o(1) there; below "the exact class layer" means R_𝔉 − G_𝔉.

**Spin layers.** For k ≥ 3 the *exact-order-k layer* and the *2-adic / odd spin layers* are
  Δ_k := 2 Σ_{𝔖} 1[w″≡3(4)] φ(u)⁻¹ Σ_{ψ mod u, ord ψ = k} ψ(x),
  S₂ := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x₂ = 1] − 1[x ∈ G²]/|A₂²|)·1[x_o = 1],
  S_o := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x ∈ G²]/|A₂²|)·(1[x_o = 1] − 1/|A_o|),
(x = x₂x_o the A₂ × A_o decomposition). S₂ is governed by the characters of 2-power order ≥ 4 (quartic, octic, … —
Rédei/governing-field data), S_o by the odd-order characters (cubic, quintic, … — Eisenstein/Kummer data).

**Statement attacked (the brief's question, made precise).**
(Q1) *Identification.* Can Δ_k, S₂, S_o (or a sub-piece) be written as Σ over the free variable w (or w″, or u) of a
spin / Kummer / Rédei symbol attached to a field depending only on p (or on p and u ≤ p^{α₁})?
(Q2) *Cancellation.* If so, does a FIMR / Koymans–Milovic-type theorem (cancellation of such a symbol over a free variable,
p fixed) apply, i.e. can one prove for some window family with M_𝔉 ≫ log²p
  (Sp-k) Δ_k = o(log²p) for fixed k;  (Sp-2) S₂ = o(log²p);  (Sp-o) S_o = o(log²p)?
Since R_𝔉 − G_𝔉 = S₂ + S_o (Lemma 3.1), (Sp-2) + (Sp-o) + (X-w) [T_w = o(log²p)] on a Theorem X window with Thm U's (C3)
would give R_𝔉 ≥ (c − o(1))log²p, hence (★) and ES(p) for all large p. So (Sp-2) + (Sp-o) is ES-(★) strength
(CONJECTURE-strength target, not claimed). (Sp-k) for fixed k is much weaker (Lemma 3.4).

## 2. Why this is not already closed
* GENUSX treats the exact layers only through order-agnostic structure (Lemma 4.1 injectivity, Lemma 4.3 diagonal
  Cauchy–Schwarz, Prop 4.6 interval data on χ_p for the BM *genus* component); its Remark 4.7 concerns *density-level*
  bounded-order w-side layers. The u-side order filtration of R − G over exact divisors was only measured (ladder G^{(K)}).
* CLASS_FORCING Thm 2.1 / GENUSREDEI JRT, Cor F are *forcing* statements (what holds at every prime with a given Frobenius
  datum); they say nothing about cancellation of a symbol *summed over a free variable at fixed p*. GENUSREDEI §7.4 and
  `BRAINSTORM/bsB_redei_oddpart.md` dismissed spins as "averages over the prime (B6)"; but in Lemma 4.1 form the free
  variable is w, not p, so that dismissal does not apply as stated. FIMR/Koymans–Milovic were never matched against the
  exact layer.
* FRONTIER §4 item 9 ("reciprocity forces parity, never class") is a forcing statement; equidistribution (cancellation)
  of higher symbols over a free variable is not excluded by it.

## 3. First lemmas (PROVED)

**Lemma 3.1 (2-adic / odd split; T1 localisation).** R_𝔉 − G_𝔉 = S₂ + S_o identically, and both summands vanish at
every shell point with x ∉ G_u². In particular at an odd square n = m² (where G_𝔉(m²) = 0, so no shell point with
w″ ≡ 3 (4) has x ∈ G²; GENUSX §5 CERTIFIED and Thm U §2.8) S₂ = S_o = 0 *pointwise*.
*Proof.* G² = A₂² × A_o (A_o has odd order, so A_o² = A_o), |G²| = |A₂²||A_o|; 1[x = 1] = 1[x₂ = 1]1[x_o = 1];
x₂ = 1 ⇒ x ∈ G². So 1[x=1] − 1[x∈G²]/|G²| = (1[x₂=1] − 1[x∈G²]/|A₂²|)1[x_o=1] + (1[x∈G²]/|A₂²|)(1[x_o=1] − 1/|A_o|), and
both terms vanish if x ∉ G². At n = m² the genus layer G is a sum of non-negative terms with value 0. ∎

**Lemma 3.2 (order-k layers and squares).** For every k ≥ 3 and x ∈ G_u,
  Σ_{ord ψ = k} ψ(x) = Σ_{d | k} μ(k/d)·|G/G^d|·1[x ∈ G^d],  |G/G^d| = ∏_{ℓ|u} gcd(d, ℓ − 1).
If 4 | k this vanishes for every x ∉ G² (hence Δ_k(m²) = 0 pointwise at odd squares); if 4 ∤ k it need not.
*Proof.* Σ_{ψ^d = 1} ψ(x) = |G/G^d|·1[x ∈ G^d] (characters of G/G^d), then Möbius inversion over the order. If 4 | k
and μ(k/d) ≠ 0 then k/d is squarefree, so 2 | d and x ∉ G² ⇒ x ∉ G^d. For 4 ∤ k see §6 (Δ₃, Δ₅, Δ₆ ≠ 0 at squares). ∎
*Reading.* Odd-order spin layers (and k ≡ 2 (4)) are T1-blind: a cancellation theorem for them holds or fails
regardless of whether n is a square; the square-sensitive step must stay in the 2-adic genus (Thm U's step).

(Lemmas 3.3–3.4 and the spin dictionary: §4.)

## 6. Falsifier F (EVIDENCE; identities CERTIFIED) — first run

Engine `scripts/z54_exactspin_engine.c` (shell enumeration as GENUSX; per shell point it computes R, G, S₂, S_o, Δ_k for
k ∈ {3,…,13,16,20,24} by Lemma 3.2, and uniform-class model variances); driver `scripts/z54_exactspin_run.py`; samples
`scripts/z54_exactspin_samples.py` (seed 5400); summary `scripts/z54_exactspin_stats.py` → `stats.txt`. Standard
GENUSX window (U₀, U₁, Y, X) = (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4) (proxy window, outside Thm X).
(results to be filled in at cp2)
