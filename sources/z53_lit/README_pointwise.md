# Pointwise-literature sweep source bundle

Access date: 2026-11-01. This supplementary bundle focuses on primary-source verification of the two 2026 Zaremba claims and late-October ES preprints. The larger repo’s existing ledgers hold the broader 2020–26 arithmetic/literature survey; avoid duplicate citations except where clarified here.

## Saved PDFs (2 of maximum 6; each <3 MB)

- Ilya D. Shkredov, arXiv:2603.14116v2, revised 2026-06-24, `shkredov-2603.14116.pdf`, 533 KB. SHA-256: `e0e54c3eedcc059c9dc7a284b0bdb64ab0fce0f408560eb0bebc3d9671335434`.
- Xin Zhang, arXiv:2605.02518v2, revised 2026-05-08, `zhang-2605.02518.pdf`, 389 KB. SHA-256: `05d996706ca2ecd1f8141cfe26f53bac2a262012b1a5655003638c6da25e65f5`.

Both PDFs downloaded from the versioned arXiv PDF URLs and text-extracted with pypdf for inspection. Verbatim excerpts and page/theorem locators are in `excerpts_pointwise.txt`.

## Sources and limitations

- arXiv API metadata for both Zaremba papers fetched 2026-11-01; latest records remain v2. Shkredov describes the prime/squarefree corollary and reports the full all-q extension in Remark 9 from Zhang–Tang expansion; its power-size Theorem 8 remains restricted to its class Z. Zhang’s PDF supplies the underlying general-modulus growth, mixing/correlation estimate, and main-term-versus-error condition.
- Erdős Problems #242 opened at https://www.erdosproblems.com/242 through the visit-webpage extraction tool on 2026-11-01. Extracted text gave no last-edit timestamp/forum chronology. A targeted web-search query failed HTTP 422; no inference about post-2026-10-17 forum posts is made.
- ArXiv API direct query for `all:"Erdos-Straus"` fetched 2026-11-01; its newest returned ES-labeled entry was Jiang 2609.09204v2 (submitted 2026-09-05). The sweep is not exhaustive across accents, alternate spellings, title metadata, or subject categories. Repository prior direct-ID verification covers Cao–Xu 2610.32302v1 (2026-10-23): its central covering claim is expressly stated to lack a logical proof; see `sources/z52/es_direct/2610.32302.txt`.

## Literature verdict in brief

No verified single-input existence theorem was found with a natural polylogarithmic expected witness count and unconditional (or GRH-conditional) pointwise nonemptiness that contradicts assessment (J)103. Near examples either have power-size count (Zaremba, Goldbach/Linnik/form representations), use a fixed-modulus character/primitive-root event under GRH, or use a deliberately designed set (thin additive bases). Precise classification and target applicability are in the research agent’s report.
