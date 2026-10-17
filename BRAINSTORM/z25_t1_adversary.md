# z25 memo 2 — the T1 adversary: invisible witnesses kill congruence-mediated recombination (O253)

Verdict: OBSTRUCTION, sharp (PROVED Thm 3.2 / Cor 3.3; CERTIFIED numerics). Promise 1/5 as a route, 3/5 as a tool.

* Lemma: if p ≡ □ (mod L) then p has no ET witness with modulus H | L (the class of p mod L contains an odd square,
  and ET Prop 1.6). Checked: no fixture's own ET modulus H has p ≡ □ (mod H).
* Any recombination/amplification step that uses an input witness only through the residue of p modulo the input
  modulus (a "determined lift") can use only inputs whose modulus contains a prime power at which p is a
  non-square. Inputs supported on primes ℓ with (p/ℓ) = 1 (and 2, 3, 5, 7 for p ∈ 𝓜) are invisible.
* Being a square mod L is local, so the lcm of invisible moduli is invisible: joint recombination over ANY finite
  set of sources that must accept every supplied witness tuple is total only if one source has no invisible
  witness (necessary only; favourable-witness proofs are not covered; joint lifts can beat single ones on visible
  inputs, e.g. p = 17 with moduli 8, 12). At all fixtures ≤ 5209 every source tried
  has ≥ 2 invisible witnesses; adversarial tuples exist (z25_joint_run.py).
* Dictionary: "usable information about p" = residues at non-residue primes of p. The only known pointwise
  positive mechanism ((J)64 self-generated mute) indeed starts from a prime window q with (q/n) = −1.
Spark: a law whose inputs are *forced* to carry a non-residue prime of p (e.g. sources q with (q/ℓ) = (p/ℓ) on all
ℓ ≤ B, so that q's own T1 constraint transfers) — visibility is necessary, not sufficient; the pass is still B2.
