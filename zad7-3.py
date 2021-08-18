
from faker import Faker
fake=Faker()

class BaseContact:
    def __init__(self, imie, nazwisko, tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.tel = tel
    def __str__ (self):
        return f"{self.imie}, {self.nazwisko}, {self.tel}"
    @property
    def contact(self):
        return f"Wybieram numer {self.tel} i dzwonię do {self.imie}"
    @property
    def label_length(self):           
        return f"Długość imienia i nazwiska razem to {len(self.imie)+len(self.nazwisko)+1} "
class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, tel_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.tel_sluzbowy = tel_sluzbowy
    def __str__ (self):
        return f"{self.imie}, {self.nazwisko}, {self.tel}, {self.stanowisko}, {self.nazwa_firmy}, {self.tel_sluzbowy}"
    @property
    def contact(self):
        return f"Wybieram numer {self.tel_sluzbowy} i dzwonię do {self.imie}"
    @property
    def label_length(self):           
        return f"Długość imienia i nazwiska razem to {len(self.imie)+len(self.nazwisko)+1} "


    
p1=BaseContact(imie="Theresa", nazwisko="McKenzie", tel="4625145216")
p2=BaseContact(imie="Vickie", nazwisko="Koelpin", tel="18968073059")

buissness_p1=BusinessContact(imie="Theresa", nazwisko="McKenzie", tel="4625145216", stanowisko="Internal Research Analyst",nazwa_firmy="Bahringer Inc", tel_sluzbowy="8454707059")
buissness_p2=BusinessContact(imie="Vickie", nazwisko="Koelpin", tel="18968073059", stanowisko="Forward Branding Planner",nazwa_firmy="Bauch - Hickle", tel_sluzbowy="8866965686")

def create_contacts():
    rodzaj = input("czy wizytówka którą chcesz stowrzyć ma być base czy business?")
    ilosc = input("ile wizytówek chcesz stworzyć?")
    if ilosc.isdigit():

        for i in range(int(ilosc)):

            if rodzaj=="base":
                print (f" imie= {fake.name()}, nazwisko= {fake.last_name()}, tel= {fake.phone_number()}")
    
            elif rodzaj=="business":
                print(f" imie= {fake.name()}, nazwisko= {fake.last_name()}, tel= {fake.phone_number()}, stanowisko={fake.job()}, nazwa firmy={fake.company()}, tel_sluzbowy={fake.phone_number()}")
            else:
                print("należy wpisać base lub business")
                exit(1)
    else:
        print("należy podać liczbę")
        exit(1)
        
create_contacts()