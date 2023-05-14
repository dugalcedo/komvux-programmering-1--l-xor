from passenger import Passenger

def validAge(str):
        if not str.isdigit():
            return False
        n = int(str)
        if (n < 0) or (n > 125):
            return False
        return True

def refuseBlankInput(str):
    val = ""
    while val == "":
        val = ""
        val = input(f"{str}: {val}")
        if val == "":
            print("Du måste ange någonting.")
    return val

def refuseInvalidInput(str, validator):
    val = ""
    while (val == "") or (not validator(val)):
        val = ""
        val = input(f"{str}: {val}")
        if val == "" or (not validator(val)):
            print("Det var inte en giltig inmatning.")
    return val


class Buss:

    def __init__(self):
        self.sittplatser = [None, None, None, None, None]
        self.stoppBegärt = False
        pass

    def run(self):
        self.skrivMeny(self.huvudMeny, self.huvudSwitch)

    # E-betyg metoder

    def add_passenger(self):
        if all(self.sittplatser):
            print("Det finns inga lediga sittplatser.")
            self.tillbakaTillHuvudMeny()
            return
        name, age, sex = "","",""
        name = refuseBlankInput("Namn")
        age = refuseInvalidInput("Ålder", validAge)
        sex = refuseBlankInput("Kön (m/f/<något annat>)")
        passenger = Passenger(name, age, sex)
        passenger.chooseSeat(self)
        print(f"{passenger.name} steg på bussen.")
        print(f"{passenger.name} satt på sittplats {passenger.bussIdx+1}.")
        self.tillbakaTillHuvudMeny()

    def print_bus(self):
        print("BUSS")
        for i, seat in enumerate(self.sittplatser):
            print(f"- Sittplats {i+1}")
            if seat:
                print(f"-- Namn: {seat.name}")
                print(f"-- Ålder: {seat.age}")
                print(f"-- Kön: {seat.sex}")
            else:
                print("-- Tom sittplats")
            Buss.mellanrum()
        self.tillbakaTillHuvudMeny()

    def calc_total_age(self):
        total = 0
        for p in self.sittplatser:
            if p:
                total += p.age
        return total
    
    # C-betyg metoder

    def calc_average_age(self):
        numPassengers = self.countPassengers()
        totalAge = self.calc_total_age()
        return totalAge / numPassengers
    
    def minMaxAge(self):
        minAge = 125
        maxAge = 0
        for p in self.sittplatser:
            if p:
                if p.age < minAge:
                    minAge = p.age
                if p.age > maxAge:
                    maxAge = p.age
        return [minAge, maxAge]
    
    def find(self):
        # jag bestämde mig att göra så att "find_age" blir "find" i stället
        # så att användaren kan söka efter andra kategorier också 
        if not any(self.sittplatser):
            print("Det finns inga passagerare att söka.")
            self.tillbakaTillHuvudMeny()
            return
        self.skrivMeny(self.sökMeny, self.sökSwitch, True)

    def sort(self):
        if not any(self.sittplatser):
            print("Det finns inga passagerare att sortera.")
            self.tillbakaTillHuvudMeny()
            return
        if self.countPassengers() < 2:
            print("Det behövs i minst 2 passagerare för att sortera.")
            self.tillbakaTillHuvudMeny()
            return
        self.skrivMeny(self.sortMeny, self.sortSwitch, True)

    # A-betyg metoder

    """
    def print_sex(self):
        pass
        
        Jag bestämde mig att kombinera detta begrepp med print_bus()
        Programmet kan göra detta i alla fall
    """

    def poke(self):
        if not any(self.sittplatser):
            print("Det finns ingen att peta på.")
            self.tillbakaTillHuvudMeny()
            return
        meny = self.skapaPassegerareMeny()
        self.skrivMeny(meny, self.pokeSwitch, True)

    def getting_off(self):
        if not any(self.sittplatser):
            print("Det finns inga passagerare.")
            self.tillbakaTillHuvudMeny()
            return
        self.skrivMeny(self.släppMeny, self.släppSwitch, True)

    # Mina metoder    

    def skrivMeny(self, meny, switch, kanGåTillbaka = False):
        giltigaVal = "0"
        print("_____")
        for alternativ in meny:
            # print(f"ALTERNATIV --- {alternativ}")
            if alternativ == "mellanrum":
                print("|")
                continue
            typ, text = alternativ.split(":")
            if typ.startswith("val"):
                val = typ.replace("val", "")
                print(f"| {val} - {text}")
                giltigaVal += val
                continue
            if typ == "titel":
                    print(f"| --- {text} ---")
        print("|")
        if kanGåTillbaka:
            print("| 0 - Tillbaka till huvudmenyn")
        else:
            print("| 0 - Avsluta programmet")
        print("|-----")
        if self.stoppBegärt:
            print("| # STOPP BEGÄRT #")
            print("|-----")
        val = ""
        while (not val in giltigaVal) or (val == ""):
            val = ""
            val = input(f"| Ange en siffra: {val}")
            if (not val in giltigaVal) or (val == ""):
                print("| ! Det var inte ett giltigt val. !")
        print("`````")
        switch(val)

    def huvudSwitch(self, val):
        Buss.mellanrum()
        match val:
            case "1": # Lägga till
                self.add_passenger()
            case "2": # Släpp av / släng ut
                self.getting_off()
            case "3": # Sortera
                self.sort()
            case "4": # Peta
                self.poke()
            case "5": # Lista passagerare
                self.print_bus()
            case "6": # Statistik
                self.statistics()
            case "7": # Sök
                self.find()
            case "8": # Köra till nästa hållplats
                self.drive()
            case "0": # Avsluta programmet
                print("Hej då!")
                Buss.mellanrum()
    
    def statistics(self):
        if not any(self.sittplatser):
            print("Det finns inga passagerare.")
            self.tillbakaTillHuvudMeny()
            return
        fullness = self.countPassengers() / 5 * 100
        avgAge = self.calc_average_age()
        male, female, other = self.sexStatistics()
        min, max = self.minMaxAge()
        print(f"Bussen är {fullness}% full.")
        print(f"Passagerarna är {male}% manliga.")
        print(f"Passagerarna är {female}% kvinnliga.")
        print(f"Passagerarna är {other}% icke-binära.")
        print(f"Den yngsta passageraren är {min} år gammal.")
        print(f"Den äldsta passageraren är {max} år gammal.")
        print(f"Den genomsnittliga åldern är {avgAge}.")
        self.tillbakaTillHuvudMeny()

    def sexStatistics(self):
        numMale = 0
        numFemale = 0
        numOther = 0
        for p in self.sittplatser:
            if p:
                match p.sex:
                    case "m":
                        numMale += 1
                    case "f":
                        numFemale += 1
                    case _:
                        numOther += 1
        numTotal = self.countPassengers()
        numMale = numMale / numTotal * 100
        numFemale = numFemale / numTotal * 100
        numOther = numOther / numTotal * 100
        return [numMale, numFemale, numOther]

    def pokeSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()
            case _:
                passenger = self.sittplatser[int(val)-1] 
                fras = passenger.fras("poked")
                print(f"{passenger.name} tänker: {fras}")
                self.tillbakaTillHuvudMeny()

    def släppSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()
            case "1": # Släpp av alla
                if not any(self.sittplatser):
                    print("Inga vill gå av.")
                for p in self.sittplatser:
                    if p and p.villStigaAv:
                        print(f"{p.name} gick av bussen.")
                        p.leaveBus(self)
                self.stoppBegärt = False
                self.tillbakaTillHuvudMeny()
            case "2": # Släng ut alla
                for p in self.sittplatser:
                    if p:
                        print(f"{p.name} var tvungen att gå av bussen.")
                        p.leaveBus(self)
                self.stoppBegärt = False
                self.tillbakaTillHuvudMeny()
            case "3": # Släpp viss
                meny = self.skapaPassegerareMeny()
                self.skrivMeny(meny, self.släppVissSwitch, True)

    def släppVissSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()
            case _:
                passenger = self.sittplatser[int(val)-1]
                passenger.leaveBus(self)
                ord = "gick av" if passenger.villStigaAv else "var tvungen att gå av"
                print(f"{passenger.name} {ord} bussen.")
                self.tillbakaTillHuvudMeny()

    def tillbakaTillHuvudMeny(self, skaTryckEnter = True):
        buss.mellanrum()
        if skaTryckEnter:
            input("Tryck enter/return för att fortsätta...")
            buss.mellanrum()
        self.skrivMeny(self.huvudMeny, self.huvudSwitch)

    def drive(self):
        self.stoppBegärt = False
        for passenger in self.sittplatser:
            if passenger:
                passenger.åk()
                if passenger.villStigaAv:
                    self.stoppBegärt = True
                if passenger.arg:
                    argFras = passenger.fras("arg")
                    print(f"{passenger.name} säger: {argFras}")
        print("Bussen har kommit fram till den nätsa hållplatsen.")
        self.tillbakaTillHuvudMeny()

    def skapaPassegerareMeny(self):
        meny = []
        for i, p in enumerate(self.sittplatser):
            if p:
                meny.append(f"val{i+1}:{p.name}")
        return meny
    
    def countPassengers(self):
        numPassengers = 0
        for p in self.sittplatser:
            if p:
                numPassengers += 1
        return numPassengers
    
    def sortSwitch(self, val):
        match val:
            case "0": # tillbaka till huvudmeny
                self.tillbakaTillHuvudMeny()
                return
            case "1": # efter ålder
                self.sittplatser.sort(key=Buss.getPassageraresÅlder)
            case "2": # efter namn
                self.sittplatser.sort(key=Buss.getPassageraresNamn)
        print("Passagerarna sorterades. Välja huvudmenyval 5 för att bekrafta.")
        self.tillbakaTillHuvudMeny()

    def sökSwitch(self, val):
        resultat = []
        match val:
            case "0": # tillbaka till huvudmeny
                self.tillbakaTillHuvudMeny()
                return
            case "1": # efter namn
                namn = refuseBlankInput("Namn")
                for p in self.sittplatser:
                    if p and p.name == namn:
                        resultat.append(p)
            case "2": # efter ålder
                ålder = refuseInvalidInput("Ålder", validAge)
                for p in self.sittplatser:
                    if p and p.age == int(ålder):
                        resultat.append(p)
            case "3": # efter kön
                kön = refuseBlankInput("Kön")
                for p in self.sittplatser:
                    if p and p.sex == kön:
                        resultat.append(p)
        ord = "träff" if len(resultat) == 1 else "träffar"
        print(f"{len(resultat)} {ord} hittades.")
        for r in resultat:
            Buss.mellanrum()
            print(f"- Namn: {r.name}")
            print(f"- Ålder: {r.age}")
            print(f"- Kön: {r.sex}")
        self.tillbakaTillHuvudMeny()


    @staticmethod
    def mellanrum(): print("")

    @staticmethod
    def getPassageraresNamn(passagerare):
        return passagerare.name if passagerare else "zzzzz"
    
    @staticmethod
    def getPassageraresÅlder(passagerare):
        return passagerare.age if passagerare else 126

    huvudMeny = [
            "titel:HUVUD MENY",
            "mellanrum",
            "titel:Hantera passagerare",
            "val1:Lägga till",
            "val2:Släpp av/släng ut",
            "val3:Sortera",
            "val4:Peta",
            "titel:Hämta information",
            "val5:Lista passagerare",
            "val6:Statistik",
            "val7:Sök",
            "mellanrum",
            "val8:Köra till nästa hållplats"
        ]
    
    släppMeny = [
        "titel:SLÄPP MENY",
        "mellanrum",
        "val1:Släpp av alla som vill släppas av",
        "val2:Släng ut alla",
        "val3:Släpp/släng en viss passagerare"
    ]

    sortMeny = [
        "titel:SORTERINGSMENY",
        "mellanrum",
        "val1:Sortera efter ålder",
        "val2:Sortera efter namn"
    ]

    sökMeny = [
        "title:SÖKMENY",
        "mellanrum",
        "val1:Sök efter namn",
        "val2:Sök efter ålder",
        "val3:Sök efter kön"
    ]

buss = Buss()
buss.run()