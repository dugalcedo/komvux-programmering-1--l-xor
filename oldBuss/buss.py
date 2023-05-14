import random
from passagerare import Passagerare

def space():
    print("")

class Buss:
    passagerare = []
    antal_passagerare = 0
    sittplatser = [False, False, False, False, False]
    stanna = False

    def run(self):  
        print("Välkommen till Buss-simulatorn.")
        self.skrivUtMenyn()

    # E

    def add_passanger(self):
        space()
        if all(self.sittplatser):
            print("Inga sittplatser är lediga. Släpp av eller släng ut en passagerare.")
            Buss.fortsätt()
            self.skrivUtMenyn()
            return
        namn, ålder, kön = "", "", ""
        print("Ange passagerares information")
        while not namn:
            namn = input(f"Namn: {namn}")
        while not ålder:
            ålder = input(f"Ålder: {ålder}")
            if not Buss.giltigÅlder(ålder):
                ålder = ""
                print("Ogiltig ålder")
        while not kön:
            kön = input(f"Kön: {kön}")
        nyPassagerare = Passagerare(namn, ålder, kön)
        self.antal_passagerare += 1
        self.passagerare.append(nyPassagerare)
        sittande = False
        sittplats = False
        while not sittande:
            sittplats = random.randint(0, len(self.sittplatser) - 1)
            sittande = not self.sittplatser[sittplats]
        self.sittplatser[sittplats] = nyPassagerare
        nyPassagerare.plats = sittplats
        print(f"{namn} har satt sig i sittplats #{sittplats+1}.")
        Buss.fortsätt()
        self.skrivUtMenyn()

    def print_buss(self):
        space()
        for idx, passagerare in enumerate(self.sittplatser):
            print(f"Sittplats {idx+1}")
            if passagerare:
                print(f"- Namn: {passagerare.namn}")
                print(f"- Ålder: {passagerare.ålder}")
                print(f"- Kön: {passagerare.kön}")
                print(f"- Plats: {passagerare.plats+1}")
            else:
                print("- [tom sittplats]")
        Buss.fortsätt()
        self.skrivUtMenyn()
        

    def calc_total_age(self):
        total = 0
        for p in self.passagerare:
            total += int(p.ålder)
        return total


    # C

    def calc_average_age(self):
        total = self.calc_total_age()
        return total / self.antal_passagerare

    def max_age(self):
        age = 0
        for p in self.passagerare:
            if p.ålder > age:
                age = p.ålder
        return age

    def min_age(self):
        age = 125
        for p in self.passagerare:
            if p.ålder < age:
                age = p.ålder
        return age

    def find_age(self, age):
        filtered = []
        if "-" in age:
            if age.count('-') > 1:
                print("Ogiltigt åldersintervall")
                Buss.fortsätt()
                self.skrivUtMenyn()
                return
            ageRange = age.split('-')
            for a in ageRange:
                if not Buss.giltigÅlder(a):
                    print("Ogiltigt åldersintervall")
                    Buss.fortsätt()
                    self.skrivUtMenyn()
                    return
            min, max = ageRange
            min = int(min)
            max = int(max)
            filtered = filter(lambda p : Buss.mellan(min, max, p), self.passagerare)
        elif Buss.giltigÅlder(age):
            age = int(age)
            filtered = filter(lambda p : Buss.ageFilter(age, p), self.passagerare)
        else: 
            print("Ogiltigt ålder")
            Buss.fortsätt()
            self.skrivUtMenyn()
            return
        return filtered

    def sort_buss(self):
        # Sortera bussen efter ålder. Tänk på att du inte kan ha tomma positioner "mitt i" vektorn.
        #         
	# Man ska kunna sortera vektorn med bubble sort
        pass


    # A

    def print_sex(self):
        # Betyg A
        # Denna metod är nödvändigtvis inte svårare än andra metoder men kräver att man skapar en klass för passagerare.
        # Skriv ut vilka positioner som har manliga respektive kvinnliga passagerare.
        pass

    def poke(self):
        space()
        print("Vilken passagerare vill du peta på?")
        giltigaVal = "0"
        for i, p in enumerate(self.passagerare):
            print(f"- {i+1} - {p.namn}")
            giltigaVal += str(i+1)
        print("- 0 - ingen")
        val = ""
        val = input(f"Skriv en siffra: {val}")
        while not val or (val not in giltigaVal):
            print(f'"{val}" är inte ett giltigt menyval.')
            val = ""
            val = input(f"Skriv en siffra: {val}")
        if val == "0":
            pass
        else:
            p = self.passagerare[int(val)-1]
            print(f"{p.namn} säger: {p.petaFras()}")

    def getting_off(self, str):
        space()
        match str:
            case "släpp-alla":
                nyaPassagerare = []
                for p in self.passagerare:
                    if p.villStigaAv:
                        self.sittplatser[p.plats] = False
                        print(f"{p.namn} gick av bussen.")
                    else:
                        nyaPassagerare.append(p)
                self.passagerare = nyaPassagerare
                self.stanna = False
                Buss.fortsätt()
                self.skrivUtMenyn()
            case "släng-alla":
                self.passagerare = []
                self.stanna = False
                self.sittplatser = [False, False, False, False, False]
                print("Alla passagerare ombads att gå av. Bussen är nu tom.")
                Buss.fortsätt()
                self.skrivUtMenyn()
            case "släpp-viss":
                print("Vilken passagerare vill du släppa av?")
                giltigaVal = "0"
                for i, p in enumerate(self.passagerare):
                    print(f"- {i+1} - {p.namn}")
                    giltigaVal += str(i+1)
                print("- 0 - Ingen")
                val = ""
                val = input(f"Skriv en siffra: {val}")
                while not val or (val not in giltigaVal):
                    print(f'"{val}" är inte ett giltigt menyval.')
                    val = ""
                    val = input(f"Skriv en siffra: {val}")
                if val == "0":
                    Buss.fortsätt()
                    self.skrivUtMenyn()
                    return
                self.sittplatser[int(val) - 1] = False
                



    # mina metoder

    def skrivUtMenyn(self):
        space()
        print("____________________________________")
        print("| ===== MENY ===== ")
        print("|-- Hantera passagerare")
        print("|  1   Lägga till")
        print("|  2   Peta på")
        print("|  3   Sortera")
        print("|  4   Släpp av/släng ut")
        print("|-- Hämta information --")
        print("|  5   Lista passagerare")
        print("|  6   Hämta genomsnittliga/totala åldern")
        print("|  7   Hämta min/max åldern")
        print("|  8   Söka passagerare efter ålder")
        print("|  9   Söka passagerare efter kön")
        print("|  0   Avsluta")
        print("|  k   Köra till den nästa hållplatsen")
        print("|___________________________________")
        if self.stanna:
            print("************************************")
            print("********** STOP REQUESTED **********")
            print("************************************")
        val = ""
        val = input(f"Vad vill du göra? Skriv en siffra: {val}")
        giltigaVal = "0123456789k"
        while not val or (val not in giltigaVal):
            print(f'"{val}" är inte ett giltigt menyval.')
            val = ""
            val = input(f"Vad vill du göra? Skriv en siffra: {val}")
        self.menySwitch(val)
    
    def menySwitch(self, n):
        match n:
            case "1": # lägga till
                self.add_passanger()
            case "2": # peta på
                self.poke()
            case "4": # släpp/släng
                self.släppMeny()
            case "5": # lista passagerare
                self.print_buss()
            case "6": # hämta genomsnittliga/totala åldern
                space()
                if self.antal_passagerare < 1:
                    print("Det fins inga passagerare.")
                else:
                    print(f"Totala åldern: {self.calc_total_age()}")
                    print(f"Genomsnittliga åldern: {self.calc_average_age()}")
                Buss.fortsätt()
                self.skrivUtMenyn()
            case "7":
                space()
                print(f"Max age: {self.max_age()}")
                print(f"Min age: {self.min_age()}")
                Buss.fortsätt()
                self.skrivUtMenyn()
            case "8":
                space()
                age = ""
                age = input(f"Ange en ålder eller åldersintervall. (tex. 25 eller 18-35): {age}")
                filtered = list(self.find_age(age))
                if len(filtered):
                    space()
                    print(f"Passagerare av åldern {age} är...")
                    for p in filtered:
                        print(f"- {p.namn}")
                else:
                    print("Inga resultat")
                Buss.fortsätt()
                self.skrivUtMenyn()
            case "k": # köra till den nästa hållplatsen
                self.nästaHållplats()

    def släppMeny(self):
        space()
        print("____________________________________")
        print("| ===== SLÄPPMENY ===== ")
        print("|  1   Släpp av alla som vill släpps av")
        print("|  2   Släng ut alla passagerare")
        print("|  3   Släpp av/släng ut en viss passagerare")
        print("|")
        print("|  0   Tillbaka till huvudmeny")
        print("|___________________________________")
        val = ""
        val = input(f"Vad vill du göra? Skriv en siffra: {val}")
        giltigaVal = "0123"
        while not val or (val not in giltigaVal):
            print(f'"{val}" är inte ett giltigt menyval.')
            val = ""
            val = input(f"Vad vill du göra? Skriv en siffra: {val}")
        self.släppSwitch(val)

    def släppSwitch(self, n):
        match n:
            case "1":
                self.getting_off("släpp-alla")

    def nästaHållplats(self):
        space()
        print("Vi har kommit fram till den nästa hållplatsen")
        for p in self.passagerare:
            p.åk()
            if p.arg:
                space()
                print(f"Passageraren {p.namn} säger: {p.argFras()}")
                space()
            p.slumpmässigtViljaStigaAv()
            if p.villStigaAv:
                self.stanna = True
        Buss.fortsätt()
        self.skrivUtMenyn()


    @staticmethod
    def fortsätt():
        space()
        input("Tryck enter/return för att fortsätta.")

    @staticmethod
    def giltigÅlder(str):
        if not str.isdigit():
            return False
        n = int(str)
        if (n < 0) or (n > 125):
            return False
        return True
    
    @staticmethod
    def mellan(min, max, passagerare):
        return passagerare.ålder <= max and passagerare.ålder >= min

    @staticmethod
    def ageFilter(age, passagerare):
        return age == passagerare.ålder