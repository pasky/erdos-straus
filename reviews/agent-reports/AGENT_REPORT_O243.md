# AGENT REPORT O243 — novelty audit of wave Z ((J)57–(J)72)

Branch `side-agent/novelty-audit-e`. Main file: `reviews/novelty-audit-2026-10e.md`
(§0 claim list, §§1–8 findings + verdict tables, §9 summary, §10 proposed ledger edits).
Archive: `sources/lit2026e/` (text excerpts only, ~110 KB; PDFs already in the repo were
re-used, not duplicated).

## Main findings (beyond what the ledger already says)

1. **(J)63 Prop 5.1 at e = 0 — KNOWN.** The class family −4D (mod M), D | A²
   (= the 3/4 note's ℛ(M)) is ET Prop 1.9's Type II family "−4a²d mod f, 4ad | f + 1"
   (ET p. 8, credited to Rosati 1954 and Vaughan 1970); the iff for primes is
   Chamberland, Integers 26 (2026) #A42, Thm 1. Neither the ledger nor
   `paper/es-threequarter-note.tex` cites these for ℛ(M). The e ≥ 1 family 𝒟_e(M) is new.
2. **(J)59 sieve ladder — PARTIAL.** "More free parameters ⇒ exponent 1 − 1/D" is the
   Vaughan → Viola → Shen → Elsholtz (Trans. AMS 2001, Thm 1.3, p. 3210) line for k-term
   representations. The campaign's ladder takes its parameters from the cap instead.
   The 3/4 note's "θ = 𝓑/(𝓑+1)" remark should cite Elsholtz 2001.
3. **(J)64 Thm 1.1 — PARTIAL.** Dahan arXiv:2608.24035 Prop 4.8/Thm 4.6 already prove the
   necessary direction: a window succeeds ⇒ −1 ∈ ⟨primes of K⟩ mod c. Dahan avoids the
   subgroup route on purpose, because membership does not bound the exponents. The
   capped converse is new.
4. **(J)65 Thm 1.1 — confirmed KNOWN in substance.** Chenu–Smith Prop 1–2 give the
   forward direction. Their **Lemma 1 (p. 6) gives the converse**, which R234 did not
   cite. Arpin et al. §5.3 is purely empirical.
5. **(J)57 Thm 1.3, lattice half — KNOWN in substance.** "Q mod 4 on L/2L" is Brown's
   ℤ/4-enhancement (Brown 1972, via Taylor arXiv:2208.06319 §2). Under the 2-adic
   diagonal form, the two-class count is: isotropic ⟺ the units are mixed mod 4. I
   checked this by brute force over all 20 unit patterns. The pentagon dictionary is new.
6. **Exponential families (J)62/(J)68/(J)69 — APPARENTLY NEW.** I checked the full zbMATH
   list of 70 "Erdős–Straus" documents and ran web searches; no ES work on exponential
   families turned up. One method lineage should be cited: (J)69's covering closed by an
   algebraic factorisation is the ES analogue of Izotov's Sierpiński-number construction
   (Filaseta–Finch–Kozek, JNT 128 (2008) §1).
7. **Function-field items (J)67/(J)71/(J)72.** The mechanisms are known: Weil/resultant
   reciprocity, the Liouville–Mahler 1949 inequality, "winning sets meet every ball"
   (Schmidt; McMullen 2010; Kristensen 2006 over F_q((T⁻¹))), and König's lemma with the
   Cantor dimension bound. The ES_q consequences, Thm 2.2 (q = 9), Prop 3.2 and the
   dictionaries are apparently new. Nothing on ES over F_q[T] exists.
8. **(J)70 sterile points for r ≥ 2^{21.44} — APPARENTLY NEW.** Lemma 3.1 is ET Prop 1.9
   (two families) in substance.
9. **(J)66 Cor 2.1/2.2 and (J)64 Thm 1.3.** These are new as statements about the
   campaign-defined cap. OpenAlex citation lists show no ES/Egyptian-fraction application
   of Pollack's IJNT 2014 or JNT 2018 theorems.
10. **(J)61 Thm 2.1** is a reformulation of the Bright–Loughran/Yamamoto sign as an
    Artin symbol. Cor 2.2/2.3 are ES-specific and apparently new.

## Limits

I did not access: Vaughan 1970, Rosati 1954, Nakayama 1939, Izotov 1995, Sierpiński 1960,
Brown 1972, Gross 1987, Falconer, Lasjaunias 2000 or Hussain 2023. Where these appear,
the citation is second-hand and tagged as such. Semantic Scholar was rate-limited.
"Apparently new" means not found; it is not a priority certificate.

## For the orchestrator

§10 of the main file lists 13 concrete ledger edits. Edits 1–4 (Chamberland/ET for ℛ(M),
Elsholtz 2001, Dahan Prop 4.8, Chenu–Smith Lemma 1) are the substantive ones. The rest
are attribution lines.
