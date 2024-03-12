import sys
import csv
from bs4 import BeautifulSoup as bea
import requests

def odkaz_pro_stahovani(adresa_URL):
    response = requests.get(adresa_URL)
    soup = bea(response.text,'html.parser')
    print(f'Stahuji data z: {adresa_URL}')
    return soup
def seznam_zemi() -> list:
    zeme = []
    ziskani_zeme = soup.find_all('td',headers='s2')
    for z in ziskani_zeme:
        zeme.append(z.text)
    return zeme

def link_zeme() -> list:
    zeme_odkaz = []
    ziskani_odkazu = soup.find_all('td','cislo','href')
    for l in ziskani_odkazu:
        l = l.a['href']
        zeme_odkaz.append(f'https://volby.cz/pls/ps2017nss/{l}')
    return zeme_odkaz
def politicke_strany() -> list:
    strany = []
    zeme = link_zeme()
    response = requests.get(zeme[0])
    soup = bea(response.text,'html.parser')
    link_strany = soup.find_all('td','overflow_name')
    for s in link_strany:
        strany.append(s.text)
    return strany
def volici_pocet() -> list:
    volici = []
    zeme = link_zeme()
    for link in zeme:
        response = requests.get(link)
        soup = bea(response.text, 'html.parser')
        lide = soup.find_all('td', headers='sa2')
        for v in lide:
            volici.append(v.text)
    return volici
def vydane_obalky() -> list:
    obalky = []
    zeme = link_zeme()
    for link in zeme:
        response = requests.get(link)
        soup = bea(response.text, 'html.parser')
        lide = soup.find_all('td', headers='sa5')
        for v in lide:
            obalky.append(v.text)
    return obalky
def platne_hlasy() -> list:
    hlasy = []
    zeme = link_zeme()
    for link in zeme:
        response = requests.get(link)
        soup = bea(response.text, 'html.parser')
        lide = soup.find_all('td', headers='sa6')
        for v in lide:
            hlasy.append(v.text)
    return hlasy
def strany_pocet_hlasu() -> list:
    pocet_hlasu = []
    zeme = link_zeme()
    for link in zeme:
        response = requests.get(link)
        soup = bea(response.text,'html.parser')
        hlasy_strany = soup.find_all('td',headers=['t1sb3','t2sb3'])
        hlasy = []
        for h in hlasy_strany:
            hlasy.append(h.text)
        pocet_hlasu.append(hlasy)
    return pocet_hlasu

def info_zeme() -> list:
    radek_zeme = []
    volic = volici_pocet()
    obalky = vydane_obalky()
    platny_hlas = platne_hlasy()
    zeme = seznam_zemi()
    strany = strany_pocet_hlasu()
    informace_zemi = zip(zeme,volic,obalky,platny_hlas)
    info_zeme = []
    for z,v,o,p, in informace_zemi:
        info_zeme.append([z,v,o,p])
    completni_info_zeme = zip(info_zeme,strany)
    for i,s in completni_info_zeme:
        radek_zeme.append(i+s)
    return radek_zeme
def vysledky(nazev_souboru):
    sloupky = ['Země','Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
    zeme = info_zeme()
    strany = politicke_strany()
    print(f'Ukládame data do souboru: {nazev_souboru}')
    for s in strany:
        sloupky.append(s)
    with open(nazev_souboru,mode='w',newline='',encoding='utf-8') as soubor:
        soubor_writer = csv.writer(soubor)
        soubor_writer.writerow(sloupky)
        soubor_writer.writerows(zeme)
    print(f'Ukoncuji: {sys.argv[0]}')

if len(sys.argv) == 2:
    soup = odkaz_pro_stahovani('https://volby.cz/pls/ps2017nss/ps36?xjazyk=CZ')
else:
    print('Zadal jsi nepsravný počet argumentu. Ukončuji program.')
    quit()


if __name__ == '__main__':
    nazev_souboru = sys.argv[1]
    vysledky(nazev_souboru)



