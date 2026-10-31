"""z52b Pass-1 U03: arXiv API lookups for literature items (title/author queries). Retries on HTTP 429.
Usage: uv run python scripts/z52b_p1_U03_arxiv.py > data/z52b/pass1/U03/arxiv_lookups.txt"""
import urllib.request, urllib.parse, time, re
QUERIES = {
 "Z2081": 'ti:"Goldbach-Linnik" AND ti:"powers of two"', "Z2082": 'ti:"Pintz" AND ti:"powers of two"',
 "Z2421": 'au:Zhang AND ti:Landau-Siegel', "Z2412": 'au:Ustinov AND ti:Kloosterman',
 "Z2413": 'au:Petrow AND au:Young AND ti:Weyl', "Z2416": 'au:Pierce AND au:Wood AND ti:Chebotarev',
 "Z2423": 'au:Drappeau AND au:Pratt', "Z2512": 'au:Holowinsky AND au:Soundararajan',
 "Z2519": 'au:Stromberg AND au:Venkatesh', "Z2522": 'au:Katz AND ti:Kloosterman',
 "Z2525": 'au:Rudnick AND au:Soundararajan AND ti:moments', "Z2578": 'au:Sawin AND ti:cancellation',
 "Z2408": 'au:Harel AND au:Samotij', "Z2411": 'au:Koukoulopoulos AND au:Maynard AND ti:Duffin',
 "Z2402": 'au:Granville AND au:Koukoulopoulos AND au:Matomaki', "Z2403": 'au:Ford AND au:Maynard AND ti:prime',
 "Z2387": 'au:Matomaki AND au:Radziwill AND au:Tao', "Z2382": 'au:Guth AND au:Maynard',
 "Z2380": 'au:Lichtman AND ti:Goldbach', "Z2381": 'au:Fouvry AND au:Radziwill',
 "Z2395": 'au:Bretheche AND au:Drappeau', "Z2397": 'au:Dunn AND au:Kerr AND au:Shparlinski',
 "Z2399": 'au:Kowalski AND au:Michel AND ti:trace', "Z2446": 'au:Peluse AND au:Prendiville',
 "Z2462": 'au:Wooley AND ti:congruencing', "Z2599": 'au:Munshi AND ti:delta',
 "Z2603": 'au:Teravainen AND ti:Chowla', "Z2603b": 'au:Klurman AND au:Mangerel',
 "Z3054": 'au:Goldfeld AND ti:Siegel', "Z2098": 'ti:Tatuzawa', "Z2077": 'au:Sorenson AND au:Bach',
 "Z2418": 'au:Platt AND au:Trudgian', "Z2078": 'au:Gupta AND au:Murty AND ti:primitive',
 "Z2094": 'au:Hooley AND ti:Waring', "Z2096": 'au:Ford AND ti:short intervals',
 "Z2097": 'au:Hall AND au:Tenenbaum', "Z2401": 'au:Irving AND ti:divisor',
 "Z2401b": 'au:Liu AND au:Shparlinski AND au:Zhang', "Z2404": 'au:Lichtman AND ti:primitive',
 "Z2459": 'au:Solymosi AND ti:sum-product', "Z2431": 'au:Bourgain AND ti:composite',
 "Z2564": 'au:Ford AND au:Konyagin AND au:Maynard AND au:Tao', "Z2356": 'au:Friedlander AND au:Iwaniec AND ti:parity',
 "Z2320": 'au:Harman AND ti:Linnik', "Z2303": 'ti:circle method AND ti:exceptional set',
 "Z2189": 'ti:Erdos AND ti:exceptional set', "Z2298": 'au:Sawhney AND ti:prime',
 "Z2611": 'au:Vaughan AND ti:exceptional', "Z2611b": 'au:Webb AND ti:exceptional set',
 "Z1427": 'au:Elsholtz AND au:Tao AND ti:exceptional',
}
def get(q):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "max_results": 2})
    for t in range(6):
        try:
            return urllib.request.urlopen(url, timeout=60).read().decode()
        except Exception as e:
            time.sleep(25)
    return ""
for key, q in QUERIES.items():
    x = get(q); time.sleep(8)
    ents = re.findall(r"<entry>(.*?)</entry>", x, re.S)[:2]
    if not ents: print(key, "| NO RESULT | q=", q); continue
    for e in ents:
        t = re.search(r"<title>(.*?)</title>", e, re.S).group(1).strip().replace("\n", " ")
        i = re.search(r"<id>(.*?)</id>", e).group(1).split("/abs/")[-1]
        d = re.search(r"<published>(.*?)T", e).group(1)
        print(key, "|", i, d, "|", t[:110])
