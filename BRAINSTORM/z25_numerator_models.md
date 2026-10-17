# z25 memo 3 — numerator models k/n give genuine exceptions; they are isolated (O253)

Verdict: STEERING TOOL (CERTIFIED computations, z25_models.py). Promise 2/5 as a test-bed.

* For k/n = 1/x + 1/y + 1/z, 8 ≤ k ≤ 25, prime exceptions exist (k = 8: 11, 17, 131, 241 below 2000; k = 12:
  13, 29, 31, 37, 73, 97, 193, 433, 577, 1129, …). Same ET parametrisation with 4 → k, same transports, same
  divisor closure. So every k-uniform law can be tested against real exceptions.
* Results: square law false (8/11 ∉ S, 8/121 ∈ S); prime-factor recombination of (p²−1)/4 false for all
  10 ≤ k ≤ 25 (e.g. k = 10, p = 61); {(p−1)/2, (p+1)/2} law false for 8 ≤ k ≤ 25 except k = 9; no exceptional
  successor of 241 in (241, 8·241] for k = 8.
* Lesson: exceptions in the models look finite and isolated — no amplification of any kind. An (A)-law must be
  4-specific (cf. numerator blindness (J)41) and must be false in every k-model with finitely many exceptions.
Next: compute E_k to 10^5 for k = 8, 12 to see whether exceptions die out (CONJECTURE: E_k finite for each k).
