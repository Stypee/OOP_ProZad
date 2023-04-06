def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f"\tIme: {korisnik['ime']}")
    print(f"\tPrezime: {korisnik['prezime']}")
    print(f"\tTelefon: {korisnik['telefon']}")
    print(f"\tEmail: {korisnik['email']}")

def get_korisnik(redni_broj, korisnik):
    print(f"\t{redni_broj}. {korisnik['ime']} {korisnik['prezime']}")

