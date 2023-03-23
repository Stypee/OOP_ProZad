from datetime import date

korisnik = {

}

korisnik['ime'] = input('Unesite ime korisnika: ').capitalize()
korisnik['prezime'] = input('Unesite prezime korisnika: ').capitalize()
korisnik['telefon'] = int(input('Unesite telefon korisnika: '))
korisnik['email'] = input('Unesite email korisnika: ').strip()

artikal = {

}

artikal['naslov'] = input('Unesite naslov artikla: ')
artikal['opis'] = input('Unesite opis artikla: ')
artikal['cijena'] = float(input('Unesite cijenu artikla: '))

prodaja = {

}

dan = int(input('Unesite dan isteka prodaje: '))
mjesec = int(input('Unesite mjesec isteka prodaje: '))
godina = int(input('Unesite godinu isteka prodaje: '))
prodaja['datum'] = date(godina ,mjesec, dan)

prodaja['korisnik'] = korisnik
prodaja['artikal'] = artikal

print('Informacije o artiklu:\n\t Naslov:',prodaja['artikal']['naslov'],'\n\t Opis:',prodaja['artikal']['opis'],
      '\n\t Cijena:',prodaja['artikal']['cijena'],'\n Datum isteka prodaje:\n\t Dan:',prodaja['datum'].day,
      '\n\t Mjesec:',prodaja['datum'].month,'\n\t Godina:',prodaja['datum'].year,'\n Informacije o korisniku:\n\t',
      prodaja['korisnik']['ime'],prodaja['korisnik']['prezime'],'\n\t Telefon:',prodaja['korisnik']['telefon'],'\n\t Email:',prodaja['korisnik']['email'])







