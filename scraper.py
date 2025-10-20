import requests
import os
import csv
from bs4 import BeautifulSoup


def prenesi_stran():
    url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    os.makedirs("podatki", exist_ok=True)

    vsebina = requests.get(url, headers=headers)
    if vsebina.status_code == 200:
        pot = os.path.join("podatki", "goodreads_stran.html")
        with open(pot, "w", encoding="utf-8") as f:
            f.write(vsebina.text)
        print("Stran prenesena in shranjena v goodreads_stran.html")
    else:
        print(f"Napaka, (status {vsebina.status_code})")


def izlusci_knjige():
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

    print("Shranjeno v knjige.csv")


if __name__ == "__main__":
    izlusci_knjige()
