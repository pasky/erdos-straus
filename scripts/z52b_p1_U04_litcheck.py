"""Literature lookups for U04 pass-1 (arXiv export API). Prints top hits (id, title, first authors) per query."""
import urllib.request, urllib.parse, re, html, sys, json, time
Q = {
 "Z0535_baker_unit": 'all:"unit fractions" AND all:"linear forms in logarithms"',
 "Z0535_baker_egypt": 'all:Egyptian AND all:Baker AND all:logarithms',
 "Z1670_derenthal": 'all:Derenthal AND all:torsors AND all:Pezzo',
 "Z2480_cox_cayley": 'all:Cox AND all:ring AND all:"del Pezzo" AND all:singular',
 "Z2042_CZ_hilbert": 'all:Corvaja AND all:Zannier AND all:"Hilbert property"',
 "Z2465_orlik_terao": 'all:"broken circuit" AND all:"reciprocal"',
 "Z2465_reciprocal_plane": 'all:"reciprocal plane" AND all:"Orlik"',
 "Z2477_CZ_integral": 'all:Corvaja AND all:Zannier AND all:"integral points" AND all:surfaces',
 "Z2697_surj_integral": 'all:"integral points" AND all:surjective AND all:fibration',
 "Z2453_alon_roichman": 'all:Alon AND all:Roichman AND all:Cayley',
 "Z2511_blomer_shifted": 'all:Blomer AND all:"shifted convolution"',
 "Z2646_gillman": 'all:Gillman AND all:"random walks" AND all:expander',
 "Z2530_bruinier_funke": 'all:Bruinier AND all:Funke AND all:"theta lifts"',
 "Z1683_mock_egypt": 'all:"mock modular" AND all:"exact formula" AND all:Rademacher',
 "Z2328_Coef_nonvanish": 'all:"Fourier coefficients" AND all:nonvanishing AND all:primes AND all:"modular forms"',
 "Z2866_button_markoff": 'all:Markoff AND all:uniqueness AND all:prime',
 "Z2664_HP_markov": 'all:Hacking AND all:Prokhorov AND all:Markov',
 "Z2228_Brauer_pencil": 'all:"Brauer-Manin" AND all:pencil AND all:"integral points" AND all:cubic',
 "Z2936_Ono_Sound": 'all:Ono AND all:Soundararajan AND all:"Ramanujan" AND all:partitions',
 "Z3026_Ono_mod": 'all:Ono AND all:"mod m" AND all:"half-integral weight"',
 "Z1484_EichlerSelberg": 'all:Eichler AND all:Selberg AND all:"class numbers" AND all:"Kronecker"',
 "Z2065_DCL_murm": 'all:murmurations AND all:elliptic',
 "Z2090_Smith": 'all:Smith AND all:"congruent numbers" AND all:"positive natural density"',
 "Z2089_Tian": 'all:Tian AND all:"congruent numbers" AND all:Heegner',
 "Z2482_BLS": 'all:"Hasse principle" AND all:"random Fano"',
 "Z2555_Radchenko": 'all:Radchenko AND all:Viazovska AND all:"Fourier interpolation"',
 "Z2190_erdos300": 'all:Croot AND all:"unit fractions"',
}
out = {}
for k, q in Q.items():
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'max_results': 4})
    x = None
    for attempt in range(6):
        try:
            x = urllib.request.urlopen(url, timeout=40).read().decode('utf8'); break
        except Exception as e:
            time.sleep(8 * (attempt + 1))
    if x is None:
        out[k] = 'ERR rate-limited'; continue
    time.sleep(4)
    hits = []
    for e in re.findall(r'<entry>(.*?)</entry>', x, re.S):
        i = re.search(r'<id>(.*?)</id>', e).group(1).split('/abs/')[-1]
        t = ' '.join(html.unescape(re.search(r'<title>(.*?)</title>', e, re.S).group(1)).split())
        a = re.findall(r'<name>(.*?)</name>', e)[:2]
        hits.append(f'{i} | {t[:95]} | {", ".join(a)}')
    out[k] = hits
json.dump(out, open('data/z52b/pass1/U04/litcheck.json', 'w'), indent=1)
for k, v in out.items():
    print('##', k)
    if isinstance(v, str): print(v); continue
    for h in v[:3]: print('  ', h)
