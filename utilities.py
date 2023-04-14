from datetime import date
def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Unijeli ste negativan broj!')

        except ValueError:
            print('Unijeli ste znak, a ne pozitivni cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0.0:
                raise Exception('Unijeli ste negativan broj!')

        except ValueError:
            print('Unijeli ste znak, a ne pozitivni realni broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_datuma(poruka):
    while True:
        try:
            dan = int(input(poruka))
            mjesec = int(input('Unesite mjesec isteka prodaje: '))
            godina = int(input('Unesite godinu isteka prodaje: '))
            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        except TypeError:
            print('Unijeli ste znak!')

        else:
            return datum

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu od {min} do {max}: "))

            if broj<min or broj>max:
                raise Exception('Broj nije u intervalu!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj




