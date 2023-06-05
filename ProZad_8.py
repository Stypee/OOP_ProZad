from PyQt5 import QtWidgets, QtGui, QtCore
import sys

from enumeratori import TipKorisnika, TipArtikla
from korisnik import PoslovniKorisnik, PrivatniKorisnik
from prodaja import Prodaja
from artikl import Automobil, Stan
from utilities import provjera_korisnickog_unos, provjera_unosa_artikla, provjera_unosa_prodaje

korisnici = []
artikli = []
prodaje = []

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 920, 520)
        self.setWindowTitle('Objektno')
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        self.initUI()

    def initUI(self):
        offset = 30
        self.font = QtGui.QFont('Times', 10)
        self.font_okvir = QtGui.QFont('Arial', 16)
        self.font_okvir.bold()

        #Okvir za korisnika
        self.okvir_korisnik = QtWidgets.QFrame(self)
        self.okvir_korisnik.setGeometry(10, 10, 300, 500)
        self.okvir_korisnik.setFrameStyle(QtWidgets.QFrame.WinPanel)
        self.okvir_korisnik.setFrameShadow(QtWidgets.QFrame.Sunken)

        #Label za okvir korisnika
        self.label_okvir_korisnik = QtWidgets.QLabel(self)
        self.label_okvir_korisnik.setFont(self.font_okvir)
        self.label_okvir_korisnik.setText('KORISNIK')
        self.label_okvir_korisnik.move(15, 12)

        #Input tip korisnika
        self.tip_korisnika = QtWidgets.QComboBox(self)

        for korisnik in TipKorisnika:
            self.tip_korisnika.addItem(str(korisnik.value))

        self.tip_korisnika.setGeometry(QtCore.QRect(150, offset, 150, 25))
        self.tip_korisnika.currentTextChanged.connect(self.occ_korisnik)

        #Label telefon
        self.label_telefon = QtWidgets.QLabel(self)
        self.label_telefon.setFont(self.font)
        self.label_telefon.setText('Telefon')
        self.label_telefon.move(50, offset * 2)

        #Input telefon
        self.text_telefon = QtWidgets.QLineEdit(self)
        self.text_telefon.setGeometry(QtCore.QRect(150, offset * 2, 150, 25))

        #Label email
        self.label_email = QtWidgets.QLabel(self)
        self.label_email.setFont(self.font)
        self.label_email.setText('E-mail')
        self.label_email.move(50, offset * 3)


        #Input email
        self.text_email = QtWidgets.QLineEdit(self)
        self.text_email.setGeometry(QtCore.QRect(150, offset * 3, 150, 25))

        #Label ime
        self.label_ime = QtWidgets.QLabel(self)
        self.label_ime.setFont(self.font)
        self.label_ime.setText('Ime')
        self.label_ime.move(50, offset * 4)

        #Input ime
        self.text_ime = QtWidgets.QLineEdit(self)
        self.text_ime.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))

        #Label prezime
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setFont(self.font)
        self.label_prezime.setText('Prezime')
        self.label_prezime.move(50, offset * 5)

        #Input prezime
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))

        #Label naziv
        self.label_naziv = QtWidgets.QLabel(self)
        self.label_naziv.setFont(self.font)
        self.label_naziv.setText('Naziv')
        self.label_naziv.move(50, offset * 4)
        self.label_naziv.hide()

        # Input naziv
        self.text_naziv = QtWidgets.QLineEdit(self)
        self.text_naziv.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))
        self.text_naziv.hide()

        #Label web
        self.label_web = QtWidgets.QLabel(self)
        self.label_web.setFont(self.font)
        self.label_web.setText('Web')
        self.label_web.move(50, offset * 5)
        self.label_web.hide()

        # Input web
        self.text_web = QtWidgets.QLineEdit(self)
        self.text_web.setGeometry(QtCore.QRect(150, offset * 5, 150, 25))
        self.text_web.hide()

        #Label error korisnik
        self.label_error_k = QtWidgets.QLabel(self)
        self.label_error_k.setFont(self.font)
        self.label_error_k.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_k.setStyleSheet('color : red')
        self.label_error_k.setGeometry(QtCore.QRect(70, offset * 7, 200, 30))

        #Gumb za unos korisnika
        self.unos_korisnika_button = QtWidgets.QPushButton(self)
        self.unos_korisnika_button.setFont(self.font)
        self.unos_korisnika_button.setText('Unesi korisnika')
        self.unos_korisnika_button.setGeometry(QtCore.QRect(100, offset * 8, 150, 30))
        self.unos_korisnika_button.clicked.connect(self.unos_korisnika)

        #Label lista korisnika
        self.label_lista_korisnika = QtWidgets.QLabel(self)
        self.label_lista_korisnika.setFont(self.font)
        self.label_lista_korisnika.setText('Popis korisnika')
        self.label_lista_korisnika.move(15, 270)

        #Lista korisnika
        self.lista_korisnika = QtWidgets.QListWidget(self)
        self.lista_korisnika.setGeometry(15, 300, 290, 150)

        #Gumb za brisanje korisnika
        self.brisanje_korisnika_button = QtWidgets.QPushButton(self)
        self.brisanje_korisnika_button.setFont(self.font)
        self.brisanje_korisnika_button.setText('Obrisi korisnika')
        self.brisanje_korisnika_button.setGeometry(QtCore.QRect(100, 460, 150, 30))
        self.brisanje_korisnika_button.clicked.connect(self.brisanje_korisnika)

        # Okvir za artikle
        self.okvir_artikl = QtWidgets.QFrame(self)
        self.okvir_artikl.setGeometry(310, 10, 300, 500)
        self.okvir_artikl.setFrameStyle(QtWidgets.QFrame.WinPanel)
        self.okvir_artikl.setFrameShadow(QtWidgets.QFrame.Sunken)

        #Label za okvir artikla
        self.label_okvir_artikl = QtWidgets.QLabel(self)
        self.label_okvir_artikl.setFont(self.font_okvir)
        self.label_okvir_artikl.setText('ARTIKL')
        self.label_okvir_artikl.move(315, 12)

        # Input tip artikla
        self.tip_artikla = QtWidgets.QComboBox(self)

        for artikl in TipArtikla:
            self.tip_artikla.addItem(str(artikl.value))

        self.tip_artikla.setGeometry(QtCore.QRect(450, offset, 150, 25))
        self.tip_artikla.currentTextChanged.connect(self.occ_artikl)

        #Label naslov
        self.label_naslov = QtWidgets.QLabel(self)
        self.label_naslov.setFont(self.font)
        self.label_naslov.setText('Naslov')
        self.label_naslov.move(350, offset * 2)

        #Input naslov
        self.text_naslov = QtWidgets.QLineEdit(self)
        self.text_naslov.setGeometry(QtCore.QRect(450, offset * 2, 150, 25))

        #Label opis
        self.label_opis = QtWidgets.QLabel(self)
        self.label_opis.setFont(self.font)
        self.label_opis.setText('Opis')
        self.label_opis.move(350, offset * 3)

        #Input opis
        self.text_opis = QtWidgets.QLineEdit(self)
        self.text_opis.setGeometry(QtCore.QRect(450, offset * 3, 150, 25))

        #Label cijena
        self.label_cijena = QtWidgets.QLabel(self)
        self.label_cijena.setFont(self.font)
        self.label_cijena.setText('Cijena')
        self.label_cijena.move(350, offset * 4)

        #Input cijena
        self.text_cijena = QtWidgets.QLineEdit(self)
        self.text_cijena.setGeometry(QtCore.QRect(450, offset * 4, 150, 25))

        #Label snaga
        self.label_snaga = QtWidgets.QLabel(self)
        self.label_snaga.setFont(self.font)
        self.label_snaga.setText('Snaga')
        self.label_snaga.move(350, offset * 5)

        #Input snaga
        self.text_snaga = QtWidgets.QLineEdit(self)
        self.text_snaga.setGeometry(QtCore.QRect(450, offset * 5, 150, 25))

        #Label kvadratura
        self.label_kvadratura = QtWidgets.QLabel(self)
        self.label_kvadratura.setFont(self.font)
        self.label_kvadratura.setText('Kvadratura')
        self.label_kvadratura.move(350, offset * 5)
        self.label_kvadratura.hide()

        # Input kvadratura
        self.text_kvadratura = QtWidgets.QLineEdit(self)
        self.text_kvadratura.setGeometry(QtCore.QRect(450, offset * 5, 150, 25))
        self.text_kvadratura.hide()

        # Label error artikl
        self.label_error_a = QtWidgets.QLabel(self)
        self.label_error_a.setFont(self.font)
        self.label_error_a.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_a.setStyleSheet('color : red')
        self.label_error_a.setGeometry(QtCore.QRect(370, offset * 7, 200, 30))

        # Gumb za unos artikla
        self.unos_artikla_button = QtWidgets.QPushButton(self)
        self.unos_artikla_button.setFont(self.font)
        self.unos_artikla_button.setText('Unesi artikl')
        self.unos_artikla_button.setGeometry(QtCore.QRect(400, offset * 8, 150, 30))
        self.unos_artikla_button.clicked.connect(self.unos_artikla)

        # Label lista artikla
        self.label_lista_artikla = QtWidgets.QLabel(self)
        self.label_lista_artikla.setFont(self.font)
        self.label_lista_artikla.setText('Popis artikla')
        self.label_lista_artikla.move(315, 270)

        # Lista artikla
        self.lista_artikla = QtWidgets.QListWidget(self)
        self.lista_artikla.setGeometry(315, 300, 290, 150)

        # Gumb za brisanje artikla
        self.brisanje_artikla_button = QtWidgets.QPushButton(self)
        self.brisanje_artikla_button.setFont(self.font)
        self.brisanje_artikla_button.setText('Obrisi artikl')
        self.brisanje_artikla_button.setGeometry(QtCore.QRect(400, 460, 150, 30))
        self.brisanje_artikla_button.clicked.connect(self.brisanje_artikla)

        #Okvir za prodaju
        self.okvir_prodaja = QtWidgets.QFrame(self)
        self.okvir_prodaja.setGeometry(610, 10, 300, 500)
        self.okvir_prodaja.setFrameStyle(QtWidgets.QFrame.WinPanel)
        self.okvir_prodaja.setFrameShadow(QtWidgets.QFrame.Sunken)

        #Label za okvir prodaje
        self.label_okvir_prodaja = QtWidgets.QLabel(self)
        self.label_okvir_prodaja.setFont(self.font_okvir)
        self.label_okvir_prodaja.setText('PRODAJA')
        self.label_okvir_prodaja.move(615, 12)

        #Label korisnik za prodaju
        self.label_korisnik_prodaja = QtWidgets.QLabel(self)
        self.label_korisnik_prodaja.setFont(self.font)
        self.label_korisnik_prodaja.setText('Korisnik')
        self.label_korisnik_prodaja.move(650, offset * 2)

        #Padajući izbornik korisnika
        self.prodaja_tip_korisnika = QtWidgets.QComboBox(self)
        self.prodaja_tip_korisnika.setGeometry(QtCore.QRect(750, offset * 2, 150, 25))

        #Label artikla za prodaju
        self.label_artikl_prodaja = QtWidgets.QLabel(self)
        self.label_artikl_prodaja.setFont(self.font)
        self.label_artikl_prodaja.setText('Artikl')
        self.label_artikl_prodaja.move(650, offset * 3)

        #Padajući izbornik artikla
        self.prodaja_tip_artikla = QtWidgets.QComboBox(self)
        self.prodaja_tip_artikla.setGeometry(QtCore.QRect(750, offset * 3, 150 ,25))

        #Label datum prodaje
        self.label_datum = QtWidgets.QLabel(self)
        self.label_datum.setFont(self.font)
        self.label_datum.setText('Datum')
        self.label_datum.move(650, offset * 4)

        #Datum prodaje
        self.datum_prodaje = QtWidgets.QDateEdit(self)
        self.datum_prodaje.move(750, offset * 4)

        # Gumb za unos prodaje
        self.unos_prodaje_button = QtWidgets.QPushButton(self)
        self.unos_prodaje_button.setFont(self.font)
        self.unos_prodaje_button.setText('Unesi prodaju')
        self.unos_prodaje_button.setGeometry(QtCore.QRect(700, offset * 8, 150, 30))
        self.unos_prodaje_button.clicked.connect(self.unos_prodaje)

        # Label lista artikla
        self.label_lista_prodaje = QtWidgets.QLabel(self)
        self.label_lista_prodaje.setFont(self.font)
        self.label_lista_prodaje.setText('Popis prodaje')
        self.label_lista_prodaje.move(615, 270)

        # Lista artikla
        self.lista_prodaje = QtWidgets.QListWidget(self)
        self.lista_prodaje.setGeometry(615, 300, 290, 150)

        #Label error prodaja
        self.label_error_p = QtWidgets.QLabel(self)
        self.label_error_p.setFont(self.font)
        self.label_error_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_p.setStyleSheet('color : red')
        self.label_error_p.setGeometry(QtCore.QRect(670, offset * 7, 200, 30))

        # Gumb za brisanje artikla
        self.brisanje_prodaje_button = QtWidgets.QPushButton(self)
        self.brisanje_prodaje_button.setFont(self.font)
        self.brisanje_prodaje_button.setText('Obrisi prodaju')
        self.brisanje_prodaje_button.setGeometry(QtCore.QRect(700, 460, 150, 30))
        self.brisanje_prodaje_button.clicked.connect(self.brisanje_prodaje)

        #Skočni prozor
        self.popup_iznimka = QtWidgets.QMessageBox(self)
        self.popup_iznimka.setWindowTitle('Iznimka')
        self.popup_iznimka.setIcon(QtWidgets.QMessageBox.Critical)
        self.popup_iznimka.setStandardButtons(QtWidgets.QMessageBox.Cancel)


    #Brisanje korisnika
    def brisanje_korisnika(self):
        odabrani_korisnik = self.lista_korisnika.currentRow()

        del korisnici[odabrani_korisnik]
        self.lista_korisnika.takeItem(odabrani_korisnik)
        self.prodaja_tip_korisnika.removeItem(odabrani_korisnik)

    #Brisanje artikla
    def brisanje_artikla(self):
        odabrani_artikl = self.lista_artikla.currentRow()

        del artikli[odabrani_artikl]
        self.lista_artikla.takeItem(odabrani_artikl)
        self.prodaja_tip_artikla.removeItem(odabrani_artikl)

    #Brisanje prodaje
    def brisanje_prodaje(self):
        odabrana_prodaja = self.lista_prodaje.currentRow()

        del prodaje[odabrana_prodaja]
        self.lista_prodaje.takeItem(odabrana_prodaja)

    #Promjena tipa korisnika
    def occ_korisnik(self):
        if self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            self.label_naziv.show()
            self.text_naziv.show()
            self.label_web.show()
            self.text_web.show()
            self.label_ime.hide()
            self.text_ime.hide()
            self.label_prezime.hide()
            self.text_prezime.hide()

        elif self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            self.label_naziv.hide()
            self.text_naziv.hide()
            self.label_web.hide()
            self.text_web.hide()
            self.label_ime.show()
            self.text_ime.show()
            self.label_prezime.show()
            self.text_prezime.show()

    #Promjena tipa artikla
    def occ_artikl(self):
        if self.tip_artikla.currentText() == TipArtikla.STAN.value:
            self.label_snaga.hide()
            self.text_snaga.hide()
            self.label_kvadratura.show()
            self.text_kvadratura.show()

        elif self.tip_artikla.currentText() == TipArtikla.AUTOMOBIL.value:
            self.label_snaga.show()
            self.text_snaga.show()
            self.label_kvadratura.hide()
            self.text_kvadratura.hide()


    def unos_korisnika(self):

        if self.tip_korisnika.currentText() == TipKorisnika.PRIVATNI.value:
            error_privatni = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text()
                                                   ,self.text_ime.text(), self.text_prezime.text())
            if error_privatni is None:
                korisnici.append(PrivatniKorisnik(self.text_ime.text(), self.text_prezime.text(),
                                                 self.text_email.text(), self.text_telefon.text()))
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.label_error_k.setText('')

                korisnik = korisnici[len(korisnici) - 1]
                self.lista_korisnika.addItem(f'{korisnik.ime} {korisnik.prezime} {korisnik.email} {korisnik.telefon}')
                self.prodaja_tip_korisnika.addItem(str(korisnik.email))

            else:
                self.label_error_k.setText(error_privatni)
                self.popup_iznimka.setText(error_privatni)
                self.popup_iznimka.exec_()

        elif self.tip_korisnika.currentText() == TipKorisnika.POSLOVNI.value:
            error_poslovni = provjera_korisnickog_unos(self.text_telefon.text(), self.text_email.text()
                                                       , self.text_naziv.text(), self.text_web.text())
            if error_poslovni is None:
                korisnici.append(PoslovniKorisnik(self.text_naziv.text(), self.text_web.text(),
                                              self.text_email.text(), self.text_telefon.text()))
                self.text_telefon.setText('')
                self.text_email.setText('')
                self.text_naziv.setText('')
                self.text_web.setText('')
                self.text_ime.setText('')
                self.text_prezime.setText('')
                self.label_error_k.setText('')

                korisnik = korisnici[len(korisnici)-1]
                self.lista_korisnika.addItem(f'{korisnik.naziv} {korisnik.web} {korisnik.email} {korisnik.telefon}')
                self.prodaja_tip_korisnika.addItem(str(korisnik.email))

            else:
                self.label_error_k.setText(error_poslovni)
                self.popup_iznimka.setText(error_poslovni)
                self.popup_iznimka.exec_()

    def unos_artikla(self):

        if self.tip_artikla.currentText() == TipArtikla.STAN.value:
            error_stan = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(),
                                                self.text_cijena.text(), self.text_kvadratura.text())
            if error_stan is None:
                artikli.append(Stan(self.text_naslov.text(), self.text_opis.text(),
                                                self.text_cijena.text(), self.text_kvadratura.text()))
                self.text_naslov.setText('')
                self.text_opis.setText('')
                self.text_cijena.setText('')
                self.text_kvadratura.setText('')
                self.label_error_a.setText('')

                artikl = artikli[len(artikli) - 1]
                self.lista_artikla.addItem(f'{artikl.naslov} {artikl.opis} {artikl.cijena} {artikl.kvadratura}')
                self.prodaja_tip_artikla.addItem(str(artikl.opis))

            else:
                self.label_error_a.setText(error_stan)
                self.popup_iznimka.setText(error_stan)
                self.popup_iznimka.exec_()

        elif self.tip_artikla.currentText() == TipArtikla.AUTOMOBIL.value:
            error_automobil = provjera_unosa_artikla(self.text_naslov.text(), self.text_opis.text(),
                                                self.text_cijena.text(), self.text_snaga.text())
            if error_automobil is None:
                artikli.append(Automobil(self.text_naslov.text(), self.text_opis.text(),
                                    self.text_cijena.text(), self.text_snaga.text()))
                self.text_naslov.setText('')
                self.text_opis.setText('')
                self.text_cijena.setText('')
                self.text_snaga.setText('')
                self.label_error_a.setText('')

                artikl = artikli[len(artikli) - 1]
                self.lista_artikla.addItem(f'{artikl.naslov} {artikl.opis} {artikl.cijena} {artikl.snaga}')
                self.prodaja_tip_artikla.addItem(str(artikl.opis))

            else:
                self.label_error_a.setText(error_automobil)
                self.popup_iznimka.setText(error_automobil)
                self.popup_iznimka.exec_()

    def unos_prodaje(self):

        error_prodaje = provjera_unosa_prodaje(self.prodaja_tip_korisnika.currentText(),
                                               self.prodaja_tip_artikla.currentText())

        if error_prodaje is None:
            index_korisnika = int(self.prodaja_tip_korisnika.currentIndex())
            index_artikla = int(self.prodaja_tip_artikla.currentIndex())

            prodaje.append(Prodaja(self.datum_prodaje.date(), korisnici[index_korisnika], artikli[index_artikla]))

            prodaja = prodaje[len(prodaje) - 1]
            self.lista_prodaje.addItem(f'{prodaja.artikl.naslov} {prodaja.artikl.opis}')

        else:
            self.label_error_p.setText(error_prodaje)
            self.popup_iznimka.setText(error_prodaje)
            self.popup_iznimka.exec_()



app = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
sys.exit(app.exec_())