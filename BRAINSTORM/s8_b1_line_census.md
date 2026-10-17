# s8_b1_line_census — the b = 1 line fails at exactly 193, 2521, 66529 below 10⁸ (O258; §2) — SHARP

**Idea.** The support-1 lottery of z24 (s | jp + 1, s ≡ 3j − 1 (4j)) is the b = 1 line with a prime. Drop primality and
dualise (Prop 1.3): b = 1 ⟺ ∃ d: p + 4d has a divisor ≡ −1 (mod 4d). How often does this ONE shift family fail?
**Literature.** (J)6 (★) (= c = 1 line); PARITY_AUDIT census; FORCED_WINDOW §6, z24_budget_not_mechanism.
**Barrier screen.** T1: fails at all odd squares (checked to 529). It also fails at 105, so primality must be used
(s7_typeII_free_controls). The numerator-8 analogue fails at 60 primes < 8000 (both k = 8 lines together at 34, incl. 131, 241),
so any mechanism must be 4-specific. Being a subfamily, it inherits B2/B3: CONJECTURE only.
**Cheap numerics.** `s8_lines census 1e6`, `census2` to 10⁸ (complete window decisions); independent brute force
`s8_check_b1.py` at the failures. b = 1 failures ≤ 10⁸: {193, 2521, 66529}. c = 1 failures: 14 ≤ 10⁷, none in (10⁷, 10⁸].
b = 1 ∪ c = 1: no failure ≤ 10⁸. Support-1 with prime s: 752 failures ≤ 10⁶.
**Assessment.** EVIDENCE + CONJECTURE 2.5. SHARP flag: a single shift family {p + 4d} carries ES at every prime
p ≡ 1 (4) ≤ 10⁸ except three.
