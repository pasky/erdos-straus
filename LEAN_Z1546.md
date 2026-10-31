# LEAN_Z1546 — Lean formalisation: C-form ⟹ ES, and the square obstruction T1

Item Z1546 (`ES_CONNECTIONS_TODO.md:182`; from `BRAINSTORM/z52b_free_fable.md` item 236). **ES is OPEN; nothing here
proves it.** All Lean statements listed below are machine-checked (Lean 4 + mathlib), with no `sorry` and no axioms
beyond Lean's standard three. The brute-force count in finding 2 and the search cited in finding 3 are Python/repo
computations and are not formalised.

## Discrepancies / scope findings (read first)

**No discrepancy was found between the repo's statements and what Lean accepted.** Three scope findings:

1. **T1 for the C-form holds at *every* square, not just odd ones** (and also at m = 0). The BRAINSTORM item
   (`BRAINSTORM/z52b_free_fable.md:489`, "odd squares") understates it. `PARITY_AUDIT.md:214` (Lemma 3.2, R265 repair m5)
   and `FRONTIER.md:241` ("any square") already have it right. `CForm`, `cform_ES` and T1 carry no C ≥ 1 or n ≥ 1
   hypotheses. C ≥ 1 follows from `4C ∣ a + 1`, and n ≥ 1 follows from the complete certificate (`a ∣ 4Cn + 1` together
   with `4C ∣ a + 1`). `ESProp_iff_rat` and `cform_iff_shifted` do assume n > 0 explicitly.
2. **T1 for the Type I *divisor form* (`FRONTIER.md:44`, f ∣ n² + 4c²d, f ≡ −n (mod 4cd)) at n = m² needs gcd(f, m) = 1,
   even for odd m.** The counterexample m = 3, c = 1, d = 3, f = 3 (3 ∣ 93, 12 ∣ 3 + 9) is checked by `decide` in
   `ES/Axioms.lean`, as is m = 2, c = d = 1, f = 4. A Python brute force over 1 ≤ m < 40, 1 ≤ c < 30, 1 ≤ d < 60 (all
   divisors f of m⁴ + 4c²d) found 13375 distinct Type I divisor-form hits at squares, every one with gcd(f, m) > 1.
   The count was confirmed independently by the reviewer. The script is not committed and the count is not
   machine-checked. This does not contradict the repo, because FRONTIER states the
   divisor forms for primes p and the R290 repair (`FRONTIER.md:42`) already warns that composite n needs coprimality.
   Still, never apply the Type I divisor-form T1 at squares without gcd(f, m) = 1. The Type II divisor form needs no
   such hypothesis.
3. The optional reduction `ES_of_cform_primes` ("C-form at every prime p ≡ 1 (4) ⟹ ES") is formally correct, but
   **vacuous: its hypothesis is false.** `cform_C_bound` (proved) shows that a certificate needs 4C ≤ n + 2, so for
   each p the search is finite. That search, done exhaustively, finds no certificate for 409, 577 or 5569
   (`BRAINSTORM/z45_euler_systems.md:126,170–183`). The reviewer also re-exhausted the ranges for 409, 577, 5569 and 9601.
   The search itself is not formalised. The useful reduction is `ES_of_primes_one_mod_four`.

## Statements (Lean ↔ English), all PROVED

File: `lean/ES/ES/Basic.lean`. The paper proofs are in its module doc comment, written step by step in the order the Lean
proofs follow.

Definitions:
* `ESProp n := ∃ x y z : ℕ, 0<x ∧ 0<y ∧ 0<z ∧ 4*x*y*z = n*(x*y+y*z+z*x)`. `ErdosStraus := ∀ n ≥ 2, ESProp n` (stated only).
* `CForm n C a := a ∣ 4*C*n+1 ∧ 4*C ∣ a+1`. This is the repo's C-form (`BRAINSTORM/z52b_free_fable.md:67`: "4Cp + 1 = ab
  with a ≡ b ≡ −1 (mod 4C)", and item 152 at `:389`) in divisor form. `cofactor_dvd` proves that the cofactor b
  automatically satisfies b ≡ −1 (mod 4C), so the two forms are the same.

(a) C-form ⟹ ES
* `ESProp_iff_rat`: for n > 0, `ESProp n` ⟺ ∃ positive x, y, z with (4:ℚ)/n = 1/x + 1/y + 1/z.
* `cform_ES : CForm n C a → ESProp n`. Proof: write a + 1 = 4Cu and b + 1 = 4Cv. Then n + u + v = 4Cuv, and the
  witnesses are x = Cuv, y = nCv, z = nCu, as in the repo (`:389`). `cform_ES_rat` gives the same as a rational
  identity, with n > 0 derived rather than assumed.
* `cform_C_bound : CForm n C a → 4*C ≤ n+2` (`BRAINSTORM/z45_euler_systems.md:126`, Lemma 3.1). It makes the C-form
  search finite for each n.

(b) T1 and the QNR lemma
* Lemma A, `jacobi_C_of_dvd_succ : 4*C ∣ a+1 → J(C | a) = 1`. Proof: split off the 2-part of C (χ₈) and use reciprocity
  on the odd part (qrSign plus `mod_left`).
* Lemma B, `jacobi_n_of_cform : CForm n C a → J(n | a) = −1`. This is the QNR lemma of `BRAINSTORM/z52b_free_fable.md:489`.
* `jacobi_a_of_cform : n % 4 = 1 → CForm n C a → J(a | n) = −1`. For prime n = p, every C-form divisor is a QNR mod p.
* **T1:** `no_cform_square (m C a) : ¬ CForm (m^2) C a`.
* **T1, shifted form** (`FRONTIER.md:241`, `PARITY_AUDIT.md:214`): `no_shifted_square (m u f) : ¬ (f ∣ m^2+u ∧ 4*u ∣ f+1)`.
* `cform_iff_shifted`: for n > 0, (∃ C a, CForm n C a) ⟺ (∃ u f, f ∣ n+u ∧ 4u ∣ f+1)
  (`BRAINSTORM/z52b_free_fable.md:36`).

Extensions (cheap by-products):
* `no_typeII_square (m c d f) : ¬ (f ∣ 4c²d·m² + 1 ∧ 4cd ∣ f+1)`. This is T1 for the full Type II divisor form
  (`FRONTIER.md:44`). The case c = 1 is the C-form.
* `no_typeI_square (m c d f) (gcd(f,m)=1) : ¬ (f ∣ m⁴ + 4c²d ∧ 4cd ∣ f + m²)`. This is T1 for the Type I divisor form;
  the coprimality hypothesis is required, see finding 2.
* `ESProp_mul`, `ESProp_two`, `ESProp_three_mod_four`, and `ES_of_primes_one_mod_four`: ES for all primes p ≡ 1 (4)
  implies `ErdosStraus`. `ES_of_cform_primes`: the C-form at all such p implies `ErdosStraus` (see finding 3).

The equivalence between the divisor forms and Elsholtz–Tao Type I/II *solutions* is **not** formalised.

## Axioms (`lean/ES/ES/Axioms.lean`, `#print axioms`)

All 15 audited theorems (`ESProp_iff_rat`, `cofactor_dvd`, `cform_ES`, `cform_ES_rat`, `cform_C_bound`, `jacobi_C_of_dvd_succ`,
`jacobi_n_of_cform`, `no_cform_square`, `no_shifted_square`, `jacobi_a_of_cform`, `cform_iff_shifted`,
`no_typeII_square`, `no_typeI_square`, `ES_of_primes_one_mod_four`, `ES_of_cform_primes`) report the same result:
`depends on axioms: [propext, Classical.choice, Quot.sound]`. There is no `sorry` and no `native_decide`. The
`decide` sanity examples check a C-form instance (n = 13, C = 2, a = 7) and the two Type I counterexamples.

## Build

Toolchain `leanprover/lean4:v4.34.1`. mathlib is pinned at `d13f23b723b8a846827a245b89c10fc7d3f11612`, the same pin as
`../plasma-erdos-lean`, so `lake exe cache get` hits the local `~/.cache/mathlib` with nothing to download.
```
cd lean/ES
lake exe cache get        # or clone .lake/packages from a sibling project at the same revs, as done here
systemd-run --user --scope -p MemoryMax=16G timeout 3600 lake build     # ~10 s after the cache is in place
```
Note: `ulimit -v 16000000` makes lake/lean abort with "failed to create thread". Lean reserves a lot of virtual memory
for its threads, so a cgroup memory cap (`systemd-run … MemoryMax=16G`) was used instead. `.lake/` is gitignored.
