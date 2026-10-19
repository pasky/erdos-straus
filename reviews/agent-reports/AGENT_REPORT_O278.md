# AGENT REPORT O278 — consolidation C2: hardening the 3/4 exceptional-set note

Branch `side-agent/paper-threequarter`. Target `paper/es-threequarter-note.tex`.
Internal only; no external release.

## 1. Literature check (goal 1)

Question: is there a published or arXiv result (2015–2026, or earlier)
that improves Vaughan's `E(N) ≪ N exp(−c (log N)^{2/3})` for 4/n, or for
m/n with three unit fractions?

**Answer: none found.** The 3/4 bound is not in the literature we could
locate. The best published bound for `4/n` is still Vaughan's 2/3. This
supports "no known improvement". It does not prove that none exists.

The search was a research subagent plus my own checks of the local PDFs.

| source | exceptional-set statement | how verified |
|---|---|---|
| Vaughan, Mathematika 17 (1970) 193–198, DOI 10.1112/S0025579300002886 | `#{n<N : f(n)=0} ≤ N exp(−c log^{2/3} N)` (as quoted by ET) | No lawful full text (`sources/vaughan-1970-access-log.md`). Statement taken from ET and Bloom–Elsholtz. |
| Elsholtz–Tao, J. Aust. Math. Soc. 94 (2013) 50–105, arXiv:1107.1010 | Intro: "it was shown by Vaughan [82] that the number of n<N for which f(n)=0 is at most N exp(−c log^{2/3} N) … (Compare also [48,84,39,89] for some weaker results)". No improvement of its own. | I read it in the local PDF (`pdftotext`, l. 101–106). |
| Bloom–Elsholtz, "Egyptian fractions", arXiv:2210.04496 (2022 survey) | "Vaughan showed that `E_{4,3}(N) ≤ N exp(−c(log N)^{2/3})`". It gives the general bound `E_{m,k}(N) ≤ N exp(−c_{m,k}(log N)^{1−1/(2^{k−1}−1)})` for `m>k≥3` (Elsholtz). At k=3 this is Vaughan's bound; at k=4 it is 6/7, but that is a different problem (four summands). | Subagent read the arXiv HTML. |
| Pomerance–Weingartner, arXiv:2511.16817 (Ramanujan J. 2026) | Thm 1.3: for `4≤m≤(log N)^2`, `#{n≤N : m/n not a sum of 3 unit fractions} ≤ N/exp(C(log² N/φ(m))^{1/3})`. At fixed m=4 the exponent is again 2/3. The paper says its proof "largely follows the argument in Vaughan". | Subagent read the arXiv HTML. The campaign had already audited this paper. |
| erdosproblems.com/242 | Lists Vaughan's bound and no stronger exceptional-set estimate. | Page visited. The formulas did not render, so only the list of references was used. |
| Elsholtz, Trans. AMS 353 (2001); Elsholtz–Planitzer 2020; Huang–Vaughan 2013 (binary); López 2022/2024; Chamberland 2026 | None improves the 2/3 exponent for three summands. (Elsholtz 2001 is the source of the k-term exponents; Huang–Vaughan treats two summands.) | Subagent; LITERATURE_2026.md. |

**Conclusion for the note.** Say "improves the exponent 2/3 of Vaughan
[V]; we are not aware of an earlier improvement of the exponent". Do not
claim priority beyond that.

Related analogue: for k ≥ 4 summands, Elsholtz already has exponents
above 3/4 (6/7 for k=4). That is consistent with a parameter-count
heuristic and is not a 3-term result.
