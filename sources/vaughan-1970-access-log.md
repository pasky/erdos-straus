# Vaughan (1970) access log

**Status at 2026-08-29: no lawful public full-text copy obtained.** The publisher copy is access-controlled, the author and institutional records have no deposited manuscript, and Internet Archive Scholar explicitly reports “No known archive.” No PDF, extracted text, or comparison memo was created.

## 1. DOI and publisher routes

- <https://doi.org/10.1112/S0025579300002886> — resolves to Wiley; direct retrieval meets Cloudflare's verification page.
- <https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/S0025579300002886> — bibliographic article page is readable through Jina Reader and exposes PDF buttons, but no open-access label or downloadable file.
- <https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/S0025579300002886> — HTTP 403, Cloudflare challenge (`cf-mitigated: challenge`). The generic host <https://onlinelibrary.wiley.com/doi/pdf/10.1112/S0025579300002886> fails identically.
- <https://londmathsoc.onlinelibrary.wiley.com/doi/epdf/10.1112/S0025579300002886> — HTTP 403, Cloudflare challenge. `/doi/pdfdirect/` and `?download=true`, `?download=1`, and `?af=R` variants also return the challenge on both Wiley hosts.
- <https://londmathsoc.onlinelibrary.wiley.com/toc/20417942/1970/17/2> — issue record found; it does not provide open full text.
- Wiley's Crossref deposit points to the same `/doi/pdf/` URL as a text-mining link; it does not confer access. Guessed Wiley CMS-asset URLs based on the public first-page-image UUID returned HTTP 403 rather than a file.

## 2. Cambridge legacy archive

- <https://www.cambridge.org/core/journals/mathematika/article/on-a-problem-of-erdos-straus-and-schinzel/6622BF4A083315C30DF1114A6F600223> — legacy article record found. It says “Get access,” reports no institutional access in this environment, and has no open-access download.
- <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6622BF4A083315C30DF1114A6F600223/S0025579300002886a.pdf/div-class-title-on-a-problem-of-erdos-straus-and-schinzel-div.pdf> — this is Cambridge's own `citation_pdf_url`, but it redirects/serves the access-block article HTML, not PDF bytes. The shortened URL ending at `S0025579300002886a.pdf` behaves the same way.

## 3. Internet Archive and preservation records

- <https://scholar.archive.org/search?q=%22On+a+problem+of+Erdos%2C+Straus+and+Schinzel%22&date=all_time&type=everything&access=everything> — finds the bibliographic record but labels it **“No known archive.”**
- <https://scholar.archive.org/work/f5d4db79-a83d-4d13-9307-25757cb07e9b> — work permalink, again “No known archive.”
- <https://scholar.archive.org/fatcat/release/a2fe09e3-098e-4478-9dc2-3bc60a48a79b> and <https://scholar.archive.org/fatcat/file/32ca8e1a-20bb-46ff-97ac-fc69e1b456f6> — useful lead, but not a copy. Fatcat knows a 220,676-byte PDF (`SHA-256 b959fbca22e5e4764b4bb14a3d765a2d980eb0bf5f93c416b973c0f8260dcbfd`, `SHA-1 7fb9a6d144934ce8026a1e919e213e6349c8c254`, `MD5 7633addef8f8729411984bc4e7d48adc`) while explicitly saying **“Not Preserved”** and “No known archives or mirrors of this file”; its public URL list is empty. Do not mistake this catalog record for archived full text.
- Internet Archive advanced metadata search for the exact title returned zero items. Searches by all three Fatcat hashes also returned zero items.
- Wayback CDX queries for the Wiley PDF URLs, Cambridge `S0025579300002886a.pdf` path, and legacy `journals.cambridge.org/*S0025579300002886*` returned empty result arrays.

## 4. Author and institutional routes

- <https://personal.science.psu.edu/rcv4/> — Vaughan's home page is live. Its publications link goes to <https://personal.science.psu.edu/rcv4/pubswww.pdf>, which cites this paper as publication 4 but supplies no reprint link.
- <https://pure.psu.edu/en/publications/on-a-problem-of-erd%C8%8Ds-straus-and-schinzel> — Penn State Pure record has metadata and only the publisher DOI under “Access to Document”; no deposited file.
- Common plausible filenames under the author's live root all returned HTTP 404: `ESS.pdf`, `Erdos.pdf`, `ErdosStraus.pdf`, `ErdossStraus.pdf`, `Vaughan1970.pdf`, `vaughan1970.pdf`, `ESS1970.pdf`, `Mathematika17.pdf`, `math17.pdf`, `ess.pdf`, `erdos.pdf`, `erdosstraus.pdf`, `1970.pdf`, `paper4.pdf`, and `pub4.pdf`. The same likely names under `/papers/`, `/reprints/`, and the migrated `https://sites.psu.edu/rcv4/files/2023/07/` area produced no file.

## 5. Broader lawful-copy search

- Exact-title and DOI searches with Jina Search found only Wiley/Cambridge publisher records, Penn State metadata, and later papers that cite Vaughan; no university course-page scan or institutional-repository manuscript surfaced.
- <https://www.semanticscholar.org/paper/On-a-problem-of-Erds%2C-Straus-and-Schinzel-Vaughan/12e284b0c21554c164cb364e1d75844b2c24358c> marks its `openAccessPdf` status **CLOSED** and gives no PDF URL.
- OpenAlex's DOI record reports `is_oa: false`, `oa_status: closed`, and `any_repository_has_fulltext: false`.
- <https://scispace.com/papers/on-a-problem-of-erdos-straus-and-schinzel-4fo2wyggyx> is only an aggregator metadata page; it was not used as a source. Searches also found no target article in EuDML/GDZ or JSTOR.

Only legitimate publisher, author, institutional, and archive routes were pursued; Sci-Hub and LibGen were not queried.
