def get_korisnik(redni_broj, korisnik):
    print(f"\t{redni_broj}. {korisnik.ime} {korisnik.prezime}")

def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()

