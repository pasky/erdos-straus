# AGENT_REPORT_O259 — spark relay on the b = 1 line (checkpoint 1)

Branch side-agent/b1-line (merged side-agent/synthesis-eight first). Main file **B1_LINE.md**. Memos BRAINSTORM/z29_*.md (6,
indexed in README). Scripts: z29_census.c (segmented census, mutual-shift form, `Z29_LINE=2` for (★), `countlist` exact
counts), z29_smooth.c (smooth p − 1 to 10¹⁵, Pollard–Brent), z29_genus.py, z29_freeze_check.py, z29_model.py, z29_samples.py.
Logs logs/z29_* (tiny). Literature: sources/lit2026f/ (López excerpts, SUMMARY.md). **ES is not solved; no infinite case claimed.**

SHARP:
1. **Census: no b = 1 failure in (66529, 10¹¹]** (all 2 059 020 280 primes p ≡ 1 (4) ≤ 10¹¹, complete decisions, independent
   algorithm from O258's). None among the 216 882 primes ≤ 10¹⁵ with 19-smooth p − 1 either (least shift ≤ 95 there).
   **(★) = c = 1 line: exactly the 14 known failures ≤ 10¹⁰** (new range (10⁸, 10¹⁰]).
2. **Prop 4.1 (PROVED) + Thm 4.2 (CONDITIONAL on Dickson):** if M_σ | p − 1, every shift s ≤ σ is frozen. Q_s = (p + s)/(1 + s)
   ≡ 1 (mod s), all small pairs are dead, and the shift-s pairs are the divisors t ≡ −1 (mod s) of (1 + s)Q_s, so Q_s prime
   kills the shift. The forms 1 + M_σk, 1 + (M_σ/(1+s))k are admissible (all = 1 at k = 0), so under Dickson the least shift
   is unbounded. This is the exact mechanism behind "the three failures have 11-smooth p − 1". The construction cannot reach
   the full line (≍ √p shifts).
3. **Why b = 1 ≫ (★) (PROVED main terms):** the incidence main term is (log p)²/8 for both, but (★)'s incidences pair up under
   (u, B) ↔ (B, u) (same solution). So b = 1 has twice the distinct trials, and half the exposed classes (p ≡ 1 (24) vs
   p ≡ 1 (8), Prop 1.4). The ratio N₁/N_{c1} is 1.67 → 1.85 over 10⁶–10¹² (→ 2). Mundane, but it closes O258 spark 1.

## Prior art (re-scoped as instructed)
López, arXiv:2206.10319 and 2404.01508: Type A = the b = 1 line; Thm 7 = the divisor form; Type B = (★); Conjecture 1 =
the union; 193, 2521 (≤ 9000) and 66529 are named as Type A failures. Verified quotes are in
sources/lit2026f/Lopez-2024-TypeB-Thm7.md and Lopez-2022.md. Gardes' thesis is per R268 (not re-verified). Potentially new
here: the census beyond 10⁸, Prop 4.1/Thm 4.2, the pair genus law in pair form, Lemma 3.1's swap count, the NB model.

## Results by goal
1. Literature: above (memo z29_lopez_typeA).
2. Census: B1_LINE §2. Engine: s t | p + s + t with 4 | st, min ≤ 1 + √(p + 1) (Lemma 1.1). Cross-checks: exact counts equal
   O258's brute force for all p < 400; ≤ 10⁸ reproduces 193/2521/66529 and the 14 (★) failures; prime totals match
   π(10¹⁰; 4, 1) by an independent sieve (π(10¹¹; 4, 1) matched against the known value only, from memory). Least-shift
   record 215 (p = 22 010 483 881).
3. Heuristic: B1_LINE §3. Mean (log p)²/8 with a −0.3 log p correction. Overdispersion D = 2–3.6, with the relative
   spread shrinking. NB back-test ≤ 10⁶ is ~2× optimistic in the tail (both lines). Out-of-sample on (★) in (10⁸, 10¹⁰]:
   1.7 predicted, 0 observed, so it is not optimistic at large p. Prediction: < 10⁻⁴ b = 1 failures beyond 10⁸, < 10⁻⁵ beyond
   10¹¹ even treating every prime as hardest-class. **Conjecture 3.5: exactly three failures** (CONJECTURE).
4. Structure: Lemma 1.2 pair genus law (ST/p) = −1, (S′T/p) = −(2/p)^k (PROVED; also for (★) incl. v₂(x) = 1). Its 2-adic
   escape was first read as a b = 1 advantage and then refuted: it is shared with (★) and acts only on trivial classes
   (Prop 1.4). Prop 4.1 / Thm 4.2 as above. Smooth classes depress the mean by 20 % (M₁₁) for both lines (§3.2).
   Astra relation: NOT done (the (J)81 lattice is the Type I slice world ρ² ≡ −p (g); no exact b = 1 dictionary found).
5. Forcing: §5 (PROVED negative). χ₋₄(p + 4d) = +1 always, so no level is forced by characters. Level d needs a prime
   ≡ 3 (4) in p + 4d (Landau event). Pure B2.

## Labels / caveats for the reviewer
* Thm 4.2 is CONDITIONAL (Dickson). The "infinitely many p with p + 4d a sum of two coprime squares" remark in §5/memo is an
  Assessment (expected from Iwaniec's half-dimensional sieve; primitive version not checked in the literature).
* The NB model is a heuristic calibrated on ≤ 10¹⁰. Conjecture 3.5 is not evidence for ES beyond what the census gives.
* Census figures rely on z29_census.c (please re-run, e.g. ≤ 10⁹ in seconds). The 10¹¹ run took ≈ 2 × 55 CPU-min.

## Sparks (not pursued)
1. An exact (J)81-style dictionary between b = 1 pairs and Astra source lattices: is "Type A fails" ⟺ "no Astra source is
   genuine on any slice"? 193 and 2521 are hard in both worlds.
2. The "middle region": Dickson-type constructions kill bounded shifts or bounded c, but pairs with s, c both ≍ p^{1/3} are
   out of reach of any fixed-form construction. Is there a proved lower bound for the number of b = 1 pairs in that region on
   average, with a variance bound strong enough for an almost-all statement with explicit exceptional-set size?
3. The (★) least-shift record 343 vs b = 1's 215: a joint Dickson construction for both lines at once (needs M_σ | p − 1 and
   prime cofactors for both shift families). Does the union of the two lines have a provably bounded "least shift" under
   any hypothesis? (Thm 4.2's forms kill both lines' small shifts simultaneously? Unchecked.)
