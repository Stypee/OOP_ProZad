from .artikl import Artikl

class Instrukcije(Artikl):

    def __init__(self, ime_predmeta, datum_odrzavanja, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)
        self.ime_predmeta = ime_predmeta
        self.datum_odrzavanja = datum_odrzavanja

    def ispis(self):
        print('Informacije o instrukcijama: ')
        print(f'\t Naslov: {self.naslov}')
        print(f'\t Opis: {self.opis}')
        print(f'\t Cijena: {self.cijena}')
        print(f'\t Ime predmeta: {self.ime_predmeta}')
        print(f'\t Datum održavanja: {self.datum_odrzavanja}')

