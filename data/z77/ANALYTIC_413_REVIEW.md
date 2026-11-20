# Independent hostile review — Lane 3

`functions.review`, mode `smart`, base `7e39f7e7`, commit `0eb20fea`; tool-reported reviewer `anthropic/claude-opus-5-5`.

Verdict (quoted): “the §3 theorem holds up, and I found no mathematical error in any of the claims I checked. The main problems are form: §0 labels the whole result PROVED, but the dispersion clause is only an assessment.”

The reviewer rederived the conditional CRT densities, pinned-prime Euler factor, omission of 2 from the native sieve, boundary error, Markov argument and height threshold. The script replay was byte-identical. Independent spot check reported at D=105, Y=300: exact pair mean 14.503 (rounded), 4000-point sample mean 14.526. The reviewer checked the CRT reduction of imprimitive frequencies, Cauchy normalization, kernel deficit and all three vertex constraints; explicitly no proof of a large off-diagonal.

Disposition: §0 now labels only the short-height multiplicity theorem PROVED. §§1–2 mark dispersion/prime-saving assessments separately, credit the z76 diagonal observation, state the choice of P, and §3 distinguishes composite inputs at prime-case height from a prime-input result. Clarified the section-local variable conventions, added endpoint-pair source pointers and qualified replay scope. The suggested transfer-budget interpretation is not needed as an impossibility theorem for arbitrary moment methods: a large upper bound for transfer error does not prove a large error. No master-file edit requested within the lane.
