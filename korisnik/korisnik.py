from abc import ABC,abstractmethod

class Korisnik(ABC):
    def __init__(self, email, telefon, oib):
        self._email = email
        self._telefon = telefon
        self._oib = oib

    @property
    def email(self):
        return self._email

    @property
    def telefon(self):
        return self._telefon

    @property
    def oib(self):
        return self._oib

    @abstractmethod
    def ispis(self):
        pass


