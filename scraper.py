import requests
import os
import csv
from bs4 import BeautifulSoup


def prenesi_stran():
    """Prenese spletno stran 'Best Books Ever' z Goodreads in jo shrani kot HTML."""
    url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    os.makedirs("podatki", exist_ok=True)

    odgovor = requests.get(url, headers=headers)
    if odgovor.status_code == 200:
        pot = os.path.join("podatki", "goodreads_stran.html")
        with open(pot, "w", encoding="utf-8") as f:
            f.write(odgovor.text)
        print("Stran uspešno prenesena in shranjena kot goodreads_stran.html")
    else:
        print(f"Napaka pri pridobivanju strani (status {odgovor.status_code})")


def izlusci_knjige():
    """Prebere shranjeno Goodreads HTML stran in izlušči podatke o knjigah ter jih shrani v CSV."""
    pot = os.path.join("podatki", "goodreads_stran.html")

    with open(pot, "r", encoding="utf-8") as f:
        vsebina = f.read()

    soup = BeautifulSoup(vsebina, "html.parser")
    knjige_html = soup.find_all("tr", {"itemtype": "http://schema.org/Book"})

    knjige = []
    for knjiga in knjige_html:
        naslov = knjiga.find("a", class_="bookTitle").get_text(strip=True)
        avtor = knjiga.find("a", class_="authorName").get_text(strip=True)
        ocena = knjiga.find("span", class_="minirating").get_text(strip=True)

        knjige.append({
            "naslov": naslov,
            "avtor": avtor,
            "ocena": ocena
        })

    print(f"Našel {len(knjige)} knjig.")

    csv_path = os.path.join("podatki", "knjige.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["naslov", "avtor", "ocena"])
        writer.writeheader()
        writer.writerows(knjige)

    print("Podatki shranjeni v knjige.csv")


if __name__ == "__main__":
    # prenesi_stran()  # če želiš ponovno prenesti HTML
    izlusci_knjige()
