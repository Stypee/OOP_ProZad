from utilities import unos_pozitivnog_realnog_broja
from .artikl import Artikl
def unos_artikla(redni_broj):

    naslov = input(f'Unesite naslov {redni_broj}. artikla: ')
    opis = input(f'Unesite opis {redni_broj}. artikla: ')
    cijena = unos_pozitivnog_realnog_broja(f'Unesite cijenu {redni_broj}. artikla: ')

    return Artikl(naslov, opis, cijena)
