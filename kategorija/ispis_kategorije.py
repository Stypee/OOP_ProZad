from artikl import ispis_artikla
def get_kategorija(redni_broj, kategorija):
    print(f"{redni_broj}. {kategorija['naziv']}")

def ispis_svih_kategorija(kategorije):
    for i,kategorija in enumerate(kategorije, start = 0):
        print(f"{kategorija['naziv']}")
        ispis_artikla(kategorije[i]['artikli'])

