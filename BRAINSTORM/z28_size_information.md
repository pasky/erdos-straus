# z28_size_information — do the sizes of a source solution know anything about p? (O257; NONCONG_LIFTS §4.2)

**Idea.** Witness-level lifts read sizes (d′, c′d′, x′) of the source solution. If sizes carried information about p's
divisor events, a size-reading lift would beat a random integer of the same size.
**Test.** Permutation-style: event "p has a witness with D | abd" for D from profile-matched sources vs D from
unmatched sources in the same window (same sizes) vs D from another target's sources.
**Result (EVIDENCE).** 83 Mordell primes 100 < p ≤ 3·10⁴: d′ 64.6% vs 69.6% (unmatched) vs 67.7% (shuffled); c′d′ 51.6% vs
50.4% vs 54.0%; a′b′d′ 4.4% vs 3.9% (shuffled 11.7%: size confound). No information beyond size.
**Literature.** s7_window_lottery (shuffle test: congruence data explain all inter-window correlation) — same verdict
in another coordinate system.
**Barrier screen.** B2 in its purest form: the source's factorisation is independent of p's divisor events. B3/B6 n/a.
**Cheap numerics.** `scripts/z28_size_info.py` (≈ 20 min, 1 core).
**Assessment.** EVIDENCE (negative). The natural non-congruential lifts carry no detectable signal.
