from datetime import date

korisnici = []
kategorije = []
prodaje = []

br_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1,br_korisnika+1):
    korisnik = {
    }

    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()

    korisnici.append(korisnik)

br_kategorija = int(input('Unesite broj kategorija: '))
for i in range(1,br_kategorija+1):
    kategorija = {
    }

    kategorija['naziv'] = input(f'Unesite naziv {i}. kategorije: ')
    kategorija['artikli'] = []

    br_artikala = int(input(f'Unesite broj artikala za {i}. kategoriju: '))
    for j in range(1,br_artikala+1):
        artikl = {
        }

        artikl['naslov'] = input(f'Unesite naslov {j}. artikla: ')
        artikl['opis'] = input(f'Unesite opis {j}. artikla: ')
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla: '))

        kategorija['artikli'].append(artikl)

    kategorije.append(kategorija)

br_prodaja = int(input('Unesite broj prodaja: '))
for i in range(1,br_prodaja+1):
    prodaja = {
    }

    dan = int(input(f'Unesite dan isteka {i}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec isteka {i}. prodaje: '))
    godina = int(input(f'Unesite godinu isteka {i}. prodaje: '))
    prodaja['datum'] = date(godina ,mjesec, dan)

    print(f'Odaberite korisnika {i}. prodaje')
    for j,korisnik in enumerate(korisnici, start = 1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")

    odabrani_korisnik = int(input('Odabrani korisnik: '))
    prodaja['korisnik'] = korisnici[odabrani_korisnik-1]

    print(f'Odaberite kategoriju {i}. prodaje')
    for j,kategorija in enumerate(kategorije, start = 1):
            print(f"{j}. {kategorija['naziv']}")

    odabrana_kategorija =int(input('Odabrana kategorija: '))

    print(f'Odaberite artikl {i}. prodaje')
    for j,artikl in enumerate(kategorije[odabrana_kategorija-1]['artikli'], start=1):
            print(f"{j}. {kategorije[odabrana_kategorija-1]['artikli'][j-1]['naslov']}")

    odabrani_artikl = int(input('Odabrani artikl: '))
    prodaja['artikl'] = kategorije[odabrana_kategorija-1]['artikli'][odabrani_artikl-1]
    prodaje.append(prodaja)


for i,prodaja in enumerate(prodaje, start = 1):
    print(f"Prodaja {i}")
    print('Informacije o korisniku: ')
    print(f"\tIme: {prodaja['korisnik']['ime']}")
    print(f"\tPrezime: {prodaja['korisnik']['prezime']}")
    print(f"\tTelefon: {prodaja['korisnik']['telefon']}")
    print(f"\tEmail: {prodaja['korisnik']['email']}")

    print('Informacije o artiklu: ')
    print(f"\tNaslov: {prodaja['artikl']['naslov']}")
    print(f"\tOpis: {prodaja['artikl']['opis']}")
    print(f"\tCijena: {prodaja['artikl']['cijena']}")

    print('Datum isteka: ')
    print(f"\tDan: {prodaja['datum'].day}")
    print(f"\tMjesec: {prodaja['datum'].month}")
    print(f"\tGodina: {prodaja['datum'].year}")
    print('-'*20)


