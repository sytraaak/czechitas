
import requests
import json

#1
ico = input("Zadej IČO subjektu: ")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    obchodni_jmeno = data.get("obchodniJmeno")
    adresa = data.get("sidlo", {}).get("textovaAdresa")

    if obchodni_jmeno and adresa:
        print(obchodni_jmeno)
        print(adresa)
    else:
        print("Nepodařilo se najít obchodní jméno nebo adresu.")
else:
    print("Subjekt s tímto IČO nebyl nalezen, nebo došlo k chybě.")

#2
nazev = input("Zadej název subjektu: ")
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = {"obchodniJmeno": nazev}

res = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
    headers=headers,
    json=data
)

if res.status_code == 200:
    vysledky = res.json()
    pocet = vysledky.get("pocetCelkem", 0)
    subjekty = vysledky.get("ekonomickeSubjekty", [])

    print(f"Nalezeno subjektů: {pocet}")

    for subjekt in subjekty:
        jmeno = subjekt.get("obchodniJmeno", "")
        ico = subjekt.get("ico", "")
        print(f"{jmeno}, {ico}")
else:
    print("Došlo k chybě při vyhledávání.")
