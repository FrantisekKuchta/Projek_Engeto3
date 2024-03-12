# Engeto python 3 projekt
Třetí projekt na Python Akademii od Engeta

## Popis projektu
Projekt slouží  k výtahu výsledků z parlamentních voleb z roku 2017. Odkaz k nahlédnuti  naleznete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, které jsou pouzity v tom to kódu jsou uložené v souboru requirements.txt . Pro instalaci se doporučuje použít nové virtuální prostředí a nainstalovaným manažerem spustit následovně:

>- pip3 --version                   #overi verzi manazeru
>- pip3 install -r requirements.txt #nainstalujete knihovny

## Spuštení projektu
Spustění souboru election_scraper.py v ramči příkatověho řádku požaduje dva argumenty.

>- python elections_scraper.py <odkaz-uzemního-celku> <jmeno-souboru>


Nasledně se Vám stáhnou výsledky jako soubor s připonou .csv .


Dále projek nabýzí spištení souboru zahranici.py , který vám stahne vysledky voleb z regionu zahraniči.
Pro spuštění je zapotřebí zadat pouze jeden argumet a to nazev souboru s priponou .csv .

>- python zahranici.py <jmeno-souboru>

## Ukázka projektu 

Výslekdy hlasovaní pro okres Svitavy:

>- 1.argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5303
>- 2.argument: vysledky_svitavy.csv

Spuštení programu:

>- python elections_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5303' 'svitavy.csv'

Průběh stahovaní:

STAHUJI DATA z adresy: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5303
Ukldám data do souboru: vysledky_svitavy.csv
Ukončuji: elections_scraper.py

Častešný výstup:

>- 'Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy', 'Občanská demokratická strana'..............
>- '572560', 'Banín', '264', '157', '157', '7', '0', '0', '12', '0', '5', '23', '1', '3', '3', '0', '1', '14', '0', '4', ................
>- '572586', 'Bělá nad Svitavou', '413', '238', '237', '16', '0', '0', '24', '2', '9', '20', '3', '1', '2', '0', '1', '16',............... 

Výsledky hlosovani pro zahraniči:

>- 1.argument: vysledky_zahranici.csv

Spustění programu:

>- python zahranici.py 'vysledky_zahranici.csv'