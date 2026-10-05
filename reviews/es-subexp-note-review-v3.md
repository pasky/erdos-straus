# Referee report R47 — `paper/es-subexp-note.tex` v3 (exponent 1/5)

Referee: hostile side agent R47 (branch `side-agent/referee-subexp-v3`).
Author branch: `side-agent/subexp-paper-v3` @ 67cda1e (merged non-ff into referee branch; ff-only failed because main moved).

Status: IN PROGRESS.

## Summary verdicts per claim

(to be filled)

## Numbered defects

(to be filled)

## Checks performed

### Pass 1: §§1–2 (lines 1–425), §3 Lemmas 3.2–3.3 re-derived by hand
* Lemma 2.1 (atoms), 2.2 (class of one): re-derived; correct. (The phrase
  "Since 4A_M^2≡A_M" in the proof of 2.2 is not what is used — the involution
  preserves D≡−A_M because (−A_M)^2=A_M^2; harmless.)
* Lemma 2.4 (i)–(iii): re-derived; correct, incl. |Ω_ℓ|=ℓ^{f−a}, class size
  ℓ^{f−v}, gcd(M,Q)|g, ω(M)≤log M/log 3, (1+1/(𝓛−1))^𝓛≤e^{𝓛/(𝓛−1)}≤e² for 𝓛≥2.
* Lemma 2.5: termination, (a) via a_ℓ+1≤v_ℓ(M) on supports, (b), (c) step
  accounting (each (ℓ,a) once, sum over a<v_ℓ(M) of 1/(a+1) = H_v) re-derived;
  correct. Start cost: log 840+ϑ(𝓛)≤1.02𝓛+7 with ϑ(x)<1.01624x (RS) — fine.
* Lemma 3.2, 3.3 (parametrisation, injectivity, involution preserving g):
  re-derived; correct.
