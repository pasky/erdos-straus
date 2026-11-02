# Z54_EXACTSUM — the exact-divisor layer R − G on the Thm U family, exponential-sum angle

Status: z54 depth lane EXACTSUM (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z54_lanes.md` § EXACTSUM).
Internal, internally reviewed only. **ES is OPEN; nothing here proves or disproves ES or (★) at any infinite set of
primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z54_exactsum_*`, data `data/z54/exactsum/`. Builds on `Z53_GENUSX.md` (cited **GX**: §1, Lemma 1, Thm X,
Lemma 4.1) and `Z53_GENUSLVAL.md` (cited **GL**: Thm U).

*(Checkpoint 1 skeleton — sections marked [TODO] are filled in later in the lane.)*

## 1. Setting and the precise statements attacked

Notation of GX §1: p ≡ 1 (4) prime; windows U_i = p^{α_i}, Y = p^β, X = p^γ; 𝒰 = {u squarefree, u ≡ 1 (4),
U₀ < u ≤ U₁}; 𝒮_u = {w odd squarefree, gcd(w, up) = 1}; shell 𝔖 = {(u, w) : u ∈ 𝒰, w ∈ 𝒮_u ∩ (Y, X], w | p + u};
on 𝔖, w″ = (p + u)/(2w) (odd) and k := 2w″ = ⌈p/w⌉. GX: R_𝔉 = 2#{𝔖 : w″ ≡ −1 (4u)},
G_𝔉 = Σ_𝔖 (2·2^{ω(u)}/φ(u))·1[w″ ≡ 3 (4), −w″ ∈ □ (mod u)], X_𝔉 = R_𝔉 − M_𝔉 = T_u + T_w + T_uw (GX Lemma 1),
R_𝔉 − G_𝔉 = T_u + T_uw, and on Theorem X windows T_u = O(p^{−δ} log p).

**Targets (CONJECTURE-strength; not claimed).**
* (X-uw) T_uw ≥ −(1 − ε)M_𝔉 + o(log²p) on some window family with M_𝔉 ≫ log²p (with (X-w) this gives (★), GX §1).
* (X-uw)₂ the two-sided |T_uw| = o(log²p) (the kickoff's "even |T_uw| = o(log²p) on SOME window family").

**What this lane attacks.** The kickoff's programme: (1) expand the class condition (r_w = u, ⌈p/w⌉ ≡ −2 (8u)) into
exponential sums over the free variables with phase p/w and frequencies h/(8u); (2) find the window/frequency ranges in
which those sums admit nontrivial bounds, and prove a theorem there or the exact scoped no-go (which exponent is
missing, by how much); (3) falsifier at 10⁹–10¹⁴.

## 2. Why this is not already closed
* GX controls only the density layer T_u (Thm X) and gives structure identities for the exact layers; it does not
  decompose them by frequency/conductor, and makes no window statement for exponential sums in w.
* Closed "low-conductor universality" (FRONTIER §7.1, smooth hyperbola blocks) is about the pair modulus m of smooth
  blocks; here the objects are the characters mod u of the level divisor on the exact shell of the Thm U family, and
  the question is which conductors exponential sums in p/w can reach *on windows where Theorem X and Theorem U also hold*
  — a window-compatibility question not addressed anywhere.
* HYPKLOOST Thm B (frequency certificates of degree < q_max/2 have mean ≤ 0) concerns positive-mean certificates for
  the full count; the present no-go (§5) concerns per-conductor bounds of the exact layer, a different class.

## 3. Exact frequency / conductor decomposition [TODO: PROVED identities]

## 4. Window reconciliation: what exponential sums in p/w can control [TODO]

## 5. Top conductor = single integers: scoped no-go [TODO]

## 6. Falsifier: conductor profile of R − G at 10⁹–10¹⁴ [TODO: first falsifier, running]
Plan: for each shell point compute the conductor-f components D_f (f | u, f > 1) of R − G,
  R − G = Σ_{f>1} D_f,  D_f = Σ_{𝔖: f | u} (2/φ(u))·1[w″ ≡ 3 (4)]·[∏_{ℓ|f}((ℓ−1)1[−w″ ≡ 1 (ℓ)] − 1) − (−w″/f)],
and measure, over random primes, near-squares, (★)-zero/test primes, odd squares and composites, where the variance of
R − G and the T1 cancellation sit (by f/u and by the number of integers p + u in each block). Kill criterion for the
exponential-sum route: if ≥ 90 % of var(R − G) sits in blocks containing O(1) integers p + u, exponential sums in w
(which need long blocks) cannot reach the variance-carrying part.

## 7. Screens, verdict, proposed FRONTIER text, bottom line [TODO]
