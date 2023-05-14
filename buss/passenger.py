import random

class Passenger:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.villStigaAv = False
        self.arg = False

    def chooseSeat(self, buss):
        numSeats = len(buss.sittplatser)
        choice = random.randint(0, numSeats - 1)
        while buss.sittplatser[choice]:
            choice = random.randint(0, numSeats - 1)
        buss.sittplatser[choice] = self
        self.bussIdx = choice

    def leaveBus(self, buss):
        buss.sittplatser[self.bussIdx] = None

    def åk(self):
        if not self.villStigaAv:
            if random.randint(1, 4) == 1:
                self.villStigaAv = True
        else:
            self.arg = True

    def fras(self, frasTyp):
        åldersGrupp = ""
        if self.age < 4:
            åldersGrupp = "bebis"
        elif self.age < 13:
            åldersGrupp = "barn"
        elif self.age < 20:
            åldersGrupp = "tonårig"
        else:
            åldersGrupp = "vuxen"
        if not self.sex == "m" and not self.sex == "f":
            return self.fraser[åldersGrupp]["o"][frasTyp]
        else:
            return self.fraser[åldersGrupp][self.sex][frasTyp]

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
