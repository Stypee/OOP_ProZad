from artikl import unos_artikla
from .kategorija import Kategorija
def unos_kategorije(redni_broj):

    naziv = input(f'Unesite naziv {redni_broj}. kategorije: ')
    artikli = []

    br_artikala = int(input(f'Unesite broj artikala za {redni_broj}. kategoriju: '))
    for j in range(1, br_artikala + 1):

        artikli.append(unos_artikla(j))

    return Kategorija(naziv, artikli)


