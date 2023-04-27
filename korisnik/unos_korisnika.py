from .korisnik import Korisnik
from utilities import unos_telefona
def unos_korisnika(redni_broj):


    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()

    return Korisnik(ime, prezime, telefon, email)
