from .korisnik import Korisnik
from .kartica import BankovnaKartica
from utilities import unos_telefona
def unos_korisnika(redni_broj):


    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    iban = input(f'Unesite iban {redni_broj}. kartice: ')
    pin = input(f'Unesite pin {redni_broj}. kartice: ')
    kratki_broj = input(f'Unesite kratki broj {redni_broj}. kartice: ')

    kartica = BankovnaKartica(iban, pin, kratki_broj)

    return Korisnik(ime, prezime, telefon, email, kartica)
