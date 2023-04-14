from utilities import unos_pozitivnog_realnog_broja
def unos_artikla(redni_broj):
    artikl = {
    }

    artikl['naslov'] = input(f'Unesite naslov {redni_broj}. artikla: ')
    artikl['opis'] = input(f'Unesite opis {redni_broj}. artikla: ')
    artikl['cijena'] = unos_pozitivnog_realnog_broja(f'Unesite cijenu {redni_broj}. artikla: ')

    return artikl
