from bs4 import BeautifulSoup
import urllib.request
import json

wiki = "http://www.ii.up.krakow.pl/consultations.html"


def addColon(string):
    if len(string) <= 3:
        newString = string[0] + ':' + string[1] + string[2]
    else:
        newString = string[0] + string[1] + ':' + string[2] + string[3]
    return newString


with urllib.request.urlopen(wiki) as response:
    webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    wykladowcy = []
    pokoje = []
    dyzury = []
    for anchor in soup.find_all('span', {'class': 'fs12'}):
        tmp = anchor.get_text()[:anchor.get_text().index('K')]
        pokoje.append(tmp[6:])

    for anchor in soup.find_all('h3'):
        tmp = anchor.get_text()
        if 'Kontakt' in tmp:
            wykladowcy.append(tmp[:tmp.index('\n')])

    for anchor in soup.find_all('table', {'class': 'consultations'}):
        dni = {'Poniedzialek': '', 'Wtorek': '', 'Sroda': '', 'Czwartek': '', 'Piatek': ''}
        td = anchor.find_all('td')
        row = [i.get_text() for i in td]
        del row[0:5]
        dni['Poniedzialek'] = row[0]
        dni['Wtorek'] = row[1]
        dni['Sroda'] = row[2]
        dni['Czwartek'] = row[3]
        dni['Piatek'] = row[4]
        for dzien in dni:
            if len(dni[dzien]) < 1:
                dni[dzien] = ' '
            else:
                element = dni[dzien].index('—')
                pom = dni[dzien][:element]
                pom = addColon(pom.strip())
                pom2 = dni[dzien][element + 1:]
                pom2 = addColon(pom2.strip())
                dni[dzien] = pom + ' — ' + pom2
        dyzury.append(dni)

    tmp = len(wykladowcy)
    doJSONA = []
    for i in range(tmp):
        doJSONA.append({
            'wykladowca': wykladowcy[i],
            'pokoj': pokoje[i],
            'godziny': dyzury[i]
        })

    with open('data/wykladowcy.json', 'w', encoding='utf-8') as dane:
        json.dump(doJSONA, dane, ensure_ascii=False)
