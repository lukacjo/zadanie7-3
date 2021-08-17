class BaseContact:
    def __init__(self, imie, nazwisko, tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.tel = tel

class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, tel_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.tel_sluzbowy = tel_sluzbowy
    def __str__ (self):
        return f"{self.imie} {self.nazwisko} {self.tel} {self.stanowisko} {self.nazwa_firmy} {self.tel_sluzbowy}"

