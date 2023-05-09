class BankovnaKartica:
    def __init__(self, iban, pin, kratki_broj):
        self.__iban = iban
        self.__pin = pin
        self.__kratki_broj = kratki_broj
    @property
    def iban(self):
        return self.__iban
    @iban.setter
    def iban(self, iban):
        self.__iban = iban
    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
    @property
    def kratki_broj(self):
        return self.__kratki_broj

    @kratki_broj.setter
    def kratki_broj(self, kratki_broj):
        self.__kratki_broj = kratki_broj
    def ispis(self):
        print("Informacije o bankovnoj kartici: ")
        print(f"\t IBAN: {self.__iban}")
        print(f"\t PIN: {self.__pin}")
        print(f"\t Kratki broj: {self.__kratki_broj}")