# <p align="center">ANALIZA KNJIG</p>
Za svojo projektno nalogo pri Uvodu v programiranje sem se odločil s pomočjo Pythona obdelati in analizirati top 100 knjig, ki so jih ocenili bralci na strani [Goodreads](https://www.goodreads.com/list/show/1.Best_Books_Ever).
## Pridobivanje podatkov v `scraper.py`
- Funkcija `prenesi_stran()` prenese HTML s spletne strani in ga shrani kot `goodreads_stran.html` v mapi `podatki`.
- Funkcija `izlusci_knjige()` nato s pomočjo knjižnice `BeautifulSoup` iz HTML-ja izlušči naslov, avtorja in oceno knjig in nato podatke shrani v `knjige.csv` v mapi `podatki`.
## Analiza
Analiza, ki se nahaja v mapi `notebooks` v datoteki `analiza.ipynb`, prikazuje razne grafe, diagrame in tabele, ki primerjajo knjige in avtorje glede na število ocen, priljubljenost in podobno. To nam da dober vpogled v bralno skupnost in razne trende.  