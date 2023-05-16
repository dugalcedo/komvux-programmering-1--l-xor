from passenger import Passenger

'''
    validAge
    Denna metod tar in en sträng och kontrollera att det är en giltigt ålder.
    Först konverterar det strängen till ett heltal. 
    Sedan kontrollerar det att heltalet är mellan 0 och 125.
    Är det så returera metoden True, annars False.
'''
def validAge(str):
        if not str.isdigit():
            return False
        n = int(str)
        if (n < 0) or (n > 125):
            return False
        return True

'''
    refuseBlankInput
    Denna metod initialerar en tom sträng "val" och ber användaren om en inmatning.
    Om inmatningen är tom, ett meddelande skrivs ut.
    Annars blir "val" inmatningen.
    Val retureras.
'''
def refuseBlankInput(str):
    val = ""
    while val == "":
        val = ""
        val = input(f"{str}: {val}")
        if val == "":
            print("Du måste ange någonting.")
    return val

'''
    refuseInvalidInput
    Denna medtod kombinerar de två förra metoderna.
    Det håller på att be användaren om en inmatning.
    Så länge inmatningen är tom ELLER en angiven "validator" funktion returera False ska metoden be om igen.
    Validatorn ska vara en metod som tar in en sträng och returera en boolean om strängen är giltig.
    Bussen använder denna metod en gång, för att få en giltig ålder.
'''
def refuseInvalidInput(str, validator):
    val = ""
    while (val == "") or (not validator(val)):
        val = ""
        val = input(f"{str}: {val}")
        if val == "" or (not validator(val)):
            print("Det var inte en giltig inmatning.")
    return val


'''
    Hur bussen struktureras
        E-, C-, och A-betygsmetoder markeras. De kommer först.
        Sedan kommer mina extra metoder.
        Sedan några statiska variabler och metoder.
'''

class Buss:

    def __init__(self):
        '''
            När bussen initialeras, så initialeras även två variabler:
            1. sittplatser, som ska representerar de fem sittplatserna på bussen.
                - om en sittplats är tom, ska det vara None, annars en instans av Passagerare classen
            2. stoppBegärt, som representerar om en passagerare har tryckt en "stoppknapp" på bussen
                - det är 1 i 4 chans att en passagerare trycka knappet varje "hållplats"
                - varje gång du öppna dörrarna på bussen är denna variabel sätts om till False
        '''
        self.sittplatser = [None, None, None, None, None]
        self.stoppBegärt = False
        pass

    def run(self):
        # Se på skrivMeny i "mina metoder"
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


    '''
    skrivMeny
    Detta är kanske bussens "viktigaste" metoden
    Det kan ta in olika parametrar för att skriva ut olika menyer med olika funktioner
    "meny" ska vara en array av strängar
    "switch" ska vara en funktion som ta in en sträng och innehåller en match-case för att göra olika saker beroende på strängen
    "kanGåTillbaka" är frivilligt, men om True ska menyn ha ett val för att gå tillbaka till huvudmenyn
        3 typer av menysträngar
            1. "mellanslag" - skapar en ny rad i menyn
            2. "titel:_" - skapar en titel i menyn
            3. "val_:" - skapar ett giltigt val i menyn
                se statiska varabler nedan för exempel
    '''
    def skrivMeny(self, meny, switch, kanGåTillbaka = False):
        # "giltigaVal" ska senare inehålla alla de tecken som kan användas i swtichen
        # alla menyerna ska ha åtminstone 0 som ett val, antingen för att avsluta eller gå tillbacka till huvudmenyn
        giltigaVal = "0"
        print("_____")

        # "alternativ" är varje sträng i menyarrayen
        # här hanteras alla de tre eventuella menysträngerna
        for alternativ in meny:
            if alternativ == "mellanrum":
                print("|")
                continue
            typ, text = alternativ.split(":")
            if typ.startswith("val"):
                val = typ.replace("val", "")
                print(f"| {val} - {text}")
                # Viktigt: "val" läggs till "giltigaVal" strängen
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

        # om en passagerare "tryckte knappen" ska "stopp begärt" visas i varje meny
        if self.stoppBegärt:
            print("| # STOPP BEGÄRT #")
            print("|-----")

        # här hämtas användarens menyval
        # while-loopen förhindra programmet från att fortsätta tills användaren anger ett giltigt val
        val = ""
        while (not val in giltigaVal) or (val == ""):
            val = ""
            val = input(f"| Ange en siffra: {val}")
            if (not val in giltigaVal) or (val == ""):
                print("| ! Det var inte ett giltigt val. !")


        print("`````")
        # nu användaren har angett ett giltigt val
        # så anropas en "switch-funktion"
        switch(val)

    # switch-funktion som förknippas med huvudmenyn
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
    
    # skriver ut bussens statistik
    def statistics(self):
        # statistiken ska inte skrivas ut om det inte finns passagerare
        if not any(self.sittplatser):
            print("Det finns inga passagerare.")
            self.tillbakaTillHuvudMeny()
            return
        
        # procent av sittplatser upptagna
        fullness = self.countPassengers() / 5 * 100
        # genomsnittliga åldern
        avgAge = self.calc_average_age()
        # sexStatistics returera en array. här destruktureras det.
        male, female, other = self.sexStatistics()
        # samma med minMaxAge
        min, max = self.minMaxAge()

        # skriv ut och gå tillbaka till huvudmenyn
        print(f"Bussen är {fullness}% full.")
        print(f"Passagerarna är {male}% manliga.")
        print(f"Passagerarna är {female}% kvinnliga.")
        print(f"Passagerarna är {other}% icke-binära.")
        print(f"Den yngsta passageraren är {min} år gammal.")
        print(f"Den äldsta passageraren är {max} år gammal.")
        print(f"Den genomsnittliga åldern är {avgAge}.")
        self.tillbakaTillHuvudMeny()

    # kalkulera könstatistik
    def sexStatistics(self):
        # initialera antal manliga, antal kvinnliga, och antal övriga till 0
        numMale = 0
        numFemale = 0
        numOther = 0

        # för varje sittplats...
        for p in self.sittplatser:
            # om sittplats har en passagerare...
            if p:
                # öka det lämpliga värde
                match p.sex:
                    case "m":
                        numMale += 1
                    case "f":
                        numFemale += 1
                    case _:
                        numOther += 1

        # hämta antal passagerare för att jämföra med
        numTotal = self.countPassengers()
        numMale = numMale / numTotal * 100
        numFemale = numFemale / numTotal * 100
        numOther = numOther / numTotal * 100
        # returnera värde som kan lätt skrivas ut som procent
        # denna array kan destruktureras senare
        return [numMale, numFemale, numOther]

    # switchfunktion som förknippas med poke-menyn
    def pokeSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()
            case _:
                # hämta passagerare som sitter i sittplatsen
                passenger = self.sittplatser[int(val)-1] 
                # hämta poke-frasen och skriv ut, sedan gå tillbaka
                fras = passenger.fras("poked")
                print(f"{passenger.name} tänker: {fras}")
                self.tillbakaTillHuvudMeny()

    # switchfunktion som förknippas med släppmenyn
    def släppSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()

            case "1": # Släpp av alla
                if not any(self.sittplatser):
                    print("Inga vill gå av.")
                # för varje sittplats...
                for p in self.sittplatser:
                    # om sittplatsen är upptagen OCH passageraren där vill gå av...
                    if p and p.villStigaAv:
                        print(f"{p.name} gick av bussen.")
                        p.leaveBus(self)
                # sätta om "stoppskylten" och gå tillbaka till huvudmenyn
                self.stoppBegärt = False
                self.tillbakaTillHuvudMeny()

            case "2": # Släng ut alla
                # för varje sittplats...
                for p in self.sittplatser:
                    # om sittplatsen är upptagen...
                    if p:
                        print(f"{p.name} var tvungen att gå av bussen.")
                        p.leaveBus(self)
                # sätta om "stoppskylten" och gå tillbaka till huvudmenyn
                self.stoppBegärt = False
                self.tillbakaTillHuvudMeny()

            case "3": # Släpp viss
                # kapa en passageraremeny och skriv ut det
                # koppla släppVissSwitch till det
                meny = self.skapaPassegerareMeny()
                self.skrivMeny(meny, self.släppVissSwitch, True)

    # släppVissSwitch för att släpp av / släng ut en viss passagerare
    def släppVissSwitch(self, val):
        match val:
            case "0":
                self.tillbakaTillHuvudMeny()
            case _:
                # hämta passagerare och få hen att lämna bussen sen gå tillbaka till huvudmeny
                passenger = self.sittplatser[int(val)-1]
                passenger.leaveBus(self)
                ord = "gick av" if passenger.villStigaAv else "var tvungen att gå av"
                print(f"{passenger.name} {ord} bussen.")
                self.tillbakaTillHuvudMeny()

    # funktion för att gå tillbaka till huvudmenyn
    def tillbakaTillHuvudMeny(self, skaTryckEnter = True):
        buss.mellanrum()
        # denna funktion har alternativet att gå tillbaka till huvudmenyn utan att utmana användaren att tryck enter
        # i slutändan använde jag inte detta
        if skaTryckEnter:
            input("Tryck enter/return för att fortsätta...")
            buss.mellanrum()
        self.skrivMeny(self.huvudMeny, self.huvudSwitch)

    # funktion för att "köra bussen till nästa hållplats"
    def drive(self):
        # "stoppskylten" sätts om varje körning
        self.stoppBegärt = False
        # för varje sittplats...
        for passenger in self.sittplatser:
            # om sittplatsen är upptagen...
            if passenger:
                passenger.åk()
                if passenger.villStigaAv:
                    self.stoppBegärt = True
                # om passageraren inte släpptes av när hen ville, en "argfras" ska srivas ut
                if passenger.arg:
                    argFras = passenger.fras("arg")
                    print(f"{passenger.name} säger: {argFras}")
        print("Bussen har kommit fram till den nätsa hållplatsen.")
        self.tillbakaTillHuvudMeny()

    # skapar en menyarray av de aktuella passagerarna
    def skapaPassegerareMeny(self):
        meny = []
        for i, p in enumerate(self.sittplatser):
            if p:
                meny.append(f"val{i+1}:{p.name}")
        return meny
    
    # returera antal sittplatser som är "truthy" (har en passagerare)
    def countPassengers(self):
        numPassengers = 0
        for p in self.sittplatser:
            if p:
                numPassengers += 1
        return numPassengers
    
    # switchfunktionen som förknippas med sortmenyn
    # här använder jag "key=" för att sortera efter variabler på objekt
    def sortSwitch(self, val):
        match val:
            case "0": # tillbaka till huvudmeny
                self.tillbakaTillHuvudMeny()
                return
            case "1": # efter ålder
                self.sittplatser.sort(key=Buss.getPassageraresÅlder)
            case "2": # efter namn
                self.sittplatser.sort(key=Buss.getPassageraresNamn)
        # berätta för användaren hur hen kan se på den nya sorteringen
        print("Passagerarna sorterades. Välja huvudmenyval 5 för att bekrafta.")
        self.tillbakaTillHuvudMeny()

    # switchfunktionen för sökmenyn
    def sökSwitch(self, val):
        # initialera en array för de relevanta passagerarna
        # beroende på användarens val ska denna array inehålla passagerare som matchar en inmatning
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
        # om det finns bara en träff så jag vill att det skriva "träff" annars "träffar"
        ord = "träff" if len(resultat) == 1 else "träffar"
        print(f"{len(resultat)} {ord} hittades.")
        # skriv ut varje träff
        for r in resultat:
            Buss.mellanrum()
            print(f"- Namn: {r.name}")
            print(f"- Ålder: {r.age}")
            print(f"- Kön: {r.sex}")
        self.tillbakaTillHuvudMeny()

    # för att skriva ut tomma rad
    @staticmethod
    def mellanrum(): print("")

    # funktioner för att sortera efter namn och ålder. om sittplatsen är tom, returera något som ska få sittplatsen att sorteras sist 
    @staticmethod
    def getPassageraresNamn(passagerare):
        return passagerare.name if passagerare else "zzzzz"
    
    @staticmethod
    def getPassageraresÅlder(passagerare):
        return passagerare.age if passagerare else 126

    # nedan finns de menyarrayerna som ska behandlas av funktionen skrivMeny
    # se "skrivMeny" för mer information

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
        "titel:SÖKMENY",
        "mellanrum",
        "val1:Sök efter namn",
        "val2:Sök efter ålder",
        "val3:Sök efter kön"
    ]

buss = Buss()
buss.run()