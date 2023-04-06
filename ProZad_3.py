from korisnik import unos_korisnika, ispis_korisnika
from kategorija import unos_kategorije, ispis_kategorije
from prodaja import unos_prodaje, ispis_prodaje


korisnici = []
kategorije = []
prodaje = []

br_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1,br_korisnika+1):
    korisnici.append(unos_korisnika(i))

br_kategorija = int(input('Unesite broj kategorija: '))
for i in range(1,br_kategorija+1):
    kategorije.append(unos_kategorije(i))

br_prodaja = int(input('Unesite broj prodaja: '))
for i in range(1,br_prodaja+1):
    prodaje.append(unos_prodaje(korisnici, kategorije, i))

for i,prodaja in enumerate(prodaje, start = 1):
    print(f"Prodaja {i}: ")
    ispis_prodaje(prodaja)
