import random

class Passenger:
    '''
        När en instans av Passenger skapas ska fem variabler skapas
        Namn, ålder, kön samt..
            villStigaAv - avgör om passageraren vill gå av bussen
            och
            arg - avgör om busschauffören missade passagerarens stopp
        Dessa sista två variablerna ska initialeras som False oavsett init-argumenten
    '''
    def __init__(self, name, age, sex):
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.villStigaAv = False
        self.arg = False

    # med denna funktion kan passageraren "välja" slumpmässigt en sittplats på bussen
    def chooseSeat(self, buss):
        numSeats = len(buss.sittplatser)
        choice = random.randint(0, numSeats - 1)
        while buss.sittplatser[choice]: # medan sittplatsen är "Truthy" (dvs en passagerare redan finns där)...
            choice = random.randint(0, numSeats - 1)
        buss.sittplatser[choice] = self # self bifogas till bussen's sittplatserarray
        self.bussIdx = choice

    def leaveBus(self, buss):
        # bussen's korresponderande sittplats ställs till None
        buss.sittplatser[self.bussIdx] = None

    def åk(self):
        # om passageraren inte redan vill gå av, nu finns det 1 i 4 chans att det blir så
        if not self.villStigaAv:
            if random.randint(1, 4) == 1:
                self.villStigaAv = True
        else: # annars, passageraren vill redan gå av, alltså betyder detta att hens hållplats missades
            self.arg = True

    # funktion för att skriva en av passagerarens två fraser
    # detta har en parameter som kan vara antingen "arg" eller "poked"
    # vilket avgör vilken typ av fras ska skrivas ut
    # passagerarens ålder och kön ska också avgör frasen
    # bebisfraser är samma oavsett kön
    def fras(self, frasTyp):
        åldersGrupp = ""
        # först ta reda på vilken åldersgrupp passageraren hör
        if self.age < 4:
            åldersGrupp = "bebis"
        elif self.age < 13:
            åldersGrupp = "barn"
        elif self.age < 20:
            åldersGrupp = "tonårig"
        else:
            åldersGrupp = "vuxen"
        # sedan om passageraren är varken manlig eller kvinnlig...
        if not self.sex == "m" and not self.sex == "f":
            return self.fraser[åldersGrupp]["o"][frasTyp] # använd en icke-binär fras
        else: # annars använd en m eller f fras
            return self.fraser[åldersGrupp][self.sex][frasTyp]

    # statisk variabel med alla fraserna
    fraser = {
        "bebis": {
            "m": {
                "arg": "waaa! waaaa!",
                "poked": "googoo gaga"
            },
            "f": {
                "arg": "waaa! waaaa!",
                "poked": "googoo gaga"
            },
            "o": {
                "arg": "waaa! waaaa!",
                "poked": "googoo gaga"
            }
        },
        "barn": {
            "m": {
                "arg": "Va!? Var är vi?",
                "poked": "Jag vill inte gå till skola idag"
            },
            "f": {
                "arg": "Åh nej! Det var min stopp...",
                "poked": "Jag hoppas att jag inte få för mycket läxor"
            },
            "o": {
                "arg": "Men jag behöver gå av bussen här!",
                "poked": "Jag vill ha pizza till lunch idag"
            }
        },
        "tonårig": {
            "m": {
                "arg": "Är du dum i huvudet? Jag tryckte knappen!",
                "poked": "Skolan blir så jobbigt nufortiden"
            },
            "f": {
                "arg": "Du! Stanna snälla!",
                "poked": "Mina vänner stör mig"
            },
            "o": {
                "arg": "Åh nej-- Ursäkta!!!",
                "poked": "Det här är så tråkigt"
            }
        },
        "vuxen": {
            "m": {
                "arg": "Du, busschaufför! Såg du inte skylten?",
                "poked": "Jag blir åksjuk."
            },
            "f": {
                "arg": "Nämen.. chaufför! Kan du stanna?!",
                "poked": "Chauffören kör jättebra"
            },
            "o": {
                "arg": "Oj! Skojar du? Min hållplats!",
                "poked": "Vädret är skönt i dag"
            }
        }
    }
