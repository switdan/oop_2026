class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec):
        # print(f"Niech powstanie człowiek {imie}")
        self.imie = imie
        self.plec = plec

    def przedstaw_sie(self):
        if self.plec == "M":
            print(f"Mam na imie {self.imie} i jestem Mężczyzną.")
        elif self.plec == "K":
            print(f"Mam na imie {self.imie} i jestem Kobietą.")

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Bawię się!")

    def przedstaw_sie(self):
        if self.plec == "M":
            print(f"Mam na imie {self.imie} i jestem chłopcem.")
        elif self.plec == "K":
            print(f"Mam na imie {self.imie} i jestem dziewczynką.")




adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")
kain = Dziecko("Kain", "M")

 
