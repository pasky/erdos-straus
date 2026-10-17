# Brief for Astra — Direction 2 (actual-exception propagation / recombination law)

*Prepared 2026-10-15 by the Claude campaign (`erdos-straus-claude`) at the user's request, for hand delivery by the user. ES is unsolved. This brief is a parallel-comparison exercise: the same SHARED CORE below is being given, verbatim, to one Claude author stream (task O253) with the same budget. Neither side sees the other's output on this problem until both have reported.*

## Suggested framing for Astra

* **Freeze Direction 1 fixture repairs for this pass.** The square-removal fixtures (193, 3361, 5209, 2521, 233689, the 24→7→2→1 and 7→45360→3→1 chains, etc.) stay as they are at `d7300f8`. Claude's `ASTRA_BRIDGE.md` ((J)81) gives a dictionary in which every square-removal gate is a "divisor in a moving residue class" event; further per-fixture repairs are unlikely to change the global status, so this pass spends the whole budget on Direction 2.
* **Your own terms apply.** In your vocabulary, the target is a *universal recombination law* (route (D) of the core: total maps from witness tuples W(q_i), q_i < p, into W(p), e.g. your least-counterexample opportunity with the prime factors of u = (p−1)/2, v = (p+1)/2), or an *amplification law* (route (A): W(p₀) = ∅ forcing W(q) = ∅ on a large explicit family of q). Your existing partial maps (W(625)→W(1249) on p = 2·5^m − 1, the 31249 repair, the W(5)→W(19) packet move, canonical exit contracts, height bounds H ≤ q³ and H ≤ 4(q+1)/3) are prior art; the core's Deliverable 1 asks for the exact "this would suffice" theorem you sketched in `POSITIVE_ES_RESEARCH_RESET.md` §4 (tests 1–3), now proved with quantifiers.
* **Starting points in Astra's tree:** `POSITIVE_ES_RESEARCH_RESET.md` §4, `POSITIVE_ES_CAMPAIGN.md` (Direction 2 table), `EXCEPTION_PROPAGATION_{OPERATIONS,STRUCTURAL,GLOBAL}.md`, `EXCEPTION_{ANCHOR_SUPPLY,PACKET_REPAIR,CANONICAL_EXIT,LINEAR_FACTOR_DESCENT,TWIST_ASSISTED,TWIST_FORCING,REPAIR_NORMALIZATION}.md`.

## Claude files you may read (read-only reference; path `/home/pasky/projects/math/erdos-straus-claude`, branch `main`)

Your last read of the Claude tree was at `53204707`; wave Z and later ((J)57–(J)83 in `DISCOVERIES.md`) are new to you. Most relevant:

* `ASTRA_BRIDGE.md` — (J)81: square removal and Claude's exponent cap are one lattice L_ρ(g) = {Y ≡ ρM (mod g)} at a slice g ≡ 3 (4) with ρ² ≡ −p; your sources are the points (m, 1), Claude's shots are (2k, Y) with k | h = (g+1)/4; ES solutions are the intersections; every gate is a divisor-in-moving-class event.
* `LATTICE_MEETING.md` — (J)82: class-group walks propagate ES only *downward*; 3361 has no Type II solution on any slice lattice.
* `CAP_POINTWISE.md`, `CAP_DOWN.md`, `CAP_BOUNDED.md` — (J)64/(J)66/(J)83: windows q ≡ 4 − n (mod 8) with (q/n) = −1, K = (n+q)/4, reciprocity forces −1 ∈ ⟨primes of K⟩ mod q; cap e*(n); bounded windows fail (conditionally on Dickson).
* `MENU_STERILITY.md`, `MENU_LADDER.md` — (J)76: positive-density menus collapse to finite coverings / divisor events; sterile profinite points.
* `EXP_OPEN.md` (Theorem W), `EXP_105.md` — exponential families (3·2^s+1, 63·2^s+1, 4^s+105, …) closed by forced algebraic budgets beyond every congruence covering.
* `EXCEPTIONAL_KARY3.md`, `paper/es-threequarter-note.tex`, `paper/vaughan-loglog-note.tex` — exceptional-set bounds (internal 3/4 exponent; limits of CRT methods at 3/4).
* `STATUS.md` (entry point), `DISCOVERIES.md` (ledger with labels).

**Fairness pin.** Please read the Claude tree only as of commit `a678d18b` (e.g. `git -C /home/pasky/projects/math/erdos-straus-claude show a678d18b:ASTRA_BRIDGE.md`); later commits may contain the Claude-side answer to this same problem (task O253, files `AMPLIFY_EXCEPTION.md`, `BRAINSTORM/z25_*`), which you should not see until both sides have reported.

## What to send back (via the user)

A report following §7 of the shared core (rows R1–R8), plus pointers to your files and commits. Please keep it in your own tree.

=== BEGIN SHARED CORE PROBLEM — "Direction 2: amplifying one exception" (core v1.1, 2026-10-17) ===

This core is given verbatim to two independent research teams. Neither team sees the other's output on this problem until both have reported.

0. STATUS. The Erdős–Straus conjecture (ES) is OPEN. Nothing below asserts otherwise. No ES-free prime is known; ES has been verified computationally far beyond any range relevant here (published: n ≤ 10^17, Salez 2014).

1. DEFINITIONS.
 * W(n) = set of all positive integer triples (x, y, z) with 4/n = 1/x + 1/y + 1/z.  S = {n ≥ 2 : W(n) ≠ ∅}.  E = {n ≥ 2 : W(n) = ∅} (exceptional integers).  P_E = E ∩ primes (exceptional primes).
 * Divisor closure: if d | n and d ∈ S then n ∈ S (scale). Hence every n ∈ E has every divisor ≥ 2 in E, the least element of E is a prime, and P_E ⊆ {p ≡ 1, 121, 169, 289, 361, 529 (mod 840)} (Mordell).
 * Prime parametrisation (complete at odd primes q, after permuting coordinates): positive integers a, b, c, d with c | a + b, e = (a+b)/c, H = 4ab, and
     Type I :  H d = q e + 1,   (x, y, z) = (q a b d, a c d, b c d);
     Type II:  H d = q + e,     (x, y, z) = (a b d, q a c d, q b c d).
 * Known witness transports (witness-dependent modulus H): a witness at q gives one at p with the same (a, b, c) if H | q − p (same Type) or H | pq − 1 (Type switched).
 * Exceptional-set bounds. PUBLISHED (Vaughan 1970): #{n ≤ N : n ∈ E} ≪ N exp(−c (log N)^{2/3}) for some c > 0. INTERNAL (Claude campaign, internally reviewed, unpublished — may be used but must be flagged when used): N exp(−c (log N)^{3/4}). Either implies Σ_{p ∈ P_E} 1/p < ∞.

2. THE PROBLEM. Find an AMPLIFICATION / PROPAGATION LAW: a theorem of the form
     "p₀ ∈ P_E  ⟹  F(p₀) ⊆ E"          (or: ⟹ at least one member of each block of F(p₀) lies in E),
   where F(p₀) is an explicit (or explicitly bounded) set of integers or primes, strong enough that the existence of a single exceptional prime contradicts known facts. Two routes count:
   (D) DESCENT / RECOMBINATION: for every prime p ≥ 5 (in the Mordell classes suffices) an explicit finite set Q(p) of integers in [2, p) such that [W(q) ≠ ∅ for all q ∈ Q(p)] ⟹ W(p) ≠ ∅, proved for EVERY witness choice at the q's (a "total" recombination map), or with a proof that a favourable witness always exists. By strong induction this proves ES. (Example of the shape: Q(p) = prime factors of (p²−1)/4.)
   (A) AMPLIFICATION: the family F(p₀) generated from one exception (possibly iterated) is large enough to contradict an exceptional-set upper bound or the convergence Σ_{P_E} 1/p < ∞.

3. REQUIRED DELIVERABLE 1 — the "this would suffice" theorem (prove it, with exact quantifiers). State and PROVE the sharpest available criterion of the form: "if every p₀ ∈ P_E generates a set F(p₀) ⊆ E (or ⊆ P_E) with property X, then P_E = ∅". It must at least treat:
   (i) counting growth: what lower bound on #(F(p₀) ∩ [1, N]) (along all N, or along a sequence N → ∞) contradicts the published bound, and what contradicts the internal 3/4 bound; careful with the unspecified constant c;
   (ii) iterated laws: a branching map p ↦ {p₁, …, p_b} with successors in a size range p^{μ} ≤ p_i ≤ p^{λ} (or p < p_i ≤ p + f(p)); for which (b, μ, λ, f) does iteration from one seed contradict the bounds or Σ 1/p < ∞ (note: fixed b with every successor ≥ p^{μ}, μ > 1, gives only polylog(N) descendants below N — show what replaces this, e.g. slowly growing successors or growing b);
   (iii) composite outputs: F(p₀) may contain composites; quantify how the divisor-closure of E (every exceptional integer's prime factors are exceptional, and a product of exceptional primes need NOT be exceptional) affects the count, and how a set of exceptional composites converts into a bound on P_E;
   (iv) the "at least one of each block" (disjunctive) variant.
   A precise negative statement (e.g. "no law whose outputs are all ≥ p₀^{1+ε} with bounded branching can ever suffice") counts as part of Deliverable 1.

4. REQUIRED DELIVERABLE 2 — construction attempt. Try hard to construct a propagation law satisfying the criterion, or a strictly weaker but genuinely new one. Required check for any proposed law: supply the actual map / witness-lifting identity; prove it is TOTAL (works for every witness, both Types), or prove the favourable-witness existence; verify that outputs are actual elements of E under the hypothesis (not just empty parametrised slices, not just "the transport fails"); then compute its growth against Deliverable 1. Test every proposed law exactly on the fixtures p ∈ {97, 193, 313, 3361, 5209, 233689} (all soluble — a law of the form "p₀ ∈ E ⟹ q ∈ E" is tested contrapositively: "q ∈ S ⟹ p₀ ∈ S" must hold with an explicit witness), on all primes p ≤ 10^5 in the Mordell classes, and on odd squares n = m² as a negative control where relevant (odd squares are ES-soluble but have NO Type I or Type II solutions in the Elsholtz–Tao sense, ET Prop 1.6; a Type-I/II-based argument all of whose steps remain valid at n = m² proves too much).

5. SUCCESS TIERS (to be reported honestly; labels PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment).
   * FULL: route (D) or (A) proved unconditionally ⟹ ES. Must survive two independent hostile reviews before being called a proof.
   * STRONG PARTIAL: one of — (a) ES ⟸ [propagation law proved here] + [a named, standard, believable hypothesis] (state the hypothesis precisely, say why it is not ES in disguise); (b) a total propagation law valid for every p₀ in an explicit infinite set (congruence / Chebotarev / exponential family) with a proved growth statement; (c) a total recombination law for every p outside an explicit thin set; (d) a new sharp Deliverable-1 theorem plus a proved obstruction theorem with exact scope showing that an entire natural class of laws (name the class: fixed-modulus transports, polynomial maps, multiplicative maps, bounded-branching maps, …) can never suffice.
   * WEAK PARTIAL: new exact transports or repairs on fixtures; numerics; a well-posed reduction to an open problem.
   * NOT SUCCESS: maps total only into already-known-soluble targets; fixed soluble labels; classical Type-I/II congruence progressions relabelled as propagation; witness-specific transports presented as total; harmonic-mass statements without an actual law.

6. BUDGET (both teams the same). One author stream (one sustained session, with commits), plus independent hostile review(s) of its claims and at most two repair rounds. At most 2 CPU cores for computation and ≤ 12 CPU-hours in total. Stop and report at the first natural checkpoint after roughly one working session, even if unfinished.

7. FINAL REPORT FORMAT (for side-by-side comparison; keep to ≤ 2 pages, fill every row):
   R1. Deliverable 1 — the sharpest "this would suffice" theorem: exact statement; label; proof location.
   R2. Best propagation / recombination law obtained: exact statement; scope (which p₀, which witnesses, which Types); label; is it total?
   R3. Its growth vs. R1: how far short (quantitatively) of sufficing.
   R4. Strongest obstruction theorem proved (exact scope).
   R5. Fixture table: for each fixture p ∈ {97, 193, 313, 3361, 5209, 233689}, what the best law does there.
   R6. Key new idea(s) in one paragraph each; what was tried and abandoned (one line each).
   R7. Honest distance-to-ES assessment (one paragraph), and the single most promising next step.
   R8. Resources used: wall-clock, CPU-hours, number of sessions, review verdicts.

=== END SHARED CORE PROBLEM ===
